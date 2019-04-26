import sys

import click
import requests


def fetch_exchanges(codes, target):
    currencies = []
    URL = 'https://api.exchangeratesapi.io/latest?base={base}&symbols={symbols}'
    base = target.upper()
    symbols = ','.join(code.upper() for code in codes)
    response = requests.get(URL.format(base=base, symbols=symbols)).json()
    if not 'rates' in response:
        sys.exit(2)
    rates = response['rates']
    for symbol in rates.keys():
        currencies.append({
            'code': symbol,
            'rate': 1/rates[symbol]
        })
    return currencies


@click.command()
@click.option('--delimiter', '-d', default=':')
@click.option('--target', '-t', default='TRY', help='Currency symbol you want to get rates for.')
@click.argument('code', nargs=-1)
def exchange(delimiter, target, code):
    """Show exchange rates"""
    if not code:
        click.echo('Provide currency code.')
        sys.exit(1)
    exchanges = fetch_exchanges(code, target)
    lines = [exchange['code'] + delimiter + '{:.4f}'.format(exchange['rate'])
             for exchange in exchanges]
    click.echo(', '.join(lines))


if __name__ == '__main__':
    exchange()
