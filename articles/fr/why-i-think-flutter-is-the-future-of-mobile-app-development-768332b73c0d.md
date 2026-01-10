---
title: Pourquoi je pense que Flutter est l'avenir du développement d'applications
  mobiles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-20T17:37:07.000Z'
originalURL: https://freecodecamp.org/news/why-i-think-flutter-is-the-future-of-mobile-app-development-768332b73c0d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YS1KCJ51iHT9vaQAoNOtIA.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Pourquoi je pense que Flutter est l'avenir du développement d'applications
  mobiles
seo_desc: 'By Eric Grandt

  I dabbled a bit in Android and iOS development quite a few years back using Java
  and Objective-C. After spending about a month working with both of them, I decided
  to move on. I just couldn’t get into it.

  But recently, I learned about ...'
---

Par Eric Grandt

Je me suis un peu essayé au développement Android et iOS il y a quelques années en utilisant Java et Objective-C. Après avoir passé environ un mois à travailler avec les deux, j'ai décidé de passer à autre chose. Je n'arrivais tout simplement pas à m'y habituer.

Mais récemment, j'ai découvert Flutter et j'ai décidé de donner une autre chance au développement d'applications mobiles. J'en suis immédiatement tombé amoureux car cela a rendu le développement d'applications multiplateformes très amusant. Depuis que j'ai découvert Flutter, j'ai créé une application et une bibliothèque en l'utilisant. Flutter semble être une avancée très prometteuse et j'aimerais expliquer quelques raisons pour lesquelles je crois cela.

### Alimenté par Dart

Flutter utilise le langage Dart développé par Google. Si vous avez déjà utilisé Java, vous serez assez familier avec la syntaxe de Dart car elles sont assez similaires. En dehors de la syntaxe, Dart est un langage assez différent.

Je ne vais pas parler de Dart en profondeur car cela sort un peu du cadre, mais j'aimerais discuter de l'une des fonctionnalités les plus utiles à mon avis. Cette fonctionnalité étant le support des opérations asynchrones. Non seulement Dart le supporte, mais il le rend exceptionnellement facile.

C'est quelque chose que vous utiliserez probablement dans toutes vos applications Flutter si vous faites des opérations d'E/S ou d'autres opérations chronophages comme l'interrogation d'une base de données. Sans opérations asynchrones, toute opération chronophage fera geler le programme jusqu'à ce qu'elles soient terminées. Pour éviter cela, Dart nous fournit les mots-clés `async` et `await` qui permettent à notre programme de continuer son exécution tout en attendant que ces opérations plus longues se terminent.

Regardons quelques exemples : un sans opérations asynchrones et un avec.

<script src="https://gist.github.com/Erigitic/ff9f18541183586bc090696f756c2ad0.js"></script>

Et le résultat :

<script src="https://gist.github.com/Erigitic/da16af9aa172410efcb6690218929607.js"></script>

Ce n'est pas idéal. Personne ne veut utiliser une application qui gèle lors de l'exécution d'opérations longues. Modifions donc cela un peu et utilisons les mots-clés `async` et `await`.

<script src="https://gist.github.com/Erigitic/f30ae96a17de307b8dc0dcb022ba62ed.js"></script>

Et le résultat une fois de plus :

<script src="https://gist.github.com/Erigitic/342215b537fabb982cb2f68366b86cd5.js"></script>

Grâce aux opérations asynchrones, nous pouvons exécuter du code qui prend un certain temps à se terminer sans bloquer l'exécution du reste de notre code.

### Écrire une fois, exécuter sur Android et iOS

Le développement d'applications mobiles peut prendre beaucoup de temps, car vous devez utiliser une base de code différente pour Android et iOS. À moins d'utiliser un SDK comme Flutter, où vous avez une seule base de code qui vous permet de construire votre application pour les deux systèmes d'exploitation. Non seulement cela, mais vous pouvez les exécuter complètement en natif. Cela signifie que des choses comme le défilement et la navigation, pour n'en nommer que quelques-unes, agissent exactement comme elles le devraient pour le système d'exploitation utilisé.

Pour rester dans le thème de la simplicité, tant que vous avez un appareil ou un simulateur en cours d'exécution, Flutter rend la construction et l'exécution de votre application pour les tests aussi simple que de cliquer sur un bouton.

### Développement de l'interface utilisateur

Le développement de l'interface utilisateur est l'une de ces choses que je n'attends presque jamais avec impatience. Je suis plus un développeur backend, donc quand il s'agit de travailler sur quelque chose qui en dépend fortement, je veux quelque chose de simple. C'est là que Flutter brille à mes yeux.

L'interface utilisateur est créée en combinant différents widgets ensemble et en les modifiant pour qu'ils correspondent à l'apparence de votre application. Vous avez un contrôle presque total sur la façon dont ces widgets s'affichent, donc vous obtiendrez toujours exactement ce que vous cherchez. Pour disposer l'interface utilisateur, vous avez des widgets tels que `Row`, `Column`, et `Container`. Pour le contenu, vous avez des widgets comme `Text` et `RaisedButton`. Ce ne sont que quelques-uns des widgets que Flutter offre, il y en a beaucoup plus. En utilisant ces widgets, nous pouvons construire une interface utilisateur très simple :

<script src="https://gist.github.com/Erigitic/38db5a711b2eac9e0b62bef1561e3386.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/9hlvITfh5FnClzD6qa-xCsnSz-Zngd38EFV8)

Flutter a d'autres tours dans son sac qui rendent le thème de votre application un jeu d'enfant. Vous pourriez passer et changer manuellement les polices, les couleurs et les apparences pour tout, un par un, mais cela prend beaucoup trop de temps. Au lieu de cela, Flutter nous fournit quelque chose appelé `ThemeData` qui nous permet de définir des valeurs pour les couleurs, les polices, les champs de saisie, et bien plus encore. Cette fonctionnalité est idéale pour garder l'apparence de votre application cohérente.

<script src="https://gist.github.com/Erigitic/a08862fc269e3a3062eada0764301200.js"></script>

Avec ce `ThemeData`, nous définissons les couleurs de l'application, la famille de polices et quelques styles de texte. Tout sauf les styles de texte sera automatiquement appliqué à l'ensemble de l'application. Les styles de texte doivent être définis manuellement pour chaque widget de texte, mais c'est toujours simple :

<script src="https://gist.github.com/Erigitic/d5e5a4237de9b7c25834efee064ff8c1.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/55hxft9gL1AxB7U4xIWcebrMTOpS-TY1Y1Xn)
_Application Flutter utilisant le ThemeData ci-dessus_

Pour rendre les choses encore plus efficaces, Flutter peut recharger à chaud les applications afin que vous n'ayez pas besoin de les redémarrer chaque fois que vous apportez une modification à l'interface utilisateur. Vous pouvez maintenant apporter une modification, l'enregistrer, puis voir la modification en une seconde ou deux.

### Bibliothèques

Flutter offre de nombreuses fonctionnalités intéressantes dès la sortie de la boîte, mais il arrive que vous ayez besoin d'un peu plus que ce qu'il offre. Ce n'est pas un problème du tout étant donné le nombre étendu de [bibliothèques disponibles pour Dart et Flutter](https://pub.dev/). Vous souhaitez intégrer des publicités dans votre application ? Il existe une bibliothèque pour cela. Vous voulez de nouveaux widgets ? Il existe des bibliothèques pour cela.

Si vous êtes plus du genre à faire les choses vous-même, créez votre propre bibliothèque et partagez-la avec le reste de la communauté en un rien de temps. L'ajout de bibliothèques à votre projet est simple et peut être fait en ajoutant une seule ligne à votre fichier `pubspec.yaml`. Par exemple, si vous souhaitez ajouter la bibliothèque `sqflite` :

<script src="https://gist.github.com/Erigitic/e708ca4f736df2c09a5a72bb5940fb20.js"></script>

Après l'avoir ajouté au fichier, exécutez `flutter packages get` et vous êtes prêt à partir. Les bibliothèques rendent le développement d'applications Flutter très facile et font gagner beaucoup de temps pendant le développement.

### Développement Backend

La plupart des applications de nos jours dépendent d'une sorte de données, et ces données doivent être stockées quelque part pour pouvoir être affichées et travaillées plus tard. Il est donc important de garder cela à l'esprit lorsque l'on cherche à créer des applications avec un nouveau SDK, comme Flutter.

Une fois de plus, les applications Flutter sont faites en utilisant Dart, et Dart est excellent lorsqu'il s'agit de développement backend. J'ai beaucoup parlé de simplicité dans cet article, et le développement backend avec Dart et Flutter ne fait pas exception à cette règle. Il est incroyablement simple de créer des applications pilotées par les données, pour les débutants et les experts, mais cette simplicité ne signifie en aucun cas un manque de qualité.

Pour lier cela à la section précédente, des bibliothèques sont disponibles afin que vous puissiez travailler avec la base de données de votre choix. En utilisant la bibliothèque `sqflite`, nous pouvons être opérationnels avec une base de données SQLite assez rapidement. Et grâce aux singletons, nous pouvons accéder à la base de données et l'interroger depuis pratiquement n'importe où sans avoir besoin de recréer un objet à chaque fois.

<script src="https://gist.github.com/Erigitic/0553aa7f34798154b4c3401a9892150f.js"></script>

Après avoir récupéré des données d'une base de données, vous pouvez les convertir en objet en utilisant un modèle. Ou si vous voulez stocker un objet dans la base de données, vous pouvez le convertir en JSON en utilisant le même modèle.

<script src="https://gist.github.com/Erigitic/fdb293140f3e05ee91793f4595979c23.js"></script>

Ces données ne sont pas très utiles sans un moyen de les afficher à l'utilisateur. C'est là que Flutter intervient avec des widgets tels que le `FutureBuilder` ou `StreamBuilder`. Si vous êtes intéressé par un regard plus approfondi sur la création d'applications pilotées par les données en utilisant Flutter, SQLite et d'autres technologies, je vous encourage à consulter l'article que j'ai écrit à ce sujet :

**[Utilisation des Streams, BLoCs et SQLite dans Flutter](https://www.freecodecamp.org/news/using-streams-blocs-and-sqlite-in-flutter-2e59e1f7cdce/)**  
[_Les Streams, BLoCs et SQLite constituent une excellente combinaison lorsqu'il s'agit de travailler avec des données dans votre application Flutter..._](https://medium.com/@erigitic/using-streams-blocs-and-sqlite-in-flutter-2e59e1f7cdce)

### Réflexions finales

Avec Flutter, les possibilités sont pratiquement infinies, donc même des applications très étendues peuvent être créées avec facilité. Si vous développez des applications mobiles et que vous n'avez pas encore essayé Flutter, je vous recommande vivement de le faire, car je suis sûr que vous en tomberez amoureux également. Après avoir utilisé Flutter pendant plusieurs mois, je pense qu'il est sûr de dire que c'est l'avenir du développement mobile. Si ce n'est pas le cas, c'est définitivement un pas dans la bonne direction.