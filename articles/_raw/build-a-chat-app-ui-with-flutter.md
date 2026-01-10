---
title: How to Build a Chat App UI With Flutter and Dart
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
seo_title: null
seo_desc: "By Krissanawat\nThese days, many people use chat applications to communicate\
  \ with team members, friends, and family via their smart phones. This makes these\
  \ messaging applications an essential medium of communication. \nThere is also high\
  \ demand for in..."
---

By Krissanawat

These days, many people use chat applications to communicate with team members, friends, and family via their smart phones. This makes these messaging applications an essential medium of communication. 

There is also high demand for intuitive and powerful user interfaces with state of the art features. The user interface (or UI) is the most impactful aspect of the overall user experience, so it's important to get right.

Flutter app development has taken the world by storm in terms of cross-platform mobile application development. You can use it to create pixel-perfect UIs, and many development companies use Flutter today. 

In this tutorial, I am going to introduce you to a mix of both: we're going to build a chat app UI entirely on the Flutter/Dart coding environment. Along with learning the awesome Chat UI implementation in Flutter, we will also learn how its coding workflows and structures work.

So, let's get started!

## How to Create a New Flutter Project

First, we need to create a new Flutter project. For that, make sure that you've installed the Flutter SDK and other Flutter app development-related requirements. 

If everything is properly set up, then in order to create a project we can simply run the following command in our desired local directory:

```bash
flutter create ChatApp

```

After we've set up the project, we can navigate inside the project directory and execute the following command in the terminal to run the project in either an available emulator or an actual device:

```bash
flutter run

```

After it's been successfully built, we will get the following result in the emulator screen:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-105.png)

## **How to Create the Main Home Screen UI**

Now, we are going to start building the UI for our chat application. The Main Home Screen will contain 2 sections: 

* the conversation screen, which we are going to implement as a separate page, and 
* a bottom navigation bar.

First, we need to make some simple configurations to the default boilerplate code in the **main.dart** file. We'll remove some default code and add the simple `MaterialApp` pointing to the empty `Container` as a home page for now:

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

Now in place of the empty Container widget, we are going to call the `HomePage` screen widget. But first, we need to implement the screen.

### How to Build the Main Home Screen

Inside the **./lib** directory of our root project folder, we need to create a folder called **./screens**. This folder will hold all the dart files for different screens.

Inside **./lib/screens/** directory, we need to create a file called **homePage.dart**. Inside the **homePage.dart** file, we need to add the basic Stateless widget code as shown in the code snippet below:

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

Now, we need to call the `HomePage` class widget in the **main.dart** file as shown in the code snippet below:

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

Now we will get the result as shown in the emulator screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-106.png)

### How to Build the Bottom Navigator Bar

Now, we are going to place a Bottom Navigation menu on the `HomePage` screen. For that, we are going to use the `BottomNavigationBar` widget in the `bottomNavigationBar` parameter provided by the `Scaffold` widget. 

Here's the overall code implementation:

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
            title: Text("Channels"),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.account_box),
            title: Text("Profile"),
          ),
        ],
      ),
    );

```

Here, we have configured `BottomNavigationBar` with various style parameters and kept our Navigation menu item in the `items` parameter. For the `body` parameter, we have just used a simple `Container` with a `Text` widget.

Now we will get the bottom navbar as shown in the emulator screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-107.png)

Now that the bottom navigation is done, we can go ahead and implement the conversation list section just above the bottom navbar.

## **How to Build the Conversation List Screen**

Here, we are going to create the conversation list section which will contain a header section, a search bar, and the conversation list view.

First, inside the **./lib/screens** folder, we need to create a new dart file called **chatPage.dart**. Then, add a simple stateful widget class template inside as shown in the code snippet below:

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

Now, we need to call the `chatPage` class widget in place of the `Container` widget in **homePage.dart** as shown in the code snippet below:

```dart
return Scaffold(
      body: ChatPage(),
      bottomNavigationBar: BottomNavigationBar(

```

This will give us the following result as shown in the emulator below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-108.png)

### How to Build a Conversation List Page Header

Now, we are going to add the header to the Conversation list section which will have a text header and a button. The complete UI implementation code is provided in the code snippet below:

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
                          Text("Add New",style: TextStyle(fontSize: 14,fontWeight: FontWeight.bold),),
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

Here, we have used the `SingleChildScrollView` so that the body section of the **chatPage.dart** is entirely scrollable. 

Then, we have used the `BouncingScrollPhysics` instance to give the bouncing effect when a user's scrolling reaches the end or beginning. 

Next, we have added a Text widget and a Container to display the bottom at the right-hand side. 

Lastly, we have a `Column` widget as a child of the `SingleChildScrollView` widget so everything will appear vertically on the screen.

This will give us the following result as shown in the emulator below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-109.png)

Now, we are going to add a search bar just below the Header section.

### **How to Add the Search Bar**

In the `Column` widget from before, we are going to add a Search bar widget just below the Header UI section. So, as a second child of the `Column` widget, we need to insert the following code provided in the code snippet below:

```dart
Padding(
  padding: EdgeInsets.only(top: 16,left: 16,right: 16),
  child: TextField(
    decoration: InputDecoration(
      hintText: "Search...",
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

This will give us the following result as shown in the emulator below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-110.png)

### **How to Build the Conversation List**

Now that we have the Header section and a Search bar, we are going to implement the conversation list section.

For that, we need to implement a class object model to store the instances of conversation lists. 

So inside the **./lib** folder, we need to create a new folder called **./models**. Inside **./models**, we need to create a file called **chatUsersModel.dart**. 

In the model file, we need to create a model object class as shown in the code snippet below:

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

The object will house the user's name, text message, image URL, and time.

Next we need to create a list of users inside the **chatPage.dart** as shown in the code snippet below:

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

Now that we have the mock users' conversation list data, we can apply it to the conversation list to create a list view.

### **How to Make a Separate Class Widget for Individual Conversation**

Here, we are going to make a separate component widget for the individual items in the conversation list view.

For that, inside **./lib** create a folder called **./widgets**. And inside **./widgets** we need to create a file called **conversationList.dart.** Inside the new widget file, we can use the code from the following code snippet:

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

This widget file takes the user's name, text message, image URL, time, and a Boolean message type value as parameters. And it returns the template containing the values.

In the **chatPage.dart,** inside the `ListView` widget, we need to call the `ConversationList` widget by passing the required parameters as shown in the code snippet below:

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

Note that this `ListView` widget is to keep as the first child of the `Column` widget in the `chatPage` screen.

This will give us the following result as shown in the emulator below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-111.png)

This completes the UI implementation of our Conversation List Screen and Main Home page screen as a whole. Now, we'll move on to the implementation of the chat details screen.

## **How to Build a Chat Detail Screen**

Now, we are going to create a chat detail screen. For that, we need to create a new file called **chatDetailPage.dart** inside the **./lib/screens/** folder. For now, we are just going to add the basic code as shown in the code snippet below:

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
        title: Text("Chat Detail"),
      ),
      body: Container()
    );
  }
}

```

Here, we have returned a basic `AppBar` with Text and an empty Container as the `body` of the `Scaffold` widget.

Now, we are going to add navigation to `ChatDetailPage` on the `GestureHandler` widget's `onTap` method in the **conversationList.dart** widget file as shown in the code snippet below:

```dart
GestureDetector(
      onTap: (){
        Navigator.push(context, MaterialPageRoute(builder: (context){
          return ChatDetailPage();
        }));
      },

```

We can now navigate to the Chat detail screen as shown in the emulator demo below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/2021-01-20-13.40.11.gif)

### How to Build a Custom App Bar for Chat Detail Screen

Here, we are going to add a custom App bar at the top of the chat detail screen. For that, we are going to use the `AppBar` widget with various parameter configurations as shown in the code snippet below:

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
                      Text("Online",style: TextStyle(color: Colors.grey.shade600, fontSize: 13),),
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

This will give us the following result as shown in the emulator below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-112.png)

### **How to Implement the Bottom Text Box**

At the bottom of the chat detail screen, we need to add a messaging section that will contain a text editor and a button to send the message. 

For this, we are going to use the `Align` widget and align the child inside the widget with the bottom of the screen. The overall code is provided in the code snippet below:

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
                        hintText: "Write message...",
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

This will give us a messaging section with a text field to type the messages and a button to send the messages:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-113.png)

We also have a button to the left which we can use to add other menu options for messaging.

### **How to Set Up the Messages List Section in Chat Screen**

Now, we are going to create the UI for messages appearing in the chat detail screen.

First, we need to create a model that reflects the message instance object.

For that, we need to create a file called **chatMessageModel.dart** inside the **./models** folder and define the class object as follows:

```dart
import 'package:flutter/cupertino.dart';

class ChatMessage{
  String messageContent;
  String messageType;
  ChatMessage({@required this.messageContent, @required this.messageType});
}

```

The class object accepts the message content and message type (whether sender or receiver as instance values.

Now in the **chatDetailPage.dart**, we need to create a list of messages to display as shown in the code snippet below:

```dart
List<ChatMessage> messages = [
    ChatMessage(messageContent: "Hello, Will", messageType: "receiver"),
    ChatMessage(messageContent: "How have you been?", messageType: "receiver"),
    ChatMessage(messageContent: "Hey Kriss, I am doing fine dude. wbu?", messageType: "sender"),
    ChatMessage(messageContent: "ehhhh, doing OK.", messageType: "receiver"),
    ChatMessage(messageContent: "Is there any thing wrong?", messageType: "sender"),
  ];

```

Next, we are going to create a list view for the messages on top of the `Stack` widget's children, above the `Align` widget, as shown in the code snippet below:

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

Now the messages will appear in list form as shown in the emulator screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-114.png)

Now, we have the messages appearing on the screen but they are not styled the way we want in the chatting screen.

### How to Style and Position the Messages Based on Sender and Receiver

Now, we are going to style the message list so that it appears as a chat message bubble. We're also going to position them based on the message type using the `Align` widget as shown in the code snippet below:

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

This will give us the following result as shown in the emulator below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-115.png)

You can see an overall demo of the app's entire UI below:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/2021-01-20-13.52.45.gif)

Congrats! We have built an intuitive and modern chat app UI entirely in the Flutter and Dart ecosystem.

## Recap

Social messaging applications are an essential communication medium nowadays. Equipped with state of the art and powerful chat interfaces with audio and video calling, image and file attachments, and many more, these chat applications have made communication much more efficient. These apps have made the world smaller for us. 

The major objective of this article was to show you how to develop a simple intuitive UI for chat applications with a modern design in the Flutter ecosystem. The step-by-step implementation provided a detailed showcase of the app's UI and also gave an overview of the Flutter coding environment. 

I hope this tutorial helps you create your next chat application using Flutter.

You can also get inspiration for a chat app UI and feature development from top [Flutter chat app](https://www.instaflutter.com/app-templates/flutter-chat-app/) templates out there in the market. Make sure to check them out as well.

