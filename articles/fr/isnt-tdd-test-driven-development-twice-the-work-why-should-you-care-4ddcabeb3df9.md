---
title: Le développement piloté par les tests peut sembler représenter deux fois plus
  de travail — mais vous devriez le faire quand même
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-17T11:25:44.000Z'
originalURL: https://freecodecamp.org/news/isnt-tdd-test-driven-development-twice-the-work-why-should-you-care-4ddcabeb3df9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C1mf126YNJHmaaMUbaYYyQ.png
tags:
- name: General Programming
  slug: programming
- name: Quality Assurance
  slug: quality-assurance
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Le développement piloté par les tests peut sembler représenter deux fois
  plus de travail — mais vous devriez le faire quand même
seo_desc: 'By Navdeep Singh

  Isn’t Test Driven Development (TDD) twice the work? Should you do it anyway?

  The short answer to the first question is NO. On the surface, it may seem like without
  TDD, time is only required to create the feature. With TDD, you need ...'
---

Par Navdeep Singh

Le développement piloté par les tests (TDD) n'est-il pas deux fois plus de travail ? Devriez-vous le faire quand même ?

La réponse courte à la première question est **NON**. En surface, il peut sembler que sans le TDD, le temps nécessaire est seulement celui pour créer la fonctionnalité. Avec le TDD, vous avez besoin de temps pour créer le test ET créer la fonctionnalité, doublant ainsi le temps de développement requis.

Ce que vous ne considérez pas, c'est le temps nécessaire pour les tests de contrôle qualité et le débogage lorsque la fonctionnalité ne fonctionne pas correctement.

> Des études de cas ont été menées avec trois équipes de développement chez Microsoft et une chez IBM qui ont adopté le TDD. Les résultats des études de cas ont indiqué que la densité des défauts pré-livraison des quatre produits a diminué entre 40 % et 90 % par rapport à des projets similaires qui n'utilisaient pas la pratique du TDD.

> Subjectivement, les équipes ont connu une augmentation de 15 à 35 % du temps de développement initial après avoir adopté le TDD. ([source](https://www.microsoft.com/en-us/research/wp-content/uploads/2009/10/Realizing-Quality-Improvement-Through-Test-Driven-Development-Results-and-Experiences-of-Four-Industrial-Teams-nagappan_tdd.pdf))

Cette diminution de 40 à 90 % des défauts pré-livraison signifie que les équipes de contrôle qualité et les clients n'ont pas trouvé et signalé ces problèmes. L'ingénierie n'a pas essayé de recréer des bugs et de développer des correctifs, ce qui a des coûts associés.

![Image](https://cdn-media-1.freecodecamp.org/images/rsCNd3MzBvEUjx9bQ-QYiXjG1vaZ4V35yZCr)
_Nombre d'itérations par tâche_

Lorsqu'on parle de TDD, nous considérons une tâche comme un sous-ensemble d'une exigence qui peut être implémentée en quelques jours ou moins. Les ingénieurs logiciels TDD développent du code de production à travers des itérations rapides, comme le montre la figure ci-dessus.

### Qu'est-ce que le TDD ?

![Image](https://cdn-media-1.freecodecamp.org/images/JWJWnEz2BCL7beWEwIlBRSKv4Qretm6OXGtn)

Le développement piloté par les tests est une approche de l'écriture de logiciels dans laquelle le développeur utilise des spécifications pour façonner la manière dont il implémente une fonctionnalité. Pour faire court, nous le décrivons comme le « cycle rouge-vert-refactorisation ».

Avant d'écrire du code qui ajoute une nouvelle fonctionnalité à une application, le développeur écrit d'abord un test automatisé décrivant comment le nouveau code doit se comporter, et regarde le test devenir rouge (échouer). Il écrit ensuite le code selon la spécification, et le test devient vert (il passe). Enfin, le développeur prend un peu de temps pour s'assurer que le code écrit est aussi propre que possible (refactorisation).

### Pourquoi vous devriez vous soucier du TDD

Les tests automatisés donnent à vos développeurs de logiciels la confiance de faire des changements au logiciel et de savoir qu'aucun bug n'a été créé comme sous-produit.

De plus, cela permet plus d'agilité pour les développeurs qui ne sont pas familiers avec les détails du logiciel de modifier le code source en toute confiance sans introduire d'erreurs.

Discutons de quelques avantages vraiment intéressants du TDD.

#### 1. Le TDD vous aide à prévenir les bugs

![Image](https://cdn-media-1.freecodecamp.org/images/FOKSPU5-luiwfkdcFbOqWqRWYBhJyD3TwncA)

Premièrement, les suites de tests garantissent une couverture de test complète de la base de code, donc les bugs sont moins susceptibles d'apparaître sans être remarqués. Deuxièmement, les suites de tests permettent aux développeurs de résoudre les problèmes potentiels avant que l'application ne soit prête à être mise en production. Enfin, parce que les suites de tests sont constamment maintenues, elles garantissent la qualité du logiciel.

#### 2. Code auto-explicatif (bien documenté)

Parce que la refactorisation du code est une étape intégrée dans le TDD, vous obtenez une base de code beaucoup plus propre au fur et à mesure. Les applications construites avec le TDD tendent à avoir moins de duplication, moins de cas particuliers non réfléchis, et une meilleure architecture globale.

Le test sert de spécification pour ce que le code écrit doit **faire**. Tant que vous écrivez de bonnes histoires, votre équipe de développement devrait être capable de construire exactement ce que vous avez demandé. Si votre équipe accepte d'utiliser le [Développement piloté par les tests d'acceptation](https://en.wikipedia.org/wiki/Test-driven_development#TDD_and_ATDD), vous pouvez même écrire des tests qui décrivent comment vous voulez qu'il fonctionne en anglais simple !

#### 3. Évitez le problème du débogueur

![Image](https://cdn-media-1.freecodecamp.org/images/VFYfcFvkkNINz-pUynhdPkrrXDXYwt6SKECJ)

Typiquement, lorsqu'on parle de technologie en matière de développement logiciel, il existe deux principaux types de tests qui peuvent être intégrés : fonctionnels et non fonctionnels. Ces deux types de pratiques de test sont ensuite divisés en de nombreux types de techniques de test comme vous pouvez le voir ici :

![Image](https://cdn-media-1.freecodecamp.org/images/U4QtKTWFv4bTw1VsmXZTSIfgG2xPwz7gBLTx)
_Et la liste continue_

Il devient vraiment important de stratégiser le plan de test avant le commencement du projet, car cela aide à définir clairement les rôles et responsabilités des développeurs par rapport aux testeurs en matière de test.

Par exemple :

* Les tests unitaires et d'intégration doivent être effectués par les développeurs avant de remettre les builds aux testeurs
* Les tests d'acceptation utilisateur doivent être effectués par les testeurs
* Les tests de performance et les tests d'interface utilisateur doivent être effectués par les deux

Une brève description de quelques méthodologies de test très importantes du diagramme ci-dessus, qui devraient être incluses dans presque tous les plans de test, sont couvertes ci-dessous.

**Les tests unitaires** impliquent de tester des unités individuelles de code source pour déterminer si elles sont aptes à l'emploi. Intuitivement, on peut voir une unité comme la plus petite partie testable d'une application. [**Faking, Mocking, et Stubbing**](https://www.martinfowler.com/articles/mocksArentStubs.html) **sont indispensables lors de l'écriture de tests unitaires pour du code qui a des interactions avec des API.**

**Les tests d'intégration** impliquent une combinaison de deux ou plusieurs « unités » étant testées. Les tests d'intégration vérifient que les composants du logiciel fonctionnent tous ensemble ou s'« intègrent » correctement.

**Les tests de performance** sont utilisés pour s'assurer que les applications logicielles fonctionneront bien sous leur charge de travail attendue. Les fonctionnalités et la fonctionnalité prises en charge par un système logiciel ne sont pas les seules préoccupations. La performance d'une application logicielle, comme son **temps de réponse, sa fiabilité, son utilisation des ressources,** et **son évolutivité**, compte. Le but des tests de performance n'est pas de trouver des bugs, mais d'éliminer les goulots d'étranglement de performance.

#### 4. Vous pouvez prévoir les problèmes

![Image](https://cdn-media-1.freecodecamp.org/images/KGS6NPx9YOIVplTrknkvNnydeZpmVo9pdtPZ)
_Une approche solide de TDD vous alerte des problèmes à l'avance_

L'avantage d'une suite de tests complète est qu'elle vous alerte des changements tôt. Par exemple, si votre flux de paiement cesse de facturer les cartes de crédit des utilisateurs, vous le saurez immédiatement, car les tests échoueront. Cela signifie également que si quelqu'un fait une erreur et que quelque chose ne fonctionne pas comme prévu, cela sera évident.

C'est bien, car cela vous donnera une chance de le corriger avant qu'il ne passe en production. Si cela devient nécessaire plus tard, vous pouvez même commencer une campagne de refactorisation approfondie sans crainte, car vous aurez une suite de tests solide qui restera verte.

#### 5. Économisez de l'argent

![Image](https://cdn-media-1.freecodecamp.org/images/dCY0sc49bVWFBMBR5Fk-dKyUTTjEEnwDBvMw)

Lorsque le code est compliqué, il devient beaucoup plus difficile de faire quoi que ce soit — un petit changement ici peut entraîner un gros problème là-bas. En suivant le TDD, les développeurs peuvent faire des changements en toute confiance et votre équipe de contrôle qualité attrapera moins de régressions. En termes de développement, **« le temps économisé est égal à l'argent gagné »**.

#### 6. Investissez le temps économisé dans l'innovation et la recherche

![Image](https://cdn-media-1.freecodecamp.org/images/u7Z0aFmVNsdtWOYuf2Z80vDXQKgG1DfuL83g)
_Utilisez le temps économisé pour l'innovation_

Si nous adoptions simplement une approche TDD, une grande partie de cet argent (le temps économisé comme exprimé au point 5) pourrait être dépensée pour de nouvelles innovations.

#### **7. Le TDD vous aide à éviter le glissement de périmètre**

Le cauchemar de tout chef de projet est le glissement de périmètre — toute croissance inattendue dans le périmètre du travail qui entraîne des retards dans la livraison du projet.

Le glissement de périmètre peut se produire pour diverses raisons : tâches mal définies, mauvaise interprétation des exigences du projet, manque de documentation, etc. Il existe de nombreuses méthodes visant à atténuer le glissement de périmètre, et le TDD en est une.

Merci d'avoir lu ! Veuillez le partager si vous l'avez trouvé utile :)