---
title: Vous n'avez peut-être pas besoin de React Router
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-11T02:48:53.000Z'
originalURL: https://freecodecamp.org/news/you-might-not-need-react-router-38673620f3d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TKvlTeNqtkp1s-eVB5Hrvg@2x.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Vous n'avez peut-être pas besoin de React Router
seo_desc: 'By Konstantin Tarkus

  If you happened to work with Facebook’s React.js library for a while, you might
  notice a few misconceptions floating in the React community. One of them is the
  affirmation that React is just V from MVC architecture and needs to b...'
---

Par Konstantin Tarkus

Si vous avez travaillé avec la bibliothèque React.js de Facebook pendant un certain temps, vous avez peut-être remarqué quelques idées fausses qui circulent dans la communauté React. L'une d'elles est l'affirmation que React n'est que le V de l'architecture MVC et doit être mélangé avec un ensemble d'autres bibliothèques avant de pouvoir être utilisé comme un framework pour développer des applications web.

En pratique, vous voyez rarement un développeur React utiliser des contrôleurs et des modèles de MVC. L'architecture UI basée sur les composants prend progressivement le dessus dans la communauté front-end et de moins en moins de personnes utilisent le modèle MVC de nos jours.

Une autre idée fausse est que la bibliothèque React Router (RR) est la solution de routage officielle de Facebook. En réalité, la majorité des projets chez Facebook ne l'utilisent même pas.

En parlant de routage, la grande multitude de projets d'applications web et de cas d'utilisation peuvent très bien fonctionner avec un petit routeur personnalisé. Avant de classer cette notion comme une complète hérésie, permettez-moi de vous montrer comment implémenter une solution de routage complète avec moins de 50 lignes de code.

#### Navigation

Tout d'abord, il n'est pas nécessaire de combiner le routage et la navigation côté client au sein du même composant comme c'est fait dans RR. Ainsi, votre routeur peut être véritablement universel — fonctionner exactement de la même manière, avec la même API dans les environnements côté client et côté serveur. Il existe un excellent module npm appelé **history** qui peut gérer la partie navigation (pour information, c'est une sorte de wrapper pour l'API HTML5 History et est également utilisé en interne par RR). Vous créez simplement un fichier history.js dans votre projet où vous initialisez ce composant (classe) et l'utilisez comme un singleton dans votre application :

```
import createHistory from 'history/lib/createBrowserHistory';
import useQueries from 'history/lib/useQueries';
```

```
export default useQueries(createHistory)();
```

Désormais, vous pouvez simplement référencer ce fichier et appeler history.push('/new-page') chaque fois que vous devez rediriger un utilisateur vers un nouvel emplacement (URL) sans rafraîchir toute la page. Dans le fichier principal de l'application (code de démarrage), vous pouvez vous abonner à tous les changements d'URL comme suit :

```
import history from './history';
```

```
function render(location) { /* Rendre l'application React, continuez la lecture */ }
```

```
render(history.getCurrentLocation()); // rendre l'URL actuelle
history.listen(render);               // rendre les URL suivantes
```

Un composant React avec des liens fonctionnant côté client peut ressembler à ceci :

```
import React from 'react';
import history from '../history';
```

```
class App extends React.Component {
```

```
  transition = event => {    event.preventDefault();    history.push({      pathname: event.currentTarget.pathname,      search: event.currentTarget.search    });  };
```

```
  render() {    return (      <ul>        <li><a href="/" onClick={this.transition}>Accueil</a></li>        <li><a href="/one" onClick={this.transition}>Un</a></li>        <li><a href="/two" onClick={this.transition}>Deux</a></li>      </ul>    );  }
```

```
}
```

Cependant, en pratique, vous pourriez vouloir extraire cette fonctionnalité de "transition" dans un composant React autonome. Voir le composant [Link](https://github.com/kriasoft/react-static-boilerplate/blob/master/components/Link/Link.js) dans [React Static Boilerplate](https://github.com/kriasoft/react-static-boilerplate) (RSB). Ainsi, vous pourriez écrire des liens côté client uniquement comme ceci : <Link to="/some-page">Cliquez</Link>.

Besoin d'afficher un message de confirmation avant que l'utilisateur ne quitte une page ? Il suffit d'enregistrer l'événement history.listenBefore(..) dans la méthode componentDidMount() de votre composant comme décrit dans la [documentation](https://github.com/ReactJSTraining/history/blob/master/docs/ConfirmingNavigation.md) du module history. La même approche peut être utilisée pour animer les transitions entre les pages ([démo](https://jsfiddle.net/frenzzy/4ota5fag/2/)).

#### Routage

Vous pouvez décrire la liste des routes et chaque route en particulier via des objets JavaScript simples, pas besoin d'utiliser JSX ici. Par exemple :

```
const routes = [  { path: '/', action: () => <HomePage /> },  { path: '/tasks', action: () => <TaskList /> },  { path: '/tasks/:id', action: () => <TaskDetails /> }];
```

_Au fait, si quelqu'un sait pourquoi tant de gens préfèrent utiliser JSX pour quelque chose qui n'est pas lié au rendu de l'UI, veuillez laisser un commentaire._

Vous pouvez écrire vos gestionnaires de routes en utilisant la syntaxe async/await d'ES2015+, il n'est pas nécessaire d'utiliser des callbacks comme c'est fait dans RR. Par exemple :

```
{  path: '/tasks/:id(\\d+)',  async action({ params }) {    const resp = await fetch(`/api/tasks/${params.id}`);    const data = await resp.json();    return data && <TaskDetails {...data} />;  }}
```

Dans la majorité des cas d'utilisation que je connais, il n'est pas nécessaire d'utiliser des routes imbriquées comme c'est fait dans RR. L'utilisation de routes imbriquées rend les choses plus compliquées qu'elles ne devraient l'être et conduit à une implémentation de routage excessivement complexe et difficile à maintenir. Pour autant que je sache, même chez Facebook, ils n'utilisent pas de routes imbriquées côté client étant donné l'échelle de leurs applications (au moins pas dans tous leurs projets).

Au lieu d'imbriquer les routes, vous pouvez imbriquer les composants React, par exemple :

```
import React from 'react';
import Layout from '../components/Layout';
```

```
class AboutPage extends React.Component {  render() {    return (      <Layout title="À propos de nous" breadcrumbs="Accueil > À propos">        <h1>Bienvenue !</h1>        <p>Ici vous pouvez en apprendre plus sur notre produit.</p>      </Layout>    );  }}
```

```
export default AboutPage;
```

Cette approche est bien plus simple à implémenter que les routes imbriquées et en même temps plus flexible, intuitive et déverrouille plus de cas d'utilisation (remarquez comment vous pouvez passer un composant de breadcrumbs dans le Layout).

Le routeur lui-même peut être écrit comme une paire de deux fonctions — matchURI(), une fonction interne (privée) qui aide à comparer une chaîne de chemin paramétrée avec l'URL réelle ; et la fonction resolve() qui parcourt la liste des routes, trouve la route qui correspond à l'emplacement donné, exécute la fonction de gestion de route et retourne le résultat à l'appelant. Voici à quoi cela peut ressembler (router.js) :

```
import toRegex from 'path-to-regexp';
```

```
function matchURI(path, uri) {  const keys = [];  const pattern = toRegex(path, keys); // TODO: Utiliser la mise en cache  const match = pattern.exec(uri);  if (!match) return null;  const params = Object.create(null);  for (let i = 1; i < match.length; i++) {    params[keys[i - 1].name] =      match[i] !== undefined ? match[i] : undefined;  }  return params;}
```

```
async function resolve(routes, context) {  for (const route of routes) {    const uri = context.error ? '/error' : context.pathname;    const params = matchURI(route.path, uri);    if (!params) continue;    const result = await route.action({ ...context, params });    if (result) return result;  }  const error = new Error('Not found');  error.status = 404;  throw error;}
```

```
export default { resolve };
```

Consultez la documentation de la bibliothèque [path-to-regexp](https://github.com/pillarjs/path-to-regexp). Cette bibliothèque est géniale ! Par exemple, vous pouvez utiliser la même bibliothèque pour convertir des chaînes de chemin paramétrées en URLs :

```
const toUrlPath = pathToRegexp.compile('/tasks/:id(\\d+)')
toUrlPath({ id: 123 }) //=> "/user/123"
toUrlPath({ id: 'abc' }) /=> error, doesn't match the \d+ constraint
```

Maintenant, vous pouvez mettre à jour le fichier principal de l'application (point d'entrée) pour utiliser ce routeur :

```
import ReactDOM from 'react-dom';
import history from './history';
import router from './router';
import routes from './routes';
```

```
const container = document.getElementById('root');
```

```
function renderComponent(component) {  ReactDOM.render(component, container);}
```

```
function render(location) {  router.resolve(routes, location)    .then(renderComponent)    .catch(error => router.resolve(routes, { ...location, error })    .then(renderComponent));}
```

```
render(history.getCurrentLocation()); // rendre l'URL actuelle
history.listen(render);               // rendre les URL suivantes
```

C'est tout ! Vous pourriez également vouloir consulter mes projets de modèles React qui présentent cette approche de routage :

[Universal Router](https://github.com/kriasoft/universal-router) — une solution de routage simple de style middleware  
[React Starter Kit](https://github.com/kriasoft/react-starter-kit) — modèle d'application web isomorphique (Node.js, GraphQL, React)  
[React Static Boilerplate](https://github.com/kriasoft/react-static-boilerplate) — application web sans serveur (React, Redux, Firebase)  
[ASP.NET Core Starter Kit](https://github.com/kriasoft/aspnet-starter-kit) — application monopage (ASP.NET Core, C#, React)

Ces modèles sont assez populaires et utilisés avec succès dans de nombreux projets réels à travers le monde. Cela vaut définitivement le coup d'œil :)

**P.S.** : Fan des routes déclaratives ? Trouvez une version déclarative de cette approche de routage [ici](https://github.com/kriasoft/react-static-boilerplate/blob/master/docs/routing-and-navigation.md). Consultez les commentaires de cet article [sur Reddit](https://www.reddit.com/r/reactjs/comments/4s8ulw/you_might_not_need_react_router/).

**Suivant** : Vous n'avez peut-être pas besoin de React Router — Partie 2 (à venir bientôt)