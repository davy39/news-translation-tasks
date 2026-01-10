---
title: Comment publier des packages sur npm (comme le font les professionnels)
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-04-09T15:17:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-packages-to-npm-the-way-the-industry-does-things-2077ec34d7e8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Nhf9jeZDYfGdX6N6.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment publier des packages sur npm (comme le font les professionnels)
seo_desc: 'It’s simple to publish a package onto npm. There are two steps:


  Create your package.

  Publish the package.


  But publishing packages the way the industry does it? Not so simple. There are more
  steps. We’ll go through what steps are required, and I’ll ...'
---

Il est simple de publier un package sur npm. Il y a deux étapes :

1. Créez votre package.
2. Publiez le package.

Mais publier des packages comme le font les professionnels ? Ce n'est pas si simple. Il y a plus d'étapes. Nous allons passer en revue les étapes nécessaires, et je vais vous montrer une méthode facile pour publier et mettre à jour votre package.

### Créer votre premier package

Cette section est pour vous si vous n'avez jamais publié de package sur npm auparavant. N'hésitez pas à passer à la section suivante si vous en avez déjà publié un.

Pour publier votre premier package sur npm, vous devez suivre ces étapes :

**Tout d'abord, vous devez avoir un compte npm**. Créez-en un [ici](https://www.npmjs.com/signup) si vous n'en avez pas encore.

**Ensuite, vous devez vous connecter à votre compte npm via la ligne de commande**. (Vous devez avoir Node et npm installés sur votre système avant d'effectuer cette étape. Installez-les [ici](https://nodejs.org/en/)).

Pour vous connecter, utilisez `npm login`.

```
npm login
```

Vous serez invité à entrer votre nom d'utilisateur, votre mot de passe et votre adresse e-mail.

![Image](https://cdn-media-1.freecodecamp.org/images/JHhisobcBkv-CepU3oB0sjvuGJ3lpkQbqixh)

**Troisièmement, vous devez créer un package**. Pour ce faire, créez un dossier quelque part sur votre ordinateur et accédez-y. La version en ligne de commande est :

```
# Création d'un dossier nommé comment-publier-sur-npm mkdir comment-publier-sur-npm # Navigation dans le dossier cd comment-publier-sur-npm
```

Ensuite, vous voulez commencer le projet avec la commande `npm init`.

```
npm init
```

Cette commande vous guide à travers quelques questions et crée un fichier `package.json` pour vous à la fin. Ce fichier `package.json` contient les éléments essentiels dont vous avez besoin pour publier votre projet. (N'hésitez pas à sauter les questions qui n'ont pas de sens).

![Image](https://cdn-media-1.freecodecamp.org/images/zkzI4ZMLfqEMMIfD2aFF6zfpxKpT54w5gU1Z)

**La dernière étape consiste à publier votre package** avec la commande `npm publish`.

```
npm publish
```

Si le package existe déjà sur npm (parce que votre package a le même nom qu'un autre package sur npm), vous ne pourrez pas le publier. Vous obtiendrez une erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/q8cTyrCM2nFMivMgtaW2Gi9Jcno1zquqViBU)

Vous devrez changer le nom de votre package.

Pour changer le nom de votre package, modifiez la propriété `name` dans le fichier `package.json`. Ici, je l'ai changé en `publication-sur-npm`.

(Vous pouvez vérifier les collisions de noms en effectuant une recherche sur npm, ou via la commande `npm search`).

![Image](https://cdn-media-1.freecodecamp.org/images/Gp-SPyfzY0nyDVKNJXa3GpFEahjKVuAfV8PD)

Il est également judicieux de mettre à jour le nom du dossier pour plus de cohérence. Voici l'équivalent en ligne de commande.

```
# Commande pour changer les noms de dossiers en déplaçant tout mv comment-publier-sur-npm publication-sur-npm
```

Essayez à nouveau la commande `publish`. Vous devriez obtenir un message de succès maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/ASGCDDVtEEjdKoPqzdvA2Ux32pgXsdcE98xE)

### Que faire si tous les noms que vous avez imaginés sont déjà pris

C'est un problème courant puisque beaucoup de gens créent des packages sur npm. Il est parfois difficile d'obtenir le nom de package que vous souhaitez. (C'est comme si je ne pouvais _jamais_ trouver un bon domaine `.com`).

Pour résoudre ce problème, npm vous permet de publier dans un scope. Cela signifie que vous pouvez publier le package sous votre propre nom d'utilisateur (ou organisation npm), ce qui vous libère des problèmes de nommage.

Pour publier dans un scope, vous pouvez soit :

1. Changer le `name` en `@username/nom-du-package` manuellement dans `package.json`
2. Exécuter `npm init --scope=username` au lieu de `npm init`

Si votre dépôt a un scope, vous devez ajuster légèrement la commande de publication :

```
npm publish --access public
```

C'est tout ce que vous devez faire pour publier un package sur npm.

Maintenant, passons à la manière dont les professionnels publient des packages.

Prenons un framework populaire comme React. Si vous explorez React, vous remarquerez quelques choses :

Premièrement, React a un [dépôt Github](https://github.com/facebook/react).

Deuxièmement, React est [publié sur](https://www.npmjs.com/package/react) npm.

Troisièmement, React suit le [versionnage sémantique](https://zellwk.com/blog/semantic-versioning/) (Semver en abrégé).

![Image](https://cdn-media-1.freecodecamp.org/images/uwwUruPCdcFdhAmArNB-nBtUYcL7yb3x2J6R)

Quatrièmement, chaque mise à jour de React a une étiquette git associée. Cette étiquette git suit également Semver.

![Image](https://cdn-media-1.freecodecamp.org/images/wZuV9GG8e9pkllgcdjrVIGmjK84bDs-atDeU)

Cinquièmement, il y a des [notes de version](https://github.com/facebook/react/releases) pour chaque mise à jour de React.

Cela signifie que la publication d'un package implique de nombreuses étapes. Au minimum, vous devez :

1. Exécuter les tests (s'il y en a)
2. Mettre à jour la `version` dans `package.json` selon Semver
3. Créer une étiquette git selon Semver
4. Pousser le package vers Github
5. Pousser le package vers npm
6. Créer des notes de version pour chaque mise à jour

Il est courant d'oublier l'une de ces choses lorsque nous sommes prêts à pousser. Parfois, nous faisons `npm publish` et nous prenons une pause. À notre retour, nous nous mettons dans l'embarras pour avoir oublié.

Il y a une méthode plus facile. C'est avec un outil appelé `np`.

### np

[np](https://github.com/sindresorhus/np) (créé par [Sindre Sorhus](https://github.com/sindresorhus)) facilite la publication de packages sans oublier aucune des étapes que j'ai détaillées ci-dessus.

### Installation de np

Pour installer `np`, vous pouvez exécuter la commande suivante :

```
npm install np
```

Cela fonctionne. Mais je préfère installer `np` globalement sur mon ordinateur pour pouvoir exécuter la commande `np` n'importe où.

```
sudo npm install --global np
```

### Avant d'utiliser np

Avant d'utiliser `np`, vous devez vous assurer que :

1. Votre projet est un dépôt Git
2. Il doit avoir un dépôt distant
3. Vous devez avoir poussé vers le dépôt distant au moins une fois.
4. Vous devez également vous assurer que votre répertoire de travail est propre.

```
# Initialiser Git git init # Ajoute un dépôt distant git remote add origin some-url # Valider les changements git add . git commit -m "Premier Commit"
```

Si votre projet n'est pas un dépôt Git, vous obtiendrez cette erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/7NrM2CyehgdU8hCtwioMAAIjFY1XD8yKfYYz)

Si votre projet n'a pas de dépôt distant, vous obtiendrez cette erreur (à une étape ultérieure des vérifications).

![Image](https://cdn-media-1.freecodecamp.org/images/3Pb4qxEzdXr-Uu8xk6o84aTg1CbhPKff1aBT)

Si votre répertoire de travail est sale, vous obtiendrez cette erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/OS9Wo5PaEyUDlmWh7ZWtig0Joik0GwRgnh6s)

Si vous n'avez pas poussé vers le dépôt distant Git au moins une fois, `np` ne fera rien et restera bloqué.

### Utilisation de npm

Pour utiliser `np`, exécutez la commande `np`.

```
np
```

`np` vous demandera de saisir un numéro Semver.

![Image](https://cdn-media-1.freecodecamp.org/images/RD-MA-FOfYfODX9M8CemmsQRfNfGzoJfykQt)

Choisissez un numéro et `np` vous demandera de confirmer votre choix.

![Image](https://cdn-media-1.freecodecamp.org/images/Kli5Ll2K9rNaLOQ1OokDMpEGoEoqxJ-kzDSZ)

`np` effectue ensuite le reste du processus de publication pour vous.

### Erreur lors de l'exécution des tests

`np` exécute la commande `npm test` dans le cadre de ses vérifications.

Si vous avez suivi le tutoriel jusqu'à ce point, vous obtiendrez une erreur qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/sORwnhnEitrpcWBx9JBa5zfkwk3jdx3eIhQE)

Cela se produit parce que notre commande `npm test` entraîne une erreur. Vous pouvez l'essayer vous-même :

```
npm test
```

![Image](https://cdn-media-1.freecodecamp.org/images/QQ28caWQvveRLIwk3jwcUkBhbLFDUMSy3Qe1)

Pour corriger cette erreur, nous devons modifier le script `test` dans le fichier `package.json`.

Actuellement, il ressemble à ceci :

```
"scripts": {     "test": "echo \"Erreur : aucun test spécifié\" && exit 1"},
```

Changez-le en ceci :

```
"scripts": {     "test": "echo \"Aucun test spécifié\""},
```

Ce changement fonctionne car `exit 1` crée une erreur.

Avec ce changement, `np` devrait terminer le processus de publication. (N'oubliez pas de valider le changement avant d'exécuter `np`).

![Image](https://cdn-media-1.freecodecamp.org/images/NFPTeC5esUzD1vLJczEy-meWcFJb1qPCEi8o)

À la fin du processus, `np` ouvre une fenêtre de navigateur pour que vous puissiez écrire vos notes de version.

![Image](https://cdn-media-1.freecodecamp.org/images/Erm2uLF-N8B4b6jCa5C0AkgwqMfD5sbqZIjf)

En résumé, `np` simplifie grandement la publication de packages !

Merci d'avoir lu. Cet article vous a-t-il aidé ? Si c'est le cas, j'espère que vous envisagerez de [le partager](https://twitter.com/share?text=Comment%20publier%20des%20packages%20sur%20npm%20(comme%20le%20font%20les%20professionnels)%20par%20@zellwk%20?%20&url=https://zellwk.com/blog/publish-to-npm/). Vous pourriez aider quelqu'un d'autre. Merci beaucoup !

Cet article a été initialement publié sur [_mon blog_](https://zellwk.com/blog/publish-to-npm).  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.