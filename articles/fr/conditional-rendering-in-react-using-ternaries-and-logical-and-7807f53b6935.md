---
title: Rendu conditionnel dans React en utilisant les ternaires et le ET logique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-01T12:59:42.000Z'
originalURL: https://freecodecamp.org/news/conditional-rendering-in-react-using-ternaries-and-logical-and-7807f53b6935
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eASRJrCIVgsy5VbNMAzD9w.jpeg
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
seo_title: Rendu conditionnel dans React en utilisant les ternaires et le ET logique
seo_desc: 'By Donavon West

  There are several ways that your React component can decide what to render. You
  can use the traditional if statement or the switch statement. In this article, we’ll
  explore a few alternatives. But be warned that some come with their o...'
---

Par Donavon West

Il existe plusieurs façons pour un composant React de décider ce qu'il doit rendre. Vous pouvez utiliser l'instruction `if` traditionnelle ou l'instruction `switch`. Dans cet article, nous explorerons quelques alternatives. Mais attention, certaines comportent leurs propres pièges si vous n'êtes pas prudent.

### Ternaire vs if/else

Supposons que nous avons un composant auquel est passé une prop `name`. Si la chaîne n'est pas vide, nous affichons un message de salutation. Sinon, nous demandons à l'utilisateur de se connecter.

Voici un Stateless Function Component (SFC) qui fait exactement cela.

```
const MyComponent = ({ name }) => {  if (name) {    return (      <div className="hello">        Hello {name}      </div>    );  }  return (    <div className="hello">      Please sign in    </div>  );};
```

Assez simple. Mais nous pouvons faire mieux. Voici le même composant écrit en utilisant un **opérateur ternaire conditionnel**.

```
const MyComponent = ({ name }) => (  <div className="hello">    {name ? `Hello ${name}` : 'Please sign in'}  </div>);
```

Remarquez à quel point ce code est concis par rapport à l'exemple précédent.

Quelques points à noter. Comme nous utilisons la forme à instruction unique de la fonction fléchée, l'instruction `return` est implicite. De plus, l'utilisation d'un ternaire nous a permis de DRY le balisage `<div className="hello">` dupliqué. ?

### Ternaire vs ET logique

Comme vous pouvez le voir, les ternaires sont parfaits pour les conditions `if/else`. Mais qu'en est-il des conditions `if` simples ?

Regardons un autre exemple. Si `isPro` (un booléen) est `true`, nous devons afficher un emoji de trophée. Nous devons également afficher le nombre d'étoiles (si ce n'est pas zéro). Nous pourrions procéder comme suit.

```
const MyComponent = ({ name, isPro, stars}) => (  <div className="hello">    <div>      Hello {name}      {isPro ? '?' : null}    </div>    {stars ? (      <div>        Stars:{'\u2b50\ufe0f'.repeat(stars)}      </div>    ) : null}  </div>); 
```

Mais remarquez que les conditions "else" retournent `null`. C'est parce qu'un ternaire attend une condition else.

Pour les conditions `if` simples, nous pourrions utiliser quelque chose de plus approprié : l'**opérateur ET logique**. Voici le même code écrit en utilisant un ET logique.

```
const MyComponent = ({ name, isPro, stars}) => (  <div className="hello">    <div>      Hello {name}      {isPro && '?'}    </div>    {stars && (      <div>        Stars:{'\u2b50\ufe0f'.repeat(stars)}      </div>    )}  </div>); 
```

Pas trop différent, mais remarquez comment nous avons éliminé le `: null` (c'est-à-dire la condition else) à la fin de chaque ternaire. Tout devrait s'afficher exactement comme avant.

Hé ! Qu'est-ce qui se passe avec John ? Il y a un `0` alors que rien ne devrait être affiché. C'est le piège dont je parlais plus haut. Voici pourquoi.

[Selon MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_Operators), un ET logique (c'est-à-dire `&&`) :

> `_expr1_ && _expr2_`

> Retourne `expr1` s'il peut être converti en `false` ; sinon, retourne `expr2`. Ainsi, lorsqu'il est utilisé avec des valeurs booléennes, `&&` retourne `true` si les deux opérandes sont vrais ; sinon, retourne `false`.

D'accord, avant que vous ne commeniez à vous arracher les cheveux, laissez-moi vous expliquer.

Dans notre cas, `expr1` est la variable `stars`, qui a une valeur de `0`. Parce que zéro est falsy, `0` est retourné et affiché. Voyez, ce n'était pas trop grave.

Je l'écrirais simplement ainsi.

> Si `expr1` est falsy, retourne `expr1`, sinon retourne `expr2`.

Donc, lorsque vous utilisez un ET logique avec des valeurs non booléennes, vous devez faire en sorte que la valeur falsy retourne quelque chose que React n'affichera pas. Par exemple, une valeur de `false`.

Il existe plusieurs façons d'y parvenir. Essayons cela à la place.

```
{!!stars && (  <div>    {'\u2b50\ufe0f'.repeat(stars)}  </div>)}
```

Remarquez l'opérateur double bang (c'est-à-dire `!!`) devant `stars`. (En fait, il n'y a pas d'opérateur "double bang". Nous utilisons simplement l'opérateur bang deux fois.)

Le premier opérateur bang va forcer la valeur de `stars` en un booléen puis effectuer une opération NOT. Si `stars` est `0`, alors `!stars` produira `true`.

Ensuite, nous effectuons une deuxième opération NOT, donc si `stars` est 0, `!!stars` produira `false`. Exactement ce que nous voulons.

Si vous n'êtes pas fan de `!!`, vous pouvez également forcer un booléen comme ceci (que je trouve un peu verbeux).

```
{Boolean(stars) && (
```

Ou simplement donner un comparateur qui résulte en une valeur booléenne (ce que certains pourraient dire est encore plus sémantique).

```
{stars > 0 && (
```

#### Un mot sur les chaînes de caractères

Les valeurs de chaînes vides souffrent du même problème que les nombres. Mais comme une chaîne vide rendue est invisible, ce n'est pas un problème que vous aurez probablement à traiter, ou même à remarquer. Cependant, si vous êtes perfectionniste et ne voulez pas d'une chaîne vide dans votre DOM, vous devriez prendre des précautions similaires à celles que nous avons prises pour les nombres ci-dessus.

### Une autre solution

Une solution possible, et qui peut être étendue à d'autres variables à l'avenir, serait de créer une variable séparée `shouldRenderStars`. Vous traitez alors avec des valeurs booléennes dans votre ET logique.

```
const shouldRenderStars = stars > 0;
```

```
return (  <div>    {shouldRenderStars && (      <div>        {'\u2b50\ufe0f'.repeat(stars)}      </div>    )}  </div>);
```

Ensuite, si à l'avenir, la règle métier est que vous devez également être connecté, posséder un chien et boire de la bière légère, vous pourriez changer la façon dont `shouldRenderStars` est calculé, et ce qui est retourné resterait inchangé. Vous pourriez également placer cette logique ailleurs où elle est testable et garder le rendu explicite.

```
const shouldRenderStars =   stars > 0 && loggedIn && pet === 'dog' && beerPref === 'light`;
```

```
return (  <div>    {shouldRenderStars && (      <div>        {'\u2b50\ufe0f'.repeat(stars)}      </div>    )}  </div>);
```

### Conclusion

Je suis d'avis que vous devriez tirer le meilleur parti du langage. Et pour JavaScript, cela signifie utiliser des opérateurs ternaires conditionnels pour les conditions `if/else` et des opérateurs ET logiques pour les conditions `if` simples.

Bien que nous puissions simplement revenir à notre place sûre et confortable où nous utilisons l'opérateur ternaire partout, vous possédez maintenant les connaissances et le pouvoir d'aller de l'avant ET prospérer.

_Je écris également pour le blog d'ingénierie d'American Express. Consultez mes autres travaux et ceux de mes collègues talentueux sur [AmericanExpress.io](http://americanexpress.io/). Vous pouvez également [me suivre sur Twitter](https://twitter.com/donavon)._