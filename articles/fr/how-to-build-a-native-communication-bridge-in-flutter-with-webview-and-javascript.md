---
title: Comment créer un pont de communication natif dans Flutter avec WebView et JavaScript
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2020-12-01T16:27:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-native-communication-bridge-in-flutter-with-webview-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/0_vBF65VQHbXyUUeHN.jpg
tags:
- name: Flutter
  slug: flutter
- name: mobile
  slug: mobile
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment créer un pont de communication natif dans Flutter avec WebView
  et JavaScript
seo_desc: 'As a follow up to my article explaining how to create communication bridges
  in Android and iOS, I thought it might be a good idea to do the same for Flutter.

  While it may seem like this is a straightforward affair, you’ll soon realize it
  takes a bit ...'
---

En complément de mon [article](https://www.freecodecamp.org/news/how-to-build-cross-origin-communication-bridges-in-ios-and-andriod-7baef82b3f02/) expliquant comment créer des ponts de communication dans Android et iOS, j'ai pensé qu'il serait bon de faire de même pour Flutter.

Bien que cela puisse sembler simple, vous réaliserez rapidement que cela demande un peu de travail pour que cette fonctionnalité fonctionne.

Tout d'abord, il est important de réaliser que (au moment de la rédaction de cet article) Flutter **ne** dispose **pas** d'un support intégré pour les WebViews embarquées.

Contrairement à une application native en Kotlin ou Swift où vous pouvez simplement instancier un composant WebView, vous ne pouvez pas ajouter un composant WebView à votre application Flutter directement.

Dans cet article, nous allons voir comment configurer WebView dans les applications Flutter et comment communiquer entre Flutter et WebView.

## Comment configurer WebView dans une application Flutter

Après avoir créé un nouveau projet Flutter, nous devons utiliser le [package webview_flutter](https://pub.dev/packages/webview_flutter) pour pouvoir utiliser une WebView. Nous allons ajouter la dépendance à notre fichier `pubspec.yaml` :

```yaml
dependencies:  
       flutter:    
           sdk: flutter
       webview_flutter: ^1.0.7
```

Ensuite, nous devons exécuter `pub get` dans le terminal :

```bash
flutter pub get
```

Puis, nous importons le package dans notre fichier `main.dart` :

```dart
import 'package:webview_flutter/webview_flutter.dart';
```

Si vous n'avez pas encore nettoyé le code du projet de départ, c'est le moment de le faire.

Après avoir supprimé tous les commentaires, le bouton d'action flottant et tout ce qui s'y rapporte, il vous restera ceci (j'ai ajouté un widget de texte juste pour l'exemple) :

```dart
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Communication Bridge',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'Native - JS Communication Bridge'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  WebViewController _controller;

  @override
  Widget build(BuildContext context) {
    return Text(
      "Flutter JS-Native Communication Bridge"
    );
  }
}
```

Ce qui donnera ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_txc-SxRUBZFMR4mdJq-tCA.png)

### Créer un fichier HTML local

Puisque nous allons utiliser un fichier HTML local avec du code JavaScript intégré, nous devons le créer dans notre projet.

Tous les fichiers locaux dans une application Flutter doivent être dans un répertoire `assets`.

Créez un répertoire `assets` dans votre hiérarchie de projet principale en cliquant avec le bouton droit dans le panneau de gauche et en choisissant Nouveau → Directory :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_xlBwiAWJUdKiZWDsAdx7SQ.png)
_La hiérarchie des fichiers après la création du répertoire assets_

Ensuite, créez `index.html` dans le répertoire assets et ajoutez le code suivant :

```html
<html>

    <head>
        <title>My Local HTML File</title>
    </head>

    <body>
        <h1 id="title">Hello World!</h1>
        <script type="text/javascript">
            function fromFlutter(newTitle) {
                document.getElementById("title").innerHTML = newTitle;
                sendBack();
             }

             function sendBack() {
                messageHandler.postMessage("Hello from JS");
             }
        </script>
    </body>
</html>
```

Vous remarquerez que nous avons écrit deux méthodes dans la section JavaScript de notre HTML :

1. `fromFlutter` est la méthode que nous allons appeler depuis Flutter avec une chaîne représentant le nouveau titre de la page.
2. `sendBack` est la méthode que nous allons appeler pour communiquer avec Flutter. Dans celle-ci, nous envoyons un message texte.

Nous allons revenir sur le contenu de `sendBack` dans un instant, mais avant cela, nous devons configurer notre WebView dans notre application.

💡 N'oubliez pas d'ajouter `index.html` à votre fichier `pubspec.yaml` sous une section `assets` (utilisez l'indentation correcte) :

```yaml
dependencies:
  flutter:
    sdk: flutter
  webview_flutter: ^1.0.7
  cupertino_icons: ^1.0.0

dev_dependencies:
  flutter_test:
    sdk: flutter
    
flutter:
  uses-material-design: true
  
  assets:
    - assets/index.html
```

### Configurer la WebView

Puisque nous avons déjà importé le package dans notre fichier `main.dart`, nous devons remplacer le widget Text par un widget WebView :

```dart
class _MyHomePageState extends State<MyHomePage> {

  WebViewController _controller;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Webview')),
      body: WebView(
        initialUrl: 'about:blank',
        onWebViewCreated: (WebViewController webviewController) {
          _controller = webviewController;
          _loadHtmlFromAssets();
        },
      ),
    );
  }

  _loadHtmlFromAssets() async {
    String file = await rootBundle.loadString('assets/index.html');
    _controller.loadUrl(Uri.dataFromString(
        file,
        mimeType: 'text/html',
        encoding: Encoding.getByName('utf-8')).toString());
  }

}
```

Nous avons enveloppé notre WebView avec un widget Scaffold (nous en parlerons plus tard dans l'article), mais concentrons-nous sur les différents champs du widget WebView vu ci-dessus :

* `initialUrl` est l'endroit où nous pouvons définir l'URL vers laquelle la WebView pointe. Ici, nous avons décidé de ne pointer vers rien puisque nous allons charger notre fichier HTML local.
* `onWebViewCreated` est un callback que nous recevons du package une fois que la WebView est créée. Puisque nous voulons sauvegarder l'instance du contrôleur que nous recevons de ce callback, nous avons créé un membre privé pour le stocker, `_controller`.

Vous remarquerez également que nous avons créé une méthode appelée `_loadHtmlFromAssets`, qui, comme son nom l'indique, chargera notre fichier HTML local dans la WebView.

Dans cette méthode, nous utilisons notre instance privée de WebViewController, `_controller`, et sa méthode exposée `loadUrl` pour charger notre fichier HTML local. En raison de la logique de cette méthode, son exécution est asynchrone.

Si nous exécutons notre application, nous obtiendrons le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_hE6jeEprGAW3YkVt0AiYrA.png)

## Comment communiquer de Flutter vers WebView

Maintenant, ajoutons une fonctionnalité pour appeler la méthode `fromFlutter` que nous avons définie dans notre fichier HTML local.

Pour cela, nous allons ajouter un bouton d'action flottant (ou FAB) à notre mise en page et connecter sa méthode `onPressed` pour appeler la méthode `fromFlutter`.

C'est aussi la raison de l'utilisation du widget Scaffold : pour pouvoir ajouter facilement un FAB :

```dart
@override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Webview')),
      body: WebView(
        initialUrl: 'about:blank',
        javascriptMode: JavascriptMode.unrestricted,
        onWebViewCreated: (WebViewController webviewController) {
          _controller = webviewController;
          _loadHtmlFromAssets();
        },
      ),
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.arrow_upward),
        onPressed: () {
          _controller.evaluateJavascript('fromFlutter("From Flutter")');
        },
      ),
    );
  }
```

Pour effectuer des appels de Flutter vers notre HTML chargé, nous utilisons la méthode `evaluateJavascript`. Pour pouvoir l'utiliser, nous devons ajouter une autre propriété à notre WebView appelée `javascriptMode`.

Dans le code ci-dessus, nous le définissons comme unrestricted. Si nous ne le définissons pas, nous ne pourrons pas communiquer entre Flutter et la WebView :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_odgcLrPQUlhGHdbaF4rO4A.gif)

## Comment communiquer de WebView vers Flutter

Vous vous souvenez que j'ai dit que nous parlerions du contenu de notre méthode `sendBack` ? Faisons-le maintenant :

```javascript
function sendBack() {
  messageHandler.postMessage("Hello from JS");
}
```

Dans la méthode `sendBack`, nous utilisons un objet appelé `messageHandler`, et sa méthode attachée appelée `postMessage`.

Tout comme la création d'un pont de communication dans une application native, une fois que vous en avez configuré un, vous ajoutez un objet à l'objet global `Window` dans la couche JavaScript pour être utilisé pour la communication.

Vous pouvez nommer cet objet comme vous le souhaitez, tant que vous y faites référence lorsque vous effectuez des appels de JavaScript vers votre application native.

Comment cet objet est-il ajouté à la couche JavaScript dans notre application, pourriez-vous demander ? En ajoutant l'attribut `JavascriptChannels` à notre widget WebView :

```dart
class _MyHomePageState extends State<MyHomePage> {

  WebViewController _controller;
  final GlobalKey<ScaffoldState> _scaffoldKey = new GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      appBar: AppBar(title: Text('Webview')),
      body: WebView(
        initialUrl: 'about:blank',
        javascriptMode: JavascriptMode.unrestricted,
        javascriptChannels: Set.from([
          JavascriptChannel(
              name: 'messageHandler',
              onMessageReceived: (JavascriptMessage message) {
               _scaffoldKey.currentState.showSnackBar(
                  SnackBar(
                      content: Text(message)
                  )
                 );
              })
        ]),
        onWebViewCreated: (WebViewController webviewController) {
          _controller = webviewController;
          _loadHtmlFromAssets();
        },
      ),
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.arrow_upward),
        onPressed: () {
          _controller.evaluateJavascript('fromFlutter("From Flutter")');
        },
      ),
    );

  }
```

Nous avons défini un `JavascriptChannel` avec un nom et un gestionnaire `onMessageReceived`. Le nom que nous avons donné à ce canal, `messageHandler`, est le nom que nous utilisons pour communiquer depuis le fichier HTML local que nous avons chargé vers notre couche native.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_AGpwDR2o8Fh7Re_Cwtg7fA.gif)
_Grand succès_

Pour les plus observateurs, vous avez probablement remarqué qu'une nouvelle variable privée a été ajoutée, `_scaffoldKey`. Cela est dû au fait que nous devions ajouter une clé à notre widget Scaffold pour pouvoir afficher la snackbar.

Vous pouvez obtenir le code source de l'application décrite dans cet article ci-dessous :

%[https://github.com/TomerPacific/MediumArticles/tree/master/flutter_communication_bridge]

Deux points finaux à prendre en compte :

1. [La méthode alert est cassée dans le package webview_flutter](https://github.com/flutter/flutter/issues/30358)
2. Pour utiliser le package dans iOS, vous devez ajouter la clé suivante à votre fichier `info.plist` : `<key>io.flutter.embedded_views_preview</key><string>yes</string>`

Voici quelques autres sources que vous pourriez trouver utiles si vous souhaitez en savoir plus sur Flutter et les WebViews :

* [The Power of WebViews In Flutter](https://medium.com/flutter/the-power-of-webviews-in-flutter-a56234b57df2)
* [WebView_Flutter Package](https://pub.dev/packages/webview_flutter)