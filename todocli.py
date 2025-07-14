import typer
from rich.console import Console
from rich.table import Table
from model import Todo  # Assuming you have a models.py with a Todo class
from database import insert_todo, get_all_todos, update_todo, delete_todo, change_position, complete_todo


console = Console()
app = typer.Typer()

@app.command(short_help='add a task to the todo list')
def add(task: str, category: str):
    typer.echo(f"Added task: {task} to category: {category}")

    todo = Todo(id=None, task=task, category=category)
    insert_todo(todo)
    show()
@app.command()
def delete(position: int):
    typer.echo(f"Deleted task at position: {position}")
    delete_todo(position-1)
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"Updated task at position {position} with new task: {task} and category: {category}")
    update_todo(position-1, task=task, category=category)
    show()

@app.command()
def complete(position: int):
    typer.echo(f"Marked task at position {position} as complete")
    complete_todo(position-1)

    show()

def get_category_color(category: str) -> str:
    colors = {
        "Reading": "bold blue",
        "Writing": "bold green",
        "Coding": "bold yellow",
    }
    return colors.get(category, "bold white")

@app.command()
def show():
    tasks = get_all_todos()
    console.print("[bold magenta]Your TODO List[/bold magenta]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Position", style="dim", width=6)
    table.add_column("Task", style="dim", width=20)
    table.add_column("Category", style="dim", width=20)
    table.add_column("Status", style="dim", width=10)
    for i, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = "No" if task.status == 1 else "Yes"
        table.add_row(str(i), task.task, task.category, is_done_str, style=c)
    console.print(table)
       

if __name__ == "__main__":
    app()