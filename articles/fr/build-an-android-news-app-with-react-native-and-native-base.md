---
title: Comment créer une application d'actualités Android avec React Native et Native
  Base
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-23T18:23:27.000Z'
originalURL: https://freecodecamp.org/news/build-an-android-news-app-with-react-native-and-native-base
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/How-to-Build-a-Weather-Application-using-React--66-.png
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
seo_title: Comment créer une application d'actualités Android avec React Native et
  Native Base
seo_desc: "By Nishant Kumar\nWe live in a world where things are constantly changing.\
  \ So if you want to stay up to date on what's happening, you'll want a good News\
  \ app. \nTo help you learn some cool tech and stay current, in this blog post we'll\
  \ build a News App..."
---

Par Nishant Kumar

Nous vivons dans un monde où les choses changent constamment. Donc, si vous voulez rester à jour sur ce qui se passe, vous aurez besoin d'une bonne application d'actualités. 

Pour vous aider à apprendre quelques technologies cool et rester à jour, dans cet article de blog, nous allons créer une application d'actualités pour Android en utilisant React Native. Elle récupérera les titres des différents canaux d'actualités et les affichera par catégorie.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-210544.png)

Voici à quoi ressemblera notre application une fois terminée. Alors, plongeons-nous directement dedans.

## Comment installer Expo

Alors, qu'est-ce qu'Expo ? Expo est un framework qui vous aide à construire et à déployer une application React Native rapidement et facilement.

Commençons par l'installer.

```
npm install --global expo-cli
```

Exécutez cette commande dans votre terminal pour installer l'interface de ligne de commande Expo. Ici, nous utilisons `--global` pour nous assurer qu'elle est installée partout.

Après son installation, nous devons créer un projet Expo.

```
expo init News-Application
```

Utilisez la commande ci-dessus pour initialiser le projet. Elle vous posera quelques questions, comme le nom de votre application, si vous souhaitez ajouter TypeScript à votre projet, ou commencer avec un projet vide. Sélectionnez simplement vide, et appuyez sur Entrée.

Ensuite, elle téléchargera tous les packages et dépendances dans le dossier.   
  
Maintenant, après que cela soit fait, naviguez dans le dossier du projet. Pour démarrer l'application, tapez **expo start**. Cela ouvrira les outils de développement dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-174505.png)
_Outils de développement Expo_

Ici, vous verrez de nombreuses options à gauche, comme exécuter sur un appareil Android/émulateur, ou sur un simulateur iOS. Nous allons exécuter l'application sur le navigateur Web, alors cliquez sur l'option Exécuter dans le navigateur Web.

```
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Ouvrez App.js pour commencer à travailler sur votre application !</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

```

Ceci est notre fichier App.js, qui contient le code standard.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-175022.png)
_Notre sortie_

Maintenant, notre application est en cours d'exécution.

## Comment créer différents écrans en utilisant React Navigation

Maintenant, créons divers écrans différents pour notre application. Pour cela, nous allons utiliser React Navigation. Alors, installons-le.

Rendez-vous sur [https://reactnavigation.org/](https://reactnavigation.org/) et cliquez sur Lire la documentation. Cela ouvrira la page de documentation.

Installons React Navigation en utilisant la commande ci-dessous :

```
npm install @react-navigation/native

expo install react-native-screens react-native-safe-area-context
```

Maintenant, notre React Navigation est installé. 

Nous allons utiliser `bottomTabNavigator`. Donc, dans le menu de gauche, choisissez Référence API, puis Navigateurs, puis les onglets du bas.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-175641.png)
_Choisissez les onglets du bas_

Installons les onglets du bas en utilisant la commande ci-dessous :

```
npm install @react-navigation/bottom-tabs
```

Maintenant, dans notre fichier App.js, nous devons importer les onglets du bas pour pouvoir les utiliser.

Alors, importez-les comme ceci :

```
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

```

Maintenant, importons les écrans d'onglets.

```
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
const Tab = createBottomTabNavigator();

function MyTabs() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Settings" component={SettingsScreen} />
    </Tab.Navigator>
  );
}
```

Voici comment nous créons les onglets du bas.

Dans notre cas, nous devons faire quelque chose comme ceci :

```
<Tab.Navigator>
  <Tab.Screen name="All" component={All} />
  <Tab.Screen name="Business" component={Business} />
  <Tab.Screen name="Health" component={HealthScreen} />
  <Tab.Screen name="Sports" component={SportsScreen} />
  <Tab.Screen name="Tech" component={TechScreen} />
</Tab.Navigator>
```

Nous devons créer ces écrans pour les onglets suivants : Toutes les actualités, Actualités économiques, Actualités sportives, Actualités santé et Actualités technologiques. Créez également un composant dans le projet pour chaque écran.

Nous devons envelopper ce `TabNavigtor` dans un `NavigationContainer` comme ceci :

```
<NavigationContainer>
  <Tab.Navigator>
    <Tab.Screen name="All" component={All} />
    <Tab.Screen name="Business" component={Business} />
    <Tab.Screen name="Health" component={HealthScreen} />
    <Tab.Screen name="Sports" component={SportsScreen} />
    <Tab.Screen name="Tech" component={TechScreen} />
  </Tab.Navigator>
</NavigationContainer>
```

Nous devons également importer tous ces composants, alors importez-les en haut.

```
import All from './screens/All';
import Business from './screens/Business';
import HealthScreen from './screens/Health';
import SportsScreen from './screens/Sports';
import TechScreen from './screens/Tech';
```

Maintenant, si nous mettons tout le code ensemble que nous avons écrit, nous obtiendrons le code ci-dessous :

```
import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import All from './screens/All';
import Business from './screens/Business';
import HealthScreen from './screens/Health';
import SportsScreen from './screens/Sports';
import TechScreen from './screens/Tech';
const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="All" component={All} />
        <Tab.Screen name="Business" component={Business} />
        <Tab.Screen name="Health" component={HealthScreen} />
        <Tab.Screen name="Sports" component={SportsScreen} />
        <Tab.Screen name="Tech" component={TechScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
} 
```

Et voici notre sortie :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-181356.png)
_Nos cinq écrans à savoir Toutes, Business, Santé, Sports et Tech_

Nous avons cinq écrans ici pour Toutes, Business, Santé, Sports et Tech.

Maintenant, faisons quelques ajustements ici. Nous devons changer les icônes pour les onglets du bas.

Pour cela, nous aurons besoin d'une bibliothèque d'icônes pour nos icônes. Pour cela, nous allons utiliser _react-native-elements._ 

Pour l'installer, tapez la commande ci-dessous :

```
npm install react-native-elements
```

Ce package d'icônes offre de nombreuses options d'icônes parmi lesquelles choisir.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-193917.png)
_Icônes disponibles dans React Native Elements_

Maintenant, ajoutons nos icônes dans le navigateur d'onglets du bas.

```
<Tab.Screen name="All" component={All}
          options={{
            tabBarIcon: (props) => (
              <Icon type='feather' name='home' color={props.color} />
            ),
          }} />
```

Ici, nous avons ajouté l'icône nommée "home" pour la page d'accueil et la classe d'icône feather pour le type.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-194136.png)
_Navigateur d'onglets du bas avec l'icône Accueil_

Cela donnera la sortie ci-dessus. Et de la même manière, répétons le même processus pour tous les autres.

```
<Tab.Navigator>
        <Tab.Screen name="All" component={All}
          options={{
            tabBarIcon: (props) => (
              <Icon type='feather' name='home' color={props.color} />
            ),
          }} />

        <Tab.Screen name="Business" component={Business}
          options={{
            tabBarIcon: (props) => (
              <Icon type='feather' name='dollar-sign' color={props.color} />
            ),
          }} />

        <Tab.Screen name="Health" component={HealthScreen}
          options={{
            tabBarIcon: (props) => (
              <Icon type='feather' name='heart' color={props.color} />
            ),
          }} />

        <Tab.Screen name="Sports" component={SportsScreen}
          options={{
            tabBarIcon: (props) => (
              <Icon type='ionicon' name="tennisball-outline" color={props.color} />
            ),
          }} />

        <Tab.Screen name="Tech" component={TechScreen}
          options={{
            tabBarIcon: (props) => (
              <Icon type='ionicon' name="hardware-chip-outline" color={props.color} />
            ),
          }} />
      </Tab.Navigator>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-194525.png)

Maintenant, chacun de nos différents onglets ou écrans est terminé, et chacun a sa propre icône distincte. 

## Comment appeler l'API News

Maintenant, appelons l'API News depuis [https://newsapi.org/](https://newsapi.org/)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-194845.png)

Allez sur ce site web et inscrivez-vous. Cela vous donnera une clé API.

Nous avons besoin d'un fichier de configuration pour stocker toutes les constantes News, alors créons-le.

```
export const API_KEY = ``;
export const endpoint = `https://newsapi.org/v2/top-headlines`;
export const country = 'in'
```

Nous avons besoin de la clé API, du point de terminaison et du code du pays.

Maintenant, nous devons créer un service pour notre **requête GET API.**

Créez un fichier appelé _services.js._

Ici, importez API_KEY, endpoint et le pays en haut.

```
import { API_KEY, endpoint, country } from '../config/config';
```

Ensuite, nous écrirons le corps de nos services.

```
export async function services(category = 'general') {
    let articles = await fetch(`${endpoint}?country=${country}&category=${category}`, {
        headers: {
            'X-API-KEY': API_KEY
        }
    });

    let result = await articles.json();
    articles = null;

    return result.articles;
}
```

Donc, nous récupérons les données d'actualités en utilisant notre point de terminaison, et en ajoutant le pays et la catégorie. Dans la fonction, nous passons la catégorie comme générale car c'est la catégorie par défaut. Nous passons également la clé API dans les en-têtes.

Ensuite, nous convertissons la réponse, ou les données entrantes, au format JSON et les stockons dans une variable de résultat. 

Et enfin, nous les retournons en utilisant le mot-clé `return`.

Voici le fichier complet pour votre référence :

```
import { API_KEY, endpoint, country } from '../config/config';

export async function services(category = 'general') {
    let articles = await fetch(`${endpoint}?country=${country}&category=${category}`, {
        headers: {
            'X-API-KEY': API_KEY
        }
    });

    let result = await articles.json();
    articles = null;

    return result.articles;
}
```

Maintenant, nous devons importer ce service dans notre fichier All.js.

```
import { services } from '../services/services';
```

Nous aurons besoin d'utiliser les hooks `useState` et `useEffect`. Le hook useEffect appellera ce service dans le fichier All.js et useState créera un état qui stockera la réponse provenant de l'API.

```
import React, { useEffect, useState } from 'react'
import { View } from 'react-native';
import { services } from '../services/services';
export default function All() {
    const [newsData, setNewsData] = useState([])
    useEffect(() => {
        services('general')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
    return (
        <View>

        </View>
    )
}

```

Dans ce fichier, nous appelons les services dans notre hook useEffect. Ensuite, nous stockons la réponse dans l'état newsData, qui est un tableau. Nous passons également un paramètre pour la catégorie qui est général. 

Cet écran récupérera toutes les actualités, donc nous utilisons la catégorie générale. Cela changera pour chaque autre écran. Ce sera _santé_ pour l'écran Santé, _sports_ pour les Sports, et ainsi de suite.

Maintenant, nous devons afficher ces données dans notre interface. Et pour cela, nous avons besoin d'un autre package appelé Native Base. Alors, installons-le.

Tapez les commandes ci-dessous pour installer Native Base :

```
yarn add native-base styled-components styled-system
expo install react-native-svg react-native-safe-area-context
```

Dans All.js, importons quelques éléments de Native Base :

```
import React, { useEffect, useState } from 'react'
import { View, Text } from 'react-native';
import { NativeBaseProvider, FlatList, ScrollView, Divider, Image, Spinner } from 'native-base';
import { services } from '../services/services';
```

Ensuite, dans le return, nous ajouterons `NativeBaseProvider`.

```
return (
        <NativeBaseProvider>
            
        </NativeBaseProvider>
    )
```

Ensuite, ajoutons la vue de défilement. Cela permettra aux utilisateurs de faire défiler si les données d'actualités dépassent la hauteur de notre écran.

```
<NativeBaseProvider>
            <ScrollView height={850}>

            </ScrollView>
        </NativeBaseProvider>
```

Maintenant, ajoutons la `FlatList` pour afficher nos données d'actualités.

```
<NativeBaseProvider>
            <ScrollView height={850}>
                <FlatList
                    data={newsData}
                    renderItem={({ item }) => (
                       <View>

                       </View> 
                    )}
                    keyExtractor={(item) => item.id}
                />
            </ScrollView>
        </NativeBaseProvider>
```

La FlatList prend une propriété data, qui est notre état `newsData` que nous avons créé précédemment, et elle retourne un `item` de `renderItems`_._

Cela est similaire à `map` en JavaScript, qui parcourt un tableau et retourne un élément. Il a également un `keyExtractor` que nous utilisons pour rendre chaque élément unique.

Maintenant, affichons nos données dans la vue.

Créez une autre vue à l'intérieur de la vue parente comme ceci :

```
<NativeBaseProvider>
            <ScrollView height={850}>
                <FlatList
                    data={newsData}
                    renderItem={({ item }) => (
                       <View>
                           <View>
                               
                           </View>
                       </View> 
                    )}
                    keyExtractor={(item) => item.id}
                />
            </ScrollView>
        </NativeBaseProvider>
```

Maintenant, ajoutons du texte à l'intérieur de la vue enfant.

```
<NativeBaseProvider>
            <ScrollView height={850}>
                <FlatList
                    data={newsData}
                    renderItem={({ item }) => (
                        <View>
                            <View>
                                <Text>
                                    {item.title}
                                </Text>
                                <Text>
                                    {item.publishedAt}
                                </Text>
                                <Text>
                                    {item.description}
                                </Text>
                            </View>
                        </View>
                    )}
                    keyExtractor={(item) => item.id}
                />
            </ScrollView>
        </NativeBaseProvider>
```

Cela contient le titre de notre actualité, la description et la date de publication.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-203253.png)

## Comment styliser notre application d'actualités React Native

Voici à quoi ressemble notre application maintenant, avec le titre des actualités, la description et la date. Pour la rendre un peu plus belle, nous devons lui donner un peu de style.

Importez `StyleSheet` depuis React Native en haut afin d'utiliser son style.

```
import { View, Text, StyleSheet } from 'react-native';
```

```
<View>
                            <View style={styles.newsContainer}>
                                <Text style={styles.title}>
                                    {item.title}
                                </Text>
                                <Text style={styles.date}>
                                    {item.publishedAt}
                                </Text>
                                <Text style={styles.newsDescription}>
                                    {item.description}
                                </Text>
                            </View>
                        </View>
```

Ensuite, ajoutez des styles comme ceci. Et en bas, nous devons créer ces styles.

```
const styles = StyleSheet.create({
    newsContainer: {
        padding: 10
    },
    title: {
        fontSize: 18,
        marginTop: 10,
        fontWeight: "600"
    },
    newsDescription: {
        fontSize: 16,
        marginTop: 10
    },
    date: {
        fontSize: 14
    },
});
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-203824.png)

Voici à quoi ressemble l'application maintenant après avoir reçu un peu de style. Vous pouvez également faire défiler la page vers le bas.

Maintenant, nous devons changer le format de la date pour un format lisible, car je ne comprends pas **'2021-08-21T11:00:40Z'.**

Nous utiliserons le package utile moment.js pour cela, alors installons-le en utilisant la commande ci-dessous :

```
npm install moment --save
```

Ensuite, importez-le dans notre écran All.js :

```
<Text style={styles.date}>
  {moment(item.publishedAt).format('LLL')}
</Text>
```

Formatez la date comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-204311.png)
_Formats de date et d'heure de Moment.js_

La documentation de moment nous donne tant de formats parmi lesquels choisir. J'ai choisi le format _'LLL'_.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-204439.png)

Et maintenant, nos dates sont beaucoup plus lisibles pour les humains.

Nous avons également besoin d'un diviseur pour séparer les articles de presse les uns des autres afin qu'ils ne se mélangent pas tous.

```
<View>
                            <View style={styles.newsContainer}>
                                <Text style={styles.title}>
                                    {item.title}
                                </Text>
                                <Text style={styles.date}>
                                    {moment(item.publishedAt).format('LLL')}
                                </Text>
                                <Text style={styles.newsDescription}>
                                    {item.description}
                                </Text>
                            </View>
                            <Divider my={2} bg="#e0e0e0" />
                        </View>
```

Donc, après avoir ajouté un diviseur après la vue enfant, notre application ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-204707.png)

Maintenant, nos titres d'actualités sont divisés, ce qui est super.

Cette API News a également une image. Alors, ajoutons-la.

```
<View>
                            <View style={styles.newsContainer}>
                                <Image
                                    width={550}
                                    height={250}
                                    resizeMode={"cover"}
                                    source={{
                                        uri: item.urlToImage,
                                    }}
                                    alt="Texte alternatif"
                                />
                                <Text style={styles.title}>
                                    {item.title}
                                </Text>
                                <Text style={styles.date}>
                                    {moment(item.publishedAt).format('LLL')}
                                </Text>
                                <Text style={styles.newsDescription}>
                                    {item.description}
                                </Text>
                            </View>
                            <Divider my={2} bg="#e0e0e0" />
                        </View>
```

Donc, nous avons ajouté l'image et nous avons utilisé la clé appelée `urlToImage` pour le faire_._

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-204945.png)

Maintenant, nous avons les images des actualités qui s'affichent.

## Comment ajouter un spinner pour montrer le chargement des actualités

Ajoutons un spinner qui s'affichera lorsque les actualités seront en cours de chargement.

Tout d'abord, nous allons créer une vérification. Si la longueur de l'état `newsData` est supérieure à un, nous afficherons notre `FlatList`, qui contient nos données d'actualités. Sinon, nous afficherons le spinner de chargement.

En d'autres termes, si la longueur de l'état `newsData` est inférieure à un, cela signifie qu'il est vide et que l'API est toujours en cours d'appel. Une fois l'appel API terminé, il stockera les données dans l'état `newsData`, et la longueur de l'état changera pour plus d'un.

```
{newsData.length > 1 ? (
                    <FlatList
                        data={newsData}
                        renderItem={({ item }) => (
                            <View>
                                <View style={styles.newsContainer}>
                                    <Image
                                        width={550}
                                        height={250}
                                        resizeMode={"cover"}
                                        source={{
                                            uri: item.urlToImage,
                                        }}
                                        alt="Texte alternatif"
                                    />
                                    <Text style={styles.title}>
                                        {item.title}
                                    </Text>
                                    <Text style={styles.date}>
                                        {moment(item.publishedAt).format('LLL')}
                                    </Text>
                                    <Text style={styles.newsDescription}>
                                        {item.description}
                                    </Text>
                                </View>
                                <Divider my={2} bg="#e0e0e0" />
                            </View>
                        )}
                        keyExtractor={(item) => item.id}
                    />
                ) : (
                    <View style={styles.spinner}>
                        <Spinner color="danger.400" />
                    </View>
                )}
```

Et dans nos styles, ajoutez le code de style ci-dessous pour le spinner.

```
spinner: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: 400
}
```

Voici le code ci-dessous pour votre référence :

```
import React, { useEffect, useState } from 'react'
import { View, Text, StyleSheet } from 'react-native';
import { NativeBaseProvider, FlatList, ScrollView, Divider, Image, Spinner } from 'native-base';
import { services } from '../services/services';
import moment from 'moment'
export default function All() {
    const [newsData, setNewsData] = useState([])
    useEffect(() => {
        services('general')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
    return (
        <NativeBaseProvider>
            <ScrollView height={850}>
                {newsData.length > 1 ? (
                    <FlatList
                        data={newsData}
                        renderItem={({ item }) => (
                            <View>
                                <View style={styles.newsContainer}>
                                    <Image
                                        width={550}
                                        height={250}
                                        resizeMode={"cover"}
                                        source={{
                                            uri: item.urlToImage,
                                        }}
                                        alt="Texte alternatif"
                                    />
                                    <Text style={styles.title}>
                                        {item.title}
                                    </Text>
                                    <Text style={styles.date}>
                                        {moment(item.publishedAt).format('LLL')}
                                    </Text>
                                    <Text style={styles.newsDescription}>
                                        {item.description}
                                    </Text>
                                </View>
                                <Divider my={2} bg="#e0e0e0" />
                            </View>
                        )}
                        keyExtractor={(item) => item.id}
                    />
                ) : (
                    <View style={styles.spinner}>
                        <Spinner color="danger.400" />
                    </View>
                )}
            </ScrollView>
        </NativeBaseProvider>
    )
}

const styles = StyleSheet.create({
    newsContainer: {
        padding: 10
    },
    title: {
        fontSize: 18,
        marginTop: 10,
        fontWeight: "600"
    },
    newsDescription: {
        fontSize: 16,
        marginTop: 10
    },
    date: {
        fontSize: 14
    },
    spinner: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: 400
    }
});
```

Notre écran All.js est maintenant complet.

Et maintenant, nous pouvons utiliser le même code dans tous les autres écrans également. Nous devons simplement changer le paramètre que nous passons dans les services dans le hook `useEffect`.

Donc, pour l'écran Business, nous utiliserons business. Pour la santé, nous utiliserons health, et ainsi de suite.

```
import React, { useEffect, useState } from 'react'
import { View, Text, StyleSheet } from 'react-native';
import { NativeBaseProvider, FlatList, ScrollView, Divider, Image, Spinner } from 'native-base';
import { services } from '../services/services';
import moment from 'moment'
export default function Business() {
    const [newsData, setNewsData] = useState([])
    useEffect(() => {
        services('business')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
    return (
        <NativeBaseProvider>
            <ScrollView height={850}>
                {newsData.length > 1 ? (
                    <FlatList
                        data={newsData}
                        renderItem={({ item }) => (
                            <View>
                                <View style={styles.newsContainer}>
                                    <Image
                                        width={550}
                                        height={250}
                                        resizeMode={"cover"}
                                        source={{
                                            uri: item.urlToImage,
                                        }}
                                        alt="Texte alternatif"
                                    />
                                    <Text style={styles.title}>
                                        {item.title}
                                    </Text>
                                    <Text style={styles.date}>
                                        {moment(item.publishedAt).format('LLL')}
                                    </Text>
                                    <Text style={styles.newsDescription}>
                                        {item.description}
                                    </Text>
                                </View>
                                <Divider my={2} bg="#e0e0e0" />
                            </View>
                        )}
                        keyExtractor={(item) => item.id}
                    />
                ) : (
                    <View style={styles.spinner}>
                        <Spinner color="danger.400" />
                    </View>
                )}
            </ScrollView>
        </NativeBaseProvider>
    )
}

const styles = StyleSheet.create({
    newsContainer: {
        padding: 10
    },
    title: {
        fontSize: 18,
        marginTop: 10,
        fontWeight: "600"
    },
    newsDescription: {
        fontSize: 16,
        marginTop: 10
    },
    date: {
        fontSize: 14
    },
    spinner: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: 400
    }
});
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-210200.png)

Faites défiler l'écran Business, et vous verrez les actualités liées aux affaires.

Et vous pouvez faire de même pour tous les autres écrans :

```
useEffect(() => {
        services('business')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
}, [])
```

```
useEffect(() => {
        services('health')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
```

```
useEffect(() => {
        services('sports')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
```

```
useEffect(() => {
        services('technology')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
```

## Conclusion

Félicitations ! Maintenant, notre application d'actualités est complète.

Alors, allez-y, construisez et expérimentez un peu avec elle. Il y a des tonnes de choses que vous pouvez faire.

Vous pouvez consulter ma playlist sur [Créer une application d'actualités en utilisant React Native et Native Base](https://youtube.com/playlist?list=PLWgH1O_994O8KP1srByN1OmoiRpLF6lNO), qui est sur ma chaîne YouTube.

N'hésitez pas à télécharger le code ici : [https://github.com/nishant-666/React-Native-News](https://github.com/nishant-666/React-Native-News)

> Bon apprentissage.