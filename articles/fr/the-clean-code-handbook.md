---
title: 'Le manuel du Clean Code : Comment écrire un meilleur code pour le développement
  logiciel Agile'
date: '2025-01-29T17:04:40.260Z'
author: Programming with Shahan
authorURL: https://www.freecodecamp.org/news/author/codewithshahan/
originalURL: https://freecodecamp.org/news/the-clean-code-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738170236859/edacf21e-7180-4f65-9e7e-f7cf95b4f9d8.png
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: agile
  slug: agile
- name: handbook
  slug: handbook
seo_desc: 'Building scalable software applications requires writing clean code that’s
  so simple that any dev can understand it.

  In this article, I’ll explain and demonstrate what clean code is. Then I’ll share
  my favorite clean code patterns for building modern...'
---


Construire des applications logicielles évolutives nécessite d'écrire un code propre (clean code) si simple que n'importe quel développeur peut le comprendre.

<!-- more -->

Dans cet article, j'expliquerai et démontrerai ce qu'est le clean code. Ensuite, je partagerai mes patterns de clean code préférés pour construire des applications Agile modernes.

Je n'utiliserai pas de jargon complexe. Je vous présenterai des exemples JavaScript simples et clairs qui se concentrent sur les concepts de base. Droit au but, sans fioritures – c'est ma façon de faire.

C'est parti.

## Table des matières

1.  [Le coût du mauvais code][1]
    
2.  [Développeur propre vs Développeur désordonné][2]
    
3.  [L'IA ne peut pas vous sauver si votre code est un désordre 🗑️][3]
    
4.  [12 patterns de conception Clean Code pour construire des applications Agile ⚖️][4]
    
    -   [🌿 Utilisez des noms qui ont du sens][5]
        
    -   [🔨 Gardez les fonctions focalisées (SRP)][6]
        
    -   [🚪 Utilisez les commentaires avec discernement][7]
        
    -   [⚡ Meilleures pratiques pour écrire de bons commentaires][8]
        
    -   [🧩 Rendez votre code lisible][9]
        
    -   [🏌️ Testez tout ce que vous écrivez][10]
        
    -   [💉 Utilisez l'injection de dépendances][11]
        
    -   [📂 Des structures de projet propres][12]
        
    -   [🤹‍♂️ Soyez cohérent avec le formatage][13]
        
    -   [✋ Arrêtez de coder des valeurs en dur][14]
        
    -   [🤏 Gardez les fonctions courtes][15]
        
    -   [⛺ Suivez la règle du Boy Scout][16]
        
    -   [🏟️ Suivez le principe Ouvert/Fermé][17]
        
5.  [Résumé des meilleures pratiques modernes pour vous aider à écrire du Clean Code 🥷][18]
    
6.  [Outils automatisés pour maintenir un code propre ⚓][19]
    
    -   [1️⃣ Analyse statique][20]
        
    -   [2️⃣ Formatage de code automatisé][21]
        
    -   [3️⃣ Tests d'intégration continue (CI)][22]
        
    -   [4️⃣ Pipelines CI/CD][23]
        
7.  [Le rôle de la documentation dans le développement logiciel Agile 🚣][24]
    
8.  [Conclusion 🏁][25]
    
9.  [Questions fréquemment posées sur le Clean Code 🧯][26]
    

![Image of agile software development meme](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xh3j6ccn1hc3euc3lfyl.png)

Dans l'Agile, où le changement est la seule constante, le clean code est votre armure. Il vous rend adaptable, rapide et, plus important encore, maître de la situation.

Voici la vérité : écrire du clean code n'est pas optionnel si vous voulez survivre dans l'industrie du développement logiciel. Heureusement, nous, les êtres humains, sommes capables de maîtriser le clean code avec un peu d'effort et de pratique.

## Le coût du mauvais code

![Image of cost of messy code vs clean code graph by shahan](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wdai6npb55j71sguj6kl.png)

Pour expliquer ce graphique à barres empilées : dans la phase de développement initiale, le mauvais code est **légèrement** plus coûteux à modifier que le clean code.

Mais à mesure que nous passons aux phases de maintenance et de refactorisation, l'écart se creuse considérablement, le mauvais code coûtant presque deux fois plus cher que le clean code.

Arrivé à la phase legacy, le mauvais code atteint un coût de 100 % – il est désormais extrêmement coûteux à mettre à jour, tandis que le clean code reste plus gérable à 45 %.

À ce jour, l'analyse la plus récente sur le coût de la mauvaise qualité logicielle aux États-Unis est le rapport 2022 du Consortium for Information and Software Quality ([cisq.org][27]). Ce rapport estime que la mauvaise qualité logicielle a coûté à l'économie américaine au moins 2,41 billions de dollars en 2022, la dette technique représentant environ 1,52 billion de dollars de ce montant.

Vous pouvez [en lire plus à ce sujet ici][28].

Les discussions récentes continuent de souligner l'impact significatif de la dette technique sur la qualité logicielle et la performance des entreprises.

Par exemple, [une enquête de 2024][29] a indiqué que pour plus de 50 % des entreprises, la dette technique représente plus d'un quart de leur budget informatique total. Et cela peut réellement entraver l'innovation si ce n'est pas traité.

Comme vous pouvez le voir, il ne fait aucun doute que le mauvais code est un problème coûteux dans le développement logiciel.

## **Développeur propre vs Développeur désordonné**

Voici un graphique qui montre le parcours de **deux types** de développeurs :

![Image of clean code vs bad code graph chart](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/c6ubf77uwipf4gtucw8q.png)

-   **⚠️ Le développeur désordonné (Ligne rouge) :** Commence vite mais s'écrase brutalement. Plus il écrit de lignes, plus il crée de problèmes.
    
-   **⚡ Le développeur propre (Ligne bleue) :** Commence lentement mais reste constant. La croissance ne s'arrête pas — elle s'accélère.
    

🫵 Maintenant, décidez quelle ligne vous voulez suivre.

## L'IA ne peut pas vous sauver si votre code est un désordre 🗑️

Quand vous êtes bloqué en écrivant du code, vous pourriez vous tourner vers l'IA. Mais laissez-moi vous dire une chose : l'IA ne peut pas vous sauver si votre code est un désordre.

C'est comme construire une maison sur du sable. Bien sûr, elle tient debout un moment, mais à la moindre rafale de vent ou grosse vague, elle s'effondre.

Rappelez-vous : l'IA n'est qu'un outil. Si vous ne savez pas comment écrire des applications propres et évolutives, vous vous préparez à l'échec.

Si vous ne pouvez pas maintenir le code que vous écrivez, vous avez des ennuis.

J'ai vu cela maintes et maintes fois : des développeurs qui connaissent cinq langages de programmation. Ils peuvent construire des applications, des sites web, des logiciels. Ils connaissent les algorithmes et les structures de données sur le bout des doigts.

Mais face à un projet de grande envergure ou au code désordonné de quelqu'un d'autre, ils s'effondrent.

Ils sont comme un ingénieur aérospatial qui conçoit et construit ses propres avions mais ne sait pas les piloter. Ils s'écrasent contre leur propre code.

C'était mon cas... il y a bien longtemps. J'écrivais des milliers de lignes de code, pour réaliser ensuite que je ne comprenais même pas ce que j'avais écrit la semaine précédente. C'était le chaos.

Mais j'ai fini par comprendre — chaque développeur lutte avec cela. Ce n'était pas une question de quantité de connaissances. C'était une question d'organisation et de structuration de ce que je savais. En d'autres termes, il s'agissait de connaître l'art de la programmation lui-même.

J'ai décidé d'échapper à ce piège. Après cinq mois de travail intense — quatre à cinq heures par jour à écrire, concevoir et rechercher — j'ai créé ce que j'aurais aimé avoir quand j'ai commencé la programmation. Un livre qui est un guide complet pour débutants : **Clean Code Zero to One.**

![cover image of clean code zero to one: from messy code to masterpiece](https://cdn.hashnode.com/res/hashnode/image/upload/v1737731329839/c4c862d9-7fdc-460a-ae2e-18b19468b6ec.png)

Si vous voulez en savoir plus sur le livre, je vous donne tous les détails à la fin de ce tutoriel. Alors continuez votre lecture pour en apprendre davantage sur l'écriture d'un code propre.

## 12 patterns de conception Clean Code pour construire des applications Agile ⚖️

Si votre code ne suit pas ces patterns de conception clean code modernes, vous pourriez créer une bombe à retardement. Ces patterns sont vos outils. Maîtrisez-les et profitez du succès de vos projets. Laissez-moi vous les montrer un par un.

### **🌿 Utilisez des noms qui ont du sens**

Nommer vos variables ou fonctions `b` ou `x` n'est pas utile. Appelez-les par ce qu'elles sont pour qu'elles soient plus faciles à comprendre. Voici un exemple de mauvais et de bon nom de variable :

```
// Weak and vague
let b = 5;

// Strong and clear
let numberOfUsers = 5;
```

Les gens qui écrivent des noms peu clairs ne veulent pas assumer leurs erreurs. Ne soyez pas cette personne.

![Comic showing a bad vs a good variable name, by Shahan](https://cdn.hashnode.com/res/hashnode/image/upload/v1736165724746/37b2edc3-3c68-47a8-ab6f-f131a2239a01.png)

### **🔨 Gardez les fonctions focalisées (SRP)**

Une fonction devrait faire **une seule chose**—et la faire parfaitement. C'est ce qu'on appelle le Principe de Responsabilité Unique (**SRP**).

Un bon code est comme un marteau. Il frappe un clou, pas dix. Par exemple, si vous embauchez quelqu'un pour tout faire dans votre entreprise — finance, ventes, marketing, ménage, et ainsi de suite — il échouera probablement lamentablement parce qu'il ne peut pas se concentrer sur une seule chose. Il en va de même pour vos classes dans le code.

🚧 Lorsqu'une classe ou une fonction fait plus d'une chose, elle devient un fouillis inextricable. Le débogage ressemble alors à la résolution d'un puzzle à l'envers. Si votre classe gère à la fois la saisie utilisateur et les opérations de base de données, par exemple, ce n'est pas du multitâche — c'est de la folie. Divisez-la. Une méthode, une tâche.

**🔥 Ma règle :** Votre code travaille pour vous. Gardez-le tranchant, focalisé et contrôlable, ou c'est lui qui va vous contrôler. Voici comment y parvenir :

```
// Clean: One job, one focus
function calculateTotal(a, b) {
    return a + b;
}

function logTotal(user, total) {
    console.log(`User: ${user}, Total: ${total}`);
}

// Messy: Trying to do EVERYTHING
function calculateAndLogTotal(a, b, user) {
    let total = a + b;
    console.log(`User: ${user}, Total: ${total}`);
}
```

🪧 Quand vous mélangez les tâches, vous mélangez la confusion. C'est aussi simple que cela.

### **🚪 Utilisez les commentaires avec discernement**

Il y a un grand dicton parmi les développeurs professionnels :

> « Le code parle de lui-même. »

Vous n'expliquez pas ce qu'une porte fait chaque fois que quelqu'un entre dans une pièce, n'est-ce pas ? Votre code devrait fonctionner de la même manière.

Les commentaires ne sont pas mauvais, mais si votre code ne peut pas se suffire à lui-même, alors vous avez peut-être un problème.

🪧 Un bon commentaire devrait dire « pourquoi » et non « comment ou quoi ». Si un développeur ne comprend pas « comment » quelque chose fonctionne, il est probable qu'il ne comprendra pas non plus « pourquoi ».

Voici quelques courts exemples de bons vs mauvais commentaires. Je vous montrerai également un projet réel pour l'écriture de commentaires propres.

**Exemple 1 : Mauvais commentaire 👎**

```
// Multiply the price by the quantity to calculate the total
const total = price * quantity;
```

C'est un **mauvais commentaire** car il répète simplement ce que le code dit déjà. Le code `price * quantity` est explicite, donc le commentaire n'ajoute rien d'utile.

**Bon commentaire : 👍**

Si le code est clair et simple, **vous n'avez pas besoin de commentaire.**

```
const total = price * quantity;
```

![Image illustrating unnecessary comment vs "silent comment", by Shahan](https://cdn.hashnode.com/res/hashnode/image/upload/v1736165891398/6a942ad7-5b09-4990-9c7f-95358dafcbf3.png)

**Exemple 2 : Mauvais commentaire 👎**

```
// Check if the user logged in
function isUserLoggedIn(session) {
    return !!session.user;
}
```

Ce commentaire est mauvais car il n'explique pas pourquoi `isUserLoggedIn()` existe. Il explique juste ce qui se passe. Mais nous savons déjà qu'il s'agit d'une fonction d'authentification. Ce commentaire est une perte de temps.

**Bon exemple 👍**

```
// The user is authenticated before accessing protected resources
function isUserLoggedIn(session) {
    return !!session.user;
}
```

C'est un **bon commentaire** car il explique **pourquoi** le code existe. Il nous indique que la fonction vérifie si l'utilisateur est authentifié avant d'autoriser l'accès aux parties sensibles de l'application. Il se concentre sur la vue d'ensemble.

![Before: "Check if the user is logged in". After: "The user is authenticated before accessing protected resources." By Shahan.](https://cdn.hashnode.com/res/hashnode/image/upload/v1736166143011/b3ddae3d-41cf-4534-8f1a-af710579922c.png)

### **⚡ Meilleures pratiques pour écrire de bons commentaires**

1.  **Expliquez le « Pourquoi », pas le « Quoi » :**  
    Écrivez des commentaires pour expliquer le but ou le contexte du code, pas ce que le code fait.
    
2.  **Évitez les commentaires évidents :**  
    N'écrivez pas de commentaires pour des choses que le code rend déjà claires.
    
3.  **Gardez-les courts et précis :**  
    Écrivez des commentaires concis, faciles à lire et qui expliquent directement l'objectif.
    
4.  **Mettez à jour les commentaires régulièrement :**  
    Des commentaires obsolètes peuvent induire les développeurs en erreur, alors mettez-les toujours à jour lorsque le code change.
    

**Exemple concret (avec de bons commentaires) 🛒**

Implémentons ces pratiques dans un projet réel : une grande application d'e-commerce. Une fonction calcule les frais d'expédition en fonction des détails de la commande. Voici le code complet, j'expliquerai chaque commentaire ci-dessous :

```
// Shipping rules:
// - Free shipping for orders over $100
// - Standard shipping ($10) for orders below $100
// - Additional $5 for international orders

function calculateShipping(order) {
    let shippingCost = 0;

    // Check if the order qualifies for free shipping
    if (order.total >= 100) {
        shippingCost = 0; // Free shipping
    } else {
        shippingCost = 10; // Standard shipping cost
    }

    // Add additional cost for international orders
    if (order.isInternational) {
        shippingCost += 5;
    }

    return shippingCost;
}

// Example usage
const order1 = { total: 120, isInternational: false };
const order2 = { total: 80, isInternational: true };

console.log(calculateShipping(order1)); // Output: 0
console.log(calculateShipping(order2)); // Output: 15
```

Au début de la fonction, nous incluons un commentaire expliquant les règles pour les frais de port. Cela donne au lecteur une vue d'ensemble de la logique sans avoir besoin de lire tout le code.

```
// Shipping rules:
// - Free shipping for orders over $100
// - Standard shipping ($10) for orders below $100
// - Additional $5 for international orders
```

Ensuite, la première condition vérifie si le total de la commande est supérieur ou égal à 100 $. Un commentaire ici clarifie **pourquoi** la livraison gratuite est appliquée.

```
// Check if the order qualifies for free shipping
if (order.total >= 100) {
    shippingCost = 0; // Free shipping
}
```

La deuxième condition applique des frais supplémentaires pour l'expédition internationale. Le commentaire explique **pourquoi** ce coût supplémentaire est ajouté.

```
// Add additional cost for international orders
if (order.isInternational) {
    shippingCost += 5;
}
```

**Pourquoi ces commentaires sont-ils bons ?**

Imaginez que vous travaillez dans une équipe de 20 développeurs. Quelqu'un lit la fonction `calculateShipping` six mois plus tard. Sans ces commentaires, il pourrait perdre du temps à deviner pourquoi les commandes internationales ont des frais supplémentaires. Les bons commentaires clarifient le pourquoi et évitent des heures de frustration.

### **🧩 Rendez votre code lisible**

Si quelqu'un lisant votre code a l'impression de résoudre une énigme, vous êtes déjà devenu une source de problèmes. En voici la preuve :

```
// Clean: Reads like a story
if (isLoggedIn) {
    console.log("Welcome!");
} else {
    console.log("Please log in.");
}

// Messy: Feels like chaos
if(isLoggedIn){console.log("Welcome!");}else{console.log("Please log in.");}
```

Si votre code est désordonné et difficile à lire, il déconcertera les autres—et même vous-même plus tard ! Imaginez revenir sur votre propre code après six mois et avoir l'impression de lire une langue étrangère. Un code lisible fait gagner du temps, réduit les bugs et facilite la vie de tout le monde.

**🍵 Pourquoi la lisibilité est-elle importante ?**

1.  **Pour vous-même :** Lorsque vous revisitez votre code après des semaines ou des mois, le clean code vous aide à reprendre là où vous vous étiez arrêté sans perdre de temps à comprendre ce que vous avez fait.
    
2.  **Pour votre équipe :** Si quelqu'un d'autre lit votre code, il ne devrait pas avoir à résoudre un puzzle. Le clean code rend le travail d'équipe plus fluide et prévient les malentendus.
    
3.  **Moins de bugs :** Un code clair est plus facile à déboguer car vous pouvez repérer rapidement les erreurs.
    

**🧙‍♂️ Comment écrire un code lisible**

Construisons un programme simple pour gérer les livres dans une bibliothèque. Nous allons le rendre propre et lisible, puis je détaillerai ce code ci-dessous :

```
// A class to represent a book
class Book {
    constructor(title, author, isAvailable) {
        this.title = title;
        this.author = author;
        this.isAvailable = isAvailable;
    }

    borrow() {
        if (this.isAvailable) {
            this.isAvailable = false;
            console.log(`You borrowed "${this.title}".`);
        } else {
            console.log(`Sorry, "${this.title}" is not available.`);
        }
    }

    returnBook() {
        this.isAvailable = true;
        console.log(`You returned "${this.title}".`);
    }
}

// A function to display available books
function displayAvailableBooks(books) {
    console.log("Available books:");
    books.forEach((book) => {
        if (book.isAvailable) {
            console.log(`- ${book.title} by ${book.author}`);
        }
    });
}

// Example usage
const book1 = new Book("The Clean Coder", "Robert Martin", true);
const book2 = new Book("You Don’t Know JS", "Kyle Simpson", false);
const book3 = new Book("Eloquent JavaScript", "Marijn Haverbeke", true);

const library = [book1, book2, book3];

displayAvailableBooks(library); // Show available books
book1.borrow(); // Borrow a book
displayAvailableBooks(library); // Show available books again
book1.returnBook(); // Return the book
displayAvailableBooks(library); // Final list
```

Nous avons créé une classe `Book` pour représenter chaque livre. Elle possède des propriétés comme `title`, `author` et `isAvailable` pour suivre son état.

-   La méthode `borrow` vérifie si le livre est disponible. Si oui, elle le marque comme indisponible et affiche un message.
    
-   La méthode `returnBook` rend le livre à nouveau disponible.
    
-   La fonction `displayAvailableBooks` parcourt la bibliothèque et n'affiche que les livres disponibles.
    
-   Nous créons trois livres (`book1`, `book2`, `book3`) et les stockons dans un tableau `library`.
    
-   Nous empruntons et rendons des livres, montrant comment la liste des livres disponibles évolue.
    

Comme vous pouvez le voir, le code lisible n'est pas seulement une question de style. Il fait gagner du temps, prévient les bugs et préserve l'utilité de votre code pour les années à venir.

### **🏌️ Testez tout ce que vous écrivez**

Si vous ne prenez pas le temps d'écrire des tests, ne soyez pas surpris si votre code casse. Si vous voulez écrire des tests, suivez cette stratégie de tests unitaires pour anticiper les problèmes.

**Qu'est-ce qu'un test unitaire ?**

Concrètement, le test unitaire vérifie des parties individuelles de votre code (comme des fonctions ou des classes) pour s'assurer qu'elles fonctionnent correctement. C'est comme vérifier la solidité de chaque brique de votre maison avant de construire les murs.

Laissez-moi vous donner un exemple de fonctionnement des tests unitaires :

```
class Calculator {
    add(a, b) { return a + b; }
    subtract(a, b) { return a - b; }
}

// Test it (Unit Test)
const calculator = new Calculator();
console.assert(calculator.add(2, 3) === 5, "Addition failed");
console.assert(calculator.subtract(5, 3) === 2, "Subtraction failed");
```

Voici ce qui se passe dans ce code :

D'abord, nous créons la classe calculator :

```
class Calculator {
    add(a, b) { return a + b; }
    subtract(a, b) { return a - b; }
}
```

La classe `Calculator` possède deux méthodes : `add` et `subtract`.

-   `add(a, b)` prend deux nombres et retourne leur somme.
    
-   `subtract(a, b)` prend deux nombres et retourne leur différence.
    

Ensuite, nous mettons en place les tests :

```
const calculator = new Calculator();
```

Ici, nous créons une instance de la classe `Calculator` pour tester ses méthodes.

Puis nous écrivons des cas de test :

```
console.assert(calculator.add(2, 3) === 5, "Addition failed");
console.assert(calculator.subtract(5, 3) === 2, "Subtraction failed");
```

`console.assert(condition, message)` vérifie si la condition est `true`. Si elle est `false`, le message ("Addition failed" ou "Subtraction failed") s'affiche dans la console.

-   **Premier test** : `calculator.add(2, 3) === 5`
    
    -   Appelle la méthode `add` avec `2` et `3`.
        
    -   Vérifie si le résultat est `5`.
        
-   **Deuxième test** : `calculator.subtract(5, 3) === 2`
    
    -   Appelle la méthode `subtract` avec `5` et `3`.
        
    -   Vérifie si le résultat est `2`.
        

Que se passe-t-il si quelque chose casse ? Il est assez simple de résoudre les problèmes qui surviennent ici. Dans ce cas, si la méthode `add` ou `subtract` ne fonctionne pas correctement, le test échouera. Par exemple :

```
console.assert(calculator.add(2, 3) === 6, "Addition failed");
```

-   La condition `calculator.add(2, 3) === 6` est `false`.
    
-   La console affichera : `"Addition failed"`.
    

**Exemple concret : Tester un système de connexion 👥**

Testons un système de connexion simple pour voir comment les tests unitaires fonctionnent dans un scénario réel.

```
class Auth {
    login(username, password) {
        return username === "admin" && password === "1234";
    }
}

// Test the Auth class
const auth = new Auth();
console.assert(auth.login("admin", "et5t45#@") === true, "Login failed for valid credentials");
console.assert(auth.login("user", "wrongpassword") === false, "Login succeeded for invalid credentials");
```

D'abord, créez la classe `Auth` :

```
class Auth {
    login(username, password) {
        return username === "admin" && password === "1234";
    }
}
```

La méthode `login` vérifie si le nom d'utilisateur est `"admin"` et le mot de passe `"1234"`. Si les deux correspondent, elle retourne `true` – sinon, `false`.

Ensuite, mettez en place les tests :

```
const auth = new Auth();
```

Créez une instance de la classe `Auth`. Puis écrivez les cas de test :

```
console.assert(auth.login("admin", "1234") === true, "Login failed for valid credentials");
console.assert(auth.login("user", "wrongpassword") === false, "Login succeeded for invalid credentials");
```

-   **Premier test** : Vérifie si des identifiants valides (`"admin"`, `"1234"`) réussissent. Sinon, `"Login failed for valid credentials"` s'affiche.
    
-   **Deuxième test** : Vérifie si des identifiants invalides (`"user"`, `"wrongpassword"`) échouent. Sinon, `"Login succeeded for invalid credentials"` s'affiche.
    

**🌱 Pourquoi les tests aboutissent à un code propre :**

1.  Vous écrivez naturellement des fonctions plus petites et plus focalisées pour rendre votre code testable.
    
2.  Les tests vérifient que votre code se comporte comme prévu sous différentes conditions.
    
3.  Avec des tests en place, vous pouvez mettre à jour votre code en toute confiance, sachant que les tests détecteront toute erreur.
    

### **💉 Utilisez l'injection de dépendances**

Coder des dépendances en dur, c'est comme se tatouer le nom de quelqu'un sur le front — c'est permanent, cela peut être abrasif et cela vous enferme.

Alors, que fait l'injection de dépendances ? Elle vous permet de gérer les relations de votre code en passant les dépendances comme arguments. C'est flexible, adaptable et maintenable.

Pour démontrer comment cela fonctionne, j'utilise ici la dépendance Nodemailer pour envoyer des e-mails aux utilisateurs :

```
// Dependency: Sending emails with Nodemailer
const nodemailer = require('nodemailer');
function sendEmail(to, subject, message) {
    const transporter = nodemailer.createTransport({ /* config */ });
    return transporter.sendMail({ from: "programmingwithshahan@gmail.com", to, subject, text: message });
}
```

⚠️ Pour vous prémunir des risques, assurez-vous d'éviter de **coder en dur** les dépendances. Utilisez l'abstraction ou des fichiers de configuration pour une maintenance sécurisée.

Ceci n'est qu'un exemple. En tant que développeur, vous pouvez utiliser des centaines de bibliothèques ou de dépendances.

Je ne dis pas que vous ne devriez pas du tout vous appuyer sur des dépendances/bibliothèques, car il est aujourd'hui difficile de s'en passer. Mais vous devriez être très prudent avant de les installer dans vos projets.

Vous devriez vérifier la sécurité, la performance, la qualité ou la fonctionnalité des systèmes logiciels d'une organisation. Car ils contiennent parfois des risques qui peuvent ruiner l'intégralité de votre projet.

🚧 Contrôlez toujours vos outils, ne les laissez pas vous contrôler.

### **📂 Des structures de projet propres**

Un projet bien organisé fait la différence entre un **dépotoir** et une **boutique** haut de gamme.

Voici comment chaque dossier devrait être organisé :

![Image of clean code project structure by shahan](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9xwyg9iqqcybz21lsgxz.png)

Si votre base de code ressemble à un tiroir à bric-à-brac, vous avez déjà causé des problèmes à votre futur "vous".

Parcourons la structure de projet propre que vous voyez ci-dessus pour mieux la comprendre :

**1.** `myProjet/src`

C'est le conteneur principal pour l'intégralité de votre application. Tout ce dont votre application a besoin est stocké dans ce dossier. Il contient des sous-dossiers pour garder les choses ordonnées et gérées en un seul endroit.

**2.** `components`

C'est ici que vous gardez toutes les pièces réutilisables de votre application. Vous pouvez utiliser ces composants à plusieurs endroits sans avoir à les reconstruire.

**3.** `services`

C'est le « cerveau » de votre application. Il gère tout le travail en coulisses pour le frontend et le backend. `emailService.js`, `userService.js` et `productService.js` sont quelques exemples de fichiers pour votre dossier `services`.

**4.** `utils`

Il contient tous les petits outils pratiques dont vous avez besoin pour que votre application fonctionne sans accroc et pour vous faciliter la vie. Par exemple, `formatedate.js`, `validateEmail.js` et `generateId.js` sont des fichiers utilitaires courants pour créer des pièces de composants réutilisables pour l'ensemble de votre projet.

#### **5.** `tests`

Par convention, les fichiers de test sont généralement situés **à l'extérieur** du dossier `src`, au niveau de la racine du projet. Cela permet de séparer votre code de production (`src`) de votre code de test (`tests`), ce qui le rend plus propre et plus facile à gérer. Regardez :

```
myProject/
├── src/              # Production code
│   ├── components/
│   ├── services/
│   └── utils/
├── tests/            # Test files
│   ├── components/
│   ├── services/
│   └── utils/
├── package.json      # Project configuration
└── README.md         # Documentation
```

Certains développeurs préfèrent créer un seul fichier de test dans le dossier `test` pour tout tester au même endroit. Malheureusement, cela peut sembler propre au début, mais à mesure que votre projet grandit, vous devrez chercher des blocs de code spécifiques. C'est inélégant et cela peut produire des résultats de tests inattendus. Il est donc fortement recommandé de les diviser en plusieurs fichiers de test dans le dossier `tests`.

**Exemple concret 📧**

Laissez-moi créer pour vous une structure de projet propre et durable à appliquer dans tous vos futurs projets. Inutile de dire qu'une structure de projet propre est la base de la construction d'un projet maintenable.

À partir de notre exemple précédent d'application d'envoi d'e-mails, nous allons écrire une structure de projet propre. Nous voulons construire une application qui envoie des e-mails aux utilisateurs. Votre structure de projet propre pour cette application devrait ressembler à ceci :

![Image of email app clean code project structure by shahan](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6v6rlc5qiplgxz1h4dps.png)

Comme vous pouvez le voir, j'ai regroupé chaque sous-dossier et fichier à l'intérieur du dossier `src` qui est le conteneur principal de notre application. À l'intérieur du dossier `src`, nous avons créé `components`, `services`, `utils`. Enfin, nous avons un dossier `tests` gérable à l'extérieur du dossier `src` pour tester chaque composant indépendamment. Ce dossier de test n'a rien à voir avec notre code de production situé dans le dossier `src`.

### **🤹‍♂️ Soyez cohérent avec le formatage**

N'écrivez pas de code comme si vous étiez 10 personnes différentes. Soyez cohérent avec votre formatage.

Utilisez des outils comme [Prettier][30] ou [ESLint][31] pour imposer un style cohérent. Si chaque fichier a un aspect différent, vous créez un chaos que personne ne voudra réparer.

Je dirais que la cohérence dans le formatage est l'un des aspects les plus importants de l'écriture d'un code propre.

Regardez...

![Image of consistent formatting snippets from clean code zero to one book](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/46zu4k5nnrkcdesgqrye.png)

```
// Always use 2 spaces for indentation
function calculateArea(width, height) {
  if (width <= 0 || height <= 0) {
    throw new Error("Dimensions must be positive numbers.");
  }
  return width * height;
}

// Add meaningful whitespace for readability
const rectangle = {
  width: 10,
  height: 20,
};

// Clear separation of logic
try {
  const area = calculateArea(rectangle.width, rectangle.height);
  console.log(`Area: ${area}`);
} catch (error) {
  console.error(error.message);
}
```

Examinons certains aspects de ce code qui le rendent propre :

#### 1️⃣ Indentation cohérente

Pourquoi 2 ou 4 espaces ? C'est propre, minimaliste et universellement accepté dans de nombreux guides de style JavaScript. Cela ne fatigue pas les yeux, et la structure du code ressort clairement. Lorsque vous mélangez des indentations incohérentes (2 espaces ici, 4 espaces là), vous déconcertez les gens—et les gens déconcertés font des erreurs.

#### 2️⃣ Espaces blancs significatifs : Donner de l'air au code

Ce saut de ligne supplémentaire entre la définition du rectangle et le bloc `try` est comme une pause dans une phrase — il donne au lecteur le temps de traiter l'information.

#### 3️⃣ Séparation claire de la logique : Pensée modulaire

```
try {
  const area = calculateArea(rectangle.width, rectangle.height);
  console.log(`Area: ${area}`);
} catch (error) {
  console.error(error.message);
}
```

Regardez comment la logique est divisée en sections claires :

-   D'abord, le calcul (fonction `calculateArea`).
    
-   Ensuite, la sortie (`console.log`).
    
-   Enfin, la gestion des erreurs (bloc `catch`).
    

Chaque tâche a son propre espace et son propre but.

#### 4️⃣ Gestion des erreurs lisible

Lorsque vous lancez des erreurs ou enregistrez des messages, vous les formatez proprement. Pas de messages vagues ou cryptiques ici. Un développeur voyant cela connaîtra immédiatement le problème.

```
throw new Error("Dimensions must be positive numbers.");
```

**🐦‍⬛ Conseils généraux pour un formatage cohérent :**

-   Utilisez 2 ou 4 espaces pour l'indentation de manière cohérente dans toute votre base de code. Évitez les tabulations pour maintenir l'uniformité entre les différents éditeurs.
    
-   Limitez les lignes à un maximum de 100-120 caractères pour éviter le défilement horizontal et améliorer la lisibilité.
    
-   Regroupez la logique associée et séparez les blocs de code par des lignes vides pour souligner leur but.
    
-   Enfin, évitez de trop aligner le code. Laissez plutôt l'indentation guider naturellement le flux de la logique.
    

### **✋ Arrêtez de coder des valeurs en dur**

Coder des valeurs en dur (hardcoding) est une façon paresseuse de coder. En voici la preuve :

```
// Bad: Hardcoded and rigid
function createUser() {
    const maxUsers = 100;
    if (currentUsers >= maxUsers) throw "Too many users!";
}

// Clean: Dynamic and flexible
const MAX_USERS = 100;
function createUser() {
    if (currentUsers >= MAX_USERS) throw "Too many users!";
}
```

Vous voyez, changer cette variable ne vous surprendra pas à l'avenir. Vous savez exactement où la trouver pour modifier des valeurs incertaines.

Il est préférable de stocker vos valeurs fixes dans le fichier de configuration globale (config).

🪧 Évitez donc à tout prix de coder des valeurs en dur. Le hardcoding est le raccourci qui risque de rendre fou votre futur "vous" (ou les autres).

### **🤏 Gardez les fonctions courtes**

Si votre fonction fait plus de 20 lignes, elle essaie probablement d'en faire trop.

Les fonctions courtes sont des fonctions percutantes. Elles atteignent leur but à chaque fois.

Les fonctions longues et boursouflées sont désordonnées et difficiles à lire, mais les fonctions courtes sont claires et focalisées. Voici comment vos grandes fonctions devraient être décomposées :

```
function updateCart(cart, item) {
    addItemToCart(cart, item);
    let total = calculateTotal(cart);
    logTransaction(item, total);
    return total;
}

function addItemToCart(cart, item) {
    cart.items.push(item);
}
```

Laissez-moi vous expliquer ce code pour que vous compreniez pourquoi décomposer les grandes fonctions est une stratégie gagnante.

1.  **La fonction principale :** `updateCart()` appelle de plus petites fonctions d'aide pour gérer des tâches spécifiques comme :
    
    -   Ajouter l'article au panier.
        
    -   Calculer le prix total.
        
    -   Enregistrer les détails de la transaction.
        
    -   Enfin, elle retourne le prix total.
        

Au lieu d'un seul long bloc de code qui essaie de tout faire, elle délègue les tâches à des fonctions d'aide.

2.  **Fonction d'aide :** `addItemToCart()` Cette fonction gère **uniquement** l'ajout de l'article au panier. Si vous devez changer la façon dont les articles sont ajoutés (par exemple, vérifier les doublons), vous pouvez simplement modifier cette petite fonction au lieu de fouiller dans un bloc de code géant dans `updateCart`. C'est ainsi que l'on écrit des fonctions clean code agréables à lire et faciles à maintenir.

**Que se passe-t-il si les fonctions sont trop longues ? 💤**

Supposons que vous n'ayez pas décomposé la fonction `updateCart`. Voici à quoi elle pourrait ressembler :

```
function updateCart(cart, item) {
    cart.items.push(item);
    let total = 0;
    for (let i = 0; i < cart.items.length; i++) {
        total += cart.items[i].price;
    }
    console.log(`Added ${item.name}. Total is now $${total}.`);
    return total;
}
```

Quels sont les problèmes ici ?

-   Elle essaie de tout faire.
    
-   Elle est difficile à lire, surtout si elle s'agrandit.
    
-   Si quelque chose casse, vous perdrez du temps à chercher quelle partie pose problème.
    

Maintenant, le choix vous appartient : restez sur l'approche désordonnée « tout-en-un » ou pratiquez l'état d'esprit propre « une fonction, une tâche ».

### **⛺ Suivez la règle du Boy Scout**

> Laissez toujours votre campement plus propre que vous ne l'avez trouvé.

Laissez-moi vous expliquer. On ne se contente pas d'utiliser quelque chose pour le laisser dans un état pire qu'avant. C'est un comportement inconsidéré. Les vrais professionnels laissent les choses dans un meilleur état qu'ils ne les ont trouvées.

En termes de code, chaque fois que vous touchez à la base de code, **améliorez-la.** Nettoyez-la, refactorisez les parties désordonnées et améliorez la lisibilité. Si vous ne le faites pas, vous ne faites qu'accumuler des déchets qui finiront par vous tomber sur la tête.

Voici un exemple. Au lieu de l'améliorer, nous ajoutons simplement des couches de complexité :

```
// Original code: Hard to read, poorly named variables
function calc(a, b) {
  let x = a + b;
  let y = x * 0.2;
  return y;
}

// We're adding to it but not cleaning it up
function calcDiscount(a, b, discountRate) {
  let total = calc(a, b);
  let final = total - discountRate;
  return final;
}
```

Après : cela s'améliore à chaque fois. Voici comment travaille un codeur discipliné — il améliore au fur et à mesure :

```
// Improved code: Clear names, refactored for clarity
function calculateSubtotal(price, quantity) {
  return price * quantity;
}

function calculateDiscountedTotal(price, quantity, discountRate) {
  const subtotal = calculateSubtotal(price, quantity);
  const discount = subtotal * discountRate;
  return subtotal - discount;
}
```

Désormais, n'importe qui peut comprendre ce qui se passe d'un coup d'œil. Parce que nous avons décomposé le code en fonctions plus petites et plus focalisées. Ainsi, l'ajout de nouvelles fonctionnalités ne cassera pas les fonctionnalités existantes. 🏕️

### **🏟️ Suivez le principe Ouvert/Fermé**

Ce principe de conception suggère que votre code devrait être conçu pour permettre des extensions sans changer les fondations existantes.

Vous voulez ajouter des fonctionnalités — pas tout déchirer à chaque mise à jour. Modifier l'ancien code pour l'adapter à de nouvelles exigences, c'est exactement comme essayer de reconstruire votre maison chaque fois que vous achetez de nouveaux meubles. Ce n'est pas viable.

Voyons comment vous pouvez construire un code plus intelligent et évolutif qui vous permet d'ajouter des fonctionnalités sans tout casser.

#### Avant : Violation du principe

Vous avez une classe pour gérer les paiements — assez simple. Au début, elle ne gère que les cartes de crédit.

Mais ensuite, votre patron arrive et dit : *« Hé, maintenant nous avons besoin du support PayPal. »*

Et parce que vous n'avez pas pris la peine d'apprendre le clean code, votre code ressemble à un monstre de spaghettis sorti tout droit d'un système d'entreprise hérité de 1995. Voici le chef-d'œuvre que vous avez conçu :

```
class PaymentProcessor {
  processPayment(paymentType, amount) {
    if (paymentType === "creditCard") {
      console.log(`Processing credit card payment of $${amount}`);
    } else if (paymentType === "paypal") {
      console.log(`Processing PayPal payment of $${amount}`);
    } else {
      throw new Error("Unsupported payment type");
    }
  }
}

const paymentProcessor = new PaymentProcessor();
paymentProcessor.processPayment("creditCard", 100);
paymentProcessor.processPayment("paypal", 200);
```

Hélas ! Chaque nouveau type de paiement (comme Apple Pay, Google Pay, etc.) nécessite de modifier la méthode `processPayment`. Inutile de dire que vous risquez de casser les fonctionnalités existantes tout en ajoutant de nouvelles fonctionnalités. Si vous aviez appris ce principe, vous ne seriez peut-être pas dans ce pétrin.

Ne vous inquiétez pas : je vais vous aider à corriger cela. D'abord, nous devons refactoriser le code. Au lieu de modifier la classe existante, nous allons étendre sa fonctionnalité en utilisant le [polymorphisme][32] :

```
javascriptCopy code// Base class
class PaymentProcessor {
  processPayment(amount) {
    throw new Error("processPayment() must be implemented");
  }
}

// Credit card payment
class CreditCardPayment extends PaymentProcessor {
  processPayment(amount) {
    console.log(`Processing credit card payment of $${amount}`);
  }
}

// PayPal payment
class PayPalPayment extends PaymentProcessor {
  processPayment(amount) {
    console.log(`Processing PayPal payment of $${amount}`);
  }
}

// Adding a new payment type? Just extend the class!
class ApplePayPayment extends PaymentProcessor {
  processPayment(amount) {
    console.log(`Processing Apple Pay payment of $${amount}`);
  }
}

// Usage
const payments = [
  new CreditCardPayment(),
  new PayPalPayment(),
  new ApplePayPayment(),
];

payments.forEach((payment) => payment.processPayment(100));
```

Désormais, l'ajout de nouvelles méthodes de paiement ne nécessite pas de modifier la classe `PaymentProcessor` existante. Vous venez de créer une nouvelle sous-classe. Ainsi, le code original reste intact, ce qui signifie qu'il n'y a aucun risque de casser les fonctionnalités existantes.

Chaque type de paiement a sa propre classe, et l'ajout du support de paiement PayPal, par exemple, ne casse pas le code. Maintenant, vous pouvez répondre à votre patron : *« Bien sûr, j'ajouterai cette fonctionnalité en 5 minutes. »* Votre promotion n'attend que vous.

Je partage encore plus de conseils dans mi livre [Clean Code Zero to One][33].

## Résumé des meilleures pratiques modernes pour vous aider à écrire du Clean Code 🥷

Laissez-moi maintenant vous montrer les meilleures pratiques et résumer nos 12 principes de conception Clean Code pour vous aider à écrire un code propre pour le développement d'applications Agile.

### 🔎 Code Smells courants et comment les corriger

-   💊 Duplication : Si vous copiez du code, vous vous créez plus de travail. Extrayez-le dans une fonction, et faites-le correctement.
    
-   🛤️ Méthodes longues : Si votre méthode nécessite une barre de défilement, c'est qu'elle en fait trop. Décomposez-la, gardez-la focalisée.
    
-   👑 Objets rois : Aucune classe ne devrait tout faire. Simplifiez les responsabilités, sinon votre base de code deviendra désordonnée.
    

### 💬 Pratiques de commentaires efficaces

-   💭 Quand commenter : Ne commentez que si le code n'est pas clair. S'il l'est, les commentaires ne sont que du désordre.
    
-   🫗 Clarté : Les commentaires devraient dire pourquoi, pas quoi. Si votre code a besoin d'explications, c'est peut-être qu'il est trop complexe.
    
-   🌴 Évitez la redondance : Ne commentez pas ce qui est évident. Si votre fonction s'appelle `addNumbers`, ne commentez pas qu'elle fait cela.
    

### 🧼 Techniques de refactorisation pour un Clean Code

-   🏭 Extraire des méthodes : Des méthodes trop grandes ? Décomposez-les. Ce n'est pas seulement une question de propreté — c'est une question de contrôle.
    
-   🫕 Renommer les variables : Si les noms de vos variables ne crient pas leur but, changez-les et améliorez-les. La précision dans le nommage est la précision dans la pensée.
    
-   🍃 Simplifier les conditionnelles : Si vos conditionnelles ressemblent à de l'algèbre, simplifiez-les. Si `a == true`, écrivez simplement `if(a)`.
    

### 🧪 Tests et Clean Code

-   🧙 Tests unitaires : Testez chaque morceau de code comme si vous interrogiez un suspect. Ne laissez rien au hasard.
    
-   🏇 TDD (Test Driven Development) : Écrivez les tests d'abord. Il ne s'agit pas seulement de traquer les bugs, il s'agit de savoir exactement ce que votre code doit faire avant de l'écrire.
    
-   🧽 Tests propres : Vos tests devraient être aussi propres que votre code. S'ils sont désordonnés, ils ne seront pas utiles.
    

### 🐛 Gestion des erreurs et Clean Code

-   ⁉️ Exceptions : Utilisez-les. Elles ne servent pas qu'aux erreurs, elles servent aussi à garder votre code propre du désordre lié aux erreurs.
    
-   🖍️ Échouer rapidement (Fail fast) : Si quelque chose ne va pas, arrêtez-vous tout de suite. Ne laissez pas les erreurs s'accumuler. Traitez-les immédiatement.
    
-   🚨 Logging : Enregistrez les logs comme si vous documentiez une scène de crime. Clair, précis et seulement ce qui est nécessaire.
    

### 🌱 Revues de code et Clean Code

-   🚢 Processus : Ayez un système. Pas de code « cowboy ». Révisez, critiquez, améliorez.
    
-   🔪 Outils : Utilisez des outils qui facilitent les revues. Ils ne servent pas seulement à attraper les erreurs, ils servent aussi à enseigner la discipline.
    
-   🧦 Culture : Cultivez une culture où le feedback est précieux. Aidez votre équipe à apprendre comment gérer et recevoir les critiques.
    

## Outils automatisés pour maintenir un code propre ⚓

Les outils et les techniques d'automatisation peuvent être très utiles pour écrire du clean code. Si vous n'utilisez pas les bons outils et n'automatisez pas les choses pour gagner du temps, vous passez à côté de quelque chose.

Vous pensez pouvoir juger de la qualité du code « à l'œil nu » ? Détrompez-vous. Sans automatisation, voici ce qui arrive :

1.  👎 Vous manquez des erreurs évidentes parce que vous êtes « trop occupé ».
    
2.  🤕 Votre code a un aspect différent dans chaque fichier, faisant de la collaboration un casse-tête.
    
3.  🪦 Le déploiement échoue parce que vous avez sauté un test critique.
    

Les développeurs qui réussissent utilisent les bons outils pour automatiser le code et faire avancer les choses. Voici quatre stratégies pour maintenir un code propre à l'aide d'outils modernes.

### **1️⃣ Analyse statique**

L'analyse statique est en fait un inspecteur de code qui parcourt votre code et signale les problèmes potentiels dès le début. Le meilleur dans tout ça ? Elle fonctionne **avant** l'exécution, capturant des erreurs qui pourraient autrement mener à des plantages, des temps d'arrêt ou des bugs embarrassants.

#### **Comment ça marche ?**

1.  **Vérification de la syntaxe** : Elle examine votre code pour analyser si tout est écrit avec la syntaxe correcte. Si vous orthographiez mal une variable ou oubliez une parenthèse fermante, elle vous le signalera instantanément.
    
2.  **Règles de qualité du code** : Des outils comme ESLint imposent des règles telles qu'une indentation cohérente, l'évitement des variables inutilisées et le respect des meilleures pratiques.
    
3.  **Prévention des erreurs** : Elle identifie les erreurs de logique, comme l'utilisation de variables non définies ou des comparaisons qui n'ont pas de sens.
    

Voici comment l'analyse statique fonctionne en action :

#### 🚨 Avant l'analyse statique :

```
let sum = (a, b) => { return a + b; }
console.log(sume(2, 3)); // Typo, unnoticed until runtime
```

-   **Problème** : La faute de frappe dans `sume` ne causera une erreur qu'au moment de l'exécution, ce qui pourrait mener à des sessions de débogage frustrantes ou pire — casser l'application en production.

#### 🚑 Après l'analyse statique (avec ESLint) :

```
codeError: 'sume' is not defined.
```

-   **Solution** : [ESLint][34] signale immédiatement la faute de frappe avant même que vous n'exécutiez le code. L'erreur est capturée tôt, vous faisant gagner du temps et vous évitant des maux de tête.

### **2️⃣ Formatage de code automatisé**

Avant le formatage :

```
function calculate ( x , y ){ return x+ y;}
console.log( calculate (2,3 ) )
```

-   **Problème** : L'espacement et le formatage incohérents rendent le code plus difficile à lire.

#### Après avoir utilisé Prettier :

```
function calculate(x, y) {
  return x + y;
}
console.log(calculate(2, 3));
```

-   **Solution** : Un formatage propre, cohérent et professionnel est appliqué automatiquement. Plus besoin de pinailler sur les espaces ou l'alignement.

C'est assez basique. J'ai abordé cela au cas où vous écririez du code dans un bloc-notes ou quelque chose où l'IDE n'est pas fourni (par exemple, lors d'un entretien d'embauche).

### **3️⃣ Tests d'intégration continue (CI)**

Les tests CI garantissent que chaque nouveau changement apporté à votre code est vérifié automatiquement. C'est comme un filet de sécurité qui capture les bugs introduits pendant le développement. Les outils de CI exécutent vos tests chaque fois que vous poussez du code, afin que rien ne casse après le déploiement.

#### **Comment fonctionnent les tests CI ?**

1.  **Déclenchement sur changement** : Chaque fois que le code est commité, l'outil de CI (comme [GitHub Actions][35], [Jenkins][36]) exécute des tests automatisés.
    
2.  **Feedback** : Il vous donne un retour instantané si quelque chose échoue.
    
3.  **Empêche le code cassé** : Seuls les commits propres et le code fonctionnel sont fusionnés dans la branche principale.
    

### **4️⃣ Pipelines CI/CD**

Nous utilisons également les pipelines CI/CD comme un processus continu qui inclut la construction du code, les tests et le déploiement, tandis que les tests CI sont une partie de ce processus qui se concentre sur l'automatisation des tests des changements de code.

**Différence entre pipelines CI/CD vs tests CI :**

-   **Pipelines CI/CD :** Un pipeline CI/CD combine la construction, les tests et le déploiement du code en un seul processus. Ce processus garantit que tous les changements apportés au code de la branche principale sont publiables en production. Les pipelines CI/CD peuvent réduire le temps de déploiement, diminuer les coûts et améliorer la collaboration d'équipe.
    
-   **Tests CI :** Les tests CI sont le processus de test automatique des changements de code qui sont intégrés dans un dépôt central. Les tests CI se concentrent sur la garantie que la base de code est stable et que les problèmes d'intégration sont résolus. Les tests CI aident les développeurs à construire des logiciels stables, sans bugs et répondant aux exigences fonctionnelles.
    

🚧 Voilà ce que sont réellement les concepts de tests CI et de pipelines CI/CD. Pas aussi complexe qu'il n'y paraît. Laissez-moi élaborer davantage sur les tests CI avec GitHub Actions, car nous exécutons généralement les tests via des outils automatisés de nos jours.

### **⚡ Tests d'intégration continue (CI) avec GitHub Actions**

Comme je l'ai dit plus tôt, les outils de CI exécutent des tests automatisés chaque fois que vous poussez du code ou ouvrez une pull request. Cela garantit que seul un code fonctionnel et sans bug est fusionné dans la branche principale.

#### Comment mettre en place des tests CI avec GitHub Actions

**Étape 1 : Créez votre dépôt**

Configurez un dépôt GitHub pour votre projet. Ensuite, poussez votre code sur GitHub en utilisant les commandes suivantes :

```
git init
git add .
git commit -m "Initial commit for CI Testing"
git branch -M main
git remote add origin https://github.com/codewithshahan/codewithshahan.git
git push -u origin main
```

Ou vous pouvez créer un nouveau dépôt depuis votre compte GitHub sans utiliser la commande. Connectez-vous simplement à votre compte GitHub et visitez le tableau de bord. Ici, vous trouverez un bouton « New » pour créer un tout nouveau dépôt :

![image of creating a new repo on github by Shahan](https://cdn.hashnode.com/res/hashnode/image/upload/v1737618697327/dcef8be8-0d08-45d7-8000-34c4c65df425.png)

**Étape 2 : Ajoutez un workflow GitHub Actions**

Naviguez vers l'onglet **Actions** de votre dépôt. Pour ce faire, vous devez d'abord visiter votre dépôt sur GitHub (vous trouverez le lien après avoir créé votre dépôt). Dans ce cas, j'ai créé un nouveau dépôt appelé « codewithshahan ». Ici, cherchez l'onglet **Actions** sur le côté droit de la barre de navigation.

![Image of github actions navigation tab by shahan](https://cdn.hashnode.com/res/hashnode/image/upload/v1737618879398/7c5aa37a-72be-4701-a8f8-9ea9e05c0d5d.png)

Après avoir navigué dans l'onglet Actions, faites défiler un peu vers le bas et vous trouverez la section **continuous integration** :

![Image of CI (Continuous Integration) testing on Github Actions Page by Shahan](https://cdn.hashnode.com/res/hashnode/image/upload/v1737619002674/60003e57-f2b2-48f1-bef8-9bde39149faf.png)

Choisissez vous-même de configurer un workflow. J'utiliserai Node.js pour ce projet.

Après avoir cliqué sur le bouton de configuration, un fichier `node.js.yml` sera créé automatiquement, et vous pourrez ajuster le code en fonction de vos objectifs.

![Image of GitHub workflow snippet for automated testing by Shahan](https://cdn.hashnode.com/res/hashnode/image/upload/v1737619475568/74da6d46-c105-42c8-8662-fc72e9410bda.png)

Je n'entrerai pas dans les détails sur la façon dont vous devriez modifier votre fichier `.yml`. Cela dépend des objectifs de votre projet et de vos préférences personnelles. De plus, c'est un sujet beaucoup plus vaste et comme cet article est déjà assez long, je l'expliquerai dans un futur article. Pour l'instant, tenez-vous-en à ces connaissances fondamentales.

Ce workflow de tests CI est idéal pour le développement d'applications modernes. Votre application reste stable tout en incorporant des fonctionnalités clés incluant les tests (ex: Mode Sombre), la construction et le déploiement d'applications directement au sein de votre dépôt GitHub. De cette façon, vous pouvez pousser votre code en toute confiance, sachant que votre code est toujours propre et prêt pour la production.

## Le rôle de la documentation dans le développement logiciel Agile 🚣

Si vous voulez que votre code soit de premier ordre, vous devez comprendre comment écrire une bonne documentation. Si vous pensez que la documentation consiste simplement à griffonner comment le code fonctionne, vous vous trompez. Il s'agit d'expliquer **pourquoi** il fonctionne, pas seulement comment. C'est là que la plupart des gens font fausse route.

### 1\. 🚡 Créez des **Docs utiles (Expliquez le Pourquoi, pas seulement le Comment)**

Lorsque vous écrivez de la documentation, vous ne vous contentez pas de jeter quelques instructions sur la façon d'utiliser le code. Vous dites à la personne suivante (ou même à vous-même dans le futur) pourquoi ce morceau de code existe en premier lieu. C'est la différence entre une bonne et une mauvaise documentation.

Les mauvaises docs laissent les gens perplexes. Elles sont trop vagues, trop simples et ne répondent pas aux grandes questions. Si votre documentation n'est pas claire, cela signifie probablement que votre pensée ne l'est pas non plus. Vous dites essentiellement : *« Je me fiche que vous compreniez, ça marche, utilisez-le. »* Ce n'est pas utile.

Une excellente documentation répond aux questions difficiles :

-   ✅ Pourquoi avez-vous choisi cette approche plutôt qu'une autre ?
    
-   ✅ Pourquoi cette fonction existe-t-elle ? Quel problème résout-elle ?
    
-   ✅ Pourquoi avez-vous écrit ce code de cette façon ?
    

Si vos docs ne font que régurgiter comment utiliser le code, vous n'êtes pas aussi utile que vous pourriez l'être. Commencez à réfléchir plus profondément et à expliquer le raisonnement derrière tout.

### 2\. ⏳ **Gardez les docs à jour (Des docs obsolètes sont pires que pas de docs du tout)**

La documentation obsolète est ce qu'il y a de pire. En fait, cela peut être pire que de ne pas avoir de docs du tout. Lorsque vous laissez une documentation qui n'est plus en phase avec le code, vous rendez un très mauvais service à votre futur "vous" — ou à quiconque devra s'en occuper ensuite.

Chaque fois que votre code change, votre documentation doit changer aussi. Elle doit refléter l'état actuel des choses. Ne trompez pas les futurs développeurs (ou vous-même) en laissant des informations obsolètes qui ne feront que les déconcerter et leur faire perdre du temps. Si quelque chose n'est plus pertinent, supprimez-le. Une documentation obsolète est l'équivalent d'un esprit encombré — elle vous freine.

Prenez l'habitude de vérifier et de mettre à jour votre documentation régulièrement. Dès qu'une ligne de code change, votre documentation doit changer aussi. Point final.

### 3\. 🚆 **Intégrez les commentaires (Les bons commentaires dans le code font partie de la documentation)**

Voici le topo — les commentaires dans votre code devraient **s'intégrer** à votre documentation. Les bons commentaires ne sont pas seulement une béquille pour les développeurs qui ne peuvent pas expliquer leur code ailleurs. Ils devraient améliorer vos docs, pas les remplacer.

Les commentaires sont des suppléments à votre documentation. Vous écrivez un code propre et compréhensible qui nécessite un minimum d'explications, mais quand quelque chose n'est pas limpide, ajoutez un commentaire. Rappelez-vous la règle pour les commentaires dans votre code : expliquez le **pourquoi**, pas le **comment**. C'est la même chose ici. Ne vous répétez pas. Laissez votre code parler. Les commentaires devraient compléter la vue d'ensemble de votre documentation, et non agir comme un pansement pour un code bâclé.

🪧 Un excellent code devrait être explicite. Corrigez le code, puis ajoutez des commentaires pour clarification si nécessaire. Gardez les commentaires propres, courts et directs.

Si vous voulez écrire un code propre, efficace et maintenable, la documentation est la clé. Arrêtez de considérer les docs comme une réflexion après coup ou quelque chose que vous faites pour remplir l'espace. C'est une extension de votre code — votre façon de communiquer clairement et efficacement. C'est votre feuille de route pour les futurs développeurs, et c'est le reflet de votre processus de pensée.

## Conclusion 🏁

Le clean code n'est pas un « plus » — c'est un impératif pour ceux qui aspirent à diriger. C'est une question de contrôle, d'efficacité et d'amélioration continue sur le long terme. Et en fin de compte, cela vous aidera à réussir dans le jeu du développement logiciel agile.

🪧 Si vous voulez vraiment maîtriser votre métier, écrivez du clean code, et laissez l'efficacité parler d'elle-même.

## Questions fréquemment posées sur le Clean Code 🧯

1.  **Qu'est-ce que le clean code ?** C'est un code qui ne vous donne pas envie de jeter votre ordinateur par la fenêtre.
    
2.  **Pourquoi le clean code est-il important en Agile ?** Parce que l'Agile est une question de rapidité et de changement, et on ne peut pas être rapide avec un désordre.
    
3.  **Que sont les code smells ?** Des signes indiquant que vous êtes sur le point de perdre le contrôle de votre base de code.
    
4.  **Comment puis-je améliorer mes commentaires ?** Ne commentez que ce qui est nécessaire, et assurez-vous que chaque commentaire apporte de la valeur, pas du bruit.
    

Merci d'avoir été avec moi. Vous pouvez visiter mon [compte Twitter][37] ou [mon site web][38] pour lire plus d'articles sur le clean code et le développement d'applications Agile. À la prochaine... continuez d'améliorer votre base de code.

Si vous voulez sérieusement maîtriser le clean code et faire passer votre carrière de programmation au niveau supérieur, alors mon livre est pour vous : [**Clean Code Zero to One**][39]. Ce livre est votre guide complet de zéro à un en clean code, du code désordonné au chef-d'œuvre. J'offre une réduction de 50 % en utilisant le code « earlybird » — seulement pour les 50 premiers exemplaires. De plus, il y a une garantie de remboursement de 30 jours — aucun risque, tout à gagner.

[1]: #heading-le-cout-du-mauvais-code
[2]: #heading-developpeur-propre-vs-developpeur-desordonne
[3]: #heading-lia-ne-peut-pas-vous-sauver-si-votre-code-est-un-desordre
[4]: #heading-12-patterns-de-conception-clean-code-pour-construire-des-applications-agile
[5]: #heading-utilisez-des-noms-qui-ont-du-sens
[6]: #heading-gardez-les-fonctions-focalisees-srp
[7]: #heading-utilisez-les-commentaires-avec-discernement
[8]: #heading-meilleures-pratiques-pour-ecrire-de-bons-commentaires
[9]: #heading-rendez-votre-code-lisible
[10]: #heading-testez-tout-ce-que-vous-ecrivez
[11]: #heading-utilisez-linjection-de-dependances
[12]: #heading-des-structures-de-projet-propres
[13]: #heading-soyez-coherent-avec-le-formatage
[14]: #heading-arretez-de-coder-des-valeurs-en-dur
[15]: #heading-gardez-les-fonctions-courtes
[16]: #heading-suivez-la-regle-du-boy-scout
[17]: #heading-suivez-le-principe-ouvertferme
[18]: #heading-resume-des-meilleures-pratiques-modernes-pour-vous-aider-a-ecrire-du-clean-code-a-summary
[19]: #heading-outils-automatises-pour-maintenir-un-code-propre
[20]: #heading-1-analyse-statique
[21]: #heading-2-formatage-de-code-automatise
[22]: #heading-3-tests-dintegration-continue-ci
[23]: #heading-4-pipelines-cicd
[24]: #heading-le-role-de-la-documentation-dans-le-developpement-logiciel-agile
[25]: #heading-conclusion
[26]: #heading-questions-frequemment-posees-sur-le-clean-code
[27]: http://cisq.org
[28]: https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/
[29]: https://vfunction.com/blog/how-to-manage-technical-debt
[30]: https://prettier.io/
[31]: https://eslint.org/
[32]: https://stackify.com/oop-concept-polymorphism/
[33]: https://codewithshahan.gumroad.com/l/cleancode-zero-to-one
[34]: https://eslint.org/
[35]: https://github.com/features/actions
[36]: https://www.jenkins.io/
[37]: https://x.com/shahancd
[38]: https://www.codewithshahan.com
[39]: https://codewithshahan.gumroad.com/l/cleancode-zero-to-one