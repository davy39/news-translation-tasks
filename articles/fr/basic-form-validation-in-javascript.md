---
title: Validation de formulaire de base en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/basic-form-validation-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d33740569d1a4ca3673.jpg
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Validation de formulaire de base en JavaScript
seo_desc: "In the past, form validation would occur on the server, after a person\
  \ had already entered in all of their information and pressed the submit button.\
  \ \nIf the information was incorrect or missing, the server would have to send everything\
  \ back with a m..."
---

Dans le passé, la validation de formulaire se faisait sur le serveur, après qu'une personne avait déjà saisi toutes ses informations et appuyé sur le bouton d'envoi. 

Si les informations étaient incorrectes ou manquantes, le serveur devait tout renvoyer avec un message demandant à la personne de corriger le formulaire avant de le soumettre à nouveau.

C'était un processus long et cela mettait beaucoup de charge sur le serveur.

De nos jours, JavaScript offre plusieurs moyens de valider les données d'un formulaire directement dans le navigateur avant de les envoyer au serveur.

Voici le code HTML que nous utiliserons dans les exemples suivants :

```html
<html>
<head>
  <title>Validation de formulaire</title>
  <script type="text/javascript">
    // La validation de formulaire ira ici
  </script>
</head>
<body>
  <form id="form">
    <table cellspacing="2" cellpadding="2" border="1">
      <tr>
        <td align="right">Nom d'utilisateur</td>
        <td><input type="text" id="username" /></td>
      </tr>
      <tr>
        <td align="right">Adresse e-mail</td>
        <td><input type="text" id="email-address" /></td>
      </tr>
      <tr>
        <td></td>
        <td><input type="submit" value="Soumettre" id="submit-btn" /></td>
      </tr>
    </table>
  </form>
</body>
</html>
```

## Validation de base

Ce type de validation consiste à vérifier tous les champs obligatoires et à s'assurer qu'ils sont correctement remplis.

Voici un exemple de base d'une fonction `validate` qui affiche une alerte si les champs de nom d'utilisateur et d'adresse e-mail sont vides, sinon elle retourne vrai :

```js
const submitBtn = document.getElementById('submit-btn');

const validate = (e) => {
  e.preventDefault();
  const username = document.getElementById('username');
  const emailAddress = document.getElementById('email-address');
  if (username.value === "") {
    alert("Veuillez entrer votre nom d'utilisateur.");
    username.focus();
    return false;
  }
  if (emailAddress.value === "") {
    alert("Veuillez entrer votre adresse e-mail.");
    emailAddress.focus();
    return false;
  }
  
  return true;
}

submitBtn.addEventListener('click', validate);

```

Mais que se passe-t-il si quelqu'un entre du texte aléatoire comme adresse e-mail ? Actuellement, la fonction `validate` retournera toujours vrai. Comme vous pouvez l'imaginer, envoyer de mauvaises données au serveur peut entraîner des problèmes.

C'est là que la validation du format des données intervient.

## Validation du format des données

Ce type de validation examine en réalité les valeurs dans le formulaire et vérifie qu'elles sont correctes.

Valider les adresses e-mail est notoirement difficile – il existe un grand nombre d'adresses e-mail et d'hôtes légitimes, et il est impossible de deviner toutes les combinaisons valides de caractères.

Cela dit, il existe quelques facteurs clés qui sont communs à toutes les adresses e-mail valides :

* Une adresse doit contenir un @ et au moins un caractère point (.)
* Le caractère @ ne peut pas être le premier caractère de l'adresse
* Le . doit venir au moins un caractère après le caractère @

Avec cela à l'esprit, de nombreux développeurs utilisent des regex pour déterminer si une adresse e-mail est valide ou non. Voici une fonction que [Tyler McGinnis recommande sur son blog](https://tylermcginnis.com/validate-email-address-javascript/) :

```js
const emailIsValid = email => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

emailIsValid('free@code@camp.org') // false
emailIsValid('quincy@freecodecamp.org') // true
```

Ajoutée au code de l'exemple précédent, cela donnera :

```js
const submitBtn = document.getElementById('submit-btn');

const validate = (e) => {
  e.preventDefault();
  const username = document.getElementById('username');
  const emailAddress = document.getElementById('email-address');
  if (username.value === "") {
    alert("Veuillez entrer votre nom d'utilisateur.");
    username.focus();
    return false;
  }
    
  if (emailAddress.value === "") {
    alert("Veuillez entrer votre adresse e-mail.");
    emailAddress.focus();
    return false;
  }

  if (!emailIsValid(emailAddress.value)) {
    alert("Veuillez entrer une adresse e-mail valide.");
    emailAddress.focus();
    return false;
  }
  
  return true; // Peut soumettre les données du formulaire au serveur
}

const emailIsValid = email => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

submitBtn.addEventListener('click', validate);

```

## Contraintes de formulaire HTML5

Certaines des contraintes HTML5 couramment utilisées pour `<input>` sont l'attribut `type` (par exemple, `type="password"`), `maxlength`, `required` et `disabled`.

Une contrainte moins couramment utilisée est l'attribut `pattern` qui prend une expression régulière JavaScript.

## Plus d'informations

* [Validation des données de formulaire | MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation)
* [Validation par contrainte | MDN](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Constraint_validation)