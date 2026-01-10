---
title: 'React Haute Performance : 3 Nouveaux Outils pour Accélérer Vos Applications'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-12T14:34:53.000Z'
originalURL: https://freecodecamp.org/news/make-react-fast-again-tools-and-techniques-for-speeding-up-your-react-app-7ad39d3c1b82
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mJFYp7LKVzZM3PPjFb0QXQ.png
tags:
- name: React
  slug: react
- name: Redux
  slug: redux
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'React Haute Performance : 3 Nouveaux Outils pour Accélérer Vos Applications'
seo_desc: 'By Ben Edelstein

  React is usually pretty fast, but it’s easy to make small mistakes that lead to
  performance issues. Slow component mounts, deep component trees, and unnecessary
  render cycles can quickly add up to an app that feels slow.

  Luckily ther...'
---

Par Ben Edelstein

React est généralement assez rapide, mais il est facile de faire de petites erreurs qui entraînent des problèmes de performance. Les montages de composants lents, les arbres de composants profonds et les cycles de rendu inutiles peuvent rapidement s'accumuler et donner une application qui semble lente.

Heureusement, il existe de nombreux outils, certains même intégrés à React, qui aident à diagnostiquer les problèmes de performance. Dans cet article, je mettrai en lumière des outils et des techniques pour rendre les applications React rapides. Chaque section contient également une démonstration interactive et (espérons-le) amusante !

### Outil #1 : La Timeline de Performance

React 15.4.0 a introduit une nouvelle fonctionnalité de timeline de performance qui vous permet de voir exactement quand les composants sont montés, mis à jour et démontés. Elle vous permet également de visualiser les cycles de vie des composants les uns par rapport aux autres.

**Note :** Pour l'instant, cette fonctionnalité ne fonctionne que dans Chrome, Edge et IE, car elle utilise l'API User Timing qui n'a pas encore été implémentée dans tous les navigateurs.

#### Comment ça marche

1. Ouvrez votre application et ajoutez le paramètre de requête : `react_perf`. Par exemple, `[http://localhost:3000?react_perf](http://localhost:3000?react_perf)`
2. Ouvrez l'onglet **Performance** des Chrome DevTools et appuyez sur **Record**.
3. Effectuez les actions que vous souhaitez analyser.
4. Arrêtez l'enregistrement.
5. Inspectez la visualisation sous **User Timing**.

![Image](https://cdn-media-1.freecodecamp.org/images/ZbBviSDWr1oGOVXDNENgd244BuFIJ72aRzH1)

#### Comprendre la sortie

Chaque barre colorée montre le temps qu'un composant passe à faire du "travail". Puisque JavaScript est monothread, chaque fois qu'un composant est en train de monter ou de rendre, il monopolise le thread principal et empêche l'exécution d'autres codes.

Le texte entre crochets comme `[update]` décrit quelle partie du cycle de vie du composant est en cours. La timeline décompose chaque étape, afin que vous puissiez voir des timings fins sur des méthodes comme `[componentDidMount]`, `[componentWillReceiveProps]`, `[ctor]` (constructeur) et `[render]`.

Les barres qui sont empilées représentent des arbres de composants. Bien qu'il soit typique d'avoir des arbres de composants assez profonds dans React, si vous optimisez un composant qui est monté fréquemment, il peut être utile de réduire le nombre de composants conteneurs, car chacun ajoute une petite pénalité de performance et de mémoire.

Un point à noter ici est que les chiffres de timing dans la timeline sont pour la version de développement de React, qui est beaucoup plus lente que la version de production. En fait, la timeline de performance elle-même ralentit même votre application. Bien que ces chiffres ne doivent pas être considérés comme représentatifs des performances réelles, les timings _relatifs_ entre différents composants sont précis. De plus, le fait qu'un composant se mette à jour ou non ne dépend pas d'une version de production.

#### Démo #1

Pour m'amuser, j'ai truqué l'application TodoMVC pour qu'elle ait quelques _sérieux_ problèmes de performance. Vous pouvez [l'essayer ici](https://perf-demo.firebaseapp.com/?react_perf).

Pour voir la timeline, ouvrez les outils de développement Chrome, allez dans l'onglet « Performance » et cliquez sur Record. Ensuite, ajoutez quelques TODOs dans l'application, arrêtez l'enregistrement et inspectez la timeline. Voyez si vous pouvez repérer quels composants causent les problèmes de performance :)

### Outil #2 : why-did-you-update

L'un des problèmes les plus courants qui affectent les performances dans React est les cycles de rendu inutiles. Par défaut, les composants React se re-rendent chaque fois que leur parent se rend, même si leurs props n'ont pas changé.

Par exemple, si j'ai un composant simple comme ceci :

```
class DumbComponent extends Component {  render() {    return <div> {this.props.value} </div>;  }}
```

Avec un composant parent comme ceci :

```
class Parent extends Component {  render() {    return <div>      <DumbComponent value={3} />    </div>;  }}
```

Chaque fois que le composant parent se rend, `DumbComponent` se re-rendra, malgré le fait que ses props n'ont pas changé.

Généralement, si `render` s'exécute et qu'il n'y a eu aucun changement dans le DOM virtuel, c'est un cycle de rendu gaspillé puisque la méthode `render` doit être pure et ne pas avoir d'effets secondaires. Dans une application React à grande échelle, il peut être difficile de détecter les endroits où cela se produit, mais heureusement, il existe un outil qui peut aider !

#### Utilisation de why-did-you-update

![Image](https://cdn-media-1.freecodecamp.org/images/mENkmTEkJkTtWuVgiNd4SWVuXskJVqBQ830H)

`why-did-you-update` est une bibliothèque qui s'intègre à React et détecte les rendus de composants potentiellement inutiles. Elle détecte lorsqu'une méthode `render` d'un composant est appelée malgré le fait que ses props n'ont pas changé.

#### Installation

1. Installez avec npm : `npm i --save-dev why-did-you-update`
2. Ajoutez ce snippet n'importe où dans votre application :

```
import React from 'react'
```

```
if (process.env.NODE_ENV !== 'production') {  const {whyDidYouUpdate} = require('why-did-you-update')  whyDidYouUpdate(React)}
```

**Notez** que cet outil est génial en développement local, mais assurez-vous qu'il est désactivé en production car il ralentira votre application.

#### Comprendre la sortie

`why-did-you-update` surveille votre application pendant son exécution et journalise les composants qui peuvent avoir changé inutilement. Il vous permet de voir les props avant et après un cycle de rendu qu'il a déterminé comme pouvant être inutile.

#### Démo #2

Pour démontrer `why-did-you-update`, j'ai installé la bibliothèque dans l'application TodoMVC sur Code Sandbox, un terrain de jeu React en ligne. Ouvrez la console du navigateur et ajoutez quelques TODOs pour voir la sortie.

[Voici la démo](https://codesandbox.io/s/xGJP4QExn).

Remarquez que quelques composants dans l'application se rendent inutilement. Essayez d'implémenter les techniques décrites ci-dessus pour prévenir les rendus inutiles. Si c'est fait correctement, il ne devrait y avoir aucune sortie de `why-did-you-update` dans la console.

### Outil #3 : React Developer Tools

![Image](https://cdn-media-1.freecodecamp.org/images/Bz54wU40zvzYGiBPZgN8oVXuLudLwd5ejQC7)

L'extension Chrome React Developer Tools dispose d'une fonctionnalité intégrée pour visualiser les mises à jour des composants. Cela est utile pour détecter les cycles de rendu inutiles. Pour l'utiliser, assurez-vous d'abord d'[installer l'extension ici](https://codesandbox.io/s/xGJP4QExn).

Ensuite, ouvrez l'extension en cliquant sur l'onglet « React » dans les Chrome DevTools et cochez « Highlight Updates ».

![Image](https://cdn-media-1.freecodecamp.org/images/87UKidIvONTuNfgRQYAsbc5nJMwmr0JXGZ9P)

Ensuite, utilisez simplement votre application. Interagissez avec divers composants et regardez les DevTools faire leur magie.

#### Comprendre la sortie

Les React Developer Tools mettent en évidence les composants qui se re-rendent à un moment donné. Selon la fréquence des mises à jour, une couleur différente est utilisée. Le bleu montre des mises à jour peu fréquentes, allant jusqu'au vert, jaune et rouge pour les composants qui se mettent à jour fréquemment.

Voir du jaune ou du rouge n'est pas _nécessairement_ une mauvaise chose. Cela serait attendu lors de l'ajustement d'un curseur ou d'un autre élément d'interface utilisateur qui déclenche des mises à jour fréquentes. Mais si vous cliquez sur un simple bouton et voyez du rouge, cela peut signifier que quelque chose ne va pas. Le but de l'outil est de repérer les composants qui se mettent à jour _inutilement_. En tant que développeur de l'application, vous devriez avoir une idée générale des composants qui devraient se mettre à jour à un moment donné.

#### Démo #3

Pour démontrer la mise en évidence des composants, j'ai truqué l'application TodoMVC pour mettre à jour certains composants inutilement.

[Voici la démo](https://highlight-demo.firebaseapp.com/).

Ouvrez le lien ci-dessus, puis ouvrez les React Developer Tools et activez la mise en évidence des mises à jour. Lorsque vous tapez dans la zone de texte du haut, vous verrez tous les TODOs se mettre en évidence inutilement. Plus vous tapez vite, plus vous verrez la couleur changer pour indiquer des mises à jour plus fréquentes.

### Correction des rendus inutiles

Une fois que vous avez identifié les composants de votre application qui se re-rendent inutilement, il existe quelques correctifs faciles.

#### Utiliser PureComponent

Dans l'exemple ci-dessus, `DumbComponent` est une fonction pure de ses props. C'est-à-dire que le composant n'a besoin de se re-rendre que lorsque ses props changent. React dispose d'un type spécial de composant intégré appelé `PureComponent` qui est conçu exactement pour ce cas d'utilisation.

Au lieu d'hériter de React.Component, utilisez React.PureComponent comme ceci :

```
class DumbComponent extends PureComponent {  render() {    return <div> {this.props.value} </div>;  }}
```

Ensuite, le composant ne se re-rendra que lorsque ses props changeront réellement. C'est tout !

Notez que `PureComponent` effectue une comparaison superficielle des props, donc si vous utilisez des structures de données complexes, il peut manquer certains changements de props et ne pas mettre à jour vos composants.

#### Implémenter shouldComponentUpdate

`shouldComponentUpdate` est une méthode de composant appelée avant `render` lorsque soit `props` soit `state` a changé. Si `shouldComponentUpdate` retourne true, `render` sera appelée ; si elle retourne false, rien ne se passe.

En implémentant cette méthode, vous pouvez indiquer à React d'éviter de re-rendre un composant donné si ses props ne changent pas.

Par exemple, nous pourrions implémenter `shouldComponentUpdate` dans notre composant simple de l'exemple ci-dessus comme ceci :

```
class DumbComponent extends Component {  shouldComponentUpdate(nextProps) {    if (this.props.value !== nextProps.value) {      return true;    } else {      return false;    }  }
```

```
render() {    return <div>foo</div>;  }}
```

### Débogage des problèmes de performance en production

Les React Developer Tools ne fonctionnent que si vous exécutez votre application sur votre propre machine. Si vous êtes intéressé par la compréhension des problèmes de performance que les utilisateurs rencontrent en production, essayez [LogRocket](https://logrocket.com).

![Image](https://cdn-media-1.freecodecamp.org/images/7IdIjQayZnkgNUsWFK89yHsyIOyR7byGxiTZ)

[LogRocket](https://logrocket.com) est comme un DVR pour les applications web, enregistrant _littéralement_ _tout_ ce qui se passe sur votre site. Au lieu de deviner pourquoi les problèmes se produisent, vous pouvez rejouer les sessions avec des bugs ou des problèmes de performance pour comprendre rapidement la cause racine.

LogRocket instrumente votre application pour enregistrer les données de performance, les actions/états Redux, les logs, les erreurs, les requêtes/réponses réseau avec les en-têtes + corps, et les métadonnées du navigateur. Il enregistre également le HTML et le CSS de la page, recréant des vidéos pixel-perfect même des applications monopages les plus complexes.

[**LogRocket | Logging et Replay de Sessions pour les Applications JavaScript**](https://logrocket.com/)  
[_LogRocket vous aide à comprendre les problèmes affectant vos utilisateurs, afin que vous puissiez retourner à la construction de logiciels géniaux._logrocket.com](https://logrocket.com/)

Merci d'avoir lu. J'espère que ces outils et techniques vous aideront dans votre prochain projet React !