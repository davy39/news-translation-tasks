---
title: Comment intégrer Prettier avec ESLint et stylelint
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-30T06:23:11.000Z'
originalURL: https://freecodecamp.org/news/integrating-prettier-with-eslint-and-stylelint-99e74fede33f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4rTkzZ0psMNKu9RgpEfQmg.jpeg
tags:
- name: eslint
  slug: eslint
- name: JavaScript
  slug: javascript
- name: Prettier
  slug: prettier
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment intégrer Prettier avec ESLint et stylelint
seo_desc: 'By Abhishek Jain

  or How to never worry about code styling again


  _Photo by [Unsplash](https://unsplash.com/photos/bJjsKbToY34?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">NordWood Themes ...'
---

Par Abhishek Jain

#### ou Comment ne plus jamais s'inquiéter du style de code

![Image](https://cdn-media-1.freecodecamp.org/images/2NnxX8zdoJFw9uQM9ez2epHwX3Z26IQQjmt-)
_Photo par [Unsplash](https://unsplash.com/photos/bJjsKbToY34?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">NordWood Themes</a> sur <a href="https://unsplash.com/search/photos/computer?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

[ESLint](https://github.com/eslint/eslint) et [stylelint](https://github.com/stylelint/stylelint) sont des outils vraiment incroyables qui vous permettent d'imposer des modèles de codage parmi vos équipes. Cela présente de nombreux avantages, comme la production d'un code meilleur et plus cohérent, l'élimination des diffs inutiles dans les commits (nouvelle ligne, indentation, etc.) parmi beaucoup d'autres.

Mais avec le temps, cela peut s'avérer un peu fastidieux parmi les développeurs d'une équipe, qui trouvent que c'est un fardeau mental supplémentaire d'ajouter manuellement des points-virgules, des nouvelles lignes, des indentations, etc. juste pour se conformer aux règles de lint. C'est là qu'un outil de formatage de code comme [Prettier](https://github.com/prettier/prettier) entre en jeu.

Prettier peut être configuré pour formater automatiquement votre code selon certaines règles spécifiées. Si vous utilisez VSCode, vous pouvez même avoir votre code formaté chaque fois que vous enregistrez (je suis sûr qu'il existe des moyens de configurer cela dans d'autres éditeurs mais je ne l'ai pas vérifié.)

Cependant, vous ne voulez pas créer un nouveau fichier de configuration Prettier, puisque vous avez déjà toutes les règles de formatage spécifiées dans vos fichiers de configuration ESLint et stylelint. Donc, nous aurons besoin d'un peu de magie pour cela. ✨

Plongeons maintenant dans un guide étape par étape de la façon de configurer tout cela, et aussi comment formater tout votre code existant selon les règles de lint. Ce guide suppose que votre projet a déjà ESLint et stylelint configurés avec leurs fichiers `.eslintrc` et `.stylelintrc`.

### PARTIE 1 : Formater la base de code existante

#### **Étape 1**

Installez [prettier-eslint](https://github.com/prettier/prettier-eslint), qui est un outil qui formate votre JavaScript en utilisant Prettier suivi de `eslint --fix`. Le `--fix` est une fonctionnalité d'ESLint qui tente de corriger automatiquement certains problèmes pour vous.

```
npm install --save-dev prettier-eslint
```

Cet outil déduit les options de configuration équivalentes de Prettier à partir de votre fichier _.eslintrc_ existant. Donc, vous ne devriez pas avoir besoin de créer un nouveau fichier _.prettierrc_ dans la plupart des cas.

#### **Étape 2**

Installez [prettier-eslint-cli](https://github.com/prettier/prettier-eslint-cli). Il s'agit de l'outil CLI qui vous aidera à exécuter tous vos fichiers à travers prettier-eslint en une seule fois.

```
npm install --save-dev prettier-eslint-cli
```

#### **Étape 3**

Installez [prettier-stylelint](https://github.com/hugomrdias/prettier-stylelint), qui est un outil qui formate votre CSS/SCSS avec Prettier suivi de `stylelint --fix`. Comme ESLint, `--fix` est une fonctionnalité de stylelint qui tente de corriger automatiquement certains problèmes pour vous.

```
npm install prettier-stylelint --save-dev
```

Cet outil _essaie également_ de créer une configuration Prettier basée sur la configuration stylelint.

Notez que contrairement à prettier-eslint, vous n'avez pas à installer un autre package pour son CLI puisque cela est déjà inclus.

#### **Étape 4**

Écrivez des scripts dans votre `package.json` ciblant les fichiers existants dans votre base de code que vous souhaitez exécuter à travers prettier-eslint et prettier-stylelint.

```
"scripts": {
```

```
  "fix-code": "prettier-eslint --write 'src/**/*.{js,jsx}' ",
```

```
  "fix-styles": "prettier-stylelint --write 'src/**/*.{css,scss}' "
```

```
}
```

Comme vous pouvez le voir, je cible tous mes fichiers JS et JSX existants et tous mes fichiers CSS et SCSS existants, respectivement.

Le drapeau `--write` écrit les modifications en place pour le fichier actuellement en cours de formatage. Donc, soyez prudent et **assurez-vous que tous vos fichiers existants sont sous contrôle de source et qu'il n'y a pas de modifications non validées**.

#### **Étape 5**

Exécutez les scripts !

```
npm run fix-codenpm run fix-styles
```

Maintenant, vous pouvez valider toutes ces nouvelles modifications en un seul grand commit (peut-être même à partir d'un utilisateur git temporaire, si vous ne voulez pas polluer votre propre historique git.)

### **Partie 2 : Configurer VSCode**

Maintenant que votre base de code existante est formatée, il est temps de s'assurer que tout le code écrit à partir de maintenant est formaté automatiquement.

#### **Étape 1**

Installez les extensions Prettier, ESLint et stylelint pour VSCode :

[**Prettier - Code formatter - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
[_Extension for Visual Studio Code - VS Code plugin for prettier/prettier_marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)[**ESLint - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
[_Extension for Visual Studio Code - Integrates ESLint JavaScript into VS Code._marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)[**stylelint - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=shinnn.stylelint)
[_Extension for Visual Studio Code - Modern CSS/SCSS/Less linter_marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=shinnn.stylelint)

#### **Étape 2**

Configurez quelques paramètres VSCode :

`"prettier.eslintIntegration": true` — indique à Prettier d'utiliser prettier-eslint au lieu de Prettier

`"prettier.stylelintIntegration": true` — indique à Prettier d'utiliser prettier-stylelint au lieu de Prettier

`"eslint.autoFixOnSave": false` — nous n'avons pas besoin qu'ESLint corrige notre code directement pour nous, puisque prettier-eslint exécutera `eslint --fix` pour nous de toute façon.

`"editor.formatOnSave": true` — exécute Prettier avec les options ci-dessus à chaque sauvegarde de fichier, afin que vous n'ayez jamais à invoquer manuellement la commande de formatage de VSCode.

De plus, vous pouvez valider les paramètres de l'espace de travail ci-dessus dans le contrôle de source afin qu'il soit plus facile pour les autres membres de l'équipe de configurer leurs éditeurs. Vous pouvez le faire en créant un dossier `.vscode` à la racine de votre projet et en mettant toutes les règles ci-dessus dans un fichier `settings.json`.

Facultativement, vous pouvez dire à Prettier d'ignorer le formatage de certains motifs de fichiers. Pour ce faire, ajoutez simplement un fichier `.prettierignore` à la racine de votre projet en spécifiant les chemins à ignorer. Par exemple :

```
strings.json
scripts/*
```

**Et c'est tout ! Ne vous inquiétez plus jamais du style de code ?**

Cet article n'a pas pour but d'être un guide exhaustif, mais plutôt une introduction à ce qui est possible avec les outils incroyables mentionnés ici. Je recommande d'ouvrir les pages officielles GitHub de chacun pour en savoir plus sur la façon d'utiliser ces outils plus efficacement pour votre flux de travail spécifique.

Veuillez écrire un commentaire ci-dessous pour toute aide, suggestion, etc.

#### _Références_

https://prettier.io/docs/en/
https://stylelint.io/user-guide/
https://eslint.org/
https://github.com/prettier/prettier-vscode
https://github.com/prettier/prettier-eslint
https://github.com/prettier/prettier-eslint-cli
https://github.com/hugomrdias/prettier-stylelint
https://www.youtube.com/watch?v=YIvjKId9m2c