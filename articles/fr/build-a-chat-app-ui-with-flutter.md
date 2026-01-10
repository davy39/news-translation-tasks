---
title: Comment créer une interface d'application de chat avec Flutter et Dart
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-20T22:14:57.000Z'
originalURL: https://freecodecamp.org/news/build-a-chat-app-ui-with-flutter
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6006d9e30a2838549dcb4bb3.jpg
tags:
- name: application
  slug: application
- name: Chat
  slug: chat
- name: Flutter
  slug: flutter
seo_title: Comment créer une interface d'application de chat avec Flutter et Dart
seo_desc: "By Krissanawat\nThese days, many people use chat applications to communicate\
  \ with team members, friends, and family via their smart phones. This makes these\
  \ messaging applications an essential medium of communication. \nThere is also high\
  \ demand for in..."
---

Par Krissanawat

De nos jours, de nombreuses personnes utilisent des applications de chat pour communiquer avec les membres de leur équipe, leurs amis et leur famille via leurs smartphones. Cela fait de ces applications de messagerie un moyen de communication essentiel.

Il existe également une forte demande pour des interfaces utilisateur intuitives et puissantes avec des fonctionnalités à la pointe de la technologie. L'interface utilisateur (ou UI) est l'aspect le plus impactant de l'expérience utilisateur globale, il est donc important de bien la concevoir.

Le développement d'applications Flutter a pris le monde d'assaut en termes de développement d'applications mobiles multiplateformes. Vous pouvez l'utiliser pour créer des interfaces utilisateur pixel-perfect, et de nombreuses entreprises de développement utilisent Flutter aujourd'hui.

Dans ce tutoriel, je vais vous présenter un mélange des deux : nous allons construire une interface d'application de chat entièrement dans l'environnement de codage Flutter/Dart. En plus d'apprendre l'implémentation de l'interface de chat dans Flutter, nous apprendrons également comment fonctionnent ses flux de travail et ses structures de codage.

Alors, commençons !

## Comment créer un nouveau projet Flutter

Tout d'abord, nous devons créer un nouveau projet Flutter. Pour cela, assurez-vous d'avoir installé le SDK Flutter et les autres exigences liées au développement d'applications Flutter.

Si tout est correctement configuré, alors pour créer un projet, nous pouvons simplement exécuter la commande suivante dans notre répertoire local souhaité :

```bash
flutter create ChatApp

```

Après avoir configuré le projet, nous pouvons naviguer à l'intérieur du répertoire du projet et exécuter la commande suivante dans le terminal pour exécuter le projet dans un émulateur disponible ou un appareil réel :

```bash
flutter run

```

Après sa construction réussie, nous obtiendrons le résultat suivant dans l'écran de l'émulateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-105.png)

## **Comment créer l'interface de l'écran d'accueil principal**

Maintenant, nous allons commencer à construire l'interface utilisateur de notre application de chat. L'écran d'accueil principal contiendra 2 sections :

* l'écran de conversation, que nous allons implémenter comme une page séparée, et
* une barre de navigation inférieure.

Tout d'abord, nous devons faire quelques configurations simples au code boilerplate par défaut dans le fichier **main.dart**. Nous allons supprimer certains codes par défaut et ajouter le simple `MaterialApp` pointant vers le `Container` vide comme page d'accueil pour l'instant :

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      debugShowCheckedModeBanner: false,
      home: Container(),
    );
  }
}

```

Maintenant, à la place du widget Container vide, nous allons appeler le widget `HomePage`. Mais d'abord, nous devons implémenter l'écran.

### Comment construire l'écran d'accueil principal

À l'intérieur du répertoire **./lib** de notre dossier de projet racine, nous devons créer un dossier appelé **./screens**. Ce dossier contiendra tous les fichiers dart pour les différents écrans.

À l'intérieur du répertoire **./lib/screens/**, nous devons créer un fichier appelé **homePage.dart**. À l'intérieur du fichier **homePage.dart**, nous devons ajouter le code de base du widget Stateless comme montré dans l'extrait de code ci-dessous :

```dart
import 'package:flutter/material.dart';

class HomePage extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: Center(child: Text("Chat")),
      ),

    );
  }
}

```

Maintenant, nous devons appeler le widget de classe `HomePage` dans le fichier **main.dart** comme montré dans l'extrait de code ci-dessous :

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      debugShowCheckedModeBanner: false,
      home: HomePage(),
    );
  }
}

```

Nous obtiendrons maintenant le résultat comme montré dans la capture d'écran de l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-106.png)

### Comment construire la barre de navigation inférieure

Maintenant, nous allons placer un menu de navigation inférieur sur l'écran `HomePage`. Pour cela, nous allons utiliser le widget `BottomNavigationBar` dans le paramètre `bottomNavigationBar` fourni par le widget `Scaffold`.

Voici le code d'implémentation global :

```dart
return Scaffold(
      body: Container(
        child: Center(child: Text("Chat")),
      ),
      bottomNavigationBar: BottomNavigationBar(
        selectedItemColor: Colors.red,
        unselectedItemColor: Colors.grey.shade600,
        selectedLabelStyle: TextStyle(fontWeight: FontWeight.w600),
        unselectedLabelStyle: TextStyle(fontWeight: FontWeight.w600),
        type: BottomNavigationBarType.fixed,
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.message),
            title: Text("Chats"),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.group_work),
            title: Text("Canaux"),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.account_box),
            title: Text("Profil"),
          ),
        ],
      ),
    );

```

Ici, nous avons configuré `BottomNavigationBar` avec divers paramètres de style et gardé notre élément de menu de navigation dans le paramètre `items`. Pour le paramètre `body`, nous avons simplement utilisé un `Container` simple avec un widget `Text`.

Nous obtiendrons maintenant la barre de navigation inférieure comme montré dans la capture d'écran de l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-107.png)

Maintenant que la navigation inférieure est terminée, nous pouvons continuer et implémenter la section de liste de conversations juste au-dessus de la barre de navigation inférieure.

## **Comment construire l'écran de liste de conversations**

Ici, nous allons créer la section de liste de conversations qui contiendra une section d'en-tête, une barre de recherche et la vue de liste de conversations.

Tout d'abord, à l'intérieur du dossier **./lib/screens**, nous devons créer un nouveau fichier dart appelé **chatPage.dart**. Ensuite, ajoutez un modèle de classe de widget stateful simple à l'intérieur comme montré dans l'extrait de code ci-dessous :

```dart
import 'package:flutter/material.dart';

class ChatPage extends StatefulWidget {
  @override
  _ChatPageState createState() => _ChatPageState();
}

class _ChatPageState extends State<ChatPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Center(child: Text("Chat")),
      ),
    );
  }
}

```

Maintenant, nous devons appeler le widget de classe `chatPage` à la place du widget `Container` dans **homePage.dart** comme montré dans l'extrait de code ci-dessous :

```dart
return Scaffold(
      body: ChatPage(),
      bottomNavigationBar: BottomNavigationBar(

```

Cela nous donnera le résultat suivant comme montré dans l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-108.png)

### Comment construire un en-tête de page de liste de conversations

Maintenant, nous allons ajouter l'en-tête à la section de liste de conversations qui aura un en-tête de texte et un bouton. Le code d'implémentation complet de l'interface utilisateur est fourni dans l'extrait de code ci-dessous :

```dart
return Scaffold(
      body: SingleChildScrollView(
        physics: BouncingScrollPhysics(),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            SafeArea(
              child: Padding(
                padding: EdgeInsets.only(left: 16,right: 16,top: 10),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: <Widget>[
                    Text("Conversations",style: TextStyle(fontSize: 32,fontWeight: FontWeight.bold),),
                    Container(
                      padding: EdgeInsets.only(left: 8,right: 8,top: 2,bottom: 2),
                      height: 30,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(30),
                        color: Colors.pink[50],
                      ),
                      child: Row(
                        children: <Widget>[
                          Icon(Icons.add,color: Colors.pink,size: 20,),
                          SizedBox(width: 2,),
                          Text("Ajouter",style: TextStyle(fontSize: 14,fontWeight: FontWeight.bold),),
                        ],
                      ),
                    )
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );

```

Ici, nous avons utilisé le `SingleChildScrollView` pour que la section du corps du **chatPage.dart** soit entièrement défilable.

Ensuite, nous avons utilisé l'instance `BouncingScrollPhysics` pour donner l'effet de rebond lorsque le défilement de l'utilisateur atteint la fin ou le début.

Ensuite, nous avons ajouté un widget Text et un Container pour afficher le bouton du côté droit.

Enfin, nous avons un widget `Column` comme enfant du widget `SingleChildScrollView` pour que tout apparaisse verticalement sur l'écran.

Cela nous donnera le résultat suivant comme montré dans l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-109.png)

Maintenant, nous allons ajouter une barre de recherche juste en dessous de la section d'en-tête.

### **Comment ajouter la barre de recherche**

Dans le widget `Column` précédent, nous allons ajouter un widget de barre de recherche juste en dessous de la section d'interface utilisateur de l'en-tête. Donc, comme deuxième enfant du widget `Column`, nous devons insérer le code suivant fourni dans l'extrait de code ci-dessous :

```dart
Padding(
  padding: EdgeInsets.only(top: 16,left: 16,right: 16),
  child: TextField(
    decoration: InputDecoration(
      hintText: "Rechercher...",
      hintStyle: TextStyle(color: Colors.grey.shade600),
      prefixIcon: Icon(Icons.search,color: Colors.grey.shade600, size: 20,),
      filled: true,
      fillColor: Colors.grey.shade100,
      contentPadding: EdgeInsets.all(8),
      enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(20),
          borderSide: BorderSide(
              color: Colors.grey.shade100
          )
      ),
    ),
  ),
),

```

Cela nous donnera le résultat suivant comme montré dans l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-110.png)

### **Comment construire la liste de conversations**

Maintenant que nous avons la section d'en-tête et une barre de recherche, nous allons implémenter la section de liste de conversations.

Pour cela, nous devons implémenter un modèle de classe d'objet pour stocker les instances de listes de conversations.

Donc, à l'intérieur du dossier **./lib**, nous devons créer un nouveau dossier appelé **./models**. À l'intérieur de **./models**, nous devons créer un fichier appelé **chatUsersModel.dart**.

Dans le fichier modèle, nous devons créer une classe d'objet modèle comme montré dans l'extrait de code ci-dessous :

```dart
import 'package:flutter/cupertino.dart';

class ChatUsers{
  String name;
  String messageText;
  String imageURL;
  String time;
  ChatUsers({@required this.name,@required this.messageText,@required this.imageURL,@required this.time});
}

```

L'objet contiendra le nom de l'utilisateur, le texte du message, l'URL de l'image et l'heure.

Ensuite, nous devons créer une liste d'utilisateurs à l'intérieur de **chatPage.dart** comme montré dans l'extrait de code ci-dessous :

```dart
class _ChatPageState extends State<ChatPage> {
  List<ChatUsers> chatUsers = [
    ChatUsers(text: "Jane Russel", secondaryText: "Awesome Setup", image: "images/userImage1.jpeg", time: "Now"),
    ChatUsers(text: "Glady's Murphy", secondaryText: "That's Great", image: "images/userImage2.jpeg", time: "Yesterday"),
    ChatUsers(text: "Jorge Henry", secondaryText: "Hey where are you?", image: "images/userImage3.jpeg", time: "31 Mar"),
    ChatUsers(text: "Philip Fox", secondaryText: "Busy! Call me in 20 mins", image: "images/userImage4.jpeg", time: "28 Mar"),
    ChatUsers(text: "Debra Hawkins", secondaryText: "Thankyou, It's awesome", image: "images/userImage5.jpeg", time: "23 Mar"),
    ChatUsers(text: "Jacob Pena", secondaryText: "will update you in evening", image: "images/userImage6.jpeg", time: "17 Mar"),
    ChatUsers(text: "Andrey Jones", secondaryText: "Can you please share the file?", image: "images/userImage7.jpeg", time: "24 Feb"),
    ChatUsers(text: "John Wick", secondaryText: "How are you?", image: "images/userImage8.jpeg", time: "18 Feb"),
  ];

```

Maintenant que nous avons les données de liste de conversations des utilisateurs fictifs, nous pouvons les appliquer à la liste de conversations pour créer une vue de liste.

### **Comment créer une classe de widget séparée pour une conversation individuelle**

Ici, nous allons créer un widget de composant séparé pour les éléments individuels dans la vue de liste de conversations.

Pour cela, à l'intérieur de **./lib**, créez un dossier appelé **./widgets**. Et à l'intérieur de **./widgets**, nous devons créer un fichier appelé **conversationList.dart**. À l'intérieur du nouveau fichier de widget, nous pouvons utiliser le code de l'extrait de code suivant :

```dart
import 'package:flutter/material.dart';

class ConversationList extends StatefulWidget{
  String name;
  String messageText;
  String imageUrl;
  String time;
  bool isMessageRead;
  ConversationList({@required this.name,@required this.messageText,@required this.imageUrl,@required this.time,@required this.isMessageRead});
  @override
  _ConversationListState createState() => _ConversationListState();
}

class _ConversationListState extends State<ConversationList> {
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: (){
      },
      child: Container(
        padding: EdgeInsets.only(left: 16,right: 16,top: 10,bottom: 10),
        child: Row(
          children: <Widget>[
            Expanded(
              child: Row(
                children: <Widget>[
                  CircleAvatar(
                    backgroundImage: NetworkImage(widget.imageUrl),
                    maxRadius: 30,
                  ),
                  SizedBox(width: 16,),
                  Expanded(
                    child: Container(
                      color: Colors.transparent,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          Text(widget.name, style: TextStyle(fontSize: 16),),
                          SizedBox(height: 6,),
                          Text(widget.messageText,style: TextStyle(fontSize: 13,color: Colors.grey.shade600, fontWeight: widget.isMessageRead?FontWeight.bold:FontWeight.normal),),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Text(widget.time,style: TextStyle(fontSize: 12,fontWeight: widget.isMessageRead?FontWeight.bold:FontWeight.normal),),
          ],
        ),
      ),
    );
  }
}

```

Ce fichier de widget prend le nom de l'utilisateur, le texte du message, l'URL de l'image, l'heure et une valeur booléenne de type de message comme paramètres. Et il retourne le modèle contenant les valeurs.

Dans le **chatPage.dart**, à l'intérieur du widget `ListView`, nous devons appeler le widget `ConversationList` en passant les paramètres requis comme montré dans l'extrait de code ci-dessous :

```dart
ListView.builder(
  itemCount: chatUsers.length,
  shrinkWrap: true,
  padding: EdgeInsets.only(top: 16),
  physics: NeverScrollableScrollPhysics(),
  itemBuilder: (context, index){
    return ConversationList(
      name: chatUsers[index].name,
      messageText: chatUsers[index].messageText,
      imageUrl: chatUsers[index].imageURL,
      time: chatUsers[index].time,
      isMessageRead: (index == 0 || index == 3)?true:false,
    );
  },
),

```

Notez que ce widget `ListView` doit être conservé comme premier enfant du widget `Column` dans l'écran `chatPage`.

Cela nous donnera le résultat suivant comme montré dans l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-111.png)

Cela complète l'implémentation de l'interface utilisateur de notre écran de liste de conversations et de l'écran d'accueil principal dans son ensemble. Maintenant, nous passerons à l'implémentation de l'écran de détails de chat.

## **Comment construire un écran de détails de chat**

Maintenant, nous allons créer un écran de détails de chat. Pour cela, nous devons créer un nouveau fichier appelé **chatDetailPage.dart** à l'intérieur du dossier **./lib/screens/**. Pour l'instant, nous allons simplement ajouter le code de base comme montré dans l'extrait de code ci-dessous :

```dart
import 'package:flutter/material.dart';

class ChatDetailPage extends StatefulWidget{
  @override
  _ChatDetailPageState createState() => _ChatDetailPageState();
}

class _ChatDetailPageState extends State<ChatDetailPage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Détails du chat"),
      ),
      body: Container()
    );
  }
}

```

Ici, nous avons retourné une `AppBar` de base avec du texte et un `Container` vide comme `body` du widget `Scaffold`.

Maintenant, nous allons ajouter la navigation vers `ChatDetailPage` dans la méthode `onTap` du widget `GestureHandler` dans le fichier de widget **conversationList.dart** comme montré dans l'extrait de code ci-dessous :

```dart
GestureDetector(
      onTap: (){
        Navigator.push(context, MaterialPageRoute(builder: (context){
          return ChatDetailPage();
        }));
      },

```

Nous pouvons maintenant naviguer vers l'écran de détails du chat comme montré dans la démonstration de l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/2021-01-20-13.40.11.gif)

### Comment construire une barre d'application personnalisée pour l'écran de détails du chat

Ici, nous allons ajouter une barre d'application personnalisée en haut de l'écran de détails du chat. Pour cela, nous allons utiliser le widget `AppBar` avec diverses configurations de paramètres comme montré dans l'extrait de code ci-dessous :

```dart
return Scaffold(
      appBar: AppBar(
        elevation: 0,
        automaticallyImplyLeading: false,
        backgroundColor: Colors.white,
        flexibleSpace: SafeArea(
          child: Container(
            padding: EdgeInsets.only(right: 16),
            child: Row(
              children: <Widget>[
                IconButton(
                  onPressed: (){
                    Navigator.pop(context);
                  },
                  icon: Icon(Icons.arrow_back,color: Colors.black,),
                ),
                SizedBox(width: 2,),
                CircleAvatar(
                  backgroundImage: NetworkImage("<https://randomuser.me/api/portraits/men/5.jpg>"),
                  maxRadius: 20,
                ),
                SizedBox(width: 12,),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      Text("Kriss Benwat",style: TextStyle( fontSize: 16 ,fontWeight: FontWeight.w600),),
                      SizedBox(height: 6,),
                      Text("En ligne",style: TextStyle(color: Colors.grey.shade600, fontSize: 13),),
                    ],
                  ),
                ),
                Icon(Icons.settings,color: Colors.black54,),
              ],
            ),
          ),
        ),
      ),
      body: Container()
    );

```

Cela nous donnera le résultat suivant comme montré dans l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-112.png)

### **Comment implémenter la boîte de texte inférieure**

En bas de l'écran de détails du chat, nous devons ajouter une section de messagerie qui contiendra un éditeur de texte et un bouton pour envoyer le message.

Pour cela, nous allons utiliser le widget `Align` et aligner l'enfant à l'intérieur du widget avec le bas de l'écran. Le code global est fourni dans l'extrait de code ci-dessous :

```dart
body: Stack(
        children: <Widget>[
          Align(
            alignment: Alignment.bottomLeft,
            child: Container(
              padding: EdgeInsets.only(left: 10,bottom: 10,top: 10),
              height: 60,
              width: double.infinity,
              color: Colors.white,
              child: Row(
                children: <Widget>[
                  GestureDetector(
                    onTap: (){
                    },
                    child: Container(
                      height: 30,
                      width: 30,
                      decoration: BoxDecoration(
                        color: Colors.lightBlue,
                        borderRadius: BorderRadius.circular(30),
                      ),
                      child: Icon(Icons.add, color: Colors.white, size: 20, ),
                    ),
                  ),
                  SizedBox(width: 15,),
                  Expanded(
                    child: TextField(
                      decoration: InputDecoration(
                        hintText: "Écrire un message...",
                        hintStyle: TextStyle(color: Colors.black54),
                        border: InputBorder.none
                      ),
                    ),
                  ),
                  SizedBox(width: 15,),
                  FloatingActionButton(
                    onPressed: (){},
                    child: Icon(Icons.send,color: Colors.white,size: 18,),
                    backgroundColor: Colors.blue,
                    elevation: 0,
                  ),
                ],
                
              ),
            ),
          ),
        ],
      ),

```

Cela nous donnera une section de messagerie avec un champ de texte pour taper les messages et un bouton pour envoyer les messages :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-113.png)

Nous avons également un bouton à gauche que nous pouvons utiliser pour ajouter d'autres options de menu pour la messagerie.

### **Comment configurer la section de liste de messages dans l'écran de chat**

Maintenant, nous allons créer l'interface utilisateur pour les messages apparaissant dans l'écran de détails du chat.

Tout d'abord, nous devons créer un modèle qui reflète l'objet d'instance de message.

Pour cela, nous devons créer un fichier appelé **chatMessageModel.dart** à l'intérieur du dossier **./models** et définir l'objet de classe comme suit :

```dart
import 'package:flutter/cupertino.dart';

class ChatMessage{
  String messageContent;
  String messageType;
  ChatMessage({@required this.messageContent, @required this.messageType});
}

```

L'objet de classe accepte le contenu du message et le type de message (expéditeur ou destinataire comme valeurs d'instance.

Maintenant dans le **chatDetailPage.dart**, nous devons créer une liste de messages à afficher comme montré dans l'extrait de code ci-dessous :

```dart
List<ChatMessage> messages = [
    ChatMessage(messageContent: "Bonjour, Will", messageType: "receiver"),
    ChatMessage(messageContent: "Comment vas-tu ?", messageType: "receiver"),
    ChatMessage(messageContent: "Hey Kriss, je vais bien mec. Et toi ?", messageType: "sender"),
    ChatMessage(messageContent: "ehhhh, ça va.", messageType: "receiver"),
    ChatMessage(messageContent: "Y a-t-il quelque chose qui ne va pas ?", messageType: "sender"),
  ];

```

Ensuite, nous allons créer une vue de liste pour les messages au-dessus des enfants du widget `Stack`, au-dessus du widget `Align`, comme montré dans l'extrait de code ci-dessous :

```dart
body: Stack(
        children: <Widget>[
          ListView.builder(
            itemCount: messages.length,
            shrinkWrap: true,
            padding: EdgeInsets.only(top: 10,bottom: 10),
            physics: NeverScrollableScrollPhysics(),
            itemBuilder: (context, index){
              return Container(
                padding: EdgeInsets.only(left: 16,right: 16,top: 10,bottom: 10),
                child: Text(messages[index].messageContent),
              );
            },
          ),
          Align(

```

Maintenant, les messages apparaîtront sous forme de liste comme montré dans la capture d'écran de l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-114.png)

Maintenant, nous avons les messages qui apparaissent à l'écran, mais ils ne sont pas stylisés comme nous le voulons dans l'écran de chat.

### Comment styliser et positionner les messages en fonction de l'expéditeur et du destinataire

Maintenant, nous allons styliser la liste des messages pour qu'elle apparaisse comme une bulle de message de chat. Nous allons également les positionner en fonction du type de message en utilisant le widget `Align` comme montré dans l'extrait de code ci-dessous :

```dart
ListView.builder(
  itemCount: messages.length,
  shrinkWrap: true,
  padding: EdgeInsets.only(top: 10,bottom: 10),
  physics: NeverScrollableScrollPhysics(),
  itemBuilder: (context, index){
    return Container(
      padding: EdgeInsets.only(left: 14,right: 14,top: 10,bottom: 10),
      child: Align(
        alignment: (messages[index].messageType == "receiver"?Alignment.topLeft:Alignment.topRight),
        child: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(20),
            color: (messages[index].messageType  == "receiver"?Colors.grey.shade200:Colors.blue[200]),
          ),
          padding: EdgeInsets.all(16),
          child: Text(messages[index].messageContent, style: TextStyle(fontSize: 15),),
        ),
      ),
    );
  },
),

```

Cela nous donnera le résultat suivant comme montré dans l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-115.png)

Vous pouvez voir une démonstration globale de l'interface utilisateur de l'application dans son ensemble ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/2021-01-20-13.52.45.gif)

Félicitations ! Nous avons construit une interface d'application de chat intuitive et moderne entièrement dans l'écosystème Flutter et Dart.

## Récapitulatif

Les applications de messagerie sociale sont un moyen de communication essentiel de nos jours. Équipées de fonctionnalités de chat à la pointe de la technologie avec des appels audio et vidéo, des pièces jointes d'images et de fichiers, et bien plus encore, ces applications de chat ont rendu la communication beaucoup plus efficace. Ces applications ont rendu le monde plus petit pour nous.

L'objectif principal de cet article était de vous montrer comment développer une interface utilisateur intuitive et simple pour les applications de chat avec un design moderne dans l'écosystème Flutter. L'implémentation étape par étape a fourni une présentation détaillée de l'interface utilisateur de l'application et a également donné un aperçu de l'environnement de codage Flutter.

J'espère que ce tutoriel vous aidera à créer votre prochaine application de chat en utilisant Flutter.

Vous pouvez également trouver de l'inspiration pour une interface utilisateur d'application de chat et le développement de fonctionnalités à partir des meilleurs modèles d'applications de chat [Flutter](https://www.instaflutter.com/app-templates/flutter-chat-app/) disponibles sur le marché. Assurez-vous de les consulter également.