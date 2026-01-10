---
title: Comment créer une application de todo en temps réel avec React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-01T18:27:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-real-time-todo-app-with-react-native-19a1ce15b0b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e2uBLw946pDyqjdV5xAJpQ.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de todo en temps réel avec React Native
seo_desc: 'By Divyanshu Maithani

  A todo app touches on all the important parts of building any data-driven app, including
  the Create, Read, Update and Delete (CRUD) operations. In this story I’ll be building
  a todo app with one of the most popular mobile framew...'
---

Par Divyanshu Maithani

Une application de todo touche à toutes les parties importantes de la construction de toute application pilotée par les données, y compris les opérations **C**réer, **L**ire, **M**ettre à jour et **S**upprimer (CRUD). Dans cet article, je vais construire une application de todo avec l'un des [frameworks mobiles les plus populaires](https://stateofjs.com/2017/mobile/results/), **React Native**.

Je vais utiliser [**ReactiveSearch Native**](https://github.com/appbaseio/reactivesearch/tree/dev/packages/native), une bibliothèque open-source qui fournit des composants UI React Native et simplifie la construction d'applications pilotées par les données.

Voici ce que je vais construire dans cet article :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bbDAbPL1rYl2k5fPFDtFHg.png)
_Application de Todo_

Découvrez l'application sur [snack](https://snack.expo.io/@dhruvdutt/todo) ou sur [expo](https://expo.io/@dhruvdutt/todos).

### Qu'est-ce que React Native ?

Voici ce que disent les [docs](https://facebook.github.io/react-native/) :

> React Native vous permet de créer des applications mobiles en utilisant uniquement JavaScript. Il utilise la même conception que React, vous permettant de composer une UI mobile riche à partir de composants déclaratifs.

Même si vous commencez tout juste avec React ou React Native, vous devriez être capable de suivre cet article et de construire votre propre application de todo en temps réel.

### Pourquoi utiliser ReactiveSearch ? ⚔️

[ReactiveSearch](https://github.com/appbaseio/reactivesearch) est une bibliothèque open-source de composants UI React et React Native pour Elasticsearch que j'ai co-écrite avec [des personnes formidables](https://github.com/appbaseio/reactivesearch/graphs/contributors). Elle fournit une variété de composants React Native qui peuvent [se connecter à n'importe quel cluster Elasticsearch](https://opensource.appbase.io/reactive-manual/native/getting-started/reactivebase.html#connect-to-elasticsearch).

J'ai écrit un autre article sur [Building a GitHub Repo Explorer with React and Elasticsearch](https://medium.freecodecamp.org/building-a-github-repo-explorer-with-react-and-elasticsearch-8e1190e59c13) que vous pouvez consulter pour un aperçu rapide d'Elasticsearch. Même si vous n'avez aucune expérience avec Elasticsearch, vous devriez être capable de suivre cet article sans problème.

### Installation des outils ⚒️

Nous allons utiliser la [version React Native](https://opensource.appbase.io/reactivesearch/native) de la bibliothèque ici.

Avant de commencer à construire l'UI, nous devons créer un datastore dans Elasticsearch. ReactiveSearch fonctionne avec n'importe quel index Elasticsearch et vous pouvez facilement [l'utiliser avec votre propre ensemble de données](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html).

![Image](https://cdn-media-1.freecodecamp.org/images/1*7be2L3leZOfV6hwRIcB9Mg.png)
_Voir mon ensemble de données d'application [ici](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAALwAAAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFs4RH-_LaQFp2SlHxdkdiaJMgDx8HsBmHrHmxFLRm7V1uYmmy_j7CIuOAUjTBNw0KgomWuYOXFddgJRsGIU7fsxTMJHKDeitU2LeOk2yVyC7H5mdOvPQ84QV-WGxMqxGGV7LjU-urZhg0CpMqTT3OZQPUib0tK7qbmGxGDnUaoY_1q4GKLDtvfIuD4EF0ZJHcCe_vWVP-1QtnZklZNaGFkoid1LOlZWFaH_-wziAA&amp;editable=false" rel="noopener" target="_blank" title="). Vous pouvez également cloner cela dans votre propre application_

Pour faire court, vous pouvez utiliser [mon ensemble de données](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJuAAAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFs4RH-_LaQFp2SlHxdkdiaJMgDx8HsBmHrHmxFLRm7V1uYmmy_j7CIuOAUjTBNw0KgomWuYOXFddgJRsGIU7fsxTMJHKDeitU2LeOk2yVyC7H5mdPqXB8pzL_9FBmAA) directement ou en créer un pour vous-même en utilisant [appbase.io](https://appbase.io/) qui vous permet de créer un index Elasticsearch hébergé (aka app).

Tous les todos sont structurés dans le format suivant :

```js
{
  "title": "react-native",
  "completed": true,
  "createdAt": 1518449005768
}
```

### Le projet de départ

Avant de commencer, je recommande d'installer [yarn](https://yarnpkg.com/lang/en/docs/install/). Sur Linux, cela peut être fait simplement en ajoutant le dépôt yarn et en exécutant la commande d'installation via votre gestionnaire de paquets. Sur Mac, vous devriez d'abord installer [Homebrew](https://brew.sh/) pour simplifier les choses. [Voici](https://yarnpkg.com/lang/en/docs/install/) les docs d'installation de yarn pour plus de détails. La prochaine chose que vous pouvez installer est [watchman](https://facebook.github.io/watchman/docs/install.html). C'est un service de surveillance de fichiers qui aidera le packager react-native à fonctionner en douceur.

J'ai configuré le projet de départ avec [create-react-native-app](https://github.com/react-community/create-react-native-app) dans une branche GitHub [ici](https://github.com/appbaseio-apps/todos-native/tree/base). Vous pouvez [télécharger un zip](https://github.com/appbaseio-apps/todos-native/archive/base.zip) ou cloner la branche de base en exécutant la commande suivante : ?

```
git clone -b base https://github.com/appbaseio-apps/todos-native
```

* Ensuite, installez les dépendances et démarrez le packager :

```
cd todos-native && yarn && yarn start
```

* Après le démarrage du packager, vous pouvez exécuter l'application sur votre téléphone en utilisant l'application [Expo](https://expo.io/) ou en utilisant un émulateur Android ou IOS :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vTzfrdAPwha5GKpkzxaOeQ.png)
_Configuration de base avec tous les onglets. Clonez depuis [ici](https://github.com/appbaseio-apps/todos-native/tree/base" rel="noopener" target="_blank" title=")._

### Plongeons dans le code ?

Une fois que vous avez cloné le code depuis la [branche de base](https://github.com/appbaseio-apps/todos-native/tree/base), vous devriez voir une structure de répertoire comme ci-dessous :

```
navigation
├── RootComponent.js         // Composant racine pour notre application
├── MainTabNavigator.js      // Composant de navigation par onglets
screens
├── TodosScreen.js           // Affiche le TodosContainer
components        
├── Header.js                // Composant d'en-tête         
├── AddTodo.js               // Entrée pour ajouter un todo        
├── AddTodoButton.js         // Bouton flottant pour ajouter un todo
├── TodoItem.js              // L'élément todo         
├── TodosContainer.js        // Conteneur principal des todos api
├── todos.js                 // APIs pour effectuer des écritures
constants                    // Toutes les constantes utilisées dans l'application
types                        // Type Todo à utiliser avec prop-types
utils                        // La logique de streaming va ici
```

Décomposons ce que la configuration de base comprend :

#### 1. Navigation

* Toutes les configurations nécessaires pour se connecter à Elasticsearch se trouvent dans `constants/Config.js`.
* Nous utilisons [TabNavigator](https://reactnavigation.org/docs/tab-navigator.html) de [react-navigation](https://reactnavigation.org/) pour afficher les écrans de todos **Tous**, **Actifs** et **Complétés**. Cela est rendu par `navigation/RootComponent.js`. Vous remarquerez que `RootComponent` enveloppe tout dans le composant `[ReactiveBase](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html)` de ReactiveSearch. Ce composant fournit toutes les données nécessaires aux composants enfants ReactiveSearch. Vous pouvez connecter votre propre index Elasticsearch ici en mettant simplement à jour les configurations dans `constants/Config.js`.

La logique de navigation est présente dans `navigation/MainNavigator.js`. Passons en revue son fonctionnement. [Voici](https://reactnavigation.org/docs/tab-based-navigation.html) les docs pour la navigation par onglets si vous souhaitez vous référer à quelque chose.

```js
import React from 'react';
import { MaterialIcons } from '@expo/vector-icons';
import { TabNavigator, TabBarBottom } from 'react-navigation';

import Colors from '../constants/Colors';
import CONSTANTS from '../constants';
import TodosScreen from '../screens/TodosScreen';

const commonNavigationOptions = ({ navigation }) => ({
    header: null,
    title: navigation.state.routeName,
});

// nous passons simplement ces éléments pour rendre différentes routes
const routeOptions = {
    screen: TodosScreen,
    navigationOptions: commonNavigationOptions,
};

// différentes routes pour tous, actifs et complétés todos
const TabNav = TabNavigator(
    {
        [CONSTANTS.ALL]: routeOptions,
        [CONSTANTS.ACTIVE]: routeOptions,
        [CONSTANTS.COMPLETED]: routeOptions,
    },
    {
        navigationOptions: ({ navigation }) => ({
            // cela nous indique quelle icône rendre sur les onglets
            tabBarIcon: ({ focused }) => {
                const { routeName } = navigation.state;
                let iconName;
                switch (routeName) {
                    case CONSTANTS.ALL:
                        iconName = 'format-list-bulleted';
                        break;
                    case CONSTANTS.ACTIVE:
                        iconName = 'filter-center-focus';
                        break;
                    case CONSTANTS.COMPLETED:
                        iconName = 'playlist-add-check';
                }
                return (
                    <MaterialIcons
                        name={iconName}
                        size={28}
                        style={{ marginBottom: -3 }}
                        color={focused ? Colors.tabIconSelected : Colors.tabIconDefault}
                    />
                );
            },
        }),
        // pour rendre les onglets en bas
        tabBarComponent: TabBarBottom,
        tabBarPosition: 'bottom',
        animationEnabled: true,
        swipeEnabled: true,
    },
);

export default TabNav;
```

* La fonction `TabNavigator` accepte deux arguments, le premier étant les configurations de route et le second étant les configurations `TabNavigator`. Dans l'extrait ci-dessus, nous passons les configurations pour afficher une barre de navigation par onglets en bas et définissons différentes icônes pour chaque onglet.

#### 2. TodosScreen et TodosContainer

Le composant `TodosScreen` dans `screens/TodosScreen.js` enveloppe notre composant principal `TodosContainer` dans `components/TodosContainer.js` où nous ajouterons divers composants pour l'application. Le `TodosContainer` affichera les données filtrées, en fonction de l'onglet sur lequel nous nous trouvons : **Tous**, **Actifs** ou **Complétés**.

#### 3. APIs pour Créer, Mettre à jour et Supprimer des todos

Les APIs pour les opérations CUD sur Elasticsearch sont présentes dans `api/todos.js`. Il contient trois méthodes simples `add`, `update` et `destroy` qui fonctionnent avec n'importe quel index Elasticsearch tel que spécifié dans `constants/Config.js`. Un point important à garder à l'esprit est que chaque élément todo que nous créons aura un champ `_id` unique. Nous pouvons utiliser ce champ `_id` pour mettre à jour ou supprimer un todo existant.

Pour notre application, nous aurons juste besoin de trois méthodes pour ajouter, créer ou supprimer des todos. Cependant, vous pouvez trouver une explication détaillée sur les méthodes API à la [docs](http://docs.appbase.io/javascript/api-reference.html).

### Construction des composants et de l'UI ?

Commençons par ajouter quelques composants pour compléter la fonctionnalité de l'application.

#### 1. Ajout de Todos

Nous utiliserons `[Fab](https://docs.nativebase.io/Components.html#fabs-def-headref)` de `[native-base](http://docs.nativebase.io/)` pour rendre un bouton flottant pour ajouter des todos.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C1-bdZSvCajaJ-dtSsWcjg.png)

```js
const AddTodoButton = ({ onPress }) => (
  <Fab
      direction="up"
      containerStyle={{}}
      style={{ backgroundColor: COLORS.primary }}
      position="bottomRight"
      onPress={onPress}
  >
      <Icon name="add" />
  </Fab>
);
```

Vous pouvez maintenant utiliser ce composant dans `components/TodosContainer.js`.

```javascript
import AddTodoButton from './AddTodoButton';
...
export default class TodosContainer extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        ...
        <AddTodoButton />
      </View>
    );
  }
}
```

Une fois que nous avons ajouté le bouton, nous verrons quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vWdtqKsk0gZzMC4UO35IGg.png)
_Après avoir ajouté le AddTodoButton_

Maintenant, lorsque quelqu'un clique sur ce bouton, nous devons afficher l'entrée pour ajouter un todo. Ajoutons le code pour cela dans `components/AddTodo.js`.

```js
class AddTodo extends Component {
  constructor(props) {
    super(props);
    const { title, completed, createdAt } = this.props.todo;
    this.state = {
      title,
      completed,
      createdAt,
    };
  }

  onSubmit = () => {
    if (this.state.title.length > 0) this.props.onAdd(this.state);
    return null;
  };

  setStateUtil = (property, value = undefined) => {
    this.setState({
      [property]: value,
    });
  };

  render() {
    const { title, completed } = this.state;
    const { onBlur } = this.props;
    return (
      <View
        style={{
          flex: 1,
          width: '100%',
          flexDirection: 'row',
          alignItems: 'center',
          paddingRight: 10,
          paddingBottom: 5,
          paddingTop: 5,
        }}
      >
        <CheckBox checked={completed} onPress={() => this.setStateUtil('completed', !completed)} />
        <Body
          style={{
            flex: 1,
            justifyContent: 'flex-start',
            alignItems: 'flex-start',
            paddingLeft: 25,
          }}
        >
          <TextInput
            style={{ width: '90%' }}
            placeholder="Qu'est-ce qui doit être fait ?"
            autoFocus
            underLineColorAndroid="transparent"
            underlineColor="transparent"
            blurOnSubmit
            onSubmitEditing={this.onSubmit}
            onChangeText={changedTitle => this.setStateUtil('title', changedTitle)}
            value={title}
            autoCorrect={false}
            autoCapitalize="none"
            onBlur={onBlur}
          />
        </Body>
        <TouchableOpacity
          onPress={() => this.props.onCancelDelete}
          style={{ paddingLeft: 25, paddingRight: 15 }}
        >
          <Ionicons
            name="ios-trash-outline"
            color={`${title.length > 0 ? 'black' : 'grey'}`}
            size={23}
          />
        </TouchableOpacity>
      </View>
    );
  }
}
```



Les principaux composants utilisés ici sont `[TextInput](https://facebook.github.io/react-native/docs/textinput.html)`, `[Checkbox](http://docs.nativebase.io/Components.html#checkbox-headref)` et `[Ionicons](https://expo.github.io/vector-icons/)` avec des props simples. Nous utilisons `title` et `completed` depuis le `state`. Nous allons passer les props `todo`, `onAdd`, `onCancelDelete` et `onBlur` depuis `components/TodosContainer.js`. Ceux-ci nous aideront à ajouter de nouveaux todos ou à réinitialiser la vue si vous souhaitez annuler l'ajout de todos.

Maintenant, nous pouvons mettre à jour `components/TodosContainer.js` avec les modifications nécessaires pour rendre le composant `AddTodo` :

```js
...
import AddTodoButton from './AddTodoButton';
import AddTodo from './AddTodo';
import TodoModel from '../api/todos';
...

// affichera les todos en fonction de l'écran actif : tous, actifs ou complétés
export default class TodosContainer extends React.Component {
  state = {
    addingTodo: false,
  };

  componentDidMount() {
    // inclut les méthodes pour la création, la mise à jour et la suppression
    this.api = new TodoModel('react-todos');
  }

  render() {
    return (
      <View style={styles.container}>
        <Header />
        <StatusBar backgroundColor={COLORS.primary} barStyle="light-content" />
        <ScrollView>
          {this.state.addingTodo ? (
            <View style={styles.row}>
              <AddTodo
                onAdd={(todo) => {
                  this.setState({ addingTodo: false });
                  this.api.add(todo);
                }}
                onCancelDelete={() => this.setState({ addingTodo: false })}
                onBlur={() => this.setState({ addingTodo: false })}
              />
            </View>
          ) : null}
        </ScrollView>
        <AddTodoButton onPress={() => this.setState({ addingTodo: true })} />
      </View>
    );
  }
}
```

Le composant `AddTodo` est rendu à l'intérieur d'un composant `[ScrollView](https://facebook.github.io/react-native/docs/scrollview.html)`. Nous passons également une prop `onPress` à `AddTodoButton` pour basculer l'état et afficher conditionnellement le composant `AddTodo` en fonction de `this.state.addingTodo`. La prop `onAdd` passée à `AddTodo` crée également un nouveau todo en utilisant l'API `add` dans `api/todos.js`.

Après avoir cliqué sur le bouton d'ajout, nous verrons l'entrée pour ajouter un todo comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VrlfuWW4tdj0TTrGjSfDSw.png)
_Ajout d'un todo_

#### 2. Affichage des Todos

Après avoir terminé l'ajout d'un todo, il est ajouté dans Elasticsearch (que nous avons configuré dans `constants/Config.js`). Toutes ces données peuvent être vues en temps réel en utilisant les composants [ReactiveSearch Native](https://github.com/appbaseio/reactivesearch/tree/dev/packages/native).

Il y a plus de 10 composants [UI natifs](https://opensource.appbase.io/reactive-manual/native/getting-started/componentsindex.html) que la bibliothèque fournit. Pour notre application de todo, nous utiliserons principalement le composant [ReactiveList](https://opensource.appbase.io/reactive-manual/native/components/reactivelist.html) pour afficher l'état des todos.

Ajoutons le composant `ReactiveList` et affichons nos todos. Nous ajouterons ce composant dans `components/TodosContainer.js` et les méthodes nécessaires pour qu'il fonctionne. Voici comment `ReactiveList` sera utilisé :

```js

...
import { ReactiveList } from '@appbaseio/reactivesearch-native';
...

export default class TodosContainer extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <Header />
        <StatusBar backgroundColor={COLORS.primary} barStyle="light-content" />
        <ScrollView>
          <ReactiveList
            componentId="ReactiveList"
            defaultQuery={() => ({
              query: {
                match_all: {},
              },
            })}
            stream
            onAllData={this.onAllData}
            dataField="title"
            showResultStats={false}
            pagination={false}
          />
          ...
        </ScrollView>
        <AddTodoButton onPress={() => this.setState({ addingTodo: true })} />
      </View>
    );
  }
}
```

Nous n'avons pas encore ajouté la méthode `onAllData`, mais comprenons un peu les props que nous avons utilisées ici :

* `componentId` — identifiant unique pour le composant.
* `defaultQuery` : la requête à appliquer initialement pour la liste. Nous utiliserons `match_all` pour afficher tous les todos par défaut.
* `stream` : si on doit diffuser les nouvelles mises à jour des résultats ou simplement afficher les résultats historiques. En définissant cela sur `true`, nous écoutons également les mises à jour en direct des todos. Nous ajouterons la logique liée au streaming plus tard.
* `onAllData` — une fonction de rappel qui reçoit la liste des éléments todo actuels et le streaming (nouveaux todos et toute mise à jour) et retourne un composant React ou JSX à rendre. Voici à quoi ressemble la syntaxe :

```js
<ReactiveList
  onAllData(todos, streamData) {
    // retourner la liste à rendre
  }
  ...
/>
```

Vous pouvez lire plus sur toutes ces props en détail sur la page [docs](https://opensource.appbase.io/reactive-manual/result-components/reactivelist.html) de ReactiveList.

Pour voir quelque chose, nous devons retourner un JSX ou un composant React depuis le callback `onAllData`. Pour cela, nous utiliserons [FlatList](https://facebook.github.io/react-native/docs/flatlist.html) de React Native qui est composé de composants [Text](https://facebook.github.io/react-native/docs/text.html). Dans l'étape suivante, nous ajouterons notre composant personnalisé `TodoItem`.

```js
...
import { ScrollView, StyleSheet, StatusBar, FlatList, Text } from 'react-native';
import CONSTANTS from '../constants';
...

export default class TodosContainer extends React.Component {
  ...
  onAllData = (todos, streamData) => {
    // filtrer les données en fonction de "screen": [All | Active | Completed]
    const filteredData = this.filterTodosData(todos);

    return (
      <FlatList
        style={{ width: '100%', top: 15 }}
        data={filteredData}
        keyExtractor={item => item._id}
        renderItem={({ item: todo }) => (
            <Text>{todo.title}</Text>
        )}
      />
    );
  };

  filterTodosData = (todosData) => {
    const { screen } = this.props;

    switch (screen) {
      case CONSTANTS.ALL:
        return todosData;
      case CONSTANTS.ACTIVE:
        return todosData.filter(todo => !todo.completed);
      case CONSTANTS.COMPLETED:
        return todosData.filter(todo => todo.completed);
    }

    return todosData;
  };

  render() {
    ...
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kobdkvtn9oZY7qvF9pzK0Q.png)
_Intégration de ReactiveList avec onAllData_

#### 3. Ajout de TodoItem(s)

Ensuite, nous allons créer un composant séparé **TodoItem** pour afficher chaque todo qui contiendra toutes les balises nécessaires pour un élément todo comme [CheckBox](https://docs.nativebase.io/Components.html#checkbox-headref), [Text](https://facebook.github.io/react-native/docs/text.html), et une icône de suppression [Icon](https://docs.nativebase.io/Components.html#icon-def-headref). Cela va dans `components/TodoItem.js` :

```js
class TodoItem extends Component {
  onTodoItemToggle = (todo, propAction) => {
    propAction({
      ...todo,
      completed: !todo.completed,
    });
  };

  render() {
    const { todo, onUpdate, onDelete } = this.props;

    return (
      <View style={styles.row}>
        <View
          style={{
            flex: 1,
            width: '100%',
            flexDirection: 'row',
            alignItems: 'center',
            paddingRight: 10,
            paddingVertical: 5,
          }}
        >
          <TouchableOpacity
            onPress={() => this.onTodoItemToggle(todo, onUpdate)}
            style={{
              flex: 1,
              width: '100%',
              flexDirection: 'row',
            }}
          >
            <CheckBox
              checked={todo.completed}
              onPress={() => this.onTodoItemToggle(todo, onUpdate)}
            />
            <Body
              style={{
                flex: 1,
                justifyContent: 'flex-start',
                alignItems: 'flex-start',
                paddingLeft: 25,
              }}
            >
              <Text
                style={{
                  color: todo.completed ? 'grey' : 'black',
                  textDecorationLine: todo.completed ? 'line-through' : 'none',
                }}
              >
                {todo.title}
              </Text>
            </Body>
          </TouchableOpacity>
          <TouchableOpacity
            onPress={() => onDelete(todo)}
            style={{ paddingLeft: 25, paddingRight: 15 }}
          >
            <Ionicons
              name="ios-trash-outline"
              color={`${todo.title.length > 0 ? 'black' : 'grey'}`}
              size={23}
            />
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}
```

Ce composant reçoit le `todo` de ses props ainsi que `onDelete` et `onUpdate` qui sont utilisés pour mettre à jour et supprimer l'élément todo respectivement. Nous utilisons ceux-ci aux endroits nécessaires en utilisant la prop `onPress` des composants que nous utilisons.

Ensuite, nous pouvons `importer` et utiliser le composant `TodoItem` dans notre `onAllData` dans `components/TodosContainer.js`. Nous passerons le `todo` en tant que prop ainsi que les méthodes API pour `update` et `destroy` qui seront utilisées par le composant `TodoItem`.

```js
class TodosContainer extends Component {
  ...
  onAllData = (todos, streamData) => {
    ...
    return (
      <FlatList
        ...
        renderItem={({ item: todo }) => (
          <TodoItem 
            todo={todo}
            onUpdate={this.api.update} 
            onDelete={this.api.destroy}
          />
        )}
      />
    );
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*46QMtTpPsof09oOBwvrELA.png)
_Après avoir ajouté TodoItem dans TodosContainer_

#### 4. Diffusion des mises à jour des données

Vous avez peut-être remarqué que les todos s'affichent correctement, sauf que vous ne pouvez pas voir les todos mis à jour sans rafraîchir l'application. Dans cette dernière étape, nous allons combler cette partie manquante du puzzle.

Dans la section précédente, nous avons ajouté une méthode `onAllData` pour le composant `ReactiveList`. Le deuxième paramètre de `onAllData` reçoit les mises à jour de streaming que nous allons utiliser pour toujours garder les todos à jour. Voici à quoi ressemblera la méthode `onAllData` mise à jour dans `components/TodosContainer.js`.

```js
import Utils from '../utils';
...

export default class TodosContainer extends React.Component {
  ...
  onAllData = (todos, streamData) => {
    // fusionner les données de streaming des todos avec les todos actuels
    const todosData = Utils.mergeTodos(todos, streamData);

    // filtrer les données en fonction de "screen": [All | Active | Completed]
    const filteredData = this.filterTodosData(todosData);

    return (
      <FlatList
        style={{ width: '100%', top: 15 }}
        data={filteredData}
        keyExtractor={item => item._id}
        renderItem={({ item: todo }) => (
            <TodoItem todo={todo} onUpdate={this.api.update} onDelete={this.api.destroy} />
        )}
      />
    );
  };
  ...
}
```

La méthode `mergeTodos` est présente dans `utils/index.js`. Voici comment elle fonctionne :

```js
class Utils {
  static mergeTodos(todos, streamData) {
    // générer un tableau d'ids de streamData
    const streamDataIds = streamData.map(todo => todo._id);

    return (
      todos
        // considérer streamData comme la source de vérité
        // d'abord prendre les todos existants qui ne sont pas présents dans stream data
        .filter(({ _id }) => !streamDataIds.includes(_id))
        // puis ajouter les todos de stream data
        .concat(streamData)
        // supprimer les todos qui sont supprimés dans stream data
        .filter(todo => !todo._deleted)
        // enfin trier sur la base du timestamp de création
        .sort((a, b) => a.createdAt - b.createdAt)
    );
  }
}

export default Utils;
```

Le `streamData` reçoit un tableau d'objets todo lorsqu'ils sont créés, supprimés ou mis à jour. Si un objet est mis à jour, il contient une clé `_updated` définie sur `true`. De même, si un objet est supprimé, il contient une clé `_deleted` définie sur `true`. Si un objet est créé, il ne contient aucune des deux. En utilisant ces points, nous avons ajouté la fonction `mergeTodos`.

Avec cela, vous devriez être en mesure de voir les modifications des éléments todo en temps réel ! Si vous avez un appareil/émulateur supplémentaire exécutant la même application, les deux diffuseront également les nouvelles mises à jour. ?

### Liens utiles

1. Application Todos [démo](https://snack.expo.io/@dhruvdutt/todo), [lien expo](https://expo.io/@dhruvdutt/todos), [projet de départ](https://github.com/appbaseio-apps/todos-native/tree/base) et [code source final](https://github.com/appbaseio-apps/todos-native)
2. [Dépôt GitHub ReactiveSearch](https://github.com/appbaseio/reactivesearch) ⭐
3. ReactiveSearch [docs](https://opensource.appbase.io/reactive-manual/native)

J'espère que vous avez apprécié cet article. Si vous avez des pensées ou des suggestions, faites-le moi savoir et amusez-vous !

---

Vous pouvez me suivre sur [twitter](https://twitter.com/divyanshu013) pour les dernières mises à jour. J'ai également commencé à publier des articles plus récents sur mon blog personnel [blog](https://divyanshu013.dev/).

_Merci spécial_ à [Dhruvdutt Jadhav](https://www.freecodecamp.org/news/how-to-build-a-real-time-todo-app-with-react-native-19a1ce15b0b3/undefined) pour m'avoir aidé avec cet article et l'application Todos.