---
title: Comment créer une FlatList React Native avec une capacité de recherche en temps
  réel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-21T19:10:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-react-native-flatlist-with-realtime-searching-ability-81ad100f6699
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3ogqzQjYCBUi_y1WYGLxtA.png
tags:
- name: flatlist
  slug: flatlist
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: technology
  slug: technology
seo_title: Comment créer une FlatList React Native avec une capacité de recherche
  en temps réel
seo_desc: 'By Vikrant Negi

  If you have ever used a mobile app or build one, then you must have come across
  some kind of list — whether it was a long list of contacts, products, countries,
  or other things.

  They may seem very simple to an end user. But for develo...'
---

Par Vikrant Negi

Si vous avez déjà utilisé une application mobile ou en avez construit une, alors vous avez dû rencontrer une sorte de liste — qu'il s'agisse d'une longue liste de contacts, de produits, de pays ou d'autres choses.

Elles peuvent sembler très simples pour un utilisateur final. Mais pour les développeurs, afficher une longue liste de données a toujours été un point douloureux en ce qui concerne les longues listes performantes. Cela est particulièrement vrai dans les applications construites avec React Native.

### Contexte

Durant les premiers jours de React Native, nous avions le bon vieux `[ListView](https://facebook.github.io/react-native/docs/listview)`. Il avait de nombreuses fonctionnalités qui le rendaient très attractif, et c'était un choix par défaut pour afficher efficacement des listes verticales de données changeantes.

Avec le temps, cependant, de nombreux problèmes et bugs sont apparus, et il y a eu un moment où l'équipe React Native a réalisé qu'il était temps de réinventer la roue.

#### Voici FlatList

En mars 2017, Facebook a introduit le composant `[FlatList](https://facebook.github.io/react-native/docs/flatlist)`, qui est une manière plus facile et plus performante d'implémenter des listes simples et performantes. Non seulement cela — son API est plus facile à comprendre que l'original `ListView`. Voici à quoi ressemble une simple FlatList :

```
<FlatList   data={[{title: 'Titre du texte', key: 'item1'}, ]}   renderItem={({item}) => <ListItem title={item.title} />} />
```

En plus de `FlatList`, vous pouvez également utiliser [`SectionList`](https://facebook.github.io/react-native/docs/sectionlist) pour rendre des listes sectionnées.

#### Qu'est-ce qui suit

Comme je l'ai mentionné précédemment, ListView était principalement utilisé pour afficher de longues listes de données verticales changeantes. Mais de longues listes de données sont aussi utiles qu'un marteau sans manche. 💡

Presque tout le temps, chaque fois que vous rencontrez une longue liste de données, vous avez également la possibilité de rechercher dans ces données afin de ne pas vous perdre dans la recherche.

![Image](https://cdn-media-1.freecodecamp.org/images/tRc29TnV5CmgAoO8moaZ79moeGeTUVTbBdj9)
_Liste des pays WhatsApp avec recherche_

### React Native Searchable FlatList

J'ai décidé de construire quelque chose pour résoudre ce problème. Vous pouvez trouver le dépôt complet du projet [ici](https://github.com/vikrantnegi/react-native-searchable-flatlist).

Si vous n'êtes pas familier avec FlatList, je vous recommande de passer par les bases de FlatList d'abord. [Cet article](https://medium.com/react-native-development/how-to-use-the-flatlist-component-react-native-basics-92c482816fe6) de Spencer Carli est le meilleur pour les débutants qui sont nouveaux dans React Native.

Et maintenant, sans plus attendre, commençons et créons notre FlatList recherchable !

Tout d'abord, définissons quelques états initiaux que nous allons utiliser plus tard dans le projet :

```
this.state = {
  loading: false,      
  data: [],      
  error: null,    
};
```

Nous aurons également besoin d'une variable de tableau :

```
this.arrayholder = [];
```

Apparemment, une liste vide n'est pas amusante. Alors, ajoutons-y une liste aléatoire d'utilisateurs.

Nous allons utiliser [randomuser.me](https://randomuser.me/) qui est une API gratuite et [open-source](https://github.com/RandomAPI/Randomuser.me-Node) pour générer des données d'utilisateurs aléatoires. C'est comme Lorem Ipsum, mais pour les personnes.

Créons une fonction qui va chercher des données d'utilisateurs pour nous.

```
makeRemoteRequest = () => {    
  const url = `https://randomuser.me/api/?&results=20`;
  this.setState({ loading: true });
  
  fetch(url)      
    .then(res => res.json())      
    .then(res => {        
      this.setState({          
        data: res.results,          
        error: res.error || null,          
        loading: false,        
      });        
      
     this.arrayholder = res.results;      
   })      
   .catch(error => {        
     this.setState({ error, loading: false });      
   });  
};
```

Dans l'extrait de code ci-dessus, nous utilisons l'API `[fetch](https://facebook.github.io/react-native/docs/network)` pour faire une requête API à distance. Lorsque la requête est terminée, nous recevons les données utilisateur qui sont sauvegardées dans l'état `data` et également dans notre `arrayholder`.

Maintenant, pour que l'utilisateur puisse rechercher dans la liste, nous devons ajouter une barre de recherche en haut de la `FlatList`. `FlatList` a une prop pour ajouter n'importe quel composant personnalisé à son en-tête, ce qui est utile car nous allons ajouter un composant de recherche là.

```
renderHeader = () => {    
  return (      
    <SearchBar        
      placeholder="Tapez ici..."        
      lightTheme        
      round        
      onChangeText={text => this.searchFilterFunction(text)}
      autoCorrect={false}             
    />    
  );  
};
```

Dans la fonction ci-dessus, nous utilisons le composant `SearchBar` de `react-native-elements` comme composant d'en-tête.

Par défaut, il n'y a aucune logique qui filtrera la liste lorsque nous tapons dans le `SearchBar`. Pour cela, nous devons écrire une fonction qui filtrera les résultats lorsque le texte dans le `SearchBar` change.

```
searchFilterFunction = text => {    
  const newData = this.arrayholder.filter(item => {      
    const itemData = `${item.name.title.toUpperCase()}   
    ${item.name.first.toUpperCase()} ${item.name.last.toUpperCase()}`;
    
     const textData = text.toUpperCase();
      
     return itemData.indexOf(textData) > -1;    
  });
  
  this.setState({ data: newData });  
};
```

La fonction ci-dessus exécutera la fonction de filtrage sur le `arrayholder`. Nous allons filtrer les utilisateurs en fonction de leur nom, donc nous allons stocker le nom dans la variable `itemData` et le convertir en majuscules.

Cette fonction recevra le texte que l'utilisateur tape comme paramètre, que nous allons stocker dans une autre variable `textData` après l'avoir converti en majuscules.

Ensuite, nous allons utiliser `indexOf` pour comparer les deux textes et retourner vrai si le texte est trouvé dans `itemData`. Si un vrai est retourné, alors `filter` conservera ces données, sinon il les ignorera. Ainsi, de nouvelles données sont retournées chaque fois que l'utilisateur tape un texte dans la barre de recherche. Ces nouvelles données sont ensuite définies dans l'état `data`, qui sera finalement utilisé comme source de données pour `FlatList`.

Maintenant, il est temps de rendre la FlatList.

```
<List containerStyle={{ borderTopWidth: 0, borderBottomWidth: 0 }}>
  <FlatList          
    data={this.state.data}          
    renderItem={({ item }) => ( 
      <ListItem              
        roundAvatar              
        title={`${item.name.first} ${item.name.last}`}  
        subtitle={item.email}                           
        avatar={{ uri: item.picture.thumbnail }}   
        containerStyle={{ borderBottomWidth: 0 }} 
       />          
     )}          
     keyExtractor={item => item.email}  
     ItemSeparatorComponent={this.renderSeparator} 
     ListHeaderComponent={this.renderHeader}                             
  />            
</List>
```

C'est tout ce que nous devons faire. Hourra !!

![Image](https://cdn-media-1.freecodecamp.org/images/PFxaKuUElMhRBp1cJh2BMtcWlsuCMXWBd588)
_React native searchable FlatList_

#### Réflexions finales

J'ai sauté un peu de code qui n'est pas si important pour ce tutoriel et pour des raisons de brièveté. Vous pouvez trouver le dépôt complet et fonctionnel [repo](https://github.com/vikrantnegi/react-native-searchable-flatlist) sur GitHub.

De plus, je crois qu'il peut y avoir d'autres moyens d'atteindre le même objectif — donc si vous trouvez une autre méthode, n'hésitez pas à la partager.

Vous pouvez également me suivre sur [Twitter](https://twitter.com/vikrant_negi) et [GitHub](https://github.com/vikrantnegi/). Et consultez mes articles précédents sur [Medium](https://medium.com/@vikrantnegi).

Autres articles utiles :

* [Suivi de localisation React Native](https://medium.com/quick-code/react-native-location-tracking-14ab2c9e2db8)
* [Graphiques React Native avec infobulles dynamiques](https://medium.freecodecamp.org/how-to-build-react-native-charts-with-dynamic-tooltips-64aefc550c95)
* [Graphiques React Native avec infobulles dynamiques](https://medium.freecodecamp.org/how-to-build-react-native-charts-with-dynamic-tooltips-64aefc550c95)