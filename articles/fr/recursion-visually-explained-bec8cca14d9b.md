---
title: Consultez mon guide visuel de la récursivité (car une image vaut 1 000 mots)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-27T20:34:35.000Z'
originalURL: https://freecodecamp.org/news/recursion-visually-explained-bec8cca14d9b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PPXnzjpCdxuMiz9OJdhe8w.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Consultez mon guide visuel de la récursivité (car une image vaut 1 000
  mots)
seo_desc: 'By Jerry Muzsik

  In this article, I will explain recursion (almost) completely with visual representations.
  I’ll show, rather than explain, how each recursive function call interacts with
  the entirety of the initial function invocation — in other word...'
---

Par Jerry Muzsik

Dans cet article, je vais expliquer la récursivité (presque) entièrement avec des représentations visuelles. Je vais montrer, plutôt qu'expliquer, comment chaque appel de fonction récursive interagit avec l'intégralité de l'invocation initiale de la fonction — en d'autres termes, comment chaque pièce se connecte au tout.

Quelques détails :

* Le code est écrit en Python
* Les boîtes bleues représentent la portée actuelle de la fonction
* Les lignes de connexion sont ce qu'une fonction retourne

Veuillez utiliser le code comme référence, car je ne passe pas en revue son exécution en détail.

Nous examinerons trois problèmes : trouver les anagrammes d'une chaîne, le tri par fusion et la tour de Hanoï. Ils deviennent progressivement un peu plus nuancés, alors attention !

Je discuterai de plus de détails sur la récursivité ci-dessous.

### Anagrammes

```python
def anagrams(s):
    if s == "":
        return [s]
    else :
        ans = []
    for w in anagrams(s[1: ]):
        for pos in range(len(w) + 1):
            ans.append(w[: pos] + s[0] + w[pos: ])
    return ans

anagrams("abc")

# retourne ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z67ClqdjbnaZvkASvFOxNg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YLyylfd6hKYJ9rhW4JrBHQ.png)
_anagramursion_

Ce qui précède est une bonne introduction à la pile d'appels. Remarquez comment chaque appel précédent attend la valeur de retour de l'appel récursif.

Remarquez également comment les valeurs de la variable `ans` sont toutes ajoutées pendant l'appel initial de la fonction (1).

### Tri par fusion

```python
def merge(lst1, lst2, lst3):
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(lst1), len(lst2)
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 = i1 + 1
        else:
            lst3[i3] = lst2[i2]
            i2 = i2 + 1
        i3 = i3 + 1
    
    # longueurs inégales des listes ? Vérifiez les deux
    while i1 < n1: 
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1
    
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

def mergeSort(nums):
    n = len(nums)
    if n > 1:
        m = n // 2
        nums1, nums2 = nums[:m], nums[m:]
        mergeSort(nums1)
        mergeSort(nums2)
        merge(nums1, nums2,nums)
    
numbers = [7, 4, 6, 2, 8]
mergeSort(numbers)

print(numbers)
# retourne les nombres triés (la fonction a modifié la structure de données sous-jacente)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*t9czQmsarojfOozmxL8yJw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nnvoyLfp3vkppsXPG0MOdg.png)
_recursamerged_

Encore une fois, remarquez l'ordre dans lequel chaque appel s'exécute. Pour comprendre comment fonctionne la fusion, regardez-la de près. Vous avez essentiellement trois pointeurs et deux moitiés triées de la liste initiale qui sont continuellement comparées. Le nombre le plus bas lors de cette comparaison est placé à l'index qui est pointé dans la liste initiale (en commençant à l'index 0).

Plusieurs notes si vous n'êtes pas habitué à Python. Lorsqu'une fonction ne retourne rien, elle retourne la valeur `None`. Vous pouvez voir la valeur de retour fréquente `None` dans mes diagrammes, car il n'y a pas d'instructions de retour explicites dans `mergeSort`.

De plus, remarquez comment la liste entrée dans l'appel de fonction est mutée, ce qui signifie que Python n'a pas créé de copie de la liste lorsque la fonction a été appelée.

### Tour de Hanoï

Voici une petite histoire en guise de note — je l'ai trouvée être une introduction assez poétique à la tour de Hanoï :

> « Quelque part dans une région reculée du monde se trouve un monastère d'un ordre religieux très dévot. Les moines ont été chargés d'une tâche sacrée qui mesure le temps pour l'univers. Au début de toutes choses, les moines ont reçu une table qui supporte trois poteaux verticaux. Sur l'un des poteaux se trouvait une pile de 64 disques concentriques et dorés. Les disques sont de rayons variés et empilés en forme de belle pyramide. Les moines sont chargés de la tâche de déplacer les disques du premier poteau au troisième poteau. Lorsque les moines auront accompli leur tâche, toutes choses s'effondreront en poussière et l'univers prendra fin. » — _John Zell, Python Programming: An Introduction to Computer Science (2004)_

```python
def moveTower(n, source, dest, temp):
    if n == 1:
        print("Déplacer le disque de", source, "vers", dest+".")
    else:
        moveTower(n-1, source, temp, dest)
        moveTower(1, source, dest, temp)
        moveTower(n-1, temp, dest, source)
    
 def hanoi(n):
    moveTower(n, "A", "C", "B")
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-VwEe3eLmdZ0e2fKLiZMQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*KwKjFU1KLTZun28Kvni0CQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dbkrNWmhXfpwJv2eJHINhA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IBrJOSrMZqF6Z0O5VDwPsQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*M19VyJnzn0mPfE4-CuFAcg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AKUhFf1l7tcgF88Pp5MaFA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7-1o9KOOaEKBScXEQskabA.png)
_hanoision_

Le déplacement des blocs est basé sur un [principe mathématique](https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/).

De l'article [Wikipedia](https://en.wikipedia.org/wiki/Tower_of_Hanoi) :

1. Déplacer _m_ − 1 disques de la **source** vers le **poteau temporaire**. Cela laisse le disque _m_ comme disque supérieur sur le poteau source.
2. Déplacer le disque _m_ de la **source** vers le **poteau de destination**.
3. Déplacer les _m_ − 1 disques que nous venons de placer sur le poteau temporaire vers le **poteau de destination**, afin qu'ils soient placés sur le disque _m_ sans violer les règles.

Mais comment comprendre ce principe ? Eh bien, regardez ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XVjr4Ue0FtF2BUj1W2E-Tw.png)
_exactitude_

Remarquez ceci : les trois règles se répètent (texte noir) sauf lorsque la règle 2 (texte bleu) s'exécute, car l'algorithme n'atteint pas son cas de base.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rt-CKWzyXM1VP-mwD8XuuA.png)
_basiquement_

#### Un mot sur la récursivité

Cet article est la première étape pour être capable de résoudre des problèmes récursifs. Je l'ai créé pour aider les lecteurs à comprendre comment fonctionne la récursivité et quelle est sa réalité. Pour chaque problème, remarquez comment j'ai ordonné chaque invocation de fonction et valeur de retour. C'est la même façon dont l'ordinateur lit le code.

Le concept sous-jacent de base de la récursivité est le suivant :

**La fonction dans laquelle l'appel de fonction récursive a été appelé doit attendre que l'appel de fonction récursive se termine avant de continuer son processus.**

Ainsi, si la fonction récursive appelle d'autres fonctions récursives, elle doit également attendre que ces fonctions récursives retournent. La récursivité, d'une certaine manière, implique simplement des fonctions attendant que les fonctions qu'elles ont appelées retournent quelque chose avant de continuer.

Si vous souhaitez progresser dans le domaine de la résolution de problèmes récursifs, alors vous devez étudier les mathématiques. Ils ne font qu'un. Mais passer en revue les mathématiques dépasse le cadre de cet article. Cet [article de Wikipedia](https://en.wikipedia.org/wiki/Mathematical_induction) est une bonne introduction pour commencer.

C'est tout. Je dois remercier, absolument et complètement, [Data Structures and Algorithms Using Python and C++](https://www.amazon.com/gp/product/1590282337/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1) de David M. Reed, ainsi que John Zelle, car c'est là que cette merveilleuse citation et les algorithmes ont été tirés.

Et voici une belle vue de l'espace parce que, eh bien, la récursivité donne un peu cette impression.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PPXnzjpCdxuMiz9OJdhe8w.png)