---
title: Principes SOLID pour la programmation et la conception de logiciels
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-09T22:43:45.000Z'
originalURL: https://freecodecamp.org/news/solid-principles-for-programming-and-software-design
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Untitled1.drawio--1-.png
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: software architecture
  slug: software-architecture
- name: software design
  slug: software-design
- name: solid
  slug: solid
seo_title: Principes SOLID pour la programmation et la conception de logiciels
seo_desc: 'The SOLID principles of object-oriented programming help make object-oriented
  designs more understandable, flexible, and maintainable.

  They also make it easy to create readable and testable code that many developers
  can collaboratively work with anyw...'
---

Les principes SOLID de la programmation orientée objet aident à rendre les conceptions orientées objet plus compréhensibles, flexibles et maintenables.

Ils facilitent également la création de code lisible et testable sur lequel de nombreux développeurs peuvent collaborer n'importe où et n'importe quand. Et ils vous sensibilisent à la meilleure façon d'écrire du code 🔪.

SOLID est un acronyme mnémotechnique qui représente les cinq principes de conception des classes orientées objet. Ces principes sont :

* **S** - Principe de responsabilité unique

* **O** - Principe ouvert-fermé

* **L** - Principe de substitution de Liskov

* **I** - Principe de ségrégation des interfaces

* **D** - Principe d'inversion des dépendances

Dans cet article, vous apprendrez ce que signifient ces principes et comment ils fonctionnent à l'aide d'exemples en JavaScript. Les exemples devraient être compréhensibles même si vous n'êtes pas totalement à l'aise avec JavaScript, car ils s'appliquent également à d'autres langages de programmation.

## Qu'est-ce que le Principe de Responsabilité Unique (SRP) ?

Le Principe de Responsabilité Unique, ou SRP, stipule qu'une classe ne devrait avoir qu'une seule raison de changer. Cela signifie qu'une classe ne devrait avoir qu'un seul travail et faire une seule chose.

Examinons un exemple approprié. Vous serez toujours tenté de regrouper des classes similaires ensemble – mais malheureusement, cela va à l'encontre du principe de responsabilité unique. Pourquoi ?

L'objet `ValidatePerson` ci-dessous a trois méthodes : deux méthodes de validation (`ValidateName()` et `ValidateAge()`), et une méthode `Display()`.

```js
class ValidatePerson {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    ValidateName(name) {
        if (name.length > 3) {
            return true;
        } else {
            return false;
        }
    }

    ValidateAge(age) {
        if (age > 18) {
            return true;
        } else {
            return false;
        }
    }

    Display() {
        if (this.ValidateName(this.name) && this.ValidateAge(this.age)) {
            console.log(`Nom : ${this.name} et Âge : ${this.age}`);
        } else {
            console.log('Invalide');
        }
    }
}
```

La méthode `Display()` va à l'encontre du SRP car le but est qu'une classe ne devrait avoir qu'un seul travail et faire une seule chose. La classe `ValidatePerson` fait deux travaux – elle valide le nom et l'âge de la personne puis affiche des informations.

Pour éviter ce problème, il faut séparer le code qui prend en charge différentes actions et travaux afin que chaque classe ne effectue qu'un seul travail et n'ait qu'une seule raison de changer.

Cela signifie que la classe `ValidatePerson` ne sera responsable que de la validation d'un utilisateur, comme le montre l'exemple ci-dessous :

```js
class ValidatePerson {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    ValidateName(name) {
        if (name.length > 3) {
            return true;
        } else {
            return false;
        }
    }

    ValidateAge(age) {
        if (age > 18) {
            return true;
        } else {
            return false;
        }
    }
}
```

Tandis que la nouvelle classe `DisplayPerson` sera désormais responsable de l'affichage d'une personne, comme vous pouvez le voir dans le bloc de code ci-dessous :

```js
class DisplayPerson {
    constructor(name, age) {
        this.name = name;
        this.age = age;
        this.validate = new ValidatePerson(this.name, this.age);
    }

    Display() {
        if (
            this.validate.ValidateName(this.name) &&
            this.validate.ValidateAge(this.age)
        ) {
            console.log(`Nom : ${this.name} et Âge : ${this.age}`);
        } else {
            console.log('Invalide');
        }
    }
}
```

Ainsi, vous aurez respecté le principe de responsabilité unique, ce qui signifie que nos classes n'ont désormais qu'une seule raison de changer. Si vous souhaitez modifier la classe `DisplayPerson`, cela n'affectera pas la classe `ValidatePerson`.

## Qu'est-ce que le Principe Ouvert-Fermé ?

Le principe ouvert-fermé peut être déroutant car il s'agit d'un principe à double sens. Selon la définition de [Bertrand Meyer](https://en.wikipedia.org/wiki/Bertrand_Meyer) sur [Wikipedia](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle), le **principe ouvert-fermé (OCP)** stipule que les entités logicielles (classes, modules, fonctions, etc.) doivent être ouvertes à l'extension, mais fermées à la modification.

Cette définition peut être déroutante, mais un exemple et une clarification supplémentaire vous aideront à comprendre.

Il y a deux attributs principaux dans l'OCP :

* Il est **ouvert** à l'extension — Cela signifie que vous pouvez étendre ce que le module peut faire.

* Il est **fermé** à la modification — Cela signifie que vous ne pouvez pas changer le code source, même si vous pouvez étendre le comportement d'un module ou d'une entité.

OCP signifie qu'une classe, un module, une fonction et d'autres entités peuvent étendre leur comportement sans modifier leur code source. En d'autres termes, une entité doit être extensible sans modifier l'entité elle-même. Comment ?

Par exemple, supposons que vous avez un tableau de `iceCreamFlavors`, qui contient une liste de saveurs possibles. Dans la classe `makeIceCream`, une méthode `make()` vérifiera si une saveur particulière existe et enregistrera un message.

```js
const iceCreamFlavors = ['chocolate', 'vanilla'];

class makeIceCream {
    constructor(flavor) {
        this.flavor = flavor;
    }

    make() {
        if (iceCreamFlavors.indexOf(this.flavor) > -1) {
            console.log('Grand succès. Vous avez maintenant de la glace.');
        } else {
            console.log('Échec épique. Pas de glace pour vous.');
        }
    }
}
```

Le code ci-dessus ne respecte pas le principe OCP. Pourquoi ? Parce que le code ci-dessus n'est pas ouvert à une extension, ce qui signifie que pour ajouter de nouvelles saveurs, vous devriez modifier directement le tableau `iceCreamFlavors`. Cela signifie que le code n'est plus fermé à la modification. Haha (c'est beaucoup).

Pour corriger cela, vous auriez besoin d'une classe ou d'une entité supplémentaire pour gérer l'ajout, afin de ne plus avoir à modifier le code directement pour faire une extension.

```js
const iceCreamFlavors = ['chocolate', 'vanilla'];

class makeIceCream {
    constructor(flavor) {
        this.flavor = flavor;
    }
    make() {
        if (iceCreamFlavors.indexOf(this.flavor) > -1) {
            console.log('Grand succès. Vous avez maintenant de la glace.');
        } else {
            console.log('Échec épique. Pas de glace pour vous.');
        }
    }
}

class addIceCream {
    constructor(flavor) {
        this.flavor = flavor;
    }
    add() {
        iceCreamFlavors.push(this.flavor);
    }
}
```

Ici, nous avons ajouté une nouvelle classe — `addIceCream` — pour gérer l'ajout au tableau `iceCreamFlavors` en utilisant la méthode `add()`. Cela signifie que votre code est fermé à la modification mais ouvert à une extension car vous pouvez ajouter de nouvelles saveurs sans affecter directement le tableau.

```js
let addStrawberryFlavor = new addIceCream('strawberry');
addStrawberryFlavor.add();
makeStrawberryIceCream.make();
```

De plus, remarquez que le SRP est en place car vous avez créé une nouvelle classe. 😊

## Qu'est-ce que le Principe de Substitution de Liskov ?

En 1987, le Principe de Substitution de Liskov (LSP) a été introduit par [Barbara Liskov](https://en.wikipedia.org/wiki/Barbara_Liskov) lors de sa conférence principale « Data abstraction ». Quelques années plus tard, elle a défini le principe comme suit :

> « Soit Φ(x) une propriété prouvable sur les objets x de type T. Alors Φ(y) devrait être vraie pour les objets y de type S où S est un sous-type de T ».

Pour être honnête, cette définition n'est pas ce que beaucoup de développeurs logiciels veulent voir 😂 — alors laissez-moi la décomposer en une définition liée à la POO.

Le principe définit que dans une hiérarchie d'héritage, les objets d'une superclasse (ou classe parente) doivent être substituables avec des objets de ses sous-classes (ou classe enfant) sans casser l'application ou causer d'erreur.

En termes très simples, vous voulez que les objets de vos sous-classes se comportent de la même manière que les objets de votre superclasse.

Un exemple très courant est le scénario du rectangle et du carré. Il est clair que tous les carrés sont des rectangles car ce sont des quadrilatères avec les quatre angles droits. Mais tous les rectangles ne sont pas des carrés. Pour être un carré, ses côtés doivent avoir la même longueur.

En gardant cela à l'esprit, supposons que vous avez une classe rectangle pour calculer l'aire d'un rectangle et effectuer d'autres opérations comme définir la couleur :

```js
class Rectangle {
    setWidth(width) {
        this.width = width;
    }

    setHeight(height) {
        this.height = height;
    }

    setColor(color) {
        // ...
    }

    getArea() {
        return this.width * this.height;
    }
}
```

Sachant pertinemment que tous les carrés sont des rectangles, vous pouvez hériter des propriétés du rectangle. Puisque la largeur et la hauteur doivent être les mêmes, vous pouvez l'ajuster :

```js
class Square extends Rectangle {
    setWidth(width) {
        this.width = width;
        this.height = width;
    }
    setHeight(height) {
        this.width = height;
        this.height = height;
    }
}
```

En regardant l'exemple, cela devrait fonctionner correctement :

```js
let rectangle = new Rectangle();
rectangle.setWidth(10);
rectangle.setHeight(5);
console.log(rectangle.getArea()); // 50
```

Dans l'exemple ci-dessus, vous remarquerez qu'un rectangle est créé, et la largeur et la hauteur sont définies. Ensuite, vous pouvez calculer la surface correcte.

Mais selon le LSP, vous voulez que les objets de vos sous-classes se comportent de la même manière que les objets de votre superclasse. Cela signifie que si vous remplacez le `Rectangle` par `Square`, tout devrait toujours bien fonctionner :

```js
let square = new Square();
square.setWidth(10);
square.setHeight(5);
```

Vous devriez obtenir 100, car le `setWidth(10)` est censé définir à la fois la largeur et la hauteur à 10. Mais à cause du `setHeight(5)`, cela retournera 25.

```js
let square = new Square();
square.setWidth(10);
square.setHeight(5);
console.log(square.getArea()); // 25
```

Cela viole le LSP. Pour corriger cela, il devrait y avoir une classe générale pour toutes les formes qui contiendra toutes les méthodes génériques que vous voulez que les objets de vos sous-classes aient accès. Ensuite, pour les méthodes individuelles, vous créez une classe individuelle pour le rectangle et le carré.

```js
class Shape {
    setColor(color) {
        this.color = color;
    }
    getColor() {
        return this.color;
    }
}

class Rectangle extends Shape {
    setWidth(width) {
        this.width = width;
    }
    setHeight(height) {
        this.height = height;
    }
    getArea() {
        return this.width * this.height;
    }
}

class Square extends Shape {
    setSide(side) {
        this.side = side;
    }
    getArea() {
        return this.side * this.side;
    }
}
```

De cette manière, vous pouvez définir la couleur et obtenir la couleur en utilisant soit la superclasse ou les sous-classes :

```js
// superclasse
let shape = new Shape();
shape.setColor('red');
console.log(shape.getColor()); // red

// sous-classe
let rectangle = new Rectangle();
rectangle.setColor('red');
console.log(rectangle.getColor()); // red

// sous-classe
let square = new Square();
square.setColor('red');
console.log(square.getColor()); // red
```

## Qu'est-ce que le Principe de Ségrégation des Interfaces ?

Le Principe de Ségrégation des Interfaces (ISP) stipule qu'« un client ne devrait jamais être forcé d'implémenter une interface qu'il n'utilise pas, ou les clients ne devraient pas être forcés de dépendre de méthodes qu'ils n'utilisent pas ». Que signifie cela ?

Tout comme le terme ségrégation signifie — il s'agit de garder les choses séparées, ce qui signifie séparer les interfaces.

**Note :** Par défaut, JavaScript n'a pas d'interfaces, mais ce principe s'applique toujours. Alors explorons cela comme si l'interface existait, afin que vous sachiez comment cela fonctionne pour d'autres langages de programmation comme Java.

Une interface typique contiendra des méthodes et des propriétés. Lorsque vous implémentez cette interface dans une classe, alors la classe doit définir toutes ses méthodes. Par exemple, supposons que vous avez une interface qui définit des méthodes pour dessiner des formes spécifiques.

```js
interface ShapeInterface {
    calculateArea();
    calculateVolume();
}
```

Lorsque n'importe quelle classe implémente cette interface, toutes les méthodes doivent être définies même si vous ne les utiliserez pas ou si elles ne s'appliquent pas à cette classe.

```js
class Square implements ShapeInterface {
    calculateArea(){
        //...
    }
    calculateVolume(){
        //...
    }  
}

class Cuboid implements ShapeInterface {
    calculateArea(){
        //...
    }
    calculateVolume(){
        //...
    }    
}

class Rectangle implements ShapeInterface {
    calculateArea(){
        //...
    }
    calculateVolume(){
        //...
    }   
}
```

En regardant l'exemple ci-dessus, vous remarquerez que vous ne pouvez pas calculer le volume d'un carré ou d'un rectangle. Parce que la classe implémente l'interface, vous devez définir toutes les méthodes, même celles que vous n'utiliserez pas ou dont vous n'aurez pas besoin.

Pour corriger cela, vous devrez séparer l'interface.

```js
interface ShapeInterface {
    calculateArea();
}

interface ThreeDimensionalShapeInterface {
    calculateArea();
    calculateVolume();
}
```

Vous pouvez maintenant implémenter l'interface spécifique qui fonctionne avec chaque classe.

```js
class Square implements ShapeInterface {
    calculateArea(){
        //...
    } 
}

class Cuboid implements ThreeDimensionalShapeInterface {
    calculateArea(){
        //...
    }
    calculateVolume(){
        //...
    }    
}

class Rectangle implements ShapeInterface {
    calculateArea(){
        //...
    }  
}
```

## Qu'est-ce que le Principe d'Inversion des Dépendances ?

Ce principe vise à découpler les modules logiciels de manière à ce que les modules de haut niveau (qui fournissent une logique complexe) soient facilement réutilisables et non affectés par les changements dans les modules de bas niveau (qui fournissent des fonctionnalités utilitaires).

Selon [Wikipedia](https://en.wikipedia.org/wiki/Dependency_inversion_principle), ce principe stipule que :

1. Les modules de haut niveau ne doivent pas importer quoi que ce soit des modules de bas niveau. Les deux doivent dépendre d'abstractions (par exemple, des interfaces).

2. Les abstractions doivent être indépendantes des détails. Les détails (implémentations concrètes) doivent dépendre des abstractions.

En termes simples, ce principe stipule que vos classes doivent dépendre d'interfaces ou de classes abstraites plutôt que de classes et de fonctions concrètes. Cela rend vos classes ouvertes à l'extension, en suivant le principe ouvert-fermé.

Regardons un exemple. Lorsque vous construisez un magasin, vous voudrez que votre magasin utilise une passerelle de paiement comme Stripe ou toute autre méthode de paiement préférée. Vous pourriez écrire votre code étroitement couplé à cette API sans penser à l'avenir.

Mais alors, que se passe-t-il si vous découvrez une autre passerelle de paiement qui offre un bien meilleur service, disons PayPal ? Alors, il devient difficile de passer de Stripe à PayPal, ce qui ne devrait pas être un problème en programmation et en conception de logiciels.

```js
class Store {
    constructor(user) {
        this.stripe = new Stripe(user);
    }

    purchaseBook(quantity, price) {
        this.stripe.makePayment(price * quantity);
    }

    purchaseCourse(quantity, price) {
        this.stripe.makePayment(price * quantity);
    }
}

class Stripe {
    constructor(user) {
        this.user = user;
    }

    makePayment(amountInDollars) {
        console.log(`${this.user} a effectué un paiement de ${amountInDollars}`);
    }
}
```

En considérant l'exemple ci-dessus, vous remarquerez que si vous changez la passerelle de paiement, vous n'aurez pas seulement besoin d'ajouter la classe — vous devrez également apporter des modifications à la classe `Store`. Cela ne va pas seulement à l'encontre du Principe d'Inversion des Dépendances, mais aussi à l'encontre du principe ouvert-fermé.

Pour corriger cela, vous devez vous assurer que vos classes dépendent d'interfaces ou de classes abstraites plutôt que de classes et de fonctions concrètes. Pour cet exemple, cette interface contiendra tous les comportements que vous voulez que votre API ait et ne dépendra de rien. Elle sert d'intermédiaire entre les modules de haut niveau et de bas niveau.

```js
class Store {
    constructor(paymentProcessor) {
        this.paymentProcessor = paymentProcessor;
    }

    purchaseBook(quantity, price) {
        this.paymentProcessor.pay(quantity * price);
    }

    purchaseCourse(quantity, price) {
        this.paymentProcessor.pay(quantity * price);
    }
}

class StripePaymentProcessor {
    constructor(user) {
        this.stripe = new Stripe(user);
    }

    pay(amountInDollars) {
        this.stripe.makePayment(amountInDollars);
    }
}

class Stripe {
    constructor(user) {
        this.user = user;
    }

    makePayment(amountInDollars) {
        console.log(`${this.user} a effectué un paiement de ${amountInDollars}`);
    }
}

let store = new Store(new StripePaymentProcessor('John Doe'));
store.purchaseBook(2, 10);
store.purchaseCourse(1, 15);
```

Dans le code ci-dessus, vous remarquerez que la classe `StripePaymentProcessor` est une interface entre la classe `Store` et la classe `Stripe`. Dans une situation où vous devez utiliser PayPal, tout ce que vous avez à faire est de créer un `PayPalPaymentProcessor` qui fonctionnerait avec la classe `PayPal`, et tout fonctionnera sans affecter la classe `Store`.

```js
class Store {
    constructor(paymentProcessor) {
        this.paymentProcessor = paymentProcessor;
    }

    purchaseBook(quantity, price) {
        this.paymentProcessor.pay(quantity * price);
    }

    purchaseCourse(quantity, price) {
        this.paymentProcessor.pay(quantity * price);
    }
}

class PayPalPaymentProcessor {
    constructor(user) {
        this.user = user;
        this.paypal = new PayPal();
    }

    pay(amountInDollars) {
        this.paypal.makePayment(this.user, amountInDollars);
    }
}

class PayPal {
    makePayment(user, amountInDollars) {
        console.log(`${user} a effectué un paiement de ${amountInDollars}`);
    }
}

let store = new Store(new PayPalPaymentProcessor('John Doe'));
store.purchaseBook(2, 10);
store.purchaseCourse(1, 15);
```

Vous remarquerez également que cela suit le Principe de Substitution de Liskov car vous pouvez le remplacer par d'autres implémentations de la même interface sans casser votre application.

## Ta-Da 😇

Cela a été une aventure👋. J'espère que vous avez remarqué que chacun de ces principes est lié aux autres d'une certaine manière.

En tentant de corriger un principe, disons le principe d'inversion des dépendances, vous assurez indirectement que vos classes sont ouvertes à l'extension mais fermées à la modification, par exemple.

Vous devriez garder ces principes à l'esprit lors de l'écriture de code, car ils facilitent la collaboration de nombreuses personnes sur votre projet. Ils simplifient le processus d'extension, de modification, de test et de refactorisation de votre code. Assurez-vous donc de comprendre leurs définitions, ce qu'ils font et pourquoi vous en avez besoin au-delà de la POO.

Pour une meilleure compréhension, vous pouvez regarder [cette vidéo](https://www.youtube.com/watch?v=XzdhzyAukMM) de [Beau Carnes](https://www.freecodecamp.org/news/author/beau/) sur la [chaîne YouTube freeCodeCamp](https://www.youtube.com/c/Freecodecamp) ou lire [cet article](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/) de [Yiğit Kemal Erinç](https://www.freecodecamp.org/news/author/erinc/).

Amusez-vous bien à coder !

Vous pouvez accéder à plus de 200 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.