---
title: Un guide pour débutants pour commencer avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-20T17:29:31.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-getting-started-with-react-c7f34354279e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h8d-4wYLN9wwiEsLAA_5yg.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Un guide pour débutants pour commencer avec React
seo_desc: 'By Ankita Masand

  In this tutorial, I’ll first help you understand why Facebook felt the need to build
  a library called React. I’ll cover all the basic concepts that you’d need to create
  your first React app. This tutorial aims to explain React by cle...'
---

Par Ankita Masand

Dans ce tutoriel, je vais d'abord vous aider à comprendre pourquoi Facebook a ressenti le besoin de créer une bibliothèque appelée _React_. Je vais couvrir tous les concepts de base dont vous aurez besoin pour créer votre première application React. Ce tutoriel vise à expliquer React en expliquant clairement ses fondamentaux comme _l'utilisation de JSX et ES6, la construction de composants avec état et sans état, les éléments React, le DOM virtuel et l'algorithme de différenciation_.

![Image](https://cdn-media-1.freecodecamp.org/images/NsBhsN56E38anPtJhwdA44UQQg8RKAgKktfM)
_Crédits : [https://matwrites.com](https://matwrites.com" rel="noopener" target="_blank" title=")_

Le web a évolué d'un simple ensemble de pages HTML statiques à des applications fiables, interactives et performantes. Avec l'avènement d'AJAX, nous pouvons charger de manière asynchrone l'ensemble de l'application en parties.

Chaque fois qu'il y a un changement dans une partie de l'application dû à des mises à jour en temps réel ou à une entrée utilisateur, cette partie seulement est chargée de manière asynchrone pour refléter l'état mis à jour. Cela signifie que seul le conteneur correspondant du Document Object Model ([DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)) doit être mis à jour pour refléter les changements auprès du client.

Par exemple, considérons la section des commentaires sur Facebook. Les données des commentaires récupérées lors du chargement initial sont ajoutées au DOM. Maintenant, lorsque vous ajoutez un nouveau commentaire, il fait une requête asynchrone au serveur pour sauvegarder ce commentaire dans la base de données, et met à jour le DOM pour refléter l'état actuel.

Entrons dans les détails de cet exemple et comprenons comment cela fonctionnerait. Supposons que j'ai 20 commentaires dans mon tableau de commentaires. Le tableau de commentaires est la source de vérité, et il reflète l'état actuel à tout moment. Lorsque l'utilisateur ajoute un nouveau commentaire, nous devons modifier ce tableau de commentaires une fois que le nouveau commentaire a été ajouté avec succès à la base de données. Le tableau de commentaires contient maintenant 21 commentaires.

Oh oui, nous devons également écrire du code pour mettre à jour le DOM afin de refléter l'état actuel (supposons que nous utilisons Vanilla JavaScript ou jQuery ici. Des trucs sympas arrivent ensuite !). Cela signifie que le conteneur DOM des commentaires est abonné au tableau des commentaires. Il doit être modifié lorsqu'il y a un changement dans le tableau des commentaires. Nous pouvons dire en toute sécurité que le tableau des commentaires est le modèle ici, et le conteneur des commentaires est la vue.

Ajoutons quelque chose de plus à cela — des centaines d'éléments div sont abonnés à ce modèle de commentaires, ce qui signifie que nous devons écrire du code pour mettre à jour chacun de ces éléments `div`.

```
function updateCommentsSubscriber (response) {    commentsArr = [ ...response ] // commentsArr = ['Commentaire 1', 'Commentaire 2', ...]    var firstDiv = document.getElementById('first')    firstDiv.innerHTML = commentsArr.length    var secondDiv = document.getElementById('second')    secondDiv.innerHTML = commentsArr.toString()    ...}
```

Soupir ! Imaginez si cela se produisait à l'échelle à laquelle Facebook opère. Chaque fois que nous avons un nouvel élément qui est abonné à ce modèle, nous devrions écrire du code pour apporter des modifications à cet élément. Cette approche n'est pas évolutive.

Facebook a traité le problème de l'évolutivité et de la lenteur du DOM en créant une bibliothèque appelée **React**. React a été déployé pour la première fois sur la section _Fil d'actualité_ de Facebook en 2011, puis sur Instagram en 2012. Il a été open-sourcé en 2013 et a été applaudi par la communauté mondiale depuis.

Dans ce tutoriel, nous allons nous appuyer sur les fondamentaux de React. À la fin de ce tutoriel, vous devriez être en mesure d'écrire votre première application React.

### Table des matières

1. Introduction à React
2. JSX
3. ES6
4. Éléments React
5. Composants
6. État et Props
7. Composants sans état
8. Méthodes de cycle de vie
9. DOM virtuel
10. Création de votre première application React avec create-react-app

Bien que je suggère une plongée approfondie dans chacun de ces sujets, n'hésitez pas à en sauter si vous êtes déjà confiant à ce sujet.

### Introduction à React

**React est une bibliothèque JavaScript utilisée pour construire des interfaces utilisateur**. Elle résout le problème d'évolutivité mentionné précédemment en mettant à jour efficacement le DOM.

Une façon de mettre à jour le DOM est de mettre manuellement les valeurs dans les nœuds DOM respectifs, ce qui est évidemment lent et non évolutif.

Angular résout ce problème en utilisant la _liaison de données_. Il lie les variables utilisées dans la vue avec leurs homologues respectifs dans le modèle. Il met automatiquement à jour toutes les instances d'une variable dans une vue lorsque sa valeur respective dans un modèle change.

D'autre part, React propose une approche différente pour résoudre ce problème. Il utilise une technique appelée _Réconciliation_ pour évaluer la différence dans la représentation du DOM à deux moments différents. Il ne met à jour que la partie qui est modifiée. Cela deviendra clair une fois que nous entrerons dans les détails de fonctionnement de React. Pour l'instant, considérons un exemple simple :

Cela va dans le HTML :

```
<div id='app'></div>
```

Mettez le code ci-dessous dans un fichier JavaScript :

```
class HelloReact extends React.Component {    render () {        return (            <div>Bonjour React !</div>        )    }}ReactDOM.render(<HelloReact>, document.getElementById('app'))
```

L'exemple ci-dessus imprimera `Bonjour React !` à l'écran. `HelloReact` est appelé un _composant_ dans React. La méthode `render` à l'intérieur de ce composant retourne la représentation DOM.

Ce n'est pas une coïncidence si j'ai écrit du HTML en JavaScript. `<div>Bonjour React !</div>` à l'intérieur de la méthode `render` est une syntaxe JSX. Elle nous permet d'écrire du HTML en JavaScript.

La dernière instruction fait le travail de rendu du composant `HelloReact` à l'intérieur de notre conteneur `app`. Dans les deux sections suivantes, nous allons approfondir JSX et ES6.

### JSX

Si nous n'avions pas JSX, vous devriez écrire le code JSX ci-dessus comme :

```
React.createElement("div", null, "Bonjour React !")
```

Cela peut compliquer les choses si vous devez traiter des éléments imbriqués.

Par exemple :

```
React.createElement("div", { className: "container" },    React.createElement("span", null, "Bonjour React !"),    React.createElement("span", null, "Je suis dans le composant HelloReact"))
```

Et voici la syntaxe JSX pour le code ci-dessus :

```
<div className='container'>    <span>Bonjour React !</span>    <span>Je suis dans le composant HelloReact</span></div>
```

Écrire du JSX à l'intérieur d'un composant React donne une idée claire de ce que le composant va rendre dans le DOM. Cela semble propre et intuitif.

Si vous êtes déjà convaincu d'utiliser JSX avec React, continuez à lire pour en savoir plus. Sinon, React vous permet de l'utiliser sans JSX. Vous pouvez en savoir plus à ce sujet [ici](https://reactjs.org/docs/react-without-jsx.html).

JSX est juste une extension JavaScript qui permet d'écrire du code de type HTML :

```
<div>Bonjour {name} !</div>
```

L'expression à l'intérieur des accolades sera évaluée à la valeur de la variable `name`. Vous pouvez même appeler des fonctions à l'intérieur de JSX :

```
<div>Bonjour, {formatName('james.gosling') !}</div>
```

Cela appellerait la fonction `formatName` et passerait `james.gosling` comme paramètre. Il rendra la valeur qui est retournée par la fonction `formatName`.

#### Instructions conditionnelles

Il est souvent nécessaire de rendre un nœud DOM uniquement lorsqu'une valeur particulière a été définie.

Cela peut être réalisé en utilisant JSX comme suit :

```
greetUser (userName) {    if (isUserLoggedIn) {        return <div>Bonjour, {userName} !</div>    }    return <div>Bonjour, Invité !</div>}
```

L'exemple ci-dessus saluera un utilisateur connecté avec son nom et en tant qu'_Invité_ lorsqu'un utilisateur n'est pas connecté.

Veuillez noter que ce rendu conditionnel n'est pas similaire au scénario d'affichage/masquage. En fonction de la valeur de la variable `isUserLoggedIn`, un seul des deux éléments sera rendu dans le DOM à la fois.

#### Rendu des nœuds enfants en utilisant la fonction map

Considérons notre exemple de commentaires ci-dessus. Ici, nous avons un tableau de commentaires, et nous devons rendre tous les commentaires dans un conteneur DOM.

`map` est une fonction JavaScript native utilisée pour itérer les éléments d'un tableau. Vous pouvez passer une fonction itérative personnalisée comme l'un de ses arguments. Chacun des éléments du tableau servirait d'entrée à cette fonction itérative. `map` produira un tableau basé sur les valeurs retournées lors de chaque itération.

`map` est utile lors de la création de composants React. Vous pouvez en savoir plus à ce sujet [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map).

```
renderComments (commentsArr) {    /* commentsArr ressemblerait à cette structure ci-dessous    commentsArr = [{        id: 1,        text: "Je suis un commentaire !"    }]    */    return (        <div class='comments-container'>            {                commentsArr.map (function (comment) {                   return <div key={comment.id}>{comment.text}</div>                })            }        </div>    )}
```

La méthode `renderComments` ci-dessus retournerait le résultat de la méthode `map`. Dans ce cas, `map` retourne un tableau de nœuds DOM.

Remarquez l'utilisation de `key` avec chaque élément `div`. Nous entrerons dans les détails de l'utilisation de `key` avec les éléments DOM plus tard. Pour l'instant, il est simplement utilisé comme un moyen d'identifier de manière unique les éléments DOM.

#### Compilation de JSX en JavaScript

La bibliothèque React ne comprend pas JSX. Il est simplement utilisé pour faciliter le travail du développeur. Donc, que fait React lorsqu'il rencontre cette syntaxe étrange de type _HTML_ dans le code JavaScript ?

JSX est transpilé en instructions JavaScript par le [plugin Babel](https://babeljs.io/docs/en/babel-plugin-transform-react-jsx) avant que React ne les rencontre. _La transpilation est le processus de conversion d'un langage source en un autre_. Donc, tout ce que React voit est de simples instructions JavaScript.

Le simple code JSX ci-dessus

```
<div class='heading'>Bonjour React !</div>
```

est transpilé en

```
React.createElement("div", { className: 'heading' }, "Bonjour React !")
```

La méthode `createElement` est définie sur React.

Le premier argument de la méthode `createElement` est le type du nœud DOM que vous souhaitez que React crée pour vous. Il peut s'agir de `div`, `span`, `p`, etc.

Le deuxième argument est utilisé pour spécifier les attributs du nœud DOM. Dans ce cas, nous disons à React que le `className` du nœud est `heading`.

Remarquez l'utilisation de `className` au lieu de l'attribut conventionnel `class`. Dans React, l'attribut `class` est spécifié comme `className` pour éviter les conflits avec les attributs existants.

Le troisième argument contient des informations sur les enfants du nœud DOM. Dans ce cas, il s'agit simplement de texte brut qui sera ajouté comme `innerHTML` au nœud DOM.

La méthode `createElement` est analogue à la méthode `document.createElement` en JavaScript, mais elle produit un élément React. Nous entrerons dans les détails des éléments React plus tard.

### ES6

ES6 est l'abréviation de ECMAScript 6 ou ECMAScript 2015. Dans cette partie, nous allons apprendre quelques techniques ES6 courantes qui facilitent le développement de composants React.

#### `let` et `const`

`let` est utilisé pour déclarer des variables au niveau du bloc, et `const` est utilisé pour déclarer des constantes. JavaScript suit une **portée au niveau de la fonction**.

Une variable déclarée à l'intérieur d'une fonction peut être utilisée dans toute la fonction, mais pas à l'extérieur.

Considérons un exemple qui nous aidera à comprendre la portée au niveau de la fonction :

```
function pokemon (id) { //id = 12    if (id === 12) {        var pokemonObj = {            id: 12,            name: 'butterfree',            height: 11,            weight: 22,            abilities: [                {                    name: 'tinted-lens'                }            ]        }    }    return pokemonObj    }
```

La méthode `pokemon` ci-dessus prend `id` comme paramètre, et retourne `pokemonObj` si `id` est égal à `12`. Allez-y et exécutez cette fonction dans la console de votre navigateur.

Si vous exécutez `pokemon(12)`, il imprime `pokemonObj` comme prévu. Cependant, si vous exécutez `pokemon(13)`, il n'affiche pas d'erreur, et imprime plutôt `undefined`.

Remarquez que `pokemonObj` est défini dans la structure `if`, ce qui signifie que si `id` n'est pas égal à 12, `pokemonObj` ne devrait pas être disponible dans le contexte de la fonction `pokemon`.

JavaScript suit la portée au niveau de la fonction, ce qui signifie qu'une variable déclarée dans une instruction à l'intérieur d'une fonction est disponible dans toute la fonction. Donc, `pokemonObj` est disponible même s'il est déclaré à l'intérieur du bloc `if`.

La construction `let` résout ce problème car elle nous permet de limiter la portée des variables au niveau du bloc.

Utilisez `let` pour déclarer `pokemonObj` et vérifiez les résultats :

```
function pokemon (id) { //id = 12    if (id === 12) {        let pokemonObj = {            id: 12,            name: 'butterfree',            height: 11,            weight: 22,            abilities: [                {                    name: 'tinted-lens'                }            ]        }    }    return pokemonObj    }
```

Vous obtiendrez `pokemonObj is not defined`, et cela justifie la portée au niveau du bloc des variables déclarées en utilisant la construction `let`.

Une variable déclarée en utilisant `const` ne peut pas être modifiée :

```
const POKEMON = 'butterfree' pokemon = 'pikachu'
```

La deuxième instruction ci-dessus affiche une erreur car il n'est pas autorisé de modifier les variables constantes.

#### Déstructuration d'objets

Considérons un objet, `berries`, qui sont de petits fruits qui peuvent fournir des points de vie et une restauration des conditions de statut, une amélioration des statistiques, et même une négation des dégâts lorsqu'ils sont mangés par les Pokémon :

```
var berries = {    id: 1,    name: 'cheri',    growth_time: '3',    max_harvest: 5,    natural_gift_power: 60,    size: 20,    smoothness: 25,    soil_dryness: 15,    natural_gift_type: {        name: 'fire',        url: 'https://pokeapi.co/api/v2/type/10/'    }}
```

Si j'ai besoin d'utiliser certaines des clés de l'objet ci-dessus, l'approche conventionnelle est :

```
var id = berries.idvar name = berries.namevar growthTime = berries.growth_time
```

Et avec ES6 :

```
let { id, name, growth_time, max_harvest, natural_gift_power, size } = berries
```

L'instruction ci-dessus crée des variables locales telles que `id`, `name`, `growth_time`, `max_harvest`, `natural_gift_power`, et `size`, et chacune d'elles aura la valeur correspondante dans l'objet `berries`. N'est-ce pas cool ?

Ici, nous déstructurons l'objet pour référencer des clés individuelles. Si l'une des clés n'était pas définie dans l'objet, sa valeur serait `undefined`.

#### Modélisation de chaînes

Voici l'ancienne façon de concaténer des chaînes en JavaScript :

```
var cheriDescription = "L'un des baies est " + name + ". Son temps de croissance est " + growth_time + ". Sa taille est " + size + ". Son maximum de récolte est " + max_harvest.
```

Et voici la façon ES6 :

```
let cheriDescription = `L'une des baies est ${name}. Son temps de croissance est ${growth_time}. Sa taille est ${size}. Son maximum de récolte est ${max_harvest}.`
```

Vous pouvez écrire la phrase entière entre backticks sans avoir à concaténer le texte statique et les variables en parties. Enveloppez les variables à l'intérieur de `'${}'`. Cela semble beaucoup plus propre.

#### Fonctions fléchées

Celle-ci est ma préférée. Voici l'ancienne façon d'écrire des fonctions en JavaScript :

```
function getBerrySize (berries) {    return berries.size}
```

Et voici la façon ES6 d'écrire des fonctions :

```
const getBerrySize = (berries) => berries.size
```

Les fonctions fléchées suivent cette syntaxe :

`déclaration` `nomFonction` = `(paramètresFonction)` =&g`t; retour res`ultat

La fonction `getBerrySize` ci-dessus retourne la taille de la baie. Remarquez que nous n'avons pas écrit le mot `return` dans la fonction fléchée ci-dessus. L'utilisation de `return` est facultative si le corps de la fonction fléchée n'a qu'une seule instruction et retourne cette instruction.

Si un corps de fonction a plus d'une instruction, enveloppez-les dans des accolades.

Les fonctions fléchées se comportent un peu différemment par rapport aux fonctions normales lorsqu'elles sont utilisées avec la construction `this`. En savoir plus sur `this` et comment les fonctions fléchées se comportent différemment lorsqu'elles sont utilisées avec `this` dans mon article [ici](https://hackernoon.com/lets-get-this-this-once-and-for-all-f59d76438d34).

#### Classes

Avec ES6, nous pouvons envelopper les fonctions pertinentes utilisées pour implémenter une fonctionnalité particulière à l'intérieur d'une classe.

Créons une classe pour évaluer les baies :

```
class Berries {    constructor (berries) {        this.berries = berries    }    getSize () {        return this.berries.size    }    getGrowthTime () {        return this.berries.growth_time    }}const cherries = new Berries(berries)cherries.getSize() // 20cherries.getGrowthTime() // 3
```

Nous avons enveloppé les méthodes pertinentes des baies à l'intérieur de la classe `Berries`.

L'instruction `const cherries = new Berries(berries)` instancie la classe Berries et crée un objet de type `Berries`.

L'entrée passée au constructeur Berries est l'objet `berries` que nous avons créé précédemment. Nous pouvons utiliser les méthodes définies dans la classe `Berries` sur cet objet.

Maintenant que nous avons appris la plupart des techniques ES6 courantes, nous pouvons les utiliser dans les sections suivantes.

### Éléments React

Les éléments React sont les plus petites unités qui représentent l'état du DOM à tout moment.

Le navigateur ne comprend pas React. Comme nous l'avons vu précédemment, JSX est converti en instructions JavaScript pour créer un nœud DOM.

Avec cette instruction :

```
React.createElement("div", { className: 'heading' }, "Bonjour React !")
```

Le nœud DOM `div` n'est pas encore ajouté au DOM. L'instruction ci-dessus est convertie en un objet JavaScript simple comme suit :

```
{    type: 'div',    props: {        className: 'heading',        children: 'Bonjour React !'    }}
```

Ces objets sont appelés **Éléments React**.

Ils contiennent deux clés importantes :

`type` spécifie le type du nœud DOM. Il peut s'agir de `div`, `span`, `p`, etc.

`props` décrit les propriétés de cet élément. Dans ce cas, nous avons `className` et `children`.

Les éléments imbriqués peuvent être spécifiés comme valeur de la clé `children`.

`ReactDOM` fait le travail de conversion de ces éléments React en nœuds DOM réels et les met également à jour en conséquence.

Les éléments React sont immuables et sont bon marché à créer. Si un élément React est modifié, son ancienne instance est détruite et une nouvelle est créée à partir de zéro.

Cependant, le nœud DOM correspondant n'est pas toujours détruit pour laisser place à un nouveau. Les opérations DOM sont coûteuses et doivent donc être évitées dans tous les cas possibles.

ReactDOM fait un excellent travail ici. Il crée de nouveaux éléments React car leur création est bon marché, cependant, il met efficacement à jour uniquement la partie du nœud DOM réel qui est modifiée.

React utilise un algorithme de _différenciation_ pour déterminer ce qui doit être mis à jour dans le DOM. Nous en apprendrons plus à ce sujet dans la section sur le DOM virtuel.

Passons en revue ce que nous avons appris jusqu'à présent :

* JSX est une syntaxe de type _HTML_ utilisée dans les composants React. Ce n'est qu'une représentation du nœud DOM et n'ajoute pas réellement d'éléments au DOM.
* Le plugin Babel le transpile en instructions JavaScript simples sous la forme `React.createElement`.
* Les instructions `React.createElement` sont ensuite converties en objets JavaScript.
* ReactDOM met efficacement à jour le DOM réel en utilisant les objets créés ci-dessus.

### Composants

Les composants sont des classes réutilisables qui définissent une fonctionnalité particulière. React suit une structure basée sur les _composants_. Chacun des composants que nous définissons dans React étend les fonctionnalités de base du composant natif React.

Créons un simple composant React pour le texte d'entrée :

```
class Text extends React.Component {    state = {        value: ''    }    onChange = (e) => {        this.setState({ value: e.target.value })    }    render () {        return (            <input                type='text'                onChange={this.onChange}                value={this.state.value}            />        )    }}export default Text
```

Chacun des composants React a une implémentation de la méthode `render`. Cette méthode retourne la représentation DOM pour ce composant. Dans notre cas, elle retourne un élément `input`. Rappelez-vous, cet élément `input` n'est pas réellement un nœud DOM. C'est juste une représentation DOM.

Les attributs — `text`, `onChange` et `value` qui sont passés à l'élément `input` sont appelés **props** dans React. `onChange` est un gestionnaire d'événements qui est appelé chaque fois que la valeur du texte dans la boîte d'entrée change. Les `props` dans React sont en lecture seule.

Les composants React maintiennent un état interne pour gérer la complexité basée sur divers paramètres. Au début de notre composant, nous avons initialisé un objet appelé `state`. Cette variable d'état gère l'état du composant Text. L'état peut être modifié en utilisant la méthode `setState`, comme montré dans la méthode `onChange` définie ci-dessus.

Le composant `Text` est une unité individuelle. Cela devient intéressant lorsque ces composants peuvent être directement utilisés dans d'autres composants compliqués. React suit un modèle basé sur la `Composition`, ce qui signifie importer des composants plus petits pour implémenter une fonctionnalité complexe. Il composite différents composants plus petits en un composant plus grand pour constituer une fonctionnalité opérationnelle.

Créons un composant de formulaires qui importerait le composant Text ci-dessus :

```
import Text from './text'class Forms extends React.Component {    state = {}    render () {        return (            <div>                <p>Formulaire pour les détails de base</p>                <Text />            </div>        )    }}
```

Tout d'abord, nous importons le composant Text. Remarquez comment le composant Text est inclus dans la méthode `render` du composant Forms.

Lorsque le composant Forms est rendu, le `<Text` /> est remplacé par la valeur de retour de la méthode `render` dans le composant Text.

### Plus sur `state` et `props`

Comme mentionné précédemment, React suit un modèle basé sur la Composition. Les composants plus grands peuvent personnaliser les composants à importer en envoyant des props pertinents.

Modifions la méthode `render` du composant Forms ci-dessus comme suit :

```
render () {    return (        <div>            <p>Formulaire pour les détails de base</p>            <Text                type='text'            />;        </div>    )}
```

Remarquez comment nous passons les props `type` dans le composant Text.

Nous devons apporter des modifications à notre composant Text pour accepter ces props.

Vérifiez les modifications dans la méthode `render` :

```
render () {    let { type } = this.props    return (        <input            type={type}            onChange={this.onChange}            value={this.state.value}        />    )}
```

Les `props` passés par le composant Forms sont disponibles sous forme d'objet dans le composant Text. Remarquez comment nous utilisons la propriété `type` dans le composant Text qui a été passée par le composant forms.

La variable d'état gère l'état interne d'un composant. Elle peut être modifiée en fonction des changements de réseau, des entrées de l'utilisateur ou de toute mise à jour planifiée.

`state` n'est rien d'autre qu'un objet JavaScript. Il peut être modifié en utilisant la méthode `setState`. La méthode `setState` prend un objet en entrée. Chaque fois qu'une valeur change dans un état, nous ne passons que cette valeur dans la méthode `setState` au lieu de passer l'objet d'état entier.

Supposons que nous avons notre composant Berries et que son état interne est l'objet `berries` que nous avons défini ci-dessus.

Si une modification se produit dans la propriété `growth_time` de l'objet `berries`, nous pouvons la mettre à jour dans l'état comme suit :

```
this.setState({ growth_time: new_growth_time })
```

Nous ne passons pas l'objet `berries` entier à la méthode `setState`. Nous ne passons que la valeur qui doit être mise à jour.

La méthode `setState` fonctionne comme une fonction asynchrone. Plusieurs appels de mise à jour d'état sont regroupés et invoqués ensemble à des intervalles ultérieurs pour traiter les problèmes de performance.

### Composants sans état

Les composants définis ci-dessus avaient leur propre état en place. Cependant, nous pouvons également définir des composants sans état.

Ces composants sont des fonctions pures. Ils ne modifient pas l'entrée qui leur est passée. Ce sont simplement des composants de représentation.

Voyons un exemple de composant sans état :

```
const getBerrySize = (props) => {    let { size } = props    return (        <p>{size}<;/p>    )}
```

Le seul travail de ce composant est de retourner une représentation DOM pour afficher la taille des baies.

### Cycle de vie des composants

Un composant React suit un certain modèle de cycle de vie. Il passe par quatre phases importantes :

1. Initialisation
2. Montage
3. Mise à jour
4. Démontage

Examinons certaines des méthodes qui sont invoquées pendant ces phases

**Initialisation**  
Initialiser l'état et les props.

**Montage**  
`componentWillMount` — cette méthode est invoquée juste avant le montage. Elle est appelée avant la méthode `render`. Pour définir l'état initial et les props, il est recommandé d'utiliser le `constructeur` à la place de cette méthode.

`render` — c'est la seule méthode requise dans un composant de classe. Elle retourne la représentation DOM à tout moment. Elle examine la valeur de `state` et `props`, et retourne la représentation DOM mise à jour.

`componentDidMount` — cette méthode est invoquée immédiatement après que le composant est monté. C'est un bon endroit pour instancier les requêtes réseau vers le serveur. Une fois les données chargées depuis le serveur, vous pouvez appeler la méthode `setState` pour invoquer `render` afin de mettre à jour les nœuds DOM.

**Mise à jour**  
`componentWillReceiveProps` — si un changement se produit dans `props`, cette méthode est appelée pour rendre l'état mis à jour. Il n'est pas recommandé d'utiliser cette méthode à partir de la version 16 de React.

`shouldComponentUpdate` — si cette méthode retourne `true`, la méthode `render` est appelée pour faire de la place pour l'état et les `props` mis à jour.

`componentWillUpdate` — cette méthode est appelée immédiatement avant que render ne commence à faire son travail.

`componentDidUpdate` — cette méthode est appelée une fois que l'état mis à jour est rendu dans le DOM.

**Démontage**  
`componentWillUnmount` — cette méthode est invoquée juste avant le démontage d'un composant. C'est un bon endroit pour supprimer les abonnements du composant.

Ceci est un aperçu bref du cycle de vie des composants React. J'expliquerai ces méthodes en détail dans mes futurs articles.

### DOM virtuel

J'ai mentionné le problème d'évolutivité plus tôt en introduisant React. Dans cette section, nous verrons comment React résout efficacement ce problème.

D'après ce que vous avez appris jusqu'à présent, il est clair que React ne met pas directement à jour le DOM réel. Tout ce que React sait, c'est que le DOM n'est rien d'autre qu'un objet JavaScript. Cet énorme objet JavaScript est appelé **DOM virtuel**.

Si un changement se produit dans la sortie de la méthode `render` dans l'un des composants, le DOM virtuel accommode ces changements en détruisant son ancienne instance et en créant une nouvelle.

Comme mentionné précédemment, React utilise une technique appelée _Réconciliation_ pour évaluer la différence entre le DOM réel et le DOM virtuel.

_La réconciliation est l'action de rendre une vue ou une croyance compatible avec une autre_. Et c'est exactement ce que fait ReactDOM. Il apporte des modifications au DOM réel pour le rendre compatible avec l'état actuel du DOM virtuel. React utilise un algorithme de _différenciation_ pour évaluer les modifications à apporter au DOM réel.

Il utilise un algorithme heuristique basé sur deux hypothèses :

1. Deux éléments de types différents produiront des arbres différents
2. Les éléments stables, ou les éléments qui ne sont pas modifiés, sont identifiés à l'aide d'un identifiant unique appelé `key`.

#### Éléments de types différents

React compare d'abord le type de l'élément racine. Si le type de l'élément racine est différent dans le DOM réel et le DOM virtuel, il détruit le DOM réel et en crée un nouveau.

Par exemple, si le type de racine dans le DOM réel était `div`, et celui dans le DOM virtuel était `span`, l'algorithme de différenciation effacerait l'ensemble du conteneur `div` du DOM réel.

#### Éléments DOM du même type

Ce cas traite des éléments qui sont du même type, mais qui ont des différences dans leurs valeurs de propriété.

Considérons ce nœud DOM dans le DOM réel :

```
<div class='heading'>Algorithme de différenciation React</div>
```

Maintenant, considérons le nœud DOM mis à jour qui est la sortie d'une méthode `render` d'un composant :

```
<div className='sub-heading'>Algorithme de différenciation React</div>
```

En comparant ces deux nœuds, React saurait que seul le className des nœuds est modifié, et il mettrait efficacement à jour uniquement la valeur de la classe dans le DOM réel.

#### Identification de la position des enfants dans le conteneur parent

React recommande l'utilisation de la prop `key` si des enfants similaires doivent être ajoutés à un nœud DOM particulier.

Considérons l'exemple d'un tableau de commentaires :

```
commentsArr.map (comment => {    return <div key={comment.id}>{comment.text}</div>})
```

L'utilisation de `key` dans les nœuds enfants du conteneur de commentaires aide React à identifier de manière unique les différents nœuds de commentaires. Si un changement se produit dans l'un des nœuds de commentaires, React saurait lequel mettre à jour en fonction de la valeur de la clé.

### Commencer avec React en utilisant `create-react-app`

`create-react-app` est un outil en ligne de commande React utilisé pour créer le code initial pour toute application React.

Il fait le travail fastidieux de configuration d'un serveur de développement, de gestion de la compilation de JSX en JavaScript comme discuté précédemment, et il fait quelques autres choses.

```
npm i create-react-app -g
```

Cela installe le module de nœud `create-react-app` globalement sur votre système.

La commande `create-react-app my-app` crée un projet React dans le répertoire `my-app`. Jouez avec les fichiers et essayez de créer un composant React plus petit.

J'espère que vous avez maintenant une idée de ce qu'est React et comment l'utiliser.

### Récapitulons ce que nous avons appris jusqu'à présent

1. Nous avons vu que la mise à jour des nœuds DOM en utilisant du code JavaScript brut n'est pas évolutive.
2. React est une bibliothèque JavaScript pour construire des interfaces utilisateur. Elle résout le problème d'évolutivité en mettant à jour efficacement le DOM.
3. Les composants React produisent une représentation DOM sous forme de JSX. JSX est simplement du sucre syntaxique utilisé pour faciliter le travail de développement. Il est transpilé en instructions JavaScript sous la forme `React.createElement`.
4. Nous avons appris la plupart des techniques ES6 courantes comme l'utilisation de `let` et `const`, la déstructuration d'objets, les classes, les fonctions fléchées et la modélisation de chaînes. Celles-ci sont utilisées lors de l'écriture de composants React.
5. Nous avons appris ce que sont les éléments React et comment ils sont créés.
6. Nous avons appris que React suit un modèle basé sur les composants et comment il utilise la composition pour créer des composants complexes à partir de composants plus simples. Le composant utilise `state` et `props` pour gérer l'état interne.
7. Nous avons plongé en profondeur dans la façon dont React crée le DOM virtuel et nous avons également compris l'algorithme de différenciation sous-jacent utilisé pour mettre à jour efficacement le DOM réel.

Dans la prochaine série d'articles sur React, je couvrirai les sujets suivants plus en détail :

1. Le cycle de vie des composants React
2. DOM virtuel
3. Commencer avec React en utilisant `create-react-app`

_Publié à l'origine sur [hashnode.com](https://hashnode.com/post/a-reintroduction-to-react-cjsbli2an02b7dys2y3ypng2z)._