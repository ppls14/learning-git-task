shop_dict = {
    'piekarnia' : ['chleb', 'bułka', 'pączek'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}
name = "Lista zakupów"
print(name)

for shop, article in shop_dict.items():
  shop = shop.title()
  capital_letter = [x.title() for x in article]
  print(f"Idę do {shop}, kupuję tu następujące rzeczy:\n\n{capital_letter}\n")