---
title: Réintroduction à React – Chaque Mise à Jour de React Depuis la v16 [Manuel
  Complet]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-02T20:05:07.000Z'
originalURL: https://freecodecamp.org/news/reintroducing-react-every-react-update-since-v16-demystified-60686ee292cc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EFYIS4Y6E3M4fv0BIG3G2w.png
tags:
- name: coding
  slug: coding
- name: handbook
  slug: handbook
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: Réintroduction à React – Chaque Mise à Jour de React Depuis la v16 [Manuel
  Complet]
seo_desc: 'By Emmanuel Ohans

  In this article (and accompanying book), unlike any you may have come across before,
  I will deliver funny, unfeigned and dead serious comic strips about every React
  update since v16+. It’ll be hilarious, either intentionally or unin...'
---

Par Emmanuel Ohans

Dans cet article (et le livre qui l'accompagne), contrairement à tout ce que vous avez pu rencontrer auparavant, je vais vous présenter des bandes dessinées drôles, sincères et très sérieuses sur chaque mise à jour de React depuis la v16+. Ce sera hilarant, soit intentionnellement soit non, accessible aux débutants comme aux professionnels, et très informatif dans l'ensemble.

#### Pourquoi des Bandes Dessinées ?

J'écris des logiciels depuis plus de 5 ans. Mais j'ai aussi fait d'autres choses. J'ai été designer graphique, auteur publié, enseignant, et il y a très longtemps, illustrateur amateur.

J'adore la communauté tech, mais parfois, en tant que groupe, nous avons tendance à être un peu étroits d'esprit.

Quand les gens tentent d'enseigner de nouveaux concepts techniques, ils oublient qui ils étaient avant de devenir développeurs et se contentent de sortir un tas de jargon technique – comme d'autres développeurs qu'ils ont vus.

Quand vous apprenez à connaître les gens, il s'avère que beaucoup d'entre nous ont des parcours très diversifiés ! « Si vous étiez un comédien, pourquoi ne pas expliquer des concepts techniques avec un peu de comédie ?

Ne serait-ce pas génial ?

Je veux montrer comment nous pouvons nous améliorer en tant qu'ingénieurs, en tant qu'équipes, et en tant que communauté, en étant ouvertement nous-mêmes, avec toutes nos bizarreries, et en **enseignant aux autres avec toute cette personnalité**. Mais au lieu de juste parler, je veux le rendre remarquable et montrer l'exemple. Alors, vous êtes les bienvenus dans ma version d'un livre inspiré de bandes dessinées sur chaque mise à jour de React depuis la v16.

Avec les fonctionnalités récemment publiées de la v16.8, il y aura beaucoup de bandes dessinées informatives à livrer !

Inspiré par [Jani Eväkallio](https://twitter.com/jevakallio?lang=en).

> C'est une lecture très intéressante mais longue. [Veuillez télécharger l'ebook](https://leanpub.com/reintroducing-react) (PDF, Epub & Mobi) **absolument gratuit** — sans avoir à partager votre email avec moi. Vous pouvez aussi payer ce que vous voulez pour le livre si vous voulez soutenir mon travail.

#### Comment Lire cet Article

Tout d'abord, [obtenez l'ebook](https://leanpub.com/reintroducing-react). En plus de pouvoir lire hors ligne, les ebooks contiennent des codes avec syntaxe colorée qui les rendent plus faciles à lire. [Allez l'obtenir](https://leanpub.com/reintroducing-react).

![Image](https://cdn-media-1.freecodecamp.org/images/Nb9iorcKIAQebUWfWgs-JhbR289ENJvinibW)
_[https://leanpub.com/reintroducing-react](https://leanpub.com/reintroducing-react" rel="noopener" target="_blank" title=")_

Deuxièmement, veuillez trouver le dépôt de code associé pour le livre sur Github. Cela vous aidera à suivre les exemples permettant une pratique plus concrète.

![Image](https://cdn-media-1.freecodecamp.org/images/YDMVHOQjYMiKVwqh5kWnebHeer10XphxEIIz)

#### Pourquoi Réintroduire React ?

J'ai écrit ma première application React il y a 3 à 4 ans. Entre alors et maintenant, les principes fondamentaux de React sont restés les mêmes. React est tout aussi déclaratif et basé sur les composants aujourd'hui qu'à l'époque.

C'est une bonne nouvelle, cependant, la façon dont nous écrivons les applications React aujourd'hui a changé !

Il y a eu beaucoup de nouvelles additions (et bien, des suppressions).

Si vous avez appris React il y a un certain temps, il n'est pas impossible que vous n'ayez pas été à jour avec chaque nouvelle fonctionnalité/publication. Il est également possible de se perdre parmi toutes les nouvelles fonctionnalités. Par où commencer exactement ? À quel point sont-elles importantes pour votre utilisation quotidienne ?

Même en tant qu'ingénieur expérimenté, je trouve parfois que désapprendre d'anciens concepts et réapprendre de nouveaux est tout aussi intimidant que d'apprendre un nouveau concept à partir de zéro.

Si c'est votre cas, j'espère pouvoir vous apporter l'aide nécessaire via ce guide.

La même chose s'applique si vous apprenez React.

Il y a beaucoup d'informations d'état disponibles. Si vous apprenez React avec une ancienne ressource, oui, vous apprendrez les fondamentaux de React, mais le React moderne a de nouvelles fonctionnalités intéressantes qui méritent votre attention. Il est préférable de les connaître maintenant, et de ne pas avoir à désapprendre et réapprendre de nouveaux concepts.

Que vous écriviez React depuis un certain temps, ou que vous soyez nouveau dans le développement d'applications React, je vais discuter de **chaque** mise à jour de React depuis la version 16.

Cela vous tiendra au courant des changements récents de React, et vous aidera à écrire de meilleurs logiciels.

N'oubliez pas, une réintroduction à React est importante non seulement pour les débutants, mais aussi pour les professionnels. Tout dépend de la manière dont vous avez gardé l'oreille au sol, et vraiment étudié les nombreux changements qui ont été publiés au cours des 12 derniers mois.

Du bon côté, je vous apporte une référence unique pour tous les changements.

Dans ce livre, je vais vous emmener dans un voyage — accompagné d'un peu d'humour et de contenu unique à suivre.

Prêt ?

#### Qu'est-ce qui a changé depuis la version 16 ?

Si vous pensez que pas grand-chose a changé, détrompez-vous.

Voici une liste des changements pertinents que nous allons discuter dans ce guide :

* Nouvelles Méthodes de Cycle de Vie.
* Gestion d'État Simplifiée avec l'API Context.
* ContextType — Utilisation du Contexte sans Consumer.
* Le Profiler : Utilisation de Graphiques et d'Interactions.
* Chargement Paresseux avec React.Lazy et Suspense.
* Functional PureComponent avec React.memo
* Simplification des Applications React avec les Hooks !
* **Modèles de Composants React Avancés avec les Hooks**.

Il va sans dire que beaucoup de choses ont été introduites depuis la version 16. Pour faciliter, chacun de ces sujets a été divisé en sections séparées.

Dans la section suivante, je vais commencer à discuter de ces changements en examinant les nouvelles méthodes de cycle de vie disponibles à partir de la version 16.

### Chapitre 1 : Nouvelles Méthodes de Cycle de Vie.

![Image](https://cdn-media-1.freecodecamp.org/images/ADJ58ZyM2MbBszxgupJp7eX9XnrTXotbsHJR)

Il écrit des logiciels depuis un certain temps, mais il est nouveau dans l'écosystème React.

Faites la connaissance de John.

![Image](https://cdn-media-1.freecodecamp.org/images/hLWHsySy2MjOixddCdxRPK5z9x5qZZWYq9Xm)

Pendant longtemps, il n'a pas complètement compris ce que le cycle de vie signifiait vraiment dans le contexte des applications React.

Quand vous pensez au cycle de vie, à quoi pensez-vous ?

#### Qu'est-ce que le Cycle de Vie, au fait ?

Eh bien, considérons les humains.

![Image](https://cdn-media-1.freecodecamp.org/images/0Y37Fw7u57Bww8eMdVhbZz9mJthSVTF8xAJl)

Le cycle de vie typique d'un humain est quelque chose comme « enfant » à « adulte » à « personne âgée ».

Dans le sens biologique, le cycle de vie fait référence à la série de « changements de forme » qu'un organisme subit.

La même chose s'applique aux composants React. Ils subissent une série de « changements de forme ».

Voici à quoi ressemblerait une représentation graphique simple pour les composants React.

![Image](https://cdn-media-1.freecodecamp.org/images/0ZXhBgvKYzQJ2ktWeLdw8Ep961sWLipbFI0b)

Les quatre phases essentielles ou cycle de vie attribuées à un composant React incluent :

* **Montage** — comme la naissance d'un enfant, à cette phase le composant est créé (votre code, et les internes de React) puis inséré dans le DOM
* **Mise à jour** — comme les humains « grandissent », à cette phase un composant React subit une croissance en étant mis à jour via des changements dans les props ou l'état.
* **Démontage** — Comme la mort d'un humain, c'est la phase où le composant est retiré du DOM.
* **Gestion des Erreurs** — Pensez à cela comme étant comparable à quand les humains tombent malades et vont chez le médecin. Parfois votre code ne s'exécute pas ou il y a un bug quelque part. Quand cela arrive, le composant est dans la phase de gestion des erreurs. J'ai intentionnellement sauté cette phase dans l'illustration précédente.

#### Méthodes de Cycle de Vie.

Maintenant que vous comprenez ce que signifie le cycle de vie, que sont les « méthodes de cycle de vie » ?

Connaître les phases/cycle de vie qu'un composant React traverse est une partie de l'équation. L'autre partie est de comprendre les méthodes que React rend disponibles (ou invoque) à chaque phase.

Les méthodes invoquées pendant différentes phases/cycle de vie d'un composant sont ce qui est populairement connu sous le nom de méthodes de cycle de vie des composants, par exemple. Dans les phases de montage et de mise à jour, la méthode de cycle de vie `render` est toujours invoquée.

Il existe des méthodes de cycle de vie disponibles sur toutes les 4 phases d'un composant — montage, mise à jour, démontage et gestion des erreurs.

Savoir quand une méthode de cycle de vie est invoquée (c'est-à-dire la phase/cycle de vie associée) signifie que vous pouvez écrire la logique associée dans la méthode et savoir qu'elle sera invoquée au bon moment.

Avec les bases hors du chemin, examinons les nouvelles méthodes de cycle de vie disponibles à partir de la version 16.

#### static getDerivedStateFromProps.

Avant d'expliquer comment cette méthode de cycle de vie fonctionne, laissez-moi vous montrer comment la méthode est utilisée.

La structure de base ressemble à ceci :

```
const MyComponent extends React.Component {  ... 
```

```
  static getDerivedStateFromProps() {     // faire des choses ici  }  }
```

La méthode prend `props` et `state` :

```
... 
```

```
  static getDerivedStateFromProps(props, state) {	// faire des choses ici  }  
```

```
...
```

Et vous pouvez soit retourner un objet pour mettre à jour l'état du composant :

```
... 
```

```
  static getDerivedStateFromProps(props, state) {      return {     	points: 200 // mettre à jour l'état avec ceci     }  }  
```

```
  ...
```

Ou retourner null pour ne faire aucune mise à jour :

```
... 
```

```
  static getDerivedStateFromProps(props, state) {    return null  }  
```

```
...
```

Je sais ce que vous pensez. Pourquoi exactement cette méthode de cycle de vie est-elle importante ?

Eh bien, c'est l'une des méthodes de cycle de vie rarement utilisées, mais elle s'avère utile dans certains scénarios.

Tout d'abord, cette méthode est appelée (ou invoquée) **avant** que le composant ne soit rendu dans le DOM lors du montage initial.

Voici un exemple rapide.

Considérons un composant simple qui affiche le nombre de points marqués par une équipe de football.

Comme vous vous en doutez, le nombre de points est stocké dans l'objet d'état du composant :

```
class App extends Component {  state = {    points: 10  }  render() {    return (      <div className="App">        <header className="App-header">          <img src={logo} className="App-logo" alt="logo" />          <p>            Vous avez marqué {this.state.points} points.          </p>        </header>      </div>    );  }}
```

![Image](https://cdn-media-1.freecodecamp.org/images/hfyqbWa079ilh8WNpff4fBknEmgMJY8r3JD7)

Notez que le texte indique _vous avez marqué 10 points_ — où 10 est le nombre de points dans l'objet d'état.

Juste à titre d'exemple, si vous placez la méthode static getDerivedStateFromProps comme montré ci-dessous, quel nombre de points sera rendu ?

```
class App extends Component {  state = {    points: 10  }	  // *******  //  NB: Ce n'est pas la manière recommandée d'utiliser cette méthode. Juste un exemple. Remplacer l'état de manière inconditionnelle ici est généralement considéré comme une mauvaise idée  // ********  static getDerivedStateFromProps(props, state) {    return {      points: 1000    }  }  render() {    return (      <div className="App">        <header className="App-header">          <img src={logo} className="App-logo" alt="logo" />          <p>            Vous avez marqué {this.state.points} points.          </p>        </header>      </div>    );  }}
```

Actuellement, nous avons la méthode de cycle de vie de composant static getDerivedStateFromProps. Si vous vous souvenez de l'explication précédente, cette méthode est appelée avant que le composant ne soit monté dans le DOM. En retournant un objet, nous mettons à jour l'état du composant avant même qu'il ne soit rendu.

Et voici ce que nous obtenons :

![Image](https://cdn-media-1.freecodecamp.org/images/zeyjZq0KXXLe1NcM7DTPaGo7CB45Y1t2Zc4x)

Avec le 1000 provenant de la mise à jour de l'état dans la méthode `static getDerivedStateFromProps`.

Eh bien, cet exemple est artificiel, et ce n'est pas vraiment la manière dont vous utiliseriez la méthode `static getDerivedStateFromProps`. Je voulais juste m'assurer que vous avez compris les bases d'abord.

Avec cette méthode de cycle de vie, juste parce que vous pouvez mettre à jour l'état ne signifie pas que vous devez le faire. Il y a des cas d'utilisation spécifiques pour la méthode `static getDerivedStateFromProps`, sinon vous résoudrez un problème avec le mauvais outil.

Alors, quand devez-vous utiliser la méthode de cycle de vie `static getDerivedStateFromProps` ?

Le nom de la méthode `getDerivedStateFromProps` comprend cinq mots différents, « Get Derived State From Props ».

![Image](https://cdn-media-1.freecodecamp.org/images/2CHM9AEB3-nVWe7YAaaTe4NxVCGc7bWO2i4w)

De plus, l'état du composant de cette manière est appelé État Dérivé.

En règle générale, l'état dérivé doit être utilisé avec parcimonie car vous pouvez introduire des bugs subtils dans votre application si vous n'êtes pas sûr de ce que vous faites.

#### getSnapshotBeforeUpdate.

Dans la phase de mise à jour du composant, juste après que la méthode render est appelée, la méthode de cycle de vie `getSnapshotBeforeUpdate` est appelée ensuite.

Celle-ci est un peu délicate, mais je vais prendre le temps de vous expliquer comment elle fonctionne.

Il est probable que vous n'ayez pas toujours besoin de cette méthode de cycle de vie, mais elle peut s'avérer utile dans certains cas particuliers. Plus précisément lorsque vous devez récupérer des informations du DOM (et potentiellement les modifier) juste après qu'une mise à jour a été effectuée.

Voici l'élément important. La valeur interrogée à partir du DOM dans `getSnapshotBeforeUpdate` fera référence à la valeur juste avant que le DOM ne soit mis à jour. Même si la méthode render a été appelée précédemment.

Une analogie qui pourrait aider concerne l'utilisation des systèmes de contrôle de version tels que git.

Un exemple de base est que vous écrivez du code, et vous mettez en attente vos modifications avant de les pousser vers le dépôt.

Dans ce cas, supposons que la fonction render a été appelée pour mettre en attente vos modifications avant de les pousser réellement vers le DOM. Donc, avant la mise à jour réelle du DOM, les informations récupérées de getSnapshotBeforeUpdate font référence à celles avant la mise à jour visuelle réelle du DOM.

Les mises à jour réelles du DOM peuvent être asynchrones, mais la méthode de cycle de vie `getSnapshotBeforeUpdate` sera toujours appelée immédiatement avant que le DOM ne soit mis à jour.

Ne vous inquiétez pas si vous ne comprenez pas encore. J'ai un exemple pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/unerso1VTE24Qf7YMQqizDGDxGaF94tMQ8xB)

L'implémentation du panneau de chat est aussi simple que vous pouvez l'imaginer. Dans le composant `App`, il y a une liste non ordonnée avec un composant `Chats` :

```
<ul className="chat-thread">    <Chats chatList={this.state.chatList} /> </ul>
```

Le composant `Chats` affiche la liste des chats, et pour cela, il a besoin d'une prop `chatList`. Il s'agit essentiellement d'un tableau. Dans ce cas, un tableau de 3 valeurs de chaîne, "Hey", "Hello", "Hi".

Le composant `Chats` a une implémentation simple comme suit :

```
class Chats extends Component {  render() {    return (      <React.Fragment>        {this.props.chatList.map((chat, i) => (          <li key={i} className="chat-bubble">            {chat}          </li>        ))}      </React.Fragment>    );  }}
```

Il parcourt simplement la prop `chatList` et affiche un élément de liste qui est ensuite stylisé pour ressembler à une bulle de chat :).

Il y a une chose de plus cependant. Dans l'en-tête du panneau de chat se trouve un bouton "Ajouter un chat".

![Image](https://cdn-media-1.freecodecamp.org/images/1m1dDWKV78TsJqLZTkPCkLI0NCCm5WpxguEV)

En cliquant sur ce bouton, un nouveau texte de chat, "Hello", sera ajouté à la liste des messages affichés.

Voici cela en action :

![Image](https://cdn-media-1.freecodecamp.org/images/lz7y-pZgh69oM8Qky58mc7Uy9GNuy-GEm4pw)
_Ajout de nouveaux messages de chat_

Le problème ici, comme avec la plupart des applications de chat, est que chaque fois que le nombre de messages de chat dépasse la hauteur disponible de la fenêtre de chat, le comportement attendu est de faire défiler automatiquement vers le bas le panneau de chat afin que le dernier message de chat soit visible. Ce n'est pas le cas maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/a54HCUsBP3ONIrJvrsiEE1H66BYTAdTZbu0o)
_Je dois faire défiler manuellement pour trouver le message le plus récent_

Voyons comment nous pouvons résoudre ce problème en utilisant la méthode de cycle de vie getSnapshotBeforeUpdate.

La méthode de cycle de vie `getSnapshotBeforeUpdate` fonctionne de telle sorte que lorsqu'elle est invoquée, elle reçoit les props et l'état précédents en tant qu'arguments.

Nous pouvons donc utiliser les paramètres `prevProps` et `prevState` comme montré ci-dessous :

```
getSnapshotBeforeUpdate(prevProps, prevState) {   }
```

Dans cette méthode, vous êtes censé retourner une valeur ou null :

```
getSnapshotBeforeUpdate(prevProps, prevState) {   return value || null // où 'value' est une valeur JavaScript valide    }
```

Quelle que soit la valeur retournée ici est ensuite transmise à une autre méthode de cycle de vie. Vous allez bientôt voir ce que je veux dire.

La méthode de cycle de vie `getSnapshotBeforeUpdate` ne fonctionne pas seule. Elle est destinée à être utilisée en conjonction avec la méthode de cycle de vie `componentDidUpdate`.

Quelle que soit la valeur retournée par la méthode de cycle de vie `getSnapshotBeforeUpdate` est transmise comme troisième argument à la méthode `componentDidUpdate`.

Appelons la valeur retournée par `getSnapshotBeforeUpdate`, _snapshot_, et voici ce que nous obtenons ensuite :

```
componentDidUpdate(prevProps, prevState, snapshot) { }
```

La méthode de cycle de vie `componentDidUpdate` est invoquée après que `getSnapshotBeforeUpdate` soit invoquée. Comme pour la méthode getSnapshotBeforeUpdate, elle reçoit les props et l'état précédents comme arguments. Elle reçoit également la valeur retournée par `getSnapshotBeforeUpdate` comme dernier argument.

Voici tout le code nécessaire pour maintenir la position de défilement dans le panneau de chat :

```
getSnapshotBeforeUpdate(prevProps, prevState) {    if (this.state.chatList > prevState.chatList) {      const chatThreadRef = this.chatThreadRef.current;      return chatThreadRef.scrollHeight - chatThreadRef.scrollTop;    }    return null;  }  componentDidUpdate(prevProps, prevState, snapshot) {    if (snapshot !== null) {      const chatThreadRef = this.chatThreadRef.current;      chatThreadRef.scrollTop = chatThreadRef.scrollHeight - snapshot;    }  }
```

Permettez-moi de vous expliquer ce qui se passe là.

Voici la fenêtre de chat :

![Image](https://cdn-media-1.freecodecamp.org/images/OzgLAOVGpmNxBigrESPZYjEqWZvPr1j93kfh)
_La fenêtre de chat complète_

Cependant, le graphique ci-dessous met en évidence la région réelle qui contient les messages de chat (la liste non ordonnée, `ul` qui abrite les messages).

![Image](https://cdn-media-1.freecodecamp.org/images/CHWDBo14-MfxpwtFUUkDjDN2Mwoq6eW-wuRq)
_La région réelle contenant les messages de chat_

C'est cette `ul` que nous maintenons une référence à l'aide d'une Référence React :

```
<ul className="chat-thread" ref={this.chatThreadRef}>   ...</ul>
```

Tout d'abord, parce que `getSnapshotBeforeUpdate` peut être déclenché pour des mises à jour via n'importe quel nombre de props ou même une mise à jour d'état, nous enveloppons le code dans une conditionnelle qui vérifie s'il y a effectivement un nouveau message de chat :

```
getSnapshotBeforeUpdate(prevProps, prevState) {    if (this.state.chatList > prevState.chatList) {      // écrire la logique ici    }  }
```

La méthode `getSnapshotBeforeUpdate` ci-dessus doit encore retourner une valeur. Si aucun message de chat n'a été ajouté, nous allons simplement retourner `null` :

```
getSnapshotBeforeUpdate(prevProps, prevState) {    if (this.state.chatList > prevState.chatList) {      // écrire la logique ici    }      return null }
```

Maintenant, considérons le code complet pour la méthode `getSnapshotBeforeUpdate` :

```
getSnapshotBeforeUpdate(prevProps, prevState) {    if (this.state.chatList > prevState.chatList) {      const chatThreadRef = this.chatThreadRef.current;      return chatThreadRef.scrollHeight - chatThreadRef.scrollTop;    }    return null;  }
```

Est-ce que cela a du sens pour vous ?

Pas encore, je suppose.

Tout d'abord, considérons une situation où la hauteur totale de tous les messages de chat ne dépasse pas la hauteur du panneau de chat.

![Image](https://cdn-media-1.freecodecamp.org/images/c0Zb3kxJmFNPmbiPP6tlCgrbWcAJ7BIpSf9L)

Ici, l'expression `chatThreadRef.scrollHeight - chatThreadRef.scrollTop` sera équivalente à `chatThreadRef.scrollHeight - 0`.

Quand cela est évalué, cela sera égal à la `scrollHeight` du panneau de chat — juste avant que le nouveau message ne soit inséré dans le DOM.

Si vous vous souvenez de l'explication précédente, la valeur retournée par la méthode `getSnapshotBeforeUpdate` est passée comme troisième argument à la méthode `componentDidUpdate`. Nous appelons cela snapshot :

```
componentDidUpdate(prevProps, prevState, snapshot) {}
```

La valeur passée ici — à ce moment, est la `scrollHeight` précédente avant la mise à jour du DOM.

Dans le `componentDidUpdate`, nous avons le code suivant, mais que fait-il ?

```
componentDidUpdate(prevProps, prevState, snapshot) {    if (snapshot !== null) {      const chatThreadRef = this.chatThreadRef.current;      chatThreadRef.scrollTop = chatThreadRef.scrollHeight - snapshot;    }  }
```

En réalité, nous faisons défiler le panneau verticalement [de haut en bas](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTop), d'une distance égale à `chatThreadRef.scrollHeight - snapshot` ;

Puisque `snapshot` fait référence à la `scrollHeight` avant la mise à jour, l'expression ci-dessus retourne la `height` du nouveau message de chat plus toute autre hauteur liée à la mise à jour.

Veuillez consulter le graphique ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/hoII8SAxbI6PJoKCgKovHu3ontCBLXb-xplp)

Lorsque toute la hauteur du panneau de chat est occupée par des messages (et déjà défilée un peu), la valeur `snapshot` retournée par la méthode `getSnapshotBeforeUpdate` sera égale à la hauteur réelle du panneau de chat.

Le calcul de `componentDidUpdate` définira la valeur `scrollTop` à la somme des hauteurs des messages supplémentaires - exactement ce que nous voulons.

![Image](https://cdn-media-1.freecodecamp.org/images/aqEisKIrxOuOCQKOePljWG15E9GGXOu9CWG1)

Oui, c'est tout.

Si vous êtes bloqué, je suis sûr que le fait de parcourir l'explication (une fois de plus) ou de vérifier le code source aidera à clarifier vos questions.

#### Les Méthodes de Cycle de Vie de Gestion des Erreurs.

Parfois, les choses tournent mal, des erreurs sont lancées. Les méthodes de cycle de vie des erreurs sont invoquées lorsqu'une erreur est lancée par un composant descendant, c'est-à-dire un composant en dessous d'eux.

Implémentons un composant simple pour attraper les erreurs dans l'application de démonstration. Pour cela, nous allons créer un nouveau composant appelé `ErrorBoundary`.

Voici l'implémentation la plus basique :

```
import React, { Component } from 'react';class ErrorBoundary extends Component {  state = {};  render() {    return null;  }}export default ErrorBoundary;
```

Maintenant, intégrons les méthodes de cycle de vie des erreurs.

#### static getDerivedStateFromError.

Chaque fois qu'une erreur est lancée dans un composant descendant, cette méthode est appelée en premier, et l'erreur lancée est passée en tant qu'argument.

Toute valeur retournée par cette méthode est utilisée pour mettre à jour l'état du composant.

Mettons à jour le composant `ErrorBoundary` pour utiliser cette méthode de cycle de vie.

```
import React, { Component } from "react";
```

```
class ErrorBoundary extends Component {  state = {};
```

```
  static getDerivedStateFromError(error) {    console.log(`Journal d'erreur de getDerivedStateFromError: ${error}`);    return { hasError: true };  }
```

```
  render() {    return null;  }}
```

```
export default ErrorBoundary;
```

Maintenant, chaque fois qu'une erreur est lancée dans un composant descendant, l'erreur sera enregistrée dans la console, `console.error(error)`, et un objet est retourné par la méthode `getDerivedStateFromError`. Cela sera utilisé pour mettre à jour l'état du composant ErrorBoundary, c'est-à-dire avec `hasError: true`.

#### componentDidCatch.

La méthode `componentDidCatch` est également appelée après qu'une erreur dans un composant descendant soit lancée. En plus de l'erreur lancée, elle reçoit un autre argument qui représente plus d'informations sur l'erreur :

```
componentDidCatch(error, info) {}
```

Dans cette méthode, vous pouvez envoyer l'`error` ou `info` reçu à un service de journalisation externe. Contrairement à `getDerivedStateFromError`, le `componentDidCatch` permet des effets secondaires :

```
componentDidCatch(error, info) {	logToExternalService(error, info) // ceci est autorisé.         //Où logToExternalService peut faire un appel API.}
```

Mettons à jour le composant `ErrorBoundary` pour utiliser cette méthode de cycle de vie :

```
import React, { Component } from "react";
```

```
class ErrorBoundary extends Component {  state = { hasError: false };  static getDerivedStateFromError(error) {    console.log(`Journal d'erreur de getDerivedStateFromError: ${error}`);    return { hasError: true };  }  componentDidCatch(error, info) {    console.log(`Journal d'erreur de componentDidCatch: ${error}`);    console.log(info);  }  render() {    return null  }}export default ErrorBoundary;
```

De plus, puisque le `ErrorBoundary` ne peut attraper les erreurs que des composants descendants, nous aurons le composant rendre ce qui est passé en tant que `Children` ou rendre une interface utilisateur d'erreur par défaut si quelque chose ne va pas :

```
... render() {    if (this.state.hasError) {      return <h1>Quelque chose s'est mal passé.</h1>;    }
```

```
    return this.props.children; }
```

J'ai simulé une erreur JavaScript chaque fois que vous ajoutez un 5ème message de chat.

Jetez un coup d'œil à la limite d'erreur en action :

![Image](https://cdn-media-1.freecodecamp.org/images/7BtaANRXqMdWT3gmpWAAfpk4l5kOtAHhiPyP)

#### Conclusion.

Il est important de mentionner que bien que de nouvelles additions aient été faites aux méthodes de cycle de vie des composants, certaines autres méthodes telles que `componentWillMount`, `componentWillUpdate`, `componentWillReceiveProps` ont été dépréciées.

![Image](https://cdn-media-1.freecodecamp.org/images/-k1Wn8Tyztlbj-iQi1JG5R9URhy4M5PZOsIl)
_Méthodes de cycle de vie dépréciées_

Maintenant, vous êtes à jour sur les changements apportés aux méthodes de cycle de vie des composants depuis la version 16 de React !

### Chapitre 2 : Gestion d'État Simplifiée avec l'API Context.

![Image](https://cdn-media-1.freecodecamp.org/images/hkHwd2gLDsTYazf2aSM5EuPUTH5RvqoUHnMJ)

John est un développeur incroyable, et il aime ce qu'il fait. Cependant, il est fréquemment confronté au même problème lors de l'écriture d'applications React.

![Image](https://cdn-media-1.freecodecamp.org/images/BasI49K5JaDLjeNq-W2ttxwZpcKjJZKY5ysr)
_Props drilling_

**Props drilling**, le terme utilisé pour décrire le passage de props inutilement à travers une arborescence de composants profondément imbriqués, a tourmenté John depuis un certain temps !

Heureusement, John a une amie qui a toujours toutes les réponses. Espérons qu'elle puisse suggérer une solution.

John contacte Mia, et elle intervient pour offrir quelques conseils.

![Image](https://cdn-media-1.freecodecamp.org/images/h5fhv1i9F8pGKAwhUoIe78RVCPI6bPDHEmPB)
_Mia dit, 'essaie Redux ou MobX'._

Mia est une ingénieure fabuleuse également, et elle suggère d'utiliser une bibliothèque de gestion d'état telle que `Redux` ou `MobX`.

Ce sont de bons choix, cependant, pour la plupart des cas d'utilisation de John, il les trouve un peu trop volumineux pour ses besoins.

« _Ne puis-je pas avoir quelque chose de plus simple et natif à React lui-même_ », dit John.

Mia se lance dans une recherche désespérée pour aider un ami dans le besoin, et elle trouve l'API Context.

![Image](https://cdn-media-1.freecodecamp.org/images/TsMolzLtPQlrPVEjJDm95t8VF3H6y6IvKb0v)

Mia recommande d'utiliser l'API Context de React pour résoudre le problème. John est maintenant heureux, excité de voir ce que l'API Context pourrait offrir, et il se met au travail de manière productive.

Cela marque le début de l'expérience de John avec l'API Context.

#### Introduction au Context.

L'API Context existe pour faciliter le partage de données considérées comme « globales » au sein d'une arborescence de composants.

Regardons un exemple illustré avant de plonger dans l'écriture de code.

Eh bien, John a commencé à travailler avec l'API Context et a été surtout impressionné jusqu'à présent. Aujourd'hui, il a un nouveau projet sur lequel travailler, et il a l'intention d'utiliser l'API context.

Voyons en quoi consiste ce nouveau projet.

![Image](https://cdn-media-1.freecodecamp.org/images/jZg7XLI0pwdpiRkAftIRJu7I6ZP32I3pdJHx)
_Le nouveau projet : Benny Home Run_

John est censé construire un jeu pour un nouveau client. Ce jeu s'appelle **Benny Home Run**, et cela semble être un bon endroit pour utiliser l'API Context.

Le seul but du jeu est de déplacer Benny de sa position de départ à sa nouvelle maison.

![Image](https://cdn-media-1.freecodecamp.org/images/41X58zNSpcIFa-a5qIXo3CVlICGAoPaYwHLB)
_Le but du jeu_

Pour construire ce jeu, John doit suivre la position de Benny.

Puisque la position de Benny est une partie si intégrale de l'ensemble de l'application, elle pourrait tout aussi bien être suivie via un état global de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/YCZQJwydNektrDR5gZ2IBwuCuZ-JRWUwJQOA)
_Suivi des valeurs de position x et y dans l'état_

Ai-je dit « état global de l'application » ?

Oui !

Cela semble être un bon ajustement pour l'API Context.

Alors, comment John peut-il construire cela ?

![Image](https://cdn-media-1.freecodecamp.org/images/goXVPDOBLY69Gaf0NgifcVoilXOcZro-NWyy)

Tout d'abord, il est nécessaire d'importer la méthode `createContext` de `React`

```
import {createContext} from 'react';
```

La méthode `createContext` vous permet de créer ce qui est appelé un objet de contexte. Considérez cela comme la structure de données qui alimente la récupération et la sauvegarde des valeurs d'état.

Pour créer un objet de contexte, vous invoquez la méthode `createContext` avec (ou sans) une valeur d'état initiale à sauvegarder dans l'objet de contexte.

```
createContext(initialStateValue)
```

Voici à quoi cela ressemble dans l'application Benny :

```
const BennyPositionContext = createContext({ 	x: 50, 	y: 50 })
```

La méthode `createContext` est invoquée avec une valeur d'état initiale correspondant aux valeurs de position initiales (x et y) pour Benny.

Cela a l'air bien !

Mais, après avoir créé un objet de contexte, comment accédez-vous exactement aux valeurs d'état dans votre application ?

Eh bien, chaque objet de contexte est livré avec un composant `Provider` et `Consumer`.

Le composant `Provider` « fournit » la valeur sauvegardée dans l'objet de contexte à ses enfants, tandis que le composant `Consumer` « consomme » les valeurs de n'importe quel composant enfant.

Je sais que c'était un peu long, alors décomposons-le lentement.

Dans l'exemple de Benny, nous pouvons aller de l'avant et déstructurer le `BennyPositionContext` pour récupérer les composants Provider et Consumer.

```
const BennyPositionContext = createContext({ 	x: 50, 	y: 50 })// obtenir le provider et le consumerconst { Provider, Consumer } = BennyPositionContext
```

Puisque `Provider` fournit la valeur sauvegardée dans l'objet de contexte à ses **enfants**, nous pourrions envelopper un arbre de composants avec le composant `Provider` comme montré ci-dessous :

```
&lt;Provider>   <Root /> // le composant racine pour l'application Benny. </Provider>
```

Maintenant, tout composant enfant dans le composant `Root` aura accès aux valeurs par défaut stockées dans l'objet de contexte.

Considérons l'arborescence de composants suivante pour l'application Benny.

```
<Provider>   <Scene>     <Benny />   &lt;/Scene></Provider>
```

Où `Scene` et `Benny` sont des enfants du composant `Root` et représentent respectivement la scène du jeu et le personnage Benny.

Dans cet exemple, le composant `Scene` ou même le composant `Benny` plus imbriqué aura accès à la valeur fournie par le composant `Provider`.

Il est important de mentionner qu'un `Provider` prend également une prop `value`.

Cette prop `value` est utile si vous souhaitez fournir une valeur autre que la valeur initiale passée lors de la création de l'objet de contexte via `createContext(initialStateValue)`

Voici un exemple où un nouvel ensemble de valeurs est passé au composant `Provider`.

```
<Provider value={x: 100, y: 150}>   <Scene>     <Benny />   &lt;/Scene></Provider>
```

Maintenant que nous avons des valeurs fournies par le composant `Provider`, comment un composant imbriqué tel que `Benny` peut-il consommer cette valeur ?

![Image](https://cdn-media-1.freecodecamp.org/images/Jy-XrFHSMdxF9UXcIxToIWMELABQqFMVtttE)

La réponse simple est d'utiliser le composant `Consumer`.

Considérons que le composant `Benny` est un composant simple qui rend un SVG.

```
const Benny = () => {  return <svg />}
```

Maintenant, dans `Benny`, nous pouvons aller de l'avant et utiliser le composant `Consumer` comme ceci :

```
const Benny = () => {  return <Consumer>  {(position) => <svg /&gt;}</Consumer>}
```

D'accord, que se passe-t-il là ?

Le composant `Consumer` expose une API de prop de rendu, c'est-à-dire que `children` est une fonction. Cette fonction reçoit ensuite des arguments correspondant aux valeurs sauvegardées dans l'objet de contexte. Dans ce cas, l'objet `position` avec les valeurs de coordonnées `x` et `y`.

Il est important de noter que chaque fois que la valeur d'un composant `Provider` change, le composant `Consumer` associé et les enfants seront réaffichés pour garder les valeurs consommées synchronisées.

De plus, un `Consumer` recevra des valeurs du `Provider` le plus proche au-dessus de lui dans l'arborescence.

Considérons la situation suivante :

```
// créer un objet de contexte const BennyPositionContext = createContext({ 	x: 50, 	y: 50 })
```

```
// obtenir le fournisseur et le consommateurconst { Provider, Consumer } = BennyPositionContext
```

```
// envelopper le composant Root dans un Provider&lt;Provider>  <Root />;</Provider>
```

```
// dans Benny, dans Root. const Benny = () => (  <Provider value={x: 100, y: 100}>    // faire ce que vous voulez  </Provider>)
```

Maintenant, avec un nouveau composant fournisseur introduit dans `Benny`, tout `Consumer` dans `Benny` recevra la valeur `{x: 100, y: 100}` et non la valeur initiale de `{x: 50, y: 50}`.

C'est un exemple illustré artificiel, mais il aide à solidifier les fondements de l'utilisation de l'API Context.

Ayant compris les éléments de base nécessaires pour utiliser l'API Context, construisons une application utilisant tout ce que vous avez appris jusqu'à présent, avec des cas d'utilisation supplémentaires discutés.

#### Exemple : L'Application Mini-Banque.

John est un gars polyvalent et concentré. Quand il ne travaille pas sur des projets de son lieu de travail, il s'adonne à des projets parallèles.

L'un de ses nombreux projets parallèles est une application bancaire qu'il pense pourrait façonner l'avenir de la banque. Comment cela ?

J'ai réussi à obtenir le code source de cette application. Vous le trouverez également dans le dépôt de code du livre.

Pour commencer, veuillez installer les dépendances et exécuter l'application en suivant les commandes ci-dessous :

```
cd 02-Context-API/bank-appyarn installyarn start
```

Une fois cela fait, l'application commence par un écran de connexion comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/VAOjsusp1WiPZs5HJC8sMmgYVNiJEmbOYd1T)

Vous pouvez entrer n'importe quelle combinaison de nom d'utilisateur et de mot de passe de votre choix.

Une fois connecté, vous serez présenté avec l'écran principal de l'application montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Z6kaXqVc45pIKNLJZYfEFdWSsU0wQHrvhMil)

Dans l'écran principal, vous pouvez effectuer des actions telles que consulter le solde de votre compte bancaire et effectuer des retraits également.

![Image](https://cdn-media-1.freecodecamp.org/images/RHV3RbXZud6IXE8JkHInhr0gj1qLiFk3p6yV)
_cliquer oui à partir de l'écran précédent affiche le solde du compte_

Notre objectif ici est de gérer l'état dans cette application beaucoup mieux en introduisant le Context de React.

#### Identifier les Props qui sont Drillés.

Le composant racine de l'application s'appelle `Root`, et a l'implémentation suivante :

```
... import { USER } from './api'class Root extends Component {  state = {    loggedInUser: null  }  handleLogin = evt => {    evt.preventDefault()    this.setState({      loggedInUser: USER    })  }  render () {    const { loggedInUser } = this.state    return loggedInUser ? (      &lt;App loggedInUser={loggedInUser} />    ) : (      <Login handleLogin={this.handleLogin} /&gt;    )  }}
```

Si l'utilisateur est connecté, le composant principal `App` est rendu, sinon nous affichons le composant `Login`.

```
... loggedInUser ? (      &lt;App loggedInUser={loggedInUser} />    ) : (   <Login handleLogin={this.handleLogin} />)...
```

Après une connexion réussie (qui ne nécessite aucune combinaison particulière de nom d'utilisateur et de mot de passe), l'`état` de l'application `Root` est mis à jour avec un `loggedInUser`.

```
...handleLogin = evt => {    ...    this.setState({      loggedInUser: USER    })  }...
```

Dans le monde réel, cela pourrait provenir d'un appel `api`.

Pour cette application, j'ai créé un faux utilisateur dans le répertoire `api` qui exporte l'objet utilisateur suivant.

```
export const USER = {  name: 'June',  totalAmount: 2500701}
```

Essentiellement, le `name` et le `totalAmount` du compte bancaire de l'utilisateur sont récupérés et définis dans l'état lorsque vous vous connectez.

Comment l'objet utilisateur est-il utilisé dans l'application ?

Eh bien, considérons le composant principal, `App`. Ce composant est responsable de tout ce qui est rendu dans l'application, à l'exception de l'écran de `Login`.

Voici l'implémentation de cela :

```
class App extends Component {  state = {    showBalance: false  }  displayBalance = () => {    this.setState({ showBalance: true })  }  render () {    const { loggedInUser } = this.props    const { showBalance } = this.state    return (      <div className='App'>            <User loggedInUser={loggedInUser} profilePic={photographer} />	<ViewAccountBalance          showBalance={showBalance}          loggedInUser={loggedInUser}          displayBalance={this.displayBalance}        />        <section>;          <WithdrawButton amount={10000} />          <WithdrawButton amount={5000} /&gt;        </section>        <Charity />      </div>    )  }}
```

C'est beaucoup plus simple que cela en a l'air. Jetez un deuxième coup d'œil !

Le `loggedInUser` est passé en tant que props à `App` depuis `Root`, et est également passé à la fois aux composants `User` et `ViewAccountBalance`.

![Image](https://cdn-media-1.freecodecamp.org/images/g4akMtcB-co2ZRACtlN0C6vbATgsbQRcvu09)

Le composant `User` reçoit la prop `loggedInUser` et la transmet à un autre composant enfant, `Greeting` qui rend le texte, _Welcome, June_.

```
//User.js const User = ({ loggedInUser, profilePic }) => {  return (    <div>      <img  src={profilePic} alt='user' />      <Greeting loggedInUser={loggedInUser} />    </div>  )}
```

De plus, `ViewAccountBalance` prend une prop booléenne `showBalance` qui décide d'afficher ou non le solde du compte. Cela est basculé à `true` lorsque vous cliquez sur le bouton yes.

![Image](https://cdn-media-1.freecodecamp.org/images/1RLdVLjZIkfAntk16bMgIyHNEtDgz8UYLlSz)

```
//ViewAccountBalance.jsconst ViewAccountBalance = ({ showBalance, loggedInUser, displayBalance }) => {  return (    <Fragment>      {!showBalance ? (        <div>          <p>            Would you love to view your account balance?          </p>          <button onClick={displayBalance}>            Yes          </button>        </div>      ) : (        <TotalAmount totalAmount={loggedInUser.totalAmount} />      )}    </Fragment>  )}
```

À partir du bloc de code ci-dessus, voyez-vous également que `ViewAccountBalance` reçoit la prop `loggedInUser` uniquement pour la transmettre à `TotalAmount` ?

![Image](https://cdn-media-1.freecodecamp.org/images/8I2fuTlfwAtBSTpcWD9d8oNMTwlfIXPPWsoN)

`TotalAmount` reçoit cette prop, récupère le `totalAmount` de l'objet utilisateur et affiche le montant total.

Je suis assez sûr que vous pouvez comprendre ce qui se passe dans les extraits de code ci-dessus.

Ayant expliqué le code jusqu'à présent, voyez-vous le perçage de props évident ici ?

`loggedInUser` est passé trop de fois à des composants qui n'ont même pas besoin de le connaître.

Corrigeons cela avec l'API `Context`.

#### Éviter le Perçage de Props avec Context.

Une solution facile est de regarder le composant `Root` où nous avons commencé à passer des props et de trouver un moyen d'introduire un objet de contexte là.

En suivant cette solution, nous pourrions créer un objet de contexte sans valeurs par défaut initiales au-dessus de la déclaration de la classe `Root` :

```
const { Provider, Consumer } = createContext()class Root extends Component {  state = {    loggedInUser: null  }  ... }
```

Ensuite, nous pourrions envelopper le composant principal `App` autour du `Provider` avec une prop de valeur.

```
class Root extends Component {  state = {    loggedInUser: null  }  ...   render () {    ...    return loggedInUser ? (      <Provider value={this.state.loggedInUser}>        <App loggedInUser={loggedInUser} />      </Provider>    ) ...
```

Initialement, la prop `value` du `Provider` sera `null`, mais dès qu'un utilisateur se connecte et que l'`état` est mis à jour dans `Root`, le `Provider` recevra également le `loggedInUser` actuel.

Avec cela fait, nous pouvons importer le `Consumer` où nous voulons et nous débarrasser du passage des props inutilement dans l'arborescence des composants.

Par exemple, voici le `Consumer` utilisé dans le composant `Greeting` :

```
import { Consumer } from '../Root'const Greeting = () => {  return (    <Consumer>      {user => <p>Welcome, {user.name}! </p>;}    </Consumer>  )}
```

Nous pourrions continuer et faire de même partout ailleurs où nous avons passé la prop `loggedInUser` inutilement.

Et l'application fonctionne comme avant, sauf que nous nous sommes débarrassés du passage de `loggedInUser` encore et encore.

#### Isolation des Détails d'Implémentation.

La solution mise en avant ci-dessus fonctionne mais pas sans quelques inconvénients.

Une meilleure solution serait de centraliser la logique de l'état utilisateur et du Provider en un seul endroit.

C'est une pratique assez courante. Laissez-moi vous montrer ce que je veux dire.

Au lieu d'avoir le composant `Root` gérer l'état pour `loggedInUser`, nous allons créer un nouveau fichier appelé `UserContext.js`.

Ce fichier contiendra la logique liée à la mise à jour de `loggedInUser` ainsi qu'exposera un contexte `Provider` et `Consumer` pour s'assurer que `loggedInUser` et toute fonction de mise à jour soient accessibles depuis n'importe où dans l'arborescence des composants.

Ce type de modularité devient important lorsque vous avez de nombreux objets de contexte différents. Par exemple, vous pourriez avoir un objet `ThemeContext` et `LanguageContext` dans la même application.

Extraire ces éléments dans des fichiers et composants séparés s'avère plus gérable et efficace avec le temps.

Considérons ce qui suit :

```
// UserContext.jsimport React, { createContext, Component } from 'react'import { USER } from '../api'const { Provider, Consumer } = createContext()class UserProvider extends Component {  state = {    loggedInUser: null  }  handleLogin = evt => {    evt.preventDefault()    this.setState({      loggedInUser: USER    })  }  render () {    const { loggedInUser } = this.state    return (      <Provider        value={{          user: loggedInUser,          handleLogin: this.handleLogin        }}      >        {this.props.children}      </Provider>    )  }}export { UserProvider as default, Consumer as UserConsumer }
```

Cela représente le contenu du nouveau fichier `context/UserContext.js`. La logique précédemment gérée par le composant `Root` a été déplacée ici.

Remarquez comment il gère toute la logique concernant la valeur d'état `loggedInUser`, et transmet les valeurs nécessaires aux `children` via un `Provider`.

```
...<Provider     value={{       user: loggedInUser,       handleLogin: this.handleLogin      }}     >      {this.props.children}</Provider>...
```

Dans ce cas, la prop `value` est un objet avec la valeur `user`, et la fonction pour la mettre à jour, `handleLogin`.

Remarquez également que le Provider et le Consumer sont tous deux exportés. Cela facilite la consommation des valeurs depuis n'importe quel composant de l'application.

```
export { UserProvider as default, Consumer as UserConsumer }
```

Avec cette configuration découplée, vous pouvez utiliser la valeur d'état `loggedInUser` n'importe où dans votre arborescence de composants, et la mettre à jour depuis n'importe où dans votre arborescence de composants également.

Voici un exemple d'utilisation de cela dans le composant `Greeting` :

```
import React from 'react'import { UserConsumer } from '../context/UserContext'const Greeting = () => {  return (    <UserConsumer>      {({ user }) => <p>Welcome, {user.name}! </p>}    </UserConsumer>  )}export default Greeting
```

Facile, n'est-ce pas ?

Maintenant, j'ai pris la peine de supprimer chaque référence à `loggedInUser` où la prop devait être passée inutilement. Merci, Context !

Par exemple :

```
// avant const User = ({ loggedInUser, profilePic }) => {  return (    <div>      <img src={profilePic} alt='user' />      <Greeting loggedInUser={loggedInUser} />    </div>  )}// après : Greeting consomme UserContext const User = ({profilePic }) => {  return (    <div>      <img src={profilePic} alt='user' />      <Greeting />     </div>  )}export default User
```

Assurez-vous de consulter le dossier de code accompagnant pour l'implémentation finale, c'est-à-dire après avoir supprimé le `loggedInUser` qui était passé inutilement.

#### Mise à jour des valeurs de contexte.

_Qu'est-ce qu'une application bancaire si vous ne pouvez pas faire de retraits, hein ?_

Eh bien, cette application a quelques boutons. Vous cliquez dessus et voilà, un retrait est effectué.

![Image](https://cdn-media-1.freecodecamp.org/images/-o1b6Cx1S97BwM1GzYQ7mjCgyHOxtdVRhFZ2)
_Les boutons de retrait_

Puisque la valeur `totalAmount` réside dans l'objet `loggedInUser`, nous pourrions tout aussi bien avoir la logique pour effectuer des retraits dans le fichier `UserContext.js`.

Rappelons que nous essayons de centraliser toute la logique liée à l'objet utilisateur en un seul endroit.

Pour ce faire, nous allons étendre le `UserProvider` dans `UserContext.js` pour inclure une méthode `handleWithdrawal`.

```
// UserContext.js... handleWithdrawal = evt => {    const { name, totalAmount } = this.state.loggedInUser    const withdrawalAmount = evt.target.dataset.amount
```

Lorsque vous cliquez sur l'un des boutons, nous invoquerons cette méthode `handleWithdrawal`.

À partir de l'objet `evt` de clic passé en argument à la méthode `handleWithdrawal`, nous extrayons ensuite le montant à retirer de l'objet `dataset`.

```
const withdrawalAmount = evt.target.dataset.amount
```

Cela est possible car les deux boutons ont un attribut `data-amount` défini sur eux. Par exemple :

```
<button data-amount=1000 />
```

Maintenant que nous avons écrit la méthode `handleWithdrawal`, nous pouvons l'exposer via la prop `values` passée à `Provider` comme montré ci-dessous :

```
<Provider    value={{       user: loggedInUser,       handleLogin: this.handleLogin       handleWithdrawal: this.handleWithdrawal     }}   >  {this.props.children}</Provider>
```

Maintenant, nous sommes prêts à consommer la méthode `handleWithdrawal` depuis n'importe où dans l'arborescence des composants.

Dans ce cas, notre focus est sur le composant `WithdrawButton`. Allez-y et enveloppez-le dans un `UserConsumer`, déstructurez la méthode `handleWithdrawal` et faites-en le gestionnaire de clic pour les boutons comme montré ci-dessous :

```
const WithdrawButton = ({ amount }) => {  return (    <UserConsumer>      {({ handleWithdrawal }) => (        <button          data-amount={amount}          onClick={handleWithdrawal}        >          WITHDRAW {amount}        </button>      )}    </UserConsumer>  )}
```

![Image](https://cdn-media-1.freecodecamp.org/images/FvzJEuO9sAL6RIJgSZ5a9WznJPMhhXcqrQl6)
_À la connexion, le retrait fonctionne maintenant comme prévu._

Et cela fonctionne !

#### Conclusion

Cela illustre que vous pouvez passer non seulement des valeurs d'état, mais aussi leurs fonctions de mise à jour correspondantes dans un fournisseur de contexte. Celles-ci seront disponibles pour être consommées n'importe où dans votre arborescence de composants.

Ayant fait fonctionner l'application bancaire avec l'API Context, je suis assez sûr que John sera fier des progrès que nous avons accomplis !

### Chapitre 3 : ContextType — Utilisation du Contexte sans Consumer.

![Image](https://cdn-media-1.freecodecamp.org/images/6P3dyJTbFpm4ovPY1u6MtSwKr-lCQ9Ef5y2N)

Jusqu'à présent, John a eu une excellente expérience avec le Context. Grâce à Mia qui a recommandé un tel outil.

Cependant, il y a un petit problème.

À mesure que John utilise plus souvent l'API context, il commence à réaliser un problème.

![Image](https://cdn-media-1.freecodecamp.org/images/p8ELt767Lxgpql6OJUMdrJTrM3-IeVyYcav7)

Lorsque vous avez plusieurs `Consumers` dans un composant, cela entraîne un code très imbriqué, pas très agréable.

Voici un exemple.

En travaillant sur l'application _Benny Home Run_, John a dû créer un nouvel objet de contexte pour maintenir l'état du niveau de jeu de l'utilisateur actuel.

```
// objet de contexte initialconst BennyPositionContext = createContext({ 	x: 50, 	y: 50 })
```

```
// un autre objet de contexte pour le niveau de jeu, c'est-à-dire Niveau 0 - 5 const GameLevelContext = createContext(0)
```

Rappelons qu'il est courant de diviser les données liées en différents objets de contexte pour la réutilisabilité et la performance (en raison du fait que chaque consommateur est réaffiché lorsque les valeurs dans un `Provider` changent)

Avec ces objets de contexte, John utilise les deux composants `Consumer` dans le composant `Benny` comme suit.

```
// récupérer le consommateur pour PositionContextconst { Consumer: PositionConsumer } = BennyPositionContext
```

```
// récupérer le consommateur pour GameLevelContextconst { Consumer: GameLevelConsumer } = GameLevelContext
```

```
// utiliser les deux Consumers ici.const Benny = () => {  return <PositionConsumer>    {position => <GameLevelConsumer>        {gameLevel => <svg /&gt;}    </GameLevelConsumer>}  </PositionConsumer>}
```

Remarquez-vous que la consommation de valeurs des deux objets de contexte entraîne un code très imbriqué ?

Eh bien, c'est l'un des problèmes les plus courants avec la consommation de données avec le composant `Consumer`. Avec plusieurs composants consommateurs, vous commencez à avoir beaucoup d'imbrications.

Alors, que pouvons-nous faire à ce sujet ?

Tout d'abord, lorsque nous apprendrons les Hooks dans un chapitre ultérieur, vous verrez une solution presque parfaite à cela. En attendant, considérons la solution disponible pour les composants `Class` via quelque chose appelé `contextType`.

#### Utilisation d'un Composant de Classe avec contextType.

Pour tirer parti de `contextType`, vous devez travailler avec un composant de classe.

Considérons le composant `Benny` réécrit en tant que composant de classe.

```
// créer un objet de contexteconst { Provider, Consumer } = createContext({ x: 50, y: 50 })// Composant de classeclass Benny extends Component {  render () {    return <Consumer>    {position => <svg />}  &lt;/Consumer>  }}
```

Dans cet exemple, `Benny` consomme les valeurs de contexte initiales `{ x: 50, y: 50 }` de l'objet de contexte.

Cependant, l'utilisation d'un `Consumer` vous oblige à utiliser une API de prop de rendu qui peut conduire à un code imbriqué.

Débarrassons-nous du composant `Consumer` en utilisant la propriété de classe `contextType`.

![Image](https://cdn-media-1.freecodecamp.org/images/-9MBEu7r7Ix1SwRWzIUmnem0PM7j-7iUC9pe)

Faire fonctionner cela est assez facile.

Tout d'abord, vous définissez la propriété `contextType` sur le composant de classe à un objet de contexte.

```
const BennyPositionContext = createContext({ x: 50, y: 50 })// Classe Benny étend le Composant ... // regardez ici ?Benny.contextType = BennyPositionContext 
```

Après avoir défini la propriété `contextType`, vous pouvez aller de l'avant et consommer des valeurs de l'objet de contexte en utilisant `this.context`.

Par exemple, pour récupérer les valeurs de position `{ x: 50, y: 50 }` :

```
class Benny extends Component {  render () {    // regardez ici. Pas d'imbrication !    const position = this.context    return <svg />  }}
```

#### La Solution Parfaite ?

Utiliser la propriété de classe `contextType` est génial, mais ce n'est pas particulièrement la meilleure solution au monde. Vous ne pouvez utiliser qu'un seul `contextType` dans un composant de classe. Cela signifie que si vous devez introduire plusieurs `Consumers`, vous aurez toujours un code imbriqué.

#### Conclusion

La propriété `contextType` résout un peu le problème d'imbrication.

Cependant, lorsque nous discuterons des Hooks dans un chapitre ultérieur, vous verrez à quel point la solution que les hooks offrent est meilleure.

### Chapitre 4 : React.memo === Functional PureComponent.

![Image](https://cdn-media-1.freecodecamp.org/images/571cqFlK3HszMqIiZJpy0gBqveysWJ1rJPDQ)

Il y a quelques semaines, John a refactorisé le composant `Benny` en un `PureComponent`.

Voici à quoi ressemblait son changement :

Eh bien, cela a l'air bien.

Cependant, la seule raison pour laquelle il a refactorisé le composant `Benny` en un composant de classe était qu'il avait besoin d'étendre `React.PureComponent`.

![Image](https://cdn-media-1.freecodecamp.org/images/ziP13p9hVF0bwg2iRIbWX-cPgKHnqlJU2Hx8)

La solution fonctionne, mais que se passerait-il si nous pouvions obtenir le même effet sans avoir à refactoriser de fonctionnel à des composants de classe ?

Refactoriser de grands composants juste parce que vous avez besoin d'une fonctionnalité React spécifique n'est pas la plus agréable des expériences.

#### Comment fonctionne React.memo.

`React.memo` est le remplacement parfait pour le `PureComponent` de classe. Tout ce que vous avez à faire est d'envelopper votre composant fonctionnel dans l'appel de fonction `React.memo` et vous obtenez le comportement exact que donne `PureComponent`.

Voici un exemple rapide :

```
// avant import React from 'react'function MyComponent ({name}) {     return ( <div>        Hello {name}.            </div>    )}export default MyComponent
```

```
// après import React, { memo } from 'react'export default  memo(function MyComponent ({name}) {    return ( <div>        Hello {name}.            </div&gt;    )})
```

Si simple, cela ne pourrait pas être plus facile.

Techniquement, `React.memo` est une fonction d'ordre supérieur qui prend un composant fonctionnel et retourne un nouveau composant mémorisé.

Ainsi, si les props ne changent pas, `react` sautera le rendu du composant et utilisera simplement la valeur mémorisée précédemment.

Avec cette nouvelle information, John refactorise le composant fonctionnel, `Benny` pour utiliser `React.memo`.

#### Gestion des Props Profondément Imbriquées.

`React.memo` effectue une comparaison superficielle des props. Par implication, si vous avez des objets props imbriqués, la comparaison échouera.

Pour gérer de tels cas, `React.memo` prend un deuxième argument, une fonction de vérification d'égalité.

Voici un exemple de base :

```
import React, { memo } from 'react'export default  memo (function MyComponent (props) {      return ( <div>        Hello World from {props.name.surname.short}            </div&gt;    )}, equalityCheck)
```

```
function equalityCheck(prevProps, nextProps) {  // return perform equality check & return true || false}
```

Si la fonction `equalityCheck` retourne `true`, aucun re-rendu n'aura lieu. Cela signifierait que les props actuelles et les props précédentes sont les mêmes. Si vous retournez `false`, alors un re-rendu se produira.

Si vous êtes préoccupé par les éventuels impacts sur les performances d'une comparaison approfondie, vous pouvez utiliser la méthode utilitaire [isEqual](https://lodash.com/docs/4.17.11#isEqual) de lodash.

```
import { isEqual } from 'lodash'function equalityCheck(prevProps, nextProps) {	return isEqual(prevProps, nextProps) }
```

#### Conclusion.

`React.memo` apporte le comportement de `PureComponent` de classe aux composants fonctionnels. Nous avons également examiné l'utilisation de la fonction `equalityCheck`. Si vous utilisez la fonction `equalityCheck`, assurez-vous d'inclure des vérifications pour les props de fonction lorsque cela est applicable. Ne pas le faire est une source courante de bugs dans de nombreuses applications React.

### Chapitre 5 : Le Profiler — Identifier les Goulots d'Étranglement de Performance.

![Image](https://cdn-media-1.freecodecamp.org/images/zWaetnakr8Rws03aoH9p6-Y7CF75XxniARP6)

C'est vendredi et Mia rentre chez elle. Sur le chemin du retour, elle ne peut s'empêcher de se demander.

![Image](https://cdn-media-1.freecodecamp.org/images/T0y1iNNOpJPISg5U9IRpgEifQ7RTQGRY8kj6)

« Qu'ai-je accompli aujourd'hui ? » se dit Mia à elle-même.

Après une longue réflexion, elle arrive à la conclusion qu'elle n'a accompli qu'une seule chose toute la journée.

![Image](https://cdn-media-1.freecodecamp.org/images/FFniQ2ufSTseN1CtbH8b9DEOZj9zVZK75B67)

Eh bien, comment est-il possible que Mia n'ait accompli qu'une seule chose toute la journée ?

Cette « une chose » doit être un exploit digne de ce nom !

Alors, quel était l'accomplissement de Mia pour la journée ?

![Image](https://cdn-media-1.freecodecamp.org/images/PR3kr9PlZMki7Ea0sDH7SG3tbgLP6gDkBwey)

Il s'avère que tout ce que Mia a accompli aujourd'hui était de rester impuissante pendant que son navigateur tentait de charger une page pendant 7 heures !

![Image](https://cdn-media-1.freecodecamp.org/images/p436ow1UJo09-3-IHLllkrye9K3aNwyEjELS)

Quoi ???

#### Mesurer les Performances dans les Applications React.

La performance web est une grande affaire. Personne n'a tout le temps du monde pour attendre des minutes que votre page web se charge.

Afin de mesurer les performances et d'identifier les goulots d'étranglement de performance dans vos applications, il est crucial d'avoir un moyen d'inspecter combien de temps il a fallu à vos composants d'application pour se rendre, et pourquoi ils ont été rendus.

C'est exactement pourquoi le Profiler existe.

Si vous écrivez React depuis un certain temps, vous vous souvenez peut-être du module `react-addons-perf`.

Eh bien, celui-ci a été déprécié au profit du Profiler.

![Image](https://cdn-media-1.freecodecamp.org/images/JSCb7hooD8c0awGqsL5gwBIyU3XLiLmbdXqU)

Avec le Profiler, vous pouvez :

* Collecter des informations de timing sur chaque composant
* Identifier facilement les goulots d'étranglement de performance
* Être sûr d'avoir un outil compatible avec le rendu concurrent

#### Getting Started.

Pour garder cela aussi pragmatique que possible, j'ai mis en place une petite [application](https://github.com/ohansemmanuel/fake-medium) que nous allons profiler ensemble. C'est-à-dire mesurer les performances. Nous allons faire cela avec l'aide du Profiler.

J'appelle l'application _fake-medium_, et elle ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/BKUaV-v1lOJWBCqmYBWQ1t9dGhK-PLhxa13K)
_L'application Fake-medium_

Vous trouverez le code source de l'application dans le dépôt de code de ce livre.

Pour installer les dépendances et exécuter l'application, exécutez les commandes suivantes à partir du répertoire `04-The-Profiler` :

```
cd fake-mediumyarn install yarn start
```

Si vous avez exécuté ces commandes, vous devriez avoir l'application en cours d'exécution dans votre navigateur par défaut, sur le port `3000` ou similaire.

![Image](https://cdn-media-1.freecodecamp.org/images/ArMFy-gNKE3TQnNHb18m087ww9yx7wmT2VZR)
_Application en cours d'exécution sur un port local._

Enfin, ouvrez vos outils de développement Chrome en appuyant sur Command+Option+J (Mac) ou Control+Shift+J (Windows, Linux et Chrome OS).

Ensuite, trouvez l'onglet de l'extension [chrome devtools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) de React et cliquez dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/i0jScYALcHijfkwCh7-4rstjV1R7cMNkVslV)

Vous serez présenté avec deux onglets, éléments et profiler.

Vous avez deviné juste, notre focus est sur l'onglet profiler, alors veuillez cliquer dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/Ea5nQBoaX-Yam1aKnwXogZM4RnSobpwuuwF0)

En faisant cela, vous serez dirigé vers la page suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/n25grg6bFRAZhVz1Pqup5QcaHO3kspVp5pX1)

#### Comment fonctionne le Profiler ?

Le Profiler fonctionne en enregistrant une session d'utilisation réelle de votre application. Lors de cette session d'enregistrement, il collecte des informations sur les composants de votre application et affiche certaines informations intéressantes que vous pouvez exploiter pour trouver des goulots d'étranglement de performance.

Pour commencer, cliquez sur le bouton d'enregistrement.

![Image](https://cdn-media-1.freecodecamp.org/images/475E6wqCElRnsNOj5i3V0zuEjSWu50Znu1zl)

Après avoir cliqué sur 'enregistrer', vous utilisez ensuite votre application comme vous vous attendez à ce qu'un utilisateur le fasse.

Dans ce cas, j'ai cliqué sur le bouton d'applaudissement medium 3 fois !

![Image](https://cdn-media-1.freecodecamp.org/images/ZS2LZOif-tK5y2jDZVzFKEql8DNPUaJcqrge)

Une fois que vous avez terminé d'interagir avec votre application, appuyez sur stop pour voir les informations que le Profiler fournit.

#### Comprendre les Résultats du Profiler.

Sur le côté droit de l'écran du profiler, vous trouverez une représentation visuelle du nombre de commits effectués pendant votre interaction avec votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/Fw0NAsuDAeeQhEVBaUxbvSybbwSgnKnZkh6z)

Conceptuellement, react effectue le travail en 2 phases. La phase de rendu où les composants sont rendus et le DOM virtuel est différencié, et la phase de commit où les changements réels dans le DOM virtuel sont validés dans le DOM.

La représentation graphique que vous voyez sur le côté droit du profiler représente le nombre de commits qui ont été effectués dans le DOM pendant votre interaction avec l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/vt00nWdS03-5irdzKMO2wrz-NzsoC9e2zDN8)

Plus la barre est haute, plus il a fallu de temps à `React` pour rendre les composants dans ce commit.

Dans l'exemple ci-dessus, le Profiler a enregistré trois commits. Cela a du sens puisque j'ai cliqué sur le bouton seulement 3 fois. Donc, il devrait y avoir seulement 3 commits effectués dans le DOM.

De plus, le premier commit a pris beaucoup plus de temps que les deux commits suivants.

Les trois barres représentent les différents commits effectués dans le DOM, et vous pouvez cliquer sur n'importe laquelle pour enquêter sur les métriques de performance pour le commit particulier.

![Image](https://cdn-media-1.freecodecamp.org/images/TvR2Lh4xKXyU1fZ9MBxtVRZUE6xDRZoGcS65)

#### Le Graphique de Flamme.

Après une session d'enregistrement réussie, vous serez présenté avec plusieurs informations différentes sur vos composants.

Tout d'abord, vous avez 3 onglets représentant différents groupes d'informations — chacun lié au commit sélectionné à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/C7RLaaqstiCC3EQX5BqSIqmyXX3bqQgGiOQL)

Le premier onglet représente un graphique de flamme.

Le graphique de flamme affiche des informations sur le temps qu'il a fallu à votre arborescence de composants pour se rendre.

![Image](https://cdn-media-1.freecodecamp.org/images/NNlVjulXdYdxRBKtxJeGfA-CKyg19nbWXQ1x)

Vous remarquerez que chaque composant de votre arborescence d'application est représenté par des barres de longueurs et de couleurs variées.

La longueur d'une barre définit le temps qu'il a fallu au composant (et à ses enfants) pour se rendre.

À en juger par la longueur de la barre, il semble que le composant `Provider` ait pris le plus de temps à se rendre. Cela a du sens puisque le `Provider` est le composant racine principal de l'application, donc le temps représenté ici est le temps pris pour que `Provider` et tous ses enfants se rendent.

Ce n'est que la moitié de l'histoire.

Notez que les couleurs des barres sont différentes.

![Image](https://cdn-media-1.freecodecamp.org/images/xCTIztG-igaUJS0bcwzJp9cazGEFNLhT2Vt2)

Par exemple, `Provider` et quelques autres composants ont une couleur _grise_.

Que signifie cela ?

Eh bien, premièrement, nous investiguons le premier commit effectué dans le DOM pendant l'interaction avec l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/CJj3CvGXLDJw8K4QlhvuSG2mYhXvybzjToQ1)

Les composants avec une couleur grise signifient qu'ils n'ont pas été rendus dans ce commit. Si le composant est grisé, il n'a pas été rendu dans ce commit. Donc, la longueur de la barre ne représente que le temps qu'il a fallu au composant pour se rendre _précédemment_ avant ce commit, c'est-à-dire avant l'interaction avec l'application.

Si vous y réfléchissez, c'est raisonnable.

Après un examen attentif, vous verrez que le seul composant avec une couleur de graphique de flamme différente ici est le composant `Clap`.

![Image](https://cdn-media-1.freecodecamp.org/images/Nxfa35snkv9yqhL7qH8BmnQzLNwl0Cfd1lUa)

Ce composant représente le bouton d'applaudissement Medium qui a été cliqué.

Une barre jaune signifie que le composant a pris le plus de temps à se rendre dans ce commit.

Eh bien, aucun autre composant n'est coloré, ce qui signifie que le bouton `Clap` était le seul composant réaffiché dans ce commit.

C'est parfait !

Vous ne voulez pas cliquer sur le bouton `Clap` et avoir un autre composant réaffiché. Ce serait un coup de performance là.

Dans des applications plus complexes, vous trouverez des graphiques de flamme avec non seulement des barres jaunes et grises. Vous en trouverez certaines avec des barres bleues.

Ce qui est à noter, c'est que les barres jaunes plus longues ont pris plus de temps à se rendre, suivies par les bleues, et enfin les barres grises n'ont pas été réaffichées dans le commit particulier en cours de visualisation.

Il est également possible de cliquer sur une barre particulière pour voir plus d'informations sur pourquoi elle a été rendue ou non, c'est-à-dire les props et l'état passés au composant.

![Image](https://cdn-media-1.freecodecamp.org/images/Zp6admN1LQ-my7sNhTyHOPuIy83tnfEDg4kE)

![Image](https://cdn-media-1.freecodecamp.org/images/68c6x0Hkn1WUsZFUadliBQ4KFieNlHLygSdY)

Pendant le zoom, vous pouvez également cliquer sur les barres de commit en haut pour voir la différence dans les `props` ou `state` à travers chaque rendu de commit.

#### Le Graphique Classé.

Une fois que vous comprenez comment fonctionne le graphique de flamme, le graphique classé devient une promenade de santé.

La deuxième option d'onglet fait référence au graphique classé.

![Image](https://cdn-media-1.freecodecamp.org/images/OzHE40WoR-zj50CdTEzoLtXA-RqwjOfA3HRo)

Le graphique classé affiche chaque composant qui a été rendu dans le commit en cours de visualisation. Il affiche ces composants classés de haut en bas — avec le composant qui a pris plus de temps à se rendre en haut.

Dans cet exemple, nous avons seulement le composant `Clap` affiché dans la vue du graphique classé. C'est correct car nous nous attendons seulement à ce que le composant `Clap` soit réaffiché lors du clic.

![Image](https://cdn-media-1.freecodecamp.org/images/-4zbLrlGiQ7JV7hhz2ZOMrTXcCg730UhzLEF)

Un graphique classé plus complexe peut ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/sSqE66OzdqOUinWUWiX9cVwY3u65gsLToquC)
_Graphique classé d'une application que nous allons profiler ensuite_

Vous pouvez voir comment les barres jaunes plus longues sont là en haut, et les barres bleues plus courtes en bas. Si vous regardez attentivement, vous remarquerez que les couleurs s'estompent lorsque vous allez de haut en bas. Des barres plus jaunes aux barres jaunes pâles, aux barres bleues claires et enfin aux barres bleues.

#### Graphique des Composants.

Chaque fois que vous zoomez sur un composant dans le Profiler, c'est-à-dire en cliquant sur sa barre associée, une nouvelle option apparaît sur la droite.

![Image](https://cdn-media-1.freecodecamp.org/images/24jjhxXViuYu7SwY4pzS-YmM4Kiapn-h6SJN)

**Cliquer sur ce bouton** vous amènera à ce qu'on appelle le graphique des composants.

Le graphique des composants affiche le nombre de fois où un composant particulier a été réaffiché pendant l'interaction enregistrée.

Dans cet exemple, je peux cliquer sur le bouton pour voir le graphique du composant `Clap`.

![Image](https://cdn-media-1.freecodecamp.org/images/NYtuqFfiwdiHnMazAfjh9qu4cSs4u9HmU-Z2)

Cela montre trois barres représentant les trois fois où le composant `Clap` a été réaffiché. Si je voyais une quatrième barre ici, je commencerais à m'inquiéter car j'ai cliqué seulement trois fois et je m'attendais à seulement trois réaffichages.

Si le composant sélectionné n'a pas été réaffiché du tout, vous serez présenté avec l'écran vide ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/r4jafAzBQZq-nNhFsmVR2v-71vFhWcboRcOf)

**NB** : vous pouvez soit voir le graphique des composants en cliquant sur le bouton à l'extrême droite, soit en double-cliquant sur une barre de composant à partir du graphique de flamme ou du graphique classé.

#### Interactions.

Il y a un dernier onglet dans le profiler, et par défaut il affiche un écran vide :

![Image](https://cdn-media-1.freecodecamp.org/images/gK7ayEjVRfzz3a5sku7ySISv97r6llrO4NqS)

**Interactions** vous permettent de taguer les actions effectuées pendant une session d'enregistrement avec un identifiant de chaîne afin qu'elles puissent être surveillées et suivies dans les résultats de profilage.

L'API pour cela est instable, mais voici comment activer les interactions dans vos résultats de profilage.

Tout d'abord, installez le module `scheduler`. À partir de votre terminal, exécutez `yarn add scheduler` dans le répertoire de l'application.

Une fois l'installation terminée, vous devez utiliser la fonction `unstable_trace` exportée par le module comme montré ci-dessous :

```
import { unstable_trace as trace } from 'scheduler/tracing'
```

La fonction est exportée sous le nom `unstable_trace` mais vous pouvez la renommer dans l'instruction d'importation comme je l'ai fait ci-dessus.

La fonction `trace` a une signature similaire à ceci :

```
trace("string identifier", timestamp, () = {})
```

Elle prend un identifiant de chaîne, un horodatage et une fonction de rappel. Idéalement, vous suivez l'interaction que vous souhaitez en la passant dans le rappel.

Par exemple, je l'ai fait dans l'application `fake-medium` :

```
// avant _handleClick () {   // faire quelque chose}
```

```
// après _handleClick () {   trace("Clap was clicked!", window.performace.now(), () => {  	  // faire quelque chose   })}
```

Le clap medium, lorsqu'il est cliqué, appelle la méthode `_handleClick`. Maintenant, j'ai enveloppé la fonctionnalité dans la méthode `trace`.

Voici ce qui se passe lorsque le résultat du profilage est maintenant visualisé :

![Image](https://cdn-media-1.freecodecamp.org/images/rFrMBm33GE-2KV4WKmxx5Z8ZmVcrEDUhTjdw)

Cliquer trois fois enregistre maintenant 3 interactions et vous pouvez cliquer sur n'importe laquelle des interactions pour voir plus de détails à leur sujet.

![Image](https://cdn-media-1.freecodecamp.org/images/xqP3wRyaTYbFwyIMdrrQ26ns3qmdVerQDDDZ)

Les interactions apparaîtront également dans les graphiques de flamme et classés.

![Image](https://cdn-media-1.freecodecamp.org/images/VIdivXfnxkXhPZXQLNz0Ahp8mTDwO-gYM9rF)

#### Exemple : Identifier les Goulots d'Étranglement de Performance dans l'Application Bancaire.

« Hé John, qu'as-tu fait ?!!! », dit Mia en entrant dans le bureau de John.

« J'étais juste en train de profiler l'application bancaire, et elle n'est pas du tout performante », ajoute-t-elle.

John n'était pas surpris. Il n'avait pas passé beaucoup de temps à réfléchir à la performance, mais avec Mia dans son visage, il commence à reconsidérer.

« D'accord, je vais regarder et corriger les goulots d'étranglement que je trouve. Peut-on faire cela ensemble ? », dit John en se disant à lui-même combien Mia serait utile puisque c'est elle qui a repéré le problème.

« Oh, bien sûr », rétorque-t-elle.

Après avoir passé quelques heures, ils ont trouvé et corrigé quelques goulots d'étranglement de performance dans l'application.

Qu'ont-ils fait ? Quelles mesures ont été prises ?

Dans cet exemple, nous allons lancer l'application bancaire et reprendre là où nous nous étions arrêtés dans le chapitre précédent. Cette fois, nous allons corriger les goulots d'étranglement de performance au sein de l'application.

Voici à quoi ressemble à nouveau l'application bancaire :

![Image](https://cdn-media-1.freecodecamp.org/images/7Yzv8gVG3AnyrZh4J0r3Mo4vyNcLRp1Hm7QC)

#### Noter le Comportement Attendu.

Lorsque je dois profiler une application, spécifiquement lors d'une certaine interaction avec une application, j'aime établir la base de ce que j'attends en termes de performance. Ce type d'attente vous aide à garder votre concentration lorsque vous vous plongez dans l'interprétation des résultats du Profiler.

Considérons l'application bancaire que nous voulons profiler. L'interaction dans l'application bancaire est simple. Vous cliquez sur un ensemble de boutons, et le montant du retrait est mis à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/wsUrSq6yFhdypOPmvWWN0YK47-0ElKftTPt2)
_L'interaction de base de l'application_

Maintenant, quel serait le comportement attendu de cette application en termes de re-rendus et de mises à jour ?

Eh bien, pour moi, c'est assez simple.

La seule partie de l'application qui change visuellement est le montant du retrait. Avant de commencer la session de profilage, mon attente pour une application performante sera qu'aucun composant inutile ne soit re-rendu, seulement le composant responsable de la mise à jour du montant total.

![Image](https://cdn-media-1.freecodecamp.org/images/EQ7JvduM5RuBWJdAmA8UsUmzqK1xk2psHuOq)
_Où je m'attends à ce que les re-rendus se produisent. Nulle part ailleurs._

Donnez ou prenez, je m'attendrais à ce que seul le composant `TotalAmount` soit re-rendu, ou tout autre composant directement connecté à cette mise à jour.

Avec cette attente établie, allons-y et profilons l'application.

Les étapes sont les mêmes que celles discutées précédemment. Vous ouvrez vos `devtools`, enregistrez une session d'interaction, et commencez à interpréter les résultats.

Maintenant, j'ai enregistré une session. Dans cette session, tout ce que j'ai fait a été de cliquer sur le bouton « retirer 10 000 $ » 3 fois.

![Image](https://cdn-media-1.freecodecamp.org/images/nJ9QImh8qxEDpRSpoxqRJ4AvbVv886-8NWpD)

Voici le graphique de flamme de la session de profilage :

![Image](https://cdn-media-1.freecodecamp.org/images/ssqiTuWu9mm8YKwjYBS6cfhCabx2DznFkEg8)
_Résultats du graphique de flamme_

Oh mon Dieu ! D'après le graphique ci-dessus, tant de composants ont été re-rendus. Vous voyez les nombreuses couleurs de barres représentées dans le graphique de flamme ?

Cela est loin d'être idéal, alors commençons à résoudre le problème.

#### Interprétation du Graphique de Flamme.

Tout d'abord, considérons ce qui est probablement la racine du problème ici. Par défaut, chaque fois qu'un `Provider` voit sa `value` changée, chaque composant enfant est forcé de se re-rendre. C'est ainsi que le `Consumer` obtient les dernières valeurs de l'objet `context` et reste synchronisé.

Le problème ici est que chaque composant, à l'exception de `Root`, est un enfant de `Provider` — et ils sont tous re-rendus inutilement !

![Image](https://cdn-media-1.freecodecamp.org/images/uEpyKNJFol4T15woTC7xYqulFpPTT5663vXe)
_Tous les composants enfants re-rendus avec un changement dans la valeur du Provider._

Alors, que pouvons-nous faire à ce sujet ?

Certains des composants enfants n'ont pas besoin d'être re-rendus car ils ne sont pas directement connectés au changement.

Tout d'abord, considérons le premier composant enfant, `App`.

![Image](https://cdn-media-1.freecodecamp.org/images/AQurw0t4lQ210joddkcWyiTrKqQjqs2PpiSb)

Le composant `App` ne reçoit aucune `prop` et il ne gère que la valeur d'état `showBalance`.

```
class App extends Component {  state = {    showBalance: false  }  displayBalance = () => {    this.setState({ showBalance: true })  }  render () {    const { showBalance } = this.state    ...  }}
```

Il n'est pas directement connecté au changement, et il est inutile de re-rendre ce composant.

Corrigeons cela en en faisant un `PureComponent`.

```
// avant class App extends Component {  state = {    showBalance: false  } ... }// après class App extends PureComponent {  state = {    showBalance: false  } ... }
```

Ayant fait de `App` un `PureComponent`, avons-nous fait des progrès décents ?

Eh bien, jetez un coup d'œil au nouveau graphique de flamme généré après ce simple changement (en une ligne).

![Image](https://cdn-media-1.freecodecamp.org/images/39wb21xBzdec7MPDtiihvIqhLDOxFNokPfaD)

Pouvez-vous voir cela ?

Beaucoup d'enfants de App ne sont pas re-rendus inutilement, et nous avons maintenant un graphique de flamme plus sain.

Génial !

#### Profiler Différentes Interactions.

Il est facile de supposer que parce que nous avions moins de re-rendus dans l'interaction « montant du retrait », nous avons maintenant une application performante.

Ce n'est pas correct.

App est maintenant un `PureComponent`, mais que se passe-t-il lorsque `App` est rendu en raison d'un changement d'`état` ?

Eh bien, profilons une interaction différente. Cette fois, chargez l'application et profilez l'interaction pour afficher le solde du compte.

![Image](https://cdn-media-1.freecodecamp.org/images/fiErzN0w3LSxjNeMoYkqBZuYKnzQI5PIor25)

Si vous allez de l'avant et profilez l'interaction, nous obtenons un résultat complètement différent.

![Image](https://cdn-media-1.freecodecamp.org/images/qMp4Ks9sIm1nMwkZqcPn8ZqtQ8Ig3dUMr-7P)
_Capture d'écran montrant l'interaction en cours de profilage._

Maintenant, qu'est-ce qui a changé ?

![Image](https://cdn-media-1.freecodecamp.org/images/6vY2o4-trUJgVEOT9xbcAkP4xFitc0sQIUVC)

D'après le graphique de flamme ci-dessus, chaque composant enfant de `App` a été re-rendu. Ils n'avaient rien à voir avec cette mise à jour visuelle, donc ce sont des rendus gaspillés.

NB : Si vous devez vérifier la hiérarchie des composants plus clairement, rappelez-vous que vous pouvez toujours cliquer sur l'onglet éléments :

![Image](https://cdn-media-1.freecodecamp.org/images/1D22MNaRUJ4dNwTMURzFBV9agzNJVAVSyvaB)

Eh bien, puisque ces composants enfants sont des composants fonctionnels, utilisons `React.memo` pour mémoriser les résultats de rendu afin qu'ils ne changent pas sauf s'il y a un changement dans les props.

```
// User.jsimport { memo } from 'react'const User = memo(({ profilePic }) => {  ...})
```

```
// ViewAccountBalance.jsimport { memo } from 'react'const ViewAccountBalance = memo(({ showBalance, displayBalance }) => {      ...})
```

```
// WithdrawButton.jsimport { memo } from 'react'const WithdrawButton = memo(({ amount }) => {    ...  )})
```

Maintenant, lorsque vous faites cela et re-profilez l'interaction, nous obtenons un graphique de flamme beaucoup plus agréable :

![Image](https://cdn-media-1.freecodecamp.org/images/vWFaZzoArl9dpgS1Pnq81szMWgMnTxE5hXGW)

Maintenant, seul `ViewAccountBalance` et d'autres composants enfants sont re-rendus. C'est bien.

Lorsque vous consultez votre graphique de flamme, c'est-à-dire si vous suivez, vous pouvez voir quelque chose de légèrement différent.

Les noms des composants peuvent ne pas être affichés. Vous obtenez le nom générique `Memo` et il devient difficile de suivre quel composant est quoi.

![Image](https://cdn-media-1.freecodecamp.org/images/jvKxSY6aIsr2b5LaoGKexRg3jKOkH0GzvOqz)

Pour changer cela, définissez la propriété `displayName` pour les composants mémorisés.

Voici un exemple.

```
// ViewAccountBalance.jsconst ViewAccountBalance = memo(({ showBalance, displayBalance }) => {  ...})
```

```
// définir le displayName iciViewAccountBalance.displayName = 'ViewAccountBalance'
```

Vous allez de l'avant et faites cela pour tous les composants fonctionnels mémorisés.

#### La Valeur du Provider.

Nous avons presque terminé avec la résolution des fuites de performance dans l'application, cependant, il y a une chose de plus à faire.

L'effet n'est pas très évident dans cette application, mais sera utile lorsque vous rencontrerez plus de cas dans le monde réel, comme dans des situations où un `Provider` est imbriqué dans d'autres composants.

L'implémentation du `Provider` dans l'application bancaire était la suivante :

```
...<Provider    value={{       user: loggedInUser,       handleLogin: this.handleLogin       handleWithdrawal: this.handleWithdrawal     }}   >  {this.props.children}</Provider>...
```

Le problème ici est que nous passons un nouvel objet à la prop `value` à chaque fois. Une meilleure solution serait de garder une référence à ces valeurs via l'état. Par exemple :

```
<Provider value={this.state}>	{this.props.children}</Provider>
```

Faire cela nécessite un peu de refactoring comme montré ci-dessous :

```
// context/UserContext.jsclass UserProvider extends Component {  constructor () {    super()    this.state = {      user: null,      handleLogin: this.handleLogin,      handleWithdrawal: this.handleWithdrawal    }  }  ...  render () {    return <Provider value={this.state}>  		{this.props.children}	</Provider>  }}
```

Assurez-vous de consulter le dossier de code associé si vous avez besoin de plus de clarté sur ce point.

#### Conclusion.

Profiling applications et identifier les fuites de performance est amusant et gratifiant. J'espère que vous avez acquis des connaissances pertinentes dans cette section.

### Chapitre 6 : Chargement Paresseux avec React.Lazy et Suspense.

![Image](https://cdn-media-1.freecodecamp.org/images/f4WHq-CWHVcLzpw3WmDmuTfOdZCbreBf4fRJ)

« Hé John, nous devons examiner le chargement paresseux de certains modules dans l'application Benny », dit Tunde, le manager de John.

John a reçu des retours très positifs de son manager au cours des derniers mois. De temps en temps, Tunde entre dans le bureau avec une nouvelle idée de projet. Aujourd'hui, c'est le chargement paresseux avec `React.Lazy` et `Suspense`.

John n'a jamais chargé paresseusement un module avec React.Lazy et Suspense auparavant. C'est tout nouveau pour lui, alors il se lance dans une étude rapide pour répondre à ce que son manager a demandé.

#### Qu'est-ce que le Chargement Paresseux ?

Lorsque vous regroupez votre application, il est probable que vous ayez l'ensemble de l'application regroupée en un seul gros bloc.

À mesure que votre application grandit, le bundle grandit également.

![Image](https://cdn-media-1.freecodecamp.org/images/-eEQQvR2dpfwYIIW45KUncl6orjYCfsIUSKv)

Pour comprendre le chargement paresseux, voici le cas d'utilisation spécifique que Tunde avait en tête lorsqu'il a discuté avec John.

« Hé John, te souviens-tu que l'application Benny a un écran d'accueil initial ? », dit Tunde.

Par écran d'accueil initial, Tunde faisait référence à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/WLAaGYYoijsLOrcC6jDilA81UbYyiwoREfg3)

C'est le premier écran que l'utilisateur rencontre lorsqu'il visite le jeu Benny. Pour commencer à jouer au jeu, vous devez cliquer sur le bouton « Start Game » pour être redirigé vers la scène de jeu réelle.

« John, le problème ici est que nous avons regroupé tous nos composants React ensemble et ils sont tous servis à l'utilisateur sur cette page. »

« Oh, je vois où tu veux en venir », dit John.

« Au lieu de charger le composant `GameScene` et ses actifs associés, nous pourrions différer le chargement de ceux-ci jusqu'à ce que l'utilisateur clique réellement sur 'Start Game', hein ? », dit John.

Et Tunde a acquiescé avec un « Oui, c'est exactement ce que je veux dire » retentissant.

Le chargement paresseux fait référence au fait de différer le chargement d'une ressource particulière jusqu'à plus tard, généralement lorsque l'utilisateur effectue une interaction qui demande que la ressource soit réellement chargée. Dans certains cas, cela pourrait aussi signifier précharger une ressource.

Essentiellement, l'utilisateur ne reçoit pas le bundle chargé paresseusement servi initialement, mais il est plutôt récupéré beaucoup plus tard à l'exécution.

C'est génial pour les optimisations de performance, la vitesse de chargement initial, etc.

React rend le chargement paresseux possible en employant la syntaxe d'importation dynamique.

Les importations dynamiques font référence à une proposition de syntaxe `tc39` [pour javascript](https://github.com/tc39/proposal-dynamic-import), cependant, avec des transpileurs comme Babel, nous pouvons utiliser cette syntaxe aujourd'hui.

La manière typique et statique d'importer un module ressemble à ceci :

```
import { myModule } from 'awesome-module'
```

Bien que cela soit souhaitable dans de nombreux cas, la syntaxe ne permet pas de charger dynamiquement un module à l'exécution.

Pouvoir charger dynamiquement une partie d'une application Javascript à l'exécution ouvre la voie à des cas d'utilisation intéressants tels que le chargement d'une ressource en fonction de la langue de l'utilisateur (un facteur qui ne peut être déterminé qu'à l'exécution), ou le chargement de certains codes uniquement lorsqu'ils sont susceptibles d'être utilisés par l'utilisateur (gains de performance).

Pour ces raisons (et plus encore), il existe une [proposition](https://github.com/tc39/proposal-dynamic-import) pour introduire la syntaxe d'importation dynamique dans Javascript.

Voici à quoi ressemble la syntaxe :

```
import('path-to-awesome-module')
```

Elle a une syntaxe similaire à une fonction, mais ce n'est vraiment pas une fonction. Elle n'hérite pas de `Funtion.proptotype` et vous ne pouvez pas invoquer de méthodes telles que `call` et `apply`.

Le résultat retourné par l'appel d'importation dynamique est une promesse qui est résolue avec le module importé.

```
import('path-to-awesome-module')	.then(module => {     // faire quelque chose avec le module ici par exemple module.default() pour invoquer l'export par défaut du module. })
```

#### Utilisation de React.lazy et Suspense.

`React.lazy` et `Suspense` rendent l'utilisation des importations dynamiques dans une application React si facile.

Par exemple, considérons le code de démonstration pour l'application Benny ci-dessous :

```
import React from 'react'import Benny from './Benny'import Scene from './Scene'import GameInstructions from './GameInstructions'
```

```
class Game extends Component {  state = {    startGame: false  }  render () {    return !this.state.startGame ?         <GameInstructions /> : 		<Scene />  }}export default Game;
```

En fonction de la propriété d'état `startGame`, soit le composant `GameInstructions` ou `Scene` est rendu lorsque l'utilisateur clique sur le bouton « Start Game ».

`GameInstructions` représente la page d'accueil du jeu et `Scene` la scène entière du jeu lui-même.

Dans cette implémentation, `GameInstructions` et `Scene` seront regroupés ensemble dans la même ressource Javascript.

Par conséquent, même lorsque l'utilisateur n'a pas montré l'intention de commencer à jouer au jeu, nous aurions chargé et envoyé à l'utilisateur le composant `Scene` complexe qui contient toute la logique de la scène de jeu.

Alors, que faisons-nous ?

Déférons le chargement du composant `Scene`.

Voici à quel point `React.lazy` rend cela facile.

```
// avant import Scene from './Scene'
```

```
// maintenant const Scene = React.lazy(() => import('./Scene'))
```

`React.lazy` prend une fonction qui doit appeler une importation dynamique. Dans ce cas, l'appel d'importation dynamique est `import('./Scene')`.

Notez que `React.lazy` s'attend à ce que le module chargé dynamiquement ait une exportation `default` contenant un composant React.

Avec le composant `Scene` maintenant chargé dynamiquement, lorsque l'application est regroupée pour la production, un module séparé (ou fichier javascript) sera créé pour l'importation dynamique `Scene`.

Lorsque l'application se charge, ce fichier javascript ne sera pas envoyé à l'utilisateur. Cependant, s'ils cliquent sur le bouton « Start Game » et montrent l'intention de charger le composant `Scene`, une requête réseau serait faite pour récupérer la ressource du serveur distant.

Maintenant, la récupération depuis le serveur introduit une certaine latence. Pour gérer cela, enveloppez le composant `Scene` dans un composant `Suspense` pour montrer un fallback pour lorsque la ressource est en cours de récupération.

Voici ce que je veux dire :

```
import { Suspense } from 'react'const Scene = React.lazy(() => import('./Scene'))
```

```
class Game extends Component {  state = {    startGame: false  }  render () {    return !this.state.startGame ?         <GameInstructions /> : 		// regardez ici		<;Suspense fallback="<div>loading ...</div>">		  <Scene />		</Suspense>  }}export default Game;
```

Maintenant, lorsque la requête réseau est initiée pour récupérer la ressource `Scene`, nous afficherons un fallback « loading... » grâce au composant `Suspense`.

`Suspense` prend une prop `fallback` qui peut être un balisage comme montré ici, ou un composant React complet par exemple un chargeur personnalisé.

Avec `React.lazy` et `Suspense`, vous pouvez suspendre la récupération d'un composant jusqu'à plus tard, et montrer un fallback pour lorsque la ressource est en cours de récupération.

Comme c'est pratique.

De plus, vous pouvez placer le composant `Suspense` n'importe où au-dessus du composant chargé paresseusement. Dans ce cas, le composant `Scene`.

Si vous aviez également plusieurs composants chargés paresseusement, vous pourriez les envelopper dans un seul composant `Suspense` ou plusieurs, selon votre cas d'utilisation spécifique.

#### Gestion des Erreurs.

Dans le monde réel, les choses se cassent souvent, n'est-ce pas ?

Il est possible que lors du processus de récupération de la ressource chargée paresseusement, une erreur réseau se produise.

Pour gérer un tel cas, assurez-vous d'envelopper vos composants chargés paresseusement dans une _Frontière d'Erreur_.

Vous vous souvenez des frontières d'erreur du chapitre sur les méthodes de cycle de vie ?

Voici un exemple :

```
import { Suspense } from 'react'import MyErrorBoundary from './MyErrorBoundary'const Scene = React.lazy(() => import('./Scene'))class Game extends Component {  state = {    startGame: false  }
```

```
  render () {    return &lt;MyErrorBoundary>         {!this.state.startGame ?            <GameInstructions /> : 		   <Suspense fallback="loading ...">		     <Scene />;		   </Suspense>}		</MyErrorBoundary>  }}export default Game;
```

Maintenant, si une erreur se produit lors de la récupération de la ressource chargée paresseusement, elle sera gérée avec grâce par la frontière d'erreur.

#### Pas d'exportations nommées.

Si vous vous souvenez de la section précédente, j'ai mentionné que `React.lazy` s'attend à ce que l'instruction d'importation dynamique inclue un module avec une **exportation par défaut** étant un composant React.

Pour le moment, `React.lazy` ne supporte pas les exportations nommées. Ce n'est pas entièrement une mauvaise chose, car cela permet de continuer à utiliser le tree shaking afin que vous n'importiez pas de modules réellement inutilisés.

Considérons le module suivant :

```
// MyAwesomeComponents.js export const AwesomeA = () => <div> I am awesome </div> export const AwesomeB = () => <div> I am awesome </div> export const AwesomeC = () => <div> I am awesome </div>
```

Maintenant, si vous essayez d'utiliser `React.lazy` avec une importation dynamique du module ci-dessus, vous obtiendrez une erreur.

```
// SomeWhereElse.js const Awesome = React.lazy(() => import('./MyAwesomeComponents'))
```

Cela ne fonctionnera pas puisque le module `MyAwesomeComponents.js` n'a pas d'exportation par défaut.

Une solution serait de créer un autre module qui exporte l'un des composants comme exportation par défaut.

Par exemple, si j'étais intéressé par le chargement paresseux du composant `AwesomeA` du module `MyAwesomeComponents.js`, je pourrais créer un nouveau module comme ceci :

```
// AwesomeA.js export { AwesomeA as default } from './MyAwesomeComponents'
```

Ensuite, je peux continuer à utiliser efficacement `React.lazy` comme suit :

```
// SomeWhereElse.jsconst AwesomeA = React.lazy(() => import('AwesomeA'))
```

Problème résolu !

#### Fractionnement du code des routes.

Le fractionnement du code préconise qu'au lieu d'envoyer ce gros bloc de code à l'utilisateur en une seule fois, vous pouvez envoyer dynamiquement des blocs à l'utilisateur lorsqu'il en a besoin.

Nous avons examiné le fractionnement de code basé sur les composants dans les exemples précédents, mais une autre approche courante est le fractionnement de code basé sur les routes.

Dans cette méthode, le code est divisé en blocs en fonction des routes de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/AdX6wJOpumuGlg07LGrWXU55cVtu-wcsxGP7)

Nous pourrions également aller plus loin dans notre connaissance du chargement paresseux en fractionnant le code des routes.

Considérons une application React typique qui utilise `react-router` pour la correspondance des routes.

```
const App = () => (  <Router>      <Switch>        <Route exact path="/" component={Home}/>        <Route path="/about" component={About}/>      </Switch>  </Router>);
```

Nous pourrions charger paresseusement les composants `Home` et `About` afin qu'ils ne soient récupérés que lorsque l'utilisateur atteint les routes associées.

Voici comment faire avec `React.Lazy` et `Suspense`.

```
// charger paresseusement les composants de routeconst Home = React.lazy(() => import('./Home'))const About = React.lazy(() => import('./About'))
```

```
// Fournir un fallback avec Suspenseconst App = () => (  <Router&gt;    <Suspense fallback={<div>Loading...</div>}>      <Switch>        <Route exact path="/" component={Home}/>        <Route path="/about" component={About}/>      </Switch>    </Suspense>  </Router>);
```

Facile, hein ?

Nous avons discuté du fonctionnement de `React.Lazy` et `Suspense`, mais sous le capot, le fractionnement de code réel, c'est-à-dire la génération de bundles séparés pour différents modules, est effectué par un bundler, par exemple [Webpack](https://webpack.js.org).

Si vous utilisez `create-react-app`, `Gatsby` ou `Next.js`, alors vous avez déjà cela configuré pour vous.

Configurer cela vous-même est également facile, vous devez simplement ajuster un peu votre configuration `Webpack`.

La documentation officielle de `Webpack` contient un [guide entier](https://webpack.js.org/guides/code-splitting/) sur ce sujet. Le guide peut valoir la peine d'être consulté si vous gérez vous-même les configurations de budding dans votre application.

#### Exemple : Ajout du Chargement Paresseux à l'Application Bancaire.

Nous pouvons ajouter un peu de chargement paresseux à l'application bancaire que nous avons vue dans le Chapitre 2.

Considérons le composant `Root` de l'application :

```
const Root = () => (  <UserProvider>    <UserConsumer>      {({ user, handleLogin }) =>        user ? <App /> : <Login handleLogin={handleLogin} />      }    </UserConsumer>  </UserProvider>)
```

Lorsque l'utilisateur n'est pas connecté, nous affichons la page de connexion, et le composant `App` uniquement lorsque l'utilisateur est connecté.

Nous pourrions charger paresseusement le composant `App`, non ?

C'est très facile. Vous utilisez la syntaxe d'importation dynamique avec `React.lazy` et enveloppez le composant `App` dans un composant `Suspense`.

Voici comment :

```
...const App = React.lazy(() => import('./containers/App'))const Root = () => (  ...  <Suspense fallback='loading...'>     <App /&gt;  </Suspense>)
```

Maintenant, si vous limitez votre connexion réseau pour simuler un réseau 3G lent, vous verrez le texte intermédiaire _"loading..."_ après la connexion.

![Image](https://cdn-media-1.freecodecamp.org/images/IW7iLI-wxcnn9I1L3bHHGzgpipbg6hcsBzPE)

#### Conclusion.

`React.lazy` et `Suspense` sont excellents et très intuitifs à utiliser, cependant, ils ne supportent pas encore le rendu côté serveur.

Il est probable que cela changera dans le futur, mais en attendant, si vous vous souciez du SSR, utiliser [react-loadable](https://github.com/jamiebuilds/react-loadable) est votre meilleur choix pour le chargement paresseux des composants `React`.

### Chapitre 7 : Hooks — Construire des Applications React Plus Simples.

![Image](https://cdn-media-1.freecodecamp.org/images/nSjeot4viuP2OG3F7I3AwlxLakzO5xCuzGV8)

Depuis trois ans, John écrit des applications React, les composants fonctionnels ont été principalement stupides.

![Image](https://cdn-media-1.freecodecamp.org/images/60PnHQsIH-SlznuOqQ84T08blhFnXM3ygp7i)

Si vous vouliez un état local ou d'autres effets secondaires complexes, vous deviez vous tourner vers les composants de classe. Vous refactorisez douloureusement vos composants fonctionnels en composants de classe ou rien d'autre.

C'est un jeudi après-midi ensoleillé, et pendant le déjeuner, Mia présente les Hooks à John.

![Image](https://cdn-media-1.freecodecamp.org/images/zG-t1Hr6vonZBF1NbaepxzXMHLemGS1zhR4x)

Elle parle avec tant d'enthousiasme que cela piqué l'intérêt de John.

De toutes les choses que Mia a dites, une chose a marqué John. « Avec les hooks, les composants fonctionnels deviennent aussi puissants (sinon plus puissants) que vos composants de classe typiques. »

![Image](https://cdn-media-1.freecodecamp.org/images/epxPtULUEPakK0-3-EVfdtK5--vLsIHjVtRi)

C'est une déclaration audacieuse de la part de Mia.

Alors, considérons ce que sont les hooks.

#### Présentation des Hooks.

Début de cette année, 2019, l'équipe React a publié un nouvel ajout, les hooks, à React dans la version `16.8.0.`

Si React était un grand bol de bonbons, alors les hooks sont les derniers ajouts, des bonbons très moelleux avec un excellent goût !

Alors, que signifient exactement les hooks ? Et pourquoi valent-ils votre temps ?

L'une des principales raisons pour lesquelles les hooks ont été ajoutés à React est d'offrir un moyen plus puissant et expressif d'écrire (et de partager) des fonctionnalités entre les composants.

> À long terme, nous nous attendons à ce que les Hooks soient le moyen principal pour les gens d'écrire des composants React — [Équipe React](https://reactjs.org/docs/hooks-faq.html#should-i-use-hooks-classes-or-a-mix-of-both)

Si les hooks vont être si importants, pourquoi ne pas les apprendre de manière amusante !

#### Le Bol de Bonbons.

Considérez React comme un beau bol de bonbons.

![Image](https://cdn-media-1.freecodecamp.org/images/pjja8sdMgoi2fUu1o2PCBoFmo4ihiNtfE7BD)

Le bol de bonbons a été incroyablement utile pour les gens du monde entier.

![Image](https://cdn-media-1.freecodecamp.org/images/1BvN5dNjhTWnvWoQh2jWDyUlyLcSZLT-zlqa)

Les personnes qui ont fait ce bol de bonbons se sont rendu compte que certains des bonbons dans le bol ne faisaient pas beaucoup de bien aux gens.

Quelques bonbons avaient un goût excellent, oui ! Mais ils apportaient une certaine complexité lorsque les gens les mangeaient — pensez aux render props et aux composants d'ordre supérieur ?

![Image](https://cdn-media-1.freecodecamp.org/images/ZuxFKQ3ZKRWVVn982t9Ey8MvL8EQGzfwkoqt)

Alors, que ont-ils fait ?

![Image](https://cdn-media-1.freecodecamp.org/images/CuOhbGjag0VyZ6Un3XfJgdoC5hiugK9V49b0)

Ils ont fait la bonne chose — ne pas jeter tous les bonbons précédents, mais en créer de nouveaux.

Ces bonbons ont été appelés **Hooks**.

![Image](https://cdn-media-1.freecodecamp.org/images/X1P4ajaVzaSiAfXwewXeXNdI5hzMJFyNBNva)

Ces bonbons existent pour un seul but : **faciliter ce que vous faites déjà**.

![Image](https://cdn-media-1.freecodecamp.org/images/m55098wKgv-QFB3zcmy0vL3smJZ9vRaeLDcc)

Ces bonbons ne sont pas super spéciaux. En fait, lorsque vous commencez à les manger, vous réaliserez qu'ils ont un goût familier — ils sont simplement des **fonctions JavaScript** !

![Image](https://cdn-media-1.freecodecamp.org/images/RWmYzL3pHLO8573ms4TNS519-Dy7CGbSfyOb)

Comme tous les bons bonbons, ces 10 nouveaux bonbons ont tous leurs noms uniques. Bien qu'ils soient collectivement appelés **hooks**.

Leurs noms commencent toujours par le mot de trois lettres, use ... par exemple, `useState`, `useEffect`, etc.

Tout comme le chocolat, ces 10 bonbons partagent certains des mêmes ingrédients. Savoir comment l'un a un goût, vous aide à vous rappeler des autres.

Cela semble amusant ? Maintenant, prenons ces bonbons.

#### Le Hook d'État.

Comme mentionné précédemment, les hooks sont des fonctions. Officiellement, il y en a 10. 10 nouvelles fonctions qui existent pour rendre l'écriture et le partage de fonctionnalités dans vos composants beaucoup plus expressifs.

Le premier hook que nous allons examiner s'appelle `useState`.

Pendant longtemps, vous ne pouviez pas utiliser l'état local dans un composant fonctionnel. Eh bien, pas jusqu'aux hooks.

Avec `useState`, votre composant fonctionnel peut avoir (et mettre à jour) un état local.

Comme c'est intéressant.

Considérons l'application de compteur suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/21F0jCXkYSFWmal4Fa3BxhlwaWre7WiBkrpG)

Avec le composant Counter montré ci-dessous :

Simple, hein ?

Permettez-moi de vous poser une question simple. Pourquoi exactement avons-nous ce composant en tant que composant `Class` ?

Eh bien, la réponse est simplement parce que nous devons suivre un certain état local au sein du composant.

Maintenant, voici le même composant refactorisé en un composant fonctionnel avec accès à l'état via les hooks `useState`.

Qu'est-ce qui est différent ?

Je vais vous guider étape par étape.

Un composant fonctionnel n'a pas toute la syntaxe `Class extend ...`.

```
function CounterHooks() {}
```

Il ne nécessite pas non plus de méthode de rendu.

```
function CounterHooks() {    return (      <div>        <h3 className="center">Welcome to the Counter of Life </h3>        <button           className="center-block"           onClick={this.handleClick}> {count} </button>      </div>    ); }
```

Il y a deux problèmes avec le code ci-dessus.

* Vous ne devez pas utiliser le mot-clé `this` dans les composants fonctionnels.
* La variable d'état `count` n'a pas été définie.

Extraire `handleClick` dans une fonction séparée au sein du composant fonctionnel :

```
function CounterHooks() {  const handleClick = () => {   }  return (      <div>        <h3 className="center">Welcome to the Counter of Life </h3>        <button           className="center-block"           onClick={handleClick}> {count} </button>      </div>    ); }
```

Avant le refactoring, la variable count provenait de l'objet d'état du composant de classe.

Dans les composants fonctionnels, et avec les hooks, cela provient de l'invocation de la fonction ou du hook `useState`.

`useState` est appelé avec un argument, la valeur d'état initiale, par exemple, `useState(0)` où 0 représente la valeur d'état initiale à suivre.

L'invocation de cette fonction retourne un tableau avec deux valeurs.

```
//? retourne un tableau avec 2 valeurs. useState(0) 
```

La première valeur étant la valeur d'état actuelle suivie, et la seconde, une fonction pour mettre à jour la valeur d'état.

Pensez à cela comme une sorte de réplique de `state` et `setState` — cependant, ils ne sont pas tout à fait les mêmes.

Avec cette nouvelle connaissance, voici `useState` en action.

```
function CounterHooks() {  // ?   const [count, setCount] = useState(0);  const handleClick = () => {    setCount(count + 1)  }  return (      <div>        <h3 className="center">Welcome to the Counter of Life </h3>        <button           className="center-block"           onClick={handleClick}> {count} </button>      </div>    ); } 
```

Il y a quelques choses à noter ici, en plus de la simplicité évidente du code !

Premièrement, puisque l'invocation de `useState` retourne un tableau de valeurs, les valeurs pourraient être facilement déstructurées en valeurs séparées comme montré ci-dessous :

```
const [count, setCount] = useState(0);
```

De plus, notez comment la fonction `handleClick` dans le code refactorisé n'a pas besoin de référence à `prevState` ou autre chose de ce genre.

Elle appelle simplement `setCount` avec la nouvelle valeur, `count + 1`.

Simple comme cela semble, vous avez construit votre tout premier composant utilisant des hooks. Je sais que c'est un exemple artificiel, mais c'est un bon début !

**NB** : il est également possible de passer une fonction à la fonction de mise à jour d'état. Cela est généralement recommandé comme avec `setState` lorsqu'une mise à jour d'état dépend d'une valeur précédente de l'état, par exemple, `setCount(prevCount => prevCount +` 1)

#### Appels multiples à useState.

Avec les composants de classe, nous nous sommes tous habitués à définir les valeurs d'état dans un objet, qu'elles contiennent une seule propriété ou plus.

```
// propriété unique state = {  count: 0}// propriétés multiples state = { count: 0, time: '07:00'}
```

Avec `useState`, vous avez peut-être remarqué une légère différence.

Dans l'exemple ci-dessus, nous avons seulement appelé `useState` avec la valeur initiale réelle. Pas un objet pour contenir la valeur.

```
useState(0)
```

Alors, que se passe-t-il si nous voulions suivre une autre valeur d'état ?

Peut-on utiliser plusieurs appels à `useState` ?

Considérons le composant ci-dessous. C'est la même application de compteur avec une touche supplémentaire. Cette fois, le compteur suit l'heure du clic.

![Image](https://cdn-media-1.freecodecamp.org/images/y1ygRHiHbm6haOM0uTRin1vZ9VoYMLvG1hYS)

Comme vous pouvez le voir, l'utilisation des hooks est assez similaire, sauf pour un nouvel appel à `useState`.

```
const [time, setTime] = useState(new Date())
```

Maintenant, la variable d'état `time` est utilisée dans le balisage rendu pour afficher l'heure, la minute et la seconde du clic.

```
<p>     at: {`${time.getHours()} : ${time.getMinutes()} :${time.getSeconds()}`}  </p>
```

Génial !

#### Objet comme Valeurs Initiales

Est-il possible d'utiliser un objet avec `useState` plutôt que plusieurs appels à `useState` ?

Absolument !

Si vous choisissez de faire cela, vous devez noter que contrairement aux appels `setState`, les valeurs passées dans `useState` remplacent la valeur d'état.

`setState` fusionne les propriétés de l'objet mais `useState` remplace la valeur entière.

#### Le Hook d'Effet.

Avec les composants de classe, vous avez probablement effectué des effets secondaires tels que la journalisation, la récupération de données ou la gestion des abonnements.

Ces effets secondaires peuvent être appelés « effets » pour faire court, et le hook d'effet, `useEffect` a été créé à cette fin.

Comment est-il utilisé ?

Eh bien, le hook `useEffect` est appelé en lui passant une fonction dans laquelle vous pouvez effectuer vos effets secondaires.

Voici un exemple rapide :

```
useEffect(() => {  // ? vous pouvez effectuer des effets secondaires ici  console.log("useEffect first timer here.")}) 
```

À `useEffect`, j'ai passé une fonction anonyme avec un effet secondaire appelé à l'intérieur.

La question logique suivante est, quand la fonction `useEffect` est-elle invoquée ?

Eh bien, rappelez-vous que dans les composants de classe, vous aviez des méthodes de cycle de vie telles que `componentDidMount` et `componentDidUpdate`.

Puisque les composants fonctionnels n'ont pas ces méthodes de cycle de vie, `useEffect` _kinda_ prend leur place.

Ainsi, dans l'exemple ci-dessus, la fonction à l'intérieur de `useEffect`, également connue sous le nom de fonction d'effet, sera invoquée lorsque le composant fonctionnel est monté (`componentDidMount`) et lorsque le composant est mis à jour (`componentDidUpdate`).

Voici cela en action.

En ajoutant l'appel `useEffect` ci-dessus à l'application de compteur, nous obtenons effectivement le journal de la fonction `useEffect`.

![Image](https://cdn-media-1.freecodecamp.org/images/T9u1mPVp81HSg4s3MsRRiOYc6KRzB1z5tLLv)

Par défaut, la fonction `useEffect` sera appelée après chaque rendu.

**NB** : Le hook `useEffect` n'est pas entièrement le même que `componentDidMount` + `componentDidUpdate`. Il peut être considéré comme tel, mais l'implémentation diffère avec quelques différences subtiles.

#### Passage de Tableaux de Dépendances.

Il est intéressant que la fonction d'effet soit invoquée chaque fois qu'il y a une mise à jour. C'est génial, mais ce n'est pas toujours la fonctionnalité souhaitée.

Que se passe-t-il si vous voulez exécuter la fonction d'effet uniquement lorsque le composant est monté ?

C'est un cas d'utilisation courant et `useEffect` prend un deuxième paramètre, un tableau de dépendances pour gérer cela.

Si vous passez un tableau vide, la fonction d'effet est exécutée uniquement au montage — les re-rendus ultérieurs ne déclenchent pas la fonction d'effet.

```
useEffect(() => {    console.log("useEffect first timer here.")}, [])
```

![Image](https://cdn-media-1.freecodecamp.org/images/KAv1j3znRKI9nnXTHC-VSLHkqHyb-4Cskas7)

Si vous passez des valeurs dans ce tableau, alors la fonction d'effet sera exécutée au montage, et chaque fois que les valeurs passées sont mises à jour. C'est-à-dire, si l'une des valeurs est modifiée, l'appel d'effet sera relancé.

```
useEffect(() => {    console.log("useEffect first timer here.")}, [count])
```

La fonction d'effet sera exécutée au montage, et chaque fois que la fonction count change.

![Image](https://cdn-media-1.freecodecamp.org/images/uDU1DVT8gyC4jce-XQZDT5ftKLMmFMUKCD8T)

Et les abonnements ?

Il est courant de s'abonner et de se désabonner de certains effets dans certaines applications.

Considérons ce qui suit :

```
useEffect(() => {  const clicked = () => console.log('window clicked');  window.addEventListener('click', clicked);}, [])
```

Dans l'effet ci-dessus, lors du montage, un écouteur d'événement de clic est attaché à la fenêtre.

Comment pouvons-nous nous désabonner de cet écouteur lorsque le composant est démonté ?

Eh bien, `useEffect` permet cela.

Si vous retournez une fonction dans votre fonction d'effet, elle sera invoquée lorsque le composant sera démonté. C'est l'endroit parfait pour annuler les abonnements comme montré ci-dessous :

```
useEffect(() => {    const clicked = () => console.log('window clicked');    window.addEventListener('click', clicked);
```

```
    return () =>; {      window.removeEventListener('click', clicked)    } }, [])
```

Il y a beaucoup plus de choses que vous pouvez faire avec le hook useEffect, comme faire des appels API.

#### Construisez vos propres Hooks

Dès le début de la section sur les hooks, nous avons pris (et utilisé) des bonbons de la boîte à bonbons que React fournit.

Cependant, React fournit également un moyen pour vous de créer vos propres bonbons uniques — appelés hooks personnalisés.

Alors, comment cela fonctionne-t-il ?

Un hook personnalisé est simplement une fonction régulière. Cependant, son nom doit commencer par le mot **use** et, si nécessaire, il peut appeler l'un des hooks React à l'intérieur de lui-même.

Voici un exemple :

#### Les Règles des Hooks

Il y a deux règles à respecter lors de l'utilisation des hooks.

* N'appelez les Hooks qu'au [Niveau Supérieur](https://reactjs.org/docs/hooks-rules.html#only-call-hooks-at-the-top-level), c'est-à-dire pas dans des conditionnelles, des boucles ou des fonctions imbriquées.
* N'appelez les Hooks que depuis des Fonctions React, c'est-à-dire des Composants Fonctionnels et des Hooks Personnalisés.

Ce plugin ESLint [plugin](https://www.npmjs.com/package/eslint-plugin-react-hooks) est génial pour vous assurer de respecter ces règles au sein de vos projets.

### Hooks Avancés

Nous n'avons considéré que deux des dix hooks que React fournit !

Ce qui est intéressant, c'est que la connaissance du fonctionnement de `useState` et `useEffect` vous aide à apprendre rapidement les autres hooks.

Curieux d'en apprendre davantage sur ceux-ci, j'ai créé une [feuille de triche sur les hooks](https://github.com/ohansemmanuel/react-hooks-cheatsheet) avec des exemples modifiables en direct.

![Image](https://cdn-media-1.freecodecamp.org/images/uocYYVAXRFmr3pkFzJFxggyNp4dUcMlfr7cc)

Pourquoi cela est important, c'est que vous pouvez immédiatement commencer à bidouiller avec des exemples réels qui renforceront votre connaissance du fonctionnement des hooks. Tous !

Rappelez-vous que l'apprentissage est renforcé lorsque vous résolvez réellement des problèmes et construisez des choses.

Ce qui est encore plus intéressant, c'est que, après avoir parcouru les exemples en direct pour chacun des hooks, il y a une section supplémentaire pour d'autres exemples génériques qui ne correspondent pas exactement à un hook ou nécessitent une étude de cas séparée.

Dans la section des exemples, vous trouverez des [exemples](https://react-hooks-cheatsheet.com/examples/fetching-data) tels que la récupération de données depuis un serveur distant en utilisant des hooks et plus encore.

![Image](https://cdn-media-1.freecodecamp.org/images/GK8XDogOdy6kbKVQ6SI9QfO2qpoNjWWYa3oU)
_Exemple en direct de la feuille de triche._

Allez, [consultez-le](https://github.com/ohansemmanuel/react-hooks-cheatsheet).

### Chapitre 8 : Modèles React Avancés avec les Hooks

![Image](https://cdn-media-1.freecodecamp.org/images/WXlCQiqH7AWqwhgBWCKZuIQ6UXT-v3h-IjRO)

Avec la sortie des hooks, certains modèles React sont tombés en désuétude. Ils peuvent encore être utilisés, mais pour la plupart des cas d'utilisation, vous seriez probablement mieux avec les hooks. Par exemple, choisissez les hooks plutôt que les render props ou les composants d'ordre supérieur.

Il peut y avoir des cas d'utilisation spécifiques où ceux-ci pourraient encore être utilisés, mais la plupart du temps, choisissez les hooks.

Cela dit, nous allons maintenant considérer quelques modèles React plus avancés implémentés avec les hooks.

Prêt ?

#### Introduction

Ce chapitre peut être le plus long du livre, et pour une bonne raison. Les hooks sont probablement la manière dont nous allons écrire les composants React dans les prochaines années, et donc ils sont assez importants.

Dans ce chapitre, nous allons considérer les modèles React avancés suivants :

* Composants Composés
* Collection de Props
* Getters de Props
* Initialisateurs d'État
* Réducteur d'État
* Props de Contrôle

Si vous êtes complètement nouveau dans ces modèles avancés, ne vous inquiétez pas, je vais les expliquer en détail. Si vous êtes familier avec le fonctionnement de ces modèles à partir d'expériences précédentes avec des composants de classe, je vais vous montrer comment utiliser ces modèles avec des hooks.

Maintenant, commençons.

#### Pourquoi des Modèles Avancés ?

John a eu une carrière assez bonne. Aujourd'hui, il est ingénieur frontend senior chez _ReactCorp_. Une grande startup qui change le monde pour le mieux.

_ReactCorp_ commence à développer sa main-d'œuvre. Beaucoup d'ingénieurs sont embauchés et John commence à travailler sur la construction de composants réutilisables pour toute l'équipe d'ingénieurs.

![Image](https://cdn-media-1.freecodecamp.org/images/UndCKKEAhJKf7KUa3Ulf9CmeY7szLAiejuzX)

Oui, John peut construire des composants avec ses compétences actuelles en React, cependant, la construction de composants hautement réutilisables apporte des problèmes spécifiques.

Il y a un million de façons différentes dont les composants peuvent être consommés, et vous voulez donner aux consommateurs du composant autant de flexibilité que possible.

Ils doivent être en mesure d'étendre la fonctionnalité et les styles du composant comme ils le jugent approprié.

Les modèles avancés que nous allons considérer ici sont des méthodes éprouvées pour construire des composants très réutilisables qui ne limitent pas la flexibilité.

Je n'ai pas créé ces modèles avancés. À vrai dire, la plupart des modèles React avancés ont été popularisés par une seule personne, [Kent Dodds](https://kentcdodds.com) — un ingénieur JavaScript incroyable.

La communauté a très bien accueilli ces modèles, et je suis ici pour vous aider à comprendre comment ils fonctionnent !

#### Modèle de Composants Composés

Le premier modèle que nous allons considérer s'appelle le modèle de Composants Composés. Je sais que cela semble sophistiqué, alors je vais expliquer ce que cela signifie vraiment.

Le mot clé dans le nom du modèle est le mot _Composé_.

Littéralement, le mot _composé_ fait référence à quelque chose qui est composé de deux ou plusieurs éléments séparés.

En ce qui concerne les composants React, cela pourrait signifier un composant qui est composé de deux ou plusieurs composants séparés.

Mais ce n'est pas tout.

N'importe quel composant React peut être composé de 2 ou plusieurs composants séparés. Donc, ce n'est pas vraiment une manière brillante de décrire les composants composés.

Avec les composants composés, il y a plus. Les composants séparés au sein desquels le composant principal est composé ne peuvent pas vraiment être utilisés sans le parent.

![Image](https://cdn-media-1.freecodecamp.org/images/oZ7CY7vfHkIbqMLOGtI5DpdPBRWgnP7tGy3J)
_composants composés_

Le composant principal est généralement appelé le parent, et les composants composés séparés, les enfants.

L'exemple classique est de considérer l'élément `html` select.

```
<select>  <option value="value0">key0</option>  <option value="value1">key1</option>  <option value="value2">key2</option></select>
```

Avec `select` étant le parent, et les nombreux éléments `option`, les enfants.

Cela fonctionne comme un composant composé. Pour commencer, cela n'a vraiment aucun sens d'utiliser l'élément `<option>key0<`;/option> sans une balise parent select. Le comportement global d'un élément select repose également sur le fait d'avoir ces éléments option composés.

Ils sont si connectés les uns aux autres.

De plus, l'état de l'ensemble du composant est géré par `select` avec tous les éléments enfants dépendants de cet état.

Avez-vous maintenant une idée de ce que sont les composants composés ?

Il est également important de mentionner que les composants composés ne sont qu'une des nombreuses façons d'exprimer l'API de vos composants.

Par exemple, bien que cela ne semble pas aussi bien, l'élément `select` aurait pu être conçu pour fonctionner comme ceci :

```
<select options="key:value;anotherKey:anotherValue"><;/select>
```

Ce n'est définitivement pas la meilleure façon d'exprimer cette API. Cela rend le passage d'attributs aux composants enfants presque impossible.

Avec cela à l'esprit, examinons un exemple qui vous aidera à comprendre et à construire vos propres composants composés.

#### Exemple : Construction d'un Composant Expandable.

![Image](https://cdn-media-1.freecodecamp.org/images/LSHe4laueTj0qrz7WZcIkNqQfI1txaaszPxo)
_Le composant final en cours d'utilisation_

Nous allons construire un composant `Expandable`. Vous avez demandé ce que cela signifie ?

Eh bien, considérons un composant `Expandable` comme un élément accordéon miniature. Il a un en-tête cliquable, qui bascule l'affichage d'un corps de contenu associé.

Dans l'état non développé, le composant ressemblerait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/xkCEtYIIkTQO0s-imNADZ8tX5ceLMV-zKpdq)

Et ceci, lorsqu'il est développé :

![Image](https://cdn-media-1.freecodecamp.org/images/NdybUeg-Rye1gyZ7yuDYcmREl2hPDflkQxi7)

Vous comprenez l'idée, n'est-ce pas ?

#### Conception de l'API

Il est généralement bon de rédiger à quoi ressemblerait l'API exposée de votre composant avant de le construire.

Dans ce cas, voici ce que nous visons :

```
<Expandable>	<Expandable.Header> Header </Expandable.Header> 	<Expandable.Icon/>    <Expandable.Body> This is the content &lt;/Expandable.Body></Expandable>
```

![Image](https://cdn-media-1.freecodecamp.org/images/gsi8CWO9uvmAh4m33n-MsQTeHS5owZfFezsM)

![Image](https://cdn-media-1.freecodecamp.org/images/EbOV-Qb3ZrK2t87zC9sLtAvq5oWQCLkycWDX)
_Une décomposition des composants enfants_

Dans le bloc de code ci-dessus, vous aurez remarqué que j'ai des expressions comme celle-ci : `Expandable.Header`

Vous pourriez aussi faire ceci :

```
<Expandable>	<Header> Header </Expandable.Header> 	<Icon/>    <Body> This is the content </Body></Expandable>
```

Cela n'a pas d'importance. J'ai choisi `Expandable.Header` plutôt que `Header` par préférence personnelle. Je trouve que cela communique bien la dépendance au composant parent, mais ce n'est que ma préférence. Beaucoup de gens ne partagent pas la même préférence et c'est parfaitement bien.

C'est votre composant, utilisez l'API qui vous semble bonne :)

#### Construction du Composant Expandable

Le composant `Expandable`, étant le composant parent, suivra l'état, et il le fera via une variable booléenne appelée `expanded`.

```
// state {  expanded: true || false}
```

Le composant `Expandable` doit communiquer l'état à chaque composant enfant, quelle que soit leur position dans l'arborescence des composants imbriqués.

Rappelons que les enfants dépendent du composant composé parent pour l'état.

Comment pouvons-nous nous y prendre au mieux ?

Si vous avez dit `context`, vous avez raison !

Nous devons créer un objet `context` pour contenir l'état du composant, et exposer la propriété `expanded` via le composant `Provider`. En plus de la propriété `expanded`, nous exposerons également une fonction de rappel pour basculer la valeur de cette propriété d'état `expanded`.

![Image](https://cdn-media-1.freecodecamp.org/images/Ga1KnN7jSDEPUsyceXFVi4mqGwYjr4fOG1Yz)
_la relation d'état pour le composant expandable_

Si cela vous semble correct, voici le point de départ pour le composant `Expandable`.

```
// Expandable.js import React, { createContext } from 'react'
```

```
const ExpandableContext = createContext()const { Provider } = ExpandableContext
```

```
const Expandable = ({children}) => {  return <Provider>{children}</Provider>}export default Expandable
```

Il ne se passe rien de spectaculaire dans le bloc de code ci-dessus.

Un objet de contexte est créé et le composant `Provider` est déstructuré. Ensuite, nous créons le composant `Expandable` qui rend le `Provider` et tous les `children`.

Vous avez compris ?

Avec la configuration de base hors du chemin, faisons un peu plus.

L'objet de contexte a été créé sans valeur initiale. Cependant, nous avons besoin que le `Provider` expose la valeur d'état `expanded` et une fonction de basculement pour mettre à jour l'état.

Créons la valeur d'état `expanded` en utilisant `useState`.

```
// Expandable.js 
```

```
import React, { createContext, useState } from 'react'...const Expandable = ({children}) => {  // regardez ici ?  const [expanded, setExpanded] = useState(false) 
```

```
  return <Provider>{children}</Provider>}
```

Avec la variable d'état `expanded` créée, créons la fonction de mise à jour `toggle` pour basculer la valeur de `expanded` — qu'elle soit `true` ou `false`.

```
// Expandable.js ...const Expandable = ({children}) => {  const [expanded, setExpanded] = useState(false)  // regardez ici ?  const toggle = setExpanded(prevExpanded => !prevExpanded) 
```

```
  return <Provider>{children}</Provider>}
```

La fonction `toggle` invoque `setExpanded`, la fonction de mise à jour réelle retournée par l'appel `useState`.

Chaque fonction de mise à jour de l'appel `useState` peut recevoir un argument de fonction. Cela est similaire à la manière dont vous passez une fonction à `setState`, par exemple, `setState(prevState => !prevState.val`ue).

C'est la même chose que j'ai faite ci-dessus. La fonction passée à `setExpanded` reçoit la valeur précédente de `expanded` et retourne l'opposé de celle-ci, `!expanded`

`toggle` agit comme une fonction de rappel et elle sera finalement invoquée par `Expandable.Header`. Prévenons tout futur problème de performance en mémorisant le rappel.

```
... import { useCallback } from 'react';
```

```
const Expandable = ({children}) => {  const [expanded, setExpanded] = useState(false)  // regardez ici ?  const toggle = useCallback(    () => setExpanded(prevExpanded => !prevExpanded),    []  ))return <Provider>{children}</Provider> 
```

Vous n'êtes pas sûr de comment fonctionne `useCallback` ? Vous avez probablement sauté la section précédente sur les hooks avancés qui pointait vers la feuille de triche. [Jetez un coup d'œil](https://react-hooks-cheatsheet.com/usecallback).

Une fois que nous avons créé `expanded` et `toggle`, nous pouvons exposer ceux-ci via la prop `value` du `Provider`.

```
...const Expandable = ({children}) => {  const [expanded, setExpanded] = useState(false)  const toggle = useCallback(    () => setExpanded(prevExpanded => !prevExpanded),    []  )   // regardez ici ?  const value = { expanded, toggle }   // et ici ?  return <;Provider value={value}>{children}</Provider>}  
```

Cela fonctionne, mais la référence `value` sera différente à chaque re-rendu, ce qui amènera le `Provider` à re-rendre ses enfants.

Mémorisons la `value`.

```
...const Expandable = ({children}) => {  ... // regardez ici ?  const value = useMemo(	() => ({ expanded, toggle }), 	[expanded, toggle]  )  return <Provider value={value}>{children}&lt;/Provider>} 
```

`useMemo` prend un rappel qui retourne la valeur de l'objet `{ expanded, toggle }` et nous passons un tableau de dépendances `[expanded, toggle]` afin que la valeur mémorisée reste la même sauf si ceux-ci changent.

Nous avons fait un excellent travail jusqu'à présent !

Maintenant, il y a juste une autre chose à faire sur le composant parent `Expandable`.

Si vous vous souvenez d'une expérience précédente avec les composants de classe, il est possible de faire ceci :

```
this.setState({  name: "value"}, () => {  this.props.onStateChange(this.state.name)})
```

C'est ainsi que vous déclenchez un rappel après un changement d'état dans les composants de classe.

Habituellement, le rappel, par exemple, `this.props.onStateChange`, est toujours invoqué avec la valeur actuelle de l'état mis à jour comme montré ci-dessous :

```
this.props.onStateChange(this.state.name)
```

Pourquoi est-ce important ?

C'est une bonne pratique lors de la création de composants réutilisables, car de cette manière, le consommateur de votre composant peut attacher une logique personnalisée à exécuter après une mise à jour de l'état.

Par exemple :

```
const doSomethingPersonal = ({expanded}) => {  // faire quelque chose de vraiment important après avoir été développé}
```

```
<Expandable onExpanded={doSomethingPersonal}> ... </Expandable>
```

Nous allons ajouter cette fonctionnalité au composant `Expanded`.

Avec les composants de classe, cela est assez simple. Avec les composants fonctionnels, nous devons faire un peu plus de travail — pas trop :)

Chaque fois que vous voulez effectuer un effet secondaire dans un composant fonctionnel, dans la plupart des cas, utilisez toujours `useEffect`.

Ainsi, la solution la plus facile pourrait ressembler à ceci :

```
useEffect(() => {  props.onExpanded(expanded)}, [expanded])
```

Le problème, cependant, avec cela est que la fonction d'effet `useEffect` est appelée au moins une fois — lorsque le composant est initialement monté.

Ainsi, même s'il y a un tableau de dépendances, `[expanded]`, le rappel sera également invoqué lorsque le composant est monté !

```
useEffect(() => {  // cette fonction sera toujours invoquée au montage})
```

La fonctionnalité que nous recherchons nécessite que le rappel à passer par l'utilisateur ne soit pas invoqué au montage.

Comment pouvons-nous imposer cela ?

Tout d'abord, considérons la solution naïve ci-dessous :

```
// solution défectueuse... let componentJustMounted = trueuseEffect(    () => {        if(!componentJustMounted) {        props.onExpand(expanded)        componentJustMounted = false      }    },    [expanded]  )...
```

Qu'est-ce qui ne va pas avec le code ci-dessus ?

De manière générale, la logique derrière le code est correcte. Vous gardez une trace d'une certaine variable `componentJustMounted` et la définissez à `true`, et n'appelez le rappel utilisateur `onExpand` que lorsque `componentJustMounted` est faux.

La valeur `componentJustMounted` n'est définie à `false` qu'après que le rappel utilisateur a été invoqué au moins une fois.

Cela semble bien.

Cependant, le problème avec cela est que chaque fois que le composant fonctionnel est re-rendu en raison d'un changement d'état ou de prop, la valeur `componentJustMounted` sera toujours réinitialisée à `true`. Ainsi, le rappel utilisateur `onExpand` ne sera jamais invoqué car il n'est invoqué que lorsque `componentJustMounted` est faux.

```
...if (!componentJustMounted) {    	onExpand(expanded)}...
```

Eh bien, la solution à cela est simple. Nous pouvons utiliser le hook `useRef` pour nous assurer qu'une valeur reste la même tout au long de la durée de vie du composant.

Voici comment cela fonctionne :

```
// implémentation correcte  const componentJustMounted = useRef(true)  useEffect(    () => {      if (!componentJustMounted.current) {        onExpand(expanded)      }      componentJustMounted.current = false    },    [expanded]  )
```

`useRef` retourne un objet `ref` et la valeur stockée dans l'objet peut être récupérée à partir de `ref.current`

La signature de `useRef` ressemble à ceci : `useRef(initialValue)`.

Ainsi, stocké initialement dans `componentJustMounted.current` se trouve un objet ref avec la propriété `current` définie à `true`.

```
const componentJustMounted = useRef(true)
```

Après avoir invoqué le rappel utilisateur, nous mettons ensuite à jour cette valeur à `false`.

```
componentJustMounted.current = false
```

Maintenant, chaque fois qu'il y a un changement d'état ou de prop, la valeur dans l'objet ref n'est pas altérée. Elle reste la même.

Avec l'implémentation actuelle, chaque fois que la valeur d'état `expanded` est basculée, la fonction de rappel utilisateur `onExpanded` sera invoquée avec la valeur actuelle de `expanded`.

Voici à quoi ressemble l'implémentation finale du composant `Expandable` maintenant :

```
// Expandable.js const Expandable = ({ children, onExpand }) => {  const [expanded, setExpanded] = useState(false)  const toggle = useCallback(    () => setExpanded(prevExpanded => !prevExpanded),    []  )  const componentJustMounted = useRef(true)  useEffect(    () => {      if (!componentJustMounted) {        onExpand(expanded)      }       componentJustMounted.current = false    },    [expanded]  )  const value = useMemo(   () => ({ expanded, toggle }),    [expanded, toggle]  )  return (    <Provider value={value}>        {children}    </Provider>  )}
```

Si vous avez suivi, c'est génial. Nous avons trié le composant le plus complexe du groupe. Maintenant, construisons les composants enfants.

#### Construction des Composants Enfants Composés

Il y a trois composants enfants pour le composant `Expandable`.

![Image](https://cdn-media-1.freecodecamp.org/images/qCrrUqNmXLJI53uFn41uZ9VtAWvsU9Xfi14a)

Ces composants enfants doivent consommer des valeurs de l'objet de contexte créé dans `Expandable.js`.

Pour rendre cela possible, nous allons faire un peu de refactoring comme montré ci-dessous :

```
export const ExpandableContext = createContext()
```

Nous exportons l'objet de contexte, `ExpandableContext` de `Expandable.js`.

Maintenant, nous pouvons utiliser le hook `useContext` pour consommer les valeurs du `Provider`.

Voici le composant enfant `Header` entièrement implémenté.

```
//Header.jsimport React, { useContext } from 'react'import { ExpandableContext } from './Expandable'
```

```
const Header = ({children}) => {  const { toggle } = useContext(ExpandableContext)  return <div onClick={toggle}>{children}</div>}export default Header
```

Simple, hein ?

Il rend un `div` dont le rappel `onClick` est la fonction `toggle` pour basculer l'état `expanded` dans le composant parent `Expandable`.

Voici l'implémentation pour le composant enfant `Body` :

```
// Body.jsimport { useContext } from 'react'import { ExpandableContext } from './Expandable'
```

```
const Body = ({ children }) => {  const { expanded } = useContext(ExpandableContext)  return expanded ? children : null}export default Body
```

Assez simple également.

La valeur `expanded` est récupérée de l'objet de contexte et utilisée dans le balisage rendu. Cela se lit comme suit : Si développé, rendre `children` sinon ne rien rendre.

Le composant `Icon` est tout aussi simple.

```
// Icon.jsimport { useContext } from 'react'import { ExpandableContext } from './Expandable'
```

```
const Icon = () => {  const { expanded } = useContext(ExpandableContext)  return expanded ? '-' : '+'}export default Icon
```

Il rend soit `+` soit `-` en fonction de la valeur de `expanded` récupérée de l'objet de contexte.

Avec tous les composants enfants construits, nous pouvons définir les composants enfants comme propriétés de `Expandable`. Voir ci-dessous :

```
import Header from './Header'import Icon from './Icon'import Body from './Body'
```

```
const Expandable = ({ children, onExpand }) => {	...}
```

```
// Souvenez-vous que ceci est juste une référence personnelle. Ce n'est pas obligatoireExpandable.Header = HeaderExpandable.Body = BodyExpandable.Icon = Icon
```

Maintenant, nous pouvons aller de l'avant et utiliser le composant `Expandable` comme conçu :

```
<Expandable>    <Expandable.Header>React hooks</Expandable.Header>           <Expandable.Icon />    <Expandable.Body>Hooks are awesome&lt;/Expandable.Body></Expandable>
```

Est-ce que cela fonctionne ?

Vous pariez !

Voici ce qui est rendu lorsqu'il n'est pas développé :

![Image](https://cdn-media-1.freecodecamp.org/images/D3EYhc5vHz6LzpqQkb38aAfzEF8NICFyX0J8)

Et lorsqu'il est développé :

![Image](https://cdn-media-1.freecodecamp.org/images/T8DJ2hZnTVMSyKFRN0t8-br-GCE5H9c-3cap)

Cela fonctionne mais c'est probablement le composant le plus laid que j'ai jamais vu. Nous pouvons faire mieux.

#### Styling Gérable pour les Composants Réutilisables

Aimez-le ou non, le styling (ou CSS) est intégral à la façon dont le web fonctionne.

Bien qu'il existe un certain nombre de façons de styliser un composant `React`, et je suis sûr que vous avez une préférée, lorsque vous construisez des composants réutilisables, il est toujours bon d'exposer une API sans friction pour remplacer les styles par défaut.

Habituellement, je recommande de permettre à vos composants d'être stylisés à la fois via les props `style` et `className`.

Par exemple :

```
// ceci devrait fonctionner.<MyComponent style={{name: "value"}} />// et ceci.<MyComponent className="my-class-name-with-dope-styles" />
```

Maintenant, notre objectif n'est pas seulement de styliser le composant, mais de le rendre aussi réutilisable que possible. Cela signifie de laisser celui qui consomme le composant styliser le composant comme il le souhaite, c'est-à-dire via un style en ligne avec la prop `style`, ou en passant une prop `className`.

Commençons par le composant enfant `Header` :

```
// avant const Header = ({children}) => {  const { toggle } = useContext(ExpandableContext)  return <div onClick={toggle}>{children}</div>}
```

Tout d'abord, changeons le balisage rendu en un `button`. C'est une alternative plus accessible et sémantique au `div` utilisé précédemment.

```
const Header = ({children}) => {  const { toggle } = useContext(ExpandableContext)  // regardez ici ?  return <button onClick={toggle}>{children}<;/button>} 
```

Nous allons maintenant écrire quelques styles par défaut pour le composant `Header` dans un fichier `Header.css`.

```
// Header.css.Expandable-trigger {    background: none;    color: hsl(0, 0%, 13%);    display: block;    font-size: 1rem;    font-weight: normal;    margin: 0;    padding: 1em 1.5em;    position: relative;    text-align: left;    width: 100%;    outline: none;    text-align: center;  }    .Expandable-trigger:focus,  .Expandable-trigger:hover {    background: hsl(216, 94%, 94%);  }
```

Je suis sûr que vous pouvez comprendre le CSS simple ci-dessus. Si ce n'est pas le cas, ne vous stressez pas. Ce qui est important, c'est de noter le `className` par défaut utilisé ici, `.Expandable-trigger`

Pour appliquer ces styles, nous devons importer le fichier `CSS` et appliquer la prop `className` appropriée au `button` rendu.

```
... import './Header.css'const Header = () => {  const { toggle } = useContext(ExpandableContext)  return <button onClick={toggle} 	 className="Expandable-trigger">	{children}&lt;/button>}
```

Cela fonctionne très bien, cependant, le `className` est défini sur la chaîne par défaut `Expandable-trigger`.

Cela appliquera le style que nous avons écrit dans le fichier `CSS`, mais cela ne prend pas en compte le `className` passé par l'utilisateur.

Il est important de permettre le passage de cette prop `className` car un utilisateur pourrait vouloir changer le style par défaut que vous avez défini dans votre `CSS`.

Voici une façon de faire cela :

```
// Header.jsimport './Header.css'const Header = ({ children, className}) => {  // regardez ici ?  const combinedClassName = `Expandable-trigger ${className}`  return (    <button onClick={toggle} className={combinedClassName}>      {children}    </button>  )} 
```

Maintenant, tout `className` passé au composant `Header` sera combiné avec le `default` `Expandable-trigger` avant d'être passé au `button` rendu.

Considérons à quel point la solution actuelle est bonne.

Tout d'abord, si la prop `className` est `null` ou `undefined`, la variable `combinedClassName` contiendra la valeur `"Expandable-trigger null"` ou `"Expandable-trigger undefined"`.

Pour éviter cela, assurez-vous de passer un `className` en utilisant la syntaxe des paramètres par défaut ES6 comme montré ci-dessous :

```
// notez comment className est défini par défaut sur une chaîne videconst Header = ({ children, className = '' }) => {  ...}
```

Ayant fourni une valeur par défaut, si l'utilisateur n'entre toujours pas de `className`, la valeur `combinedClassName` sera égale à `"Expandable-trigger "`.

Notez la chaîne vide ajoutée à `Expandable-trigger`. Cela est dû au fonctionnement des littéraux de gabarit.

Ma solution préférée est de faire ceci :

```
const combinedClassName = ['Expandable-trigger', className].join('')
```

Cette solution gère les cas limites précédemment discutés. Si vous souhaitez également être explicite sur la suppression de `null`, `undefined` ou toute autre valeur fausse, vous pouvez faire ce qui suit :

```
const combinedClassName = ['Expandable-trigger', className].filter(Boolean).join('')
```

Je vais m'en tenir à l'alternative plus simple, et fournir une valeur par défaut pour `className` via les paramètres par défaut.

Cela dit, voici l'implémentation finale pour `Header` :

```
// après ...import './Header.css'const Header = ({ children, className = ''}) => {  const { toggle } = useContext(ExpandableContext)  const combinedClassName = ['Expandable-trigger', className].join('')
```

```
return (    <button onClick={toggle} className={combinedClassName}>      {children}    </button>  )}
```

Jusqu'à présent, tout va bien.

Au cas où vous vous poseriez la question, `combinedClassName` retourne une chaîne. Puisque les chaînes sont comparées par valeur, il n'est pas nécessaire de mémoriser cette valeur avec `useMemo`.

Jusqu'à présent, nous avons géré avec grâce la prop `className`. Et pour l'option de remplacer les styles par défaut en passant une prop `style` ?

Eh bien, corrigeons cela.

Au lieu de déstructurer explicitement la prop `style`, nous pouvons transmettre toute autre prop passée par l'utilisateur au composant `button`.

```
// paramètre de repos ...otherProps ?const Header = ({ children, className = '', ...otherProps }) => {	return (    // syntaxe de propagation {...otherProps} ?    <button {...otherProps}>      {children}    </button>  )}  
```

Notez l'utilisation du [paramètre de repos](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters) et de la [syntaxe de propagation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax).

Avec cela fait, le composant `Header` reçoit nos styles par défaut, tout en permettant des changements via les props `className` ou `style`.

```
// remplacer le style via className<Expandable.Header className="my-class">	React hooks</Expandable.Header>
```

```
// remplacer le style via la prop style<Expandable.Header style={{color: "red"}}>	React hooks</Expandable.Header>
```

Maintenant, je vais faire de même pour les autres composants enfants, `Body` et `Icon`.

```
// avant const Body = ({ children }) => {  const { expanded } = useContext(ExpandableContext)  return expanded ? children : null}
```

```
// après import './Body.css'const Body = ({ children, className = '', ...otherProps }) => {  const { expanded } = useContext(ExpandableContext)  const combinedClassNames = ['Expandable-panel', className].join('')
```

```
  return expanded ? (    <div className={combinedClassNames} {...otherProps}>      {children}    </div>  ) : null}
```

```
// Body.css.Expandable-panel {    margin: 0;    padding: 1em 1.5em;    border: 1px solid hsl(216, 94%, 94%);;    min-height: 150px;  }
```

Faites de même pour le composant `Icon` :

```
// avant const Icon = () => {  const { expanded } = useContext(ExpandableContext)  return expanded ? '-' : '+'}
```

```
// après ...import './Icon.css'const Icon = ({ className = '', ...otherProps }) => {  ...  const combinedClassNames = ['Expandable-icon', className].join('')
```

```
  return (    <span className={combinedClassNames} {...otherProps}>      {expanded ? '-' : '+'}    </span>  )}
```

```
// Icon.css.Expandable-icon {    position: absolute;    top: 16px;    right: 10px;}
```

Et enfin, quelques styles pour le composant parent, `Expandable`.

```
import './Expandable.css'const Expandable = ({ children, onExpand, className = '', ...otherProps }) => {   ...   const combinedClassNames = ['Expandable', className].join('')  return (    <Provider value={value}>      <div className={combinedClassNames} {...otherProps}>        {children}      </div>    </Provider>  )}
```

```
// Expandable.css.Expandable {     position: relative;     width: 350px;}
```

Maintenant, nous avons un beau composant réutilisable !

![Image](https://cdn-media-1.freecodecamp.org/images/hrQd5NnJyljpaXrRKyja27D9zUWhMmNjD2j4)

![Image](https://cdn-media-1.freecodecamp.org/images/rKVwrothDrwalJqh04muFzOpFIzL98Yqjvk2)

Nous ne l'avons pas seulement rendu beau, mais il est également personnalisable.

À quel point le composant que nous avons construit est-il personnalisable ?

Voyez ce que j'ai fait ci-dessous avec le même composant !

![Image](https://cdn-media-1.freecodecamp.org/images/vrUIQnYihcnlrQftUj6lXhen7LBVO3HJijr1)

![Image](https://cdn-media-1.freecodecamp.org/images/n04wsdnMMD-qykRyopr-JcQq1stOiNUhqdQj)

Et cela n'a pas pris beaucoup de code.

```
<Expandable>    <Expandable.Header>Reintroducing React</Expandable.Header>    <Expandable.Icon />    <Expandable.Body>     	<img            src='https://i.imgur.com/qpj4Y7N.png'            style={{ width: '250px' }}            alt='reintroducing react book cover'        />        <p style={{ opacity: 0.7 }}>          This book is so f*cking amazing! <br />        <a          href='https://leanpub.com/reintroducing-react'          target='_blank'          rel='noopener noreferrer'          >            Go get it now.        </a>       </p>     </Expandable.Body></Expandable>
```

Vous pouvez aller plus loin pour tester si le remplacement des styles via la prop `style` fonctionne également.

```
<Expandable>   <Expandable.Header       // regardez ici ?	  style={{ color: 'red', border: '1px solid teal' }}>        Reintroducing React    </Expandable.Header>        ...</Expandable> 
```

Et voici le résultat de cela :

![Image](https://cdn-media-1.freecodecamp.org/images/dg50ZCANWn3YXiFdxq1kX0-KFwYDLuyhEgF-)
_Styles par défaut de l'en-tête remplacés avec la prop style._

Hourra ! Cela fonctionne comme prévu.

**Note** : J'ai couvert 5 autres modèles de composants avancés avec les Hooks [dans l'ebook](https://leanpub.com/reintroducing-react) (PDF, Epub et Mobi). **Vous pouvez l'obtenir complètement gratuitement** (ou payer ce que vous voulez si vous aimez mon travail).

![Image](https://cdn-media-1.freecodecamp.org/images/P8npt6FWcQTqVRfBE4oJ0mseFztCZ-Fod0lt)
_[https://leanpub.com/reintroducing-react](https://leanpub.com/reintroducing-react" rel="noopener" target="_blank" title=")_

### Conclusion

Cela a été un long discours sur les changements modernes dans React. Si vous ne comprenez pas encore tout, passez un peu plus de temps à pratiquer les exemples dans votre travail quotidien, et je suis assez sûr que vous en comprendrez rapidement le fonctionnement.

Lorsque vous le ferez, allez être l'ingénieur React avec une compréhension décente de React Moderne et allez construire des composants hautement réutilisables avec des modèles de hooks avancés.

Merci de m'avoir suivi dans ce voyage. Des questions ? Utilisez la section des commentaires !