---
title: Comment construire et valider de beaux formulaires avec HTML, CSS et JS vanille
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-16T21:50:13.000Z'
originalURL: https://freecodecamp.org/news/build-and-validate-beautiful-forms-with-vanilla-html-css-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/sign-up-form-desktop.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment construire et valider de beaux formulaires avec HTML, CSS et JS
  vanille
seo_desc: "By Daniel K. Hunter\nForms are hard.  \nKnowing how to properly collect\
  \ and validate user data is one of the most important skills a frontend developer\
  \ needs to have. But it's hard because edge cases abound. \nYou have to consider\
  \ all of the ways a user..."
---

Par Daniel K. Hunter

Les formulaires sont difficiles. 

Savoir comment collecter et valider correctement les données des utilisateurs est l'une des compétences les plus importantes qu'un développeur frontend doit posséder. Mais c'est difficile parce que les cas particuliers abondent. 

Vous devez considérer toutes les façons dont un utilisateur pourrait casser votre joli petit formulaire tout en fournissant une excellente expérience utilisateur.

La partie UX est importante car les formulaires sont les gardiens des conversions pour les produits et services. Si vous, en tant que développeur frontend, vous trompez, il pourrait y avoir des conséquences financières significatives.

C'est pourquoi il existe des milliers (légère exagération) de bibliothèques de formulaires qui implémentent les meilleures pratiques de l'industrie. 

Il n'y a rien de mal à utiliser ces bibliothèques. Le problème survient lorsque les développeurs les utilisent sans comprendre comment les formulaires fonctionnent réellement et pourquoi certains modèles sont considérés comme des _standards_.

Je vais vous montrer comment je construirais un formulaire d'inscription à partir de zéro, en utilisant uniquement HTML, CSS et JavaScript.

D'accord, sans plus tarder, plongeons-nous.

# Le piège de l'état unique (par défaut)

### Desktop

![Image](https://www.freecodecamp.org/news/content/images/2020/09/sign-up-form-desktop-1.png)

### Mobile

<iframe src="https://nolibs.io/dkh/motifs/2fnKSwMn/embed" frameborder="0" width="100%" height="450" title="Sign Up Form" allowtransparency="true" allowfullscreen="allowfullscreen" class="motif-embed" style="border: 1px solid lightgray; border-radius: 4px;" scrolling="yes"></iframe>



Lorsque vous êtes présenté avec un design comme celui-ci, votre première question devrait être, combien d'états _ne sont_ pas représentés ici ? 

Les exemples ci-dessus représentent un état (quand un utilisateur visite la page de connexion, c'est ce qu'il verra sur desktop et sur mobile). 

D'autres états incluraient :

* État d'erreur
    * Que se passe-t-il si je saisis un email qui existe déjà ?
* État de chargement
    * Que se passe-t-il lorsque je soumets le formulaire ?

Lors de la planification de votre travail, assurez-vous de considérer ce qui n'est pas dans le design et qui doit être pris en compte. Vous devez examiner attentivement les exigences fonctionnelles et poser des questions si vous pensez que quelque chose manque. 

# Exigences fonctionnelles

En parlant d'exigences... 

En tant que développeur, vous serez souvent présenté avec un [PRD](https://en.wikipedia.org/wiki/Product_requirements_document) (Document d'exigences produit) d'un chef de produit, d'un designer ou d'un chef de projet. 

Ces documents sont généralement décomposés en histoires utilisateur individuelles que vous exécuterez pendant un sprint. 

En mettant mon chapeau de chef de produit, voici les exigences fonctionnelles pour notre formulaire :

* L'utilisateur doit fournir une adresse email
* Le mot de passe doit comporter au moins 10 caractères et contenir au moins une lettre majuscule, un nombre et un caractère spécial.
* Nous devons afficher des messages d'erreur à l'utilisateur lorsqu'il ne répond pas aux exigences

## Balisage

Le premier code que nous écrivons sera en HTML avec juste une touche de CSS. 

<iframe src="https://nolibs.io/dkh/motifs/WhCWybHQ/embed" frameborder="0" width="100%" height="450" title="Sign Up Form - Markup" allowtransparency="true" allowfullscreen="allowfullscreen" class="motif-embed" style="border: 1px solid lightgray; border-radius: 4px;"></iframe>



Cela ne semble pas grand-chose pour l'instant, mais il y a du bon travail ici. Plongeons un peu.

* Nous avons configuré les éléments side et main avec notre formulaire
* J'utilise BEM comme guide pour créer des noms de classes et des éléments HTML sémantiques pour la lisibilité.
* Notre page d'inscription adopte une approche mobile first, ce qui signifie que nous écrivons d'abord les styles mobiles et ajoutons des points d'arrêt pour les styles desktop.
* Je tire parti de CSS grid pour la mise en page générale et Flexbox pour positionner les éléments dans la section principale.
* J'ai ajouté un écouteur d'événement de soumission pour le formulaire ainsi qu'une fonction de gestionnaire d'événement qui se contente de journaliser l'objet d'événement pour l'instant.

## Validation

Tirons parti de certaines logiques de validation intégrées en choisissant judicieusement nos types d'entrée. Nous utiliserons les éléments suivants :

* Type d'entrée Email
* Type d'entrée Mot de passe

Le type d'entrée email nous offre quelques validations sympas gratuitement.

1. Il vérifie que le symbole `@` est utilisé
2. Il vérifie également qu'il y a du texte après le symbole 

Puisque l'email et le mot de passe sont obligatoires, ajoutons l'attribut `required` aux deux éléments. Nous ajouterons également un attribut `minlength` à l'entrée du mot de passe.

```html
<form id="dkh-signup-form">
  <div class="dkh-form-header">
    <div>
      <small>S'inscrire avec</small>
      <div class="dkh-form-header__social-wrapper">
        <button type="button" class="dkh-btn dkh-btn-icon dkh-btn-github">
          Github
        </button>
        <button type="button" class="dkh-btn dkh-btn-icon dkh-btn-twitter">
          Twitter
        </button>
      </div>
    </div>
  </div>
  <div class="dkh-form-body">
    <small>Ou connectez-vous avec email et mot de passe</small>
    <div class="dkh-form-field">
      <fieldset>
        <input autofocus class="dkh-form-field__input" name="email" type="email" id="email" required placeholder="Email">
      </fieldset>
      <div class="dkh-form-field__messages"></div>
    </div>
    <div class="dkh-form-field">
      <fieldset>
        <input class="dkh-form-field__input" name="password" type="password" id="password" required minlength="10" placeholder="Mot de passe">
      </fieldset>
      <div class="dkh-form-field__messages"></div>
    </div>
  </div>
  <div class="dkh-form-footer">
    <button class="dkh-btn dkh-btn-primary" type="submit">S'inscrire</button>
  </div>
</form>
```

L'attribut `type=email` indique au navigateur qu'il doit valider l'entrée comme un email.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/email-validation.png)

L'attribut `minlength` sur l'entrée du mot de passe nous donne ce message d'erreur utile :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/minlength.png)

Maintenant, dans notre fonction handleSignupFormSubmit, nous pouvons utiliser l'[API FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData/Using_FormData_Objects) pour obtenir les valeurs de notre formulaire, et éventuellement les soumettre à une API.

```javascript
function handleSignupFormSubmit(e) {
  // empêcher le comportement par défaut du navigateur
  e.preventDefault();

  const formDataEntries = new FormData(signupForm).entries();
  const { email, password } = Object.fromEntries(formDataEntries);

  // soumettre email et mot de passe à une API
}
```

## Messages d'erreur

Les messages d'erreur rendus par le navigateur sont utiles pour commencer, mais que faire si vous voulez que ces messages s'affichent sous leur entrée de formulaire respective ? Que faire si vous voulez contrôler leur apparence ?

Malheureusement, le navigateur ne nous donne aucun contrôle sur la façon dont les messages d'erreur par défaut sont rendus. C'est là que nos éléments div `dkh-form-field__messages` entrent en jeu. Nous pouvons rendre nos messages d'erreur personnalisés à l'intérieur de ces éléments.

Écrivons quelques fonctions de validation personnalisées pour vérifier que les valeurs de mot de passe et d'email de notre utilisateur répondent aux exigences. 

```javascript

function validatePassword(password, minlength) {
  if (!password) return 'Le mot de passe est requis';

  if (password.length < minlength) {
    return `Veuillez entrer un mot de passe d'au moins ${minlength} caractères`;
  }

  const hasCapitalLetter = /[A-Z]/g;
  if (!hasCapitalLetter.test(password)) {
    return 'Veuillez utiliser au moins une lettre majuscule.';
  }

  const hasNumber = /\d/g;
  if (!hasNumber.test(password)) {
    return 'Veuillez utiliser au moins un chiffre.';
  }

  return '';
}
```

```javascript
function validateEmail(email) {
  if (!email) return 'L\'email est requis';
    
  const isValidEmail = /^\S+@\S+$/g
  if (!isValidEmail.test(email)) {
    return 'Veuillez entrer un email valide';
  }

  return '';
}
```

L'expression régulière `/^\\S+@\\S+$/g` est loin d'être infaillible, mais elle vérifie au moins qu'il y a des caractères avant et après le symbole `@`. 

La meilleure façon de valider un email est d'envoyer un email de confirmation à tout utilisateur qui s'inscrit. L'utilisateur devrait alors ouvrir cet email et cliquer sur un lien pour confirmer que son adresse email est valide.

Si vous souhaitez approfondir la validation des emails côté client, ce [fil de discussion](https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript) est excellent.

Maintenant, découvrons comment rendre les messages d'erreur sur la page.

```javascript
function handleSignupFormSubmit(e) {
  // empêcher le comportement par défaut du navigateur
  e.preventDefault();

  const formDataEntries = new FormData(signupForm).entries();
  const { email, password } = Object.fromEntries(formDataEntries);

  const emailErrorMessage = validateEmail(email);
  const passowrdErrorMessage = validatePassword(password);

  if (!emailErrorMessage) {
		// sélectionner l'élément de message du champ de formulaire email
    const emailErrorMessageElement = document.querySelector('.email .dkh-form-field__messages');
    // afficher le message d'erreur email à l'utilisateur
    emailErrorMessageElement.innerText = emailErrorMessage;
  }

  if (passowrdErrorMessage) {
		// sélectionner l'élément de message du champ de formulaire email
    const passwordErrorMessageElement = document.querySelector('.password .dkh-form-field__messages');
    // afficher le message d'erreur du mot de passe à l'utilisateur
    passwordErrorMessageElement.innerText = passowrdErrorMessage;
  }
}
```

Une chose supplémentaire que je vais souligner : pour que ces messages s'affichent, nous devons supprimer les attributs `required` des entrées email et mot de passe.

Nous devons changer la valeur de l'attribut type pour l'entrée email.

```html
<input autofocus class="dkh-form-field__input" type="text" name="email" id="email" required placeholder="Email">
```

Nous devons également supprimer l'attribut `minlength` de l'entrée du mot de passe.

```html
<input class="dkh-form-field__input" name="password" type="password" id="password" required placeholder="Mot de passe">
```

La mise à jour de ces attributs supprime la validation basée sur le navigateur au profit de notre propre logique de validation. Voici comment nos messages d'erreur personnalisés seront rendus :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screen_Shot_2020-09-15_at_11.41.03_AM.png)

## Styles

Je laisse le CSS pour la fin car, selon mon expérience personnelle, il est un peu plus difficile de se concentrer sur la logique lorsque la conception visuelle est complète. 

Lorsque qu'un composant ou une page "semble" terminé à l'œil, cela peut créer une fausse impression qu'il est réellement terminé. Je n'ai aucune recherche pour étayer cela, juste mon opinion personnelle.

Voici l'état de notre code après avoir ajouté beaucoup de CSS.

### Desktop

![Image](https://www.freecodecamp.org/news/content/images/2020/09/sign-up-form-desktop-2.png)

### Mobile

<iframe src="https://nolibs.io/dkh/motifs/2fnKSwMn/embed" frameborder="0" width="100%" height="450" title="Sign Up Form" allowtransparency="true" allowfullscreen="allowfullscreen" class="motif-embed" style="border: 1px solid lightgray; border-radius: 4px;" scrolling="yes"></iframe>

### État d'erreur

![Image](https://www.freecodecamp.org/news/content/images/2020/09/error-state.png)

J'ai inclus des icônes [font awesome](https://fontawesome.com/) pour les boutons Github et Twitter.

```html
<div class="dkh-form-header">
  <div>
    <small>S'inscrire avec</small>
    <div class="dkh-form-header__social-wrapper">
      <button type="button" class="dkh-btn dkh-btn-icon dkh-btn-github">
        <i class="fab fa-github fa-lg"></i>
        Github
      </button>
      <button type="button" class="dkh-btn dkh-btn-icon dkh-btn-twitter">
        <i class="fab fa-twitter fa-lg"></i>
        Twitter
      </button>
    </div>
  </div>
</div>
```

## Résumé

Nous avons créé les blocs de construction pour créer des formulaires d'inscription et de connexion sans bibliothèques tierces. Vous pouvez consulter le code source final [ici](https://nolibs.io/dkh/motifs/2fnKSwMn/edit). 

Si vous utilisez un framework comme React ou Vue, il existe une tonne de bibliothèques de formulaires et de validation géniales. Vous pouvez vous appuyer sur elles pour accomplir rapidement le travail. 

Cependant, si vous êtes nouveau dans le développement logiciel, je vous encourage à vous concentrer d'abord sur les fondamentaux avant d'utiliser ces outils.

J'ai obtenu mon premier emploi en tant que développeur il y a cinq ans et mon parcours dans la tech a changé ma vie pour le mieux à jamais. Je crois qu'il est important de se concentrer et de maîtriser les fondamentaux afin de pouvoir plus facilement comprendre des outils comme React et Vue.

L'un des problèmes que j'ai remarqué en [animant un meetup](https://technical.ly/philly/2018/03/05/free-coding-camp-philly-study-hall/) pendant des années était que les personnes nouvelles en codage se tournaient vers les bibliothèques et les frameworks trop rapidement. Cela a fini par leur nuire et beaucoup ont eu du mal pendant les entretiens.

Si vous apprenez à coder et avez besoin d'aide, n'hésitez pas à me contacter sur [twitter](https://twitter.com/danielkhunter). J'ai hâte d'aider comme je peux.