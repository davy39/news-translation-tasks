---
title: Comment utiliser les fermetures en JavaScript – Un guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-07T18:18:01.000Z'
originalURL: https://freecodecamp.org/news/closures-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/English-Header-4.png
tags:
- name: closure
  slug: closure
- name: Closure with example
  slug: closure-with-example
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les fermetures en JavaScript – Un guide pour débutants
seo_desc: "By Matías Hernández\nClosures are a confusing JavaScript concept to learn,\
  \ because it's hard to see how they're actually used. \nUnlike other concepts such\
  \ as functions, variables, and objects, you don't always use closures conscientiously\
  \ and directly..."
---

Par Matías Hernández

Les fermetures sont un concept JavaScript confus à apprendre, car il est difficile de voir comment elles sont réellement utilisées.

Contrairement à d'autres concepts tels que les fonctions, les variables et les objets, vous n'utilisez pas toujours les fermetures de manière consciente et directe. Vous ne dites pas : Oh ! Ici, j'utiliserai une fermeture comme solution.

Mais en même temps, vous avez peut-être déjà utilisé ce concept une centaine de fois. Apprendre les fermetures consiste davantage à identifier quand elles sont utilisées plutôt qu'à apprendre un nouveau concept.

## Qu'est-ce qu'une fermeture en JavaScript ?

Vous avez une fermeture lorsqu'une fonction lit ou modifie la valeur d'une variable définie en dehors de son contexte.

```javascript
const value = 1
function doSomething() {
    let data = [1,2,3,4,5,6,7,8,9,10,11]
    return data.filter(item => item % value === 0)
}

```

Ici, la fonction `doSomething` utilise la variable `value`. Mais aussi, la fonction `item => item % value === 0` peut alors s'écrire comme ceci :

```javascript
function(item){
    return item % value === 0
}

```

Vous utilisez la valeur de la variable `value` qui a été définie en dehors de la fonction elle-même.

## Les fonctions peuvent accéder à des valeurs hors contexte

Comme dans l'exemple précédent, une fonction peut accéder et utiliser des valeurs qui sont définies en dehors de son "corps" ou contexte, par exemple :

```javascript
let count = 1
function counter() {
    console.log(count)
}
counter() // affiche 1
count = 2
counter() // affiche 2

```

Cela nous permet de modifier la valeur de la variable `count` depuis n'importe quel endroit dans le module. Ensuite, lorsque la fonction counter est appelée, elle saura comment utiliser la valeur actuelle.

## **Pourquoi utilisons-nous des fonctions ?**

Mais pourquoi utilisons-nous des fonctions dans nos programmes ? Il est certainement possible – difficile, mais possible – d'écrire un programme sans utiliser de fonctions que nous définissons. Alors pourquoi créons-nous des fonctions appropriées ?

Imaginez un morceau de code qui fait quelque chose de merveilleux, peu importe quoi, et qui est composé de X nombre de lignes.

```
/* Mon merveilleux morceau de code */

```

Maintenant, supposez que vous devez utiliser ce **merveilleux morceau de code** dans diverses parties de votre programme, que feriez-vous ?

L'option "naturelle" est de mettre ce morceau de code ensemble dans un ensemble qui peut être réutilisable, et cet ensemble réutilisable est ce que nous appelons une fonction. Les fonctions sont le meilleur moyen de réutiliser et de partager du code au sein d'un programme.

Maintenant, vous pouvez utiliser votre fonction autant de fois que possible. Et, en ignorant certains cas particuliers, appeler votre fonction N fois revient au même que d'écrire ce **merveilleux morceau de code** N fois. C'est un simple remplacement.

## **Mais où est la fermeture ?**

En utilisant l'exemple du compteur, considérons cela comme le **merveilleux morceau de code**.

```javascript
let count = 1
function counter() {
    console.log(count)
}
counter() // affiche 1

```

Maintenant, nous voulons le réutiliser dans de nombreuses parties, nous allons donc l'"envelopper" dans une fonction.

```javascript
function wonderfulFunction() {
    let count = 1
    function counter() {
        console.log(count)
    }
    counter() // affiche 1
}

```

Maintenant, qu'avons-nous ? Une fonction : `counter` qui utilise une valeur déclarée en dehors d'elle `count`. Et une valeur : `count` qui a été déclarée dans la portée de la fonction `wonderfulFunction` mais qui est utilisée à l'intérieur de la fonction `counter`.

C'est-à-dire, nous avons une fonction qui utilise une valeur déclarée en dehors de son contexte : **une fermeture**.

Simple, n'est-ce pas ? Maintenant, que se passe-t-il lorsque la fonction `wonderfulFunction` est exécutée ? Que se passe-t-il avec la variable `count` et la fonction `counter` une fois que la fonction **parente** est exécutée ?

Les variables et fonctions déclarées dans son corps _"disparaissent"_ (ramasse-miettes).

Maintenant, modifions un peu l'exemple :

```javascript
function wonderfulFunction() {
    let count = 1
    function counter() {
        count++
        console.log(count)
    }
   setInterval(counter, 2000)
}
wonderfulFunction()

```

Que va-t-il se passer maintenant avec la variable et la fonction déclarées à l'intérieur de `wonderfulFunction` ?

Dans cet exemple, nous demandons au navigateur d'exécuter `counter` toutes les 2 secondes. Ainsi, le moteur JavaScript doit conserver une référence à la fonction et également à la variable qui est utilisée par celle-ci. Même après que la fonction parente `wonderfulFunction` ait terminé son cycle d'exécution, la fonction `counter` et la valeur count continueront de "_vivre_".

Cet "effet" d'avoir des fermetures se produit parce que JavaScript supporte l'imbrication de fonctions. Ou en d'autres termes, les fonctions sont des **citoyens de première classe** dans le langage et vous pouvez les utiliser comme n'importe quel autre objet : imbriquées, passées en argument, comme valeur de retour, etc.

## **Que puis-je faire avec les fermetures en JavaScript ?**

### **Expression de fonction immédiatement invoquée (IIFE)**

Il s'agit d'une technique qui était beaucoup utilisée à l'époque d'ES5 pour implémenter le modèle de conception "module" (avant que cela ne soit supporté nativement). L'idée est d'"envelopper" votre module dans une fonction qui est immédiatement exécutée.

```javascript
(function(arg1, arg2){
...
...
})(arg1, arg2)

```

Cela vous permet d'utiliser des variables privées qui ne peuvent être utilisées que par le module lui-même au sein de la fonction – c'est-à-dire qu'il est permis d'émuler les modificateurs d'accès.

```javascript
const module = (function(){
	function privateMethod () {
	}
	const privateValue = "something"
	return {
	  get: privateValue,
	  set: function(v) { privateValue = v }
	}
})()

var x = module()
x.get() // "something"
x.set("Another value")
x.get() // "Another Value"
x.privateValue //Error

```

### **Fabrique de fonctions**

Un autre modèle de conception implémenté grâce aux fermetures est la "Fabrique de fonctions". Cela se produit lorsque des fonctions créent des fonctions ou des objets, par exemple, une fonction qui permet de créer des objets utilisateur.

```javascript

const createUser = ({ userName, avatar }) => ({
      id: createID(),
      userName,
      avatar,
      changeUserName (userName) {
        this.userName = userName;
        return this;
      },
      changeAvatar (url) {
        // exécuter une logique pour récupérer l'image de l'avatar
        const newAvatar = fetchAvatarFromUrl(url)
        this.avatar = newAvatar
        return this
      }
    });
    
        console.log(createUser({ userName: 'Bender', avatar: 'bender.png' }));
    
    {
      "id":"17hakg9a7jas",
      "avatar": "bender.png",
      "userName": "Bender",
      "changeUsername": [Function changeUsername]
      "changeAvatar": [Function changeAvatar]
    
    }
    */c
```

Et en utilisant ce modèle, vous pouvez implémenter une idée de la programmation fonctionnelle appelée **currying**.

### **Currying**

Le currying est un modèle de conception (et une caractéristique de certains langages) où une fonction est immédiatement évaluée et retourne une deuxième fonction. Ce modèle vous permet d'exécuter une spécialisation et une composition.

Vous créez ces fonctions "curryfiées" en utilisant des fermetures, en définissant et en retournant la fonction interne de la fermeture.

```javascript
function multiply(a) {

    return function (b) {
        return function (c)  {
            return a * b * c
        }
    }
}
let mc1 = multiply(1);
let mc2 = mc1(2);
let res = mc2(3);
console.log(res);

let res2 = multiply(1)(2)(3);
console.log(res2);

```

Ces types de fonctions prennent une seule valeur ou argument et retournent une autre fonction qui reçoit également un argument. C'est une application partielle des arguments. Il est également possible de réécrire cet exemple en utilisant ES6.

```javascript
let multiply = (a) => (b) => (c) => {

    return a * b * c;
}

let mc1 = multiply(1);
let mc2 = mc1(2);
let res = mc2(3);
console.log(res);

let res2 = multiply(1)(2)(3);
console.log(res2);

```

Où pouvons-nous appliquer le currying ? Dans la composition, disons que vous avez une fonction qui crée des éléments HTML.

```javascript
function createElement(element){
    const el = document.createElement(element)
    return function(content) {
        return el.textNode = content
    }
}

const bold = crearElement('b')
const italic = createElement('i')
const content = 'My content'
const myElement  = bold(italic(content)) // <b><i>My content</i></b>

```

### **Écouteurs d'événements**

Un autre endroit où vous pouvez utiliser et appliquer des fermetures est dans les gestionnaires d'événements en utilisant React.

Supposons que vous utilisez une bibliothèque tierce pour rendre les éléments de votre collection de données. Cette bibliothèque expose un composant appelé `RenderItem` qui n'a qu'une seule prop disponible `onClick`. Cette prop ne reçoit aucun paramètre et ne retourne aucune valeur.

Maintenant, dans votre application particulière, vous exigez que lorsque l'utilisateur clique sur l'élément, l'application affiche une alerte avec le titre de l'élément. Mais l'événement `onClick` dont vous disposez n'accepte pas d'arguments – alors que pouvez-vous faire ? **Les fermetures à la rescousse** :

```javascript
// Fermeture
// avec es5
function onItemClick(title) {
    return function() {
      alert("Clicked " + title)
    }
}
// avec es6
const onItemClick = title => () => alert(`Clcked ${title}`)

return (
  <Container>
{items.map(item => {
return (
   <RenderItem onClick={onItemClick(item.title)}>
    <Title>{item.title}</Title>
  </RenderItem>
)
})}
</Container>
)

```

Dans cet exemple simplifié, nous créons une fonction qui reçoit le titre que vous souhaitez afficher et retourne une autre fonction qui répond à la définition de la fonction que RenderItem reçoit en tant que prop.

## **Conclusion**

Vous pouvez développer une application sans même savoir que vous utilisez des fermetures. Mais savoir qu'elles existent et comment elles fonctionnent vraiment ouvre de nouvelles possibilités lorsque vous créez une solution.

Les fermetures sont l'un de ces concepts qui peuvent être difficiles à comprendre lorsque vous commencez. Mais une fois que vous savez que vous les utilisez et que vous les comprenez, cela vous permet d'augmenter vos outils et de faire avancer votre carrière.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/English-Footer-Social-Card-1.jpg)

🐙 [Suivez-moi sur Twitter](https://twitter.com/matiasfha)           ✉️ [Rejoignez la newsletter](https://matiashernandez.ck.page)           ❤️ [Soutenez mon travail](https://buymeacoffee.com/matiasfha)