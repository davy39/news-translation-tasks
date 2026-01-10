---
title: Une introduction à Vim pour les utilisateurs de Visual Studio Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-24T17:55:14.000Z'
originalURL: https://freecodecamp.org/news/vim-for-people-who-use-visual-studio-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/vimvsvscode.png
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: vim
  slug: vim
- name: Web Development
  slug: web-development
seo_title: Une introduction à Vim pour les utilisateurs de Visual Studio Code
seo_desc: 'By Jared Nutt

  Hot tips to bring the awesomeness of Visual Studio Code to Vim.

  Front-Matter

  I want to start by saying, this is not an editor-shame article. You can use whatever
  text editor you want. It really doesn’t matter. I’m only writing this beca...'
---

Par Jared Nutt

Des conseils pour apporter l'awesomeness de Visual Studio Code à Vim.

### Préambule

Je veux commencer par dire que ceci n'est pas un article pour critiquer les éditeurs de texte. Vous pouvez utiliser l'éditeur de texte que vous voulez. Cela n'a vraiment pas d'importance. Je n'écris ceci que parce que j'ai trouvé un niveau de productivité dans Vim que je n'avais pas dans les éditeurs que j'utilisais auparavant (Sublime Text, Atom ou VSCode).

Si vous avez entendu parler de Vim et que vous souhaitez l'essayer, j'espère que cet article pourra vous apporter un peu de familiarité que vous trouverez dans VSCode.

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/5b26kbDYzsqGartaXz" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

### Pourquoi Vim ?

Il y a beaucoup de raisons d'utiliser Vim, en voici quelques-unes.

#### Gardez vos mains à 10 et 2

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/11Qm8y698eYC8U" width="480" height="198" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

Lorsque vous utilisez uniquement le clavier, il y aura un gain de vitesse inhérent simplement parce que vous n'avez pas à déplacer physiquement vos mains. Et peut-être que vous êtes une ceinture noire en mouvement de souris, et que vous pouvez vous déplacer d'avant en arrière à une vitesse invisible à l'œil nu. Pour le reste d'entre nous, simples humains, cela prend du temps.

Faisons un peu de maths rapides.

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/Fh28yu3oxWRlm" width="480" height="210" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

Il me faut 600 ms pour déplacer ma main des "touches de base" à la souris. En moyenne, pour l'argument, je fais cela une fois par minute lorsque j'écris du [code](https://www.java67.com/2018/06/21-websites-to-learn-how-to-code-for.html). Que ce soit pour faire défiler, naviguer vers un nouveau fichier, ou quelque chose de similaire.

600 (temps perdu en ms) x 60 (fois par heure) x 5 (heures où je code réellement) = 180 000 ms perdus =

> 3. Minutes. Chaque. Jour.

Oui, d'accord, peut-être que cela ne semble pas si grave, mais ces 3 minutes pourraient être utilisées pour écrire une fonction, ou [refactoriser du code](http://www.java67.com/2016/02/5-books-to-improve-coding-skills-of.html), et non pas pour agiter la main comme si vous étiez Harry Potter !

#### Vitesse

<figure class="kg-card kg-image-card kg-card-hascaption" style="text-align: center;">
    <iframe src="https://giphy.com/embed/4wEFKQgMGLlqU" width="480" height="264" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    <figcaption>D'accord, donc peut-être que 65 n'est plus vraiment si rapide, mais hey, c'était en 1994 !</figcaption>
</figure>

Ma citation préférée qui décrit ce que c'est que de coder dans VIM :

> "Coder à la vitesse de la pensée"

Vim est construit autour de l'idée que vous communiquez directement avec votre ordinateur. Vous lui dites ce que vous voulez, et il le fait pour vous. La plus grande révélation pour moi a été ce petit détail :

Pour supprimer tout ce qui se trouve entre deux objets (parenthèses, guillemets, etc.), c'est aussi simple que :

`di'`

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Hnet.com-image.gif)
_Ordinateur : Supprimer, à l'intérieur, guillemets simples._

Ce n'est que la surface des choses incroyables que vous pouvez faire avec Vim.

#### Je suis un vrai programmeur !

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/v5OtzSjwSu3w4" width="480" height="240" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

Faire partie du voyage d'apprentissage de VIM, c'est s'exposer à la manière dont UNIX fonctionne. Je suis sous l'impression que plus vous vous exposez à des choses comme bash, meilleur programmeur vous serez.

Il y a de fortes chances que vous ayez une configuration de ligne de commande assez sympa. Ne serait-ce pas bien si votre éditeur de code et votre ligne de commande travaillaient en concert ?

#### Comment quitter Vim ?

Il est probable que vous ayez déjà édité un fichier sur un serveur Linux et que vous n'ayez pas su comment quitter le fichier. Disons, par exemple, changer une clé SSH sur Digital Ocean. Si vous connaissez VIM... vous n'avez pas à vous soucier de cela !

#### La vraie raison pour laquelle je suis passé à Vim

Moment d'honnêteté. Le vrai catalyseur pour vouloir passer à Vim a été de regarder Kyle Mathews (créateur de Gatsby.js) l'utiliser pendant une démonstration.

<figure class="kg-card kg-image-card kg-card-hascaption" style="text-align: center;">
    <iframe src="https://giphy.com/embed/UUypRspZCaF94uKasd" width="480" height="269" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    <figcaption>Vous m'avez attrapé.</figcaption>
</figure>

### Fonctionnalités de VS Code et leurs équivalents

Convaincu ? Super, voici quelques outils !

#### Système de plugins

Vim seul est assez basique. Pour ajouter des plugins, nous devons avoir un mécanisme pour les gérer. Voici Plug :

[**junegunn/vim-plug**](https://github.com/junegunn/vim-plug)

> Note : Il existe quelques gestionnaires de plugins. J'ai choisi Plug sans raison particulière. Je l'aime bien et je n'ai eu aucun problème avec. Pour information, Vundle est obsolète.

#### Recherche de fichiers

Il y a eu beaucoup de solutions pour la recherche de fichiers au fil des ans, comme en témoignent les nombreuses réponses dans les forums. J'en ai essayé quelques-unes, mais je suis arrivé à cette combinaison :

[Fuzzy Finder(fzf)](https://github.com/junegunn/fzf) + [Ripgre](https://github.com/BurntSushi/ripgrep)p

![Image](https://www.freecodecamp.org/news/content/images/2019/09/fzf.gif)
_Recherche floue pour "theme"_

Fzf est une recherche floue très bien construite/maintenue qui fonctionne à la fois dans la ligne de commande et dans vim.

> Note : Vous pouvez voir Ag (Silver searcher) dans beaucoup d'articles, cependant le plugin vim lié à Ag n'est plus maintenu, il est donc suggéré d'utiliser RipGrep.

#### Intellisense

Le système d'auto-complétion (Intellisense) dans VSCode est sans doute sa meilleure fonctionnalité. Heureusement pour nous, il a été porté sur Vim !

[**neoclide/coc.nvim**](https://github.com/neoclide/coc.nvim)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/CoC.gif)
_auto-complétion pour importer une fonction écrite dans un autre fichier en React_

CoC a son propre système d'extensions, qui reflète celui de VSCodes. Il est facile à utiliser et bien documenté (la partie la plus importante).

> Note : Vous pouvez voir quelques anciens articles parlant de YouCompleteMe, mais autant que je sache, cela n'est plus maintenu.

#### Explorateur de système de fichiers

VSCode, comme la plupart des éditeurs de texte modernes, vient avec un explorateur de fichiers. Le `netrw` natif de Vim est correct, et j'ai vu plusieurs articles disant que vous n'avez pas besoin d'autre chose, comme [ici](https://shapeshed.com/vim-netrw/). Cependant, je trouve que NERDTree est trop utile pour ne pas l'utiliser.

[**scrooloose/nerdtree**](https://github.com/scrooloose/nerdtree)

#### Intégration Git

Je dois être honnête ici, je fais la plupart de mes trucs git directement dans Iterm. Cependant, VSCode a un incroyable écran divisé Git Diff. Pour obtenir ce niveau d'intégration git, consultez ce plugin :

[**tpope/vim-fugitive**](https://github.com/tpope/vim-fugitive)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/gitdiff.gif)

### Plugins supplémentaires que vous pourriez vouloir

Voici quelques-unes des choses que j'utilisais dans Visual Studio Code et que je voulais apporter dans Vim.

#### Auto-complétion des crochets

Ce petit package sympa fermera automatiquement ces crochets gênants.

[**jiangmiao/auto-pairs**](https://github.com/jiangmiao/auto-pairs)

#### Icônes de fichiers

Cela ajoutera des icônes à des trucs comme NERDTree.

[**ryanoasis/vim-devicons**](https://github.com/ryanoasis/vim-devicons)

#### Prettier

Devinez quoi, mais l'équipe officielle de Prettier a un plugin vim. Trop cool ! Et incroyablement simple à configurer.

[**prettier/vim-prettier**](https://github.com/prettier/vim-prettier)

Faites-le fonctionner sur l'auto-sauvegarde, consultez [cet article](https://www.dailysmarty.com/posts/how-to-setup-prettier-with-vim).

#### Snippets

Devinez quoi, en utilisant le Conquer of Completion, vous pouvez importer des snippets VSCode !

Consultez ceci pour voir comment faire :

[**neoclide/coc.nvim**](https://github.com/neoclide/coc.nvim/wiki/Using-snippets)

Voici le package de snippets React que j'utilise.

[**xabikos/vscode-react**](https://github.com/xabikos/vscode-react)

#### Autres trucs

LE site pour les plugins Vim est Vim Awesome.

[**Vim Awesome**](https://vimawesome.com/)

Un excellent endroit pour regarder les gens utiliser Vim :

[**Vimcasts - Screencasts gratuits sur l'éditeur de texte Vim**](http://vimcasts.org/)

### Dotfiles

J'ai quelques touches remappées pour faciliter les choses. Consultez mes dotfiles pour tout cela.

[**DarthOstrich/dotfiles**](https://github.com/DarthOstrich/dotfiles)

### Réflexions finales

#### Mon parcours

J'utilise uniquement Vim maintenant, après avoir passé environ un an à l'apprendre. Initialement, je l'utilisais uniquement pour mes projets personnels, car mon niveau de productivité était faible. Je devais constamment m'arrêter pour chercher comment faire quelque chose. Cependant, j'ai complètement abandonné VSCode il y a environ 4 mois, et je ne prévois pas de revenir en arrière.

#### Cela demande de la discipline

Apprendre Vim peut sembler intimidant, et franchement, c'est le cas. Cela demande une discipline auto-imposée. Cependant, tout en développement n'est-il pas ainsi ? Il n'y a aucun outil/langage/framework que j'ai appris qui n'a pas demandé un certain niveau de [pratique délibérée](http://www.calnewport.com/blog/2011/12/28/how-i-used-deliberate-practice-to-destroy-my-computer-science-final/).

Vim est un choix de mode de vie. Cela prendra un certain temps pour s'y habituer, et cela SERA frustrant à certains moments. Cependant, si vous persévérez, je garantis que cela améliorera votre flux de travail. Si vous avez des conseils ou des questions supplémentaires, n'hésitez pas à les laisser ci-dessous. Comme toujours, bon codage !

<figure class="kg-card kg-image-card" style="text-align: center;">
    <iframe src="https://giphy.com/embed/hv4TC2Ide8rDoXy0iK" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</figure>

## Ressources supplémentaires pour apprendre

[**Maîtriser Vim rapidement

Jovica Ilic**](https://jovicailic.org/mastering-vim-quickly/)

[**8 astuces Vim qui vous feront passer de débutant à expert**](https://medium.com/swlh/8-vim-tricks-that-will-take-you-from-beginner-to-expert-817ff4870245)

## Références

[**Passer à Vim**](http://brendandawes.com/blog/vim)

[**10 astuces Linux simples qui économisent 50% de mon temps en ligne de commande**](https://dev.to/javinpaul/10-simple-linux-tips-which-save-50-of-my-time-in-the-command-line-4moo)