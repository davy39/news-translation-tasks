---
title: Tutoriel C++ – Que sont les spécificateurs constexpr et constinit ?
subtitle: ''
author: Jayant Chowdhary
co_authors: []
series: null
date: '2023-12-11T18:50:12.000Z'
originalURL: https://freecodecamp.org/news/cpp-constexpr-and-constinit
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/ConstCover-1.jpg
tags:
- name: C++
  slug: c-2
seo_title: Tutoriel C++ – Que sont les spécificateurs constexpr et constinit ?
seo_desc: "When we write programs, many operations which are performed at runtime\
  \ can actually be done at compile time – that is, baked into code. \nThis improves\
  \ program performance since operations are no longer being computed on the fly,\
  \ during runtime. \nWhil..."
---

Lorsque nous écrivons des programmes, de nombreuses opérations effectuées à l'exécution peuvent en réalité être réalisées à la compilation – c'est-à-dire, intégrées directement dans le code. 

Cela améliore les performances du programme puisque les opérations ne sont plus calculées à la volée, pendant l'exécution. 

Bien que ces techniques de déplacement des opérations à la compilation améliorent les performances, elles peuvent également aider à résoudre des problèmes subtils tels que le 'Static Initialization Order Fiasco' que j'ai abordé dans un [article précédent](https://www.freecodecamp.org/news/cpp-static-initialization-order-fiasco/).  

Ce tutoriel vous enseigne deux façons de réaliser cela en C++. Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequisites)
* [Comment évaluer des fonctions à la compilation en utilisant `constexpr`](#heading-comment-evaluer-des-fonctions-a-la-compilation-en-utilisant-constexpr)
* [Le spécificateur `constinit` et ses utilisations](#heading-le-specificateur-constinit-et-ses-utilisations)
* [Résumé](#heading-resume)

## Prérequis

* Une compréhension basique du C++ : Pour les lecteurs non familiers avec le C++, [Apprendre la programmation C++ pour débutants – Cours gratuit de 31 heures](https://www.freecodecamp.org/news/learn-c-with-free-31-hour-course/) est une ressource utile
* La lecture de mon article précédent [Qu'est-ce que le Static Initialization Order Fiasco en C++](https://www.freecodecamp.org/news/cpp-static-initialization-order-fiasco/) vous sera bénéfique pour comprendre le contexte autour de `constinit`.

## Comment évaluer des fonctions à la compilation en utilisant `constexpr`

Pour comprendre cela, examinons d'abord un exemple de fonction qui effectue un calcul très simple :

```cpp
int add2(int input) {
    return input + 2;
}

int main() {
    int b = add2(3);
    std::cout << "b = " << b;
    return 0;
}

```

Ici, tout ce que fait la fonction `add2()` est d'ajouter 2 à l'entrée. Dans `main()`, `add2()` a été appelée avec l'entrée `2`. Il est donc assez simple pour quiconque regardant le programme de dire quel sera le résultat de la fonction : 5. Il n'y a aucune sorte de non-déterminisme ici. 

Mais si nous regardons le code assembleur x86 généré par le compilateur, il ressemblerait à ceci :

```
add2(int):
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], edi
        mov     eax, DWORD PTR [rbp-4]
        add     eax, 2
        pop     rbp
        ret
.LC0:
        .string "b = "
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     edi, 3
        // Fonction add2() appelée
        call    add2(int)
        mov     DWORD PTR [rbp-4], eax
        mov     esi, OFFSET FLAT:.LC0
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     rdx, rax
        mov     eax, DWORD PTR [rbp-4]
        mov     esi, eax
        mov     rdi, rdx
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(int)
        mov     eax, 0
        leave
        ret

```

(Notez que les codes assembleurs de référence dans cet article ont été générés en utilisant l'outil Compiler Explorer sur [godbolt.org](https://godbolt.org/).)

La fonction `add2()` est effectivement appelée à l'exécution dans `main()` avec la ligne `call add2(int)`. 

Puisque cette fonction fait quelque chose qui peut être entièrement calculé avant que le programme ne s'exécute (2+3 = 5, même dans nos têtes !), ne serait-il pas génial si nous pouvions faire en sorte que le compilateur ne crée pas de fonction pour cette opération et insère directement la réponse dans le code assembleur ? C'est exactement ce que fait `constexpr`. 

Si le code était modifié comme suit :

```cpp
constexpr int add2(int input) {
    return input +2;
}

int main() {
    int b = add2(3);
    std::cout << "b = " << b;
    return 0;
}

```

le compilateur générerait le code assembleur suivant :

```
.LC0:
        .string "b = "
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     DWORD PTR [rbp-4], 5
        mov     esi, OFFSET FLAT:.LC0
        mov     edi, OFFSET FLAT:_ZSt4cout
        call    std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*)
        mov     rdx, rax
        mov     eax, DWORD PTR [rbp-4]
        mov     esi, eax
        mov     rdi, rdx
        call    std::basic_ostream<char, std::char_traits<char> >::operator<<(int)
        mov     eax, 0
        leave
        ret

```

La fonction `add2()` a disparu et la ligne `mov DWORD PTR [rbp-4], 5` a intégré dans le programme l'évaluation de la fonction `add2()` à la compilation. Il n'y a pas d'appel à l'exécution de `add2()`. 

Notez que cela est possible puisque nous avons passé 3 – une expression connue à la compilation – à la fonction `add2()`. Si quelque chose qui ne pouvait pas être évalué à la compilation était passé, le compilateur générerait à nouveau une fonction `add2()`. 

Vous pouvez voir ce que je veux dire dans cet extrait :

```cpp
#include<iostream>
#include <random>

constexpr int add2(int input) {
    return input +2;
}

int main() {
    int rd = std::rand();
    int b = add2(rd);
    std::cout << "b = " << b;
    return 0;
}

```

L'assembleur généré contient à nouveau la fonction `add2()` :

```
add2(int):
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], edi
        mov     eax, DWORD PTR [rbp-4]
        add     eax, 2
        pop     rbp
        ret
.LC0:
        .string "b = "
main:
        push    rbp
// Snip
```

D'accord, vous avez maintenant vu comment l'utilisation du spécificateur `constexpr` peut aider les programmes à déplacer les coûts d'exécution vers les coûts de compilation dans de nombreux cas. 

Examinons maintenant un autre spécificateur introduit récemment, en C++20, qui vérifie que les variables sont initialisées à la compilation.

## Le spécificateur `constinit` et ses utilisations

Le spécificateur [`constinit`](https://en.cppreference.com/w/cpp/language/constant_initialization) a été introduit en C++ 20. Ce spécificateur _affirme_ qu'une variable a une initialisation constante – il [définit les valeurs initiales des variables statiques à une constante de compilation](https://en.cppreference.com/w/cpp/language/constant_initialization). Sinon, le programme est mal formé et le compilateur produit une erreur. Par exemple :

```cpp
int add2(int v) {
    return v + 2;
}

//Erreur : la variable 'constinit' 'glob' n'a pas d'initialiseur constant  
constinit int glob = add2(2);

int main() {

    return 0;
}

```

Le compilateur génère une erreur ici puisque la fonction `add2()` n'est pas _certaine_ d'avoir une initialisation constante – ce qui peut être déterminé à la compilation. Maintenant, si la fonction `add2()` est marquée `constexpr`, elle aura une initialisation constante, donc le code compile.

```cpp
constexpr int add2(int v) {
    return v + 2;
}

//OKAY la variable 'constinit' 'glob' a bien un initialiseur constant.  
constinit int glob = add2(2);

int main() {

    return 0;
}

```

Maintenant, vous pourriez demander – quelle est vraiment l'utilité de ce spécificateur ?

La réponse est qu'il peut être utilisé dans certains cas pour résoudre le 'Static Initialization Order Fiasco'. 

J'ai parlé du 'Static Initialization Order Fiasco' dans un [article précédent](https://www.freecodecamp.org/news/cpp-static-initialization-order-fiasco/). Si nous utilisons `constinit`, le compilateur donne au programmeur sa garantie que la variable `constinit` sera initialisée de manière constante – c'est-à-dire avant que toute autre variable statique ne soit construite à l'exécution. Nous nous débarrassons du 'Static Initialization / Destruction Order Fiasco'. 

Un autre exemple où nous utilisons des chaînes qui sont initialisées de manière constante illustre cela :

```cpp
// Parent.h
#pragma once
class Parent {
    public:
       size_t getMoneyCount();
       constexpr Parent(const char *moneyString): mData(moneyString) {};
    private:
        std::string_view mData;     
};
extern Parent everyonesParent;

// Parent.cpp
#include<Producer.h>

constinit static Parent everyonesParent("TheParent");

size_t Parent::getMoneyCount() {
    return mData.size();
}

//Child.cpp
#include<Child.h>

class Child {
    public:
    Child(Parent &parent) : mMoneyCount(parent.getMoneyCount()) {};
    private:
    size_t mMoneyCount;
};

static Child everyonesChild(everyonesParent);

```

Il n'y a pas de problème d'ordre d'initialisation statique ici, puisque l'objet statique `everyonesParent` est garanti d'être initialisé avant `everyonesChild`, car il a été marqué `constinit`. 

Il était acceptable de marquer `everyonesParent` `constinit` puisqu'il utilisait `std::string_view` qui peut être initialisé de manière constante – contrairement à `std::string`. De plus, il avait un constructeur `constexpr`. Si cela n'avait pas utilisé l'un ou l'autre, la compilation aurait échoué !

Pour conclure, quelque chose à noter à propos de `constinit` : `constinit` n'implique pas `const`.

Les valeurs `constinit` peuvent être modifiées après la construction. Prenons cet exemple – il est parfaitement légal :

```cpp
#include<iostream>

constinit int i = 42;
int main() {
 i++;
 std::cout << " i est " << i << "\n";
}

```

## Résumé

Cet article a couvert les opérations à la compilation et les opérations à l'exécution. Il a analysé comment les compilateurs produisent du code pour générer des fonctions utilisées à l'exécution ou les évaluer à la compilation. 

Vous avez appris les spécificateurs `constexpr` et `constinit` en C++, et comment ils sont extrêmement utiles.

J'espère que vous avez apprécié l'article !