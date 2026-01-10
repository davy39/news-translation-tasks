---
title: Un guide complet pour les débutants sur React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-04T20:03:10.000Z'
originalURL: https://freecodecamp.org/news/a-complete-beginners-guide-to-react-4d490abc349c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tnOVr25yQ2GPzKfpglcxCQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Un guide complet pour les débutants sur React
seo_desc: 'By Ali Spittel

  I want to get back into writing more technical content. React is one of my favorite
  technologies, so I thought I would create a React intro! This post requires knowledge
  of HTML and JavaScript. I am of the firm opinion that you should ...'
---

Par Ali Spittel

Je veux me remettre à écrire plus de contenu technique. React est l'une de mes technologies préférées, alors j'ai pensé créer une introduction à React ! Cet article nécessite des connaissances en HTML et JavaScript. Je suis fermement convaincue que vous devriez connaître ces technologies avant de passer à des bibliothèques comme React !

### Qu'est-ce que React

React est une bibliothèque JavaScript créée en 2013 par l'équipe de développement de Facebook. React voulait rendre les interfaces utilisateur plus modulaires (ou réutilisables) et plus faciles à maintenir. Selon le site web de React, il est utilisé pour "Créer des composants encapsulés qui gèrent leur propre état, puis les composer pour créer des interfaces utilisateur complexes".

Je vais utiliser beaucoup d'exemples de Facebook tout au long de cet article puisque ce sont eux qui ont écrit React en premier lieu !

Vous vous souvenez quand Facebook est passé des likes aux réactions ? Au lieu de pouvoir aimer les publications, vous pouvez maintenant réagir avec un cœur, ou un smiley, ou un like à n'importe quelle publication. Si ces réactions étaient principalement faites en HTML, ce serait un travail énorme de changer tous ces likes en réactions et de s'assurer qu'ils fonctionnent.

C'est là que React intervient. Au lieu de mettre en œuvre la "séparation des préoccupations", nous avons une architecture différente dans React. Cette architecture augmente la modularité basée sur la structure d'un composant.

> _Aujourd'hui, nous garderons le CSS séparé, mais vous pouvez même le rendre spécifique au composant si vous le souhaitez !_

### React vs. JavaScript Vanilla

Lorsque nous parlons de JavaScript "vanilla", nous parlons généralement de l'écriture de code JavaScript qui n'utilise pas de bibliothèques supplémentaires comme JQuery, React, Angular ou Vue. Si vous souhaitez en savoir plus sur ces technologies et ce qu'est un framework, j'ai un [article](https://zen-of-programming.com/web-framework-intro) entièrement consacré aux frameworks web.

### Quelques notes rapides avant de commencer

* Pour rendre ce tutoriel un peu plus concis, certains exemples de code ont `...` avant ou après eux. Cela signifie que nous avons omis du code.
* J'utilise des diffs Git à certains endroits pour montrer les lignes de code qui vont changer. Si vous copiez et collez, vous devez supprimer le `+` au début de la ligne.
* J'ai des CodePens complets avec les versions complètes de chaque section — vous pouvez les utiliser pour rattraper votre retard !
* Les concepts plus avancés qui ne sont pas essentiels pour le tutoriel sont dans des citations. Ce sont des faits intéressants !

### Installation

Si vous créez une application React de production, vous voudrez utiliser un outil de construction comme Webpack. Webpack regroupera votre code puisque React utilise certains motifs qui ne fonctionneront pas par défaut dans le navigateur. [Create React App](https://github.com/facebook/create-react-app) est très utile à ces fins puisqu'il fait la plupart de la configuration pour vous !

Pour l'instant, nous utiliserons le CDN React, qui est uniquement à des fins de développement ! Nous utiliserons également le CDN Babel afin de pouvoir utiliser certaines fonctionnalités JavaScript non standard (nous en parlerons plus tard !).

```
<script crossorigin src="https://unpkg.com/react@16/umd/react.development.js"></script>
```

```
<script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
```

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/6.1.19/browser.js">
```

J'ai également créé un [modèle Codepen](https://codepen.io/aspittel/pen/gdrexE) que vous pouvez utiliser !

Dans un projet React complet, je diviserais mes composants en différents fichiers. À des fins d'apprentissage, nous combinerons notre JavaScript en un seul fichier pour l'instant.

### Composants

Pour ce tutoriel, nous allons construire un widget de statut Facebook, puisque Facebook a écrit React en premier lieu !

Pensez à combien de fois le widget `like` apparaît sur Facebook. Vous pouvez aimer un statut, ou un lien, ou une vidéo, ou une photo ! Ou même une page ! Chaque fois que Facebook modifie quelque chose dans la fonctionnalité des likes, ils ne veulent pas avoir à le faire dans tous ces endroits. C'est là que les composants entrent en jeu ! Toutes les pièces réutilisables d'une page web sont abstraites dans un composant. Ce composant peut être utilisé encore et encore. Nous n'aurons qu'à changer le code à un seul endroit pour le mettre à jour.

Regardons une image d'un statut Facebook et décomposons les différents composants qui le composent.

![Image](https://cdn-media-1.freecodecamp.org/images/0*iodL_qOvw1lqk2Yp.png)

Le statut lui-même sera un composant. Il y a beaucoup de statuts dans une timeline Facebook. Nous voulons définitivement pouvoir réutiliser le composant de statut.

Dans ce composant, nous aurons des _sous-composants_ ou des composants dans un composant parent. Ceux-ci seront également réutilisables. Nous pourrions avoir le composant de bouton like comme enfant du composant `PhotoStatus` et du composant `LinkStatus`.

Peut-être que nos sous-composants ressembleraient à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*MK4hJnEE7b9O4gmQ.png)

Nous pouvons même avoir des sous-composants dans des sous-composants ! Donc, le groupe de like, commentaire et partage pourrait être son propre composant `ActionBar`. Il aurait des composants pour aimer, commenter et partager à l'intérieur !

![Image](https://cdn-media-1.freecodecamp.org/images/0*7wv2ExT3ihc9IEhr.png)

Il y a plusieurs façons de décomposer ces composants et sous-composants en fonction de l'endroit où vous réutiliserez la fonctionnalité dans votre application.

### Premiers pas

Je voulais commencer ce tutoriel avec un "Hello World" React — c'est la tradition après tout ! Ensuite, nous passerons à l'exemple de statut légèrement plus complexe.

Dans notre fichier HTML, ajoutons juste un élément — une `div` avec un identifiant. Par convention, vous verrez normalement que cette div a un identifiant "root" puisque ce sera la racine de notre application React !

Si vous écrivez le code dans le [modèle CodePen](https://codepen.io/aspittel/pen/gdrexE?editors=0010), vous pouvez écrire ce JavaScript directement dans la section `js`. Si vous écrivez cela sur votre ordinateur, vous devrez ajouter une balise de script avec le type `text/jsx`, donc :

```
<script type="text/jsx"><;/script>
```

Maintenant, passons à notre code React !

```
class HelloWorld extends React.Component {
```

```
  render() {
```

```
    // Indique à React quel code HTML rendre
```

```
    return <h1>Hello World</h1>
```

```
  }}
```

```
// Indique à React d'attacher le composant HelloWorld à la div HTML 'root'
```

```
ReactDOM.render(<HelloWorld />, document.getElementById("root"))
```

Tout ce qui se passe, c'est que "Hello World" est affiché en tant que H1 sur la page !

Passons en revue ce qui se passe ici.

Tout d'abord, nous utilisons une classe ES6 qui hérite de la classe `React.Component`. C'est un motif que nous utiliserons pour la plupart de nos composants React.

Ensuite, nous avons une méthode dans notre classe — et c'est une méthode spéciale appelée `render`. React recherche la méthode `render` pour décider quoi rendre sur la page ! Le nom a du sens. Tout ce qui est retourné par cette méthode `render` sera rendu par ce composant.

Dans ce cas, nous retournons un H1 avec le texte "Hello World" — c'est exactement ce qui serait dans le fichier HTML normalement.

Enfin, nous avons :

```
ReactDOM.render(<HelloWorld />, document.getElementById("root"))
```

Nous utilisons la fonctionnalité ReactDOM pour attacher notre composant react au DOM.

> _React utilise quelque chose appelé le DOM virtuel qui est une représentation virtuelle du DOM avec lequel vous interagiriez normalement en JavaScript Vanilla ou JQuery. Ce `reactDOM.render` rend ce DOM virtuel au DOM réel. En coulisses, React fait beaucoup de travail pour éditer et re-rendre efficacement le DOM lorsque quelque chose sur l'interface doit changer._

Notre composant, `<HelloWorld />`, ressemble à une balise HTML ! Cette syntaxe fait partie de JSX qui est une extension de JavaScript. Vous ne pouvez pas l'utiliser nativement dans le navigateur. Vous vous souvenez que nous utilisons Babel pour notre JavaScript ? Babel transpilera (ou convertira) notre JSX en JavaScript régulier afin que le navigateur puisse le comprendre.

> _JSX est en fait optionnel dans React, mais vous le verrez utilisé dans la grande majorité des cas !_

Ensuite, nous utilisons le `document.getElementById` intégré de JavaScript pour récupérer notre élément racine que nous avons créé dans notre HTML.

En résumé, dans cette instruction `ReactDOM.render`, nous attachons notre composant `HelloWorld` à notre `div` que nous avons créé dans notre fichier HTML.

### Code de démarrage

D'accord — maintenant que nous avons fait un « Hello World », nous pouvons commencer avec notre composant Facebook.

Tout d'abord, je veux que vous jouiez avec cette démonstration. Nous travaillerons dessus tout au long du reste du tutoriel. N'hésitez pas à regarder le code aussi, mais ne vous inquiétez pas de ne pas le comprendre ! C'est à cela que sert le reste du tutoriel !

Commençons par « coder en dur » le HTML pour le widget :

Avec un peu de CSS ajouté, cela ressemble à ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*iYUATDXs_LeCtVv9.png)

[Voici un Codepen avec le code de démarrage complet](https://codepen.io/aspittel/pen/KxzGdx).

Pour les besoins de ce tutoriel, nous allons créer quatre composants : un composant `Status` qui sera le parent, un composant `Like` qui englobera la logique des likes, et le composant `Comment` qui contiendra la logique pour taper un commentaire. Le composant `Like` aura également un enfant `LikeIcon` qui apparaîtra ou sera masqué lorsque vous basculerez le bouton like.

### Architecture des composants

Divisons le code HTML que nous avons écrit en ces composants.

Nous commencerons avec la coque d'un composant, et nous le rendrons également pour nous assurer qu'il fonctionne !

> _Une note intéressante concernant ce qui précède, c'est que nous avons dû changer les attributs « class » en « className ». Class signifie déjà quelque chose en JavaScript — c'est pour les classes ES6 ! Certains attributs sont nommés différemment en JSX qu'en HTML._

Nous pouvons également supprimer le contenu de notre HTML, ne laissant qu'un élément avec l'ID root — le parent « content » div est juste pour le style !

```
<body>   <div class="content">     <div id="root"></div>   </div> </body>
```

Voici le HTML qui va aller dans le composant Status. Remarquez, une partie du HTML original n'est pas encore là — elle ira dans nos sous-composants à la place !

Créons un deuxième composant, puis nous l'inclurons dans notre composant `Status`.

```
class Comment extends React.Component {   render() {     return (       <div>         <textarea className="form-control" placeholder="Écrire un commentaire..." />          <small>{this.props.maxLetters} Restant</small>       </div>       )    } }
```

Voici le composant pour notre commentaire. Il contient notre `textarea` pour taper, et le texte avec le nombre de caractères restants. Remarquez que les deux sont enveloppés dans une `div`. Cela est dû au fait que React nous oblige à envelopper tout le contenu d'un composant dans une seule balise HTML. Si nous n'avions pas la `div` parente, nous retournerions une `textarea` et une balise `small`.

Nous devons donc inclure ce composant dans notre composant `Status` puisqu'il sera notre sous-composant. Nous pouvons le faire en utilisant cette même syntaxe JSX que nous avons utilisée pour rendre le composant Status !

D'accord, maintenant nous devons faire la même chose pour nos likes :

Ensuite, nous devons l'inclure dans notre composant `Status` original :

Super, maintenant nous avons « React-ifié » notre HTML original, mais il ne fait toujours rien. Commençons à corriger cela !

En résumé, le code de cette section ressemblera à [ce CodePen](https://codepen.io/aspittel/pen/yxOQMe?editors=0010).

### État et Props

Nous avons deux interactions utilisateur différentes que nous voulons implémenter :

* Nous voulons que l'icône de like apparaisse uniquement si le bouton like est pressé
* Nous voulons que le nombre de caractères restants diminue à mesure que la personne tape

Commençons à travailler sur ces points !

### Props

Imaginez que nous voulons que notre boîte de commentaire permette un nombre différent de lettres à différents endroits. Sur un statut, par exemple, nous voulons qu'un utilisateur puisse écrire une réponse de 200 lettres. Sur une photo, cependant, nous voulons seulement qu'il puisse écrire une réponse de 100 caractères.

React nous permet de passer des props (abréviation de propriétés) du composant `PictureStatus` et du composant `Status` pour spécifier combien de lettres nous voulons permettre dans notre réponse, plutôt que d'avoir deux composants de commentaire différents.

La syntaxe des props ressemble à ce qui suit :

```
<Comment maxLetters={20} /> <Comment text='hello world' /> <Comment show={false} /> 
```

```
let test = 'hello world' <Comment text={test} />
```

Les props ressemblent à des attributs HTML. Si vous passez une chaîne de caractères via des props, vous n'avez pas besoin des crochets. Tout autre type de données ou une variable doit être dans les crochets.

Ensuite, dans notre composant, nous pouvons utiliser nos props :

```
console.log(this.props.maxLetters)
```

Ils sont regroupés dans l'attribut `props` de l'instance afin qu'ils puissent être accessibles avec `this.props.myPropName`.

Alors, changeons la limite de 140 caractères codée en dur pour qu'elle soit modifiable à l'extérieur du composant !

Tout d'abord, nous allons changer l'endroit où nous instancions le composant Comment dans le composant Status (notez que certains codes sont omis) :

```
class Status extends React.Component {   ...       <div className="card-footer text-muted">         <Comment maxLetters={280} />       </div>      </div>;    </div>   )  } }
```

Ensuite, nous allons changer la limite de 140 caractères codée en dur dans le composant Comment.

```
class Comment extends React.Component {   ...     <div>      <textarea className="form-control" placeholder="Écrire un commentaire..." />     <small>{this.props.maxLetters} Restant</small>;     </div>    ... }
```

### État

Les props que nous passons d'un composant à l'autre ne changeront jamais dans le composant enfant. Elles peuvent changer dans le parent mais pas dans l'enfant. Mais — souvent, nous aurons des attributs que nous voudrons changer au cours de la vie d'un composant.

Par exemple, nous voulons garder une trace du nombre de caractères que l'utilisateur a tapés dans la zone de texte, et nous voulons garder une trace de savoir si le statut a été « liké » ou non. Nous stockerons ces attributs que nous voulons changer dans le composant dans son état.

> _Vous remarquerez beaucoup d'immuabilité dans React — il est fortement influencé par le paradigme fonctionnel, donc les effets secondaires sont également découragés._

Nous voulons que cet état soit créé chaque fois que nous créons une nouvelle instance d'un composant, donc nous utiliserons le constructeur de classe ES6 pour le créer. Si vous voulez une petite révision sur les classes ES6, [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) est une excellente ressource !

L'état va être un objet avec toutes les paires clé-valeur que nous voulons inclure. Dans ce cas, nous voulons un compteur de caractères du nombre de caractères que l'utilisateur a tapés. Nous allons le définir à zéro pour l'instant :

```
class Comment extends React.Component {     constructor () {       super()       this.state = { characterCount: 0 }     } ...
```

Maintenant, soustrayons cela de la prop `maxLetters`, afin que nous sachions toujours combien de caractères nous avons restants :

```
<small>{this.props.maxLetters - this.state.characterCount} Restant</small>
```

Si vous augmentez le `characterCount`, l'affichage des caractères restants diminue.

Mais — rien ne se passe lorsque vous tapez ! Nous ne changeons jamais la valeur de `characterCount`. Nous devons ajouter un gestionnaire d'événements à la `textarea` afin de changer le `characterCount` lorsque l'utilisateur tape.

### Gestionnaires d'événements

Lorsque vous avez écrit du JavaScript par le passé, vous avez probablement écrit des gestionnaires d'événements pour interagir avec les entrées de l'utilisateur. Nous allons faire de même dans React, la syntaxe va être un peu différente.

Nous allons ajouter un gestionnaire `onChange` à notre `textarea`. À l'intérieur, nous placerons une référence à une méthode de gestion d'événements qui s'exécutera chaque fois que l'utilisateur tape dans la `textarea`.

```
<textarea className="form-control" placeholder="Écrire un commentaire..." onChange={this.handleChange}/>
```

Maintenant, nous devons créer une méthode `handleChange` !

```
class Comment extends React.Component {     constructor () {      super()      this.state = { characterCount: 0 }     }         handleChange (event) {       console.log(event.target.value)     } ...
```

Pour l'instant, nous faisons simplement un `console.log` de `event.target.value`. Cela fonctionnera de la même manière que dans le JavaScript sans React (bien que si vous creusez un peu plus, l'objet événement est un peu différent). Si vous regardez cette console, nous imprimons ce que nous tapons dans la zone de texte.

Maintenant, nous devons mettre à jour l'attribut `characterCount` dans l'état. Dans React, nous ne modifions jamais directement l'état, donc nous ne pouvons pas faire quelque chose comme ceci : `this.state.characterCount = event.target.value.length`. Nous devons plutôt utiliser la méthode `this.setState`.

```
handleChange (event) {    this.setState({ characterCount: event.target.value.length }) }
```

Mais ! Vous obtenez une erreur — « Uncaught TypeError: this.setState is not a function ». Cette erreur nous indique que nous devons préserver le contexte de la classe ES6 dans le gestionnaire d'événements. Nous pouvons faire cela en liant `this` à la méthode dans le constructeur ! Si vous voulez en savoir plus à ce sujet, [voici un bon article](https://medium.freecodecamp.org/this-is-why-we-need-to-bind-event-handlers-in-class-components-in-react-f7ea1a6f93eb).

```
class Comment extends React.Component {    constructor () {      super() this.handleChange = this.handleChange.bind(this) ...
```

D'accord ! Nous y sommes presque. Nous devons simplement ajouter la possibilité de basculer l'affichage du `like`.

Nous devons ajouter un constructeur à notre composant `Like`. Dans ce constructeur, nous devons instancier l'état du composant. La chose qui changera au cours du cycle de vie du composant est de savoir si le statut a été liké ou non.

```
class Like extends React.Component {     constructor() {       super()       this.state = { liked: false }      } ...
```

Maintenant, nous devons ajouter un gestionnaire d'événements pour changer si le statut a été liké ou non :

```
class Like extends React.Component {   constructor() {     super()     this.state = { liked: false }    this.toggleLike = this.toggleLike.bind(this)    } 
```

```
  toggleLike () {     this.setState(previousState => ({ liked: !previousState.liked    }))    } ...
```

La différence ici est que la fonction de rappel `this.setState` reçoit un paramètre -- `previousState`. Comme vous pouvez probablement le deviner à partir du nom du paramètre, il s'agit de la valeur de l'état avant que `this.setState` soit appelé. `setState` est asynchrone, donc nous ne pouvons pas dépendre de l'utilisation de `this.state.liked` à l'intérieur.

Maintenant, nous devons :

a) appeler le gestionnaire d'événements chaque fois que l'utilisateur clique sur le bouton like

b) n'afficher le LikeIcon que lorsque `liked` est vrai

Super ! Maintenant, toute notre fonctionnalité est en place !

### Bonus : Composants fonctionnels

Si vous avez l'impression d'être déjà dépassé, n'hésitez pas à sauter cette partie. Je voulais faire une autre refactorisation rapide de ce projet. Si nous créons des composants qui n'ont pas d'état associé (que nous appelons des composants sans état), nous pouvons transformer nos composants en fonctions au lieu de classes ES6.

Dans ce cas, notre `LikeIcon` pourrait ressembler à ceci :

Nous retournons simplement l'UI du composant au lieu d'utiliser la méthode `render` !

[Voici](https://codepen.io/aspittel/pen/NLrPWN) un CodePen qui implémente cette refactorisation.

### Aide-mémoire

J'adore les aides-mémoire, alors j'en ai fait un avec le contenu de cet article :

![Image](https://cdn-media-1.freecodecamp.org/images/0*jH9Vm3B7WVGr09-6.png)

Vous pouvez également le télécharger en PDF [ici](https://zen-of-programming.com/react-intro/cheatsheet.pdf) !

### Prochaines étapes

Pour résumer, nous avons parlé de l'architecture des composants, de la syntaxe de base de React et de JSX, de l'état et des props, des gestionnaires d'événements et des composants fonctionnels.

Si vous souhaitez voir tous les CodePens de ce tutoriel, [voici](https://codepen.io/collection/XpPbVv/) une collection.

Si vous souhaitez essayer d'étendre le code de ce tutoriel, je vous recommande de changer les likes en réactions ou de créer un composant photo qui réutilise certains des composants que nous avons créés !

De plus, voici quelques autres endroits géniaux pour apprendre React :

* [Documentation React](https://facebook.github.io/react/tutorial/tutorial.html)
* [DevCoffee](https://www.youtube.com/watch?v=ZnRFerIP8aA)
* [Wes Bos Redux](https://www.youtube.com/watch?v=hmwBow1PUuo&list=PLu8EoSxDXHP5uyzEWxdlr9WQTJJIzr6jy)

### Restez en contact

Si vous avez aimé cet article et souhaitez en lire plus, j'ai une [newsletter hebdomadaire](https://tinyletter.com/ali_writes_code) avec mes liens préférés de la semaine et mes derniers articles. De plus, [tweetez-moi](https://twitter.com/aspittel) sur les choses que vous voulez que j'écrive des tutoriels, ou des commentaires constructifs sur la façon dont je pourrais rendre ceux-ci plus faciles à suivre ! Si vous avez des questions, mon [dépôt AMA](https://github.com/aspittel/ama) est le meilleur endroit pour me joindre !

_Publié à l'origine sur [zen-of-programming.com](https://zen-of-programming.com/beginners-guide-react).