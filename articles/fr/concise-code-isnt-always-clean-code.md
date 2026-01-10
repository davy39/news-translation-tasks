---
title: Le code concis n'est pas toujours du code propre – et voici pourquoi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-23T23:29:37.000Z'
originalURL: https://freecodecamp.org/news/concise-code-isnt-always-clean-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/Code-Photography-Images-02.jpg
tags:
- name: best practices
  slug: best-practices
- name: clean code
  slug: clean-code
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
seo_title: Le code concis n'est pas toujours du code propre – et voici pourquoi
seo_desc: "By Kenny Dubroff\nAs developers, we want to write code that works, is readable,\
  \ efficient, concise, and if possible, reusable. \nWhen a lot of us think of clean\
  \ code, we probably fall into the trap of thinking that less code is better code.\
  \ While this ..."
---

Par Kenny Dubroff

En tant que développeurs, nous voulons écrire du code qui fonctionne, qui est lisible, efficace, concis et, si possible, réutilisable. 

Lorsque beaucoup d'entre nous pensent au code propre, nous tombons probablement dans le piège de penser que moins de code est meilleur. Bien que ce soit souvent le cas, ce n'est pas toujours vrai. 

Si je peux accomplir la tâche de manière à ce que d'autres développeurs puissent me suivre et comprendre immédiatement (ou au moins facilement) ce que j'ai fait, c'est ce que je ferai. 

## Alors, qu'est-ce que le code propre ?

De nos jours, il est beaucoup plus important que vous et moi puissions lire le code efficacement que l'appareil (dans _la plupart des cas_).

Lorsque j'écris du code, mon premier objectif est toujours d'accomplir la tâche. Ensuite, j'écris du code pour la lisibilité humaine, puis pour la complexité d'exécution, puis pour la concision. Enfin, si je le peux, je rend le code facilement réutilisable. 

Si je dois écrire du code de manière à ce qu'il ne soit plus facilement lisible par l'homme afin de satisfaire une exigence de complexité/temps ou de réutilisabilité, vous pouvez être sûr qu'il sera très bien documenté.

## Un exemple de ce que je considère comme du code propre

On m'a récemment donné un défi : trouver un seul nombre impair dans un tableau de nombres pairs, ou vice-versa. On m'a donné un tableau d'entiers comme entrée, et je ne savais pas s'il contenait des nombres impairs ou pairs. Il y aurait définitivement un minimum de 3 valeurs dans le tableau et une seule d'entre elles serait impaire/paire.

### Voici ma solution :

```swift
func findOutlier(_ array: [Int]) -> Int {
  //puisque nous sommes garantis d'avoir 3 valeurs, prenons les 3 premières
  let parityArr = [
      array[0],
      array[1],
      array[2]
  ]
  //suivre les nombres impairs ou pairs trouvés dans parityArr || O(1) - (techniquement O(n) mais nous savons que l'entrée ne grandira pas)
  var odd = 0
  var even = 0
  for num in parityArr {
     //le nombre est pair
     if num % 2 == 0 {
         even += 1
     //le nombre est impair
     } else {
         odd += 1
     } 
  }
  //suivre et tester s'il y avait plus de nombres impairs ou pairs dans le tableau
  var isEven = false
  if even > odd {
      isEven = true
  }  
  //retourner la première correspondance qui est une valeur aberrante basée sur le tableau contenant plus de nombres pairs ou impairs || O(n) - nous ne connaissons pas la taille de l'entrée 
  if isEven {
      return array.first(where: ({ $0 % 2 != 0 }))!
  } else {
      return array.first(where: ({ $0 % 2 == 0 }))!
  }
}
```

Si vous le remarquez, j'ai laissé des notes qui incluaient la complexité d'exécution, ou à quel point un algorithme est efficace — même si c'est probablement assez évident si vous vous intéressez à ce genre de choses. J'ai également laissé des notes sur la taille de l'entrée d'une opération donnée (même si encore une fois, c'est assez évident).

## Quand être concis et quand "l'écrire en entier"

Il y a des cas où le code concis peut réduire le temps de compilation, ou l'exécution, ou un certain nombre d'autres choses. Encore une fois, ma principale préoccupation est de savoir si le prochain développeur peut le lire, le suivre facilement et travailler avec.

### Comment être trop concis peut affecter la lisibilité ?

Dans mon retour par exemple, j'aurais pu transformer cette ligne `return array.first(where: ({ $0 % 2 != 0 }))!` en une boucle for où je retournerais la première correspondance. Mais cela ferait exactement la même chose, et grâce à la manière dont cela est nommé, je pense que c'est tout aussi lisible. 

Mais peut-être que vous ne comprenez pas la syntaxe de fermeture, ou votre collègue ne la comprend pas. Ce n'est pas grave - écrivez-la en entier. J'ai choisi de ne pas le faire, car cela me semble tout aussi lisible tout en étant plus concis.

`return array.first(where: { ...` "écrit en entier" est :

```swift
for num in array {
    if num %2 !=0 {
        return num
    }
}
```

Il y a quelques opportunités de rendre le code dans cet exemple plus concis, tout en restant lisible pour la majorité des développeurs.

Ainsi, j'aurais également pu rendre ce bloc :

```swift
var isEven = false
if even > odd {
    isEven = true
}
```

Ressembler à ceci :

`var isEven = even > odd`

Le bloc de retour mentionné ci-dessus pourrait être transformé en une vérification en une ligne en utilisant l'opérateur ternaire, mais il semble y avoir un nombre croissant de développeurs qui ne sont pas familiers avec l'opérateur ternaire. Je pense qu'un bloc if/else est plus lisible dans la plupart des cas également :

```swift
if isEven {
    return array.first(where: ({ $0 % 2 != 0 }))!
} else {
    return array.first(where: ({ $0 % 2 == 0 }))!
}
```

`return isEven ? array.first(where: {$0 %2 != 0}) : array.first(where: {$0 %2 == 0})`

Personnellement, je trouve que ces deux déclarations concises en une ligne sont un peu moins facilement lisibles - surtout lorsque l'opérateur ternaire est impliqué.

Dans tous les cas, j'étais assez satisfait de ma solution - elle a passé tous les tests unitaires, elle était assez efficace et elle était lisible par l'homme. Mais lorsque j'ai vu les solutions des autres, au début j'ai eu un peu honte de la mienne, rudimentaire...

Beaucoup d'entre eux utilisaient filter, beaucoup utilisaient l'opérateur ternaire. La plupart étaient beaucoup plus concis. 

### Un exemple d'être trop concis

La solution la mieux notée était de 2 lignes de code que j'ai eu du mal à lire au début — mais ce code fera définitivement le travail. Il peut être plus efficace que ma solution dans certains cas, et il est évidemment très concis :

```swift
func findOutlier(_ array: [Int]) -> Int {
    let odd = array.filter{$0 % 2 != 0}
    return odd.count > 1 ? array.filter{$0 % 2 == 0}[0] : odd[0]
}
```

Ces deux exemples répondent au premier critère de l'écriture de code propre (ou vraiment, de n'importe quel code) - ils fonctionnent. Ils sont également concis, bien que ma solution pourrait être plus concise. À première vue, j'ai pensé que la solution plus concise était excellente. Elle est élégante, efficace et concise. 

Ensuite, j'ai commencé à décomposer le retour en un if/else et j'ai réalisé que ma solution est probablement plus efficace la plupart du temps. Je ne parcourt jamais l'ensemble du tableau plus d'une fois, et seulement si la valeur aberrante de parité est le dernier nombre du tableau. 

C'est toujours une bonne solution, mais je ne dirais pas qu'elle est _géniale_ (ou comme beaucoup l'ont noté sur le site - une meilleure pratique).

Dans le cas d'un tableau majoritairement pair dans la solution concise, il serait filtré deux fois. Une fois pour créer le tableau appelé odd (qui pourrait également être mieux nommé) — c'est l'ensemble du tableau qui est parcouru. Ensuite, une autre fois s'il s'avère que ce n'est pas un tableau majoritairement impair. 

Ce n'est pas grave s'il n'y a que 3 nombres. Mais étant donné un tableau de 10 000 nombres, vous regardez un morceau de temps où votre utilisateur est laissé en attente pour que quelque chose soit calculé alors que cela n'a pas besoin de l'être.

Une autre chose à noter à propos de ma solution par rapport à la solution concise est que ma réponse est retournée dès qu'elle est trouvée dans le tableau. 

Supposons que le tableau d'entrée était impair, et que le nombre pair était le premier nombre du tableau. Dans ma solution, il serait calculé et retourné presque immédiatement, tandis que dans la solution concise, nous attendrions que l'ensemble du tableau soit filtré avant de retourner la réponse.

### Une note sur la réutilisabilité

J'ai abordé la réutilisabilité plus tôt, mais nous n'en avons pas beaucoup parlé. Le code réutilisable signifie que vous pouvez l'utiliser dans plus d'une situation. 

C'est l'une des principales préoccupations de l'écriture de code propre, mais seulement lorsqu'elle s'applique. Nous pouvons le faire en utilisant des paramètres dans les fonctions qui sont flexibles pour différents cas d'utilisation, et d'autres choses qui vont dans le sens de pouvoir utiliser notre code ailleurs sans aucune ou peu de modification.

**Mais comment l'écriture de code réutilisable peut-elle affecter la lisibilité ?**  
J'aurais pu rendre cette fonction entière générique. Elle répondrait toujours aux critères et la rendrait plus réutilisable. Nous pourrions vérifier n'importe quel type numérique par exemple, mais cela n'était pas dans le cadre de ce projet, et le faire rendrait le code moins lisible si vous n'êtes pas familier avec la syntaxe générique.

## Garder le code propre évite les pièges

L'un des pièges de l'écriture de code un peu trop concis est qu'il est difficile de prendre en compte les cas limites. Cela est dû au fait qu'il est plus difficile de voir les "pièces mobiles" d'un seul coup d'œil.

Je ne dis pas que ma solution est parfaite. Je peux déjà voir une façon de la rendre plus efficace (nous pourrions sauter la dernière opération O(n) dans certains cas) et rester lisible. 

Mais le point est, je peux revenir à ce code à tout moment dans un avenir proche ou lointain, voir facilement comment il fonctionne et comment je peux l'améliorer.

Rappelez-vous simplement qu'il y a beaucoup de choses qui entrent en jeu dans l'écriture de code propre. Propre ne signifie pas **uniquement** concis ! Écrivez votre code de manière à ce que d'autres développeurs puissent travailler avec — chaque humain qui travaille dessus vous en remerciera.