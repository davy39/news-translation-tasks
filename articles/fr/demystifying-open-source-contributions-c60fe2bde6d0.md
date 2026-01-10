---
title: Démystifier les contributions Open Source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-22T14:38:43.000Z'
originalURL: https://freecodecamp.org/news/demystifying-open-source-contributions-c60fe2bde6d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Prw61PsRJRwSoUddoO5bcQ.jpeg
tags:
- name: community
  slug: community
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Démystifier les contributions Open Source
seo_desc: 'By Wassim Chegham

  This quick guide is mainly for first-time contributors and people who want to start
  helping open source projects.


  As an author and maintainer of a bunch of open source projects, I appreciate hearing
  and seeing my projects being use...'
---

Par Wassim Chegham

_Ce guide rapide est principalement destiné aux nouveaux contributeurs et aux personnes qui souhaitent commencer à aider les projets open source._

![Image](https://cdn-media-1.freecodecamp.org/images/r7X7hiwNT6pS1mkawFyctIUFhKczgWbQmRjd)

En tant qu'auteur et mainteneur de plusieurs projets open source, j'apprécie d'entendre et de voir mes projets être utilisés. Et j'aime encore plus quand d'autres développeurs interviennent et offrent leur aide pour corriger et améliorer mes projets.

Dans ce guide rapide, je souhaite vous montrer à quel point il est facile de commencer à contribuer à n'importe quel projet open source. Croyez-moi, c'est essentiellement un jeu d'enfant !

> Je suppose que vous êtes déjà familiarisé avec Git. Si ce n'est pas le cas, voici [un guide complet](https://guides.github.com/activities/hello-world/) pour vous.

#### Identifier le projet sur lequel vous souhaitez travailler

Tout d'abord, commencez par identifier le projet qui vous tient à cœur, ou celui auquel vous vous sentez à l'aise de contribuer. Je conseille généralement aux nouveaux contributeurs de commencer par les projets des outils qu'ils utilisent dans leur travail quotidien. Cela rendra plus facile la contribution à ces outils, puisque vous les connaissez déjà et que vous êtes peut-être déjà conscient de certains problèmes ou fonctionnalités manquantes que vous souhaitez aider à corriger ou à améliorer.

En même temps, il n'y a vraiment rien qui vous empêche de choisir n'importe quel projet auquel vous souhaitez contribuer. Certaines personnes choisissent un projet en fonction de la technologie qu'elles utilisent, d'autres choisissent un projet sans raison particulière, juste pour le défi !

C'est à vous de choisir. Il suffit d'en sélectionner un !

#### Forker le projet

Vous devez forker le projet vers votre compte GitHub (en supposant que vous utilisez [GitHub](https://github.com)) avant de commencer à contribuer. Ce processus copiera essentiellement le projet en amont vers vos propres projets GitHub, afin que vous puissiez avoir votre propre copie du projet sur laquelle travailler.

![Image](https://cdn-media-1.freecodecamp.org/images/-U5Pk9zzGkJhzgB359COR4lRyLqlcNc2J3cN)

#### Cloner et installer les dépendances

L'étape suivante consiste à cloner — télécharger — le projet que vous venez de forker sur votre machine locale afin de pouvoir commencer à travailler — hacker.

![Image](https://cdn-media-1.freecodecamp.org/images/NSC0Id48dj5wzbdUhz8GtFMrAHJv1l20rqta)

Si vous travaillez principalement sur la documentation, la traduction ou la correction de fautes de frappe, c'est quelque chose que vous pouvez définitivement faire directement depuis votre navigateur. Pas besoin de cloner le projet localement. Cependant, si le projet nécessite que vous exécutiez une étape de construction pour la documentation, ou que vous exécutiez un processus de formatage sur la documentation elle-même avant de pousser vos modifications, alors vous devrez cloner le projet localement et installer les dépendances requises.

Une fois que vous avez cloné le projet localement, assurez-vous de lire attentivement le fichier [CONTRIBUTING.md](https://github.com/angular/angular/blob/master/CONTRIBUTING.md) — ou le [README.md](https://github.com/angular/angular#want-to-help) — ou tout autre fichier décrivant toutes les étapes nécessaires pour exécuter et construire le projet localement. En cas de blocage, demandez simplement de l'aide aux mainteneurs du projet et ils seront heureux de vous intégrer.

**Ne soyez pas timide ! Vous offrez votre aide « gratuitement », et les mainteneurs du projet — y compris moi-même — ne peuvent qu'en être reconnaissants !**

#### Ce que vous pouvez faire pour aider

La plupart des nouveaux contributeurs sont généralement confus face à cette étape et à ce qu'elle implique réellement. Clarifions d'abord ce qu'est une « contribution ».

Contribuer à un projet open source ne signifie pas seulement écrire du code et corriger des problèmes techniques. Les contributions open source n'ont littéralement aucune limite ni frontière. Elles peuvent être (des plus rapides aux plus engageantes) :

1. Utiliser l'outil et remercier l'équipe qui travaille dessus,
2. Promouvoir le projet lors d'événements ou en ligne,
3. Aider à répondre aux questions,
4. Corriger les fautes de frappe dans la documentation,
5. Écrire ou traduire de la documentation,
6. Aider à reproduire les bugs et les problèmes signalés,
7. Refactoriser le code existant,
8. Corriger — techniques — les bugs,
9. Écrire des tests unitaires,
10. Implémenter de nouvelles fonctionnalités,
11. Remettre en question la conception architecturale centrale
12. **À vous de jouer !**

C'est essentiellement tout ce que vous pouvez faire pour aider à améliorer un projet.

#### Identifier un problème à « corriger »

Par « corriger », nous entendons « fournir de l'aide ». Je recommande généralement aux nouveaux contributeurs de commencer petit. Choisissez quelque chose que vous pouvez facilement et rapidement corriger. Les fautes de frappe dans la documentation sont idéales. De plus, vous pourrez lire toute la documentation du projet et vous familiariser encore plus avec celui-ci — c'est génial si vous voulez avoir une vue d'ensemble !

Ensuite, écrire ou corriger des tests unitaires est une autre façon facile de commencer à contribuer. Les tests unitaires vous permettent de plonger progressivement dans les détails d'implémentation d'une fonctionnalité spécifique, à votre propre rythme. Si le projet dispose de tests d'intégration, commencez par ceux-ci avant les tests unitaires. De cette manière, vous aurez une compréhension de l'architecture de haut niveau sans vous plonger dans les détails d'implémentation.

Cela dit, vous devriez vous sentir libre de choisir n'importe quel problème que vous vous sentez à l'aise de corriger. Cependant, assurez-vous simplement de faire savoir aux autres contributeurs du projet que vous travaillez sur ce problème particulier en commentant le fil de discussion correspondant sur la page du dépôt du projet.

#### Appliquer la « correction »

Cette étape dépend vraiment du type de problème que vous résolvez. Assurez-vous simplement de lire attentivement les directives de contribution du projet et de vous y conformer. La plupart des projets open source grand public ont un processus strict de directives et de règles de formatage que tous les contributeurs doivent suivre.

De plus, n'hésitez pas à demander de l'aide au mainteneur ou à d'autres contributeurs si vous êtes bloqué ou si vous avez des questions sur quoi que ce soit.

#### Valider et pousser vos modifications

Une fois votre correction prête, vous devriez être fier de vous ! Vous avez fait le travail difficile, le reste n'est qu'une formalité.

Ensuite, vous devez valider et pousser vos modifications vers votre propre copie du projet — celle que vous avez forkée !

Encore une fois, lisez attentivement les directives de contribution du projet et vérifiez comment vous devez formater vos messages de validation et les noms de branches. Chaque projet a sa propre convention. De plus, il est considéré comme une bonne pratique de pousser vos modifications — correction — vers une branche différente de « master » ou « develop », afin que vous puissiez facilement [fusionner ou rebaser](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) vos modifications plus tard — au cas où vous devriez le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/UrAUCrpG7tSDOt6RrvVc3J4-X4EsyBwQDC6O)

Il est généralement apprécié, parfois obligatoire, d'inclure une description détaillée de vos modifications/correction/implémentation dans le corps de la validation. Cela aidera les autres à connaître instantanément les modifications introduites par cette validation.

#### Envoyer une PR — Pull Request

Maintenant, vous êtes prêt à envoyer vos modifications au projet original — le projet en amont. Pour cela, vous devrez ouvrir une Pull Request.

![Image](https://cdn-media-1.freecodecamp.org/images/Oi9p1Em-hkCQ2s4UtWc1RqlwUSpV65Bi5gHs)

Maintenant, envoyez votre PR et croisez les doigts ! Parfois, les mainteneurs du projet vous demanderont de mettre à jour ou de fournir certaines modifications à vos modifications avant de pouvoir fusionner votre PR.

Si les mainteneurs du projet ne peuvent pas fusionner votre PR pour une raison quelconque (généralement technique), ne soyez pas contrarié ou déçu ! Essayez à nouveau ou passez simplement à un autre problème à corriger. C'est tout à fait normal, cela fait partie de la contribution.

J'espère que vous avez maintenant une idée claire des contributions Open Source et de leur facilité.

Santé.

_Suivez-moi [@manekinekko](https://twitter.com/manekinekko) sur Twitter pour plus de mises à jour sur l'Open Source._