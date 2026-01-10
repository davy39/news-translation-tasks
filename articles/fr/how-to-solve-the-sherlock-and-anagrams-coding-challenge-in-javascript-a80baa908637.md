---
title: Comment résoudre le défi de codage Sherlock et Anagrammes en JavaScript
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-04-23T15:28:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-the-sherlock-and-anagrams-coding-challenge-in-javascript-a80baa908637
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A_R6N6YK1HylRbzIi_0KPw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding challenge
  slug: coding-challenge
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment résoudre le défi de codage Sherlock et Anagrammes en JavaScript
seo_desc: 'This post is going to get you through my solution to a coding challenge
  called “Sherlock and Anagrams.” You may take a look at it in HackerRank.

  I spent a lot of time trying to solve it, with JavaScript. When I tried to google
  it, I could not find a ...'
---

Cet article va vous guider à travers ma solution pour un défi de codage appelé « Sherlock et Anagrammes ». Vous pouvez le consulter sur [HackerRank](https://www.hackerrank.com/challenges/sherlock-and-anagrams).

J'ai passé beaucoup de temps à essayer de le résoudre en JavaScript. Lorsque j'ai essayé de le chercher sur Google, je n'ai pas trouvé de solution JS décente. J'en ai trouvé une seule, mais elle ne fonctionnait pas correctement. De plus, les explications étaient complètement hors de question. C'est pourquoi j'ai décidé d'écrire un article à ce sujet et d'essayer d'inclure des explications claires et faciles à comprendre. Continuez à lire maintenant !

⚠️ ATTENTION : *Je vais présenter ma solution ci-dessous avec des explications courtes sur chaque étape. Si vous souhaitez essayer par vous-même, veuillez vous arrêter ici et vous rendre sur le site de HackerRank.*

### Problème

Deux chaînes sont des [anagrammes](http://en.wikipedia.org/wiki/Anagram) l'une de l'autre si les lettres d'une chaîne peuvent être réarrangées pour former l'autre chaîne. Étant donné une chaîne, trouvez le nombre de paires de sous-chaînes de la chaîne qui sont des anagrammes l'une de l'autre.

Par exemple, pour *s = mom*, la liste de toutes les paires anagrammiques est \[*m, m*\], \[*mo, om*\] aux positions \[\[0\], \[2\]\], \[\[0, 1\], \[1, 2\]\] respectivement.

**Contraintes**

Longueur de la chaîne d'entrée : 2 ≤ |s| ≤ 100

La chaîne *s* ne contient que des lettres minuscules de la plage ascii\[a-z\].

### Analyse

Tout d'abord, nous devons mieux comprendre le problème dans son ensemble. Qu'est-ce qu'un anagramme ? Qu'est-ce qu'une paire anagramme ? Puis-je en voir un ? De plus, que signifie exactement *sous-chaînes* ?

**En d'autres termes, nous devons avoir une image claire de ce que nous essayons de résoudre, avant de le résoudre.**

À partir de la description du problème, nous pouvons déduire tout ce dont nous avons besoin. Continuez à avancer ! ?

*Je pense que c'est un bon moment pour mentionner que le défi en question se trouve dans la section « Dictionnaires et Hashmaps » sur le site HackerRank. Vous penserez probablement que vous devriez utiliser ce type de structure de données pour le résoudre.* ?

#### Anagrammes

Puisque nous allons chercher des anagrammes, commençons par eux. Comme décrit ci-dessus, un anagramme d'un mot est un autre mot qui a la même longueur et est créé avec les mêmes caractères que le mot précédent.

![Image](https://cdn-media-1.freecodecamp.org/images/yqexlCorVcBamgbm1UuU1q2ixW74Zgd50bOs align="left")

*Animation pour l'anagramme « Listen = Silent »*

Nous devrons donc chercher des mots et les comparer avec d'autres mots, afin de voir s'ils sont des paires anagrammiques. Une fois trouvées, nous les compterons simplement.

#### Paires anagrammiques

Puisque nous avons vu ce qu'est un anagramme, il devrait être relativement facile de conclure qu'une paire anagramme est simplement deux chaînes qui sont des anagrammes. Comme « mo » et « om », ou « listen » et « silent ». Nous devrons compter combien de paires de ce type peuvent être trouvées dans une chaîne donnée. Pour ce faire, nous devons diviser cette chaîne originale en sous-chaînes.

#### Sous-chaînes

Les sous-chaînes, comme le suggère le nom, sont des parties d'une chaîne. Ces parties peuvent être une seule lettre ou une paire de lettres, comme nous l'avons vu dans l'exemple ci-dessus — « *m* » ou « *mo* ». Dans notre solution, nous diviserons la chaîne originale en de telles sous-chaînes, puis nous les parcourons et effectuons la comparaison, qui nous dira si nous avons des paires anagrammiques parmi elles.

### Solution

Maintenant que nous avons fait notre analyse, c'est l'heure du spectacle ! ?

Récapitulons :

1. Nous devons trouver toutes les sous-chaînes de la chaîne donnée — créer une méthode pour cela.

2. Nous devons être capables de vérifier si deux chaînes sont des anagrammes — créer une méthode pour cela.

3. Nous devons compter toutes les paires anagrammiques dans la chaîne donnée — créer une méthode pour cela.

4. Combiner tout ce qui précède et retourner le résultat — créer une méthode pour cela.

#### Obtenir toutes les sous-chaînes

Ce sera notre méthode auxiliaire pour trouver toutes les sous-chaînes d'une chaîne donnée :

```js
function getAllSubstrings(str) {
  let i, j, result = [];

  for (i = 0; i < str.length; i++) {
    for (j = i + 1; j < str.length + 1; j++) {
      result.push(str.slice(i, j))
    }
  }
  return result
}
```

Comme vous pouvez le voir, elle a une complexité temporelle de O(n²). Pour notre cas, cela fait le travail, car nous avons une longueur limitée de la chaîne d'entrée (jusqu'à 100 caractères).

#### Vérifier les anagrammes

Ce sera notre méthode auxiliaire pour vérifier si deux chaînes sont des paires anagrammiques :

```js
function isAnagram(str1, str2) {
  const hist = {}

  for (let i = 0; i < str1.length; i++) {
    const char = str1[i]
    if (hist[char]) {
      hist[char]++
    } else {
      hist[char] = 1
    }
  }

  for (let j = 0; j < str2.length; j++) {
    const char = str2[j]
    if (hist[char]) {
      hist[char]--
    } else {
      return false
    }
  }

  return true
}
```

Rappelez-vous que nous avons supposé que nous devrions probablement utiliser des structures de données telles que des tables de hachage ou des dictionnaires (étant donné la section où se trouve ce défi sur HackerRank).

Nous utilisons un simple objet JavaScript pour jouer le rôle d'une table de hachage. Nous faisons deux itérations — une par chaîne. Lorsque nous itérons sur la première, nous ajoutons ses caractères comme clés à la table de hachage et comptons leurs apparitions, qui seront stockées comme leurs valeurs. Ensuite, nous faisons une autre itération sur la deuxième chaîne. Vérifions si ses caractères sont stockés dans notre table de hachage. Si oui — décrémentez leur valeur. Si des caractères sont manquants, ce qui signifie que les deux chaînes ne sont pas une paire anagramme, nous retournons simplement false. Si les deux boucles se terminent, nous retournons true, signifiant que les chaînes analysées sont une paire anagramme.

#### Faire le comptage

C'est la méthode où nous utiliserons l'auxiliaire pour vérifier si une paire est anagramme et la compter. Nous le faisons avec l'aide des tableaux JavaScript et des méthodes qu'ils fournissent. Nous itérons sur un tableau contenant toutes les sous-chaînes de la chaîne originale. Ensuite, nous obtenons l'élément correct et le supprimons du tableau. Puis nous faisons une autre boucle à travers ce tableau et retournons 1 si nous trouvons qu'il y a un anagramme de l'élément actuel. Si rien n'est trouvé, nous retournons 0.

```js
function countAnagrams(currentIndex, arr) {
  const currentElement = arr[currentIndex]
  const arrRest = arr.slice(currentIndex + 1)
  let counter = 0

  for (let i = 0; i < arrRest.length; i++) {
    if (currentElement.length === arrRest[i].length && isAnagram(currentElement, arrRest[i])) {
      counter++
    }
  }

 return counter
}
```

#### Et enfin

La seule chose qui reste à faire maintenant est de combiner tout ce qui précède et de retourner le résultat souhaité. Voici à quoi ressemble la méthode finale :

```js
function sherlockAndAnagrams(s) {
  const duplicatesCount = s.split('').filter((v, i) => s.indexOf(v) !== i).length

  if (!duplicatesCount) return 0
  let anagramsCount = 0

  const arr = getAllSubstrings(s)

  for (let i = 0; i < arr.length; i++) {
    anagramsCount += countAnagrams(i, arr)
  }

  return anagramsCount
}
```

*Peut-être avez-vous remarqué, ici je vérifie d'abord les doublons pour savoir si je dois continuer. Car s'il n'y a pas de lettres dupliquées, alors il n'est pas possible d'avoir un anagramme.*

Et enfin, nous obtenons toutes les sous-chaînes dans un tableau, itérons dessus, comptons les paires anagrammiques trouvées et retournons ce nombre.

Vous pouvez trouver le code complet [ici](https://github.com/mihailgaberov/misc/blob/master/coding-challenges/sherlock-and-anagrams.js).

### Conclusion

Ces types d'exercices sont très bons pour vous faire penser de manière algorithmique. Ils changent également votre façon de travailler dans votre travail quotidien. Ma recommandation serait de faire la même chose que j'essaie de faire — entraînez votre cerveau de temps en temps avec l'un de ceux-ci. Et si vous pouvez — partagez. Je sais que parfois vous n'avez pas le temps pour de tels défis, mais quand vous en avez — allez-y.

Mon sentiment personnel après avoir terminé cela était une satisfaction totale, ce qui est parfaitement compréhensible, compte tenu du temps qu'il m'a fallu pour le faire. Mais au final, cher lecteur, je suis encore plus heureux de pouvoir partager cette expérience avec vous ?!

Merci pour la lecture. Lisez plus de mes articles sur [mihail-gaberov.eu](https://mihail-gaberov.eu/sherlock-and-anagrams/).