---
title: Recherche binaire – Algorithme et complexité temporelle expliqués
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2023-07-12T14:26:58.000Z'
originalURL: https://freecodecamp.org/news/binary-search-algorithm-and-time-complexity-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/cover-img-search.png
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: Python
  slug: python
seo_title: Recherche binaire – Algorithme et complexité temporelle expliqués
seo_desc: 'When working with arrays, you’ll often have to search through them to check
  if they contain a target element.

  You can always run a sequential search—scanning the array from the beginning to
  the end—on the array. But if the array is sorted, running th...'
---

Lorsque vous travaillez avec des tableaux, vous devrez souvent les parcourir pour vérifier s'ils contiennent un élément cible.

Vous pouvez toujours effectuer une recherche séquentielle—en scannant le tableau du début à la fin—sur le tableau. Mais si le tableau est trié, exécuter l'algorithme de recherche binaire est beaucoup plus efficace.

Apprenons comment fonctionne la recherche binaire, sa complexité temporelle, et codons une implémentation simple en Python.

## Comment fonctionne la recherche linéaire ?

Nous commencerons notre discussion avec la **recherche linéaire** ou **séquentielle**.

Supposons que nous avons une séquence non triée de nombres `nums`. Étant donné ce tableau `nums`, vous devez vérifier si la `cible` est présente dans `nums`. Vous n'avez pas d'information sur le fait que `nums` soit trié ou non.

La seule façon de procéder est donc de scanner le tableau de manière linéaire, en commençant par le premier élément—jusqu'à ce que vous trouviez une correspondance.

Vous pouvez parcourir l'ensemble du tableau pour vérifier si l'élément à l'index `i` correspond à la `cible`. Une fois que vous trouvez une correspondance, vous pouvez sortir de la boucle.

Remarquez que dans le pire des cas, vous devrez scanner l'ensemble du tableau et avoir de la chance de trouver une correspondance au dernier index. Ou vous aurez épuisé le tableau—sans trouver de correspondance—indiquant que l'élément n'est pas présent dans le tableau.

Supposons que le tableau ait `n` éléments. Parce que vous devez scanner l'ensemble du tableau—dans le pire des cas—l'algorithme de recherche linéaire a une complexité temporelle de O(n).

Voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-66.png)
_Exemple de recherche linéaire | Image de l'auteur_

Mais lorsque vous ne savez rien de la séquence, c'est le mieux que vous puissiez faire. *Ainsi, la recherche linéaire ou séquentielle est la meilleure option lorsque vous recherchez dans des séquences non triées.*

### Comment la recherche linéaire fonctionne en Python

La fonction `linear_search` prend en entrée un tableau `nums` et une `cible` à rechercher. Elle parcourt ensuite le tableau de manière séquentielle pour vérifier si `cible` est présente dans `nums` :

```python
def linear_search(nums,target):
  for num in nums:
    if num == target:
      return True
  return False
```

Voici quelques exemples de sorties :

```python
nums = [14,21,27,30,36,2,5,7,11]
target = 27

print(linear_search(nums,target))
# Sortie : True

target = 100
print(linear_search(nums,target))
# Sortie : False
```

## Comment fonctionne la recherche binaire ?

Considérons maintenant la séquence `nums` avec `n` éléments triés par ordre croissant. Pour tout index valide `k`, ce qui suit est vrai pour l'élément `a_k` à l'index `k` :

> Les éléments aux indices 0, 1, 2, ..., (k-1) sont tous inférieurs ou égaux à `a_k`. Et tous les éléments aux indices (k+1) à (n-1) sont supérieurs ou égaux à `a_k`.

Avec cette information, vous n'avez plus besoin d'effectuer un scan linéaire. Vous pouvez le faire beaucoup plus rapidement avec une recherche binaire.

Nous avons un tableau trié `nums` et une `cible`. Soit mid l'index central du tableau et `nums[mid]` l'élément à l'index central. Voici comment fonctionne l'algorithme de recherche binaire :

* Vérifiez si `nums[mid]` est égal à la `cible`. Si c'est le cas, nous avons déjà trouvé une correspondance—dès la première étape—et la recherche se termine.
* Si `nums[mid]` > `cible`, vous n'avez besoin de rechercher que dans la _moitié gauche_ du tableau. Même lorsque vous recherchez dans le sous-tableau gauche, vous pouvez utiliser le même algorithme de recherche binaire.
* Si `nums[mid]` < `cible`, vous pouvez ignorer tous les éléments jusqu'à l'élément central et ne considérer que la _moitié droite_ du tableau.

Remarquez que nous avons ici une relation de récurrence. D'abord, nous commençons par exécuter l'algorithme de recherche binaire sur le tableau avec n éléments. Si nous ne trouvons pas la cible dès la première étape, nous exécutons une recherche binaire sur le sous-tableau de taille au plus n/2 éléments.

Si nous obtenons un tableau vide ou un tableau avec un élément qui n'est _pas_ la `cible`, nous concluons que la cible n'existe pas dans le tableau `nums`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-65.png)
_Exemple de recherche binaire | Image de l'auteur_

### Comment implémenter la recherche binaire en Python

Voici une implémentation récursive de la recherche binaire en Python :

```python
def binary_search(nums,target,low,high):
  if low > high:
    return False
  else:
    mid = (low + high)//2
    if nums[mid] == target:
      return True
    elif nums[mid] < target:
      return binary_search(nums,target,mid+1,high)
    else:
      return binary_search(nums,target,low,mid-1)
```

Avec quelques exécutions d'exemple de la fonction `binary_search` :

```python
nums = [2,5,7,11,14,21,27,30,36]
target = 27

print(binary_search(nums,target,0,len(nums)-1))
# Sortie : True

target = 38
print(binary_search(nums,target,0,len(nums)-1))
# Sortie : False
```

## Quelle est la complexité temporelle de la recherche binaire ?

Dans la recherche binaire, nous savons que *l'espace de recherche est réduit de moitié* à chaque étape et cela nous guide dans le calcul de la complexité temporelle.

Pour un tableau avec `n` éléments, nous vérifions si l'élément central correspond à la `cible`. Si c'est le cas, nous retournons `True` et terminons la recherche.

Mais si l'élément central ne correspond pas à la `cible`, nous effectuons une recherche binaire sur un sous-tableau de taille au plus `n/2`. À l'étape suivante, nous devons rechercher dans un tableau de taille au plus `n/4`. Et nous continuons cela de manière récursive jusqu'à ce que nous puissions prendre une décision en temps constant (quand le sous-tableau est vide).

À l'étape `k`, nous devons rechercher dans un tableau de taille au plus `n/(2^k)`. Et nous devons trouver le plus petit `k` pour lequel nous n'avons plus de sous-tableau à rechercher.

Mathématiquement :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-68.png)

La complexité temporelle de la recherche binaire est donc **O(logn)**. Cela est beaucoup plus efficace que le temps linéaire O(n), surtout pour les grandes valeurs de n.

Par exemple, si le tableau a 1000 éléments. 2^(10) = 1024. Alors que l'algorithme de recherche binaire se terminera en environ 10 étapes, la recherche linéaire prendra mille étapes dans le pire des cas.

## Conclusion

Et c'est tout. J'espère que vous avez trouvé cette introduction à la recherche binaire utile ! Vous rencontrerez souvent des questions impliquant la recherche binaire lors des entretiens de codage.

Si vous vous préparez pour des entretiens de codage, consultez [10 Common Coding Interview Questions [Solved]](https://youtu.be/Peq4GCPNC5c) sur la chaîne YouTube de freeCodeCamp.