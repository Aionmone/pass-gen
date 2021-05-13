# Third party package
import click

# pass_gen packages
import pass_gen

def version(ctx, param, value):
    '''
    Show version
    '''
    if not value or ctx.resilient_parsing:
        return
    click.echo(pass_gen.__version__)
    ctx.exit()

@click.command()
@click.option('-v', '--version', is_flag=True, callback=version,
                expose_value=False, is_eager=True, help='Show version')
@click.option('-l', '--length', type=click.IntRange(8, 16), default=12, metavar='', help='Password length [8 - 16]')
def cli(length):
    password = pass_gen.generate(length)
    click.echo(password)

if __name__ == '__main__':
    cli(12)