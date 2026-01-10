---
title: Comment utiliser Redux Persist lors de la migration de vos états
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-12T10:54:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-redux-persist-when-migrating-your-states-a5dee16b5ead
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xwtbmeBwPveQTgzDMP-zsw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment utiliser Redux Persist lors de la migration de vos états
seo_desc: 'By Lusan Das

  Storage has always been an integral part of building apps. While building a webapp
  for our company, I needed a way to persist my states in storage which was reliable,
  easy to use, and configurable based on the requirements.

  Thankfully th...'
---

Par Lusan Das

Le stockage a toujours été une partie intégrante de la construction d'applications. En développant une application web pour notre entreprise, j'avais besoin d'un moyen de persister mes états dans le stockage qui soit fiable, facile à utiliser et configurable en fonction des exigences.

Heureusement, cette bibliothèque a été la réponse à tous mes problèmes !

Cet article est basé sur un problème que j'ai rencontré en travaillant sur un projet. Plongeons-nous et comprenons comment la bibliothèque m'a aidé à le résoudre.

Si vous n'avez pas encore utilisé [redux-persist](https://github.com/rt2zz/redux-persist), alors lisez la documentation, car elle est auto-explicative. Si vous voulez savoir pourquoi vous devriez utiliser cette bibliothèque, parcourez cet [article](https://medium.com/async-la/redux-persist-your-state-7ad346c4dd07) — c'est une excellente introduction par l'[auteur](https://twitter.com/rt2zz) lui-même !

### Problème

Prenons un exemple où je voulais persister un réducteur dans mon localStorage :

```javascript
// Réducteur
reducerA: {  
    engine: {    
        model: "F5AAA",    
        manufacturer: "Ferrari"  
    },  
    tyre: {    
        model: "T123",   
		manufacturer: "MRF",    
		owner: {      
            details: {        
                name: "Zack",        
				age: "26"            
            }    
        }  
    },  
	condition: "prime"
}
```

```javascript
// Vue
class TestComponent extends React.Component {  
    render() {    
        const model = someStateOfReducerA.tyre.model    
        const manufacturer = someStateOfReducerA.tyre.manufacturer
        
		return (      
            <div>{model}</div>      
            <div>{manufacturer}</div>    
        )  
    }
}

// Réducteur dans localStorage
reducerA: {  
    engine: {    
        model: "F5AAA",    
		manufacturer: "Ferrari"  
    },  
	tyre: {    
        model: "T123",    
		manufacturer: "MRF",    
		owner: {      
            details: {        
                name: "Zack",        
				age: "26"            
            }    
        }  
    },  
	condition: "prime"
}
```

Maintenant, ce réducteur a persisté dans le dispositif de notre client. Alors, que se passera-t-il si j'introduis une nouvelle clé dans notre **reducerA** ?

```javascript
reducerA: {  
	engine: {    
    	model: "F5AAA",    
	    manufacturer: "Ferrari"  
   	},  
    tyre: {    
    	model: "T123",    
        manufacturer: "MRF",    
        owner: {      
        	details: {        
            	name: "Zack",        
                age: "26",        
                address: "CA" // NOUVELLE CLÉ AJOUTÉE
			}    
		}  
	},  
    condition: "prime"
}
```

Disons que nous avons une vue qui rend la valeur de notre nouvelle clé :

```javascript
// Vue avec la nouvelle clé address
class TestComponent extends React.Component {  
    render() {    
        const model = someStateOfReducerA.tyre.model    
        const manufacturer = someStateOfReducerA.tyre.manufacturer    
        const address = someStateOfReducerA.tyre.owner.details.address
        
		return (      
            <div>{model}</div>      
            <div>{manufacturer}</div>      
            <div>{address}</div>
		)  
    }
}
```

Lorsque je charge mon application avec la nouvelle clé introduite, le rendu de notre vue échoue. Cela génère une erreur indiquant :

```javascript
Cannot render address of undefined
```

Cela s'est produit parce que le stockage du client est synchronisé avec le rootReducer initialisé lors du rechargement de notre application.

Même si nous avons introduit la nouvelle clé, le stockage du client ne l'a jamais reçue. Il initialise notre rootReducer avec les anciennes valeurs dans le stockage, où l'adresse n'a jamais existé, et provoque l'échec du rendu de notre composant.

### Solution

Cela conduit à un concept bien connu : la migration de la base de données.

> Une **migration** de schéma est effectuée sur une **base de données** chaque fois qu'il est nécessaire de mettre à jour ou de revenir à une version plus ancienne ou plus récente de ce **schéma de base de données**. Les **migrations** sont effectuées de manière programmatique à l'aide d'un outil de **migration de schéma** — [Wikipedia](https://en.wikipedia.org/wiki/Schema_migration)

LocalStorage est en fait une petite base de données de paires clé-valeur. Redux Persist le fait magnifiquement. Si vous regardez un projet initialisé avec cette bibliothèque, il utilise déjà une **version par défaut -1**. Jetez un œil ci-dessous à la capture d'écran prise dans l'onglet application de l'outil de développement Chrome.

![Image](https://cdn-media-1.freecodecamp.org/images/0rJmD7xq6mgOnUokqih4WTMy2F6Kd3GmgalV)
_localStorage dans l'outil de développement Chrome_

C'est vraiment bien ! La bibliothèque maintient déjà une version par défaut pour nous, afin que nous puissions incorporer la fonctionnalité de migration à l'avenir.

La clé est de configurer votre configuration de persistance dans votre rootReducer.

```javascript
export const persistConfig = {  
    key: 'testApp',  
    version: 0, // Nouvelle version 0, version par défaut ou précédente -1  
    storage,  
    debug: true,  
    stateReconciler: autoMergeLevel2,  
    migrate: createMigrate(migrations, { debug: true })
}
```

Il est important que nous mettons à jour la version à 0, afin qu'elle migre notre stockage de -1 à 0.

Ensuite, nous écrivons la migration pour informer notre stockage qu'il y a une mise à jour.

```javascript
const migrations = {  
    0: (state) => {    
        return {      ...
			state,      
			tyre: {        ...
				state.tyre,        
				owner: {          ...
					state.tyre.owner,          
					details: {
                        state.tyre.owner.details,
                        address: "CA" // Nouvelle clé ajoutée pour la migration
                    }
				}      
			}    
		}  
    }
}
```

Les **migrations** sont ensuite utilisées dans notre configuration de persistance mentionnée ci-dessus :

```
migrate: createMigrate(migrations, { debug: true })
```

Ainsi, lorsque nous rechargeons notre application, notre application passe par une phase de réconciliation où le stockage est synchronisé avec le réducteur nouvellement mis à jour.

### Conclusion

La configuration ci-dessus maintiendra toujours l'application à jour côté client lorsque vous publierez de nouvelles versions. Il est très important que nous soyons prudents à ce sujet lorsque nous créons des applications offline first.

C'est simple une fois que vous comprenez le concept de base et la technique pour le faire. J'espère que cet article vous a aidé à comprendre l'importance de gérer les versions de vos états dans le stockage :)

_Suivez-moi sur [twitter](https://twitter.com/daslusan)_ pour obtenir plus de mises à jour concernant les nouveaux articles et pour rester informé des derniers développements frontend. Partagez également cet article sur twitter pour aider les autres à le connaître. Partager, c'est prendre soin **^_^.**

### Quelques ressources utiles

1. [https://github.com/rt2zz/redux-persist/blob/master/docs/api.md](https://github.com/rt2zz/redux-persist/blob/master/docs/api.md)
2. [https://medium.com/@clrksanford/persist-ence-is-key-using-redux-persist-to-store-your-state-in-localstorage-ac6a000aee63](https://medium.com/@clrksanford/persist-ence-is-key-using-redux-persist-to-store-your-state-in-localstorage-ac6a000aee63)
3. [https://medium.com/async-la/redux-persist-your-state-7ad346c4dd07](https://medium.com/async-la/redux-persist-your-state-7ad346c4dd07)