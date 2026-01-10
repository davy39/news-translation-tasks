---
title: Principe Ouvert-Fermé – Concept d'Architecture SOLID Expliqué
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-02-22T15:50:42.000Z'
originalURL: https://freecodecamp.org/news/open-closed-principle-solid-architecture-concept-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/chests-34153_1280.png
tags:
- name: software development
  slug: software-development
- name: solid
  slug: solid
seo_title: Principe Ouvert-Fermé – Concept d'Architecture SOLID Expliqué
seo_desc: 'The Open-Closed principle (OCP) is one the 5 SOLID design principles. It
  was popularized by the American computer scientist and instructor, Robert C. Martin
  (aka Uncle Bob) in a paper he published in 2000.

  The other 4 SOLID design principles are:


  Si...'
---

Le principe Ouvert-Fermé (OCP) est l'un des 5 principes de conception SOLID. Il a été popularisé par l'informaticien et instructeur américain, Robert C. Martin (alias Uncle Bob) dans un article qu'il a publié en 2000.

Les 4 autres principes de conception SOLID sont :
- Principe de Responsabilité Unique (SRP)
- Principe de Substitution de Liskov (LSP)
- Principe de Ségrégation des Interfaces (ISP)
- Principe d'Inversion des Dépendances (DIP).

Si vous souhaitez en apprendre davantage sur tous ces principes, vous pouvez lire mon tutoriel sur les [principes SOLID ici](https://www.freecodecamp.org/news/solid-design-principles-in-software-development/).

Dans cet article, je vais vous montrer ce que signifie le principe Ouvert-Fermé (OCP), pourquoi vous devriez l'utiliser, et son implémentation en JavaScript.

## Ce que nous allons couvrir
- [Qu'est-ce que le Principe Ouvert-Fermé ?](#heading-quest-ce-que-le-principe-ouvert-ferme)
- [Pourquoi devriez-vous utiliser le Principe Ouvert-Fermé ?](#heading-pourquoi-devriez-vous-utiliser-le-principe-ouvert-ferme)
- [Comment implémenter le Principe Ouvert-Fermé en JavaScript](#heading-comment-implementer-le-principe-ouvert-ferme-en-javascript)
- [Conclusion](#heading-conclusion)

## Qu'est-ce que le Principe Ouvert-Fermé ?
Le principe Ouvert-Fermé stipule que les entités logicielles (classes, modules, fonctions, etc.) doivent être ouvertes à l'extension, mais fermées à la modification.

Vous vous demandez probablement pourquoi cette déclaration semble être une contradiction. Comment quelque chose peut-il être à la fois ouvert et fermé ?

Eh bien, dans le monde du développement logiciel, il est possible qu'un élément soit ouvert à l'extension et fermé à la modification. Cela signifie que vous ou les membres de votre équipe devriez pouvoir ajouter de nouvelles fonctionnalités à un système logiciel existant sans modifier le code existant.

Le principe Ouvert-Fermé encourage les ingénieurs logiciels à se concentrer sur ce qui est nécessaire lorsqu'il est temps d'ajouter de nouvelles fonctionnalités.

Si vous souhaitez ajouter une nouvelle fonctionnalité à votre code existant et que vous devez le modifier avant d'ajouter la nouvelle fonctionnalité, alors vous ne suivez pas le principe Ouvert-Fermé.

## Pourquoi devriez-vous utiliser le Principe Ouvert-Fermé ?
Voici quelques raisons pour lesquelles vous devriez utiliser le principe Ouvert-Fermé :

- **Vous n'avez pas besoin de réinventer la roue** : comme le stipule le principe, le code sur lequel vous et votre équipe travaillez est fermé à l'extension. Cela signifie que si vous suivez le principe Ouvert-Fermé, vous n'avez pas besoin de réinventer la roue (et de tout reconstruire) lorsque vous souhaitez ajouter de nouvelles fonctionnalités.

- **Vous vous concentrez sur ce qui est nécessaire** : comme le stipule l'OCP, votre code est fermé à la modification. Cela signifie que vous pouvez ajouter de nouvelles fonctionnalités sans effectuer trop de modifications sur le code existant, voire aucune. Cela peut vous aider, vous et les membres de votre équipe, à vous concentrer sur ce qui est nécessaire lorsqu'il est temps d'implémenter de nouvelles fonctionnalités.

- **Vous pouvez éviter les bugs** : puisque vous n'avez pas à modifier le code existant avant d'ajouter de nouvelles fonctionnalités, vous pouvez éviter d'introduire des bugs inutiles.

- **Votre code est plus maintenable, testable et flexible** : suivre l'OCP rendra votre base de code faiblement couplée. Ainsi, le code est plus flexible et maintenable. Et si vous le souhaitez, vous pouvez tester chaque classe avec succès.

## Comment implémenter le Principe Ouvert-Fermé en JavaScript
Le premier exemple du principe Ouvert-Fermé que je vais montrer est une classe utilisant un switch ou plusieurs instructions if. C'est parce que dans un code comme celui-ci, il y a une réelle possibilité que vous modifiiez la classe utilisant le switch ou les instructions if. Et cela viole le principe Ouvert-Fermé dans le processus.

```js
class Footballeur {
  constructor(nom, age, role) {
    this.nom = nom;
    this.age = age;
    this.role = role;
  }

  getRoleFootballeur() {
    switch (this.role) {
      case 'gardien' :
        console.log(`Le footballeur, ${this.nom} est un gardien`);
        break;
      case 'defenseur' :
        console.log(`Le footballeur, ${this.nom} est un defenseur`);
        break;
      case 'milieu' :
        console.log(`Le footballeur, ${this.nom} est un milieu`);
        break;
      case 'attaquant' :
        console.log(`Le footballeur, ${this.nom} joue en attaque`);
        break;
      default:
        throw new Error(`Type de role non supporté : ${this.type}`);
    }
  }
}

const kante = new Footballeur('Ngolo Kante', 31, 'milieu');
const hazard = new Footballeur('Eden Hazard', 32, 'attaquant');

kante.getRoleFootballeur(); // Le footballeur, Ngolo Kante est un milieu
hazard.getRoleFootballeur(); // Le footballeur, Eden Hazard joue en attaque
```

Il existe d'autres rôles de footballeurs comme ailier, milieu défensif, etc. Donc, dans le code ci-dessus, que pensez-vous qu'il se passerait si vous deviez ajouter un autre rôle de footballeur sur le terrain ? Vous devriez modifier l'instruction `switch`. Cela viole le principe Ouvert-Fermé car vous devez modifier le code existant.

Pour corriger la violation, vous devez créer une classe de rôle séparée pour consommer la méthode qui obtient le rôle du joueur depuis la classe parente. Mais cela ne s'arrête pas là. Vous devez ensuite créer une classe différente pour chaque rôle qui étend la classe qui obtient le rôle du joueur.

Cela sera plus clair en code :

```js
class Footballeur {
  constructor(nom, age, role) {
    this.nom = nom;
    this.age = age;
    this.role = role;
  }

  getRole() {
    return this.role.getRole();
  }
}

// La classe RoleJoueur utilise la méthode getRole
class RoleJoueur {
  getRole() {}
}

// Les sous-classes pour différents rôles étendent la classe RoleJoueur
class RoleGardien extends RoleJoueur {
  getRole() {
    return 'gardien';
  }
}

class RoleDefenseur extends RoleJoueur {
  getRole() {
    return 'defenseur';
  }
}

class RoleMilieu extends RoleJoueur {
  getRole() {
    return 'milieu';
  }
}

class RoleAttaquant extends RoleJoueur {
  getRole() {
    return 'attaquant';
  }
}

// Mettre tout ensemble
const hazard = new Footballeur('Hazard', 32, new RoleAttaquant());
console.log(`${hazard.nom} joue en ${hazard.getRole()}`); // Hazard joue en attaque

const kante = new Footballeur('Ngolo Kante', 31, new RoleMilieu());
console.log(`${kante.nom} est le meilleur ${kante.getRole()} du monde !`); // Ngolo Kante est le meilleur milieu du monde !
```

Voici un autre exemple qui utilise des fonctions au lieu de classes JavaScript :

```js
function calculerPrix(prix, remise) {
  if (remise === '10%') {
    return prix * 0.9;
  } else if (remise === '20%') {
    return prix * 0.8;
  } else if (remise === '30%') {
    return prix * 0.7;
  } else {
    throw new Error('Remise invalide');
  }
}

const prixRemise = calculerPrix(100, '10%');
console.log(`Votre prix remisé est ${prixRemise}`); // Le prix remisé est 90
```

Le code ci-dessus viole le principe Ouvert-Fermé car vous devez ajouter une autre instruction `if...else` si vous souhaitez ajouter une nouvelle remise.

Pour le corriger, vous pouvez extraire toutes vos remises dans un objet et l'utiliser dans la fonction de cette manière :

```js
const remises = {
  '10%': 0.9,
  '20%': 0.8,
  '30%': 0.7,
};

function calculerPrix(prix, typeRemise) {
  const remise = remises[typeRemise];
  if (remise === undefined) {
    throw new Error('Remise invalide');
  }
  return prix * remise;
}

const prixRemise = calculerPrix(100, '30%');
console.log(`Votre prix remisé est $${prixRemise}`);
```

Maintenant, si vous souhaitez ajouter de nouvelles remises, vous n'avez besoin d'ajouter que dans l'objet de remise, et non dans la fonction existante qui calcule la remise.

## Conclusion
Dans cet article, vous avez appris le principe Ouvert-Fermé, ses avantages et comment l'implémenter.

Pour réaliser l'implémentation, nous avons utilisé des classes JavaScript pour illustrer comment vous pouvez le faire avec la programmation orientée objet JavaScript. D'abord, j'ai montré comment le code viole le principe, puis comment le refactoriser pour qu'il ne le viole plus.

Puisque la fonction est également une entité logicielle, nous avons également examiné comment vous pouvez implémenter le principe Ouvert-Fermé avec des fonctions JavaScript.

Continuez à coder !