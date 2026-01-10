---
title: Re-Render React Component When Its Props Changes
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
seo_title: null
seo_desc: 'Imagine you have a React and Redux project with two components, a parent
  and a child.

  The parent component passes some props to the child component. When the child component
  receives those props, it should call some Redux action which changes some of...'
---

Imagine you have a React and Redux project with two components, a parent and a child.

The parent component passes some props to the child component. When the child component receives those props, it should call some Redux action which changes some of the props that were passed from the parent asynchronously.

Here are the two components:

### Parent Component

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
     <h1>I am gonna call my child </h1>
    {this.getChilds()}
 </div>
)
```

### Child Component

```jsx
class Child extends React.Component {
 componentDidMount(){
  if(this.props.data.items.length === 0){
    // calling an action to fill this.props.data.items array with data
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
       <h1> I am the child component and I will call my own child </h1>
      {this.getGrandSon()}
    </div>
     )
 }
}
```

The `redux-store` is updated properly, but the child component doesn't re-render.

It's normally not the responsibility of the `Child` to fill the data. Instead, it should receive data that's already been prepared by the `Parent`. Also, props are automatically updated.

Still, it can be useful to update and manipulate data from a `Child` component, especially when Redux is involved.

React is probably performs shallow comparisons, and might not re-render even though the state is clearly changing.

As a workaround, you can do this in `mapStateToProps`:

```jsx
const mapStateToProps = state => {
  return { 
    id: state.data.id,
   items: state.data.items
  }
}
```


