---
title: 'Comment créer un formulaire accessible : c''est plus facile que vous ne le
  pensez'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-03T21:36:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-an-accessible-form-its-easier-than-you-think-672d3f4ff573
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AenJNna8ufix9ON-b9noJA.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Comment créer un formulaire accessible : c''est plus facile que vous ne
  le pensez'
seo_desc: 'By Jonathan Speek

  Forms are an essential component of the web, as they connect users to your business
  and help them accomplish what they came to your site or app for. That being said,
  you want to make sure all of your users are able to use your forms...'
---

Par Jonathan Speek

Les formulaires sont un composant essentiel du web, car ils connectent les utilisateurs à votre entreprise et les aident à accomplir ce pour quoi ils sont venus sur votre site ou votre application. Cela dit, vous voulez vous assurer que tous vos utilisateurs peuvent utiliser vos formulaires sans avoir une mauvaise expérience. L'objectif est de rendre ces interactions utilisateur clés aussi fluides que possible.

Bien que la création de formulaires puisse être une tâche difficile à certains moments, les rendre modérément accessibles n'est pas aussi compliqué que vous pourriez le penser. Il y a souvent des excuses comme "nous n'avons pas le temps de nous soucier de l'accessibilité" ou "nous le rendrons accessible plus tard". Ces excuses sont souvent (si ce n'est toujours) invalides et vous pouvez aider votre équipe à changer cette mentalité.

Voici quelques points à considérer lors de la création de formulaires :

* Quelles difficultés une personne avec des déficiences visuelles pourrait-elle rencontrer en utilisant mon formulaire ?
* L'utilisateur a-t-il une indication claire des données attendues pour l'entrée ?
* Le formulaire est-il facile à comprendre rapidement ?
* Suis-je capable d'utiliser le clavier pour compléter le formulaire ?

### Créons un formulaire d'abonnement basique

![Image](https://cdn-media-1.freecodecamp.org/images/5v7lXfDhYtJD2kiXs2isTPo2ipucsgfATUWT)
_Je vous ai donné un peu de code de départ pour vous aider à tricher un peu ?_

Commencez avec ceci : [code de départ sur CodePen](https://codepen.io/JonathanSpeek/pen/JwNMYK)

Nous finirons par obtenir ceci : [**CodePen finalisé**](https://codepen.io/JonathanSpeek/pen/KrEdxR)

Je vous ai fourni quelques styles de base et éléments qui composent un formulaire d'abonnement simple, mais il y a beaucoup de choses que nous pouvons faire ici pour rendre ce formulaire plus utilisable. Avec tout ce que vous faites, l'utilisation d'un bon HTML sémantique vous mènera loin.

Commençons par connecter les éléments `<input>` à leurs `<label>` respectifs. Nous faisons cela en donnant à l'`<input>` un id et en utilisant celui-ci comme attribut `for` du `<label>`. Nous pouvons utiliser "name" et "email" pour ceux-ci et nous avons déjà fait deux choses :

1. nous avons associé programmatiquement le label à l'entrée, ce qui lira le label à un utilisateur de lecteur d'écran si cette entrée est focalisée
2. l'utilisateur peut maintenant cliquer sur le label et l'entrée respective sera focalisée, donc les utilisateurs ont maintenant une taille de cible plus grande

Maintenant que nos entrées et labels sont tous connectés, nous pouvons définir les types d'entrée HTML. Ceux-ci sont vraiment utiles et une manière super facile de donner une excellente expérience utilisateur. Ajouter l'attribut type ([lire sur les différents types ici](https://codepen.io/JonathanSpeek/pen/JwNMYK)) aidera l'utilisateur à remplir automatiquement votre formulaire et fournira un clavier plus adapté pour les utilisateurs mobiles. Pour notre cas d'utilisation, nous pouvons faire `type="text"` pour l'entrée du nom et `type="email"` pour l'entrée de l'email.

Nous voulons également que nos utilisateurs aient une bonne idée du type de données (et de leur formatage) que nous attendons d'eux. Ici, c'est assez évident, mais ce n'est pas toujours le cas. Il est généralement bon de fournir un label qui est toujours visible et un placeholder qui communique l'entrée attendue. Cela signifie **_ne pas_** utiliser l'attribut `placeholder` comme label visuel pour les entrées où le label n'est pas visible une fois qu'un utilisateur commence à taper. Cela a été une pratique populaire et doit être abandonnée... Nous pouvons donner un placeholder de "ex. Jane Doe" pour le nom et "ex. [jane.doe@example.com](mailto:jane.doe@example.com)" pour l'email.

Pour conclure, nous pouvons travailler sur le style de l'état `focus`. Les styles par défaut des états de focus sont différents entre les navigateurs et nous pouvons améliorer le style par défaut pour le rendre plus convivial. Dans notre cas, nous voulons que les entrées aient un contour épais et coloré qui correspond au bouton :

![Image](https://cdn-media-1.freecodecamp.org/images/SWhrj3fNWGP2t71lyFXP3WakSzJquhanOnXp)
_Ajoutez vos styles de focus dans votre sélecteur d'entrée ?_

Enfin, nous devons ajouter quelques styles de focus autour de l'élément bouton. Cela est souvent négligé, mais peut vraiment aider les utilisateurs qui n'utilisent que le clavier à savoir où ils se trouvent. Nous devons ajouter ce `&::moz-focus-innner` pour nous débarrasser de certains styles par défaut dans Firefox (vous pourriez vouloir sauvegarder ce snippet pour une utilisation future).

Tout simplement, nous avons un formulaire d'abonnement basique dont vous pouvez être fier et que vous pouvez améliorer. Parce que nous avons utilisé une bonne sémantique, le formulaire est accessible via le clavier uniquement (essayez d'utiliser les touches de tabulation et la barre d'espace/entrée). Les couleurs utilisées pour le bouton ont un [ratio de couleur de 11,51](https://contrast-ratio.com/#%23FFF-on-%232E1BA6), répondant aux [normes AAA pour les WCAG](https://www.w3.org/WAI/WCAG21/quickref/#contrast-enhanced) (Web Content Accessibility Guidelines). Nous avons fourni des labels pour les utilisateurs visuels et les utilisateurs de lecteurs d'écran, ainsi que des styles d'état de focus pour nos amis utilisant le clavier. Enfin, remarquez que la police est définie à `18px` dans le corps, ce qui rend notre formulaire beaucoup plus lisible ? (vous devriez essayer de rester au-dessus de 14px).

Concevoir et construire avec l'accessibilité en tête demande de la pratique, mais vous serez un meilleur développeur pour cela et vous aurez l'avantage supplémentaire de rendre le web un meilleur endroit ?

### Ressources

Voici quelques excellentes ressources pour vous aider à vous mettre à la place de vos utilisateurs et à vérifier votre travail :

[Funkify](https://chrome.google.com/webstore/detail/funkify-disability-simula/ojcijjdchelkddboickefhnbdpeajdjg) — une toute nouvelle extension pour Chrome qui vous aide à expérimenter le web et les interfaces à travers les yeux d'utilisateurs extrêmes avec différentes capacités et handicaps.

[Sim Daltonism](https://michelf.ca/projects/sim-daltonism/) — visualisez les couleurs telles qu'elles sont perçues avec divers types de daltonisme.

[Web.dev](https://web.dev/measure) — fournissez n'importe quelle URL, et web.dev exécutera une série d'audits en utilisant [Lighthouse](https://developers.google.com/web/tools/lighthouse/).

[Guide d'accessibilité de MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility) — c'est une excellente ressource à consulter régulièrement (j'❤️ les guides de MDN).

[Vérificateur de contraste de couleur](https://webaim.org/resources/contrastchecker/) — fournit un moyen rapide et facile de vérifier les ratios de contraste de couleur et les normes qu'ils respectent.

Merci d'avoir lu. Si vous avez des connaissances à partager sur l'accessibilité, n'hésitez pas à laisser un commentaire.

Vous pouvez [me suivre sur Twitter ici](https://twitter.com/intent/follow?screen_name=jonspeek) ✉️