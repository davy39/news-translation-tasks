---
title: Comment utiliser les alias Git pour augmenter votre productivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-27T16:47:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-aliases
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/yancy-min-842ofHC6MaI-unsplash.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: version control
  slug: version-control
seo_title: Comment utiliser les alias Git pour augmenter votre productivité
seo_desc: 'By Leonardo Faria

  Git is a very powerful tool, and it can be a little scary sometimes. It doesn''t
  matter how long you''ve used it, you will find yourself searching for "how to do
  X".

  Today I want to talk about aliases. Aliases are short, custom made c...'
---

Par Leonardo Faria

Git est un outil très puissant, et il peut parfois faire un peu peur. Peu importe depuis combien de temps vous l'utilisez, vous vous retrouverez à chercher "comment faire X".

Aujourd'hui, je veux parler des alias. Les alias sont des commandes courtes et personnalisées qui se traduisent par d'autres commandes. En plus d'économiser des frappes, les alias vous aident à éviter de mémoriser les options de commande ou de fouiller dans l'historique de votre shell pour trouver la commande dont vous avez besoin.

Il existe 2 types d'alias : les [alias Git](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases) et les alias shell, contrôlés par bash, zsh, etc. Commençons par les alias Git.

## Comment créer des alias Git

Les alias Git peuvent être stockés globalement ou dans des dépôts individuels. À moins d'avoir une raison très spécifique de garder un alias limité à un projet, je recommande de modifier le fichier de configuration global, qui se trouve à `~/.gitconfig`.

Les alias se trouvent dans la section `[alias]`. Ils sont disponibles dans votre terminal en tant qu'options Git de la même manière que `add`, `commit` et autres options fonctionnent. Voyons comment ajouter un alias, étape par étape :

Tout d'abord, ouvrez votre fichier de configuration Git. Dans mon cas, j'utiliserai VS Code :

```bash
code ~/.gitconfig
```

Ensuite, ajoutons notre premier alias Git :

```shell
[alias]
	graph = log --oneline --graph --decorate
```

Après avoir sauvegardé le fichier, allez dans un projet Git existant et exécutez `git graph`. Le résultat est similaire à l'image ci-dessous :

![exemple de git graph dans le dépôt Tailwind CSS](https://leonardofaria.net/wp-content/uploads/2020/10/git-graph.jpg)

Au lieu de taper `git log --oneline --graph --decorate` et de mémoriser les trois flags, vous pouvez maintenant utiliser `git graph` et obtenir le même résultat.

## Mes alias Git préférés

Voici quelques alias que j'ai beaucoup utilisés récemment :

```shell
[alias]
	graph = log --oneline --graph --decorate
	ls = log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate
	ll = log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate --numstat
	lds = log --pretty=format:"%C(yellow)%h\\ %ad%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate --date=short
	conflicts = diff --name-only --diff-filter=U
	local-branches = !git branch -vv | cut -c 3- | awk '$3 !~/\\[/ { print $1 }'
	recent-branches = !git branch --sort=-committerdate | head
	authors = !git log --format='%aN <%aE>' | grep -v 'users.noreply.github.com' | sort -u --ignore-case
```

`graph`, `ls`, `ll` et `lds` sont utiles pour visualiser l'historique. J'utilise beaucoup `git ll` car il me donne le commit, les fichiers modifiés et le nombre de lignes modifiées, comme montré ci-dessous :

![exemple de git ll dans le dépôt Tailwind CSS](https://leonardofaria.net/wp-content/uploads/2020/10/git-ll.jpg)

`conflicts` retourne une liste de conflits que vous pouvez simplement copier et coller dans votre éditeur.

`local-branches` retourne une liste de branches disponibles localement et non sur origin (GitHub par exemple). Cela peut être utile si, par exemple, vous devez vérifier si votre équipe a accès à vos branches.

`recent-branches` est probablement celui que j'utilise le plus dans cette liste. Si vous travaillez sur différentes fonctionnalités en même temps et que vous passez d'une branche à l'autre, c'est un must-have.

`authors` est pratique pour le travail open-source. Vous pouvez exécuter `git authors > AUTHORS.txt` et voir une liste des personnes qui ont travaillé dans le dépôt.

## Alias shell avec le plugin Git d'Oh My Zsh

La liste ci-dessus est assez petite, vous pourriez penser. Et c'est vrai. Cela est dû au fait que j'utilise également les alias créés par le [plugin Git d'Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh/blob/master/plugins/git/git.plugin.zsh).

>Oh My Zsh est un framework pour gérer votre configuration zsh. Avec cet outil, vous pouvez personnaliser l'invite de commande, utiliser différents thèmes et ajouter des plugins qui offrent des alias pour augmenter votre productivité.

Les alias shell sont créés de manière légèrement différente. Ils vivent à l'intérieur des fichiers de configuration du shell (généralement `~/.bashrc` ou `~/.zshrc`, si vous utilisez Bash et Zsh respectivement).

Voici un exemple créé par le plugin :

```shell
alias gst='git status'
```

Si vous n'utilisez pas Oh My Zsh, vous pouvez toujours copier la ligne ci-dessus et la coller à la fin des fichiers `~/.bashrc` ou `~/.zshrc` – l'alias shell fonctionnera parfaitement.

Au lieu de configurer un alias Git `st` pour `status`, j'utilise l'alias shell `gst` qui me donne le même résultat.

Je préfère les alias shell aux alias Git pour 2 raisons :

1. Les alias shell n'ont pas besoin d'être précédés par la commande `git`.
2. Je n'ai pas besoin de maintenir une liste d'alias puisque je peux simplement apprendre ceux maintenus par la communauté Oh My Zsh.

> Protip : Si vous utilisez le shell par défaut sans aucune personnalisation, je vous recommande de consulter le projet [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh/) et [Wes Bos](https://wesbos.com/)' [Command Line Power User](https://commandlinepoweruser.com/).

## Conclusion

Les alias sont des raccourcis que vous pouvez créer ou utiliser pour augmenter votre productivité. Aujourd'hui, j'ai montré deux façons de les utiliser dans Git.

J'espère que cet article vous inspire à re-imaginer comment vous utilisez le terminal. Pourquoi ne pas commencer à créer vos propres alias ?

Vous pouvez lire plus d'articles comme celui-ci sur [mon blog](https://leonardofaria.net). Si vous aimez ce contenu, vous pouvez me suivre sur [Twitter](https://twitter.com/leozera) et [GitHub](https://github.com/leonardofaria).

Photo de couverture par [Yancy Min/Unsplash](https://unsplash.com/photos/842ofHC6MaI)