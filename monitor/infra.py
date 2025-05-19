import boto3
from rich.console import Console
from rich.table import Table

def check_infra():
    ec2 = boto3.client("ec2")
    console = Console()

    try:
        statuses = ec2.describe_instance_status(IncludeAllInstances=True)

        table = Table(title="EC2 Instance Status")
        table.add_column("Instance ID", style="green")
        table.add_column("State", style="cyan")
        table.add_column("System Status", style="yellow")
        table.add_column("Instance Status", style="magenta")

        for inst in statuses["InstanceStatuses"]:
            table.add_row(
                inst["InstanceId"],
                inst["InstanceState"]["Name"],
                inst["SystemStatus"]["Status"],
                inst["InstanceStatus"]["Status"]
            )

        if len(statuses["InstanceStatuses"]) == 0:
            console.print("[bold red]No EC2 instances found.[/bold red]")
        else:
            console.print(table)

    except Exception as e:
        print(f"[ERROR] Failed to fetch EC2 status: {e}")
