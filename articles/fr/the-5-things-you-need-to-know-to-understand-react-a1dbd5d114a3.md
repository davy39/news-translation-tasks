---
title: Les Cinq Doigts de la Mort de React. Maîtrisez ces cinq concepts, puis maîtrisez
  React.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-05T08:14:50.000Z'
originalURL: https://freecodecamp.org/news/the-5-things-you-need-to-know-to-understand-react-a1dbd5d114a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8RqHYTvYg4KX4_G_RiZ5Og.jpeg
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
seo_title: Les Cinq Doigts de la Mort de React. Maîtrisez ces cinq concepts, puis
  maîtrisez React.
seo_desc: 'By Sacha Greif

  A few years ago, my friend Sean started telling me how this brand new front-end
  library called React was going to take over the web. At first I dismissed it as
  just another framework fad. But then I started hearing about React more and...'
---

Par Sacha Greif

Il y a quelques années, mon ami Sean a commencé à me dire comment cette toute nouvelle bibliothèque front-end appelée [React](https://facebook.github.io/react/) allait prendre le contrôle du web. Au début, je l'ai rejetée comme une autre mode de framework. Mais ensuite, j'ai commencé à entendre parler de React de plus en plus, au point où je sentais que l'ignorer n'était plus une option.

Peut-être êtes-vous dans la même position que moi : vous entendez parler de React à gauche et à droite, mais vous asseoir et l'_apprendre_ semble être une corvée.

La bonne nouvelle est que vous pouvez réduire tout ce que vous devez savoir sur React à **cinq concepts clés**.

Maintenant, ne vous méprenez pas, cela ne signifie pas que je peux vous transformer en un maître de React instantanément. Mais au moins, vous comprendrez tous les concepts majeurs, si vous décidez de vous lancer.

Les cinq concepts clés sont :

1. **Les Composants**
2. **JSX**
3. **Props & State**
4. **L'API des Composants**
5. **Les Types de Composants**

Avant de commencer, notez que j'ai initialement appris React grâce aux cours de [Wes Bos](http://wesbos.com/), et j'ai inclus quelques liens d'affiliation vers ceux-ci. Chaque fois que possible, j'ai également inclus des liens vers des ressources gratuites.

Oh, et mon ami Sean ? Il est passé à des choses beaucoup plus avant-gardistes depuis. Après tout, React est _tellement_ 2015.

### Concept #1 : Comment fonctionnent les composants React

La première chose que vous devez savoir sur React est qu'il s'agit entièrement de **composants**. Votre base de code React est essentiellement une grande pile de grands composants qui appellent des composants plus petits.

Mais qu'est-ce qu'un composant, demandez-vous ? Un exemple parfait de composant est l'élément HTML commun `<select>`. Non seulement il vient avec sa propre sortie visuelle (la boîte grise, l'étiquette de texte et la flèche vers le bas qui composent l'élément lui-même) — il gère également sa propre logique d'ouverture et de fermeture.

![Image](https://cdn-media-1.freecodecamp.org/images/0xAAMB78GtbQa0YGc7jHBP5Wo2YjZeUhVY4C)
_Le classique <select>_

Imaginez maintenant pouvoir construire votre propre `<select>` personnalisé et autonome, avec son propre style et comportement :

![Image](https://cdn-media-1.freecodecamp.org/images/ahFp0oNOqmS946ezTrcyVBvWX585M2C3BQ2-)
_Une version plus élégante du bon vieux <select>_

Eh bien, c'est exactement ce que React vous permet de faire. Un composant React est un seul objet qui non seulement produit du HTML comme le ferait un modèle traditionnel, mais inclut également tout le code nécessaire pour _contrôler_ cette sortie.

En pratique, la manière la plus courante d'écrire des composants React est sous forme de **classe ES6** contenant une méthode `render` qui retourne du HTML. (Il existe également une manière super-secrète _fonctionnelle_, mais vous devrez attendre jusqu'au concept #4 pour en apprendre davantage à ce sujet) :

```
class MyComponent extends React.Component {
```

```
  render() {    return <p>Hello World!<p>;  }
```

```
}
```

### Concept #2 : Comment fonctionne JSX

Comme vous pouvez le voir, l'approche par composants signifie que le code HTML et JavaScript vivent dans le même fichier. L'arme secrète de React pour réaliser cette alliance impie est le [langage JSX](https://facebook.github.io/react/docs/jsx-in-depth.html) (où "X" signifie "XML").

JSX peut sembler étrange au début, mais on s'y habitue assez rapidement.

Oui, je sais. On nous a tous appris à maintenir une forte séparation entre HTML et JavaScript. Mais il s'avère que relâcher un peu ces règles peut réellement faire des merveilles pour votre productivité front-end.

Par exemple, puisque vous avez maintenant toute la puissance de JavaScript à votre disposition, voici comment vous pouvez afficher la date actuelle en insérant un extrait de JavaScript dans votre HTML en utilisant `{...}` :

```
class MyComponent extends React.Component {
```

```
  render() {    return <p>Today is: {new Date()}</p>;  }
```

```
}
```

Cela signifie également que vous utiliserez du JavaScript standard pour les instructions `if` ou les boucles, plutôt qu'une sorte de syntaxe spécifique aux modèles. L'opérateur [ternaire](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) de JavaScript est particulièrement utile ici :

```
class MyComponent extends React.Component {
```

```
  render() {    return <p>Hello {this.props.someVar ?  'World' : 'Kitty'}</p>;  }
```

```
}
```

Et au fait, si vous devez vous rafraîchir la mémoire sur les nouveaux points de la syntaxe JavaScript, je recommande [ES6 for Everyone](https://es6.io/friend/STATEOFJS) de Wes Bos (si vous aimez les vidéos) ou [Practical ES6](https://ponyfoo.com/books/practical-es6/chapters#toc) de Nicolas Bevacqua (si vous préférez lire).

### Concept #3 : Comment fonctionnent Props & State

Peut-être vous êtes-vous demandé d'où venait la variable `this.props.someVar` ci-dessus.

Si vous avez déjà écrit une ligne de HTML, vous êtes probablement familier avec les attributs HTML comme l'attribut `href` de la balise `<a>`. Dans React, les attributs sont connus sous le nom de **props** (abréviation de "properties"). Les props sont la manière dont les composants communiquent entre eux.

```
class ParentComponent extends React.Component {
```

```
  render() {    return <ChildComponent message="Hello World"/>;  }
```

```
}
```

```
class ChildComponent extends React.Component {
```

```
  render() {    return <p>And then I said, "{this.props.message}"</p>;  }
```

```
}
```

Pour cette raison, le flux de données de React est **unidirectionnel** : les données ne peuvent aller que des composants parents à leurs enfants, et non l'inverse.

Parfois, cependant, un composant doit réagir à des données qui **ne proviennent pas** d'un composant parent (comme une entrée utilisateur, par exemple). Et c'est là que l'**état** entre en jeu.

Une bonne métaphore pour comprendre la différence entre les props et l'état serait l'Etch-A-Sketch. Contrairement à des choses comme la couleur du corps et la position du cadran de la tablette Etch-A-Sketch (**props**), le dessin lui-même (**état**) n'est pas une propriété inhérente de l'Etch-A-Sketch. Ce n'est que le résultat temporaire de l'entrée utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/xAYoLms-eS2-jC9rcNRvpKLVXCkyzrQnXq3m)
_Représenté ici : votre composant React typique_

Notez que l'**état** d'un composant peut également être transmis à ses propres enfants en tant que **prop**. Vous pouvez penser à cela comme une grande rivière coulant en descente, avec le routeur, la couche de données et divers composants ajoutant chacun leur propre petit flux de données pour former l'état principal de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/tGTzybJdJyDJ3eXwXLEcgvmIJi0R-W02lio5)

À l'intérieur d'un composant, l'état est géré à l'aide de la fonction `[setState](https://facebook.github.io/react/docs/react-component.html#setstate)`, qui est souvent appelée à l'intérieur d'un [gestionnaire d'événements](https://facebook.github.io/react/docs/handling-events.html) :

```
class MyComponent extends React.Component {
```

```
  handleClick = (e) => {    this.setState({clicked: true});  }
```

```
  render() {    return <a href="#" onClick={this.handleClick}>Click me</a>;  }
```

```
}
```

En pratique, la grande majorité des données dans une application React seront une **prop**. Ce n'est que lorsque vous devez accepter une entrée utilisateur que vous utiliserez l'**état** pour gérer le changement.

Notez que nous utilisons ici une flèche grasse pour gérer la liaison du gestionnaire `handleClick`. Vous pouvez [en apprendre davantage sur cette technique ici](http://www.ian-thomas.net/autobinding-react-and-es6-classes/).

### Concept #4 : Comment fonctionne l'API des composants

Nous avons déjà mentionné `render` et `setState`, qui font tous deux partie d'un petit ensemble de méthodes de l'API des composants. Une autre méthode utile est le `[constructor](https://facebook.github.io/react/docs/react-component.html#constructor)`, que vous pouvez utiliser pour initialiser votre état et [lier les méthodes](https://medium.com/@housecor/react-binding-patterns-5-approaches-for-handling-this-92c651b5af56#.gzacvcu3h).

En dehors de ces trois fonctions, React fournit également un ensemble de rappels déclenchés à divers moments pendant le [cycle de vie du composant](https://facebook.github.io/react/docs/state-and-lifecycle.html) (avant le chargement, après le chargement, après le démontage, etc.). À moins que vous ne fassiez du React avancé, vous n'aurez probablement presque jamais besoin de vous soucier de ceux-ci.

Si cette section semble courte, c'est parce que l'apprentissage de React consiste en réalité beaucoup plus à maîtriser les concepts de programmation et d'architecture qu'à apprendre un ensemble de méthodes API ennuyeuses. C'est ce qui le rend si rafraîchissant !

### Concept #5 : Comment fonctionnent les types de composants

Nous avons vu comment utiliser des classes pour définir un composant :

```
class MyComponent extends React.Component {
```

```
  render() {    return <p>Hello World!<p>;  }
```

```
}
```

Et nous avons également parlé des méthodes de composant prises en charge par ces classes. Maintenant, oubliez tout cela ! De plus en plus, les gens écrivent des composants React en tant que **composants fonctionnels**.

Un composant fonctionnel est une fonction qui prend un objet `props` comme argument et retourne du HTML. Presque comme un modèle traditionnel, avec la différence clé que vous pouvez toujours utiliser le code JavaScript dont vous avez besoin à l'intérieur de cette fonction :

```
const myComponent = props => {
```

```
  return <p>Hello {props.name}! Today is {new Date()}.</p>
```

```
}
```

La conséquence de l'utilisation de la syntaxe des composants fonctionnels est que vous perdez l'accès aux méthodes de composant dont nous venons de parler. Mais il s'avère que, en pratique, c'est parfaitement acceptable, puisque la grande majorité de vos composants n'en auront probablement pas besoin.

Au fait, l'une de ces méthodes est `setState`, et cela signifie que les composants fonctionnels ne peuvent pas avoir d'état. Pour cette raison, ils sont souvent appelés **composants fonctionnels sans état**.

Puisque les composants fonctionnels nécessitent beaucoup moins de code standard, il est logique de les utiliser chaque fois que possible. Pour cette raison, la plupart des applications React contiennent un mélange sain des deux syntaxes.

Notez qu'il existe également une troisième syntaxe héritée utilisant [la fonction `createClass`](https://facebook.github.io/react/docs/react-api.html#createclass). Mais toute personne l'utilisant devrait être honteuse et appelée des noms pour oser encore utiliser des modèles de codage d'il y a 18 mois :

```
var Greeting = React.createClass({     render: function() {         return <h1>Hello, {this.props.name}</h1>;     }
```

```
});
```

### Concept #6 : Comment fonctionnent les rôles des composants

D'accord, j'ai menti. Il y a en fait six choses, pas cinq. Mais que puis-je dire, le film ne s'appelle pas "Six Doigts de la Mort". Bien que maintenant que j'y pense, cela semble être un film assez cool, impliquant probablement une sorte de maître alien de kung-fu cherchant vengeance.

Mais revenons au sujet en question. Voici les concepts architecturaux ennuyeux dont je parlais. Donc si rien de tout cela n'a de sens, n'hésitez pas à revenir une fois que vous aurez eu l'occasion de jouer avec React un peu plus.

Après avoir utilisé React pendant un certain temps, les gens ont commencé à voir deux "saveurs" distinctes de code apparaître dans leurs composants : une saveur concernait la logique **UI** telle que l'affichage et le masquage des choses. Et l'autre était tout sur la logique **données**, comme le chargement des données depuis votre serveur.

Cela a conduit à la distinction entre les composants **conteneurs** et **présentationnels** (également parfois appelés composants "**intelligents**" et "**bêtes**"). Les composants conteneurs doivent gérer vos données, mais — et c'est la partie importante — **pas votre UI**. Les composants présentationnels sont exactement l'inverse.

![Image](https://cdn-media-1.freecodecamp.org/images/ahdkD3vH6YSgcmtM05m8cN44Ld6t2xjVrnIS)
_Résultat de l'image Google pour "smart component". Je n'ai aucune idée de ce que c'est. [Crédit image](http://blog.fea-tc.com/2014/03/smart-mates-solidworks-2013-vs-solidworks-2014.html" rel="noopener" target="_blank" title=")_

En d'autres termes, dans l'exemple classique de la liste de tâches, un composant chargera les données, puis transmettra ces données à un _autre_ composant qui sera responsable de la sortie du balisage HTML réel et de la gestion des changements d'état locaux.

Cela est très similaire au modèle vue/contrôleur que vous connaissez peut-être de vos jours de développeur back-end. (_Vous souvenez-vous de Rails ? Vous souvenez-vous de Django ?_)

La distinction conteneur/présentationnel a été popularisée dans [cet article de blog de Dan Abramov](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0#.o74col49d) (le créateur de Redux), et je recommande de le consulter si vous souhaitez approfondir.

### Composants d'ordre supérieur

Avant de conclure, nous devons parler un peu d'un type de composants conteneurs appelés **composants d'ordre supérieur** (souvent abrégés en HoCs).

Un HoC est un composant que vous pouvez **envelopper autour** d'un autre composant pour lui passer des props spéciales, et il est généralement créé en utilisant une **fonction d'usine de composants d'ordre supérieur**. Notez que les gens se réfèrent couramment à la _fonction_ elle-même comme un "[HoC](https://github.com/ReactTraining/react-router/blob/master/upgrade-guides/v2.4.0.md#withrouter-hoc-higher-order-component)", ce qui n'est peut-être pas techniquement correct à 100%, mais ce n'est pas un gros problème en pratique.

Par exemple, appeler la fonction d'usine `withRouter` de React Router sur `<MyComponent>` l'enveloppera dans un nouveau composant `<withRouter(MyComponent)/>` qui passe la prop Router au composant `<MyComponent>` mentionné précédemment.

Vous pouvez penser à une fonction HoC comme à un caddie de golf qui suit son golfeur et lui tend le club dont il a besoin. Par eux-mêmes, le caddie ne peut pas vraiment _faire_ quoi que ce soit avec les clubs de golf. Ils sont juste là pour donner au golfeur l'accès à plus d'outils.

![Image](https://cdn-media-1.freecodecamp.org/images/-F5dRmBJk1jinhRCAzJuTu9v6nJ87uarUA9T)
_Passe-moi la prop Router, James !_

Les HoCs sont un concept très puissant. Par exemple, la bibliothèque [Recompose](https://github.com/acdlite/recompose/) vous permet même de gérer les changements d'état via des HoCs. En d'autres termes, vous pouvez maintenant gérer l'état sans avoir à impliquer de composants basés sur des classes ES6.

Avec la composition HoC devenant si courante, il semble que React pourrait s'éloigner de la syntaxe des classes ES6 et se diriger vers une approche purement fonctionnelle. Des temps intéressants !

### Récapitulatif

Alors, récapitulons ce que nous venons d'apprendre :

* Une base de code React est composée de composants.
* Ces composants sont écrits en utilisant JSX.
* Les données circulent des parents aux enfants, sauf en ce qui concerne l'`état`, qui provient de l'intérieur d'un composant.
* Les composants possèdent un petit ensemble de méthodes de cycle de vie et d'utilitaires.
* Les composants peuvent également être écrits sous forme de fonctions pures.
* Vous devez garder la logique des données et la logique de l'UI dans des composants séparés.
* Les composants d'ordre supérieur sont un modèle courant pour donner à un composant l'accès à de nouveaux outils.

Croyez-le ou non, nous venons de couvrir 90% des connaissances utilisées par un développeur React au quotidien. Peu importe à quel point le modèle est abstrait ou obscur, tout dans React peut toujours être réduit à des fonctions et des props.

Une fois que vous comprendrez vraiment cela, React cessera d'être effrayant. Vous serez en mesure de voir des modèles dans le code, de comprendre de nouvelles bases de code en un coup d'œil, et ce n'est qu'alors que vous pourrez proclamer fièrement :

Pfff ! React est _tellement_ 2015 !

### Aller plus loin

Si j'ai réussi à vous convaincre que React n'est pas si mal, vous pourriez vouloir essayer de l'apprendre correctement. Si c'est le cas, je ne peux que trop recommander le cours vidéo [React for Beginners](https://reactforbeginners.com/friend/STATEOFJS). C'est ainsi que j'ai appris React moi-même, et il vient d'être mis à jour pour couvrir toutes les nouvelles fonctionnalités cool comme les composants fonctionnels sans état :

![Image](https://cdn-media-1.freecodecamp.org/images/CVkcLHsnqJZ5LnZRS9sQsNZtbB6hx3NjdJga)
_Ne vous laissez pas tromper par le choix de l'arrière-plan "artistique" : c'est du matériel de haute qualité_

Si vous ne voulez pas que vos dollars durement gagnés financent le lobby néfaste de React (j'ai entendu dire que Dan Abramov en était à son troisième yacht), vous pouvez également apprendre gratuitement en consultant [cette énorme liste de ressources React](https://github.com/markerikson/react-redux-links).

Et si vous devez mettre en pratique toutes ces nouvelles connaissances en contribuant à un projet open-source React cool, consultez [Telescope Nova](https://github.com/TelescopeJS/Telescope/tree/devel). C'est le moyen le plus simple de créer rapidement une application full-stack React + GraphQL, complète avec des comptes utilisateurs, des formulaires et le chargement de données dès la sortie de la boîte. Et ai-je mentionné que nous cherchons des contributeurs ?

Enfin, si vous avez aimé cet article, veuillez le partager et le recommander (ce petit cœur vert juste en dessous). Et s'il vous plaît [faites-moi savoir sur Twitter](http://twitter.com/sachagreif) ce que vous aimeriez que j'écrive ensuite !