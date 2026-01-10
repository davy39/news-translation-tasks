---
title: Comment un adolescent autodidacte a construit un système d'exploitation qui
  fonctionne dans votre navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-21T04:31:46.000Z'
originalURL: https://freecodecamp.org/news/how-a-self-taught-teenager-built-an-operating-system-that-runs-in-your-browser-47da735ac919
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3GSXtqHjyCFn-zqJncrhOA.png
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: Comment un adolescent autodidacte a construit un système d'exploitation
  qui fonctionne dans votre navigateur
seo_desc: 'By Peter Gleeson

  Arizona teenager Aaron Adams built and maintains this awe-inspiring solo project.
  Developed entirely in the cloud using c9.io’s online development environment, aOS
  (short for AaronOS) is an impressive tool, packed with a whole bunch ...'
---

Par Peter Gleeson

Aaron Adams, un adolescent de l'Arizona, a construit et maintient [ce projet solo impressionnant](https://aaron-os-mineandcraft12.c9.io/). Développé entièrement dans le cloud en utilisant l'environnement de développement en ligne de [c9.io](https://c9.io/), aOS (abréviation de AaronOS) est un outil impressionnant, rempli de nombreuses fonctionnalités et d'opportunités de personnalisation.

Pour n'en citer que quelques-unes :

* Vous préférez une interface inspirée d'OSX ? C'est possible. Vous préférez une interface thématique classique Windows XP ? C'est possible. Ou vous avez envie de concevoir la vôtre ? Allez-y !
* Assurez-vous d'essayer la capacité de reconnaissance vocale de l'assistant virtuel NORAA
* Testez les commandes dans la fenêtre de terminal de style bash
* Essayez d'utiliser certaines des applications intégrées telles que l'Éditeur de texte, le Traceur de fonctions et le Visualiseur de musique
* Pourquoi ne pas écrire votre propre application personnalisée en utilisant App Maker ?

Encore plus impressionnant est l'histoire derrière ce jeune programmeur et comment il maintient ce projet en cours.

J'ai donc contacté Aaron, et il a gentiment accepté de répondre à quelques questions. Vous pouvez lire ses réponses ci-dessous.

**Moi : Salut Aaron, merci d'avoir accepté de répondre à quelques questions sur aOS. Commençons par en savoir un peu plus sur toi, et comment tu as commencé ton parcours en programmation. Y a-t-il eu des figures clés ou des événements qui t'ont inspiré ?**

Aaron : Merci pour votre intérêt pour aOS ! À propos de moi ? Je suis juste un adolescent moyen de l'Arizona, fraîchement sorti du lycée. Je travaille actuellement dans une succursale d'AMC Theatres et aussi dans une épicerie. Ma première expérience en programmation est venue par un ironique coup du sort, en fait. Lorsque je me suis inscrit aux cours du lycée en première année, j'étais (et je le suis encore aujourd'hui) très intéressé par la photographie, alors j'ai demandé la production cinématographique comme l'un de mes cours.

Apparemment, ce cours était complet, alors j'ai été placé à la place dans GenYes — un cours qui se concentre sur l'éducation de ma génération sur les compétences importantes liées à l'informatique. Des choses comme le dépannage et la réparation d'ordinateurs, l'utilisation de programmes courants, et bien sûr — la programmation. Si j'avais été accepté pour le cours de production cinématographique, je n'aurais probablement jamais découvert la programmation, et encore moins laissé celle-ci envelopper ma vie comme elle l'a fait ! Mon professeur de GenYes m'a vraiment aidé, et j'ai refait le cours à nouveau lors de ma dernière année de lycée. Ce cours seul est ce qui a permis à mon parcours en programmation de décoller.

**C'était vraiment un coup de chance ! Parle-moi plus de la façon dont aOS a commencé ? Quelle était l'idée initiale, ou la portée du projet ?**

C'est une question délicate ! Mes premières expériences en programmation ont été passées à faire des dizaines de petits projets ; comme des calculatrices, des manipulateurs de chaînes, etc. L'un de ces projets était un « Système d'exploitation », ou du moins quelque chose qui y ressemblait un peu. Vous pouvez voir ce projet [ici](https://www.codecademy.com/MineAndCraft12/codebits/o4qKD).

À l'époque, j'étais si fier de lui — mais je me suis dit, pourquoi m'arrêter à une simple application de blague ? Et si j'essayais de faire un programme légitime avec un vrai but ? aOS est là où je suis allé avec ce désir initial. Notez que aOS et le premier projet de « système d'exploitation » sont deux constructions complètement différentes. J'ai recommencé et abandonné plusieurs fois au début de aOS, généralement avec l'excuse de « Je suis largement dépassé ».

**Je suis sûr que beaucoup de développeurs débutants passent par une expérience similaire. Comment as-tu surmonté ces doutes initiaux ?**

La principale façon dont j'ai surmonté ces doutes initiaux est qu'après toutes ces tentatives infructueuses, j'ai décidé de terminer mon cours de programmation sur JavaScript pour en apprendre un peu plus, afin de pouvoir revenir et réessayer.

L'approche que j'ai adoptée lors de la prochaine tentative était, plutôt que de me concentrer sur « construire un système d'exploitation entier », je me concentrerais plutôt sur « créer un bureau », puis « créer une fenêtre », puis « faire bouger la fenêtre » — chaque tâche étant séparée et autonome. Ce changement de focus signifiait que le projet ne semblait plus être une tâche immense qui ne serait jamais terminée. Au lieu de cela, il semblait maintenant être une collection de tâches (supposément) plus faciles, et chaque fois que j'en terminais une, cela me motivait à passer à une autre. Cela a continué, et nous voici aujourd'hui — je suis fier de dire que aOS ressemble presque à un bureau « réel ».

**Pourrais-tu clarifier pour tous ceux qui lisent ceci exactement ce qu'est aOS ? Dans quelle mesure imite-t-il un système d'exploitation « réel » ?**

D'accord, donc aOS n'interagit en réalité d'aucune manière avec le matériel de la machine. La chose la plus proche du matériel que aOS atteint est la lecture du niveau de la batterie, et peut-être la lecture de l'état du réseau. Le navigateur gère toute la gestion de la mémoire de bas niveau, et aOS ne peut pas fonctionner seul, par exemple, installé dans le code de démarrage ou exécuté en code natif. En ce sens, aOS est vraiment plus proche d'un environnement de bureau que d'un système d'exploitation.

**Bien sûr — en tant qu'exercice de conception de l'interface utilisateur et des systèmes, c'est un exploit remarquable. Quelle inspiration as-tu tirée de projets existants ?**

Je me suis inspiré de nombreuses sources. En regardant en arrière aussi loin que je me souvienne, les seuls systèmes d'exploitation réels que j'ai utilisés étaient Windows (à la maison) et Chrome OS (à l'école). Dans la version la plus ancienne survivante de aOS disponible, il y a quelques artefacts inspirés de Windows présents. L'un d'eux est que le Bloc-notes est, bien sûr, nommé d'après son homologue Windows.

Les applications Fichiers et Internet ont pris quelques indices subtils du navigateur Chrome dans leur conception ; principalement avec la barre d'onglets en haut qui dépasse au-dessus du contenu. Plus récemment, l'inspiration d'autres sources peut être très facilement trouvée dans différents endroits du système d'exploitation. L'effet WindowBlur est très évocateur de l'apparence Aero de Windows. La barre des tâches est très similaire à celle de Windows. J'ai inclus une console bash simulée, qui est évidemment inspirée de Linux. Une autre fonctionnalité de Linux est la capacité à plier les fenêtres avec le bouton sur le côté gauche de la barre de titre. Le menu « Paramètres » est très inspiré du menu des paramètres de Windows 10.

Il y a quelques modes de tableau de bord différents qui sont inspirés de ceux de Windows 7, Android, et du Whiskermenu XFCE de Linux. Je suis sûr que vous pouvez repérer de nombreuses autres fonctionnalités où je me suis inspiré de ces sources !

**Dans l'ensemble, quelles ont été tes parties préférées du projet jusqu'à présent ? Et quels ont été les plus grands défis auxquels tu as été confronté ?**

Ma partie préférée du projet ? Oh là là, encore avec les questions difficiles ! Je ne suis vraiment pas sûr de pouvoir pointer un moment spécifique, mais je me souviens que le fait de faire fonctionner correctement les fonctionnalités de déplacement et de redimensionnement des fenêtres avec l'effet WindowBlur a été l'un des meilleurs moments « Je l'ai fait ! ». Je dirais que ces moments où l'on travaille dur sur quelque chose pendant plus d'une semaine avant de finalement le terminer et le perfectionner — ce sont mes moments préférés dans le développement de aOS.

En ce qui concerne les parties difficiles du développement, je peux immédiatement penser à deux choses : travailler avec les restrictions de sécurité imposées par le navigateur, et les problèmes de performance causés par le navigateur. En fait, j'ai dû réécrire des parties majeures du système d'exploitation plusieurs fois parce que les performances étaient trop mauvaises.

Par exemple, lorsqu'il a été dévoilé pour la première fois, WindowBlur était _horrible_ en termes de fréquence d'images, même sur des machines plus puissantes. J'ai été obligé de le refaire, et plus récemment, je l'ai simplement réduit un peu, pour le bien des performances.

En ce qui concerne la sécurité, s'assurer que tout le monde visualise la page en https était très difficile. Sans https, Chrome demanderait une confirmation de permission _à chaque fois_ que j'essayais d'accéder au microphone (pour l'assistant virtuel NORAA) ou à la caméra (pour l'application Caméra). En utilisant https, le site est plus sécurisé, et Chrome ne demande qu'_une seule fois_ pour tout cela, et se souvient des préférences de chaque utilisateur.

Aussi, maintenant que j'y pense, peut-être que le pire problème auquel j'ai été confronté dans le développement de aOS était le cache de Chrome. Chrome mettait en cache mon script et ma feuille de style, ce qui rendait les mises à jour presque impossibles à déployer. J'ai depuis contourné cette fonctionnalité, en plaçant la milliseconde de la requête GET dans les paramètres d'URL du fichier de script. C'était un obstacle difficile à surmonter !

**Fais-tu partie d'une communauté de développeurs plus large ?**

Jusqu'à récemment, j'ai travaillé seul sur ce projet. Cependant, j'ai depuis reçu des contributions sous forme d'icônes, de graphiques et d'idées du public, et je suis ouvert aux contributions de quiconque — tant que je suis en mesure de passer en revue et d'implémenter les changements moi-même.

**Une grande partie de ton code source est publique et est inhabituelle en ce sens que la plupart de la logique est contenue dans un seul fichier de plus de 12 000 lignes. Cela affecte-t-il ton flux de travail, et si oui, prévois-tu de refactoriser ton code à un moment donné ?**

Bien que le très grand fichier unique puisse sembler être un inconvénient, je l'ai en fait gardé ainsi pour une raison. Lorsque les fichiers de script sont appelés séparément — disons chaque application dans son propre fichier de script — alors Chrome charge chaque fichier de manière asynchrone et les exécute tous dès qu'ils sont chargés, avec pour résultat qu'ils sont presque toujours exécutés dans le désordre !

Dans aOS, les applications système s'initialisant dans le mauvais ordre, ou certains morceaux de code de démarrage s'exécutant dans le mauvais ordre, peuvent briser le système. Dans un grand fichier, tous ces problèmes de timing sont évités, et chaque module se charge un par un, dans l'ordre parfait. J'ai depuis fait plus de pas vers l'obtention d'une configuration plus modulaire dans la source, mais pour l'instant, un gros fichier est toujours la voie que je suis en train de suivre.

**Tu as utilisé Cloud9 pour développer et héberger AaronOS. Fais-tu tout ton travail de développement en ligne, ou travailles-tu aussi localement ? À quoi ressemble ton environnement de développement actuel ?**

À l'origine, AaronOS a été développé sur le programme codebit de Codecademy. C'était à l'époque de la V0.9 et des versions antérieures, et la version codebit était très limitée car je ne pouvais utiliser que trois fichiers — un HTML, un CSS et un JavaScript. Pas de PHP, ou de liens externes (à part les images).

Tout mon travail de développement est fait en ligne, et l'IDE Cloud9 est très bon en termes de continuité — je peux écrire du code sur un ordinateur, manquer de batterie abruptement, et reprendre sur un autre ordinateur avec l'IDE dans _exactement le même état qu'il était lorsque j'ai manqué de batterie_. Le fichier est défilé au même endroit, les sessions de terminal persistent, les onglets persistent, tout persiste. Même le curseur reste au même endroit ! Je me connecte littéralement sur n'importe quel ordinateur et je me mets au travail, ce qui est incroyable.

Ma configuration matérielle principale est une machine HP 350 G1 avec un processeur i3 et des graphiques intégrés, et, plus récemment, 16 Go de RAM. C'est aussi ma machine de jeu principale, et elle m'a surpris par sa capacité à faire tourner 60 FPS dans de nombreux jeux.

J'utilise Windows 10 pour les jeux, mais je fais principalement tourner Linux Mint avec le bureau XFCE. J'ai installé AeroGlass et Classic Shell, ce qui le fait ressembler beaucoup à Windows 7. Personnellement, je ne suis pas un fan de l'interface utilisateur de Windows 10 — les petits détails me dérangent vraiment, comme l'invite de commande qui s'ouvre parfois avec les bordures de fenêtre thématiques Windows 98, ou la façon dont l'exécution de programmes en mode de compatibilité pour Windows XP les fait utiliser les bordures de fenêtre de base de Windows 7. Faites un choix, Windows !

**Tu as clairement un œil attentif pour une UX cohérente ! Quels frameworks ou outils as-tu utilisés pour construire l'interface utilisateur et la logique backend ? Et as-tu un langage préféré avec lequel travailler ?**

L'un de mes objectifs avec aOS était de n'utiliser aucune bibliothèque JavaScript tierce. Tout le code a été écrit à partir de zéro par moi-même — pas de jQuery, Angular, Underscore, etc. — c'est du JavaScript « vanilla » à 100 %. L'interface utilisateur est entièrement présentée en HTML et CSS, et tout le code côté client est en JavaScript. Le code côté serveur est écrit en PHP.

Mon langage préféré serait JavaScript, bien que TI-BASIC arrive en deuxième position. Pour ceux qui ne savent pas, TI-BASIC est le langage utilisé sur les calculatrices TI-8*, et il signifie beaucoup pour moi parce que c'était le seul moyen de programmer pendant les autres cours ! De plus, les autres enfants à l'école appréciaient les jeux vidéo que je mettais sur leurs calculatrices pour eux.

**L'assistant virtuel NORAA est une fonctionnalité vraiment cool — comment est-il venu ?**

NORAA a été inventé une nuit où je regardais à nouveau War Games, (un film avec un ordinateur appelé JOSHUA qui a trompé tout le monde en leur faisant croire qu'il y avait une guerre thermonucléaire mondiale). NORAA est inspiré en partie par Cortana de Windows, et en partie par JOSHUA _(édité : Aaron, s'il te plaît, ne commence pas la Troisième Guerre mondiale…)_.

JOSHUA est l'origine de l'apparence de type terminal pour NORAA. J'ai codé la capacité pour NORAA d'adapter ses réponses en fonction de son attitude envers vous. Malheureusement, cette fonctionnalité a peu été implémentée en dehors de quelques commandes de test. Actuellement, NORAA est plus axé sur l'exécution de tâches que sur la recherche de choses sur Internet. Au cas où vous vous poseriez la question, NORAA est mon propre nom, épelé à l'envers !

**En termes d'avenir, quels sont tes plans et ambitions ? Qu'est-ce qui attend AaronOS ? Et qu'en est-il des systèmes et des bureaux basés sur le cloud en général ?**

À ce stade, je n'ai pas de plans spécifiques pour AaronOS ; ce que je veux dire par là, c'est qu'AaronOS n'a pas de point réel où il sera « terminé ». Un peu comme le jeu Minecraft, il sera continuellement mis à jour et amélioré jusqu'à ce que je sois physiquement incapable de continuer à travailler dessus, ou si je manque d'argent… selon ce qui arrive en premier !

Cela dit, la prochaine grande étape pour aOS est la sortie de la version Bêta. La Bêta n'est pas terminée et est encore en développement, mais elle sera marquée par quelques grandes mises à jour, peut-être par l'introduction d'un Marché d'Extensions où vous pourrez télécharger des applications, des scripts et des feuilles de style créés par d'autres utilisateurs. Seul le temps nous le dira.

Bien qu'il y ait peu de bureaux basés sur le cloud disponibles, les deux seuls qui me viennent à l'esprit et qui sont encore en développement actif sont mon propre aOS et un autre appelé [OS.js](https://www.os-js.org/), qui est un projet incroyable.

J'espère qu'aOS, OS.js et d'autres projets comme eux serviront de preuve que, avec la programmation (et assez de temps libre), vous pouvez faire presque tout ce que vous voulez devenir réalité.

**Aaron, merci d'avoir pris le temps de répondre à quelques questions ! Encore une fois, félicitations pour un projet vraiment impressionnant — j'ai hâte de voir ce qui vient ensuite !**

Avec plaisir — merci pour cette merveilleuse opportunité de parler d'aOS ! J'ai hâte de le lire quand il sortira.