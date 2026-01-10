---
title: Une brève histoire de la ligne de commande
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-21T09:55:28.000Z'
originalURL: https://freecodecamp.org/news/the-command-line-1fdbc692b3bf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uIU5dRHM7WFi1EFds5XD3Q.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une brève histoire de la ligne de commande
seo_desc: 'By Gitter

  This post by Andy Trevorah, Engineer at Gitter, has been adapted from a talk that
  he originally gave at codebar, a non-profit initiative that facilitates the growth
  of a diverse tech community by running regular programming workshops.

  This ...'
---

Par Gitter

_Cet article d'[Andy Trevorah](https://www.freecodecamp.org/news/the-command-line-1fdbc692b3bf/undefined), Ingénieur chez [Gitter](http://gitter.im), a été adapté d'une conférence qu'il a initialement donnée chez_ [codebar](http://codebar.io/)_, une initiative à but non lucratif qui favorise le développement d'une communauté technologique diverse en organisant des ateliers de programmation réguliers._

Cet article est divisé en deux parties : un peu d'histoire, suivi de quelques exemples pratiques de la ligne de commande.

#### Une brève histoire

Dans les années 1960 — 70, les ordinateurs devenaient plus que de simples calculatrices. Ils pouvaient sauvegarder des fichiers sur disque et exécuter plusieurs applications avec plusieurs utilisateurs. Mais ces choses étaient difficiles à contrôler et faciles à casser. Heureusement, une idée très intelligente a vu le jour : couvrir toutes ces parties internes avec une belle coque utilisable.

![Image](https://cdn-media-1.freecodecamp.org/images/8dQXHBemVAUp4xgVzFqgEHGyNjCsQT0usHBw)

Ces coques ont depuis évolué pour devenir le bureau Windows, Mac OS, et toutes les parties tactiles de votre téléphone. Basiquement, tout ce qui concerne l'interaction utilisateur. Elles rendent votre ordinateur facile à utiliser et (raisonnablement) difficile à casser.

Mais avant que ces coques ne deviennent jolies et graphiques, elles étaient simplement une ligne de commande. Vous tapiez quelque chose, et vous obteniez une réponse. Elles ressemblaient à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/z6KVS8d-ygTOk6nf25pzAas6NhWtxu01Iw8P)

Voici une coque exécutant la commande _cal_ et imprimant un calendrier.

Cette coque particulière s'appelle _bash_, ce qui est l'abréviation de ["Bourne Again SHell"](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29) car avant cela, il y avait le ["Bourne Shell"](https://en.wikipedia.org/wiki/Bourne_shell) de Stephen Bourne. Ne laissez jamais un ingénieur logiciel nommer quelque chose qui finira par durer.

Il y a une riche histoire des coques, et ces coques de style "[Unix](https://en.wikipedia.org/wiki/Unix)" ont commencé avec la [coque d'Unix System 1](https://en.wikipedia.org/wiki/History_of_Unix#1969) en 1969. Mais même celle-ci a été influencée par des programmes plus anciens tels que [RUNCOM](https://en.wikipedia.org/wiki/Run_commands). Si vous avez déjà remarqué que certains fichiers de configuration se terminent par "rc" (par exemple, ._vimrc_), c'est pourquoi.

Si ces coques ont changé depuis les années 1960, pourquoi les développeurs continuent-ils à les utiliser ?

![Image](https://cdn-media-1.freecodecamp.org/images/eKIIYJsqGQIaqkkd7NRrKfNpWN2AirtM6ius)

**_Parce qu_** elles n'ont pas vraiment changé depuis les années 60. Les interfaces graphiques de votre téléphone ou de votre ordinateur changent de manière fashionable avec chaque mise à jour (avec des améliorations d'utilisabilité), mais les coques de ligne de commande, non. Lorsque vous écrivez des scripts ou que vous gérez une ferme entière de serveurs, vous ne voulez vraiment pas que votre interface (utilisateur) change, car cela casserait vos scripts.

Heureusement, les coques de ligne de commande et les coques graphiques sont toutes deux des coques autour de la même chose, donc nous pouvons les utiliser de manière interchangeable. Voici quelques exemples pour montrer ce que les coques de ligne de commande peuvent faire.

#### Coques en action

Nous pouvons commencer petit et simplement faire répéter à l'ordinateur ce que nous disons :

```
bash-3.2$ echo hello  hello
```

L'ordinateur a également quelques mots spéciaux comme $RANDOM :

```
bash-3.2$ echo $RANDOM  23914
```

Gardez à l'esprit que presque toutes ces commandes sont simplement de petits programmes qui acceptent une entrée et émettent une sortie. Vous pouvez découvrir où ils se trouvent en utilisant _which_ :

```
bash-3.2$ which echo  /bin/echo
```

Avec Mac OS, nous pouvons même faire _dire_ des choses à l'ordinateur :

```
bash-3.2$ say hello  ["hello" provient des haut-parleurs]
```

```
bash-3.2$ say butts butts butts  ["butts butts butts" provient des haut-parleurs sans plainte]
```

Il y a aussi _cat_ qui imprimera le contenu des fichiers. Il date de 1971.

```
bash-3.2$ cat cool_websites.txt  Some websites that I like:
```

```
http://codebar.io  http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt
```

Nous pouvons l'utiliser pour lire certains fichiers intégrés sur votre ordinateur :

```
bash-3.2$ cat /usr/share/dict/words  [sauter quelques milliers de lignes]zymotically  zymotize  zymotoxic  zymurgy  Zyrenian  Zyrian  Zyryan  zythem  Zythia  zythum  Zyzomys  Zyzzogeton
```

Ce sont tous les mots que votre ordinateur connaît ! Cette liste est assez longue (presque trop longue pour faire défiler !), mais nous pouvons utiliser la commande _head_ pour voir le début :

```
bash-3.2$ head /usr/share/dict/words  A  a  aa  aal  aalii  aam  Aani  aardvark  aardwolf  Aaron
```

Et il y a une commande opposée, _tail_ :

```
bash-3.2$ tail /usr/share/dict/words  zymotoxic  zymurgy  Zyrenian  Zyrian  Zyryan  zythem  Zythia  zythum  Zyzomys  Zyzzogeton
```

Ce serait bien de simplement obtenir le dernier mot. _tail_ peut le faire, mais nécessite un argument spécial. Nous pouvons le chercher en utilisant _man_ :

```
bash-3.2$ man tail
```

```
TAIL(1)                   BSD General Commands Manual
```

```
NAME       tail -- display the last part of a file
```

```
SYNOPSIS       tail [-F | -f | -r] [-q] [-b number | -c number | -n number] [file ...]
```

```
DESCRIPTION       The tail utility displays the contents of file or, by default, its stan-     dard input, to the standard output.
```

```
     The display begins at a byte, line or 512-byte block location in the     input.  Numbers having a leading plus (`+') sign are relative to the     beginning of the input, for example, ``-c +2'' starts the display at the     second byte of the input.  Numbers having a leading minus (`-') sign or     no explicit sign are relative to the end of the input, for example, ``-n     2'' displays the last two lines of the input.  The default starting loca-     tion is ``-n 10'', or the last 10 lines of the input.
```

```
     The options are as follows:
```

```
:
```

Ah ! L'argument est _-n_ (vous appuyez sur "q" pour quitter le manuel au fait) :

```
bash-3.2$ tail -n 1 /usr/share/dict/words  Zyzzogeton
```

Je n'ai aucune idée de la façon de prononcer "Zyzzogeton", mais nous pouvons faire en sorte que l'ordinateur le fasse en utilisant la commande say. Nous redirigeons simplement la sortie de _tail_ vers l'entrée de _say_ en utilisant le caractère pipe (|) :

```
bash-3.2$ tail -n 1 /usr/share/dict/words | say  ["Zyzzogeton" provient des haut-parleurs]
```

Génial ! Nous pouvons même avoir plusieurs pipes. Nous pouvons rediriger _cat_ vers _tail_ vers _say_ et obtenir le même résultat :

```
bash-3.2$ cat /usr/share/dict/words | tail -n 1 | say  ["Zyzzogeton" provient des haut-parleurs]
```

Maintenant, si nous voulions obtenir un mot aléatoire, nous pourrions obtenir tous les mots jusqu'à un point aléatoire, puis obtenir le dernier mot de celui-ci. Nous pouvons faire cela avec _head_ et _tail_ :

```
bash-3.2$ cat /usr/share/dict/words | head -n $RANDOM | tail -n 1 | say  ["atmological" provient des haut-parleurs]
```

_cat_ lit les fichiers depuis votre disque dur, mais nous pouvons utiliser _curl_ pour lire des fichiers depuis Internet. Voici une URL pour un fichier qui contient les œuvres complètes de Shakespeare :

```
bash-3.2$ curl -s http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt  [sauter quelques milliers de lignes]  Would yet again betray the fore-betrayed,  And new pervert a reconciled maid.'
```

```
THE END
```

```
<<THIS ELECTRONIC VERSION OF THE COMPLETE WORKS OF WILLIAM  SHAKESPEARE IS COPYRIGHT 1990-1993 BY WORLD LIBRARY, INC., AND IS  PROVIDED BY PROJECT GUTENBERG ETEXT OF ILLINOIS BENEDICTINE COLLEGE  WITH PERMISSION.  ELECTRONIC AND MACHINE READABLE COPIES MAY BE  DISTRIBUTED SO LONG AS SUCH COPIES (1) ARE FOR YOUR OR OTHERS  PERSONAL USE ONLY, AND (2) ARE NOT DISTRIBUTED OR USED  COMMERCIALLY.  PROHIBITED COMMERCIAL DISTRIBUTION INCLUDES BY ANY  SERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP.>>
```

```
End of this Etext of The Complete Works of William Shakespeare
```

Si nous utilisons ce _curl_ comme entrée pour nos pipes de mots aléatoires, nous pouvons faire en sorte que l'ordinateur nous cite des lignes aléatoires de Shakespeare !

```
bash-3.2$ curl -s http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt | head -n $RANDOM | tail -n 1 | say  ["The sister to my wife, this gentlewoman" provient des haut-parleurs]
```

Nous pouvons accomplir beaucoup avec seulement quelques commandes. Cette philosophie d'avoir de petits programmes réutilisables qui peuvent être combinés ensemble a duré depuis longtemps, un peu comme des briques Lego. En combinant les bons, vous pouvez créer un programme assez impressionnant !