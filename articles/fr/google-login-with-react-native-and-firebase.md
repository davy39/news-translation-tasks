---
title: Comment configurer la connexion Google dans React Native & Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-15T20:42:32.000Z'
originalURL: https://freecodecamp.org/news/google-login-with-react-native-and-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/React-native-Google-login.png
tags:
- name: Firebase
  slug: firebase
- name: React Native
  slug: react-native
seo_title: Comment configurer la connexion Google dans React Native & Firebase
seo_desc: "By Florian Marcu\nGoogle sign-in is a great login feature to offer to your\
  \ app's users. It makes it easier for them to create an account and sign in. \n\
  And what's even better, Firebase makes it extremely easy for developers to add support\
  \ for Google si..."
---

Par Florian Marcu

La connexion Google est une excellente fonctionnalité de connexion à offrir aux utilisateurs de votre application. Cela leur facilite la création d'un compte et la connexion. 

Et ce qui est encore mieux, Firebase rend extrêmement facile pour les développeurs d'ajouter la prise en charge de la connexion Google. Mais la configuration de l'environnement React Native peut créer quelques défis, qui sont entièrement couverts dans ce tutoriel. 

React Native et le SDK Firebase rendent l'implémentation de la connexion Google assez simple. Construisons une application simple qui n'a qu'un seul bouton de connexion Google. Une fois que l'utilisateur s'est connecté avec succès à Google, nous allons afficher les informations de l'utilisateur récupérées depuis leur compte Google ainsi qu'un bouton de déconnexion.

Vous pouvez également ajouter la connexion Facebook à votre application si vous souhaitez offrir encore plus d'options de connexion à vos utilisateurs. Vous pouvez consulter ce guide sur la [connexion Facebook dans React Native avec Firebase](https://www.instamobile.io/react-native-tutorials/facebook-login-react-native-firebase/) si vous souhaitez en savoir plus sur la configuration de la connexion Facebook.

## Pourquoi utiliser un bouton de connexion Google dans les applications mobiles ?

1. L'utilisation de Google ou d'autres tiers peut rendre votre processus d'authentification fluide et convivial. Les utilisateurs n'ont pas à perdre de temps dans le processus d'inscription, ce qui améliorera considérablement vos taux d'inscription et de rétention.
2. C'est sûr et sécurisé.
3. Les utilisateurs font plus confiance à Google ou Facebook qu'à un site ou une application inconnue sur Internet.
4. Cela offre une bonne expérience utilisateur. En tant qu'utilisateur, nous avons peu de patience pour toute action ou travail que nous devons faire, surtout dans une application relativement inconnue que nous essayons pour la première fois.

Sans plus tarder, passons directement à la partie développement de l'application de ce tutoriel.

## Configuration du projet Firebase

Rendez-vous sur la [Console Firebase](https://firebase.google.com/) et créez un projet Firebase :

![créer un nouveau projet firebase](https://www.instamobile.io/wp-content/uploads/2020/06/create-new-firebase-project.png)
_créer un nouveau projet firebase_

Ici, nous devons configurer le nom du projet Firebase et l'identifiant de l'application, alors créons d'abord l'application React Native.

## Création du projet React Native

Tout d'abord, nous devons créer un projet React Native en utilisant la commande suivante :

`react-native init instamobile-google-login-demo`

Ici, nous avons donné le nom du projet **instamobile-google-login-demo**. Maintenant, nous devons installer le package **react-native-google-signin** en utilisant la commande suivante :

`yarn add react-native-google-signin`

Le package `react-native-google-signin` est utilisé pour implémenter les fonctions d'authentification Google dans l'application React Native. Maintenant, nous devons importer les modules et composants nécessaires depuis le package respectif comme montré dans l'extrait de code ci-dessous :

```javascript
import {
  GoogleSignin,
  GoogleSigninButton,
  statusCodes,
} from 'react-native-google-signin';
```

Ensuite, nous devons créer les états afin de gérer l'état d'authentification et les informations de l'utilisateur. Pour cela, nous utilisons le module `useState` comme montré dans l'extrait de code ci-dessous :

```javascript
const [loggedIn, setloggedIn] = useState(false);
const [userInfo, setuserInfo] = useState([]);
```

Maintenant, nous devons créer une fonction de connexion pour gérer l'authentification comme montré dans l'extrait de code ci-dessous :

```javascript
_signIn = async () => {
  try {
    await GoogleSignin.hasPlayServices();
    const {accessToken, idToken} = await GoogleSignin.signIn();
    setloggedIn(true);
  } catch (error) {
    if (error.code === statusCodes.SIGN_IN_CANCELLED) {
      // l'utilisateur a annulé le flux de connexion
      alert('Annulé');
    } else if (error.code === statusCodes.IN_PROGRESS) {
      alert('Connexion en cours');
      // l'opération (par exemple, la connexion) est déjà en cours
    } else if (error.code === statusCodes.PLAY_SERVICES_NOT_AVAILABLE) {
      alert('PLAY_SERVICES_NOT_AVAILABLE');
      // les services play ne sont pas disponibles ou sont obsolètes
    } else {
      // une autre erreur s'est produite
    }
  }
};
```

Ensuite, nous devons initialiser la configuration de l'objet de connexion Google en utilisant la fonction `useEffect` :

```javascript
useEffect(() => {
   GoogleSignin.configure({
     scopes: ['email'], // quelle API vous souhaitez accéder au nom de l'utilisateur, par défaut email et profil
     webClientId:
       '418977770929-g9ou7r9eva1u78a3anassxxxxxxx.apps.googleusercontent.com', // ID client de type WEB pour votre serveur (nécessaire pour vérifier l'ID utilisateur et l'accès hors ligne)
     offlineAccess: true, // si vous souhaitez accéder à l'API Google au nom de l'utilisateur DEPUIS VOTRE SERVEUR
   });
 }, []);
```

Enfin, nous avons besoin d'une fonction qui gère l'action de déconnexion. Pour cela, nous allons implémenter la méthode `signOut` comme montré dans l'extrait de code ci-dessous :

```javascript
signOut = async () => {
    try {
      await GoogleSignin.revokeAccess();
      await GoogleSignin.signOut();
      setloggedIn(false);
      setuserInfo([]);
    } catch (error) {
      console.error(error);
    }
  };
```

Maintenant, nous devons rendre les composants à l'écran également. Pour cela, nous allons utiliser divers composants comme `View` et `Button` :

```javascript
return (
    <>
      <StatusBar barStyle="dark-content" />
      <SafeAreaView>
        <ScrollView
          contentInsetAdjustmentBehavior="automatic"
          style={styles.scrollView}>
          <Header />

          <View style={styles.body}>
            <View style={styles.sectionContainer}>
              <GoogleSigninButton
                style={{width: 192, height: 48}}
                size={GoogleSigninButton.Size.Wide}
                color={GoogleSigninButton.Color.Dark}
                onPress={this._signIn}
              />
            </View>
            <View style={styles.buttonContainer}>
              {!loggedIn && <Text>Vous êtes actuellement déconnecté</Text>}
              {loggedIn && (
                <Button
                  onPress={this.signOut}
                  title="Déconnexion"
                  color="red"></Button>
              )}
            </View>
          </View>
        </ScrollView>
      </SafeAreaView>
    </>
  );
```

Maintenant, si nous exécutons notre projet dans l'émulateur, nous obtiendrons les résultats suivants :

![premier écran de connexion google](https://www.instamobile.io/wp-content/uploads/2020/06/google-login-first-screen.png)
_Connexion avec Google React Native_

Plutôt bien, n'est-ce pas ? Nous avons terminé l'implémentation (à la fois l'UI et la logique métier) au niveau React Native dans notre projet. 

Comme vous pouvez le voir, nous avons un bouton "Se connecter avec Google" qui se transforme en bouton de déconnexion une fois l'opération de connexion réussie.

Nous allons maintenant configurer le package Google SignIn et l'application Firebase.

## Configuration des projets natifs iOS et Android

Il y a quelques étapes de configuration que nous devons suivre avant que le projet ne fonctionne complètement. Elles sont principalement liées au côté natif de l'application.

### Pour iOS

Ici, dans VSCode (ou tout Terminal), exécutez simplement `cd ios && pod install`. Ensuite, ouvrez le fichier _.xcworkspace_ dans Xcode (à partir du dossier ios) et assurez-vous que les Pods sont inclus :

![installer la bibliothèque de connexion google dans xcode](https://www.instamobile.io/wp-content/uploads/2020/06/install-google-login-lib-in-xcode.png)
_installer la bibliothèque de connexion google dans xcode_

### Pour Android

1. Tout d'abord, nous devons lier le module natif.

* Dans RN >= 0.60, vous ne devriez pas avoir besoin de faire quoi que ce soit grâce à l'auto-liage.
* Dans RN < 0.60, exécutez `react-native link react-native-google-signin`.

2. Mettez à jour **android/build.gradle** avec la configuration suivante :

```java
buildscript {
    ext {
        buildToolsVersion = "27.0.3"
        minSdkVersion = 16
        compileSdkVersion = 27
        targetSdkVersion = 26
        supportLibVersion = "27.1.1"
        googlePlayServicesAuthVersion = "16.0.1" // <--- utilisez cette version ou une version plus récente
    }
...
    dependencies {
        classpath 'com.android.tools.build:gradle:3.1.2' // <--- utilisez cette version ou une version plus récente
        classpath 'com.google.gms:google-services:4.1.0' // <--- utilisez cette version ou une version plus récente
    }
...
allprojects {
    repositories {
        mavenLocal()
        google() // <--- assurez-vous que cela est inclus
        jcenter()
        maven {
            // Toutes les dépendances React Native (JS, sources Obj-C, binaires Android) sont installées depuis npm
            url "$rootDir/../node_modules/react-native/android"
        }
    }
}
```

3. Mettez à jour `android/app/build.gradle` avec la configuration suivante :

```java
...
dependencies {
    implementation fileTree(dir: "libs", include: ["*.jar"])
    implementation "com.android.support:appcompat-v7:23.0.1"
    implementation "com.facebook.react:react-native:+"
    implementation(project(":react-native-community_google-signin")) // <--- ajoutez cette dépendance
}
```

Vérifiez que `react-native link` a lié le module natif — mais seulement si vous avez utilisé `react-native link` !

Dans `android/settings.gradle`, nous devons avoir les configurations suivantes :

```java
...
include ':react-native-google-signin', ':app'
project(':react-native-google-signin').projectDir = new File(rootProject.projectDir, '../node_modules/@react-native-community/google-signin/android')
```

Ensuite, dans `MainApplication.java`, nous devons avoir le package Google ajouté comme dans l'extrait de code suivant :

```java
import co.apptailor.googlesignin.RNGoogleSigninPackage;  // <--- importer

public class MainApplication extends Application implements ReactApplication {

  ......

  @Override
    protected List<ReactPackage> getPackages() {
      return Arrays.<ReactPackage>asList(
          new MainReactPackage(),
          new RNGoogleSigninPackage() // <-- cela doit être dans la liste
      );
    }
  ......

}
```

## Configuration de Firebase

### Pour iOS

Maintenant, nous devons commencer la configuration Firebase. Dans Firebase, nous devons configurer une application Google Cloud. Mais lorsque nous configurons la méthode d'authentification sur Firebase, cela crée également une application Google Cloud.

Tout d'abord, nous devons créer une application Firebase iOS afin d'obtenir **GoogleService-Info.plist** comme montré dans la capture d'écran ci-dessous :

![ajouter un nouveau nom d'application firebase](https://www.instamobile.io/wp-content/uploads/2020/06/add-new-firebase-app-name.png)
_ajouter un nouveau nom d'application firebase_

Ensuite, nous copions le fichier **GoogleService-Info.plist** dans le projet Xcode comme montré dans la capture d'écran ci-dessous :

![ajouter google service plist à xcode](https://www.instamobile.io/wp-content/uploads/2020/06/add-google-service-plist-to-xcode.png)
_ajouter google service plist à xcode_

Maintenant, nous devons ajouter l'ID client inversé présent dans le fichier **GoogleService-Info.plist** aux types d'URL, comme montré dans la capture d'écran ci-dessous :

![obtenir l'id client inversé depuis xcode](https://www.instamobile.io/wp-content/uploads/2020/06/get-reverse-client-id-from-xcode.png)
_obtenir l'id client inversé depuis xcode_

L'étape suivante consiste à aller dans **Info** → **Types d'URL**, puis à remplir les **Schémas d'URL** comme montré dans la capture d'écran ci-dessous :

![ajouter le schéma d'url à xcode](https://www.instamobile.io/wp-content/uploads/2020/06/add-url-scheme-to-xcode.png)
_ajouter le schéma d'url à xcode_

### Pour Android

Tout d'abord, nous devons créer une application Android sur Firebase. Pour cela, nous avons besoin d'un nom de package et d'un certificat **SHA-1** de notre application. Ensuite, nous pouvons enregistrer l'application Firebase comme montré ci-dessous :

![créer une nouvelle application firebase android](https://www.instamobile.io/wp-content/uploads/2020/06/create-new-android-firebase-app-300x252.png)
_créer une nouvelle application firebase android_

Nous pouvons obtenir le nom du package dans **MainApplication.java** de notre projet comme mis en évidence dans l'extrait de code ci-dessous :

![trouver le nom du bundle dans l'application android](https://www.instamobile.io/wp-content/uploads/2020/06/find-out-bundle-name-in-android-app-1024x408.png)
_trouver le nom du bundle dans l'application android_

Ensuite, nous pouvons obtenir la clé SHA-1 dans le fichier Keystore. Dans le répertoire **android/app**, nous pouvons exécuter la commande :

```shell
cd android/app ; 
keytool -exportcert -keystore debug.keystore -list -v
```

Ensuite, la clé **SHA-1** apparaîtra, comme montré dans la capture d'écran ci-dessous :

![générer sha1 pour enregistrer l'application android dans firebase](https://www.instamobile.io/wp-content/uploads/2020/06/generate-sha1-for-register-android-app-in-firebase.png)
_générer sha1 pour enregistrer l'application android dans firebase_

Après avoir créé avec succès l'application de configuration Firebase, nous devons télécharger le fichier **google-services.json** et le copier dans le répertoire, comme montré dans la capture d'écran ci-dessous :

![ajouter google service json au dossier de l'application android](https://www.instamobile.io/wp-content/uploads/2020/06/add-google-service-json-to-android-app-folder-250x300.png)
_ajouter google service json au dossier de l'application android_

Maintenant, la dernière étape consiste à configurer un composant de connexion Google dans Android.

### Installation du package React Native Firebase

Pour installer le package **react-native-firebase** version 6, nous devons exécuter la commande suivante dans l'invite de commande de notre projet :

```shell
# En utilisant npm 
npm install --save @react-native-firebase/app 
# En utilisant Yarn 
yarn add @react-native-firebase/app
```

Le module `@react-native-firebase/app` doit être installé avant d'utiliser tout autre service Firebase.

### Pour iOS

Nous avons déjà ajouté **GoogleService-Info.plist** à Xcode. Il reste à permettre à Firebase sur iOS d'utiliser les identifiants. Le SDK Firebase iOS doit être configuré pendant la phase de démarrage de votre application.

Pour cela, nous devons ouvrir notre fichier `/ios/{projectName}/AppDelegate.m` et ajouter ce qui suit :

En haut du fichier, nous devons importer le SDK Firebase :

```swift
#import <Firebase.h>
```

Dans votre méthode `didFinishLaunchingWithOptions` existante, nous devons ajouter ce qui suit en haut de la méthode :

```m
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Ajoutez-moi --- \/
  if ([FIRApp defaultApp] == nil) {
    [FIRApp configure];
  }
  // Ajoutez-moi --- /\
  // ...
}
```

Enfin, nous devons exécuter la commande suivante pour finaliser l'installation du package CocoaPods :

```shell
cd ios ; pod install
```

C'est tout. Nous avons maintenant terminé l'installation du package principal Firebase sur iOS.

### Pour Android

Nous devons configurer Firebase avec les identifiants Android. Pour permettre à Firebase sur Android d'utiliser les identifiants, le plugin google-services doit être activé sur le projet. Cela nécessite une modification de deux fichiers dans le répertoire Android.

Tout d'abord, ajoutez le plugin google-services comme dépendance dans votre fichier **android/build.gradle** :

```java
buildscript {
  dependencies {
    // ... autres dépendances
    classpath 'com.google.gms:google-services:4.2.0'
    // Ajoutez-moi --- /\
  }
}
Enfin, exécutez le plugin en ajoutant ce qui suit tout en bas de votre fichier /android/app/build.gradle :

apply plugin: 'com.google.gms.google-services'
```

## Module d'authentification React Native Firebase

Après la fin de l'installation, nous devons configurer le package parent Firebase. Ensuite, nous devons installer le module enfant pour l'authentification. Pour cela, nous devons ouvrir un terminal et exécuter la commande suivante :

```shell
yarn add @react-native-firebase/auth
```

### Pour iOS

Nous devons simplement installer les pods à nouveau dans l'invite de commande :

```
cd ios/ && pod install
```

### Pour Android

Vous pouvez suivre les instructions du [document officiel](https://rnfirebase.io/auth/usage/installation/android) qui est uniquement requis si vous utilisez React Native <= 0.59 ou si vous devez intégrer manuellement la bibliothèque.

### Activation de la connexion Google sur Firebase

Nous devons nous rendre sur la console Firebase. Ensuite, dans la section Authentification, nous devons cliquer sur Google comme montré dans la capture d'écran ci-dessous :

![méthode d'authentification dans firebase](https://www.instamobile.io/wp-content/uploads/2020/06/authentication-method-in-firebase-1024x396.png)
_méthode d'authentification dans firebase_

Ensuite, nous devons activer la configuration avec la configuration suivante et enregistrer la configuration comme montré dans la capture d'écran ci-dessous :

![activer le support de projet par email](https://www.instamobile.io/wp-content/uploads/2020/06/select-support-email-in-firebase-app.png)
_activer le support de projet par email_

Dans **App.js**, nous devons importer **auth** depuis le package Firebase comme montré dans l'extrait de code ci-dessous :

```
import auth from '@react-native-firebase/auth';
```

Ensuite, nous devons intégrer la configuration d'authentification à la fonction **sign-in**. Après une connexion réussie, nous stockons le **accessToken** et **idToken** dans **Firebase**. Maintenant, nous pouvons essayer de nous connecter avec Google sur notre application de démonstration React Native. 

```javacript
_signIn = async () => {
    try {
      await GoogleSignin.hasPlayServices();
      const {accessToken, idToken} = await GoogleSignin.signIn();
      setloggedIn(true);
      const credential = auth.GoogleAuthProvider.credential(
        idToken,
        accessToken,
      );
      await auth().signInWithCredential(credential);
    } catch (error) {
```

Maintenant, nous avons réussi à intégrer la connexion Google dans notre application React Native :

![résultat de la connexion google avec react native](https://www.instamobile.io/wp-content/uploads/2020/06/2020-06-29-17.52.16.gif)
_résultat de la connexion google avec react native_

Nous pouvons voir de nouvelles données ajoutées à la console Firebase :

![console d'authentification firebase](https://www.instamobile.io/wp-content/uploads/2020/07/firebase-authentication-console.png)
_console d'authentification firebase_

## Suivi du statut de l'utilisateur

Pour vérifier le statut de connexion de l'utilisateur, nous utilisons Firebase Auth. Pour cela, nous devons ajouter la méthode **onAuthStateChanged** à **useEffect** afin qu'elle s'exécute à chaque appel d'événement **componentDidMount**. 

De plus, nous devons passer un rappel à la fonction nommée **onAuthStateChanged** en tant qu'argument comme montré dans l'extrait de code ci-dessous :

```javascript
useEffect(() => {
    .............
    const subscriber = auth().onAuthStateChanged(onAuthStateChanged);
    return subscriber; // se désabonner au démontage
  }, []);
```

Dans la fonction **onAuthStateChanged**, nous gérons les données d'état local comme montré dans l'extrait de code ci-dessous :

```javascript
function onAuthStateChanged(user) {
    setUser(user);
    console.log(user);
    if (user) setloggedIn(true);
  }
```

Maintenant, nous devons stocker les données de l'utilisateur pour l'état. Ensuite, essayer d'afficher les données de l'utilisateur après une connexion réussie. Pour cela, nous devons utiliser le morceau de code suivant :

```javascript
{!user && <Text>Vous êtes actuellement déconnecté</Text>}
{user && (
  <View>
    <Text>Bienvenue {user.displayName}</Text>
    <Button
      onPress={this.signOut}
      title="Déconnexion"
      color="red"></Button>
  </View>
)}
```

Nous obtiendrons le résultat suivant dans notre simulateur :

![résultat de l'affichage du nom d'utilisateur auth](https://www.instamobile.io/wp-content/uploads/2020/07/show-auth-user-name.png)
_déconnexion de l'authentification firebase_

## Déconnexion de Firebase

Pour se déconnecter, nous devons supprimer toutes les informations d'identification de l'utilisateur et révoquer le jeton de connexion Google. 

Tout d'abord, nous devons attendre que le module **GoogleSignin** révoque l'accès et se déconnecte. Ensuite, nous appelons la méthode **signOut** de l'authentification **Firebase** afin de nous déconnecter avec succès. 

L'implémentation globale du code est fournie dans l'extrait de code ci-dessous :

```javascript
signOut = async () => {
    try {
      await GoogleSignin.revokeAccess();
      await GoogleSignin.signOut();
      auth()
        .signOut()
        .then(() => alert('Vous êtes déconnecté !'));
      setloggedIn(false);
      // setuserInfo([]);
    } catch (error) {
      console.error(error);
    }
  };
```

En conséquence, nous pouvons maintenant effectuer des opérations de déconnexion comme montré dans l'extrait de code ci-dessous :

![résultat de la déconnexion firebase react native](https://www.instamobile.io/wp-content/uploads/2020/07/firebase-signout-result.gif)
_déconnexion firebase react native_

## Conclusion

Dans ce tutoriel, nous avons appris à configurer la connexion Google, ainsi qu'à stocker un jeton d'accès, en utilisant Firebase dans notre projet React Native. 

Tout d'abord, nous avons créé le projet React Native avec tous les composants nécessaires et les configurations de fonctions. Ensuite, nous avons appris à configurer Google Sign In et Firebase pour les plateformes Android et iOS. Enfin, nous avons configuré Firebase dans l'application React Native en utilisant un package Firebase et affiché les données de l'utilisateur ainsi qu'un bouton de déconnexion.

Vous pouvez télécharger le code source complet de ce tutoriel depuis [Github](https://github.com/florion101/firebase-google-login-react-native).

Le meilleur, c'est que Firebase & Google Auth sont pris en charge dans tous les langages de développement mobile, tels que [Flutter](https://www.instaflutter.com), [Swift](https://www.iosapptemplates.com) ou [Kotlin](https://www.instakotlin.com). Les étapes de configuration et l'approche architecturale sont exactement les mêmes.

## Prochaines étapes

Maintenant que vous avez appris à configurer la connexion Google Firebase dans les applications React Native, voici quelques autres sujets que vous pouvez explorer :

* [Comment créer une application React Native avec un backend Firebase](https://www.freecodecamp.org/news/react-native-firebase-tutorial/)
* Firebase & React Native — [Notifications push](https://www.instamobile.io/react-native-tutorials/push-notifications-react-native-firebase/) | [Stockage Firebase](https://www.instamobile.io/mobile-development/react-native-firebase-storage/)
* Plus de méthodes d'authentification dans React Native & Firebase — [Connexion Google](https://www.instamobile.io/mobile-development/google-login-react-native-firebase/) | [Connexion Facebook](https://www.instamobile.io/react-native-tutorials/facebook-login-react-native-firebase/) | [Authentification par SMS téléphonique](https://www.instamobile.io/mobile-development/firebase-phone-authentication-react-native/)

Si vous avez aimé ce tutoriel React Native, veuillez me donner une étoile sur le [dépôt Github](https://github.com/florion101/firebase-google-login-react-native) et partagez cela avec votre communauté. Vous pouvez consulter encore plus de [projets React Native gratuits](https://www.instamobile.io/mobile-templates/react-native-templates-free/) sur Instamobile. Santé !