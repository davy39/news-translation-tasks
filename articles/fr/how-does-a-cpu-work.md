---
title: Comment fonctionne un CPU ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-18T22:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-does-a-cpu-work
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_n3hgXdDt8zb5pvjmBi570g.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: cpu
  slug: cpu
- name: programing
  slug: programing
seo_title: Comment fonctionne un CPU ?
seo_desc: 'By Milap Neupane

  CPU, also known as the microprocessor is the heart and/or brain of a computer. Lets
  Deep dive into the core of the computer to help us write computer programs efficiently.


  "A tool is usually more simple than a machine; it is general...'
---

Par Milap Neupane

Le CPU, également connu sous le nom de microprocesseur, est le cœur et/ou le cerveau d'un ordinateur. Plongeons au cœur de l'ordinateur pour nous aider à écrire des programmes informatiques efficacement.

> *"Un outil est généralement plus simple qu'une machine ; il est généralement utilisé avec la main, tandis qu'une machine est fréquemment mue par la force animale ou la vapeur."*  
>   
> *– Charles Babbage*

*Un* ***ordinateur*** est une **machine** alimentée principalement par l'électricité, mais sa flexibilité et sa programmabilité ont aidé à atteindre la simplicité d'un outil.

Le **CPU** est le cœur et/ou le cerveau d'un ordinateur. Il exécute les instructions qui lui sont fournies. Son travail principal est d'effectuer des opérations arithmétiques et logiques et d'orchestrer les instructions ensemble. Avant de plonger dans les parties principales, commençons par examiner quels sont les principaux composants d'un CPU et quels sont leurs rôles :

### Deux principaux composants d'un processeur

* ***Unité de contrôle – CU***
    
* ***Unité arithmétique et logique – ALU***
    

#### Unité de contrôle – CU

L'unité de contrôle CU est la partie du CPU qui aide à orchestrer l'exécution des instructions. Elle indique quoi faire. Selon l'instruction, elle aide à activer les fils reliant le CPU à différentes autres parties de l'ordinateur, y compris l'**ALU**. L'unité de contrôle est le premier composant du CPU à recevoir l'instruction pour le traitement.

Il existe deux types d'unités de contrôle :

* unités de contrôle **câblées**.
    
* unités de contrôle **microprogrammables** (microprogrammées).
    

Les unités de contrôle **câblées** sont matérielles et nécessitent un changement de matériel pour modifier leur fonctionnement, tandis que les unités de contrôle **microprogrammables** peuvent être programmées pour changer leur comportement. Les CU câblées sont plus rapides dans le traitement des instructions, tandis que les microprogrammables sont plus flexibles.

#### Unité arithmétique et logique – ALU

L'unité arithmétique et logique ALU, comme son nom l'indique, effectue tous les calculs arithmétiques et logiques. L'ALU effectue des opérations comme l'addition, la soustraction. L'ALU est composée de circuits logiques ou de portes logiques qui effectuent ces opérations.

La plupart des portes logiques prennent deux entrées et produisent une sortie.

Ci-dessous se trouve un exemple de circuit demi-additionneur qui prend deux entrées et sort le résultat. Ici, A et B sont les entrées, S est la sortie et C est la retenue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u-VunK6bUafXlhubpGlNkA.png align="left")

*Source :* [*https://en.wikipedia.org/wiki/Adder\_(electronics)*](https://en.wikipedia.org/wiki/Adder_\(electronics\))

### Stockage – Registres et Mémoire

Le travail principal du CPU est d'exécuter les instructions qui lui sont fournies. Pour traiter ces instructions, la plupart du temps, il a besoin de données. Certaines données sont des données intermédiaires, certaines sont des entrées et d'autres sont des sorties. Ces données, ainsi que les instructions, sont stockées dans les éléments de stockage suivants :

#### Registres

Un registre est un petit ensemble d'emplacements où les données peuvent être stockées. Un registre est une combinaison de **verrous**. Les **verrous**, également connus sous le nom de **bascules**, sont des combinaisons de **portes logiques** qui stockent 1 bit d'information.

Un verrou a deux fils d'entrée, un fil d'écriture et un fil d'entrée, et un fil de sortie. Nous pouvons activer le fil d'écriture pour modifier les données stockées. Lorsque le fil d'écriture est désactivé, la sortie reste toujours la même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5WDU45YAH5CnICZOOvn1Yw.gif align="left")

*Un verrou SR, construit à partir d'une paire de* [*portes*](https://en.wikipedia.org/wiki/NOR_gate) *couplées en croix*

Le CPU dispose de registres pour stocker les données de sortie. L'envoi à la mémoire principale (RAM) serait lent car il s'agit de données intermédiaires. Ces données sont envoyées à un autre registre qui est connecté par un **BUS**. Un registre peut stocker des instructions, des données de sortie, des adresses de stockage ou tout type de données.

#### Mémoire (RAM)

La RAM est une collection de registres disposés et compactés ensemble de manière optimisée afin qu'elle puisse stocker un nombre plus élevé de données. Les RAM (Random Access Memory) sont volatiles et leurs données sont perdues lorsque nous éteignons l'alimentation. Comme la RAM est une collection de registres pour lire/écrire des données, une RAM prend en entrée une adresse de 8 bits, une entrée de données pour les données réelles à stocker et enfin un activateur de lecture et d'écriture qui fonctionne comme tel pour les verrous.

### Qu'est-ce que les Instructions

Une instruction est le niveau granulaire de calcul qu'un ordinateur peut effectuer. Il existe divers types d'instructions qu'un CPU peut traiter.

Les instructions incluent :

* Arithmétique telle que **add** et **subtract**
    
* Instructions logiques telles que **and**, **or**, et **not**
    
* Instructions de données telles que **move**, **input**, **output**, **load**, et **store**
    
* Instructions de flux de contrôle telles que **goto**, **if … goto**, **call**, et **return**
    
* Notifier le CPU que le programme s'est terminé **Halt**
    

Les instructions sont fournies à l'ordinateur en utilisant le langage d'assemblage ou sont générées par le compilateur ou sont interprétées dans certains langages de haut niveau.

Ces instructions sont câblées à l'intérieur du CPU. L'ALU contient l'arithmétique et la logique tandis que le flux de contrôle est géré par le CU.

En un **cycle d'horloge**, les ordinateurs peuvent effectuer une instruction, mais les ordinateurs modernes peuvent en effectuer plus d'une.

Un groupe d'instructions qu'un ordinateur peut effectuer est appelé un **jeu d'instructions**.

### Horloge du CPU

**Cycle d'horloge**

La vitesse d'un ordinateur est déterminée par son cycle d'horloge. C'est le nombre de **périodes d'horloge** par seconde qu'un ordinateur utilise. Un seul cycle d'horloge est très petit, environ 250 \* 10 \*-12 sec. Plus le cycle d'horloge est élevé, plus le processeur est rapide.

Le cycle d'horloge du CPU est mesuré en gHz (**Gigahertz**). 1 gHz est égal à 10 	 Hz (**hertz**). Un hertz signifie une seconde. Donc 1 Gigahertz signifie 10 	 cycles par seconde.

Plus le cycle d'horloge est rapide, plus le **CPU** peut exécuter d'instructions. Cycle d'horloge = 1/taux d'horloge Temps CPU = nombre de cycles d'horloge / taux d'horloge

Cela signifie que pour améliorer le temps CPU, nous pouvons augmenter le taux d'horloge ou diminuer le nombre de cycles d'horloge en optimisant les instructions que nous fournissons au CPU. Certains processeurs offrent la possibilité d'augmenter le cycle d'horloge, mais comme il s'agit de changements physiques, il peut y avoir une surchauffe et même des fumées/incendies.

### Comment une instruction est-elle exécutée

Les instructions sont stockées dans la **RAM** dans un ordre séquentiel. Pour un CPU hypothétique, une instruction se compose d'un code **OP** (code opérationnel) et d'une **adresse de mémoire ou de registre**.

Il y a deux registres à l'intérieur d'une unité de contrôle : le **registre d'instruction (IR)** qui charge le code OP de l'instruction et le **registre d'adresse d'instruction** qui charge l'adresse de l'instruction en cours d'exécution. Il y a d'autres registres à l'intérieur d'un CPU qui stockent la valeur stockée à l'adresse des 4 derniers bits d'une instruction.

Prenons un exemple d'un ensemble d'instructions qui additionne deux nombres. Voici les instructions ainsi que leur description :

**ÉTAPE 1 – LOAD\_A 8 :**

L'instruction est initialement enregistrée dans la RAM, disons &lt;1100 1000&gt;. Les 4 premiers bits sont le code d'opération. Cela détermine l'instruction. Cette instruction est **récupérée** dans l'**IR** de l'unité de contrôle. L'instruction est **décodée** pour être load\_A, ce qui signifie qu'elle doit charger les données à l'adresse 1000, qui est les 4 derniers bits de l'instruction, dans le registre A.

**ÉTAPE 2 – LOAD\_B 2**

De manière similaire à ci-dessus, cela charge les données à l'adresse mémoire 2 (0010) dans le registre B du CPU.

**ÉTAPE 3 – ADD B A**

Maintenant, l'instruction suivante est d'additionner ces deux nombres. Ici, le CU indique à l'ALU d'effectuer l'opération d'addition et de sauvegarder le résultat dans le registre A.

**ÉTAPE 4 – STORE\_A 23**

Il s'agit d'un ensemble d'instructions très simple qui aide à additionner deux nombres.

Nous avons réussi à additionner deux nombres !

#### **BUS**

Toutes les données entre le CPU, le registre, la mémoire et les dispositifs d'E/S sont transférées via le bus. Pour charger les données en mémoire qu'il vient d'ajouter, le CPU place l'adresse mémoire sur le bus d'adresse et le résultat de la somme sur le bus de données et active le bon signal dans le bus de contrôle. De cette manière, les données sont chargées en mémoire avec l'aide du bus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*N5wkXycN_ceV9HByxQUzCA.png align="left")

*Source :* [*https://en.wikipedia.org/wiki/Bus\_(computing)*](https://en.wikipedia.org/wiki/Bus_\(computing\))

#### Cache

Le CPU dispose également d'un mécanisme pour précharger les instructions dans son cache. Comme nous le savons, il y a des millions d'instructions qu'un processeur peut compléter en une seconde. Cela signifie qu'il y aura plus de temps passé à récupérer les instructions de la RAM qu'à les exécuter. Ainsi, le cache du CPU précharge certaines des instructions et également des données afin que l'exécution soit plus rapide.

Si les données dans le cache et la mémoire opérationnelle sont différentes, les données sont marquées comme un **bit sale**.

#### **Pipeline d'instructions**

Les CPU modernes utilisent le **pipeline d'instructions** pour la parallélisation dans l'exécution des instructions. Récupérer, Décoder, Exécuter. Lorsque une instruction est en phase de décodage, le CPU peut traiter une autre instruction pour la phase de récupération.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FJxls8ZBHc3l3tTKxrO6Sg.png align="left")

*Source :* [*https://en.wikipedia.org/wiki/Instruction\_pipelining*](https://en.wikipedia.org/wiki/Instruction_pipelining)

Cela pose un problème lorsque une instruction dépend d'une autre. Ainsi, les processeurs exécutent les instructions qui ne sont pas dépendantes et dans un ordre différent.

#### Ordinateur multicœur

Il s'agit essentiellement de différents CPU mais avec certaines ressources partagées comme le cache.

### Performance

La performance d'un CPU est déterminée par son temps d'exécution. Performance = 1/temps d'exécution

Disons qu'il faut 20 ms pour qu'un programme s'exécute. La performance du CPU est de 1/20 = 0,05 ms Performance relative = temps d'exécution 1 / temps d'exécution 2

Les facteurs qui entrent en considération pour la performance d'un CPU sont le temps d'exécution des instructions et la vitesse d'horloge du CPU. Ainsi, pour augmenter la performance d'un programme, nous devons soit augmenter la vitesse d'horloge, soit diminuer le nombre d'instructions dans un programme. La vitesse du processeur est limitée et les ordinateurs modernes avec plusieurs cœurs peuvent supporter des millions d'instructions par seconde. Mais si le programme que nous avons écrit contient beaucoup d'instructions, cela diminuera la performance globale.

La **notation Big O** détermine comment la performance sera affectée avec l'entrée donnée.

Il y a beaucoup d'optimisations faites dans le CPU pour le rendre plus rapide et performant. Lors de l'écriture de tout programme, nous devons considérer comment la réduction du nombre d'instructions que nous fournissons au CPU augmentera la performance du programme informatique.

---

Également publié sur le blog de Milap Neupane : [How Does a CPU work](https://milapneupane.com.np/2019/07/06/how-does-a-cpu-work/)