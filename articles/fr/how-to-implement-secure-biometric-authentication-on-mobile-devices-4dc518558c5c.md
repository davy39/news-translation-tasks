---
title: Comment implémenter une authentification biométrique sécurisée sur les appareils
  mobiles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-17T16:41:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-secure-biometric-authentication-on-mobile-devices-4dc518558c5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XeuEHmQJLOKLRhit-mZZRw.jpeg
tags:
- name: biometric authentication
  slug: biometric-authentication
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment implémenter une authentification biométrique sécurisée sur les
  appareils mobiles
seo_desc: 'By Kathy Dinh

  A quick search for React Native biometric authentication would give you several
  tutorials. That was the first thing I did when there was a need for such a feature
  in one of my projects. Depending on the level of risk acceptable for your...'
---

Par Kathy Dinh

Une recherche rapide sur l'authentification biométrique React Native vous donnera plusieurs tutoriels. C'est la première chose que j'ai faite lorsqu'il y avait besoin d'une telle fonctionnalité dans l'un de mes projets. Selon le niveau de risque acceptable pour votre application, l'une de ces solutions pourrait être adaptée. Pour une application à haut risque comme la nôtre, elle ne passerait pas les tests de sécurité.

Si vous souhaitez ajouter une authentification biométrique sécurisée à une **_application React Native iOS_**, vous êtes au bon endroit.

#### **Qu'est-ce qui ne va pas avec react-native-touchid ?**

La plupart des implémentations utilisent le package _react-native-touchid_. À la [ligne 65](https://github.com/naoufal/react-native-touch-id/blob/2e7c4bcd0aedad01e45708fbb831fcc70fc48264/TouchID.m#L65) dans le fichier [TouchID.m](https://github.com/naoufal/react-native-touch-id/blob/master/TouchID.m), la méthode _authenticate_ appelle la méthode LAContext suivante lors de la tentative d'authentification TouchID/FaceID :

```
evaluatePolicy:localizedReason:reply:^(BOOL success, NSError *error)
```

La méthode repose sur une vérification d'authentification locale si l'empreinte digitale fournie correspond à celle enregistrée sur l'appareil. Lorsque la vérification passe, un booléen de succès est retourné et l'utilisateur s'est authentifié avec succès avec TouchID/FaceID.

_Il a été signalé la possibilité de contourner l'authentification locale en envoyant un signal de succès aux API d'Apple sur des appareils iOS jailbreakés ou non jailbreakés_. Ainsi, l'authentification biométrique via l'authentification locale est vulnérable à l'usurpation par un attaquant qui pourrait interférer avec la vérification à l'exécution.

#### **Quelle est la manière sécurisée d'implémenter l'authentification biométrique ?**

Pour implémenter l'authentification biométrique dans une application iOS, il existe deux méthodes — soit via les API d'authentification locale d'Apple, soit via le _contrôle d'accès des services Keychain_ fourni nativement par le système sous-jacent.

L'authentification avec l'authentification locale est plus simple mais généralement non recommandée pour les applications critiques. Comme décrit dans la section précédente, l'authentification locale est une API de haut niveau dont le comportement peut être remplacé, c'est-à-dire qu'un attaquant pourrait simuler une authentification réussie en modifiant la réponse de l'API.

Il est reconnu comme _bonne pratique d'utiliser les services Keychain_ pour implémenter l'authentification biométrique dans les applications à haut risque. Les services Keychain appliquent un contrôle d'accès sur leur contenu stocké en utilisant les fonctionnalités fournies par iOS et [Secure Enclave](https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/storing_keys_in_the_secure_enclave). Le processus s'exécute au niveau du matériel et du système d'exploitation et minimise ainsi l'exposition à la couche applicative moins fiable. Des risques de sécurité existent lorsque l'utilisateur est sur un appareil jailbreaké ou infecté par un malware, mais ces menaces peuvent être atténuées par la technologie de gestion des appareils mobiles (MDM).

#### **Comment implémenter l'authentification biométrique avec les services Keychain ?**

Pour accéder aux services Keychain dans notre application React Native, nous allons utiliser le package [react-native-keychain](https://github.com/oblador/react-native-keychain). Le code exemple est en TypeScript, qui peut facilement être converti en JavaScript.

Tout d'abord, _installez_ react-native-keychain et sa déclaration de type en tant que dépendance de votre projet :

```
npm i -S react-native-keychain
```

```
npm i -S @types/react-native-keychain
```

Ensuite, nous devons _lier la bibliothèque_ car elle dépend du composant natif. Il existe deux méthodes pour lier les bibliothèques dans une application React Native : le lien automatique et le lien manuel. J'ai rencontré de nombreuses erreurs avec CocoaPods lors de la réalisation du lien automatique. Le lien manuel fonctionne mais implique de nombreuses étapes.

J'ai découvert que la bibliothèque est liée correctement sans erreurs si vous exécutez _react-native link_ après avoir temporairement supprimé le _Podfile_ sous le dossier iOS. Pour vous éviter des tracas, suivons une approche hybride. En supposant que votre code est _sous contrôle de version_ afin qu'il soit possible de revenir en arrière en toute sécurité, supprimez votre Podfile, _puis_ exécutez la commande de liaison :

```
react-native link react-native-keychain
```

Maintenant, annulez la suppression de votre Podfile. Pour iOS 10, vous devrez activer l'autorisation `Keychain Sharing` dans la section `Capabilities` de votre cible de build.

![Image](https://cdn-media-1.freecodecamp.org/images/2HiA1V62TFWjNAJW6-sS2E-EpCAkon9aqFjE)

Ajoutez la paire clé-valeur suivante à _Info.plist_ :

```
<key>NSFaceIDUsageDescription</key><string>L'activation de Face ID permet un accès rapide et sécurisé à votre compte.</string>
```

Puis reconstruisez votre projet avec :

```
react-native run-ios
```

En cas de difficulté à installer react-native-keychain, référez-vous à ce [README GitHub](https://github.com/oblador/react-native-keychain).

Avant de demander à l'utilisateur de s'authentifier avec TouchID/FaceID, il est judicieux de vérifier si l'appareil iOS de l'utilisateur supporte une telle capacité en appelant `[getSupportedBiometryType](https://github.com/oblador/react-native-keychain#getsupportedbiometrytype)` :

![Image](https://cdn-media-1.freecodecamp.org/images/UOLq4S9cQehzR8tgQIJqHEOofr-PK9J4a4lN)

Après avoir confirmé que l'authentification biométrique est supportée, vous devez enregistrer un contenu dans le trousseau et définir les indicateurs de contrôle d'accès. Le contenu pourrait être des identifiants utilisateur ou un jeton d'accès. L'entrée du trousseau est chiffrée et stockée dans un stockage sécurisé. Pour stocker une valeur dans le trousseau, appelez `[setGenericPassword](https://github.com/oblador/react-native-keychain#setgenericpasswordusername-password--accesscontrol-accessible-accessgroup-service-securitylevel-)` :

![Image](https://cdn-media-1.freecodecamp.org/images/9tIdxr-QPhcRBF2KOEA7k1stwcsB2RZ21HD-)

Quelques points à noter ici :

* La définition de _accessControl_ sur l'une de ces valeurs d'énumération `[Keychain.ACCESS_CONTROL](https://github.com/oblador/react-native-keychain#keychainaccess_control-enum)` `BIOMETRY_ANY`, `BIOMETRY_CURRENT_SET`, `BIOMETRY_ANY_OR_DEVICE_PASSCODE`, `BIOMETRY_CURRENT_SET_OR_DEVICE_PASSCODE` impose que l'utilisateur s'authentifie avec TouchID/FaceID chaque fois que nous tentons de récupérer l'élément du trousseau.
* Nous définissons également _accessible_ sur la valeur d'énumération `Keychain.ACCESSIBLE` `WHEN_PASSCODE_SET_THIS_DEVICE_ONLY`. Il s'agit de la contrainte accessible la plus stricte, qui impose :

```
Votre appareil doit être déverrouillé pour que le secret soit accessible.
```

```
Votre appareil doit avoir un code d'accès à l'appareil défini.
```

```
Si vous désactivez le code d'accès de votre appareil, le secret est supprimé.
```

```
Le secret ne peut pas être restauré sur un autre appareil.
```

```
Le secret n'est pas inclus dans les sauvegardes iCloud.
```

Enfin, nous déclenchons l'invite d'authentification TouchID/FaceID en tentant d'accéder à la valeur du trousseau précédemment stockée avec `[getGenericPassword](https://github.com/oblador/react-native-keychain#getgenericpassword-authenticationprompt-service-)` :

![Image](https://cdn-media-1.freecodecamp.org/images/ZX3bMhpsIXH9XNWGJklGOL5yUxNlOrXPkbK6)

Puisque nous avons enregistré notre secret avec un contrôle d'accès précédemment, l'accès à l'élément nécessite que l'utilisateur passe l'authentification biométrique. Lorsque l'authentification est réussie, le résultat retourne un objet, dont le _username_ est 'your-secret-name', le _password_ est 'your-secret-value', et le _service_ est 'your-service-name'.

Après _5 tentatives échouées d'authentification TouchID/FaceID à l'échelle du système_, l'authentification biométrique est désactivée partout sur l'appareil. L'utilisateur doit verrouiller et déverrouiller l'appareil avec un code d'accès pour réactiver TouchID/FaceID. C'est pourquoi à la ligne 14, nous devons vérifier le type de biométrie supporté et gérer le cas de manière appropriée, par exemple, en demandant à l'utilisateur de se connecter avec son nom d'utilisateur/mot de passe.

#### **Mises en garde**

Bien que l'authentification biométrique avec react-native-keychain soit adaptée aux applications critiques, il y a quelques mises en garde que je souhaite porter à votre attention :

**Il n'y a _pas de repli par code d'accès_**. Vous pouvez recevoir une exigence permettant à l'utilisateur de s'authentifier avec le code d'accès de son appareil. En consultant le README du package, vous devriez trouver les clés d'énumération `Keychain.ACCESS_CONTROL` `DEVICE_PASSCODE`, `BIOMETRY_ANY_OR_DEVICE_PASSCODE`, `BIOMETRY_CURRENT_SET_OR_DEVICE_PASSCODE`.

Malheureusement, la définition d'une valeur de contrôle d'accès lors de l'appel de `setGenericPassword` sur l'une de ces trois clés d'énumération n'active pas de repli "Entrer le mot de passe". [Le problème a été signalé sur GitHub](https://github.com/oblador/react-native-keychain/issues/182), mais il n'y a pas eu de réponse au moment de la publication de cet article.

Vous pourriez penser à implémenter un repli par code d'accès avec une bibliothèque différente. Soyez conscient que votre système n'est sécurisé que _autant que votre maillon le plus faible_. Si votre implémentation de repli par code d'accès s'exécute au niveau de la couche applicative, elle est une cible potentielle pour une attaque de sécurité et annule l'objectif de s'appuyer sur les services Keychain pour l'authentification biométrique.

De plus, **l'authentification avec react-native-keychain sur les appareils Android _peut ne pas être considérée comme sécurisée_** car il n'y a pas d'équivalent des services Keychain dans Android.

#### Conclusion

Merci d'avoir lu jusqu'ici. J'espère que vous avez trouvé le tutoriel utile. Une amélioration que vous pourriez vouloir apporter est de demander à l'utilisateur s'il souhaite opter pour l'authentification biométrique avant de l'activer dans votre application. Vous pouvez également ajouter un paramètre pour permettre à l'utilisateur d'activer ou de désactiver l'authentification TouchID/FaceID dans la page des paramètres de votre application.

#### **Références**

* [Pourquoi l'authentification locale n'est pas sécurisée](https://www.punchkick.com/blog/2016/03/31/best-practices-of-implementing-touch-id-within-financial-apps)
* [Comment fonctionne l'authentification Keychain avec Touch ID](https://docplayer.net/62572307-Keychain-and-authentication-with-touch-id.html)