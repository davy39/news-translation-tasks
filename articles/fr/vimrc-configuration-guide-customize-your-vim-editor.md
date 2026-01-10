---
title: Guide de configuration Vimrc - Comment personnaliser votre éditeur de code Vim avec des mappages, Vimscript, la ligne d'état, et plus encore
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-02T20:44:22.000Z'
originalURL: https://freecodecamp.org/news/vimrc-configuration-guide-customize-your-vim-editor
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/cover_image.png
tags:
- name: editor
  slug: editor
- name: Productivité
  slug: productivite
- name: 'développement personnel '
  slug: developpement-personnel
- name: vim
  slug: vim
seo_title: null
seo_desc: 'Par Brandon Wallace

  Configurer votre fichier .vimrc vous permet d''utiliser toute la puissance de Vim. Avec un fichier .vimrc personnalisé, vous pouvez décupler vos pouvoirs Vim.

  Dans cet article, je vais vous montrer quelques façons de personnaliser votre fichier .vimrc.

  Je vais aborder :...'
---

Par Brandon Wallace

Configurer votre fichier .vimrc vous permet d'utiliser toute la puissance de Vim. Avec un fichier .vimrc personnalisé, vous pouvez décupler vos pouvoirs Vim.

Dans cet article, je vais vous montrer quelques façons de personnaliser votre fichier .vimrc.

Je vais aborder :

* Les paramètres de base
* Les plugins
* Le repliage (Folding)
* Vimscript
* La ligne d'état (Status line)

Tout d'abord, créez la structure de répertoires suivante dans votre répertoire personnel (home).

```bash
.vim/
 ├── autoload/
 ├── backup/
 ├── colors/
 └── plugged/
```

```bash
$ mkdir -p ~/.vim ~/.vim/autoload ~/.vim/backup ~/.vim/colors ~/.vim/plugged
```

Créez un fichier .vimrc dans votre répertoire personnel.

```bash
$ touch ~/.vimrc

```

# Comment mettre à jour les paramètres de base dans Vim

Commençons par ajouter quelques paramètres de base qui amélioreront votre expérience d'édition. J'utilise des guillemets doubles pour commenter les lignes.

Ajoutez les lignes suivantes à votre fichier .vimrc :

```vimrc
" Désactiver la compatibilité avec vi qui peut causer des problèmes inattendus.
set nocompatible

" Activer la détection du type de fichier. Vim sera capable d'essayer de détecter le type de fichier utilisé.
filetype on

" Activer les plugins et charger le plugin pour le type de fichier détecté.
filetype plugin on

" Charger un fichier d'indentation pour le type de fichier détecté.
filetype indent on
```

La coloration syntaxique est très utile. La ligne suivante que nous ajoutons activera la coloration syntaxique et rendra votre code plus facile à lire.

```vimrc
" Activer la coloration syntaxique.
syntax on

```

### Voici à quoi cela ressemble avant :

![vim-no-highlighting.png](https://www.freecodecamp.org/news/content/images/2021/05/vim_no_highlighting.png)

### Et après :

![vim-highlighting.png](https://www.freecodecamp.org/news/content/images/2021/05/vim_highlighting.png)

Vous pouvez également choisir d'afficher les numéros de ligne pour faciliter la navigation dans le fichier.

```vimrc
" Ajouter des numéros à chaque ligne sur le côté gauche.
set number

```

![set-numbers.png](https://www.freecodecamp.org/news/content/images/2021/05/set_numbers.png)

Vous pouvez repérer exactement où se trouve le curseur en mettant en surbrillance la ligne sur laquelle il se trouve horizontalement et verticalement.

Ajoutez ces lignes pour activer cette fonctionnalité.

```vimrc
" Mettre en surbrillance la ligne du curseur horizontalement.
set cursorline

" Mettre en surbrillance la colonne du curseur verticalement.
set cursorcolumn

```

![set-cursor-line-column.png](https://www.freecodecamp.org/news/content/images/2021/05/set_cursor-line-column-1.png)

Voici d'autres paramètres courants qui améliorent l'expérience d'édition.
Chaque ligne contient un commentaire au-dessus expliquant ce qu'elle fait.

Ajoutez les lignes suivantes au fichier .vimrc.

```vimrc
" Définir la largeur de décalage (shift width) à 4 espaces.
set shiftwidth=4

" Définir la largeur de tabulation à 4 colonnes.
set tabstop=4

" Utiliser des caractères d'espace au lieu des tabulations.
set expandtab

" Ne pas enregistrer de fichiers de sauvegarde.
set nobackup

" Ne pas laisser le curseur défiler au-dessous ou au-dessus de N lignes lors du défilement.
set scrolloff=10

" Ne pas revenir à la ligne automatiquement. Permettre aux longues lignes de s'étendre aussi loin que nécessaire.
set nowrap

" Lors de la recherche dans un fichier, mettre en surbrillance incrémentale les caractères correspondants au fur et à mesure de la frappe.
set incsearch

" Ignorer les majuscules lors de la recherche.
set ignorecase

" Outrepasser l'option ignorecase si la recherche contient des majuscules.
" Cela vous permettra de rechercher spécifiquement des lettres majuscules.
set smartcase

" Afficher la commande partielle que vous tapez sur la dernière ligne de l'écran.
set showcmd

" Afficher le mode dans lequel vous êtes sur la dernière ligne.
set showmode

" Afficher les mots correspondants lors d'une recherche.
set showmatch

" Utiliser la mise en surbrillance lors d'une recherche.
set hlsearch

" Définir le nombre de commandes à enregistrer dans l'historique (par défaut 20).
set history=1000
```

La complétion Bash est une fonctionnalité géniale qui économise des frappes en complétant automatiquement ce que vous tapez. Vim possède une fonctionnalité similaire appelée wildmenu.

Ajoutez les lignes suivantes pour activer la fonctionnalité wildmenu. Vous verrez une liste de fichiers correspondant à celui que vous recherchez. Vous pouvez également activer l'auto-complétion dans Vim.

```vimrc
" Activer le menu d'auto-complétion après avoir appuyé sur TAB.
set wildmenu

" Faire en sorte que wildmenu se comporte comme la complétion Bash.
set wildmode=list:longest

" Il y a certains fichiers que nous ne voudrions jamais éditer avec Vim.
" Wildmenu ignorera les fichiers avec ces extensions.
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx

```

![vim-wildmenu.gif](https://www.freecodecamp.org/news/content/images/2021/05/vim_wildmenu.gif)

Tapez `:help <command>` pour plus d'informations sur des commandes spécifiques.

Exemple :

```
:help nocompatible

```

# Comment replier les longs fichiers dans Vim

Le fichier .vimrc peut devenir long, donc l'organiser en sections est une idée judicieuse.
Vim vous permettra de replier (fold) les longs fichiers pour masquer des sections de texte.

Ajoutez les lignes suivantes au bas de votre .vimrc pour organiser le fichier en sections.

```vimrc
" PLUGINS ---------------------------------------------------------------- {{{

" Le code du plugin va ici.

" }}}


" MAPPINGS --------------------------------------------------------------- {{{

" Le code des mappages va ici.

" }}}


" VIMSCRIPT -------------------------------------------------------------- {{{

" Ceci activera le repliage de code.
" Utiliser la méthode de repliage par marqueur.
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END

" Plus de code Vimscript va ici.

" }}}


" STATUS LINE ------------------------------------------------------------ {{{

" Le code de la barre d'état va ici.

" }}}
```

Enregistrez le fichier .vimrc avec `:w` et sourcez le fichier .vimrc comme ceci `:source ~/.vimrc` pour que les changements prennent effet. Maintenant, une fois que vous déplacez votre curseur sur un repli, vous pouvez appuyer sur :

`zo` pour ouvrir un seul repli sous le curseur.

`zc` pour fermer le repli sous le curseur.

`zR` pour ouvrir tous les replis.

`zM` pour fermer tous les replis.

![vim-open-close-fold.gif](https://www.freecodecamp.org/news/content/images/2021/05/vim_open_close_fold.gif)

Tapez `:help folding` pour plus d'informations.

# Comment ajouter des plugins à Vim

Vous pouvez ajouter des plugins à Vim pour ajouter des fonctionnalités supplémentaires. La plupart des gens utilisent un gestionnaire de plugins pour faciliter l'installation des plugins.

Il existe une variété de gestionnaires de plugins que nous pouvons utiliser. Je vais vous montrer comment installer et utiliser le gestionnaire de plugins [vim-plug](https://github.com/junegunn/vim-plug).

Pour installer le plugin vim-plug, exécutez cette commande :

Sur Linux ou Mac OS.

```bash
$ curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

Sur Windows avec Powershell.

```powershell
$ iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |`
    ni $HOME/vimfiles/autoload/plug.vim -Force

```

Ajoutez les lignes `call plug#begin('~/.vim/plugged')` et `call plug#end()` dans la section des plugins. Les plugins que nous installons seront ajoutés entre les deux appels de fonction.

```vimrc
" PLUGINS ---------------------------------------------------------------- {{{

call plug#begin('~/.vim/plugged')




call plug#end()

" }}}

```

Maintenant, installer des plugins est aussi simple que d'ajouter la chaîne `Plug 'username/plugin-name'` que vous trouvez sur GitHub entre les appels de fonction.

Voici comment j'installe [NERDTree](https://github.com/preservim/nerdtree) et [Asynchronous Lint Engine (ALE)](https://github.com/dense-analysis/ale).

Ajoutez ces deux lignes entre les deux lignes `call plug#...` :

```vimrc
" PLUGINS ---------------------------------------------------------------- {{{

call plug#begin('~/.vim/plugged')


  Plug 'dense-analysis/ale'

  Plug 'preservim/nerdtree'


call plug#end()

" }}}
```

Enregistrez le fichier .vimrc avec la commande `:w` et sourcez le fichier .vimrc avec cette commande `:source ~/.vimrc` pour que les changements prennent effet.

Maintenant tapez `:PlugInstall` pour télécharger et installer les deux plugins.

![vim-plug-install.png](https://www.freecodecamp.org/news/content/images/2021/05/vim-plug_install.png)

# Comment mapper des raccourcis clavier dans Vim

Dans la section mappage, nous ajouterons des raccourcis pour faciliter la saisie de commandes plus longues. Cela vous économisera des frappes et beaucoup de temps, surtout pour les commandes longues.

La syntaxe de mappage des touches est comme ceci :

`map_mode <ce_que_vous_tapez> <ce_qui_est_exécuté>`

### Modes de mappage populaires dans Vim

Voici quelques modes de mappage populaires et probablement les plus utiles et importants.

* `nnoremap` – Vous permet de mapper des touches en mode normal.
* `inoremap` – Vous permet de mapper des touches en mode insertion.
* `vnoremap` – Vous permet de mapper des touches en mode visuel.

Un exemple de mappage courant est de mapper 'jj' à la touche d'échappement (Esc). Vous allez appuyer souvent sur la touche d'échappement. La touche d'échappement est dans le coin éloigné du clavier.
La lettre 'j' est au milieu du clavier, il est donc plus facile d'appuyer sur 'jj' au lieu d'aller chercher la touche d'échappement.

Voici comment vous mapperiez la touche d'échappement à `jj`.

`inoremap jj <esc>`

### Comment utiliser Mapleader dans Vim

Mapleader vous permettra de définir une touche non utilisée par Vim comme la touche `<leader>`.
La touche leader, en conjonction avec une autre touche, vous permettra de créer de nouveaux raccourcis.

La touche barre oblique inverse (backslash) est la touche leader par défaut, mais certaines personnes la changent pour une virgule `","`.

`let mapleader = "\"`

Avec la touche leader mappée sur la barre oblique inverse, je peux l'utiliser comme ceci :

Désactiver la mise en surbrillance de la recherche en appuyant sur `\\`.
`nnoremap <leader>\ :nohlsearch<CR>`

Voici quelques mappages courants que les gens utilisent. Voir les commentaires au-dessus de chaque ligne pour l'explication.

Ajoutez ce code dans la section des mappages :

```vimrc
" MAPPINGS --------------------------------------------------------------- {{{

" Définir la barre oblique inverse comme touche leader.
let mapleader = "\"

" Appuyez sur \\ pour revenir à la dernière position du curseur.
nnoremap <leader>\ ``

" Appuyez sur \p pour imprimer le fichier actuel sur l'imprimante par défaut depuis un système d'exploitation Linux.
" Voir les imprimantes disponibles :   lpstat -v
" Définir l'imprimante par défaut :    lpoptions -d <nom_imprimante>
" <silent> signifie ne pas afficher la sortie.
nnoremap <silent> <leader>p :%w !lp<CR>

" Tapez jj pour quitter le mode insertion rapidement.
inoremap jj <Esc>

" Appuyez sur la barre d'espace pour taper le caractère : en mode commande.
nnoremap <space> :

" Appuyer sur la lettre o ouvrira une nouvelle ligne sous la ligne actuelle.
" Quitter le mode insertion après avoir créé une nouvelle ligne au-dessus ou au-dessous de la ligne actuelle.
nnoremap o o<esc>
nnoremap O O<esc>

" Centrer le curseur verticalement lors du déplacement vers le mot suivant pendant une recherche.
nnoremap n nzz
nnoremap N Nzz

" Copier (Yank) du curseur jusqu'à la fin de la ligne.
nnoremap Y y$

" Mapper la touche F5 pour exécuter un script Python à l'intérieur de Vim.
" Je mappe F5 à une chaîne de commandes ici.
" :w enregistre le fichier.
" <CR> (retour chariot) est comme appuyer sur la touche entrée.
" !clear exécute la commande externe d'effacement d'écran.
" !python3 % exécute le fichier actuel avec Python.
nnoremap <f5> :w <CR>:!clear <CR>:!python3 % <CR>

" Vous pouvez diviser la fenêtre dans Vim en tapant :split ou :vsplit.
" Naviguez plus facilement dans la vue divisée en appuyant sur CTRL+j, CTRL+k, CTRL+h, ou CTRL+l.
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l

" Redimensionner les fenêtres divisées en utilisant les touches fléchées en appuyant sur :
" CTRL+HAUT, CTRL+BAS, CTRL+GAUCHE, ou CTRL+DROITE.
noremap <c-up> <c-w>+
noremap <c-down> <c-w>-
noremap <c-left> <c-w>>
noremap <c-right> <c-w><

" Mappages spécifiques à NERDTree.
" Mapper la touche F3 pour basculer l'ouverture et la fermeture de NERDTree.
nnoremap <F3> :NERDTreeToggle<cr>

" Faire en sorte que nerdtree ignore certains fichiers et répertoires.
let NERDTreeIgnore=['\.git$', '\.jpg$', '\.mp4$', '\.ogg$', '\.iso$', '\.pdf$', '\.pyc$', '\.odt$', '\.png$', '\.gif$', '\.db$']

" }}}

```

Tapez `help: map-modes` pour plus d'informations.

# Comment ajouter du Vimscript

Vimscript est un langage de script qui vous permet de créer des scripts utilisant des variables, des instructions if else et des fonctions. Les commandes automatiques (autocmd) attendent que des événements se produisent pour déclencher une commande.

```vimrc
" VIMSCRIPT -------------------------------------------------------------- {{{

" Activer la méthode de repliage par marqueur.
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END

" Si le type de fichier actuel est HTML, définir l'indentation à 2 espaces.
autocmd Filetype html setlocal tabstop=2 shiftwidth=2 expandtab

" Si la version de Vim est égale ou supérieure à 7.3, activer undofile.
" Cela vous permet d'annuler les modifications d'un fichier même après l'avoir enregistré.
if version >= 703
    set undodir=~/.vim/backup
    set undofile
    set undoreload=10000
endif

" Vous pouvez diviser une fenêtre en sections en tapant `:split` ou `:vsplit`.
" Afficher cursorline et cursorcolumn UNIQUEMENT dans la fenêtre active.
augroup cursor_off
    autocmd!
    autocmd WinLeave * set nocursorline nocursorcolumn
    autocmd WinEnter * set cursorline cursorcolumn
augroup END

" Si la version GUI de Vim est en cours d'exécution, définir ces options.
if has('gui_running')

    " Définir le ton de l'arrière-plan.
    set background=dark

    " Définir le schéma de couleurs.
    colorscheme molokai

    " Définir une police personnalisée que vous avez installée sur votre ordinateur.
    " Syntaxe : set guifont=<nom_police>\ <poids_police>\ <taille>
    set guifont=Monospace\ Regular\ 12

    " Afficher plus de contenu du fichier par défaut.
    " Masquer la barre d'outils.
    set guioptions-=T

    " Masquer la barre de défilement de gauche.
    set guioptions-=L

    " Masquer la barre de défilement de droite.
    set guioptions-=r

    " Masquer la barre de menu.
    set guioptions-=m

    " Masquer la barre de défilement du bas.
    set guioptions-=b

    " Mapper la touche F4 pour basculer le menu, la barre d'outils et la barre de défilement.
    " <Bar> est le caractère pipe.
    " <CR> est la touche entrée.
    nnoremap <F4> :if &guioptions=~#'mTr'<Bar>
        \set guioptions-=mTr<Bar>
        \else<Bar>
        \set guioptions+=mTr<Bar>
        \endif<CR>

endif

" }}}

```

Lisez [Learn Vimscript the Hard Way](https://learnvimscriptthehardway.stevelosh.com/) pour plus d'informations sur Vimscript.

Tapez `:help autocmd` pour plus d'informations sur les commandes automatiques.

# Comment ajouter des schémas de couleurs à Vim

Vous pouvez facilement ajouter des schémas de couleurs à Vim pour changer les couleurs par défaut. Faites une recherche pour "Vim color schemes" et vous trouverez de très nombreux choix.

Installer un schéma de couleurs est aussi simple que d'ajouter un fichier `<colorscheme>.vim` au répertoire `~/.vim/colors/`.

Je vais ajouter le schéma de couleurs populaire molokai :

```bash
$ cd ~/.vim/colors

$ curl -o molokai.vim https://raw.githubusercontent.com/tomasr/molokai/master/colors/molokai.vim
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  7558  100  7558    0     0   150k      0 --:--:-- --:--:-- --:--:--  150k

```

Pour définir le schéma de couleurs, tapez cette commande :

```vimrc
:colorscheme molokai

```

### Exemples de schémas de couleurs :

![vim_four_colorschemes](https://www.freecodecamp.org/news/content/images/2021/05/vim_four_colorschemes.png)
_schémas de couleurs : molokai, base16-tomorrow, blue, one_

# Comment configurer la barre d'état dans Vim

Vous pouvez configurer votre barre d'état Vim avec des informations utiles. Par exemple, configurer le type de fichier, le nombre total de lignes dans le fichier, le chemin vers le fichier, le numéro de colonne, le numéro de ligne, le pourcentage de progression dans le fichier, et bien plus encore.

Ajoutez ce code dans la section de la ligne d'état :

```vimrc
" STATUS LINE ------------------------------------------------------------ {{{

" Effacer la ligne d'état lorsque vimrc est rechargé.
set statusline=

" Côté gauche de la ligne d'état.
set statusline+=\ %F\ %M\ %Y\ %R

" Utiliser un séparateur pour séparer le côté gauche du côté droit.
set statusline+=%=

" Côté droit de la ligne d'état.
set statusline+=\ ascii:\ %b\ hex:\ 0x%B\ row:\ %l\ col:\ %c\ percent:\ %p%%

" Afficher l'état sur l'avant-dernière ligne.
set laststatus=2

" }}}

```

`%F` – Affiche le chemin complet du fichier actuel.

`%M` – Indicateur de modification, montre si le fichier n'est pas enregistré.

`%Y` – Type de fichier dans le tampon (buffer).

`%R` – Affiche l'indicateur de lecture seule.

`%b` – Affiche le caractère ASCII/Unicode sous le curseur.

`0x%B` – Affiche le caractère hexadécimal sous le curseur.

`%l` – Affiche le numéro de ligne.

`%c` – Affiche le numéro de colonne.

`%p%%` – Affiche le pourcentage du curseur par rapport au haut du fichier.

![vim_statusline](https://www.freecodecamp.org/news/content/images/2021/05/vim_statusline.png)

Tapez `help: statusline` pour plus d'informations.

Voici le fichier .vimrc complet.

```vimrc
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""               
"               
"               ██╗   ██╗██╗███╗   ███╗██████╗  ██████╗
"               ██║   ██║██║████╗ ████║██╔══██╗██╔════╝
"               ██║   ██║██║██╔████╔██║██████╔╝██║     
"               ╚██╗ ██╔╝██║██║╚██╔╝██║██╔══██╗██║     
"                ╚████╔╝ ██║██║ ╚═╝ ██║██║  ██║╚██████╗
"                 ╚═══╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝
"               
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""               

" Désactiver la compatibilité avec vi qui peut causer des problèmes inattendus.
set nocompatible

" Activer la détection du type de fichier. Vim sera capable d'essayer de détecter le type de fichier utilisé.
filetype on

" Activer les plugins et charger le plugin pour le type de fichier détecté.
filetype plugin on

" Charger un fichier d'indentation pour le type de fichier détecté.
filetype indent on

" Activer la coloration syntaxique.
syntax on

" Ajouter des numéros au fichier.
set number

" Mettre en surbrillance la ligne du curseur horizontalement.
set cursorline

" Mettre en surbrillance la colonne du curseur verticalement.
set cursorcolumn

" Définir la largeur de décalage à 4 espaces.
set shiftwidth=4

" Définir la largeur de tabulation à 4 colonnes.
set tabstop=4

" Utiliser des caractères d'espace au lieu des tabulations.
set expandtab

" Ne pas enregistrer de fichiers de sauvegarde.
set nobackup

" Ne pas laisser le curseur défiler au-dessous ou au-dessus de N lignes lors du défilement.
set scrolloff=10

" Ne pas revenir à la ligne automatiquement. Permettre aux longues lignes de s'étendre aussi loin que nécessaire.
set nowrap

" Lors de la recherche dans un fichier, mettre en surbrillance incrémentale les caractères correspondants au fur et à mesure de la frappe.
set incsearch

" Ignorer les majuscules lors de la recherche.
set ignorecase

" Outrepasser l'option ignorecase si la recherche contient des majuscules.
" Cela vous permettra de rechercher spécifiquement des lettres majuscules.
set smartcase

" Afficher la commande partielle que vous tapez sur la dernière ligne de l'écran.
set showcmd

" Afficher le mode dans lequel vous êtes sur la dernière ligne.
set showmode

" Afficher les mots correspondants lors d'une recherche.
set showmatch

" Utiliser la mise en surbrillance lors d'une recherche.
set hlsearch

" Définir le nombre de commandes à enregistrer dans l'historique (par défaut 20).
set history=1000

" Activer le menu d'auto-complétion après avoir appuyé sur TAB.
set wildmenu

" Faire en sorte que wildmenu se comporte comme la complétion Bash.
set wildmode=list:longest

" Il y a certains fichiers que nous ne voudrions jamais éditer avec Vim.
" Wildmenu ignorera les fichiers avec ces extensions.
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx

" PLUGINS ---------------------------------------------------------------- {{{

call plug#begin('~/.vim/plugged')

  Plug 'dense-analysis/ale'

  Plug 'preservim/nerdtree'

call plug#end()

" }}}

" MAPPINGS --------------------------------------------------------------- {{{

" Définir la barre oblique inverse comme touche leader.
let mapleader = "\"

" Appuyez sur \\ pour revenir à la dernière position du curseur.
nnoremap <leader>\ ``

" Appuyez sur \p pour imprimer le fichier actuel sur l'imprimante par défaut depuis un système d'exploitation Linux.
" Voir les imprimantes disponibles :   lpstat -v
" Définir l'imprimante par défaut :    lpoptions -d <nom_imprimante>
" <silent> signifie ne pas afficher la sortie.
nnoremap <silent> <leader>p :%w !lp<CR>

" Tapez jj pour quitter le mode insertion rapidement.
inoremap jj <Esc>

" Appuyez sur la barre d'espace pour taper le caractère : en mode commande.
nnoremap <space> :

" Appuyer sur la lettre o ouvrira une nouvelle ligne sous la ligne actuelle.
" Quitter le mode insertion après avoir créé une nouvelle ligne au-dessus ou au-dessous de la ligne actuelle.
nnoremap o o<esc>
nnoremap O O<esc>

" Centrer le curseur verticalement lors du déplacement vers le mot suivant pendant une recherche.
nnoremap n nzz
nnoremap N Nzz

" Copier (Yank) du curseur jusqu'à la fin de la ligne.
nnoremap Y y$

" Mapper la touche F5 pour exécuter un script Python à l'intérieur de Vim.
" Nous mappons F5 à une chaîne de commandes ici.
" :w enregistre le fichier.
" <CR> (retour chariot) est comme appuyer sur la touche entrée.
" !clear exécute la commande externe d'effacement d'écran.
" !python3 % exécute le fichier actuel avec Python.
nnoremap <f5> :w <CR>:!clear <CR>:!python3 % <CR>

" Vous pouvez diviser la fenêtre dans Vim en tapant :split ou :vsplit.
" Naviguez plus facilement dans la vue divisée en appuyant sur CTRL+j, CTRL+k, CTRL+h, ou CTRL+l.
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l

" Redimensionner les fenêtres divisées en utilisant les touches fléchées en appuyant sur :
" CTRL+HAUT, CTRL+BAS, CTRL+GAUCHE, ou CTRL+DROITE.
noremap <c-up> <c-w>+
noremap <c-down> <c-w>-
noremap <c-left> <c-w>>
noremap <c-right> <c-w><

" Mappages spécifiques à NERDTree.
" Mapper la touche F3 pour basculer l'ouverture et la fermeture de NERDTree.
nnoremap <F3> :NERDTreeToggle<cr>

" Faire en sorte que nerdtree ignore certains fichiers et répertoires.
let NERDTreeIgnore=['\.git$', '\.jpg$', '\.mp4$', '\.ogg$', '\.iso$', '\.pdf$', '\.pyc$', '\.odt$', '\.png$', '\.gif$', '\.db$']

" }}}

" VIMSCRIPT -------------------------------------------------------------- {{{

" Activer la méthode de repliage par marqueur.
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END

" Si le type de fichier actuel est HTML, définir l'indentation à 2 espaces.
autocmd Filetype html setlocal tabstop=2 shiftwidth=2 expandtab

" Si la version de Vim est égale ou supérieure à 7.3, activer undofile.
" Cela vous permet d'annuler les modifications d'un fichier même après l'avoir enregistré.
if version >= 703
    set undodir=~/.vim/backup
    set undofile
    set undoreload=10000
endif

" Vous pouvez diviser une fenêtre en sections en tapant `:split` ou `:vsplit`.
" Afficher cursorline et cursorcolumn UNIQUEMENT dans la fenêtre active.
augroup cursor_off
    autocmd!
    autocmd WinLeave * set nocursorline nocursorcolumn
    autocmd WinEnter * set cursorline cursorcolumn
augroup END

" Si la version GUI de Vim est en cours d'exécution, définir ces options.
if has('gui_running')

    " Définir le ton de l'arrière-plan.
    set background=dark

    " Définir le schéma de couleurs.
    colorscheme molokai

    " Définir une police personnalisée que vous avez installée sur votre ordinateur.
    " Syntaxe : <nom_police>\ <poids>\ <taille>
    set guifont=Monospace\ Regular\ 12

    " Afficher plus de contenu du fichier par défaut.
    " Masquer la barre d'outils.
    set guioptions-=T

    " Masquer la barre de défilement de gauche.
    set guioptions-=L

    " Masquer la barre de défilement de gauche.
    set guioptions-=r

    " Masquer la barre de menu.
    set guioptions-=m

    " Masquer la barre de défilement du bas.
    set guioptions-=b

    " Mapper la touche F4 pour basculer le menu, la barre d'outils et la barre de défilement.
    " <Bar> est le caractère pipe.
    " <CR> est la touche entrée.
    nnoremap <F4> :if &guioptions=~#'mTr'<Bar>
        \set guioptions-=mTr<Bar>
        \else<Bar>
        \set guioptions+=mTr<Bar>
        \endif<CR>

endif

" }}}

" STATUS LINE ------------------------------------------------------------ {{{

" Effacer la ligne d'état lorsque vimrc est rechargé.
set statusline=

" Côté gauche de la ligne d'état.
set statusline+=\ %F\ %M\ %Y\ %R

" Utiliser un séparateur pour séparer le côté gauche du côté droit.
set statusline+=%=

" Côté droit de la ligne d'état.
"set statusline+=\ ascii:\ %b\ hex:\ 0x%B\ row:\ %l\ col:\ %c\ percent:\ %p%%

" Afficher l'état sur l'avant-dernière ligne.
set laststatus=2

" }}}
```

# Conclusion

Dans cet article, je n'ai fait qu'effleurer la surface de la façon dont vous pouvez personnaliser Vim.
Il existe des milliers de façons de configurer et de personnaliser un .vimrc à votre goût.
Vous pouvez même écrire vos propres plugins et schémas de couleurs et les partager avec le monde.

J'espère que vous avez appris une nouvelle astuce ou deux en lisant cet article. Alors si vous utilisez Vim, ne partez pas sans un fichier .vimrc !

Au fait, j'ai utilisé Vim pour écrire cet article.

Suivez-moi sur [Github](https://github.com/brandon-wallace) | [DEV.to](https://dev.to/brandonwallace)