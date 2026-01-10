---
title: Comment utiliser Python pour créer votre propre scraper Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-07-10T13:11:06.000Z'
originalURL: https://freecodecamp.org/news/use-python-sdk-to-build-a-web-scraper
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/ilya-pavlov-OqtafYT5kTw-unsplash.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Comment utiliser Python pour créer votre propre scraper Web
seo_desc: 'By Jess Wilk

  What is Web scraping?

  Web scraping is a technique used to collect large amounts of data automatically
  using a programming script. This makes it useful for many professionals such as
  data analysts, market researchers, SEO specialists, bus...'
---

Par Jess Wilk

## **Qu'est-ce que le Web scraping ?**

Le Web scraping est une technique utilisée pour collecter automatiquement de grandes quantités de données à l'aide d'un script de programmation. Cela le rend utile pour de nombreux professionnels tels que les analystes de données, les chercheurs en marketing, les spécialistes du SEO, les analystes commerciaux et les chercheurs académiques.

## **Ce que vous apprendrez ici**

Python fournit deux bibliothèques, Requests et Beautiful Soup, qui vous aident à scraper des sites Web plus facilement. L'utilisation combinée de Requests et Beautiful Soup de Python peut récupérer le contenu HTML d'un site Web et ensuite le parser pour extraire les données dont vous avez besoin. Dans cet article, je vais vous montrer comment utiliser ces bibliothèques avec un exemple.

À la fin de ce guide, vous serez équipé pour construire votre propre Web Scraper et aurez une compréhension plus profonde de la manipulation de grandes quantités de données et de la manière de les appliquer pour prendre des décisions basées sur les données.

Veuillez noter que bien qu'un scraper Web soit un outil utile, assurez-vous d'être conforme à toutes les directives légales. Cela implique de respecter le fichier `robots.txt` du site Web et d'adhérer aux conditions d'utilisation pour éviter l'extraction non autorisée de données.

De plus, avant de scraper, assurez-vous que le processus de scraping ne nuit pas à la fonctionnalité du site Web ou ne surcharge pas ses serveurs. Enfin, respectez la confidentialité des données en ne scrapant pas d'informations personnelles ou sensibles sans consentement approprié.

## **Comment Beautiful Soup et Python Requests fonctionnent ensemble**

Comprenons le rôle de chaque bibliothèque.

La bibliothèque Python Requests est responsable de la récupération du contenu HTML à partir de l'URL que vous fournissez dans le script. Une fois qu'elle a récupéré le contenu, elle stocke les données dans un objet de réponse.

Beautiful Soup prend ensuite le relais, transformant le HTML brut de la réponse Requests en un format structuré et le parse. Vous pouvez ensuite scraper les données du HTML parsé en spécifiant des attributs, ce qui vous permet d'automatiser la collecte de données spécifiques à partir de sites Web ou de dépôts.

Mais ce duo a ses limites. La bibliothèque Requests ne peut pas gérer les sites Web avec du contenu JavaScript dynamique. Vous devez donc l'utiliser principalement pour les sites qui servent du contenu statique à partir de serveurs. Si vous devez scraper un site chargé dynamiquement, vous devrez utiliser des outils d'automatisation plus avancés comme Selenium.

## **Comment construire un Web Scraper avec Python**

Maintenant que nous comprenons ce que Beautiful Soup et Python Requests peuvent faire, discutons de la manière dont nous pouvons scraper des données en utilisant ces outils.

Dans l'exemple suivant, nous allons scraper des données à partir du [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/datasets).

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXd2MTmii-KD8tu6AAeHhbr9Sb5vauq3jC3AcYc2Yvd4kcCQLdTdVrBqZuFOpF-vKQ3E012hV7W6bm0iOtqrCsvJx6xsT165mKqbKVC8Kf48ZxOMq-Joi7n2jDw6fl3AM4XLVBuikCJpXTIB6c6JriJtP9MQ?key=f_hrU3B_rjNJFpKZiiV3Pw)
_Jeux de données au UC Irvine Machine Learning Repository_

Comme vous pouvez le voir, il contient de nombreux jeux de données, et vous pouvez trouver des détails supplémentaires sur chaque jeu de données en allant sur une page dédiée pour le jeu de données. Vous pouvez accéder à la page dédiée en cliquant sur le nom du jeu de données dans la liste ci-dessus.

Consultez l'image ci-dessous pour avoir une idée des informations fournies pour chaque jeu de données.

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXcb7_BVgpIh1P931U-HHX6BKIPN1ODKRzc6WqjX-n77uA9Uvz_e80wqc2YtJx2-Rq3HzWKtlDE31gV-7jz0UASzKrhq86X45paNDkVVO5oNXeaRZ99vIs45g1TwMk54hpyEetzyuDjMgPYW4KKW-oPhKjh8?key=f_hrU3B_rjNJFpKZiiV3Pw)
_Jeu de données Iris_

Le code que nous écrivons ci-dessous parcourra chaque jeu de données, scrapera les détails et les enregistrera dans un fichier CSV.

### Prérequis

Pour essayer ce tutoriel, vous devez avoir plusieurs prérequis configurés.

Je suppose que vous avez déjà une installation de Python sur votre machine. Si ce n'est pas le cas, veuillez télécharger la dernière version de Python depuis le [site officiel](https://www.python.org/downloads/).

Les bibliothèques Requests et Beautiful Soup ne sont pas fournies avec Python. Vous devrez les installer séparément. Pour cela, vous pouvez utiliser le gestionnaire de paquets pip qui est inclus par défaut avec l'installation de Python depuis Python 3.4.

Vous pouvez utiliser pip pour installer les bibliothèques Requests et Beautiful Soup en utilisant les commandes suivantes :

```python
pip install requests
pip install beautifulsoup4
```

Si elles ont été installées avec succès, vous êtes maintenant prêt à commencer à coder.

### Étape 1 : Importer les bibliothèques nécessaires

Tout d'abord, importez les bibliothèques nécessaires : Requests pour faire des requêtes HTTP, BeautifulSoup pour parser le contenu HTML (si vous ne l'avez pas déjà installé à partir de l'étape précédente), et CSV pour sauvegarder les données.

```python
import requests
from bs4 import BeautifulSoup
import csv
```

### Étape 2 : Définir l'URL de base et les en-têtes CSV

Définissez l'URL de base pour les listes de jeux de données et définissez les en-têtes pour le fichier CSV où les données scrapées seront sauvegardées.

```python
def scrape_uci_datasets():
    base_url = "https://archive.ics.uci.edu/datasets"


    headers = [
        "Nom du jeu de données", "Date de donation", "Description",
        "Caractéristiques du jeu de données", "Domaine", "Tâches associées",
        "Type de caractéristiques", "Instances", "Caractéristiques"
    ]


    data = []
```

### Étape 3 : Créer une fonction pour scraper les détails du jeu de données

Définissez une fonction `scrape_dataset_details` qui prend l'URL d'une page de jeu de données individuelle, récupère le contenu HTML, le parse en utilisant BeautifulSoup, et extrait les informations pertinentes.

```python

    def scrape_dataset_details(dataset_url):
        response = requests.get(dataset_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_name = soup.find(
            'h1', class_='text-3xl font-semibold text-primary-content')
        dataset_name = dataset_name.text.strip() if dataset_name else "N/A"


        donated_date = soup.find('h2', class_='text-sm text-primary-content')
        donated_date = donated_date.text.strip().replace(
            'Donated on ', '') if donated_date else "N/A"


        description = soup.find('p', class_='svelte-17wf9gp')
        description = description.text.strip() if description else "N/A"


        details = soup.find_all('div', class_='col-span-4')


        dataset_characteristics = details[0].find('p').text.strip() if len(
            details) > 0 else "N/A"
        subject_area = details[1].find('p').text.strip() if len(
            details) > 1 else "N/A"
        associated_tasks = details[2].find('p').text.strip() if len(
            details) > 2 else "N/A"
        feature_type = details[3].find('p').text.strip() if len(
            details) > 3 else "N/A"
        instances = details[4].find('p').text.strip() if len(
            details) > 4 else "N/A"
        features = details[5].find('p').text.strip() if len(
            details) > 5 else "N/A"


        return [
            dataset_name, donated_date, description, dataset_characteristics,
            subject_area, associated_tasks, feature_type, instances, features
        ]
```

La fonction `scrape_dataset_details` récupère le contenu HTML d'une page de jeu de données et le parse en utilisant BeautifulSoup. Elle extrait les informations en ciblant des éléments HTML spécifiques en fonction de leurs balises et classes, tels que les noms de jeux de données, les dates de donation et les descriptions.

La fonction utilise des méthodes comme `find` et `find_all` pour localiser ces éléments et récupérer leur contenu textuel, en gérant les cas où les éléments pourraient être manquants en fournissant des valeurs par défaut.

Cette approche systématique garantit que les détails pertinents sont capturés avec précision et retournés dans un format structuré.

### Étape 4 : Créer une fonction pour scraper les listes de jeux de données

Définissez une fonction `scrape_datasets` qui prend l'URL d'une page listant plusieurs jeux de données, récupère le contenu HTML et trouve tous les liens de jeux de données. Pour chaque lien, elle appelle `scrape_dataset_details` pour obtenir des informations détaillées.

```python
    def scrape_datasets(page_url):
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_list = soup.find_all(
            'a', class_='link-hover link text-xl font-semibold')


        if not dataset_list:
            print("Aucun lien de jeu de données trouvé")
            return


        for dataset in dataset_list:
            dataset_link = "https://archive.ics.uci.edu" + dataset['href']
            print(f"Scraping des détails pour {dataset.text.strip()}...")
            dataset_details = scrape_dataset_details(dataset_link)
            data.append(dataset_details)
```

### Étape 5 : Boucler à travers les pages en utilisant les paramètres de pagination

Implémentez une boucle pour naviguer à travers les pages en utilisant les paramètres de pagination. La boucle continue jusqu'à ce qu'aucune nouvelle donnée ne soit ajoutée, indiquant que toutes les pages ont été scrapées.

```python
    skip = 0
    take = 10
    while True:
        page_url = f"https://archive.ics.uci.edu/datasets?skip={skip}&take={take}&sort=desc&orderBy=NumHits&search="
        print(f"Scraping de la page : {page_url}")
        initial_data_count = len(data)
        scrape_datasets(page_url)
        if len(
                data
        ) == initial_data_count:  
            break
        skip += take
```

### Étape 6 : Sauvegarder les données scrapées dans un fichier CSV

Après avoir scrapé toutes les données, sauvegardez-les dans un fichier CSV.

```python
    with open('uci_datasets.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


    print("Scraping terminé. Les données ont été sauvegardées dans 'uci_datasets.csv'.")
```

### Étape 7 : Exécuter la fonction de scraping

Enfin, appelez la fonction `scrape_uci_datasets` pour démarrer le processus de scraping.

```python
scrape_uci_datasets()
```

## **Code complet**

Voici le code complet pour le scraper Web :

```python
import requests
from bs4 import BeautifulSoup
import csv


def scrape_uci_datasets():
    base_url = "https://archive.ics.uci.edu/datasets"


    headers = [
        "Nom du jeu de données", "Date de donation", "Description",
        "Caractéristiques du jeu de données", "Domaine", "Tâches associées",
        "Type de caractéristiques", "Instances", "Caractéristiques"
    ]


    # Liste pour stocker les données scrapées
    data = []


    def scrape_dataset_details(dataset_url):
        response = requests.get(dataset_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_name = soup.find(
            'h1', class_='text-3xl font-semibold text-primary-content')
        dataset_name = dataset_name.text.strip() if dataset_name else "N/A"


        donated_date = soup.find('h2', class_='text-sm text-primary-content')
        donated_date = donated_date.text.strip().replace(
            'Donated on ', '') if donated_date else "N/A"


        description = soup.find('p', class_='svelte-17wf9gp')
        description = description.text.strip() if description else "N/A"


        details = soup.find_all('div', class_='col-span-4')


        dataset_characteristics = details[0].find('p').text.strip() if len(
            details) > 0 else "N/A"
        subject_area = details[1].find('p').text.strip() if len(
            details) > 1 else "N/A"
        associated_tasks = details[2].find('p').text.strip() if len(
            details) > 2 else "N/A"
        feature_type = details[3].find('p').text.strip() if len(
            details) > 3 else "N/A"
        instances = details[4].find('p').text.strip() if len(
            details) > 4 else "N/A"
        features = details[5].find('p').text.strip() if len(
            details) > 5 else "N/A"


        return [
            dataset_name, donated_date, description, dataset_characteristics,
            subject_area, associated_tasks, feature_type, instances, features
        ]


    def scrape_datasets(page_url):
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_list = soup.find_all(
            'a', class_='link-hover link text-xl font-semibold')


        if not dataset_list:
            print("Aucun lien de jeu de données trouvé")
            return


        for dataset in dataset_list:
            dataset_link = "https://archive.ics.uci.edu" + dataset['href']
            print(f"Scraping des détails pour {dataset.text.strip()}...")
            dataset_details = scrape_dataset_details(dataset_link)
            data.append(dataset_details)


    # Boucler à travers les pages en utilisant les paramètres de pagination
    skip = 0
    take = 10
    while True:
        page_url = f"https://archive.ics.uci.edu/datasets?skip={skip}&take={take}&sort=desc&orderBy=NumHits&search="
        print(f"Scraping de la page : {page_url}")
        initial_data_count = len(data)
        scrape_datasets(page_url)
        if len(
                data
        ) == initial_data_count: 
            break
        skip += take


    with open('uci_datasets.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


    print("Scraping terminé. Les données ont été sauvegardées dans 'uci_datasets.csv'.")


scrape_uci_datasets()

```

Une fois que vous exécutez le script, il s'exécutera pendant un certain temps jusqu'à ce que le terminal affiche "Aucun lien de jeu de données trouvé", suivi de "Scraping terminé. Les données ont été sauvegardées dans 'uci_datasets.csv'", indiquant que les données scrapées ont été sauvegardées dans un fichier CSV.

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXdRUvJJsu32oaxdattur__98CEF9GvqQMDTDQzpqS-NW3I2-haF5tfWH_mIBFwEhAqLhUhURVKCNFJE-b1bRzeZtz2oApWePqLZqWahKT0uhoXN0Ok7JJQnWN32dWQOHclZ2y9hg2MdqvoLDhToy-gCj9o?key=f_hrU3B_rjNJFpKZiiV3Pw)

Pour voir les données scrapées, ouvrez le fichier 'uci_datasets.csv', vous devriez pouvoir voir les données organisées par Nom du jeu de données, Date de donation, Description, Caractéristiques, Domaine, etc.

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXd1ZkPzSyPxZ3KsZklCPPcruSll4xUBxm3KiNdageDzHK-wbTxG7v8HLFpoJ-gMvIpdKPxzoshzRlmNjiPeVcbvse14gdGFHu7Wm89UgTACtImpToHOkqcU29S6s31CzC_T20h1bUO4w0D9sLFC_5Tmy3o?key=f_hrU3B_rjNJFpKZiiV3Pw)
_Données organisées par Nom du jeu de données, Date de donation, Description, Caractéristiques, Domaine, etc._

Vous pouvez avoir une meilleure vue des données si vous ouvrez le fichier via Excel.

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXfdmf621HGzQNHCdgxTJ6cvl2YEpuAq5hfvqpE9KrbZ8kDkGo6R3YIYpCFMmNoY8z29YEfcesZap9hpxiLc3fwHEyzLdo6dNQGNExRdam3t3taUebgKL_ocDFXyo2KhhMTpGDod2sUQI5miEUp_UCyNPZo?key=f_hrU3B_rjNJFpKZiiV3Pw)
_Données organisées dans un fichier Excel_

En suivant la logique mentionnée dans cet article, vous pouvez scraper de nombreux sites. Tout ce que vous avez à faire est de commencer par l'URL de base, de comprendre comment naviguer dans la liste et d'aller à la page dédiée pour chaque élément de la liste. Ensuite, identifiez les éléments de page appropriés comme les IDs et les classes où vous pouvez isoler et extraire les données que vous voulez.

Vous devez également comprendre la logique derrière la pagination. Le plus souvent, la pagination apporte des modifications mineures à l'URL, que vous pouvez utiliser pour boucler d'une page à l'autre.

Enfin, vous pouvez écrire les données dans un fichier CSV, qui est adapté pour le stockage et comme entrée pour la visualisation.

## **Conclusion**

L'utilisation de Python avec Requests et Beautiful Soup vous permet de créer des scrapers Web entièrement fonctionnels pour extraire des données de sites Web. Bien que cette fonctionnalité puisse être hautement avantageuse pour la prise de décisions basée sur les données, il est important de garder à l'esprit les considérations éthiques et légales.

Une fois que vous devenez familier avec les méthodes utilisées dans ce script, vous pouvez explorer des techniques comme la gestion de proxy et la persistance des données. Vous pouvez également vous familiariser avec d'autres bibliothèques comme Scrapy, Selenium et Puppeteer pour répondre à vos besoins de collecte de données.

Merci d'avoir lu ! Je suis Jess, et je suis une experte chez Hyperskill. Vous pouvez consulter mon cours de développeur **Python** sur la plateforme.