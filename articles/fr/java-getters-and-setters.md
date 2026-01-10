---
title: Getters et Setters en Java Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-25T17:13:00.000Z'
originalURL: https://freecodecamp.org/news/java-getters-and-setters
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d90740569d1a4ca386a.jpg
tags:
- name: Java
  slug: java
seo_title: Getters et Setters en Java Expliqués
seo_desc: "Getters and setters are used to protect your data, particularly when creating\
  \ classes. \nFor each instance variable, a getter method returns its value while\
  \ a setter method sets or updates its value. Given this, getters and setters are\
  \ also known as a..."
---

Les getters et setters sont utilisés pour protéger vos données, en particulier lors de la création de classes. 

Pour chaque variable d'instance, une méthode getter retourne sa valeur tandis qu'une méthode setter définit ou met à jour sa valeur. Ainsi, les getters et setters sont également connus sous le nom d'_accessors_ et de _mutators_, respectivement.

Par convention, les getters commencent par le mot "get" et les setters par le mot "set", suivis du nom d'une variable. Dans les deux cas, la première lettre du nom de la variable est en majuscule :

```java
public class Vehicle {
  private String color;
  
  // Getter
  public String getColor() {
    return color;
  }
  
  // Setter
  public void setColor(String c) {
    this.color = c;
  }
}
```

La méthode getter retourne la valeur de l'attribut. La méthode setter prend un paramètre et l'assigne à l'attribut.

Une fois le getter et le setter définis, nous les utilisons dans notre main :

```java
public static void main(String[] args) {
  Vehicle v1 = new Vehicle();
  v1.setColor("Red");
  System.out.println(v1.getColor());
}

// Affiche "Red"
```

Les getters et setters permettent de contrôler les valeurs. Vous pouvez valider la valeur donnée dans le setter avant de l'assigner.

### Pourquoi utiliser des getters et setters ?

Les getters et setters vous permettent de contrôler comment les variables importantes sont accédées et mises à jour dans votre code. Par exemple, considérons cette méthode setter :

```java
public void setNumber(int number) {
  if (number < 1 || number > 10) {
    throw new IllegalArgumentException();
  }
  this.number = num;
}
```

En utilisant la méthode `setNumber`, vous pouvez être sûr que la valeur de `number` est toujours comprise entre 1 et 10. Cela est bien mieux que de mettre à jour la variable `number` directement :

```java
obj.number = 13;
```

Si vous mettez à jour `number` directement, il est possible que vous causiez des effets secondaires non intentionnels ailleurs dans votre code. Ici, définir `number` à 13 viole la contrainte de 1 à 10 que nous voulons établir. 

Rendre `number` une variable privée et utiliser la méthode `setNumber` empêcherait cela de se produire. 

D'autre part, la seule façon de lire la valeur de `number` est d'utiliser une méthode getter :

```java
public int getNumber() {
  return this.number;
}
```