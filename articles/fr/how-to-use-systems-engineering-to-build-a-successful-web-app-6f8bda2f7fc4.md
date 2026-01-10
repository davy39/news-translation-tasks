---
title: Comment utiliser l'ingénierie des systèmes pour construire une application
  web réussie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-10T17:47:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-systems-engineering-to-build-a-successful-web-app-6f8bda2f7fc4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f1AObOsOTggi7QhrW8Frsw.png
tags:
- name: Design
  slug: design
- name: systems-engineering
  slug: systems-engineering
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: Comment utiliser l'ingénierie des systèmes pour construire une application
  web réussie
seo_desc: 'By Dler Ari

  If you understand how it works, its easier to build it

  So you’ve finally completed your design in Adobe XD, Figma, Sketch or InVision,
  but still struggle with the idea of how to implement the functionality. Don’t worry,
  we’ve thought for ...'
---

Par Dler Ari

#### Si vous comprenez comment cela fonctionne, c'est plus facile à construire

Vous avez enfin terminé votre design dans Adobe XD, Figma, Sketch ou InVision, mais vous avez encore du mal avec l'idée de comment implémenter la fonctionnalité. Ne vous inquiétez pas, nous avons pensé pendant un moment que la seule façon de construire des applications web était de commencer par la conception UI/UX ainsi que des croquis de prototypes.

Heureusement, il s'avère qu'il existe d'autres techniques, et meilleures, que nous pouvons utiliser pour décrire les applications web sans nous soucier des positions, tailles ou espacements des éléments sur une page.

Permettez-moi de vous présenter quelque chose qui a été utilisé par des entreprises dans les domaines de l'aérospatial, du maritime, de la défense, de l'automobile et des télécommunications pour mieux comprendre comment les systèmes se comportent et interagissent. Je ne parle pas de X nombre de conseils et astuces sur la façon d'améliorer l'UI/UX, mais des techniques que vous pouvez appliquer de l'arsenal de l'**Ingénierie des Systèmes** (SE) pour construire des applications web réussies.

Ces techniques ont de nombreux avantages, mais le plus important est la rapidité avec laquelle on peut exprimer des idées et comprendre comment les choses fonctionnent.

À la fin de cet article, vous serez en mesure d'utiliser certaines de ces techniques SE pour construire de meilleures applications.

Voici quatre techniques SE pratiques et pertinentes que vous pouvez appliquer.

> Si vous voulez devenir un meilleur développeur web, créer votre propre entreprise, enseigner aux autres ou simplement améliorer vos compétences en développement, je publierai des conseils et astuces de haute qualité chaque semaine sur les derniers langages web disponibles sur le marché.

### Un exemple pratique — Plateforme d'apprentissage en ligne

Afin de rendre les exemples intuitifs et applicables, nous allons construire une plateforme d'apprentissage en ligne fictive. Une plateforme qui permet aux gens de publier du contenu, le même concept que Medium, YouTube, Unsplash, etc.

> Note : l'idée d'utiliser ces techniques est de les décrire suffisamment pour que les développeurs puissent facilement implémenter ces fonctionnalités, ce qui signifie que nous n'avons pas besoin d'entrer dans les détails.

Voici quelques conseils utiles à connaître dans les premières étapes de l'application.

#### 1. Ne commencez pas par la conception détaillée

Dans les premières étapes, la plupart des développeurs commencent naturellement par définir les solutions d'abord, et se retrouvent ainsi pris dans des détails qui n'ont pas vraiment d'importance pour le produit final. Cela nous mène dans la mauvaise direction, et nous oublions le véritable but de l'application.

Le design est important, mais ce n'est pas quelque chose sur lequel nous devrions nous concentrer dans les premières étapes. Il n'est pas fixe (et change souvent) — par exemple, la couleur d'un bouton, la position des éléments, le type de police, etc. Ce qui ne change pas, c'est le comportement sous-jacent de l'application web, comme la manière dont une personne s'authentifie, la manière dont ils téléchargent quelque chose sur une page, les étapes pour traiter un paiement, et ainsi de suite. Les parties fondamentales restent les mêmes.

#### 2. Commencez par le problème

Identifiez d'abord le problème : l'environnement, qui sont les parties prenantes, le comportement et le contexte de l'application (la portée).

Nous ne construisons pas des applications basées sur des solutions, nous les construisons parce qu'il y a un problème, une question ou un défi qui doit être résolu. Dans la plupart des cas, le client ne se soucie pas de la solution, sauf qu'elle fonctionne. La solution doit être identifiée lorsque les développeurs comprennent comment l'application se comporte et interagit.

Le problème peut être, par exemple, que la plateforme de communication actuelle est trop lente, ce qui influence le flux de travail. Un autre problème peut être que le gestionnaire n'a pas une vue d'ensemble claire des tâches sur lesquelles l'employé travaille, et ainsi de suite.

Gardez à l'esprit que le problème nous indique qu'il y a un besoin, mais ne fournit aucune solution. Le problème est ce qui déclenche le processus de développement. Alors commencez par le problème avant de commencer avec les solutions.

Voyons quelles techniques nous pouvons utiliser pour décrire notre plateforme d'apprentissage en ligne.

### 1. Diagramme de contexte

![Image](https://cdn-media-1.freecodecamp.org/images/1*f1AObOsOTggi7QhrW8Frsw.png)

#### Définir les limites

Le but du diagramme de contexte est de définir les limites au sein de l'application, ou des parties de l'application, et de fournir une compréhension claire des entités avec lesquelles elle interagit.

Comme le montre l'image, nous pouvons voir quels types de parties prenantes (utilisateurs) interagissent avec l'application, et les types d'interactions entre eux. Notez que les noms des parties prenantes ne sont pas mentionnés, ni le type de base de données avec lequel nous traitons. Nous ne voulons pas nous perdre dans des détails qui pourraient changer dans le futur.

#### Clarifier les applications complexes

Si vous traitez une application assez complexe composée de nombreuses parties, alors un diagramme de contexte est une bonne alternative qui vous permet de simplifier les choses. C'est aussi un bon moyen de nous rappeler quel est le but de l'application, et d'éliminer les choses qui apportent peu de valeur à l'application. C'est une façon de faire un pas en arrière et de se concentrer sur ce qui est important.

### 2. Diagramme de cas d'utilisation

![Image](https://cdn-media-1.freecodecamp.org/images/1*9pm2euQHRmIO1izFgd1-uA.png)
_Diagramme de cas d'utilisation de haut niveau_

Notez que nous ne mentionnons rien sur la disposition, la taille ou la position des éléments. En SE, il est important que les choses soient modulaires, ce qui signifie que nous pouvons changer les choses sans affecter l'application — nous ne voulons pas que les choses soient fixes et immuables.

> Un développeur qui doit construire un logiciel fonctionnel doit être capable de lire un cas d'utilisation et d'avoir une bonne idée de ce que le logiciel doit faire. [Source](http://www.gatherspace.com/static/use_case_example.html).

#### Décrire les interactions

Le but du diagramme de cas d'utilisation est de décrire comment l'utilisateur interagit avec l'application web de manière verbale. C'est un excellent outil pour comprendre ce dont le client a besoin et aussi quelles fonctionnalités le développeur doit implémenter.

#### Élaborer un cas d'utilisation (action)

Comme le montre l'image ci-dessus, l'utilisateur est le producteur de contenu et effectue quatre actions. Une action est une fonctionnalité qui doit être implémentée. Le diagramme de cas d'utilisation ne décrit pas le comportement de l'application, sauf l'interaction entre l'utilisateur et l'application, ou des parties de celle-ci.

Afin de décrire le comportement, nous pouvons prendre une action et l'élaborer à travers des diagrammes tels que les diagrammes d'activité, les diagrammes d'état-transition, les diagrammes de séquence, et ainsi de suite.

Par exemple, nous pouvons créer un diagramme d'activité pour décrire les étapes nécessaires pour accomplir l'action "téléverser du contenu". Il y a un exemple de cela dans les sections 3 et 4.

#### Se concentrer sur différents scénarios de cas d'utilisation

L'application sera probablement utilisée par des utilisateurs ayant différents rôles tels qu'un administrateur, un producteur de contenu, un éditeur, un analyste, et ainsi de suite. Et chaque rôle a un ensemble de besoins uniques avec différents cas d'utilisation (interactions). Il est important que nous couvions ces interactions, sinon nous nous retrouvons avec une application statique personnalisée pour un rôle d'utilisateur spécifique.

### 3. Diagramme d'activité

![Image](https://cdn-media-1.freecodecamp.org/images/1*dUNAPGt-4Fn2BxRKgx8esg.png)
_Diagramme d'activité — téléverser du contenu_

#### Décrire le comportement

Le but d'un diagramme d'activité est de décrire la séquence d'activités nécessaires pour accomplir un cas d'utilisation. Le cas d'utilisation sélectionné est "téléverser du contenu" du diagramme de cas d'utilisation, comme le montre l'image ci-dessus.

Vous êtes libre de décider quel cas d'utilisation vous voulez développer et élaborer — le but n'est pas de faire un diagramme d'activité pour chaque cas d'utilisation, mais pour ceux qui sont difficiles à comprendre ou à implémenter.

#### Décrire les étapes pour atteindre l'objectif

Il est difficile de prédire ce que l'utilisateur fait, et dans quel ordre. Pour cette raison, un diagramme d'activité nous aide à cartographier les activités que l'utilisateur effectue, et couvre également les décisions dont nous pourrions ne pas être conscients. Il peut également être utilisé pour décrire les activités d'un non-utilisateur, par exemple une partie de l'application qui attend quelque chose avant de pouvoir s'exécuter. Le focus est de décrire le flux de travail.

#### Exprimer des idées à travers le design

Lorsque je travaillais dans une équipe, un ingénieur senior m'a remis un diagramme d'activité d'une fonctionnalité qu'il voulait voir implémentée. Le processus de développement entier est devenu beaucoup plus facile parce que je n'ai pas eu à deviner comment l'application se comporte, le comportement était déjà décrit à travers un diagramme d'activité.

En général, c'est un excellent outil pour exprimer des idées et des pensées aux gens plutôt que de se fier uniquement à la communication verbale.

### 4. Diagramme d'état-transition

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJFctGbCz-p_LVm2VmsVGA.png)
_Diagramme d'état-transition — État du contenu_

#### Définir les états

Le but du diagramme d'état-transition est de décrire un comportement discret de l'application. La différence entre un diagramme d'activité et un diagramme d'état-transition est que le premier décrit les étapes pour accomplir quelque chose (flux de travail), tandis que le second décrit comment les états d'un objet changent au cours de sa durée de vie.

Les deux sont des techniques utiles pour décrire le comportement de l'application, et sont utiles pour les clients et les développeurs afin d'acquérir une compréhension commune de comment les choses fonctionnent.

### Réflexions finales

Le design est en constante évolution et change tout au long du processus de développement. Comme mentionné ci-dessus, aborder les problèmes de design tels que l'UI/UX et les croquis de prototypes est important, mais ne décrit pas vraiment comment les parties sous-jacentes de l'application fonctionnent ou communiquent. Cela nécessite également d'avoir des designers graphiques éduqués et beaucoup de ressources.

Pour cette raison, nous avons besoin de quelque chose qui ne dépend pas du design, quelque chose qui ne se concentre pas sur des détails mineurs tels que les types de polices, les ombres portées, les couleurs, etc.

Nous avons besoin de techniques d'ingénierie des systèmes pour décrire comment l'application se comporte et interagit, pour exprimer des idées, simplifier le processus de développement et aider les personnes sans formation technique à comprendre le comportement des applications.

> Notez qu'il existe un ensemble de règles qui doivent être suivies lors de la création de tels diagrammes, cependant, la plupart des personnes avec lesquelles j'ai travaillé ne comprennent pas ou ne se soucient pas vraiment de ces règles. Le meilleur conseil que je puisse donner est de vous assurer de suivre le but du diagramme, mais ne vous perdez pas dans les règles telles que si la ligne doit se terminer par une tête de flèche, un losange, etc.

Voici quelques autres articles que j'ai écrits sur l'écosystème web ainsi que des conseils et astuces de programmation personnelle.

* [Un guide pratique des modules ES6](https://medium.freecodecamp.org/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773)
* [Comment effectuer des requêtes HTTP en utilisant l'API Fetch](https://medium.freecodecamp.org/a-practical-es6-guide-on-how-to-perform-http-requests-using-the-fetch-api-594c3d91a547)
* [Une comparaison entre Angular et React](https://medium.freecodecamp.org/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76)
* [Améliorez vos compétences avec ces méthodes JavaScript importantes](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)
* [Un esprit chaotique mène à un code chaotique](https://medium.freecodecamp.org/a-chaotic-mind-leads-to-chaotic-code-e7d6962777c0)
* [Les développeurs qui veulent constamment apprendre de nouvelles choses](https://codeburst.io/developers-that-constantly-want-to-learn-new-things-heres-a-tip-7a16e42302e4)
* [Apprenez ces concepts fondamentaux du Web](https://medium.freecodecamp.org/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0?gi=6274e9c4d599)
* [Programmez plus rapidement en créant des commandes bash personnalisées](https://codeburst.io/learn-how-to-create-custom-bash-commands-in-less-than-4-minutes-6d4ceadd9590)

Vous pouvez me trouver sur Medium où je publie chaque semaine. Ou vous pouvez me suivre sur [Twitter](http://twitter.com/dleroari), où je publie des conseils et astuces pertinents sur le développement web.