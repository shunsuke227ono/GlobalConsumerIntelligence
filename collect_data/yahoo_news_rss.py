import feedparser

RSS_URL = "http://rss.dailynews.yahoo.co.jp/fc/rss.xml"

yahoo_news_dic = feedparser.parse(RSS_URL)

print yahoo_news_dic.feed.title

for entry in yahoo_news_dic.entries:
  title = entry.title
  link  = entry.link
  print link
  print title
