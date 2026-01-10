---
title: 'Modèle React : Extraire les composants enfants pour éviter la liaison'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-04T13:55:44.000Z'
originalURL: https://freecodecamp.org/news/react-pattern-extract-child-components-to-avoid-binding-e3ad8310725e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zISOb74W7PriWKX0y7biKg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Modèle React : Extraire les composants enfants pour éviter la liaison'
seo_desc: 'By Cory House

  Here’s a common scenario in React: You’re mapping over an array, and you need each
  item to call a click handler and pass some relevant data.

  Here’s an example. I’m iterating over a list of users and passing the userId to
  delete to the d...'
---

Par Cory House

Voici un scénario courant dans React : vous parcourez un tableau et vous avez besoin que chaque élément appelle un gestionnaire de clic et transmette certaines données pertinentes.

Voici un exemple. Je parcours une liste d'utilisateurs et je transmets l'userId à supprimer à la fonction deleteUser à la ligne 31.

```js
import React from 'react';

class App extends React.Component {
  constructor() {
    this.state = {
      users: [
        { id: 1, name: 'Cory' }, 
        { id: 2, name: 'Meg' }
      ]
    };
  }
  
  deleteUser = id => {
    this.setState(prevState => {
      return { users: prevState.users.filter( user => user.id !== id)}
    })
  }

  render() {
    return (
      <div>
        <h1>Utilisateurs</h1>
        <ul>
        { 
          this.state.users.map( user => {
            return (
              <li key={user.id}>
                <input 
                  type="button" 
                  value="Supprimer" 
                  onClick={() => this.deleteUser(user.id)} 
                /> 
                {user.name}
              </li>
            )
          })
        }
        </ul>
      </div>
    );
  }
}

export default App;
```

Voici un [exemple fonctionnel sur Codesandbox](https://codesandbox.io/s/0OP2Yq87). (qui est génial ?)

### Quel est le problème ?

J'utilise une fonction fléchée dans le gestionnaire de clic. Cela signifie **qu'à chaque exécution de render, une nouvelle fonction est allouée**. Dans de nombreux cas, ce n'est pas un gros problème. Mais si vous avez des composants enfants, ils se re-rendront même lorsque les données n'ont pas changé parce que chaque rendu alloue une nouvelle fonction.

**En résumé** : Évitez de déclarer des fonctions fléchées ou de lier dans render pour des performances optimales. Mon équipe utilise [cette règle ESLint](https://github.com/yannickcr/eslint-plugin-react/blob/master/docs/rules/jsx-no-bind.md) pour nous aider à détecter ce problème.

### Quelle est la solution ?

Alors, comment éviter la liaison et les fonctions fléchées dans render ? Une option est d'extraire un composant enfant. Ici, j'ai extrait l'élément de liste dans UserListItem.js :

```js
import React from 'react';
import PropTypes from 'prop-types';

class UserListItem extends React.Component {
  onDeleteClick = () => {
    // Pas besoin de bind puisque nous pouvons composer
    // les données pertinentes pour cet élément ici
    this.props.onClick(this.props.user.id);
  }

  // Pas de fonction fléchée dans render ! ?
  render() {
    return (
      <li>
        <input 
          type="button" 
          value="Supprimer" 
          onClick={this.onDeleteClick} 
        /> 
        {this.props.user.name}
      </li>
    );
  }
}

UserListItem.propTypes = {
  user: PropTypes.object.isRequired,
  onClick: PropTypes.func.isRequired
};

export default UserListItem;
```

Ensuite, le rendu du composant parent devient plus simple et n'a plus besoin de contenir une fonction fléchée. Il transmet le contexte pertinent pour chaque élément de liste via les props dans la nouvelle fonction "renderUserListItem".

```js
import React from 'react';
import { render } from 'react-dom';
import UserListItem from './UserListItem';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [{ id: 1, name: 'Cory' }, { id: 2, name: 'Sherry' }],
    };
  }

  deleteUser = id => {
    this.setState(prevState => {
      return { users: prevState.users.filter(user => user.id !== id) };
    });
  };

  renderUserListItem = user =>
    <UserListItem key={user.id} user={user} onClick={this.deleteUser} />;

  render() {
    return (
      <div>
        <h1>Utilisateurs</h1>
        <ul>
          {this.state.users.map(this.renderUserListItem)}
        </ul>
      </div>
    );
  }
}

render(<App />, document.getElementById('root'));
```

Remarquez qu'au lieu d'utiliser une fonction fléchée dans render lors du mappage, nous appelons une nouvelle fonction déclarée en dehors de render à la ligne 19. Plus d'allocation de fonction à chaque rendu. ?

Voici un [exemple fonctionnel de ce refactoring final](https://codesandbox.io/s/jqQ0AlQlW).

### Top ou Flop ?

Ce modèle améliore les performances en éliminant les allocations de fonctions redondantes. Il est donc particulièrement utile lorsque cette situation s'applique à votre composant :

1. Render est appelé fréquemment.
2. Le rendu des enfants est coûteux.

Admettons-le, extraire un composant enfant comme je l'ai suggéré ci-dessus est également un travail supplémentaire. Cela nécessite plus de pièces mobiles et plus de code. Donc, si vous n'avez pas de problèmes de performance, c'est probablement une optimisation prématurée ?.

Vous avez donc deux options : soit autoriser les fonctions fléchées et les liaisons partout (et traiter les problèmes de performance s'ils surviennent), soit les interdire pour des performances et une cohérence optimales.

**En résumé** : Je recommande d'interdire les fonctions fléchées et les liaisons dans render. Voici pourquoi :

1. Vous devez désactiver [la règle ESLint utile](https://github.com/yannickcr/eslint-plugin-react/blob/master/docs/rules/jsx-no-bind.md) que j'ai suggérée ci-dessus pour l'autoriser.
2. Une fois que vous désactivez une règle de linting, les gens sont susceptibles de copier ce modèle et de commencer à désactiver d'autres règles de linting. Une exception à un endroit peut rapidement devenir la norme...

%[https://twitter.com/housecor/status/839511073279598594?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E839511073279598594%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fhousecor%2Fstatus%2F839511073279598594%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F650743198348808192%25252FLT6SeOJr_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Je trouve donc que l'extraction des composants enfants est un modèle utile pour éviter la liaison dans render.

Avez-vous une autre façon de gérer cela que vous préférez ? Faites-le nous savoir via les commentaires !

### Vous cherchez plus d'informations sur React ? 

J'ai écrit [plusieurs cours sur React et JavaScript](http://bit.ly/psauthorpageimmutablepost) sur Pluralsight ([essai gratuit](http://bit.ly/pstrialimmutablepost)). Mon dernier cours, [Création de composants React réutilisables](http://bit.ly/psreactcomponentsimmutablepost), vient de paraître ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), architecte logiciel chez VinSolutions, MVP Microsoft, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).