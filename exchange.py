import sys

import click
import requests


def fetch_exchanges(codes):
    try:
        currencies = []
        URL = 'https://free.currencyconverterapi.com/api/v5/convert?q={query}&compact=y'
        for code in codes:
            code = code.upper()
            query = '{code}_TRY'.format(code=code)
            response = requests.get(URL.format(query=query)).json()
            if query in response:
                currencies.append({
                    'code': code,
                    'rate': str(response[query]['val'])
                })
        return currencies
    except:
        return []


@click.command()
@click.option('--delimiter', '-d', default=':')
@click.argument('code', nargs=-1)
def exchange(delimiter, code):
    """Show exchange rates"""
    if not code:
        click.echo('Provide currency code.')
        sys.exit(1)
    exchanges = fetch_exchanges(code)
    lines = [exchange['code'] + delimiter + exchange['rate'] for exchange in exchanges]
    click.echo(', '.join(lines))


if __name__ == '__main__':
    exchange()
