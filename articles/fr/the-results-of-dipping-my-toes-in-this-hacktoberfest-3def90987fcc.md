---
title: Ce que j'ai appris en plongeant dans Hacktoberfest pour la première fois
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-06T23:55:20.000Z'
originalURL: https://freecodecamp.org/news/the-results-of-dipping-my-toes-in-this-hacktoberfest-3def90987fcc
coverImage: https://cdn-media-1.freecodecamp.org/images/0*fvKBQ0addZa-P8zY
tags:
- name: GitHub
  slug: github
- name: hacktoberfest
  slug: hacktoberfest
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Ce que j'ai appris en plongeant dans Hacktoberfest pour la première fois
seo_desc: 'By Travis Fantina

  Imposter syndrome is something we all struggle with to one degree or another. Imposter
  syndrome is the fear of exposure as a fraud. If you’re anything like me you have
  felt like your work was not good enough to show. Or you weren’t ...'
---

Par Travis Fantina

Le syndrome de l'imposteur est quelque chose avec lequel nous luttons tous à un degré ou un autre. Le syndrome de l'imposteur est la peur d'être exposé comme un fraudeur. Si vous êtes comme moi, vous avez peut-être eu l'impression que votre travail n'était pas assez bon pour être montré. Ou que vous n'étiez pas assez avancé dans votre parcours de développeur pour avoir beaucoup à contribuer.

Après avoir appris l'existence de Hacktoberfest l'année dernière, j'ai voulu contribuer. Mais je me sentais dépassé, et le syndrome de l'imposteur a commencé à prendre le dessus.

Je me suis dit que j'étais trop inexpérimenté en tant que développeur et je m'inquiétais que mes commits ne soient pas utiles. Malheureusement, j'ai laissé ces peurs prendre le dessus et je ne me suis même pas inscrit.

Cette année, je me suis forcé à mettre mes peurs de côté, j'ai étudié [cet article](https://medium.freecodecamp.org/hacktoberfest-2018-how-you-can-get-your-free-shirt-even-if-youre-new-to-coding-96080dd0b01b) sur Hacktoberfest, et je me suis lancé. Je vais partager un peu de ce sur quoi j'ai travaillé et les avantages de participer. Des avantages qui vont bien au-delà de la réception d'un t-shirt et qui peuvent être obtenus 12 mois sur 12 !

![Image](https://cdn-media-1.freecodecamp.org/images/cqmCGieQ0qebpj3trmwsa3RW01EETqHfgmd9)
_Image : [twillo](https://www.twilio.com/blog/hacktoberfest-and-new-twilioquest-mission-here" rel="noopener" target="_blank" title=")_

#### Mon expérience avec Hacktoberfest

J'ai commencé le 11 octobre. J'étais déjà légèrement désavantagé, étant donné qu'un tiers du mois était déjà passé.

Le manque de temps m'a motivé. J'ai décidé que j'essaierais de soumettre une pull request chaque vendredi et une fois pendant la semaine pour le reste du mois. Établir un calendrier était important. Je me suis concentré sur les pull requests deux ou trois jours par semaine et j'ai essayé de ne pas stresser le reste du temps. Peu importe l'ambition de votre objectif, cinq pull requests en un mois ou cinq pull requests en une semaine : il est important d'avoir un plan.

Ma première pull request était sur freeCodeCamp. Je travaillais sur certains des défis d'algorithmes JavaScript. J'ai remarqué un lien pointant vers un emplacement inattendu. C'était une correction simple, mais elle m'a donné un peu de confiance. Il y avait effectivement des choses que je pouvais résoudre !

La pull request était facile, je n'ai pas forké ou cloné le dépôt freeCodeCamp, je l'ai ouvert directement sur la page GitHub.

Boom, première pull request ouverte.

Je ne voulais pas que mes cinq pull requests proviennent d'un seul dépôt (bien qu'il n'y ait rien de mal à cela). Après quelques pull requests sur freeCodeCamp, j'ai commencé à explorer GitHub.

J'ai commencé par regarder des projets que je connaissais bien. Plus précisément, j'ai parcouru des outils et des projets que j'avais beaucoup utilisés comme Rails, React, Bootstrap et Devise, entre autres. Chaque fois que possible, j'ai recherché des problèmes étiquetés « Hacktoberfest », « First Time Contributor » ou « Easy ».

![Image](https://cdn-media-1.freecodecamp.org/images/nvN-kYzKeFb1rpF5rBOhtJo0qr-LI2uOQfvf)
_GitHub facilite la recherche parmi les problèmes_

Avec les grands projets, il y a beaucoup plus de contributeurs. Les problèmes faciles tendent à être résolus assez rapidement. J'ai restreint ma recherche aux dépôts plus petits.

Il y a quelques années, un ami et moi avons construit un site de critiques pour les professeurs appelé « AvalueMeuProfessor ». En travaillant sur ce projet, j'ai découvert une bibliothèque appelée [jQuery Raty](https://github.com/wbotelhos/raty). Cette bibliothèque facilite l'ajout d'étoiles de vote à votre projet. Bien qu'elle ait plus de 2 000 étoiles sur GitHub, il n'y avait que 21 contributeurs. Il y avait plusieurs problèmes non résolus.

![Image](https://cdn-media-1.freecodecamp.org/images/E5RQPbqXZVfFjDEOrj8PSGbSy2uDT8ehCGcu)
_Raty en action…_

En améliorant ce que je pouvais, j'ai soumis une pull request qui a ajouté de la valeur au projet. C'est important. La taille ou l'ampleur de votre pull request n'a pas d'importance, mais elle doit apporter de la valeur au projet. Elle a été fusionnée dans le projet en quelques heures.

Même si je n'ai corrigé que des fautes de frappe dans la documentation, j'ai acquis une nouvelle compréhension du fonctionnement de la bibliothèque. Cela m'a également donné une plus grande appréciation pour le projet et ses mainteneurs.

Grâce à mon travail avec Rails et l'application Raty, je suis tombé sur un gem Ruby abandonné. Il servait jQuery Raty dans le pipeline d'actifs de Rails : simple mais utile. Il y avait quelques problèmes ouverts, mais le README indiquait clairement que le projet était abandonné.

Encore une fois, c'était un projet idéal car il était de petite envergure et l'activité sur le projet était minimale… inexistante.

J'ai forké le dépôt et j'ai commencé à mettre à jour le gem pour le rendre compatible avec Rails 5. Dans le processus, j'ai appris un peu sur le pipeline d'actifs et beaucoup sur le fonctionnement des gems Rails. J'ai lu plusieurs articles sur la création de gems que je n'aurais autrement jamais vus. Dans le processus, j'ai contacté le créateur original. Il n'était plus intéressé à gérer le projet et je l'ai repris. Il est maintenant maintenu sur [mon fork](https://github.com/tfantina/jquery-raty-rails).

Malgré mes insécurités initiales concernant la contribution, je me suis lancé et je me suis poussé. J'espérais un t-shirt, mais j'ai obtenu bien plus. J'ai pu :

* Soumettre ma première pull request dans un dépôt public
* Apprendre beaucoup sur les gems Ruby
* Prendre en charge la maintenance d'un gem
* Acquérir une nouvelle appréciation pour certains des outils et ressources que j'utilise depuis des années
* Augmenter mon nombre moyen de commits pour le mois (et de beaucoup)
* Devenir plus à l'aise avec Git, à la fois sur GitHub et via la CLI

![Image](https://cdn-media-1.freecodecamp.org/images/CHMriD3rpBsx0hsPF1gjwSo9MHA12ypLBuLQ)
_Hacktoberfest, c'est fait ! (De [https://hacktoberfest.digitalocean.com](https://hacktoberfest.digitalocean.com" rel="noopener" target="_blank" title="))_

Par-dessus tout, ma participation à Hacktoberfest a fait de moi un meilleur développeur avec un plus grand désir de contribuer. J'ai vu qu'il y avait de la place dans ces projets pour de nouveaux contributeurs.

Vous voulez peut-être contribuer, mais vous vous inquiétez de ne pas être assez bon ou de ne pas savoir par où commencer. Mais contribuer à des dépôts open source n'est pas réservé aux développeurs seniors avec des années d'expérience. Contribuer à des projets est un excellent moyen d'améliorer vos compétences, de gagner en confiance et de pratiquer la programmation. Bien que trouver le bon projet puisse prendre un peu de recherche, cela en vaudra la peine.