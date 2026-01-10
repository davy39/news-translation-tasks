---
title: 'tmux en pratique : intégration avec le presse-papiers système'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-27T11:13:55.000Z'
originalURL: https://freecodecamp.org/news/tmux-in-practice-integration-with-system-clipboard-bcd72c62ff7b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gGNWXlll62GCAM55hbldbw.png
tags:
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'tmux en pratique : intégration avec le presse-papiers système'
seo_desc: 'By Alexey Samoshkin

  How to build a bridge between tmux copy buffer and system clipboard, and to store
  selected text on OSX or Linux system clipboard, in a way that address both local
  and remote usage scenarios

  This is the 4th part of my tmux in pract...'
---

Par Alexey Samoshkin

#### Comment construire un pont entre le tampon de copie de tmux et le presse-papiers système, et stocker le texte sélectionné sur le presse-papiers du système OSX ou Linux, de manière à répondre aux scénarios d'utilisation locale et distante

Il s'agit de la 4ème partie de ma série d'articles [tmux en pratique](https://medium.com/@alexeysamoshkin/tmux-in-practice-series-of-posts-ae34f16cfab0).

![Image](https://cdn-media-1.freecodecamp.org/images/hLvVwjePtz6ORxA6S5mKvdVTsoysRvgDtLA7)
_Vous pouvez copier du texte depuis une session locale ou distante, ou même une session distante imbriquée vers votre presse-papiers système_

Dans la [partie précédente de la série « tmux en pratique »](https://medium.com/@alexeysamoshkin/tmux-in-practice-scrollback-buffer-47d5ffa71c93), nous avons parlé de choses comme le tampon de défilement, le mode copie, et nous avons légèrement abordé le sujet de la copie de texte dans le tampon de copie de tmux.

Tôt ou tard, vous réaliserez que tout ce que vous copiez dans tmux est stocké uniquement dans le tampon de copie de tmux, mais n'est pas partagé avec le presse-papiers système. Les opérations de copie et de collage sont si courantes que cette limitation suffit à transformer tmux en un simple pavé inutile, malgré ses autres avantages.

Dans cet article, nous explorerons comment construire un pont entre le tampon de copie de tmux et le presse-papiers système, pour stocker le texte copié dans le presse-papiers système, de manière à répondre aux scénarios d'utilisation locale et distante.

**Nous discuterons des techniques suivantes :**

1. OSX uniquement, partager du texte avec le presse-papiers en utilisant « pbcopy »
2. OSX uniquement, utiliser le wrapper « reattach-to-user-namespace » pour faire fonctionner pbcopy correctement dans l'environnement tmux
3. Linux uniquement, partager du texte avec la sélection X en utilisant les commandes `xclip` ou `xsel`

Les techniques ci-dessus ne traitent que les scénarios locaux. 
**Pour supporter les scénarios distants, il existe 2 méthodes supplémentaires :**

1. Utiliser la séquence d'échappement [ANSI OSC 52](https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences) pour communiquer avec le terminal parent afin de gérer et stocker du texte dans le presse-papiers d'une machine locale.
2. Configurer un écouteur réseau local qui transmet l'entrée à `pbcopy` ou `xclip` ou `xsel`. Transmettre le texte sélectionné copié depuis la machine distante vers un écouteur sur la machine locale via un tunnel SSH distant. Cela est plutôt complexe, et je consacrerai un article dédié pour le décrire.

### OSX. Commandes pbcopy et pbpaste

Les commandes `pbcopy` et `pbpaste` vous permettent d'interagir et de manipuler le presse-papiers système depuis la ligne de commande.

`pbcopy` lit les données depuis `stdin` et les stocke dans le presse-papiers. `pbpaste` fait l'inverse et place le texte copié sur `stdout`.

L'idée est de s'intégrer à diverses commandes tmux, qui gèrent la copie de texte en mode copie.

Listons-les :

```
$ tmux -f /dev/null list-keys -T copy-mode-vi
```

```
bind-key -T copy-mode-vi Enter send-keys -X copy-selection-and-cancelbind-key -T copy-mode-vi C-j send-keys -X copy-selection-and-cancelbind-key -T copy-mode-vi D send-keys -X copy-end-of-linebind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-selection-and-cancelbind-key -T copy-mode-vi A send-keys -X append-selection-and-cancel
```

`copy-selection-and-cancel` et `copy-end-of-line` sont des commandes spéciales de tmux que tmux comprend lorsque le panneau est en mode copie. Il existe deux variantes de la commande de copie : `copy-selection` et `copy-pipe`.

Réécrivons la liaison de la touche `Enter` avec la commande copy-pipe :

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "pbcopy"
```

La commande `copy-pipe` stocke le texte sélectionné dans le tampon tmux de la même manière que `copy-selection`, et transmet également le texte sélectionné à la commande donnée `pbcopy`. Ainsi, le texte est stocké à deux endroits : le tampon de copie de tmux et le presse-papiers système.

### OSX. Wrapper reattach-to-user-namespace

Jusqu'à présent, tout va bien. Cependant, sur certaines versions d'OSX, `pbcopy` et `pbpaste` ne fonctionnent pas correctement lorsqu'ils sont exécutés sous tmux.

Lisez [plus de détails](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard#interaction-with-tmux) de Chris Johnsen sur les raisons pour lesquelles cela se produit :

> tmux utilise la fonction de bibliothèque daemon(3) lors du démarrage de son processus serveur. Dans Mac OS X 10.5, Apple a modifié daemon(3) pour déplacer le processus résultant de son espace de noms de démarrage d'origine vers l'espace de noms de démarrage racine. Cela signifie que le serveur tmux, et ses enfants, perdront automatiquement et de manière incontrôlable l'accès à ce qui aurait été leur espace de noms de démarrage d'origine (c'est-à-dire celui qui a accès au service de presse-papiers).

Une solution courante consiste à utiliser le wrapper [reattach-to-user-namespace](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard). Cela nous permet de lancer un processus et d'avoir ce processus attaché à l'espace de noms de démarrage par utilisateur, ce qui fait que le programme se comporte comme nous nous y attendons. Vous devez modifier correctement la liaison de la touche :

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "reattach-to-user-namespace pbcopy"
```

De plus, vous devrez dire à tmux d'exécuter votre shell (bash, zsh, ...) à l'intérieur d'un wrapper, en définissant l'option `default-command` :

```
if -b "command -v reattach-to-user-namespace > /dev/null 2>&1" \    "run 'tmux set -g default-command \"exec $(tmux show -gv default-shell) 2>/dev/null & reattach-to-user-namespace -l $(tmux show -gv default-shell)\"'"
```

**Note** : certaines versions d'OSX fonctionnent bien même sans ce hack (OSX 10.11.5 El Capitan), tandis que les utilisateurs d'OSX Sierra [signalent que ce hack est toujours nécessaire](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard/issues/56).

### Linux. Interagir avec la sélection X via xclip et xsel

Nous pouvons utiliser les commandes `xclip` ou `xsel` sur Linux pour stocker du texte dans le presse-papiers, comme `pbcopy` sur OSX. Sur Linux, il existe [plusieurs types de sélections de presse-papiers](https://wiki.archlinux.org/index.php/Clipboard) maintenus par le serveur X : primaire, secondaire et presse-papiers. Nous ne nous intéressons qu'au primaire et au presse-papiers. Le secondaire était destiné à être une alternative au primaire.

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "xclip -i -f -selection primary | xclip -i -selection clipboard"
```

Ou lorsque vous utilisez `xsel` :

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "xsel -i --clipboard"
```

[Lisez ici](https://askubuntu.com/questions/705620/xclip-vs-xsel) pour une comparaison de `xclip` vs. `xsel`, si vous êtes curieux. Consultez également [cet article sur l'utilisation et les exemples de `xclip`](https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/). Et n'oubliez pas d'installer l'une de ces utilités, car elles peuvent ne pas faire partie de votre distribution.

### Utilisation de la séquence d'échappement ANSI OSC 52 pour amener le terminal à stocker du texte dans le presse-papiers

Jusqu'à présent, nous n'avons couvert que les scénarios locaux. Lorsque vous vous connectez en SSH à une machine distante et que vous démarrez des sessions tmux, vous ne pouvez pas utiliser `pbcopy`, `xclip` ou `xsel`, car le texte sera stocké dans le presse-papiers de la machine distante, et non dans le vôtre. Vous avez besoin d'un moyen de transporter le texte copié vers le presse-papiers de votre machine locale.

La [séquence d'échappement ANSI](https://en.wikipedia.org/wiki/ANSI_escape_code) est une séquence d'octets envoyée au terminal qui sont entrelacés avec des caractères imprimables réguliers, et sont utilisés pour contrôler divers aspects du terminal : tels que les couleurs de texte, la position du curseur, les effets de texte, l'effacement de l'écran. Le terminal est capable de détecter une telle séquence de contrôle d'octets qui le fait déclencher des actions spécifiques et ne pas imprimer ces caractères à la sortie.

La séquence d'échappement ANSI peut être détectée car elle commence par le caractère ASCII `ESC` (0x1b hex, 027 décimal, \033 en octal). Par exemple, lorsque le terminal voit la séquence `\033[2A`, il déplacera la position du curseur de 2 lignes vers le haut.

Il existe [vraiment](http://ascii-table.com/ansi-escape-sequences.php) [beaucoup](https://www.xfree86.org/4.8.0/ctlseqs.html) de ces séquences connues. Certaines d'entre elles sont les mêmes pour différents types de terminaux, tandis que d'autres peuvent varier et être très spécifiques à votre émulateur de terminal. Utilisez la commande `infocmp` pour interroger la base de données `terminfo` pour les séquences d'échappement prises en charge par différents types de terminaux.

D'accord, mais comment cela peut-il nous aider concernant le presse-papiers ? Il s'avère qu'il existe une catégorie spéciale de séquences d'échappement : les « Operating System Controls » (OSC) et la séquence d'échappement « OSC 52 », qui permet aux applications d'interagir avec le presse-papiers.

Si vous utilisez iTerm, essayez d'exécuter la commande suivante, puis « `V` » pour voir le contenu du presse-papiers système. Assurez-vous d'activer la gestion de la séquence d'échappement OSC 52 : « Préférences -> Général -> Les applications dans le terminal peuvent accéder au presse-papiers ».

```
printf "\033]52;c;$(printf "%s" "blabla" | base64)\a"
```

La conclusion est que nous pouvons stocker du texte dans le presse-papiers système en envoyant une séquence d'échappement ANSI spécialement conçue à notre terminal.

Écrivons le script shell `yank.sh` :

```
#!/bin/bash
```

```
set -eu
```

```
# obtenir les données soit depuis stdin soit depuis un fichierbuf=$(cat "$@")
```

```
# Obtenir la longueur du tamponbuflen=$( printf %s "$buf" | wc -c )
```

```
maxlen=74994
```

```
# avertir si la longueur dépasse maxlenif [ "$buflen" -gt "$maxlen" ]; then   printf "input is %d bytes too long" "$(( buflen - maxlen ))" >&2fi
```

```
# construire la séquence d'échappement ANSI OSC 52esc="\033]52;c;$( printf %s "$buf" | head -c $maxlen | base64 | tr -d '\r\n' )\a"
```

Ainsi, nous lisons le texte à copier depuis `stdin`, puis vérifions si sa longueur dépasse la longueur maximale de 74994 octets. Si c'est le cas, nous le tronquons, et enfin convertissons les données en base64 et les enveloppons dans la séquence d'échappement OSC 52 : `\033]53;c;${data_in_base64}\a`

Ensuite, connectons-le à nos liaisons de touches tmux. C'est assez simple : il suffit de transmettre le texte sélectionné à notre script `yank.sh`, tout comme nous le transmettons à `pbcopy` ou `xclip`.

```
yank="~/.tmux/yank.sh"
```

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "$yank"
```

Cependant, il reste une pièce à ajouter pour compléter le puzzle. Où devons-nous envoyer la séquence d'échappement ? Apparemment, l'envoyer simplement à `stdout` ne fonctionnera pas. La cible devrait être notre émulateur de terminal parent, mais nous ne connaissons pas le bon `tty`. Nous allons donc l'envoyer au `tty` du panneau actif de tmux, et dire à tmux de le retransmettre à l'émulateur de terminal parent :

```
# construire la séquence d'échappement ANSI OSC 52esc="\033]52;c;$( printf %s "$buf" | head -c $maxlen | base64 | tr -d '\r\n' )\a"esc="\033Ptmux;\033$esc\033\\"
```

```
pane_active_tty=$(tmux list-panes -F "#{pane_active} #{pane_tty}" | awk '$1=="1" { print $2 }')
```

```
printf "$esc" > "$pane_active_tty"
```

Nous utilisons la commande `tmux list-panes` pour interroger le panneau actif et son `tty`. Nous plaçons également notre séquence OSC 52 dans une séquence d'enveloppe supplémentaire (Device Control String, ESC P), de sorte que tmux déballage cette enveloppe et transmet OSC 52 au terminal parent.

Dans les versions plus récentes de tmux, vous pouvez dire à tmux de gérer les interactions avec le presse-papiers pour vous. Voir l'option `set-clipboard` de tmux. `on` — tmux créera un tampon interne et tentera de définir le presse-papiers du terminal en utilisant OSC 52. `external` — ne pas créer de tampon, mais tenter de définir le presse-papiers du terminal.

Assurez-vous simplement qu'il est soit `external` soit `on` :

```
set -g set-clipboard on
```

Alors, si tmux est déjà capable de cette fonctionnalité, pourquoi devons-nous nous soucier de la configuration manuelle de l'OSC 52 ? C'est parce que `set-clipboard` ne fonctionne pas lorsque vous avez une session tmux distante imbriquée dans une session locale. Et il ne fonctionne que dans ces [terminaux qui supportent la gestion de la séquence d'échappement OSC 52](https://askubuntu.com/questions/621522/use-tmux-set-clipboard-in-gnome-terminal-xterms-disallowedwindowops/621646).

L'astuce pour les sessions distantes imbriquées est de contourner la session distante et d'envoyer notre séquence d'échappement OSC 52 directement à la session locale, afin qu'elle atteigne notre émulateur de terminal local (iTerm).

Utilisez `$SSH_TTY` à cette fin :

```
# résoudre le terminal cible pour envoyer la séquence d'échappement# si nous sommes sur une machine distante, envoyer directement à SSH_TTY pour transporter la séquence d'échappement# vers le terminal sur la machine locale, afin que les données arrivent dans le presse-papiers de notre machine localepane_active_tty=$(tmux list-panes -F "#{pane_active} #{pane_tty}" | awk '$1=="1" { print $2 }')target_tty="${SSH_TTY:-$pane_active_tty}"
```

```
printf "$esc" > "$target_tty"
```

C'est tout. Maintenant, nous avons une solution complètement fonctionnelle, qu'il s'agisse d'une session locale, distante ou des deux, imbriquées l'une dans l'autre. [Crédits à ce excellent article](https://sunaku.github.io/tmux-yank-osc52.html), où j'ai lu pour la première fois cette approche.

Le principal inconvénient de l'utilisation des séquences d'échappement OSC est que, malgré leur déclaration dans la spécification, seuls quelques terminaux les supportent en pratique : iTerm et xterm le font, tandis que le Terminal OSX, Terminator et le terminal Gnome ne le font pas. Ainsi, une solution par ailleurs excellente (surtout dans les scénarios distants, lorsque vous ne pouvez pas simplement `pipe` vers `xclip` ou `pbcopy`) manque d'un support plus large des terminaux.

Vous pourriez vouloir [consulter la version complète](https://github.com/samoshkin/tmux-config/blob/af2efd9561f41f30c51c9deeeab9451308c4086b/tmux/yank.sh) du script `yank.sh`.

Il existe une autre solution pour supporter les scénarios distants, qui est plutôt folle, et je la décrirai dans un autre [article dédié](https://medium.com/@alexeysamoshkin/tmux-in-practice-copy-text-from-remote-session-using-ssh-remote-tunnel-and-systemd-service-dd3c51bca1fa). L'idée est de configurer un écouteur réseau local qui transmet l'entrée à `pbcopy` ou `xclip` ou `xsel` ; et de transmettre le texte sélectionné copié depuis une machine distante vers un écouteur sur la machine locale via un tunnel SSH distant. Restez à l'écoute.

### Ressources et liens

ANSI escape code — Wikipedia — [https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences](https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences)

What are OSC terminal control sequences / escape codes? | ivucica blog — [https://blog.vucica.net/2017/07/what-are-osc-terminal-control-sequences-escape-codes.html](https://blog.vucica.net/2017/07/what-are-osc-terminal-control-sequences-escape-codes.html)

Copying to clipboard from tmux and Vim using OSC 52 — The Terminal Programmer — [https://sunaku.github.io/tmux-yank-osc52.html](https://sunaku.github.io/tmux-yank-osc52.html)

Copy Shell Prompt Output To Linux / UNIX X Clipboard Directly — nixCraft — [https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/](https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/)

software recommendation — 'xclip' vs. 'xsel' — Ask Ubuntu — [https://askubuntu.com/questions/705620/xclip-vs-xsel](https://askubuntu.com/questions/705620/xclip-vs-xsel)

Everything you need to know about Tmux copy paste · rushiagr — [http://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting/](http://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting/)

macos — Synchronize pasteboard between remote tmux session and local Mac OS pasteboard — Super User — [https://superuser.com/questions/407888/synchronize-pasteboard-between-remote-tmux-session-and-local-mac-os-pasteboard/408374#408374](https://superuser.com/questions/407888/synchronize-pasteboard-between-remote-tmux-session-and-local-mac-os-pasteboard/408374#408374)

linux — Getting Items on the Local Clipboard from a Remote SSH Session — Stack Overflow — [https://stackoverflow.com/questions/1152362/getting-items-on-the-local-clipboard-from-a-remote-ssh-session](https://stackoverflow.com/questions/1152362/getting-items-on-the-local-clipboard-from-a-remote-ssh-session)

Use tmux set-clipboard in gnome-terminal (XTerm's disallowedWindowOps) — Ask Ubuntu — [https://askubuntu.com/questions/621522/use-tmux-set-clipboard-in-gnome-terminal-xterms-disallowedwindowops/621646](https://askubuntu.com/questions/621522/use-tmux-set-clipboard-in-gnome-terminal-xterms-disallowedwindowops/621646)