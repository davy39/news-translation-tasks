---
title: Comment trier une liste de manière récursive en Python
subtitle: ''
author: P S Mohammed Ali
co_authors: []
series: null
date: '2022-09-23T14:35:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-recursively-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/max-harlynking-_QcLpud-gD0-unsplash-1.jpg
tags:
- name: algorithms
  slug: algorithms
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Recursion
  slug: recursion
seo_title: Comment trier une liste de manière récursive en Python
seo_desc: 'When you want to sort a list or array in Python, there are many sorting
  algorithms you can use.

  Some use looping concepts like Insertion Sort, Bubble Sort, and Selection Sort.
  On the other hand, you can also sort the same list or array using Merge So...'
---

Lorsque vous souhaitez trier une liste ou un tableau en Python, il existe de nombreux algorithmes de tri que vous pouvez utiliser.

Certains utilisent des concepts de boucle comme l'Insertion Sort, le Bubble Sort et le Selection Sort. D'un autre côté, vous pouvez également trier la même liste ou le même tableau en utilisant le Merge Sort à l'aide de la récursion.

Dans cet article, vous apprendrez comment fonctionne l'algorithme Merge Sort. Vous apprendrez également comment la récursion joue un rôle important dans le Merge Sort.

## Comment fonctionne la récursion

Comme condition préalable, nous allons d'abord comprendre comment fonctionne la récursion, car c'est la colonne vertébrale de l'algorithme Merge Sort.

Tout d'abord, vous devez savoir qu'une fonction récursive est une fonction qui s'appelle elle-même jusqu'à ce qu'elle atteigne le résultat souhaité.

Maintenant, à moins que vous ne définissiez une condition pour arrêter ce processus, il continuera indéfiniment – ou jusqu'à ce que votre code JS génère une erreur. C'est ce qu'on appelle un cas de base, et cela empêchera la fonction de s'appeler elle-même lorsque sa condition est remplie.

Maintenant que vous connaissez les bases de la récursion, entrons un peu dans les détails et comprenons comment elle fonctionne sous le capot :

En général, la récursion fonctionne sur la base d'un concept appelé le Principe de récurrence (PMI). En termes simples, le PMI est une technique utilisée pour prouver certaines affirmations à partir d'un ensemble de base d'affirmations prouvées.

Habituellement, ce processus comporte trois étapes.

Prouvons que la formule de la somme des n premiers entiers naturels est `P(n)= n*(n+1)/2` en utilisant le PMI :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/123.PNG align="left")

*Pour prouver que P(n) est vrai*

Étape 1 : La première étape est également connue sous le nom de **cas de base**. Au cours de cette étape, vous spécifiez les affirmations prouvées. Universellement, nous savons que la somme du premier entier naturel est `1`. Considérons cela comme le membre de gauche de l'équation (LHS).

Lorsque nous appliquons `n = 1` dans la formule, nous obtenons `p(1) = 1*(1+1)/2 => 1` comme membre de droite (RHS).

![Image](https://www.freecodecamp.org/news/content/images/2022/09/1234.PNG align="left")

*Application de 1 dans la formule*

Cela signifie que LHS = RHS. Cette étape confirme qu'il s'agit d'un cas de base valide.

Étape 2 : Cette étape est connue sous le nom d'**hypothèse de récurrence**. Dans cette étape, nous supposons simplement que cette formule est vraie pour un certain entier `k` où `1 < k < n`. Ainsi, nous remplaçons k dans la formule et nous obtenons `p(k) = k*(k+1)/2` :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/12345.PNG align="left")

*Étape d'hypothèse de récurrence pour une certaine valeur entière k*

Étape 3 : Cette étape est connue sous le nom d'**étape de récurrence** (ou hérédité). À ce stade, nous devons prouver que cela fonctionnera pour l'entier `k+1`.

Lorsque nous remplaçons `k + 1` dans la formule et que nous le considérons comme le LHS, nous obtenons ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/125.PNG align="left")

*Affirmation du membre de gauche pour P(k+1)*

Pour le RHS, nous savons que la somme des entiers naturels jusqu'à l'entier `k+1` est égale à la somme des entiers naturels jusqu'à l'entier `k` plus le `(k+1)`-ième entier. Nous pouvons l'écrire comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/21.PNG align="left")

*La somme de k+1 entiers est égale au (k+1)-ième entier plus la somme de k entiers*

L'équation ci-dessus peut être réécrite comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/22.PNG align="left")

*la somme de k entiers naturels est réécrite comme p(k) à partir de l'étape 2*

À ce stade, nous connaissons la valeur de p(k) d'après l'étape 2 (hypothèse de récurrence). Lorsque nous remplaçons la valeur de p(k), nous obtenons ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/23.PNG align="left")

*Remplacement de p(k) de l'étape 2*

Nous pouvons prendre le dénominateur commun et simplifier l'équation, et nous obtenons :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/37.PNG align="left")

*Simplification de l'équation*

En comparant le LHS et le RHS, nous obtenons le même résultat et nous avons prouvé que cette formule fonctionne pour `k+1` entiers.

De plus, lorsque nous remplaçons `k+1` par `n`, nous obtenons le résultat final suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/45.PNG align="left")

*Remplacement de k+1 par n*

Nous avons prouvé que la formule pour n entiers naturels est n*(n+1)/2.

En observant toutes les étapes du PMI, nous avons fait une simple supposition à l'étape 2 et, par conséquent, nous avons prouvé l'affirmation à l'étape 3.

C'est ainsi que fonctionne la récursion : nous initialisons un cas de base pour un problème au début de la fonction et nous supposons que cette fonction fonctionne pour de petites valeurs du même problème. Ensuite, comme étape finale, nous prouvons que cela fonctionne pour le problème existant.

## Comment fonctionne l'algorithme Merge Sort

L'algorithme Merge Sort fonctionne en divisant une liste non triée en deux moitiés. Vous appelez ensuite le Merge Sort sur chacune de ces deux parties.

Puisque nous savons que la récursion fonctionne sur la base du principe de récurrence (PMI), nous supposons que les listes plus petites sont triées lors de l'appel du Merge Sort sur ces 2 listes plus petites.

> **Note :** Avant d'appeler la récursion sur des listes plus petites, il est crucial de définir un cas de base pour la fonction car il sert de point d'arrêt pour l'appel récursif.

Ici, le cas de base pour le Merge Sort sera si la longueur de la liste est de 1. Dans ce cas (si la longueur est de 1, cela signifie qu'il n'y a qu'un seul élément dans la liste), la liste est déjà triée, nous n'avons donc qu'à renvoyer la liste telle quelle.

Pour plus de clarté, prenons un exemple et implémentons le Merge Sort sur une liste non triée.

```python
my_list = [3,8,2,7,1,4,5]
```

Dans le code ci-dessus, vous pouvez voir que la variable `my_list` contient une liste qui n'est pas triée.

Maintenant, puisque la longueur de `my_list` n'est pas 1, nous ne pouvons pas supposer qu'elle est triée. Nous appelons donc le Merge Sort sur la première moitié `list1 = [3,8,2]` et appelons également le Merge Sort sur la seconde moitié `list2 = [7,1,4,5]`.

Nous supposons que `list1` et `list2` sont triées conformément à l'étape de récurrence. Maintenant, la liste ressemble à `list1 = [2,3,8]` et `list2 = [1,4,5,7]`. Il ne nous reste plus qu'à fusionner ces deux listes triées en une seule en utilisant la technique des deux pointeurs.

Afin de combiner et de trier les deux petites listes triées, nous prenons 2 pointeurs, pointant au début de chaque liste.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/56.PNG align="left")

*Pointeurs à l'index de départ de la liste et liste vide pour ajouter la nouvelle liste lors de la comparaison*

![Image](https://www.freecodecamp.org/news/content/images/2022/09/333.PNG align="left")

*Étape intermédiaire dans le processus de comparaison des valeurs des pointeurs*

Nous comparons la valeur à chaque endroit pointé par le pointeur, et celle qui est la plus petite est ajoutée ensuite dans la liste finale. Ensuite, nous déplaçons le pointeur vers l'index suivant.

Après avoir parcouru ce processus, lorsque nous atteignons le premier index final (dans l'une des deux boucles que nous joignons), nous arrêtons la boucle. Ensuite, nous ajoutons toutes les valeurs de l'autre liste (s'il en reste) à la liste finale.

En utilisant cette technique, nous pouvons fusionner et trier les deux petites listes pré-triées.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Blank-diagram--1-.png align="left")

*Flux de travail du Merge Sort*

Lorsque nous utilisons la récursion, we supposons qu'elle fonctionne lorsque nous appelons la même fonction pour un problème plus petit. Cette supposition provient de l'étape de l'hypothèse de récurrence dans le PMI.

Ainsi, lorsque nous déclarons le cas de base pour le problème, nous supposons de même que la fonction renverra la réponse correcte pour les problèmes plus petits. Tout ce que nous avons à faire est de prouver que cela fonctionne aussi pour les problèmes plus grands.

Dans cet algorithme, nous avons déclaré que le cas de base est qu'une liste de longueur 1 est triée. Dans l'étape de l'hypothèse de récurrence, nous avons supposé que l'algorithme fonctionnerait pour la moitié de la liste. Dans la troisième étape, nous avons simplement fusionné la liste triée et prouvé que cela fonctionnerait sur une liste plus grande.

## Code Python pour l'algorithme Merge Sort

```python
def merge_sort(my_list):

	# Cas de base
    if len(my_list) <= 1:
        return my_list
   
    list_1 = my_list[0:len(my_list) // 2]
    list_2 = my_list[len(my_list) // 2:]
    
   	# Étape de récurrence
    ans_1 = merge_sort(list_1)
    ans_2 = merge_sort(list_2)
    
    # Tri et fusion de deux listes triées
    sort_list = sort_two_list(ans_1, ans_2)
    return sort_list



# Fonction séparée pour trier et fusionner 2 listes triées
def sort_two_list(list_1, list_2):
    final_list = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            final_list.append(list_1[i])
            i += 1
            continue
        final_list.append(list_2[j])
        j += 1

    while i < len(list_1):
        final_list.append(list_1[i])
        i = i + 1
        
    while j < len(list_2):
        final_list.append(list_2[j])
        j = j + 1
        
    return final_list


my_list = [3, 8, 2, 7, 1, 4, 5]
ans = merge_sort(my_list)
print(ans)
# affiche [1, 2, 3, 4, 5, 7, 8]
```

Comme vous le voyez dans le code ci-dessus, j'ai implémenté deux fonctions distinctes pour trier et fusionner les deux listes triées. Cela permet une meilleure lisibilité et facilite les révisions de code.

Le main drawback du Merge Sort est qu'il utilise plus d'espace. En effet, à chaque appel récursif, une nouvelle liste est créée et la récursion est appelée sur cette nouvelle liste. Ainsi, la complexité spatiale pour le pire des cas est `O(n)` et la complexité temporelle est `O(n log n)`.

## Conclusion

Le Merge Sort est assez rapide pour trier une liste de manière récursive du point de vue de la complexité temporelle. Il est utile pour compter les inversions dans les listes et il est plus largement utilisé pour les applications de tri externe que d'autres algorithmes de tri.

Bonne programmation...

Merci de votre lecture. Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis.