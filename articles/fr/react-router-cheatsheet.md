---
title: Le guide pratique de React Router – Tout ce que vous devez savoir
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-19T14:52:33.000Z'
originalURL: https://freecodecamp.org/news/react-router-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/the-react-router-cheatsheet.png
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: Le guide pratique de React Router – Tout ce que vous devez savoir
seo_desc: "If you're building React applications for the web, you're going to need\
  \ to use a dedicated router to display pages and navigate your user around them.\
  \ \nThat's why today we're going to go over the most popular and most powerful router\
  \ for React applic..."
---

Si vous construisez des applications React pour le web, vous allez avoir besoin d'utiliser un routeur dédié pour afficher des pages et naviguer vos utilisateurs entre elles. 

C'est pourquoi aujourd'hui nous allons passer en revue le routeur le plus populaire et le plus puissant pour les applications React – React Router. 

Nous allons passer en revue 11 des fonctionnalités essentielles que vous devez connaître si vous utilisez React Router dans vos projets aujourd'hui, spécifiquement pour le web en utilisant le package `react-router-dom`.

## Vous voulez votre propre copie ? 📄

**[Cliquez ici pour télécharger le guide pratique au format PDF](https://reedbarger.com/resources/react-router-cheatsheet-2021)** (cela prend 5 secondes).

Il inclut toutes les informations essentielles ici sous forme de guide PDF pratique.

## Installer React Router

La toute première étape pour utiliser React Router est d'installer le package approprié. 

Il existe techniquement trois packages différents : React Router, React Router DOM et React Router Native. 

La principale différence entre eux réside dans leur utilisation. React Router DOM est pour les applications web et React Router Native est pour les applications mobiles faites avec React Native.

La première chose que vous devrez faire est d'installer React Router DOM en utilisant npm (ou yarn) : 

```bash
npm install react-router-dom
```

## Configuration de base de React Router

Une fois installé, nous pouvons importer notre premier composant qui est requis pour utiliser React Router et qui s'appelle BrowserRouter. 

Notez qu'il existe plusieurs types de routeurs que `react-router-dom` fournit en plus de BrowserRouter, que nous n'aborderons pas ici. Il est courant de donner un alias (renommer) BrowserRoute simplement en 'Router' lorsqu'il est importé.

Si nous voulons fournir des routes dans toute notre application, cela doit être enveloppé autour de tout notre arbre de composants. C'est pourquoi vous le verrez généralement enveloppé autour ou dans le composant principal de l'application :

```js
import { BrowserRouter as Router } from 'react-router-dom';

export default function App() {
  return (
    <Router>
      {/* les routes vont ici, en tant qu'enfants */}
    </Router>
  );
}
```

C'est la fonction principale de BrowserRouter : pouvoir déclarer des routes individuelles dans notre application. 

Notez que toute donnée spécifique au routeur ne peut pas être accessible en dehors du composant Router. Par exemple, nous ne pouvons pas accéder aux données d'historique en dehors du routeur (c'est-à-dire, avec le hook `useHistory`) et nous ne pouvons pas créer une Route en dehors d'un composant Router.

## Composant Route

Le composant suivant est le composant Route. 

Nous déclarons les routes dans le composant Router en tant qu'enfants. Nous pouvons déclarer autant de routes que nous le souhaitons et nous devons fournir au moins deux props à chaque route, `path` et `component` (ou `render`) :

```js
import { BrowserRouter as Router, Route } from 'react-router-dom';

export default function App() {
  return (
    <Router>
      <Route path="/about" component={About} />
    </Router>
  );
}

function About() {
  return <>about</>   
}
```

La prop `path` spécifie sur quel chemin de notre application une route donnée est située. 

Pour une page "à propos", par exemple, nous pourrions vouloir que cette route soit accessible sur le chemin '/about'. 

Les props `render` ou `component` sont utilisées pour afficher un composant spécifique pour notre chemin.

La prop `component` ne peut recevoir qu'une référence à un composant donné, tandis que `render` est plus typiquement utilisée pour appliquer une logique conditionnelle afin de rendre un composant ou un autre. Pour render, vous pouvez soit utiliser une référence à un composant, soit utiliser une fonction :

```js
import { BrowserRouter as Router, Route } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Route path="/" render={() => <Home />} />
      <Route path="/about" component={About} />
    </Router>
  );
}

function Home() {
  return <>home</>;
}

function About() {
  return <>about</>;
}
```

Il est bon de noter que vous pouvez potentiellement supprimer entièrement la prop `render` ou `component` et utiliser le composant que vous souhaitez associer à une route donnée en tant qu'enfant de Route :

```js
import { BrowserRouter as Router, Route } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Route path="/about">
        <About />
      </Route>
    </Router>
  );
}
```

Enfin, si vous voulez qu'un composant (comme une barre de navigation) soit visible sur chaque page, placez-le toujours dans le routeur du navigateur, mais au-dessus (ou en dessous) des routes déclarées : 

```js
import { BrowserRouter as Router, Route } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Route path="/" component={Home} />
      <Route path="/about" component={About} />
    </Router>
  );
}

function Navbar() {
  // visible sur chaque page
  return <>navbar</>
}

function Home() {
  return <>home</>;
}

function About() {
  return <>about</>;
}
```

## Composant Switch

Lorsque nous commençons à ajouter plusieurs routes, nous remarquerons quelque chose d'étrange.

Supposons que nous avons une route pour la page d'accueil et la page à propos. Même si nous spécifions deux chemins différents, '/' et '/about', lorsque je visite la page à propos, nous verrons à la fois les composants de la page d'accueil et de la page à propos.

Nous pouvons corriger cela avec la prop exact, sur la route de la page d'accueil pour nous assurer que notre routeur correspond exactement au chemin '/' au lieu de '/about' :

```js
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
      </Switch>
    </Router>
  );
}
```

Lorsque nous devons basculer entre différentes routes que notre routeur doit afficher, il existe en fait un composant dédié que vous devez utiliser si vous avez plusieurs routes dans votre routeur et c'est le composant Switch. 

Le composant switch doit être inclus dans le routeur et nous pouvons placer toutes nos routes à l'intérieur : 

```js
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
      </Switch>
    </Router>
  );
}
```

Le composant switch parcourt toutes ses routes enfants et affiche la première dont le chemin correspond à l'URL actuelle. 

Ce composant est ce que nous voulons utiliser dans la plupart des cas pour la plupart des applications, car nous avons plusieurs routes et plusieurs pages dans notre application, mais nous ne voulons afficher qu'une seule page à la fois. 

Si pour une raison quelconque vous souhaitez que plusieurs pages soient affichées en même temps, vous pourriez envisager de ne pas utiliser le composant switch.

## Route 404

Si nous essayons d'aller à un chemin qui n'existe pas dans notre application, que allons-nous voir ?

Nous ne allons rien voir si nous n'avons pas de route correspondant à cela. Comment faire une route catch-all ? 

Si un utilisateur essaie d'aller à une page pour laquelle nous n'avons pas de route définie, nous pouvons créer une route et définir le chemin avec un astérisque * :

```js
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  );
}

function NotFound() {
  return <>Vous avez atterri sur une page qui n'existe pas</>;
}
```

Cela correspondra à toute tentative de visite d'une page qui n'existe pas et nous pouvons la connecter à un composant non trouvé pour informer nos utilisateurs qu'ils ont "atterri sur une page qui n'existe pas".

## Composant Link

Supposons que dans notre NavBar, nous voulons créer des liens pour pouvoir naviguer plus facilement dans notre application au lieu de devoir changer l'URL manuellement dans le navigateur. 

Nous pouvons le faire avec un autre composant spécial de React Router DOM appelé le composant Link. Il accepte la prop `to`, qui spécifie où nous voulons que le lien navigue notre utilisateur. Dans notre cas, nous pourrions avoir un lien vers la page d'accueil et un lien vers la page à propos :

```js
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" component={Home} />
        <Route path="/about" component={About} />
      </Switch>
    </Router>
  );
}

function Navbar() {
  return (
    <nav>
      <Link to="/">Accueil</Link>
      <Link to="/about">À propos</Link>
    </nav>
  )
}
```

Le composant Link nous permet de fournir des styles en ligne comme n'importe quel composant React standard. Il nous donne également une prop `component` utile, afin que nous puissions définir notre lien comme notre propre composant personnalisé pour un style encore plus facile.

## Composant NavLink

De plus, React Router DOM nous donne un composant NavLink qui est utile dans le cas où nous voulons appliquer des styles spéciaux. 

Si nous sommes sur le chemin actuel vers lequel le lien pointe, cela nous permet de créer des styles de lien actifs pour informer nos utilisateurs, en regardant notre lien, sur quelle page ils se trouvent. 

Par exemple, si nos utilisateurs sont sur la page d'accueil, nous pourrions leur dire autant en utilisant la prop `activeStyle` pour rendre notre lien en gras et rouge lorsqu'ils sont sur la page d'accueil :

```js
import {
  BrowserRouter as Router,
  Switch,
  Route,
  NavLink
} from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" component={Home} />
        <Route path="/about" component={About} />
      </Switch>
    </Router>
  );
}

function Navbar() {
  return (
    <nav>
      <NavLink
        activeStyle={{
          fontWeight: "bold",
          color: "red"
        }}
        to="/"
      >
        Accueil
      </NavLink>
      <NavLink activeClassName="active" to="/about">
        À propos
      </NavLink>
    </nav>
  );
}

```

Il existe également une prop `activeClassName` qui peut être définie si vous ne souhaitez pas inclure de styles en ligne ou souhaitez des styles plus réutilisables pour effectuer la même fonction que `activeStyle`.

## Composant Redirect

Un autre composant très utile que React Router DOM nous donne est le composant Redirect.

Cela peut sembler étrange d'avoir un composant qui effectue une fonction de redirection de notre utilisateur lorsqu'il est affiché, mais cela est très fonctionnel. 

Lorsque nous utilisons quelque chose comme une route privée et que nous avons une condition dans laquelle l'utilisateur n'est pas authentifié, nous voulons le rediriger vers la page de connexion. 

Voici un exemple d'implémentation d'un composant de route privée qui garantit qu'un utilisateur est authentifié avant de lui montrer une route particulière qui a été déclarée avec ce composant. 

Sinon, s'ils ne sont pas authentifiés, ils seront redirigés vers une route publique (présumément une route de connexion) une fois le composant de redirection affiché :

```js
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect
} from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <PrivateRoute path="/hidden" component={Hidden} />
      </Switch>
    </Router>
  );
}

function PrivateRoute({ component: Component, ...rest }) {
  // useAuth est un hook personnalisé pour obtenir l'état d'authentification de l'utilisateur actuel
  const isAuth = useAuth();

  return (
    <Route
      {...rest}
      render={(props) =>
        isAuth ? <Component {...props} /> : <Redirect to="/" />
      }
    />
  );
}

function Home() {
  return <>accueil</>;
}

function Hidden() {
  return <>caché</>;
}
```

Le composant Redirect est très simple à utiliser, très déclaratif, et nous permet de voir le grand avantage de React Router DOM étant basé sur des composants, tout comme tout dans React.

## Hook useHistory

En plus de tous ces composants puissants, il existe des hooks très utiles que React Router DOM nous donne. 

Ils sont principalement utiles en fournissant des informations supplémentaires que nous pouvons utiliser dans nos composants. Ils peuvent être appelés comme des hooks React normaux pour lesquels nous pouvons utiliser leurs valeurs exactement comme nous le souhaitons. 

Peut-être le hook le plus puissant est le hook `useHistory`. Nous pouvons l'appeler en haut de n'importe quel composant qui est déclaré dans notre composant routeur et obtenir les données `history`, qui incluent des informations telles que l'emplacement associé à notre composant. 

Cela nous dit tout sur l'endroit où l'utilisateur se trouve actuellement, comme le chemin sur lequel il se trouve, ainsi que tous les paramètres de requête qui pourraient être ajoutés à notre URL. Toutes les données d'emplacement sont accessibles depuis `history.location` :

```js
import { useHistory } from "react-router-dom";


function About() {
  const history = useHistory();
    
  console.log(history.location.pathname); // '/about'

  return (
    <>
     <h1>La page à propos est sur : {history.location.pathname}</h1>
    </>
  );
}
```

De plus, l'objet history inclut directement des méthodes utiles qui nous permettent de diriger nos utilisateurs vers différentes pages dans notre application de manière programmatique. 

Cela est très utile, par exemple, pour rediriger notre utilisateur après la connexion, ou dans toute situation où nous devons emmener un utilisateur d'une page à une autre. 

Nous pouvons pousser les utilisateurs d'une page à une autre en utilisant `history.push`. Lorsque nous utilisons la méthode push, nous devons simplement fournir le chemin vers lequel nous voulons emmener nos utilisateurs en utilisant cette méthode. Elle ajoute cette nouvelle page à la pile (pour ainsi dire) de notre historique :

```js
import { useHistory } from "react-router-dom";


function About() {
  const history = useHistory();
    
  console.log(history.location.pathname); // '/about'

  return (
    <>
     <h1>La page à propos est sur : {history.location.pathname}</h1>
     <button onClick={() => history.push('/')}>Aller à la page d'accueil</button>
    </>
  );
}
```

Nous pouvons également rediriger nos utilisateurs avec `history.replace`, qui accepte également une valeur de chemin, mais efface tout dans l'historique, après que la navigation soit effectuée. Cela est utile pour les situations où revenir en arrière dans l'historique n'est plus nécessaire, comme après que les utilisateurs ont été déconnectés.

## Hook useLocation

Le hook `useLocation` inclut toutes les mêmes informations que le hook `useHistory`. 

Il est important de noter que si vous avez besoin à la fois des données de localisation et d'utiliser l'historique pour naviguer de manière programmatique votre utilisateur, assurez-vous d'utiliser useHistory. Cependant, si vous voulez uniquement les données de localisation, tout ce que vous avez à faire est d'appeler useLocation ou de récupérer toutes les données de localisation sur un objet qui est identique aux données fournies sur `history.location` :

```js
import { useLocation } from "react-router-dom";


function About() {
  const location = useLocation();
    
  console.log(location.pathname); // '/about'

  return (
    <>
     <h1>La page à propos est sur : {location.pathname}</h1>
    </>
  );
}
```

## Hook useParams + Routes dynamiques

Une chose que nous n'avons pas couverte en ce qui concerne les routes est que nous pouvons naturellement créer des routes dynamiques. Cela signifie des routes qui ne sont pas fixes et déterminées, mais qui peuvent être n'importe quel nombre de caractères. 

Les routes dynamiques sont utiles dans des situations où nous avons, par exemple, un article de blog avec un slug unique. Comment pouvons-nous nous assurer que nous affichons les données appropriées et les composants appropriés, étant donné que le slug de notre article de blog peut être complètement différent ?

Pour déclarer un paramètre de route sur une route donnée, il doit être préfixé par un deux-points `:`. Si je voulais créer une route dynamique, "/blog/:postSlug", pour un composant d'article de blog, cela pourrait ressembler à ce qui suit :

```js
import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/blog/:postSlug" component={BlogPost} />
      </Switch>
    </Router>
  );
}

function Home() {
  return <>accueil</>;
}

function BlogPost() {
  return <>article de blog</>;
}

```

Nous correspondons maintenant au composant approprié ou quel que soit le slug. Mais dans notre composant BlogPost, comment recevons-nous ces données de slug de l'article ? 

Nous pouvons accéder à n'importe quel paramètre de route d'une route déclarée avec son composant associé en utilisant le hook `useParams`. 

useParams retournera un objet qui contiendra des propriétés correspondant à nos paramètres de route (dans ce cas, `postSlug`). Nous pouvons utiliser la déstructuration d'objet pour accéder immédiatement et déclarer en tant que variable avec le nom `postSlug` :

```js
import React from "react";
import { BrowserRouter as Router, Switch, Route, useParams } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/blog/:postSlug" component={BlogPost} />
      </Switch>
    </Router>
  );
}

function Home() {
  return <>accueil</>;
}

function BlogPost() {
  const [post, setPost] = React.useState(null);
  const { postSlug } = useParams();

  React.useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/posts/${postSlug}`)
      .then((res) => res.json())
      .then((data) => setPost(data));
  }, [postSlug]);

  if (!post) return null;

  return (
    <>
      <h1>{post.title}</h1>
      <p>{post.description}</p>
    </>
  );
}
```

Si nous allons à la route '/blog/mon-article-de-blog', je peux accéder à la chaîne 'mon-article-de-blog' sur la variable `postSlug` et récupérer les données associées à cet article dans useEffect.

## Hook useRouteMatch

Si nous voulons savoir si le composant donné est sur une certaine page, nous pouvons utiliser le hook `useRouteMatch`. 

Par exemple, dans notre article de blog, pour voir si la page sur laquelle nous nous trouvons correspond à la route "/blog/:postSlug", nous pouvons obtenir une valeur booléenne qui nous indiquera si la route sur laquelle nous nous trouvons correspond au motif que nous avons spécifié :

```js
import { useRouteMatch } from "react-router-dom";

function BlogPost() {
  const isBlogPostRoute = useRouteMatch("/blog/:postSlug");
 
  // afficher, masquer le contenu, ou faire autre chose
}
```

Cela est utile dans des conditions où nous voulons montrer quelque chose de spécifique, en fonction du fait que nous sommes sur une certaine route ou non.

## Vous voulez garder ce guide pour référence future ?

**[Cliquez ici pour télécharger le guide pratique en tant que PDF utile](https://reedbarger.com/resources/react-router-cheatsheet-2021).**

Voici 3 avantages rapides que vous obtenez lorsque vous téléchargez la version téléchargeable :

* Vous obtiendrez des tonnes d'extraits de code copiables pour une réutilisation facile dans vos propres projets.
* C'est un excellent guide de référence pour renforcer vos compétences en tant que développeur React et pour les entretiens d'embauche.
* Vous pouvez prendre, utiliser, imprimer, lire et relire ce guide littéralement n'importe où que vous aimez.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*