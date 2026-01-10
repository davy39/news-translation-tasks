---
title: Comment configurer les canaux de plateforme Flutter avec Protobuf
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-31T10:18:45.000Z'
originalURL: https://freecodecamp.org/news/flutter-platform-channels-with-protobuf-e895e533dfb7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qoKGLp8R3kVLlJ6bKlNkBw.jpeg
tags:
- name: android app development
  slug: android-app-development
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment configurer les canaux de plateforme Flutter avec Protobuf
seo_desc: 'By TruongSinh Tran-Nguyen

  This post is intermediate-advanced level. It is aimed for the audience who is going
  to write custom platform-specific code as a Flutter plugin.

  TLDR: When writing platform-specific code as Flutter plugins, you should use Pro...'
---

Par TruongSinh Tran-Nguyen

Cet article est de niveau intermédiaire à avancé. Il est destiné aux développeurs qui vont [écrire du code spécifique à une plateforme en tant que plugin Flutter](https://flutter.dev/docs/development/platform-integration/platform-channels).

TLDR : Lorsque vous écrivez du code spécifique à une plateforme en tant que plugins Flutter, vous devriez utiliser ProtoBuf pour la sécurité des types, les hautes performances et une excellente expérience de développement. Le code exemple et les 5 étapes sont disponibles sur mon [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf).

![Image](https://cdn-media-1.freecodecamp.org/images/1*qoKGLp8R3kVLlJ6bKlNkBw.jpeg)

### Le Problème

Lorsque vous écrivez du code spécifique à une plateforme en tant que plugins Flutter, l'un des points clés est le transfert de données entre le côté Dart et le côté plateforme. Sous le capot, ce ne sont que des 0 et des 1 binaires. Bien que tout le code avec lequel nous travaillons (Dart, Java/Kotlin, ObjC/Swift) soit typé, Flutter facilite donc l'utilisation de certains typages :

Cependant, en regardant le tableau ci-dessus, vous remarquerez plusieurs choses :

* La famille FlutterStandardTypedData est problématique. (Croyez-moi, j'ai été là et fait ça ?)
* Toute structure plus compliquée que ces types plus ou moins "primitifs" devra utiliser `List<dynamic>` et `Map<String, dynamic>` , dans lesquels dynamic devrait être un drapeau rouge.

Regardons mon erreur courante de casting `List` (et la même chose se produit avec `Map`) :

et à quel point il est verbeux de le faire correctement :

Ce n'est qu'un niveau supérieur `List`/`Map`, imaginez que vous devez aller profondément dans la structure de données que vous devez passer entre Dart et le code spécifique à la plateforme :

Donc, pour résumer :

* `FlutterStandardTypedData` est frustrant.
* Le casting des données est un cauchemar.
* Lorsque vous travaillez avec `List`/`Map`, nous perdons la sécurité des types (surtout avec les fautes de frappe dans les clés de `Map`, ou le refactoring de code/structure).
* `List<dynamic>` et `Map<String, dynamic>` ne sont pas particulièrement bons en termes de performance.

### La solution

[Protocol Buffers](https://developers.google.com/protocol-buffers/), alias Protobuf, est un mécanisme neutre en termes de langage, de plateforme et extensible pour la sérialisation de données structurées, qui prend en charge :

* [Dart](https://developers.google.com/protocol-buffers/docs/darttutorial) (maintenu par Google)
* [Java](https://developers.google.com/protocol-buffers/docs/javatutorial) (maintenu par Google)
* [Kotlin via les bindings Java](https://github.com/protocolbuffers/protobuf/issues/3742) (Kotlin non-JVM n'est pas encore supporté, mais ce n'est pas notre problème)
* [ObjC](https://github.com/protocolbuffers/protobuf/tree/master/objectivec) (maintenu par Google)
* [Swift](https://github.com/apple/swift-protobuf) (maintenu par Apple)

Alors, plongeons-nous !

#### Préparer le projet

Je vais créer le projet de plugin avec Kotlin et Swift (parce que je les aime), c'est la même chose pour Java et ObjC de toute façon.

```
flutter create -t plugin -i swift -a kotlin plugin_with_protobuf
```

Ensuite, vous devriez voir

```
Tout est fait !
```

```
[✓] Flutter est entièrement installé. (Channel master, v1.4.2, sur Mac OS X 10.14.3 18D109, locale en-US)
```

```
[✓] Android toolchain - développer pour les appareils Android est entièrement installé. (Android SDK version 28.0.3)
```

```
[✓] iOS toolchain - développer pour les appareils iOS est entièrement installé. (Xcode 10.2)
```

```
[✓] Android Studio est entièrement installé. (version 3.3)
```

```
[✓] VS Code est entièrement installé. (version 1.32.3)
```

```
[!] Aucun appareil connecté n'est disponible.
```

```
Exécutez "flutter doctor" pour obtenir des informations sur l'installation de composants supplémentaires.
```

```
Pour exécuter votre application, tapez :
```

```
$ cd plugin_with_protobuf/example
```

```
$ flutter run
```

```
Votre code d'application se trouve dans plugin_with_protobuf/example/lib/main.dart.
```

```
Votre code de plugin se trouve dans plugin_with_protobuf/lib/plugin_with_protobuf.dart.
```

```
Le code de la plateforme hôte se trouve dans les répertoires "android" et "ios" sous plugin_with_protobuf.
```

```
Pour modifier le code de la plateforme dans un IDE, voir https://flutter.io/developing-packages/#edit-plugin-package.
```

Maintenant, exécutez le projet pour vous assurer que tout est correct. Je suppose que vous avez déjà un appareil connecté ou un simulateur/émulateur en cours d'exécution

```
cd plugin_with_protobuf/exampleflutter run
```

Ou plus facilement, utilisez votre IDE préféré, soit VS Code ou Android Studio / IntelliJ. De toute façon, vous devriez avoir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jvE26cm-S4EfzpQWpf4a_A.png)

Le code actuel à cette étape est disponible sur [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/0).

#### Préparer les environnements

* Installer le compilateur Protobuf : `brew install protobuf` sur Mac, ou voir les instructions détaillées dans [README](https://github.com/protocolbuffers/protobuf#protocol-compiler-installation).
* Installer le plugin Swift pour le compilateur Protobuf : `brew install swift-protobuf` sur Mac, ou voir les instructions détaillées dans [README](https://github.com/apple/swift-protobuf#building-and-installing-the-code-generator-plugin).
* Installer le plugin Dart pour le compilateur Protobuf : `pub global activate protoc_plugin`
* Installer l'extension Protobuf pour les IDE

![Image](https://cdn-media-1.freecodecamp.org/images/1*RIpKgYZTMuvZ9J5mUaQq-A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*LkpfLs-ny3WZ6Wv9qSMt2g.png)

#### Créer proto

Maintenant, utilisons un IDE. J'utilise à la fois VS Code et Android Studio, mais pour celui-ci, j'utiliserai Android Studio. Ouvrez le projet `plugin_with_protobuf` (pas `plugin_with_protobuf/example`) avec Android Studio. Ensuite, créez un nouveau répertoire appelé `protos`, et créez un nouveau fichier `person.proto`

![Image](https://cdn-media-1.freecodecamp.org/images/1*e0FUBz3vtCLjRchHDvguYg.png)

Le code actuel à cette étape est disponible sur [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/1).

#### Générer proto en Dart

Vous pouvez voir à partir des deux premières lignes dans `person.proto`, exécutez les premières commandes pour générer le code Dart (vous pourriez vouloir créer les répertoires `gen` au préalable).

```
protoc --dart_out=./lib/gen ./protos/person.proto
```

Dans `pubspec.yaml`, ajoutez une dépendance pour l'environnement d'exécution Protobuf également :

Le code actuel à cette étape est disponible sur [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/2).

#### Générer proto en Swift

Similaire à l'étape 2 :

```
protoc --swift_out=./ios/Classes ./protos/person.proto
```

Dans `ios/plugin_with_protobuf.podspec`, ajoutez une dépendance pour l'environnement d'exécution Protobuf également, notez que SwiftProtobuf 1.4 nécessite un minimum iOS 9.0.

Le code actuel à cette étape est disponible sur [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/3).

#### Envoyer des données depuis Swift et recevoir en Dart

Ouvrez XCode depuis Android Studio :

![Image](https://cdn-media-1.freecodecamp.org/images/1*aYbh5McitgTRqM7sdagCdg.png)

Créez des données mock (la création de données mock est abrégée, vous pouvez voir les diffs complets sur [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/4)), sérialisez et envoyez-les à Dart.

Retournez à Android Studio, recevez et désérialisez les données :

Certains autres changements d'UI sont abrégés, vous pouvez voir les diffs complets sur [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/4). Maintenant, cela semble fonctionner.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TPtVuNPxCHYJdGEin090hA.png)

Le code actuel à cette étape est disponible sur [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/4).

#### Générer proto et envoyer des données depuis Kotlin

Contrairement aux étapes 2 et 3, les protos en Java/Kotlin peuvent être générés automatiquement depuis Gradle. Nous devons simplement utiliser `protobuf-gradle-plugin`.

Similaire à l'étape 4, créez des données mock (la création de données mock est abrégée, vous pouvez voir les diffs complets sur [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/5)), sérialisez et envoyez-les à Dart.

Et parce que nous pouvons déjà recevoir des données depuis Dart et les afficher, cela "fonctionne simplement".

![Image](https://cdn-media-1.freecodecamp.org/images/1*IYCf6njmxpJ_1qJjdwJFTw.png)

Le code actuel à cette étape est disponible sur [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/5).

### Conclusion

La communication entre Dart et le code spécifique à la plateforme, surtout lorsqu'elle implique des structures de données compliquées, devrait utiliser un outil de sérialisation sûr en termes de types et performant, tel que ProtoBuf (par exemple, [BuiltValue](https://github.com/google/built_value.dart) est plus ou moins sûr en termes de types mais pas aussi performant). Il est heureux que ProtoBuf supporte les 5 langages et outils de construction requis pour Flutter, et soit facile à intégrer.

Note finale : quel type de test unitaire / test d'intégration pensez-vous que nous devrions avoir pour cet exemple ? ?