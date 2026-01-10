---
title: Un récit tordu de la recherche binaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-04T00:33:07.000Z'
originalURL: https://freecodecamp.org/news/a-twisted-tale-of-binary-search-49f5ac01e83d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DClFFS2kX-MPvGuHYvOyTw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Un récit tordu de la recherche binaire
seo_desc: 'By Divya Godayal

  Awesome. That’s how I feel right now. Writing my first solo tech article.

  I must say I have a lot to share with you guys, and have a lot more to learn as
  well. So without any further ado, lets get to it. And yes, hold on tight — ‘cau...'
---

Par Divya Godayal

Génial. C'est comme ça que je me sens en ce moment. Écrire mon premier article technique en solo.

Je dois dire que j'ai beaucoup à partager avec vous, et j'ai encore beaucoup à apprendre aussi. Alors sans plus attendre, commençons. Et oui, accrochez-vous bien — car il y a un rebondissement dans l'histoire. 💡

### Recherche binaire

Nous avons tous entendu parler du problème classique des [2 œufs et 100 étages](https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/). J'ai quelque chose de similaire pour vous.

Vous avez un bâtiment de 100 étages avec une règle :

`**Les personnes avec des animaux de compagnie ne peuvent occuper que les étages supérieurs**`

Votre amie souhaite acheter un appartement dans ce bâtiment. Elle a trop peur des animaux de compagnie pour vivre près d'eux, mais vous les adorez. Elle vous a demandé si vous pouviez l'aider à trouver où commencent exactement les étages acceptant les animaux. Elle veut explorer toutes les différentes options disponibles, et vous devez donc trouver quels étages, en partant du rez-de-chaussée, sont ceux qui n'autorisent pas les animaux.

Les responsables de l'immeuble sont en vacances. À chaque étage, il y a un panneau à côté de l'ascenseur indiquant si l'étage est adapté aux animaux ou non. Mais vous êtes trop paresseux pour vous arrêter à chaque étage pour vérifier le panneau des animaux, car l'ascenseur est si lent.

Que faites-vous ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*mVvYhywAIoa11tCRfsHPQA.png)
_Les deux panneaux possibles. #GoRed est ce que votre amie soutient._

L'ascenseur prend presque une minute à chaque étage pour s'arrêter puis redémarrer. Oui, c'est à ce point-là. Mais entre les étages, la navigation est assez fluide. Vous devez faire cela rapidement.

Comment vous y prenez-vous ?

### Approche itérative

Une approche naïve à ce problème serait de commencer tout en bas du bâtiment (le rez-de-chaussée) et de continuer à arrêter l'ascenseur à chaque étage pour vérifier le panneau que cet étage a affiché. Vous vous arrêtez lorsque vous trouvez le panneau adapté aux animaux.

**Le meilleur cas** est que le rez-de-chaussée ait le panneau pour animaux. Cela signifie que tout le bâtiment a des animaux. Aucune chance que votre amie achète un appartement ici.

**Le cas moyen** est que vous alliez au 50ème étage, en vous arrêtant à chaque étage entre les deux, et que vous trouviez enfin un panneau pour animaux. Ainsi, votre amie peut en acheter un de 1 à 49.

**Le pire cas** serait que vous atteigniez le 100ème étage, en vous arrêtant à chaque étage en montant, pour découvrir qu'il n'y a aucun panneau pour animaux dans tout le bâtiment. Ainsi, votre amie peut acheter n'importe quel appartement de 1 à 100, mais qui s'en soucie, cela vous a pris presque deux heures pour le découvrir. 😅 😅.

Algorithmiquement, étant donné un tableau de 100 valeurs booléennes, l'index du tableau représente les étages du bâtiment et un 0 représente un étage où les animaux ne sont pas autorisés tandis qu'un 1 représente un étage où les animaux seraient autorisés. Selon la règle du bâtiment, le tableau serait de la forme

```
000... 1111...
```

c'est-à-dire, tous les 0 suivis de tous les 1, car seuls les étages supérieurs peuvent être ceux où les animaux sont autorisés.

Étant donné ce tableau, nous devons trouver le premier index où il y a un `1`. Un algorithme de recherche linéaire pour ce problème serait aussi simple que de parcourir le tableau et de chercher un `1` et de retourner lorsque nous en trouvons un.

Comme prévu, la complexité de cet algorithme serait `O(n)` où n = 100 pour notre exemple spécifique de bâtiment. Vous devez trouver quelque chose de plus rapide que cela. Vous arrêter à chaque étage n'est pas faisable, car cela vous prendrait beaucoup de temps pour couvrir tout le bâtiment dans le pire des cas.

### Approche de recherche binaire

Supposons que vous commençiez par le rez-de-chaussée et que vous alliez au 50ème étage sans vous arrêter. Au 50ème étage, vous vous arrêtez et sortez de l'ascenseur et vérifiez le panneau. Le panneau indiquait « Pas d'animaux ». Cela signifierait que, jusqu'au 50ème étage, il n'y a définitivement pas d'animaux.

Ainsi, sachant cela, vous réduisez votre espace de recherche à l'autre moitié, qui est les étages 51 à 100. Cela signifie qu'avec un seul arrêt, vous avez pu couvrir la moitié du bâtiment en sachant avec certitude que la première moitié n'a aucun animal. C'est incroyable !

En continuant, vous divisez à nouveau votre ensemble restant d'étages en deux et prenez l'ascenseur et allez directement au 75ème étage. Et vous voyez un panneau « Animaux ». Cela signifie que l'étage où cela a commencé à apparaître doit être entre 50 et 75. Vous pouvez continuer à suivre une approche similaire en divisant les étages restants en deux et en vérifiant jusqu'à ce que vous trouviez le premier étage avec le panneau « Animaux ».

Vous voyez, chaque fois que vous prenez une décision, vous divisez votre espace de recherche en deux moitiés et continuez avec une moitié de l'espace de recherche. C'est ainsi que nous réduisons notre recherche. Puisque nous divisons toujours l'espace de recherche en deux et choisissons l'un plutôt que l'autre, c'est pourquoi ce type de stratégie de recherche est appelé une stratégie de recherche `Binaire`.

N'est-ce pas bien plus rapide ?

Examinons l'algorithme pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5xqxb4gs88vQGaK8CCp47w.png)
_Algorithme de recherche binaire_

Si vous avez suivi attentivement et que vous avez saisi l'algorithme, vous aurez réalisé une condition stricte pour que l'algorithme de recherche binaire fonctionne. La condition est que le tableau doit être trié au préalable. Dans notre exemple, les étages du bâtiment étaient triés de 1 à 100 et nous avons pu facilement diviser l'espace de recherche en deux.

Examinons un exemple de tableau qui est trié et essayons d'y rechercher un élément.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sCdkKU8RqA6_R3uiy4nL2w.png)

Dans l'exemple ci-dessus, l'élément à rechercher est 8. Le tableau donné est un tableau trié dans l'ordre croissant. Une fois que nous avons trouvé l'élément du milieu (qui est 5), nous voyons que l'élément à rechercher est plus grand que l'élément de l'index actuel. Puisque le tableau est trié dans l'ordre croissant, 8 se trouverait à droite du tableau et ne peut jamais être du côté gauche.

Nous ignorons donc les éléments à gauche de 5 et continuons notre recherche avec les éléments restants, trouvant finalement 8.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S2lDovD5HeUsdSHm3NM4Sw.png)

D'un autre côté, que se passe-t-il si le tableau n'est pas trié ? Même si nous savons que l'élément actuel est 5 et que nous savons que nous devons rechercher 8, nous ne sommes pas sûrs de la direction à prendre. Si nous finissons par penser que le tableau est trié et appliquons une recherche binaire et allons vers la partie droite, nous ne trouverons jamais 8.

**Ainsi, la recherche binaire nécessite essentiellement que votre tableau soit trié.**

C'était l'algorithme standard de recherche binaire que nous venons d'examiner. Mais, comme le suggère le titre de l'article, il y a un rebondissement dans l'histoire !

Je suis un programmeur compétitif passionné, et il y avait une variante intéressante de l'algorithme de recherche binaire dans le [CodeChef May Long Challenge](https://www.codechef.com/MAY18B/problems/FAKEBS).

Essentiellement, le Chef a écrit la recherche binaire classique, en supposant que le tableau d'entrée serait trié. Tous les autres enfants de la classe ont copié le code de lui, car le Chef est le meilleur programmeur de la classe. Son hypothèse aurait pu coûter à toute la classe leurs notes d'assignation, car le tableau d'entrée n'était pas trié au préalable.

La seule chose que le Chef peut faire est de pré-traiter le tableau en échangeant quelques paires de nombres ici et là afin que la procédure de recherche binaire retourne toujours le bon index.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MOupjMd8PLQIkCoXHPIkHw.png)

**Note :** Le pré-processeur ci-dessus devrait idéalement retourner le tableau modifié pour que la recherche binaire fonctionne correctement. Cependant, comme l'énoncé du problème le demande, nous essayons simplement de déterminer le nombre d'échanges nécessaires pour que la recherche binaire fonctionne correctement sur le tableau non trié donné une entrée. L'algorithme retournerait également un -1 si une telle modification n'est pas possible pour le tableau et l'élément donnés.

L'idée ici est très simple.

Nous devons comprendre deux étapes de base. Je les appelle les étapes **TI-ME**. Peut-être que cela vous aidera à vous souvenir de ce que nous faisons ici.

a. **T**arget **I**ndex : L'index de l'élément à rechercher. Nous devons connaître cela, car cet index nous aidera à conduire les modifications. Parce que chaque fois que nous modifions un élément, nous devons nous diriger vers cet index et non pas nous en éloigner.

b. **M**iddle **E**lement : Si vous regardez attentivement dans une recherche binaire, c'est l'élément du milieu de l'espace de recherche actuel qui conduit le prochain mouvement. Si cet élément du milieu nous emmène dans la mauvaise direction, nous devons le remplacer par l'élément approprié.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xgnYQLeH-9l2MVU_OqTNLQ.png)
_Nous recherchons 8 dans le tableau non trié ci-dessus. Nous avons déjà vu dans les exemples ci-dessus qu'une recherche binaire normale échouerait pour un tableau non trié._

![Image](https://cdn-media-1.freecodecamp.org/images/1*sJNU_8PdNlbIuy7RStVHdA.png)
_Les éléments du milieu donnent une direction à la recherche binaire. L'élément du milieu 5 ferait que la recherche binaire irait à droite. De cette façon, nous ne trouverions jamais `8`. Si nous échangeons 5 avec un élément supérieur à 8, nous forcerions la recherche à aller à gauche._

Ainsi, l'idée ici est que nous échangeons tous les éléments du milieu qui sont mal placés.

L'algorithme de recherche binaire (la valeur de l'élément du milieu par rapport à l'élément à rechercher, c'est-à-dire, X) peut soit nous emmener vers la moitié gauche du tableau, soit vers la moitié droite. Il y a donc deux possibilités pour un élément du milieu mal placé :

1. L'élément à rechercher était à droite de l'élément du milieu, mais puisque `Element[Mid] > Element[Target Ind`ex] , la recherche binaire aurait dû ignorer la moitié droite et se déplacer vers la moitié gauche. OU
2. L'élément à rechercher était à gauche de l'élément du milieu, mais puisque `Element[Mid] < Element[Target Ind`ex] , la recherche binaire aurait dû ignorer la moitié gauche et se déplacer vers la moitié droite.

Par conséquent, si un élément du milieu est mal placé de sorte qu'un nombre `X` était nécessaire à sa place où `X < Element[Target Ind`ex] , alors nous maintenons un compteur pour cela et l'appelons `it count_low_nee`ded .

De même, si un élément du milieu est mal placé de sorte qu'un nombre `X` était nécessaire à sa place où `X > Element[Target Ind`ex] , alors nous maintenons un compteur pour cela et l'appelons `it count_high_nee`ded .

De plus, si nous exécutons simplement l'algorithme de recherche binaire sur le tableau donné tout en recherchant des nombres, il y aurait certains nombres qui seraient correctement placés. Ce seraient les éléments du milieu qui ont conduit la recherche binaire dans les bonnes directions correspondant à l'élément donné `X` (l'élément à rechercher). Ces nombres ne peuvent pas faire partie de l'échange, car ils sont correctement positionnés par rapport à `X` .

Examinons d'abord le pseudo-code de cet algorithme, puis passons par un exemple.

```
function can_preprocess(arr, X){     low = 0     high= 0
```

```
while X is not found {          mid = (low + high) / 2          if arr[mid] == X {             break                     }
```

```
correctly_placed_low = 0          correctly_placed_high = 0          count_low_needed = 0          count_high_needed = 0
```

```
if `mid` suggests we should go right for X {               if X is actually on the right {                   correctly_placed_low ++               }               else {                   count_low_needed ++               }          } else {               if X is actually on the left {                  correctly_placed_high ++               }                else {                  count_high_needed ++               }          }
```

```
modify low and high according to           where `X` actually is with respect to `mid`
```

```
}
```

```
// Total smaller numbers available for swapping     TSM = sorted_index[X] - correctly_placed_low
```

```
// Total Larger numbers available for swapping     TLM = (N - sorted_index[X]) - correctly_placed_high
```

```
if count_low_needed > TSM or count_high_needed > TLM {          return -1     }
```

```
return max(count_low_needed, count_high_needed)
```

**NOTE:** L'énoncé du problème fixe le tableau d'entrée pour nous et passe à plusieurs reprises des valeurs à rechercher dans le tableau d'entrée. Nous pouvons donc parcourir une fois le tableau original pour connaître l'emplacement réel de l'élément à rechercher (créer un dictionnaire, essentiellement).

De plus, nous avons besoin de `sorted_index[X]` pour nous dire combien de valeurs sont inférieures ou supérieures à l'élément `X` dans notre tableau. Nous pouvons trier le tableau et créer un autre dictionnaire stockant l'emplacement de chaque élément dans le tableau trié.

Passons par les étapes de l'algorithme proposé tout en exécutant un exemple à sec.

1. Étant donné un tableau non trié, vous devez rechercher `X = 4`. 
Ainsi, notre index cible est 7.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3vnVPsJgCPjLLmWENiB8rQ.png)

2. L'index de l'élément du milieu < Index cible, nous devons donc manœuvrer notre recherche vers la moitié droite. M`ais Element[Mid] > Element[Target` Index], `donc count_low_need`ed = 1

![Image](https://cdn-media-1.freecodecamp.org/images/1*goOz9sCtElJn8_GVf86n-Q.png)

3. L'index de l'élément du milieu < Index cible, nous devons donc toujours manœuvrer notre recherche vers la moitié droite. Une fois de pl`us, Element[Mid] > Element[Target` Index], `donc count_low_need`ed = 2

![Image](https://cdn-media-1.freecodecamp.org/images/1*RuHR_k66dh-G0KzI-6DRuQ.png)

4. Le nombre total d'échanges nécessaires pour que la recherche binaire retourne l'index correct ici serait deux échanges avec des éléments inférieurs à 4. Nous avons des nombres plus petits `1, 3 ou 2` pour l'échange disponibles, nous pouvons donc réussir l'échange pour ce tableau afin que la recherche binaire trouve correctement `4`.

Voici le code Python pour le problème donné. Chaque étape est expliquée dans les commentaires.

La complexité temporelle de cet algorithme de recherche binaire tordue est toujours `O(nlogn)`.

J'espère que vous avez pu saisir le fonctionnement interne de l'algorithme de recherche binaire et que vous vous êtes amusé en parcourant ce problème intéressant. Si vous avez trouvé cet article utile, partagez l'amour et partagez autant que possible. 💖