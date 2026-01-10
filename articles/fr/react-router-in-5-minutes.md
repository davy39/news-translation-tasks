---
title: Apprendre React Router en 5 Minutes - Un Tutoriel pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-11T19:30:00.000Z'
originalURL: https://freecodecamp.org/news/react-router-in-5-minutes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f69740569d1a4ca4284.jpg
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
- name: Tutorial
  slug: tutorial
seo_title: Apprendre React Router en 5 Minutes - Un Tutoriel pour Débutants
seo_desc: 'By Bob Ziroll

  Sometimes you''ve only got 5 minutes to spare. Instead of wasting it on social media,
  let''s get a 5-minute introduction to React-Router! In this tutorial, we''re going
  to learn the basics of routing in React by building navigation for a S...'
---

Par Bob Ziroll

Parfois, vous n'avez que 5 minutes à perdre. Au lieu de les gaspiller sur les réseaux sociaux, apprenons les bases de React-Router en 5 minutes ! Dans ce tutoriel, nous allons apprendre les bases du routage dans React en construisant la navigation pour un site web de boutique de tricot Scrimba. Ce n'est pas réel, mais peut-être un jour... ;)

Si vous voulez une introduction complète à ce sujet, vous pouvez rejoindre la liste d'attente pour mon [prochain cours avancé sur React](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=router_article), ou si vous êtes encore débutant, consultez mon [cours d'introduction à React](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=router_article).

### Qu'est-ce que React-Router, au fait ?

De nombreux sites web modernes sont en réalité constitués d'une seule page, ils semblent simplement composés de plusieurs pages car ils contiennent des composants qui s'affichent comme des pages séparées. Ceux-ci sont généralement appelés SPAs - **a**pplications **s**ingle-**p**age. Au cœur, React Router permet de rendre conditionnellement certains composants à afficher en fonction de la *route* utilisée dans l'URL (`/` pour la page d'accueil, `/about` pour la page à propos, etc.).

Par exemple, nous pouvons utiliser React Router pour connecter _www.knit-with-scrimba.com/_ à _www.knit-with-scrimba.com/about_ ou _www.knit-with-scrimba.com/shop_

### Cela semble génial - comment l'utiliser ?

Pour utiliser React Router, vous devez d'abord l'installer en utilisant NPM :

```bash
npm install react-router-dom
```

Alternativement, vous pouvez simplement utiliser [ce terrain de jeu dans Scrimba](https://scrimba.com/c/cNq8MzCr), qui contient déjà le code complet.

Vous devrez importer BrowserRouter, Route et Switch depuis le package `react-router-dom` :

```js
import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
```

Dans mon exemple, je lie la page d'accueil avec deux autres "pages" (qui sont en réalité juste des composants) appelées `Shop` et `About`.

Tout d'abord, vous devez configurer votre application pour qu'elle fonctionne avec React Router. Tout ce qui est rendu doit être placé à l'intérieur de l'élément `<BrowserRouter>`, alors enveloppez votre App avec ceux-ci en premier. C'est le composant qui gère toute la logique d'affichage des différents composants que vous lui fournissez.

```js
// index.js
ReactDOM.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>, 
    document.getElementById('root')
)
```

Ensuite, dans votre composant App, ajoutez l'élément `Switch` (balises d'ouverture et de fermeture). Ceux-ci garantissent qu'un seul composant est rendu à la fois. Si nous ne les utilisons pas, nous pouvons par défaut utiliser le composant `Error`, que nous allons écrire plus tard.

```js
function App() {
    return (
        <main>
            <Switch>
                
            </Switch>
        </main>
    )
}
```

Il est maintenant temps d'ajouter vos balises `<Route>`. Ce sont les liens entre les composants et doivent être placés à l'intérieur des balises `<Switch>`.

Pour indiquer aux balises `<Route>` quel composant charger, ajoutez simplement un attribut `path` et le nom du composant que vous souhaitez charger avec l'attribut `component`.

```js
<Route path='/' component={Home} />
```

De nombreuses URL de pages d'accueil sont le nom du site suivi de `"/"`, par exemple, _www.knit-with-scrimba.com/_. Dans ce cas, nous ajoutons `exact` à la balise Route. Cela est dû au fait que les autres URL contiennent également "/", donc si nous ne disons pas à l'application qu'elle doit chercher uniquement `/`, elle charge la première correspondante à la route, et nous obtenons un bug assez délicat à gérer.

```js
function App() {
    return (
        <main>
            <Switch>
                <Route path="/" component={Home} exact />
                <Route path="/about" component={About} />
                <Route path="/shop" component={Shop} />
            </Switch>
        </main>
    )
}
```

Maintenant, importez les composants dans l'application. Vous pouvez souhaiter les placer dans un dossier "components" séparé pour garder le code propre et lisible.

```js
import Home from './components/Home';
import About from './components/About';
import Shop from './components/Shop';
```

Passons à ce message d'erreur dont j'ai parlé plus tôt, qui se charge si un utilisateur tape une URL incorrecte. Cela ressemble à une balise `<Route>` normale, mais sans chemin. Le composant Error contient `<h1>Oups ! Page non trouvée !</h1>`. N'oubliez pas de l'importer dans l'application.

```js
function App() {
    return (
        <main>
            <Switch>
                <Route path="/" component={Home} exact />
                <Route path="/about" component={About} />
                <Route path="/shop" component={Shop} />
                <Route component={Error} />
            </Switch>
        </main>
    )
}
```

Jusqu'à présent, notre site n'est navigable qu'en tapant les URL. Pour ajouter des liens cliquables au site, nous utilisons l'élément `Link` de React Router et configurons un nouveau composant `Navbar`. Une fois de plus, n'oubliez pas d'importer le nouveau composant dans l'application.

Ajoutez maintenant un `Link` pour chaque composant dans l'application et utilisez `to="URL"` pour les lier.

```js
function Navbar() {
  return (
    <div>
      <Link to="/">Accueil </Link>
      <Link to="/about">À propos </Link>
      <Link to="/shop">Boutique </Link>
    </div>
  );
};
```

Votre site dispose maintenant de liens cliquables qui peuvent vous naviguer autour de votre application monopage !

### Conclusion
Voilà donc comment faire. Si vous souhaitez naviguer facilement dans une application React, oubliez les balises d'ancrage et ajoutez React Router. C'est propre, c'est organisé, et cela rend l'ajout et la suppression de pages beaucoup plus faciles.

Pour en savoir plus sur les React Hooks et autres grandes fonctionnalités de React, vous pouvez rejoindre la liste d'attente pour mon [prochain cours avancé sur React](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=router_article).

Ou si vous cherchez quelque chose de plus adapté aux débutants, vous pouvez consulter mon [cours d'introduction à React](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=router_article).

Bon codage ;)