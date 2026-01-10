---
title: Qu'est-ce qu'un Algorithme ? Définition d'Algorithme pour les Débutants en
  Informatique
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-12-13T00:38:26.000Z'
originalURL: https://freecodecamp.org/news/what-is-an-algorithm-definition-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/laptop-gfe4d4bfc0_1280.png
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: Qu'est-ce qu'un Algorithme ? Définition d'Algorithme pour les Débutants
  en Informatique
seo_desc: 'If you’re a student and want to study computer science, or you’re learning
  to code, then there’s a chance you’ve heard of algorithms. Simply put, an algorithm
  is a set of instructions that performs a particular action.

  Contrary to popular belief, an ...'
---

Si vous êtes étudiant et souhaitez étudier l'informatique, ou si vous apprenez à coder, alors il est probable que vous ayez entendu parler des algorithmes. En termes simples, un algorithme est un ensemble d'instructions qui effectue une action particulière.

Contrairement à la croyance populaire, un algorithme n'est pas un morceau de code qui nécessite des connaissances extrêmement avancées pour être implémenté. En même temps, je ne dirai pas qu'un algorithme est facile à implémenter non plus. Certains peuvent l'être, mais cela dépend de ce que vous essayez de faire.

En fin de compte, la meilleure façon de s'améliorer en algorithmes est de les pratiquer régulièrement.

Dans cet article, vous apprendrez tout sur les algorithmes afin d'être préparé la prochaine fois que vous en rencontrerez un, ou que vous devrez en écrire un vous-même. Je partagerai également quelques ressources de freeCodeCamp qui vous aideront à apprendre à écrire des algorithmes dans différents langages.

## Ce que nous allons couvrir
- [Qu'est-ce qu'un Algorithme exactement ?](#heading-quest-ce-quun-algorithme)
- [Pourquoi avez-vous besoin d'un Algorithme ?](#heading-pourquoi-avez-vous-besoin-dun-algorithme)
- [Types d'Algorithmes](#heading-types-dalgorithmes)
- [Quel langage de programmation est le meilleur pour écrire des algorithmes ?](#quel-langage-de-programmation-est-le-meilleur-pour-ecrire-des-algorithmes)
- [Ressources pour apprendre les algorithmes](#heading-ressources-pour-apprendre-les-algorithmes)
- [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un Algorithme exactement ?
Un algorithme est un ensemble d'étapes pour résoudre un problème connu. La plupart des algorithmes sont implémentés pour fonctionner selon les **quatre étapes** suivantes :

- prendre une entrée
- accéder à cette entrée et s'assurer qu'elle est correcte
- montrer le résultat
- terminer (l'étape où l'algorithme cesse de fonctionner)

Certaines étapes de l'algorithme peuvent s'exécuter de manière répétée, mais en fin de compte, la **terminaison** est ce qui met fin à un algorithme.

Par exemple, l'algorithme ci-dessous trie les nombres par ordre décroissant. Il parcourt les nombres spécifiés jusqu'à ce qu'il les organise par ordre décroissant, puis se termine lorsqu'il n'y a plus de nombres à trier :

```js
function sortNumbersInDescendingOrder(nums) {
  let sortedNums = false;
  while (!sortedNums) {
    sortedNums = true;
    for (let i = 1; i < nums.length; i++) {
      if (nums[i] > nums[i - 1]) {
        [nums[i], nums[i - 1]] = [nums[i - 1], nums[i]];
        sortedNums = false;
      }
    }
  }
  return nums;
}

const unsortedNums = [2, 3, 1, 6, 4, 5, 10, 9, 8, 7];
const sortedNums = sortNumbersInDescendingOrder(unsortedNums);

console.log(sortedNums); // [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
```

Pour une base théorique, par exemple, un algorithme pour diviser deux nombres et montrer le reste pourrait suivre les étapes ci-dessous :

- **Étape 1** : l'utilisateur entre le premier et le deuxième nombre – le dividende et le diviseur
- **Étape 2** : l'algorithme écrit pour effectuer la division prend les nombres, puis place un signe de division entre le dividende et le diviseur. Il vérifie également s'il y a un reste.
- **Étape 3** : le résultat de la division et le reste sont montrés à l'utilisateur
- **Étape 4** : l'algorithme se termine

Voici comment ce type d'algorithme est implémenté en JavaScript :
```js
function divideTwoNums(num1, num2) {
  const result =  num1 / num2;
  const remainder = num1 % num2
  
  return `Le résultat est ${result} reste ${remainder}`
}

const result = divideTwoNums(21, 2)

console.log(result) // Le résultat est 10.5 reste 1
```

S'il y a une erreur, l'algorithme peut ne pas s'exécuter, ou peut retourner une sortie incorrecte. Si le programmeur qui a écrit l'algorithme a pris en compte l'expérience utilisateur, alors un gestionnaire d'erreurs pourrait montrer une erreur à l'utilisateur et lui faire savoir quoi faire.

## Pourquoi avez-vous besoin d'un Algorithme ?
Si vous êtes l'un de ces étudiants en informatique qui se demandent "pourquoi les algorithmes", voici quelques raisons pour lesquelles vous devriez les apprendre :

**Résolution de problèmes** : être capable d'écrire un algorithme améliore votre capacité à résoudre des problèmes. Il est communément admis que si vous pouvez résoudre un problème avec une chose, vous pouvez résoudre des problèmes avec une autre chose étroitement liée. Donc, si vous pouvez résoudre des problèmes avec Python, vous pouvez résoudre des problèmes avec JavaScript.

**Évolutivité** : un algorithme aide votre logiciel/application/site web à répondre de manière appropriée aux demandes.

**Utilisation appropriée des ressources** : choisir le bon algorithme garantit une utilisation appropriée des ressources telles que la mémoire, le stockage, le réseau, et autres.

## Types d'Algorithmes
Les algorithmes en informatique peuvent être largement catégorisés en algorithmes de recherche et de tri :
- Tri – tri par sélection, tri à bulles, tri par insertion, tri par fusion, tri rapide, et ainsi de suite.
- Recherche – recherche binaire, recherche exponentielle, recherche par saut, et ainsi de suite.

Mais il existe de nombreux types d'algorithmes que les programmeurs utilisent régulièrement. Voici quelques autres types d'algorithmes courants organisés par catégorie :

- Hachage – SHA-256, SHA-1
- Force brute – essai et erreur
- Diviser pour régner – algorithme de tri par fusion
- Glouton – algorithme de Prim, algorithme de Kruskal
- Récursif – factoriels informatiques

## Quel langage de programmation est le meilleur pour écrire des algorithmes ?
Vous pouvez écrire des algorithmes dans n'importe quel langage de programmation. Il n'y a aucun avantage à utiliser un langage plutôt qu'un autre.

Chaque langage a ses forces et ses faiblesses, et chacun a une syntaxe et des fonctionnalités uniques. Ainsi, l'écriture d'un algorithme peut sembler différente dans un langage par rapport à un autre.

Mais les algorithmes sont des concepts universels. Donc, si vous pouvez écrire un **tri à bulles** en Python, vous devriez également être capable de l'écrire en JavaScript ou en C#.

## Ressources pour apprendre les algorithmes
Voici quelques vidéos de la chaîne YouTube freeCodeCamp qui peuvent vous aider à apprendre les algorithmes efficacement :
- [Algorithmes et Structures de Données Tutoriel - Cours Complet pour Débutants](https://www.youtube.com/watch?v=8hly31xKli0)
- [Algorithmes en Python – Cours Complet pour Débutants](https://www.youtube.com/watch?v=fW_OS3LGB9Q)
- [Cours sur les Structures de Données de Facile à Avancé - Tutoriel Complet par un Ingénieur Google](https://www.youtube.com/watch?v=RBSGKlAvoiM&list=PLR69o5h4xAwUgZHf8Y6V-KukXHBlbAcc1&index=2)
- [Programmation Dynamique - Apprendre à Résoudre des Problèmes Algorithmiques et des Défis de Codage](https://www.youtube.com/watch?v=oBt53YbR9Kk&list=PLR69o5h4xAwUgZHf8Y6V-KukXHBlbAcc1&index=4)
- [Comprendre les Algorithmes de Tri](https://www.youtube.com/watch?v=l7-f9gS8VOs&list=PLR69o5h4xAwUgZHf8Y6V-KukXHBlbAcc1&index=14)

De plus, la certification interactive [Algorithmes et Structures de Données JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) sur freeCodeCamp peut vous donner un cours accéléré sur la pensée algorithmique en JavaScript.

## Conclusion
Dans cet article, nous avons passé en revue ce qu'est un algorithme, leurs types et les ressources pour apprendre les algorithmes.

Si vous avez lu jusqu'ici, la prochaine chose que vous devriez faire est de commencer à apprendre les algorithmes avec une ou plusieurs des ressources listées dans cet article.

Merci d'avoir lu.