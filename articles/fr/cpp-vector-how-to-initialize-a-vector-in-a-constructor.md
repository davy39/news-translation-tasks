---
title: C++ Vector – Comment initialiser un vecteur dans un constructeur en C++
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-27T20:08:33.000Z'
originalURL: https://freecodecamp.org/news/cpp-vector-how-to-initialize-a-vector-in-a-constructor
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/uday-awal-UjJWhMerJx0-unsplash--2-.jpg
tags:
- name: C++
  slug: c-2
seo_title: C++ Vector – Comment initialiser un vecteur dans un constructeur en C++
seo_desc: "When you're working with a collection of variables or data in programming,\
  \ you usually store them in specific data types. \nIn C++, you can store them in\
  \ arrays, structures, vectors, strings and so on. While these data structures have\
  \ their distinctiv..."
---

Lorsque vous travaillez avec une collection de variables ou de données en programmation, vous les stockez généralement dans des types de données spécifiques.

En C++, vous pouvez les stocker dans des tableaux, des structures, des vecteurs, des chaînes de caractères, etc. Bien que ces structures de données aient leurs propres caractéristiques distinctives, nous nous concentrerons principalement sur les différentes méthodes d'initialisation des vecteurs.

Avant cela, parlons brièvement des vecteurs et de ce qui les rend particuliers lors de la manipulation de collections de données en C++.

## Qu'est-ce qu'un vecteur en C++ ?

Contrairement aux tableaux en C++ où la mémoire allouée à la collection est statique, les vecteurs nous permettent de créer des structures de données plus dynamiques.

Voici un tableau en C++ :

```c++
#include <iostream>
using namespace std;

int main() {
    string names[2] = {"Jane", "John"};
    cout << names[1];
    // John
}
```

Le tableau dans le code ci-dessus a été créé et alloué avec suffisamment d'espace pour contenir seulement deux éléments. Tentative d'assigner de nouvelles valeurs via un nouvel index lancerait une erreur.

Avec les vecteurs, les choses sont un peu différentes. Nous n'avons pas à spécifier la capacité du vecteur lorsqu'il est défini. Sous le capot, la mémoire allouée du vecteur change à mesure que la taille du vecteur change.

## Syntaxe pour les vecteurs en C++

Déclarer un `vector` est différent de l'initialiser. Déclarer un `vector` signifie créer un nouveau `vector` tandis que l'initialisation implique de passer des éléments dans le `vector`.

Voici à quoi ressemble la syntaxe :

```txt
vector <data_type> vector_name
```

Chaque nouveau `vector` doit être déclaré en commençant par le mot-clé **vector**. Cela est suivi de crochets angulaires qui contiennent le type de données que le vecteur peut accepter comme des chaînes de caractères, des entiers, etc. Enfin, le nom du vecteur - nous pouvons l'appeler comme nous le souhaitons.

Notez que vous devez mettre `include <vector>` en haut de votre fichier pour pouvoir utiliser les vecteurs.

## Comment initialiser un vecteur en C++

Dans cette section, nous allons passer en revue les différentes façons d'initialiser un `vector` en C++. Nous les diviserons en sous-sections avec quelques exemples pour chaque sous-section.

Commençons par le plus basique.

### Comment initialiser un vecteur en C++ en utilisant la méthode `push_back()`

`push_back()` est l'une des nombreuses méthodes que vous pouvez utiliser pour interagir avec les vecteurs en C++. Elle prend le nouvel élément à passer en tant que paramètre. Cela nous permet de pousser de nouveaux éléments au dernier index d'un `vector`.

Voici un exemple :

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> myVector;

	myVector.push_back(5);
	myVector.push_back(10);
	myVector.push_back(15);

	for (int x : myVector)
		cout << x << " ";
		// 5 10 15 
}

```

Dans le code ci-dessus, nous avons créé un `vector` vide : `vector<int> myVector;`.

En utilisant `push_back()`, nous avons passé trois nouveaux nombres dans le `vector`.

Nous avons ensuite parcouru ces nouveaux nombres et les avons affichés dans la console.

### Comment initialiser un vecteur lors de la déclaration du vecteur en C++

Tout comme les tableaux, nous pouvons assigner des valeurs à un vecteur lorsqu'il est déclaré.

Voici un exemple :

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> myVector{ 5, 10, 15 };

	for (int x : myVector)
		cout << x << " ";
		// 5 10 15 
}

```

Dans cet exemple, la déclaration et l'initialisation ont été faites en même temps.

Au moment de déclarer le `vector`, nous avons passé trois nombres puis nous les avons parcourus et affichés.

Vous remarquerez que j'ai mis `int` entre les crochets angulaires. Cela est pour montrer que les données que le `vector` contiendra sont spécifiquement des entiers.

### Comment initialiser un vecteur à partir d'un tableau en C++

Dans cette section, nous allons d'abord créer et initialiser un tableau. Ensuite, nous allons copier tous les éléments du tableau dans notre vecteur en utilisant deux méthodes de vecteur – `begin()` et `end()`.

Voyons comment cela fonctionne.

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int myArray[] = { 5, 10, 15 };
    
    vector<int> myVector(begin(myArray), end(myArray));


	for (int x : myVector)
		cout << x << " ";
		// 5 10 15 
}

```

Nous pouvons également initialiser un `vector` à partir d'un autre vecteur en utilisant les mêmes méthodes ci-dessus. Vous devrez définir le premier `vector` puis utiliser les méthodes `begin()` et `end()` pour copier ses valeurs dans le second `vector`.

### Comment initialiser un vecteur en spécifiant la taille et la valeur en C++

Nous pouvons spécifier la taille et les éléments d'un `vector` lors de sa déclaration. Cela est principalement dans des situations où le `vector` est requis d'avoir une valeur spécifique tout au long.

Voici un exemple :

```c++
#include <iostream>
#include <vector>
using namespace std;

int main() {

  int num_of_items = 5; 
  
  vector<int> myVector(num_of_items, 2); 
  
  	for (int x : myVector)
		cout << x << " ";
// 		2 2 2 2 2 
}
```

Dans le code ci-dessus, nous avons d'abord défini une variable et lui avons passé une valeur de 5. Cela agit comme le nombre maximum de valeurs que le `vector` aura.

Nous avons ensuite déclaré notre `vector` : `vector myVector(num_of_items, 2);` . Le premier paramètre est la variable du nombre maximum d'éléments tandis que le second paramètre est l'élément réel à stocker dans le `vector`.

Nous avons parcouru et affiché les éléments du `vector`. Nous avons obtenu 2 imprimé cinq fois.

### Comment initialiser un vecteur en utilisant un constructeur en C++

Nous pouvons également initialiser des vecteurs dans des constructeurs. Nous pouvons rendre les valeurs un peu dynamiques. De cette façon, nous n'avons pas à coder en dur les éléments du vecteur.

Voici un exemple :

```c++
#include <iostream>
#include <vector>
using namespace std;

class Vector {
	vector<int> myVec;

public:
	Vector(vector<int> newVector) {
	    myVec = newVector;
	}
	
	void print() {
		for (int i = 0; i < myVec.size(); i++)
			cout << myVec[i] << " ";
	}
	
};

int main() {
    vector<int> vec;
    
	vec.push_back(5);
	vec.push_back(10);
	vec.push_back(15);
	
	Vector vect(vec);
	vect.print();
	// 5 10 15 
}

```

Décortiquons le code.

```c++
class Vector {
	vector<int> myVec;

public:
	Vector(vector<int> newVector) {
	    myVec = newVector;
	}
	
	void print() {
		for (int i = 0; i < myVec.size(); i++)
			cout << myVec[i] << " ";
	}
	
};
```

Nous avons créé une classe appelée **Vector**. Ensuite, nous avons créé une variable de vecteur appelée `myVec`.

Après cela, nous avons défini notre constructeur. Le constructeur a deux méthodes – une qui prend un `vector` initialisé et une autre qui affiche les éléments du `vector`.

```c++
int main() {
    vector<int> vec;
    
	vec.push_back(5);
	vec.push_back(10);
	vec.push_back(15);
	
	Vector vect(vec);
	vect.print();
	// 5 10 15 
}
```

Enfin, comme vous pouvez le voir dans le code ci-dessus, nous avons créé un nouveau `vector` et y avons poussé de nouveaux éléments. Nous avons ensuite affiché ces éléments dans la console.

La logique dans `main` a été créée dans la classe **Vector** qui a également un constructeur.

## Conclusion

Dans cet article, nous avons parlé des vecteurs en C++.

Nous avons commencé par différencier les tableaux et les vecteurs. Les tableaux ont une taille statique tandis que les vecteurs sont plus dynamiques et peuvent s'étendre à mesure que des éléments sont ajoutés.

Nous avons ensuite passé en revue quelques méthodes que nous pouvons utiliser pour initialiser un `vector` en C++ avec des exemples pour chaque section.

Bon codage !