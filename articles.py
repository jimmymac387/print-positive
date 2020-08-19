from flask import Blueprint, render_template
# from nltk.tokenize import word_tokenize
from . import funkytown as funky
import pandas as pd
# import re
# from collections import Counter
# from wordcloud import WordCloud, STOPWORDS
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io

bp = Blueprint('articles', __name__)


# def make_plot(word_list):
#     """ renders the plot on the fly.
#     """
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     x_points = range(num_x_points)
#     axis.plot(x_points, [random.randint(1, 30) for x in x_points])
#
#     output = io.BytesIO()
#     FigureCanvasSVG(fig).print_svg(output)
#     return Response(output.getvalue(), mimetype="image/svg+xml")


@bp.route('/')
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
    # list(positive_articles['title'])[0]

    # top5 = sorted(
    #     npr_articles,
    #     key=lambda x: x['positivity'],
    #     reverse=True
    # )[:5]

    articles = sorted_top5

    # # Word counts
    # stopwords = set(STOPWORDS)
    #
    # all_words = []
    # for row in positive_articles['title']:
    #     all_words += word_tokenize(row)
    # rm_punc = re.compile('.*[A-za-z0-9].*')
    # filtered = [w for w in all_words if rm_punc.match(w)]
    # # counts = Counter(filtered)
    #
    # wc = WordCloud(
    #     width=800, height=400,
    #     background_color='white',
    #     stopwords=stopwords,
    #     min_font_size=4
    # )
    # wc.generate(' '.join(filtered))
    # # sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # plt.figure(figsize=(8, 4), facecolor=None)
    # plt.imshow(wc)
    # plt.axis('off')
    # plt.tight_layout(pad=0)
    # plt.show()
    # # df.head()

    return render_template('articles/index.html', articles=articles)
