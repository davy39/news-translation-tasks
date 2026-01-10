---
title: Apprenez à repérer les signaux d'alerte dans votre code React/JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-06T20:11:15.000Z'
originalURL: https://freecodecamp.org/news/learn-to-spot-red-flags-in-your-react-javascript-code-d52d5fac85f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tfKnZ6l_0P7r1Wim-n-0og.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Apprenez à repérer les signaux d'alerte dans votre code React/JavaScript
  ?
seo_desc: 'By Donavon West

  This opinionated article will explain some of the red flags to look for when reviewing
  a React/JavaScript project. Avoiding these patterns can make your code more performant,
  more reliable, and easier to maintain.

  ? Look out for the l...'
---

Par Donavon West

Cet article subjectif expliquera certains des signaux d'alerte à rechercher lors de la révision d'un projet React/JavaScript. Éviter ces modèles peut rendre votre code plus performant, plus fiable et plus facile à maintenir.

### ? Méfiez-vous du mot-clé `let`

À l'époque d'ES5, `var` était le seul moyen à notre disposition pour créer des variables. ES6 a introduit les mots-clés `let` et `const` à portée de bloc.

D'après mon expérience, je vois très peu de situations où vous devriez utiliser `let`. Bien sûr, il a sa place (comme un compteur, par exemple), mais pour la plupart des applications, `const` est mieux adapté. Vous verrez bientôt pourquoi.

Prenons le cas d'utilisation suivant. Il rend le `montant` en rouge s'il est négatif, sinon, il sera en noir.

```
let color;
```

```
if (amount < 0) {  color = 'red';} else {  color = 'black';}
```

```
return (  <span style={{ color }}>    {formatCurrency(amount)}  </span>);
```

Le code utilise un `let`, mais après l'initialisation, la variable `color` n'est jamais réassignée. **C'est exactement le cas d'utilisation pour un `const` !**

Nous ne pouvons pas simplement remplacer le `let` par un `const` à cause de la structure du code. Cependant, si nous le refactorisons pour utiliser un ternaire, un `const` fonctionne parfaitement.

```
const color = amount < 0 ? 'red' : 'black';
```

Non seulement nous sommes passés de 6 lignes de code à 1, mais en utilisant un `const` au lieu d'un `let`, nos outils lanceront une erreur si nous réassignons involontairement `const` ailleurs dans le code.

Voici le résultat d'ESLint si j'essaie de définir `color` sur `null` après sa définition.

```
/Users/donavon/Projects/my-project/src/index.jsx
```

```
43:5  error 'color' is constant
```

Alors, la prochaine fois que vous sentez votre mémoire musculaire commencer à taper `let`, reprenez-vous et utilisez un `const` à la place. Neuf fois sur dix, cela vous conviendra parfaitement.

#### Avantages de l'utilisation de const

* Vous oblige à écrire un code plus propre
* Vérification à la compilation de la réassignation involontaire de variables

### ? La destructuration est votre amie

Selon [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) :

> La syntaxe d'**affectation par destructuration** est une expression JavaScript qui permet de déballer les valeurs des tableaux, ou les propriétés des objets, dans des variables distinctes.

Cela rend également le code significativement plus facile à lire. Prenons cet extrait par exemple.

```
render() {  return(    <div className={this.props.className}>      {        this.props.isLoading          ? 'Loading...'          : this.props.children      }    </div>  );}
```

Il y a plusieurs opérations `this.props` en cours. Cela est plus lent à exécuter (OK, marginalement, mais plusieurs recherches de propriétés d'objet doivent encore se produire), et cela ajoute du désordre visuel.

```
render() {  const { className, isLoading, children } = this.props;
```

```
  return(    <div className={className}>      {isLoading ? 'Loading...' : children}    </div>  );}
```

En ajoutant la ligne de code ci-dessus, le reste du code est plus lisible.

#### Avantages de la **destructuration**

* Potentiellement plus rapide à exécuter
* Plus propre
* Moins sujet aux erreurs cachées causées par des fautes de frappe

### ? Préférez l'opérateur de propagation à Object.assign

Il fut un temps où faire une copie superficielle d'un objet ou construire un objet à partir d'autres objets nécessitait `Object.assign`. Mais aujourd'hui, avec l'aide de Babel, nous pouvons utiliser la nouvelle syntaxe de propagation ES.

Voici un exemple de code utilisant `Object.assign`.

```
const defaults = { foo: 'foo', bar: 'bar' };const obj1 = Object.assign({}, defaults, { bar: 'baz' });// {foo:'foo', bar:'baz'}
```

Le code ci-dessous produit les mêmes résultats, mais en utilisant la syntaxe de propagation d'objet.

```
const defaults = { foo: 'foo', bar: 'bar' };const obj1 = { ...defaults, bar: 'baz' };// {foo:'foo', bar:'baz'}
```

Ce "sucre syntaxique" vous permet de voir les données avec lesquelles vous travaillez sans tout le bruit et le désordre causés par la plomberie ES5. Vous pouvez en lire plus sur le bruit et le désordre dans mon article "[**Le bruit est tout autour de nous**](https://medium.freecodecamp.org/noise-is-all-around-us-d0c0fcb8d48)".

[Axel Rauschmayer](https://www.freecodecamp.org/news/learn-to-spot-red-flags-in-your-react-javascript-code-d52d5fac85f4/) a une excellente explication approfondie de la propagation vs `Object.assign` dans son article "[ES2018 : Rest/Spread Properties](http://2ality.com/2016/10/rest-spread-properties.html)". Cela vaut vraiment la peine si vous aimez creuser dans la plomberie.

#### Avantages de l'utilisation de la propagation

* Moins de désordre
* Potentiellement plus efficace

### ? Utiliser un ternaire au lieu d'un ET logique

Pour des conditions `if` simples, un ternaire n'est pas l'outil approprié. J'explique cela en détail dans mon article sur les ternaires et le ET logique dans mon article "[**Rendu conditionnel dans React en utilisant des ternaires et le ET logique**](https://medium.freecodecamp.org/conditional-rendering-in-react-using-ternaries-and-logical-and-7807f53b6935)".

#### Avantages de l'utilisation du ET logique

* Moins de désordre

### ? Fonction fléchée avec corps d'expression

Les fonctions fléchées sont parfaites pour écrire des composants fonctionnels sans état (SFC) dans React et se présentent sous deux formes. La forme avec corps de déclaration comme ceci.

```
const SomeFunction = () => {  return 'value';};
```

Et la forme avec corps d'expression qui a une instruction `return` implicite.

```
const SomeFunction = () => 'value';
```

Certaines personnes appellent cela à tort "ligne unique", mais comme vous pouvez le voir ci-dessous, l'expression peut s'étendre sur plusieurs lignes. Notez que j'utilise des parenthèses et non des accolades.

```
const SomeFunction = () => (  'value');
```

Donc, si votre fonction retourne une seule expression, et que vous n'avez pas besoin d'instructions `const` de calcul intermédiaire, utilisez la forme d'expression sur la fonction fléchée. C'est une idée simple, et presque trop évidente lorsqu'elle est écrite comme ceci, mais c'est une chose facile à négliger pour certaines personnes.

Heureusement, ESLint peut à nouveau venir à votre secours.

```
/Users/donavon/Projects/my-project/src/index.jsx
```

```
  12:17  error Unexpected block statement surrounding arrow body;         move the returned value immediately after the `=>`
```

La seule chose à retenir est que pour retourner un objet dans la forme d'expression, vous devez enfermer le littéral de l'objet dans des parenthèses, comme ceci.

```
const SomeFunction = () => ({  foo: 'foo',  bar: 'bar',});
```

#### Avantages des fonctions fléchées avec corps d'expression

* Moins de désordre

### ? Éliminez ce code dupliqué

Vous ne pensiez pas que j'écrirais un article sur les signaux d'alerte dans votre code sans mentionner DRY, n'est-ce pas ? C'est parti...

Jetez un coup d'œil aux deux SFC suivants.

```
const Foo = () => (  <div>    <h2 className="sectionTitle">      Foo Title    </h2>    ...  </div>);
```

```
const Bar = () => (  <div>    <h2 className="sectionTitle">      Bar Title    </h2>    ...  </div>);
```

Remarquez comment les sections surlignées du code ci-dessus dans `Foo` et `Bar` sont presque identiques. Il est évident qu'ils affichent tous les deux un titre dans un certain style. Et si vous aviez le même code en 4, 5, ou plus d'endroits ? Il est très probable que tout changement futur nécessiterait que vous fassiez le changement à plusieurs endroits.

Vous devriez refactoriser le code dupliqué dans sa propre fonction. Cela s'appelle DRYing ou [Don't Repeat Yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

```
const Title = text => (  <h2 className="sectionTitle">    {text}  </h2>);
```

```
const Foo = () => (  <div>    <Title text="Foo Title" />    ...  </div>);
```

```
const Bar = () => (  <div>    <Title text="Bar Title" />    ...  </div>);
```

#### Avantages du code DRY

* Plus propre
* Plus maintenable

### ? Pourquoi utilisez-vous un constructeur ?

De nombreuses fois, lors de l'écriture d'un composant de classe React avec état, vous créez un constructeur pour définir la valeur initiale de `state`. Voici un exemple courant.

```
constructor(props) {  super(props);  this.state = { count: 0 };}
```

Mais saviez-vous que vous pouvez faire tout cela en utilisant la nouvelle proposition de propriétés de classe ? Le code ci-dessus peut être écrit simplement comme ceci.

```
state = { count: 0 };
```

Vous pouvez en lire plus à ce sujet dans mon article "[**Le constructeur est mort, vive le constructeur**](https://hackernoon.com/the-constructor-is-dead-long-live-the-constructor-c10871bea599)".

#### Avantages de ne pas utiliser un constructeur

* Plus propre

### ? Conclusion

Comme je l'ai dit en introduction, apprendre à éviter certains de ces modèles peut rendre votre code plus performant, plus fiable et plus facile à maintenir.

Ce ne sont pas des règles strictes, mais des lignes directrices générales destinées à ouvrir vos yeux à d'autres façons de regarder le code. À utiliser avec prudence. Les résultats peuvent varier.

Des règles ESLint strictes vous aideront grandement à repérer certains de ces problèmes pour vous, ou... vous pouvez toujours me taguer dans votre pull request. ?

Je m'excuse si cet article vous a semblé être un épisode de flashback de votre sitcom préféré (je déteste ceux-là), mais je voulais exposer ceux d'entre vous qui n'ont jamais lu mes autres articles, à la chance de plonger plus profondément.

J'écris également pour le blog d'ingénierie d'American Express. Consultez mes autres travaux et ceux de mes talentueux collègues sur [AmericanExpress.io](http://americanexpress.io/). Vous pouvez également [me suivre sur Twitter](https://twitter.com/donavon).