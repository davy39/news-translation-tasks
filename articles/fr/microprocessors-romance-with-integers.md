---
title: La romance du microprocesseur avec les entiers négatifs – Le comment et pourquoi
  de la conception de l'arithmétique CPU
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-28T18:30:45.000Z'
originalURL: https://freecodecamp.org/news/microprocessors-romance-with-integers
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/cover2.jpg
tags:
- name: binary
  slug: binary
- name: cpu
  slug: cpu
- name: Mathematics
  slug: mathematics
- name: systems
  slug: systems
seo_title: La romance du microprocesseur avec les entiers négatifs – Le comment et
  pourquoi de la conception de l'arithmétique CPU
seo_desc: "By Vivek Agrawal\nOne of the first things we learn about computers is that\
  \ they only understand 0s and 1s, or bits. \nWe humans, on the other hand, communicate\
  \ numbers via the decimal system. This system uses digits from 0 to 9 along with\
  \ plus and minu..."
---

Par Vivek Agrawal

Une des premières choses que nous apprenons sur les ordinateurs est qu'ils ne comprennent que les **0 et 1**, ou **bits**.

Nous, les humains, communiquons les nombres via le système décimal. Ce système utilise des chiffres de 0 à 9 ainsi que des signes plus et moins (+ et -) pour désigner les nombres positifs ou négatifs.

Puisque les ordinateurs ne peuvent utiliser que deux chiffres – 0 et 1 – les ingénieurs et les mathématiciens de l'époque ont conçu des techniques ingénieuses pour représenter les nombres négatifs et pour faire de l'arithmétique avec eux. Explorons la beauté de ces techniques.

## D'abord, un peu de contexte sur le fonctionnement des ordinateurs

Les logiciels, images, textes, vidéos, nombres et tout ce qui se trouve entre eux sont des 0 et des 1 au niveau le plus bas de notre ordinateur.

Pour les images, textes, vidéos et nombres, nous avons des schémas de codage qui décident comment ces éléments seront convertis en 0 et 1. Par exemple, ASCII et Unicode pour le texte.

Les programmes logiciels que nous codons sont convertis en 0 et 1 via des compilateurs et des assembleurs. Cet ensemble de 0 et de 1, connu sous le nom de code machine (ou instruction machine), est d'abord stocké dans la mémoire principale de notre ordinateur (RAM) avant que le processeur ne puisse les exécuter.

![Un diagramme montrant le cycle de récupération, décodage et exécution](https://www.freecodecamp.org/news/content/images/2021/01/fetch-decode-exec.png)
_Le cycle de récupération, décodage et exécution architecturé par Sir [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann). Chaque ordinateur numérique suit ce cycle pour exécuter le code machine._

Le processeur commence le cycle d'exécution en **récupérant** les instructions de la mémoire principale, puis l'unité de contrôle du processeur **décode** ces instructions en deux parties – le code d'opération (opcode) et les opérandes.

L'opcode décide de l'action ultérieure à effectuer, comme ADD (addition), JMP (saut), INC (incrément) et ainsi de suite. Les opérandes sont les valeurs (ou emplacements mémoire) sur lesquelles cette opération sera effectuée.

Les instructions décodées sont envoyées à l'Unité Arithmétique et Logique (ALU) pour **exécution**. Dans l'ALU, l'instruction est exécutée en fonction de l'opcode sur les opérandes et le résultat est stocké dans la mémoire.

Par exemple, le code assembleur `ADD eax, 42` est d'abord transformé en code machine (0 et 1) par l'assembleur. Ensuite, il est stocké dans la mémoire principale avant que le cycle de récupération-décodage-exécution ne puisse commencer.

Lorsque la récupération du code machine pour `ADD eax, 42` de la mémoire est terminée, l'instruction est décodée. Le résultat décodé indique que l'opcode est `ADD` et les opérandes sont `eax` et `42`.

`eax` est un registre – un emplacement mémoire intégré dans le processeur qui peut être accessible instantanément par le processeur. Le registre `eax` est appelé un accumulateur dans la plupart des processeurs.

Le code assembleur `ADD eax, 42` est conçu pour ajouter 42 à la valeur actuelle du registre `eax` (accumulateur) et stocke cette somme dans `eax`. C'est `eax = eax + 42`.

Supposons que actuellement `eax` est 20. Cela signifie que la valeur de `eax` après l'exécution de `ADD eax, 42` sera 20 + 42 = 62.

![Deux hommes opérant l'ordinateur EDVAC](https://www.freecodecamp.org/news/content/images/2021/01/Edvac-1.jpg)
_EDVAC était l'un des premiers ordinateurs électroniques binaires construits pour le Ballistics Research Laboratory de l'armée américaine. ([Source de l'image](https://en.wikipedia.org/wiki/EDVAC#/media/File:Edvac.jpg), Domaine Public)._

La conception des premiers ordinateurs comme EDVAC a commencé avec le désir de rendre les calculs mathématiques fastidieux plus faciles et plus rapides.

Toute la responsabilité de faire calculer les ordinateurs reposait sur les épaules des additionneurs – des circuits qui additionnent deux nombres. Cela est dû au fait que des opérations sophistiquées comme la soustraction, la multiplication et la division utilisent des additionneurs dans leurs circuits.

En fin de compte, les ordinateurs ne sont que des machines arithmétiques rapides avec des capacités logiques. Comprendre les défis et la beauté de la conception de l'arithmétique binaire (des entiers positifs et surtout négatifs) est **l'un des concepts les plus fondamentaux dans un processeur d'ordinateur**.

Commençons d'abord par voir comment les nombres décimaux sont représentés en binaire et comment additionner deux valeurs binaires. Ensuite, nous commencerons à explorer la beauté.

## Comment fonctionne le système binaire

Si je vous dis de lire `872500`, vous direz probablement **872,5K**. Voyons comment notre esprit fait cela.

![La procédure que nous, les humains, utilisons pour lire les nombres décimaux](https://www.freecodecamp.org/news/content/images/2021/01/decimal_sys_img-2.png)

Nous attribuons la place des unités au premier chiffre de droite, puis la place des dizaines au deuxième de droite, les centièmes au troisième, et ainsi de suite, en augmentant chaque fois par puissance de 10.

Ces puissances de 10 dans chaque place sont les poids des places. Le poids de la place des centaines est cent. Nous multiplions les chiffres dans chaque place par le poids de leur place et les additionnons tous pour obtenir un nombre complet.

Dans le diagramme ci-dessus, vous pouvez voir que la croissance du poids de chaque place est en puissances de 10, commençant par `10^0` et allant jusqu'à `10^5`. C'est pourquoi les décimaux sont appelés un système de base dix.

![La procédure par laquelle les ordinateurs lisent les codes binaires](https://www.freecodecamp.org/news/content/images/2021/01/binary_sys_img-2.png)

En binaire, le poids de chaque place augmente par une puissance de 2. Cela signifie que le poids de la place commence par `2^0` et se termine par `2^quelque chose`. C'est la seule différence.

`00110101` en décimal se traduit par 53. Les ordinateurs interprètent le binaire de la même manière que nous, les humains, interprétons les décimaux, c'est-à-dire en multipliant le chiffre de chaque place par son poids et en les additionnant.

### Comment additionner des 1 et des 0

L'addition fonctionne en binaire presque de la même manière qu'en décimal. Voyons cela à travers un exemple. Nous allons additionner deux nombres binaires : `1101` (13) et `1100` (12).

![Étape un de l'addition de 1101 et 1100 qui est un plus zéro](https://www.freecodecamp.org/news/content/images/2021/01/1-1.png)

Comme nous le faisons dans le système décimal, nous commençons par la place des unités (`2^0`). Ajouter 1 et 0 nous donne 1. Donc nous mettons un 1 là. Restez avec moi et vous obtiendrez l'image complète.

![Étape deux de l'addition de 1101 et 1100 qui est zéro plus zéro](https://www.freecodecamp.org/news/content/images/2021/01/2-1.png)

0 plus 0 est 0. Continuons.

![Étape trois de l'addition de 1101 et 1100 qui est un plus un](https://www.freecodecamp.org/news/content/images/2021/01/3-2.png)

1 plus 1 est 2. Et 2 en binaire est représenté comme `10`. Nous reportons 1 à la place suivante et gardons 0 comme résultat de la place actuelle où nous sommes. N'est-ce pas la même chose que de dépasser 9 dans une place en addition décimale ?

![Étape quatre de l'addition de 1101 et 1100 qui est un plus un plus un de la ligne de report](https://www.freecodecamp.org/news/content/images/2021/01/4-1.png)

Nous avons deux 1 là et un 1 qui a été reporté de la place précédente, donc il y a un total de trois 1. Leur somme sera 3, et en binaire 3 est `11` donc nous écrivons `11`. Le résultat final est `11001` ou 25 en forme décimale, ce qui est effectivement 13 + 12.

Le calcul ci-dessus suppose que nous avons cinq bits disponibles pour stocker le résultat. Si un ordinateur 4 bits fait cette addition, alors il n'aura que quatre bits disponibles pour stocker le résultat.

Ce cinquième bit sera appelé un **débordement** dans les ordinateurs 4 bits. En arithmétique entière, le bit de débordement est ignoré ou rejeté. Donc nous aurions obtenu `1001` (9) comme résultat si nous avions utilisé un ordinateur 4 bits.

## La beauté de la conception de l'arithmétique binaire

Deux termes importants que nous devons comprendre avant de continuer sont **le bit le moins significatif** et **le bit le plus significatif**.

![Le bit le moins significatif et le bit le plus significatif dans un mot d'un octet](https://www.freecodecamp.org/news/content/images/2021/01/lsb_msb-1.png)

Le bit le plus à **droite est le bit le moins significatif** car il a le plus petit poids de place (`2^0`). Et le bit le plus à **gauche est le bit le plus significatif** car il a le plus grand poids de place (`2^7`).

Si le monde n'avait que des nombres positifs, alors ce serait la fin de cet article (car nous avons déjà appris comment représenter les décimaux en binaire et comment les additionner en binaire).

Heureusement, nous avons aussi des nombres négatifs.

La beauté de la conception arithmétique du CPU réside dans la négativité.

Alors, comment les ordinateurs représentent-ils les nombres négatifs, et comment fonctionne l'arithmétique sur les nombres négatifs ? Voyons une approche de codage pour ce problème.

Veuillez noter que dans les sections suivantes, nous travaillerons avec un ordinateur 4 bits pour comprendre les concepts, ce qui signifie que le cinquième bit sera traité comme un débordement. Les mêmes principes s'appliquent à toutes les architectures de CPU comme 16 bits, 32 bits ou 64 bits pour faire de l'arithmétique.

### L'approche de codage par signe et magnitude

![Le bit le plus à gauche dans un binaire à quatre bits est le bit de signe et les trois restants représentent la magnitude](https://www.freecodecamp.org/news/content/images/2021/01/sign-bit01-1.png)

`1101` en forme décimale serait -5 dans ce schéma de codage. Le bit le plus à gauche ou le bit le plus significatif est le bit de signe. Il indique au processeur le signe du nombre – c'est-à-dire si le nombre est positif ou négatif.

`0` dans le bit de signe représente une valeur positive et `1` représente une valeur négative. Les bits restants nous indiquent la magnitude réelle.

Dans `1101`, le bit de signe est `1`, donc le nombre est négatif. `101` est égal à 5 en décimal. Donc `1101` sera calculé comme -5 en décimal.

![Tous les nombres possibles avec quatre bits en utilisant le schéma de codage par bit de signe](https://www.freecodecamp.org/news/content/images/2021/01/4bit-1.png)
_Tous les nombres possibles qui peuvent être représentés par quatre bits avec le schéma de codage par bit de signe_

Dans le diagramme ci-dessus, vous pouvez voir tous les entiers qui peuvent être représentés par quatre bits en utilisant cette approche de codage. Tout semble bon jusqu'à ce point.

Mais si nous regardons de près, nous pouvons voir un problème de conception très sérieux dans ce schéma de codage. Affrontons ce problème.

Ajoutons un nombre positif et un nombre négatif. Par exemple, nous ajouterons +4 et -1. Notre réponse devrait être `(+4) + (-1) = (+3)` c'est-à-dire `0011`.

![Addition de +4 et -1 en binaire résultant en -5 lors de l'utilisation du schéma de codage par bit de signe](https://www.freecodecamp.org/news/content/images/2021/01/signbitproblem.png)

Voyez, le résultat est `1101` (-5). La réponse réelle devrait être `0011` (+3). Si nous devions implémenter cette approche sur un processeur, nous devrions ajouter une logique pour traiter ce problème, et les ingénieurs détestent la complexité supplémentaire dans leur logique.

À mesure que nous ajoutons plus de circuits, la consommation d'énergie augmente et les performances en souffrent.

Cela peut sembler un problème trivial pour les ordinateurs modernes à base de transistors.

Mais pensez aux premiers ordinateurs comme EDVAC qui fonctionnait sur des milliers de tubes à vide consommant des kilowatts de puissance, exploités par des centaines de personnes par jour. Et le gouvernement a dépensé des millions pour les construire.

À cette époque, ajouter des circuits et des tubes à vide supplémentaires signifiait des milliers de dollars et de sérieux problèmes de maintenance.

Donc les ingénieurs devaient penser à une conception de codage plus intelligente.

Maintenant, le moment est venu de révéler la beauté qui va résoudre ce problème et rendre notre système plus simple, plus performant et moins gourmand en énergie.

### Un beau système de codage entre en jeu et le CPU brille ❤️

Dans ce schéma de codage, comme dans le précédent, le bit le plus à gauche agit comme un bit de signe – mais avec un peu d'art pour représenter les nombres négatifs.

Les nombres positifs sont représentés de la même manière que dans le schéma de codage précédent : un `0` de tête suivi des bits restants pour la magnitude. Par exemple, dans ce schéma de codage aussi, 6 sera représenté comme `0110`.

Pour représenter un nombre négatif, un processus mathématique en deux étapes est exécuté sur son homologue positif. Cela signifie que pour représenter -6, nous effectuerons un processus mathématique en deux étapes sur +6 pour obtenir -6 en binaire.

Voyons comment -6 sera codé en binaire :

![Une illustration des bits qui s'inversent](https://www.freecodecamp.org/news/content/images/2021/01/invert-1.png)

Dans l'approche précédente de la magnitude du signe, pour calculer le négatif de +6, nous aurions simplement changé le bit de signe de `0` à `1`. `0110` (+6) deviendrait `1110` (-6).

Dans ce nouveau schéma de codage, nous inversons d'abord les bits. En changeant les zéros en uns et les uns en zéros. `0110` (+6) devient `1001`. L'inversion des bits est appelée "complément à un", donc ici nous avons calculé le complément à un de `0110` résultant en `1001`. Ensuite...

![Ajout d'un binaire à 1001, résultant en 1001](https://www.freecodecamp.org/news/content/images/2021/01/-6-1.png)

Nous ajoutons `0001` (+1) au complément à un que nous avons obtenu de l'étape un (`1001`). Le résultat **`1010` sera la représentation binaire de -6. Ce schéma de codage est appelé complément à deux.** Donc gardez à l'esprit que le calcul du complément à deux d'un entier positif nous donne son homologue négatif.

![Étapes de calcul du complément à deux de 0110](https://www.freecodecamp.org/news/content/images/2021/01/twocomplementshort-4.png)

L'inversion des bits nous donne le complément à un. L'ajout de un au complément à un nous donne le complément à deux des bits originaux avec lesquels nous avons commencé. Simple, n'est-ce pas ?

![Tous les nombres possibles qui peuvent être représentés par quatre bits avec le schéma de codage du complément à deux](https://www.freecodecamp.org/news/content/images/2021/01/2complement.png)
_Tous les nombres possibles qui peuvent être représentés par quatre bits avec le schéma de codage du complément à deux_

Maintenant, voyons pourquoi ce schéma de codage est si beau. Nous allons ajouter `0100` (+4) et `1111` (-1).

![Addition de 0100 et 1111 lors de l'utilisation du schéma de codage du complément à deux](https://www.freecodecamp.org/news/content/images/2021/01/2complesolution.png)

Voyez, nous obtenons le résultat exact avec le schéma de codage du complément à deux. Maintenant, nous pouvons additionner des entiers sans nous soucier de leurs signes.

Nous avons appris comment un entier négatif peut être représenté en 0 et 1 via le codage du complément à deux. Maintenant, supposons que nous exécutons `ADD eax, -3` et que la valeur actuelle dans le registre eax est -1. Donc la valeur dans eax après l'exécution de `ADD eax, -3` sera -4 (qui est `1100` dans le codage du complément à deux).

Lorsque le système d'exploitation récupère `1100` de eax pour présenter le résultat à l'utilisateur, comment le système d'exploitation décode-t-il `1100` en décimal ? Ou supposons que nous, en tant que programmeurs, rencontrons `1100`, comment pouvons-nous déterminer quel nombre représente `1100` ?

Bien sûr, nous ne pouvons pas continuer à calculer le complément à deux de chaque entier positif pour voir quand nous atteignons `1100`. Ce serait trop lent.

Les programmeurs et le système d'exploitation utilisent une belle propriété du complément à deux pour décoder le binaire en décimal.

Lorsque nous calculons le complément à deux d'un nombre positif, nous obtenons son homologue négatif. Eh bien, **l'inverse est également vrai** – ce qui signifie que le calcul du complément à deux d'un nombre négatif nous donnera son homologue positif. Nous verrons le pourquoi de cela dans une minute.

D'abord, comprenons comment le système d'exploitation ou un programmeur décodera `1100` en décimal.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/2complementexample-1.png)

En récupérant `1100` du registre eax, le système d'exploitation voit `1` comme bit de signe qui signale que l'entier est négatif. Le complément à deux de `1100` est calculé, ce qui donne l'homologue positif de `1100` qui est `0100` (+4). Le système d'exploitation ajoute ensuite un signe négatif à l'homologue positif et retourne la réponse finale comme -4. Relisez ce paragraphe une fois de plus et vous obtiendrez une meilleure compréhension.

Ensuite, le CPU sourit et dit au revoir à la beauté pour aujourd'hui ;)

Le CPU est rentré chez lui pour rencontrer sa mère. Maintenant, nous avons beaucoup de temps pour discuter du fonctionnement interne de l'art du complément à deux.

## Pourquoi et comment fonctionne le codage du complément à deux ?

Si je vous dis de trouver le négatif d'un nombre, disons +42, quelle est la manière la plus simple de trouver le négatif de +42 ?

Arguablement, la manière la plus simple est de soustraire le nombre de 0, n'est-ce pas ? `0 - (+42) = -42`. Si nous répétons cela, nous revenons à la valeur positive, `0 - (-42) = +42`. C'est toute la mathématique sur laquelle le complément à deux est construit.

![Soustraction de 0101 de 10000 résultant en 1011](https://www.freecodecamp.org/news/content/images/2021/01/zerominusnum-1.png)

Nous faisons `10000` (0 en décimal puisque le 1 le plus à gauche est un débordement) moins `0101` (+5). Nous obtenons `1011` qui est -5 en décimal dans le codage du complément à deux. Ignorez comment la soustraction est faite. Ce n'est pas important. Comprendre l'intuition derrière le complément à deux est important.

`10000` peut s'écrire `1111 + 0001` (essayez d'additionner ces deux, vous obtiendrez `10000`). Donc en réalité, nous faisons :

```
        10000       -   0101
=>  (1111 + 0001)   -   0101

```

En réarrangeant l'équation ci-dessus, nous pouvons l'écrire comme :

```
    (1111 + 0001)  -  0101
=>  (1111 - 0101)  +  0001

Étape 1 : soustraire 0101 de 1111

        1 1 1 1
       -0 1 0 1
       ---------
        1 0 1 0
        
       voir, soustraire 0101 de 1111 est équivalent 
       à inverser les bits de 0101, car nous avons obtenu 1010 comme résultat. 

  
       
Étape 2 : ajouter 0001 au résultat ci-dessus  

        1 0 1 0  ---> résultat de l'étape 1
       +0 0 0 1
       ---------
        1 0 1 1      
       
       nous obtenons 1011 qui est -5 dans le codage du complément à deux.      

```

Avez-vous vu que le système du complément à deux fait fondamentalement 0 moins le nombre ? Inverser les bits et ajouter un est une manière rapide et intelligente de soustraire le nombre de 0.

C'est la raison pour laquelle nous obtenons le positif d'un nombre négatif et le négatif d'un nombre positif lorsque nous calculons son complément à deux – parce que nous soustrayons en réalité le nombre de 0 (`0 - nombre`).

Les ordinateurs des années 1900 n'avaient que la logique arithmétique d'addition car le schéma de codage du complément à deux est si beau que la soustraction peut être facilement effectuée.

Par exemple, pour soustraire 12 de 100, le CPU calcule le complément à deux de +12 qui produit -12, puis nous ajoutons -12 à 100, ce qui nous donne la sortie requise.

Pourquoi ne soustrayons-nous pas directement de 0 pour trouver le négatif d'un nombre ou vice versa en binaire ?

Parce que la soustraction est un processus lent et compliqué (grâce à l'emprunt), notre ordinateur aurait besoin d'un circuit de soustraction coûteux si nous allons dans cette voie. Imaginez soustraire de 0 chaque fois que nous voulons représenter un entier négatif. Ce serait un cauchemar pour nous et pour nos ordinateurs aussi !

Le codage du complément à deux est une solution plus performante, conduit à une conception de circuit simple et économise beaucoup d'argent. Cela est dû au fait que nous n'avons pas besoin d'un circuit coûteux pour la soustraction et qu'il n'y a pas de logique supplémentaire pour traiter l'arithmétique des entiers + et -. Juste une addition simple et nous pouvons faire les deux – additionner et soustraire.

Alors apprécions nos concepteurs d'ordinateurs pour ce beau schéma de codage – **le complément à deux ❤️.**

## Mots finaux

Je me suis promis que je ne facturerais jamais aucun matériel d'apprentissage que je produis. Tout ce que je fais pour l'éducation, qu'il s'agisse d'un simple article, d'un cours ou d'un ebook, sera toujours 100% gratuit et ouvert.

Je publie des ressources utiles et partage des pensées significatives sur [mon compte Twitter](https://twitter.com/vkwebdev). Vous pouvez me suivre là-bas et m'envoyer un DM si vous avez appris quelque chose de nouveau grâce à cet article. Cela fera ma journée :)

Chaque développeur, chaque auteur et chaque être humain apprend de quelqu'un. Je crois que les personnes et les ressources dont nous apprenons doivent être citées et diffusées. Cela encourage ces bonnes personnes à faire plus pour nous tous. Donc voici mes bonnes personnes.

[Animesh de mycodeschool](https://www.youtube.com/watch?v=zxb8DvLUqcM) m'a enseigné de nombreux concepts de programmation mieux que quiconque, y compris les concepts dont j'ai écrit dans cet article.

[André Jaenisch](https://jaenis.ch/), mon mentor et ami, sans ses efforts de révision et son soutien constant, je n'aurais pas écrit cet article.

Bon apprentissage !