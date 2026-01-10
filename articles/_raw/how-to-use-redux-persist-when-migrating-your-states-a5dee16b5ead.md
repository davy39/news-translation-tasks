---
title: How to use Redux Persist when migrating your states
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
seo_title: null
seo_desc: 'By Lusan Das

  Storage has always been an integral part of building apps. While building a webapp
  for our company, I needed a way to persist my states in storage which was reliable,
  easy to use, and configurable based on the requirements.

  Thankfully th...'
---

By Lusan Das

Storage has always been an integral part of building apps. While building a webapp for our company, I needed a way to persist my states in storage which was reliable, easy to use, and configurable based on the requirements.

Thankfully this library was the answer to all my problems!

This article is based on a problem I faced while working on a project. Let us dive deep and understand how the library helped me solve it.

If you haven’t already used [redux-persist](https://github.com/rt2zz/redux-persist), then do read the docs, as they’re self-explanatory. If you want to know why you should use this library, go through this [article](https://medium.com/async-la/redux-persist-your-state-7ad346c4dd07) — it is a great intro by the [author](https://twitter.com/rt2zz) himself!

### Problem

Let’s take an example where I wanted to persist a reducer in my localStorage:

```javascript
//Reducer
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
//View
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

//Reducer in localStorage
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

Now this reducer has persisted in our client’s device. So what will happen if I introduce a new key to our **reducerA**?

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
                address: "CA" // NEW KEY ADDED
			}    
		}  
	},  
    condition: "prime"
}
```

Let’s say we have a view which renders the value of our newly introduced key:

```javascript
//View with new key address
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

When I load my application with the newly introduced key, the rendering of our view fails. It throws an error where it states:

```javascript
Cannot render address of undefined
```

This happened because the client’s storage is in sync with the rootReducer initialized during our app reload.

Even though we introduced the new key, the client’s storage never received it. It initializes our rootReducer with the old values in storage, where the address never existed, and causes the rendering of our component to fail.

### Solution

This leads to a well-known concept: the migration of the database.

> A schema **migration** is performed on a **database** whenever it is necessary to update or revert that **database’s** schema to some newer or older version. **Migrations** are performed programmatically by using a schema **migration** tool — [Wikipedia](https://en.wikipedia.org/wiki/Schema_migration)

LocalStorage is in fact a small database of key value pairs. Redux Persist does it beautifully. If you look at a project initialized with this library, it already uses a **default version -1**. Take a look below at the screenshot taken from the application tab in the Chrome dev tool.

![Image](https://cdn-media-1.freecodecamp.org/images/0rJmD7xq6mgOnUokqih4WTMy2F6Kd3GmgalV)
_localStorage in Chrome Dev Tool_

This is really good! The library already maintains a default version for us, so that we can incorporate the migration feature in the future.

The key is to configure your persist configuration in your rootReducer.

```javascript
export const persistConfig = {  
    key: 'testApp',  
    version: 0, //New version 0, default or previous version -1  
    storage,  
    debug: true,  
    stateReconciler: autoMergeLevel2,  
    migrate: createMigrate(migrations, { debug: true })
}
```

It is important that we update the version to 0, so that it migrates our storage from -1 to 0.

Next, we write the migration to let our storage know that there is an update.

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
                        address: "CA" //New Key added for migration
                    }
				}      
			}    
		}  
    }
}
```

The **migrations** are then used in our persist config mentioned above:

```
migrate: createMigrate(migrations, { debug: true })
```

Thus, when we reload our application, our application goes through a reconciliation phase where the storage is brought in sync with the newly-updated reducer.

### Conclusion

The configuration above will always keep the application updated on the client side when you release new versions. It is very important that we are careful about this when making offline first apps.

It is simple once you understand the basic concept and technique to do it. I hope this article helped you understand the importance of managing versions of your states in storage :)

_Follow me on [twitter](https://twitter.com/daslusan)_ to get more updates regarding new articles and to stay updated in latest frontend developments. Also share this article on twitter to help others know about it. Sharing is caring **^_^.**

### Some helpful resources

1. [https://github.com/rt2zz/redux-persist/blob/master/docs/api.md](https://github.com/rt2zz/redux-persist/blob/master/docs/api.md)
2. [https://medium.com/@clrksanford/persist-ence-is-key-using-redux-persist-to-store-your-state-in-localstorage-ac6a000aee63](https://medium.com/@clrksanford/persist-ence-is-key-using-redux-persist-to-store-your-state-in-localstorage-ac6a000aee63)
3. [https://medium.com/async-la/redux-persist-your-state-7ad346c4dd07](https://medium.com/async-la/redux-persist-your-state-7ad346c4dd07)

