---
title: Comment créer un formulaire email Bootstrap avec ReCaptcha et PHP en 30 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T08:38:25.000Z'
originalURL: https://freecodecamp.org/news/build-a-bootstrap-form-with-recaptcha-and-php-backend-for-emails-in-30-minutes-17964a374819
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-rFtK5Bs2Y2Ugvib.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer un formulaire email Bootstrap avec ReCaptcha et PHP en 30
  minutes
seo_desc: 'By Ondrej Svestka

  In this tutorial, I will show you how to easily and quickly add a captcha to your
  Bootstrap form to prevent spam. We will be using Google’s ReCaptcha, the most popular
  Captcha solution today.

  As a base, I will be using an HTML conta...'
---

Par Ondrej Svestka

Dans ce tutoriel, je vais vous montrer comment ajouter facilement et rapidement un **captcha à votre formulaire Bootstrap pour prévenir le spam**. Nous utiliserons **ReCaptcha de Google**, la solution Captcha la plus populaire aujourd'hui.

Comme base, j'utiliserai [un **formulaire de contact HTML**](https://bootstrapious.com/p/how-to-build-a-working-bootstrap-contact-form) avec le backend PHP **d'un de mes tutoriels précédents**. Vous pouvez l'utiliser avec n'importe quel autre formulaire Bootstrap que vous avez.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-rFtK5Bs2Y2Ugvib.png)

Notre formulaire utilisera la syntaxe **HTML5** agrémentée de quelques éléments **Bootstrap** et d'un **validateur JavaScript**.

**Nous le soumettrons via AJAX** (la page ne se rechargera pas), puis nous traiterons les valeurs du formulaire avec PHP.

Et enfin, nous enverrons un email avec PHP et retournerons une réponse à la page d'origine qui sera affichée dans un message d'état au-dessus du formulaire.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Lm6jtqIQlaFNeeXU.gif)
_Ce sera le résultat. Voir aussi la démo [en direct](https://bootstrapious.com/tutorial/recaptcha/" rel="noopener" target="_blank" title=")._

Comme je l'ai mentionné précédemment, je me concentrerai principalement sur **l'utilisation de ReCaptcha** aujourd'hui et pas trop sur le formulaire Bootstrap lui-même. Donc, si vous l'avez manqué, jetez au moins [un rapide coup d'œil à mon tutoriel sur le formulaire Bootstrap](https://bootstrapious.com/p/how-to-build-a-working-bootstrap-contact-form).

#### Démo & Liens

* [Voir la démo](https://bootstrapious.com/tutorial/recaptcha/)
* ou [télécharger les fichiers](https://bootstrapious.com/p/bootstrap-recaptcha#demo-and-links) pour le tutoriel

**D'accord, commençons !**

### 1. Inscrire votre site

Pour pouvoir utiliser ReCaptcha, vous devrez d'abord **inscrire votre site web** sur le [site de ReCaptcha](https://www.google.com/recaptcha/admin).

![Image](https://cdn-media-1.freecodecamp.org/images/0*GRk4rP9nglbHOw7V.png)

Après une inscription réussie, vous obtiendrez **une paire de clés** à utiliser avec votre ReCaptcha. Laissez la page ouverte ou copiez les clés dans un fichier texte, nous en aurons besoin bientôt.

![Image](https://cdn-media-1.freecodecamp.org/images/0*G0dDkucp15TJJFNa.png)

### 2. HTML

Nous utiliserons le modèle de formulaire de contact du [tutoriel précédent](https://bootstrapious.com/p/how-to-build-a-working-bootstrap-contact-form) + nous ajouterons un élément reCAPTCHA et une entrée cachée à côté pour nous aider avec la validation JavaScript.

**Expliquons un peu le code HTML :**

* nous avons un formulaire de contact HTML prêt écrit avec le balisage Bootstrap
* les principaux scripts et feuilles de style tiers qui seront utilisés sont : jQuery, Bootstrap 4, CSS et JavaScript

**Pour ajouter un ReCaptcha à votre formulaire, vous avez juste besoin :**

* d'inclure `<div class="g-recaptcha" data-sitekey="6LfKURIUAAAAAO50vlwWZkyK_G2ywqE52NU7YO0S">`</div>à l'endroit où vous en avez besoin dans votre formulaire (remplacez la clé du site par votre propre clé de la première étape)
* Inclure le JS ReCaptcha pour initialiser ReCaptcha sur la page — `<script src='https://www.google.com/recaptcha/api.js'><`;/script>
* J'utilise également les attributs `data-callback` et `data-expired-callback` sur la div `g-recaptcha` — ceux-ci sont optionnels et je les utiliserai pour faire coopérer ReCaptcha avec le validateur

**Voici le code complet du formulaire**

### 3. PHP

En PHP, nous utiliserons la [bibliothèque cliente de Google](https://github.com/google/recaptcha) qui prendra en charge la vérification.

Vous pouvez utiliser Composer pour l'installer dans votre projet, la télécharger depuis GitHub ou simplement utiliser la version que j'ai incluse dans le [package de téléchargement](https://bootstrapious.com/tutorial/files/recaptcha.zip).

La majeure partie du code provient également de mon tutoriel précédent, donc je vais essayer de le résumer brièvement.

**Nommons le fichier** `contact.php` **et voyons ce que nous allons faire dans celui-ci :**

* au début, nous devons inclure la bibliothèque PHP ReCaptcha — `require('recaptcha-master/src/autoload.php');`
* et faire quelques configurations, par exemple entrer votre clé secrète — `$recaptchaSecret = 'YOUR_SECRET_KEY';`
* Nous définissons également les variables supplémentaires telles que les emails pour envoyer l'email, le sujet et les messages de succès/erreur
* puis, vous devrez initialiser la classe avec votre clé secrète - `$recaptcha = new \ReCaptcha\ReCaptcha($recaptchaSecret);`
* envoyer un appel pour valider le ReCaptcha — `$response = $recaptcha->verify($_POST['g-recaptcha-response'], $_SERVER['REMOTE_ADDR'`]);
* lever une exception si la validation échoue — `if (!$response->isSuccess()) {.`..}
* le script compose ensuite le message email, l'envoie et retourne une réponse JSON. _(Le formulaire est soumis par AJAX par défaut.)_

### 4. JavaScript

Notre fichier JavaScript `contact.js` prendra en charge :

* **la validation des entrées** avec le [validateur Bootstrap](http://1000hz.github.io/bootstrap-validator/)
* la gestion des **rappels JS de ReCaptcha** _(nous remplirons l'entrée cachée_ `input[data-recaptcha]` _en fonction de la réponse de ReCaptcha. Si elle est réussie, nous remplissons cette entrée = le validateur considérera le formulaire comme valide.)_
* **l'envoi AJAX du formulaire**
* et enfin, **l'affichage du message de succès ou d'erreur** et également la vidange du formulaire.

**Voici le code :**

### 5. Résultat

C'est tout !

Vous devriez maintenant avoir un formulaire de contact Bootstrap fonctionnel avec ReCaptcha et un arrière-plan PHP.

#### Merci pour les 50 applaudissements ? si vous avez aimé cet article ! **Consultez également mes autres [tutoriels Bootstrap](https://bootstrapious.com/tutorials) ou mes [modèles Bootstrap](https://bootstrapious.com/free-templates).**

_Publié à l'origine sur le [blog Bootstrapious](https://bootstrapious.com/p/bootstrap-recaptcha)._

### À propos de l'auteur

Ondrej Svestka est un passionné de Bootstrap et de front-end et fondateur de [Bootstrapious](https://bootstrapious.com/).