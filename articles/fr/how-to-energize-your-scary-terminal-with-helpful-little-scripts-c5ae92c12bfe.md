---
title: Comment dynamiser votre terminal effrayant avec des petits scripts utiles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-05T11:58:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-energize-your-scary-terminal-with-helpful-little-scripts-c5ae92c12bfe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ip_q_6I-kNpUjuPMOutuTA.jpeg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment dynamiser votre terminal effrayant avec des petits scripts utiles
seo_desc: 'By Vijayabharathi Balasubramanian

  I’m going to talk about three valuable tools that will finally help conquer your
  fear of terminals: Git Aliases, Bash Aliases, and One click snippets.

  A combination of aliases and bash scripts can make you very produ...'
---

Par Vijayabharathi Balasubramanian

Je vais parler de trois outils précieux qui vous aideront enfin à vaincre votre peur des terminaux : les alias Git, les alias Bash et les extraits en un clic.

Une combinaison d'alias et de scripts bash peut vous rendre très productif dans votre flux de travail de développement. Utilisez-les suffisamment longtemps et vous oublierez même les commandes originales sous les alias. Ce qui n'est pas réellement une mauvaise chose — jusqu'à ce que vous obteniez un nouvel ordinateur portable flambant neuf et que vous n'ayez aucune idée de l'endroit où vous avez placé vos alias dans l'ancien :)

Vous avez peut-être utilisé des alias Git. Vous pourriez trouver les alias bash nouveaux. **Mais, ne manquez pas** le `gif` montrant les icônes en un clic au travail vers la fin. Ces icônes de bureau en un clic sont ma ligne de défense. Elles m'aident à plonger directement dans le codage/l'écriture avant que la liste inoffensive des "**plus visités**" sur le nouvel onglet du navigateur ne puisse me faire dévier de ma route.

Au fait, j'utilise Firefox nightly et il est facile de configurer une ardoise propre comme votre nouvel onglet. Très bien, passons aux choses sérieuses.

### 1 : Alias Git

Si le terminal est le donjon pour les personnes nouvelles dans le domaine de la technologie, Git tend à être le passage le plus sombre, intimidant avec de longues séquences de commandes.

**Mais, Git est magnifique.** Essayez ce [jeu](https://try.github.io/).

Faire en sorte que `git` soit plus facile à utiliser consiste à configurer vos propres alias. C'est-à-dire, une fois que vous comprenez les commandes sous-jacentes. Ce n'est pas pour vous donner **tous** les alias utiles. Au lieu de cela, je vais vous montrer les possibilités afin que vous puissiez **construire votre propre liste d'alias.**

#### En solo

Supposons que vous travaillez seul. Vous mettez en scène et validez toute la journée, peut-être votre code ou vos écrits pour le blog. Vous trouverez un ensemble d'alias très utiles.

```
git config --global alias.s statusgit config --global alias.aa 'add --all'git config --global alias.cm 'commit -am'git config --global alias.up 'push'
```

Assurez-vous d'avoir un fichier `.gitignore` bien défini pour éviter de suivre des fichiers inutiles tels que `node_modules`. Cela vous aidera lorsque vous utiliserez `git aa` pour mettre en scène tous les fichiers.

Tous ces alias sont stockés dans un fichier de configuration sous le répertoire personnel. Jetez un coup d'œil à `~/.gitconfig`. Vous pouvez même éditer directement le fichier de configuration — assurez-vous simplement de ne pas le désorganiser.

#### Collaboration de code

Lorsque vous collaborez avec une équipe, une toute autre liste de commandes peut être utile. Souvenez-vous, rebase réécrit l'historique. Il est [conseillé uniquement pour les branches locales](https://coderwall.com/p/7aymfa/please-oh-please-use-git-pull-rebase), pour nettoyer votre code au-dessus de la branche distante.

```
git config --global alias.pr 'pull --rebase upstream master'
```

En voici un de [Harry](https://csswizardry.com/2017/05/little-things-i-like-to-do-with-git/) sur l'alias de `blame` en `praise` et d'autres pépites que vous pourriez trouver utiles.

#### Alias avancés

```
git config --global alias.ls 'log --pretty=format:"%C(yellow)%h %C(green)%s %Creset(%ad)" --date=relative'
```

`%C(yellow)` marque le jeton suivant le code de couleur en jaune. Dans notre cas ci-dessus, `%h` représente le hash de validation, qui sera peint en jaune sur notre terminal. %Creset, sans crochets, vous ramène à la couleur de police par défaut du terminal. `--date=relative` vous indique `il y a des jours/semaines` au lieu d'une date réelle.

Tous ces mots peuvent essayer de vous expliquer à quoi cela ressemble, mais voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/xSc0RQ1OUSbkrbmbpDk3zJreEWA2Sn96GH8X)
_Journal git codé par couleur_

#### Références

Vous pouvez en apprendre plus sur la décoration sur [git-scm.com](https://git-scm.com/docs/pretty-formats). Il y a tout un ensemble d'informations que vous pouvez extraire telles que `%h`, `%n` et ainsi de suite. Au fait, **c'est un livre gratuit entier sur Git**. Commencez à la page 1.

J'ai appris beaucoup de trucs utiles de Nicola il y a un moment lors de son discours au sommet Atlassian 2014. Je n'ai pas pu trouver la vidéo, mais j'ai trouvé [sa diapositive](https://www.slideshare.net/GoAtlassian/becoming-a-git-master-nicola-paolucci). Ne manquez pas cette fonction anonyme dans les alias.

Voici une liste de ses alias G[it](http://bit.do/git-aliases). Mais, selon ses propres mots, ne copiez pas simplement les alias. Construisez-les au fur et à mesure, en ajoutant uniquement les alias qui vous sont utiles. Sinon, ce sera comme passer des heures à curer des articles/livres que nous ne lirons jamais.

### 2 : Alias Bash

`Git` n'est pas la seule `interface de ligne de commande` (CLI) qui demande un peu de frappe sur le terminal. Pensez à `bundle exec rails db:migrate` sur un terminal ou `docker-compose exec npm run script` que vous exécutez sur un conteneur. Que diriez-vous de quelque chose de plus court ?

Si vous utilisez des commandes plus longues, sur une base quotidienne, envisagez de configurer des alias bash.

La syntaxe est très simple.

```
alias new_cmd='never-ending-command; and another command'
```

**Vous ajoutez cela à la fin du fichier `.bashrc` dans votre dossier personnel.** Normalement `~/.bashrc` est l'endroit où il se trouve. Le dernier que j'ai configuré est pour les commandes docker. Cela devrait servir d'exemple.

```
alias dc='docker-compose'alias de='docker-compose exec' alias up='cd ~/Projects/docker_project/; dc up'
```

Je devais me déconnecter et me reconnecter pour que cela fonctionne sur les terminaux. Cependant, cette commande cool de S[tackoverflow](https://stackoverflow.com/questions/2518127/how-do-i-reload-bashrc-without-logging-out-and-back-in) m'a sauvé. Exécutez cela sur votre terminal et commencez à utiliser de nouveaux alias immédiatement : `source ~/.bashrc`

Pensez-vous à ce que je pense ? Oublier les alias Git ? Comment nommer l'alias bash pour `git pull --rebase upstream master` ? Que diriez-vous de `gprum` ?

Laissez-vous aller ! Soyez prudent **à ne pas réutiliser les commandes existantes.** Par exemple, `df` montre l'espace disque libre dans Linux, donc je n'utiliserais pas cela comme alias pour autre chose.

### 3 : Extraits en un clic

Mes préférés. Un clic, sur votre icône de bureau personnalisée, avec votre propre logo, et vous aurez tout cela prêt à rouler :

* Ouvre votre dossier de projet dans VS Code/atom
* Un terminal exécutant le serveur de développement sur un onglet
* Un autre onglet exécutant des tests / rechargement à chaud
* Le dernier onglet qui s'ouvre avec l'état Git
* Le dernier onglet reste ouvert pour que vous puissiez `git` les choses faites.
* Si votre serveur de développement n'ouvre pas le navigateur, vous pouvez l'ouvrir ici

Il y a quelque chose de magique lorsque vous pouvez simplement taper sur une icône et que tout l'environnement se lance pour vous. Un clic et vous obtenez votre éditeur de texte, votre serveur web et vos tests déjà en cours d'exécution.

Le fichier bash `get-to-work.sh` ressemble à ceci. Au fait, cela est sur Linux.

```
#!/bin/bashexport WD="~/development"code $WD gnome-terminal \ --tab --working-directory=$WD \ -e 'bash -c "export BASH_POST_RC=\"npm start\"; exec bash"' \ --tab --working-directory=$WD \ -e 'bash -c "export BASH_POST_RC=\"npm run watch\"; exec bash"' \ --tab --working-directory=$WD \ -e 'bash -c "export BASH_POST_RC=\"git status\"; exec bash"'
```

Nous avons un répertoire de travail configuré sous la variable `WD`. Ensuite, commence une très longue ligne qui se plie sur 7 lignes sur une largeur de terminal de 80 caractères. Ne laissez pas cela vous effrayer. Si vous regardez de près, nous ouvrons gnome-terminal avec trois onglets et exécutons trois commandes différentes sur eux.

Exécutez cette commande pour marquer le script bash comme exécutable.

```
chmod +x get-to-work.sh
```

Vous pouvez déjà vérifier si le script fonctionne. `cd` dans le dossier où vous avez le script shell et tapez ceci sur votre terminal.

```
./get-to-work.sh
```

Ajoutons une belle icône de bureau à notre script. `Exec` et `Icon` sont importants. Ils doivent être dans un fichier `.desktop`. J'ai nommé le mien `get-to-work.desktop`.

Au fait, cela est pour Linux. La plupart des bureaux utilisent la spécification [freedesktop](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html). En lisant entre les lignes, j'ai peut-être enfreint quelques directives (comme ne pas supprimer de champs même s'ils ne sont pas applicables).

```
[Desktop Entry] Name=Get To Work Comment=Commencez à coder en un instant. GenericName=Environnement de développement Exec=/home/username/snippets/get-to-work.sh Icon=/usr/share/icons/logo.png Type=Application Terminal=true StartupNotify=true Categories=Utility;
```

N'oubliez pas d'utiliser le bon chemin au lieu de `/home/username/...`. Assurez-vous de placer l'`Icon` dans un dossier accessible où vous avez la permission de lire le fichier.

Validez et installez le fichier `.desktop`.

```
desktop-file-validate get-to-work.desktop desktop-file-install get-to-work.desktop
```

En cas de problèmes de permission, il est préférable de l'installer localement, comme ceci :

```
desktop-file-install get-to-work.desktop --dir=.local/share/applications
```

C'est tout. Vous aurez votre logo prêt en tant qu'application dans votre lanceur. Vous pouvez également le configurer dans le dock.

#### Regardez l'icône en un clic en action

Voici un gif montrant mon récent script en un clic.

![Image](https://cdn-media-1.freecodecamp.org/images/9HPhZCIGUJQhUVIH51ptARU7z2HocD-syzns)

Un plus grand, de 2,6 Mo, peut être trouvé [ici](https://www.pineboat.in/img/005_one_click/one-click.gif) si vous voulez regarder de plus près.

En voici un autre que j'utilise pour commencer à écrire mon blog.

* Ouvre le dossier du blog dans VS code
* Charge `localhost` sur firefox
* Ouvre `hugo server` sur le terminal

Contrairement à l'exemple précédent, dans celui-ci, j'utilise le système d'exploitation elementary et le `pantheon-terminal` par défaut qui l'accompagne. Mais celui-ci n'ouvre pas plusieurs onglets, et je n'ai pas encore compris comment faire en sorte que `pantheon-terminal` le fasse (comme nous l'avons vu précédemment avec `gnome-terminal`). Ce petit `&` à la fin de `firefox` redonne le contrôle au script. Sinon, mon terminal ne s'ouvrirait pas jusqu'à ce que je ferme `firefox`.

```
#!/bin/bash  export WORK_DIR="~/pineboat" /opt/firefox/firefox localhost:1313 & code $WORK_DIR pantheon-terminal -e 'bash -c "cd $WORK_DIR;hugo server -wvFD"'
```

Enfin, j'ai configuré un fichier de bureau avec le logo de mon blog. Plutôt sympa, n'est-ce pas ?

J'espère que cela a été utile et économise quelques frappes. Applaudissez/Partagez/Tweetez pour faire savoir à votre réseau, si vous pensez qu'ils apprécieront cet article. En cas de problèmes, enregistrez-les sous ce [problème github](https://github.com/pineboat/pineboat.github.io/issues/4). Ou dans les conversations ci-dessous.

Merci pour votre temps et votre attention !

_Publié à l'origine sur [www.pineboat.in](https://www.pineboat.in/post/energize-terminal-with-git-bash-aliases-one-click-icon/) — une île inexplorée sur l'internet._