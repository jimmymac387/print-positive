import os
from flask import Flask, render_template
import funkytown as funky
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://www.today.com/news/good-news'
    content_tag = None  # NBC Today - Good News does not have
    article_tag = 'article.tease-card__content'
    title_tag = 'span.tease-card__headline'
    category_tag = 'div.tease-card__picture > h2 > span'
    teaser_tag = None  # NBC Today - Good News does not have

    page_content = funky.get_page_content(url, content_tag)

    today_good_articles = funky.pull_articles(
        page_content,
        article_tag,
        title_tag,
        category_tag,
        teaser_tag
    )

    today_good_articles

    df = pd.DataFrame.from_dict(today_good_articles)
    positive_articles = df[df['positivity'] > 0.0]
    top5 = positive_articles[:5].to_dict(orient='records')
    sorted_top5 = sorted(top5, key=lambda x: x['positivity'], reverse=True)

    return render_template('articles/index.html', articles=sorted_top5)
    # return render_template('base.html')
