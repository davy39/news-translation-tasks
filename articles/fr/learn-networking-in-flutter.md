---
title: Apprendre le Réseautage dans Flutter en Construisant une Application Simple
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-05-15T18:42:25.000Z'
originalURL: https://freecodecamp.org/news/learn-networking-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Networking-in-Flutter
seo_title: Apprendre le Réseautage dans Flutter en Construisant une Application Simple
---

Banner.png
tags:
- name: réseaux informatiques
  slug: reseaux-informatiques
- name: Flutter
  slug: flutter
- name: développement d'applications mobiles
  slug: developpement-applications-mobiles
seo_title: null
seo_desc: "Presque toutes les applications que vous utilisez aujourd'hui fonctionnent en accédant à Internet. Vous pouvez difficilement trouver une application qui fonctionne sans se connecter à Internet. Internet est devenu une partie intégrante de nos vies, car il résout l'un des problèmes les plus critiques que nous devons gérer : le transfert de données. Nous recevons ou envoyons constamment des données à quelqu'un, qu'il s'agisse d'une application de médias sociaux, d'une application d'actualités ou de tout autre type, il y a une forme de transfert de données. En raison de cela, il est super important d'apprendre le réseautage si vous apprenez le développement d'applications mobiles. Dans cet article, je vais expliquer comment construire une application mobile super simple qui récupère des données depuis Internet et les affiche sur l'application.

## Comment Créer le Projet

Accédez au dossier où vous souhaitez créer votre projet dans le terminal et exécutez la commande suivante :

```bash
git clone https://github.com/5minslearn/Flutter-Boilerplate.git
```

Accédez au dossier Flutter-Boilerplate et exécutez la commande `flutter pub get` pour installer les dépendances.

```bash
cd Flutter-Boilerplate/
flutter pub get
```

C'est tout. Nous avons nos dépendances installées.

Ouvrez le projet dans Visual Studio Code en exécutant la commande `code ./` dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-40.png)
_Créer une application Flutter à partir d'un modèle de base_

Démarrez votre émulateur/connectez votre appareil et appuyez sur `F5` dans VS Code pour exécuter votre application.

Pour le moment, l'application contiendra simplement un écran vide comme montré dans la capture d'écran ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-41.png)
_Application Flutter avec un écran vide_

Construisons notre application de réseautage.

## Où Obtenir les Données

C'est la question la plus évidente. Si nous devons récupérer quelque chose depuis Internet et l'afficher, nous avons besoin d'un serveur API exposant les données dont nous avons besoin. Mais, la plupart des gens ne peuvent pas se permettre de le faire à des fins d'apprentissage. Pour surmonter cela, de nombreuses personnes offrent des services API gratuits.

Vous pouvez consommer les données de leurs services API à des fins d'apprentissage. Cependant, nous ne pouvons pas valider l'originalité des données, car la plupart d'entre elles seront aléatoires.

Dans ce tutoriel, nous utiliserons l'API exposée par [https://sampleapis.com/](https://sampleapis.com/). Ils exposent un point de terminaison API qui liste les Ressources de Codage. L'URL du point de terminaison est [https://api.sampleapis.com/codingresources/codingResources](https://api.sampleapis.com/codingresources/codingResources).

Dans notre application, nous récupérerons les données depuis ce point de terminaison et les listerons dans notre application.

## Installer les Dépendances

Installons les dépendances dont nous avons besoin pour construire cette application. Elles sont :

1. Le package `http`
2. Le package `url_launcher`

Nous utiliserons le package `http` pour faire un appel au point de terminaison de l'API. Et nous utiliserons le package `url_launcher` pour ouvrir une URL dans un navigateur externe.

Ouvrez le fichier `pubspec.yml` et ajoutez les deux packages suivants dans la section des dépendances :

```bash
  http: ^0.13.6
  url_launcher: ^6.1.11
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-42.png)
_Ajouter des dépendances_

Si vous utilisez VS Code comme IDE, les dépendances seront installées automatiquement en enregistrant ce fichier. Pour les autres IDE, exécutez `flutter pub get` dans le dossier racine de votre projet pour installer les dépendances.

## Comment Récupérer les Données de l'API

Nous avons nos dépendances prêtes. Faisons une requête à notre API et obtenons les données.

Importez le package `http` dans le fichier `lib/main.dart`.

```bash
import 'package:http/http.dart' as http;
```

Initialisez un objet de liste dans la classe `_MyHomePageState` en ajoutant le code suivant :

```dart
List _resources = [];
```

Écrivons une méthode qui fait un appel à notre point de terminaison API et les décode en un objet JSON.

```dart
  void _fetchResources() async {
    final response = await http.get(Uri.parse(
        'https://api.sampleapis.com/codingresources/codingResources'));
    if (response.statusCode == 200) {
      final data = json.decode(response.body) as List;
      setState(() {
        _resources = data;
      });
    } else {
      throw Exception('Échec du chargement des ressources');
    }
  }
```

Collez le code ci-dessus dans la classe `MyHomePageState`. Dans la méthode ci-dessus, nous faisons un appel au point de terminaison de l'API ([https://api.sampleapis.com/codingresources/codingResources](https://api.sampleapis.com/codingresources/codingResources)). À partir de la réponse, nous validons si elle a réussi à recevoir les données en vérifiant si son code de statut est `200` (et en lançant une erreur si ce n'est pas le cas). Nous décodons ensuite les données reçues et les enregistrons dans l'état de notre application.

Vous avez peut-être remarqué une erreur après avoir collé le code ci-dessus à la partie `json.decode`. Pour décoder JSON, nous devons importer un package `convert` dans notre fichier. Ajoutez le code suivant en haut du fichier :

```dart
import 'dart:convert';
```

L'erreur devrait avoir disparu maintenant.

Nous avons une méthode qui fait un appel au point de terminaison de l'API et enregistre les données dans l'état. Notre prochaine étape est de déclencher cette méthode lorsque nous ouvrons l'application.

Nous pouvons le faire en remplaçant la méthode `initState`.

```dart
  @override
  void initState() {
    super.initState();
    _fetchResources();
  }
```

En citant la [documentation](https://api.flutter.dev/flutter/widgets/State/initState.html) de Flutter,

> "`initState` est appelé lorsque cet objet est inséré dans l'arbre. Le framework appellera cette méthode exactement une fois pour chaque objet [State](https://api.flutter.dev/flutter/widgets/State-class.html) qu'il crée."

Dans le code ci-dessus, nous avons appelé notre méthode `_fetchResources()` dans la méthode `initState()`.

## Comment Construire l'Interface Utilisateur

Nous avons obtenu la liste des éléments chaque fois que nous ouvrons l'application. Notre prochaine étape est de les afficher sur l'interface utilisateur.

Copiez le code ci-dessous et remplacez-le par la méthode `build` de la classe `_MyHomePageState`.

```dart
@override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.title),
        ),
        body: _resources.isEmpty
            ? const Center(
                child: CircularProgressIndicator(),
              )
            : ListView.builder(
                itemCount: _resources.length,
                itemBuilder: (context, index) {
                  final resource = _resources[index];
                  return InkWell(
                      onTap: () => {},
                      child: Card(
                          child: ListTile(
                        title: Text(resource['description']),
                        subtitle: Text(resource['url']),
                        leading: const CircleAvatar(
                            backgroundImage: NetworkImage(
                                "https://images.unsplash.com/photo-1547721064-da6cfb341d50")),
                        trailing: Text(resource['types'].join(', ')),
                      )));
                }));
  }
```

Comprenons le code ci-dessus.

Nous affichons un chargeur si notre état a des valeurs vides. S'il contient des valeurs, nous les parcourons avec un ListView builder et nous affichons un widget de carte pour chaque élément, affichant la `description`, l'`url` et les `types` de la ressource.

C'est tout.

Exécutez l'application en appuyant sur `F5` et vous devriez pouvoir voir ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-43.png)
_Chargement des ressources_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-44.png)
_Affichage des ressources_

C'est génial, n'est-ce pas ?

## Corrigons la Partie Manquante

Mais je pense qu'il manque une petite chose à ce stade.

Nous pouvons voir la liste des ressources. Mais nous ne pouvons pas les consulter. Certaines ressources ont un lien court que nous pouvons facilement retenir et taper. Mais certaines d'entre elles ont une URL longue qui serait difficile à retenir pour un être humain typique. Ajoutons une petite amélioration : lorsque nous cliquons sur une ressource, son lien doit s'ouvrir dans notre navigateur par défaut.

C'est très simple à implémenter dans Flutter. C'est la raison pour laquelle nous avons ajouté le package `url_launcher` au début de ce tutoriel.

Importez le package `url_launcher` dans votre application comme ceci :

```dart
import 'package:url_launcher/url_launcher.dart';
```

Ajoutez la méthode suivante dans la classe `_MyHomePageState` :

```dart
_launchURL(String url) async {
    if (await canLaunch(url)) {
      await launch(url);
    } else {
      throw 'Impossible d'ouvrir $url';
    }
  }
```

La méthode ci-dessus accepte une URL, valide le lien et l'ouvre dans le navigateur.

Nous devons appeler cette méthode en appuyant sur la carte. Nous pouvons y parvenir en appelant cette méthode dans la propriété `onTap` du widget `InkWell`.

Voici le code pour cela :

```dart
onTap: () => {_launchURL(resource['url'])},
```

Exécutons notre application et testons cela.

Vous avez probablement été déçu en appuyant sur une carte, je l'ai certainement été en travaillant dessus.

Vous auriez dû voir cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-45.png)
_Erreur lors de l'ouverture d'une URL : Exception s'est produite. "Impossible d'ouvrir https://www.youtube.com/bocajs"_

Bien que l'URL soit correcte, pourquoi notre système ne l'ouvre-t-il pas dans un navigateur ?

## Qu'est-ce que les Intent Actions ?

Eh bien, maintenant nous devons apprendre les intent actions.

En citant la [documentation](https://developer.android.com/reference/android/content/Intent) des développeurs Android,

> "Un Intent fournit un moyen de réaliser une liaison d'exécution tardive entre le code dans différentes applications. Son utilisation la plus significative est dans le lancement d'activités, où il peut être considéré comme le lien entre les activités. Il s'agit essentiellement d'une structure de données passive contenant une description abstraite d'une action à effectuer."

Cela signifie essentiellement que lorsque nous transmettons quelque chose à l'application externe, nous devons le déclarer dans notre application. Pour Android, nous devons le définir dans `AndroidManifest.xml` et pour iOS, la plupart de ces configurations vont dans le fichier `Info.plist`.

Ajoutez le bloc `queries` dans le code suivant à votre fichier `AndroidManifest.xml`.

```xml
<manifest>
    <application>
        ...
    </application>
    <queries>
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.BROWSABLE" />
            <data android:scheme="https" />
        </intent>
    </queries>
</manifest>
```

Désinstallez l'application de votre mobile et exécutez à nouveau l'application.

Espérons que vous devriez pouvoir voir le lien ouvert dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-46.png)
_Lien ouvert dans un navigateur_

## Conclusion

Dans cet article, vous avez appris le réseautage dans Flutter. Nous avons fait une requête à une API, affiché la liste et ouvert l'URL dans le navigateur.

Ce [dépôt](https://github.com/5minslearn/Flutter-Networking) contient mon code. Vous pouvez l'utiliser pour référence.

Pour en savoir plus sur Flutter, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_flutter_networking) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_flutter_networking)) et suivez-moi sur les réseaux sociaux.