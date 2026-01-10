---
title: Apprendre la programmation orientée objet en TypeScript
subtitle: ''
author: Lucas
co_authors: []
series: null
date: '2025-05-12T14:12:24.153Z'
originalURL: https://freecodecamp.org/news/learn-object-oriented-programming-in-typescript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747058547629/98922409-4eaf-45e5-8721-10c6a1e6e5e4.png
tags:
- name: TypeScript
  slug: typescript
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: JavaScript
  slug: javascript
seo_title: Apprendre la programmation orientée objet en TypeScript
seo_desc: 'Object-Oriented Programming (OOP) is one of the most widely used programming
  paradigms in software development. But is also one of the most misunderstood.

  This article will help you gain a solid grasp of OOP in TypeScript by walking you
  through the l...'
---

La programmation orientée objet (POO) est l'un des paradigmes de programmation les plus largement utilisés dans le développement logiciel. Mais c'est aussi l'un des plus mal compris.

Cet article vous aidera à acquérir une solide compréhension de la POO en TypeScript en vous guidant à travers les fonctionnalités du langage qui la supportent, puis en montrant comment ces fonctionnalités donnent naturellement naissance aux quatre principes fondamentaux : **l'héritage**, **le polymorphisme**, **l'encapsulation** et **l'abstraction**.

## Prérequis

Pour tirer le meilleur parti de cet article, vous devez être familiarisé avec :

* **Les fondamentaux de JavaScript** – variables, fonctions, objets et tableaux.

* **La syntaxe de base de TypeScript** – y compris les types et comment ils diffèrent de JavaScript.

## **Table des matières**

* [Comment lire cet article](#heading-comment-lire-cet-article)

* [Fonctionnalités du langage TypeScript](#heading-fonctionnalites-du-langage-typescript)

    * [Objets](#heading-objets)

    * [Classes, attributs et méthodes](#heading-classes-attributs-et-methodes)

    * [Interfaces](#heading-interfaces)

    * [Classes abstraites](#heading-classes-abstraites)

* [Principes de la programmation orientée objet](#heading-principes-de-la-programmation-orientee-objet)

    * [Héritage – Superclasse et sous-classe](#heading-heritage-superclasse-et-sous-classe)

    * [Polymorphisme](#heading-polymorphisme)

    * [Encapsulation](#heading-encapsulation)

    * [Abstraction](#heading-abstraction)

* [Conclusion](#heading-conclusion)

### Comment lire cet article

J'ai organisé cet article en deux sections. La première section couvre les fonctionnalités du langage TypeScript qui vous permettent de mettre en œuvre la programmation orientée objet (POO). La deuxième partie discute des concepts dérivés de ces fonctionnalités qui mènent aux quatre principes de la POO : l'héritage, le polymorphisme, l'encapsulation et l'abstraction.

Alors que de nombreux enseignants, livres et cours commencent par expliquer ces principes, je préfère commencer par les fonctionnalités du langage elles-mêmes. La raison est simple : ce sont des structures formelles, en d'autres termes, concrètes. De plus, tout au long de l'article, vous remarquerez que les principes de la POO émergent naturellement lorsque vous utilisez correctement la structure du langage.

## **Fonctionnalités du langage TypeScript**

Dans cette section, nous explorerons les fonctionnalités de TypeScript qui facilitent la mise en œuvre de la POO. Des mécanismes similaires existent dans d'autres langages orientés objet, tels que Java et C#, bien qu'ils puissent varier en syntaxe tout en préservant les concepts de base.

### **Objets**

Un objet est un type de données qui stocke une collection de valeurs organisées en paires clé/valeur. Celles-ci peuvent inclure des données primitives ou d'autres objets.

Dans l'exemple suivant, l'objet `person` stocke diverses informations, telles que la clé `name`, qui contient la valeur `"Lucas"` de type `string`, et la clé `address`, qui contient un autre objet.

```typescript
const person = {
  name: "Lucas", // valeur primitive de type string
  surname: "Garcez",
  age: 28, // valeur primitive de type number
  address: {
    // type objet contenant les clés "city" et "country"
    city: "Melbourne",
    country: "Australia",
  },
};
```

### **Classes, attributs et méthodes**

Une classe sert de modèle pour créer des objets. Elle spécifie la structure et le comportement d'un objet à travers ses attributs et méthodes. Les attributs décrivent la structure des données (clés et types de valeurs), tandis que les méthodes définissent les actions qui peuvent être effectuées sur ces attributs.

```typescript
class Person {
  name: string; // attribut
  surname: string; // attribut
  age: number; // attribut

  // méthode constructeur (méthode spéciale)
  constructor(name: string, surname: string, age: number) {
    this.name = name;
    this.surname = surname;
    this.age = age;
  }

  // méthode pour obtenir le nom complet : "Lucas Garcez"
  getFullName() {
    return `${this.name} ${this.surname}`;
  }
}
```

#### **Méthode constructeur**

Le constructeur est une méthode spéciale au sein d'une classe. Il est automatiquement invoqué lorsqu'un nouvel objet est créé. Les constructeurs sont responsables de l'initialisation des attributs de la classe avec les valeurs fournies lors de la création de l'objet. En TypeScript, le constructeur est défini en utilisant le mot-clé `constructor`, comme vous pouvez le voir dans le code ci-dessus.

#### **Instance**

Une instance fait référence à un objet créé à partir d'une classe. Par exemple, en utilisant la classe `Person` mentionnée ci-dessus, vous pouvez créer un objet nommé `lucas`. Par conséquent, `lucas` est une instance de la classe `Person`. Pour créer une instance d'un objet en JavaScript ou TypeScript, vous utilisez le mot-clé `new`, comme démontré ci-dessous :

```typescript
const lucas = new Person("Lucas", "Garcez", 28);
lucas.name; // "Lucas"
lucas.getFullName(); // "Lucas Garcez"
```

Il est important de noter que vous pouvez créer plusieurs objets (instances) à partir de la même classe. Bien que tous ces objets partagent la même structure (attributs et méthodes), ils sont indépendants et occupent des espaces mémoire séparés dans le programme.

Par exemple, lors de la création d'un nouvel objet :

```typescript
const maria = new Person("Maria", "Oliveira", 19);
```

Vous avez maintenant une nouvelle instance de la classe `Person` qui n'interfère pas avec l'objet `lucas` précédemment créé. Chaque instance maintient ses propres valeurs et comportements, garantissant que la manipulation d'un objet n'affecte pas les autres.

### **Interfaces**

Une interface définit un contrat établissant quels attributs et méthodes une classe doit implémenter. En TypeScript, cette relation est établie en utilisant le mot-clé `implements`. Lorsqu'une classe implémente une interface, elle doit inclure tous les attributs et méthodes spécifiés par cette interface et leurs types respectifs.

Dans l'exemple suivant, vous avez un système bancaire où un client peut avoir soit un compte `CurrentAccount` soit un compte `SavingsAccount`. Les deux options doivent adhérer aux règles générales des comptes de la banque définies par l'interface `BankAccount`.

```typescript
// Contrat définissant les attributs et méthodes d'un compte bancaire
interface BankAccount {
  balance: number;
  deposit(amount: number): void;
  withdraw(amount: number): void;
}

class CurrentAccount implements BankAccount {
  balance: number;
  // La classe peut avoir d'autres attributs et méthodes
  // au-delà de ceux spécifiés dans l'interface
  overdraftLimit: number;

  deposit(amount: number): void {
    this.balance += amount;
  }

  withdraw(amount: number): void {
    if (amount <= this.balance) {
      this.balance -= amount;
    }
  }
}

class SavingsAccount implements BankAccount {
  balance: number;

  deposit(amount: number): void {
    // peut avoir une logique différente de CurrentAccount
    // mais doit respecter la signature de la méthode,
    // c'est-à-dire, les paramètres (amount: number) et le type de retour (void)
  }

  withdraw(amount: number): void {
    // ...
  }
}
```

### **Classes abstraites**

Tout comme les interfaces, les classes abstraites définissent un modèle ou un contrat que d'autres classes doivent suivre. Mais tandis qu'une interface ne décrit que la structure d'une classe sans fournir d'implémentations, une classe abstraite peut inclure des déclarations de méthodes et des implémentations concrètes.

Contrairement aux classes régulières, cependant, les classes abstraites **ne peuvent pas être instanciées directement** – elles existent uniquement comme une base à partir de laquelle d'autres classes peuvent hériter de leurs méthodes et attributs.

En TypeScript, le mot-clé `abstract` est utilisé pour définir une classe abstraite. Dans l'exemple suivant, vous allez refactoriser le système bancaire en remplaçant l'interface par une classe abstraite pour définir le comportement de base de tous les comptes bancaires.

```typescript
// Classe abstraite qui sert de base pour tout type de compte bancaire
abstract class BankAccount {
  balance: number;

  constructor(initialBalance: number) {
    this.balance = initialBalance;
  }

  // Méthode concrète (avec implémentation)
  deposit(amount: number): void {
    this.balance += amount;
  }

  // Méthode abstraite (doit être implémentée par les sous-classes)
  abstract withdraw(amount: number): void;
}

class CurrentAccount extends BankAccount {
  withdraw(amount: number): void {
    const fee = 2; // Les comptes courants ont des frais de retrait fixes
    const totalAmount = amount + fee;

    if (this.balance >= totalAmount) {
      this.balance -= totalAmount;
    } else {
      console.log("Solde insuffisant.");
    }
  }
}

class SavingsAccount extends BankAccount {
  withdraw(amount: number): void {
    if (this.balance >= amount) {
      this.balance -= amount;
    } else {
      console.log("Solde insuffisant.");
    }
  }
}

// ❌ Erreur ! Impossible d'instancier une classe abstraite
const genericAccount = new BankAccount(1000); // Erreur

// ✅ Création d'un compte courant
const currentAccount = new CurrentAccount(2000); // utilise le constructeur BankAccount
currentAccount.deposit(500); // utilise la méthode deposit de BankAccount
currentAccount.withdraw(300); // utilise la méthode withdraw de CurrentAccount

// ✅ Création d'un compte d'épargne
const savingsAccount = new SavingsAccount(1500); // utilise le constructeur BankAccount
savingsAccount.deposit(1100); // utilise la méthode deposit de BankAccount
savingsAccount.withdraw(500); // utilise la méthode withdraw de SavingsAccount
```

## **Principes de la programmation orientée objet**

Maintenant que vous comprenez les mécanismes clés du langage, vous pouvez formaliser les piliers de la programmation orientée objet qui guident la création de systèmes mieux organisés, réutilisables et évolutifs.

### **Héritage – Superclasse et sous-classe**

L'héritage est un mécanisme qui permet à une classe de dériver des caractéristiques d'une autre classe. Lorsque une classe `B` hérite d'une classe `A`, cela signifie que `B` acquiert automatiquement les attributs et méthodes de `A` sans avoir besoin de les redéfinir.

Vous pouvez visualiser cette relation comme une structure parent-enfant, où `A` est la superclasse (classe de base/parent) et `B` est la sous-classe (classe dérivée/enfant). Une sous-classe peut utiliser les ressources héritées, ajouter de nouveaux comportements ou remplacer les méthodes de la superclasse pour répondre à des besoins spécifiques.

Nous avons déjà discuté de l'héritage lors de l'apprentissage des classes abstraites, mais l'héritage peut également être appliqué aux classes concrètes. Cela permet la réutilisation du code et la spécialisation du comportement.

```typescript
// BankAccount est maintenant une classe régulière où vous définissez des attributs et des méthodes
// qui seront réutilisés par la classe enfant CurrentAccount
class BankAccount {
  balance: number = 0;

  constructor(initialBalance: number) {
    this.balance = initialBalance;
  }

  deposit(amount: number): void {
    this.balance += amount;
  }

  withdraw(amount: number): void {
    if (amount <= this.balance) {
      this.balance -= amount;
    }
  }
}

// CurrentAccount est une sous-classe de BankAccount, ce qui signifie
// qu'elle hérite de ses attributs et méthodes.
class CurrentAccount extends BankAccount {
  overdraftLimit: number; // nouvel attribut exclusif à CurrentAccount

  // Lorsque vous spécifiez une méthode constructeur pour une sous-classe,
  // vous devez appeler une autre méthode spéciale, "super".
  // Cette méthode appelle le constructeur de la superclasse (BankAccount) pour s'assurer
  // qu'il est initialisé avant de créer l'objet CurrentAccount lui-même.
  constructor(initialBalance: number, overdraftLimit: number) {
    super(initialBalance); // Doit correspondre à la signature de la méthode constructeur de la superclasse
    this.overdraftLimit = overdraftLimit;
  }

  // Même si la méthode withdraw existe déjà dans la superclasse (BankAccount),
  // elle est remplacée ici. Cela signifie que chaque fois qu'un objet CurrentAccount
  // appelle la méthode withdraw, cette implémentation sera utilisée,
  // ignorant la méthode de la superclasse.
  override withdraw(amount: number): void {
    const totalAvailable = this.balance + this.overdraftLimit;
    if (amount > 0 && amount <= totalAvailable) {
      this.balance -= amount;
    }
  }
}

// Création d'un CurrentAccount avec un solde initial de 0,00 $ 
// et une limite de découvert de 100 $.
const currentAccount = new CurrentAccount(0, 100);

// Effectuer un dépôt de 200 $ en appelant la méthode deposit
// Dans ce cas, la méthode de BankAccount sera invoquée
// puisque deposit n'a pas été remplacée dans CurrentAccount
currentAccount.deposit(200); // solde : 200

// Retirer 250 $ en appelant la méthode withdraw
// Dans ce cas, la méthode de CurrentAccount sera invoquée
// car elle a été remplacée dans sa définition
currentAccount.withdraw(250); // solde : -50
```

### **Polymorphisme**

Le polymorphisme est un concept qui crée souvent de la confusion en programmation orientée objet. Mais en pratique, il s'agit simplement d'une conséquence naturelle de l'utilisation des interfaces et de l'héritage.

Le terme polymorphisme provient du grec et signifie "plusieurs formes" (poly = plusieurs, morphos = formes). Ce concept permet aux objets de différentes classes de répondre au même appel de méthode mais avec des implémentations distinctes, rendant le code plus flexible et réutilisable.

Pour clarifier ce concept, considérons un exemple pratique. Supposons que vous avez une fonction nommée `sendMoney`, responsable du traitement d'une transaction financière, transférant un certain montant du compte A au compte B. La seule exigence est que les deux comptes suivent un contrat commun, garantissant que les méthodes `withdraw` et `deposit` sont disponibles.

```typescript
// BankAccount pourrait être une interface, une classe concrète,
// ou une classe abstraite. Pour la fonction sendMoney, l'implémentation spécifique
// n'a pas d'importance—seulement que BankAccount inclut les méthodes withdraw et deposit.
function sendMoney(
  sender: BankAccount,
  receiver: BankAccount,
  amount: number
) {
  sender.withdraw(amount);
  receiver.deposit(amount);
}

const lucasAccount = new CurrentAccount(500, 200);
const mariaAccount = new SavingsAccount(300);

// transfert de 100 $ de Lucas à Maria
sendMoney(lucasAccount, mariaAccount, 100);
```

#### **Méthodes polymorphiques :**

Les méthodes `withdraw` et `deposit` sont appelées dans la fonction `sendMoney` sans que la fonction ait besoin de savoir si elle traite avec un `CurrentAccount` ou un `SavingsAccount`. Chaque classe implémente `withdraw` selon ses propres règles, démontrant le concept de polymorphisme.

#### **Découplage :**

La fonction `sendMoney` ne dépend pas du type spécifique de compte bancaire. Toute classe qui étend `BankAccount` (si c'est une classe) ou implémente `BankAccount` (si c'est une interface) peut être utilisée sans nécessiter de modifications à la fonction `sendMoney`.

Avec cette approche, vous assurez la flexibilité et la réutilisabilité du code, car de nouveaux types de comptes peuvent être introduits sans affecter la fonctionnalité de `sendMoney`.

### **Encapsulation**

L'encapsulation est l'un des principes fondamentaux de la POO, mais son concept peut être appliqué à tout paradigme de programmation. Il s'agit de masquer les détails d'implémentation interne d'un module, d'une classe, d'une fonction ou de tout autre composant logiciel, en exposant uniquement ce qui est nécessaire pour une utilisation externe. Cela améliore la sécurité, la maintenabilité et la modularité du code en empêchant l'accès non autorisé et en assurant des interactions contrôlées.

#### **Modificateurs d'accès –** `public`, `private` et `protected`

En POO, l'encapsulation est essentielle pour contrôler la visibilité et l'accès aux méthodes et attributs au sein d'une classe. En TypeScript, cela est réalisé en utilisant des modificateurs d'accès, qui sont définis par les mots-clés `public`, `protected` et `private`.

* `public` – Permet à l'attribut ou à la méthode d'être accessible de n'importe où, à la fois à l'intérieur et à l'extérieur de la classe. Il s'agit de la visibilité par défaut, ce qui signifie que si aucun modificateur d'accès n'est spécifié dans le code, TypeScript l'assume comme `public`.

* `protected` – Permet l'accès au sein de la classe et de ses sous-classes mais empêche l'accès externe.

* `private` – Restreint l'accès à l'attribut ou à la méthode uniquement au sein de la classe elle-même.

```typescript
export class Person {
  private firstName: string; // Accessible uniquement au sein de la classe elle-même
  private lastName: string; // Accessible uniquement au sein de la classe elle-même
  protected birthDate: Date; // Accessible par les sous-classes mais pas de l'extérieur

  constructor(firstName: string, lastName: string, birthDate: Date) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.birthDate = birthDate;
  }

  // Méthode publique qui peut être accessible de n'importe où
  public getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
}

// La classe Professor hérite de Person et peut accéder
// aux attributs et méthodes selon leurs modificateurs d'accès.
class Professor extends Person {
  constructor(firstName: string, lastName: string, birthDate: Date) {
    super(firstName, lastName, birthDate); // Appelle le constructeur de la superclasse (Person)
  }

  getProfile() {
    this.birthDate; // ✅ Accessible car il est protégé
    this.getFullName(); // ✅ Accessible car il est public
    this.firstName; // ❌ Erreur ! Ne peut pas être accessible car il est privé dans la classe Person
    this.lastName; // ❌ Erreur ! Ne peut pas être accessible car il est privé dans la classe Person
  }
}

function main() {
  // Création d'une instance de Professor
  const lucas = new Professor("Lucas", "Garcez", new Date("1996-02-06"));

  // Test d'accès direct aux attributs et méthodes
  lucas.birthDate; // ❌ Erreur ! birthDate est protégé et ne peut être accessible qu'au sein de la classe ou des sous-classes
  lucas.getFullName(); // ✅ Accessible car il s'agit d'une méthode publique
  lucas.firstName; // ❌ Erreur ! firstName est privé et ne peut pas être accessible en dehors de la classe Person
  lucas.lastName; // ❌ Erreur ! lastName est également privé et inaccessible en dehors de la classe Person
}
```

#### **Tableau des modificateurs d'accès**

| **Modificateur** | **Accès au sein de la classe** | **Accès dans la sous-classe** | **Accès en dehors de la classe** |
| --- | --- | --- | --- |
| `public` | ✅ Oui | ✅ Oui | ✅ Oui |
| `protected` | ✅ Oui | ✅ Oui | ❌ Non |
| `private` | ✅ Oui | ❌ Non | ❌ Non |

### **Abstraction**

Le concept d'abstraction provoque fréquemment de la confusion car sa signification va au-delà du contexte technique. Si vous cherchez la définition du mot en anglais, le Cambridge Dictionary définit **"abstract"** comme :

> *Quelque chose qui existe en tant qu'idée, sentiment ou qualité, plutôt que comme un objet matériel.*

Cette définition peut être directement appliquée à la POO : L'abstraction représente une idée ou un concept sans entrer dans les détails concrets de l'implémentation.

De nombreuses références en ligne décrivent l'abstraction comme *"*masquer les détails de l'implémentation*,"* ce qui peut être trompeur puisque ce concept est plus étroitement lié à l'encapsulation. En POO, l'abstraction ne signifie PAS masquer les détails mais définir des contrats à travers des **classes** et des **interfaces** abstraites.

```typescript
// Abstraction utilisant une interface
interface BankAccountInterface {
  balance: number;
  deposit(amount: number): void;
  withdraw(amount: number): void;
}

// Abstraction utilisant une classe
abstract class BankAccountClass {
  balance: number;

  constructor(initialBalance: number) {
    this.balance = initialBalance;
  }

  // Méthode concrète (avec implémentation)
  deposit(amount: number): void {
    this.balance += amount;
  }

  // Méthode abstraite (doit être implémentée par les sous-classes)
  abstract withdraw(amount: number): void;
}
```

Dans les exemples ci-dessus, `BankAccountInterface` et `BankAccountClass` sont des exemples d'abstraction car ils définissent des contrats qui doivent être implémentés par ceux qui les utilisent.

## **Conclusion**

Bien que l'apprentissage de la programmation orientée objet ne soit pas facile, j'espère que cet article a aidé à clarifier les fondamentaux et les sujets avancés de la POO.

Si vous souhaitez continuer à apprendre TypeScript et la POO, je vous recommande vivement de lire le livre de Martin Fowler **Refactoring: Improving the Design of Existing Code**. Ce livre contient un vaste catalogue de techniques de refactoring, et la deuxième édition a tous les exemples de code écrits en TypeScript, dont beaucoup utilisent les fonctionnalités et principes de la POO mentionnés ici.