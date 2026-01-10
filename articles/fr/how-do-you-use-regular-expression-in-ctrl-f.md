---
title: Comment utiliser les expressions régulières dans CTRL F
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-30T13:12:06.000Z'
originalURL: https://freecodecamp.org/news/how-do-you-use-regular-expression-in-ctrl-f
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--6-.png
tags:
- name: Regex
  slug: regex
seo_title: Comment utiliser les expressions régulières dans CTRL F
seo_desc: 'The conventional CTRL + F does not support Regex in many software tools
  we use in our day-to-day lives. But almost nothing is impossible in the tech world.

  Many of these software tools, such as VS Code, Chrome browser, Dreamweaver, Jetbrains,
  and oth...'
---

La combinaison conventionnelle `CTRL + F` ne prend pas en charge les expressions régulières (Regex) dans de nombreux outils logiciels que nous utilisons au quotidien. Mais presque rien n'est impossible dans le monde de la technologie.

De nombreux outils logiciels, tels que VS Code, le navigateur Chrome, Dreamweaver, Jetbrains et autres, disposent d'un mécanisme intégré qui prend en charge les expressions régulières lors de l'utilisation de `CTRL + F` pour rechercher une page ou un document.

Voyons comment vous pouvez rechercher avec `CTRL + F` en utilisant des expressions régulières dans VS Code, le navigateur Chrome et les outils de développement Chrome.


## Ce que nous allons couvrir
- [Comment utiliser les expressions régulières dans `CTRL + F` dans VS Code](#heading-comment-utiliser-les-expressions-regulieres-dans-ctrl-f-dans-vs-code)
- [Comment utiliser les expressions régulières dans `CTRL + F` dans les outils de développement Chrome](#heading-comment-utiliser-les-expressions-regulieres-dans-ctrl-f-dans-les-outils-de-developpement-chrome)
- [Comment utiliser les expressions régulières dans `CTRL + F` sur une page web Chrome](#heading-comment-utiliser-les-expressions-regulieres-dans-ctrl-f-sur-une-page-web-chrome)
- [Conclusion](#heading-conclusion)


## Comment utiliser les expressions régulières dans `CTRL + F` dans VS Code
Appuyez sur `CTRL + F` et l'interface de recherche apparaîtra :
![Screenshot-2023-03-30-at-11.09.19](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.09.19.png)

Passez la souris sur `.*` et "Utiliser une expression régulière" avec certaines combinaisons de touches devrait apparaître :
![Screenshot-2023-03-30-at-11.10.50](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.10.50.png)

Partout où vous voyez le signe `.*`, cela signifie Regex. Cliquez dessus pour commencer à rechercher avec Regex.

Entrez votre expression régulière et les résultats de recherche s'affichent :
![Screenshot-2023-03-30-at-11.17.13](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.17.13.png)

Si la seule chose que vous voulez faire avec `CTRL + F` est de rechercher en utilisant Regex, la combinaison de touches `ALT + CTRL + R` active et désactive la recherche `CTRL + F` avec Regex.


## Comment utiliser les expressions régulières dans `CTRL + F` dans les outils de développement Chrome
Vous pouvez également rechercher en utilisant Regex dans les outils de développement Chrome lorsque vous ouvrez une source de page.

Faites un clic droit n'importe où sur une page et sélectionnez "Inspecter" :
![Screenshot-2023-03-30-at-11.22.21](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.22.21.png)

Cliquez sur les 3 points dans le coin supérieur droit et sélectionnez recherche pour révéler l'interface de recherche des outils de développement :
![Screenshot-2023-03-30-at-11.23.01](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.23.01.png)

Vous pouvez également appuyer sur `CTRL + ALT + F` sous Windows ou `CMD + ALT + F` sur Mac pour faire cela.

Cliquez sur le bouton `.*` pour rechercher avec Regex :
![Screenshot-2023-03-30-at-11.24.59](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.24.59.png)

Tapez votre expression régulière et appuyez sur `ENTRÉE` pour révéler les résultats de recherche :
![Screenshot-2023-03-30-at-11.27.20](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.27.20.png)


## Comment utiliser les expressions régulières dans `CTRL + F` sur une page web Chrome
Puisque vous pouvez rechercher avec Regex dans les outils de développement Chrome, vous vous demandez peut-être comment rechercher avec Regex sur une page web.

Bien que Chrome ne dispose pas de cette fonctionnalité intégrée, vous pouvez installer une extension pour le faire.

Rendez-vous sur [Chrome Web Store](https://chrome.google.com/webstore/category/extensions) et recherchez Regex :
![Screenshot-2023-03-30-at-11.33.27](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.33.27.png)

Installez l'extension de recherche Chrome Regex :
![Screenshot-2023-03-30-at-11.34.10](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.34.10.png)

Fermez et rouvrez votre navigateur Chrome. Ensuite, allez dans vos extensions et sélectionnez "Chrome Regex Search" :
![Screenshot-2023-03-30-at-11.39.34](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.39.34.png)

Entrez votre expression régulière et les résultats de recherche s'affichent :
![Screenshot-2023-03-30-at-11.38.35](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.38.35.png)


## Conclusion
Même si de nombreux logiciels ne disposent pas d'une recherche `CTRL + F` par défaut avec Regex, il existe un moyen d'activer cette fonctionnalité ou d'installer une extension.

VS Code et Google Chrome disposent de cette fonctionnalité intégrée.

Avec les outils de développement Chrome, appuyez sur `CTRL + SHIFT + F` sous Windows et `CMD + SHIFT + F` sur Mac, puis sur le même bouton `.*` pour rechercher avec Regex. Vous faites exactement la même chose dans VS Code.

Sur une page web, Chrome ne prend pas en charge la recherche avec `CTRL + F` en utilisant Regex, mais vous pouvez télécharger des extensions qui ajoutent cette fonctionnalité.

Si vous utilisez un autre outil et que vous souhaitez rechercher en utilisant Regex, une rapide recherche sur le web vous orientera dans la bonne direction.

Merci d'avoir lu !