---
title: Une introduction au web scraping avec lxml et Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T19:17:26.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-web-scraping-with-lxml-and-python-b02b7a3f3098
coverImage: https://cdn-media-1.freecodecamp.org/images/0*AXQfWm6LMJwLwS2f.png
tags:
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: web scraping
  slug: web-scraping
seo_title: Une introduction au web scraping avec lxml et Python
seo_desc: 'By Timber.io

  Why should you bother learning how to web scrape? If your job doesn’t require you
  to learn it, then let me give you some motivation.

  What if you want to create a website which curates the cheapest products from Amazon,
  Walmart, and a cou...'
---

Par Timber.io

Pourquoi devriez-vous vous donner la peine d'apprendre le web scraping ? Si votre travail ne vous oblige pas à l'apprendre, laissez-moi vous donner une motivation.

Et si vous souhaitez créer un site web qui recense les produits les moins chers d'Amazon, Walmart et quelques autres magasins en ligne ? Beaucoup de ces magasins en ligne ne vous fournissent pas un moyen facile d'accéder à leurs informations via une API. En l'absence d'une API, votre seul choix est de créer un web scraper. Cela vous permet d'extraire des informations de ces sites web automatiquement et rend ces informations faciles à utiliser.

Voici un exemple de réponse typique d'une API en JSON. Il s'agit de la réponse de Reddit :

![Image](https://cdn-media-1.freecodecamp.org/images/3AAHh7eokTALm4tw82sQT-Kl3zzeqZlo6CYy)

Il existe de nombreuses bibliothèques Python qui peuvent vous aider avec le web scraping. Il y a [lxml](http://lxml.de/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/?), et un framework complet appelé [Scrapy](https://scrapy.org/).

La plupart des tutoriels discutent de BeautifulSoup et Scrapy, donc j'ai décidé d'utiliser lxml dans cet article. Je vais vous enseigner les bases des XPaths et comment vous pouvez les utiliser pour extraire des données d'un document HTML. Je vais vous guider à travers quelques exemples différents afin que vous puissiez rapidement vous familiariser avec lxml et les XPaths.

### Obtenir les données

Si vous êtes un gamer, vous connaissez déjà (et probablement aimez) ce site web. Nous allons essayer d'extraire des données de [Steam](https://store.steampowered.com/). Plus spécifiquement, nous allons sélectionner les informations des "[nouvelles sorties populaires](https://store.steampowered.com/explore/new/)".

Je divise ce processus en une série de deux parties. Dans cette partie, nous allons créer un script Python qui peut extraire les noms des jeux, les prix des jeux, les différentes étiquettes associées à chaque jeu et les plateformes cibles. Dans la deuxième partie, nous transformerons ce script en une API basée sur Flask et l'hébergerons sur Heroku.

![Image](https://cdn-media-1.freecodecamp.org/images/o-MbyodJMiNMhSvwE7HLEBpgDx2pbx0Fmekd)

Tout d'abord, ouvrez la page des "[nouvelles sorties populaires](https://store.steampowered.com/explore/new/)" sur Steam et faites défiler jusqu'à ce que vous voyiez l'onglet des Nouvelles Sorties Populaires. À ce stade, j'ouvre généralement les outils de développement de Chrome et je vois quelles balises HTML contiennent les données requises. J'utilise extensivement l'outil d'inspection d'éléments (le bouton en haut à gauche des outils de développement). Il vous permet de voir le balisage HTML derrière un élément spécifique de la page en un seul clic.

En tant qu'aperçu de haut niveau, tout sur une page web est encapsulé dans une balise HTML, et les balises sont généralement imbriquées. Vous devez déterminer quelles balises vous devez extraire pour obtenir les données, et vous serez prêt à partir. Dans notre cas, si nous regardons, nous pouvons voir que chaque élément de liste séparé est encapsulé dans une balise d'ancrage (`a`).

![Image](https://cdn-media-1.freecodecamp.org/images/UB6gYciEusxfGnCix3bcaXkHTCHKkyr-J5KY)

Les balises d'ancrage elles-mêmes sont encapsulées dans la `div` avec un id de `tab_newreleases_content`. Je mentionne l'id car il y a deux onglets sur cette page. Le deuxième onglet est l'onglet standard "Nouvelles Sorties", et nous ne voulons pas extraire d'informations de cet onglet. Nous allons donc d'abord extraire l'onglet "Nouvelles Sorties Populaires", puis nous extrairons les informations requises de cette balise.

C'est le moment idéal pour créer un nouveau fichier Python et commencer à écrire notre script. Je vais créer un fichier `scrape.py`. Maintenant, importons les bibliothèques requises. La première est la bibliothèque `[requests](http://docs.python-requests.org/)` et la seconde est la bibliothèque `[lxml.html](http://lxml.de/)`.

```
import requests
import lxml.html
```

Si vous n'avez pas `requests` installé, vous pouvez facilement l'installer en exécutant cette commande dans le terminal :

```
$ pip install requests
```

La bibliothèque requests va nous aider à ouvrir la page web en Python. Nous aurions pu utiliser `lxml` pour ouvrir la page HTML également, mais cela ne fonctionne pas bien avec toutes les pages web. Pour être du bon côté, je vais utiliser `requests`.

### Extraction et traitement des informations

Maintenant, ouvrons la page web en utilisant requests et passons cette réponse à `lxml.html.fromstring`.

```
html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)
```

Cela nous fournit un objet de type `HtmlElement`. Cet objet dispose de la méthode `xpath` que nous pouvons utiliser pour interroger le document HTML. Cela nous fournit un moyen structuré d'extraire des informations d'un document HTML.

Maintenant, sauvegardez ce fichier et ouvrez un terminal. Copiez le code du fichier `scrape.py` et collez-le dans une session d'interpréteur Python.

![Image](https://cdn-media-1.freecodecamp.org/images/StkkSYH4Gr4mbmXuPj8mtkDQtuIpT8nA4WmO)

Nous faisons cela pour pouvoir tester rapidement nos XPaths sans avoir à éditer, sauvegarder et exécuter continuellement notre fichier `scrape.py`.

Essayons d'écrire un XPath pour extraire la div qui contient l'onglet "Nouvelles Sorties Populaires". Je vais expliquer le code au fur et à mesure :

```
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
```

Cette instruction renverra une liste de toutes les `divs` dans la page HTML qui ont un id de `tab_newreleases_content`. Maintenant, comme nous savons qu'une seule div sur la page a cet id, nous pouvons prendre le premier élément de la liste (`[0]`) et ce serait notre `div` requise. Décomposons le `xpath` et essayons de le comprendre :

* `//` ces doubles barres obliques indiquent à `lxml` que nous voulons rechercher toutes les balises dans le document HTML qui correspondent à nos exigences/filtres. Une autre option est d'utiliser `/` (une seule barre oblique). La barre oblique unique renvoie uniquement les balises/nœuds enfants immédiats qui correspondent à nos exigences/filtres
* `div` indique à `lxml` que nous recherchons des `divs` dans la page HTML
* `[@id="tab_newreleases_content"]` indique à `lxml` que nous ne sommes intéressés que par les `divs` qui ont un id de `tab_newreleases_content`

Super ! Nous avons la `div` requise. Maintenant, retournons à Chrome et vérifions quelle balise contient les titres des sorties.

![Image](https://cdn-media-1.freecodecamp.org/images/L9fPrMkTIwhdbwklG9-0X9gZl3e0ko3OuuBF)

Le titre est contenu dans une div avec une classe de `tab_item_name`. Maintenant que nous avons extrait l'onglet "Nouvelles Sorties Populaires", nous pouvons exécuter d'autres requêtes XPath sur cet onglet. Écrivez le code suivant dans la même console Python dans laquelle nous avons exécuté notre code précédemment :

```
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
```

Cela nous donne les titres de tous les jeux dans l'onglet "Nouvelles Sorties Populaires". Voici la sortie attendue :

![Image](https://cdn-media-1.freecodecamp.org/images/Xhf8xeRmP1HcnQylCKcRICVcP3wS49jhKyHt)

Décomposons un peu ce XPath, car il est un peu différent du précédent.

* `.` indique à lxml que nous ne sommes intéressés que par les balises qui sont les enfants de la balise `new_releases`
* `[@class="tab_item_name"]` est assez similaire à la façon dont nous filtrions les `divs` en fonction de l'`id`. La seule différence est que ici nous filtrons en fonction du nom de la classe
* `/text()` indique à lxml que nous voulons le texte contenu dans la balise que nous venons d'extraire. Dans ce cas, il renvoie le titre contenu dans la div avec le nom de classe `tab_item_name`

Maintenant, nous devons extraire les prix des jeux. Nous pouvons facilement le faire en exécutant le code suivant :

```
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')
```

Je ne pense pas avoir besoin d'expliquer ce code, car il est très similaire au code d'extraction des titres. Le seul changement que nous avons apporté est le changement du nom de la classe.

![Image](https://cdn-media-1.freecodecamp.org/images/2fnisL0yYetblYk1s8JTw8KMVDq5IyiRBItW)

Maintenant, nous devons extraire les étiquettes associées aux titres. Voici le balisage HTML :

![Image](https://cdn-media-1.freecodecamp.org/images/Z88XEIzl3gg9Y94h2j9hNiQviV8N22ttfQnL)

Écrivez le code suivant dans le terminal Python pour extraire les étiquettes :

```
tags = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
total_tags = []
for tag in tags:
    total_tags.append(tag.text_content())
```

Ce que nous faisons ici, c'est extraire les `divs` contenant les étiquettes pour les jeux. Ensuite, nous parcourons la liste des étiquettes extraites et nous extrayons le texte de ces étiquettes en utilisant la méthode `[text_content()](http://lxml.de/lxmlhtml.html#html-element-methods)`. `text_content()` renvoie le texte contenu dans une balise HTML sans le balisage HTML.

**Note :** Nous aurions également pu utiliser une compréhension de liste pour rendre ce code plus court. Je l'ai écrit de cette manière afin que même ceux qui ne connaissent pas les compréhensions de liste puissent comprendre le code. Dans tous les cas, voici le code alternatif :

```
tags = [tag.text_content() for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]')]
```

![Image](https://cdn-media-1.freecodecamp.org/images/hcRXlOSBvpuEiek51XbZeBtrqtN2ubKimKmt)

Séparons les étiquettes dans une liste également, afin que chaque étiquette soit un élément séparé :

```
tags = [tag.split(', ') for tag in tags]
```

Maintenant, la seule chose restante est d'extraire les plateformes associées à chaque titre. Voici le balisage HTML :

![Image](https://cdn-media-1.freecodecamp.org/images/SckW1McK61WTzv0v0aaDUJb2eVAcQejKMvn-)

La principale différence ici est que les plateformes ne sont pas contenues en tant que textes dans une balise spécifique. Elles sont listées comme nom de classe. Certains titres n'ont qu'une seule plateforme associée, comme ceci :

```
<span class="platform_img win">&lt;/span>
```

Alors que certains titres ont 5 plateformes associées, comme ceci :

```
<span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span><span class="platform_img hmd_separator"></span> <span title="HTC Vive" class="platform_img htcvive"></span> <span title="Oculus Rift" class="platform_img oculusrift"></span>
```

Comme nous pouvons le voir, ces `spans` contiennent le type de plateforme comme nom de classe. La seule chose commune entre ces `spans` est que tous contiennent la classe `platform_img`. Tout d'abord, nous allons extraire les `divs` avec la classe `tab_item_details`. Ensuite, nous allons extraire les `spans` contenant la classe `platform_img`. Enfin, nous allons extraire le deuxième nom de classe de ces `spans`. Voici le code :

```
platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []
for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)
```

À la **ligne 1**, nous commençons par extraire la `div` `tab_item_details`. Le XPath à la **ligne 5** est un peu différent. Ici, nous avons `[contains(@class, "platform_img")]` au lieu de simplement avoir `[@class="platform_img"]`. La raison est que `[@class="platform_img"]` renvoie les `spans` qui ont uniquement la classe `platform_img` associée. Si les `spans` ont une classe supplémentaire, ils ne seront pas renvoyés. Alors que `[contains(@class, "platform_img")]` filtre tous les `spans` qui ont la classe `platform_img`. Peu importe si c'est la seule classe ou s'il y a plus de classes associées à cette balise.

À la **ligne 6**, nous utilisons une compréhension de liste pour réduire la taille du code. La méthode `.get()` nous permet d'extraire un attribut d'une balise. Ici, nous l'utilisons pour extraire l'attribut `class` d'un `span`. Nous obtenons une chaîne de caractères en retour de la méthode `.get()`. Dans le cas du premier jeu, la chaîne renvoyée est `platform_img win`, donc nous divisons cette chaîne en fonction de la virgule et de l'espace. Ensuite, nous stockons la dernière partie (qui est le nom réel de la plateforme) de la chaîne divisée dans la liste.

Aux **lignes 7-8**, nous supprimons le `hmd_separator` de la liste s'il existe. Cela est dû au fait que `hmd_separator` n'est pas une plateforme. C'est simplement une barre de séparation verticale utilisée pour séparer les plateformes réelles du matériel VR/AR.

Voici le code que nous avons jusqu'à présent :

```
import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')
tags = [tag.text_content() for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]')]
tags = [tag.split(', ') for tag in tags]
platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []
for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)
```

Maintenant, nous devons simplement renvoyer une réponse JSON afin de pouvoir facilement transformer cela en une API basée sur Flask. Voici le code :

```
output = []
for info in zip(titles, prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)
```

Ce code est explicite. Nous utilisons la fonction `[zip](https://docs.python.org/3/library/functions.html#zip)` pour parcourir toutes ces listes en parallèle. Ensuite, nous créons un dictionnaire pour chaque jeu et attribuons le titre, le prix, les étiquettes et les plateformes comme une clé séparée dans ce dictionnaire. Enfin, nous ajoutons ce dictionnaire à la liste de sortie.

### Conclusion

Dans le prochain article, nous verrons comment convertir cela en une API basée sur Flask et l'héberger sur Heroku.

Je suis [Yasoob](http://yasoob.me/) de [Python Tips](https://pythontips.com/). J'espère que vous avez apprécié ce tutoriel. Si vous souhaitez lire plus de tutoriels de ce type, veuillez vous rendre sur [Python Tips](https://pythontips.com/). J'écris régulièrement des conseils, astuces et tutoriels sur Python sur ce blog. Et si vous êtes intéressé par l'apprentissage de Python intermédiaire, alors veuillez consulter mon livre open source [ici](http://book.pythontips.com/).

**_Juste une mise en garde : nous sommes une entreprise de journalisation [ici @ Timber](http://timber.io). Nous aimerions que vous essayiez notre produit (il est vraiment génial !), mais vous êtes ici pour apprendre le web scraping en Python et nous ne voulions pas vous en détourner._**

![Image](https://cdn-media-1.freecodecamp.org/images/M2arEU7akD9w2V4YapbwHr9u0axtZQfxy9q5)

_Publié à l'origine sur [timber.io](https://timber.io/blog/an-intro-to-web-scraping-with-lxml-and-python/).