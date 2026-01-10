---
title: Comment scraper des sites web en utilisant Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T11:26:40.000Z'
originalURL: https://freecodecamp.org/news/scrap-websites-using-python-c0c7ad41d2dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*M0ip5ay8z72peBXvwXZSqQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: web scraping
  slug: web-scraping
seo_title: Comment scraper des sites web en utilisant Python
seo_desc: 'By Devanshu Jain

  It is that time of the year when the air is filled with the claps and cheers of
  4 and 6 runs during the Indian Premier League Cricket T20 tournament followed by
  the ICC Cricket World Cup in England. And how can we forget the election...'
---

Par Devanshu Jain

C'est cette période de l'année où l'air est rempli d'applaudissements et de cris de 4 et 6 runs pendant le tournoi de cricket T20 de la [Indian Premier League](https://www.iplt20.com/) suivi de la Coupe du Monde de Cricket ICC en Angleterre. Et comment pouvons-nous oublier les résultats des élections du plus grand pays démocratique du monde, l'Inde, qui seront connus dans les prochaines semaines ?

Pour rester informé de qui obtiendra le titre de l'IPL de cette année ou de quel pays remportera la Coupe du Monde ICC en 2019 ou de l'avenir du pays dans les 5 prochaines années, nous devons constamment être connectés à Internet.

Mais si vous êtes comme moi et ne pouvez pas passer beaucoup de temps sur Internet, mais avez un fort désir de rester informé de tous ces titres, alors cet article est pour vous. Alors sans perdre de temps, commençons !

![Image](https://cdn-media-1.freecodecamp.org/images/dySuWsAk2qARPtM0cOs88-YztYwzc1fWPz1F)
_Photo par [Unsplash](https://unsplash.com/photos/sScmok4Iq1o?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Balázs Kétyi</a> sur <a href="https://unsplash.com/search/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Il existe deux moyens d'accéder aux informations mises à jour. L'un est par le biais des API fournies par ces sites médias, et l'autre est par le biais du Web/Content Scraping.

La méthode API est trop simple, et probablement la meilleure façon d'obtenir des informations mises à jour est d'appeler l'interface de programmation associée. Mais malheureusement, tous les sites web ne fournissent pas d'API publiques accessibles. Le seul moyen qui nous reste est donc le Web Scraping.

### **Web Scraping**

Le web scraping est une technique permettant d'extraire des informations des sites web. Cette technique se concentre principalement sur la transformation de données non structurées (format HTML) sur le web en données structurées (base de données ou feuille de calcul). Le web scraping peut impliquer l'accès direct au web en utilisant HTTP, ou par le biais d'un navigateur web.

Dans cet article, nous utiliserons Python pour créer un bot permettant de scraper le contenu des sites web.

### **Processus de travail**

* Obtenir l'URL de la page à partir de laquelle nous voulons extraire/scraper les données
* Copier/télécharger le contenu HTML de la page
* Analyser le contenu HTML et obtenir les données requises

Le flux ci-dessus nous aide à naviguer vers l'URL de la page requise, à obtenir son contenu HTML et à analyser les données requises. Mais parfois, il y a des cas où nous devons d'abord nous connecter au site web, puis naviguer vers un emplacement spécifique pour obtenir les données requises. Dans ce cas, cela ajoute une étape supplémentaire de connexion au site web.

### **Paquets**

Pour analyser le contenu HTML et obtenir les données requises, nous utilisons la bibliothèque **Beautiful Soup**. C'est un package Python amazing pour analyser les documents HTML et XML. Consultez-le [ici](https://code.launchpad.net/beautifulsoup/).

Pour se connecter au site web, naviguer vers l'URL requise dans la même session et télécharger le contenu HTML, nous utiliserons la bibliothèque **Selenium**. [Selenium Python](https://selenium-python.readthedocs.io/) aide à cliquer sur les boutons, à entrer du contenu dans les structures, et bien plus encore.

### **Plongez directement dans le code**

Tout d'abord, nous importons toutes les bibliothèques que nous allons utiliser.

```
# importing librariesfrom selenium import webdriverfrom bs4 import BeautifulSoup
```

Ensuite, nous devons donner au pilote du navigateur le chemin vers Selenium pour initier notre navigateur web (Google Chrome). Et si nous ne voulons pas que notre bot affiche l'interface graphique du navigateur, nous pouvons ajouter l'option **headless** à Selenium. Les navigateurs headless fournissent un contrôle automatisé d'une page web dans un environnement similaire aux navigateurs web populaires, mais sont exécutés via une interface de ligne de commande ou en utilisant des communications réseau.

```
# chrome driver pathchromedriver = '/usr/local/bin/chromedriver'options = webdriver.ChromeOptions()options.add_argument('headless')  # for opening headless browser
```

```
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
```

Après avoir configuré l'environnement en définissant le navigateur et en installant les bibliothèques, nous allons nous attaquer au HTML. Naviguez vers la page de connexion et trouvez l'email, le mot de passe et l'identifiant, la classe ou le nom du champ du bouton de soumission pour entrer notre contenu dans la structure de la page.

```
# Navigating to the login pagebrowser.get('http://playsports365.com/default.aspx')
```

```
#Finding the tags by nameemail = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_UserName')
```

```
password = browser.find_element_by_name('ctl00$MainContent$ctlLogin$_Password')
```

```
login = browser.find_element_by_name('ctl00$MainContent$ctlLogin$BtnSubmit')
```

Ensuite, nous allons envoyer les identifiants dans ces balises HTML en cliquant sur le bouton de soumission pour entrer notre contenu dans la structure de la page.

```
# appending login credentialsemail.send_keys('********')password.send_keys('*******')
```

```
# clicking submit buttonlogin.click()
```

Une fois la connexion réussie, naviguez vers la page requise et obtenez le contenu HTML de la page

```
# After successful login, navigating to Open Bets Pagebrowser.get('http://playsports365.com/wager/OpenBets.aspx')
```

```
# Getting HTML content and parsing itrequiredHtml = browser.page_source
```

Maintenant, nous avons reçu le contenu HTML et la seule chose qui reste est d'analyser ce contenu. Nous allons analyser le contenu en utilisant les bibliothèques Beautiful Soup et html5lib. [**html5lib**](http://code.google.com/p/html5lib/) est un package Python qui implémente l'algorithme d'analyse HTML5 qui est fortement influencé par les navigateurs actuels. Dès que nous obtenons la structure normalisée du contenu analysé, nous pouvons trouver nos données présentes dans n'importe quelle balise enfant de la balise HTML. Nos données sont présentes dans la balise table et c'est pourquoi nous recherchons cette balise.

```
soup = BeautifulSoup(requiredHtml, 'html5lib')table = soup.findChildren('table')my_table = table[0]
```

Une fois que nous avons trouvé la balise parente, nous devons simplement parcourir récursivement ses enfants et imprimer les valeurs.

```
# fetching tags and printing valuesrows = my_table.findChildren(['th', 'tr'])for row in rows:    cells = row.findChildren('td')    for cell in cells:        value = cell.text        print (value)
```

Pour exécuter le programme ci-dessus, installez les bibliothèques Selenium, Beautiful Soup et html5lib en utilisant [pip](https://pip.pypa.io/en/stable/installing/). Après avoir installé les bibliothèques, taper `#python <program name>` imprimera les valeurs sur la console.

De cette manière, nous pouvons scraper et trouver des données sur n'importe quel site web.

Maintenant, si nous scrapons un site web qui change son contenu très fréquemment, comme les scores de cricket ou les résultats des élections en direct, nous pouvons exécuter ce programme dans un cron job et définir un intervalle pour le cron job.

En outre, nous pouvons également avoir les résultats affichés directement sur notre écran au lieu de la console en imprimant les résultats dans l'onglet de notification qui apparaît sur le bureau après un intervalle de temps particulier. Nous pouvons même partager ces valeurs sur un client de messagerie. Python dispose de bibliothèques riches qui peuvent nous aider avec tout cela.

Si vous voulez que je vous explique comment configurer un cron job et faire apparaître des notifications sur le bureau, n'hésitez pas à me le demander dans la section des commentaires.

Jusqu'à la prochaine fois, au revoir et j'espère que vous avez aimé l'article.