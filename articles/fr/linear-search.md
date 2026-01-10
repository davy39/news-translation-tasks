---
title: Recherche Linéaire Expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T21:58:00.000Z'
originalURL: https://freecodecamp.org/news/linear-search
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d65740569d1a4ca3786.jpg
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
seo_title: Recherche Linéaire Expliquée
seo_desc: 'What is Linear Search?

  Suppose you are given a list or an array of items. You are searching for a particular
  item. How do you do that?

  Find the number 13 in the given list.


  You just look at the list and there it is!


  Now, how do you tell a computer ...'
---

## **Qu'est-ce que la Recherche Linéaire ?**

Supposons que vous avez une liste ou un tableau d'éléments. Vous recherchez un élément particulier. Comment faites-vous cela ?

Trouvez le nombre 13 dans la liste donnée.

![Recherche Linéaire 1](https://i.imgur.com/ThkzYEV.jpg)

Vous regardez simplement la liste et le voilà !

![Recherche Linéaire 2](https://i.imgur.com/K7HfCly.jpg)

Maintenant, comment dire à un ordinateur de le trouver ?

Un ordinateur ne peut pas regarder plus d'une valeur à la fois. Il prend donc un élément du tableau et vérifie s'il est identique à ce que vous recherchez.

![Recherche Linéaire 3](https://i.imgur.com/ZOSxeZD.jpg)

Le premier élément ne correspond pas. Passez donc au suivant.

![Recherche Linéaire 4](https://i.imgur.com/SwKsPxD.jpg)

Et ainsi de suite…

Cela se fait jusqu'à ce qu'une correspondance soit trouvée ou que tous les éléments aient été vérifiés.

![Recherche Linéaire 5](https://i.imgur.com/3AaViff.jpg)

Dans cet algorithme, vous pouvez vous arrêter lorsque l'élément est trouvé et il n'est alors plus nécessaire de chercher plus loin.

Combien de temps faudrait-il pour effectuer l'opération de recherche linéaire ? Dans le meilleur des cas, vous pourriez avoir de la chance et l'élément que vous cherchez pourrait être à la première position du tableau !

Mais dans le pire des cas, vous devriez regarder chaque élément avant de trouver l'élément à la dernière place ou avant de réaliser que l'élément n'est pas dans le tableau.

La complexité de la recherche linéaire est donc O(n).

Si l'élément à rechercher se trouvait dans le premier bloc mémoire, la complexité serait alors : O(1).

Le code pour une fonction de recherche linéaire en JavaScript est montré ci-dessous. Cette fonction retourne la position de l'élément que nous recherchons dans le tableau. Si l'élément n'est pas présent dans le tableau, la fonction retournera null.

### **Exemple en Javascript**

```javascript
function linearSearch(arr, item) {
  // Parcourir tous les éléments de arr pour chercher item.
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] === item) { // Trouvé !
      return i;
    }
  }
  
  // Item non trouvé dans le tableau.
  return null;
}
```

### **Exemple en Ruby**

```ruby
def linear_search(target, array)
  counter = 0

  while counter < array.length
    if array[counter] == target
      return counter
    else
      counter += 1
    end
  end
  return nil
end
```

### **Exemple en C++**

```c++
int linear_search(int arr[],int n,int num)
{
	for(int i=0;i<n;i++){
		if(arr[i]==num)
			return i;
   }
   // Élément non trouvé dans le tableau
   return -1; 
}
```

### **Exemple en Python**

```python
def linear_search(array, num):
	for i in range(len(array)):
		if (array[i]==num):
			return i
	return -1
```

## **Recherche Linéaire Globale**

Que faire si vous recherchez plusieurs occurrences d'un élément ? Par exemple, vous voulez voir combien de 5 il y a dans un tableau.

Cible = 5

Tableau = [ 1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 5]

Ce tableau a 3 occurrences de 5 et nous voulons retourner les index (où ils se trouvent dans le tableau) de tous.

Cela s'appelle la recherche linéaire globale et vous devrez ajuster votre code pour retourner un tableau des points d'index où il trouve votre élément cible.

Lorsque vous trouvez un élément d'index qui correspond à votre cible, le point d'index (compteur) sera ajouté dans le tableau des résultats. S'il ne correspond pas, le code continuera à passer à l'élément suivant du tableau en ajoutant 1 au compteur.

```ruby
def global_linear_search(target, array)
  counter = 0
  results = []

  while counter < array.length
    if array[counter] == target
      results << counter
      counter += 1
    else
      counter += 1
    end
  end

  if results.empty?
    return nil
  else
    return results
  end
end
```

## **Pourquoi la recherche linéaire n'est pas efficace**

Il ne fait aucun doute que la recherche linéaire est simple. Mais parce qu'elle compare chaque élément un par un, elle est chronophage et donc pas très efficace. Si nous devons trouver un nombre parmi, disons, 1 000 000 de nombres et que ce nombre est à la dernière position, une technique de recherche linéaire deviendrait assez fastidieuse.

Vous devriez donc également apprendre le tri à bulles, le tri rapide et d'autres algorithmes plus efficaces.

## Autres algorithmes de recherche :

* [Comment implémenter le tri rapide](https://guide.freecodecamp.org/certifications/coding-interview-prep/algorithms/implement-quick-sort/)
* [Algorithme de recherche binaire](https://guide.freecodecamp.org/algorithms/search-algorithms/binary-search/)
* [Algorithme de recherche par saut](https://guide.freecodecamp.org/algorithms/search-algorithms/jump-search/)
* [Algorithmes de recherche expliqués avec des exemples](https://www.freecodecamp.org/news/search-algorithms-explained-with-examples-in-java-python-and-c/)
* [Implémenter un algorithme de recherche binaire en Java sans récursivité](https://www.freecodecamp.org/news/how-to-implement-a-binary-search-algorithm-in-java-without-recursion-67d9337fd75f/)
* [Plus d'informations sur les algorithmes de recherche](https://guide.freecodecamp.org/algorithms/search-algorithms)