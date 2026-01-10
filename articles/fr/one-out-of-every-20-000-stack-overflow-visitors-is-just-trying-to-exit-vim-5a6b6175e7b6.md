---
title: Comment quitter Vim et sortir de l'éditeur VI — la question la plus populaire
  sur Stack Overflow
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2017-05-23T19:58:40.000Z'
originalURL: https://freecodecamp.org/news/one-out-of-every-20-000-stack-overflow-visitors-is-just-trying-to-exit-vim-5a6b6175e7b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AD1e170YTJaiUBypv1H9Ow.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Comment quitter Vim et sortir de l'éditeur VI — la question la plus populaire
  sur Stack Overflow
seo_desc: 'Vim is a popular keyboard-only code editor originally released in 1991.
  It is famously difficult to learn, but many developers swear by it.

  Vim is installed on pretty much every Linux- or Unix-based computer, and if you
  accidentally open it, it’s qui...'
---

Vim est un éditeur de code populaire utilisant uniquement le clavier, initialement publié en 1991. Il est réputé difficile à apprendre, mais de nombreux développeurs en sont convaincus.

Vim est installé sur presque tous les ordinateurs basés sur Linux ou Unix, et si vous l'ouvrez accidentellement, il est assez difficile d'en sortir.

Stack Overflow [vient d'annoncer](https://fcc.im/2qSxIN5) qu'ils ont atteint un nouveau jalon : plus d'un million de développeurs ont visité Stack Overflow pour essayer de comprendre comment quitter Vim.

![Image](https://cdn-media-1.freecodecamp.org/images/O9WUUSIUJN2fedVEOT7Cuc07dCG-tX53xr6F)
_Un tweet lié à Vim par [I Am Devloper](https://fcc.im/2qdz2XL" rel="noopener" target="_blank" title=")_

Si vous vous retrouvez coincé dans Vim, vous pouvez généralement en sortir en faisant ce qui suit :

1. appuyez sur échap pour entrer en mode "Maître"
2. puis tapez `:` pour entrer en mode "Dernière Ligne"
3. puis tapez `q` et appuyez sur entrée.

Cela devrait vous permettre de sortir. Si cela ne fonctionne pas, répétez ces étapes en utilisant `q!` pour forcer la sortie.

Si vous souhaitez enregistrer les modifications apportées au fichier, vous pouvez ajouter un `w` à ces commandes (w signifie "write" ou écrire) : `wq` ou `wq!`

Si vous devez modifier quelque chose sur un serveur Linux et que vous n'avez pas investi des dizaines d'heures à vous améliorer avec Vim, vous pouvez ouvrir un fichier avec un éditeur intégré beaucoup plus simple appelé Nano en tapant : `nano [nomdufichier]`

Et si vous voulez vous améliorer avec Vim, consultez [Vim Adventures](https://fcc.im/2rQka1J), un jeu de type Zelda contrôlé en utilisant des commandes Vim.

![Image](https://cdn-media-1.freecodecamp.org/images/qQgRVU41xBricYjR865rsAZuueOR32hoUFc-)

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps. ?**