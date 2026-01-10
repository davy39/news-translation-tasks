---
title: Comment extraire facilement des informations de sites web en utilisant Standard
  Library et Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-12T07:14:10.000Z'
originalURL: https://freecodecamp.org/news/scrape-websites-for-information-easily-using-code-xyz-and-node-js-8be3e2f938ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*owqsessjwq39-cbYI5glLw.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment extraire facilement des informations de sites web en utilisant
  Standard Library et Node.js
seo_desc: 'By Janeth Ledezma

  A web scraper is a tool that allows us to select and transform a website’s unstructured
  data into a structured database. So where would a web scraper come in handy? I have
  listed my favorite use cases to get you excited about launch...'
---

Par Janeth Ledezma

Un scraper web est un outil qui permet de sélectionner et transformer les données non structurées d'un site web en une base de données structurée. Alors, dans quels cas un scraper web peut-il être utile ? J'ai listé mes cas d'utilisation préférés pour vous donner envie de lancer le vôtre !

![Image](https://cdn-media-1.freecodecamp.org/images/sjGtkAW7bu3T6pLz1Vv4oXLwUmpk8IZUiObt)
_[Cette question sur Quora](https://www.quora.com/What-are-examples-of-how-real-businesses-use-web-scraping-Are-there-any-types-of-businesses-which-use-this-more-than-others" rel="noopener" target="_blank" title=") m'a encouragée à créer mon propre scraper web._

* Extraire des annonces immobilières — les entreprises utilisent le web scraping pour collecter des propriétés déjà listées
* Extraire des produits/avis de produits depuis des sites de détaillants ou de fabricants pour les afficher sur votre site, fournir des comparatifs de spécifications/prix
* Extraire des sites d'actualités pour appliquer une analyse et une curation personnalisées (manuelle ou automatique), fournir des nouvelles mieux ciblées à votre audience
* Collecter des adresses e-mail pour la génération de leads

Vous pouvez lire d'autres cas d'utilisation pratiques pour un [scraper web ici](https://www.quora.com/What-are-examples-of-how-real-businesses-use-web-scraping-Are-there-any-types-of-businesses-which-use-this-more-than-others).

Maintenant, commençons ! Comme exemple simple — [nous allons extraire la page d'accueil de Hacker News](https://news.ycombinator.com/) pour récupérer les titres des liens.

_Si vous n'êtes pas encore familier avec [Standard Library](https://stdlib.com/?utm_source=content&utm_medium=blog&utm_campaign=scrape_service), vous allez être agréablement surpris ! [Standard Library](https://www.freecodecamp.org/news/scrape-websites-for-information-easily-using-code-xyz-and-node-js-8be3e2f938ab/undefined) est une plateforme de développement et de publication d'API qui peut vous aider à construire et déployer du code en un temps record en utilisant l'éditeur d'API en navigateur — [Code on Standard Library.](https://code.stdlib.com)_

### Étape Une : Connectez-vous à Code on Standard Library

La première étape consiste à vous rendre sur [https://code.stdlib.com](https://code.stdlib.com)/ et à créer un compte gratuit. [Code on Standard Library](https://code.stdlib.com) est un éditeur d'API en ligne développé par l'équipe de [Standard Library](https://stdlib.com/?utm_source=content&utm_medium=blog&utm_campaign=scrape_service) — un environnement de développement intégrable pour construire rapidement des API, des webhooks et des tâches d'automatisation de workflow.

Dans le coin inférieur gauche, cliquez sur **(se connecter)**. Si vous avez un compte [Standard](https://stdlib.com/?utm_source=content&utm_medium=blog&utm_campaign=scrape_service) [Library](https://stdlib.com/?utm_source=content&utm_medium=blog&utm_campaign=scrape_service), cliquez sur **Déjà inscrit**, et connectez-vous en utilisant vos identifiants [Standard Library](https://stdlib.com/?utm_source=content&utm_medium=blog&utm_campaign=scrape_service). Une fenêtre modale apparaîtra vous demandant de choisir un espace de noms (c'est votre nom d'utilisateur). Entrez votre e-mail et choisissez un mot de passe.

Après avoir créé votre compte, un module différent apparaîtra listant les plans d'abonnement. Un compte gratuit est tout ce dont vous avez besoin pour commencer, mais vous [pouvez en savoir plus sur les forfaits de prix de Standard Library ici](https://stdlib.com/pricing).

Une fois que vous cliquez sur **S'abonner + Gagner des crédits**, vous devriez voir un message de confirmation apparaître.

Cliquez sur **Continuer** pour revenir à la page d'accueil.

### Étape Deux : Sélectionnez le code source du Web Scraper

Sélectionnez le bouton **API à partir du code source**. Les [Standard Library](https://stdlib.com/?utm_source=content&utm_medium=blog&utm_campaign=scrape_service) Sourcecodes sont conçus pour rationaliser la création de différents types de projets. Les Sourcecodes fournissent des valeurs par défaut pour des éléments comme le code de base et la configuration des répertoires afin que vous puissiez vous concentrer directement sur le développement et la mise en œuvre de fonctionnalités plus complexes.

Vous devriez voir une liste de codes sources publiés. Faites défiler vers le bas et sélectionnez **@nemo/web-scraper**. Assurez-vous d'entrer le nom souhaité pour votre API et cliquez sur **Okay** (ou appuyez sur entrée)

Vous verrez alors le code de votre endpoint sous : `functions/__main__.js`

![Image](https://cdn-media-1.freecodecamp.org/images/fxvrAQ16nO2vIJyREwOXiFJjiJFiboO2JW5V)

Sur le côté droit, vous remarquerez une boîte de paramètres.

Dans le paramètre URL requis, tapez :

`[https://news.ycombinator.com/](https://news.ycombinator.com/)`

Dans les requêtes, tapez :

`[[".storylink", "text"]]`

Sélectionnez le bouton vert « **Exécuter** ».

En quelques secondes, vous devriez avoir une liste de titres de liens de la page d'accueil de [Hacker News](https://news.ycombinator.com/) sous la section **Résultats** de [Code on Standard Library](https://code.stdlib.com). Vous remarquerez un portail de documentation — copiez et collez l'URL de la documentation dans un nouvel onglet de votre navigateur pour voir les informations de votre API sur Standard Library.

![Image](https://cdn-media-1.freecodecamp.org/images/FWTfuTNbvtcxKG0f7g14zuDLZBsYAkvfEuKN)

### Comment ça marche ?

Le scraper web effectue une simple requête GET vers une URL, exécute une série de requêtes sur la page résultante et vous la retourne. Il utilise le puissant processeur DOM (Document Object Model) [cheerio](https://github.com/cheeriojs/cheerio), ce qui nous permet d'utiliser des [sélecteurs CSS](https://www.w3schools.com/cssref/css_selectors.asp) pour extraire des données de la page ! Les sélecteurs CSS sont des motifs utilisés pour sélectionner le ou les éléments que vous souhaitez organiser.

### **Comment interroger en utilisant des sélecteurs CSS**

Les pages web sont écrites en [langages de balisage](https://en.wikipedia.org/wiki/Markup_language) tels que HTML. [Un élément HTML](https://www.w3schools.com/Html/html_elements.asp) est un composant d'un document HTML ou d'une page web. Les éléments définissent la manière dont les informations sont affichées à l'œil humain sur le navigateur — des informations telles que des images, des multimédias, du texte, des feuilles de style, des scripts, etc.

Pour cet exemple, nous avons utilisé le sélecteur de « [.class](https://www.w3schools.com/cssref/css_selectors.asp) » (class = « storylink ») pour récupérer les titres de tous les hyperliens de tous les éléments de la page d'accueil de Hacker News.

Si vous vous demandez comment trouver les noms des éléments qui composent un site web — permettez-moi de vous montrer !

Lancez [Google Chrome](https://www.google.com/chrome/?brand=CHBD&gclid=EAIaIQobChMI87WK1Iya3AIVh_hkCh1hMgIIEAAYASAAEgKilfD_BwE&gclsrc=aw.ds&dclid=CLuW3dWMmtwCFcq5ZAodXTwHBA) et tapez notre URL [Hacker News](https://news.ycombinator.com/) `[https://news.ycombinator.com/](https://news.ycombinator.com/)`. Ensuite, faites un clic droit sur le titre de n'importe quel article et sélectionnez « **inspecter** ». Cela ouvrira la console web sur Google Chrome. Ou vous pouvez utiliser la **touche commande** (**⌘**) + **touche option** (**⌥**) + **touche J**.

![Image](https://cdn-media-1.freecodecamp.org/images/aI2tVsJLANFpuOdChy0O6gZHFN1HBe4Am4gF)
_Clic droit et sélectionnez Inspecter_

La console de développement web s'ouvrira à droite de votre écran. Remarquez que lorsque vous avez sélectionné le titre d'un lien, une section de la console est également mise en surbrillance. L'élément mis en surbrillance a une « classe » définie comme « storylink ». Et maintenant, vous savez comment trouver les noms des éléments sur n'importe quel site !

![Image](https://cdn-media-1.freecodecamp.org/images/b9U1cj2dENdmS6zTP3jrYIkdfngZm33Zh10Y)

Si vous souhaitez interroger différentes métadonnées sur [Hacker News](https://news.ycombinator.com/), survolez-les avec votre curseur. Ci-dessous, vous pouvez voir comment j'ai trouvé le sélecteur .class = « sitestr » pour interroger l'URL d'un lien en survolant cet élément sur Hacker News avec ma souris.

![Image](https://cdn-media-1.freecodecamp.org/images/Ntst2lyUgnwM93vP819Xi0VDsrKNuR7IPi2W)

![Image](https://cdn-media-1.freecodecamp.org/images/rFtJJhAOLDauqHKw2565vXMGI4OGPxZ-6AKt)

### C'est tout, et merci !

Merci d'avoir lu ! J'adorerais que vous **commentiez ici**, **m'envoyiez un e-mail à Janeth [at] stdlib [dot] com**, ou suiviez [Standard Library](http://www.stdlib.com?utm_source=content&utm_medium=blog&utm_campaign=scrape_service) sur Twitter, [@StdLibHQ](https://twitter.com/StdLibHQ). Faites-moi savoir si vous avez construit quelque chose d'excitant que vous aimeriez que l'équipe de Standard Library mette en avant ou partage — j'adorerais aider !

_Janeth Ledezma est une Developer Advocate pour Standard Library et diplômée de Berkeley — allez les ours ! 🐻 Quand elle n'apprend pas la langue arabe ou ne fait pas de sport, vous pouvez la trouver en train de conduire sa CBR500R. 🏍 Suivez son parcours avec Standard Library sur Twitter @ms[s_ledezma.](https://twitter.com/mss_ledezma)_