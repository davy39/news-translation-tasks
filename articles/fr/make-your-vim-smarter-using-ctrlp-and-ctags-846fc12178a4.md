---
title: Rendez Votre Vim Plus Intelligent avec Ctrlp et Ctags
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-09T21:59:53.000Z'
originalURL: https://freecodecamp.org/news/make-your-vim-smarter-using-ctrlp-and-ctags-846fc12178a4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-DMqWWZ_btpEiyNgKpc8NQ.gif
tags:
- name: Ctrlp
  slug: ctrlp
- name: ctags
  slug: ctags
- name: JavaScript
  slug: javascript
- name: Software Engineering
  slug: software-engineering
- name: vim
  slug: vim
seo_title: Rendez Votre Vim Plus Intelligent avec Ctrlp et Ctags
seo_desc: 'By _haochuan

  I absolutely love Vim, and I use Vim for all my coding and writing from year to
  year. Although more are more people, especially for those are working with JavaScript,
  prefer modern code editors such as Sublime Text or VSCode, I’d rather ...'
---

Par _haochuan

J'adore absolument Vim, et j'utilise Vim pour tout mon codage et mon écriture d'année en année. Bien que de plus en plus de personnes, surtout celles qui travaillent avec JavaScript, préfèrent les éditeurs de code modernes comme Sublime Text ou VSCode, je préfère passer un peu de temps à essayer de rendre mon jouet plus intelligent.

### [CtrlP](https://github.com/ctrlpvim/ctrlp.vim)

Si vous êtes un utilisateur de Sublime Text, Atom ou VSCode, vous devez utiliser `ctrl + p` des milliers de fois pour améliorer votre productivité. Eh bien, ne soyez pas jaloux si vous êtes un utilisateur de Vim, car ce plugin Vim fantastique, CtrlP, vous donnera tout ce dont vous avez besoin. 
Consultez cette [documentation officielle](http://ctrlpvim.github.io/ctrlp.vim/) pour l'installation et la configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/xakiKSsq2OC4UyFPHEszv9x5Qr96KNHcbRXy)

### [Ctags](http://ctags.sourceforge.net/)

Ctags est un outil qui va parcourir votre code, indexant les méthodes, les classes, les variables et autres identifiants, stockant l'index dans un fichier de tags. Le fichier de tags contient un seul tag par ligne. Selon les arguments de la ligne de commande et le langage contre lequel ctags est exécuté, beaucoup d'informations peuvent être obtenues à partir de cet index.

Ctags prend actuellement en charge [41 langages de programmation](http://ctags.sourceforge.net/languages.html), et il est relativement facile d'ajouter des définitions pour d'autres.

Ctags facilite grandement la navigation dans un projet plus grand, en particulier si le code avec lequel vous travaillez est peu familier. Si vous n'êtes pas sûr de ce que fait une méthode ou de la manière dont elle est censée être appelée, vous pouvez sauter directement à sa définition. Si vous êtes dans la spirale descendante d'un script Perl de 500+ lignes et que vous voulez savoir où une variable a été définie il y a trois heures, vous pouvez revenir directement à cet endroit. Et ensuite, vous pouvez revenir directement à l'endroit où vous travailliez.

Vous pouvez installer Ctags en utilisant Homebrew dans OSX :

```bash
brew install ctags
```

Veuillez noter que OS X est livré avec un exécutable Ctags, mais ce n'est pas exuberant-Ctags et il manque la plupart des fonctionnalités utiles. Si vous voyez une erreur comme `Invalid Parameter` lorsque vous exécutez `ctags`, cela signifie que le système n'utilise pas celui que vous avez installé avec Homebrew. Pour résoudre ce problème :

```bash
$ alias ctags="`brew --prefix`/bin/ctags"
```

Lorsque vous êtes dans le répertoire que vous souhaitez indexer, exécutez simplement :

```bash
ctags -R.
```

Ctags parcourra le répertoire de manière récursive, en taguant tous les fichiers sources qu'il rencontre. Pour des projets très grands, cela peut prendre un certain temps, mais normalement c'est assez rapide.

Vous pourriez également avoir besoin de quelques configurations supplémentaires pour Ctags, voici le `~/.ctags` que j'utilise :

```
--langmap=javascript:.js.es6.es.jsx
--javascript-kinds=-c-f-m-p-v

--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([A-Za-z0-9_$]+)[ \t]*=[ \t]*\[/\2/A,Array,Arrays/

--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([A-Z][A-Za-z0-9_$]+)[ \t]*=[ \t]*function/\2/C,Class,Classes/
--regex-javascript=/^[ \t]*class[ \t]+([A-Za-z0-9_$]+)/\1/C,Class,Classes/

--regex-javascript=/^[ \t]*export[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\3/E,Export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\5/E,export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\7/E,Export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?(var|let|const)[ \t]+([A_Za-z0-9_$]+)/\2/E,Export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?(var|let|const)[ \t]+([A_Za-z0-9_$]+)[ \t]*[^,]+,[ \t]*([A_Za-z0-9_$]+)/\3/E,Export,Exports/
--regex-javascript=/^[ \t]*export[ \t]?(var|let|const)[ \t]+([A_Za-z0-9_$]+)[ \t]*[^,]+,[ \t]*([A_Za-z0-9_$]+)[ \t]*[^,]+,[ \t]*([A_Za-z0-9_$]+)/\4/E,Export,Exports/

--regex-javascript=/^[ \t]*function[ \t]*([A-Za-z0-9_$]+)[ \t\(]/\1/F,Function,Functions/
--regex-javascript=/^[ \t]*[\(]function[ \t]*([A-Za-z0-9_$]+)[ \t\(]/\1/F,Function,Functions/
--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([a-z][A-Za-z0-9_$]+)[ \t]*=[ \t]*function[^\*][^\*]/\2/F,Function,Functions/
--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([a-z][A-Za-z0-9_$]+)[ \t]*=[ \t]*\([^\*]/\2/F,Function,Functions/

--regex-javascript=/^[ \t]*function[ \t]*\*[ \t]*([A-Za-z0-9_$]+)/\1/G,Generator,Generators/
--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([a-z][A-Za-z0-9_$]+)[ \t]*=[ \t]*function([ \t]*\*)/\2/G,Generator,Genrators/
--regex-javascript=/^[ \t]*(\*[ \t])([A-Za-z0-9_$]+)[ \t]*\(.*\)[ \t]*{/\2/G,Generator,Generators/

--regex-javascript=/^[ \t]*import[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\3/I,Import,Imports/
--regex-javascript=/^[ \t]*import[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\5/I,Import,Imports/
--regex-javascript=/^[ \t]*import[ \t]?({[ \t]*)*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])*([A-Za-z0-9_]+),[ \t]*([A-Za-z0-9_\*]*[ \t]as[ \t])([A-Za-z0-9_]+)/\7/I,Import,Imports/

--regex-javascript=/^[ \t]*this\.([A-Za-z0-9_$]+)[ \t]*=.*{$/\1/M,Method,Methods/
--regex-javascript=/^[ \t]*([A-Za-z0-9_$]+)[ \t]*[:=][ \t]*[\(]*function[ \t]*\(/\1/M,Method,Methods/
--regex-javascript=/^[ \t]*static[ \t]+([A-Za-z0-9_$]+)[ \t]*\(/\1/M,Method,Methods/
--regex-javascript=/^[ \t]*([A-Za-z0-9_$]+)\(.*\)[ \t]*{/\1/M,Method,Methods/

--regex-javascript=/^[ \t]*(this\.)*([A-Za-z0-9_$]+)[ \t]*[:=].*[,;]*[^{]$/\2/P,Property,Properties/

--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([A-Za-z0-9_$]+)[ \t]*=[ \t]*{/\2/O,Object,Objects/

--regex-javascript=/\/\/[ \t]*(FIXME|TODO|BUG|NOBUG|\?\?\?|\!\!\!|HACK|XXX)[ \t]*\:*(.*)/\1/T,Tag,Tags/

--regex-javascript=/^[ \t]*(var|let|const)[ \t]+([A-Za-z0-9_$]+)[ \t]*=[ \t]*[^\[{]*;$/\2/V,Variable,Variables/

--exclude=min
--exclude=vendor
--exclude=\*.min.\*
--exclude=\*.map
--exclude=\*.swp
--exclude=\*.bak
--exclude=tags
--exclude=node_modules
--exclude=bower_components
--exclude=test
--exclude=__test__
--exclude=build
--exclude=dist
--exclude=*.bundle.*
```

Voici à quoi cela ressemble lorsque vous allez à la définition d'une fonction :

![Image](https://cdn-media-1.freecodecamp.org/images/DSIuLEu-PDITYUoQVBxz7UJAklOA5DBgKKKO)

Vous pouvez également utiliser Ctrlp pour rechercher des tags au lieu de fichiers. Pour ce faire, vous devez d'abord mapper un raccourci dans votre `.vimrc` :

```
nnoremap <leader>. :CtrlPTag<cr>
```

Voici comment cela fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/4RHDaqFDwqBHZSKKegGHckqoSlAa6eBJ0bkz)

J'espère que cela aide :)

J'écris du code pour l'audio et le web, et je joue de la guitare sur YouTube. Si vous voulez voir plus de choses de ma part ou en savoir plus sur moi, vous pouvez toujours me trouver sur :

Site web :  
[https://haochuan.io/](https://haochuan.io/)

GitHub :  
[https://github.com/haochuan](https://github.com/haochuan)

Medium :  
[https://medium.com/@haochuan](https://medium.com/@haochuan)

YouTube : [https://www.youtube.com/channel/UCNESazgvF_NtDAOJrJMNw0g](https://www.youtube.com/channel/UCNESazgvF_NtDAOJrJMNw0g)