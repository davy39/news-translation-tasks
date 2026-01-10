---
title: Ré-afficher un composant React lorsque ses props changent
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:13:00.000Z'
originalURL: https://freecodecamp.org/news/re-render-react-component-when-its-props-changes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aaa740569d1a4ca26f9.jpg
tags:
- name: components
  slug: components
- name: React
  slug: react
- name: Render Props
  slug: render-props
- name: toothbrush
  slug: toothbrush
seo_title: Ré-afficher un composant React lorsque ses props changent
seo_desc: 'Imagine you have a React and Redux project with two components, a parent
  and a child.

  The parent component passes some props to the child component. When the child component
  receives those props, it should call some Redux action which changes some of...'
---

Imaginez que vous avez un projet React et Redux avec deux composants, un parent et un enfant.

Le composant parent passe certaines props au composant enfant. Lorsque le composant enfant reçoit ces props, il doit appeler une action Redux qui modifie certaines des props qui ont été passées par le parent de manière asynchrone.

Voici les deux composants :

### Composant Parent

```jsx
class Parent extends React.Component {
  getChilds(){
    let child = [];
    let i = 0;
    for (let keys in this.props.home.data) {
      child[i] = (
        <Child title={keys} data={this.props.home.data[keys]} key={keys} />
      );
      i++;
      if (i === 6) break;
    }

    return Rows;
  }
  render(){
return (
  <div>
     <h1>Je vais appeler mon enfant </h1>
    {this.getChilds()}
 </div>
)
```

### Composant Enfant

```jsx
class Child extends React.Component {
 componentDidMount(){
  if(this.props.data.items.length === 0){
    // appel d'une action pour remplir le tableau this.props.data.items avec des données
   this.props.getData(this.props.data.id);
  }
 }
  getGrandSon(){
  let grandSons = [];
  if(this.props.data.items.length > 0){
   grandSons = this.props.data.items.map( item => <GrandSon item={item} />);
  }
  return grandSons;
 }
  render(){
    return (
      <div>
       <h1> Je suis le composant enfant et je vais appeler mon propre enfant </h1>
      {this.getGrandSon()}
    </div>
     )
 }
}
```

Le `redux-store` est mis à jour correctement, mais le composant enfant ne se ré-affiche pas.

Normalement, ce n'est pas la responsabilité de l'`Enfant` de remplir les données. Au lieu de cela, il devrait recevoir des données qui ont déjà été préparées par le `Parent`. De plus, les props sont automatiquement mises à jour.

Cependant, il peut être utile de mettre à jour et de manipuler des données à partir d'un composant `Enfant`, surtout lorsque Redux est impliqué.

React effectue probablement des comparaisons superficielle, et pourrait ne pas ré-afficher même si l'état change clairement.

En tant que solution de contournement, vous pouvez faire ceci dans `mapStateToProps` :

```jsx
const mapStateToProps = state => {
  return { 
    id: state.data.id,
   items: state.data.items
  }
}
```