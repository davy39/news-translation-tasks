---
title: Un guide visuel pour comprendre le signe « = » en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T16:17:24.000Z'
originalURL: https://freecodecamp.org/news/a-visual-guide-to-understanding-the-sign-in-javascript-3de8495ab3f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_LfSneHGshm2MhXImfg13w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: Web Development
  slug: web-development
seo_title: Un guide visuel pour comprendre le signe « = » en JavaScript
seo_desc: 'By Kevin Kononenko

  The assignment operator, or “=” sign, is actually very misleading for anyone that
  is learning to code for the first time.

  You are taught about the concept of the equals sign for your entire life in math
  class.

  2 x 3 = 6

  x²-4 = 0

  Th...'
---

Par Kevin Kononenko

#### L'opérateur d'affectation, ou signe « = », est en réalité très trompeur pour quiconque apprend à coder pour la première fois.

On vous enseigne le concept du signe égal durant toute votre vie en cours de mathématiques.

_2 x 3 = 6_

_x²-4 = 0_

Les éléments du côté gauche de l'équation sont égaux en valeur aux éléments du côté droit de l'équation. Ils pourraient être inversés à tout moment, et l'affirmation resterait vraie.

Et puis JavaScript arrive comme le bonhomme Kool-Aid et détruit complètement cette compréhension.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HYP5gtpVtBz9YezFdegGWw.gif)

Oh, et ne me lancez pas sur le concept de variables. En cours d'algèbre, on nous apprend que les variables ne peuvent être égales qu'à des nombres qui satisfont l'équation. Par exemple,

_x²-4x+3 = 0_

Dans l'équation ci-dessus, _x_ ne peut être que 1 ou 3. Mais en JavaScript, le concept de variable est en fait assez différent de ce que vous avez appris en cours d'algèbre.

C'est un problème **énorme** ! Cela signifie que chaque fois qu'un débutant regarde un signe « = » lorsqu'il apprend les variables, il doit se répéter sans cesse dans sa tête :

_Ce n'est pas ce que tu crois._

_Ce n'est pas ce que tu crois._

_Ce n'est pas ce que tu crois._

Je voulais créer une façon plus mémorable d'expliquer les variables que de réenseigner ce que signifie un signe « = ». À la fin de ce tutoriel, vous comprendrez pourquoi le « = » dans l'affectation de variable ressemble plus à **une rampe qui charge un camion**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e478HxvNr4Mdtcb99r0iBw.gif)

Cela devrait constituer un guide clair sur l'objectif des variables et la manière de les utiliser tout au long de votre script.

### Le nom et la valeur d'une variable

**Les variables sont des conteneurs permettant de transporter des valeurs au sein de votre script.** À certains égards, elles sont l'opposé des variables d'algèbre.

* Vous pouvez toujours leur donner une nouvelle valeur et redémarrer votre script. Il n'y a pas d'égalité « permanente » pour satisfaire une condition.
* Le côté gauche de l'**instruction** (statement) a un objectif complètement différent du côté droit de l'instruction.

Voici un exemple :

```
let days = 7;
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*wE-bRRODuz52v_ENxM0m_A.png)

C'est ce qu'on appelle **déclarer** la variable. Cela crée un nouveau camion appelé _days_ qui peut circuler dans votre script et livrer sa **valeur** OU récupérer une nouvelle **valeur**.

* Le **mot-clé** _let_ annonce que vous créez une nouvelle variable. Ou, dans l'analogie que nous allons utiliser, que vous créez un nouveau camion.
* La variable a besoin d'un **nom** unique, qui est ici _days_. Cela distingue ce camion de tous les autres camions.
* L'**opérateur d'affectation**, ou signe « = », charge la **valeur** 7 dans le camion.

Il est très difficile de perdre l'habitude de regarder cela comme si c'était à nouveau un cours de maths, je vais donc expliquer un peu plus les différentes parties du camion-variable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NaoMytaTS9UNi9vyXbU8uw.png)

C'est le côté gauche de l'**instruction** de variable. Ce n'est pas une équation ! Nous créons un camion avec un nom spécifique que nous pouvons utiliser encore et encore. Chaque fois que nous regardons le côté gauche de l'instruction, nous appelons un camion avec un nom spécifique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*I_Axu1OrB9XKmNPNNokpMg.gif)

L'**opérateur d'affectation** est exactement comme la rampe d'un camion. Il charge une nouvelle valeur. Vous pouvez charger une nouvelle valeur à peu près n'importe quand avec le **mot-clé** _let_.

En tant que programmeur, nous créons continuellement de nouvelles variables, chargeons des valeurs et observons les changements dans le script.

### Réassigner des valeurs aux variables

Jusqu'à présent, nous pouvons créer un camion qui peut circuler dans le script et livrer sa valeur. Mais qu'en est-il du changement de la valeur que le camion transporte ?

Le **mot-clé** _let_ nous permet de créer des variables **mutables** dont les valeurs peuvent être modifiées. Si nous utilisions le mot-clé const, cela signifierait que la valeur est **immuable** et non modifiable.

En JavaScript, contrairement aux mathématiques, vous pouvez simplement **affecter** une nouvelle valeur à la variable. Notre variable days représente actuellement les 7 jours d'une semaine. Mais que se passerait-il si nous voulions qu'elle représente les 5 jours ouvrables ? Voici le code que nous pourrions utiliser.

1. À la ligne 2, nous créons la variable _days_ avec une valeur de 7.
2. À la ligne 4, nous **réassignons** la valeur de la variable. Elle est maintenant de 5.
3. À la ligne 6, le camion days arrive avec la valeur de 5.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9uGxOUVl7u3xXaPKy_oyyw.gif)

Dans le GIF ci-dessus, la ligne 4 place une nouvelle valeur dans le camion qui est utilisée plus tard à la ligne 6.

Voici ce qui se passe à la ligne 6.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TomJtNkR39aAiAzWjzhK_A.gif)

La variable days n'est « égale » à rien ! Elle transporte simplement la valeur que vous lui affectez. C'est beaucoup plus de contrôle que ce que vous avez en cours de maths, où vous devez découvrir la valeur de la variable qui satisfait l'équation. Maintenant, c'est vous qui commandez !

### Pourquoi avez-vous besoin de variables ?

Imaginez que vous construisez une application qui indique aux patients quand prendre leurs médicaments. Vous devez changer le nombre de jours par semaine en fonction du médicament. Voici un court extrait.

1. À la ligne 2, days est chargé avec une valeur de 7.
2. À la ligne 4, la valeur 5 est chargée à la place.

Aux lignes 4 et 6, vous utilisez la **valeur** de la variable days. Pourriez-vous coder cela en dur en mettant simplement le chiffre 7 à la ligne 4 et le chiffre 5 à la ligne 6 ? Bien sûr que oui !

Mais, à mesure que votre application grandit, vous constaterez que les variables sont utiles pour deux raisons :

1. **Changer instantanément toutes les valeurs appropriées en une seule fois.** Disons que vous avez trois médicaments qui doivent être pris 7 jours par semaine, et trois médicaments qui doivent être pris 5 jours par semaine. Vous ne voulez pas changer constamment la **valeur** de _days_ d'avant en arrière ! Vous voudriez plutôt utiliser deux variables distinctes. Cela vous donne deux camions séparés pour transporter les valeurs dans votre script.
2. **Se souvenir de ce qu'une valeur représente.** Si vous codez une valeur en dur, vous pourriez regarder en arrière et vous dire : pourquoi diable y a-t-il un 7 ici ? Mais, si vous créez une variable, vous vous souviendrez qu'elle représente les 7 jours de la semaine, afin de pouvoir la modifier rapidement si nécessaire.

### Noms de variables sur le côté droit de l'opérateur d'affectation

Jusqu'à présent, nous avions une règle assez stricte. Le nom de la variable est sur le côté gauche de l'**opérateur d'affectation**, tandis que la valeur est sur le côté droit.

Mais que se passe-t-il si nous avons une situation comme celle-ci ?

À la ligne 4, le nom de la variable est des deux côtés de l'opérateur d'affectation ! C'est encore une autre raison pour laquelle ce n'est PAS un signe égal ! En fait, la relation entre les deux côtés de l'instruction reste la même.

À la ligne 4, nous chargeons une nouvelle valeur dans la variable _days_. Voici à quoi cela ressemble.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CddN2NTkrM4x5M9ad2lEyA.gif)

Remarquez comment nous commençons par l'**opérateur d'affectation** et calculons d'abord le côté droit de l'instruction ? C'est parce que nous **assignons** une nouvelle valeur à days ici. Nous ne pouvons pas toucher au côté gauche de l'instruction. Voici ce qui se passe ensuite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*santo6oDTf_Cns6XomXUvg.gif)

Le camion days s'arrête deux fois dans ce cas. La première fois, c'est sur le côté droit de l'équation pour livrer l'ancienne valeur. Et la deuxième fois, c'est sur le côté gauche de l'équation pour récupérer la nouvelle valeur pour _days_.

Notre nouvelle **valeur** pour la variable _days_ est 9. Dans notre instruction de log à la ligne 6, la console afficherait 9.

#### Appel à l'action

Avez-vous apprécié cet article ? Applaudissez-le pour que d'autres puissent également le découvrir. Et, si vous voulez être averti lorsque je publierai de futurs tutoriels utilisant des analogies, inscrivez-vous ici :