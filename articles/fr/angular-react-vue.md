---
title: Une analyse statistique de React, Angular et Vue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-10T10:21:17.000Z'
originalURL: https://freecodecamp.org/news/angular-react-vue
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/cover-2.jpg
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: statistics
  slug: statistics
- name: vue
  slug: vue
seo_title: Une analyse statistique de React, Angular et Vue
seo_desc: 'By Mohammad Kermani

  Many people look at GitHub stars when they''re deciding to trust and use an open-source
  project. And some people easily compare or judge projects based on the number of
  stars a repository has. Making decisions based solely on GitHu...'
---

Par Mohammad Kermani

Beaucoup de gens regardent les étoiles GitHub lorsqu'ils décident de faire confiance et d'utiliser un projet open-source. Et certaines personnes comparent ou jugent facilement les projets en fonction du nombre d'étoiles qu'un dépôt a. Prendre des décisions basées uniquement sur les étoiles GitHub n'est pas toujours la meilleure idée, cependant - et vous devriez mettre vos exigences, les caractéristiques du framework et l'architecture en premier.

Aucun de ces frameworks ou bibliothèques n'est "mauvais". Nous devrions toujours être conscients que de nombreux experts ont consacré d'innombrables heures de leur temps au développement de ces projets. Donc, si vous êtes un fanatique d'un framework spécifique, baissez votre garde pendant quelques minutes, détendez-vous simplement et continuez en paix.

> Nous travaillons tous vers le même objectif, tous ces auteurs de frameworks essaient de vous fournir quelque chose qui vous aide à construire des applications web aussi efficacement que possible

Evan You (créateur de Vue.js)

### De quoi parle précisément cet article ?

Cet article n'est pas une comparaison entre ces trois frameworks web. Cela est dû au fait que, la plupart du temps, les comparaisons sont faites par des personnes qui veulent faire la publicité de leurs frameworks préférés. Ou elles sont faites par des personnes qui ne comprennent pas vraiment ce qu'il faut pour créer un framework, donc elles ne peuvent pas voir les différents aspects de ces frameworks.

Cet article est simplement un regard statistique sur Angular, React et Vue, et leurs mouvements au fil des années. Voici ce que nous allons apprendre :

1. Les dépôts GitHub d'Angular, React et Vue au fil du temps
2. Les questions/réponses sur Stack Overflow
3. Les statistiques d'emploi
4. Conclusion

**Alors, commençons.**

## Les dépôts GitHub d'Angular, React et Vue au fil du temps

**291 934 utilisateurs GitHub uniques** ont étoilé au moins l'un des dépôts d'Angular, Angular.js, React et Vue. Il m'a fallu environ deux semaines pour crawler toutes ces pages utilisateur à des fins statistiques et démographiques (vous pouvez accéder à ces données collectées [sur GitHub](https://github.com/m98/react-angular-vue-starers)). **Alors, que pouvons-nous apprendre de ces données collectées ?**

### Quelles sont les moyennes des dépôts ?

Le tableau ci-dessous montre les moyennes de certaines des principales métriques de GitHub. Comme vous pouvez le voir, il y a un court écart entre chacune de ces moyennes. J'essaie simplement de fournir des informations et je n'interpréterai rien.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_XDhqtYPoKnYJKL5NikO2HQ-1-.jpeg)

Afin de mieux comprendre les taux de croissance de ces dépôts au cours des dernières années, j'ai préparé leur nombre d'étoiles au fil du temps dans le graphique suivant.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_XwBY_qEXn6XJ3fyAbwiz-A-1-.jpeg)

### Étoiles communes

Le diagramme et le tableau ci-dessous montrent le nombre d'utilisateurs qui ont étoilé plus d'un dépôt. Comme vous pouvez le voir, React et Vue ont plus d'étoiles en commun, et Angular a presque le même nombre d'utilisateurs communs entre React et Vue.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_-O7wREYwK2TeWPXNnau96g-1-.jpeg)

### Commits Git au fil du temps

Le nombre de commits est un bon moyen de savoir à quel point le projet est activement développé.

La course de graphiques à barres ci-dessous montre le nombre de commits au fil du temps. Contrairement à Vue, les contributeurs d'Angular et React commettent beaucoup à leurs dépôts.

%[https://public.flourish.studio/visualisation/795427/]

Voici un autre graphique des mêmes données :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_hdJsY8ISFOjUgL2p2k35iw-1-.jpeg)
_Le nombre de commits d'Angular, React et Vue_

### Nombre de contributeurs

Le nombre de contributeurs est l'une des choses qui rendent un dépôt plus fort car il y a plus de personnes qui savent comment développer et améliorer le framework ou la bibliothèque. Ils peuvent simplement faire avancer le projet, ce qui signifie qu'il y a une plus grande opportunité de découvrir et de corriger plus de bugs et de problèmes et de les améliorer plus rapidement. 

En fait, c'est aussi bon pour la communauté car plus de participants peuvent répondre à des questions spécifiques des programmeurs. Cela peut également être un signe de l'ouverture des principaux contributeurs.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_sjNGqu-57fOelBtXRwiWMA-1-.jpeg)

### Questions/réponses sur Stack Overflow

Il ne fait aucun doute que, au cours des dernières années, Stack Overflow est devenu l'une des plateformes les plus importantes et puissantes que les développeurs utilisent pour apprendre et résoudre leurs problèmes de codage. 

Le nombre de questions posées sur Stack Overflow représente le nombre de personnes qui utilisent ou apprennent une technologie particulière. J'ai utilisé l'explorateur de données StackExchange et écrit une [requête SQL](https://data.stackexchange.com/stackoverflow/query/1126512/tag-question-count-history) pour récupérer le nombre de chaque tag groupé par année et mois. Les graphiques suivants montrent le nombre de questions posées par chaque tag au fil du temps.

%[https://public.flourish.studio/visualisation/783473/]

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_KndAlRmEKo72QNENMJaszg-1-.jpeg)

### Statistiques d'emploi

Le marché de l'emploi montre quelles technologies les entreprises utilisent. Les ingénieurs logiciels et les responsables d'ingénierie comparent généralement les frameworks ou les bibliothèques afin de choisir celui ou ceux qui conviennent à leurs besoins. Ils se soucient également de la facilité à trouver un développeur qui maîtrise cette plateforme particulière. Par conséquent, plus le framework ou la bibliothèque est populaire, plus il a de potentiel pour être sélectionné.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_Ft4Mm_DDAHTHidqgDkJKkw-1-.jpeg)
_Emplois Angular, React et Vue sur certains sites populaires de listes d'emplois_

## Conclusion

C'était un court article qui, espérons-le, vous aidera à examiner ces bons et populaires frameworks web sous différents angles.

Malheureusement, il y a des ingénieurs logiciels qui comparent les frameworks ou les bibliothèques uniquement par leurs étoiles GitHub et non par leur architecture et leurs caractéristiques. Même si je crois que presque aucun de ces nombres statistiques n'est précieux lorsqu'il s'agit d'un projet de la vie réelle.

Le seul souhait que j'ai est d'être même un peu efficace pour aider à mettre fin à la guerre entre les frameworks. J'espère pouvoir aider à convaincre les personnes qui se battent pour leurs outils préférés de considérer que les autres frameworks ne sont pas pauvres ou mauvais du tout. Ils se portent tous très bien.

Apprendre est merveilleux et agréable. Choisissez simplement un nouveau framework et essayez de l'utiliser dans votre projet parallèle. Ou utilisez simplement votre framework préféré, et ne laissez pas ces nombres vous décevoir.

Vous pouvez [**me suivre**](https://medium.com/@kermani) pour plus d'articles techniques ❤️?