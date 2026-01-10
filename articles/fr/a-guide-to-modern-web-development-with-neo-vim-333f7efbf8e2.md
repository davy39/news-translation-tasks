---
title: Un guide pour le développement Web moderne avec (Neo)vim
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T16:25:42.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-modern-web-development-with-neo-vim-333f7efbf8e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VwtBkUpu7nSToAEP8N2IOQ.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: vim
  slug: vim
- name: Web Development
  slug: web-development
seo_title: Un guide pour le développement Web moderne avec (Neo)vim
seo_desc: 'By Caleb Taylor

  There are a lot of great editors out there that provide a ton of features for web
  development. Recreating those features in Vim has always been a challenge. I love
  Vim, but I’ve also dedicated a ton of time to tweaking my setup. This ...'
---

Par Caleb Taylor

Il existe de nombreux éditeurs excellents qui offrent une tonne de fonctionnalités pour le développement web. Reproduire ces fonctionnalités dans Vim a toujours été un défi. J'adore Vim, mais j'ai également consacré un **_énorme_** temps à ajuster ma configuration. Cet article est un résumé du résultat de mon travail.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VwtBkUpu7nSToAEP8N2IOQ.png)
_Jarvis en action_

J'utilise [coc.nvim](https://github.com/neoclide/coc.nvim) et [denite](https://github.com/Shougo/denite.nvim) pour alimenter mon expérience de codage. Denite est utilisé pour trouver des fichiers de manière floue, gérer les fichiers ouverts et rechercher dans votre projet. Coc.nvim alimente le moteur [intellisense](https://docs.microsoft.com/en-us/visualstudio/ide/using-intellisense?view=vs-2019) en enveloppant de nombreuses extensions principales qui alimentent l'IDE [VSCode](https://code.visualstudio.com/). Pour ma configuration complète, y compris comment je configure ces plugins et plus, consultez [mes dotfiles](https://github.com/ctaylo21/jarvis).

> **Note** : Je vais simplement référencer Vim dans cet article, mais j'utilise en réalité [Neovim](https://neovim.io/). Les plugins fonctionnent tous avec Vim également — selon la version — mais des fonctionnalités comme la fenêtre flottante seront spécifiques à Neovim.

### **Introduction**

J'écris du TypeScript/JavaScript quotidiennement, et je sais à quel point la différence est marquée entre Vim et un éditeur comme VSCode dès l'installation. Il existe de nombreuses fonctionnalités disponibles dans les éditeurs modernes qui prennent du temps, de l'expertise et/ou des plugins pour être réalisées dans Vim.

J'ai créé la liste suivante de fonctionnalités que j'attends d'un éditeur moderne. Les fonctionnalités standard des éditeurs (comme la coloration syntaxique) ne sont pas incluses.

1. **Recherche floue de fichiers** — Si vous connaissez le nom du fichier dans le projet, vous devriez pouvoir l'ouvrir rapidement (comme — deux touches + nombre minimum de caractères pour un nom de fichier unique).
2. **Changement de fichier** — Vous devriez pouvoir voir les fichiers ouverts et basculer rapidement entre les fichiers ouverts, à la fois avec une recherche floue et une navigation manuelle.
3. **Linting** — Le linting du code doit être automatique et rapide, et vous devriez pouvoir utiliser un correcteur de code.
4. **Recherche dans le projet** — Vous devriez pouvoir rechercher une chaîne arbitraire, rechercher un symbole, trouver des définitions et trouver les utilisations d'un symbole.
5. **Intellisense de code** — Avoir votre IDE fournir des suggestions et des auto-complétions pertinentes et transparentes peut être un énorme gain de productivité. À mon avis, le « grand blanc » pour la plupart des utilisateurs de Vim.

Obtenir toutes ces fonctionnalités dans Vim peut être un casse-tête. Il existe des tonnes de plugins parmi lesquels choisir, des configurations à ajuster et des documentations à lire. Après 7 ans d'essais et d'erreurs, j'ai enfin réussi à configurer mon environnement de manière optimale. La meilleure partie ?

**Je vais vous montrer comment obtenir toutes les fonctionnalités de base avec seulement deux plugins.**

Je ne vais pas couvrir toutes les fonctionnalités de ces plugins incroyables, ni lister toutes les alternatives possibles (et il y en a beaucoup de bonnes). Je vais me concentrer sur la mise en avant des fonctionnalités principales que j'utilise, ainsi que sur les mappings ou configurations que j'utilise pour améliorer l'expérience.

Alors sans plus attendre, commençons.

### **Denite**

**Ce que vous obtenez** : Recherche floue de fichiers, gestion des fichiers, recherche dans le projet

Je ne vais pas mentir, [Denite](https://github.com/Shougo/denite.nvim) est assez incroyable. Il suffit de jeter un œil à [la documentation](https://github.com/Shougo/denite.nvim/blob/master/doc/denite.txt). À un niveau basique, il fournit une couche de recherche floue par-dessus un ensemble de fonctionnalités principales. Il a été construit par le légendaire [Shougo](https://github.com/Shougo), un maître Jedi de Vim.

Denite est construit sur [lambdalisue/neovim-prompt](https://github.com/lambdalisue/neovim-prompt). Il dispose d'une interface complète qui peut prendre un certain temps à maîtriser. Vous pouvez créer des menus personnalisés et utiliser de nombreuses sources personnalisées avec Denite comme couche supérieure.

#### **Bases**

J'utilise principalement [Denite](https://github.com/Shougo/denite.nvim) pour trouver des fichiers dans mon projet et gérer mes fichiers ouverts. J'ai configuré Denite pour utiliser [ripgrep](https://github.com/BurntSushi/ripgrep) pour alimenter mes recherches. Vous pouvez voir [comment je l'ai configuré](https://github.com/ctaylo21/jarvis/blob/master/config/nvim/init.vim#L58) dans ma configuration.

J'ai mappé toutes les fonctionnalités clés pour un accès rapide et facile. Les touches que j'utilise pour ces mappings sont simplement une préférence personnelle et doivent être personnalisées par utilisateur. J'utilise l'option de « fenêtre flottante » pour mes mappings Denite, mais d'autres variations sont également prises en charge (comme les divisions horizontales/verticales).

#### **Gestion des fichiers ouverts**

`;` affiche une liste des fichiers actuellement ouverts. Vous pouvez commencer à taper et cela vous permettra de rechercher de manière floue parmi vos fichiers ouverts actuels. Avec la liste de fichiers ouverte, `<ctrl>o` vous permet de parcourir la liste comme si vous étiez en mode normal, où vous pouvez ouvrir et/ou supprimer des fichiers de la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oVQVFnE9i41t_tmK9chiUQ.gif)
_Gestion des buffers ouverts avec Denite_

#### **Recherche floue de fichiers**

`<leader>t` effectue une recherche floue des fichiers dans le répertoire actuel. Avec ripgrep, tous les fichiers dans votre `.gitignore` sont également ignorés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YiZ9RVBkO1xunJW8V3_DoQ.gif)
_Recherche floue de fichiers dans le répertoire actuel_

#### **Recherche dans le projet**

`<leader>g` et `<leader>j` recherchent dans l'ensemble du projet un terme donné et le terme sous le curseur, respectivement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bwBvzXB5iv94W7KCmvwK8w.gif)
_Recherche avec Denite_

#### **Configuration**

Denite peut être un outil assez difficile à comprendre. Il est bien documenté, mais il fait référence à certains concepts qui peuvent être inconnus pour la plupart des utilisateurs. Toutes mes [configurations Denite](https://github.com/ctaylo21/jarvis/blob/master/config/nvim/init.vim#L58) sont documentées dans ma configuration, vous pouvez donc l'utiliser comme référence. Voici un exemple rapide de configuration des options de base de Denite pour des choses comme la personnalisation des groupes de surlignage et des dispositions.

### **Coc.nvim**

**Ce que vous obtenez** : Moteur de code Intellisense, auto-complétion, linting, correction de code

L'un des plus grands défis du développement moderne dans Vim est la configuration de la [complétion de code Intellisense](https://en.wikipedia.org/wiki/Intelligent_code_completion). La plupart des éditeurs modernes comme [Visual Studio Code](https://code.visualstudio.com/) viennent avec des moteurs Intellisense intégrés, ou facilement disponibles avec un plugin (avec une configuration minimale).

J'ai essayé quelques solutions, et [coc.nvim](https://github.com/neoclide/coc.nvim) est la meilleure que j'ai utilisée. Il vient avec plusieurs fonctionnalités majeures qui sont le cœur de l'élévation de Vim au même niveau que les IDE modernes.

Il y a quelques raisons principales pour lesquelles je pense que c'est l'une des meilleures solutions pour Intellisense dans Vim :

1. Il était **incroyablement** facile à configurer et a immédiatement fonctionné avec mes projets TypeScript et JavaScript.
2. Il est construit sur [language servers](https://langserver.org/), qui alimentent Intellisense dans de nombreux éditeurs modernes.
3. Les extensions de serveur de langage comme [coc-tsserver](https://github.com/neoclide/coc-tsserver) sont construites sur l'extension de code [TypeScript/JavaScript](https://github.com/Microsoft/vscode/tree/master/extensions/typescript-language-features) qui est intégrée à VSCode. Ainsi, à mesure que les extensions de serveur VSCode s'améliorent, les utilisateurs de Vim peuvent également en bénéficier.

#### **Bases**

La mise en route de coc.nvim est très simple. Une fois que vous suivez les [instructions d'installation](https://github.com/neoclide/coc.nvim/wiki/Install-coc.nvim), vous pouvez installer des extensions de serveur de langage en exécutant `:CocInstall`.

Par exemple, dans mes projets web actuels, je peux avoir un moteur Intellisense entièrement fonctionnel pour la plupart des projets TypeScript/JavaScript modernes en exécutant :

```
:CocInstall coc-tsserver coc-eslint coc-json coc-prettier coc-css
```

#### **Extension LSP**

C'est le cœur de l'expérience coc.nvim. Avec une extension de serveur de langage comme [coc-tsserver](https://github.com/neoclide/coc-tsserver), vous obtenez [une tonne de fonctionnalités](https://github.com/neoclide/coc-tsserver#features). J'en mettrai quelques-unes en avant :

* Prise en charge de la complétion de code
* Aller à la définition
* Trouver les références
* Aide à la signature
* Validation du code
* Prise en charge de JavaScript & TypeScript et JSX/TSX

![Image](https://cdn-media-1.freecodecamp.org/images/1*gveAH1EA0tK3LIPCMkq-pw.gif)
_coc-tsserver en action avec React et Typescript_

Par défaut, vous obtenez une complétion de code automatique et rapide. Les types sont automatiquement importés, et vous pouvez voir les signatures de fonction et les complétions de code pertinentes au fur et à mesure que vous tapez.

J'ai configuré quelques mappings pour utiliser rapidement quelques fonctionnalités clés du serveur de langage :

Ces mappings vous permettent de sauter rapidement à la définition d'un symbole, de voir l'implémentation d'un symbole ou de trouver où il est référencé. Je les utilise tous fréquemment et les trouve être un énorme gain de productivité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sugrSH6xNNPIxRuw-Rw1mA.gif)
_Utilisation des mappings coc.nvim_

#### **Linting**

Je m'appuie sur [ESLint](https://eslint.org/) pour le linting de mes projets JavaScript et TypeScript. Maintenant que [TSLint est en cours de dépréciation](https://medium.com/palantir/tslint-in-2019-1a144c2317a9), le choix est encore plus facile. J'ai initialement utilisé [Ale](https://github.com/w0rp/ale) (qui est un excellent outil), mais il avait quelques problèmes lorsqu'il était utilisé avec coc.nvim.

Maintenant, en utilisant l'extension de serveur de langage [coc-eslint](https://github.com/neoclide/coc-eslint), vous pouvez obtenir des retours en temps réel de votre linter et de votre serveur de langage en utilisant le même outil. J'utilise également [coc-prettier](https://github.com/neoclide/coc-prettier) pour que coc.nvim formate mon code selon les normes [prettier](https://prettier.io/) lors de l'enregistrement du fichier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0nZE62WR2LxaufaX2anB0g.gif)
_Utilisation de eslint et prettier via coc.nvim_

#### **Configuration**

Vous pouvez configurer votre installation de coc.nvim en créant un fichier de configuration. En ce moment, [le mien](https://github.com/ctaylo21/jarvis/blob/master/config/nvim/coc-settings.json) est assez simple :

Vous pouvez en savoir plus sur la configuration de votre propre fichier de configuration coc.nvim [ici](https://github.com/neoclide/coc.nvim/wiki/Using-configuration-file).

### **Conclusion**

Cela conclut à peu près tout. J'adorerais entendre vos retours ou suggestions, alors n'hésitez pas à laisser un commentaire ! Au cas où vous l'auriez manqué ci-dessus, pour ma configuration complète, consultez mes [dotfiles](https://github.com/ctaylo21/jarvis) et [mon article sur le reste de ma configuration](https://medium.freecodecamp.org/coding-like-a-hacker-in-the-terminal-79e22954968e) en dehors de Vim. Merci pour votre lecture !