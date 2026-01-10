---
title: Comment fonctionne un CPU en interne ? Des transistors à l'architecture du
  jeu d'instructions
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-07-10T19:14:05.000Z'
originalURL: https://freecodecamp.org/news/how-does-cpu-work-internally
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/1.jpg
tags:
- name: Computers
  slug: computers
- name: cpu
  slug: cpu
- name: hardware
  slug: hardware
seo_title: Comment fonctionne un CPU en interne ? Des transistors à l'architecture
  du jeu d'instructions
seo_desc: 'The CPU (Central Process Unit) is the brain of a computer, and the main
  connection between software and hardware. It makes it possible to operate software
  on hardware.

  However, how does it work in deep detail? And how can it connect programs to certa...'
---

Le CPU (Unité Centrale de Traitement) est le cerveau d'un ordinateur, et le principal lien entre le logiciel et le matériel. Il permet de faire fonctionner des logiciels sur du matériel.

Cependant, comment fonctionne-t-il en détail ? Et comment peut-il connecter des programmes à certains matériels informatiques ?

Cet article vise à vous faire comprendre cette connexion en expliquant en profondeur comment un CPU fonctionne. Ce sujet est souvent familier uniquement à ceux ayant un background en conception de matériel informatique de l'université.

Souvent, de nombreux diplômés en informatique n'ont jamais de cours en logique numérique avancée. Ainsi, même des programmeurs très expérimentés peuvent manquer de compréhension sur la manière dont un CPU traite réellement l'information.

Bien que nous ne concevrons pas de [portes logiques à partir de transistors](https://www.homemade-circuits.com/how-to-make-logic-gates-using-transistors/) ou de [composants de CPU à partir de portes logiques](https://www.techspot.com/article/1830-how-cpus-are-designed-and-built-part-2/), nous couvrirons les concepts clés nécessaires pour comprendre comment un CPU traite les données créées par un programme écrit dans un langage de programmation.

Nous verrons :

* [Analogie : Introduction à ce qui fait fonctionner les CPU](#heading-analogie-introduction-a-ce-qui-fait-fonctionner-les-cpu)
* [Les Hubs de Mémoire : Comprendre la RAM et la ROM](#heading-les-hubs-de-memoire-comprendre-la-ram-et-la-rom)
* [Les Voies de Données : Naviguer dans le Chemin de Données du CPU](#heading-les-voies-de-donnees-naviguer-dans-le-chemin-de-donnees-du-cpu)
* [Contrôleurs de Trafic : Le Rôle des Machines à États dans les CPU](#heading-controleurs-de-trafic-le-role-des-machines-a-etats-dans-les-cpu)
* [Routines Quotidiennes : Le Cycle Fetch-Execute Expliqué](#heading-routines-quotidiennes-le-cycle-fetch-execute-explique)
* [Le Règlement : Décoder l'Architecture du Jeu d'Instructions (ISA)](#heading-le-reglement-dechiffrer-larchitecture-du-jeu-dinstructions-isa)
* [Des langages de programmation au code machine](#heading-des-langages-de-programmation-au-code-machine)
* [Défis Urbains : Résoudre les Problèmes de CPU](#heading-defis-urbains-resoudre-les-problemes-de-cpu)
* [Conclusion : Meilleure unité de contrôle et parties de données](#heading-conclusion-meilleure-unite-de-controle-et-parties-de-donnees)

Je vais utiliser l'Intel 8008 comme référence.

<h2 id="analogie">Analogie : Introduction à ce qui fait fonctionner les CPU</h2>

Pour comprendre en profondeur comment fonctionne un ordinateur, imaginons une ville comme notre scénario de la vie réelle. Nous comparerons les éléments informatiques à des parties de cette ville.

De cette façon, vous obtenez une vue plus claire des différentes parties du CPU et de leur importance. Ensuite, nous examinerons en profondeur chacun des composants.

### Les Hubs de Mémoire : Comprendre la RAM et la ROM

La RAM (Random Access Memory) est comme une bibliothèque publique de la ville : elle stocke des livres et des informations que les gens peuvent emprunter et rendre selon leurs besoins.

Dans un ordinateur, la RAM charge les données et les instructions de la mémoire de l'ordinateur nécessaires au CPU pour traiter les données.

La ROM (Read Only Memory) est comme une archive historique dans la ville : elle ne stocke que des enregistrements qui ne changeront jamais et ne seront jamais empruntés par le public.

### Les Voies de Données : Naviguer dans le Chemin de Données du CPU

Le chemin de données du CPU est le réseau de routes dans la ville. Les bus et les registres du chemin de données du CPU agissent comme le réseau routier de la ville.

Tout comme les routes aident les voitures et les gens à se déplacer, le chemin de données du CPU garantit que les données voyagent de manière efficace dans le CPU.

### Contrôleurs de Trafic : Le Rôle des Machines à États dans les CPU

Les machines à états agissent comme les systèmes de contrôle du trafic.

Le système de contrôle du trafic gère le flux de véhicules, et les machines à états gèrent le flux de données selon les instructions fournies au CPU.

### Routines Quotidiennes : Le Cycle Fetch-Execute Expliqué

Le cycle fetch-execute est le trajet quotidien pour les résidents de la ville.

Chaque jour, les gens décident où ils vont, voyagent là-bas, effectuent leurs tâches et rentrent chez eux. Ce processus est toujours répété.

De la même manière, le CPU récupère les instructions, les décode et les exécute dans un cycle répétitif.

### Le Règlement : Décoder l'Architecture du Jeu d'Instructions (ISA)

L'architecture du jeu d'instructions est comme la loi sur les transports de la ville.

La loi sur les transports de la ville montre ce qu'il est légal de faire dans la ville en relation avec le transport des personnes.

L'architecture du jeu d'instructions est l'ensemble des règles et des instructions que le CPU peut exécuter.

<h2 id="memory">Les Hubs de Mémoire : Comprendre la RAM et la ROM</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3.jpg)
_Photo par Valentine Tanasovich : https://www.pexels.com/photo/black-and-gray-computer-motherboard-2588757/_

[La RAM signifie Random Access Memory et peut être utilisée pour lire et écrire des données.](https://www.freecodecamp.org/news/how-to-access-and-read-ram-contents/)

Le CPU obtient les données de la mémoire de l'ordinateur vers la RAM d'abord pour éviter les longs temps d'attente.

Ensuite, il utilise les données de la RAM pour compléter les instructions.

Elles sont utilisées dans les ordinateurs et dans de nombreux dispositifs électroniques en raison de la volatilité de la mémoire. Cela signifie que les données ne sont présentes que lorsque l'ordinateur est allumé, ce qui en fait un stockage temporel idéal pendant que le dispositif fonctionne.

La ROM signifie Read Only Memory. Elle ne contient que des données ajoutées lors de la fabrication de l'ordinateur.

Elles sont largement utilisées dans le [firmware](https://www.freecodecamp.org/news/what-is-firmware/) des dispositifs, le BIOS et les petits systèmes embarqués.

C'est parce que la ROM est une mémoire non volatile. Cela signifie qu'elle reste en mémoire lorsque le dispositif est éteint, ce qui en fait un stockage permanent très important pour les données.

<h2 id="roadways">Les Voies de Données : Naviguer dans le Chemin de Données du CPU</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/4.png)
_Photo par Rogeer Marques : https://www.pexels.com/photo/close-up-shot-of-a-chip-processor-11272008/_

Le chemin de données du CPU est un circuit numérique complexe avec de nombreux composants qui travaillent ensemble, tels que :

* **Unité Arithmétique et Logique (ALU) :** Effectue des opérations arithmétiques et logiques à l'intérieur de la partie données du CPU.
* **Registres :** Petits emplacements de stockage rapides pour les données temporaires récupérées de la RAM.
* **Bus :** Les bus de données, de contrôle et d'adresse sont des fils utilisés à l'intérieur du chemin de données du CPU pour transférer des informations.

Bien que les CPU aient beaucoup changé depuis l'Intel 8008, ce sont quelques-uns des composants qui servent encore de fondation pour tous les CPU.

Grâce à eux, il est possible de laisser les données circuler, mais pas de contrôler le flux réel. C'est le travail de l'unité de contrôle dans le CPU, créée dans l'Intel 8008 sous forme de machines à états.

<h2 id="traffic">Contrôleurs de Trafic : Le Rôle des Machines à États dans les CPU</h2>

[Une machine à états est un système qui passe par différents états afin d'effectuer des tâches.](https://www.freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66/)

Elles sont composées d'un certain nombre d'états et de transitions. Elles ont été utilisées dans l'Intel 8008 pour créer l'unité de contrôle en raison de sa structure et de sa manière efficace de gérer la séquence d'opérations nécessaires pour traiter les instructions.

Chacun des états peut activer un ou plusieurs composants du CPU pour traiter une certaine instruction en langage d'assemblage.

De cette façon, certaines parties du chemin de données du CPU sont activées pour qu'une instruction soit complétée.

De plus, grâce à ces machines à états, le CPU est complet et peut effectuer toutes les instructions qu'un utilisateur souhaite dans une boucle continue appelée le cycle fetch-execute.

<h2 id="fetch">Routines Quotidiennes : Le Cycle Fetch-Execute Expliqué</h2>

La machine à états dans le CPU contrôle comment le chemin de données du CPU fonctionne ensemble pour effectuer une instruction donnée.

De nos jours, chaque ordinateur reçoit des millions d'instructions par seconde. De cette façon, les machines à états agissent comme une boucle pour obtenir les instructions et les exécuter.

Ce processus est connu sous le nom de cycle fetch-execute, où le CPU récupère et exécute les instructions :

* **Fetch :** Le CPU récupère l'instruction de la mémoire.
* **Decode :** L'instruction récupérée est décodée pour déterminer l'action requise.
* **Execute :** L'instruction décodée est exécutée en utilisant les composants appropriés du CPU.
* **Write-back :** Le résultat de l'exécution est écrit en mémoire ou dans un registre.

Dans l'étape de fetch, l'unité de contrôle dit à la RAM de donner l'instruction suivante au CPU.

Dans l'étape de décodage, le CPU interprète l'instruction, et dans l'étape d'exécution, il effectue l'opération. Ensuite, l'étape de write-back garantit que le résultat est stocké correctement.

Ce cycle continue tant que le PC est allumé. De cette façon, dans les processeurs modernes, en traitant des milliards d'instructions par seconde.

### Mais Qu'en est-il des Données du Clavier ou de la Souris ?

Ces données ne proviennent pas de la RAM mais sont gérées par un mécanisme appelé interruptions. Pendant que le CPU exécute des instructions, il peut détecter lorsque des données proviennent de périphériques.

Si cela se produit, le CPU arrête sa tâche actuelle et priorise les instructions des périphériques. Ensuite, le CPU reprend ses tâches précédentes.

Il existe de nombreuses façons de gérer les interruptions, parmi les plus populaires :

1. **Interruptions par Polling :** Le CPU vérifie périodiquement si une interruption s'est produite.
2. **Interruptions Vectorielles :** Le dispositif interrupteur dirige le CPU vers la routine de service d'interruption appropriée.
3. **Interruptions Prioritaires :** Les interruptions sont assignées à différents niveaux de priorité, garantissant que les tâches critiques sont traitées en premier.

De cette façon, avec ces mécanismes, le CPU maintient ses performances tout en interagissant avec les périphériques.

<h2 id="instruction">Le Règlement : Décoder l'Architecture du Jeu d'Instructions (ISA)</h2>

Avec l'unité de contrôle, le CPU complet et la RAM, il est possible d'effectuer de nombreuses instructions.

Mais quelles instructions peuvent être effectuées sur un CPU donné ? Et combien ? C'est ce que l'Architecture du Jeu d'Instructions (ISA) résout.

L'ISA définit un ensemble d'instructions qu'un certain CPU peut exécuter. C'est ce qui permet aux programmeurs de comprendre ce qu'un processeur peut et ne peut pas faire sans avoir à comprendre tout le matériel de logique numérique à l'intérieur.

De cette façon, il agit comme une interface entre le logiciel et le matériel.

**Aspects Clés de l'ISA :**

* **Types d'Instructions :** Inclut les instructions arithmétiques, logiques, de contrôle et de transfert de données.
* **Modes d'Adressage :** Méthodes pour spécifier les opérandes des instructions.
* **Registres :** L'ensemble des registres disponibles pour être utilisés par les instructions.

**ISA Courantes :**

* **x86 :** Largement utilisé dans les processeurs de bureau et de serveur.
* **ARM :** Dominant dans les dispositifs mobiles et embarqués grâce à son efficacité énergétique.
* **RISC-V :** Un standard ouvert d'ISA conçu pour une large gamme d'applications.

Chaque CPU a souvent sa propre version de l'architecture du jeu d'instructions. Et l'architecture du jeu d'instructions est très souvent définie avec les langages de programmation d'assemblage.

C'est pourquoi il existe tant de [versions](https://www.freecodecamp.org/news/what-are-assembly-languages/) du langage de programmation d'assemblage.

Puisque chaque CPU a ses propres spécifications matérielles, chacun aura des composants similaires à ceux des autres CPU et, ainsi, des langages de programmation d'assemblage associés similaires.

Le choix de l'ISA impacte la conception du CPU, ses performances et sa compatibilité avec le logiciel.

Par exemple, la complexité de x86 permet des applications de bureau puissantes, tandis que la simplicité d'ARM favorise les dispositifs mobiles écoénergétiques.

<h2 id="programming">Des Langages de Programmation au Code Machine</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3-1.jpg)
_Photo par luis gomes : https://www.pexels.com/photo/close-up-photo-of-programming-of-codes-546819/_

Bien que chaque processeur ait son propre langage d'assemblage, gérer le code en langage d'assemblage et écrire du code en langage d'assemblage pour créer de grands programmes peut être complexe.

C'est très compliqué, et peut conduire à perdre du temps à corriger des choses et des détails au lieu de, de manière plus rapide et plus facile, gérer le développement d'un programme et le développer réellement.

Pour résoudre ce problème, de nombreux langages de programmation ont été créés à partir de l'assemblage. Nous écrivons le code dans les langages de programmation, et il est ensuite converti en langage d'assemblage.

De cette façon, au lieu de passer du temps sur des détails, il est possible de se concentrer sur des choses plus importantes comme le développement du système et la conception d'algorithmes.

C'est le processus par lequel la plupart des langages de programmation convertissent leur code en langage d'assemblage :

1. Convertir le code en code d'assemblage via un compilateur ou un interpréteur.
2. Le code d'assemblage est ensuite converti en code machine brut et exécuté par le CPU.
3. Une boucle spécifique dans la machine à états du CPU est complétée.
4. Ensuite, le CPU récupère et exécute l'instruction suivante.

Regardons deux exemples de langages de programmation faisant cela !

### Langage de Programmation C

Le langage de programmation C a été créé à partir de l'assemblage au début des années 1970. Il a été créé pour fournir un langage de plus haut niveau pour une programmation système efficace qui permet également la manipulation du matériel.

Avec un compilateur, le code C est converti en langage d'assemblage puis traité par le CPU complet.

Grâce à cette conversion, en écrivant des programmes en langage de programmation C, nous pouvons résoudre de nombreux problèmes de manière plus efficace, tels que :

* Erreurs de gestion de la mémoire
* Débordements de tampon
* Problèmes d'optimisation manuelle

De nos jours, même pour des tâches plus simples, le code d'assemblage converti à partir du compilateur C est beaucoup plus efficace et fiable qu'un humain écrivant le code d'assemblage.

Si vous souhaitez en savoir plus sur le compilateur C, vous pouvez consulter :

%[https://www.freecodecamp.org/news/what-is-a-compiler-in-c/]

### Langage de Programmation Python

Le langage de programmation Python a été créé à partir de C à la fin des années 1980.

Son objectif était de fournir un langage de programmation de haut niveau, convivial, qui met l'accent sur la lisibilité et la simplicité, permettant un développement rapide d'applications.

En Python, un interpréteur convertit le code Python en bytecode ligne par ligne.

Et ce bytecode est converti en code machine dans le CPU et traité dans le cycle fetch-execute.

De cette façon, il est possible pour les gens de programmer de manière plus facile et de se concentrer sur des programmes plus grands, tels que :

* Modèles d'intelligence artificielle
* Applications web
* Analyse de données
* Calcul scientifique

Cependant, le défi avec les CPU dans tous les langages de programmation est qu'il traite les données de manière séquentielle.

<h2 id="problems">Défis Urbains : Résoudre les Problèmes de CPU</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/4-1.jpg)
_Photo par Peng LIU : https://www.pexels.com/photo/timelapse-photography-of-vehicle-on-concrete-road-near-in-high-rise-building-during-nighttime-169677/_

Le CPU traditionnel monocœur traite les données de manière séquentielle, instruction après instruction. Cela devient une limitation si nous avons de nombreuses instructions à traiter.

C'est ce que les GPU (Graphics Processing Units) sont venus résoudre. Grâce aux GPU, nous pouvons traiter les instructions en parallèle, réduisant ainsi considérablement le temps de calcul.

Avec ces capacités de traitement parallèle, il est possible d'atteindre un calcul beaucoup plus rapide et une efficacité améliorée dans une large gamme d'applications.

<h2 id="conclusion">Conclusion : Meilleure Unité de Contrôle et Parties de Données</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/5.jpg)
_Photo par Miguel Á. Padriñán : https://www.pexels.com/photo/green-circuit-board-343457/_

En plus des CPU modernes étant multicœurs, les avancées dans les unités de contrôle et les chemins de données jouent un rôle crucial dans l'amélioration des performances du processeur.

Les unités de contrôle sont souvent conçues en utilisant la microprogrammation ou des unités de contrôle câblées.

La microprogrammation offre une plus grande flexibilité et des mises à jour plus faciles de la logique de contrôle, tandis que les unités de contrôle câblées fournissent des performances plus rapides en implémentant directement les signaux de contrôle.

Une autre avancée significative est l'exploration de nouveaux matériaux pour les transistors dans les portes logiques.

Au lieu de dépendre uniquement du silicium, les chercheurs étudient des matériaux alternatifs pour créer des processeurs plus rapides et plus efficaces.

Alors que la technologie continue de progresser, comprendre ces concepts fondamentaux restera essentiel pour les passionnés et les professionnels du domaine.

Rester à jour avec ces développements garantit l'innovation et l'amélioration continues de la conception et de la fonctionnalité des CPU.