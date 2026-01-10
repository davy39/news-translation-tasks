---
title: Apprenez les bases de la programmation orientée objet avec JavaScript (et boostez
  votre codage…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-13T05:54:42.000Z'
originalURL: https://freecodecamp.org/news/intro-to-object-oriented-programming-oop-with-javascript-made-easy-a317b87d6943
coverImage: https://cdn-media-1.freecodecamp.org/images/1*X6c_RNPQ7YOwfQemVNgBkw.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprenez les bases de la programmation orientée objet avec JavaScript (et
  boostez votre codage…
seo_desc: 'By Kris Baillargeon

  As a moderator of the freeCodeCamp chat rooms, I spend a lot of time with new developers.
  Boy, are they eager to learn. For a lot us, this can be quite a challenging quality.

  In the case of object-oriented programming (OOP), this ...'
---

Par Kris Baillargeon

En tant que modérateur des salons de discussion de [freeCodeCamp](https://www.freecodecamp.org/), je passe beaucoup de temps avec de nouveaux développeurs. Ils sont vraiment impatients d'apprendre. Pour beaucoup d'entre nous, cela peut être une qualité assez difficile à gérer.

Dans le cas de la programmation orientée objet (POO), cela est particulièrement vrai. Qu'est-ce qu'une méthode et pourquoi est-elle si spéciale ? Quelle est la différence entre une méthode et une propriété ? Pourquoi utilisons-nous même la programmation orientée objet, et pourquoi est-elle essentielle pour moi en tant que développeur ? Ce sont quelques-unes des questions que je me suis posées en apprenant la POO, et comme vous êtes ici, il est sûr de supposer que vous vous les êtes posées aussi.

### Utiliser la programmation orientée objet avec JavaScript

Presque tout en JavaScript est un objet. Quelque part en coulisses, chaque morceau de code que vous écrivez est soit écrit, soit stocké avec la POO. C'est l'une des raisons pour lesquelles il est si important de la comprendre. Si vous ne le faites pas, vous ne pourrez probablement jamais lire le code d'autres développeurs. En plus de cela, votre code n'atteindra jamais son plein potentiel !

Un nouvel objet est créé en JavaScript en assignant une variable à deux accolades, comme ceci :

```
var myObject = {};
```

```
// var myObject = new Object();  // Version non recommandée, mais elle fonctionne
```

C'est aussi simple que cela ! Vous avez maintenant un objet qui peut stocker n'importe quel type de données que vous stockeriez dans une variable. Il existe de nombreuses façons d'insérer des données dans un objet, mais nous allons nous en tenir aux méthodes les plus faciles pour l'instant.

### Leçon rapide de syntaxe

Pour terminer une ligne en JavaScript, lorsque vous créez une variable comme ceci :

var a = 5;

la « ligne » se termine au point-virgule. Lorsque vous créez un objet, la « ligne » se terminera par une virgule, comme ceci :

```
myObject = { myProp: 5,  myOtherProp: 10,}
```

* Propriété/Clé : Le nom d'une variable d'objet. Un exemple serait `myProp` dans le code ci-dessus. || Côté gauche des assignations
* Méthode : Une fonction à l'intérieur d'un objet, disponible uniquement pour cet objet. Il s'agit d'un type de propriété.
* Valeur : La valeur d'une variable d'objet. Un exemple serait 10, qui est la valeur de `myOtherProp`. Cela peut être n'importe quel type de données JavaScript valide.

Seule la dernière propriété d'un objet peut ne pas utiliser de virgule.

_Note : Vous pouvez encadrer vos propriétés avec des guillemets simples ou doubles. Si le nom de la propriété contient un espace, vous devez toujours utiliser des guillemets. Lorsque vous utilisez [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON), l'utilisation de guillemets n'est pas facultative._

### Référencer les propriétés d'un objet

#### Notation par point

Il existe deux façons de référencer un objet, toutes deux utilisant un nom comme référence. La plus couramment utilisée, la notation par point, est principalement utilisée. Cela ressemble à ceci :

```
var myObject = {
```

```
otherObject: {            one: 1,        two: 2      },
```

```
addFunction: function(x,y){ return x+y }
```

```
}
```

```
var dot = myObject.otherObject;console.log(dot);//évalue à otherObject: {..props:vals..}
```

Le code ci-dessus entre dans `myObject` et y ajoute un autre objet, `otherObject` via la notation par point. Tout nom qui peut être utilisé comme variable convient pour une utilisation dans la notation par point. La notation par point est la meilleure pratique pour référencer toute propriété qui n'inclut pas d'espaces.

#### Notation par crochets

```
var myObject = {  "Other Obj": {          one: 1,      two: 2    }}
```

```
var bracket = myObject["Other Obj"];
```

```
bracket.newProperty = "This is a new property in myObject";
```

```
console.log(bracket.newProperty);
```

```
//évalue à myObject["Other Obj"].newProperty
```

L'autre façon de référencer les objets est via la notation par crochets. Cela n'est recommandé que si la propriété de l'objet contient un espace, comme la propriété `myObject["Other Object"]`. Dans ce cas, l'utilisation de la notation par crochets est une nécessité. Lorsque vous nommez des méthodes, n'utilisez pas d'espaces — sinon la fonction ne peut pas être appelée. De plus, vous pouvez utiliser des guillemets pour nommer n'importe quelle propriété.

### Utiliser JavaScript dans la vraie vie

Les fonctions constructrices valent la peine d'être mentionnées, car nous créerons notre propre forme de fonctions constructrices plus tard dans cet article. Pour cela, nous devons d'abord apprendre deux mots-clés JavaScript — **new** et **this**. Vous utilisez le mot-clé new lorsque vous faites référence à la fonction constructrice.

Pour le mot-clé this, c'est essentiellement un mot-clé sophistiqué pour l'objet parent de la dernière fonction appelée. S'il n'a pas d'objet parent, window sera son objet parent. Vous pouvez lier une fonction à ce mot-clé en utilisant Function.bind(). En savoir plus [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind). Mais c'est un peu plus avancé. Cela a-t-il du sens ? Regardons un peu de code :

```
var ConstructorForPerson = function(first, last, email) {  this.firstName = first;this.lastName = last;this.fullName = first + " " + last;this.eMail =  email;
```

```
}
```

```
var Bob = new ConstructorForPerson("bob", "brown", "bob122099@gmail.com");
```

```
console.log(Bob.eMail);
```

```
//évalue "bob122099@gmail.com"
```

Le code ci-dessus retournera un nouvel objet, `Bob`. C'est le résultat de la fonction constructrice, qui aura les propriétés `Bob.firstName`, `Bob.lastName`, `Bob.fullName`, et `_Bob.eMail_`**.**_

Notez qu'à l'intérieur d'une fonction constructrice, au lieu de terminer une ligne avec une virgule, elle se termine par un point-virgule comme vous vous y attendriez à l'intérieur d'une fonction. Optionnellement, pour garder les choses simples, vous pouvez créer vos propres fonctions constructrices sans utiliser **new** ou **this**. C'est ce que nous ferons aujourd'hui afin de mieux voir toutes les pièces en mouvement.

### En termes simples

La programmation orientée objet est une manière de structurer votre code pour une lisibilité, une utilisation et une maintenance optimales. Avec cela en tête, essayons de coder une représentation de Google en tant qu'entreprise, incluant certaines fonctions d'une entreprise normale.

* L'Objet — Le Bâtiment/La Gestion. Cela contiendra toutes les informations sur n'importe quel type d'employé, tout ce qui peut être fait à un employé, y compris en créer un nouveau.
* Les Propriétés — Les Employés. Cela peut être un manager ou un employé de bureau. Cela peut être une liste d'employés. Cela peut être votre profit brut pour cette année. Pratiquement n'importe quoi.
* Les Méthodes — Que peut faire Google ? Que peuvent faire les employés ? C'est ainsi que de nouveaux employés sont créés, ainsi que la manière dont ils « effectueront des tâches ».

### Codons !

Tout d'abord, regardons notre résultat final :

```
var google = { //créer {google}
```

```
employees: {           management: {            },
```

```
developers: {                 },
```

```
maintenance: {            }   },      NewEmployee: function(name, role, phone, idNumber) {  //créer NewExployee()            var newEmployeeData = {        name: name,        role: role,        phone: phone,        idNumber: idNumber,        working: false,        hours: [],       }     //créer un nouvel objet à ajouter à google.employees[role]        google.employees[role][name] = newEmployeeData;    //assigner l'objet à google.employees[role][name]
```

```
return  google.employees[role][name];  //retourner le nouvel objet directement depuis google.employees[role][name]        } //fin NewEmployee  } //fin {google}
```

```
google.NewEmployee("james", "maintenance", "2035555555", "1234521"); //créer {google:employees:maintenance["james"]} depuis NewEmployee()
```

```
google.employees["maintenance"]["james"].clockInOut = function() { //créer clockInOut() - par défaut false         if(this.working) {         this.hours[this.hours.length - 1].push(Date.now());         this.working = false;         return this.name + " a terminé à " + Date.now();        }       else{         this.hours.push([Date.now()]);         this.working = true;         return this.name + " a commencé à " + Date.now();        }
```

```
return "Erreur"     //si le code ci-dessus ne fonctionne pas, "Erreur" }
```

```
google.employees["maintenance"]["james"].clockInOut(); //pointer James ou le dépointer, retourne une chaîne avec l'heure et l'état
```

Intimidant ?

Décomposons cela en morceaux plus petits. Pour commencer, nous allons créer un objet global appelé `Google`. Il contiendra un autre objet pour les employés, qui contiendra d'autres objets pour chaque rôle et ses employés individuels.

À quoi cela ressemblera-t-il en code ? Pour simplifier les choses, nous allons créer un constructeur en utilisant une fonction normale. Il aura 7 propriétés : `name`, _`role,`_ `phone`, _`idNumber`**,**_ `working`, et `hours`.

De plus, il aura 1 méthode : `clockInOut(),` qui regardera la propriété `_working_` pour mettre à jour `hours.`

Décomposons cela.

Tout d'abord, nous allons mettre à jour notre objet `Google` avec la fonction constructrice `NewEmployee()`. Souvenez-vous, au lieu d'utiliser la fonction constructrice JavaScript régulière, nous utiliserons la nôtre.

_Note : Faites attention à la syntaxe car elle changera un peu en fonction de ce que vous faites_

_Aussi note : Ces exemples ne s'exécuteront pas correctement car ils n'ont pas les bonnes dépendances/propriétés/variables. La plupart, sinon toutes les fonctionnalités du produit final, retourneront une erreur. Si vous exécutez le produit final, cependant, tout devrait fonctionner correctement._

```
var google = { //créer {google}
```

```
employees: {           management: {
```

```
},           developers: {
```

```
},
```

```
maintenance: {
```

```
}         }, //<--cette virgule est inutile pour l'instant mais lorsque nous ajouterons plus de propriétés d'objet, elle sera nécessaire}
```

`employees` contient d'autres objets qui sont divers rôles dans l'entreprise : `management`, `developers`, et `maintenance`. Nous allons ajouter un employé via le rôle de l'employé, dans ce cas, maintenance.

```
var google = {  NewEmployee: function(name, role, phone, idNumber) {    var newEmployeeData = {      name: name,      role: role,      phone: phone,      idNumber: idNumber,      working: false,      hours: [],     }     //créer un nouvel objet à ajouter à google.employees[role]        google.employees[role][name] = newEmployeeData;    //assigner l'objet à google.employees[role][name]
```

```
return  google.employees[role][name];  //retourner le nouvel objet directement depuis google.employees[role][name]  }}
```

Notre fonction « constructeur ». Assez simple, elle prend un nouvel objet et l'ajoute au rôle correspondant.

```
google.employees["maintenance"]["james"].clockInOut = function() { //créer clockInOut() - par défaut false         if(this.working) {         this.hours[this.hours.length - 1].push(Date.now());         this.working = false;         return this.name + " a terminé à " + Date.now();        }       else{         this.hours.push([Date.now()]);         this.working = true;         return this.name + " a commencé à " + Date.now();        }
```

```
return "Erreur" //si le code ci-dessus ne fonctionne pas, "Erreur" }
```

```
google.employees["maintenance"]["james"].clockInOut(); //appeler clockInOut()
```

C'est là que cela peut devenir confus. Souvenez-vous que le mot-clé this est simplement une manière amusante de dire l'objet parent de la fonction appelante ? Dans le code ci-dessus, nous ajoutons la méthode `clockInOut**_()_**` à notre code. Nous l'invoquons simplement en l'appelant. Si working est false, elle créera un nouveau tableau avec un timestamp Unix à l'index 0. Si vous travaillez déjà, elle ajoutera simplement un timestamp Unix au dernier tableau créé, créant un tableau qui ressemble un peu à ceci : [1518491647421, 1518491668453] avec le premier timestamp étant lorsque l'employé « commence », le second étant lorsque l'employé « termine ».

Maintenant, nous avons vu comment l'utilisation de la POO peut être pratique ! Chaque employé individuel peut « commencer » et « terminer » avec un simple appel de fonction, et tout ce que vous avez à savoir est leur nom et leur rôle !

Cela peut, bien sûr, être optimisé pour faire quelque chose comme regarder un numéro d'identification au lieu de leur rôle et nom, mais ne compliquons pas trop les choses. Ci-dessous, nous ramenons tout dans un seul programme. Un peu moins effrayant, non ?

```
var google = { //créer {google}
```

```
employees: {           management: {      },      developers: {      },
```

```
maintenance: {      }         },      NewEmployee: function(name, role, phone, idNumber) { //créer NewExployee()            var newEmployeeData = {        name: name,        role: role,        phone: phone,        idNumber: idNumber,        working: false,        hours: [],       }     //créer un nouvel objet à ajouter à google.employees[role]        google.employees[role][name] = newEmployeeData;    //assigner l'objet à google.employees[role][name]
```

```
return  google.employees[role][name];  //retourner le nouvel objet directement depuis google.employees[role][name]        }//fin NewEmployee  } //fin {google}
```

```
google.NewEmployee("james", "maintenance", "2035555555", "1234521"); //créer {google:employees:maintenance["james"]} depuis NewEmployee()
```

```
google.employees["maintenance"]["james"].clockInOut = function() { //créer clockInOut() - par défaut false         if(this.working) {         this.hours[this.hours.length - 1].push(Date.now());         this.working = false;         return this.name + " a terminé à " + Date.now();        }       else{         this.hours.push([Date.now()]);         this.working = true;         return this.name + " a commencé à " + Date.now();        }
```

```
return "Erreur" //si le code ci-dessus ne fonctionne pas, "Erreur" }
```

```
google.employees["maintenance"]["james"].clockInOut(); //appeler clockInOut()
```

Utiliser la programmation orientée objet peut non seulement rendre votre code plus puissant, mais aussi beaucoup plus lisible pour les autres développeurs. N'hésitez pas à me contacter via [Github](https://github.com/krisb1220/) pour des projets, des informations sur [Free Code Camp](http://www.freecodecamp.org/), de l'aide en Javascript/HTML/CSS, pour m'encourager à écrire un tutoriel sur l'utilisation de JSON et des API, ou pour parler de chats !

Au fait, si vous ne le saviez pas, tout ce qui est enseigné dans ce tutoriel ainsi que TOUT ce que vous devez savoir sur le Javascript vanilla, HTML, CSS et plus encore, vous pouvez compter sur [MDN](https://developer.mozilla.org/) pour avoir une quantité extensive de connaissances à ce sujet. C'est pratiquement Google pour les développeurs web ! C'est aussi 1220% gratuit et open source.

N'oubliez pas d'applaudir et de suivre si vous avez aimé ! Plus d'articles à venir bientôt ! :)

Restez en contact avec moi sur Instagram [@krux.io](http://instagram.com/krux.io)

POUR ALLER PLUS LOIN SUR [MDN](https://developer.mozilla.org/) :

[**POO POUR DÉBUTANTS**](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)

[**OBJETS GLOBAUX**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/)

[**TUTORIEL JSON**](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)

[**UTILISER JSON EN JAVASCRIPT — OBJET GLOBAL JSON**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

[**MOT-CLÉ _THIS_**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)

[**FONCTIONS CONSTRUCTRICES**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)