---
title: Terminé avant même d'avoir commencé — comment éviter les rebonds des emails
  mal saisis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T18:25:09.000Z'
originalURL: https://freecodecamp.org/news/over-before-it-started-how-to-not-bounce-mistyped-user-emails-69be32408f21
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2Oo1Din32plTMdI8GypK4Q.jpeg
tags:
- name: marketing
  slug: marketing
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: writing
  slug: writing
seo_title: Terminé avant même d'avoir commencé — comment éviter les rebonds des emails
  mal saisis
seo_desc: 'By Alex Peterson

  I type my email address so much that it has become muscle memory. Whenever I sign
  up for a newsletter or make a new account on a website, that’s what I use. And I
  barely, if ever, double-check to see that the address I typed is actua...'
---

Par Alex Peterson

Je saisis mon adresse email si souvent que cela est devenu un réflexe. Chaque fois que je m'inscris à une newsletter ou que je crée un nouveau compte sur un site web, c'est ce que j'utilise. Et je vérifie à peine, si jamais, que l'adresse que j'ai saisie est réellement correcte.

Et si mes doigts glissent, ou si je rate une touche ?

Ce n'est pas un événement rare. C'est un gros problème pour les sites web qui dépendent d'une adresse email pour vérifier les nouveaux utilisateurs. Mais c'est un problème encore plus grand pour les sites web qui ne dépendent pas de la vérification des adresses email.

Cela entraîne le renvoi des emails envoyés par les entreprises.

Le taux de "rebond dur" est le nombre d'adresses email invalides envoyées en pourcentage des adresses email valides.

### Quelle est l'ampleur du problème ?

Selon les [recherches](https://mailchimp.com/resources/research/email-marketing-benchmarks/) de MailChimp, le taux de "rebond dur" pour les entreprises envoyant des emails peut atteindre **plus de 1 %**, tandis que le taux moyen est de **0,53 %**. Ces chiffres peuvent ne pas sembler élevés, mais les rebonds peuvent s'accumuler.

Pensez aux emails suivants que vous pourriez envoyer à vos clients,

* email de bienvenue
* email de vérification
* campagne de drip marketing
* annonces de produits
* notifications d'activité
* alertes d'erreur de l'application
* revues hebdomadaires de blog

Et la liste continue...

À mesure que votre site web ou votre application se développe, le nombre d'emails renvoyés augmente également.

Les emails renvoyés de manière constante commenceront à nuire à votre réputation en tant qu'expéditeur. Cela rendra moins probable le fait que les futurs emails que vous envoyez soient considérés comme fiables.

Et vous ne pouvez pas envoyer un email à un utilisateur pour lui demander de corriger ses informations dans votre base de données si vous... ne pouvez pas le joindre.

Sauf si vous avez établi un canal de communication secondaire _au préalable_, les utilisateurs qui s'inscrivent avec une adresse email invalide risquent d'être perdus à jamais.

Nous devrions régler ce problème.

#### Que peut-on faire ?

En général, il est déconseillé de modifier les saisies d'un utilisateur sans qu'il en soit informé.

Pour une chose, aucune machine n'est parfaite à 100 % pour deviner ce que les [humains](https://www.youtube.com/watch?v=-DSVDcw6iW8) veulent réellement. Mais encore, si vous voyez quelque chose, dites-le.

J'ai constaté que donner aux utilisateurs une suggestion douce lorsque l'application remarque que quelque chose est _probablement_ incorrect tend à être bien accueilli. Cette règle de base a bien fonctionné dans un ancien emploi en startup et dans la startup que je construis actuellement.

Sur mon [site web pour les ateliers d'écriture en ligne](https://www.penmob.com), il y a un simple plugin qui aide à prévenir les fautes de frappe lorsque un utilisateur s'inscrit avec son adresse email :

Vous pouvez l'essayer vous-même sur la [page de connexion](https://www.penmob.com/login). Je vais vous montrer comment configurer cela sur votre propre site web.

#### Les détails techniques

Cet article suppose que vous utilisez [Browserify](https://medium.com/@christopherphillips_88739/a-beginners-guide-to-browserify-1170a724ceb2), [webpack](https://webpack.js.org/), ou quelque chose de similaire pour construire des packages NPM sur le front-end de votre site web. Par exemple, Penmob utilise l'installation [VueJS webpack](https://vuejs.org/v2/guide/installation.html#CLI).

Tout d'abord, installez le [package Mistyep](https://www.npmjs.com/package/mistyep) :

```
npm install mistyep --save
```

Ensuite, ajoutez-le à votre page de connexion/inscription :

```
var mistyep = require('mistyep');
```

Mistyep est un package qui vérifie les saisies de vos utilisateurs par rapport aux fournisseurs d'email les plus courants. Le code suivant garantit qu'une personne qui fait une faute de frappe en tapant "gnail" au lieu de "gmail" peut toujours se connecter.

```
<input type="email" id="emailInput" />
```

```
<!-- ... -->
```

```
<script>// Obtenez la saisie de l'email de l'utilisateur à partir du formulaire de connexion.var emailInput = document.getElementById('emailInput').value;
```

```
// Mistyep retourne la valeur originale si aucune correction n'est trouvée.var correctedEmail = mistyep.email(emailInput);
```

```
if (emailInput !== correctedEmail) {  // suggérez l'orthographe alternative à l'utilisateur.}</script>
```

C'est à vous de décider comment présenter la suggestion à l'utilisateur. Dans le GIF ci-dessus, lorsque `emailInput` n'est pas égal à `correctedEmail`, j'affiche une boîte. La boîte contient le texte `Vouliez-vous dire {{ correctedEmail }} ?`. En cliquant sur cette boîte, le champ `emailInput` original est défini comme étant égal à `correctedEmail`, ce qui masque ensuite la boîte.

Notez qu'il faut un clic manuel de l'utilisateur pour appliquer réellement la suggestion dans cet exemple. Vous allez rencontrer des problèmes assez rapidement en mettant à jour automatiquement vos enregistrements de base de données avec les suggestions que Mistyep trouve.

Vous pouvez également utiliser Mistyep pour vérifier par rapport à une liste arbitraire de mots — pas seulement des adresses email. N'hésitez pas à consulter l'[exemple de code](https://www.npmjs.com/package/mistyep#for-custom-words) et à essayer la [démo en direct](https://penmob.github.io/mistyep/).

#### Gardez cela simple

Valider les adresses email est un [trou noir](http://emailregex.com/) dans lequel je ne recommande pas de s'aventurer trop loin. Mistyep ne peut pas attraper chaque erreur possible (rien ne le peut). Mais il fournira la bonne suggestion aux utilisateurs qui font une faute de frappe dans leur adresse email pour la grande majorité des cas.

J'espère que vous trouverez cela utile pour votre propre application ou site web. Je publie des insights techniques, des conseils d'écriture et des annonces de produits sur [Twitter](https://twitter.com/pen_mob). Pour des mises à jour (peu fréquentes), [suivez-moi](https://twitter.com/pen_mob). Bonne construction !