---
title: Mutabilité vs Immuabilité en JavaScript – Expliqué avec des Exemples de Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-05T18:20:10.000Z'
originalURL: https://freecodecamp.org/news/mutability-vs-immutability-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/purple-balls-1.jpg
tags:
- name: immutability
  slug: immutability
- name: JavaScript
  slug: javascript
seo_title: Mutabilité vs Immuabilité en JavaScript – Expliqué avec des Exemples de
  Code
seo_desc: "By Chukwunonso Nwankwo\nIn JavaScript, different data types have different\
  \ behaviors and locations in memory. So to reduce the chances of having bugs in\
  \ your code, you need to understand the concept of mutability and immutability in\
  \ JavaScript. \nMutab..."
---

Par Chukwunonso Nwankwo

En JavaScript, différents types de données ont différents comportements et emplacements en mémoire. Pour réduire les chances d'avoir des bugs dans votre code, vous devez comprendre le concept de mutabilité et d'immuabilité en JavaScript. 

La mutabilité fait référence aux types de données qui peuvent être accessibles et modifiés après avoir été créés et stockés en mémoire. L'immuabilité, en revanche, fait référence aux types de données que vous ne pouvez pas modifier après les avoir créés – mais que vous pouvez toujours accéder en mémoire.

Cet article vous aidera à comprendre pleinement le concept de mutabilité et d'immuabilité des données en JavaScript. Nous commencerons par comprendre les différents types de données et nous irons de là. 

### Prérequis

* Connaissance du fonctionnement des variables en JavaScript
* Connaissance du fonctionnement des objets en JavaScript

### Table des Matières

* [Quels sont les Types de Données Primitifs en JavaScript ?](#heading-quels-sont-les-types-de-donnees-primitifs-en-javascript)
* [Quels sont les Types de Données de Référence en JavaScript ?](#heading-quels-sont-les-types-de-donnees-de-reference-en-javascript)
* [Comment Cloner les Propriétés d'un Objet](#heading-comment-cloner-les-proprietes-dun-objet)
* [Qu'est-ce que l'Immuabilité en JavaScript ?](#heading-quest-ce-que-limmuabilite-en-javascript)
* [Comment Empêcher la Mutabilité des Objets](#heading-comment-empecher-la-mutabilite-des-objets)
* [const != Immuabilité](#heading-const-immutabilite)
* [Réflexions Finales](#heading-reflexions-finales)

# Types de Données en JavaScript

Les types de données sont catégorisés en types `Primitifs` et `Références` en JavaScript. Avant d'expliquer ces catégories, examinons deux termes importants concernant la mémoire que vous devez connaître : la `Pile` et le `Tas`.

### Qu'est-ce que la Pile ?

La pile est une structure de données qui obéit au principe `Dernier Entré, Premier Sorti` (LIFO). Cela implique que le dernier élément à entrer dans la `pile` en sort le premier. 

Imaginez une pile de livres empilés sur une étagère. Le dernier livre se retrouve être le premier à être retiré. Les données stockées dans la pile peuvent encore être facilement accessibles.

### Qu'est-ce que le Tas ?

Les données de référence sont stockées dans le `tas`. Lorsque des données de référence sont créées, la variable de la donnée est placée sur la `pile`, mais la valeur réelle est placée sur le `tas`. 

## Quels sont les Types de Données Primitifs en JavaScript ?

Les types de données primitifs sont immuables et ne sont pas des objets car ils manquent de propriétés et de méthodes.

![data-types-1](https://www.freecodecamp.org/news/content/images/2023/04/data-types-1.png)

Pour déterminer le type de données avec lequel vous travaillez, utilisez l'opérateur `typeof`. L'opérateur `typeof` fonctionne parfaitement avec tous les types de données primitifs sauf `null`. 

### Exemples de Types de Données Primitifs

Examinons quelques exemples de types de données primitifs pour mieux comprendre ce qu'ils sont et comment ils fonctionnent.

Voici un exemple de nombre :

```js
let num = 23;

console.log(typeof num)
```

Voici un exemple de chaîne de caractères :

```js
let str = "Table"
```

Voici un exemple de variable non définie. Une variable est dite non définie si aucune valeur ne lui est attachée.

```js
let figure;

 `null`
 
   let fig = null

   console.log(fig)

   console.log(fig === null)
```

Gardez à l'esprit que `null` n'est pas la même chose que `Null` ou `NULL`.

Voici un exemple de booléen. Ce type de données primitif est soit `true` soit `false`.

```js
   let student = true;

   let married = false;
```

Les booléens ne sont pas des chaînes de caractères – notez que `true` ou `false` ne sont pas entre guillemets.

Voici un exemple de symbole. En tant que type de données primitif, les symboles sont uniques. Les valeurs qui sont retournées sont également garanties d'être uniques.

```js
   const mySymbol = Symbol();
   
   console.log(typeof mySymbol) //Symbol
```

Voici un exemple de BigInt. Utilisez `BigInt` lorsque les valeurs avec lesquelles vous travaillez sont trop grandes pour les types de données numériques.

```js
   const myBigInt = 12n;

   console.log(typeof myBigInt) //BigInt

   const check = BigInt(414242532)

   console.log(typeof check)
```


## Quels sont les Types de Données de Référence en JavaScript ?

Par défaut, les types de données de référence sont mutables. Les types de données de référence se composent de `Fonctions`, `Tableaux` et `Objets`.  

Examinons quelques exemples de types de données de référence pour vous aider à mieux comprendre :

Voici un exemple de fonction :

```js
   function favorite(question) {
      console.log(`Salut, aimez-vous le langage de programmation ${question} ?`)
   }

   favorite('JavaScript')

```

Voici un exemple de tableau :

```js
   const countriesVisited = ['Nigeria', 'Japan', 'Australia']

   console.log(countriesVisited)

```

Voici un exemple d'objet :

```js

   const touristData = {
      firstname: 'Camila',
      lastname: 'Pedro',
      Nationality: 'Spanish'
   }
   console.log(touristData)

```

Pour plus de clarté, le prénom est appelé la `clé` tandis que Camila est la `valeur`.

Les types de données de référence placent la variable sur la `pile`. La variable sert de pointeur qui pointe vers l'`objet` situé sur le `tas`. 

La principale distinction entre ces catégories est que les Primitifs sont `immuables` mais les Références sont `mutables`. Maintenant, passons au cœur du sujet.

# Qu'est-ce que la Mutabilité en JavaScript ?

Si un type de données est mutable, cela signifie que vous pouvez le changer. La mutabilité vous permet de modifier des valeurs existantes sans en créer de nouvelles. 

Pour chaque `objet`, un pointeur est ajouté à la `pile`, et ce pointeur pointe vers l'`objet` sur le `tas`.  

Prenons, par exemple, le code suivant : 

```js
    const staff = {
         name: "Strengthened",
         age: 43,
         Hobbies: ["reading", "Swimming"]
   }

```

Sur la pile, vous trouverez `staff` qui est un pointeur vers l'objet réel sur le `tas`.

```js
   const staff2 = staff;

   console.log(staff);
   
   console.log(staff2);
```

Un autre pointeur est placé sur la `pile` lorsque `staff` a été assigné à `staff2`. Maintenant, ces pointeurs pointent vers un seul objet sur le `tas`.

Les données de référence ne copient pas les valeurs, mais plutôt les pointeurs.

```js
   staff2.age = 53;

   console.log(staff)

   console.log(staff2)

```

Changer l'`age` de `staff2` met à jour l'`age` de l'objet `staff`. Maintenant, vous savez que c'est parce que les deux pointent vers le même objet. 

  ![reference2-1](https://www.freecodecamp.org/news/content/images/2023/04/reference2-1.png)


## Comment Cloner les Propriétés d'un Objet

Vous pouvez cloner les propriétés d'un objet en utilisant la méthode `Object.assign()` et l'opérateur de `spread`. Avec ceux-ci, vous pouvez changer les propriétés de l'objet cloné sans changer les propriétés de l'objet à partir duquel il a été cloné.
 
### Comment la méthode `Object.assign()` fonctionne

La méthode `object.assign` copie les propriétés d'un objet (la source) dans un autre objet (la cible) et retourne l'objet cible modifié.

Voici la syntaxe :

```Object.assign(target, source)```

La méthode a deux arguments, `target` et `source`. Le `target` est l'objet qui reçoit de nouvelles propriétés, tandis que le `source` est l'endroit d'où proviennent les propriétés. Le `target` peut être un objet vide `{}.` 

Dans une situation où le `source` et le `target` partagent la même `clé`, l'objet `source` écrase la valeur de la `clé` sur la cible.

```js
   const staff = {
      name: "Strengthened",
      age: 43,
      Hobbies: ["reading", "Swimming"]
   }

   const staff2 = Object.assign({}, staff);
```

Les propriétés de l'objet `staff` ont été clonées dans une cible vide. 

`staff2` a maintenant ses propres propriétés. Vous pouvez le prouver en changeant la valeur de l'une de ses propriétés. Faire ce changement n'affectera pas les valeurs des propriétés de l'objet `staff`.

```js
   staff2.age = 53;

   console.log(staff)

   console.log(staff2)
```

La valeur de `staff2.age` qui a été changée en `53` n'affecte en aucun cas la valeur de `staff.age` car ils ont tous les deux leurs propres propriétés.

### Comment l'opérateur `Spread` fonctionne

Voici la syntaxe de l'opérateur spread :

```js
   const newObj = {...obj}

```

Utiliser l'opérateur `spread` est assez simple. Vous devez placer trois points `...` avant le nom de l'objet dont vous souhaitez cloner les propriétés :

```js
   const staff = {
    name: "Strengthened",
    age: 43,
    Hobbies: ["reading", "Swimming"]
   }

   const staff2 = {...staff};


   staff2.age = 53;

   console.log(staff)

   console.log(staff2)

```

![cloning](https://www.freecodecamp.org/news/content/images/2023/04/cloning.png)


## Qu'est-ce que l'Immuabilité en JavaScript ?

L'immuabilité est l'état où les valeurs sont immuables (c'est-à-dire qu'elles ne peuvent pas être changées). Une valeur est immuable lorsqu'il est impossible de la modifier. Les types de données primitifs sont immuables, comme nous l'avons discuté ci-dessus.

Examinons un exemple :

```js
   const num = 46;
   const newNum = num;

```

En regardant le code ci-dessus, `num` a été réassigné à `newNum`. Maintenant, `num` et `newNum` ont tous les deux une valeur de `46`. Changer la valeur de `newNum` ne modifiera pas la valeur de `num`.

```js
      let student1 = "Halina";

      let student2 = student1;
```

Dans le code ci-dessus, une variable appelée `student1` a été créée et assignée à `student2`.

```js
      student1 = "Brookes"

      console.log(student1);

      console.log(student2)
```

Changer `student1` en `Brookes` ne change pas la valeur initiale de `student2`. Cela prouve que dans les types de données primitifs, les valeurs réelles sont copiées, donc les deux ont leurs propres valeurs. Dans la mémoire de la pile, `student1` et `student2` sont distincts. 

La pile obéit au principe `Dernier Entré, Premier Sorti`. Le premier élément qui entre dans la pile est le dernier à en sortir et vice versa. Accéder aux éléments stockés dans la pile est facile.

![primitive-1](https://www.freecodecamp.org/news/content/images/2023/04/primitive-1.png)

## Comment Empêcher la Mutabilité des Objets 

Jusqu'à présent, vous avez appris que les objets sont mutables par défaut.

```js
   const studentNames = {
           student1: 'Halina',
           student2: "Brookes",
           student3:"Anthony"
   }


   Object.defineProperty(studentNames, "student4", {
      value: "Mirabel",
   })

   console.log(studentNames);
```

Maintenant, nous avons ajouté `student4`.

Pour empêcher la mutabilité des objets, vous pouvez utiliser les méthodes `Object.preventExtensions()`, `Object.seal()` et `Object.freeze()`.

Pour les trois méthodes, nous allons explorer l'ajout de propriétés en utilisant la notation par points et la propriété `define`, la modification de propriétés en utilisant defineProperty, et la suppression de propriétés. 

Cela vous donnera une meilleure compréhension des capacités et des limitations de chaque méthode, et vous aidera finalement à déterminer quelle méthode peut être la mieux adaptée à un cas d'utilisation particulier. 

Alors, plongeons-nous et explorons ces méthodes plus en détail.


### Comment Utiliser la Méthode `Object.preventExtensions`

Voici la syntaxe de cette méthode :

`Object.preventExtensions(obj)`

L'utilisation de `Object.preventExtensions` empêche l'ajout de nouvelles propriétés à l'objet. L'objet ne voit pas sa taille augmenter et conserve ses propriétés. Par défaut, tous les objets en JavaScript sont extensibles. Avec cette méthode, vous pouvez supprimer des propriétés de votre objet.

#### Comment ajouter de nouvelles propriétés


* en utilisant la `notation par points` :


```js
   const makeNonExtensive = {
           firstname: "Charles",
           lastname: "Chandlier"
   }

   Object.preventExtensions(makeNonExtensive)

   makeNonExtensive.designation = "Software Engineer";
   
   console.log(makeNonExtensive)

```

Vérifiez la console – la propriété `designation` n'a pas été ajoutée et il n'y a pas de message d'erreur.

```js
   const obj = {
           firstname: "Derek",
           designation: "Software Engineer"
   }
```   

* en utilisant la méthode `defineProperty`
   
Voici la syntaxe :
   
```js
   Object.defineProperty(obj, prop, descriptor)
```

Voici ce qui se passe dans ce code :
   
- `obj` : L'objet auquel vous souhaitez ajouter des propriétés.
- `prop` : Vous définissez le nom de la propriété que vous souhaitez ajouter ou modifier. Il doit être une chaîne de caractères ou un symbole.
- `Descriptor` : Vous incluez la valeur de la propriété.


```js
   const makeNonExtensive = {
           firstname: "Charles",
           lastname: "Chandlier"
   }

   Object.preventExtensions(makeNonExtensive)

   Object.defineProperty(makeNonExtensive, "age", {
      value: "twenty",
   })

   console.log(makeNonExtensive)
```

- L'ajout de nouvelles propriétés en utilisant la propriété define génère ce message d'erreur : `index.js:361 Uncaught TypeError: Cannot define property age, object is not extensible`.

![define-prop-cons](https://www.freecodecamp.org/news/content/images/2023/04/define-prop-cons.png)

#### Comment modifier une propriété existante en utilisant `define Property`

```js
    const makeNonExtensive = {
            firstname: "Charles",
            lastname: "Chandlier"
    }

   Object.preventExtensions(makeNonExtensive)

   Object.defineProperty(makeNonExtensive, 'firstname', {
    value: 'Jason',
    })
    console.log(makeNonExtensive)
```

La valeur de la propriété d'un objet non extensible peut être modifiée comme démontré avec la ligne de code ci-dessus.

![modify-pext-1](https://www.freecodecamp.org/news/content/images/2023/04/modify-pext-1.png)


#### Comment supprimer une propriété

Voici la syntaxe :

```
   delete object.propertyname
```

```js
   const makeNonExtensive = {
           firstname: "Charles",
           lastname: "Chandlier"
   }

   Object.preventExtensions(makeNonExtensive)

   delete makeNonExtensive.lastname

   console.log(makeNonExtensive)

```

Malgré le fait que l'objet soit non extensible, la propriété `lastname` a été supprimée.

![pExtension-del-1](https://www.freecodecamp.org/news/content/images/2023/04/pExtension-del-1.png)


### Comment Utiliser `Object.seal()`

Tous les objets en Javascript sont extensibles par défaut. Comme le suggère le nom, cette méthode scelle un objet. Vous ne pouvez pas ajouter de nouvelles propriétés à un objet scellé ou supprimer une propriété existante d'un objet scellé. Mais `object.seal` permet de modifier les propriétés existantes.

Voici la syntaxe :

```
Object.seal()
```

#### Comment ajouter de nouvelles propriétés

```js
   const studentNames = {
           student1: 'Halina',
           student2: "Brookes", 
           student3:"Alina"
   }

   Object.seal(studentNames)

   console.log(Object.isSealed(studentNames))
```

`Object.isSealed(studentNames)` est utilisé pour vérifier si un objet est scellé.

#### Comment utiliser la `notation par points`

```js
   studentNames.student4 = "Barbara";

   console.log(studentNames)
```

Sans produire d'erreur, la notation par points échoue lors de l'ajout de la nouvelle propriété `student4`. 
  
#### Comment utiliser la méthode `defineProperty`
  
  ```js
      const studentNames = {
              student1: 'Halina',
              student2: "Brookes",
              student3:"Alina"
      }

      Object.seal(studentNames)

      Object.defineProperty(studentNames, 'student4', {
         value: 'Barbara'
      })

      console.log(studentNames)

  ```

Le message d'erreur "Uncaught TypeError: Cannot define property student4, the object is not extendable" est généré lorsque vous essayez d'ajouter la même propriété en utilisant la méthode `define property`.

![seal1-2](https://www.freecodecamp.org/news/content/images/2023/04/seal1-2.png)

#### Comment modifier une propriété existante en utilisant `define Property`
  
```js
   
      const studentNames = {
              student1: 'Halina',
              student2: "Brookes",
              student3:"Alina"
      }

         Object.seal(studentNames)

      Object.defineProperty(studentNames, 'student2', {
         value: "Water-Brookes",
      })

      console.log(studentNames)

```

Maintenant, `student2` a été changé de "Brookes" à "Water-Brookes".

![seal2](https://www.freecodecamp.org/news/content/images/2023/04/seal2.png)

#### Comment supprimer une propriété

```js
   const studentNames = {
           student1: 'Halina',
           student2: "Brookes",
           Student3:"Alina"
   }

   Object.seal(studentNames)

   delete studentNames.student1

   console.log(studentNames)
 
```

Les propriétés ne peuvent pas être supprimées des objets scellés. Dans la console, student1 reste toujours.

![seal3-2](https://www.freecodecamp.org/news/content/images/2023/04/seal3-2.png)


### Comment Utiliser `Object.freeze()`

Voici la syntaxe :

```
   Object.freeze()
```

La méthode `Object.freeze()` gèle un objet. L'utilisation de cette méthode garantit une haute intégrité en s'assurant qu'il ne sera pas possible de retirer, modifier des propriétés existantes ou ajouter de nouvelles propriétés à l'objet. 

Pour vérifier si un objet est gelé, utilisez la syntaxe ci-dessous :

```
   Object.isFrozen(obj);
```

Même lorsque vous appliquez `object.freeze` à un objet, vous pouvez ajouter une nouvelle propriété, modifier une propriété existante ou supprimer des propriétés des objets imbriqués sous celui-ci. 

Comme nous l'avons fait pour les autres méthodes, explorons la méthode object.freeze en relation avec l'ajout de nouvelles propriétés, la modification de valeurs ou la suppression de propriétés d'un objet.


#### Comment ajouter de nouvelles propriétés

* En utilisant la `notation par points`

```js
   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance"
   }


   Object.freeze(teamplayers)

   teamplayers.player3 = "Finder";

   console.log(teamplayers)

```

![freeze-dot](https://www.freecodecamp.org/news/content/images/2023/04/freeze-dot.png)

Remarquez que `player3` n'a pas été ajouté.

* En utilisant la méthode `defineProperty`

```js
   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance"
   }


   Object.freeze(teamplayers)

   Object.defineProperty(teamplayers, 'player3', {
      value: 'Charis'
      })
      console.log(teamplayers)

   console.log(teamplayers)

```

La notation par points échoue silencieusement lors de la tentative d'ajout d'une propriété, mais `defineproperty` génère une TypeError à la place.

![freeze1](https://www.freecodecamp.org/news/content/images/2023/04/freeze1.png)


#### Comment modifier une propriété existante


```js
   
   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance"
   }


   Object.freeze(teamplayers)


   teamplayers.player1 = "Christabel"

   console.log(teamplayers)
```

![freeze2](https://www.freecodecamp.org/news/content/images/2023/04/freeze2.png)

Cela échouera silencieusement. Mais avec la propriété define ci-dessous, une `typeError` est générée.
 
```js
   
      const teamplayers = {
              player1: "Andrey",
              player2: "Abundance"
      }


      Object.freeze(teamplayers)


      Object.defineProperty(teamplayers, 'player1', {
         value: "Anne"
      })

      console.log(teamplayers)
```

 `Uncaught TypeError: Cannot redefine property: player1`


![freeze3](https://www.freecodecamp.org/news/content/images/2023/04/freeze3.png)

#### Comment supprimer une propriété

```js

   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance"
   }


   Object.freeze(teamplayers)


   delete teamplayers.player2

   console.log(teamplayers)

```

Tenter de supprimer une propriété d'un objet gelé échoue également silencieusement.

![freeze4](https://www.freecodecamp.org/news/content/images/2023/04/freeze4.png)

#### Comment utiliser Deep Freeze

```js
  
   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance",
                   substitutes: {
                   player3: "Jeremiah",
                   player4: "Jayden"
            }
   }

   const squad = teamplayers;

   Object.freeze(teamplayers)


   Object.defineProperty(teamplayers.substitutes, 'player5', {
      value: "Woodland"
   })

   console.log(teamplayers)


```

Player5 a été ajouté aux `substitutes` imbriqués même si la méthode `object.freeze` a été appliquée au parent `teamplayers`.

![deep1](https://www.freecodecamp.org/news/content/images/2023/04/deep1.png)

Vous pouvez également modifier la valeur des propriétés dans l'objet imbriqué.

- Comment supprimer une propriété

```js
   delete teamplayers.substitutes.player3

   console.log(teamplayers)
```

Player3 a été supprimé. Tout ce que object.freeze empêche sur l'objet parent est possible sur l'objet enfant qui est imbriqué.

![deep2](https://www.freecodecamp.org/news/content/images/2023/04/deep2.png)

Pour empêcher cela, nous employons la technique de gel profond comme montré ci-dessous :

```js
   const deepVal = obj => {
        Object.keys(obj).forEach(prop => {
        if (typeof obj[prop] === 'object') deepVal(obj[prop]);
        });
        return Object.freeze(obj);
    };

    const teamplayers = deepVal( {
            player1: "Andrey",
            player2: "Abundance",
                    substitutes: {
                        player3: "Jeremiah",
                        player4: "Jayden"
                    }
            }
    )
   const squad = teamplayers;

   Object.freeze(teamplayers)
   
   console.log(Object.isFrozen(teamplayers));
   
   console.log(Object.isFrozen(squad));


```

- Comment ajouter une nouvelle propriété à l'objet enfant.
  
```js
   
const deepVal = obj => {
        Object.keys(obj).forEach(prop => {
        if (typeof obj[prop] === 'object') deepVal(obj[prop]);
        });
        return Object.freeze(obj);
 };

    const teamplayers = deepVal( {
            player1: "Andrey",
            player2: "Abundance",
                    substitutes: {
                        player3: "Jeremiah",
                        player4: "Jayden"
                    }
            }
    )

   Object.freeze(teamplayers)

   Object.defineProperty(teamplayers.substitutes, 'player5', {
      value: "Alice"
   })

   console.log(teamplayers)

```

Maintenant, lorsque vous essayez d'ajouter une propriété, vous obtiendrez cette erreur `Uncaught TypeError: Cannot define property player5, object is not extensible`

![deep-addd-1](https://www.freecodecamp.org/news/content/images/2023/04/deep-addd-1.png)

De plus, le gel profond vous empêche de changer et de supprimer les propriétés d'un objet.

## const != Immuabilité

Une variable déclarée en utilisant le mot-clé `let` peut être réassignée en utilisant l'opérateur d'assignation (`=`). Regardez le code ci-dessous pour comprendre ce que je veux dire.

```js
   let num = 34;
   num = 50;

   console.log(num);
```

Ici, après avoir déclaré la variable `num` en utilisant le mot-clé `let`, la valeur a été réassignée de 34 à 50.

Cependant, vous ne pouvez pas faire la même chose sur la même variable déclarée en utilisant le mot-clé `const`. 

```js
 const num = 34;
 num = 50;

 console.log(num);

```

Vous obtiendrez cette erreur `Uncaught TypeError: Assignment to constant variable`.

Mais ce n'est pas le cas avec les objets. Un objet que vous avez déclaré en utilisant `const` est toujours mutable, donc vous pouvez toujours modifier les propriétés de cet objet particulier comme vous pouvez le voir ci-dessous :


```js
   const getObj = {
           color1: "Green",
           color2: "Blue",
           color3: "Yellow"
   }

   getObj.color1 = "Brown";
   
   console.log(getObj.color1) 

```

La valeur de `color1` a été modifiée de `Green` à `Brown`, même lorsqu'elle a été déclarée avec `const`.


## Réflexions Finales
Vous avez maintenant appris les différents types de données et s'ils sont immuables ou mutables par défaut. 

Les objets peuvent être modifiés par défaut. Mais en utilisant des méthodes spécifiques comme Object.seal, Object.freeze et preventExtensions, vous pouvez empêcher la mutabilité. 

Le niveau d'immuabilité fourni par ces méthodes varie, alors assurez-vous d'utiliser celle qui correspond au niveau d'intégrité que vous souhaitez atteindre. Jusqu'à la prochaine fois, continuez à explorer JavaScript.