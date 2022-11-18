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
def printYoda():
  txt = r'''
                    ____
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\ ;  /___ ; \      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\ ' J
              "-.   "--"   .-"
             __.l"-:_JL_;-";.__
          .-j/'.;  ;""""  / .'\"-.
        .' /:`. "-.:     .-" .';  `.
     .-"  / ;  "-. "-..-" .-"  :    "-.
  .+"-.  : :      "-.__.-"      ;-._   \
  ; \  `.; ;                    : : "+. ;
  :  ;   ; ;                    : ;  : \:
 : `."-; ;  ;                  :  ;   ,/;
  ;    -: ;  :                ;  : .-"'  :
  :\     \  : ;             : \.-"      :
   ;`.    \  ; :            ;.'_..--  / ;
   :  "-.  "-:  ;          :/."      .'  :
     \       .-`.\        /t-""  ":-+.   :
      `.  .-"    `l    __/ /`. :  ; ; \  ;
        \   .-" .-"-.-"  .' .'j \  /   ;/
         \ / .-"   /.     .'.' ;_:'    ;
          :-""-.`./-.'     /    `.___.'
                \ `t  ._  /  bug :F_P:
                 "-.t-._:'''
  print(txt)
  return

printYoda()