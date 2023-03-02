from bs4 import BeautifulSoup
import requests


def get_links(search_query: str) -> list:
    links = []

    url = f"https://www.google.com/search?q={search_query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("div", class_="g")

    for result in results:
        try:
            link = result.find("a")["href"]
            links.append(link)
        except KeyError:  # No link for as to harves
            pass

    return links
