---
title: Comment créer et publier une extension Chrome en 20 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-24T20:04:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-and-publish-a-chrome-extension-in-20-minutes-6dc8395d7153
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2eZjMzwZoO2zThFwJ2CuoQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: publishing
  slug: publishing
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment créer et publier une extension Chrome en 20 minutes
seo_desc: 'By Jake Prins

  Ever wondered what it would be like to create a Chrome extension? Well, I’m here
  to tell you just how easy it is. Follow these steps and your idea will turn into
  reality and you’ll be able to publish a real extension in the Chrome Web S...'
---

Par Jake Prins

Vous êtes-vous déjà demandé ce que ce serait de créer une extension Chrome ? Eh bien, je suis là pour vous dire à quel point c'est facile. Suivez ces étapes et votre idée deviendra réalité, et vous pourrez publier une véritable extension dans le [Chrome Web Store](https://chrome.google.com/webstore/category/extensions) en un rien de temps.

### Qu'est-ce qu'une extension Chrome ?

Les extensions Chrome vous permettent d'ajouter des fonctionnalités au navigateur web Chrome sans plonger profondément dans le code natif. C'est génial parce que vous pouvez créer de nouvelles extensions pour Chrome avec des technologies de base que les développeurs web connaissent très bien - HTML, CSS et JavaScript. Si vous avez déjà construit une page web, vous serez en mesure de créer une extension plus rapidement que vous ne pouvez déjeuner. La seule chose que vous devez apprendre est comment ajouter certaines fonctionnalités à Chrome à travers certaines des API JavaScript que Chrome expose.

Si vous n'êtes pas encore expérimenté dans la construction de pages web, je vous recommande de plonger d'abord dans certaines ressources gratuites pour apprendre à coder, comme [freeCodeCamp](https://www.freecodecamp.org/).

### Que voulez-vous construire ?

Avant de commencer, vous devriez avoir une idée approximative de ce que vous voulez construire. Cela n'a pas besoin d'être une nouvelle idée révolutionnaire, nous pouvons simplement le faire pour le plaisir. Dans cet article, je vais vous parler de mon idée et de la manière dont je l'ai implémentée dans une extension Chrome.

### Le plan

J'ai utilisé l'extension Chrome [Unsplash](https://chrome.google.com/webstore/detail/unsplash-instant/pejkokffkapolfffcgbmdmhdelanoaih) pendant un certain temps, ce qui me permet d'avoir de belles images de fond de [Unsplash](https://unsplash.com/) dans mon onglet par défaut. Je l'ai ensuite remplacée par l'extension Chrome [Muzli](https://muz.li/) qui transforme l'onglet par défaut en un flux d'actualités de design et de captures d'écran du monde entier.

Utilisons ces deux extensions comme inspiration pour construire quelque chose de nouveau, mais cette fois, pour les amateurs de cinéma. Mon idée est de montrer une image de fond aléatoire d'un film chaque fois que vous ouvrez un nouvel onglet. En faisant défiler, cela devrait se transformer en un flux agréable de films et d'émissions de télévision populaires. Alors, commençons.

### **Étape 1 : Configuration des choses**

La première étape consiste à créer un fichier manifest nommé `manifest.json`. Il s'agit d'un fichier de métadonnées au format JSON qui contient des propriétés telles que le nom de votre extension, la description, le numéro de version, etc. Dans ce fichier, nous indiquons à Chrome ce que l'extension va faire et quelles permissions elle nécessite.

Pour l'extension de film, nous devons avoir la permission de contrôler **activeTab**, donc notre fichier `manifest.json` ressemble à quelque chose comme ceci :

```
{ "manifest_version": 2, "name": "RaterFox", "description": "Les films et émissions de télévision les plus populaires dans votre onglet par défaut. Inclut les évaluations, les résumés et la possibilité de regarder des bandes-annonces.", "version": "1", "author": "Jake Prins",
```

```
"browser_action": {   "default_icon": "tab-icon.png",   "default_title": "Passez une bonne journée" },
```

```
"chrome_url_overrides" : {  "newtab": "newtab.html"},
```

```
 "permissions": ["activeTab"]}
```

Comme vous pouvez le voir, nous disons que `newtab.html` sera le fichier HTML qui doit être rendu chaque fois qu'un nouvel onglet est ouvert. Pour ce faire, nous devons avoir la permission de contrôler **activeTab**, donc lorsque l'utilisateur essaie d'installer l'extension, il sera averti de toutes les permissions dont l'extension a besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/4y26iiG0Z4jq3tbBwTgjBlCoksECGWII1LyF)

Une autre chose intéressante dans le fichier `manifest.json` sont les actions du navigateur. Dans cet exemple, nous les utilisons pour définir le titre, mais il y a plus d'options. Par exemple, pour afficher une fenêtre contextuelle chaque fois que vous cliquez sur l'icône de l'application dans la barre d'adresse, il suffit de faire quelque chose comme ceci :

```
"browser_action": {  "default_popup": "popup.html", },
```

Maintenant, `popup.html` sera rendu dans la fenêtre contextuelle qui est créée en réponse à un clic de l'utilisateur sur l'action du navigateur. C'est un fichier HTML standard, donc il vous donne libre cours sur ce que la fenêtre contextuelle affiche. Il suffit de mettre un peu de votre magie dans un fichier nommé `popup.html`.

### Étape 2 : Testez si cela fonctionne

L'étape suivante consiste à créer le fichier `newtab.html` et à y mettre un 'Hello world' :

```
<!doctype html><html>  <head>    <title>Test</title>  </head>  <body>    <h1>Bonjour le monde !</h1>  </body></html>
```

Pour tester si cela fonctionne, visitez `chrome://extensions` dans votre navigateur et assurez-vous que la case **Mode développeur** dans le coin supérieur droit est cochée.

![Image](https://cdn-media-1.freecodecamp.org/images/hplLksya7cBxpBQdzgbjt6ZjIJG9U8D6whVl)
_Mode développeur Chrome_

Cliquez sur **Charger l'extension non empaquetée** et sélectionnez le répertoire dans lequel se trouvent les fichiers de votre extension. Si l'extension est valide, elle sera active immédiatement, vous pouvez donc ouvrir un nouvel onglet pour voir votre 'Hello world'.

### **Étape 3 : Rendre les choses agréables**

Maintenant que nous avons notre première fonctionnalité qui fonctionne, il est temps de la rendre agréable. Nous pouvons simplement styliser notre nouvel onglet en créant un fichier `main.css` dans notre répertoire d'extension et le charger dans notre fichier `newtab.html`. Il en va de même pour l'inclusion d'un fichier JavaScript pour toute fonctionnalité active que vous souhaitez inclure. En supposant que vous avez déjà créé une page web, vous pouvez maintenant utiliser votre magie pour montrer à vos utilisateurs ce que vous voulez.

### **Finalisation du plan**

Tout ce dont j'avais besoin pour terminer l'extension de film était du HTML, du CSS et du JavaScript, donc je ne pense pas qu'il soit pertinent de plonger profondément dans le code, mais j'aimerais le parcourir rapidement.

Voici ce que j'ai fait :

Pour mon idée, j'avais besoin de belles images de fond, donc dans le fichier JavaScript, j'ai utilisé l'API [TMDb](https://www.themoviedb.org/) pour récupérer des films populaires, j'ai pris leurs images de fond et je les ai mises dans un tableau. Chaque fois que la page se charge, elle choisit maintenant aléatoirement une image de ce tableau et la définit comme fond de la page. Pour rendre cette page un peu plus intéressante, j'ai également ajouté la date actuelle dans le coin supérieur droit. Et pour plus d'informations, elle permet aux utilisateurs de cliquer sur le fond, ce qui les conduit à visiter la page [IMDb](http://www.imdb.com/) du film.

J'ai remplacé l'écran par un flux agréable de films populaires lorsque l'utilisateur essaie de faire défiler vers le bas. J'ai utilisé la même API pour construire des cartes de films avec une image, un titre, une note et un compte de votes. Ensuite, en cliquant sur l'une de ces cartes, elle affiche l'aperçu avec un bouton pour regarder une bande-annonce.

### **Le résultat**

Maintenant, avec ce petit fichier `manifest.json` et juste un peu de HTML, CSS et JavaScript, chaque nouvel onglet que vous ouvrez semble beaucoup plus intéressant :

![Image](https://cdn-media-1.freecodecamp.org/images/vUPpM1QiRIgV8dcHwBvKsGwJYI1GyJctJaHo)
_Voir le résultat final [ici](https://chrome.google.com/webstore/detail/raterfox-popular-movies-t/pbmdibcifmempicdafabdakcoamfobik" rel="noopener" target="_blank" title=")._

### Étape 4 : Publiez votre extension

Lorsque votre première extension Chrome est belle et fonctionne comme elle le devrait, il est temps de la publier dans le Chrome Store. Suivez simplement [ce lien](https://chrome.google.com/webstore/developer/dashboard) pour accéder à votre tableau de bord du Chrome Web Store (vous serez invité à vous connecter à votre compte Google si vous ne l'êtes pas). Ensuite, cliquez sur le bouton `**Ajouter un nouvel élément**`, acceptez les termes et vous accéderez à la page où vous pourrez télécharger votre extension. Compressez maintenant le dossier qui contient votre projet et téléchargez ce fichier ZIP.

![Image](https://cdn-media-1.freecodecamp.org/images/9zUs3mIMtnvMDxWsPjVCZ-gNpvIzx3-mPFUe)
_Chrome Web Store_

Après avoir téléchargé votre fichier avec succès, vous verrez un formulaire dans lequel vous devez ajouter certaines informations sur votre extension. Vous pouvez ajouter une icône, une description détaillée, télécharger des captures d'écran, etc.

Assurez-vous de fournir de belles images pour montrer votre projet. Le magasin peut utiliser ces images pour promouvoir votre projet révolutionnaire. Plus vous fournissez d'images, plus votre extension sera mise en avant de manière proéminente. Vous pouvez prévisualiser l'apparence de votre extension dans le magasin en ligne en cliquant sur le bouton `**Prévisualiser les modifications**`. Lorsque vous êtes satisfait du résultat, cliquez sur `**Publier les modifications**` et c'est tout, vous avez terminé !

Maintenant, allez dans le [Chrome Web Store](https://chrome.google.com/webstore/category/extensions) et recherchez votre extension par son titre (cela peut prendre un certain temps avant qu'elle n'apparaisse). Si vous êtes intéressé, vous pouvez trouver la mienne [ici](https://chrome.google.com/webstore/detail/raterfox-popular-movies-t/pbmdibcifmempicdafabdakcoamfobik).

La seule chose qui reste à faire est d'obtenir quelques utilisateurs. Vous pourriez donc vouloir partager un article sur votre extension Chrome qui change la vie sur les réseaux sociaux. Dites à vos amis de la vérifier. Ajoutez-la à [ProductHunt](https://www.producthunt.com/posts/raterfox). Et n'oubliez pas de partager votre projet ici dans les commentaires. Je suis curieux de voir ce que vous avez imaginé !

### **Conclusion**

En tant que développeur web, il est très facile de créer une extension Chrome en peu de temps. Tout ce dont vous avez besoin est un peu de HTML, de CSS, de JavaScript et une connaissance de base de la manière d'ajouter des fonctionnalités à travers certaines des API JavaScript que Chrome expose. Votre configuration initiale peut être publiée dans le Chrome Web Store en seulement 20 minutes. La construction d'une extension qui est nouvelle, utile ou belle prendra un peu plus de temps. Mais c'est à vous de jouer !

Utilisez votre créativité pour imaginer quelque chose d'intéressant et si vous êtes bloqué, l'excellente documentation sur les extensions Chrome peut probablement vous aider.

Alors, qu'attendez-vous ? Il est temps de commencer à travailler sur votre propre extension Chrome et de transformer votre idée en réalité.

N'oubliez pas de partager votre projet dans les commentaires et de cliquer sur le bouton d'applaudissements si cet article vous a été utile. Si vous avez un peu de temps et que vous voulez être un héros, donnez à [mon extension](https://chrome.google.com/webstore/detail/raterfox-popular-movies-t/pbmdibcifmempicdafabdakcoamfobik) une note positive. Cela serait grandement apprécié !

Vous avez des questions ou des commentaires ? Faites-le moi savoir dans les commentaires !

Merci d'avoir lu ! J'espère que les informations ont été utiles. Suivez-moi sur Medium pour plus d'articles liés à la technologie ou sur Twitter et Instagram @jakeprins_nl.