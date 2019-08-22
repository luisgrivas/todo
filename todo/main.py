import click
from utils import create_db, create_dir

@click.group()
def todo():
	pass

@todo.command()
def init():
	create_dir()
	create_db()
	click.echo("ToDo project initialized!")


@todo.command()
def add():
	click.echo("Aqui agrego tareas")


@todo.command()
def log():
	click.echo("historia")


if __name__ == '__main__':
	todo()