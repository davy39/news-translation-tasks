---
title: Et si tous vos appareils mobiles formaient un seul écran ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-20T18:51:28.000Z'
originalURL: https://freecodecamp.org/news/what-if-all-your-mobile-devices-formed-a-single-screen-9c6ff01ed0c3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eIQx-sLpotbpIrRnhPLPMA.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Et si tous vos appareils mobiles formaient un seul écran ?
seo_desc: 'By Tim Grossmann

  What if all your mobile devices were a single screen? This probably isn’t the most
  common question to ask yourself.

  But, just for a second, actually think about it. Think about all the possibilities
  of being able to combine any kind ...'
---

Par Tim Grossmann

Et si tous vos appareils mobiles ne formaient qu'un seul écran ? Ce n'est probablement pas la question la plus courante à se poser.

Mais, juste une seconde, réfléchissez-y vraiment. Imaginez toutes les possibilités de pouvoir combiner n'importe quel type d'appareil mobile, indépendamment de son système d'exploitation. C'est ce que fait Swip.js.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S1DIXIJzt6WZVysqorz2ug.png)
_Logo de Swip.js_

L'idée est assez simple : placez plusieurs appareils de n'importe quelle taille les uns à côté des autres et "swipez" (pincez) vos doigts sur leurs bords pour combiner les écrans séparés en un grand écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bqv2v1dcFFUMhdv9K4DufA.jpeg)
_Il suffit de pincer les écrans ensemble_

Avec Swip.js, vous pouvez construire des expériences multi-appareils compliquées comme celle-ci :

%[https://www.youtube.com/watch?time_continue=4&v=ZE0gxa-p8HY]

### Origines de l'idée

Lorsque nous cherchions une idée à développer lors d'un Hackathon, Paul s'est souvenu de ce gadget qu'il avait vu il y a assez longtemps :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KmyEPMVP1zxpKETQ2Ykplw.gif)
_Siftables — [Regardez la présentation sur YouTube](https://www.youtube.com/watch?v=JP0w9lZoLwU" rel="noopener" target="_blank" title=")_

Nous avons tous les deux aimé l'idée d'avoir des choses séparées "stupides", que nous pourrions combiner pour créer un système fonctionnel. Nous avons pensé à construire quelque chose de similaire avec un RaspberryPi.

Mais comme nous n'étions pas des experts en matériel, nous n'avons pas pu construire quelque chose comme ça. C'est alors que nous avons réalisé que presque tout le monde a **un petit ordinateur (avec un navigateur web) dans sa poche.** Un ordinateur suffisamment puissant pour gérer même des tâches complexes.

Nous savions que notre langage de choix serait **JavaScript**, car il est complètement indépendant de la plateforme et fonctionne sur n'importe quel appareil avec un navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mwRvmAs9lyRUpsVwQy456w.jpeg)

### Prototypage au Hackathon Inno{Hacks}

La première idée, en fait, était de construire une démonstration de physique où les téléphones pourraient "lancer" des cubes dans un appareil plus grand (comme un iPad) qui contiendrait l'environnement physique.

Les idées ont rapidement évolué et après quelques bidouillages et du codage, nous avons décidé de réduire un peu la complexité. À la fin du Hackathon, nous avions une démonstration fonctionnelle.

Notre idée suivante était de construire un jeu où vous aviez un iPad posé sur la table et vous deviez interagir avec lui en utilisant votre téléphone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jC74suQS7nChF3AET7zZqg.png)
_Concept de l'idée_

Si vous regardez le concept, vous pouvez voir que la tablette devrait servir de "jeu de société" et avec les téléphones, vous étendiez le plateau pour battre le niveau. L'idée était d'avoir différentes pièces de chemin sur votre téléphone parmi lesquelles vous pouviez en choisir une. La balle bougerait, allant de plus en plus vite, et le but était soit de survivre plus longtemps que les autres joueurs, soit d'atteindre la position cible.

Après un moment, nous avons également abandonné cette idée (parce que nous n'avons pas pu obtenir une tablette) et avons décidé de faire de la fusion des écrans la fonctionnalité principale de notre présentation, au lieu d'un jeu gadget qui deviendrait rapidement ennuyeux.

C'est alors que nous avons décidé de nous lancer dans 2 exemples simples : le jeu classique **Pong** et, pour montrer que ce n'est pas seulement pour s'amuser avec des jeux, une petite application de **partage de photos**.

#### Voici donc le résultat d'environ 20h de hacking au Hackathon :

![Image](https://cdn-media-1.freecodecamp.org/images/1*U46DsbFKhSGpiNesNPLE_Q.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mWgpk2WYoHhMyANQ7dSD3g.gif)
_Démos du Hackathon_

#### Quel genre de sorcellerie est-ce ?

Croyez-le ou non, ce n'est que du JavaScript, du Canvas et une technologie appelée [WebSockets](https://www.html5rocks.com/en/tutorials/websockets/basics/).

Les bibliothèques sont toujours une bonne chose pour les Hackathons, donc vous n'aurez pas besoin de gérer du JavaScript brut. Par conséquent, nous avons utilisé [Socket.IO](https://socket.io) pour nous donner une API plus agréable pour gérer les websockets dans Swip.

> Allez-y, jetez un coup d'œil à [comment fonctionnent les websockets](https://www.html5rocks.com/en/tutorials/websockets/basics/) et essayez [Socket.IO](https://socket.io)! Vous serez impressionné par leur puissance et leur facilité d'utilisation.

En gros, vous pouvez imaginer une connexion websocket comme un tunnel qui connecte un client et un serveur avec une connexion en temps réel persistante et bidirectionnelle. Les deux parties peuvent alors simplement envoyer, recevoir et répondre aux messages.

#### **Un exemple rapide utilisant Socket.IO**

Commençons d'abord par le serveur. Comme nous voulons garder cela simple et rapide, nous utiliserons Express pour configurer rapidement un serveur.

```js
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  console.log('un utilisateur s\'est connecté');
});

http.listen(3000);
```

C'est tout ce dont vous avez besoin côté serveur pour commencer.

Ouvrez maintenant le navigateur et allez sur `localhost:3000` et demandez-vous pourquoi il ne journalise rien dans la console. Vous devez faire une chose de plus. Vous devrez également démarrer la connexion websocket côté client. Ce sera le `index.html` que vous pouvez voir dans la fonction `app.get` côté serveur.

```html
<script src="/socket.io/socket.io.js"></script>
<script>
  var socket = io();
  
  socket.emit('message', 'Hello');
</script>
```

Si vous allez maintenant sur `localhost:3000` et regardez le terminal où vous avez démarré le serveur, vous verrez `un utilisateur s\'est connecté`.

Le **socket** est la partie sur laquelle vous voulez vous concentrer maintenant. Dans `index.html`, nous faisons `socket.emit('message', 'Hello')`. Nous **émettons** un nouveau message avec le **nom** `message` et la **donnée** `Hello` et voulons réagir à ce message sur le serveur. Pour ce faire, nous devons travailler avec le socket que nous obtenons lorsque nous appelons `io.on('connection', (**socket**) => .`..). Par conséquent, nous ajoutons simplement les lignes suivantes.

```js

io.on('connection', (socket) => {
  socket.on('message', (msg) => {
    console.log('message: ' + msg);
    
    socket.emit('messageBack', { message: 'Hello à vous !'});
  });
});
```

Vous verrez maintenant `Hello` imprimé dans la console chaque fois qu'un nouveau client rejoint le serveur. Pour l'instant, ce n'est pas trop spécial. Mais nous pouvons également envoyer des données du serveur au client, via le même socket et même utiliser des objets entiers au lieu de simples chaînes de caractères. Le client doit simplement réagir à l'événement émis avec `socket.on('messageBack', (data) => .`..) et peut ensuite utiliser les données envoyées.

Si vous voulez en savoir plus sur Socket.IO, consultez leur [tutoriel ChatApp](https://socket.io/get-started/chat/), où vous construisez rapidement un clone basique de Slack.

Maintenant que vous connaissez un peu la technologie derrière cela, vous pouvez probablement déjà deviner comment cela fonctionnait essentiellement.

Nous envoyions simplement les données de position des éléments tout le temps et rendions, par exemple, la balle de pong sur chaque client.

Ce n'est vraiment pas performant à grande échelle. Mais nous avons appris que lors du prototypage lors d'un Hackathon, **vous ne devriez vraiment pas vous soucier de la performance**.

Les gens là-bas étaient assez impressionnés et perplexes quant à la façon dont cela pourrait fonctionner et [nous avons fini par remporter le prix de l'innovation technologique](https://devpost.com/software/swip). Ils nous ont même demandé si nous pensions travailler davantage sur ce projet.

> À retenir : Si vous ne voulez pas construire quelque chose avec les outils donnés du hackathon, ne le faites pas. Expérimentez, jouez, et — surtout — amusez-vous !

![Image](https://cdn-media-1.freecodecamp.org/images/1*mwRvmAs9lyRUpsVwQy456w.jpeg)

### Faire connaître le projet et obtenir les 1 000 premières étoiles GitHub

Lorsque nous avons terminé notre première version utilisable de [Swip.js](https://github.com/paulsonnentag/swip), nous étions assez fiers que cela se soit transformé en un projet aussi divertissant.

Nous voulions le montrer à plus de gens, obtenir des retours et (bien sûr) obtenir des étoiles GitHub pour améliorer notre audience. La source d'informations technologiques de notre choix était [HackerNews](https://news.ycombinator.com). Il dispose d'une section spéciale pour présenter votre travail.

Paul m'a envoyé un message environ une demi-heure après [la publication du lien](https://news.ycombinator.com/item?id=12735665), me disant que nous avions déjà atteint plus de 100 étoiles GitHub. À partir de ce moment, j'ai vérifié les commentaires sur [HackerNews](https://news.ycombinator.com) comme toutes les minutes. Nous ne pouvions pas croire à quelle vitesse cela a décollé.

J'ai commencé à spammer chaque blogueur possible, gourou JavaScript et Subreddit auquel je pouvais penser avec un lien vers le dépôt. Nous avons obtenu des retours vraiment géniaux. Une personne qui l'a remarqué était [Quincy Larson](https://www.freecodecamp.org/news/what-if-all-your-mobile-devices-formed-a-single-screen-9c6ff01ed0c3/undefined) :

%[https://twitter.com/ossia/status/789148681194921984]

[Le Twitter de Paul a été inondé de notifications](https://twitter.com/search?q=swip.js&src=typd) et nous avons même été présentés dans un [blog japonais](http://gigazine.net/news/20161029-swip-js/?utm_content=buffer822e3&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer).

C'était juste génial !

[**paulsonnentag/swip**](https://github.com/paulsonnentag/swip)
[_swip - une bibliothèque pour créer des expériences multi-appareils_](https://github.com/paulsonnentag/swip)
[github.com](https://github.com/paulsonnentag/swip)

> À retenir : Personne ne verra votre projet à moins que vous ne le montriez. Utilisez des canaux populaires pour faire connaître !

![Image](https://cdn-media-1.freecodecamp.org/images/1*mwRvmAs9lyRUpsVwQy456w.jpeg)

### À propos de la construction d'une bibliothèque JavaScript

Après avoir entendu les retours incroyables de tous les concurrents et juges, nous avons discuté de la possibilité de travailler un peu plus sur ce projet. Nous avons décidé d'y consacrer **2 jours de plus** pour construire une bibliothèque.

Eh bien, nous avons fini par **investir 2 semaines entières** dans le projet, car nous avons extrêmement sous-estimé la charge de travail. Nous avons dû repartir de zéro, car notre base de code était presque inutilisable.

En travaillant dessus, nous avons rencontré quelques défis. L'un des plus grands défis était **comment faire cela avec plus de 2 appareils ?** En travaillant dessus lors du hackathon, nous n'avions que 2 téléphones avec nous, donc nous n'avons jamais pensé aux problèmes que nous rencontrerions en ajoutant plus d'appareils.

### Devenir assez technique

Si vous n'êtes pas intéressé par les aspects techniques du projet, n'hésitez pas à sauter cette partie et à regarder les démos que nous avons construites avec la bibliothèque.

Prendre un prototype brut et sale et le transformer en une bibliothèque fonctionnelle et réellement utilisable vient avec tout un tas de défis auxquels nous n'avions jamais pensé en construisant le prototype.

#### Quelle est la taille d'un pixel physique ?

Pour une première preuve de concept, nous avons construit un petit test où nous afficherions une image statique et l'étendrions sur deux appareils une fois qu'ils seraient "swipés ensemble".

Après l'avoir fait fonctionner, nous avons réalisé qu'il y avait quelque chose qui n'allait pas : les images ne correspondaient pas tout à fait et le redimensionnement n'était pas correct. Le problème est que, selon la taille et la résolution d'un appareil, 100px peuvent être légèrement plus grands ou plus petits que sur un autre appareil.

![Image](https://cdn-media-1.freecodecamp.org/images/1*--vTIC7L7vEBKdIU5mVKNg.jpeg)
_Exemple de bon alignement mais de mauvaise taille_

Nous avons mesuré plusieurs smartphones et tablettes et avons simplement pris la moyenne de toutes les mesures. Pour Swip.js, nous avons donc déterminé que 60 pixels devraient être équivalents à 1 centimètre, et avons redimensionné le canvas en conséquence.

C'était la clé si nous voulions créer l'impression d'un grand monde de jeu continu, dans lequel vous pouvez regarder avec vos smartphones.

Sans dimensions standardisées, les particules rendues avaient des tailles différentes sur différents écrans.

Malheureusement, nous n'avons pas trouvé de moyen de calculer automatiquement ce facteur d'échelle, donc au premier démarrage de l'application, nous demandons à l'utilisateur d'entrer la longueur diagonale de l'appareil.

### Gestion de l'état

Synchroniser l'état entre plusieurs appareils en temps réel est un problème difficile. Il n'y a pas de temps global car l'horloge interne de chaque appareil peut être réglée sur quelques centaines de millisecondes dans le futur ou quelques millisecondes dans le passé. Le réseau n'est pas toujours fiable et les messages peuvent être retardés ou complètement perdus. Nous n'avons pas abordé tous ces problèmes en détail, mais nous avons visé une solution suffisamment bonne pour tester notre idée.

La logique de l'application réside sur le serveur et les smartphones ne sont que des clients stupides. Le client envoie un événement au serveur si l'utilisateur déclenche une action comme toucher l'écran. Le serveur réagit à ce changement, calcule le prochain état du jeu et envoie cette mise à jour aux clients. De cette façon, les clients reçoivent tous les mêmes changements et ne deviendront pas désynchronisés après un moment. Ce n'est pas une solution parfaite et cela devient laggy si la latence du réseau augmente, mais c'est facile à implémenter et cela fonctionne bien.

Nous avons utilisé Redux pour implémenter ce modèle. Si vous êtes intéressé par les détails techniques, vous pouvez [en lire plus ici !](http://redux.js.org)

![Image](https://cdn-media-1.freecodecamp.org/images/1*m7oX4iW2PSE7YEEK25aDvA.png)
_Modèle Redux dans swip.js_

![Image](https://cdn-media-1.freecodecamp.org/images/1*qdfJZrXiKgWHhgi0Sh83bw.png)
_Deux clusters pour deux appareils pas encore connectés_

Initialement, chaque appareil a son propre cluster. Le développeur peut spécifier ce qui doit se passer lorsque deux appareils sont swipés et donc combinés. Tout cela se passe côté serveur. Dans cet exemple, nous voulons simplement fusionner toutes les balles de la scène.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gp7YYJCjvrUwio9k4y2Fgg.jpeg)
_Les clusters fusionnés_

#### À quoi ressemblait réellement le monde du canvas ?

Vous pouvez imaginer l'« environnement » comme une zone infiniment longue et large. Chaque appareil rend simplement le contenu qui serait visible dans sa zone fenêtrée.

Un appareil démarrera en tant qu'origine. Avec un « swip », un simple geste de pincement, vous définissez deux points de référence qui sont utilisés pour calculer les décalages en tenant compte de la hauteur et de la largeur de l'appareil, ainsi que de la translation physique X et Y du nouvel appareil.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZ8bcIUSSjXV0CxGPbyBgA.png)
_Concept de l'apparence du monde du canvas_

Très bien, puisque nous avons maintenant terminé avec les trucs de geek, voici une autre démonstration pour montrer ce que la bibliothèque Swip.js pouvait faire. Profitez-en !

%[https://www.youtube.com/watch?v=qXOwT0ieOgw]

> À retenir : Ne sous-estimez pas le travail nécessaire pour transformer un concept rapide et sale en un vrai projet !

![Image](https://cdn-media-1.freecodecamp.org/images/1*mwRvmAs9lyRUpsVwQy456w.jpeg)

### Qui nous sommes

#### Paul Sonnentag

Développeur principal, initiateur de l'idée et maître d'œuvre de ce projet

> Consultez-le sur [**GitHub**](https://github.com/paulsonnentag) ou [**Twitter**](https://twitter.com/paulsonnentag)

![Image](https://cdn-media-1.freecodecamp.org/images/1*41HSqei6mb9hp0QV6u-haA.jpeg)
_Paul Sonnentag_

> Un développeur passionné, étudiant en informatique. À l'aise sur le web. Construisant des choses avec JavaScript, Elm et Clojure.

#### Tim Grossmann

Développeur, Façonneur d'idées, Diffuseur de mots et Rédacteur

> Consultez-moi sur [**GitHub**](https://github.com/timgrossmann)**, [YouTube](https://www.youtube.com/channel/UC9_Bk9247GgJ3k9O7yxctFg), [Twitter](https://twitter.com/timigrossmann), [Facebook](https://www.facebook.com/profile.php?id=100000656212416)**

![Image](https://cdn-media-1.freecodecamp.org/images/1*R-Pw8B8Fc6ezoera-1ewSg.jpeg)
_Tim Grossmann_

> Apprenant et développeur passionné. Étudiant en informatique à l'Université des Médias. Impatient de travailler avec des équipes ingénieuses sur des projets stimulants.

#### Merci d'avoir lu, nous aimerions entendre **vos** pensées et opinions à ce sujet, alors n'hésitez pas à commenter ou à me contacter directement [moi](mailto:contact.timgrossmann@gmail.com) ou [Paul](mailto:paul.sonnentag@gmail.com) par [e-mail](mailto:contact.timgrossmann@gmail.com).

![Image](https://cdn-media-1.freecodecamp.org/images/1*mwRvmAs9lyRUpsVwQy456w.jpeg)

N'oubliez pas de nous suivre sur [YouTube](https://www.youtube.com/channel/UC9_Bk9247GgJ3k9O7yxctFg) et de [mettre une étoile à Swip.js sur GitHub](https://github.com/paulsonnentag/swip).

Nous sommes toujours à la recherche de nouvelles opportunités. Êtes-vous d'une grande entreprise technologique et cherchez des stagiaires ou un organisateur d'une conférence JS ? [Veuillez nous contacter](mailto:contact.timgrossmann@gmail.com). Nous aimerions entrer en contact !

> Je serai à Palo Alto pour un stage à partir de septembre et j'aimerais **rencontrer autant d'entre vous que possible** ! Si vous êtes intéressé, [contactez-moi par e-mail](mailto:contact.timgrossmann@gmail.com), je serais ravi d'entrer en contact !