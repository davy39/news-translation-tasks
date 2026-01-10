---
title: Comment créer une application de caméra avec Expo et React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-21T00:36:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-camera-app-with-expo-and-react-native
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9825740569d1a4ca186e.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Photography
  slug: photography
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: Comment créer une application de caméra avec Expo et React Native
seo_desc: 'By Said Hayani

  If you are not familiar with expo, it''s a client that helps you build React Native
  apps with less build complexity. It also helps you deal with the stress of installing
  and setting up your environment to run React Native.

  In this tutor...'
---

Par Said Hayani

Si vous n'êtes pas familier avec [expo](https://expo.io/), c'est un client qui vous aide à construire des applications React Native avec moins de complexité de construction. Il vous aide également à gérer le stress de l'installation et de la configuration de votre environnement pour exécuter React Native.

Dans ce tutoriel, nous allons construire une application de caméra simple dans laquelle l'utilisateur peut prendre des photos, voir les aperçus de leurs photos, utiliser le mode flash et basculer entre les caméras avant et arrière.

## Prérequis

Expo ne nécessite pas beaucoup de choses pour commencer à construire votre première application React Native. Vous pouvez en savoir plus sur l'installation [d'expo et de l'expo-cli ici dans la documentation](https://docs.expo.io/get-started/installation/).

Note : dans ce tutoriel, j'utiliserai macOS et iOS. Vous pouvez également utiliser Android, il n'y a pas beaucoup de différence lorsque vous utilisez expo à ce stade.

Vous pouvez installer expo et expo-cli globalement en exécutant la commande suivante :

```shell
npm install --global expo-cli
```

Expo nécessite [Nodejs](https://nodejs.org/en/) pour fonctionner. Vous pouvez exécuter la dernière version sur le site officiel [ici](https://nodejs.org/en/).

## Getting Started

Après avoir installé Expo et Nodejs, vous pouvez commencer à initialiser un nouveau projet Expo avec la commande ci-dessous :

```shell
expo init expo-camera-app
```

### Comment installer les packages et exécuter l'application

Expo nous fournit une application cliente où nous pouvons exécuter et voir l'aperçu de l'application que nous construisons. Elle est disponible à la fois sur l'[App Store](https://apps.apple.com/us/app/expo-client/id982107779) et [Google Play](https://play.google.com/store/apps/details?id=host.exp.exponent) pour le téléchargement.

Voici l'interface de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/IMG_5488.PNG)

### Comment initialiser un projet expo

Allez dans le répertoire de l'application et exécutez l'application.

```shell
cd expo-camera-app


```

Vous serez invité à répondre à quelques questions pour sélectionner le modèle par défaut pour l'application. Dans ce tutoriel, nous sélectionnons simplement une option vide (TypeScript), mais vous êtes libre de choisir ce qui vous convient.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-10-18-at-5.06.18-PM.png)

### Exécuter l'application

Après avoir initialisé le projet, nous pouvons exécuter l'application avec `expo run`

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-10-18-at-4.52.46-PM.png)

Cela ouvrira une fenêtre dans votre navigateur où vous pourrez voir les logs. Cela générera également un code QR que vous pourrez scanner pour exécuter l'application sur votre appareil.

Le bon côté d'Expo est que vous n'avez pas besoin d'installer et de configurer les simulateurs pour exécuter l'application. Il vous donne toujours la possibilité d'exécuter Expo sur le simulateur, mais vous devez installer et configurer le simulateur vous-même.

Revenons à notre application. En supposant que vous avez réussi à exécuter l'application sur l'appareil, voici l'écran par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/IMG_5489.PNG)

Ouvrez le répertoire de l'application dans votre éditeur de code préféré. J'utilise [VS Code](https://code.visualstudio.com/).

Le fichier `App.tsx` ressemblera à ceci :

```jsx
import {StatusBar} from 'expo-status-bar'
import React from 'react'
import {StyleSheet, Text, View} from 'react-native'

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Open up App.tsx to start working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center'
  }
})

```

## Comment créer l'interface utilisateur

Après avoir fait fonctionner le projet, il est maintenant temps de commencer à créer une interface utilisateur.

### Installer expo-camera

L'étape suivante consiste à installer [expo-camera](https://docs.expo.io/versions/latest/sdk/camera/), comme ceci :

```shell
expo install expo-camera
```

Nous allons créer une interface utilisateur simple qui permettra à l'utilisateur de démarrer le processus d'utilisation de la caméra.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/IMG_5490.PNG)

```jsx
import {StatusBar} from 'expo-status-bar'
import React from 'react'
import {StyleSheet, Text, View, TouchableOpacity} from 'react-native'

export default function App() {
  return (
    <View style={styles.container}>
      <View
        style={{
          flex: 1,
          backgroundColor: '#fff',
          justifyContent: 'center',
          alignItems: 'center'
        }}
      >
        <TouchableOpacity
          style={{
            width: 130,
            borderRadius: 4,
            backgroundColor: '#14274e',
            flexDirection: 'row',
            justifyContent: 'center',
            alignItems: 'center',
            height: 40
          }}
        >
          <Text
            style={{
              color: '#fff',
              fontWeight: 'bold',
              textAlign: 'center'
            }}
          >
            Prendre une photo
          </Text>
        </TouchableOpacity>
      </View>

      <StatusBar style="auto" />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center'
  }
})

```

C'est une interface utilisateur simple : nous importons `TouchableOpacity` pour le bouton et faisons un peu de style simple. Si vous vous demandez comment fonctionne le style dans React Native, vous pouvez consulter mes deux articles ici :

* [Styling in React Native](https://blog.bitsrc.io/styling-in-react-native-c48caddfbe47)
* [Demystifying Flexbox in React Native](https://blog.bitsrc.io/demystifying-flexbox-in-react-native-4b62979fa9ea)

Maintenant, nous devons utiliser un hook `useState` pour gérer l'état et afficher la vue de la caméra lorsque l'utilisateur appuie sur le bouton **prendre une photo**.

```jsx
  <TouchableOpacity
        onPress={__startCamera}
          style={{
            width: 130,
            borderRadius: 4,
            backgroundColor: '#14274e',
            flexDirection: 'row',
            justifyContent: 'center',
            alignItems: 'center',
            height: 40
          }}
        >
          <Text
            style={{
              color: '#fff',
              fontWeight: 'bold',
              textAlign: 'center'
            }}
          >
            Prendre une photo
          </Text>
        </TouchableOpacity>
```

```jsx
  const [startCamera,setStartCamera] = React.useState(false)

const __startCamera = ()=>{

}
```

Il y a deux choses importantes que nous devons faire lorsque l'utilisateur appuie sur le bouton :

* Demander la permission d'accéder à la caméra. Dans le développement mobile, l'accès à de nombreuses API natives et fonctionnalités mobiles est souvent restreint par les permissions de l'utilisateur et la confidentialité. C'est juste quelque chose auquel vous devez vous habituer lorsque vous développez des applications mobiles.
* Changer l'état et présenter la caméra.

Importons le module de la caméra depuis `expo-camera` avec cette commande :

```jsx
import {Camera} from 'expo-camera'
```

Et ajoutons la vue de la caméra, comme ceci :

```jsx
    <Camera
    style={{flex: 1,width:"100%"}}
    ref={(r) => {
    camera = r
    }}
    ></Camera>
```

Nous pouvons utiliser `ref` pour accéder aux méthodes de la caméra :

```jsx
let camera: Camera
```

Lorsque le bouton **prendre une photo** est pressé, la fonction `__startCamera` sera appelée :

```jsx
  const __startCamera = async () => {
    const {status} = await Camera.requestPermissionsAsync()
 if(status === 'granted'){
   // faire quelque chose

 }else{
   Alert.alert("Accès refusé")
 }
```

La fonction demandera d'abord la permission. Si l'utilisateur accorde l'accès à la caméra, nous pouvons procéder et ouvrir la caméra. Sinon, nous affichons une simple alerte.

### Ajouter le composant de la caméra

Affichons la caméra lorsque l'utilisateur accorde l'accès à la caméra de l'appareil.

```jsx
  const __startCamera = async () => {
    const {status} = await Camera.requestPermissionsAsync()
    if (status === 'granted') {
      // démarrer la caméra
      setStartCamera(true)
    } else {
      Alert.alert('Accès refusé')
    }
  }
```

Nous devons apporter quelques modifications à l'interface utilisateur et ajouter un rendu conditionnel. Nous affichons la caméra uniquement lorsque l'utilisateur la demande, sinon nous affichons l'écran par défaut.

```
  {startCamera ? (
        <Camera
          style={{flex: 1,width:"100%"}}
          ref={(r) => {
            camera = r
          }}
        ></Camera>
      ) : (
        <View
          style={{
            flex: 1,
            backgroundColor: '#fff',
            justifyContent: 'center',
            alignItems: 'center'
          }}
        >
          <TouchableOpacity
            onPress={__startCamera}
            style={{
              width: 130,
              borderRadius: 4,
              backgroundColor: '#14274e',
              flexDirection: 'row',
              justifyContent: 'center',
              alignItems: 'center',
              height: 40
            }}
          >
            <Text
              style={{
                color: '#fff',
                fontWeight: 'bold',
                textAlign: 'center'
              }}
            >
              Prendre une photo
            </Text>
          </TouchableOpacity>
        </View>
      )}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/expo-camera.gif)



Super, maintenant nous devons ajouter un bouton pour pouvoir prendre la photo réelle.

### Ajouter le bouton de capture

![Image](https://www.freecodecamp.org/news/content/images/2020/10/IMG_5495.PNG)

C'est une simple `View` à l'intérieur de la vue de la caméra qui a une position absolue. Ainsi, nous nous assurons qu'elle est toujours au-dessus de la caméra.

```jsx
    <View
        style={{
        position: 'absolute',
        bottom: 0,
        flexDirection: 'row',
        flex: 1,
        width: '100%',
        padding: 20,
        justifyContent: 'space-between'
        }}
      >
        <View
        style={{
        alignSelf: 'center',
        flex: 1,
        alignItems: 'center'
        }}
        >
            <TouchableOpacity
            onPress={__takePicture}
            style={{
            width: 70,
            height: 70,
            bottom: 0,
            borderRadius: 50,
            backgroundColor: '#fff'
            }}
            />
    </View>
    </View>
```

### Comment prendre une photo

L'application doit prendre une photo lorsque le bouton de capture est pressé. Cette fonction ressemblera à ceci :

```jsx
  const __takePicture = async () => {
    if (!camera) return
    const photo = await camera.takePictureAsync()
   
  }
```

Tout d'abord, nous vérifions que nous avons accès au composant `Camera` en utilisant `ref` :

```jsx
  if (!camera) return
  // si la caméra est indéfinie ou nulle, nous arrêtons l'exécution de la fonction
```

Ensuite, nous prenons la photo en appelant la méthode `takePictureAsync`. Elle retourne une promesse et un objet qui contient les détails de la photo. Le résultat ressemblera à ceci :

```js
Object {
  "height": 4224,
  "uri": "file:///var/mobile/Containers/Data/Application/E6740A15-93AF-4120-BF11-6E8B74AFBF93/Library/Caches/ExponentExperienceData/%2540anonymous%252Fcamera-app-ee0fa3c8-1bb1-4d62-9863-33bf26341c55/Camera/19F0C5DD-7CA6-4043-8D89-AF65A1055C7E.jpg",
  "width": 1952,
}
```

Nous nous intéressons uniquement à l'URL de la photo `uri`. Après avoir pris une photo, nous devons montrer l'aperçu de la photo et masquer la vue de la caméra. Pour cela, nous utiliserons deux hooks pour changer l'état :

```jsx
  const [previewVisible, setPreviewVisible] = useState(false)
  const [capturedImage, setCapturedImage] = useState<any>(null)
```

```
  const __takePicture = async () => {
    if (!camera) return
    const photo = await camera.takePictureAsync()
    console.log(photo)
    setPreviewVisible(true)
    setCapturedImage(photo)
  }
```

* `setPreviewVisible` pour afficher l'aperçu
* `setCapturedImage(photo)` pour stocker le résultat de l'objet

Ensuite, nous affichons l'aperçu comme ceci :

```jsx
  {previewVisible && capturedImage ? (
            <CameraPreview photo={capturedImage} />
          ) : (
            <Camera
              style={{flex: 1}}
              ref={(r) => {
                camera = r
              }}
            >
              <View
                style={{
                  flex: 1,
                  width: '100%',
                  backgroundColor: 'transparent',
                  flexDirection: 'row'
                }}
              >
                <View
                  style={{
                    position: 'absolute',
                    bottom: 0,
                    flexDirection: 'row',
                    flex: 1,
                    width: '100%',
                    padding: 20,
                    justifyContent: 'space-between'
                  }}
                >
                  <View
                    style={{
                      alignSelf: 'center',
                      flex: 1,
                      alignItems: 'center'
                    }}
                  >
                    <TouchableOpacity
                      onPress={__takePicture}
                      style={{
                        width: 70,
                        height: 70,
                        bottom: 0,
                        borderRadius: 50,
                        backgroundColor: '#fff'
                      }}
                    />
                  </View>
                </View>
              </View>
            </Camera>
          )}
```

Le composant `CameraPreview` ressemble à ceci :

```jsx
const CameraPreview = ({photo}: any) => {
  console.log('sdsfds', photo)
  return (
    <View
      style={{
        backgroundColor: 'transparent',
        flex: 1,
        width: '100%',
        height: '100%'
      }}
    >
      <ImageBackground
        source={{uri: photo && photo.uri}}
        style={{
          flex: 1
        }}
      />
    </View>
  )
}
```

Et le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/preview-camera.gif)

### Comment reprendre une photo

Nous pouvons ajouter des boutons à l'aperçu qui permettront à l'utilisateur d'effectuer plus d'actions. Par exemple, ils pourraient reprendre la photo ou l'enregistrer.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/IMG_5499.PNG)

Ajoutez les props `savePhoto` et `retakePicture` au composant `CameraPreview` comme ceci :

```
<CameraPreview photo={capturedImage} savePhoto={__savePhoto} retakePicture={__retakePicture} />
```

Lorsque le bouton **Reprendre** est pressé, nous devons masquer l'aperçu, supprimer la photo actuelle et afficher à nouveau la caméra. Faites cela avec le code suivant :

```jsx
  const __retakePicture = () => {
    setCapturedImage(null)
    setPreviewVisible(false)
    __startCamera()
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/10/re-take-preview.gif)

## Comment ajouter d'autres options – caméra arrière, flash, et plus

**expo-camra** offre de nombreuses options pour personnaliser la caméra, comme FlashMode, définir le type de caméra (avant/arrière), zoomer, etc.

### Comment ajouter FlashMode

Ajoutons une option pour que l'utilisateur puisse activer et désactiver le FlashMode :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/flashmode-expo-camera.gif)

Nous créons simplement un petit bouton pour activer/désactiver le flash, comme ceci :

```jsx
        <TouchableOpacity
            onPress={__handleFlashMode}
            style={{
            position: 'absolute',
            left: '5%',
            top: '10%',
            backgroundColor: flashMode === 'off' ? '#000' : '#fff',
            borderRadius: '50%',
            height: 25,
            width: 25
        }}
        >
            <Text
                style={{
                fontSize: 20
                }}
            >
            ⚡️
            </Text>
        </TouchableOpacity>
```

Et nous changeons simplement l'état lorsque le bouton est pressé :

```js
  const [flashMode, setFlashMode] = React.useState('off')
  
   const __handleFlashMode = () => {
    if (flashMode === 'on') {
      setFlashMode('off')
    } else if (flashMode === 'off') {
      setFlashMode('on')
    } else {
      setFlashMode('auto')
    }

  }
```

Et ensuite nous ajoutons les props FlashMode :

```jsx
    <Camera
    flashMode={flashMode}
    style={{flex: 1}}
    ref={(r) => {
    camera = r
    }}
    ></Camera>
```

### Comment accéder à la caméra avant et arrière

Nous allons ajouter un bouton qui bascule entre la caméra arrière et avant.

Nous pouvons obtenir le type de caméra par défaut directement depuis le module de la caméra comme ci-dessous :

```
  const [cameraType, setCameraType] = React.useState(Camera.Constants.Type.back)
```

Ajoutez les props `type` comme ceci :

```jsx
    <Camera
    type={cameraType}
    flashMode={flashMode}
    style={{flex: 1}}
    ref={(r) => {
    camera = r
    }}
    ></Camera>
```

Et ajoutez le bouton de bascule :

```jsx
<TouchableOpacity
    onPress={__switchCamera}
    style={{
    marginTop: 20,
    borderRadius: '50%',
    height: 25,
    width: 25
    }}
   >
       <Text
           style={{
           fontSize: 20
           }}
           >
       {cameraType === 'front' ? '?' : '?'}
       </Text>
</TouchableOpacity>
```

Et la fonction de bascule :

```jsx
  const __switchCamera = () => {
    if (cameraType === 'back') {
      setCameraType('front')
    } else {
      setCameraType('back')
    }
  }
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/camera-type-expo.gif)

Vous pouvez trouver le code source complet sur [GitHub](https://github.com/hayanisaid/expo-camera-tutorial/tree/master).

## Conclusion

En général, Expo est un outil incroyable qui peut vous faire gagner beaucoup de temps. Il vous aide à commencer à construire directement et vous évite la douleur de la configuration de l'environnement.

Parfois, vous pouvez vouloir construire une extension native et gérer l'utilisation des fonctionnalités natives à votre manière. Dans ce cas, je recommande d'utiliser le [react-native](https://github.com/react-native-community/cli) CLI afin que vous puissiez modifier et jouer avec le code natif facilement.

> Bonjour, je m'appelle Said Hayani. J'ai créé [subscribi.io](https://subscribi.io/) pour aider les créateurs, blogueurs et influenceurs à développer leur audience grâce à la newsletter.

Rejoignez ma [liste de diffusion](https://subscribi.io/subscribe/5f63b2b306cb71c069272c47) si vous êtes intéressé à lire plus sur React Native.