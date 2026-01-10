---
title: Une introduction pratique au Développement Piloté par les Tests
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-01T16:34:33.000Z'
originalURL: https://freecodecamp.org/news/practical-tdd-test-driven-development-84a32044ed0b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Yd-MlvHYafduLBLFkSgH4Q.jpeg
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: test driven development
  slug: test-driven-development
- name: Testing
  slug: testing
seo_title: Une introduction pratique au Développement Piloté par les Tests
seo_desc: 'By Luca Piccinelli

  Test Driven Development is hard! This is the untold truth about it.

  These days you read a ton of articles about all the advantages of doing Test Driven
  Development (TDD). And you probably hear a lot of talks at tech conferences tha...'
---

Par Luca Piccinelli

#### Le Développement Piloté par les Tests est difficile ! Voici la vérité non dite à ce sujet.

De nos jours, vous lisez une tonne d'articles sur tous les avantages du Développement Piloté par les Tests (TDD). Et vous entendez probablement beaucoup de discours lors de conférences techniques qui vous disent de "Faire les tests !", et à quel point c'est cool de les faire. 

Et vous savez quoi ? Malheureusement, ils ont raison (pas nécessairement sur la partie "cool", mais sur la partie utile). **Les tests sont une OBLIGATION !** Les avantages typiques que nous listons lorsqu'il s'agit de parler de TDD sont réels :

* Vous écrivez un meilleur logiciel
* Vous êtes protégé contre la casse du monde lorsque de nouvelles fonctionnalités sont introduites
* Votre logiciel est auto-documenté
* Vous évitez le sur-ingénierie

Même si j'ai toujours été d'accord avec ces avantages, **il fut un temps où je pensais que je n'avais pas besoin de TDD pour écrire un bon logiciel et maintenable.** Bien sûr, maintenant je sais que j'avais tort, mais pourquoi avais-je cette idée malgré la magie étincelante des pros ? La raison est simple : et laissez-moi demander à Rihanna de le dire pour moi...

### **Le Coût !**

Cela coûte cher ! Probablement, quelqu'un pense "mais cela coûte encore plus cher si vous ne faites pas les tests" — et cela est vrai aussi. Mais ces deux coûts arrivent à des moments différents :

* vous faites du TDD ➡ vous avez un coût **maintenant**.
* Vous ne faites pas de TDD ➡ vous aurez un coût **dans le futur**.

Alors, comment sortir de cette impasse ?

La manière la plus efficace de faire quelque chose est de le faire aussi naturellement que possible. La nature des gens est d'être paresseux (ici, les développeurs logiciels sont les meilleurs performeurs) et avides, donc vous devez trouver votre manière de **réduire les coûts maintenant**. C'est facile à dire, mais si difficile à faire !

Ici, je vais partager mon expérience et ce qui a fonctionné pour moi afin de faire pencher le rapport bénéfice/coût en ma faveur.

Mais avant de faire cela, analysons quelques difficultés typiques dans l'application du TDD.

### Êtes-vous capable de tester la somme de deux nombres ?

De manière générale, la théorie n'est pas optionnelle ; vous devez la maîtriser afin de maîtriser la pratique. Cependant, essayer d'appliquer d'un seul coup toutes les connaissances théoriques que vous avez précédemment acquises pourrait avoir l'effet suivant :

La leçon typique de théorie sur le TDD commence par quelque chose comme ceci :

Et vous êtes comme

Ensuite, vient ceci :

* cycle rouge ➡ vert ➡ refactor
* tests unitaires, d'acceptation, de régression, d'intégration
* mocking, stubs, fakes
* si vous avez de la chance (ou peut-être de la malchance ?), quelqu'un vous parlera de contract testing
* et si vous avez beaucoup de chance (ou peut-être beaucoup de malchance ?) vous toucherez au refactoring de codebase legacy

Les choses se compliquent, mais vous êtes un développeur expérimenté et tous ces concepts ne sont pas si difficiles à gérer pour vous. Ensuite, le cours se termine ; vous rentrez chez vous, et au cours des jours suivants, vous faites diligemment quelques code katas pour fixer les concepts nouvellement appris. Jusqu'à présent, tout va bien.

#### La lutte est réelle

Ensuite, vient un projet du monde réel, avec des délais réels et des coûts de timing réels — mais vous êtes motivé à appliquer votre nouveau TDD flambant neuf. Vous commencez à réfléchir à l'architecture de votre logiciel et commencez à écrire des tests pour la première classe et la classe elle-même — appelons-la **Class1**.

Maintenant, vous pensez au premier utilisateur de Class1, appelons-le **UsageOfAClass**, et encore une fois, vous testez et l'écrivez. Class1 est un collaborateur de UsageOfAClass, alors allez-vous le mock ? D'accord, mockons-le. Mais qu'en est-il des interactions réelles de Class1 et UsageOfAClass ? Peut-être devriez-vous les tester également ? Faisons-le.

À ce stade, en vous, vous commencez à entendre une petite voix qui dit "Je développerais beaucoup plus vite si je n'avais pas à écrire ces tests...". Vous n'écoutez pas cette voix maléfique et passez directement au test suivant.

**Class2** va être utilisé par UsageOfAClass et il se persiste lui-même dans une Db. Donc, devons-nous tester Class2, son interaction avec UsageOfAClass, et la persistance dans la Db ? Mais attendez... quelqu'un a-t-il mentionné comment gérer les tests d'I/O pendant le cours de théorie sur le TDD ?

La théorie derrière le TDD n'est pas si difficile à comprendre, mais l'appliquer au monde réel peut être vraiment complexe si vous ne l'abordez pas de la bonne manière.

### Faites-le simplement

Nous devons toujours garder à l'esprit que la théorie doit être adaptée à nos besoins et non l'inverse.

L'objectif principal est de faire le travail. Donc mon conseil est, **faites-le simplement** !

**Commencez simplement et faites votre tâche jusqu'à la fin.** Ensuite, lorsque vous êtes bloqué dans une boucle mentale théorique comme :

* est-ce un test unitaire ou un test d'intégration ?
* ici, devrais-je le mock ou non ?
* oh zut, ici je devrais écrire un nouveau collaborateur, donc une toute nouvelle suite de tests unitaires infinis juste pour écrire "hey, banana"...

oubliez simplement la théorie pendant un moment et faites un pas en avant. Faites-le comme cela vient !

Une fois que vous avez terminé votre tâche, jetez un regard en arrière sur votre travail. **Regarder en arrière** le travail terminé, il sera beaucoup plus facile d'analyser ce qu'aurait été la bonne chose à faire.

### TDD Pratique

Faites-le simplement. D'ailleurs, je pense que c'est aussi la bonne approche pour le TDD.

Qu'est-ce qui n'allait pas dans la façon dont nous avons construit Class1, Class2 et UsageOfAClass ? **L'approche.**

Il s'agit d'une approche bottom-up :

* analyser le problème
* concevoir une architecture
* commencer à la construire à partir de composants unitaires

Cette approche est la meilleure amie du **sur-ingénierie**. Vous construisez typiquement le système afin de prévenir les changements que vous pensez venir dans le futur, sans savoir s'ils viendront réellement. Ensuite, lorsque certaines exigences changent, cela se produit généralement d'une manière qui ne correspond pas à votre structure, peu importe à quel point elle est bonne.

Pour moi, **la clé pour réduire drastiquement le coût immédiat** de l'écriture avec le TDD a été de prendre une approche top-down :

1. apporter une user story
2. écrire un test très simple d'un cas d'utilisation
3. le faire fonctionner
4. revenir à l'étape 2 jusqu'à ce que tous les cas d'utilisation soient complets

Pendant ce processus, ne vous inquiétez pas trop de l'architecture, du code propre (bien, souvenez-vous au moins d'utiliser des noms de variables décents) ou de toute complication qui n'est pas actuellement nécessaire. Faites simplement ce que vous savez que vous avez besoin **maintenant**, jusqu'à la fin.

**Les tests de la story indiquent clairement quelles sont les exigences actuelles et connues.**

Une fois que vous avez terminé, jetez un regard à votre gros ballon de code spaghetti boueux, surmontez la honte, et regardez plus profondément ce que vous avez fait :

* cela fonctionne ! Et les tests le prouvent.
* Tout le système est là, **et juste ce qui est réellement nécessaire pour faire le travail**.

Maintenant, vous avez une vue d'ensemble de toutes les parties de votre système, donc vous pouvez refactoriser avec la connaissance du domaine que vous n'auriez pas pu avoir lorsque vous avez commencé à partir de zéro. Et les tests s'assureront que rien ne cassera pendant le refactoring.

### Refactoring

La meilleure façon pour moi de commencer à refactoriser est d'identifier les zones de responsabilité et de les séparer en méthodes privées. Cette étape aide à identifier les responsabilités et leurs entrées et sorties.

Après cela, les classes de collaborateurs sont presque là et vous devez simplement les déplacer dans différents fichiers.

Au fur et à mesure que vous avancez, écrivez d'abord les tests pour les classes qui émergent du processus et itérez jusqu'à ce que vous soyez satisfait du résultat. Et souvenez-vous, si vous êtes bloqué quelque part, faites-le simplement ! Si vous faites quelque chose de mal, une fois que vous avez terminé, vous aurez plus d'informations sur la façon de surmonter l'erreur la prochaine fois que vous la rencontrerez. **Faire le travail est la priorité**, au mieux de vos capacités actuelles.

De cette façon, si vous analysez vos erreurs pour en tirer des leçons, vous affinerez également vos capacités.

### La prochaine user story

Continuez à développer votre produit en suivant ces étapes :

* prenez une story
* faites-la fonctionner complètement dans un cycle "test — code".
* refactorisez

En ajoutant des fonctionnalités, vous continuerez à modifier votre logiciel et peut-être même sa structure. Mais à mesure que le système grandit, le coût du changement maintiendra une croissance linéaire grâce aux deux principales caractéristiques du TDD :

* découverte de l'architecture (qui aide à contrôler la complexité)
* protection contre les changements cassants

Le système ne sera pas sur-ingénierisé, car l'architecture va émerger à mesure que les stories sont complétées. Vous ne pensez pas à ce que pourraient être les exigences futures ; si vous finissez par en avoir besoin, alors le coût pour l'implémenter sera faible.

#### Qu'est-ce qui peut faire que cela tourne mal ?

La taille de la story. Ce que vous construisez jusqu'à la fin doit être de la bonne taille. Pas trop grande (sinon cela prendra trop de temps pour obtenir un retour) ou trop petite (sinon vous n'aurez pas la vue d'ensemble).

Que faire si la story est trop grande ? Divisez-la en morceaux qui peuvent être construits du début à la fin.

### Qu'est-ce qui suit ?

Dans le prochain article, je donnerai un exemple pratique des concepts que j'ai expliqués ici. Nous implémenterons, étape par étape, le [Bowling Game kata](http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata) en commençant par un test d'acceptation.

Ce n'est pas un problème du monde réel, mais il a suffisamment de complexité pour voir comment le TDD peut aider à le gérer.

Veuillez partager votre opinion et vos suggestions sur cet article. Êtes-vous d'accord avec moi ou pensez-vous que tout cela est un tas de conneries ? Faites-moi savoir ce que vous pensez dans les commentaires ; ce serait très bien de commencer une conversation sur le TDD et de partager nos expériences.

Je tiens à remercier [Matteo Baglini](https://www.freecodecamp.org/news/practical-tdd-test-driven-development-84a32044ed0b/undefined) pour m'avoir aidé à trouver ma voie à travers une approche pratique du développement logiciel et du TDD.

Merci d'avoir lu !

Image de couverture offerte par [testsigma](https://testsigma.com/blog/ai-driven-test-automation/).