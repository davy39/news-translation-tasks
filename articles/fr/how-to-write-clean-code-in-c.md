---
title: Comment écrire du code propre en C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T21:34:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-clean-code-in-c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e51740569d1a4ca3c7c.jpg
tags:
- name: C++
  slug: c-2
- name: clean code
  slug: clean-code
- name: toothbrush
  slug: toothbrush
seo_title: Comment écrire du code propre en C++
seo_desc: "Clean Code Guidelines\nWhen coding, the coding style you follow can be\
  \ really important. Especially when you are working with a team or you plan on sharing\
  \ your code. \nMost of these guidelines are standard and can be applied to most\
  \ programming langua..."
---

# **Directives pour un code propre**

Lors de la programmation, le style de codage que vous suivez peut être vraiment important. Surtout lorsque vous travaillez en équipe ou que vous prévoyez de partager votre code. 

La plupart de ces directives sont standard et peuvent être appliquées à la plupart des langages de programmation. Cependant, ici vous avez des applications et des extraits avec du code C++, afin que vous puissiez vous familiariser plus facilement avec celui-ci. 

Rappelez-vous que ce ne sont que des recommandations pour atteindre la clarté, ce qui peut être une préférence personnelle. Alors prenez ces conseils en compte mais ne les suivez pas à la lettre. Parfois, enfreindre certaines de ces règles peut conduire à un code plus propre.

## **Utiliser de bons noms de variables et faire des commentaires**

Assurez-vous de créer de bons noms de variables. Par exemple, si vous créez un jeu, évitez d'utiliser la variable "a" et utilisez plutôt quelque chose comme "p1" lorsque vous faites référence au joueur 1. 

La [notation hongroise](https://en.wikipedia.org/wiki/Hungarian_notation) est couramment utilisée et peut vous donner quelques directives pour déclarer des variables.

Aussi, S'IL VOUS PLAÎT, utilisez des commentaires.
Sans blague, essayez simplement de lire certains de vos anciens projets sans commentaires… maintenant imaginez être quelqu'un d'autre qui n'a même pas codé cela.

## **Variables globales**

Les variables globales peuvent être faciles à utiliser, et lorsque vous travaillez avec un peu de code, cela peut sembler une excellente solution. Mais lorsque le code devient de plus en plus grand, il devient plus difficile de savoir quand elles sont utilisées.

Au lieu d'utiliser des variables globales, vous pourriez utiliser des variables déclarées dans des fonctions. Cela peut vous aider à savoir quelles valeurs sont passées afin que vous puissiez identifier les erreurs plus rapidement.

```cpp
#include <iostream>
using namespace std;

// Les variables globales sont déclarées en dehors des fonctions
int cucumber; // variable globale "cucumber"
```

## **Utilisation de goto, continue, etc.**

Ceci est une discussion courante parmi les programmeurs. Tout comme les variables globales, ces types d'instructions sont généralement considérés comme de mauvaises pratiques. Elles sont considérées comme mauvaises car elles conduisent à du ["code spaghetti"](https://en.wikipedia.org/wiki/Spaghetti_code). 

Lorsque nous programmons, nous voulons un flux linéaire. Mais lorsque nous utilisons ces instructions, le flux est modifié et conduit à un flux "tordu et emmêlé".

Goto était utilisé dans le passé. Mais lorsque les fonctions while, for, if sont arrivées, cependant, avec l'introduction de ces fonctions, la programmation structurée a été créée. En général, évitez d'utiliser goto sauf si vous êtes sûr que cela rendra votre code plus propre et plus facile à lire. Un exemple pourrait être de l'utiliser dans des boucles imbriquées.

L'utilisation de break et continue est pratiquement la même. Utilisez-les dans les switches et essayez de faire des fonctions avec un seul but afin que vous n'ayez qu'un seul point de sortie.

![img](https://imgs.xkcd.com/comics/goto.png)

## **Éviter de modifier la variable de contrôle à l'intérieur d'une boucle for**

Habituellement, il existe des solutions pour contourner cela qui semblent plus claires et moins confuses, par exemple, les boucles while. Faites ceci :

```cpp
int i=1;
while (i <= 5)
{
    if (i == 2)
        i = 4;

    ++i;
}
```

Au lieu de :

```cpp
for (int i = 1; i <= 5; i++)
{
    if (i == 2)
    {
       i = 4;
    }
    // Faire le travail
}
```

## **Déclarer les constantes et les types en haut**

Ils sont généralement déclarés après les bibliothèques. Cela les regroupe et les rend plus faciles à lire. Pour les variables locales, c'est la même chose : déclarez-les en haut (D'autres personnes préfèrent les déclarer le plus tard possible afin d'économiser de la mémoire voir : [cplusplus.com](http://www.cplusplus.com/forum/general/33612/)).

## **Utiliser une seule fonction de retour à la fin**

Comme je l'ai dit avant, je tends à faire une seule entrée et une seule sortie pour rendre le flux plus clair.

## **Utiliser des accolades même lorsque vous écrivez des lignes uniques**

Faire cela systématiquement vous aidera à le faire plus rapidement. Et au cas où vous voudriez changer le code à l'avenir, vous pourrez le faire sans soucis.

Au lieu de :

```cpp
for (int i = 1; i <= 5; i++)
    //CODE
```

Faites ceci :

```cpp
for (int i = 1; i <= 5; i++)
{
    //CODE
}
```

## **Autres recommandations**

Utilisez `for` lorsque vous connaissez le nombre d'itérations, mais utilisez `while` et `do while` lorsque vous ne le connaissez pas.

Utilisez const, passez par valeur/référence lorsque cela est approprié. Cela aidera à économiser de la mémoire.

Écrivez const en majuscules, les types de données commençant par T et les variables en minuscules.

```cpp
const int MAX= 100;             // Constante
typedef int TVector[MAX];       // Type de données
TVector vector;                 // Vecteur
```