---
title: 'Android Instant Apps 101 : ce qu''ils sont et comment ils fonctionnent'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T21:56:05.000Z'
originalURL: https://freecodecamp.org/news/android-instant-apps-101-what-they-are-and-how-they-work-8b039165ed24
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tuoH_I8zkHA2f1PuqtIcfQ.jpeg
tags:
- name: Android
  slug: android
- name: Instant Apps
  slug: instant-apps
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Android Instant Apps 101 : ce qu''ils sont et comment ils fonctionnent'
seo_desc: 'By Tomislav Smrečki

  Android Instant Apps are a cool new way to consume native apps without prior installation.
  Only parts of the app are downloaded and launched, giving the users a native look
  and feel in a couple of seconds.

  How do they work?

  First ...'
---

Par Tomislav Smrečki

Les Android Instant Apps sont une nouvelle façon passionnante de consommer des applications natives sans installation préalable. Seules certaines parties de l'application sont téléchargées et lancées, offrant aux utilisateurs une apparence et une sensation natives en quelques secondes.

#### Comment fonctionnent-ils ?

Tout d'abord, ne les confondez pas avec les Progressive Web Apps où une icône de lanceur ouvre une application web via le navigateur Chrome. Une Instant App sera réellement installée sur votre téléphone, mais sans avoir besoin de la rechercher sur le Play Store.

Les URLs web déclencheront le Google Play Store sur votre téléphone et ne récupéreront que la partie de l'application associée à l'URL demandée. Le reste de l'application n'est pas téléchargé. Ainsi, les utilisateurs peuvent rapidement profiter de l'expérience native de votre application Android.

#### Quel est le contexte ?

Eh bien, vous devez diviser votre projet Android en plusieurs modules. L'un d'eux est un module de base avec le code essentiel utilisé dans tous les autres modules (connexion API, base de données, préférences partagées, etc.). Les autres modules, appelés modules de fonctionnalités, contiennent des fonctionnalités et activités spécifiques accessibles via des URLs associées.

Supposons que vous avez une application web avec une liste de produits et une page unique de produit. Par exemple, vous pouvez lier [https://example.domain/products](https://example.domain/products) pour lancer ProductsListActivity et [https://example.domain/products/12](https://example.domain/products/12) pour lancer ProductActivity.

Pour les rendre accessibles en tant qu'activités d'Instant App, elles doivent être emballées dans des modules de fonctionnalités individuels et doivent avoir des App Links associés définis dans leurs manifestes de module. Nous les appellerons modules Produit et Liste de produits.

Maintenant, lorsqu'un utilisateur tente d'ouvrir [https://example.domain/products/12](https://example.domain/products/12), les modules Produit et Base commenceront à se télécharger et ProductActivity sera lancé.

#### Que sont les App Links et comment sont-ils définis ?

Vous avez probablement entendu parler des deep links. Ils sont définis dans le manifeste de l'application et seront enregistrés dans le système d'exploitation. Lorsqu'un utilisateur tente d'ouvrir un tel lien, le système d'exploitation demande à l'utilisateur de choisir entre ouvrir le lien dans un navigateur web ou dans votre application. Cependant, cela ne suffit pas pour les Instant Apps, vous devez aller plus loin — [App Links](https://developer.android.com/training/app-links/). Vous devez inclure la propriété **autoVerify="true"**.

```
<activity android:name=".ProductActivity"> <intent-filter android:autoVerify="true" android:order="100"> 
```

```
<action android:name="android.intent.action.VIEW" /> <category android:name="android.intent.category.DEFAULT" /> <category android:name="android.intent.category.BROWSABLE" /> 
```

```
<data android:scheme="http"      android:host="example.domain"       android:pathPrefix="/products" /> <data android:scheme="https"/> 
```

```
</intent-filter> </activity>
```

Votre application [vérifiera](https://developer.android.com/training/app-links/verify-site-associations) si les liens que vous avez spécifiés sont réellement associés à votre domaine. Pour cela, vous devez inclure le fichier **assetlinks.json** dans le dossier suivant de la racine de votre domaine :

[**https://example.domain/.well-known/assetlinks.json.**](https://example.domain/.well-known/assetlinks.json.)

Remarquez également la propriété **android:order="100"**. Il s'agit en fait d'une priorité dans ce cas. Si vous avez une liste de produits et un produit unique correspondant au même chemin **(/products et /products/10)**, l'activité de produit unique sera lancée s'il y a un identifiant après le chemin **/products**. Sinon, l'activité de liste de produits est lancée.

Il est très important de définir cela. Si deux activités correspondent au même chemin, le Play Store ne saura pas quelle partie de l'application doit être récupérée.

#### Associez votre application à votre domaine

Le fichier **assetlinks.json** devra contenir vos empreintes SHA256 du keystore. Le champ de relation est défini sur la valeur par défaut ci-dessous, et l'objet cible doit être rempli avec des données spécifiques à l'application et votre empreinte SHA256 du keystore.

```
[{   "relation": ["delegate_permission/common.handle_all_urls"],  "target": {   "namespace": "android_app",   "package_name": "com.example.app",   "sha256_cert_fingerprints":["00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00"]   } }]
```

Lorsque **autoVerify=true** fait son travail, tous les App Links associés lanceront directement votre application. Si vous n'avez pas l'application installée, l'Instant App sera téléchargée à la place.

Voici un exemple d'une application de démonstration que nous avons réalisée récemment. Lorsque vous cliquez sur le lien associé, un écran comme celui-ci s'ouvre et propose d'utiliser l'Instant App à la place. Remarquez à quelle vitesse l'application s'ouvre, et sur Oreo, c'est encore plus rapide.

#### Comment définir les modules Android Instant ?

Pour une Instant App, votre projet se composera d'au moins trois modules différents. Vous devez utiliser Android Studio 3.0 pour cela. Si vous créez votre application à partir de zéro, il y a une option pour activer le support des Instant Apps pour votre projet.

Tous les modules suivants seront initialisés automatiquement. Si vous modifiez une ancienne application, vous devrez diviser l'ancien module de l'application en un seul module de base et plusieurs modules de fonctionnalités. De plus, vous devrez créer un module App et un module Instant App, que vous utiliserez pour construire les APKs de l'application régulière et de l'Instant App.

**Module App**

Tout d'abord, vous devez créer un module App qui définit les dépendances pour tous les autres modules (module de base + modules de fonctionnalités). Dans le fichier build.gradle de ce module, vous devrez définir ce qui suit :

```
apply plugin: 'com.android.application' ...
```

```
dependencies {   implementation project(':product')   implementation project(':productlist')   implementation project(':base') }
```

**Module de base**

Dans ce module, vous définirez les déclarations de dépendance suivantes. Assurez-vous également que le plugin **'com.android.feature'** est appliqué ici.

```
apply plugin: 'com.android.feature' android {  baseFeature true   ... } 
```

```
dependencies {   api 'com.android.support:appcompat-v7:26.0.1'   api 'com.android.support.constraint:constraint-layout:1.0.2'  implementation 'com.google.firebase:firebase-appindexing:11.0.4'  application project(':app')   feature project(':product')   feature project(':productlist') }
```

Notez que ici, les déclarations compile deviennent des déclarations API pour les dépendances régulières que nous avons utilisées auparavant. Les projets d'application et les projets de fonctionnalités sont définis séparément.

**Module de fonctionnalités**

Ce module aura le paramètre suivant, également avec le plugin **com.android.feature** appliqué.

```
apply plugin: 'com.android.feature' ... dependencies {   implementation project(':base')   ... }
```

Vous devez indiquer quel module est votre module de base et l'inclure avec la déclaration de projet d'implémentation. Ensuite, vous pouvez inclure les dépendances nécessaires uniquement pour ce module spécifique. Par exemple, si vous utilisez une bibliothèque d'animation qui n'est pas utilisée dans aucun des autres modules.

**Module Instant App**

Enfin, il y a maintenant un plugin **com.android.instantapp** à inclure dans le fichier **build.gradle** pour le module instantapp.

```
apply plugin: 'com.android.instantapp' dependencies {   implementation project(':product')   implementation project(':productlist')   implementation project(':base') }
```

Dans ce module, nous définirons quels modules seront construits en tant qu'Instant Apps. Le résultat de la construction du module instantapp est un fichier zip avec les APKs de l'Instant App que vous pouvez télécharger séparément sur le Google Play Store dans le gestionnaire de publication des Android Instant Apps. Ces APKs sont gérés de manière similaire aux APKs réguliers, ils ont leur propre historique de déploiement et de version.

C'est tout ! Il est assez simple de commencer à développer des Android Instant Apps. Mais, il y a toujours un mais !

#### Quels étaient les défis des Android Instant Apps ?

Tout d'abord, les Instant Apps ne sont pas activées par défaut pour le moment. Si vous voulez les essayer, vous devez vérifier les paramètres de votre téléphone sous le compte Google et activer le paramètre Instant Apps.

Ensuite, nous avons constaté qu'il est extrêmement important de spécifier les données des App Links dans le format suivant :

```
<intent-filter android:autoVerify="true"> ... <data android:scheme="http"   android:host="example.domain"   android:pathPrefix="/products" /> <data android:scheme="https"/> </intent-filter>
```

Les schémas http et https doivent être définis comme montré dans cet extrait de code. Toute autre méthode provoquerait un échec de vérification du lien et l'application ne serait pas correctement liée.

De plus, il est recommandé d'inclure l'extrait de code suivant dans l'une des activités de votre manifeste d'application. Cela indique quelle activité doit être lancée si l'Instant App est lancée à partir des Paramètres ou d'un lanceur système.

```
<meta-data  android:name="default-url" android:value="https://example.domain" />
```

La documentation officielle indique que Google Search proposerait l'annotation Instant App par défaut (petite icône de foudre), mais nous avons eu des problèmes avec cela. Pour notre application de démonstration, ce n'était pas le cas. Les résultats de Google Search n'ont pas annoté nos liens de démonstration comme des Instant Apps et les liens menaient à la page web. Ce n'est que lorsque nous avons tenté d'ouvrir le lien associé à partir d'une autre application, comme Gmail, que le processus complet de l'Instant App a été déclenché et que l'Instant App a été lancée. Avez-vous rencontré des problèmes similaires ?

#### Conclusion

Lorsque cela a été annoncé pour la première fois il y a deux ans, j'étais très enthousiaste à propos des Android Instant Apps. Elles répondent au problème des utilisateurs devant rechercher les applications sur le Store et attendre qu'elles soient téléchargées pour commencer à les utiliser. Les applications web sont beaucoup plus accessibles à cet égard et la facilité de découverte est bien meilleure.

Les Instant Apps se rapprochent vraiment de combler cet écart entre les applications web et les applications mobiles natives. Elles fonctionnent déjà très bien et je pense qu'elles deviendront plus populaires avec le temps. Les principaux problèmes que nous avons rencontrés étaient une communauté plutôt petite et le manque de documentation appropriée, mais la situation à cet égard s'améliore également.

Nous aimerions avoir de vos nouvelles si vous avez essayé de les utiliser ou si vous avez rencontré des défis lors de leur mise en œuvre !

_Publié à l'origine sur [www.bornfight.com](https://www.bornfight.com/blog/android-instant-apps-101/)._