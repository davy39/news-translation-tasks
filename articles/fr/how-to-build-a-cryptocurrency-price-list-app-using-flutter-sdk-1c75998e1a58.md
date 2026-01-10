---
title: Comment créer une application de liste de prix de cryptomonnaies en utilisant
  le SDK Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-08T05:50:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-cryptocurrency-price-list-app-using-flutter-sdk-1c75998e1a58
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0umkh4edvLRBJgxiuoVDcA.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: Cryptocurrency
  slug: cryptocurrency
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer une application de liste de prix de cryptomonnaies en utilisant
  le SDK Flutter
seo_desc: 'By Elvis Chidera

  Flutter is Google’s new open-source toolkit for helping developers build iOS and
  Android apps with just one codebase. Flutter apps are written in the Dart programming
  language and compile to native code, so the performance is really,...'
---

Par Elvis Chidera

[Flutter](https://flutter.io) est le nouvel outil **open-source** de Google pour aider les développeurs à créer des applications iOS et Android avec une seule **base de code**. Les applications Flutter sont écrites dans le langage de programmation [Dart](http://dartlang.org) et compilées en code **natif**, donc les performances sont vraiment excellentes.

Dans ce tutoriel, je vais vous montrer comment utiliser Flutter pour créer une application qui affiche le prix actuel de différentes cryptomonnaies. Je vais vous guider à travers les bases de Flutter et Dart.

Avant de commencer, [installez Flutter](https://flutter.io/get-started/install/) et le [plugin de l'éditeur Flutter](https://flutter.io/get-started/editor/) si vous ne l'avez pas déjà fait. L'installation devrait être simple, mais si vous rencontrez des problèmes, vous pouvez laisser un commentaire sur cet article et je serai ravi de vous aider.

Pour ce tutoriel, j'utiliserai [Android Studio](https://developer.android.com/studio/index.html), mais vous pouvez également utiliser [IntelliJ](https://www.jetbrains.com/idea/) ou [Visual Studio Code](https://code.visualstudio.com/).

De plus, une certaine expérience en programmation orientée objet (POO) est requise. Détendez-vous ! Vous n'avez pas besoin de plusieurs années d'expérience — si vous savez ce que sont [les classes et les objets](https://www.techrepublic.com/article/intro-to-oop-understanding-classes-and-objects/), vous devriez être capable de suivre.

#### Commençons

Dans Android Studio ou IntelliJ, cliquez sur le menu **Fichier** -> **Nouveau** -> **Nouveau projet Flutter**. Si vous ne voyez pas l'option Nouveau projet Flutter, assurez-vous d'avoir installé le [plugin Flutter](https://flutter.io/get-started/editor/). Si vous utilisez Visual Studio Code, suivez les [étapes](https://flutter.io/get-started/test-drive/) ici pour créer un nouveau projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oE6SlcmuRJwR-tHRJzpZvA.png)

Lorsque la page s'ouvre, sélectionnez **Application Flutter** et cliquez sur le bouton **Suivant**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SM_ttARLHyGXP38TaxMngA.png)

La page suivante vous permet de configurer le projet. Vous pouvez utiliser une configuration similaire à celle de l'image ci-dessous. Assurez-vous simplement que le chemin du SDK Flutter pointe vers le répertoire où vous avez téléchargé Flutter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uEgNPColbpe8DQTqc5EE5g.png)

La dernière page vous permet de configurer le nom de domaine de votre entreprise, et vous pouvez le définir sur n'importe quel nom de domaine. Après cela, cliquez sur le bouton Terminer.

La création du projet devrait commencer après avoir cliqué sur le bouton Terminer, ce qui prend généralement quelques minutes.

Lorsque c'est terminé, votre projet devrait ressembler à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SOKlN4-dxCw4X-CAN1_ZAA.png)

Un fichier appelé `main.dart` a été créé dans le dossier `lib`. Il contient le code pour une application de démonstration. Puisque nous allons créer notre application à partir de zéro, ouvrez le fichier `main.dart` et supprimez/effacez tout le code qu'il contient.

Si votre projet inclut un répertoire `test` qui contient le fichier `widget_test.dart`, supprimez ce fichier avant de continuer. Il contient des tests pour le code que nous venons de supprimer.

Les applications Flutter sont écrites dans le langage de programmation Dart. Le fichier `main.dart` est un fichier source Dart (extension `.dart`). La convention Dart est de nommer les fichiers sources en utilisant `minuscules_avec_tirets_bas`.

Commençons à écrire un peu de code Dart. Nous commencerons par la tradition de la programmation : imprimer « Hello World! »

Pour cela, nous devons créer quelque chose appelé la fonction `main`. La fonction `main` est une fonction de niveau supérieur que chaque application Flutter possède et qui sert de point d'entrée dans votre application. Pensez-y comme à l'entrée d'une maison.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hC831nn9aLYCdcGaYkDQGw.png)

Lorsque vous exécutez votre application sur un appareil, l'exécution commencera à partir de la fonction main. Créons une simple fonction `main`, alors entrez le code suivant dans votre fichier `main.dart`.

Comme vous pouvez le voir, la création de la fonction `main` est facile. La deuxième ligne contient la déclaration de la fonction `main` : son type de retour (`void`) et son nom (`main`). La fonction main retourne `void`, ce qui signifie qu'elle ne retourne rien.

La troisième ligne effectue l'impression sur la console. Nous appelons la fonction `print` et lui passons un argument de chaîne. Notez qu'en Dart, vous pouvez utiliser des guillemets simples (`'chaîne'`) ou des guillemets doubles (`"chaîne"`) lors de la déclaration d'un littéral de chaîne.

Pour exécuter le code, cliquez sur le bouton d'exécution vert (lecture) en haut d'Android Studio ou IntelliJ. Assurez-vous d'avoir un appareil réel connecté ou un [émulateur en cours d'exécution](https://flutter.io/setup-windows/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*3TYytoIBY2UvLR-VOdR_Cw.png)

Après que l'application a démarré avec succès, vous devriez voir « Hello World! » imprimé sur la console.

![Image](https://cdn-media-1.freecodecamp.org/images/1*smn4mdtI8SzSkRH0c0I3Ew.png)

Mais si vous vérifiez votre appareil ou émulateur, vous verrez quelque chose de décevant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NXFISzRQgevj7BjxiAtIPw.png)
_Un écran vide_

Eh bien, c'était attendu, car nous imprimons actuellement uniquement sur la console. Il n'y avait rien d'ajouté à l'interface utilisateur de l'application, et c'est pourquoi elle est vide.

Alors, corrigeons cela en ajoutant quelques éléments à l'interface utilisateur de l'application. Notre application utilisera le design matériel, alors ajoutons un package au fichier `main.dart` pour nous aider avec cela.

```
import 'package:flutter/material.dart';
```

Comme dans tout langage de programmation moderne, vous pouvez importer une bibliothèque/package à utiliser dans votre code. Ici, nous importons le package `material.dart`. Ce package contient du code qui nous aide à créer une application stylisée avec du matériel.

Le package `material.dart` possède une fonction appelée `runApp`. La fonction `runApp` prend un widget et l'attache à l'écran. Eh bien, qu'est-ce qu'un widget ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*NK6qwYtoWPzPrUptqheOnQ.jpeg)
_Widgets_

Vous pouvez penser aux widgets comme des vues ou des éléments d'interface utilisateur. Ce sont les choses que vous voyez (et certaines que vous ne voyez pas) lorsque vous exécutez votre application sur un appareil. Dans Flutter, vous utiliserez beaucoup de widgets, car l'idée principale est que l'interface utilisateur de votre application est entièrement composée de widgets.

Flutter est déjà livré avec une suite de widgets puissants comme le texte et les images. Le package `material.dart` que nous venons d'importer possède plusieurs widgets de design matériel que nous utiliserons bientôt.

Utilisons maintenant la méthode `runApp` pour afficher « Hello World! » au centre de l'écran de l'appareil. Remplacez le contenu de la fonction `main` par le code ci-dessous.

```dart
void main() {
  print('Hello World!');
  
  // Exécute le widget MaterialApp
  runApp(new MaterialApp(
    // C'est le widget qui est affiché en premier lorsque l'application est démarrée normalement
    home: new Center(
      // Le widget Text est enveloppé dans un widget Center pour le centrer sur l'écran
      child: new Text('Hello World!'),
    ),
  ));
}
```

Permettez-moi d'expliquer certaines des nouvelles choses dans le code ci-dessus

1. `new` : Pour créer un objet, vous utilisez généralement le mot-clé `new` avec un _constructeur_ pour une classe. (POO)
2. `new MaterialApp()` : Ici, nous créons un nouvel objet widget appelé `MaterialApp`. Le widget `MaterialApp` crée un certain nombre de choses utiles nécessaires par une application de design matériel.
3. `home:` : En Dart, nous pouvons clairement indiquer le nom de chaque paramètre dans l'appel de fonction/constructeur. Le widget passé en tant que paramètre `home` est affiché en premier lorsque l'application est démarrée normalement.
4. `new Center(child: new Text('Hello World!'))` : Nous enveloppons le widget Text à l'intérieur d'un widget Center afin que le texte soit centré sur l'écran. Le widget Text est un enfant du widget Center. Oui, les widgets peuvent être imbriqués.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z79-bHQP9bhwSh9IYlaMTA.png)

Si vous exécutez le code à nouveau et ouvrez votre appareil, vous devriez obtenir un écran légèrement meilleur maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gnn1V4u5ClUok_kAeOnl4g.png)

Cool ! Nous avons pu afficher un texte peu attrayant centré sur l'écran de l'appareil.

#### Les prochaines étapes

Faisons maintenant quelques pas en avant. Nous allons obtenir les prix des cryptomonnaies à partir de l'API [CoinMarketCap](https://api.coinmarketcap.com/v1/ticker/). L'API retourne un tableau JSON. Voici un exemple de réponse de l'API :

```
[
    {
        "name": "Bitcoin", 
        "price_usd": "11525.7", 
        "percent_change_1h": "-0.18",
        ...
    },
    ...
]
```

Nous allons faire une requête à l'API CoinMarketCap et décoder le JSON à partir de l'application. Nous allons devoir inclure quelques nouveaux packages dans le fichier `main.dart`.

```
import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;
```

Voici un aperçu des nouveaux packages :

1. `dart:async` : Fournit la classe `Future`, dont je parlerai plus en détail ci-dessous.
2. `dart:convert` : Fournit la variable `json` que nous utiliserons pour décoder la réponse de la chaîne JSON.
3. `package:http/http.dart` : Fournit la fonction que nous utiliserons pour faire des requêtes HTTP GET.

Ajoutons une nouvelle fonction au fichier `main.dart` qui fait une requête à l'API CoinMarketCap.

```

Future<List> getCurrencies() async {
  String apiUrl = 'https://api.coinmarketcap.com/v1/ticker/?limit=50';
  // Faire une requête HTTP GET à l'API CoinMarketCap.
  // Await pause essentiellement l'exécution jusqu'à ce que la fonction get() retourne une Response
  http.Response response = await http.get(apiUrl);
  // Utilisation de la classe JSON pour décoder la chaîne JSON
  return JSON.decode(response.body);
}
```

Analysons le nouveau code

→ `Future<List>` : Nous disons essentiellement que la fonction `getCurrencies()` retournera une `Liste` à un moment donné dans le futur. Elle fera une requête HTTP à l'API CoinMarketCap et retournera une `Liste` de devises une fois terminée.

La fonction `getCurrencies()` est asynchrone. Si vous avez une certaine expérience en JavaScript, vous pouvez penser aux `Futures` comme aux `Promesses`. J'ai créé les images ci-dessous pour vous aider à comprendre les `Futures` en Dart.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YrTpSezcRdjSQl5M6R33IA.png)
_Bob appelle la fonction asynchrone askKateForBalloons() qui retourne un Future<Balloons>_

![Image](https://cdn-media-1.freecodecamp.org/images/1*dyGmD3Z6t0uEFYthWVUq0A.png)
_Bob peut garder le Future<Balloons>_

![Image](https://cdn-media-1.freecodecamp.org/images/1*fj18OGjh4wfy42q5XXTwWg.png)
_Bob peut savoir quand le Future se termine_

→ `async et await` :

Les expressions `Await` vous permettent d'écrire du code asynchrone presque comme s'il était synchrone. La fonction `http.get(url)` est asynchrone, retournant un `Future<Respon`se> immédiatement lorsqu'elle est appelée. Nous voulons attendre la `Re`sponse pour pouvoir décoder la chaîne JSON, mais nous ne voulons pas non plus utiliser de rappels laids.

L'expression `await` évalue `http.get(url)`, puis suspend la fonction actuellement en cours d'exécution (`getCurrencies()`) jusqu'à ce que le résultat soit prêt — c'est-à-dire jusqu'à ce que le Future soit terminé.

Pour utiliser `await`, le code doit être dans une fonction marquée comme asynchrone. Une fonction `async` est une fonction dont le corps est marqué avec un modificateur `async`. Lorsque vous appelez une fonction `async`, elle retourne immédiatement un Future. Le corps de la fonction est planifié pour une exécution ultérieure.

Vous pouvez lire plus sur `async` et `await` en Dart [ici](https://www.dartlang.org/articles/language/await-async).

→ `http.get(url)` : Fait une requête HTTP GET à l'API CoinMarketCap. Cette fonction est asynchrone et retourne un Future immédiatement.

1. `JSON.decode(response.body)` : Décode la réponse de la chaîne JSON.

Testons la fonction `getCurrencies()` que nous venons de créer. Nous le faisons en faisant un appel à celle-ci dans notre fonction `main` et en imprimant la valeur retournée sur la console.

```
// Puisque nous utilisons await dans la fonction main, nous devons également la rendre asynchrone
void main() async {
  // Test de la fonction getCurrencies
  // Nous attendons que les données de devise arrivent
  List currencies = await getCurrencies();
  // Avant de l'imprimer sur la Console
  print(currencies);
  
  runApp(new MaterialApp(
    home: new Center(
      child: new Text('Hello World!'),
    ),
  ));
```

Si vous exécutez le code ci-dessus, vous devriez voir la réponse de l'API imprimée sur la console.

![Image](https://cdn-media-1.freecodecamp.org/images/1*asbOqbSU3_M12wYvbe4vSw.png)

Eh bien, dans le monde réel, de mauvaises choses peuvent arriver. Par exemple, vous n'êtes peut-être pas connecté à Internet, donc la requête à l'API CoinMarketCap échouera. Pour ce tutoriel, nous supposerons que nous sommes à [Wakanda](https://en.wikipedia.org/wiki/Wakanda_(comics)).

Dans une application de production, vous devrez gérer les échecs de réseau. Vous le faites en mettant l'appel HTTP dans un bloc `[try…catch](https://www.dartlang.org/guides/libraries/futures-error-handling)`.

#### Construction de l'interface utilisateur

Maintenant que nous avons une liste de devises, continuons à construire l'interface utilisateur pour afficher cette liste.

Lorsque vous écrivez des applications Flutter, vous créerez généralement de nouvelles classes de widgets. Le travail principal d'un widget est de mettre en œuvre une fonction `build`, qui décrit le widget en termes d'autres widgets de niveau inférieur.

Créons un nouveau Widget appelé CryptoListWidget. Ajoutez le code ci-dessous au bas de votre fichier `main.dart`.

```dart
class CryptoListWidget extends StatelessWidget {
  
  // Il s'agit d'une liste de couleurs matérielles. N'hésitez pas à ajouter plus de couleurs, cela ne cassera pas le code
  final List<MaterialColor> _colors = [Colors.blue, Colors.indigo, Colors.red];
  // Le tiret bas avant un nom de variable le marque comme une variable privée
  final List _currencies;

  // Il s'agit d'un constructeur en Dart. Nous attribuons la valeur passée au constructeur
  // à la variable _currencies
  CryptoListWidget(this._currencies);

  @override
  Widget build(BuildContext context) {
    // Build décrit le widget en termes d'autres widgets de niveau inférieur.
    return new Text('Hello World!');
  }

}
```

Analysons le nouveau code ci-dessus :

1. `StatelessWidget` : Vous créerez généralement des Widgets qui sont des sous-classes de soit `[StatelessWidget](https://stackoverflow.com/questions/47501710/stateful-vs-stateless-widgets-in-flutter)` soit `[StatefulWidget`](https://stackoverflow.com/questions/47501710/stateful-vs-stateless-widgets-in-flutter), selon que votre widget gère un état ou non. Nous utilisons `StatelessWidget` car nous avons déjà nos données et nous ne les mettrons pas à jour dans ce tutoriel.
2. `final List<MaterialColor> _`colors : Les variables `dans un Stateless`Widget doivent être` finales (ce qui signifie qu'elles sont constantes ou ne changent pas). Ici, nous déclarons` une` variable finale qui contient une liste de Materia`lColors. Le tiret bas (_) avant le nom de la variable la rend privée (inaccessible depuis d'autres classes).
3. `CryptoListWidget(this._currencies)` : Il s'agit du constructeur de notre widget. Il attribue la liste de devises que nous passons dans le constructeur à la variable `_currencies`.
4. Fonction `build` : La méthode build retourne un Widget de niveau inférieur (`Text`) qui décrit son apparence.

Remplaçons le widget Text dans la fonction `build` ci-dessus par un nouveau widget appelé `Scaffold`. Le widget `Scaffold` met en œuvre la structure de mise en page visuelle de base du design matériel. Remplacez la fonction `build` ci-dessus par celle ci-dessous.

```dart
@override
  Widget build(BuildContext context) {
    return new Scaffold(
      body: _buildBody(),
      backgroundColor: Colors.blue,
    );
  }
```

La classe Scaffold fournit des API pour afficher des tiroirs, un bouton d'action flottant, une barre inférieure, une barre de notification, etc. Nous ajouterons un bouton d'action flottant plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PsoStgOHjRfZ2C2saoPQEw.png)

Vous devriez obtenir un avertissement que `_buildBody()` n'est pas défini pour la classe `CryptoListWidget`. Continuons à créer la fonction `_buildBody()` à l'intérieur de la classe `CryptoListWidget`.

```dart
Widget _buildBody() {
    return new Container(
      // Une marge supérieure de 56.0. Une marge gauche et droite de 8.0. Et une marge inférieure de 0.0.
      margin: const EdgeInsets.fromLTRB(8.0, 56.0, 8.0, 0.0),
      child: new Column(
        // Un widget de colonne peut avoir plusieurs widgets qui sont placés de haut en bas
        children: <Widget>[
          _getAppTitleWidget(),
          _getListViewWidget()
        ],
      ),
    );
  }
```

La syntaxe ici devrait être familière. Nous utilisons deux nouveaux Widgets :

1. Widget `Container` : Un widget `[Container](https://docs.flutter.io/flutter/widgets/Container-class.html)` est simplement un conteneur :) (pour d'autres widgets).
2. Widget Column : Un widget `[Column](https://docs.flutter.io/flutter/widgets/Column-class.html)` dispose une liste de widgets enfants dans la direction verticale. Il a un paramètre appelé `children` qui prend une liste de widgets.

Créons les deux fonctions que nous avons appelées dans la fonction `_buildBody()`. La première est `_getAppTitleWidget()`.

```dart
Widget _getAppTitleWidget() {
    return new Text(
      'Cryptomonnaies',
      style: new TextStyle(
          color: Colors.white,
          fontWeight: FontWeight.bold,
          fontSize: 24.0),
    );
  }
```

Cette fonction retourne un widget `Text` régulier avec un style qui le rend gras et blanc avec une taille de police de 24.0.

Le texte va ressembler à ceci lorsque nous exécuterons l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fAbESNYbWMV900x1Fq84CA.png)

Nous ne pouvons pas encore exécuter l'application car nous n'avons pas créé l'autre fonction appelée `_getListViewWidget()`. Créons-la rapidement en utilisant le code ci-dessous.

```dart
Widget _getListViewWidget() {
    // Nous voulons que le ListView ait la flexibilité de s'étendre pour remplir
    // l'espace disponible dans l'axe vertical
    return new Flexible(
        child: new ListView.builder(
            // Le nombre d'éléments à afficher
            itemCount: _currencies.length,
            // Rappel qui doit retourner les enfants de ListView
            // Le paramètre index = 0...(itemCount-1)
            itemBuilder: (context, index) {
              // Obtenir la devise à cette position
              final Map currency = _currencies[index];

              // Obtenir la couleur de l'icône. Puisque x mod y, sera toujours inférieur à y,
              // cela sera dans les limites
              final MaterialColor color = _colors[index % _colors.length];

              return _getListItemWidget(currency, color);
            }));
  }
```

La fonction `_getListViewWidget()` retourne un widget `ListView` qui est enveloppé dans un widget `Flexible`. Nous utilisons le `ListView.builder` pour créer facilement la liste. Nous passons un `itemCount` qui indique au constructeur combien de devises afficher.

Le rappel `itemBuilder` sera appelé pour chaque élément et vous devez retourner un nouveau widget. Dans le code ci-dessus, nous appelons une fonction appelée `_getListItemWidget()` qui retourne un Widget.

```dart
CircleAvatar _getLeadingWidget(String currencyName, MaterialColor color) {
    return new CircleAvatar(
      backgroundColor: color,
      child: new Text(currencyName[0]),
    );
  }
```

Avant de créer la fonction `_getListItemWidget()`, créons rapidement les éléments individuels pour le widget d'élément ListView. Nous voulons que chaque élément dans le ListView ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*O3HD57q2Ovl5MPUyndgWUw.png)

Nous avons donc trois widgets principaux :

1. Un widget d'icône ronde avec le premier caractère du nom de la devise
2. Un widget de texte avec le nom de la devise
3. Un widget de texte avec le prix et le pourcentage de changement en 1 heure.

```dart
Text _getTitleWidget(String currencyName) {
    return new Text(
      currencyName,
      style: new TextStyle(fontWeight: FontWeight.bold),
    );
  }

  Text _getSubtitleWidget(String priceUsd, String percentChange1h) {
    return new Text('\$$priceUsd\n1 heure: $percentChange1h%');
  }
```

Créons les widgets. Pour simplifier, j'ai créé une fonction pour chacun d'eux. La première fonction appelée `_getLeadingWidget()` retourne l'icône ronde avec le texte.

Le widget ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QkD7n2hBzTXCL5yiANx2Xg.png)

La deuxième fonction appelée `_getTitleWidget` retourne le widget `Text` pour le nom de la devise.

La troisième fonction appelée _getSubtitleWidget() retourne le widget `Text` pour le prix actuel de la devise et le pourcentage de changement en 1 heure.

Ces deux widgets devraient ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hIF928PlzKa_tOi3CPE0mg.png)

Enveloppons ces trois widgets dans quelque chose appelé un widget `ListTile`. Le widget `ListTile` est basé sur la documentation [Material Design List](https://material.io/guidelines/components/lists.html). Il montre les trois widgets dans ce style.

![Image](https://cdn-media-1.freecodecamp.org/images/1*O3HD57q2Ovl5MPUyndgWUw.png)

Nous allons créer une nouvelle fonction appelée `_getListTile` qui retourne un widget `ListTile`.

```dart
ListTile _getListTile(Map currency, MaterialColor color) {
    return new ListTile(
      leading: _getLeadingWidget(currency['name'], color),
      title: _getTitleWidget(currency['name']),
      subtitle: _getSubtitleWidget(
          currency['price_usd'], currency['percent_change_1h']),
      isThreeLine: true,
    );
  }
```

Enfin, créons la fonction `_getListItemWidget()`. Elle va retourner un widget `Container` qui a un remplissage supérieur de 5.0 et qui a un enfant `Card` widget. Le widget card a le `ListTile` retourné par `_getListTile` comme son enfant.

```dart
Container _getListItemWidget(Map currency, MaterialColor color) {
    // Retourne un widget de conteneur qui a un enfant de carte et une marge supérieure de 5.0
    return new Container(
      margin: const EdgeInsets.only(top: 5.0),
      child: new Card(
        child: _getListTile(currency, color),
      ),
    );
  }
```

Le widget ressemblera à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SFq5wfAj25va2RZkaWX3Kg.png)

Nous avons réussi à compléter notre `CryptoListWidget`. Mais nous devons mettre à jour la fonction `main` pour afficher le widget nouvellement créé au lieu du widget `Text`.

```dart
void main() async {
  // Alerte de mauvaise pratique :). Vous devriez idéalement afficher l'interface utilisateur, et probablement une vue de progression,
  // puis lorsque la requête est terminée, mettre à jour l'interface utilisateur pour afficher les données.
  List currencies = await getCurrencies();
  print(currencies);
  
  runApp(new MaterialApp(
    home: new CryptoListWidget(currencies),
  ));
}
```

C'est tout. Vous pouvez appuyer à nouveau sur le bouton d'exécution. Si tout fonctionne bien et que vous êtes connecté à Internet, vous devriez obtenir un écran qui ressemble à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5UqjvSl_Q9SEJESOoXSJHw.png)

Vraiment cool, n'est-ce pas ?

L'application que vous voyez sera légèrement différente de la capture d'écran ci-dessus :

1. Elle n'a pas de bouton d'action flottant en bas à droite.
2. La couleur du texte du pourcentage de changement en 1 heure est noire.

J'ai décidé de ne pas les inclure dans le tutoriel. Mais vous pouvez consulter le dépôt [Github du projet](https://github.com/Elvis10ten/FlutterCryptocurrencyListApp) pour voir comment j'ai pu les réaliser.

L'application complète peut être téléchargée [ici](https://drive.google.com/file/d/1awcyZCsbeM3qiNHgBb_Jx-On2N3lEh9F/view?usp=sharing).

Merci d'avoir lu et j'espère que vous apprécierez Flutter autant que moi. N'hésitez pas à laisser un commentaire ci-dessous si vous avez des problèmes, des suggestions, etc.