---
title: Comment ajouter des appels vidéo à une application React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-22T22:56:21.000Z'
originalURL: https://freecodecamp.org/news/building-video-call-app-in-react-native
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6052f30428094f59be257c13.jpg
tags:
- name: Android
  slug: android
- name: api
  slug: api
- name: iOS
  slug: ios
- name: React Native
  slug: react-native
seo_title: Comment ajouter des appels vidéo à une application React Native
seo_desc: "By Krissanawat\nVideo calling has become an essential day to day activity\
  \ during the COVID-19 pandemic. By using features such as chat apps, audio calling,\
  \ and video calling, we have been able to stay connected with our friends and family.\
  \ \nNow, let's..."
---

Par Krissanawat

Les appels vidéo sont devenus une activité essentielle au quotidien pendant la pandémie de COVID-19. En utilisant des fonctionnalités telles que les applications de chat, les appels audio et les appels vidéo, nous avons pu rester connectés avec nos amis et notre famille.

Maintenant, créons notre propre application React Native qui nous permettra de passer des appels vidéo.

Dans ce tutoriel, nous allons apprendre comment implémenter une fonctionnalité d'appel vidéo dans une application React Native en utilisant l'API Twilio programmable pour les appels vidéo.

Le processus est assez simple. Nous allons simplement créer une salle de conférence vidéo et inviter d'autres personnes à rejoindre cette salle. Pour ce faire, nous aurons besoin d'accéder à la caméra et au microphone. Nous aurons donc besoin d'utiliser un véritable appareil smartphone pour les tests.

Le package principal que nous allons utiliser pour accéder à l'API Twilio est le package [react-native-twilio-video-webrtc](https://github.com/blackuy/react-native-twilio-video-webrtc).

### Prérequis

* [Compte Twilio](https://www.twilio.com/)
* Un minimum de deux appareils iOS ou Android pour les tests.
* [Configuration de l'environnement React Native](https://reactnative.dev/docs/environment-setup).

_C'est parti !_

## Comment obtenir votre clé API Twilio

Pour obtenir votre clé API Twilio, vous aurez besoin d'un compte Twilio. Pour cela, visitez cette [URL](https://www.twilio.com/console/video/project/api-keys/). Après avoir configuré votre compte, vous devez vous rendre à l'emplacement indiqué par la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-1.png)

## Comment configurer le serveur pour gérer la récupération du jeton d'accès

Pour récupérer le jeton d'accès, nous devons créer un nouveau projet de serveur Node. Pour cela, nous devons installer les packages nécessaires en exécutant la commande suivante :

```sh
yarn add dotenv express ngrok nodemon twilio
```

Ensuite, nous devons ajouter les informations d'identification Twilio dans le fichier des variables d'environnement .env, comme montré dans l'extrait de code ci-dessous :

```sh
PORT=3000
ACCOUNT_SID=AC5ceb0847c50c91b143ce07
API_KEY_SID=SKa173c10de99a26fd86969b
API_KEY_SECRET=Czv7IjNIZJis8s7jb5FePi
```

Maintenant, nous devons créer un point de terminaison API. Tout d'abord, nous devons importer les packages nécessaires et créer des instances d'objets pour obtenir le jeton d'accès comme indiqué dans l'extrait de code ci-dessous :

```javascript
import 'dotenv/config';
import express from 'express';

import twilio from 'twilio';
import ngrok from 'ngrok';
const AccessToken = twilio.jwt.AccessToken;
const VideoGrant = AccessToken.VideoGrant;

const app = express();
```

Ici, nous allons créer un point de terminaison API pour obtenir le jeton d'accès. En utilisant la méthode get fournie par l'instance Express, nous devons créer une fonction de point de terminaison qui répond avec le jeton d'accès.

À l'intérieur de la fonction, nous devons créer une nouvelle instance avec les informations d'identification Twilio. Ensuite, nous devons ajouter le nom d'utilisateur que nous avons reçu de l'écran d'enregistrement sur l'appareil mobile en tant qu'attribut d'identité.

Enfin, nous accorderons l'accès à l'utilisateur afin qu'il puisse utiliser la vidéo et renvoyer le jeton JWT à l'appareil. Voici le code pour tout cela dans l'extrait ci-dessous :

```javascript
app.get('/getToken', (req, res) => {
  if (!req.query || !req.query.userName) {
    return res.status(400).send('Le paramètre de nom d\'utilisateur est requis');
  }
  const accessToken = new AccessToken(
    process.env.ACCOUNT_SID,
    process.env.API_KEY_SID,
    process.env.API_KEY_SECRET,
  );

  // Définir l'identité de ce jeton
  accessToken.identity = req.query.userName;

  // Accorder l'accès à la vidéo
  var grant = new VideoGrant();
  accessToken.addGrant(grant);

  // Sérialiser le jeton en tant que JWT
  var jwt = accessToken.toJwt();
  return res.send(jwt);
});

```

Nous exposons également le point de terminaison API que nous avons créé sur Internet pour un accès facile. Pour cela, nous pouvons utiliser le code de l'extrait de code suivant :

```powershell
app.listen(process.env.PORT, () =>
  console.log(`Serveur à l'écoute sur le port ${process.env.PORT}!`),
);

ngrok.connect(process.env.PORT).then((url) => {
  console.log(`Serveur redirigé vers l'URL publique ${url}`);
});

```

Enfin, nous devons exécuter le serveur comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-2.png)

Ici, nous avons créé avec succès un point de terminaison API pour retourner le jeton d'accès.

## Comment configurer notre projet React Native

Dans notre projet React Native, nous devons configurer les packages manuellement ainsi que les permissions pour accéder à la caméra et au microphone pour les plateformes Android et iOS.

Mais d'abord, nous devons installer les packages nécessaires, qui sont `react-navigation` et `react-native-twilio-video-webrtc`, en exécutant la commande suivante dans notre terminal de projet :

```powershell
yarn add @react-navigation/native @react-navigation/stack react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view react-native-dotenv react-native-permissions <https://github.com/blackuy/react-native-twilio-video-webrtc>

```

### Configuration pour iOS

Pour iOS, nous devons configurer le package manuellement. Tout d'abord, nous devons incrémenter la **cible IOS à 11 dans le Podfile**. Cela est nécessaire car [le SDK vidéo natif de Twilio ne prend en charge que iOS 11.0+](https://www.twilio.com/docs/video/ios#prerequisites) :

```powershell
platform :ios, '11.0'
require_relative '../node_modules/@react-native-community/cli-platform-ios/native_modules'

```

Dans le Podfile, nous devons configurer une demande de permission comme indiqué dans l'extrait de code ci-dessous :

```powershell
permissions_path = '../node_modules/react-native-permissions/ios'
  pod 'Permission-Camera', :path => "#{permissions_path}/Camera.podspec"
  pod 'Permission-Microphone', :path => "#{permissions_path}/Microphone.podspec"

```

Ensuite, nous devons ouvrir info.plist et ajouter du code pour demander la permission d'accès à la caméra et au microphone comme indiqué dans l'extrait de code ci-dessous :

```powershell
  <key>UIViewControllerBasedStatusBarAppearance</key>
	<false/>
  <key>NSCameraUsageDescription</key>
  <string>Nous avons besoin de votre permission pour accéder à la caméra pendant un appel vidéo</string>
  <key>NSMicrophoneUsageDescription</key>
  <string>Nous avons besoin de votre permission pour accéder au microphone pendant un appel vidéo</string>

```

Maintenant, nous avons terminé notre configuration iOS.

### Configuration pour Android

Tout d'abord, nous devons ajouter la ligne de code suivante au fichier **./android/settings.gradle** :

```dart
project(':react-native-twilio-video-webrtc').projectDir = new File(rootProject.projectDir, '../node_modules/react-native-twilio-video-webrtc/android')

```

De plus, nous devons ajouter le code d'implémentation du package au fichier **./android/app/build.gradle** :

```dart
implementation project(':react-native-twilio-video-webrtc')

```

Enfin, nous devons également importer cela dans le fichier **[MainApplication.java](http://mainapplication.java)** :

```dart
import com.twiliorn.library.TwilioPackage;

```

Ensuite, nous devons activer le package en utilisant le morceau de code suivant :

```dart
@Override
protected List getPackages() {
  @SuppressWarnings("UnnecessaryLocalVariable")
  List packages = new PackageList(this).getPackages();
  //  ajouter le code suivant
  packages.add(new TwilioPackage());
  return packages;
}

```

### Comment construire l'écran d'enregistrement de la salle

Ici, nous allons créer un écran appelé "Register Room" qui nous permettra de nous enregistrer dans une salle dans notre application React Native d'appel vidéo.

Tout d'abord, nous devons importer les packages nécessaires comme montré dans l'extrait de code ci-dessous :

```jsx
import React, {useState, useRef, useEffect, useContext} from 'react';
import {
  StyleSheet,
  View,
  Text,
  StatusBar,
  TouchableOpacity,
  TextInput,
  Alert,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
  Dimensions,
} from 'react-native';

import {
  TwilioVideoLocalView,
  TwilioVideoParticipantView,
  TwilioVideo,
} from 'react-native-twilio-video-webrtc';

import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';

```

* react-navigation : Pour gérer la navigation de l'écran d'enregistrement et de l'écran d'appel vidéo.
* react-native : Ce package nous permet de gérer les permissions pour accéder à la caméra et au microphone.
* react-native-twilio-video-webrtc : cela nous permet d'accéder à l'API programmable d'appel vidéo de Twilio.

### Comment initialiser les instances et les variables

Tout d'abord, nous allons créer une instance pour react-navigation. Ensuite, nous allons initialiser les états ainsi que les variables de contexte pour distribuer les états comme montré dans l'extrait de code ci-dessous :

```jsx
const Stack = createStackNavigator();
const initialState = {
  isAudioEnabled: true,
  status: 'disconnected',
  participants: new Map(),
  videoTracks: new Map(),
  userName: '',
  roomName: '',
  token: '',
};

const AppContext = React.createContext(initialState);

const dimensions = Dimensions.get('window');

```

### Bootstrap Navigation

Dans le fichier **App.js**, nous allons créer un conteneur de navigation de pile. En utilisant le composant `Stack`, nous allons distribuer l'état à chaque écran en utilisant le contexte comme indiqué dans l'extrait de code ci-dessous :

```jsx
export default () => {
  const [props, setProps] = useState(initialState);

  return (
    <>
      <StatusBar barStyle="dark-content" />
      <AppContext.Provider value={{props, setProps}}>
        <NavigationContainer>
          <Stack.Navigator>
            <Stack.Screen name="Home" component={HomeScreen} />
            <Stack.Screen name="Video Call" component={VideoCallScreen} />
          </Stack.Navigator>
        </NavigationContainer>
      </AppContext.Provider>
    </>
  );
};

```

### Comment créer l'écran d'enregistrement

L'écran d'enregistrement aura une boîte de dialogue modale pour obtenir les informations d'identification de l'utilisateur et permettre aux utilisateurs de rejoindre la salle d'appel vidéo.

Tout d'abord, nous devons récupérer les props du contexte dans le fichier **register.js** comme montré dans l'extrait de code ci-dessous :

```jsx
import React, {useState, useRef, useEffect, useContext} from 'react';
import {
  checkMultiple,
  request,
  requestMultiple,
  PERMISSIONS,
  RESULTS,
} from 'react-native-permissions';

const RegisterScreen = ({navigation}) => {
  const {props, setProps} = useContext(AppContext);

```

Ensuite, nous devons créer une fonction pour gérer les permissions de la caméra et du microphone. Le code de la fonction est fourni dans l'extrait de code ci-dessous :

```jsx
const _checkPermissions = (callback) => {
    const iosPermissions = [PERMISSIONS.IOS.CAMERA, PERMISSIONS.IOS.MICROPHONE];
    const androidPermissions = [
      PERMISSIONS.ANDROID.CAMERA,
      PERMISSIONS.ANDROID.RECORD_AUDIO,
    ];
    checkMultiple(
      Platform.OS === 'ios' ? iosPermissions : androidPermissions,
    ).then((statuses) => {
      const [CAMERA, AUDIO] =
        Platform.OS === 'ios' ? iosPermissions : androidPermissions;
      if (
        statuses[CAMERA] === RESULTS.UNAVAILABLE ||
        statuses[AUDIO] === RESULTS.UNAVAILABLE
      ) {
        Alert.alert(
          'Erreur',
          'Le matériel pour supporter les appels vidéo n\'est pas disponible',
        );
      } else if (
        statuses[CAMERA] === RESULTS.BLOCKED ||
        statuses[AUDIO] === RESULTS.BLOCKED
      ) {
        Alert.alert(
          'Erreur',
          'La permission d\'accéder au matériel a été bloquée, veuillez accorder manuellement',
        );
      } else {
        if (
          statuses[CAMERA] === RESULTS.DENIED &&
          statuses[AUDIO] === RESULTS.DENIED
        ) {
          requestMultiple(
            Platform.OS === 'ios' ? iosPermissions : androidPermissions,
          ).then((newStatuses) => {
            if (
              newStatuses[CAMERA] === RESULTS.GRANTED &&
              newStatuses[AUDIO] === RESULTS.GRANTED
            ) {
              callback && callback();
            } else {
              Alert.alert('Erreur', 'Une des permissions n\'a pas été accordée');
            }
          });
        } else if (
          statuses[CAMERA] === RESULTS.DENIED ||
          statuses[AUDIO] === RESULTS.DENIED
        ) {
          request(statuses[CAMERA] === RESULTS.DENIED ? CAMERA : AUDIO).then(
            (result) => {
              if (result === RESULTS.GRANTED) {
                callback && callback();
              } else {
                Alert.alert('Erreur', 'Permission non accordée');
              }
            },
          );
        } else if (
          statuses[CAMERA] === RESULTS.GRANTED ||
          statuses[AUDIO] === RESULTS.GRANTED
        ) {
          callback && callback();
        }
      }
    });
  };

```

Ensuite, nous devons appeler cette fonction de vérification des permissions chaque fois que l'application démarre. Pour cela, nous devons appeler la fonction à l'intérieur du hook `useEffect` comme indiqué dans l'extrait de code ci-dessous :

```jsx
useEffect(() => {
    _checkPermissions();
  }, []);

```

Enfin, nous devons créer un formulaire simple avec deux champs qui acceptent le nom de la salle et le nom d'utilisateur. Ensuite, nous devons envoyer les entrées au serveur pour nous enregistrer sur l'API Twilio. Le code pour cela est fourni dans l'extrait de code ci-dessous :

```jsx
return (
    <KeyboardAvoidingView
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      style={styles.container}>
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.form}>
          <View style={styles.formGroup}>
            <Text style={styles.text}>Nom d'utilisateur</Text>
            <TextInput
              style={styles.textInput}
              autoCapitalize="none"
              value={props.userName}
              onChangeText={(text) => setProps({...props, userName: text})}
            />
          </View>
          <View style={styles.formGroup}>
            <Text style={styles.text}>Nom de la salle</Text>
            <TextInput
              style={styles.textInput}
              autoCapitalize="none"
              value={props.roomName}
              onChangeText={(text) => setProps({...props, roomName: text})}
            />
          </View>
          <View style={styles.formGroup}>
            <TouchableOpacity
              disabled={false}
              style={styles.button}
              onPress={() => {
                _checkPermissions(() => {
                  fetch(`https://ae7a722dc260.ngrok.io/getToken?userName=${props.userName}`)
                    .then((response) => {
                      if (response.ok) {
                        response.text().then((jwt) => {
                          setProps({...props, token: jwt});
                          navigation.navigate('Video Call');
                          return true;
                        });
                      } else {
                        response.text().then((error) => {
                          Alert.alert(error);
                        });
                      }
                    })
                    .catch((error) => {
                      console.log('error', error);
                      Alert.alert('API non disponible');
                    });
                });
              }}>
              <Text style={styles.buttonText}>Se connecter à l'appel vidéo</Text>
            </TouchableOpacity>
          </View>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );

```

Nous obtiendrons le résultat comme montré dans la capture d'écran de l'émulateur ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/home-screen.png)

Ici, nous pouvons voir notre écran d'enregistrement de salle avec un formulaire modal où nous pouvons entrer le nom de la salle et le nom d'utilisateur afin de nous enregistrer sur l'API Twilio en cours d'exécution sur le serveur.

### Comment construire l'écran d'appel vidéo

Dans l'écran d'appel vidéo, nous allons avoir deux fenêtres : une pour afficher notre propre vue de caméra, et l'autre pour afficher la vue de la caméra du destinataire.

Tout d'abord, nous devons initialiser le contexte pour accepter les états. Ensuite, nous créerons une variable de référence en utilisant le hook `useRef` pour accéder aux états comme indiqué dans l'extrait de code ci-dessous :

```jsx
const VideoCallScreen = ({navigation}) => {
  const twilioVideo = useRef(null);
  const {props, setProps} = useContext(AppContext);

```

Ensuite, nous devons initialiser la connexion en utilisant la méthode `connect` de l'objet `twilioVideo`, en fournissant le nom de la salle et le jeton d'accès comme indiqué dans l'extrait de code ci-dessous :

```jsx
useEffect(() => {
    twilioVideo.current.connect({
      roomName: props.roomName,
      accessToken: props.token,
    });
    setProps({...props, status: 'connecting'});
    return () => {
      _onEndButtonPress();
    };
  }, []);

```

Maintenant, nous devons créer le modèle de corps principal pour l'écran d'appel vidéo. Ici, nous affichons la vue de la caméra du participant uniquement lorsque la connexion est établie et en streaming en utilisant le rendu conditionnel. Le code global pour cela est fourni dans l'extrait de code ci-dessous :

```jsx
{(props.status === 'connected' || props.status === 'connecting') && (
        <View style={styles.callWrapper}>
          {props.status === 'connected' && (
            <View style={styles.grid}>
              {Array.from(props.videoTracks, ([trackSid, trackIdentifier]) => (
                <TwilioVideoParticipantView
                  style={styles.remoteVideo}
                  key={trackSid}
                  trackIdentifier={trackIdentifier}
                />
              ))}
            </View>
          )}
        </View>
      )}

```

Ensuite, nous devons créer des fonctions pour contrôler les fonctionnalités en appel vidéo telles que la fin de l'appel, le muting et le basculement entre les caméras avant et arrière. L'implémentation du codage des fonctions requises est fournie dans l'extrait de code ci-dessous :

```jsx
const _onEndButtonPress = () => {
    twilioVideo.current.disconnect();
    setProps(initialState);
  };

  const _onMuteButtonPress = () => {
    twilioVideo.current
      .setLocalAudioEnabled(!props.isAudioEnabled)
      .then((isEnabled) => setProps({...props, isAudioEnabled: isEnabled}));
  };

  const _onFlipButtonPress = () => {
    twilioVideo.current.flipCamera();
  };

```

Ici, nous avons utilisé les méthodes `disconnect`, `setLocalAudioEnabled` et `flipCamera` fournies par l'instance `twilioVideo` pour déclencher les fonctionnalités en appel vidéo requises.

Maintenant, nous devons afficher quelques boutons pour déclencher les fonctions. Pour cela, nous devons utiliser le code de l'extrait de code suivant :

```jsx
       <View style={styles.optionsContainer}>
        <TouchableOpacity style={styles.button} onPress={_onEndButtonPress}>
          <Text style={styles.buttonText}>Fin</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={_onMuteButtonPress}>
          <Text style={styles.buttonText}>
            {props.isAudioEnabled ? 'Muet' : 'Activer le son'}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={_onFlipButtonPress}>
          <Text style={styles.buttonText}>Retourner</Text>
        </TouchableOpacity>
      </View>

```

La dernière étape consiste à ajouter le composant `TwilioVideo` qui est configuré pour gérer et observer tous les événements d'appel vidéo. Le composant `TwilioVideo` configuré globalement est fourni dans l'extrait de code ci-dessous :

```jsx
      <TwilioVideo
        ref={twilioVideo}
        onRoomDidConnect={() => {
          setProps({...props, status: 'connected'});
        }}
        onRoomDidDisconnect={() => {
          setProps({...props, status: 'disconnected'});
          navigation.goBack();
        }}
        onRoomDidFailToConnect={(error) => {
          Alert.alert('Erreur', error.error);
          setProps({...props, status: 'disconnected'});
          navigation.goBack();
        }}
        onParticipantAddedVideoTrack={({participant, track}) => {
          if (track.enabled) {
            setProps({
              ...props,
              videoTracks: new Map([
                ...props.videoTracks,
                [
                  track.trackSid,
                  {
                    participantSid: participant.sid,
                    videoTrackSid: track.trackSid,
                  },
                ],
              ]),
            });
          }
        }}
        onParticipantRemovedVideoTrack={({track}) => {
          const videoTracks = props.videoTracks;
          videoTracks.delete(track.trackSid);
          setProps({...props, videoTracks});
        }}
      />

```

Nous obtiendrons le résultat suivant si nous sommes en mesure d'établir la connexion appropriée entre les utilisateurs dans une salle :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/ffff-1.png)

Les captures d'écran ci-dessus démontrent un appel vidéo entre deux participants dans une salle.

Avec cela, nous avons implémenté avec succès la fonctionnalité d'appel vidéo dans notre application React Native.

## Conclusion

Ce tutoriel visait à fournir une ressource d'apprentissage de niveau débutant sur la façon de configurer les appels vidéo dans une application React Native. Nous l'avons fait en utilisant l'API programmable d'appel vidéo de Twilio.

Nous avons couvert non seulement la partie React Native, mais aussi l'implémentation globale de l'API dans un projet de serveur Node séparé.

Maintenant, la prochaine étape peut être d'ajouter des fonctionnalités avancées telles que le démarrage d'un appel anonyme ou des salles d'appel vidéo à plusieurs participants.

Pour l'inspiration des fonctionnalités et une application d'appel vidéo appropriée, vous pouvez consulter [instamobile.io](http://instamobile.io) qui offre un état d'une [application de chat vidéo](https://www.instamobile.io/app-templates/video-chat-app-in-react-native/) avec des fonctionnalités puissantes.

_À la prochaine, les gars, bon codage !_