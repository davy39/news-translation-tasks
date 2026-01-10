---
title: 'tmux en pratique : le tampon de défilement'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T13:50:16.000Z'
originalURL: https://freecodecamp.org/news/tmux-in-practice-scrollback-buffer-47d5ffa71c93
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WOE01gwjsFx-0gGi5KdZfA.gif
tags:
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'tmux en pratique : le tampon de défilement'
seo_desc: 'By Alexey Samoshkin

  The difference between terminal and tmux scrollback buffers, and how to tweak copy
  mode, scroll, and mouse selection of tmux behavior.

  This is 3rd part of my tmux in practice article series.

  Usually terminal emulators implement sc...'
---

Par Alexey Samoshkin

#### La différence entre le tampon de défilement du terminal et celui de tmux, et comment ajuster le mode copie, le défilement et la sélection avec la souris dans tmux.

Il s'agit de la 3ème partie de ma série d'articles [tmux en pratique](https://medium.com/@alexeysamoshkin/tmux-in-practice-series-of-posts-ae34f16cfab0).

Habituellement, les émulateurs de terminal implémentent un tampon de défilement, afin que vous puissiez explorer les sorties passées, lorsqu'elles disparaissent de la vue. tmux, comme d'autres applications terminal en plein écran comme vim, s'exécute dans ce qu'on appelle le tampon d'écran alternatif du terminal parent. Le tampon alternatif a exactement les mêmes dimensions de largeur et de hauteur que la taille physique de la fenêtre.

Il y a plusieurs effets de l'utilisation du tampon alternatif :

* Toute sortie qui dépasse la partie visible du tampon alternatif est perdue. Dès que les lignes disparaissent de la vue, elles sont perdues. Pour éviter la perte de l'historique, tmux implémente son propre tampon de défilement "interne". La conséquence de cela est que vous ne pouvez pas travailler avec le tampon de défilement interne de tmux de la même manière que vous le faites habituellement dans votre terminal.
* Toute sortie produite à l'intérieur de tmux (la même chose est vraie pour vim, nano, man, less, etc.) ne se déverse pas dans l'historique de défilement du terminal externe. Lorsque vous fermez votre application en plein écran, vous revenez à l'état dans lequel vous étiez lorsque vous avez lancé l'application et ne voyez plus la sortie de l'intérieur de l'application.

En pratique, si vous avez l'habitude de faire défiler vers le haut en utilisant `[1;3A` dans votre iTerm et si vous allez faire de même à l'intérieur d'une session tmux en cours d'exécution, vous allez contrôler et faire défiler le tampon de défilement externe de iTerm, plutôt que le tampon de défilement interne de tmux.

La solution est d'utiliser les contrôles spécifiques de tmux pour accéder à son propre tampon de défilement : `Ctrl-b` puis `[` pour entrer en mode copie, utilisez les flèches `Bas/Haut` ou les touches `PageDown` et `PageUp`, `q` ou `Entrée` pour quitter le mode copie.

Certaines personnes qui trouvent cela ennuyeux configurent le tampon de défilement de tmux pour qu'il puisse être affiché dans le tampon de défilement du terminal parent, afin qu'elles puissent simplement utiliser les contrôles de défilement familiers. [Voir cet article](https://dan.carley.co/blog/2013/01/11/tmux-scrollback-with-iterm2/). Cependant, cette solution est limitée à une session tmux avec 1 fenêtre et 1 panneau uniquement. Et lorsque vous détachez/fermez une session tmux, le terminal parent est pollué avec la sortie de la fenêtre tmux.

Personnellement, j'utilise le tampon de défilement de tmux sans les astuces ci-dessus, mais je modifie sa configuration pour qu'il soit plus convivial et familier.

Tout d'abord, je n'aime pas `prefix,[` pour entrer en mode copie. Je me suis habitué à `[1;3A` pour commencer à défiler dans iTerm, et j'ai ajouté la liaison de touche racine suivante :

```
# déclencher le mode copie parbind -n M-Up copy-mode
```

Une fois que vous êtes en mode copie, vous pouvez continuer à appuyer sur `M-Up` pour faire défiler d'une ligne vers le haut. Les contrôles habituels `PageDown` et `PageUp` sont disponibles pour faire défiler par écran entier, et en plus `M-PageDown` et `M-PageUp` pour faire défiler par moitié d'écran (vraiment pratique).

```
# Faire défiler vers le haut/bas d'une ligne, moitié d'écran, écran entierbind -T copy-mode-vi M-Up              send-keys -X scroll-upbind -T copy-mode-vi M-Down            send-keys -X scroll-downbind -T copy-mode-vi M-PageUp          send-keys -X halfpage-upbind -T copy-mode-vi M-PageDown        send-keys -X halfpage-downbind -T copy-mode-vi PageDown          send-keys -X page-downbind -T copy-mode-vi PageUp            send-keys -X page-up
```

De plus, même lorsque je suis à l'intérieur d'une session tmux, je peux continuer à utiliser `[1;3A` et `[1;3B` pour contrôler le tampon de défilement interne de tmux, plutôt que celui de iTerm. C'est possible en utilisant un profil iTerm personnalisé avec certaines liaisons de touches remplacées pour déclencher des actions tmux. Ainsi, `[1;3A` pressé dans iTerm envoie simplement la frappe `M-Up` à la session tmux.

Lisez ma partie précédente de la série "tmux en pratique" pour plus de détails : [tmux en pratique : intégration d'iTerm2 et de tmux](https://medium.com/@alexeysamoshkin/tmux-in-practice-iterm2-and-tmux-integration-7fb0991c6c01).

Un autre paramètre par défaut de tmux que je préférerais changer est le défilement de la molette de la souris. Il fait défiler de 5 lignes, ce qui semble être un grand saut. Réduisons-le à un défilement de 2 lignes :

```
# Lorsque vous faites défiler avec la molette de la souris, réduisez le nombre de lignes défilées par cran à "2" (par défaut, c'est 5)
```

```
bind -T copy-mode-vi WheelUpPane select-pane \; send-keys -X -N 2 scroll-upbind -T copy-mode-vi WheelDownPane select-pane \; send-keys -X -N 2 scroll-down
```

Maintenant, parlons de la copie de texte une fois que vous êtes en mode copie. J'ai l'habitude de copier du texte en utilisant la souris. Activons le support de la souris :

```
set -g mouse on
```

Par défaut, lorsque vous sélectionnez du texte avec la souris dans tmux, il est copié dans le tampon, et vous êtes immédiatement sorti du mode copie. Votre position de défilement actuelle est réinitialisée à la fin de la sortie, et vous êtes placé en mode invite de commande. Voyons cela en action :

![Image](https://cdn-media-1.freecodecamp.org/images/S61DaFvLkDfW6Q2RmmPkZojMHwxrHj-JZZKN)
_Mode copie désactivé à la fin du glisser-déposer avec la souris_

Comme vous le remarquez, chaque fois que je sélectionne du texte avec la souris, cela me sort du mode copie. C'est vraiment ennuyeux. Habituellement, lorsque je suis bloqué avec une tâche, j'ai tendance à sélectionner du texte ici ou là juste pour méditer (cela m'aide à me concentrer sur ?). Ou vous pourriez vouloir simplement sélectionner du texte pour le mettre en évidence pour votre collègue assis à côté de vous.

Alors, ajustons cela. Nous ne voulons pas être sortis du mode copie. Nous ne voulons pas que la sélection soit effacée à la fin du glisser-déposer avec la souris. Le texte de la sélection peut être copié lors du clic gauche de la souris ensuite.

```
# Ne pas copier la sélection et annuler le mode copie à la fin de l'événement de glisser-déposer# Préférer le style de sélection iTerm : sélectionner, puis cliquer avec la souris pour copier dans le tamponunbind -T copy-mode-vi MouseDragEnd1Panebind -T copy-mode-vi MouseDown1Pane select-pane \;\  send-keys -X copy-pipe "pbcopy" \;\  send-keys -X clear-selection
```

Vérifions le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/AZl-e1MAfVIJRZjUjW37DGehkURLqVzBWPOj)
_Rester en mode copie et ne pas effacer la sélection à la fin de l'événement de glisser-déposer avec la souris_

Pour accéder aux éléments du tampon de copie et coller l'élément le plus récent, utilisez `C-p` et `p` :

```
bind p paste-bufferbind C-p choose-buffer
```

C'est tout pour aujourd'hui. Restez à l'écoute. Dans la prochaine partie de la série "tmux en pratique", nous parlerons de l'intégration du presse-papiers, et de la manière de partager le texte copié à l'intérieur de tmux avec le presse-papiers du système (localement et lors du travail à distance, sur OSX et Linux).

Au fait, vous pouvez voir toutes ces modifications de configuration en action, consultez simplement mon dépôt [tmux-config](https://github.com/samoshkin/tmux-config).

#### Astuce

Si vous souhaitez contourner complètement le mode copie de tmux et sélectionner du texte via iTerm, maintenez simplement la touche `<O`pt> enfoncée tout en faisant glisser votre souris.

### Ressources et liens

shell — Qu'est-ce que le défilement et le tampon de défilement exactement ? — Unix & Linux Stack Exchange — [https://unix.stackexchange.com/questions/145050/what-exactly-is-scrollback-and-scrollback-buffer](https://unix.stackexchange.com/questions/145050/what-exactly-is-scrollback-and-scrollback-buffer)

tmux scrollback avec iTerm2 • dan.carley.co — [https://dan.carley.co/blog/2013/01/11/tmux-scrollback-with-iterm2/](https://dan.carley.co/blog/2013/01/11/tmux-scrollback-with-iterm2/)

tmux copier le texte sélectionné avec la souris dans le presse-papiers automatiquement à la libération de la souris — Stack Overflow — [https://stackoverflow.com/questions/36815879/tmux-copy-mouse-selected-text-to-clipboard-automatically-on-mouse-release](https://stackoverflow.com/questions/36815879/tmux-copy-mouse-selected-text-to-clipboard-automatically-on-mouse-release)

raccourcis clavier — tmux — faire défiler vers le haut/bas avec shift + page up/down dans un panneau — Super User — [https://superuser.com/questions/702189/tmux-scroll-up-down-with-shift-page-up-down-into-a-pane](https://superuser.com/questions/702189/tmux-scroll-up-down-with-shift-page-up-down-into-a-pane)

[question/requête] mode copie sans sélection automatique d'un panneau ? • Problème #1021 • tmux/tmux — [https://github.com/tmux/tmux/issues/1021](https://github.com/tmux/tmux/issues/1021)

ssh — Laisser le défilement de tmux dans le terminal (iTerm2) — Stack Overflow — [https://stackoverflow.com/questions/12865559/leaving-tmux-scrollback-in-terminal-iterm2](https://stackoverflow.com/questions/12865559/leaving-tmux-scrollback-in-terminal-iterm2)

ligne de commande — Utiliser la barre de défilement du terminal avec tmux — Super User — [https://superuser.com/questions/310251/use-terminal-scrollbar-with-tmux](https://superuser.com/questions/310251/use-terminal-scrollbar-with-tmux)