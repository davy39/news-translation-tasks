---
title: Une introduction de 5 minutes aux Styled Components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-23T01:01:38.000Z'
originalURL: https://freecodecamp.org/news/a-5-minute-intro-to-styled-components-41f40eb7cd55
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DIFji4ZmJa4_H3EpbG2XAw.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Une introduction de 5 minutes aux Styled Components
seo_desc: 'By Sacha Greif

  CSS is weird. You can learn the basics of it in 15 minutes. But it can take years
  before you figure out a good way to organize your styles.

  Part of this is just due to the quirks of the language itself. Out of the box, CSS
  is quite lim...'
---

Par Sacha Greif

CSS est étrange. Vous pouvez en apprendre les bases en 15 minutes. Mais il peut falloir des années avant de trouver une bonne façon d'organiser vos styles.

Une partie de cela est simplement due aux particularités du langage lui-même. Par défaut, CSS est assez limité, sans variables, boucles ou fonctions. En même temps, il est assez permissif dans le sens où vous pouvez styliser des éléments, des classes, des IDs, ou toute combinaison de ces derniers.

### Feuilles de style chaotiques

Comme vous l'avez probablement expérimenté vous-même, cela est souvent une recette pour le chaos. Et bien que des préprocesseurs comme SASS et LESS ajoutent beaucoup de fonctionnalités utiles, ils ne font pas grand-chose pour stopper l'anarchie CSS.

Ce travail d'organisation a été laissé à des méthodologies comme [BEM](http://getbem.com/), qui — bien qu'utile — est entièrement optionnelle, et ne peut pas être imposée au niveau du langage ou des outils.

### La nouvelle vague de CSS

Avancez rapidement de quelques années, et une nouvelle vague d'outils basés sur JavaScript essaient de résoudre ces problèmes à la racine, en changeant la façon dont vous écrivez CSS.

[Styled Components](https://github.com/styled-components/styled-components) est l'une de ces bibliothèques, et elle a rapidement attiré beaucoup d'attention grâce à son mélange d'innovation et de familiarité. Donc, si vous utilisez React (et si ce n'est pas le cas, [consultez mon plan d'étude JavaScript](https://medium.freecodecamp.com/a-study-plan-to-cure-javascript-fatigue-8ad3a54f2eb1) et mon [introduction à React](https://medium.freecodecamp.com/the-5-things-you-need-to-know-to-understand-react-a1dbd5d114a3)), cela vaut définitivement le coup de jeter un œil à cette nouvelle alternative CSS.

Je l'ai récemment utilisée pour [redessiner mon site personnel](http://sachagreif.com/), et aujourd'hui je voulais partager quelques choses que j'ai apprises dans le processus.

### Composants, stylisés

La principale chose que vous devez comprendre à propos des Styled Components est que leur nom doit être pris assez littéralement. Vous ne stylisez plus les éléments HTML ou les composants en fonction de leur classe ou de leur élément HTML :

```
<h1 className="title">Hello World</h1>
```

```
h1.title{  font-size: 1.5em;  color: purple;}
```

Au lieu de cela, vous définissez des **composants stylisés** qui possèdent leurs propres styles encapsulés. Ensuite, vous utilisez ces composants librement dans votre codebase :

```
import styled from 'styled-components';
```

```
const Title = styled.h1`  font-size: 1.5em;  color: purple;`;
```

```
<Title>Hello World</Title>
```

Cela peut sembler une différence mineure, et en fait, les deux syntaxes sont très similaires. Mais la différence clé est que les styles font maintenant **partie** de leur composant.

En d'autres termes, nous nous débarrassons des classes CSS comme étape intermédiaire entre le composant et ses styles.

Comme le dit Max Stoiber, co-créateur de styled-components :

_L'idée de base de_ `styled-components` _est de renforcer les bonnes pratiques en supprimant la correspondance entre les styles et les composants._

### Déléguer la complexité

Cela peut sembler contre-intuitif au premier abord, puisque l'intérêt d'utiliser CSS au lieu de styliser directement les éléments HTML (vous souvenez-vous de la balise `<font>` ?) est de découpler les styles et le balisage en introduisant cette couche de classe intermédiaire.

Mais ce découplage crée également beaucoup de complexité, et il y a un argument à faire valoir que, comparé à CSS, un langage de programmation reel comme JavaScript est beaucoup mieux équipé pour gérer cette complexité.

### Props au lieu de classes

Conformément à cette philosophie sans classes, styled-components utilise des props au lieu de classes lorsqu'il s'agit de personnaliser le comportement d'un composant. Donc, au lieu de :

```
<h1 className="title primary">Hello World</h1> // sera bleu
```

```
h1.title{  font-size: 1.5em;  color: purple;    &.primary{    color: blue;  }}
```

Vous écrirez :

```
const Title = styled.h1`  font-size: 1.5em;  color: ${props => props.primary ? 'blue' : 'purple'};`;
```

```
<Title primary>Hello World</Title> // sera bleu
```

Comme vous pouvez le voir, styled-components vous permet de nettoyer vos composants React en gardant tous les détails d'implémentation CSS et HTML en dehors de ceux-ci.

Cela dit, le CSS de styled-components reste du CSS. Donc, des choses comme ceci sont également un code totalement valide (bien que légèrement non idiomatique) :

```
const Title = styled.h1`  font-size: 1.5em;  color: purple;    &.primary{    color: blue;  }`;
```

```
<Title className="primary">Hello World</Title> // sera bleu
```

C'est une fonctionnalité qui rend styled-components très facile à adopter : en cas de doute, vous pouvez toujours revenir à ce que vous connaissez !

### Mises en garde

Il est également important de mentionner que styled-components est encore un projet jeune, et que certaines fonctionnalités ne sont pas encore pleinement supportées. Par exemple, si vous voulez [styliser un composant enfant depuis un parent](https://github.com/styled-components/styled-components/issues/142), vous devrez vous appuyer sur l'utilisation de classes CSS pour l'instant (au moins jusqu'à la sortie de styled-components v2).

Il n'y a pas non plus de moyen officiel de [pré-rendre votre CSS sur le serveur](https://github.com/styled-components/styled-components/issues/124) pour l'instant, bien que ce soit définitivement possible en injectant les styles manuellement.

Et le fait que styled-components génère ses propres noms de classes aléatoires peut rendre difficile l'utilisation des outils de développement de votre navigateur pour déterminer où vos styles sont initialement définis.

Mais ce qui est très encourageant, c'est que l'équipe principale de styled-components est consciente de tous ces problèmes et travaille dur pour les résoudre un par un. [La version 2 arrive bientôt](https://github.com/styled-components/styled-components/tree/v2), et j'ai vraiment hâte de la voir !

### En savoir plus

Mon objectif ici n'est pas d'expliquer en détail comment fonctionnent les styled-components, mais plutôt de vous donner un petit aperçu afin que vous puissiez décider par vous-même si cela vaut le coup de les explorer.

Si j'ai réussi à éveiller votre curiosité, voici quelques endroits où vous pouvez en apprendre plus sur les styled-components :

* Max Stoiber a récemment écrit un article sur la raison d'être des styled-components pour [Smashing Magazine](https://www.smashingmagazine.com/2017/01/styled-components-enforcing-best-practices-component-based-systems/).
* Le [dépôt styled-components](https://github.com/styled-components/styled-components) lui-même dispose d'une documentation extensive.
* [Cet article de Jamie Dixon](https://medium.com/@jamiedixon/styled-components-production-patterns-c22e24b1d896#.tfxr5bws2) décrit quelques avantages du passage aux styled-components.
* Si vous souhaitez en savoir plus sur la façon dont la bibliothèque est réellement implémentée, consultez [cet article](http://mxstbr.blog/2016/11/styled-components-magic-explained/) de Max.

Et si vous voulez aller encore plus loin, vous pouvez également consulter [Glamor](https://github.com/threepointone/glamor), une autre approche de la nouvelle vague CSS !

Auto-promotion : [nous recherchons des contributeurs open-source pour aider avec Nova](https://github.com/TelescopeJS/Telescope/tree/devel), le moyen le plus simple de créer des applications full-stack React & GraphQL complètes avec des formulaires, le chargement de données et des comptes utilisateurs. Nous n'utilisons pas encore styled-components, mais vous pourriez être le premier à les implémenter !