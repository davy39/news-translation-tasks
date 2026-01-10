---
title: Comment fonctionnent les classes en C++
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2021-03-09T01:48:00.000Z'
originalURL: https://freecodecamp.org/news/how-classes-work-in-cplusplus
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60424789a7946308b7682566.jpg
tags:
- name: C++
  slug: c-2
- name: class
  slug: class
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Comment fonctionnent les classes en C++
seo_desc: "C++ supports Object Oriented Programming, and classes and objects are the\
  \ heart of this programming paradigm. \nYou might be wondering – what is a class\
  \ and why do we need them? In this article I'll go over some basics to help you\
  \ understand how class..."
---

C++ prend en charge la programmation orientée objet, et les classes et objets sont au cœur de ce paradigme de programmation. 

Vous vous demandez peut-être – qu'est-ce qu'une classe et pourquoi en avons-nous besoin ? Dans cet article, je vais passer en revue quelques bases pour vous aider à comprendre comment fonctionnent les classes en C++.

## Comment fonctionnent les classes en C++

C++ dispose de divers types intégrés (comme `bool`, `int`, `floats`, etc.). Chacun de ces types possède diverses caractéristiques (par exemple, la taille de leur occupation mémoire). Les opérateurs ont des significations différentes pour chaque type différent.

Par exemple : L'opérateur '+' ajoute des entiers, des flottants et des doubles :

```c++
int x = 5;
int y = 6;

int z= x+y;//z==11
```

Cependant, si nous utilisons l'opérateur '+' avec des chaînes de caractères, il les concatène.

```c++
string s1 = "abhilekh";
string s2 = "gautam";

string s3=s1+s2;//s3 sera abhilekhgautam
```

Ici, x, y et z représentent un entier, tandis que s1, s2 et s3 représentent des chaînes de caractères. Donc x, y et z sont des objets de type `int`. Pendant ce temps, s1, s2 et s3 sont des objets de type `string`.

**Note : ne confondez pas cela avec le mot 'Objet'**. Un objet est tout ce qui occupe de la mémoire.

Mais que faire si nous voulons avoir un type qui représente des objets de notre vie quotidienne ? Comment pourriez-vous représenter une maison, une voiture, des livres, des animaux, etc. ? C'est pourquoi nous avons besoin des classes.

**Une classe est un type défini par l'utilisateur**. Cela signifie que vous pouvez définir vos propres types. Vous pouvez créer vos propres types comme des entiers, des flottants et des caractères. Vous pouvez définir des opérateurs pour vos types et définir diverses propriétés pour vos propres types.

Les classes sont vraiment une fonctionnalité puissante. Voyons comment elles fonctionnent :

```c++
class Book{
string author_name,title;
int no_of_pages,edition_no;
//...
};
```

Ici, nous avons créé une classe nommée Book. Le mot-clé class est suffisant pour que nous comprenions cela.

Un livre doit avoir un auteur, un titre et des pages – ce sont les membres de notre classe. Ici, `book` représente une entité qui possède ces caractéristiques. 

Mais créer notre propre type ne sera pas utile tant que nous n'avons pas un objet de ce type. Alors, comment faire ?

```c++
int x;//x est un objet de type x.

Book y;//y est un objet de type Book
```

La seule différence ici est que x est un objet d'un type intégré (c'est-à-dire, `int`) et y est un objet du type Book (Book est un type défini par l'utilisateur, défini par vous).

Alors, discutons maintenant des bases de la définition d'une classe, de la manière de créer des objets de cette classe, et des façons dont nous pouvons utiliser ces objets.

## Quelles sont les fonctions membres en C++ ?

Les fonctions déclarées dans une classe sont des fonctions membres. Elles ne peuvent être invoquées que par l'objet de la classe dans laquelle la fonction est définie.

Mettons maintenant à jour notre classe `Book` un peu :

```c++
class Book{
//..
public:
void update_edition(int edition);
//..
};
```

C'est tout – `update_edition` est une fonction membre de notre classe book. Nous pouvons définir notre fonction de deux manières : à l'intérieur de la classe, et à l'extérieur de la classe.

Voyons comment chacune d'elles fonctionne :

```c++
/*Déclaration à l'intérieur de la classe*/
class Book{
//..
public:
void update_edition(int edition){
//Définissez votre fonction 
edition_no = edition;
}
};
```

```c++
/* Déclaration à l'extérieur de la classe*/
void Book::update_edition(int edition){
//Définissez votre fonction ici
//..
}
```

Et pour appeler la fonction ?

```c++
Book y;//y est un objet de type Book

y.update_edition(5);
```

Rappelez-vous que seuls les objets de type Book peuvent invoquer la fonction. **Un appel d'objets de tout autre type entraînera une erreur syntaxique.**

Une fonction membre (non statique) connaît toujours l'objet pour lequel elle a été invoquée et peut s'y référer comme ceci :

```c++
void Book::update_edition(int edition){
this->edition_no = edition;
}
```

## Types de fonctions membres en C++

Il existe plusieurs types de fonctions membres en C++. Examinons chacun d'eux plus en détail ici.

### Fonctions membres constantes

```c++
class Book{
//..
public:
//..
int display_edition() const{
return edition_no;
}
//..
};
```

Le mot-clé `const` indique que cette fonction ne modifie pas l'état de la fonction.

Changer l'état de la fonction à partir d'une fonction membre constante entraînera une erreur.

```c++
int Book::book_edition() const{
edition_no = edition_no + 1;//erreur : impossible de changer la valeur dans une fonction constante
}
```

### Fonctions membres statiques

Si vous avez une fonction membre qui a besoin d'accéder aux membres de la classe mais qui n'a pas besoin d'être invoquée par chaque objet de cette classe, vous devez la déclarer comme statique.

De telles fonctions feront partie de la classe mais ne feront pas partie de l'objet.

```c++
class Book{
//..
public:
static void my_static_func();
};
```

Un membre statique peut être référencé sans utiliser d'objet.

```
void Book::my_static_func(){
//définir ici.
}
```

Le mot-clé **static** ne doit pas être répété dans la déclaration de la fonction. Les fonctions membres statiques n'ont pas accès au pointeur **`this`**.

### Fonctions amies

Les fonctions amies ne sont pas dans la portée d'une classe et n'ont aucun accès à **`this`**.

```c++
class Book{
//..
public:
//..
void check();
void display();
//..
};

class E_book{
//..
public:
//..
friend void Book::check();
};
```

Ici, la fonction membre `check` de la classe `Book` est une amie de la classe `E_book`.

Si nous voulons que toutes les fonctions membres d'une classe soient les amies d'une autre classe, nous pouvons utiliser la syntaxe suivante :

```c++
class E_book{
//...
public:
//..
friend class Book;
};
```

Maintenant, toutes les fonctions de la classe `Book` sont des amies de la classe `E-book`.

### Spécificateurs d'accès

Si vous avez un background en C, vous vous souvenez peut-être de la création de votre propre type en utilisant le mot-clé **struct**.

```c,c++
struct Book{
char author_name[20];
char title[20];
int no_of_page,edition_no;
};

Book b1;//b1 est un objet de type Book
```

La structure est un type défini par l'utilisateur. En fait, **la structure est un type de classe dont tous les membres sont publics par défaut.** Confus ?

Vous vous souvenez de l'étiquette **`public:`** que nous avons utilisée dans l'un de nos extraits de code précédents ci-dessus ? C'est ce que nous appelons un spécificateur d'accès.

Alors, quelle est la différence entre les spécificateurs d'accès privés et publics ?

Les membres après une étiquette `private` sont dits membres privés. Cela signifie qu'ils ne peuvent être accédés que par la fonction membre de cette classe. Si aucune étiquette n'est fournie, elle est privée par défaut.

D'autre part, les membres après l'étiquette `public` sont accessibles partout.

Ces spécificateurs sont utilisés à des fins de **masquage de données**, d'**abstraction de données** et d'**encapsulation de données**.

### Constructeurs

Un constructeur est une fonction membre qui est utilisée pour initialiser un objet. Un constructeur est exécuté chaque fois qu'un objet de ce type de classe est créé. 

Le nom de la fonction constructeur est le même que le nom de la classe et elle n'a aucun type de retour, non plus.

```c++
class Book{
//..
public:
//Constructeur

Book(){  //aucun type de retour et nom identique au nom de la classe

//définir le constructeur ici

}
};
```

Il peut y avoir plusieurs constructeurs pour une classe car il peut y avoir plusieurs fonctions avec le même nom, ce qu'on appelle la surcharge de fonctions.

### Destructeurs

Le destructeur libère la mémoire occupée par l'objet. Il détruit simplement l'objet. Le symbole `~` (tilde) désigne un destructeur.

```c++
class Book{
//..
public:
//constructeur
//..
//destructeur
~Book(){
//détruire l'objet ici
}
};
```

## C'est tout !

En utilisant ces divers concepts de classe en C++, vous pouvez facilement créer de nouveaux types (vos propres types) que vous pouvez utiliser commodément comme des types intégrés.

Vous pouvez lire mes autres articles [ici](https://abhilekhblogs.blogspot.com/).