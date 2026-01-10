---
title: Comment rendre votre package Flutter compatible avec le Privacy Manifest
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-05-20T08:10:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-flutter-package-privacy-manifest-compatible
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/tierra-mallorca-rgJ1J8SDEAY-unsplash.jpg
tags:
- name: Flutter
  slug: flutter
seo_title: Comment rendre votre package Flutter compatible avec le Privacy Manifest
seo_desc: "Beginning May 1st, Apple will enforce all new applications or updated versions\
  \ of applications that will be uploaded to the Apple Store, to include a Privacy\
  \ Manifest file. \nIf you are unfamiliar with what a Privacy Manifest is, I suggest\
  \ reading my ..."
---

À partir du 1er mai, Apple exigera que toutes les nouvelles applications ou les versions mises à jour des applications téléchargées sur l'Apple Store incluent un fichier Privacy Manifest. 

Si vous ne savez pas ce qu'est un Privacy Manifest, je vous suggère de lire mon [autre article](https://www.freecodecamp.org/news/what-the-ios-privacy-manifest-means-for-developers/).

Il y a eu beaucoup de confusion concernant ce que les développeurs doivent faire s'ils utilisent Flutter. 

C'est parce que Flutter a été marqué par Apple comme un ["SDK couramment utilisé"](https://developer.apple.com/news/?id=r1henawx#:~:text=Third%2Dparty%20SDK%20privacy%20manifest%20and%20signatures.&text=Starting%20in%20spring%202024%2C%20if,used%20as%20a%20binary%20dependency.) (y compris plusieurs autres packages Flutter). Cela a été quelque peu abordé par la communauté Flutter. Si vous êtes intéressé, vous pouvez lire les problèmes GitHub suivants :

* [Support Privacy Manifest and Required APIs in iOS and macOS](https://github.com/flutter/flutter/issues/143232?source=post_page-----52b2da5eabf3--------------------------------)
* [Determine how to handle privacy manifests in packages](https://github.com/flutter/flutter/issues/131940?source=post_page-----52b2da5eabf3--------------------------------)

En mai 2024, les choses sont encore un peu floues. Il serait préférable d'avoir une solution qui nous rassure sur la possibilité de mettre à jour notre package et de ne pas causer le rejet des applications qui l'utilisent.

Nous voulons continuer à être de bons citoyens dans l'écosystème Mobile.

## Comment mettre à jour les dépendances

Quelle que soit la logique que vous avez dans votre package, pour supporter les changements d'Apple, vous devez forcer votre package à utiliser [Flutter version 3.19](https://medium.com/flutter/whats-new-in-flutter-3-19-58b1aae242d2) au minimum. 

Vous pouvez faire cela en allant dans votre fichier `pubspec.yaml` et en changeant la version là-bas :

```yaml
environment:
  sdk: ">=3.0.0 <4.0.0"
  flutter: "^2.0.0"   /// <--- Changez ceci en 3.19
```

Ensuite, vous devez passer en revue toutes les dépendances que vous pourriez avoir dans votre fichier `pubspec.yaml` et vérifier si vous avez des packages qui sont listés sous les "SDK couramment utilisés".

Si c'est le cas, vous devrez vérifier si ce package a publié une nouvelle version avec un fichier de manifest de confidentialité. Par exemple, si le `pubspec.yaml` de notre package ressemble à ceci :

```yaml
dependencies:
  flutter:
    sdk: flutter
  intl: ^0.17.0
  shared_preferences: ^2.0.5
  url_launcher: ^6.0.17
  package_info_plus: ^3.1.2
```

notre package dépend de `url_launcher`, qui, comme il se trouve, est également listé sous les "SDK couramment utilisés". 

Lorsque nous allons sur la page de `url_launcher` sur [pub.dev](https://pub.dev/packages/url_launcher), nous pouvons voir qu'ils ont publié une nouvelle version, 6.2.6, qui inclut un manifest de confidentialité.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/1.jpg)
_Capture d'écran du package url_launcher et de sa version qui supporte le manifest de confidentialité_

Nous allons donc passer à cette version.

Une fois que nous avons passé en revue toutes nos dépendances, nous pouvons nous attaquer au code de notre propre package.

## Comment ajouter le fichier Privacy Manifest

Le fichier Privacy Manifest doit résider dans le dossier `Resources` de votre structure de projet (sous `darwin`).

![Image](https://www.freecodecamp.org/news/content/images/2024/05/1-1.jpg)
_Structure du répertoire du dossier iOS dans un package Flutter_

Assurez-vous de suivre les directives d'Apple sur les données à inclure. Cela dépendra du cas d'utilisation de votre package. Si vous n'êtes pas sûr, vous pouvez soit vous référer à la [documentation d'Apple](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files), soit consulter mon article que j'ai lié au début.

Ensuite, dans le fichier `podspec` de votre package, vous devez ajouter le manifest de confidentialité comme une ressource :

```podspec
 s.resource_bundles = {'package_name_privacy' => ['Resources/PrivacyInfo.xcprivacy']}
```

## Presque terminé

Comme indiqué, les choses ne sont pas encore claires sur le fait que les solutions proposées résisteront à l'épreuve du temps. 

Un problème qui est actuellement à l'étude est le fait que les packages Flutter sont, sous le capot, des frameworks statiques. Cela peut causer des problèmes pour les développeurs d'applications. 

Lors de l'utilisation de votre package, le fichier de manifest de confidentialité peut être obscurci par les ressources de niveau supérieur de l'application elle-même. Cela signifie que le fichier de manifest de confidentialité de l'application elle-même peut éclipser le fichier de manifest de confidentialité de votre package. Cela, à son tour, entraînera le rejet de l'application par l'Apple Store, car elle ne percevra pas que votre package dispose effectivement d'un fichier de manifest de confidentialité.

Selon [ce commentaire sur le problème GitHub](https://github.com/flutter/flutter/issues/145269?source=post_page-----52b2da5eabf3--------------------------------#issuecomment-2070221423), c'est un problème connu d'Apple et ils travaillent à le résoudre.

Dans [l'annonce d'Apple du 26 avril](https://developer.apple.com/news/?id=pvszzano), ils déclarent que :

> Les applications ne seront pas acceptées si elles ne répondent pas aux exigences de manifest et de signature. 

Les applications ne seront également pas acceptées si tout ce qui suit s'applique :

* Elles manquent une raison pour une API listée.
* Le code fait partie d'un framework dynamique intégré via la phase de construction Embed Frameworks.
* Le framework est un SDK tiers nouvellement ajouté qui est sur la liste des SDK tiers couramment utilisés.

Il semble que les choses aient été limitées aux frameworks dynamiques pour le moment, car Apple ajoute :

> _À l'avenir, ces exigences de raison requises s'étendront pour inclure l'ensemble du binaire de l'application._

## Conclusion

Espérons qu'à présent vous avez les connaissances et les outils pour vous assurer que votre package Flutter est compatible avec les changements de Privacy Manifest d'Apple. 

Mais assurez-vous de garder les yeux et les oreilles ouverts pour toute annonce d'Apple, car d'autres changements à votre package Flutter pourraient être nécessaires.