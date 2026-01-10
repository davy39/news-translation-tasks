---
title: Comment créer une application de calculatrice avec React Native – Un tutoriel
  étape par étape
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-02T19:29:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-calculator-app-using-react-native-a-step-by-step-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/banner
seo_title: Comment créer une application de calculatrice avec React Native – Un tutoriel
  étape par étape
---

how-to-build-calculator-app-using-react-native-1.png
tags:
- name: JavaScript
  slug: javascript
- name: React Native
  slug: react-native
seo_title: null
seo_desc: "Par Muhammad Adam\nUne application de calculatrice est une application simple qui est toujours disponible sur chaque appareil Android, iOS et de bureau. \nDans cet article, nous allons créer une application de calculatrice en utilisant React Native et Expo. Alors pourquoi utilisons-nous ces outils..."
---

Par Muhammad Adam

Une application de calculatrice est une application simple qui est toujours disponible sur chaque appareil Android, iOS et de bureau.

Dans cet article, nous allons créer une application de calculatrice en utilisant React Native et Expo. Alors pourquoi utilisons-nous ces outils ?

React Native est un framework basé sur JavaScript que vous pouvez utiliser pour développer des applications mobiles sur deux systèmes d'exploitation en même temps – Android et iOS. React Native a été lancé pour la première fois en 2015 par Facebook, et est open source.

Vous pouvez trouver plus d'informations sur React Native [ici](https://reactnative.dev/docs/getting-started).

Expo est un ensemble d'outils, de bibliothèques et de services que vous pouvez utiliser pour simplifier votre code React Native. Ainsi, vous pouvez exécuter des applications React Native sur l'émulateur Expo.

Vous pouvez trouver plus d'informations sur Expo [ici](https://expo.dev/).

Avant de commencer à créer une application de calculatrice, vous devrez d'abord installer Node.js, React Native et Expo sur votre ordinateur.

### Prérequis

1. Installer Node.js – vous pouvez voir comment l'installer [ici](https://nodejs.org/en/download/).
2. Installer React Native – vous pouvez voir la documentation d'installation [ici](https://reactnative.dev/docs/environment-setup).
3. Installer Expo – vous pouvez voir la documentation d'installation [ici](https://reactnative.dev/docs/environment-setup).

## Étape 1 : Créer un nouveau projet

La première étape consiste à créer un nouveau projet. Utilisez l'interface de ligne de commande Expo pour créer la base de code React Native avec la commande suivante :

```bash
$ expo init calculator-app
```

Ensuite, vous aurez le choix de démarrer le projet que vous souhaitez. Ici, nous choisissons l'option vide et utilisons JavaScript comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-349.png)
_choisir le modèle de projet expo_

Après cela, le processus se poursuivra en téléchargeant toutes les dépendances.

## Étape 2 : Créer le composant Bouton

Lorsque vous développez des applications en utilisant React Native, assurez-vous de décomposer les composants d'interface utilisateur en composants plus petits afin que le code que vous créez puisse être réutilisable.

Tout d'abord, créez un nouveau dossier appelé « **components** » pour stocker votre code de composant. Le premier composant que nous allons créer est un Bouton, alors créez un nouveau fichier appelé **Button.js**. Voici le code source pour le composant Bouton :

```javascript
import { Dimensions, StyleSheet, Text, TouchableOpacity } from "react-native";

export default ({ onPress, text, size, theme }) => {
  const buttonStyles = [styles.button];
  const textStyles = [styles.text];

  if (size === "double") {
    buttonStyles.push(styles.buttonDouble);
  }

  if (theme === "secondary") {
    buttonStyles.push(styles.buttonSecondary);
    textStyles.push(styles.textSecondary);
  } else if (theme === "accent") {
    buttonStyles.push(styles.buttonAccent);
  }

  return (
    <TouchableOpacity onPress={onPress} style={buttonStyles}>
      <Text style={textStyles}>{text}</Text>
    </TouchableOpacity>
  );
};
```

Explication du code :

* À la ligne 3, il y a quatre props dont nous avons besoin pour créer ce composant Bouton : onPress, text, size et theme.
* Chacune des props a une fonction comme onPress pour gérer les actions sur les boutons.
* Le composant bouton que nous avons créé a 2 types de thèmes, secondary et accent, et 1 taille, double.
* Le composant bouton utilise le composant par défaut de React Native, TouchableOpacity.

Après avoir créé le code du composant, n'oubliez pas d'ajouter le style pour ce composant bouton. Voici le code pour le style du composant :

```javascript
// définir la dimension
const screen = Dimensions.get("window");
const buttonWidth = screen.width / 4;

const styles = StyleSheet.create({
  button: {
    backgroundColor: "#333333",
    flex: 1,
    height: Math.floor(buttonWidth - 10),
    alignItems: "center",
    justifyContent: "center",
    borderRadius: Math.floor(buttonWidth),
    margin: 5,
  },
  text: {
    color: "#fff",
    fontSize: 24,
  },
  textSecondary: {
    color: "#060606",
  },
  buttonDouble: {
    width: screen.width / 2 - 10,
    flex: 0,
    alignItems: "flex-start",
    paddingLeft: 40,
  },
  buttonSecondary: {
    backgroundColor: "#a6a6a6",
  },
  buttonAccent: {
    backgroundColor: "#ffc107",
  },
});

```

Ainsi, le code complet de notre composant bouton est le suivant :

```javascript
import { Dimensions, StyleSheet, Text, TouchableOpacity } from "react-native";

export default ({ onPress, text, size, theme }) => {
  const buttonStyles = [styles.button];
  const textStyles = [styles.text];

  if (size === "double") {
    buttonStyles.push(styles.buttonDouble);
  }

  if (theme === "secondary") {
    buttonStyles.push(styles.buttonSecondary);
    textStyles.push(styles.textSecondary);
  } else if (theme === "accent") {
    buttonStyles.push(styles.buttonAccent);
  }

  return (
    <TouchableOpacity onPress={onPress} style={buttonStyles}>
      <Text style={textStyles}>{text}</Text>
    </TouchableOpacity>
  );
};

// définir la dimension
const screen = Dimensions.get("window");
const buttonWidth = screen.width / 4;

const styles = StyleSheet.create({
  button: {
    backgroundColor: "#333333",
    flex: 1,
    height: Math.floor(buttonWidth - 10),
    alignItems: "center",
    justifyContent: "center",
    borderRadius: Math.floor(buttonWidth),
    margin: 5,
  },
  text: {
    color: "#fff",
    fontSize: 24,
  },
  textSecondary: {
    color: "#060606",
  },
  buttonDouble: {
    width: screen.width / 2 - 10,
    flex: 0,
    alignItems: "flex-start",
    paddingLeft: 40,
  },
  buttonSecondary: {
    backgroundColor: "#a6a6a6",
  },
  buttonAccent: {
    backgroundColor: "#ffc107",
  },
});

```

## Étape 3 : Créer le composant Ligne

Le composant suivant que nous allons créer est un composant Ligne. Ce composant est utile pour créer des lignes lorsque nous voulons traiter les mises en page.

Voici le code pour le composant Ligne et son code de style :

```javascript
import { StyleSheet, View } from "react-native";

const Row = ({ children }) => {
  return <View style={styles.container}>{children}</View>;
};

// créer les styles de la ligne
const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
  },
});

export default Row;

```

Voici ce qui se passe :

* Dans le composant ligne, il y a 1 prop dont nous avons besoin : children.
* Le composant ligne utilise le composant View par défaut de React Native.
* flexDirection : "row" dans ce style est utilisé pour faire en sorte que la mise en page soit une ligne.

## Étape 4 : Créer la logique de la calculatrice

Créez un nouveau dossier appelé util et un nouveau fichier **calculator.js**. Ici, nous allons créer la logique des fonctions dans l'application de calculatrice que nous implémenterons plus tard dans le fichier **App.js**. Voici le code complet :

```javascript
export const initialState = {
  currentValue: "0",
  operator: null,
  previousValue: null,
};

export const handleNumber = (value, state) => {
  if (state.currentValue === "0") {
    return { currentValue: `${value}` };
  }

  return {
    currentValue: `${state.currentValue}${value}`,
  };
};

const handleEqual = (state) => {
  const { currentValue, previousValue, operator } = state;

  const current = parseFloat(currentValue);
  const previous = parseFloat(previousValue);
  const resetState = { operator: null, previousValue: null };

  switch (operator) {
    case "+":
      return {
        currentValue: `${previous + current}`,
        ...resetState,
      };
    case "-":
      return {
        currentValue: `${previous - current}`,
        ...resetState,
      };
    case "*":
      return {
        currentValue: `${previous * current}`,
        ...resetState,
      };
    case "/":
      return {
        currentValue: `${previous / current}`,
        ...resetState,
      };

    default:
      return state;
  }
};

// fonction de calculatrice
const calculator = (type, value, state) => {
  switch (type) {
    case "number":
      return handleNumber(value, state);
    case "clear":
      return initialState;
    case "posneg":
      return {
        currentValue: `${parseFloat(state.currentValue) * -1}`,
      };
    case "percentage":
      return {
        currentValue: `${parseFloat(state.currentValue) * 0.01}`,
      };
    case "operator":
      return {
        operator: value,
        previousValue: state.currentValue,
        currentValue: "0",
      };
    case "equal":
      return handleEqual(state);
    default:
      return state;
  }
};

export default calculator;

```

Et voici ce qui se passe :

* initialState est utilisé pour donner la valeur par défaut à notre application de calculatrice.
* La fonction handleNumber sert à retourner la valeur de la calculatrice, et a 2 props – value et state.
* La fonction handleEqual sert à traiter la valeur définie de chaque opérateur mathématique et retourne sa valeur.
* La fonction calculator valide chaque opérateur donné. Par exemple, si le nombre appelle la fonction handleNumber, si c'est clear, elle retournera la valeur d'état par défaut de initiaState, et ainsi de suite.

## Étape 5 : Refactoriser le fichier App.js

Après avoir créé tous les composants et le processus logique, l'étape suivante consiste à apporter des ajustements au code dans le fichier App.js. Voici le code complet :

```javascript
import React, { Component } from "react";
import { SafeAreaView, StyleSheet, Text, View } from "react-native";
import Button from "./components/Button";
import Row from "./components/Row";
import calculator, { initialState } from "./util/calculator";

// créer un composant de classe App
export default class App extends Component {
  state = initialState;

  // méthode handleTap
  HandleTap = (type, value) => {
    this.setState((state) => calculator(type, value, state));
  };

  // méthode render
  render() {
    return (
      <View style={styles.container}>
        {/* Status bae ici */}
        <SafeAreaView>
          <Text style={styles.value}>
            {parseFloat(this.state.currentValue).toLocaleString()}
          </Text>

          {/* Créer un composant Row */}
          <Row>
            <Button
              text="C"
              theme="secondary"
              onPress={() => this.HandleTap("clear")}
            />

            <Button
              text="+/-"
              theme="secondary"
              onPress={() => this.HandleTap("posneg")}
            />

            <Button
              text="%"
              theme="secondary"
              onPress={() => this.HandleTap("percentage")}
            />

            <Button
              text="/"
              theme="accent"
              onPress={() => this.HandleTap("operator", "/")}
            />
          </Row>

          {/* Nombre */}
          <Row>
            <Button text="7" onPress={() => this.HandleTap("number", 7)} />
            <Button text="8" onPress={() => this.HandleTap("number", 8)} />
            <Button text="9" onPress={() => this.HandleTap("number", 9)} />
            <Button
              text="X"
              theme="accent"
              onPress={() => this.HandleTap("operator", "*")}
            />
          </Row>

          <Row>
            <Button text="5" onPress={() => this.HandleTap("number", 5)} />
            <Button text="6" onPress={() => this.HandleTap("number", 6)} />
            <Button text="7" onPress={() => this.HandleTap("number", 7)} />
            <Button
              text="-"
              theme="accent"
              onPress={() => this.HandleTap("operator", "-")}
            />
          </Row>

          <Row>
            <Button text="1" onPress={() => this.HandleTap("number", 1)} />
            <Button text="2" onPress={() => this.HandleTap("number", 2)} />
            <Button text="3" onPress={() => this.HandleTap("number", 3)} />
            <Button
              text="+"
              theme="accent"
              onPress={() => this.HandleTap("operator", "+")}
            />
          </Row>

          <Row>
            <Button text="0" onPress={() => this.HandleTap("number", 0)} />
            <Button text="." onPress={() => this.HandleTap("number", ".")} />
            <Button
              text="="
              theme="primary"
              onPress={() => this.HandleTap("equal", "=")}
            />
          </Row>
        </SafeAreaView>
      </View>
    );
  }
}

// créer les styles de l'application
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#202020",
    justifyContent: "flex-end",
  },
  value: {
    color: "#fff",
    fontSize: 42,
    textAlign: "right",
    marginRight: 20,
    marginBottom: 10,
  },
});

```

Quelques notes rapides :

* handleTap est une fonction que nous avons créée qui vise à fournir des valeurs d'état et à appeler utils/calculator.
* Ici, nous appelons deux composants, Button et Row, pour concevoir l'apparence de la calculatrice telle que ses nombres, les opérations mathématiques et le processus de calcul.

## Étape 6 : Exécuter l'application

Dans cette étape, nous allons essayer d'exécuter l'application de calculatrice sur l'appareil ou nous pouvons utiliser un émulateur. Ici, j'utilise le simulateur iPhone de MacOS. Exécutez la commande suivante pour exécuter le programme :

```bash
$ yarn ios
```

Le processus d'exécution ici utilise Expo comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-350.png)

Si le processus de compilation est terminé, alors l'affichage de l'application de calculatrice que nous avons programmée sera comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-351.png)

## Conclusion

C'est assez pour cet article. Vous avez appris le style, les composants, les props et les états dans React Native et avez créé une application de calculatrice fonctionnelle.

Si vous avez besoin du code source complet, vous pouvez visiter mon dépôt GitHub ici : [https://github.com/bangadam/calculator-app](https://github.com/bangadam/calculator-app)

### Merci d'avoir lu !

Disponible pour un nouveau projet ! Parlons-en.  
Email : [bangadam.dev@gmail.com](mailto:bangadam.dev@gmail.com)  
Linkedin : [https://www.linkedin.com/in/bangadam](https://www.linkedin.com/in/bangadam/)