---
title: Comment j'ai rendu la recherche dans tout le projet avec VIM transparente grâce
  à ripgrep
subtitle: ''
author: Rahul gupta
co_authors: []
series: null
date: '2020-06-08T16:57:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-search-project-wide-vim-ripgrep-ack
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/markus-winkler-afW1hht0NSs-unsplash--1-.jpg
tags:
- name: Productivity
  slug: productivity
- name: vim
  slug: vim
seo_title: Comment j'ai rendu la recherche dans tout le projet avec VIM transparente
  grâce à ripgrep
seo_desc: 'Yes, I ditched grep & the_silver_searcher(ag) for ripgrep.

  Whether you''re forced to use VIM at your workplace or you''re a mad VIM fan like
  I am who obsesses about productivity, the project-wide keyword search is a basic
  requirement every developer ne...'
---

Oui, j'ai abandonné grep et the_silver_searcher (ag) pour ripgrep.

Que vous soyez obligé d'utiliser VIM sur votre lieu de travail ou que vous soyez un fanatique de VIM comme moi, obsédé par la productivité, la recherche de mots-clés dans tout le projet est une exigence de base dont tout développeur a besoin dans l'arsenal de son éditeur. Et nous nous attendons à ce qu'elle soit ultra-rapide. ⚡

J'utilise VIM depuis environ 3 ans. Et venant d'un environnement [Sublime](https://www.sublimetext.com/), le besoin de recherche dans tout le projet était essentiel.

[ripgrep](https://github.com/BurntSushi/ripgrep) et [a](https://github.com/mileszs/ack.vim)ck.vim étaient des outils que j'ai adoptés tôt après mes expériences peu satisfaisantes avec grep et the_silver_searcher (ag). Je n'ai pas regardé en arrière depuis.

Cet article est le résultat d'expérimentations avec différents outils de recherche et d'améliorations incrémentielles que j'ai apportées sur une période de temps jusqu'à ce que cela semble parfait.

## Pourquoi ack.vim & ripgrep ?

1. **Rapide** : J'ai travaillé sur des projets Symfony et JavaScript avec des milliers de fichiers et c'est simplement ultra-rapide. Voici une comparaison rapide avec d'autres outils de recherche. 
    Mon critère de vitesse est : "cela ne doit jamais sembler lent". J'ai remarqué une amélioration énorme après être passé de grep, the_silver_searcher et ack.
    
2. **Navigation rapide** : ack.vim s'occupe de remplir la liste Quickfix, ce qui vous permet de naviguer facilement à travers tous ces résultats de recherche dans différents fichiers.
    
3. **Paramètres par défaut sensés** : ripgrep considère par défaut gitignore et ignore automatiquement les fichiers/répertoires cachés et les fichiers binaires.
    

## Aperçu

**ack.vim** est un plugin VIM qui agit comme un wrapper pour rechercher des mots-clés et remplir la liste Quickfix pour naviguer dans les résultats.

**ripgrep (rg)** est un outil en ligne de commande que ack.vim utilisera en interne pour effectuer la recherche réelle dans tout le projet.

## Étapes

### **Étape 1** : Installer ripgrep

Si vous préférez [Homebrew](https://brew.sh/) comme moi, exécutez la commande suivante pour installer rg :

```bash
brew tap burntsushi/ripgrep https://github.com/BurntSushi/ripgrep.git
brew install burntsushi/ripgrep/ripgrep-bin
```

Voici un [script automatisé](https://gist.github.com/PezCoder/72ba0f5eba3ca5dc7271bde1a1fcfe5e) que j'utilise dans le cadre de mes [dotfiles](https://github.com/pezcoder/dotfiles).

Si vous préférez un autre mode d'installation, consultez la section [installation](https://github.com/BurntSushi/ripgrep#installation) officielle de ripgrep.

### **Étape 2** : Installer ack.vim

Pour installer ack.vim en utilisant le gestionnaire de paquets [vim-plug](https://github.com/junegunn/vim-plug), ajoutez ce qui suit dans votre vimrc :

```plaintext
Plug 'mileszs/ack.vim'
```

ou consultez la section [installation](https://github.com/mileszs/ack.vim#installation) de ack.vim.

### **Étape 3** : Configurer ack.vim pour utiliser rg

Ajoutez la configuration suivante dans votre vimrc :

```plaintext
" ack.vim --- {{{

" Utiliser ripgrep pour la recherche ⚡
" Options incluses :
" --vimgrep -> Nécessaire pour analyser correctement la réponse de rg pour ack.vim
" --type-not sql -> Éviter les gros fichiers SQL qui ralentissent la recherche
" --smart-case -> Recherche insensible à la casse si le motif est en minuscules, sensible à la casse sinon
let g:ackprg = 'rg --vimgrep --type-not sql --smart-case'

" Fermer automatiquement la liste Quickfix après avoir pressé '<enter>' sur un élément de la liste
let g:ack_autoclose = 1

" Toute recherche ack vide recherchera le mot sous le curseur
let g:ack_use_cword_for_empty_search = 1

" Ne pas sauter vers la première correspondance
cnoreabbrev Ack Ack!

" Mapper <leader>/ pour être prêt à taper le mot-clé de recherche
nnoremap <Leader>/ :Ack!<Space>
" }}}

" Naviguer dans la liste Quickfix facilement
nnoremap <silent> [q :cprevious<CR>
nnoremap <silent> ]q :cnext<CR>
```

Note : `let g:ackprg` définit la commande que ack.vim exécutera en interne. 
Notez également que nous utilisons `rg` ici avec certaines options. Consultez `man rg` pour modifier les options qui pourraient répondre à vos besoins.

Pour explorer les options de ack.vim, consultez la [documentation](https://github.com/mileszs/ack.vim/blob/master/doc/ack.txt) suivante.

## Utilisation

Maintenant que nous sommes prêts, voici les cas d'utilisation les plus courants :

### Rechercher un mot sous le curseur

*Appuyez sur / suivi de entrée*.  
Puisque nous avons défini `let g:ack_use_cword_for_empty_search = 1`, Ack utilise le mot courant sous le curseur pour la recherche, donc pas besoin de taper ce mot.

### Recherche de mot

*Appuyez sur / suivi du mot (sans guillemets) et entrée.*  
Puisque nous utilisons la casse intelligente avec ripgrep, cela effectuera une recherche insensible à la casse si le mot est entièrement en minuscules, et une recherche sensible à la casse sinon.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-04-at-3.33.02-AM-1.png align="left")

*recherche de mot avec ack.vim*

### Recherche par expression régulière

*Appuyez sur / suivi d'un motif regex entre guillemets et entrée.*

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-04-at-3.38.21-AM.png align="left")

*recherche regex avec ack.vim*

### Navigation dans les résultats

Ack.vim remplit les résultats dans la liste Quickfix, qui s'ouvre comme une fenêtre séparée en bas. Il existe plusieurs façons de naviguer dans la liste des résultats :

* Vous pouvez naviguer dans la liste Quickfix en utilisant `j/k` et appuyer sur `entrée` pour fermer la liste Quickfix. VIM vous emmènera à l'emplacement exact du mot trouvé.
    
* Vous pouvez également utiliser les raccourcis `]q` ou `[q`. VIM déplacera le curseur vers le résultat suivant/précédent et ouvrira le fichier dans un nouveau buffer si nécessaire.  
    Pour fermer la liste Quickfix une fois que vous avez terminé, vous pouvez soit aller dans la fenêtre Quickfix du bas et la fermer, soit simplement exécuter `:cclose`
    
* Pour rouvrir la liste Quickfix, exécutez `:copen`
    

## Note de clôture

Et voilà, une recherche et une navigation transparentes pour votre prochaine recherche de mots-clés dans tout le projet !

Si vous êtes bloqué quelque part, consultez les documentations ou les problèmes respectifs de ack.vim et ripgrep dans leurs dépôts respectifs, ou envoyez-moi un message. Partagez la configuration dont vous êtes fier, afin qu'elle puisse aider les autres à améliorer la leur.

Voici mes [dotfiles](https://github.com/pezcoder/dotfiles).