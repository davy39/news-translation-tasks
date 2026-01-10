---
title: Comment extraire des données de plusieurs pages web en utilisant Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-14T19:48:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-scrape-multiple-web-pages-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/How-to-Scrape-Multiple-Web-Pages-Using-Python-1.png
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: Comment extraire des données de plusieurs pages web en utilisant Python
seo_desc: "By Shittu Olumide\nData is all around us. Every website you visit includes\
  \ data in a readable format that you can utilize for a project. \nAnd although you\
  \ can easily copy and paste the data, the best approach for big amounts of data\
  \ is to perform web ..."
---

Par Shittu Olumide

Les données sont partout autour de nous. Chaque site web que vous visitez contient des données dans un format lisible que vous pouvez utiliser pour un projet. 

Et bien que vous puissiez facilement copier et coller les données, la meilleure approche pour de grandes quantités de données est d'effectuer du web scraping.

Apprendre le web scraping peut être délicat au début, mais avec une bonne bibliothèque de web scraping, les choses deviendront beaucoup plus faciles. 

Le web scraping peut être un outil utile pour collecter des données et des informations, mais il est important de s'assurer que vous le faites de manière sûre et légale. 

Voici quelques conseils pour effectuer le web scraping correctement :

* Demandez la permission avant de scraper un site.
* Lisez et comprenez les conditions d'utilisation du site web et le fichier robots.txt.
* Limitez la fréquence de votre scraping.
* Utilisez des outils de web scraping qui respectent les conditions d'utilisation des propriétaires de sites web.

Maintenant que vous comprenez la bonne manière d'aborder le scraping, plongeons dans le vif du sujet. Dans ce tutoriel étape par étape, nous allons passer en revue comment scraper plusieurs pages d'un site web en utilisant le module de web scraping le plus convivial de Python, Beautiful Soup.

Ce tutoriel sera divisé en deux parties : nous allons scraper une seule page dans la première phase. Ensuite, dans la deuxième section, nous scraperons plusieurs pages en nous basant sur le code utilisé dans la première section.

## Prérequis 

**Python 3** : vous devrez utiliser Python 3 pour ce tutoriel, car la bibliothèque que nous allons utiliser est une bibliothèque Python. Pour télécharger et installer Python, consultez le site officiel [website](https://www.python.org/downloads/).

**Beautiful Soup** : Beautiful Soup est un package Python pour l'analyse de données structurées. Pour les pages analysées, il génère un arbre d'analyse que vous pouvez utiliser pour extraire des données à partir de HTML. Il vous permet d'interagir avec HTML de la même manière que vous pouvez interagir avec une page web en utilisant les outils de développement. 

Pour commencer à l'utiliser, lancez votre terminal et installez Beautiful Soup :

```bash
pip install beautifulsoup4

```

**Bibliothèque Requests** : La [bibliothèque requests](https://pypi.org/project/requests/) est la norme Python pour effectuer des requêtes HTTP. Nous allons l'utiliser en conjonction avec Beautiful Soup pour obtenir le HTML d'un site web.

```bash
pip install requests

```

**Installer un analyseur** : Pour extraire des données à partir de texte HTML, nous avons besoin d'un analyseur. Nous allons utiliser l'analyseur `lxml` ici. Pour installer cet analyseur, exécutez la commande suivante :

```bash
pip install lxml

```

**Note** : Vous n'avez pas besoin d'être un professionnel de Python pour suivre ce tutoriel.

## Comment scraper une seule page web

Comme je l'ai expliqué précédemment, nous allons commencer par comprendre comment scraper une seule page web. Ensuite, nous passerons au scraping de plusieurs pages web. 

Construisons notre premier scraper.

### Importer les bibliothèques

Tout d'abord, importons les bibliothèques dont nous aurons besoin :

```py
import requests
from bs4 import BeautifulSoup

```

### Obtenir le HTML du site web

Nous voulons scraper un site web avec des centaines de pages de transcriptions de films. Nous allons commencer par scraper une seule page, puis démontrer comment scraper plusieurs pages.  
  
Tout d'abord, nous allons définir la connexion. Dans cet exemple, nous allons utiliser la transcription du film Titanic, mais vous pouvez sélectionner n'importe quel film que vous souhaitez. 

Ensuite, nous faisons une `requête` au site web et recevons une réponse, que nous enregistrons dans la variable result. Après cela, nous allons utiliser la méthode `.text` pour récupérer le contenu du site web. 

Enfin, nous allons utiliser l'analyseur `lxml` pour obtenir le `soup`, qui est l'objet contenant toutes les données dans la structure imbriquée que nous allons réutiliser plus tard.

```py
website = 'https://subslikescript.com/movie/Titanic-120338'

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())

```

Une fois que nous avons l'objet `soup`, nous pouvons simplement obtenir du HTML lisible en utilisant `.prettify()`. Bien que nous puissions utiliser le HTML imprimé dans un éditeur de texte pour trouver des éléments, il est beaucoup plus facile d'aller directement au code HTML de l'élément que nous cherchons. Nous allons faire cela dans la phase suivante. 

### Examiner la page web et le code HTML

Avant de commencer à écrire du code, nous devons d'abord évaluer le site web que nous voulons scraper et le code HTML que nous avons obtenu pour identifier la meilleure stratégie pour scraper le site web. Un exemple de transcription est disponible ci-dessous. Les éléments à scraper sont le titre du film et la transcription.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screen-Shot-2023-02-10-at-16.45.28.png)
_Image montrant le titre et la transcription du film Titanic._

Pour obtenir le code HTML d'un élément donné, effectuez les étapes suivantes :

1. Naviguez jusqu'au site web de la transcription de Titanic.
2. Faites un clic droit sur le titre du film ou sur la transcription. Vous verrez une liste. Sélectionnez "Inspecter" pour voir le code source de la page.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screen-Shot-2023-02-10-at-17.00.05.png)
_Image montrant le code source de la page_

### Comment trouver un élément avec Beautiful Soup

Il est facile de trouver un élément dans Beautiful Soup. Il suffit d'appliquer la méthode `.find()` à la soupe précédemment préparée.

Par exemple, trouvez la boîte contenant le titre du film, la description et la transcription. Elle est dans une balise `article` et a la classe `main-article`. Nous pouvons utiliser le code suivant pour trouver cette boîte :

```py
box = soup.find('article', class_='main-article')

```

Le titre du film est enfermé dans une balise `h1` et ne possède pas de nom de classe. Après l'avoir trouvé, nous utilisons la fonction `.get_text()` pour récupérer le texte à l'intérieur du nœud :

```py
title = box.find('h1').get_text()

```

La transcription est incluse dans une balise `div` et a la classe `full-script`. Dans ce scénario, nous allons changer les arguments par défaut dans la fonction `.get_text()` pour obtenir le texte. 

Nous commençons par définir `strip=True` pour éliminer les espaces de début et de fin. Ensuite, nous ajoutons un espace vide au séparateur `separator=' '` pour nous assurer que les mots ont un espace vide après chaque nouvelle ligne `\n`.

```py
transcript = box.find('div', class_='full-script')
transcript = transcript.get_text(strip=True, separator=' ')

```

Jusqu'à présent, nous avons scrapé les données avec succès. Imprimez les variables `title` et `transcript` pour vous assurer que tout fonctionne correctement.

### Comment exporter des données dans un fichier .txt

Vous pouvez stocker des données dans des formats `CSV`, `JSON`, et autres. Dans cet exemple, nous allons sauvegarder les données extraites dans un fichier .txt. Pour ce faire, nous allons utiliser le mot-clé `with`, comme montré dans le code ci-dessous :

```py
with open(f'{title}.txt', 'w') as file:
    file.write(transcript)

```

N'oubliez pas d'utiliser la `f`-string pour définir le nom du fichier comme le titre du film. Après avoir exécuté le code, nous devrions avoir un fichier `.txt` dans notre répertoire de travail.

Nous sommes prêts à scraper des transcriptions de plusieurs pages maintenant que nous avons réussi à scraper des données d'une page web !

## Comment scraper plusieurs pages web

Sur la page de transcription, faites défiler vers le bas et cliquez sur [tous les scripts de films](https://subslikescript.com/movies). Vous pouvez le trouver en bas de la page web.  

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screen-Shot-2023-02-11-at-07.59.55.png)
_Toutes les pages de transcriptions_

La capture d'écran montre toutes les transcriptions de films. Le site web compte 1 757 pages, avec environ 30 transcriptions de films sur chaque page. 

Dans cette section, nous allons scraper plusieurs liens en obtenant l'attribut `href` de chaque lien. Tout d'abord, nous devons modifier le site web pour permettre le scraping. Notre nouvelle variable de site web sera la suivante :

```py
root = 'https://subslikescript.com'
website = f'{root}/movies'

```

La raison principale pour laquelle une variable `root` est définie dans le code est d'aider à scraper plusieurs pages web plus tard.

### Comment obtenir l'attribut href

Commençons par l'attribut `href` des 30 films sur une page. Examinez n'importe quel titre de film dans la boîte "Liste des transcriptions de films". 

Après cela, nous devrions avoir le code HTML. Une balise `a` devrait être mise en évidence en bleu. Chaque balise `a` appartient à un titre de film.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screen-Shot-2023-02-11-at-13.04.17.png)

Comme nous pouvons le voir, les liens dans le `href` n'incluent pas le domaine racine subslikescript.com. C'est pourquoi nous avons créé une variable racine avant de la concaténer.

Recherchons tous les éléments `a` sur la page.

### Comment trouver plusieurs éléments

Dans Beautiful Soup, nous utilisons la méthode `.find_all()` pour localiser plusieurs éléments. Pour extraire le lien qui correspond à chaque transcription de film, nous devons inclure le paramètre `href=True`.

```py
box.find_all('a', href=True)

```

Pour obtenir les liens à partir du href, ajoutez `['href']` à l'expression ci-dessus. Cependant, comme la méthode `.find_all()` retourne une liste, nous devons boucler à travers elle et obtenir les `hrefs` un par un dans la boucle.

```py
for link in box.find_all('a', href=True):
    link['href']

```

Nous pouvons utiliser la compréhension de liste pour sauvegarder les liens, comme montré ci-dessous :

```py
links = [link['href'] for link in box.find_all('a', href=True)]
print(links)

```

Les liens que nous voulons scraper seront visibles si vous imprimez la liste des liens. Dans l'étape suivante, nous allons scraper chaque page.

### Comment boucler à travers chaque lien

Pour scraper la transcription de chaque lien, nous allons répéter les étapes que nous avons utilisées pour la première transcription. Cette fois, nous allons mettre ces étapes à l'intérieur de la boucle `for` ci-dessous.

```py
for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

```

Comme vous vous en souvenez peut-être, les liens que nous avons précédemment sauvegardés n'incluaient pas la racine `subslikescript.com`, nous devons donc la concaténer avec l'expression `f'{root}/{link}'`.

Le reste du code est identique à ce que nous avons écrit dans la première section de ce guide.

## Conclusion

Si vous souhaitez parcourir les pages web, vous avez deux options.

* Vérifiez n'importe laquelle des pages visibles sur la page web (par exemple, 1, 2, 3 ou 1757). Obtenez la balise `a` avec l'attribut `href` ainsi que les liens pour chaque page. Lorsque vous avez les liens, combinez-les avec la racine et procédez comme décrit dans la section 2 après l'avoir fait.
* Visitez la page 2 et copiez le lien que vous voyez là. Voici à quoi il devrait ressembler : `subslikescript.com/movies?page=2`. Vous pouvez voir que le site web a un format cohérent pour chaque page : `f'{website}?page={i}'`. Si vous voulez parcourir les dix premières pages, vous pouvez réutiliser la variable website et boucler entre 1 et 10.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.freecodecamp.org/news/p/596c046e-0ba5-4a99-bf4d-eb3e0bebe75c/linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !