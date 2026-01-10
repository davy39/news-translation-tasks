---
title: « JavaScript est facile ! » Ils m'ont dit ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-23T09:27:05.000Z'
originalURL: https://freecodecamp.org/news/ok-now-ill-learn-how-to-program-in-javascript-2c7847414830
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E_VitjYO3ku_IhUHasRBHw.png
tags:
- name: agile
  slug: agile
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: « JavaScript est facile ! » Ils m'ont dit ?
seo_desc: 'By Fagner Brack

  Junior Developer: Ok, now I’ll learn how to program in JavaScript! Where should
  I start?

  "Senior" Developer: That''s very easy, you don''t even need to write a lot of code!
  Just go to npm, install the Zebra and Koala Open Source modules...'
---

Par Fagner Brack

**Développeur Junior** : D'accord, maintenant je vais apprendre à programmer en JavaScript ! Par où devrais-je commencer ?

**Développeur "Senior"** : C'est très facile, tu n'as même pas besoin d'écrire beaucoup de code ! Va simplement sur npm, installe les modules Zebra et Koala [Open Source](https://hackernoon.com/lets-implement-the-open-source-model-but-which-open-source-a89c82d1b494), et c'est tout !

**Développeur Junior** : Cool !

**npm** : Salut petite sauterelle, comment puis-je t'aider ?

**Développeur Junior** : Donne-moi les modules Zebra et Koala.

**npm** : Bien sûr, les voici.

**Développeur Junior** : Tout est prêt. Maintenant mon travail est terminé !

*Un jour plus tard*

**Développeur Junior** : Maintenant, j'ai besoin d'ajouter cette fonctionnalité. Par où devrais-je commencer ?

**Développeur "Senior"** : C'est très facile, tu n'as même pas besoin d'écrire beaucoup de code ! Va simplement sur le dépôt Github de Zebra et demande-leur de l'implémenter !

**Développeur Junior** : Salut Zebra, j'ai besoin d'ajouter cette nouvelle fonctionnalité, pourrais-tu m'aider ?

**Zebra** : Bien sûr, crée une Pull Request.

**Développeur Junior** : La voici.

*2 jours plus tard*

**Zebra** : Ta Pull Request n'est pas bonne, tu dois corriger quelques choses.

**Développeur Junior** : La voici.

*2 jours plus tard*

**Zebra** : Maintenant ta Pull Request est bonne, je l'ai fusionnée.

**Développeur Junior** : Merci. Maintenant mon travail est terminé !

*3 heures plus tard*

**Développeur Junior** : Maintenant, j'ai besoin de corriger ce bug. Par où devrais-je commencer ?

**Développeur "Senior"** : C'est très facile, tu n'as même pas besoin d'écrire beaucoup de code ! Va simplement sur le dépôt Github de Koala et signale-le !

**Développeur Junior** : Salut Koala, il y a un bug dans ton module.

*2 jours plus tard*

**Développeur Junior** : Salut Koala, es-tu là ?

*1 semaine plus tard*

**Développeur Junior** : Y a-t-il quelqu'un qui maintient ce module ?

*1 semaine plus tard*

**Développeur Junior** : Je vais le forker et le corriger. C'est fait.

*6 mois plus tard*

**Développeur Junior** : Maintenant, j'ai besoin d'ajouter cette autre fonctionnalité. Voyons quel module je dois modifier en premier :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SRxZPGixj9CQraELn7L2Kw.png)
*Le diagramme des dépendances du projet du Développeur Junior. C'est un ensemble de gribouillis formant des spaghettis illisibles.*

**Développeur Junior** : Euh… Je pense que quelque chose a vraiment mal tourné… JavaScript est si difficile et compliqué ! Que devrais-je faire maintenant ?

**Vrai Développeur** : Le problème n'est pas JavaScript.

Une dépendance externe tend à être trop générique et donc a beaucoup de complexité pour tenir compte des cas particuliers que tu n'as probablement pas.

En principe, tu dois réduire ta dépendance à un code externe autant que possible. Avec le temps, les dépendances entraîneront un coût de changement si tu comptes sur elles pour le **but principal** de ton projet.

Évalue leur nécessité de manière critique.

Il est possible d'écrire ton propre code pour des choses qu'un module générique peut déjà faire pour toi sans avoir à réinventer la roue, **tant que tu le conçois correctement.** Cela inclut (mais ne se limite pas à) [pas d'effets secondaires](https://hackernoon.com/this-is-how-to-get-the-best-out-of-front-end-components-52ee29dfb4ae), [faible couplage](https://medium.com/@fagnerbrack/why-do-you-need-to-know-package-coupling-fundamentals-8e0fa8e33e20), [forte cohésion](https://medium.com/@fagnerbrack/why-do-you-need-to-know-package-cohesion-fundamentals-8a3510cba2c1), [interface appropriée](https://codeburst.io/why-do-you-need-to-know-interface-fundamentals-a129ac6ab0c3), [assez d'affordance](https://hackernoon.com/affordance-in-software-design-12cc0d9d2721), [pas d'outils de test bidon](https://hackernoon.com/a-test-is-as-good-as-its-ability-to-fail-when-it-needs-to-b4b8f212119a), [code qui peut être supprimé](https://medium.freecodecamp.org/code-that-dont-exist-is-the-code-you-don-t-need-to-debug-88985ed9604), [pas de "surenchère"](https://hackernoon.com/how-to-accept-over-engineering-for-what-it-really-is-6fca9a919263), [pas de copier/coller](https://medium.freecodecamp.org/the-benefits-of-typing-instead-of-copying-54ed734ad849), [strict](https://medium.com/@fagnerbrack/the-strictness-principle-9997e483cafb), [petit](https://medium.com/@fagnerbrack/why-small-modules-matter-4e4d629321b8) et [sans faux positifs dans les tests](https://medium.com/@fagnerbrack/mocking-can-lean-to-nondeterministic-tests-4ba8aef977a0).

Si tu ne le conçois pas correctement, tu te retrouveras dans le même désordre, ou même pire.

Si tu es plombier et que le tuyau fuit, c'est ta responsabilité de le réparer. Pas celle de quelqu'un d'autre.

Il s'agit d'appliquer des principes logiciels et des [techniques](https://medium.com/@fagnerbrack/the-trick-to-write-better-software-lies-on-the-technique-944015f84ce4). Il s'agit d'apprendre à programmer.

[Ne blâme pas le scalpel.](https://hackernoon.com/the-doctor-and-the-scalpel-78656f508c9a)

**Développeur Junior** : D'accord, maintenant je vais apprendre à programmer. Peut-tu m'aider ?

**Vrai Développeur** : Oui.

*7 ans plus tard*

**Nouveau Développeur Junior** : D'accord, maintenant je vais apprendre à programmer dans ce langage populaire ! Par où devrais-je commencer ?

**Ancien Développeur Junior** : Je peux t'enseigner, mais ce n'est **pas** facile.

Je suis passé par là.

Assieds-toi.

Parlons.

Merci d'avoir lu. Si tu as des commentaires, contacte-moi sur [Twitter](https://twitter.com/FagnerBrack), [Facebook](https://www.facebook.com/fagner.brack) ou [Github](http://github.com/FagnerMartinsBrack).

Tu veux discuter en personne ? Tu peux me trouver dans le [**Sydney Software Crafters meetup**](https://www.meetup.com/Software-Crafters-Sydney/).