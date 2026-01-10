---
title: Apprenez les variables CSS dans ce cours GRATUIT et interactif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-23T08:21:53.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-css-variables-heres-my-free-8-part-course-f2ff452e5140
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m4MKxjoyY-RXYRWBGEjkOw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: Apprenez les variables CSS dans ce cours GRATUIT et interactif
seo_desc: 'By Per Harald Borgen

  CSS Variables is an exciting new technology for modern browsers. It brings the power
  of variables to CSS, which results in less repetition, better readability, and more
  flexibility.

  To help you get started, I’ve created a free co...'
---

Par Per Harald Borgen

Les variables CSS sont une technologie passionnante pour les navigateurs modernes. Elles apportent la puissance des variables à CSS, ce qui entraîne moins de répétition, une meilleure lisibilité et plus de flexibilité.

Pour vous aider à commencer, j'ai [créé un cours gratuit sur les variables CSS sur Scrimba.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article)

Ceci est une continuation de notre série de cours gratuits sur CSS. Précédemment, nous avons lancé des cours sur [CSS Grid](https://scrimba.com/g/gR8PTE?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article) et [Flexbox](https://scrimba.com/g/gflexbox?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article). Ensemble, ils ont obtenu bien plus de 20K inscriptions.

### La structure du cours

Le cours contient 8 screencasts interactifs. Ils durent tous entre 3 et 6 minutes, car mon objectif est de vous enseigner les variables CSS aussi rapidement que possible. À la fin de certains d'entre eux, je vous donnerai un défi et vous encouragerai à jouer avec le code de manière interactive. Cela peut être fait directement dans le navigateur, car les screencasts Scrimba le permettent.

Tout au long du cours, nous travaillerons avec un site web de portfolio très simple, car cela nous donne la possibilité de mettre en évidence les cas d'utilisation les plus importants pour les variables CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Eu0wU_hiyqOqrhyxNamvsg.png)

Maintenant, examinons chacune des leçons.

#### Leçon #1 : Pourquoi apprendre les variables CSS

Dans la toute première screencast, je parlerai de pourquoi vous devriez apprendre les variables CSS. Je discuterai des avantages généraux ainsi que de ses avantages par rapport aux variables SASS et LESS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MxS9trU9nmVDttW_IqQTyA.png)

#### Leçon #2 : Votre première variable CSS

Ensuite, nous plongerons directement dans le code. Je vous montrerai d'abord comment créer une variable CSS, puis je vous demanderai de faire de même. Il est important que vous codiez réellement, et pas seulement que vous regardiez les screencasts, car cela fait mieux adhérer les connaissances.

:root {  
--red: #ff6f69;  
}

body {  
color: var(--red);  
}

#### Leçon #3 : Remplacer les variables

Nous continuerons avec le remplacement, un concept intéressant qui est possible puisque les variables CSS ont accès au DOM et sont héritées dans la hiérarchie. Cela les sépare clairement des variables SASS et LESS, qui fonctionnent plus comme des _constantes_ que des _variables_ lorsqu'elles atteignent le navigateur, et n'ont aucune connaissance du DOM.

#### Leçon #4 : Variables locales

Les variables locales sont des variables qui ne sont disponibles que dans un certain contexte, par exemple à l'intérieur de l'en-tête ou de la section de la barre latérale de votre application. Si vous essayez d'y accéder depuis un autre contexte, elle ne sera pas définie.

#### Leçon #5 : Thématisation avec les variables CSS

Les thèmes sont l'un des plus grands avantages des variables CSS. Par thèmes, je ne parle pas seulement des thèmes complets de sites web, mais aussi des thèmes spécifiques aux composants, qui sont un cas d'utilisation plus normal (par exemple, changer visuellement un élément en _mis en avant_ pour qu'il se distingue des autres).

![Ici, nous utilisons des thèmes pour faire ressortir l'un de nos éléments dans la grille par rapport aux autres.](https://cdn-media-1.freecodecamp.org/images/1*oRy5JEdUGibetP7OSQ7upQ.png)

Ici, nous utilisons des thèmes pour faire ressortir l'un de nos éléments dans la grille par rapport aux autres.

#### Leçon #6 : Changer les variables avec JavaScript

Vous pouvez également changer les variables CSS avec JavaScript, ce qui est très utile. Cela ouvre la possibilité de permettre à vos utilisateurs de changer vos variables. Encore une chose qui n'est pas possible avec les variables LESS et SASS. Un exemple très pertinent de cela est de permettre aux utilisateurs d'ajuster la taille globale de la police sur votre site. Cela le rendra plus accessible pour les personnes ayant une mauvaise vision.

#### Leçon #7 : Réactivité avec les variables CSS

Étant donné que les variables CSS ont accès au DOM, elles peuvent également être modifiées en fonction de la taille de l'écran. Cela n'est en fait qu'un exemple de remplacement, mais je pense qu'il mérite une toute nouvelle screencast, car la réactivité est assez centrale de nos jours. Tout ce qui facilite la réactivité devrait être utilisé par les développeurs front-end.

#### Leçon #8 : Variables CSS et héritage

Même si je parle d'héritage tout au long du cours, nous terminerons le cours avec quelques notes supplémentaires à ce sujet, car il y a quelques cas d'utilisation que vous pourriez imaginer fonctionner, mais qui ne fonctionnent pas.

Et c'est tout. En parcourant ces screencasts rapides, vous aurez une solide compréhension des variables CSS. Les regarder vous prendra moins de 30 minutes, et vous pouvez également ajuster la vitesse de lecture pour aller encore plus vite.

En d'autres termes : ce cours est probablement le moyen le plus rapide d'apprendre correctement les variables CSS.

Les défis peuvent, bien sûr, prendre un peu plus de temps, mais ils sont volontaires. Vous choisissez à quel point vous voulez que ce cours soit interactif.

### Le format Scrimba

Le cours est construit en utilisant Scrimba, un outil de screencast de codage interactif dont je suis cofondateur, avec [Magnus](https://medium.com/u/1a7998d688dd) et [Sindre](https://medium.com/u/c825b7f99be3).

Comme je l'ai mentionné auparavant, la chose unique avec Scrimba est que les screencasts sont entièrement interactifs, ce qui signifie que vous pouvez modifier le code à l'intérieur des casts.

Voici un gif qui explique le concept :

![Pausez le screencast → Modifiez le code → Exécutez-le ! → Voyez vos modifications](https://cdn-media-1.freecodecamp.org/images/1*4PWxbgV--7ZHlB-YVqavJg.gif)

Pausez le screencast → Modifiez le code → Exécutez-le ! → Voyez vos modifications

Cela est idéal lorsque vous sentez que vous devez expérimenter avec le code afin de le comprendre correctement, ou lorsque vous souhaitez simplement copier un morceau de code.

De plus, les screencasts Scrimba pèsent 1 % de la taille des vidéos, ce qui signifie qu'il est beaucoup plus facile de les regarder même lorsque votre connexion Internet est lente.

Alors, consultez [le cours aujourd'hui](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article), et bon codage :)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article) – le moyen le plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de conception web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_launch_article) si vous voulez apprendre à construire des sites web modernes à un niveau professionnel.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_launch_article)_