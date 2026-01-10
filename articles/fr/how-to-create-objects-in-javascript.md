---
title: Comment créer des objets en JavaScript
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-05-10T06:22:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-objects-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--9-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment créer des objets en JavaScript
seo_desc: "In programming, objects are fundamental building blocks used to represent\
  \ real-world entities or concepts. JavaScript, a versatile and popular language,\
  \ offers various ways to create these objects. \nThis article dives deep into these\
  \ methods, equippi..."
---

En programmation, les objets sont des blocs de construction fondamentaux utilisés pour représenter des entités ou des concepts du monde réel. JavaScript, un langage polyvalent et populaire, offre diverses façons de créer ces objets. 

Cet article explore en profondeur ces méthodes, vous équipant des connaissances nécessaires pour créer des objets adaptés à vos besoins de programmation.

Nous commencerons par explorer le concept d'objets en JavaScript et les avantages qu'ils apportent. Ensuite, nous passerons en revue les différentes méthodes de création : les littéraux d'objets, les fonctions constructeurs et la méthode `Object.create()`. Chaque méthode sera expliquée en détail, avec des exemples pour consolider votre compréhension.

À la fin de ce guide complet, vous serez en mesure de choisir en toute confiance l'approche la plus adaptée pour créer des objets dans vos projets JavaScript. Non seulement vous acquerrez les connaissances techniques, mais vous découvrirez également les meilleures pratiques pour garantir que votre code orienté objet est efficace et bien structuré.

## Table des matières

1. **[Qu'est-ce que les objets en JavaScript ?](#heading-quest-ce-que-les-objets-en-javascript)**
2. **[Comment créer des objets en JavaScript](#heading-comment-creer-des-objets-avec-les-litteraux-dobjets)**

* [Comment ajouter des propriétés et des méthodes](#heading-comment-ajouter-des-proprietes-et-des-methodes)
* [Comment imbriquer des objets et des tableaux](#heading-comment-imbriquer-des-objets-et-des-tableaux)
* [Comment créer un exemple d'objet Personne](#heading-comment-creer-un-exemple-dobjet-personne)

3. **[Comment utiliser les fonctions constructeurs pour créer des objets](#heading-comment-utiliser-les-fonctions-constructeurs-pour-creer-des-objets)**

* [Comment définir une fonction constructeur](#heading-comment-definir-une-fonction-constructeur)
* [Comment utiliser le mot-clé `new`](#heading-comment-utiliser-le-mot-cle-new)
* [Comment ajouter des propriétés et des méthodes au prototype](#heading-comment-ajouter-des-proprietes-et-des-methodes-au-prototype)
* [Comment créer un exemple d'objet Sac à main](#heading-comment-creer-un-exemple-dobjet-sac-a-main)

4. **[Comment utiliser la méthode `Object.create()` pour créer des objets](#heading-comment-utiliser-la-methode-objectcreate-pour-creer-des-objets)**

* [Comment spécifier un objet prototype](#heading-comment-specifier-un-objet-prototype)
* [Comment créer un objet avec un prototype spécifique Exemple](#heading-comment-creer-un-objet-avec-un-prototype-specifique-exemple)

5. **[Pourquoi créer des objets en JavaScript ?](#heading-pourquoi-creer-des-objets-en-javascript)**

6. [Comment choisir la bonne méthode pour créer des objets](#heading-comment-choisir-la-bonne-methode-pour-creer-des-objets-en-javascript)

* [Quand utiliser les littéraux d'objets](#heading-quand-utiliser-les-litteraux-dobjets)
* [Quand utiliser les fonctions constructeurs et les classes](#heading-quand-utiliser-les-fonctions-constructeurs-et-les-classes)
* [Quand utiliser `Object.create()`](#heading-quand-utiliser-objectcreate)
* [Exemples de scénarios](#heading-exemples-de-scenarios)

7. **[Meilleures pratiques pour la création d'objets en JavaScript](#heading-meilleures-pratiques-pour-la-creation-dobjets-en-javascript)**

8. **[Conclusion](#heading-conclusion)**

## Qu'est-ce que les objets en JavaScript ?

En JavaScript, les objets sont des structures de données qui stockent des collections de données et de fonctionnalités liées. Ils sont composés de paires clé-valeur, où chaque clé est une chaîne (ou un symbole) et chaque valeur peut être de n'importe quel type de données, y compris d'autres objets, des tableaux, des fonctions, et plus encore. 

Les objets sont polyvalents et couramment utilisés pour représenter des entités ou des concepts du monde réel dans le code. 

## Comment créer des objets avec des littéraux d'objets

En JavaScript, vous pouvez créer des objets en utilisant des littéraux d'objets. La syntaxe pour créer un littéral d'objet est la suivante :

```javascript
let nomObjet = {
  cle1: valeur1,
  cle2: valeur2,
  // Plus de paires clé-valeur si nécessaire
};

```

* `nomObjet` : C'est le nom que vous attribuez à votre variable d'objet.
* `{ cle1: valeur1, cle2: valeur2 }` : Cette partie est enfermée dans des accolades `{}` et représente le littéral d'objet. Chaque paire clé-valeur est séparée par un deux-points `:` et les paires individuelles sont séparées par des virgules `,`.

### Comment ajouter des propriétés et des méthodes

Vous pouvez ajouter des propriétés et des méthodes à votre littéral d'objet en les spécifiant comme des paires clé-valeur. Les propriétés contiennent des valeurs de données, tandis que les méthodes sont des fonctions associées à l'objet :

```javascript
let nomObjet = {
  propriete1: valeur1,
  propriete2: valeur2,
  methode1: function() {
    // Définition de la méthode
  }
};

```

### Comment imbriquer des objets et des tableaux

Vous pouvez imbriquer des objets et des tableaux dans un littéral d'objet pour créer des structures de données plus complexes :

```javascript
let nomObjet = {
  propriete1: valeur1,
  objetImbrique: {
    proprieteImbriquee: valeurImbriquee
  },
  tableauImbrique: [element1, element2, element3]
};

```

### Comment créer un exemple d'objet Personne

Créons un exemple d'objet personne en utilisant des littéraux d'objets :

```javascript
// Création d'un objet personne
let personne = {
  nom: "Bella Nwachukwu",
  age: 29,
  adresse: {
    rue: "123 Rue Ade",
    ville: "Lagos",
    codePostal: "10001"
  },
  passeTemps: ["lecture", "voyage", "programmation"],
  saluer: function() {
    return "Bonjour, je m'appelle " + this.nom + " et j'ai " + this.age + " ans.";
  }
};

// Accès aux propriétés et méthode de l'objet personne
console.log(personne.nom); // Sortie : Bella Nwachukwu
console.log(personne.adresse.ville); // Sortie : Lagos
console.log(personne.passeTemps[0]); // Sortie : lecture
console.log(personne.saluer()); // Sortie : Bonjour, je m'appelle Bella Nwachukwu et j'ai 29 ans.

```

Dans cet exemple :

* Nous avons créé un objet `personne` avec des propriétés comme `nom`, `age`, `adresse`, `passeTemps`, et une méthode `saluer`.
* La propriété `adresse` est elle-même un objet avec des propriétés imbriquées.
* La propriété `passeTemps` est un tableau contenant plusieurs éléments.
* La méthode `saluer` retourne un message de salutation en utilisant le nom et l'âge de la personne.

## Comment utiliser les fonctions constructeurs pour créer des objets

### Comment définir une fonction constructeur

Une fonction constructeur est une fonction JavaScript utilisée pour créer et initialiser des objets. Elle sert de plan pour créer plusieurs objets avec des propriétés et des méthodes similaires :

```javascript
function NomConstructeur(param1, param2) {
  this.propriete1 = param1;
  this.propriete2 = param2;
  // Propriétés et méthodes supplémentaires si nécessaire
}

```

* `NomConstructeur` : C'est le nom que vous attribuez à votre fonction constructeur.
* `param1, param2` : Ce sont des paramètres que la fonction constructeur accepte pour initialiser les propriétés de l'objet.

### Comment utiliser le mot-clé `new`

Vous pouvez créer une instance d'un objet en utilisant le mot-clé `new` suivi du nom de la fonction constructeur et en passant les paramètres requis.

```javascript
let nomInstance = new NomConstructeur(valeur1, valeur2);

```

* `nomInstance` : C'est le nom de variable attribué à la nouvelle instance d'objet créée.

### Comment ajouter des propriétés et des méthodes au prototype

Pour ajouter des propriétés et des méthodes partagées entre toutes les instances d'objets créées à partir de la fonction constructeur, vous pouvez utiliser la propriété prototype de la fonction constructeur :

```javascript
NomConstructeur.prototype.nomMethode = function() {
  // Définition de la méthode
};

```

### Comment créer un exemple d'objet Sac à main

Créons un exemple en utilisant une fonction constructeur pour représenter un objet `SacAMain`, car les sacs à main sont quelque chose que j'aime :

```javascript
// Définir la fonction constructeur
function SacAMain(marque, couleur, prix) {
  this.marque = marque;
  this.couleur = couleur;
  this.prix = prix;
}

// Ajouter une méthode au prototype
SacAMain.prototype.obtenirDescription = function() {
  return "Un " + this.couleur + " " + this.marque + " sac à main, au prix de $" + this.prix + ".";
};

// Créer une instance de l'objet SacAMain
let monSacAMain = new SacAMain('Louis Vuitton', 'marron', 2000);

// Accès aux propriétés et méthode de l'objet sac à main
console.log(monSacAMain.marque); // Sortie : Louis Vuitton
console.log(monSacAMain.obtenirDescription()); // Sortie : Un sac à main marron Louis Vuitton, au prix de $2000.

```

Dans cet exemple :

* Nous définissons une fonction constructeur `SacAMain` qui accepte les paramètres `marque`, `couleur` et `prix` pour initialiser les objets sac à main.
* Nous ajoutons une méthode `obtenirDescription` au prototype de la fonction constructeur `SacAMain` pour retourner une description du sac à main.
* Nous créons une instance de l'objet `SacAMain` nommée `monSacAMain` en utilisant le mot-clé `new` et fournissons des valeurs pour les paramètres.
* Nous accédons ensuite aux propriétés et à la méthode de l'objet `monSacAMain` en utilisant la notation par points.

## Comment utiliser la méthode `Object.create()` pour créer des objets

La méthode `Object.create()` est utilisée pour créer un nouvel objet avec l'objet prototype spécifié et éventuellement des propriétés supplémentaires. Sa syntaxe est la suivante :

```javascript
Object.create(proto[, propertiesObject])

```

* `proto` : L'objet prototype à utiliser pour créer le nouvel objet. Il peut être `null` ou un objet.
* `propertiesObject` (optionnel) : Un objet dont les propriétés définissent des propriétés supplémentaires à ajouter au nouvel objet créé. Les propriétés de cet objet correspondent aux propriétés à ajouter à l'objet créé, avec leurs valeurs étant des descripteurs de propriétés.

### Comment spécifier un objet prototype

En passant un objet prototype comme premier argument à `Object.create()`, vous pouvez spécifier le prototype du nouvel objet. 

L'objet prototype sert de modèle à partir duquel le nouvel objet hérite des propriétés.

### Comment créer un objet avec un prototype spécifique Exemple

Créons un exemple d'utilisation de `Object.create()` pour créer un objet avec un prototype spécifique :

```javascript
// Définir un objet prototype
let prototypePersonne = {
  saluer: function() {
    return "Bonjour, je m'appelle " + this.nom + ".";
  }
};

// Créer un nouvel objet en utilisant le prototypePersonne comme prototype
let john = Object.create(prototypePersonne);

// Ajouter des propriétés au nouvel objet
john.nom = "John";

// Accès aux propriétés et méthode de l'objet john
console.log(john.nom); // Sortie : John
console.log(john.saluer()); // Sortie : Bonjour, je m'appelle John.

```

Dans cet exemple :

* Nous définissons un objet `prototypePersonne` avec une méthode `saluer`.
* Nous créons un nouvel objet nommé `john` en utilisant `Object.create(prototypePersonne)`, ce qui définit `prototypePersonne` comme le prototype de `john`.
* Nous ajoutons une propriété `nom` à l'objet `john`.
* Nous accédons ensuite aux propriétés et à la méthode de l'objet `john` en utilisant la notation par points.

## Pourquoi créer des objets en JavaScript ?

Créer des objets en JavaScript vous permet d'organiser et de gérer les données de manière structurée. Voici quelques raisons pour lesquelles la création d'objets est bénéfique :

* **Organisation** : Les objets aident à organiser les données et les fonctionnalités liées en une seule entité. Par exemple, si vous travaillez avec des informations sur une personne, vous pouvez stocker son nom, son âge, son adresse et d'autres détails dans un seul objet.

```javascript
// Exemple d'organisation de données liées dans un objet
let personne = {
  nom: "John Doe",
  age: 25,
  adresse: {
    rue: "123 Rue Principale",
    ville: "New York",
    codePostal: "10001"
  }
};

// Accès aux propriétés de l'objet personne
console.log(personne.nom); // Sortie : John Doe
console.log(personne.adresse.ville); // Sortie : New York

```

* **Encapsulation** : Les objets encapsulent les données et les comportements associés, ce qui favorise un code plus propre et plus modulaire. Au lieu d'avoir des variables et des fonctions dispersées, vous pouvez les regrouper dans un objet, rendant votre code plus facile à comprendre et à maintenir.

```javascript
// Exemple d'encapsulation de données et de comportement dans un objet
let calculatrice = {
  additionner: function(a, b) {
    return a + b;
  },
  soustraire: function(a, b) {
    return a - b;
  }
};

// Utilisation de l'objet calculatrice pour effectuer des calculs
console.log(calculatrice.additionner(5, 3)); // Sortie : 8
console.log(calculatrice.soustraire(10, 4)); // Sortie : 6

```

* **Réutilisabilité** : Une fois que vous avez créé un objet, vous pouvez le réutiliser dans tout votre code. Cela vous évite d'écrire du code répétitif et favorise la réutilisation du code, ce qui est un principe fondamental de l'ingénierie logicielle.

```javascript
// Exemple de réutilisation d'une définition d'objet plusieurs fois
function creerPersonne(nom, age) {
  return {
    nom: nom,
    age: age,
    saluer: function() {
      return "Bonjour, je m'appelle " + this.nom + " et j'ai " + this.age + " ans.";
    }
  };
}

let personne1 = creerPersonne("Alice", 30);
let personne2 = creerPersonne("Bob", 25);

console.log(personne1.saluer()); // Sortie : Bonjour, je m'appelle Alice et j'ai 30 ans.
console.log(personne2.saluer()); // Sortie : Bonjour, je m'appelle Bob et j'ai 25 ans.

```

* **Flexibilité** : Les objets en JavaScript sont dynamiques, ce qui signifie que vous pouvez facilement ajouter, modifier ou supprimer des propriétés et des méthodes à l'exécution. Cette flexibilité vous permet d'adapter votre code à des exigences ou des scénarios changeants sans trop de difficultés.
* **Passage par référence** : Les objets sont passés par référence en JavaScript, ce qui signifie que lorsque vous attribuez un objet à une variable ou le passez comme argument à une fonction, vous passez en réalité une référence au même objet en mémoire. Cela peut être utile pour travailler avec des structures de données complexes ou implémenter des techniques de programmation avancées.

## Comment choisir la bonne méthode pour créer des objets en JavaScript

Cela dépend de divers facteurs, y compris la complexité de votre application, vos préférences de style de codage et les exigences spécifiques de votre projet. Voici un guide général sur quand utiliser chaque méthode :

### Quand utiliser les littéraux d'objets

Utilisez les littéraux d'objets lorsque vous avez besoin d'une manière simple et directe pour créer des objets avec un ensemble fixe de propriétés et de méthodes. Les littéraux d'objets sont idéaux pour :

* Créer des objets simples et uniques.
* Définir des objets de configuration.
* Créer des objets avec une structure connue qui ne changera pas fréquemment.

### Quand utiliser les fonctions constructeurs et les classes

Utilisez les fonctions constructeurs et les classes ES6 lorsque vous devez créer plusieurs instances d'objets avec des propriétés et des méthodes partagées. Les fonctions constructeurs et les classes sont adaptées pour :

* Créer des objets avec un comportement et un état.
* Implémenter l'héritage et le polymorphisme.
* Créer des composants et des modules réutilisables.
* Organiser le code de manière plus orientée objet.

### Quand utiliser `Object.create()`

Utilisez `Object.create()` lorsque vous avez besoin d'un contrôle plus fin sur la chaîne de prototypes ou lorsque vous souhaitez créer des objets avec des prototypes spécifiques. `Object.create()` est adapté pour :

* Créer des objets avec un prototype spécifique sans invoquer de fonction constructeur.
* Implémenter l'héritage basé sur les prototypes.
* Créer des objets avec des propriétés et des méthodes partagées.

### Exemples de scénarios

* **Littéraux d'objets** : Utilisez lors de la création d'un objet de configuration pour une petite fonction utilitaire :

```javascript
let config = {
  apiUrl: "https://example.com/api",
  timeout: 5000
};

```

* **Fonctions constructeurs et classes** : Utilisez lors de la création d'instances d'objets complexes avec un comportement :

```javascript
class Personne {
  constructor(nom, age) {
    this.nom = nom;
    this.age = age;
  }

  saluer() {
    return `Bonjour, je m'appelle ${this.nom} et j'ai ${this.age} ans.`;
  }
}

let personne1 = new Personne("Alice", 30);

```

* **Object.create()** : Utilisez lors de la création d'objets avec des prototypes spécifiques :

```javascript
let animal = {
  parler() {
    return "Un son";
  }
};

let chien = Object.create(animal);
chien.race = "Labrador";

```

## Meilleures pratiques pour la création d'objets en JavaScript

### 1. Utilisez les littéraux d'objets pour les structures simples

Pour les structures de données simples avec un ensemble fixe de propriétés, utilisez les littéraux d'objets. Ils fournissent une syntaxe concise pour définir des objets.

### 2. Préférez les fonctions constructeurs ou les classes pour les objets complexes

Pour les objets avec un comportement et des propriétés partagées, utilisez les fonctions constructeurs ou les classes ES6. Elles permettent l'encapsulation, l'héritage et le polymorphisme.

### 3. Favorisez les classes pour le JavaScript moderne

Dans le JavaScript moderne, les classes ES6 fournissent une syntaxe plus propre pour définir des plans d'objets. Elles sont plus faciles à comprendre et à maintenir par rapport aux fonctions constructeurs traditionnelles.

### 4. Utilisez les fonctions de fabrication pour la création d'objets

Les fonctions de fabrication sont des fonctions qui retournent de nouveaux objets. Elles fournissent un moyen d'encapsuler la logique de création d'objets et permettent plus de flexibilité dans la création d'instances.

### 5. Utilisez `Object.create()` pour l'héritage prototypal explicite

Utilisez `Object.create()` lorsque vous devez définir explicitement la chaîne de prototypes ou créer des objets avec des prototypes spécifiques. Cela est particulièrement utile pour l'héritage basé sur les prototypes.

### 6. Encapsulez la logique d'initialisation

Si un objet nécessite une logique d'initialisation complexe, encapsulez-la dans la fonction constructeur ou une fonction de fabrication pour garder le processus de création d'objets propre et compréhensible.

### 7. Évitez les mutations excessives

Minimisez la mutation directe des propriétés d'objets, en particulier des objets partagés. Au lieu de cela, favorisez l'immuabilité ou utilisez des techniques comme les getters et les setters pour un accès contrôlé.

### 8. Suivez les conventions de nommage

Suivez les conventions de nommage pour les fonctions constructeurs, les classes et les fonctions de fabrication. Utilisez le PascalCase pour les fonctions constructeurs et les classes, et le camelCase pour les fonctions de fabrication.

### 9. Favorisez la composition plutôt que l'héritage

Préférez la composition à l'héritage lors de la structuration d'objets complexes. La composition favorise la réutilisation du code et est souvent plus flexible que l'héritage.

### 10. Documentez les structures et les comportements des objets

Documentez la structure et le comportement de vos objets, y compris les propriétés, les méthodes et leur utilisation prévue. Cela aide les autres développeurs à comprendre et à utiliser votre code efficacement.

## Conclusion

En conclusion, nous avons exploré les littéraux d'objets, les fonctions constructeurs, la méthode `Object.create()` et les classes ES6, chacune avec ses forces et ses cas d'utilisation.

Maintenant, vous pouvez choisir stratégiquement la bonne approche pour les structures orientées objet dans vos applications JavaScript.

Rappelez-vous, les littéraux d'objets excellent dans la création d'objets simples, tandis que les fonctions constructeurs et les classes sont idéales pour les plans d'objets réutilisables avec des propriétés et des méthodes partagées. La méthode `Object.create()` offre un contrôle plus granulaire sur l'héritage des objets.

Gardez ces meilleures pratiques à l'esprit, utilisez efficacement les propriétés et les méthodes des objets, privilégiez la lisibilité du code et n'hésitez pas à revisiter ce guide comme référence. 

Connectez-vous avec moi sur [LinkedIn](https://ng.linkedin.com/in/joan-ayebola).