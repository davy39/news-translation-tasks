---
title: Comment rechercher et remplacer dans plusieurs fichiers avec Vim
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-08-28T15:01:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-search-and-replace-across-multiple-files-in-vim
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cover-5.png
tags:
- name: Productivity
  slug: productivity
- name: vim
  slug: vim
seo_title: Comment rechercher et remplacer dans plusieurs fichiers avec Vim
seo_desc: 'In this article, you''ll learn how to interactively search-and-replace
  across many files with just two commands, thanks to Vim.

  While a multitude of methods exist to search for and replace words in a single file,
  what do you do when you’ve got a strin...'
---

Dans cet article, vous apprendrez à rechercher et remplacer de manière interactive dans plusieurs fichiers avec seulement deux commandes, grâce à Vim.

Bien qu'il existe de nombreuses méthodes pour rechercher et remplacer des mots dans un seul fichier, que faire lorsque vous avez une chaîne à mettre à jour dans plusieurs fichiers sans lien entre eux, tous avec des noms différents ? Vous utilisez la puissance des outils en ligne de commande, bien sûr !

Tout d'abord, vous devrez `find` tous les fichiers que vous souhaitez modifier. Enchaîner ce qui revient effectivement à des requêtes de recherche pour `find` n'est limité que par votre imagination.

Voici un exemple simple qui trouve les fichiers Python :

```sh
find . -name '*.py'
```

Le test `-name` recherche un motif, tel que tous les fichiers se terminant par `.py`. Mais `find` peut faire beaucoup plus avec d'autres conditions de test, y compris les tests `-regex`. Exécutez `find --help` pour voir la multitude d'options.

Affinez davantage votre recherche en utilisant `grep` pour obtenir uniquement les fichiers qui contiennent la chaîne que vous souhaitez modifier, par exemple en ajoutant :

```sh
grep -le '\<a whale\>'
```

L'option `-l` vous donne uniquement les noms de fichiers pour tous les fichiers contenant un motif (dénoté avec `-e`) qui correspond à "a whale".

Vous pouvez également utiliser `:bufdo` de Vim, qui vous permet d'exécuter la même commande sur plusieurs buffers. Il fonctionne de manière interactive avec tous ces fichiers sans la monotonie d'ouvrir, sauvegarder et fermer chaque fichier, un à la fois.

Intégrez vos résultats puissants de `find`+`grep` dans Vim avec :

```sh
vim `find . -name '*.py' \
-exec grep -le '\<a whale\>' {} \;`
```

L'utilisation de l'expansion des backticks pour passer notre recherche à Vim ouvre plusieurs buffers prêts à l'emploi. (Faites `:h backtick-expansion` dans Vim pour plus d'informations.)

Maintenant, vous pouvez appliquer la commande Vim `:bufdo` à tous ces fichiers et effectuer des actions telles que la recherche et le remplacement interactifs :

```vim
:bufdo %s/a whale/a bowl of petunias/gce
```

Le `g` pour "global" changera les occurrences du motif sur toutes les lignes. Le `e` omettra les erreurs si le motif n'est pas trouvé. L'option `c` rend cela interactif. Si vous êtes sûr de vous, vous pouvez l'omettre pour effectuer les changements sans revoir chacun d'eux.

Lorsque vous avez terminé de parcourir tous les buffers, sauvegardez tout le travail que vous avez accompli avec :

```vim
:bufdo wq!
```

Puis, régalez-vous de la gloire du temps et des efforts économisés.