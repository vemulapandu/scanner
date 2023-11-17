import click
import os
from scanner.services import checks

class Context:
    def __init__(self, path):
        self.path = path
        self.checks = checks.Checks()
        pass

@click.command()
@click.option("-p", "--path", type=str, help="Path of the apk")
@click.pass_context
def cli(ctx, path):
    if not path:
        path = os.getcwd()
    ctx.obj = Context(path)
    # click.echo(ctx.obj.path)
    # click.echo(ctx.obj.checks.isValid(ctx.obj.path))
    if not ctx.obj.checks.isValid(ctx.obj.path):
        click.secho("Please give a valid path to apk", bg="red")
    ctx.obj.checks.scan(ctx.obj.path)