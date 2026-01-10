---
title: Comment configurer l'authentification React Native avec react-native-app-auth
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-01T17:07:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-react-native-authentication-with-react-native-app-auth-f6fd66e0e6d0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*k2549xFsiA_FKSv0
tags:
- name: app development
  slug: app-development
- name: authentication
  slug: authentication
- name: React Native
  slug: react-native
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Comment configurer l'authentification React Native avec react-native-app-auth
seo_desc: 'By Melih Yumak

  Versions

  Before we start, make sure you have the following versions installed:

  “react”: “16.8.3”,“react-native”: “0.59.1”,“react-native-contacts”: “3.1.5”,

  Here’s the link to the Github repo if you want to check it out: https://github....'
---

Par Melih Yumak

#### Versions

Avant de commencer, assurez-vous d'avoir les versions suivantes installées :

"react" : "16.8.3",  
"react-native" : "0.59.1",  
"react-native-contacts" : "3.1.5",

**Voici le lien vers le dépôt Github si vous souhaitez le consulter** : [https://github.com/FormidableLabs/react-native-app-auth](https://github.com/FormidableLabs/react-native-app-auth)

**React-native-app-auth** est utilisé pour fournir une authentification dans vos applications react-native. Dans mon cas, j'essayais de l'utiliser avec Google, voici donc une explication sur la façon de l'installer et de l'utiliser pour les versions ci-dessus.

Dans leur documentation, il est également expliqué comme un pont React Native pour les SDK [AppAuth-iOS](https://github.com/openid/AppAuth-iOS) et [AppAuth-Android](https://github.com/openid/AppAuth-Android) pour communiquer avec les fournisseurs [OAuth 2.0](https://tools.ietf.org/html/rfc6749) et [OpenID Connect](http://openid.net/specs/openid-connect-core-1_0.html).

### Fournisseurs OpenID testés :

Ces fournisseurs sont conformes à OpenID, ce qui signifie que vous pouvez utiliser [autodiscovery](https://openid.net/specs/openid-connect-discovery-1_0.html) :

* [Identity Server4](https://demo.identityserver.io/) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/identity-server-4.md))
* [Identity Server3](https://github.com/IdentityServer/IdentityServer3.md) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/identity-server-3.md))
* [Google](https://developers.google.com/identity/protocols/OAuth2) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/google.md))
* [Okta](https://developer.okta.com/) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/okta.md))
* [Keycloak](http://www.keycloak.org/) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/keycloak.md))
* [Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/azure-active-directory.md))
* [AWS Cognito](https://eu-west-1.console.aws.amazon.com/cognito) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/aws-cognito.md))

### Fournisseurs OAuth2 testés :

Ces fournisseurs implémentent la spécification OAuth2, mais ne sont pas des fournisseurs OpenID, ce qui signifie que vous devez configurer les points de terminaison d'autorisation et de jeton vous-même.

* [Uber](https://developer.uber.com/docs/deliveries/guides/three-legged-oauth.md) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/uber))
* [Fitbit](https://dev.fitbit.com/build/reference/web-api/oauth2/) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/fitbit.md))
* [Dropbox](https://www.dropbox.com/developers/reference/oauth-guide) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/dropbox.md))
* [Reddit](https://github.com/reddit-archive/reddit/wiki/oauth2) ([Exemple de configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/reddit.md))

#### **Installation**

```
npm install react-native-app-auth --save
react-native link react-native-app-auth
```

**iOS**  
Dans la documentation, il y a trois façons d'implémenter cet état, mais je préfère **CocoaPods.**

Si vous utilisez CocoaPods pour la première fois, veuillez suivre les étapes ci-dessous :

```
sudo gem install cocoapods
```

Depuis votre dossier racine, ouvrez

```
cd ios
```

```
pod init
```

La commande pod init initialisera le Podfile dans votre répertoire iOS.

Ajoutez ensuite cette ligne dans votre Podfile après **target 'your_app' do**

```
pod 'AppAuth', '0.95.0'
```

#### **Enregistrer le schéma d'URL de redirection**

Si vous prévoyez de supporter iOS 10 et les versions antérieures, vous devez définir les schémas d'URL de redirection pris en charge dans votre `Info.plist` comme suit :

Note : vous obtiendrez ces valeurs auprès de votre **fournisseur oauth**.   
Pour Google : [https://console.developers.google.com/](https://console.developers.google.com/)

```
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLName</key>
    <string>com.your.app.identifier</string>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>io.identityserver.demo</string>
    </array>
  </dict>
</array>
```

* `CFBundleURLName` est une chaîne globalement unique. Une pratique courante consiste à utiliser l'identifiant de votre application.
* `CFBundleURLSchemes` est un tableau de schémas d'URL que votre application doit gérer. Le schéma est le début de votre URL de redirection OAuth, jusqu'au caractère séparateur de schéma (`:`).

#### **Définir le rappel openURL dans AppDelegate**

Vous devez conserver la session d'authentification afin de continuer le flux d'autorisation depuis la redirection. Suivez ces étapes :

Faites en sorte que `AppDelegate` se conforme à `RNAppAuthAuthorizationFlowManager` avec les modifications suivantes dans `AppDelegate.h` :

```
+ #import "RNAppAuthAuthorizationFlowManager.h"
```

```
- @interface AppDelegate : UIResponder <UIApplicationDelegate>
+ @interface AppDelegate : UIResponder <UIApplicationDelegate, RNAppAuthAuthorizationFlowManager>
```

```
+ @property(nonatomic, weak) id<RNAppAuthAuthorizationFlowManagerDelegate> authorizationFlowManagerDelegate;
```

Modifiez la méthode suivante de `UIApplicationDelegate` dans `AppDelegate.m` :

```
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  return [self.authorizationFlowManagerDelegate resumeExternalUserAgentFlowWithURL:url];
}
```

**Android**

Après un lien réussi, vous devez ajouter la valeur **defaultConfig** du fichier **android/app/build.gradle** comme URL de redirection de vos identifiants.

```
manifestPlaceholders = [
```

```
appAuthRedirectScheme: "io.identityserver.demo"
```

```
]
```

#### Utilisation

```
import { authorize } from 'react-native-app-auth';
```

```
// configuration de base
const config = {
  issuer: '<YOUR_ISSUER_URL>',
  clientId: '<YOUR_CLIENT_ID>',
  redirectUrl: '<YOUR_REDIRECT_URL>',
  scopes: ['<YOUR_SCOPES_ARRAY>'],
};
```

```
// utiliser le client pour faire la demande d'authentification et recevoir le statut d'authentification
try {
  const result = await authorize(config);
  // result inclut accessToken, accessTokenExpirationDate et refreshToken
} catch (error) {
  console.log(error);
}
```

**Bon codage !**

**Merci d'avoir lu jusqu'ici. Si vous avez aimé cet article, partagez-le, commentez-le et appuyez sur ce ? quelques fois (jusqu'à 50 fois). . . Peut-être que cela aidera quelqu'un.**

**Suivez-moi sur Medium ou [Github](https://github.com/hadnazzar) si vous êtes intéressé par des articles plus approfondis et informatifs comme ceux-ci à l'avenir.** ?