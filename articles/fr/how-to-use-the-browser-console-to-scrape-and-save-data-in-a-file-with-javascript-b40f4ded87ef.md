---
title: Comment utiliser la console du navigateur pour extraire et sauvegarder des
  données dans un fichier avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T21:09:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-browser-console-to-scrape-and-save-data-in-a-file-with-javascript-b40f4ded87ef
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5OIliU0XmrYf_hx_
tags:
- name: Browsers
  slug: browsers
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: json
  slug: json
- name: 'tech '
  slug: tech
seo_title: Comment utiliser la console du navigateur pour extraire et sauvegarder
  des données dans un fichier avec JavaScript
seo_desc: 'By Praveen Dubey

  A while back I had to crawl a site for links, and further use those page links to
  crawl data using selenium or puppeteer. Setup for the content on the site was bit
  uncanny so I couldn’t start directly with selenium and node. Also, un...'
---

Par Praveen Dubey

Il y a quelque temps, j'ai dû explorer un site pour des liens, et utiliser ensuite ces liens de pages pour extraire des données avec selenium ou puppeteer. La configuration du contenu sur le site était un peu étrange, donc je n'ai pas pu commencer directement avec selenium et node. De plus, malheureusement, les données étaient énormes sur le site. J'ai dû rapidement trouver une approche pour d'abord extraire tous les liens et les passer pour l'extraction des détails de chaque page.

C'est là que j'ai appris cette astuce avec l'API Console du navigateur. Vous pouvez l'utiliser sur n'importe quel site web sans beaucoup de configuration, car ce n'est que du JavaScript.

Plongeons dans les détails techniques.

### Aperçu général

![Image](https://cdn-media-1.freecodecamp.org/images/1*YMZ8kpUfQxnuF2_5Byt1KQ.png)

Pour extraire tous les liens d'une page, j'ai écrit un petit morceau de JS dans la console. Ce JavaScript extrait tous les liens (prend 1 à 2 heures, car il fait aussi la pagination) et génère un fichier `json` avec toutes les données extraites. La chose à garder à l'esprit est que vous devez vous assurer que le site web fonctionne _de manière similaire à une application monopage_. Sinon, il ne recharge pas la page si vous voulez extraire plus d'une page. Si ce n'est pas le cas, votre code de console sera perdu.

Medium ne recharge pas la page dans certains scénarios. Pour l'instant, explorons une histoire et sauvegardons les données extraites dans un fichier automatiquement après l'extraction.

Mais avant cela, voici une rapide démonstration de l'exécution finale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aMGV57P1VH7OOpGMcwCqWA.gif)
_Démonstration_

### 1. Obtenir l'instance de l'objet console du navigateur

```
// API Console pour effacer la console avant de journaliser de nouvelles données 
```

```
console.API;
```

```
if (typeof console._commandLineAPI !== 'undefined') {    console.API = console._commandLineAPI; //chrome
```

```
} else if (typeof console._inspectorCommandLineAPI !== 'undefined'){    console.API = console._inspectorCommandLineAPI; //Safari
```

```
} else if (typeof console.clear !== 'undefined') {    console.API = console;
```

```
}
```

Le code essaie simplement d'obtenir l'instance de l'objet console en fonction du navigateur actuel de l'utilisateur. Vous pouvez ignorer et assigner directement l'instance à votre navigateur.

Par exemple, si vous utilisez _Chrome_, le code suivant devrait suffire.

```
if (typeof console._commandLineAPI !== 'undefined') {    console.API = console._commandLineAPI; //chrome
```

```
}
```

### 2. Définir la fonction d'assistance Junior

Je vais supposer que vous avez ouvert une histoire Medium dans votre navigateur. Les lignes 6 à 12 définissent les attributs des éléments DOM qui peuvent être utilisés pour extraire _le titre de l'histoire, le nombre d'applaudissements, le nom de l'utilisateur, l'URL de l'image de profil, la description du profil et le temps de lecture de l'histoire_, respectivement.

Ce sont les éléments de base que je veux montrer pour cette histoire. Vous pouvez ajouter quelques éléments supplémentaires comme extraire les liens de l'histoire, toutes les images, ou les liens intégrés.

### 3. Définir notre fonction d'assistance Senior — la bête

Alors que nous explorons la page pour différents éléments, nous allons les sauvegarder dans une collection. Cette collection sera passée à l'une des fonctions principales.

Nous avons défini une fonction nommée `console.save`. La tâche de cette fonction est de générer un fichier csv/json avec les données passées.

Elle crée un objet Blob avec nos données. Un objet `Blob` représente un objet de type fichier de données brutes immuables. Les Blobs représentent des données qui ne sont pas nécessairement dans un format natif JavaScript.

Créer un blob est attaché à une balise de lien `<a>` sur laquelle un événement de clic est déclenché.

Voici une rapide démonstration de `console.save` avec un petit `tableau` passé en tant que données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NThL0qi4r1RQcgsJjdz-dw.gif)

En assemblant tous les morceaux du code, voici ce que nous avons :

1. Instance de l'API Console
2. Fonction d'assistance pour extraire les éléments
3. Fonction Console Save pour créer un fichier

Exécutons notre `console.save()` dans le navigateur pour sauvegarder les données dans un fichier. Pour cela, vous pouvez aller sur une [histoire sur Medium](https://medium.freecodecamp.org/an-introduction-to-plotly-js-an-open-source-graphing-library-c036a1876e2e) et exécuter ce code dans la console du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aMGV57P1VH7OOpGMcwCqWA.gif)

J'ai montré la démonstration avec l'extraction de données d'une seule page, mais le même code peut être modifié pour explorer plusieurs histoires depuis la page d'accueil d'un éditeur. Prenez l'exemple de [freeCodeCamp](https://medium.freecodecamp.org) : vous pouvez naviguer d'une histoire à une autre et revenir _(en utilisant le bouton de retour du navigateur)_ à la [page d'accueil de l'éditeur](https://medium.freecodecamp.org) sans que la page ne soit rechargée.

Voici le code minimum dont vous avez besoin pour extraire plusieurs histoires depuis la page d'accueil d'un éditeur.

Regardons le code en action pour obtenir la description du profil à partir de plusieurs histoires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*asB621a3j1s6ZGZa9Up2Hw.gif)

**Pour toute application de ce type, une fois que vous avez extrait les données, vous pouvez les passer à notre fonction _console.save_ et les stocker dans un fichier.**

La fonction de sauvegarde de la console peut être rapidement attachée à votre code de console et peut vous aider à sauvegarder les données dans le fichier. Je ne dis pas que vous _devez_ utiliser la console pour extraire des données, mais parfois ce sera une approche beaucoup plus rapide puisque nous sommes tous très familiers avec le travail sur le DOM en utilisant les sélecteurs CSS.

Vous pouvez télécharger le code depuis [Github](https://github.com/edubey/browser-console-crawl)

> Merci d'avoir lu cet article ! J'espère qu'il vous a donné une idée cool pour extraire rapidement des données sans beaucoup de configuration. Appuyez sur le bouton d'applaudissements si vous l'avez apprécié ! Si vous avez des questions, envoyez-moi un email (praveend806 [at] gmail [dot] com).

#### _Ressources pour en savoir plus sur la Console :_

[**Utilisation de la Console | Outils pour les développeurs Web | Développeurs Google**](https://developers.google.com/web/tools/chrome-devtools/console/)  
[_Apprenez à naviguer dans la console JavaScript des outils de développement Chrome._developers.google.com](https://developers.google.com/web/tools/chrome-devtools/console/)[**Console du navigateur**](https://developer.mozilla.org/en-US/docs/Tools/Browser_Console)  
[_La console du navigateur est similaire à la console Web, mais appliquée à l'ensemble du navigateur plutôt qu'à un seul onglet de contenu._developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Tools/Browser_Console)[**Blob**](https://developer.mozilla.org/en-US/docs/Web/API/Blob)  
[_Un objet Blob représente un objet de type fichier de données brutes immuables. Les Blobs représentent des données qui ne sont pas nécessairement dans unformat natif JavaScript._developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/Blob)