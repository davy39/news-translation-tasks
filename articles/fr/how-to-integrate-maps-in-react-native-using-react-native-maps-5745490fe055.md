---
title: Comment intégrer des cartes dans React Native en utilisant react-native-maps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T20:37:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-maps-in-react-native-using-react-native-maps-5745490fe055
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qp8QiCRmx0D041XU4qhx4g.png
tags:
- name: maps
  slug: maps
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment intégrer des cartes dans React Native en utilisant react-native-maps
seo_desc: 'By Mukhamed Khasanza

  Nowadays, almost all mobile applications have a maps feature. I had to integrate
  Google Maps to my React Native application, and the only choice was react-native-maps
  by Airbnb (it’s the only one still supported by the React Nati...'
---

Par Mukhamed Khasanza

De nos jours, presque toutes les applications mobiles disposent d'une fonctionnalité de cartes. J'ai dû intégrer Google Maps à mon application React Native, et le seul choix était react-native-maps par Airbnb (c'est le seul encore soutenu par la communauté React Native).

J'ai trouvé plusieurs tutoriels sur la façon de configurer cette bibliothèque, mais aucun n'a complètement fonctionné pour moi. Cela était dû au fait que je devais exécuter sur les plateformes iOS et Android et également prendre en charge Google Maps pour iOS.

Créons une application React Native à partir de zéro en utilisant **react-native-cli** pour montrer, étape par étape, comment tout est installé. Si vous souhaitez intégrer react-native-maps pour votre application existante, passez à l'**Étape 1**.

#### Étape 1 : Installer et configurer l'application React Native

Si vous n'avez pas installé l'interface de ligne de commande React Native, exécutez : `npm install -g react-native-cli`. Vous pouvez maintenant créer votre projet, simplement en utilisant : `react-native init ReactNativeMaps`

Voici les versions des dépendances au moment de la construction de ce projet :

* "react" : "16.6.1"
* "react-native" : "0.57.5"
* "react-native-maps" : "0.22.1" — nous installerons celui-ci plus tard.

Vous pouvez maintenant essayer d'exécuter votre application, `react-native run-ios` ou `react-native run-android`. Habituellement, cela fonctionne sans aucun problème.

#### Étape 2 : Ajouter et lier le package react-native-maps

Maintenant, installons react-native-map : `npm install --save react-native-maps` après avoir installé le package, vous devez le lier à vos applications natives : `react-native link react-native-maps`.

![Image](https://cdn-media-1.freecodecamp.org/images/UIyvyNDxVXBMQeYn9Wno72ob5T8iqR7Cr1c3)
_Vous avez aussi obtenu cela ? Cool, maintenant nous pouvons continuer._

#### Étape 3 : Configurer Apple Maps (iOS)

Il sera plus facile si nous les configurons séparément par plateforme, alors commençons par iOS. Avant d'intégrer Google Maps, nous vérifierons si Apple Maps fonctionne correctement. Ajoutez le code suivant à votre composant de rendu actuel où vous souhaitez rendre votre MapView.

```
import MapView from 'react-native-maps'
```

```
export default class App extends Component<Props> {  render() {    return (      <MapView        style={{flex: 1}}        region={{          latitude: 42.882004,          longitude: 74.582748,          latitudeDelta: 0.0922,          longitudeDelta: 0.0421        }}        showsUserLocation={true}      />    );  }}
```

Vous pouvez tester n'importe quel emplacement que vous souhaitez, il suffit de spécifier la latitude et la longitude appropriées. Comme vous pouvez le voir, j'ai activé la localisation de l'utilisateur simplement en ajoutant la prop `showUserLocation` au composant MapView. Si vous exécutez sur un appareil réel, vous verrez votre position actuelle.

![Image](https://cdn-media-1.freecodecamp.org/images/qtVkxY6KL4FhpwLUbEbBeqN8o6o7poi1ewRF)

Ainsi, comme vous pouvez le voir, par défaut, Apple Maps fonctionne déjà. De plus, si vous avez tout lié correctement et activé la localisation de l'utilisateur, cela a en fait fait beaucoup de choses pour nous (la permission de l'utilisateur pour la localisation avec un message par défaut). Si vous venez du développement natif iOS, alors vous savez probablement ce qu'est un fichier info.plist.

#### Étape 4 : Installer Cocoapods et le package 'GoogleMaps' (iOS)

Apple Maps était facile, n'est-ce pas ? D'accord — voyons ce que Google Maps nous réserve. Nous devons installer le SDK Google Maps pour iOS. Nous utiliserons Cocoapods. Si vous ne l'avez pas utilisé auparavant, exécutez `sudo gem install cocoapods`.

Maintenant, vous devez créer un Podfile où vous spécifierez les dépendances de votre application iOS. Naviguez vers votre dossier iOS/ dans votre application React Native et exécutez : `pod init` ou vous pouvez utiliser `touch Podfile`, vous devriez avoir quelque chose de similaire à ceci :

```
# platform :ios, '9.0'
```

```
target 'ReactNativeMaps' do
```

```
# Pods pour ReactNativeMaps
```

```
pod 'GoogleMaps'
```

```
end
```

Comme vous pouvez le voir, j'ai ajouté le pod GoogleMaps et maintenant nous devons l'installer. Si vous êtes toujours dans le dossier iOS/, exécutez : `pod install`. Si vous essayez de l'exécuter maintenant, vous obtiendrez probablement une erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/soaOtijGp-7CiGQVsNiwgljfHyLEQvrDJvEg)

D'accord, faisons ce qu'il veut. Maintenant, nous devons ouvrir l'espace de travail xCode.

![Image](https://cdn-media-1.freecodecamp.org/images/Vr6q4qYXaiFqnHdGtSNnhKSIZFqCMCFVeVEI)

Naviguez vers le dossier AirGoogleMaps depuis node_modules/

![Image](https://cdn-media-1.freecodecamp.org/images/Taoc1pnk-dNBMzyAmjjE3CO8AkOm8t9KQhXf)

Et faites-le glisser en haut de votre projet xCode

![Image](https://cdn-media-1.freecodecamp.org/images/ewvVl0gCwzwrNj1gd3itRZnWJVPGOCiKkdSo)

Veuillez essayer de construire votre projet xCode, si vous échouez

![Image](https://cdn-media-1.freecodecamp.org/images/6aQVp2Zl6gKnE6d3DdqMULm2WHmp70ws6QBE)

Vous devez ajouter `HAVE_GOOGLE_MAPS=1` Macro de préprocesseur aux Paramètres de construction

![Image](https://cdn-media-1.freecodecamp.org/images/IhgPZQBomXmc4UKlP4ynYNIoU3Y0hlyGivGc)

#### Étape 5 : Obtenir la clé API Google Maps, exécuter l'application iOS avec Google Maps

Maintenant, nous devons générer une [**clé API Google Maps**](https://developers.google.com/maps/documentation/ios-sdk/get-api-key).

![Image](https://cdn-media-1.freecodecamp.org/images/dnmuyvL7Nd99BHxkK2F4iUCBbBeoypyPVfyw)

Copiez votre clé API et ajoutez-la au fichier AppDelegate.m.

`#import <GoogleMaps/GoogleMaps.h>`

`[GMSServices provideAPIKey:@"YOUR_API_KEY"]`

![Image](https://cdn-media-1.freecodecamp.org/images/oHeCkflMd3zznfYFMPBD6tglu4n9tfnoCghs)

Maintenant, vous pouvez dire à votre composant MapView que vous êtes prêt à utiliser Google Maps.

![Image](https://cdn-media-1.freecodecamp.org/images/EojYRgWTNtO0zlMmicx0EVmv-0dBi22Y3Euf)

Oh oui, veuillez exécuter votre application iOS. Et vous obtiendrez Google Maps.

Je l'espère.

#### Étape 6 : Essayons Android maintenant

D'accord, maintenant nous pouvons quitter xCode et essayons simplement `react-native run-android`. Si vous obtenez la même chose que ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/PZJ0vNEXuf1F-IUTAx0UAoJcW9rZy9V1FlbR)

vérifiez votre fichier **android/app/build.gradle**. Et remplacez ceci :

`compile project(':react-native-maps')` par ceci :

```
implementation(project(':react-native-maps')){        exclude group: 'com.google.android.gms', module: 'play-services-base'        exclude group: 'com.google.android.gms', module: 'play-services-maps'    }implementation 'com.google.android.gms:play-services-base:12.0.0'implementation 'com.google.android.gms:play-services-maps:12.0.0'
```

Oh, et n'oubliez pas d'ajouter API_KEY au fichier AndroidManifest.xml.

```
<application>   <meta-data      android:name="com.google.android.geo.API_KEY"      android:value="YOUR_API_KEY"/></application>
```

Oui, maintenant votre application s'exécute sur les deux plateformes. Veuillez consulter le dépôt [**react-native-maps**](https://github.com/react-community/react-native-maps/blob/master/README.md) pour plus de choses amusantes que vous pouvez faire avec votre composant MapView.

#### Conclusion

J'espère que mon premier article sur Medium vous a été utile. S'il vous plaît, si vous voyez des erreurs, n'hésitez pas à laisser un commentaire, j'apprécierai vos commentaires !