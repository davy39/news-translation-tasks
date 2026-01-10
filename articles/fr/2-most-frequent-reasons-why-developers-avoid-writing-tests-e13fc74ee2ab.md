---
title: 2 raisons les plus fréquentes pour lesquelles les développeurs évitent d'écrire
  des tests
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2017-05-21T19:44:07.000Z'
originalURL: https://freecodecamp.org/news/2-most-frequent-reasons-why-developers-avoid-writing-tests-e13fc74ee2ab
coverImage: https://cdn-media-1.freecodecamp.org/images/0*UH-V4A_C066itlUL.jpg
tags:
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Testing
  slug: testing
seo_title: 2 raisons les plus fréquentes pour lesquelles les développeurs évitent
  d'écrire des tests
seo_desc: Writing tests represents one of those few stages of software development
  that is usually overlooked, even though it may be one of the most important one.
  Developers mention it and usually are either uncomfortable and prefer not to write
  tests for the...
---

Écrire des tests représente l'une de ces rares étapes du développement logiciel qui est souvent négligée, bien qu'elle puisse être l'une des plus importantes. Les développeurs en parlent et sont généralement soit mal à l'aise et préfèrent ne pas écrire de tests pour leur code, soit ont de nombreuses excuses pour ne pas en écrire du tout.

Eh bien, les tests sont importants :

* Un bug logiciel dans une machine de radiothérapie Therac-25 [a causé](https://www.newscientist.com/gallery/software-bugs/) la mort de cinq patients après avoir reçu une dose massive de rayons X.

* Knight Capital [a perdu](https://www.newscientist.com/gallery/software-bugs/) un demi-milliard de dollars en une demi-heure lorsqu'un bug logiciel a permis aux ordinateurs d'acheter et de vendre des millions d'actions sans surveillance humaine.

Ces histoires et bien d'autres montrent comment des bugs en apparence sans importance peuvent en réalité causer tant de catastrophes tragiques.

Nous savons à quel point le logiciel devient crucial dans tous les domaines de notre vie. Nous savons que la sécurité, la stabilité et la justesse de ce logiciel ont une importance cruciale dans nos vies. Alors la question est : pourquoi les développeurs évitent-ils encore d'écrire des tests ?

![Image](https://cdn-media-1.freecodecamp.org/images/wJohG85PObDvIyTlRliAjn-H3nV4GX0BChbQ align="left")

### **Excuse n°1 : « Écrire des tests prend simplement trop de temps. »**

Il est facile de percevoir l'écriture de tests comme prenant trop de temps, par opposition au fait de se lancer directement dans la partie implémentation.

Cela peut être vrai à court terme, mais si nous prenons en considération le temps que vous pourriez potentiellement devoir consacrer à corriger tous les bugs que vous auriez pu éviter en écrivant des tests, alors écrire des tests peut en réalité faire gagner du temps — et même de l'argent — en cours de route.

![Image](https://cdn-media-1.freecodecamp.org/images/slBXRNwprKzehUbYFIIVBZa4IGvzSkxcYgwl align="left")

Les tests n'éliminent pas complètement les bugs (rien ne peut faire cela), mais ils peuvent les réduire considérablement. Ils peuvent même vous donner plus de confiance que vous ne cassez aucune fonctionnalité existante lorsque vous ajoutez de nouvelles fonctionnalités et refactorisez les anciennes.

Les tests vous aident également à gagner du temps et à protéger vos implémentations existantes des programmeurs inexpérimentés qui ont récemment rejoint votre équipe. Si ces nouveaux membres introduisent des bugs, vos tests échoueront. Et lorsque vos tests échouent, vous devenez conscient que quelque chose n'a pas fonctionné.

![Image](https://cdn-media-1.freecodecamp.org/images/PS1Wo1qApAUPAvgrNZu8FqLPXidkC7u0agXF align="left")

Les chefs de projet qui manquent de formation en programmation — et qui ne comprennent donc peut-être pas les complexités de la programmation qui peuvent survenir soudainement — ont tendance à avoir des attentes élevées envers les développeurs de leurs équipes. Ils veulent que les choses soient faites rapidement, et un code prêt pour la production rapidement. Ils peuvent considérer qu'il est déraisonnable de reporter une date limite stricte.

Ces situations peuvent vous mettre dans des positions difficiles — où vous devez choisir entre suivre les meilleures pratiques ou faire les choses rapidement et de manière approximative.

Vous devriez essayer de trouver quelques principes professionnels auxquels vous pouvez vous tenir quoi qu'il arrive. Vous devriez faire de votre mieux pour convaincre votre manager de l'importance des meilleures pratiques, et comment elles portent leurs fruits à long terme. Et si votre manager ne peut pas être convaincu, alors vous pourriez envisager de changer de travail.

### **Excuse n°2 : la peur d'écrire des tests**

![Image](https://cdn-media-1.freecodecamp.org/images/1F0BAyUDX9oJjN5fs5eJ8HSUBXdBiYxqP6A4 align="left")

Il n'est pas surprenant que les développeurs passent la plupart de leurs heures de travail soit à lire du code, à écrire du code, ou à discuter de nouveaux problèmes à résoudre avec du code. En conséquence, ils ont un attachement émotionnel très fort à celui-ci, et préfèrent le traiter comme leur précieuse propriété.

Beaucoup sont convaincus qu'ils sont déjà suffisamment expérimentés, et qu'ils sont capables de couvrir tous les scénarios possibles sans trop d'efforts.

Au fond d'eux, ils peuvent abriter un sentiment d'insécurité. Et soumettre leur code à des tests peut faire resurgir cette insécurité.

Peut-être ont-ils poussé leurs modifications de code vers la branche principale plus rapidement qu'ils n'auraient dû, parce qu'ils veulent avoir l'air d'un employé productif aux yeux de leur manager. Et maintenant, ils ont peur que l'écriture de tests puisse révéler des bugs dans leur code. Ils ont peur d'être exposés comme des programmeurs *moyens* qui ne peuvent pas écrire de code sans bugs.

![Image](https://cdn-media-1.freecodecamp.org/images/kcgPmvyvpOwxsaPNItqdB5dWm6yOEQaWbSs9 align="left")

Eh bien, nous devrions tous nous rendre service et ne jamais laisser notre propre ego nous tromper au point de ne pas écrire de tests. Aussi inconfortable que cela puisse être, nous devrions prendre la responsabilité de notre propre travail. C'est l'une des meilleures façons d'éviter les bugs — des bugs qui peuvent souvent avoir des conséquences tragiques.

Les tests vous permettent d'apporter des modifications importantes à votre code rapidement, car vous pouvez être confiant que tout fonctionne correctement. Lorsque vous êtes habitué à écrire des tests pour votre code, vous pourrez généralement terminer votre travail beaucoup plus rapidement, car vous aurez un retour visuel instantané lorsque quelque chose ne fonctionne pas, comme vous verrez une lumière rouge. En conséquence, vous écrirez également un meilleur code, vous sentirez moins de stress, et vous serez finalement promu, car vous apportez finalement plus de valeur avec le travail que vous faites.

### **Prendre le temps de tester**

![Image](https://cdn-media-1.freecodecamp.org/images/kRuS3l7Q92dpJbvhyNVeVLJi5djfvT7IRXNO align="left")

Les tests ne pourront jamais attraper 100 % des bugs, mais ils contribueront à la sécurité, à la stabilité et à la justesse de votre code. Prenez le temps de les faire.

*Cet article a été initialement publié sur* [*Medium*](https://medium.com/p/why-developers-avoid-writing-tests-until-its-too-late-912e326b5210)