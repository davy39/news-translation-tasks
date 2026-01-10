---
title: Tomber amoureux de React Fiber
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-28T23:44:59.000Z'
originalURL: https://freecodecamp.org/news/lets-fall-in-love-with-react-fiber-90f2e1f68ded
coverImage: https://cdn-media-1.freecodecamp.org/images/0*GOQYA_azJHmi1N0N.
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Tomber amoureux de React Fiber
seo_desc: 'By Ryan Yurkanin

  TLDR, React Fiber is an internal engine change that allows React to break the limits
  of the call stack. It’s creation enables React to pause/start rendering work at
  will. Eventually, React users will be able to hint at the “priority”...'
---

Par Ryan Yurkanin

**TLDR,** React Fiber est un changement interne du moteur qui permet à React de briser les limites de la pile d'appels. Sa création permet à React de mettre en pause/reprendre le travail de rendu à volonté. Finalement, les utilisateurs de React pourront indiquer la "priorité" du travail.

Actuellement, nous ne pouvons pas interfacer directement avec lui, alors pourquoi devrions-nous nous en soucier ? Parce que c'est vraiment super cool !

### React avant Fiber était comme travailler dans une entreprise au rythme effréné sans git.

Imaginez être au milieu d'une énorme fonctionnalité, et votre patron a besoin d'un correctif urgent, tout de suite. Vous ne pouvez pas arrêter de travailler parce que toutes vos modifications sont dans un seul fichier, vous êtes engagé à finir ce travail.

Si nous utilisions git, nous pourrions commiter notre travail dans une branche et basculer vers une branche de correctif rapide.

**Avec Fiber, React peut mettre en pause et reprendre le travail à volonté pour se concentrer sur ce qui compte dès que possible ! ?**

### Les internes de React en bref ?

Vous créez un arbre de composants. React prend cet arbre, le parcourt et crée un modèle virtuel du résultat final. Peut-être que vous rendez vers le DOM, peut-être que vous ciblez le natif. À ce stade, cela n'a pas d'importance pour React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LZzl0FxVvinV2zLjqJQeaA.png)
*Si vous n'avez jamais utilisé React, voici un exemple d'un arbre de composants.*

Maintenant, lorsque votre application se met à jour, React répétera ce processus de création du résultat virtuel encore et encore. À chaque fois, il compare l'arbre virtuel précédent avec le suivant.

À ce stade, nous devenons dépendants de la plateforme. Si vous rendez vers le DOM, il se peut qu'une seule classe d'un seul élément ait changé. React parcourra l'arbre virtuel, trouvera ce qui a changé et mettra à jour le moins possible.

Cela peut signifier la mise à jour d'un seul attribut de classe, ou cela peut signifier la destruction complète du DOM. C'est la [Réconciliation](https://reactjs.org/docs/reconciliation.html).

Avant Fiber, c'était tout. Le travail était défini, et le moteur de rendu choisi se mettait au travail. Même si le navigateur était en retard, l'utilisateur tapait ou la planète était sur le point d'exploser, le train de rendu ne s'arrêterait pas. ?

### Comment cela fonctionne-t-il (à haut niveau) ?

Avec Fiber, il existe désormais différents niveaux de priorité pour les mises à jour. La mise à jour d'une entrée qu'un utilisateur est en train de taper a une priorité plus élevée qu'une liste avec des milliers de composants.

Fiber divise le calcul de l'arbre en unités de travail qu'il peut "commiter" à tout moment. **Alors, qu'est-ce qu'une unité de travail ?** C'est simplement un nœud dans votre arbre de composants !

1. React peut maintenant mettre en pause, reprendre et redémarrer le travail sur un composant. Cela signifie que certains hooks de cycle de vie peuvent se déclencher plusieurs fois.
2. React peut avoir un système de mise à jour basé sur la priorité. Cela permet à l'équipe React d'affiner le moteur de rendu pour que React soit le plus rapide dans les cas d'utilisation les plus courants.

Je veux me concentrer un peu sur ce premier point. React va s'éloigner (mais continuer à supporter !) certains anciens hooks de cycle de vie et en ajouter de nouveaux ! ?

`componentWillMount`, `componentWillUpdate`, `componentWillReceiveProps`, peuvent maintenant se déclencher plusieurs fois. Vous ne devriez pas déclencher d'effets secondaires ici.

Maintenant, vous voulez déclencher des effets secondaires dans les hooks de cycle de vie qui ne se déclencheront qu'une seule fois : `componentDidMount` et `componentDidUpdate`

Pour compenser de nombreux cas d'utilisation que couvrait `componentWillReceiveProps`, nous recevrons deux nouveaux hooks.

1. `getDerivedStateFromProps` qui n'a pas accès aux props précédents ou à l'instance du composant, mais vous permet de synchroniser l'état avec vos props.
2. `getSnapshotBeforeUpdate` vous donne accès au DOM avant qu'il ne soit mis à jour. La valeur que vous retournez est utilisable dans `componentDidUpdate`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OoDfQ7pzAqg6yETH.)
*Ce graphique illustre comment les hooks de cycle de vie fonctionnent avec React Fiber*

> À partir de React 16.4, getDerivedStateFromProps se déclenche toujours avant la méthode de rendu. Pas seulement lorsque les props sont mises à jour !

En résumé, **Fiber permet à React d'affiner le rendu pour s'assurer que les mises à jour les plus importantes se produisent dès que possible**, tout cela pour le faible coût de certains hooks de cycle de vie et des gallons de sang des développeurs de Facebook. **?**

Si vous avez des questions ou si vous cherchez un mentorat individuel sur React, n'hésitez pas à me tweeter **@yurkaninryan** à tout moment !

Si vous aimez mon style d'écriture, voici quelques autres articles que j'ai écrits.

Bonne chance et bon codage ! ??