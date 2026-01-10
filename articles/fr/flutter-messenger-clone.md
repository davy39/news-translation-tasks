---
title: Tutoriel Flutter UI – Comment créer une application de chat avec des stories
  en utilisant le SDK Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-11T00:42:18.000Z'
originalURL: https://freecodecamp.org/news/flutter-messenger-clone
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60228d650a2838549dcc1f0b.jpg
tags:
- name: Chat
  slug: chat
- name: Facebook Messenger
  slug: facebook-messenger
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: Tutoriel Flutter UI – Comment créer une application de chat avec des stories
  en utilisant le SDK Flutter
seo_desc: "By Krissanawat\nChat applications have become one of the easiest ways to\
  \ communicate over the internet. As such, many applications incorporate chat features\
  \ in them so that users can interact and engage in social communications. \nThese\
  \ applications ha..."
---

Par Krissanawat

Les applications de chat sont devenues l'un des moyens les plus faciles de communiquer sur Internet. Ainsi, de nombreuses applications intègrent des fonctionnalités de chat afin que les utilisateurs puissent interagir et s'engager dans des communications sociales. 

Ces applications ont rendu le monde plus petit grâce à leur puissante communication audio/vidéo et textuelle de bout en bout. En plus de cela, d'autres fonctionnalités telles que le partage de stories, l'envoi de pièces jointes, et plus encore, ont rendu ces applications encore plus engageantes et utiles. 

La plupart des applications ont également une fonctionnalité de stories. Elle permet aux utilisateurs de partager leurs expériences brièvement et la story disparaît après un certain temps. Ces fonctionnalités accrochent les utilisateurs à cette application et les incitent à partager leurs pensées, idées, souvenirs et expériences.

Facebook Messenger est l'une des applications de chat les plus utilisées. Elle se classe juste derrière WhatsApp en termes d'utilisation globale dans le monde. 

Dans ce tutoriel, nous allons reproduire l'interface utilisateur de Messenger en utilisant le framework de développement d'applications mobiles Flutter. Nous explorerons également le développement d'interface utilisateur basé sur des widgets en utilisant le codage Flutter. Cela nous familiarisera avec l'écosystème Flutter ainsi qu'avec les meilleures pratiques pour écrire du code Flutter. 

Ici, nous allons implémenter l'écran d'accueil principal de l'application de messagerie qui contiendra une barre d'application supérieure, une barre de recherche, une section de stories et une section de liste de conversations. 

À travers ce processus, nous verrons comment Flutter facilite le développement de l'interface utilisateur et nous obtiendrons une application de chat clone de messenger. 

Alors, commençons !

## Créer un nouveau projet Flutter

Tout d'abord, nous devons créer un nouveau projet Flutter. Pour cela, assurez-vous que le SDK Flutter et les autres exigences liées au développement d'applications Flutter sont correctement installés. 

Si tout est correctement configuré, alors pour créer un projet, nous pouvons simplement exécuter la commande suivante dans le répertoire local souhaité :

```bash
flutter create messengerUI

```

Après la configuration du projet, nous pouvons naviguer à l'intérieur du répertoire du projet et exécuter la commande suivante dans le terminal pour exécuter le projet dans un émulateur disponible ou un appareil réel :

```bash
flutter run

```

Après une construction réussie, nous obtiendrons le résultat suivant dans l'écran de l'émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/tip1.jpg)

Maintenant, nous devons remplacer le modèle par défaut par notre propre modèle de structure de projet. 

Tout d'abord, nous devons créer un dossier appelé **./screens** à l'intérieur du dossier **./lib**. Ensuite, à l'intérieur du dossier ./lib/screens, nous devons créer un nouveau fichier appelé **conversations.dart**. 

À l'intérieur de **conversation.dart**, nous allons implémenter une simple classe de widget Stateful retournant un widget `Scaffold` avec une barre d'application basique et un corps `Container` vide. Le code pour **conversations.dart** est montré dans l'extrait de code ci-dessous :

```dart
import 'package:flutter/material.dart';

class Conversations extends StatefulWidget {
  @override
  _ConversationsState createState() => _ConversationsState();
}

class _ConversationsState extends State<Conversations> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Chat"),
      ),
      body: Container(),
    );
  }
}

```

Maintenant, nous devons remplacer le modèle par défaut dans le fichier **main.dart** et appeler l'écran `Conversations` dans l'option `home` du widget `MaterialApp` comme montré dans l'extrait de code ci-dessous :

```dart
import 'package:flutter/material.dart';
import 'package:messangerUI/screens/conversations.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Messenger Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: Conversations(),
    );
  }
}

```

Nous obtenons le résultat comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/mess1.png)

## Comment ajouter l'AppBar

Maintenant, nous allons personnaliser la barre d'application en haut. Comme la barre d'application doit être défilable, nous n'allons **pas** utiliser l'option `appBar` fournie par le widget `Scaffold`. Nous allons simplement utiliser le widget `ListView` dans l'option body de `Scaffold` et garder tous les autres widgets comme enfants du widget `ListView`. 

L'implémentation globale de la barre d'application personnalisée est fournie dans l'extrait de code ci-dessous :

```dart
Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
          child: Container(
        padding: EdgeInsets.only(left: 20, right: 20, top: 15),
        child: ListView(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: <Widget>[
                Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      image: DecorationImage(
                          image: NetworkImage(
                              "<https://randomuser.me/api/portraits/men/11.jpg>"),
                          fit: BoxFit.cover)),
                ),
                Text(
                  "Chats",
                  style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                ),
                Icon(Icons.edit)
              ],
            ),
          ],
        ),
      )),
    );
  }

```

Pour l'interface utilisateur de la barre d'application, nous avons utilisé un widget `Row` à l'intérieur du widget `ListView`. À l'intérieur du widget Row, nous avons placé un widget `Container` avec `NetworkImage` comme enfant, un widget `Text`, et un widget `Icon`.

Ainsi, nous obtiendrons le résultat comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/mess2.png)

## Comment ajouter la barre de recherche

Maintenant, nous allons ajouter un champ de saisie de recherche juste en dessous de la barre d'application. Il contiendra un widget `InputField` décoré avec des styles et une icône de recherche. 

Puisque nous avons besoin d'un contrôleur de texte pour le widget `InputField`, nous devons l'initialiser d'abord comme montré dans l'extrait de code ci-dessous :

```dart
TextEditingController _searchController = new TextEditingController();

```

Maintenant, nous allons implémenter l'interface utilisateur pour la barre de recherche juste en dessous du widget `Row` qui se trouve à l'intérieur du widget parent `ListView`. Nous utiliserons le widget `SizedBox` pour donner une petite séparation entre les deux sections. 

L'implémentation globale de la barre de recherche en utilisant un widget `TextField` à l'intérieur d'un widget `Container` avec décoration est montrée dans l'extrait de code ci-dessous :

```dart
body: SafeArea(
          child: Container(
        padding: EdgeInsets.only(left: 20, right: 20, top: 15),
        child: ListView(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: <Widget>[
                Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      image: DecorationImage(
                          image: NetworkImage(
                              "<https://randomuser.me/api/portraits/men/11.jpg>"),
                          fit: BoxFit.cover)),
                ),
                Text(
                  "Chats",
                  style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                ),
                Icon(Icons.edit)
              ],
            ),
            SizedBox(
              height: 15,
            ),
            Container(
              width: double.infinity,
              height: 40,
              decoration: BoxDecoration(
                  color: Color(0xFFe9eaec),
                  borderRadius: BorderRadius.circular(15)),
              child: TextField(
                cursorColor: Color(0xFF000000),
                controller: _searchController,
                decoration: InputDecoration(
                    prefixIcon: Icon(
                      Icons.search,
                      color: Color(0xFF000000).withOpacity(0.5),
                    ),
                    hintText: "Rechercher",
                    border: InputBorder.none),
              ),
            ),
          ],
        ),
      )),
    );

```

Ainsi, nous obtiendrons la barre de recherche comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/mess3.png)

## Comment implémenter la section des Stories

Maintenant, il est temps d'implémenter la section des stories. Les stories sont une fonctionnalité populaire dans chaque application sociale de nos jours. Nous allons l'implémenter juste en dessous de la barre de recherche. 

Cette section contiendra une image de l'utilisateur avec son nom en bas. Les utilisateurs qui ont des stories auront un anneau circulaire bleu autour de leur image, contrairement aux autres.

Mais d'abord, nous devons préparer une liste d'utilisateurs fictifs pour les afficher dans la section des stories. 

Pour cela, nous allons initialiser une liste appelée `storyList`. Nous garderons quelques objets contenant les informations de l'utilisateur telles que `name`, `imageUrl`, `isOnline` (pour vérifier si l'utilisateur est en ligne), et `hasStory` (pour vérifier si l'utilisateur a une story). 

Les données de la liste fictive sont fournies dans l'extrait de code ci-dessous :

```dart
List storyList = [
    {
      "name": "Novac",
      "imageUrl": "<https://randomuser.me/api/portraits/men/31.jpg>",
      "isOnline": true,
      "hasStory": true,
    },
    {
      "name": "Derick",
      "imageUrl": "<https://randomuser.me/api/portraits/men/81.jpg>",
      "isOnline": false,
      "hasStory": false,
    },
    {
      "name": "Mevis",
      "imageUrl": "<https://randomuser.me/api/portraits/women/49.jpg>",
      "isOnline": true,
      "hasStory": false,
    },
    {
      "name": "Emannual",
      "imageUrl": "<https://randomuser.me/api/portraits/men/35.jpg>",
      "isOnline": true,
      "hasStory": true,
    },
    {
      "name": "Gracy",
      "imageUrl": "<https://randomuser.me/api/portraits/women/56.jpg>",
      "isOnline": false,
      "hasStory": false,
    },
    {
      "name": "Robert",
      "imageUrl": "<https://randomuser.me/api/portraits/men/36.jpg>",
      "isOnline": false,
      "hasStory": true,
    }
  ];

```

Maintenant, nous allons implémenter une fonction séparée qui retourne l'interface utilisateur globale pour la section des Stories. L'implémentation est fournie dans l'extrait de code ci-dessous :

```dart
_stories() {
    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      child: Row(
        children: <Widget>[
          Padding(
            padding: EdgeInsets.only(right: 20),
            child: Column(
              children: <Widget>[
                Container(
                  width: 60,
                  height: 60,
                  decoration: BoxDecoration(
                      shape: BoxShape.circle, color: Color(0xFFe9eaec)),
                  child: Center(
                    child: Icon(
                      Icons.add,
                      size: 33,
                    ),
                  ),
                ),
                SizedBox(
                  height: 10,
                ),
                SizedBox(
                  width: 75,
                  child: Align(
                      child: Text(
                    'Votre Story',
                    overflow: TextOverflow.ellipsis,
                  )),
                )
              ],
            ),
          ),
          Row(
              children: List.generate(storyList.length, (index) {
            return Padding(
              padding: const EdgeInsets.only(right: 20),
              child: Column(
                children: <Widget>[
                  Container(
                    width: 60,
                    height: 60,
                    child: Stack(
                      children: <Widget>[
                        storyList[index]['hasStory']
                            ? Container(
                                decoration: BoxDecoration(
                                    shape: BoxShape.circle,
                                    border: Border.all(
                                        color: Colors.blueAccent, width: 3)),
                                child: Padding(
                                  padding: const EdgeInsets.all(3.0),
                                  child: Container(
                                    width: 75,
                                    height: 75,
                                    decoration: BoxDecoration(
                                        shape: BoxShape.circle,
                                        image: DecorationImage(
                                            image: NetworkImage(
                                                storyList[index]['imageUrl']),
                                            fit: BoxFit.cover)),
                                  ),
                                ),
                              )
                            : Container(
                                width: 70,
                                height: 70,
                                decoration: BoxDecoration(
                                    shape: BoxShape.circle,
                                    image: DecorationImage(
                                        image: NetworkImage(
                                            storyList[index]['imageUrl']),
                                        fit: BoxFit.cover)),
                              ),
                        storyList[index]['isOnline']
                            ? Positioned(
                                top: 38,
                                left: 42,
                                child: Container(
                                  width: 20,
                                  height: 20,
                                  decoration: BoxDecoration(
                                      color: Color(0xFF66BB6A),
                                      shape: BoxShape.circle,
                                      border: Border.all(
                                          color: Color(0xFFFFFFFF), width: 3)),
                                ),
                              )
                            : Container()
                      ],
                    ),
                  ),
                  SizedBox(
                    height: 10,
                  ),
                  SizedBox(
                    width: 75,
                    child: Align(
                        child: Text(
                      storyList[index]['name'],
                      overflow: TextOverflow.ellipsis,
                    )),
                  )
                ],
              ),
            );
          }))
        ],
      ),
    );
  }

```

Ici, nous avons retourné un `SingleChildScrollView` comme widget parent avec une option de défilement horizontal. 

Ensuite, nous avons utilisé le widget `List.generate` à l'intérieur du widget `Row` pour itérer à travers notre tableau `storyList`. Pour chaque élément de la liste, un modèle à l'intérieur du `List.generate` est retourné. Le rendu conditionnel est utilisé pour les utilisateurs en ligne et ceux qui ont des stories.

Maintenant, nous devons appeler la fonction à l'intérieur des enfants `ListView` juste en dessous du `InputField` en faisant une séparation en utilisant le widget `SizedBox` comme montré dans l'extrait de code ci-dessous :

```dart
body: SafeArea(
          child: Container(
        padding: EdgeInsets.only(left: 20, right: 20, top: 15),
        child: ListView(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: <Widget>[
                Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      image: DecorationImage(
                          image: NetworkImage(
                              "<https://randomuser.me/api/portraits/men/11.jpg>"),
                          fit: BoxFit.cover)),
                ),
                Text(
                  "Chats",
                  style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                ),
                Icon(Icons.edit)
              ],
            ),
            SizedBox(
              height: 15,
            ),
            Container(
              width: double.infinity,
              height: 40,
              decoration: BoxDecoration(
                  color: Color(0xFFe9eaec),
                  borderRadius: BorderRadius.circular(15)),
              child: TextField(
                cursorColor: Color(0xFF000000),
                controller: _searchController,
                decoration: InputDecoration(
                    prefixIcon: Icon(
                      Icons.search,
                      color: Color(0xFF000000).withOpacity(0.5),
                    ),
                    hintText: "Rechercher",
                    border: InputBorder.none),
              ),
            ),
            SizedBox(
              height: 20,
            ),
            _stories(),
          ],
        ),
      )),
    );

```

Nous obtiendrons le résultat comme montré dans la démonstration ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/messGIF1.gif)

Comme vous pouvez le voir, la section des stories est défilable horizontalement.

## Comment créer la section de la liste de conversations

Maintenant, nous allons créer une liste de conversations juste en dessous de la section des Stories. Elle contiendra une image de l'utilisateur, son nom, son message et l'heure. 

Pour la liste de conversations également, nous allons créer des données fictives. La liste est similaire à `storiesList` mais contient deux informations supplémentaires pour `message` et `time`. La liste de données fictives `conversationList` est montrée dans l'extrait de code ci-dessous :

```dart
List conversationList = [
    {
      "name": "Novac",
      "imageUrl": "<https://randomuser.me/api/portraits/men/31.jpg>",
      "isOnline": true,
      "hasStory": true,
      "message": "Où es-tu ?",
      "time": "17:00"
    },
    {
      "name": "Derick",
      "imageUrl": "<https://randomuser.me/api/portraits/men/81.jpg>",
      "isOnline": false,
      "hasStory": false,
      "message": "C'est bien !!",
      "time": "7:00"
    },
    {
      "name": "Mevis",
      "imageUrl": "<https://randomuser.me/api/portraits/women/49.jpg>",
      "isOnline": true,
      "hasStory": false,
      "message": "Je t'aime aussi !",
      "time": "6:50"
    },
    {
      "name": "Emannual",
      "imageUrl": "<https://randomuser.me/api/portraits/men/35.jpg>",
      "isOnline": true,
      "hasStory": true,
      "message": "Je dois y aller !! Au revoir !!",
      "time": "hier"
    },
    {
      "name": "Gracy",
      "imageUrl": "<https://randomuser.me/api/portraits/women/56.jpg>",
      "isOnline": false,
      "hasStory": false,
      "message": "Désolé, j'ai oublié !",
      "time": "2 févr."
    },
    {
      "name": "Robert",
      "imageUrl": "<https://randomuser.me/api/portraits/men/36.jpg>",
      "isOnline": false,
      "hasStory": true,
      "message": "Non, je n'irai pas !",
      "time": "28 janv."
    },
    {
      "name": "Lucy",
      "imageUrl": "<https://randomuser.me/api/portraits/women/56.jpg>",
      "isOnline": false,
      "hasStory": false,
      "message": "Hahahahahaha",
      "time": "25 janv."
    },
    {
      "name": "Emma",
      "imageUrl": "<https://randomuser.me/api/portraits/women/56.jpg>",
      "isOnline": false,
      "hasStory": false,
      "message": "Ça fait un bail !",
      "time": "15 janv."
    }
  ];

```

De manière similaire à la section des stories, nous allons construire la section de la liste de conversations comme une fonction séparée. 

En tant que widget parent, nous avons retourné le widget `Column`. L'enfant du widget `Column` contient le widget `List.generate` qui itère à travers le tableau `conversationList` et fournit l'interface utilisateur pour chaque élément de la liste de conversations. 

Nous utilisons le rendu conditionnel pour les utilisateurs en ligne et ceux qui ont des stories. L'implémentation globale de la fonction est fournie dans l'extrait de code ci-dessous :

```dart
_conversations(BuildContext context) {
    return Column(
      children: List.generate(conversationList.length, (index) {
        return InkWell(
          child: Padding(
            padding: const EdgeInsets.only(bottom: 20),
            child: Row(
              children: <Widget>[
                Container(
                  width: 60,
                  height: 60,
                  child: Stack(
                    children: <Widget>[
                      conversationList[index]['hasStory'] ? 
                      Container(
                        decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            border:
                                Border.all(color: Colors.blueAccent, width: 3)),
                        child: Padding(
                          padding: const EdgeInsets.all(3.0),
                          child: Container(
                            width: 75,
                            height: 75,
                            decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                image: DecorationImage(
                                    image: NetworkImage(
                                        conversationList[index]['imageUrl']),
                                    fit: BoxFit.cover)),
                          ),
                        ),
                      )
                      : Container(
                        width: 70,
                        height: 70,
                        decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            image: DecorationImage(
                                image: NetworkImage(
                                    conversationList[index]['imageUrl']),
                                fit: BoxFit.cover)),
                      ),
                      conversationList[index]['isOnline']
                          ? Positioned(
                              top: 38,
                              left: 42,
                              child: Container(
                                width: 20,
                                height: 20,
                                decoration: BoxDecoration(
                                    color: Color(0xFF66BB6A),
                                    shape: BoxShape.circle,
                                    border: Border.all(color: Color(0xFFFFFFFF), width: 3)),
                              ),
                            )
                          : Container()
                    ],
                  ),
                ),
                SizedBox(
                  width: 20,
                ),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Text(
                      conversationList[index]['name'],
                      style:
                          TextStyle(fontSize: 17, fontWeight: FontWeight.w500),
                    ),
                    SizedBox(
                      height: 5,
                    ),
                    SizedBox(
                      width: MediaQuery.of(context).size.width - 135,
                      child: Text(
                        conversationList[index]['message'] +
                            " - " +
                            conversationList[index]['time'],
                        style: TextStyle(
                            fontSize: 15, color: Color(0xFF000000).withOpacity(0.7)),
                        overflow: TextOverflow.ellipsis,
                      ),
                    )
                  ],
                )
              ],
            ),
          ),
        );
      }),
    );
  }

```

Maintenant, nous devons appeler la fonction `_conversations()` dans le `ListView` de `Scaffold` juste en dessous de la fonction Stories comme montré dans l'extrait de code ci-dessous :

```dart
body: SafeArea(
          child: Container(
        padding: EdgeInsets.only(left: 20, right: 20, top: 15),
        child: ListView(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: <Widget>[
                Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      image: DecorationImage(
                          image: NetworkImage(
                              "<https://randomuser.me/api/portraits/men/11.jpg>"),
                          fit: BoxFit.cover)),
                ),
                Text(
                  "Chats",
                  style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                ),
                Icon(Icons.edit)
              ],
            ),
            SizedBox(
              height: 15,
            ),
            Container(
              width: double.infinity,
              height: 40,
              decoration: BoxDecoration(
                  color: Color(0xFFe9eaec),
                  borderRadius: BorderRadius.circular(15)),
              child: TextField(
                cursorColor: Color(0xFF000000),
                controller: _searchController,
                decoration: InputDecoration(
                    prefixIcon: Icon(
                      Icons.search,
                      color: Color(0xFF000000).withOpacity(0.5),
                    ),
                    hintText: "Rechercher",
                    border: InputBorder.none),
              ),
            ),
            SizedBox(
              height: 20,
            ),
            _stories(),
            SizedBox(
              height: 20,
            ),
            **_conversations(context)**
          ],
        ),
      )),
    );
  }

```

Nous obtiendrons le résultat comme montré dans la démonstration ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/messGIF2.gif)

Comme vous pouvez le voir, l'écran global est défilable verticalement avec la vue de la liste de conversations et la section des Stories est défilable horizontalement.

Enfin, nous avons réussi à créer l'écran d'accueil d'une application de messagerie en utilisant Flutter.

## Conclusion

L'objectif principal de ce tutoriel était de vous montrer comment construire une interface utilisateur comme Facebook Messenger en utilisant l'écosystème Flutter. 

Si vous regardez de près le code, vous verrez que la plupart de l'implémentation était assez facile grâce à la flexibilité et à la structure de mise en page que Flutter fournit. 

Avec seulement quelques widgets, nous pouvons placer chaque composant dans l'interface utilisateur à la position correcte. En plus de cette création d'interface utilisateur, vous pouvez également apprendre les modèles de codage de base pour le développement Flutter. 

Séparer les grandes sections de code en fonctions séparées aide à simplifier et à nettoyer notre code. Cela a démontré une meilleure pratique de codage pour le développement d'interface utilisateur dans Flutter. 

Le tutoriel met également en évidence comment certains widgets dans Flutter facilitent les choses pour nous, tels que le défilement horizontal et le placement d'icônes et d'images avec des styles. Vous pouvez définitivement prendre ces informations et les utiliser pour construire votre propre application de chat à l'avenir.

De plus, vous pouvez également vous inspirer des modèles d'applications de chat [Flutter](https://www.instaflutter.com/app-templates/flutter-chat-app/) qui offrent des interfaces utilisateur magnifiques ainsi que des fonctionnalités puissantes. Et au cas où vous souhaiteriez consulter des modèles d'applications de chat construits en utilisant d'autres frameworks de développement d'applications mobiles, vous pouvez également parcourir ces modèles d'applications de chat [React Native](https://www.instamobile.io/app-templates/react-native-chat-app-template/).