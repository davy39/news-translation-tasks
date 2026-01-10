---
title: Pourquoi nous testons — faites les choses plus rapidement avec le Développement
  Piloté par les Tests
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-17T15:40:24.000Z'
originalURL: https://freecodecamp.org/news/why-we-test-do-things-faster-with-test-driven-development-ce00141680e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jit5trmBsttM0DIxOKhizA.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Pourquoi nous testons — faites les choses plus rapidement avec le Développement
  Piloté par les Tests
seo_desc: 'By Rainer Hahnekamp

  As we all know, unit tests provide us with some kind of safety net. They give us
  a program we can use to validate that a system works the way it is supposed to —
  especially after we make modifications or extensions.

  You are doing ...'
---

Par Rainer Hahnekamp

Comme nous le savons tous, les tests unitaires nous fournissent une sorte de filet de sécurité. Ils nous donnent un programme que nous pouvons utiliser pour valider qu'un système fonctionne comme il est censé le faire — surtout après avoir apporté des modifications ou des extensions.

Vous faites beaucoup de travail en amont en écrivant ces tests. Si vous adoptez la perspective selon laquelle le vrai bénéfice vient pendant les phases de maintenance et d'extension, alors vous verrez les tests comme faisant partie de l'embellissement ou du nettoyage.

Dans cet article, je veux montrer que, dans le contexte d'une application web courante, le processus de validation typique prend beaucoup plus de temps que vous ne le pensez et que l'écriture de tests avant le code réel vous permettra de terminer le travail plus rapidement.

#### Vous pouvez penser que les vérifications manuelles sont rapides

La méthode habituelle pour vérifier une modification dans une application web courante consiste à valider son comportement dans un navigateur, comme le ferait un utilisateur final. Cela signifie que vous modifiez le code, rechargez le navigateur, cliquez sur un bouton et voyez si le résultat attendu se produit.

La durée de ce processus dépend beaucoup de votre environnement et de la partie de l'application sur laquelle vous travaillez. Si vous avez la "chance" d'utiliser des frameworks comme Angular et Spring, leur capacité à supporter de grands projets a un prix avec chaque amorçage et compilation. Considérez cet exemple optimiste :

* 10 secondes d'amorçage
* 5 secondes de compilation
* 5 secondes de rechargement et de test

Nous sommes déjà à 20 secondes pour une vérification manuelle. Cela suppose que vos outils de construction côté client et côté serveur, comme Webpack et Maven, sont optimisés.

![Image](https://cdn-media-1.freecodecamp.org/images/1XdNOR82xVsdoCNIlgGw7khYRfNi2RWod0rN)
_Les vérifications manuelles prennent plus de temps que vous ne le pensez_

#### Mais les vérifications prennent plus de temps que vous ne le pensez

Cependant, très souvent, d'autres choses augmentent considérablement le temps de validation. Parfois, nous, les développeurs, négligeons les fautes de frappe lors de la première exécution. Et lors de la deuxième. (Ou de la troisième !) Chacune d'elles multiplie le temps que vous passez à vérifier le code.

Considérez le cas plus sérieux où vous travaillez sur une fonctionnalité de paiement dans une boutique en ligne. Vérifier si un bouton déclenche une action appropriée peut prendre peu de temps. Mais le processus de paiement typique contenant des champs à remplir prendra beaucoup plus de temps. Si vous travaillez sur des tâches de longue durée, cela peut facilement dépasser une minute.

Vous pourriez argumenter que l'utilisation d'un langage interprété pourrait accélérer les choses. C'est vrai, mais le point ici est que vous vous retrouvez facilement avec des cycles de test manuels, chacun durant une minute, plusieurs fois. Et cela, juste pour valider si quelques lignes de code ont eu l'effet désiré.

#### Le TDD accélère les choses

Faire du développement piloté par les tests (TDD) correctement — écrire le test d'abord et le code ensuite — vous place dans une position puissante où vous pouvez exécuter virtuellement n'importe quelle partie spécifique de code isolé en quelques secondes.

Rappelez-vous que les tests unitaires ne testent qu'une seule classe. Toutes les dépendances de cette classe sont simulées — surtout pour les opérations d'I/O comme les bases de données, les systèmes de fichiers ou les réseaux.

Remplacer la validation manuelle par ces tests améliore considérablement la vitesse. Vous obtenez également un code de meilleure qualité, mais nous en parlerons plus tard dans un autre article. La dernière exécution de validation sera la vérification manuelle. C'est là que vous vérifiez réellement si les choses sont telles qu'elles devraient être en tant qu'utilisateur final dans le navigateur.

#### Oui, même pour ces cas particuliers

Vous pouvez toujours trouver des situations où vous trouvez complètement contre-intuitif d'appliquer le TDD.

Pensez à ce que j'appelle le "travail expérimental" — les essais et erreurs que vous devez faire pour découvrir comment utiliser une bibliothèque ou un service que vous ne connaissez pas très bien. Vous travaillez déjà contre un composant inconnu. Pourquoi le compliquer davantage en ajoutant une couche de framework de test autour de votre code principal ?

Ou considérez la phase de démarrage d'une application web où vous travaillez généralement sur la partie front-end — principalement du HTML et du CSS avec une petite partie de code côté serveur qui ne fait que "déplacer" les données de la base de données vers le navigateur.

Dans les deux cas, vous devriez appliquer le TDD dès le début. Créer des tests unitaires pour le "travail expérimental" vous permet de faire la partie essai-erreur plus rapidement et vous équipe d'un ensemble d'outils auquel vous pouvez toujours revenir plus tard. Votre code de "déplacement de données de la base de données vers le navigateur" va croître avec le temps, résultant en une base de code non testable où vous ne pouvez pas exécuter des parties de code isolées les unes des autres. Vous devrez faire les tests manuels chronophages vous-même.

#### Le TDD vaut l'effort

C'est votre responsabilité de trouver des moyens d'arriver à un code testable et de l'intégrer dans votre processus de travail. Quelqu'un vous paie en tant qu'expert. Cette personne ne comprend pas pourquoi vous êtes assis là à attendre qu'une application démarre ou que vous cliquez sur des boutons — un travail qu'une personne moins qualifiée pourrait faire.

Écrire des tests unitaires de la bonne manière est une compétence que vous n'apprenez généralement pas à l'université ou dans une éducation normale en programmation. C'est difficile les premières fois, et cela nécessitera plusieurs heures pour s'adapter, mais vous verrez les premiers résultats bientôt et vous ne regarderez plus jamais en arrière.

Économisez votre temps en investissant dans de bons tests unitaires dès le début et commencez avec une application modulaire dès le premier commit.

_Publié à l'origine sur [www.rainerhahnekamp.com](https://www.rainerhahnekamp.com/en/why-we-test-do-things-faster-with-test-driven-development/) le 15 mars 2017._