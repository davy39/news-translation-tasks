---
title: Gestion des formulaires côté client avec JavaScript – Expliqué avec des exemples
  de code
subtitle: ''
author: Samyak Jain
co_authors: []
series: null
date: '2024-03-08T21:10:35.000Z'
originalURL: https://freecodecamp.org/news/form-validation-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/form-handling-in-javascript.jpg
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: JavaScript
  slug: javascript
seo_title: Gestion des formulaires côté client avec JavaScript – Expliqué avec des
  exemples de code
seo_desc: "HTML forms are essential components of most websites and web apps. They\
  \ enable interaction between users and those websites, and are a key concept for\
  \ web developers to understand. \nThis comprehensive guide covers various aspects\
  \ of HTML forms, from ..."
---

Les formulaires HTML sont des composants essentiels de la plupart des sites web et des applications web. Ils permettent l'interaction entre les utilisateurs et ces sites web, et sont un concept clé que les développeurs web doivent comprendre. 

Ce guide complet couvre divers aspects des formulaires HTML, de la création et de la structuration des formulaires à l'interaction avec JavaScript et à la validation des formulaires. 

Comprendre comment travailler avec les formulaires de manière programmatique vous permet de valider et de capturer les entrées utilisateur, de gérer les soumissions et d'améliorer l'expérience utilisateur globale. 

En suivant les exemples et les meilleures pratiques fournies dans ce guide, vous serez équipé des connaissances nécessaires pour construire des formulaires web robustes qui améliorent l'expérience utilisateur et facilitent la collecte et la soumission de données sans faille. 

Que vous soyez débutant ou développeur expérimenté, ce guide sert de ressource précieuse pour comprendre et implémenter efficacement les formulaires HTML dans vos projets web. 

### **Prérequis :**

Une compréhension de base des fondamentaux de JavaScript est recommandée pour comprendre pleinement les concepts discutés dans ce tutoriel. La familiarité avec les formulaires HTML sera également bénéfique pour comprendre et appliquer le matériel couvert.

Si vous êtes nouveau dans JavaScript, il est recommandé de vous familiariser avec les variables, les types de données, les fonctions, les boucles et les techniques de manipulation de base du DOM avant de plonger dans ce tutoriel. Ces connaissances fondamentales faciliteront une expérience d'apprentissage plus fluide alors que nous explorons des sujets plus avancés liés à la gestion des formulaires en JavaScript.

Note de départ : Pour votre commodité, tous les exemples et le code discutés ici peuvent être consultés sur [GitHub](https://github.com/theSamyak/FCC-Blog-CodeArchive/tree/main/Client-Side%20Form%20Handling%20with%20JavaScript).

## **Table des matières**

1. [Comprendre les formulaires HTML](#heading-comprendre-les-formulaires-html)  
– [Introduction aux éléments de formulaire HTML](#heading-introduction-aux-elements-de-formulaire-html)  
– [JavaScript et la gestion des formulaires](#heading-javascript-et-la-gestion-des-formulaires)  
– [Accéder aux champs de formulaire](#accessing-form-fields)  
– [Exemple : Formulaire d'inscription](#heading-voyons-un-exemple-formulaire-dinscription)
2. [Comment créer des boutons radio](#heading-comment-creer-des-boutons-radio)  
– [JavaScript pour gérer la sélection des boutons radio](#javascript-to-handle-radio-button-selection)  
– [Événement de changement de bouton radio](#heading-evenement-de-changement-de-bouton-radio)
3. [Cases à cocher](#heading-cases-a-cocher)  
– [Comment vérifier si une case à cocher est cochée](#heading-comment-verifier-si-une-case-a-cocher-est-cochee)  
– [Comment obtenir les valeurs des cases à cocher](#heading-comment-obtenir-les-valeurs-des-cases-a-cocher)  
– [Comment gérer plusieurs cases à cocher](#heading-comment-gerer-plusieurs-cases-a-cocher)  
– [Comment cocher / décocher toutes les cases à cocher](#heading-comment-cocher-decocher-toutes-les-cases-a-cocher)  
– [Comment générer dynamiquement des cases à cocher](#heading-comment-generer-dynamiquement-des-cases-a-cocher)
4. [Élément Select](#select-element)  
– [Comment interagir avec un élément Select](#how-to-interact-with-a-select-element)  
– [Comment accéder aux options avec JavaScript](#heading-comment-acceder-aux-options-avec-javascript)  
– [Comment gérer plusieurs sélections](#how-to-handle-multiple-selections)  
– [Exemple : Gestionnaire de tâches](#lets-see-an-example-task-manager-adding-and-removing-tasks)
5. [Différence entre l'événement Change et Input](#heading-difference-entre-les-evenements-change-et-input)
6. [Conclusion](#heading-conclusion)

Avant de commencer, voici quelque chose à noter :

Il s'agit d'un suivi de ce [Guide du DOM et des événements](https://www.freecodecamp.org/news/javascript-in-the-browser-dom-and-events/) et ne couvre pas la communication côté serveur/la gestion des formulaires côté serveur dans ce blog, car cela implique des sujets avancés tels que AJAX (Asynchronous JavaScript et XML), les Promesses, la gestion des erreurs et la gestion des opérations asynchrones en JavaScript.

Dans ce tutoriel, nous nous concentrerons plutôt sur la manière de travailler avec divers éléments de formulaire, y compris les boutons radio, les cases à cocher et les éléments de sélection, ainsi que sur la génération dynamique et l'interaction avec eux en utilisant JavaScript. 

Aborder la communication côté serveur dépasserait le cadre de cet article, qui vise à fournir une compréhension complète de la manipulation du DOM et de la gestion des événements dans le contexte des éléments de formulaire.

## Comprendre les formulaires HTML

Les formulaires HTML sont des éléments fondamentaux utilisés pour collecter et soumettre des données utilisateur sur le web. Ils permettent l'interaction entre les utilisateurs et les sites web en permettant aux utilisateurs de saisir des informations, de faire des sélections et de soumettre des données aux serveurs pour traitement.

#### Introduction aux éléments de formulaire HTML

Les formulaires HTML sont créés en utilisant l'élément `<form>`, qui agit comme un conteneur pour divers éléments d'entrée. Les éléments de formulaire courants incluent les champs de texte, les cases à cocher, les boutons radio, les menus déroulants et les boutons.

Pour référencer un formulaire en JS, vous pouvez utiliser des méthodes DOM comme `getElementById()` ou `document.forms`. `document.forms` retourne une collection de formulaires, et vous pouvez accéder à un formulaire spécifique en utilisant un index, un nom ou un identifiant.	

```javascript
const form = document.getElementById('signup');
const firstForm = document.forms[0]; // accéder au premier formulaire
const formByName = document.forms['formName']; // accéder au formulaire par nom
const formById = document.forms['formId']; // accéder au formulaire par identifiant

```

Voyons un exemple de base d'un formulaire HTML :

```html
<form>
  <label for="username">Nom d'utilisateur :</label>
  <input type="text" id="username" name="username"><br>

  <label for="password">Mot de passe :</label>
  <input type="password" id="password" name="password"><br>

  <input type="submit" value="Soumettre">
</form>

```

Dans cet exemple, nous avons un formulaire avec deux champs d'entrée pour le nom d'utilisateur et le mot de passe, ainsi qu'un bouton de soumission.

### Structure et attributs du formulaire

Les formulaires HTML peuvent avoir divers attributs qui contrôlent leur comportement et leur apparence. Certains attributs courants incluent :

* **action** : Spécifie l'URL où les données du formulaire doivent être soumises.
* **method** : Spécifie la méthode HTTP utilisée pour envoyer les données du formulaire (`post` ou `get`).
* **target** : Spécifie où afficher la réponse après la soumission du formulaire (par exemple, `_self`, `_blank`, `_parent`, `_top`).
* **name** : Attribue un nom au formulaire à des fins d'identification.

Voici un exemple de formulaire avec les attributs action, method et target :

```html
<form action="/submit-form" method="POST" name="myForm" target="_blank">
  <!-- Les éléments de formulaire vont ici -->
</form>

```

### JavaScript et la gestion des formulaires

JavaScript utilise l'objet `HTMLFormElement` pour représenter un formulaire. Cet objet a des propriétés correspondant aux attributs HTML `action` et `method`.

Les méthodes comme `submit()` et `reset()` sont utilisées pour soumettre et réinitialiser les formulaires.

```html
const form = document.getElementById('signup');
form.action; // retourne l'attribut action
form.method; // retourne l'attribut method
form.submit(); // soumet le formulaire

```

JavaScript fournit des gestionnaires d'événements pour ajouter de l'interactivité aux formulaires HTML. En exploitant ces événements, vous pouvez exécuter des scripts personnalisés en réponse aux actions des utilisateurs dans le formulaire :

**Événement de soumission** : Un formulaire a généralement un bouton de soumission, qui, lorsqu'il est cliqué, envoie les données du formulaire au serveur. Cela est réalisé en utilisant un élément `<input>` ou `<button>` avec `type="submit"`.

```html
<input type="submit" value="S'inscrire">
// ou
<button type="submit">S'inscrire</button>
```

Pour attacher un écouteur d'événement à l'événement de soumission, vous utilisez la méthode `addEventListener()`. Voici un exemple :

```javascript
const form = document.getElementById('signup');
form.addEventListener('submit', (event) => {
    // Logique de validation et de soumission personnalisée ici
});

```

Dans de nombreux cas, vous pouvez vouloir intercepter le comportement de soumission de formulaire par défaut et exécuter une logique personnalisée avant de permettre au formulaire d'être soumis au serveur. Vous pouvez utiliser `preventDefault()` pour cela. Exemple :

```javascript
const form = document.getElementById('signup');
form.addEventListener('submit', (event) => {
    event.preventDefault(); // Empêche la soumission de formulaire par défaut
    // Logique de validation et de soumission personnalisée ici
});
```

Sans `event.preventDefault()`, toute logique de validation et de soumission personnalisée s'exécuterait toujours dans l'écouteur d'événement, mais le comportement de soumission de formulaire par défaut ne serait pas empêché.

**Événement de réinitialisation** : L'événement `reset` est déclenché lorsque le formulaire est réinitialisé en utilisant un bouton de réinitialisation ou de manière programmatique. Nous utilisons la méthode `reset()` pour effacer tous les champs de formulaire et les réinitialiser à leurs valeurs par défaut.

```javascript
document.querySelector('form').addEventListener('reset', function(event) {
    // Logique de réinitialisation de formulaire personnalisée ici
});
```

### Comment accéder aux champs de formulaire

Vous pouvez accéder aux champs de formulaire en utilisant des méthodes DOM comme `getElementsByName()`, `getElementById()`, `querySelector()`, etc.

La propriété `form.elements` stocke une collection d'éléments de formulaire. Vous pouvez accéder à ces éléments par index, identifiant ou nom. Voici un exemple :

```javascript
const form = document.getElementById('signup');
const nameField = form.elements['name']; // accéder à l'élément par nom
const emailField = form.elements['email']; // accéder à l'élément par nom
const firstElement = form.elements[0]; // accéder au premier élément par index

```

Une fois que vous avez accédé à un champ de formulaire, vous pouvez utiliser la propriété `value` pour accéder à sa valeur. Voici un exemple :

```javascript
const nameValue = nameField.value;
const emailValue = emailFieldByName.value;

```

### Validation de formulaire

La validation de formulaire est un aspect essentiel du développement web qui garantit que les données soumises par les utilisateurs sont exactes et répondent à des critères spécifiés avant d'être traitées par le serveur. Les validations courantes incluent la vérification des champs vides, des formats d'email valides, etc.

#### Validation de formulaire HTML

HTML5 fournit une validation de formulaire intégrée via divers attributs :

* **required** : Spécifie qu'un champ doit être rempli.
* **pattern** : Spécifie une expression régulière que la valeur d'entrée doit correspondre.
* **min** et **max** : Spécifient les valeurs minimale et maximale pour un champ d'entrée.
* **maxlength** et **minlength** : Spécifient la longueur maximale et minimale de l'entrée
* **type** : Spécifie le type d'entrée attendu (par exemple, email, nombre, date).

Voici un exemple de validation de formulaire HTML utilisant ces attributs :

```html
<form>
  <label for="username">Nom d'utilisateur :</label>
  <input type="text" id="username" name="username" required minlength="3" maxlength="15"><br>

  <label for="email">Email :</label>
  <input type="email" id="email" name="email" required><br>

  <label for="age">Âge :</label>
  <input type="number" id="age" name="age" min="18" max="99"><br>

  <input type="submit" value="Soumettre">
</form>

```

#### Validation de formulaire JavaScript

JavaScript permet aux développeurs d'effectuer une logique de validation plus sophistiquée au-delà de ce que les attributs HTML offrent. Des écouteurs d'événements peuvent être attachés aux éléments de formulaire pour gérer la validation de manière dynamique. 

Voici un exemple de base de validation de formulaire JavaScript :

```javascript
const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Empêcher la soumission du formulaire

    // Effectuer une logique de validation personnalisée
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!emailIsValid(email)) {
        alert('Veuillez entrer une adresse email valide.');
        return;
    }

    if (password.length < 6) {
        alert('Le mot de passe doit comporter au moins 6 caractères.');
        return;
    }

    // Si la validation réussit, soumettre le formulaire
    form.submit();
});

function emailIsValid(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

```

Dans cet exemple, la fonction JavaScript `emailIsValid()` utilise une expression régulière pour valider le format de l'email. L'écouteur d'événement `submit` empêche le formulaire d'être soumis si la validation échoue, et des messages d'erreur personnalisés sont affichés à l'utilisateur.

### Voyons un exemple : Formulaire d'inscription

Maintenant, combinons tous les concepts que nous avons couverts dans un exemple complet de formulaire d'inscription avec validation côté client en utilisant JavaScript :

```html
<!DOCTYPE html>
<html>
  <body>
    <h2>Inscription de l'utilisateur</h2>
    <form id="registrationForm">
      <div>
        <label for="username">Nom d'utilisateur :</label>
        <input type="text" id="username" name="username" />
      </div>
      <div>
        <label for="email">Email :</label>
        <input type="email" id="email" name="email" />
      </div>
      <div>
        <label for="password">Mot de passe :</label>
        <input type="password" id="password" name="password" />
      </div>
      <div>
        <input type="submit" value="S'inscrire" />
      </div>
    </form>

    <div id="errorMessages"></div>
    <script src="script.js"></script>
  </body>
</html>

```

**Structure HTML** : Nous avons un formulaire d'inscription simple avec des champs pour le nom d'utilisateur, l'email, le mot de passe et un bouton de soumission. Il y a aussi un div conteneur (`errorMessages`) pour afficher les messages d'erreur de validation.

Maintenant, écrivons le code JavaScript pour gérer la soumission du formulaire et effectuer la validation côté client :

```javascript
const registrationForm = document.getElementById("registrationForm");
const errorMessages = document.getElementById("errorMessages");

registrationForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const { username, email, password } = registrationForm.elements;

  errorMessages.innerHTML = "";

  if (!username.value.trim()) {
    displayError("Le nom d'utilisateur est requis.");
    return;
  }

  if (!email.value.trim() || !isValidEmail(email.value)) {
    displayError("Veuillez entrer une adresse email valide.");
    return;
  }

  if (!password.value.trim() || !isStrongPassword(password.value)) {
    displayError(
      "Le mot de passe doit comporter au moins 8 caractères et contenir au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial."
    );
    return;
  }

  alert("Inscription réussie !");
  registrationForm.reset();
});

function displayError(message) {
  errorMessages.innerHTML += `<div class="error">${message}</div>`;
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function isStrongPassword(password) {
  return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$/.test(password);
}

```

**Gestion JavaScript** : Nous sélectionnons le formulaire et le conteneur de message d'erreur en utilisant `getElementById`. Nous attachons un écouteur d'événement à l'événement de soumission du formulaire. Lorsque le formulaire est soumis, nous empêchons son comportement par défaut en utilisant `event.preventDefault()` pour gérer la soumission du formulaire manuellement.

**Validation du formulaire** : Nous récupérons les valeurs du nom d'utilisateur, de l'email et du mot de passe.

Nous effectuons une validation de base : Le nom d'utilisateur ne doit pas être vide, l'email doit être dans un format valide, le mot de passe doit comporter au moins 8 caractères et contenir au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial.

**Gestion des erreurs** : Si une validation échoue, nous affichons le message d'erreur correspondant. Les messages d'erreur sont affichés dans le div `errorMessages`.

**Réinitialisation du formulaire** : Après une inscription réussie (dans ce cas, une simple alerte), nous réinitialisons le formulaire en utilisant `registrationForm.reset()`

Actuellement, le code utilise une `alerte` pour indiquer une inscription réussie. Dans un scénario réel, vous pourriez vouloir implémenter un appel AJAX pour soumettre les données à un serveur pour traitement et gérer la réponse en conséquence. Mais ce n'est pas ce dont nous allons discuter, comme mentionné au début de ce tutoriel.

Dans l'ensemble, cet exemple couvre la création de formulaires, la gestion des formulaires avec JavaScript, la validation des formulaires en utilisant des expressions régulières, et l'affichage dynamique de messages d'erreur personnalisés, démontrant un formulaire d'inscription utilisateur de base avec validation côté client.

## Boutons radio

Les boutons radio sont un élément de formulaire courant utilisé pour sélectionner une option parmi un ensemble d'options. En JavaScript, vous pouvez manipuler les boutons radio pour récupérer les sélections des utilisateurs et effectuer des actions basées sur ces sélections.

### Comment créer des boutons radio

Vous pouvez utiliser des boutons radio si vous souhaitez que les utilisateurs sélectionnent une seule option parmi un ensemble de choix. En HTML, vous pouvez créer des boutons radio en utilisant l'élément `<input>` avec l'attribut `type` défini sur "radio". Un groupe de boutons radio avec le même attribut `name` forme un groupe radio. 

Voici un exemple :

```html
<!DOCTYPE html>
<html>
  <body>
    <form id="languageForm">
      <p>Sélectionnez votre langage de programmation préféré :</p>
      <div>
        <input type="radio" name="language" value="JavaScript" id="js" />
        <label for="js">JavaScript</label>
      </div>
      <div>
        <input type="radio" name="language" value="Python" id="python" />
        <label for="python">Python</label>
      </div>
      <div>
        <input type="radio" name="language" value="Java" id="java" />
        <label for="java">Java</label>
      </div>
      <!-- Plus d'options de langage peuvent être ajoutées ici -->
    </form>
  </body>
</html>

```

Vous utilisez les attributs `id` et `for` pour l'accessibilité, reliant l'étiquette au bouton radio correspondant.

### Comment récupérer la valeur du bouton radio sélectionné 

Maintenant, discutons de la manière de récupérer la valeur du bouton radio sélectionné en utilisant JavaScript.

```html
    <!-- HTML -->
    <button id="btn">Afficher le langage sélectionné</button>
    <p id="output"></p>

    <script>
      const btn = document.querySelector("#btn");
      const radioButtons = document.querySelectorAll('input[name="language"]');
      const output = document.getElementById("output");

      btn.addEventListener("click", () => {
        let selectedLanguage;
        for (const radioButton of radioButtons) {
          if (radioButton.checked) {
            selectedLanguage = radioButton.value;
            break;
          }
        }
        // Affichage de la sortie :
        output.innerText = selectedLanguage
          ? `Vous avez sélectionné ${selectedLanguage}`
          : `Vous n'avez sélectionné aucun langage`;
      });
    </script>
```

Voici comment fonctionne ce code : le code JavaScript initialise en sélectionnant le bouton, les boutons radio et les éléments de sortie du document HTML. Nous ajoutons un écouteur d'événement de clic à l'élément bouton. Lorsque le bouton est cliqué, la fonction à l'intérieur de l'écouteur d'événement est exécutée.

À l'intérieur de l'écouteur d'événement de clic, nous itérons sur tous les boutons radio dans la collection `radioButtons`. Nous vérifions si un bouton radio est coché en utilisant sa propriété `checked`. Si un bouton radio est coché, nous attribuons sa valeur à la variable `selectedLanguage` et sortons de la boucle en utilisant `break`.

Nous mettons à jour le contenu de l'élément de sortie (`<p>` tag avec l'id `output`) en fonction du fait qu'un langage est sélectionné. Si un langage est sélectionné (`selectedLanguage` est truthy), nous affichons un message indiquant le langage sélectionné. Sinon, nous invitons l'utilisateur à sélectionner un langage.

### Événement de changement de bouton radio

Lorsque qu'un bouton radio est coché ou décoché, il déclenche un événement `change`. Vous pouvez écouter cet événement en utilisant `addEventListener()`. À l'intérieur du gestionnaire d'événement, vous pouvez accéder à l'état coché et à la valeur du bouton radio en utilisant `this.checked` et `this.value`.

```javascript
radioButton.addEventListener('change', function (e) {
  if (this.checked) {
    console.log(this.value);
  }
});
```

### Comment générer dynamiquement des boutons radio

Maintenant, explorons comment générer dynamiquement des boutons radio en utilisant JavaScript. Cela est utile lorsque vous souhaitez créer des options de boutons radio dynamiquement en fonction de certains critères ou données.

Supposons que nous avons un tableau de langages, et nous voulons générer dynamiquement des boutons radio pour chaque option de langage :

```javascript
<!DOCTYPE html>
<html>
  <body>
    <div id="languages"></div>

    <script>
      const languageOptions = ["Python", "Javascript", "C++", "Java"];

      // Générer les boutons radio
      const languages = document.querySelector("#languages");
      languages.innerHTML = languageOptions.map((language) => `
          <div>
              <input type="radio" name="language" value="${language}" id="${language}">
              <label for="${language}">${language}</label>
          </div>`).join(' ');
    </script>
  </body>
</html>

```

Il génère dynamiquement des boutons radio en fonction du tableau `languageOptions` et les insère dans l'élément conteneur (`<div id="languages"></div>`). Chaque bouton radio a un identifiant et une valeur uniques correspondant au nom du langage, et les étiquettes sont associées à leurs boutons radio respectifs en utilisant l'attribut `for`.

Après avoir généré dynamiquement les boutons radio, ajoutons maintenant des écouteurs d'événements `change` pour gérer les changements de sélection.

```javascript
    <!-- HTML -->
    <div id="languages"></div>
    <div id="languageOutput"></div> // nous créons celui-ci pour récupérer la sortie de notre langage sélectionné
    
    <!-- Générer les boutons radio -->

// Attacher les écouteurs d'événements de changement
const radioButtons = document.querySelectorAll('input[name="language"]');
for (const radioButton of radioButtons) {
    radioButton.addEventListener('change', showSelectedlanguage);
}        

// Gérer l'événement de changement
function showSelectedlanguage() {
    if (this.checked) {
        document.querySelector('#languageOutput').innerText = `Vous avez sélectionné ${this.value}`;
    }
}

```

Voici ce qui se passe :

* Nous sélectionnons tous les boutons radio avec l'attribut `name` défini sur `"language"`.
* Nous utilisons une boucle `for...of` pour itérer sur chaque bouton radio et ajouter un écouteur d'événement `change` à chaque bouton radio. Cet écouteur écoute les changements dans l'état des boutons radio, c'est-à-dire lorsqu'un bouton radio est sélectionné ou désélectionné.
* Nous définissons une fonction nommée `showSelectedLanguage` pour gérer l'événement de changement déclenché par la sélection d'un bouton radio. 
* À l'intérieur de la fonction `showSelectedLanguage`, nous vérifions d'abord si le bouton radio actuel (`this`) est coché en utilisant la propriété `checked`. Si le bouton radio est coché, nous mettons à jour le contenu textuel d'un élément avec l'identifiant `languageOutput` en utilisant `document.querySelector('#languageOutput')`. Cet élément sert de placeholder pour afficher le langage sélectionné.

Cette configuration garantit que les boutons radio générés dynamiquement ont des écouteurs d'événements `change` attachés, permettant une gestion dynamique des sélections de l'utilisateur.

## Cases à cocher

### Comment créer une case à cocher HTML

Créons d'abord une case à cocher en utilisant l'élément `<input>` et l'attribut type défini sur "checkbox". Associons-la à une étiquette pour une meilleure accessibilité.

```html
<label for="agree">
   <input type="checkbox" id="agree" name="agree" value="yes"> J'accepte les termes
</label>

```

### Comment vérifier si une case à cocher est cochée

Une case à cocher en HTML peut exister dans deux états : cochée et non cochée. Et nous pouvons déterminer lequel est actif en utilisant la propriété `checked`. Si elle est `true`, la case à cocher est cochée – sinon, elle est non cochée. Exemple :

```html
<!DOCTYPE html>
<html>
<body>
    <label for="agree">
        <input type="checkbox" id="agree" name="agree"> J'accepte les termes
    </label>

    <script>
        const checkbox = document.getElementById('agree');
        console.log(checkbox.checked);
    </script>
</body>
</html>
```

### Comment obtenir les valeurs des cases à cocher

Dans les formulaires HTML, lorsqu'une case à cocher est cochée et que le formulaire est soumis, le navigateur inclut la case à cocher dans les données du formulaire avec son attribut `name` comme clé et l'attribut `value` (si spécifié) comme valeur. Mais si la case à cocher n'est pas cochée, elle n'est pas incluse dans les données du formulaire du tout.

```html
<label for="agree">
    <input type="checkbox" id="agree" name="agree"> J'accepte les termes
</label>

<button id="btn">Afficher la valeur</button>
<script>
    const checkbox = document.querySelector('#agree');
    const btn = document.querySelector('#btn');
    btn.onclick = () => {
       alert(checkbox.value);
    };
</script>

```

Donc, en gros, le point est : Lorsqu'une case à cocher est cochée et incluse dans les soumissions de formulaire, le navigateur envoie par défaut `'on'` comme valeur si aucun attribut `value` n'est explicitement défini pour l'élément d'entrée de la case à cocher. Pour gérer correctement l'état coché d'une case à cocher en utilisant JavaScript, utilisez la propriété `checked` au lieu de vous fier uniquement à l'attribut `value`.

### Comment gérer plusieurs cases à cocher

Parfois, vous pouvez avoir besoin de travailler avec plusieurs cases à cocher ayant le même nom et vous souhaitez récupérer les valeurs des cases à cocher sélectionnées. Voici un exemple :

```html
<!DOCTYPE html>
<html>
  <body>
    <p>Sélectionnez vos langages préférés :</p>
    <label for="l1">
      <input type="checkbox" name="language" value="C++" id="l1" />C++
    </label>
    <label for="l2">
      <input type="checkbox" name="language" value="Python" id="l2" />Python
    </label>
    <label for="l3">
      <input type="checkbox" name="language" value="Java" id="l3" />Java
    </label>
    <p>
      <button id="btn">Obtenir les langages sélectionnés</button>
    </p>

    <script>
      const btn = document.querySelector("#btn");
      btn.addEventListener("click", () => {
        const checkboxes = document.querySelectorAll(
          'input[name="language"]:checked'
        );
        const selectedLanguages = Array.from(checkboxes).map(
          (checkbox) => checkbox.value
        );
        alert("Langages sélectionnés : " + selectedLanguages.join(", "));
      });
    </script>
  </body>
</html>

```

Dans cet exemple, nous avons des cases à cocher pour sélectionner les langages de programmation préférés.

* Lorsque le bouton est cliqué, il déclenche un écouteur d'événement. À l'intérieur de l'écouteur d'événement, nous sélectionnons toutes les cases à cocher avec l'attribut de nom "language" qui sont cochées.
* Nous convertissons ensuite la NodeList retournée par `querySelectorAll()` en un tableau en utilisant `Array.from()`.
* Enfin, nous parcourons le tableau pour récupérer les valeurs des cases à cocher sélectionnées et les affichons en utilisant `alert()`.

### Comment cocher / décocher toutes les cases à cocher

Maintenant, créons une fonctionnalité pour cocher ou décocher toutes les cases à cocher à la fois :

```html
<!DOCTYPE html>
<html>
  <body>
    <p>
      <button id="btn">Cocher / Décocher tout</button>
    </p>
    <p>Sélectionnez vos langages préférés :</p>
    <label for="l1">
      <input type="checkbox" name="language" value="C++" id="l1" />C++
    </label>
    <label for="l2">
      <input type="checkbox" name="language" value="Python" id="l2" />Python
    </label>
    <label for="l3">
      <input type="checkbox" name="language" value="Java" id="l3" />Java
    </label>
    <script src="script.js"></script>
  </body>
</html>

```

Code JavaScript :

```javascript
// fonction pour cocher ou décocher toutes les cases à cocher
function check(checked = true) {
  const checkboxes = document.querySelectorAll('input[name="language"]');

  // Parcourir chaque case à cocher
  checkboxes.forEach((checkbox) => {
    // Définir la propriété checked de chaque case à cocher sur la valeur du paramètre 'checked'
    checkbox.checked = checked;
  });
}

// fonction pour cocher toutes les cases à cocher et changer le comportement du bouton pour décocher tout
function checkAll() {
  check();
  this.onclick = uncheckAll;
}

// fonction pour décocher toutes les cases à cocher et changer le comportement du bouton pour cocher tout
function uncheckAll() {
  check(false);
  this.onclick = checkAll;
}

const btn = document.querySelector("#btn");

btn.onclick = checkAll;

```

Dans cet exemple, nous avons un bouton étiqueté "Cocher / Décocher tout".

* Lorsque le bouton est cliqué pour la première fois, il est destiné à cocher toutes les cases à cocher. Par conséquent, la fonction `checkAll` est assignée pour gérer cette action (`const btn = document.querySelector("#btn");`).
* Si le bouton est cliqué à nouveau, il décoche toutes les cases à cocher. Nous définissons les fonctions `check()`, `checkAll()`, et `uncheckAll()` pour gérer la coche et le décochage des cases à cocher.
* Nous assignons `checkAll()` à l'événement `onclick` du bouton initialement, puis nous basculons entre `checkAll()` et `uncheckAll()` en fonction de l'état actuel des cases à cocher.

Une approche alternative pourrait être :

```javascript
function checkAll(checked = true) {
  const checkboxes = document.querySelectorAll('input[name="language"]');
  checkboxes.forEach((checkbox) => {
    checkbox.checked = checked;
  });
}

const btn = document.querySelector("#btn");

btn.addEventListener("click", () => {
  // Trouver la première case à cocher avec l'attribut name défini sur 'language'
  const firstCheckbox = document.querySelector('input[name="language"]');
  // Vérifier si la première case à cocher est cochée
  const isChecked = firstCheckbox.checked;
  // Appeler la fonction checkAll avec l'état opposé de la première case à cocher
  checkAll(!isChecked);
});

```

Ici, nous sélectionnons la première case à cocher avec le nom "language" pour déterminer son état coché actuel. Ensuite, nous appelons `checkAll()` avec l'état opposé.

### Comment générer dynamiquement des cases à cocher

```html
<!DOCTYPE html>
<html>
  <body>
    <div id="languages"></div>

    <script>
      const languageOptions = ["Python", "Javascript", "C++", "Java"];

      // Générer les cases à cocher
      const html = languageOptions
        .map(
          (language) => `<label for="language-${language}">
                <input type="checkbox" name="language" id="language-${language}" value="${language}"> ${language}
            </label>`
        )
        .join(" ");
      document.querySelector("#languages").innerHTML = html;
    </script>
  </body>
</html>

```

Voici comment cela fonctionne :

* Nous définissons un tableau `languageOptions` contenant les noms des langages.
* Nous utilisons la méthode `map()` pour parcourir le tableau `languageOptions` et générer un tableau de chaînes HTML pour chaque langage.
* Chaque chaîne HTML comprend un élément `label` associé à une case à cocher `input`. La case à cocher `input` inclut des attributs appropriés tels que `type`, `name`, `id` et `value`, dérivés dynamiquement du nom du langage.
* Nous joignons le tableau de chaînes HTML en une seule chaîne en utilisant `join(' ')`.
* Enfin, nous définissons la propriété `innerHTML` de l'élément racine `<div>` avec l'identifiant `languages` à la chaîne HTML générée, rendant ainsi les cases à cocher pour chaque langage de programmation.

## Élément Select :

L'élément `<select>` en HTML fournit une liste déroulante d'options parmi lesquelles les utilisateurs peuvent choisir. Il permet une sélection unique ou multiple. Exemple :

```javascript
<select id="cities">
    <option value="JAI">Jaipur</option>
    <option value="DEL">New Delhi</option>
    <option value="UDR">Udaipur</option>
    <option value="MUM">Mumbai</option>
</select>

```

Par défaut, un élément `<select>` permet une seule sélection. Pour activer plusieurs sélections, ajoutez l'attribut `multiple`. 

```javascript
<select id="cities" multiple>
```

Les utilisateurs peuvent maintenant sélectionner plusieurs fruits en maintenant la touche Ctrl (ou Cmd sur Mac) enfoncée tout en cliquant.

### Comment interagir avec un élément Select :

Pour interagir avec un élément `<select>` en utilisant JavaScript, nous utilisons le type `HTMLSelectElement`, qui fournit des propriétés utiles comme `selectedIndex` et `value`. Exemple :

```html
<script>
const selectElement = document.getElementById('cities');
console.log(selectElement.selectedIndex); // Retourne l'index de l'option sélectionnée
console.log(selectElement.value); // Retourne la valeur de l'option sélectionnée
console.log(selectElement.multiple); // Retourne true si plusieurs sélections sont autorisées
</script>
```

JavaScript vous permet de gérer les événements sur l'élément `<select>`, tels que lorsqu'un utilisateur sélectionne une option. Exemple :

```javascript
<button id="btn">Obtenir la ville sélectionnée</button>
    <script>
      const btn = document.querySelector("#btn");
      const selectElement = document.getElementById("cities");
      btn.onclick = (event) => {
        event.preventDefault();
        const selectedCity =
          selectElement.options[selectElement.selectedIndex].text;
        alert(`Ville sélectionnée : ${selectedCity}, 
        Index : ${selectElement.selectedIndex}`);
      };
    </script>
```

**Utilisation de la propriété `value` :** La propriété `value` représente la valeur de l'option sélectionnée. Comprenons-la avec un exemple :

```html
<select id="cities">
    <option value="">Jaipur</option> 
    <option value="DEL">New Delhi</option>
    <option value="UDR">Udaipur</option>
    <option>Mumbai</option>
</select>
```

```javascript
const btn = document.querySelector("#btn");
const selectElement = document.querySelector("#cities");

btn.onclick = (event) => {
    event.preventDefault();
    alert(selectElement.value);
};

```

* Si "Jaipur" est sélectionné, cela signifie que nous avons une chaîne vide puisque l'attribut value est vide dans notre HTML.
* Si une option manque d'un attribut value, la propriété value de la boîte de sélection devient le texte de l'option sélectionnée. Exemple : si "Mumbai" est sélectionné, la propriété value est "Mumbai".
* Si plusieurs options sont sélectionnées, la propriété `value` de la boîte de sélection est dérivée de la première option sélectionnée en fonction des règles précédentes.

### Comment accéder aux options avec JavaScript

Le type `HTMLOptionElement` représente les éléments `<option>` individuels dans un élément `<select>` en JavaScript. Il fournit des propriétés comme `index`, `selected`, `text` et `value` pour accéder aux informations sur chaque option. 

```javascript
const selectElement = document.getElementById('cities');
const secondOptionText = selectElement.options[1].text; // Accéder au texte de la deuxième option
const secondOptionValue = selectElement.options[1].value; // Accéder à la valeur de la deuxième option

```

### Comment gérer plusieurs sélections :

Lorsque qu'un élément `<select>` permet plusieurs sélections, vous pouvez itérer à travers ses options pour trouver celles qui sont sélectionnées et récupérer leurs valeurs textuelles. 

```javascript
const selectElement = document.getElementById('cities');
const selectedOptions = Array.from(selectElement.options).filter(option => option.selected);
const selectedValues = selectedOptions.map(option => option.text); 
```

La sortie sera un tableau contenant le texte des options sélectionnées. Nous pouvons utiliser `option.value` pour obtenir un tableau de valeurs à la place. Exemple :

```html
<!DOCTYPE html>
<html>
  <body>
    <select id="cities" multiple>
      <option value="JAI">Jaipur</option>
      <option value="DEL">New Delhi</option>
      <option value="UDR">Udaipur</option>
      <option value="MUM">Mumbai</option>
    </select>

    <button id="btn">Obtenir les villes sélectionnées</button>
    <script>
      const btn = document.querySelector("#btn");
      const selectElement = document.querySelector("#cities");

      btn.onclick = (event) => {
        event.preventDefault();
        const selectedOptions = Array.from(selectElement.options)
          .filter((option) => option.selected)
          .map((option) => option.text);
        alert("Ville sélectionnée : " + selectedOptions.join(", "));
      };
    </script>
  </body>
</html>

```

* Lorsque le bouton est cliqué, le script collecte les options sélectionnées en filtrant les options en fonction de la propriété `selected`. Il map ensuite les options sélectionnées pour récupérer leur contenu textuel.
* Enfin, il affiche les langages sélectionnés dans un message d'alerte.

### Voyons un exemple : Gestionnaire de tâches (Ajout et suppression de tâches)

```html
<!DOCTYPE html>
<html>
  <style>
    #container {
      max-width: 540px;
      margin: 50px auto;
    }

    form {
      display: flex;
      flex-direction: column;
    }
  </style>
  <body>
    <div id="container">
      <form>
        <label for="task">Tâche :</label>
        <input
          type="text"
          id="task"
          placeholder="Entrez une tâche"
          autocomplete="off"
        />

        <button id="btnAdd">Ajouter une tâche</button>

        <label for="taskList">Liste des tâches :</label>
        <select id="taskList" name="taskList" multiple></select>

        <button id="btnRemove">Supprimer les tâches sélectionnées</button>
      </form>
    </div>
    <script src="script.js"></script>
  </body>
</html>

```

Cette structure HTML inclut des champs d'entrée pour saisir les descriptions des tâches, des boutons pour ajouter et supprimer des tâches, et un élément `<select>` pour afficher la liste des tâches. Nous avons ajouté un peu de CSS pour la clarté. Voyons maintenant le code JavaScript :

```javascript
const btnAdd = document.querySelector('#btnAdd');
const btnRemove = document.querySelector('#btnRemove');
const taskList = document.querySelector('#taskList');
const taskInput = document.querySelector('#task');

btnAdd.onclick = (e) => {
    e.preventDefault();

    // Valider l'entrée de la tâche
    if (taskInput.value.trim() === '') {
        alert('Veuillez entrer une description de tâche.');
        return;
    }

    // Créer une nouvelle option de tâche
    const option = new Option(taskInput.value, taskInput.value);
    taskList.add(option, undefined);

    // Réinitialiser l'entrée de la tâche
    taskInput.value = '';
    taskInput.focus();
};

btnRemove.onclick = (e) => {
    e.preventDefault();

    // Sauvegarder les tâches sélectionnées
    let selectedTasks = [];

    for (let i = 0; i < taskList.options.length; i++) {
        selectedTasks[i] = taskList.options[i].selected;
    }

    // Supprimer les tâches sélectionnées
    let index = taskList.options.length;
    while (index--) {
        if (selectedTasks[index]) {
            taskList.remove(index);
        }
    }
};

```

Explication : nous sélectionnons les éléments nécessaires du HTML et attachons des écouteurs d'événements aux boutons "Ajouter une tâche" et "Supprimer les tâches sélectionnées". Lorsque le bouton "Ajouter une tâche" est cliqué, nous créons une nouvelle option de tâche basée sur la valeur du champ d'entrée et l'ajoutons à l'élément `<select>`. Lorsque le bouton "Supprimer les tâches sélectionnées" est cliqué, nous supprimons les tâches sélectionnées de l'élément `<select>`.

## Différence entre l'événement Change et Input

L'événement input en JavaScript est déclenché chaque fois que la valeur d'un élément input, `<select>`, ou `<textarea>` change. Contrairement à l'événement change, qui attend qu'une valeur soit validée (par exemple, lorsqu'un input perd le focus), l'événement input se déclenche en continu lorsque la valeur change. L'événement input fournit essentiellement un moyen de répondre à l'entrée de l'utilisateur en temps réel. Exemple : 

```html
<!DOCTYPE html>
<html>
<body>
    <label for="userInput">Entrez votre nom :</label>
    <input type="text" id="userInput" placeholder="Votre nom">
    <p>Votre nom est : <span id="displayName"></span></p>
</body>
</html>

```

```javascript
<script>
    const userInput = document.getElementById('userInput');
    const Name = document.getElementById('displayName');

    userInput.addEventListener('input', function() {
        Name.textContent = userInput.value || 'Invité !';
    });
</script>
```

* Ce code JavaScript sélectionne le champ d'entrée avec l'ID "userInput" et l'élément span avec l'ID "displayName".
* Un écouteur d'événement est attaché à l'événement input du champ userInput.
* Lorsque l'événement input est déclenché (par exemple, lors de la saisie dans le champ d'entrée), le gestionnaire d'événement met à jour le contenu textuel de l'élément `displayName` span dynamiquement pour refléter le nom saisi, ou il affiche "Invité" si le champ d'entrée est vide.
* Maintenant, si vous changez 'input' en 'change' ici `userInput.addEventListener('input', function()` comme ceci : `userInput.addEventListener('change', function()`, l'écouteur d'événement ne sera déclenché que lorsque le champ d'entrée perdra le focus après qu'une valeur aura été saisie (par opposition à en continu pendant que la valeur est modifiée en temps réel).

## Conclusion

En comprenant les fondamentaux des éléments de formulaire HTML, des attributs et des événements, vous pouvez créer des formulaires web dynamiques et conviviaux qui améliorent l'expérience utilisateur. 

JavaScript joue un rôle crucial dans la gestion des soumissions de formulaires, la validation des entrées utilisateur et la fourniture de feedback en temps réel aux utilisateurs.

À travers des exemples pratiques et des explications détaillées, dans ce guide, vous avez appris à travailler avec des boutons radio, des cases à cocher, des éléments de sélection et à gérer plusieurs sélections. 

Continuez à explorer et à expérimenter avec les concepts présentés ici pour créer des formulaires robustes et intuitifs pour vos applications web.