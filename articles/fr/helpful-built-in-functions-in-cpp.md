---
title: Fonctions intégrées utiles en C++ que tous les développeurs devraient connaître
subtitle: ''
author: AYUSH MISHRA
co_authors: []
series: null
date: '2025-07-22T17:24:12.694Z'
originalURL: https://freecodecamp.org/news/helpful-built-in-functions-in-cpp
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1753105870543/7bdb3c7e-873b-46a2-bdbd-0d881aacedfc.png
tags:
- name: C++
  slug: cpp
- name: Functional Programming
  slug: functional-programming
seo_title: Fonctions intégrées utiles en C++ que tous les développeurs devraient connaître
seo_desc: 'Built-in functions in C++ are those functions that are part of the C++
  standard libraries. These functions are designed to provide common and essential
  functionality that is often required in programming.

  In this article, we will look at some of the ...'
---

Les fonctions intégrées en C++ sont celles qui font partie des bibliothèques standard de C++. Ces fonctions sont conçues pour fournir des fonctionnalités courantes et essentielles souvent requises en programmation.

Dans cet article, nous examinerons certaines des fonctions intégrées les plus couramment utilisées en C++ afin que vous puissiez commencer à les utiliser dans votre code.

### Ce que nous allons couvrir :

1. [La fonction `sqrt()`](#heading-la-fonction-sqrt)
    
2. [La fonction `pow()`](#heading-la-fonction-pow)
    
3. [La fonction `sort()`](#heading-la-fonction-sort)
    
4. [La fonction `find()`](#heading-la-fonction-find)
    
5. [La fonction `binary_search()`](#heading-la-fonction-binary_search)
    
6. [La fonction `max()`](#heading-la-fonction-max)
    
7. [La fonction `min()`](#heading-la-fonction-min)
    
8. [La fonction `swap()`](#heading-la-fonction-swap)
    
9. [La fonction `toupper()`](#heading-la-fonction-toupper)
    
10. [La fonction `tolower()`](#heading-la-fonction-tolower)
    

## La fonction `sqrt()`

Vous utilisez la fonction `sqrt()` pour déterminer la racine carrée de la valeur de type double. Elle est définie dans le fichier d'en-tête `<cmath>`.

### **Syntaxe :**

```plaintext
sqrt (n)
```

**Paramètre :** Cette fonction prend un seul paramètre de type double qui est un nombre dont nous voulons trouver la racine carrée.

**Type de retour :** La racine carrée de la valeur de type double.

### Exemple de code

Regardons un exemple pour voir comment cette fonction fonctionne :

```cpp
// Programme C++ pour voir l'utilisation de la fonction sqrt()
#include <cmath>     
#include <iostream>  

using namespace std;  
int main()
{
    double x = 100;

    double answer;

    // Utilisez la fonction sqrt() pour calculer la racine carrée du nombre
    answer = sqrt(x);

    // Affichez le résultat 
    cout << answer << endl;

    return 0;
}
```

Sortie :

10

## **La** fonction `pow()`

Vous utilisez la fonction `pow()` pour trouver la valeur du nombre donné élevé à une certaine puissance. Cette fonction est également définie dans le fichier d'en-tête `<cmath>`.

### **Syntaxe :**

```plaintext
double pow(double x, double y);
```

**Paramètres :**

* **x :** Le nombre de base.
    
* **y :** La puissance exponentielle.
    

**Type de retour :** valeur de **x** élevée à la puissance **y**.

### Exemple de code :

Regardons un exemple pour voir comment cela fonctionne :

```cpp
// Programme C++ pour voir l'utilisation de la fonction pow()
#include <cmath>
#include <iostream>
using namespace std;

int main()
{
 // Déclare une variable entière 'base' 
    int base = 5;

// Déclare une variable entière 'exponent' 
    int exponent = 3;

// pow(5, 3) signifie 5^3 qui est 5*5*5 = 125
// Utilisez la fonction pow() pour calculer la base élevée à la puissance de l'exposant
    int answer = pow(base, exponent);

// affiche le résultat
    cout << answer << endl;
}
```

Sortie :

125

## La fonction `sort()`

La fonction `sort()` fait partie de l'en-tête `<algorithm>` de la STL. Il s'agit d'un modèle de fonction que vous pouvez utiliser pour trier les conteneurs à accès aléatoire, tels que les vecteurs, les tableaux, etc.

### Syntaxe :

```plaintext
sort (arr , arr + n, comparator)
```

**Paramètres :**

* **arr :** Le pointeur ou l'itérateur vers le premier élément du tableau.
    
* **arr + n :** Le pointeur vers l'élément imaginaire suivant le dernier élément du tableau.
    
* **comparator :** La fonction prédicat unaire utilisée pour trier la valeur dans un ordre spécifique. La valeur par défaut de celle-ci trie le tableau par ordre croissant.
    

**Valeur de retour :** Cette fonction ne retourne aucune valeur.

### Exemple de code :

Regardons un exemple :

```cpp
#include <iostream>     
#include <algorithm>    // Fichier d'en-tête qui inclut la fonction sort()

using namespace std;    

int main()
{
    // Déclare et initialise un tableau d'entiers avec des éléments non triés
    int arr[] = { 13, 15, 12, 14, 11, 16, 18, 17 };

    // Calcule le nombre d'éléments dans le tableau
    int n = sizeof(arr) / sizeof(arr[0]);

    // Utilise la fonction intégrée sort() de la bibliothèque algorithm
    sort(arr, arr + n);

    // Affiche le tableau trié en utilisant une boucle
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";  
    
    return 0;
}
```

Sortie :

11 12 13 14 15 16 17 18

## La fonction `find()`

La fonction `find()` fait également partie de la bibliothèque `<algorithm>` de la STL. Vous utilisez cette fonction pour trouver une valeur dans la plage donnée. Vous pouvez l'utiliser avec des ensembles de données triés et non triés car elle implémente un algorithme de recherche linéaire.

### **Syntaxe :**

```plaintext
find(startIterator, endIterator, key)
```

**Paramètres :**

* **startIterator :** Itère au début de la plage.
    
* **endIterator :** Itère à la fin de la plage.
    
* **key :** La valeur à rechercher.
    

**Valeur de retour :** Si l'élément est trouvé, alors l'itérateur est défini sur l'élément. Sinon, il itère à la fin.

### Exemple de code :

Regardons un exemple pour mieux comprendre comment cela fonctionne :

```cpp
// Programme C++ pour voir l'utilisation de la fonction find()

#include <algorithm>   // Requis pour la fonction find()
#include <iostream>    
#include <vector>      

using namespace std;   

int main()
{
    // Initialise un vecteur 
    vector<int> dataset{ 12, 28, 16, 7, 33, 43 };

    // Utilise la fonction find() pour rechercher la valeur 7
    auto index = find(dataset.begin(), dataset.end(), 7);

    // Vérifie si l'élément a été trouvé
    if (index != dataset.end()) {
        // Si trouvé, affiche la position (index) en soustrayant l'itérateur de début
        cout << "L'élément est trouvé à l'index "
             << index - dataset.begin() << "nd index";
    }
    else {
        // Si non trouvé
        cout << "Élément non trouvé";
   }
    return 0;
}
```

Sortie :

L'élément est trouvé à l'index 3

## La fonction `binary_search()`

La fonction `binary_search()` est également utilisée pour trouver un élément dans la plage – mais cette fonction implémente une recherche binaire au lieu d'une recherche linéaire comme c'est le cas pour la fonction `find()`. Elle est également plus rapide que la fonction `find()`, mais vous ne pouvez l'utiliser que sur des ensembles de données triés avec un accès aléatoire. Elle est définie dans le fichier d'en-tête `<algorithm>`.

### **Syntaxe :**

```plaintext
binary_search (starting_pointer , ending_pointer , target);
```

**Paramètres :**

* **starting\_pointer :** Pointeur vers le début de la plage.
    
* **ending\_pointer :** Pointeur vers l'élément après la fin de la plage.
    
* **target :** Valeur à rechercher dans l'ensemble de données.
    

**Valeur de retour :**

* Retourne vrai si la cible est trouvée.
    
* Sinon retourne faux.
    

### Exemple de code :

Regardons un exemple pour voir comment cela fonctionne :

```cpp
// Programme C++ pour la fonction binary_search()

#include <algorithm>   
#include <iostream>    
#include <vector>      

using namespace std;   

int main()
{
    // Initialise un vecteur trié d'entiers
    vector<int> arr = { 56, 57, 58, 59, 60, 61, 62 };

    // binary_search() fonctionne uniquement sur des conteneurs triés
    if (binary_search(arr.begin(), arr.end(), 62)) {
        // Si trouvé, affiche que l'élément est présent
        cout << 62 << " est présent dans le vecteur.";
    }
    else {
        // Si non trouvé, affiche que l'élément n'est pas présent
        cout << 16 << " n'est pas présent dans le vecteur";
    }

    cout << endl;
}
```

Sortie :

62 est présent dans le vecteur.

## La fonction `max()`

Vous pouvez utiliser la fonction `std::max()` pour comparer deux nombres et trouver le plus grand entre eux. Elle est également définie dans le fichier d'en-tête `<algorithm>`.

### Syntaxe :

```plaintext
max (a , b)
```

**Paramètres :**

* **a :** Premier nombre
    
* **b :** Deuxième nombre
    

**Valeur de retour :**

* Cette fonction retourne le plus grand nombre entre les deux nombres **a** et **b.**
    
* Si les deux nombres sont égaux, elle retourne le premier nombre.
    

### Exemple de code :

Voici un exemple :

```cpp
// fonction max()

#include <algorithm>  
#include <iostream>   
using namespace std;

int main()
{
    // Déclare deux variables entières
    int a = 8 ;
    int b = 10 ;

    // Utilise la fonction max() pour trouver le plus grand nombre entre a et b
    int maximum = max(a, b);

    // Affiche le résultat avec un message significatif
    cout << "Le maximum de " << a << " et " << b << " est : " << maximum << endl;

    return 0;
}
```

Sortie :

Le maximum de 8 et 10 est : 10

## La fonction `min()`

Vous pouvez utiliser la fonction `std::min()` pour comparer deux nombres et trouver le plus petit des deux. Elle est également définie dans le fichier d'en-tête `<algorithm>`.

### Syntaxe :

```plaintext
min (a , b)
```

**Paramètres :**

* **a :** Premier nombre
    
* **b :** Deuxième nombre
    

**Valeur de retour :**

* Cette fonction retourne le plus petit nombre entre les deux nombres **a** et **b.**
    
* Si les deux nombres sont égaux, elle retourne le premier nombre.
    

### Exemple de code :

Voici un exemple :

```cpp
// utilisation de la fonction min()

#include <algorithm>  // Pour la fonction intégrée min()
#include <iostream>   
using namespace std;

int main()
{
    // Déclare deux variables entières pour stocker l'entrée de l'utilisateur
    int a = 4 ;
    int b = 8 ;

    // Utilise la fonction min() pour trouver le plus petit 
    int smallest = min(a, b);

    // Affiche le résultat 
    cout << "Le plus petit nombre entre " << a << " et " << b << " est : " << smallest << endl;

    return 0;
}
```

Sortie :

Le plus petit nombre entre 4 et 8 est : 4

## La fonction `swap()`

La fonction `std::swap()` vous permet d'échanger deux valeurs. Elle est définie dans le fichier d'en-tête `<algorithm>`.

### **Syntaxe :**

```plaintext
swap(a , b);
```

**Paramètres :**

* **a :** Premier nombre
    
* **b :** Deuxième nombre
    

**Valeur de retour :** Cette fonction ne retourne aucune valeur.

### Exemple :

Voici comment cela fonctionne :

```cpp
//  utilisation de la fonction swap()

#include <algorithm>  // Pour la fonction intégrée swap()
#include <iostream>   
using namespace std;

int main()
{
    int firstNumber = 8 ;
    int secondNumber = 9 ;

    
    // Utilise la fonction intégrée swap() pour échanger les valeurs
    swap(firstNumber, secondNumber);

    // Affiche les valeurs après l'échange
    cout << "Après l'échange :" << endl;
    cout << firstNumber << " " << secondNumber << endl;

    return 0;
}
```

Sortie :

Après l'échange :

9 8

## La fonction `tolower()`

Vous pouvez utiliser la fonction `tolower()` pour convertir un caractère alphabétique donné en minuscule. Elle est définie dans l'en-tête `<cctype>`.

### Syntaxe :

```plaintext
tolower (c);
```

**Paramètre(s) :**

* **c :** Le caractère à convertir.
    

**Valeur de retour :**

* Minuscule du caractère c.
    
* Retourne c si c n'est pas une lettre.
    

### Exemple de code :

Voici comment cela fonctionne :

```cpp
// Programme C++

// utilisation de la fonction tolower()

#include <cctype>     
#include <iostream>   
using namespace std;

int main()
{
    // Déclare et initialise une chaîne avec des caractères en majuscules
    string str = "FRECODECAMP";

    for (auto& a : str) {
        a = tolower(a);
    }

    // Affiche la chaîne modifiée 
    cout << str;

    return 0;
}
```

Sortie :

freecodecamp

## La fonction `toupper()`

Vous pouvez utiliser la fonction `toupper()` pour convertir le caractère alphabétique donné en majuscule. Elle est définie dans l'en-tête `<cctype>`.

### Syntaxe :

```plaintext
toupper (c);
```

**Paramètres :**

* **c :** Le caractère à convertir.
    

**Valeur de retour**

* Majuscule du caractère c.
    
* Retourne c si c n'est pas une lettre.
    

### Exemple de code :

Voici comment cela fonctionne :

```cpp
// utilisation de la fonction toupper()

#include <cctype>     
#include <iostream>   
using namespace std;

int main()
{
    // Déclare et initialise une chaîne 
    string str = "freecodecamp";

    for (auto& a : str) {
        a = toupper(a);
    }

    // Affiche la chaîne convertie en majuscules
    cout << str;

    return 0;
}
```

Sortie :

FREECODECAMP

## Conclusion

Les fonctions intégrées sont des outils utiles en programmation compétitive et dans les tâches de programmation courantes. Elles aident à améliorer la lisibilité du code et à renforcer l'efficacité du code. Dans l'article ci-dessus, nous avons discuté de certaines fonctions intégrées courantes très utiles. Certaines fonctions intégrées courantes sont `max()`, `min()`, `sort()`, et `sqrt()`, etc. En utilisant ces bibliothèques intégrées, nous pouvons réduire le code boilerplate et accélérer le processus de développement logiciel. Elles aident à écrire des programmes C++ plus concis, fiables et maintenables.

Et si vous souhaitez me soutenir et mon travail directement afin que je puisse continuer à créer ces tutoriels, [vous pouvez le faire ici](https://paypal.me/ayushM010). Merci !