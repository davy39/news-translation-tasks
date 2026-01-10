---
title: Comment obtenir la valeur ASCII de n'importe quel caractère avec une ligne
  de code
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-02-28T16:20:44.000Z'
originalURL: https://freecodecamp.org/news/get-the-ascii-value-of-any-character-with-one-line-of-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/ascii-banner.jpg
tags:
- name: ascii
  slug: ascii
- name: c programming
  slug: c-programming
seo_title: Comment obtenir la valeur ASCII de n'importe quel caractère avec une ligne
  de code
seo_desc: "When you're working on a project or computer program, you might need to\
  \ use the ASCII value of a certain character. \nThis is a common phenomenon in competitive\
  \ programming, as well – we typically need to use the ASCII value of characters\
  \ when solving..."
---

Lorsque vous travaillez sur un projet ou un programme informatique, vous pourriez avoir besoin d'utiliser la valeur ASCII d'un certain caractère. 

C'est un phénomène courant en programmation compétitive, ainsi qu'en général – nous avons généralement besoin d'utiliser la valeur ASCII des caractères lors de la résolution de certains problèmes sur diverses plateformes en ligne comme HackerRank, Codeforces et Codechef.

Que faisons-nous dans ces situations ? La plupart d'entre nous recherchent simplement la valeur ASCII sur Internet, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-200516.png)

Oui, il est vrai que nous pouvons obtenir la valeur ASCII de n'importe quel caractère directement en recherchant sur Internet. Mais parfois, vous pourriez ne pas pouvoir les rechercher sur Internet. Par exemple, si vous passez un examen, vous pourriez être interdit d'accéder à Internet pendant l'examen. 

Alors, que feriez-vous si vous ne vous souvenez pas de la valeur ASCII du caractère dont vous avez besoin, et que vous êtes également interdit de la rechercher sur Internet ? 

Pas de panique ! Dans cet article, je vais résoudre le problème pour vous. Vous n'aurez plus jamais besoin d'Internet pour rechercher la valeur ASCII de n'importe quel caractère.

## Mise en route

Supposons que vous écrivez un programme en C, et que vous avez également besoin de connaître la valeur ASCII d'un caractère. Ne craignez rien ! Vous n'avez pas besoin de passer à d'autres langages juste pour obtenir la valeur à l'aide de code – vous pouvez le faire dans votre code C ! Suivez le code ci-dessous :

```c
#include<stdio.h>
int main()
{
    char ch = 'A';
    printf("%c\n" , ch);
}
```

Pouvez-vous me dire ce que nous obtiendrions en sortie ? Si vous pensez que vous obtiendriez le caractère lui-même en sortie, alors vous avez raison !

```c
// A
```

J'ai utilisé `//` pour indiquer le commentaire ici.

Permettez-moi de vous donner une belle capture d'écran ci-dessous également :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-184023.png)

À la ligne 4, je prends un type de données caractère comme `ch`, et j'assigne un caractère à cette variable. Pour l'instant, je prends le caractère 'A', puis j'imprime le caractère lui-même à la ligne 5.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-184216.png)

Mais si j'utilise `%d` au lieu de `%c`, alors je lui dis d'imprimer la valeur entière du caractère, et non le caractère lui-même. 

Si nous parlons de la valeur entière d'un caractère, alors elle peut représenter une chose – la valeur ASCII du caractère, n'est-ce pas ? Le code exemple est donné ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-184314.png)
_Entrée exemple_

Dans la sortie, nous obtiendrons la valeur ASCII du caractère 'A'.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-184401.png)

C'est ainsi que nous obtenons la valeur ASCII de n'importe quel caractère en utilisant le code ci-dessus. 

Permettez-moi de vous présenter une chose plus intéressante maintenant. Comme je ne vous montre que le processus d'obtention de la valeur ASCII de l'alphabet anglais, vous pourriez vous demander si le code ne fonctionne que pour obtenir la valeur ASCII d'une lettre de l'alphabet ou s'il fonctionne avec n'importe quel caractère valide. 

Eh bien, la bonne nouvelle est que ce processus fonctionne pour n'importe quel caractère valide ! Permettez-moi de vous montrer plus d'exemples d'abord.

## Comment obtenir la valeur ASCII d'un espace (  )

Un espace est également considéré comme un caractère valide. Dans le code, normalement nous utilisons un espace pour le représenter, comme `char ch = ' '`. Donc, si j'utilise l'espace dans le code ci-dessus – mais cette fois-ci j'utilise l'espace au lieu de la lettre de l'alphabet – alors le code serait comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-184845.png)

À la ligne 4, nous avons assigné un espace à la variable caractère nommée `char`. Maintenant, si j'exécute le code, alors j'obtiendrais la valeur ASCII d'un espace, qui est 32.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-185014.png)

Maintenant, si vous pouvez comprendre comment cela fonctionne, alors laissez-moi vous donner une simple tâche. Dans tout le code, nous avons assigné des données de caractères manuellement et nous avons vérifié la valeur ASCII en imprimant la valeur dans la sortie.

Dans ce processus, si nous voulons obtenir la valeur ASCII de divers caractères, alors nous devons changer le code manuellement chaque fois. Mais cela pourrait être une corvée si nous voulons quelque chose comme une calculatrice ASCII, où l'utilisateur fournirait le caractère comme entrée et le code fournirait la valeur ASCII exacte comme sortie dans le terminal. 

Pensez-vous pouvoir créer cela maintenant par vous-même ? Ne faites pas défiler vers le bas jusqu'à ce que vous ayez essayé d'écrire le code au moins une fois !

Très bien, j'espère que vous avez essayé de faire la calculatrice en modifiant un peu le code. Si vous avez du mal à le faire, alors ne vous inquiétez pas car je vous ai couvert.

## Comment créer une calculatrice ASCII

Auparavant, nous avons assigné chaque caractère manuellement dans notre code. Comme nous voulons que l'utilisateur fournisse le caractère lui-même, nous allons modifier un peu le code. 

Cette fois-ci, nous n'assignerons pas de valeurs de caractères dans les variables de caractères. Nous déclarerons d'abord une variable de caractère afin de pouvoir assigner le caractère à la variable plus tard. Ensuite, nous demanderons à l'utilisateur de fournir un caractère dans le terminal. 

Après avoir obtenu l'entrée de l'utilisateur, nous assignerons la valeur à notre variable de caractère. Ensuite, nous imprimerons simplement la valeur ASCII du caractère dans le terminal. C'est aussi simple que cela !

Suivez simplement le code ci-dessous, et je vous expliquerai toutes les étapes à nouveau ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-185809.png)
_Notre calculatrice ASCII utilisant le langage de programmation C_

Permettez-moi d'expliquer ce que j'ai fait dans le code d'abord. Ensuite, je vous montrerai le résultat en exécutant le programme. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-190838.png)

Comme vous pouvez le voir, j'ai inclus le fichier d'en-tête standard de base et nécessaire à la ligne 1. `stdio` représente le format d'entrée et de sortie standard. 

En fait, `stdio.h` est un fichier d'en-tête qui contient les informations nécessaires pour inclure les fonctions liées à l'entrée/sortie dans notre programme. Comme nous travaillerons définitivement sur l'entrée et la sortie, c'est un fichier d'en-tête nécessaire dans notre programme C. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-203815.png)

À la ligne 2, j'ai ajouté la fonction principale. Un main est un mot-clé ou une fonction prédéfinie en C. L'exécution de tout programme C commence toujours par la fonction **main** – gardez cela à l'esprit. 

Nous devons fournir le type de retour de la fonction. J'ai utilisé `int` afin que la fonction principale puisse retourner n'importe quelle valeur entière. Mais comme vous pouvez le voir, je ne retourne en fait rien plus tard. Donc, je peux aussi utiliser `void` au lieu de `int` à la ligne 2. La sortie serait exactement la même. **Void** signifie qu'elle ne retourne rien.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-190920.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-190939.png)

À la ligne 3 et à la ligne 7, j'ai utilisé des accolades `{` `}`. Normalement, nous utilisons des accolades pour regrouper un ensemble d'instructions. Comme toutes les instructions (ou, vous pourriez dire, les lignes de code) de la ligne 4 à la ligne 6 sont incluses dans la fonction principale, j'ai utilisé ces accolades pour les représenter toutes comme un ensemble d'instructions, ou un bloc de code.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-191024.png)

À la ligne 4, j'ai déclaré une variable de caractère. Nous utilisons `char` pour représenter le type de données caractère. 

Après avoir déclaré le type de données, nous devons fournir le nom du caractère. J'ai utilisé `ch` comme nom de ma variable, mais vous pouvez utiliser n'importe quel nom que vous voulez sauf les [mots-clés C](https://www.javatpoint.com/keywords-in-c). Il y a [certaines conventions de nommage d'une variable dans le langage de programmation C](https://www.programiz.com/c-programming/c-variables-constants#:~:text=%3D%20%27l%27%3B-,Rules%20for%20naming%20a%20variable,name%20(identifier)%20can%20be.) que vous pouvez consulter également.

Les points-virgules ( `;` ) sont les instructions de fin dans le langage de programmation C. Nous utilisons `;` pour indiquer la fin d'une ligne de code.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-191426.png)

À la ligne 5, j'utilise la fonction `scanf`. Nous l'utilisons pour obtenir une entrée de l'utilisateur. Je prends une valeur de caractère de l'utilisateur comme entrée. Ici, `%c` fait référence au type de données caractère. 

Après avoir pris la valeur du caractère comme entrée de l'utilisateur, nous stockons la valeur dans notre variable de caractère, `ch`. (Si nous ne stockons pas les données, alors comment allons-nous faire des calculs dessus, n'est-ce pas ?).

 `&` est un opérateur d'adresse, et l'opérateur `&` est utilisé pour obtenir l'adresse de la variable. Comme nous utilisons `&ch`, cela indique que nous disons au compilateur C que nous donnons ou passons la valeur des données d'entrée dans la variable `ch`. Nous prononçons `&` comme **Ampersand.**

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-192257.png)

À la ligne 6, j'imprime la valeur ASCII du caractère (le caractère que nous avons pris comme entrée de l'utilisateur).

J'ai beaucoup parlé, n'est-ce pas ? 😅 Maintenant, il est temps de vous montrer le résultat de notre calculatrice ASCII très simple.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-104.png)

Ici, j'ai fourni `L` comme entrée pour obtenir la valeur ASCII de `L`. À la ligne suivante, le programme a fourni 76 comme sortie, et 76 est la valeur ASCII exacte de `L`.

Maintenant, vérifions quelque chose de différent. Je vais vérifier la valeur ASCII de `!` maintenant.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-192616.png)

Comme vous pouvez le voir, cela fonctionne sans faille ! Maintenant, rendons le code plus joli. 

Vous voyez, comme nous avons écrit tout le code, nous pouvons comprendre que nous devons d'abord donner une valeur de caractère comme entrée. Ensuite, le programme fournit la valeur ASCII.

Mais d'autres utilisateurs pourraient ne pas comprendre cela. Ils pourraient également être confus sur ce qu'ils doivent faire après avoir exécuté le code – comme, est-ce que le code fournira directement la valeur ASCII de n'importe quel caractère aléatoire ou autre chose ? Nous ne voulons pas rendre les autres confus avec notre projet simple mais plutôt pratique, n'est-ce pas ?

Donnons d'abord quelques instructions qui facilitent la compréhension des utilisateurs sur ce qu'ils doivent faire après avoir exécuté le code. Le code ressemblerait à ceci :

```c
#include <stdio.h>
void main()
{
    char ch;
    printf("Entrez un caractère : ");
    scanf("%c", &ch);
    printf("La valeur ASCII de %c est : %d\n", ch, ch);
}

```

Nous voulons tous une belle capture d'écran. Permettez-moi de vous en donner une :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/carbon-1.png)
_Notre calculatrice ASCII simple mais pratique_

Ne craignez rien ! Je vais expliquer toutes les parties modifiées maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-193306.png)

À la ligne 5, j'ai ajouté une instruction d'impression pour afficher la chaîne donnée chaque fois que l'utilisateur exécute le code. Je veux que les utilisateurs sachent qu'ils doivent simplement entrer un caractère dans le terminal après avoir exécuté le programme.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-193518.png)

À la ligne 7, j'ai modifié un peu la fonction d'impression. Je veux que le code génère une belle ligne tout en fournissant la valeur ASCII du caractère donné. Le `%c` indique que nous fournirons le caractère lui-même ici, et le `%d` indique d'imprimer la valeur entière comme précédemment. 

Maintenant, laissez-moi vous montrer le résultat en fournissant des caractères aléatoires comme entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-193703.png)
_La valeur ASCII pour `a`_

C'est beau, n'est-ce pas ? Au moins, plus joli que le code précédent, car les utilisateurs obtiendront tout ici – ce qu'ils devront faire, quelle valeur le programme fournit en sortie, etc., n'est-ce pas ?

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-26-193839.png)
_La valeur ASCII pour `^`_

J'ai également ajouté ce dernier code dans [mon gist public](https://gist.github.com/FahimFBA/e0c9c3697db9dd45301edb8cdde499db).

Notre calculatrice ASCII est prête ! Nous avons appris beaucoup, même si nous n'avons utilisé que du code simple. 

Si vous vous demandez si nous avons utilisé le langage de programmation C dans cet article, mais ne pouvons-nous pas le faire en utilisant d'autres langages de programmation ? La réponse est OUI ! Je pensais vous montrer la calculatrice ASCII exacte en utilisant d'autres langages, mais cela rendrait cet article beaucoup plus grand. Donc, je garde cette tâche et vous laisse la faire vous-même. 

Vous pouvez également personnaliser le code pour répondre à vos besoins, ajouter une belle interface graphique, etc. Explorez le monde merveilleux de la programmation :)

## Conclusion

J'espère que cet article vous aide à comprendre comment fonctionnent les programmes C de base.

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez entrer en contact avec moi, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/) et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers types de langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !