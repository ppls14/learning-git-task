shop_dict = {
    'piekarnia' : ['chleb', 'bułka', 'pączek'],
    'warzywniak' : ['marchew', 'seler', 'rukola'],
    'drogeria' : ['szampon', 'żel do mycia', 'krem nawilżający', 'dezodorant']
}
name = "Lista zakupów"
print(name)
n = 0

for shop, article in shop_dict.items():
  article.sort()
  shop = shop.title()
  capital_letter = [x.title() for x in article]
  print(f"Idę do {shop}, kupuję tu następujące rzeczy:\n\n{capital_letter}\n")
  n = n + len(article)
  
print(f"W sumie kupuję {n} produktów.\n")