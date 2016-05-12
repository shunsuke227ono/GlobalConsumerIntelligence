require 'open-uri'
require 'nokogiri'

url = 'https://ja.wikipedia.org/wiki/%E5%90%89%E6%9C%AC%E8%88%88%E6%A5%AD%E6%89%80%E5%B1%9E%E3%82%BF%E3%83%AC%E3%83%B3%E3%83%88%E4%B8%80%E8%A6%A7'

charset = nil
html = open(url) do |f|
  charset = f.charset
  f.read
end

# htmlをパース(解析)してオブジェクトを生成
doc = Nokogiri::HTML.parse(html, nil, charset)

taget = doc.css("#mw-content-text ul li")

yoshimoto_commedians = []
start = false
doc.css('#mw-content-text').children().css('ul').each do |ul|
  ul.css('li').each do |li|
    if li.css('a').inner_text == 'R藤本'
      start = true
    end
    if start
      yoshimoto_commedians << li.css('a').inner_text
    end
  end
  if yoshimoto_commedians.last == 'ビューティーメーカー'
    break
  end
end

puts yoshimoto_commedians
