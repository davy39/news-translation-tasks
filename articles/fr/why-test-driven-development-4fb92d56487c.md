---
title: Pourquoi le Développement Piloté par les Tests est-il Utile ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-08T10:59:55.000Z'
originalURL: https://freecodecamp.org/news/why-test-driven-development-4fb92d56487c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1_HDbOMLg5KeS8tYsbpJYg.jpeg
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: TDD (Test-driven development)
  slug: tdd
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi le Développement Piloté par les Tests est-il Utile ?
seo_desc: 'By Fagner Brack

  Tips on how to apply TDD more efficiently, and why it''s a valuable technique

  There''s a common pattern we follow when we start a project using TDD. We describe
  the specifications of what we expect the system to do in the form of a spec...'
---

Par Fagner Brack

#### Conseils pour appliquer le TDD plus efficacement, et pourquoi c'est une technique précieuse

Il existe un schéma commun que nous suivons lorsque nous commençons un projet en utilisant le TDD. Nous décrivons les spécifications de ce que nous attendons du système sous la forme d'un test spécial. Ce "test spécial" peut être un test de bout en bout avec le front-end ou un test d'intégration qui exécute une requête HTTP pour tester le back-end.

C'est le premier test que nous écrivons. Nous le faisons avant qu'une seule ligne de code ne soit écrite. Ce test spécial servira de guide pour nous assurer que nous ne cassons rien qui empêche le flux régulier de fonctionner. Si nous ne le faisons pas et que nous nous appuyons uniquement sur des tests unitaires, il y a une chance que, finalement, nous ayons tous les tests qui passent mais que le serveur ne démarre pas ou que l'utilisateur ne puisse rien faire à l'écran.

> Lorsque vous commencez un projet en utilisant le TDD, il existe un schéma commun pour créer un test spécial afin de vous assurer que vous ne cassez rien qui empêche le flux régulier de fonctionner.

Après avoir fait passer ce test spécial avec une implémentation naïve (ou nous pouvons le garder en échec si nous utilisons l'[ATDD](https://www.agilealliance.org/glossary/atdd/) pour piloter les internes de l'application), nous commençons à construire les unités du système en utilisant un schéma similaire à un niveau micro, sans jamais casser aucun test que nous avons créé précédemment. Nous décrivons chaque unité du système à travers un test en échec et le faisons passer avec une implémentation naïve d'abord. Ensuite, nous identifions les [mauvaises odeurs](https://medium.com/@fagnerbrack/code-smell-92ebb99a62d0) et les [refactorisons](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3) si nécessaire afin de pouvoir continuer le cycle encore et encore.

Cela s'appelle le [cycle Red/Green/Refactor du TDD](http://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html).

Ce cycle nous conduira à construire toutes les pièces de notre application avec suffisamment de confiance pour qu'elle soit robuste et maintenable. Il exposera également les problèmes tôt si nous devions être bloqués en raison d'une mauvaise hypothèse sur la façon dont l'API est censée se comporter.

Il y a une chose importante à laquelle nous devons faire attention : nous devons **éviter de [refactoriser](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3) le code ou d'ajouter un nouveau test pendant qu'un autre test est en échec.** Si nous le faisons, il y a une forte chance que nous soyons bloqués à cause de la charge cognitive inutile de nous soucier d'une autre règle que nous avons déjà couverte. Pour éviter cela, nous devons corriger le test en échec avant de commencer autre chose.

> En TDD, nous devons **éviter de [refactoriser](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3) le code ou d'ajouter un nouveau test pendant qu'un autre test est en échec.**

Il existe des circonstances où l'on préfère écrire des tests après avoir écrit le code. Cependant, il y a quelques effets négatifs qui accompagnent cette approche :

* Nous pouvons manquer des fonctionnalités importantes car il est plus difficile de savoir si la couverture correspond à nos attentes.
* Cela peut [créer des faux positifs](https://medium.com/@fagnerbrack/mocking-can-lean-to-nondeterministic-tests-4ba8aef977a0) car nous ne verrons pas un test en échec en premier.
* Cela peut nous faire [surenchérir](https://hackernoon.com/how-to-accept-over-engineering-for-what-it-really-is-6fca9a919263) l'architecture car nous n'aurons aucune directive pour nous forcer à écrire la quantité minimale de code qui correspond à nos exigences les plus basiques.
* Il est plus difficile de valider si le message pour le test en échec est clair et pointe vers la cause de cet échec ou non.

Une chose à garder à l'esprit est que le TDD peut être posé comme une discipline, mais [il n'y a aucun moyen de créer une discipline pour écrire des tests après le code de production](http://blog.cleancoder.com/uncle-bob/2017/03/07/SymmetryBreaking.html).

Il existe [des cas où il n'y a aucune valeur à appliquer le TDD ou les tests automatisés](https://8thlight.com/blog/uncle-bob/2014/04/30/When-tdd-does-not-work.html) du tout. C'est lorsque nous testons certaines couches d'E/S, des fonctions de support pour les tests, ou des choses construites en utilisant un langage déclaratif comme HTML ou CSS (nous pouvons tester le visuel en CSS, mais pas le code CSS). Cependant, les tests sont une partie fondamentale du processus qui garantit qu'une pièce complexe de fonctionnalité satisfait un ensemble d'attentes. Cela seul nous permet d'être suffisamment confiants que chaque partie du système fonctionne comme prévu.

> Il existe des cas où il n'y a aucune valeur à appliquer le TDD ou les tests automatisés du tout, comme lors du test des couches d'E/S, des fonctions de support pour les tests, ou du code écrit avec un langage déclaratif.

Il existe un concept appelé [The Transformation Priority Premise](https://8thlight.com/blog/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html). Le [TL;DR](https://en.wikipedia.org/wiki/TL;DR) est qu'il existe certaines transformations que nous pouvons appliquer lorsque nous rendons le code plus générique dans la phase "verte" du cycle TDD.

"[Refactoriser](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3)" est lorsque nous changeons la structure du code sans changer son comportement. Les transformations ne sont pas appelées "[refactoring](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3)" car elles changent la structure **et le comportement** du code pour le rendre plus générique.

Un exemple d'utilisation de la Transformation Priority est lorsque nous faisons un test qui nous force à passer du retour d'une constante unique au retour d'un argument qui contiendra plus d'une valeur. Dans ce cas, il s'agit de la transformation de priorité **constant->scalar**.

> _Alors, quelles sont ces transformations ? Peut-être pouvons-nous en faire une liste :_  
>   
> _*** ({}->nil)**_ aucun code du tout -> code qui utilise nil  
>   
> _*** (nil->constant)**_  
>   
> _*** (constant->constant+)**_ une constante simple à une constante plus complexe  
>   
> _*** (constant->scalar)**_ remplacer une constante par une variable ou un argument  
>   
> _*** (statement->statements)**_ ajouter plus d'instructions inconditionnelles.  
>   
> _*** (unconditional->if)**_ diviser le chemin d'exécution  
>   
> _*** (scalar->array)**_  
>   
> _*** (array->container)**_  
>   
> _*** (statement->recursion)**_  
>   
> _*** (if->while)**_  
>   
> _*** (expression->function)**_ remplacer une expression par une fonction ou un algorithme  
>   
> _*** (variable->assignment)**_ remplacer la valeur d'une variable.  
>   
> _Il y en a probablement d'autres._  
>   
> _— Extrait de l'article [The Transformation Priority Premise](https://8thlight.com/blog/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)_

> En TDD, The Transformation Priority Premise peut nous donner une directive pour la phase "verte".

[Écrire un logiciel correct est difficile](https://medium.com/@fagnerbrack/the-trick-to-write-better-software-lies-on-the-technique-944015f84ce4). Le TDD est un schéma commun où nous utilisons les tests pour aider à piloter l'implémentation de notre système tout en conservant un pourcentage élevé de couverture de test. Cependant, ce n'est pas une [solution miracle](https://medium.com/@fagnerbrack/how-to-reject-the-belief-on-the-silver-bullet-1d86b686acbb).

Si nous utilisons le TDD, nous devons éviter de [refactoriser](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3) le code lorsque les tests sont en échec. Pour le faire passer dans la phase "verte", nous utilisons le Transformation Priority Premise pour nous guider dans l'approche d'implémentation la plus naïve que nous pouvons prendre avant de [refactoriser](https://medium.com/@fagnerbrack/how-to-refactor-a-public-interface-317ed18d38a3).

En comparaison avec d'autres façons d'écrire des tests, le TDD peut prendre plus de temps au début. Cependant, comme pour toute nouvelle compétence, avec suffisamment de pratique, nous atteindrons un plateau, et le temps qu'il faut pour appliquer le TDD ne sera pas différent du temps qu'il faudrait pour écrire des tests de manière traditionnelle.

La différence maintenant est que votre logiciel sera moins susceptible de se comporter d'une manière à laquelle vous ne vous attendiez pas.

Et pour tous les moyens pratiques, ce n'est pas différent de 100% de couverture de test.

Merci d'avoir lu. Si vous avez des commentaires, contactez-moi sur [Twitter](https://twitter.com/FagnerBrack), [Facebook](https://www.facebook.com/fagner.brack) ou [Github](http://github.com/FagnerMartinsBrack).