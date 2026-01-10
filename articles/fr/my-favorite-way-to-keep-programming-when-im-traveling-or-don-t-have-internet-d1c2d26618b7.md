---
title: Ma méthode préférée pour continuer à programmer en voyage ou sans internet
subtitle: ''
author: Andrico Karoulla
co_authors: []
series: null
date: '2018-11-14T17:32:46.000Z'
originalURL: https://freecodecamp.org/news/my-favorite-way-to-keep-programming-when-im-traveling-or-don-t-have-internet-d1c2d26618b7
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5djL-YOSdGd_rK_x
tags:
- name: JavaScript
  slug: javascript
- name: personal development
  slug: personal-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Ma méthode préférée pour continuer à programmer en voyage ou sans internet
seo_desc: 'This is a short guide on sharpening your skills and keeping productive
  when in transit. And it doesn’t involve burying your face in a book.

  Books can only get you so far

  Now don’t get me wrong, I love a good programming book. Jon Duckett’s series on
  ...'
---

Voici un court guide pour affûter vos compétences et rester productif en déplacement. Et cela n'implique pas de plonger le nez dans un livre.

### Les livres ne peuvent vous mener que jusqu'à un certain point

Ne vous méprenez pas, j'adore les bons livres de programmation. La série de Jon Duckett sur HTML, CSS et JavaScript a été une lumière directrice pendant mes années de formation en tant que développeur Web. L'ouvrage séminal de Robert C. Martin, Clean Code, a ses pages cornées et déformées après des années à en extraire chaque goutte d'information. Même Getting MEAN de Simon Holmes, bien que désormais obsolète, a eu son heure de gloire à mes côtés dans un café local. Il a été mon compagnon lors de la création de ma première application full-stack.

Avec un peu de préparation, la plupart de ces livres auraient pu être utilisés sans internet, ou pire, avec une connexion lente. Téléchargez les packages à l'avance. Faites fonctionner vos environnements locaux. Si le livre est suffisamment complet, vous ferez probablement des progrès solides sans avoir besoin de Google, GitHub ou StackOverflow.

En revanche, nous, les programmeurs, nous épanouissons mieux lorsqu'on nous lance un défi. Avoir un auteur qui nous guide à travers des solutions est agréable, mais ce n'est pas suffisant. La meilleure façon d'améliorer nos compétences en résolution de problèmes est de résoudre des problèmes.

Si vous êtes un programmeur professionnel, vous résolvez probablement votre part de problèmes au quotidien. Si vous êtes un passionné, vous trouvez peut-être du plaisir à créer vos propres applications [JSF**k](http://www.jsfuck.com/). Ou même à tuer le temps en résolvant des défis algorithmiques en ligne. C'est pourquoi des sites comme CodeWars ou HackerRank sont si populaires.

Le problème sous-jacent avec la plupart de ces sites, en particulier les derniers, est de continuer lorsque l'internet est coupé. Ou sans connexion dès le départ. Les deux scénarios sont courants alors que les développeurs deviennent de plus en plus nomades. Comment tuer le temps pendant votre vol de 12 heures de Londres à Shanghai, tout en récoltant les bénéfices de la résolution de problèmes ?

J'ai eu le désagrément de faire un tel long vol. Il y a à peine assez de place dans ledit vol pour poser votre ordinateur portable sur le plateau rabattable. Tout le reste devient un jeu de Tetris, essayant de faire tenir votre confort et vos affaires dans l'espace limité qui vous est donné sur votre vol low-cost. Donc, vous avez votre ordinateur portable, vos écouteurs, votre pull, vos snacks et votre eau tous à portée de main ? Cela commence à devenir étroit, n'est-ce pas ? Essayez de sortir votre livre de programmation de 600 pages et 2 kilos. Oui, ce n'est pas près d'arriver.

### La solution miracle

Alors, comment ai-je surmonté cet obstacle ? Eh bien, j'ai réimplémenté la bibliothèque Lodash.

Pourquoi ai-je choisi une tâche aussi arbitraire ? Il y a plusieurs raisons clés. Certaines que j'ai rationalisées avant de relever le défi et d'autres que j'ai découvertes en cours de route. En voici quelques-unes des plus notables :

* Chaque fonction ressemble à un mini défi de code
* La documentation est sur une seule page HTML, facile à télécharger et à consulter hors ligne
* Elle encourage à regarder à l'intérieur du code source en cas de blocage
* Elle vous permet de construire votre propre suite de fonctions utilitaires
* C'est une bibliothèque sans dépendances, ce qui simplifie les choses
* Vous vous familiariserez davantage avec votre langage de programmation préféré

Approfondissons un peu chacun de ces points.

#### **Chaque fonction ressemble à un défi de code**

Comme je l'ai mentionné précédemment, Codewars et HackerRack sont deux sites de défis de programmation très populaires. Pour ceux qui ne connaissent pas, on vous donne une tâche de programmation à compléter dans l'éditeur de texte intégré. Une fois terminée, vous exécutez votre code final contre la suite de tests curatée. Le but du défi est de faire passer tous les tests.

Il n'est pas difficile d'imiter cela soi-même. Si quoi que ce soit, c'est une excellente façon d'améliorer votre approche du TDD (développement piloté par les tests). Mon approche générale pour réimplémenter une fonction serait de créer un stub de la méthode :

```js
const concat = (arr, ...otherParams) => {
  // si le tableau est invalide, lancer une erreur

  // gérer l'absence d'entrée pour le deuxième paramètre

  // ajouter chaque élément à un nouveau tableau
    // aplatir d'un niveau si l'élément est un tableau

  // retourner le nouveau tableau
};
```

const concat = (arr, ...otherParams) => {  // si le tableau est invalide, lancer une erreur  // gérer l'absence d'entrée pour le deuxième paramètre  // ajouter chaque élément à un nouveau tableau    // aplatir d'un niveau si l'élément est un tableau  // retourner le nouveau tableau};

L'étape suivante est de créer ma suite de tests avec quelques assertions que je m'attends à ce que ma fonction satisfasse :

```js
const concat = require('../concat');

describe('concat', () => {
  it('should return the expect results with valid inputs', () => {
    expect(concat([1, 2], [1], [2], 4939, 'DDD')).toEqual([1, 2, 1, 2, 4939, 'DDD']);
    expect(concat([], null, 123)).toEqual([null, 123]);
  });

  it('should throw errors with invalid inputs', () => {
    expect(() => concat(23, 23).toThrow(TypeError));
    expect(() => concat([1, 2, 3], -1).toThrow(TypeError));
  });

  it('should correctly handle strange inputs', () => {
    expect(concat([111], null, 'rum ham')).toEqual([111, null, 'rum ham']);
  });
});
```

Ensuite, j'ai implémenté le code pour que les tests s'exécutent avec succès :

```js
const { isValidArray } = require('../helpers');

const concat = (arr, ...otherParams) => {
  if (!isValidArray(arr)) throw new Error('Argument is not a valid array');

  if (otherParams.length === 0) return [];

  const concatenatedArray = otherParams.reduce((acc, item) => {
    if (isValidArray(item)) return [...acc, ...item];

    return [...acc, item];
  }, [...arr]);

  return concatenatedArray
};
```

Réussir à implémenter une de ces fonctions vous laissera avec un sentiment de fierté et d'accomplissement.

#### **Documentation HTML simple**

La plupart des bibliothèques ont une page GitHub avec une référence API. Ce sont généralement des pages uniques de Markdown disponibles pour le téléchargement. Prenons un extrait de la bibliothèque Recompose :

### `branch()`

```js
branch(
  test: (props: Object) => boolean,
  left: HigherOrderComponent,
  right: ?HigherOrderComponent
): HigherOrderComponent
```

Accepte une fonction de test et deux composants d'ordre supérieur. La fonction de test reçoit les props du propriétaire. Si elle retourne vrai, le composant d'ordre supérieur `left` est appliqué à `BaseComponent` ; sinon, le composant d'ordre supérieur `right` est appliqué. Si `right` n'est pas fourni, il rendra par défaut le composant enveloppé.

Il y a ici suffisamment d'informations pour vous mettre sur la bonne voie. Si vous apprenez React et que vous voulez comprendre les HOCs (composants d'ordre supérieur), alors implémenter cette bibliothèque pourrait être un défi gratifiant à relever.

#### **Examen du code source**

Jusqu'à récemment, je ne prenais pas beaucoup de temps pour voir comment les packages que j'utilise le plus fonctionnent sous le capot. Être sans Google ou StackOverflow m'a rendu désespéré et j'ai donc commencé à regarder à l'intérieur. Je ne savais pas à quoi m'attendre, mais ce n'était pas un fouillis minifié et illisible.

Ouvrir la boîte de Pandore n'a pas envoyé un essaim de mépris, de haine et de famine pour me tourmenter, moi et ma famille. Au lieu de cela, j'ai été accueilli avec un code proprement écrit et bien documenté.

Vous pouvez même jeter un coup d'œil pour voir comment les gens de Lodash écrivent leurs solutions différemment des vôtres :

```js

function concat() {
  var length = arguments.length;
  if (!length) {
    return [];
  }
  var args = Array(length - 1),
      array = arguments[0],
      index = length;

  while (index--) {
    args[index - 1] = arguments[index];
  }
  return arrayPush(isArray(array) ? copyArray(array) : [array], baseFlatten(args, 1));
}
```

Vous apprendrez de nouvelles façons d'atteindre les mêmes objectifs. Peut-être que leurs solutions sont plus efficaces, peut-être que les vôtres le sont. C'est toujours une excellente façon d'ouvrir les yeux sur de nouveaux paradigmes et modèles.

#### **Développer vos propres fonctions utilitaires**

Lodash a mauvaise réputation en tant que bibliothèque ayant une grande empreinte. Les projets peuvent n'avoir besoin que d'un petit nombre d'utilitaires. Nous importerons tout de même la bibliothèque entière en tant que dépendance.

Vous pourriez télécharger les quelques fonctions que vous utilisez. Pourquoi ne pas utiliser les méthodes que vous avez passées 8 heures à écrire en volant au-dessus de l'océan Pacifique ? Cela ne sera peut-être pas aussi robuste. Mais vous vous souviendrez toujours de votre voyage à l'Angular Fest Hawaii '19 chaque fois que vous sortirez votre implémentation de `_.memoize`.

#### **Garder les choses simples**

Voyager est épuisant et voler est stressant. Lorsque vous êtes fatigué, tout niveau de bureaucratie qui se dresse sur le chemin de la programmation devient une barrière. L'idée est de choisir une tâche qui vous fait coder avec le moins de friction possible.

Je ne voulais pas m'embêter avec un tas de dépendances aléatoires et du code fournisseur désordonné lorsque j'étais coincé entre deux ronfleurs lors de mon vol de nuit vers le Canada. Ce fut un heureux hasard de découvrir que Lodash ne dépend d'aucun module externe. Le package Lodash lui-même est simple. Chaque méthode a son propre fichier, qui peut importer quelques méthodes de base ou utilitaires.

#### **Se familiariser avec vos outils de choix**

Si vous lisez cet article, il y a des chances que vous soyez familier avec JavaScript. Comme la plupart des autres langages de programmation modernes, JavaScript reçoit des mises à jour semi-régulières. Ces mises à jour vous donnent accès à de nouvelles fonctionnalités. Implémenter une bibliothèque peut vous emmener dans des recoins de votre langage choisi que vous n'avez jamais explorés auparavant. Cela m'est arrivé.

En fait, j'ai récemment découvert certains des nouveaux [objets intégrés](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects#Keyed_collections) de JavaScript. Je ne les avais jamais utilisés dans du code auparavant, alors j'ai fait un effort conscient pour en intégrer certains dans les méthodes utilitaires que j'ai créées :

```js
const difference = (arr, ...otherArgs) => {
  if (!isValidArray(arr)) throw new TypeError('First argument must be an array');

  const combinedArguments = otherArgs.reduce((acc, item) => [...acc, ...item], [])
  if (!isValidArray(combinedArguments)) throw new TypeError('2nd to nth arguments must be arrays');

  const differenceSet = new Set([...arr]);
  combinedArguments.forEach(item => {
    if (differenceSet.has(item)) differenceSet.delete(item);
  });

  return [...differenceSet]
}
```

Utiliser `Set()` a beaucoup de sens ici. Ce qui le distingue d'un tableau normal, c'est que seules des valeurs uniques peuvent être stockées. Cela signifie que vous ne pouvez pas avoir de valeurs en double à l'intérieur de votre ensemble. Cela fonctionne bien lorsque vous essayez de créer une fonction qui supprime les valeurs en double.

Que vous soyez guitariste, peintre ou physicien moléculaire, vous n'irez pas loin sans vous familiariser avec votre guitare, vos pinceaux ou vos... molécules ?

Il en va de même pour être programmeur. Maîtrisez vos outils et cherchez activement les lacunes dans vos connaissances. Faites un effort conscient pour implémenter des fonctionnalités que vous n'avez pas encore rencontrées. Ou utilisez celles que vous trouvez intimidantes. C'est l'une des façons les plus efficaces d'apprendre.

### **Conclusion**

Ce n'est pas la seule façon de rester productif sans internet, mais cela a bien fonctionné pour moi. En fait, c'est quelque chose que je recommande aux gens de faire dans les premières étapes de leur carrière en programmation.

J'adorerais savoir si vous avez fait quelque chose de similaire, ou si vous avez vos propres façons de rester affûté sans internet. Faites-le moi savoir ci-dessous !

Connaissez-vous d'autres packages qui se prêteraient bien à une réécriture ?

#### Merci d'avoir lu !

Le partage des connaissances est l'un des piliers de ce qui rend la communauté des développeurs si formidable. N'hésitez pas à commenter vos solutions.

Si vous êtes intéressé à m'inviter à une conférence, un meetup, ou en tant qu'invité pour toute autre engagement, vous pouvez me contacter sur [twitter](https://twitter.com/andricokaroulla?lang=en) !

J'espère que cet article vous a appris quelque chose de nouveau. Je publie régulièrement, alors si vous voulez rester à jour avec mes dernières publications, vous pouvez me suivre. Et n'oubliez pas, plus vous maintenez le bouton d'applaudissements enfoncé, plus vous pouvez donner d'applaudissements. ???

#### Vous pouvez également consulter mes autres articles ci-dessous :

[_Ajoutez une touche de Suspense à votre application web avec React.lazy()_](https://codeburst.io/add-a-touch-of-suspense-to-your-web-app-with-react-lazy-374e66ee05af)

[_Comment utiliser les nouveaux composants Query d'Apollo pour gérer l'état local_](https://medium.com/@andricokaroulla/updated-for-apollo-v2-1-managing-local-state-with-apollo-d1882f2fbb7)

[_Pas besoin d'attendre les vacances, commencez à Décorer maintenant_](https://codeburst.io/no-need-to-wait-for-the-holidays-start-decorating-now-67b9dabd60d7)

[_Gestion de l'état local avec Apollo et les Composants d'Ordre Supérieur_](https://itnext.io/managing-local-state-with-apollo-client-3be522258645)

[_Le jeu de boisson de la conférence React_](https://medium.com/@andricokaroulla/the-react-conference-drinking-game-7a996bfbef3)

[_Développez et déployez votre propre application React monorepo en moins de 2 heures, en utilisant Lerna, Travis et Now_](https://codeburst.io/develop-and-deploy-your-own-react-monorepo-app-in-under-2-hours-using-lerna-travis-and-now-2b140d647238)