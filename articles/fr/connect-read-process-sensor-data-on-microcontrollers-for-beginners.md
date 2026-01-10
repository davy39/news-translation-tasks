---
title: Comment connecter, lire et traiter les données de capteurs sur les microcontrôleurs
  – Un guide pour débutants
subtitle: ''
author: Soham Banerjee
co_authors: []
series: null
date: '2025-03-14T16:30:15.622Z'
originalURL: https://freecodecamp.org/news/connect-read-process-sensor-data-on-microcontrollers-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741902732575/fd41a2d5-ed4f-445d-b186-936625837c8d.png
tags:
- name: embedded systems
  slug: embedded-systems
- name: microcontroller
  slug: microcontroller
- name: embedded software
  slug: embedded-software
- name: ADC
  slug: adc
- name: I2C
  slug: i2c
- name: real-time data processing
  slug: real-time-data-processing
- name: Signal Processing
  slug: signal-processing
- name: sensors
  slug: sensors
- name: Electronics
  slug: electronics
- name: hardware
  slug: hardware
- name: electrical engineering
  slug: electrical-engineering
- name: software architecture
  slug: software-architecture
- name: MathJax
  slug: mathjax
seo_title: Comment connecter, lire et traiter les données de capteurs sur les microcontrôleurs
  – Un guide pour débutants
seo_desc: 'In today’s world, computers are ubiquitous and generally serve two primary
  purposes.

  The first is general-purpose computing, where they handle a wide range of tasks,
  including running diverse applications and programs. Examples include laptops, deskt...'
---

Dans le monde d'aujourd'hui, les ordinateurs sont omniprésents et servent généralement deux objectifs principaux.

Le premier est le calcul généraliste, où ils gèrent une large gamme de tâches, y compris l'exécution d'applications et de programmes divers. Les exemples incluent les ordinateurs portables, les ordinateurs de bureau, les serveurs et les supercalculateurs.

Le second concerne les systèmes embarqués, qui sont des ordinateurs spécialisés conçus pour des fonctions spécifiques. On les trouve couramment dans des appareils tels que les thermostats, les réfrigérateurs, les voitures et autres appareils intelligents, qui s'appuient sur des capteurs pour collecter des données environnementales et exécuter leurs tâches efficacement.

### **Le rôle des capteurs**

Les capteurs jouent un rôle critique dans les deux types de calcul. Dans les systèmes embarqués, les capteurs recueillent des données environnementales pour aider des appareils comme les véhicules autonomes, les appareils domestiques et les machines industrielles à accomplir leurs tâches. Dans les ordinateurs généralistes, les capteurs surveillent principalement les conditions internes telles que la température et la tension, assurant un fonctionnement sûr et prévenant des problèmes comme la surchauffe ou les défauts électriques.

À mesure que l'intelligence artificielle (IA) et l'Internet des objets (IoT) évoluent, les capteurs sont devenus indispensables pour recueillir des données du monde réel afin de soutenir la prise de décision intelligente. Les systèmes embarqués exploitent les capteurs pour percevoir leur environnement, transformant les données brutes en informations exploitables qui alimentent l'automatisation et améliorent l'efficacité dans divers secteurs.

Cela signifie que la compréhension de l'interfaçage des capteurs et la conception de logiciels robustes pilotés par des capteurs sont devenues des compétences vitales pour les ingénieurs et les amateurs.

Que vous soyez débutant ou ingénieur expérimenté, ce guide vous aidera à construire une compréhension solide des logiciels d'interfaçage de capteurs.

## **Ce que vous apprendrez et le champ de l'article**

Dans cet article, vous apprendrez comment connecter des capteurs à des microcontrôleurs (MCU) et concevoir des pipelines logiciels pour capteurs qui transforment les données brutes en informations significatives et utilisables. Vous explorerez également des techniques pratiques pour traiter les données des capteurs avec précision et efficacité dans les systèmes embarqués.

Voici un aperçu de ce que nous couvrirons :

* Qu'est-ce qu'un capteur et comment fonctionne-t-il – Une introduction aux capteurs, aux types courants et à la manière dont les pipelines de capteurs aident à traiter les données des capteurs.

* Caractéristiques clés des capteurs – Paramètres importants comme la sensibilité, la précision, la justesse, la plage, la dérive et le temps de réponse pour vous aider à choisir le bon capteur pour votre projet.

* Comment interfacer des capteurs avec des microcontrôleurs – Connexions matérielles et protocoles de communication comme SPI, I²C et GPIO qui permettent aux microcontrôleurs de lire les données des capteurs.

* Architecture logicielle pour les données des capteurs – Un aperçu de haut niveau du pipeline logiciel qui traite les données des capteurs, y compris les pilotes, le support ADC, la mise à l'échelle, l'étalonnage et le post-traitement.

* Conception détaillée des composants du pipeline – Un examen plus approfondi de chaque étape du pipeline, en se concentrant sur la mise à l'échelle des données brutes, l'étalonnage des capteurs et l'application de filtres pour nettoyer les signaux bruyants.

* Conseils pratiques pour la gestion de l'alimentation – Bonnes pratiques pour gérer l'alimentation efficacement en utilisant des modes basse consommation, des tampons FIFO et DMA lors de la manipulation de données de capteurs dans les systèmes embarqués.

À la fin de cet article, vous saurez comment concevoir et implémenter un pipeline complet de données de capteurs pour un système embarqué, depuis la lecture des données brutes des capteurs jusqu'à leur préparation pour une utilisation dans des appareils intelligents et connectés.

**Remarque** : Le traitement avancé des données, les ADC haute résolution et la conception de circuits matériels pour les capteurs ne sont pas abordés dans cet article.

## **Prérequis**

Pour tirer le meilleur parti de cet article, vous devriez avoir :

1. Des connaissances de base sur les microcontrôleurs : Compréhension des périphériques courants comme les ADC (Converters Analogique-Numérique), SPI (Interface Périphérique Sérielle), I2C (Circuit Inter-Intégré) et GPIO (Entrée/Sortie à Usage Général). Si vous êtes nouveau dans ces protocoles, [cet article offre un excellent aperçu](https://www.parlezvoustech.com/en/comparaison-protocoles-communication-i2c-spi-uart/).

2. Des connaissances de base en électronique : Familiarité avec les circuits et les signaux, y compris les interfaces analogiques et numériques.

3. Programmation en C : Expérience en développement de logiciels embarqués, y compris le développement de pilotes.

4. (Optionnel) Des connaissances de base sur les capteurs : Comprendre les différents types de capteurs (comme la température, la pression, le mouvement) est utile mais non requis.

De plus, cet article suppose ce qui suit :

* Vous travaillez avec un microcontrôleur équipé des périphériques nécessaires pour l'intégration des capteurs. Les détails des périphériques des microcontrôleurs peuvent être trouvés dans un [manuel de référence, par exemple pour un STM32F4](https://pdf.xab3.ro/manual/reference-manual-for-stm32f405415-stm32f407417-stm32f427437-and-stm32f429439-mcus-100).

* Vous êtes familier avec les compilateurs, les débogueurs et les IDE utilisés dans les systèmes embarqués. Voici quelques outils courants :

  * Compilateurs : [GCC](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads), [Clang](https://developer.arm.com/documentation/dui0773/l/Introducing-the-Toolchain/Toolchain-overview?lang=en),

  * Débogueurs : [GDB](https://sourceware.org/gdb/), [LLDB](https://lldb.llvm.org/use/tutorial.html)

  * IDE : [Visual Studio Code](https://code.visualstudio.com) (VSCode) est un choix populaire, notamment avec des extensions pour le développement et le débogage embarqués.

* Vous visez à construire des systèmes embarqués fiables et pilotés par des capteurs, capables de collecter et de traiter efficacement des données du monde réel.

## Table des matières

* [Qu'est-ce qu'un capteur et un pipeline de capteur ?](#heading-questce-quun-capteur-et-un-pipeline-de-capteur)

* [Caractéristiques des capteurs](#heading-caracteristiques-des-capteurs)

* [Comment interfacer avec un microcontrôleur](#heading-comment-interfacer-avec-un-microcontroleur)

* [Architecture logicielle](#heading-architecture-logicielle)

  * [Aperçu de haut niveau des composants](#heading-aperçu-de-haut-niveau-des-composants)

  * [Accès aux données du capteur](#heading-acces-aux-donnees-du-capteur)

  * [Gestion de l'alimentation du capteur](#heading-gestion-de-lalimentation-du-capteur)

* [Conception détaillée des composants](#heading-conception-detaillée-des-composants)

  * [1. Pilote de capteur](#heading-1-pilote-de-capteur)

  * [2. Support ADC](#heading-2-support-adc)

  * [3. Mise à l'échelle](#heading-3-mise-a-lechelle)

  * [4. Étalonnage](#heading-4-etalonnage)

  * [5. Post-traitement des données](#heading-5-post-traitement-des-donnees)

* [Conclusion](#heading-conclusion)

## **Qu'est-ce qu'un capteur et un pipeline de capteur ?**

Un capteur détecte les changements dans les propriétés physiques telles que la température, la pression ou la lumière et les convertit en signaux électriques qui peuvent être mesurés ou interprétés. Par exemple, une thermistance est un type de résistance dont la résistance change avec la température. À mesure que la température varie, la résistance de la thermistance change, modifiant la tension à ses bornes. Le système interprète ensuite ce changement de tension pour déterminer la température.

Pour mieux comprendre les capteurs, considérons les capteurs naturels du corps humain : les yeux, les oreilles, la peau, le nez et la langue. Ces capteurs naturels envoient constamment des signaux sur l'environnement au cerveau pour traitement. Différentes régions du cerveau interprètent ces signaux et utilisent les informations pour déclencher des actions et des réponses. Tout comme le cerveau traite les signaux des capteurs naturels, un microcontrôleur traite les signaux des capteurs électroniques en utilisant un pipeline de capteur.

Les capteurs existent en de nombreux types, chacun conçu pour détecter des propriétés physiques spécifiques. Certains capteurs ont un élément de détection qui change ses propriétés en réponse à des conditions comme la chaleur, la lumière ou la pression. Les exemples incluent les thermistances, les récepteurs infrarouges et les photodiodes.

Pour détecter le mouvement, comme l'accélération et la rotation, les capteurs MEMS (Systèmes Microélectromécaniques) – comme les accéléromètres et les gyroscopes – sont largement utilisés.

Pour mesurer la distance, des capteurs comme les sonars, les capteurs ultrasoniques et les radars sont courants. Ce ne sont là que quelques exemples des nombreux types de capteurs disponibles.

Au-delà des types de propriétés physiques qu'ils détectent, les capteurs diffèrent également par leurs niveaux d'intégration. Certains capteurs sont des capteurs bruts, composés uniquement d'un élément de détection et d'un transducteur avec des fils simples pour une connexion directe à un circuit externe.

D'autres, connus sous le nom de capteurs intelligents, incluent des composants supplémentaires tels qu'un ADC (convertisseur analogique-numérique) et des capacités de traitement embarqué, leur permettant de gérer davantage du traitement des données de manière indépendante.

Le choix entre un capteur brut et un capteur intelligent dépend des exigences de votre application, y compris des facteurs comme le coût, la taille et la charge de traitement sur le microcontrôleur d'interface.

Revenons à notre analogie humaine, considérons comment la vision fonctionne comme un pipeline de capteur. Lorsque la lumière entre dans nos yeux, les cellules photoréceptrices (bâtonnets et cônes) de la rétine agissent comme des éléments de détection, convertissant la lumière en signaux électriques. Ces signaux voyagent via le nerf optique jusqu'au cortex visuel du cerveau, où ils subissent un traitement pour former une image reconnaissable. Le cerveau interprète ensuite ces informations et initie une réponse, comme sourire lorsque vous voyez un beau paysage.

De manière similaire, un pipeline de capteur pour un système embarqué peut être défini comme montré dans l'image ci-dessous :

![Figure 1 : Un pipeline de capteur montrant la conversion analogique-numérique, l'étalonnage, le filtrage, puis le traitement.](https://cdn.hashnode.com/res/hashnode/image/upload/v1738828676916/75137176-c9ba-432d-bf44-bb3da093e18d.png align="center")

Chacune de ces étapes peut avoir des exigences différentes en fonction de l'application. Créer un document d'exigences pour le capteur est utile lors de la sélection du capteur approprié et de la configuration du pipeline.

## **Caractéristiques des capteurs**

Avant de plonger dans les blocs du pipeline de capteur, examinons quelques caractéristiques importantes d'un capteur.

### **Sensibilité**

La sensibilité est la capacité d'un capteur à détecter de petits changements dans la propriété physique qu'il est conçu pour mesurer.

La sensibilité peut varier en fonction de facteurs comme les processus de fabrication, le coût et la conception de l'élément de détection.

Les capteurs conçus pour une propriété spécifique sont souvent disponibles en différents niveaux de sensibilité, permettant aux utilisateurs de sélectionner une sensibilité appropriée en fonction des exigences de l'application.

### **Précision**

La précision est le degré auquel la mesure d'un capteur correspond à la valeur réelle de la propriété physique qu'il mesure. Tester la précision d'un capteur nécessite généralement de comparer ses lectures à celles d'un instrument de référence.

Un capteur peut avoir des erreurs de gain et de décalage – des problèmes que l'étalonnage peut aider à corriger. L'étalonnage ajuste ces erreurs systématiques, souvent dues aux tolérances de fabrication ou aux facteurs de conception.

Une fois étalonné, la sortie du capteur peut être vérifiée par rapport à une référence pour confirmer sa précision. Le niveau de précision requis doit être déterminé en fonction des besoins de l'application.

### **Justesse**

La justesse fait référence à la cohérence ou à la répétabilité des mesures d'un capteur, indépendamment de la proximité de ces mesures par rapport à la valeur réelle. Elle indique la capacité du capteur à produire la même sortie dans des conditions identiques et la finesse avec laquelle il peut résoudre et rapporter des valeurs.

Par exemple, si la température réelle d'un objet est de 12,53°C :

* Un capteur précis mesurera de manière cohérente des valeurs comme 12,52°C, 12,53°C ou 12,54°C, même si ces valeurs sont légèrement décalées par rapport à la température réelle.

* Un capteur très précis, en revanche, mesurera des valeurs proches de 12,53°C mais peut manquer de justesse si ces lectures varient largement (par exemple, 12,50°C, 12,53°C et 12,56°C).

Pour les applications nécessitant des mesures exactes, un capteur avec une haute précision (proximité de la valeur réelle) et une haute justesse (faible variabilité) est essentiel. Cela est particulièrement important pour distinguer de petites différences, comme entre 12,5°C et 12,53°C.

En revanche, les applications avec des exigences moins strictes peuvent utiliser des capteurs avec des tolérances plus larges, telles que ±1°C, qui sont suffisantes pour des fins de surveillance générale.

### **Plage**

La plage d'un capteur fait référence à l'étendue entre les valeurs maximale et minimale de la propriété physique qu'il peut mesurer tout en maintenant sa précision et sa justesse spécifiées. La plage de fonctionnement d'un capteur peut s'étendre au-delà de sa plage de mesure, mais la plage de mesure définit les limites dans lesquelles le capteur adhère de manière fiable à sa sensibilité, sa précision et son temps de réponse spécifiés.

### **Dérive**

La dérive se produit lorsque la sortie d'un capteur change au fil du temps en raison de conditions comme la température ou l'humidité. Les composants à l'intérieur du capteur, y compris l'élément de détection, peuvent être sensibles à ces conditions, entraînant des décalages progressifs dans les mesures.

Par exemple, de nombreux composants sont affectés par les changements de température et d'humidité, ce qui peut altérer les lectures des capteurs. De plus, les capteurs avec des oscillateurs internes peuvent subir une dérive basée sur le temps, impactant la précision.

Un étalonnage régulier avec une référence externe précise (comme une horloge précise) peut aider à corriger la dérive et à maintenir des mesures fiables. Pour certaines applications, la sélection d'un capteur avec des caractéristiques de dérive acceptables est cruciale.

### **Temps de réponse**

Le temps de réponse est la durée qu'un capteur prend pour détecter et refléter un changement dans la propriété physique mesurée. Par exemple, si la température augmente de 5°C, le temps de réponse indique combien de temps le capteur de température prend pour refléter ce changement dans sa sortie.

Le temps de réponse dépend de la conception du capteur, de la qualité de fabrication et des composants internes, tels que l'ADC (Converters Analogique-Numérique), les circuits de moyennage et les filtres dans le pipeline du capteur.

Tous les paramètres mentionnés ci-dessus sont documentés en détail dans la fiche technique du capteur. En pratique, il est judicieux de créer un document d'exigences pour le capteur pour chaque application spécifique, détaillant ces paramètres clés comme base pour la sélection du capteur.

Maintenant que vous avez examiné les caractéristiques clés des capteurs, explorons comment vous pouvez les connecter à un microcontrôleur pour des applications réelles.

## **Comment interfacer avec un microcontrôleur**

### Choix d'un protocole de communication

Un autre aspect essentiel des exigences des capteurs est la spécification de l'interface de communication entre le capteur et le MCU ou le processeur dans le système. Il est important de comprendre comment le capteur sera interfacé en fonction de son type de signal de sortie et des broches disponibles sur le microcontrôleur.

Par exemple, certains capteurs peuvent se connecter directement à une broche d'entrée analogique ou numérique sur un microcontrôleur. Un capteur brut, tel qu'un capteur de température, se connecte généralement à une broche d'entrée analogique, qui est ensuite lue par l'ADC (Converters Analogique-Numérique) interne du microcontrôleur.

En revanche, un capteur à sortie numérique se connecte à une broche GPIO (Entrée/Sortie à Usage Général) numérique. Par exemple, les capteurs de vitesse génèrent des ondes carrées avec des largeurs d'impulsion variables pour indiquer la vitesse. Ces signaux sont généralement connectés à une broche GPIO configurée comme une interruption externe ou une entrée de capture de temporisateur, permettant au microcontrôleur de mesurer la largeur d'impulsion avec précision.

Un capteur intelligent, en revanche, prend souvent en charge des protocoles de communication comme SPI (Interface Périphérique Sérielle) ou I2C (Circuit Inter-Intégré). Ces interfaces permettent au microcontrôleur de configurer le capteur, de vérifier son état et de récupérer des données par le biais de lectures et d'écritures de registres.

Le choix du protocole de communication approprié pour l'interface d'un capteur dépend des broches disponibles dans le système et des exigences spécifiques de l'application.

**Astuce** : Lors de l'utilisation de protocoles comme I²C ou SPI, l'utilisation d'outils tels que les analyseurs logiques [Saleae](https://www.saleae.com) peut grandement simplifier le débogage et la validation. Les analyseurs logiques capturent et visualisent les signaux de communication, et des outils comme Saleae offrent des interpréteurs de protocole intégrés pour vous aider à décoder la communication des capteurs en temps réel. Cela peut être particulièrement utile lors du dépannage des problèmes de configuration, des problèmes de synchronisation ou des erreurs de communication pendant l'interfaçage des capteurs.

La figure 2 ci-dessous montre un exemple de microcontrôleur connecté à 4 capteurs ayant différentes interfaces.

![Figure 2 : Un microcontrôleur interfacé avec différents capteurs utilisant différentes interfaces de communication.](https://cdn.hashnode.com/res/hashnode/image/upload/v1738828730915/25e62db6-a583-427a-bd77-c61c33990cdf.png align="center")

### Détermination des exigences de puissance

Les exigences de puissance sont une autre considération clé lors de l'interfaçage d'un capteur. Les capteurs peuvent fonctionner à différentes tensions (par exemple, 3,3 V ou 5 V), il est donc essentiel de s'assurer que le microcontrôleur peut accommoder ces niveaux. Les convertisseurs de niveau peuvent combler les écarts de tension, assurant la compatibilité entre les niveaux de tension du capteur et du microcontrôleur.

Les exigences de synchronisation et d'échantillonnage doivent également être évaluées, en particulier pour les capteurs générant des données à haute fréquence. La configuration d'interruptions externes sur les broches GPIO peut garantir une capture de données en temps opportun, tandis que des techniques comme l'utilisation de DMA peuvent rationaliser le transfert de données pour les capteurs échantillonnant à haute fréquence sans intervention du CPU.

Maintenant que vous avez appris les protocoles de communication et les connexions matérielles, concentrons-nous sur la conception de l'architecture logicielle qui acquiert, traite et prépare les données des capteurs pour une utilisation. La conception de logiciels efficaces est cruciale pour obtenir des données propres et fiables à partir du capteur.

## **Architecture logicielle**

Maintenant que nous avons choisi le capteur et le protocole de communication, concevons l'architecture logicielle pour le pipeline de capteur. Ce logiciel s'exécute sur le microcontrôleur connecté au capteur et traite les données brutes pour les rendre propres et utilisables.

Bien que le traitement des données au niveau de l'application soit hors du champ de cet article, concentrons-nous sur l'interface avec le capteur et la préparation des données pour une utilisation par l'application.

Le pipeline de traitement des capteurs peut être divisé en les composants suivants :

1. Pilote de capteur

2. Conversion Analogique-Numérique (ADC) Support

3. Mise à l'échelle

4. Étalonnage

5. Post-traitement des données

Examinons un aperçu de haut niveau de ces composants pour les capteurs intelligents et bruts.

### **Aperçu de haut niveau des composants**

1. **Pilote de capteur**

   1. Capteurs intelligents : Le pilote configure le capteur, gère l'alimentation et gère les opérations de lecture et d'écriture des registres du capteur via un protocole de communication comme SPI, I2C.

   2. Capteurs bruts : Le pilote peut uniquement contrôler les GPIOs pour la gestion de l'alimentation, car les capteurs bruts manquent généralement de registres.

2. **Support de conversion analogique-numérique (ADC)**

   1. Capteurs intelligents : Incluent un ADC embarqué, qui est configuré via le pilote du capteur.

   2. Capteurs bruts : Nécessitent un ADC externe, un pilote ADC implémenté en logiciel pour configurer l'ADC, initier les conversions et récupérer les données.

3. **Mise à l'échelle** : La mise à l'échelle est nécessaire pour les capteurs intelligents et bruts. Elle convertit les comptes numériques après la conversion analogique-numérique en quantités physiques significatives en utilisant des formules fournies dans la fiche technique du capteur. Par exemple, un capteur de température utilisera une formule pour convertir les comptes numériques en degrés Celsius.

4. **Étalonnage** : Une fois la quantité physique mesurée obtenue, l'étalonnage ajuste la valeur en appliquant des décalages, des gains ou les deux pour corriger les erreurs. Ce processus garantit que la sortie du capteur s'aligne avec les valeurs de référence sur toute sa plage de mesure. Une discussion détaillée du processus d'étalonnage suivra dans la section suivante.

5. **Post-traitement des données** : Des techniques de post-traitement, telles que le filtrage, sont appliquées pour améliorer la qualité des données et réduire le bruit. Des filtres courants tels que les filtres passe-bas ou passe-haut peuvent éliminer les composantes de fréquence indésirables.

### **Accès aux données du capteur**

La méthode d'accès aux données dépend du fait qu'il s'agisse d'un capteur brut ou d'un capteur intelligent. Les capteurs intelligents auront des ADC et des FIFO embarqués. Avant de se plonger dans la manière dont les données sont accessibles, il est important de comprendre d'abord la fréquence d'échantillonnage.

#### Fréquence d'échantillonnage :

La fréquence de prise de mesure à partir du capteur doit suivre le [théorème d'échantillonnage de Nyquist-Shannon](https://www.allaboutcircuits.com/technical-articles/nyquist-shannon-theorem-understanding-sampled-systems/). Il stipule que le taux d'échantillonnage doit être deux fois la composante de fréquence la plus élevée du signal à mesurer pour reconstruire avec précision les données mesurées.

La fréquence d'échantillonnage définit la fréquence à laquelle le capteur capture les données, ce qui affecte la manière dont les données sont accessibles. Selon que le capteur est un capteur brut ou un capteur intelligent, l'approche pour gérer ces données échantillonnées varie.

**Capteurs intelligents :**

1. Registre de données : Le capteur écrit les données échantillonnées directement dans un registre en fonction de la fréquence d'échantillonnage définie, mise à jour lors de la configuration. Le microcontrôleur lit ce registre de données en fonction d'une interruption de fin de conversion des données.

2. Tampon FIFO : Certains capteurs incluent des tampons FIFO (First-In, First-Out) pour stocker plusieurs points de données. Lorsqu'ils sont activés, les FIFO se mettent à jour à la fréquence d'échantillonnage configurée et déclenchent des interruptions lorsqu'ils deviennent pleins ou atteignent un niveau prédéterminé. Les avantages des FIFO incluent :

   1. Efficacité énergétique : Le MCU peut traiter les données par lots, réduisant la charge du CPU et lui permettant d'entrer en mode basse consommation pendant la collecte des données.

   2. Correspondance des taux d'échantillonnage et de traitement : Les tampons FIFO aident à concilier les différences entre le taux d'échantillonnage du capteur et le taux de traitement des données du MCU.

   3. Pour les MCU avec Accès Direct à la Mémoire (DMA), le transfert de données du capteur vers la mémoire du MCU peut se produire sans intervention du CPU, réduisant davantage la consommation d'énergie.

**Capteurs bruts :**

Pour les capteurs bruts, le MCU déclenche les conversions ADC à la fréquence d'échantillonnage, souvent en utilisant une interruption de temporisateur. Les données sont lues lors de l'interruption de fin de conversion de l'ADC, permettant au MCU de dormir pendant les conversions et entre les échantillons pour économiser de l'énergie.

### **Gestion de l'alimentation du capteur**

La gestion de l'alimentation est cruciale pour les applications sensibles à l'énergie. Les stratégies incluent :

1. Modes basse consommation : De nombreux capteurs supportent des modes basse consommation configurables via les registres du capteur.

2. Cyclage de l'alimentation contrôlé par GPIO (Duty-Cycling) : Pour les capteurs sans modes basse consommation intégrés, le microcontrôleur peut basculer la ligne d'alimentation du capteur en utilisant une broche GPIO, réduisant davantage la consommation d'énergie. La figure 3 ci-dessous montre le diagramme d'un capteur de température brut dont l'alimentation est contrôlée en utilisant un GPIO du MCU. Par exemple, un capteur de température en mode veille peut être activé uniquement lorsque des lectures de température sont requises.

![Figure 3 : Interfaçage d'un capteur de température brut avec un MCU](https://cdn.hashnode.com/res/hashnode/image/upload/v1739042040654/1f2d4bbd-f15a-417a-9c79-3b93384e95bd.png align="center")

Les techniques ci-dessus assurent une utilisation efficace de l'énergie tout en maintenant le taux d'échantillonnage des données requis et la réactivité du capteur.

Avec l'architecture de haut niveau en tête, nous allons maintenant plonger dans la conception détaillée de chaque composant du pipeline.

## **Conception détaillée des composants**

Dans cette section, vous allez approfondir les composants clés du pipeline de capteur décrits dans la section Architecture logicielle.

### **1. Pilote de capteur**

Le pilote de capteur est responsable de la gestion de la communication, de la configuration, de l'alimentation et de l'acquisition des données pour les capteurs intelligents et bruts.

#### Pilote de capteur intelligent :

1. Pilote de communication : Les pilotes I2C ou SPI génériques sur le MCU peuvent être adaptés en utilisant des fonctions d'enveloppement pour gérer les exigences spécifiques du capteur, telles que les transferts de 1, 2 ou 4 octets.

2. Configuration : Les tâches typiques incluent la définition du taux d'échantillonnage, la configuration des interruptions, la gestion des tampons FIFO et, si nécessaire, les paramètres d'horloge.

3. Gestion de l'alimentation : Les API doivent permettre aux couches logicielles supérieures de faire passer les capteurs entre les modes d'alimentation en écrivant dans des registres spécifiques ou en contrôlant les lignes GPIO pour les capteurs sans modes d'alimentation intégrés.

#### Pilote de capteur brut :

Pour les capteurs bruts, le pilote gère principalement l'alimentation, souvent par basculement contrôlé par GPIO.

### **2. Support ADC**

Le support ADC est requis uniquement pour les capteurs bruts. Dans cet article, nous nous concentrons sur les ADC SAR, qui sont couramment intégrés dans les microcontrôleurs.

#### Comment fonctionnent les ADC SAR ?

Un ADC SAR convertit un signal analogique en une valeur numérique sur plusieurs cycles d'horloge, le nombre de cycles étant égal à sa résolution en bits (par exemple, 10 cycles pour un ADC 10 bits).

#### Termes clés liés aux ADC :

1. Tension de référence (VRef) : Représente la tension maximale que l'ADC peut mesurer. Les signaux analogiques dépassant cette limite doivent être mis à l'échelle.

2. Résolution : Détermine le plus petit changement de tension détectable. Par exemple, un ADC 10 bits avec une VRef de 3,3 V a une résolution de 3,22 mV

$$V_{\text{Res}} = V_{\text{Ref}} /2^{10}$$

Le résultat de l'ADC est stocké dans un registre de données, qui peut ensuite être mis à l'échelle en unités physiques significatives.

### **3. Mise à l'échelle**

La mise à l'échelle convertit les comptes ADC en valeurs physiques significatives, telles que la température (°C) ou l'accélération (g) en fonction du type de capteur. Les fiches techniques des capteurs fournissent généralement les formules ou tables de consultation nécessaires.

Par exemple, la méthode pour convertir une tension mesurée par un capteur de température brut en valeur de température est montrée ci-dessous :

$$V_{\text{Measured}} = Counts_{\text{ADC}} / 2^{10} * V_{\text{Ref}} \quad \text{(Obtenir V_Measured à partir des comptes ADC)}$$

$$Temperature_{\text{Measured}} = V_{\text{Measured}} * T_{\text{C/mV}} \quad \text{(Obtenir la valeur physique de la température)}$$

De même, un accéléromètre à 3 axes mappe les comptes sur les axes X, Y et Z aux valeurs d'accélération en g ou milli-g.

### **4. Étalonnage**

![Figure 4a : Étalonnage avec gain et décalage | Figure 4b : Étalonnage avec décalage fixe](https://cdn.hashnode.com/res/hashnode/image/upload/v1738829686302/bfa643dc-5e01-4b24-b885-b682acdb11cb.png align="center")

La figure ci-dessus à gauche (4a) montre l'étalonnage avec gain et décalage, tandis que la figure ci-dessus à droite (4b) montre l'étalonnage avec décalage fixe.

$$x_{\text{calibrated}} = Gain * x_{\text{raw}} + Offset \quad \text{(Figure 4a - Étalonnage linéaire)}$$

$$x_{\text{calibrated}} = x_{\text{raw}} + Offset \quad \text{(Figure 4b - Étalonnage à décalage fixe)}$$

L'étalonnage garantit que la sortie du capteur s'aligne avec les mesures de référence, corrigeant les erreurs introduites par la conception, les matériaux ou la fabrication.

#### Types d'erreurs :

1. Erreur de décalage : Un écart constant de la sortie du capteur par rapport à la valeur de référence réelle, indépendamment de l'amplitude de l'entrée.

2. Erreur de gain : Une erreur proportionnelle où l'échelle de sortie du capteur s'écarte de la valeur attendue, provoquant une augmentation ou une diminution incorrecte de la sortie par rapport à l'entrée.

#### Méthodes d'étalonnage :

1. Étalonnage à 2/3 points : Ce type d'étalonnage peut impliquer soit l'application d'un décalage fixe à la valeur brute, soit l'application à la fois du gain et du décalage. La figure 4a illustre un exemple d'étalonnage de gain/décalage, tandis que la figure 4b représente l'étalonnage de décalage. Dans les deux figures, l'axe des y représente la valeur de référence mesurée par un instrument précis, tandis que l'axe des x représente la valeur brute mesurée par le capteur après l'ADC.

2. Étalonnage à N points : Implique plusieurs points pour une correction d'erreur plus complexe et non linéaire.

#### Implémentation :

1. Les points d'étalonnage doivent couvrir toute la plage de mesure du capteur pour une précision optimale.

2. Les paramètres tels que le gain et le décalage, une fois estimés, doivent être stockés dans une mémoire non volatile du système pour une persistance à travers les cycles d'alimentation.

### **5. Post-traitement des données**

Le post-traitement abordé dans cette section concerne l'élimination du bruit et des composantes de signal indésirables, ce qui améliore la fiabilité des données.

#### Filtrage

Le filtrage est le processus d'élimination des composantes de fréquence indésirables d'un signal pour améliorer la qualité des données. Il existe plusieurs types de filtres différents :

* Filtres passe-bas : Permettent aux signaux basse fréquence de passer tout en atténuant le bruit haute fréquence.

* Filtres passe-haut : Permettent aux signaux haute fréquence de passer tout en atténuant le bruit basse fréquence. (par exemple, l'accélération gravitationnelle dans les données de l'accéléromètre).

* Filtres passe-bande : Conservent uniquement les signaux dans une plage de fréquences spécifique, éliminant à la fois les fréquences inférieures et supérieures en dehors de la bande souhaitée.

Ces filtres sont souvent implémentés sous forme de filtres FIR (Réponse Impulsionnelle Finie) ou IIR (Réponse Impulsionnelle Infinie). Les filtres IIR sont faciles à implémenter et efficaces sur le plan computationnel, tandis que les filtres FIR sont intensifs en calcul mais offrent un meilleur contrôle sur la réponse en fréquence.

Ici, nous allons explorer un filtre passe-bas simple connu sous le nom de Moyenne Mobile Exponentielle (EMA), un type de filtre IIR. Un filtre de moyenne mobile est une technique mathématique qui lisse les fluctuations à court terme tout en mettant en évidence les tendances à long terme.

Contrairement aux autres filtres de moyenne mobile, l'EMA ne nécessite pas de maintenir un tampon, ce qui la rend plus efficace en mémoire. Elle est également plus réactive aux changements de données tout en fournissant un lissage, ce qui la rend bien adaptée au filtrage en temps réel. L'EMA attribue un poids plus important aux échantillons de données récents qu'aux plus anciens, lui permettant de s'adapter rapidement aux changements dans les lectures des capteurs.

L'EMA peut être calculée comme suit :

$$EMA_{\text{t}} = \alpha * x_{\text{t}} + (1 - \alpha) * EMA_{\text{t - 1}}$$

$$\alpha = 2 / (N + 1) \quad \text{(Facteur de lissage, N - taille de la fenêtre du filtre)}$$

$$EMA_{\text{t}} \quad \text{(Moyenne Mobile Exponentielle à l'itération actuelle)}$$

$$x_{\text{t}} \quad \text{(Nouvel échantillon de données à l'itération actuelle)}$$

$$EMA_{\text{t - 1}} \quad \text{(Moyenne Mobile Exponentielle à la dernière itération)}$$

Maintenant que nous comprenons la Moyenne Mobile Exponentielle (EMA), voici deux facteurs clés à considérer lors de son réglage pour une application :

* Lissage vs. Réactivité : Un facteur de lissage plus élevé (plus proche de 1, taille de fenêtre de filtre plus petite) donne plus de poids aux données récentes, rendant le filtre plus réactif aux changements mais moins efficace pour la réduction du bruit. Un facteur de lissage plus faible (plus proche de 0, taille de fenêtre de filtre plus grande) offre une meilleure réduction du bruit mais réagit plus lentement aux changements de données.

* Réglage spécifique à l'application : Le facteur de lissage doit être choisi en fonction du taux d'échantillonnage, de la sensibilité du capteur et des exigences de l'application. Les systèmes en temps réel nécessitent souvent un équilibre entre une réactivité rapide et une sortie stable.

Voici un exemple de code pour l'EMA :

```c
#include <stdio.h>
#include <stdint.h>

// Implémentation du filtre Moyenne Mobile Exponentielle (EMA)
#define FILTER_WINDOW 5

// Fonction pour calculer l'EMA
float calculateEMA(float ema, float new_value, float alpha) {
    return (alpha * new_value) + (1 - alpha) * ema;
}

int main() {
    float sensorReadings[] = {26.0, 27.5, 28.2, 27.0, 26.8, 26.5, 27.2};
    int numReadings = sizeof(sensorReadings) / sizeof(sensorReadings[0]);

    float alpha = 2.0f / (FILTER_WINDOW + 1); // Formule standard EMA
    float ema = sensorReadings[0];  // Initialiser EMA avec la première lecture

    printf("Données du capteur filtrées par EMA:\n");

    for (int i = 0; i < numReadings; i++) {
        ema = calculateEMA(ema, sensorReadings[i], alpha);
        printf("Lecture %d: Brute = %.2f, EMA = %.2f\n", i + 1, sensorReadings[i], ema);
    }

    return 0;
}
```

## **Conclusion**

En résumé, les capteurs sont la colonne vertébrale des appareils intelligents modernes, comblant le fossé entre le monde physique et les systèmes numériques. Des appareils électroniques grand public à l'automatisation industrielle et aux dispositifs médicaux, ils permettent aux appareils de percevoir et d'interagir avec leur environnement.

Comprendre le fonctionnement des capteurs, les composants de leur pipeline de données et leur intégration avec les microcontrôleurs est essentiel pour les ingénieurs et les amateurs. En concevant des pipelines efficaces, les développeurs peuvent garantir des données précises, propres et fiables, permettant aux systèmes de répondre aux objectifs de performance et d'efficacité énergétique.

Si vous avez des questions ou souhaitez discuter davantage de ce sujet, n'hésitez pas à me contacter sur [Twitter](https://x.com/sohamstars) ou [Lin](https://x.com/sohamstars)[kedIn](https://www.linkedin.com/in/sohambanerjee2/). Toujours heureux de connecter.