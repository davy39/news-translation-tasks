---
title: Configurer Flow lorsque vous avez déjà Babel en place
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-09T14:53:46.000Z'
originalURL: https://freecodecamp.org/news/using-flow-with-babel-c04fdca8d14d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S3mUOCWvhWPralT0YbcdRA.png
tags:
- name: flowtype
  slug: flowtype
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: Configurer Flow lorsque vous avez déjà Babel en place
seo_desc: 'By Jamie Kyle

  Flow is a static type checker for JavaScript. It makes you more productive by providing
  feedback as you write code. Flow gives you warnings in real-time that point out
  when you’ve made a mistake. If you would like to know more, check ou...'
---

Par Jamie Kyle

Flow est un vérificateur de types statique pour JavaScript. Il vous rend plus productif en fournissant des retours d'information pendant que vous écrivez du code. Flow vous donne des avertissements en temps réel qui pointent lorsque vous avez fait une erreur. Si vous souhaitez en savoir plus, consultez [flowtype.org](https://flowtype.org/).

Plutôt que d'essayer de construire son propre écosystème entièrement séparé, Flow s'intègre à l'écosystème JavaScript existant. Utiliser Babel pour compiler votre code est l'une des manières les plus simples d'intégrer Flow dans un projet.

Après deux ans de travail acharné, Babel fonctionne pratiquement partout, il suffit de regarder la page de configuration avec des intégrations pour [tous les outils de construction que vous pouvez imaginer](http://babeljs.io/docs/setup/).

Si vous n'avez pas encore configuré Babel, vous pouvez utiliser ce guide pour vous installer. Vous pourriez également vouloir consulter mon [manuel sur Babel](https://github.com/thejameskyle/babel-handbook).

![Image](https://cdn-media-1.freecodecamp.org/images/jnjy7OosWCrCZ9O8fqF3Bg8NbCPnggn804el)

### Configurer Flow sur Babel

Une fois que vous avez configuré Babel, il est facile de commencer avec Flow. Commençons par installer deux dépendances :

```
$ npm install --save-dev babel-plugin-transform-flow-strip-types
$ npm install --global flow-bin
```

Le plugin Babel est là pour supprimer les types Flow afin que votre programme s'exécute. **flow-bin** est la manière dont vous utilisez Flow depuis la ligne de commande.

Ensuite, ajoutons le plugin Babel à votre **.babelrc** (ou là où vous configurez Babel avec des options) :

```
{
  presets: [...],
  plugins: [..., "transform-flow-strip-types"]
}
```

> **Note :** Je suppose que vous utilisez Babel 6 pour ce tutoriel. Il est recommandé de [mettre à jour](http://babeljs.io/blog/2015/10/31/setting-up-babel-6) si vous ne l'avez pas déjà fait.

Enfin, nous exécuterons **flow init** dans notre répertoire, ce qui créera un fichier **.flowconfig** qui devrait ressembler à ceci :

```
[ignore]
```

```
[include]
```

```
[libs]
```

```
[options]
```

Super ! Maintenant nous avons Flow entièrement configuré dans votre projet. Que diriez-vous de commencer à l'exécuter sur certains fichiers ?

### Faire fonctionner Flow

Flow est conçu pour être introduit dans votre dépôt de manière incrémentielle. Cela signifie que vous n'avez pas à l'ajouter à l'ensemble de votre base de code en une seule fois. Au lieu de cela, vous pouvez l'ajouter fichier par fichier au fur et à mesure. Commençons par quelque chose de simple pour vous lancer.

Tout d'abord, essayez de trouver un fichier qui n'a pas beaucoup de complexité ou de dépendances externes. Quelque chose avec juste une poignée de fonctions simples pour commencer.

```
import {getNumberFromString} from "string-math-lib";
```

```
export function multiplyStrings(a, b) {
  return getNumberFromString(a) * getNumberFromString(b);
}
```

Afin de faire fonctionner Flow sur ce fichier, nous devons ajouter un commentaire "flow pragma" en haut comme ceci :

```
// @flow
```

```
import {getNumberFromString} from "string-math-lib";
```

```
export function multiplyStrings(a, b) {
  return getNumberFromString(a) * getNumberFromString(b);
}
```

Ce petit commentaire en haut du fichier indique à Flow "Okay, je veux que vous vérifiiez les types de ce fichier".

Maintenant, nous devons réellement exécuter Flow pour la première fois. Pour ce faire, vous devrez revenir à votre terminal et exécuter la commande suivante :

```
$ flow
```

> **Note :** Cette commande est un alias de **flow status**. 

Ce que fait cette commande, c'est démarrer un serveur Flow et lui demander le "statut" de votre dépôt, ce qui retournera probablement quelques erreurs à corriger.

Les erreurs les plus courantes que vous allez voir dans un nouveau fichier sont :

* "Annotation manquante"
* "Module requis introuvable"

Ces erreurs sont liées aux imports et exports. La raison pour laquelle elles apparaissent est le résultat de la manière dont Flow fonctionne. Afin de vérifier les types à travers les fichiers, Flow regarde directement les imports et exports de chaque fichier.

#### **"Annotation manquante"**

Vous verrez une erreur comme celle-ci de la part de Flow car elle est somehow liée à un export de votre fichier. Autrement, Flow ne se plaindra pas des annotations de type manquantes.

Ainsi, afin de corriger cela, nous pouvons commencer à ajouter quelques types à votre fichier. Pour un guide détaillé sur la manière de le faire, [voir le guide utilisateur](https://flowtype.org/docs/type-annotations.html). Ce à quoi vous devriez aboutir, c'est avec quelques types comme ceci :

```
import {getNumberFromString} from "string-math-lib";
```

```
export function multiplyStrings(a: string, b: string): number {
  return getNumberFromString(a) * getNumberFromString(b);
}
```

Continuez à exécuter **flow** pendant que vous ajoutez vos types pour voir les effets de ce que vous faites. Finalement, vous devriez pouvoir éliminer toutes les erreurs "Annotation manquante".

#### "Module requis introuvable"

Vous obtiendrez ces erreurs chaque fois que vous avez un import/require qui ne peut pas être résolu en utilisant l'algorithme de module normal de Node ou si vous l'avez ignoré avec votre **.flowconfig**.

Cela peut être causé par beaucoup de choses, peut-être utilisez-vous un résolveur webpack spécial, peut-être avez-vous oublié d'installer quelque chose. Quelle que soit la raison, Flow doit être capable de trouver le module que vous importez pour faire son travail correctement. Vous avez quelques options sur la manière de résoudre cela :

1. **module.name_mapper —** spécifiez une expression régulière pour correspondre aux noms de modules, et un motif de remplacement.
2. Créez une définition de bibliothèque pour le module manquant

Nous nous concentrerons sur la création d'une définition de bibliothèque pour le module, si vous devez utiliser **module.name_mapper**, vous pouvez en voir plus à ce sujet [dans la documentation](https://flowtype.org/docs/advanced-configuration.html#options).

#### Créer une définition de bibliothèque

Avoir des définitions de bibliothèque est utile pour donner des types aux packages que vous avez installés et qui n'ont pas de types. Configurons-en une pour notre bibliothèque **string-math-lib** de l'exemple précédent.

Tout d'abord, créez un répertoire **flow-typed** dans votre répertoire racine (le répertoire où vous mettez votre **.flowconfig**).

> Vous pouvez utiliser d'autres noms de répertoire en utilisant la section **[lib]** de votre **.flowconfig**. Cependant, l'utilisation de **flow-typed** fonctionnera directement.

Maintenant, nous allons créer un fichier **flow-typed/string-math-lib.js** pour contenir notre "libdef" et le commencer comme ceci :

```
declare module "string-math-lib" {
  // ...
}
```

Ensuite, nous devons simplement écrire des définitions pour les exports de ce module.

```
declare module "string-math-lib" {
  declare function getNumberFromString(str: string): number
}
```

> **Note :** Si vous devez documenter l'export "default" ou principal, vous pouvez le faire avec **declare module.exports:** ou **declare export default**

Il y a beaucoup plus à dire sur les définitions de bibliothèque, vous devriez donc lire la [documentation](https://flowtype.org/docs/declarations.html) et lire [cet article de blog sur la manière de créer des libdefs de haute qualité](https://medium.com/@thejameskyle/flow-mapping-an-object-373d64c44592).

#### Installer une libdef depuis flow-typed

![Image](https://cdn-media-1.freecodecamp.org/images/fnjErEoc73SGhKGGham9ABRSZpDjgRv9hk96)

Parce que les libdefs peuvent consommer beaucoup de temps, nous maintenons un dépôt officiel de libdefs de haute qualité pour toutes sortes de packages appelé [flow-typed](https://github.com/flowtype/flow-typed).

Pour commencer avec flow-typed, installez l'interface de ligne de commande (CLI) globalement :

```
$ npm install --global flow-typed
```

Maintenant, vous pouvez regarder dans [**flow-typed/definitions/npm**](https://github.com/flowtype/flow-typed/tree/master/definitions/npm) pour voir s'il existe une libdef existante pour un package que vous souhaitez utiliser, si c'est le cas, vous pouvez l'installer comme ceci :

```
$ flow-typed install chalk@1.0.0 --flowVersion 0.30
```

Cela indique à flow-typed que vous souhaitez installer le package **chalk** à la version **1.0.0** lorsque vous exécutez Flow **0.30**. 

La CLI **flow-typed** est encore en bêta et de nombreuses améliorations sont prévues, attendez-vous donc à ce qu'elle s'améliore beaucoup dans un proche avenir.

N'oubliez pas de contribuer aux libdefs de flow-typed. C'est un effort communautaire, et plus il y a de personnes qui contribuent, meilleur c'est.

#### Autres erreurs que vous pourriez rencontrer :

Espérons que nous avons couvert presque tout ce que vous rencontrerez en commençant avec Flow. Cependant, vous pourriez également rencontrer des erreurs comme celles-ci :

* Le package à l'intérieur de **node_modules** signale des erreurs
* La lecture de **node_modules** prend beaucoup de temps
* Un JSON malformé à l'intérieur de **node_modules** provoque des erreurs

Il y a une poignée de raisons pour ces types d'erreurs que je n'aborderai pas dans cet article (je travaille sur une documentation détaillée pour chaque erreur individuelle). Pour l'instant, afin de continuer à avancer, vous pouvez simplement **[ignorer]** les fichiers qui causent ces erreurs.

Cela signifie ajouter des chemins de fichiers à votre section **[ignore]** dans votre **.flowconfig** comme ceci :

```
[ignore]
./node_modules/package-name/*
./node_modules/other-package/tests/*.json
```

```
[include]
```

```
[libs]
```

```
[options]
```

Il existe généralement de meilleures options que celle-ci, mais cela devrait vous donner un bon point de départ.

> Pour des exemples de la manière de mieux gérer les erreurs dans node_modules, voir cette [réponse Stack Overflow sur fbjs](http://stackoverflow.com/questions/38225538/flow-type-checker-errors-in-node-modules/38264353#38264353).

#### **Astuce pro : Vérifier pour voir à quel point vous êtes couvert**

Si vous vous demandez à quel point un fichier est couvert par Flow, vous pouvez utiliser la commande suivante pour voir un rapport de couverture :

```
$ flow coverage path/to/file.js --color
```

### Ressources supplémentaires et support

Il y a beaucoup de choses qui n'ont pas été couvertes par cet article. Voici donc quelques liens vers des ressources qui peuvent vous aider.

* [Site Web de Flow](https://flowtype.org/)
* [Essayer Flow en ligne](https://flowtype.org/try/)
* [Flow GitHub](https://github.com/facebook/flow)
* [Stack Overflow #flowtyped](http://stackoverflow.com/questions/tagged/flowtype)

L'équipe Flow s'engage à faire en sorte que tout le monde ait une excellente expérience avec Flow. Si ce n'est jamais le cas, nous aimerions avoir de vos nouvelles sur la manière de nous améliorer.

Suivez [James Kyle sur twitter](https://twitter.com/thejameskyle). Suivez également [Flow sur twitter](https://twitter.com/flowtype).