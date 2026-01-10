---
title: Pourquoi utiliser des types statiques en JavaScript ? Devrions-nous les utiliser
  ou non ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-11T18:27:35.000Z'
originalURL: https://freecodecamp.org/news/why-use-static-types-in-javascript-part-4-b2e1e06a67c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PKmiFZ47uY9CwfIHrPny-A.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Pourquoi utiliser des types statiques en JavaScript ? Devrions-nous les
  utiliser ou non ?
seo_desc: 'By Preethi Kasireddy

  Note: This is Part 3 of a 3-part series. You can check out Part 1 and Part 2 if
  you haven’t already!

  So should we use static types in JavaScript or not?

  The first programming languages I learned were JavaScript and Python, both o...'
---

Par Preethi Kasireddy

_Note : Ceci est la partie 3 d'une série en 3 parties. Vous pouvez consulter la [Partie 1](https://medium.freecodecamp.com/why-use-static-types-in-javascript-part-1-8382da1e0adb#.91629ow6y) et la [Partie 2](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-2-part-3-be699ee7be60#.j4viwr6km) si vous ne l'avez pas déjà fait !_

### Devrions-nous donc utiliser des types statiques en JavaScript ou non ?

Les premiers langages de programmation que j'ai appris étaient JavaScript et Python, tous deux des langages à typage dynamique.

Mais mon incursion dans les types statiques a ajouté une toute nouvelle dimension à ma façon de penser la programmation. Par exemple, même si j'ai trouvé les erreurs du compilateur Elm accablantes au début, définir des types et "plaire au compilateur" est devenu une seconde nature, et a réellement amélioré ma réflexion sur le code. De plus, il n'y a rien de plus libérateur qu'un robot intelligent qui me dise quand je fais quelque chose de mal et comment le corriger.

Malgré les compromis qui accompagnent les types, comme la verbosité et l'investissement initial pour les maîtriser, la sécurité et la justesse que les types ajoutent à nos programmes rendent ces "inconvénients" moins problématiques pour moi personnellement.

Le typage dynamique semble plus rapide et plus facile, mais il perd parfois du terrain une fois que vous essayez de faire fonctionner un programme en conditions réelles. En même temps, vous pouvez parler à n'importe quel développeur Java qui a dû travailler avec des définitions de types génériques plus compliquées et ils vous diront à quel point ils détestent les types.

En fin de compte, il n'y a pas de solution miracle. Mon approche personnelle est de privilégier l'utilisation des types dans les circonstances suivantes :

1. Le programme est crucial pour votre entreprise
2. Le programme est susceptible d'être refactorisé au fur et à mesure que vos besoins évoluent
3. Le programme est complexe et comporte de nombreuses parties mobiles
4. Le programme est maintenu par une grande équipe de développeurs qui doivent pouvoir saisir et comprendre le code rapidement et avec précision

En revanche, je considérerais l'option de ne pas utiliser de types dans les situations suivantes :

1. Le code est éphémère et non critique
2. Vous prototypiez et essayez d'avancer le plus rapidement possible
3. Le programme est petit et/ou simple
4. Vous êtes le seul développeur

La beauté d'être un développeur JavaScript aujourd'hui est que, grâce à des outils comme Flow et TypeScript, nous avons enfin le choix d'utiliser des types statiques ou le bon vieux JavaScript vanilla.

### Conclusion

J'espère que cet article vous a aidé à comprendre pourquoi les types sont importants, comment les utiliser et, surtout, *quand* les utiliser.

Pouvoir basculer entre les types dynamiques et statiques est un outil puissant pour la communauté JavaScript — et passionnant :)

Plus de questions ? Comme toujours, contactez-moi dans les commentaires pour poursuivre la conversation.