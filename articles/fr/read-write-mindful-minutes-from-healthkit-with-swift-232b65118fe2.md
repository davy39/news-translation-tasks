---
title: Comment lire et écrire les Minutes de Pleine Conscience depuis HealthKit d'iOS
  avec Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T18:01:41.000Z'
originalURL: https://freecodecamp.org/news/read-write-mindful-minutes-from-healthkit-with-swift-232b65118fe2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rFvNSSAw51LOil7bwsVjBA.png
tags:
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment lire et écrire les Minutes de Pleine Conscience depuis HealthKit
  d'iOS avec Swift
seo_desc: 'By Ben Church

  I took the time to figure out how to read and write from HealthKit so you don’t
  have to!


  Let me show you what Apple makes hard to find ?

  I absolutely love the route Apple has been going with their iOS SDK’s. (Their hardware
  not so much...'
---

Par Ben Church

J'ai pris le temps de comprendre comment lire et écrire depuis HealthKit pour que vous n'ayez pas à le faire !

![Image](https://cdn-media-1.freecodecamp.org/images/1*fPKXwxU5RwbLuoSMBJzcBg.png)
_Laissez-moi vous montrer ce qu'Apple rend difficile à trouver ?_

J'adore absolument la direction qu'Apple a prise avec leurs SDK iOS. ([Leur matériel un peu moins](https://twitter.com/bnchrch/status/995519114318725120)). L'accent mis par Apple sur la [sécurité](https://www.theguardian.com/technology/2016/jun/15/apple-fbi-file-encryption-wwdc) lui a permis de devenir une entreprise fiable à qui confier vos informations sensibles. Cela a permis aux iPhones de progresser en tant que dispositifs les mieux adaptés pour héberger des données médicales. Par conséquent, ils sont également les meilleurs dispositifs pour créer des logiciels qui interagissent avec les informations personnelles sensibles d'un utilisateur.

Dans cette optique, je crois qu'il est essentiel de savoir comment lire et écrire depuis HealthKit d'Apple afin que nous, en tant que développeurs, puissions tirer parti de la position qu'Apple s'est donnée. Ainsi, le tutoriel d'aujourd'hui va se concentrer sur **la lecture et l'écriture des Minutes de Pleine Conscience depuis HealthKit d'Apple**.

À la fin de ce tutoriel, vous aurez appris comment :

* Configurer une application iOS de base
* Demander la permission de lire et écrire des données depuis HealthKit
* Lire et interroger des données depuis HealthKit
* Écrire des données dans HealthKit

Très bien, plongeons dans la configuration du projet XCode. ?

### Configurer le squelette

Tout grand projet commence à partir du même écran (si vous cherchez simplement du code, vous pouvez sauter cette section).

#### 1. Créer un nouveau projet

Commençons par créer un nouveau projet **Single View App** dans XCode.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2rFbwZuGufTSLI8p_FsJJg.png)
_Commencez par aller dans Fichier > Nouveau > Projet_

![Image](https://cdn-media-1.freecodecamp.org/images/1*HiwauM4djV0kvMcPjrDVPQ.png)
_Vous devriez pouvoir laisser tout cela identique, à l'exception de mon nom._

#### 2. Inclure HealthKit

Une fois que nous avons créé le projet, nous devons inclure `HealthKit` avec notre application :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZK3RgCV8Z9HBhSiCEU3Org.png)
_Inclure HealthKit dans notre App_

et mettre à jour le fichier `info.plist` pour contenir ce que l'utilisateur verra lorsque nous demanderons la permission d'accéder à leurs données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rLBnDDqGFBBeHL7rM0lauA.png)
_Vous devez éditer le code source de ce fichier._

Ajoutez le `xml` suivant au fichier `info.plist` :

#### 3. Créer une interface utilisateur basique

Pour terminer la configuration, nous voudrons créer une interface utilisateur simple qui nous permettra de visualiser les données que nous avons lues depuis `HealthKit` et de fournir une action qui nous permettra de déclencher une écriture dans `HealthKit`.

Commencez par ouvrir le `storyboard` et :

1. Ajoutez une étiquette et connectez-la au fichier `ViewController.swift` sous le nom `mindfulMinuteLabel`
2. Ajoutez un bouton et connectez-le à une `Action` dans le fichier `ViewController.swift` intitulée `addMinuteAct`

![Image](https://cdn-media-1.freecodecamp.org/images/1*-ro1ScwT71pOlvYWM0rJzg.gif)
_Création de notre interface utilisateur_

### Donnons-lui un peu de vie...

Maintenant que nous avons mis en place l'infrastructure, il est temps d'écrire la logique qui effectuera toutes les interfaces avec `HealthKit` dont nous avons parlé.

#### 1. Demander la permission

Chaque application `HealthKit` doit explicitement demander la permission de l'utilisateur pour chaque type de lecture et d'écriture qu'elle doit effectuer. Pour ce faire, nous voulons demander sur `viewDidLoad` la permission de lire les séances de pleine conscience et la permission d'écrire les séances de pleine conscience.

Maintenant, lorsque l'application est exécutée, vous devriez voir l'écran suivant.

> _Si vous exécutez cela maintenant, vous voudrez commenter `self.retrieveMindfulMinutes()`_

![Image](https://cdn-media-1.freecodecamp.org/images/1*rFvNSSAw51LOil7bwsVjBA.png)
_Notre écran de permission_

#### 2. Lire les Minutes de Pleine Conscience

Jusqu'à présent, cela a été très simple : créer une interface utilisateur, demander la permission. Ensuite, nous allons aborder la lecture depuis HealthKit. Bien qu'Apple nous fournisse une interface utilisateur puissante, elle n'est pas nécessairement intuitive. Je vais donc commencer par vous montrer le code, puis je l'expliquerai ensuite.

La requête que nous exécutons pour récupérer nos séances de pleine conscience peut être divisée en quatre composants :

**1. Trier par date de fin**

![Image](https://cdn-media-1.freecodecamp.org/images/1*N5vzEO0ua5ZOz7yonHdldA.png)
_Obtenir les séances les plus récentes_

La première section de ce code est facultative mais utile à connaître. Ce que nous faisons, c'est demander à la requête de nous donner la liste des séances de pleine conscience triées par leur heure de fin, la séance la plus récente étant en premier.

**2. Utiliser le prédicat pour définir la requête**

![Image](https://cdn-media-1.freecodecamp.org/images/1*99AbYdyrnCnzwmgeLEQEeA.png)
_Rechercher toutes les séances des dernières 24 heures_

La partie suivante de notre code traite des spécificités réelles d'une "requête" : quel sous-ensemble de données recherchons-nous. Dans notre cas, nous voulons tous les échantillons des dernières 24 heures.

**3. Composer et exécuter votre requête**

![Image](https://cdn-media-1.freecodecamp.org/images/1*avN2Xe7pnlkiypvUN-e7aQ.png)
_Exécutez-la !_

Enfin, nous voulons combiner le `sortDescriptor`, le `predicate` et le `sampleType` que nous voulons depuis HealthKit avec la fonction qui gérera ce qui est retourné par la requête (`resultsHandler`). Après que tout cela soit composé dans une `HKSampleQuery`, la seule étape restante est de l'exécuter !

**4. Agrégation des données de session et mise à jour de l'interface utilisateur**

À l'intérieur de la fonction que nous avons définie comme notre `resultsHandler` dans la section précédente, nous voulons :

1. Obtenir le temps total pour chaque séance de pleine conscience
2. Additionner tous les temps totaux pour obtenir le nombre total de minutes de pleine conscience au cours des dernières 24 heures.
3. Mettre à jour notre étiquette avec le total.

Cela devrait être relativement simple si vous comprenez les concepts de map et reduce. Si ces concepts sont nouveaux pour vous, je vous recommande de prendre le temps de les apprendre. Ils se trouvent dans la plupart des langages de programmation et sont une excellente introduction au monde merveilleux de la programmation fonctionnelle.

La seule partie qui peut ne pas être évidente est pourquoi nous enveloppons

```
self.meditationMinutesLabel.text = labelText
```

dans `DispatchQueue.main.async`. La raison pour laquelle nous faisons cela est de pouvoir mettre à jour l'interface utilisateur sans bloquer le thread principal de l'application. C'est une convention imposée par le compilateur lui-même !

#### Écrire les données

Dans ce qui précède, nous avons vu comment lire depuis HealthKit. Mais comment y écrire des données ? Heureusement, le processus est beaucoup plus simple. Le code suivant va :

1. Compléter la fonction `addMinuteAct` que nous avons ajoutée pendant la configuration, et par conséquent, le reste de l'application.
2. Créer une `MindfulSession` d'une minute commençant maintenant
3. Sauvegarder cette nouvelle `MindfulSession` dans HealthKit
4. Mettre à jour l'étiquette pour refléter le nouveau total des Minutes de Pleine Conscience

### Lancez-le !

Avec tout cela terminé et le code écrit, vous devriez pouvoir démarrer cette application dans votre simulateur, accepter la demande de lecture et d'écriture depuis votre HealthKit, et commencer à visualiser la fréquence à laquelle vous avez médité au cours des dernières 24 heures !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z3YJ4P_pI3gt7v7ozZJuCg.gif)
_Génial !_

### Conclusion

Au début de ce projet, j'étais très enthousiaste à l'idée de me plonger dans HealthKit. Je vois qu'il est positionné pour changer la façon dont nous et les autres interagissons avec les informations personnelles sensibles.

Cependant, je pense qu'Apple, contrairement à d'autres plateformes, rend ses API un peu trop difficiles à découvrir, tant à travers leur documentation qu'à travers XCode. Espérons qu'ils amélioreront cette expérience, mais en attendant, apprendre à utiliser HealthKit peut être un exercice fastidieux.

J'espère que cet article vous évitera de devoir tâtonner et vous permettra de livrer vos produits plus rapidement !

> ? C'est open source ! vous pouvez le trouver ici sur Github](https://github.com/bechurch/MindfulMinuteDemo)

>  Je n'écris que sur la programmation et le travail à distance. Si vous [me suivez sur Twitter](https://www.twitter.com/bnchrch), je ne perdrai pas votre temps.