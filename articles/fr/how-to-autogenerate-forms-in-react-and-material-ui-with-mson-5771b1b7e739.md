---
title: Comment autogénérer des formulaires dans React et Material-UI avec MSON
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-22T20:34:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-autogenerate-forms-in-react-and-material-ui-with-mson-5771b1b7e739
coverImage: https://cdn-media-1.freecodecamp.org/images/0*WKoVhYdsFzzh3_21.png
tags:
- name: Design
  slug: design
- name: forms
  slug: forms
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment autogénérer des formulaires dans React et Material-UI avec MSON
seo_desc: 'By Geoff Cox

  Implementing great forms can be a real time-waster. With just a few lines of JSON,
  you can use MSON to generate forms that perform real-time validation and have a
  consistent layout. And, MSON comes with a bunch of cool stuff like date pi...'
---

Par Geoff Cox

La mise en œuvre de formulaires performants peut être une vraie perte de temps. Avec seulement quelques lignes de JSON, vous pouvez utiliser [MSON](https://github.com/redgeoff/mson) pour générer des formulaires qui effectuent une validation en temps réel et ont une mise en page cohérente. Et, [MSON](https://github.com/redgeoff/mson) vient avec un tas de fonctionnalités sympas comme des sélecteurs de date, des champs masqués et des collections de champs.

**Avertissement** : cet article est destiné à ceux qui souhaitent utiliser Material-UI avec React. Les futures versions de MSON prendront en charge d'autres couches de rendu.

#### Qu'est-ce que MSON ?

[MSON](https://github.com/redgeoff/mson) est un langage déclaratif qui a les capacités d'un langage orienté objet. Le compilateur MSON vous permet de générer des applications à partir de JSON. L'objectif ultime de MSON est de permettre à quiconque de développer des logiciels visuellement. Vous pouvez également utiliser des morceaux de MSON pour accélérer le développement de vos formulaires.

### Un formulaire de base généré avec MSON

Déclarez simplement votre formulaire en JSON. Ensuite, laissez le compilateur MSON et la couche de rendu UI autogénérer votre interface utilisateur :

Avez-vous essayé de soumettre le formulaire sans remplir de valeurs ? Avez-vous remarqué comment la validation en temps réel est automatiquement intégrée ?

Maintenant, examinons de plus près ce qui se passe. Le premier bloc de code contient une définition JSON qui décrit les champs du formulaire :

Ce code ajoute les champs suivants à votre formulaire :

1. Le composant _Text_ affiche un peu de [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
2. Le _PersonNameField_ est utilisé pour capturer le prénom et le nom d'une personne
3. Le _DateField_ permet à un utilisateur de choisir une date en utilisant un sélecteur de date élégant
4. Le _PhoneField_ utilise un masque de saisie et des codes de pays pour guider l'utilisateur lors de la saisie d'un numéro de téléphone
5. Le _SubmitField_ contient une icône _Send_ et permet à l'utilisateur de soumettre le formulaire via un clic ou en appuyant sur entrée

Maintenant, examinons le code qui rend le composant et gère l'événement de soumission :

C'est tout ? Oui ! La couche [mson-react](https://github.com/redgeoff/mson-react) **sait automatiquement** comment rendre le composant de formulaire. Elle utilise [pub/sub](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) et [Pure Components](https://reactjs.org/docs/react-api.html#reactpurecomponent) pour garder le rendu à jour.

Lorsque qu'il n'y a pas d'erreur de validation et que l'utilisateur clique sur le bouton de soumission, un événement avec le nom égal au nom du bouton est émis. Dans notre cas, cet événement s'appelle _submit_. Par conséquent, nous pouvons définir un gestionnaire en utilisant la propriété _onSubmit_. Pour garder les choses simples, nous alertons simplement l'utilisateur des valeurs saisies. Typiquement, vous voulez faire quelque chose comme contacter une API, rediriger, etc...

### Formulaire de base 2

Maintenant, approfondissons un peu le CRUD avec un exemple différent :

La première chose que vous pouvez remarquer sont les [validateurs](https://github.com/redgeoff/mson#validators) dans la définition :

Chaque champ a un ensemble par défaut de [validateurs](https://github.com/redgeoff/mson#validators), par exemple, le _EmailField_ garantit que les adresses e-mail sont dans un format valide. Vous pouvez également étendre ces validateurs pour un champ particulier ou même pour un formulaire entier. Par exemple, vous pouvez empêcher l'utilisateur de saisir [_nope@example.com_](mailto:nope@example.com).

Ensuite, examinons le code qui charge les valeurs initiales lorsque le composant est monté :

Ce code pourrait tout aussi facilement être remplacé par un code qui récupère les valeurs de manière asynchrone à partir d'une API.

Enfin, nous utilisons un écouteur d'événements plus sophistiqué pour gérer l'action de soumission. Dans une application réelle, vous voudriez probablement envoyer une requête à une API pour sauvegarder les données. Vous recevriez une réponse de cette API. Si vous recevez une erreur, par exemple, l'adresse e-mail est déjà utilisée, vous pouvez présenter cette erreur à l'utilisateur :

### [Démonstration en direct](https://redgeoff.github.io/mson-react/)

Cet article ne traite qu'une petite partie de ce que vous pouvez faire en utilisant [MSON](https://github.com/redgeoff/mson). Parce que [MSON](https://github.com/redgeoff/mson) est un langage complet, vous pouvez déclarer tous types de composants sympas. Si vous êtes intéressé à voir plus d'exemples en direct, consultez la [démonstration en direct](https://redgeoff.github.io/mson-react).

![Image](https://cdn-media-1.freecodecamp.org/images/0*WKoVhYdsFzzh3_21.png)
_[https://redgeoff.github.io/mson-react](https://redgeoff.github.io/mson-react/" rel="noopener" target="_blank" title=")_

### Conclusion

Si vous utilisez React et Material-UI, vous pouvez accélérer le développement de votre application en autogénérant vos formulaires à partir de JSON. Cela peut être particulièrement utile si vous devez démarrer une application rapidement et ne souhaitez pas avoir à vous soucier de la construction d'une interface utilisateur à partir de zéro.

Si vous avez aimé cet article, n'hésitez pas à l'applaudir. Bonne [autogénération](https://github.com/redgeoff/mson) !

### À propos de l'auteur

Geoff Cox est le créateur de [MSON](https://github.com/redgeoff/mson), un nouveau langage de programmation déclaratif qui permettra à quiconque de développer des logiciels visuellement. Il est indépendant depuis la majeure partie des 15 dernières années. Il adore se lancer dans des projets ambitieux, mais qui rendent sa femme folle, comme [créer une base de données](https://github.com/delta-db/deltadb) et [un système de synchronisation de données distribuées](https://github.com/redgeoff/spiegel). Vous pouvez le contacter [@redgeoff7](https://twitter.com/redgeoff7) ou sur [github](https://github.com/redgeoff).