# print('positive')
This project was developed as part of an intensive eight-week data science fellowship at The Data Incubator. The goal of the project was to create an aggregator for positive news.

### Problem Statement/Purpose
Consuming negative news on a daily basis can have a significant impact on our mental health. In response, news organizations are starting to recognize the benefits serving positive content to users, but they are not the only ones. Other companies like Starbucks, Apple, and Coca-Cola know that positive emotions toward a brand have greatly influence consumer loyalty and can lead to greater sales. The purpose of this project was to develop a tool that can be used by companies to highlight positive stories to help improve mental health and drive sales.

Compare sentiment of various news organizations.

### Data/Models Used
The data used in this project comes from four sources--two neutral sources and two sources that specialize in providing positive and uplifting news stories.

Neutral Sources:
- [NPR](https://www.npr.org/)
- [NBC Today](https://www.today.com/)

Positive Sources:
- [NBC Today - Good News](https://www.today.com/news/good-news)
- [Positive News](https://www.positive.news/)

Headlines are scraped from the front page of each news organization using BeautifulSoup and then passed through the Valence Aware Dictionary and sEntiment Reasoner (VADER) sentiment analysis tool available in the Natural Language ToolKit (NLTK) package to generate a normalized score between +1 (positive sentiment) and -1 (negative sentiment).

These scores are used to sort the data and identify the top 10 positive stories, which are then served to the user in a Flask web application. Data for the web application is generated each time the page is reloaded to keep the content up-to-date.

### Results
- Static plots (word cloud; compare sentiment between positive news site and neutral)

In addition to providing a link to the article, the web application also generates a word cloud to visualize words associated with positive, neutral, and negative headlines.

![Positive Words](./static/images/positive_words_example.png)

*Example of most common words in positive news articles*


- Predicted sentiment on NPR returned lots of COVID articles (e.g., people had to leave school because too many COVID cases)
- Base functionality provided by nltk is not sufficient for analyzing sentiment of news articles

- Naural Language Toolkit (NLTK) used for sentiment analysis (VADER)
- VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.
