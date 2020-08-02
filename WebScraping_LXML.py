import requests
import lxml.html

website = requests.get('https://store.steampowered.com/explore/new/')
document = lxml.html.fromstring(website.content)

releases_new = document.xpath('//div[@id="tab_newreleases_content"]')[0]

game_titles = releases_new.xpath('.//div[@class="tab_item_name"]/text()')
game_prices = releases_new.xpath('.//div[@class="discount_final_price"]/text()')


result = []
for information in zip(game_titles,game_prices):
    out = {}
    out['game_titles'] = information[0]
    out['game_prices'] = information[1]
    result.append(out)

print(result[0:3])