---
title: Comment créer une bibliothèque d'utilités JavaScript comme Lodash
subtitle: ''
author: Gideon Akinsanmi
co_authors: []
series: null
date: '2023-08-08T21:15:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-javascript-utility-library-like-lodash
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/inaki-del-olmo-NIJuEQw0RKg-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment créer une bibliothèque d'utilités JavaScript comme Lodash
seo_desc: 'A utility library is a library that helps you streamline the implementation
  of common coding tasks. With it, you only need to focus on writing code that makes
  your project unique.

  One of the most popular JavaScript utility libraries is Lodash. Lodash...'
---

Une bibliothèque d'utilités est une bibliothèque qui vous aide à rationaliser la mise en œuvre de tâches de codage courantes. Avec elle, vous n'avez besoin de vous concentrer que sur l'écriture de code qui rend votre projet unique.

L'une des bibliothèques d'utilités JavaScript les plus populaires est Lodash. Lodash est une bibliothèque JS avec plus de 40 millions de téléchargements hebdomadaires sur npm. Elle aide à fournir des fonctionnalités supplémentaires aux objets JS vanilla préexistants. Lodash utilise une approche de programmation fonctionnelle pour implémenter des tâches courantes en JavaScript.

Bien que cette bibliothèque soit excellente, son utilisation dans des projets plus petits peut être excessive, surtout si vous n'avez besoin que de 3 ou 4 fonctionnalités. Avec une taille de package de plus de [1,4 Mo](https://www.npmjs.com/package/lodash) comprenant plus de 1000 fichiers et 500 fonctions, avoir Lodash sur votre front-end peut nuire aux performances de votre site web.

Dans cet article, je vais vous montrer comment implémenter certaines des fonctionnalités clés fournies par Lodash. À la fin de ce tutoriel, vous saurez non seulement comment implémenter la fonctionnalité d'une bibliothèque populaire, mais vous verrez également une amélioration de vos compétences en JavaScript.

## Prérequis
Pour cet article, tout ce dont vous avez besoin est un éditeur de code, un navigateur web et une connaissance de base de JavaScript.

## Table des matières
1. [Installation du projet](#heading-installation)
2. [Comment créer des méthodes de tableau](#heading-comment-creer-des-methodes-de-tableau)
    1. [La méthode _.chunk()](#heading-la-methode-chunk)
    2. [La méthode _.compact()](#heading-la-methode-compact)
    3. [La méthode _.concat()](#heading-la-methode-concat)
    4. [La méthode _.drop()](#heading-la-methode-drop)
    5. [La méthode _.dropRight()](#heading-la-methode-dropright)
    6. [La méthode _.fill()](#heading-la-methode-fill)
    7. [La méthode _.flatten()](#heading-la-methode-flatten)
    8. [La méthode _.intersection()](#heading-la-methode-intersection)
    9. [La méthode _.remove()](#heading-la-methode-remove)
    10. [La méthode _.union()](#heading-la-methode-union)
3. [Comment créer des méthodes de collection](#heading-comment-creer-des-methodes-de-collection)
    1. [La méthode _.filter()](#heading-la-methode-filter)
    2. [La méthode _.find()](#heading-la-methode-find)
    3. [La méthode _.partition()](#heading-la-methode-partition)
    4. [La méthode _.shuffle()](#heading-la-methode-shuffle)
4. [Comment créer des méthodes mathématiques](#heading-comment-creer-des-methodes-mathematiques)
    1. [La méthode _.mean()](#heading-la-methode-mean)
    2. [La méthode _.max()](#heading-la-methode-max)
    3. [La méthode _.min()](#heading-la-methode-min)
    4. [La méthode _.sum()](#heading-la-methode-sum)
5. [Comment créer des méthodes d'objet](#heading-comment-creer-des-methodes-dobjet)
    1. [La méthode _.keys()](#heading-la-methode-keys)
    2. [La méthode _.values()](#heading-la-methode-values)
6. [Comment créer des méthodes de chaîne](#heading-comment-creer-des-methodes-de-chaine)
    1. [La méthode _.repeat()](#heading-la-methode-repeat)
    2. [La méthode _.split()](#heading-la-methode-split)
7. [Conclusion](#heading-conclusion)

## Installation du projet
La première chose à faire est de créer un dossier appelé `projet-lodash` qui contient un fichier HTML et un fichier JavaScript. 

Le fichier JavaScript contiendra le code, tandis que notre fichier HTML sera utilisé pour lier les fichiers ensemble. 

Vous pouvez leur donner n'importe quel nom valide que vous souhaitez, mais je vais rester avec `index.html` et `index.js`.

Dans le fichier HTML, vous ajouterez l'élément script pour lier avec votre fichier index.js.

Voici le code pour `index.html` :

```html
<!DOCTYPE HTML>
<html>
      <head>
             <title>Projet Lodash</title>
      </head>
      <body>
             <script src='index.js'></script>
      </body>
</html>
```

Dans le fichier JavaScript (index.js), nous allons utiliser une classe JavaScript (`_`) et des méthodes statiques (dont le nom sera les méthodes Lodash que nous allons implémenter) pour structurer notre code.

Voici le format qu'il devrait avoir :

```javascript
class _ {
    static nom_de_la_methode(){
        //code
    }
}
```

À partir de ce point, je vais vous montrer comment implémenter 10 méthodes de tableau Lodash, quatre méthodes de collection, quatre méthodes mathématiques, deux méthodes d'objet et deux méthodes de chaîne. Êtes-vous prêt ? C'est parti !

## Comment créer des méthodes de tableau

### La méthode `_.chunk()`

Tout d'abord, nous verrons comment implémenter la méthode `_.chunk()`. Dans Lodash, la méthode chunk vous aide à diviser le contenu de votre tableau en groupes. 

Cette méthode est utile lorsque vous souhaitez afficher une longue liste d'éléments dans une interface utilisateur paginée. 

En appliquant la méthode `chunk()`, vous pouvez diviser le tableau en tableaux plus petits, chacun contenant un nombre fixe d'éléments. Cela vous permet de gérer efficacement l'affichage des éléments page par page, améliorant l'expérience utilisateur et minimisant le temps de chargement.

Elle peut également être utilisée pour traiter des données qui doivent être traitées en parallèle ou par lots.

Selon la [documentation de Lodash](https://lodash.com/docs/#chunk), voici comment cela fonctionne : 

```javascript
//divise le tableau en un groupe de 2
_.chunk(['a', 'b', 'c', 'd'], 2);
//retourne [ ['a', 'b'], ['c', 'd'] ]
 
//divise le tableau en un groupe de 3 et décale le reste dans un autre
_.chunk(['a', 'b', 'c', 'd'], 3);
//retourne [ ['a', 'b', 'c'], ['d'] ]
```

Voici comment l'implémenter vous-même : 

```javascript
class {
     //... autres méthodes
     
      static chunk(array, size=1){
             let newArray = [];  
             for(let i = 0; i < array.length; i += size){ 
                    let chunk = array.slice(i, i + size);
                    newArray.push(chunk) 
             } 
             return newArray;                        
      }
}
```

Dans le code ci-dessus, la première étape consiste à créer une méthode statique `chunk()` avec un paramètre `array` et `size`. Le paramètre `size` reçoit une valeur par défaut de 1. 

Ensuite, nous créons un tableau vide (`newArray`) qui stockera les chunks divisés. Puis nous utiliserons des boucles et la méthode `array.slice()` pour extraire des chunks du tableau original et les pousser dans le nouveau tableau (`newArray`). 
 
### La méthode `_.compact()`

Maintenant, regardons la méthode `_.compact()`. Dans Lodash, la méthode `compact()` retourne un tableau avec tous les éléments falsy supprimés. Des exemples de valeurs falsy sont `undefined`, `null`, `''`, `false`, `0`, etc.

Cette méthode est utile lorsque vous souhaitez nettoyer un tableau et vous concentrer sur des valeurs significatives et non vides.

Vous pouvez également l'utiliser pour nettoyer des tableaux qui ont des données incomplètes ou des informations non pertinentes.

Selon la [documentation de Lodash](https://lodash.com/docs/#compact), voici comment cela fonctionne :

```javascript
let rapportEnquete = ['oui', 'non', 'pas sûr', null, 'non', ''];

//supprime les éléments falsy
_.compact(rapportEnquete);
//retourne ['oui', 'non', 'pas sûr', 'non']
```

Voici comment l'implémenter vous-même :

```javascript
class _ {
      //... autres codes
      static compact(array){
             let newArray = array.filter( val => {return Boolean(val) === true})
             return newArray;
      }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `compact()` avec un paramètre `array`. Ensuite, nous avons utilisé la méthode `array.filter()` et la fonction `Boolean()` pour filtrer les valeurs qui sont truthy, et non falsy. 
 
### La méthode `_.concat()`

Dans Lodash, la méthode `concat()` est utilisée pour concaténer deux ou plusieurs tableaux ou valeurs. Cela est particulièrement utile lorsque vous traitez des données provenant de différentes sources et que vous souhaitez les présenter dans une vue complète.

Imaginez un scénario où vous avez plusieurs tableaux contenant des informations connexes, telles que des noms de clients, des adresses et des détails de commande. La méthode `concat()` vous permet de combiner facilement ces tableaux, créant un ensemble de données unifié qui peut être facilement traité ou affiché.

Selon la [documentation de Lodash](https://lodash.com/docs/#concat), voici comment cela fonctionne : 
 
```javascript
let tableau = [1, 2];
let autre = _.concat(tableau, 4, [1], [ [12, true] ] );
 
console.log(autre)
//retourne [ 1, 2, 4, 1, [12, true] ]
```

Voici comment l'implémenter vous-même :

```javascript
class _ {
      //...autres méthodes
      
      static concat(array, ...values){
                          
             for(let i = 0; i < values.length; i++){
                    array = array.concat( values[i] ) 
             } 
             return array;
      }
}
```

Dans le code ci-dessus, j'ai créé une méthode statique `concat()` avec un paramètre `array` et `values`. Le paramètre sera traité comme un tableau représentant les différents tableaux/valeurs que nous allons concaténer. 

Ensuite, nous avons utilisé la boucle for et la méthode `array.concat()` pour concaténer chaque élément dans le paramètre values à notre paramètre array.
 
### La méthode `_.drop()`

La méthode `drop()` retourne un tableau avec certains de ses éléments supprimés du début.
 
La méthode `drop()` joue un rôle crucial dans la mise en œuvre d'un comportement de type pile avec des tableaux. Vous pouvez utiliser cette méthode pour vous assurer que seules les tâches les plus récentes sont prioritaires.

Selon la [documentation de Lodash](https://lodash.com/docs/#drop), voici comment cela fonctionne :

```javascript
//supprime le premier élément et retourne le reste
_.drop([1,2,3])
//=> [2,3]
 
//supprime les deux premiers éléments et retourne le reste
_.drop([1,2,3,4], 2)
//=> [3,4]
 
//supprime les trois premiers éléments et retourne le reste
_.drop([2,4,6], 3)
//=> []
 ```
 
Voici comment l'implémenter vous-même :

```javascript
class _ {
    //autres méthodes
    
    static drop(array, n=1){
           return array.slice(n, array.length) 
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `drop()` avec un paramètre `array` et `n`. `array` représente le tableau dont les éléments seront supprimés tandis que `n` représente le nombre d'éléments à supprimer du début. 

Ensuite, nous avons utilisé une méthode `array.slice()` pour retourner un tableau commençant à la position `n` jusqu'au dernier élément.

### La méthode `_.dropRight()`

La méthode `dropRight()` retourne un tableau avec certains de ses éléments supprimés de la fin.
 
La méthode `drop()` joue un rôle crucial dans la mise en œuvre d'un comportement de type file d'attente avec des tableaux. Vous pouvez utiliser cette méthode pour vous assurer que seules les tâches les plus anciennes sont prioritaires.

Selon [Lodash](https://lodash.com/docs/#dropRight), voici comment cela fonctionne :

```javascript
//supprime le dernier élément et retourne le reste
_.dropRight([1,2,3,4]) 
 
//supprime les deux derniers éléments et retourne le reste
_.dropRight([1,2,3,4], 2)
//[2, 3]
```

Voici comment l'implémenter vous-même :

```javascript
class _ {
    //autres méthodes ...
    
     static dropRight(array, n=1){
           return array.slice(0, -n)
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `dropRight()` avec un paramètre `array` et `n`. `array` représente le tableau dont les éléments seront supprimés tandis que `n` représente le nombre d'éléments à supprimer de la fin. 

Ensuite, nous utilisons la méthode `array.slice()` pour retourner un tableau commençant à la position 0 jusqu'à (mais sans inclure) -`n`.
 
### La méthode `_.fill()`

La méthode `fill()` remplit un tableau avec une valeur spécifique.
 
Imaginez que vous avez un tableau représentant un plateau de jeu où certaines cellules doivent être marquées comme occupées. En utilisant la méthode `fill()`, vous pouvez efficacement remplacer une plage de cellules par une valeur de marqueur, indiquant leur statut.

Selon [Lodash](https://lodash.com/docs/#fill), voici comment cela fonctionne :

```javascript
let plateau = Array(9);
 
//remplace ou remplit tous les éléments du tableau avec '0'
_.fill(tableau, 0);
console.log(tableau)
//retourne [0, 0, 0, 0, 0, 0, 0, 0, 0];
 
let tableau = [1,3,5,7];
//remplace ou remplit le tableau avec 'hello' de l'index 0 à (mais sans inclure) l'index 3
_.fill(tableau, 'hello', 0, 3)

console.log(tableau)
//retourne ['hello', 'hello', 'hello', 7];
```

Voici comment l'implémenter vous-même :

```javascript
class _ {
    //autres méthodes ...
    
     static fill(array, value, start=0, end=array.length){ 
           for(let i = start; i < end; i++){ 
                 array[i] = value 
           } 
           return array;    
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `fill()` avec un paramètre `array`, `value`, `start` et `end`. 

`array` représente le tableau dont les éléments seront remplis. `value` est la valeur qui remplira/remplacera les éléments dans le tableau. `start` est la position à partir de laquelle le remplissage commence. Il a une valeur par défaut de 0. `end` représente la position à laquelle le remplissage se terminera. Sa valeur par défaut est `array.length`. 

Dans la méthode, nous avons créé une boucle qui change la valeur de chaque élément en `value`.

### La méthode `_.flatten()`

La méthode `flatten()` aplatit un tableau d'un niveau de profondeur.

Imaginez que vous avez un tableau contenant des sous-tableaux représentant différentes catégories d'éléments. En appliquant la méthode `flatten()`, vous pouvez fusionner sans effort ces sous-tableaux en un seul tableau, simplifiant le processus d'itération, de recherche ou d'exécution d'opérations sur l'ensemble de données combiné. 

Selon la [documentation de Lodash](https://lodash.com/docs/#flatten), voici comment cela fonctionne :

```javascript
_.flatten([['James'], [17], ['Male']]);
//-> ['James', 17, 'Male']
```

Voici comment l'implémenter :

```javascript
class _ {
    //... autres méthodes
    
     static flatten(array){
           return [].concat(...array);
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `flatten()` avec un argument `array`. Ensuite, nous avons utilisé l'opérateur de propagation et `array.concat()` pour concaténer un tableau vide avec l'itérable développé.

### La méthode `_.intersection()`

La méthode `intersection()` retourne un tableau qui contient des valeurs présentes dans tous les tableaux donnés.

Imaginez que vous avez plusieurs tableaux contenant des préférences d'utilisateurs pour différentes fonctionnalités de votre application. En utilisant la méthode `intersection()`, vous pouvez facilement déterminer quelles préférences sont communes à tous les utilisateurs, vous aidant ainsi à identifier les fonctionnalités les plus populaires ou préférées. 

Selon la [documentation de Lodash](https://lodash.com/docs/#intersection), voici comment cela fonctionne :

```javascript
let preference1 = ['Post', 'View', 'Comment'];
let preference2 = ['Like', 'Comment', 'Share'];

_.intersection(preference1, preference2)
retourne ['Comment']
```

Voici comment l'implémenter vous-même :

```javascript
class _ {
     //...autres méthodes
     
     static intersection(...arrays){ 
           if (arrays.length === 0){
                 return []
           }
           let intersection = arrays.reduce((prev, current) => {
                 return prev.filter((element) => current.includes(element) );
           })
                       
           return [...new Set(intersection)]; //supprime les doublons
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `intersection()` avec un paramètre `arrays` qui a un opérateur de propagation. Dans la fonction, nous retournerons un tableau vide si la méthode est appelée sans aucun paramètre. 

Ensuite, nous utilisons la méthode `reduce()` pour itérer récursivement sur les tableaux et filtrer les éléments communs à chaque étape, jusqu'à ce qu'elle trouve l'intersection de tous les tableaux. 

Ensuite, nous retournons le résultat final sous forme de tableau après avoir supprimé les doublons avec une fonction constructeur `Set`.

### La fonction `_.remove()`

La fonction `remove()` supprime certains éléments qui satisfont une condition et retourne le résultat. Elle supprime également définitivement ces éléments du tableau original. 

Par exemple, si vous avez un tableau de nombres et que vous souhaitez supprimer toutes les occurrences d'une certaine valeur, vous pouvez utiliser `remove()` pour y parvenir efficacement.

Selon la [documentation de Lodash](https://lodash.com/docs/#remove), voici comment cela fonctionne :

```javascript
let tableau = [1,2,3,4,5,6,7];

let impair = _.remove(tableau, function(){
     return n%2 !== 0
});

console.log(impair)
//[1,2,5,7]
     
console.log(tableau)
//retourne le reste => [2,4,6]
```

Voici comment l'implémenter vous-même :

```javascript
class _ {
     //... autres méthodes
     
     static remove(array, predicate){
           let truthy = array.filter(predicate);
           for(let i of truthy){
                 let n = array.indexOf(i)
                 array.splice(n, 1); 
           } 
           return truthy;
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `remove()` qui contient deux paramètres : `array` et `predicate`. `array` fait référence au tableau dont les éléments seront supprimés tandis que `predicate` est une fonction qui spécifiera les conditions que les éléments doivent passer pour être supprimés.

Ensuite, nous utilisons la méthode `array.filter()` pour filtrer les éléments qui passent les conditions. Puis nous avons utilisé des boucles et `array.splice()` pour supprimer l'élément passé du tableau original. Enfin, nous retournons le tableau truthy.

### La méthode `_.union()`

La méthode `union()` retourne un tableau de valeurs uniques à partir d'un ou plusieurs tableaux.

Imaginez que vous avez plusieurs tableaux représentant différentes catégories d'éléments, et que vous souhaitez les combiner en un seul tableau sans répéter aucun élément. En utilisant la méthode `union()`, vous pouvez facilement fusionner ces tableaux, en vous assurant que chaque valeur n'apparaît qu'une seule fois dans le tableau résultant.

Cela est précieux lorsque vous traitez des données provenant de diverses sources qui peuvent contenir des informations chevauchantes.

Selon [Lodash](https://lodash.com/docs/#union), voici comment cela fonctionne :

```javascript
let panier1 = ['Œuf', 'Chaussure', 'Lait'];
let panier2 = ['Chaussure, 'Lait', 'Miel'];

let tousLesPaniers = _.union(panier1, panier2)
console.log(tousLesPaniers)
//['Œuf', 'Chaussure', 'Lait', 'Miel']
```

Voici comment l'implémenter vous-même :

 ```javascript
class _ {
    //autres méthodes ...
    
    static union(...arrays){
          let total = []
          for(let i of arrays){
                total.push(...i)
          }
          return new Set(total);
    }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `union()` avec un paramètre `arrays` qui a un opérateur de propagation. Nous avons créé une variable stockant un tableau vide et utilisé la boucle `for-of` pour pousser les éléments dans le paramètre `arrays` vers `total`. 

Ensuite, nous insérons la variable total dans une fonction `Set` pour supprimer les doublons et la retourner.

## Comment créer des méthodes de collection

### La méthode `_.filter()`

Dans Lodash, la méthode `filter()` retourne un tableau d'éléments qui satisfont une condition. Contrairement à `remove()`, elle ne modifie pas le tableau original.

Ses applications vont du filtrage de données à la création de sous-ensembles personnalisés. 

Par exemple, si vous avez un tableau d'objets représentant des utilisateurs, et que vous souhaitez récupérer tous les utilisateurs qui sont actifs. En utilisant la méthode `filter()`, vous pouvez efficacement créer un nouveau tableau contenant uniquement les utilisateurs actifs.

Un autre exemple est l'utilisation de cette méthode pour des scénarios de transformation de données. Si vous avez un tableau de valeurs numériques et que vous souhaitez extraire uniquement les nombres pairs, vous pouvez facilement y parvenir en appliquant la méthode `filter()` avec une fonction de filtrage personnalisée.

Selon la [documentation de Lodash](https://lodash.com/docs/#filter), voici comment cela fonctionne :

```javascript
let utilisateurs = [
    {nom: 'Zoe', age: 24, actif: false},
    {nom: 'Aisha', age: 20, actif: true},
    {nom: 'Alex', age: 19, actif: true}
];
filter(utilisateurs, function(element){ return element.actif > true})

//retourne => [
    {nom: 'Aisha', age: 20, actif: true},
    {nom: 'Alex', age: 19, actif: true}
]
 ```
 
Voici comment l'implémenter vous-même :

```javascript
class _ {
     //... autres méthodes
    
     static filter(collection, predicate){
           return collection.filter(predicate);
    }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `filter()` avec un paramètre `array` et `predicate`. `array` est le tableau dont les éléments seront filtrés et `predicate` est la fonction qui contient les conditions que chaque élément doit passer pour être filtré. 

Ensuite, nous utilisons la méthode `array.filter()` pour filtrer le tableau et retourner le résultat.

### La méthode `_.find()`

La méthode `find()` retourne le premier élément d'un tableau qui satisfait une condition particulière.

Ses applications vont des recherches ciblées à la récupération efficace de données.

Par exemple, disons que vous avez un tableau d'objets représentant des produits dans une boutique en ligne, et que vous souhaitez trouver le premier produit qui est actuellement en vente. En utilisant la méthode `find()`, vous pouvez rapidement localiser l'objet produit souhaité qui correspond à la condition de vente.

La méthode `find()` joue également un rôle crucial dans les scénarios où vous devez rechercher un élément spécifique au sein d'une collection, comme trouver un utilisateur particulier par son nom d'utilisateur ou localiser un livre par son titre. 

Selon la [documentation de Lodash](https://lodash.com/docs/#find), voici comment cela fonctionne :

```javascript
let produits = [
     {nom: 'Riz', qty: 20},
     {nom: 'Œuf', qty: 24},
     {nom: 'Lait', qty: 19},
     {nom: 'Blé', qty: 20}
]

//trouve le premier produit dont la quantité est supérieure à 20
_.find(produits, function(produit){ return produit.qty > 20})
 
//retourne {nom: 'Œuf', qty: 24}
```

Voici comment l'implémenter vous-même :

```javascript
class _ {
    //... autres méthodes
    
     static find(collection, predicate, fromIndex=0){
           let ans = collection.slice(fromIndex, collection.length)
           return ans.find(predicate);
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `find()` avec 3 paramètres : `collection`, `predicate`, `fromIndex`. 

`collection` est le tableau que nous allons rechercher. `predicate` est une fonction contenant la condition que l'élément doit passer pour être retourné. `fromIndex` spécifie l'index à partir duquel commencer la recherche. 

Tout d'abord, nous avons utilisé la méthode `array.slice()` pour découper le tableau à partir d'une position de départ spécifiée par le paramètre `fromIndex` jusqu'à la fin de la collection. Ensuite, nous utilisons la méthode `array.find()` sur le tableau découpé et retournons le résultat.

### La méthode `_.partition()`

La méthode `partition()` crée un tableau composé de deux éléments. Le premier est un tableau d'éléments qui satisfont une certaine condition tandis que le second est un tableau d'éléments qui ne satisfont pas la condition.
 
Ses applications vont de la ségrégation des données à la création de sous-ensembles distincts.

Imaginez que vous avez un tableau de nombres, et que vous souhaitez séparer les nombres pairs des nombres impairs. En utilisant la méthode `partition()`, vous pouvez facilement créer deux tableaux : l'un contenant tous les nombres pairs et l'autre contenant tous les nombres impairs. Cela facilite l'exécution d'opérations ou d'analyses séparées sur chaque sous-ensemble.

De plus, la méthode `partition()` est bénéfique lorsque vous traitez des scénarios de filtrage et de catégorisation. Si vous avez une collection d'objets représentant des produits et que vous souhaitez les catégoriser en deux groupes - ceux qui sont en vente et ceux qui ne le sont pas - la méthode `partition()` offre une solution élégante.

Selon la [documentation de Lodash](https://lodash.com/docs/#partition), voici comment cela fonctionne :

 ```javascript
 let produits = [
     {nom: 'Lait', vendu: true},
     {nom: 'Crème', vendu: false},
     {nom: 'Bicyclette', vendu: true},
     {nom: 'Chaussettes', vendu: false}
 ];
 
_.partition(produits, function(e){ return e.vendu === true})
retourne [
     [
    {nom: 'Lait', vendu: true},
    {nom: 'Bicyclette', vendu: true}
],
     [
     {nom: 'Crème', vendu: false},
     {nom: 'Chaussettes', vendu: false}
]
]
 ```
 
Voici comment l'implémenter vous-même :

```javascript
class _ {
    //... autres méthodes
    
    static partition(collection, predicate){
        let truthy = array.filter(predicate);
        let falsy = collection;
        
        for(let i of truthy){
            let n = falsy.indexOf(i)
            falsy.splice(n, 1); 
        } 
        
        return [truthy, falsy];
    }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `partition()` avec un paramètre `collection` et `predicate`. `collection` est le tableau qui sera utilisé tandis que `predicate` est la fonction qui contient les conditions que les éléments doivent passer pour être partitionnés dans le premier élément. 

Tout d'abord, nous avons créé deux variables : `truthy` et `falsy`. `truthy` est un tableau contenant les éléments qui ont passé la condition tandis que `falsy` stocke la collection. 

Ensuite, nous avons utilisé une boucle `for-of` et la méthode `splice()` pour supprimer les éléments du tableau `falsy` de `truthy`. Et enfin, nous avons retourné un tableau contenant les deux tableaux `truthy` et `falsy`.

### La méthode `_.shuffle()`

La méthode `shuffle()` retourne un tableau mélangé en utilisant le mélange de Fisher-Yates.

Ses applications vont de l'amélioration de l'engagement des utilisateurs à l'introduction de l'aléatoire dans divers scénarios

Imaginez que vous avez un tableau de questions pour une application de quiz, et que vous souhaitez présenter les questions dans un ordre différent à chaque fois qu'un utilisateur passe le quiz. En utilisant la méthode `shuffle()`, vous pouvez facilement créer un nouveau tableau avec les questions dans un ordre aléatoire, offrant une expérience nouvelle pour les utilisateurs à chaque session de quiz.

Selon [Lodash](https://lodash.com/docs/#shuffle), voici comment cela fonctionne :

```javascript
let questionsQuiz = [1, 2, 3, 4, 5, 6, 7, 8];

_.shuffle(questionsQuiz)
//version mélangée par exemple [2,3,8,5,1,7,4,6]
 ```
 
Voici comment l'implémenter vous-même :

```javascript
class _ {
    //... autres méthodes
    
     static shuffle(collection){
           function sh(array=collection, shuffled=[], length=collection.length){
                 if(length === 0){
                      return shuffled;
                 }
                       
                 let rand = Math.floor( Math.random() * ( length - 1) );
                       
                 shuffled.push( array[rand] )
           
                length -= 1;
                       
                       array.splice(rand, 1);
                       
                 return sh(array, shuffled, length);
                       
           }
           return sh() 
                 
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `shuffle()` avec un paramètre `collection` qui représente le tableau à mélanger. À l'intérieur se trouve une autre fonction `sh()` qui utilise la récursivité pour mélanger le tableau.

## Comment créer des méthodes mathématiques

### La méthode `_.mean()`

Dans Lodash, la méthode `mean()` calcule la valeur moyenne des éléments d'un tableau.

Cette méthode peut être utilisée pour effectuer des analyses de données.

Imaginez que vous avez un tableau de scores de test, et que vous souhaitez connaître la moyenne des scores des étudiants. En utilisant la méthode `mean()`, vous pouvez calculer facilement la moyenne des scores de test, ce qui vous donne une idée de la performance globale du groupe.

De plus, la méthode `mean()` joue un rôle crucial dans l'analyse des données et les statistiques.

Que vous travailliez avec des données financières, des mesures scientifiques ou toute autre donnée numérique, le calcul de la moyenne vous aide à comprendre la valeur typique et à prendre des décisions éclairées basées sur la tendance centrale des données.

Selon la [documentation de Lodash](https://lodash.com/docs/#mean), voici comment cela fonctionne :

```javascript
let scoreMath = [60, 70, 50, 80];

_.mean(scoreMath)
retourne 65
```

Voici comment l'implémenter vous-même :

```javascript
class _ {
    //... autres méthodes
    
     static mean(array){
           let sum = array.reduce( (accumulator, current) => {
                 return accumulator + current
           }, 0);
           return sum/array.length;
    }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `mean()` avec un paramètre `array` qui représente le tableau dont les éléments nous utiliserons pour calculer la moyenne. 

Ensuite, nous utilisons la méthode `array.reduce()` pour trouver la somme de toutes les valeurs. 

Enfin, nous divisons le résultat par la longueur du tableau et le retournons.

### La méthode `_.max()`

La méthode `max()` retourne la valeur maximale dans un tableau.

Ses applications vont de l'identification des valeurs les plus élevées à la détection des valeurs aberrantes.

La méthode `max()` est cruciale dans les scénarios où vous devez identifier les valeurs extrêmes dans un ensemble de données.

Que vous analysiez des relevés de température, des prix des actions ou toute autre donnée numérique, trouver la valeur maximale peut vous aider à comprendre la plage et les valeurs aberrantes potentielles au sein des données.

Selon la [documentation de Lodash](https://lodash.com/docs/#max), voici comment cela fonctionne :

```javascript
let prixActions = [545, 230, 123, 1004, 890, 890];

_.max(prixActions)
//1004
```

Voici comment l'implémenter :

```javascript
class _ {
    //... autres méthodes
    
     static max(array){
           return Math.max(...array)
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `mean()` avec un paramètre `array` qui représente le tableau dont les éléments seront utilisés pour calculer la valeur maximale. 

Ensuite, nous utilisons l'opérateur de propagation et la fonction `Math.max()` pour calculer la valeur maximale.

### La méthode `_.min()`

La méthode `_.min()` retourne la valeur minimale dans un tableau.

La méthode `min()` est cruciale dans les scénarios où vous devez identifier la plus petite valeur dans un ensemble de données.

Que vous analysiez des prix, des durées ou toute autre donnée numérique, trouver la valeur minimale peut vous aider à comprendre la plage et les valeurs aberrantes potentielles au sein des données.

Selon la [documentation de Lodash](https://lodash.com/docs/#min), voici comment cela fonctionne :

```javascript
let prixProduit = [200, 150, 500, 230, 99];

_.min(prixProduit)
//retourne 99
```

Voici comment l'implémenter :
```javascript
class _ {
    //...autres méthodes
    
     static max(array){
           return Math.min(...array)
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `min()` avec un paramètre `array` qui représente le tableau dont les éléments seront utilisés pour calculer le minimum. 

Ensuite, nous utilisons l'opérateur de propagation et la fonction `Math.min()` pour calculer la valeur minimale.
 
### La méthode `_.sum()`

La méthode `sum()` calcule la somme de tous les éléments d'un tableau.

Cette méthode peut être utilisée pour calculer des valeurs agrégées.

Par exemple, la méthode `sum()` est cruciale dans les scénarios où vous devez déterminer la valeur agrégée d'un ensemble de données.

Que vous travailliez avec des transactions financières, des quantités ou toute autre donnée numérique, le calcul de la somme vous aide à comprendre l'ampleur globale des données.

Selon la [documentation de Lodash](https://lodash.com/docs/#sum), voici comment cela fonctionne :

```javascript
let ventes = [20000, 34000, 21000, 15000];

_.sum(ventes)
//retourne -> 90000
```

Voici comment l'implémenter :

```javascript
class _ {
    //... autres méthodes
    
     static sum(array){
           let total = array.reduce( (accumulator, current) => {
                 return accumulator + current
           }, 0);
           return total;
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `sum()` avec un paramètre `array`. Ensuite, nous avons utilisé la méthode `array.reduce()` pour additionner toutes les valeurs des éléments du tableau.

## Comment créer des méthodes d'objet

### La méthode `_.keys()`
	
Dans Lodash, la méthode `keys()` retourne un tableau contenant les propriétés d'un objet.

Imaginez que vous avez un objet représentant un profil utilisateur avec des propriétés comme nom, email et âge. En utilisant la méthode `keys()`, vous pouvez facilement extraire les noms des propriétés et travailler avec eux.

Selon la [documentation de Lodash](https://lodash.com/docs/#keys), voici comment cela fonctionne :

```javascript
retourne toutes les propriétés de l'objet
_.keys({nom: 'john', age: 7})
//['nom', 'age']
```

Voici comment l'implémenter :

```javascript
Class _{
     static keys(object){
           return Object.keys(object)
    }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `keys()` avec un paramètre `object` qui représente l'objet dont les propriétés seront extraites. 

Ensuite, nous utilisons la méthode `Object.keys()` pour extraire les propriétés et retourner le résultat.

### La méthode `_.values()`

La méthode `values()` retourne un tableau contenant les valeurs des propriétés d'un objet.

Imaginez que vous avez un objet représentant un profil utilisateur avec des propriétés comme nom, email et âge. En utilisant la méthode `values()`, vous pouvez facilement extraire les valeurs des propriétés et travailler avec elles.

Selon la [documentation de Lodash](https://lodash.com/docs/#values), voici comment cela fonctionne :

```javascript
//retourne les valeurs de l'objet
_.values({nom: 'john', age: 7})
//['john', 7]
```

Voici comment l'implémenter :
```javascript
class _{
     static values(){
           return Object.values(object)
    }
}
```

Dans le code ci-dessus, nous avons créé une méthode `values()` avec un paramètre `object` qui représente l'objet dont les valeurs des propriétés seront extraites. Ensuite, nous utilisons la méthode `Object.values()` pour extraire les valeurs et retourner le résultat.
 
## Comment créer des méthodes de chaîne

### La méthode `_.repeat()`

Dans Lodash, la méthode `repeat()` retourne une chaîne qui a été dupliquée un nombre spécifique de fois.

Ses applications vont de la création de motifs à la mise en forme de la sortie, ce qui en fait un outil pratique pour diverses tâches de manipulation de chaînes.

Par exemple, si vous souhaitez créer une ligne de séparation de tirets dans une sortie de console, vous pouvez utiliser la méthode `repeat()` pour générer le nombre nécessaire de tirets.

Selon [Lodash](https://lodash.com/docs/#repeat), voici comment cela fonctionne :

```javascript
//répète la chaîne '-' 10 fois

_.repeat('-', 10)
console.log('hello world')
_.repeat('-', 10)

//retourne:
//'----------'
//'hello world'
//'----------'
```

Voici comment l'implémenter :

```javascript
class _ { 
    //... autres méthodes
    
     static repeat(string='', n=1){
           let repeated ='';
                       
           for(let i = 0; i < n; i++){
                 repeated += string;
           }
           return repeated;
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode statique `repeat()` avec un paramètre string et n. `string` fait référence à la chaîne qui sera dupliquée tandis que `n` spécifie le nombre de fois qu'elle sera répétée.

Ensuite, nous avons créé une variable `repeated` qui stocke une chaîne vide. Et enfin, nous avons utilisé la boucle `for` pour concaténer la chaîne `n` fois.

### La méthode `_.split()`

La méthode `split()` divise une chaîne par un séparateur et stocke les parties dans un tableau.

Ses applications vont du traitement de texte à l'extraction de données.

La méthode `split()` peut être bénéfique dans les scénarios où vous traitez des données dans un format spécifique.

Par exemple, si vous avez une liste de valeurs dans une chaîne séparées par un signe plus (+), vous pouvez utiliser la méthode `split()` pour extraire chaque valeur et les stocker dans un tableau.

Selon la [documentation de Lodash](https://lodash.com/docs/#split), voici comment cela fonctionne :

```javascript
//Divise tous les caractères
_.split('hello', '')
['h', 'e', 'l', 'l', 'o']
 
//Divise en utilisant _ comme séparateur 
_.split('h_e_l_l_o', '_')
['h', 'e', 'l', 'l', 'o']
 
Divise la chaîne en utilisant + comme séparateur et limite les éléments à 2
_.split'`how+to+cook+rice', '+', 2)
['how', 'to']
```
 
Voici comment l'implémenter :

```javascript
class _ {
    //... autres méthodes
    
     static split(string='', separator, limit){
           let spl = string.split(separator);
           let limited = [];
                       
           if (limit === undefined){
                 return spl;
           } else {
                 for(let i=0; i<limit; i++){
                       limited.push(spl[i])
                 }
                 return limited
                       
            }
     }
}
```

Dans le code ci-dessus, nous avons créé une méthode `split()` avec un paramètre `string`, `separator` et `limit`. 

`string` est la chaîne dont les caractères seront divisés. `separator` sera utilisé comme séparateur de chaîne et `limit` définit une limite pour les caractères divisés à retourner. 

Ensuite, nous avons utilisé la méthode `string.split()` pour diviser la chaîne avec le séparateur. Puis nous avons retourné la chaîne divisée si aucune limite n'était spécifiée. Si la limite était spécifiée, nous avons utilisé la boucle `for` pour pousser les éléments sélectionnés vers une variable `limited` et retourné son résultat.

## Conclusion
Ouf - c'était beaucoup. Si vous êtes arrivé jusqu'ici, laissez-moi vous féliciter pour le temps bien passé. 

Tout au long de l'article, vous avez appris comment implémenter certaines fonctionnalités de la bibliothèque Lodash. 

Maintenant, vous pouvez vous challenger pour compléter la bibliothèque en implémentant les méthodes et fonctions restantes, ou ajouter plus de fonctionnalités à celle-ci. 

J'espère que cela aide. Sans rapport, mais si vous avez besoin d'un rédacteur technique compétent, n'oubliez pas de me contacter via [Twitter(@GidtheCoder)](https://twitter.com/gidthecoder) ou [email(akinsanmi20700@gmail.com)](mailto:akinsanmi20700@gmail.com). À bientôt.