---
title: Comment passer à React Router 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-01T22:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-upgrading-to-react-router-4
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/react-router-4-2.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react router
  slug: react-router
- name: react-router-4
  slug: react-router-4
seo_title: Comment passer à React Router 4
seo_desc: "By Lekha Surasani\n\nNot long after I started working at my current position,\
  \ the team realized that it would be necessary for us to upgrade to React 16 so\
  \ we could use a new UI library we were keen on adopting. \nTo figure out how much\
  \ time this upgrad..."
---

Par Lekha Surasani

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-82.png)

Peu de temps après avoir commencé à travailler à mon poste actuel, l'équipe a réalisé qu'il serait nécessaire pour nous de passer à React 16 afin que nous puissions utiliser une nouvelle bibliothèque d'interface utilisateur que nous souhaitions adopter. 

Pour déterminer combien de temps cette mise à niveau nécessiterait, nous avons examiné tous nos packages actuels pour voir s'ils étaient compatibles avec React 16, et pour voir si nous utilisions toujours des packages non supportés ou obsolètes. 

Les débuts de notre base de code avaient été construits par des développeurs qui utilisaient n'importe quelle bibliothèque open source ou tierce qu'ils voulaient, sans vraiment les évaluer. Ainsi, nous avons constaté que beaucoup de ces packages étaient obsolètes et devaient être remplacés dès que possible. 

L'une des plus grandes surprises pour nous a été l'obsolescence de `react-router-redux`. Nous utilisions `react-router-redux` en conjonction avec react-router v3. Cela nous a amenés à réfléchir sérieusement à la raison pour laquelle nous utilisions `redux` dans notre routeur en premier lieu. 

Une fois que nous avons commencé à nous pencher sur react router v4, nous avons réalisé que les nouvelles fonctionnalités élimineraient pratiquement toute raison pour nous d'utiliser une bibliothèque supplémentaire pour connecter notre routeur et `redux`. Ainsi, nous nous sommes retrouvés dans la position de simplement passer de react router 3 à 4, et de supprimer `react-router-redux` de notre application.

Ainsi, j'ai été chargée de mettre à niveau notre routeur vers la v4 après seulement deux mois dans ce poste et en travaillant avec React. Cela était dû au fait que la mise à niveau de React Router 3 vers React Router 4 semblait être une tâche triviale. Mais, comme je l'ai rapidement découvert, cela était un peu plus impliqué que je ne l'avais anticipé. 

En parcourant la [documentation](https://reacttraining.com/react-router/web/guides/quick-start), le [dépôt GitHub](https://github.com/ReactTraining/react-router/), et de nombreuses réponses sur Stack Overflow, j'ai finalement rassemblé les étapes pour la mise à niveau et souhaitais partager mes conclusions — surtout pour expliquer comment et pourquoi certains changements sont effectués.

Le plus grand changement à noter, selon les créateurs de React Router, est que la mise à niveau de React Router 3 à React Router 4 est plus qu'une simple mise à jour de quelques bibliothèques et fonctionnalités — elle vous permet de changer fondamentalement le fonctionnement de votre routeur. Les créateurs de React Router voulaient revenir à un routeur simple, permettant au développeur de le personnaliser comme il le souhaite.

J'ai divisé ce guide en 5 parties différentes :

1. Package
2. Historique
3. Route
4. Props
5. Intégration Redux

---

# Package

La structure du package React Router v4 a changé de telle sorte qu'il n'est plus nécessaire d'installer react-router — vous devez installer `react-router-dom` (et désinstaller `react-router`), mais vous ne perdez rien puisque celui-ci ré-export toutes les exportations de `react-router`. Cela signifie que vous devez également mettre à jour toutes les déclarations d'importation de `react-router` vers `react-router-dom`.

---

# Historique

L'historique est une partie essentielle du routage, nous permettant de nous souvenir d'où nous venons et où nous sommes actuellement. L'historique se présente sous de nombreuses formes pour react-router, et pourrait prendre un certain temps à expliquer. Donc, pour garder cet article sur le sujet, je recommande simplement de lire [cet article](https://medium.com/@pshrmn/a-little-bit-of-history-f245306f48dd) qui explique l'historique en relation avec react router 4. Cet article devrait couvrir la plupart des cas d'utilisation de l'historique.

---

# Route

React Router v3 nous permettait de placer toutes les routes de notre application dans un seul fichier, que nous appellerons router.js. Cependant, React Router v4 vous permet de placer les Routes dans les composants qu'elles rendent. L'idée ici est de _router dynamiquement_ l'application — en d'autres termes, le routage a lieu pendant que l'application est en train de se rendre.

Cependant, si vous travaillez avec une base de code héritée de taille décente, vous ne ferez probablement pas un changement aussi important. Heureusement, React Router v4 permet toujours de placer toutes les routes dans un fichier central, ce qui est la manière dont je vais créer tous nos exemples. Il y a, cependant, quelques anciens composants et fonctionnalités qui devront être remplacés.

## IndexRoute

Auparavant, `IndexRoute` était utilisé comme une route pour une interface utilisateur par défaut d'une route parente. Mais, dans la v4, `IndexRoute` n'est plus utilisé, puisque cette fonctionnalité est maintenant disponible dans Route.

Pour fournir une interface utilisateur par défaut, plusieurs Routes ayant le même chemin permettront à tous les composants associés de se rendre :

```
import { BrowserRouter as Router, Route } from 'react-router-dom';

<Router>
    // exemple de nos composants de route
    <Route path="/" component={Home} />
    <Route path="/" component={About} />
    <Route path="/" component={Contact} />
</Router>
```

Ainsi, tous les composants — `Home`, `About`, et `Contact` — se rendront. À cause de cela, vous ne pouvez plus imbriquer les Routes.

De plus, pour permettre une meilleure correspondance sans l'utilisation de `IndexRoute`, vous pouvez utiliser le mot-clé exact.

```javascript
import { BrowserRouter as Router, Route } from 'react-router-dom';

<Router>
    // exemple de nos composants de route
    <Route exact path="/" component={Home} />
    <Route path="/about" component={About} />
</Router>
```

## Routage Exclusif

Après avoir ajouté le mot-clé exact, `something.com/about` sera routé vers lorsque le routeur voit un chemin `/about`. Mais maintenant, que se passe-t-il si vous avez un autre chemin, `/about/team` ? Comme je l'ai mentionné précédemment, le routeur rendra tout ce qui correspond. Ainsi, les composants associés à la fois à `/about` et `/about/team` se rendront. Si c'est ce que vous aviez l'intention de faire, alors c'est parfait ! Cependant, si ce n'est pas ce que vous voulez, vous devrez peut-être mettre un Switch autour de ce groupe de Routes. Cela permettra au premier chemin qui correspond à l'URL de se rendre.

```javascript
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

<Router>
    <Switch>
       <Route exact path ="/" component={Home} />
       <Route path="/about/team" component={Team} />
       <Route path="/about" component={About} />
    </Switch>
</Router>
```

Notez que le mot-clé exact doit toujours apparaître pour le composant Home — sinon, il correspondrait aux routes suivantes. Notez également que nous devons lister `/about/team` avant `/about` afin que la route aille vers le composant `Team` au lieu du composant `About` lorsqu'elle voit `something.com/about/team`. Si elle voyait `/about` en premier, elle s'arrêterait là et rendrait le composant `About` parce que Switch ne rend que le premier composant qui correspond.

## Route par défaut

Une route par défaut, ou une route attrape-tout, couramment utilisée pour les pages 404, est la route que vous utilisez lorsque aucune des routes ne correspond.

Dans React Router v3, une route `Route` par défaut était :

`<Route path="*" component={NotFound} />`

Dans React Router v4, la route `Route` par défaut a été changée en :

```
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

<Router>
    <Switch>
       <Route exact path ="/" component={Home} />
       <Route path="/about/team" component={Team} />
       <Route path="/about" component={About} />
       <Route component={NotFound} /> // ceci est notre route par défaut
    </Switch>
</Router>
```

Lorsque vous n'incluez pas de chemin dans une `Route`, le composant se rendra toujours. Ainsi, comme nous l'avons discuté ci-dessus, nous pouvons utiliser `Switch` pour n'obtenir qu'un seul composant à rendre, puis placer la route attrape-tout tout à la fin (afin qu'elle ne l'utilise pas avant que le `Router` n'ait une chance de vérifier le reste des chemins), de sorte que quelque chose se rendra toujours même si les autres chemins ne correspondent pas.

## onEnter

Auparavant, vous pouviez utiliser `onEnter` pour vous assurer que le composant de la `Route` dispose de toutes les informations dont il a besoin ou comme vérification (par exemple, pour vous assurer que l'utilisateur est authentifié) avant que le composant ne se rende.

Cette fonctionnalité a été abandonnée car la nouvelle structure des Routes est qu'elles doivent agir comme des composants, vous devez donc profiter des méthodes du cycle de vie des composants à la place.

Dans React Router v3 :

`<Route path="about" onEnter={fetchedInfo} component={Team}/>`

Devient :

```
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

<Router>
    <Switch>
       <Route exact path ="/" component={Home} />
       <Route path="/about/team" component={Team} />
       <Route path="/about" component={About} />
       <Route component={NotFound} />
    </Switch>
</Router>
```

```
...

componentDidMount() {
    this.props.fetchInfo();
}

...
```

---

# Props

Dans React Router v4, les props transmises via le routeur ont changé, tout comme la manière dont elles sont accessibles. La Route transmet désormais trois props :

* `history`
* `location`
* `match`

## history

`history` contient beaucoup d'autres propriétés et méthodes, donc je ne vais pas toutes les lister, mais voici une sélection de celles qui pourraient être les plus couramment utilisées :

* `length` : nombre d'entrées dans la pile d'historique
* `location` : contient les mêmes informations que ci-dessous
* `push(path, [state])` : pousse une nouvelle entrée sur la pile d'historique
* `goBack()` : permet de déplacer le pointeur sur la pile d'historique d'une entrée en arrière

Il est important de noter que `history` est mutable, et bien qu'il contienne une propriété `location`, cette instance de `location` ne doit pas être utilisée car elle pourrait avoir été modifiée. Au lieu de cela, vous voulez utiliser la prop `location` réelle discutée ci-dessous.

## location

La location a les propriétés suivantes :

* `pathname`
* `search`
* `hash`
* `state`

`location.search` est utilisé pour remplacer `location.query` et il doit être analysé. J'ai utilisé `URLSearchParams` pour l'analyser. Ainsi, une URL telle que `https://something.com/about?string='hello'` serait analysée comme suit :

```
...

const query = new URLSearchParams(this.props.location.search)
const string = query.get('string') // string = 'hello'

...
```

De plus, la propriété `state` peut être utilisée pour transmettre l'état spécifique à la `location` des composants via les props. Ainsi, si vous souhaitiez transmettre certaines informations d'un composant à un autre, vous pourriez l'utiliser comme ceci :

```
...
// Pour lier à un autre composant, nous pourrions faire ceci :
<Link to='/path/' />

// Cependant, si nous voulions ajouter un état à la location, nous pourrions faire ceci :
const location = {
    pathname: '/path/',
    state: { fromDashboard: true },
}
<Link to={location} />
...
```

Ainsi, une fois que nous arrivons au composant rendu par ce chemin, nous aurons accès à `fromDashboard` depuis `location.state.fromDashboard`.

## match

`match` a les propriétés suivantes :

* `params` : obtient les segments dynamiques du chemin à partir de l'URL — par exemple, si le chemin est `/about/:id`, dans le composant, l'accès à `this.props.match.params` vous donnera l'id dans l'URL
* `isExact` : vrai si l'URL entière a été correspondante
* `path` : le chemin dans les routes qui a été correspondante
* `url` : la portion correspondante de l'URL

# Intégration Redux

Comme je l'ai mentionné précédemment, nous avons constaté que dans notre cas, nous n'avions pas besoin d'avoir une bibliothèque supplémentaire pour connecter `redux` avec notre routeur, surtout puisque notre principal cas d'utilisation pour cela — Mises à jour bloquées — était couvert par react router.

## Mises à jour bloquées

Dans certains cas, l'application ne se met pas à jour lorsque l'emplacement change. Cela s'appelle une Mise à jour bloquée. Cela peut se produire si ces deux conditions sont remplies :

1. Le composant est connecté à Redux via `connect()(Component)`.
2. Le composant n'est pas rendu par un `<Route>`

Dans ces cas, j'ai enveloppé la connexion du composant avec `withRouter`.

Cela a permis aux informations du routeur de suivre le composant lorsqu'il est lié, afin que l'application se mette toujours à jour lorsque l'état Redux change.

---

Et c'est tout !

Cette mise à niveau m'a pris plus d'une semaine — quelques jours pour essayer de comprendre comment la faire, et ensuite quelques jours de plus pour commencer à faire des changements. Passer à React Router 4 est un énorme changement à ne pas prendre à la légère, mais cela rendra votre routeur beaucoup plus léger et facile à utiliser.

N'hésitez pas à commenter/poser des questions !