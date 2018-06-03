import sys

import click
import requests


def fetch_exchanges(codes, target):
    currencies = []
    URL = 'https://free.currencyconverterapi.com/api/v5/convert?q={query}&compact=y'
    target = target.upper()
    for code in codes:
        code = code.upper()
        query = '{code}_{target}'.format(code=code, target=target)
        response = requests.get(URL.format(query=query)).json()
        if query in response:
            currencies.append({
                'code': code,
                'rate': str(response[query]['val'])
            })
    return currencies


@click.command()
@click.option('--delimiter', '-d', default=':')
@click.option('--target', '-t', default='TRY')
@click.argument('code', nargs=-1)
def exchange(delimiter, target, code):
    """Show exchange rates"""
    if not code:
        click.echo('Provide currency code.')
        sys.exit(1)
    exchanges = fetch_exchanges(code, target)
    lines = [exchange['code'] + delimiter + exchange['rate'] for exchange in exchanges]
    click.echo(', '.join(lines))


if __name__ == '__main__':
    exchange()
