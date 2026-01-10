---
title: Dotfiles – Qu'est-ce qu'un Dotfile et Comment le Créer sur Mac et Linux
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-10-21T19:49:01.000Z'
originalURL: https://freecodecamp.org/news/dotfiles-what-is-a-dot-file-and-how-to-create-it-in-mac-and-linux
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/dmitry-ratushny-xsGApcVbojU-unsplash.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: macOS
  slug: macos
- name: Productivity
  slug: productivity
- name: shell script
  slug: shell-script
- name: zsh
  slug: zsh
seo_title: Dotfiles – Qu'est-ce qu'un Dotfile et Comment le Créer sur Mac et Linux
seo_desc: 'Dotfiles are important files that will play an integral role in your career
  as a software developer.

  First, they can help make you more productive. But not only that - you''ll be able
  to have that productive setup you created for youself on any machin...'
---

Les dotfiles sont des fichiers importants qui joueront un rôle intégral dans votre carrière de développeur logiciel.

Tout d'abord, ils peuvent vous aider à être plus productif. Mais pas seulement cela - vous pourrez avoir cette configuration productive que vous avez créée pour vous-même sur n'importe quelle machine.

Cet article est une introduction sur la façon de commencer avec les dotfiles.

Vous apprendrez ce qu'ils sont, comment les localiser sur votre système, et comment créer quelques dotfiles simples. En outre, je vous donnerai quelques suggestions et ressources sur la façon de personnaliser vos paramètres et d'élargir vos connaissances.

Commençons !

## Qu'est-ce que les dotfiles ?

De nombreux programmes logiciels stockent leurs paramètres de configuration dans des fichiers ou répertoires basés sur du texte brut.

Les dotfiles sont des fichiers de configuration pour divers programmes, et ils aident ces programmes à gérer leur fonctionnalité.

Ce qui les distingue des fichiers et répertoires réguliers est leur préfixe.

Les dotfiles sont nommés ainsi parce que chaque fichier et répertoire commence par un point (`.`)

Sur les systèmes basés sur Unix, les dotfiles sont masqués par le système d'exploitation par défaut.

### Exemples de dotfiles courants

La plupart des programmes stockent leurs configurations dans votre répertoire personnel par défaut.

Certains dotfiles courants que vous avez peut-être entendus ou utilisés auparavant sont :

- Si vous utilisez le shell Bash, vous avez peut-être un fichier `.bash_profile` et `.bashrc`, tous deux contenant des scripts qui se chargent chaque fois que vous démarrez une nouvelle session de terminal et configurez le shell.
- Si vous utilisez le shell Zsh, qui est le nouveau défaut pour MacOS, vous auriez (ou auriez créé) un fichier `.zshrc` qui configure et personnalise le shell.
- Si vous utilisez l'éditeur de code en ligne de commande Vim, vous stockeriez ses configurations dans un fichier `.vimrc`.
- Après avoir configuré et configuré Git sur votre machine locale, vous auriez un fichier `.gitconfig`, qui contiendrait toutes vos informations et paramètres.
- De nombreux programmes, au lieu de stocker leurs configurations dans votre répertoire personnel, les stockent plutôt dans le répertoire caché `.config` (dossier) sur votre système.

## Comment trouver les dotfiles

Dans Finder, la racine de votre répertoire personnel peut ressembler à ceci :

![Screenshot-2021-10-20-at-7.11.45-PM](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-20-at-7.11.45-PM.png)

Mais vous avez vu que les systèmes informatiques ont beaucoup plus de fichiers stockés qui sont masqués par défaut.

Pour afficher les dotfiles dans Finder, allez à la racine de votre répertoire personnel et maintenez les touches `Command Shift .` enfoncées en même temps.

Vous verrez bientôt une variété de dotfiles que vous avez créés vous-même ou qui ont été créés lorsque vous avez installé un logiciel.

![Screenshot-2021-10-20-at-7.12.04-PM](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-20-at-7.12.04-PM.png)

Pour afficher les dotfiles depuis la ligne de commande (là où vous les utiliserez et interagirez le plus), vous devez à nouveau ajouter quelques étapes supplémentaires à votre recherche.

La commande list, `ls`, qui liste tous les fichiers et répertoires dans le répertoire courant, ne montre pas les dotfiles par défaut - malgré le fait qu'ils soient là.

Tout d'abord, naviguez jusqu'à votre répertoire personnel. Vous pouvez utiliser la commande `cd` pour vous y rendre, si vous n'y êtes pas déjà.

Ensuite, utilisez la commande `ls` avec le flag `-a`, qui signifie `all`, comme ceci :

```shell
ls -a
```

Si vous voulez voir quelques informations supplémentaires sur vos fichiers, vous pouvez également utiliser le flag `-l`, qui liste les fichiers et répertoires au format long et inclut des détails sur la date et l'heure de leur création, leur taille, et ainsi de suite.

```shell
ls -la
```

Dans la sortie, vous verrez tous les fichiers et répertoires – y compris tous ceux cachés – dans votre répertoire personnel actuel.

![Screenshot-2021-10-19-at-1.37.15-PM](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-19-at-1.37.15-PM.png)

Chaque fichier et répertoire qui commence par un point/point est un dotfile.

## Pourquoi utiliser les dotfiles ?

Vos dotfiles vous sont personnels.

Vous passez un temps suffisant à affiner votre configuration. Vous sélectionnez des configurations et des paramètres qui conviennent le mieux à votre flux de travail, à votre esthétique et à vos préférences. Et vous obtenez un environnement de développement qui vous aide, personnellement, à être plus productif.

Et si, après tout ce temps passé, vous deviez maintenant passer à une nouvelle machine différente ? Cela signifie-t-il que vous devez tout recommencer depuis le début ?

Comment vous souviendriez-vous des paramètres et commandes exacts que vous avez utilisés ?

Ou si vous avez une deuxième machine et que vous voulez que votre configuration soit exactement la même sur les deux systèmes ?

L'un des principaux objectifs des développeurs est d'automatiser les tâches répétitives.

Créer un dépôt de dotfiles qui est contrôlé par source et hébergé sur GitHub vous fera gagner du temps lorsque vous voudrez configurer un nouvel ordinateur et installer les mêmes paramètres exacts que vous avez créés pour le précédent.

Ainsi, tous vos paramètres et préférences peuvent être réutilisables et cohérents sur d'autres machines.

## Comment créer des dotfiles

### Comment configurer un dossier pour contenir vos dotfiles

Il est bon de pratique d'avoir tous vos dotfiles dans leur propre dossier.

Pour simplifier, je vais montrer un exemple de création d'un dossier à la racine de votre répertoire personnel. Mais vous pouvez ajouter le dossier où vous le souhaitez.

De plus, je vais montrer des exemples de création d'un fichier `.zshrc` et `.vimrc`, mais des idées similaires s'appliquent à tout autre dotfile que vous créez.

Naviguez jusqu'à votre répertoire personnel (`cd`) et créez un répertoire nommé `dotfiles` qui contiendra tous vos fichiers de configuration :

```shell
mkdir dotfiles
```

Pour créer des dotfiles, vous utilisez la commande `touch` et passez le(s) nom(s) du(des) fichier(s) comme argument à la commande. Le(s) nom(s) de fichier(s) auront un point précédent.

Pour créer un fichier `.zshrc` et un fichier `.vimrc` dans le répertoire `dotfiles`, faites ceci :

```shell
touch ~/dotfiles/.zshrc  ~/dotfiles/.vimrc
```

Si ces fichiers existent déjà sur votre système et que vous souhaitez les déplacer dans le répertoire `dotfiles`, vous pouvez les déplacer là en utilisant la commande `mv` :

```shell
mv ~/.zshrc ~/dotfiles/
```

Le premier argument est le chemin actuel du fichier – le tilde (`~`) représente le répertoire personnel. Par défaut, la plupart des fichiers de configuration cachés s'y trouvent.

Le deuxième argument est le chemin où vous souhaitez déplacer le fichier. Dans ce cas, vous souhaitez le déplacer vers le répertoire dotfiles qui se trouve dans le répertoire personnel.

Vous pouvez faire de même pour le fichier `.vimrc` :

```shell
mv ~/.vimrc ~/dotfiles/
```

Pour afficher les fichiers :

```shell
ls -a dotfiles 
.         ..     .vimrc    .zshrc
```

Avec ces fichiers en place, vous pouvez ensuite ajouter toutes vos configurations préférées.

### Comment configurer les configurations

Voici quelques idées qui pourraient vous aider à démarrer les configurations des dotfiles que vous avez créés.

#### Comment personnaliser votre prompt Zsh

Après avoir configuré le fichier `.zshrc`, tout ce qui est ajouté à ce fichier affectera la personnalisation de votre programme de shell Zsh.

Maintenant pourrait être le moment de personnaliser votre prompt de shell. Cela sera personnel à votre goût, mais voici quelques ressources pour vous aider à démarrer :

- [Comment personnaliser votre prompt zsh comme un pro](https://www.freecodecamp.org/news/how-to-configure-your-macos-terminal-with-zsh-like-a-pro-c0ab3f3c1156/)
- [Jazz up your zsh terminal in seven steps](https://www.freecodecamp.org/news/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38/)
- [Plus d'idées pour personnaliser le prompt zsh](https://scriptingosx.com/2019/07/moving-to-zsh-06-customizing-the-zsh-prompt/)
- [Comment personnaliser le prompt zsh dans le terminal macOS](https://www.makeuseof.com/customize-zsh-prompt-macos-terminal/)

#### Comment personnaliser Vim

Après avoir créé le fichier `.vimrc`, vous pouvez personnaliser l'éditeur de texte en ligne de commande Vim. Voici quelques ressources pour vous aider à démarrer ce processus :

- [Guide de configuration Vimrc](https://www.freecodecamp.org/news/vimrc-configuration-guide-customize-your-vim-editor/)
- [Comment rendre Vim beau : 5 conseils de personnalisation de Vim](https://www.makeuseof.com/tag/5-things-need-put-vim-config-file/)

#### Qu'est-ce que les alias et les fonctions

Une façon d'améliorer votre flux de travail et d'augmenter votre productivité est de réduire le temps nécessaire pour taper les commandes que vous utilisez souvent. Vous pouvez y parvenir en créant des raccourcis.

Les alias sont des raccourcis vers les commandes du terminal. Ils sont une version plus courte d'une longue commande.

En tant que développeur, vous utiliserez souvent Git, il est donc judicieux de créer des alias Git pour vous faire gagner du temps sur les longues commandes Git répétitives. [Lisez quelques-uns des plus utiles dans cet article de freeCodeCamp](https://www.freecodecamp.org/news/how-to-use-git-aliases/).

Une autre façon de gagner du temps est de simplifier les processus.

Vous pouvez combiner deux commandes en une seule en créant un comportement isolé qui effectue un travail spécifique. Vous pouvez le faire en créant des fonctions.

Une fonction utile à créer est de combiner la commande de création d'un nouveau répertoire (`mkdir`) avec la commande de changement de répertoire (`cd`).

De cette façon, vous créerez un nouveau dossier et changerez immédiatement de répertoire – le tout en une seule étape.

La fonction pour ce faire ressemble à ceci :

```shell
function mkcd() {
  mkdir -p "$@" && cd "$_";
}
```

Pour en savoir plus sur Zsh, les fonctions, jetez un œil à [cet article sur Scripting OS X qui couvre à la fois les alias et les fonctions dans Zsh](https://scriptingosx.com/2019/07/moving-to-zsh-part-4-aliases-and-functions/).

Vous pouvez ajouter à la fois des alias et des fonctions à votre fichier `.zshrc` ou vous pouvez créer des fichiers `.aliases` et `.functions` séparés.

## Comment créer des liens symboliques pour vos dotfiles

Vous avez peut-être remarqué que aucun des paramètres que vous avez ajoutés aux fichiers dans le dossier `dotfiles` n'a d'effet sur votre système.

Les fichiers de configuration d'un programme, comme mentionné précédemment, sont cachés et stockés dans le répertoire personnel par défaut. C'est là que le programme cherchera et lira ses paramètres.

Il est bon de créer un lien symbolique (ou un pointeur) pour le fichier dans le répertoire `dotfiles` où vous avez stocké vos paramètres préférés ainsi que d'autres fichiers que vous avez créés, avec le fichier dans son répertoire personnel par défaut.

C'est comme si le fichier était à deux endroits en même temps !

Le fichier sera à la fois dans le répertoire `dotfiles` et il y aura également une "copie" dans le répertoire personnel.

Pour créer un lien, vous utilisez la commande `ln` (pour link) avec l'argument `-s` (qui signifie symbolique).

Voici comment créer un lien symbolique pour les fichiers `.zshrc` et `.vimrc` :

```shell
ln -s ~/dotfiles/.vimrc  ~/.vimrc
ln -s ~/dotfiles/.zshrc  ~/.zshrc
```

Cela permettra aux programmes que vous utilisez de savoir où se trouvent normalement leurs fichiers de configuration – dans le répertoire personnel.

```shell
ls -l ~/.zshrc 

lrwxr-xr-x  1 dionysialemonaki  staff  39 Oct 21 18:30 /Users/dionysialemonaki/.zshrc -> /Users/dionysialemonaki/dotfiles/.zshrc
```

En regardant les détails du fichier `.zshrc`, il montre que le fichier situé dans le répertoire personnel pointe vers le fichier dans le répertoire dotfiles. Le `->` indique le lien symbolique.

Créer des liens symboliques pour tous vos dotfiles manuellement est un processus fastidieux et peut devenir fatigant et répétitif rapidement à mesure que vous ajoutez plus de dotfiles au dossier.

Pour faciliter le processus, vous pouvez créer un script shell qui automatisera l'appel de `ln -s` sur les dotfiles que vous créez ou utiliser un [utilitaire](http://dotfiles.github.io/utilities/) pour ce travail.

## Comment contrôler les versions de vos dotfiles

Avoir vos fichiers sous contrôle de version vous aidera à suivre tous les changements que vous apportez au fil du temps, et vous permettra également de les partager sur GitHub.

Assurez-vous de changer de répertoire dans le répertoire `dotfiles` (`cd dotfiles`).

Suivez ces étapes pour organiser vos fichiers dans un dépôt git :

1. Initialisez le dépôt :

```shell
git init
```

2. Ajoutez tous les fichiers que vous avez créés jusqu'à présent :

```shell
git add .
```

3. Validez les changements et ajoutez un message de validation :

```shell
git commit -m "Added dotfiles"
```


### Comment héberger vos dotfiles sur GitHub

Assurez-vous d'être connecté à votre compte GitHub.

Ensuite, créez un nouveau dépôt :

![Screenshot-2021-10-21-at-5.21.59-PM](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-21-at-5.21.59-PM.png)

Donnez-lui un nom et cliquez sur "Create repository".

Ensuite, dans la ligne de commande, ajoutez :

```shell
git remote add origin url 

#où 'url' est l'URL GitHub du dépôt que vous avez précédemment créé
#se terminant par .git
```

Enfin,

```shell
git push -u origin main
```

Et maintenant vous êtes en mesure de partager vos dotfiles en ligne !


## Conclusion

Et voilà – vous connaissez maintenant les bases des dotfiles ! J'espère que vous avez trouvé ce tutoriel utile.

Votre projet de dotfiles vous suivra probablement tout au long de votre carrière et grandira à mesure que vous en apprendrez davantage sur les dotfiles eux-mêmes. Et il changera également à mesure que vous en apprendrez davantage sur ce que vous aimez et n'aimez pas concernant votre flux de travail et la configuration de votre environnement de développement par de nombreux essais et erreurs.

Merci d'avoir lu !