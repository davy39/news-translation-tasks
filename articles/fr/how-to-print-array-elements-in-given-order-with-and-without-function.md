---
title: Comment imprimer les éléments d'un tableau dans un ordre donné avec ou sans
  fonction
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-02-16T21:58:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-print-array-elements-in-given-order-with-and-without-function
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/func.png
tags:
- name: arrays
  slug: arrays
- name: C++
  slug: c-2
- name: Problem Solving
  slug: problem-solving
seo_title: Comment imprimer les éléments d'un tableau dans un ordre donné avec ou
  sans fonction
seo_desc: 'If you are learning to solve problems using a programming language, you''ve
  likely faced the problem of printing array elements in a given order or in reverse
  order.

  You might have also needed to do this by either using a user-defined function or
  not ...'
---

Si vous apprenez à résoudre des problèmes en utilisant un langage de programmation, vous avez probablement été confronté au problème d'impression des éléments d'un tableau dans un ordre donné ou dans l'ordre inverse.

Vous avez peut-être également dû le faire soit en utilisant une fonction définie par l'utilisateur, soit sans utiliser de fonction du tout.

Si ce problème vous semble un peu compliqué, ne vous inquiétez pas ! Je suis là pour vous aider. Alors, plongeons-nous rapidement dans la question et voyons comment cela fonctionne.

🎥 Si vous êtes du genre à aimer suivre avec une vidéo, j'ai également créé une vidéo pour vous :

%[https://youtu.be/pACJ2_bGaZ0]

## Comprendre la question – puis commencer à résoudre

Pour résoudre n'importe quel type de problème, la première chose à faire est de comprendre la question. Non seulement cela, mais vous devez également prêter une attention particulière à toutes les instructions, y compris les critères requis pour résoudre ce problème.

Si votre question vous demande d'utiliser la récursivité, c'est la technique que vous emploierez. Si votre question vous demande de ne pas utiliser de fonctions spéciales intégrées, vous les éviterez.

Pour cet article, j'utiliserai une seule question mais avec deux critères différents. Je passerai par le processus pour vous aider à comprendre ce que vous devrez faire dès le début pour résoudre le problème.

### Voici la question avec ses critères :

Créez un tableau d'entiers. Prenez les éléments du tableau en entrée de l'utilisateur et imprimez tous les éléments du tableau dans l'ordre donné et ensuite dans l'ordre inverse. Vous ne pouvez pas utiliser de fonction définie par l'utilisateur.

Très bien, maintenant que nous avons notre question, assurez-vous de l'avoir lue entièrement. Si la lire une fois ne la rend pas claire dans votre esprit, alors lisez-la deux ou trois fois – ou même plus.

Ensuite, examinez également les critères donnés avec attention. La question vous dit que vous ne pouvez pas utiliser de fonction définie par l'utilisateur. Cela signifie que vous ne pouvez pas ajouter de fonction définie manuellement par l'utilisateur dans votre code comme `myFunction()`, et ainsi de suite.

Pour cet article, j'utiliserai le langage de programmation **C++**. Mais si vous pouvez comprendre le concept de base, alors vous pouvez utiliser n'importe quel autre langage de programmation pour résoudre ce problème. Après avoir résolu le problème, assurez-vous d'ajouter votre solution [à ce dépôt GitHub](https://github.com/FahimFBA/problem-solving-made-easy).

De plus, si vous aimez résoudre des problèmes en utilisant des langages de programmation, assurez-vous de consulter [ma playlist YouTube en cours où je résous des problèmes en utilisant le langage de programmation](https://www.youtube.com/playlist?list=PL7ZCWbO2Dbl5p3wf0IOHeIZ6PHxTI3ADD).

### Comment résoudre le problème

En C/C++, si vous déclarez un tableau sans initialiser la valeur, vous devez également spécifier la taille du tableau.

Lorsque vous déclarez le tableau avec la taille du tableau, il prend automatiquement l'espace nécessaire en mémoire pour l'ensemble du tableau. Donc, si vous prenez un tableau plus grand que ce dont vous avez réellement besoin, vous gaspillerez de la mémoire, car il prend l'espace complet en mémoire pour le tableau complet, que vous utilisiez tous les index ou non.

Donc, tout d'abord, nous voulons que l'utilisateur saisisse la taille du tableau (combien de nombres il veut que nous traitons). Ensuite, nous créerons le tableau avec la taille de tableau donnée. De cette manière, nous pouvons éviter le gaspillage inutile de mémoire.

Eh bien, comme les ordinateurs d'aujourd'hui sont plus puissants, vous ne remarquerez probablement aucune différence dans le gaspillage de mémoire, car il serait assez négligeable. Mais croyez-moi, vous devez comprendre comment économiser de la mémoire, car c'est l'une des plus grandes préoccupations dans le monde d'aujourd'hui. De plus, vous ne savez jamais quand cette connaissance vous aidera plus tard, n'est-ce pas ?

```cpp
    cout << "Entrez la taille du tableau : ";
    int arraySize;
    cin >> arraySize;
    int arr[arraySize];
```

Eh bien, après avoir déclaré notre tableau, nous prendrons les éléments du tableau de l'utilisateur. Nous pouvons simplement utiliser une boucle `for()` pour cela.

```cpp
    cout << "Entrez les éléments du tableau " << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cin >> arr[i];
    }
```

De cette manière, nous pouvons prendre chaque valeur de l'utilisateur et la stocker dans notre tableau de manière séquentielle. Gardez à l'esprit que le tableau commence toujours par l'index `0` (le premier élément est à l'index `0`, le deuxième est à l'index `1`, et ainsi de suite).

Il est maintenant temps d'imprimer tous les éléments du tableau (la valeur que chaque index du tableau possède) dans l'ordre donné. Cela signifie que nous devons imprimer l'ensemble du tableau dans le même ordre que celui que nous avons reçu de l'utilisateur.

```cpp
    // impression du tableau dans le bon ordre
    cout << "Impression du tableau dans l'ordre original" << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cout << arr[i] << " ";
    }
```

Pour imprimer le tableau dans l'ordre inverse, nous pouvons simplement imprimer le tableau dans une direction inverse. De cette manière, la valeur de l'index le plus élevé du tableau sera imprimée en premier. Ensuite, la valeur de l'index avant-dernier (du côté droit du tableau) serait imprimée en deuxième position, et ainsi de suite.

```cpp
    // impression du tableau dans l'ordre inverse
    cout << "\nImpression du tableau dans l'ordre inversé" << endl;
    for (int i = arraySize - 1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }
```

C'est tout ! Grâce à cela, vous pouvez résoudre le problème facilement. Remarquez que nous n'avons pas utilisé de fonction définie par l'utilisateur dans l'ensemble de notre code. Ainsi, nous nous sommes également assurés que nous avons réussi à répondre à tous les critères.

Le code entier ressemble maintenant à ceci :

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    cout << "Entrez la taille du tableau : ";
    int arraySize;
    cin >> arraySize;
    int arr[arraySize];
    cout << "Entrez les éléments du tableau " << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cin >> arr[i];
    }
    // impression du tableau dans le bon ordre
    cout << "Impression du tableau dans l'ordre original" << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cout << arr[i] << " ";
    }
    // impression du tableau dans l'ordre inverse
    cout << "\nImpression du tableau dans l'ordre inversé" << endl;
    for (int i = arraySize - 1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }    
}
```

### Voici un autre exemple de question et de critères :

Créez un tableau d'entiers. Prenez les éléments du tableau en entrée de l'utilisateur et imprimez tous les éléments du tableau dans l'ordre donné et ensuite dans l'ordre inverse. Vous devez utiliser une fonction définie par l'utilisateur pour imprimer le tableau dans l'ordre inverse.

Maintenant, cette fois, les critères ont été modifiés. La seule différence est que nous devons utiliser une fonction définie par l'utilisateur maintenant.

Si vous pouvez comprendre la technique précédente et le code, alors vous avez probablement déjà deviné comment résoudre ce problème. Nous devons déplacer la partie du code qui imprime le tableau dans l'ordre inverse vers une nouvelle fonction définie par l'utilisateur. Faire cela simplement résoudra notre problème.

Par exemple, je vais nommer la nouvelle fonction définie par l'utilisateur `printReversely(int arr[], int arraySize)`. Vous pouvez la nommer comme vous le souhaitez en suivant les conventions de nommage du C++ (ou quel que soit le langage de programmation que vous utilisez).

Je vous donne simplement le code entier pour l'instant :

```cpp
#include <bits/stdc++.h>
using namespace std;
void printReversely(int arr[], int arraySize);
int main()
{
    cout << "Entrez la taille du tableau : ";
    int arraySize;
    cin >> arraySize;
    int arr[arraySize];
    cout << "Entrez les éléments du tableau " << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cin >> arr[i];
    }
    // impression du tableau dans le bon ordre
    cout << "Impression du tableau dans l'ordre original" << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cout << arr[i] << " ";
    }
    // impression du tableau dans l'ordre inverse
    cout << "\nImpression du tableau dans l'ordre inversé" << endl;
    printReversely(arr, arraySize);
}

void printReversely(int arr[], int arraySize)
{
    for (int i = arraySize - 1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }
}
```

En C/C++, l'exécution du code commence toujours à partir du coin supérieur gauche.

Comme j'ai écrit ma fonction `printReversely(int arr[], int arraySize)` après la fonction principale, j'ai ajouté la partie déclaration avant la fonction **main()**. Cela aidera le compilateur à déterminer s'il a accès à la fonction ou non. Si vous ne le faites pas, vous obtiendrez une erreur.

Mais si vous écrivez la fonction entière `printReversely(int arr[], int arraySize)` avant la fonction **main()**, vous n'avez pas nécessairement besoin d'ajouter la déclaration à nouveau avant cela.

## Conclusion

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez entrer en contact avec moi, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/) et [GitHub](https://github.com/FahimFBA).

Vous pouvez également [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers types de langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !