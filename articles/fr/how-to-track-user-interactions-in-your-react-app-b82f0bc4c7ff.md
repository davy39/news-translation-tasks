---
title: Comment suivre les interactions des utilisateurs dans votre application React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T10:11:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-track-user-interactions-in-your-react-app-b82f0bc4c7ff
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZP7MCxvL4o34z5ku4zY_vw.jpeg
tags:
- name: analytics
  slug: analytics
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment suivre les interactions des utilisateurs dans votre application
  React
seo_desc: 'By Faouzi Oudouh

  Worry not about which Analytics provider you need to gather user interaction within
  your app.

  Instead, worry more about how to gather these interactions.

  A few months ago, I was involved in an Analytics project within a large E-comme...'
---

Par Faouzi Oudouh

Ne vous inquiétez pas de savoir quel fournisseur d'Analytics vous devez utiliser pour recueillir les interactions des utilisateurs dans votre application.

Au lieu de cela, inquiétez-vous davantage de la manière de recueillir ces interactions.

Il y a quelques mois, j'ai été impliqué dans un projet d'Analytics au sein d'une grande organisation de commerce électronique. Cette organisation a une activité basée sur les données où les analytics sont plus importants que tout le reste.

Nous construisions une solution de Datalayer pour contenir toutes les interactions et actions des utilisateurs avant de les envoyer au fournisseur d'Analytics (par exemple, Google Tag Manager). Nous avons construit notre solution DataLayer sans avoir React à l'esprit, car la migration vers React a commencé plus tard.

### C'est l'heure de React !

Nous avons commencé la migration vers React progressivement, ce qui signifie que React était responsable uniquement du rendu de certaines parties de la plateforme. Et j'étais responsable de l'intégration de la solution DataLayer que nous avions déjà construite avec React Land.

Soudain, les difficultés ont commencé à surgir :

* La solution était basée sur jQuery
* Elle était imprévisible
* Elle était difficile à tester et à maintenir
* Partager les connaissances avec d'autres développeurs qui n'avaient pas d'expérience en analytics était effrayant !

J'ai commencé à chercher dans la communauté des solutions prêtes à l'emploi qui répondent à nos besoins. Il n'y avait tout simplement aucune chance.

Et c'est là qu'est venue l'idée de [React-Tracker](https://github.com/faouzioudouh/react-tracker).

Pourquoi [React-tracker](https://github.com/faouzioudouh/react-tracker) ?

* Il est facile à utiliser, tester et maintenir (comme Redux)
* Il peut être utilisé avec n'importe quel fournisseur d'Analytics
* Il est scalable et prévisible
* Il a une API minimale

Avec React-tracker, nous avons facilement pu intégrer deux fournisseurs d'Analytics (Google Tag Manager et Adobe Analytics).

### Comment ?

Pour garder cela simple, pensez à cela comme à Redux.

* Instanciez votre Tracker ~ Store de vos événements
* Créez votre/vos écouteur(s) d'événements ~ Reducer
* Événement ~ Action
* Fournissez votre instance de tracker à votre composant racine.
* React-tracker s'occupera [magiquement](https://reactjs.org/docs/context.html) de fournir votre instance de tracker à tous vos composants.

Avant d'instancier quoi que ce soit, passons en revue chaque terme de la liste ci-dessus et expliquons-le.

#### Qu'est-ce qu'un Tracker ?

Un Tracker est un conteneur qui conserve l'historique de suivi ainsi que certaines fonctions pour écouter/envoyer des événements.

* `tracker.on(eventType, callback)` la fonction de rappel donnée sera appelée chaque fois qu'un événement avec `event.type` égal à l'`eventType` donné est envoyé.
* `tracker.trackEvent(event)` est une fonction qui accepte un `event` et appelle tous les écouteurs d'événements qui écoutent cet `event`.
* `tracker.getHistory()` retourne un tableau et contient tous les événements suivis qui ont été sauvegardés

#### Qu'est-ce qu'un Événement ?

Un événement est un objet simple qui représente l'interaction de l'utilisateur, comme un clic de l'utilisateur, une vue de page et un achat.

Il doit être un objet avec `type` et des `data` associés si nécessaire. Voici un exemple d'un événement `PageView` :

```
const PageViewEvent = {  type: 'PAGE_VIEW', // Requis  data: { // Optionnel    pageId: '123',    userId: 'UID-123'  }}
```

#### Qu'est-ce que l'écouteur d'événements ?

L'écouteur d'événements est une fonction qui sera appelée si son `eventType` correspond au type de l'événement envoyé.

`eventListener.eventType === event.type`

Exemple d'un écouteur d'événements :

```
const pageViewListener = (event, ) => {  // Par exemple, poussons l'événement reçu vers notre DataLayer.  window.dataLayer.push(event);
```

```
  return event;};
```

Permettons à notre `pageViewListener` d'écouter uniquement l'événement `PAGE_VIEW` :

```
pageViewListener.eventType = 'PAGE_VIEW';
```

Il y a quatre choses à remarquer ici :

* Retourner l'événement le sauvegardera dans l'historique de suivi. Sinon, il sera ignoré :)
* Si aucun `eventType` n'a été spécifié pour l'écouteur d'événements, il sera appelé à chaque envoi d'événement.
* `eventHistory` a été fourni comme deuxième paramètre pour vous aider à appliquer des restrictions sur vos événements facilement, comme suivre un clic sur un produit une seule fois. Pour y parvenir, vous devez avoir l'historique des événements à portée de main.
* Pousser notre événement vers `window.dataLayer` n'était qu'un exemple. Vous pouvez principalement faire n'importe quoi dans cette fonction, comme appeler `GTM` directement ou `Facebook Pixel`

### Il est temps de combiner tout

Premières choses d'abord :

#### 1. Instanciez notre héros `Tracker` :

```
import { Tracker } from 'react-tracker';
```

```
const tracker = new Tracker();
```

C'est tout !

Maintenant, nous avons notre `Tracker` mais sans écouteur d'événements :-(

Il y a deux façons d'ajouter des écouteurs d'événements à votre `Tracker` :

* Lors de l'instanciation :

```
const anOtherTracker = new Tracker([  pageViewListener,  productClickListener,  ...]);
```

* Ou vous pouvez ajouter l'écouteur d'événements après avoir instancié votre `Tracker` en utilisant `on` :

```
const anOtherTracker = new Tracker();
```

```
tracker.on('PAGE_VIEW', pageViewListener);
```

#### 2. Créez un écouteur d'événements de vue de page :

Je veux que mon écouteur d'événements pousse l'événement `PAGE_VIEW` reçu directement vers mon `dataLayer`.

```
const pageViewListener = (event, trackingHistory) {
```

```
  window.dataLayer.push(event);
```

```
};
```

Faisons connaître notre `tracker` à propos de `pageViewListener` :

```
tracker.on('PAGE_VIEW', pageViewListener);
```

#### 3. Créez un créateur d'événements :

Le créateur d'événements est simplement une fonction qui retourne un objet événement :

```
const pageViewEvent = (pageId, userId) => ({  type: 'PAGE_VIEW',  data: {    pageId,    userId  }});
```

**Notre Tracker est bien configuré maintenant.**

### Présentation de notre `tracker` à React

![Image](https://cdn-media-1.freecodecamp.org/images/5pYC8r-p6vhMiA9nRpopQDn4QK25YObvq7oG)
_Crédit : [rawpixel.com](https://unsplash.com/photos/sHzMcXkJNrw" rel="noopener" target="_blank" title=")_

#### 4. Fournissez notre `tracker` au composant racine :

```
import React from 'react;import ReactDOM from 'react-dom';import { TrackerProvider } from 'react-tracker'
```

```
import RootComponent from '../RootComponent';
```

```
const RootComponentWithTracking = (  <TrackerProvider tracker={tracker}>    <RootComponent />  </TrackerProvider>);
```

```
const domElement = document.getElementById('root');
```

```
ReactDOM.render(<RootComponentWithTracking />, domElement);
```

En fournissant notre `tracker` au composant racine, il sera [magiquement](https://reactjs.org/docs/context.html) disponible pour tous les sous-composants.

Alors maintenant, puisque nous avons notre `tracker` disponible, utilisons-le pour suivre l'événement `PAGE_VIEW` lors du montage du `RootComponent`.

#### 4. Suivez l'événement `Page View`.

```
import React from 'react';import { withTracking } from 'react-tracker';// Nous avons créé cette fonction plus tôt à l'étape (3.)import { pageViewEvent} from '../tracking/events';
```

```
class RootComponent extends React.Component {  componentDidMount() {    this.props.trackPageView(this.props.pageId, this.props.userId)  }
```

```
  render() {    return (<h1> Mon App est géniale </h1>)  }};
```

```
const mapTrackingToProps = trackEvent => ({  trackPageView: (pageId, userId) =>     trackEvent(pageViewEvent(pageId, userId))});
```

```
export default withTracking(mapTrackingToProps)(RootComponent);
```

Le HOC `withTracking` s'occupera de nous fournir `trackEvent` à partir de notre `tracker` afin que nous puissions l'utiliser pour suivre l'événement `pageView`.

`mapTrackingToProps` fusionnera l'objet retourné avec les props du `RootComponent`, ce qui signifie que `trackPageView` sera disponible en tant que prop dans `RootComponent`.

**C'est tout — vous avez terminé ;)**

#### 5. Démo

Veuillez vous référer à cette [démo](https://faouzioudouh.github.io/react-tracker/) et à [GitHub](https://github.com/faouzioudouh/react-tracker) pour une documentation approfondie et une meilleure façon d'organiser vos fichiers de suivi.

### Essayez-le !

[React-tracker](https://github.com/faouzioudouh/react-tracker) a été construit pour faciliter l'intégration des outils d'Analytics autant que possible, en fournissant une API minimale et une intégration facile avec votre application React.

### Remerciements

Merci à [doha faridi](https://www.freecodecamp.org/news/how-to-track-user-interactions-in-your-react-app-b82f0bc4c7ff/undefined), [AbdelAli Eramli](https://www.freecodecamp.org/news/how-to-track-user-interactions-in-your-react-app-b82f0bc4c7ff/undefined) et [khalid benrafik](https://www.freecodecamp.org/news/how-to-track-user-interactions-in-your-react-app-b82f0bc4c7ff/undefined) pour leurs commentaires utiles.