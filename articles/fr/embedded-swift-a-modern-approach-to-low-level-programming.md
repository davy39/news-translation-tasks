---
title: 'Swift embarqué : une approche moderne de la programmation bas niveau'
subtitle: ''
author: Soham Banerjee
co_authors: []
series: null
date: '2025-08-02T00:45:59.467Z'
originalURL: https://freecodecamp.org/news/embedded-swift-a-modern-approach-to-low-level-programming
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754090186842/80a42dca-f2c4-49de-b704-2e90134c6397.png
tags:
- name: embedded systems
  slug: embedded-systems
- name: Firmware Development
  slug: firmware-development
- name: Swift
  slug: swift
- name: C
  slug: c
- name: C++
  slug: cpp
- name: Programming Blogs
  slug: programming-blogs
- name: software development
  slug: software-development
- name: memory-management
  slug: memory-management
- name: programming languages
  slug: programming-languages
seo_title: 'Swift embarqué : une approche moderne de la programmation bas niveau'
seo_desc: Embedded programming has long been dominated by C and C++, powering everything
  from microcontrollers to real-time systems. While these languages offer unmatched
  low-level control, they also introduce persistent challenges, manual memory management,
  u...
---

La programmation embarquée a longtemps été dominée par les langages C et C++, alimentant tout, des microcontrôleurs aux systèmes temps réel. Bien que ces langages offrent un contrôle bas niveau inégalé, ils introduisent également des défis persistants, tels que la gestion manuelle de la mémoire, les opérations de pointeurs non sécurisées et les bugs logiques subtils découlant de systèmes de types faibles et de comportements indéfinis.

Avec la sortie de Swift 6 et son nouveau mode de compilation Embedded Swift, les développeurs ont désormais accès à une alternative moderne, sécurisée en mémoire et performante, spécialement conçue pour les systèmes à ressources limitées.

Bien que des langages comme Rust aient également émergé pour répondre à ces problèmes, Embedded Swift apporte la clarté et la sécurité de Swift aux environnements de microcontrôleurs, sans sacrifier le déterminisme, la taille binaire ou l'accès matériel.

Cet article présente Embedded Swift et explore comment il se compare au développement traditionnel en C/C++. Nous aborderons ses principales caractéristiques, les modèles de programmation et de mémoire, comment configurer la chaîne d'outils pour les microcontrôleurs STM32, et comment lier Swift avec les pilotes C existants.

En cours de route, nous examinerons les compromis de performance, le soutien croissant de l'écosystème, et le mouvement plus large de l'industrie vers les langages sécurisés en mémoire. Comme je l'espère, vous verrez que Swift est un concurrent sérieux dans l'avenir du développement embarqué.

## Prérequis

Pour tirer le meilleur parti de cet article, vous devez avoir une compréhension de base de la programmation en Swift et en C. La familiarité avec les plateformes matérielles embarquées et les concepts de développement de micrologiciels sera également utile.

Si vous êtes nouveau dans les systèmes embarqués, envisagez de consulter ce [guide d'introduction au micrologiciel embarqué](https://www.freecodecamp.org/news/learn-embedded-systems-firmware-basics-handbook-for-devs/) pour acquérir des connaissances fondamentales avant de plonger dans Embedded Swift.

## Portée

Cet article est destiné à servir d'introduction pratique à Embedded Swift. Il couvre :

* Un aperçu d'Embedded Swift et de ses principales caractéristiques linguistiques

* Le modèle de programmation et de mémoire de Swift dans un contexte embarqué

* La configuration de la chaîne d'outils Embedded Swift sur macOS pour les microcontrôleurs STM32

* L'interopérabilité avec le code C et la liaison avec les pilotes bas niveau existants

* Un aperçu de la mémoire et des performances au niveau des instructions

* Les orientations futures et les cas d'utilisation pour Embedded Swift

Notez que cet article ne fournit pas un tutoriel complet sur le langage Swift lui-même. Bien que l'accent principal soit mis sur STM32, des principes similaires s'appliquent à d'autres plateformes prises en charge telles que ESP32, Raspberry Pi Pico et nRF52.

## Table des matières :

* [Qu'est-ce que Swift ? Qu'est-ce que Embedded Swift ?](#heading-qu-est-ce-que-swift-qu-est-ce-que-embedded-swift)

* [Modèle de programmation Swift](#heading-modele-de-programmation-swift)

* [Gestion de la mémoire Swift](#heading-gestion-de-la-memoire-swift)

* [Comparaison de la mémoire et du cycle d'instructions](#heading-comparaison-de-la-memoire-et-du-cycle-d-instructions)

* [Comment configurer Embedded Swift](#heading-comment-configurer-embedded-swift)

* [Liaisons C-Swift :](#heading-liaisons-c-swift)

* [Travail futur](#heading-travail-futur)

* [Conclusion](#heading-conclusion)

## Qu'est-ce que Swift ? Qu'est-ce que Embedded Swift ?

Swift est un langage de programmation moderne développé par Apple qui combine la performance des langages compilés avec l'expressivité et la sécurité de la conception des langages modernes. Bien que Swift ait été initialement créé pour le développement iOS et macOS, il a évolué pour devenir un langage polyvalent puissant utilisé dans le développement côté serveur, la programmation système, et de plus en plus, les systèmes embarqués.

Embedded Swift est un mode de compilation spécial introduit dans Swift 6 qui apporte les avantages de Swift aux plateformes à ressources limitées comme les microcontrôleurs. Il permet aux développeurs d'utiliser un langage sûr et de haut niveau tout en produisant des binaires compacts, déterministes et performants adaptés aux applications embarquées.

### Caractéristiques clés de Swift

Embedded Swift conserve de nombreuses caractéristiques puissantes du langage qui font de Swift une alternative attrayante à C/C++ dans le développement embarqué :

**Sécurité des types** : Swift utilise un système de types statiques fort, qui prévient de nombreuses erreurs de programmation au moment de la compilation. Contrairement à C, où les incompatibilités de types peuvent entraîner un comportement indéfini, Swift garantit que tous les types sont utilisés correctement avant même que le code ne s'exécute.

**Vérification stricte des types** : Swift n'autorise pas les conversions de types implicites qui pourraient entraîner une perte de données ou un comportement inattendu. Par exemple :

```swift
// Cela ne compilera pas en Swift
let integer: Int = 42
let decimal: Double = 3.14
let result = integer + decimal  // Erreur : Impossible de convertir la valeur de type 'Int' en type d'argument attendu 'Double'

// Vous devez être explicite sur les conversions
let result = Double(integer) + decimal  // Correct
```

**Types non-nullables par défaut** : En C, les pointeurs peuvent être nuls par défaut, ce qui introduit un risque. En Swift, les variables ne peuvent pas être nil sauf si elles sont explicitement marquées comme optionnelles :

```swift
var name: String = "John"
name = nil  // Erreur de compilation - String ne peut pas être nil

var optionalName: String? = "John"
optionalName = nil  // Cela est autorisé
```

#### Sécurité de la mémoire via ARC (détaillée plus tard) :

Swift gère la mémoire automatiquement en utilisant le comptage automatique des références (ARC). Contrairement à la gestion manuelle de la mémoire en C/C++, ARC gère les cycles de vie des objets efficacement sans pauses imprévisibles de collecte des déchets. Nous aborderons ARC et son impact dans les contextes embarqués dans une section dédiée plus tard.

**Syntaxe moderne** : 
La syntaxe de Swift est claire, cohérente et conçue pour la lisibilité. Elle supporte les paradigmes modernes incluant :

* Programmation fonctionnelle (map, filter, reduce)

* Génériques (abstractions sécurisées par les types)

* Programmation orientée protocole (discutée dans la section suivante)

Ces caractéristiques vous permettent d'écrire un code plus expressif et maintenable par rapport au C procédural ou au C++ lourd en héritage.

**Performance** : 
Swift est conçu pour performer au même niveau que C++ dans de nombreux scénarios. Des optimisations telles que l'inlining, l'élimination de code mort et le dispatch statique aident à garantir que les abstractions de haut niveau n'affectent pas les performances. En mode embarqué, Swift désactive des fonctionnalités comme la réflexion à l'exécution et le dispatch dynamique pour réduire davantage les frais généraux.

Pour tirer pleinement parti de Swift pour le développement embarqué, il est important de comprendre son modèle de programmation. Contrairement à l'approche procédurale de C ou à la conception lourde en classes de C++, Swift promeut la programmation orientée protocole et la composition, ce qui offre à la fois flexibilité et sécurité dans la conception de systèmes embarqués.

## Modèle de programmation Swift

Swift adopte un modèle de programmation multi-paradigme qui mélange la programmation orientée objet, fonctionnelle et orientée protocole, le tout sous-tendu par une forte sécurité des types et de la mémoire.

Pour les développeurs embarqués venant de C ou C++, ce modèle peut sembler différent au début. Mais il offre une manière plus modulaire et testable de construire des systèmes complexes, quelque chose de particulièrement précieux dans les applications embarquées où l'abstraction matérielle et la fiabilité stricte sont cruciales.

### Programmation orientée protocole (POP)

Swift met l'accent sur les protocoles plutôt que sur l'héritage, encourageant les développeurs à définir des comportements par le biais de protocoles et à les implémenter en utilisant des types de valeur comme `struct` et `enum`, plutôt que de s'appuyer fortement sur les classes.

Cette philosophie favorise la composition plutôt que l'héritage, vous permettant de construire des fonctionnalités complexes en combinant des composants plus petits et bien définis.

**Concepts clés** :

* `protocol` définit le comportement requis.

* Les extensions de protocole fournissent un comportement par défaut.

* Préférer la sémantique de valeur en utilisant `struct`.

**Exemple** :

```swift
protocol Speakable {
    func speak()
}

extension Speakable {
    func speak() {
        print("Default sound")
    }
}

struct Dog: Speakable {
    func speak() {
        print("Woof!")
    }
}
```

Embedded Swift utilise des protocoles avec un dispatch statique. Avec le dispatch statique, le compilateur connaît l'adresse mémoire exacte de la fonction à appeler et peut générer une instruction de saut direct. Il n'y a pas de recherche à l'exécution, pas d'indirection, et pas d'incertitude.

#### Pourquoi POP est important pour les systèmes embarqués

Tout d'abord, vous obtenez une extraction matérielle flexible. Les protocoles facilitent la définition d'interfaces pour les composants matériels, permettant des implémentations simulées pendant les tests ou des variations spécifiques à la plateforme.

Deuxièmement, vous avez une faible surcharge. Embedded Swift utilise un dispatch statique pour les protocoles, ce qui signifie qu'il n'y a pas de recherche à l'exécution, et les appels sont résolus au moment de la compilation pour des performances maximales.

De plus, les types `struct` et `enum` évitent les allocations de tas, rendant le code plus efficace et prévisible dans les environnements à faible mémoire.

Maintenant que nous avons exploré comment le modèle de programmation de Swift permet un code embarqué plus sûr et plus modulaire, tournons-nous vers un autre élément critique du puzzle : la gestion de la mémoire. L'utilisation par Swift du comptage automatique des références (ARC) remplace la gestion manuelle de la mémoire et offre des avantages importants, ainsi que des compromis, pour les systèmes embarqués.

## Gestion de la mémoire Swift

L'une des fonctionnalités les plus impactantes de Swift, surtout dans le contexte des systèmes embarqués, est son utilisation du comptage automatique des références (ARC) pour la gestion de la mémoire. Contrairement à C/C++, où la mémoire doit être allouée et libérée manuellement en utilisant `malloc` et `free`, Swift automatise ce processus tout en maintenant des performances déterministes.

Cette automatisation réduit considérablement le risque de bugs courants liés à la mémoire comme les fuites, les pointeurs pendants ou les erreurs d'utilisation après libération, tous notoires dans le code C de bas niveau.

### Comment fonctionne ARC

Swift supporte ARC non seulement pour les API Cocoa Touch mais pour toutes les API, offrant une approche rationalisée de la gestion de la mémoire. Contrairement aux systèmes de collecte des déchets qui peuvent causer des pauses imprévisibles, ARC fonctionne de manière déterministe au moment de la compilation et de l'exécution pour gérer la mémoire.

ARC suit et gère automatiquement la durée de vie des objets en mémoire en fonction du nombre de références qui pointent vers eux.

* Comptage des références : Chaque objet a un compteur qui suit combien de références fortes pointent vers lui.

* Retain / Release : Le compilateur insère des appels `retain` et `release` automatiquement pendant l'assignation et la désinitialisation.

* Désallocation immédiate : Lorsque le compteur de références atteint zéro, l'objet est désalloué immédiatement.

* Déterministe : Contrairement aux collecteurs de déchets, ARC n'introduit pas de pauses imprévisibles ou de balayage à l'exécution.

Swift offre plusieurs types de références pour vous donner un contrôle précis sur le comportement de la mémoire et prévenir les cycles :

**Références fortes** (par défaut)

* Maintient l'objet référencé en vie.

* Utilisé dans la plupart des cas.

```swift
class MotorController {
    var sensor: SensorData?  // Référence forte
    
    func updateReading(newData: SensorData) {
        self.sensor = newData  // Les données du capteur précédentes sont automatiquement désallouées
    }
}
```

**Références faibles**

* Utilisées pour briser les cycles de référence (surtout dans les relations bidirectionnelles entre objets).

* Devient automatiquement `nil` lorsque l'objet référencé est désalloué.

```swift
class Device {
    var controller: MotorController?
    
    deinit {
        print("Device désalloué")
    }
}

class MotorController {
    weak var device: Device?  // ← Référence faible brise le cycle
    
    deinit {
        print("MotorController désalloué")
    }
}

func breakCycle() {
    let device = Device()
    let controller = MotorController()
    
    device.controller = controller
    controller.device = device  // ← Ceci est maintenant une référence faible
    
    // Lorsque cette fonction se termine, les deux objets sont correctement désalloués
}

breakCycle()
// Sortie :
// Device désalloué
// MotorController désalloué
```

**Références non-possédées**

* Version non optionnelle de `weak`.

* Suppose que l'objet ne sera jamais désalloué tant qu'il est encore utilisé.

* Plus léger que `weak`, mais non sécurisé si mal utilisé.

```swift
class SensorSystem {
    unowned let controller: MotorController  // référence non-possédée

    init(controller: MotorController) {
        self.controller = controller
    }
}

class MotorController {
    var sensorSystem: SensorSystem?

    func setupSensors() {
        sensorSystem = SensorSystem(controller: self)
    }

    deinit {
        print("MotorController désalloué")
    }
}

func testUnowned() {
    let controller = MotorController()
    controller.setupSensors()
    // sensorSystem se désalloue avant la fin de controller
}

testUnowned()
// Sortie : MotorController désalloué
```

### Surcoût d'ARC dans les systèmes embarqués

Bien qu'ARC offre des avantages en termes de sécurité, il introduit un certain surcoût par rapport à la gestion manuelle de la mémoire :

#### Surcoût de mémoire :

Les instances de classes gérées par ARC dans Swift incluent généralement 4 ou 8 octets supplémentaires pour stocker les métadonnées du compteur de références, selon l'architecture du système, 4 octets sur les systèmes 32 bits et 8 octets sur les systèmes 64 bits. Ces métadonnées permettent au runtime de suivre combien de références actives existent pour un objet donné et de le désallouer lorsqu'aucune référence ne reste. Lorsque les développeurs utilisent des références faibles ou non-possédées, l'empreinte mémoire augmente davantage. Ces références nécessitent des structures de données supplémentaires, telles que des tables latérales ou des mécanismes de suivi, pour gérer la vivacité des objets et le nettoyage. Dans le cas des références faibles spécifiquement, Swift maintient des tables de références faibles à zéro qui annulent automatiquement les pointeurs une fois que l'objet référencé est désalloué, garantissant ainsi la sécurité de la mémoire.

#### Surcoût du processeur :

ARC introduit un certain surcoût d'exécution en raison des opérations de retain et de release, qui sont insérées automatiquement lors des affectations de références. Ces opérations impliquent l'incrémentation ou la décrémentation du compteur de références et sont particulièrement courantes dans le code qui passe des objets entre fonctions ou les stocke dans des collections. Pour garantir la sécurité des threads, ces mises à jour sont généralement implémentées à l'aide d'opérations atomiques, ce qui ajoute davantage de cycles d'instructions. Dans les graphes d'objets complexes, ARC peut également s'engager dans la détection de cycles et le nettoyage à l'aide de références faibles pour prévenir les fuites de mémoire causées par des cycles de références fortes. Bien que l'ARC de Swift fournisse une gestion de la mémoire déterministe et efficace, il le fait avec des coûts de mémoire et de processeur que les développeurs doivent considérer attentivement, en particulier dans les systèmes embarqués critiques pour la performance.

### Sécurité des types et prévention des erreurs

Le système de types de Swift prévient de nombreuses erreurs courantes qui affligent les programmes C/C++ :

* **Débordements de tampon** : Les tableaux Swift sont vérifiés en limites, empêchant les vulnérabilités de débordement de tampon qui sont courantes en C.

* **Déréférencements de pointeurs nuls** : Les types optionnels de Swift rendent les déréférencements de pointeurs nuls impossibles au moment de la compilation.

* **Utilisation après libération** : Le modèle de propriété de Swift prévient les erreurs d'utilisation après libération qui peuvent causer des plantages ou des vulnérabilités de sécurité.

Maintenant que nous avons couvert le modèle de mémoire de Swift et le comportement d'ARC, explorons comment il se compare à C en termes d'utilisation de la mémoire et de cycles d'instructions, un aspect crucial lors de l'évaluation d'Embedded Swift pour un déploiement dans le monde réel.

## Comparaison de la mémoire et du cycle d'instructions

Comprendre les caractéristiques de performance de Swift par rapport à C est essentiel pour les systèmes embarqués, où chaque cycle d'instruction et chaque octet de mémoire compte. Bien que Swift apporte des avantages comme la sécurité et l'expressivité, ces bénéfices s'accompagnent de certains compromis en termes d'utilisation de la mémoire et de comportement d'exécution que les développeurs embarqués doivent évaluer soigneusement.

### Gestion de la mémoire :

Swift utilise le comptage automatique des références (ARC) pour gérer la mémoire. ARC suit le nombre de références à chaque objet et le désalloue lorsqu'aucune référence ne reste. Cela élimine le besoin d'appels explicites `free()` mais introduit une surcharge.

C, en revanche, utilise la gestion manuelle de la mémoire. Les développeurs allouent la mémoire en utilisant `malloc` et la libèrent en utilisant `free`, ou s'appuient sur la pile pour la plupart des données de courte durée.

Le tableau ci-dessous fournit la comparaison de la gestion de la mémoire entre Swift et C :

| **Fonctionnalité** | **Swift (ARC)** | **C (Manuel)** |
| --- | --- | --- |
| Stratégie de mémoire | Comptage automatique des références | Manuel avec `malloc`/`free` |
| Surcoût par objet | 4–8 octets (pour le compteur de références) | Aucun pour la pile ; variable pour le tas |
| Désallocation | Déterministe, déclenchée par ARC | Contrôlée par le développeur |
| Support des références faibles | Nécessite des métadonnées supplémentaires | Non intégré |
| Sécurité des threads | Opérations atomiques dans ARC | Non garanti |
| Contrôle de la disposition | Limité, géré par le compilateur | Contrôle complet (via structs/pointeurs) |

Swift garantit la sécurité grâce à un nettoyage déterministe et une utilisation prévisible de la mémoire. Mais cela se fait au prix d'une surcharge de mémoire et de CPU.

L'approche de C offre un contrôle complet sur la disposition de la mémoire et un coût d'exécution minimal, mais augmente le risque de fuites de mémoire et de fragmentation sans pratiques disciplinées.

### Analyse des cycles d'instruction

Les fonctionnalités de sécurité dans Swift, telles que la vérification des limites, le déballage des optionnels et les mises à jour d'ARC, se traduisent par des instructions CPU supplémentaires. Bien que cela puisse impacter les performances, le compilateur Swift est agressif en matière d'optimisation dans les builds de release. Par exemple, l'inlining et l'élision d'ARC peuvent éliminer une grande partie de la surcharge dans les chemins critiques pour les performances.

C n'a pas de vérifications de sécurité intégrées, lui permettant de générer un code efficace et prévisible. Les développeurs peuvent même utiliser l'assemblage en ligne pour un contrôle serré des performances.

Le tableau ci-dessous fournit la comparaison des cycles d'instruction entre Swift et C :

| **Fonctionnalité au niveau des instructions** | **Swift** | **C** |
| --- | --- | --- |
| Mises à jour du compteur de références | 2–4 instructions par assignation | N/A |
| Vérification des limites | 1–3 instructions par accès au tableau | Aucune |
| Déballage des optionnels | 1–2 instructions par vérification | N/A |
| Dispatch des méthodes | Les protocoles introduisent une indirection | Appels directs ou pointeurs de fonction |
| Potentiel d'optimisation | Élision d'ARC, inlining, élimination de code mort | Contrôle manuel complet, assemblage en ligne |
| Prédictibilité | Élevée dans les builds optimisées, avec une certaine surcharge d'abstraction | Très élevée, abstraction minimale |

Bien que Swift insère des instructions supplémentaires pour la sécurité, une grande partie de ce coût peut être atténuée par l'optimisation du compilateur.

C n'a pas de telles fonctionnalités par défaut, ce qui en fait un choix idéal pour les applications où les performances doivent être étroitement contrôlées et où le développeur est prêt à assumer la pleine responsabilité de la sécurité.

### Comparaison du nombre d'instructions : Performance de boucle Swift vs C

Lors de l'évaluation de Swift et C pour une utilisation embarquée, il est utile d'analyser les performances au niveau des instructions sur des opérations de base, telles qu'une boucle qui traite un tableau de nombres à virgule flottante. Cela nous donne une idée concrète du coût computationnel des fonctionnalités de sécurité et d'abstraction de chaque langage.

Considérons un exemple simple : la somme d'un tableau de valeurs `Float` et le retour de la moyenne. En Swift, le code utilise une boucle `for-in` de haut niveau sur un tableau :

Performance de boucle simple :

```swift
// Boucle Swift avec vérifications de sécurité
func processData(_ data: [Float]) -> Float {
    var sum: Float = 0.0
    for value in data {  // Itérateur avec vérification des limites
        sum += value     // Arithmétique sécurisée
    }
    return sum / Float(data.count)  // Division sécurisée
}
// Estimé : ~8-10 instructions par itération
```

Bien qu'élégant et sûr, cette boucle inclut plusieurs mécanismes de sécurité :

1. Vérification des limites à chaque accès au tableau

2. Comptage des références si `data` est passé comme un type de référence

3. Protection contre le débordement en mode debug

4. Gestion des optionnels ou vérifications à l'exécution si `data` pourrait être vide

Ces vérifications introduisent une surcharge à l'exécution, résultant en un estimé de 8 à 10 instructions par itération sur la plupart des plateformes (selon le niveau d'optimisation et l'architecture cible). Dans les builds de release, Swift optimise agressivement et supprime les vérifications redondantes, mais un certain niveau de coût d'abstraction reste, surtout par rapport à l'accès direct à la mémoire en C.

Maintenant, comparez cela à son équivalent en C :

```c
// Boucle C sans vérifications de sécurité
float process_data(float* data, int count) {
    float sum = 0.0f;
    for (int i = 0; i < count; i++) {  // Arithmétique de pointeur directe
        sum += data[i];                // Accès direct à la mémoire
    }
    return sum / count;  // Division directe (aucune vérification de sécurité)
}
// Estimé : ~4-5 instructions par itération
```

Cette version effectue un accès direct à la mémoire avec l'arithmétique des pointeurs, sans vérification des limites, et sans sécurité des types. Le code C est de plus bas niveau, avec moins de vérifications à l'exécution, et se compile en seulement 4 à 5 instructions par itération, selon le CPU cible et les drapeaux du compilateur. Il est léger et rapide, idéal pour les scénarios critiques en termes de cycles par instruction.

Le tableau ci-dessous montre la comparaison des performances de boucle unique entre Swift et C :

| Aspect | Swift | C |
| --- | --- | --- |
| Accès au tableau | Vérifié en limites | Accès direct par pointeur |
| Itération de boucle | Abstraction d'itérateur de haut niveau | Boucle brute avec incrément de pointeur |
| Nombre d'instructions (par boucle) | ~8–10 (en debug), ~6–8 (en release) | ~4–5 |
| Division | Sécurisée (évite la division par zéro en dev) | Directe |
| Comportement en cas de débordement | Vérifié en debug, non vérifié en release | Non vérifié |
| Lisibilité et sécurité | Élevée | Faible |
| Performance | Plus faible (mais optimisable) | Plus élevée (manuelle) |

Maintenant que nous avons comparé Swift et C en termes de coûts de mémoire et de cycles, passons à l'aspect pratique : comment configurer Embedded Swift sur une plateforme STM32 et commencer le développement dans le monde réel.

## Comment configurer Embedded Swift

Dans cette section, nous allons passer en revue comment configurer et utiliser Embedded Swift pour le développement sur les microcontrôleurs STM32. STM32 est une famille populaire de microcontrôleurs basés sur ARM Cortex-M, couramment utilisés dans les applications industrielles, grand public et IoT.

### Prérequis

**Logiciels requis :**

* Instantané de développement Swift (inclut la chaîne d'outils Embedded Swift)

* Swiftly - La manière la plus simple de gérer et d'installer les chaînes d'outils Swift

* Swiftc - Outil de compilation en ligne de commande Swift

* Python3 - Requis pour exécuter des scripts de conversion de Mach-O en fichiers binaires

* Git (pour cloner des dépôts d'exemples) comme [https://github.com/swiftlang/swift-embedded-examples](https://github.com/swiftlang/swift-embedded-examples)

* Un environnement de développement de type Unix (macOS est actuellement le mieux supporté)

**Matériel cible :** Ce guide se concentre sur les microcontrôleurs STM32, qui sont largement utilisés dans les applications embarquées et bénéficient d'un excellent support communautaire.

Ce guide vous accompagne tout au long du processus de configuration, de l'installation de la chaîne d'outils Swift requise à la programmation du binaire final sur votre carte. Nous commencerons par installer l'instantané de développement Swift en utilisant Swiftly, un utilitaire simple en ligne de commande pour gérer les chaînes d'outils Swift. À partir de là, nous configurerons le système de construction, définirons la variante de carte correcte, personnaliserons le script de construction, et compilerons le code source Swift et C en un binaire. Enfin, nous programmerons le micrologiciel sur le STM32 en utilisant des outils standard.

### Installer l'instantané de développement Swift

La manière la plus simple d'installer et de gérer les chaînes d'outils Embedded Swift est d'utiliser l'outil swiftly, qui simplifie le téléchargement et l'utilisation des instantanés Swift.

#### Installation sur macOS :

Les étapes ci-dessous vous aideront à installer la chaîne d'outils Swift embarquée :

```bash
# Utilisation de Swiftly (Recommandé)
curl -O https://download.swift.org/swiftly/darwin/swiftly.pkg
installer -pkg swiftly.pkg -target CurrentUserHomeDirectory
~/.swiftly/bin/swiftly init --quiet-shell-followup
source "${SWIFTLY_HOME_DIR:-$HOME/.swiftly}/env.sh"

# Installer et utiliser l'instantané de développement
swiftly install main-snapshot
swiftly use main-snapshot

# Vérifier l'installation
swift --version
```

Vous pouvez cloner ce dépôt d'exemples GitHub :

```bash
git clone https://github.com/swiftlang/swift-embedded-examples.git 
cd swift-embedded-examples/projects/stm32-blink
```

Le stm32-blink contient :

* Code Swift qui bascule les GPIOs

* Un fichier de démarrage C avec une table de vecteurs

* Un script build.sh qui utilise swiftc, clang, et une configuration de linker personnalisée

### Configurer la carte STM32

Indiquez au script de construction quelle carte STM32 est utilisée :

```bash
export STM_BOARD=STM32F746G_DISCOVERY
```

Vous pouvez ajouter votre propre variante de carte en définissant la carte mémoire appropriée et les drapeaux du compilateur dans le script.

### Modifier build.sh (Optionnel)

Assurez-vous que le script localise correctement les éléments suivants :

* swiftc : doit pointer vers la chaîne d'outils que vous avez installée avec Swiftly

* clang : peut être le Clang par défaut de macOS

* libBuiltin.a, crt0.s, et macho2bin.py : utilisés pour fournir un support d'exécution minimal et convertir la sortie en binaires flashables

Si nécessaire, mettez à jour ces chemins :

```bash
SWIFT_EXEC=${SWIFT_EXEC:-$(swiftly which swiftc)}
CLANG_EXEC=${CLANG_EXEC:-$(xcrun -f clang)}
PYTHON_EXEC=${PYTHON_EXEC:-$(which python3)}
```

Assurez-vous que les drapeaux du linker correspondent aux tailles de flash et de RAM de votre cible.

### Construire et flasher le projet :

Exécutez :

```bash
./build.sh
```

Cela compile le code Swift et C, les lie, et produit un fichier blink.bin.

Si tout se passe bien, vous verrez :

```bash
.build/blink.bin  # prêt à flasher Étape 6 : Flasher le micrologiciel sur STM32
```

Utilisez les outils ST-Link ou openocd pour flasher votre carte. Exemple utilisant st-flash :

```bash
brew install stlink
st-flash write .build/blink.bin 0x8000000
```

Vous devriez maintenant voir une LED clignoter.

[Voici](https://docs.swift.org/embedded/documentation/embedded/stm32baremetalguide) une approche plus détaillée étape par étape pour écrire un code bare metal sur STM32. Pour des guides d'installation complets couvrant d'autres plateformes (Raspberry Pi Pico, ESP32, nRF52), une configuration détaillée de l'IDE, le dépannage et des exemples avancés, vous pouvez consulter la documentation officielle :

* Guide de configuration complet : [Installer Embedded Swift](https://docs.swift.org/embedded/documentation/embedded/installembeddedswift/)

* Exemples de plateformes : [Dépôt d'exemples Swift Embedded](https://github.com/apple/swift-embedded-examples)

* Didacticiel de démarrage : [Embedded Swift sur les microcontrôleurs](https://docs.swift.org/embedded/documentation/embedded)

Maintenant que nous avons configuré Embedded Swift et exploré comment construire et exécuter un projet d'exemple, examinons un scénario réel critique : l'interface de Swift avec les pilotes C de bas niveau.

## Liaisons C-Swift

Dans de nombreux projets embarqués, les pilotes matériels de bas niveau sont écrits en C en raison de son contrôle proche du matériel et de son large support d'écosystème. Embedded Swift supporte l'interopérabilité transparente avec C, ce qui vous permet de réutiliser les bibliothèques et pilotes C existants, d'écrire la logique de contrôle matériel en C, et d'implémenter la logique d'application de haut niveau en Swift.

Ce modèle hybride vous permet de combiner la sécurité et la productivité de Swift avec le contrôle matériel de bas niveau de C, sans surcharge d'exécution ou traduction d'objets.

Parcourons un exemple où un pilote de capteur de bas niveau est implémenté en C et la logique d'application est écrite en Swift.

### Fichier d'en-tête C (sensor_driver.h) :

Ce fichier d'en-tête C définit l'interface publique pour un pilote de capteur de bas niveau. Il inclut des types d'entiers à largeur fixe standard et déclare quatre fonctions :

* sensor_init() : Initialise le capteur matériel

* sensor_read_temperature() et sensor_read_humidity() : Lisent les valeurs brutes du capteur

* sensor_delay_ms() : Retarde l'exécution pour un nombre donné de millisecondes

Cette interface sert de pont entre Swift et C. Swift se liera à ces fonctions par leur nom, aucun wrapper ou binding n'est requis.

```c
#ifndef SENSOR_DRIVER_H
#define SENSOR_DRIVER_H

#include <stdint.h>

// Fonctions de pilote de capteur de bas niveau
void sensor_init(void);
uint32_t sensor_read_temperature(void);
uint32_t sensor_read_humidity(void);
void sensor_delay_ms(uint32_t milliseconds);

#endif
```

### Implémentation C (sensor_driver.c) :

Cette implémentation suppose que le capteur est mappé en mémoire à une adresse fixe (0x40001000). Chaque registre, température, humidité et contrôle, est accessible par décalage à partir de cette adresse de base.

La fonction sensor_init() écrit 0x01 dans le registre de contrôle, activant ou démarrant probablement le matériel du capteur.

Les méthodes sensor_read_temperature() et sensor_read_humidity() lisent à partir des registres mappés en mémoire et retournent les valeurs brutes de l'ADC du capteur.

La méthode sensor_delay_ms() effectue une boucle d'attente simple en utilisant des instructions nop (no-operation) pour approximer un délai. Cela est adapté pour des délais courts et grossiers dans des contextes bare-metal.

```c
#include "sensor_driver.h"

// Adresses des registres matériels
#define SENSOR_BASE_ADDR    0x40001000
#define TEMP_REG_OFFSET     0x00
#define HUMIDITY_REG_OFFSET 0x04
#define CONTROL_REG_OFFSET  0x08

void sensor_init(void) {
    // Initialiser le matériel du capteur
    volatile uint32_t* control_reg = (volatile uint32_t*)(SENSOR_BASE_ADDR + CONTROL_REG_OFFSET);
    *control_reg = 0x01; // Activer le capteur
}

uint32_t sensor_read_temperature(void) {
    volatile uint32_t* temp_reg = (volatile uint32_t*)(SENSOR_BASE_ADDR + TEMP_REG_OFFSET);
    return *temp_reg;
}

uint32_t sensor_read_humidity(void) {
    volatile uint32_t* humidity_reg = (volatile uint32_t*)(SENSOR_BASE_ADDR + HUMIDITY_REG_OFFSET);
    return *humidity_reg;
}

void sensor_delay_ms(uint32_t milliseconds) {
    // Implémentation simple du délai
    for (uint32_t i = 0; i < milliseconds * 1000; i++) {
        __asm__("nop");
    }
}
```

### Code Swift utilisant le pilote C :

Pour utiliser ces fonctions C à partir de Swift, vous les déclarez en utilisant @_silgen_name, qui indique au compilateur Swift de se lier directement à ces noms de symboles à l'exécution.

La classe SensorController encapsule la logique liée au capteur. Dans sa méthode init(), elle appelle la fonction sensor_init() définie en C pour initialiser le matériel du capteur.

La méthode readSensors() lit les valeurs brutes à partir du pilote C, les convertit en unités lisibles par l'homme en utilisant des fonctions d'assistance, les stocke en interne et retourne les valeurs traitées.

Les méthodes de conversion convertTemperature() et convertHumidity() appliquent une formule linéaire de base pour transformer les valeurs brutes de l'ADC en température en Celsius et en humidité en pourcentage, respectivement. Ces formules seraient basées sur la fiche technique spécifique du capteur.

La méthode checkThresholds() applique une logique de seuil simple, un bon exemple de l'endroit où la lisibilité et la sécurité des types de Swift brillent. Vous pourriez facilement étendre cette logique pour inclure des marges d'erreur, des machines à états ou des alertes.

```swift
// Importer les fonctions du pilote C

/*
Ces déclarations correspondent exactement aux signatures des fonctions C. 
Elles permettent à Swift d'invoquer les fonctions C comme si elles étaient des fonctions Swift natives 
— avec zéro surcharge.
*/
@_silgen_name("sensor_init")
func sensor_init()

@_silgen_name("sensor_read_temperature")
func sensor_read_temperature() -> UInt32

@_silgen_name("sensor_read_humidity")
func sensor_read_humidity() -> UInt32

@_silgen_name("sensor_delay_ms")
func sensor_delay_ms(_ ms: UInt32)

// Contrôleur de capteur Swift utilisant le pilote C
class SensorController {
    private var lastTemperature: Float = 0.0
    private var lastHumidity: Float = 0.0
    
    init() {
        // Initialiser le pilote C
        sensor_init()
    }
    
    func readSensors() -> (temperature: Float, humidity: Float) {
        // Lire les valeurs brutes à partir du pilote C
        let rawTemp = sensor_read_temperature()
        let rawHumidity = sensor_read_humidity()
        
        // Convertir les valeurs brutes en unités significatives en Swift
        let temperature = convertTemperature(rawValue: rawTemp)
        let humidity = convertHumidity(rawValue: rawHumidity)
        
        // Stocker pour comparaison
        lastTemperature = temperature
        lastHumidity = humidity
        
        return (temperature: temperature, humidity: humidity)
    }
    
    private func convertTemperature(rawValue: UInt32) -> Float {
        // Convertir la valeur brute de l'ADC en Celsius
        return (Float(rawValue) * 3.3 / 4095.0 - 0.5) * 100.0
    }
    
    private func convertHumidity(rawValue: UInt32) -> Float {
        // Convertir la valeur brute de l'ADC en pourcentage
        return Float(rawValue) * 100.0 / 4095.0
    }
    
    func checkThresholds() -> Bool {
        // Logique Swift pour la vérification des seuils
        let tempThreshold: Float = 25.0
        let humidityThreshold: Float = 60.0
        
        return lastTemperature > tempThreshold || lastHumidity > humidityThreshold
    }
}

// Boucle principale de l'application
func main() -> Never {
    let sensorController = SensorController()
    
    while true {
        // Lire les capteurs en utilisant le contrôleur Swift avec le pilote C
        let readings = sensorController.readSensors()
        
        // Traiter les données avec la sécurité des types et l'expressivité de Swift
        if sensorController.checkThresholds() {
            print("Avertissement : Température : \(readings.temperature)C, Humidité : \(readings.humidity)%")
        } else {
            print("Normal : Température : \(readings.temperature)C, Humidité : \(readings.humidity)%")
        }
        
        // Délai en utilisant la fonction du pilote C
        sensor_delay_ms(1000) // Délai de 1 seconde
    }
}
```

La fonction `func main()` est la boucle d'événements principale standard pour les systèmes embarqués. Elle crée le contrôleur de capteur, lit les données du capteur en boucle, vérifie les seuils et imprime les résultats en conséquence. La boucle inclut un délai (via le pilote C) pour éviter de saturer le capteur en continu.

Dans un contexte embarqué réel, au lieu d'utiliser `print()`, vous pourriez faire clignoter une LED, envoyer des messages UART ou journaliser des données en mémoire.

Avec Embedded Swift et C fonctionnant maintenant ensemble, explorons ce qui nous attend. La section suivante décrit les améliorations en cours, les cas d'utilisation émergents et les directions de recherche qui façonnent l'avenir d'Embedded Swift.

## Travail futur

Embedded Swift est encore une technologie jeune mais en rapide évolution. Ses fonctionnalités de langage modernes, sa sécurité de la mémoire et ses performances en font une option attrayante pour le développement embarqué, et les travaux en cours élargissent ses capacités, sa portée et son écosystème.

### Améliorations en cours

**Optimisations du compilateur** : L'équipe du compilateur Swift travaille activement à améliorer la génération de code pour les cibles embarquées, notamment :

* Réduction de la taille des binaires

* Minimisation de la surcharge d'ARC

* Amélioration des performances du dispatch statique

**Support matériel** : Embedded Swift peut cibler une grande variété de microcontrôleurs ARM et RISC-V, qui sont populaires pour la construction d'applications industrielles. Le support pour des architectures supplémentaires est en cours de développement.

**Améliorations des outils** : Le support des outils pour Embedded Swift est encore en évolution, mais plusieurs efforts communautaires et open-source rendent le développement plus accessible :

* **Systèmes de construction** : Le groupe de travail Swift Embedded fournit des projets d'exemple qui adaptent le gestionnaire de paquets Swift (SwiftPM) pour la compilation croisée. Des scripts de liaison personnalisés et des assistants de construction sont disponibles pour des plateformes comme STM32 et nRF52.

* **Support de débogage** : Les développeurs peuvent déboguer les programmes Embedded Swift en utilisant des outils existants comme GDB ou OpenOCD, à condition que la construction inclue des symboles de débogage appropriés. Bien que cela ne soit pas encore officiellement rationalisé, cette approche permet le débogage pas à pas sur du matériel réel.

* **Intégration IDE** : Il n'y a pas encore de support IDE officiel, mais certains développeurs utilisent VSCode avec la coloration syntaxique Swift et des tâches de construction externes. Ces configurations sont encore manuelles mais servent de prototypes précoces pour les flux de travail embarqués.

### Cas d'utilisation émergents

Il existe un certain nombre de cas d'utilisation émergents pour Embedded Swift. Par exemple, la sécurité de la mémoire de Swift, les garanties de type et la conception orientée protocole en font un choix idéal pour les appareils IoT sécurisés et évolutifs, en particulier là où les bugs de micrologiciel pourraient affecter la sécurité ou la vie privée des utilisateurs.

Le secteur automobile explore également Swift pour les systèmes d'infodivertissement, les fonctionnalités d'assistance à la conduite et la logique de sécurité critique (où l'exécution déterministe et la sécurité comptent).

La syntaxe expressive de Swift et sa sécurité à la compilation le rendent adapté à l'automatisation industrielle - pensez aux boucles de contrôle en temps réel, aux systèmes de fusion de capteurs et aux appareils de bord dans la fabrication intelligente.

Il est également utile pour les appareils médicaux, car il s'aligne bien avec les réglementations médicales strictes concernant la sécurité de la mémoire, les garanties de type et l'utilisation prévisible des ressources.

### Communauté et écosystème

#### Projets open source

Le groupe de travail Swift Embedded maintient des [dépôts d'exemples](https://github.com/swiftlang/swift-embedded-examples) montrant comment utiliser Embedded Swift sur des microcontrôleurs tels que STM32, nRF52 et ESP32. Des bibliothèques en phase initiale pour UART, GPIO et périphériques de base émergent, bien que l'écosystème soit encore jeune par rapport à C ou Rust.

#### Ressources d'apprentissage

Bien que [Embedded Swift](https://docs.swift.org/embedded/documentation/embedded) ne soit pas encore largement enseigné dans les programmes formels, les tutoriels communautaires et les projets exploratoires (par exemple, Swift pour Arduino) réduisent la barrière pour les amateurs et les apprenants indépendants. À mesure que les outils maturent, l'adoption éducative est susceptible de suivre.

#### Intérêt de l'industrie

Embedded Swift commence à attirer l'attention des développeurs et des entreprises à la recherche d'alternatives plus sûres et plus maintenables à C. Bien que l'adoption à grande échelle reste limitée, des cas d'utilisation comme le prototypage rapide, le développement IoT et l'expérimentation interne gagnent en traction.

## Conclusion

Embedded Swift représente une avancée majeure dans la programmation embarquée. En combinant la puissance et la sécurité de Swift avec le contrôle de bas niveau nécessaire pour les microcontrôleurs, il offre une alternative passionnante au développement traditionnel en C et C++.

Bien que C reste essentiel pour la programmation au niveau matériel et les chemins critiques pour les performances, Swift apporte des avantages convaincants à de nombreux scénarios embarqués :

* **Sécurité de la mémoire** : Swift élimine des catégories entières de bugs tels que les débordements de tampon, l'utilisation après libération et la déréférenciation de pointeurs nuls.

* **Sécurité des types** : De nombreuses erreurs logiques sont détectées au moment de la compilation, bien avant qu'elles ne puissent causer des échecs à l'exécution.

* **Fonctionnalités de langage modernes** : Les développeurs peuvent utiliser des paradigmes fonctionnels, des génériques et une conception orientée protocole même dans le code embarqué.

* **Interopérabilité avec C** : Swift fonctionne de manière transparente avec les bibliothèques C existantes, permettant une adoption progressive sans réécrire les pilotes de bas niveau.

* **Productivité des développeurs** : Une syntaxe claire, une gestion automatique de la mémoire et des outils puissants conduisent à un développement plus rapide et à une maintenance plus facile.

Les organismes gouvernementaux et réglementaires encouragent de plus en plus, voire imposent, l'utilisation de langages de programmation sécurisés en mémoire pour réduire les vulnérabilités dans les systèmes logiciels critiques. Par exemple :

* En 2022, la [**National Security Agency (NSA)**](https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF) des États-Unis a recommandé d'abandonner les langages non sécurisés comme C/C++ pour les nouveaux projets logiciels, en promouvant des alternatives sécurisées en mémoire.

* En juin 2025, la NSA et la CISA ont publié une fiche d'information conjointe sur la cybersécurité intitulée [Memory Safe Languages: Reducing Vulnerabilities in Modern Software Development](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4223298/nsa-and-cisa-release-csi-highlighting-importance-of-memory-safe-languages-in-so/), qui soulignait que les défauts de sécurité de la mémoire restent un risque persistant, et que les organisations devraient développer des stratégies pour adopter des langages de programmation sécurisés en mémoire dans les nouveaux systèmes.

* La [**Cybersecurity and Infrastructure Security Agency (CISA)**](https://www.trust-in-soft.com/resources/blogs/memory-safety-is-key-the-shift-in-u.s.-cyber-standards) et le [**NIST**](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf) des États-Unis ont émis des recommandations similaires dans le contexte de la cybersécurité nationale.

Bien que ces documents ne mentionnent pas explicitement Swift, le système de types fort de Swift, son modèle de mémoire basé sur ARC et ses garanties de sécurité à la compilation s'alignent étroitement sur les objectifs décrits dans ces recommandations. Ainsi, il offre une voie pratique et conviviale pour les développeurs vers un développement embarqué plus sûr.

Swift peut ne pas être adapté à tous les systèmes embarqués. Dans les applications où chaque octet de mémoire ou cycle d'instruction est critique, où les garanties en temps réel sont des exigences strictes, ou où la maturité de la chaîne d'outils est essentielle (par exemple, l'intégration RTOS, les analyseurs statiques), C ou Rust peuvent encore être préférés.

Mais dans de nombreuses applications embarquées modernes, en particulier celles impliquant le prototypage rapide, l'itération rapide des produits, les micrologiciels critiques pour la sécurité ou maintenables, et l'interopérabilité avec les bases de code C existantes, Swift offre une expérience de développement très productive et sûre.

Embedded Swift est encore en maturation, mais son élan est indéniable. Avec les travaux en cours sur le compilateur, les exemples pilotés par la communauté et l'intérêt croissant des développeurs, il est prêt à jouer un rôle majeur dans l'avenir des systèmes embarqués.

Que vous construisiez un appareil IoT, un équipement industriel ou un wearable de preuve de concept, Swift peut vous aider à écrire des micrologiciels plus sûrs et plus expressifs, sans sacrifier les performances ou le contrôle.

Swift peut être particulièrement puissant pendant la phase de prototypage, lorsque l'objectif principal est de valider rapidement et en toute sécurité la fonctionnalité. Et avec son support croissant pour plusieurs plateformes matérielles, il offre une base solide pour apporter des pratiques de développement logiciel modernes dans le monde embarqué.