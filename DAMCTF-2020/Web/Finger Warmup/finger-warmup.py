import sys
import requests
from bs4 import BeautifulSoup

# Removes recursion limit.
sys.setrecursionlimit(30000)

# Makes a recursive request until it finds the flag getting the href attribute from the a tag.
def get_recursive_page(page):
    if page.status_code == 200:
        html = BeautifulSoup(page.text,"html.parser")
        print(html)
        # Checks if the flag format is in the body page then the url of the flag will be indicated.
        if 'dam' in page.text:
            print('The flag is in this page: {}'.format(page.url))
            return False
        base_url = 'https://finger-warmup.chals.damctf.xyz/{}'.format(html.a['href'])
        page = requests.get(base_url)
        return get_recursive_page(page)

if __name__ == "__main__":
    # Basic information.
    base_url = 'https://finger-warmup.chals.damctf.xyz/'
    page = requests.get(base_url)
    get_recursive_page(page)


