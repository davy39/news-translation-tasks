---
title: Apprendre les bases des Hooks React en <10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T15:47:03.000Z'
originalURL: https://freecodecamp.org/news/learn-the-basics-of-react-hooks-in-10-minutes-b2898287fe5d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9FSQFJgVw_Ip1a3E4rmmow.png
tags:
- name: hooks
  slug: hooks
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Apprendre les bases des Hooks React en <10 minutes
seo_desc: 'By Emmanuel Ohans

  Early this year, the React team released a new addition, hooks, to React in version
  16.8.0.

  If React were a big bowl of candies, then hooks are the latest additions, very chewy
  candies with great taste!

  So, what exactly do hooks mea...'
---

Par Emmanuel Ohans

Début cette année, l'équipe React a publié une nouvelle addition, les hooks, à React dans la version 16.8.0.

Si React était un grand bol de bonbons, alors les hooks sont les dernières additions, des bonbons très moelleux avec un excellent goût !

Alors, que signifient exactement les hooks ? Et pourquoi valent-ils votre temps ?

### Introduction

L'une des principales raisons pour lesquelles les hooks ont été ajoutés à React est d'offrir une manière plus puissante et expressive d'écrire (et de partager) des fonctionnalités entre les composants.

> À long terme, nous nous attendons à ce que les Hooks soient le moyen principal pour les gens d'écrire des composants React — [Équipe React](https://reactjs.org/docs/hooks-faq.html#should-i-use-hooks-classes-or-a-mix-of-both)

Si les hooks vont être si importants, pourquoi ne pas apprendre à les connaître de manière amusante !

### Le Bol de Bonbons

Considérez React comme un beau bol de bonbons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u1Ubc4Zybc5AeACy38K08w.png)

Le bol de bonbons a été incroyablement utile pour les gens du monde entier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T-X_uzowaEqEDhRYkUfPvA.png)

Les personnes qui ont fait ce bol de bonbons se sont rendu compte que **certains** des bonbons dans le bol ne faisaient pas beaucoup de bien aux gens.

Certains bonbons avaient un excellent goût, oui ! Mais ils apportaient une certaine complexité lorsque les gens les mangeaient — pensez aux render props et aux composants d'ordre supérieur ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*9FSQFJgVw_Ip1a3E4rmmow.png)

Alors, que ont-ils fait ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*jahda3D5PnCmuyZOlqj5eA.png)

Ils ont fait la bonne chose — ne pas jeter tous les bonbons précédents, mais en créer de nouveaux.

Ces bonbons ont été appelés **Hooks**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WqUVZyfDQX6ihazFZ21w_g.png)

Ces bonbons existent pour un seul but : **faciliter les choses que vous faisiez déjà**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EG-OKgzmiZewSjEJ9l0y7Q.png)

Ces bonbons ne sont pas super spéciaux. En fait, lorsque vous commencez à les manger, vous réaliserez qu'ils ont un goût familier — ils sont simplement des **fonctions JavaScript** !

![Image](https://cdn-media-1.freecodecamp.org/images/1*HRw5WfHH02tvoM13sDSfVA.png)

Comme pour tous les bons bonbons, ces **10** nouveaux bonbons ont tous des noms uniques. Bien qu'ils soient collectivement appelés **hooks**.

Leurs noms commencent toujours par les trois lettres, _use …_ par exemple, `useState`, `useEffect`, etc.

Tout comme le chocolat, ces 10 bonbons partagent certains des mêmes ingrédients. Savoir comment l'un a un goût, vous aide à vous rappeler des autres.

Ça a l'air amusant ? Maintenant, dégustons ces bonbons.

### Le Hook d'État

Comme mentionné précédemment, les hooks sont des fonctions. Officiellement, il y en a 10. 10 nouvelles fonctions qui existent pour rendre l'écriture et le partage de fonctionnalités dans vos composants beaucoup plus expressifs.

Le premier hook que nous allons examiner s'appelle `useState`.

Pendant longtemps, vous ne pouviez pas utiliser l'état local dans un composant fonctionnel. Eh bien, pas jusqu'aux hooks.

Avec `useState`, votre composant fonctionnel peut avoir (et mettre à jour) un état local.

Comme c'est intéressant.

Considérez l'application de compteur suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2909ks8DqBVC23n2Ykqe0Q.gif)

Avec le composant `Counter` montré ci-dessous :

Simple, n'est-ce pas ?

Permettez-moi de vous poser une question simple. Pourquoi exactement avons-nous ce composant en tant que composant de classe ?

Eh bien, la réponse est simplement parce que nous devons garder une trace de l'état local dans le composant.

Maintenant, voici le même composant refactorisé en un composant fonctionnel avec accès à l'état via les hooks `useState`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GxX7yyUGXJG2Kmf8CIG3aQ.gif)
_Classe vers Hooks — attendez l'animation._

Qu'est-ce qui est différent ?

Je vais vous le décrire étape par étape.

Un composant fonctionnel n'a pas toute la syntaxe `Class extend ...`.

```
function CounterHooks() {  }
```

Il ne nécessite pas non plus de méthode `render`.

```
function CounterHooks() {    return (      <div>        <h3 className="center">Bienvenue au Compteur de la Vie </h3>        <button           className="center-block"           onClick={this.handleClick}> {count} </button>      </div>    ); }
```

Il y a deux problèmes avec le code ci-dessus.

1. Vous n'êtes pas censé utiliser le mot-clé `this` dans les composants fonctionnels.
2. La variable d'état `count` n'a pas été définie.

Extraire `handleClick` dans une fonction séparée au sein du composant fonctionnel :

```
function CounterHooks() {  const handleClick = () => {      }  return (      <div>        <h3 className="center">Bienvenue au Compteur de la Vie </h3>        <button           className="center-block"           onClick={handleClick}> {count} </button>      </div>    ); }
```

Avant la refactorisation, la variable `count` provenait de l'objet d'état du composant de classe.

Dans les composants fonctionnels, et avec les hooks, cela provient de l'invocation de la fonction ou du hook `useState`.

`useState` est appelé avec un argument, la valeur initiale de l'état, par exemple `useState(0)` où `0` représente la valeur initiale de l'état à suivre.

L'invocation de cette fonction retourne un tableau avec deux valeurs.

```
//? retourne un tableau avec 2 valeurs. useState(0) 
```

La première valeur étant la valeur actuelle de l'état suivie, et la seconde, une fonction pour mettre à jour la valeur de l'état.

Pensez à cela comme une réplique de `state` et `setState` — cependant, ils ne sont pas tout à fait les mêmes.

Avec cette nouvelle connaissance, voici `useState` en action.

```
function CounterHooks() {  // ?   const [count, setCount] = useState(0);  const handleClick = () => {    setCount(count + 1)  }  return (      <div>        <h3 className="center">Bienvenue au Compteur de la Vie </h3>        <button           className="center-block"           onClick={handleClick}> {count} </button>      </div>    ); } 
```

Il y a quelques points à noter ici, en plus de la simplicité évidente du code !

Premièrement, puisque l'invocation de `useState` retourne un tableau de valeurs, les valeurs peuvent être facilement déstructurées en valeurs séparées comme montré ci-dessous :

```
const [count, setCount] = useState(0);
```

De plus, notez comment la fonction `handleClick` dans le code refactorisé n'a pas besoin de référence à `prevState` ou autre chose de ce genre.

Elle appelle simplement `setCount` avec la nouvelle valeur `count + 1`.

```
  const handleClick = () => {    setCount(count + 1) }
```

Cela est dû au fait que la valeur correcte de la variable d'état `count` sera toujours maintenue à travers les re-rendus.

Ainsi, pour mettre à jour la variable d'état count, il suffit d'appeler `setCount` avec la nouvelle valeur, par exemple `setCount(count + 1)`.

Aussi simple que cela paraisse, vous avez construit votre tout premier composant en utilisant des hooks. Je sais que c'est un exemple artificiel, mais c'est un bon début !

**Nb** : il est également possible de passer une fonction à la fonction de mise à jour de l'état. Cela est généralement recommandé comme avec le `setState` de classe lorsqu'une mise à jour de l'état dépend d'une valeur précédente de l'état, par exemple `setCount(prevCount => prevCount +` 1)

#### Appels multiples à useState

Avec les composants de classe, nous nous sommes tous habitués à définir les valeurs d'état dans un objet, qu'elles contiennent une seule propriété ou plus.

```
// propriété unique state = {  count: 0}// propriétés multiples state = { count: 0, time: '07:00'}
```

Avec `useState`, vous avez peut-être remarqué une légère différence.

Dans l'exemple ci-dessus, nous avons seulement appelé `useState` avec la valeur initiale réelle. Pas un objet pour contenir la valeur.

```
useState(0)
```

Alors, que se passe-t-il si nous voulions une autre valeur d'état ?

Peut-on utiliser plusieurs appels à `useState` ?

Considérez le composant ci-dessous. Identique à avant, mais cette fois, il suit l'heure du clic.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E_BJDnVGUB8BLBs1tN2DKA.gif)

Comme vous pouvez le voir, l'utilisation des hooks est assez similaire, sauf qu'il y a un nouvel appel à `useState`.

```
const [time, setTime] = useState(new Date())
```

Maintenant, `time` est utilisé dans le `JSX` rendu pour récupérer l'heure, la minute et la seconde du clic.

```
<p className="center">    à : { `${time.getHours()} : ${time.getMinutes()} : ${time.getSeconds()}`}</p>
```

Super !

Cependant, est-il possible d'utiliser un objet avec `useState` plutôt que plusieurs appels à `useState` ?

Absolument !

Si vous choisissez de faire cela, vous devez noter que contrairement aux appels `setState`, les valeurs passées dans `useState` remplacent la valeur de l'état. `setState` fusionne les propriétés de l'objet, mais `useState` remplace la valeur entière.

### Le Hook d'Effet

Avec les composants de classe, vous avez probablement effectué des effets secondaires tels que la journalisation, la récupération de données ou la gestion des abonnements.

Ces effets secondaires peuvent être appelés "effets" pour faire court, et le hook d'effet, `useEffect`, a été créé à cette fin.

Comment est-il utilisé ?

Eh bien, le hook `useEffect` est appelé en lui passant une fonction dans laquelle vous pouvez effectuer vos effets secondaires.

Voici un exemple rapide.

```
useEffect(() => {  // ? vous pouvez effectuer des effets secondaires ici  console.log("useEffect premier timer ici.")}) 
```

À `useEffect`, j'ai passé une fonction anonyme avec un effet secondaire appelé à l'intérieur.

La question logique suivante est, quand la fonction `useEffect` est-elle appelée ?

Eh bien, rappelez-vous que dans les composants de classe, vous aviez des méthodes de cycle de vie telles que `componentDidMount` et `componentDidUpdate`.

Puisque les composants fonctionnels n'ont pas ces méthodes de cycle de vie, `useEffect` _remplace_ en quelque sorte leur place.

Ainsi, dans l'exemple ci-dessus, la fonction à l'intérieur de `useEffect`, également connue sous le nom de fonction d'effet, sera invoquée lorsque le composant fonctionnel est monté (`componentDidMount`) et lorsque le composant est mis à jour (`componentDidUpdate`).

Voici cela en action.

En ajoutant l'appel `useEffect` ci-dessus à l'application de compteur, voici le comportement que nous obtenons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0lmKYgp9IoA0ELj4Pfn7vw.gif)

**NB** : Le hook `useEffect` n'est pas entièrement le même que `componentDidMount` + `componentDidUpdate`. Il peut être considéré comme tel, mais l'implémentation diffère avec quelques différences subtiles.

Il est intéressant de noter que la fonction d'effet a été invoquée à chaque fois qu'il y avait une mise à jour. C'est bien, mais ce n'est pas toujours la fonctionnalité souhaitée.

Et si vous ne vouliez exécuter la fonction d'effet que lorsque le composant est monté ?

C'est un cas d'utilisation courant et `useEffect` prend un deuxième paramètre, un tableau de dépendances pour gérer cela.

Si vous passez un tableau vide, la fonction d'effet est exécutée uniquement au montage — les re-rendus ultérieurs ne déclenchent pas la fonction d'effet.

```
useEffect(() => {    console.log("useEffect premier timer ici.")}, []) 
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*RsAP38Wj8zUihrVXNwKcsw.gif)

Si vous passez des valeurs dans ce tableau, alors la fonction d'effet sera exécutée au montage, et chaque fois que les valeurs passées sont mises à jour. C'est-à-dire que si l'une des valeurs est modifiée, l'appel d'effet sera réexécuté.

```
useEffect(() => {    console.log("useEffect premier timer ici.")}, [count]) 
```

La fonction d'effet sera exécutée au montage, et chaque fois que la fonction count change.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0lmKYgp9IoA0ELj4Pfn7vw.gif)
_le count change lorsque le bouton est cliqué, donc la fonction d'effet est réexécutée_

Et les abonnements ?

Il est courant de s'abonner et de se désabonner de certains effets dans certaines applications.

Considérez ce qui suit :

```
useEffect(() => {  const clicked = () => console.log('fenêtre cliquée');  window.addEventListener('click', clicked);}, [])
```

Dans l'effet ci-dessus, lors du montage, un écouteur d'événement de clic est attaché à la fenêtre.

Comment se désabonner de cet écouteur lorsque le composant est démonté ?

Eh bien, `useEffect` permet cela.

Si vous retournez une fonction dans votre fonction d'effet, elle sera invoquée lorsque le composant est démonté. C'est l'endroit parfait pour annuler les abonnements comme montré ci-dessous :

```
useEffect(() => {    const clicked = () => console.log('fenêtre cliquée');    window.addEventListener('click', clicked);    return () => {      window.removeEventListener('click', clicked)    } }, [])
```

Il y a beaucoup plus de choses que vous pouvez faire avec le hook `useEffect`, comme effectuer des appels API.

### Construisez vos propres Hooks

Dès le début de cet article, nous avons pris (et utilisé) des bonbons dans la boîte à bonbons que React fournit.

Cependant, React fournit également un moyen pour vous de créer vos propres bonbons uniques — appelés hooks personnalisés.

Alors, comment cela fonctionne-t-il ?

Un hook personnalisé est simplement une fonction régulière. Cependant, son nom doit commencer par le mot `use` et, si nécessaire, il peut appeler l'un des hooks React à l'intérieur de lui-même.

Voici un exemple :

### Les Règles des Hooks

Il y a deux règles à respecter lors de l'utilisation des hooks.

1. N'appelez les Hooks qu'au [Niveau Supérieur](https://reactjs.org/docs/hooks-rules.html#only-call-hooks-at-the-top-level), c'est-à-dire _pas_ dans des conditionnels, des boucles ou des fonctions imbriquées.
2. N'appelez les Hooks que depuis des Fonctions React, c'est-à-dire des Composants Fonctionnels et des Hooks Personnalisés.

Ce plugin ESLint [plugin](https://www.npmjs.com/package/eslint-plugin-react-hooks) est excellent pour vous assurer de respecter ces règles dans vos projets.

### Autres Bonbons

Nous avons considéré quelques-uns des hooks que React fournit, mais il y en a plus !

Cette introduction devrait vous avoir préparé à aborder la documentation peut-être plus dense [documentation](https://reactjs.org/docs/hooks-intro.html). Consultez également ma feuille de triche réactive en direct et modifiable sur les [hooks cheatsheet](https://react-hooks-cheatsheet.com).