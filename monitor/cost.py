import boto3
import datetime
from rich.table import Table
from rich.console import Console

def fetch_cost():
    client = boto3.client("ce")

    # Calculate time range: first of month to today
    today = datetime.date.today()
    start = today.replace(day=1).isoformat()
    end = today.isoformat()

    try:
        response = client.get_cost_and_usage(
            TimePeriod={"Start": start, "End": end},
            Granularity="DAILY",
            Metrics=["UnblendedCost"]
        )

        table = Table(title="AWS Daily Cost Report")
        table.add_column("Date", style="cyan")
        table.add_column("Cost (USD)", style="magenta")

        for day in response["ResultsByTime"]:
            date = day["TimePeriod"]["Start"]
            cost = day["Total"]["UnblendedCost"]["Amount"]
            table.add_row(date, f"${float(cost):.2f}")

        console = Console()
        console.print(table)

    except Exception as e:
        print(f"[ERROR] Failed to fetch cost data: {e}")
