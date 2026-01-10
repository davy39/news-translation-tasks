---
title: Comment Sérialiser un Objet dans Flutter
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-06-09T21:57:00.000Z'
originalURL: https://freecodecamp.org/news/serialize-object-flutter
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca227740569d1a4ca52e4.jpg
tags:
- name: Flutter
  slug: flutter
seo_title: Comment Sérialiser un Objet dans Flutter
seo_desc: 'If you intend to save user data to the shared preferences or local storage
  in your Flutter application, you will need to serialize it manually.

  This is because both methods only support a limited selection of primitive object
  types and your object wi...'
---

Si vous avez l'intention de sauvegarder les données utilisateur dans les préférences partagées ou le stockage local de votre application Flutter, vous devrez les sérialiser manuellement.

C'est parce que les deux méthodes ne supportent qu'une sélection limitée de types d'objets primitifs et votre objet ne rentrera probablement dans aucune catégorie. Pour ce faire, nous utiliserons le décodeur **_dart:convert_** avec ses méthodes jsonEncode/jsonDecode, alors assurez-vous de l'importer dans votre projet.

Pour ce faire, importez la classe dans votre fichier dart principal :

```dart
import 'dart:convert';

```

## Comment créer une Classe Modèle en Dart

Pour permettre à notre objet d'être activé pour le décodage/encodage, nous devons d'abord créer une classe Modèle pour celui-ci. Cette classe représentera l'objet et ses champs et aura les méthodes importantes qui feront le travail lourd d'encodage/décodage. La première s'appelle **_fromJson_** et la seconde s'appelle **toJson**. Nous montrerons divers exemples d'objets complexes et comment les sérialiser, mais pour commencer, nous commencerons par un exemple simple.

Imaginons que nous avons une boutique de beignets, où nous avons divers beignets. Chaque beignet est un objet qui contient les clés suivantes :

* Nom - String
* Garniture - String
* Garniture supérieure - String
* Prix - Double

En Dart, cela ressemblerait à ceci :

```dart
class Doughnut {
  final String name;
  final String filling;
  final String topping;
  final double price;

  Doughnut(this.name, this.filling, this.topping, this.price);

  Doughnut.fromJson(Map<String, dynamic> json)
      : name = json['name'],
        filling = json['filling'],
        topping = json['topping'],
        price = json['price'];

  Map<String, dynamic> toJson() => {
    'name' : name,
    'filling' : filling,
    'topping' : topping,
    'price' : price
  };
}
```

Vous avez peut-être remarqué un type étrange appelé **_dynamic_**. Dynamic signifie un type inconnu dans le langage Dart, un type qui sera réalisé pendant l'exécution. Pensez à cela comme similaire au type Object en Java, dont tous les types héritent. Tout objet peut être converti en dynamic pour invoquer des méthodes sur celui-ci. Si aucun type n'est déclaré pour une variable ou un type de retour pour une méthode, il est supposé être dynamic.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-242.png)
_Photo par [Unsplash](https://unsplash.com/@sharonmccutcheon?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Sharon McCutcheon</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Comment Sérialiser et Désérialiser des Données dans Flutter

Maintenant que nous avons notre classe modèle, nous pouvons l'utiliser pour sérialiser et désérialiser nos données. Voici un exemple de la manière de procéder.

Créer un objet beignet est simple :

```dart
Doughnut myDoughnut = new Doughnut("Glazed", "None", "Sprinkles", 2.99);

```

Et maintenant nous pouvons le sérialiser en utilisant jsonEncode :

```dart
String encodedDoughnut = jsonEncode(myDoughnut);

```

Sous le capot, jsonEncode appelle notre propre méthode toJson que nous avons créée dans notre classe modèle de beignet. La même chose s'applique pour jsonDecode car elle appelle la méthode fromJson.

Sous forme de chaîne, notre objet beignet ressemble maintenant à ceci :

```dart
{"name":"Glazed","filling":"None","topping":"Sprinkles","price":2.99}

```

Et après l'avoir décodé,

```dart
Map<String, dynamic> decodedDoughnut = jsonDecode(encodedDoughnut);

```

nous obtiendrons :

```dart
{name: Glazed, filling: None, topping: Sprinkles, price: 2.99}

```

Avez-vous remarqué les différences subtiles ?

L'objet décodé est maintenant une Map avec des clés de type string et des valeurs de type dynamic. Si nous voulons convertir ce type de données en notre objet original, nous devons accéder aux propriétés de la map :

```dart
Doughnut newDoughnut = new Doughnut(decodedDoughnut["name"], 
                                    decodedDoughnut["filling"], 
                                    decodedDoughnut["topping"], 
                                    decodedDoughnut["price"]);
```

## Comment Sérialiser des Tableaux en Dart

La vie n'est pas aussi simple qu'un beignet (si seulement, n'est-ce pas ?), donc nous devons prendre en compte que nous ne traiterons pas toujours avec des types de paramètres simples. Supposons que le champ toppings n'est pas une String, mais un tableau de strings. D'abord, redéfinissons le champ toppings :

```dart
String topping => List<String> toppings;

```

Ensuite, dans notre méthode fromJson, nous devrons faire ce qui suit :

```dart
Doughnut.fromJson(Map<String, dynamic> json) {
    name = json['name'];
    filling = json['filling'];
    var toppingsFromJson = json['toppings'];
    toppings = new List<String>.from(toppingsFromJson);
    price = json['price'];

  }
```

Remarquez comment nous avons une variable temporaire pour extraire d'abord la valeur de la variable json, puis nous convertissons explicitement la valeur en notre type original de liste de toppings. Nous devons faire cela car au début, le type de la valeur des toppings est dynamic et Dart ne sait pas explicitement de quel type il s'agit.

## Objets Complexes

Personne n'achète jamais un seul beignet, n'est-ce pas ? Cela serait inutile. Imaginons que nous en avons une douzaine. Nous traitons donc maintenant avec une liste d'objets de type Doughnut. Pour sérialiser/désérialiser une liste d'objets, nous utiliserons la classe modèle ci-dessus, mais nous devrons créer une classe modèle différente pour gérer la liste.

```dart
import 'package:serialization_example/models/doughnut.dart';

class DoughnutList {
  final List<Doughnut> doughnuts;

  DoughnutList(this.doughnuts);

  DoughnutList.fromJson(Map<String, dynamic> json)
  : doughnuts = json['doughnuts'] != null ? List<Doughnut>.from(json['doughnuts']) : null;

  Map<String, dynamic> toJson()  =>
  {
    'doughnuts': doughnuts,
  };

}
```

Comme vous pouvez le voir, nous avons maintenant une classe modèle qui a un champ de type List qui contient des objets Doughnut.

Similaire à l'exemple ci-dessus, pour sérialiser l'objet, nous utilisons la méthode jsonEncode et lorsque nous voulons décoder l'objet, nous devons effectuer ce qui suit :

```dart
Map<String, dynamic> decodedDoughnuts = jsonDecode(encodedJson);
List<dynamic> decodedJson =  decodedDoughnuts['doughnuts'];
decodedJson.map((elem) => jsonDecode(elem));
```

Pour voir tout ce que nous avons couvert dans cet article, rendez-vous sur [le dépôt sur GitHub](https://github.com/TomerPacific/MediumArticles/tree/master/serialization_example).