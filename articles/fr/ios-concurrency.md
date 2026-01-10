---
title: 'La Concurrence Expliquée : Comment Construire une Application iOS Multithread'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-28T01:24:39.000Z'
originalURL: https://freecodecamp.org/news/ios-concurrency
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/onur-k-fHDVylCKLX0-unsplash-3.jpg
tags:
- name: concurrency
  slug: concurrency
- name: iOS
  slug: ios
seo_title: 'La Concurrence Expliquée : Comment Construire une Application iOS Multithread'
seo_desc: "By Besher Al Maleh\nConcurrency in iOS is a massive topic. So in this article\
  \ I want to zoom in on a sub-topic concerning queues and the Grand Central Dispatch\
  \ (GCD) framework. \nIn particular, I wish to explore the differences between serial\
  \ and concu..."
---

Par Besher Al Maleh

La concurrence dans iOS est un sujet vaste. Dans cet article, je souhaite me concentrer sur un sous-sujet concernant les files d'attente et le framework Grand Central Dispatch (GCD).

En particulier, je souhaite explorer les différences entre les files d'attente série et concurrentes, ainsi que les différences entre l'exécution synchrone et asynchrone.

Si vous n'avez jamais utilisé GCD auparavant, cet article est un excellent point de départ. Si vous avez déjà une certaine expérience avec GCD, mais que vous êtes toujours curieux à propos des sujets mentionnés ci-dessus, je pense que vous le trouverez toujours utile. Et j'espère que vous apprendrez une ou deux nouvelles choses en cours de route.

J'ai créé une application compagnon SwiftUI pour démontrer visuellement les concepts de cet article. L'application comprend également un petit quiz amusant que je vous encourage à essayer avant et après la lecture de cet article. [Téléchargez le code source ici](https://github.com/almaleh/Dispatcher), ou obtenez la [version bêta publique ici](https://testflight.apple.com/join/2tC0CKMO).

Je commencerai par une introduction à GCD, suivie d'une explication détaillée sur sync, async, serial et concurrent. Ensuite, je couvrirai quelques pièges lors de l'utilisation de la concurrence. Enfin, je terminerai par un résumé et quelques conseils généraux.

## Introduction

Commençons par une brève introduction à GCD et aux files d'attente de distribution. N'hésitez pas à passer à la section **Sync vs Async** si vous êtes déjà familier avec le sujet.

### Concurrence et Grand Central Dispatch

La concurrence vous permet de tirer parti du fait que votre appareil dispose de plusieurs cœurs CPU. Pour utiliser ces cœurs, vous devrez utiliser plusieurs threads. Cependant, les threads sont un outil de bas niveau, et la gestion manuelle des threads de manière efficace est extrêmement difficile.

[Grand Central Dispatch](https://developer.apple.com/documentation/DISPATCH) a été créé par Apple il y a plus de 10 ans comme une abstraction pour aider les développeurs à écrire du code multithread sans créer et gérer manuellement les threads eux-mêmes.

Avec GCD, Apple a adopté une [approche de conception asynchrone](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/ConcurrencyandApplicationDesign/ConcurrencyandApplicationDesign.html#//apple_ref/doc/uid/TP40008091-CH100-SW8) pour résoudre le problème. Au lieu de créer des threads directement, vous utilisez GCD pour planifier des tâches de travail, et le système exécutera ces tâches pour vous en faisant le meilleur usage de ses ressources. GCD gérera la création des threads nécessaires et planifiera vos tâches sur ces threads, transférant le fardeau de la gestion des threads du développeur au système.

Un grand avantage de GCD est que vous n'avez pas à vous soucier des ressources matérielles lorsque vous écrivez votre code concurrent. GCD gère un pool de threads pour vous, et il peut évoluer d'une Apple Watch monocœur à un MacBook Pro multicœur.

### Files d'attente de distribution

Ce sont les principaux éléments de construction de GCD qui vous permettent d'exécuter des blocs de code arbitraires en utilisant un ensemble de paramètres que vous définissez. Les tâches dans les files d'attente de distribution sont toujours démarrées dans un ordre premier entré, premier sorti (FIFO). Notez que j'ai dit _démarrées_, car le temps de completion de vos tâches dépend de plusieurs facteurs, et n'est pas garanti d'être FIFO (plus d'informations à ce sujet plus tard).

De manière générale, il existe trois types de files d'attente disponibles pour vous :

* La file d'attente de distribution principale (série, prédéfinie)
* Les files d'attente globales (concurrentes, prédéfinies)
* Les files d'attente privées (peuvent être série ou concurrentes, vous les créez)

Chaque application dispose d'une file d'attente principale, qui est une file d'attente _série_ exécutant des tâches sur le thread principal. Cette file d'attente est responsable du rendu de l'interface utilisateur de votre application et de la réponse aux interactions de l'utilisateur (toucher, défilement, panoramique, etc.). Si vous bloquez cette file d'attente trop longtemps, votre application iOS semblera gelée, et votre application macOS affichera la célèbre boule de plage/roue tournante.

Lors de l'exécution d'une tâche longue (appel réseau, travail intensif en calcul, etc.), nous évitons de geler l'interface utilisateur en effectuant ce travail sur une file d'attente d'arrière-plan. Ensuite, nous mettons à jour l'interface utilisateur avec les résultats sur la file d'attente principale :

```swift
URLSession.shared.dataTask(with: url) { data, response, error in
    if let data = data {
        DispatchQueue.main.async { // Travail UI
            self.label.text = String(data: data, encoding: .utf8)
        }
    }
}
```

En règle générale, tout le travail UI doit être exécuté sur la file d'attente principale. Vous pouvez activer l'option Main Thread Checker dans Xcode pour recevoir des avertissements chaque fois que du travail UI est exécuté sur un thread d'arrière-plan.

![le vérificateur de thread principal peut être trouvé dans l'éditeur de schéma](https://www.freecodecamp.org/news/content/images/2020/01/1-HwivHHBJZKmFzhQfiJZ3nQ.png)

En plus de la file d'attente principale, chaque application dispose de plusieurs files d'attente concurrentes prédéfinies qui ont différents niveaux de [Qualité de Service](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html) (une notion abstraite de priorité dans GCD).

Par exemple, voici le code pour soumettre du travail de manière asynchrone à la file d'attente QoS _interaction utilisateur_ (priorité la plus élevée) :

```swift
DispatchQueue.global(qos: .userInteractive).async {
    print("Nous sommes sur une file d'attente globale concurrente !") 
}
```

Alternativement, vous pouvez appeler la file d'attente globale de _priorité par défaut_ en ne spécifiant pas de QoS comme ceci :

```swift
DispatchQueue.global().async {
    print("File d'attente globale générique")
}
```

De plus, vous pouvez créer vos propres files d'attente privées en utilisant la syntaxe suivante :

```swift
let serial = DispatchQueue(label: "com.besher.serial-queue")
serial.async {
    print("File d'attente série privée")
}
```

Lors de la création de files d'attente privées, il est utile d'utiliser une étiquette descriptive (comme la notation DNS inverse), car cela vous aidera lors du débogage dans le navigateur de Xcode, lldb et Instruments :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-vri5m4HJq2CBLeTUYg-RTQ-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-zc_ZBGW9gVUF4h7TQA5Lgw.png)

Par défaut, les files d'attente privées sont _série_ (je vais expliquer ce que cela signifie bientôt, promis !) Si vous souhaitez créer une file d'attente privée _concurrente_, vous pouvez le faire via le paramètre optionnel _attributes_ :

```swift
let concurrent = DispatchQueue(label: "com.besher.serial-queue", attributes: .concurrent)
concurrent.sync {
    print("File d'attente concurrente privée")
}
```

Il existe également un paramètre QoS optionnel. Les files d'attente privées que vous créez finiront par atterrir dans l'une des files d'attente globales concurrentes en fonction de leurs paramètres donnés.

### Qu'y a-t-il dans une tâche ?

J'ai mentionné l'envoi de tâches aux files d'attente. Les tâches peuvent faire référence à tout bloc de code que vous soumettez à une file d'attente en utilisant les fonctions `sync` ou `async`. Elles peuvent être soumises sous la forme d'une fermeture anonyme :

```swift
DispatchQueue.global().async {
    print("Fermeture anonyme")
}
```

Ou à l'intérieur d'un [élément de travail de distribution](https://developer.apple.com/documentation/dispatch/dispatchworkitem) qui est exécuté plus tard :

```swift
let item = DispatchWorkItem(qos: .utility) {
    print("Élément de travail à exécuter plus tard")
}
```

Quelle que soit la manière dont vous envoyez de manière synchrone ou asynchrone, et que vous choisissiez une file d'attente série ou concurrente, tout le code à l'intérieur d'une seule tâche s'exécutera ligne par ligne. La concurrence n'est pertinente que lors de l'évaluation de _multiples_ tâches.

Par exemple, si vous avez 3 boucles à l'intérieur de la **même** tâche, ces boucles s'exécuteront _toujours_ dans l'ordre :

```swift
DispatchQueue.global().async {
    for i in 0..<10 {
        print(i)
    }

    for _ in 0..<10 {
        print("?")
    }

    for _ in 0..<10 {
        print("?")
    }
}
```

Ce code imprime toujours dix chiffres de 0 à 9, suivis de dix cercles bleus, suivis de dix cœurs brisés, quelle que soit la manière dont vous envoyez cette fermeture.

Les tâches individuelles peuvent également avoir leur propre niveau de QoS (par défaut, elles utilisent la priorité de leur file d'attente). Cette distinction entre la QoS de la file d'attente et la QoS de la tâche conduit à un comportement intéressant que nous discuterons dans la section sur l'inversion de priorité.

À ce stade, vous vous demandez peut-être ce que signifient _série_ et _concurrent_. Vous vous demandez peut-être aussi quelles sont les différences entre `sync` et `async` lors de l'envoi de vos tâches. Cela nous amène au cœur de cet article, alors plongeons-nous dedans !

## Sync vs Async

Lorsque vous envoyez une tâche à une file d'attente, vous pouvez choisir de le faire de manière synchrone ou asynchrone en utilisant les fonctions d'envoi `sync` et `async`. Sync et async affectent principalement la **source** de la tâche soumise, c'est-à-dire la file d'attente à partir de laquelle elle est soumise.

Lorsque votre code atteint une instruction `sync`, il bloquera la file d'attente actuelle jusqu'à ce que cette tâche soit terminée. Une fois la tâche terminée, le contrôle est rendu à l'appelant, et le code qui suit la tâche `sync` continuera.

Considérez `sync` comme synonyme de « bloquant ».

Une instruction `async`, en revanche, s'exécutera de manière asynchrone par rapport à la file d'attente actuelle, et rendra immédiatement le contrôle à l'appelant sans attendre que le contenu de la fermeture `async` s'exécute. Il n'y a aucune garantie quant au moment exact où le code à l'intérieur de cette fermeture async s'exécutera.

### File d'attente actuelle ?

Il n'est peut-être pas évident de savoir quelle est la source, ou la file d'attente _actuelle_, car elle n'est pas toujours explicitement définie dans le code.

Par exemple, si vous appelez votre instruction `sync` à l'intérieur de viewDidLoad, votre file d'attente actuelle sera la file d'attente de distribution principale. Si vous appelez la même fonction à l'intérieur d'un gestionnaire de completion URLSession, votre file d'attente actuelle sera une file d'attente d'arrière-plan.

Revenons à sync vs async, prenons cet exemple :

```swift
DispatchQueue.global().sync {
    print("À l'intérieur")
}
print("À l'extérieur")
// Sortie de la console :
// À l'intérieur
// À l'extérieur
```

Le code ci-dessus bloquera la file d'attente actuelle, entrera dans la fermeture et exécutera son code sur la file d'attente globale en imprimant « À l'intérieur », avant de procéder à l'impression de « À l'extérieur ». Cet ordre est garanti.

Voyons ce qui se passe si nous essayons `async` à la place :

```swift
DispatchQueue.global().async {
    print("À l'intérieur")
}
print("À l'extérieur")
// Sortie potentielle de la console (basée sur le QoS) :
// À l'extérieur
// À l'intérieur
```

Notre code soumet maintenant la fermeture à la file d'attente globale, puis procède immédiatement à l'exécution de la ligne suivante. Il imprimera _probablement_ « À l'extérieur » avant « À l'intérieur », mais cet ordre n'est pas garanti. Cela dépend du QoS des files d'attente source et de destination, ainsi que d'autres facteurs contrôlés par le système.

Les threads sont un détail d'implémentation dans GCD — nous n'avons pas de contrôle direct sur eux et ne pouvons les gérer qu'en utilisant des abstractions de files d'attente. Néanmoins, je pense qu'il peut être utile de « jeter un coup d'œil sous le capot » au comportement des threads pour comprendre certains défis que nous pourrions rencontrer avec GCD.

Par exemple, lorsque vous soumettez une tâche en utilisant `sync`, [GCD optimise les performances en exécutant cette tâche sur le thread actuel](https://developer.apple.com/documentation/dispatch/1452870-dispatch_sync?language=objc) (l'appelant).

Il y a une exception cependant, qui est lorsque vous soumettez une tâche synchrone à la file d'attente principale — cela exécutera toujours la tâche sur le thread principal et non sur l'appelant. Ce comportement peut avoir certaines répercussions que nous explorerons dans la section sur l'inversion de priorité.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Sync-400.gif)
_[De Dispatcher sur Github](https://github.com/almaleh/Dispatcher" rel="noopener nofollow)_

### Lequel utiliser ?

Lors de l'envoi de travail à une file d'attente, [Apple recommande d'utiliser l'exécution asynchrone plutôt que l'exécution synchrone](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationQueues/OperationQueues.html#//apple_ref/doc/uid/TP40008091-CH102-SW21). Cependant, il existe des situations où `sync` pourrait être le meilleur choix, comme lors de la gestion des conditions de course, ou lors de l'exécution d'une tâche très petite. Je couvrirai ces situations sous peu.

Une grande conséquence de l'exécution de travail de manière asynchrone à l'intérieur d'une fonction est que la fonction ne peut plus directement retourner ses valeurs (si elles dépendent du travail async qui est en cours). Elle doit plutôt utiliser un paramètre de fermeture/gestionnaire de completion pour livrer les résultats.

Pour démontrer ce concept, prenons une petite fonction qui accepte des données d'image, effectue un calcul coûteux pour traiter l'image, puis retourne le résultat :

```swift
func processImage(data: Data) -> UIImage? {
    guard let image = UIImage(data: data) else { return nil }
    // appel d'une fonction coûteuse
    let processedImage = upscaleAndFilter(image: image)
    return processedImage 
}
```

Dans cet exemple, la fonction `upscaleAndFilter(image:)` peut prendre plusieurs secondes, nous voulons donc la délesguer à une file d'attente séparée pour éviter de geler l'interface utilisateur. Créons une file d'attente dédiée pour le traitement d'image, puis envoyons la fonction coûteuse de manière asynchrone :

```swift
let imageProcessingQueue = DispatchQueue(label: "com.besher.image-processing")

func processImageAsync(data: Data) -> UIImage? {
    guard let image = UIImage(data: data) else { return nil }
    
    imageProcessingQueue.async {
        let processedImage = upscaleAndFilter(image: image)
        return processedImage
    }
}
```

Il y a deux problèmes avec ce code. Tout d'abord, l'instruction return est à l'intérieur de la fermeture async, donc elle ne retourne plus de valeur à la fonction `processImageAsync(data:)`, et ne sert actuellement à rien.

Mais le problème plus important est que notre fonction `processImageAsync(data:)` ne retourne plus aucune valeur, car la fonction atteint la fin de son corps avant d'entrer dans la fermeture `async`.

Pour corriger cette erreur, nous allons ajuster la fonction afin qu'elle ne retourne plus directement une valeur. Au lieu de cela, elle aura un nouveau paramètre de gestionnaire de completion que nous pouvons appeler une fois que notre fonction asynchrone a terminé son travail :

```swift
let imageProcessingQueue = DispatchQueue(label: "com.besher.image-processing")

func processImageAsync(data: Data, completion: @escaping (UIImage?) -> Void) {
    guard let image = UIImage(data: data) else {
        completion(nil)
        return
    }

    imageProcessingQueue.async {
        let processedImage =  self.upscaleAndFilter(image: image)
        completion(processedImage)
    }
}
```

Comme le montre cet exemple, le changement pour rendre la fonction asynchrone s'est propagé à son appelant, qui doit maintenant passer une fermeture et gérer les résultats de manière asynchrone également. En introduisant une tâche asynchrone, vous pouvez potentiellement modifier une chaîne de plusieurs fonctions.

La concurrence et l'exécution asynchrone ajoutent de la complexité à votre projet comme nous venons de l'observer. Cette indirection rend également le débogage plus difficile. C'est pourquoi il est vraiment payant de penser à la concurrence tôt dans votre cycle de conception — ce n'est pas quelque chose que vous voulez ajouter à la fin de votre cycle de conception.

L'exécution synchrone, en revanche, n'augmente pas la complexité. Elle vous permet plutôt de continuer à utiliser les instructions return comme vous le faisiez auparavant. Une fonction contenant une tâche `sync` ne retournera pas tant que le code à l'intérieur de cette tâche n'aura pas été terminé. Par conséquent, elle ne nécessite pas de gestionnaire de completion.

Si vous envoyez une tâche minuscule (par exemple, la mise à jour d'une valeur), envisagez de le faire de manière synchrone. Non seulement cela vous aide à garder votre code simple, mais il s'exécutera également mieux — Async est censé [entraîner un surcoût](https://gist.github.com/tclementdev/6af616354912b0347cdf6db159c37057) qui dépasse le bénéfice de faire le travail de manière asynchrone pour des tâches minuscules qui prennent moins de 1 ms à compléter.

Si vous envoyez une tâche volumineuse, cependant, comme le traitement d'image que nous avons effectué ci-dessus, envisagez de le faire de manière asynchrone pour éviter de bloquer l'appelant trop longtemps.

### Envoi sur la même file d'attente

Bien qu'il soit sûr d'envoyer une tâche de manière asynchrone d'une file d'attente vers elle-même (par exemple, vous pouvez utiliser [.asyncAfter](https://developer.apple.com/documentation/dispatch/dispatchqueue/2300020-asyncafter) sur la file d'attente actuelle), vous ne pouvez pas envoyer une tâche _de manière synchrone_ d'une file d'attente vers la même file d'attente. Cela entraînera un blocage qui fera planter immédiatement l'application !

Ce problème peut se manifester lors de l'exécution d'une chaîne d'appels synchrones qui ramènent à la file d'attente d'origine. C'est-à-dire que vous envoyez une tâche sur une autre file d'attente avec `sync`, et lorsque la tâche est terminée, elle envoie les résultats en arrière dans la file d'attente d'origine, entraînant un blocage. Utilisez `async` pour éviter de tels plantages.

### Bloquer la file d'attente principale

L'envoi de tâches de manière synchrone _à partir_ de la file d'attente principale bloquera cette file d'attente, gelant ainsi l'interface utilisateur, jusqu'à ce que la tâche soit terminée. Il est donc préférable d'éviter d'envoyer du travail de manière synchrone à partir de la file d'attente principale, sauf si vous effectuez un travail vraiment léger.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Async-400.gif)
_[préférez utiliser async à partir de la file d'attente principale](https://github.com/almaleh/Dispatcher" rel="noopener nofollow)_

## Série vs Concurrent

_Série_ et _concurrent_ affectent la **destination** — la file d'attente dans laquelle votre travail a été soumis pour s'exécuter. Cela contraste avec _sync_ et _async_, qui affectaient la **source**.

Une file d'attente série n'exécutera pas son travail sur plus d'un thread à la fois, quel que soit le nombre de tâches que vous envoyez sur cette file d'attente. Par conséquent, les tâches sont garanties de non seulement démarrer, mais aussi de se terminer, dans l'ordre premier entré, premier sorti.

De plus, lorsque vous bloquez une file d'attente série (en utilisant un appel `sync`, un sémaphore ou un autre outil), tout le travail sur cette file d'attente s'arrêtera jusqu'à ce que le blocage soit terminé.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Serial-400.gif)
_[De Dispatcher sur Github](https://github.com/almaleh/Dispatcher" rel="noopener nofollow)_

Une file d'attente concurrente peut générer plusieurs threads, et le système décide du nombre de threads créés. Les tâches commencent toujours dans l'ordre FIFO, mais la file d'attente n'attend pas que les tâches se terminent avant de démarrer la tâche suivante, donc les tâches sur les files d'attente concurrentes peuvent se terminer dans n'importe quel ordre.

Lorsque vous effectuez une commande de blocage sur une file d'attente concurrente, elle ne bloquera pas les autres threads de cette file d'attente. De plus, lorsqu'une file d'attente concurrente est bloquée, elle risque de provoquer une _explosion de threads_. Je couvrirai cela plus en détail plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Concurrent-400.gif)
_[De Dispatcher sur Github](https://github.com/almaleh/Dispatcher" rel="noopener nofollow)_

La file d'attente principale de votre application est série. Toutes les files d'attente globales prédéfinies sont concurrentes. Toute file d'attente de distribution privée que vous créez est série par défaut, mais peut être définie comme concurrente en utilisant un attribut optionnel comme discuté précédemment.

Il est important de noter ici que le concept de _série_ vs _concurrent_ n'est pertinent que lors de la discussion d'une file d'attente spécifique. Toutes les files d'attente sont concurrentes les unes par rapport aux _autres_.

C'est-à-dire, si vous envoyez du travail de manière asynchrone à partir de la file d'attente principale vers une file d'attente privée _série_, ce travail sera terminé _de manière concurrente_ par rapport à la file d'attente principale. Et si vous créez deux files d'attente série différentes, puis effectuez un travail bloquant sur l'une d'elles, l'autre file d'attente n'est pas affectée.

Pour démontrer la concurrence de plusieurs files d'attente série, prenons cet exemple :

```swift
let serial1 = DispatchQueue(label: "com.besher.serial1")
let serial2 = DispatchQueue(label: "com.besher.serial2")

serial1.async {
    for _ in 0..<5 { print("?") }
}

serial2.async {
    for _ in 0..<5 { print("?") }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-zJztLeessQUMvONpoLW0ZQ.png)

Les deux files d'attente ici sont série, mais les résultats sont mélangés car elles s'exécutent de manière concurrente l'une par rapport à l'autre. Le fait qu'elles soient chacune série (ou concurrente) n'a aucun effet sur ce résultat. Leur niveau de QoS détermine qui terminera généralement en premier (l'ordre n'est pas garanti).

Si nous voulons nous assurer que la première boucle se termine avant de commencer la deuxième boucle, nous pouvons soumettre la première tâche de manière synchrone à partir de l'appelant :

```swift
let serial1 = DispatchQueue(label: "com.besher.serial1")
let serial2 = DispatchQueue(label: "com.besher.serial2")

serial1.sync { // <---- nous avons changé cela en 'sync'
    for _ in 0..<5 { print("?") }
}
// nous n'arrivons pas ici jusqu'à ce que la première boucle se termine
serial2.async {
    for _ in 0..<5 { print("?") }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-s1N-5HfXpcAtsKQ3tZ-DHQ-2.png)

Ce n'est pas nécessairement souhaitable, car nous bloquons maintenant l'appelant pendant que la première boucle s'exécute.

Pour éviter de bloquer l'appelant, nous pouvons soumettre les deux tâches de manière asynchrone, mais à la _même_ file d'attente série :

```swift
let serial = DispatchQueue(label: "com.besher.serial")

serial.async {
    for _ in 0..<5 { print("?") }
}

serial.async {
    for _ in 0..<5 { print("?") }
}	
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-s1N-5HfXpcAtsKQ3tZ-DHQ-2-1.png)

Maintenant, nos tâches s'exécutent de manière concurrente par rapport à l'_appelant_, tout en conservant leur ordre intact.

Notez que si nous rendons notre file d'attente unique concurrente via le paramètre optionnel, nous revenons aux résultats mélangés, comme prévu :

```swift
let concurrent = DispatchQueue(label: "com.besher.concurrent", attributes: .concurrent)

concurrent.async {
    for _ in 0..<5 { print("?") }
}

concurrent.async {
    for _ in 0..<5 { print("?") }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-zJztLeessQUMvONpoLW0ZQ-1.png)

Parfois, vous pourriez confondre l'exécution synchrone avec l'exécution série (en tout cas, moi oui), mais ce sont des choses très différentes. Par exemple, essayez de changer le premier envoi à la ligne 3 de notre exemple précédent en un appel `sync` :

```swift
let concurrent = DispatchQueue(label: "com.besher.concurrent", attributes: .concurrent)

concurrent.sync {
    for _ in 0..<5 { print("?") }
}

concurrent.async {
    for _ in 0..<5 { print("?") }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-s1N-5HfXpcAtsKQ3tZ-DHQ.png)

Soudain, nos résultats sont de nouveau dans un ordre parfait. Mais c'est une file d'attente concurrente, alors comment cela peut-il se produire ? L'instruction `sync` l'a-t-elle transformée en une file d'attente série ?

La réponse est **non !**

C'est un peu trompeur. Ce qui s'est passé, c'est que nous n'avons pas atteint l'appel `async` avant que la première tâche n'ait terminé son exécution. La file d'attente est toujours très concurrente, mais dans cette section zoomée du code, elle apparaît comme si elle était série. Cela est dû au fait que nous bloquons l'appelant et ne procédons pas à la tâche suivante jusqu'à ce que la première soit terminée.

Si une autre file d'attente quelque part dans votre application essayait de soumettre du travail à cette même file d'attente alors qu'elle exécutait encore l'instruction `sync`, ce travail s'exécutera _concurremment_ avec ce que nous avons en cours ici, car c'est toujours une file d'attente concurrente.

### Lequel utiliser ?

Les files d'attente série tirent parti des optimisations CPU et de la mise en cache, et aident à réduire les changements de contexte.

Apple recommande de commencer avec une file d'attente série par sous-système dans votre application — par exemple, une pour le réseau, une pour la compression de fichiers, etc. Si le besoin se présente, vous pouvez ensuite étendre à une [hiérarchie de files d'attente par sous-système](https://developer.apple.com/videos/play/wwdc2017/706/) en utilisant la [méthode setTarget](https://developer.apple.com/documentation/dispatch/dispatchobject/1452989-settarget) ou le [paramètre cible optionnel](https://developer.apple.com/documentation/dispatch/dispatchqueue/2300059-init) lors de la construction des files d'attente.

Si vous rencontrez un goulot d'étranglement de performance, mesurez les performances de votre application, puis voyez si une file d'attente concurrente aide. Si vous ne voyez pas de bénéfice mesurable, il est préférable de rester avec des files d'attente série.

## Pièges

### Inversion de priorité et Qualité de Service

L'[inversion de priorité](https://en.wikipedia.org/wiki/Priority_inversion) se produit lorsqu'une tâche de haute priorité est empêchée de s'exécuter par une tâche de basse priorité, inversant ainsi leurs priorités relatives.

Cette situation se produit souvent lorsqu'une file d'attente de haute QoS partage des ressources avec une file d'attente de basse QoS, et que la file d'attente de basse QoS obtient un verrou sur cette ressource.

Mais je souhaite couvrir un scénario différent qui est plus pertinent pour notre discussion — c'est lorsque vous soumettez des tâches à une file d'attente série de basse QoS, puis soumettez une tâche de haute QoS à cette même file d'attente. Ce scénario entraîne également une inversion de priorité, car la tâche de haute QoS doit attendre que les tâches de basse QoS se terminent.

GCD résout l'inversion de priorité en augmentant temporairement la QoS de la file d'attente qui contient les tâches de basse priorité qui sont « devant », ou bloquant, votre tâche de haute priorité.

C'est un peu comme avoir des voitures bloquées _devant_ une ambulance. Soudain, elles sont autorisées à traverser le feu rouge juste pour que l'ambulance puisse avancer (en réalité, les voitures se déplacent sur le côté, mais imaginez une rue étroite (série) ou quelque chose, vous voyez le point :-P)

Pour illustrer le problème d'inversion, commençons par ce code :

```swift

enum Color: String {
    case blue = "?"
    case white = "F535"
}

func output(color: Color, times: Int) {
    for _ in 1...times {
        print(color.rawValue)
    }
}

let starterQueue = DispatchQueue(label: "com.besher.starter", qos: .userInteractive)
let utilityQueue = DispatchQueue(label: "com.besher.utility", qos: .utility)
let backgroundQueue = DispatchQueue(label: "com.besher.background", qos: .background)
let count = 10

starterQueue.async {

    backgroundQueue.async {
        output(color: .white, times: count)
    }

    backgroundQueue.async {
        output(color: .white, times: count)
    }

    utilityQueue.async {
        output(color: .blue, times: count)
    }

    utilityQueue.async {
        output(color: .blue, times: count)
    }

    // la prochaine instruction va ici
}
```

Nous créons une file d'attente de démarrage (à partir de laquelle nous envoyons les tâches), ainsi que deux files d'attente avec différentes QoS. Ensuite, nous envoyons des tâches à chacune de ces deux files d'attente, chaque tâche imprimant un nombre égal de cercles d'une couleur spécifique (la file d'attente _utility_ est bleue, _background_ est blanche.)

Parce que ces tâches sont soumises de manière asynchrone, chaque fois que vous exécutez l'application, vous obtiendrez des résultats légèrement différents. Cependant, comme vous vous en doutez, la file d'attente avec la QoS la plus basse (background) termine presque toujours en dernier. En fait, les 10 à 15 derniers cercles sont généralement tous blancs.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-woRLw218x4QZKFov0w1hDA.gif)
_aucune surprise ici_

Mais regardez ce qui se passe lorsque nous envoyons une tâche **sync** à la file d'attente d'arrière-plan après la dernière instruction async. Vous n'avez même pas besoin d'imprimer quoi que ce soit à l'intérieur de l'instruction `sync`, l'ajout de cette ligne suffit :

```swift
// ajoutez ceci après la dernière instruction async,
// toujours à l'intérieur de starterQueue.async
backgroundQueue.sync {}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-yxMCgE4Vy8Ws2309CvYelA.gif)
_inversion de priorité_

Les résultats dans la console ont changé ! Maintenant, la file d'attente de priorité plus élevée (utility) termine toujours en dernier, et les 10 à 15 derniers cercles sont _bleus._

Pour comprendre pourquoi cela se produit, nous devons revenir au fait que le travail synchrone est exécuté sur le thread de l'appelant (sauf si vous envoyez à la file d'attente principale.)

Dans notre exemple ci-dessus, l'appelant (starterQueue) a la QoS la plus élevée (userInteractive). Par conséquent, cette tâche `sync` en apparence inoffensive ne bloque pas seulement la file d'attente de démarrage, mais elle s'exécute également sur le thread de haute QoS du starter. La tâche s'exécute donc avec une QoS élevée, mais il y a deux autres tâches devant elle sur la même file d'attente d'arrière-plan qui ont une QoS _background_. Inversion de priorité détectée !

Comme prévu, GCD résout cette inversion en augmentant la QoS de toute la file d'attente pour correspondre temporairement à la tâche de haute QoS. Par conséquent, toutes les tâches de la file d'attente d'arrière-plan finissent par s'exécuter avec une QoS _user interactive_, qui est plus élevée que la QoS _utility_. Et c'est pourquoi les tâches utility se terminent en dernier !

Note de côté : Si vous retirez la file d'attente de démarrage de cet exemple et envoyez depuis la file d'attente principale à la place, vous obtiendrez des résultats similaires, car la file d'attente principale a également une QoS _user interactive_.

Pour éviter l'inversion de priorité dans cet exemple, nous devons éviter de bloquer la file d'attente de démarrage avec l'instruction `sync`. Utiliser `async` résoudrait ce problème.

Bien que ce ne soit pas toujours idéal, vous pouvez minimiser les inversions de priorité en vous en tenant à la QoS par défaut lors de la création de files d'attente privées ou de l'envoi à la file d'attente globale concurrente.

### Explosion de threads

Lorsque vous utilisez une file d'attente concurrente, vous risquez une explosion de threads si vous n'êtes pas prudent. Cela peut se produire lorsque vous essayez d'envoyer des tâches à une file d'attente concurrente qui est actuellement bloquée (par exemple avec un sémaphore, sync, ou autre). Vos tâches _s'exécuteront_, mais le système finira probablement par créer de nouveaux threads pour accommoder ces nouvelles tâches, et les threads ne sont pas bon marché.

C'est probablement pourquoi Apple suggère de commencer avec une file d'attente série par sous-système dans votre application, car chaque file d'attente série ne peut utiliser qu'un seul thread. Rappelez-vous que les files d'attente série sont concurrentes par rapport aux _autres_ files d'attente, donc vous obtenez toujours un avantage de performance lorsque vous déléguez votre travail à une file d'attente, même si elle n'est pas concurrente.

### Conditions de course

Les tableaux, dictionnaires, structures et autres types de valeur Swift ne sont pas thread-safe par défaut. Par exemple, lorsque vous avez plusieurs threads qui tentent d'accéder et de **modifier** le même tableau, vous commencerez à rencontrer des problèmes.

Il existe différentes solutions au [problème des lecteurs-écrivains](https://en.wikipedia.org/wiki/Readers%E2%80%93writers_problem), comme l'utilisation de verrous ou de sémaphores. Mais la solution pertinente que je souhaite discuter ici est l'utilisation d'une [file d'attente d'isolement](http://khanlou.com/2016/04/the-GCD-handbook/).

Supposons que nous avons un tableau d'entiers, et que nous voulons soumettre un travail asynchrone qui référence ce tableau. Tant que notre travail ne fait que _lire_ le tableau et ne le modifie pas, nous sommes en sécurité. Mais dès que nous essayons de modifier le tableau dans l'une de nos tâches asynchrones, nous introduisons une instabilité dans notre application.

C'est un problème délicat car votre application peut s'exécuter 10 fois sans problème, puis planter à la 11ème fois. Un outil très pratique pour cette situation est le Thread Sanitizer dans Xcode. L'activation de cette option vous aidera à identifier les conditions de course potentielles dans votre application.

![le thread sanitizer peut être accessible dans l'éditeur de schéma](https://www.freecodecamp.org/news/content/images/2020/01/1-SQpYE8quVN_ziJsg8bqrYQ.png)
_cette option est uniquement disponible sur le simulateur_

Pour démontrer le problème, prenons cet exemple (admettons, un peu forcé) :

```swift
class ViewController: UIViewController {
    
    let concurrent = DispatchQueue(label: "com.besher.concurrent", attributes: .concurrent)
    var array = [1,2,3,4,5]

    override func viewDidLoad() {
        for _ in 0...1 {
            race()
        }
    }

    func race() {

        concurrent.async {
            for i in self.array { // accès en lecture
                print(i)
            }
        }

        concurrent.async {
            for i in 0..<10 {
                self.array.append(i) // accès en écriture
            }
        }
    }
}
```

L'une des tâches `async` modifie le tableau en ajoutant des valeurs. Si vous essayez de l'exécuter sur votre simulateur, vous ne planterez peut-être pas. Mais exécutez-le suffisamment de fois (ou augmentez la fréquence de la boucle à la ligne 7), et vous finirez par planter. Si vous activez le thread sanitizer, vous recevrez un avertissement à chaque fois que vous exécuterez l'application.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/1-NNBN1ZKViVwYzqJfZenaeQ.png)

Pour gérer cette condition de course, nous allons ajouter une file d'attente d'isolement qui utilise le [drapeau de barrière](https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/1780674-barrier). Ce drapeau permet à toutes les tâches en attente sur la file d'attente de se terminer, mais bloque toute tâche supplémentaire de s'exécuter jusqu'à ce que la tâche de barrière soit terminée.

Pensez à la barrière comme à un concierge nettoyant des toilettes publiques (ressource partagée). Il y a plusieurs (concurrentes) cabines à l'intérieur des toilettes que les gens peuvent utiliser.

À l'arrivée, le concierge place un panneau de nettoyage (barrière) bloquant tout nouvel arrivant d'entrer jusqu'à ce que le nettoyage soit terminé, mais le concierge ne commence pas à nettoyer avant que toutes les personnes à l'intérieur n'aient terminé leurs affaires. Une fois qu'elles sont toutes parties, le concierge procède au nettoyage des toilettes publiques en isolation.

Une fois enfin terminé, le concierge retire le panneau (barrière) afin que les personnes qui sont en attente à l'extérieur puissent enfin entrer.

Voici à quoi cela ressemble en code :

```swift
class ViewController: UIViewController {
    let concurrent = DispatchQueue(label: "com.besher.concurrent", attributes: .concurrent)
    let isolation = DispatchQueue(label: "com.besher.isolation", attributes: .concurrent)
    private var _array = [1,2,3,4,5]
    
    var threadSafeArray: [Int] {
        get {
            return isolation.sync {
                _array
            }
        }
        set {
            isolation.async(flags: .barrier) {
                self._array = newValue
            }
        }
    }
    
    override func viewDidLoad() {
        for _ in 0...15 {
            race()
        }
    }
    
    func race() {
        concurrent.async {
            for i in self.threadSafeArray {
                print(i)
            }
        }
        
        concurrent.async {
            for i in 0..<10 {
                self.threadSafeArray.append(i)
            }
        }
    }
}
```

Nous avons ajouté une nouvelle file d'attente d'isolement, et restreint l'accès au tableau privé en utilisant un getter et un setter qui placeront une barrière lors de la modification du tableau.

Le getter doit être `sync` afin de retourner directement une valeur. Le setter peut être `async`, car nous n'avons pas besoin de bloquer l'appelant pendant que l'écriture est en cours.

Nous aurions pu utiliser une file d'attente série sans barrière pour résoudre la condition de course, mais alors nous aurions perdu l'avantage d'avoir un accès concurrent en lecture au tableau. Peut-être que cela a du sens dans votre cas, c'est à vous de décider.

## Conclusion

Merci beaucoup d'avoir lu jusqu'ici ! J'espère que vous avez appris quelque chose de nouveau dans cet article. Je vais vous laisser avec un résumé et quelques conseils généraux :

### Résumé

* Les files d'attente commencent toujours leurs tâches dans l'ordre FIFO
* Les files d'attente sont toujours concurrentes par rapport aux _autres_ files d'attente
* **Sync** vs **Async** concerne la source
* **Série** vs **Concurrent** concerne la destination
* Sync est synonyme de « bloquant »
* Async rend immédiatement le contrôle à l'appelant
* Série utilise un seul thread, et garantit l'ordre d'exécution
* Concurrent utilise plusieurs threads, et risque une explosion de threads
* Pensez à la concurrence tôt dans votre cycle de conception
* Le code synchrone est plus facile à raisonner et à déboguer
* Évitez de dépendre des files d'attente globales concurrentes si possible
* Envisagez de commencer avec une file d'attente série par sous-système
* Passez à une file d'attente concurrente uniquement si vous voyez un bénéfice de performance **mesurable**

J'aime la métaphore du [Swift Concurrency Manifesto](https://gist.github.com/lattner/31ed37682ef1576b16bca1432ea9f782) d'avoir une « île de sérialisation dans un océan de concurrence ». Ce sentiment a également été partagé dans ce tweet de Matt Diephouse :

%[https://twitter.com/mdiep/status/1207112168224763905?s=20]

Lorsque vous appliquez la concurrence avec cette philosophie en tête, je pense que cela vous aidera à atteindre un code concurrent qui peut être raisonné sans se perdre dans un fouillis de rappels.

Si vous avez des questions ou des commentaires, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/BesherMaleh)

[Besher Al Maleh](https://www.besher.ca)

_Photo de couverture par [Onur K](https://unsplash.com/@kodozani?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/railway?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_

### Téléchargez l'application compagnon ici :

%[https://github.com/almaleh/Dispatcher]

#### Consultez quelques-uns de mes autres articles :

%[https://medium.com/flawless-app-stories/fireworks-a-visual-particles-editor-for-swift-618e76347798]

%[https://medium.com/flawless-app-stories/you-dont-always-need-weak-self-a778bec505ef]

#### Lectures complémentaires :

%[https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html]

%[https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/#grand-central-dispatch]

%[https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/]

[http://khanlou.com/2016/04/the-GCD-handbook/](http://khanlou.com/2016/04/the-GCD-handbook/)

%[https://stackoverflow.com/a/53582047]

#### Vidéos WWDC :

%[https://developer.apple.com/videos/play/wwdc2017/706/]

%[https://developer.apple.com/videos/play/wwdc2015/718/]