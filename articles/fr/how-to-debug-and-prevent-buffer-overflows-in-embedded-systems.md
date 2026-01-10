---
title: Comment déboguer et prévenir les débordements de tampon dans les systèmes embarqués
subtitle: ''
author: Soham Banerjee
co_authors: []
series: null
date: '2025-03-17T16:34:42.768Z'
originalURL: https://freecodecamp.org/news/how-to-debug-and-prevent-buffer-overflows-in-embedded-systems
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742229245130/858b21cc-443e-43ee-82ce-091438f6c5c0.png
tags:
- name: embedded systems
  slug: embedded-systems
- name: embedded
  slug: embedded
- name: memory-management
  slug: memory-management
- name: Buffer Overfow
  slug: buffer-overfow
- name: debugging
  slug: debugging
- name: Firmware Development
  slug: firmware-development
- name: Security
  slug: security
- name: Code Quality
  slug: code-quality
- name: Software Engineering
  slug: software-engineering
- name: learn to code
  slug: learn-to-code
- name: Programming basics
  slug: programming-basics
- name: C
  slug: c
- name: Coding Best Practices
  slug: coding-best-practices
- name: clean code
  slug: clean-code
seo_title: Comment déboguer et prévenir les débordements de tampon dans les systèmes
  embarqués
seo_desc: 'Buffer overflows are one of the most serious software bugs, especially
  in embedded systems, where hardware limitations and real-time execution make them
  hard to detect and fix.

  A buffer overflow happens when a program writes more data into a buffer t...'
---

Les débordements de tampon sont l'un des bugs logiciels les plus graves, en particulier dans les systèmes embarqués, où les limitations matérielles et l'exécution en temps réel les rendent difficiles à détecter et à corriger.

Un débordement de tampon se produit lorsqu'un programme écrit plus de données dans un tampon que ce qui a été alloué, entraînant une corruption de la mémoire, des plantages ou même des vulnérabilités de sécurité. Une corruption de tampon se produit lorsque des modifications non intentionnelles écrasent des données non lues ou modifient la mémoire de manière inattendue.

Dans les systèmes critiques pour la sécurité comme les voitures, les dispositifs médicaux et les engins spatiaux, les débordements de tampon peuvent causer des défaillances mettant la vie en danger. Contrairement aux simples bugs logiciels, les débordements de tampon sont imprévisibles et dépendent de l'état du système, ce qui les rend difficiles à diagnostiquer et à déboguer.

Pour prévenir ces problèmes, il est important de comprendre comment les débordements de tampon et les corruptions se produisent, et comment les détecter et les corriger.

## Portée de l'article

Dans cet article, vous apprendrez :

1. Ce que sont les tampons, les débordements de tampon et les corruptions. Je vous donnerai une explication adaptée aux débutants avec des exemples concrets.

2. Comment déboguer les débordements de tampon. Vous apprendrez à utiliser des outils comme GDB, LLDB et les cartes mémoire pour trouver les corruptions de mémoire.

3. Comment prévenir les débordements de tampon. Nous aborderons certaines bonnes pratiques comme la validation des entrées, la gestion sécurisée de la mémoire et la programmation défensive.

Je vous montrerai également quelques exemples de code pratiques - des programmes C simples qui démontrent les problèmes de débordement de tampon et comment les corriger.

Ce que cet article ne couvre pas :

1. Les exploits de sécurité et les techniques de piratage. Nous nous concentrerons sur la prévention des débordements accidentels, pas sur les débordements de tampon liés au piratage.

2. Les problèmes spécifiques au système d'exploitation. Ce guide est pour les systèmes embarqués, pas pour les ordinateurs ou serveurs à usage général.

3. La gestion avancée de la mémoire RTOS. Bien que nous discutions des débordements pilotés par interruption, nous n'approfondirons pas les concepts de système d'exploitation en temps réel (RTOS).

Maintenant que vous savez ce que cet article couvre (et ce qu'il ne couvre pas), passons en revue les compétences qui vous aideront à en tirer le meilleur parti.

## Prérequis

Cet article est conçu pour les développeurs qui ont une certaine expérience avec la programmation C et qui veulent comprendre comment déboguer et prévenir les débordements de tampon dans les systèmes embarqués. Cependant, les débutants peuvent suivre, car j'expliquerai les concepts clés de manière claire et structurée.

Avant de lire, il est utile de connaître :

1. La programmation C de base.

2. Le fonctionnement de la mémoire - la différence entre la pile, le tas et les variables globales.

3. Les concepts de base du débogage - si vous avez utilisé un débogueur comme GDB ou LLDB, c'est un plus, mais ce n'est pas obligatoire.

4. Ce que sont les systèmes embarqués - une idée de base de la manière dont les microcontrôleurs stockent et gèrent la mémoire.

Même si vous n'êtes pas familier avec ces sujets, ce guide vous guidera à travers eux de manière facile à comprendre.

Avant de plonger dans les débordements de tampon, le débogage et la prévention, faisons un pas en arrière et comprenons ce qu'est un tampon et pourquoi il est important dans les systèmes embarqués. Les tampons jouent un rôle crucial dans la gestion du flux de données entre le matériel et le logiciel, mais lorsqu'ils sont mal gérés, ils peuvent entraîner des défaillances logicielles graves.

## Table des matières

* [Qu'est-ce qu'un tampon et comment fonctionne-t-il ?](#heading-quest-ce-quun-tampon-et-comment-fonctionne-t-il)

* [Qu'est-ce qu'un débordement de tampon ?](#heading-quest-ce-quun-debordement-de-tampon)

* [Causes courantes des débordements et corruptions de tampon](#heading-causes-courantes-des-debordements-et-corruptions-de-tampon)

* [Conséquences des débordements de tampon](#heading-consequences-des-debordements-de-tampon)

* [Comment déboguer les débordements de tampon](#heading-comment-deboguer-les-debordements-de-tampon)

* [Comment prévenir les débordements de tampon](#heading-comment-prevenir-les-debordements-de-tampon)

* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un tampon et comment fonctionne-t-il ?

Un tampon est un bloc contigu de mémoire utilisé pour stocker temporairement des données avant qu'elles ne soient traitées. Les tampons sont couramment utilisés dans deux scénarios :

1. Accumulation de données : Lorsque le système doit collecter une certaine quantité de données avant le traitement.

2. Correspondance de débit : Lorsque le producteur de données génère des données plus rapidement que le consommateur de données ne peut les traiter.

Les tampons sont généralement implémentés sous forme de tableaux en C, où les éléments sont indexés de 0 à N-1 (où N est la taille du tampon).

Examinons un exemple de tampon dans un système de capteurs.

Considérons un système avec une tâche de capteur qui génère des données à 400 Hz (400 échantillons par seconde ou 1 échantillon toutes les 2,5 ms). Mais le processeur de données (consommateur) fonctionne à seulement 100 Hz (100 échantillons par seconde ou 1 échantillon toutes les 10 ms). Comme la tâche du consommateur est plus lente que celle du producteur, nous avons besoin d'un tampon pour stocker les données entrantes jusqu'à ce qu'elles soient traitées.

Pour déterminer la taille du tampon, nous calculons :

Taille du tampon = Temps pour consommer 1 échantillon / Temps pour générer 1 échantillon = 10 ms / 2,5 ms = 4

Cela signifie que le tampon doit contenir au moins 4 échantillons à la fois pour éviter la perte de données.

Une fois que le tampon atteint sa capacité, il existe plusieurs stratégies pour décider quelles données sont transmises à la tâche du consommateur :

1. Échantillonnage max/min : Utiliser la valeur maximale ou minimale dans le tampon.

2. Moyenne : Calculer la moyenne de toutes les valeurs dans le tampon.

3. Accès aléatoire : Choisir un échantillon à partir d'un emplacement spécifique (par exemple, le plus récent ou le premier).

Dans les applications réelles, il est bénéfique d'utiliser des tampons circulaires ou des tampons doubles pour prévenir la corruption des données.

* Approche de tampon circulaire : Un tampon circulaire (également appelé tampon annulaire) s'enroule continuellement lorsqu'il atteint la fin, garantissant que les anciennes données sont écrasées en toute sécurité sans dépasser les limites de la mémoire. La taille du tampon doit être multipliée par 2 (4 × 2 = 8) pour contenir 8 échantillons. Cela permet à la tâche du consommateur de traiter 4 échantillons pendant que les 4 échantillons suivants sont remplis, empêchant les écrasements de données.

* Approche de tampon double : Le double tamponnage est utile lorsque la perte de données est inacceptable. Il permet une capture continue des données pendant que le processeur est occupé à traiter les données précédentes. Un second tampon de la même taille est ajouté. Lorsque le premier tampon est plein, le pointeur d'écriture bascule vers le second tampon, permettant à la tâche du consommateur de traiter les données du premier tampon pendant que le second tampon est rempli. Cela empêche les écrasements de données et garantit un flux de données continu.

Les tampons aident à gérer les données de manière efficace, mais que se passe-t-il lorsqu'ils sont mal gérés ? C'est là que les débordements et corruptions de tampon entrent en jeu.

## Qu'est-ce qu'un débordement de tampon ?

Un débordement de tampon se produit lorsqu'un programme écrit plus de données dans un tampon que ce qui a été alloué, provoquant une corruption de mémoire non intentionnelle. Cela peut entraîner un comportement imprévisible, allant de bugs mineurs à des défaillances critiques du système.

Pour comprendre le débordement de tampon, utilisons une analogie simple. Imaginez une cruche avec un robinet près du bas. La cruche représente un tampon, tandis que le robinet contrôle la quantité de liquide (données) consommée.

La cruche est conçue pour contenir une quantité fixe de liquide. Tant que l'eau s'écoule dans la cruche au même rythme ou plus lentement qu'elle ne s'écoule, tout fonctionne bien. Mais si l'eau s'écoule plus rapidement qu'elle ne s'écoule, la cruche finira par déborder.

De même, dans un logiciel, si des données entrent dans un tampon plus rapidement qu'elles ne sont traitées, elles dépassent l'espace mémoire alloué, provoquant un débordement de tampon. Dans le cas d'un tampon circulaire, cela peut amener le pointeur d'écriture à s'enrouler et à écraser des données non lues, entraînant une corruption de tampon.

### Débordements de tampon dans les logiciels

Contrairement à la cruche, où l'eau déborde simplement, un débordement de tampon dans un logiciel écrase les emplacements mémoire adjacents. Cela peut provoquer divers problèmes difficiles à diagnostiquer, notamment :

1. Corrompre d'autres données stockées à proximité.

2. Modifier l'exécution du programme, entraînant des plantages.

3. Des vulnérabilités de sécurité, où les attaquants exploitent les débordements pour injecter du code malveillant.

Lorsqu'un débordement de tampon se produit, les données peuvent écraser des variables, des pointeurs de fonction ou même des adresses de retour, selon l'endroit où le tampon est alloué.

Les débordements de tampon peuvent se produire dans différentes régions de la mémoire :

1. Débordements de tampon dans la mémoire globale/statique (sections .bss / .data)

* Ceux-ci se produisent lorsque les variables globales ou statiques dépassent leur taille allouée.

* Le débordement peut corrompre les variables adjacentes, entraînant un comportement inattendu dans d'autres modules.

* Le débogage est plus facile car les adresses mémoire sont fixes au moment de la compilation, sauf si le compilateur les optimise. Les fichiers map fournissent une disposition de la mémoire des variables pendant la compilation et l'édition des liens.

2. Débordement de tampon basé sur la pile (plus prévisible, plus facile à déboguer) :

* Se produit lorsqu'un tampon est alloué dans la pile (par exemple, des variables locales à l'intérieur des fonctions).

* Le débordement de la pile peut affecter les variables locales adjacentes ou les adresses de retour, provoquant potentiellement le plantage du programme.

* Dans les systèmes embarqués avec des tailles de pile réduites, cela conduit souvent à un plantage ou à l'exécution de code non intentionnel.

3. Débordement de tampon basé sur le tas (plus difficile à déboguer) :

* Se produit lorsqu'un tampon est alloué dynamiquement dans le tas (par exemple, en utilisant malloc() en C).

* Le débordement d'un tampon de tas peut corrompre des objets alloués dynamiquement adjacents ou des structures de gestion de tas.

* Le débogage est plus difficile car la mémoire du tas est allouée dynamiquement à l'exécution, ce qui fait varier les emplacements mémoire.

#### Débordement de tampon vs Corruption de tampon

Le débordement de tampon et la corruption de tampon sont bien sûr liés, mais font référence à des situations différentes.

Un débordement de tampon se produit lorsque des données sont écrites au-delà de la taille allouée du tampon, entraînant une corruption de la mémoire, un comportement imprévisible ou des plantages du système.

Une corruption de tampon se produit lorsque des modifications de données non intentionnelles entraînent des défaillances logicielles inattendues, même si l'écriture reste dans les limites du tampon.

Les deux problèmes résultent généralement d'une mauvaise gestion du pointeur d'écriture, d'un manque de vérifications des limites et d'un comportement inattendu du système.

Maintenant que nous avons couvert ce qu'est un débordement de tampon et comment il peut écraser la mémoire, examinons de plus près comment ces problèmes affectent les systèmes embarqués.

Dans la section suivante, nous explorerons comment les débordements et corruptions de tampon se produisent dans les systèmes embarqués réels et décomposerons les causes courantes, y compris la mauvaise gestion des pointeurs et les violations de limites.

## Causes courantes des débordements et corruptions de tampon

Les systèmes embarqués utilisent des tampons pour stocker des données provenant de capteurs, d'interfaces de communication (comme UART (Universal Asynchronous Receiver-Transmitter), SPI (Serial Peripheral Interface), I2C (Inter-integrated Circuit), et des tâches en temps réel. Ces tampons sont souvent alloués statiquement pour éviter la fragmentation de la mémoire, et de nombreuses implémentations utilisent des tampons circulaires (annulaires) pour gérer efficacement les flux de données continus.

Voici trois scénarios courants où des débordements ou corruptions de tampon se produisent dans les systèmes embarqués :

### Écriture de données plus grandes que l'espace disponible

**Problème** : Le logiciel écrit les données entrantes dans le tampon sans vérifier s'il y a assez d'espace.

**Exemple** : Imaginez un tampon de 100 octets pour stocker des données de capteur. Le tampon reçoit des paquets de taille variable. Si un paquet entrant est plus grand que l'espace restant, il écrasera la mémoire adjacente, entraînant une corruption.

Alors pourquoi cela arrive-t-il ?

* Certaines conceptions embarquées incrémentent le pointeur d'écriture après avoir copié les données, rendant toute prévention de débordement trop tardive.

* De nombreuses fonctions de mémoire de bas niveau (memcpy, strcpy, etc.) ne vérifient pas les limites du tampon, entraînant des écritures non intentionnelles.

* Sans vérification appropriée des limites, une écriture volumineuse peut dépasser la taille du tampon et corrompre la mémoire à proximité.

Voici un exemple de code pour démontrer un débordement de tampon dans une section .bss / .data :

```c
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 300

static uint16_t sample_count = 0;
static uint8_t buffer[BUFFER_SIZE] = {0};

// Fonction pour simuler un scénario de débordement de tampon
void updateBufferWithData(uint8_t *data, uint16_t size)
{
    // Simulation d'un débordement de tampon : pas de vérification des limites !
    printf("Tentative d'écriture de %d octets à la position %d...\n", size, sample_count);

    // Débordement de tampon délibéré pour démonstration
    if (sample_count + size > BUFFER_SIZE)
    {
        printf("ATTENTION : Débordement de tampon produit ! Écriture au-delà de la mémoire allouée !\n");
    }

    // Copie des données (non sécurisée, peut provoquer un débordement)
    memcpy(&buffer[sample_count], data, size);

    // Incrémentation du compteur d'échantillons (incorrectement, entraînant des problèmes de retour à la ligne)
    sample_count += size;
}

int main()
{
    // Sauvegarde de 1 octet dans le tampon
    uint8_t data_to_buffer = 10;
    updateBufferWithData(&data_to_buffer, 1);

    // Sauvegarde d'un tableau de 20 octets dans le tampon
    uint8_t data_to_buffer_1[20] = {5};
    updateBufferWithData(data_to_buffer_1, sizeof(data_to_buffer_1));

    // Débordement de tampon intentionnel : sauvegarde d'un tableau de 50 x 8 octets (400 octets)
    uint64_t data_to_buffer_2[50] = {7};
    updateBufferWithData((uint8_t*)data_to_buffer_2, sizeof(data_to_buffer_2));

    return 0;
}
```

### Débordements pilotés par interruption (Systèmes en temps réel)

**Problème** : La routine de service d'interruption (ISR) peut écrire des données plus rapidement que la tâche principale ne peut les traiter, entraînant une corruption ou un débordement de tampon si le pointeur d'écriture n'est pas correctement géré.

**Exemple** : Imaginez une ISR de capteur qui écrit les données entrantes dans un tampon chaque fois qu'une nouvelle lecture arrive. Pendant ce temps, une tâche de traitement de faible priorité lit et traite les données.

Qu'est-ce qui peut mal se passer ?

* Si l'ISR se déclenche trop fréquemment (en raison d'un capteur malveillant ou d'une priorité d'interruption élevée), le tampon peut se remplir plus rapidement que la tâche de traitement ne peut suivre.

* Cela peut entraîner l'une des deux défaillances suivantes :

  1. Corruption de tampon : L'ISR écrase les données non lues, entraînant une perte d'informations.

  2. Débordement de tampon : L'ISR dépasse les limites du tampon, provoquant une corruption de la mémoire ou des plantages du système.

Alors pourquoi cela arrive-t-il ?

* Dans les systèmes embarqués en temps réel, l'exécution de l'ISR préempte les tâches de priorité inférieure.

* Si la tâche de traitement ne reçoit pas assez de temps CPU, le tampon peut être écrasé ou déborder au-delà de sa portée allouée.

### Changements d'état du système et corruption de tampon

**Problème** : Le système peut redémarrer de manière inattendue, entrer en mode basse consommation ou changer d'état de fonctionnement, laissant les pointeurs d'écriture du tampon dans un état incohérent. Cela peut entraîner une corruption de tampon (données obsolètes ou incorrectes) ou un débordement de tampon (écriture au-delà des limites du tampon).

**Scénarios d'exemple** :

1. Problème de réveil en basse consommation (risque de débordement de tampon) : Certains systèmes embarqués entrent en sommeil profond pour économiser l'énergie. Au réveil, si le pointeur d'écriture du tampon n'est pas correctement réinitialisé, il peut pointer en dehors des limites du tampon, entraînant un débordement de tampon et une corruption de mémoire non intentionnelle.

2. Transitions de mode inattendues : Si une tâche de capteur écrit des données et que le système bascule soudainement de mode, les états et pointeurs de tampon peuvent ne pas être nettoyés. La prochaine fois que la tâche de capteur s'exécute, elle peut continuer à écrire sans effacer les données précédentes. Cela peut provoquer un comportement indéfini en raison de la présence de données obsolètes.

Maintenant que vous comprenez comment les débordements et corruptions de tampon se produisent, examinons leurs conséquences dans les systèmes embarqués, allant des lectures de capteurs incorrectes aux défaillances complètes du système, rendant le débogage et la prévention critiques.

## Conséquences des débordements de tampon

Les débordements de tampon peuvent être catastrophiques dans les systèmes embarqués, entraînant des plantages du système, une corruption des données et un comportement imprévisible. Contrairement aux ordinateurs à usage général, de nombreux dispositifs embarqués manquent de protection de la mémoire, les rendant particulièrement vulnérables aux débordements de tampon.

Un débordement de tampon peut corrompre deux types critiques de mémoire :

### 1. Corruption des variables de données

Un débordement de tampon peut écraser des variables de données, corrompant les entrées pour d'autres modules logiciels. Cela peut provoquer un comportement inattendu ou même des plantages du système si des paramètres critiques sont modifiés.

Par exemple, un débordement de tampon pourrait accidentellement écraser une valeur d'étalonnage de capteur stockée en mémoire. En conséquence, le système commencerait à utiliser des lectures de capteur incorrectes, entraînant un fonctionnement défectueux et potentiellement des conditions non sécurisées.

### 2. Corruption des pointeurs de fonction

Dans les systèmes embarqués, les pointeurs de fonction sont souvent utilisés pour les gestionnaires d'interruption, les fonctions de rappel et la planification des tâches RTOS. Si un débordement de tampon corrompt un pointeur de fonction, le système peut exécuter des instructions non intentionnelles, entraînant un plantage ou un comportement inattendu.

Par exemple, un pointeur de fonction contrôlant la régulation de la vitesse du moteur pourrait être écrasé. Au lieu d'exécuter la fonction correcte, le système sauterait à une adresse mémoire aléatoire, provoquant une défaillance du système ou un comportement erratique du moteur.

Les débordements de tampon sont parmi les bugs les plus difficiles à identifier et à corriger car leurs effets dépendent des données corrompues et des valeurs qu'elles contiennent. Un débordement de tampon peut affecter la mémoire de différentes manières :

* Si un débordement de tampon corrompt une mémoire inutilisée, le système peut sembler fonctionner correctement pendant les tests, rendant le problème plus difficile à détecter.

* Si un débordement de tampon modifie des variables de données critiques, il peut provoquer des erreurs logiques cachées qui entraînent un comportement imprévisible.

* Si un débordement de tampon corrompt des pointeurs de fonction, il peut planter immédiatement, rendant le problème plus facile à identifier.

Pendant le développement, si les tests se concentrent uniquement sur la détection des plantages, ils peuvent négliger la corruption silencieuse de la mémoire causée par un débordement de tampon. Dans les déploiements réels, de nouveaux cas d'utilisation non couverts par les tests peuvent déclencher des problèmes de débordement de tampon précédemment non détectés, entraînant des défaillances imprévisibles.

Les débordements de tampon peuvent provoquer une réaction en chaîne, où un débordement en entraîne un autre ou une corruption de tampon, entraînant des défaillances généralisées du système. Alors comment cela se produit-il ?

1. Un débordement de tampon corrompt une variable critique (par exemple, un intervalle de temporisateur).

2. La variable corrompue perturbe un autre module (par exemple, déclenche l'interruption du temporisateur trop fréquemment, l'amenant à pousser plus de données dans un tampon que prévu).

3. Cette fréquence d'interruption accrue force une tâche de capteur à écrire des données plus rapidement que prévu, entraînant finalement un autre débordement de tampon ou une corruption en écrasant des données non lues.

Cette réaction en chaîne peut se propager à travers plusieurs modules logiciels, rendant le débogage presque impossible. Dans les applications réelles, les débordements de tampon dans les systèmes embarqués peuvent être mortels :

* Dans les voitures : Un débordement de tampon dans un ECU (Electronic Control Unit) pourrait provoquer une défaillance des freins ou une accélération non intentionnelle.

* Dans un engin spatial : Un problème de corruption de mémoire pourrait désactiver les systèmes de navigation, entraînant un échec de la mission.

Maintenant que nous avons vu comment les débordements de tampon peuvent corrompre la mémoire, perturber le comportement du système et même provoquer des défaillances critiques, l'étape suivante consiste à comprendre comment les détecter et les corriger avant qu'ils ne conduisent à des problèmes graves.

## Comment déboguer les débordements de tampon

Le débogage des débordements de tampon dans les systèmes embarqués peut être complexe, car leurs effets vont des plantages immédiats à la corruption silencieuse des données, les rendant difficiles à tracer. Un débordement de tampon peut provoquer soit :

1. Un plantage du système, qui est plus facile à détecter car il arrête l'exécution ou force un redémarrage du système.

2. Un comportement inattendu, qui est beaucoup plus difficile à déboguer car il nécessite de tracer comment les données corrompues affectent différents modules.

Cette section se concentre sur les techniques de débogage des systèmes embarqués en utilisant des fichiers de carte mémoire, des débogueurs (GDB/LLDB) et une approche de débogage structurée. Examinons les débogueurs et les fichiers de carte mémoire.

### Fichier de carte mémoire (.map file)

Un fichier de carte mémoire est généré pendant le processus de liaison. Il fournit une disposition de la mémoire des variables globales/statiques, des adresses de fonction et des emplacements de tas/pile. Il fournit une disposition de la mémoire Flash et RAM, y compris :

* Section de texte (.text) : Stocke le code exécutable.

* Section en lecture seule (.rodata) : Stocke les constantes et les littéraux de chaîne.

* Section BSS (.bss) : Stocke les variables globales et statiques non initialisées.

* Section de données (.data) : Stocke les variables globales et statiques initialisées.

* Emplacements de tas et de pile, selon le script de liaison.

![Figure 1 : Une visualisation de la disposition de la mémoire](https://cdn.hashnode.com/res/hashnode/image/upload/v1739064875727/1e01992d-4d9d-42fb-b971-6f4e92452c22.png align="center")

Si un débordement de tampon corrompt une variable globale, le fichier .map peut identifier les variables à proximité qui peuvent également être affectées, à condition que le compilateur n'ait pas optimisé l'allocation de mémoire. De même, si un pointeur de fonction est corrompu, le fichier .map peut révéler où il était stocké en mémoire.

### Débogueurs (GDB & LLDB)

Les outils de débogage comme GDB (GNU Debugger) et LLDB (LLVM Debugger) permettent :

* Contrôler l'exécution (points d'arrêt, exécution pas à pas du code).

* Inspecter les valeurs des variables et les adresses mémoire.

* Obtenir des backtraces (visualisation des appels de fonction avant un plantage).

* Extraire des core dumps des microcontrôleurs pour une analyse post-mortem.

Si le système s'arrête sur un plantage, un backtrace (commande bt dans GDB) peut révéler quelle fonction était en cours d'exécution avant l'échec. Si le débordement affecte une variable allouée sur le tas, GDB peut inspecter l'utilisation de la mémoire du tas pour détecter la corruption.

### Le processus de débogage

Maintenant, passons en revue un processus de débogage étape par étape pour identifier et corriger les débordements de tampon. Une fois qu'un plantage ou un comportement inattendu se produit, suivez ces techniques pour tracer la cause racine :

#### Étape 1 : Identifier le module malveillant

Si le système plante, utilisez la commande backtrace (bt) de GDB ou LLDB pour localiser la dernière fonction exécutée. Si le système se comporte de manière inattendue, déterminez quel module logiciel contrôle la fonctionnalité affectée.

#### Étape 2 : Analyser les entrées et sorties du module

Chaque fonction ou module a des entrées et des sorties. Créez une table de vérité listant les sorties attendues pour toutes les entrées possibles. Vérifiez si le comportement inattendu correspond à une combinaison d'entrée non définie, ce qui peut indiquer une corruption.

#### Étape 3 : Localiser la corruption de mémoire en utilisant l'analyse d'adresse

Si une variable montre des valeurs incorrectes, déterminez son emplacement physique en mémoire. Selon l'endroit où la variable est stockée :

1. Variables globales/statiques (.bss / .data) : Consultez le fichier de carte mémoire pour les tampons à proximité.

2. Variables de tas : Capturez les allocations de tas en utilisant GDB.

Voici un exemple d'utilisation de GDB pour trouver des variables corrompues :

```c
(gdb) print &my_variable  # Obtenir l'adresse mémoire de la variable
$1 = (int *) 0x20001000
(gdb) x/10x 0x20001000   # Examiner la mémoire près de cette adresse, Afficher 10 mots mémoire en format hexadécimal à partir de 0x20001000
```

#### Étape 4 : Identifier le tampon débordant

Si un tampon est situé juste avant la variable corrompue, inspectez son utilisation dans le code. Passez en revue tous les chemins de code possibles qui écrivent dans le tampon. Vérifiez si des limitations de conception pourraient provoquer un débordement dans des cas d'utilisation spécifiques.

#### Étape 5 : Corriger la cause racine

Si le débordement de tampon s'est produit en raison de vérifications de limites manquantes, ajoutez une validation d'entrée appropriée pour l'empêcher. La conception du tampon doit imposer des limites de mémoire strictes. Le module doit implémenter des vérifications de limites strictes pour toutes les entrées et maintenir un état cohérent.

![Figure 2 : Étapes pour déboguer un débordement de tampon](https://cdn.hashnode.com/res/hashnode/image/upload/v1739065828677/74322607-5997-4275-87d0-b3d0acf54373.png align="center")

En plus de GDB/LLDB, vous pouvez également utiliser des techniques comme le traçage matériel et l'injection de fautes pour simuler des débordements de tampon et observer le comportement du système en temps réel.

Bien que le débogage aide à identifier et à corriger les débordements de tampon, la prévention est toujours la meilleure approche. Explorons les techniques qui peuvent aider à éviter complètement les débordements de tampon.

## Comment prévenir les débordements de tampon

Vous pouvez souvent prévenir les débordements de tampon grâce à une bonne conception logicielle, une programmation défensive, des protections matérielles et des tests rigoureux. Les systèmes embarqués, contrairement aux ordinateurs à usage général, manquent souvent de mécanismes de protection de la mémoire, ce qui signifie que la prévention des débordements de tampon est cruciale pour la fiabilité et la sécurité du système.

Voici quelques techniques clés pour aider à prévenir les débordements de tampon :

### Programmation défensive

La programmation défensive aide à minimiser les risques de débordement de tampon en s'assurant que toutes les entrées sont validées et que les conditions inattendues sont gérées en toute sécurité.

Tout d'abord, il est crucial de valider la taille des entrées avant d'écrire dans un tampon. Vérifiez toujours l'index d'écriture en ajoutant la taille des données à écrire avant d'écrire les données pour vous assurer que plus de données ne sont pas écrites que l'espace tampon disponible.

Ensuite, vous voudrez vous assurer que vous avez une gestion des erreurs appropriée et des mécanismes de sécurité en place. Si une entrée est invalide, arrêtez l'exécution, journalisez l'erreur ou basculez vers un état sûr. De plus, les fonctions doivent indiquer le succès/échec avec des codes d'erreur utiles pour prévenir les mauvaises utilisations.

Exemple de code :

```c
#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

#define BUFFER_SIZE 300

static uint16_t sample_count = 0;
static uint8_t buffer[BUFFER_SIZE] = {0};

typedef enum
{
    SUCCESS = 0,
    NOT_ENOUGH_SPACE = 1,
    DATA_IS_INVALID = 2,
} buffer_err_code_e;

buffer_err_code_e updateBufferWithData(uint8_t *data, uint16_t size)
{
    if (data == NULL || size == 0 || size > BUFFER_SIZE)
    {
        return DATA_IS_INVALID; // Taille d'entrée invalide
    }

    uint16_t available_space = BUFFER_SIZE - sample_count;
    bool can_write = (available_space >= size) ? true : false;

    if (!can_write)
    {
        return NOT_ENOUGH_SPACE;
    }

    // Copie des données en toute sécurité
    memcpy(&buffer[sample_count], data, size);
    sample_count += size;

    return SUCCESS;
}

int main()
{
    buffer_err_code_e ret;

    // Sauvegarde de 1 octet dans le tampon
    uint8_t data_to_buffer = 10;
    ret = updateBufferWithData(&data_to_buffer, sizeof(data_to_buffer));
    if (ret)
    {
        printf("La mise à jour du tampon n'a pas réussi, Err:%d\n", ret);
    }

    // Sauvegarde d'un tableau de 20 octets dans le tampon
    uint8_t data_to_buffer_1[20] = {5};
    ret = updateBufferWithData(data_to_buffer_1, sizeof(data_to_buffer_1));
    if (ret)
    {
        printf("La mise à jour du tampon n'a pas réussi, Err:%d\n", ret);
    }

    // Sauvegarde d'un tableau de 50 x 8 octets, Débordement de tampon intentionnel
    uint64_t data_to_buffer_2[50] = {7};
    ret = updateBufferWithData((uint8_t*)data_to_buffer_2, sizeof(data_to_buffer_2));
    if (ret)
    {
        printf("La mise à jour du tampon n'a pas réussi, Err:%d\n", ret);
    }

    return 0;
}
```

### Choisir la bonne conception et taille de tampon

Certaines conceptions de tampon gèrent mieux les débordements que d'autres. Choisir le bon type et la bonne taille de tampon pour l'application réduit le risque de corruption.

* Les tampons circulaires (tampons annulaires) empêchent les écritures hors limites en s'enroulant. Ils écrasent les données les plus anciennes au lieu de corrompre la mémoire. Ceux-ci sont utiles pour les données de streaming en temps réel (par exemple, UART, lectures de capteurs). Cette approche est idéale pour les applications où la perte de données est inacceptable.

* Les tampons ping-pong (tampons doubles) utilisent deux tampons. Un tampon se remplit de données. Ensuite, une fois qu'il est plein, il bascule vers le second tampon pendant que le premier est traité. Cette approche est bénéfique pour les applications qui ont des exigences strictes de non-perte de données. La conception du tampon doit être basée sur la vitesse des tâches d'écriture et de lecture.

### Protection matérielle

#### Unité de protection de la mémoire (MPU)

Une MPU (Memory Protection Unit) aide à détecter les accès mémoire non autorisés, y compris les débordements de tampon, en restreignant les régions de mémoire qui peuvent être écrites. Elle empêche les débordements de tampon de modifier les régions de mémoire critiques et déclenche une faute de gestion de mémoire si un processus tente d'écrire en dehors d'une région autorisée.

Mais gardez à l'esprit qu'une MPU ne prévient pas les débordements de tampon - elle ne les détecte et n'arrête l'exécution que lorsqu'ils se produisent. Tous les microcontrôleurs n'ont pas de MPU, et certains microcontrôleurs bas de gamme manquent de protection matérielle, rendant les sauvegardes basées sur le logiciel encore plus critiques.

Les compilateurs C modernes fournissent plusieurs indicateurs pour identifier les erreurs de mémoire au moment de la compilation :

1. \-Wall -Wextra : Active les avertissements utiles

2. \-Warray-bounds : Détecte l'accès hors limites des tableaux lorsque la taille du tableau est connue au moment de la compilation

3. \-Wstringop-overflow : Avertit des débordements possibles dans les fonctions de chaîne comme memcpy et strcpy.

### Tests et validation

Les tests aident à détecter les débordements de tampon avant le déploiement, réduisant le risque de défaillances sur le terrain. Les tests unitaires de chaque fonction indépendamment avec des entrées valides, des cas limites et des entrées invalides aident à détecter les problèmes liés aux tampons tôt. Les tests automatisés impliquent de fournir des entrées aléatoires et invalides dans le système pour découvrir les plantages et les comportements inattendus. Les outils d'analyse statique comme Coverity, Clang Static Analyzer aident à détecter les débordements de tampon avant l'exécution. Exécutez des entrées réelles sur le matériel embarqué pour détecter les problèmes.

Maintenant que nous avons exploré comment identifier, déboguer et prévenir les débordements de tampon, il est clair que ces vulnérabilités posent une menace significative pour les systèmes embarqués. Des corruptions de données silencieuses aux défaillances catastrophiques du système, les conséquences peuvent être graves.

Mais avec les bons outils de débogage, une analyse systématique et des techniques préventives, vous pouvez efficacement prévenir ou atténuer les débordements de tampon dans vos systèmes.

## Conclusion

Les débordements et corruptions de tampon sont des défis majeurs dans les systèmes embarqués, entraînant des plantages, des comportements imprévisibles et des risques de sécurité. Le débogage de ces problèmes est difficile car leurs symptômes varient en fonction de l'état du système, nécessitant une analyse systématique utilisant des fichiers de carte mémoire, GDB/LLDB et des approches de débogage structurées.

Dans cet article, nous avons exploré :

* Les causes et conséquences des débordements et corruptions de tampon

* Comment déboguer les débordements de tampon en utilisant l'analyse de mémoire et les outils de débogage

* Les meilleures pratiques pour la prévention

La prévention des débordements de tampon nécessite une approche multicouche :

1. Suivre un processus de conception logicielle structuré pour identifier les risques tôt.

2. Appliquer les principes de programmation défensive pour valider les entrées et gérer les erreurs de manière élégante.

3. Utiliser des protections basées sur le matériel comme les MPU lorsque cela est disponible.

4. Activer les indicateurs du compilateur qui aident à identifier les erreurs de mémoire.

5. Tester de manière exhaustive, les tests unitaires, les tests automatisés et les revues de code aident à détecter les vulnérabilités tôt.

En mettant en œuvre ces meilleures pratiques, vous pouvez minimiser le risque de débordements de tampon dans les systèmes embarqués, améliorant la fiabilité et la sécurité.

Dans les systèmes embarqués, où la fiabilité et la sécurité sont critiques, prévenir les débordements de tampon n'est pas seulement une bonne pratique, c'est une nécessité. Un seul débordement de tampon peut compromettre un système entier. La programmation défensive, les tests rigoureux et les protections matérielles sont essentiels pour construire des applications embarquées sécurisées et robustes.