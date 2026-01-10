---
title: 'Tmux en pratique : sessions tmux locales et imbriquées à distance'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-25T20:21:14.000Z'
originalURL: https://freecodecamp.org/news/tmux-in-practice-local-and-nested-remote-tmux-sessions-4f7ba5db8795
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r4K9uyZByd-WyK4WC0s79w.png
tags:
- name: Linux
  slug: linux
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Tmux en pratique : sessions tmux locales et imbriquées à distance'
seo_desc: 'By Alexey Samoshkin

  We discuss tmux features, their relevance for local and remote scenarios, and how
  to setup and configure tmux to support nested sessions

  This is the first part of my tmux in practice article series. It is about using
  and configuri...'
---

Par Alexey Samoshkin

#### Nous discutons des fonctionnalités de tmux, de leur pertinence pour les scénarios locaux et distants, et de la manière de configurer tmux pour supporter les sessions imbriquées

Il s'agit de la première partie de ma série d'articles [tmux en pratique](https://medium.com/@alexeysamoshkin/tmux-in-practice-series-of-posts-ae34f16cfab0). Elle traite de l'utilisation et de la configuration de [tmux](https://github.com/tmux/tmux) v2, de l'utilisation des sessions tmux locales et distantes, et de la manière de supporter un scénario où une session tmux distante est imbriquée dans une session tmux locale.

Avant de commencer à lire, voici un [exemple fonctionnel](https://github.com/samoshkin/tmux-config/) de ma machine. Nous avons une session tmux locale sur OSX à l'intérieur d'iTerm2 (exécuté en mode plein écran). La session locale a 2 fenêtres : « zsh » et « node ».

La fenêtre « zsh » est divisée en 2 panneaux : dans les deux panneaux, nous nous sommes connectés en SSH aux hôtes distants (CentOS7 et Ubuntu14) et avons sauté dans des sessions tmux distantes.

Le panneau inférieur avec la session distante Ubuntu14 est divisé en 2 panneaux, et nous avons 3 fenêtres : shell, mon et logs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*r4K9uyZByd-WyK4WC0s79w.png)
_Les sessions tmux distantes imbriquées coexistent harmonieusement même dans des panneaux côte à côte dans une session tmux locale_

Si vous êtes curieux de savoir comment tout cela fonctionne ensemble, continuez à lire.

### Fonctionnalités

Commençons par passer rapidement en revue les fonctionnalités et avantages de tmux, afin de comprendre leur pertinence pour les scénarios locaux ou distants. Nous devons clarifier pourquoi nous avons besoin de cette fonctionnalité de « tmux imbriqué dans tmux », car à première vue, cela semble assez fou.

1. **Multiplexage de terminal, fenêtres nommées, division de la fenêtre en plusieurs panneaux.** Cela a plus de sens pour l'environnement local, lorsque vous décidez de supercharger votre émulateur de terminal, qui sinon ne supporte pas les fonctionnalités mentionnées. Par exemple, iTerm ou Terminator sont déjà capables de multiplexer un terminal.
2. Configuration et lancement d'une session tmux avec un ensemble préconfiguré de fenêtres et de panneaux, leur disposition, et les commandes exécutées à l'intérieur pour **éviter la corvée de les configurer à nouveau et encore à partir de zéro.** Par exemple :
   - Une session « dev », qui inclut la fenêtre « #1 : shell » avec 2 panneaux pour une utilisation ad-hoc
   - Une fenêtre « #2 : monitoring » avec les panneaux `htop` et `sysdig`
   - Une fenêtre « #3 : log » avec les panneaux `journalctl` et `tail -f app.log`
   - Une fenêtre « #4 : node » exécutant le serveur `node`
   tmux vous permet d'écrire un script pour y parvenir, et si vous préférez une approche de type configuration, regardez [tmuxinator](https://github.com/tmuxinator/tmuxinator). Cela est pertinent pour les scénarios locaux et distants.
3. **Conservez votre état de travail, afin de pouvoir vous détacher et reprendre plus tard avec le même état que vous avez laissé.** Lorsque vous travaillez localement avec plusieurs projets, vous pouvez configurer plusieurs sessions tmux par projet et basculer facilement entre les contextes.
   Sur la machine distante, vous pouvez vous détacher de la session à la fin d'une journée de travail, et revenir à la même session depuis chez vous le soir.
4. **Survivre aux coupures de connexion brutales.** Il s'agit de l'une des fonctionnalités les plus importantes. Supposons que vous vous connectez en SSH à un hôte distant et que vous avez un processus de longue durée. Si la connexion SSH est perdue ou si une coupure physique du réseau se produit, un signal SIGHUP serait envoyé à la shell distante, et celle-ci ainsi que tous ses processus enfants seraient terminés. Tmux rend vos processus distants résistants à de tels risques.

Les fonctionnalités moins importantes, mais qui valent tout de même la peine d'être mentionnées, sont les suivantes :

1. **Une fois que vous avez configuré l'environnement tmux, vous êtes moins dépendant de l'émulateur de terminal parent et de son ensemble unique de fonctionnalités**, et vous pouvez passer à un autre émulateur de terminal avec moins de tracas. Étant un utilisateur d'iTerm2 sur OSX, je peux migrer vers Terminator ou konsole sur Linux en installant ma configuration tmux, et obtenir le même environnement connu auquel je suis déjà habitué.
2. **Partagez votre session distante avec votre collègue, afin de pouvoir collaborer en temps réel.** Je pense que c'est rarement utilisé dans le monde réel, mais cela semble cool. Oui, la programmation en binôme, et d'autres mots à la mode. ?

Ainsi, pour conclure, **tmux est responsable de deux choses principales** :

1. Multiplexage de terminal, gestion des sessions/fenêtres/panneaux
2. Conservation de l'état de la session et survie aux déconnexions pour les scénarios distants

Là où tmux excelle vraiment, c'est le point (2). Concernant le point (1), [certaines personnes soutiennent](https://news.ycombinator.com/item?id=11283955) que tmux enfreint la philosophie Unix, car il essaie de faire deux choses au lieu d'en faire une et de bien la faire, et que (1) ne devrait pas être une responsabilité de tmux.

### Sessions locales et distantes imbriquées

Ainsi, étant donné tout cela, certaines personnes préfèrent utiliser tmux uniquement sur la machine locale, au-dessus de leur émulateur de terminal, le superchargeant avec le multiplexage et la gestion des fenêtres en premier lieu. Les personnes qui passent la plupart de leur temps à se connecter en SSH à des hôtes distants utilisent la nature des sessions persistantes et la résistance aux déconnexions réseau.

**Mais les cas locaux et distants doivent-ils être mutuellement exclusifs ? Puis-je les combiner ?** Oui, il est légal de se connecter en SSH à un hôte distant et de démarrer la session tmux là-bas, tout en étant déjà dans un environnement tmux localement.

Cela s'appelle des sessions imbriquées, mais cela présente quelques obstacles :

Tout d'abord, vous êtes confronté à la question : **Comment pouvez-vous contrôler les sessions internes, puisque toutes les combinaisons de touches sont capturées et traitées par les sessions externes ?**

La solution la plus courante consiste à appuyer deux fois sur `prefix` (prefix est une combinaison de touches qui met tmux en mode commande, généralement c'est `C-b`, mais certaines personnes préfèrent le remapper en `C-a` comme screen). La première pression sur prefix est capturée par la session externe, tandis que la seconde est transmise à la session interne. Aucune étape supplémentaire n'est nécessaire, et cela fonctionne dès la sortie de la boîte.

Cependant, les combinaisons de touches root — celles qui sont écoutées globalement, pas en mode commande — sont toujours capturées par la session externe uniquement. Et j'ai trouvé que c'est vraiment ennuyeux de double-appuyer sur `prefix`. Pour moi, c'est même ennuyeux de l'appuyer une fois, dans iTerm2 il n'y a pas de mode commande, et je presse simplement « `⌘⇧→` » pour sélectionner le panneau de droite, au lieu d'envoyer deux frappes séparées `C-a RightArrow`.

Une autre solution consiste à configurer deux préfixes individuels, par exemple, `C-b` pour une session locale, tandis que `C-a` pour une session distante. Avec la configuration ci-dessous, cela signifie qu'appuyer sur `C-a` localement enverrait le préfixe par défaut `C-b` à la session distante. J'ai trouvé cette solution [ici](https://simplyian.com/2014/03/29/using-tmux-remotely-within-a-local-tmux-session/).

```
set -g prefix C-b
bind-key -n C-a send-prefix
```

Mais cela donne vraiment l'impression que :

![Image](https://cdn-media-1.freecodecamp.org/images/1*GqnVJ6nxi1Otr37LdSYGLg.jpeg)

La meilleure solution serait d'utiliser la même table de touches à la fois sur les sessions locales et distantes — pas de préfixes séparés ou de double pression sur le préfixe — et de désactiver toutes les combinaisons de touches et la gestion du préfixe dans la session externe, lors de l'utilisation de la session interne. [Crédits](http://stahlke.org/dan/tmux-nested/) et ce [problème Github](https://github.com/tmux/tmux/issues/237).

Ainsi, lorsque je vais travailler dans la session interne, je presse simplement `F12` et bascule en mode `OFF` dans la session externe. Lorsque cela se produit, la session externe affiche l'indicateur visuel `OFF` dans la ligne d'état et change le style visuel de la ligne d'état pour souligner davantage que la session est en mode OFF.

Voici un [Gist](https://gist.github.com/samoshkin/05e65f7f1c9b55d3fc7690b59d678734) de ma configuration [tmux](https://github.com/samoshkin/tmux-config) fonctionnelle, que j'ai conçue récemment (seules les parties pertinentes sont incluses) :

En gros, nous configurons la combinaison de touches `F12` pour la table de touches racine. Lorsque pressée, nous définissons le préfixe sur `None`, basculons la table de touches actuelle sur `off`, changeons les styles de la ligne d'état, et forçons tmux à rafraîchir la ligne d'état. Une étape supplémentaire est effectuée pour annuler le mode copie du panneau actuel, s'il est présent. Dès que nous avons basculé sur `off` pour la table de touches et désactivé la gestion du préfixe, la session externe n'écoute plus aucune frappe. Toutes les frappes sont transmises à la session interne sans être interceptées par la session externe.

C'est tout très bien, mais nous devons trouver un moyen de revenir en arrière et de remettre la session externe en mode de fonctionnement normal. C'est pourquoi nous configurons une seule combinaison de touches `F12` dans la table de touches `off`, qui inverse l'effet de la pression initiale de la touche `F12`.

De plus, nous configurons un indicateur visuel pour la ligne d'état, qui s'affiche lorsque la table de touches actuelle est `off`, et se cache sinon.

Pour conclure, étant donné cette configuration, vous pouvez configurer une seule session locale avec 1 fenêtre avec 2 panneaux qui contient des sessions distantes imbriquées vers différents hôtes (voir l'image au début de l'article).

### Configuration spécifique de la session distante

Dans l'exemple précédent, vous avez peut-être remarqué que la ligne d'état de la session externe est positionnée en haut, tandis que la session interne a sa ligne d'état en bas. Cela fournit une distinction visuelle agréable et ne fait pas que les lignes d'état se superposent.

Mais comment est-il possible d'appliquer différentes configurations basées sur des conditions ?

Eh bien, c'est plutôt facile. Nous pouvons détecter si la session est distante ou locale par l'existence de la variable d'environnement `SSH_CLIENT`.

```
if-shell 'test -n "$SSH_CLIENT"' \
  'source-file ~/.tmux/tmux.remote.conf'
```

Et le fichier `~/.tmux/tmux.remote.conf` contient la configuration qui sera appliquée uniquement à la session distante. Là, nous changeons la position de la ligne d'état, et supprimons certains widgets (comme l'horloge et la batterie) car ils répliquent simplement les mêmes widgets de la session locale.

Ainsi, c'est tout. Si vous voulez voir tout cela en action, consultez mon dépôt [tmux-config](https://github.com/samoshkin/tmux-config).

### Ressources et liens

Code source de tmux/tmux — [https://github.com/tmux/tmux](https://github.com/tmux/tmux)

Utilisation de Tmux à distance dans une session Tmux locale | Simply Ian — [https://simplyian.com/2014/03/29/using-tmux-remotely-within-a-local-tmux-session/](https://simplyian.com/2014/03/29/using-tmux-remotely-within-a-local-tmux-session/)

Tmux imbriqué — [http://stahlke.org/dan/tmux-nested/](http://stahlke.org/dan/tmux-nested/)

Activer/désactiver toutes les combinaisons de touches · Problème #237 · tmux/tmux — [https://github.com/tmux/tmux/issues/237](https://github.com/tmux/tmux/issues/237)

Configuration tmux de samoshkin : Configuration tmux qui supercharge votre tmux pour créer un environnement de terminal confortable et cool — [https://github.com/samoshkin/tmux-config](https://github.com/samoshkin/tmux-config)