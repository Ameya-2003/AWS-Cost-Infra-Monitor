import typer
from monitor.cost import fetch_cost
from monitor.infra import check_infra

app = typer.Typer()

@app.command()
def cost():
    """Get daily AWS cost report"""
    fetch_cost()

@app.command()
def infra():
    """Check EC2 instance health"""
    check_infra()

if __name__ == "__main__":
    app()
