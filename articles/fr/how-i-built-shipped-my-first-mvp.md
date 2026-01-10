---
title: Comment j'ai construit et livré mon premier MVP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-15T13:15:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-shipped-my-first-mvp
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-11-at-8.05.29-PM.png
tags:
- name: JavaScript
  slug: javascript
- name: lessons learned
  slug: lessons-learned
- name: mvp
  slug: mvp
seo_title: Comment j'ai construit et livré mon premier MVP
seo_desc: "By JavaScript Joe\nOn June 29th, I shared the MVP of mentored.dev on Twitter–my\
  \ first \"real\" project that was bigger than anything I'd built before and something\
  \ I was excited for other people to use. \nhttps://twitter.com/jsjoeio/status/11449945802002..."
---

Par JavaScript Joe

Le 29 juin, j'ai partagé le MVP de [mentored.dev](https://mentored.dev) sur Twitter – mon premier projet "réel" plus important que tout ce que j'avais construit auparavant et quelque chose que j'étais excité de voir d'autres personnes utiliser. 

%[https://twitter.com/jsjoeio/status/1144994580200210432?s=20]

Après avoir partagé cela, j'ai reçu quelques retours positifs, y compris une mention dans la [newsletter hebdomadaire npm](https://t.co/7sCziRMC9f?amp=1). 

J'ai pensé partager l'histoire derrière tout le processus.

## Origine de l'idée

Je ne me souviens pas quand j'ai eu l'idée pour la première fois, mais il y a un moment, quand j'ai été introduit à [TwilioQuest](https://www.twilio.com/quest), je me suis dit, 

> Ne serait-ce pas cool de construire une plateforme d'apprentissage "gamifiée" qui vous apprend à coder ?

Comme beaucoup d'autres personnes, j'ai ces idées à des moments aléatoires tout au long de ma vie. Je garde une liste de ces idées dans un tableau [Trello](https://trello.com/en-US) appelé "IDÉES". En regardant ici, je peux voir que j'ai noté cela le 21 janvier 2019. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/trello-card1.gif)
_Tableau Trello avec l'idée originale du 21 janvier_

Je savais quelques choses :

* Je voulais que ce soit interactif
* Je voulais que cela ressemble à un jeu
* Je voulais que cela ait des exercices rapides

---

## Par où commencer ?

À peu près à la même époque, je terminais un projet freelance (porter un thème Jekyll vers un site Gatsby), donc je ne me sentais pas prêt à commencer tout de suite. Ensuite, j'ai eu une conversation avec [@signalnerve](https://twitter.com/signalnerve) sur Twitter qui a déclenché ma motivation :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-09-at-6.20.11-PM.png)
_Capture d'écran de la conversation Twitter qui m'a motivé à commencer._

> Construisez une petite application – un vrai MVP – validez votre idée et décidez ensuite si vous devez continuer à construire. 

Alors je me suis dit, "Pourquoi pas commencer ?"

---

## Mars 2019 

J'ai utilisé un starter Gatsby/TypeScript pour lancer le premier et j'ai poussé mon [premier commit](https://github.com/jsjoeio/mentored.dev/commit/0e38821f30d1f6f1bca804315fe24ccd5d5baf05). À l'origine, j'ai nommé le dépôt "Life of Code" parce que c'est ce qui me venait à l'esprit, mais plus tard, je l'ai renommé après avoir acheté le domaine mentored.dev. 

#### Maquettes initiales

Après avoir créé le dépôt, j'ai esquissé quelques maquettes élémentaires dans [Figma](https://figma.com)

![Image](https://www.freecodecamp.org/news/content/images/2019/07/figma.gif)
_Maquettes initiales dans Figma_

Une fois que j'ai eu tout cela, j'ai surmonté la paralysie initiale du "par où commencer" et j'ai su que je devais maintenir l'élan.

#### Prise en compte des entrées

L'une des premières choses que j'ai essayées a été de demander une entrée utilisateur et de l'afficher dans un message. Cela serait utile pour le dialogue entre le narrateur et l'utilisateur. 

%[https://twitter.com/jsjoeio/status/1103860530605780998?s=20]

### Dialogue de base fonctionnel

Même si ce n'était pas joli, la logique du dialogue fonctionnait ! Cela semblait être une bonne étape car la plupart des choses difficiles étaient faites. 

%[https://twitter.com/jsjoeio/status/1106779197614088192?s=20]

### Narrateur qui parle

J'ai eu beaucoup de mal à trouver la meilleure façon de faire parler le narrateur, mais après avoir trouvé `[react-keyframes](https://github.com/zeit/react-keyframes)`, j'ai pu trouver une solution. C'était énorme car auparavant, je n'avais pas fait grand-chose avec l'animation.

%[https://twitter.com/jsjoeio/status/1107812366891180032?s=20]

### Obtenir des retours sur le dialogue

Comme je l'ai dit plus tôt, je pense qu'il est important d'obtenir des retours des autres. Je ne sais pas si Twitter est le meilleur endroit pour le faire, mais heureusement pour moi, les personnes qui ont répondu à ma demande de retours étaient gentilles.

%[https://twitter.com/jsjoeio/status/1108190126876680193?s=20]

### Migration vers TypeScript

J'ai utilisé un starter Gatsby-TypeScript pour ce projet parce que je voulais apprendre TS. Cependant, jusqu'à ce point, je n'utilisais pas vraiment TS. Les fichiers avaient simplement des extensions .ts ou .tsx.

Avant le 30, j'avais mentionné vouloir apprendre TS et [@TejasKumar_](https://twitter.com/TejasKumar_) a proposé de m'enseigner en migrant la base de code de mentored.dev vers TS lors d'un livestream Google Hangouts. C'était l'un des moments les plus cool de ce projet. Et j'ai appris énormément. 

%[https://twitter.com/jsjoeio/status/1112088320182370304?s=20]

---

## Avril 2019 

### Ajout d'un composant "Carte de profil"

Après avoir terminé la partie dialogue du projet, j'ai décidé de me concentrer sur le tableau de bord – ou la page après vous être connecté. J'ai créé une simple "Carte de profil" qui montrera éventuellement votre expérience, tout code-cash que vous avez, etc.

%[https://twitter.com/jsjoeio/status/1113644342172774400?s=20]

### Conception du tableau de bord

Avec le recul, je me suis peut-être emballé ici car j'ai conçu bien plus que ce que je pouvais implémenter dans le MVP, mais au moins cela m'a donné une idée pour l'avenir. J'ai d'abord ajouté cela en tant que composants codés en dur, mais plus tard, je les ai commentés pour maintenir une UX saine.

%[https://twitter.com/jsjoeio/status/1114009915545141249?s=20]

### Conception de la carte du campus

Cela a pris beaucoup plus de temps que je ne le pensais. Je voulais que cela ressemble à un campus universitaire, mais je me suis fortement inspiré de [Pallet Town](https://bulbapedia.bulbagarden.net/wiki/Pallet_Town) dans Pokémon. La version complète a plus, mais au moins j'avais quelque chose que je pouvais ajouter au tableau de bord. J'ai conçu tout cela dans Figma et je l'ai exporté en SVG. Travailler avec des SVG dans React s'est avéré être une expérience agréable. 

%[https://twitter.com/jsjoeio/status/1114635991191396352?s=20]

### Ajout de musique de gameplay

Je n'avais jamais réalisé à quel point il est difficile de créer ou de trouver de la musique pour un jeu. J'ai fini par trouver cet artiste sonore incroyable nommé [Eric Matyas](https://www.soundimage.org) qui crée de la musique et des sons libres de droits. Je voulais que l'audio démarre automatiquement (car c'est ainsi que la plupart des jeux le font), mais malheureusement, ce n'est pas [accessible](https://a11yproject.com/posts/never-use-auto-play/), donc il ne se lance pas automatiquement. 

Cependant, si vous l'activez au menu de démarrage ou lorsque vous jouez au jeu, cela ajoute une belle touche.

%[https://twitter.com/jsjoeio/status/1115436705346019328?s=20]

### Changement de cartes

Cela doit être ma fonctionnalité préférée que j'ai ajoutée – pouvoir changer de carte. Au début, je n'avais aucune idée de la façon dont j'allais faire cela, puis je me suis dit, "pourquoi ne pas simplement échanger la carte avec une autre carte ?"

C'est exactement ce que j'ai fait et cela a fonctionné ! 

J'ai extrait les parties de la carte qui étaient cliquables (comme les bâtiments) et j'ai fait en sorte qu'elles ouvrent différentes cartes. Je ne sais pas comment bien ma solution évoluera, mais hey, cela fonctionne pour l'instant et c'est ce qui compte. 

%[https://twitter.com/jsjoeio/status/1119834245013196801?s=20]

### Page des cours

L'un des autres défis auxquels j'ai été confronté était de déterminer où et comment montrer les cours (c'est-à-dire le dialogue avec le narrateur).

Même chose – j'ai eu du mal avec cela pendant un moment, puis j'ai décidé, "Affichons-le dans un composant Overlay !"

Cela a bien fonctionné. Encore une fois, je ne sais pas si cela évoluera bien, mais cela fonctionne pour l'instant.

%[https://twitter.com/jsjoeio/status/1123063970468786176?s=20]

---

## Mai 2019

En mai, j'ai pris un peu de repos. Je me mariais, donc je voulais me concentrer sur la préparation de cela plutôt que sur mon jeu. J'avais encore des idées ici et là, mais je n'ai pas mis autant de temps que mars ou avril. 

Même si c'est difficile pour moi de prendre des pauses et de m'éloigner, je pense qu'il est sain de sortir, de changer ce que vous faites, de méditer, etc. Comme le dit toujours ma mère, 

> Tout avec modération. 

---

## Juin 2019

En regardant le tableau de bord que j'ai créé, il restait encore tant à faire. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Dashboard-v1.1.png)

Je me sentais submergé.

"Comment vais-je finir tout cela ?"

### Une prise de conscience à la rencontre Phoenix ReactJS

Je n'étais pas allé à la [rencontre Phoenix ReactJS](https://www.meetup.com/Phoenix-ReactJS/) depuis un moment. Mes deux collègues et moi avons décidé d'y aller pour écouter les talks éclair. 

Avant les talks, nous étions regroupés autour d'une table, discutant de nos projets secondaires. J'ai dit que je voulais terminer le MVP pour mentored.dev d'ici la fin de l'année. 

"Combien te reste-t-il à finir ?" 

"Une quantité décente. Tout sur la page du tableau de bord est codé en dur pour le moment."

"Abandonne tout cela. Termine les fonctionnalités principales et livre-le."

Ce sont les sages paroles de mes collègues. C'est à ce moment-là que j'ai réalisé qu'ils avaient raison. J'ai décidé de réduire la portée et d'implémenter deux dernières fonctionnalités – le suivi des séries et la progression des leçons. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-10-at-8.06.01-PM.png)
_Capture d'écran du suivi des séries_

 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-10-at-8.06.13-PM.png)
_Capture d'écran de la progression des leçons_

La logique du suivi des séries était boguée lorsque je l'ai implémentée pour la première fois et ne fonctionnait pas du tout. Je n'étais pas sûr de savoir si je devais incrémenter la série après 24-48 heures, ou simplement le faire par jour, ou quoi. Cela [semblait beaucoup plus compliqué](https://github.com/jsjoeio/mentored.dev/issues/93) que cela n'aurait dû être. 

Je ne sais toujours pas si je suis satisfait de l'implémentation. Mais encore une fois, c'est sorti et la fonctionnalité de base fonctionne. 

La progression des leçons (terminé - 1/3) est également rudimentaire au mieux. Encore une fois, mon objectif était de le sortir. Je le styliserai à l'avenir. 

### Livrez-le

Le 29 juin. Le grand jour.

%[https://twitter.com/jsjoeio/status/1144994580200210432?s=20]

Comme je le dis dans le fil de tweets, 

> ...Ce n'est nulle part près d'être complet, mais je pense que c'est un bon point d'arrêt pour partager le MVP.

Il y a un moment, j'ai lu _[Lean Startup](http://theleanstartup.com/)_ d'Eric Ries. Une chose qui m'est toujours restée est quelque chose qu'il a dit dans le genre de, "Vous devriez être gêné de mettre votre produit là-bas. C'est à ce moment-là que vous savez que c'est un MVP."

Et c'est ce que je ressentais ! Tant de choses restent à faire. C'est difficile de même le considérer comme un "jeu" – la plupart des vrais joueurs ne le feraient probablement pas. 

Mais c'est le but – cela m'a aidé à soulager un fardeau de mes épaules et à faire un pas en arrière pour entendre ce que les gens pensent. 

La plupart des gens à qui j'ai parlé pensent que c'est un bon début et un concept intéressant. Ils sont excités de voir où cela mène. 

---

## Ce que je pense avoir fonctionné

En réfléchissant à ce qui m'a aidé à lancer ce MVP, quelques choses me viennent à l'esprit. 

### Responsabilité - Amis et Communauté Twitter

Comme nous le savons tous, il est très facile de s'isoler et de travailler seul. Cela peut fonctionner pour certaines personnes et c'est bien. Mais dans mon cas, je pense que le fait de partager ce projet avec mes collègues m'a rendu plus responsable que si je n'en avais parlé à personne. Chaque semaine, le lundi matin, l'un d'eux demandait, "Hey Joe. As-tu travaillé sur ton jeu ?"

Leur intérêt et leur soutien signifiaient beaucoup pour moi. Ils voulaient le voir réussir autant que moi. Cela m'a gardé motivé. 

L'autre partie qui m'a rendu responsable était de le partager avec des personnes sur Twitter. Parfois, les gens commentaient et d'autres fois non. Dans tous les cas, les gens suivaient. Quelques-uns m'envoyaient des DM pour demander comment cela se passait. 

En le partageant en public, j'ai ressenti une certaine pression (de manière positive) pour le terminer. 

### Utilisation de GitHub Projects, Issues et Milestones

J'ai traité ce projet comme nous traitons les applications client/entreprise au travail. Je n'ai pas utilisé de sprints à proprement parler, mais j'ai gardé une liste de tâches dans un [tableau de projet GitHub](https://github.com/jsjoeio/mentored.dev/projects/3) puis j'en ai sélectionné quelques-unes et créé une milestone. Cela a rendu le travail plus réalisable et moins accablant. 

J'ai configuré un environnement de staging à [https://staging.mentored.dev](https://staging.mentored.dev) (grâce à [Netlify](https://www.netlify.com/), cela a été simple). Ensuite, chaque issue que j'ai terminée, j'ai soumis une PR pour fusionner dans staging. Je l'ai revue et fusionnée moi-même (oui, un peu idiot, mais bonne pratique). 

Une fois qu'une [milestone était complète](https://github.com/jsjoeio/mentored.dev/milestones?state=closed), j'ai fusionné staging dans master et créé une nouvelle release. Ce processus m'a mis sur la voie du succès. J'ai gardé les milestones petites (quelque chose que je pouvais terminer en 1-3 semaines). 

Avoir une sorte de gestion de projet en place pour votre projet secondaire, je crois, vous aidera à atteindre la ligne d'arrivée plus tôt. 

### Réduction de la portée

Je n'aurais pas terminé ce MVP si je n'avais pas coupé beaucoup de fonctionnalités. Par exemple, je voulais vraiment créer un dépôt appelé "mentored-dev" après que l'utilisateur se soit connecté et y stocker la progression des leçons. Mais cela allait prendre plus de temps que je ne l'avais anticipé, donc je l'ai coupé. 

À la place, je stocke la progression dans le localstorage. Oui, c'est à court terme, mais encore une fois, j'ai dû réduire la portée pour livrer. Si je ne l'avais pas fait, je n'aurais pas terminé cette phase du projet. 

---

## Réflexions finales

Dans l'ensemble, je me sens reconnaissant pour tout le soutien. Je suis fier du petit projet que j'ai construit et des retours que j'ai reçus, alors merci. En ce qui concerne les prochaines étapes, j'ai déjà créé la [prochaine milestone](https://github.com/jsjoeio/mentored.dev/milestone/6). L'objectif principal est de terminer toutes les leçons sur les bases de la ligne de commande, puis de partager cela pour voir ce que les gens en pensent. 

En ce qui concerne les fonctionnalités réelles – je ne promets rien, mais j'adorerais ajouter des points d'expérience (XP) que vous accumulez en fonction de votre score dans les leçons ou du nombre de fois où vous suivez chaque leçon, de la fréquence à laquelle vous vous connectez, etc. 

Il serait également agréable de donner des XP pour faire des choses en dehors du jeu (c'est-à-dire écrire un article de blog, tweeter quelque chose que vous avez appris, contribuer à l'open source, aider quelqu'un, etc.). Nous verrons ce qui se passe. 

Merci d'avoir écouté le voyage. 

###

Si vous avez aimé cet article ou l'avez trouvé intéressant, veuillez le partager avec d'autres ou faites-le moi savoir sur [Twitter](https://twitter.com/jsjoeio). 

Pour rester à jour sur mentored.dev ou d'autres choses sur lesquelles je travaille, j'ai une newsletter à laquelle vous pouvez [vous inscrire ici](https://github.com/jsjoeio/mentored.dev/milestone/6). 

Bon codage !