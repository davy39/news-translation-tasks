---
title: Introduction aux algorithmes - avec des exemples en JavaScript
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-06-06T14:40:36.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-algorithms-with-javascript-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-guduru-ajay-bhargav-1044302.jpg
tags:
- name: algorithms
  slug: algorithms
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
seo_title: Introduction aux algorithmes - avec des exemples en JavaScript
seo_desc: 'Hi everyone! In this article we''re going to take a look at algorithms,
  a key topic when it comes to computer science and software development.

  Algorithm is a fancy, sometimes intimidating, and often misunderstood word. It sounds
  like something really...'
---

Bonjour à tous ! Dans cet article, nous allons examiner les algorithmes, un sujet clé en informatique et en développement logiciel.

Un algorithme est un terme sophistiqué, parfois intimidant et souvent mal compris. Cela semble être quelque chose de vraiment difficile et complexe, mais en réalité, ce n'est rien de plus qu'un ensemble d'étapes à suivre pour atteindre un certain objectif.

Je dirais que les connaissances de base sur les algorithmes se composent principalement de deux choses :

* La notation asymptotique (que nous utilisons pour comparer les performances d'un algorithme par rapport à un autre).
  
* Une connaissance générale des algorithmes classiques utilisés pour des tâches très fréquentes telles que la recherche, le tri et le parcours.
  

C'est exactement ce que nous allons voir ici. 😉 
C'est parti !

## Table des matières

* [Qu'est-ce qu'un algorithme ?](#heading-quest-ce-quun-algorithme)
  
* [Complexité algorithmique](#heading-complexite-algorithmique)
  
* [Algorithmes de recherche](#heading-algorithmes-de-recherche)
  
  * [Recherche linéaire](#heading-recherche-lineaire)
      
  * [Recherche binaire](#heading-recherche-binaire)
      
* [Algorithmes de tri](#heading-algorithmes-de-tri)
  
  * [Tri à bulles](#heading-tri-a-bulles)
      
  * [Tri par sélection](#heading-tri-par-selection)
      
  * [Tri par insertion](#heading-tri-par-insertion)
      
  * [Tri fusion](#heading-tri-fusion)
      
  * [Tri rapide](#heading-tri-rapide)
      
  * [Tri par base](#heading-tri-par-base)
      
* [Algorithmes de parcours](#heading-algorithmes-de-parcours)
  
  * [Parcours en largeur d'abord (BFS)](#heading-parcours-en-largeur-dabord-bfs)
      
  * [Parcours en profondeur d'abord (DFS)](#heading-parcours-en-profondeur-dabord-dfs)
      
      * [Pré-ordre DFS](#heading-pre-ordre-dfs)
          
      * [Post-ordre DFS](#heading-post-ordre-dfs)
          
      * [Ordre DFS](#heading-ordre-dfs)
          
* [Conclusion](#heading-conclusion)
  

# Qu'est-ce qu'un algorithme ?

Comme mentionné précédemment, un algorithme est simplement un ensemble d'étapes à suivre pour atteindre un certain objectif.

Je trouve que lorsque les gens entendent le mot algorithme pour la première fois, ils s'imaginent quelque chose comme ceci...

![Image](https://www.freecodecamp.org/news/content/images/2022/05/markus-spiske-FXFz-sW0uwo-unsplash.jpg align="left")

*Une scène de Matrix ou Mr. Robot*

Mais en réalité, ce genre d'image serait plus précis...

![Image](https://www.freecodecamp.org/news/content/images/2022/05/frank-holleman-rN_RMqSXRKw-unsplash.jpg align="left")

*Un livre de recettes*

Un algorithme est comme une recette, dans le sens où il indique les étapes nécessaires à suivre pour atteindre votre objectif.

Une recette pour faire du pain pourrait être :

```plaintext
1- Mélanger la farine, le sel, l'eau et la levure
2- Laisser lever la pâte
3- Mettre au four pendant 30'
4- Laisser refroidir et déguster
```

Commentaire : J'espère que vous appréciez le fait que je vous apprenne à coder et à cuisiner en même temps, tout cela gratuitement. 😜

Un algorithme pour identifier si un mot est un [palindrome](https://en.wikipedia.org/wiki/Palindrome) ou non pourrait être :

```javascript
function isPalindrome(word) {
	// Étape 1- Placer un pointeur à chaque extrémité du mot
    // Étape 2 - Parcourir la chaîne "vers l'intérieur"
	// Étape 3 - À chaque itération, vérifier si les pointeurs représentent des valeurs égales
	// Si cette condition n'est pas remplie, le mot n'est pas un palindrome
    let left = 0
    let right = word.length-1

    while (left < right) {
        if (word[left] !== word[right]) return false
        left++
        right--
    }
    
    return true
}

isPalindrome("neuquen") // true
isPalindrome("Buenos Aires") // false
```

Comme pour une recette, dans cet algorithme, nous avons des étapes avec un certain but qui sont exécutées dans un ordre donné afin d'obtenir le résultat souhaité.

Selon [Wikipedia](https://en.wikipedia.org/wiki/Algorithm) :

> Un algorithme est une séquence finie d'instructions bien définies, généralement utilisées pour résoudre une classe de problèmes spécifiques ou pour effectuer un calcul.

# Complexité algorithmique

Maintenant que nous savons ce qu'est un algorithme, apprenons à comparer différents algorithmes entre eux.

Imaginons que nous soyons confrontés à ce problème :

> Écrire une fonction qui prend deux paramètres : un tableau non vide d'entiers distincts et un entier représentant une somme cible. Si deux nombres du tableau additionnés donnent la somme cible, la fonction doit les retourner dans un tableau. Si aucun couple de nombres ne donne la somme cible, la fonction doit retourner un tableau vide.

Voici une solution valide au problème :

```javascript
function twoNumberSum(array, targetSum) {
    let result = []
    // Nous utilisons une boucle imbriquée pour tester toutes les combinaisons possibles de nombres dans le tableau
        for (let i = 0; i < array.length; i++) {
          for (let j = i+1; j < array.length; j++) {
              // Si nous trouvons la bonne combinaison, nous ajoutons les deux valeurs au tableau de résultats et le retournons
              if (array[i] + array[j] === targetSum) {
                  result.push(array[i])
                  result.push(array[j])
                  return result
              }
          }
      }
      // Retourner le tableau de résultats
      return result
}

console.log(twoNumberSum([9,1,3,4,5], 6)) // [1,5]
console.log(twoNumberSum([1,2,3,4,5], 10)) // []
```

Voici une autre solution valide :

```javascript
function twoNumberSum(array, targetSum) {
	// Trier le tableau et le parcourir avec un pointeur à chaque extrémité
	// À chaque itération, vérifier si la somme des deux pointeurs est plus grande ou plus petite que la cible
	// Si elle est plus grande, déplacer le pointeur de droite vers la gauche
	// Si elle est plus petite, déplacer le pointeur de gauche vers la droite
	let sortedArray = array.sort((a,b) => a-b)
	let leftLimit = 0
	let rightLimit = sortedArray.length-1

	while (leftLimit < rightLimit) {
			const currentSum = sortedArray[leftLimit] + sortedArray[rightLimit]

			if (currentSum === targetSum) return [sortedArray[leftLimit], sortedArray[rightLimit]]
			else currentSum < targetSum ? leftLimit++ : rightLimit--        
	}

	return []
}

console.log(twoNumberSum([9,1,3,4,5], 6)) // [1,5]
console.log(twoNumberSum([1,2,3,4,5], 10)) // []
```

Et voici une autre solution valide :

```javascript
function twoNumberSum(array, targetSum) {
    // Parcourir le tableau une fois, et à chaque itération
    // vérifier si le nombre dont vous avez besoin pour atteindre la cible existe dans le tableau
    // Si il existe, retourner son index et l'index du nombre actuel
	let result = []

	for (let i = 0; i < array.length; i++) {
        let desiredNumber = targetSum - array[i]
        if (array.indexOf(desiredNumber) !== -1 && array.indexOf(desiredNumber) !== i) {
            result.push(array[i])
            result.push(array[array.indexOf(desiredNumber)])
            break
        }
	}

    return result
}

console.log(twoNumberSum([9,1,3,4,5], 6)) // [1,5]
console.log(twoNumberSum([1,2,3,4,5], 10)) // []
```

Alors, comment pouvons-nous comparer quelle solution est la meilleure ? Elles accomplissent toutes leur objectif, n'est-ce pas ?

Mais outre l'**efficacité** (si l'objectif est atteint ou non), nous devons également évaluer les algorithmes en termes d'**efficience**, c'est-à-dire celui qui résout le problème en utilisant la plus petite quantité de ressources **en termes de temps** (temps de traitement) **et d'espace** (utilisation de la mémoire).

Une pensée automatique qui vient à l'esprit lorsque l'on réfléchit à cela est : "Mesurez simplement combien de temps l'algorithme met à s'exécuter". Et c'est valable.

Mais le problème est que le même algorithme peut prendre plus ou moins de temps sur un ordinateur différent en fonction de son matériel et de sa configuration. Et même sur le même ordinateur, il peut prendre plus ou moins de temps à s'exécuter en fonction des tâches en arrière-plan que vous avez en cours à ce moment-là.

Ce dont nous avons besoin, c'est d'une méthode objective et invariable pour mesurer les performances d'un algorithme, et c'est exactement à cela que sert la **notation asymptotique**.

La notation asymptotique (également appelée **notation Big O**) est un système qui nous permet d'**analyser et comparer les performances d'un algorithme à mesure que son entrée grandit**.

Big O est une méthode standardisée pour analyser et comparer la complexité (en termes de temps d'exécution et d'espace) de différents algorithmes. La complexité Big O d'un algorithme sera toujours la même, peu importe l'ordinateur sur lequel vous la "calculez", car la complexité est calculée sur **la manière dont le nombre d'opérations de l'algorithme varie lorsque l'entrée varie**, et cette relation reste toujours la même, quel que soit l'environnement.

Il existe de nombreuses complexités possibles pour un algorithme, mais les plus courantes sont les suivantes :

* **Constante — O(1) :** Lorsque le nombre d'opérations/espace requis est toujours le même indépendamment de l'entrée. Prenons par exemple une fonction qui prend un nombre en entrée et retourne ce nombre moins 10. Peu importe que vous lui donniez 100 ou 1000000 en entrée, cette fonction effectuera toujours une seule opération (soustraire 10), donc la complexité est constante O(1).
  
* **Logarithmique — O(log n) :** Lorsque le nombre d'opérations/espace requis croît à un rythme de plus en plus lent par rapport à la croissance de l'entrée. Ce type de complexité se trouve souvent dans les algorithmes qui adoptent une approche de type "diviser pour régner" ou dans les algorithmes de recherche. L'exemple classique est la recherche binaire, dans laquelle l'ensemble de données que vous devez parcourir se divise continuellement par deux jusqu'à ce que vous atteigniez le résultat final.
  
* **Linéaire —O(n) :** Lorsque le nombre d'opérations/espace requis croît au même rythme que l'entrée. Prenons par exemple une boucle qui imprime chaque valeur trouvée dans un tableau. Le nombre d'opérations croîtra avec la longueur du tableau, donc la complexité est linéaire O(n).
  
* **Quadratique — O(n²) :** Lorsque le nombre d'opérations/espace requis croît au carré par rapport à l'entrée. Les boucles imbriquées sont l'exemple classique pour cela. Imaginez que nous avons une boucle qui itère à travers un tableau de nombres, et dans cette boucle, nous en avons une autre qui itère à nouveau à travers le tableau entier. Pour chaque valeur dans le tableau, nous itérons à travers le tableau deux fois, donc la complexité est quadratique O(n²).
  

![Image](https://www.freecodecamp.org/news/content/images/2022/05/2022-05-16_1232131236.png align="left")

*Une représentation graphique des complexités classiques des algorithmes*

Notez que la même notation est utilisée pour parler à la fois de la complexité temporelle et spatiale. Par exemple, si nous avons une fonction qui crée toujours un tableau avec une seule valeur, quelle que soit l'entrée qu'elle reçoit, alors la complexité spatiale sera constante O(1), et ainsi de suite pour les autres types de complexité.

Pour mieux comprendre tout cela, revenons à notre problème et analysons nos exemples de solutions.

### Exemple 1 :

```javascript
function twoNumberSum(array, targetSum) {
    let result = []
    // Nous utilisons une boucle imbriquée pour tester toutes les combinaisons possibles de nombres dans le tableau
        for (let i = 0; i < array.length; i++) {
          for (let j = i+1; j < array.length; j++) {
              // Si nous trouvons la bonne combinaison, nous ajoutons les deux valeurs au tableau de résultats et le retournons
              if (array[i] + array[j] === targetSum) {
                  result.push(array[i])
                  result.push(array[j])
                  return result
              }
          }
      }
      // Retourner le tableau de résultats
      return result
}

console.log(twoNumberSum([9,1,3,4,5], 6)) // [1,5]
console.log(twoNumberSum([1,2,3,4,5], 10)) // []
```

Dans cet exemple, nous parcourons le tableau de paramètres, et pour chaque valeur dans le tableau, nous parcourons à nouveau tout le tableau à la recherche d'un nombre qui, additionné, donne la somme cible.

Chaque itération compte comme une tâche.

* Si nous avions **3** nombres dans le tableau, nous itérerions 3 fois pour chaque nombre et 9 fois de plus (3 fois les trois nombres dans le tableau.) **12** tâches au total.
  
* Si nous avions 4 nombres dans le tableau, nous itérerions 4 fois pour chaque nombre et 16 fois de plus (4 fois les quatre nombres dans le tableau.) **20** tâches au total.
  
* Si nous avions 5 nombres dans le tableau, nous itérerions 5 fois pour chaque nombre et 25 fois de plus (5 fois les cinq nombres dans le tableau.) **25** tâches au total.
  

Vous pouvez voir comment le nombre de tâches dans cet algorithme croît de manière exponentielle et disproportionnée par rapport à l'entrée. La complexité de cet algorithme est quadratique — **O(n²)**.

Chaque fois que nous voyons des boucles imbriquées, nous devons penser à une complexité quadratique => MAUVAIS => Il y a probablement une meilleure façon de résoudre cela.

### Exemple 2 :

```javascript
function twoNumberSum(array, targetSum) {
	// Trier le tableau et le parcourir avec un pointeur à chaque extrémité
	// À chaque itération, vérifier si la somme des deux pointeurs est plus grande ou plus petite que la cible
	// Si elle est plus grande, déplacer le pointeur de droite vers la gauche
	// Si elle est plus petite, déplacer le pointeur de gauche vers la droite
	let sortedArray = array.sort((a,b) => a-b)
	let leftLimit = 0
	let rightLimit = sortedArray.length-1

	while (leftLimit < rightLimit) {
			const currentSum = sortedArray[leftLimit] + sortedArray[rightLimit]

			if (currentSum === targetSum) return [sortedArray[leftLimit], sortedArray[rightLimit]]
			else currentSum < targetSum ? leftLimit++ : rightLimit--        
	}

	return []
}

console.log(twoNumberSum([9,1,3,4,5], 6)) // [1,5]
console.log(twoNumberSum([1,2,3,4,5], 10)) // []
```

Ici, nous trions l'algorithme avant de l'itérer. Ensuite, nous ne l'itérons qu'une seule fois, en utilisant un pointeur à chaque extrémité du tableau et en itérant "vers l'intérieur".

C'est mieux que la solution précédente, puisque nous n'itérons qu'une seule fois. Mais nous trions toujours le tableau (ce qui a généralement une complexité logarithmique) puis nous itérons une fois (ce qui est une complexité linéaire). La complexité algorithmique de cette solution est **O(n log(n)).**

### Exemple 3 :

```javascript
function twoNumberSum(array, targetSum) {
    // Parcourir le tableau une fois, et à chaque itération
    // vérifier si le nombre dont vous avez besoin pour atteindre la cible existe dans le tableau
    // Si il existe, retourner son index et l'index du nombre actuel
	let result = []

	for (let i = 0; i < array.length; i++) {
        let desiredNumber = targetSum - array[i]
        if (array.indexOf(desiredNumber) !== -1 && array.indexOf(desiredNumber) !== i) {
            result.push(array[i])
            result.push(array[array.indexOf(desiredNumber)])
            break
        }
	}

    return result
}

console.log(twoNumberSum([9,1,3,4,5], 6)) // [1,5]
console.log(twoNumberSum([1,2,3,4,5], 10)) // []
```

Dans ce dernier exemple, nous ne parcourons le tableau qu'une seule fois, sans rien faire d'autre avant. C'est la meilleure solution, car nous effectuons le plus petit nombre d'opérations. La complexité dans ce cas est linéaire — **O(n)**.

C'est vraiment **le concept le plus important derrière les algorithmes**. Être capable de comparer différentes implémentations et de comprendre laquelle est la plus efficace et pourquoi est vraiment une connaissance importante à avoir. Donc si le concept n'est pas encore clair pour vous, je vous encourage à relire les exemples, à chercher d'autres ressources ou à consulter [cette vidéo-cours géniale de freeCodeCamp](https://www.youtube.com/watch?v=8hly31xKli0).

# Algorithmes de recherche

Une fois que vous avez une bonne compréhension de la complexité algorithmique, la prochaine chose à savoir sont les algorithmes populaires utilisés pour résoudre des tâches de programmation très courantes. Alors commençons par la recherche.

Lorsque l'on recherche une valeur dans une structure de données, il existe différentes approches que nous pouvons adopter. Nous allons examiner deux des options les plus utilisées et les comparer.

## **Recherche linéaire**

La recherche linéaire consiste à parcourir la structure de données une valeur à la fois et à vérifier si cette valeur est celle que nous recherchons. C'est probablement le type de recherche le plus intuitif et le meilleur que nous puissions faire si la structure de données que nous utilisons n'est pas ordonnée.

Supposons que nous avons un tableau de nombres et que pour ce tableau, nous voulons écrire une fonction qui prend un nombre en entrée et retourne l'index de ce nombre dans le tableau. Dans le cas où il n'existe pas dans le tableau, il retournera -1. Une approche possible pourrait être la suivante :

```javascript
const arr = [1,2,3,4,5,6,7,8,9,10]

const search = num => {
    for (let i = 0; i < arr.length; i++) {
        if (num === arr[i]) return i
    }
    return -1
}

console.log(search(6)) // 5
console.log(search(11)) // -1
```

Comme le tableau n'est pas ordonné, nous n'avons pas de moyen de connaître la position approximative de chaque valeur, donc le mieux que nous puissions faire est de vérifier une valeur à la fois. La complexité de cet algorithme est **linéaire - O(n)** puisque dans le pire des cas, nous devrons parcourir tout le tableau une fois pour obtenir la valeur que nous recherchons.

La recherche linéaire est l'approche utilisée par de nombreuses méthodes JavaScript intégrées comme `indexOf`, `includes` et `findIndex`.

## **Recherche binaire**

Lorsque nous avons une structure de données ordonnée, il existe une approche beaucoup plus efficace que nous pouvons adopter, la recherche binaire. Ce que nous faisons dans la recherche binaire est le suivant :

* Sélectionner la valeur médiane de notre structure de données et "demander", est-ce la valeur que nous recherchons ?
  
* Si ce n'est pas le cas, nous "demandons" si la valeur que nous recherchons est plus grande ou plus petite que la valeur médiane ?
  
* Si elle est plus grande, nous "écartons" toutes les valeurs plus petites que la valeur médiane. Si elle est plus petite, nous "écartons" toutes les valeurs plus grandes que la valeur médiane.
  
* Et ensuite nous répétons la même opération jusqu'à ce que nous trouvions la valeur donnée ou que le "morceau" restant de la structure de données ne puisse plus être divisé.
  

![Image](https://www.freecodecamp.org/news/content/images/2022/05/binary_search_1.png align="left")

*Une représentation graphique de la recherche binaire*

Ce qui est si génial avec la recherche binaire, c'est que dans chaque itération, nous écartons environ la moitié de la structure de données. Cela rend la recherche vraiment rapide et efficace. 👌

Supposons que nous avons le même tableau (ordonné) et que nous voulons écrire la même fonction que précédemment, qui prend un nombre en entrée et retourne l'index de ce nombre dans le tableau. Dans le cas où il n'existe pas dans le tableau, il retournera -1. Une approche de recherche binaire pourrait être la suivante :

```javascript
const arr = [1,2,3,4,5,6,7,8,9,10]

const search = num => {
    // Nous allons utiliser trois pointeurs.
    // Un au début du tableau, un à la fin et un autre au milieu.
    let start = 0
    let end = arr.length-1
    let middle = Math.floor((start+end)/2)

    // Tant que nous n'avons pas trouvé le nombre et que le pointeur de début est égal ou inférieur au pointeur de fin
    while (arr[middle] !== num && start <= end) {
        // Si le nombre souhaité est plus petit que le milieu, écarter la moitié supérieure du tableau
        if (num < arr[middle]) end = middle - 1
        // Si le nombre souhaité est plus grand que le milieu, écarter la moitié inférieure du tableau
        else start = middle + 1
        // Recalculer la valeur médiane
        middle = Math.floor((start+end)/2)
    }
    // Si nous avons quitté la boucle, cela signifie que nous avons soit trouvé la valeur, soit le tableau ne peut plus être divisé
    return arr[middle] === num ? middle : -1
}

console.log(search(6)) // 5
console.log(search(11)) // -1
```

Cette approche peut sembler "plus de code" au premier abord, mais les itérations potentielles sont en réalité beaucoup moins nombreuses que dans la recherche linéaire, et cela est dû au fait que dans chaque itération, nous écartons environ la moitié de la structure de données. La complexité de cet algorithme est **logarithmique** — **O(log n)**.

# Algorithmes de tri

Lorsque l'on trie des structures de données, il existe de nombreuses approches possibles que nous pouvons adopter. Examinons quelques-unes des options les plus utilisées et comparons-les.

## **Tri à bulles**

Le tri à bulles parcourt la structure de données et compare une paire de valeurs à la fois. Si l'ordre de ces valeurs est incorrect, il échange leurs positions pour le corriger. L'itération est répétée jusqu'à ce que les données soient ordonnées. Cet algorithme fait "remonter" les valeurs plus grandes à la fin du tableau.

Cet algorithme a une complexité **quadratique — O(n²)** puisqu'il comparera chaque valeur avec le reste des valeurs une fois.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1641395941732/Apvay5Jc9.png?auto=compress,format&format=webp align="left")

Une implémentation possible pourrait être la suivante :

```javascript
const arr = [3,2,1,4,6,5,7,9,8,10]

const bubbleSort = arr => {
    // définir une variable de drapeau
    let noSwaps
	
    // Nous aurons une boucle imbriquée
    // avec un pointeur itérant de droite à gauche
    for (let i = arr.length; i > 0; i--) {
        noSwaps = true
		// et un autre itérant de droite à gauche
        for (let j = 0; j < i-1; j++) {
            // Nous comparons les deux pointeurs
            if (arr[j] > arr[j+1]) {
                let temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                noSwaps = false
            }
        }
        if (noSwaps) break
    }
}

bubbleSort(arr)
console.log(arr) // [1,2,3,4,5,6,7,8,9,10]
```

## **Tri par sélection**

Le tri par sélection est similaire au tri à bulles, mais au lieu de placer les valeurs plus grandes à la fin de la structure de données, il se concentre sur le placement des valeurs plus petites au début. Les étapes qu'il suit sont les suivantes :

* Stocker le premier élément de la structure de données comme valeur minimale.
  
* Parcourir la structure de données en comparant chaque valeur avec la valeur minimale. Si une valeur plus petite est trouvée, elle identifie cette valeur comme la nouvelle valeur minimale.
  
* Si la valeur minimale n'est pas le premier élément de la structure de données, elle échange les positions de la valeur minimale et du premier élément.
  
* Elle répète cette itération jusqu'à ce que la structure de données soit ordonnée.
  

Cet algorithme a une complexité **quadratique — O(n²)**.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1641396007307/xL8U4iwf8.png?auto=compress,format&format=webp align="left")

Une implémentation possible pourrait être la suivante :

```javascript
const arr = [3,2,1,4,6,5,7,9,8,10]

const selectionSort = arr => {
    
    for (let i = 0; i < arr.length; i++) {
        let lowest = i
        
        for (let j = i+1; j < arr.length; j++) {
            if (arr[j] < arr[lowest]) {
                lowest = j
            }
        }

        if (i !== lowest) {
            let temp = arr[i]
            arr[i] = arr[lowest]
            arr[lowest] = temp
        }
    }
}

selectionSort(arr)
console.log(arr) // [1,2,3,4,5,6,7,8,9,10]
```

## **Tri par insertion**

Le tri par insertion ordonne la structure de données en créant une "moitié ordonnée" qui est toujours correctement triée, et parcourt la structure de données en prenant chaque valeur et en l'insérant dans la moitié ordonnée exactement à l'endroit où elle devrait être.

Les étapes qu'il suit sont les suivantes :

* Il commence par prendre le deuxième élément de la structure de données.
  
* Il compare cet élément avec celui qui le précède et échange leurs positions si nécessaire.
  
* Il passe à l'élément suivant et s'il n'est pas à la bonne position, il parcourt la "moitié ordonnée" pour trouver sa position correcte et l'y insère.
  
* Il répète le même processus jusqu'à ce que la structure de données soit triée.
  

Cet algorithme a une complexité **quadratique (O(n²))**.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1641396070224/7T4A0Sfqr.png?auto=compress,format&format=webp align="left")

Une implémentation possible pourrait être la suivante :

```javascript
const arr = [3,2,1,4,6,5,7,9,8,10]

const insertionSort = arr => {
    let currentVal
    
    for (let i = 0; i < arr.length; i++) {
        currentVal = arr[i]

        for (var j = i-1; j >= 0 && arr[j] > currentVal; j--) {
            arr[j+1] = arr[j]
        }
        
        arr[j+1] = currentVal
    }
    
    return arr
}

insertionSort(arr)
console.log(arr) // [1,2,3,4,5,6,7,8,9,10]
```

Le problème avec le tri à bulles, le tri par sélection et le tri par insertion est que ces algorithmes ne s'adaptent pas bien.

Il existe de bien meilleures options que nous pouvons choisir lorsque nous travaillons avec de grands ensembles de données. Certaines d'entre elles sont le tri fusion, le tri rapide et le tri par base. Alors, examinons celles-ci maintenant !

## **Tri fusion**

Le tri fusion est un algorithme qui décompose récursivement la structure de données en valeurs individuelles, puis la recompose de manière triée.

Les étapes qu'il suit sont les suivantes :

* Diviser récursivement la structure de données en moitiés jusqu'à ce que chaque "morceau" n'ait qu'une seule valeur.
  
* Ensuite, fusionner récursivement les morceaux de manière triée jusqu'à ce qu'il retrouve la longueur de la structure de données originale.
  

Cet algorithme a une complexité **O(n log n)**, puisque la partie décomposition a une complexité de log n et la partie comparaison a une complexité de n.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1641396131234/Oiryt3mR92.png?auto=compress,format&format=webp align="left")

Une implémentation possible pourrait être la suivante :

```javascript
const arr = [3,2,1,4,6,5,7,9,8,10]

// Fonction de fusion
const merge = (arr1, arr2) => {
    const results = []
    let i = 0
    let j = 0

    while (i < arr1.length && j < arr2.length) {
        if (arr2[j] > arr1[i]) {
            results.push(arr1[i])
            i++
        } else {
            results.push(arr2[j])
            j++
        }
    }

    while (i < arr1.length) {
        results.push(arr1[i])
        i++
    }

    while (j < arr2.length) {
        results.push(arr2[j])
        j++
    }

    return results
}

const mergeSort = arr => {
    if (arr.length <= 1) return arr
    let mid = Math.floor(arr.length/2)
    let left = mergeSort(arr.slice(0,mid))
    let right = mergeSort(arr.slice(mid))
    return merge(left, right)
}

console.log(mergeSort(arr)) // [1,2,3,4,5,6,7,8,9,10]
```

## **Tri rapide**

Le tri rapide fonctionne en sélectionnant un élément (appelé "le pivot") et en trouvant l'index où le pivot devrait se retrouver dans le tableau trié.

Le temps d'exécution du tri rapide dépend en partie de la manière dont le pivot est sélectionné. Idéalement, il devrait être approximativement la valeur médiane de l'ensemble de données à trier.

Les étapes que l'algorithme suit sont les suivantes :

* Identifier la valeur du pivot et la placer à l'index où elle devrait être.
  
* Exécuter récursivement le même processus sur chaque "moitié" de la structure de données.
  

Cet algorithme a une complexité **O(n log n)**.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1641396182239/_MdqPPTf7.png?auto=compress,format&format=webp align="left")

Une implémentation possible pourrait être la suivante :

```javascript
const arr = [3,2,1,4,6,5,7,9,8,10]

const pivot = (arr, start = 0, end = arr.length - 1) => {
    const swap = (arr, idx1, idx2) => [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]]

    let pivot = arr[start]
    let swapIdx = start

    for (let i = start+1; i <= end; i++) {
        if (pivot > arr[i]) {
            swapIdx++
            swap(arr, swapIdx, i)
        }
    }

    swap(arr, start, swapIdx)
    return swapIdx
}

const quickSort = (arr, left = 0, right = arr.length - 1) => {
    if (left < right) {
        let pivotIndex = pivot(arr, left, right)
        quickSort(arr, left, pivotIndex-1)
        quickSort(arr, pivotIndex+1, right)
    }

    return arr
}

console.log(quickSort(arr)) // [1,2,3,4,5,6,7,8,9,10]
```

## **Tri par base**

Radix est un algorithme qui fonctionne différemment des précédents, dans le sens où il ne compare pas les valeurs. Radix est utilisé pour trier des listes de nombres, et pour ce faire, il exploite le fait que la taille d'un nombre est définie par le nombre de chiffres qu'il possède (plus il y a de chiffres, plus le nombre est grand).

Ce que fait Radix, c'est trier les valeurs par leurs chiffres dans l'ordre. Il trie d'abord toutes les valeurs par le premier chiffre, puis à nouveau par le deuxième, puis par le troisième... Ce processus est répété autant de fois que le nombre de chiffres du plus grand nombre dans la liste. Et à la fin de ce processus, l'algorithme retourne la liste entièrement triée.

Les étapes qu'il suit sont les suivantes :

* Déterminer combien de chiffres le plus grand nombre possède.
  
* Parcourir la liste jusqu'au plus grand nombre de chiffres. À chaque itération :
  
* Créer des "seaux" pour chaque chiffre (de 0 à 9) et placer chaque valeur dans son seau correspondant selon le chiffre évalué.
  
* Remplacer la liste existante par les valeurs triées dans les seaux, en commençant par 0 et en allant jusqu'à 9.
  

Cet algorithme a une complexité **O(n*k)**, k étant le nombre de chiffres du plus grand nombre. Étant donné qu'il ne compare pas les valeurs entre elles, cet algorithme a un meilleur temps d'exécution que ceux vus précédemment, mais ne fonctionnera que sur des listes de nombres.

Si nous voulons un algorithme de tri agnostique des données, nous opterions probablement pour l'un des précédents.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1641396244650/EwnCsTr4y.png?auto=compress,format&format=webp align="left")

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1641396253081/wJlnCC_kg.png?auto=compress,format&format=webp align="left")

Une implémentation possible pourrait être la suivante :

```javascript
const arr = [3,2,1,4,6,5,7,9,8,10]

const getDigit = (num, i) => Math.floor(Math.abs(num) / Math.pow(10, i)) % 10

const digitCount = num => {
    if (num === 0) return 1
    return Math.floor(Math.log10(Math.abs(num))) + 1
}

const mostDigits = nums => {
    let maxDigits = 0

    for (let i = 0; i < nums.length; i++) maxDigits = Math.max(maxDigits, digitCount(nums[i]))

    return maxDigits
}

const radixSort = nums => {
    let maxDigitCount = mostDigits(nums)

    for (let k = 0; k < maxDigitCount; k++) {
        let digitBuckets = Array.from({ length: 10 }, () => [])
        
        for (let i = 0; i < nums.length; i++) {
            let digit = getDigit(nums[i], k)
            digitBuckets[digit].push(nums[i])
        }

        nums = [].concat(...digitBuckets)
    }

    return nums
}

console.log(radixSort(arr)) // [1,2,3,4,5,6,7,8,9,10]
```

# Algorithmes de parcours

Le dernier type d'algorithme que nous allons examiner sont les algorithmes de parcours, qui sont utilisés pour itérer à travers des structures de données qui peuvent être itérées de différentes manières (principalement des arbres et des graphes).

Lorsque l'on itère une structure de données comme un arbre, nous pouvons prioriser les itérations de deux manières principales, soit en largeur, soit en profondeur.

Si nous priorisons la profondeur, nous "descendrons" à travers chaque branche de l'arbre, allant de la tête à la feuille de chaque branche.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-42.png align="left")

*Profondeur d'abord*

Si nous priorisons la largeur, nous parcourons chaque "niveau" de l'arbre horizontalement, en itérant à travers tous les nœuds qui se trouvent au même niveau avant de "descendre" au niveau suivant.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-39.png align="left")

*Largeur d'abord*

Celui que nous choisissons dépendra largement de la valeur que nous recherchons dans notre itération et de la manière dont notre structure de données est construite.

## Parcours en largeur d'abord (BFS)

Alors analysons d'abord le BFS. Comme mentionné, ce type de parcours itérera à travers notre structure de données de manière "horizontale". En suivant cette nouvelle image d'exemple, les valeurs seraient parcourues dans l'ordre suivant : `[10, 6, 15, 3, 8, 20]`.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-40.png align="left")

Typiquement, les étapes suivies par les algorithmes BFS sont les suivantes :

* Créer une file d'attente et une variable pour stocker les nœuds qui ont été "visités"
  
* Placer le nœud racine à l'intérieur de la file d'attente
  
* Continuer à boucler tant qu'il y a quelque chose dans la file d'attente
  
* Défiler un nœud de la file d'attente et pousser la valeur du nœud dans la variable qui stocke les nœuds visités
  
* Si le nœud défilé a une propriété gauche, l'ajouter à la file d'attente
  
* Si le nœud défilé a une propriété droite, l'ajouter à la file d'attente
  

Une implémentation possible pourrait être la suivante :

```javascript
class Node {
    constructor(value) {
        this.value = value
        this.left = null
        this.right = null
    }
}

class BinarySearchTree {
    constructor(){ this.root = null; }

    insert(value){
        let newNode = new Node(value);
        if(this.root === null){
            this.root = newNode;
            return this;
        }
        let current = this.root;
        while(true){
            if(value === current.value) return undefined;
            if(value < current.value){
                if(current.left === null){
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if(current.right === null){
                    current.right = newNode;
                    return this;
                } 
                current = current.right;
            }
        }
    }

    BFS(){
        let node = this.root,
            data = [],
            queue = [];
        queue.push(node);

        while(queue.length){
           node = queue.shift();
           data.push(node.value);
           if(node.left) queue.push(node.left);
           if(node.right) queue.push(node.right);
        }
        return data;
    }
}


const tree = new BinarySearchTree()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

console.log(tree.BFS()) // [ 10, 6, 15, 3, 8, 20 ]
```

## Parcours en profondeur d'abord (DFS)

Le DFS itérera à travers notre structure de données de manière "verticale". En suivant le même exemple que nous avons utilisé pour le BFS, les valeurs seraient parcourues dans l'ordre suivant : `[10, 6, 3, 8, 15, 20]`.

Cette manière de faire le DFS est appelée "pré-ordre". Et il existe en réalité trois manières principales de faire le DFS, chacune étant différente simplement en changeant l'ordre dans lequel les nœuds sont visités.

* **Pré-ordre :** Visiter le nœud actuel, puis le nœud de gauche, puis le nœud de droite.
  
* **Post-ordre :** Explorer tous les enfants à gauche, et tous les enfants à droite avant de visiter le nœud.
  
* **Ordre :** Explorer tous les enfants à gauche, visiter le nœud actuel, et explorer tous les enfants à droite.
  

Si cela semble confus, ne vous inquiétez pas. Ce n'est pas si complexe et cela deviendra plus clair avec quelques exemples.

### Pré-ordre DFS

Dans un algorithme DFS pré-ordre, nous faisons ce qui suit :

* Créer une variable pour stocker les valeurs des nœuds visités
  
* Stocker la racine de l'arbre dans une variable
  
* Écrire une fonction auxiliaire qui accepte un nœud comme paramètre
  
* Pousser la valeur du nœud dans la variable qui stocke les valeurs
  
* Si le nœud a une propriété gauche, appeler la fonction auxiliaire avec le nœud de gauche comme paramètre
  
* Si le nœud a une propriété droite, appeler la fonction auxiliaire avec le nœud de gauche comme paramètre
  

Une implémentation possible pourrait être la suivante :

```javascript
class Node {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor(){
        this.root = null;
    }
    insert(value){
        var newNode = new Node(value);
        if(this.root === null){
            this.root = newNode;
            return this;
        }
        var current = this.root;
        while(true){
            if(value === current.value) return undefined;
            if(value < current.value){
                if(current.left === null){
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if(current.right === null){
                    current.right = newNode;
                    return this;
                } 
                current = current.right;
            }
        }
    }

    DFSPreOrder(){
        var data = [];
        function traverse(node){
            data.push(node.value);
            if(node.left) traverse(node.left);
            if(node.right) traverse(node.right);
        }
        traverse(this.root);
        return data;
    }

}


var tree = new BinarySearchTree()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

console.log(tree.DFSPreOrder()) // [ 10, 6, 3, 8, 15, 20 ]
```

### Post-ordre DFS

Dans un algorithme DFS post-ordre, nous faisons ce qui suit :

* Créer une variable pour stocker les valeurs des nœuds visités
  
* Stocker la racine de l'arbre dans une variable
  
* Écrire une fonction auxiliaire qui accepte un nœud comme paramètre
  
* Si le nœud a une propriété gauche, appeler la fonction auxiliaire avec le nœud de gauche comme paramètre
  
* Si le nœud a une propriété droite, appeler la fonction auxiliaire avec le nœud de gauche comme paramètre
  
* Appeler la fonction auxiliaire avec le nœud actuel comme paramètre
  

Une implémentation possible pourrait être la suivante :

```javascript
class Node {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor(){
        this.root = null;
    }
    insert(value){
        var newNode = new Node(value);
        if(this.root === null){
            this.root = newNode;
            return this;
        }
        var current = this.root;
        while(true){
            if(value === current.value) return undefined;
            if(value < current.value){
                if(current.left === null){
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if(current.right === null){
                    current.right = newNode;
                    return this;
                } 
                current = current.right;
            }
        }
    }


    DFSPostOrder(){
        var data = [];
        function traverse(node){
            if(node.left) traverse(node.left);
            if(node.right) traverse(node.right);
            data.push(node.value);
        }
        traverse(this.root);
        return data;
    }
}


var tree = new BinarySearchTree()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

console.log(tree.DFSPostOrder()) // [ 3, 8, 6, 20, 15, 10 ]
```

### Ordre DFS

Dans un algorithme DFS en ordre, nous faisons ce qui suit :

* Créer une variable pour stocker les valeurs des nœuds visités
  
* Stocker la racine de l'arbre dans une variable
  
* Écrire une fonction auxiliaire qui accepte un nœud comme paramètre
  
* Si le nœud a une propriété gauche, appeler la fonction auxiliaire avec le nœud de gauche comme paramètre
  
* Pousser la valeur du nœud dans la variable qui stocke les valeurs
  
* Si le nœud a une propriété droite, appeler la fonction auxiliaire avec le nœud de gauche comme paramètre
  
* Appeler la fonction auxiliaire avec le nœud actuel comme paramètre
  

Une implémentation possible pourrait être la suivante :

```javascript
class Node {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor(){
        this.root = null;
    }
    insert(value){
        var newNode = new Node(value);
        if(this.root === null){
            this.root = newNode;
            return this;
        }
        var current = this.root;
        while(true){
            if(value === current.value) return undefined;
            if(value < current.value){
                if(current.left === null){
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if(current.right === null){
                    current.right = newNode;
                    return this;
                } 
                current = current.right;
            }
        }
    }

    DFSInOrder(){
        var data = [];
        function traverse(node){
            if(node.left) traverse(node.left);
            data.push(node.value);
            if(node.right) traverse(node.right);
        }
        traverse(this.root);
        return data;
    }
}


var tree = new BinarySearchTree()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

console.log(tree.DFSInOrder()) // [ 3, 6, 8, 10, 15, 20 ]
```

Comme vous l'avez probablement remarqué, les implémentations pré-ordre, post-ordre et en ordre sont toutes très similaires et nous changeons simplement l'ordre de visite des nœuds. Le résultat du parcours que nous obtenons est assez différent avec chaque implémentation et parfois l'une peut être plus utile que les autres.

En ce qui concerne le moment où utiliser BFS ou DFS, comme je l'ai dit, cela dépend de la manière dont notre structure de données est organisée.

De manière générale, si nous avons un arbre ou un graphe très large (ce qui signifie qu'il y a beaucoup de nœuds frères qui se trouvent au même niveau), nous devons privilégier DFS. Et si nous traitons avec un très grand arbre ou graphe qui a des branches très longues, nous devons privilégier BFS.

La complexité temporelle des deux algorithmes est la même, car nous visitons toujours chaque nœud une seule fois. Mais la complexité spatiale peut être différente selon le nombre de nœuds qui doivent être stockés en mémoire pour chaque implémentation. Donc moins nous avons de nœuds à suivre, mieux c'est.

# Conclusion

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman).

À plus tard !

![Image](https://www.freecodecamp.org/news/content/images/2022/05/6cd09fef66df69d9a3c4c8ab4b8576db.gif align="left")