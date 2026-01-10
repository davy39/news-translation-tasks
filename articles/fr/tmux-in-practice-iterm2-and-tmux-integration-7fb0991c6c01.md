---
title: 'tmux en pratique : iTerm2 et tmux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T00:01:18.000Z'
originalURL: https://freecodecamp.org/news/tmux-in-practice-iterm2-and-tmux-integration-7fb0991c6c01
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gGNWXlll62GCAM55hbldbw.png
tags:
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'tmux en pratique : iTerm2 et tmux'
seo_desc: 'By Alexey Samoshkin

  Benefits and drawbacks of using iterm2 vs tmux locally. How to set up iTerm2 profile
  to override key mappings to trigger analogue tmux actions

  This is 2nd part of “tmux in practice” post series.


  tmux experience inside full-screen...'
---

Par Alexey Samoshkin

#### Avantages et inconvénients de l'utilisation de iTerm2 vs tmux localement. Comment configurer un profil iTerm2 pour remplacer les mappings de touches afin de déclencher des actions analogues de tmux

Il s'agit de la 2ème partie de la série de posts « [tmux en pratique](https://medium.com/@alexeysamoshkin/tmux-in-practice-series-of-posts-ae34f16cfab0) ».

![Image](https://cdn-media-1.freecodecamp.org/images/ENolmODK64FDqsCG3HlDAmw2YW8IGOP5KDL-)
_expérience tmux dans iTerm en plein écran avec 2 sessions distantes imbriquées dans une session locale_

Vous utilisez donc l'émulateur de terminal iTerm2 sur OSX. Et vous avez entendu parler de tmux, et décidé de l'essayer. Google ici, Google là, après un certain temps, vous comprenez des concepts comme le multiplexage de terminal, les fenêtres, la division des panneaux, et comprenez l'utilisation de tmux sur des machines distantes pour persister l'état de la session et survivre aux déconnexions brutales.

À un moment donné, vous pourriez vous demander sur l'utilisation de tmux localement.

> « Étant donné qu'iTerm peut déjà créer plusieurs fenêtres virtuelles dans une seule fenêtre 'physique', peut diviser, échanger et redimensionner les panneaux, ai-je vraiment besoin d'utiliser tmux sur ma machine locale au lieu d'iTerm ? »

Lorsque j'apprenais tmux, je revenais sans cesse à la même question. Ce n'était pas clair sans un peu de pratique. J'ai donc décidé de l'essayer, et aujourd'hui je peux partager les avantages et les inconvénients avec vous.

### iTerm2 vs tmux sur une machine locale : avantages et inconvénients

#### **Avantages :**

* **Fenêtres nommées.** Similaires aux onglets dans iTerm, mais vous pouvez leur donner un nom
* **Une ligne d'état avec des informations système.** Inclut le CPU, la mémoire, l'état en ligne/hors ligne, la batterie, l'utilisateur, l'hôte, et la date et l'heure.
* Ayant une ligne d'état et un ensemble de fenêtres nommées à l'intérieur, je peux passer iTerm en mode plein écran. Cela me permet de travailler dans **un environnement sans distraction** et aussi d'obtenir 3 lignes supplémentaires. Celles-ci étaient auparavant occupées par la barre de menu OSX, le cadre de la fenêtre iTerm et la ligne d'onglets iTerm.
* **Surveiller la fenêtre pour l'activité ou le silence.** Lorsque j'exécute une commande longue dans un panneau, je peux passer à un autre panneau et être notifié lorsque plus aucune sortie n'apparaît dans le panneau précédent pendant un certain intervalle
iTerm a [quelque chose de similaire](https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration), mais il s'agit uniquement de vous notifier lorsque l'exécution revient à l'invite de commande, et nécessite l'installation d'une [intégration shell](https://iterm2.com/documentation-shell-integration.html) supplémentaire
* **Dispositions de panneaux redéfinies.** Even-horizontal, even-vertical, main-horizontal, main-vertical et tiled
* **Capacité à basculer entre plusieurs sessions tmux locales par projet** pour changer facilement de contexte
* Si vous utilisez tmux à la fois localement et sur une machine distante, vous obtiendrez **le même environnement de terminal familier**
* Lorsque vous utilisez tmux, vous dépendez beaucoup moins des fonctionnalités uniques de iTerm2
Cela rend **plus facile la migration vers un autre émulateur de terminal**, que ce soit sur le même OS ou un autre (Linux)

#### **Inconvénients :**

* **tmux maintient son propre buffer de défilement.** Il est plus difficile d'y accéder et de copier du texte que dans iTerm (il suffit de faire défiler et de sélectionner avec la souris)
* **Si vous copiez du texte dans tmux, il est stocké dans le buffer propre à tmux, et n'est pas partagé avec votre presse-papiers OS par défaut.** Pour être 100% correct, le partage avec le presse-papiers système fonctionne dans iTerm2, mais uniquement parce qu'il supporte les séquences d'échappement ANSI OSC 52 qui permettent à des applications comme tmux d'accéder et de stocker des données dans le presse-papiers. iTerm2 est un cas spécial. Essayez simplement de copier du texte dans tmux en cours d'exécution dans le Terminal par défaut d'OSX, qui ne supporte pas OSC52
* Si vous êtes déjà habitué aux raccourcis clavier d'iTerm, **vous devez apprendre et passer aux raccourcis clavier de tmux**, qui sont encombrants. Au lieu d'une simple frappe comme , vous avez besoin de deux frappes : un préfixe suivi d'une autre touche, mappée à une action spécifique de tmux.

Personnellement, j'ai décidé d'avancer avec tmux et ses fonctionnalités, et de moins dépendre des fonctionnalités spécifiques de iTerm2. En effet, en ce moment, j'utilise iTerm juste comme un tunnel vers tmux ?

**Les problèmes avec le buffer de défilement et l'intégration avec le presse-papiers OS sont hautement vitaux, au point que vous pourriez même décider d'abandonner l'adoption de tmux.** Nous aborderons ces sujets dans mes futurs posts.

### Remplacer les mappings de touches d'iTerm pour déclencher une action tmux

Aujourd'hui, voyons comment nous pouvons utiliser les raccourcis clavier familiers d'iTerm tout en travaillant dans un environnement tmux. L'idée est de mapper les frappes de touches dans iTerm pour déclencher des actions tmux.

La méthode facile serait d'aller dans `.tmux.conf` et de mapper les actions tmux à ces raccourcis clavier. Par exemple, pour redimensionner un panneau dans iTerm, nous utilisons « `^` », mappons la même frappe de touche dans tmux de manière quelque peu naïve :

```
bind ^ resize-pane -U
```

Cependant, le code ci-dessus ne fonctionnera pas car vous ne pouvez pas utiliser  dans les raccourcis clavier de tmux, et l'utilisation de SHIFT est également très limitée. Et même si cela était possible, iTerm intercepterait cette frappe de touche avant.

Au lieu de cela, nous configurons un nouveau profil iTerm, et remplaçons les mappings de touches pour envoyer des séquences pré-configurées d'octets, qui déclencheront l'action correspondante dans tmux.

![Image](https://cdn-media-1.freecodecamp.org/images/OTGL8jqmLb6EK9cMaxorINKrWAqffH0Aqgpe)
_Création d'un profil dédié et remplacement des mappings de touches_

Par exemple, lorsque « `^` » est pressé, la séquence d'octets `0x01 0x1b 0x5b 0x31 0x3b 0x35 0x41` est envoyée à travers le terminal à l'instance tmux en cours d'exécution. Elle les interprète comme le raccourci `C-a C-` et déclenche `resize-pane -U` selon notre configuration `.tmux.conf`.

Alors, comment pouvez-vous obtenir ces codes hexadécimaux ? Utilisez les commandes `showkey`, `od` ou `hexdump` pour voir la représentation binaire des pressions de touches du clavier :

```
$ showkey -aAppuyez sur n'importe quelle touche - Ctrl-D mettra fin à ce programme
```

```
^A        1 0001 0x01^[[1;5A  27 0033 0x1b         91 0133 0x5b         49 0061 0x31         59 0073 0x3b         53 0065 0x35         65 0101 0x41
```

**Note** : `showkey` n'est pas disponible sur OSX, mais vous pouvez toujours vous connecter en SSH sur une machine distante Linux et l'utiliser ?. Si cela semble être un énorme surcoût, utilisez simplement `od` ou `hexdump`.

```
$ od -t x1
```

```
^A^[[1;5A   // appuyez sur C-a C- sur votre clavier0000000 01 1b 5b 31 3b 35 410000007
```

Vous pouvez remapper n'importe quelle touche de cette manière, mais je ne le fais que pour les plus courantes, qui ont une action analogue dans tmux.

À la fin de la journée, je peux créer de nouveaux panneaux tmux en utilisant `D` et `D`, sélectionner des panneaux en utilisant ` , ^`Tab pour basculer vers la fenêtre la plus récemment utilisée, ``Enter pour zoomer sur le panneau, `^` pour redimensionner le panneau vers la gauche, `[` pour sélectionner le panneau précédent, `W` pour tuer le panneau actuel, et ainsi de suite. Donc, je n'ai pas besoin de lutter contre ma mémoire musculaire pour les actions les plus courantes.

Pour toutes les autres actions sans correspondance, j'utilise toujours la méthode tmux : le préfixe `C-a` suivi de la touche d'action. Si vous êtes curieux de connaître la liste complète de ces raccourcis clavier, et comment tout cela fonctionne en action, consultez mon dépôt [tmux-config](https://github.com/samoshkin/tmux-config#key-bindings).

De plus, j'ai trouvé les dispositions prédéfinies très utiles : even-horizontal, even-vertical, main-horizontal, main-vertical, tiled. Je travaille généralement dans la disposition main-vertical, et j'ai besoin d'échanger le panneau secondaire avec le panneau principal avant et arrière. C'est si courant que j'ai décidé de configurer un raccourci clavier à la fois dans tmux `(prefix \)` et iTerm `(\)`.

```
# Échanger les panneaux avant et arrière avec le 1er panneau# Lorsque dans les dispositions main-(horizontal|vertical), le panneau le plus grand/large est toujours @1bind \ if '[ #{pane_index} -eq 1 ]' \  'swap-pane -s "!"' \  'select-pane -t:.1 ; swap-pane -d -t 1 -s "!"'
```

En tant qu'étape supplémentaire, vous pouvez configurer ce nouveau profil iTerm comme profil par défaut, et lui dire de sauter dans une session tmux dès le démarrage.

![Image](https://cdn-media-1.freecodecamp.org/images/ma0knlzOuYXJfroPYHaj-VpEyfXeQ7iGizg3)

Et n'oubliez pas de lancer votre iTerm2 en mode plein écran. Cela en vaut la peine.

### Intégration native entre iTerm2 et tmux

Il existe une [intégration entre iTerm2 et tmux](https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration) alimentée par iTerm qui pourrait vous intéresser.

L'idée est qu'iTerm gère toujours les fenêtres et les panneaux, maintient les buffers de défilement, copie/colle comme d'habitude, mais toutes les fenêtres sont soutenues par une session tmux sous le capot. Il s'agit effectivement d'une session tmux, mais abstraite et encapsulée par l'environnement familier d'iTerm pour vous. Vous pouvez fermer iTerm, l'ouvrir à nouveau et vous rattacher à la session précédente, sans perte d'état.

Cependant, cela a peu de sens pour un environnement local (utile uniquement en cas de plantage d'iTerm, ce qui est un événement extrêmement rare). Personnellement, je n'aime pas cette approche, car elle me cache le fait que j'utilise tmux, et n'expose que les fonctionnalités tmux les plus courantes, qui ont des analogues dans iTerm (créer une fenêtre, diviser un panneau, redimensionner une fenêtre/panneau, fermer une session).

### Ressources et liens

Tmuxintegration · Wiki · George Nachman / iterm2 · GitLab — [https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration](https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration)

iTerm2 keymaps pour tmux — Dan Lowe — [http://tangledhelix.com/blog/2012/04/28/iterm2-keymaps-for-tmux/](http://tangledhelix.com/blog/2012/04/28/iterm2-keymaps-for-tmux/)

Auto-Starting Tmux dans iTerm2 — Sašo Matejina — Medium — [https://medium.com/@sasom/auto-starting-tmux-in-iterm2-4276182d452a](https://medium.com/@sasom/auto-starting-tmux-in-iterm2-4276182d452a)

samoshkin/tmux-config : Configuration Tmux, qui supercharge votre tmux pour construire un environnement de terminal confortable et cool — [https://github.com/samoshkin/tmux-config](https://github.com/samoshkin/tmux-config)