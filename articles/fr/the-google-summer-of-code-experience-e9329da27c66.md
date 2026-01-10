---
title: Mon expérience avec Google Summer of Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-24T12:39:00.000Z'
originalURL: https://freecodecamp.org/news/the-google-summer-of-code-experience-e9329da27c66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g5RBYeGe0VLB6t_ZsvO_wQ.png
tags:
- name: Google
  slug: google
- name: gsoc
  slug: gsoc
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Mon expérience avec Google Summer of Code
seo_desc: 'By Aswin G

  This article is a quick summary of my experience participating in and completing
  Google Summer of Code 2018 (also referred to as GSoC).


  What is GSoC?

  Google Summer of Code is a program organized by Google to bring student developers
  into ...'
---

Par Aswin G

Cet article est un bref résumé de mon expérience en participant et en complétant le Google Summer of Code 2018 (également appelé GSoC).

![Image](https://cdn-media-1.freecodecamp.org/images/dQWqLEerkgkz8Gu89J3gUymNppjOy2ZscfM4)

### Qu'est-ce que le GSoC ?

Google Summer of Code est un programme organisé par Google pour intégrer les développeurs étudiants dans le développement open source. Comme son nom l'indique, il a lieu chaque été, pendant les mois d'avril à août. Pendant ces mois, les étudiants sélectionnés passent leur été à coder pour l'une des nombreuses organisations open source participant à l'événement.

Les étudiants peuvent parcourir la liste des organisations participant à l'événement, la plupart d'entre elles ayant une page **idées** qui indique quelles parties de leurs projets existants pourraient nécessiter plus de travail. Les étudiants peuvent ensuite soumettre jusqu'à trois propositions à ces organisations. La proposition doit décrire exactement ce que vous prévoyez de faire pendant l'été, et pourquoi vous devriez être la personne choisie pour travailler dessus.

Ensuite, après une attente d'un mois, les étudiants sélectionnés sont annoncés — et après une brève période de "liaison communautaire", ils peuvent commencer à coder. En plus du certificat de **boursier GSoC**, Google encourage davantage la participation en fournissant une bourse à l'étudiant — variant de 6600 $ à 2400 $, selon votre localisation — c'est 2400 $ ici en Inde.

### Quelles sont les organisations open source ? Pourquoi sont-elles importantes ?

![Image](https://cdn-media-1.freecodecamp.org/images/67ID7G4pwqCBmyyLCJ2qAGSL7aixTT3IxZSY)
_Les meilleurs outils sont souvent open source ! (Crédit image : [hackernoon](https://hackernoon.com/lessons-for-creating-good-open-source-software-1b7bbbc13b13" rel="noopener" target="_blank" title="))_

Les organisations open source ont le code de leurs produit(s) sur une plateforme de collaboration, comme GitHub. L'idée ici est qu'une équipe centrale travaillant directement pour l'organisation maintiendra le dépôt de code (et contribuera souvent les plus grandes parties du code) — tandis que n'importe qui d'autre peut contribuer au code, ouvrir des problèmes avec le produit existant, ou utiliser le produit lui-même (gratuitement, généralement).

Les organisations open source sont le pilier de la culture FOSS, qui promeut les logiciels libres et open source, encourage le partage et la collaboration, et tente de rendre les logiciels accessibles à un public plus large en supprimant les restrictions monétaires. Certains des meilleurs produits et outils disponibles sont open source, en particulier dans le monde du développement logiciel où presque tout, des IDE populaires aux langages de programmation eux-mêmes, est open source.

### Être sélectionné

![Image](https://cdn-media-1.freecodecamp.org/images/RcNw3oCUXWpyZZJ9hLavh5MoSOzYavx4TWqe)
_Nous devons tous commencer quelque part ! (Crédit image : [xkcd](https://xkcd.com/" rel="noopener" target="_blank" title="))_

Initialement, puisque j'étais en première année, j'avais prévu de postuler pour le GSoC à la fin de ma deuxième année à l'université — et de passer le temps entre-temps à améliorer mes compétences pour être assez bon pour être sélectionné.

Par curiosité, j'ai décidé de parcourir la liste des organisations GSoC une semaine avant la date limite de soumission des propositions pour voir quels types de projets étaient disponibles. Intéressamment, j'ai trouvé plusieurs projets qui, je pensais, n'étaient pas trop compliqués pour moi.

Après un bref moment de "Oh, je pourrais essayer ça tout de suite", j'ai rapidement rédigé trois propositions pour trois organisations différentes et les ai soumises avant la date limite. La proposition que j'avais soumise pour [Zulip](https://zulipchat.com/), une application de chat de productivité open source, basée sur l'amélioration de l'UI/UX de leur application mobile React Native, a finalement été acceptée.

La plupart des organisations sélectionnent les étudiants qui ont précédemment contribué à leur base de code, car elles auraient une assurance sur la qualité de code que ces étudiants pourraient produire — plutôt que de sélectionner uniquement sur la base de leurs propositions. Les directives de proposition de Zulip demandaient explicitement aux étudiants de soumettre des liens pointant vers leurs contributions précédentes à Zulip et à d'autres organisations open source, ce qui était vide pour moi. Par conséquent, je n'étais pas particulièrement optimiste quant à mes chances d'être sélectionné, mais j'ai décidé d'essayer quand même.

La communication avec les membres de l'organisation est cruciale pour le GSoC. Parfois, vous devrez chercher des canaux IRC ou des listes de diffusion pour établir la communication. Zulip est une application de chat et avait un serveur de chat dédié pour les développeurs. Je m'y suis connecté après la date limite de soumission des propositions et j'ai veillé à m'impliquer dans les conversations qui s'y déroulaient. J'ai résolu quelques problèmes mineurs, soumis un certain nombre de Pull Requests au dépôt mobile de Zulip sur GitHub, les ai mis à jour selon les revues de code et les ai fusionnés.

Bien sûr, il y avait plusieurs autres étudiants qui faisaient de même, mais lorsque les étudiants sélectionnés ont finalement été annoncés, mon nom était sur la liste. C'était la plus grande réalisation que j'avais obtenue jusqu'à présent, et j'étais incroyablement heureux.

### La période de codage

J'ai passé un moment merveilleux à coder avec la communauté fantastique et serviable de Zulip. Mes mentors étaient deux anciens étudiants du GSoC — et avec les administrateurs qui ont soigneusement révisé mon code — ils m'ont expliqué patiemment les erreurs que j'avais commises, le cas échéant, et m'ont aidé à façonner mon code pour atteindre le standard requis pour qu'il soit fusionné.

Un autre avantage agréable de faire partie de Zulip était de participer à la rencontre d'une semaine des membres de Zulip. Faire personnellement connaissance avec l'équipe de codeurs du monde entier était incroyable, et c'était vraiment une expérience qui m'a fait sentir partie de la communauté.

![Image](https://cdn-media-1.freecodecamp.org/images/-65OBR6C6FRClietbCkLkulrVEdsa743O2gt)
_La retraite d'une semaine de Zulip était assez incroyable !_

En bref, je peux définitivement dire que mes compétences en codage se sont améliorées au cours des trois mois du GSoC. Mon git-fu (compétences GitHub) — qui se limitaient au cycle de base `add-commit-push` — s'est significativement amélioré en premier. J'ai dû rebase, réorganiser et diviser les commits pour les mettre dans un ordre qui avait plus de sens.

La plus grande différence entre contribuer à une organisation et à un projet personnel est que le produit de l'organisation est utilisé par des milliers de personnes dans le monde. La base de code existante a été créée par quelqu'un d'autre, et le code que je contribue doit être compréhensible pour une autre personne qui pourrait travailler dessus à l'avenir.

Écrire une documentation claire, structurer votre code pour répondre aux normes, et vous assurer que vos modifications ne cassent rien d'autre a été une expérience vraiment éducative — pour une personne qui avait l'habitude de démanteler et de refactoriser rapidement de grandes parties de code pour faire de la place à de nouvelles fonctionnalités et écrire peu ou pas de documentation pour mes projets de loisir jusqu'alors.

### Conclusion

Google Summer of Code est une excellente opportunité pour les étudiants de travailler sur un projet qui compte vraiment, et d'augmenter exponentiellement leurs compétences en tant que codeur et leur capacité à travailler en grande équipe. Bien sûr, finir avec 2400 $ de plus est également génial :)

À l'avenir, je continuerai à contribuer à Zulip et à faire partie de cette communauté. Je recommande vivement à quiconque a une passion pour le codage et le FOSS de postuler pour le GSoC'19 lorsqu'il sera annoncé, car c'est une expérience mémorable.