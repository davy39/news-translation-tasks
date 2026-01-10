---
title: Pourquoi Vim est bien plus qu'un simple éditeur – Langage Vim, mouvements et
  modes expliqués
subtitle: ''
author: Simon Späti
co_authors: []
series: null
date: '2023-02-14T19:52:55.000Z'
originalURL: https://freecodecamp.org/news/vim-language-and-motions-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/using-neo-vim-feature-freecode-3.jpg
tags:
- name: editor
  slug: editor
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: vim
  slug: vim
seo_title: Pourquoi Vim est bien plus qu'un simple éditeur – Langage Vim, mouvements
  et modes expliqués
seo_desc: 'Throughout my time as a developer, I''ve used VS Code, Sublime, Notepad++,
  TextMate, and others. But shortcuts like cmd(+shift)+end and jumping with option+arrow-keys
  from word to word needed to be faster at some point.

  I was hitting my limits. Everyt...'
---

Tout au long de ma carrière de développeur, j'ai utilisé VS Code, Sublime, Notepad++, TextMate, et bien d'autres. Mais les raccourcis comme `cmd(+shift)+end` et les sauts avec `option+arrow-keys` d'un mot à l'autre devaient être plus rapides à un moment donné.

J'avais atteint mes limites. Tout ce que je faisais, je le faisais assez rapidement, mais je ne devenais pas plus rapide.

J'ai depuis appris que Vim est le seul éditeur avec lequel vous devenez plus rapide avec le temps.

[Vim](https://www.vim.org/) est basé uniquement sur des raccourcis. Quand j'ai découvert cela et que j'ai un peu joué avec, je me suis senti engourdi et un peu stupide de ne pas avoir appris les raccourcis (appelés langage Vim) plus tôt dans ma carrière.

J'ai réalisé qu'il y avait une touche pour atteindre n'importe quelle position spécifique où je voulais sauter. C'était comme un jeu, voir si je pouvais utiliser moins de raccourcis pour accomplir une édition particulière. C'est là que beaucoup d'utilisateurs de Vim trouvent beaucoup de plaisir à coder et à écrire. C'était libérateur, déplacer mon curseur avec la précision d'un chirurgien.

Bien que la vitesse soit un avantage mineur, c'est ce qui m'a fait commencer quand j'ai vu [d'autres](https://youtu.be/1UXHsCT18wE) naviguer dans Vim. Après avoir surmonté la courbe d'apprentissage abrupte, c'est toujours l'une des compétences les plus puissantes que j'ai jamais apprises dans ma carrière, travaillant pour gagner ma vie sur un ordinateur.

Démystifions le mythe de Vim et apprenons comment il est possible de retenir tous les raccourcis en utilisant le langage spécifique de Vim. Nous verrons comment nous déplacer avec les mouvements de Vim, et je partagerai ce que j'ai appris jusqu'à présent, et pourquoi vous pourriez aussi donner une chance à Vim.

## Apprendre le langage Vim

Beaucoup de choses ont été dites sur Vim – à quel point il est rapide, comment seuls les nerds de Linux l'utilisent, et qu'il est impossible de [quitter Vim](https://stackoverflow.com/q/11828270).

Pour ma part, je suis tombé amoureux du « langage Vim ». Vous voyez, je suis mauvais pour retenir quoi que ce soit et je pensais que Vim n'était pas fait pour moi. Mais ce n'était pas le cas pour une raison spécifique : les *mouvements* de Vim et son langage.

J'ai appris qu'il y avait une grammaire derrière l'éditeur. Avec celle-ci, vous exprimez ce que vous voulez faire en premier, combien de fois, et ensuite ce à quoi vous voulez l'appliquer.

Approfondissons Vim et le langage qui se cache derrière.

### Comment fonctionne le langage Vim et les mouvements

Vim possède un langage ou une grammaire fantastique derrière ses raccourcis. Au lieu de retenir mille raccourcis, vous pouvez en apprendre quelques-uns et les combiner.

Cela s'appelle souvent le langage Vim ou les mouvements Vim pour se déplacer. Cela n'a rien à voir avec l'éditeur pour l'instant – ceux-ci sont universels et disponibles dans d'autres éditeurs également.

Par exemple, il y a [VSVim](https://marketplace.visualstudio.com/items?itemName=JaredParMSFT.VsVim) pour VSCode, [IdeaVim](https://plugins.jetbrains.com/plugin/164-ideavim) pour les produits JetBrains, [Vintage Mode](https://www.sublimetext.com/docs/vintage.html) pour Sublime, et ainsi de suite. Mais il y a aussi des extensions de navigateur comme [Vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en) ou [Firenvim](https://chrome.google.com/webstore/detail/firenvim/egpjdkipkomnmjhjmdamaniclmdlobbo?hl=en), et Gmail a même adapté certains des [raccourcis](https://support.google.com/mail/answer/6594?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cjumping%2Cnavigation) de Vim pour la navigation (`j`, `k` pour se déplacer, `g` pour sauter).

Toute personne qui tape sur un ordinateur huit heures par jour devrait apprendre le langage Vim. Oui, c'est difficile au début, mais c'est le cas avec tout ce qui est nouveau et différent. Mais s'améliorer chaque jour et s'amuser davantage à coder ou à écrire devrait être une motivation suffisante. Vous n'êtes pas trop occupé pour apprendre - vous apprendrez en cours de route.

![Êtes-vous trop occupé pour vous améliorer | Image du blog de Steen Schledermann : https://steenschledermann.wordpress.com/](https://www.sspaeti.com/blog/why-using-neovim-data-engineer-and-writer-2023/weel-too-busy.png align="left")

#### Grammaire Vim

Tout comme la grammaire d'une langue parlée a des verbes, des sujets et des objets, il en va de même pour le langage Vim. La grammaire a différents **verbes** pour commencer. Copier (ou yank en anglais) dans Vim avec `y`, supprimer avec `d`, coller avec `p`, changer avec `c`, et ainsi de suite.

Par exemple, le raccourci le plus simple est de copier une ligne avec `yy`. Dans ce cas, yank est le verbe et le second `y` est un synonyme de `y_`. Le `y` est doublé, ce qui le rend plus facile à taper car c'est une opération conjointe.

Ensuite, nous pouvons ajouter des mouvements. Chaque verbe prend un **sujet** pour leurs mouvements. Il y a beaucoup de mouvements (plus dans la section suivante) – le plus simple est avec des nombres.

Par exemple, pour copier trois lignes, vous ajoutez un 3 devant, comme `3yy`. Vous pouvez faire cela avec tous les verbes, comme supprimer trois lignes avec `3dd`. Un autre exemple serait `{` et `}` pour se déplacer au début ou à la fin du paragraphe, respectivement.

En plus des verbes et des sujets, le langage Vim a aussi des **objets**. Par exemple, nous pouvons sauvegarder du texte dans différents presse-papiers (appelés registre dans Vim) avec `"ay`. Ici, nous le copions dans le registre a, qui serait l'objet. Nous pouvons le coller à nouveau en faisant la même chose mais en utilisant le verbe coller au lieu de yank `"ap`.

Il y a même des **adjectifs** et des **adverbes** avec des préfixes. Habituellement, vous utilisez un verbe et un objet. Mais au lieu de descendre de trois lignes avec `3J`, qui joint les trois lignes suivantes, vous pourriez ajouter `d5}`, ce qui signifie « supprimer de la ligne actuelle jusqu'à la fin du cinquième paragraphe en dessous d'ici ».

Pour moi, la chose la plus magique à propos de Vim est la façon dont vous naviguez et éditez du texte – et cela n'a toujours rien à voir avec l'éditeur.

Bien sûr, Vim a été le premier à introduire et à perfectionner ces actions, mais encore une fois – vous pouvez les obtenir ailleurs. Cela va profondément dans le langage Vim, mais nous devons encore aborder l'éditeur. C'est important à savoir.

J'espère que vous avez commencé à voir la puissance de tels motifs, cependant. Avec quelques verbes et objets, vous pouvez déjà connaître des centaines de combinaisons sans mémoriser chacune individuellement.

Vous pouvez regarder une vidéo sur [Maîtriser le langage Vim](https://youtu.be/wlR5gYd6um0) ou lire une exposition complète du langage Vim sur ce commentaire terrifique de [StackOverflow](https://stackoverflow.com/a/1220118).

### Mouvements Vim

Les mouvements Vim sont la façon dont vous naviguez, que vous alliez à la fin d'un mot ou retour au début du document – ce sont tous des mouvements.

Ce sont les premières choses que vous commencez à apprendre (et à détester) lorsque vous apprenez Vim. Ils sont extra difficiles à comprendre au début, mais ce sont des choses que vous voudrez utiliser partout une fois que vous vous y serez habitué.

Au lieu d'utiliser les touches fléchées, Vim utilise `jk` pour descendre et monter et `hl` pour aller à gauche et à droite. L'idée principale est d'utiliser les touches sur lesquelles votre main droite se repose naturellement. Vous n'avez pas besoin de bouger vos mains ou même vos doigts pour la navigation.

Encore une fois, cela semble être une petite chose, mais une fois que vous l'avez appris, vous savez pourquoi tout le monde vous en parle.

Quelques mouvements courants sont :

```python
h,j,k,l - gauche, bas, haut, droite
w,W - au début du mot ou MOT suivant
b,B - au début du mot ou MOT précédent
e,E - à la fin du mot ou MOT
$   - à la fin de la ligne
^   - au début de la ligne
```

Vous pouvez trouver les mouvements les plus importants pour commencer dans cette feuille de triche :

![Feuille de triche des commandes Vim de Cloud Guru](https://www.sspaeti.com/blog/why-using-neovim-data-engineer-and-writer-2023/vim-language-cheetsheet.png align="left")

Cette feuille de triche des commandes Vim provient de [Cloud Guru](https://www.pluralsight.com/resources/blog/cloud/a-vim-cheat-sheet-reference-guide).

## Comment utiliser les modes Vim (normal, insertion, visuel et commande)

Les modes sont une autre chose qui pourrait vous confondre au début.

Lorsque vous lancez Vim, vous ne tapez pas ce que vous cliquez sur votre clavier car vous n'êtes pas en mode « insertion » auquel vous êtes probablement habitué avec d'autres éditeurs. Au lieu de cela, le mode normal dans lequel vous vous trouvez vous permet d'exécuter les commandes expliquées dans le langage Vim et les mouvements ci-dessus.

Vim est le seul éditeur qui **optimise l'édition de texte** au lieu d'écrire à partir d'une page blanche.

![Trois modes illustrés (le mode escape étant le mode commande) | Image de Geekforgeeks https://www.geeksforgeeks.org/vi-editor-unix/](https://www.sspaeti.com/blog/why-using-neovim-data-engineer-and-writer-2023/vim-modes.png align="left")

C'est une autre raison pour laquelle Vim vous rend si efficace : vous avez différents modes pour chaque phase de votre travail ou tâche actuelle.

* Le mode normal est pour lire le code et naviguer rapidement.

* Le mode insertion est pour quand vous voulez ajouter du code ou du texte.

* Le mode visuel est unique, comme surligner du texte avec la souris, mais avec les mouvements Vim ci-dessus.

* Et le mode commande est la centrale électrique, où vous pouvez taper des commandes Linux telles que formater un fichier JSON avec `:%!jq` (où [jq](https://stedolan.github.io/jq/) est un outil de ligne de commande installé sur votre machine) et les exécuter dans Vim. C'est aussi là que vous pouvez utiliser des commandes Vim telles que `:sort` pour trier vos fichiers.

Je pourrais continuer ici, mais je veux maintenant plonger dans l'éditeur lui-même et explorer pourquoi je l'ai appris initialement et comment commencer.

## Introduction à Vim l'éditeur (Neovim, Lunarvim et Helix)

Alors, qu'est-ce que Vim l'éditeur ? Tout a commencé avec le simple éditeur vi, un éditeur de base qui implémente le langage Vim et peut éditer du texte. C'est un peu comme Notepad++, que vous pourriez utiliser sur Windows, mais sans souris ni menu contextuel.

Vim est simplement une version améliorée de Vi avec plus de fonctionnalités.

![Différences entre Vi et Vim | Image par Linuxiac : https://linuxiac.com/differences-between-vi-and-vim-text-editors-explained/](https://www.sspaeti.com/blog/why-using-neovim-data-engineer-and-writer-2023/vi-vs-vim.png align="left")

Aujourd'hui, il existe même une nouvelle version de Vim appelée [Neovim](https://neovim.io/). Cette version est super populaire, et j'ai aussi commencé à utiliser Neovim. Comparé à Vim, Neovim utilise [Lua](https://www.lua.org/), un vrai langage de programmation, pour configurer et étendre l'éditeur. Cela rend l'écriture de plugins et la configuration de Neovim plus faciles comparé au [Vimscript](https://learnvimscriptthehardway.stevelosh.com/) natif de Vim.

Neovim est un excellent point de départ pour apprendre Vim aujourd'hui, car il dispose de nombreux plugins géniaux. Neovim a également remporté le titre d'IDE le plus [aimé](https://survey.stackoverflow.co/2022/#integrated-development-environment) sur l'enquête StackOverflow à plusieurs reprises, la dernière fois en 2022.

Il existe également un éditeur appelé [Helix](https://github.com/helix-editor/helix) construit en Rust, mais il présente de légères déviations par rapport au langage Vim, ce qui en fait un endroit moins optimal pour commencer.

Si vous souhaitez commencer sans avoir besoin de connaître quoi que ce soit sur Neovim et sans passer des heures sur les configurations, vous pouvez commencer avec [LunarVim](https://www.lunarvim.org/). Il s'agit d'une distribution avec toutes les fonctionnalités que vous connaissez déjà de VS Code incluses.

Si vous êtes à l'aise avec le terminal et que vous réalisez que vous voulez modifier l'éditeur à votre guise, vous pouvez commencer votre voyage avec une [configuration simple en un seul fichier](https://github.com/nvim-lua/kickstart.nvim) avec de nombreuses explications qui fonctionnera dès la sortie de la boîte. Vous pouvez également apprendre chaque configuration en ouvrant le fichier de configuration unique.

## Pourquoi j'ai appris Vim

En utilisant la méthode d'entrée standard que nous utilisons dans nos éditeurs quotidiennement, nous finissons par stagner à un certain niveau. Bien sûr, vous pouvez utiliser `cmd+arrow-keys` (sur un Mac) pour sauter au début d'une ligne ou `option+arrow-keys` pour sauter entre les mots au lieu des caractères.

Mais que se passe-t-il une fois que vous avez maîtrisé cela ? Et si vous devez changer quelque chose au milieu d'une phrase ? Il n'y a pas d'autre moyen de sauter plusieurs fois avec cette option, ou vous éloignez vos mains à chaque fois pour atteindre la souris et cliquer sur l'endroit exact.

Un jour, j'ai vu un collègue travailler dans Vim, et tout a fait sens. Le langage Vim et les mouvements étaient les choses dont j'avais besoin depuis le début. J'ai donc installé le plugin VS Code, regardé quelques vidéos YouTube, et commencé mon voyage pour apprendre les mouvements de base.

J'aime aussi apprendre de nouvelles choses et, mieux encore, je cherche toujours des moyens de devenir plus productif 😉.

Mais comme beaucoup d'entre vous l'ont peut-être vécu, la partie la plus difficile de l'apprentissage de Vim est de commencer. La courbe d'apprentissage initiale est très raide. Ci-dessous se trouve une illustration qui montre cela :).

![La courbe d'apprentissage des éditeurs de texte. Bien que drôle, très précise | Image de Why I Love Using Vim To Write Code : https://youtu.be/o4X8GU7CCSU](https://www.sspaeti.com/blog/why-using-neovim-data-engineer-and-writer-2023/vim-learning-curve.png align="left")

Il m'a aussi fallu deux ou trois tentatives pour commencer à apprendre Vim avant de le comprendre pleinement. J'ai alterné. Tout en ayant du travail à faire, il est parfois difficile de passer entièrement d'un jour à l'autre. Mais j'adorais apprendre tous les mouvements, et je savais que cela me rendrait plus rapide après un court laps de temps.

## Pourquoi j'aime Vim

J'utilise Vim depuis seulement huit mois, et je code en Python depuis environ six ans. J'ai utilisé d'autres éditeurs de code depuis le début de ma carrière en 2003. Chaque éditeur que j'ai utilisé avait ses forces et son attrait. Mais je n'ai jamais connu de gains d'efficacité tels que ceux que j'ai eus avec Vim.

En fin de compte, utilisez l'éditeur qui fonctionne le mieux pour vous. Personnellement, je veux que mon éditeur m'aide à travailler aussi vite que possible, surtout puisque je l'utilise quotidiennement. Investir du temps pour apprendre Vim est nécessaire, mais cela porte ses fruits avec le temps. C'est tout l'intérêt de Vim et surtout du langage Vim.

Une compétence sous-estimée en général parmi les programmeurs est l'utilisation du **terminal**. En apprenant votre éditeur, surtout avec Vim, vous apprendrez naturellement plus sur le terminal et améliorez vos compétences Linux (recherche inverse, lazy git, Tmux, et bien d'autres).

Avant Vim, j'utilisais le terminal seulement si je devais. Je googlisais tout, et aujourd'hui, j'utilise le terminal avec ses manuels utiles chaque fois que je peux.

Parfois, je suis surpris par moi-même aussi, et c'est super nerd 😉 – mais c'est si efficace. Je suis devenu un bien meilleur développeur depuis que j'ai commencé à me sentir à l'aise avec Vim.

Optimiser et configurer Vim peut prendre des heures et des jours, et c'est inévitable au début. Mais après un certain temps, vos [dotfiles](https://github.com/sspaeti/dotfiles) mûrissent, et vous commencez à changer moins de choses. Vous deviendrez également beaucoup plus rapide pour essayer un nouveau plugin ou ajouter un remap.

De plus, Vim est **amusant** ! Travailler dans Neovim est l'un des points forts de mon travail quotidien. Améliorer votre éditeur de texte et le rendre vôtre – peut-être de manières que personne d'autre n'a optimisées – est génial.

Par exemple, j'écris beaucoup, donc j'ai optimisé pour l'écriture en markdown et la programmation en Python. C'est ce qui ajoute beaucoup à mon bonheur en tant que codeur.

À cause de tout cela, [TJ DeVries](https://github.com/tjdevries) appelle Neovim un [PDE](https://brain.sspaeti.com/pde-personalized-development-environment) (Environnement de Développement Personnalisé), et non « juste » un IDE. Vous pouvez en apprendre plus à ce sujet dans les vidéos vraiment inspirantes de [ThePrimeagen](https://www.youtube.com/c/ThePrimeagen) sur [Vim](https://youtube.com/playlist?list=PLm323Lc7iSW_wuxqmKx_xxNtJC_hJbQ7R) et découvrir pourquoi il a utilisé [Vim en 2022](https://youtu.be/D4YTJ2W5q4Y).

Vim a également manifesté en moi le **minimalisme**. J'ai utilisé le terminal au lieu de GUIs fantaisistes et des fichiers texte simples pour la clarté, la liberté, des raccourcis ultra-rapides, pas de verrouillage par le fournisseur, et rester dans le [Flow](https://brain.sspaeti.com/deep-work) avec le contenu devant moi.

Vim a changé non seulement mon flux de travail, mais aussi comment j'ai pu **éditer à la vitesse de la pensée**. Au lieu de penser, « Je veux éditer ce mot », mes doigts sautent à ce mot et le changent avec quelques touches.

## Vim pour l'ingénierie des données

Mon flux de travail en ingénierie des données utilise Neovim avec le [LSP](https://microsoft.github.io/language-server-protocol/) (Language Server Protocol) [pyright](https://github.com/microsoft/pyright) installé avec [mason](https://github.com/williamboman/mason.nvim). Il y a beaucoup plus avec [Tmux](https://github.com/sspaeti/dotfiles/tree/master/tmux), mais vous pouvez trouver tous les détails sur [dotfiles/nvim](https://github.com/sspaeti/dotfiles/tree/master/nvim).

![Installation de Pyright avec Mason](https://www.sspaeti.com/blog/why-using-neovim-data-engineer-and-writer-2023/vim-mason-install.png align="left")

## Vim pour l'écriture

J'utilise encore beaucoup [Obsidian](https://brain.sspaeti.com/obsidian) pour l'écriture (voir plus sur mon [flux de travail PKM](https://sspaeti.com/blog/pkm-workflow-for-a-deeper-life/)) grâce à ses fonctionnalités supplémentaires de support d'images, de backlinks, de graphes et de plugins spécifiques pour la prise de notes, tels que [ReadWise](https://brain.sspaeti.com/readwise) (synchronisation de mes surlignages de livres et de tweets), [Dataview](https://github.com/blacksmithgu/obsidian-dataview) (utilisation de notes comme base de données), [Excalidraw](https://excalidraw.com/) (dessiner avec le format Markdown), Templates, et ainsi de suite.

Néanmoins, j'écris de plus en plus dans Neovim. Pour l'instant, j'utilise [ZenMode](https://github.com/folke/zen-mode.nvim) (pour centrer le texte), Grammarly (pour la vérification de la grammaire), [write-good](https://github.com/btford/write-good) (vérification de la grammaire), et spécifiquement [Obsidian.nvim](https://github.com/epwalsh/obsidian.nvim) (suivre les backlinks, etc.). Vous trouverez tous les détails dans mes [dotfiles](https://github.com/sspaeti/dotfiles).

Dans Obsidian, j'utilise le [mode Vim](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/for+Vim+users) d'Obsidian [.vimrc](https://github.com/sspaeti/dotfiles/blob/master/obsidian/.vimrc) et je mappe la plupart des [raccourcis](https://github.com/sspaeti/dotfiles/tree/master/obsidian) à mes paramètres Vim. En même temps, j'ai écrit de plus en plus dans Neovim et j'ai progressivement basculé vers Neovim complet.

Des plugins comme [Telescope](https://github.com/nvim-telescope/telescope.nvim) et des fonctionnalités de grep simples que j'utilise pour le codage fonctionnent très bien avec Markdown. Voici quelques extraits montrant ce qui est possible dans une excellente conférence sur [Écrire, éditer et construire un monde à la vitesse de la pensée avec Vim](https://youtu.be/2ORWaIqyj7k).

## Pourquoi vous devriez apprendre Vim, aussi

Quand j'ai entendu parler de Vim, je pensais que c'était seulement pour les ingénieurs logiciels et les nerds de Linux 😅. Je n'ai jamais pensé que j'allais l'utiliser aussi. Mais comment suis-je entré dedans ?

J'ai déjà partagé quelques raisons pour lesquelles j'aime Vim. Mais cela a vraiment changé tous mes flux de travail, pas seulement en tant que développeur, mais aussi comment je surfe sur Internet, j'écris, je navigue et j'utilise des outils. Je cherche un mode Vim dans toute application que j'utilise.

Mais si vous n'aimez pas bidouiller et optimiser votre flux de travail, et si vous n'écrivez ou ne codez pas pour gagner votre vie, Vim n'est peut-être pas pour vous. Commencez avec votre éditeur actuel et activez le mode Vim avant de faire quoi que ce soit avec Vim. Cela vous évitera [beaucoup de frustration](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/), faites-moi confiance 😅.

## Comment commencer à utiliser Vim

Il existe de nombreuses bonnes ressources qui vous aideront à commencer avec Vim. La plus simple est de taper `vimtutor` dans votre terminal, qui est un tutoriel interactif pour Vim.

J'ai déjà lié quelques vidéos YouTube ci-dessus – surtout vérifiez ThePrimagen en commençant par [Vim As Your Editor](https://youtu.be/X6AR2RMB5tE) ou [Why even bother with Vim or Neovim in 2022](https://youtu.be/84qoMxS-iqQ).

J'ai commencé avec le [tutoriel Vim](https://youtu.be/IiwGbcd8S7I) de Ben Awads à l'époque. Une excellente [Conférence : Éditeurs (Vim) (2020)](https://youtu.be/a6Q8Na575qc). [Maîtriser le langage Vim](https://youtu.be/wlR5gYd6um0). Je collecte également une petite [playlist](https://www.youtube.com/playlist?list=PLxGd5Sk9B7IZfFOxGWgg8XswEKZ6lEzmh) sur YouTube avec du contenu Vim. Une grande inspiration aussi [dev workflow using Tmux and Vim](https://youtu.be/sSOfr2MtRU8) de [Takuya](https://twitter.com/inkdrop_app?lang=en).

## Conclusion

Nous avons appris que Vim est un puissant éditeur de texte populaire parmi les développeurs. Il est basé sur des raccourcis, appelés langage Vim, qui peuvent rendre le codage et l'écriture plus rapides et plus efficaces.

Avec Vim, vous pouvez sauter à n'importe quelle position de texte spécifique et effectuer des éditions précises rapidement. Bien que l'apprentissage de Vim puisse être difficile, cela en vaut la peine à long terme car cela améliorera votre productivité et apportera de la joie à votre expérience de codage.

Si vous voulez aller plus loin, essayez [Tmux](https://github.com/tmux/tmux/wiki), qui fonctionne bien avec Vim. Vous pourriez même aller un niveau plus profond, comme une disposition de clavier dédiée telle que [Dvorak](https://en.wikipedia.org/wiki/Dvorak_keyboard_layout) ou [Halmak](https://brain.sspaeti.com/halmak) (que j'ai commencé à apprendre à un moment donné). Ou achetez un clavier ergonomique [fancy](https://www.reddit.com/r/kinesisadvantage/comments/yplirr/im_also_part_of_the_team_kinesis_now/?utm_source=share&utm_medium=web2x&context=3) ou [construisez-en un vous-même](https://bit.ly/sspaeti_keyboard).

Merci d'avoir lu jusqu'ici. J'espère que vous avez apprécié cet article. J'ai hâte de lire vos commentaires et expériences.

*Vous pouvez lire plus de mes autres tutoriels sur* [*www.sspaeti.com*](https://www.sspaeti.com/blog/why-using-neovim-data-engineer-and-writer-2023/)*.*