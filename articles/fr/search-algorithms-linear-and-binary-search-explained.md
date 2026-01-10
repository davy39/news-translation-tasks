---
title: Algorithmes de recherche – Implémentation de code et analyse de complexité
  pour la recherche linéaire et la recherche binaire
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-01-11T17:21:54.000Z'
originalURL: https://freecodecamp.org/news/search-algorithms-linear-and-binary-search-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/searching.png
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
- name: binary search
  slug: binary-search
- name: Computer Science
  slug: computer-science
seo_title: Algorithmes de recherche – Implémentation de code et analyse de complexité
  pour la recherche linéaire et la recherche binaire
seo_desc: 'Search algorithms are a fundamental computer science concept that you should
  understand as a developer. They work by using a step-by-step method to locate specific
  data among a collection of data.

  In this article, we''ll learn how search algorithms wo...'
---

**Les algorithmes de recherche** sont un concept fondamental en informatique que vous devriez comprendre en tant que développeur. Ils fonctionnent en utilisant une méthode étape par étape pour localiser des données spécifiques parmi une collection de données.

Dans cet article, nous allons apprendre comment fonctionnent les algorithmes de recherche en examinant leurs implémentations en Java et Python.

## Qu'est-ce qu'un algorithme de recherche ?

Selon Wikipedia, un algorithme de recherche est :

> *Tout algorithme qui résout le problème de recherche, à savoir, récupérer des informations stockées dans une structure de données, ou calculées dans l'espace de recherche d'un domaine de problème, soit avec des valeurs discrètes ou continues.*

Les algorithmes de recherche sont conçus pour vérifier ou récupérer un élément à partir de toute structure de données où cet élément est stocké. Ils recherchent une cible (clé) dans l'espace de recherche.

## Types d'algorithmes de recherche

Dans cet article, nous allons discuter de deux types importants d'algorithmes de recherche :

1. **Recherche linéaire ou séquentielle**

2. **Recherche binaire**

Examinons ces deux types en détail avec des exemples, des implémentations de code et une analyse de la complexité temporelle.

## Recherche linéaire ou séquentielle

Cet algorithme fonctionne en itérant séquentiellement à travers tout le tableau ou la liste à partir d'une extrémité jusqu'à ce que l'élément cible soit trouvé. Si l'élément est trouvé, il retourne son index, sinon -1.

Examinons maintenant un exemple et essayons de comprendre comment cela fonctionne :

```python
arr = [2, 12, 15, 11, 7, 19, 45]
```

Supposons que l'élément cible que nous voulons rechercher est `7`.

### Approche pour la recherche linéaire ou séquentielle

* Commencez avec l'index 0 et comparez chaque élément avec la cible

* Si la cible est trouvée égale à l'élément, retournez son index

* Si la cible n'est pas trouvée, retournez -1

### **Implémentation de code**

Examinons maintenant comment nous implémenterions ce type d'algorithme de recherche dans quelques langages de programmation différents.

#### Recherche linéaire ou séquentielle en Java

```java
package algorithms.searching;

public class LinearSearch {
    public static void main(String[] args) {
        int[] nums = {2, 12, 15, 11, 7, 19, 45};
        int target = 7;
        System.out.println(search(nums, target));

    }

    static int search(int[] nums, int target) {
        for (int index = 0; index < nums.length; index++) {
            if (nums[index] == target) {
                return index;
            }
        }
        return -1;
    }
}
```

#### Recherche linéaire ou séquentielle en Python

```python
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

if __name__ == '__main__':
    nums = [2, 12, 15, 11, 7, 19, 45]
    target = 7
    print(search(nums, target))
```

### **Analyse de la complexité temporelle**

**Le meilleur cas** se produit lorsque l'élément cible est le premier élément du tableau. Le nombre de comparaisons, dans ce cas, est 1. Donc, la complexité temporelle est `O(1)`.

**Le cas moyen** : En moyenne, l'élément cible sera quelque part au milieu du tableau. Le nombre de comparaisons, dans ce cas, sera N/2. Donc, la complexité temporelle sera `O(N)` (la constante étant ignorée).

**Le pire cas** se produit lorsque l'élément cible est le dernier élément du tableau ou n'est pas dans le tableau. Dans ce cas, nous devons parcourir tout le tableau, et donc le nombre de comparaisons sera N. Donc, la complexité temporelle sera `O(N)`.

## Recherche binaire

Ce type d'algorithme de recherche est utilisé pour trouver la position d'une valeur spécifique contenue **dans un tableau trié**. L'algorithme de recherche binaire fonctionne sur le principe de diviser pour régner et il est considéré comme le meilleur algorithme de recherche car il est plus rapide à exécuter.

Prenons maintenant un tableau trié comme exemple et essayons de comprendre comment cela fonctionne :

```python
arr = [2, 12, 15, 17, 27, 29, 45]
```

Supposons que l'élément cible à rechercher est `17`.

### **Approche pour la recherche binaire**

* Comparez l'élément cible avec l'élément du milieu du tableau.

* Si l'élément cible est plus grand que l'élément du milieu, alors la recherche continue dans la moitié droite.

* Sinon, si l'élément cible est plus petit que la valeur du milieu, la recherche continue dans la moitié gauche.

* Ce processus est répété jusqu'à ce que l'élément du milieu soit égal à l'élément cible, ou que l'élément cible ne soit pas dans le tableau.

* Si l'élément cible est trouvé, son index est retourné, sinon -1 est retourné.

### Implémentation de code

#### Recherche binaire en Java

```java
package algorithms.searching;

public class BinarySearch {
    public static void main(String[] args) {
        int[] nums = {2, 12, 15, 17, 27, 29, 45};
        int target = 17;
        System.out.println(search(nums, target));
    }

    static int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] > target)
                end = mid - 1;
            else if (nums[mid] < target)
                start = mid + 1;
            else
                return mid;
        }
        return -1;
    }
}
```

#### Recherche binaire en Python

```python
def search(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start + (end-start)//2


        if nums[mid] > target:
            end = mid-1
        elif nums[mid] < target:
            start = mid+1
        else:
            return mid

    return -1


if __name__ == '__main__':
    nums = [2, 12, 15, 17, 27, 29, 45]
    target = 17
    print(search(nums, target))
```

### **Analyse de la complexité temporelle**

**Le meilleur cas** se produit lorsque l'élément cible est l'élément du milieu du tableau. Le nombre de comparaisons, dans ce cas, est 1. Donc, la complexité temporelle est `O(1)`.

**Le cas moyen** : En moyenne, l'élément cible sera quelque part dans le tableau. Donc, la complexité temporelle sera `O(logN)`.

**Le pire cas** se produit lorsque l'élément cible n'est pas dans la liste ou s'il est éloigné de l'élément du milieu. Donc, la complexité temporelle sera `O(logN)`.

### Comment calculer la complexité temporelle :

Disons que l'itération dans la recherche binaire se termine après **k** itérations.

À chaque itération, le tableau est divisé par deux. Donc, disons que la longueur du tableau à une itération quelconque est **N**.

À **l'itération 1**,

```markdown
Longueur du tableau = N
```

À **l'itération 2**,

```markdown
Longueur du tableau = N/2
```

À **l'itération 3**,

```markdown
Longueur du tableau = (N/2)/2 = N/2^2
```

À **l'itération k**,

```markdown
Longueur du tableau = N/2^k
```

De plus, nous savons qu'après k divisions, la **longueur du tableau devient 1** : Longueur du tableau = **N/2^k = 1** => **N = 2^k**

Si nous appliquons une fonction logarithme des deux côtés : **log2 (N) = log2 (2^k)** => **log2 (N) = k log2 (2)**

Comme **(log_a (a) = 1)**
Par conséquent, => **k = log2 (N)**

Nous pouvons maintenant voir pourquoi la complexité temporelle de la recherche binaire est log2 (N).

Vous pouvez également visualiser les deux algorithmes ci-dessus à l'aide de l'outil simple construit par [Dipesh Patil](https://www.linkedin.com/in/dipesh-patil/) - [Algorithms Visualizer](https://dipeshpatil.github.io/algorithms-visualiser/#/searching).

## Recherche binaire agnostique d'ordre

Supposons que nous devons trouver un élément cible dans un tableau trié. Nous savons que le tableau est trié, mais nous ne savons pas s'il est trié par ordre croissant ou décroissant.

### **Approche pour la recherche binaire agnostique d'ordre**

L'implémentation est similaire à la recherche binaire, sauf que nous devons identifier si le tableau est trié par ordre croissant ou décroissant. Cela nous permet ensuite de prendre la décision de continuer la recherche dans la moitié gauche du tableau ou dans la moitié droite du tableau.

* Nous comparons d'abord la cible avec l'élément du milieu

* Si le tableau est trié par ordre croissant et que la cible est inférieure à l'élément du milieu **OU** le tableau est trié par ordre décroissant et que la cible est supérieure à l'élément du milieu, alors nous continuons la recherche dans la moitié inférieure du tableau en définissant `end=mid-1`.

* Sinon, nous effectuons la recherche dans la moitié supérieure du tableau en définissant `start=mid+1`

La seule chose que nous devons faire est de déterminer si le tableau est trié par ordre croissant ou décroissant. Nous pouvons facilement le découvrir en comparant les premier et dernier éléments du tableau.

```markdown
if arr[0] < arr[arr.length-1]
    le tableau est trié par ordre croissant 
else
    le tableau est trié par ordre décroissant
```

### **Implémentation de code**

#### Recherche binaire agnostique d'ordre en Java

```java
package algorithms.searching;

public class OrderAgnosticBinarySearch {
    public static void main(String[] args) {
        int[] nums1 = {-1, 2, 4, 6, 7, 8, 12, 15, 19, 32, 45, 67, 99};
        int[] nums2 = {99, 67, 45, 32, 19, 15, 12, 8, 7, 6, 4, 2, -1};
        int target = -1;
        System.out.println(search(nums1, target));
        System.out.println(search(nums2, target));
    }

    static int search(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;

        boolean isAscending = arr[start] < arr[end];

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (target == arr[mid])
                return mid;

            if (isAscending) {
                if (target < arr[mid]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else {
                if (target < arr[mid]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        return -1;
    }


}
```

#### Recherche binaire agnostique d'ordre en Python

```python
def search(nums, target):
    start = 0
    end = len(nums)-1

    is_ascending = nums[start] < nums[end]

    while start <= end:
        mid = start + (end-start)//2

        if target == nums[mid]:
            return mid

        if is_ascending:
            if target < nums[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if target < nums[mid]:
                start = mid+1
            else:
                end = mid-1

    return -1


if __name__ == '__main__':
    nums1 = [-1, 2, 4, 6, 7, 8, 12, 15, 19, 32, 45, 67, 99]
    nums2 = [99, 67, 45, 32, 19, 15, 12, 8, 7, 6, 4, 2, -1]
    target = -1
    print(search(nums1, target))
    print(search(nums2, target))
```

### **Analyse de la complexité temporelle**

Il n'y aura aucun changement dans la complexité temporelle, donc elle sera la même que pour la recherche binaire.

# **Conclusion**

Dans cet article, nous avons discuté de deux des algorithmes de recherche les plus importants ainsi que de leurs implémentations de code en Python et Java. Nous avons également examiné leur analyse de la complexité temporelle.

Merci d'avoir lu !

[Abonnez-vous à ma newsletter](https://newsletter.ashutoshkrris.tk)