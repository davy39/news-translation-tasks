---
title: Comment utiliser Lazygit pour améliorer votre flux de travail Git
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2025-04-10T13:49:46.631Z'
originalURL: https://freecodecamp.org/news/how-to-use-lazygit-to-improve-your-git-workflow
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744293114488/5332db88-bff6-4aef-91eb-3423f3b95e1a.png
tags:
- name: Lazygit-tutorial
  slug: lazygit-tutorial
- name: Lazygit
  slug: lazygit
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment utiliser Lazygit pour améliorer votre flux de travail Git
seo_desc: 'Lazygit is an open-source command line terminal UI for Git commands that
  I’ve used for the last couple of years, and it’s become my new best friend.

  Basically, the Lazygit tool is a wrapper for the Git command line that replaces
  it with a UI. Instead...'
---

[Lazygit](https://github.com/jesseduffield/lazygit) est une interface utilisateur de terminal en ligne de commande open-source pour les commandes Git que j'ai utilisée au cours des dernières années, et elle est devenue ma nouvelle meilleure amie.

En gros, l'outil Lazygit est un wrapper pour la ligne de commande Git qui la remplace par une interface utilisateur. Au lieu de taper encore et encore les commandes Git dans votre terminal, vous pouvez utiliser des raccourcis clavier pour commiter, pousser, tirer, créer, éditer et supprimer des branches dans votre projet.

En termes simples, Lazygit vous aide à augmenter votre productivité tout en travaillant avec Git.

Dans cet article, nous allons passer en revue les fonctionnalités essentielles de Lazygit, et je vous montrerai comment il fonctionne.

## Table des matières :

1. [Comment installer Lazygit](#heading-installation)
   
2. [Comment utiliser Lazygit](#comment-utiliser-lazygit)
   
3. [Raccourcis et mappings de touches dans Lazygit](#heading-raccourcis-et-mappings-de-touches-dans-lazygit)
   
4. [Autres raccourcis clavier dans Lazygit](#autres-raccourcis-clavier-dans-lazygit)
   
5. [Conclusion](#conclusion)
   

## Comment installer Lazygit

Avant de commencer, vous devrez vous assurer qu'il est installé sur votre machine. Vous pouvez installer l'outil dans votre système en utilisant les méthodes suivantes (selon votre système) :

### Homebrew

Vous pouvez [installer lazygit](https://formulae.brew.sh/formula/lazygit#default) dans macOS en utilisant Homebrew comme ceci :

```bash
brew install lazygit
```

### Scoop (Windows)

Vous pouvez [installer lazygit](https://scoop.sh/#/apps?q=lazygit) dans Windows en utilisant Scoop comme ceci :

```bash
# Ajouter le bucket extras
scoop bucket add extras

# Installer lazygit
scoop install lazygit
```

### Arch Linux

Vous pouvez [installer lazygit](https://aur.archlinux.org/packages/lazygit-git) dans Arch en utilisant Pacman comme ceci :

```bash
sudo pacman -S lazygit
```

### Ubuntu et Debian

Vous pouvez installer lazygit dans Ubuntu et Debian en utilisant la commande suivante :

```bash
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/download/v${LAZYGIT_VERSION}/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit -D -t /usr/local/bin/
```

Vérifiez l'installation correcte de lazygit :

```bash
lazygit --version
```

La sortie de la commande ressemble à ceci :

```bash
[1;34m[0m lazygit --version
commit=, build date=, build source=nix, version=0.44.1, os=linux, arch=amd64, git version=2.47.0
```

### Fedora et RHEL

Vous pouvez installer lazygit dans Fedora et RHEL en utilisant DNF comme ceci :

```bash
sudo dnf copr enable atim/lazygit -y
sudo dnf install lazygit
```

### NixOS

Vous pouvez [installer lazygit](https://search.nixos.org/packages?channel=24.11&from=0&size=50&sort=relevance&type=packages&query=lazygit) dans NixOS en utilisant la méthode suivante :

```bash
# avec nix-shell
nix-shell -p lazygit

# avec nix-env
nix-env -iA lazygit

# avec /etc/nixos/configuration.nix
environment.systemPackages = [
  pkgs.lazygit
];
# ou avec enable lazygit flakes
nix run nixpkgs#lazygit
```

## Comment utiliser Lazygit

Pour utiliser Lazygit, vous n'avez pas besoin de connaissances avancées sur Lazygit ou la CLI Git. Si vous êtes débutant, ce n'est pas grave - je vais vous guider à travers le processus et les bases ici.

La chose principale à comprendre est le fonctionnement des mappings de touches (raccourcis clavier). Dans ce tutoriel, je ne vais pas discuter de chaque mapping de touches, mais je vais vous enseigner quelques-uns des mappings de touches Lazygit les plus courants que vous utiliserez au quotidien. Ils vous aideront à construire une base solide pour utiliser l'outil efficacement.

Pour utiliser Lazygit, ouvrez d'abord le terminal que vous utilisez. Par exemple, j'utilise la distribution GNOME, donc j'utiliserai le [terminal Ptyxis](https://gitlab.gnome.org/chergert/ptyxis).

Tapez la commande `lazygit` dans votre terminal :

```bash
lazygit
```

La sortie de la commande devrait ressembler à ceci dans votre terminal :

![Démo cli Lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743685042853/ab3f10f0-0d13-44d3-a86a-a58676cf30a5.gif align="center")

L'interface utilisateur de Lazygit est divisée en six panneaux, ou sections. Chaque panneau sert un cas d'utilisation spécifique. Explorons ces panneaux plus en détail. Vous pouvez les voir mis en évidence dans l'image ci-dessous :

![Explorer les panneaux Lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743687006438/5ca2451e-d4a0-42a7-89b2-0b94fd4ca162.png align="center")

### Panneaux ou sections dans Lazygit

Comme je l'ai mentionné ci-dessus, il y a six panneaux principaux dans Lazygit. Ils sont :

1. Statut
   
2. Fichiers
   
3. Branches
   
4. Commits
   
5. Stash
   
6. Aperçus
   

Les panneaux les plus importants dans Lazygit sont les fichiers, les branches et les commits, mais nous allons examiner chacun des six maintenant.

#### Panneau de statut

Le panneau de statut fournit un aperçu de votre dépôt actuel et de la branche actuellement extraite, y compris les modifications locales et distantes.

![Panneau de statut dans Lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743759630157/a7ef738b-5353-4941-9eb5-073d3235aaba.png align="center")

De plus, lorsque vous cliquez sur le texte du panneau de statut, il ouvre un nouvel onglet ou panneau où il affiche la liste des dépôts récemment ouverts.

![Dépôts récemment ouverts](https://cdn.hashnode.com/res/hashnode/image/upload/v1743760171736/8edb2f41-86ad-4e64-95f2-b1310d8c6f57.png align="center")

#### Panneau des fichiers

Le panneau des fichiers affiche les listes des fichiers dans votre dépôt qui ont été modifiés ou changés. Vous pouvez voir les fichiers que vous avez supprimés ou rejetés et non mis en scène.

![Panneau des fichiers dans Lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743760570130/c891940b-4ba2-4fcb-a867-817b74e53618.png align="center")

#### Panneau des branches

Le panneau des branches affiche les listes des branches locales et distantes disponibles dans ce dépôt.

![Panneau des branches dans lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743761276628/b34dc945-11c8-482d-8c4d-51783c68bf55.png align="center")

#### Panneau des commits

Le panneau des commits affiche une liste des commits dans la branche actuelle, ce qui vous permet de visualiser, extraire ou interagir avec (visualiser/annuler/etc.) des commits spécifiques.

![Panneau des commits dans lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743761671236/80a7321a-8d16-4add-bc4a-db52d2987836.png align="center")

#### Panneau des stashes

Le panneau des stashes vous aide à gérer vos changements stashés, vous permettant de les appliquer, supprimer ou visualiser. Git stash est un emplacement pour stocker les changements non commités (fichiers modifiés, mis en scène ou non suivis) dans un endroit caché, vous permettant de changer de branche sans commiter ou rejeter les changements.

![Panneau des stashes dans laygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743764679570/d7233d92-cfb0-4757-a338-bcc3d9fec2b8.png align="center")

#### Panneau de prévisualisation

Le panneau de prévisualisation vous permet de prévisualiser les changements non mis en scène, les commits, les logs, le contenu des fichiers, etc. dans Lazygit.

![Panneau de prévisualisation dans lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743765844602/7c492361-bbcf-4d2c-8588-b0c3e8704132.png align="center")

Pour basculer entre les panneaux, utilisez les touches fléchées gauche et droite ou les raccourcis clavier spécifiques affichés en haut de chaque panneau.

Appuyez sur `1` pour ouvrir le panneau de statut, `2` pour les fichiers, `3` pour les branches, `4` pour les commits, et `5` pour le panneau de stash.

![Navigation entre les panneaux dans lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743766590099/91689f4d-eba3-47cf-80a6-e18307c326cd.gif align="center")

## **Raccourcis et mappings de touches dans Lazygit**

Lazygit est particulièrement populaire grâce à ses raccourcis. Vous n'avez pas besoin d'écrire les mêmes commandes Git dans le terminal encore et encore. Au lieu de cela, vous devez simplement utiliser un raccourci.

Par exemple, habituellement lorsque vous commitez un fichier, vous ajoutez d'abord le fichier en utilisant `git add` puis vous commitez le fichier en utilisant `git commit`.

Mais dans Lazygit, vous devez simplement sélectionner le fichier en utilisant votre souris ou les touches haut et bas et appuyer sur espace pour commiter le fichier.

Dans Lazygit, tout fonctionne autour des commandes de raccourci, et vous utilisez des raccourcis pour effectuer des opérations Git courantes. Voici quelques commandes essentielles que nous allons passer en revue dans ce tutoriel :

* `a` – Mettre en scène ou annuler la mise en scène de tous les fichiers disponibles dans le panneau des fichiers.
   
* `espace` (panneau des fichiers) – Mettre en scène ou annuler la mise en scène d'un seul fichier dans le panneau des fichiers.
   
* `c` – Commiter les changements mis en scène en ouvrant un éditeur de message de commit.
   
* `p` – Pousser les commits vers le dépôt distant.
   
* `P` – Tirer les changements depuis le dépôt distant.
   
* `z` – Annuler le commit.
   
* `s` – Stasher les changements, vous permettant de changer de branche ou d'effectuer d'autres opérations.
   
* `S` – Visualiser et appliquer les changements stashés.
   
* `n` – Créer une nouvelle branche.
   
* `d` – Supprimer votre branche.
   
* `y` – Copier dans le presse-papiers.
   
* `M` – Fusionner la branche.
   
* `espace` (panneau des branches) – Extraire la branche cible sélectionnée.
   
* `e` – Éditer ou ouvrir le fichier dans un éditeur externe.
   
* `q` – Quitter Lazygit et revenir au terminal.
   
* `d` – Rejeter tout changement dans le fichier.
   
* `?` – Ouvrir le menu des raccourcis clavier.
   

Maintenant, passons en revue ces raccourcis afin que vous puissiez comprendre comment ils fonctionnent et les voir en action.

### Comment commiter un fichier

Pour commiter un fichier dans Lazygit, sélectionnez d'abord le fichier dont vous avez besoin en appuyant sur la touche `espace` ou la touche `a` ou en double-cliquant sur le fichier. Ensuite, appuyez sur `c`, et un nouveau panneau devrait s'ouvrir. Là, vous pouvez ajouter un message et appuyer sur Entrée pour commiter le fichier.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743770682782/cbd83578-a286-482f-aeaa-31a9715a5483.gif align="center")

### Comment tirer et pousser du code

Pour tirer le code distant depuis le serveur Git (Github, GitLab, Gitea, etc.), vous pouvez appuyer sur `p` (p minuscule) :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743774642242/decec44c-7622-432a-9da5-81b14b60ef8a.gif align="center")

Pour pousser le code local vers un serveur Git, vous pouvez appuyer sur `P` (P majuscule) :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743842516002/37647a76-afe5-4d4b-acfc-fc85f1010749.gif align="center")

### Comment créer et supprimer une branche

Pour créer une nouvelle branche dans Lazygit, appuyez sur `n`. Un nouveau panneau s'ouvrira où vous ajouterez le nom de la branche et appuierez sur Entrée.

![Créer une nouvelle branche dans lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743843881624/6c4db14e-0102-4333-be56-5d3796ab1c50.gif align="center")

Pour supprimer une branche, appuyez sur `d` puis spécifiez si vous souhaitez supprimer la branche dans un dépôt local ou distant. Dans l'exemple suivant, je supprime une branche locale.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743847541934/34e378b6-03ac-4e6d-93d0-35aaeda39e57.gif align="center")

> Note : Pour supprimer et créer une nouvelle branche dans Lazygit, sélectionnez d'abord le panneau des branches puis appuyez sur la touche de raccourci correspondante pour supprimer une branche. Appuyez sur la touche d pour supprimer, puis pour créer une branche, appuyez sur la touche n. Sinon, cela ne fonctionnera pas.

### Comment annuler un commit

Pour annuler le dernier commit dans Lazygit, appuyez simplement sur `z`. Un nouveau panneau s'ouvrira, montrant les détails du commit que vous annulez. Ensuite, appuyez sur Entrée.

![Annuler un commit dans lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743852917448/a3f2cab7-2806-48e4-a749-90f821b537dc.gif align="center")

### Comment fusionner une branche

Pour fusionner une branche, appuyez sur `M` (M majuscule). Pour ouvrir les options de fusion, choisissez le type de fusion, puis appuyez sur Entrée.

#### Type de fusion :

* **Fusion** : Une fusion standard, préservant l'historique de la branche.
   
* **Fusion squash** : Combine tous les commits de la branche en un seul commit sur la branche cible.
   
* **Fusion squash et laisser non commité** : Identique à la fusion squash, mais laisse les changements non commités.
   

![Fusionner une branche dans lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743921595283/e46e0c89-b69a-4462-acd3-295045c99dfd.gif align="center")

### Comment résoudre les conflits de fusion

Pour résoudre les conflits de fusion dans Lazygit, fusionnez d'abord une branche en appuyant sur `M`, puis choisissez le type de fusion (que je décris dans la sous-section sur la façon de fusionner une branche) et appuyez sur Entrée.

Si des conflits de fusion se produisent, le(s) fichier(s) en conflit apparaissent dans le panneau des fichiers. Appuyez sur Entrée pour visualiser les conflits de fusion dans le panneau de prévisualisation et naviguez entre les conflits en utilisant les touches haut et bas. Sélectionnez les conflits de fusion corrects, appuyez sur la touche espace, et votre problème de fusion sera résolu.

![Résoudre les conflits de fusion dans lazygit](https://cdn.hashnode.com/res/hashnode/image/upload/v1743921640247/e5b7f971-f027-47df-be4c-a90b356e24f8.gif align="center")

### Comment rejeter les changements

Pour rejeter ou supprimer tout changement dans un fichier ou un commit, appuyez sur `d`.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743774406564/bc5b91fb-2d33-41d0-95b9-667478c4c8db.gif align="center")

### Comment copier

Pour copier un nom de fichier, un chemin, un hash de commit, un message, une URL, un auteur ou tout autre détail, sélectionnez d'abord le commit ou le fichier, puis appuyez sur `y` pour copier l'information.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743856793802/e23d9e5c-b0b4-40a0-8124-f94669b377c0.gif align="center")

## Autres raccourcis clavier dans Lazygit

Il existe d'autres raccourcis clavier dans Lazygit que je n'ai pas discutés dans cet article. Pour en savoir plus sur chaque raccourci clavier, vous pouvez consulter le menu des raccourcis clavier. Ouvrez le menu des raccourcis clavier et appuyez sur `?`.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743843262905/a4aba097-999b-4ff8-bd00-661181d96aad.gif align="center")

Lorsque vous ouvrez le menu d'aide des raccourcis clavier, il change en fonction du panneau dans lequel vous vous trouvez.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1743915037200/9339b7b1-b2a4-45e5-8a51-5be0a9f2a319.gif align="center")

## Conclusion

Lazygit vous aide à devenir plus productif lorsque vous travaillez avec Git ou les commandes Git. En tant que débutant, commencer avec Lazygit peut être quelque peu difficile en raison de ses mappings de touches, mais une fois que vous les maîtrisez, ils sont assez faciles à retenir et à utiliser.

Si vous êtes un utilisateur de Lazygit pour la première fois, ma suggestion est d'éviter d'utiliser Lazygit sur un dépôt de travail. Au lieu de cela, créez un dépôt de démonstration et essayez-le/practiquez.

Pour en savoir plus sur les [raccourcis ou raccourcis clavier de LazyGit](https://github.com/jesseduffield/lazygit/blob/master/docs/keybindings/Keybindings_en.md), vous pouvez vous référer à la documentation de Lazygit. Vous pouvez également consulter les tutoriels YouTube suivants pour les débutants :

* [LazyGIt - Une manière plus rapide et plus facile d'utiliser Git sur Terminal & NeoVim](https://www.youtube.com/watch?v=A6F_8ajlrYQ)
   
* [Lazygit - La meilleure façon d'utiliser Git sur le Terminal & Neovim](https://www.youtube.com/watch?v=Ihg37znaiBo)
   
* [Ma nouvelle manière préférée d'utiliser Git](https://www.youtube.com/watch?v=06lEP59XAgM)
   
* [LazyGit : Git sans effort dans votre Terminal !](https://www.youtube.com/watch?v=dSWJKcEiAaM)