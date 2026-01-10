---
title: Comment construire des interfaces utilisateur complexes sans devenir complètement
  fou
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-06T13:21:04.000Z'
originalURL: https://freecodecamp.org/news/3-tips-to-keep-in-mind-while-developing-complex-ui-in-web-b56312310390
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jwBhYQ_c_HZ_OOCE4pwbwQ.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: Comment construire des interfaces utilisateur complexes sans devenir complètement
  fou
seo_desc: 'By Illia Kolodiazhnyi

  I recently built a web application with a complex, dynamic User Interface (UI).
  Along the way, I learned several valuable lessons.

  Here are a few tips I wish someone had told me before I embarked on such an ambitious
  project. Th...'
---

Par Illia Kolodiazhnyi

J'ai récemment construit une application web avec une interface utilisateur (UI) complexe et dynamique. En cours de route, j'ai appris plusieurs leçons précieuses.

Voici quelques conseils que j'aurais aimé que quelqu'un me donne avant de me lancer dans un projet aussi ambitieux. Cela m'aurait fait gagner beaucoup de temps et de sérénité.

### Conseil de sérénité #1 : Utilisez l'état interne d'un composant pour stocker des données temporaires

Une UI complexe nécessite généralement de maintenir un certain type d'état de l'application. Cela indique à l'UI quoi afficher et comment l'afficher. Une option consiste à accéder à cet état dès que l'utilisateur déclenche une action sur la page. Cependant, j'ai appris qu'il existe des situations où il est bénéfique de reporter le changement dans l'état de l'application et de sauvegarder ce changement temporairement dans l'état interne du composant actuel.

Un exemple pour illustrer cela est une fenêtre de dialogue permettant à l'utilisateur de modifier un enregistrement, tel que son nom :

![Image](https://cdn-media-1.freecodecamp.org/images/CPXNaulUTgrgAf8EGe68lSZ4Ia04WkxKuVb1)

Dans ce cas, vous pourriez vouloir déclencher un changement chaque fois que l'utilisateur modifie un champ dans cette fenêtre de dialogue. Mais je vous encourage à maintenir un état interne de cette boîte de dialogue avec toutes les données affichées. Attendez que l'utilisateur appuie sur le bouton Enregistrer. À ce moment-là, vous pouvez changer en toute sécurité l'état de l'application qui contient les données de ces enregistrements.

De cette manière, si l'utilisateur décide d'annuler la modification et de fermer la fenêtre de dialogue, vous pouvez abandonner le composant. Ensuite, l'état de l'application reste intact. Si vous devez envoyer les données au back-end, vous pouvez le faire en une seule requête. Si la même liste est disponible pour d'autres utilisateurs, ils ne verront pas les valeurs temporaires pendant que quelqu'un les modifie.

> Le comportement de votre UI doit correspondre au modèle mental de l'utilisateur

Lorsque les utilisateurs travaillent avec une boîte de dialogue, ils ne considéreront pas l'enregistrement comme terminé tant qu'ils n'auront pas fini de le modifier. La fonctionnalité du composant doit fonctionner exactement comme cela.

_Note pour ceux qui travaillent avec React/Redux :_ ce comportement est réalisable si vous gardez les données générales dans le Redux Store et utilisez l'état du composant React pour stocker des morceaux de données temporaires.

### Conseil de sérénité #2 : Séparer les données du modèle de l'état de l'UI

_Je utilise le terme **modèle** ici en référence à l'entité classique du modèle MVC._

L'UI moderne dans les applications web peut être complexe en structure et en comportement. Cela vous amène généralement à stocker les données purement liées à l'UI dans l'état de votre application. Je recommande de garder les données liées à l'UI et les données métier séparées.

> Stockez les modèles avec les données et la logique métier séparément de l'état de l'UI

Cette approche est plus facile à suivre et à comprendre car elle sépare la logique métier du reste. Vos modèles peuvent contenir à la fois les données ainsi que les méthodes (fonctions, moyens) pour gérer ces données. Sinon, votre application se retrouvera probablement avec une logique métier répartie dans plusieurs endroits, très probablement dans les composants _View_.

Par exemple, vous avez une liste de tâches à faire dans votre application et vous implémentez une page pour ajouter une nouvelle tâche à cette liste. Vous voulez que le bouton Enregistrer soit désactivé jusqu'à ce qu'il y ait à la fois une description expliquant la tâche et une date correctement formatée pour la tâche :

![Image](https://cdn-media-1.freecodecamp.org/images/BN3RqtgyCEclZhIHAbP5L8rZkH0BLUBiuHIq)

La manière naïve serait de stocker les données nécessaires quelque part dans l'état de l'application et d'avoir du code comme `const saveButtonDisabled = !description && !date && !dateIsValid(date)` directement dans votre composant _View_. Mais le problème est que le bouton Enregistrer est désactivé parce qu'il y a une _exigence métier_ d'avoir tous les enregistrements avec des descriptions et des dates appropriées.

Donc, dans ce cas, la logique pour désactiver le bouton doit être placée dans le _modèle_ pour la tâche à faire. Ce modèle peut ressembler à ceci :

```
{    description: 'Sauver Gotham',    date: 'MAINTENANT',    notes: 'Parler avec une voix grave',    dateIsValid: () => this.date === 'MAINTENANT',    isValid: () => this.description !== '' && this.dateIsValid()}
```

Et maintenant vous pouvez utiliser ceci pour votre logique UI `const saveButtonDisabled = !task.isValid()` dans le composant _View_.

Comme vous pouvez le voir, ce conseil consiste essentiellement à garder vos _Modèles_ séparés des _Vues_ dans le modèle MVC.

### Conseil de sérénité #3 : Privilégiez les tests d'intégration aux tests unitaires

Ce n'est pas un problème si vous avez la chance de travailler dans un environnement où vous avez le temps d'écrire plusieurs tests pour chaque fonctionnalité. Mais je suis sûr que ce n'est pas le cas pour la plupart d'entre nous. Habituellement, vous devez décider quel type de test utiliser. **La majorité du temps, je considérerais les tests d'intégration plus précieux que les tests unitaires**.

![Image](https://cdn-media-1.freecodecamp.org/images/fai4O3r2kQvjxPCov-QfQgKBqMRcxRPWR3rF)

Selon mon expérience, j'ai appris que la base de code avec une bonne couverture de tests unitaires est généralement plus sujette aux erreurs que celle avec une bonne couverture de tests d'intégration. J'ai remarqué que la majorité des bugs introduits avec le développement sont des [bugs de régression](https://en.wikipedia.org/wiki/Software_regression). Et les tests unitaires ne sont généralement pas très bons pour les attraper.

Lorsque vous corrigez un problème dans le code, je vous encourage à suivre ces étapes simples :

1. Écrivez un test qui échoue en raison du problème existant. Si cela peut être fait avec un test unitaire, c'est parfait. Sinon, faites en sorte que le test touche autant de modules de code que nécessaire.
2. Corrigez le problème dans la base de code.
3. Vérifiez que le test n'échoue plus.

Cette pratique simple garantit que le problème est résolu et qu'il ne se reproduira pas, car le test le vérifiera.

Les applications web modernes présentent de nombreux défis aux développeurs et le développement d'UI en est un. J'espère que cet article vous aidera à éviter des erreurs ou vous donnera un bon sujet à réfléchir et à discuter.

J'apprécierais grandement de lire vos pensées et découvertes dans les commentaires.