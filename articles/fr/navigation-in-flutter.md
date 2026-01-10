---
title: Navigation dans Flutter – Comment ajouter des navigateurs Stack, Tab et Drawer
  à vos applications
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-04-21T18:10:23.000Z'
originalURL: https://freecodecamp.org/news/navigation-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Types-of-Navigations-in-Flutter
seo_title: Navigation dans Flutter – Comment ajouter des navigateurs Stack, Tab et
  Drawer à vos applications
---

Banner.png
tags:
- name: Flutter
  slug: flutter
- name: développement d'applications mobiles
  slug: developpement-applications-mobiles
seo_title: null
seo_desc: "Presque toutes les applications que vous concevez ou développez utiliseront un type de navigation.\
  \ \nIl existe trois types de navigation courants à toutes les applications – stack, tab,\
  \ et drawer navigation.\nFlutter prend en charge les trois types, et leur implémentation\
  \ est similaire à la manière dont vous le faites dans d'autres applications. Mais j'ai trouvé cela super fluide pour construire la navigation dans mon application Flutter.\n\nDans cet article, nous allons construire une application Flutter qui utilise les trois types de navigation dans une seule application afin que vous puissiez apprendre comment ils fonctionnent.\n\n## Types de Navigation\n\nComme je l'ai mentionné ci-dessus, il existe trois principaux types de navigation que vous pourriez utiliser dans vos applications. Encore une fois, ils sont :\n\n1. Navigation par Stack\n2. Navigation par Tab\n3. Navigation par Drawer\n\nComprenons comment chacun fonctionne.\n\n### Navigation par Stack\n\nImaginez un jeu de cartes, où vous pouvez ajouter ou retirer des cartes du haut de la pile. La navigation par Stack dans Flutter fonctionne de manière similaire. Elle vous aide à naviguer entre les pages ou les écrans en empilant de nouvelles pages par-dessus les existantes.\n\nLorsque vous passez à un nouvel écran, l'écran actuel est poussé sur la pile de navigation, et lorsque vous revenez, l'écran du haut est retiré de la pile.\n\nCe type de navigation est couramment utilisé pour les flux hiérarchiques et linéaires au sein d'une application.\n\n### Navigation par Tab\n\nLes onglets sont un élément essentiel de la navigation des applications mobiles, permettant aux utilisateurs de basculer rapidement entre différentes sections ou vues sans perdre leur contexte actuel.\n\nFlutter facilite la mise en œuvre de la navigation par onglets avec ses widgets intégrés, tels que TabBar et TabBarView. En utilisant ces widgets, vous pouvez créer une expérience de navigation par onglets belle et fonctionnelle, parfaite pour organiser le contenu en sections logiques.\n\nVous avez également la liberté de personnaliser l'apparence de vos onglets, ce qui rend simple la création d'un look et d'une sensation uniques pour votre application.\n\n### Navigation par Drawer\n\nLe modèle de navigation par Drawer, également connu sous le nom de "menu hamburger" ou "menu latéral", est un style de navigation populaire dans les applications mobiles. Il consiste en un panneau caché qui glisse depuis le côté de l'écran, révélant un menu avec diverses options de navigation.\n\nCette technique d'économie d'espace garde le contenu principal de votre application visible tout en fournissant un accès facile à des fonctionnalités ou sections supplémentaires.\n\nCommençons à construire l'application et voyons comment implémenter chacune de ces fonctionnalités de navigation.\n\n## Comment créer le projet\n\nAu lieu de créer un nouveau projet à chaque fois à partir de zéro, j'ai créé une application boilerplate et l'ai téléchargée sur [GitHub](https://github.com/5minslearn/Flutter-Boilerplate). Vous pouvez récupérer le code et l'exécuter. J'espère que cela rend la création de ce projet un peu plus simple.\n\nNaviguez vers le dossier où vous souhaitez créer votre projet dans le terminal et exécutez la commande suivante.\n\n```bash\ngit clone https://github.com/5minslearn/Flutter-Boilerplate.git\n```\n\nNaviguez vers le dossier `Flutter-Boilerplate` et exécutez la commande `flutter pub get` pour installer les dépendances.\n\n```bash\ncd Flutter-Boilerplate/\nflutter pub get\n```\n\nC'est tout. Nous avons nos dépendances installées.\n\nOuvrez le projet dans Visual Studio Code en exécutant la commande `code ./` dans le terminal.\n\n![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-147.png)\n_Cloner le dépôt et installer les dépendances_\n\nDémarrez votre émulateur/connectez votre appareil et appuyez sur `F5` dans VS Code pour exécuter votre application.\n\nPour le moment, l'application contiendra simplement un écran vide comme montré dans la capture d'écran ci-dessous.\n\n![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-148.png)\n_Application Flutter avec écran vide_\n\nConstruisons les trois types de navigation dans notre application.\n\nMais avant cela, voyons à quoi ressemblera notre application finale :\n\n![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-155.png)\n_Apparence de notre application finale_\n\nNous aurons à la fois des navigateurs drawer et tab en haut. Appuyer sur le bouton dans le premier onglet nous emmènera à la page suivante via le navigateur stack.\n\n## Comment construire la navigation par Tab\n\nCommençons par construire le navigateur tab. Supposons que l'onglet sera sur la page d'accueil (idéalement, c'est là qu'il devrait être).\n\nCréez un nouveau fichier nommé `tab.dart` dans le répertoire `lib/`. Ajoutez le code suivant :\n\n```dart\nimport 'package:flutter/material.dart';
import './tabs/tab1.dart';
import './tabs/tab2.dart';
import './tabs/tab3.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Scaffold(
          appBar: AppBar(
            title: const Text("Accueil"),
            bottom: const TabBar(
              tabs: [
                Tab(icon: Icon(Icons.phone_android)),
                Tab(icon: Icon(Icons.tablet_android)),
                Tab(icon: Icon(Icons.laptop_windows)),
              ],
            ),
          ),
          body: const TabBarView(
            children: <Widget>[
              Tab1(),
              Tab2(),
              Tab3(),
            ],
          )),
    );
  }
}
```\n\nDans le code ci-dessus, nous créons une classe nommée `HomePage`. Dans la méthode build, nous retournons le widget `DefaultTabController`, qui est essentiellement une vue à onglets. Nous définissons que nous avons besoin de 3 onglets dans la propriété `length`.\n\nEn bas de la propriété `appBar`, nous avons défini des icônes pour chaque onglet (icônes Téléphone, Tablette et Ordinateur). En dessous, nous définissons la propriété `body` avec un `TabBarView` rendant tous les onglets à l'intérieur.\n\nDès que vous collez le code ci-dessus, vous remarquerez de nombreuses erreurs mises en évidence dans votre éditeur VS Code.\n\nCela est dû au fait que, si vous regardez les quatre premières lignes, la première ligne est l'import du package Material UI de Flutter et les trois autres sont des imports de fichiers définis par l'utilisateur. Mais nous ne les avons pas encore créés. Donc, votre éditeur de code lancera une erreur dans ces lignes et dans les trois dernières lignes où nous appelons `Tab1()`, `Tab2()`, et `Tab3()` (car ces classes sont importées de ces fichiers). Résolvons ce problème maintenant.\n\nCréez un nouveau dossier nommé `tabs` à l'intérieur du répertoire `lib/` et créez trois fichiers nommés `tab1.dart`, `tab2.dart`, et `tab3.dart`.\n\nCopiez le contenu ci-dessous dans le fichier `tab1.dart` :\n\n```dart\nimport 'package:flutter/material.dart';

class Tab1 extends StatelessWidget {
  const Tab1({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          const Text("Téléphones"),
          Padding(
            padding: const EdgeInsets.only(top: 16.0),
            child: ElevatedButton(
              onPressed: () {
                Navigator.of(context).pushNamed("/secret");
              },
              child: const Text('Révéler le Secret'),
            ),
          ),
        ],
      ),
    );
  }
}
```\n\nCopiez le contenu ci-dessous dans le fichier `tab2.dart` :\n\n```dart\nimport 'package:flutter/material.dart';

class Tab2 extends StatelessWidget {
  const Tab2({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: const <Widget>[
          Text("Tablettes"),
        ],
      ),
    );
  }
}
```\n\nCopiez le code ci-dessous dans le fichier `tab3.dart` :\n\n```\nimport 'package:flutter/material.dart';

class Tab3 extends StatelessWidget {
  const Tab3({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: const <Widget>[
          Text("Ordinateurs portables"),
        ],
      ),
    );
  }
}\n```\n\nSi vous regardez le code des trois fichiers, vous remarquerez que tout est identique sauf que le premier fichier d'onglet (`tab1.dart`) a un bouton supplémentaire appelé "Révéler le Secret". Appuyer dessus naviguera l'utilisateur vers la route `/secret`. Cela ne lancera pas d'erreur car cette route n'a pas encore été définie. Les deux autres fichiers (`tab2.dart` et `tab3.dart`) afficheront uniquement le texte.\n\nToutes les erreurs que vous avez vues dans le fichier `tab.dart` seront résolues maintenant. Mais si vous exécutez votre application, vous ne remarquerez aucun changement dans la sortie. Cela est dû au fait que nous avons simplement créé la disposition des onglets et que nous ne l'avons pas mappée à notre fichier `main.dart`.\n\nAjoutez la ligne suivante en haut du fichier `main.dart` :\n\n```dart\nimport './tab.dart';
```\n\nRemplacez `home: const MyHomePage(title: 'Home')` par `home: const HomePage()`, dans la méthode `build` de la classe `MyApp`.\n\nEnregistrez le fichier et exécutez votre application. Vous devriez pouvoir voir la disposition des onglets sur votre écran maintenant.\n\n![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-157.png)\n_Disposition des onglets dans l'application Flutter_\n\nNe pressez pas le bouton "Révéler le Secret". Si vous le pressez, cela lancera une erreur. Parce que, comme je l'ai mentionné précédemment, nous avons configuré une navigation de route dans la propriété `onPress` de ce bouton, mais la route n'est pas encore définie.\n\n"Appuyons dessus et voyons ce qui se passe"...\n\nEspérons que cette pensée vous aura traversé l'esprit maintenant. Ce n'est pas une erreur, c'est la nature humaine. Nous sommes curieux d'explorer les choses même si elles ne sont pas recommandées.\n\nAu fait, si vous faites cela, vous verrez l'erreur suivante (Exception en terminologie de programmation) :\n\n![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-156.png)\n_Exception du routeur Flutter_\n\nEn résumé, cette capture d'écran d'erreur décrit que la route fournie n'existe pas.\n\n## Comment construire la navigation par Drawer\n\nNotre prochain objectif est d'ajouter la navigation par drawer. Mais avant cela, nous devons créer deux fichiers :\n\n1. `drawer.dart` : pour afficher le Navigation Drawer\n2. `about.dart` : une option sera fournie sur le Drawer Navigator pour naviguer ici\n\nCréez le fichier `drawer.dart` à l'intérieur du répertoire `lib/` et non à l'intérieur du répertoire `tab/`. Le répertoire `tab/` est uniquement pour les onglets et nous n'avons pas besoin de le toucher davantage car nous avons terminé avec les onglets. Copiez le code ci-dessous dans le fichier `drawer.dart` :\n\n```dart\nimport 'package:flutter/material.dart';

class MyDrawer extends StatelessWidget {
  const MyDrawer({super.key});

  navigateTo(String route, BuildContext context) {
    Navigator.of(context).pushReplacementNamed(route);
  }

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: const EdgeInsets.all(16.0),
        children: <Widget>[
          ListTile(
            leading: const Icon(Icons.home),
            title: const Text('Accueil'),
            onTap: () {
              navigateTo("/home", context);
            },
          ),
          ListTile(
            leading: const Icon(Icons.info),
            title: const Text('À propos'),
            onTap: () {
              navigateTo("/about", context);
            },
          ),
        ],
      ),
    );
  }
}
```\n\nDans ce fichier, nous définissons la classe nommée `MyDrawer`. Dans la méthode `build`, nous rendons le widget `Drawer` avec les options `Accueil` et `À propos` dans la liste. Cliquer sur ces options nous naviguera vers les routes appropriées.\n\nCréez un fichier `about.dart` dans le même répertoire et copiez le code ci-dessous :\n\n```dart\nimport './drawer.dart';
import 'package:flutter/material.dart';

class About extends StatelessWidget {
  const About({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: const MyDrawer(),
      appBar: AppBar(title: const Text("À propos")),
      body: const Center(child: Text("À propos")),
    );
  }
}
```\n\nDans ce fichier, nous créons une classe nommée `About` qui retourne un widget `Scaffold` contenant le drawer que nous avons défini juste avant ce fichier. L'`appBar` et le `body` afficheront le texte "À propos".\n\nEncore une fois, vous ne pourrez pas voir ces changements immédiatement dans l'application. Cela est dû au fait que nous ne les avons pas liés au fichier `main.dart`.\n\nAvant de les lier, nous avons un élément dans notre backlog. Terminez-le et revenez pour les lier tous ensemble.\n\nCréez un fichier nommé `secret.dart` dans le répertoire `lib/` et copiez le code ci-dessous :\n\n```dart\nimport 'package:flutter/material.dart';

class SecretPage extends StatelessWidget {
  const SecretPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          // backgroundColor: Colors.red,
          title: const Text("Secret"),
        ),
        body: SizedBox(
          width: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: const <Widget>[
              Text("Rien à montrer"),
            ],
          ),
        ));
  }
}
```\n\nDans ce fichier, nous avons créé une classe nommée `SecretPage` et retourné simplement un `Text` dans le `body`. Rien de fantaisiste ici. C'est un widget Flutter super simple.\n\nNotre élément de backlog est également terminé. Voici ce que vous attendiez : nous allons définir nos routes maintenant.\n\nOuvrez le fichier `main.dart` et ajoutez les imports suivants en haut du fichier :\n\n```dart\nimport './about.dart';
import './secret.dart';
```\n\nRemplacez la méthode `build` de la classe `MyApp` par le code ci-dessous :\n\n```dart\n  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      routes: <String, WidgetBuilder>{
        "/about": (BuildContext context) => const About(),
        "/home": (BuildContext context) => const HomePage(),
        "/secret": (BuildContext context) => const SecretPage(),
      },
      initialRoute: "/home",
      title: 'Navigation Flutter',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
    );
  }
```\n\nDans le code ci-dessus, vous pouvez voir que nous définissons le MaterialApp pour contenir des routes. Elles sont définies comme des paires clé-valeur, mappant une route avec un Widget. Nous avons défini trois routes :\n\n* `/about` – la route pour le navigateur drawer\n* `/home` – la route pour le navigateur tab\n* `/secret` – la route pour le navigateur stack\n\nNous avons défini la route initiale comme étant `/home`, qui contient le navigateur tab.\n\nExécutez l'application et vous devriez pouvoir voir la sortie suivante sur votre appareil :\n\n![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-158.png)\n_Vue fusionnée des onglets et du drawer_\n\nEn appuyant sur le bouton "Révéler le Secret", vous serez dirigé vers la page Secret que nous avons créée (idéalement, elle ne contient pas de secret). Vous devriez également pouvoir faire défiler les onglets en douceur.\n\nD'ici, j'espère que vous aurez remarqué une erreur ici. Si ce n'est pas le cas, voici ce que c'est : le bouton de retour est affiché sur le premier écran de notre application.\n\n"Pourquoi aurions-nous besoin d'afficher le bouton de retour sur le premier écran ?"\n\nC'est une erreur et nous devons la résoudre. Appuyez sur le bouton de retour et voyons ce qui se passe. Espérons que vous voyez ce que j'ai vu. Le bouton de retour était masqué et nous voyons simplement le titre "Accueil" dans l'`appBar` (similaire à la capture d'écran ci-dessous) :\n\n![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-160.png)\n_Problème du bouton de retour_\n\nMais il y a un autre problème sur le même écran. Espérons que vous l'avez vu aussi. Si ce n'est pas le cas, ne vous inquiétez pas, je vais le révéler ici.\n\n"Pouvez-vous accéder au navigateur drawer par quelque moyen que ce soit ?"\n\nNon. N'est-ce pas ?\n\nMais heureusement, la solution pour les deux problèmes ci-dessus est la même. Si nous résolvons le deuxième problème, le premier problème sera automatiquement résolu.\n\nC'est super. Mais comment résoudre le deuxième problème ?\n\nVous devez afficher le bouton du navigateur drawer (icône Hamburger) en haut à gauche. Cela masquera éventuellement le bouton de retour.\n\nOuvrez le fichier `tab.dart` et importez le fichier drawer en haut de ce fichier.\n\n```dart\nimport './drawer.dart';
```\n\nAjoutez la ligne suivante à l'intérieur du widget `Scaffold` de la méthode `build` :\n\n```dart\ndrawer: const MyDrawer(),
```\n\nEt c'est tout !\n\nVoici la sortie que vous pouvez voir lorsque vous exécutez votre application :\n\n![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-163.png)\n_Apparence de l'application après la résolution des problèmes_\n\n## Conclusion\n\nDans cet article, vous avez appris comment implémenter la navigation dans une application Flutter. Nous avons inclus les trois types de navigation dans une seule application dans ce tutoriel à des fins éducatives. Idéalement, vous ne feriez pas cela avec une véritable application que vous construisez. La plupart des applications seront construites sur un ou deux types de navigation.\n\nCe [dépôt](https://github.com/5minslearn/Flutter-Navigation-Types) contient mon code. Vous pouvez l'utiliser pour référence.\n\nPour en savoir plus sur Flutter, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_flutter_navigation) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_flutter_navigation)) et suivez-moi sur les réseaux sociaux.