---
title: Comment écrire de meilleurs noms pour vos variables, fonctions et classes –
  Avec des exemples
subtitle: ''
author: Asfak Ahmed
co_authors: []
series: null
date: '2024-12-04T17:32:28.545Z'
originalURL: https://freecodecamp.org/news/how-to-write-better-variable-names
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733325693047/f3dff206-f0cf-47b0-9345-991b4d980d71.png
tags:
- name: JavaScript
  slug: javascript
- name: CSS
  slug: css
- name: variables
  slug: variables
- name: naming
  slug: naming
seo_title: Comment écrire de meilleurs noms pour vos variables, fonctions et classes
  – Avec des exemples
seo_desc: Naming is one of the most important and challenging parts of writing clean,
  maintainable, and scalable code. A well-thought-out variable name, for example,
  can act as self-documenting code, saving time and effort in understanding the logic.
  But poorl...
---

Le nommage est l'une des parties les plus importantes et les plus difficiles de l'écriture de code propre, maintenable et évolutif. Un nom de variable bien pensé, par exemple, peut agir comme un code auto-documenté, économisant du temps et des efforts pour comprendre la logique. Mais des noms mal choisis, en revanche, peuvent entraîner de la confusion et des bugs.

Cet article servira de guide complet sur la manière de trouver des noms significatifs pour les noms de classes, les variables et les fonctions avec des exemples et des bonnes pratiques.

## **Pourquoi le nommage est-il important ?**

* **Lisibilité** : Les bons noms rendent votre code intuitif et réduisent la courbe d'apprentissage pour les autres.
  
* **Maintenabilité** : Il est plus facile de refactoriser ou de déboguer un code bien nommé.
  
* **Collaboration** : Des noms clairs améliorent la communication et la productivité de l'équipe.
  
* **Évolutivité** : Des noms significatifs aident à garder les grands projets gérables.
  
## Différents styles de conventions de nommage

Différents styles de conventions de nommage sont cruciaux pour améliorer la lisibilité et la maintenabilité du code dans divers langages de programmation.

Des styles comme camelCase, PascalCase, snake_case et kebab-case sont adaptés à des contextes et pratiques spécifiques.

**camelCase** est largement utilisé pour les variables et les fonctions, tandis que **PascalCase** est préféré pour les classes. **snake_case** est un favori en Python pour sa clarté, et **kebab-case** domine le CSS pour le style des éléments HTML.

Chaque style assure la cohérence, rendant le code intuitif pour les équipes et les développeurs futurs. Voici un tableau récapitulatif rapide de quelques conventions de nommage populaires ainsi que leurs cas d'utilisation et exemples :

| **Style** | **Exemple** | **Utilisation courante** |
| --- | --- | --- |
| camelCase | `userName` | Variables, fonctions, propriétés d'objets |
| PascalCase | `UserName` | Classes, composants, constructeurs |
| kebab-case | `primary-button` | Classes CSS, IDs HTML, noms de fichiers |
| snake_case | `user_name` | Variables, noms de fonctions en Python |
| SCREAMING_SNAKE_CASE | `MAX_CONNECTIONS` | Constantes |
| dot.case | `config.file.path` | Configurations, clés |
| Train-Case | `Primary-Button` | Titres rarement utilisés |
| Hungarian Notation | `bIsActive` | Code hérité |
| UPPERCASE avec espaces | `USER ACCOUNT DETAILS` | Rare, surtout pour l'ancienne documentation |
| Flatcase | `username` | Minimaliste, noms de fichiers, identifiants |

### **Comment choisir le bon style**

1. **Spécifique au langage** : Suivez les conventions de votre langage de programmation ou framework. Par exemple :
   
   * JavaScript : `camelCase` pour les variables et fonctions, `PascalCase` pour les composants.
       
   * Python : `snake_case` pour les variables et fonctions.
       
   * CSS/HTML : `kebab-case` pour les noms de classes et les IDs.
       
2. **Normes d'équipe ou de projet** : La cohérence est essentielle. Utilisez le style convenu pour votre équipe/projet.
   
3. **Spécifique à l'usage** : Utilisez des styles de nommage qui représentent au mieux l'entité nommée (par exemple, les constantes en `SCREAMING_SNAKE_CASE`).
   

## **Directives générales de nommage**

Avant de plonger dans les conventions de nommage spécifiques pour les noms de classes, les variables et les fonctions, explorons quelques principes universels :

1. **Soyez descriptif et concis** : Les noms doivent transmettre le but ou le rôle de la variable/fonction/etc :
   
   ```javascript
   // Mauvais
   let x = 10;
   
   // Bon
   let maxUsersAllowed = 10;
   ```
   
2. **Évitez les abréviations cryptiques** qui pourraient être difficiles à comprendre pour d'autres développeurs (ou même pour vous-même dans le futur) :
   
   ```javascript
   // Mauvais
   let usrNm = "John";
   
   // Bon
   let userName = "John";
   ```
   
3. **Utilisez des conventions de nommage cohérentes** : Choisissez un style de nommage (camelCase, PascalCase, kebab-case, snake_case) et respectez-le tout au long de votre projet.
   
4. **Évitez les mots-clés réservés ou les noms confus** :
   
   ```javascript
   // Mauvais
   let let = 5;
   
   // Bon
   let variableName = 5;
   ```
   

D'accord, maintenant que nous avons couvert les bases, approfondissons certaines conventions de nommage utiles.

## **Comment créer de bons noms de classes**

Les noms de classes définissent le comportement visuel ou structurel des éléments dans votre application. Écrire des noms de classes clairs garantit que votre HTML et CSS sont faciles à comprendre et à maintenir.

### **1. Utilisez des noms descriptifs**

Les noms de classes doivent décrire le but de l'élément, et non son apparence.

```xml
<!-- Mauvais -->
<div class="red-button"></div>

<!-- Bon -->
<div class="primary-button"></div>
```

### **2. Suivez la méthodologie BEM (Block-Element-Modifier)**

BEM est une convention populaire pour écrire du CSS évolutif et maintenable. Elle sépare les composants en :

* **Block** : Représente le composant (par exemple, `card`).
   
* **Element** : Représente les éléments enfants du bloc (par exemple, `card__title`).
   
* **Modifier** : Représente les variations du bloc ou de l'élément (par exemple, `card__title--highlighted`).
   

**Exemple** :

```xml
<div class="card">
  <h1 class="card__title card__title--highlighted">Bienvenue</h1>
  <p class="card__description">Ceci est un composant de carte.</p>
</div>
```

### **3. Utilisez kebab-case**

Les noms de classes CSS sont traditionnellement écrits en kebab-case pour une meilleure lisibilité.

```xml
<!-- Mauvais -->
<div class="primaryButton"></div>

<!-- Bon -->
<div class="primary-button"></div>
```

## **Comment créer de bons noms de variables**

Les variables contiennent des données et doivent avoir des noms significatifs qui décrivent ce qu'elles représentent.

### **1. Utilisez des noms pour les variables**

Les variables sont généralement des noms car elles représentent des entités ou des données.

```javascript
// Mauvais
let a = "John";

// Bon
let userName = "John";
```

### **2. Utilisez des préfixes pour ajouter du contexte**

L'ajout de préfixes aide à clarifier le type ou le but d'une variable :

* **Booléen** : `is`, `has`, `can`
   
* **Nombres** : `max`, `min`, `total`
   
* **Tableaux** : Utilisez des formes plurielles (par exemple, `users`, `items`).
   

**Exemple** :

```javascript
let isUserLoggedIn = true;
const maxUploadLimit = 5; // Mo
const usersList = ["John", "Jane"];
```

### **3. Évitez les noms génériques**

Évitez les noms comme `data`, `value`, ou `item` sauf si ils sont nécessaires.

```javascript
// Mauvais
let data = 42;

// Bon
let userAge = 42;
```

## **Comment créer de bons noms de fonctions**

Les fonctions effectuent des actions, donc leurs noms doivent refléter l'opération ou le processus qu'elles exécutent.

### **1. Utilisez des verbes pour les fonctions**

Les fonctions sont orientées action, donc leurs noms doivent commencer par un verbe :

```javascript
// Mauvais
function userData() {
  // ...
}

// Bon
function fetchUserData() {
  // ...
}
```

### **2. Soyez spécifique sur la fonctionnalité**

Les noms de fonctions doivent indiquer ce qu'elles font.

```javascript
// Mauvais
function handle() {
  // ...
}

// Bon
function handleFormSubmit() {
  // ...
}
```

### **3. Utilisez des préfixes pour l'intention**

* Pour les gestionnaires d'événements : `handle`, `on`
   
* Pour les utilitaires : `calculate`, `convert`, `format`
   
* Pour les opérations de récupération : `fetch`, `get`, `load`
   
* Pour les setters et getters : `set`, `get`
   

**Exemple** :

```javascript
function handleButtonClick() {
  console.log("Bouton cliqué !");
}

function calculateDiscount(price, discountPercentage) {
  return price * (discountPercentage / 100);
}
```

## Comment savoir si un nom est bon pour une variable, une fonction ou une classe

Pour comprendre si un nom est bon pour une variable, une fonction ou une classe, il est important de l'évaluer en utilisant plusieurs principes clés. Voici un guide pour vous aider à décider si un nom est approprié et significatif dans votre contexte de programmation :

### 1. **Représente-t-il le but ?**

**Les noms orientés but** sont la caractéristique la plus importante d'un bon nommage. Un nom doit immédiatement vous dire ce que la variable, la fonction ou la classe représente ou fait sans avoir besoin de lire des commentaires ou une documentation supplémentaire.

**Comment évaluer :**

Demandez-vous : "Lorsque je lis ce nom, puis-je immédiatement comprendre son but ?"

**Exemple :**

* `userAge` est meilleur que `a` car `userAge` vous indique ce que la variable représente, alors que `a` est trop ambigu.
   

### 2. **Est-il suffisamment spécifique ?**

Le nom doit être **suffisamment spécifique** pour refléter le rôle exact de l'entité dans votre code. Des noms trop génériques comme `data` ou `temp` peuvent être confus car ils ne fournissent pas assez de contexte.

**Comment évaluer :**

Demandez : "Ce nom est-il spécifique à ce que cette variable, fonction ou classe représente dans mon application ?"

**Exemple :**

* `calculateTaxAmount()` est meilleur que `calculate()` car il est clair ce que la fonction calcule.
   

### 3. **Suiv-il une convention de nommage cohérente ?**

**La cohérence** dans les conventions de nommage est vitale. Lorsque tous les membres de l'équipe suivent les mêmes conventions, le code est plus facile à comprendre et à naviguer.

**Comment évaluer :**

Demandez : "Ce nom est-il cohérent avec les conventions de nommage utilisées dans le reste du projet ?" Suivez les directives du projet telles que :

* `camelCase` pour les variables et fonctions (par exemple, `userAge`)
   
* `PascalCase` pour les classes (par exemple, `UserProfile`)
   
* `UPPERCASE_SNAKE_CASE` pour les constantes (par exemple, `MAX_USERS`)
   

**Exemple :**

* Si votre équipe suit `camelCase`, `userData` est meilleur que `UserData`.
   

### 4. **Évite-t-il l'ambiguïté ?**

Un bon nom **élimine l'ambiguïté**. Il ne doit pas être ouvert à plusieurs interprétations. S'il peut signifier différentes choses dans différents contextes, cela entraînera de la confusion.

**Comment évaluer :**

Demandez : "Quelqu'un qui ne connaît pas la base de code pourrait-il mal interpréter ce à quoi ce nom fait référence ?"

**Exemple :**

* Au lieu de nommer un booléen `isValid`, utilisez `isUserLoggedIn` ou `isEmailVerified` pour clarifier ce qui est vérifié.
   

### 5. **Est-il facile à lire et à prononcer ?**

Bien que ce ne soit pas strictement nécessaire, **la facilité de lecture et de prononciation** peut améliorer la lisibilité et la maintenabilité globale de votre code.

**Comment évaluer :**

Demandez : "Ce nom est-il facile à lire à voix haute, et puis-je le comprendre d'un coup d'œil ?"

Évitez les noms longs, et utilisez des abréviations courantes uniquement lorsqu'elles sont largement acceptées.

**Exemple :**

* `maxRetries` est meilleur que `maximumNumberOfAttemptsToReconnect`.
   

### 6. **Évite-t-il la redondance ?**

**Évitez la redondance** dans les noms. Ne répétez pas d'informations qui sont déjà impliquées ou décrites par le contexte.

**Comment évaluer :**

Demandez : "Est-ce que je répète des informations qui sont déjà claires d'après le contexte environnant ?"

**Exemple :**

* Si vous avez une classe nommée `User`, nommer une méthode `userGetData()` est redondant. Utilisez plutôt `getData()`.
   

### 7. **Est-il auto-documenté ?**

Les meilleurs noms **se documentent eux-mêmes**. De bons noms réduisent le besoin de commentaires ou d'explications supplémentaires.

**Comment évaluer :**

Demandez : "Ce nom décrit-il pleinement la variable, la fonction ou la classe sans nécessiter de commentaire pour expliquer ce qu'elle fait ?"

**Exemple :**

* `calculateTotalPrice` est auto-explicatif, donc il n'y a pas besoin de commentaire supplémentaire comme "Cette fonction calcule le prix total après réduction."
   

### 8. **Est-il contextuel et pertinent pour le domaine ?**

Le nom doit s'inscrire dans le contexte de votre projet et de son domaine. Par exemple, les conventions de nommage pour une application web peuvent différer de celles pour une application mobile ou un modèle d'apprentissage automatique.

**Comment évaluer :**

Demandez : "Ce nom est-il aligné avec le domaine et le contexte de mon projet ?"

Si vous travaillez dans un domaine spécifique (par exemple, finance, santé, gaming), utilisez des termes spécifiques au domaine qui sont facilement reconnaissables.

**Exemple :**

* Dans une application de gaming, `healthPoints` est plus approprié que `hp`, car il reflète sa signification.
   

### 9. **Est-il à l'épreuve du futur ?**

Pensez à la manière dont votre code évoluera. Les noms doivent être suffisamment flexibles pour s'adapter aux changements futurs sans nécessiter de refactorisation.

**Comment évaluer :**

Demandez : "Ce nom aura-t-il encore du sens si la fonctionnalité change ou si le projet grandit ?"

**Exemple :**

* `userInfo` pourrait devenir obsolète si la structure de données change. Il est préférable d'utiliser `userProfile` si vous prévoyez d'ajouter plus de champs.
   

### 10. **Évite-t-il les nombres magiques et les valeurs codées en dur ?**

**Les nombres magiques** (nombres avec une signification peu claire) doivent être évités au profit de constantes nommées.

**Comment évaluer :**

Demandez : "Ce nom représente-t-il une constante significative, ou est-ce simplement un nombre brut ?"

**Exemple :**

* Au lieu d'utiliser `1000`, utilisez une constante comme `MAX_FILE_SIZE` pour expliquer la signification derrière le nombre.
   

## **Exemples pratiques**

### **Exemple CSS**

L'exemple CSS suivant démontre comment appliquer les conventions de nommage **BEM (Block-Element-Modifier)** pour maintenir une hiérarchie de classes structurée et évolutive dans votre feuille de style :

```xml
<!-- HTML -->
<div class="navbar">
  <ul class="navbar__list">
    <li class="navbar__item navbar__item--active">Accueil</li>
    <li class="navbar__item">À propos</li>
    <li class="navbar__item">Contact</li>
  </ul>
</div>
```

```css
/* CSS */
.navbar {
  background-color: #333;
  padding: 10px;
}

.navbar__list {
  list-style: none;
}

.navbar__item {
  display: inline-block;
  padding: 10px;
}

.navbar__item--active {
  color: orange;
}
```

Voici ce qui se passe dans ce code :

* **Nommage BEM** : `navbar` est le **Block**, représentant le composant principal de navigation.
   
* `navbar__list` est l'**Element**, un enfant du bloc, représentant la liste des éléments de navigation.
   
* `navbar__item` est un autre **Element** représentant les éléments individuels de la liste.
   
* `navbar__item--active` est un **Modifier**, utilisé pour mettre en évidence l'élément de menu actif.  
   Cette approche facilite la compréhension des relations et des rôles au sein du HTML et du CSS, soutenant des styles modulaires et réutilisables.
   

### **Exemple JavaScript**

Cet exemple JavaScript montre comment utiliser des conventions de nommage significatives et cohérentes pour les variables et les fonctions afin de rendre le code auto-explicatif :

```javascript
// Variables
let isUserLoggedIn = false;
const maxAllowedItems = 10;

// Fonctions
function fetchUserDetails(userId) {
  // Récupérer les données de l'utilisateur depuis l'API
}

function calculateTotalPrice(cartItems) {
  return cartItems.reduce((total, item) => total + item.price, 0);
}
```

Voici ce qui se passe dans le code :

* **Variables** :
   
   * `isUserLoggedIn` : Une variable booléenne nommée pour indiquer clairement son but. Le préfixe `is` aide à l'identifier comme un booléen.
       
   * `maxAllowedItems` : Une constante avec un préfixe `max` en majuscule montre qu'il s'agit d'une limite, rendant son intention claire.
       
* **Fonctions** :
   
   * `fetchUserDetails(userId)` : Le nom reflète le but de la fonction, c'est-à-dire récupérer les détails de l'utilisateur. Le paramètre `userId` est descriptif et évite l'ambiguïté.
       
   * `calculateTotalPrice(cartItems)` : Le nom de la fonction indique explicitement l'action effectuée. Le paramètre `cartItems` est contextuellement pertinent pour le domaine du e-commerce.
       

**Pourquoi c'est bien** : Ces conventions garantissent que le code est lisible et intuitif, réduisant la charge cognitive pour les autres développeurs travaillant sur le même projet.

## **Conclusion**

Le nommage significatif est à la fois une convention importante et un art qui impacte significativement la lisibilité et la maintenabilité de votre code.

Essayez de suivre ces principes de base :

* Utilisez des noms descriptifs et concis.
   
* Respectez des conventions cohérentes comme BEM pour les noms de classes et camelCase pour les variables et les fonctions.
   
* Utilisez des préfixes pour ajouter du contexte et de la clarté.
   

Ces conseils, ainsi que les autres astuces que nous avons discutées ici, rendront votre code agréable à travailler, que vous le revisitiez des mois plus tard ou que vous collaboriez avec une équipe. Commencez à appliquer ces conseils dès aujourd'hui, et regardez la qualité de votre code s'envoler.