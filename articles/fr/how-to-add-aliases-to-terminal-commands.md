---
title: Comment ajouter des alias aux commandes du terminal sous Linux et Mac
subtitle: ''
author: Kaushal Joshi
co_authors: []
series: null
date: '2024-04-15T15:37:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-aliases-to-terminal-commands
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/terminal-alias.jpg
tags:
- name: Linux
  slug: linux
- name: mac
  slug: mac
- name: terminal
  slug: terminal
seo_title: Comment ajouter des alias aux commandes du terminal sous Linux et Mac
seo_desc: 'In this article, we''ll explore a simple trick that can save you hours
  of typing repetitive commands in the terminal.

  As developers, we spend a substantial amount of time executing commands on the terminal.
  Whether it''s navigating through directories,...'
---

Dans cet article, nous allons explorer une astuce simple qui peut vous faire gagner des heures de saisie de commandes répétitives dans le terminal.

En tant que développeurs, nous passons une quantité substantielle de temps à exécuter des commandes sur le terminal. Qu'il s'agisse de naviguer dans les répertoires, d'exécuter des scripts, de changer les versions de Node.js ou de commandes de contrôle de version, la saisie manuelle de chaque commande est une tâche chronophage.

Pour ceux qui ont du mal à se souvenir des commandes ou de leurs flags associés, cela peut devenir encore plus fastidieux.

Ne vous inquiétez pas ! Il existe une solution simple mais puissante à ce problème. Cela s'appelle les alias de terminal.

## La commande `alias`

La commande `alias` vous permet de créer des raccourcis pour des commandes existantes, les rendant plus faciles à retenir et plus rapides à exécuter. Lorsque vous définissez un alias, vous créez une nouvelle étiquette pour une commande existante.

### Syntaxe de la commande `alias`

La syntaxe est simple : vous pouvez assigner une commande à une étiquette comme vous assigneriez une valeur à une variable dans la plupart des langages de programmation.

```bash
alias nom_alias='longue commande'
```

Décortiquons cette commande pour mieux la comprendre :

* `alias` : La commande du terminal qui permet de définir un alias.
* `nom_alias` : C'est le nom ou l'étiquette que vous assignez à la commande. En gros, vous allez taper cela dans le terminal au lieu de la commande complète.
* `'longue commande'` : C'est la commande à laquelle vous voulez ajouter un alias. Assurez-vous d'entourer la commande avec des guillemets simples (`'`) car presque toutes les commandes contiennent des espaces ou des caractères spéciaux.

## Alias prédéfinis

Il existe déjà certains alias prédéfinis dans les terminaux. Et il y a de fortes chances que vous les ayez utilisés sans même le savoir.

De tels alias sont définis dans les fichiers de configuration du shell système (`/etc/bash.bashrc`) ou spécifiques à l'utilisateur (`~/.bsahrc`).

Vous pouvez trouver une liste de tous les alias prédéfinis en exécutant la commande `alias` sans aucune option ou flag.

```
alias
```

## Comment créer un alias qui persiste entre les sessions

Par défaut, les alias ne persistent que dans la session actuelle. Cela signifie que si vous fermez le terminal, l'alias sera effacé et vous ne pourrez plus l'utiliser par la suite.

Pour résoudre ce problème, vous devez définir l'alias dans le fichier de configuration du shell. Le shell est un interpréteur qui réside à l'intérieur d'un terminal et établit une interface entre vous et le système d'exploitation. Par conséquent, accéder au bon shell ainsi que modifier le bon fichier de configuration est très important.

Voici les fichiers de configuration pour les trois applications shell les plus couramment utilisées :

1. **Bash** : `~/.bashrc`
2. **Zsh** : `~/.zshrc`
3. **Fish** : `~/.config/fish/config.fish`

Essayons d'ajouter un nouvel alias à Bash.

```
echo "alias nrd='npm run dev'" >> ~/.bashrc
```

Décortiquons cette commande :

* `echo` : Une commande de terminal qui vous permet d'écrire du contenu dans la commande du terminal.
* `"alias ..."` : Il s'agit du contenu dont nous avons parlé dans le point précédent. C'est une commande alias qui ajoute `nrd` comme alias pour la commande `npm run dev`.
* `>>` : Indique au terminal d'ajouter le contenu de gauche (commande alias) au fichier de droite. Dans notre cas, nous le stockons dans le fichier de configuration bash.
* `~/.bashrc` : Il s'agit du fichier auquel le contenu de la commande echo sera ajouté.

N'oubliez pas de remplacer `~/.bashrc` par le fichier de configuration de votre shell.

## Comment créer un alias dynamique

Souvent, vous devez utiliser des commandes répétitives mais avec quelques petites modifications en fonction de ce que vous voulez. Le meilleur exemple de cela est les commandes Git. Dans ce cas, vous pouvez ajouter un substitut à votre commande qui serait remplacé par l'option/paramètre dynamique lors de son exécution dans le terminal.

```
alias gpll='git pull --rebase origin ${branch}'
```

Lors de l'exécution de la commande, vous devez remplacer `${branch}` par la branche à partir de laquelle vous souhaitez tirer les modifications. Voici comment vous le feriez pour tirer les modifications de la branche `main` :

```
gpll main
```

Vous pouvez également ajouter plusieurs substituts à votre alias. Assurez-vous simplement d'écrire l'alias avec le bon ordre des valeurs réelles :

```
alias gpll='git pull --rebase ${remote} ${branch}
```

Lors de l'exécution de la commande, vous devez remplacer `${remote}` et `${branch}` par des valeurs appropriées, comme suit :

```
gpll origin main

```

## Comment créer un alias pour plusieurs commandes

Il existe des cas où vous devez utiliser plusieurs commandes séquentiellement. Vous pouvez également créer un alias pour cela. Séparez chaque commande par `&&` qui exécute la commande de droite après que la commande de gauche soit exécutée.

```
gpsh='git pull --rebase && git push'
```

## Comment supprimer un alias

Si vous souhaitez supprimer un alias de la session actuelle, vous pouvez utiliser la commande `unalias`. Cette commande ne prend qu'un seul argument : le nom de l'alias.

```
unalias mon-nom-dalias
```

Cependant, si vous souhaitez supprimer un alias enregistré dans le fichier de configuration, vous devez le supprimer du fichier lui-même. Vous pouvez utiliser un simple éditeur de texte comme [Nano](https://help.ubuntu.com/community/Nano) pour cela.

```
nano ~/.bashrc
```

Faites défiler vers le bas pour trouver tous vos alias et supprimez ceux que vous ne voulez plus.

Lorsque vous avez terminé, vous pouvez quitter l'éditeur après avoir enregistré. C'est ici que je peux introduire un mème sur l'impossibilité de quitter les éditeurs de texte basés sur le terminal. Mais avec Nano, c'est très simple :

1. Appuyez sur `ctrl`+`x` si vous êtes sous Linux et `^`+`x` si vous êtes sous Mac.
2. Appuyez sur `Y` pour confirmer les modifications
3. Appuyez sur Entrée ou retour selon votre système d'exploitation pour enregistrer le fichier.

Vous voyez ? Rien de difficile :)

## Mises en garde

Il y a deux choses importantes que vous devez retenir lors de la création d'un alias.

### Les alias sont spécifiques au shell

Les alias sont spécifiques au shell que vous utilisez. Un alias créé dans un shell ne fonctionnera pas dans un autre shell.

Vous devez créer un nouvel alias si vous souhaitez l'utiliser dans une session différente. Il n'y a pas de solution de contournement à cette mise en garde. Une astuce que vous pouvez faire est d'enregistrer manuellement l'alias dans les fichiers de configuration de tous les shells que vous utilisez.

### Les alias sont liés à la session par défaut

Les alias ne sont disponibles que dans la session actuelle. Si vous ouvrez une nouvelle fenêtre de terminal ou vous déconnectez, l'alias ne sera pas disponible.

Par conséquent, il est recommandé d'enregistrer toujours un alias dans un fichier de configuration afin de pouvoir l'utiliser à tout moment.

## TL;DR

* La commande `alias` ajoute des _raccourcis_ à une commande ou une série de commandes. `alias raccourci='commande existante valide`.
* Enregistrez un alias dans le fichier de configuration du shell pour qu'il persiste entre les sessions. Chaque shell a un fichier de configuration unique. `echo "nrd='npm run dev'" >> ~/.bashrc`.
* Créez un alias dynamique en substituant la valeur dynamique par un espace réservé. L'espace réservé doit être entouré par `${}`. `alias gp='git pull origin ${branch}` doit être exécuté comme `gp main` dans le terminal.
* Ajoutez plusieurs commandes à un alias en les joignant avec `&&`.
* Supprimez un alias en l'effaçant manuellement du fichier de configuration.

## Conclusion

J'espère que cet article vous aide à optimiser votre temps et à améliorer votre productivité en tant que développeur. Si c'est le cas, n'oubliez pas de le partager avec vos pairs afin qu'ils puissent améliorer leur efficacité également.

Quelles autres techniques utilisez-vous pour travailler efficacement ? J'adorerais en savoir plus. Je suis le plus actif sur [Twitter](https://twitter.com/clumsy_coder) et [Peerlist](https://peerlist.io/kaushal), si vous voulez dire bonjour !

En attendant, bon scripting ! 👨💻