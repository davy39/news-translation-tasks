---
title: Comment créer un gestionnaire de dépenses avec HTML, CSS et JavaScript
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-09-11T17:25:59.380Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-expense-tracker-with-html-css-and-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726055511234/dcaa759f-58f9-477d-92da-c8b98b71d310.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
- name: HTML5
  slug: html5
- name: CSS
  slug: css
seo_title: Comment créer un gestionnaire de dépenses avec HTML, CSS et JavaScript
seo_desc: 'Building projects is a great way to practice and improve your web development
  skills. And that''s what we''ll do in this in-depth tutorial: build a practical
  project using HTML, CSS, and JavaScript.

  If you often find yourself wondering where all your m...'
---

Créer des projets est un excellent moyen de pratiquer et d'améliorer vos compétences en développement web. Et c'est précisément ce que nous allons faire dans ce tutoriel approfondi : construire un projet pratique en utilisant HTML, CSS et JavaScript.

Si vous vous demandez souvent où est passé tout votre argent ou comment vous avez réussi à dépenser autant, alors ce projet est pour vous. J'ai créé un gestionnaire de dépenses simple pour m'aider à gérer mes propres finances, et j'ai décidé de partager un tutoriel étape par étape avec la communauté des développeurs.

Dans ce tutoriel, nous allons parcourir le processus de création d'un gestionnaire de dépenses de base à partir de zéro. Que vous soyez novice en développement web ou que vous cherchiez à perfectionner vos compétences, ce projet vous apportera une expérience pratique en HTML, CSS et JavaScript.

À la fin, vous disposerez d'un outil entièrement fonctionnel pour suivre vos revenus, gérer vos dépenses et maintenir une vue d'ensemble claire de vos finances au sein d'une interface élégante et conviviale.

Nous commencerons par mettre en place la structure du gestionnaire, puis nous passerons au stylisage pour le rendre visuellement attrayant, et enfin, nous implémenterons les fonctionnalités qui lui donneront vie.

### Table des matières

1. [Configurer la structure HTML](#heading-configurer-la-structure-html)
2. [Styliser le gestionnaire de dépenses avec CSS](#heading-styliser-le-gestionnaire-de-depenses-avec-css)
3. [Implémenter les fonctionnalités avec JavaScript](#heading-implementer-les-fonctionnalites-avec-javascript)
4. [Améliorer l'expérience utilisateur](#heading-ameliorer-lexperience-utilisateur)
5. [Tests et débogage](#heading-tests-et-debogage)
6. [Conclusion](#heading-conclusion)

### Prérequis

Pour tirer le meilleur parti de ce tutoriel, il sera bénéfique d'avoir une compréhension de base de HTML, CSS et JavaScript. Une familiarité avec la création de pages web simples et la manipulation de base du DOM en JavaScript vous aidera à suivre plus facilement.

Mais si vous êtes nouveau dans ces technologies, ne vous inquiétez pas – je vous guiderai à chaque étape avec des explications détaillées.

## Configurer la structure HTML

Tout d'abord, nous devons mettre en place la structure HTML de base. Elle servira de fondation à tout ce que nous allons construire. Ne vous inquiétez pas si vous débutez en HTML, je vous guiderai pas à pas.

### 1\. Créer un modèle HTML de base

Commencez par créer un nouveau fichier et nommez-le `index.html`. Ce fichier contiendra la structure de notre gestionnaire de dépenses. Chaque fichier HTML commence par un modèle de base, qui comprend la déclaration `<!DOCTYPE html>`, la balise `<html>`, ainsi que les sections head et body.

Voici à quoi devrait ressembler votre modèle HTML initial :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestionnaire de dépenses</title>
</head>
<body>
    
</body>
</html>
```

### 2\. Ajouter un conteneur

À l'intérieur de la balise `<body>`, commençons par ajouter un élément `div` avec une classe `container`. Ce conteneur contiendra tout le contenu de notre gestionnaire, comme le titre, les champs de saisie et le résumé. Nous utilisons un conteneur pour tout centrer sur la page et nous assurer que notre mise en page est soignée.

Voici comment faire :

```html
<body>
    <div class="container">
        <!-- Tout le contenu ira ici -->
    </div>
</body>
```

### 3\. Ajouter le titre du gestionnaire de dépenses

Maintenant, ajoutons un titre à notre gestionnaire. Nous utiliserons la balise `<h1>` pour cela, qui est généralement utilisée pour le titre principal d'une page web.

Ajoutez le code suivant à l'intérieur de la div `container` :

```html
<h1>Gestionnaire de dépenses</h1>
```

Ce titre s'affichera bien en vue en haut de votre page, permettant aux utilisateurs de savoir de quoi traite l'application.

### 4\. Mise en place des sections pour les revenus et les dépenses

Ensuite, nous allons ajouter des sections pour les revenus et les dépenses. Ces sections incluront des champs de saisie où les utilisateurs pourront entrer les détails de leurs revenus et dépenses.

Commencez par ajouter deux éléments `div`, chacun avec une classe `section`. Une section sera pour les revenus et l'autre pour les dépenses. Voici le code :

```html
<div class="section">
    <h2>Revenus</h2>
    <!-- Les champs de saisie des revenus iront ici -->
</div>

<div class="section">
    <h2>Dépenses</h2>
    <!-- Les champs de saisie des dépenses iront ici -->
</div>
```

Les balises `<h2>` à l'intérieur de ces sections servent de sous-titres pour identifier chaque section. Nous ajouterons les champs de saisie à l'étape suivante.

### 5\. Ajouter des champs de saisie

Ajoutons maintenant les champs de saisie pour la section des revenus. Les utilisateurs devront saisir une description (par exemple, "Salaire") et un montant. Chaque champ de saisie sera enveloppé dans une `div` avec une classe `input-group` pour faciliter le stylisage ultérieur.

Bien que cet exemple utilise le Naira nigérian (₦) comme devise, vous pouvez facilement l'adapter à la devise de votre choix. Il suffit de remplacer le symbole monétaire dans l'espace réservé (placeholder) ou les étiquettes selon vos besoins.

Voici comment ajouter les champs de saisie :

```html
<div class="input-group">
    <label for="income-description">Description</label>
    <input type="text" id="income-description" placeholder="ex: Salaire">
</div>
<div class="input-group">
    <label for="income-amount">Montant (₦)</label>
    <input type="number" id="income-amount" placeholder="ex: 100000">
</div>
```

Faites de même pour la section des dépenses, mais cette fois, nous ajouterons également une liste déroulante pour la catégorie de la dépense :

```html
<div class="input-group">
    <label for="expense-description">Description</label>
    <input type="text" id="expense-description" placeholder="ex: Loyer">
</div>
<div class="input-group">
    <label for="expense-category">Catégorie</label>
    <select id="expense-category">
        <option value="Logement">Logement</option>
        <option value="Alimentation">Alimentation</option>
        <option value="Transport">Transport</option>
        <option value="Divertissement">Divertissement</option>
        <option value="Autres">Autres</option>
    </select>
</div>
<div class="input-group">
    <label for="expense-amount">Montant (₦)</label>
    <input type="number" id="expense-amount" placeholder="ex: 50000">
</div>
```

### 6\. Ajouter un bouton à chaque section

Enfin, nous avons besoin d'un bouton dans chaque section sur lequel les utilisateurs cliqueront pour ajouter leur revenu ou leur dépense au gestionnaire. Placez un élément `button` à l'intérieur de chaque section comme ceci :

```html
<div class="button-group">
    <button onclick="addIncome()">Ajouter Revenu</button>
</div>
```

Et pour la section des dépenses :

```html
<div class="button-group">
    <button onclick="addExpense()">Ajouter Dépense</button>
</div>
```

### 7\. Affichage de l'historique des transactions

Après les sections de revenus et de dépenses, nous avons besoin d'un endroit pour afficher l'historique des transactions. Nous utiliserons un tableau pour cela, car c'est une façon propre et organisée de présenter des données.

Ajoutez le code suivant après la section des dépenses :

```html
<div class="table-container">
    <h2>Historique des transactions</h2>
    <table>
        <thead>
            <tr>
                <th>Description</th>
                <th>Catégorie</th>
                <th>Montant (₦)</th>
                <th>Type</th>
                <th>Action</th> <!-- Colonne pour le bouton supprimer -->
            </tr>
        </thead>
        <tbody id="transaction-history">
            <!-- Les transactions apparaîtront ici -->
        </tbody>
    </table>
</div>
```

### 8\. Ajouter une section de résumé

Au bas du conteneur, ajoutons une section de résumé qui affiche le revenu total, les dépenses totales et le solde.

Voici le code pour le résumé :

```html
<div class="summary">
    <h2>Résumé du budget</h2>
    <p>Revenu total : ₦<span id="total-income">0</span></p>
    <p>Dépenses totales : ₦<span id="total-expenses">0</span></p>
    <p>Solde : ₦<span id="balance">0</span></p>
</div>
```

### 9\. Ajouter un bouton "Tout effacer"

Enfin, incluez un bouton qui permettra aux utilisateurs d'effacer toutes les données en un clic. C'est particulièrement utile s'ils souhaitent tout réinitialiser.

Voici comment ajouter le bouton d'effacement :

```html
<div class="clear-button-group">
    <button onclick="clearAll()">Tout effacer</button>
</div>
```

### 10\. Assembler le tout

Lorsque vous assemblez toutes les pièces, votre structure HTML devrait ressembler à ceci :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planificateur de budget créatif</title>
</head>
<body>
    <div class="container">
        <h1>Gestionnaire de dépenses</h1>
        <div class="section">
            <h2>Revenus</h2>
            <div class="input-group">
                <label for="income-description">Description</label>
                <input type="text" id="income-description" placeholder="ex: Salaire">
            </div>
            <div class="input-group">
                <label for="income-amount">Montant (₦)</label>
                <input type="number" id="income-amount" placeholder="ex: 100000">
            </div>
            <div class="button-group">
                <button onclick="addIncome()">Ajouter Revenu</button>
            </div>
        </div>
        <div class="section">
            <h2>Dépenses</h2>
            <div class="input-group">
                <label for="expense-description">Description</label>
                <input type="text" id="expense-description" placeholder="ex: Loyer">
            </div>
            <div class="input-group">
                <label for="expense-category">Catégorie</label>
                <select id="expense-category">
                    <option value="Logement">Logement</option>
                    <option value="Alimentation">Alimentation</option>
                    <option value="Transport">Transport</option>
                    <option value="Divertissement">Divertissement</option>
                    <option value="Autres">Autres</option>
                </select>
            </div>
            <div class="input-group">
                <label for="expense-amount">Montant (₦)</label>
                <input type="number" id="expense-amount" placeholder="ex: 50000">
            </div>
            <div class="button-group">
                <button onclick="addExpense()">Ajouter Dépense</button>
            </div>
        </div>
        <div class="table-container">
            <h2>Historique des transactions</h2>
            <table>
                <thead>
                    <tr>
                        <th>Description</th>
                        <th>Catégorie</th>
                        <th>Montant (₦)</th>
                        <th>Type</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody id="transaction-history">
                    <!-- Les transactions apparaîtront ici -->
                </tbody>
            </table>
        </div>
        <div class="summary">
            <h2>Résumé du budget</h2>
            <p>Revenu total : ₦<span id="total-income">0</span></p>
            <p>Dépenses totales : ₦<span id="total-expenses">0</span></p>
            <p>Solde : ₦<span id="balance">0</span></p>
        </div>
        <div class="clear-button-group">
            <button onclick="clearAll()">Tout effacer</button>
        </div>
    </div>
</body>
</html>
```

%[https://codepen.io/joanayebola/pen/NWZEvLy] 

## Styliser le gestionnaire de dépenses avec CSS

Maintenant que notre structure HTML est en place, il est temps de rendre notre gestionnaire de dépenses visuellement attrayant en ajoutant du CSS. Nous commencerons par un stylisage de base, puis nous passerons à des détails plus spécifiques pour nous assurer que tout est propre et convivial.

### 1\. Configurer le fichier CSS

Tout d'abord, créez un nouveau fichier nommé `styles.css` dans le même répertoire que votre fichier `index.html`. Liez ce fichier CSS à votre HTML en ajoutant la ligne suivante à l'intérieur de la section `<head>` de `index.html` :

```html
<link rel="stylesheet" href="styles.css">
```

Cette ligne indique à votre fichier HTML d'utiliser les styles définis dans `styles.css`.

### 2\. Styliser le Body

Commençons par ajouter quelques styles de base au `<body>` pour définir une belle couleur d'arrière-plan, une police et une mise en page. Ouvrez `styles.css` et ajoutez le code suivant :

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
```

* **font-family :** Nous utilisons une police simple et propre.
* **background-color :** Un arrière-plan gris clair donnera à notre gestionnaire un aspect doux.
* **display, justify-content, align-items, height :** Ces propriétés centrent le contenu verticalement et horizontalement.

### 3\. Styliser le Conteneur

Ensuite, nous allons styliser le `.container` pour lui donner un aspect ordonné :

```css
.container {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    width: 100%;
}
```

* **background-color :** Le blanc fait ressortir le contenu sur l'arrière-plan gris.
* **padding :** Ajoute de l'espace à l'intérieur du conteneur pour que le contenu ne touche pas les bords.
* **border-radius :** Arrondit les coins pour un look moderne.
* **box-shadow :** Ajoute une ombre subtile pour décoller légèrement le conteneur de la page.
* **max-width et width :** Garantit que le conteneur est réactif et ne dépasse pas une certaine largeur.

### 4\. Styliser les Titres

Stylisons les titres pour les rendre plus distincts visuellement :

```css
h1, h2 {
    color: #333;
    text-align: center;
}

h1 {
    margin-bottom: 20px;
}

h2 {
    margin-bottom: 15px;
}
```

* **color :** Un gris foncé pour le texte le gardera lisible.
* **text-align :** Centre les titres pour créer une mise en page équilibrée.
* **margin-bottom :** Ajoute de l'espace sous les titres.

### 5\. Styliser les groupes de saisie (Input Groups)

Maintenant, stylisons les champs de saisie et les étiquettes au sein de la classe `.input-group` :

```css
.input-group {
    margin-bottom: 15px;
}

.input-group label {
    display: block;
    margin-bottom: 5px;
    color: #555;
}

.input-group input,
.input-group select {
    width: calc(100% - 10px);
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-sizing: border-box;
    font-size: 16px;
}
```

* **margin-bottom :** Ajoute de l'espace entre les groupes de saisie.
* **display: block :** Garantit que les étiquettes occupent toute la largeur.
* **width :** Rend les champs de saisie et les éléments select réactifs.
* **padding, border, border-radius :** Crée un aspect plus poli pour les entrées.
* **box-sizing :** Garantit que le rembourrage est inclus dans la largeur totale de l'élément.

### 6\. Styliser les Boutons

Donnons aux boutons un aspect plus interactif et attrayant :

```css
.button-group button,
.clear-button-group button {
    background-color: #FF69B4;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

.button-group button:hover,
.clear-button-group button:hover {
    background-color: #FF1493;
}
```

* **background-color :** Un rose vif pour que les boutons se démarquent.
* **color :** Texte blanc pour le contraste.
* **border, padding, border-radius :** Pas de bordure, un rembourrage généreux et des coins arrondis.
* **cursor :** Transforme le curseur en main au survol, indiquant que le bouton est cliquable.
* **hover :** Assombrit la couleur du bouton au survol pour un effet d'interaction subtil.

### 7\. Styliser le tableau d'historique des transactions

Nous allons également styliser le tableau pour qu'il soit facile à lire et cohérent avec le reste :

```css
.table-container {
    margin-top: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

th, td {
    text-align: left;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #FF69B4;
    color: white;
}

td {
    color: #333;
}

td button {
    background-color: #FF1493;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 3px;
    cursor: pointer;
}

td button:hover {
    background-color: #C71585;
}
```

* **border-collapse :** Garantit qu'il n'y a pas d'espace entre les bordures du tableau.
* **padding, border-bottom :** Ajoute de l'espace dans les cellules et une bordure sous chaque ligne pour la séparation.
* **background-color for th :** Assorti aux boutons pour un design cohérent.
* **td button :** Ajoute un bouton de suppression stylisé de manière similaire aux autres boutons.

### 8\. Styliser la section de résumé

Enfin, stylisons la section de résumé pour qu'elle se démarque :

```css
.summary {
    background-color: #FFB3FF;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    color: #333;
}

.summary p {
    margin: 10px 0;
    font-size: 18px;
}

.summary span {
    font-weight: bold;
}
```

* **background-color :** Un fond rose doux aide à distinguer le résumé du reste.
* **padding, border-radius :** Ajoute de l'espacement et des coins arrondis.
* **text-align :** Centre le texte dans le résumé.
* **font-size, font-weight :** Augmente la taille et l'épaisseur de la police pour mettre en évidence les totaux et le solde.

### 9\. Assembler le tout

Voici à quoi devrait ressembler votre fichier `styles.css` complet :

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    width: 100%;
}

h1, h2 {
    color: #333;
    text-align: center;
}

h1 {
    margin-bottom: 20px;
}

h2 {
    margin-bottom: 15px;
}

.input-group {
    margin-bottom: 15px;
}

.input-group label {
    display: block;
    margin-bottom: 5px;
    color: #555;
}

.input-group input,
.input-group select {
    width: calc(100% - 10px);
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-sizing: border-box;
    font-size: 16px;
}

.button-group button,
.clear-button-group button {
    background-color: #FF69B4;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

.button-group button:hover,
.clear-button-group button:hover {
    background-color: #FF1493;
}

.table-container {
    margin-top: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

th, td {
    text-align: left;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #FF69B4;
    color: white;
}

td {
    color: #333;
}

td button {
    background-color: #FF1493;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 3px;
    cursor: pointer;
}

td button:hover {
    background-color: #C71585;
}

.summary {
    background-color: #FFB3FF;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    color: #333;
}

.summary p {
    margin: 10px 0;
    font-size: 18px;
}

.summary span {
    font-weight: bold;
}
```

Avec ce CSS, votre gestionnaire devrait maintenant avoir un look propre, moderne et facile à utiliser.

%[https://codepen.io/joanayebola/pen/rNEQzqb] 

## Implémenter les fonctionnalités avec JavaScript

Maintenant que nous avons la structure HTML et le style CSS, il est temps de donner vie à notre gestionnaire de dépenses en utilisant JavaScript. Nous allons ajouter des fonctionnalités pour que les utilisateurs puissent ajouter des dépenses, consulter un résumé et supprimer des éléments de la liste.

### 1\. Configurer le fichier JavaScript

Créez un nouveau fichier nommé `script.js` dans le même répertoire que votre fichier `index.html`. Liez ce fichier à votre HTML en ajoutant la ligne suivante juste avant la balise de fermeture `</body>` dans `index.html` :

```html
<script src="script.js"></script>
```

### 2\. Définition des variables

Commençons par définir des variables pour référencer les éléments clés de notre HTML. Ouvrez `script.js` et ajoutez le code suivant :

```javascript
const expenseForm = document.getElementById('expense-form');
const expenseInput = document.getElementById('expense-input');
const amountInput = document.getElementById('amount-input');
const categoryInput = document.getElementById('category-input');
const transactionList = document.getElementById('transaction-list');
const totalExpense = document.getElementById('total-expense');
const totalIncome = document.getElementById('total-income');
const balance = document.getElementById('balance');
```

Voici le rôle de chaque variable :

* **expenseForm :** Référence le formulaire où les utilisateurs saisissent de nouvelles dépenses.
* **expenseInput :** Référence le champ de saisie pour la description de la dépense.
* **amountInput :** Référence le champ pour le montant.
* **categoryInput :** Référence la liste déroulante des catégories.
* **transactionList :** Référence le tableau où nous afficherons les transactions.
* **totalExpense, totalIncome, balance :** Référencent les éléments affichant le résumé.

### 3\. Ajouter une dépense

Créons une fonction qui gère l'ajout d'une nouvelle dépense lors de la soumission du formulaire :

```javascript
expenseForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const description = expenseInput.value.trim();
    const amount = parseFloat(amountInput.value.trim());
    const category = categoryInput.value;

    if (description === '' || isNaN(amount) || amount <= 0) {
        alert('Veuillez entrer une description et un montant valides.');
        return;
    }

    addTransaction(description, amount, category);
    updateSummary();
    clearInputs();
});

function addTransaction(description, amount, category) {
    const transactionRow = document.createElement('tr');

    transactionRow.innerHTML = `
        <td>${description}</td>
        <td>${category}</td>
        <td>${amount.toFixed(2)}</td>
        <td><button class="delete-btn">Supprimer</button></td>
    `;

    transactionList.appendChild(transactionRow);

    transactionRow.querySelector('.delete-btn').addEventListener('click', function() {
        transactionRow.remove();
        updateSummary();
    });
}
```

Explications :

* `event.preventDefault()` : Empêche le rechargement de la page lors de la soumission.
* `addTransaction` : Ajoute une nouvelle ligne de transaction au tableau.
* `updateSummary` : Met à jour les totaux et le solde.
* `clearInputs` : Efface les champs du formulaire après l'ajout.
* **Bouton supprimer :** Permet aux utilisateurs de retirer une transaction de la liste.

### 4\. Mise à jour du résumé

Pour suivre les totaux, nous allons créer une fonction `updateSummary` :

```javascript
function updateSummary() {
    let totalExpenses = 0;
    let totalIncomes = 0;

    const transactions = transactionList.querySelectorAll('tr');

    transactions.forEach(function(transaction) {
        const amount = parseFloat(transaction.children[2].textContent);
        const category = transaction.children[1].textContent;

        if (category === 'Income') {
            totalIncomes += amount;
        } else {
            totalExpenses += amount;
        }
    });

    totalExpense.textContent = totalExpenses.toFixed(2);
    totalIncome.textContent = totalIncomes.toFixed(2);
    balance.textContent = (totalIncomes - totalExpenses).toFixed(2);
}
```

### 5\. Effacer les champs de saisie

```javascript
function clearInputs() {
    expenseInput.value = '';
    amountInput.value = '';
    categoryInput.value = 'Expense';
}
```

### 6\. Assembler le tout

(Le script complet regroupe toutes les fonctions précédentes).

### 7\. Tester le gestionnaire de dépenses

Ouvrez votre fichier `index.html` dans un navigateur. Essayez d'ajouter des dépenses et des revenus pour voir comment ils apparaissent. Félicitations ! Vous avez implémenté un gestionnaire de dépenses fonctionnel.

## Améliorer l'expérience utilisateur

Maintenant que la fonctionnalité de base est opérationnelle, améliorons l'expérience utilisateur avec quelques détails réfléchis.

### 1\. Ajouter un retour en temps réel

Ajoutons une notification pour confirmer qu'une transaction a été ajoutée. Dans votre HTML :

```html
<div id="notification" class="hidden"></div>
```

Dans votre CSS :

```css
#notification {
  background-color: #28a745;
  color: white;
  padding: 10px;
  margin-top: 10px;
  text-align: center;
  border-radius: 5px;
}

.hidden {
  display: none;
}
```

Dans JavaScript :

```javascript
function showNotification(message) {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.classList.remove('hidden');
    
    setTimeout(function() {
        notification.classList.add('hidden');
    }, 2000); // La notification disparaîtra après 2 secondes
}
```

### 2\. Affichage d'un indicateur de solde

Changeons la couleur du solde s'il est positif ou négatif. En CSS :

```css
.positive {
  color: #28a745; /* Vert pour un solde positif */
}

.negative {
  color: #dc3545; /* Rouge pour un solde négatif */
}
```

Et mettez à jour la logique dans `updateSummary` pour appliquer ces classes.

### 3\. Préserver les données avec le Local Storage

L'utilisation du local storage du navigateur permet de conserver les transactions même après le rafraîchissement de la page. (Utilisez `localStorage.setItem` et `localStorage.getItem` comme décrit dans les extraits de code précédents).

### 4\. Améliorer l'UX du formulaire

Donnez automatiquement le focus au champ de description au chargement de la page :

```javascript
window.addEventListener('load', function() {
    expenseInput.focus();
});
```

### 5\. Utiliser des icônes pour une meilleure interface

Remplacez le texte "Supprimer" par une icône de corbeille en utilisant Font Awesome.

## Tests et débogage

Il est crucial de tester votre application pour s'assurer que tout fonctionne comme prévu :

1.  **Fonctionnalités de base** : Ajout, suppression et mise à jour des totaux.
2.  **Compatibilité entre navigateurs** : Testez sur Chrome, Firefox, Safari et Edge.
3.  **Réactivité mobile** : Vérifiez que la mise en page s'adapte aux petits écrans.
4.  **Cas limites** : Entrées vides, montants négatifs, nombres très élevés.
5.  **Débogage** : Utilisez la console du navigateur pour identifier les erreurs JavaScript.

## Conclusion

Construire un gestionnaire de dépenses à partir de zéro est un excellent moyen de perfectionner vos compétences en développement web tout en créant un outil utile.

Tout au long de ce tutoriel, nous avons vu comment configurer la structure HTML, styliser avec CSS, ajouter de la logique avec JavaScript et améliorer l'expérience utilisateur.

N'oubliez pas que les principes appliqués ici peuvent être étendus à des projets plus complexes. Merci d'avoir suivi ce tutoriel. J'espère qu'il vous a aidé à gagner en confiance dans vos capacités de développement.

Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter sur [LinkedIn](https://ng.linkedin.com/in/joan-ayebola). Si vous avez apprécié ce contenu, vous pouvez m'offrir un [café](https://www.buymeacoffee.com/joanayebola) pour soutenir la création de futurs tutoriels.