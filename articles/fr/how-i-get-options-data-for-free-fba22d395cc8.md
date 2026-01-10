---
title: Comment j'obtiens des données d'options gratuitement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-10T17:05:11.000Z'
originalURL: https://freecodecamp.org/news/how-i-get-options-data-for-free-fba22d395cc8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*8B9koPyETFCwVvO6.png
tags:
- name: finance
  slug: finance
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: web scraping
  slug: web-scraping
seo_title: Comment j'obtiens des données d'options gratuitement
seo_desc: 'By Harry Sauers

  An introduction to web scraping for finance


  Ever wished you could access historical options data, but got blocked by a paywall?
  What if you just want it for research, fun, or to develop a personal trading strategy?

  In this tutorial, ...'
---

Par Harry Sauers

#### Une introduction au web scraping pour la finance

![Image](https://cdn-media-1.freecodecamp.org/images/3ijdvJH6eCn2kke2e555zvyrpErBZKhZN0fx)

Vous avez déjà souhaité accéder à des données historiques d'options, mais vous avez été bloqué par un paywall ? Que faire si vous en avez besoin pour la recherche, le plaisir ou pour développer une stratégie de trading personnelle ?

Dans ce tutoriel, vous apprendrez à utiliser Python et BeautifulSoup pour extraire des données financières du Web et construire votre propre ensemble de données.

### **Installation**

Vous devriez avoir au moins une connaissance de base de Python et des technologies Web avant de commencer ce tutoriel. Pour développer ces compétences, je vous recommande vivement de consulter un site comme [codecademy](https://www.codecademy.com/) pour apprendre de nouvelles compétences ou rafraîchir les anciennes.

Tout d'abord, lancez votre IDE préféré. Normalement, j'utilise [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html), mais pour un script rapide comme celui-ci, [Repl.it](https://repl.it/) fera également l'affaire. Ajoutez un simple print ("Hello world") pour vous assurer que votre environnement est correctement configuré.

Maintenant, nous devons trouver une source de données.

Malheureusement, [les données de la chaîne d'options de Cboe](http://www.cboe.com/delayedquote/quote-table) sont assez verrouillées, même pour les cotations différées actuelles. Heureusement, Yahoo Finance dispose de données d'options suffisamment solides [ici](https://finance.yahoo.com/quote/SPY/options?p=SPY). Nous les utiliserons pour ce tutoriel, car les web scrapers ont souvent besoin d'une certaine conscience du contenu, mais il est facilement adaptable pour toute source de données que vous souhaitez.

### **Dépendances**

Nous n'avons pas besoin de nombreuses dépendances externes. Nous avons juste besoin des modules Requests et BeautifulSoup en Python. Ajoutez ces lignes en haut de votre programme :

```
from bs4 import BeautifulSoup
import requests
```

Créez une méthode `main` :

```
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

### Extraction de HTML

Maintenant, vous êtes prêt à commencer l'extraction ! À l'intérieur de `main()`, ajoutez ces lignes pour récupérer le `HTML` complet de la page :

```
data_url = "https://finance.yahoo.com/quote/SPY/options"
data_html = requests.get(data_url).content
print(data_html)
```

Cela récupère le contenu `HTML` complet de la page, afin que nous puissions trouver les données que nous voulons. N'hésitez pas à l'exécuter et à observer la sortie.

N'hésitez pas à commenter les instructions print au fur et à mesure — elles sont là pour vous aider à comprendre ce que fait le programme à chaque étape.

BeautifulSoup est l'outil parfait pour travailler avec les données `HTML` en Python. Réduisons le `HTML` aux seules tables de prix des options afin de mieux le comprendre :

```
content = BeautifulSoup(data_html, "html.parser")
# print(content)
```

```
options_tables = content.find_all("table")
print(options_tables)
```

C'est encore beaucoup de `HTML` — nous ne pouvons pas en tirer grand-chose, et le code de Yahoo n'est pas le plus convivial pour les web scrapers. Décomposons-le en deux tables, pour les calls et les puts :

```
options_tables = []
tables = content.find_all("table")
for i in range(0, len(content.find_all("table"))):
    options_tables.append(tables[i])
```

```
print(options_tables)
```

Les données de Yahoo contiennent des options qui sont assez profondes dans et hors de la monnaie, ce qui peut être idéal pour certains objectifs. Je ne m'intéresse qu'aux options proches de la monnaie, à savoir les deux calls et les deux puts les plus proches du prix actuel.

Trouvons ces options en utilisant BeautifulSoup et les entrées de tableau différentiel de Yahoo pour les options dans et hors de la monnaie :

```
expiration = datetime.datetime.fromtimestamp(int(datestamp)).strftime("%Y-%m-%d")
```

```
calls = options_tables[0].find_all("tr")[1:]  # première ligne est l'en-tête
```

```
itm_calls = []
otm_calls = []
```

```
for call_option in calls:
    if "in-the-money" in str(call_option):
        itm_calls.append(call_option)
    else:
        otm_calls.append(call_option)
```

```
itm_call = itm_calls[-1]
otm_call = otm_calls[0]
```

```
print(str(itm_call) + " \n\n " + str(otm_call))
```

Maintenant, nous avons les entrées de tableau pour les deux options les plus proches de la monnaie en `HTML`. Extrayons les données de prix, le volume et la volatilité implicite de la première option call :

```
itm_call_data = []
for td in BeautifulSoup(str(itm_call), "html.parser").find_all("td"):
    itm_call_data.append(td.text)
```

```
print(itm_call_data)
```

```
itm_call_info = {'contract': itm_call_data[0], 'strike': itm_call_data[2], 'last': itm_call_data[3],
                 'bid': itm_call_data[4], 'ask': itm_call_data[5], 'volume': itm_call_data[8], 'iv': itm_call_data[10]}
```

```
print(itm_call_info)
```

Adaptez ce code pour la prochaine option call :

```
# otm call
otm_call_data = []
for td in BeautifulSoup(str(otm_call), "html.parser").find_all("td"):
    otm_call_data.append(td.text)
```

```
# print(otm_call_data)
```

```
otm_call_info = {'contract': otm_call_data[0], 'strike': otm_call_data[2], 'last': otm_call_data[3],
                 'bid': otm_call_data[4], 'ask': otm_call_data[5], 'volume': otm_call_data[8], 'iv': otm_call_data[10]}
```

```
print(otm_call_info)
```

Lancez votre programme !

Vous avez maintenant des dictionnaires des deux options call proches de la monnaie. Il suffit d'extraire le tableau des options put pour ces mêmes données :

```
puts = options_tables[1].find_all("tr")[1:]  # première ligne est l'en-tête
```

```
itm_puts = []
  otm_puts = []
```

```
for put_option in puts:
    if "in-the-money" in str(put_option):
      itm_puts.append(put_option)
    else:
      otm_puts.append(put_option)
```

```
itm_put = itm_puts[0]
  otm_put = otm_puts[-1]
```

```
# print(str(itm_put) + " \n\n " + str(otm_put) + "\n\n")
```

```
itm_put_data = []
  for td in BeautifulSoup(str(itm_put), "html.parser").find_all("td"):
    itm_put_data.append(td.text)
```

```
# print(itm_put_data)
```

```
itm_put_info = {'contract': itm_put_data[0],                  'last_trade': itm_put_data[1][:10],                  'strike': itm_put_data[2], 'last': itm_put_data[3],
                   'bid': itm_put_data[4], 'ask': itm_put_data[5], 'volume': itm_put_data[8], 'iv': itm_put_data[10]}
```

```
# print(itm_put_info)
```

```
# otm put
  otm_put_data = []
  for td in BeautifulSoup(str(otm_put), "html.parser").find_all("td"):
    otm_put_data.append(td.text)
```

```
# print(otm_put_data)
```

```
otm_put_info = {'contract': otm_put_data[0],                  'last_trade': otm_put_data[1][:10],                  'strike': otm_put_data[2], 'last': otm_put_data[3],
                   'bid': otm_put_data[4], 'ask': otm_put_data[5], 'volume': otm_put_data[8], 'iv': otm_put_data[10]}
```

Félicitations ! Vous venez d'extraire les données de toutes les options proches de la monnaie de l'ETF S&P 500, et vous pouvez les visualiser comme ceci :

```
print("\n\n")
print(itm_call_info)
print(otm_call_info)
print(itm_put_info)
print(otm_put_info)
```

Lancez votre programme — vous devriez obtenir des données comme celles-ci imprimées dans la console :

```
{'contract': 'SPY190417C00289000', 'last_trade': '2019–04–15', 'strike': '289.00', 'last': '1.46', 'bid': '1.48', 'ask': '1.50', 'volume': '4,646', 'iv': '8.94%'}
{'contract': 'SPY190417C00290000', 'last_trade': '2019–04–15', 'strike': '290.00', 'last': '0.80', 'bid': '0.82', 'ask': '0.83', 'volume': '38,491', 'iv': '8.06%'}
{'contract': 'SPY190417P00290000', 'last_trade': '2019–04–15', 'strike': '290.00', 'last': '0.77', 'bid': '0.75', 'ask': '0.78', 'volume': '11,310', 'iv': '7.30%'}
{'contract': 'SPY190417P00289000', 'last_trade': '2019–04–15', 'strike': '289.00', 'last': '0.41', 'bid': '0.40', 'ask': '0.42', 'volume': '44,319', 'iv': '7.79%'}
```

### Configuration de la collecte de données récurrente

Yahoo, par défaut, ne retourne les options que pour la date que vous spécifiez. C'est cette partie de l'URL : [https://finance.yahoo.com/quote/SPY/options?date=**1555459200**](https://finance.yahoo.com/quote/SPY/options?date=1555459200)

Il s'agit d'un timestamp Unix, nous devons donc en générer ou en extraire un, plutôt que de le coder en dur dans notre programme.

Ajoutez quelques dépendances :

```
import datetime, time
```

Écrivons un script rapide pour générer et vérifier un timestamp Unix pour notre prochain ensemble d'options :

```
def get_datestamp():
    options_url = "https://finance.yahoo.com/quote/SPY/options?date="
    today = int(time.time())
    # print(today)
    date = datetime.datetime.fromtimestamp(today)
    yy = date.year
    mm = date.month
    dd = date.day
```

Le code ci-dessus contient l'URL de base de la page que nous extrayons et génère un objet `datetime.date` que nous pouvons utiliser à l'avenir.

Incrémentons cette date d'un jour, afin de ne pas obtenir d'options déjà expirées.

```
dd += 1
```

Maintenant, nous devons le convertir à nouveau en un timestamp Unix et nous assurer qu'il s'agit d'une date valide pour les contrats d'options :

```
options_day = datetime.date(yy, mm, dd)
datestamp = int(time.mktime(options_day.timetuple()))
# print(datestamp)
# print(datetime.datetime.fromtimestamp(options_stamp))
```

```
# vérifier le timestamp, puis retourner s'il est valide
for i in range(0, 7):
    test_req = requests.get(options_url + str(datestamp)).content
    content = BeautifulSoup(test_req, "html.parser")
    # print(content)
    tables = content.find_all("table")
```

```
if tables != []:
    # print(datestamp)
    return str(datestamp)
else:
    # print("Bad datestamp!")
    dd += 1
    options_day = datetime.date(yy, mm, dd)
    datestamp = int(time.mktime(options_day.timetuple()))
    return str(-1)
```

Adaptons notre méthode `fetch_options` pour utiliser un timestamp dynamique afin de récupérer les données d'options, plutôt que ce que Yahoo veut nous donner par défaut.

Changez cette ligne :

```
data_url = "https://finance.yahoo.com/quote/SPY/options"
```

En ceci :

```
datestamp = get_datestamp()
data_url = "https://finance.yahoo.com/quote/SPY/options?date=" + datestamp
```

Félicitations ! Vous venez d'extraire des données d'options du monde réel depuis le web.

Maintenant, nous devons faire quelques opérations simples de fichier et configurer un minuteur pour enregistrer ces données chaque jour après la fermeture du marché.

### Amélioration du programme

Renommez `main()` en `fetch_options()` et ajoutez ces lignes en bas :

```
options_list = {'calls': {'itm': itm_call_info, 'otm': otm_call_info}, 
                'puts': {'itm': itm_put_info, 'otm': otm_put_info}, 
                'date': datetime.date.fromtimestamp(time.time()).strftime("%Y-%m-%d")}
return options_list
```

Créez une nouvelle méthode appelée `schedule()`. Nous l'utiliserons pour contrôler quand nous extrayons les options, toutes les vingt-quatre heures après la fermeture du marché. Ajoutez ce code pour planifier notre premier travail à la prochaine fermeture du marché :

```
from apscheduler.schedulers.background import BackgroundScheduler
```

```
scheduler = BackgroundScheduler()
```

```
def schedule():
    scheduler.add_job(func=run, trigger="date", run_date = datetime.datetime.now())
    scheduler.start()
```

Dans votre instruction `if __name__ == "__main__" :`, supprimez `main()` et ajoutez un appel à `schedule()` pour configurer votre premier travail planifié.

Créez une autre méthode appelée `run()`. C'est ici que nous gérerons la majorité de nos opérations, y compris l'enregistrement réel des données de marché. Ajoutez ceci au corps de `run()` :

```
today = int(time.time())
date = datetime.datetime.fromtimestamp(today)
yy = date.year
mm = date.month
dd = date.day
```

```
# doit utiliser 12:30 pour l'heure Unix au lieu de 4:30 heure de New York
next_close = datetime.datetime(yy, mm, dd, 12, 30)
```

```
# faire les opérations ici """ C'est ici que nous écrirons notre dernier morceau de code. """
```

```
# planifier le prochain travail
scheduler.add_job(func=run, trigger="date", run_date = next_close)
```

```
print("Job scheduled! | " + str(next_close))
```

Cela permet à notre code de s'appeler lui-même à l'avenir, afin que nous puissions simplement le mettre sur un serveur et construire nos données d'options chaque jour. Ajoutez ce code pour réellement récupérer les données sous `""" C'est ici que nous écrirons notre dernier morceau de code. """`

```
options = {}
```

```
# assure que les données d'options ne cassent pas le programme si internet est hors ligne
try:
    if next_close > datetime.datetime.now():
        print("Le marché est encore ouvert ! Attente jusqu'à la fermeture...")
    else:
        # assure que le programme a été exécuté après les heures de marché
        if next_close < datetime.datetime.now():
            dd += 1
            next_close = datetime.datetime(yy, mm, dd, 12, 30)
            options = fetch_options()
            print(options)
            # écrire dans le fichier
            write_to_csv(options)
except:
    print("Vérifiez votre connexion et réessayez.")
```

### Enregistrement des données

Vous avez peut-être remarqué que `write_to_csv` n'est pas encore implémenté. Pas de souci — prenons soin de cela ici :

```
def write_to_csv(options_data):
    import csv
    with open('options.csv', 'a', newline='\n') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([str(options_data)])
```

### **Nettoyage**

Comme les contrats d'options sont sensibles au temps, nous pourrions vouloir ajouter un champ pour leur date d'expiration. Cette capacité n'est pas incluse dans le HTML brut que nous avons extrait.

Ajoutez cette ligne de code pour enregistrer et formater la date d'expiration vers le haut de `fetch_options()` :

```
expiration = datetime.datetime.fromtimestamp(int(get_datestamp())).strftime("%Y-%m-%d")
```

Ajoutez `'expiration': expiration` à la fin de chaque dictionnaire `option_info` comme ceci :

```
itm_call_info = {'contract': itm_call_data[0], 'strike': itm_call_data[2], 'last': itm_call_data[3],
                 'bid': itm_call_data[4], 'ask': itm_call_data[5], 'volume': itm_call_data[8], 'iv': itm_call_data[10], 'expiration': expiration}
```

Lancez votre nouveau programme — il extraira les dernières données d'options et les écrira dans un fichier .csv sous forme de représentation de chaîne d'un dictionnaire. Le fichier .csv sera prêt à être analysé par un programme de backtesting ou servi aux utilisateurs via une application web. Félicitations !