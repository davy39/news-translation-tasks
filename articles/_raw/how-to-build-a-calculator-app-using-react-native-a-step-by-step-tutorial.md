---
title: How to Build a Calculator App Using React Native – A Step-by-Step Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-02T19:29:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-calculator-app-using-react-native-a-step-by-step-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/banner---how-to-build-calculator-app-using-react-native-1.png
tags:
- name: JavaScript
  slug: javascript
- name: React Native
  slug: react-native
seo_title: null
seo_desc: "By Muhammad Adam\nA calculator application is a simple application that\
  \ is always available on every Android, iOS, and desktop device. \nIn this article,\
  \ we will build a calculator application using React Native and Expo. So why are\
  \ we using these tool..."
---

By Muhammad Adam

A calculator application is a simple application that is always available on every Android, iOS, and desktop device. 

In this article, we will build a calculator application using React Native and Expo. So why are we using these tools? 

React Native is a JavaScript-based framework you can use to develop mobile applications on two operating systems at the same time – Android and iOS. React Native was first launched in 2015 by Facebook, and is open source.

You can find out more information about React Native [here](https://reactnative.dev/docs/getting-started).

Expo is a set of tools, libraries, and services that you can use to simplify your React Native code. So you can run React Native apps on the Expo emulator.

You can find out more information about Expo [here](https://expo.dev/).

Before we start making a calculator application, you'll first need to install Node.js, React Native, and Expo on your computer.

### Prerequisites

1. Install Node.js – you can see how to install it [here](https://nodejs.org/en/download/).
2. Install React Native – you can see the installation documentation [here](https://reactnative.dev/docs/environment-setup).
3. Install Expo – you can see the installation documentation [here](https://reactnative.dev/docs/environment-setup).

## Step 1: Create a New Project

The first step is to create a new project. Use the Expo CLI to create the React Native code base with the following command:

```bash
$ expo init calculator-app
```

Then you'll have the choice of starting the project you want. Here we choose the blank option and use JavaScript as below:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-349.png)
_choose template expo project_

After that, the process will continue by downloading all the dependencies.

## Step 2: Create the Button Component

When you're developing applications using React Native, make sure you break down UI components into smaller components so that the code you create can be reusable.

First, create a new folder called “**components**” to store your component code. The first component we will create is a Button, so create a new file called **Button.js**. Here is the source code for the Button component:

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

Code explanation:

* In line 3, there are four props that we need in order to make this Button component: onPress, text, size and theme.
* Each of the props has a function like onPress for handling actions on buttons.
* The button component that we created has 2 types of themes, secondary and accent, and 1 size, double.
* The button component uses the default React Native component, TouchableOpacity.

After we make the code from the component, don’t forget to add the styling for this button component. Here is the code for the component's styling:

```javascript
// set dimmenstion
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

So the complete code of our button component is as follows:

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

// set dimmenstion
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

## Step 3: Create the Row Component

The next component that we will create is a Row component. This component is useful for creating rows when we want to process layouts. 

Here is the code for the Row component and its styling code:

```javascript
import { StyleSheet, View } from "react-native";

const Row = ({ children }) => {
  return <View style={styles.container}>{children}</View>;
};

// create styles of Row
const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
  },
});

export default Row;

```

Here's what's going on:

* In the row component, there is 1 prop that we need: children.
* The row component uses the default View component from React Native.
* flexDirection: “row” in this styling is used to make the layout a row.

## Step 4: Create the Calculator Logic

Create a new folder called util and a new file **calculator.js**. Here we will create function logic in the calculator application which we will implement later in the **App.js** file. Here is the complete code:

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

// calculator function
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

And here's what's going on:

* initialState is used to give the default value to our calculator app.
* The function handleNumber serves to return the value of the calculator, and has 2 props – value and state.
* The function handle Equal serves to process the set value of each mathematical operator and returns its value.
* The function calculator validates every given operator. For example, if the number calls the handleNumber function, if it is clear it will return the default state value from initiaState, and so on.

## Step 5: Refactor the App.js File

After we have created all the components and the logic process, the next step is to make adjustments to the code in the App.js file. Here is the full code:

```javascript
import React, { Component } from "react";
import { SafeAreaView, StyleSheet, Text, View } from "react-native";
import Button from "./components/Button";
import Row from "./components/Row";
import calculator, { initialState } from "./util/calculator";

// create class component of App
export default class App extends Component {
  state = initialState;

  // handle tap method
  HandleTap = (type, value) => {
    this.setState((state) => calculator(type, value, state));
  };

  // render method
  render() {
    return (
      <View style={styles.container}>
        {/* Status bae here */}
        <SafeAreaView>
          <Text style={styles.value}>
            {parseFloat(this.state.currentValue).toLocaleString()}
          </Text>

          {/* Do create componentRow */}
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

          {/* Number */}
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

// create styles of app
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

A few quick notes:

* handleTap is a function that we created which aims to provide state values and call utils/calculator.
* Here we call two components, Button and Row, to design the appearance of the calculator such as its numbers, mathematical operations, and the calculation process.

## Step 6: Run the App

In this step we will try to run the calculator application on the device or we can use an emulator. Here I use the iPhone simulator from MacOS. Run the command below to run the program:

```bash
$ yarn ios
```

The running process here uses Expo as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-350.png)

If the compiling process is complete, then the display of the calculator application that we programmed will be like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-351.png)

## Conclusion

That’s enough for this article. You learned about styling, components, props, and states in React Native and built a functional calculator app.

If you need the full source code, you can visit my GitHub repository here: [https://github.com/bangadam/calculator-app](https://github.com/bangadam/calculator-app)

### Thanks For Reading!

Available for a new project! Let’s have a talk.  
Email: [bangadam.dev@gmail.com](mailto:bangadam.dev@gmail.com)  
Linkedin: [https://www.linkedin.com/in/bangadam](https://www.linkedin.com/in/bangadam/)

