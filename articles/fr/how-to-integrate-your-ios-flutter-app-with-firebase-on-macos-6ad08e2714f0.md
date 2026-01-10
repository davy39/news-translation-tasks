---
title: Comment intégrer votre application iOS Flutter avec Firebase sur MacOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-28T18:06:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-your-ios-flutter-app-with-firebase-on-macos-6ad08e2714f0
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e6d740569d1a4ca3d06.jpg
tags:
- name: Firebase
  slug: firebase
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment intégrer votre application iOS Flutter avec Firebase sur MacOS
seo_desc: 'By Shen Huang

  Firebase is a mobile app development platform developed by Firebase, Inc. in 2011,
  and then Acquired by Google in 2014. It provides various features such as Cloud
  Storage, Authentication and an ML kit, which are essential to developing ...'
---

Par Shen Huang

Firebase est une plateforme de développement d'applications mobiles développée par Firebase, Inc. en 2011, puis acquise par Google en 2014. Elle offre diverses fonctionnalités telles que le stockage en nuage, l'authentification et un kit ML, qui sont essentiels pour développer des applications mobiles modernes. 

De plus, elle fournit des services tels que la surveillance des performances, Crashlytics et Google Analytics pour vous aider à améliorer la qualité de vos applications.

![Image](https://cdn-media-1.freecodecamp.org/images/rdJbjlOjN0qrQOz1vVGAhz5Ndy3JltvhJWIt)
_Succès de l'application simplifié avec Firebase_

Dans ce tutoriel, je vais vous montrer comment connecter votre application iOS Flutter à la plateforme Firebase sur un ordinateur Mac, afin que vous puissiez utiliser les puissants services fournis par l'API Firebase dans vos futurs projets...

### 1. Préparer un compte Gmail et un projet Flutter

Pour utiliser les services de Firebase et de Google Cloud Platform, vous aurez besoin d'un compte Google. Si vous n'en avez pas, suivez simplement les instructions de la page [**ici**](https://accounts.google.com/signup/v2/webcreateaccount?hl=en-GB&flowName=GlifWebSignIn&flowEntry=SignUp) pour vous inscrire.

Ce tutoriel va vous montrer comment connecter votre application Flutter existante à la plateforme Firebase. Si vous êtes intéressé par la création de votre première application Flutter, j'ai un tutoriel sur [**Comment créer votre première application iOS Flutter sur MacOS**](https://medium.com/front-end-weekly/how-to-create-your-first-ios-flutter-app-on-macos-7dfa9c3e1962). À la fin de ce tutoriel, vous devriez avoir une application **_hello_world_** prête dans le simulateur et comprendre comment modifier l'application en modifiant le fichier **_main.dart_**.

### 2. Créer un projet Firebase

Pour intégrer votre application Flutter avec la plateforme Firebase, vous devez d'abord créer un projet Firebase. Voici les étapes.

1. Allez sur la [**Console Firebase**](https://console.firebase.google.com/).

2. Cliquez sur le grand bouton **Ajouter un projet**.

![Image](https://cdn-media-1.freecodecamp.org/images/bBzkYgbreUqtXjaF8gHm459WoBGG2iFVJ8zq)

3. Entrez le **Nom de votre projet**.

* J'ai utilisé **_hello-world_** pour cet exemple. Firebase ajoute automatiquement un identifiant unique à votre nom de projet — par exemple, le projet que j'ai créé a fini par s'appeler **_hello-world-f2206_**.

4. Vous pouvez choisir un emplacement pour **_Cloud Firestore_**. 

* Je l'ai laissé sur _nam5 (us-central)_ parce que je vis à Los Angeles, mais les fonctions Cloud ne sont pas disponibles sur _us-west2_, et le trafic entre les deux créera des frais supplémentaires. Vous pouvez en savoir plus sur les disponibilités des services et les emplacements des serveurs [**ici**](https://cloud.google.com/about/locations/).

5. Acceptez les **Conditions générales**.

![Image](https://cdn-media-1.freecodecamp.org/images/B5rzqO7YzxBfcTPpL0-SpWj-Opi1dF0FH0h2)

5. Une fois terminé, faites défiler vers le bas et cliquez sur **Créer un projet**.

![Image](https://cdn-media-1.freecodecamp.org/images/vEG0IraiNoAedcBgHK8T-Iixohwr4-Jvfete)

* Voir **3.1 Passer à un compte administrateur** dans l'annexe à la fin de cet article si vous avez rencontré un message d'erreur demandant un compte administrateur.

Firebase prendra un certain temps pour préparer votre application. Une fois terminé, cliquez sur le bouton **Continuer** pour ouvrir la **Page d'aperçu du projet Firebase**.

![Image](https://cdn-media-1.freecodecamp.org/images/juqNs74YCpoCTwiGiwLfNwIhfcwHUsBS7K7D)

#### 4. Configurer une application iOS

1. Dans votre **Page d'aperçu du projet Firebase**, lancez l'assistant de configuration pour **iOS**.

![Image](https://cdn-media-1.freecodecamp.org/images/0oBCTTpEkwEKdWeJx0q8L3eFiUFBbzQj8BPj)

2. Dans l'assistant de configuration, entrez l'**ID de bundle iOS**. Le bouton **Enregistrer l'application** devrait alors s'allumer, cliquez dessus.

* Un guide sur la façon de trouver l'ID de bundle iOS peut être trouvé ci-dessous dans la section **4.1 Trouver le dossier racine du projet iOS et obtenir l'ID de bundle** de l'annexe.

![Image](https://cdn-media-1.freecodecamp.org/images/AC5HOfe1A3qBExHbEAi3quD3BI7-5FUU9Em5)

3. Téléchargez le fichier de configuration **_GoogleService-Info.plist_** et placez-le dans le dossier racine du projet iOS, puis cliquez sur **Suivant**.

* Un guide sur la façon de trouver l'ID de bundle iOS peut être trouvé ci-dessous dans la section **4.1 Trouver le dossier racine du projet iOS et obtenir l'ID de bundle** de l'annexe.

![Image](https://cdn-media-1.freecodecamp.org/images/DgXQCKfCZ84AZL5gwAiitFHrpzhw1Jkw4ftA)

4. Suivez les instructions pour ajouter le **SDK Firebase**, puis cliquez sur **Suivant**.

![Image](https://cdn-media-1.freecodecamp.org/images/cBV0KNA7yJOUqXZltFjA7NvIJ1gnYIed64dI)

* Un guide détaillé sur la façon d'installer **CocoaPods** et le **SDK Firebase** peut être trouvé ci-dessous dans la section **4.2 Installation de CocoaPods et du SDK Firebase**.

5. Modifiez le code à l'intérieur du **AppDelegate** principal comme indiqué par l'assistant de configuration, puis cliquez sur **Suivant**. Pour cet exemple, j'ai utilisé **Objective-C**, et j'ai donc remplacé le contenu à l'intérieur de **_AppDelegate.m_** par le code suivant.

```objectivec
#include "AppDelegate.h"
#include "GeneratedPluginRegistrant.h"

@import UIKit;
@import Firebase;

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
[FIRApp configure];
return YES;
}

@end
```

![Image](https://cdn-media-1.freecodecamp.org/images/5agXkDqo0aAGpa6N9ZLWgn3oN710M9c5Z2fj)

6. Retournez au dossier racine et exécutez votre application, après un certain temps, vous devriez voir l'assistant de configuration indiquant que votre application est ajoutée à Firebase. Cliquez sur **Continuer vers la console** pour terminer la configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/p5ODqX7TTswka1QMpu4r93k5G9AVHr0Si2kg)

![Image](https://cdn-media-1.freecodecamp.org/images/oBZf6Nqo-nvZTUORtvybrVv8Ia2aldKXnJq6)

Félicitations ! Vous avez ajouté Firebase avec succès à votre application Flutter. Malgré le fait que Firebase et Flutter soient tous deux de Google, c'est en fait une bonne pratique d'ingénierie logicielle d'avoir toujours un plan B, ainsi que les plans C, D, E, F et G. À l'avenir, j'écrirai un autre guide sur une application exemple utilisant Firebase, et plus sur Flutter.

Amusez-vous bien en codant !!!

### Annexes :

#### 3.1 Passer à un compte administrateur

Si vous avez rencontré le message suivant, cela signifie que vous devez contacter l'organisation de votre compte Gmail pour vous accorder l'accès à la **Console des développeurs Google**.

![Image](https://cdn-media-1.freecodecamp.org/images/OCEEJckD9203lGfiVrwQavZ26GPzGdKIjscK)
_Demande de compte administrateur_

#### 4.1 Trouver le dossier racine du projet iOS et obtenir l'ID de bundle

1. Lancez **Xcode** depuis le **Launchpad**.

2. Sélectionnez **« Ouvrir un autre projet... »** en bas de l'écran d'invite.

![Image](https://cdn-media-1.freecodecamp.org/images/Wlr2j9zKkVEHwNQYdTI9wxWriKAMIvkmp8IQ)

3. Accédez à votre dossier de projet Flutter, ouvrez le dossier **« ios »** et sélectionnez **« Runner.xcodeproj »**. Cela devrait ouvrir automatiquement le projet dans Xcode.

![Image](https://cdn-media-1.freecodecamp.org/images/oFjvHMqE4YtJiwfuSP55thHvD0GUjxEwY01x)

4. Sélectionnez le projet **Runner** à gauche, vous devriez maintenant voir l'**Identifiant de bundle** sous **Identité**.

![Image](https://cdn-media-1.freecodecamp.org/images/kl55NJhmnZH74ihBKE-3fdrXeMmBysovfJ96)

#### **4.2 Installation de CocoaPods et du SDK Firebase**

Au cas où les instructions de l'assistant de configuration n'auraient pas fonctionné, vous devrez supprimer le Podfile existant afin de les réinstaller correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/o6kODHbEcH9JMV5gbf7FlBQKOVQnYlGPEuQn)

1. **CocoaPods** est construit avec **Ruby** et peut être installé avec le **Ruby** par défaut disponible sur **MacOS**. Utilisez les commandes suivantes pour l'installer.

```bash
sudo gem install cocoapods
```

![Image](https://cdn-media-1.freecodecamp.org/images/EgRhnJPf9kSRicH5fKajuXeMcPOdKnVerKvw)

2. Initialisez le **_Podfile_** avec la commande suivante.

```bash
pod init
```

3. Ensuite, ajoutez le code suivant au **_Podfile_** initialisé.

```bash
pod 'Firebase/Core'
```

![Image](https://cdn-media-1.freecodecamp.org/images/zemw1-5IZvI5VkGO7mGO0aSySoY-t5KMQruW)

4. Une fois terminé, enregistrez les modifications apportées au **_Podfile_**, et installez le **SDK Firebase** avec la commande suivante.

```bash
pod install
```

![Image](https://cdn-media-1.freecodecamp.org/images/VuguYbQEDy6r9EcMXQ2vDaeOcvgHBcumNllL)

5. Après l'installation, vous devrez probablement configurer les fichiers **._xcconfig_**. Tout d'abord, vous devrez copier les fichiers du dossier **_Pods/Target Support Files/Pods-Runner_** vers le dossier **_Flutter_**. 

![Image](https://cdn-media-1.freecodecamp.org/images/3amfUm5sWKDF9bf-ed9tsbknTggn0vVCwxwf)

6. Ensuite, vous devrez les inclure dans les fichiers **_Debug.xcconfig_** et **_Release.xcconfig_** à l'intérieur du dossier **_Flutter_**. 

Dans **_Debug.xcconfig_** :

```
#include "Pods-Runner.debug.xcconfig"
```

![Image](https://cdn-media-1.freecodecamp.org/images/9zJj8Nyvi1mIWq7y3cfsa2uhBMbw4qOz6zm1)

Dans **_Release.xcconfig_** :

```
#include "Pods-Runner.profile.xcconfig"
#include "Pods-Runner.release.xcconfig"
```

![Image](https://cdn-media-1.freecodecamp.org/images/BlQuedQwnCZmIQl9PLgBhJL1ugr8VLoqDfPu)