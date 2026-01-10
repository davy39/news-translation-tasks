---
title: Validation des données – Comment vérifier les entrées utilisateur sur les formulaires
  HTML avec un exemple de code JavaScript
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2021-01-18T17:56:53.000Z'
originalURL: https://freecodecamp.org/news/form-validation-with-html5-and-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6003768298be260817e4aadc.jpg
tags:
- name: Form validations
  slug: form-validations
- name: HTML5
  slug: html5
- name: JavaScript
  slug: javascript
seo_title: Validation des données – Comment vérifier les entrées utilisateur sur les
  formulaires HTML avec un exemple de code JavaScript
seo_desc: "Forms are ubiquitous in web applications. Some apps use forms to collect\
  \ data to sign up users and provide an email address. Others use them to fulfill\
  \ online transactions to facilitate a shopping experience. \nYou might use some\
  \ web forms to apply fo..."
---

Les formulaires sont omniprésents dans les applications web. Certaines applications utilisent des formulaires pour collecter des données afin d'inscrire des utilisateurs et fournir une adresse e-mail. D'autres les utilisent pour effectuer des transactions en ligne afin de faciliter une expérience d'achat. 

Vous pouvez utiliser certains formulaires web pour demander un nouveau prêt automobile, tandis que vous utiliserez d'autres pour commander une pizza pour le dîner. Il est donc important que les données collectées à partir de ces formulaires soient nettoyées, correctement formatées et exemptes de tout code malveillant. Ce processus est appelé validation de formulaire.

Nous avons besoin de la validation de formulaire chaque fois que nous acceptons une entrée utilisateur. Nous devons nous assurer que les données saisies sont dans le bon format, se situent dans une plage de données valide (comme pour les champs de date) et ne contiennent pas de code malveillant qui pourrait conduire à des injections SQL. Des données malformées ou manquantes peuvent également provoquer des erreurs dans l'API.

## Quels sont les différents types de validations de formulaire ?

La validation de formulaire peut se faire côté client et côté serveur.

La validation côté client se fait en utilisant les attributs HTML5 et JavaScript côté client. 

Vous avez peut-être remarqué que dans certains formulaires, dès que vous entrez une adresse e-mail invalide, le formulaire affiche une erreur "Veuillez entrer une adresse e-mail valide". Ce type de validation immédiate est généralement effectué via JavaScript côté client.

![Erreur de validation pour un numéro de carte de crédit incorrect](https://www.freecodecamp.org/news/content/images/2021/04/form-validation-cc.gif)

Dans d'autres cas, vous avez peut-être remarqué que lorsque vous remplissez un formulaire et entrez des détails tels qu'une carte de crédit, il peut afficher un écran de chargement puis afficher une erreur "Cette carte de crédit est invalide". 

Ici, le formulaire a fait appel à son code côté serveur et a retourné une erreur de validation après avoir effectué des vérifications supplémentaires sur la carte de crédit. Ce cas de validation où un appel côté serveur est effectué est appelé validation côté serveur.

## Quelles données doivent être validées ?

La validation de formulaire est nécessaire chaque fois que vous acceptez des données d'un utilisateur. Cela peut inclure :

1. Validation du format des champs tels que l'adresse e-mail, le numéro de téléphone, le code postal, le nom, le mot de passe.
2. Validation des champs obligatoires
3. Vérification du type de données tel que chaîne de caractères vs nombre pour des champs tels que le numéro de sécurité sociale.
4. S'assurer que la valeur entrée est une valeur valide telle que le pays, la date, et ainsi de suite.

## Comment configurer la validation côté client

Côté client, la validation peut être effectuée de deux manières :

1. En utilisant les fonctionnalités HTML5
2. En utilisant JavaScript


### Comment configurer la validation avec les fonctionnalités HTML5

HTML5 fournit un ensemble d'attributs pour aider à valider les données. Voici quelques cas de validation courants :

- Rendre les champs obligatoires en utilisant `required`
- Contraindre la longueur des données :
  - `minlength`, `maxlength` : pour les données textuelles
  - `min` et `max` pour la valeur maximale du type num
- Restreindre le type de données en utilisant `type` :
  - `<input type="email" name="multiple>`
- Spécifier des motifs de données en utilisant `pattern` :
  - spécifie un motif regex que les données du formulaire entrées doivent correspondre

Lorsque la valeur d'entrée correspond à la validation HTML5 ci-dessus, elle reçoit une pseudo-classe `:valid`, et `:invalid` si ce n'est pas le cas.

Essayons un exemple :

```HTML
<form>
<label for="firstname"> Prénom : </label>
<input type="text" name="firstname" id="firstname" required maxlength="45">
<label for="lastname"> Nom : </label>
<input type="text" name="lastname" id="lastname" required maxlength="45">
<button>Soumettre</button>
</form>
```

![Validation côté client des champs obligatoires en utilisant les attributs HTML5](https://www.freecodecamp.org/news/content/images/2021/04/form-validation-required.png)


[Lien vers JSFiddle](https://jsfiddle.net/58xc2qyj/)

Ici, nous avons deux champs obligatoires - Prénom et Nom. Essayez cet exemple dans JSFidle. Si vous sautez l'un de ces champs et appuyez sur soumettre, vous obtiendrez un message, "Veuillez remplir ce champ". Ceci est une validation utilisant HTML5 intégré.


### Comment configurer la validation en utilisant JavaScript

Lors de la mise en œuvre de la validation de formulaire, il y a quelques points à considérer :

1. Qu'est-ce qui est défini comme des données "valides" ? Cela vous aide à répondre aux questions sur le format, la longueur, les champs obligatoires et le type de données.
2. Que se passe-t-il lorsque des données invalides sont entrées ? Cela vous aidera à définir l'expérience utilisateur de la validation - que ce soit pour afficher un message d'erreur en ligne ou en haut du formulaire, à quel point le message d'erreur doit être détaillé, le formulaire doit-il être soumis de toute façon, doit-il y avoir des analyses pour suivre le format invalide des données ? Et ainsi de suite.

Vous pouvez effectuer la validation JavaScript de deux manières :

1. Validation en ligne en utilisant JavaScript
1. API de validation de contrainte HTML5

#### Validation en ligne en utilisant JavaScript

```html
<form id="form">
  <label for="firstname"> Prénom* </label>
  <input type="text" name="firstname" id="firstname" />
  <button id="submit">Soumettre</button>

  <span role="alert" id="nameError" aria-hidden="true">
    Veuillez entrer le Prénom
  </span>
</form>
```

```javascript
const submit = document.getElementById("submit");

submit.addEventListener("click", validate);

function validate(e) {
  e.preventDefault();

  const firstNameField = document.getElementById("firstname");
  let valid = true;

  if (!firstNameField.value) {
    const nameError = document.getElementById("nameError");
    nameError.classList.add("visible");
    firstNameField.classList.add("invalid");
    nameError.setAttribute("aria-hidden", false);
    nameError.setAttribute("aria-invalid", true);
  }
  return valid;
}
```

```css
#nameError {
  display: none;
  font-size: 0.8em;
}

#nameError.visible {
  display: block;
}

input.invalid {
  border-color: red;
}
```

[Lien vers JSFiddle](https://jsfiddle.net/0tq3e49w/4/)

Dans cet exemple, nous vérifions les champs obligatoires en utilisant JavaScript. Si un champ obligatoire est absent, nous utilisons CSS pour afficher le message d'erreur. 

Les libellés Aria sont modifiés en conséquence pour signaler une erreur. En utilisant CSS pour afficher/masquer une erreur, nous réduisons le nombre de manipulations DOM que nous devons faire. Le message d'erreur est fourni en contexte, rendant ainsi l'expérience utilisateur intuitive.

#### API de validation de contrainte HTML5

Les attributs HTML `required` et `pattern` peuvent aider à effectuer une validation de base. Mais si vous souhaitez une validation plus complexe ou fournir des messages d'erreur détaillés, vous pouvez utiliser l'API de validation de contrainte. 

Certaines méthodes fournies par cette API sont :

1. `checkValidity`
2. `setCustomValidity`
3. `reportValidity`

Les propriétés suivantes sont utiles :

1.  `validity`
2.  `validationMessage`
3.  `willValidate`


Dans cet exemple, nous allons valider en utilisant les méthodes intégrées HTML5 telles que `required` et `length` en conjonction avec l'API de validation de contrainte pour fournir des messages d'erreur détaillés.

```HTML
<form>
<label for="firstname"> Prénom : </label>
<input type="text" name="firstname" required id="firstname">
<button>Soumettre</button>
</form>
```

```javascript
const nameField = document.querySelector("input");

nameField.addEventListener("input", () => {
  nameField.setCustomValidity("");
  nameField.checkValidity();
  console.log(nameField.checkValidity());
});

nameField.addEventListener("invalid", () => {
  nameField.setCustomValidity("Veuillez remplir votre Prénom.");
});
```

[Lien vers JSFiddle](https://jsfiddle.net/xz2wjLck/1/)

## N'oubliez pas la validation côté serveur

La validation côté client n'est pas la seule vérification de validation que vous devez effectuer. Vous devez également valider les données reçues de votre client dans le code côté serveur pour vous assurer que les données correspondent à ce que vous attendez. 

Vous pouvez également utiliser la validation côté serveur pour effectuer des vérifications de logique métier qui ne doivent pas résider côté client.

## Bonnes pratiques de validation de formulaire

1. Ayez toujours une validation côté serveur, car des acteurs malveillants peuvent contourner la validation côté client.
2. Fournissez des messages d'erreur détaillés en contexte avec le champ qui a produit l'erreur.
3. Fournissez un exemple de ce à quoi les données doivent ressembler en cas de message d'erreur, tel que - "L'e-mail ne correspond pas au format - test@example.com"
4. Évitez d'utiliser des pages d'erreur uniques qui impliquent une redirection. Cela offre une mauvaise expérience utilisateur et force l'utilisateur à revenir à une page précédente pour corriger le formulaire et perdre le contexte.
5. Marquez toujours les champs obligatoires.



### Intéressé par plus de tutoriels et d'articles comme celui-ci ? [Inscrivez-vous à ma newsletter.](https://tinyletter.com/shrutikapoor) ou [suivez-moi sur Twitter](https://twitter.com/shrutikapoor08)