---
title: Comment les retours des utilisateurs ont amélioré la sécurité de mon application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-09T18:37:46.000Z'
originalURL: https://freecodecamp.org/news/how-user-feedback-improved-my-apps-security-53eb11977880
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Sk4M13Bb8Sh3P1VL.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Comment les retours des utilisateurs ont amélioré la sécurité de mon application
seo_desc: 'By Ethan Ryan

  Getting published on freeCodeCamp’s Medium publication was super exciting.

  The week my post was accepted, I was busy with work and headed out of town for the
  weekend, so I didn’t get a chance to check Medium for a few days. I’d gotten s...'
---

Par Ethan Ryan

Être publié sur [la publication Medium de freeCodeCamp](https://medium.freecodecamp.org/) était super excitant.

La semaine où [mon article](https://medium.freecodecamp.org/how-to-surprise-your-apps-users-by-hiding-easter-eggs-in-the-console-3b6e9285e7e7) a été accepté, j'étais occupé avec le travail et je partais en ville pour le week-end, donc je n'ai pas eu l'occasion de vérifier Medium pendant quelques jours. J'avais reçu quelques notifications par e-mail, et j'étais excité à l'idée de rattraper les réponses à [mon article](https://medium.freecodecamp.org/how-to-surprise-your-apps-users-by-hiding-easter-eggs-in-the-console-3b6e9285e7e7) quand j'en aurais l'occasion.

![Image](https://cdn-media-1.freecodecamp.org/images/v0ypDXKM2V2tnU70O6qrejSXM9DEd0b3UhWF)
_Notifications Medium_

Super ! Ce grand cercle vert signifiait des applaudissements ! De nouveaux abonnés ! Des gens lisaient mes mots et découvraient mon application de générateur d'histoires ! C'était génial !

Puis j'ai lu les messages.

![Image](https://cdn-media-1.freecodecamp.org/images/7JVfMXKsZ6pCZ7TGtm-h1-5dJEUQemMqBpL0)
_commentaire un_

Oh-oh, spaghetti-os.

![Image](https://cdn-media-1.freecodecamp.org/images/lrcyUuw6DTmxBiTOr7jMrcnBKOHm6ExjIRHE)
_commentaire deux_

Pas bon.

![Image](https://cdn-media-1.freecodecamp.org/images/a-ofyiUOaAunD3bHVbuYm9bzinFfvHzodIBw)
_commentaire 3_

Hmm, ça a du sens.

![Image](https://cdn-media-1.freecodecamp.org/images/RFAm14hs1xKedDqRWmGVCEcU2sTq0MPrvUHZ)
_commentaire 4_

Aïe !

À vrai dire, je n'avais jamais vérifié l'onglet Réseau dans les outils de développement de Chrome 🙆.

Je passe beaucoup de temps dans la console du navigateur, à lire mes logs, avertissements et erreurs, mais pas beaucoup de temps avec les autres options des outils de développement.

Ces commentaires étaient super utiles et m'ont fait réaliser que j'avais du travail à faire.

Pour résumer jusqu'à présent :

* **Bonne nouvelle** : [WordNerds](http://wordnerds.co) avait de nouveaux utilisateurs ! :)
* **Mauvaise nouvelle** : Les méchants pouvaient toujours voir une liste de tous mes utilisateurs et leurs adresses e-mail :/

Tout ce que quelqu'un avait à faire pour trouver les adresses e-mail de tous mes utilisateurs était d'aller sur wordnerds.co, d'ouvrir la console, de cliquer sur Réseau et d'aller à : [https://word-nerds-api.herokuapp.com/users](https://word-nerds-api.herokuapp.com/users)

Ils verraient ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/01-PJrx5GmmzwYfkteS8-BY9vOgM5Bl0b7fx)
_Point de terminaison de l'API /users de WordNerds_

> Note : Mes premiers utilisateurs n'avaient pas d'adresses e-mail stockées dans la base de données car ils s'étaient inscrits à WordNerds avant que je ne fasse des adresses e-mail des attributs obligatoires via l'authentification frontend.

En parcourant ce point de terminaison de l'API, j'ai également remarqué un autre problème qui devait être corrigé :

![Image](https://cdn-media-1.freecodecamp.org/images/MNjse84v41BnzDGf-j4zifMguGqc7K4lvDTf)
_nom d'utilisateur lorem ipsum_

Oups. Mon attribut de nom d'utilisateur n'avait aucune limite de longueur de chaîne. Ou si c'était le cas, cette limite était trop élevée. Le nom d'utilisateur de personne n'a besoin d'être aussi long.

Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/bLLS-ev9iBj7Puum5QGlvMUXEEb1DPwl0oAw)
_nom d'utilisateur Navy Seal Copypasta, grossièretés floutées_

Jésus Marie. Comment quelqu'un pourrait-il se souvenir de coller [le Navy Seal Copypasta](https://knowyourmeme.com/memes/navy-seal-copypasta) pour se connecter à WordNerds ?!

Quelle galère. Je ne voulais pas donner à mes utilisateurs une mauvaise expérience utilisateur, en attendant d'eux qu'ils se souviennent de copier et coller tout ce copypasta.

Les champs de saisie de nom d'utilisateur sont comme les enfants : ils ont besoin de limites.

J'avais donc du travail à faire.

1. Je devais protéger les adresses e-mail de mes utilisateurs. _Encore_. Je pensais avoir corrigé cela la dernière fois, mais j'avais tort.
2. Je devais limiter le nombre de caractères d'un nom d'utilisateur.
3. Comme mes commentateurs utiles l'avaient souligné, je ne devais récupérer que les données absolument nécessaires depuis le backend pour chaque point de terminaison de l'API. Je renvoyais trop de données, ce qui était mauvais pour des raisons de sécurité et de performance. Je devais protéger les données de mes utilisateurs **et** limiter la quantité de données renvoyées pour chaque appel d'API.

Cool cool cool. Travail travail travail. Il est temps de se mettre au travail.

#### Protéger les données des utilisateurs

Mon premier et plus urgent problème : m'assurer que je ne journalisais pas tous les noms et adresses e-mail de mes utilisateurs vers mon point de terminaison de l'API /users en JSON.

Il y avait plusieurs façons de corriger cela, et après réflexion, j'ai choisi l'approche la plus évidente et la plus facile, si évidente et facile que j'étais surpris de ne pas l'avoir réalisée plus tôt. Je n'avais absolument aucun besoin d'un point de terminaison d'API pour tous les utilisateurs. Je pouvais donc simplement supprimer cet appel d'API du frontend, et la méthode Rails correspondante sur le backend.

J'aimais bien montrer le nombre total d'utilisateurs dans le composant Metadata de mon application. C'était juste un simple nombre, mais j'aimais le voir grandir lentement à mesure que plus de personnes s'inscrivaient sur mon site.

J'ai donc décidé de garder ce nombre, **et** d'éliminer toutes ces données utilisateur apparaissant sur le point de terminaison de l'API.

J'ai gardé l'appel d'API exactement le même sur le frontend, et sur le backend Ruby on Rails, j'ai changé la méthode index dans le UserController de ceci :

```
def index   users = User.all   render json: usersend
```

à ceci :

```
def index   users = User.all.size   render json: usersend
```

> Note : J'aurais pu utiliser `length` ou `count` au lieu de `size`, mais `size` est le meilleur choix selon [ce post StackOverflow](https://stackoverflow.com/questions/14794492/which-is-faster-count-or-length).

Maintenant, au lieu de renvoyer un tableau rempli d'objets utilisateur, contenant des noms d'utilisateur et des adresses e-mail, mon backend renvoie simplement un nombre.

### AVANT :

![Image](https://cdn-media-1.freecodecamp.org/images/pgjW8cW1-EJkFlQ9Sitdmltrf-nbaaJ55L-f)
_Point de terminaison de l'API /users — AVANT_

### APRÈS :

![Image](https://cdn-media-1.freecodecamp.org/images/CSVl2iG9jXMEA9KXbD2Hl-sXlWnNVAdKO8Fk)
_Point de terminaison de l'API /users — APRÈS_

Waouh ! Quelle transformation incroyable !

Après ce changement sur le backend, j'ai apporté quelques modifications mineures au frontend. Au lieu de rendre `props.users.length` dans mon composant Metadata, je pouvais simplement rendre `props.users`. Et je pouvais changer ce nom dans l'état du conteneur de `this.state.users` à `this.state.userCount`. Des mises à jour faciles.

Plus de données utilisateur dans mon point de terminaison d'API accessible au public !

Eh bien, mes noms d'utilisateur et adresses e-mail étaient toujours accessibles via le point de terminaison /stories, donc je devais encore corriger cela. Mais cela pourrait être traité bientôt.

#### Limiter la longueur du nom d'utilisateur

Je n'aimais pas voir qu'un nom d'utilisateur pouvait être aussi long que le Navy Seal Copypasta, et bien que ce soit fou que quelqu'un essaie même de rendre son nom aussi long, je suis content qu'ils l'aient fait, car maintenant je pouvais corriger ce problème !

Merci, à celui qui a rendu son nom d'utilisateur WordNerds si long. Je vous regarde, Lorem Ipsum et Navy Seal Copypasta.

J'avais déjà quelques validations sur mon frontend pour m'assurer que les utilisateurs se connectant ou s'inscrivant à WordNerds avaient des noms d'utilisateur et des mots de passe qui n'étaient pas vides.

Mon SignUpForm était un composant stateful qui appelait validate dans ma fonction de rendu, ainsi que dans ma fonction canBeSubmitted.

J'ai obtenu cette fonction validate à partir de [cet article de blog freeCodeCamp](https://medium.freecodecamp.org/how-to-use-reacts-controlled-inputs-for-instant-form-field-validation-b1c7b033527e), probablement il y a environ un an.

Ma fonction validate originale ressemblait à ceci :

```
validate(name, password) {   return {      name: name.length === 0, //vrai si le nom d'utilisateur est vide      password: password.length === 0 //vrai si le mot de passe est vide   }}
```

J'ai décidé de refactoriser cette fonction, la rendant moins succincte, mais aussi plus claire, afin que moi, présent et futur, la comprenne :

```
validateFormInputs(name, password) {   let nameIsInvalid = (name.length === 0) //vrai si vide   let passwordIsInvalid = (password.length === 0) //vrai si vide   let errorObject = {      name: nameIsInvalid,      password: passwordIsInvalid   }   return errorObject}
```

Je peux vous entendre grogner, « Beurk, tu as rendu cette fonction succincte si longue et laide ! Tu as ajouté des noms de variables pour aucune raison ! »

Oui, j'ajoute quelques lignes ici, mais pour moi, je peux maintenant comprendre plus rapidement ce qui se passe dans cette fonction.

Maintenant, j'ajoute simplement quelques conditions supplémentaires à remplir. En plus d'un nom d'utilisateur valide qui n'est pas vide, je valide également qu'il ne peut pas être plus long que 15 caractères.

J'ai choisi le nombre 15 car c'est ce que [Twitter permet pour ses noms d'utilisateur](https://help.twitter.com/en/managing-your-account/twitter-username-rules), et si c'est assez bon pour Twitter, c'est assez bon pour WordNerds.

Avec ma nouvelle condition pour les noms d'utilisateur, ma fonction ressemble à ceci :

```
validateFormInputs(name, password) {   let nameIsInvalid = (name.length < 2 || name.length > 15)   let passwordIsInvalid = (password.length === 0)   let errorObject = {      name: nameIsInvalid,      password: passwordIsInvalid   }   return errorObject}
```

Super ! Maintenant, le Navy Seal Copypasta ne peut plus être utilisé comme nom d'utilisateur sur WordNerds.

Désolé, fans de copypasta ! Vous devez garder vos noms d'utilisateur à 15 caractères ou moins à partir de maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/TA0dzPY0YYqljqaX3ATdn0Wg4niTczfDqEh6)
_nom invalide si plus de 15 caractères_

J'ai réalisé qu'il était bon de ne pas permettre les espaces dans les noms d'utilisateur non plus. « Bob Smith » serait un mauvais nom d'utilisateur, tout comme « ». J'ai envisagé d'ajouter une simple regex à ma fonction, quand j'ai appris l'existence de l'[attribut pattern d'entrée](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#Attributes) en HTML5. Cool ! Pas besoin d'ajouter quoi que ce soit à ma fonction, je pouvais simplement mettre à jour mon champ de formulaire JSX pour le nom d'utilisateur.

Mon champ de formulaire de nom d'utilisateur du frontend React ressemble maintenant à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ofzGmtUNes-oQwFIrGsH2fuEzujDUJMTLABj)
_Champ de formulaire de nom d'utilisateur LoginForm_

Ce qui donne cette alerte dans le navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/tVyjswWUpBxtn15mInmg1jAh7lWKCPtHDi6y)
_alerte de mauvais nom_

J'ai apporté des mises à jour similaires à mon SignUpForm comme je l'ai fait pour mon LoginForm, et j'ai inclus quelques validations pour les adresses e-mail.

Super, maintenant je devais simplement m'assurer qu'il n'y avait pas d'adresses e-mail rendues visibles dans mon point de terminaison de l'API /stories. Au backend !

#### Limiter les données retournées pour chaque appel d'API

Blah blah blah, un tas de trucs sur le backend.

Je n'ai pas fait un bon travail d'écriture de ces trucs car j'essayais de le faire rapidement, et quand cela a échoué, j'essayais de le faire.

Je continue à réfléchir à des moyens d'améliorer les données retournées par mes points de terminaison d'API, pour rendre mon application à la fois plus sécurisée et plus évolutive.

Mais pour résumer, plus d'adresses e-mail rendues visibles dans mon point de terminaison de l'API /stories !

Maintenant, chaque histoire a un attribut `user_name`, en plus d'un attribut `user_id`, mais plus d'adresses e-mail ne sont accessibles via l'API.

On pourrait soutenir que j'expose toujours les noms d'utilisateur de mes utilisateurs, et que je ne devrais pas faire cela. Mais je traite ces noms d'utilisateur comme des informations publiques. Les utilisateurs peuvent choisir leurs noms d'utilisateur, donc c'est à eux de décider à quel point ils veulent être révélateurs dans leur choix de nom d'utilisateur. Cela pourrait être RichAt123FakeSt, ou cela pourrait être batman6669. Qui suis-je pour juger ce que les utilisateurs de mon application choisissent comme noms d'utilisateur ? Ce n'est pas comme si je révélais leurs adresses e-mail extrêmement personnelles ou quoi que ce soit ! Je veux dire, plus maintenant.

### Conclusion : Le feedback est bon

Après avoir apporté ces mises à jour de sécurité, j'ai également apporté quelques autres modifications amusantes. C'est amusant de continuer à améliorer mon application, grâce aux retours utiles d'inconnus sur Internet, ainsi qu'à toute fonctionnalité farfelue que je pense rendre meilleure.

Découvrez WordNerds ici, sur [WordNerds.co](http://wordnerds.co).

Merci d'avoir lu, les nerds !

À la prochaine.