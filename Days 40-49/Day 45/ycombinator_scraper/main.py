from bs4 import BeautifulSoup
import requests
# import lxml

# Get the website
website = requests.get(url="https://news.ycombinator.com/news")
soup = BeautifulSoup(markup=website.text, features="html.parser")

# Get the articles
articles = soup.find_all(name="span", class_="titleline")

# Get the article links
article_links = [article.find(name="a") for article in articles]

# Get the article titles
article_titles = [link.get_text() for link in article_links]

# Get the article links
article_links = [link.get("href") for link in article_links]

# Get the article upvotes
article_upvotes = [int(span.get_text().split(" ")[0]) for span in soup.find_all(name="span", class_="score")]

# print(article_titles)
# print(article_links)
# print(article_upvotes)
#
# print()

# Get the highest upvotes
max_upvotes = max(article_upvotes)

# Get the index of the highest upvote
article_num = article_upvotes.index(max_upvotes)

# Print the highest upvoted article
print(article_titles[article_num])
print(article_links[article_num])
print(article_upvotes[article_num])
