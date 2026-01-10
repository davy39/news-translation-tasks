---
title: Un guide du bluffeur pour React Router v4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T16:29:41.000Z'
originalURL: https://freecodecamp.org/news/bluffers-guide-to-react-router-v4-20f607a10478
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Lf1qdyphgejovy6uvWWRw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Un guide du bluffeur pour React Router v4
seo_desc: 'By Greg Byrne

  In this article, we''ll cover the important things you can quickly learn to be informed
  and confident with using and conversing on React Router v4.

  What is React Router?

  React Router is a client-side router (CSR) for use with React proje...'
---

Par Greg Byrne

Dans cet article, nous aborderons les choses importantes que vous pouvez apprendre rapidement pour être informé et confiant dans l'utilisation et la discussion sur React Router v4.

## Qu'est-ce que React Router ?

React Router est un routeur côté client (CSR) pour une utilisation avec des projets React (_je sais, évidemment, non ?_). Il fournit un _routage_, qui est le terme sophistiqué pour le rendu de différents composants en fonction des chemins d'URL dans une application web React.

## Comment installer et utiliser ?

Exécutez la commande suivante dans votre projet pour enregistrer `react-router-dom` comme une dépendance du projet :

```
npm i -S react-router-dom
```

En utilisant la syntaxe ES2015, vous pouvez importer React Router dans vos composants React en utilisant :

```
import * from 'react-router-dom'
```

### Configuration de vos routes de base

Les composants `Link` peuvent être considérés comme vos liens d'ancrage typiques qui, lorsqu'ils sont cliqués, redirigent l'utilisateur vers le chemin spécifié dans sa propriété `to`.

Les composants `Route` peuvent être considérés comme le contrôleur pour le rendu. Lorsque vous voyez ces composants, pensez simplement qu'ils disent ceci :

QUAND _je vois l'URL comme ce qui est spécifié dans ma_ propriété `path`, _ALORS je vais rendre le composant listé dans ma_ propriété `component` _ou_ `render`.

L'exemple de base ci-dessous est principalement tiré de [l'exemple de base de ReactTraining](https://reacttraining.com/react-router/web/example/basic) :

### Imbrication des routes

L'imbrication des routes est exactement la même que la création de routes de haut niveau, à l'exception de la définition d'un composant `BrowserRouter` (car vos routes imbriquées sont composées dans le composant `BrowserRouter` de haut niveau de toute façon). Il suffit simplement de plus de composants `Link` et `Route`. Nous pouvons imbriquer indéfiniment d'autres routes dans n'importe quelle autre route imbriquée.

### Passage de paramètres d'URL

Dans l'exemple précédent, nous avions différents composants définis pour chaque sujet dans les routes imbriquées. Dans l'exemple suivant, nous avons un seul composant `Topic` qui est rendu pour les trois routes différentes. Le composant `Topic` rend dynamiquement le `topicId`, qui est passé comme une propriété par le `Route`, et sa valeur définie comme partie de l'URL en utilisant le `:`.

Lorsque qu'un `Route` définit un composant à rendre, il passe un objet `match` à ses props (ainsi que `location` et `history`, mais sans importance pour l'instant). Cet objet `match` a un objet `params` qui contient toutes les variables passées par `Route` définies en utilisant la notation `:` dans l'URL du `path` (aka Paramètre de Route).

De cette manière, nous pouvons réduire la création séparée de composants pour chaque `Link` et à la place créer un composant réutilisable rendu avec les informations qui lui sont passées.

### Éviter le codage en dur des liens imbriqués

Lors de la création de liens imbriqués, notre composant `Link` doit encore se référer à l'ensemble du chemin d'URL au lieu de l'emplacement qui le concerne vraiment. Cela signifie que les liens imbriqués auraient des emplacements codés en dur vers leurs liens parents, ce qui n'est pas idéal lorsqu'un changement de nom se produit et qu'un effort de renommage important est nécessaire.

Au lieu de cela, en utilisant l'objet `match` passé par `Route`, nous pouvons nous référer dynamiquement à son emplacement et l'utiliser pour éviter le codage en dur.

Par exemple :  
`<Route path="/topics" component={Topics`}/> passe un objet `match` avec une propriété `url` avec la valeur "/topics" .` Topics , via ses props, peut réutiliser `match.url` lors de la définition de ses liens imbriqués.

### Éviter les correspondances ambiguës

Par défaut, lorsque vous spécifiez des composants `Route`, _chaque chemin correspondant sera rendu de manière inclusive_. En utilisant des paramètres d'URL, cela devient problématique. Comme le paramètre agit effectivement comme un joker (donc tout texte est trouvé comme correspondant), vous constaterez que lorsque ceux-ci sont mélangés avec des routes codées en dur, ils s'afficheront tous les deux. L'utilisation de `exact` n'aidera pas non plus.

La solution de React Router est le composant `Switch`. Le composant `Switch` rendra le composant enfant `Route` sur le _premier chemin correspondant de manière exclusive_. Cela signifie que si toutes les routes codées en dur sont spécifiées en premier, alors celles-ci seront rendues uniquement.

### Rendu multiple de Route

Il arrive que vous ne vouliez pas de correspondance ambiguë des composants `Route`, mais il y aura des moments où vous en aurez besoin.

En vous souvenant que nous pouvons penser à `Route` comme un simple "_QUAND je vois ce chemin, ALORS je rends ce composant_", ce qui signifie que nous pouvons avoir plusieurs composants `Route` correspondant à une seule page, mais fournissant un contenu différent.

Dans l'exemple ci-dessous, nous utilisons un composant pour passer le paramètre d'URL afin de montrer à l'utilisateur leur chemin actuel, et un autre composant qui rend avec le composant de contenu. Cela signifie que deux composants différents sont rendus pour le même chemin d'URL.

### Rendu directement à partir de Route

Un composant `Route` peut recevoir un `component` à rendre si disponible. Il peut également rendre un composant directement en utilisant la propriété `render`.

```
<Route exact path={url} render={  () => <h3>Veuillez sélectionner un sujet</h3>} />
```

### Passage de propriétés à un composant en utilisant Route

Les paramètres passés par URL sont bien, mais qu'en est-il du passage de propriétés qui nécessitent plus de données aux composants, comme des objets ? `Route` ne vous permet pas d'ajouter des propriétés qu'il ne reconnaît pas.

```
<Route exact path="/" component={Home} doSomething={() => "doSomething" } /> // ne fonctionne pas
```

Cependant, ce qui peut être fait pour passer des propriétés est d'utiliser la méthode _render_ de `Route`.

```
<Route exact path="/" render={(props) => <Home {...props} doSomething={() => "doSomething"} />
```

### Passage de propriétés à un composant en utilisant Link

Vous pouvez également passer des propriétés à un composant via le composant `Link`. Au lieu de passer une chaîne de caractères à la propriété `to`, nous pouvons passer un objet à la place. Sur cet objet, nous pouvons déclarer le `pathname` représentant l'URL vers laquelle nous voulons naviguer. Nous déclarons également un objet `state` qui contient toutes les propriétés personnalisées que nous voulons. Ces propriétés sont contenues dans l'objet `location` (dans `location.state`).

Dans l'exemple ci-dessous (_artificiel, je sais..._), nous passons une propriété de message à afficher sur une page.

### Redirection — Utilisation de Redirect

Vous pouvez utiliser le composant `Redirect` pour rediriger l'URL immédiate des utilisateurs vers une autre.

Dans l'exemple ci-dessous, nous voyons une redirection pour un utilisateur selon que l'état `isAuthenticated` sur le composant `RedirectExample` est vrai ou faux, redirigeant de manière appropriée s'ils sont connectés (vers _/home_) ou déconnectés (vers _/dashboard_) :

### Redirection — Utilisation de withRouter()

Une autre façon de rediriger est d'utiliser le composant d'ordre supérieur `withRouter`. Cela vous permet de passer les propriétés de `Route` (`match`, `location`, et surtout dans cet exemple `history`) à des composants qui _ne sont pas_ rendus via le composant `Route` typique. Nous faisons cela en _enveloppant_ notre composant exporté avec `withRouter`.

Pourquoi est-il important d'avoir `history` ? Nous pouvons utiliser `history` pour forcer la redirection en poussant une URL vers l'objet `history`.

Il y a des mises en garde à cette façon de router que je ne détaille pas (voir la [documentation withRouter](https://reacttraining.com/react-router/web/api/withRouter)). De plus, le composant exporté doit toujours être composé dans un autre composant qui est rendu dans `BrowserRouter` (que je ne montre pas dans cet exemple).

### Composant de Route par défaut

Il y aura des moments où un `Link` peut faire référence à une URL qui n'a pas de `<Route path='/something' component={Something`}/> correspondant. Ou un utilisateur tapera une URL incorrecte dans la barre du navigateur.

Lorsque cela se produit, tout ce que nous aurons est une page ou un lien non réactif où rien ne se passe (ce qui n'est pas aussi grave que d'être réellement dirigé vers une page inexistante).

La plupart du temps, nous voulons au moins montrer à l'utilisateur que nous ne pouvons pas trouver leur contenu, peut-être avec une image spirituelle comme [la page 404 de Github](https://github.com/non-existing-page). Dans ce cas, vous voudrez un composant par défaut, également connu sous le nom de composant de non-correspondance ou de capture.

Lorsque qu'un utilisateur clique sur un lien (ou tape quelque chose d'incorrect dans la barre de navigation du navigateur), tant qu'il n'y a pas d'autres composants correspondants, nous serons dirigés vers le composant par défaut à rendre.

Notez l'utilisation de `Switch` (correspondance ambiguë avec les paramètres d'URL). Comme ce `Route` n'a pas de chemin, il sera effectivement toujours rendu. Nous avons besoin d'un `Switch` pour ne rendre que s'il ne peut pas trouver d'autres chemins `Route` correspondants.

### Liens personnalisés

Le composant `Link` à sa base rend un élément d'ancrage pour tout ce qui est passé comme sa propriété `to`. Il arrive que nous voulions des personnalisations apportées au composant Link sans avoir à avoir ces personnalisations partout. React Router permet un moyen de faire cela en créant un lien personnalisé (voir [le guide de formation React Router](https://reacttraining.com/react-router/web/example/custom-link) pour plus d'informations — nous utilisons leur exemple plus ou moins ci-dessous).

Pour un lien personnalisé, on enveloppe essentiellement le composant `Link` existant à l'intérieur d'un composant personnalisé, et on fournit des informations supplémentaires, un peu comme le [modèle de composant d'ordre supérieur](https://reactjs.org/docs/higher-order-components.html).

Dans notre exemple, nous ne montrons les liens que pour les pages qui ne sont pas affichées. Pour que notre composant `CustomLink` ait la connaissance de la page actuellement affichée, nous devons envelopper le composant `Link` dans un composant `Route` afin de pouvoir passer l'objet `match` qui vient avec le `Route` de React Router. Nous passons cet enveloppement de notre composant `Link` en tant qu'enfant au composant `Route`.

Route, si vous vous souvenez, vérifie simplement le chemin actuel et, lorsque nous correspondons, rendra "quelque chose" (soit défini par les propriétés `component`/`render` ou en tant qu'enfant de `Route` — comme notre composant Link).

Nous détournons légèrement cela avec une vérification d'égalité pour dire que si nous ne trouvons pas d'objet `match` (si notre chemin actuel ne correspond pas à ce qui est défini dans la propriété `path` dans le `Route` déclaré dans `CustomLink`), alors nous rendons un `Link`, sinon nous ne rendons rien.

### Analyse des chaînes de requête

Les chaînes de requête sont des paramètres dans l'URL qui ressemblent à des variables et sont précédées du point d'interrogation (comme `www.example.com/search?name=Greg`).

Je vais retirer le band-aid rapidement — React Router ne vient pas avec un moyen d'analyser les chaînes de requête ?. Il localise cependant les chaînes de requête sous forme de chaîne dans ses propriétés passées, dans `location.search`, où dans l'exemple ci-dessus serait défini comme `search: "?name=Greg"`.

Que faire donc ? Il existe plusieurs façons de résoudre ce problème, y compris réinventer la roue. Je voudrais souligner anecdotiquement le package npm [query string](https://www.npmjs.com/package/query-string) comme solution que j'ai utilisée et qui est devenue mon analyseur de chaînes de requête de facto.

### Inviter les utilisateurs lors de la transition

React Router v4 vient avec un composant `Prompt`, qui, comme vous pouvez le deviner, affiche une invite à l'utilisateur. Cela est utile comme fonctionnalité UX pour les utilisateurs lorsqu'ils sont avertis de la perte potentielle de données de formulaire s'ils quittent la page de formulaire actuelle.

Le modèle de base pour implémenter une invite de navigation consiste à avoir une propriété d'état booléen qui décide s'ils doivent être invités ou non. Cet état est mis à jour via le formulaire en fonction de la présence de valeurs sélectionnées pour un champ de formulaire. Dans le formulaire, vous rendez un composant `Prompt`, en passant deux propriétés : un `when` (qui est votre état booléen défini précédemment) et un `message` à afficher.

Ci-dessous se trouve un exemple (il suit principalement l'exemple de [ReactTraining prevent transitions](https://reacttraining.com/react-router/web/example/preventing-transitions)) :

## Résumé

Dans cet article, vous aurez appris toutes les bases pour utiliser React Router dans vos applications web. Vous devriez même être capable de discuter avec vos nombreux amis et votre famille des joies du routage React.

> Si vous avez aimé cet article, partagez votre appréciation avec un applaudissement amical.

> Si vous n'avez pas aimé cet article et que vous souhaitez exprimer votre ressentiment, vous pouvez le faire en donnant un applaudissement haineux.

> _Les **opinions exprimées** dans cette publication sont celles de l'auteur. Elles ne prétendent pas refléter les **opinions** ou vues de toute organisation ou entreprise à laquelle l'auteur peut être lié._