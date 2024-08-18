from bs4 import BeautifulSoup

def parse_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.title.string

def parse_links_and_names(html):
    soup = BeautifulSoup(html, 'html.parser')
    link_name_pairs = []
    for div in soup.find_all("div", class_="name-div"):
        a_tag = div.find("a", href=True)
        if a_tag:
            link = a_tag['href']
            name = a_tag.text.strip()
            link_name_pairs.append((link, name))
    return link_name_pairs
