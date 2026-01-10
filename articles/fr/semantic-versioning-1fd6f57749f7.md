---
title: 'Une introduction rapide au Versionnage Sémantique : qu''est-ce que c''est
  et pourquoi l''utilisons-nous'
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-10-03T04:58:47.000Z'
originalURL: https://freecodecamp.org/news/semantic-versioning-1fd6f57749f7
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FQw6EFwILTQfFjY3.png
tags:
- name: Git
  slug: git
- name: semantics
  slug: semantics
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Une introduction rapide au Versionnage Sémantique : qu''est-ce que c''est
  et pourquoi l''utilisons-nous'
seo_desc: 'We create numbers like 1.0.0 and 1.0.1 for releases and hotfixes when we
  work on Git Flow. What do these numbers represent, and why do we use them?

  These numbers represent the version number of the product we put out in the world.
  We use them because...'
---

Nous créons des numéros comme `1.0.0` et `1.0.1` pour les versions et les correctifs lorsque nous travaillons avec Git Flow. Que représentent ces numéros et pourquoi les utilisons-nous ?

Ces numéros représentent le numéro de version du produit que nous mettons à disposition du public. Nous les utilisons parce que nous suivons une meilleure pratique appelée Versionnage Sémantique.

**Lorsque nous utilisons le Versionnage Sémantique, les développeurs sauront si un changement cassera leur code.** Les numéros donnent une indication sur le type de changements qui ont eu lieu.

De nombreux projets populaires utilisent le Versionnage Sémantique. Des exemples sont React et Vue.

### Comprendre le Versionnage Sémantique

**Une version sémantique a trois numéros.** Le numéro le plus à droite est une version de correctif.

#### Versions de Correctif

**Les versions de correctif sont utilisées pour les corrections de bugs.** Il n'y a pas de changements de fonctionnalités. (C'est pourquoi nous utilisons une version de correctif lorsque nous publions un correctif dans la [leçon précédente](https://zellwk.com/blog/git-flow)).

Lorsque vous augmentez un nouveau correctif, **vous augmentez le numéro le plus à droite de 1.** De 1, vous l'augmentez à 2, puis à 3, et ainsi de suite.

**Si votre numéro de correctif est 9** lorsque vous augmentez à nouveau la version de correctif, **vous l'augmentez à 10,** puis 11, puis 12, et ainsi de suite. (Il n'y a pas de limites aux numéros.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*FQw6EFwILTQfFjY3.png)

#### Versions Mineures

Le deuxième numéro est appelé le numéro de version mineure. Il est **utilisé lorsque vous publiez de nouvelles fonctionnalités** dans votre projet.

Lorsque vous augmentez la version mineure, vous l'augmentez également d'une unité. **Mais** **lorsque vous augmentez la version mineure, vous devez réinitialiser la version de correctif à zéro.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*ljytd-KnDUHIcPP_.png)

#### Versions Majeures

Le numéro le plus à gauche est une version majeure. Lorsque vous augmentez la version majeure, vous indiquez aux gens qu'il y a des **changements rétro-incompatibles**. Les gens peuvent rencontrer des problèmes s'ils utilisent la version suivante.

**Lorsque vous augmentez le numéro de version majeure, vous réinitialisez à la fois la version de correctif et les versions mineures.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*HDxRFW5vBUnkN1pN.png)

#### Pré-versions

Si vous souhaitez créer une pré-version (comme une version alpha ou bêta), vous pouvez ajouter un `-`, suivi des mots `alpha` ou `beta`.

Il n'y a **pas de règles strictes pour les pré-versions**, vous pouvez donc les nommer comme vous le souhaitez. Habituellement, nous utilisons alpha ou beta, suivi d'un numéro, comme `alpha1`.

### Démarrer un projet

La plupart des gens commencent les projets avec `0.1.0`. Lorsque vous êtes prêt à publier le projet au public, vous augmentez la version à `1.0.0`.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une quelconque manière ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Semantic%20Versioning%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/semantic-versioning/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [_mon blog_](https://zellwk.com/blog/semantic-versioning)_._

Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.