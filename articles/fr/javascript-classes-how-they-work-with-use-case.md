---
title: Les classes JavaScript – Comment elles fonctionnent avec un exemple de cas
  d'utilisation
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2021-12-13T19:24:50.000Z'
originalURL: https://freecodecamp.org/news/javascript-classes-how-they-work-with-use-case
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/feliphe-schiarolli-hes6nUC1MVc-unsplash-1.jpg
tags:
- name: classes
  slug: classes
- name: JavaScript
  slug: javascript
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Les classes JavaScript – Comment elles fonctionnent avec un exemple de
  cas d'utilisation
seo_desc: "In this blog post I'll walk you through a real life example which uses\
  \ the concept of classes in JavaScript. \nI think it's helpful to work with a practical\
  \ use case because it is much simpler to understand the concepts when you can relate\
  \ them to rea..."
---

Dans cet article de blog, je vais vous guider à travers un exemple concret qui utilise le concept de classes en JavaScript.

Je pense qu'il est utile de travailler avec un cas d'utilisation pratique car il est beaucoup plus simple de comprendre les concepts lorsque vous pouvez les relier à la vie réelle.

Ainsi, dans ce guide, vous apprendrez les classes en JavaScript, l'héritage, les fonctions abstraites, comment utiliser des mots-clés tels que `super` et `extends`, les mots-clés statiques et les membres privés des classes.

Plongeons-nous dans le sujet.

## Table des matières

* [Prérequis](#Prerequisites)
* [Que sont les classes en JavaScript ?](#heading-quest-ce-que-les-classes-en-javascript)
* [Description du cas d'utilisation](#heading-description-du-cas-dutilisation)
* [Fonctions abstraites et héritage dans le système de gestion de chaises](#heading-fonctions-abstraites-et-heritage-dans-le-systeme-de-gestion-de-chaises)
* [Mot-clé statique en JavaScript](#heading-mot-cle-statique-en-javascript)
* [Membres privés en JavaScript](#heading-membres-prives-des-classes-en-javascript)

## Prérequis

Avant de commencer à lire cet article de blog, vous devriez avoir une compréhension de base des sujets suivants :

* [Diagrammes de classes : Nous allons les utiliser pour présenter notre exemple](https://drawio-app.com/uml-class-diagrams-in-draw-io/)
* [Diagramme de contexte et diagrammes de conteneurs](https://en.wikipedia.org/wiki/System_context_diagram)
* [Connaissance de la POO](https://www.freecodecamp.org/news/object-oriented-programming-javascript/)
* [Introduction à l'héritage prototypal et au chaînage de prototypes](https://dev.to/lawrence_eagles/understanding-prototypal-inheritance-in-javascript-4f31#chp-2)
* [Introduction aux fonctions constructeurs en JS](https://dev.to/lawrence_eagles/an-easy-guide-to-understanding-constructors-in-javascript-2mf6)

## Que sont les classes en JavaScript ?

Les classes ont été introduites dans [EcmaScript 2015](https://262.ecma-international.org/6.0/) (ES6) pour fournir une manière plus propre de suivre les modèles de programmation orientée objet.

JavaScript suit toujours un modèle d'héritage basé sur les prototypes. Les classes en JavaScript sont du sucre syntaxique sur le modèle d'héritage basé sur les prototypes que nous utilisons pour implémenter les concepts de la POO.

Ainsi, l'introduction des classes en JS a facilité la tâche des développeurs pour construire des logiciels autour des concepts de la POO. Cela a également apporté des similitudes avec différents langages de programmation basés sur la POO tels que C++ et Java.

Avant les classes, nous utilisions des fonctions constructeurs pour faire de la POO en JavaScript. Jetez un œil à l'exemple ci-dessous :

```javascript
function Pen(name, color, price) {
    this.name = name;
    this.color = color;
    this.price = price;
}

const pen1 = new Pen("Marker", "Blue", "$3");
console.log(pen1);

```

Le code ci-dessus montre une fonction constructeur `Pen` qui a des propriétés name, color et price. Nous utilisons le mot-clé `new` avec le constructeur `Pen` pour créer un objet `pen1`.

Maintenant, disons que nous voulons ajouter une nouvelle fonction au constructeur `Pen`. Pour ce faire, nous devons ajouter la fonction dans la propriété prototype de `Pen`. Jetez un œil à la fonction `showPrice` ci-dessous :

```javascript
function Pen(name, color, price) {
    this.name = name;
    this.color = color;
    this.price = price;
}

const pen1 = new Pen("Marker", "Blue", "$3");

Pen.prototype.showPrice = function(){
    console.log(`Price of ${this.name} is ${this.price}`);
}

pen1.showPrice();
```

Si ces concepts ne vous semblent pas clairs, je vous recommande de rafraîchir vos connaissances en JS à travers les articles mentionnés dans la section Prérequis. En particulier, consultez l'article sur le Prototype et les fonctions constructeurs.

En regardant le code ci-dessus, nous pouvons dire que nous avons fait ce que nous voulions faire – c'est-à-dire, ajouter une fonction `showPrice` au constructeur `Pen`. Mais vous pouvez voir que ce n'est pas aussi lisible que les concepts de POO que nous implémentons en C++ ou Java.

Nous pouvons recréer l'exemple ci-dessus à l'aide du mot-clé `class`. Jetez un œil au code ci-dessous :

```javascript
class Pen {
    constructor(name, color, price){
        this.name = name;
        this.color = color; 
        this.price = price;
    }
    
    showPrice(){
        console.log(`Price of ${this.name} is ${this.price}`);
    }
}

const pen1 = new Pen("Marker", "Blue", "$3");
pen1.showPrice();
```

Avez-vous remarqué la différence ! Nous avons obtenu les mêmes résultats mais avec une syntaxe beaucoup plus propre. L'ajout d'une nouvelle fonction membre comme `showPrice` est beaucoup plus facile par rapport à l'ajout d'une fonction directement dans le prototype du constructeur.

Plongeons-nous un peu plus dans les classes en JS en utilisant un exemple de cas d'utilisation. Avec ce cas d'utilisation, nous allons voir comment ces concepts peuvent être utiles pour résoudre certains problèmes réels.

## Description du cas d'utilisation

**Juste une petite note** : les diagrammes de Contexte, de Conteneur et de Classes dessinés dans cet article de blog ne suivent pas exactement les conventions des diagrammes ci-dessus. J'ai approximé les diagrammes pour vous aider à comprendre les concepts en général.

Avant de commencer, je vous suggère de lire sur les modèles c4, les diagrammes de conteneurs et les diagrammes de contexte si vous avez besoin d'un rappel. Vous pouvez les trouver dans la section prérequis.

Nous allons résoudre le problème suivant : aider un commerçant à classer les chaises dans son inventaire et à les afficher à l'écran.

Le cas d'utilisation est simple et assez explicite. Jetez un œil au diagramme ci-dessous qui présente le système proposé dans son ensemble :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/js_classes_tut_context.drawio--1-.png)
_Diagramme de contexte pour le système de gestion de chaises_

Comme vous pouvez le voir sur le diagramme ci-dessus, il y a 3 composants principaux :

1. **Personne** : Le commerçant va interagir avec notre système.
2. **Système logiciel : Portail d'interface de stock** - Il s'agit d'une interface qui permet au commerçant de visualiser ou de modifier les informations sur les chaises présentes dans l'inventaire.
3. **Système logiciel : Système de gestion de chaises** - Ce système permettra à l'interface de récupérer ou de modifier les détails demandés par le commerçant.

Maintenant que nous comprenons le cas d'utilisation, commençons par le système cible sur lequel nous allons nous concentrer dans cet article de blog. Il s'agit du **Système de gestion de chaises**.

Nous allons commencer par créer quelques composants majeurs dans notre Système de gestion de chaises. Nos composants dans ce système sont simplement différentes classes qui aideront à faciliter les différents besoins du commerçant.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/chairModel.drawio--2--1.png)
_Composant Chaise du Système de gestion de chaises_

Ajoutons un composant appelé **`Chair`**. Puisqu'il s'agit d'une classe, elle aura ses propres attributs (propriétés) et comportements (méthodes).

Jetez un œil au diagramme ci-dessus. Nous pouvons voir que :

* La deuxième ligne contient les attributs de la classe chaise, par exemple color, seatHeight, recliningAngle, et ainsi de suite.
* La troisième ligne correspond aux méthodes qui nous indiquent quelles fonctions la chaise peut effectuer, par exemple adjustSeatHeight, adjustAngle, moveChair, et ainsi de suite.

Nous suivrons la représentation ci-dessus pour tous les composants que nous créerons tout au long de cet article.

Le composant `Chair` sera notre composant de base. Cela signifie que tous les autres types de chaises tels que les chaises de bureau, les chaises de salle à manger, etc., seront sous cette classe/composant.

Commençons par créer notre classe de chaise de base en JS. Jetez un œil au code ci-dessous :

```javascript
class Chair {
    constructor(color, seatHeight, recliningAngle, backSupport, headSupport, padding, armRests, seatSize, isHeightAdjustable, isMovable){
        this.color = color;
        this.seatHeight = seatHeight;
        this.recliningAngle = recliningAngle;
        this.backSupport = backSupport;
        this.headSupport = headSupport;
        this.padding = padding;
        this.armRests = armRests;
        this.seatSize = seatSize;
        this.isHeightAdjustable = isHeightAdjustable;
        this.isMovable = isMovable;
    }
    
    adjustableHeight() {};
    adjustAngle(){};
    moveChair(){};    
}

const newChair = new Chair("Blue","25 inch","20 deg",true,false,"3 inch",true,"16 inch",false,false);

console.dir("Chair Prototype", Chair);
console.log("Chair Object", newChair);
```

La classe chair a les membres suivants :

* **Attributs** : Ceux-ci définiront les attributs de la chaise tels que la couleur, la hauteur du siège, backSupport, et ainsi de suite.
* **Fonctions** : Celles-ci définissent le comportement de la chaise. Par exemple, si la chaise a `isHeightAdjustable` défini sur true, alors elle peut utiliser la fonction `adjustableHeight`. Vous pouvez voir que toutes les fonctions sont déclarées dans la classe `Chair`. Ce sont les fonctions abstraites. Nous parlerons plus de ces fonctions plus tard dans cet article.

En bas du code, nous avons deux instructions console.log. La première imprimera la définition de la classe `Chair`. Le deuxième objet imprimera l'instance `newChair`.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-from-2021-12-11-11-58-14.png)
_Premier console.dir output_

Si vous regardez la première sortie, elle imprime la classe `Chair`. Jetez un œil à son contenu :

* Elle se compose d'une propriété `prototype`. Il s'agit du prototype que toutes les instances de la classe Chair auront.
* La propriété `name` est le nom de l'objet.
* Enfin, nous avons la propriété `__proto__` ou `[[Prototype]]`. Il s'agit du prototype réel de la classe `Chair`.

```json
{
    "color": "Blue",
    "seatHeight": "25 inch",
    "recliningAngle": "20 deg",
    "backSupport": true,
    "headSupport": false,
    "padding": "3 inch",
    "armRests": true,
    "seatSize": "16 inch",
    "isHeightAdjustable": false,
    "isMovable": false,
    [[Prototype]]: {
        adjustAngle:  adjustAngle()
        adjustableHeight:  adjustableHeight()
        constructor: class Chair
        moveChair:  moveChair()
        [[Prototype]]: Object
    }
}
```

La deuxième instruction de journalisation imprime les informations de l'instance de l'objet chaise. Elle consistera en tous les attributs de la classe Chair. Si vous observez de près, vous pouvez voir que le prototype de cette instance est similaire à celui de la propriété `prototype` de la classe chair. Cela se produit en raison de l'héritage prototypal.

Maintenant, voyons comment nous pouvons utiliser ce concept en ajoutant un nouveau composant/classe à notre **Système de gestion de chaises**.

## Fonctions abstraites et héritage dans le système de gestion de chaises

La fonction abstraite est simplement une signature de fonction dans une classe sans aucune implémentation. Elle nous aide à généraliser le code afin que les sous-classes puissent les utiliser et ajouter leur propre implémentation.

Pour démontrer cela dans notre cas d'utilisation, ajoutons un autre composant à notre **Système de gestion de chaises**.

J'ai modifié la classe chair de sorte qu'elle comporte désormais des valeurs par défaut. Ces valeurs par défaut seront utilisées par toutes les instances. Plus tard, la sous-classe pourra les modifier. Nous verrons bientôt comment nous pouvons y parvenir. Jetez un œil à la nouvelle classe `Chair` ci-dessous :

```javascript
class Chair {
    constructor(color, seatHeight, recliningAngle, backSupport, headSupport, padding, armRests, seatSize, isHeightAdjustable, isMovable){
        //Defaults which can be changed by the subclass class.
        this.color = color;
        this.seatHeight = seatHeight;
        this.recliningAngle = recliningAngle;
        this.backSupport = true;
        this.headSupport = false;
        this.padding = "3 inch";
        this.armRests = true;
        this.seatSize = "16 inch";
        this.isHeightAdjustable = false;
        this.isMovable = false;
        this.type = "Chair";
    }
    
    adjustableHeight() {};
    adjustAngle(){};
    moveChair(){};    
}

const newChair = new Chair();

newChair;
```

Maintenant, ajoutons un nouveau composant/classe appelé **`OfficeChair`**. Celui-ci héritera des attributs et des méthodes de la classe `Chair`. Le nouveau diagramme de classe modifié ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/chairModel.drawio--1---1-.png)
_Diagramme de classe_

Remarquez que la nouvelle classe `OfficeChair` ne contient que les méthodes et non les attributs. Nous supposons ici que tous les attributs seront hérités de la classe `Chair`.

Pour la classe `OfficeChair`, nous avons implémenté les méthodes abstraites présentes dans la classe `Chair`.

Jetez un œil au code ci-dessous pour la classe `OfficeChair` :

```javascript
class OfficeChair extends Chair{
    constructor(color, isHeightAdjustable, seatHeight, recliningAngle){
        super();
        this.type = "Office Chair";
        this.color = color;
        this.isHeightAdjustable = isHeightAdjustable;
        this.seatHeight = seatHeight;
        this.recliningAngle = recliningAngle;
        this.isMovable = true;
    }
    
    adjustableHeight(height){
        if(height > this.seatHeight){
            console.log(`Chair height changed to ${height}`);        
        } else {
            console.log(`Height cannot be decreased more than the seat height ${this.seatHeight}`);
        }
    }
    
    adjustAngle(angle){
        if(angle >= this.recliningAngle){
            console.log(`Chair angle changed to ${angle}`);        
        } else {
            console.log(`Angle cannot be decreased more than the min reclining angle ${this.recliningAngle}`);
        }
    }
    
    moveChair(x,y){
        console.log(`Chair moved to co-ordinates = (${x}, ${y})`);
    }
}

const newOfficeChair = new OfficeChair("Red", true, 30, 30);

console.log(newOfficeChair.adjustableHeight(31));
console.log(newOfficeChair.adjustAngle(40));
console.log(newOfficeChair.moveChair(10,20));
```

Il s'agit d'une classe qui hérite des fonctions et des attributs de la superclasse `chair`. Elle utilise le mot-clé `extends` pour permettre à la classe `OfficeChair` de réaliser l'héritage.

Le mot-clé `extends` a la syntaxe suivante :

```javascript
class ChildClass extends ParentClass{...}
```

Ensuite, nous avons une fonction constructeur et l'implémentation de certaines des fonctions de la superclasse. Remarquez que nous utilisons le mot-clé `super` dans le constructeur.

Nous utilisons le mot-clé `super` pour appeler le constructeur de la classe parente. Nous pouvons également l'utiliser pour appeler des fonctions et des propriétés de la classe parente.

Un mot d'avertissement lorsque vous utilisez le mot-clé `super` :

* Assurez-vous d'appeler la fonction `super` au début du constructeur. Si vous ne le faites pas et que vous essayez d'accéder aux propriétés de la classe parente avant d'utiliser `super` dans le constructeur de la classe enfant, cela générera une erreur.
* Une fois la fonction `super` appelée, vous pouvez alors accéder à tous les attributs et fonctions de la classe parente.
* Super n'est pas seulement lié aux classes – vous pouvez également l'utiliser pour appeler des fonctions sur le parent de l'objet.

Vous pouvez lire plus sur `super` dans la documentation MDN [docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super).

Enfin, si vous remarquez, nous avons ajouté l'implémentation pour les fonctions abstraites. Les fonctions sont les suivantes :

* `adjustableHeight` : Cette fonction vérifiera si la hauteur d'entrée est supérieure à la hauteur minimale de la chaise. Si oui, nous pouvons changer la hauteur ou afficher le message d'erreur. Une personne peut également augmenter ou diminuer la hauteur de la chaise. Notez que `this.seatHeight` est la hauteur minimale de la chaise par rapport au sol en dessous de laquelle la personne ne peut pas abaisser la hauteur.
* `adjustAngle` : Cette fonction vérifiera si l'angle d'entrée est supérieur à la valeur par défaut `this.recliningAngle`. Si l'angle d'entrée est supérieur à l'angle par défaut, alors l'angle changera ou un message d'erreur sera affiché.
* `moveChair` : Toute chaise dont la propriété `isMovable` est vraie, la classe correspondante aura une implémentation de la fonction `moveChair`. Elle aide simplement à déplacer la chaise en fonction des coordonnées x et y d'entrée.

Notez que nous avons également réinitialisé certains des attributs de la classe `Chair` tels que `type`. Nous définirons explicitement l'attribut `type` pour chaque sous-classe. Cela nous aidera à classer les chaises présentes dans l'inventaire en attribuant ces classes à chacune d'elles.

Vous devriez maintenant avoir une idée de ce que sont les fonctions abstraites et de leur utilité. Certains avantages d'avoir des fonctions abstraites :

* Réduit la redondance dans la base de code.
* Fournit une manière appropriée de généraliser les classes.
* Permet une flexibilité aux sous-classes pour implémenter les fonctions abstraites dont elles ont besoin.

## Mot-clé statique en Javascript

Le mot-clé `static` en JavaScript vous aide à définir des fonctions et des propriétés dans la classe qui ne peuvent pas être appelées par l'instance de l'objet. Elles ne peuvent être appelées que par la classe elle-même qui contient ces fonctions et propriétés statiques.

Généralement, nous utilisons les méthodes `static` dans les classes à des fins utilitaires telles que l'impression de toutes les propriétés de la classe, la création d'un nouvel objet, la suppression d'autres objets des classes, et ainsi de suite.

L'avantage d'utiliser des fonctions ou des propriétés `static` dans une classe est que :

* Elles peuvent être utilisées pour créer des fonctions/propriétés qui n'ont pas besoin d'être présentes dans les instances. Cela aide à maintenir une certaine isolation dans la base de code.
* Elles réduisent la redondance du code dans certains cas.

Maintenant, voyons comment nous pouvons implémenter ce concept dans notre classe `Chair`. Nous allons également examiner quelques cas d'utilisation où nous pouvons utiliser le mot-clé `static`.

Voici les scénarios où vous pouvez utiliser le mot-clé `static` :

* Utilisation dans les classes
* Statique dans statique
* Appel statique depuis un constructeur
* Blocs d'initialisation statique de classe

Pour plus d'informations sur les scénarios ci-dessus, veuillez consulter la documentation MDN [docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static).

Nous allons voir toutes les variantes de la classe `Chair` via ces scénarios :

### Comment utiliser le mot-clé `static` dans les classes

Comme dans tout autre langage de programmation, il s'agit de l'une des manières les plus adaptées aux débutants pour utiliser le mot-clé statique. Définissons certaines méthodes et propriétés des classes comme `static` et observons le comportement.

Jetez un œil au code ci-dessous :

```javascript
class Chair {
//Defaults that will be common for all the instances:
    static backSupport = true;
    static armRests = true;
    
    constructor(color, seatHeight, recliningAngle, headSupport, padding, seatSize, isHeightAdjustable, isMovable){
        //Defaults which can be changed by the subclass class.
        this.color = color;
        this.seatHeight = seatHeight;
        this.recliningAngle = recliningAngle;
        this.headSupport = false;
        this.padding = "3 inch";
        this.seatSize = "16 inch";
        this.isHeightAdjustable = false;
        this.isMovable = false;
        this.type = "Chair";
    } 
        
    static logObjectProps(){
        console.dir(this);
    }
    
    adjustableHeight() {};
    adjustAngle(){};
    moveChair(){};    
}
```

Voici le résultat du code ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-from-2021-12-01-11-05-15.png)
_Variables statiques_

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-from-2021-12-01-11-06-35.png)
_La sortie de la fonction statique_

Comme vous pouvez le voir ci-dessus, les méthodes statiques ne sont accessibles que via la classe elle-même. Elles ne peuvent pas être accessibles par les instances de la classe `Chair`. Les instances de la classe n'ont pas les attributs statiques présents :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-from-2021-12-01-11-09-20.png)
_Aucun membre statique dans les instances_

Comme vous pouvez le voir ci-dessus, l'instance `x` de la classe `Chair` n'a pas la méthode statique ou les propriétés présentes dans ses définitions.

Si vous essayez d'accéder à une méthode statique ou à une propriété en utilisant une instance de classe, cela générera une erreur de référence ou retournera simplement indéfini.

### Comment utiliser le mot-clé `static` dans une autre fonction statique

Il peut y avoir une situation où vous pourriez avoir besoin d'utiliser les propriétés ou fonctions statiques à l'intérieur d'une autre fonction statique. Vous pouvez faire cela en faisant référence à votre autre propriété/fonction en utilisant ce mot-clé à l'intérieur de la fonction statique.

Modifions notre classe `Chair` pour montrer comment cela fonctionne :

```javascript
class Chair {
//Defaults that will be common for all the instances:
    static backSupport = true;
    static armRests = true;
    
    constructor(color, seatHeight, recliningAngle, headSupport, padding, seatSize, isHeightAdjustable, isMovable){
        //Defaults which can be changed by the subclass class.
        this.color = color;
        this.seatHeight = seatHeight;
        this.recliningAngle = recliningAngle;
        this.headSupport = false;
        this.padding = "3 inch";
        this.seatSize = "16 inch";
        this.isHeightAdjustable = false;
        this.isMovable = false;
        this.type = "Chair";
    } 
        
    static logObjectProps(){
        console.dir(this);
    }

		//Static within static usage
		static printDefaultProps(){
				console.log(`Chair Back Support = ${this.backSupport}`);
				console.log(`Arm rests support = ${this.armRests}`);
		}
    
    adjustableHeight() {};
    adjustAngle(){};
    moveChair(){};    
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-from-2021-12-05-16-49-12.png)
_Sortie du code ci-dessus_

Comme vous pouvez le voir, la fonction `printDefaultProps` a accès aux propriétés statiques `backSupport` et `armRests`.

### Comment appeler des propriétés/fonctions statiques depuis un constructeur

De manière similaire à ce que nous avons vu ci-dessus, vous pouvez également accéder à ces propriétés/fonctions statiques dans un constructeur. Pour ce faire, les choses sont un peu différentes ici.

Dans un constructeur pour appeler une propriété/fonction statique, vous devez utiliser `<classname>.property` ou `<classname>.functionName()`. Cela se produit parce que le mot-clé `this` n'a pas d'accès direct aux membres statiques. Cela n'est pas seulement vrai pour les constructeurs mais aussi pour toute fonction non statique.

Essayons de comprendre cela en modifiant la classe `Chair`.

```javascript
class Chair {
//Defaults that will be common for all the instances:
    static backSupport = true;
    static armRests = true;
    
    constructor(color, seatHeight, recliningAngle, headSupport, padding, seatSize, isHeightAdjustable, isMovable){
        //Defaults which can be changed by the subclass class.
        this.color = color;
        this.seatHeight = seatHeight;
        this.recliningAngle = recliningAngle;
        this.headSupport = false;
        this.padding = "3 inch";
        this.seatSize = "16 inch";
        this.isHeightAdjustable = false;
        this.isMovable = false;
        this.type = "Chair";
		console.log(Chair.printDefaultProps()); //Usage of static method inside constructor
    } 
        
    static logObjectProps(){
        console.dir(this);
    }

		//Static within static usage
		static printDefaultProps(){
				console.log(`Chair Back Support = ${this.backSupport}`);
				console.log(`Arm rests support = ${this.armRests}`);
		}
    
    adjustableHeight() {};
    adjustAngle(){};
    moveChair(){};    
} 
```

Dans le code ci-dessus, la dernière ligne `console.log(Chair.printDefaultProps());` montre comment nous pouvons utiliser une méthode statique à l'intérieur d'un constructeur.

## Membres privés des classes en Javascript

Les membres privés sont des membres de la classe qui ne peuvent être utilisés qu'en interne par la classe elle-même. Ils ne peuvent pas être accessibles en dehors de la classe. Même les instances de la classe ne peuvent pas accéder à ces membres privés.

Tous les membres privés sont déclarés en utilisant la syntaxe `#<propertName>`. Ils sont généralement appelés _hash names_.

Jetez un œil à un exemple basé sur notre cas d'utilisation.

Nous allons définir de nouvelles propriétés à l'intérieur de la classe `OfficeChair`. Supposons que nous voulons ajouter des informations de facturation par défaut pour toutes les chaises de bureau. Nous voulons également que celles-ci soient uniquement accessibles à la classe `OfficeChair` afin que les autres fonctions utilitaires puissent utiliser ces variables.

Nous ne voulons pas que d'autres classes interfèrent avec les informations de facturation d'autres classes. Pour gérer cela, nous pouvons utiliser des champs privés.

Considérez l'ajout des champs suivants :

* Prix
* Remise maximale
* Adresse du vendeur

![Image](https://www.freecodecamp.org/news/content/images/2021/12/chairModel2.drawio--1-.png)
_Diagramme de classe mis à jour_

Notez que nous pouvons représenter les champs privés dans un diagramme de classe en utilisant un tiret, comme ceci : `-`.

Jetez un œil au code ci-dessous qui démontre comment nous avons ajouté ces champs dans la classe `OfficeChair` :

```javascript
class OfficeChair extends Chair {
	//Newly Added Properties
	#basePrice;
	#maxDiscount;
	#sellerAddress;

	constructor(type, color, isHeightAdjustable, seatHeight, recliningAngle) {
		super();
		this.type = type;
		this.color = color;
		this.isHeightAdjustable = isHeightAdjustable;
		this.seatHeight = seatHeight;
		this.recliningAngle = recliningAngle;
		this.isMovable = true;
		this.#basePrice = 1000;
		this.#maxDiscount = 5; //In percentage
		this.#sellerAddress = "XYZ, street";
	}

	adjustableHeight(height) {
		if (height > this.seatHeight) {
			console.log(`Chair height changed to ${height}`);
		} else {
			console.log(`Height cannot be decreased more than the seat height ${this.seatHeight}`);
		}
	}

	adjustAngle(angle) {
		if (angle >= this.recliningAngle) {
			console.log(`Chair angle changed to ${angle}`);
		} else {
			console.log(`Angle cannot be decreased more than the min reclining angle ${this.recliningAngle}`);
		}
	}

	moveChair(x, y) {
		console.log(`Chair moved to co-ordinates = (${x}, ${y})`);
	}

	//Newly Added function
	#getChairAmount(taxCharge) {
		return this.#basePrice + (this.#basePrice - this.#basePrice * this.#maxDiscount / 100) + taxCharge;
	}

	//Newly Added function
	generateBill() {
		console.log("**** BILLING INFORMATION ****");
		console.log(`Chair Price = ${this.#getChairAmount(20)}`);
		console.log(`Seller Address = ${this.#sellerAddress}`);
	}
}
```

Lorsque vous exécutez le code ci-dessus dans la console, vous devriez voir la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-from-2021-12-05-17-03-53.png)
_Sortie des membres privés_

Comme vous pouvez le voir dans la sortie ci-dessus, nous avons exécuté la fonction `generateBill`. Cette fonction accède aux champs privés et à la fonction au sein de la classe pour générer les informations de facturation.

Ces variables privées ne seront accessibles qu'au sein de la classe elle-même. Si vous essayez de référencer l'un des membres privés de la classe, cela générera une erreur de syntaxe comme ci-dessous :

```javascript
Uncaught SyntaxError: Private field '#basePrice' must be declared in an enclosing class
```

Permettez-moi de démontrer comment cela se présentera si une sous-classe essaie d'accéder aux variables privées de la classe de base :

```javascript
class DinningChair extends OfficeChair{}

let dineChair = new DinningChair();
dineChair.#basePrice(); //Throws syntax error
```

Le code ci-dessus générera une erreur de syntaxe puisque vous essayez d'accéder à la propriété privée d'une autre classe.

Les variables statiques privées sont hors du cadre de cet article de blog, donc nous n'en discuterons pas davantage. Mais vous pouvez en lire plus [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_class_fields).

## Résumé

Ce sont quelques-unes des manières dont nous pouvons tirer parti des classes en JavaScript pour implémenter des concepts de programmation orientée objet dans un exemple réel.

Vous pouvez lire plus sur les concepts avancés de la programmation orientée objet ci-dessous :

* [Polymorphisme](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
* [Types d'héritage](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))

Merci d'avoir lu !

Suivez-moi sur [Twitter](https://twitter.com/keurplkar), [GitHub](http://github.com/keyurparalkar) et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).