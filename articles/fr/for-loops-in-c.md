---
title: Les boucles For en C – Expliquées avec des exemples de code
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-11-03T15:56:21.000Z'
originalURL: https://freecodecamp.org/news/for-loops-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/for.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: c programming
  slug: c-programming
- name: Loops
  slug: loops
seo_title: Les boucles For en C – Expliquées avec des exemples de code
seo_desc: "In programming, you'll use loops when you need to repeat a block of code\
  \ multiple times. \nThese repetitions of the same block of code a certain number\
  \ of times are called iterations. And there's a looping condition that decides the\
  \ number of iteratio..."
---

En programmation, vous utiliserez des boucles lorsque vous devrez répéter un bloc de code plusieurs fois. 

Ces répétitions du même bloc de code un certain nombre de fois sont appelées _itérations_. Et il y a une condition de boucle qui détermine le nombre d'itérations. 

Les boucles `for` et `while` sont largement utilisées dans presque tous les langages de programmation.

Dans ce tutoriel, vous apprendrez à propos des boucles `for` en C. En particulier, vous apprendrez :

* la syntaxe pour utiliser les boucles `for`, 
* comment les boucles `for` fonctionnent en C, et
* la possibilité d'une boucle `for` infinie.

Commençons.

## Syntaxe de la boucle `for` en C et son fonctionnement

Dans cette section, vous apprendrez la syntaxe de base des boucles `for` en C.

La syntaxe générale pour utiliser la boucle `for` est montrée ci-dessous :

```
for(initialiser; vérifier_condition; mettre_à_jour)
    {
        //faire ceci
    }
```

Dans la syntaxe ci-dessus :

* `initialiser` est l'instruction d'initialisation – la variable de contrôle de boucle est initialisée ici.
* `vérifier_condition` est la condition qui détermine si la boucle doit continuer. 

> Tant que `vérifier_condition` est _vraie_, le corps de la boucle est exécuté.

* L'instruction `mettre_à_jour` met à jour la variable de contrôle de boucle après que les instructions du corps de la boucle soient exécutées.

### Flux de contrôle dans les boucles `for` en C

Le flux de contrôle est le suivant :

1. Initialiser le compteur – l'instruction `initialiser` est exécutée. Cela ne se produit qu'une seule fois, au début de la boucle.
2. Vérifier si la condition de boucle est vraie – l'expression `vérifier_condition` est évaluée. Si la condition est _vraie_, passer à l'étape 3. Si _fausse_, quitter la boucle.
3. Exécuter les instructions du corps de la boucle.
4. Mettre à jour le compteur – l'instruction `mettre_à_jour` est exécutée.
5. Aller à l'étape 2.

Cela est également illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-66.png)
_Boucle For en C_

Maintenant que vous avez une idée de comment les boucles `for` fonctionnent, prenons un exemple simple pour voir la boucle `for` en action.

### Exemple de boucle `for` en C

Écrivons une simple boucle `for` pour compter jusqu'à 10, et afficher la valeur du compteur à chaque passage dans la boucle.

```c
#include <stdio.h>

int main() 
{
   for(int count = 0; count <= 10; count++)
   {
       printf("%d\n",count);
   }
   return 0;
}
```

Dans l'extrait de code ci-dessus,

* `count` est la variable de compteur, et elle est initialisée à `0`.
* La condition de test ici est `count <= 10`. Par conséquent, `count` peut être au plus 10 pour que la boucle continue.
* Dans le corps de la boucle, la valeur de `count` est affichée.
* Et la valeur de `count` est augmentée de 1.
* Le contrôle atteint ensuite la condition `count <= 10` et la boucle continue si la condition est évaluée à vraie.
* Dans cet exemple, la condition de boucle `count <= 10` est évaluée à _faux_ lorsque la valeur de count est 11 – et votre boucle se termine. 

Et voici le résultat :

```
//Sortie
0
1
2
3
4
5
6
7
8
9
10
```

Lorsque vous utilisez des boucles, vous devez toujours vous assurer que votre boucle _se termine_ à un moment donné. 

> Vous savez que la boucle continue tant que `vérifier_condition` est _vraie_. Et la boucle s'arrête une fois que `vérifier_condition` devient _fausse_. Mais que se passe-t-il lorsque votre condition de boucle est _toujours vraie_ ? 

Eh bien, c'est là que vous tombez dans une boucle infinie – votre boucle continue indéfiniment, jusqu'à ce que votre programme plante, ou que votre système s'éteigne.😢

Vous en apprendrez plus sur les boucles infinies dans la section suivante.

## Boucle `for` infinie

Lorsque votre boucle ne s'arrête pas et continue de tourner indéfiniment, vous avez une boucle infinie. Prenons quelques exemples pour comprendre cela.

▶ Dans la construction de la boucle `for`, si vous ne spécifiez pas la condition de test (`vérifier_condition`), elle est considérée comme _vraie_ par défaut. 

En conséquence, votre condition ne devient jamais fausse. Et la boucle continuera de tourner indéfiniment jusqu'à ce que vous forciez l'arrêt du programme.

Cela est montré dans l'extrait de code ci-dessous :

```c
#include <stdio.h>

int main()
{
    
    for(int i = 0; ; i++) //la condition de test n'est pas mentionnée
    {
        printf("%d ",i);
    }
    
    return 0;
}

```

▶ Voici un autre exemple. 

Vous initialisez la variable de compteur `i` à 10. Et `i` augmente de 1 après chaque itération. 

Remarquez comment la condition de test est `i > 0`. La valeur de `i` ne sera-t-elle pas toujours supérieure à 0 ?

Vous avez donc une autre boucle infinie, comme montré :

```c
#include <stdio.h>

int main()
{
    
    for(int i = 10; i > 0 ; i++) //la condition de test est toujours VRAIE
    {
        printf("%d ",i);
    }
    
    return 0;
}

```

▶ Dans cet exemple, votre variable de compteur `i` est initialisée à `0`. Mais elle diminue de 1 à chaque itération. 

En conséquence, `i` est toujours inférieur à 10. Donc la condition `i < 10` est _toujours vraie_, et vous aurez une boucle infinie.

```c
#include <stdio.h>

int main()
{
    
    for(int i = 0; i < 10 ; i--) //la condition de test est toujours VRAIE
    {
        printf("%d",i);
    }
    
    return 0;
}
```

Pour éviter de tomber dans des boucles infinies, vous devez définir correctement la condition de boucle.

Si vous êtes débutant, vous poser les questions suivantes peut aider.

> Que veux-je que cette boucle fasse ?   
> Combien de fois veux-je que la boucle s'exécute ?   
> Quand ma boucle doit-elle s'arrêter ? 

Et ensuite, vous pouvez définir votre construction de boucle en conséquence. 👨‍💻

## Conclusion

J'espère que vous avez trouvé ce tutoriel utile.

Pour résumer, vous avez appris la syntaxe des boucles `for` et comment elles fonctionnent. Vous savez également comment anticiper la possibilité de boucles `for` infinies et comment les éviter en définissant soigneusement votre condition de boucle. 

À bientôt dans un autre tutoriel. En attendant, bon codage !