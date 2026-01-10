---
title: Apprenons comment fonctionnent les module bundlers et ensuite écrivons-en un
  nous-mêmes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-23T19:28:22.000Z'
originalURL: https://freecodecamp.org/news/lets-learn-how-module-bundlers-work-and-then-write-one-ourselves-b2e3fe6c88ae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oxAMv8OXwMUxyk8c9ZnPUA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Apprenons comment fonctionnent les module bundlers et ensuite écrivons-en
  un nous-mêmes
seo_desc: 'By Adam Kelly

  Hello! Welcome, welcome, it’s great to have you here! Today we’re going to be building
  a really simple JavaScript module bundler.

  Before we start, I want to give a few acknowledgements. This article draws heavily
  on the following resour...'
---

Par Adam Kelly

Bonjour ! Bienvenue, bienvenue, c'est génial de vous avoir ici ! Aujourd'hui, nous allons construire un module bundler JavaScript vraiment simple.

Avant de commencer, je souhaite rendre hommage à quelques ressources. Cet article s'inspire largement des ressources suivantes :

* [Unbundling the JavaScript module bundler](http://loige.link/bundle-dublinjs) - Luciano Mammino
* [Minipack](https://github.com/ronami/minipack) - Ronen Amiel

D'accord, commençons par ce qu'est réellement un module bundler.

### Qu'est-ce qu'un Module Bundler ?

Un module bundler est un outil qui prend des morceaux de JavaScript et leurs dépendances et les regroupe dans un seul fichier, généralement pour une utilisation dans le navigateur. Vous avez peut-être utilisé des outils tels que [Browserify](http://browserify.org/), [Webpack](https://webpack.js.org/), [Rollup](https://rollupjs.org/guide/en) ou l'un des nombreux autres.

Il commence généralement par un fichier d'entrée, et à partir de là, il regroupe tout le code nécessaire pour ce fichier d'entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/0*WwDTeWwIRxVPg5jK.png)

Il y a deux étapes principales d'un bundler :

1. Résolution des dépendances
2. Emballage

En partant d'un point d'entrée (comme `app.js` ci-dessus), le but de la résolution des dépendances est de rechercher toutes les dépendances de votre code (d'autres morceaux de code dont il a besoin pour fonctionner) et de construire un graphe (appelé graphe de dépendances).

Une fois cela fait, vous pouvez ensuite emballer ou convertir votre graphe de dépendances en un seul fichier que l'application peut utiliser.

Commençons notre code avec quelques imports (j'élaborerai sur la raison plus tard).

### Résolution des dépendances

La première chose que nous devons faire est de réfléchir à la manière dont nous voulons représenter un module pendant la phase de résolution des dépendances.

#### Représentation du module

Nous allons avoir besoin de quatre choses :

* Le nom et un identifiant du fichier
* D'où vient le fichier (dans le système de fichiers)
* Le code dans le fichier
* Les dépendances dont ce fichier a besoin

La structure du graphe est construite en vérifiant récursivement les dépendances dans chaque fichier.

En JavaScript, la manière la plus simple de représenter un tel ensemble de données serait un objet.

En regardant la fonction `createModuleObject` ci-dessus, la partie notable est l'appel à une fonction appelée `detective`.

[Detective](https://github.com/browserify/detective) est une bibliothèque qui peut « trouver tous les appels à require() peu importe leur niveau de nesting », et en l'utilisant, nous pouvons éviter de faire notre propre traversée AST !

Une chose à noter (et c'est la même dans presque tous les module bundlers) est que si vous essayez de faire quelque chose de bizarre comme :

```
const libName = 'lodash'
const lib = require(libName)
```

Il ne pourra pas le trouver (car cela signifierait exécuter le code).

Alors, que donne l'exécution de cette fonction à partir du chemin d'un module ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*5gAnBAhQ3_4cn5oq.png)

Qu'est-ce qui suit ? La résolution des dépendances.

D'accord, pas tout de suite. D'abord, je veux parler d'une chose appelée module map.

#### Module Map

Lorsque vous importez des modules dans Node, vous pouvez faire des imports relatifs, comme `require('./utils')`. Donc lorsque votre code appelle cela, comment le bundler sait-il quel est le bon fichier `./utils` lorsque tout est empaqueté ?

C'est le problème que la module map résout.

Notre objet module a une clé `id` unique qui sera notre « source de vérité ». Donc lorsque nous faisons notre résolution des dépendances, pour chaque module, nous garderons une liste des noms de ce qui est requis ainsi que leur id. De cette façon, nous pouvons obtenir le bon module au moment de l'exécution.

Cela signifie également que nous pouvons stocker tous les modules dans un objet non imbriqué, en utilisant l'id comme clé.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1LBQSrDoGoQrbE3t.png)

### Résolution des dépendances

D'accord, il y a pas mal de choses qui se passent dans la fonction `getModules`. Son but principal est de commencer au module racine/entrée, et de rechercher et résoudre les dépendances de manière récursive.

Que veux-je dire par « résoudre les dépendances » ? Dans Node, il y a une chose appelée `require.resolve`, et c'est ainsi que Node détermine où se trouve le fichier que vous requérez. C'est parce que nous pouvons importer relativement ou depuis un dossier `node_modules`.

Heureusement pour nous, il y a un module npm nommé `resolve` qui implémente cet algorithme pour nous. Nous devons simplement passer en arguments la dépendance et l'URL de base, et il fera tout le travail difficile pour nous.

Nous devons effectuer cette résolution pour chaque dépendance de chaque module dans le projet.

Nous créons également la module map nommée `map` dont j'ai parlé plus tôt.

À la fin de la fonction, nous obtenons un tableau nommé `modules` qui contiendra des objets module pour chaque module/dépendance dans notre projet.

Maintenant que nous avons cela, nous pouvons passer à l'étape finale : l'emballage !

### Emballage

Dans le navigateur, il n'y a pas de modules (en quelque sorte). Mais cela signifie qu'il n'y a pas de fonction require, et pas de `module.exports`. Donc même si nous avons toutes nos dépendances, nous n'avons actuellement aucun moyen de les utiliser comme modules.

#### Fonction d'usine de module

Entrez la fonction d'usine.

Une fonction d'usine est une fonction (qui n'est pas un constructeur) qui retourne un objet. C'est un modèle de programmation orientée objet, et l'une de ses utilisations est de faire de l'encapsulation et de l'injection de dépendances.

Ça semble bien ?

En utilisant une fonction d'usine, nous pouvons à la fois injecter notre propre fonction `require` et notre objet `module.exports` qui peuvent être utilisés dans notre code empaqueté et donner au module son propre scope.

#### Emballage

Ce qui suit est la fonction pack qui est utilisée pour l'emballage.

La plupart de cela est simplement des littéraux de gabarit JavaScript, alors discutons de ce qu'il fait.

Tout d'abord, il y a `modulesSource`. Ici, nous passons par chacun des modules et les transformons en une chaîne de sources.

Alors, à quoi ressemble la sortie pour un objet module ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*dJtsT5gsI2_heqtL.png)

Maintenant, c'est un peu difficile à lire, mais vous pouvez voir que la source est encapsulée. Nous fournissons `modules` et `require` en utilisant la fonction d'usine comme je l'ai mentionné précédemment.

Nous incluons également la module map que nous avons construite pendant la résolution des dépendances.

Ensuite dans la fonction, nous joignons tous ceux-ci pour créer un grand objet de toutes les dépendances.

La chaîne de code suivante est un IIFE, ce qui signifie que lorsque vous exécutez ce code dans le navigateur (ou ailleurs), la fonction s'exécutera immédiatement. IIFE est un autre modèle pour encapsuler le scope, et est utilisé ici pour que nous ne polluions pas le scope global avec notre `require` et nos modules.

Vous pouvez voir que nous définissons deux fonctions require, `require` et `localRequire`.

Require accepte l'id d'un objet module, mais bien sûr le code source n'est pas écrit en utilisant des ids. Au lieu de cela, nous utilisons l'autre fonction `localRequire` pour prendre tous les arguments requis par les modules et les convertir en l'id correct. Cela utilise ces module maps.

Après cela, nous définissons un `objet module` que le module peut remplir, et passons les deux fonctions dans l'usine, après quoi nous retournons `module.exports`.

Enfin, nous appelons `require(0)` pour requérir le module avec un id de 0, qui est notre fichier d'entrée.

Et c'est tout ! Notre module bundler est à 100 % complet !

### Félicitations ! 🎉

Nous avons donc maintenant un module bundler fonctionnel.

Celui-ci ne devrait probablement pas être utilisé en production, car il manque de nombreuses fonctionnalités (comme la gestion des dépendances circulaires, s'assurer que chaque fichier n'est analysé qu'une seule fois, les modules es, etc.), mais cela vous a probablement donné une bonne idée de comment fonctionnent réellement les module bundlers.

En fait, celui-ci fonctionne en environ 60 lignes si vous supprimez tout le code source.

Merci d'avoir lu, et j'espère que vous avez apprécié un aperçu du fonctionnement de notre simple module bundler. Si c'est le cas, assurez-vous d'applaudir 👏 et de partager.

> Cet article a été initialement publié sur mon [blog](https://adamisntdead.com/lets-write-a-module-bundler/).  
> Consultez la source [https://github.com/adamisntdead/wbpck-bundler](https://github.com/adamisntdead/wbpck-bundler)