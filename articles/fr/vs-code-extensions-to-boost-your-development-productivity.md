---
title: Extensions VS Code qui stimuleront votre productivité de développement
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-12-28T14:50:40.000Z'
originalURL: https://freecodecamp.org/news/vs-code-extensions-to-boost-your-development-productivity
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/vscode.jpg
tags:
- name: Productivity
  slug: productivity
- name: Visual Studio Code
  slug: vscode
- name: Web Development
  slug: web-development
seo_title: Extensions VS Code qui stimuleront votre productivité de développement
seo_desc: 'Having a good text or code editor that fits into your workflow is crucial
  to productivity as a developer. VS Code comes stocked with a lot of features by
  default, but here are 7 extensions that will help take your workflow up another
  level.


  What is ...'
---

Avoir un bon éditeur de texte ou de code qui s'intègre à votre flux de travail est crucial pour la productivité en tant que développeur. VS Code est livré avec de nombreuses fonctionnalités par défaut, mais voici 7 extensions qui vous aideront à faire passer votre flux de travail à un niveau supérieur.

* [Qu'est-ce que VS Code ?](#heading-quest-ce-que-vs-code)
* [Extensions VS Code](#heading-extensions-vs-code)
* [Importateur de Mappage Clavier et Paramètres Sublime Text](#heading-importateur-de-mappage-clavier-et-parametres-sublime-text)
* [Import Cost](#heading-import-cost)
* [indent-rainbow](#heading-indent-rainbow)
* [Rainbow Brackets](#heading-rainbow-brackets)
* [Settings Sync](#heading-settings-sync)
* [Profile Switcher](#heading-profile-switcher)
* [Better Comments](#heading-better-comments)
* [Duplicate Action](#heading-duplicate-action)

%[https://www.youtube.com/watch?v=OIWVJj9yRbA]

## Qu'est-ce que VS Code ?

Une rapide note au cas où vous ne seriez pas familier. [VS Code](https://code.visualstudio.com/), qui est l'abréviation de Visual Studio Code, est un éditeur de texte ou de code populaire maintenu par l'équipe Microsoft.

Il a gagné une part énorme du marché des développeurs au cours des dernières années, en faisant l'éditeur de référence pour les développeurs web.

Couplé au fait que Microsoft investit beaucoup de temps dans son développement et que des développeurs indépendants créent un grand nombre d'extensions, vous ne pouvez pas vous tromper en l'essayant.

## Extensions VS Code

Ce qui rend VS Code génial, c'est son extensibilité. Il permet aux développeurs de faire passer l'éditeur à un niveau supérieur en implémentant des fonctionnalités que Microsoft pourrait ne pas vouloir supporter, ou même en construisant une expérience complète de prise de notes avec [Foam](https://foambubble.github.io/foam/).

Bien qu'il y ait des milliers d'extensions disponibles dans le [VS Code Marketplace](https://marketplace.visualstudio.com/vscode), voici les 7 qui sont essentielles à mon flux de travail en tant que développeur actif.

## Importateur de Mappage Clavier et Paramètres Sublime Text

Avant de passer à VS Code, j'étais un utilisateur de Sublime Text 3. C'est toujours un excellent éditeur de texte, mais en passant à VS Code, beaucoup de raccourcis et de mappages de touches n'étaient pas les mêmes.

L'Importateur de Mappage Clavier et Paramètres Sublime Text m'a permis d'abord d'importer mes paramètres de Sublime Text, mais il a également configuré les mappages de touches par défaut. Cela a rendu les raccourcis disponibles dans Sublime immédiatement disponibles dans VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-sublime-keyboard-shortcuts.gif)
_Mappages de touches Sublime Text dans VS Code_

Cela inclut deux de mes préférés comme la multi-sélection (sélectionner quelque chose puis appuyer sur CMD+D / Ctrl+D) et la duplication d'une ligne (ajouter un curseur sur une ligne et appuyer sur CMD+Shift+D / Ctrl+Shift+D).

[Importateur de Mappage Clavier et Paramètres Sublime Text](https://marketplace.visualstudio.com/items?itemName=ms-vscode.sublime-keybindings) (marketplace.visualstudio.com)

## Import Cost

Les développeurs modernes doivent constamment gérer des dépendances provenant de diverses sources. Alors que nous intégrons un tas de code différent pour construire notre projet, ce code supplémentaire a un coût.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-import-cost.jpg)
_Affichage de la taille de l'import dans VS Code_

[Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) calcule une estimation de la taille d'un import, nous permettant de voir combien de poids supplémentaire nous ajouterions à la taille de notre projet avec cette dépendance ajoutée.

Cela nous aide à reconnaître la taille de nos dépendances, évitant ainsi la surcharge accidentelle de bibliothèques énormes qui pourraient impacter les performances et nuire à l'expérience utilisateur de nos clients.

[Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) (marketplace.visualstudio.com)

## indent-rainbow

Le style est un facteur important pour rendre notre code lisible. Une partie de ce style est la façon dont nous indentons notre code, afin de comprendre la imbrication des différents blocs de code.

Le problème est que parfois cette imbrication peut devenir assez grande et il peut être difficile de trouver à quelle balise d'ouverture appartient quelle balise de fermeture.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-indent-rainbow.jpg)
_Espacement d'indentation en couleur arc-en-ciel dans VS Code_

[indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) ajoute des couleurs aux espaces d'indentation, nous permettant de facilement aligner et voir quelles balises appartiennent les unes aux autres.

[indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) (marketplace.visualstudio.com)

## Rainbow Brackets

Similaire à l'indentation, le code complexe, en particulier lors de l'utilisation de mathématiques, peut créer des lignes de code facilement confuses lorsque vous avez plusieurs utilisations de parenthèses dans la même instruction.

Par exemple, si nous voulons appliquer quelques mathématiques simples :

```
const value = (((1+1)*2)+1)*2;

```

Et bien que ce soit un exemple simple, cela peut facilement devenir ingérable et difficile à suivre.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-rainbow-brackets.jpg)
_Parenthèses en couleur arc-en-ciel dans VS Code_

[Rainbow Brackets](https://marketplace.visualstudio.com/items?itemName=2gua.rainbow-brackets) met en évidence les parenthèses dans différentes couleurs, nous permettant de mieux comprendre à quelle parenthèse ouvrante appartient quelle parenthèse fermante de notre équation.

[Rainbow Brackets](https://marketplace.visualstudio.com/items?itemName=2gua.rainbow-brackets) (marketplace.visualstudio.com)

## Settings Sync

Si vous travaillez généralement entre deux ordinateurs portables ou deux environnements différents, vous devrez peut-être maintenir manuellement votre éditeur de texte de la même manière, si vous êtes particulier sur votre configuration (comme je le suis).

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-settings-sync.jpg)
_Configuration pour Settings Sync dans VS Code_

[Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) vous permet de sauvegarder vos paramètres VS Code dans un GitHub Gist. Cela vous permet de synchroniser ces paramètres entre différentes installations de VS Code.

[Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) (marketplace.visualstudio.com)

_Note : si vous voulez en savoir plus, [j'ai écrit un tutoriel](https://www.freecodecamp.org/news/how-to-sync-vs-code-settings-between-multiple-devices-and-environments/) qui vous guide à travers la configuration étape par étape !_

## Profile Switcher

En tant que créateur de contenu, je dois m'assurer que lorsque je montre mon écran aux autres, j'utilise des couleurs accessibles et des tailles de police qui permettent aux gens de voir facilement ce que je démontre.

Le problème est que ces paramètres ne sont pas ceux que j'aime utiliser au quotidien lorsque je suis concentré sur le codage.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-profile-switcher.jpg)
_Changement de profils dans VS Code_

[Profile Switcher](https://marketplace.visualstudio.com/items?itemName=aaronpowell.vscode-profile-switcher) vous permet de configurer plusieurs profils VS Code, chacun avec sa propre configuration, vous permettant de basculer facilement entre différentes configurations.

[Profile Switcher](https://marketplace.visualstudio.com/items?itemName=aaronpowell.vscode-profile-switcher) (marketplace.visualstudio.com)

## Better Comments

Bien qu'ils ne semblent pas importants lorsque vous écrivez du code, les commentaires sont cruciaux pour aider les autres à comprendre ce code. Ils vous aident également généralement à le comprendre lorsque vous le regardez un an plus tard.

Ces commentaires sont utiles, mais ils peuvent être difficiles à lire, car ils sont généralement tous d'une seule couleur grise qui ne se distingue pas nécessairement.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-better-comments.jpg)
_Mise en évidence des mots-clés des blocs de commentaires dans VS Code_

C'est là que [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) entre en jeu, qui ajoute une sorte de coloration syntaxique aux commentaires, ajoutant de la couleur aux mots-clés et aux instructions qui améliore la lisibilité de vos commentaires de code.

[Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) (marketplace.visualstudio.com)

## Duplicate Action

Cette dernière semble être une petite chose, mais pour une raison quelconque, VS Code ne vient pas avec la capacité de faire un clic droit sur un fichier et de le dupliquer par défaut.

Lorsque je suis concentré sur le code, je duplique généralement un fichier, comme un modèle existant, ce qui me permet de ne changer que le contenu. Cela rend la création d'une nouvelle page plus productive.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-duplicate-action.jpg)
_Option de duplication de fichier ou de répertoire dans VS Code_

[Duplicate Action](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-duplicate) ajoute simplement l'option Dupliquer le Fichier ou le Dossier au menu contextuel lorsque vous faites un clic droit sur un fichier ou un dossier.

[Duplicate Action](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-duplicate) (marketplace.visualstudio.com)

## Quelle est votre extension préférée ?

Il existe une tonne d'extensions qui font des choses incroyables – quelle est votre préférée ? Faites-le moi savoir en [partageant avec moi sur Twitter](https://twitter.com/colbyfayock) !

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">🐦 Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">📺 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">📧 Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">💝 Sponsor Me</a>
    </li>
  </ul>
</div>