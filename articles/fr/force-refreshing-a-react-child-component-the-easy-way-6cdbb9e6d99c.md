---
title: 'Comment forcer le rafraîchissement d''un composant enfant React : la méthode
  facile'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T16:26:31.000Z'
originalURL: https://freecodecamp.org/news/force-refreshing-a-react-child-component-the-easy-way-6cdbb9e6d99c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5GipOUpmtMBQf3pOTcJ1YQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: 'Comment forcer le rafraîchissement d''un composant enfant React : la méthode
  facile'
seo_desc: 'By Amber Wilkie

  Note: As of React 16, componentWillReceiveProps() is deprecated, meaning if you
  are using that version or higher in your project, this is not good advice for you.

  In the React world, forcing a re-render is frowned upon. You should let...'
---

Par Amber Wilkie

**Note : À partir de React 16, `componentWillReceiveProps()` est obsolète, ce qui signifie que si vous utilisez cette version ou une version supérieure dans votre projet, ce conseil n'est pas adapté pour vous.**

Dans le monde React, forcer un re-rendu est mal vu. Vous devriez laisser le DOM se gérer lui-même lorsque React perçoit des changements dans `state` ou `props`. Pour suivre ces modèles, nous devons parfois faire des choses qui semblent un peu ridicules. Considérez ce scénario :

![Image](https://cdn-media-1.freecodecamp.org/images/SPU87A7KxxBLyug8JI0ZKYNqZH84EGfvO78o)
_Exemple simple et ridicule d'un composant enfant qui gère son propre état_

Nous avons deux composants — un parent et un enfant. Le parent fait un appel API pour récupérer l'`user`. À partir de cela, nous obtenons des choses comme `name`, `age`, `favorite color`. Nous obtenons également un `id` de notre base de données. Nous allons passer cela à notre composant enfant, qui va également faire un appel API, avec l'id de l'utilisateur. Super — beaucoup de données arrivent dans notre application.

Disons que nous stockons une liste de chaussures dans la base de données. Lorsque l'utilisateur change sa préférence de couleur, le serveur écrit de nouvelles données dans la liste de chaussures de l'utilisateur. Super ! Sauf que nous ne voyons pas la nouvelle liste de chaussures dans notre composant enfant. Qu'est-ce qui se passe ?

**Note de côté** : Bien sûr, nous devrions simplement obtenir les chaussures à partir de l'appel pour l'utilisateur — ceci n'est qu'une explication simplifiée.

### Les bases du re-rendu React

En bref, React ne mettra à jour que les parties du DOM qui ont changé. Dans ce cas, les `props` que nous passons au composant de chaussures (`userId`) n'ont pas changé, donc rien ne change dans notre composant enfant.

La préférence de couleur de l'utilisateur sera mise à jour lorsque nous recevrons de nouvelles informations de l'API — en supposant que nous faisons quelque chose avec la réponse après avoir mis à jour un utilisateur.

Mais comme React ne voit aucune raison de mettre à jour la liste de chaussures, il ne le fera pas — même si sur notre serveur, les chaussures sont maintenant différentes.

### Le code de départ

```jsx
const UserShow extends Component {
  state = {
    user: {}
  }
  
  componentDidMount() {
    this.fetchUser().then(this.refreshUser)
  }
  
  setNewColor = color => {
    this.updateUser({color}).then(this.refreshUser)
  }
  
  refreshUser = res => this.setState({user: res.data.user})
  
  render() {
    const { user } = this.state;
    
    return (
      <div>
        User name: {user.name}
        Pick color: 
        <div>
          {colors.map(color => 
            <div className={color} 
                 onClick={() => this.setNewColor(color)} />)}
          )}
        </div>
        <ShoeList id={user.id} />
      </div>
    )
  }
}
```

Notre `ShoeList` va simplement être une liste de chaussures, que nous allons récupérer du serveur avec l'id de l'utilisateur :

```jsx
const ShoeList extends Component {
  state = {
    shoes: []
  }
  
  componentDidMount() {
    this.fetchShoes(this.props.id)
        .then(this.refreshShoeList)
  }

  refreshShoeList = res => this.setState({ shoes: res.data.shoes })
  
  render() {
    // une liste de chaussures
  }
}
```

Si nous voulons que le composant de chaussures récupère la nouvelle liste de chaussures, nous devons mettre à jour les props que nous lui envoyons. Sinon, il ne verra aucune raison de se rafraîchir.

En fait, de la manière dont cela est écrit, le `ShoeList` ne se rafraîchirait jamais, car nous ne dépendons pas des props pour le rendu. Corrigons cela.

### Déclencher un composant enfant pour qu'il se re-render

Pour forcer le composant enfant à se re-render — et à faire un nouvel appel API — nous devrons passer une prop qui changera si la préférence de couleur de l'utilisateur a changé.

Pour ce faire, nous allons ajouter une méthode dans `setNewColor` :

```jsx
[...]

setNewColor = color => {
  this.updateUser({color}).then(res => {
    this.refreshUser(res);
    this.refreshShoeList();
  })
}

refreshShoeList = () => 
  this.setState({refreshShoeList: !this.state.refreshShoeList})
  
[...]

<ShoeList id={user.id} refresh={refreshShoeList}
```

C'est un simple interrupteur que nous pouvons basculer. J'ai gardé les choses aussi simples que possible, mais en production, nous voudrions nous assurer que la couleur que nous définissons est différente de la couleur que nous avions auparavant. Sinon, il n'y aura rien à mettre à jour.

Maintenant dans le `ShoeList` :

```jsx
componentWillReceiveProps(props) {
  const { refresh, id } = this.props;
  if (props.refresh !== refresh) {
    this.fetchShoes(id)
      .then(this.refreshShoeList)
  }
}
```

Si vous passez uniquement `refreshShoeList` et que vous basculez en fonction de ce booléen, le composant se mettra simplement à jour pour toujours.

Nous devons nous assurer que l'interrupteur n'a basculé qu'une seule fois — donc nous allons simplement vérifier que les props entrantes sont différentes des props que nous avions auparavant. Si elles sont différentes, nous ferons un nouvel appel API pour obtenir la nouvelle liste de chaussures.

Et boom — notre composant enfant a été "forcé" à se mettre à jour.

#### componentWillReceiveProps

Il vaut la peine de prendre encore une minute pour examiner ce qui se passe dans ce dernier morceau de code. Dans `componentWillReceiveProps`, nous avons notre seule opportunité de voir les nouvelles props lorsqu'elles arrivent et de les comparer avec les props précédentes.

Ici, nous pouvons détecter les changements (comme dans `refresh`) et nous pouvons également faire des vérifications pour de nouvelles props (notons, par exemple, que `refresh` est initialement `undefined`).

Cette méthode React est un moyen très puissant de manipuler et d'examiner les `props`.