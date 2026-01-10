---
title: 'Création de composants : comment créer un curseur avec une entrée liée'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-11T17:00:35.000Z'
originalURL: https://freecodecamp.org/news/component-crafting-how-to-create-a-slider-with-a-linked-input-600d3438a050
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4xqdv8O0r3mXLL13R0Gk3A.jpeg
tags:
- name: forms
  slug: forms
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: 'Création de composants : comment créer un curseur avec une entrée liée'
seo_desc: 'By Robin Sandborg

  Here at Stacc, we’re huge fans of React and the render-props pattern. When it came
  time to create a slider input, we turned to one of our favorite resources — Jared
  Palmers awesome-react-render-props. Here we found react-compound-sl...'
---

Par Robin Sandborg

Ici chez [Stacc](https://stacc.com/), nous sommes de grands fans de React et du modèle render-props. Lorsqu'il a été temps de créer une entrée de curseur, nous nous sommes tournés vers l'une de nos ressources préférées — la liste [awesome-react-render-props](https://github.com/jaredpalmer/awesome-react-render-props) de Jared Palmer. C'est là que nous avons trouvé [react-compound-slider](https://github.com/sghall/react-compound-slider).

Notre défi était de combiner le curseur avec une entrée liée. L'utilisateur pouvait choisir de saisir ses données soit par l'entrée clavier, soit par le curseur.

Le curseur et l'entrée étaient comme des frères et sœurs typiques, constamment en train de se disputer. Lorsque l'entrée demandait une valeur en dehors du domaine du curseur ou une valeur qui ne tombait pas exactement sur l'une des étapes du curseur, le curseur obstiné non seulement refusait d'écouter l'entrée — il forçait l'entrée à changer sa valeur. Le résultat était une expérience utilisateur frustrante.

J'ai cherché mais je n'ai pas trouvé quelqu'un qui avait résolu ce problème pour moi. Alors, dans un esprit de partage, voici ma solution. Si vous avez des idées ou des suggestions sur la façon dont elle pourrait être encore meilleure, n'hésitez pas à les partager ! Je suis, après tout, plus designer que développeur.

### L'objectif

Cela semble assez simple, n'est-ce pas ? Alors réfléchissons à ce que nous devons faire ici.

1. Placer la valeur partagée là où à la fois le curseur et l'entrée y ont accès. Dans ce cas, nous allons créer un composant qui les enveloppe tous les deux, et y placer les valeurs.
2. Gérer les valeurs envoyées à la fois à l'entrée et au curseur lorsque quelque chose change dans l'un ou l'autre.
3. Éviter que les règles strictes du domaine du curseur (min et max) et des étapes n'interfèrent avec la capacité de l'utilisateur à taper une valeur dans l'entrée.

Nous reviendrons plus tard au composant d'enveloppement. D'abord, mettons les mains dans le cambouis avec l'implémentation du curseur. Explication ci-dessous l'exemple.

Ici, j'ai implémenté _getDerivedStateFromProps_. Le curseur doit mettre à jour son état interne à partir des valeurs fournies par les props du curseur. J'ai également ajouté quelques props pour onUpdate, onChange et onSlideStart. Nous pouvons gérer ces événements dans notre composant enveloppeur. À part ces détails, cela est très proche du code utilisé dans la [documentation de react-compound-slider](https://sghall.github.io/react-compound-slider/#/slider-demos/horizontal).

La partie avec laquelle j'ai eu du mal était la gestion de la liaison entre l'entrée et le curseur. Lors de la frappe, la valeur sort souvent des valeurs min et max autorisées du curseur. Il n'y a aucune garantie que l'utilisateur tape une valeur qui correspond exactement à l'une des étapes autorisées dans le curseur.

Si nous ne gérions pas ces cas, l'utilisateur ne serait jamais autorisé à vider l'entrée. Si elle tapait une valeur en dehors de l'une des étapes, elle serait simplement définie sur l'étape la plus proche. Basiquement, tout changement dans notre entrée entraînerait le déplacement du curseur là où il pense qu'il devrait être, et ainsi la mise à jour de notre état avec sa valeur, écrasant la valeur que l'utilisateur venait de taper.

Afin de gérer ces situations, j'avais besoin d'une certaine logique. La meilleure solution à laquelle j'ai pu penser était celle-ci :

1. Lorsque l'entrée a le focus, définir la prop step du curseur à 1 afin qu'elle puisse être définie sur ce que l'utilisateur tape.
2. Si la valeur de l'entrée change ET que la nouvelle valeur se situe dans la plage autorisée, définir la valeur du curseur. Sinon, ne rien faire.
3. Lorsque l'utilisateur commence à faire glisser le curseur, redéfinir la prop step à ce qu'elle est censée être et mettre à jour la valeur des entrées.

Vous pouvez voir l'implémentation complète avec plus de commentaires sur [CodeSandbox](https://codesandbox.io/s/wj9wv6nyw).

Merci d'avoir lu !