---
title: Composants fonctionnels vs composants de classe dans React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-17T19:46:00.000Z'
originalURL: https://freecodecamp.org/news/functional-vs-class-components-react-native
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dcf740569d1a4ca39c4.jpg
tags:
- name: class
  slug: class
- name: components
  slug: components
- name: React Native
  slug: react-native
seo_title: Composants fonctionnels vs composants de classe dans React Native
seo_desc: 'In React Native, there are two main types of components that make up an
  application: functional components and class components. These are structured the
  same as they would be in a regular React app for the web.

  Class Components

  Class components are ...'
---

Dans React Native, il existe deux principaux types de composants qui constituent une application : les **composants fonctionnels** et les **composants de classe**. Ces derniers sont structurés de la même manière que dans une application React classique pour le web.

## Composants de classe

Les composants de classe sont des classes JavaScript ES2015 qui étendent une classe de base de React appelée `Component`.

```js
class App extends Component {
    render () {
        return (
            <Text>Bonjour le monde !</Text>
        )
    }
}
```

Cela donne à la classe `App` accès aux méthodes du cycle de vie de React comme `render`, ainsi qu'à la gestion de l'état (state) et des props du parent.

## Composants fonctionnels

Les composants fonctionnels sont plus simples. Ils ne gèrent pas leur propre état ni n'ont accès aux méthodes du cycle de vie fournies par React Native. Ce sont littéralement de simples fonctions JavaScript, et on les appelle parfois des composants sans état.

```js
const PageOne = () => {
    return (
        <h1>Page Une</h1>
    );
}
```

## Résumé

Les composants de classe sont utilisés comme conteneurs pour gérer l'état et envelopper les composants enfants.

Les composants fonctionnels sont généralement utilisés à des fins d'affichage - ces composants appellent des fonctions des composants parents pour gérer les interactions utilisateur ou les mises à jour d'état.

## Plus d'informations sur l'état des composants

### État du composant

Dans les composants de `Classe`, il existe un moyen de stocker et de gérer l'état intégré à React Native.

```javascript
class App extends Component {
  constructor () {
    super();
    this.state = {
      counter: 0
    };
  }
  incrementCount () {
    this.setState({
      counter: this.state.counter + 1
    });
  }
  decrementCount () {
    this.setState({
      counter: this.state.counter - 1
    });
  }
  render () {
    return (
      <View>
        <Text>Compteur : {this.state.counter}</Text>
        <Button onPress={this.decrementCount.bind(this)}>-</Button>
        <Button onPress={this.incrementCount.bind(this)}>+</Button>
      </View>
    );
  }
}
```

L'état est similaire aux props, mais il est privé et entièrement contrôlé par le composant. Ici, la méthode `constructor()` appelle le constructeur de la classe parente avec `super();` - **`Component`** est la classe parente de `App` parce que nous utilisons le mot-clé `extends`. La méthode `constructor()` initialise également l'objet d'état du composant :

```text
this.state = {
  counter: 0
};
```

L'état peut être affiché dans le composant :

```js
{this.state.counter}
```

Ou mis à jour en appelant :

```js
this.setState({});
```

**Note :** En dehors de sa création initiale dans la méthode `constructor()` de votre composant, vous ne devez jamais modifier directement l'état du composant avec `this.state =`. Vous devez utiliser `this.setState` comme on peut le voir dans les fonctions `incrementCount` et `decrementCount` ci-dessus.

Le compteur est incrémenté et décrémenté en appelant les fonctions passées aux gestionnaires `onPress`, tout comme si vous appeliez un gestionnaire de clic depuis JavaScript sur le web.

_ASIDE : Dans le premier exemple, `<Button>` est un composant personnalisé ; c'est une combinaison de `<TouchableOpacity>` et `<Text>` de l'API React Native :_

```js
const Button = ({ onPress, children, buttonProps, textProps }) => {
  const { buttonStyle, textStyle } = styles;
  return (
    <TouchableOpacity onPress={onPress} style={[buttonStyle, buttonProps]}>
      <Text style={[textStyle, textProps]}>
        {children}
      </Text>
    </TouchableOpacity>
  );
};
```

## Plus d'informations sur React Native :

* [Guide React Native](https://www.freecodecamp.org/news/react-native-guide/)