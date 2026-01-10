---
title: Recherche binaire en Python – Comment coder l'algorithme avec des exemples
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2022-07-18T16:53:41.000Z'
originalURL: https://freecodecamp.org/news/binary-search-in-python-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-pixabay-277593.jpg
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: Python
  slug: python
seo_title: Recherche binaire en Python – Comment coder l'algorithme avec des exemples
seo_desc: 'In our daily lives, we''re constantly searching for information or trying
  to find solutions to problems we encounter.

  When going through search results on the web, we pick the most relevant articles
  or resources that we think will help us.

  Search is s...'
---

Dans notre vie quotidienne, nous recherchons constamment des informations ou essayons de trouver des solutions aux problèmes que nous rencontrons.

Lorsque nous parcourons les résultats de recherche sur le web, nous choisissons les articles ou ressources les plus pertinents que nous pensons pouvoir nous aider.

La recherche fait tellement partie de notre vie parce que nous ne pouvons pas toujours avoir les réponses. Et il existe divers algorithmes qui aident les programmes à fonctionner plus efficacement et à traiter les données plus efficacement.

## Ce que nous allons couvrir dans ce tutoriel

* Qu'est-ce qu'un algorithme de recherche ?
  
* Qu'est-ce qu'un algorithme de recherche binaire ?
  
* Comment fonctionne la recherche binaire – Diviser pour régner
  
* Processus impliqués dans les algorithmes de recherche binaire
  
* Méthodes utilisées dans les algorithmes de recherche binaire
  
* Exemples concrets de recherche binaire
  

## Qu'est-ce qu'un algorithme de recherche ?

Un algorithme de recherche permet de récupérer des éléments à partir de n'importe quelle structure de données. Il compare les données qui arrivent en entrée avec les informations stockées dans sa base de données et produit le résultat. Un exemple est de trouver le numéro de votre meilleur ami dans votre liste de contacts de 1 000 numéros.

Il existe différents types d'algorithmes de recherche. Certains d'entre eux sont :

### Algorithmes de recherche linéaire

Les algorithmes de recherche linéaire sont les plus simples de tous les algorithmes de recherche. Comme leur nom l'indique, ils fonctionnent en séquence.

La recherche linéaire vérifie les éléments d'une liste les uns après les autres pour trouver une valeur clé particulière. Cette valeur clé se trouve parmi d'autres éléments de la liste et l'algorithme retourne la position en parcourant la vérification.

### Algorithme de Dijkstra

L'algorithme du plus court chemin de Dijkstra est utilisé dans des recherches plus avancées. L'algorithme de Dijkstra trace le plus court chemin entre deux nœuds. Ces nœuds sont souvent des réseaux de routes.

Ce type de recherche est utile lorsque vous essayez de trouver des itinéraires sur des cartes. Il vous donne des options basées sur la recherche du chemin le plus court possible.

### Algorithme de recherche binaire

Les algorithmes de recherche binaire sont également connus sous le nom de recherche par moitié d'intervalle. Ils retournent la position d'une valeur cible dans une liste triée.

Ces algorithmes utilisent la technique « diviser pour régner » pour trouver la position de la valeur.

Les algorithmes de recherche binaire et les algorithmes de recherche linéaire sont des exemples d'algorithmes de recherche simples.

Dans la recherche binaire, l'élément du milieu de la liste est trouvé avant d'être comparé avec la valeur clé que vous recherchez. Mais dans la recherche linéaire, les éléments sont pris un par un dans la liste en boucle et comparés avec la valeur clé.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/differences-1.png align="left")

Lors de la recherche binaire, la liste est divisée en deux parties pour obtenir l'élément du milieu : il y a le côté gauche, l'élément du milieu et le côté droit.

Le côté gauche contient des valeurs plus petites que l'élément du milieu et le côté droit contient des valeurs qui sont plus grandes que l'élément du milieu. Cette méthode utilise une liste triée pour fonctionner.

Une liste triée a ses éléments disposés dans un ordre particulier. Pour rendre la recherche efficace pour la recherche binaire, les valeurs de la liste doivent être disposées dans le bon ordre pour satisfaire le processus de recherche. Si une liste a ses valeurs mélangées, elle doit être triée par un algorithme de tri avant d'effectuer la recherche.

### Algorithmes de tri

Les algorithmes de tri acceptent une liste non triée en entrée et retournent une liste avec les éléments disposés dans un ordre particulier (principalement par ordre croissant).

Il existe [différents types d'algorithmes de tri](https://www.freecodecamp.org/news/sorting-algorithms-explained-with-examples-in-python-java-and-c/), comme le tri par insertion, le tri rapide, le tri à bulles et le tri par fusion.

## Comment fonctionne la recherche binaire – Diviser pour régner

Un algorithme de recherche binaire utilise une technique appelée « diviser pour régner » pour accomplir sa tâche. L'algorithme de tri par fusion emploie la même technique pour trier les éléments d'une liste.

Dans les algorithmes de recherche binaire, la méthode « diviser pour régner » fonctionne de cette manière :

* L'algorithme divise la liste en deux parties : le côté gauche et le côté droit, séparés par l'élément du milieu
  
* Il crée une variable pour stocker la valeur de l'élément à rechercher
  
* Il sélectionne l'élément du milieu et le compare avec l'élément à rechercher
  
* Si les éléments comparés sont égaux, le processus se termine
  
* Si ce n'est pas le cas, l'élément du milieu est soit plus grand soit plus petit que l'élément que vous recherchez. Si l'élément du milieu est plus grand, l'algorithme divise la liste et recherche l'élément du côté gauche. Si l'élément du milieu est plus petit, il divise la liste et recherche l'élément du côté droit de la liste.
  

Vous pouvez implémenter cette méthode en utilisant la récursivité ou l'itération dans le processus de recherche binaire.

### Comment fonctionne l'algorithme de recherche binaire – Étape par étape

Tout d'abord, avant d'effectuer la recherche, vous devez trier la liste.

Ensuite, vous créez une variable qui stocke la valeur à rechercher.

Ensuite, la liste est divisée en deux parties. Nous additionnons les premiers et derniers index pour trouver l'index de l'élément du milieu dans la liste.

Lorsque la valeur calculée de l'index de l'élément du milieu est un nombre à virgule (comme 3,45), nous prenons la partie entière comme index.

Ensuite, nous comparons la valeur que nous recherchons et l'élément du milieu.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/process1--2-.png align="left")

### Cas d'utilisation de la recherche binaire

#### Condition 1

Si l'élément du milieu est égal à la valeur à rechercher, la position où se trouve la valeur sera retournée et le processus est terminé.

```python
if middle element == to_search 
    return position of middle element 
*code ends*
```

#### En utilisant l'image ci-dessus comme exemple :

L'élément du milieu = 23, la valeur cible/to\_search = 23. En comparant les deux valeurs, nous voyons qu'elles sont égales des deux côtés. 23 apparaît à l'index 2 dans la liste. C'est la sortie du code et le processus se termine.

#### Condition 2

Si l'élément du milieu n'est pas égal à "to\_search", alors nous vérifions les scénarios suivants :

**Scénario 1** : si l'élément du milieu est plus grand que la valeur à rechercher :

`if middle element > to_search`

* la recherche se déplace vers le côté gauche car les valeurs sont inférieures à l'élément du milieu
  
* la position de l'élément du milieu se décale vers la gauche de 1
  
* new\_position = index(middle element) - 1
  
* une nouvelle recherche commence et la recherche se termine à cette nouvelle position et prend toutes les valeurs avant elle.
  

#### En utilisant l'image ci-dessus comme exemple :

```python
middle element = 23
to_search = 4
if 23 > 4
```

* nous nous déplaçons vers le côté gauche car tous les nombres inférieurs à 23 y sont stockés. index (23) = 2
  
* new\_position = index(23) - 1 = 2-1 = 1
  
* La recherche se terminera à l'index 1 et prendra toutes les autres valeurs avant l'index 1
  

![Image](https://www.freecodecamp.org/news/content/images/2022/07/leftside.png align="left")

En comparant le nouvel élément du milieu (4) à la valeur cible (4), nous voyons qu'ils sont égaux. La recherche est donc terminée et la sortie est la position que "4" occupe dans la liste (qui est l'index 0).

**Scénario 2** : si l'élément du milieu est inférieur à la valeur à rechercher :

`if middle element < to_search`

* la recherche se déplace vers le côté droit car les valeurs sont supérieures à l'élément du milieu
  
* la position de l'élément du milieu se décale vers la droite de 1
  
* new\_position = index(middle element) + 1
  
* une nouvelle recherche commence à la nouvelle position et se termine au dernier index de la liste
  
* toutes les valeurs sont prises de la nouvelle position à la fin de la liste
  

#### En utilisant la première image comme exemple :

```python
middle element = 23 
to_search = 32 
if 23 > 32
```

* nous nous déplaçons vers le côté droit car tous les nombres supérieurs à 23 y sont stockés. index(23) = 2 ,
  
* new\_position = index(23) + 1 = 2+1 = 3
  
* La recherche commencera à l'index 3 et prendra toutes les autres valeurs après l'index 3
  

![Image](https://www.freecodecamp.org/news/content/images/2022/07/rightside.png align="left")

En comparant l'élément du milieu (32) à la valeur cible (32), nous voyons qu'ils sont égaux. La recherche est donc terminée et la sortie est la position que "4" occupe dans la liste (index 4).

## Méthodes utilisées dans les algorithmes de recherche binaire

Il existe deux méthodes qui peuvent implémenter la technique « diviser pour régner » dans la recherche. Ce sont l'itération et la récursivité.

### Qu'est-ce que l'itération ?

Afin d'obtenir des éléments d'un tuple, d'une liste ou d'un dictionnaire, vous parcourez les éléments avec des boucles.

L'itération est une séquence répétée d'instructions pendant l'exécution et elle a un nombre comptable de valeurs. Par exemple, lors du parcours de listes aléatoires, nous parcourons la variable réelle contenant les listes pour obtenir les valeurs.

#### Implémentation du code pour la recherche binaire avec itération

Voici le code :

```python
def binary_search(list_num , to_search):
    first_index = 0
    size = len(list_num)
    last_index = size - 1
    mid_index = (first_index + last_index) // 2
    # print(mid_index)
    mid_element = list_num[mid_index]
    # print(mid_element)

    is_found = True
    while is_found:
        if first_index == last_index:
            if mid_element != to_search:
                is_found = False
                return " Does not appear in the list"

        elif mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"

        elif mid_element > to_search:
            new_position = mid_index - 1
            last_index = new_position
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"

        elif mid_element < to_search:
            new_position = mid_index + 1
            first_index = new_position
            last_index = size - 1
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"



list_container = [16 , 18 , 20 , 50 , 60 , 81 , 84 , 89]
print(binary_search(list_container , 81))
print(binary_search(list_container , 10))
```

Voyons maintenant ce qui se passe ici :

* Tout d'abord, nous passons une liste et une valeur à rechercher (to\_search) en entrée à une fonction.
  
* Dans la fonction, nous créons une variable nommée first index et lui attribuons "0". Le premier index dans une liste est toujours "0".
  
* Ensuite, nous créons quatre noms de variables : "size" pour stocker la longueur de la liste, "last\_index" pour stocker l'index du dernier élément, "mid\_index" pour stocker l'opération de recherche de l'index de l'élément du milieu, et "mid\_element" pour stocker l'élément du milieu obtenu à partir de la liste en utilisant l'index du milieu comme position.
  
* Ensuite, nous introduisons une boucle while pour faire fonctionner les conditions en répétition. Au-dessus de la boucle while, nous créons une variable nommée "is\_found" et la définissons sur "True". Cette condition vérifie si l'"élément à rechercher" est trouvé ou non.
  
* Dans la boucle while, nous vérifions toutes les conditions. La première condition est de vérifier si l'élément du milieu et la variable "to\_search" sont égaux. Si ils sont égaux, la position de l'élément sera retournée.
  
* Ensuite, nous vérifions la deuxième condition (si l'élément du milieu != élément à rechercher) qui nous mène aux deux scénarios :  
  – si l'élément du milieu est plus grand que l'élément à rechercher, la nouvelle position se décalera une fois vers la gauche. La recherche commencera à partir du premier index et se terminera à la nouvelle position qui est le nouvel index de fin.  
  – Si l'élément du milieu est plus petit que l'élément à rechercher, la nouvelle position se décalera une fois vers la droite. La recherche commencera à partir de la nouvelle position comme nouvel index de début et se terminera à l'index de fin.
  

À la fin de ces scénarios, nous vérifions si le nouvel élément du milieu est le même que l'élément à rechercher. Si c'est le même, la position de l'élément sera retournée. Si ce n'est pas le cas, les conditions sont vérifiées jusqu'à ce que les valeurs soient égales.

Pour la gestion des erreurs, disons que nous voulons rechercher une valeur qui n'apparaît pas dans la liste. Si nous terminons aux deux conditions, la boucle continuera à fonctionner et pourrait éventuellement faire planter le système.

Pour attraper l'erreur, nous définissons une condition pour vérifier si le premier index est égal au dernier index. Ensuite, nous vérifions si l'élément du milieu est égal à l'élément à rechercher. Si ce n'est pas égal, "is found" sera "False". Lorsque vous exécutez cela, cela montre un tableau vide. Dans mon code, la sortie est une déclaration.

La dernière étape consiste à appeler la fonction et le résultat est affiché.

**Et voici les résultats :**

Si l'élément est dans la liste, la sortie est la position.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-194.png align="left")

Si l'élément n'est pas dans la liste, la sortie est une déclaration comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-195.png align="left")

### Qu'est-ce que la récursivité ?

Une fonction est dite récursive si elle fait référence à elle-même ou à des termes précédents pour résoudre une tâche.

Une fonction récursive est répétitive et elle est exécutée en séquence. Elle commence par un problème complexe et décompose les choses en une forme plus simple.

#### Implémentation du code pour la recherche binaire avec récursivité

Avec la récursivité, c'est un peu plus simple et nécessite moins de code. Voici à quoi cela ressemble :

```python
def binary_search(list_num, first_index, last_index, to_search):
    if last_index >= first_index:
      
        mid_index = (first_index + last_index) // 2
        mid_element = list_num[mid_index]
      
 
        if mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"
 
        elif mid_element > to_search:
            new_position = mid_index - 1
            # new last index is the new position
            return binary_search(list_num, first_index, new_position, to_search)
 
        elif mid_element < to_search:
            new_position = mid_index + 1
             # new first index is the new position
            return binary_search(list_num, new_position, last_index, to_search)
 
    else:
        return " Does not appear in the list"
      
list_container = [ 1, 9, 11, 21, 34, 54, 67, 90 ]
search = 34
first = 0
last= len(list_container) - 1
 
print(binary_search(list_container,first,last,search))
```

* Tout d'abord, une fonction accepte quatre entrées : le premier index, le dernier index, la liste et to\_search (élément à rechercher).
  
* Ensuite, nous vérifions si la valeur du dernier index est supérieure ou égale à la valeur du premier index. Si la condition est vraie, nous attribuons l'opération de recherche de l'index de l'élément du milieu au nom de la variable "mid\_index". Ensuite, l'élément du milieu est obtenu à partir de la liste en utilisant l'index du milieu comme position.
  
* Nous créons une instruction "if" sous le premier bloc "if" pour vérifier si l'élément du milieu et la variable "to\_search" sont égaux. Si ils sont égaux, la position de l'élément sera retournée.
  
* Ensuite, nous vérifions la deuxième condition, (si l'élément du milieu != élément à rechercher) qui nous mène à deux scénarios :  
  – si l'élément du milieu est plus grand que l'élément à rechercher, la nouvelle position se décalera une fois vers la gauche. La recherche commencera à partir du premier index et se terminera à la nouvelle position. Nous retournons la fonction et passons la nouvelle position comme valeur du dernier index.  
  – si l'élément du milieu est plus petit que l'élément à rechercher, la nouvelle position se décalera une fois vers la droite. La recherche commencera à partir de la nouvelle position et se terminera au dernier index. Nous retournons la fonction et passons la nouvelle position comme valeur du premier index.
  
* La dernière condition sera au même niveau d'indentation que la première instruction "if". Si le to\_search n'est pas dans la liste, il retournera une déclaration
  

La dernière étape consiste à appeler la fonction et le résultat est affiché.

**Et voici les résultats :**

Si l'élément est dans la liste, la sortie est la position :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-196.png align="left")

Si l'élément n'est pas dans la liste, la sortie est une déclaration :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-197.png align="left")

## Exemples concrets de recherche binaire

Vous ne vous en rendez peut-être pas compte, mais nous effectuons des recherches binaires tout le temps. Voici quelques exemples de la manière dont vous pourriez l'utiliser ou la rencontrer dans votre vie quotidienne ou votre travail :

* Rechercher un mot dans un dictionnaire
  
* rechercher un manuel de littérature dans une section de littérature dans une bibliothèque
  
* rechercher un élément dans une liste triée
  
* rechercher des étudiants plus grands que 5 pieds 3 pouces dans une ligne d'étudiants disposés selon leur taille.
  

## Conclusion

À la fin de cet article, vous devriez être familiarisé avec le fonctionnement des algorithmes de recherche binaire et comment les implémenter en code.

Ce n'est pas grave si vous n'avez pas tout compris d'un coup – donnez-vous un peu de temps et pratiquez. Si vous rencontrez des erreurs ou avez des questions, vous pouvez me contacter sur [Twitter](https://twitter.com/HeritageAlabi1).













