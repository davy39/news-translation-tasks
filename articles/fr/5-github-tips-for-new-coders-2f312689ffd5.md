---
title: 5 conseils GitHub pour les nouveaux codeurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T21:59:49.000Z'
originalURL: https://freecodecamp.org/news/5-github-tips-for-new-coders-2f312689ffd5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zJqp4FDnH00116rssJbdeg.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 5 conseils GitHub pour les nouveaux codeurs
seo_desc: 'By Alyson La

  This October I celebrated my 5 year anniversary working at GitHub. ? 5 years ago,
  I was an enthusiastic accountant (like straight nerd — my former twitter handle
  was @taxaly) who knew nothing about code, let alone about using Git and Git...'
---

Par Alyson La

En octobre dernier, j'ai fêté mes 5 ans chez GitHub. ✨ Il y a 5 ans, j'étais une comptable enthousiaste (une vraie geek — mon ancien pseudo Twitter était @taxaly) qui ne connaissait rien au code, et encore moins à l'utilisation de Git et GitHub.

Maintenant, je suis une Data Scientist enthousiaste qui connaît pas mal de choses sur le codage avec Git & GitHub. C'est en partie grâce à l'apprentissage de ces technologies que j'ai pu effectuer cette reconversion professionnelle enrichissante.

Mais même en travaillant chez GitHub, apprendre Git et GitHub a été difficile ! En tant que forme de contribution open source, je voulais partager avec d'autres débutants en programmation mes 5 meilleurs conseils pour utiliser GitHub.

### **Conseil n°1 : Changez votre éditeur de texte par défaut associé à Git**

Pour beaucoup de gens, l'éditeur de texte par défaut lors de l'utilisation de Git depuis le terminal est VIM. VIM peut être une chose terrible et effrayante pour le hacker débutant ou occasionnel. Ou même pour les hackers chevronnés ou [@haacked](https://twitter.com/haacked) lui-même.

Si jamais vous vous retrouvez avec un conflit de fusion (et cela arrivera, voir le conseil n°4), vous serez renvoyé vers VIM pour résoudre le conflit et vous devrez alors connaître les commandes VIM spécifiques pour éditer le document, ce qui donne envie de pleurer. Pendant plus d'un an, j'ai eu un post-it sur mon écran au travail pour me rappeler les commandes VIM de base comme `i` (pour éditer) et `:wq` (pour sauvegarder et quitter). Pour éviter les larmes potentielles, vous pouvez simplement changer l'éditeur de texte par défaut.

Pour changer votre éditeur de texte pour Atom, Sublime ou TextMate, suivez les instructions de cette [aide GitHub](https://help.github.com/articles/associating-text-editors-with-git/).

Pendant que vous y êtes, vous devriez également vous assurer que vos raccourcis sont configurés afin de pouvoir ouvrir des fichiers dans votre éditeur de texte préféré directement depuis le terminal en utilisant `subl .` ou `atom .`. Consultez [ces documents](http://flight-manual.atom.io/getting-started/sections/atom-basics/#opening-modifying-and-saving-files) pour configurer l'accès à Atom depuis votre terminal et [ces documents](http://www.sublimetext.com/docs/2/osx_command_line.html) pour configurer Sublime.

### Conseil n°2 : **Changez vos dotfiles**

Je n'ai entendu parler des dotfiles qu'après avoir programmé et utilisé Git & GitHub pendant plusieurs années. Je regrette encore de ne pas l'avoir su plus tôt !

Les dotfiles vous permettent de personnaliser l'invite de votre terminal afin de voir sur quelle branche git vous vous trouvez et si vous avez des modifications non commitées. C'EST GÉNIAL ! J'ai récupéré [mes dotfiles](https://github.com/alysonla/dotfiles) auprès d'un collègue ([John Nunemaker](https://www.freecodecamp.org/news/5-github-tips-for-new-coders-2f312689ffd5/undefined)), mais si vous cherchez 'dotfiles' sur GitHub, vous trouverez des tas d'options.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nLOXZnYWV-CopD55vREPXA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*0UPvjS69Z925qDx_1RJ68Q.jpeg)
_les dotfiles pour la gagne !_

### Conseil n°3 : **Installez Hub**

[Hub](https://github.com/github/hub) est un outil en ligne de commande qui facilite l'utilisation de GitHub. Souvent, je travaille sur un dépôt dans mon terminal mais je veux voir les tickets (issues) ou les pull requests sur GitHub. J'ouvre alors un onglet de navigateur, puis je me laisse distraire par mes e-mails/Twitter/un chiot — et dix minutes plus tard, je finis par taper l'URL du dépôt GitHub.

En tapant `hub browse` dans le terminal, cela ouvrira automatiquement l'URL du dépôt directement dans votre navigateur pour une utilisation de GitHub sans distraction. Boum.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zJqp4FDnH00116rssJbdeg.png)
_Nash l'Octodog_

### Conseil n°4 : **Entraînez-vous aux conflits de fusion**

C'est ici que j'avoue que je baisse parfois les bras. Surtout en ce qui concerne les conflits de fusion. Je ne compte plus le nombre de fois où j'ai abandonné un projet ou une pull request parce que j'avais un conflit de fusion.

Ils me faisaient peur, la documentation sur la façon de les résoudre me faisait peur, et puis je me retrouvais dans VIM et je voulais tout arrêter (voir le conseil n°1).

Puis j'ai réalisé que je devais affronter ma peur, alors j'ai créé un dépôt d'entraînement, j'ai provoqué un conflit de fusion **exprès**, et j'ai [suivi la documentation](https://github.com/blog/2293-resolve-simple-merge-conflicts-on-github) ou regardé une vidéo YouTube sur la façon de résoudre les conflits de fusion. Je l'ai fait plusieurs fois. De plus, vous pouvez désormais [résoudre des conflits de fusion simples](https://github.com/blog/2293-resolve-simple-merge-conflicts-on-github) dans l'interface utilisateur de GitHub, ce qui est très pratique.

Aujourd'hui, quand je rencontre un conflit de fusion, j'ai un peu moins peur et je supprime calmement les chevrons, sachant que grâce au contrôle de version, je ne peux pas faire trop de dégâts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DKRDKuXmj0b7x6L2bsz4bQ.gif)
_Entraînement._

### **Conseil n°5 : Créez une GitHub Page**

Une GitHub Page est un site web personnel ou de projet que GitHub héberge gratuitement ! Il est toujours utile d'avoir un projet concret à pousser sur GitHub pour mettre en pratique vos compétences Git et GitHub.

Créez un site web simple en utilisant HTML, CSS et JavaScript à partir d'un tutoriel de programmation, puis suivez les étapes pour l'héberger sur GitHub [ici](https://pages.github.com/) ou vous pouvez regarder [cette](https://www.youtube.com/watch?v=rRGrT0wsJxI) vidéo que j'ai faite il y a quelque temps avec des instructions étape par étape. Ou essayez la méthode super facile [Fork and Go](https://github.com/jlord/forkngo).

Enfin, je vais glisser un 6ème conseil peut-être évident : **suivez un cours ou un tutoriel sur Git et GitHub** !

En voici quelques-uns qui valent le détour :

* Git-it : [https://github.com/jlord/git-it-electron](https://github.com/jlord/git-it-electron)
* Vidéos freeCodeCamp : [https://youtu.be/vR-y_2zWrIE](https://youtu.be/vR-y_2zWrIE)
* Formation GitHub : [https://services.github.com/on-demand/resources/](https://services.github.com/on-demand/resources/)
* Aide-mémoire Git — [http://ohshitgit.com/](http://ohshitgit.com/)

J'espère que cette liste de conseils vous a été utile et si vous avez d'autres astuces qui vous ont aidé dans votre apprentissage de Git et GitHub, j'aimerais beaucoup les connaître ! ❤️