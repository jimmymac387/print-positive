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

    

    df = pd.DataFrame.from_dict(today_good_articles)
    positive_articles = df[df['positivity'] > 0.0]
    top5 = positive_articles[:5].to_dict(orient='records')
    sorted_top5 = sorted(top5, key=lambda x: x['positivity'], reverse=True)

    return render_template('articles/index.html', articles=sorted_top5)
    # return render_template('base.html')
