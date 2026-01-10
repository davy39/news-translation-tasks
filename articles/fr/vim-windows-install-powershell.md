---
title: Guide d'installation de Vim sur Windows – Comment exécuter l'éditeur de texte
  Vim dans PowerShell sur votre PC
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-05-06T17:21:00.000Z'
originalURL: https://freecodecamp.org/news/vim-windows-install-powershell
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b34740569d1a4ca2a64.jpg
tags:
- name: vim
  slug: vim
- name: Windows 10
  slug: windows-10
seo_title: Guide d'installation de Vim sur Windows – Comment exécuter l'éditeur de
  texte Vim dans PowerShell sur votre PC
seo_desc: 'Vim is a powerful code editor. So powerful that both Linux and Mac have
  it installed by default.

  But if you are using Windows as your operating system, you will need to install
  Vim separately.

  Fortunately, Microsoft makes it very easy to install Vim ...'
---

Vim est un éditeur de code puissant. Tellement puissant que Linux et Mac l'ont installé par défaut.

Mais si vous utilisez Windows comme système d'exploitation, vous devrez installer Vim séparément.

Heureusement, Microsoft facilite grandement l'installation de Vim et son exécution sur votre PC.

## Comment télécharger Vim

Vous pouvez [télécharger la dernière version de l'éditeur de texte Vim directement depuis le site officiel de Vim](https://www.vim.org/download.php).

Ils ont conçu un programme d'installation auto-exécutable spécial qui vous guide à travers le processus d'installation de Vim au bon endroit sur votre disque dur.

## Comment installer Vim

Notez que pour Windows, vous téléchargerez techniquement quelque chose appelé gVim, qui est une version de Vim incluant une interface graphique de base (GUI). Vous pouvez [l'installer en téléchargeant ce programme d'installation exécutable](https://ftp.nluug.nl/pub/vim/pc/gvim82.exe).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_005-1.png)
_Une capture d'écran de ce que vous verrez lorsque vous tenterez d'ouvrir le fichier. Comme il s'agit d'un fichier .exe, Windows vous demandera d'abord votre autorisation._

Une fois le fichier téléchargé, il vous suffit de l'exécuter, et vous verrez un assistant d'installation convivial qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_004.png)
_Une capture d'écran de l'assistant que vous verrez lors de la première exécution du programme d'installation de Vim_

Ils proposent une installation "typical" recommandée. Mais si vous avez un disque dur raisonnablement grand, il n'y a aucun mal à installer tout en choisissant l'option "full" :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_003.png)
_Une capture d'écran de l'installateur Vim où vous pouvez choisir les composants de Vim que vous souhaitez installer._

## Comment exécuter Vim dans PowerShell

Ensuite, une fois Vim installé, vous devriez pouvoir le lancer depuis votre invite de commande Windows. 

Notez qu'en 2020, PowerShell possède toutes les mêmes fonctionnalités que CMD, et bien plus encore. Je recommande d'utiliser PowerShell pour tout.

Vous pouvez ouvrir PowerShell depuis la barre de menu Windows en tapant "powershell" dans le champ de recherche de la barre de démarrage.

Windows ouvrira PowerShell, et vous obtiendrez une invite de commande qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_001.png)
_Une capture d'écran de l'invite Windows PowerShell._

Une fois dans PowerShell, voici comment exécuter Vim lui-même. Tout ce que vous avez à faire est de taper "vim" et d'appuyer sur Entrée. Cela ouvrira Vim. Une fois Vim ouvert, voici ce que vous devriez voir :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/signal-attachment-2020-05-07-144326_002.png)
_Une capture d'écran de Vim lorsque vous l'ouvrez pour la première fois._

Félicitations – vous avez maintenant installé Vim.

## Comment exécuter Vim dans VS Code

Si vous utilisez déjà VS Code et que vous voulez profiter de la rapidité de Vim sans perdre les fonctionnalités de VS Code, j'ai une bonne nouvelle. Il est possible de vivre une expérience de type Vim directement dans VS Code.

[Voici un plugin Vim pour VS Code](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim) qui vous aidera à faire cela. Au moment où j'écris ces lignes, ce plugin a été installé près de 2 millions de fois.

## Comment apprendre à utiliser Vim correctement

Vim est un éditeur de code puissant, et il vous faudra beaucoup de pratique pour vous sentir à l'aise avec lui. 

Voici quelques tutoriels Vim qui vous aideront vraiment à saisir rapidement les bases et à faire voler vos doigts sur le clavier en un rien de temps.

Pour commencer, l'une des différences entre Vim et les autres éditeurs de code est que Vim possède des "modes". Voici [tous les modes de Vim expliqués, avec des exemples](https://www.freecodecamp.org/news/vim-editor-modes-explained/).

Vim peut être intimidant. Il y a tellement de choses à apprendre. Mais ce guide vous montrera [comment ne plus avoir peur de Vim](https://www.freecodecamp.org/news/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae/).

Si vous utilisez déjà VS Code et que vous souhaitez passer complètement à Vim, [cet article vous expliquera comment faire](https://www.freecodecamp.org/news/vim-for-people-who-use-visual-studio-code/).

Et [voici 7 astuces Vim qui ont changé la vie du fondateur de #100DaysOfCode, Alex Kallaway](https://www.freecodecamp.org/news/7-vim-tips-that-changed-my-life/). Dans cet article, il ne se contente pas de les expliquer, mais propose des démonstrations de ces astuces en action.

## Vim : Apprenez-le, vivez-le, aimez-le.

Au cours des 30 années écoulées depuis que Bram Moolenaar a créé Vim, son influence s'est largement répandue. Et même aujourd'hui, le projet Vim est activement maintenu et s'améliore constamment.

J'ai rencontré tellement de développeurs au fil des ans qui ne jurent que par Vim.

J'espère que ce guide vous a aidé à faire fonctionner Vim sur votre PC Windows. Et j'espère que ces autres tutoriels que j'ai partagés ici vous aideront à passer de zéro à cent dans les mois à venir.

La clé est de continuer à pratiquer et de ne pas se laisser décourager par le nombre de raccourcis Vim à mémoriser. Finalement, tout cela deviendra une mémoire musculaire, et vous passerez d'un fichier à l'autre, enchaînant les lignes de code comme un terminator.

Il n'y a pas de sensation aussi cool que de pouvoir plonger dans une base de code et de commencer immédiatement à apporter des modifications sans même toucher à une souris ou un pavé tactile. C'est la puissance que Vim promet, et elle la tient largement.