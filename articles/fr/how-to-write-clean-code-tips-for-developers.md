---
title: Comment écrire du code propre – Conseils pour les développeurs avec exemples
date: '2024-11-05T17:11:28.560Z'
author: Programming with Shahan
authorURL: https://www.freecodecamp.org/news/author/codewithshahan/
originalURL: https://freecodecamp.org/news/how-to-write-clean-code-tips-for-developers
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730737606075/5cb4369b-9f2e-4f97-9765-ac00a62800c6.png
tags:
- name: JavaScript
  slug: javascript
- name: clean code
  slug: clean-code
- name: Web Development
  slug: web-development
- name: Programming Blogs
  slug: programming-blogs
- name: Beginner Developers
  slug: beginners
seo_desc: 'Imagine a messy room with clothes, books, and other items scattered everywhere.
  Finding something in that room would be tough, right?

  Now, think about writing messy code – it’s just as confusing, if not more!

  On the other hand, clean code is like an ...'
---


Imaginez une pièce en désordre avec des vêtements, des livres et d'autres objets éparpillés partout. Trouver quelque chose dans cette pièce serait difficile, n'est-ce pas ?

<!-- more -->

Maintenant, pensez à l'écriture d'un code désordonné – c'est tout aussi déroutant, sinon plus !

D'un autre côté, un code propre est comme une pièce organisée : vous pouvez facilement trouver ce dont vous avez besoin, comprendre ce qui se passe et accomplir les tâches plus rapidement.

Jetons un coup d'œil à ce graphique. Il montre deux manières différentes d'écrire du code et comment elles affectent le temps nécessaire pour ajouter de nouvelles lignes :

![3fa8f5a1-0af4-4ffd-aa3a-bb70001b026d](https://cdn.hashnode.com/res/hashnode/image/upload/v1730728342241/3fa8f5a1-0af4-4ffd-aa3a-bb70001b026d.png)

1.  ⚠️ **Code rapide et bâclé** (Ligne rouge) : C'est lorsque vous écrivez du code rapidement sans planification ni organisation. Au début, cela peut sembler plus rapide, mais à mesure que les lignes s'ajoutent, il devient plus difficile à comprendre et à corriger. Ainsi, avec le temps, l'ajout de chaque nouvelle ligne prend de plus en plus de temps.
    
2.  **⚡ Code réfléchi et propre** (Ligne bleue) : C'est lorsque vous écrivez du code avec soin, en le rendant facile à comprendre et à modifier. Au début, cela peut prendre un peu plus de temps, mais avec le temps, il reste facile à manipuler. De cette façon, l'ajout de nouvelles lignes ne devient pas plus difficile.
    

En termes simples, écrire du code propre peut sembler plus lent au début, mais sur le long terme, cela permet de gagner beaucoup de temps et facilite le travail. Cela conduit également à des logiciels plus fiables et à de meilleurs produits.

Écrire du code propre est une habitude que les développeurs professionnels cultivent, montrant un dévouement à la qualité et une forte éthique de travail. Dans cet article, je vais vous présenter quelques bonnes pratiques pour garder votre code propre.

### Ce que nous allons couvrir :

1.  [Utilisez des noms significatifs][1]
    
2.  [Suivez le principe de responsabilité unique (SRP)][2]
    
3.  [Évitez les commentaires inutiles][3]
    
4.  [Rendez votre code lisible][4]
    
5.  [Écrivez des tests unitaires][5]
    
6.  [Faites attention aux dépendances][6]
    
7.  [Organisez votre projet][7]
    
8.  [Utilisez un formatage cohérent][8]
    
9.  [Évitez les valeurs codées en dur][9]
    
10.  [Limitez la longueur des fonctions][10]
    
11.  [Conclusion][11]
    

## 10 conseils essentiels pour écrire du code propre

Pour vous aider à démarrer votre parcours vers un code propre, voici 10 conseils pratiques pour garder votre code lisible, organisé et efficace.

### 1\. Utilisez des noms significatifs

Lors du nommage des variables, des fonctions et des classes, choisissez des noms qui décrivent clairement leur utilité.

Au lieu d'appeler une variable `b`, essayez `numberOfUsers`. De cette façon, toute personne lisant votre code peut facilement comprendre son but sans avoir besoin de commentaires supplémentaires. Un nom significatif élimine les suppositions et évite la confusion.

**Exemple** :

```
// Good
let numberOfUsers = 5; // Clear and easy to understand

// Bad
let b = 5; // Vague and unclear
```

**💡 Conseils de nommage**

-   **Variables** : Utilisez des noms qui décrivent les données, comme `userAge` ou `totalAmount`.
    
-   **Fonctions** : Utilisez des verbes d'action, comme `calculateTotal()` ou `fetchUserData()`.
    
-   **Classes** : Utilisez des noms au singulier, comme `User` ou `Order`, pour représenter ce qu'elles sont.
    

```
// Variable: Describes the data it holds
let userAge = 25;

// Function: Uses an action word to describe what it does
function calculateTotal(price, quantity) {
    return price * quantity;
}

// Class: Singular noun representing a type of object
class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}
```

### 2\. Suivez le principe de responsabilité unique (SRP)

Le **principe de responsabilité unique** signifie que chaque fonction ou méthode doit avoir **une tâche spécifique.**

Cela permet de garder vos fonctions courtes et ciblées, ce qui les rend plus faciles à lire, à tester et à maintenir.

Imaginez une boîte à outils où chaque outil a un but unique — les fonctions d'un code propre devraient fonctionner de la même manière.

![77666f78-7ec9-4a5c-af4f-253e6de4acac](https://cdn.hashnode.com/res/hashnode/image/upload/v1730728643183/77666f78-7ec9-4a5c-af4f-253e6de4acac.jpeg)

Par exemple, si vous avez une fonction appelée `calculateTotal`, elle ne devrait s'occuper que du calcul du total. Si vous ajoutez des tâches supplémentaires, cela peut mener à un code confus et difficile à maintenir.

Voici un exemple pour montrer pourquoi il est important de garder les fonctions ciblées :

Disons que vous voulez calculer un total et retourner un objet avec des informations supplémentaires, comme qui l'a calculé et quand. Au lieu d'ajouter cela directement dans `calculateTotal`, nous pouvons utiliser une deuxième fonction.

1.  **Bon exemple (Tâches séparées)**
    
    ```
     // This function only calculates the total
     function calculateTotal(a, b) {
         return a + b;
     }
    
     // This function creates an object with extra details
     function createCalculationRecord(a, b, user) {
         let sum = calculateTotal(a, b); // Calls the calculate function
         return {
             user: user,
             total: sum,
             timestamp: new Date()
         };
     }
    
     let record = createCalculationRecord(5, 10, "Shahan");
     console.log(record);
    ```
    
    **👍 Pourquoi c'est bien** : Chaque fonction a une tâche claire et ciblée. `calculateTotal` ne fait que le calcul mathématique, tandis que `createCalculationRecord` ajoute les détails supplémentaires. Si vous voulez changer la façon dont le total est calculé, vous ne mettez à jour que `calculateTotal`, et si vous voulez changer le format de l'enregistrement, vous ne mettez à jour que `createCalculationRecord`.
    
2.  **Mauvais exemple (Tâches mixtes dans une seule fonction)**
    
    ```
     // This function calculates the total and creates an object in one step
     function calculateTotalAndReturnRecord(a, b, user) {
         let sum = a + b;
         return {
             user: user,
             total: sum,
             timestamp: new Date()
         };
     }
    
     let record = calculateTotalAndReturnRecord(5, 10, "Shahan");
     console.log(record);
    ```
    
    **👎 Pourquoi c'est mauvais** : Le nom de la fonction `calculateTotalAndReturnRecord` montre qu'elle essaie de faire plusieurs choses. Si vous voulez utiliser uniquement le calcul, vous ne pouvez pas réutiliser cette fonction sans la partie enregistrement. C'est aussi plus difficile de mettre à jour et de tester chaque tâche séparément.
    

### 3\. Évitez les commentaires inutiles

Un bon code devrait être explicite sans avoir besoin de commentaires excessifs. Concentrez-vous sur l'écriture d'un code clair et compréhensible par lui-même.

Les commentaires sont utiles pour expliquer une logique complexe ou une approche unique, mais trop de commentaires peuvent encombrer votre code et le rendre difficile à suivre.

**💬 Quand utiliser des commentaires** :

-   Pour clarifier pourquoi quelque chose est fait d'une manière particulière.
    
-   Lors de l'utilisation d'algorithmes ou de calculs complexes.
    
-   Pour ajouter des notes sur des limitations potentielles.
    

**Exemple** :

```
// Clear name, no comment needed
let userAge = 25;

// Unclear name, comment needed
let a; // age of the user
```

### 4\. Rendez votre code lisible

Un code lisible utilise l'**indentation**, les **sauts de ligne** et les **espaces** pour garder l'ensemble propre et organisé.

Pensez-y comme à l'écriture d'une histoire : les paragraphes facilitent la lecture en décomposant de gros blocs de texte. En programmation, les sauts de ligne servent le même but.

**Exemple** :

```
// Good Code
if (isLoggedIn) {
    console.log("Welcome!");
} else {
    console.log("Please log in.");
}

// Bad Code
if(isLoggedIn){console.log("Welcome!");}else{console.log("Please log in.");}
```

Dans VS Code, **Prettier** et **Black** sont des formateurs populaires qui appliquent automatiquement un style de code propre pour plusieurs langages.

**PyCharm** et **IntelliJ** disposent de formateurs intégrés puissants avec des règles personnalisables, prenant en charge PEP 8 pour Python et d'autres guides standards. Ces outils garantissent un code cohérent et lisible sur tous les projets avec un effort manuel minimal.

### 5\. Écrivez des tests unitaires

Les tests unitaires aident à s'assurer que chaque partie de votre code fonctionne comme prévu.

En testant de petites parties individuelles (comme des fonctions), vous pouvez détecter les bogues tôt et les empêcher de se propager à d'autres parties du code.

Concrètement, les tests unitaires sont de mini contrôles de qualité pour chaque partie de votre code afin de garantir qu'elles fonctionnent comme prévu.

**🍎 Exemple concret :**

Voyons comment tester un objet JavaScript complexe avec plusieurs méthodes, en utilisant une classe `Calculator` comme exemple.

Cette approche vous aidera à comprendre pourquoi il est important de garder chaque méthode focalisée sur une seule tâche et de s'assurer que chacune fonctionne correctement via des tests unitaires.

Voici la classe `Calculator` qui inclut des méthodes pour les opérations arithmétiques de base : addition, soustraction, multiplication et division.

```
class Calculator {
    constructor() {
        this.result = 0;
    }

    add(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }

    multiply(a, b) {
        return a * b;
    }

    divide(a, b) {
        if (b === 0) throw new Error("Cannot divide by zero");
        return a / b;
    }
}
```

Comme vous pouvez le voir, chaque méthode effectue une opération spécifique. La méthode `divide` possède une logique supplémentaire pour gérer la division par zéro, qui causerait sinon une erreur.

Maintenant, nous allons écrire des tests unitaires pour confirmer que chaque méthode se comporte comme prévu. 🔬

**🧪 Écrire des tests unitaires pour chaque méthode**

Pour tester notre classe `Calculator`, nous pouvons écrire des tests unitaires qui couvrent les cas normaux ainsi que les cas limites. Voici comment nous configurerions les tests pour chaque méthode :

```
// Initialize the Calculator instance
const calculator = new Calculator();

// Test add method
console.assert(calculator.add(2, 3) === 5, 'Test failed: 2 + 3 should be 5');
console.assert(calculator.add(-1, 1) === 0, 'Test failed: -1 + 1 should be 0');

// Test subtract method
console.assert(calculator.subtract(5, 3) === 2, 'Test failed: 5 - 3 should be 2');
console.assert(calculator.subtract(0, 0) === 0, 'Test failed: 0 - 0 should be 0');

// Test multiply method
console.assert(calculator.multiply(2, 3) === 6, 'Test failed: 2 * 3 should be 6');
console.assert(calculator.multiply(-1, 2) === -2, 'Test failed: -1 * 2 should be -2');

// Test divide method
console.assert(calculator.divide(6, 3) === 2, 'Test failed: 6 / 3 should be 2');
try {
    calculator.divide(1, 0);
    console.assert(false, 'Test failed: Division by zero should throw an error');
} catch (e) {
    console.assert(e.message === "Cannot divide by zero", 'Test failed: Incorrect error message for division by zero');
}
```

**🫧 Explication des tests :**

1.  **Addition** (méthode `add`) : Nous testons que `add(2, 3)` retourne `5`, et `add(-1, 1)` retourne `0`. Si ces tests passent, nous savons que la logique d'addition fonctionne correctement.
    
2.  **Soustraction** (méthode `subtract`) : Nous vérifions que `subtract(5, 3)` retourne `2`, et `subtract(0, 0)` retourne `0`. Ces vérifications confirment que la soustraction est exacte.
    
3.  **Multiplication** (méthode `multiply`) : Nous testons la fonction de multiplication avec des valeurs positives et négatives, en nous assurant que `multiply(2, 3)` retourne `6`, et `multiply(-1, 2)` retourne `-2`.
    
4.  **Division** (méthode `divide`) : Nous vérifions que diviser `6` par `3` retourne `2`. Pour la division par zéro, nous utilisons un bloc `try...catch` pour confirmer qu'une erreur est levée avec le bon message. Ce test garantit que la méthode gère correctement les erreurs.
    

Vous pouvez voir que si une méthode échoue, le test produira un message d'erreur clair, nous permettant d'identifier et de corriger rapidement le problème. Tester les méthodes individuellement nous aide à détecter les bogues tôt et à maintenir un code propre et fiable au fur et à mesure que le projet grandit.

### 6\. Faites attention aux dépendances

Les dépendances sont des morceaux de logiciel sur lesquels votre code repose. 🔌

Imaginez que vous construisez une application web qui envoie des e-mails. Au lieu d'écrire vous-même le code d'envoi d'e-mails, vous utilisez une bibliothèque externe comme [**Nodemailer**][12]. Ici, Nodemailer est une **dépendance** — votre application compte sur elle pour gérer la fonctionnalité d'envoi d'e-mails.

**Exemple :**

```
const nodemailer = require('nodemailer');

function sendEmail(to, subject, message) {
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'your-email@gmail.com',
            pass: 'your-email-password'
        }
    });

    const mailOptions = {
        from: 'your-email@gmail.com',
        to: to,
        subject: subject,
        text: message
    };

    return transporter.sendMail(mailOptions);
}
```

Dans ce code, `nodemailer` est importé et utilisé pour créer un transporteur pour l'envoi d'e-mails. Sans cela, vous devriez construire toute la fonctionnalité d'e-mail à partir de zéro, ce qui serait complexe et chronophage. En utilisant Nodemailer comme dépendance, votre application peut envoyer des e-mails facilement.

Même si les dépendances sont utiles, vous devriez essayer d'éviter une dépendance excessive envers des logiciels ou bibliothèques externes. Utilisez des dépendances uniquement lorsqu'elles simplifient votre travail ou ajoutent une fonctionnalité importante.

Gérer les dépendances efficacement est essentiel pour écrire du code propre. Voici quelques conseils :

-   **Limitez les dépendances** : N'incluez que les bibliothèques ou modules essentiels à votre projet.
    
-   **Gardez les versions à jour** : Utilisez des versions à jour des bibliothèques pour éviter les risques de sécurité.
    
-   **Séparez la logique** : Écrivez vous-même les fonctions de base chaque fois que possible. De cette façon, si vous devez un jour supprimer une dépendance, cela ne cassera pas votre code.
    

Laissez-moi vous donner un exemple avec notre précédent code Nodemailer pour implémenter le concept de séparation de la logique.

Vous pouvez créer une fonction d'enveloppement (wrapper) qui fait abstraction des détails de l'envoi d'e-mails. De cette façon, vous pouvez changer le service d'e-mail sous-jacent ou supprimer la dépendance à Nodemailer sans affecter le reste de votre code.

Voici comment vous pouvez structurer votre code pour y parvenir :

```
const nodemailer = require('nodemailer');

// Core function to send email
function sendEmail(to, subject, message) {
    const transporter = createTransporter();
    const mailOptions = createMailOptions(to, subject, message);
    return transporter.sendMail(mailOptions);
}

// Function to create the transporter
function createTransporter() {
    return nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'your-email@gmail.com',
            pass: 'your-email-password'
        }
    });
}

// Function to create mail options
function createMailOptions(to, subject, message) {
    return {
        from: 'your-email@gmail.com',
        to: to,
        subject: subject,
        text: message
    };
}

// Example usage
sendEmail('recipient@example.com', 'Test Subject', 'Hello, this is a test email.')
    .then(() => {
        console.log('Email sent successfully!');
    })
    .catch((error) => {
        console.error('Error sending email:', error);
    });
```

**🗝️ Points clés :**

1.  **Fonctions de base** : Les fonctions `sendEmail`, `createTransporter` et `createMailOptions` sont séparées, vous permettant d'en modifier une sans affecter les autres.
    
2.  **Modifications faciles** : Si vous voulez passer à un autre service d'e-mail à l'avenir, vous pouvez simplement modifier la fonction `createTransporter`.
    
3.  **Maintenabilité** : Cette structure rend votre code plus maintenable et plus facile à comprendre.
    

### 7\. Organisez votre projet

Une structure de projet bien organisée est aussi importante que le code lui-même.

Pensez-y comme à l'organisation de votre espace de travail — vous avez besoin d'endroits désignés pour chaque chose afin de pouvoir les trouver facilement. Pour les projets de programmation, créez des dossiers pour des parties spécifiques, comme `components`, `utils` et `services`.

**📂 Comment organiser votre projet**

Pour mettre en place un projet propre et organisé, vous devriez catégoriser les différentes parties de votre code dans des dossiers désignés. Voici un exemple simple de ce à quoi pourrait ressembler une structure de projet bien organisée :

```
myProject
├── src
│   ├── components
│   ├── services
│   ├── utils
└── tests
```

#### Détail de la structure du projet :

1.  **myProject** : C'est le dossier racine de votre projet. Il contient tout ce qui concerne votre application.
    
2.  **src (Source)** : Ce dossier contient tout le code source de votre projet. C'est là que vous passerez la majeure partie de votre temps à coder.
    
3.  **components** : Ce sous-dossier contient les composants UI réutilisables. Par exemple, si vous construisez une application web, vous pourriez avoir des fichiers individuels pour les boutons, les en-têtes ou les formulaires ici. Chaque composant peut être dans son propre fichier pour garder les choses modulaires.
    
    -   Exemple de structure dans `components` :

```
    components
    ├── Button.js
    ├── Header.js
    └── Form.js
```

4.  **services** : Ce dossier comprend des fonctions qui effectuent des tâches spécifiques ou gèrent la logique métier. Par exemple, si vous envoyez des e-mails, vous pourriez avoir un fichier ici avec toutes les fonctions liées aux e-mails.
    
    -   Exemple de structure dans `services` :

```
    services
    ├── emailService.js
    ├── userService.js
    └── productService.js
```

5.  **utils (Utilities)** : Ici, vous placez les fonctions utilitaires qui peuvent être utilisées à travers tout votre projet. Celles-ci peuvent inclure des fonctions pour formater des dates, valider des entrées ou toute autre tâche commune qui n'appartient pas à des composants ou services spécifiques.
    
    -   Exemple de structure dans `utils` :

```
    utils
    ├── formatDate.js
    ├── validateEmail.js
    └── generateId.js
```

6.  **tests** : Ce dossier est dédié à vos fichiers de test. Garder vos tests organisés permet de s'assurer que, au fur et à mesure que vous construisez de nouvelles fonctionnalités, vous pouvez facilement les tester sans fouiller dans votre base de code.
    
    -   Exemple de structure dans `tests` :

```
    tests
    ├── emailService.test.js
    ├── userService.test.js
    └── component.test.js
```

**📨 Exemple concret : Travailler avec Nodemailer**

Disons que vous construisez une application qui envoie des e-mails aux utilisateurs. Vous pourriez structurer votre projet comme ceci :

```
myEmailApp
├── src
│   ├── components
│   │   ├── EmailForm.js
│   │   └── SuccessMessage.js
│   ├── services
│   │   └── emailService.js
│   ├── utils
│   │   └── validateEmail.js
└── tests
    ├── emailService.test.js
    └── EmailForm.test.js
```

-   **EmailForm.js** : Ce composant gère l'interface utilisateur pour l'envoi d'un e-mail, comme les champs de saisie pour le destinataire, le sujet et le message.
    
-   **SuccessMessage.js** : Ce composant affiche un message de succès une fois que l'e-mail a été envoyé.
    
-   **emailService.js** : Ce service contient la logique pour l'envoi d'e-mails via Nodemailer, gardant votre code modulaire et propre.
    
-   **validateEmail.js** : Une fonction utilitaire qui vérifie si une adresse e-mail est correctement formatée.
    
-   **tests** : Ici, vous écririez des tests pour vous assurer que votre service d'e-mail et vos composants fonctionnent comme prévu.
    

**🍱 Avantages d'un projet bien organisé**

1.  **Facilité de navigation** : Toute personne consultant votre projet peut rapidement comprendre où trouver des parties spécifiques du code.
    
2.  **Meilleure collaboration** : Si vous travaillez avec d'autres personnes, une structure claire aide tout le monde à savoir où contribuer sans se gêner mutuellement.
    
3.  **Évolutivité** : À mesure que votre projet grandit, maintenir une structure claire aide à gérer la complexité et garde votre base de code propre.
    
4.  **Maintenance améliorée** : Lorsque vous devez mettre à jour ou corriger quelque chose, vous pouvez trouver les fichiers pertinents rapidement, ce qui fait gagner du temps et réduit les erreurs.
    

### **8\. Utilisez un formatage cohérent**

La cohérence dans le formatage améliore la lisibilité.

Établissez un modèle pour la façon dont vous écrivez votre code, comme l'utilisation de deux espaces pour l'indentation ou l'inclusion systématique d'un saut de ligne avant les commentaires.

Suivre un formatage cohérent rend votre code propre et bien organisé.

**🛠️ Outils de formatage**

-   [**Prettier**][13] : Formate automatiquement le code selon un ensemble de règles. [Voici un tutoriel][14] qui explique comment configurer et utiliser Prettier dans VSCode.
    
-   [**ESLint**][15] : Aide à faire respecter les standards de codage en soulignant les problèmes. [Voici un tutoriel][16] qui inclut une section utile et approfondie sur la configuration d'ESLint pour vos projets.
    

### 9\. Évitez les valeurs codées en dur

Le codage en dur (hardcoding) consiste à intégrer directement des valeurs de données dans le code, comme définir un ID utilisateur à `123` au lieu d'utiliser une variable.

Éviter les valeurs codées en dur vous permet de réutiliser le code sans faire de changements constants. Stockez plutôt les valeurs dans des variables, des constantes ou des fichiers de configuration.

Voici un scénario où le codage en dur peut poser problème :

```
// Bad: Hardcoding user limit
function createUser(name) {
    let numberOfUsers = 100; // Hardcoded value
    if (numberOfUsers >= 100) {
        return 'User limit reached.';
    }
    // Code to create the user
    return 'User created.';
}
```

Dans cet exemple, `numberOfUsers` est codé en dur à `100`. Si vous voulez changer la limite d'utilisateurs, vous devez trouver et modifier cette valeur dans le code. Si elle apparaît à plusieurs endroits, cette tâche devient fastidieuse et sujette aux erreurs.

#### **🏗️ Exemple amélioré utilisant des constantes**

Maintenant, refactorisons ce code pour utiliser une constante à la place :

```
// Good: Using a constant
const MAX_USERS = 100; // Store the limit in a constant

function createUser(name) {
    let numberOfUsers = getCurrentUserCount(); // Get the current count from a function or database
    if (numberOfUsers >= MAX_USERS) {
        return 'User limit reached.';
    }
    // Code to create the user
    return 'User created.';
}

// Example function to get current user count
function getCurrentUserCount() {
    // Simulate fetching the current count, e.g., from a database
    return 90; // Example count
}
```

**🥣 Détail de l'exemple amélioré :**

1.  **Utilisation de constantes** : La constante `MAX_USERS` est définie en haut. De cette façon, si vous devez un jour changer le nombre maximum d'utilisateurs, vous n'avez qu'à le mettre à jour à un seul endroit.
    
2.  **Valeurs dynamiques** : La fonction `getCurrentUserCount()` récupère dynamiquement le nombre actuel d'utilisateurs à partir d'une base de données ou de toute autre source. Cette approche évite de coder le nombre en dur et permet des changements faciles.
    
3.  **Maintenabilité** : En stockant les valeurs dans des constantes, votre code devient plus maintenable. Si l'exigence métier change et que vous devez augmenter la limite d'utilisateurs à `150`, vous pouvez simplement changer `MAX_USERS` de `100` à `150`, et le changement se reflétera dans toute votre application.
    
4.  **Clarté** : L'utilisation de noms descriptifs pour vos constantes (comme `MAX_USERS`) améliore la lisibilité de votre code. Toute personne consultant votre code peut rapidement comprendre ce que cette valeur représente.
    

**🤐 Quand utiliser des fichiers de configuration**

Dans les applications plus importantes, vous pourriez également envisager d'utiliser des fichiers de configuration (comme JSON, YAML ou des variables d'environnement) pour stocker des valeurs qui peuvent changer entre les environnements (développement, staging, production).

Par exemple, dans votre fichier **config.json**, vous pouvez définir `maxUsers` comme suit (n'oubliez pas que dans config.json, il est recommandé d'utiliser le camelCase pour suivre un formatage cohérent) :

```
{
    "maxUsers": 100,
    "emailService": {
        "service": "gmail",
        "user": "your-email@gmail.com",
        "pass": "your-email-password"
    }
}
```

**🪴 Utilisation de la configuration dans votre code :**

```
const config = require('./config.json');

function createUser(name) {
    let numberOfUsers = getCurrentUserCount(); 
    if (numberOfUsers >= config.maxUsers) {
        return 'User limit reached.';
    }
    // Code to create the user
    return 'User created.';
}
```

### 10\. Limitez la longueur des fonctions

Les fonctions longues sont plus difficiles à comprendre et à maintenir.

Il n'y a pas de règle stricte, mais en général, les fonctions devraient idéalement ne pas dépasser 20 à 30 lignes. Si une fonction a plusieurs responsabilités ou contient de nombreuses étapes, c'est une bonne indication qu'elle est peut-être trop longue. Décomposer ces fonctions en plus petites fonctions "utilitaires" (helper functions) peut les rendre plus gérables et compréhensibles.

Voici à quoi pourrait ressembler une fonction longue et complexe :

```
function updateCart(cart, item, discountCode) {
    // Add the item to the cart
    cart.items.push(item);

    // Calculate the new total
    let total = 0;
    cart.items.forEach(cartItem => {
        total += cartItem.price * cartItem.quantity;
    });

    // Apply discount if available
    if (discountCode) {
        total = applyDiscount(total, discountCode);
    }

    // Log the transaction
    console.log(`Item added: ${item.name}, New total: $${total}`);

    return total;
}
```

⚠️ **Cette fonction fait plusieurs choses :**

1.  Ajoute un article au panier.
    
2.  Calcule le prix total.
    
3.  Applique une remise s'il y a un code.
    
4.  Enregistre la transaction.
    

Bien que cette fonction puisse sembler gérable pour l'instant, elle peut rapidement grossir si d'autres tâches sont ajoutées, ce qui la rend plus difficile à déboguer et à maintenir.

Décomposons cette longue fonction en plus petites fonctions à but unique :

```
function updateCart(cart, item, discountCode) {
    addItemToCart(cart, item);
    let total = calculateTotal(cart);

    if (discountCode) {
        total = applyDiscount(total, discountCode);
    }

    logTransaction(item, total);
    return total;
}

function addItemToCart(cart, item) {
    cart.items.push(item);
}

function calculateTotal(cart) {
    return cart.items.reduce((total, cartItem) => total + cartItem.price * cartItem.quantity, 0);
}

function logTransaction(item, total) {
    console.log(`Item added: ${item.name}, New total: $${total}`);
}
```

#### 🧩 Laissez-moi vous expliquer :

1.  `addItemToCart` : Cette fonction est maintenant responsable uniquement de l'ajout d'un article au panier. Elle est simple, avec un but clair.
    
2.  `calculateTotal` : Cette fonction calcule le prix total de tous les articles du panier. Elle est plus facile à lire et à comprendre, et si vous devez mettre à jour la façon dont les totaux sont calculés, vous n'avez qu'à modifier cette fonction.
    
3.  `logTransaction` : Gère la responsabilité de l'enregistrement des détails. Si vous devez un jour changer ce qui est enregistré (par exemple, ajouter un horodatage), vous pouvez le faire dans cette fonction sans toucher au reste du code.
    
4.  `updateCart` : La fonction principale se lit maintenant davantage comme un résumé des actions entreprises : ajouter un article, calculer le total, appliquer les remises et enregistrer le résultat. Elle est plus facile à suivre et à comprendre d'un coup d'œil.
    

**📒 Résumons la limitation de la longueur des fonctions :**

1.  **🎯 Concentrez-vous sur une seule tâche** : Chaque fonction devrait idéalement n'effectuer qu'une seule tâche. Si une fonction semble effectuer plusieurs tâches, envisagez de la diviser.
    
2.  **🩼 Utilisez des fonctions utilitaires** : Les fonctions utilitaires sont de petites fonctions ciblées qui aident une fonction principale en effectuant une tâche spécifique. Dans l'exemple ci-dessus, `addItemToCart`, `calculateTotal` et `logTransaction` sont des fonctions utilitaires.
    
3.  **🪦 Noms descriptifs** : Nommez vos fonctions en fonction de leurs tâches (par exemple, `addItemToCart`), ce qui aide à rendre le code explicite.
    

## Bonnes pratiques pour un code propre

Maintenant que nous avons couvert quelques conseils importants, examinons certains principes fondamentaux qui constituent la philosophie du code propre :

1.  **🎏 Simplicité** : Essayez toujours de rendre votre code aussi simple que possible.
    
2.  **🧂 Cohérence** : Gardez votre code uniforme en termes de style et de structure.
    
3.  **🌾 Clarté** : Votre code doit communiquer clairement ce qu'il fait.
    
4.  **⛽ Efficacité** : Écrivez un code optimisé pour la performance sans sacrifier la lisibilité.
    

Ces principes font du codage moins une question d'écriture et plus une question de conception de solutions. Écrire du code propre est une compétence qui se développe avec la pratique, alors continuez à apprendre et à vous améliorer au fil du temps.

**🔌 Une note sur les dépendances**

Au lieu de coder les dépendances directement en dur dans votre code, utilisez des gestionnaires de paquets comme [**npm**][17] (pour JavaScript) ou **pip** (pour Python) pour les gérer. De cette façon, vous pouvez facilement les mettre à jour ou les supprimer au besoin.

## Conclusion 🏁

Écrire du code propre, c'est comme construire les fondations solides d'une maison. Cela permet de garder tout en ordre, facilitant l'ajout de nouvelles fonctionnalités ou la correction de problèmes à mesure que votre projet grandit.

Grâce à ces conseils, vous pouvez commencer à développer des habitudes qui rendront votre code plus lisible, maintenable et agréable à travailler.

### Prochaines étapes recommandées 📘

Pour un guide structuré afin de devenir développeur backend en six mois, vous pouvez consulter ma [feuille de route du développeur backend][18]. Elle est conçue pour aider les débutants à rester sur la bonne voie avec des objectifs hebdomadaires, couvrant les compétences, outils et technologies essentiels. Cette feuille de route peut vous garder motivé et rendre l'apprentissage plus gérable.

**Vous pouvez me suivre sur** [**𝕏**][19] **pour des mises à jour instantanées.**

Au plaisir de vous revoir la prochaine fois !

[1]: #heading-1-utilisez-des-noms-significatifs
[2]: #heading-2-suivez-le-principe-de-responsabilite-unique-srp
[3]: #heading-3-evitez-les-commentaires-inutiles
[4]: #heading-4-rendez-votre-code-lisible
[5]: #heading-5-ecrivez-des-tests-unitaires
[6]: #heading-6-faites-attention-aux-dependances
[7]: #heading-7-organisez-votre-projet
[8]: #heading-8-utilisez-un-formatage-coherent
[9]: #heading-9-evitez-les-valeurs-codees-en-dur
[10]: #heading-10-limitez-la-longueur-des-fonctions
[11]: #heading-conclusion
[12]: https://nodemailer.com/
[13]: https://prettier.io/
[14]: https://www.freecodecamp.org/news/how-to-use-prettier-in-visual-studio-code/
[15]: https://eslint.org/
[16]: https://www.freecodecamp.org/news/how-to-set-up-eslint-prettier-stylelint-and-lint-staged-in-nextjs/#heading-set-up-eslint
[17]: https://www.npmjs.com/
[18]: https://codewithshahan.gumroad.com/l/pcela
[19]: https://x.com/shahancd