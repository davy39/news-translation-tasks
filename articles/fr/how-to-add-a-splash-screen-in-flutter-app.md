---
title: Comment ajouter un écran de démarrage à votre application Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-26T16:30:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-splash-screen-in-flutter-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/photo-1603539240352-8f2cce3257c4.jpeg
tags:
- name: Flutter
  slug: flutter
- name: user experience
  slug: user-experience
- name: UX
  slug: ux
seo_title: Comment ajouter un écran de démarrage à votre application Flutter
seo_desc: 'By Krissanawat

  In this article, we''re going to learn how to integrate a splash screen in a Flutter
  app. But first, why is having a splash screen in your app essential?

  What is a Splash Screen?

  A splash screen is an initial screen that gets displayed ...'
---

Par Krissanawat

Dans cet article, nous allons apprendre comment intégrer un écran de démarrage dans une application Flutter. Mais d'abord, pourquoi est-il essentiel d'avoir un écran de démarrage dans votre application ?

## Qu'est-ce qu'un écran de démarrage ?

Un écran de démarrage est un écran initial qui s'affiche dès que l'utilisateur lance l'application, avant que la page principale ne se charge. Il peut ne pas sembler grand-chose car il n'est affiché que pendant une courte durée. Mais les écrans de démarrage peuvent vraiment faire une forte impression car ils sont la première impression de l'application. 

Vous pourriez penser que la plupart des utilisateurs les ignorent. Mais les écrans de démarrage ont un impact, même de manière subconsciente. Ils donnent le ton pour le thème général de l'application et l'expérience utilisateur. 

Considérez un écran de démarrage comme un écran de bienvenue pour votre application. Ils aident également à informer vos utilisateurs lorsqu'il y a un délai de chargement dû à un problème de réseau ou à une autre erreur. Pour toutes ces raisons, nous, en tant que développeurs, devons savoir comment ajouter un écran de démarrage approprié à nos applications mobiles.

## Aperçu de l'écran de démarrage

Puisque les écrans de démarrage sont un élément initial précieux dans toute application, vous devez apprendre à les intégrer correctement. Dans ce tutoriel, nous allons donc apprendre comment le faire dans l'écosystème Flutter. 

Les étapes exactes sont assez simples car nous allons utiliser un package pour nous aider à intégrer l'écran appelé [_splashscreen_](https://pub.dev/packages/splashscreen). Ce package nous permet de définir l'écran de démarrage ainsi que de chronométrer l'apparition de l'écran de démarrage avec seulement quelques lignes de code. Et nous n'avons pas besoin de toucher aux codes natifs. 

Alors, commençons et apprenons comment ajouter un simple écran de démarrage contenant du texte, une image et un indicateur de chargement. 

## Créer un nouveau projet Flutter

Tout d'abord, nous devons créer un nouveau projet Flutter. Pour cela, assurez-vous d'avoir le SDK Flutter et les autres composants liés au développement d'applications Flutter installés. 

Si tout est correctement configuré, pour créer un projet, vous pouvez simplement exécuter la commande suivante dans le répertoire local de votre choix :

```
flutter create splashSceenExample
```

Après la création du projet, naviguez dans le répertoire du projet et exécutez la commande suivante dans le terminal pour exécuter le projet dans un émulateur disponible ou un appareil réel :

```flutter run```

Après sa construction réussie, vous obtiendrez le résultat suivant sur l'écran de l'émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-74.png)

### Comment installer le package splashscreen

Maintenant que notre projet Flutter est opérationnel, nous pouvons installer les dépendances requises. Vous pourriez ajouter un écran de démarrage en modifiant le code natif dans les dossiers Android et iOS – mais si vous n'êtes pas un développeur natif Android ou iOS, ce n'est pas quelque chose que vous devez savoir faire. 

Heureusement, nous avons le package [_splashscreen_](https://pub.dev/packages/splashscreen) qui facilite l'ajout d'un écran de démarrage dans votre application Flutter. Le package offre des widgets et divers paramètres de personnalisation pour mettre en place un simple écran de démarrage introductif dans votre application. 

Pour l'utiliser, vous devez d'abord l'ajouter à vos dépendances. Pour cela, copiez simplement le morceau de code dans l'extrait de code ci-dessous et collez-le dans votre fichier **pubspec.yaml** :

```splashscreen: ^1.3.5```

Le package fournit un widget `SplashScreen` qui vous permet d'afficher un écran de démarrage avant de naviguer vers l'écran principal de votre application.

## Comment ajouter un écran de démarrage à votre application

Maintenant, nous allons utiliser le widget `SplashScreen` fourni par le package _splashscreen_. L'idée est d'appliquer le widget `SplashScreen` au paramètre `home` de votre widget `MaterialApp`. Vous pouvez voir la mise en œuvre globale du codage dans l'extrait de code ci-dessous :

```
class MyApp extends StatelessWidget {
  // Ce widget est la racine de votre application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: SplashScreen(
        seconds: 8,
        navigateAfterSeconds:MyHomePage(title: 'Flutter Demo Home Page'),
        title: new Text(
          'Exemple de SplashScreen',
          style: new TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 20.0,
              color: Colors.white),
        ),
        backgroundColor: Colors.lightBlue[200],
      )
    );
  }
}
```

Dans ce code, nous avons introduit le widget SplashScreen dans le paramètre home de MaterialApp. Il y a plusieurs paramètres que nous avons configurés à l'intérieur du widget `SplashScreen`. Examinons chacun d'eux plus en détail.

* `seconds` : L'option `seconds` vous permet d'entrer le temps en secondes pendant lequel vous souhaitez que l'écran de démarrage soit affiché. 
* `navigateAfterSeconds` : Cette option vous permet de définir le Widget ou l'écran (de préférence l'écran d'accueil de l'application) qui est affiché après la fin de l'écran de démarrage. 
* `title` : Cette option vous permet d'ajouter du texte à votre écran de démarrage. Ici, nous avons utilisé le widget `Text` avec quelques styles pour le faire. 
* `backgroundColor` : Cela vous permet de spécifier la couleur de fond globale de l'écran de démarrage.

D'accord, c'était une configuration simple d'un écran de démarrage avec du texte. Voici à quoi il ressemblera :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/splashGIF1--1-.gif)

Ici, vous pouvez voir que l'écran de démarrage apparaît pendant quelques secondes avant que la page d'accueil par défaut ne se charge. L'indicateur de chargement est également affiché par défaut. 

Mais nous pouvons contrôler la visibilité de l'indicateur de chargement en appliquant le paramètre `useLoader` dans le widget `SplashScreen`, qui peut être vrai ou faux.

### Comment ajouter un indicateur de chargement personnalisé à votre écran de démarrage

Nous avons déjà l'indicateur de chargement en place par défaut. Mais nous pouvons contrôler sa couleur et son style en utilisant les options `loaderColor` comme montré dans l'extrait de code ci-dessous :

```
home: SplashScreen(
        seconds: 8,
        navigateAfterSeconds:MyHomePage(title: 'Flutter Demo Home Page'),
        title: new Text(
          'Exemple de SplashScreen',
          style: new TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 20.0,
              color: Colors.white),
        ),
        backgroundColor: Colors.blue,
        styleTextUnderTheLoader: new TextStyle(),
        loaderColor: Colors.white
      )
```

Maintenant, vous obtiendrez le résultat comme montré dans la démonstration ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/splashGIF2--1-.gif)

Ici, vous pouvez voir que nous avons changé la couleur de l'indicateur de chargement en blanc.

### Comment ajouter une image ou un logo à un écran de démarrage

Maintenant, pour rendre l'écran de démarrage plus attrayant, nous pouvons ajouter une image ou un diagramme – peut-être un logo ou quelque chose de similaire. 

Le widget `SplashScreen` vous offre deux paramètres supplémentaires pour définir correctement le logo dans l'écran de démarrage. L'option `image` vous permet d'ajouter une image à partir de vos actifs ou du réseau, et l'option `photoSize` vous permet de spécifier les dimensions de l'image. 

Il est préférable d'ajouter des images à partir de vos actifs car le chargement des images du réseau dépend de la connectivité et parfois l'image peut ne pas s'afficher en raison d'une connexion Internet lente. 

Nous devons donc obtenir l'image dans notre répertoire **./assets** puis enregistrer le chemin dans notre fichier **pubspec.yaml**. Ensuite, nous pouvons utiliser les options `image` et `photoSize` comme montré dans l'extrait de code ci-dessous :

```
home: SplashScreen(
        seconds: 5,
        navigateAfterSeconds:MyHomePage(title: 'Flutter Demo Home Page'),
        title: new Text(
          'Exemple de SplashScreen',
          style: new TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 20.0,
              color: Colors.white),
        ),
        image: new Image.asset('assets/flut.png'),
        photoSize: 100.0,        
        backgroundColor: Colors.blue,
        styleTextUnderTheLoader: new TextStyle(),
        loaderColor: Colors.white
      )
 ```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/splashGIF3--1-.gif)

Comme vous pouvez le voir, nous avons placé l'image en haut de notre texte. Il existe d'autres options disponibles que vous pouvez explorer via la documentation du package splash screen lui-même. 

Et voilà ! Gardez à l'esprit que cela fonctionne à la fois sur Android et iOS et ne nécessite pas de mises en œuvre séparées.

## Conclusion

Ajouter un écran de démarrage à votre application ne doit pas être difficile, grâce au plugin _splashscreen_. L'objectif principal de ce tutoriel était de vous montrer comment intégrer un écran de démarrage dans votre application Flutter sans avoir à toucher le code natif. 

Ici, vous avez appris comment créer un écran de démarrage et inclure du texte, un indicateur de chargement et une image. Maintenant, le défi est d'utiliser les paramètres restants fournis par le widget `SplashScreen`. 

N'oubliez pas qu'un bel écran de démarrage aide également à atténuer toute anxiété qu'un utilisateur pourrait avoir lors du lancement de votre application. Il offre donc également des avantages pour la santé mentale. 

Gardez simplement à l'esprit que la fonctionnalité du plugin `splashscreen` est un peu limitée. Si vous souhaitez créer un écran de démarrage personnalisé avec un contrôle total sur ce que vous pouvez y ajouter, vous devrez alors vous plonger dans le code natif. Néanmoins, pour les écrans de démarrage simples, ce plugin fait le travail. 

Enfin, vous pouvez trouver de l'inspiration pour votre [application Flutter](http://instaflutter.com/) à partir d'autres applications déjà disponibles.