import os
from flask import Flask, render_template
import funkytown as funky
import pandas as pd
import json


app = Flask(__name__)


@app.route('/')
def index():
    with open('data_sources.json', 'r') as f:
        data_sources = json.load(f)

    res = []
    for source, values in data_sources.items():
        articles = funky.pull_articles(
            source=source,
            url=values['url'],
            content_tag=values['content_tag'],
            article_tag=values['article_tag'],
            title_tag=values['title_tag'],
            category_tag=values['category_tag'],
            teaser_tag=values['teaser_tag']
        )
        res += articles

    df = pd.DataFrame.from_dict(res)
    df = df.drop_duplicates('title')

    positive_articles = df[df['positivity'] > 0.2]
    neutral_articles = df[(df['positivity'] >= -0.2) &
                          (df['positivity'] <= 0.2)]
    negative_articles = df[df['positivity'] < -0.2]

    sorted_df = df.sort_values('positivity', ascending=False)
    top10 = sorted_df[:10].to_dict(orient='records')

    return render_template('articles/index.html', articles=top10)
    # return render_template('base.html')
