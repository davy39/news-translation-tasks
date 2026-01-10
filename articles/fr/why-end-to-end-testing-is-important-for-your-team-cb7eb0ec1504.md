---
title: Pourquoi les tests de bout en bout sont importants pour votre équipe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-04T00:47:45.000Z'
originalURL: https://freecodecamp.org/news/why-end-to-end-testing-is-important-for-your-team-cb7eb0ec1504
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KMFrX776LOznXpsJSfQXVw.jpeg
tags:
- name: code
  slug: code
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Pourquoi les tests de bout en bout sont importants pour votre équipe
seo_desc: 'By Phong Huynh

  How our team implemented end to end testing in 4 easy steps

  At Hubba, our business needs are always evolving and the speed of development needs
  to catch up with it. One of the ways to keep the team moving forward without breaking
  every...'
---

Par Phong Huynh

#### Comment notre équipe a mis en place les tests de bout en bout en 4 étapes faciles

Chez [Hubba](https://www.hubba.com/), nos besoins commerciaux évoluent constamment et la vitesse de développement doit suivre le rythme. L'une des façons de faire avancer l'équipe sans tout casser est le test de bout en bout (E2E).

Avoir une suite de tests complète avec des tests E2E nous permet d'avancer rapidement. Cela permet aux développeurs de **pousser du code sans s'inquiéter de casser des choses**. Cela permet des **versions avec une confiance supplémentaire**. Et cela **attrape les erreurs qui sont manquées** lors des tests de régression manuels.

### Qu'est-ce que le test E2E ?

Le test de bout en bout est un test où vous testez toute votre application du début à la fin. Cela implique de s'assurer que toutes les pièces intégrées d'une application fonctionnent et travaillent ensemble comme prévu.

Les tests de bout en bout simulent des scénarios d'utilisateurs réels, testant essentiellement comment un utilisateur réel utiliserait l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/l0ZO6o8ovUKrS5GgoqrXlNPFbX5dDfDWkgmj)
_[Test E2E](https://twitter.com/Una/status/850451564527591424" rel="noopener" target="_blank" title=")_

Un exemple pour le cas de Hubba serait un cas de test E2E pour l'inscription d'un utilisateur.

Le test impliquerait :

* ouvrir Hubba dans un navigateur et rechercher certains éléments
* effectuer une série de clics et de saisies au clavier
* s'assurer qu'un utilisateur est créé avec succès

### Pourquoi devriez-vous vous en soucier ?

Chez Hubba, nous croyons fortement en l'automatisation des tests. Nous écrivons actuellement des tests unitaires et des tests d'intégration pour notre code.

Ces tests sont utilisés pour :

* spécifier notre système
* prévenir les bugs et les régressions
* effectuer une intégration continue

De plus, ces tests s'exécutent aussi fréquemment que possible pour fournir des commentaires et pour s'assurer que notre système reste propre.

La motivation pour une couche supplémentaire de tests E2E réside dans les avantages d'avoir une suite de tests entièrement automatisée. Ces avantages incluent **l'augmentation de la vitesse des développeurs**, ainsi que d'autres avantages mentionnés précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/8NtBfj6HITU093EGaYhfynsMecih3civAcEY)
_Source : [Giphy](https://giphy.com/gifs/fail-technology-i5RWkVZzVScmY" rel="noopener" target="_blank" title=")_

Les tests E2E nous permettent de couvrir des sections de l'application que les tests unitaires et les tests d'intégration ne couvrent pas. Cela est dû au fait que les tests unitaires et les tests d'intégration ne prennent qu'une petite partie de l'application et évaluent cette partie en isolation.

Même si ces parties fonctionnent bien par elles-mêmes, vous ne savez pas nécessairement si elles fonctionneront ensemble dans leur ensemble. Avoir une suite de tests de bout en bout en plus des tests unitaires et d'intégration nous permet de tester toute notre application.

> Plus le code échoue rapidement, moins nous trouvons de bugs en QA, plus nos cycles de QA sont rapides - [Edward Robinson](https://medium.com/@earobinson)

![Image](https://cdn-media-1.freecodecamp.org/images/2hCjNrylujhop6fe8MXH7vzINh0ek6eqCRqh)
_[Pyramide de l'automatisation des tests](https://blog.kentcdodds.com/write-tests-not-too-many-mostly-integration-5e8c7fff591c" rel="noopener" target="_blank" title=")_

Il s'agit d'une pyramide de tests provenant du [blog de Kent C. Dodds](https://blog.kentcdodds.com/write-tests-not-too-many-mostly-integration-5e8c7fff591c), qui est une combinaison des pyramides du [blog de Martin Fowler](https://martinfowler.com/bliki/TestPyramid.html) et du [blog de test de Google](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html).

La majorité de vos tests se trouvent au bas de la pyramide. En remontant la pyramide, le nombre de tests diminue. En remontant la pyramide, les tests deviennent plus lents et plus coûteux à écrire, exécuter et maintenir.

Nous voulons écrire un très petit nombre de tests de bout en bout en raison du fait qu'ils sont lents à exécuter et sont censés changer. Cela est particulièrement important car en tant que startup, nous voulons avancer rapidement.

> Google suggère souvent une répartition 70/20/10 : 70 % de tests unitaires, 20 % de tests d'intégration et 10 % de tests de bout en bout. Le mélange exact sera différent pour chaque équipe, mais en général, il devrait conserver cette forme de pyramide. - [Blog de test de Google](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

### 4 étapes pour commencer

#### 1. Choisir un Framework de test

La première action que nous avons entreprise pour commencer a été d'évaluer divers frameworks de test E2E. Notre évaluation ne consiste pas à examiner toutes les fonctionnalités d'un framework, mais plutôt à avoir une impression de haut niveau. Le critère principal était de choisir un framework facile à configurer et rapide à démarrer.

Nous avons fait un rapide tour des frameworks suivants : [CasperJS](http://casperjs.org/), [Protractor](http://www.protractortest.org/#/), [Nightwatch](http://nightwatchjs.org/), et [Testcafe](https://devexpress.github.io/testcafe/).

Nous avons décidé d'opter pour TestCafe en raison de l'installation et du lancement faciles. Il est relativement nouveau mais devient populaire. Plus remarquable encore, il est facile à configurer car il ne nécessite pas WebDriver.

Étant donné que WebDriver n'était pas requis, il n'était pas nécessaire d'installer et de maintenir des produits supplémentaires et des plugins de navigateur. Les tests peuvent être exécutés immédiatement après l'installation de npm. Cela nous a permis de rapidement écrire une preuve de concept/prototype qui nous met en route.

![Image](https://cdn-media-1.freecodecamp.org/images/Yc5yLP91UJjzf2T1iOUzubMkcOeHY2pVrKmx)
_Exécution d'un [test d'exemple](https://github.com/DevExpress/testcafe" rel="noopener" target="_blank" title=") dans Safari_

TestCafe utilise async/await et le code ES2017 pour les fichiers de test. Il dispose également d'un mécanisme d'attente automatique implicite, ce qui signifie que TestCafe attend automatiquement les requêtes XHR et les chargements de page. Vous n'avez donc pas besoin de vous en occuper dans votre code.

* Pure Node.js - TestCafe est construit sur Node.js et n'utilise pas Selenium ni n'a besoin de plugins pour exécuter des tests dans de vrais navigateurs. Il s'intègre et fonctionne parfaitement avec les outils de développement modernes.
* Aucune configuration ou installation supplémentaire - TestCafe est prêt à exécuter des tests immédiatement après `npm install`.
* Harnais de test complet - Avec une seule commande de lancement, TestCafe démarre les navigateurs, exécute les tests, collecte les résultats et génère des rapports.

#### 2. Choisir les tests importants

La deuxième étape consistait à déterminer les cas de test principaux que nous écririons pour notre application.

L'un de nos points sensibles concerne les tests de régression QA. Notre cycle d'assurance qualité (QA) consiste en des tests manuels qui incluent un test de régression à la fin.

Ces tests de régression sont un processus manuel qui prend beaucoup de temps et peut potentiellement manquer des choses en raison d'erreurs humaines.

![Image](https://cdn-media-1.freecodecamp.org/images/-YhLeoMwxG-7CtgHnhC5OWzJvZFLZmli1Sjz)
_Connexion de Hubba_

Nous avons décidé d'écrire des cas de test liés à ces tests de régression. Pour Hubba, cela incluait des fonctionnalités de base - mais importantes comme l'inscription/connexion de l'utilisateur et la création d'un produit.

Le premier lot de cas de test :

* Inscription de la marque/acheteur/influenceur
* Connexion
* Créer un produit

#### 3. Intégrer dans un pipeline CI/CD

L'étape suivante consistait à intégrer cela dans un pipeline d'intégration continue et de déploiement continu, ou CI/CD. L'objectif d'ajouter des tests E2E à notre pipeline est de détecter toute erreur ou test échoué avant que le code ne soit déployé en production.

Nous avons pensé à deux façons différentes d'intégrer cela dans notre système.

1. Exécuter les tests chaque fois que du nouveau code est poussé vers le projet.
2. Exécuter les tests périodiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/DmqtpLXgDmGyHRuZv0v1qe8sul4Mntg-OrPc)
_Jenkins_

Nous avons décidé d'exécuter nos tests E2E sur une base nocturne/hebdomadaire périodique plutôt que d'exécuter les tests à chaque changement de code dans le cadre du pipeline CD. La raison en est que les tests E2E sont lents à exécuter.

Nous ne voulons pas que ces tests ralentissent notre pipeline, car cela retarderait notre processus et notre cycle et affecterait les demandes de tirage, les fusions et les déploiements vers différents environnements.

Nous voulions un ensemble de tests E2E principaux que nous pouvons exécuter régulièrement pour nous indiquer si quelque chose ne va pas ou est cassé. C'est pourquoi nous avons décidé d'exécuter ces tests sur une base nocturne via un [travail cron](https://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800) Jenkins.

#### 4. Créer une preuve de concept/prototype

La dernière étape consistait à créer une preuve de concept ou un prototype pour montrer les tests E2E en cours d'exécution, puis à les incorporer dans notre système.

Nous devions également décider soit d'intégrer complètement les tests E2E dans notre base de code actuelle, soit d'avoir un projet ponctuel séparé de la base de code principale.

Pour le prototype initial, nous avons opté pour un nouveau dépôt isolé de notre base de code principale et exécuté nos tests dans l'environnement de staging.

En conclusion, bien que les tests E2E soient très coûteux à maintenir, nous croyons qu'ils sont hautement précieux car ils sont un excellent analogue au comportement de l'utilisateur, ce qui nous aide à tester les fonctionnalités de base de l'utilisateur sur Hubba.