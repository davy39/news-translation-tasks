---
title: Comment gérer la navigation dans vos applications Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-14T17:59:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-navigation-in-your-flutter-apps-ceaf2f411dcd
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca450740569d1a4ca61a9.jpg
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment gérer la navigation dans vos applications Flutter
seo_desc: 'By Sameeha Rahman

  Flutter is a Google product used to build hybrid mobile apps with Dart as the coding
  language.

  An app page in Flutter is a Widget, a description of the UI portrayed. To make a
  legitimate app, you need many of these pages, displaying...'
---

Par Sameeha Rahman

Flutter est un produit Google utilisé pour créer des applications mobiles hybrides avec Dart comme langage de programmation.

Une page d'application dans Flutter est un Widget, une description de l'interface utilisateur représentée. Pour créer une application légitime, vous avez besoin de nombreuses pages de ce type, affichant une multitude de fonctionnalités. Tout va bien une fois que vous avez créé une nouvelle page. Mais, comment passez-vous de l'une à l'autre ?

Assez simple : vous utilisez la classe [Navigator](https://docs.flutter.io/flutter/widgets/Navigator-class.html), intégrée dans le SDK Flutter.

### Navigator

Navigator est un autre Widget qui gère les pages d'une application dans un format de type pile. Les pages en plein écran sont appelées routes lorsqu'elles sont utilisées dans le Navigator. Le Navigator fonctionne comme une implémentation normale de pile. Il dispose de deux méthodes bien connues, `push` et `pop`.

1. Push : La méthode push est utilisée pour ajouter une autre route au sommet de la pile actuelle. La nouvelle page est affichée par-dessus la précédente.
2. Pop : Comme le Navigator fonctionne comme une pile, il utilise le principe LIFO (Last-In, First-Out). La méthode pop supprime la route la plus haute de la pile. Cela affiche la page précédente à l'utilisateur.

Dans cet article, je vais montrer :

1. Deux façons de naviguer et
2. Passer des données à la page suivante.

### Navigation normale

Il existe deux façons de procéder :

#### Créer une nouvelle page dans la méthode `push`

Dans cette méthode, une nouvelle route est créée en utilisant la classe `MaterialPageRoute`. Une nouvelle page (Widget) est créée à l'intérieur. Ces deux instructions de création sont encapsulées dans la méthode `push` et ajoutent cette page au sommet de la pile.

Pour afficher un exemple simple, j'utilise du code d'un ancien dépôt et d'un [article de blog](https://medium.freecodecamp.org/https-medium-com-rahman-sameeha-whats-flutter-an-intro-to-dart-6fc42ba7c4a3). Je l'ai modifié pour inclure un bouton sur le composant `CustomCard`. Ce bouton utilise la méthode `push`, tandis que la nouvelle route et la nouvelle page sont créées à l'intérieur.

```dart
Widget build(BuildContext context) {  
	return Card(    
    	child: Column(      
        	children: <Widget>[        
            	Text('Card $index'),        
                FlatButton(          
                	child: Text("Press Me"),          
                    onPressed: () {            
                    	Navigator.push(context, MaterialPageRoute<void>(
                        	builder: (BuildContext context) {                
                            	return Scaffold(                  
                                	appBar: AppBar(title: Text('My Page')),
                                    body: Center(                    
                                    	child: FlatButton(
                                        	child: Text('POP'),
                                           	onPressed: () {
                                            	Navigator.pop(context);
                                            },                    
                                        ),                  
                                    ),                
                                );              
                            },            
                        ));          
                    }),    
            ],  
        ));
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/ALt9-AfRlKL7NIYPAsCu1LJvMEuoaS4Xqy1H)

#### Ajouter des routes au point d'entrée de l'application

En rétrospective, les applications ont de nombreuses pages, et souvent avec un codage complexe. Il ne serait pas facile de continuer à créer une nouvelle page à chaque fois. Cela est particulièrement vrai si la page est accessible depuis de nombreuses zones différentes. Vous pourriez perdre la trace du code pour chaque route identique.

Ainsi, dans la deuxième méthode, la page est créée une fois mais ajoutée comme une route dans le point d'entrée de l'application, `main.dart`. Ces routes sont nommées comme des chemins de fichiers puisque la page racine de l'application est le chemin `/`.

Vous commencez par créer une nouvelle page d'application, comme suit :

```dart
class SecondPage extends StatelessWidget {
	@override
	Widget build(BuildContext context) {
		return Scaffold(
			appBar: AppBar(
				title: Text('Second Page'),
			),
			body: Center(
				child: RaisedButton(
					child: Text('Back To HomeScreen'),
					color: Theme.of(context).primaryColor,
					textColor: Colors.white,
					onPressed: () => Navigator.pop(context)),
			),
		);
	}
}
```

Ensuite, importez la nouvelle page dans le fichier `main.dart` et ajoutez-la à la liste des routes à l'intérieur du constructeur MaterialApp.

```dart
class MyApp extends StatelessWidget {
// This widget is the root of your application.
	@override
	Widget build(BuildContext context) {
		return MaterialApp(
			title: 'Flutter Demo',
			theme: ThemeData(
				primarySwatch: Colors.green,
			),
			home: MyHomePage(title: 'Flutter Demo Home Page'),
			routes: <String, WidgetBuilder>{
				'/a': (BuildContext context) => SecondPage(),
			});
	}
}
```

Nous modifions ensuite la méthode onPressed du `FlatButton` dans le `CustomCard` comme suit :

```
Navigator.pushNamed(context, '/a');
```

![Image](https://cdn-media-1.freecodecamp.org/images/VBQNP-t93AVi2wmCoiyYawJk326olmYxNByE)

Dans l'exemple ci-dessus, l'utilisateur est redirigé vers la classe `SecondPage` créée car elle est la page correspondante au chemin `/a`.

### Passer des données entre les pages

Maintenant, pour la dernière partie de la démonstration, passer des données à la page suivante. Pour ce faire de manière simple, il faut un mélange des deux méthodes de navigation mentionnées ci-dessus.

Les méthodes `pushNamed` et la création d'une nouvelle route à l'intérieur de la méthode push peuvent être utilisées pour passer des données à la nouvelle page. Pour cette dernière, une nouvelle page n'a pas besoin d'être créée. Le paramètre builder de `MaterialPageRoute` appellera maintenant le constructeur de la classe `SecondPage`.

Mettez à jour la classe `SecondPage` pour accepter les données qui lui sont passées, comme suit :

```dart
class SecondPage extends StatelessWidget {
	SecondPage({@required this.title});
	final title;
    
	@override
	Widget build(BuildContext context) {
		return Scaffold(
			appBar: AppBar(
				title: Text('Card No. $title'),
			),
			body: Center(...),
		);
	}
}
```

La méthode onPressed des `FlatButtons` est maintenant modifiée comme suit :

```dart
Navigator.push(context,
	MaterialPageRoute(
		builder: (context) => SecondPage(title: index)
	)
);
```

Ou comme ceci :

```dart
Navigator.pushNamed( context, '/a',
	arguments: <String, String>{
		'title': index + "",
	},
);
```

L'index de la carte est maintenant passé à la classe `SecondPage` et est affiché dans l'`AppBar`.

![Image](https://cdn-media-1.freecodecamp.org/images/OuRrgD0YV1Ukxgjv7-MZL7pB2sFxfKHaKNxb)

Merci d'avoir lu ! Vous pouvez trouver le dépôt [ici](https://github.com/samsam-026/flutter-example).

Trouvez le commit pour les modifications suivantes [ici](https://github.com/samsam-026/flutter-example/commit/166122bf68f3a17ed516f91cb9d9341571c3da50).