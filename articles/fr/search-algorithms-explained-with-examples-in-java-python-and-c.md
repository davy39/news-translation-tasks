---
title: Algorithmes de Recherche Expliqués avec des Exemples en Java, Python et C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-13T22:09:00.000Z'
originalURL: https://freecodecamp.org/news/search-algorithms-explained-with-examples-in-java-python-and-c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb7740569d1a4ca3eaa.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Java
  slug: java
- name: Python
  slug: python
seo_title: Algorithmes de Recherche Expliqués avec des Exemples en Java, Python et
  C++
seo_desc: 'What is a Search Algorithm?

  This kind of algorithm looks at the problem of re-arranging an array of items in
  ascending order. The two most classical examples of that is the binary search and
  the merge sort algorithm.

  Exponential Search

  Exponential Se...'
---

## Qu'est-ce qu'un Algorithme de Recherche ?

Ce type d'algorithme examine le problème de réorganiser un tableau d'éléments dans l'ordre ascendant. Les deux exemples les plus classiques sont l'algorithme de recherche binaire et l'algorithme de tri fusion.

## Recherche Exponentielle

La recherche exponentielle, également connue sous le nom de recherche par finger, recherche un élément dans un tableau trié en sautant `2^i` éléments à chaque itération, où i représente la valeur de la variable de contrôle de boucle, puis vérifie si l'élément recherché est présent entre le dernier saut et le saut actuel.

### Complexité dans le pire des cas

O(log(N)) Souvent confondu à cause du nom, l'algorithme n'est pas nommé ainsi à cause de la complexité temporelle. Le nom provient du fait que l'algorithme saute des éléments avec des étapes égales aux exponents de 2.

### Étapes

1. Sautez dans le tableau `2^i` éléments à la fois en recherchant la condition `Array[2^(i-1)] < valeurRecherchée < Array[2^i]`. Si `2^i` est supérieur à la longueur du tableau, alors définissez la borne supérieure à la longueur du tableau.
2. Effectuez une recherche binaire entre `Array[2^(i-1)]` et `Array[2^i]`

# Code

```
// Programme C++ pour trouver un élément x dans un
// tableau trié en utilisant la recherche exponentielle.
#include <bits/stdc++.h>
using namespace std;
 
int binarySearch(int arr[], int, int, int);
 
// Retourne la position de la première occurrence de
// x dans le tableau
int exponentialSearch(int arr[], int n, int x)
{
    // Si x est présent à la première position elle-même
    if (arr[0] == x)
        return 0;
 
    // Trouver la plage pour la recherche binaire par
    // doublement répété
    int i = 1;
    while (i < n && arr[i] <= x)
        i = i*2;
 
    // Appeler la recherche binaire pour la plage trouvée.
    return binarySearch(arr, i/2, min(i, n), x);
}
 
// Une fonction de recherche binaire récursive. Elle retourne
// l'emplacement de x dans le tableau donné arr[l..r] si
// présent, sinon -1
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l)
    {
        int mid = l + (r - l)/2;
 
        // Si l'élément est présent au milieu
        // lui-même
        if (arr[mid] == x)
            return mid;
 
        // Si l'élément est plus petit que le milieu, alors il
        // ne peut être présent que dans le sous-tableau de gauche
        if (arr[mid] > x)
            return binarySearch(arr, l, mid-1, x);
 
        // Sinon l'élément ne peut être présent
        // que dans le sous-tableau de droite
        return binarySearch(arr, mid+1, r, x);
    }
 
    // Nous arrivons ici lorsque l'élément n'est pas présent
    // dans le tableau
    return -1;
}
 
int main(void)
{
   int arr[] = {2, 3, 4, 10, 40};
   int n = sizeof(arr)/ sizeof(arr[0]);
   int x = 10;
   int result = exponentialSearch(arr, n, x);
   (result == -1)? printf("L'élément n'est pas présent dans le tableau")
                 : printf("L'élément est présent à l'index %d", result);
   return 0;
}

```

## Recherche dans les Listes Chaînées versus les Tableaux

Supposons que vous deviez rechercher un élément dans une liste chaînée et un tableau non triés. Dans ce cas, vous devez effectuer une recherche linéaire (rappelons, non trié). Effectuer une recherche linéaire pour un élément dans l'une ou l'autre structure de données sera une opération O(n).

Maintenant, si vous avez une liste chaînée et un tableau triés, vous pouvez toujours rechercher dans les deux structures de données en temps O(log n) en utilisant la recherche binaire. Bien que cela soit un peu fastidieux à coder lors de l'utilisation de listes chaînées.

Les listes chaînées sont généralement préférées aux tableaux lorsque l'insertion est une opération fréquente. Il est plus facile d'insérer dans les listes chaînées car seul un pointeur change. Mais pour insérer dans un tableau (au milieu ou au début), vous devez déplacer tous les éléments après celui que vous insérez. Un autre cas où vous devriez utiliser des listes chaînées est lorsque la taille est incertaine (vous ne connaissez pas la taille lorsque vous commencez), car les tableaux ont une taille fixe.

Les tableaux offrent quelques avantages par rapport aux listes chaînées :

1. Accès aléatoire
2. Moins de mémoire par rapport aux listes chaînées
3. Les tableaux ont une meilleure localité de cache, offrant ainsi de meilleures performances

Cela dépend entièrement du cas d'utilisation pour déterminer si les tableaux ou les listes chaînées sont meilleurs.

## Recherche Linéaire

Supposons que vous avez une liste ou un tableau d'éléments. Vous recherchez un élément particulier. Comment faites-vous cela ?

Trouvez le nombre 13 dans la liste donnée.

![Recherche Linéaire 1](https://cdn-media-1.freecodecamp.org/imgr/ThkzYEV.jpg)

Vous regardez simplement la liste et le voilà !

![Recherche Linéaire 2](https://cdn-media-1.freecodecamp.org/imgr/K7HfCly.jpg)

Maintenant, comment dites-vous à un ordinateur de le trouver.

Un ordinateur ne peut pas regarder plus d'une valeur à un instant donné. Il prend donc un élément du tableau et vérifie s'il est le même que ce que vous recherchez.

![Recherche Linéaire 3](https://cdn-media-1.freecodecamp.org/imgr/ZOSxeZD.jpg)

Le premier élément ne correspondait pas. Passez donc au suivant.

![Recherche Linéaire 4](https://cdn-media-1.freecodecamp.org/imgr/SwKsPxD.jpg)

Et ainsi de suite...

Cela se fait jusqu'à ce qu'une correspondance soit trouvée ou jusqu'à ce que tous les éléments aient été vérifiés.

![Recherche Linéaire 5](https://cdn-media-1.freecodecamp.org/imgr/3AaViff.jpg)

Dans cet algorithme, vous pouvez vous arrêter lorsque l'élément est trouvé et il n'est alors plus nécessaire de chercher plus loin.

Combien de temps faudrait-il pour effectuer l'opération de recherche linéaire ? Dans le meilleur des cas, vous pourriez avoir de la chance et l'élément que vous recherchez pourrait être à la première position dans le tableau ! Mais dans le pire des cas, vous devriez regarder chaque élément avant de trouver l'élément à la dernière place ou avant de réaliser que l'élément n'est pas dans le tableau.

La complexité de la recherche linéaire est donc O(n).

Si l'élément à rechercher se trouve dans le premier bloc de mémoire, la complexité serait O(1).

Le code pour une fonction de recherche linéaire en JavaScript est montré ci-dessous. Cette fonction retourne la position de l'élément que nous recherchons dans le tableau. Si l'élément n'est pas présent dans le tableau, la fonction retournera null.

```
int linearSearch(int arr[], int num)
{
        int len = (int)( sizeof(arr) / sizeof(arr[0]);
        int *a = arr;
        for(int i = 0; i < len; i++)
        {
                if(*(a+i) == num) return i;
        }
        return -1;
}

```

### Exemple en JavaScript

```
function linearSearch(arr, item) {
  // Parcourez tous les éléments de arr pour chercher item.
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] === item) { // Trouvé !
      return i;
    }
  }
  
  // L'élément n'est pas trouvé dans le tableau.
  return null;
}

```

### Exemple en Ruby

```
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

### Exemple en C++

```
int linear_search(int arr[],int n,int num)
{
	for(int i=0;i<n;i++){
		if(arr[i]==num)
			return i;
   }
   // L'élément n'est pas trouvé dans le tableau
   return -1; 
}

```

### Exemple en Python

```
def linear_search(array, num):
	for index, element in enumerate(array):
		if element == num:
			return index
	return -1

```

### Exemple en Swift

```
func linearSearch(for number: Int, in array: [Int]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == number { return index } // retourne l'index du nombre
    }
    return nil // le nombre n'a pas été trouvé dans le tableau
}

```

### Exemple en Java

```
int linearSearch(int[] arr, int element)
{
        for(int i=0;i<arr.length;i++)
        {
                if(arr[i] == element)
                        return i;
        }
        return -1;
}

```

### Exemple en PHP

```
function linear_search($arr=[],$num=0)
{
     $n = count($arr);   
     for( $i=0; $i<$n; $i++){
           if($arr[$i] == $num)
                return $i;
      }
      // L'élément n'est pas trouvé dans le tableau
      return -1; 
}

$arr = array(1,3,2,8,5,7,4,0);
print("Résultat de la recherche linéaire pour 2: ");
echo linear_search($arr,2);

```

### Recherche Linéaire Globale

Que faire si vous recherchez plusieurs occurrences d'un élément ? Par exemple, vous voulez voir combien de 5 il y a dans un tableau.

Cible = 5

Tableau = [ 1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 5]

Ce tableau a 3 occurrences de 5 et nous voulons retourner les index (où ils se trouvent dans le tableau) de tous. Cela s'appelle la recherche linéaire globale. Vous devrez ajuster votre code pour retourner un tableau des points d'index auxquels il trouve l'élément cible. Lorsque vous trouvez un élément d'index qui correspond à votre cible, le point d'index (compteur) sera ajouté dans le tableau des résultats. S'il ne correspond pas, le code continuera à passer à l'élément suivant dans le tableau en ajoutant 1 au compteur.

```
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

### Pourquoi la recherche linéaire n'est pas efficace

Il ne fait aucun doute que la recherche linéaire est simple, mais comme elle compare chaque élément un par un, elle est chronophage et donc pas très efficace. Si nous devons trouver un nombre parmi, disons, 1 000 000 de nombres et que le nombre est à la dernière position, la technique de recherche linéaire deviendrait assez fastidieuse. Apprenez donc aussi la recherche binaire, la recherche exponentielle, etc., qui sont beaucoup plus efficaces que la recherche linéaire.

## Recherche Binaire

Une recherche binaire localise un élément dans un tableau trié en divisant répétitivement l'intervalle de recherche en deux.

Comment recherchez-vous un nom dans un annuaire téléphonique ?

Une façon serait de commencer par la première page et de regarder chaque nom dans l'annuaire jusqu'à ce que nous trouvions ce que nous cherchons. Mais ce serait une méthode de recherche extrêmement laborieuse et inefficace.

Parce que nous savons que les noms dans l'annuaire sont triés par ordre alphabétique, nous pourrions probablement suivre les étapes suivantes :

1. Ouvrez la page du milieu de l'annuaire
2. Si elle contient le nom que nous cherchons, nous avons terminé !
3. Sinon, jetez la moitié de l'annuaire qui ne contient pas le nom
4. Répétez jusqu'à ce que vous trouviez le nom ou qu'il n'y ait plus de pages dans l'annuaire

[

![Binaire vs Recherche Linéaire](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif)

]

Complexité temporelle : Comme nous éliminons une partie du cas de recherche à chaque étape de la recherche binaire, et effectuons l'opération de recherche sur l'autre moitié, cela entraîne une complexité temporelle dans le pire des cas de O(log2N). Le meilleur cas se produit lorsque l'élément à trouver est au milieu de la liste. La complexité temporelle du meilleur cas est O(1).

Complexité spatiale : La recherche binaire prend un espace constant ou O(1) ce qui signifie que nous ne définissons aucune variable liée à la taille de l'entrée.

Pour les petits ensembles, la recherche linéaire est meilleure, mais pour les grands ensembles, il est beaucoup plus efficace d'utiliser la recherche binaire.

En détail, combien de fois pouvez-vous diviser N par 2 jusqu'à ce que vous ayez 1 ? Cela revient essentiellement à dire, faites une recherche binaire (la moitié des éléments) jusqu'à ce que vous l'ayez trouvé. Dans une formule, cela serait :

```
1 = N / 2^x

```

Multipliez par 2x :

```
2^x = N

```

Maintenant, faites le log2 :

```
log2(2^x)   = log2 N
x * log2(2) = log2 N
x * 1       = log2 N

```

Cela signifie que vous pouvez diviser log N fois jusqu'à ce que vous ayez tout divisé. Ce qui signifie que vous devez diviser log N ("faire l'étape de recherche binaire") jusqu'à ce que vous trouviez votre élément.

O(log2N) est tel parce qu'à chaque étape, la moitié des éléments de l'ensemble de données sont éliminés, ce qui est justifié par la base de la fonction logarithmique.

C'est l'algorithme de recherche binaire. Il est élégant et efficace, mais pour qu'il fonctionne correctement, le tableau doit être trié.

Trouvez 5 dans le tableau donné de nombres en utilisant la recherche binaire.

![Recherche Binaire 1](https://cdn-media-1.freecodecamp.org/imgr/QAuugOL.jpg)

Marquez les positions basse, haute et médiane dans le tableau.

![Recherche Binaire 2](https://cdn-media-1.freecodecamp.org/imgr/1710fEx.jpg)

Comparez l'élément que vous recherchez avec l'élément du milieu.

![Recherche Binaire 3](https://cdn-media-1.freecodecamp.org/imgr/jr4icze.jpg)

Jetez la moitié gauche et cherchez dans la moitié droite.

![Recherche Binaire 4](https://cdn-media-1.freecodecamp.org/imgr/W57lGsk.jpg)

Comparez à nouveau avec l'élément du milieu.

![Recherche Binaire 5](https://cdn-media-1.freecodecamp.org/imgr/5Twm8NE.jpg)

Maintenant, passez à la moitié gauche.

![Recherche Binaire 6](https://cdn-media-1.freecodecamp.org/imgr/01xetay.jpg)

L'élément du milieu est l'élément que nous recherchions !

L'algorithme de recherche binaire adopte une approche de type diviser pour régner où le tableau est continuellement divisé jusqu'à ce que l'élément soit trouvé ou jusqu'à ce qu'il n'y ait plus d'éléments à vérifier. Par conséquent, cet algorithme peut être défini de manière récursive pour générer une solution élégante.

Les deux cas de base pour la récursion seraient :

* Il n'y a plus d'éléments dans le tableau
* L'élément est trouvé

Le Pouvoir de la Recherche Binaire dans les Systèmes de Données (Arbres B+) : Les Arbres de Recherche Binaire sont très puissants grâce à leurs temps de recherche O(log n), juste après la structure de données de la table de hachage qui utilise une clé de hachage pour rechercher des données en O(1). Il est important de comprendre comment le temps d'exécution log n provient de la hauteur d'un arbre de recherche binaire. Si chaque nœud se divise en deux nœuds, (binaire), alors la profondeur de l'arbre est log n (base 2). Pour améliorer cette vitesse dans les Systèmes de Données, nous utilisons des Arbres B+ car ils ont un facteur de branchement plus large, et donc une plus grande hauteur. J'espère que cet article court aide à élargir votre esprit sur la façon dont la recherche binaire est utilisée dans les systèmes pratiques.

Le code pour la recherche binaire récursive est montré ci-dessous :

### Implémentation en JavaScript

```
function binarySearch(arr, item, low, high) {
    if (low > high) { // Il n'y a plus d'éléments dans le tableau.
        return null;
    }

    // Trouver le milieu du tableau.
    var mid = Math.ceil((low + high) / 2);

    if (arr[mid] === item) { // L'élément a été trouvé !
        return mid;
    }

    if (item < arr[mid]) { // L'élément est dans la moitié de low à mid-1.
        return binarySearch(arr, item, low, mid-1);
    }

    else { // L'élément est dans la moitié de mid+1 à high.
        return binarySearch(arr, item, mid+1, high);
    }
}

var numbers = [1,2,3,4,5,6,7];
print(binarySearch(numbers, 5, 0, numbers.length-1));

```

Voici une autre implémentation en JavaScript :

```
function binary_search(a, v) {
    function search(low, high) {
        if (low === high) {
            return a[low] === v;
        } else {
            var mid = math_floor((low + high) / 2);
            return (v === a[mid])
                   ||
                   (v < a[mid])
                   ? search(low, mid - 1)
                   : search(mid + 1, high);
        }
    }
    return search(0, array_length(a) - 1);
}

```

### Implémentation en Ruby

```
def binary_search(target, array)
  sorted_array = array.sort
  low = 0
  high = (sorted_array.length) - 1

  while high >= low
    middle = (low + high) / 2

    if target > sorted_array[middle]
      low = middle + 1
    elsif target < sorted_array[middle]
      high = middle - 1
    else
      return middle
    end
  end
  return nil
end

```

### Exemple en C

```
int binarySearch(int a[], int l, int r, int x) {
   if (r >= l){
        int mid = (l + (r - l))/2;
        if (a[mid] == x)
            return mid;
        if (arr[mid] > x)
            return binarySearch(arr, l, mid-1, x);
        return binarySearch(arr, mid+1, r, x);
   }
   return -1;
}

```

### Implémentation en Python

```
def binary_search(arr, l, r, target):
    if r >= l:
        mid = (l + (r - l))/2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, l, mid-1, target)
        else:
            return binary_search(arr, mid+1, r, target)
    else:
        return -1

```

### Exemple en C++

Approche récursive !

```
// Approche récursive en C++
int binarySearch(int arr[], int start, int end, int x)
{
   if (end >= start)
   {
        int mid = (start + (end - start))/2;
        if (arr[mid] == x)
            return mid;

        if (arr[mid] > x)
            return binarySearch(arr, start, mid-1, x);

        return binarySearch(arr, mid+1, end, x);
   }
   return -1;
}

```

Approche itérative !

```
int binarySearch(int arr[], int start, int end, int x)
{
    while (start <= end)
    {
        int mid = (start + (end - start))/2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] < x)
            start = mid + 1;
        else
            end = mid - 1;
    }
    return -1;
}

```

### Exemple en Swift

```
func binarySearch(for number: Int, in numbers: [Int]) -> Int? {
    var lowerBound = 0
    var upperBound = numbers.count
    while lowerBound < upperBound {
        let index = lowerBound + (upperBound - lowerBound) / 2
        if numbers[index] == number {
            return index // nous avons trouvé le nombre donné à cet index
        } else if numbers[index] < number {
            lowerBound = index + 1
        } else {
            upperBound = index
        }
    }
    return nil // le nombre donné n'a pas été trouvé
}

```

### Exemple en Java

```
// Approche itérative en Java
int binarySearch(int[] arr, int start, int end, int element)
{
    while(start <= end)
    {
        int mid = start + ( end - start ) / 2;
        if(arr[mid] == element)
            return mid;
        if(arr[mid] < element)
            start = mid+1;
        else
            end = mid-1;
    }
   return -1;
}

```

```
// Approche récursive en Java
int binarySearch(int[] arr, int start,int end , int element)
{
  if (end >= start)
  {
    int mid = start + ( end - start ) / 2;
    if(arr[mid] ==  element)
        return mid;
    if(arr[mid] < element)
        return binarySearch( arr , mid + 1 , end , element );
    else
        return binarySearch( arr, start, mid - 1 , element);
  }
  return -1;
}

```