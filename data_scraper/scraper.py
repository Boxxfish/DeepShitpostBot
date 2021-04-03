"""
A data scraping tool designed to scrape memes from the ShitpostBot5000 Facebook page.
"""

import click

@click.command()
@click.option('--account', help='Facebook account to scrape from.')
@click.option('--dest', type=click.Path(), help='Folder to download data to.')
@click.option('--count', type=click.INT, help='Number of posts to download.')
@click.option('--meta/--no-meta', default=False, help='Whether metadata should be downloaded.')
def scrape(account, dest, count, meta):
    pass

if __name__ == '__main__':
    scrape()