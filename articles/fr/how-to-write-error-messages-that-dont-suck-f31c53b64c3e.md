---
title: Comment écrire des messages d'erreur qui ne sont pas nuls
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T16:50:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-error-messages-that-dont-suck-f31c53b64c3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oCtk28IdNdpjnyMGiRsfLA.jpeg
tags:
- name: communication
  slug: communication
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment écrire des messages d'erreur qui ne sont pas nuls
seo_desc: 'By Justin Fuller

  “A validation error occurred.” Yep. Thanks!

  The release is imminent; this is the last update that needs to be verified, and
  I get an error message that’s as useful as the close button on an elevator.

  It turns out that it is a validat...'
---

Par Justin Fuller

« Une erreur de validation s'est produite. » Oui. Merci !

La sortie est imminente ; c'est la dernière mise à jour qui doit être vérifiée, et je reçois un message d'erreur qui est aussi utile que le bouton de fermeture d'un ascenseur.

Il s'avère que c'est bien une erreur de validation, en quelque sorte. L'entrée que je donne est un doublon. Elle est valide, elle existe simplement déjà !

Ne serait-ce pas si utile de le savoir ?

En fait, il serait utile d'être informé de plusieurs choses lorsque des erreurs se produisent. Je n'ai pas besoin de tout savoir. L'histoire de la programmation ne m'aidera pas ici. Le message devrait me donner juste assez d'informations pour que je puisse corriger cette erreur afin de pouvoir terminer mon travail, rentrer chez moi et jouer avec mes enfants.

#### Qu'est-ce qui fait une Erreur ?

En JavaScript, un objet d'erreur a toujours les propriétés name, message et stack. Le name vous donne une classification d'un coup d'œil de l'erreur. Le stack vous indique où cela s'est produit. Le message ? Eh bien, selon certains développeurs, vous n'avez pas besoin de vous en soucier ! « La trace de la pile vous donne tout ce dont vous avez besoin. »

S'il vous plaît, ne soyez pas un de ces développeurs.

#### Messages d'erreur utiles

Levez votre main droite, placez votre main gauche sur une copie de « Clean Code » et répétez après moi.

« Je jure d'inclure suffisamment de détails dans mes messages d'erreur pour que les développeurs futurs puissent facilement déterminer ce qui s'est mal passé et ce qu'ils doivent faire pour le corriger. »

#### Ce qui s'est passé

Lorsque qu'un policier vous arrête pour vous donner une amende, dit-il « Mauvaise conduite » ? Non ! Il dit que vous rouliez à 65 miles par heure dans une zone scolaire limitée à 25 miles par heure, que vous avez dépassé un bus arrêté et que votre voiture n'a pas été inspectée depuis quatre ans ! Bien sûr, vous allez en prison, mais au moins vous savez pourquoi.

Donc le message d'erreur de tout à l'heure ne devrait pas être « Une erreur de validation s'est produite », mais plutôt :

```
Impossible d'enregistrer le modèle "user" car la propriété "email" avec la valeur "JustinFuller@company.com" existe déjà.
```

Au lieu d'une simple erreur qui dit « Option invalide », utilisez :

```
L'option "update" n'est pas valide. Les options valides incluent "upsert", "get" et "delete".
```

Ces messages d'erreur mis à jour tentent de nous aider à comprendre la cause, nous donnant un point de départ vers la solution.

#### Comment cela a pu se produire

Maintenant que l'erreur décrit exactement ce qui s'est mal passé, il est temps d'aider la pauvre âme qui est tombée dans ce pétrin à commencer à s'en sortir. Regardez attentivement. Lorsque c'est fait correctement, cela semblera comme si vous atteigniez l'avenir en anticipant ce qui aurait pu conduire à ce tournant malheureux des événements. Vous serez là avec ce développeur futur — peut-être vous-même — leur disant que tout est bien, que vous allez surmonter cela ensemble.

Vous commencerez par expliquer ce qui s'est passé.

Pour tout ce qui a une étape préalable, comme la configuration ou la validation, vous pouvez suggérer de vérifier que cette étape a été complétée. Ne vous inquiétez pas si vos messages d'erreur deviennent longs. Il est préférable de fournir trop d'informations que pas assez.

Je vais ajouter plus de détails à l'un des exemples précédents :

```
L'option "update" n'est pas valide. Les options valides incluent "upsert", "get" et "delete". Si vous vous attendiez à ce que "update" soit une option, vous devez d'abord l'exporter depuis le fichier : "./src/controllers/index.js".
```

Maintenant, vous anticipez comment cela a pu se produire : le développeur a probablement oublié d'exporter la nouvelle option. L'erreur devient un rappel de cette étape. Vous avez maintenant montré deux causes possibles de l'erreur ; la première est une possible faute de frappe (voici les options valides) et la seconde est une erreur de configuration (voici où elle devrait être exportée).

La bibliothèque React fait un excellent travail d'anticipation de la manière dont les erreurs ont pu se produire. Ils ne traitent pas tous les cas particuliers, mais ils donnent des indices utiles pour les erreurs les plus courantes. Par exemple, vous ne pouvez pas utiliser la fonction `reactDom.renderToNodeString()` dans le navigateur car les flux de nœuds n'existent pas là. Donc React vous donne une suggestion de la manière dont cela s'est produit et comment le corriger :

```
ReactDOMServer.renderToNodeStream() : L'API de streaming n'est pas disponible dans le navigateur. Utilisez ReactDOMServer.renderToString() à la place.
```

Il pourrait y avoir d'autres manières pour que cette erreur se produise, mais ils supposent que la raison la plus courante est que `renderToNodeStream` a été appelé dans le navigateur.

#### Données pertinentes

Lors de la rédaction de messages d'erreur, vous devez vous rappeler que les applications font rarement une seule chose à la fois. Donc, lorsque des erreurs se produisent, il est difficile de trouver l'état de l'application à ce moment-là. Pour cette raison, il est très important de capturer les données pertinentes et de les relayer au développeur afin qu'il puisse identifier la cause.

Dans le premier exemple, j'ai inclus la phrase :

```
La propriété "email" avec la valeur "JustinFuller@company.com" existe déjà.
```

Cela est très utile, mais pourrait être peu pratique. Cela peut prendre trop d'efforts ou de temps pour créer des erreurs en langage naturel pour chaque variation de données, ou dans certains cas, nous pouvons simplement transmettre une défaillance hors de notre contrôle, donc la seule option restante est de donner une bonne description et d'inclure autant de données pertinentes qu'il est sûr d'imprimer.

Le choix des données qu'il est sûr d'imprimer est délicat : si vous choisissez exactement quelles propriétés inclure, vous finissez par modifier la liste chaque fois qu'il y a une nouvelle propriété, ou, pire, vous oubliez et elle n'apparaît pas lorsqu'elle est nécessaire ; d'un autre côté, vous pouvez supprimer les propriétés connues pour être non sûres, mais ici vous risquez d'ajouter une nouvelle propriété et d'oublier de l'exclure, provoquant une fuite de données sensibles. Vous devez utiliser votre jugement et considérer les règles de votre entreprise. Votre logiciel traite-t-il des données hautement précieuses ou personnelles qui ne devraient pas être écrites vers une destination non cryptée ? Le fait de journaliser sans réfléchir chaque objet qui provoque une erreur est susceptible de vous faire renvoyer de certains emplois, tandis que dans d'autres, c'est la procédure opérationnelle standard. Donc, s'il vous plaît, utilisez le bon sens et soyez prudent !

#### Erreurs inattendues

Il y a deux façons d'inclure des données pertinentes lorsque vous ne savez pas exactement quelle propriété ou action a provoqué l'erreur.

La première doit être utilisée lorsque vous destinez l'erreur à être lue par des humains, vous mettez les données directement dans le message : `Une erreur a été reçue : « Entrée en double trouvée pour user.email », lors de la mise à jour de l'utilisateur : { « email » : « justinfuller@company.com » }.` Ce style d'erreur a ses inconvénients, comme l'objet entier étant placé dans le message d'erreur qui pourrait être envoyé quelque part de manière non intentionnelle. Si, cependant, vous savez qu'il est sûr, alors ce style a l'avantage de donner des détails complets sur la situation.

Dans d'autres cas, vous ne voudrez peut-être pas que les données fuient vers un fichier journal ou une réponse d'API. Vous pouvez fournir un ID de référence, un horodatage qui peut être référencé manuellement ou automatiquement à des données plus tard, ou une autre propriété qui permettra au développeur de retrouver le point de données ennuyeux qui a provoqué une erreur.

#### Erreurs attendues

Je serai le premier à admettre que je suis enclin à faire des erreurs simples. Je tape « upswert » au lieu de « upsert » ; je tape « npm tes » au lieu de « npm test ». Donc, c'est vraiment rafraîchissant lorsque je reçois un message d'erreur disant :

```
Commande inconnue, "npm tes". Vouliez-vous dire npm test ?
```

Lorsque les développeurs se sont préparés à cela, ils ont évidemment regardé dans le futur et ont vu que quelqu'un ferait cette faute de frappe — ou peut-être savent-ils simplement que les humains sont enclins à des erreurs stupides.

Chaque fois qu'il y a une étape dans un processus qui peut mal tourner de manière prévisible, vous avez l'opportunité de préparer des directives claires sur ce qui s'est mal passé et comment le corriger.

#### Étapes pour corriger le problème

Pour certaines erreurs, il sera possible de donner une solution à l'erreur au lieu de simplement signaler qu'elle s'est produite. Parfois, ce sera facile, comme plus tôt lorsque nous avons montré les options correctes après avoir accidentellement tapé « update » au lieu de « upsert ». D'autres fois, vous devrez faire plus d'efforts pour donner à l'utilisateur suffisamment d'informations pour corriger son erreur, comme si vous avez détecté une dépendance récursive, et que vous devez lui dire où se trouve la boucle et ce qu'il doit faire pour la supprimer.

#### Une erreur qui ne suce pas

Alors, voulez-vous fournir des messages d'erreur utiles ? Dans le prochain message d'erreur que vous écrivez, essayez d'inclure une description complète de ce qui s'est passé, comment cela a pu se produire, toutes les données pertinentes qu'il est sûr d'inclure, et toutes les étapes qui pourraient aider à résoudre le problème.

Bonjour, je suis Justin Fuller. Je suis si heureux que vous ayez lu mon article ! Je dois vous informer que tout ce que j'ai écrit ici est mon propre avis et n'est pas destiné à représenter mon employeur de quelque manière que ce soit. Tous les exemples de code sont les miens et sont complètement sans rapport avec le code de Bank Of America.

J'aimerais aussi avoir de vos nouvelles, n'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/justin-fuller-8726b2b1/), [Github](https://github.com/justindfuller), ou [Medium](https://medium.com/@justindanielfuller). Merci encore d'avoir lu !