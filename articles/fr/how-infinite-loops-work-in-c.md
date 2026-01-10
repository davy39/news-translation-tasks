---
title: Comment fonctionnent les boucles infinies en C++
subtitle: ''
author: AYUSH MISHRA
co_authors: []
series: null
date: '2025-08-01T22:44:18.097Z'
originalURL: https://freecodecamp.org/news/how-infinite-loops-work-in-c
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754065314765/5c8e45f0-6a43-4f1f-b254-2603b7d37e0c.png
tags:
- name: C++
  slug: cpp
- name: Loops
  slug: loops
- name: while loop
  slug: while-loop
- name: Do while loop
  slug: do-while-loop
- name: for loop
  slug: for-loop
seo_title: Comment fonctionnent les boucles infinies en C++
seo_desc: 'In C++, a loop is a part of code that is executed repetitively until the
  given condition is satisfied. An infinite loop is a loop that runs indefinitely,
  without any condition to exit the loop.

  In this article, we will learn about infinite loops in C...'
---

En C++, une boucle est une partie de code qui est exécutée de manière répétitive jusqu'à ce que la condition donnée soit satisfaite. Une boucle infinie est une boucle qui s'exécute indéfiniment, sans aucune condition pour sortir de la boucle.

Dans cet article, nous allons apprendre les boucles infinies en C++, leurs types et causes, ainsi que leurs applications.

### Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'une boucle infinie en C++ ?](#heading-qu-est-ce-qu-une-boucle-infinie-en-c)

2. [Types de boucles infinies en C++](#heading-types-de-boucles-infinies-en-c)

3. [Causes courantes des boucles infinies accidentelles en C++](#heading-causes-courantes-des-boucles-infinies-accidentelles-en-c)

4. [Applications des boucles infinies en C++](#heading-applications-des-boucles-infinies-en-c)

5. [Utilisation des boucles infinies pour prendre une entrée utilisateur en C++](#heading-utilisation-des-boucles-infinies-pour-prendre-une-entrée-utilisateur-en-c)

6. [Conclusion](#heading-conclusion)

## Qu'est-ce qu'une boucle infinie en C++ ?

Une boucle infinie est toute boucle dans laquelle la condition de la boucle est toujours vraie, conduisant à l'exécution du bloc de code donné un nombre infini de fois. Elles peuvent également être appelées boucles sans fin ou non terminantes, qui s'exécuteront jusqu'à la fin de la vie du programme.

Les boucles infinies sont généralement accidentelles et se produisent en raison d'une erreur du programmeur. Mais elles sont également assez utiles dans différents types d'applications, comme la création d'un programme qui ne se termine pas jusqu'à ce qu'une commande spécifique soit donnée.

## Types de boucles infinies en C++

Il existe plusieurs façons de créer une boucle infinie en C++, en utilisant différentes structures de boucle telles que while, for et do-while. Ici, nous allons explorer chaque méthode et fournir des exemples.

* Boucles While infinies

* Boucles For infinies

* Boucles do-while infinies

### 1. Boucle infinie utilisant While Loop

Il s'agit du type de boucle while le plus populaire en raison de sa simplicité. Vous passez simplement la valeur qui résultera en vrai comme condition de la boucle while.

**Syntaxe :**

```plaintext
while(1)
    ou
while(true)
```

**Exemple de code :**

```cpp
// Exemple de boucle infinie en C++ utilisant for loop
#include <iostream>
using namespace std;

int main() {
    // Boucle infinie utilisant while
    while (true) {
        cout << "Ceci est une boucle infinie." << endl;
    }
    return 0;
}
```

Sortie :

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

...

### Boucle infinie utilisant For Loop

Dans une boucle for, si nous supprimons les conditions d'initialisation, de comparaison et de mise à jour, cela résultera en une boucle infinie.

**Syntaxe :**

```plaintext
for(;;)
```

**Exemple de code :**

```cpp
// Exemple de boucle infinie en C++ utilisant for loop

#include <iostream>
using namespace std;

int main() {
    // Boucle infinie utilisant for loop
    for (;;) {
        cout << "Ceci est une boucle infinie." << endl;
    }
    return 0;
}
```

Sortie :

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

...

### Boucle infinie utilisant do-while Loop

Tout comme les deux autres boucles discutées ci-dessus, nous pouvons également créer une boucle infinie en utilisant une boucle do-while. Bien que cette boucle ne soit pas beaucoup préférée en raison de sa syntaxe plus longue.

**Syntaxe :**

```plaintext
do{
}while(1)
```

**Exemple de code :**

```cpp
// Boucle infinie en C++ utilisant do-while loop

#include <iostream>
using namespace std;

int main() {
   // boucle do-while infinie
    do {
        cout << "Ceci est une boucle infinie." << endl;
    } while (true);
    
    return 0;
}
```

Sortie :

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

...

## Causes courantes des boucles infinies accidentelles en C++

Les boucles infinies peuvent être à la fois intentionnelles et accidentelles. Les boucles infinies accidentelles sont celles qui n'étaient pas intentionnelles de la part du programmeur mais qui sont causées par une erreur dans le programme.

Voici quelques-unes des erreurs qui peuvent causer des boucles infinies dans vos programmes de manière involontaire :

### 1. Instructions de mise à jour manquantes

Les boucles infinies sont causées lorsque vous oubliez d'ajouter une condition de mise à jour à l'intérieur de la boucle, qui mettra fin à la boucle dans le futur. Le programme suivant illustre un tel scénario :

**Exemple de code :**

```cpp
// Boucle infinie causée par une instruction de mise à jour manquante

#include <iostream>
using namespace std;

int main() {
    int i = 3;
    while (i < 5) {
        cout << i <<endl;
        // Mise à jour manquante : i++;
    }
    return 0;
}
```

Sortie :

3

3

3

3

3

3

3

...

Pour corriger le code ci-dessus, nous pouvons ajouter une condition de mise à jour à l'intérieur de la boucle comme ceci :

```cpp
// code corrigé

#include<iostream>
using namespace std ;

int main() {
int i = 3;
while (i < 5) {
    cout << i << endl;
    i++; // ajouter la condition
}

return 0 ; 

}
```

Sortie :

3

4

### Conditions de boucle incorrectes

Les conditions mentionnées à l'intérieur du corps de la boucle sont cruciales pour terminer une boucle. Une condition de boucle incorrecte peut entraîner une boucle infinie. Le programme suivant illustre un tel scénario :

**Exemple de code :**

```cpp
// Boucle infinie causée par des conditions de boucle incorrectes

#include <iostream>
using namespace std;

int main() {
    int i = 2;
    while (i >= 0) {  
        cout << "Bonjour AnshuAyush " << endl;
        
    }
    return 0;
}
```

Sortie :

Bonjour AnshuAyush

Bonjour AnshuAyush

Bonjour AnshuAyush

Bonjour AnshuAyush

Bonjour AnshuAyush

...

Pour corriger le code ci-dessus, nous pouvons mettre à jour `i` à l'intérieur de la boucle pour rendre éventuellement la condition fausse :

```cpp
// code corrigé 

#include<iostream>
using namespace std ;

int main() {
int i = 2;
while (i >= 0) {  
    cout << "Bonjour AnshuAyush" << endl;
    i--; // la boucle s'arrêtera
}

return 0 ; 

}
```

Sortie :

Bonjour AnshuAyush

Bonjour AnshuAyush

Bonjour AnshuAyush

### Erreurs logiques dans la boucle

Dans de nombreux scénarios, les boucles infinies sont causées par de petites erreurs logiques dans le code. Le programme suivant illustre un tel scénario :

**Exemple de code :**

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 3; i >2; i += 2) {  
        cout <<"Ceci est une boucle infinie" << endl;
    }
    return 0;
}
```

Sortie :

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

Ceci est une boucle infinie.

...

Pour corriger le code ci-dessus, nous pouvons soit utiliser une condition décroissante, soit utiliser une condition de boucle incrémentielle.

Condition décroissante :

```cpp
for (int i = 3; i > 0; i--) {
    cout <<"Ceci n'est PAS une boucle infinie" << endl;
}
```

Condition incrémentielle :

```cpp
for (int i = 3; i < 10; i += 2) {
    cout <<"La boucle se terminera lorsque i atteindra 10" << endl;
}
```

## Applications des boucles infinies en C++

Les boucles infinies ne se produisent pas seulement par accident, comme je l'ai mentionné ci-dessus. Vous pouvez également les créer intentionnellement pour différents cas d'utilisation. Voici quelques-unes des applications courantes où vous pourriez utiliser des boucles infinies intentionnellement :

* **Boucles d'événements :** De nombreuses interfaces utilisateur graphiques (GUI) utilisent des boucles infinies pour maintenir le programme en cours d'exécution et réactif aux actions de l'utilisateur.

* **Applications serveur :** Les serveurs web utilisent des boucles infinies pour écouter en continu les connexions ou les requêtes des clients.

* **Systèmes embarqués :** Les systèmes embarqués, tels que les microcontrôleurs, utilisent fréquemment des boucles infinies comme boucles principales de leur programme pour répondre en continu aux événements externes.

* **Entrées utilisateur :** Les boucles infinies sont également utilisées pour attendre des entrées utilisateur valides. La boucle continue de s'exécuter jusqu'à ce qu'une entrée valide soit fournie par l'utilisateur. Nous allons examiner un exemple de cela.

### Utilisation des boucles infinies pour prendre une entrée utilisateur en C++

Les boucles infinies sont couramment utilisées dans des scénarios où un programme doit prendre en continu une entrée utilisateur jusqu'à ce qu'une condition spécifique soit remplie, comme la sortie du programme ou l'obtention d'une entrée utilisateur valide. Le programme suivant démontre comment nous pouvons prendre une entrée utilisateur jusqu'à ce qu'une condition spécifique soit remplie :

**Exemple de code :**

```cpp
// Programme C++ pour prendre une entrée utilisateur en utilisant des boucles infinies

#include <iostream>
#include <string>
using namespace std;

int main() {
    string input;
    
    while (true) {
        cout << "Entrez une commande (tapez 'exit' pour quitter) : ";
        getline(cin, input);

        if (input == "exit") {
        // Sortir de la boucle si l'utilisateur tape 'exit'
            break; 
        }

        cout << "Vous avez entré : " << input << endl;
        // Traiter l'entrée
    }
    cout << "Programme quitté." << endl;
    return 0;
}
```

Sortie :

Entrez une commande (tapez 'exit' pour quitter) : Anshu

Vous avez entré : Anshu

Entrez une commande (tapez 'exit' pour quitter) : Ayush

Vous avez entré : Ayush

Entrez une commande (tapez 'exit' pour quitter) : exit

Programme quitté.

## Conclusion

Les boucles infinies ne sont pas toujours dangereuses. Elles peuvent être très utiles lorsqu'elles sont utilisées avec un contrôle approprié, comme des instructions break ou des vérifications de conditions. Mais si vous les utilisez sans précaution, elles peuvent faire planter votre programme.

Assurez-vous simplement de vérifier vos conditions de boucle et testez votre code en utilisant des instructions d'impression entre les programmes pour découvrir tout comportement inattendu. En somme, les boucles infinies peuvent être très puissantes lorsqu'elles sont manipulées avec soin, mais peuvent être très risquées si elles sont laissées sans contrôle.

Et si vous souhaitez me soutenir directement et mon travail afin que je puisse continuer à créer ces tutoriels, [vous pouvez le faire ici](https://paypal.me/ayushM010). Merci !