---
title: Comment créer un widget personnalisé dans Flutter
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-06-06T15:12:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-custom-widget-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Custom-Widget-in-Flutter
seo_title: Comment créer un widget personnalisé dans Flutter
---

Banner.png
tags:
- name: Flutter
  slug: flutter
- name: développement d'applications mobiles
  slug: mobile-app-development
seo_title: null
seo_desc: "Flutter est devenu de plus en plus populaire ces derniers temps. Vous pouvez l'utiliser pour\n  \ construire des applications complexes qui fonctionnent de manière fluide sur MacOS, Windows et Linux. \n\
  Mais la construction de ces applications n'est pas toujours un processus simple. Vous devez souvent\n  \ refactoriser votre code..."
---

Flutter est devenu de plus en plus populaire ces derniers temps. Vous pouvez l'utiliser pour construire des applications complexes qui fonctionnent de manière fluide sur MacOS, Windows et Linux. 

Mais la construction de ces applications n'est pas toujours un processus simple. Vous devez souvent refactoriser votre code pour maintenir les performances de l'application. 

Une technique de refactorisation consiste à extraire le code et les composants dupliqués et à les réutiliser à plusieurs endroits. 

Dans ce tutoriel, vous apprendrez à remplacer un composant dupliqué en créant un widget personnalisé dans Flutter.

## Qu'est-ce qu'un Widget Personnalisé ?

Dans Flutter, un widget personnalisé fait référence à un widget défini par l'utilisateur qui encapsule un ensemble spécifique de fonctionnalités ou de représentations visuelles. 

Les widgets personnalisés sont les éléments de base d'une application Flutter. Ils permettent aux développeurs de créer des composants d'interface utilisateur réutilisables qui peuvent être utilisés dans toute l'application. 

Si vous passez de React Native, vous pouvez penser aux widgets personnalisés comme à des composants React personnalisés. Et ce que nous appelons `props` dans React sont appelés `paramètres` dans Flutter. 

## Pourquoi Utiliser des Widgets Personnalisés ?

Les widgets personnalisés vous aident à encapsuler des éléments d'interface utilisateur complexes. Ils favorisent également la réutilisabilité du code et améliorent la maintenabilité de vos applications Flutter. 

Il existe plusieurs raisons de créer des widgets personnalisés dans Flutter. Examinons-en quelques-unes.

### Réutilisabilité du Code

Les widgets personnalisés permettent aux développeurs d'encapsuler des fonctionnalités et des apparences complexes dans des composants réutilisables. 

Une fois créés, les widgets personnalisés peuvent être utilisés plusieurs fois dans toute l'application, réduisant la duplication de code et favorisant une approche de développement modulaire.

### Maintenabilité

Les widgets personnalisés contribuent à la maintenabilité de la base de code. En encapsulant des fonctionnalités ou des représentations visuelles spécifiques, les widgets personnalisés créent une séparation des préoccupations. Cette séparation facilite la localisation, la modification et le débogage du code lié à un composant d'interface utilisateur particulier.

### Interface Utilisateur Cohérente

Ils permettent également aux développeurs de définir une conception d'interface utilisateur cohérente et unifiée dans leur application.

### Abstraction

Et enfin, les widgets personnalisés fournissent un niveau d'abstraction qui masque les détails d'implémentation et la complexité d'un élément d'interface utilisateur particulier. 

Vous pouvez créer des widgets de haut niveau qui exposent une interface simplifiée et gèrent la logique interne. Cela permet à d'autres développeurs d'utiliser le widget sans se soucier de son fonctionnement interne. Cette abstraction favorise la modularité, facilitant la compréhension, le test et la maintenance du code. 

## Comment Créer un Widget Personnalisé dans Flutter

Commençons à créer notre widget personnalisé. 

### Cloner le Dépôt

Au lieu de commencer à partir de zéro, j'ai créé une application Flutter sur [GitHub](https://github.com/5minslearn/Flutter-Custom-Widget) et ajouté du code et des composants dupliqués dans ce dépôt. Commençons à partir de là.

Récupérez le code depuis GitHub en exécutant la commande suivante :

```bash
git clone https://github.com/5minslearn/Flutter-Custom-Widget.git

ou

git clone git@github.com:5minslearn/Flutter-Custom-Widget.git
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-67.png)
_Cloner le dépôt Flutter Custom Widget depuis GitHub_

Par défaut, il sera dans la branche `master`. Je passe à une branche `refactor` (vous n'avez pas besoin de le faire) car je veux que vous jetiez un coup d'œil à mon code initial et final. Le code initial sera dans la branche `master` et le code final sera dans la branche `refactor`. 

Exécutez la commande suivante pour installer toutes les dépendances :

```bash
cd Flutter-Custom-Widget/
flutter pub get
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-68.png)
_Installer les dépendances Flutter_

### Exécuter l'Application

Ouvrez le dépôt dans Visual Studio Code et lancez votre émulateur (vous pouvez également connecter votre appareil mobile). Une fois votre émulateur en cours d'exécution, appuyez sur `F5` pour exécuter l'application dans l'émulateur. 

Voici la vue de votre application lors du premier lancement. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-69.png)
_Écran initial de l'application_

Si vous êtes arrivé jusqu'ici, c'est génial. 

### Analyser le Code

Examinons le code. Ouvrez le fichier `lib/main.dart`.

Nous avons une classe `MyApp` appelée au début. Celle-ci appelle à son tour la classe `MyHomePage`.

Voici notre code pour toute l'interface utilisateur qui est définie dans la classe `_MyHomePageState` :

```dart
class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Bienvenue dans le tutoriel de refactorisation Flutter',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20)),
            const SizedBox(height: 16),
            const Text('Appuyez sur le bouton ci-dessous pour me suivre sur Twitter'),
            ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text("Bouton Suivre sur Twitter pressé"),
                    duration: Duration(seconds: 1),
                  ),
                );
                // Ouvrir l'application Twitter
              },
              child: const Text("Suivre sur Twitter"),
            ),
            const SizedBox(height: 16),
            const Text('Appuyez sur le bouton ci-dessous pour me suivre sur Instagram'),
            ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text("Bouton Suivre sur Instagram pressé"),
                    duration: Duration(seconds: 1),
                  ),
                );
                // Ouvrir l'application Instagram
              },
              child: const Text("Suivre sur Instagram"),
            ),
          ],
        ),
      ),
    );
  }
}
```

Et pour que vous puissiez vous référer aux numéros de ligne, voici une visualisation :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-72.png)
_Code pour l'interface utilisateur de l'application_

Si vous êtes quelqu'un qui aime écrire du code propre, vous diriez définitivement que ce code est laid. 

En voici la raison. Regardez attentivement le code – les lignes 44 à 56 et les lignes 58 à 70 sont complètement dupliquées à l'exception de quelques mots soigneusement choisis. Par exemple, le mot « Twitter » a été remplacé par le mot « Instagram ». 

Le codeur propre refactorisera définitivement ce code avant de travailler sur l'ajout de nouvelles fonctionnalités. Suivons également ces pratiques de codage propre maintenant. 

### Refactoriser le Code et Créer un Widget Personnalisé

Nous devons extraire le texte et le bouton dans un composant séparé. Ce composant doit accepter la `plateforme` et `onPressed` comme paramètres. Nous pouvons extraire le texte commun de ceux-ci. 

Ainsi, notre code pour créer le widget personnalisé ressemble à ceci :

```dart
class CustomButton extends StatelessWidget {
  final String platform;
  final VoidCallback onPressed;
  const CustomButton(
      {super.key, required this.platform, required this.onPressed});
  @override
  Widget build(BuildContext context) {
    return Center(
        child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
      Text("Appuyez sur le bouton ci-dessous pour me suivre sur $platform"),
      ElevatedButton(
        onPressed: () {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text("Bouton Suivre sur $platform pressé"),
              duration: const Duration(seconds: 1),
            ),
          );
          onPressed();
        },
        child: Text("Suivre sur $platform"),
      )
    ]));
  }
}
```

Comme nous l'avons discuté ci-dessus, le texte du modèle et les paramètres `platform` et `onPressed`. Nous avons remplacé `platform` partout où nous en avons besoin et appelé la méthode `onPressed` comme extension de l'affichage d'une barre de notification. 

Ajoutez le code ci-dessus à la toute fin du fichier `main.dart`. 

### Intégrer le Widget Personnalisé

Intégrons notre widget personnalisé dans notre code.

Prenez le premier bloc de code de la ligne 44 à 56 comme montré ci-dessous

```dart
            const Text('Appuyez sur le bouton ci-dessous pour me suivre sur Twitter'),
            ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text("Bouton Suivre sur Twitter pressé"),
                    duration: Duration(seconds: 1),
                  ),
                );
                // Ouvrir l'application Twitter
              },
              child: const Text("Suivre sur Twitter"),
            ),
```

Remplacez-le par le code suivant :

```dart
CustomButton(
  platform: 'Twitter',
  onPressed: () {
    // Ouvrir l'application Twitter
  },
),
```

De même, prenez le bloc de code suivant de la ligne 58 à 70 comme montré ci-dessous

```dart
            const Text('Appuyez sur le bouton ci-dessous pour me suivre sur Instagram'),
            ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text("Bouton Suivre sur Instagram pressé"),
                    duration: Duration(seconds: 1),
                  ),
                );
                // Ouvrir l'application Instagram
              },
              child: const Text("Suivre sur Instagram"),
            ),
```

Remplacez-le par le code suivant :

```dart
CustomButton(
  platform: 'Instagram',
  onPressed: () {
    // Ouvrir l'application Instagram
  },
),
```

Voici le code final de la classe `_MyHomePageState` après avoir terminé notre processus de refactorisation. 

```dart
class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Bienvenue dans le tutoriel de refactorisation Flutter',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20)),
            const SizedBox(height: 16),
            CustomButton(
              platform: 'Twitter',
              onPressed: () {
                // Ouvrir l'application Twitter
              },
            ),
            const SizedBox(height: 16),
            CustomButton(
              platform: 'Instagram',
              onPressed: () {
                // Ouvrir l'application Instagram
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

Et voici à nouveau la capture d'écran pour la référence des numéros de ligne :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-73.png)
_Après avoir refactorisé votre code_

Exécutez votre application maintenant. 

Malheureusement, vous ne remarquerez aucun changement dans l'interface utilisateur. Mais votre code sous-jacent a changé. C'est exactement ce qu'est la refactorisation. 

Citant Martin Fowler, 

> **La refactorisation** est une technique disciplinée pour restructurer un corps de code existant, modifiant sa structure interne sans changer son comportement externe. – https://refactoring.com/

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-74.png)
_Application finale_

Vous vous demandez peut-être quelque chose après avoir regardé le code ci-dessus. Les lignes 43 et 50 contiennent également le même code (`const SizedBox(height: 16),`). Alors pourquoi ne pas inclure cela dans le composant ?

C'est une excellente question si vous l'avez eue.

Il n'est pas nécessaire que le composant de widget personnalisé inclue le composant `SizedBox`. Cela est dû au fait que le composant `SizedBox` est ajouté dans la page d'accueil pour donner un peu d'espace entre chaque composant. Mais il n'est pas nécessaire que chaque fois que nous utilisons ce bouton, nous donnions un espace en haut/bas du widget. 

Néanmoins, si de tels cas se présentent, vous pouvez ajouter le widget `SizedBox` à l'intérieur de votre widget personnalisé. 

### Pourquoi Créer un Widget Personnalisé ?

Vous ne verrez peut-être pas de bénéfice direct immédiatement. Mais vous pourriez en faire l'expérience à l'avenir. Voici un exemple rapide pour vous. 

Supposons que vous avez construit cette application pour un client. Elle est devenue une application complexe et vous avez utilisé ce widget personnalisé à environ 20 endroits dans votre application. L'application est publiée et les gens adorent l'utiliser. 

Environ 6 mois plus tard, votre client revient vers vous avec la prochaine version des changements. L'un des éléments de la longue liste est : « Nous apportons un léger changement de thème. Remplacez tous les boutons de référence aux réseaux sociaux pour qu'ils aient une forme en contour et changez la couleur en vert ». 

Il s'agit d'un simple changement de configuration dans le widget personnalisé. Mais imaginez si vous n'aviez pas créé le widget personnalisé et que vous aviez dû copier/coller le même code aux 20 endroits. Vous auriez alors dû examiner soigneusement chaque endroit et remplacer chaque instance avec soin sans toucher aux autres parties du code. 

Ce sont les seules 2 lignes que nous devons changer dans notre widget personnalisé dans cet exemple :

```dart
OutlinedButton(
        style: OutlinedButton.styleFrom(foregroundColor: Colors.green),
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-75.png)
_Changements dans notre widget personnalisé_

Mais si vous n'aviez pas refactorisé votre code, vous auriez dû apporter ce changement à 20 endroits. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-76.png)
_Petit changement reflété partout_

J'ai poussé mon code vers le même [dépôt GitHub](https://github.com/5minslearn/Flutter-Custom-Widget). Référez-vous à la branche `master` pour le code non refactorisé et à la branche `refactor` pour le code refactorisé. 

## Cas d'Utilisation des Widgets Personnalisés

Utilisez toujours des widgets personnalisés pour leurs cas d'utilisation spécifiques. Par exemple, dans notre cas, il s'agit de redirections vers les réseaux sociaux. Ce widget ne doit pas être utilisé dans des endroits sans rapport avec son contexte. 

Si vous le faites, rappelez-vous le cas ci-dessus où l'exigence du client était de changer la conception uniquement des boutons de référence aux réseaux sociaux... mais notre changement serait appliqué à tous les autres endroits où ce widget était utilisé. Cela entraînerait des bugs inattendus. 

Vous devez toujours écrire des cas de test unitaires pour les widgets personnalisés, ce qui vous aidera à atténuer les bugs plus tôt.

Un autre conseil est de nommer votre composant de manière plus lisible. Cela aide les autres développeurs à savoir ce que fait le widget simplement en lisant son nom. 

Dans notre cas, je l'ai nommé `CustomButton` ce qui n'a pas de sens. Au lieu de cela, de bonnes alternatives seraient `SocialMediaButton`, `SocialButton`, etc., qui correspondent à notre cas d'utilisation. 

## Conclusion

Dans ce tutoriel, vous avez appris à créer un widget personnalisé en supprimant le code et les composants dupliqués. 

La création de widgets personnalisés dans Flutter favorise la réutilisabilité du code, la maintenabilité, la cohérence, l'abstraction, la flexibilité et la collaboration communautaire. 

Les widgets personnalisés sont un outil puissant dans la boîte à outils du développeur Flutter, vous permettant de créer des interfaces utilisateur belles et fonctionnelles tout en maximisant l'efficacité et la maintenabilité. 

Si vous souhaitez en savoir plus sur Flutter, abonnez-vous à ma [newsletter par e-mail](https://5minslearn.gogosoon.com/?ref=fcc_flutter_custom_widget) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_flutter_custom_widget)) et suivez-moi sur les réseaux sociaux.