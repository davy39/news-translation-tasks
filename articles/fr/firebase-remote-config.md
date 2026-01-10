---
title: Qu'est-ce que Firebase Remote Config ?
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2023-10-03T15:44:31.000Z'
originalURL: https://freecodecamp.org/news/firebase-remote-config
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/rima-kruciene-gpKe3hmIawg-unsplash.jpg
tags:
- name: Cloud Services
  slug: cloud-services
- name: configuration
  slug: configuration
- name: Firebase
  slug: firebase
seo_title: Qu'est-ce que Firebase Remote Config ?
seo_desc: Remote configurations are useful because they allow you to alter the behavior
  in your application without having to release a new version of the app. One prominent
  example is using remote configurations to decide if a feature should be turned on
  or o...
---

Les configurations à distance sont utiles car elles vous permettent de modifier le comportement de votre application sans avoir à publier une nouvelle version de l'app. Un exemple prominent est l'utilisation des configurations à distance pour décider si une fonctionnalité doit être activée ou désactivée. Ainsi, vous pouvez la déployer progressivement en production ou la tester pour voir comment les utilisateurs réagissent.

Si vous souhaitez que votre application dispose de cette fonctionnalité, vous devriez généralement construire votre serveur et sa logique. Mais nous vivons maintenant à une époque d'innovation technologique, et des outils ont été créés pour vous aider à minimiser votre temps de développement.

Cet outil s'appelle Firebase Remote Config — un service cloud qui vous permet de modifier différentes fonctionnalités de votre application sans publier de mises à jour ou demander aux utilisateurs de mettre à jour l'app.

## Aperçu

Vous pouvez accéder à la fonctionnalité Remote Config dans la console Firebase de votre projet. Elle se trouve généralement sous la section Release & Monitor dans la barre latérale de gauche.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-6.png)

Il existe deux façons de définir vos configurations à distance :

1. En utilisant Firebase.
2. En utilisant un fichier de modèle au format JSON.

Nous nous concentrerons sur la première option, car la deuxième option est une approche moins intuitive.

Firebase Remote Config vous permet de définir une ou plusieurs clés lors de la configuration. Les clés peuvent être des types suivants :

* Chaîne de caractères
* Nombre
* Booléen
* JSON

Ces clés sont utilisées comme configurations pour votre application. Par exemple, si vous avez une fonctionnalité dans votre application que vous souhaitez contrôler via des configurations à distance, vous pourriez définir une clé booléenne intitulée enableFeatureX.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-7.png)

Chaque clé que vous définissez a quelques autres paramètres qui peuvent vous être utiles. Par exemple, vous pouvez définir une valeur par défaut pour une clé (par exemple, false peut être la valeur par défaut d'une clé booléenne) ou la faire utiliser une valeur que vous avez définie dans votre application.

Une autre chose intéressante que vous pouvez faire, en cliquant sur le bouton Add new dans l'image ci-dessus, est de définir la valeur d'une clé en fonction de certains facteurs. Vous verrez ces options lorsque vous cliquerez sur le bouton :

* Valeur conditionnelle.
* Expérience.
* Personnalisation.

Une fois que vous avez terminé d'ajouter une clé, assurez-vous de publier vos modifications pour qu'elles soient déployées.

## L'option Valeur conditionnelle

Vous pouvez configurer comment une valeur sera définie pour des utilisateurs spécifiques en fonction de diverses conditions.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-8.png)

Ici, vous pouvez décider ce que vous voulez tester et comment. Vous découvrirez plusieurs options lorsque vous cliquerez sur le menu déroulant "Applies if".

Pour illustrer l'utilisation de cette fonctionnalité, disons que vous souhaitez cibler les utilisateurs iOS aux États-Unis. Vous pouvez le faire en utilisant le menu déroulant "Applies if" et en choisissant Platform puis iOS.

Après cela, vous pouvez appuyer sur le bouton "and" pour ajouter une condition pour Country/Region et choisir United States.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-9.png)

Assurez-vous également de nommer votre condition, sinon le bouton Create condition ne sera pas activé.

Remarquez comment le dernier champ de la fenêtre de définition d'une nouvelle condition vous indique combien d'utilisateurs seront affectés par cette condition ? C'est une fonctionnalité assez intéressante.

## L'option Expérience

Cette option vous permet de modifier le comportement d'une valeur dans vos configurations à distance avant qu'elle ne prenne effet sur tous vos utilisateurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-10.png)

Vous pouvez suivre ces étapes pour configurer l'option expérience :

* Dans la première étape, vous devez remplir le nom et la description de votre expérience.
* Ensuite, vous devez choisir quelle application cibler et combien d'utilisateurs seront affectés (en pourcentage) dans la deuxième étape.
* La troisième étape consiste à configurer les métriques pour mesurer cette expérience. Il existe deux types — les métriques principales et les métriques supplémentaires.
* Enfin, vous pouvez décider du nombre de groupes de test A/B pour cette expérience.

## L'option Personnalisation

Dernière mais non des moindres est l'option de personnaliser une valeur spécifique de vos configurations à distance pour un utilisateur en fonction de son propre comportement.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-11.png)

Vous pouvez définir des valeurs que l'algorithme peut fournir à l'utilisateur en fonction de son comportement. Celles-ci seront choisies par un objectif que vous définissez (Étape 2). Cet objectif peut varier du temps d'engagement de l'utilisateur au nombre de clics qu'il effectue. Dans l'Étape 3, vous définissez une condition qui ciblera les utilisateurs afin qu'ils deviennent personnalisés. Enfin, dans l'Étape 4, vous ajoutez le nom et la description de cette personnalisation.

Chaque option a beaucoup plus à offrir que ce que j'ai décrit ici, donc si vous voulez en savoir plus, vous pouvez utiliser l'un des liens de référence en bas. Maintenant que nous comprenons ce qu'est Remote Config, voyons comment nous pouvons l'ajouter à notre application.

## Comment configurer Firebase Remote Config

Avant de pouvoir faire quoi que ce soit lié à l'application des configurations à distance, vous devez vous assurer d'avoir ajouté Firebase à votre projet Android. Cela a été documenté [ici](https://firebase.google.com/docs/android/setup?authuser=0).

Après avoir fait cela, suivez ces étapes :

### Étape #1 - Ajoutez la bibliothèque de configuration à distance Firebase à votre projet dans votre fichier build.gradle de l'application

```
 implementation 'com.google.firebase:firebase-config-ktx'
```

Il existe une option pour importer également le module Firebase Analytics, mais il n'est pas requis pour les configurations à distance. Il est utilisé dans d'autres domaines des configurations à distance, comme la définition d'une condition basée sur un événement spécifique.

### Étape #2 - Utilisez l'objet `RemoteConfig`

Après avoir synchronisé votre projet, vous pouvez accéder à l'objet `RemoteConfig` avec cette commande :

```kotlin
val remoteConfig: FirebaseRemoteConfig = Firebase.remoteConfig
```

### Étape #3 - Définir l'intervalle de récupération

Vous pouvez définir la fréquence à laquelle vos configurations à distance seront récupérées et mises à jour. Lorsque vous développez encore votre application, il est plus idéal de définir ce nombre relativement bas.

```kotlin
val remoteConfigSettings = remoteConfigSettings {                             minimumFetchIntervalInSeconds = 2000
}
```

Si vous définissez `**minimumFetchIntervalInSeconds**` trop bas, Firebase lancera une `FirebaseRemoteConfigFetchThrottledException`, donc utilisez un nombre bas uniquement lorsque vous testez des choses.

### Étape #4 - Configurer la configuration pour la configuration à distance

Vous pouvez configurer la configuration à distance en utilisant le code ci-dessous :

```kotlin
remoteConfig.setConfigSettingsAsync(remoteConfigSettings)
```

### Étape #5 - Définir les valeurs par défaut

Vous pouvez avoir des valeurs par défaut pour vos configurations à distance. Celles-ci peuvent être créées sous forme de fichier XML dans le répertoire XML à l'intérieur du dossier res. Voici à quoi ressemble le code :

```kotlin
:remoteConfig.setDefaultsAsync(R.xml.remote_config_defaults)
```

Ce fichier XML doit avoir un élément sous-jacent de type map pour envelopper toutes vos valeurs par défaut. Par exemple, imaginons que nous avons défini une clé dans les configurations à distance appelée `my_key`, dont la valeur est `1`. Le XML pour les valeurs par défaut ressemblera à ceci :

```xml
<?xml version="1.0" encoding="utf-8"?>
<defaultsMap>
   <entry>      
      <key>my_key</key>     
      <value>1</value>   
    </entry>
</defaultsMap>
```

Les configurations à distance doivent être récupérées et activées. L'action de récupération récupère et stocke vos configurations à distance dans l'objet Remote Config. La partie activation consiste à rendre ces valeurs disponibles pour votre application. C'est pourquoi il existe deux méthodes d'API :

* `fetch` (et utiliser plus tard activate)

```kotlin
remoteConfig.fetch().addOnCompleteListener { task ->               if                if (task.isSuccessful) {     
              //Remote Configurations fetch successfully          
           }         
        }.addOnFailureListener { error ->             
				//Remote Configurations fetch failure            
       }
-------------------------
remoteConfig.activate().addOnCompleteListener { task ->  
if (task.isSuccessful) {
		//Remote Configurations activation success   
        }  
   }.addOnFailureListener { error -> 
   			//Remote Configurations activation failure
  }
```

* `fetchAndActivate`

```kotlin
remoteConfig.fetchAndActivate().addOnCompleteListener { task ->                				if (task.isSuccessful) {     
				//Remote Configurations fetched and activated successfully                }        
       }.addOnFailureListener { error ->           
       //Remote Configurations fetched and activated failure    
     }
```

### Étape #6 - Accéder aux configurations

Maintenant que nos configurations à distance ont été récupérées et activées, nous pouvons y accéder et les utiliser dans notre application. Nous pouvons le faire en accédant à l'objet `remoteConfig` et en utilisant l'une des méthodes getter selon le type de la valeur que nous avons définie :

```kotlin
val myRemoteConfigValue: String = remoteConfig.getString("my_key")
```

## Conclusion

Puisque votre application dépendra des configurations à distance pour son fonctionnement (ou certaines parties), il est crucial de décider comment l'application se comportera si elle n'arrive pas ou met trop de temps à recevoir une réponse.

En essence, il existe deux façons de gérer le chargement des configurations à distance :

1. Votre application démarre et attend que les configurations à distance soient activées.
2. Votre application démarre et n'attend pas que la configuration à distance soit activée. Elle opte plutôt pour utiliser les configurations à distance lors du deuxième lancement de l'application.

Il est important de comprendre qu'il n'y a pas d'option préférable à l'autre. Tout dépend de votre cas d'utilisation et de la manière dont vous souhaitez que l'expérience de l'utilisateur soit lors de l'utilisation de votre application. La première option garantit que, une fois votre application chargée, toutes les configurations à distance que vous avez définies seront configurées et l'expérience de l'utilisateur sera fluide après le temps de chargement initial. Si vous avez des fonctionnalités critiques qui dépendent des configurations à distance, vous devrez opter pour cette option.

D'autre part, si vos configurations à distance concernent une fonctionnalité spécifique de votre application qui n'a pas nécessairement besoin de se produire lors du premier lancement initial, vous pourriez envisager d'opter pour la deuxième option. Ainsi, votre application n'a pas besoin d'attendre que les configurations à distance soient reçues de Firebase et la logique à l'intérieur de votre application peut se produire plus tard.

Il existe des implications positives et négatives pour chacune de ces méthodes, et c'est à vous de décider laquelle est la mieux adaptée à votre application. Si vous choisissez la première option, vous pouvez ajouter un écran de chargement qui expire après une certaine période. Si vous choisissez la deuxième option, il est recommandé de créer un mécanisme par défaut pour les fonctionnalités de votre application et la manière dont elles doivent fonctionner lorsque la configuration n'a pas encore été reçue.

Il y a plus que ce que nous avons discuté dans cet article, et je vous encourage à approfondir. J'ai récemment utilisé les configurations à distance Firebase dans une application que j'ai créée pour aider les utilisateurs à planifier des rendez-vous.

Vous pouvez la consulter sur [le Google Play store](https://play.google.com/store/apps/details?id=com.tomerpacific.scheduler).

Et vous pouvez voir le code source ici :

%[https://github.com/TomerPacific/scheduler]

Si vous souhaitez lire d'autres articles que j'ai écrits, vous pouvez les trouver ci-dessous :

%[https://github.com/TomerPacific/MediumArticles]

## Références

* [Getting Started With Firebase For Android](https://firebase.google.com/docs/remote-config/get-started?platform=android)
* [Remote Config Use Cases](https://firebase.google.com/docs/remote-config/use-cases)
* [Remote Config Loading Strategies](https://firebase.google.com/docs/remote-config/loading)
* [Remote Config Personalization](https://firebase.google.com/docs/remote-config/personalization)