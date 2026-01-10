---
title: Allez vite et ne cassez rien
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-28T15:44:51.000Z'
originalURL: https://freecodecamp.org/news/how-test-driven-development-increased-my-confidence-of-shipping-new-code-without-breaking-things-a759a570bd95
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZQnE-uRaQeaJBXgJB5D9Fg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Allez vite et ne cassez rien
seo_desc: 'By Guido Schmitz

  An intro to Test Driven Development

  When I started writing code, I never wrote any tests. I assumed that my code didn’t
  contain any bugs. I sort of figured that everything would just keep on working when
  I changed a line of code here...'
---

Par Guido Schmitz

#### Une introduction au Développement Piloté par les Tests

Quand j'ai commencé à écrire du code, je n'écrivais jamais de tests. Je supposais que mon code ne contenait aucun bug. Je pensais plus ou moins que tout continuerait à fonctionner lorsque je changerais une ligne de code ici ou là, ou que j'ajouterais de nouvelles fonctionnalités entièrement.

Mon dieu, comme je me trompais.

Alors que mon application restait fonctionnelle, des bugs étranges ont commencé à apparaître. Et les choses ont empiré à mesure que ma base de code grandissait.

Bientôt, j'ai commencé à stresser à chaque fois que j'ajoutais du nouveau code à ma base de code, pensant que ma prochaine ligne de code pourrait être celle qui ferait planter toute l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AmCx9MGHN-tz9_HYbOpWkg.gif)

C'est alors que j'ai découvert le Développement Piloté par les Tests (TDD).

Le TDD est une méthodologie qui peut augmenter votre confiance lorsque vous livrez de nouvelles fonctionnalités. Cela vous rend moins susceptible de casser votre application.

Lorsque vous commencez avec le TDD, il y a [trois règles simples](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd) que vous devriez suivre :

1. écrire un test qui échoue avant d'écrire du code de production
2. écrire un test à la fois, et assurez-vous qu'il échoue avant de passer au suivant
3. n'écrire pas plus de code de production que nécessaire pour faire passer le test qui échoue actuellement

Ensuite, vous pouvez refactoriser le code de production que vous avez écrit.

Ce processus dans son ensemble est souvent appelé Red Light (test échoué) -> Green Light (test réussi) -> Refactor

### Récolter les bénéfices

En suivant ces trois règles, le TDD peut vous aider avec :

* **Débogage.** Imaginez travailler sur un projet où vous ne finissez _jamais_ avec plusieurs modules en lambeaux, espérant que vous pourrez somehow les rassembler tous avant la deadline.
* **Courage.** Si vous avez un design et une architecture magnifiques, mais aucun test, vous avez toujours peur de changer le code. En même temps, si vous avez une suite complète de tests, vous pouvez revenir en arrière et refactoriser en toute sécurité le code médiocre.
* **Documentation.** Les tests unitaires sont comme des exemples de code. Lorsque vous voulez savoir comment appeler une méthode, vous aurez des tests à portée de main qui appellent cette méthode de toutes les façons possibles, et ceux-ci ne peuvent pas se désynchroniser avec votre code de production.
* **Design.** Chaque module sera _testable_ par définition. Et un autre mot pour _testable_ est _découplé_. Afin d'écrire vos tests en premier, vous devez découpler les unités que vous testez du reste du système. Cette pratique est inestimable.
* **Professionnalisme.** Étant donné que ces avantages sont réels, le fait est qu'il serait _peu professionnel_ de ne pas adopter la pratique qui les apporte.

### Structurer vos Tests

Chaque test devrait suivre une structure comme celle-ci :

* **Installation** : Mocking une fonction ou ajoutant quelques lignes à votre base de données
* **Exécuter** : Appeler la méthode que vous voulez tester
* **Assertion** : Vérifier que vos résultats sont corrects
* **Nettoyage** : Nettoyer les enregistrements de base de données modifiés ou les objets mockés

Si vous voulez en savoir plus sur la structure des tests, voici une excellente lecture qui vous montrera quelques meilleures (et pires) pratiques pour écrire des tests unitaires :

[**Écrire de grands tests unitaires : meilleures et pires pratiques**](http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/)
[_Quelle est la différence entre un bon test unitaire et un mauvais ? Comment apprendre à écrire de bons tests unitaires ? C'est loin..._blog.stevensanderson.com](http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/)

### Intégrer le TDD dans votre flux de travail

Permettez-moi de vous guider à travers un exemple de ce à quoi cela pourrait ressembler avec un exemple pas à pas de TDD dans le monde réel.

Nous allons créer une fonction qui détecte un format de mention spécifique dans une chaîne et le remplace par le nom de l'utilisateur. Le format de mention ressemble à ceci :

@(userId)

Maintenant que nous avons un cas simple, nous allons écrire un test pour celui-ci. Je vais utiliser le framework de test JavaScript [Tape](https://github.com/substack/tape) dans cet exemple car il est relativement facile à utiliser :

J'ai créé un fichier appelé _parse-mentionable-text.js_ qui retourne « OK ».

#### Red Light

Laissez-moi exécuter le test pour voir s'il échoue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PorfQkV4VOItPPADuhdohw.png)

Bien. Lorsque le test échoue, nous pouvons être sûrs que la fonctionnalité ne fonctionnait pas lorsque nous avons commencé.

C'est une étape importante. Dans une grande base de code, vous pouvez parfois écrire un test pour une partie de la logique, mais à cause d'un effet secondaire, il peut vous surprendre et réussir alors que vous vous attendez à ce qu'il échoue. Cela signifie que vous devez reconcevoir votre test. Souvenez-vous — vous devez commencer par un test qui échoue.

#### Green Light

Après que notre test a échoué, nous devons faire passer ce test avec un code minimal :

Pour vérifier si notre implémentation répond à nos exigences, nous devons exécuter le test à nouveau :

![Image](https://cdn-media-1.freecodecamp.org/images/1*IbJn7LC0blnbQ4VYOehY1Q.png)

#### Refactor

Super ! Tout fonctionne comme nous le voulons. Maintenant, il est temps de nettoyer le code et de le rendre plus joli et plus lisible :

Le meilleur aspect est qu'après avoir refactorisé votre code, vous pouvez vérifier et voir si la fonction répond toujours à vos exigences en exécutant le test à nouveau.

Écrire des tests en premier changera votre façon de coder. Cela augmentera votre confiance lorsque vous livrerez du nouveau code. Cela diminuera votre peur de casser des choses et vous aidera à avancer plus rapidement.

_Voulez-vous en savoir plus sur le Développement Piloté par les Tests ?_

_Si vous utilisez ReactJS, j'ai également écrit un article sur le test de vos composants React, que vous pouvez consulter [ici](https://medium.com/javascript-world/testing-your-react-components-with-enzyme-5f1c7f185b58#.nsfy9ymuk)._

_Je envoie des articles intéressants sur JavaScript & ReactJS chaque semaine._
_[**Vous pouvez vous abonner ici pour acquérir des connaissances gratuites en JavaScript**](http://bit.ly/1R9Qwd9d2)**.**_

_Oh, et cliquez sur le ? ci-dessous pour que d'autres personnes voient cet article ici sur Medium. Merci d'avoir lu._

![Image](https://cdn-media-1.freecodecamp.org/images/1*prif7-04oPf8Dqo1gvSDsQ.gif)