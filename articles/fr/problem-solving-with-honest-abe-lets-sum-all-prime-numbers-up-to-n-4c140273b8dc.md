---
title: 'Résolution de problèmes avec Honest Abe : additionnons tous les nombres premiers
  jusqu''à n'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-07T12:08:59.000Z'
originalURL: https://freecodecamp.org/news/problem-solving-with-honest-abe-lets-sum-all-prime-numbers-up-to-n-4c140273b8dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MZTE3Hr9MY3Ia_YUa9Sddg.jpeg
tags:
- name: creativity
  slug: creativity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Résolution de problèmes avec Honest Abe : additionnons tous les nombres
  premiers jusqu''à n'
seo_desc: 'By Daniel Weiner

  Follow along as Honest Abe solves an intermediate algorithm challenge using the
  basic software development principles


  _Back in the day, we called it math [link](http://www.publicdomainpictures.net/pictures/80000/nahled/abraham-linco...'
---

Par Daniel Weiner

#### Suivez Honest Abe alors qu'il résout un défi algorithmique intermédiaire en utilisant les principes de base du développement logiciel

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_À l'époque, nous appelions cela des maths [link](http://www.publicdomainpictures.net/pictures/80000/nahled/abraham-lincoln-clipart.jpg" rel="noopener" target="_blank" title=")_

Disons que le défi est le suivant :

Additionnez tous les nombres premiers jusqu'à et y compris le nombre fourni.

Un nombre premier est défini comme **un nombre supérieur à un et ayant seulement deux diviseurs, un et lui-même**. Par exemple, 2 est un nombre premier car il n'est divisible que par un et deux.

Le nombre fourni peut ne pas être un nombre premier.

Comment Honest Abe résoudrait-il ce problème ?

### Honest Abe pense en grand

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Prenez le temps de comprendre le problème [link](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/SDLC_-_Software_Development_Life_Cycle.jpg/764px-SDLC_-_Software_Development_Life_Cycle.jpg" rel="noopener" target="_blank" title=")_

> « Donnez-moi six heures pour abattre un arbre et je passerai les quatre premières à aiguiser la hache. » — Honest Abe

Avant de plonger dans le code, Honest Abe aime **formuler les exigences** et **déterminer les spécifications**. Il apprend autant que possible sur le problème et comprend exactement quel problème doit être résolu. Tant qu'il ne comprend pas pleinement le problème, il ne peut pas commencer à le résoudre.

Il doit également déterminer exactement ce que le programme accomplira. Il se concentre sur **ce que** le programme accomplira, plutôt que sur **comment** il fonctionnera. Pour des programmes simples, cela implique de décrire les entrées et les sorties et comment elles se rapportent les unes aux autres.

Pour ce problème, l'entrée sera un nombre (n), un entier. La sortie sera la somme de tous les nombres premiers de 2 à n (il n'y a pas de nombres premiers inférieurs à 2). Le problème explique les nombres premiers, et Abe se sent à l'aise avec cette définition.

### Honest Abe commence avec du papier et un crayon

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Un algorithme est une recette ? Peut-être [link](https://c2.staticflickr.com/4/3059/3073489187_bd76ae6747_z.jpg?zz=1" rel="noopener" target="_blank" title=")_

Abe ne se lance pas directement dans le codage. L'étape suivante consiste à créer la structure globale du programme. C'est là qu'il détermine **comment** le programme accomplit sa tâche.

Le travail principal ici est de **concevoir l'algorithme(s)** qui répondra aux spécifications. L'algorithme sera souvent écrit en **pseudocode**, ou une description précise en anglais de ce que fait le programme. Cela aide Abe à communiquer des algorithmes sans le surcoût mental supplémentaire de devoir tout faire correctement dans un langage de programmation particulier.

Voici un algorithme pour additionner tous les nombres premiers jusqu'à n :

* Entrer n comme un entier
* Trouver les nombres premiers jusqu'à n
* Trouver la somme de tous les nombres premiers trouvés

Abe sait qu'il peut revenir à ce pseudocode lors de la mise en œuvre de la conception.

### Honest Abe adore Python Tutor

![Image](https://cdn-media-1.freecodecamp.org/images/sh59wqAG42mQr3Pn7lW8qrRgHbRUYF65QuWu)
_Un artiste n'est aussi bon que ses outils [link](https://c1.staticflickr.com/4/3132/2504310138_f7d3e1aec3_b.jpg" rel="noopener" target="_blank" title=")_

Abe sait qu'il a de nombreuses options pour coder, y compris un éditeur tel que Sublime, ou un IDE tel que Visual Studio Code, ou même directement dans un panneau de codage fourni (comme celui fourni par freeCodeCamp).

Abe préfère vraiment pythontutor.com.

Voici un exemple de comment fonctionne Python Tutor :

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Codage en Python3 en utilisant Python Tutor_

Python Tutor est une interface très intuitive pour entrer du code dans un éditeur. Il permet à Abe de visualiser l'exécution d'un programme, sans avoir besoin d'apprendre à utiliser un débogueur ou un IDE. Il peut même définir des points d'arrêt simplement en cliquant sur des lignes de code (le point d'arrêt ici est marqué en rouge). Malgré son nom, Python Tutor est également compatible avec Java, JavaScript, Ruby et d'autres langages de programmation.

### Honest Abe utilise le développement incrémental

![Image](https://cdn-media-1.freecodecamp.org/images/HQwGLbkuoBxjAJnid24NeBJNW09lqyrrpTzp)
_Cela rend les choses plus claires [link](http://3vwizk2qtr8l3diwrm3r2ba0-wpengine.netdna-ssl.com/wp-content/uploads/2011/10/convergent-vs-divergent2.jpg" rel="noopener" target="_blank" title=")_

Contrairement à de nombreuses conférences, tutoriels et manuels, le code qu'Honest Abe écrit lui-même ne vient pas complètement assemblé en tant que programme fonctionnel. Bien que parfois il pense que ce serait bien si c'était le cas.

Par conséquent, Honest Abe pratique le développement incrémental.

Plutôt que d'écrire une fonction complète, un programme, ou ce sur quoi il travaille, Honest Abe écrira d'abord de petits morceaux de code, s'assurera qu'ils fonctionnent, puis les reliera ensemble dans un programme plus grand. Il développe donc son programme par **incréments**.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Développement incrémental pour obtenir un entier de l'utilisateur_

Dans cet exemple, Honest Abe commence avec une petite version du code, en obtenant une entrée de l'utilisateur. Il insère une instruction print pour s'assurer que cela fonctionne. La version finale du code est commentée ci-dessous pour montrer comment il pourrait passer d'un incrément à un bloc de code plus grand.

### Honest Abe pratique la programmation défensive

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Voilà de l'autodéfense [link](https://pixel.nymag.com/imgs/fashion/daily/2016/11/18/18-womens-self-defense.w710.h473.jpg" rel="noopener" target="_blank" title=")_

Honest Abe sait que les utilisateurs ne peuvent pas être fiables pour suivre les instructions fournies par son programme. Il doit mettre en place des protections au cas où les utilisateurs entrent de mauvaises valeurs. Dans ce cas, les mauvaises valeurs seraient autre chose qu'un entier positif.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Capture des mauvaises entrées utilisateur — flottants, caractères et entiers négatifs_

Le bloc try / except vu ci-dessus, encapsulé dans la fonction readInt, capture toute entrée utilisateur qui n'est pas un entier positif, et retourne finalement l'entrée utilisateur une fois qu'un entier est correctement saisi.

### Honest Abe commence avec une solution brute force

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_« Rendez-le correct, rendez-le clair, rendez-le concis, rendez-le rapide. Dans cet ordre. » Wes Dyer_

La première priorité d'Honest Abe est d'obtenir un résultat correct du programme. Il s'appuie sur une approche brute force, une énumération exhaustive, en itérant sur tous les nombres de cinq jusqu'à l'entrée utilisateur, en vérifiant si chacun est premier.

Il sait que deux et trois sont des nombres premiers, donc si l'un d'eux est l'entrée utilisateur, il les ajoute à la somme.

Il optimise également la boucle interne en ne recherchant que de deux jusqu'à la racine carrée de i.

Cela donne le résultat correct, mais Honest Abe sait qu'il peut faire mieux. Cela serait terriblement lent sur de grandes entrées.

### Honest Abe étudie les classiques

![Image](https://cdn-media-1.freecodecamp.org/images/Nj8BvK6MWqypP2T1Wq16-W8jOmNAusjLrt5s)
_Crible d'Ératosthène [link](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#/media/File:Sieve_of_Eratosthenes_animation.gif" rel="noopener" target="_blank" title=")_

Attribué au mathématicien grec ancien, Ératosthène, il s'agit d'un algorithme efficace pour trouver des nombres premiers jusqu'à une limite donnée.

Il marque itérativement les multiples de chaque nombre premier comme non premiers, en commençant par le premier nombre premier, 2. Par exemple, 4, 6, 8, etc. sont marqués comme non premiers jusqu'à la limite. Ensuite, en revenant au début de la liste, 3 est marqué comme premier. 6 a déjà été marqué comme non premier, donc 9 est marqué comme non premier, suivi de 12, 15, etc. jusqu'à ce que la séquence soit terminée.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Crible d'Ératosthène dans pythontutor_

Honest Abe commence par initialiser une liste avec les valeurs True de longueur num. Il définit les deux premières valeurs de la liste à False car ni 0 ni 1 ne sont premiers. Il crée ensuite une variable sum avec une valeur initiale de 0, qui augmentera avec chaque nombre premier trouvé.

En utilisant la fonction enumerate en Python, Honest Abe vérifie d'abord si la valeur dans la liste a est définie à True, ce qui signifie que c'est un nombre premier. Si c'est le cas, la somme augmente de ce montant.

Il itère ensuite, en commençant par i*i (une petite optimisation), jusqu'à num, en incrémentant par i, en changeant la valeur à chaque index de liste à False.

Par exemple, 0 et 1 sont tous deux définis à False, donc ces valeurs n'entrent pas dans la boucle interne for.

2 est défini à True, donc 2 est ajouté à la somme. Ensuite, en commençant à 4, les indices de liste sont définis à False, y compris 6, 8, 10, etc., jusqu'à ce que la boucle soit terminée.

Ensuite, i incrémente à 3, qui est défini à True, et le processus ci-dessus se répète.

Honest Abe sait qu'il existe des [implémentations plus efficaces](https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n), mais le compromis en efficacité sera l'explicabilité, donc il laissera au lecteur le soin d'explorer davantage ces algorithmes.

### Honest Abe teste son programme

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Passer de pythontutor pour les tests_

Normalement, Abe ferait des tests unitaires avant les tests d'intégration.

Cependant, les tests sont un sujet très vaste, mieux laissé pour d'autres articles.

Abe veut simplement s'assurer que son programme fonctionne comme prévu.

Il utilise pytest et teste son programme sur une série d'entiers positifs.

Il se sent confiant que son programme fournit les bonnes réponses.

### Les ressources préférées d'Honest Abe

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Apprentissage tout au long de la vie [link](http://maxpixel.freegreatpicture.com/static/photo/1x/Education-Learn-School-Classroom-Learning-1959551.jpg" rel="noopener" target="_blank" title=")_

[Apprenez-vous la programmation en dix ans](http://norvig.com/21-days.html) — Peter Norvig

[Méthodologie de programmation de Stanford](https://www.youtube.com/playlist?list=PL84A56BC7F4A1F852)

[Python du MIT](https://www.youtube.com/playlist?list=PL57FCE46F714A03BC)

[CS50 de Harvard](https://www.youtube.com/channel/UCcabW7890RKJzL968QWEykA)

Merci d'avoir lu ! Bonne chance dans votre parcours !

Profitez également de cette [bande dessinée](https://zenpencils.com/comic/asimov/) sur l'apprentissage tout au long de la vie.