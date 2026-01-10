---
title: Comment éviter le Prop Drilling avec l'API Context de React
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-10-13T16:52:03.000Z'
originalURL: https://freecodecamp.org/news/avoid-prop-drilling-with-react-context-api
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/ferenc-almasi-c8h0n7fSTqs-unsplash.jpg
tags:
- name: React
  slug: react
- name: React context
  slug: react-context
- name: 'State Management '
  slug: state-management
seo_title: Comment éviter le Prop Drilling avec l'API Context de React
seo_desc: "The React Context API provides a way to pass data through multiple nested\
  \ levels of components without having to manually pass that data to each level.\
  \ \nReact context is one sure way of globally managing your data in your app, and\
  \ it's a good way to ..."
---

L'API Context de React fournit un moyen de transmettre des données à travers plusieurs niveaux de composants imbriqués sans avoir à passer manuellement ces données à chaque niveau. 

Le contexte React est un moyen sûr de gérer globalement vos données dans votre application, et c'est une bonne façon d'éviter le prop drilling. 

Dans ce tutoriel, nous allons apprendre comment utiliser l'API Context de React (le hook useContext) pour éviter le prop drilling.

## Qu'est-ce que le Prop Drilling ?

Dans une application React traditionnelle, les données sont souvent partagées entre les composants en utilisant des props. Partager manuellement ces données peut être fastidieux, surtout lorsqu'elles sont partagées entre plusieurs composants imbriqués. De plus, partager des données entre deux composants enfants peut être fastidieux. D'où le besoin de gestion d'état globale. 

**Le Prop Drilling** est une situation où les données sont passées d'un composant à travers plusieurs composants interdépendants jusqu'à ce que vous arriviez au composant où les données sont nécessaires. Voici une illustration du prop drilling pour vous aider à comprendre :  


![Image](https://lh5.googleusercontent.com/K1veBT9r_aQPq_iYI9MdtljbsBu8egv7n8cu78fWqzL0POVn2xb66r_gEFgJ8qg9FxphsGFqNZIDQ3QZ0zuT-XtEcrpNVZylXvxhDTPAySL8_FJWiIGHlcXggcHYCFKaQeNp8HRQvCZZQHRULaf8_vtg8mgyZElVhkSiUYgicFQ0mo6zPgGve9-Pcg)

Passer des données à travers plusieurs composants n'est pas une bonne façon d'écrire du code propre, réutilisable et DRY. 

L'API Context de React est un moyen rapide d'éviter le prop drilling et de s'assurer que vos données sont gérées globalement sans utiliser une énorme application de gestion d'état tierce comme [Redux](https://redux.js.org/) et [MobX](https://mobx.js.org/README.html).

## Qu'est-ce que l'API Context de React ?

Le contexte React est une API intégrée qui utilise le hook useContext pour partager des données entre les composants. 

Imaginez passer les données d'un utilisateur authentifié d'un composant parent à un composant enfant profondément imbriqué. Cela sera fastidieux si vous devez passer les données à travers beaucoup de composants intermédiaires. 

Une meilleure approche pour faire cela est d'utiliser le contexte React pour gérer les données.  

## Comment utiliser l'API Context de React

### Comment créer un contexte

useContext est un hook intégré dans React. Vous pouvez commencer à utiliser l'API Context en important la fonction createContext de React comme ceci :

```app.js
Import {createContext} from 'react';
const AuthContext = createContext();
```

Ici, nous avons initialisé notre contexte et l'avons nommé **AuthContext.** L'étape suivante est de fournir le contexte.

### Comment fournir le contexte aux composants qui en ont besoin

L'API Context utilise un fournisseur pour passer des données à ses composants enfants. Vous devrez envelopper tous les composants avec un composant fournisseur.

```app.js
<AuthContext.Provider value={...}>
	<ParentComponent/>
<AuthContext.Provider>
```

Le composant Provider a une prop **value** comme vu ci-dessus. La valeur du contexte peut être mise à jour ou définie en utilisant la prop **value**. Dans notre cas, nous allons définir la prop value au nom de notre utilisateur authentifié.

```app.js
import React from 'react';

function App() {

	const username = "John Doe"
    
	return(
        <AuthContext.Provider value={username}>
        	<Dashboard/>
        <AuthContext.Provider>
    )
}

export default App;
```

Hourra ! Tous les composants à l'intérieur de ce composant **App** auront accès aux données du nom d'utilisateur. Ensuite, voyons comment utiliser le contexte.

### Comment consommer le contexte

Nous pouvons consommer le contexte en utilisant le hook **useContext**. Sans passer de données à travers des composants imbriqués, vous pouvez accéder à votre contexte dans n'importe quel composant que vous voulez. Voici comment.

```profile.js
import { useContext } from 'react';

const Profile = () => {

	const value = useContext(AuthContext);
    
	return (
        <div>
        	{value}
        </div>
    )
}

export default Profile
```

## Conclusion

En plus de résoudre le problème du prop drilling, vous pouvez également utiliser le contexte React pour la configuration de thème, la gestion d'état globale et plus encore. 

Notez que l'API Context de React n'est pas un remplacement pour un outil de gestion d'état global comme Redux et MobX. Vous pouvez lire plus sur le contexte React [ici](https://reactjs.org/docs/context.html).

J'espère que vous avez apprécié ce tutoriel.

**Bon codage !**