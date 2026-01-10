---
title: C++ Vector – Modèle STD Vector en CPP avec Exemple de Code
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-01T21:27:30.000Z'
originalURL: https://freecodecamp.org/news/c-vector-std-pattern-vector-in-cpp-with-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/christin-hume-mfB1B1s4sMc-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: C++
  slug: c-2
seo_title: C++ Vector – Modèle STD Vector en CPP avec Exemple de Code
seo_desc: 'Vectors in C++ are a helpful way to store dynamic data. They also help
  you avoid having to deal with the not so flexible arrays that are inherited from
  the C programming language.

  This article is a beginner friendly introduction to vectors. It will s...'
---

Les vecteurs en C++ sont une manière utile de stocker des données dynamiques. Ils vous aident également à éviter de devoir gérer les tableaux peu flexibles hérités du langage de programmation C.

Cet article est une introduction conviviale pour les débutants aux vecteurs. Il vous montrera certaines de leurs fonctionnalités de base et essentielles pour vous aider à commencer votre apprentissage.


## Qu'est-ce qu'un Vector en C++ ?

Les programmes ont besoin de groupes de données pour pouvoir faire à peu près n'importe quoi.

Ces données pourraient être une liste de livres que vous avez lus tout au long de l'année, ou des options de paiement pour des repas dans un restaurant, ou simplement une liste de noms - les données peuvent être de n'importe quel type.

Mais comment stockez-vous ces groupes de données ?

Les vecteurs en C++ sont un moyen simple et efficace de stocker des données et de les garder organisées.

Les vecteurs, ou `std::vector`, sont une classe de modèle dans la STL (Standard Template Library). Mais que signifie cela ?

Ils sont un remplacement plus flexible, raffiné et efficace pour les tableaux, qui sont utilisés dans le langage de programmation C (et sur lequel le langage C++ est basé).

Contrairement aux tableaux en C qui ont une taille statique, rigide et fixe, les vecteurs sont des conteneurs séquencés qui stockent des collections dynamiques d'éléments de données. La taille du conteneur n'est pas fixée - au lieu de cela, elle grandit et diminue dynamiquement.


## Pourquoi et quand utiliser un Vector en C++

Envisagez d'utiliser des vecteurs lorsque vous travaillez avec des données en constante évolution.

Si vous trouvez que vous ajoutez ou supprimez souvent des données, alors les vecteurs sont la manière préférée de gérer ces éléments dynamiques, car ils sont capables de redimensionner automatiquement.

Comme mentionné précédemment, les vecteurs n'ont pas une taille fixe, ce qui les rend idéaux à utiliser lorsque vous ne connaissez pas la taille de vos données à l'avance et lorsque vos données ne sont pas établies à l'avance.

La taille des conteneurs peut changer, donc vous n'avez pas besoin de spécifier leur taille maximale dès le début.

## Comment créer des vecteurs en C++

Pour créer un vecteur en C++, vous devez d'abord inclure la bibliothèque vector.

Vous faites cela en ajoutant la ligne `#include <vector>` en haut de votre fichier. Cette ligne vient après la ligne `#include <iostream>` et tout autre fichier d'en-tête que vous avez inclus dans votre programme.

Le `std::vector` est inclus dans la bibliothèque `#include <vector>`.

La syntaxe générale pour créer un vecteur ressemble à ceci :

```
std::vector<data_type> name (items);
```

Décomposons cela :

- Vous commencez avec le mot-clé `std::vector`.
- `<data_type>` spécifie le type de données que le vecteur stockera, et est entouré de chevrons ouvrants et fermants, `<>`. Certains exemples de types de données qui peuvent être stockés sont : `<string>`, `<int>`, `double` et `char`. Notez que le type du vecteur ne peut pas être changé une fois qu'il a été déclaré.
- Ensuite vient le nom que vous voulez donner au vecteur. Définir le type de données et donner un nom au vecteur sont des étapes obligatoires.
- Optionnellement, vous pouvez spécifier le nombre d'éléments que le vecteur contiendra. Cela définira la taille du vecteur. Cela s'avère utile lorsque vous ne connaissez pas les valeurs spécifiques des éléments que le vecteur contiendra dès le début, mais que vous connaissez la taille.
- Enfin, n'oubliez pas de terminer l'instruction par un point-virgule, `;`.

Par exemple :

```cpp
#include <iostream>
#include <vector>

int main() {
//sans spécifier le nombre d'éléments

//définir un vecteur nommé prices qui stocke des nombres à virgule flottante
std::vector<double> prices;
}
```

```cpp
#include <iostream>
#include <vector>

int main() {
//en spécifiant le nombre d'éléments

//crée un vecteur nommé prices
//il contiendra des nombres à virgule flottante
//la taille initiale du vecteur est définie à 10
std::vector<double> prices (10);
}
```

Vous n'avez pas besoin de préfixer `std::` lorsque vous utilisez `using namespace std;` en haut de votre fichier (après les fichiers d'en-tête), comme ceci :

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
vector<double> prices;
}
```

## Comment trouver la taille des vecteurs en C++

La fonction `.size()` retournera le nombre d'éléments contenus dans un vecteur.

Vous avez vu précédemment comment créer un vecteur, qui était vide.

Pour double vérifier, vous feriez :

```cpp
#include <iostream>
#include <vector>

int main() {
std::vector<double> prices;

//retourne la taille
std::cout << prices.size() << std::endl;

//affiche 0
}
```

## Comment ajouter des éléments aux vecteurs en C++

Les vecteurs sont des conteneurs dynamiques d'éléments et leur taille peut croître tout au long de la vie d'un programme, en fonction de ses besoins.

Pour ajouter des éléments un par un à la **fin** d'un vecteur, vous utilisez la méthode `.push_back()`.

L'élément que vous voulez ajouter va à l'intérieur des parenthèses.

```cpp
#include <iostream>
#include <vector>


int main() {
std::vector <std::string> names;

//ajouter des éléments au vecteur en utilisant .push_back()

names.push_back("Dionysia");
names.push_back("Dimitra");
names.push_back("George");

}
```

## Comment supprimer un élément d'un vecteur en C++

Outre l'ajout d'éléments à un vecteur, vous pouvez également les supprimer.

La fonction `.pop_back()` supprimera le **dernier** élément du vecteur.

Comparée à la méthode `.push_back()` qui est utilisée pour ajouter des éléments, la fonction `.pop_back()` ne prend aucun argument.

```cpp
#include <iostream>
#include <vector>


int main() {
std::vector <std::string> names;

//ajouter des éléments au vecteur en utilisant .push_back()

names.push_back("Dionysia");
names.push_back("Dimitra");
names.push_back("George");

//vérifier la taille
std::cout << names.size() << std::endl; //affiche 3

//supprimer le dernier élément
names.pop_back();

//vérifier la taille à nouveau
std::cout << names.size() << std::endl; //affiche 2
}
```

## Indexation dans les Vecteurs

Comme mentionné précédemment, les vecteurs sont des conteneurs d'éléments séquentiels, ce qui signifie que chaque élément individuel peut être accessible par son index.

L'indexation dans les vecteurs commence à `0` – le premier élément d'un vecteur a un index de `0`, le deuxième élément a un index de `1`, et ainsi de suite.

Vous pouvez ajouter des éléments individuellement en spécifiant la position à laquelle vous voulez les ajouter.

Ainsi, vous pourriez réécrire l'exemple précédent comme suit :

```cpp
#include <iostream>
#include <vector>


int main() {
std::vector <std::string> names;

names[0] = "Dionysia"; // ajoute la chaîne à la 1ère place
names[1] = "Dimitra";  // ajoute la chaîne à la 2ème place
names[2] = "George";   // ajoute la chaîne à la troisième place
}
```

Pour accéder à un élément et afficher chaque élément individuel, vous mentionnez le nom du vecteur et la position de l'élément souhaité entre crochets.

```cpp
#include <iostream>
#include <vector>


int main() {
std::vector<std::string> names;

names[0] = "Dionysia"; 
names[1] = "Dimitra";  
names[2] = "George";   

//afficher chaque élément dans la console :
std::cout << names[0] << std::endl; //affiche 'Dionysia'
std::cout << names[1] << std::endl; //affiche 'Dimitra'
std::cout << names[2] << std::endl; //affiche 'George'
}
```

## Conclusion

Et voilà - vous connaissez maintenant les bases des vecteurs en C++.

Si vous êtes intéressé à en apprendre davantage sur le C++, regardez le [C++ Tutorial For Beginners](https://www.youtube.com/watch?v=vLnPwxZdW4Y&t=3457s) sur la chaîne YouTube de freeCodeCamp.

Merci d'avoir lu et bon codage :)