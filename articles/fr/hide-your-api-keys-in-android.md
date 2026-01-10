---
title: Comment cacher vos clés API dans une application Android
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2023-01-16T21:03:19.000Z'
originalURL: https://freecodecamp.org/news/hide-your-api-keys-in-android
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/oleg-didenko-lMNo9SwBN_o-unsplash.jpg
tags:
- name: Android
  slug: android
seo_title: Comment cacher vos clés API dans une application Android
seo_desc: 'Let''s say that you are using a version control system and your project
  uses services that require API keys. Everything is all good when they''re on your
  local machine, but you don’t want to share these API keys with the world.

  So how can you still pre...'
---

Supposons que vous utilisiez un système de contrôle de version et que votre projet utilise des services nécessitant des clés API. Tout va bien lorsqu'elles sont sur votre machine locale, mais vous ne voulez pas partager ces clés API avec le monde.

Alors, comment pouvez-vous préserver vos clés API au sein de votre application tout en les cachant lorsque vous téléchargez votre code vers votre dépôt ?

Vous voulez probablement pouvoir utiliser vos clés API de manière normale dans vos applications, mais sans les exposer.

## Qu'est-ce que les Secrets ?

C'est là que les **secrets** interviennent. Similaires à ceux que vous gardez pour vous seul, mais d'une manière développeuse.

Les secrets peuvent représenter des informations cruciales nécessaires au fonctionnement de votre application, mais qui ne doivent pas être visibles par quiconque travaillant en dehors du projet.

Cela peut être des clés API ou des jetons d'autorisation, mais en essence, un secret est toute information d'autorisation qui ne doit être utilisée que par vous et vous seul. C'est similaire à ne pas vouloir partager votre mot de passe pour un site web avec quelqu'un d'autre.

⚠️ Avertissement : Soyez conscient que la solution fournie dans cet article fonctionne pour ne pas exposer vos secrets depuis votre système de contrôle de version. Mais comme ils font partie de votre application, ils peuvent toujours être découverts en décompilant votre APK.

## Comment garder vos secrets en sécurité

Dans votre projet, vous devriez avoir un fichier **local.properties** sous le répertoire racine de votre projet.

Pour vous assurer qu'il est ignoré par votre système de contrôle de version, ouvrez le fichier .gitignore et vérifiez qu'il s'y trouve :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/1_Br5FcOmNI-SVp7QxWM3FYA.jpeg)

Vous devrez importer dans votre projet le [plugin Gradle Secrets](https://github.com/google/secrets-gradle-plugin).

Pour ce faire, allez dans le fichier build.gradle racine de votre projet et collez la ligne suivante :

```kotlin
buildscript {
    dependencies {
        id 'com.google.android.libraries.mapsplatform.secrets-gradle-plugin' version '2.0.1' apply false
    }
}
```

Ensuite, allez dans le fichier build.gradle de votre application et collez la ligne suivante :

```kotlin
plugins {
    ...
    id 'com.google.android.libraries.mapsplatform.secrets-gradle-plugin'
}
```

Ajoutez votre clé API à l'intérieur du fichier local.properties :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/1__T-HkbD9isK3IuCLdE1v5w.jpeg)

Vous pouvez utiliser votre secret dans votre fichier **AndroidManifest.xml** en ajoutant une balise meta-data à l'intérieur de votre balise application :

```xml
<application
        android:allowBackup="true" 
        .....
                                     >
    <activity>
      ....
    </activity>
      <meta-data
            android:name="NOM_DE_VOTRE_CLE_API"     /// Choisissez une valeur ici
            android:value="${NOM_CLE_API}"/>    /// Écrivez le nom que vous avez donné dans votre fichier local.properties
</application>
```

Pour accéder à votre clé API, vous pouvez utiliser le PackageManager pour obtenir les métadonnées :

```kotlin
val applicationInfo: ApplicationInfo = application.packageManager
                .getApplicationInfo(application.packageName, PackageManager.GET_META_DATA)
val apiKey = applicationInfo.metaData["NOM_DE_VOTRE_CLE_API"]
```

Alternativement, vous pouvez également utiliser l'objet BuildConfig pour l'obtenir :

```kotlin
BuildConfig.NOM_DE_VOTRE_CLE_API
```

C'est tout. Maintenant, vous pouvez être tranquille en sachant que vos secrets ne seront pas exposés par votre système de contrôle de version.

Profitez de garder vos secrets. 🔑

J'ai utilisé cela dans l'un de mes projets récents, et vous pouvez voir le code source (sans les secrets) [ici](https://github.com/TomerPacific/movies-presenter).

Et si vous voulez consulter d'autres articles que j'ai écrits, vous pouvez aller [ici](https://github.com/TomerPacific/MediumArticles).