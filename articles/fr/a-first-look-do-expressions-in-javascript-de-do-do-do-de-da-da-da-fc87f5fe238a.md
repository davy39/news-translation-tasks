---
title: 'Un premier regard : les expressions do en JavaScript (De Do Do Do, De Da Da
  Da)'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-03T15:52:11.000Z'
originalURL: https://freecodecamp.org/news/a-first-look-do-expressions-in-javascript-de-do-do-do-de-da-da-da-fc87f5fe238a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1EjPzePghALoUfc2lUcQOQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Un premier regard : les expressions do en JavaScript (De Do Do Do, De
  Da Da Da)'
seo_desc: 'By Donavon West

  This article is not about about the The Police’s 1980 hit song from album Zenyatta
  Mondatta (although that would be awesome!) No, it’s about the T39 proposal called
  do expressions. If approved by TC39, “do expressions” will be part of...'
---

Par Donavon West

Cet article ne traite **pas** de la chanson à succès de 1980 du groupe The Police issue de l'album [_Zenyatta Mondatta_](https://en.wikipedia.org/wiki/Zenyatta_Mondatta) (bien que ce serait génial !) Non, il s'agit de la proposition T39 appelée [do expressions](https://github.com/tc39/proposal-do-expressions). Si elle est approuvée par TC39, les « do expressions » feront partie de JavaScript et pourraient aider à sortir votre code de l'enfer des ternaires.

Les expressions do vous permettent d'intégrer une instruction à l'intérieur d'une expression. La valeur résultante est retournée par l'expression.

Elle est actuellement à ce qu'on appelle le « stade 1 » du processus TC39, ce qui signifie que les expressions do ont encore un long chemin à parcourir avant de voir le jour.

[Axel Rauschmayer](https://www.freecodecamp.org/news/a-first-look-do-expressions-in-javascript-de-do-do-do-de-da-da-da-fc87f5fe238a/undefined) explique le [processus TC39](http://exploringjs.com/es2016-es2017/ch_tc39-process.html) dans son livre intitulé [Exploring ES2016 and ES2017](https://leanpub.com/exploring-es2016-es2017/) (gratuit en ligne, ou achetez l'eBook).

### Qu'est-ce qu'une expression do ?

Voici un exemple simple d'une expression do simple.

```
const status = do {  if (isLoading) {    'Loading';  } else if (isError) {    'Error'  } else {    'Running'  };};
```

Elle prend ce qui est « retourné » comme valeur de l'instruction et l'assigne à `status`. Pas très utile par rapport à une instruction `if` basique, à mon avis.

Là où elle brille vraiment, c'est lorsqu'elle est utilisée dans JSX dans une application React.

### Utilisation dans JSX

Les expressions do sont particulièrement utiles dans JSX. Voyons comment vous pourriez les utiliser pour un motif React courant dans le contexte de JSX : déterminer ce qu'il faut rendre en fonction des props `loading` et `error`.

```
const View = ({ loading, error, ...otherProps }) => (  <div>    {do {      if (loading) {        <Loading />      } else if (error) {        <Error error={error} />      } else {        <MyLoadedComponent {...otherProps} />      };    }}  </div>);
```

Wow ! C'est incroyablement puissant.

La même chose pourrait être réalisée avec une instruction AND logique, mais vous finissez par nier toutes les autres valeurs. Cela peut devenir assez désordonné et est plutôt difficile à suivre. Ce n'est pas non plus aussi efficace d'un point de vue exécution, car cela est roughly équivalent à effectuer trois instructions `if`.

```
const View = ({ loading, error, ...otherProps }) => (  <div>    {loading && !error &&      <Loading />    }    {!loading && error &&      <Error error={error} />    }    {!loading && !error &&      <MyLoadedComponent {...otherProps} />    }  </div>);
```

### Qu'est-ce que l'enfer des ternaires ?

Pour un peu de contexte, un [ternaire](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) est un opérateur JavaScript qui accepte trois opérandes : une condition, suivie de deux expressions. Il est souvent utilisé pour remplacer une instruction `if`.

Voici un exemple d'un opérateur ternaire en action.

```
const text = isLoading ? 'Loading' : 'Loaded';
```

La variable `text` est définie sur « Loading » ou « Loaded » selon le drapeau binaire `isLoading`. Cela est roughly équivalent à l'instruction `if` suivante.

```
let text;
```

```
if (isLoading) {  text = 'Loading';} else {  text = 'Loaded';}
```

Cependant, remarquez que nous devons utiliser une instruction `let` au lieu d'un `const`. Vous pouvez voir qu'un ternaire est un excellent moyen de réduire l'encombrement de votre code, et il vous permet également d'éviter d'utiliser une instruction `let` inutile au lieu d'un `const`.

Je vois les instructions let comme un drapeau rouge lorsque je fais des revues de code. Même chose avec les instructions `if`.

Mais que se passe-t-il si nous avons une valeur non binaire ? Vous pourriez combiner des ternaires et finir avec quelque chose comme ceci.

```
const text =   stopSignColor === 'red'     ? 'Stop' :  stopSignColor === 'yellow'     ? 'Caution' :  stopSignColor === 'green'     ? 'Go' :  'Error';
```

C'est à cela que je fais référence lorsque je parle de l'enfer des ternaires.

C'est une sorte d'instruction `if/else if/else if/else` écrite en utilisant un ternaire. Beaucoup de gens trouvent cette forme difficile à suivre. En fait, vous pouvez même empêcher ce comportement avec un paramètre [ESLint `no-nested-ternary`](https://eslint.org/docs/rules/no-nested-ternary).

Voici le même code écrit en utilisant une instruction `switch` intégrée dans une expression do.

```
const text = do {  switch (stopSignColor) {  case 'red': 'Stop'  case 'yellow': 'Caution'  case 'green': 'Go'  case default: 'Error'  }};
```

### Le futur est maintenant

Même si les expressions do ne font pas officiellement partie du langage (pas encore ?), vous pouvez toujours les utiliser **maintenant** dans votre projet. Cela est dû au fait que la plupart d'entre nous ne codons pas vraiment en JavaScript — nous codons en Babel. Et heureusement, il existe une [transformation Babel](https://babeljs.io/docs/plugins/transform-do-expressions/) qui nous apportera la syntaxe du langage de demain dès aujourd'hui.

Mais soyez prudent lorsque vous choisissez cette option. Il n'y a aucune garantie que la proposition sera adoptée en l'état. La spécification peut changer de manière significative, laissant votre code dans le besoin d'une certaine refactorisation. En fait, il est tout à fait plausible que la spécification puisse être abandonnée entièrement.

### Conclusion

Les expressions do ont leur place, mais ne sont hardly une solution miracle. Avec l'aide d'une transformation Babel, elles peuvent être utilisées dès aujourd'hui. L'un des plus grands avantages des expressions do est lorsqu'elles sont utilisées depuis JSX.

Et c'est « tout ce que je veux vous dire ».

J'écris également pour le blog d'ingénierie d'American Express. Consultez mes autres travaux et ceux de mes collègues talentueux sur [AmericanExpress.io](http://americanexpress.io/). Vous pouvez également [me suivre sur Twitter](https://twitter.com/donavon).