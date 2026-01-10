---
title: VS Code Performance – Comment optimiser Visual Studio Code et choisir les "meilleures"
  extensions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-19T18:01:39.000Z'
originalURL: https://freecodecamp.org/news/optimize-vscode-performance-best-extensions
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/banner-1.png
tags:
- name: editor
  slug: editor
- name: performance
  slug: performance
- name: Productivity
  slug: productivity
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: VS Code Performance – Comment optimiser Visual Studio Code et choisir les
  "meilleures" extensions
seo_desc: "By Rob O'Leary\nVisual Studio Code (VS Code) is designed to be lightweight.\
  \ It has a tight set of core features, and you can add extra features through extensions.\
  \  \nBut performance will inevitably be affected as your collection of extensions\
  \ grows. \n..."
---

Par Rob O'Leary

Visual Studio Code (VS Code) est conçu pour être léger. Il dispose d'un ensemble restreint de fonctionnalités principales, et vous pouvez ajouter des fonctionnalités supplémentaires via des extensions. 

Mais les performances seront inévitablement affectées à mesure que votre collection d'extensions grandit. 

Évaluez-vous les performances d'une extension avant de l'installer ? Que faites-vous si le démarrage de VS Code ralentit ? D'après l'absence de personnes écrivant sur ce sujet, je suppose que les gens ne savent pas.

Dans cet article, je vais expliquer les facteurs qui affectent les performances d'une extension. Je vais également évaluer les performances de certaines extensions populaires. Ensuite, je vais décrire comment vous pouvez auditer les performances de votre suite d'extensions existante, et donner quelques conseils généraux sur les performances.

## Configuration matérielle et logicielle minimale

Avant de parler des extensions, parlons brièvement des exigences minimales pour exécuter VS Code. 

Un ordinateur acheté ces dernières années avec des spécifications modestes devrait pouvoir exécuter VS Code sans aucun problème. 

### Matériel

Le matériel minimal que je recommande est :

- Un processeur de 1,6 GHz ou plus rapide ;
- Au moins 1 Go de RAM ;
- Au moins 200 Mo d'espace disque.

### Systèmes d'exploitation

VS Code a été testé sur les systèmes d'exploitation suivants :

- OS X Yosemite et versions ultérieures.
- Windows 7 (avec .NET Framework 4.5.2), 8.0, 8.1 et 10 (32 bits et 64 bits).
- Linux (Debian) : Ubuntu Desktop 14.04, Debian 7.
- Linux (Red Hat) : Red Hat Enterprise Linux 7, CentOS 7, Fedora 23.

### Versions communautaires non officielles pour Raspberry Pi et Chromebooks

Jay Rodgers a publié un projet open source qui effectue des [versions nocturnes de VS Code pour Raspberry Pi et Chromebooks](http://code.headmelted.com/). 

> J'ai maintenu le projet depuis quelques années maintenant et il s'est étendu de la fourniture de binaires pour Pi à la fourniture de support et d'outils pour faire fonctionner VS Code sur des appareils ARM bas de gamme qui pourraient ne pas le supporter autrement, comme les Chromebooks (qui représentent environ 60 % des appareils dans les écoles maintenant). 
> 
> Si vous voulez l'essayer vous-même, vous pouvez suivre les instructions qu'il a établies. Il a fait beaucoup de travail pour le rendre aussi simple que possible. 


## Toutes les extensions ne se valent pas

![parodie de l'inégalité des extensions](https://www.freecodecamp.org/news/content/images/2020/10/blind-judgment.jpg)
<small>Modification de "Lady Justice aux yeux bandés" par [Tingey Injury Law Firm](https://unsplash.com/@tingeyinjurylawfirm?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/equal?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)</small>

Les extensions sont chargées et déchargées sous différentes conditions. L'auteur de l'extension décide de cela. Cela est spécifié via les *Événements d'Activation*, que nous aborderons plus tard. 

Il n'y a aucun retour dans l'éditeur indiquant si une extension est active ou non. Alors, comment savons-nous quand une extension est active ?

La plupart des extensions sont écrites en TypeScript, mais elles peuvent également être écrites en JavaScript. Les extensions peuvent inclure des modules Node comme dépendances. 

Vous pouvez regrouper et minifier vos fichiers sources en un seul fichier si vous le souhaitez. La [Documentation VS Code](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) recommande de faire cela pour améliorer les temps de chargement, mais de nombreuses extensions ne le font pas. Ces choix affectent leurs performances.

Les extensions sont principalement des projets open source secondaires écrits par des développeurs. La qualité du code variera. La maintenance du code variera. 

Les extensions écrites par Microsoft ne sont pas immunisées contre ces défauts, mais elles sont moins susceptibles d'en souffrir.

## Critères pour sélectionner une extension

La plupart des listes d'extensions parlent des fonctionnalités sympas, et peu d'autres choses. Si quelque chose est génial, parlez-moi aussi un peu du carburant et des fumées. ???

Certains des critères que je suggère impliquent de regarder le code source. Ne soyez pas rebuté par cela. Pour recueillir les faits clés, cela ne prend que quelques minutes. Je vais vous montrer comment !

1. **La fonctionnalité dont j'ai besoin est-elle déjà disponible dans VS Code ?**

   J'ai démontré que vous n'avez pas besoin de nombreuses extensions populaires dans un article ["VS Code : vous n'avez pas besoin de cette extension"](https://roboleary.net/vscode/2020/08/05/dont-need-extensions.html). Vous pouvez consulter la [documentation VS Code](https://code.visualstudio.com/Docs) pour vérifier une fonctionnalité particulière. 

2. **L'extension a-t-elle les fonctionnalités dont j'ai besoin ?**

   Consultez la page de l'extension sur Visual Studio Marketplace pour le découvrir.

3. **Quand une extension est-elle chargée et active ?**

   Je vais en discuter en détail dans la section [Événements d'Activation](#heading-installation). Vous devez vérifier le *package.json* du code source pour le découvrir à l'avance. 
   
   Vous pouvez exécuter la commande **Developer: Startup Performance** pour voir les Événements d'Activation des extensions installées. Je discute de cela plus en détail dans la section [Comment auditer les performances.](#how-to-audit-performance) 

4. **Les ressources sont-elles optimisées ?**  

   Vous devez vérifier le code source pour voir s'il utilise un bundler. Vous pouvez vérifier le *package.json* pour voir si la section *scripts* a une étape de pré-construction pour le bundling.

   Le fichier d'extension VSIX est une archive compressée de fichiers pour le code et la liste dans la marketplace. Les développeurs incluent souvent des fichiers inutiles. Il existe un fichier *.vscodeignore* pour exclure des fichiers. 

   Le nombre de fichiers que le VSIX contient a un impact sur le temps d'activation à froid. Le temps d'activation à froid est la première exécution de l'extension après son installation. Il tend à être plus lent que les autres fois. Je suppose que c'est parce que le VSIX est décompressé et mis en cache. 

   Voici à quoi ressemble l'extension [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur) lorsque vous l'ouvrez dans [7Zip](https://www.7-zip.org/).
   
![vetur VSIX ouvert dans 7zip](https://www.freecodecamp.org/news/content/images/2020/10/vetur-7zip.png)

5. **Y a-t-il eu des problèmes de performance signalés récemment, qui ne sont pas résolus ?**

   Vous pouvez découvrir ces problèmes en auditant les performances de l'extension. Vous devez vérifier les problèmes sur le dépôt Git également.

6. **Le code a-t-il des tests ?**

   L'extension sera plus susceptible aux bugs sans tests. Vous devez vérifier le code source pour voir s'il y a des tests.

7. **Est-elle activement maintenue ?**

   La section *Détails du Projet* de la page de l'extension donne un aperçu de l'activité du dépôt Git public. Dans certains cas, une extension peut être "terminée", donc la maintenance n'est pas une considération importante.

![Détails du Projet de la Page Marketplace](https://www.freecodecamp.org/news/content/images/2020/10/marketplace-maintenance.png)

## Événements d'Activation

Les Événements d'Activation sont des événements qui déclenchent l'activation d'une extension. Ils définissent les conditions de chargement et de déchargement d'une extension.

L'auteur d'une extension déclare cela dans le champ `activationEvents` du `package.json` ([Manifest de l'Extension](https://code.visualstudio.com/api/references/extension-manifest)). 

Il existe une gamme d'Événements d'Activation parmi lesquels choisir. Une extension peut écouter de nombreux Événements d'Activation pour obtenir une portée plus spécifique. 

Voici un Diagramme de Séquence de ce qui se passe lorsque vous lancez VS Code. Il vous donne une idée de la chronologie des événements qui se produisent, ce qui affecte quand vous pouvez interagir avec l'éditeur et utiliser certaines extensions.

[![lancement de VS Code](https://www.freecodecamp.org/news/content/images/2020/10/activation-events-2.svg)](https://cdn.imgpaste.net/2020/10/19/IDOqm.png)

Maintenant, je vais passer en revue les Événements d'Activation les plus importants. Je vais commencer par la portée la plus large, et continuer jusqu'à atteindre la portée la plus étroite. 

### Événement de démarrage

L'Événement d'Activation `*` activera une extension lorsque VS Code démarre. Ces extensions seront **toujours actives**. Cela impacte le temps de démarrage de VS Code.

```json
"activationEvents": [
    "*"
]
```

La documentation VS Code donne le conseil suivant :

> Pour garantir une excellente expérience utilisateur, veuillez utiliser cet événement d'activation dans votre extension uniquement lorsque aucune autre combinaison d'événements d'activation ne fonctionne dans votre cas d'utilisation.

À mon avis, il doit y avoir un cas spécial pour accorder à une extension cette portée. Il est préférable d'utiliser au moins `onStartUpFinished`.

**Extensions Populaires avec cet Événement d'Activation** : [ES Lint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) (11M installations), [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) (7,4 installations), [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) (6,5M installations), [Beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify) (5,4M installations), [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer) (3,6M installations), [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) (2,9M installations), [Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) (2M installations), [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) (1,1M installations).

### Événement onStartupFinished

Cette extension sera activée **quelque temps après le démarrage de VS Code**. Cela ressemble à l'événement d'activation `*`, mais il ne ralentira pas le démarrage de VS Code.

```json
"activationEvents": [
    "onStartupFinished"
]
```

**Extensions Populaires avec cet Événement d'Activation** : [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) (8,5M installations).

### Événement onLanguage

Cette extension sera activée chaque fois qu'un fichier d'un certain langage est ouvert.

```json
"activationEvents": [
    "onLanguage:json",
    "onLanguage:markdown",
    "onLanguage:typescript"
]
```

L'événement `onLanguage` prend une valeur d'[identifiant de langage](https://code.visualstudio.com/docs/languages/identifiers). Vous pouvez déclarer autant de langages que vous le souhaitez.

**Extensions Populaires avec cet Événement d'Activation** : La plupart des extensions dans la catégorie ["Langages de Programmation"](https://marketplace.visualstudio.com/search?target=VSCode&category=Programming%20Languages&sortBy=Installs) dans la Marketplace Visual Studio Code ont une entrée *onLanguage* ainsi que d'autres Événements d'Activation, [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur) (5,6M installations - actif pour *Vue* uniquement), [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) (4,3M installations - actif pour *YAML* uniquement), [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) (1,1M installations - actif pour les langages supportés uniquement).


### Événement workspaceContains

Cette extension sera activée chaque fois que vous ouvrez un dossier qui contient au moins un fichier correspondant à un motif glob.

```json
"activationEvents": [
    "workspaceContains:**/package.json"
]
```

### Événement onCommand

Cette extension sera activée chaque fois que vous invoquez une commande.

```json
"activationEvents": [
        "onCommand:vscode-docker.compose.down",
        "onCommand:vscode-docker.compose.restart",
        "onCommand:vscode-docker.compose.up",
        ...
]
```

### Autres Événements d'Activation

Vous pouvez lire la [liste complète des Événements d'Activation](https://code.visualstudio.com/api/references/activation-events) dans la documentation de référence.

### Les extensions définissent-elles une portée spécifique de manière cohérente ?

Non !

Trop d'extensions utilisent l'Événement d'Activation `*`.

Voici comment je noterais la définition de la portée de certaines des extensions que j'ai utilisées :

- **Le Bon** : [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur), [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml), [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments).
- **Le Mauvais** : 
  -  [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) : Il serait préférable de cibler uniquement les langages qu'il supporte.
  - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) : Il est actif lorsqu'un fichier markdown est ouvert, ou que l'espace de travail contient un README.md. Ce dernier me semble inutile.
- **Le Mauvais** : Toutes les extensions avec l'Événement d'Activation `*` mentionné ci-dessus.

## Quel impact le bundling peut-il avoir sur les performances d'une extension ?

![bundling d'un burger](https://www.freecodecamp.org/news/content/images/2020/10/burger-bundle.jpg)
<small>Modification de la photo sans titre par [Pablo Merchán Montes](https://unsplash.com/@pablomerchanm?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/burger?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)</small>

Cela peut avoir un grand impact !

John Papa en parle dans son article "[Votre extension VS Code est-elle lente ? Voici comment l'accélérer !](https://dev.to/azure/is-your-vs-code-extension-slow-heres-how-to-speed-it-up-4d66)". 

Il révèle les résultats d'une révision de 2 extensions de Microsoft :

1. [Azure Account](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account&wt.mc_id=devto-blog-jopapa) : Le bundling a réduit le temps d'activation de 50 %. La taille de l'extension a été réduite de 6,2 Mo à 840 Ko grâce au bundling et à l'exclusion de plus de fichiers (dans le fichier *.vscodeignore*).
2. [Docker](https://marketplace.visualstudio.com/items?itemName=PeterJausovec.vscode-docker&wt.mc_id=devto-blog-jopapa) : Le bundling a réduit le temps d'activation de 3,5 secondes à moins de 2 secondes. De plus, une considération est le temps d'activation à froid, qui tend à être plus lent que les autres fois (temps d'activation à chaud). Le temps d'activation à froid est passé de 20 secondes à 2 secondes. 

Vous pouvez améliorer votre extension préférée en soulevant ce problème avec l'auteur de l'extension. Le [Guide Utilisateur du Bundling des Extensions](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) explique comment.

## Comment auditer les performances

Vous pouvez exécuter la commande **Developer: Show Running Extensions** pour obtenir les statistiques de base sur les extensions en cours d'exécution. Elle trie les extensions du temps d'activation le plus long au plus court. Le temps est intitulé "Startup Activation" si l'extension est chargée au démarrage.

Comme vous pouvez le voir sur la capture d'écran, elle donne également des avertissements sur les problèmes de performance.

![extensions en cours d'exécution](https://www.freecodecamp.org/news/content/images/2020/10/running-extensions.png)

Comme mentionné précédemment, il est important de noter que le temps d'activation à froid (la première fois qu'une extension est exécutée) et le temps d'activation à chaud (deuxième exécution et suivantes) peuvent varier considérablement. Pour cette raison, vous devriez baser les performances typiques d'une extension sur une deuxième exécution.

Vous pouvez auditer les performances de démarrage en exécutant la commande **Developer: Startup Performance**. Elle ouvre un document avec des statistiques détaillées sur des sujets tels que : les informations système, les marques de performance, les statistiques d'activation des extensions, les statistiques de chargement des modules, et plus encore. 

![informations système sur les performances de démarrage](https://www.freecodecamp.org/news/content/images/2020/10/startup-performance1.png)

Les résultats sont spécifiques au projet actuel et à tous les fichiers ouverts lorsque vous exécutez la commande.

La section *Extension Activation Stats* donne un aperçu plus détaillé des performances des extensions. Elle est très utile pour voir les *Activation Events* sans avoir besoin de vérifier le code source d'une extension.

![performances de démarrage](https://www.freecodecamp.org/news/content/images/2020/10/startup-performance.png)

Vous pouvez voir que VS Code charge ses propres extensions "core" pour Git, Emmet, et quelques autres au démarrage également. ? Vous ne voulez pas que la liste des extensions chargées au démarrage devienne trop longue !

## Fiche d'évaluation pour certaines des extensions les plus populaires

Je me concentre ici sur les extensions que j'ai utilisées moi-même. Je ne veux pas spéculer sur les extensions que je n'ai pas vraiment utilisées.

### ESLint

[ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) est l'outil d'analyse statique le plus populaire pour JavaScript et TypeScript. Il met en évidence les problèmes dans l'éditeur avec des lignes rouges en zigzag. 

- **Auteur** : Microsoft.
- **Nombre d'installations** : 11 millions.
- **Note sur la Marketplace** : 4,3/5 (156).
- **Fonctionnalités principales** : Signalement des problèmes de syntaxe. Capacité à corriger automatiquement certains problèmes.
- **Événements d'Activation** : Au démarrage (`*`). Il peut être changé en `onStartupFinished` dans la prochaine version. Voir [cet problème ouvert](https://github.com/microsoft/vscode-eslint/issues/1068) pour l'explication de pourquoi ce choix a été fait.
- **Les ressources sont-elles optimisées** : Oui.
- **Taille du fichier** : 133 Ko.
- **Temps d'activation sur mon système** : 39 ms.
- **Suite de tests** : Semble être très basique. Juste un test mineur des motifs glob.
- **Maintenu activement** : Oui.
- **Extensions alternatives** : [JS Hint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.jshint), [TS Lint](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-tslint-plugin).

ESLint est une extension solide. Les performances sont excellentes. 

Il est décevant qu'il soit chargé au démarrage. Si cela vous dérange, vous pouvez essayer [JS Hint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.jshint) (écrit par le même développeur) pour JavaScript, et [TS Lint](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-tslint-plugin) pour TypeScript. Ou vous pouvez forker le projet et le changer vous-même !

Il est activement maintenu. Il ne dispose pas d'une suite de tests significative.

**Note : 8/10**

### Prettier - Formateur de Code

[Prettier](https://prettier.io/) est un formateur de code opinionné. Il supporte actuellement les langages suivants : JavaScript, TypeScript, Flow, JSX, JSON, CSS, SCSS, Less, HTML, Vue, Angular, GraphQL, Markdown, YAML. 

- **Auteur** : Prettier.
- **Nombre d'installations** : 8,5 millions.
- **Note sur la Marketplace** : 3,8/5 (204).
- **Fonctionnalités principales** : Formatage du code.
- **Événements d'Activation** : `onStartupFinished`.
- **Les ressources sont-elles optimisées** : Oui.
- **Taille du fichier** : 2,1 Mo.
- **Temps d'activation sur mon système** : 286 ms.
- **Suite de tests** : Oui. La couverture semble décente.
- **Maintenu activement** : Oui.
- **Extensions alternatives** : [Beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify).

Prettier fait un excellent travail pour simplifier le formatage du code.

Les performances sont correctes, mais peut-être pourraient-elles être améliorées. Il est du côté lent du spectre d'activation.

La portée d'activation est très large. Il serait préférable de cibler uniquement les langages supportés. J'ai rencontré un problème avec le formatage Markdown, donc je ne l'utilise pas pour formater le Markdown actuellement. Ce sont des choses qui peuvent être changées facilement.

**Note : 7,5/10.**

### Live Server

[Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) lance un serveur de développement local pour donner un aperçu en direct de vos fichiers HTML et SVG. 

- **Auteur** : Retwick Dey.
- **Nombre d'installations** : 7,5 millions.
- **Note sur la Marketplace** : 4,5/5 (269).
- **Fonctionnalités principales** : Aperçu en direct HTML et SVG.
- **Événements d'Activation** : Au démarrage (`*`).
- **Les ressources sont-elles optimisées** : Non.
- **Taille du fichier** : 2,5 Mo.
- **Temps d'activation sur mon système** : 2513 ms.
- **Suite de tests** : Oui. Tests basiques.
- **Maintenu activement** : Non. Le dernier commit date d'il y a un an. L'auteur de l'extension cherche un nouveau mainteneur.
- **Extensions alternatives** : Je n'en ai pas trouvé !

Quand cela fonctionne, c'est une extension pratique à utiliser. 

Les performances sont médiocres et elle n'est plus maintenue. 

Je recommanderais de devenir le mainteneur et de la remettre en forme. Ou de trouver une autre extension pour le travail.

**Note : 5/10.**

### GitLens

[GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) aide à visualiser l'attribution du code et à explorer les dépôts Git.

- **Auteur** : Eric Amodio.
- **Nombre d'installations** : 6,5 millions.
- **Note sur la Marketplace** : 4,86/5 (387)
- **Fonctionnalités principales** : Visualisation de l'attribution du code en un coup d'œil. Riches vues de la barre latérale des dépôts git.
- **Événements d'Activation** : Au démarrage (`*`).
- **Les ressources sont-elles optimisées** : Oui.
- **Taille du fichier** : 1,5 Mo.
- **Temps d'activation sur mon système** : 35 ms.
- **Suite de tests** : Non.
- **Maintenu activement** : Oui, mais l'activité récente est faible. Le dernier commit date de 4 mois.
- **Extensions alternatives** : Aucune.

GitLens est une bonne idée et peut être utile pour obtenir des informations sur une base de code. 

Il est bien écrit et les performances sont excellentes.

Je n'ai utilisé l'extension que pour les annotations de blame, mais il y a beaucoup de fonctionnalités et d'options de configuration (135 paramètres individuels !).

Il y a des paramètres pour activer chacune des fonctionnalités, ce qui est une très bonne approche. Vous pouvez activer et désactiver le codelens facilement.

Il y a eu un ralentissement de l'activité récemment. Je ne sais pas si c'est une situation temporaire ou non. Donc, il est difficile de dire à quel point les extensions seront supportées à l'avenir. L'auteur a des détails pour le soutenir.

**Note : 9/10.**

### Vetur

Support de langage Vue.

- **Auteur** : Pine Wu.
- **Nombre d'installations** : 5,6 millions.
- **Note sur la Marketplace** : 4,5/5 (117)
- **Fonctionnalités principales** : Colorisation syntaxique. Intellisense. Formatage de code.
- **Événements d'Activation** : `onLanguage: vue`.
- **Les ressources sont-elles optimisées** : Non.
- **Taille du fichier** : 70,6 Mo.
- **Temps d'activation sur mon système** : 252 ms. Cependant, la statistique "Finish Activate" est de 3943 ms !
- **Suite de tests** : Oui.
- **Maintenu activement** : Oui.
- **Extensions alternatives** : Aucune alternative évidente. Le formatage peut être fait avec Prettier.

Vetur est l'extension de référence pour développer des applications Vue dans VS Code. 

La colorisation syntaxique, l'intellisense et les références de survol sont excellents à avoir pour le développement Vue. 

La taille de l'extension est ÉNORME. 

Les performances sont un peu erratiques. Il faut au moins 4 secondes sur ma machine pour terminer l'activation, ce qui est beaucoup plus long que les fonctionnalités de langage *JavaScript* intégrées. Il y a également un délai notable pour l'autocomplétion de la syntaxe JavaScript.

Les développeurs travaillent actuellement sur le bundling de l'extension dans [cet problème](https://github.com/vuejs/vetur/pull/2301), donc espérons qu'il y aura une amélioration des performances bientôt. ?

**Note : 7/10.**

### Settings Sync

[Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) synchronise les paramètres en utilisant GitHub Gist.

- **Auteur** : Shan Khan.
- **Nombre d'installations** : 2 millions.
- **Note sur la Marketplace** : 4,61/5 (638)
- **Fonctionnalités principales** : Synchronisation des paramètres.
- **Événements d'Activation** : Au démarrage (`*`).
- **Les ressources sont-elles optimisées** : Oui.
- **Taille du fichier** : 1,2 Mo.
- **Temps d'activation sur mon système** : 2513 ms. 
- **Suite de tests** : Oui.
- **Maintenu activement** : Non. Le dernier commit date d'il y a un an.
- **Extensions alternatives** : Ceci est une [fonctionnalité intégrée dans VS Code](https://code.visualstudio.com/docs/editor/settings-sync).

C'était une extension remarquable. Synchroniser votre configuration complète de l'éditeur sur plusieurs machines est super utile.

Depuis juillet 2020, la même fonctionnalité est une fonctionnalité intégrée dans VS Code pour cette même chose. La principale différence est que cette extension sauvegarde vos paramètres dans un gist, que vous avez la possibilité de partager avec d'autres également. 

Le temps d'activation est assez lent. Est-ce justifiablement lent ? C'est difficile à dire. 

Je suppose que la fonctionnalité intégrée fera un meilleur travail éventuellement car elle a le soutien de Microsoft. L'extension semble ne plus être supportée.

**Note : 8/10.**

### Markdown All in One

[Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) répond à de nombreux besoins en markdown.

- **Auteur** : Yu Zhang.
- **Nombre d'installations** : 1,7 million.
- **Note sur la Marketplace** : 4,8/5 (90)
- **Fonctionnalités principales** : Édition en mode toggle. Table des matières. 
- **Événements d'Activation** :  `onLanguage: markdown`, `onCommand: markdown.extension.printToHtmlBatch`, `workspaceContains: README.md`.
- **Les ressources sont-elles optimisées** : Oui.
- **Taille du fichier** : 4,1 Mo.
- **Temps d'activation sur mon système** : 195 ms. 
- **Suite de tests** : Oui.
- **Maintenu activement** : Oui.
- **Extensions alternatives** : [Marky Markdown](https://marketplace.visualstudio.com/items?itemName=robole.marky-markdown).

C'est une extension solide et les performances sont excellentes.

Elle a trop de fonctionnalités à mon goût. Pour beaucoup de gens, il est attrayant d'avoir tout ce qu'ils peuvent vouloir dans une seule extension.

L'Événement d'Activation `workspaceContains: README.md` semble être une inclusion inutile pour moi. La plupart de mes projets ont un README, mais je les édite rarement. Donc pour moi, c'est comme avoir l'extension toujours active. 

La logique pour la table des matières est un peu inhabituelle. Elle avait des problèmes de faux positifs dans le passé. Je ne sais pas si cela a été complètement résolu.

La taille du fichier de l'extension peut être réduite en excluant les captures d'écran du README du package de l'extension.

**Note : 8/10.**

## Conseils généraux sur les performances

### Utiliser un OS 64 bits

Si vous passez à une version 64 bits d'un OS, vous pouvez étendre la quantité de mémoire virtuelle (VM) disponible pour VS Code de 2 Go à 4 Go. 

Cela permet à VS Code de gérer des charges de travail significativement plus grandes lorsque la VM est requise.

### Désactiver la restauration de l'état du projet au démarrage

VS Code restaure automatiquement l'état du projet de la session précédente. Cela peut prolonger le temps nécessaire pour charger un projet. 

Vous pouvez désactiver certains des paramètres de restauration pour accélérer le temps de chargement :

- `Workbench • Editor: Restore View State` : Activé par défaut.
- `Files: Restore Undo Stack` : Activé par défaut.
- `Workbench: Startup Editor` : Contrôle quel éditeur est affiché au démarrage. Le défaut est `welcome page`. Vous pouvez le définir sur `none` pour empêcher tout éditeur d'apparaître au démarrage.

### Désactiver les fonctionnalités coûteuses qui impactent les performances d'édition

- **Minimap** : `Editor • Minimap: Enabled`. Activé par défaut.
- **Retour à la ligne** : `Editor: Word Wrap`. Désactivé par défaut.
- **CodeLens** : `Editor: CodeLens`. Activé par défaut.
- **Formatage à l'enregistrement** : `Editor: Format On Save`. Désactivé par défaut.
- **Formatage au collage** : `Editor: Format On Paste`. Désactivé par défaut.

### Désactiver les extensions pour un espace de travail

Vous pouvez désactiver une extension pour un espace de travail (projet).

![désactiver l'extension pour l'espace de travail](https://www.freecodecamp.org/news/content/images/2020/10/disable-extension-workspace.png)

Vous allez probablement vouloir faire cela pour les extensions qui s'exécutent toujours. Pour un projet Java, vous n'allez pas avoir besoin d'ESLint ! 

Vous pouvez également adopter l'approche inverse. Vous pouvez désactiver une extension globalement, et ne l'activer que pour un nombre sélectionné de projets.

### Créer des ensembles d'extensions

Vous pouvez spécifier un répertoire alternatif pour les extensions à partir de la ligne de commande comme ci-dessous.

```bash
code --extensions-dir <dir>
```

Ainsi, si vous souhaitez utiliser différents ensembles d'extensions, vous pouvez. Vous pouvez ajouter un raccourci sur le bureau pour cela, ou un alias pour l'exécuter régulièrement à partir de la ligne de commande.

Une chose à garder à l'esprit est la synchronisation. Si vous synchronisez vos extensions entre les machines, vous pouvez vouloir exclure les extensions de la synchronisation. Sinon, vous pourriez accidentellement perturber votre dossier lorsque vous changez.

Idéalement, vous ne devriez pas avoir besoin de faire cela.

### Désactiver toutes les extensions pour une session

Vous pouvez démarrer VS Code avec toutes les extensions utilisateur désactivées à partir de la ligne de commande. Mode zen plus plus !

```bash
code --disable-extensions
```

## Résolution des problèmes de performance

### Expérience de lenteur ou d'un écran vide

VS Code a des problèmes avec l'accélération matérielle GPU (unité de traitement graphique) sur certains systèmes. Vous pouvez vérifier si c'est le cas en désactivant l'accélération GPU.

````bash
code --disable-gpu
````

Pour définir cela de manière permanente, procédez comme suit : 

- Ouvrez la Palette de Commandes (Ctrl+Shift+P).
- Exécutez la commande **Preferences: Configure Runtime Arguments**.
- Cette commande ouvrira un fichier `argv.json` pour configurer les arguments d'exécution. Vous pourriez voir certains arguments par défaut déjà présents.
- Ajoutez `"disable-hardware-acceleration": true`.
- Redémarrez VS Code.

### L'installation semble être corrompue avec le message [Unsupported]

VS Code effectue une vérification en arrière-plan lorsqu'il démarre pour vérifier si vous avez modifié l'un de ses fichiers sources. Si c'est le cas, vous verrez le texte **[Unsupported]** dans la barre de titre. 

Une cause de ce problème peut être un logiciel antivirus. VS Code pourrait avoir été mis en quarantaine par erreur, ou des fichiers pourraient avoir été supprimés par le logiciel antivirus (voir le problème [#94858](https://github.com/microsoft/vscode/issues/94858)). Vérifiez les paramètres de votre logiciel antivirus pour éviter cela. 

Pour résoudre cette situation, vous pouvez [réinstaller VS Code](https://code.visualstudio.com/download). Cela remplacera les fichiers modifiés et fera taire l'avertissement.

## Mots de la fin

Vous ne devriez pas avoir à compromettre les performances pour obtenir les fonctionnalités dont vous avez besoin. 

L'approche la plus pragmatique est d'ajouter progressivement les extensions dont vous avez besoin. Faites un peu de recherche à chaque fois et testez l'extension. Et avant de vous en rendre compte, vous aurez un portfolio impressionnant d'extensions.