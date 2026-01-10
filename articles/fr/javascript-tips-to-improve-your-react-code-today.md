---
title: 5 conseils JavaScript pour améliorer votre code React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-07-06T15:12:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-tips-to-improve-your-react-code-today
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/5-javascript-tips-to-improve-your-react-code.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
seo_title: 5 conseils JavaScript pour améliorer votre code React
seo_desc: "Let's look at five JavaScript tips you can use today to instantly improve\
  \ your React applications. \nBecause React is a JavaScript library, any improvements\
  \ that we make in our JavaScript skills will directly improve the applications that\
  \ we build wit..."
---

Examinons cinq conseils JavaScript que vous pouvez utiliser dès aujourd'hui pour améliorer instantanément vos applications React. 

Puisque React est une bibliothèque JavaScript, toute amélioration que nous apportons à nos compétences JavaScript améliorera directement les applications que nous construisons avec React.

Pour cette raison, j'ai rassemblé un certain nombre de conseils pour vous montrer comment utiliser les dernières fonctionnalités JavaScript afin de rendre votre code React encore meilleur.

## Comment utiliser l'opérateur de chaînage optionnel en JavaScript

En JavaScript, nous devons d'abord nous assurer qu'un objet existe avant de pouvoir accéder à une propriété de celui-ci. 

Si l'objet a une valeur de `undefined` ou `null`, cela entraînera une erreur de type. 

Dans notre exemple ici, nous avons une application React où les utilisateurs peuvent modifier les publications qu'ils ont faites. 

Seulement si `isPostAuthor` est vrai – ce qui signifie que l'utilisateur authentifié a le même identifiant que l'identifiant de l'auteur de la publication – nous afficherons le composant `EditButton`.

```js
export default function EditButton({ post }) {
  const user = useAuthUser();  
  const isPostAuthor = post.author.userId !== user && user.userId;
    
  return isPostAuthor ? <EditButton /> : null;
}
```

Le problème avec ce code est que notre valeur `user` pourrait être `undefined`. C'est pourquoi nous devons utiliser l'opérateur `&&` pour nous assurer que `user` est un objet avant d'essayer d'obtenir la propriété `userId`. 

Si nous devions accéder à un objet dans un objet, nous devrions inclure une autre condition `&&`. Cela peut rendre notre code fastidieux et difficile à comprendre.

Heureusement, une nouvelle fonctionnalité JavaScript qui nous permet de vérifier si un objet existe avant d'accéder à une propriété sans utiliser la condition finale est l'**opérateur de chaînage optionnel**.

Pour vous assurer qu'un objet existe avant d'essayer d'accéder à une propriété de celui-ci, placez simplement un point d'interrogation immédiatement après :

```js
export default function EditButton({ post }) {
  const user = useAuthUser();  
  const isPostAuthor = post.author.userId !== user?.userId;
    
  return isPostAuthor ? <EditButton /> : null;
}
```

Cela empêchera toute erreur de type et nous permettra d'écrire une logique conditionnelle beaucoup plus propre.

## Comment utiliser le retour implicite avec des parenthèses en JavaScript

Dans les applications React, nous pouvons écrire des composants avec la syntaxe de déclaration de fonction en utilisant le mot-clé `function` ou nous pouvons utiliser une fonction fléchée, qui doit être assignée à une variable. 

Il est important de noter que les composants qui utilisent le mot-clé `function` doivent utiliser le mot-clé `return` avant de retourner du JSX.

```js
export default function App() {
  return (
    <Layout>
      <Routes />
    </Layout>
  );
}
```

Nous pouvons retourner plusieurs lignes de code JavaScript à partir d'une fonction avec un retour implicite (sans utiliser le mot-clé `return`), en enveloppant le code retourné dans une paire de parenthèses.

Pour les composants créés avec des fonctions fléchées, nous n'avons pas à inclure le mot-clé `return` – nous pouvons simplement retourner notre JSX avec une paire de parenthèses.

```js
const App = () => (
  <Layout>
    <Routes />
  </Layout>
);

export default App;
```

De plus, chaque fois que vous itérez sur une liste d'éléments avec la fonction `.map()` de React, vous pouvez également sauter le mot-clé return et retourner votre JSX simplement avec une paire de parenthèses dans le corps de votre fonction interne.

```js
function PostList() {
  const posts = usePostData();  
    
  return posts.map(post => (
    <PostListItem key={post.id} post={post} />  
  ))
}
```

## Comment utiliser l'opérateur de coalescence nulle en JavaScript

En JavaScript, si une certaine valeur est fausse (comme `null`, `undefined`, `0`, `''`, `NaN`), nous pouvons utiliser le conditionnel ou (`||`) pour fournir une valeur de repli. 

Par exemple, si nous avons un composant de page produit et que nous voulons afficher le prix d'un produit donné, vous pouvez utiliser un conditionnel `||` pour afficher soit le prix, soit le texte "Le produit n'est pas disponible". 

```js
export default function ProductPage({ product }) {    
  return (
     <>
       <ProductDetails />
       <span>{product.price || "Le produit n'est pas disponible"} // si le prix est 0, nous verrons "Le produit n'est pas disponible"
     </>
  );
}
```

Cependant, il y a une petite erreur dans notre code existant. 

Si le prix a une valeur de `0`, qui est fausse, au lieu d'afficher le prix lui-même, nous allons afficher le texte "Le produit n'est pas disponible" – ce qui n'est pas ce que nous voulons. 

Nous avons besoin d'un opérateur plus précis pour retourner le côté droit de notre expression uniquement si le côté gauche est `null` ou `undefined` au lieu de toute valeur fausse. 

Cela est maintenant disponible dans l'**opérateur de coalescence nulle**. Il retournera son opérande de droite lorsque son opérande de gauche est `null` ou `undefined`. Sinon, il retournera son opérande de gauche :

```
null ?? 'fallback';
// "fallback"

0 ?? 42;
// 0
```

La façon de corriger notre code ci-dessus est simplement de remplacer le conditionnel ou par l'opérateur de coalescence nulle pour afficher le prix correct de `0`.

```js
export default function ProductPage({ product }) {    
  return (
     <>
       <ProductDetails />
       <span>{product.price ?? "Le produit n'est pas disponible"}
     </>
  );
}
```

## Comment utiliser l'opérateur de propagation d'objet pour mettre à jour l'état en JavaScript

En ce qui concerne l'utilisation de l'état dans React, nous avons quelques options : nous pouvons créer plusieurs variables d'état avec le hook `useState` pour des valeurs primitives individuelles ou gérer plusieurs valeurs dans une seule variable d'état en utilisant un objet. 

Dans l'exemple ci-dessous, nous avons une page d'inscription où nous suivons le nom d'utilisateur, l'e-mail et le mot de passe des utilisateurs actuels. 

Lorsqu'ils soumettent le formulaire d'inscription, nous validons le contenu du formulaire qu'ils ont tapé et nous gérons l'inscription de l'utilisateur. 

```js
import React from 'react'

export default function SignUpPage() {
  const [state, setState] = React.useState({ username: '', email: '', password: '' });
    
  function handleSubmit(event) {   
    event.preventDefault();
    validateForm(state);
    signUpUser(state)
  }

  function handleChange(event) {
    const {name, value} = event.target;
    setState({ ...state, [name]: value });
  }
    
  return (
    <form onSubmit={handleSubmit}>
      <input name="username" onChange={handleChange} />
      <input name="email" onChange={handleChange} />
      <input name="password" onChange={handleChange} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

Notez également que lors de l'utilisation du hook `useState`, vous devez propager tous les états précédents afin de mettre à jour une paire clé-valeur individuelle. 

Chaque fois qu'un utilisateur tape dans une entrée et que l'événement de changement a lieu, la fonction `handleChange` est appelée. 

Ensuite, nous mettons non seulement à jour la valeur d'une certaine entrée selon son attribut `name`, mais nous propagons également toutes les valeurs d'état actuelles du nom d'utilisateur, de l'e-mail et du mot de passe. Nous propagons toutes ces valeurs en tant que propriétés individuelles dans le nouvel objet que nous définissons dans l'état avec le `...` – l'opérateur de propagation d'objet.

## Comment utiliser les ternaires pour appliquer conditionnellement des classes / props en JavaScript

Les ternaires sont un opérateur essentiel à utiliser lors de l'écriture de conditionnels dans les composants React. 

Nous utilisons souvent des ternaires dans notre JSX car ce sont des expressions et elles se résolvent en une valeur ou une autre qui peut être affichée. Cela leur permet souvent d'être utilisées pour afficher ou masquer des composants et des éléments.

Il est cependant utile de noter que nous pouvons utiliser des ternaires lorsqu'il s'agit de toute valeur dans notre JSX. 

Cela signifie que, au lieu d'utiliser des bibliothèques tierces comme `classnames` pour ajouter ou supprimer conditionnellement des classes à nos éléments React, nous pouvons le faire avec un ternaire en ligne et un littéral de modèle JavaScript. 

Vous pouvez voir dans l'exemple ici que si notre utilisateur a sélectionné le mode sombre, nous appliquons une classe `body-dark`. Sinon, nous appliquons la classe `body-light` pour donner à notre application les styles appropriés à tout ce qui se trouve dans notre composant `Routes`. 

```js
export default function App() {
  const { isDarkMode } = useDarkMode();
    
  return (
    <main className={`body ${isDarkMode ? "body-dark" : "body-light"}`}>
      <Routes />
    </main>
  );
}
```

Il est utile de noter que cette logique conditionnelle peut être appliquée à n'importe quelle prop également, pas seulement aux noms de classe ou aux styles en ligne. 

Nous avons un autre exemple ici dans lequel notre application détecte si l'utilisateur est sur un appareil mobile ou non avec un hook spécial. Si c'est le cas, nous transmettons une valeur de hauteur spécifique via la prop `height` à notre composant `Layout`.

```js
export default function App() {
  const { isMobile } = useDeviceDetect();
    
  return (
    <Layout height={isMobile ? '100vh' : '80vh'}>
      <Routes />
    </Layout>
  );
}
```

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*