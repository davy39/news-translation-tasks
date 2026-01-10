---
title: Qu'est-ce que le CPU ? Signification, Définition et Que Signifie CPU
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-16T22:53:22.000Z'
originalURL: https://freecodecamp.org/news/what-is-cpu-meaning-definition-and-what-cpu-stands-for
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/niek-doup-Xf071ws2Icg-unsplash.jpg
tags:
- name: Computer Science
  slug: computer-science
- name: cpu
  slug: cpu
seo_title: Qu'est-ce que le CPU ? Signification, Définition et Que Signifie CPU
seo_desc: 'Every single computing device has a CPU.

  You may have heard of this tech term before, but what is it exactly? What is a CPU
  and how does it work?

  In this beginner-friendly article you''ll learn the basics on what a CPU actually
  is, and I''l give you an...'
---

Chaque appareil informatique possède un CPU.

Vous avez peut-être déjà entendu ce terme technique, mais qu'est-ce que c'est exactement ? Qu'est-ce qu'un CPU et comment fonctionne-t-il ?

Dans cet article adapté aux débutants, vous apprendrez les bases de ce qu'est réellement un CPU, et je vous donnerai un aperçu de son fonctionnement.

## Qu'est-ce qu'un CPU et où le trouve-t-on dans un ordinateur ?

CPU est l'abréviation de Central Processing Unit (Unité Centrale de Traitement). Il est également connu sous le nom de processeur ou microprocesseur.

C'est l'un des éléments matériels les plus importants de tout système informatique numérique – sinon le plus important.

À l'intérieur d'un CPU, il y a des milliers de *transistors* microscopiques, qui sont de minuscules interrupteurs contrôlant le flux d'électricité à travers les circuits intégrés.

Vous trouverez le CPU situé sur la *carte mère* d'un ordinateur.

La carte mère d'un ordinateur est la carte de circuit principale à l'intérieur d'un ordinateur. Son rôle est de connecter tous les composants matériels ensemble.

Souvent appelé le cerveau et le cœur de tous les systèmes numériques, un CPU est responsable de tout le travail. Il effectue chaque action qu'un ordinateur exécute et lance les programmes.

### Qu'est-ce que les programmes informatiques et où sont-ils stockés ?

Il existe un programme pour tout ce qu'un CPU fait.

Vous avez un programme qui vous permet d'utiliser votre navigateur web ou un traitement de texte. Vous en avez un qui effectue des opérations mathématiques sur une calculatrice ou vous permet de taper des lettres et des caractères sur un clavier. Et il y a des programmes qui gèrent le clic et la sélection d'éléments avec une souris d'ordinateur et l'appui sur le pavé tactile de votre ordinateur portable.

Quoi que ce soit, il existe un programme pour toutes les activités informatiques.

Les programmes sont des ensembles d'instructions qui doivent être exécutées dans un ordre séquentiel et logique, et suivies précisément étape par étape.

Ils sont écrits dans un langage lisible par l'homme – un langage de programmation – par un programmeur.

Les ordinateurs ne comprennent pas directement les langages de programmation, ils doivent donc être traduits dans une forme plus facilement compréhensible.

Cette forme est appelée langage machine ou binaire.

Le binaire est un système numérique en *base deux*. Il est composé de seulement deux chiffres : 0 et 1.

Cela reflète bien les deux seuls états possibles des transistors pour contrôler le flux d'électricité – ils sont soit allumés (1) soit éteints (0).

Ainsi, sous le capot, les programmes sont stockés sous forme de séquences de bits. Les bits sont un autre nom pour les chiffres binaires (séquences de 1 et de 0).

Les programmes sont stockés de manière permanente et à long terme dans un dispositif de stockage, qu'il s'agisse d'un HDD (Hard Disk Drive) ou d'un SSD (Solid State Drive).

Ce sont des types de mémoire non volatils, ce qui signifie qu'ils stockent les données même lorsque l'alimentation est coupée.

Alors qu'un programme est en cours d'exécution et actuellement utilisé, toutes ses données sont stockées dans la mémoire principale, primaire, ou RAM (Random Access Memory).

Ce type de mémoire est volatile, et toutes les données sont perdues lorsque l'alimentation est coupée.

## Que fait un CPU ?

En résumé, un CPU est responsable de la gestion du traitement des opérations logiques et mathématiques et de l'exécution des instructions qui lui sont données.

Il peut exécuter des millions d'instructions par seconde – mais ne peut effectuer qu'une seule instruction à la fois.

Il reçoit d'abord un type d'entrée, généralement depuis un dispositif d'entrée (tel qu'un écran de moniteur, un clavier, une souris ou un microphone) ou depuis un programme logiciel d'application/système (comme votre navigateur web ou système d'exploitation).

Ensuite, le CPU est responsable de quatre tâches :

1) **Récupérer** les instructions depuis la mémoire, afin de savoir comment gérer l'entrée et connaître les instructions correspondantes pour ces données d'entrée particulières qu'il a reçues. Plus précisément, il recherche l'adresse de l'instruction correspondante et transmet la demande à la RAM. Le CPU et la RAM travaillent constamment ensemble. Cela s'appelle également *lire depuis* la mémoire.
2) **Décoder** ou traduire les instructions dans une forme que le CPU peut comprendre, qui est le langage machine (binaire).
3) **Exécuter** et réaliser les instructions données.
4) **Stocker** le résultat de l'exécution dans la mémoire pour une récupération ultérieure si et lorsque cela est demandé. Cela s'appelle également *écrire dans* la mémoire.

Enfin, il y a une sortie de quelque sorte, comme l'impression de quelque chose à l'écran.

Le processus décrit ci-dessus est appelé le cycle **fetch-execute**, et il se produit des millions de fois par seconde.

![Screenshot-2021-10-25-at-5.30.18-PM](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-10-25-at-5.30.18-PM.png)

## Les principales parties d'un CPU

Maintenant que vous connaissez les tâches de base qu'un CPU effectue pour chaque opération se produisant sur un ordinateur, quelles sont les parties du CPU qui aident à accomplir ce travail ?

Voici quelques-uns des composants importants à l'intérieur :

- **CU** (abréviation de Control Unit, Unité de Contrôle). Elle régule le flux d'entrée et de sortie. C'est la partie qui récupère et récupère les instructions depuis la mémoire principale et les décode ensuite.
- **ALU** (abréviation de Arithmetic Logic Unit, Unité Arithmétique et Logique). La partie où tout le traitement se produit. C'est ici que toutes les calculs mathématiques ont lieu, comme l'addition, la soustraction, la multiplication et la division, ainsi que toutes les opérations logiques pour la prise de décision, comme la comparaison de données.
- **Registres**. Un emplacement de mémoire extrêmement rapide. Les données et les instructions qui sont actuellement traitées pendant le cycle fetch-execute y sont stockées, pour un accès rapide par le processeur.

## Qu'est-ce que les cœurs de CPU ?

Plus tôt, vous avez appris qu'un CPU ne peut généralement effectuer qu'une seule action à la fois.

Il exécute une instruction à la fois et le fait avec l'aide de cœurs physiques.

Essentiellement, un cœur est un CPU en soi, un dispositif séparé à l'intérieur de la puce principale du CPU. Cela signifie qu'il a la capacité de faire une seule chose à la fois.

Cependant, les ordinateurs modernes ont la capacité de supporter plus d'un cœur à l'intérieur de la puce principale.

Plus un CPU a de cœurs, plus la puissance de calcul est grande et plus de tâches peuvent être exécutées et complétées simultanément, faisant du CPU un multitâche en série.

Par exemple, il existe des CPU dual-core, ce qui signifie qu'il y a deux CPU sur la même puce et qu'ils peuvent exécuter deux instructions en même temps.

Les CPU quad-core signifient qu'il y a quatre CPU sur la même puce, les CPU hexa-core signifient qu'il y a six cœurs, et ainsi de suite.

### Qu'est-ce que l'hyperthreading ?

Les CPU modernes supportent également une technologie appelée hyperthreading.

Le fonctionnement de cela est qu'un seul cœur physique apparaît comme plusieurs cœurs physiques, faisant croire au système d'exploitation qu'il y a plus de cœurs qu'il n'y en a réellement. Cela fait à son tour croire à l'ordinateur qu'il a plus de puissance qu'il n'en a réellement.

Ainsi, en plus des cœurs physiques mentionnés dans la section ci-dessus, il y a également ces cœurs virtuels, ou threads comme on les appelle également.

Ils ne sont pas des cœurs physiques réels, mais ils semblent l'être.

La combinaison des cœurs physiques et virtuels rend le temps d'exécution des programmes encore plus rapide et donne au CPU encore plus de puissance de calcul.

## Conclusion

Merci d'avoir lu et d'être arrivé à la fin ! Espérons que vous avez maintenant une meilleure compréhension de ce que sont les CPU, ce qu'ils font et pourquoi ils sont si importants.

Si vous souhaitez en savoir plus sur les bases de l'informatique, consultez [ce guide qui passe en revue les parties de base d'un ordinateur](https://www.freecodecamp.org/news/what-is-a-pc-computer-definition-and-computer-basics-for-beginners/).

Bon apprentissage !