---
title: Comment utiliser l'API de transfert de style dans React Native avec Fritz
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T20:53:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-style-transfer-api-in-react-native-with-fritz-e90bc609fb17
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca3b5740569d1a4ca5d65.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: technology
  slug: technology
seo_title: Comment utiliser l'API de transfert de style dans React Native avec Fritz
seo_desc: 'By Sameeha Rahman

  Fritz is a platform that’s intended to make it easy for developers to power their
  mobile apps with machine learning features. Currently, it has an SDK for both Android
  and iOS. The SDK contains ready-to-use APIs for the following fe...'
---

Par Sameeha Rahman

[Fritz](https://www.fritz.ai/) est une plateforme conçue pour faciliter l'intégration de fonctionnalités de machine learning dans les applications mobiles. Actuellement, elle propose un SDK pour Android et iOS. Le SDK contient des API prêtes à l'emploi pour les fonctionnalités suivantes :

1. [Détection d'objets](https://www.fritz.ai/features/object-detection.html)
2. [Étiquetage d'images](https://www.fritz.ai/features/image-labeling.html)
3. [Transfert de style](https://www.fritz.ai/features/style-transfer.html)
4. [Segmentation d'images](https://www.fritz.ai/features/image-segmentation.html)
5. [Estimation de pose](https://www.fritz.ai/features/pose-estimation.html)

Aujourd'hui, nous allons explorer comment utiliser l'API de transfert de style dans React Native.

J'ai seulement pu développer et tester sur Android (pas de Mac ici !) et j'ai obtenu une application fonctionnelle.

L'API de transfert de style applique des styles d'œuvres d'art réelles à des images ou vidéos. Il existe 11 styles artistiques pré-entraînés, incluant La Nuit étoilée de Van Gogh et Le Cri de Munch, parmi d'autres.

L'application que nous allons développer permettra à l'utilisateur de prendre une photo et de la convertir en une image stylisée. Elle permettra également à l'utilisateur de choisir le style artistique qu'il souhaite appliquer à l'image.

L'application contiendra une page d'accueil, où l'utilisateur pourra choisir le style artistique. Elle inclura également une vue Caméra séparée, où l'utilisateur capturera l'image.

> Note : Le tutoriel suivant est uniquement pour la plateforme Android.

#### Prérequis

1. React Native CLI : exécutez `npm i -g react-native-cli` pour installer globalement le CLI

Puisqu'il n'existe pas de module React Native par défaut pour Fritz, nous devrons écrire le nôtre. Écrire un module natif signifie écrire du code natif réel pour une ou les deux plateformes.

### Étape 1 — Création de l'application RN et installation des modules

Pour créer l'application, exécutez la commande suivante dans le terminal :

```
react-native init <nomdelapp>
```

Déplacez-vous à la racine du dossier pour commencer la configuration.

Pour la navigation, nous utiliserons [React Navigation](https://reactnavigation.org/) et [React Native Camera](https://github.com/react-native-community/react-native-camera) pour la vue Caméra.

Pour installer les deux dépendances, exécutez la commande suivante dans le terminal :

```
npm i --save react-navigation react-native-camera
```

Suivez les instructions [ici](https://reactnavigation.org/docs/en/getting-started.html#installation) pour configurer React Navigation pour l'application. Nous devrons également installer `react-native-gesture-handler`, car c'est une dépendance de React Navigation.

Suivez les instructions [ici](https://github.com/react-native-community/react-native-camera#android) pour configurer React Native Camera pour l'application. Nous pouvons nous arrêter à l'étape 6, car pour cet exemple, nous n'utiliserons pas la reconnaissance de texte, de visage ou de code-barres.

### Étape 2 — Inclusion du SDK Fritz dans l'application

Tout d'abord, nous devons créer un compte Fritz et un nouveau projet.

À partir de l'aperçu du projet, cliquez sur Ajouter à Android pour inclure le SDK pour la plateforme Android. Nous devrons inclure un nom d'application et l'ID de l'application. L'ID de l'application peut être trouvé dans `android/app/build.gradle`, à l'intérieur de la balise `defaultConfig`.

Après avoir enregistré l'application, nous devons ajouter les lignes suivantes dans `android/build.gradle` :

```
allprojects {    
	.....    
    repositories {        
    	.....        
        maven { url "https://raw.github.com/fritzlabs/fritz-repository/master" } //ajoutez cette ligne    
    }
}
```

Ensuite, incluez la dépendance dans `android/app/build.gradle` :

```
dependencies {    
	implementation 'ai.fritz:core:3.0.2'
}
```

Nous devons mettre à jour le fichier `AndroidManifest.xml` pour donner à l'application la permission d'utiliser Internet et enregistrer le service Fritz :

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
	.....    
	<uses-permission android:name="android.permission.INTERNET" />    
    <application>        
    	.....        
        <service            
        	android:name="ai.fritz.core.FritzCustomModelService"            
            android:exported="true"            
            android:permission="android.permission.BIND_JOB_SERVICE" />    
    </application>
</manifest>
```

Nous devons ensuite inclure la méthode suivante dans `MainActivity.java` :

```java
import ai.fritz.core.Fritz;
import android.os.Bundle; //importez également ces deux éléments

public class MainActivity extends ReactActivity {    
	.....    
    @Override    
    protected void onCreate(Bundle savedInstanceState) {        
    	// Initialiser Fritz        
        Fritz.configure(this, "<api-key>");    
    }
}
```

### Étape 3 — Création du module natif

Puisque le SDK ne prend en charge que iOS et Android, nous devons créer le module natif. Pour mieux comprendre cela, consultez la documentation ici :

[**Modules natifs · React Native**](https://facebook.github.io/react-native/docs/native-modules-android)  
[_Parfois, une application a besoin d'accéder à une API de plateforme pour laquelle React Native n'a pas encore de module correspondant. Peut-être..._facebook.github.io](https://facebook.github.io/react-native/docs/native-modules-android)

Pour créer un module natif Android, nous devons créer deux nouveaux fichiers. Ils seront dans le package racine du dossier source Android.

1. `FritzStyleModule` : Ce fichier contient le code qui retournera l'image stylisée
2. `FritzStylePackage` : Ce fichier enregistre le module afin qu'il puisse être utilisé par le côté JavaScript de l'application.

#### FritzStyleModule

```java
package com.fritzexample;

import com.facebook.react.bridge.Callback;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;

import java.util.*;
import java.io.*;
import android.graphics.*;

import ai.fritz.fritzvisionstylepaintings.PaintingStyles;
import ai.fritz.vision.styletransfer.*;
import ai.fritz.core.FritzOnDeviceModel;
import ai.fritz.vision.*;

public class FritzStyleModule extends ReactContextBaseJavaModule {
    private final ReactApplicationContext reactContext;

    public FritzStyleModule(ReactApplicationContext reactContext) {
        super(reactContext);
        this.reactContext = reactContext;
    }

    @Override
    public String getName() {
        return "FritzStyle";
    }

    @ReactMethod
    public void getNewImage(String image, String filter, Callback errorCallback, Callback successCallback) {

        try {

            // Obtenez le style de peinture que l'utilisateur souhaite utiliser pour convertir l'image.

            FritzOnDeviceModel styleOnDeviceModel;

            switch (filter) {
            case "STARRY_NIGHT":
                styleOnDeviceModel = PaintingStyles.STARRY_NIGHT;
                break;
            case "BICENTENNIAL_PRINT":
                styleOnDeviceModel = PaintingStyles.BICENTENNIAL_PRINT;
                break;
            case "FEMMES":
                styleOnDeviceModel = PaintingStyles.FEMMES;
                break;
            case "HEAD_OF_CLOWN":
                styleOnDeviceModel = PaintingStyles.HEAD_OF_CLOWN;
                break;
            case "HORSES_ON_SEASHORE":
                styleOnDeviceModel = PaintingStyles.HORSES_ON_SEASHORE;
                break;
            case "KALEIDOSCOPE":
                styleOnDeviceModel = PaintingStyles.KALEIDOSCOPE;
                break;
            case "PINK_BLUE_RHOMBUS":
                styleOnDeviceModel = PaintingStyles.PINK_BLUE_RHOMBUS;
                break;
            case "POPPY_FIELD":
                styleOnDeviceModel = PaintingStyles.POPPY_FIELD;
                break;
            case "RITMO_PLASTICO":
                styleOnDeviceModel = PaintingStyles.RITMO_PLASTICO;
                break;
            case "THE_SCREAM":
                styleOnDeviceModel = PaintingStyles.THE_SCREAM;
                break;
            case "THE_TRAIL":
                styleOnDeviceModel = PaintingStyles.THE_TRAIL;
                break;
            default:
                styleOnDeviceModel = PaintingStyles.THE_TRAIL;
                break;
            }

            // Initialisez le prédicteur de style avec le style d'œuvre d'art sélectionné.
            FritzVisionStylePredictor stylePredictor = FritzVision.StyleTransfer.getPredictor(styleOnDeviceModel);

            // Obtenez l'encodeur et le décodeur Base 64.
            Base64.Decoder decoder = Base64.getDecoder();
            Base64.Encoder encoder = Base64.getEncoder();

            // Décodez l'image base 64 en un tableau d'octets.
            byte[] decodedString = decoder.decode(image);

            // Convertissez le tableau d'octets en une image Bitmap du début (0) à la fin
            // (decodedString.length) du tableau.
            Bitmap bitmap = BitmapFactory.decodeByteArray(decodedString, 0, decodedString.length);

            // Une classe d'entrée standard pour le prédicteur de style.
            FritzVisionImage visionImage = FritzVisionImage.fromBitmap(bitmap);

            // Convertissez l'image normale en une image stylisée selon le style
            // d'œuvre d'art sélectionné.
            FritzVisionStyleResult styleResult = stylePredictor.predict(visionImage);

            // Obtenez une image Bitmap à partir du résultat stylisé.
            Bitmap styledBitmap = styleResult.getResultBitmap();

            ByteArrayOutputStream baos = new ByteArrayOutputStream();

            // Compressez l'image Bitmap en une image .png et ajoutez-la au flux de sortie
            // baos.
            styledBitmap.compress(Bitmap.CompressFormat.PNG, 0, baos);

            // Convertissez le flux de sortie en un tableau d'octets.
            byte[] b = baos.toByteArray();

            // Encodez le tableau d'octets en une image base 64.
            String newImage = encoder.encodeToString(b);

            // Envoyez la chaîne base 64 de l'image stylisée via le callback de succès au
            // côté JavaScript.
            successCallback.invoke(newImage);

        } catch (Exception e) {

            errorCallback.invoke(e.getMessage());

        }

    }

}
```

La méthode React utilisée a un callback de succès et d'erreur. Le style d'œuvre d'art choisi et une base64 de l'image originale sont envoyés à la méthode. Le callback d'erreur est invoqué lorsqu'une `Exception` est levée et retourne l'erreur. Le callback de succès retourne une chaîne encodée en base64 de l'image convertie. À haut niveau, le code ci-dessus fait ce qui suit :

1. Initialise le prédicteur de style avec le choix de l'utilisateur en matière d'œuvre d'art.
2. Convertit l'image base64 originale en un `Bitmap`.
3. Crée un `FritzVisionImage`, qui est l'entrée du prédicteur de style.
4. Convertit le `FritzVisionImage` en un `FritzVisionStyleResult` stylisé, qui est l'image convertie.
5. Obtient un `Bitmap` à partir du `FritzVisionStyleResult`.
6. Convertit le `Bitmap` en une base64 pour l'envoyer au côté JavaScript de l'application.

#### FritzStylePackage

```java
package com.fritzexample;

import com.facebook.react.ReactPackage;
import com.facebook.react.bridge.NativeModule;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.uimanager.ViewManager;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class FritzStylePackage implements ReactPackage {

    @Override
    public List<NativeModule> createNativeModules(ReactApplicationContext reactContext) {
        List<NativeModule> modules = new ArrayList<>();

        // Ajoutez le module DataUsage à la liste des modules natifs, qui est
        // référencée par le code React-Native
        modules.add(new FritzStyleModule(reactContext));
        return modules;
    }

    @Override
    public List<ViewManager> createViewManagers(ReactApplicationContext reactContext) {
        return Collections.emptyList();
    }
}
```

Cette classe est utilisée pour enregistrer le package afin qu'il puisse être appelé du côté JavaScript de l'application.

Cette classe est également initialisée dans `getPackages()` de `MainApplication.java` :

```java
@Override
protected List<ReactPackage> getPackages() {  
	return Arrays.<ReactPackage>asList(    
    	new MainReactPackage(),    
        ......,     
        new FritzStylePackage() //Ajoutez cette ligne et importez-la en haut  
        );
}
```

Passons maintenant au côté JavaScript de l'application.

### Étape 4 — Création de l'interface utilisateur

Pour ce faire, nous allons créer/mettre à jour les pages suivantes :

1. Home.js — Afficher le sélecteur de styles artistiques et le résultat final.
2. CameraContainer.js — Afficher la vue caméra pour capturer une image.
3. FritzModule.js — Exporter le module natif créé ci-dessus vers le côté JavaScript.
4. App.js — Racine de l'application qui inclut la pile de navigation.

#### Home.js

```js
import React, { Component } from 'react';
import { StyleSheet, Text, View, Button, Image, Picker } from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';

export default class Home extends Component {

    // Masquer l'en-tête
    static navigationOptions = {
        header: null,
    }

    constructor(props) {
        super(props);

        // initialiser le sélecteur avec la première valeur
        this.state = {
            filter: "BICENTENNIAL_PRINT"
        }
    }

    render() {

        // Obtenir les paramètres suivants à partir des props de navigation, s'ils ont une valeur.
        const { navigation } = this.props;
        const oldImage = navigation.getParam('oldImage');
        const newImage = navigation.getParam('newImage');

        return (
            <View style={styles.container}>
                <ScrollView>
                    <View style={styles.innerContainer}>
                        <Text style={styles.welcome}>Exemple React Native Fritz !</Text>
                        <Text style={{ fontSize: 18 }}>Transfert de style</Text>
                        <Picker style={{ width: "100%" }} selectedValue={this.state.filter} mode="dropdown" onValueChange={(value) => this.setState({ filter: value })}>
                            <Picker.Item value="BICENTENNIAL_PRINT" label="Impression bicentenaire" />
                            <Picker.Item value="FEMMES" label="Femmes" />
                            <Picker.Item value="HEAD_OF_CLOWN" label="Tête de clown" />
                            <Picker.Item value="HORSES_ON_SEASHORE" label="Chevaux sur le rivage" />
                            <Picker.Item value="KALEIDOSCOPE" label="Caléidoscope" />
                            <Picker.Item value="PINK_BLUE_RHOMBUS" label="Rhombus rose bleu" />
                            <Picker.Item value="POPPY_FIELD" label="Champ de coquelicots" />
                            <Picker.Item value="RITMO_PLASTICO" label="Ritmo Plastico" />
                            <Picker.Item value="STARRY_NIGHT" label="Nuit étoilée" />
                            <Picker.Item value="THE_SCREAM" label="Le Cri" />
                            <Picker.Item value="THE_TRAIL" label="La Piste" />
                        </Picker>
                        <Button title="Prendre une photo" onPress={() => this.props.navigation.navigate('Camera', { filter: this.state.filter })} />
                        {/* Afficher les images, seulement si les valeurs ne sont pas indéfinies ou des chaînes vides */}
                        {oldImage && <Image style={styles.imageStyle} source={{ uri: 'data:image/png;base64,' + oldImage }} />}
                        {newImage && <Image style={styles.imageStyle} source={{ uri: 'data:image/png;base64,' + newImage }} />}
                    </View>
                </ScrollView>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: '#F5FCFF',
    },
    innerContainer: {
        flex: 1,
        flexDirection: 'column',
        justifyContent: "center",
        alignItems: "center",
        padding: 20
    },
    welcome: {
        fontSize: 20,
        textAlign: 'center',
        margin: 10,
    },
    imageStyle: {
        width: 250,
        height: 250,
        marginVertical: 5
    }
});

```

Cette page contient :

1. Texte pour afficher la description de l'application.
2. Sélecteur pour permettre à l'utilisateur de choisir le style artistique de l'image convertie.
3. Bouton pour rediriger l'utilisateur vers la page Caméra. Il transmettra le style artistique sélectionné au CameraContainer.
4. Si les props de navigation contiennent l'image originale et convertie, elles seront affichées.

La page ressemble actuellement à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*atFkoViOX1zmV5QhBCr9TA.png)
_Page d'accueil avant de prendre une photo_

#### CameraContainer.js

```js
import React, { Component } from 'react';
import { RNCamera } from 'react-native-camera';
import { View, StyleSheet, Button, Alert, ActivityIndicator } from 'react-native';
import FritzStyle from "./FritzModule";

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: "#000",
        position: 'absolute',
        height: '100%',
        width: '100%'
    },
    preview: {
        flex: 1,
        justifyContent: 'flex-end',
        alignItems: 'center',
    },
    cameraButton: {
        position: "absolute",
        bottom: 0,
        width: "100%",
        backgroundColor: "#000",
        alignItems: "center",
        justifyContent: "center",
        paddingVertical: 10
    },
});

class CameraContainer extends Component {

    // Masquer l'en-tête
    static navigationOptions = {
        header: null,
    }

    constructor(props) {
        super(props);

        // Initialiser les propriétés ci-dessous
        this.state = {
            oldImage: '',
            newImage: '',
            loading: false
        };
    }

    render() {

        return (
            <View style={styles.container}>
                <RNCamera
                    ref={ref => {
                        this.camera = ref;
                    }}
                    style={styles.preview}
                    type={RNCamera.Constants.Type.back}
                    captureAudio={false}
                >
                    {/* Afficher le bouton pour prendre une photo uniquement si la permission de la caméra est accordée */}
                    {({ camera, status }) => {
                        if ((status !== 'NOT_AUTHORIZED')) {
                            return (
                                <View style={styles.cameraButton}>
                                    {/* Afficher le spinner si chargement, sinon afficher le bouton */}
                                    {this.state.loading ? <ActivityIndicator size="large" color="#FFF" /> : <Button onPress={this.takePicture.bind(this)} title={"Prendre une photo"} />}
                                </View>
                            );
                        }
                    }}
                </RNCamera>
            </View>

        );
    }

    takePicture = async function () {

        // définir le chargement à vrai lors du clic sur le bouton, pour montrer à l'utilisateur qu'une action est en cours.
        this.setState({ loading: true });

        // Obtenez le filtre d'œuvre d'art choisi par l'utilisateur.
        const { navigation } = this.props;
        const filter = navigation.getParam('filter');

        // Si la référence à la caméra existe.
        if (this.camera) {

            // Prenez une image base64 avec les options suivantes.
            const options = { quality: 0.75, base64: true, maxWidth: 500, maxHeight: 500, fixOrientation: true };
            const data = await this.camera.takePictureAsync(options);

            // Définissez l'ancienne image comme celle capturée ci-dessus.
            this.setState({
                oldImage: data.base64
            },
                () => {

                    // Appelez la méthode du module natif et passez la base64 de l'image originale et le nom du style d'œuvre d'art sélectionné.
                    FritzStyle.getNewImage(data.base64, filter,
                        // Callback d'erreur
                        (error) => {
                            // Affichez une alerte pour informer l'utilisateur qu'une erreur a été rencontrée.
                            console.log(error);
                            Alert.alert("Alerte", "Une erreur s'est produite.");
                        },
                        // Callback de succès
                        (newData) => {

                            // Définissez la nouvelle image comme celle envoyée depuis le callback de succès.
                            this.setState({
                                newImage: newData
                            },
                                () => {

                                    // Naviguez vers la page d'accueil, tout en passant l'ancienne et la nouvelle image.
                                    this.props.navigation.navigate("Home", {
                                        oldImage: this.state.oldImage,
                                        newImage: this.state.newImage
                                    });
                                });
                        });
                }
            );
        }
    }
}

export default CameraContainer;
```

La page CameraContainer affiche une vue Caméra en plein écran. Elle inclut un bouton pour prendre la photo en bas de la page. En cliquant dessus, un spinner sera affiché pour indiquer à l'utilisateur qu'une action est en cours.

L'image est d'abord capturée en utilisant la méthode `takePictureAsync()` de react-native-camera. L'image originale est ensuite enregistrée dans l'état de la page. La méthode `setState` est asynchrone et possède donc un callback de succès qui s'exécute après que l'état soit défini.

La méthode `getNewImage` du `FritzModule` est exécutée dans ce callback de succès. L'image originale et le filtre (style artistique) choisi depuis la page d'accueil sont passés à la méthode. Dans le callback d'erreur, une alerte est affichée à l'utilisateur pour indiquer qu'une erreur s'est produite. Dans le callback de succès, la nouvelle image stylisée est enregistrée dans l'état. Dans ce deuxième callback de succès de la méthode `setState`, l'utilisateur est redirigé vers la page d'accueil avec les images originale et stylisée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*K-DDDA0go549lHTaXIq9Dw.png)
_CameraContainer sur l'émulateur_

#### FritzModule.js

```js
import { NativeModules } from 'react-native';
export default NativeModules.FritzStyle;
```

Cette page expose le module natif, `FritzStyle`. Cela permet au côté JavaScript de faire des appels à la méthode `getNewImage`.

#### App.js

```js
import React, { Component } from 'react';
import Home from './src/Home';
import CameraContainer from './src/CameraContainer';
import { createStackNavigator, createAppContainer } from 'react-navigation';

const AppNavigator = createStackNavigator({  
	Home: { screen: Home },  
    Camera: { screen: CameraContainer }
});

const AppContainer = createAppContainer(AppNavigator);

export default class App extends Component {
	render() {    
    	return (
        	<AppContainer />
        );  
    }
}
```

Tout d'abord, nous créons le navigateur de pile avec la page d'accueil et la vue Caméra. La clé 'Home' est utilisée lors de la navigation vers la page d'accueil, et la clé 'Camera' lors de la navigation vers le CameraContainer.

Le `AppContainer` devient le composant racine de l'application. C'est également le composant qui gère l'état de l'application.

Maintenant, pour voir l'application entière en fonctionnement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2vAb3iKgvRHAwawop8Crew.gif)

### Pour résumer, nous avons :

1. Créé une application React Native,
2. Inclus le SDK Fritz,
3. Créé un module natif qui utilise l'API de transfert de style, et
4. Conçu une interface utilisateur pour afficher l'image stylisée.

Trouvez le dépôt de code, [ici](https://github.com/samsam-026/FritzExample).

Pour des implémentations natives iOS ou Android de l'API de transfert de style de Fritz, consultez les tutoriels suivants :

[**Transfert de style en temps réel pour Android — Transformez vos photos et vidéos en chefs-d'œuvre**](https://heartbeat.fritz.ai/real-time-style-transfer-for-android-6a9d238dfdb5)  
[_Le transfert de style vous permet de vous inspirer d'artistes comme Picasso et Van Gogh et de transformer des images ordinaires en..._heartbeat.fritz.ai](https://heartbeat.fritz.ai/real-time-style-transfer-for-android-6a9d238dfdb5)[**Transfert de style en temps réel pour iOS — Transformez vos photos et vidéos en chefs-d'œuvre**](https://heartbeat.fritz.ai/real-time-style-transfer-for-ios-transform-your-photos-and-videos-into-masterpieces-f04111fcd2ff)  
[heartbeat.fritz.ai](https://heartbeat.fritz.ai/real-time-style-transfer-for-ios-transform-your-photos-and-videos-into-masterpieces-f04111fcd2ff)