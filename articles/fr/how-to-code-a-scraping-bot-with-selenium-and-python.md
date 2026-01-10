---
title: Comment coder un bot de scraping avec Selenium et Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-12T18:37:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-a-scraping-bot-with-selenium-and-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5ffd8f3b75d5f706921cc190.jpg
tags:
- name: Python
  slug: python
- name: selenium
  slug: selenium
- name: Tutorial
  slug: tutorial
- name: web scraping
  slug: web-scraping
seo_title: Comment coder un bot de scraping avec Selenium et Python
seo_desc: "By Otávio Simões Silveira\nSelenium is a tool designed to help you run\
  \ automated tests in web applications. It is available in several different programming\
  \ languages. \nAlthough it’s not its main purpose, Selenium is also used in Python\
  \ for web scrapi..."
---

Par Otávio Simões Silveira

Selenium est un outil conçu pour vous aider à exécuter des tests automatisés dans les applications web. Il est disponible dans plusieurs langages de programmation différents.

Bien que ce ne soit pas son objectif principal, Selenium est également utilisé en Python pour le web scraping, car il peut accéder au contenu rendu par JavaScript (ce que les outils de scraping réguliers comme BeautifulSoup ne peuvent pas faire).

Selenium est également utile lorsque vous devez interagir avec la page d'une manière ou d'une autre avant de collecter les données, comme cliquer sur des boutons ou remplir des champs. C'est le cas d'utilisation qui sera couvert dans cet article.

En guise d'exemple, nous allons scraper investing.com pour extraire les données historiques des taux de change du dollar contre une ou plusieurs devises.

Si vous recherchez sur le web, vous pouvez trouver des API et des packages Python qui facilitent grandement la collecte de données financières (au lieu de les scraper manuellement). Cependant, l'idée ici est d'explorer comment Selenium peut vous aider avec l'extraction générale de données.

## Le site web que nous allons scraper

Tout d'abord, nous devons comprendre le site web. [Ce site](https://investing.com/currencies/usd-eur-historical-data) contient les données historiques du taux de change du dollar contre l'euro.

Sur cette page, vous pouvez voir un tableau avec les données et l'option de définir la plage de dates que nous voulons. C'est ce que nous allons utiliser.

Pour voir les données d'autres devises contre le dollar, il suffit de remplacer « _eur_ » par le code de l'autre devise dans l'URL.

De plus, cela suppose que vous ne voudrez que le taux de change de la devise contre le dollar. Si ce n'est pas le cas, remplacez simplement « usd » dans l'URL.

## Le code du scraper

Nous commencerons par les imports, et nous n'avons pas besoin de beaucoup. Importons quelques éléments utiles de Selenium : la fonction `sleep` pour insérer des pauses dans le code, et Pandas pour manipuler la date lorsque cela est nécessaire.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
```

Ensuite, nous allons écrire une fonction pour scraper les données. La fonction recevra :

* Une liste de codes de devises
* Une date de début
* Une date de fin
* Un booléen indiquant si nous voulons exporter les données sous forme de fichier _.csv_. J'utiliserai False comme valeur par défaut.

De plus, comme l'idée ici est de construire un scraper capable de collecter des données sur plusieurs devises, nous allons également initialiser une liste vide pour stocker les données de chaque devise.

```python
def get_currencies(currencies, start, end, export_csv=False):
    frames = []
```

Comme la fonction a maintenant une liste de devises, vous imaginez probablement que nous allons itérer sur cette liste et obtenir les données devise par devise. C'est précisément le plan.

Ainsi, pour chaque devise dans la liste des devises, nous allons créer une URL, instancier un objet driver, et l'utiliser pour obtenir la page. Ensuite, nous allons maximiser la fenêtre, mais cela n'est visible que si vous gardez `option.headless` comme False. Sinon, Selenium fera tout le travail sans vous montrer quoi que ce soit.

```python
for currency in currencies:
    my_url = f'https://br.investing.com/currencies/usd-{currency.lower()}-historical-data'
    option = Options()
    option.headless = False
    driver = webdriver.Chrome(options=option)
    driver.get(my_url)
    driver.maximize_window()
```

Nous regardons déjà les données historiques à ce stade, et nous pourrions simplement obtenir le tableau avec les données. Cependant, par défaut, nous ne voyons les données que pour environ les 20 derniers jours. Nous voulons obtenir ces données pour n'importe quelle période.

Pour cela, nous allons utiliser certaines fonctionnalités intéressantes de Selenium pour interagir avec le site web. C'est là que Selenium brille !

Ce que nous allons faire ici est de cliquer sur les dates et remplir les champs Date de début et Date de fin avec les dates que nous voulons et cliquer sur Appliquer.

Pour cela, nous allons utiliser `WebDriverWait`, `ExpectedConditions`, et `By` pour nous assurer que le driver web attendra que les éléments avec lesquels nous voulons interagir soient cliquables.

C'est important car si le driver essaie d'interagir avec quelque chose avant qu'il ne devienne cliquable, une exception sera levée.

Le temps d'attente sera de vingt secondes, mais c'est à vous de le définir comme vous le jugez approprié. Tout d'abord, sélectionnons le bouton de date par son Xpath, puis cliquons dessus.

```python
date_button = WebDriverWait(driver, 20).until(
              EC.element_to_be_clickable((By.XPATH,
              "/html/body/div[5]/section/div[8]/div[3]/div/div[2]/span")))

date_button.click()
```

Maintenant, nous devons remplir le champ Date de début. Sélectionnons-le d'abord, puis utilisons `clear` pour supprimer la date par défaut et `send_keys` pour le remplir avec la date que nous voulons.

```python
start_bar = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
	        "/html/body/div[7]/div[1]/input[1]")))

start_bar.clear()
start_bar.send_keys(start)
```

Et maintenant, nous répétons le processus pour le champ Date de fin.

```python
end_bar = WebDriverWait(driver, 20).until(
          EC.element_to_be_clickable((By.XPATH,
          "/html/body/div[7]/div[1]/input[2]")))

end_bar.clear()
end_bar.send_keys(end)
```

Avec cela fait, nous allons sélectionner le bouton Appliquer et cliquer dessus. Ensuite, nous utilisons `sleep` pour mettre le code en pause pendant quelques secondes et nous assurer que la nouvelle page est entièrement chargée.

```python
apply_button = WebDriverWait(driver, 20).until(
	           EC.element_to_be_clickable((By.XPATH,
               "/html/body/div[7]/div[5]/a")))

apply_button.click()
sleep(5)
```

Si vous aviez `option.headless` comme False, vous verrez ce processus entier se dérouler devant vous comme si quelqu'un cliquait réellement sur la page. Lorsque Selenium clique sur Appliquer, vous verrez le tableau se recharger pour afficher les données pour la période que vous avez spécifiée.

Nous utilisons maintenant la fonction `pandas.read_html` pour sélectionner tous les tableaux de la page. Cette fonction recevra le code source de la page. Enfin, nous pouvons quitter le driver.

```python
dataframes = pd.read_html(driver.page_source)
driver.quit()
print(f'{currency} scrapé.')
```

## Comment gérer les exceptions dans Selenium

Le processus de collecte des données est terminé. Mais nous devons considérer que Selenium peut parfois être un peu instable et pourrait éventuellement échouer à charger la page à un moment donné pendant toutes les actions que nous effectuons ici.

Pour éviter cela, nous aurons tout le code à l'intérieur d'une clause `try` qui sera à l'intérieur d'une boucle infinie. Une fois que Selenium parvient à collecter les données comme je l'ai décrit ci-dessus, la boucle sera rompue. Mais chaque fois qu'il trouve un problème, une clause `except` sera activée.

Dans ce scénario, le code va :

* Quitter le driver – il est toujours important de le faire pour ne pas finir avec des dizaines de drivers web consommant de la mémoire en cours d'exécution
* Afficher un message indiquant l'erreur
* Attendre trente secondes
* Retourner au début de la boucle une fois de plus

Ce processus sera répété jusqu'à ce que les données pour chaque devise soient correctement collectées. Et voici le code pour tout cela :

```python
 for currency in currencies:
        while True:
            try:
                # Ouverture de la connexion et récupération de la page
                my_url = f'https://br.investing.com/currencies/usd-{currency.lower()}-historical-data'
                option = Options()
                option.headless = False
                driver = webdriver.Chrome(options=option)
                driver.get(my_url)
                driver.maximize_window()
                   
                # Cliquer sur le bouton de date
                date_button = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                            "/html/body/div[5]/section/div[8]/div[3]/div/div[2]/span")))
                
                date_button.click()
                
                # Envoyer la date de début
                start_bar = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                            "/html/body/div[7]/div[1]/input[1]")))
                            
                start_bar.clear()
                start_bar.send_keys(start)

                # Envoyer la date de fin
                end_bar = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                            "/html/body/div[7]/div[1]/input[2]")))
                            
                end_bar.clear()
                end_bar.send_keys(end)
               
                # Cliquer sur le bouton appliquer
                apply_button = WebDriverWait(driver,20).until(
                		EC.element_to_be_clickable((By.XPATH,
                		"/html/body/div[7]/div[5]/a")))
                
                apply_button.click()
                sleep(5)
                
                # Obtenir les tableaux de la page et quitter
                dataframes = pd.read_html(driver.page_source)
                driver.quit()
                print(f'{currency} scrapé.')
                break
            
            except:
                driver.quit()
                print(f'Échec du scraping de {currency}. Réessai dans 30 secondes.')
                sleep(30)
                continue

```

Une dernière étape, cependant. Si vous vous souvenez, ce que nous avons jusqu'à présent est une liste contenant tous les tableaux de la page stockés sous forme de DataFrames. Nous devons sélectionner le tableau qui contient les données historiques que nous voulons.

Pour chaque DataFrame dans cette liste de dataframes, nous allons vérifier si le nom de ses colonnes correspond à ce que nous attendons. Si c'est le cas, alors c'est notre frame et nous rompons la boucle. Et maintenant, nous sommes enfin prêts à ajouter ce DataFrame à la liste qui a été initialisée au début.

```python
for dataframe in dataframes:
    if dataframe.columns.tolist() == ['Date', 'Price', 'Open', 'High', 'Low', 'Change%']:
        df = dataframe
        break

frames.append(df)
```

Et oui, si le paramètre `export_csv` était défini sur True, nous devrions exporter un fichier _.csv_. Mais ce n'est pas un problème car la méthode `DataFrame.to_csv` peut facilement le faire.

Et ensuite, nous pouvons simplement terminer cette fonction en retournant la liste des DataFrames. Cette dernière étape est effectuée après la boucle à travers la liste des devises, bien sûr.

```python
if export_csv:
        df.to_csv('currency.csv', index=False)
        print(f'{currency}.csv exporté.')

# En dehors de la boucle
return frames
```

Et c'est tout ! Voici le code complet pour ces deux dernières étapes combinées :

```python
		# Sélection du tableau correct            
        for dataframe in dataframes:
            if dataframe.columns.tolist() == ['Date', 'Price', 'Open', 'High', 'Low', 'Change%']:
                df = dataframe
                break
        frames.append(df)

        # Exportation du fichier .csv
        if export_csv:
            df.to_csv('currency.csv', index=False)
            print(f'{currency}.csv exporté.')
                  
  return frames
```

## Prochaines étapes et conclusion

Jusqu'à présent, ce code obtient les données historiques du taux de change d'une liste de devises contre le dollar et retourne une liste de DataFrames et plusieurs fichiers _.csv_.

Mais il y a toujours place à l'amélioration. Avec quelques lignes de code supplémentaires, il n'est pas difficile de faire en sorte que la fonction retourne et exporte un seul DataFrame contenant les données pour chaque devise de la liste.

Une autre suggestion est d'écrire une fonction `update` utilisant les mêmes fonctionnalités de Selenium qui reçoit un dataframe existant et met à jour les données historiques jusqu'à la date actuelle.

De plus, la même logique utilisée pour scraper les devises peut être utilisée pour scraper des actions, des indices, des matières premières, des contrats à terme, et bien plus encore. Il y a tant de pages que vous pouvez scraper.

Cependant, si c'est l'objectif, il est important d'insérer plus de pauses dans le code pour éviter de surcharger le serveur. Vous devriez également tirer parti d'un fournisseur de proxy, tel que [Infatica](https://infatica.io/), pour vous assurer que votre code continuera à fonctionner tant qu'il y a des pages à scraper et que vous et votre connexion êtes protégés.

Enfin, Selenium peut être utile dans plusieurs autres situations telles que la connexion à des sites web, le remplissage de formulaires, la sélection d'éléments dans une liste déroulante, et bien plus encore. Bien sûr, ce n'est pas la seule solution pour de tels problèmes, mais cela peut définitivement être utile en fonction du cas d'utilisation.

J'espère que vous avez apprécié cet article et qu'il vous a été utile. Si vous avez une question ou une suggestion, n'hésitez pas à [me contacter](https://www.linkedin.com/in/otavioss28/).