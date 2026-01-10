---
title: Comment rendre votre code plus lisible avec l'abstraction
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-05T11:14:16.000Z'
originalURL: https://freecodecamp.org/news/make-your-code-understandable-by-using-abstraction-4b522307130c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*0jBreLbQiLwEDd_g.jpg
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment rendre votre code plus lisible avec l'abstraction
seo_desc: 'By Tiago Antunes

  While you’re learning how to program, it’s common to see people using a term called
  abstraction. You start questioning yourself: what is abstraction and why is it important?

  In this article, I will be explaining to you the concept of...'
---

Par Tiago Antunes

Lorsque vous apprenez à programmer, il est courant d'entendre les gens utiliser un terme appelé **abstraction**. Vous commencez à vous demander : qu'est-ce que l'abstraction et pourquoi est-elle importante ?

Dans cet article, je vais vous expliquer le concept d'abstraction et comment l'utiliser, et je donnerai quelques exemples en Python.

### D'abord, qu'est-ce que l'abstraction ?

Selon mon [professeur de Fondements de la Programmation](https://en.wikipedia.org/wiki/Jo%C3%A3o_Pav%C3%A3o_Martins) :

> « L'abstraction est une spécification simplifiée d'une entité »

Cela signifie qu'une abstraction est une représentation d'une entité de calcul. C'est une façon de dissimuler ses informations particulières et de ne donner que les informations les plus pertinentes au programmeur.

Une abstraction est également situationnelle : chacune répond à un besoin, donc vous pouvez associer _une bonne abstraction à l'utilisation particulière de cette entité_.

Examinons les Arbres Binaires de Recherche (si vous ne savez pas ce que c'est, consultez mon [article](https://medium.freecodecamp.org/trees-in-programming-the-oxygen-of-efficient-code-6c7c11a3dd64) à leur sujet). Nous pouvons définir un nœud comme une entité avec les propriétés suivantes :

```
Un Nœud a :    Nœud * gauche    Nœud * droite    int val
```

Ici, nous dirions qu'un Nœud a deux pointeurs vers d'autres nœuds et une valeur entière. Mais **à quel point cela est-il utile** pour quelqu'un par rapport à une fonction `insert(node, value)` qui insérerait simplement correctement la valeur ? Ainsi, vous n'auriez qu'à l'appeler et ce serait fait. Simple.

C'est ainsi que l'abstraction est utile. Toutes les bibliothèques que vous utilisez dans vos programmes l'utilisent pour que l'utilisation d'une bibliothèque devienne vraiment simple.

### D'accord, mais à quel point l'abstraction des données est-elle bonne ?

L'abstraction des données nous permet de transformer une structure de données complexe en une structure simple et facile à utiliser. L'effet de cela est qu'un programme avec un niveau élevé de complexité de code peut être transformé en un programme qui ressemble à de l'anglais (appelons-le _code de haut niveau_).

Un type de données est composé de 2 choses : des propriétés et des méthodes, qui peuvent être publiques ou privées. Les propriétés publiques sont le seul moyen d'utiliser les données. Elles doivent couvrir toutes les fonctionnalités que vous souhaitez que les données soient capables de faire.

Que se passe-t-il alors si vous utilisez votre code abstrait ? Cela n'a pas vraiment d'importance si vos propriétés internes changent tant que les méthodes reçoivent toujours les mêmes arguments et font la même chose qu'avant. Si quelque chose ne va pas, vous n'avez besoin de le changer qu'une seule fois.

Prenons un exemple et travaillons avec : les Vecteurs

Nous supposerons que les Vecteurs sont :

* Des objets avec 2 valeurs, x et y
* x et y sont tous deux des nombres non négatifs

Ainsi, les Vecteurs sont quelque chose comme (2, 5), (0, 19), et ainsi de suite.

Une bonne façon de créer des abstractions est d'utiliser des Objets. Ils fournissent la dissimulation d'informations et l'anonymat de représentation. Cela permet à l'utilisateur de maintenir l'abstraction.

Commençons par définir notre classe (je ne définirai pas la validation de type pour garder le code plus propre, mais vous devriez le faire) :

![Image](https://cdn-media-1.freecodecamp.org/images/20fnPffDOv4fnL3eURvntvd9XCYz9XS4ui0v)

Nous avons donc défini plusieurs méthodes et nous avons maintenant beaucoup de choses que nous pouvons faire :

![Image](https://cdn-media-1.freecodecamp.org/images/hpEw8SBFt3eI6dQi0klMZHYXrWD9ZlQZ5oUe)

Pour un Vecteur 2D, cela peut sembler simple. Si vous commencez à implémenter cela dans des programmes plus grands et plus complexes, vous remarquerez qu'ils sont vraiment pratiques.

Faisons maintenant une implémentation différente de la classe vecteur (changer son état interne) en quelque chose avec les mêmes méthodes mais avec un code différent :

![Image](https://cdn-media-1.freecodecamp.org/images/UtEBOgQTBAPSEEFf1QCa1AUEDnXtWvZV4f8-)
_L'implémentation est différente, mais le résultat est le même_

Si nous exécutons les mêmes commandes, le résultat sera toujours le même. Cela est dû à l'abstraction que nous avons utilisée, même si le code a complètement changé. C'est pourquoi il est très important d'utiliser l'abstraction. Elle permet de la flexibilité dans votre code et de l'indépendance par rapport au code des autres.

Utilisons maintenant un autre exemple, cette fois avec 2 classes : City et Citizen.

![Image](https://cdn-media-1.freecodecamp.org/images/RdwMtL7GiE7tKQPC3BzTc9-oPhaYGevI5oN4)
_Une Ville est composée de Citoyens_

Et nous obtenons ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/4ACkQNAQl4-GxE9XaPu7uwvcmmza9FZ5CDEX)

```
### SORTIE ###La population de la ville est de 1000, aléatoire : Le citoyen est une femme de 20 ansLa population de la ville est de 1000, aléatoire : Le citoyen est un homme de 74 ans
```

Mais imaginez maintenant que nous voulons changer le fonctionnement de la classe Citizen. Si nous n'avions pas utilisé l'abstraction, nous aurions dû changer tout le code ! C'est beaucoup de travail !

![Image](https://cdn-media-1.freecodecamp.org/images/J9d8o3vpSR3cO1tzWQNnAhvB3B13ccR2o2aE)
_Nous avons maintenant changé la classe Citizen, très rapidement — et tout fonctionne toujours !_

Maintenant, si le code est exécuté à nouveau, nous savons qu'il fonctionne, bien que les résultats soient différents. Comme vous pouvez le voir, nous avons changé une classe entière, mais tout fonctionne !

### Conclusion

Au début, l'abstraction peut sembler inutile. Plus le niveau du langage que vous utilisez est bas, plus il est important d'utiliser l'abstraction. Cela évite d'avoir un code complexe et le garde vraiment simple. Dans des langages comme C, c'est vraiment très utile. Si vous en doutez, consultez ce [projet que j'ai réalisé](https://github.com/TiagoMAntunes/critical_path) où j'ai implémenté l'abstraction et il était vraiment facile de comprendre ce qui se passait.

Si vous avez des questions ou quelque chose dont vous voulez parler ou discuter, laissez un commentaire ci-dessous !

N'oubliez pas de me suivre sur [Instagram](https://www.instagram.com/tm.antunes/) et [Twitter](https://twitter.com/tm_antune) !