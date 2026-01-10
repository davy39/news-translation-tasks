---
title: Tutoriel Flutter – Comment migrer vers V2 Embedding
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-01-29T18:35:05.000Z'
originalURL: https://freecodecamp.org/news/flutter-migrating-to-v2-embedding
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/nick-fewings-J54DjpXYJuE-unsplash.jpg
tags:
- name: Android
  slug: android
- name: Flutter
  slug: flutter
seo_title: Tutoriel Flutter – Comment migrer vers V2 Embedding
seo_desc: If you hopped on the Flutter bandwagon in it’s early days, most likely you
  have a project or two that were created prior to version 1.12 of Flutter. If that
  is the case, you may have seen this message whenever you run Pub get in one of your
  projects:...
---

Si vous avez rejoint le mouvement Flutter dans ses premiers jours, il est probable que vous ayez un projet ou deux qui ont été créés avant la version 1.12 de Flutter. Si c'est le cas, vous avez peut-être vu ce message chaque fois que vous exécutez Pub get dans l'un de vos projets :

> Cette application utilise une version obsolète de l'intégration Android.  
> Pour éviter les échecs d'exécution inattendus, ou les échecs de build futurs, essayez de migrer cette application vers l'intégration V2.  
>   
> Consultez la documentation pour migrer une application : [https://github.com/flutter/flutter/wiki/Upgrading-pre-1.12-Android-projects](https://github.com/flutter/flutter/wiki/Upgrading-pre-1.12-Android-projects)

Maintenant, le document lui-même contient les étapes à suivre pour faire disparaître cet avertissement, mais il ne clarifie pas toujours ce qu'il faut changer et où. 

Cet article vous guidera étape par étape pour migrer votre application Flutter vers V2 Embedding afin que vous puissiez faire disparaître cet avertissement pour de bon.

## Migration automatique – La solution facile

Il faut dire que vous pouvez éviter ce processus de migration si votre application peut être facilement recréée. Alors, que signifie cela ? 

Eh bien, si le code de votre application n'est pas complexe, vous pouvez simplement sauvegarder les fichiers dans votre dossier lib et créer un nouveau projet en utilisant **`flutter create`**. Ainsi, vous aurez un projet déjà migré vers V2 Embedding et il vous suffira de copier-coller le code que vous avez dans votre dossier lib.

Mais, si votre projet est plus complexe – disons qu'il s'agit d'un package qui contient du code spécifique à la plateforme – vous serez probablement mieux loti en le migrant manuellement.

## Migration manuelle – Suivez ces étapes

1. Ouvrez le fichier **MainActivity**.kt (ou .java) dans votre application
2. Vous devez supprimer tout le contenu de ce fichier et le laisser vide avec une déclaration de classe (sauf si vous avez une logique spécifique là).
3. Supprimez toutes les imports et assurez-vous d'avoir une import qui est celle-ci :

```java
import io.flutter.embedding.android.FlutterActivity;
```

Le résultat final devrait être le suivant :

```java
import io.flutter.embedding.android.FlutterActivity;
public class MainActivity extends FlutterActivity {   
    // Rien ne devrait être ici
}
```

4.  Ouvrez le fichier AndroidManifest.xml et changez l'attribut name sous la balise application en **`${applicationName}`** – pour qu'il ressemble à ceci : 

```xml
<application      
    android:name="${applicationName}"> 
     .... 
</application>
```

5.  Vous devez ajouter les métadonnées suivantes à l'intérieur de vos balises application :

```xml
<meta-data           
     android:name="flutterEmbedding"       
     android:value="2" />
```

6.  Si vous souhaitez un comportement spécifique pour l'écran de démarrage, vous devrez supprimer la balise meta de l'écran de démarrage :

```xml
<meta-data                     android:name="io.flutter.app.android.SplashScreenUntilFirstFrame"                android:value="true" />
```

7.  Ensuite, allez dans votre fichier styles.xml et configurez le LaunchTheme là avec le drawable de votre choix :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>    
 	<style name="LaunchTheme" parent="@android:style/Theme.Black.NoTitleBar">        <item name="android:windowBackground">@drawable/launch_background
    	</item>   
    </style>
</resources>
```

Votre AndroidManifest.xml ressemblera à ceci après toutes les modifications ci-dessus :

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"    package="PACKAGE_NAME">
<application        
	android:name="${applicationName}"    
    android:label="APPLICATION_LABEL"      
    android:icon="@mipmap/ic_launcher">     
    	<activity           
        	android:name=".MainActivity"
            android:exported="true"   
            android:launchMode="singleTop"     android:theme="@style/LaunchTheme"            	android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"            android:hardwareAccelerated="true"            android:windowSoftInputMode="adjustResize">     
            	<intent-filter>    
                	<action android:name="android.intent.action.MAIN"/>                				<category android:name="android.intent.category.LAUNCHER"/>  
                    </intent-filter>     
       </activity>     
       <meta-data       
       		android:name="flutterEmbedding"         
            android:value="2" /> 
 </application>
</manifest>
```

## Support AndroidX

Votre projet pourrait également devoir être migré pour utiliser les bibliothèques AndroidX au lieu des anciennes bibliothèques de support. Vous en serez averti lorsque vous construirez et exécuterez votre application :

> Votre application n'utilise pas AndroidX. Pour éviter les échecs de build potentiels, vous pouvez rapidement migrer votre application en suivant les étapes sur [https://goo.gl/CP92wY](https://goo.gl/CP92wY).

Corriger cela est plutôt simple, car Android Studio dispose d'un support intégré pour migrer vers AndroidX.

Commencez par ouvrir le dossier Android de votre application Flutter en tant que projet autonome

Cliquez sur Refactor → Migrate to AndroidX :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/migration.jpg)
_Menu déroulant pour migrer vers AndroidX_

Vous serez alors invité à sauvegarder une copie de votre projet et, après cela, le processus de migration aura lieu.

### Erreurs que vous pourriez rencontrer

Lors de ce processus de migration, vous pourriez rencontrer plusieurs erreurs lors de la construction de votre application. Les plus importantes sont :

* _Unable to get mutable Windows environment variable map_
* _cvc-complex-type.2.4.a: Invalid content was found starting with element ‘base-extension’. One of ‘{layoutlib}’ is expected_
* _Warning: This version only understands SDK XML versions up to 2 but an SDK XML file of version 3 was encountered. This can happen if you use versions of Android Studio and the command-line tools that were released at different times_

Les deux premières erreurs sont liées entre elles et proviennent toutes deux de la même cause racine. C'est parce que votre projet a été configuré avec une ancienne version de Gradle et qu'il est nécessaire de la mettre à niveau. 

Pour ce faire, suivez ces étapes :

1. Ouvrez le dossier Android dans votre application Flutter en tant que projet autonome
2. Cliquez sur File → Project Structure :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/migration-1.jpg)
_Menu déroulant pour sélectionner Project Structure_

3.  Changez la version de Gradle pour quelque chose de plus récent et qui correspond à la version actuelle d'Android Studio que vous utilisez

![Image](https://www.freecodecamp.org/news/content/images/2024/01/migration-2.jpg)
_Écran de configuration AGP et Gradle_

Vous pouvez également utiliser l'AGP Upgrade Assistant pour cela en allant dans Tools → AGP Upgrade Assistant :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/migration-3.jpg)
_Menu déroulant pour mettre à niveau AGP en utilisant l'AGP Upgrade Assistant_

Le troisième problème, qui est un avertissement, peut être causé par une ancienne version des outils Android SDK. Pour apprendre comment faire cela, vous pouvez aller [ici](https://developer.android.com/studio/intro/update#sdk-manager).

Votre projet devrait maintenant être entièrement migré, compilé et fonctionner sans problème. 

Si vous souhaitez lire d'autres articles que j'ai écrits, vous pouvez les consulter ici :

%[https://github.com/TomerPacific/MediumArticles]