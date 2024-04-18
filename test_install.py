import requests
from bs4 import BeautifulSoup

def test_packages():
    try:
        page = requests.get("https://www.python.org")
        soup = BeautifulSoup(page.content, 'html.parser')
        # Extract and print the title of the page
        page_title = soup.find('title').text
        return f"Requests and BeautifulSoup are working! Status code: {page.status_code}, Page title: {page_title}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    result = test_packages()
    print(result)
