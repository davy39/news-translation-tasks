---
title: Améliorez votre flux de travail avec ces outils CLI géniaux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-08T16:59:25.000Z'
originalURL: https://freecodecamp.org/news/improve-your-workflow-with-these-awesome-cli-tools-fc3750cbb2bf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gQ5M2T5sQInL3NJmKfTx_g.gif
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: terminal
  slug: terminal
seo_title: Améliorez votre flux de travail avec ces outils CLI géniaux
seo_desc: 'By Dylan Tientcheu

  Happily(?), today we are in an era where productivity is mostly achieved through
  smart work rather than hard work. We constantly have to be looking for faster, easier
  and smarter ways to achieve results.

  The following tools will no...'
---

Par Dylan Tientcheu

Heureusement (?), nous vivons aujourd'hui à une époque où la productivité est principalement atteinte par le travail intelligent plutôt que par le travail acharné. Nous devons constamment chercher des moyens plus rapides, plus faciles et plus intelligents pour obtenir des résultats.

Les outils suivants vous aideront non seulement à travailler plus vite, mais vous le ferez tout en vous amusant **dans votre terminal**.

![Image](https://cdn-media-1.freecodecamp.org/images/ULJ6TbMj9gcaFDmnX7N3oM26nZMYRs2LOfkJ)
_OMG est-ce que c'est... Oui, c'est vraiment sur Windows (Suivez ces étapes)_

**_Note aux utilisateurs de Windows_**_: Comme vous pouvez le constater, la plupart de ces outils sont basés sur Unix et implémentent certaines fonctionnalités qui peuvent ne pas fonctionner correctement sur CMD ou PowerShell. Je vous recommande d'utiliser [**WSL**](https://docs.microsoft.com/en-us/windows/wsl/install-win10) **(Windows Subsystem for Linux).**_

_Ne vous inquiétez pas, [**cet article**](https://medium.com/@blurdylan/transforming-your-ugly-terminal-to-a-unicorn-b83f315a36d1) peut vous montrer comment rendre WSL le terminal le plus beau_ ?

Améliorons nos CLIs.

### Gestion des tâches et planification

Oui, je sais, nous avons une pléthore d'outils de gestion des tâches incroyables sur le web et le bureau. Cependant, vous devriez essayer ceux basés sur votre émulateur de terminal.

#### [Task Warrior](https://taskwarrior.org/)

[Taskwarrior](https://taskwarrior.org/) est un logiciel libre et open source qui gère votre liste de tâches à faire depuis la ligne de commande. Il est flexible, rapide et discret. Il fait son travail puis s'efface.

![Image](https://cdn-media-1.freecodecamp.org/images/jJXuuUIULwDuLXkK6hWX1Rb6KFQPHROJohaA)
_Ce n'est même pas [1/10ème](https://taskwarrior.org/docs/" rel="noopener" target="_blank" title=") de ce que Taskwarrior peut faire._

#### [Thyme](https://github.com/hughbien/thyme) — Minuterie Pomodoro en console

La [Technique Pomodoro](http://www.pomodorotechnique.com/) a été développée par Francesco Cirillo. Cette technique aide vraiment à l'efficacité et à la gestion du temps. Maintenant, **Thyme** est un outil qui aide à apporter cette technique à votre terminal avec de grandes options personnalisables.

#### [Moro](https://github.com/albacoretuna/moro) — Suivi des heures de travail

Un outil en ligne de commande pour suivre les heures de travail, aussi simple que possible.

![Image](https://cdn-media-1.freecodecamp.org/images/9wsZXpsy2P9o9oXLr88jXnylCt18yH3wguMs)
_[https://moro.js.org/](https://moro.js.org/" rel="noopener" target="_blank" title=")_

### Développement

#### [Wuzz](https://github.com/asciimoo/wuzz) — Inspecteur HTTP

Imaginez un [**Postman terminalisé**](https://www.getpostman.com/)**.** Wuzz est un outil cli interactif pour l'inspection HTTP.

![Image](https://cdn-media-1.freecodecamp.org/images/Drmxf3VabkRmwkF6EeBTryiKuhBuY2Ucncuq)
_[https://github.com/asciimoo/wuzz](https://github.com/asciimoo/wuzz" rel="noopener" target="_blank" title=")_

#### [FX](https://github.com/antonmedv/fx) — Visualiseur JSON

FX est l'outil de référence pour le traitement et la visualisation de JSON. Il est vraiment impressionnant avec toutes ses commandes d'exécution. Je cherche toujours son équivalent basé sur le web ou le bureau.

![Image](https://cdn-media-1.freecodecamp.org/images/14YFwWthez7m3MpFd52hH7OTolCVPh8cQ2cU)
_[https://github.com/antonmedv/fx](https://github.com/antonmedv/fx" rel="noopener" target="_blank" title=")_

#### [Serve](https://github.com/zeit/serve) — Utilitaire de service de fichiers CLI le plus rapide

Peut-être pensez-vous que j'exagère. Eh bien, non. Vous souvenez-vous lorsque vous deviez télécharger [_simpleHTTPServer de Python_](https://docs.python.org/2/library/simplehttpserver.html) ou le _serveur web pour l'application Chrome_ chaque fois que vous deviez configurer un site statique en localhost ? Tout cela est du passé. Avec une commande aussi simple que `npx serve` directement depuis le dossier de votre site statique, vous êtes servi !

#### [howdoi](https://github.com/gleitz/howdoi) — Votre solution rapide StackOverFlow

Il se décrit mieux ainsi : « des réponses de codage instantanées via la ligne de commande ».

La prochaine fois que vous cherchez une réponse de codage, réfléchissez à deux fois avant d'ouvrir votre navigateur pour lire des blogs. Avec `howdoi`, la réponse pourrait être plus proche que vous ne le pensez.

#### [gitstats](https://github.com/IonicaBizau/git-stats) — print(githubCharts);

![Image](https://cdn-media-1.freecodecamp.org/images/EQ2C027E5YjbbwcMGFRFCrZuN3zLkO1VP31d)

#### [DevStats](https://github.com/shroudedcode/devstats) — print(allDevStats);

DevStats est une application CLI qui récupère des statistiques depuis des « sites de développeurs » comme StackOverflow, WakaTime et GitHub et les affiche de manière agréable. Si vous êtes un maniaque des statistiques, vous pouvez même afficher vos rapports quotidiens et basculer entre les jours.

![Image](https://cdn-media-1.freecodecamp.org/images/AGvVXQZRo4JV-Y1cDmePomHggn4Rd8vrdr02)

#### [Terminalizer](https://github.com/faressoft/terminalizer) & [Asciinema](https://asciinema.org/) — Enregistreurs de terminal

* [Terminalizer](https://github.com/faressoft/terminalizer) vous aide à enregistrer vos sessions de terminal et à générer des images gif. Cela aide vraiment à montrer comment une commande est utilisée.

![Image](https://cdn-media-1.freecodecamp.org/images/xlVFNeVHCIOuTJX0X2W6Xx2hfouEDOApJjHK)
_Terminalizer_

* [Asciinema](https://asciinema.org) est une excellente solution open source pour enregistrer des sessions de terminal et les partager sur le web. Il vise à être un endroit « incontournable » pour chaque utilisateur de ligne de commande qui souhaite partager ses compétences avec les autres. Ou, en d'autres termes, c'est un endroit pour montrer votre côté geek.

### Amusement

> Qui attend vraiment que `npm install` se termine ?

#### [Bash2048](https://github.com/mydzor/bash2048) — Jouez à 2048 dans votre terminal

Jouez au célèbre jeu 2048 directement depuis votre terminal. (Copiez la ligne suivante et collez-la dans votre terminal).

`$ bash <(curl [-s https://raw.githubusercontent.com/mydzor/bash2048/master/bash2048](https://raw.githubusercontent.com/mydzor/bash2048/master/bash2048.sh).sh)`

![Image](https://cdn-media-1.freecodecamp.org/images/Tc5aH2Z5QczSO90aBlVU6hKnBinR3aY6uQrT)
_`bash &lt;(curl [-s https://raw.githubusercontent.com/mydzor/bash2048/master/bash2048](https://raw.githubusercontent.com/mydzor/bash2048/master/bash2048.sh" rel="noopener" target="_blank" title=").sh)`_

#### [TextMeme](https://github.com/beatfreaker/text-meme-cli)

Générez de beaux mémes textuels comme celui ci-dessous, directement depuis votre terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/1xUJPfihe5tiQCJ7leaOa3labcHLK1AB5hEB)
_[https://github.com/beatfreaker/text-meme-cli](https://github.com/beatfreaker/text-meme-cli" rel="noopener" target="_blank" title=")_

#### [CLI Typer](https://github.com/balzss/cli-typer) — Pratiquez la dactylographie comme en 2003

Pratiquez la frappe au clavier en ligne de commande et mesurez vos compétences.

![Image](https://cdn-media-1.freecodecamp.org/images/O-5eRsZ64wy57THPvYgpHoOdlr1opKJABsXz)

### Divers

#### [Speed test](https://github.com/sindresorhus/speed-test) — Test de vitesse Internet

Git agit bizarrement ? Peut-être avez-vous besoin d'un test de connexion rapide. Laissez speed test ping depuis votre terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/lUeU3ZidtTrx16TeQOIYYeCAK0ZEZ2yPvHdg)

#### [Overtime-cli](https://github.com/diit/overtime-cli)

Tableaux de chevauchement de temps faciles pour les équipes distantes.

![Image](https://cdn-media-1.freecodecamp.org/images/LSdvBbUVeYy8AuAYlvWRGVb8p8u5bp4PVJzl)
_[https://github.com/diit/overtime-cli](https://github.com/diit/overtime-cli" rel="noopener" target="_blank" title=")_

### Vous trouvez la liste trop courte ?

Ce sont tous des **outils géniaux** que des **développeurs géniaux** ont créés pour aider la communauté.

Vous savez ce qui est encore **plus génial** ? Une **liste géniale** de **listes géniales** contenant des **outils CLI géniaux** ?

* [https://github.com/agarrharr/awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)
* [https://github.com/alebcay/awesome-shell](https://github.com/alebcay/awesome-shell)
* [http://reddit.com/r/commandline](http://reddit.com/r/commandline)

Assurez-vous de les consulter et de laisser quelques étoiles sur les dépôts.

> Vous pouvez laisser un c_lap_?? si vous avez apprécié la lecture.

[**Dylan Tientcheu (@DylanTientcheu) | Twitter**](https://twitter.com/dylantientcheu)  
[_F525F4A5 * Éditeur : VSCode * Thème : Material Darker * Police : Operator Mono w Ligatures_twitter.com](https://twitter.com/dylantientcheu)