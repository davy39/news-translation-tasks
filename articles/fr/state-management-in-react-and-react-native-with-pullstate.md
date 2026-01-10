---
title: Comment gérer l'état dans React et React Native avec la bibliothèque PullState
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2023-04-03T21:47:52.000Z'
originalURL: https://freecodecamp.org/news/state-management-in-react-and-react-native-with-pullstate
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Background1--1-.png
tags:
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: 'State Management '
  slug: state-management
seo_title: Comment gérer l'état dans React et React Native avec la bibliothèque PullState
seo_desc: "React and React Native are popular JavaScript libraries that allow developers\
  \ to create complex user interfaces and mobile applications with ease. \nOne of\
  \ the key benefits of both these libraries is that they each have the ability to\
  \ manage their own..."
---

React et React Native sont des bibliothèques JavaScript populaires qui permettent aux développeurs de créer des interfaces utilisateur complexes et des applications mobiles avec facilité. 

L'un des principaux avantages de ces bibliothèques est qu'elles ont chacune la capacité de gérer leur propre état au sein des composants. Mais la gestion de l'état, ainsi que les données partageables, peut être délicate - surtout lorsque les applications deviennent plus complexes.

Dans cet article, nous allons explorer la gestion de l'état global - et en particulier, comment utiliser la bibliothèque Pullstate. Vous apprendrez comment vous pouvez facilement l'implémenter dans vos projets React et React Native.

Prérequis :

* Connaissance de base des applications React / React Native
* Connaissance de base de CSS et du styling (non essentiel)

**Note** : dans cet article, j'utiliserai TypeScript et React Native. Mais l'implémentation et les concepts seront exactement les mêmes pour les utilisateurs de JavaScript et React (sans les variables fortement typées).

## Qu'est-ce que l'état ?

L'état fait référence à un objet qui stocke des données pouvant changer au fil du temps. C'est un moyen de gérer et de mettre à jour des données au sein d'un composant ou d'une application sans affecter d'autres parties de l'application.  
  
L'état dans React est comme un sac à dos que vous portez avec vous, contenant des choses dont vous pourriez avoir besoin pour votre journée. C'est un moyen de stocker et de gérer des données dans votre application qui peuvent changer au fil du temps, comme ce que vous avez ramassé ou déposé en cours de route.

### État local vs état global

L'état du composant est local à un composant spécifique. Cela signifie qu'il n'est accessible et modifiable que dans ce composant. Vous utilisez l'état du composant pour gérer des données spécifiques à un seul composant - par exemple, des messages de validation de formulaire ou la visibilité de certains éléments de l'interface utilisateur (UI).

L'état global, en revanche, fait référence à des données accessibles et modifiables à partir de plusieurs composants dans toute l'application. L'état global serait quelque chose géré par une bibliothèque de gestion d'état. Il est utile pour gérer des données partagées entre plusieurs composants, comme le statut d'authentification, les préférences de l'utilisateur ou le contenu du panier d'achat.   
  
L'état global et l'état du composant ont chacun leurs propres avantages et inconvénients, selon les besoins spécifiques de l'application. 

L'état global peut simplifier la gestion des données et améliorer les performances, mais peut également augmenter la complexité s'il n'est pas géré correctement. L'état du composant est plus simple à gérer et à comprendre, mais peut entraîner des données dupliquées et un comportement incohérent dans l'application.

## Que sont les bibliothèques de gestion d'état ?

![Image](https://www.freecodecamp.org/news/content/images/2023/03/SCR-20230325-oif-1.png)
_logos des bibliothèques d'état populaires_

Les bibliothèques de gestion d'état dans React sont des outils qui aident les développeurs à gérer et à organiser l'état de leurs applications plus facilement. Ces bibliothèques sont conçues pour gérer des scénarios de gestion d'état complexes dans des applications à grande échelle afin que vous n'ayez pas à le faire. Elles aident également à créer un état plus centralisé et organisé.   
  
En parlant de gestion d'état et de partage de données, la solution la plus couramment évoquée est Redux. Mais Redux est souvent considéré comme trop compliqué car il ajoute une couche supplémentaire de complexité. 

Redux est conçu pour gérer l'état de l'application de manière prévisible et cohérente, mais il nécessite que les développeurs apprennent un nouvel ensemble de concepts, tels que les actions, les réducteurs et le magasin. 

D'autres bibliothèques populaires de gestion d'état dans React incluent Zustand, MobX et Recoil. Ces bibliothèques fournissent des fonctionnalités telles que la gestion d'état globale, l'immuabilité et le re-rendu optimisé pour aider à rendre les applications plus performantes et plus faciles à maintenir.  
  
L'utilisation d'une bibliothèque de gestion d'état peut faciliter la gestion de l'état de leur application pour les développeurs et simplifier le processus de passage de données entre les composants. Cela peut prendre un certain temps pour apprendre à utiliser ces bibliothèques efficacement, mais elles peuvent être des outils très puissants pour construire des applications React complexes.

## Qu'est-ce que Pullstate ?

Pullstate est une bibliothèque de gestion d'état beaucoup plus simple et plus légère pour React. Elle simplifie tout le processus et facilite la création d'applications évolutives. 

Puisque React Native est basé sur React, vous pouvez utiliser Pullstate pour construire non seulement des applications web mais aussi des applications mobiles. Il est basé sur le concept de "tirer" les données de l'état, plutôt que de pousser les données dedans.

### Comment utiliser Pullstate

Pour utiliser Pullstate et commencer, vous devez d'abord savoir quel gestionnaire de paquets vous utilisez (yarn ou npm).  
  
Ouvrez votre projet React / React Native existant, et dans le terminal, entrez les commandes suivantes selon que vous utilisez npm ou yarn :

``` terminal
npm install pullstate
//ou
yarn add pullstate

```


Si vous n'avez pas encore d'application React Native, vous pouvez en créer une en utilisant le cli React Native.  
  
Tout d'abord, vous devez vous assurer que vous [avez installé Node.js](https://nodejs.org/en/download).  
  
Ouvrez le terminal dans le dossier où vous souhaitez créer votre application React Native :

``` terminal
npm uninstall -g react-native-cli
npx react-native init myReactNativeApp --template react-native-template-typescript
```

## Comment configurer le Store

Le code ci-dessous et l'image correspondante montrent comment initialiser le code du store Pullstate pour le copier et le coller ci-dessous (c'est ainsi que j'inclurai tout le code dans ce tutoriel - code pour copier, ainsi que son apparence dans un instantané).  
  
Vous pouvez placer le code ci-dessous dans son propre fichier, par exemple `store.ts`, dans le dossier racine de votre projet.

``` typescript
import {Store} from 'pullstate';

interface UIStore {
  user: {
    firstName: string;
    lastName: string;
    acceptedTnC: boolean;
  };
  preferences: {
    isDarkMode: boolean;
    pushNotifications: boolean;
  };
}

const initialStore: UIStore = {
  user: {
    firstName: '',
    lastName: '',
    acceptedTnC: false,
  },
  preferences: {
    isDarkMode: false,
    pushNotifications: false,
  },
};

export const store = new Store<UIStore>({
  user: {
    firstName: '',
    lastName: '',
    acceptedTnC: false,
  },
  preferences: {
    isDarkMode: false,
    pushNotifications: false,
  },
});

```

Voici un aperçu de ce à quoi cela devrait ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/store-2.png)
_image montrant un aperçu du code de configuration du store_

### Que fait ce code ?

Tout d'abord, nous avons créé une interface pour le store Pullstate. Cela contient toutes les informations que nous devrons stocker dans l'état à travers l'application. Nous avons des choses comme le prénom et le nom de l'utilisateur (pour pouvoir les utiliser dans toute l'application). 

Le store peut également contenir des objets imbriqués, par exemple notre objet _preferences_, ce qui rend la gestion de l'état plus propre.  
  
Pour garder les choses simples et permettre un code plus propre à l'avenir, j'ai créé un état initial du store. Cela réinitialise toutes les propriétés de l'état à leurs valeurs par défaut.  
Nous pouvons ensuite (si nécessaire) ramener l'état à son état initial rapidement et facilement. Cela pourrait être très utile dans des situations comme **logOut**, **onError**, et ainsi de suite.

Ensuite, nous initialisons le store et en faisons un objet exportable. Cela signifie qu'après la première fois où nous importons l'objet (idéalement au niveau supérieur de notre application), il est alors accessible dans toute notre application.

## Comment récupérer les données du Store

D'accord, nous avons notre store, mais comment accéder à ces données dans notre composant ?  
Pour récupérer les données du store, nous pouvons utiliser soit les fonctions **getRawState** soit **useState**.

`getRawState()` retourne l'état brut à ce moment précis. Lorsqu'il est appelé, il donne l'état en direct du store Pullstate. Si l'état est mis à jour, la valeur ne sera pas mise à jour.

Par exemple, dans le code ci-dessous, la variable **acceptedTerms** aurait la valeur qu'elle avait au moment de l'appel de `store.getRawState()` :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/getRawState-1.png)
_exemple d'utilisation de la fonction getRawState()_

`useState()` fonctionne de la même manière que la fonction `useState()` de React. Lorsque le store Pullstate est mis à jour, la valeur acceptedTerms sera également mise à jour, provoquant ainsi un re-rendu du composant. 

Pensez à useState dans Pullstate comme une fonction d'écoute - elle attend qu'une valeur soit mise à jour puis vous fournit cette nouvelle valeur mise à jour.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/usestate.png)
_exemple d'utilisation de la fonction store.useState()_

## Exemple concret :

Examinons un exemple concret, impliquant l'acceptation d'une page de conditions générales. Le code ci-dessous va :

* Créer un composant de carte avec quelques termes, et 
* Avoir deux boutons, 'Retour' et 'Suivant', qui exécuteront une fonction lors du clic.

``` typescript
import React from "react";
import { StyleSheet, Text, View } from "react-native";
import { Card } from "react-native-paper";
import { store } from "./store";import { BlueButton } from "../atoms/button";

export const PullStateCard: React.FC = () => {  
    const handleAgreeTerms = () => {
        store.update((state) => {     
            state.user.acceptedTnC = true;    
        });  
    };  

    const handleDisagreeTerms = () => { 
        store.update((state) => {      
            state.user.acceptedTnC = false;    
        });  
    };  

    return (    
        <Card style={[styles.marginTop, styles.padding]}>
            <Text>Nos services sont fournis en l'état. 
            Nous ne garantissons pas la disponibilité, l'exactitude ou l'exhaustivité de nos services. 
            Vous ne pouvez utiliser nos services qu'à des fins légales et conformément à ces termes et conditions.
            </Text>
            <Text style={{ marginTop: 16 }}>
                En cliquant sur 'Suivant', vous acceptez les termes et conditions de cette application
            </Text>
            <View style={styles.row}>
                <BlueButton 
                    styleOverride={styles.button}
                    onPress={handleDisagreeTerms}
                    title="Retour"/>        
                <BlueButton
                    styleOverride={styles.button}
                    onPress={handleAgreeTerms}
                    title="Suivant"/>
            </View>
        </Card>  

       )
}
```

Mes boutons personnalisés :
``` typescript
import {
  StyleProp,
  StyleSheet,
  Text,
  TouchableOpacity,
  ViewStyle,
} from 'react-native';
import React from 'react';

interface BlueButtonProps {
  onPress: () => void;
  title: string;
  styleOverride?: StyleProp<ViewStyle>;
}

export const BlueButton: React.FC<BlueButtonProps> = ({
  onPress,
  title,
  styleOverride,
}) => (
  <TouchableOpacity onPress={onPress} style={[styles.button, styleOverride]}>
    <Text style={styles.buttonText}>{title}</Text>
  </TouchableOpacity>
);

const styles = StyleSheet.create({
  button: {
    backgroundColor: '#007AFF',
    borderRadius: 10,
    padding: 10,
    alignItems: 'center',
    marginVertical: 10,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
```

Le code du composant Card ressemblerait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/CARD-1.png)

### Dissection des fonctions de gestion

Les fonctions de gestion sont appelées lorsque les boutons sont cliqués. Selon celui que vous cliquez, une action particulière sera exécutée. Mais l'intention sous-jacente est la même, en ce sens qu'elles modifient toutes deux l'état du store Pullstate que nous avons créé précédemment.

L'une définira `user.acceptedTnC` à **true**, et l'autre à **false**. Nous avons utilisé la fonction `.update()` sur l'objet `store` que nous avons créé précédemment, et nous lui avons passé une fonction anonyme pour mettre à jour les propriétés.   
  
La méthode n'est pas limitée à la mise à jour d'une seule propriété, et vous pouvez mettre à jour plusieurs propriétés à la fois, par exemple :

``` typescript
store.update((state) => {  
    state.user.acceptedTnC = true;  
    state.user.firstName = "John";  
    state.user.lastName = "Doe";  
    state.preferences.pushNotifications = true;
});
```

## Pourquoi Pullstate et la gestion d'état global sont-ils si utiles ?

La beauté d'utiliser l'état de cette manière signifie que le composant ne gère pas le store, c'est l'application qui le fait. Vous pouvez ensuite partager cela dans toute l'application, et avoir d'autres composants écouter ces changements.  
  
Prenons l'exemple ci-dessus un peu plus loin et avons un composant séparé qui affichera un message pertinent dépendant de l'état de la propriété acceptedTnC.

```
const styles = StyleSheet.create({  
    disagree: {    
        color: "red",
        textDecoration: "italic",
    },
    accepted: {
        color: "#0d8009",
    },  
    marginTop: {
        marginTop: 10,
    },
});

export const AgreedToTerms: React.FC = () => {  
    const acceptedTerms = store.useState((state) => state.user.acceptedTnC);
    return (    
        <View style={styles.marginTop}> 
            {acceptedTerms ? (
                <Text style={styles.accepted}>
                    Vous avez accepté avec succès les Termes et Conditions                  </Text>) : (
                 <Text style={styles.disagree}>
                     Veuillez accepter les Termes et Conditions en appuyant sur 'Suivant'        
                     </Text>)
            }
        </View>
    )
};
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/accepted.png)

  
Si vous importez ces composants et ajoutez votre propre style à App.tsx (App.js pour JS) comme ceci :

``` typescript
<PullStateCard />
<AgreedToTerms />
```

Votre code complet App.tsx ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/app_whole.png)

``` typescript
import React from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  View,
} from 'react-native';

import {AgreedToTerms, PullStateCard} from './src/pullstate/pullstate_example';

const App = () => {
  return (
    <SafeAreaView>
      <StatusBar barStyle={'light-content'} />
      <ScrollView contentInsetAdjustmentBehavior="automatic">
        <View style={styles.container}>
          <PullStateCard />
          <AgreedToTerms />
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    height: '100%',
    paddingHorizontal: 16,
    paddingVertical: 16,
  },
});

export default App;

```

Une fois que vous avez copié le code, vous pouvez ajouter votre propre style si nécessaire et exécuter l'application. 

Cliquez sur le bouton **Suivant**, et votre texte deviendra vert et vous informera que vous avez accepté les termes.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/SCR-20230329-tsq.png)

  
Si vous cliquez ensuite sur le bouton **Retour**, vous verrez que le texte est rouge vous informant que vous devez accepter les termes :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/SCR-20230329-ts9.png)

  
Tout cela est alimenté par le store global Pullstate. Il n'y a pas d'état interne sur le composant **AgreedToTerms**. 

## Découplage de la logique

Le découplage fait référence à la pratique de séparation des différentes parties de votre code afin qu'elles ne soient pas étroitement dépendantes ou liées les unes aux autres.

Pensez à cela comme à la construction avec des LEGO. Lorsque vous construisez avec des LEGO, chaque pièce peut se connecter à d'autres pièces, mais elles peuvent également être facilement déconnectées et reconnectées avec d'autres pièces. Cela facilite la modification de votre construction LEGO.

De même, en programmation, lorsque nous découplons notre code, nous le rendons plus facile à changer et à modifier sans affecter d'autres parties de notre code. Cela est particulièrement important dans les grandes applications avec de nombreux composants ou modules différents.

En déplaçant l'état d'acceptation des "termes acceptés" vers Pullstate, il peut être ajouté et supprimé de tout composant qui en aurait besoin. Il n'est pas étroitement couplé au composant AgreedToTerms, et devient un morceau d'état réutilisable qui est mis à jour globalement. Par exemple, nous pourrions l'utiliser ailleurs dans l'application comme mécanisme d'autorisation, pour afficher/masquer des éléments d'interface utilisateur, et bien plus encore.

## Conclusion

J'espère que vous avez trouvé cet article utile et que vous avez apprécié cette brève introduction à Pullstate et à la gestion d'état global.

Ce que nous avons couvert :

* Ce que sont les bibliothèques de gestion d'état
*  Une introduction à Pullstate et comment l'intégrer dans votre application
* Les avantages de Pullstate et son fonctionnement

Pour toute question supplémentaire, n'hésitez pas à me contacter sur [Twitter](http://twitter.com/gweaths).