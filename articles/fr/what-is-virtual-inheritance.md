---
title: Qu'est-ce que l'héritage virtuel ?
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2023-02-23T21:09:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-virtual-inheritance
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-ruiyang-zhang-3717242.jpg
tags:
- name: C++
  slug: c-2
- name: inheritance
  slug: inheritance
seo_title: Qu'est-ce que l'héritage virtuel ?
seo_desc: "C++ supports the concept of inheritance – that is, a class can inherit\
  \ properties from other classes. \nBut sometimes you might need to use what is commonly\
  \ referred as virtual inheritance. \nIn this article we will discuss when you might\
  \ need to use v..."
---

C++ supporte le concept d'héritage – c'est-à-dire qu'une classe peut hériter de propriétés d'autres classes. 

Mais parfois, vous pourriez avoir besoin d'utiliser ce que l'on appelle communément l'héritage virtuel. 

Dans cet article, nous discuterons de quand vous pourriez avoir besoin d'utiliser l'héritage virtuel et comment le mettre en œuvre en C++.

## Qu'est-ce que l'héritage virtuel ?

En C++, une classe peut hériter de plusieurs classes, ce qui est communément appelé héritage multiple. Mais cela peut parfois causer des problèmes, car vous pouvez avoir plusieurs instances de la classe de base.

Pour résoudre ce problème, C++ utilise une technique qui garantit qu'une seule instance de la classe de base est présente. Cette technique est appelée héritage virtuel.

### Exemple de quand l'héritage virtuel est utile

Regardons un exemple puis expliquons ce qui se passe :

```c++
#include <iostream>

class A {
    public:
     int x = 5;
     // quelques autres choses
};
class B : public A { // héritage de la classe A.
    public:
      int i = 6;
};
class C : public A { // héritage de la classe A.
    public:
      int i = 7;
};
class D : public B, public C { // héritage des classes B et C
    // quelque chose peut aller ici..
};

int main(){
    D obj;
    std::cout << obj.x << std::endl;
    return 0;
}
```

Voyons ce qui se passe ici :

Tout d'abord, nous avons une classe `A` qui est héritée par deux classes `B` et `C`. Ces deux classes sont ensuite héritées par une autre classe `D`.

Dans notre fonction `main`, nous créons une nouvelle instance (objet) de la classe `D`. Nous avons ensuite simplement essayé d'imprimer la valeur de `x` sur la console.

Il peut sembler légitime d'accéder à la valeur de `x` ici, car la classe `D` hérite à la fois de `B` et `C` qui héritent finalement de la classe `A`.

Mais lorsque vous essayez de compiler le programme ci-dessus, vous obtenez l'erreur suivante :

```
<source>: In function 'int main()':
<source>:21:22: error: request for member 'x' is ambiguous
   21 |     std::cout << obj.x << std::endl;
      |                      ^
<source>:5:10: note: candidates are: 'int A::x'
    5 |      int x = 5;
      |          ^
<source>:5:10: note:                 'int A::x'
```

L'erreur est assez claire : **`error:`** `request for member '`**`x`**`' is ambiguous`. Voyons maintenant pourquoi la requête est ambiguë. 

Si nous dessinons la structure hiérarchique des classes, cela devrait devenir assez clair :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/hierarchial-1.png)
_Structure hiérarchique des classes_

Nous pouvons voir que nous avons plusieurs instances de la classe `A`. Ainsi, la requête de la variable `x` devient ambiguë car le compilateur ne sait pas à quelle instance nous faisons référence – est-ce par `B` ou par `C` ? C'est le vrai problème. 

### Une façon de résoudre ce problème

Une façon de résoudre le problème est d'utiliser l'`opérateur de résolution de portée (::)` avec lequel nous pouvons spécifier directement quelle instance de `A` nous voulons.

```c++
int main(){
    D obj;
    std::cout << obj.B::x << std::endl;
    std::cout << obj.C::x << std::endl;
}
```

En utilisant l'`opérateur de résolution de portée`, nous avons explicitement indiqué au compilateur à quelle instance de `A` nous faisions référence.

Le principal problème avec cette approche est qu'elle ne résout pas notre problème – car notre problème principal est d'avoir plusieurs instances de la classe `A`, et nous les avons toujours. Nous devons donc chercher d'autres solutions.

Et l'autre solution est d'utiliser l'héritage virtuel. Voyons comment cela fonctionne maintenant.

### Comment utiliser l'héritage virtuel

Pour hériter virtuellement, nous ajoutons simplement le mot-clé `virtual` avant le nom de notre classe de base dans la déclaration de la classe dérivée comme ceci :

```c++
class B : virtual public A{
    public:
      int i = 6;
};
class C : virtual public A{
    public:
      int i = 7;
};
```

L'ajout du mot-clé `virtual` indique que nous voulons hériter de `A` virtuellement. 

L'héritage virtuel garantit qu'il n'y aura qu'une seule instance de la classe de base parmi les classes dérivées qui l'ont héritée virtuellement. Après les modifications, notre structure hiérarchique de classe devient :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/diamond-1.png)
_La structure hiérarchique après l'héritage virtuel_

Ainsi, si nous essayons de compiler le code suivant, il se compilera avec succès.

```c++
#include <iostream>

class A {
    public:
     int x = 5;
};
class B : virtual public A{
    public:
      int i = 6;
};
class C : virtual public A{
    public:
      int i = 7;
};
class D : public B, public C{
    
};

int main(){
    D obj;
    std::cout << obj.x << std::endl;

}
```

Ainsi, avec l'introduction de l'héritage `virtual`, nous sommes en mesure de supprimer les ambiguïtés que nous avions précédemment.

## Conclusion

Dans cet article, vous avez appris le problème que vous pourriez rencontrer lors de l'héritage d'une classe et une façon de le résoudre en utilisant l'héritage `virtual`.

Bon codage !