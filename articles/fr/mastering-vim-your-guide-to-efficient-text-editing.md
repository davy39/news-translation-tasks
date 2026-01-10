---
title: 'Maîtriser VIM : Votre guide pour l''édition de texte efficace'
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2024-06-24T15:51:35.172Z'
originalURL: https://freecodecamp.org/news/mastering-vim-your-guide-to-efficient-text-editing
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1719244279807/32ef1ce5-423b-4762-b0fa-5f6420d67788.jpeg
tags:
- name: vim
  slug: vim
- name: youtube
  slug: youtube
seo_title: 'Maîtriser VIM : Votre guide pour l''édition de texte efficace'
seo_desc: 'VIM is a highly configurable text editor that enables efficient text editing.
  It''s favored by many developers and system administrators for its powerful capabilities
  and extensive customization options.

  We just published a course on the freeCodeCamp....'
---

VIM est un éditeur de texte hautement configurable qui permet une édition de texte efficace. Il est privilégié par de nombreux développeurs et administrateurs système pour ses capacités puissantes et ses options de personnalisation étendues.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous aidera à maîtriser l'éditeur VIM. Que vous soyez nouveau dans VIM ou que vous cherchiez à approfondir votre compréhension, ce cours vous fournira les compétences essentielles pour utiliser VIM efficacement dans votre flux de travail de développement. Andrew Brown d'ExamPro a développé ce cours.

À la fin de ce cours, vous comprendrez le contexte historique et l'évolution de VIM, acquerrez une maîtrise de ses commandes et modes de base, apprendrez à personnaliser VIM pour l'adapter à votre flux de travail personnel, explorerez des fonctionnalités avancées, y compris les plugins et le scripting avec VimScript, et développerez la capacité d'intégrer VIM dans divers environnements de développement.

VIM est connu pour sa courbe d'apprentissage abrupte, et il n'est pas rare d'entendre parler des frustrations des débutants. Les défis initiaux, cependant, laissent place à une expérience d'édition puissante, efficace et hautement productive. Ce cours vise à lisser votre courbe d'apprentissage et à transformer votre expérience VIM de redoutable en délicieuse.

Ci-dessous, vous trouverez une description des sections principales de ce cours, commençant par le Prélude, puis couvrant les commandes de base.

# Prélude

### PDP-7 et la naissance d'Unix

Pour vraiment comprendre VIM, nous devons commencer par le PDP-7, un mini-ordinateur des années 1960 où le système d'exploitation Unix est né. Le développement d'Unix a conduit à la création de divers éditeurs de texte qui ont servi de précurseurs à VIM. Unix a introduit une série d'outils en ligne de commande fondamentaux pour l'informatique moderne, et l'émulation d'Unix 1 nous permet d'apprécier l'environnement dans lequel les premiers éditeurs de texte comme Ed et Ex ont été développés.

### Qu'est-ce qu'Ed et EX ?

Ed est l'un des premiers éditeurs de texte pour Unix, connu pour sa simplicité et son interface basée sur les commandes. S'engager directement avec Ed nous aide à comprendre sa structure de commande et sa fonctionnalité, posant les bases pour les éditeurs suivants.

Ex, en revanche, a étendu les capacités d'Ed, ajoutant plus de fonctionnalités et améliorant l'interaction utilisateur. En suivant Ex, nous pouvons expérimenter ses améliorations et voir comment il a préparé le terrain pour Vi, la prochaine évolution dans l'édition de texte.

### Qu'est-ce que VI ?

Vi, ou éditeur visuel, a été un bond en avant significatif, offrant une approche orientée écran pour l'édition de texte. Explorer l'interface de Vi et ses commandes de base révèle pourquoi il est devenu si populaire parmi les développeurs.

Vi a été encore amélioré en VIM (Vi IMproved), qui s'appuie sur Vi avec des améliorations étendues, en faisant un éditeur puissant pour le développement moderne. Commencer avec Vimtutor, un tutoriel interactif, et explorer le système d'aide intégré est un excellent moyen de se familiariser avec VIM.

### Évolution et versions de VIM

Comprendre les différentes versions de VIM et leur évolution au fil du temps est crucial pour apprécier ses capacités actuelles. Expérimenter avec diverses versions de VIM nous permet d'apprécier leurs différences et comment VIM s'est adapté pour répondre aux besoins des développeurs.

De plus, apprendre à installer et utiliser GVim, la version graphique de VIM, offre une introduction plus accessible pour les nouveaux utilisateurs.

### Personnalisation et plugins

Découvrir VimScript, le langage de script utilisé pour étendre les fonctionnalités de VIM, vous permet d'automatiser des tâches et de créer des commandes personnalisées.

En plongeant dans les fichiers de configuration de VIM, nous apprenons à personnaliser notre environnement d'édition. En utilisant des gestionnaires de plugins, nous pouvons étendre les capacités de VIM avec des plugins développés par la communauté.

Janus, une distribution populaire de VIM qui vient pré-configurée avec une suite de plugins et de paramètres, offre une installation simplifiée. Installer et expérimenter avec Janus, et apprendre à utiliser Vim Plug, un gestionnaire de plugins minimaliste, nous aide à gérer les plugins VIM efficacement.

NeoVIM, un refactor moderne de VIM conçu pour améliorer les performances et l'extensibilité, offre des fonctionnalités améliorées et une meilleure expérience utilisateur. Explorer NeoVIM et ses capacités améliore encore notre compréhension de la polyvalence de VIM.

Enfin, Vimium, une extension de navigateur qui apporte la navigation de style VIM sur le web, montre l'influence des raccourcis clavier de VIM au-delà de l'édition de texte traditionnelle.

# Commandes principales de VIM

### Intégration avec les IDE

Apprendre comment VIM peut être intégré dans d'autres environnements de développement intégrés (IDE) combine l'efficacité de VIM avec les fonctionnalités des IDE modernes. Installer des extensions VIM dans des IDE populaires comme Visual Studio Code nous permet d'utiliser les capacités d'édition de VIM dans un environnement familier.

### Navigation et édition de base

Maîtriser les touches de la ligne de base, qui sont centrales dans la structure de commande de VIM, augmente notre vitesse et notre efficacité d'édition. VIM fonctionne dans différents modes, chacun conçu pour des types spécifiques de tâches, et comprendre et basculer entre ces modes est crucial pour une utilisation efficace. Pratiquer les modes normal, insertion, visuel et ligne de commande nous aide à nous familiariser avec la nature modale de VIM.

### Commandes de fichier et de mouvement

Apprendre les commandes pour ouvrir, sauvegarder et fermer des fichiers est essentiel pour gérer notre travail dans VIM. Les commandes de mouvement nous permettent de naviguer dans le texte efficacement, avec les mouvements directionnels (h, j, k, l) étant les mouvements de base utilisés pour naviguer dans le texte.

Pratiquer l'utilisation des commandes de mouvement directionnel pour se déplacer rapidement dans le texte, ainsi que l'apprentissage des mouvements de saut pour sauter à des emplacements spécifiques dans le fichier, améliore nos compétences de navigation dans le texte.

Les mouvements de mot permettent de naviguer par mots, ce qui facilite le déplacement dans le texte, et la commande de jointure de lignes de texte de manière transparente est une commande utile pour la mise en forme du texte.

Les commandes pour naviguer rapidement au début ou à la fin d'une ligne, la commande de remplacement pour des substitutions rapides de texte, et les commandes d'annulation et de rétablissement pour gérer les changements efficacement font toutes partie de notre boîte à outils VIM de base.

### Édition avancée

La commande de changement nous permet de remplacer des portions de texte efficacement, tandis que la commande de suppression nous aide à supprimer du texte rapidement.

Copier (yanking) et coller du texte sont des opérations fondamentales dans VIM, et apprendre les commandes d'insertion et d'ajout nous permet d'ajouter du texte de différentes manières.

La commande d'insertion de ligne pour insérer des lignes de texte efficacement, la commande de recherche pour localiser du texte spécifique rapidement, et la commande de substitution pour remplacer des motifs de texte sont toutes des techniques d'édition avancées qui augmentent notre efficacité.

La touche leader est un raccourci personnalisable qui simplifie les séquences de commandes complexes, et maîtriser le mode visuel pour la sélection et la manipulation de texte est essentiel pour une édition efficace.

Les commandes d'indentation nous aident à formater correctement le code et le texte, et le fractionnement de fenêtre nous permet de travailler avec plusieurs fichiers ou vues simultanément.

Comprendre les buffers pour gérer plusieurs fichiers ouverts, et les registres pour stocker et récupérer des extraits de texte pour réutilisation, complète nos capacités d'édition avancées.

# Conclusion

À la fin de ce cours, vous aurez une base solide dans VIM, vous permettant de l'utiliser efficacement dans votre travail de développement. Regardez le cours complet sur la [chaîne YouTube freeCodeCamp.org](https://youtu.be/JYNA9j8SXs4) (4 heures de visionnage).

%[https://youtu.be/JYNA9j8SXs4]