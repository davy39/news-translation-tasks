---
title: How to Serialize An Object In Flutter
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
seo_title: null
seo_desc: 'If you intend to save user data to the shared preferences or local storage
  in your Flutter application, you will need to serialize it manually.

  This is because both methods only support a limited selection of primitive object
  types and your object wi...'
---

If you intend to save user data to the shared preferences or local storage in your Flutter application, you will need to serialize it manually.

This is because both methods only support a limited selection of primitive object types and your object will probably not fall into any category. To do this we will be using the **_dart:convert_** decoder with its jsonEncode/jsonDecode methods, so make sure to import it into your project.

To do this, import the class in your main dart file:

```dart
import 'dart:convert';

```

## How to build a Model Class in Dart

To allow our object to become enabled for decoding/encoding we first need to create a Model class for it. This class will represent the object and it’s fields and have the important methods which will do the heavy work of encoding/decoding. The first one is called **_fromJson_** and the second one is called **toJson**. We will show various examples of complex objects and how to serialize them, but for the beginning, we’ll start with a simple one.

We’ll imagine we have a doughnut shop, where we have various doughnuts. Each doughnut is an object that contains the following keys:

* Name - String
* Filling - String
* Topping - String
* Price - Double

In Dart, it would like this:

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

You may have noticed a weird type in there called **_dynamic_**. Dynamic signifies an unknown type in the dart language, one which will be realized during runtime. Think of it as similar to the Object type in Java, which all types inherit from. Any object can be cast into dynamic to invoke methods on it. If no type is declared for a variable or a return type for a method, it is assumed to be dynamic.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-242.png)
_Photo by [Unsplash](https://unsplash.com/@sharonmccutcheon?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Sharon McCutcheon</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## How to Serialize and De-Serialize Data in Flutter

Now that we have our model class, we can use it to serialized and de-serialize our data. Below is an example of just how to do that.

Creating a doughnut object is simple:

```dart
Doughnut myDoughnut = new Doughnut("Glazed", "None", "Sprinkles", 2.99);

```

And now we can serialize it by using jsonEncode:

```dart
String encodedDoughnut = jsonEncode(myDoughnut);

```

Under the hood, jsonEncode calls our own toJson method that we created in our doughnut model class. The same also applies for jsonDecode as it calls the fromJson method.

In string form, our doughnut object, now looks like this:

```dart
{"name":"Glazed","filling":"None","topping":"Sprinkles","price":2.99}

```

And after we decode it,

```dart
Map<String, dynamic> decodedDoughnut = jsonDecode(encodedDoughnut);

```

we will get:

```dart
{name: Glazed, filling: None, topping: Sprinkles, price: 2.99}

```

Did you notice the subtle differences?

The decoded object is now a Map with keys of string type and values of dynamic type. If we want to convert this data type back to our original object, we need to access the properties of the map:

```dart
Doughnut newDoughnut = new Doughnut(decodedDoughnut["name"], 
                                    decodedDoughnut["filling"], 
                                    decodedDoughnut["topping"], 
                                    decodedDoughnut["price"]);
```

## How to Serialize Arrays in Dart

Life is not as simple as a doughnut(if only, right?), so we have to take into account that we won’t always be dealing with parameter types that are simple. Let’s assume that the toppings field is not a String, but is an Array of strings. First, let’s redefine the toppings field:

```dart
String topping => List<String> toppings;

```

Then, in our fromJson method we will have to do the following:

```dart
Doughnut.fromJson(Map<String, dynamic> json) {
    name = json['name'];
    filling = json['filling'];
    var toppingsFromJson = json['toppings'];
    toppings = new List<String>.from(toppingsFromJson);
    price = json['price'];

  }
```

Notice, how we have a temporary variable to first extract the value from the json variable and then we explicitly convert the value to our toppings list original type. We have to do this since at first, the type for the value of toppings is dynamic and dart does not know which type it is explicitly.  


## Complex Objects

No one ever buys only one doughnut, right? That would be useless. Let’s imagine we have a dozen. So now we are dealing with a list of objects of Doughnut type. To serialize/de-serialize a list of objects we will use the model class above, but we will need to create a different model class to handle the list.

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

As you can see, we now have a model class that has a field of type List that holds Doughnut objects.

Similar to the example above, to serialize the object we use the jsonEncode method and when we want to decode the object we have to perform the following:

```dart
Map<String, dynamic> decodedDoughnuts = jsonDecode(encodedJson);
List<dynamic> decodedJson =  decodedDoughnuts['doughnuts'];
decodedJson.map((elem) => jsonDecode(elem));
```

To see all that we covered in this article, head over to [the repository on GitHub](https://github.com/TomerPacific/MediumArticles/tree/master/serialization_example).

