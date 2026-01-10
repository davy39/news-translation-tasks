---
title: Une particularité de Javascript qui pourrait vous piéger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-23T15:14:38.000Z'
originalURL: https://freecodecamp.org/news/a-javascript-quirk-that-will-catch-you-out-7895dfbae657
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VmGTvNbFTD3HrCJbyrtTeg.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une particularité de Javascript qui pourrait vous piéger
seo_desc: 'By William Woodhead

  This piece describes a feature that good Javascript developers should know. And
  once you have read this piece, you can pretend you have known about it for ages
  like me.

  Note: If you are not a Javascript developer, this might be a ...'
---

Par William Woodhead

Cet article décrit une fonctionnalité que les bons développeurs Javascript devraient connaître. Et une fois que vous aurez lu cet article, vous pourrez prétendre que vous le saviez depuis toujours, comme moi.

**Note :** Si vous n'êtes pas un développeur Javascript, cela pourrait être un peu difficile à appréhender. Si vous l'êtes, alors attachez votre ceinture pour un voyage extrêmement court.

Tout est question de _copie_ de variables (ou de clonage, d'où le mouton).

Plongeons directement dans le vif du sujet.

### **Copier des chaînes de caractères**

Faisons un peu de code :

```
var initialName = ‘William’;
```

```
var copyName = initialName;copyName = ‘Bill’;
```

```
console.log(initialName);   // affiche ‘William’console.log(copyName);      // affiche ‘Bill’
```

Tout cela semble attendu. Nous copions **initialName** et changeons ensuite sa valeur. **initialName** affiche **_‘_William’** et **copiedName** affiche **‘Bill’**.

Jusqu'ici, tout va bien. Essayons le même exercice avec des objets au lieu de chaînes de caractères. (_Attendez-vous à l'inattendu_)

### Copier des objets

```
var initialObject = { name: ‘William’ };
```

```
var copyObject = initialObject;copyObject.name = ‘Bill’;
```

```
console.log(initialObject.name);   // affiche ‘Bill’console.log(copyObject.name);      // affiche ‘Bill’
```

Hmmm, voici le problème. Lorsque nous affichons le nom de **initialObject**, il a été modifié en **Bill**.

Alors, que s'est-il passé ici ?

Lorsque nous avons défini le **name** dans **copyObject**, cela a également modifié le **name** dans **initialObject**. C'est parce que les objets sont copiés _par référence_. **copyObject** n'est qu'une référence aux données sous-jacentes.

Ainsi, lorsque nous modifions le **name** dans **copyObject**, cela modifie également le **name** dans **initialObject** car il référence la même partie des données sous-jacentes.

### Où vous pourriez vous faire piéger

Dans les grandes applications, cela pourrait faire en sorte que des parties de vos structures de données se retrouvent effectivement à plusieurs endroits en même temps.

Ainsi, si vous modifiez un objet dans une partie du code de votre application, vous pourriez le changer ailleurs. Cela peut parfois provoquer des comportements indésirables (comme un nouveau rendu) et peut être difficile à déboguer et à isoler.

Bien que cela semble très simple, dans des applications web complexes utilisant des frameworks populaires, ce simple problème de base peut causer de graves maux de tête aux développeurs.

#### Exemple Redux/React

Un exemple où j'ai vu des développeurs se faire piéger à maintes reprises est dans les [Redux action creators](https://redux.js.org/docs/basics/Actions.html#action-creators) où vous manipulez l'état avant de dispatcher des actions. En manipulant l'objet qui est passé à l'action creator sans le cloner, vous pouvez réellement modifier l'état sous-jacent, ou l'état du composant React avant votre dispatch.

### Notre solution

Il existe de nombreuses bibliothèques qui fournissent des fonctions de clonage pour les objets et les tableaux, par exemple, Lodash.

Chez [pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=jsquirk&utm_campaign=awareness), nous utilisons [Immutable.js de Facebook](https://facebook.github.io/immutable-js/) pour éviter ce problème. Même s'il s'agit d'une bibliothèque volumineuse, elle permet à nos développeurs d'écrire du Javascript fonctionnel de manière prévisible et d'éviter ce piège. Je ne saurais trop la recommander.

Voilà donc une fonctionnalité très simple mais importante à connaître en Javascript. Si vous n'êtes pas un développeur Javascript, félicitations pour être arrivé jusqu'au bout.

Si vous _êtes_ un développeur Javascript senior et que c'était nouveau pour vous, vous devriez vous sentir comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/c4C35c05ok6vxcah56o39Yxdc3jpjiq0--sz)
_giphy_

_Si vous avez aimé cette histoire, n'hésitez pas à ? et à la partager avec d'autres. N'hésitez pas non plus à consulter mon entreprise sur [pilcro.com.](https://www.pilcro.com/?utm_source=medium&utm_medium=jsquirk&utm_campaign=awareness) Pilcro aide les startups à rester cohérentes avec leur marque sur tous leurs différents canaux marketing. Vous allez adorer ce que nous préparons !_