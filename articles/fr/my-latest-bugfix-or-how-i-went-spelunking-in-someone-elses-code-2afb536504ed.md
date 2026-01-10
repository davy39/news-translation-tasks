---
title: 'Ma dernière correction de bug : ou comment j''ai exploré le code de quelqu''un
  d''autre'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T00:45:51.000Z'
originalURL: https://freecodecamp.org/news/my-latest-bugfix-or-how-i-went-spelunking-in-someone-elses-code-2afb536504ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NSN1a2xVtV1exzcD8fpzhA.jpeg
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: 'Ma dernière correction de bug : ou comment j''ai exploré le code de quelqu''un
  d''autre'
seo_desc: 'By Tiffany White

  I love CodeSandbox. It has pretty much replaced CodePen for me unless I am fiddling
  around with CSS or freeCodeCamp front-end projects.

  I like going through the sandboxes and picking out different ones to look at, take
  apart, and fig...'
---

Par Tiffany White

J'adore [CodeSandbox](https://codesandbox.io/). Il a pratiquement remplacé CodePen pour moi, sauf lorsque je m'amuse avec CSS ou des projets front-end de freeCodeCamp.

J'aime parcourir les sandboxes et en choisir différents à examiner, décomposer et comprendre comment ils fonctionnent.

En suivant le [Tutoriel React pour débutants](https://egghead.io/courses/the-beginner-s-guide-to-react) de [Kent C. Dodds](https://kentcdodds.com/) sur [Egghead.io](https://egghead.io), j'ai décidé de chercher des sandboxes qui correspondaient au cours, car j'utilisais Codesandbox pour construire le chronomètre que nous développions dans ce cours.

J'ai trouvé un [sandbox](https://codesandbox.io/s/v1vqomk697) que j'ai forké et que j'ai trouvé bogué.

Pourquoi le chronomètre ne fonctionnait-il pas ? En jetant un coup d'œil au code pendant quelques secondes, j'ai immédiatement vu quelques problèmes évidents.

Voici un exemple du chronomètre qui ne fonctionne pas :

![Image](https://cdn-media-1.freecodecamp.org/images/0*eaNKf6gfrCEUwhR8.gif)

#### Correction de bug 1

La première chose que j'ai remarquée était à la ligne 7 :

`Date.now()` a besoin de parenthèses. `Date` est un constructeur d'objet avec `.now()` étant une méthode. Lorsque nous cliquons sur le bouton de démarrage, React ne sait pas quoi faire ici ; nous ne définissons pas l'état de `lapse` pour qu'il soit un nombre, ce que nous attendons. En ajoutant les parenthèses, nous faisons fonctionner le bouton de démarrage. Plus de `NaNms`.

Mais maintenant nous avons un autre problème : _le minuteur ne s'arrête pas_.

![Image](https://cdn-media-1.freecodecamp.org/images/0*NH4ULkrZWEeopk1_.gif)

J'ai également supprimé le `console.log(Math.random());` car je le trouvais inutile.

#### Correction de bug 2 : Faire en sorte que le chronomètre s'arrête et se réinitialise

À chaque clic sur le bouton, nous définissons l'état soit sur `running`, soit sur `lapse`. Le minuteur fonctionne lorsque nous cliquons sur `start`, mais cliquer sur `stop` ou `clear` ne semble pas fonctionner. Comment pouvons-nous corriger cela ?

Nous pouvons créer une fonction de mise à jour du minuteur qui accepte l'état actuel. Nous pouvons y parvenir en utilisant les API DOM natives telles que `setInterval()` et `clearInterval()`. Nous pouvons exécuter une logique conditionnelle pour voir si le minuteur est en cours d'exécution :

et utiliser `Date.now()` pour obtenir le timestamp en ms, et l'assigner à une variable `startTime` pour comparer l'heure actuelle à la quantité de temps qui s'est écoulée. Lorsque nous cliquons sur le bouton de démarrage, il définit `startTime` sur le timestamp actuel. Nous devons également retourner un nouvel état car l'état n'est _pas_ mutable.

D'accord, donc cela fonctionne _partiellement_. Mais comme vous pouvez le voir ci-dessous, si je clique sur `clear` alors que le minuteur du chronomètre est en cours d'exécution, il _ne_ réinitialise _pas_ le minuteur, et il ne me permet pas non plus de _stopper_ le minuteur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*LLjNKMeXojOisrdD.gif)

Comment corriger ce bug particulier ?

Si nous regardons le code précédent, nous pouvons voir que nous utilisons `clearInterval()` pour réinitialiser le minuteur du chronomètre. Dans notre itération actuelle, notre méthode `handleOnClear` se contente de _définir_ l'état sans _effacer_ l'état précédent.

Nous pouvons corriger cela en ajoutant `clearInterval()` et en passant la fonction du minuteur à la méthode `handleOnClear` pour effacer l'état.

Cela nous donnera les résultats que nous voulons.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wtb7CitBJj9OtyLf.gif)

#### Problème potentiel ?

Il y a une fuite de mémoire dans cette itération particulière. Le minuteur continuera à fonctionner jusqu'à ce qu'il soit _explicitement_ arrêté dans le DOM. Nous pouvons utiliser une [méthode de cycle de vie React](https://reactjs.org/docs/state-and-lifecycle.html#adding-lifecycle-methods-to-a-class) pour arrêter tous les processus dans le DOM lorsque ce composant est monté ou démonté.

Pour cela, nous pouvons utiliser `componentWillUnmount` pour dire à React de démonter le composant une fois qu'il a fini de rendre.

#### Réflexions et conclusions

Je trouve beaucoup plus agréable de corriger les bugs _des autres_ que les miens. C'était un exercice amusant et je prévois de le faire plus régulièrement et d'en bloguer.

Ce chronomètre est un composant simple, mais si vous ne faites que gratter la surface de React comme moi, je suis sûr que creuser dans quelque chose comme ce chronomètre et comprendre comment il fonctionne est un excellent exercice et une bonne utilisation de son temps.

#### Inscrivez-vous à la newsletter. Pas de spam. Je déteste ça aussi.