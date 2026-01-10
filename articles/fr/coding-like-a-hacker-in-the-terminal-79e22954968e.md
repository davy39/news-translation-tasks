---
title: Comment coder comme un Hacker dans le terminal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-17T19:55:16.000Z'
originalURL: https://freecodecamp.org/news/coding-like-a-hacker-in-the-terminal-79e22954968e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V73Ai9Nc8NhSRrs8zOvcHA.png
tags:
- name: hacking
  slug: hacking
- name: General Programming
  slug: programming
- name: satire
  slug: satire
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment coder comme un Hacker dans le terminal
seo_desc: 'By Caleb Taylor

  You are a hacker. Your home is the terminal. You know every key stroke is valuable.
  If something is less than 100% efficient, you will spend hours figuring out the
  right tool to save yourself seconds. Because it’s always worth it.


  _S...'
---

Par Caleb Taylor

Vous êtes un hacker. Votre maison est le terminal. Vous savez que chaque frappe est précieuse. Si quelque chose est moins de 100% efficace, vous passerez des heures à trouver le bon outil pour vous économiser des secondes. Parce que cela en vaut toujours la peine.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GMvdjMQAjokYEFzTXjsp6Q.jpeg)
_Source : [Twitter](https://www.pablostanley.com/" rel="noopener" target="_blank" title="">Pablo Stanley</a> via <a href="https://twitter.com/pablostanley/status/963469081910296576" rel="noopener" target="_blank" title=")_

Votre recherche constante de nouvelles et meilleures façons de faire les choses vous détourne-t-elle de faire réellement les choses ? Certains pourraient dire oui, mais vous dites non. Aucun travail ne vaut la peine d'être fait à moins que vous ne puissiez donner une leçon à vos collègues sur pourquoi vous avez pu le faire si efficacement (temps d'installation non inclus).

Ce qui suit est une liste d'outils/fonctionnalités que tout bon hacker devrait connaître.

> **Avertissement** : Cet article est écrit avec une forte dose de satire. C'est une variation du mème ["Moi, un Intellectuel"](https://knowyourmeme.com/memes/me-an-intellectual). Bien que les suggestions soient sincères (et en aucun cas complètes), les références à être un "hacker" sont juste pour le fun.

### **Shell (zsh)**

> **Développeur moyen** : Un shell est un shell. Cela n'a pas vraiment d'importance lequel j'utilise. Ils sont tous nuls de toute façon.

> **Vous, un Hacker** : Le shell est le sang de mon travail. Ma passion pour l'efficacité et les fonctionnalités ne connaît pas de limites. Mon shell doit être digne d'un vrai hacker.

Vous vivez dans le terminal, et c'est pourquoi vous voulez utiliser un excellent shell. C'est pourquoi vous utilisez [zsh](http://www.zsh.org/).

Il vient avec une multitude de fonctionnalités :

* Correction automatique des commandes mal orthographiées
* Remplacement facile de bash
* Meilleure complétion `cd` en utilisant `<t`ab>
* Expansion de chemin : `cd /u/c/c/j` + `<t`ab`> =cd /user/caleb/code/`jarvis
* [Beaucoup plus](http://zsh.sourceforge.net/Doc/Release/zsh_toc.html)

Il vient également avec un excellent framework pour gérer votre configuration zsh : [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh). Il inclut 200+ plugins et 140+ thèmes pour ajouter toutes sortes de fonctionnalités géniales à votre terminal. Un petit échantillon :

* [git](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git) - des tonnes d'alias et de fonctions utiles pour git
* t[mux](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/tmux/tmux.plugin.zsh) - alias et paramètres pour intégrer zsh avec tmux
* [node](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/node) - ajoute la commande `node-docs` pour ouvrir la documentation du site web
* [osx](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/osx) - plusieurs utilitaires pour travailler avec OSX
* [web-search](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/web-search) - initialiser des recherches web à partir de la ligne de commande
* [auto-suggestions](https://github.com/zsh-users/zsh-autosuggestions) - suggestions rapides et non intrusives basées sur l'historique

Vous pouvez trouver la liste complète des plugins [ici](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins).

### Gestion de session ([tmux](https://github.com/tmux/tmux))

> **Développeur moyen** : D'accord, j'ai mes fichiers ouverts pour lame_project_1. Mais je dois aussi travailler sur boring_project_2. Je dois également me connecter à un serveur et regarder les logs. Je suppose que je vais juste créer un gros désordre dans mon terminal avec des fichiers/onglets de plusieurs projets ouverts d'une manière que je finirai par perdre le contrôle et être forcé de fermer et de recommencer.

> **Vous, un Hacker** : Je travaille sur plusieurs projets à la fois, donc j'ai besoin d'un outil pour m'aider à rester organisé. Il devrait fonctionner sur plusieurs plateformes et me permettre de créer des espaces de travail organisés et d'avoir beaucoup d'autres fonctionnalités qui aident à la productivité.

Vous savez que le développement peut devenir désordonné. Parfois, vous devez travailler sur plusieurs projets à la fois. C'est pourquoi vous utilisez [tmux](https://github.com/tmux/tmux).

Il vous permet de créer des sessions. Chaque session peut être personnalisée selon la disposition exacte dont vous avez besoin. Vous pouvez nommer les sessions pour un changement facile, et même sauvegarder et restaurer les sessions si votre terminal est fermé. De plus, il a sa propre ligne d'état personnalisable qui vous permettra d'afficher des choses comme l'heure, la date, l'utilisation du CPU, et plus encore. Et si vous ne connaissez pas votre utilisation du CPU à tout moment, êtes-vous même un hacker ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*1aaEQExjdaueLgsLWxfr1g.gif)
_Organisez votre terminal avec des sessions et utilisez fzf pour la création/recherche/suppression floue de sessions_

Il a même un [gestionnaire de plugins](https://github.com/tmux-plugins/tpm) et une [multitude de plugins et fonctionnalités géniaux](https://github.com/rothgar/awesome-tmux) qui porteront votre hacking au niveau supérieur.

**Astuce Super-Pro Hacker** :
Utilisez tmux avec fzf via quelques [scripts géniaux](https://github.com/junegunn/fzf/wiki/examples#tmux) pour créer/supprimer/naviguer rapidement et pousser votre niveau de hacker à plus de 9000.

### Recherche (ripgrep)

> **Développeur moyen** : Où ai-je défini cette constante ? Je sais qu'elle est quelque part ici. Je vais essayer de grep. Quels sont les arguments déjà ? Laissez-moi googler cela. Oh zut, maintenant il cherche dans mon dossier node_modules. C'est le pire.

> **Vous, un Hacker** : Lorsque je recherche quelque chose, cela doit être ultra-rapide. De plus, cela doit utiliser des paramètres par défaut sensés, comme ignorer les binaires ou les fichiers cachés.

Vous savez que la recherche dans votre projet est une tâche courante. Elle doit être rapide et ne pas perdre votre temps. Cela signifie des choses comme ignorer tout ce que votre fichier `.gitignore` ignore, et sauter les binaires et les fichiers cachés. C'est pourquoi vous utilisez [ripgrep](https://github.com/BurntSushi/ripgrep). C'est comme grep sur stéroïdes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5Nt_6zoCkF0THdmdNtGoQw.gif)
_ripgrep en action_

En [mots de son créateur](https://blog.burntsushi.net/ripgrep/) : _"Utilisez ripgrep si vous aimez la vitesse, le filtrage par défaut, moins de bugs et le support Unicode."_

### Recherche floue ([fzf](https://github.com/junegunn/fzf))

> **Développeur moyen** : Il est sûr que c'est difficile de se souvenir de l'emplacement exact de tant de fichiers dans mon projet. Je suppose que je vais errer jusqu'à ce que je trouve le bon.

> **Vous, un Hacker** : Je devrais pouvoir trouver des fichiers de manière floue. Je peux taper le nom du fichier, ou une partie du chemin, ou tout cela, et trouver rapidement le fichier que je cherche.

Vous savez que vous ne devriez pas avoir à taper plus que nécessaire. Vous utilisez donc [fzf](https://github.com/junegunn/fzf), un outil de recherche floue polyvalent en ligne de commande. Il peut également faire bien plus que trouver des fichiers de manière floue. Il peut être utilisé avec n'importe quelle liste : "fichiers, historique de commandes, processus, noms d'hôtes, signets, commits git, etc".

**Astuce Super-Pro Hacker** : Vous savez que les alias sont un excellent moyen de créer des raccourcis pour tirer parti des fonctionnalités de fzf. Par exemple, si vous voulez trouver un fichier de manière floue, puis ouvrir la sélection dans votre éditeur par défaut, vous pouvez ajouter ceci à votre configuration `zsh` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*c4DFt6p5PDhOxHTx2p_lag.gif)
_Maintenant vous pouvez exécuter "fo" pour trouver de manière floue et ouvrir un fichier_

De nombreux autres exemples peuvent être trouvés sur le [wiki fzf](https://github.com/junegunn/fzf/wiki/examples).

### Invite de terminal ([Spaceship](https://github.com/denysdovhan/spaceship-prompt))

> **Développeur moyen** : Qui se soucie de l'apparence de mon invite de terminal ? Il n'y a aucun moyen qu'elle puisse me donner des informations utiles. Je vais juste la laisser par défaut.

> **Vous, un Hacker** : Je veux que mon invite soit incroyable. Elle doit être contextuelle. Elle doit me donner des informations utiles et être configurable. De plus, ce serait génial si elle était liée à l'espace.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vtc9ZCR2p7a_9-6MuFB-hw.gif)
_Bienvenue dans le futur... mais en réalité le présent. Hackers/astronautes seulement._

Vous savez qu'une invite doit être simple, propre et fournir uniquement des informations pertinentes. Elle doit également souffler l'esprit des gens lorsqu'ils voient sa beauté. C'est pourquoi vous utilisez [spaceship-prompt](https://github.com/denysdovhan/spaceship-prompt). Il fournit une intégration git/mercurial, un indicateur de niveau de batterie, un nom d'hôte et des données utilisateur intelligents, des numéros de version pour une variété de bibliothèques, des icônes magnifiques, et bien plus encore.

### Changer de répertoires ([z](https://github.com/rupa/z))

> **Développeur moyen** : Je dois changer mon répertoire pour mon projet "hacker", qui est dans mon dossier cool, qui est dans mon dossier personnel, qui est dans mon dossier code, qui est dans mon répertoire home.

```
cd ~/code/personal/cool/hacker
```

> **Vous, un Hacker** : Je dois changer mon répertoire pour mon projet "hacker".

```
z hacker
```

Taper des chemins de fichiers complets est ce que font les développeurs moyens. Vous êtes un hacker. Vous comptez sur [z](https://github.com/rupa/z). Une fois installé, il commencera à apprendre quels répertoires vous visitez. Ensuite, vous pouvez lui donner une regex (ou un simple nom de dossier) pour sauter vers le candidat le plus probable.

### Outils bonus pour Hackers

Les outils suivants sont des moyens supplémentaires pour vraiment élever votre jeu de hacking.

1. [wttr.in](https://github.com/chubin/wttr.in) — Il n'y a qu'une seule bonne façon de vérifier la météo.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eoCAnuHdh9I69SiGJU_aOg.png)

2. Star Wars — Les gens cool aiment Star Wars. Les hackers le regardent dans le terminal.

```
telnet towel.blinkenlights.nl
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*VHd1lA9C36pYxi_a5-afYQ.gif)
_Astuce Pro : Regardez Star Wars dans un autre volet tmux tout en travaillant. Personne ne vous posera de questions._

3. [haxor-news](https://github.com/donnemartin/haxor-news) — Êtes-vous même un hacker si vous ne lisez pas [Hacker News](https://news.ycombinator.com/) ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*lcF0nWWF74IZCcc8I-ULBQ.gif)

4. Spotify — En utilisant [shpotify](https://github.com/hnarayanan/shpotify), vous pouvez jouer de la musique à partir du terminal (OSX uniquement... Hé, arrêtez de huer ! Posez cette chaise ! Qui a lancé cette tomate !?), ou [mopidy](https://www.mopidy.com/) pour quelque chose de multiplateforme.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ued2Pipg7m16DOKuwpAUdw.gif)
_Dieu bénisse les commandes dans le terminal_

Cela conclut à peu près tout. Ce n'est en aucun cas une liste exhaustive. Avez-vous d'autres outils de hacker incroyables ? Laissez un commentaire et faites-le moi savoir.

Si vous êtes intéressé à voir plus de ces outils en action, consultez mes [dotfiles](https://github.com/ctaylo21/jarvis) que j'utilise pour le développement. En bonus, voici une capture d'écran du glorieux terminal en action :

![Image](https://cdn-media-1.freecodecamp.org/images/1*V73Ai9Nc8NhSRrs8zOvcHA.png)