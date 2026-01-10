---
title: 'VS Code snippets : l''outil le plus puissant pour booster votre productivité
  de codage'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-16T15:34:08.000Z'
originalURL: https://freecodecamp.org/news/the-most-powerful-tool-to-boost-your-coding-productivity-2dc80e0eff00
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UwAkIPzykbLNqOffgyvegw.gif
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Visual Studio Code
  slug: vscode
seo_title: 'VS Code snippets : l''outil le plus puissant pour booster votre productivité
  de codage'
seo_desc: 'By Sam Williams

  Write more code with fewer keystrokes


  _Photo by [Unsplash](https://unsplash.com/@dlanor_s?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Dlanor S on <a href="https://unsplash.com?utm_source=medium&utm_...'
---

Par Sam Williams

#### Écrivez plus de code avec moins de frappes

![Image](https://cdn-media-1.freecodecamp.org/images/0*aEvz1gdQhix8dzTi)
_Photo par [Unsplash](https://unsplash.com/@dlanor_s?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Dlanor S</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Tout le monde veut pouvoir produire plus de code avec moins de frappes. Les fonctions fléchées en JavaScript sont devenues incroyablement populaires récemment — et elles ne vous font économiser que 6 caractères !

```
(function(){console.log('a')})() // 32 caractères
(()=>{console.log('a')})() // 26 caractères
```

Mais il existe une meilleure façon d'économiser des frappes — et cet article vous montrera l'outil pour le faire.

### Extraits de code

Depuis des années, les gens utilisent des extraits de code pour gagner du temps — qu'il s'agisse de fonctions courantes, de structures de fichiers ou même de modèles pour des systèmes entiers. Ce n'est pas une idée nouvelle.

Le problème avec beaucoup de systèmes existants est que ces extraits étaient souvent stockés dans des fichiers texte ou d'autres systèmes de fichiers et devaient être copiés et collés manuellement là où ils étaient nécessaires.

C'était génial pour les grands extraits de code. Mais les lignes de code uniques étaient souvent plus rapides à taper qu'à chercher le fichier, le copier et le coller.

L'étape suivante a été des outils tels que TextExpander ou AutoHotKeys, où des séquences de touches spéciales pouvaient être configurées pour coller des extraits de code là où vous tapiez. Ce sont de grands outils et ils peuvent vous faire économiser beaucoup de temps… mais nous pouvons aller encore plus loin.

### Extraits de code VS Code

![Image](https://cdn-media-1.freecodecamp.org/images/1*UwAkIPzykbLNqOffgyvegw.gif)

VS Code dispose d'un système plus puissant que même TextExpander ou AutoHotKeys. Ses extraits de code intégrés peuvent être configurés pour faire bien plus que simplement coller le code.

Avant de parler des fonctionnalités avancées, nous allons apprendre comment créer un extrait.

Dans VS Code, appuyez sur ctrl+shift+P pour ouvrir la palette de commandes et recherchez snippet. Sélectionner 'Configure User Snippets' vous présente une liste de langages de programmation pour lesquels vous pouvez créer un extrait. Nous allons choisir JavaScript.

Cela ouvre l'éditeur d'extraits. Il y a un commentaire qui vous montre comment créer un extrait de base, mais nous allons créer le nôtre.

Cet extrait est celui qui est [ma ligne de code préférée](https://medium.freecodecamp.org/my-favourite-line-of-code-53627668aab4). C'est un joli modèle pour la gestion des promesses.

```
const handle = prom => prom.then(res => [null, res]).catch(err => [err, null]);
```

Pour créer notre extrait, nous devons créer une nouvelle clé dans l'objet. Cette clé pointe vers un objet avec un `prefix`, `body` et `description`.

```
"insert handle function": {    "prefix": "",    "body": [],    "description": ""}
```

Le préfixe est le texte que nous voulons entrer pour déclencher cet extrait. Vous devez vous assurer que celui-ci est unique. L'appeler `handle` déclencherait l'extrait chaque fois que vous appelez la fonction, donc nous pouvons opter pour quelque chose comme `promHandle`.

Le corps est un tableau des lignes de l'extrait. Si vous avez plusieurs lignes de code, vous aurez plusieurs chaînes dans le tableau du corps. La description est ce qui sera affiché lorsque vous verrez la suggestion dans VS Code.

Lorsque tout cela est terminé, vous obtenez quelque chose comme ceci :

```
"insert handlefunction": {    "prefix": "promHandle",    "body": [        "const handle = prom => prom.then(res => [null, res]).catch(err => [err, null]);"    ],    "description": "insertion d'une fonction 'handle'"}
```

Avec votre fichier d'extraits sauvegardé, lorsque vous commencez à taper `promhandle`, vous obtenez une nouvelle suggestion. En appuyant sur la touche bas, vous voyez la description de l'extrait ainsi que la première ligne du code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mi0gmOsCo4I6AyoHHjB24w.gif)

Maintenant, vous pouvez économiser des centaines de caractères en créant vos propres extraits. Mais il y a des fonctionnalités encore plus puissantes !

#### Points d'insertion par tabulation

Lorsque vous collez vos extraits, il y a généralement des morceaux d'informations que vous devez ajouter. Qu'il s'agisse de nommer une fonction ou de choisir les variables, vous pouvez définir des points dans votre code où vous devez entrer des données. Lorsque vous collez ces extraits, vous pouvez tabuler entre ces points d'insertion.

Pour ajouter un point d'insertion, vous devez simplement ajouter `$1` pour le premier point, `$2` pour le second, et ainsi de suite. Cela est vraiment utile pour les fonctions où elles attendent un objet.

```
"sendMessage": {    "prefix": "sendMessage",    "body": [        "await botHelper.sendToUser({message$1, userID});"    ],    "description": "attendre l'envoi d'un message en utilisant l'aide du bot"},
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*1JFkjHn1m1Lpi_fzKrz2Ww.gif)

Vous pouvez avoir plusieurs points de tabulation répartis dans le code, ce qui signifie que vous pouvez rapidement et facilement remplir votre extrait sans avoir à cliquer ou à utiliser les touches fléchées pour chaque point.

#### Extraits spécifiques à un langage

Lorsque nous avons ouvert l'éditeur d'extraits pour la première fois, nous avons été présentés avec une liste de langages. Nous avons choisi JavaScript, mais vous auriez pu choisir l'un des 44 autres langages. La grande chose à propos des extraits de code VS Code est qu'ils peuvent être verrouillés à un type de fichier spécifique.

Si vous écrivez un fichier HTML, vous n'obtiendrez pas tous vos extraits JavaScript ou Python. Cela signifie également que vous pouvez avoir le même préfixe produire différents extraits en fonction du type de fichier sur lequel vous travaillez actuellement ! Mais ne vous inquiétez pas, vous pouvez toujours ajouter des extraits globaux si vous voulez pouvoir les utiliser dans n'importe quel type de fichier.

#### Extraits spécifiques à un emplacement

De manière similaire aux extraits spécifiques à un langage, vous pouvez également créer des extraits spécifiques à un dossier. Cela peut être génial lorsque la même fonction nommée fait une chose différente dans deux projets différents.

Il suffit de sélectionner `New Snippet file for '...'` lors du choix de votre langage.

### Créer plus d'extraits

Maintenant que vous connaissez les moyens puissants dont les extraits de code VS Code peuvent améliorer votre productivité, vous voulez probablement en créer beaucoup. Malheureusement, ils peuvent être frustrants à créer. Heureusement, il existe deux solutions :

#### Générateur d'extraits

[Snippet Generator](https://snippet-generator.app/) est un site qui vous permet de coller du code et de le convertir facilement au format d'extrait.

Il est très facile à utiliser et vous permet de créer rapidement des extraits que vous pouvez simplement copier et coller directement dans vos fichiers d'extraits. Il fonctionne avec n'importe quel langage et est complètement gratuit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kw9vrKEgA4mhMurEpniDbg.png)

#### Extensions d'extraits

Si vous utilisez un framework, tel que React ou Angular, il y a beaucoup d'extraits que vous allez vouloir créer. Heureusement, c'est un problème que d'autres personnes ont eu avant vous, donc elles ont créé des bibliothèques d'extraits courants pour chaque framework.

Rechercher `snippets` dans le marché d'extensions VS Code produit des centaines de résultats que vous pouvez installer. Tout, de React, Angular et Vue à ES6 JS, C# et PHP. Ceux-ci ont souvent une gamme complète d'extraits pour réduire considérablement le temps passé à taper.

Le seul inconvénient de ces extensions est que vous devrez apprendre quels sont les préfixes (déclencheurs), mais vous mémoriserez rapidement ceux que vous utilisez le plus.

Merci d'avoir lu cet article sur l'augmentation de votre productivité de codage avec les extraits de code VS Code. Si vous avez appris quelque chose, appuyez sur ce bouton d'applaudissements ? et suivez-moi pour plus de conseils, astuces et tutoriels !

![Image](https://cdn-media-1.freecodecamp.org/images/1*LhwiNc46QXzOCEb2QhERBg.gif)