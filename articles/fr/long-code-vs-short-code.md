---
title: 'Code long vs. code court : quoi de mieux pour votre cas d''utilisation ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-24T17:05:41.000Z'
originalURL: https://freecodecamp.org/news/long-code-vs-short-code
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c00740569d1a4ca2f4c.jpg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
seo_title: 'Code long vs. code court : quoi de mieux pour votre cas d''utilisation
  ?'
seo_desc: 'By Alfrick Opidi

  In order to successfully program an application, you need to make a number of small
  decisions while trying to solve a greater set of problems.

  How wisely you make those decisions, and whether you write long lines of code or
  short lin...'
---

Par Alfrick Opidi

Afin de programmer une application avec succès, vous devez prendre un certain nombre de petites décisions tout en essayant de résoudre un ensemble plus grand de problèmes.

La sagesse avec laquelle vous prenez ces décisions, et si vous écrivez de longues lignes de code ou de courtes lignes de code, dépend davantage de vos préférences, de vos compétences et des résultats attendus.

Vous vous demandez peut-être : entre le code long et le code court, lequel est le meilleur ?

Voici quelques facteurs à considérer avant de décider d'utiliser beaucoup ou peu de lignes de code.

## 1. Lisibilité

[Martin Fowler](https://en.wikipedia.org/wiki/Martin_Fowler), un expert en développement logiciel, a un jour déclaré : « N'importe quel idiot peut écrire du code qu'un ordinateur peut comprendre. Les bons programmeurs écrivent du code que les humains peuvent comprendre ».

Créez votre code en pensant aux autres. D'une part, il sera traité par une machine, qui ne se soucie pas de savoir si vous utilisez beaucoup ou peu de code. Mais votre code source peut évoluer entre les mains d'autres personnes qui doivent comprendre comment le code fonctionne et quelles améliorations elles doivent apporter.

Ainsi, lors de la programmation, la lisibilité du code source sera souvent plus importante que le nombre de lignes de code.

Voici un exemple de code JavaScript qui utilise la syntaxe de l'opérateur ternaire pour une instruction `if..else` :

```js
const firstNumb = 100;

let secondNumb;

const secondNumb = firstNumb > 50 ? "Le nombre est supérieur à 50" : "Le nombre est inférieur à 50";

```

Voici le même code écrit dans le format long traditionnel :

```js
const firstNumb = 100;

let secondNumb;

if (firstNumb > 50) {
  secondNumb = "Le nombre est supérieur à 50";
} else {
  secondNumb = "Le nombre est inférieur à 50";
}

```

Le deuxième style de programmation comprend beaucoup plus de lignes de code que le premier. Mais on pourrait soutenir qu'il est plus facile à lire et à interpréter, surtout pour les programmeurs novices.

Néanmoins, la première version avec la syntaxe de l'opérateur ternaire pourrait être un gain de temps considérable si vous souhaitez écrire une instruction `if..else` en une seule ligne.

Si vous travaillez sur un projet avec d'autres équipes de programmation, assurez-vous que votre code est lisible. Surtout si vous vous souciez de la durabilité à long terme du projet.

Vous devez considérer que d'autres développeurs peuvent ne pas être en mesure d'interpréter facilement votre code source. Vous devez donc rendre votre code facilement et rapidement compréhensible.

Par exemple, si vous collaborez avec d'autres développeurs pour construire une application qui récupère le [contenu Netflix](https://vpnpro.com/guides-and-tutorials/how-to-change-netflix-region/), il est préférable d'utiliser de longues lignes de code claires. Dans ce cas, les courtes lignes de code peuvent seulement montrer à vos pairs que vous êtes « intelligent », et leurs contributions peuvent ne pas être utiles.

## 2. Maintenabilité

Le code court et confus peut être difficile à maintenir. Cela peut entraîner des problèmes comme des bugs et des coûts de maintenance plus élevés. Cela peut également causer des problèmes de motivation et de simple pagaille pour vous en tant que développeur.

Et si vous écrivez un court morceau de code et découvrez que vous êtes incapable de l'interpréter six mois plus tard ? Un code plus long et plus détaillé pourrait vous aider à vous réapproprier ce que vous avez écrit et pourquoi vous l'avez écrit dans ce style particulier.

Avec un code plus long, le [débogage](https://docs.microsoft.com/en-us/visualstudio/debugger/debugging-absolute-beginners?view=vs-2019) d'un programme devient beaucoup plus facile, car vous aurez des variables non liées à examiner et plus d'endroits pour insérer des points d'arrêt.

D'autre part, un code court et peu clair peut gaspiller du temps et de l'argent pendant que les développeurs refactorisent ou réécrivent le code existant pour inclure de nouvelles fonctionnalités qui sont [plus faciles à maintenir](https://www.freecodecamp.org/news/legacy-software-maintenance-challenges/) à long terme.

Ce code est plus court :

```js
let a, b, c= 50;
```

Cependant, il est plus facile de maintenir le code ci-dessous :

```js
let a;

let b;

let c = 50;
```

## 3. Efficacité

On pourrait soutenir que l'utilisation de lignes de code plus courtes est plus efficace que de répartir le code sur plusieurs lignes. Si vous avez plus de lignes de code, il y a plus d'endroits où les bugs peuvent se cacher et les trouver peut être plus fastidieux.

Moins de lignes de code peuvent atteindre les mêmes résultats (et probablement mieux) que de nombreuses lignes de code. Si vous réduisez la quantité de code dans une tâche, vous diminuerez le nombre de bugs, surtout si le code source est clair, lisible et maintenable.

De plus, l'écriture de longues lignes de code peut vous obliger à inclure trop de variables locales, car vous devez formuler des noms pour elles. Tous ces noms différents peuvent entraîner de la confusion et des programmes inefficaces.

Si vous souhaitez construire des applications efficaces avec moins de bugs pour vous tracasser, alors utiliser moins de lignes de code peut être votre meilleure solution.

## 4. Charge de travail attendue

La programmation en shorthand vous permet de faire plus avec moins, et réduit donc considérablement le nombre d'heures que vous passez à développer vos applications. Avec une formation et une expérience suffisantes, vous pouvez apprendre à faire plus rapidement et avec moins de lignes de code.

Comme vous le savez probablement, les longues lignes de code sont parfois exigeantes à écrire et peuvent vous faire travailler de longues heures.

Avec un code court, vous pouvez réduire la quantité de code nécessaire pour les instructions répétitives et la manipulation de chaînes. Ainsi, au lieu d'utiliser un code verbeux, vous pouvez combiner commodément de nombreuses étapes en une seule étape et réduire considérablement votre charge de travail et les autres coûts associés.

Voici un exemple de code JavaScript écrit en utilisant de nombreuses lignes :

```js
function myFunc(foo) {
  console.log("Hello World", foo);
}

setTimeout(function () {
  console.log("Téléchargement terminé");
}, 3000);

mylist.forEach(function (foo) {
  console.log(foo);
});

```

Et voici le même code dans un format plus court écrit en utilisant la [syntaxe des fonctions fléchées JavaScript](https://guide.freecodecamp.org/javascript/arrow-functions/) :

```js
myFunc = (foo) => console.log("Hello World", foo);

setTimeout(() => console.log("Téléchargement terminé"), 3000);

mylist.forEach((foo) => console.log(foo));

```

Clairement, le premier exemple nécessite plus de temps à écrire que le deuxième exemple.

Si la charge de travail est importante pour vous et que vous avez des compétences en programmation suffisantes, alors utiliser un code plus court est probablement la voie à suivre.

## Conclusion

En fin de compte, le choix entre utiliser un code long ou un code court n'a pas d'importance. Ce qui compte, c'est d'écrire le code de manière adaptée à son utilisation prévue. Un code source plus long que nécessaire entraînera plus d'erreurs, une charge inutile accrue et un gaspillage de temps et de ressources.

D'autre part, si vous écrivez un code plus court en remplaçant de nombreuses lignes de code simples par une ligne de code complexe, ou des instructions verbeuses par des instructions vagues, ou des opérations simples par des hacks étranges, alors la perte en utilité globale l'emportera normalement sur le gain en concision.

Ainsi, lors de la construction d'une application, vous devez vous assurer que chaque ligne sert son objectif prévu. Et que vous utilisiez de longues lignes de code ou de courtes lignes de code ne devrait pas être votre principale motivation.

Votre objectif réel pour chaque cas devrait être d'atteindre des normes élevées de lisibilité, de maintenabilité, d'efficacité et de rentabilité, généralement dans cet ordre. Et le nombre de lignes de code ne devrait pas avoir sa place dans cette liste.