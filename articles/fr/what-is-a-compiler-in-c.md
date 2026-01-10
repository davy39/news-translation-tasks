---
title: Qu'est-ce qu'un compilateur ? Les compilateurs en C expliqués aux débutants
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2022-03-14T18:39:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-compiler-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/1-YhjIVZXE56R6YZaTF-Lzig.jpeg
tags:
- name: beginners guide
  slug: beginners-guide
- name: c programming
  slug: c-programming
- name: compilers
  slug: compilers
seo_title: Qu'est-ce qu'un compilateur ? Les compilateurs en C expliqués aux débutants
seo_desc: 'Did you know that it is thanks to compilers that software exists?

  Exactly – compilers are very important, and some form of a compiler exists in all
  programming languages.

  But, what is a compiler? What do they do exactly?

  This article will teach you:

  ...'
---

Saviez-vous que c'est grâce aux compilateurs que les logiciels existent ?

Exactement – les compilateurs sont très importants, et une forme de compilateur existe dans tous les langages de programmation.

Mais, qu'est-ce qu'un compilateur ? Que font-ils exactement ?

Cet article vous enseignera :

1. Ce qu'est un compilateur à l'aide d'une analogie.
    
2. L'histoire de base des compilateurs C.
    

Ne vous inquiétez pas, vous n'avez pas besoin d'expérience en programmation pour comprendre ce qu'est un compilateur.

Il vous suffit d'abord de comprendre le concept, puis, si vous le souhaitez, vous pourrez passer à la définition technique.

## 1\. Qu'est-ce qu'un compilateur ? Une analogie

![Image d'un téléphone](https://miro.medium.com/max/1400/1*xFzl6UbF6XI6V0_Tnx-PYg.jpeg align="left")

*Photo par* [***Tyler Lastovich***](https://www.pexels.com/@lastly?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) ***sur*** [***Pexels***](https://www.pexels.com/photo/black-iphone-7-on-brown-table-699122/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

**Imaginez que vous apprenez une langue (anglais, espagnol ou portugais) et que vous voulez connaître la signification d'un mot ou d'une phrase.**

**Pour ce faire, vous allez utiliser Google Traduction.**

**La première étape consiste à savoir ce que vous allez taper dans Google Traduction et à vérifier si c'est correctement écrit.**

**La deuxième étape consiste à choisir la langue vers laquelle vous voulez convertir. Pour beaucoup de lecteurs, ce sera le français.**

**La troisième et dernière étape consiste simplement à savoir ce que signifie cette phrase en français.**

**Essentiellement, vous venez de taper dans Google Traduction une phrase ou un mot que vous ne compreniez pas. Google Traduction a traduit cette phrase en français.**

***Exemple : nadar (portugais) –> nager (français)***

**La même chose se produit en programmation.**

**Dans ce cas, nous utilisons le langage C.**

**La première étape que vous devez franchir est de savoir ce que vous allez taper dans le fichier .c et si cela est correctement écrit.**

**Dans cet exemple, le fichier s'appelle main.c\_.\_**

```c
#include <stdio.h>

int main()
{
	printf("Hello World");
    
    return 0;
}
```

***Première étape : Ce code affichera « Hello world »\*\****

**La deuxième étape consiste à le compiler. Il sera compilé selon le compilateur que vous possédez.**

```bash
gcc -o main main.c -Wall
```

***Deuxième étape : Commande pour compiler du code C\*\****

**La troisième et dernière étape consiste simplement à connaître la sortie du programme – pour s'assurer qu'il fonctionne comme nous le souhaitons.**

**Note rapide : si vous voulez savoir ce que signifie chaque mot dans le terminal de commande, veuillez consulter la section « En savoir plus... » de cet article !**

***Troisième étape : Hello world !\*\****

**Vous pouvez voir dans l'image ci-dessous une explication visuelle du processus de compilation :**

***Comparaison de la compilation d'un fichier C avec la traduction de mots***

## **Comment fonctionnent les compilateurs C**

***Photo par*** [***JÉSHOOTS\*\****](https://www.pexels.com/@jeshoots?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) ***sur*** [***Pexels\*\****](https://www.pexels.com/photo/person-holding-sony-ps4-dualshock-4-21067/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

**Au fil des ans, la technologie a évolué à un rythme incroyable. Il en va de même pour les compilateurs.**

**Le compilateur C a, au fil du temps, évolué vers de nombreuses versions.**

**Tout comme la PlayStation – il y a la PlayStation 2, la PlayStation 3, la PlayStation 4, et ainsi de suite.**

**Il en va de même pour les compilateurs C. Une fois qu'il a été *standardisé*, de nombreuses versions ont été créées :**

* **C89/90, une version du C autrefois *standardisée*,**
    
* **Le C99 a remplacé le C89 et le C90 en 1999.**
    
* **Le C11 a remplacé le C99 en 2011.**
    
* **Le C17 a remplacé le C11 en 2018.**
    
* **Le C2X remplacera le C17 en 2023.**
    

**Tout comme avec une PlayStation, chaque nouvelle version apporte de nouvelles fonctionnalités.**

**Certaines personnes préfèrent simplement jouer sur leur PlayStation 2.**

**C'est la même chose pour les programmeurs. Pour diverses raisons, les programmeurs peuvent préférer écrire et déboguer du code C avec le C99 ou le C11.**

## **En savoir plus sur les compilateurs**

**Que signifie exactement *« gcc -o main main.c -Wall »*, que nous avons vu dans le code ci-dessus ? Analysons-le morceau par morceau.**

`gcc` est la commande qui invoque le processus de compilation (prétraitement, compilation, assemblage et édition de liens).

`-o main` indique que le nom du fichier exécutable créé par la compilation de "main.c" sera appelé "main".

`main.c` est le nom du fichier à compiler.

**L'option** `-Wall` active les avertissements du compilateur. Les avertissements du compilateur vous informent que quelque chose dans votre code n'est pas tout à fait correct.

**C'est similaire à Grammarly. Si Grammarly suggère de changer une phrase, vous devriez dans la plupart des cas la changer pour la rendre plus claire et plus correcte.**

**Sinon, si vous essayez de changer quelque chose dans une phrase qui est déjà correcte, elle peut devenir illisible.**

**De la même manière, si vous ignorez les avertissements dans le code, cela peut finalement causer des bugs majeurs et votre projet pourrait même échouer.**

### **Que signifie « Standardisé » ?**

**Vous vous demandez peut-être ce que signifie « *standardisé* » que nous avons vu plus haut ?**

***Photo par*** [***Pixabay\*\****](https://www.pexels.com/@pixabay?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) ***sur*** [***Pexels\*\****](https://www.pexels.com/photo/architecture-building-construction-daylight-534220/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

**Regardons cela à travers une autre analogie. Il existe de nombreuses façons de construire une maison. Mais il y a une certaine manière qui est généralement à la fois la plus efficace et la plus sûre.**

**Pour cette raison, les personnes et les organisations doivent convenir qu'il existe une manière standard de construire une maison.**

**Le processus de création de cette norme s'appelle la normalisation (ou standardisation).**

**Lorsqu'un ensemble de règles devient une norme, cet ensemble de règles devient standardisé\_.\_**

**Cet ensemble de règles peut être une loi, un certificat ou simplement une convention de base utilisée par les travailleurs dans un certain domaine.**

**Il en va de même pour les compilateurs C.**

**C'est la normalisation qui aide les gens à s'accorder sur la manière dont les choses doivent être faites, qu'il s'agisse de compilateurs C, de composants automobiles ou de n'importe quoi d'autre.**

**La normalisation peut également aider les gens à s'accorder sur la version du C à utiliser. Les compilateurs C en sont un exemple.**

**Le compilateur C a longtemps été considéré comme un composant fondamental du développement logiciel.**

**Grâce à la norme du compilateur C, les développeurs peuvent compiler et exécuter le code d'autres personnes sans craindre que leurs compilateurs ne fonctionnent pas.**

**Afin de créer un bloc de construction aussi important pour l'industrie, il doit y avoir une organisation responsable de l'établissement des normes.**

**De nombreuses organisations créent et gèrent des normes. Dans le cas des compilateurs C, l'ISO (Organisation internationale de normalisation) gère les normes.**

**Tant que l'ISO gérera les futures normes des compilateurs C, les programmeurs et les entreprises pourront développer des logiciels fiables.**

## **Conclusion**

**Merci de votre lecture ! Maintenant, vous comprenez :**

* **Ce qu'est un compilateur**
    
* **L'histoire de base des compilateurs C**
    
* **Ce que signifie la normalisation**
    

[**Voici le dépôt GitHub**](https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code/tree/main/What%20exactly%20is%20a%20compiler%3F) **avec le code et les fichiers images que j'ai créés.**