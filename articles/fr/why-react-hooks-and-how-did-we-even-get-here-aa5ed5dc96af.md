---
title: Pourquoi les Hooks React, et comment en sommes-nous arrivés là ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T21:18:18.000Z'
originalURL: https://freecodecamp.org/news/why-react-hooks-and-how-did-we-even-get-here-aa5ed5dc96af
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tFj5MfPtA2bvvJWo
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Pourquoi les Hooks React, et comment en sommes-nous arrivés là ?
seo_desc: 'By Ryan Yurkanin

  TL;DR: Hooks have learned from the trade-offs of mixins, higher order components,
  and render props to bring us new ways to create contained, composable behaviors
  that can be consumed in a flat and declarative manner. ?

  However, hooks...'
---

Par Ryan Yurkanin

**TL;DR :** Les Hooks ont tiré des enseignements des compromis des mixins, des composants d'ordre supérieur et des render props pour nous apporter de nouvelles façons de **créer** des **comportements contenus et composables** qui peuvent être consommés de manière **plate et déclarative**. ?

Cependant, les hooks viennent avec leur propre prix. Ils ne sont pas la solution miracle. Parfois, vous avez besoin de hiérarchie. Alors, examinons cela de plus près.

[Les Hooks React](https://reactjs.org/docs/hooks-overview.html) sont là, et je suis immédiatement tombé amoureux d'eux. Pour comprendre pourquoi les Hooks sont géniaux, je pense qu'il est utile de voir comment nous avons résolu un problème courant tout au long de l'histoire de React.

**Voici la situation.** Vous devez montrer la position de la souris de l'utilisateur. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*skhvS29DZ6sBkCPBmaMz7g.png)
_Eh bien, c'était facile !_

#### ⚠️ Cependant, il y a des moyens par lesquels cela peut nous revenir en boomerang.

* Si vous avez besoin de ce comportement de mouvement de souris dans un autre composant, vous devrez réécrire le même code.
* Si vous ajoutez plus de comportements comme celui-ci, il deviendra plus difficile à comprendre au premier coup d'œil. Cela est dû au fait que la logique du comportement est répartie entre `componentDidMount` et `componentWillUnmount` ?

Nous sommes des ingénieurs, et nous avons _une tonne_ d'outils pour nous aider à briser ce schéma. Passons en revue certaines des façons dont nous l'avons historiquement fait et leurs compromis. ?

### Mixins

Les Mixins reçoivent beaucoup de critiques. Ils ont posé les bases pour regrouper les hooks de cycle de vie afin de décrire un effet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nkp3K5sbw6FuGvoLofVk8g.png)

Bien que l'idée générale d'encapsuler la logique soit géniale, nous avons fini par apprendre quelques [leçons sérieuses des mixins](https://reactjs.org/blog/2016/07/13/mixins-considered-harmful.html).

Il n'est pas évident de savoir d'où vient `this.state.x`. Avec les mixins, il est également possible que le mixin dépende aveuglément du fait qu'une propriété existe dans le composant.

Cela devient un énorme problème lorsque les gens commencent à inclure et à étendre des tonnes de mixins. Vous ne pouvez pas simplement rechercher dans un seul fichier et supposer que vous n'avez rien cassé ailleurs.

Le refactoring doit être facile. **Ces comportements intégrés doivent être plus évidents qu'ils n'appartiennent pas au composant.** Ils ne devraient pas utiliser les internes du composant. ?‍

### Composants d'ordre supérieur

Nous pouvons obtenir un effet similaire, et le rendre un peu moins magique en créant un conteneur qui passe des props ! Le principal compromis de l'héritage est qu'il rend le refactoring plus difficile, alors essayons la composition !

![Image](https://cdn-media-1.freecodecamp.org/images/1*qJZXnzuAgXQsSoibXZH6Zg.png)

Bien que ce soit plus de code, nous allons dans la bonne direction. Nous avons tous les avantages des Mixins. Maintenant, nous avons un composant `<MouseRender` /> qui n'est plus étroitement couplé au comportement d'abonnement.

Et si nous voulions rendre quelque chose de différent ? Devons-nous toujours créer un nouveau composant ?

### Render Props & Children as a Function

C'est le modèle qui nous a regardés en face tout le temps. Tout ce que nous voulons, c'est un composant qui gère le comportement du mouvement de la souris, et la capacité de rendre ce que nous voulons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ii7bRuk2u7jBqunmIzwGrQ.png)

#### Cette différence subtile a quelques avantages assez géniaux

* Il est maintenant super évident de voir ce qui fournit `x` et `y`. Vous pouvez également les renommer facilement pour éviter les collisions de noms.
* Nous avons un contrôle flexible sur ce qui est rendu. Nous n'avons pas besoin de créer de nouveaux composants, et si nous décidons de le faire, c'est juste un simple copier-coller.
* Vous pouvez voir tout cela directement dans une fonction de rendu de composant. C'est en pleine vue et facile pour les nouveaux développeurs à identifier. `cmd + f` fonctionne bien ici.

Le principal problème avec ce modèle est que vos composants sont liés à en nicher plusieurs dans leurs rendus. Une fois que vous commencez à nicher plusieurs composants de render prop, il peut être incroyablement difficile de comprendre ce qui se passe.

De plus, cela crée un faux sentiment de hiérarchie. Juste parce qu'un comportement est "niché" sous un autre comportement ne signifie pas qu'il dépend du comportement parent. Prenons par exemple ce snippet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sYxg-jYyqnRrNuRVkxoqrg.png)
_Ça me rappelle l'enfer des callbacks_

**Si seulement il y avait un moyen d'avoir tout ce pouvoir, de manière déclarative ET plate. ?**

### Hooks

Et si nous pouvions supprimer la imbrication, et tout remonter en haut ? De cette façon, le seul JSX dans notre fonction de rendu est la logique de rendu pure.

![Image](https://cdn-media-1.freecodecamp.org/images/1*11zyjavrNZlqDypso2EaeQ.png)
_C'est si beau...

C'est tout ce que j'ai toujours voulu.

* Non seulement le comportement est dans son propre petit package, `useEffect` l'empêche d'être réparti sur trois hooks de cycle de vie différents
* D'où le composant obtient ces données est incroyablement clair, il est niché proprement à l'intérieur de la fonction de rendu.
* Peu importe combien de ceux-ci j'ai besoin d'apporter, mon code ne deviendra pas de plus en plus imbriqué.

[Sunil Pai](https://www.freecodecamp.org/news/why-react-hooks-and-how-did-we-even-get-here-aa5ed5dc96af/undefined) a utilisé une mise en évidence astucieuse dans le tweet ci-dessous pour illustrer à quel point les hooks sont efficaces non seulement pour réduire la quantité totale de code, mais aussi pour regrouper les parties liées.

### Cependant, il y a quelques pièges

Lorsque vous utilisez des hooks, vous devez vous souvenir de quelques règles qui peuvent sembler étranges au premier abord :

#### **⚠️ Vous devez appeler les hooks au niveau supérieur de la fonction de rendu.**

Cela signifie pas de hooks conditionnels. Notre contrat avec React est que nous appellerons le même nombre de hooks, dans le même ordre à chaque fois.

Cette règle commence à avoir plus de sens lorsque vous la comparez à la façon dont les Mixins et les HOC fonctionnent. Vous ne pouvez pas les utiliser de manière conditionnelle et les réorganiser à chaque rendu.

Si vous voulez des effets conditionnels, vous devriez diviser vos hooks en d'autres composants, ou envisager un modèle différent.

#### ⚠️ **Vous ne pouvez utiliser les hooks que dans les composants de fonction React et dans les hooks personnalisés.**

Je ne suis pas sûr qu'il y ait une raison technique de ne pas essayer de les appeler dans une fonction régulière. Cela garantit que les données sont toujours visibles dans le fichier du composant.

#### ⚠️ **Il n'y a pas de primitives de hook pour componentDidCatch ou getSnapshotBeforeUpdate.**

L'équipe React dit qu'ils sont en chemin !

Pour le cas d'utilisation de componentDidCatch, vous pourriez créer un composant Error Boundary, getSnapshotBeforeUpdate est un peu plus délicat, mais heureusement assez rare.

### Quelques notes finales

Je n'ai aucun doute que les hooks sont sur le point de changer la façon dont nous voyons React et de bouleverser certaines meilleures pratiques. La quantité d'enthousiasme et de bibliothèques qui sortent est inspirante !

Cependant, j'ai vu l'engouement pour tous ces modèles de conception dans le passé. Bien que la plupart se soient avérés être des outils très précieux dans notre boîte à outils, ils ont tous un prix.

Je ne comprends toujours pas pleinement les compromis des hooks, et cela me fait peur. Je vous suggère fortement de jouer avec eux et d'apprendre par l'exemple. Vous devriez probablement attendre un peu avant de faire une réécriture complète avec eux ?

Si vous avez des questions ou si vous cherchez un mentorat React en tête-à-tête, n'hésitez pas à me tweeter **@yurkaninryan** à tout moment !

Si vous aimez mon style d'écriture, voici quelques autres articles que j'ai écrits.

Bonne chance et bon codage !! ?