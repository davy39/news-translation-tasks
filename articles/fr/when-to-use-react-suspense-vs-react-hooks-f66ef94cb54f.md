---
title: Quand utiliser React Suspense vs React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T13:59:44.000Z'
originalURL: https://freecodecamp.org/news/when-to-use-react-suspense-vs-react-hooks-f66ef94cb54f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7vvZM3wS9aUoDvyqt3yR9Q.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Quand utiliser React Suspense vs React Hooks
seo_desc: 'By Vitalii Akimov

  React Suspense is to a Monad as Hooks are to Applicative Notation

  Monads and Applicative Functors are extensively used in functional programming.
  There is a relationship between them and React Suspense for Data Fetching and React
  Ho...'
---

Par Vitalii Akimov

#### React Suspense est à une Monade ce que les Hooks sont à la Notation Applicative

Les Monades et les Functeurs Applicatifs sont largement utilisés en programmation fonctionnelle. Il existe une relation entre eux et React Suspense pour la Récupération de Données et les APIs React Hooks. Voici une introduction rapide et simple aux Monades et aux Applicatifs, ainsi qu'une description de leurs similitudes.

Cet article traite de React Suspense pour la Récupération de Données, et non de React Suspense pour le Code Splitting (`React.Suspense` et `React.lazy`) récemment publié.

#### Notation do des Monades

L'approche du framework React encourage les développeurs à utiliser des techniques de programmation fonctionnelle. Au moins, les fonctions de rendu des composants ne devraient pas avoir d'effets secondaires observables. JavaScript n'a aucun moyen de garantir cela, mais il existe des langages de programmation qui le peuvent. Par exemple, Haskell n'accepte aucun effet secondaire.

Les fonctions pures rendent le code modulaire, prévisible et plus facile à vérifier. Mais elles augmentent également considérablement la verbosité. Voici une déclaration du tutoriel [Monads for functional programming](https://homepages.inf.ed.ac.uk/wadler/papers/marktoberdorf/baastad.pdf) (1995) de [Phil Walder](https://en.wikipedia.org/wiki/Philip_Wadler) :

> C'est en termes de modularité que le flux de données explicite devient à la fois une bénédiction et une malédiction. D'une part, c'est l'ultime modularité. Toutes les données entrantes et sortantes sont rendues manifestes et accessibles, offrant un maximum de flexibilité. D'autre part, c'est le nadir de la modularité. L'essence d'un algorithme peut être enterrée sous la plomberie nécessaire pour transporter les données de leur point de création à leur point d'utilisation.

Les Monades résolvent ce problème pour Haskell. Et Suspense/Hooks résolvent le même problème dans React.

Alors, qu'est-ce qu'une Monade ? C'est une interface abstraite simple qui possède deux fonctions, appelons-les `of` et `chain`.

* `of` — prend n'importe quelle valeur et retourne une valeur monadique (avec effets)
* `chain` — prend une valeur avec effets et une fonction de n'importe quelle valeur à une valeur avec effets et retourne une autre valeur avec effets

Les valeurs avec effets peuvent encapsuler n'importe quelle information spécifique à l'implémentation concrète. Il n'y a pas d'exigences sur ce que cela doit être exactement, ce sont des données opaques. Les implémentations concrètes de l'interface doivent suivre un ensemble de lois, et c'est tout.

Il n'y a rien de plus à dire sur les monades puisqu'elles sont abstraites. Elles ne stockent pas nécessairement quoi que ce soit, n'emballent ou ne déballent rien, ou même ne chaînent rien.

Mais pourquoi en avons-nous besoin si c'est si abstrait et définit presque rien ? L'interface fournit un moyen abstrait de composer des calculs avec des effets secondaires.

Si vous écrivez du code en JavaScript, vous pouvez vous demander maintenant. Vous avez déjà composé beaucoup de calculs avec des effets secondaires sans voir de Monade. Mais en fait, vous pouvez considérer que vous les avez déjà utilisés.

En informatique, les Monades sont d'abord apparues pour étudier les effets secondaires dans les langages impératifs. Elles sont un outil pour intégrer des mondes impératifs dans un monde mathématique pur pour une étude plus approfondie.

Ainsi, si vous souhaitez convertir votre programme impératif en formules mathématiques le représentant, faire cela avec des expressions Monad serait le moyen le plus simple et le plus direct. C'est si direct que vous n'avez même pas besoin de le faire manuellement, il existe des outils qui le font pour vous.

Haskell a un sucre syntaxique appelé do-notation exactement pour cela. Cela rend possible l'écriture de programmes impératifs en Haskell. Il y a un outil spécial dans son compilateur. Il convertit de tels programmes impératifs en expressions pures Monadiques Haskell. Les expressions sont proches des mathématiques que vous voyez dans les manuels.

JavaScript est un langage impératif. Nous pouvons considérer tout code impératif comme étant déjà une do-notation. Mais contrairement à celle de Haskell, elle n'est pas abstraite. Elle ne fonctionne que pour les effets secondaires intégrés. Il n'y a aucun moyen d'ajouter la prise en charge de nouveaux effets sauf en étendant le langage.

Il existe de telles extensions, à savoir les générateurs, async et les fonctions de générateurs async. Le compilateur JIT JavaScript convertit les fonctions async et générateurs en appels d'API intégrés concrets. Haskell n'a pas besoin de telles extensions. Son compilateur convertit la do-notation en appels de fonctions d'interface de Monades abstraites.

Voici un exemple de la façon dont les fonctions async simplifient les sources. Cela montre à nouveau pourquoi nous devons nous soucier d'avoir une syntaxe pour les effets.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uPPyZSrp-3AuABxNnfPhmA.gif)
_de [@manekinekko](http://www.async-await.xyz" rel="noopener" target="_blank" title="">www.async-await.xyz</a> par Wassim Chegham (<a href="https://twitter.com/@manekinekko" rel="noopener" target="_blank" title="))_

Pour cet article, nous n'avons besoin que de deux effets intégrés de JavaScript. Appelons-les Mutation et Exception. Ils ont des significations claires. Les Mutations permettent de changer les valeurs de certaines références. JavaScript a l'effet Exceptions intégré en utilisant les instructions `throw`/`try-catch`.

Nous pouvons convertir certains effets en d'autres. De cette façon, nous pouvons écrire du code async en utilisant des Générateurs.

Ce truc de conversion peut également être appliqué à d'autres effets. Et apparemment, juste Mutation et Exception suffisent pour obtenir n'importe quel autre effet. Cela signifie que nous pouvons transformer n'importe quelle fonction simple en une do-notation abstraite déjà. Et c'est exactement ce que fait Suspense.

Lorsque le code rencontre une opération avec effets et nécessite une suspension, il lance une exception. Elle contient certains détails (par exemple un objet Promise). L'un de ses appelants attrape l'exception, attend que la promesse dans l'argument soit résolue, stocke la valeur résultante dans un cache, et réexécute la fonction avec effets depuis le début.

Après que la Promise est résolue, le moteur appelle à nouveau la fonction. L'exécution reprend depuis son début, et lorsqu'elle rencontre les mêmes opérations, elle retourne sa valeur depuis le cache. Elle ne lance pas d'exception et continue l'exécution jusqu'à la prochaine demande de suspension ou la sortie de la fonction. Si la fonction n'a pas d'autres effets secondaires, son exécution devrait suivre les mêmes chemins et toutes les expressions pures sont recalculées, produisant les mêmes valeurs.

Réimplémentons Suspense. Contrairement à React, celui-ci fonctionne avec l'interface abstraite des Monades. Pour simplifier, mon implémentation cache également un cache de ressources. Au lieu de cela, la fonction runner compte les effets invoqués et utilise la valeur actuelle du compteur comme clé pour le cache interne. Voici le runner pour l'interface abstraite :

```js
/** effectful expression throws this object if it requires suspension */
const token = {};

/** Pointer to mutable data used to record effectful computations */
let context;

/** Runs `thunk()` as an effectful expression with `of` and `chain` as Monad's definition */
const run = (of, chain) => thunk => {
  /** here it caches effects requests */
  const trace = [];
  const ctx = {trace};
  return step();
  function step() {
    const savedContext = context;
    ctx.pos = 0;
    try {
      context = ctx;
      return of(thunk());
    } catch(e) {
      /** re-throwing other exceptions */
      if (e !== token)
        throw e;
      const {pos} = ctx;
      return chain(ctx.effect,
                   (value) => {
                     trace.length = pos;
                     /* recording the resolved value */
                     trace[pos] = value;
                     ctx.pos = pos + 1;
                     /** replay */
                     return step(value);
                   })
    } finally {
      context = savedContext;
    }
  }
}

/** marks effectful expression */
const M = eff => {
  /* if the execution is in a replay stage the value will be cached */
  if (context.pos < context.trace.length)
    return context.trace[context.pos++];
  /* saving the expression to resolve in `run` */
  context.effect = eff;
  throw token;
}
```

Maintenant, ajoutons une implémentation concrète des effets Async. Les Promesses, malheureusement, ne sont pas exactement des monades puisque une loi des Monades ne tient pas pour elles, et c'est une source de problèmes subtils, mais elles sont toujours adaptées à notre do-notation.

Voici l'implémentation concrète des effets Async :

```js
const runPromise = run(
  v => Promise.resolve(v), 
  (arg, f) => arg.then(f));
```

Et voici un exemple simple, il attend des valeurs retardées avant de procéder au rendu :

%[https://codesandbox.io/s/714n51l6mq?from-embed]

Le bac à sable contient également un wrapper `Component`. Il transforme un composant fonctionnel avec effets en un composant React. Il ajoute simplement un callback `chain` et met à jour l'état en conséquence. Cette version n'a pas encore de fonctionnalité de repli sur seuil, mais le dernier exemple ici en dispose.

Le runner est abstrait, donc nous pouvons l'appliquer pour autre chose. Essayons cela pour le hook `useState`. C'est une Monade de Continuation, et non une Monade d'État comme son nom pourrait le suggérer.

La valeur avec effets ici est une fonction qui prend un callback comme argument. Ce callback est appelé lorsque le runner a une valeur à transmettre. Par exemple, lorsque le callback retourné par `useState` est appelé.

Ici, pour simplifier, j'utilise des continuations de callback unique. Les Promesses ont une continuation supplémentaire pour la propagation des échecs.

```js
const runCont = run(
  value => cont => cont(value),
  (arg, next) => cont => arg(value => next(value)(cont)));

const useState = initial =>
  M(cont => 
    cont([initial, function next(value) { cont([value,next]); }]));
```

Et voici un exemple d'utilisation fonctionnel, avec la plupart de "kit.js" copié-collé, à l'exception de la définition de la monade.

%[https://codesandbox.io/s/j79mv6yv0v?from-embed]

Malheureusement, ce n'est pas exactement le hook `useState` de React, et la section suivante montre pourquoi.

#### Notation do Applicative

Il existe une autre extension pour la do-notation en Haskell. Elle cible non seulement les appels d'interface abstraite Monad mais aussi les appels d'interface abstraite des Functeurs Applicatifs.

Les interfaces Applicatives partagent la fonction `of` avec les Monades et il y a une autre fonction, appelons-la `join`. Elle prend un tableau de valeurs avec effets et retourne une seule valeur avec effets se résolvant en un tableau. Le tableau résultant contient toutes les valeurs auxquelles chaque élément du tableau d'argument a été résolu.

J'utilise une interface différente de celle de Haskell. Les deux sont équivalentes cependant — il est simple de convertir l'interface de Haskell en celle utilisée ici et vice versa. Je fais cela parce que cette base est beaucoup plus simple à utiliser en JavaScript, elle n'a pas besoin de fonctions d'ordre supérieur, et il y a déjà son instance dans le runtime standard.

En Haskell et en JavaScript, toute Monade est immédiatement un Functeur Applicatif. Cela signifie que nous n'avons pas besoin d'écrire une implémentation concrète de l'interface Applicative, nous pouvons la générer automatiquement.

S'il y a une implémentation par défaut, pourquoi avons-nous besoin des Functeurs Applicatifs ? Il y a deux raisons. La première est que tous les Functeurs Applicatifs ne sont pas des Monades, donc il n'y a pas de méthode `chain` à partir de laquelle nous pouvons générer `join`. Une autre raison est que, même s'il y a `chain`, une implémentation personnalisée de `join` peut faire la même chose d'une manière différente, probablement plus efficacement. Par exemple, récupérer des ressources en parallèle plutôt qu'en séquence.

Il y a une instance de cette interface pour les Promesses dans le runtime standard. C'est `Promise.all` (en ignorant certains détails ici pour simplifier à nouveau).

Revenons maintenant à l'exemple d'état. Que se passe-t-il si nous ajoutons un autre compteur dans le composant ?

%[https://codesandbox.io/s/3k0j3olk61?from-embed]

Le deuxième compteur réinitialise maintenant sa valeur lorsque le premier est incrémenté. Ce n'est pas ainsi que les Hooks sont censés fonctionner. Les deux compteurs devraient conserver leurs valeurs et fonctionner en parallèle.

Cela se produit parce que chaque invocation de continuation efface tout ce qui suit dans le code. Lorsque le premier compteur change sa valeur, toute la continuation suivante est redémarrée depuis le début. Et là, la valeur du deuxième compteur est à nouveau 0.

Dans l'[implémentation de la fonction run](https://medium.com/dailyjs/react-suspense-as-a-monad-notation-and-hooks-as-an-applicative-notation-f66ef94cb54f#fae1), l'invalidation se produit à la ligne 26 — `trace.length = pos` — cela supprime toutes les valeurs mémorisées après la valeur actuelle (à `pos`). Au lieu de cela, nous pourrions essayer de diff/patch le trace. Ce serait une instance de Monade Adaptative utilisée pour les calculs incrémentiels. MobX et des bibliothèques similaires sont très similaires à cela.

Si nous invoquons des opérations avec effets uniquement depuis le niveau supérieur d'une fonction, il n'y a pas de branches ou de boucles. Tout sera bien fusionné en écrasant les valeurs aux positions correspondantes, et c'est exactement ce que font les Hooks. Essayez de supprimer la ligne dans le bac à sable de code pour les deux compteurs ci-dessus.

#### Alternative de Transpiler

L'utilisation des Hooks rend déjà les programmes plus concis, réutilisables et lisibles. Imaginez ce que vous pourriez faire s'il n'y avait pas de limitations (Règles des Hooks). Les limitations sont dues à l'intégration uniquement au runtime. Nous pouvons supprimer ces limitations au moyen d'un transpiler.

[Effectful.JS](https://github.com/awto/effectfuljs) est un transpiler pour intégrer des effets dans JavaScript. Il prend en charge les cibles Monadiques et Applicatives. Il simplifie grandement les programmes dans les phases de conception, d'implémentation, de test et de maintenance.

Contrairement aux React Hooks et Suspense, le transpiler n'a pas besoin de suivre de règles. Il fonctionne pour n'importe quelle instruction JavaScript (branches, boucles, exceptions, etc.). Il ne réexécute jamais les fonctions depuis le début. C'est plus rapide. De plus, les fonctions peuvent utiliser n'importe quel effet secondaire intégré de JavaScript.

Effectful.JS n'est pas exactement un transpiler mais plutôt un outil pour créer des transpilers. Il existe également quelques transpilers prédéfinis et de nombreuses options de réglage. Il prend en charge la syntaxe à double niveau, avec des marqueurs spéciaux pour les valeurs avec effets (comme les expressions `await` dans les fonctions async, ou le `do` de Haskell). Et il prend également en charge une syntaxe à niveau unique où cette information est implicite (comme Suspense, Hooks ou les langages avec Algebraic Effects).

J'ai rapidement construit un transpiler de type Hooks à des fins de démonstration — [@effectful/react-do](https://github.com/awto/effectfuljs/tree/master/samples/react-do). Appeler une fonction avec des noms commençant par « use » est considéré comme ayant des effets. Les fonctions ne sont transpilées que si leur nom commence par « use » ou si elles ont une directive de bloc « component » ou « effectful » (une chaîne au début de la fonction).

Il existe également des directives de niveau bloc « par » et « seq » pour basculer entre les cibles applicatives et monadiques. Avec le mode « par » activé, le compilateur analyse les dépendances des variables et injecte `join` au lieu de `chain` si possible.

Voici l'exemple avec deux compteurs, mais maintenant adapté avec le transpiler :

%[https://codesandbox.io/s/mzp619y8wj?from-embed]

À des fins de démonstration, il implémente également Suspense pour le Code Splitting. La fonction entière fait six lignes de long. Consultez-la dans l'implémentation runtime [@effectful/react-do/main.js](https://github.com/awto/effectfuljs/blob/master/samples/react-do/main.js). Dans l'exemple suivant, j'ai ajouté un autre compteur dont le rendu est artificiellement retardé à des fins de démonstration.

%[https://codesandbox.io/s/nwmxwnp34j?from-embed]

#### Effets Algébriques

Les Effets Algébriques sont souvent mentionnés avec Suspense et Hooks. Ceux-ci peuvent être des détails internes ou un outil de modélisation, mais React ne fournit pas les Effets Algébriques à son userland de toute façon.

Avec l'accès aux Effets Algébriques, les utilisateurs pourraient remplacer le comportement des opérations en utilisant leur propre Effect Handler. Cela fonctionne comme des exceptions avec la capacité de reprendre un calcul après `throw`. Par exemple, une fonction de bibliothèque lance une exception si un fichier n'existe pas. Toute fonction appelante peut remplacer la manière dont elle peut le gérer, soit l'ignorer ou quitter le processus, etc.

EffectfulJS n'a pas d'Effets Algébriques intégrés. Mais leur implémentation est une petite bibliothèque runtime sur le dessus des continuations ou des monades libres.

L'appel d'une continuation efface également tout ce qui suit le `throw` correspondant. Il existe également une syntaxe spéciale et des règles de typage pour obtenir l'API Applicative (et Arrows) — [Algebraic Effects and Effect Handlers for Idioms and Arrows](http://homepages.inf.ed.ac.uk/slindley/papers/aeia.pdf). Contrairement à Applicative-do, cela interdit l'utilisation de quoi que ce soit qui nécessite des opérations Monad.

#### Conclusion

Le transpiler est un fardeau et a son propre coût d'utilisation. Comme pour tout autre outil, utilisez-le uniquement si ce coût est inférieur à la valeur que vous obtenez.

Et vous pouvez accomplir beaucoup avec EffectfulJS. C'est une nouvelle façon d'écrire des programmes JavaScript. Il est utile pour les projets avec une logique métier complexe. Tout workflow complexe peut être un script simple et maintenable.

Par exemple, Effectful.JS peut remplacer Suspense, Hooks, Context et Components State avec de petites fonctions. Les Error Boundaries sont les instructions `try-catch` habituelles. Le rendu asynchrone est un planificateur asynchrone. Mais nous pouvons l'utiliser pour n'importe quels calculs, pas seulement pour le rendu.

Il y a beaucoup d'autres utilisations spécifiques à l'application, et je vais en écrire plus bientôt. Restez à l'écoute !