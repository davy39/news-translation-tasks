---
title: Comment aplatir un tableau en JavaScript en utilisant la récursivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-18T15:11:05.000Z'
originalURL: https://freecodecamp.org/news/flatten-array-recursion
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-damon-hall-1705254.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Recursion
  slug: recursion
seo_title: Comment aplatir un tableau en JavaScript en utilisant la récursivité
seo_desc: 'By Adwaith KS

  In this tutorial, we''ll go through a common coding problem that interviewers love
  to ask candidates. Hopefully this will help you understand how to think through
  it and solve it.

  Let''s begin by understanding the problem. You are given a...'
---

Par Adwaith KS

Dans ce tutoriel, nous allons aborder un problème de codage courant que les recruteurs adorent poser aux candidats. Espérons que cela vous aidera à comprendre comment le résoudre.

Commençons par comprendre le problème. Vous recevez un tableau qui contient des nombres et des tableaux imbriqués de nombres. Votre tâche est de retourner un nouveau tableau qui contient tous les nombres de manière linéaire sans aucune imbrication. Gardez à l'esprit que l'imbrication peut être à n'importe quel niveau de profondeur.

Voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Dribbble-shot---1-2.png)
_Exemple d'entrée et de sortie_


Maintenant, à quoi pensez-vous lorsque vous entendez le mot **imbrication** ? Eh bien, un concept qui devrait vous venir à l'esprit est la **récursivité**.

## **Qu'est-ce que la récursivité ?**

La récursivité signifie simplement une fonction qui s'appelle elle-même. Immédiatement, vous pourriez demander si une fonction continue de s'appeler elle-même, cela ne créera-t-il pas une boucle infinie ? Oui – vous avez raison !

Pour y remédier, nous utilisons certaines **conditions** (probablement une condition if) pour arrêter les appels de fonction récursifs, une fois que nous avons terminé notre tâche. Ces conditions sont appelées **cas de base**.

Commençons par un exemple. Supposons que je veux imprimer les nombres de 1 à N (inclus). Typiquement, vous écriviez une boucle for pour cela, n'est-ce pas ? Quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/carbon-1.svg)
_Fonction pour imprimer 1 à N (solution itérative)_

Et si je veux écrire le code pour imprimer 1 à N en utilisant la récursivité ?

Pour écrire une fonction récursive pour ce qui précède, nous devons nous poser les deux questions suivantes :

1. Quand notre fonction récursive doit-elle s'arrêter ? Réponse : En atteignant N + 1, puisque nous devons imprimer de 1 à N **inclus**.
2. Quel est le travail réel que notre fonction récursive doit faire ? Réponse : Imprimer les valeurs sur la console.

Donc en résumé, **continuez à imprimer les valeurs jusqu'à ce que nous atteignions N + 1**.

Selon la deuxième question que nous venons de discuter, notre code devrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/carbon-3-2.svg)

Le morceau de code ci-dessus imprime également 1 à N (5), n'est-ce pas ? Le travail réel que fait ce morceau de code est d'imprimer les valeurs sur la console.

Maintenant, au lieu d'appeler la même fonction manuellement, faisons en sorte que le code le fasse pour nous. Quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/carbon-6.svg)

Si vous observez attentivement le code ci-dessus, la ligne 6 `print1ToNo(currentValue + 1)` appelle la même fonction avec une nouvelle valeur (quelle que soit la valeur actuelle, plus 1, c'est-à-dire currentValue + 1). Et elle continue à le faire, **jusqu'à ce que la currentValue dépasse N**, car c'est à ce moment-là que nous lui avons dit de **retourner**. Maintenant, c'est ce que signifie la récursivité.

## Comment penser de manière récursive

Maintenant, revenons à notre problème principal – nous devons **aplatir un tableau**. Supposons que nous n'avons qu'un seul niveau d'imbrication (bien sûr, nous pouvons avoir plusieurs imbrications, mais pour l'instant nous allons traiter un seul). Le tableau devrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Dribbble-shot---1-4.png)
_Exemple d'entrée - 1 niveau d'imbrication_

Nous allons parcourir le tableau d'entrée index par index.

### Index 0, Valeur = 1

L'index 0 contient un nombre (valeur = 1). Ce n'est qu'un nombre et non un tableau. Avons-nous besoin d'aplatir les nombres ? Non ! Ils vont faire partie du tableau de sortie tel quel. C'est-à-dire que nous n'avons pas besoin de faire quoi que ce soit de spécial aux nombres, nous ne prêtons une attention spéciale qu'aux tableaux.

Donc, notre règle est, si c'est un nombre, poussez-le dans le tableau de sortie et passez à l'index suivant (c'est-à-dire l'index 1 ici).

### Index 1, Valeur = 2

L'index 1 contient également un nombre (valeur = 2). Avons-nous besoin d'aplatir les nombres ? Non ! Ils vont faire partie du tableau de sortie tel quel.

Donc, en suivant notre règle, si c'est un nombre, poussez-le dans le tableau de sortie et passez à l'index suivant (index 2 ici).

### Index 2, Valeur = [ 3, 4 ]

Maintenant, **l'index 2 est un tableau ([ 3, 4 ])** et non un nombre. Nous devons donc trouver un moyen de l'aplatir.

Et si je vous donnais un tableau [3, 4] et que je vous demandais de l'aplatir ? Vous commenceriez à parcourir les éléments du tableau index par index comme nous l'avons fait précédemment. Ensuite, vous réaliseriez que 3 est juste un nombre, donc poussez-le dans le tableau de sortie et passez à l'index suivant.

Eh bien, à l'index suivant, 4 est également juste un nombre, donc poussez-le dans le tableau de sortie. Et c'est fait ! Eh bien, pourquoi ne pas faire la même chose sur `**index 2 ( [ 3, 4 ] )**` de notre tableau d'entrée, alors ?

Vous devez vous demander, eh bien, c'est facile à dire ! Comment allons-nous faire cela en code ? **C'est là que la récursivité entre en jeu.** Chaque fois que nous rencontrons un tableau, nous allons dire à la fonction récursive de prendre ce tableau comme nouvelle entrée et de le résoudre pour nous.

En mettant tout cela en contexte, si c'est juste un nombre, ne faites rien, poussez simplement ce nombre dans notre tableau de sortie et passez à l'index suivant.

Si c'est un tableau, alors prenez ce tableau comme nouvelle entrée et commencez à faire ce que nous avons fait précédemment. (Nous allons faire cette partie en utilisant la récursivité)

## Solution au problème

D'accord, juste pour rappeler, voici notre problème :

Vous recevez un tableau qui contient des nombres et des tableaux imbriqués de nombres. Votre tâche est de retourner un nouveau tableau qui contient tous les nombres de manière linéaire sans aucune imbrication. Gardez à l'esprit que l'imbrication peut être à n'importe quel niveau de profondeur.

Voici la solution à notre problème en utilisant la récursivité :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/carbon-3.svg)
_Solution - Code_

Si vous observez attentivement la fonction nommée **recursion** dans l'extrait de code ci-dessus, nous vérifions si l'élément du tableau sur lequel nous nous trouvons actuellement est un tableau ou non. La variable nommée **`index`** est utilisée pour représenter l'index actuel sur lequel nous nous trouvons, dans le `**inputArray**`.

Si ce n'est pas un tableau, nous poussons simplement cet élément dans notre tableau de sortie et passons à l'index suivant. Sinon, nous commençons un nouvel appel de fonction (récursif) avec le tableau pointé par la variable d'index.

Ce morceau de code fonctionne pour n'importe quel niveau d'imbrication, pas seulement pour 1 niveau d'imbrication ! Et pourquoi cela ? Chaque fois que nous trouvons un tableau et non un nombre, nous initiions un nouvel appel récursif avec ce tableau comme notre entrée pour l'appel récursif.

Donc, peu importe le nombre de tableaux imbriqués que nous avons, la récursivité continuera jusqu'à ce que nous trouvions un nombre, afin que nous commencions à le pousser dans le tableau de sortie !

Voici comment la récursivité fonctionne en coulisses (pour l'exemple précédent) :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Dribbble-shot---1.svg)
_Comment les choses se font !_

## Conclusion

Maintenant, vous savez comment aplatir un tableau en utilisant la récursivité. La récursivité est une approche coûteuse en termes de complexité temporelle et spatiale.

Par exemple, le seul espace supplémentaire que nous utilisons dans notre solution est le `**outputArray**`, que nous utilisons pour stocker la réponse de notre problème.

Mais, ce n'est pas le seul espace que nous utilisons ! Il y a toujours un espace de pile auxiliaire que nous utilisons lorsque nous utilisons la récursivité.

À quel point cet espace de pile auxiliaire est-il grand ? Eh bien, les fonctions récursives sont appelées encore et encore jusqu'à ce que la condition de base soit remplie, n'est-ce pas ? Ces appels de fonction répétés sont placés à l'intérieur de la pile d'appels et retirés lorsque chaque fonction est terminée. Donc, la hauteur maximale de la pile (représente à quel point nos appels récursifs sont profonds) est ce qui constitue l'espace de pile auxiliaire. Quelque chose comme **`O(h) espace, où h est la hauteur maximale de la pile`**.

Maintenant, en ce qui concerne la complexité temporelle, cela dépend de l'entrée. Par exemple : `**[1 , 2, 3, 4, 5]**`**. Une entrée comme celle-ci n'a pas besoin d'être aplatie, mais nous parcourons toujours le tableau entier une fois. Donc, la complexité temporelle est `**O(n) où n est le nombre d'éléments**`.

Maintenant, qu'en est-il de cet exemple ? `**[ [ 1, 2 ], 3, 4, [ 4, [ 5 ] ] ]**` Ici, nous avons 2 options : Si c'est un tableau, appelez la fonction récursive avec ce tableau, comme notre nouveau tableau d'entrée. Si c'est un nombre, poussez-le dans notre tableau de sortie puis récursez à l'index suivant.

Donc, la complexité temporelle va être presque exponentielle. La récursivité est rarement utilisée dans les environnements de production. Mais vous la verrez souvent dans les entretiens techniques :)