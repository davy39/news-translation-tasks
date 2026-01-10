---
title: Un guide pour créer une application Android moderne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T20:05:00.000Z'
originalURL: https://freecodecamp.org/news/kriptofolio-app-series
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rvYYjocj8-ytP2OBY_Fdpg.png
tags:
- name: Android
  slug: android
- name: Apps
  slug: apps-tag
- name: Cryptocurrency
  slug: cryptocurrency
- name: Kotlin
  slug: kotlin
- name: 'tech '
  slug: tech
seo_title: Un guide pour créer une application Android moderne
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series — Introduction

  Welcome to this series of blog posts where I will be creating a modern Android app.
  I will use the best tools and practices available in the year 2018–2019. I am doing
  this because I want to c...'
---

Par Andrius Baruckis

#### Série d'applications Kriptofolio — Introduction

Bienvenue dans cette série d'articles de blog où je vais créer une application Android moderne. J'utiliserai les meilleurs outils et pratiques disponibles en 2018–2019. Je fais cela parce que je veux couvrir tous les sujets les plus chauds dans le monde Android et acquérir des connaissances en les enseignant.

Si vous suivez cette série, vous apprendrez à développer l'application à partir de zéro. Chaque article de blog de cette série couvrira un sujet de développement spécifique dont je veux parler. Je ferai de mon mieux pour créer une application de bonne qualité et expliquer le processus de développement. Ce premier article de blog de la série est une feuille de route du projet de ce que nous allons faire.

### Contenu de la série

* Introduction : Un guide pour créer une application Android moderne en 2018–2019 (vous êtes ici)

* [Partie 1 : Une introduction aux principes SOLID](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)

* [Partie 2 : Comment commencer à construire votre application Android : création de maquettes, UI et mises en page XML](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)

* [Partie 3 : Tout sur cette architecture : exploration de différents modèles d'architecture et comment les utiliser dans votre application](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)

* [Partie 4 : Comment implémenter l'injection de dépendances dans votre application avec Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)

* [Partie 5 : Gérer les services Web RESTful en utilisant Retrofit, OkHttp, Gson, Glide et Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)

### L'application : l'idée de « Kriptofolio » (précédemment « My Crypto Coins »)

Au début, il était difficile de penser à un plan pour présenter toutes les tendances du développement Android, mais finalement, j'en ai trouvé un qui me plaisait. Il est lié à mon immense domaine d'intérêt — la blockchain et les cryptomonnaies. J'ai décidé de créer une application qui contiendrait votre portefeuille de cryptomonnaies et vous indiquerait leur valeur convertie en monnaie fiduciaire.

L'important pour l'utilisateur est que cette application garantira une confiance à 100 %. Elle ne nécessitera aucun processus de connexion/enregistrement. Elle ne collectera pas les données des utilisateurs en les envoyant au serveur. Je suppose que personne ne se sentirait à l'aise de partager des informations en ligne sur l'argent possédé.

Les données fournies par les utilisateurs sur les investissements en cryptomonnaies ne seront stockées que dans une base de données locale conservée dans un appareil Android. Cependant, pour connaître la valeur du portefeuille convertie en monnaie fiduciaire, l'application utilisera Internet pour obtenir les derniers taux de conversion.

Ainsi, comme vous pouvez le voir, à des fins de formation, cette idée d'application est excellente. Elle vous met techniquement au défi d'essayer différentes approches pour travailler avec les données. C'est l'une des compétences les plus importantes à connaître pour construire des applications modernes. Le sujet de l'argent est si sensible pour les gens. Pour garantir encore plus de confiance, je développerai cette application ouvertement en créant cette série d'articles de blog et en rendant le code du projet disponible afin que tout le monde puisse voir qu'il n'y a rien à cacher.

### Que allons-nous utiliser ?

Tout d'abord, pour créer cette application, nous devons connaître les différents prix des cryptomonnaies à l'instant présent. Ces données seront fournies depuis Internet car elles changent continuellement.

#### API de données :

[CoinMarketCap](https://coinmarketcap.com/) — l'un des sites web les plus populaires pour obtenir un aperçu du marché des cryptomonnaies. Ce site propose une [API](https://coinmarketcap.com/api) gratuite que tout le monde peut utiliser et qui nous convient parfaitement en tant que fournisseur de services de données.

Ensuite, j'ai dressé une liste des choses les plus significatives en vogue dans le monde Android qui conviennent à ce projet et qui devraient être utilisées.

#### Langage de programmation :

[Kotlin](https://kotlinlang.org/) — un langage officiel sur Android. Il est expressif, concis et puissant. Le meilleur de tout, il est interopérable avec les langages et le runtime Android existants.

L'introduction de ce nouveau langage était l'un des sujets les plus chauds en 2017 pour Android. Notre application doit être écrite dans ce langage. Je parle également de Kotlin et de ses fonctionnalités dans mon ancien article de blog « [Apprenons Kotlin en construisant une application de calculatrice Android](https://medium.com/mindorks/learn-kotlin-android-calculator-app-b86b275cc27c) ».

#### Environnement de développement intégré (IDE) :

[Android Studio](https://developer.android.com/studio) — l'IDE officiel pour Android. Il fournit les outils les plus rapides pour construire des applications sur chaque type d'appareil Android. Il n'y a pas de meilleures alternatives pour développer des applications natives. C'est notre choix principal pour un IDE sans aucune question.

#### Système de gestion de construction de projet :

[Gradle](https://gradle.org/) — est un système de gestion de construction avancé à usage général basé sur Groovy et Kotlin. Il supporte le téléchargement et la configuration automatiques des dépendances ou d'autres bibliothèques. C'est le système de construction recommandé par Google. Il est bien intégré dans Android Studio, donc nous allons l'utiliser.

#### Architecture :

[Composants d'architecture Android](https://developer.android.com/topic/libraries/architecture) — une collection de bibliothèques qui vous aident à concevoir des applications robustes, testables et maintenables.

[Modèle–Vue–ViewModel (MVVM)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel) — un modèle architectural. Le concept est de séparer la logique de présentation des données de la logique métier en la déplaçant dans une classe particulière pour une distinction claire. L'équipe Android pousse ce modèle comme choix par défaut. C'est aussi une alternative aux modèles [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) et [MVP](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter) populaires.

Je parlerai séparément dans cette série de ce choix de modèle, d'autres options d'architecture et de la manière d'organiser notre code en général. C'est essentiel si nous voulons construire un projet solide et facilement maintenable.

[Coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html) — un modèle de conception de concurrency que vous pouvez utiliser sur Android pour simplifier le code qui s'exécute de manière asynchrone.

#### Persistance des données :

[Base de données SQLite](https://developer.android.com/training/data-storage/sqlite) — c'est une base de données SQL open source qui stocke les données de manière persistante dans un fichier texte sur un appareil. Android est livré avec une implémentation intégrée de la base de données SQLite. SQLite supporte toutes les fonctionnalités des bases de données relationnelles.

[Shared Preferences](https://developer.android.com/reference/android/content/SharedPreferences) — une API du SDK Android pour stocker et récupérer les préférences de l'application. Les SharedPreferences sont simplement des ensembles de valeurs de données stockées de manière persistante. Il vous permet de sauvegarder et de récupérer des données sous forme de paires clé-valeur.

#### Bibliothèques :

[Composants *Android Jetpack*](https://developer.android.com/jetpack) :

[AppCompat](https://developer.android.com/topic/libraries/support-library/packages#v7-appcompat) — c'est un ensemble de bibliothèques de support qui peuvent être utilisées pour faire fonctionner les applications développées avec des versions plus récentes avec des versions plus anciennes.

[Android KTX](https://developer.android.com/kotlin/ktx) — un ensemble d'extensions Kotlin pour le développement d'applications Android. Le but d'Android KTX est de rendre le développement Android avec Kotlin plus concis, agréable et idiomatique en tirant parti des fonctionnalités du langage telles que les fonctions/propriétés d'extension, les lambdas, les paramètres nommés et les valeurs par défaut des paramètres.

[Data Binding](https://developer.android.com/topic/libraries/data-binding) — est une bibliothèque de support qui vous permet de lier les composants de l'interface utilisateur dans vos mises en page aux sources de données dans votre application en utilisant un format déclaratif plutôt que de manière programmatique.

[Lifecycles](https://developer.android.com/topic/libraries/architecture/lifecycle) — pour gérer les cycles de vie de vos activités et fragments.

[LiveData](https://developer.android.com/topic/libraries/architecture/livedata) — est une classe de détention de données observable qui a été conçue pour aider à résoudre les défis courants du cycle de vie Android et pour rendre les applications plus maintenables et testables.

[Room](https://developer.android.com/topic/libraries/architecture/room) — il fournit une couche d'abstraction sur SQLite pour permettre un accès facile à la base de données tout en exploitant toute la puissance de SQLite.

[ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) — conçu pour stocker et gérer les données liées à l'interface utilisateur de manière consciente du cycle de vie. La classe ViewModel permet aux données de survivre aux changements de configuration tels que les rotations d'écran.

*Autres :*

[ConstraintLayout](https://developer.android.com/reference/android/support/constraint/ConstraintLayout) — pour construire des mises en page flexibles et efficaces. L'éditeur de mise en page utilise des contraintes pour déterminer la position d'un élément de l'interface utilisateur dans la mise en page. Une contrainte représente une connexion ou un alignement avec une autre vue, la mise en page parente ou une ligne directrice invisible.

[CardView](https://developer.android.com/reference/android/support/v7/widget/CardView) — élément qui représente les informations sous forme de carte avec une ombre portée (élévation) et un rayon de coin qui semble cohérent sur la plateforme.

[RecyclerView](https://developer.android.com/reference/android/support/v7/widget/RecyclerView) — une version flexible et efficace de ListView. C'est un conteneur pour rendre de grands ensembles de données de vues qui peuvent être recyclées et défilées très efficacement.

*Tiers :*

[Dagger 2](https://google.github.io/dagger) — il s'agit d'un framework d'injection de dépendances entièrement statique, à temps de compilation, pour Java et Android.

[Retrofit 2](https://square.github.io/retrofit) — un client HTTP open source et sécurisé pour Android et Java. Avec Retrofit, nous pouvons composer la connexion HTTP facilement via une interface simple et expressive, comme un document d'API.

[OkHttp](http://square.github.io/okhttp) — un client HTTP moderne, rapide et efficace, open source, qui supporte HTTP/2 et SPDY.

[Gson](https://github.com/google/gson) — une bibliothèque Java open source pour sérialiser et désérialiser des objets Java vers et depuis JSON.

[Glide](https://bumptech.github.io/glide) — une bibliothèque de chargement d'images rapide et efficace pour Android, axée sur le défilement fluide. Glide offre une API facile à utiliser, un pipeline de décodage de ressources performant et extensible, et un regroupement automatique des ressources.

### Configuration d'un nouveau projet

Nous allons créer ce projet à partir de zéro. Je vais donc lancer Android Studio, créer un nouveau projet, le nommer « My Crypto Coins » et sélectionner « Basic Activity ». À ce stade, il n'y a rien de spécial à discuter. Notre objectif est de faire un nouveau départ, propre, et d'éviter toute complexité dans nos esprits en ajoutant des fonctionnalités supplémentaires (par exemple, la prise en charge des applications instantanées). Nous pouvons ajouter ce que nous voulons plus tard si nous le souhaitons pendant le processus de développement.

Pour commencer, incluons la prise en charge du langage Kotlin et ciblons [API 23 : Android 6.0 (Marshmallow)](https://en.wikipedia.org/wiki/Android_Marshmallow).

Pourquoi ne cible-je pas une API plus basse ou plus haute ? Admettons-le. Il est agréable de couper le support pour certains appareils plus anciens et de ne pas s'inquiéter des problèmes de compatibilité pendant le développement. De plus, je suis le fier propriétaire d'une ancienne [tablette Nexus 7 (2013)](https://en.wikipedia.org/wiki/Nexus_7_\(2013\)), qui fonctionne sous Android 6.0.1. J'espère tester mon application en direct sur celle-ci. ? Donc pour ce projet individuel, cela a influencé mon choix de SDK minimum.

De plus, comme vous l'avez remarqué, je vais demander à l'IDE d'ajouter automatiquement une activité de base générée avec la prise en charge des fragments et un bouton d'action flottant. Je pense que tout cela pourrait être utile pour notre projet.

![Image](https://cdn-media-1.freecodecamp.org/images/TVPZwad45enjSKAkTnJPRK4ld-BV1toGKXs- align="left")

***Dans Android Studio à partir de la v3.0, le plugin Kotlin est déjà intégré, il suffit de cocher la case pour ajouter la prise en charge.***

![Image](https://cdn-media-1.freecodecamp.org/images/vp5Rm1gsBRER1UbDrkcMv5LjQihJsI6cqXFT align="left")

***Sélectionnez le SDK minimum ciblé en fonction des besoins commerciaux.***

![Image](https://cdn-media-1.freecodecamp.org/images/xNcIHSD6HRUnVbKI5u42o520HMfDLu9NeM9o align="left")

***Choisissez l'activité de base qui générera un code utile pour commencer.***

![Image](https://cdn-media-1.freecodecamp.org/images/Bl0EpPhu8JPnNuDkYveUdbwqGWJurodIuhX8 align="left")

***Cochez la case pour que le contenu soit placé dans le fragment.***

[GitHub](https://github.com/) — l'un des services d'hébergement web les plus populaires pour le contrôle de version. Il s'agit d'un projet open source, et bien sûr, je vais l'utiliser.

Tous les articles de blog de cette série auront leurs commits effectués en tant que branches séparées et la branche master pour la dernière version du code source. Voici un lien vers le dépôt pour vous.

#### [Voir le code source sur GitHub](https://github.com/baruckis/Kriptofolio)

C'est tout pour le début. Si vous avez des questions, des suggestions ou des remarques à faire, n'hésitez pas à le faire dans les commentaires. Et maintenant, apprenons ensemble ! La partie 2 arrive bientôt… ?

---

***Ačiū ! Merci d'avoir lu ! J'ai initialement publié cet article pour mon blog*** [***www.baruckis.com***](https://www.baruckis.com/android/kriptofolio-app-series/) ***le 12 février 2018.***