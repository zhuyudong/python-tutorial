from rich import print
from rich.console import Console
from rich.progress import Progress
from rich.prompt import Prompt

# from rich.style import Style
from rich.table import Table

console = Console()
table = Table(show_header=True, header_style="bold magenta")

# NOTE: locals() returns a dictionary of the current local symbol table
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")  # Hello, World! 🧛
print("[bold]Hello[/bold], [italic]world[/italic]!")  # Hello, world!
print("[red]This is[/red] [blue]colorful[/blue].")  # This is colorful.

print("[green]------------------------------------------------------------[/green]")

table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_row("2020-12-01", "Test", "$5,000.00")
table.add_row("2020-12-02", "Test", "$5,000.00")
console.print(table)
# +------------+-------+---------------------+
# | Date       | Title | Production Budget   |
# +------------+-------+---------------------+
# | 2020-12-01 | Test  |          $5,000.00  |
# | 2020-12-02 | Test  |          $5,000.00  |
# +------------+-------+---------------------+

print("[green]------------------------------------------------------------[/green]")

with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=100000)
    while not progress.finished:
        progress.update(task, advance=1)
print("[green]------------------------------------------------------------[/green]")

markdown_text = """
# Welcome to My CLI App

This is a **Markdown** text rendered using [Rich](https://github.com/willmcgugan/rich).
- You can use lists.
- You can add [links](https://github.com/willmcgugan/rich).
- You can emphasize text.
"""
print(markdown_text)

print("[green]------------------------------------------------------------[/green]")

source_code = """
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(hello("World"))
"""
print(source_code, "python")

print("[green]------------------------------------------------------------[/green]")

choice = Prompt.ask("Pick a color", choices=["red", "green", "blue"])
console.print(f"[{choice}]You picked: {choice}[/{choice}]")

print("[green]------------------------------------------------------------[/green]")

# FIXME
# custom_style = Style.parse(color="white", on_color="green", bold=True, italic=True)

# print("[bold]Hello[/bold], [italic]world[/italic]!", style=custom_style)  # Hello, world!
