# Put on hold for now (make static visualizations)

from flask import Blueprint, render_template
from . import funkytown as funky


bp = Blueprint('visualizations', __name__)


@bp.route('/visualization1', methods=['POST'])
def visualization1():
    request.form['viz1']
    url = 'https://www.npr.org/'
    content_tag = '#contentWrap'
    article_tag = 'div.story-wrap'
    title_tag = 'h3'
    category_tag = None  # NPR does not have
    teaser_tag = 'p.teaser'

    page_content = funky.get_page_content(url, content_tag)

    npr_articles = funky.pull_articles(
        page_content,
        article_tag,
        title_tag,
        category_tag,
        teaser_tag
    )

    top5 = sorted(
        npr_articles,
        key=lambda x: x['positivity'],
        reverse=True
    )[:5]

    articles = top5
    return render_template('articles/index.html', articles=articles)
