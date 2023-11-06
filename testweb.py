>>> url='https://docs.google.com/spreadsheets/d/1hg1rNsRpEIz8CBTPW2q3fhcVfiGm7dOYk-ZRupnBqEQ/edit?pli=1#gid=1817848148'
>>> # Import libraries
>>> import requests
>>> from bs4 import BeautifulSoup
>>> import pandas as pd
>>> # Create object page
>>> page = requests.get(url)
>>> # Obtain page's information
>>> soup = BeautifulSoup(page.text, 'lxml')
>>> soup

