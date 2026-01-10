---
title: La meilleure façon d'architecturer votre application Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T22:13:56.000Z'
originalURL: https://freecodecamp.org/news/the-best-way-to-architect-your-redux-app-ad9bd16c8e2d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OxDtmLW8xodYnzAeLKXMqA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La meilleure façon d'architecturer votre application Redux
seo_desc: 'By Lusan Das

  This article is about how to think in Redux. We’ll try to understand how we can
  utilise this wonderful library to make our application more stable, robust, and
  maintainable. It is language agnostic, however we will keep our scope to Redu...'
---

Par Lusan Das

Cet article explique comment penser en Redux. Nous allons essayer de comprendre comment utiliser cette bibliothèque merveilleuse pour rendre notre application plus stable, robuste et maintenable. Il est indépendant du langage, cependant, nous allons nous limiter à Redux avec React.

Pour ceux qui n'ont jamais utilisé Redux, je vais citer la [documentation](https://redux.js.org/) :

> Redux est un conteneur d'état prévisible pour les applications JavaScript.

Ce n'est qu'une bibliothèque de 2 ko qui résout l'un des plus grands problèmes de maintenance des grandes applications JavaScript : la gestion d'état.

Cet article ne parle pas de Redux, car il existe déjà de nombreux articles à ce sujet. Il s'agit plutôt de la manière dont nous devons visualiser une application Redux et l'utiliser efficacement.

Supposons que nous construisons une application de commerce électronique avec quelques pages de base comme le catalogue, les détails du produit et le succès du paiement.

Voici les maquettes de l'apparence de l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/AOXLtZSHXOg-wHn2nL-exW2QXjHCQvMnBpMv)
_Page Catalogue_

![Image](https://cdn-media-1.freecodecamp.org/images/9ozwPviyKCIKwKaeEAQ6m9UK5yLtdkvXFedE)
_Page Produit_

![Image](https://cdn-media-1.freecodecamp.org/images/-ycevoUXMQz0Br2N3u-OxfunYLfs8ueaEx93)
_Succès du Paiement_

Ainsi, architecturer en Redux signifie que nous devons visualiser l'application comme une seule entité, et chaque page est une sous-entité.

Il y a quatre étapes pour construire une application Redux :

1. Visualiser l'arborescence d'état
2. Concevoir vos reducers
3. Implémenter les Actions
4. Implémenter la Présentation

### Étape 1 : Visualiser l'arborescence d'état

À partir des maquettes ci-dessus, concevons notre arborescence d'état.

![Image](https://cdn-media-1.freecodecamp.org/images/PxbfMiRBMWkyTYHpwT3hfv8sLRSCL-XeW2hb)
_Arborescence d'état de l'application_

C'est l'étape la plus importante. Une fois que nous avons visualisé notre arborescence d'état, la mise en œuvre des techniques Redux devient vraiment facile ! Les cercles pointillés sont des états qui seront partagés par l'application, les cercles pleins sont des états spécifiques à une page.

### Étape 2 : Concevoir vos reducers

Au cas où vous vous demanderiez ce qu'est exactement un reducer, je vais citer directement la documentation :

> Les **reducers** spécifient comment l'état de l'application change en réponse aux [actions](https://redux.js.org/basics/actions) envoyées au store. Rappelez-vous que les actions décrivent uniquement _ce qui s'est passé_, mais ne décrivent pas comment l'état de l'application change.

Chacun des états qui sont importants peut avoir ses propres reducers. Plus tard, nous pouvons les combiner en un seul reducer racine qui définira finalement le store (la seule source de vérité de l'application). C'est là que réside la véritable puissance : vous avez un contrôle total sur vos états et leur comportement. Rien n'échappe à la surveillance du store. L'observateur silencieux garde un œil.

![Image](https://cdn-media-1.freecodecamp.org/images/0J1lSXo1yvDLVPTyogpfNw7c1YONwwO0iqAQ)
_Le store garde un œil_

Examinons un exemple de la manière de concevoir un reducer à l'aide de l'arborescence d'état de l'application que nous avons conçue ci-dessus.

```javascript
// Reducer Racine
const rootReducer = combineReducer({  
    header: headerReducer,  
    login: loginReducer,  
    footer: footerReducer,  
    common: commonReducer,  
    product: productReducer,  
    catalog: catalogReducer,  
    payment: paymentReducer
});
```

Le reducer racine dit tout. Il contient tout ce que le store doit savoir sur l'application.

Maintenant, voyons à quoi ressemble une sous-entité headerReducer.

Rappelez-vous comment nous avons conçu notre état d'en-tête ?

![Image](https://cdn-media-1.freecodecamp.org/images/QASD6Q8cBo1IkbTZw7LKP8sDQcbmEgRLO1TG)
_Arborescence d'état de l'en-tête_

```javascript
// Header Reducer

const headerReducer = combineReducer({
    menu: menuReducer,  
    search: searchReducer,  
    location: locationReducer
});
```

Notre reducer est une réplique de ce que nous avons conçu précédemment dans notre arborescence d'état. C'est la puissance de la visualisation.

Remarquez comment un reducer contient d'autres reducers. Nous n'avons pas besoin de créer un reducer énorme. Il peut être facilement divisé en reducers plus petits, car chacun possède ses identités individuelles et a ses propres opérations spécifiques. Cela nous aide à créer une séparation de la logique, ce qui est très important pour maintenir de grandes applications.

Maintenant, comprenons comment un fichier reducer typique doit être configuré, par exemple searchReducer.

```javascript
// Search Reducer

const initialState = {  payload: [],  isLoading: false,  error: {}};

export function searchReducer( state=initialState, action ) { 	 
    switch(action.type) {    
        case FETCH_SEARCH_DATA:      
            return {        
                	...state,        
                    isLoading: true    
            };        
        case FETCH_SEARCH_SUCCESS:      
            return {        
	                ...state,        
                    payload: action.payload,        
                    isLoading: false      
                   };        
        case FETCH_SEARCH_FAILURE:      
            return {        
	                ...state,        
                    error: action.error,        
                    isLoading: false            
            };
                
        case RESET_SEARCH_DATA:      
            return { ...state, ...initialState }        
		default:      return state;
    }
}
```

Ce modèle de reducer définit les changements possibles dans son état de recherche lorsque l'API de recherche est appelée.

```javascript
FETCH_SEARCH_DATA, FETCH_SEARCH_SUCCESS, FETCH_SEARCH_FAILURE, RESET_SEARCH_DATA
```

Tous les éléments ci-dessus sont des constantes possibles qui définissent quelles **actions** peuvent être effectuées.

> _Note : Il est important de maintenir une action RESET_SEARCH_DATA, au cas où nous aurions besoin de réinitialiser les données lors du démontage d'un composant._

### Étape 3 : Implémenter les Actions

Chaque action qui comporte des appels API passe généralement par trois étapes dans une application.

1. État de chargement -> FETCH_SEARCH_DATA
2. Succès -> FETCH_SEARCH_SUCCESS
3. Échec -> FETCH_SEARCH_FAILURE

Maintenir ces types d'actions nous aide à vérifier le flux de données lorsqu'une API est appelée dans notre application.

Plongeons dans le code pour comprendre à quoi ressemble une action typique.

```javascript
export function fetchSearchData(args) {  
	return async (dispatch) => {    
        // Initiate loading state    
        dispatch({      
            type: FETCH_SEARCH_DATA    
        });
        try {      
            // Call the API      
            const result = await fetchSearchData(
                args.pageCount, 
                args.itemsPerPage
            );           
            // Update payload in reducer on success     
            dispatch({        
                type: FETCH_SEARCH_SUCCESS,        
                payload: result,        
                currentPage: args.pageCount      
            });    
        } catch (err) {     
            // Update error in reducer on failure           
            dispatch({        
                type: FETCH_SEARCH_FAILURE,        
                error: err      
            });    
        }  
    };
}
```

Remarquez comment le flux de données est suivi par le store à travers les actions. Cela rend chaque changement dans l'application responsable.

Ainsi, des actions similaires sont écrites pour chaque changement dans les reducers de divers états.

L'un des plus grands avantages de Redux est l'abstraction de chaque action.

![Image](https://cdn-media-1.freecodecamp.org/images/1bOAlC9gdaJZtjvLE8VbESW0m4zGX435YDLo)
_Flux de données dans une application Redux_

### Étape 4 : Implémenter la Présentation

```javascript
import React, { Component } from 'react';
import { connect } from 'react-redux';;

import fetchSearchData from './action/fetchSearchData';
import SearchData from './SearchData';

const Search = (props) => (  
    <SearchData     
    	search={props.search}    
		fetchSearchData={props.fetchSearchData}   
	/>
);

const mapStateToProps = (state) => ({  
    search: state.header.search.payload
});

const mapDispatchToProps = {  fetchSearchData};

export default connect(mapStateToProps, mapDispatchToProps)(Search)
```

Comme vous pouvez le voir, le composant de présentation est très simple et facile à comprendre.

### Conclusion

Je voudrais mentionner certains des plus grands avantages que j'ai trouvés en utilisant Redux :

1. Il réduit certainement les mauvaises odeurs de code.
2. L'abstraction du code est plus facile à atteindre.
3. Redux nous introduit également à d'autres principes comme l'immuabilité, la programmation fonctionnelle, et bien d'autres.
4. Il vous permet de visualiser chaque action et de les suivre avec le "time traveling".

J'espère que cet article vous aide à avoir une image plus claire de pourquoi Redux est vraiment génial, et comment nous pouvons utiliser le pouvoir de la visualisation pour créer des applications maintenables.

_Suivez-moi sur [twitter](https://twitter.com/daslusan)_ pour obtenir plus de mises à jour concernant les nouveaux articles et pour rester à jour dans les derniers développements frontend. Partagez également cet article sur twitter pour aider les autres à le connaître. Partager, c'est prendre soin **^_^.**

### Quelques ressources utiles

1. [https://redux.js.org/](https://redux.js.org/)
2. [https://github.com/reduxjs/redux/blob/master/examples](https://github.com/reduxjs/redux/blob/master/examples)
3. [https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.c4yhhvk0d](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.c4yhhvk0d)

### Mes articles précédents

1. [https://medium.freecodecamp.org/how-to-use-redux-persist-when-migrating-your-states-a5dee16b5ead](https://medium.freecodecamp.org/how-to-use-redux-persist-when-migrating-your-states-a5dee16b5ead)
2. [https://codeburst.io/redux-observable-to-the-rescue-b27f07406cf2](https://codeburst.io/redux-observable-to-the-rescue-b27f07406cf2)
3. [https://codeburst.io/building-webapp-for-the-future-68d69054cbbd](https://codeburst.io/building-webapp-for-the-future-68d69054cbbd)
4. [https://codeburst.io/cors-story-of-requesting-twice-85219da7172d](https://codeburst.io/cors-story-of-requesting-twice-85219da7172d)