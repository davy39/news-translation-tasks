---
title: Transformer Vim en un IDE R
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T20:22:52.000Z'
originalURL: https://freecodecamp.org/news/turning-vim-into-an-r-ide-cd9602e8c217
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cRo1ybQbVMMbAHRjgUhXqg.png
tags:
- name: Data Science
  slug: data-science
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Transformer Vim en un IDE R
seo_desc: 'By Kade Killary

  Warning: No, this is not the R setup to use if you are a beginner. The RStudio IDE
  is amazing and should probably always be your default tool. However, if you happen
  to belong to the outcast realms of Vim / Emacs land, then this post ...'
---

Par Kade Killary

_Avertissement_ : **Non**, ce n'est pas la configuration R à utiliser si vous êtes débutant. L'[IDE RStudio](https://www.rstudio.com/products/RStudio/) est incroyable et devrait probablement toujours être votre outil par défaut. Cependant, si vous appartenez aux royaumes marginaux de [Vim](http://www.vim.org/) / [Emacs](https://www.gnu.org/software/emacs/), alors cet article pourrait être pour vous. De plus, je vais mentionner Vim et [Neovim](https://neovim.io/) tout au long de l'article, à ce stade, ils sont largement identiques. Donc, si vous êtes attaché à l'un ou à l'autre, cela ne devrait pas importer.

### Pourquoi ne pas simplement utiliser RStudio ?

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Une excellente question en effet. Pour moi, les principales raisons sont la vitesse et la familiarité. Oui, je sais que RStudio a des raccourcis Vim, mais ce n'est pas la _vraie_ chose. À ce stade, je suis gâté par Vim. Un fou solitaire frappant vigoureusement `<e`sc>`; et` <C-f> dans Microsoft Word pour être déçu.

> Cependant, tout n'est pas perdu.

### R dans Vim

Au début, la recherche de R dans Vim semble être un exercice de brutalisme. Vos options sont peu nombreuses et le support semble sombre.

Votre meilleure option sera d'utiliser un buffer `:terminal` séparé. Le flux de travail de base est le suivant :

* Écrire du code dans `myFile.R`
* Sélectionner visuellement le code
* Coller le code dans le buffer `:terminal`
* Exécuter le code
* Répéter

Cela peut ne pas sembler trop mauvais, cependant, cela devient fastidieux assez rapidement. De plus, cette approche laisse beaucoup à désirer. Principalement, voir ce qui est défini, parcourir les données, et une complétion + linting de base.

### Nvim-R à la rescousse

[Nvim-R](https://github.com/jalvesaq/Nvim-R) est facilement l'un de mes plugins préférés pour Vim. Il prend un vieux pistolet à eau et le transforme en un fusil automatique entièrement fonctionnel. Il est équipé de nombreuses fonctionnalités qui vous feront regretter de ne pas l'avoir utilisé depuis le début. Donc, assez de lyrisme poétique. Plongeons dans la transformation de Vim en notre nouveau foyer R.

La première étape vers l'illumination R est... vous l'avez deviné, installer [Nvim-R](https://github.com/jalvesaq/Nvim-R). J'utilise [Vim-Plug](https://github.com/junegunn/vim-plug), donc c'est ce que je montre ci-dessous. Cependant, vous pouvez tout aussi facilement l'installer en utilisant le gestionnaire de plugins de votre choix.

```
Plug 'jalvesaq/Nvim-R'
```

Maintenant, si vous ouvrez un fichier R et appuyez sur `\rf`, vous verrez un buffer terminal apparaître avec une console R liée à votre session actuelle. Pour le terminer, appuyez sur `\rq`.

![Image](https://cdn-media-1.freecodecamp.org/images/dUyfYbzNF7juie4gwzaDMFl2roeFckvY1naV)
_Fichier R + Console R_

Une chose importante à noter, la console n'est pas liée uniquement au buffer actuel. Cela signifie que vous pouvez avoir plusieurs buffers alimentant tous la même console. Cela peut être bon/mauvais selon vos préférences personnelles. J'apprécie cela, mais cela peut définitivement vous désorienter si vous êtes négligent. Pour une plongée plus profonde sur la façon dont R et Vim communiquent dans Nvim-R, vous pouvez vous rendre [ici](https://github.com/jalvesaq/Nvim-R).

### La sauce secrète

Maintenant que vous avez les bases en place, nous pouvons plonger dans tout ce que Nvim-R a à offrir. Il y a une grande quantité de raccourcis intégrés, pour la liste complète, vous pouvez lire la documentation [ici](https://github.com/jalvesaq/Nvim-R/blob/master/doc/Nvim-R.txt). Je vais brièvement couvrir une poignée de commandes utiles qui vous serviront bien au quotidien.

#### Envoyer des lignes

Le besoin le plus immédiat est de pouvoir envoyer des lignes de code. Il existe plusieurs façons de le faire dans Nvim-R :

* Envoyer :: Fichier entier `\aa`
* Envoyer :: Bloc entier `\bb`
* Envoyer :: Fonction entière `\ff`
* Envoyer :: Sélection entière `\ss`
* Envoyer :: Ligne entière `\l`

Comme vous pouvez commencer à le voir, la barre oblique `\` est le leader pour de nombreuses opérations. Cependant, la plupart de celles-ci, et les distinctions mineures entre elles, sont superflues. Vous serez probablement mieux servi en remappant quelques-unes d'entre elles.

```
" dans votre .vimrc /init.vim
```

```
 remapping the basic :: send linenmap , <Plug>RDSendLine
```

```
 remapping selection :: send multiple linesvmap , <Plug>RDSendSelection
```

```
 remapping selection :: send multiple lines + echo linesvmap ,e <Plug>RESendSelection
```

J'ai choisi de remapper l'envoi de ligne de base + plusieurs lignes à ma touche virgule. Cela réduit considérablement le nombre de touches que je dois utiliser. De plus, le mappage `,e` me permet de vérifier que les lignes que j'ai envoyées ont été calculées correctement. Pour la plupart, ces trois mappages vous permettront de faire tout ce dont vous avez besoin. Il y en a quelques autres qui valent la peine d'être mentionnés, et qui peuvent ajouter quelque chose à votre flux de travail si vous les remappez.

#### Navigateur d'objets

Premièrement, le navigateur d'objets. Cette fonctionnalité, sollicitée en tapant `\ro`, vous permettra de voir quelles variables et bibliothèques sont actives dans votre environnement actuel.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Les objets peuvent également être vus en tapant `\rl`, ce qui exécutera la fonction `ls()` dans votre console actuelle.

#### Documentation

Afin de mieux comprendre votre code, vous avez quelques options. Depuis Nvim-R, il y en a deux particulièrement notables : `\rh` — aide et `\re` — exemple. Chacune de ces commandes s'ouvrira dans un buffer divisé avec les informations pertinentes.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Une autre option intéressante est le [plugin Dash](https://github.com/rizzatti/dash.vim). Le chemin le plus facile pour l'utiliser est le suivant :

```
 install plugin :: using vim-plugPlug 'rizzatti/dash.vim'
```

```
 remap search keynmap <silent> <leader>d <Plug>DashSearch<CR>
```

Maintenant, lorsque vous cherchez plus d'informations sur un morceau de code R, ou tout autre langage, tout ce que vous avez à faire est de placer votre curseur sur le mot et d'appuyer sur `<leade`r>d. L'application Dash apparaîtra alors avec les informations pertinentes. Vous pouvez également rechercher sur Google et Stack Overflow depuis celle-ci. C'est un excellent outil, surtout pour les utilisateurs de Vim qui utilisent Vim pour une variété de langages.

#### Visualisation des données

Ensuite, obtenir un aperçu rapide de vos données. RStudio dispose d'un visualiseur de données intégré magnifique, qui peut être pratique pour se faire une idée des données. Dans Vim, c'est un peu plus difficile, mais pas impossible.

Nvim-R vous permet de visualiser un cadre de données en utilisant la commande `\rv`. Cela affichera le cadre de données en utilisant X Quartz, sur Mac, ou le [plugin CSV](https://github.com/chrisbra/csv.vim) pour Vim, si vous l'avez installé.

Le plugin CSV offre une multitude de fonctionnalités supplémentaires pour manipuler les données, mais cela dépasse le cadre de cet article. Dans l'ensemble, ma suggestion serait d'utiliser Excel. Bien qu'adoré par beaucoup, il sert de bon visualiseur de données.

### Autres astuces et conseils

Malgré ce que vous pourriez penser, il y a encore plus, et même plus que je ne couvrirai pas. Mais, ces quelques astuces valent définitivement la peine d'être gardées à l'esprit.

#### Sortie de code en ligne

Si vous avez une ligne de code et que vous appuyez sur `\o`, vous verrez la sortie rendue en commentaires dans votre fichier actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/EwV3DlUikbtra6tEpT0LIphRz2ji-XHUY3ai)

#### Fonctions

Au lieu de faire le flux de base de `str()` + `plot()`, etc... Nvim-R permet un flux simplifié.

* summary() :: `\rs`
* plot() :: `\rg`
* args() :: `\ra`
* setwd() :: `\rd`
* print() :: `\rp`
* names() :: `\rn`

#### Flèches

Les flèches peuvent être pénibles à taper. Heureusement, Nvim-R facilite cela en mappant `_` à `&l`t;-. Cela peut, ou non, vous déconcerter complètement. Si vous êtes quelqu'un qui préfère le snake case, alors vous devrez taper le soulignement deux fois afin d'obtenir un soulignement réel, et non une flèche. Cependant, vous pouvez remplacer ce paramètre. Je le trouve utile et je me suis adapté, mais je peux certainement comprendre que d'autres soient agacés.

### Complétion

Souvent, je vois le manque de complétion de code comme une raison majeure pour laquelle les gens sautent Vim. Cette notion est incorrecte. La complétion de code fait très partie de Vim. Pour notre objectif spécifique, à savoir la complétion pour R, il existe, encore une fois, quelques options.

#### Complétion Nvim-R

Nvim-R supporte la complétion de code dès la sortie de la boîte. Vous devrez l'engager manuellement en utilisant `<C-X>`;<C-O> pour un nom d'objet, ou <C-X><C-A> pour un argument de fonction. Pour certaines personnes, ce flux de travail est idéal, mais à l'ère actuelle de l'Intellisense de VS Code, et d'autres options similaires, cela semble maladroit.

#### Ncm-R

[Ncm-R](https://github.com/gaalcaras/ncm-R) est votre meilleur choix pour les complétions au fur et à mesure de la frappe. C'est un package relativement nouveau, mais une addition très bienvenue. Il s'intègre avec Nvim-R pour fournir des complétions asynchrones pour R via [nvim-completion-manager](https://github.com/roxma/nvim-completion-manager).

![Image](https://cdn-media-1.freecodecamp.org/images/nWIAYtf-zxwmjx7tXAJddKOyH1cIbjREXj1s)

Ncm-R fournit des complétions riches pour tous les éléments suivants :

* Objets de l'environnement global R
* Fonctions de tous les packages chargés
* Packages à l'intérieur de `library()` et `require()`
* Jeux de données à l'intérieur de `data()`
* Arguments à l'intérieur des fonctions
* Variables à l'intérieur des pipes `%&g`t;% et ggplo`t`s +

Pour une configuration de base, ajoutez le code ci-dessous à votre fichier de configuration Vim.

```
Plug 'roxma/nvim-completion-manager'Plug 'gaalcaras/ncm-R'
```

```
 Optional: for snippet supportPlug 'sirver/UltiSnips'
```

#### Serveur de langage R

Si vous n'êtes pas familier avec ce qu'est un serveur de langage, rendez-vous [ici](https://github.com/Microsoft/language-server-protocol). Si vous êtes familier, alors [ce projet](https://github.com/REditorSupport/languageserver) pourrait vous intéresser. Il est encore dans ses premiers jours, et largement expérimental, mais il fonctionne et supporte actuellement à la fois la complétion de code et le linting.

### Linting

Dernier mais non des moindres, le linting. La configuration pour un linting de qualité est assez simple. Vous voudrez utiliser [ALE](https://github.com/w0rp/ale), Asynchronous Lint Engine, comme votre pilote. Vous pouvez le configurer dans votre .vimrc comme suit :

```
Plug 'w0rp/ale'
```

Maintenant, tout ce que vous avez à faire est d'installer [lintr](https://github.com/jimhester/lintr). Cela peut être fait en utilisant `install.packages('lintr')`.

Maintenant, la prochaine fois que vous ouvrirez un fichier .R, vous devriez être prêt à partir.

### Conclusion

À ce stade, vous avez une configuration redoutable pour R dans Vim. Il y a certainement plus à faire si vous êtes curieux. Les domaines pour une exploration plus approfondie incluent la lecture de toute la documentation dans les plugins que j'ai liés tout au long de cet article. Vous y trouverez de nombreux conseils et astuces utiles, ainsi que des paramètres utiles. J'espère que cela vous a aidé à vous lancer avec R dans Vim !

[**_Pour plus d'informations sur Vim, rendez-vous sur mon blog !_**](https://kadekillary.work/)

### Section bonus

Bien que je sache que j'ai dit que vous devriez explorer par vous-même, cela ne fait pas de mal de fournir quelques paramètres supplémentaires qui peuvent faciliter votre vie.

```
 settings :: Nvim-R plugin
```

```
 R output is highlighted with current colorschemelet g:rout_follow_colorscheme = 1
```

```
 R commands in R output are highlightedlet g:Rout_more_colors = 1
```