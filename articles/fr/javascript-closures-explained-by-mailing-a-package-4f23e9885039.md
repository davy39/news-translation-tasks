---
title: Les fermetures JavaScript expliquées par l'envoi d'un colis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-19T02:27:41.000Z'
originalURL: https://freecodecamp.org/news/javascript-closures-explained-by-mailing-a-package-4f23e9885039
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IJ7H4WWlDuAWxlUSaF-Z6A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les fermetures JavaScript expliquées par l'envoi d'un colis
seo_desc: 'By Kevin Kononenko

  If you have mailed a package or letter in the past, then you can understand closures
  in JavaScript.

  On your journey to becoming an intermediate or advanced JavaScript dev, you may
  have come across closures. After reading a technica...'
---

Par Kevin Kononenko

#### Si vous avez déjà envoyé un colis ou une lettre, alors vous pouvez comprendre les fermetures en JavaScript.

Sur votre chemin pour devenir un développeur JavaScript intermédiaire ou avancé, vous avez peut-être rencontré les fermetures. Après avoir lu une ressource technique sur le sujet… vous avez probablement aussi couru dans la direction opposée.

**Voici ce qui est génial avec les fermetures** : elles vous permettent d'écrire des fonctions avec une étape intermédiaire qui peut capturer des données de votre site à un moment spécifique. C'est comme ajouter un bouton 'pause' à votre fonction. Vous pouvez exécuter votre fonction et sauvegarder la valeur d'une variable à ce point précis. Ensuite, lorsque vous souhaitez reprendre la fonction plus tard et utiliser des valeurs de variables qui ont changé dans votre application… vous pouvez le faire avec une **fermeture**, ou une fonction **à l'intérieur de la fonction originale**.

Cela devient plus facile, je vous le promets.

**Alors, quand diable utiliseriez-vous une fermeture ?**

Disons que vous construisez une carte interactive des monuments touristiques de New York en utilisant l'API Google Maps. Vous avez un tableau avec une série de marqueurs de carte que vous souhaitez ajouter à la carte - la Statue de la Liberté, l'Empire State Building, Coney Island, vous voyez le genre. Vous voulez ajouter tous ces marqueurs à la carte, mais vous voulez aussi ajouter un événement de clic à chaque marqueur. Lorsque vous cliquez sur le marqueur, vous voulez afficher des informations dynamiques sur ce marqueur, y compris des données météorologiques en direct.

```
var touristPlaces = […];
```

```
for(var i=0; i < touristPlaces.length; i++) {  var marker = touristPlaces[i];  $(marker).click(function() {    showToolTip(i)  });}
```

Voici le problème - si vous l'écrivez comme ça, [ça ne fonctionnera pas](http://stackoverflow.com/questions/2622421/what-are-the-use-cases-for-closures-callback-functions-in-javascript). La boucle 'for' se terminera avant que le callback dans l'événement de clic puisse enregistrer la valeur i appropriée. Vous devez capturer ce point intermédiaire afin de pouvoir appeler la fonction plus tard avec le i approprié.

**Que devez-vous savoir d'abord ?**

1. La portée des variables
2. Le concept des callbacks (J'ai aussi écrit [un guide sur ce sujet](https://medium.freecodecamp.com/javascript-callbacks-explained-using-minions-da272f4d9bcd#.rf0y0hl26) !)

Si vous cherchez une explication technique des fermetures, [le guide sur MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures) est probablement le meilleur.

#### Les fermetures suivent le même processus que l'envoi d'un colis.

Examinons un peu de code de base qui utilise une fermeture pour envoyer un colis.

La fonction addressPackage() est une **fermeture** ! Elle peut être appelée à tout moment après que la fonction packBox a été appelée. Elle a également accès aux variables et arguments du moment où packBox() a été appelée à l'origine.

Remarquez comment la sortie console.log ne s'affiche pas avant les lignes 14 et 15 ? **Ceci est extrêmement important.** Si vous exécutiez ce code après la ligne 11, vous verriez simplement 'Put jersey in box'. Il n'y aurait pas d'erreur, mais la fermeture, addressPackage(), ne s'exécuterait pas à ce moment-là.

Lorsque vous envoyez un colis, vous seriez probablement d'accord pour dire que votre travail n'est pas terminé tant que le colis n'est pas rempli et l'adresse écrite. De même, la fonction packBox() attend que la fermeture soit également appelée. Passons en revue cela ligne par ligne.

**Ligne 11 :** Vous créez la variable brotherGift, qui est une **instance** de la fonction packBox(). Vous envoyez un maillot à votre frère.

**Ligne 3 :** Votre code journalise une déclaration sur le maillot.

**Ligne 8 :** La fonction packBox() retourne… une autre fonction ? Hein ?

Arrêtons-nous ici, et supposons que la ligne 13 ne s'est pas encore exécutée. Voici ce qui se passe : La fonction packBox() ne retournera pas la ligne « prêt à envoyer » tant que vous n'aurez pas également appelé la fonction addressPackage() avec un argument. Tout comme il y a deux étapes pour envoyer un colis : d'abord, le remplir, et ensuite, l'adresser. Votre colis est sans valeur s'il n'a pas de contenu ou s'il n'a pas d'adresse ! Cela dit, vous n'avez pas nécessairement besoin d'adresser le colis directement après avoir rempli le contenu. Vous pouvez attendre quelques jours avant de l'adresser. Vous devrez peut-être aller à votre ordinateur pour chercher l'adresse. Vous attendez peut-être que votre frère change officiellement son adresse !

Quoi qu'il en soit, si vous n'adressez pas immédiatement le colis, cela ne signifie pas que le colis se videra magiquement. **Le contenu sera toujours là lorsque vous reviendrez pour l'adresser !** Donc, chaque fois que nous appelons brotherGift, le premier argument, jersey, sera toujours disponible.

… En attente… En attente… Maintenant, exécutons la ligne 13.

**Ligne 13 :** D'accord, terminons cette **instance** ! Vous êtes prêt à ajouter l'adresse, alors vous appelez brotherGift et offrez l'adresse comme argument. Rappelez-vous de la ligne 11, brotherGift est une **instance** de packBox avec l'argument 'jersey'. Donc lorsque vous l'appelez, vous offrez un autre argument, qui sera ensuite envoyé à la fermeture : addressPackage();

**Ligne 3 :** La console.log affichera puisque nous exécutons maintenant le code à partir de la ligne 13.

**Ligne 4 :** Nous offrons maintenant le deuxième argument à addressPackage();

**Ligne 6 :** addressPackage journalise une déclaration liée à l'argument d'adresse.

**Ligne 8 :** L'instruction return peut se déclencher pour cette instance.

Encore une fois, les fermetures nous permettent d'avoir cette instance intermédiaire où un argument a été rempli, mais brotherGift reste non rempli jusqu'à ce que nous ajoutions le deuxième argument. **Si nous voulions faire cela en une ligne**, nous écririons : packBox('jersey')('123 Main Street, Anywhere USA 01234');

#### Un autre exemple

Disons que vous voulez envoyer un cadeau à chaque membre de votre famille. Vous pourriez emballer chaque boîte avant d'ajouter les adresses à chacune. Voici à quoi cela ressemble en code.

Une autre caractéristique magique des fermetures ! Chaque instance est capable d'utiliser le bon article de cadeau avec la bonne adresse, même si nous exécutons la fonction avec 4 paires cadeau/adresse séparées. Dans une fonction traditionnelle, il n'y a pas de concept de mémoire. Vous devriez explicitement restater les cadeaux originaux dans les lignes 6–15 si vous vouliez utiliser une fonction traditionnelle.

#### Où vous allez utiliser cela

Vous rencontrerez fréquemment des fermetures dans Node.js. Si vous êtes seulement intéressé par le front-end, revenez à notre exemple original. Si vous voulez écrire une fonction qui considère l'entrée de l'utilisateur à deux étapes séparées de votre application, vous pourriez vouloir considérer une fermeture !

**Avez-vous apprécié ce guide ?** Ou avez-vous des difficultés avec un autre sujet JavaScript ? Donnez-lui un cœur et faites-le moi savoir dans les commentaires !

Vous cherchez d'autres concepts JavaScript expliqués ? Consultez ces articles précédents de la série.

[Les promesses JavaScript expliquées par le jeu dans un casino](https://medium.freecodecamp.com/javascript-promises-explained-by-gambling-at-a-casino-28ad4c5b2573#.8e096ciu2)

[Modèle-Vue-Contrôleur (MVC) expliqué à travers la commande de boissons au bar](https://medium.freecodecamp.com/model-view-controller-mvc-explained-through-ordering-drinks-at-the-bar-efcba6255053#.a2wmxu74b)

[Les callbacks JavaScript expliqués en utilisant des Minions](https://medium.freecodecamp.com/javascript-callbacks-explained-using-minions-da272f4d9bcd#.rf0y0hl26)