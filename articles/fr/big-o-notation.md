---
title: Comment fonctionne la notation Big O – Expliqué avec un gâteau
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2020-12-28T14:54:48.000Z'
originalURL: https://freecodecamp.org/news/big-o-notation
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd9038ee6787e098393f598.jpg
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
seo_title: Comment fonctionne la notation Big O – Expliqué avec un gâteau
seo_desc: 'Big O notation is used in computer science to define an upper bound of
  an algorithm. It is mostly used to define the maximum time of an algorithm as a
  function of the input size, but it can also be used to define memory usage.

  In this article we will...'
---

La notation Big O est utilisée en informatique pour définir une limite supérieure d'un algorithme. Elle est principalement utilisée pour définir le temps maximum d'un algorithme en fonction de la taille de l'entrée, mais elle peut également être utilisée pour définir l'utilisation de la mémoire.

Dans cet article, nous allons parler des types les plus courants de notation 'Big O', en utilisant des gâteaux d'anniversaire pour illustrer les concepts. Nous allons imaginer que nous organisons une fête et que nous devons déterminer combien de gâteaux cuire en fonction du nombre de personnes présentes.

## O(1) - Temps constant

Pour l'exemple de temps constant, peu importe le nombre de personnes qui viennent à la fête d'anniversaire, vous ne faites qu'un seul gâteau. Ainsi, le temps de préparation du gâteau reste constant.

![O(1) Illustration du temps constant](https://www.freecodecamp.org/news/content/images/2020/12/o-1--constant-time.png)

Notez que la notation Big O ne précise pas combien de temps dure le temps constant (peut-être qu'il faut 1 heure pour faire le gâteau, peut-être qu'il en faut 4). Elle indique simplement que le temps pris n'augmente pas avec le nombre d'invités.

Un exemple concret d'une opération O(1) est l'accès à un tableau par son index. Il est aussi rapide de récupérer un élément d'un tableau de 10 éléments que de récupérer un élément d'un tableau d'un million d'éléments.

![O(1) Graphique du temps constant](https://www.freecodecamp.org/news/content/images/2020/12/o-1--constant-time-grqph.png)

## O(log n) - Temps logarithmique

Pour l'exemple de temps logarithmique, les gâteaux d'anniversaire sont utilisés comme moyen d'inciter les gens à arriver à l'heure à la fête.

La première personne à arriver obtient un gâteau entier pour elle-même. Ensuite, les deux personnes suivantes à arriver partagent un gâteau. Puis les quatre personnes suivantes partagent un gâteau, et ainsi de suite.

Ainsi, une fête avec 1 personne nécessite 1 gâteau. Une fête avec 2 ou 3 personnes nécessite 2 gâteaux. Une fête avec 4 à 7 personnes nécessite 3 gâteaux, et une fête avec 8 à 15 personnes nécessite 4 gâteaux. En général, une fête avec 'n' personnes nécessite log₂(n) gâteaux.

![O(log n) Illustration du temps logarithmique](https://www.freecodecamp.org/news/content/images/2020/12/o-log-n--logarithmic-time.png)

L'exemple le plus courant d'une opération O(log n) est une recherche binaire dans un tableau ordonné.

Cet algorithme regarde le milieu d'un tableau et voit si la valeur est inférieure ou supérieure à celle qu'il recherche. Comme la liste est ordonnée, il sait ensuite dans quelle moitié du tableau se trouve la valeur cible.

Il répète ensuite le processus avec cette moitié du tableau. Ainsi, pour un tableau de 16 éléments, la première itération réduit la recherche à 8 éléments, puis 4, puis 2 et enfin 1, pour un maximum de 4, ou log₂(16), itérations au total.

![O(log n) Graphique du temps logarithmique](https://www.freecodecamp.org/news/content/images/2020/12/o-log-n--logarithmic-time-graph.png)

## O(n) - Temps linéaire

Pour l'exemple de temps linéaire, chaque invité obtient son propre gâteau. Si 'n' personnes viennent à la fête, vous devez faire 'n' gâteaux. Ainsi, le temps pris est lié au nombre d'invités.

![O(n) Illustration du temps linéaire](https://www.freecodecamp.org/news/content/images/2020/12/o-n--linear-time.png)

Encore une fois, la notation Big O ne précise pas combien de temps cela prend (peut-être qu'il faut 1 heure pour faire le gâteau, peut-être qu'il en faut 4), elle indique simplement que le temps augmente linéairement avec le nombre d'invités.

Un exemple concret d'une opération O(n) est une recherche naïve d'un élément dans un tableau. Dans un tableau de 10 éléments, au pire, vous devrez regarder les 10 éléments pour trouver celui que vous voulez. Mais pour un tableau d'un million d'éléments, vous devrez peut-être regarder les un million d'éléments.

Bien sûr, vous pourriez trouver la solution plus tôt, mais la notation Big O spécifie le temps maximum qu'un algorithme prendra.

![O(n) Graphique du temps linéaire](https://www.freecodecamp.org/news/content/images/2020/12/o-n--linear-time-graph.png)

## O(n²) - Temps quadratique

Pour l'exemple de temps quadratique, chaque invité obtient son propre gâteau. De plus, chaque gâteau a les noms de tous les invités écrits dessus, avec un délicieux glaçage.

Dans ce cas, une fête avec 1 personne a un gâteau avec un nom dessus. Une fête avec 2 personnes a deux gâteaux, tous les deux avec deux noms dessus (4 noms au total) et une fête avec 3 personnes a trois gâteaux, tous avec trois noms dessus, ce qui fait 9 noms au total.

![O(n²) Illustration du temps quadratique](https://www.freecodecamp.org/news/content/images/2020/12/o-n-2--quadratic-time.png)

En général, une fête avec 'n' personnes nécessite n*n noms à écrire (également connu sous le nom de n au carré, ou n à la puissance de 2), donc la vitesse de fabrication des gâteaux (et d'écriture de tous les noms) est liée au carré du nombre d'invités.

Un exemple concret d'une opération O(n²) est une recherche naïve de doublons dans un tableau. Dans ce scénario, vous parcourez tous les éléments du tableau, et pour chacun de ces éléments, vous parcourez à nouveau le tableau pour voir s'il y a des correspondances.

Pour un tableau de 10 éléments, la boucle externe a 10 itérations, et pour chacune de celles-ci, il y a 10 itérations de la boucle interne, soit 100 au total. Pour un tableau d'un million d'éléments, c'est 1000 milliards.

Il existe un cas plus général de O(n²), où au lieu que le temps soit relatif à n à la puissance de 2 (n²), il est relatif à n à la puissance de c (n^c). Cela s'appelle généralement le temps polynomial.

![O(n²) Graphique du temps quadratique](https://www.freecodecamp.org/news/content/images/2020/12/o-n-2--quadratic-time-graph.png)

## O(n!) - Temps factoriel

Pour l'exemple de temps factoriel, les invités participent à une compétition de [Pétanque](https://en.wikipedia.org/wiki/P%C3%A9tanque), et le gagnant ramène le gâteau à la maison.

Il y a un léger problème, cependant, en ce que le joueur qui prend le premier tour est désavantagé. Pour aider à équilibrer les choses, de nombreux jeux sont joués, de sorte que chaque permutation d'invités soit couverte et que tout le monde puisse commencer. Toutes ces permutations sont écrites sur le gâteau, à nouveau avec un délicieux glaçage.

Cela signifie qu'une fête avec 2 personnes a deux jeux, car chaque invité prend à tour de rôle pour commencer. Une fête avec 3 personnes a 6 jeux (si nous imaginons que les invités sont Anna, Brian et Chris, alors les permutations sont ABC, ACB, BAC, BCA, CAB, CBA).

![O(n!) - Illustration du temps factoriel](https://www.freecodecamp.org/news/content/images/2020/12/o-n---factorial-time.png)

En général, une fête avec 'n' personnes nécessite n!, ou n factoriel jeux, donc la vitesse de fabrication du gâteau est liée à cela.

n! est calculé en multipliant tous les nombres entiers de n jusqu'à un «n * (n - 1) * (n - 2) … * 2 * 1». Ainsi, pour la fête avec 2 personnes, c'est 2 * 1, soit 2. Pour la fête avec trois personnes, c'est 3 * 2 * 1, ce qui fait 6.

Des exemples concrets d'opérations O(n!) sont tout ce qui nécessite l'analyse d'une liste de permutations, comme le [problème du voyageur de commerce](https://en.wikipedia.org/wiki/Travelling_salesman_problem).

![O(n!) Graphique du temps factoriel](https://www.freecodecamp.org/news/content/images/2020/12/image-165.png)

## Conclusions

Espérons que les gâteaux d'anniversaire ont rendu la notation 'Big O' plus facile à comprendre ! Le graphique ci-dessous est également une bonne aide-mémoire, montrant les vitesses relatives des algorithmes (si vous avez le choix, vous voulez le plus rapide !)

![Graphique de la notation Big O](https://www.freecodecamp.org/news/content/images/2020/12/image-166.png)

Il existe plusieurs autres notations 'Big O', comme O(n log n) et O(c^n), mais elles suivent toutes le même schéma. Si vous voulez en apprendre plus, [consultez cet article](https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/).