---
title: Comment commenter votre code JavaScript
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-12-11T21:55:46.000Z'
originalURL: https://freecodecamp.org/news/comment-your-javascript-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Comment-Your-JS-Code-fCC.png
tags:
- name: best practices
  slug: best-practices
- name: code comments
  slug: code-comments
- name: JavaScript
  slug: javascript
seo_title: Comment commenter votre code JavaScript
seo_desc: "Writing comments in JavaScript is crucial for code readability, maintainability,\
  \ and developer collaboration. Comments serve as notes within the codebase, explaining\
  \ its functionality and logic, or providing context. \nIn this article, I will explain\
  \ ..."
---

Écrire des commentaires en JavaScript est crucial pour la lisibilité du code, la maintenabilité et la collaboration entre développeurs. Les commentaires servent de notes au sein de la base de code, expliquant sa fonctionnalité et sa logique, ou fournissant un contexte. 

Dans cet article, je vais expliquer l'importance de commenter votre code, les meilleures pratiques à suivre et des exemples montrant des commentaires efficaces en JavaScript.

## Pourquoi les commentaires sont importants en JavaScript

### Ils améliorent la lisibilité du code :

Les commentaires fournissent de la clarté au code, rendant plus facile pour les développeurs de comprendre le but et la fonctionnalité du code. Les commentaires agissent comme un guide, surtout lorsque vous devez revisiter un ancien code après une période de temps.

Considérez ce code non commenté :

```javascript
function calculateTotal(price, quantity) {
    return price * quantity;
}

let totalPrice = calculateTotal(25, 5);
console.log(totalPrice); // Sortie : 125
```

Il est assez difficile pour nous de comprendre ce que fait le code, n'est-ce pas ? Maintenant, ajoutons des commentaires pour plus de clarté :

```javascript
// Calcule le coût total en multipliant le prix par article avec la quantité
function calculateTotal(price, quantity) {
    return price * quantity;
}

// Exemple d'utilisation : Calcule le prix total pour 5 articles à 25 $ chacun en multipliant le prix par article (25 $) avec la quantité (5), et stocke le résultat dans la variable totalPrice.
let totalPrice = calculateTotal(25, 5);
console.log(totalPrice); // Sortie : 125
```

Avec les commentaires, il est assez compréhensible ce que chaque partie du code fait, et cela améliore également sa lisibilité.

### Ils facilitent la collaboration :

Dans un environnement d'équipe, les commentaires aident à la collaboration en permettant aux développeurs de comprendre le code des uns et des autres, rendant plus facile le travail ensemble sur des projets.

Imaginez travailler dans une équipe où différents développeurs gèrent diverses parties d'un projet. Des commentaires clairs aident à comprendre le code des uns et des autres. Voici un exemple :

```javascript
// Valide le format de l'adresse e-mail fournie en utilisant une expression régulière, qui vérifie la présence du symbole "@", du nom de domaine et du domaine de premier niveau (TLD) dans l'e-mail
function validateEmail(email) {
    // Motif d'expression régulière pour correspondre au format standard des e-mails
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
```

Dans un cadre collaboratif, un autre développeur peut rapidement comprendre le but de la fonction `validateEmail` grâce au commentaire, permettant un travail d'équipe plus fluide. Cela aurait été très difficile sans les commentaires indiquant ce que fait le bloc de code.

### Ils rendent la maintenance et le débogage plus faciles :

Un code bien commenté simplifie la maintenance et le débogage. Les commentaires peuvent mettre en évidence des problèmes potentiels, décrire la raison derrière des solutions spécifiques et aider à localiser les bugs.

Les commentaires aident au débogage et à la maintenance du code. Considérez le code commenté suivant :

```javascript
// Trouve le nombre maximum entre num1 et num2 en utilisant un opérateur ternaire pour la comparaison et retourne le nombre le plus grand
function findMax(num1, num2) {
    /* Utilisation de l'opérateur ternaire pour comparer num1 et num2
       et retourner le nombre le plus grand */
    return (num1 > num2) ? num1 : num2;
}
```

Si un bug survient ou si des modifications sont nécessaires, le commentaire clarifie la logique utilisée, aidant au débogage ou aux mises à jour rapides.

## Bonnes pratiques pour commenter en JavaScript

### Utilisez des commentaires descriptifs :

Expliquez le but des fonctions, des variables ou de la logique complexe en utilisant des commentaires descriptifs. Cela aide les autres développeurs, y compris vous-même dans le futur, à comprendre l'intention du code.

```javascript
// Calcule l'aire d'un cercle en utilisant le rayon fourni en multipliant le carré du rayon par la constante mathématique π (pi)
function calculateCircleArea(radius) {
    return Math.PI * radius * radius;
}
```

Des commentaires descriptifs comme celui-ci expliquent le but des fonctions ou des opérations, aidant à comprendre l'intention du code.

### Évitez de trop commenter :

Bien que les commentaires soient bénéfiques, un excès de commentaires peut encombrer le code. Visez un équilibre où les commentaires ajoutent de la valeur sans énoncer l'évident.

```javascript
// Variable pour stocker les données de l'utilisateur
let userData = fetchUserData(); // Récupère les données de l'utilisateur depuis le serveur
```

Dans ce cas, le commentaire se contente de répéter ce que le code exprime déjà clairement. Éviter de trop commenter maintient la clarté du code.

### Mettez à jour les commentaires régulièrement :

Au fur et à mesure que le code évolue, assurez-vous que les commentaires restent précis et alignés avec les changements de code. Des commentaires obsolètes peuvent entraîner de la confusion.

```javascript
// Fonction pour calculer l'aire d'un rectangle
function calculateRectangleArea(length, width) {
    return length * width;
    // Commentaire mis à jour : Aire calculée en multipliant la longueur et la largeur
}
```

S'assurer que les commentaires sont alignés avec la fonctionnalité ou la logique actuelle du code est vital pour une documentation précise.

### Commentez les sections complexes :

Lorsqu'on traite des algorithmes complexes ou des solutions non conventionnelles, des commentaires détaillés expliquant la logique peuvent être extrêmement utiles.

```javascript
// Effectue un calcul complexe sur les données fournies, impliquant plusieurs étapes incluant le prétraitement des données, le calcul basé sur les données prétraitées, et retourne le résultat final
function performComplexCalculation(data) {
    /* 
        Logique complexe impliquant plusieurs étapes :
        - Étape 1 : Prétraitement des données
        - Étape 2 : Calcul basé sur les données prétraitées
        - Étape 3 : Résultat final
    */
    // ... logique de calcul complexe
}
```

Pour des algorithmes complexes ou des processus en plusieurs étapes, des commentaires détaillés expliquant chaque étape peuvent grandement aider à la compréhension.

## Types de commentaires en JavaScript

### Commentaires sur une seule ligne :

En JavaScript, les commentaires sur une seule ligne commencent par `//`. Ils sont adaptés pour des explications brèves ou pour annoter des lignes spécifiques. Gardez à l'esprit que les deux barres obliques n'ont pas d'espaces entre elles.

Exemple :

```javascript
// Cette fonction calcule le carré d'un nombre
function square(number) {
    return number * number;
}

```

### Commentaires multi-lignes :

Les commentaires multi-lignes commencent par `/*` et se terminent par `*/`. Ils sont utiles pour commenter des blocs de code ou fournir des explications plus longues. Gardez à l'esprit que la barre oblique et l'astérisque (`*`) n'ont pas d'espaces entre eux.

Exemple :

```javascript
/*
    Ce bloc de code trouve le maximum de deux nombres
    et retourne le nombre le plus grand.
*/
function findMax(num1, num2) {
    // Logique pour trouver le maximum
    return (num1 > num2) ? num1 : num2;
}

```

### Commentaires JSDoc :

JSDoc est une convention pour ajouter des commentaires au code JavaScript qui permet la génération automatique de documentation. Il utilise une syntaxe spécifique pour décrire les fonctions, les paramètres, les valeurs de retour, etc.

Exemple :

```javascript
/**
 * Calcule l'aire d'un rectangle
 * @param {number} length - La longueur du rectangle
 * @param {number} width - La largeur du rectangle
 * @returns {number} - L'aire du rectangle
 */
function calculateArea(length, width) {
    return length * width;
}

```

## Pratiquez le commentaire de votre code 📝💏

Apprendre sans pratiquer est un processus incomplet. Voici donc [**un défi d'apprentissage du cours de certification freeCodeCamp**](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/comment-your-javascript-code) où vous apprendrez comment fonctionnent les commentaires en JavaScript, et comment vous pouvez les utiliser dans votre code. 

Dans ce défi, vous essaierez de comprendre comment fonctionnent les commentaires sur une seule ligne et les commentaires multi-lignes.

J'ai inclus la solution ci-dessous au cas où vous ne pourriez pas résoudre le défi vous-même.

Si vous souhaitez également regarder une vidéo sur ce sujet, vous pouvez la trouver ici :

%[https://www.youtube.com/watch?v=oqFs3bRQDSY]

## La solution au défi

Assurez-vous d'avoir essayé de résoudre ce défi par vous-même avant de vérifier ma solution.

Très bien, si vous êtes prêt... la voici :

```javascript
// Fahim

/*
Mon
Nom
Est
Fahim
*/
```

Le premier est le commentaire sur une seule ligne, et le second est le commentaire multi-lignes.

## Conclusion

Commenter le code JavaScript est une pratique essentielle dans le développement logiciel. Cela améliore la compréhension du code, aide à la collaboration et facilite la maintenance et le débogage. 

En suivant les meilleures pratiques et en utilisant divers types de commentaires, nous pouvons créer des bases de code plus faciles à comprendre, à maintenir et à développer.

J'espère que vous avez acquis des informations précieuses grâce à cet article. 

Si vous avez apprécié les procédures étape par étape, n'oubliez pas de me le faire savoir sur [Twitter/X](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Vous pouvez également me suivre sur [GitHub](https://github.com/FahimFBA) si vous êtes intéressé par l'open source. Assurez-vous de consulter [mon site web](https://fahimbinamin.com/) ([https://fahimbinamin.com/](https://fahimbinamin.com/)) également !

Si vous aimez regarder des vidéos sur la programmation et la technologie, vous pouvez consulter ma [chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1). Vous pouvez également consulter mes autres écrits sur [Dev.to](https://dev.to/fahimfba).

Je vous souhaite tout le meilleur pour votre parcours en programmation et en développement. 😊

Vous pouvez le faire ! Ne abandonnez jamais, jamais ! 💔