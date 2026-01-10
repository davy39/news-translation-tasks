---
title: Une recette pour les tests automatisés de sites web avec Python Selenium &
  Headless Chrome dans Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-16T10:58:19.000Z'
originalURL: https://freecodecamp.org/news/a-recipe-for-website-automated-tests-with-python-selenium-headless-chrome-in-docker-8d344a97afb5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LFMkcmJNOOgGK1qyKYebLw.jpeg
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: women in tech
  slug: women-in-tech
seo_title: Une recette pour les tests automatisés de sites web avec Python Selenium
  & Headless Chrome dans Docker
seo_desc: 'By Joyz

  The QA team leads bug catching, but manual testing is not scalable when your company
  takes on more projects. Since my company sends builds every two weeks, the QA team
  wants to test every build before we pass them to our clients.

  To improve Q...'
---

Par Joyz

L'équipe QA mène la chasse aux bugs, mais les tests manuels ne sont pas évolutifs lorsque votre entreprise prend en charge plus de projets. Puisque mon entreprise envoie des builds toutes les deux semaines, l'équipe QA veut tester chaque build avant de les transmettre à nos clients.

Pour améliorer la QA, j'ai aidé à modifier les processus de gestion de projet, recruté une équipe de testeurs exploratoires et construit des outils de test automatisés pour l'intégration continue en tant qu'ingénieur QA. La plupart des outils que je construis utilisent des bibliothèques open-source ou gratuites.

Ci-dessous se trouve un guide pour mon dépôt open-source [Github repo](https://hub.docker.com/r/joyzoursky/python-chromedriver/) avec plus de 100 000 téléchargements d'images docker pour aider les équipes de développement et les développeurs freelance à configurer leurs propres tests automatisés.

### Notre Tâche

Nous allons passer par le processus étape par étape pour voir comment configurer un test avec [Selenium](https://www.seleniumhq.org/), qui automatise les navigateurs pour effectuer des tests. Dans cet exemple, nous utiliserons Chrome headless pour charger notre site web et effectuer un simple clic sur le bouton que nous voulons tester sur le site.

### Configuration de Chrome headless

Démarrer un navigateur Chrome dans Docker pour exécuter un test Selenium prend seulement une minute. Une fois que cela fonctionne, cela fonctionne avec n'importe quel build CI automatisé.

Voici un exemple :

Tout d'abord, ouvrez votre terminal et allez dans votre répertoire de travail.

```
$ cd [votre répertoire de travail]
```

Ensuite, tirez et exécutez cette image docker depuis [joyzoursky/python-chromedriver](https://hub.docker.com/r/joyzoursky/python-chromedriver/). Nous allons exécuter le test Selenium à l'intérieur du conteneur Docker.

```
$ docker run -it -v $(pwd):/usr/workspace joyzoursky/python-chromedriver:3.6-alpine3.7-selenium shUnable to find image 'joyzoursky/python-chromedriver:3.6-alpine3.7-selenium' locally3.6-alpine3.7-selenium: Pulling from joyzoursky/python-chromedriverff3a5c916c92: Pull complete471170bb1257: Pull completed487cc70216e: Pull complete9358b3ca3321: Pull complete78b9945f52f1: Pull complete66eb40d9fb29: Pull complete36cb996dbd54: Pull complete8e6f0ca23b1a: Pull completed5a3895f190c: Pull completeDigest: sha256:c51c240f1a472b0f252e96cd39678c7d039b757b83e46bf8ed182e95caaf02e7Status: Downloaded newer image for joyzoursky/python-chromedriver:3.6-alpine3.7-selenium
```

Maintenant, le conteneur est prêt. Passons à l'espace de travail et essayons le code.

```
/ # cd /usr/workspace/
```

### Maintenant, nous pouvons écrire notre test

Démarrons Python.

```
/usr/workspace # pythonPython 3.6.4 (default, Jan 10 2018, 05:20:21)[GCC 6.4.0] on linuxType "help", "copyright", "credits" or "license" for more information.>>>
```

Avant d'essayer le code, importons le webdriver Selenium depuis le package préinstallé.

```
>>> from selenium import webdriver
```

Ensuite, démarrons Chrome headless. Certaines options sont requises pour éviter les plantages lors du démarrage.

```
>>> chrome_options = webdriver.ChromeOptions()>>> chrome_options.add_argument('--no-sandbox')>>> chrome_options.add_argument('--window-size=1420,1080')>>> chrome_options.add_argument('--headless')>>> chrome_options.add_argument('--disable-gpu')>>> driver = webdriver.Chrome(chrome_options=chrome_options)
```

Maintenant, le navigateur est déjà ouvert dans le conteneur, mais nous ne pouvons pas le voir. Essayons d'aller sur ce site web et de vérifier le texte interne du bouton en haut à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/d8pHoiJdyENTGuhTRqyEMGsJ2NufawIOAFfQ)

```
>>> driver.get('https://www.oursky.com/')>>> el = driver.find_element_by_class_name('btn-header')>>> el.text'START YOUR PROJECT'
```

Trouvons l'élément avec lequel nous voulons interagir, par exemple le bouton dans l'en-tête "btn-header".

C'est bon ! Maintenant, essayons de déclencher un clic sur le bouton.

```
>>> el.click()>>> driver.current_url'https://oursky.com/enquiry/general/'
```

Succès ! Le driver va à l'URL attendue après avoir cliqué sur le bouton.

Vous pouvez maintenant exécuter vos scripts dans le conteneur, ou utiliser l'image dans un script de build CI. Vous pouvez également construire votre propre image avec plus de packages pip installés, afin de pouvoir automatiser des tests plus puissants.

Profitez-en !

Vous pouvez trouver le [dépôt GitHub de l'image docker](https://github.com/joyzoursky/docker-python-chromedriver) ici avec l'environnement de test configuré.

Jetez également un coup d'œil à l'exemple complet de [script Python Selenium](https://github.com/joyzoursky/selenium-template), afin de pouvoir le personnaliser pour votre propre test.

![Image](https://cdn-media-1.freecodecamp.org/images/0pEr4VFOcP6iQEO9cTpQjFwcPGq2Jq4Qlzyr)

_Je travaille pour l'entreprise de développement de logiciels basée à Hong Kong et à Taïwan [Oursky](https://oursky.com). Nous construisons des produits numériques pour les clients et des [outils pour développeurs](https://oursky.com/products/) comme notre BaaS open source, Skygear, qui aide les développeurs à construire des applications plus rapidement._