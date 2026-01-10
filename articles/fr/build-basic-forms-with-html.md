---
title: Les formulaires en HTML – Comment créer des formulaires de base avec HTML
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-12T14:44:04.000Z'
originalURL: https://freecodecamp.org/news/build-basic-forms-with-html
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Presentacion-Brainstorming-Lluvia-de-Ideas-Doodle-Blanco.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Les formulaires en HTML – Comment créer des formulaires de base avec HTML
seo_desc: 'Forms are a fundamental part of web development, allowing users to input
  and submit data efficiently.

  Creating forms in HTML is a relatively straightforward process. In this article,
  we''ll explore how to build basic forms using HTML <form>, <input>, ...'
---

Les formulaires sont une partie fondamentale du développement web, permettant aux utilisateurs de saisir et de soumettre des données efficacement.

La création de formulaires en HTML est un processus relativement simple. Dans cet article, nous explorerons comment construire des formulaires de base en utilisant les éléments HTML `<form>`, `<input>` et `<button>`. Nous aborderons également divers types de saisie tels que le texte, le mot de passe, les boutons radio, les cases à cocher et les boutons de soumission.

## Qu'est-ce qu'un formulaire en HTML ?

En HTML, un formulaire est un conteneur utilisé pour collecter et soumettre des données des visiteurs d'un site web. Il agit comme une zone interactive où les utilisateurs peuvent saisir des informations, telles que du texte, des sélections et des options, qui peuvent ensuite être envoyées à un serveur pour traitement.

Les formulaires sont un composant fondamental du développement web, permettant l'engagement des utilisateurs et l'échange de données.

Les formulaires HTML ne se limitent pas aux simples saisies de texte. Ils englobent une variété de fonctionnalités et de types de saisie qui améliorent leur fonctionnalité. Les formulaires peuvent inclure des saisies de texte, des champs de mot de passe, des boutons radio, des cases à cocher et des boutons de soumission, entre autres. Ces fonctionnalités vous permettent de collecter et de traiter efficacement les données des utilisateurs.

## L'élément `<form>`

Pour commencer à créer un formulaire, vous utiliserez l'élément `<form>`. Cet élément définit un conteneur pour tous les éléments du formulaire. Voici un exemple de base d'un formulaire :

```html
<form>
  <!-- Les éléments du formulaire iront ici -->
</form>
```

## Saisie de texte

Les champs de saisie de texte sont utilisés pour collecter des données textuelles sur une seule ligne, telles qu'un nom ou une adresse e-mail. Vous pouvez créer un champ de saisie de texte en utilisant l'élément `<input>` avec l'attribut `type` défini sur "text".

```html
<label for="name">Nom :</label>
<input type="text" id="name" name="name" placeholder="Entrez votre nom">
```

Résultat :

<label for="name">Nom :</label>
<input type="text" id="name" name="name" placeholder="Entrez votre nom">

Dans cet extrait de code, l'attribut `for` dans l'élément `<label>` associe l'étiquette au champ de saisie, le rendant plus accessible et convivial.

## Saisie de mot de passe

Les champs de saisie de mot de passe sont similaires aux saisies de texte, mais les caractères saisis sont masqués par des points ou des astérisques pour des raisons de sécurité.

Pour créer un champ de saisie de mot de passe, définissez l'attribut `type` sur "password".

```html
<label for="password">Mot de passe :</label>
<input type="password" id="password" name="password" placeholder="Entrez votre mot de passe">
```

Résultat :

<label for="password">Mot de passe :</label>
<input type="password" id="password" name="password" placeholder="Entrez votre mot de passe">

## Boutons radio

Les boutons radio sont utilisés lorsque vous souhaitez que les utilisateurs sélectionnent une option parmi une liste. Chaque option est représentée par un bouton radio.

Pour créer des boutons radio, utilisez l'élément `<input>` avec l'attribut `type` défini sur "radio".

```html
<form>

    <label>Choisissez votre méthode de paiement préférée :</label>
    <input type="radio" id="creditCard" name="paymentMethod" value="creditCard">
    <label for="creditCard">Carte de crédit</label><br>

    <input type="radio" id="paypal" name="paymentMethod" value="paypal">
    <label for="paypal">PayPal</label><br>

    <input type="radio" id="bitcoin" name="paymentMethod" value="bitcoin">
    <label for="bitcoin">Bitcoin</label><br>
 
</form>
```

Résultat :

<form>

    <label>Choisissez votre méthode de paiement préférée :</label>
    <input type="radio" id="creditCard" name="paymentMethod" value="creditCard">
    <label for="creditCard">Carte de crédit</label><br>

    <input type="radio" id="paypal" name="paymentMethod" value="paypal">
    <label for="paypal">PayPal</label><br>

    <input type="radio" id="bitcoin" name="paymentMethod" value="bitcoin">
    <label for="bitcoin">Bitcoin</label><br>
 
</form>

Dans cet exemple, l'utilisation du même attribut `name` pour les deux boutons radio les regroupe, permettant à l'utilisateur de sélectionner une seule option.

## Cases à cocher

Les cases à cocher sont utilisées lorsque vous souhaitez que les utilisateurs sélectionnent une ou plusieurs options parmi une liste. Chaque option est représentée par une case à cocher.

Pour créer des cases à cocher, utilisez l'élément `<input>` avec l'attribut `type` défini sur "checkbox".

```html
<label>Intérêts :</label>
<input type="checkbox" id="music" name="interest" value="music">
<label for="music">Musique</label>

<input type="checkbox" id="sports" name="interest" value="sports">
<label for="sports">Sports</label>

<input type="checkbox" id="reading" name="interest" value="reading">
<label for="reading">Lecture</label>
```

Résultat :

<label>Intérêts :</label>
<input type="checkbox" id="music" name="interest" value="music">
<label for="music">Musique</label>

<input type="checkbox" id="sports" name="interest" value="sports">
<label for="sports">Sports</label>

<input type="checkbox" id="reading" name="interest" value="reading">
<label for="reading">Lecture</label>

Avec les cases à cocher, les utilisateurs peuvent sélectionner plusieurs options en fonction de leurs préférences.

## Bouton de soumission

Un bouton de soumission est utilisé pour envoyer les données du formulaire au serveur pour traitement. Vous pouvez créer un bouton de soumission en utilisant l'élément `<button>` avec l'attribut `type` défini sur "submit".

```html
<button type="submit">Soumettre</button>
```

Résultat :

<button type="submit">Soumettre</button>

Ce bouton déclenche la soumission du formulaire lorsqu'il est cliqué.

## L'accessibilité compte

Bien que nous ayons discuté des bases, il est crucial d'aborder l'accessibilité des formulaires HTML.

**L'accessibilité** dans le développement web consiste à garantir que tous les utilisateurs, quelles que soient leurs capacités ou leurs handicaps, peuvent percevoir, comprendre, naviguer et interagir avec votre contenu web.

Ce principe s'étend également aux formulaires HTML. Les formulaires accessibles ne sont pas seulement éthiques, mais souvent légalement requis, car de nombreux pays ont établi des normes et des réglementations d'accessibilité web pour promouvoir l'inclusivité.

## Comment créer des formulaires accessibles en HTML

### HTML sémantique

Commencez par utiliser des éléments HTML sémantiques. Par exemple, utilisez l'élément `<form>` pour envelopper votre formulaire, les éléments `<label>` pour étiqueter les champs de formulaire, et les éléments `<input>` avec des attributs `type` appropriés.

La sémantique aide les lecteurs d'écran et autres technologies d'assistance à comprendre le contenu.

### Étiquetage

Associez toujours les champs de formulaire avec des étiquettes en utilisant l'attribut `for` dans l'élément `<label>` et l'attribut `id` dans l'élément `<input>` correspondant. Cela permet aux utilisateurs de lecteurs d'écran d'entendre une étiquette lorsqu'ils se concentrent sur une saisie, fournissant ainsi un contexte et une clarté.

```html
<label for="name">Nom :</label>
<input type="text" id="name" name="name" placeholder="Entrez votre nom">
```

### Texte descriptif

Utilisez des étiquettes claires et concises qui décrivent le but de chaque champ de formulaire. Évitez les étiquettes génériques comme "Champ 1" ou "Saisir les données".

### Accessibilité au clavier

Testez vos formulaires en utilisant uniquement le clavier pour la navigation. Assurez-vous que les utilisateurs peuvent interagir avec les éléments du formulaire, tels que la sélection de boutons radio et de cases à cocher, en utilisant la touche "Tab" et la touche "Entrée".

### Gestion des erreurs

Lorsque l'utilisateur commet une erreur, fournissez des messages d'erreur clairs et utiles. Utilisez l'attribut `aria-invalid` pour indiquer qu'une saisie contient une erreur.

```html
<input type="text" aria-invalid="true" />
```

### Rôles et attributs ARIA

La spécification Accessible Rich Internet Applications (ARIA) fournit des rôles et des attributs pour améliorer l'accessibilité du contenu web.

Par exemple, vous pouvez utiliser `aria-describedby` pour associer un champ à des informations descriptives supplémentaires.

```html
<label for="password">Mot de passe :</label>
<input type="password" id="password" name="password" placeholder="Entrez votre mot de passe" aria-describedby="password-hint">
<div id="password-hint">Le mot de passe doit comporter au moins 8 caractères.</div>
```

Résultat :

<label for="password">Mot de passe :</label>
<input type="password" id="password" name="password" placeholder="Entrez votre mot de passe" aria-describedby="password-hint">
<div id="password-hint">Le mot de passe doit comporter au moins 8 caractères.</div>

### Fieldset et Legend

Si votre formulaire contient des groupes de champs liés, utilisez l'élément `<fieldset>` avec un élément `<legend>` pour fournir un titre au groupe. Cela aide les utilisateurs à comprendre le regroupement des éléments du formulaire.

```html
<fieldset>
  <legend>Informations d'adresse</legend>
  <!-- Les champs d'adresse vont ici -->
</fieldset>
```

### L'expérience inclusive

Créer des formulaires accessibles n'est pas seulement une exigence légale – c'est une opportunité d'offrir une expérience inclusive à tous les utilisateurs.

Lorsque vos formulaires sont conçus en tenant compte de l'accessibilité, vous garantissez que chacun, quelles que soient ses capacités, peut accéder aux informations et aux services que votre site web propose.

Les formulaires HTML accessibles suivent les meilleures pratiques en matière d'étiquetage, de structure, de navigation au clavier et de gestion des erreurs. En tenant compte de ces facteurs, vous pouvez créer des formulaires conviviaux pour tous, y compris les personnes handicapées.

## Réactivité mobile

Dans le monde actuel où le mobile est prioritaire, il est vital de rendre vos formulaires réactifs à diverses tailles d'écran. Testez vos formulaires sur différents appareils pour vous assurer qu'ils fonctionnent et apparaissent correctement sur les plateformes de bureau et mobiles. Le design réactif est essentiel pour offrir une expérience utilisateur positive.

## Mettre le tout ensemble

Maintenant que nous avons couvert divers éléments de formulaire et types de saisie, rassemblons-les dans un formulaire complet. Voici un exemple de formulaire d'inscription simple :

```html
<form>
  <label for="name">Nom :</label>
  <input type="text" id="name" name="name" placeholder="Entrez votre nom"><br>

  <label for="email">Email :</label>
  <input type="text" id="email" name="email" placeholder="Entrez votre email"><br>

  <fieldset>
    <legend>Genre :</legend>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Homme</label>

    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Femme</label>
  </fieldset>

  <fieldset>
    <legend>Intérêts :</legend>
    <input type="checkbox" id="music" name="interest" value="music">
    <label for="music">Musique</label>

    <input type="checkbox" id="sports" name="interest" value="sports">
    <label for="sports">Sports</label>

    <input type="checkbox" id="reading" name="interest" value="reading">
    <label for="reading">Lecture</label>
  </fieldset>

  <label for="password">Mot de passe :</label>
  <input type="password" id="password" name="password" placeholder="Entrez votre mot de passe"><br>

  <button type="submit">Soumettre</button>
</form>
```

Résultat :

<form>
  <label for="name">Nom :</label>
  <input type="text" id="name" name="name" placeholder="Entrez votre nom"><br>

  <label for="email">Email :</label>
  <input type="text" id="email" name="email" placeholder="Entrez votre email"><br>

  <fieldset>
    <legend>Genre :</legend>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Homme</label>

    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Femme</label>
  </fieldset>

  <fieldset>
    <legend>Intérêts :</legend>
    <input type="checkbox" id="music" name="interest" value="music">
    <label for="music">Musique</label>

    <input type="checkbox" id="sports" name="interest" value="sports">
    <label for="sports">Sports</label>

    <input type="checkbox" id="reading" name="interest" value="reading">
    <label for="reading">Lecture</label>
  </fieldset>

  <label for="password">Mot de passe :</label>
  <input type="password" id="password" name="password" placeholder="Entrez votre mot de passe"><br>

  <button type="submit">Soumettre</button>
</form>

Ceci est un formulaire complet avec des saisies de texte, des boutons radio, des cases à cocher, une saisie de mot de passe et un bouton de soumission.

## Conclusion

La création de formulaires en HTML est une compétence essentielle pour le développement web. En utilisant les éléments `<form>`, `<input>` et `<button>`, et en comprenant divers types de saisie, vous pouvez concevoir des formulaires interactifs et conviviaux pour collecter des données auprès des visiteurs de votre site web.

Les formulaires sont un composant critique de l'engagement des utilisateurs, et maîtriser leur création est une étape significative dans le développement web.

Dans cet article, nous avons exploré les bases de la création de formulaires, y compris les saisies de texte et de mot de passe, les boutons radio, les cases à cocher et les boutons de soumission. Maintenant, vous avez les connaissances pour créer et personnaliser des formulaires pour diverses utilisations sur vos sites web.

Commencez à expérimenter et à améliorer vos applications web avec des formulaires dès aujourd'hui :)