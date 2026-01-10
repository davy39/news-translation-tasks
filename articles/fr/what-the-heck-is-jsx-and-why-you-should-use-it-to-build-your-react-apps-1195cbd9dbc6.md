---
title: Qu'est-ce que JSX et pourquoi l'utiliser pour construire vos applications React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T17:29:36.000Z'
originalURL: https://freecodecamp.org/news/what-the-heck-is-jsx-and-why-you-should-use-it-to-build-your-react-apps-1195cbd9dbc6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*o7WmwGkLVR0dVQUYqfSBeg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Qu'est-ce que JSX et pourquoi l'utiliser pour construire vos applications
  React
seo_desc: 'By Ryan Harris

  As developers, we use a variety of tools and open source packages to make our jobs
  easier. Some of them are so widely used throughout the community that they seem
  native to JavaScript. But, they’re not, and they can fundamentally chang...'
---

Par Ryan Harris

En tant que développeurs, nous utilisons une variété d'outils et de packages open source pour faciliter notre travail. Certains d'entre eux sont si largement utilisés dans la communauté qu'ils semblent natifs à JavaScript. Mais ils ne le sont pas, et ils peuvent **changer fondamentalement la façon dont vous écrivez du code** au quotidien.

L'une de ces technologies que vous utilisez probablement déjà est JSX - **une extension de syntaxe similaire à XML pour JavaScript**. Créée par l'équipe de Facebook, elle est destinée à simplifier l'expérience du développeur. Comme le dit la spécification, la raison de la création de JSX était :

> "...définir une syntaxe concise et familière pour définir des structures arborescentes avec des attributs." ~ [Spécification JSX](https://facebook.github.io/jsx/)

Maintenant, vous vous dites probablement à vous-même, "Hé, Ryan, cela semble génial, mais **passons au code déjà**", alors voici notre premier exemple.

```
const helloWorld = <h1>Bonjour, le Monde !</h1>;
```

Et c'est tout !

L'extrait de code ci-dessus semble familier, mais avez-vous déjà arrêté de penser à sa puissance ? JSX nous permet de **passer des structures arborescentes composées d'éléments HTML ou React** comme s'ils étaient des valeurs JavaScript standard.

Bien que vous n'ayez pas à utiliser JSX lorsque vous écrivez React ([ou utiliser React pour essayer JSX](https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-jsx)), il est indéniable qu'il fait partie importante de l'écosystème React, alors plongeons et voyons ce qui se passe sous le capot.

#### Commencer avec JSX

La première chose à noter lors de l'utilisation de la syntaxe JSX est que React doit être dans la portée. Cela est dû à la façon dont il est compilé. Prenons cet exemple de composant :

```
function Hello() {  return <h1>Bonjour, le Monde !</h1>}
```

En coulisses, chaque élément rendu par le composant `Hello` est transpilé en un appel à `React.createElement`.

Dans ce cas :

```
function Hello() {  return React.createElement("h1", {}, "Bonjour, le Monde !")}
```

![Image](https://cdn-media-1.freecodecamp.org/images/i45KojKuegRdDklO7hgQUgFvqxOIUvvI-hZv)
*Source de l'image [rawpixel](https://unsplash.com/@rawpixel" rel="noopener" target="_blank" title=")*

Il en va de même pour les éléments imbriqués. Les deux exemples ci-dessous rendraient finalement le même balisage.

```
// Exemple 1 : Utilisation de la syntaxe JSX
function Nav() {  return (    <ul>      <li>Accueil</li>      <li>À propos</li>      <li>Portfolio</li>      <li>Contact</li>    </ul>  );}
```

```
// Exemple 2 : Sans utiliser la syntaxe JSX
function Nav() {  return (    React.createElement(      "ul",      {},      React.createElement("li", null, "Accueil"),      React.createElement("li", null, "À propos"),      React.createElement("li", null, "Portfolio"),      React.createElement("li", null, "Contact")    )  );}
```

#### React.createElement

Lorsque React crée des éléments, il appelle cette méthode, qui prend trois arguments.

1. Le nom de l'élément
2. Un objet représentant les props de l'élément
3. Un tableau des enfants de l'élément

Une chose à noter ici est que React interprète les éléments en minuscules comme du HTML et les éléments en PascalCase (ex. ThisIsPascalCase) comme des composants personnalisés. En raison de cela, les exemples suivants seraient interprétés différemment.

```
// 1. Élément HTML
React.createElement("div", null, "Un texte de contenu ici")
```

```
// 2. Élément React
React.createElement(Div, null, "Un texte de contenu ici")
```

Le premier exemple générerait un `<div>` avec la chaîne "Un texte de contenu ici" comme enfant. Cependant, la deuxième version lancerait une erreur (sauf, bien sûr, si un composant personnalisé `<Div />` était dans la portée) parce que `<Div />` est indéfini.

#### Props dans JSX

Lorsque vous travaillez avec React, vos composants rendent souvent des enfants et doivent leur passer des données pour que les enfants se rendent correctement. Ce sont ce qu'on appelle les props.

J'aime penser aux composants React comme à un groupe d'amis. Et que font les amis ? Ils [se donnent des props](https://www.urbandictionary.com/define.php?term=props). Heureusement, JSX nous offre plusieurs façons de le faire.

```
// 1. Props par défaut à vrai
<User loggedIn />
```

```
// 2. Littéraux de chaîne
<User name="Jon Johnson" />
```

```
// 3. Expressions JavaScript
<User balance={5 + 5 + 10} />
```

```
// 4. Attributs étendus
<User preferences={...this.state} />
```

Mais attention ! Vous ne pouvez pas passer d'instructions if ou de boucles for comme props car ce sont des [instructions, pas des expressions](https://dev.to/promhize/javascript-in-depth-all-you-need-to-know-about-expressions-statements-and-expression-statements-5k2).

![Image](https://cdn-media-1.freecodecamp.org/images/540ZKVGYlZkyJmuY6dpHkUwAozpqC2Xf4l5w)
*Source de l'image [Kevin Ku](https://unsplash.com/@ikukevk" rel="noopener" target="_blank" title=")*

#### Enfants dans JSX

Lorsque vous construisez votre application, vous finissez par avoir des composants qui rendent des enfants. Et puis ces composants doivent parfois rendre des enfants. Et ainsi de suite.

Puisque JSX est conçu pour nous faciliter le raisonnement sur les structures arborescentes d'éléments, il rend tout cela très facile. Basiquement, les éléments qu'un composant retourne deviennent ses enfants.

Il existe quatre façons de rendre des éléments enfants en utilisant JSX :

#### Chaînes de caractères

C'est l'exemple le plus simple d'enfants JSX. Dans le cas ci-dessous, React crée un élément HTML `<h1>` avec un enfant. L'enfant, cependant, n'est pas un autre élément HTML, juste une simple chaîne de caractères.

```
function AlertBanner() {  return (    <h1>Votre facture est due dans 2 jours</h1>  )}
```

#### **Éléments JSX**

C'est probablement le cas d'utilisation que les nouveaux développeurs React connaissent le mieux. Dans le composant ci-dessous, nous retournons un enfant HTML (le `<header>`), qui a deux enfants à lui, `<Nav />` et `<ProfilePic />`, tous deux étant des éléments JSX définis personnalisés.

```
function Header(props) {  return (    <header>      <Nav />      <ProfilePic />    </header>  )}
```

#### **Expressions**

Les expressions nous permettent de rendre facilement des éléments dans notre UI qui sont le résultat d'un calcul JavaScript. Un exemple simple de cela serait une addition de base.

Supposons que nous avons un composant appelé `<BillFooter />` qui rend des informations sur une facture ou un reçu. Supposons qu'il prend une prop appelée `total` qui représente le coût avant taxes et une autre prop `taxRate`, qui représente le taux de taxe applicable.

En utilisant des expressions, nous pouvons facilement rendre quelques informations utiles pour nos utilisateurs !

```
function BillFooter(props) {  return (    <div>      <h5>Taxe : {props.total * props.taxRate}</h5>      <h5>Total : {props.total + props.total * props.taxRate}</h5>    </div>  );}
```

#### **Fonctions**

Avec les fonctions, nous pouvons créer des éléments et des structures de manière programmatique, que React rendra ensuite pour nous. Cela facilite la création de plusieurs instances d'un composant ou le rendu d'éléments UI répétés.

Par exemple, utilisons la fonction `.map()` de JavaScript pour créer une barre de navigation.

```
// Tableau d'informations de page
const pages = [  {    id: 1,    text: "Accueil",    link: "/"  },  {    id: 2,    text: "Portfolio",    link: "/portfolio"  },  {    id: 3,    text: "Contact",    link: "/contact"  }];

// Rend une <ul> avec des enfants <li> créés de manière programmatique
function Nav() {  return (    <ul>      {pages.map(page => {        return (          <li key={page.id}>            <a href={page.link}>{page.text}</a>          </li>        );      })}    </ul>  );}
```

Maintenant, si nous voulons ajouter une nouvelle page à notre site, tout ce que nous avons à faire est d'ajouter un nouvel objet au tableau `pages` et React s'occupera du reste !

**Notez la prop `key`**. Notre fonction retourne un tableau d'éléments frères, dans ce cas des `<li>`, et React a besoin d'un moyen de suivre ceux qui sont montés, démontés ou mis à jour. Pour cela, il s'appuie sur cet identifiant unique pour chaque élément.

#### Utilisez les outils !

![Image](https://cdn-media-1.freecodecamp.org/images/ry5AANkjQySL0wIL0UlvdjlsG8ZHH720HGtf)
*Source de l'image [Barn Images](https://unsplash.com/@barnimages" rel="noopener" target="_blank" title=")*

Bien sûr, vous pouvez écrire des applications React sans JSX, mais je ne suis pas vraiment sûr de pourquoi vous voudriez le faire.

La capacité que JSX nous donne de passer des éléments en JavaScript comme s'ils étaient des citoyens de première classe se prête bien à travailler avec le reste de l'écosystème React. Si bien, en fait, que vous avez peut-être écrit cela tous les jours sans même le savoir.

En résumé : utilisez simplement JSX. Vous serez heureux de l'avoir fait.