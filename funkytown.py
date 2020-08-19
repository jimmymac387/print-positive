# Features to add:
# Pull images from article container
# Pull article text (and take first 100 characters for teaser)

from requests import get
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_page_content(url, content_tag=None):
    r = get(url)
    content = BeautifulSoup(r.content, features="html.parser")
    if content_tag:
        content = content.select_one(content_tag)

    return content


def get_title(article, title_tag=None):
    title = article.select_one(title_tag)

    if title:
        return title.text.strip()

    else:
        return None


def get_category(article, category_tag=None):
    if category_tag:
        categories = article.select(category_tag)

        if categories:

            return {category.text for category in categories}


def get_teaser(article, teaser_tag=None):
    # Add Feature: Pull first 100 characters from articles with no teaser
    if teaser_tag:
        teaser = article.select_one(teaser_tag)

        if teaser:
            return teaser.text.strip()

    else:
        pass  # This is where the function to pull first 100 characters goes


def get_url(article):
    # url = article.select('a')['href']
    url = article.select('a')

    if url:
        url = url[-1]['href']

        return url


# Still need to write get_category function
def extract_info(article, title_tag, category_tag=None, teaser_tag=None):
    title = get_title(article, title_tag)
    category = get_category(article, category_tag)
    teaser = get_teaser(article, teaser_tag)
    url = get_url(article)

    return (title, category, teaser, url)  # category, teaser, url)


def fformat(articles, title_tag, category_tag=None, teaser_tag=None):
    sia = SentimentIntensityAnalyzer()
    result = []

    for article in articles:
        title, category, teaser, url = extract_info(
            article,
            title_tag,
            category_tag,
            teaser_tag
        )

        positivity = sia.polarity_scores(title)['compound']

        d = {
            'title': title, 'url': url, 'category': category,
            'teaser': teaser, 'positivity': positivity,
            'source': 'NBC Today - Good News'
        }

        result.append(d)

    return result


def pull_articles(page_content, article_tag, title_tag, category_tag=None,
                  teaser_tag=None):
    raw_articles = page_content.select(article_tag)
    articles = fformat(raw_articles, title_tag, category_tag, teaser_tag)

    return articles
