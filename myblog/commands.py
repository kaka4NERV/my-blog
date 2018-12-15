import click
from myblog import create_app
from myblog.models import db

app = create_app()


@app.cli.command()
def initdb():
    db.create_all()
    click.echo('Initialized database.')