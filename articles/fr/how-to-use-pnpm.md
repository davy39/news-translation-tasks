---
title: Comment utiliser pnpm – Installation et commandes courantes
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2024-01-09T15:31:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-pnpm
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/cover-pnpm-1.png
tags:
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: performance
  slug: performance
- name: pnpm
  slug: pnpm
seo_title: Comment utiliser pnpm – Installation et commandes courantes
seo_desc: 'pnpm is like npm, but it''s way faster and more efficient. After all, the
  starting p stands for _p_erformant.

  According to its creator, Zoltan Kochan, pnpm "allows you to save gigabytes of disk
  space."

  Many popular projects including Next.js, Vite, Sv...'
---

_pnpm_ est similaire à npm, mais il est bien plus rapide et efficace. Après tout, le _p_ initial signifie _p_erformant.

Selon son créateur, Zoltan Kochan, pnpm "vous permet d'économiser des gigaoctets d'espace disque".

De nombreux projets populaires, dont Next.js, Vite, Svelte, et même freeCodeCamp, utilisent pnpm. C'est donc le moment idéal pour essayer cet outil si vous ne l'avez pas encore fait. Je suis sûr que votre temps ne sera pas perdu.

Dans cet article, je ne vais pas entrer dans les détails de pourquoi pnpm est plus rapide et plus efficace que npm. Vous pouvez consulter la [documentation officielle](https://pnpm.io/motivation) si vous souhaitez en savoir plus.

Le but de cet article est de vous faire démarrer rapidement avec pnpm afin que vous puissiez effectuer vos tâches quotidiennes que vous faisiez auparavant avec npm ou yarn. Prenez votre tasse de thé ou de café préférée ☕, et plongeons directement dans le sujet ! 🚀

## Comment installer pnpm

Je suppose que vous avez déjà une version moderne de Node.js installée sur votre machine. Ces versions modernes incluent une commande appelée `corepack`. Elle vous permet de gérer vos gestionnaires de paquets Node.

Oui, vous avez bien lu ! Il s'agit d'une fonctionnalité expérimentale de Node, mais elle fonctionne plutôt bien.

Pour commencer à l'utiliser, vous devez d'abord l'activer en entrant la commande suivante depuis votre terminal, ce qui a pour effet d'installer pnpm (et aussi yarn) sur votre système :

```zsh
corepack enable
```

C'est aussi simple que cela. Maintenant, si vous exécutez `pnpm --version`, vous verrez la version que vous venez d'installer. Cependant, cela peut ne pas être la dernière version de pnpm. Si c'est le cas, vous pouvez installer la dernière version de pnpm en utilisant cette commande :

```zsh
corepack prepare pnpm@latest --activate
```

Gardez à l'esprit qu'il existe de nombreuses façons d'installer pnpm sur votre système, et vous pouvez lire à leur sujet dans la [documentation d'installation](https://pnpm.io/installation). Ma méthode préférée est la formule `corepack` que j'ai montrée ci-dessus.

## Comment configurer votre shell pour plus d'efficacité (Optionnel)

Vous avez maintenant pnpm installé. Mais l'expérience par défaut en ligne de commande peut être améliorée pour vous faire gagner du temps.

Notez que cette section est optionnelle. Si vous le souhaitez, vous pouvez passer à la section suivante. Mais si vous êtes sérieux quant à la configuration pour que l'expérience CLI soit agréable, apprenons comment le faire.

### `pnpm` est difficile à taper – Configurer un alias

Si vous trouvez `pnpm` difficile à taper comme moi, vous pouvez configurer un alias pour vous faciliter la tâche. Si vous êtes sous Linux ou MacOS, ajoutez simplement ce qui suit dans votre configuration de shell (`.bashrc`, `.zshrc`, ou `config.fish`) :

```
alias pn=pnpm

```

Si vous souhaitez configurer votre alias dans Powershell (Windows), vous pouvez [consulter cette documentation](https://pnpm.io/installation#adding-a-permanent-alias-in-powershell-windows).

### Comment configurer la complétion par tabulation

Il existe deux façons de procéder dans pnpm. Les deux ont leurs avantages et inconvénients.

Je vais d'abord partager avec vous ma méthode préférée. Il s'agit d'un plugin shell appelé `pnpm-shell-completion` et il est disponible pour zsh, fish shell, et Powershell core. Il ne couvre que les commandes les plus couramment utilisées. Si vous êtes utilisateur d'Arch Linux et de zsh, vous pouvez l'installer avec n'importe quel helper AUR. Par exemple, si vous utilisez `yay`, exécutez la commande suivante pour l'installer :

```zsh
yay -S pnpm-shell-completion
```

Ensuite, ajoutez la ligne suivante dans votre fichier `.zshrc` pour le charger :

```zsh
source /usr/share/zsh/plugins/pnpm-shell-completion/pnpm-shell-completion.zsh
```

Maintenant, cela devrait fonctionner. Si vous utilisez un autre shell supporté, suivez la [documentation](https://github.com/g-plane/pnpm-shell-completion) du plugin pour apprendre comment l'installer.

La deuxième méthode est intégrée avec pnpm. Pour configurer ce style de complétion automatique, exécutez la commande suivante :

```shell
pnpm install-completion

```

Puis suivez les étapes qu'il vous donne. Cette méthode couvre plus de commandes que la première approche. Mais elle a quelques limitations – par exemple, elle ne peut pas compléter automatiquement les scripts de votre `package.json`. Elle ne peut pas non plus, par exemple, compléter automatiquement le nom de toute dépendance que vous souhaitez désinstaller.

## Comment utiliser `pnpm`

Maintenant, vous devriez avoir pnpm installé avec un alias et une complétion par tabulation. Plus de délai – voyons comment utiliser pnpm.

### Comment initialiser un nouveau projet avec `pnpm`

Pour obtenir le `package.json` par défaut dans le répertoire courant, exécutez la commande suivante :

```zsh
pnpm init

```

Contrairement à npm, il ne le créera pas de manière interactive et vous n'avez pas besoin de spécifier le flag `-y` pour cela.

### Comment installer un paquet

Pour installer un paquet en tant que dépendance, la syntaxe est :

```
pnpm add <pkg>

```

Pour installer un paquet en tant que dépendance de développement, vous devez passer le flag `-D` (ou `--save-dev`) :

```
pnpm add -D <pkg>

```

Pour installer un paquet globalement, utilisez le flag `-g` :

```
pnpm add -g <pkg>

```

### Comment installer toutes les dépendances

Supposons que vous avez cloné un projet depuis GitHub. Il a un fichier `package.json` mais pas de `node_modules` (vous ne devriez pas suivre `node_modules` avec Git). Maintenant, pour installer toutes les dépendances de ce `package.json`, la commande est très similaire à `npm` :

```
pnpm install

```

ou

```
pnpm i

```

### Comment exécuter un script `package.json`

Ce processus est également très similaire à `npm`. La manière explicite de le faire est d'utiliser la commande `run`. Si vous avez un script nommé `build`, vous pouvez l'exécuter avec cette commande :

```
pnpm run build

```

Vous pouvez également utiliser `pnpm build` pour faire la même chose. Il s'agit d'un format abrégé qui peut faire d'autres choses également. Nous en apprendrons plus sur les formes abrégées très bientôt dans cet article.

### Comment exécuter des commandes qui viennent avec les dépendances

Vous pouvez exécuter des commandes qui viennent avec les dépendances en utilisant `pnpm exec`.

Lorsque vous installez un paquet, s'il a des commandes spécifiées par le champ `bin` dans son `package.json`, vous obtiendrez un exécutable du même nom dans votre répertoire `node_modules/.bin`. Son but est d'exécuter le fichier correspondant.

`pnpm exec` préfixe `./node_modules/.bin` au `PATH` (c'est-à-dire `PATH=./node_modules/.bin:$PATH`) et exécute ensuite la commande donnée.

L'exemple suivant montre l'installation de `typescript` en tant que dépendance de développement, puis l'exécution de la commande `tsc` pour créer un fichier `tsconfig.json` :

```
pnpm add -D typescript
pnpm exec tsc --init

```

Similaire à la commande `pnpm run`, vous pouvez également omettre `exec` et utiliser simplement `pnpm tsc` pour faire la même chose. Cela fonctionne lorsque vous n'avez pas de script `tsc` conflictuel dans votre `package.json`. Dans la section suivante, nous examinerons de près cette syntaxe abrégée.

Notez que puisque `pnpm exec` a accès à toutes les commandes résolues par les chemins spécifiés dans `PATH`, vous pouvez avoir accès à de nombreuses commandes système, par exemple `rm`, `ls`, etc.

### Comment fonctionne `pnpm <command>`

`pnpm <command>` fonctionne comme suit :

* Si `<command>` est une commande pnpm (c'est-à-dire `add`, `install`, etc.), exécute cette commande.
* Sinon, si `<command>` est un script trouvé dans `package.json`, exécute `pnpm run <command>`.
* Sinon, exécute `pnpm exec <command>`.

Ainsi, `pnpm <command>` sert de raccourci pratique où `pnpm exec` et `pnpm run` sont des commandes explicites sans repli.

### Comment mettre à jour les paquets

Pour mettre à jour les paquets vers leurs dernières versions en fonction de la plage spécifiée dans `package.json`, exécutez cette commande :

```
pnpm up

```

Pour mettre à jour toutes les dépendances vers leurs dernières versions, en ignorant les plages spécifiées dans `package.json`, exécutez ceci :

```
pnpm up --latest

```

### Comment supprimer un paquet

Pour supprimer un paquet à la fois de `node_modules` et de votre `package.json`, vous pouvez utiliser `pnpm rm`. Par exemple, si vous avez installé `express`, vous pouvez le supprimer en utilisant :

```
pnpm rm express

```

Pour supprimer un paquet installé globalement, utilisez le flag `-g`. Voici un exemple de suppression du paquet installé globalement `nodemon` :

```
pnpm rm -g nodemon

```

## Existe-t-il une alternative à `npx` ?

Oui – c'est la commande `pnpm dlx`. Elle est très similaire à npx. Elle télécharge le paquet spécifié depuis le registre sans l'installer en tant que dépendance, puis exécute la commande binaire par défaut qu'il expose.

Par exemple, vous pouvez exécuter la commande que le paquet `cowsay` expose comme ci-dessous pour imprimer un art ASCII d'une vache disant une chaîne que vous passez :

```
pnpm dlx cowsay hi freeCodeCamp

```

Maintenant, vous vous demandez peut-être, si un paquet expose plusieurs commandes binaires, quelle commande `pnpm dlx` choisit comme commande par défaut ? Ou comment pouvez-vous spécifier explicitement une commande binaire ?

Voyons d'abord comment la commande binaire par défaut est déterminée :

* Si le champ `bin` de `package.json` n'a qu'une seule entrée, celle-ci est utilisée.
* Sinon, s'il y a un nom de commande dans le champ `bin` de `package.json` qui correspond au nom du paquet, en ignorant la partie scope si elle existe, alors cette commande est utilisée.
* Sinon, pnpm ne peut pas déterminer la commande par défaut et lance une erreur avec un message d'erreur utile qui répondra probablement à la deuxième question.

Pour spécifier explicitement une commande particulière, vous devrez d'abord installer le paquet en utilisant l'option `--package` et spécifier cette commande après `dlx`.

Par exemple, le paquet `typescript` expose deux commandes binaires `tsc` et `tsserver`. Maintenant, si vous voulez exécuter `tsc --init` pour créer un fichier `tsconfig.json` sans avoir `typescript` dans votre `node_modules` ou `package.json`, vous pouvez utiliser `pnpm dlx` comme suit :

```
pnpm --package=typescript dlx tsc --init

```

## Conclusion

Dans ce tutoriel, vous avez appris ce qu'est pnpm et comment l'installer. Nous avons également couvert plusieurs commandes courantes de pnpm que vous aurez probablement besoin au quotidien.

J'espère que cet article vous a aidé à démarrer avec pnpm. Consultez la [documentation de pnpm](https://pnpm.io/motivation) pour en apprendre davantage.

Si vous le souhaitez, vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/ashutosh-biswas/) et [Twitter](https://twitter.com/ashutoshbw) où je partage des choses utiles liées à la programmation.

Bon codage !