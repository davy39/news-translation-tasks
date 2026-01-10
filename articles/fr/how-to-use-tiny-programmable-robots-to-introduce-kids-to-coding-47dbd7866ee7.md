---
title: Comment utiliser de petits robots programmables pour initier les enfants au
  code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-23T02:49:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-tiny-programmable-robots-to-introduce-kids-to-coding-47dbd7866ee7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KzSnqWrTeJrq6otN4JfWPQ.jpeg
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment utiliser de petits robots programmables pour initier les enfants
  au code
seo_desc: 'By Tim Grossmann

  You might be asking yourself, “Eh, why do I really care about whether kids learn
  to code?” Well I can assure you that you’re not the only person who has thought
  this. You might not even have kids of your own, so why should you care?

  ...'
---

Par Tim Grossmann

Vous vous demandez peut-être : « Eh bien, pourquoi devrais-je vraiment me soucier de savoir si les enfants apprennent à coder ? » Eh bien, je peux vous assurer que vous n'êtes pas la seule personne à avoir eu cette pensée. Vous n'avez peut-être même pas d'enfants, alors pourquoi devriez-vous vous en soucier ?

> _«_ Que vous souhaitiez découvrir les secrets de l'univers ou que vous vouliez simplement poursuivre une carrière au XXIe siècle, la programmation informatique de base est une compétence essentielle à apprendre. _»_  
>   
> _— Stephen Hawking_

Et cela s'applique aux enfants, ainsi qu'aux parents et aux grands-parents.

Cet article ne traite pas du codage, il s'agit d'apprendre aux enfants à réfléchir et à résoudre des problèmes de manière structurée.

Il y a 6 ans, le pionnier de Netscape Marc Andreesen a publié un essai dans le Wall Street Journal intitulé « [Why Software is Eating the World](https://a16z.com/2016/08/20/why-software-is-eating-the-world/) ».

Cet article a maintenant presque 6 ans, ce qui montre que même à l'époque, c'était un sujet brûlant. Et sa popularité a crû de manière exponentielle. Vous ne devriez donc pas protéger vos enfants de ce qui les aidera à l'avenir.

Lisez [ce lien](https://github.com/robotopia-x/robotopia) pour voir comment la création d'un outil qui aide les bibliothèques, les écoles et les institutions éducatives a rendu l'enseignement amusant et divertissant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M8wXRadYOT8cRoHHBVVr5Q.png)

### Pourquoi enseigner le code à vos enfants ?

Travailler avec des enfants est génial. Les voir apprendre plus vite, être plus créatifs et concentrés sur leur vision a le potentiel de remplir votre temps libre avec quelque chose qui compte.

Nous avions animé des ateliers [Scratch](https://scratch.mit.edu) et [Makey-Makey](http://www.makeymakey.com) pendant près d'un an avant de décider de créer un nouvel outil capable d'apprendre la logique et d'enseigner les bases de la programmation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KzSnqWrTeJrq6otN4JfWPQ.jpeg)
_Atelier Makey-Makey à la bibliothèque municipale de Stuttgart_

Lorsque nous avons donné aux enfants la tâche de créer un nouveau réveil, ils ont proposé des solutions très créatives. Beaucoup d'entre elles sembleraient vraiment bizarres, du moins pour nous.

Il y a eu de nombreuses fois où j'ai pensé que je n'aurais pas pu imaginer leurs solutions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VhMjYhZ3dNAwDoyVz2J-UQ.jpeg)
_L'une des solutions pour la tâche du réveil_

Nous avions initialement pensé à utiliser une plateforme similaire à [CodeCombat](https://codecombat.com) ou [Code.org](https://code.org). Cependant, avec CodeCombat, vous devez « écrire du code », ce qui n'était pas ce que nous voulions. Et Code.org était vraiment facile, trop facile en fait, pour notre cas d'utilisation.

Nous voulions que la plateforme offre une courbe d'apprentissage abrupte à ses utilisateurs. Avec des niveaux commençant très facilement puis progressant rapidement vers un niveau de difficulté plus élevé afin que les utilisateurs puissent en tirer le meilleur parti. Comme nous savions que cet outil serait utilisé lors d'événements (ce qui est décrit plus loin), nous pouvions faire en sorte que certains niveaux fournissent de l'aide et des explications.

Nous avons également fait des recherches sur certains des outils déjà publiés et disponibles. Cela nous a aidés à avoir une meilleure vue d'ensemble des avantages et des inconvénients des jeux et outils déjà établis. Nous avons documenté cette recherche [ici](https://github.com/robotopia-x/research).

Après avoir fait nos recherches et rencontré des professeurs et le chef de projet [Per](https://github.com/pguth), nous (notre consultant technique [David](https://github.com/queicherius), [Paul](https://github.com/paulsonnentag), [Johannes](https://github.com/H3rby7) et [moi](https://github.com/timgrossmann)) savions où nous allions avec notre voyage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4yRoS85JdnCN5D7itI-pyw.png)

### L'idée

Notre idée était que le programme convienne aux jeunes enfants tout en n'effrayant pas les plus grands.

D'abord, nous avons pensé à simplifier la partie informatique en utilisant le monde de la magie. L'idée était d'introduire les concepts de programmation en utilisant différents sorts enseignés par un petit magicien. Cela nous aurait donné l'avantage de fournir de la « magie » lorsqu'une logique plus complexe était nécessaire, comme dans le cas de la recherche de chemin (pathfinding).

Les enfants pourraient ensuite plus tard observer la logique derrière ces sorts « magiques » et comprendre comment la recherche de chemin a été implémentée avec la logique de base qu'ils avaient apprise.

![Image](https://cdn-media-1.freecodecamp.org/images/1*F-Sfw3DJpEGWPnBiIduVuA.jpeg)
_L'une des premières maquettes de l'idée du magicien_

Après de nombreuses itérations et discussions, nous avons décidé d'adopter une approche moins conte de fées et d'utiliser des [robots](http://github.com/robotopia-x/robotopia) qui pourraient être « programmables » avec les blocs logiques fournis. Les robots seraient générés à partir d'une usine où ils recevraient leur comportement lors de la production.

Les utilisateurs ont la possibilité de construire des robots capables d'effectuer différentes tâches, comme extraire des ressources ou trouver et combattre d'autres robots.

C'est à ce moment-là que [Robotopia](http://robotopia.co/) (à l'époque appelé « Project-X ») est né.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VJXBZB4M9i_Zj5BLXYhB0w.jpeg)
_Logo de Robotopia_

[Per](https://github.com/pguth), notre chef de projet, a décidé que pour apprendre le plus de ce projet, nous devions utiliser des frameworks et des technologies plus expérimentaux.

Il nous a présenté un Framework JavaScript front-end inconnu (du moins à l'époque) qui permettait une belle approche fonctionnelle. Cela nous a rappelé [Elm](http://elm-lang.org).

L'outil s'appelait [Choo](https://github.com/choojs/choo). N'hésitez pas à y jeter un œil. C'est génial.

La communication pour le mode événement devait fonctionner avec une communication Peer2Peer (P2P). [Johannes](https://github.com/H3rby7) est devenu notre chercheur P2P. Son rôle était d'établir une connexion solide avec nos étudiants.

Si vous êtes intéressé, vous pouvez approfondir les technologies utilisées dans la section La tech. De là, vous pourrez probablement en apprendre davantage sur des outils dont vous n'avez jamais entendu parler auparavant (du moins, c'est ce qui m'est arrivé).

La partie la plus importante du projet était probablement l'interface utilisateur. Nos utilisateurs étaient des enfants et de jeunes adultes qui n'avaient jamais codé auparavant. Par conséquent, nous devions choisir une interface qui ne simplifiait pas le codage, mais facilitait l'assemblage et le test des éléments.

C'est ainsi que nous avons trouvé [Blockly.](https://developers.google.com/blockly/)

C'était le choix parfait pour notre projet. Il était facile à intégrer, modulaire et, plus important encore, compatible JavaScript. Vous pouvez [visiter son site web](https://developers.google.com/blockly/) pour vous faire une idée de sa puissance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eZBiG3kdKhuuKOfi8ISgCA.png)
_Un exemple du langage de programmation Blockly_

Note : Découvrez Blockly et envisagez de l'utiliser pour votre prochain projet. Il est facile à intégrer et possède de puissants générateurs de code pour tous les principaux langages de programmation. Ce n'est pas seulement pour les enfants, cela donne aussi aux non-programmeurs un forum pour construire une logique complexe.

Pour plus d'informations, [cliquez ici](https://developers.google.com/blockly/).

C'est la bonne combinaison d'outils qui nous a donné l'élan nécessaire pour concrétiser [Robotopia](http://robotopia.co).

![Image](https://cdn-media-1.freecodecamp.org/images/1*QeJNqsYAp5tF2dIyj6UggQ.png)

### Le jeu

Une fois que nous avons eu notre idée et notre pile technologique en place, nous avons enfin pu commencer à coder.   
Mais comme nous n'avions jamais travaillé avec ces outils auparavant, nous avons dû passer par une courbe d'apprentissage abrupte afin de gagner de l'élan et de donner au projet l'attention qu'il méritait.

Nous avons utilisé tout notre temps libre pour créer ce projet. Au début, nous avons même participé à un week-end de Hackathon pour pouvoir coder tout le week-end. Pour la logique de base du jeu, nous n'avions que deux développeurs et environ quatre mois seulement pour inclure tous les cours et tests de ce semestre. Johannes s'est d'abord occupé de la logique d'événement P2P et a développé un mini-jeu (qui a été abandonné plus tard), qui aurait créé un meilleur engagement dans le mode événement.

Le week-end du Hackathon, où nous avons passé plus de 20 heures à coder, s'est avéré précieux. Dès le premier jour, nous avions quelque chose qui pouvait être montré aux gens. Nous avions un éditeur et une figure que nous pouvions déplacer sur une grille en utilisant le [langage de programmation graphique Blockly.](https://developers.google.com/blockly/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YnsSQmrAeoB4ROiNqxhrsQ.png)
_Une ancienne version avec Robot Rick encore dans le programme_

Comme nous n'avions pas d'artiste capable de fournir des ressources graphiques, nous devions nous assurer que nos outils n'avaient pas l'air de mauvaise qualité. Comme nous sommes de grands fans de [Rick and Morty](http://www.adultswim.com/videos/rick-and-morty), même si ce n'est pas adapté aux enfants, nous avons utilisé certaines ressources de leurs jeux mobiles pour embellir notre outil.

À l'approche de notre date limite, nous avons remplacé les ressources Rick and Morty par des robots. Nous nous sommes également assurés que les gens puissent jouer à notre jeu en utilisant [ce site web](http://robotopia.co/).

La version finale offrait une belle vue d'ensemble, où les gens peuvent visiter les niveaux précédents, consolidant ainsi leurs connaissances.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9OiVbtvOC9uZBgDGX8N-vw.png)
_Une liste de tutoriels séparés par sujet_

Après avoir sélectionné un niveau, vous recevrez des informations sur les objectifs du niveau. Ensuite, vous pouvez résoudre le niveau en utilisant une quantité présélectionnée de blocs. Cela nous a donné la chance d'ajouter progressivement des blocs de plus en plus complexes dans les niveaux suivants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*42UIG_YOTiVKkevVPCmAXg.png)
_Niveau des conditions If (avancé)_

Une fois que les utilisateurs réussissent un niveau, ils reçoivent un résumé des objectifs qu'ils ont atteints, « débloquant » un nouveau bloc pour les niveaux suivants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kbtDlqmG1DQQEANeOazy2Q.png)
_Déblocage d'un nouveau bloc pour les niveaux suivants_

#### **Que la compétition commence**

Après que les enfants ont appris ce que font les blocs, nous avons testé leurs connaissances en organisant une compétition où ils essaient d'extraire le plus de ressources possible dans le temps le plus court.

Pour cela, nous avons dû construire deux vues différentes.

Les utilisateurs peuvent utiliser l'[éditeur Robotopia](http://robotopia.co/#editor) pour aider à construire la logique de leurs robots et tester leur implémentation, tout en améliorant en permanence leur comportement.   
Les utilisateurs saisissent leur nom d'affichage et la salle qu'ils souhaitent rejoindre (les salles sont les compétitions qui peuvent être ouvertes avec la vue présentateur).

![Image](https://cdn-media-1.freecodecamp.org/images/1*a5h6wi1PqgzpJWS1Cl0LKQ.png)
_Les utilisateurs peuvent développer leur propre logique pour gagner_

La [vue présentateur](http://robotopia.co/#presenter) est projetée avec un projecteur à une classe d'enfants, afin qu'ils puissent voir la compétition. Dans cette vue, les utilisateurs peuvent entrer un nom de salle, que les utilisateurs peuvent utiliser pour rejoindre la compétition. Dans cette vue, vous pouvez voir le nombre de points de chaque utilisateur et le temps restant avant la fin de la manche.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ai5Q8UjPwyU2-HIP4ykicQ.png)
_Deux utilisateurs peuvent jouer l'un contre l'autre. Leurs robots seront générés à partir des usines grises._

Après notre présentation, nous avons reçu beaucoup de retours positifs. Cela a renforcé notre confiance. Nous avons ensuite montré la présentation à une classe d'enfants et avons travaillé avec eux à travers les différents niveaux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bvwbgzGTd7v5ujGPYpLmZA.jpeg)
_Épuisés mais heureux. Notre équipe : Paul, Per, Tim et Johannes (de gauche à droite, de haut en bas)_

Voici une très courte impression de l'événement :

%[https://www.youtube.com/watch?v=9aIa5Etqv5E]

![Image](https://cdn-media-1.freecodecamp.org/images/1*Og9Gj3Quh8mrPe3J94eUrg.png)

### La tech

Per avait quelques jalons pour notre projet. En plus de tester réellement ce que nous avions imaginé ensemble, il voulait que nous utilisions la « scène » open source. Ce que cela signifiait pour nous, c'est que nous étions encouragés à utiliser de petites bibliothèques JavaScript et à signaler aux développeurs les problèmes que nous rencontrions.

Per a eu l'opportunité de contacter et de demander au créateur de Choo, [Yoshua](https://medium.com/@yoshuawuyts), de le rencontrer lors d'une réunion en ligne. C'était pour nous lancer avec Choo !

Même si la réunion n'a pas eu lieu (à cause d'un accident de vélo de Yoshua), nous avons pu discuter avec Yoshua de Choo à au moins deux occasions différentes.

Nous avons également soumis quelques correctifs (patches) à d'autres projets open source via GitHub. ?

**Leçon apprise :** Si vous réalisez un projet qui implique une technologie open source, foncez. Contactez le créateur. Dans la plupart des cas, le créateur sera ravi de vous aider. Derrière les très gros projets, il n'y a que quelques personnes qui aiment réellement travailler avec du contenu open source. Ils veulent juste montrer ce qu'ils ont fait et que les gens les utilisent.

#### Blockly

Comme expliqué précédemment, nous avons choisi Blockly pour notre interface utilisateur. Si vous visitez [leur page web](https://github.com/google/blockly) et consultez leurs exemples, vous verrez qu'il a déjà établi de nombreux outils pédagogiques. Comme la conception abstraite facilite la création de nouveaux blocs, vous pouvez l'intégrer dans n'importe quel jeu ou application de votre choix.

La façon dont les individus et, surtout, les enfants utilisent les différents blocs de codage pour créer le comportement est unique. Les blocs de différentes couleurs permettent d'associer facilement chaque bloc à un comportement. De plus, les développeurs sont libres de fournir quelques blocs lors de l'introduction de nouveaux concepts. Une autre fonctionnalité incroyable de ce Framework est que vous pouvez facilement passer de l'empilement de blocs à l'écriture de code, puis basculer rapidement entre les deux.

#### **Fonctionnalités**

Voici quelques fonctionnalités de Blockly :

* C'est un langage de programmation graphique
* Il vous permet de créer et de styliser vos propres blocs
* Il est compatible avec le Web et les appareils mobiles
* Il est établi dans [de nombreux projets](https://code.org)
* Il a la capacité d'interpréter la plupart des langages

#### **Même des projets comme [Micro:bit de Microsoft](https://microbit.org/code/) utilisent Blockly pour enseigner.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Quc8cROYUf-kkRogicMucg.png)
_Le Jeu de la Vie sur Micro:bit_

#### [Peer2Peer](https://en.wikipedia.org/wiki/Peer-to-peer)

La technologie Peer2Peer (P2P) est cool.

Pourquoi ? Parce qu'elle permet aux développeurs de créer des applications qui non seulement offrent d'excellentes fonctionnalités, mais réduisent également les dépendances vis-à-vis des services centraux.

Heureusement pour nous, les grands acteurs du marché (notamment Google) ont réussi à rendre le P2P disponible sur le navigateur. La technologie s'appelle [WebRTC](https://webrtc.org) et est un standard Web — ce qui signifie qu'elle est disponible sur le navigateur via JavaScript.

Une partie des spécifications de notre projet consistait à avoir le moins d'infrastructure back-end possible. Donc pas de serveurs lourds, juste une simple page HTML avec du JavaScript. Nous devions gérer l'état de notre jeu côté client en utilisant uniquement des serveurs de signalisation WebRTC (qui peuvent être comparés à des annuaires numériques) pour initier la connexion P2P.

#### **Fonctionnalités**

Voici quelques fonctionnalités du P2P :

* Il est décentralisé
* Il est disponible pour le Web ([WebRTC](https://webrtc.org))
* Il est facile à utiliser ([simple peer](https://github.com/feross/simple-peer))
* Il utilise uniquement un serveur de signalisation pour la connexion initiale

![Image](https://cdn-media-1.freecodecamp.org/images/1*I-6kCsVhSchBzQPQ8prFWg.jpeg)
_Source photo : [curlewresearch.com](https://curlewresearch.com/wp-content/uploads/2016/05/Server-P2P.jpg" rel="noopener" target="_blank" title=")_

Vous pouvez faire des choses géniales avec la technologie P2P. Par exemple, vous pouvez envoyer des fichiers entre clients sans autorité centrale. Vous pouvez le faire dans votre navigateur. Pour un exemple de cela, cliquez [ici](https://github.com/perguth/peertransfer).

Si vous voulez passer au niveau supérieur, vous pouvez construire un clone de [Spotify](https://www.spotify.com/ca-en/) entièrement décentralisé et open source (PeerMusic). Cliquez [ici](https://github.com/peermusic/peermusic) pour voir un exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4Jua9sz3h5xwVfbu-xwXCw.png)
_Peermusic est un lecteur de musique prêt pour le mobile qui exécute le navigateur localement. Il s'efforce de fournir toutes les fonctionnalités pratiques des lecteurs de musique modernes en les combinant avec un partage de fichiers musicaux facile et crypté basé sur le P2P._

#### Choo

Choo est un langage de programmation amusant et fonctionnel utilisé pour créer des applications front-end robustes. Les développeurs de Choo avaient une philosophie spéciale en tête lorsqu'ils l'ont créé. Ils pensaient que la programmation devait être amusante et légère, pas stressante, et qu'il est cool d'être mignon. Et que l'utilisation de mots techniques sans les expliquer donne de mauvais résultats et fait fuir les gens.

Vous devriez lire la philosophie de Choo sur sa page de [dépôt GitHub](https://github.com/choojs/choo). C'est intéressant et inspirant.

#### **Fonctionnalités**

Voici quelques fonctionnalités de Choo :

* Son poids minimum est de 4 ko
* Il est basé sur les événements
* C'est une petite API avec seulement six méthodes
* Il a un outillage minimal
* Il a une conception isomorphe qui s'affiche de manière transparente avec Node et les navigateurs
* Il est très mignon. Choo choo !

Le genre de « Hello World » pour les langages de programmation fonctionnelle est une application « Counter ». Avec Choo, cela ressemble à quelque chose comme ça.

```js
var html = require('choo/html')
var log = require('choo-log')
var choo = require('choo')

var app = choo()

// l'insertion de middleware est aussi simple que cela
app.use(log())
app.use(countStore)

// avez-vous déjà vu une définition de routes aussi simple que celle-ci ?
app.route('/', mainView)
app.mount('body')

// les vues, les pages rendues, peuvent être configurées aussi facilement que cela
function mainView (state, emit) {
  return html`
    <body>
      <h1>le compte est ${state.count}</h1>
      <button onclick=${onclick}>Incrémenter</button>
    </body>
  `

  function onclick () {
    emit('increment', 1)
  }
}

function countStore (state, emitter) {
  state.count = 0
  emitter.on('increment', function (count) {
    state.count += count
    emitter.emit('render')
  })
}
```

Cela a l'air facile et léger, n'est-ce pas ? Si vous êtes intéressé, vous devriez absolument y jeter un œil. Ils ont beaucoup de [ressources formidables](https://github.com/choojs/choo-handbook).

#### [Esper.js](https://github.com/codecombat/esper.js)

Il s'agit d'un génial auto-interprète JavaScript mettant l'accent sur le test de l'exécution et l'introspection au moment de l'exécution. À notre avis, ce programme n'est pas aussi réputé qu'il devrait l'être compte tenu de sa qualité.

Malheureusement, il n'y a pas de véritable documentation pour [esper.js](https://github.com/codecombat/esper.js). Il n'y a que les commentaires dans le code et quelques explications mineures, ce qui le rend difficile à utiliser. Mais cela vaut vraiment le coup d'œil. Il y a un interprète sur la page Blockly. Mais pour notre cas d'utilisation, ce n'était pas suffisant. Et nous sommes simplement tombés amoureux d' [esper](https://github.com/codecombat/esper.js).js. Merci à [CodeCombat](https://github.com/codecombat) pour le passage en open source. ?

#### **Fonctionnalités**

Voici quelques fonctionnalités d'esper.js :

* Il possède un interprète JavaScript
* Il dispose d'un environnement de test pour son exécution
* Il est conçu pour CodeCombat
* Il permet des exécutions étape par étape
* Il construit un [Arbre de Syntaxe Abstraite](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (AST) complet

Pour voir la démo réelle, cliquez [ici.](http://esper.chessgears.com)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zmfgpYLCAE3jwUn-Ae5NIw.png)
_Démo d'esper.js_

#### Le moteur de robot

Lorsque deux équipes s'affrontent, en mode tournoi, nous avons besoin d'un environnement qui simule l'interaction des robots avec le monde du jeu. Chaque robot a son propre programme, et chacun effectue une action à chaque tour. Le runtime suit l'état de chaque robot et du monde du jeu. À chaque événement cadencé, le runtime exécute l'action suivante de chaque robot et envoie un événement au monde du jeu.

Le monde du jeu contient toute la logique du jeu. Par exemple, il est responsable de vérifier que les robots ne peuvent pas se déplacer sur des champs d'eau.

#### **Fonctionnalités**

Voici les fonctionnalités du moteur de robot :

* Il fournit une simulation au tour par tour
* Il permet des exécutions simultanées de plusieurs robots
* Il possède un système d'événements qui déclenche les bots, par exemple lorsqu'un robot découvre une ressource
* Il fournit une API pour que les robots interagissent avec le monde

![Image](https://cdn-media-1.freecodecamp.org/images/1*W-oQ4VU5Rfdss8iZljifIA.png)
_Concept du moteur de robot_

![Image](https://cdn-media-1.freecodecamp.org/images/1*O1PDaIHooYcpKV4dTGiujA.png)

### Vous pouvez aider

Si vous pensez que ce projet est intéressant et que vous souhaitez planifier votre propre événement, parfait.

Rendez-vous simplement sur notre [dépôt GitHub](https://github.com/robotopia-x/robotopia) et cherchez la section **«** How you could use this ». Elle explique comment vous pouvez reprendre ce projet et en faire votre propre événement.

Voici les choses dont vous aurez besoin pour organiser un événement comme celui-ci :

#### Éléments nécessaires pour planifier un événement

* Environ 1,5 heure
* Un ordinateur avec un navigateur à jour pour chaque enfant
* Un projecteur et un grand écran pour afficher la compétition
* Des tuteurs qui peuvent aider les enfants s'ils ont des questions

L'événement est ensuite divisé en 4 sections :

* Tutoriels
* Programmation des robots
* Faire concourir les robots
* Amélioration des programmes

Vous pouvez lire chacune des étapes [ici](https://github.com/robotopia-x/robotopia).

Si vous avez des questions sur la manière et l'endroit où organiser un tel événement, ou sur la meilleure façon de le planifier, [n'hésitez pas à nous demander](mailto:contact.timgrossmann@gmail.com).

Nous adorons travailler avec les enfants. Si vous essayez, nous sommes sûrs que vous ne le regretterez pas. Vous apprendrez à expliquer les choses d'une manière plus simple et plus logique, ce qui vous aidera à grandir en tant que développeur et en tant que personne.

#### Essayez. Nous sommes sérieux. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*AZfK04kDjs6dG_WMFBnCVw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*RYYzZpYuWUQS5v-QNBruew.png)

#### Merci de votre lecture.

#### Nous aimerions connaître votre opinion, alors n'hésitez pas à commenter ou à [me contacter par e-mail](mailto:contact.timgrossmann@gmail.com).

Assurez-vous également de nous suivre sur [YouTube](https://www.youtube.com/channel/UC9_Bk9247GgJ3k9O7yxctFg) et de [donner une étoile à Robotopia sur GitHub.](https://github.com/robotopia-x/robotopia)

N'oubliez pas de cliquer sur le bouton clap et de me suivre sur [Twitter](https://twitter.com/timigrossmann), [GitHub](https://github.com/timgrossmann), [Youtube](https://www.youtube.com/channel/UC9_Bk9247GgJ3k9O7yxctFg) et [Facebook](https://www.facebook.com/profile.php?id=100000656212416) pour me suivre dans mon voyage.

Nous sommes toujours à la recherche de nouvelles opportunités.

[N'hésitez pas à nous contacter](mailto:contact.timgrossmann@gmail.com). Nous serions ravis d'être en contact avec vous.

**Je serai à Palo Alto, en Californie, pour un stage commençant en septembre. J'aimerais beaucoup vous rencontrer ! Si vous êtes intéressé, [contactez-moi par e-mail](mailto:contact.timgrossmann@gmail.com). Je serais heureux d'être en contact !**

**De plus, si vous êtes quelqu'un qui travaille réellement chez Google et que vous lisez ceci, j'aimerais beaucoup rencontrer l'équipe derrière Blockly !**