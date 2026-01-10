---
title: Comment configurer un nouveau bureau Ubuntu en utilisant uniquement des dotfiles
  et des scripts Bash
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-08-21T13:05:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-fresh-ubuntu-desktop-using-only-dotfiles-and-bash-scripts
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/E62F2B0D-E706-4A55-BAAC-84EF3F59D538.jpeg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
- name: Productivity
  slug: productivity
- name: Scripting
  slug: scripting
- name: shell script
  slug: shell-script
seo_title: Comment configurer un nouveau bureau Ubuntu en utilisant uniquement des
  dotfiles et des scripts Bash
seo_desc: One of my most favourite things about open source files on GitHub is the
  ability to see how others do (what some people might call) mundane things, like
  set up their .bashrc and other dotfiles. While I’m not as enthusiastic about ricing
  as I was when...
---

L'une de mes choses préférées à propos des fichiers open source sur GitHub est la possibilité de voir comment les autres font (ce que certaines personnes pourraient appeler) des choses banales, comme configurer leur `.bashrc` et autres dotfiles. Bien que je ne sois pas aussi enthousiaste à propos du ricing que je l'étais lorsque je suis arrivé du côté Linux, je suis toujours assez excité lorsque je trouve un paramètre de configuration qui rend les choses plus jolies et plus rapides, et donc, meilleures.

J'ai récemment découvert quelques-unes de ces choses, en particulier dans les [dotfiles de Tom Hudson](https://github.com/tomnomnom). Tom semble aimer scripter les choses, et certaines de ces choses incluent la création automatique de liens symboliques, et l'installation d'applications de dépôt Ubuntu et d'autres programmes. Cela m'a fait réfléchir. Pourrais-je automatiser la configuration d'une nouvelle machine pour répliquer la mienne actuelle ?

Étant quelqu'un généralement enclin à démonter les choses pour voir comment elles fonctionnent, je sais que j'ai parfois abîmé mon ordinateur portable. (Généralement lorsque je suis loin de chez moi, et que mon disque dur de sauvegarde n'est pas avec moi.) Dans ces situations rares mais vraiment gênantes où mon ordinateur devient une coquille vide de ce qu'il était, (ba-dum-ching) ce serait assez agréable d'avoir un moyen rapide et simple de remettre Humpty Dumpty ensemble, exactement comme je l'aime.

Contrairement à la création d'une [image disque et à sa restauration ultérieure](https://askubuntu.com/questions/19901/how-to-make-a-disk-image-and-restore-from-it-later), une collection de scripts bash est plus facile à créer, à maintenir et à déplacer. Ils ne nécessitent aucune utilité spéciale, seulement une méthode de transport externe. C'est comme transmettre la recette, au lieu du gâteau bundt entier. (Mmm, gâteau.)

De plus, une fonctionnalité comme celle-ci serait super utile lors de la configuration d'une machine virtuelle, ou VM, ou même simplement d'un serveur privé virtuel, ou VPS. (Les deux, maintenant que j'écris cela, seraient probablement des cibles plus indulgentes pour mes expérimentations les plus destructrices... vivre et apprendre !)

Eh bien, après quelques recherches avec grep et Google et en fouillant un peu, j'ai maintenant une suite de scripts qui peut faire cela :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/cover-1.jpg)

_Voir [une vidéo de la configuration ici](https://victoria.dev/verbose/how-to-set-up-a-fresh-ubuntu-desktop-using-only-dotfiles-and-bash-scripts)._

Il s'agit de la fin d'un essai des scripts de configuration sur un nouveau bureau Ubuntu, chargé à partir d'un USB bootable. Tous mes programmes et paramètres ont été restaurés en moins de trois minutes !

Cet article expliquera comment réaliser la configuration automatique d'un ordinateur exécutant Ubuntu Desktop (dans mon cas, Ubuntu LTS 18.04) en utilisant des scripts bash. La majorité des informations couvertes est applicable à toutes les distributions Linux de bureau, bien que certaines syntaxes puissent différer. Les scripts bash couvrent trois domaines principaux : le lien des dotfiles, l'installation de logiciels à partir d'Ubuntu et d'autres sources, et la configuration de l'environnement de bureau. Nous couvrirons chacun de ces domaines et passerons en revue les parties importantes afin que vous puissiez commencer à créer vos propres scripts.

# Dotfiles

Les dotfiles sont ce que la plupart des passionnés de Linux appellent les fichiers de configuration. Ils résident généralement dans le répertoire personnel de l'utilisateur (désigné dans les scripts bash par la variable [builtin](https://www.tldp.org/LDP/abs/html/internal.html#BUILTINREF) `$HOME`) et contrôlent l'apparence et le comportement de toutes sortes de programmes. Les noms de fichiers commencent par `.`, ce qui désigne les fichiers cachés dans Linux (d'où les "dot" files). Voici quelques dotfiles courants et les façons dont ils sont utiles.

## `.bashrc`

Le fichier `.bashrc` est une liste de commandes exécutées au démarrage par les shells interactifs non-login. [Les shells interactifs vs non-interactifs](https://www.tldp.org/LDP/abs/html/intandnonint.html) peuvent être un peu déroutants, mais ne sont pas nécessaires pour nous ici. Pour nos besoins, chaque fois que vous ouvrez un nouveau terminal, voyez une invite et pouvez y taper des commandes, votre `.bashrc` a été exécuté.

Les lignes de ce fichier peuvent aider à améliorer votre flux de travail en créant des alias qui réduisent les frappes, ou en affichant une invite utile avec des informations utiles. Il peut même exécuter des programmes créés par l'utilisateur, comme [Eddie](https://github.com/victoriadrake/eddie-terminal). Pour plus d'idées, vous pouvez consulter [mon fichier `.bashrc` sur GitHub](https://github.com/victoriadrake/dotfiles/blob/ubuntu-19.10/.bashrc).

## `.vimrc`

Le dotfile `.vimrc` configure le champion de tous les éditeurs de texte, [Vim](https://www.vim.org/about.php). (Si vous n'avez pas encore utilisé les pouvoirs des raccourcis clavier, je vous recommande fortement [un jeu amusant pour apprendre Vim](https://vim-adventures.com/).)

Dans `.vimrc`, nous pouvons définir les préférences de l'éditeur telles que les paramètres d'affichage, les couleurs et les raccourcis clavier personnalisés. Vous pouvez consulter [mon `.vimrc` sur GitHub](https://github.com/victoriadrake/dotfiles/blob/ubuntu-19.10/.vimrc).

D'autres dotfiles peuvent être utiles en fonction des programmes que vous utilisez, tels que `.gitconfig` ou `.tmux.conf`. Explorer les dotfiles sur GitHub est un excellent moyen de se faire une idée de ce qui est disponible et utile pour vous !

# Lier les dotfiles

Nous pouvons utiliser un script pour créer des liens symboliques, ou [symlinks](https://en.wikipedia.org/wiki/Symbolic_link#POSIX_and_Unix-like_operating_systems) pour tous nos dotfiles. Cela nous permet de conserver tous les fichiers dans un dépôt central, où ils peuvent être facilement gérés, tout en fournissant une sorte de placeholder à l'endroit où nos programmes s'attendent à trouver le fichier de configuration. Cela est généralement, mais pas toujours, le répertoire personnel de l'utilisateur. Par exemple, puisque je stocke mes dotfiles sur GitHub, je les conserve dans un répertoire avec un chemin comme `~/github/dotfiles/` tandis que les fichiers eux-mêmes sont liés symboliquement, résultant en un chemin comme `~/.vimrc`.

Pour vérifier et gérer de manière programmatique les fichiers et symlinks existants, puis en créer de nouveaux, nous pouvons utiliser [ce script shell élégant](https://github.com/victoriadrake/dotfiles/blob/master/scripts/symlink.sh). Je le complimente seulement parce que j'ai ouvertement volé le cœur de celui-ci à partir du [script de configuration de Tom](https://github.com/tomnomnom/dotfiles/blob/master/setup.sh), donc je ne peux pas prendre le crédit pour sa beauté.

Le script `symlink.sh` fonctionne en tentant de créer des symlinks pour chaque dotfile dans notre `$HOME`. Il vérifie d'abord si un symlink existe déjà, ou si un fichier ou répertoire régulier avec le même nom existe. Dans le premier cas, le symlink est supprimé et recréé ; dans le second, le fichier ou répertoire est renommé, puis le symlink est créé.

# Installer des logiciels

L'une des belles choses à propos de l'exploration des scripts shell est de découvrir combien de choses peuvent être réalisées en utilisant uniquement la ligne de commande. En tant que personne dont la première exposition aux ordinateurs était à travers un système d'exploitation graphique, je trouve que travailler dans le terminal est rafraîchissant et rapide.

Avec Ubuntu, la plupart des programmes dont nous avons probablement besoin sont disponibles via les dépôts de logiciels Ubuntu par défaut. Nous les recherchons généralement avec la commande `apt search <program>` et les installons avec `sudo apt install <program>`. Certains logiciels que nous aimerions peuvent ne pas être dans les dépôts par défaut, ou peuvent ne pas y être offerts dans la version la plus récente. Dans ces cas, nous pouvons toujours installer ces programmes dans Ubuntu en utilisant un [PPA, ou Personal Package Archive](https://en.wikipedia.org/wiki/Ubuntu#Package_Archives). Nous devrons simplement être prudents quant aux PPA que nous choisissons, en veillant à ce qu'ils proviennent des sources officielles.

Si un programme que nous aimerions n'apparaît pas dans les dépôts par défaut ou ne semble pas avoir de PPA, nous pouvons toujours être en mesure de l'installer via la ligne de commande. Une recherche rapide pour "installation command line" devrait donner quelques réponses.

Puisque les scripts bash ne sont qu'une collection de commandes que nous pourrions exécuter individuellement dans le terminal, créer un script pour installer tous nos programmes souhaités est aussi simple que de mettre toutes les commandes dans un fichier de script. J'ai choisi d'organiser mes scripts d'installation entre les dépôts par défaut, qui sont installés par [mon script `aptinstall.sh`](https://github.com/victoriadrake/dotfiles/blob/ubuntu-19.10/scripts/aptinstall.sh), et les programmes qui impliquent des sources externes, gérés avec [mon script `programs.sh`](https://github.com/victoriadrake/dotfiles/blob/ubuntu-19.10/scripts/programs.sh).

# Configurer l'environnement de bureau

Lors des récentes occasions où j'ai obtenu un nouveau bureau (intentionnellement ou non), je semble toujours oublier combien de temps il faut pour se souvenir, trouver, puis changer tous les paramètres de l'environnement de bureau. Raccourcis clavier, espaces de travail, paramètres de son, mode nuit... cela s'accumule !

Heureusement, tous ces paramètres doivent être stockés quelque part dans un format non graphique, ce qui signifie que si nous pouvons découvrir comment cela est fait, nous pouvons probablement trouver un moyen de manipuler facilement les paramètres avec un script bash. Et voici la commande terminal, `gsettings list-recursively`.

Il y a une tonne de paramètres pour l'environnement de bureau GNOME. Nous pouvons rendre la liste plus facile à parcourir (si, comme moi, vous êtes parfois du genre à dire "Laissez-moi simplement tout regarder et comprendre ce que je veux !") en utilisant `less` : `gsettings list-recursively | less`. Alternativement, si nous avons une idée de ce que nous pourrions chercher, nous pouvons utiliser `grep` : `gsettings list-recursively | grep 'keyboard'`.

Nous pouvons manipuler nos paramètres avec la commande `gsettings set`. Il peut parfois être difficile de trouver la syntaxe pour le paramètre que nous voulons, donc lorsque nous construisons notre script pour la première fois, je recommande d'utiliser l'interface graphique pour faire les changements, puis de trouver la ligne `gsettings` que nous avons changée et d'enregistrer sa valeur.

Pour quelques idées, vous pouvez consulter [mon script `desktop.sh` sur GitHub](https://github.com/victoriadrake/dotfiles/blob/ubuntu-19.10/scripts/desktop.sh).

# Mettre le tout ensemble

Avoir des scripts modulaires (un pour les symlinks, deux pour installer des programmes, un autre pour les paramètres de bureau) est utile à la fois pour garder les choses organisées et pour pouvoir exécuter certains mais pas tous les scripts de configuration automatisée. Par exemple, si je devais configurer un VPS dans lequel je n'utilise que la ligne de commande, je n'aurais pas besoin de m'occuper de l'installation de programmes graphiques ou de paramètres de bureau.

Dans les cas où je veux exécuter tous les scripts, cependant, le faire un par un est un peu fastidieux. Heureusement, puisque les scripts bash peuvent eux-mêmes être exécutés par des commandes de terminal, nous pouvons simplement écrire un autre script maître pour les exécuter tous !

Voici mon script maître pour gérer la configuration d'une nouvelle machine de bureau Ubuntu :

```bash
#!/bin/bash

./symlink.sh
./aptinstall.sh
./programs.sh
./desktop.sh

# Obtenir toutes les mises à jour
sudo apt upgrade -y

# Voir nos changements bash
source ~/.bashrc

# Un bonjour amusant
figlet "... et nous sommes de retour !" | lolcat
```

J'ai ajouté la ligne de mise à jour pour bonne mesure. Elle s'assurera que les programmes installés sur notre nouveau bureau ont les dernières mises à jour. Maintenant, une simple commande bash s'occupera de tout !

Vous avez peut-être remarqué que, bien que notre bureau ait maintenant l'air et fonctionne de manière familière, ces scripts ne couvrent pas un domaine très important : nos fichiers. Espérons que vous avez une méthode de sauvegarde pour ceux-ci qui implique une forme de matériel externe fiable. Si ce n'est pas le cas, et si vous avez tendance à mettre votre travail dans des hôtes de dépôts externes comme GitHub ou GitLab, j'ai un moyen de [cloner et sauvegarder automatiquement vos dépôts GitHub avec des one-liners bash](https://victoria.dev/verbose/how-to-write-bash-one-liners-for-cloning-and-managing-github-and-gitlab-repositories/).

S'appuyer sur des hôtes de dépôts externes n'offre cependant pas une couverture à 100 %. Les fichiers que vous ne mettriez pas dans un dépôt hébergé externement (privé ou non) ne peuvent donc pas être récupérés. Les objets ignorés par Git qui ne peuvent pas être générés à partir des fichiers inclus, comme les clés privées et les secrets, ne seront pas recréés. Ces fichiers, cependant, sont probablement suffisamment petits pour que vous puissiez en mettre beaucoup sur quelques clés USB cryptées (et si vous n'avez pas de sauvegardes de clés privées, peut-être devriez-vous faire cela en premier ?).

Cela dit, j'espère que cet article vous a donné au moins quelques idées sur la façon dont les dotfiles et les scripts bash peuvent aider à automatiser la configuration d'un nouveau bureau. Si vous trouvez des paramètres utiles, aidez les autres à les découvrir en partageant vos dotfiles également !