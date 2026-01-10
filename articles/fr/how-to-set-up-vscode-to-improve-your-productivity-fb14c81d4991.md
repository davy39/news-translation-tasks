---
title: Comment configurer VSCode pour améliorer votre productivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T17:03:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-vscode-to-improve-your-productivity-fb14c81d4991
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cgkkTflpK9s3jL1yb1Jygw.png
tags:
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment configurer VSCode pour améliorer votre productivité
seo_desc: 'By Chiamaka Ikeanyi

  Code editors have evolved over the years. A few years ago, there was no Visual Studio
  Code (VS Code). You were probably using Sublime Text, Atom, Bracket, etc. But with
  the release of VS Code, it has become the favourite code edit...'
---

Par Chiamaka Ikeanyi

Les éditeurs de code ont évolué au fil des ans. Il y a quelques années, Visual Studio Code (VS Code) n'existait pas. Vous utilisiez probablement Sublime Text, Atom, Bracket, etc. Mais avec la sortie de VS Code, il est devenu l'éditeur de code préféré de la plupart des développeurs.

### Pourquoi VS Code ?

Les développeurs l'adorent parce que

* Il est personnalisable
* Débogage facile
* Emmet
* Extensions
* Intégration Git
* Terminal intégré
* Intellisense
* Thèmes et plus encore...

Maintenant que vous avez vu les avantages de l'utilisation de VS Code, cet article couvrira la configuration de VS Code et les extensions nécessaires lors de l'utilisation de VS Code pour une productivité maximale.

### Terminal

Vous pouvez [configurer votre terminal](https://chiamakaikeanyi.dev/how-to-configure-your-macos-terminal-with-zsh-like-a-pro/) pour utiliser iTerm2 et ZSh et configurer votre terminal VS Code pour l'utiliser.

Après avoir configuré Zsh, lancez le terminal intégré de VS Code `Terminal > New Terminal` et exécutez la commande

```
source ~/.zshrc
```

ou

```
. ~/.zshrc
```

pour exécuter le contenu du fichier de configuration .zshrc dans le shell.

### Police

[FiraCode](https://github.com/tonsky/FiraCode) a l'air cool grâce à la prise en charge des ligatures. Téléchargez et installez FiraCode, puis ajoutez-le à votre fichier `settings.json`.

![Image](https://cdn-media-1.freecodecamp.org/images/vqdv5dokMCcD5yivbaPUBTtYsWBiUIMo6gZ6)

```
"editor.fontFamily": "Fira Code",
"editor.fontLigatures": true,
```

### Lancement depuis la ligne de commande

Lancer VS Code depuis le terminal, c'est cool. Pour ce faire, appuyez sur CMD + SHIFT + P, tapez **shell command** et sélectionnez **Install code command in path**. Ensuite, accédez à n'importe quel projet depuis le terminal et tapez `**code .**` depuis le répertoire pour lancer le projet en utilisant VS Code.

### Configuration

Les configurations de VS Code non spécifiques à un espace de travail sont logées dans le fichier settings.json. Vous pouvez configurer VS Code pour qu'il corresponde à vos préférences.

Pour lancer le fichier settings.json, appuyez sur

```
CMD + ,
```

Copiez et collez le code ci-dessous dans le fichier settings.json :

```
{    "editor.multiCursorModifier": "ctrlCmd",    "editor.formatOnPaste": true,    "editor.wordWrap": "bounded",    "editor.trimAutoWhitespace": true,    "editor.fontFamily": "Fira Code",    "editor.fontLigatures": true,    "editor.fontSize": 14,    "editor.formatOnSave": true,    "files.autoSave": "onFocusChange",    "emmet.syntaxProfiles": {        "javascript": "jsx"    },    "eslint.autoFixOnSave": true,    "eslint.validate": [        "javascript",        "javascriptreact"    ],    "javascript.validate.enable": true,    "git.enableSmartCommit": true,    "files.trimTrailingWhitespace": true,    "editor.tabSize": 2,    "gitlens.historyExplorer.enabled": true,    "diffEditor.ignoreTrimWhitespace": false,    "workbench.sideBar.location": "right",    "explorer.confirmDelete": false,    "javascript.updateImportsOnFileMove.enabled": "always",}
```

### Extensions

Voici des extensions utiles qui peuvent améliorer votre expérience de développeur lors du travail sur une base de code.

Pour accéder à ces extensions,

* Allez dans `View -> Extensions`
* Recherchez des extensions dans le marketplace
* Cliquez sur Installer

#### 1. Auto Import

Avec cette extension, vous n'avez pas besoin d'importer manuellement les fichiers. Si vous travaillez sur un projet basé sur des composants, il vous suffit de taper le nom du composant et il sera automatiquement importé.

![Image](https://cdn-media-1.freecodecamp.org/images/d88RTDvyIzGWYC5BuLcnIaFOjHiyDMaqE5Bh)

#### 2. Add jsdoc comments

Cela ajoute un bloc de commentaires au code. Pour l'utiliser, surlignez la première ligne de la fonction, appuyez sur `CMD + SHIFT + P` et sélectionnez **_Add Doc Comments._**

![Image](https://cdn-media-1.freecodecamp.org/images/jlJk05MHt3HknnqZyKQB-8d1Oj7qgh7ZOBGL)

#### 3. ESDoc MDN

Dans certains scénarios, nous avons tendance à oublier comment fonctionne une chose particulière. C'est là que cette extension devient utile. Vous n'avez pas besoin de lancer votre navigateur web pour découvrir la syntaxe. Tout ce dont vous avez besoin est de taper

```
//mdn [object].[method];
```

![Image](https://cdn-media-1.freecodecamp.org/images/r8pUHOgNQwAyNq0DU9VPcL5xb8zGgT1ybCZV)

#### 4. CSS Peek

Comme son nom l'indique, cela vous aide à voir les règles appliquées par un style défini dans une base de code et sa [spécificité](https://chiamakaikeanyi.dev/css-specificity). Cela s'avère utile lors du travail sur des bases de code héritées.

![Image](https://cdn-media-1.freecodecamp.org/images/7orGFqwr8mdQPOVPuQVMTlRO8XtPgnR0Ggmj)

#### 5. GitLens

GitLens améliore ce que vous pouvez accomplir avec Git. Il vous aide à faire beaucoup plus, comme explorer facilement les dépôts Git, voir les révisions de code, l'auteur et bien plus encore.

![Image](https://cdn-media-1.freecodecamp.org/images/Sf2hWdpXSF7CPBhmQ9sTf9zGPD-OiXQsf2aM)

#### 6. ESLint

Cela intègre ESLint dans VS Code pour vérifier vos codes. Le projet sur lequel vous travaillez doit avoir ESLint installé soit localement soit globalement pour profiter des fonctionnalités offertes par cette extension.

Pour installer ESLint localement, exécutez

```
npm install eslint
```

ou globalement en utilisant

```
npm install -g eslint
```

Vous devrez également créer un fichier de configuration `.eslintrc`. Si vous avez installé ESLint localement, exécutez

```
./node_modules/.bin/eslint --init
```

ou

```
eslint --init
```

pour une installation globale.

#### 7. Debugger for Chrome

Cela vous permet de déboguer votre code JavaScript directement depuis le navigateur Google Chrome

![Image](https://cdn-media-1.freecodecamp.org/images/O4SSLTXtEEdU3AjZODIdUKG7AYao27y6O7jq)

#### 8. Google Fonts

L'ajout de polices Google est devenu plus facile avec cette extension. Vous n'avez plus besoin de rechercher des polices dans le navigateur. Pour accéder à une liste de polices, appuyez sur `CMD + SHIFT + P` et recherchez **_Google fonts_** pour continuer.

![Image](https://cdn-media-1.freecodecamp.org/images/sqVCRBo5mlEUjIFcSsp28oEo4ugo3LMXjKoS)

#### 9. TODO Highlight

Avec beaucoup de travail à faire et à prioriser, parfois vous pouvez tendre à oublier les tâches non encore terminées. TODO highlight les rend facilement visibles en les mettant en évidence.

#### 10. Docker

Vous pouvez créer des Dockerfiles à la volée avec cette extension. Elle fournit également la coloration syntaxique, l'intellisense et bien plus encore.

Appuyez sur CMD + SHIFT + P et recherchez _Add Docker files to workspace._

![Image](https://cdn-media-1.freecodecamp.org/images/Yv09L4W8lraVLXLr-aYpCHz8hfLC-tuORELa)

#### 11. Code Spellchecker

Cela s'avère utile pour identifier les erreurs typographiques dans la base de code.

#### 12. Import Cost

Import Cost montre l'impact des packages importés dans le code. Il aide à mesurer les goulots d'étranglement de performance.

![Image](https://cdn-media-1.freecodecamp.org/images/4Xl2OdUzPmPFW54eqzrHz59Kg9qSFbCDxUWf)

#### 13. HTMLHint

Cette extension valide votre HTML, vous aidant à écrire un [code conforme aux normes](https://chiamakaikeanyi.dev/writing-standards-compliant-html/).

![Image](https://cdn-media-1.freecodecamp.org/images/ZJN4LadCSa6e1EVHlEMs7gB1f4AVINChBxaY)

#### **14. Peacock**

Cette extension vous donne la possibilité de changer la couleur de votre espace de travail. Elle est idéale lorsque vous avez plusieurs instances de VS Code et que vous souhaitez identifier rapidement une instance particulière.

![Image](https://cdn-media-1.freecodecamp.org/images/BRiUh7NQh1PdVW7aP5mZJcnbzZFaCQcblYpq)

Après avoir installé Peacock, cliquez sur l'icône des paramètres > paramètres, sélectionnez l'onglet des paramètres de l'espace de travail, cliquez sur {} et collez le code ci-dessous.

```
{    "workbench.colorCustomizations": {        "activityBar.background": "#e90b8d",        "activityBar.foreground": "#fff",        "activityBar.inactiveForeground": "#b5b5b5",    },    "peacock.affectedElements": [        "activityBar",    ]}
```

Vous pouvez également ajouter `titleBar` et `statusBar` aux éléments affectés et ajouter des personnalisations de couleur pour eux dans la section colorCustomizations.

Pour utiliser l'une des couleurs par défaut, appuyez sur CMD + SHIFT + P, tapez **peacock** et sélectionnez votre thème préféré. Cela remplace les paramètres de couleur dans le fichier settings.json défini pour cet espace de travail.

#### **15. Prettier**

Appuyez-vous toujours sur la barre d'espace ou la touche de tabulation lors du codage ? Voici Prettier pour vous sauver. Il formate les lignes de code et les rend lisibles.

Découvrez [les choses incroyables que vous pouvez faire avec Visual Studio Code](https://vscodecandothat.com/) ici.

N'hésitez pas à laisser ce qui fonctionne pour vous dans la section des commentaires et à partager cet article.

Consultez également [mon blog](https://chiamakaikeanyi.dev) pour plus d'articles.