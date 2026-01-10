---
title: Comment utiliser la technique de la fenêtre glissante – Exemple et solution
  d'algorithme
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2024-01-11T15:11:48.000Z'
originalURL: https://freecodecamp.org/news/sliding-window-technique
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Sliding-Window-Technique
seo_title: Comment utiliser la technique de la fenêtre glissante – Exemple et solution
  d'algorithme
---

Banner.png
tags:
- name: algorithmes
  slug: algorithmes
- name: structures de données
  slug: structures-de-donnees
seo_title: null
seo_desc: "Récemment, je m'entraînais à résoudre des problèmes de codage axés sur les structures de données et les algorithmes en préparation pour un changement d'emploi.\n\nPendant ce processus, je suis tombé sur la technique de la fenêtre glissante. J'ai trouvé cet algorithme très intéressant, alors j'ai voulu partager mes apprentissages avec la communauté."
---

Récemment, je m'entraînais à résoudre des problèmes de codage axés sur les structures de données et les algorithmes en préparation pour un changement d'emploi.

Pendant ce processus, je suis tombé sur la technique de la fenêtre glissante. J'ai trouvé cet algorithme très intéressant, alors j'ai voulu partager mes apprentissages avec la communauté.

Ce tutoriel sera utile pour vous si vous vous préparez pour des entretiens de programmation compétitive. Alors, commençons.

## Qu'est-ce que la technique de la fenêtre glissante ?

La technique de la fenêtre glissante est une approche algorithmique utilisée en informatique et en traitement du signal. Elle consiste à sélectionner un sous-ensemble de taille fixe, ou « fenêtre », à partir d'un ensemble de données plus grand et à déplacer cette fenêtre à travers l'ensemble de données de manière progressive.

La fenêtre glisse sur les données, généralement un élément à la fois, et effectue une opération sur les éléments à l'intérieur de la fenêtre à chaque étape.

Êtes-vous confus ? Laissez-moi élaborer sur cette technique avec un exemple.

### Exemple de fenêtre glissante

Supposons que vous vous entraînez pour la programmation compétitive et que vous rencontrez le problème suivant :

"Trouvez la somme maximale d'un sous-tableau de taille k avec une complexité temporelle de O(N).

Tableau = [1, 2, 6, 2, 4, 1], k = 3"

Si vous n'êtes pas familier avec le concept de complexité temporelle, voici une définition rapide :

> En informatique théorique, la complexité temporelle est la complexité computationnelle qui décrit la quantité de temps informatique nécessaire pour exécuter un algorithme.

Et [voici un cours](https://www.freecodecamp.org/news/learn-big-o-notation/) si vous souhaitez en apprendre davantage.

Revenons à notre problème. Basiquement, nous devons trouver le sous-tableau de taille 3 dont la somme est maximale (le plus grand nombre). Voici une vue picturale de la manière dont nous pouvons procéder pour résoudre cela :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-27.png)
_Trouver la somme d'un sous-tableau de taille k_

#### Solution manuelle

Résolvons-le manuellement. À partir de l'image ci-dessus, trouvons la somme de chacun des sous-tableaux de taille 3.

* Somme du 1er sous-tableau = 1 + 2 + 6 = 9
* Somme du 2ème sous-tableau = 2 + 6 + 2 = 10
* Somme du 3ème sous-tableau = 6 + 2 + 4 = 12
* Somme du 4ème sous-tableau = 2 + 4 + 1 = 7

Le nombre maximum (le plus grand) parmi 9, 10, 12 et 7 est 12 – ou le 3ème sous-tableau. C'est notre solution.

#### Solution de code

D'accord, enfilons nos chaussures de programmation et essayons de résoudre cela en utilisant du code.

Voici ma solution au problème :

<script src="https://gist.github.com/5minslearn/c4867d2750d89f81c8d72cc8bbacf700.js"></script>

Voici un rapide aperçu du code ci-dessus.

Je définis le tableau d'entrée et la taille de la fenêtre en bas, et j'appelle la méthode `findMaxSumOfSequence` avec ces paramètres.

Initialement, je fais une validation si la taille du tableau d'entrée est supérieure à la taille de la fenêtre, sinon le calcul n'est pas possible, donc je retourne null.

Je suppose que la somme maximale est négative à l'infini.

J'itère sur le tableau, et pour chaque élément du tableau, j'itère sur les `k` éléments suivants, je trouve leur somme, et j'assigne la somme de la fenêtre actuelle à la variable de somme maximale si la somme de la fenêtre actuelle est supérieure à la somme maximale existante. Enfin, je retourne la somme maximale.

Essayons d'exécuter le code.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-26.png)
_Trouver la somme maximale d'un sous-tableau de taille k_

Nous y voilà. Nous avons obtenu la bonne réponse.

Mais le problème ne s'arrête pas là. Si vous regardez attentivement le problème, nous devons trouver la solution avec une complexité temporelle de O(N).

Vous pourriez donc vous demander quelle est la complexité temporelle de la solution ci-dessus. Eh bien, la complexité temporelle de la solution ci-dessus est O(N*k). Cela signifie que nous itérons `k` fois pour chaque élément du tableau (boucle for imbriquée).

La complexité temporelle O(N) décrit essentiellement que vous devez trouver la valeur maximale en itérant sur le tableau donné une seule fois.

#### Utilisation de la technique de la fenêtre glissante

Comment résoudre cela avec une seule itération ? C'est là que la technique de la fenêtre glissante entre en jeu. Jetons un coup d'œil à la représentation picturale de notre solution une fois de plus :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-27.png)
_Technique de la fenêtre glissante_

Ici, vous pouvez remarquer que la fenêtre glisse sur le tableau. Elle couvre initialement les indices 0, 1 et 2 dans le 1er sous-tableau. Pour le sous-tableau suivant, elle glisse d'une position vers la droite, éliminant l'indice 0 à gauche et ajoutant l'indice 3 à droite. Ainsi, elle couvre maintenant les indices 1, 2 et 3 dans le 2ème sous-tableau... et ainsi de suite.

Le calcul se fait de cette manière pour les sous-tableaux :

* 1er sous-tableau = 1 + 2 + 6 = 9
* 2ème sous-tableau = 9 (somme du 1er sous-tableau) - 1 + 2 = 10

Examinons cela attentivement. Nous trouvons que la somme du 1er sous-tableau est 9. Pour calculer la somme du 2ème sous-tableau, nous soustrayons le nombre qui sort (1 à l'indice 0) et ajoutons le nombre qui entre (2 à l'indice 3).

* 3ème sous-tableau = 10 (somme du 2ème sous-tableau) - 2 + 4 = 12
* 4ème sous-tableau = 12 (somme du 3ème sous-tableau) - 6 + 1 = 7

C'est la technique de la fenêtre glissante. En suivant cette technique, nous serons en mesure de trouver la somme du sous-tableau maximum en une seule itération.

#### Comment implémenter la fenêtre glissante en code

D'accord, remettons nos chaussures de codage et essayons de l'implémenter.

<script src="https://gist.github.com/5minslearn/f5fb22bec4cba7e39403bc59b55c8d44.js"></script>

Essayons de comprendre le code ci-dessus. J'ai apporté quelques modifications à la méthode `findMaxSumOfSequence`. J'ai introduit les variables `start` et `end` qui décrivent le bloc de la fenêtre.

Dans cette implémentation, nous avons 2 boucles mais elles ne sont pas imbriquées. Cela est dû au fait que, dans la première boucle, nous devons trouver la somme de la première fenêtre. La deuxième boucle soustraira et ajoutera des éléments au résultat de la première boucle.

À partir de l'exemple ci-dessus, la première boucle itérera sur les premiers éléments k (3) qui sont 1, 2 et 6. Je calcule la somme et je les stocke dans les variables `maxSum` et `windowSum`.

Dans la boucle suivante, j'itère sur chaque élément du tableau. Pour chaque élément, je soustrais le nombre précédent et j'ajoute le nombre suivant, et je mets à jour le résultat dans la variable `windowSum`. Je compare les variables `windowSum` et `maxSum` et je mets à jour la variable `maxSum` si `windowSum` est plus grand. Ensuite, je déplace la fenêtre vers le sous-tableau suivant en incrémentant les variables `start` et `end`. Enfin, je retourne la somme maximale.

Voici le résultat du code ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-32.png)
_Trouver la somme maximale d'un sous-tableau de taille k en utilisant la technique de la fenêtre glissante_

Avec cette implémentation, nous avons satisfait l'exigence du problème en itérant sur le tableau une seule fois et en trouvant la somme maximale d'un sous-tableau (avec une complexité temporelle de O(N)).

## Applications de la technique de la fenêtre glissante

La technique de la fenêtre glissante est polyvalente et trouve des applications dans divers domaines.

**Manipulation de tableaux et de chaînes de caractères** : Dans le traitement de tableaux ou de chaînes de caractères, une fenêtre glissante peut être utilisée pour effectuer efficacement des opérations telles que la recherche de sous-tableaux ou de sous-chaînes qui satisfont certaines conditions.

**Compression de données** : Les algorithmes de compression par fenêtre glissante, comme LZ77 et ses variantes, utilisent une fenêtre pour trouver des motifs répétés dans les données d'entrée et les remplacer par des références aux occurrences précédentes.

**Traitement d'image** : En traitement d'image, une fenêtre glissante peut être employée pour des tâches telles que l'extraction de caractéristiques, la détection d'objets ou la segmentation d'image.

**Traitement du signal** : Les données de séries temporelles peuvent être analysées en utilisant une fenêtre glissante pour capturer des motifs locaux, des tendances ou des anomalies.

**Protocoles réseau** : Les protocoles de fenêtre glissante sont utilisés dans les réseaux informatiques pour une transmission de données fiable et efficace. L'émetteur et le récepteur maintiennent une fenêtre de numéros de séquence autorisés pour gérer le flux de données.

## Conclusion

J'espère que vous avez maintenant une idée claire de la manière dont la technique de la fenêtre glissante fonctionne après avoir vu ces exemples. Je vous recommande d'essayer de résoudre d'autres problèmes avec cette technique pour vous familiariser avec elle. Essayer de trouver la somme minimale du sous-tableau de taille k par vous-même en utilisant cette technique serait un exercice utile.

Comme je l'ai mentionné précédemment, je cherche activement à changer d'emploi. Si vous avez une bonne position disponible dans votre organisation, veuillez me recommander [ici](https://arunachalam-b.github.io/).

J'espère que vous avez apprécié la lecture de cet article. Si vous souhaitez en apprendre davantage sur les techniques pour réussir les entretiens de programmation compétitive, abonnez-vous à ma newsletter en visitant mon [site](https://5minslearn.gogosoon.com/?ref=fcc_sliding_window_technique) qui contient également une liste consolidée de tous mes blogs.