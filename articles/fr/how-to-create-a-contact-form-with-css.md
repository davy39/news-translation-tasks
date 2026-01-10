---
title: Comment créer un formulaire de contact avec CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-29T00:41:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-contact-form-with-css
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d52740569d1a4ca3720.jpg
tags:
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
seo_title: Comment créer un formulaire de contact avec CSS
seo_desc: 'First we create the HTML elements - input fields for First Name, Last Name,
  Email and a Text Area for the message.

  Later we apply CSS styles to make the form visually appealing.

  The HTML part

  The HTML section has a div with class container with the h...'
---

Tout d'abord, nous créons les éléments HTML - des champs de saisie pour le Prénom, le Nom, l'Email et une zone de texte pour le message.

Ensuite, nous appliquons des styles CSS pour rendre le formulaire visuellement attrayant.

### **La partie HTML**

La section HTML contient une div avec la classe `container` et le titre `h3` « **Formulaire de Contact** »

Le formulaire avec le nom **contact_form** contient des champs de saisie pour :

* Prénom
* Nom
* Email
* Message

Une div avec la classe `center` pour aligner les éléments au centre. Un `input` de type `submit` pour soumettre le formulaire.  
L'attribut `required` dans les champs de texte est vérifié pour la valeur lors de la soumission.

```html
<div class="container">
	<h3>Formulaire de Contact</h3>
	<form action="#" name="contact_form">
		<label for="first_name">Prénom</label>
		<input name="first_name" type="text" required placeholder="John"/>
		<br>
		<label for="last_name">Nom</label>
		<input name="last_name" type="text" required placeholder="Doe"/>
		<br>
		<label for="email">Email</label>
		<input name="email" type="email" required placeholder="vous@domaine.com"/>
		<br>
		<label for="message">Message</label><br>
		<textarea name="message" cols="30" rows="10" placeholder="Entrez votre message ici ..." required> </textarea>
		<div class="center">
			<input type="submit" value="Soumettre">
		</div>
	</form>	
</div>
```

### **La partie CSS**

```css
/* Importation de la police Roboto depuis Google Fonts. */
@import url("https://fonts.googleapis.com/css?family=Roboto:400");

/* Définir la police de tous les éléments sur 'Roboto' */
* {
	font-family: 'Roboto', sans-serif;
	font-weight: 400;
}

/* Supprimer le contour de tous les éléments au focus */
*:focus {
	outline: 0;
}

body {
	background: #263238;  /* Définir la couleur de fond sur #263238*/
}

h3 {
	text-align: center;
}

/* Ajouter des styles à la classe 'container' */
.container {
	padding: 12px 24px 24px 24px;
	margin: 48px 12px;
	background: #E3F2FD;
	border-radius: 4px;
}

/* Ajouter des styles au sélecteur 'label' */
label {
	font-size: 0.85em;
	margin-left: 12px;
}

/* Ajouter des styles aux sélecteurs 'input' et 'textarea' */
input[type=text],input[type=email], textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px;
    resize: vertical;
}

/* Ajouter des styles pour montrer le 'focus' du sélecteur */
input[type=text]:focus,input[type=email]:focus, textarea:focus {
	border: 1px solid green;
}

/* Ajouter des styles au bouton de soumission */
input[type=submit] {
	background: #64B5F6;
	margin: 0 auto;
	outline: 0;
	color: white;
	border: 0;
	padding: 12px 24px;
	border-radius: 4px;
	transition: all ease-in-out 0.1s;
	position: relative;
	display: inline-block;
	text-align: center;
}

/* Ajouter des styles pour la propriété 'focus' */
input[type=submit]:focus {
	background: #A5D6A7;
	color: whitesmoke;
}

/* Styliser la propriété 'hover' */
input[type=submit]:hover {
	background: #2196F3;
}

/* Aligner les éléments au centre de la 'div' avec la classe 'center' */
.center {
	text-align: center;
}
```

### **Résultat**

![FreeCodeCamp/guides - Formulaire de Contact](http://res.cloudinary.com/crack-jack/image/upload/v1508434398/FCC_Github_Contact_form.png)

### **Plus d'informations :**

Visitez le [FreeCodeCamp - Formulaire de Contact](https://codepen.io/rakhi2104/pen/QqYOoe/) sur [Codepen.io](https://codepen.io/)