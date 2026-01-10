---
title: Mots-clés C++ que vous devriez connaître
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2021-03-22T16:39:23.000Z'
originalURL: https://freecodecamp.org/news/cpp-keywords-you-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/keyword.png
tags:
- name: C++
  slug: c-2
seo_title: Mots-clés C++ que vous devriez connaître
seo_desc: 'C++ has various keywords, and you should know what they are and how to
  use them. So in this article, I will be talking about some of the most important
  keywords you''ll find in the language.

  What are Keywords in C++?

  Keywords are certain reserved word...'
---

C++ possède divers mots-clés, et vous devriez savoir ce qu'ils sont et comment les utiliser. Donc dans cet article, je vais parler de certains des mots-clés les plus importants que vous trouverez dans le langage.

## Qu'est-ce que les mots-clés en C++ ?

Les mots-clés sont certains mots réservés qui ont une signification prédéfinie en C++. Puisque les mots-clés ont leur propre signification prédéfinie, ils ne peuvent pas être utilisés comme identifiants (par exemple, le nom d'une fonction ou le nom d'une variable).

La définition de fonction ci-dessous est une erreur parce que **friend** est un mot-clé en C++.

```c++
void friend(){
/*.......*/
}
```

Regardons quelques-uns des mots-clés courants en C++ et comment ils sont utilisés.

## Mots-clés C++

### Le mot-clé `typedef` en C++

Parfois, il peut être fastidieux de déclarer une variable d'un certain type comme ceci :

```c++
const unsigned char
```

Les programmeurs ont du mal à déclarer de telles variables, et elles sont trop longues à utiliser fréquemment. Ne pouvons-nous pas les rendre plus courtes ou créer quelque chose de différent ? Oui, nous pouvons.

En utilisant **`typedef`**, nous pouvons créer des synonymes :

```c++
typedef const unsigned char CON_UCHAR;
```

Ainsi, au lieu d'utiliser de tels types de base longs, comme ceci :

```c++
const unsigned char x;
```

Nous pouvons utiliser ceci :

```c++
CON_UCHAR x;
```

Les **typedefs** sont également utiles pour la déclaration de pointeurs :

```c++
typedef char *const CON_PTRCHAR; // pointeur constant vers char

typedef const char* PTR_CONCHAR; // pointeur vers char constant
```

### Le mot-clé `bool` en C++

**bool** est un nom de type qui a deux valeurs – il est soit **true** soit **false**.

Toute valeur non nulle est **true**, tandis que zéro est **false**.

```c++
if(1){
std::cout<<"Hello World"<<'\n';
}
else{
std::cout<<"Sorry World"<<'\n';
}
```

Puisque toutes les valeurs non nulles sont vraies, chaque fois que le programme s'exécute, il affiche **Hello World**.

Rappelez-vous que les deux valeurs booléennes, **true** et **false**, sont également des mots-clés.

### Le mot-clé `using` en C++

```c++
using namespace std;
```

Vous avez peut-être utilisé le mot-clé **using** sans le savoir. Il peut être utilisé comme ceci :

**`using-declaration`** :

```c++
namespace My_space{

class My_class{
/*Votre code ici*/
};
}

namespace Her_space{

using My_space::My_class;

}
```

Voici à quoi ressemble une déclaration using. Une déclaration using apporte chaque déclaration avec un nom donné à une portée.

**`using directive`** :

L'exemple le plus courant d'une directive using est celui-ci :

```c++
using namespace std;
```

La ligne de code ci-dessus rend chaque nom de l'espace de noms std disponible.

### Les mots-clés `public`, `protected` et `private` en C++

Les mots-clés **public**, **protected** et **private** sont utilisés comme spécificateurs d'accès dans une classe.

```c++
class Home{
private:
int members;
protected:
double tot_expenditure;
public:
void display_detail();
};
```

Les membres après l'étiquette **private** ne sont accessibles que par le biais des fonctions membres. Si aucune étiquette n'est fournie, alors elle est privée par défaut.

Les membres après l'étiquette **public** sont accessibles partout.

Les membres après l'étiquette **protected** sont similaires aux membres **public** pour une classe dérivée et sont similaires aux membres **private** pour une classe non dérivée.

### Le mot-clé `enum` en C++

Une énumération est un type défini par l'utilisateur. Nous déclarons une énumération en utilisant le mot-clé **enum**.

```c++
enum days{SUN, MON, TUE, WED, THU, FRI, SAT};
```

Ici, SUN, MON, TUE ... sont appelés énumérateurs et leurs valeurs sont assignées en augmentant à partir de 0.

Par défaut, SUN==0, MON ==1 et ainsi de suite.

Cependant, nous pouvons également initialiser nous-mêmes les énumérateurs.

```c++
enum{ a = 5, b = 6};
```

Par défaut, les énumérations sont converties en entiers pour les opérations arithmétiques. Puisque les énumérations sont des _types définis par l'utilisateur_, nous pouvons [surcharger des opérateurs pour eux](https://www.freecodecamp.org/news/how-to-overload-operators-in-cplusplus/), aussi.

### Le mot-clé `new` en C++

Le mot-clé **new** (également un opérateur) est utilisé pour créer des objets dans le magasin libre (également appelé tas).

```c++
int main(){

int *p = new int;

*p = 20;
//..

}


```

Pour la ligne de code ci-dessus, l'opérateur new alloue une mémoire pour stocker un objet de type entier et retourne un pointeur pointant vers cette adresse allouée.

### Le mot-clé `delete` en C++

La mémoire est une ressource importante pour nous. Nous devons donc l'utiliser judicieusement. La mémoire indésirable ne doit pas être occupée. Donc **delete** (également un opérateur) est utilisé pour désallouer la mémoire qui a été précédemment allouée par l'opérateur **new**.

```c++
int main(){

int *p = new int;
*p =20;

delete p;
//..

}
```

### Le mot-clé `this` en C++

Toutes les fonctions membres (non statiques) savent pour quel objet elles ont été invoquées et elles peuvent s'y référer en utilisant le pointeur **this**.

```c++
class A{
int b;
public:
//...
void display() const;
};
```

Considérons une classe qui a un membre privé b et une fonction membre display.

Notre fonction display serait la suivante :

```c++
void A::display() const{
cout<<"b = "<<b<<'\n';
}
```

Le même code ci-dessus peut être écrit en utilisant **this** comme ceci :

```c++
void A::display() const{
cout<<"b = "<<this->b<<'\n';
}
```

Notez que **this** est un pointeur, donc nous devons utiliser l'opérateur ->. De plus, **this** ici fait référence à l'objet qui a invoqué la fonction.

### Le mot-clé `class` en C++

C++ supporte la programmation orientée objet, donc nous avons le concept de classes. Le mot-clé **class** est utilisé pour déclarer/définir une classe.

```c++
class Fb_user{
//..votre code ici
};
```

**struct** est également un mot-clé. C'est une classe avec tous les membres étiquetés publics par défaut.

```c++
struct Fb_user{
//...Votre code ici
};
```

Le code ci-dessus est une abréviation pour ce code :

```c++
class Fb_user{
public:
//..votre code ici
};
```

Pour en savoir plus sur les classes, vous pouvez vous référer à mon article approfondi sur les classes [ici](https://www.freecodecamp.org/news/how-classes-work-in-cplusplus/).

### Le mot-clé `operator` en C++

Le mot-clé **operator** est utilisé lors de la surcharge des opérateurs. La syntaxe pour surcharger un opérateur est la suivante :

```c++
return_type operator operator's_symbol(parameters){
//...Votre code ici...
}
```

Pour en savoir plus sur la surcharge des opérateurs en C++, vous pouvez vous référer à mon article [ici](https://www.freecodecamp.org/news/how-to-overload-operators-in-cplusplus/).

### Le mot-clé `inline` en C++

Le mot-clé **inline** est utilisé avec des fonctions qui sont développées "en ligne" lors de chaque appel.

Une fonction membre définie dans la définition de classe est considérée comme une fonction inline.

Mais nous pouvons utiliser le mot-clé **inline** pour inliner une fonction membre comme ceci :

```c++
class Random(){
int a;
public:
int display const();
//...
};

inline int Random::display() const{
return a;
}
```

La spécification 'inline' est juste une demande au compilateur d'inliner une fonction. Le compilateur peut ignorer cette demande.

### Le mot-clé `goto` en C++

C++ supporte également le mot-clé **goto**. **goto** est utilisé comme une instruction de saut pour sauter dans et hors d'un bloc. La restriction est que nous ne pouvons pas sauter dans un gestionnaire d'exceptions.

Les instructions **goto** sont utiles pour sortir d'une boucle imbriquée ou de toute instruction de cas de commutateur.

```c++
int main(){

for(int i = 0 ; i < 5 ; i++){
  for(int j = 0 ; j < 5 ; j++{
    if(){//vérifier une condition
    goto here;
    }
  }
}

here:
cout<<"I am here"<<;

}
```

Donc, en gros, nous utilisons goto pour sauter d'un bloc à un autre.

Il est bon d'éviter d'utiliser goto en général, bien qu'il puisse parfois être utile.

## C'est tout !

Ce sont quelques-uns des mots-clés les plus courants en C++. J'espère que vous avez passé un bon moment à lire ceci (pas le pointeur **this** :) )

Bon codage !

Vous pouvez lire mes autres blogs [ici](https://abhilekhblogs.blogspot.com/).