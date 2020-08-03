import nltk
from newspaper import Article

nltk.download('punkt')

website = "https://www.wsj.com/articles/pickup-trucks-are-getting-huge-got-a-problem-with-that-11596254412"

news_article = Article(website)
news_article.download()
news_article.parse()

news_article.nlp()

print("The authors of this newspaper article is/are: ")
print(news_article.authors)

print("Date of Article Publication:")
print(news_article.publish_date)

print ("Article Keywords")
print(news_article.keywords)

print("Artice Image:")
print(news_article.top_image)

print("Summary of the Article:")
print(news_article.summary)