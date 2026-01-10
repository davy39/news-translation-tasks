---
title: Comment contribuer aux projets open source – Les aspects non techniques à connaître
subtitle: ''
author: Ayu Adiati
co_authors: []
series: null
date: '2023-09-14T17:34:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-contribute-to-open-source
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/How-to-Contribute-to-Open-Source-Projects-Non-Technical-Things-You-Should-Know--1-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: Comment contribuer aux projets open source – Les aspects non techniques
  à connaître
seo_desc: 'I''ve contributed to open-source projects for a few years and learned a
  lot from the process. These experiences allowed me to look closer at the open source
  flow, from the technical, such as Git and GitHub, to the non-technical aspects.

  Although they ...'
---

J'ai contribué à des projets open source pendant quelques années et j'ai beaucoup appris de ce processus. Ces expériences m'ont permis d'examiner de plus près le flux open source, des aspects techniques, tels que Git et GitHub, aux aspects non techniques.

Bien qu'ils soient aussi importants que les aspects techniques, les aspects non techniques sont souvent négligés. Dans cet article, je vais partager les aspects non techniques essentiels que vous devez connaître lorsque vous contribuez à des projets open source.

## Quels sont les fichiers importants dans un dépôt ?

Dans cette section, nous allons parler de certains des fichiers importants que vous rencontrerez probablement lorsque vous contribuerez à un projet open source.

### Le fichier `README.md`

Lorsque vous êtes intéressé à contribuer à un projet open source, vous devez toujours lire le fichier `README.md` – communément appelé README – pour vous familiariser avec le projet.

Le fichier `README.md` est la vitrine du projet, contenant tout ce qui est essentiel. Vous y trouverez généralement la plupart, sinon la totalité, de ces sections dans un README :

* La description du projet.
* La technologie utilisée pour le projet.
* Les instructions sur la façon d'installer, d'exécuter et d'utiliser le projet.
* La licence du projet.
* Le code de conduite.
* Comment contribuer au projet.
* Le style de communication attendu (via les commentaires des problèmes et des demandes de tirage, les discussions GitHub, les applications de service de chat telles que Slack ou Discord, et ainsi de suite).

### Le fichier `CONTRIBUTING.md`

Ensuite, vous devez connaître les règles à suivre pour contribuer à un projet. Les procédures et exigences pour contribuer peuvent différer entre les projets. Par exemple, dans certains projets, vous devez commenter un problème avant qu'il ne vous soit attribué, tandis que d'autres vous permettent de vous attribuer un problème vous-même.

Le fichier `CONTRIBUTING.md` sert de guide de contribution. Il explique les règles et attentes de la communauté à l'égard de leurs contributeurs, de la création d'un problème à la création d'une demande de tirage.

Dans la plupart des cas, vous trouverez une section de contribution dans le README. Mais si elle n'est pas incluse dans le README, vous pouvez la trouver dans un fichier nommé `CONTRIBUTING.md` ou quelque chose de similaire.

### Le fichier `LICENSE`

Vous ne pouvez pas simplement supposer que tous les projets sur GitHub sont open source et que leur base de code est librement disponible.

> "Dans la plupart des juridictions, tout code ou contenu est automatiquement protégé par le droit d'auteur par l'auteur, avec tous les droits réservés, sauf indication contraire." (Source : [Open source licenses: What, which, and why](https://arstechnica.com/gadgets/2020/02/how-to-choose-an-open-source-license/))

"Tous droits réservés" signifie que personne ne peut utiliser, modifier ou redistribuer quoi que ce soit dans le projet à moins que le propriétaire ne vous donne la permission de le faire. Si vous l'ignorez, ils peuvent légalement vous poursuivre. Donc, un projet sur GitHub n'est open source que s'il a une licence qui le spécifie.

Vous trouverez généralement une section de licence dans le README, dans la section "À propos" d'un dépôt. Elle se trouve dans un fichier appelé `LICENSE`.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/repo-about-section-github-1.png)
_Une licence MIT dans la section "À propos" sur la barre latérale droite d'un dépôt sur GitHub_

### Le fichier `CODE_OF_CONDUCT.md`

Vous devriez lire habituellement le Code de Conduite (COC) de la communauté. Le COC est la règle de la maison de la communauté. Il est là pour une raison : maintenir un espace sûr et accueillant pour les contributeurs. Suivre le COC vous empêchera d'être banni de la communauté et du projet.

Vous pouvez trouver le COC dans un fichier appelé `CODE_OF_CONDUCT.md`, dans la section "À propos" du dépôt. La plupart du temps, il est également inclus dans le README et le guide de contribution.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/code-of-conduct-on-github.png)
_Code de Conduite dans la section "À propos" sur la barre latérale droite d'un dépôt sur GitHub_

## **Éthique dans l'Open Source**

### Vérifier les doublons

Supposons que vous installez et exécutez un projet sur votre machine locale et que vous rencontrez un bug. Ou que vous lisez la documentation et que vous trouvez une étape manquante. Vous pourriez vouloir signaler un problème pour le résoudre.

Avant de le faire, vous devez vérifier si un problème ou une demande de tirage similaire (ouvert ou fermé) a été signalé pour éviter les doublons. Entrez des mots-clés possibles dans la barre de recherche en haut de la page des problèmes ou des demandes de tirage sur GitHub pour vérifier les éventuels doublons.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/search-bar-github.png)
_Barre de recherche en haut de la page des problèmes ou des demandes de tirage sur GitHub_

Par exemple :

```text
is:issue is:open docs 
```

```text
is:pull request is:closed button 
```

Vérifier les doublons aidera à éviter que votre problème ou votre demande de tirage ne soit rejeté par les mainteneurs.

### Demander la permission avant de travailler sur un problème

L'une des éthiques essentielles dans l'open source est de demander la permission du mainteneur pour travailler sur un problème, sauf indication contraire dans le guide de contribution. Demander la permission aide les mainteneurs à contrôler et à éviter les demandes de tirage en double.

Vous ne voulez travailler sur des changements et créer une demande de tirage qu'après avoir obtenu le feu vert d'un mainteneur. Si vous ignorez cette partie et que vous allez de l'avant pour travailler sur les changements, votre demande de tirage sera probablement ignorée ou rejetée. Cela peut être dû au fait que le problème a déjà été attribué à quelqu'un d'autre, ou que le problème n'est pas leur priorité à ce moment-là.

Dans les deux cas, ce serait une perte pour vous. Donc, que devez-vous faire lorsque vous demandez la permission ?

#### 1. Vérifiez si le problème a déjà été attribué

Vous pouvez voir si un problème a été attribué en regardant la colonne "Assigné" lorsque vous ouvrez l'onglet des problèmes dans le dépôt GitHub ou sur la barre latérale droite lorsque vous ouvrez le problème.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/issue-tab-github-01-3.png)
_Colonne Assigné sur la page des problèmes sur GitHub_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/issue-right-sidebar-01-3.png)
_Section Assignés sur la barre latérale droite de la page du problème sur GitHub_

#### 2. Vérifiez les fils de commentaires

Vous voulez également vous assurer que quelqu'un n'a pas déjà demandé aux mainteneurs de lui attribuer le problème. S'ils n'ont pas obtenu de réponse, alors les mainteneurs n'ont probablement pas vu le commentaire. Vous devriez également vérifier d'autres informations dans les fils pour mieux comprendre le problème.

#### 3. Laissez un commentaire pour demander un problème sur lequel vous souhaitez travailler

Vous pouvez dire : "Bonjour, je souhaite travailler sur ce problème. Pouvez-vous me l'attribuer ?" Ou, "Je vois que ce problème a été attribué, mais je n'ai pas vu d'activité ici depuis un moment. Si vous avez encore besoin d'aide, puis-je travailler sur ce problème ?"

#### 4. Attendez que le mainteneur réponde à votre message

S'ils (les mainteneurs) disent que vous pouvez l'avoir et vous l'attribuent, alors vous pouvez commencer à travailler sur le problème et, à la fin, créer une demande de tirage.

### Qu'est-ce que le label "Good First Issue" ?

Les labels sur GitHub sont des étiquettes qui transmettent des informations sur le type ou le statut d'un problème ou d'une demande de tirage. Un `good-first-issue` est un label considéré comme approprié pour les débutants par le propriétaire et les mainteneurs du projet.

J'ai déjà créé un problème concernant un lien brisé. J'ai expliqué le bug et les étapes que les contributeurs doivent suivre pour le résoudre.

J'ai également mentionné que ce problème est adapté aux débutants, donc nous voulons le laisser pour les débutants qui souhaitent contribuer au projet. Après avoir passé la revue des mainteneurs, le problème a été étiqueté comme un `good-first-issue`.

La partie triste était que les personnes qui ont délibérément pris le problème n'étaient pas des débutants.

Si vous avez déjà une certaine expérience, veuillez envisager de laisser ce label. Il est destiné aux débutants dans l'open source ou la technologie utilisée dans le projet.

### Bonne communication et patience

Utilisez toujours des mots clairs et polis pour communiquer avec les mainteneurs et les autres contributeurs. N'oubliez pas que la communication asynchrone est sujette à des pertes de traduction et à des malentendus.

Si vous avez besoin de plus de clarifications sur quelque chose, demandez aux mainteneurs. Ne faites pas de suppositions. Vous pouvez poser des questions dans les commentaires des problèmes ou des demandes de tirage. Certaines communautés ont également un tableau de discussions GitHub que vous pouvez trouver sur la barre supérieure, tandis que d'autres utilisent des applications de service de chat comme Slack ou Discord pour partager des idées et poser des questions ou des clarifications.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/discussion-tab-github.png)
_Onglet Discussions sur GitHub_

Un mainteneur peut vous demander de corriger quelque chose dans votre demande de tirage ou demander des clarifications en utilisant une phrase simple. Les messages courts et directs se produisent principalement parce qu'ils sont occupés. Ils doivent être rapides et efficaces pour répondre aux messages. Ne le prenez pas personnellement, car cela peut conduire à une mauvaise communication ou même à la perte de votre chance de contribuer.

La plupart des mainteneurs et contributeurs dans l'open source sont des bénévoles. Cela dit, ils ont une vie et d'autres devoirs en dehors du projet. Donc, lorsque vous contribuez, vous devez avoir de la patience. Ne demandez pas aux mainteneurs de répondre immédiatement à votre question ou de fusionner votre demande de tirage.

### Rédiger un problème et une demande de tirage de manière structurée

Certaines communautés open source fournissent des modèles sur GitHub pour ouvrir un problème ou créer une demande de tirage. Mais lorsqu'ils ne le font pas, envisagez de les rédiger de manière structurée. Cela serait pratique pour tout le monde de voir les détails et d'aider les mainteneurs à examiner et à fusionner les demandes de tirage.

#### Comment rédiger un problème GitHub

Voici quelques points à considérer lors de la rédaction d'un problème :

**Utilisez des titres clairs et descriptifs** : En lisant un titre clair et descriptif, tout le monde peut comprendre le problème. Par exemple, "fix: Le lien vers la page À propos mène à une erreur 404".

**Recherchez des problèmes similaires** : Vérifiez les problèmes ouverts et fermés pour voir s'il existe un problème similaire ou identique au vôtre. Si vous n'en trouvez pas, alors incluez dans la description que vous avez vérifié et n'avez pas trouvé de problèmes similaires. Cette étape est essentielle pour éviter toute duplication.

**Description du problème** : Décrivez le problème de la manière la plus directe possible.

**Comportement attendu** : Décrivez le comportement attendu d'un problème.

**Comportement actuel** : Indiquez le comportement problématique actuel qui cause le problème.

**Reproduire le problème** : Quelles étapes devons-nous suivre pour reproduire le problème ? Il serait utile pour tout le monde d'exécuter les mêmes étapes et de le tester. Voici un exemple :

```markdown
1. Allez à ce lien.
2. Cliquez sur ce bouton.
3. Voici ce qui se passe.
```

**Captures d'écran ou enregistrements d'écran** : Fournissez des captures d'écran ou des enregistrements d'écran si nécessaire. Cela est généralement bénéfique pour les problèmes d'interface utilisateur.

**Suggérer une solution** : Si vous avez une solution en tête, vous pouvez donner une suggestion. Mais si vous n'en avez pas, ce n'est pas grave non plus. Vous n'êtes pas censé avoir une solution lorsque vous signalez un problème.

Voici un exemple qui utilise les points listés ci-dessus :

```markdown
<!-- Titre du problème -->
# fix: Le lien vers la page À propos mène à une erreur 404

<!-- Corps du problème -->
## Description

Lorsque je suis allé à la page À propos, j'ai obtenu une erreur 404.
J'ai recherché et je n'ai pas trouvé de problèmes similaires.

## Comportement attendu

Nous devrions voir la section À propos lorsque nous allons à la page À propos.

## Comportement actuel

Lorsque nous allons à la page À propos, nous voyons une page d'erreur 404.

## Comment reproduire

1. Allez sur https://website.com.
2. Cliquez sur l'onglet À propos.
3. Vous verrez l'erreur 404.

## Captures d'écran

![404 dans la page à propos](lien vers l'image)

## Suggestion

Corrigez et utilisez le bon lien vers la page À propos.
```

#### Comment rédiger une demande de tirage

Voici quelques points à considérer lors de la rédaction d'une demande de tirage :

**Utilisez un titre court, clair et informatif** : Par exemple, "fix: Lien vers la page À propos".

**Utilisez une description claire de la correction** : Par exemple, "Cette demande de tirage corrige le lien vers la page À propos qui menait précédemment à une erreur 404".

**Lien vers le problème lié** : Incluez le lien vers le problème lié. Par exemple, "Corrige #123".

**Captures d'écran ou enregistrements d'écran** : Fournissez des captures d'écran ou des enregistrements d'écran qui montrent le problème avant et après la correction si nécessaire.

Voici un exemple qui utilise la structure ci-dessus :

```markdown
<!-- Titre de la demande de tirage -->
# fix: Lien vers la page À propos

<!-- Corps de la demande de tirage -->
## Problème lié

Corrige #123

## Description

Cette PR corrige le lien vers la page À propos qui menait précédemment à une erreur 404.

## Captures d'écran

### Avant

![404 dans la page à propos](lien vers l'image)

### Après

![Page à propos](lien vers l'image)
```

## Bon à savoir : Contribuer à l'Open Source ne concerne pas seulement le code

J'entends souvent dire que les gens – surtout les débutants – hésitent à contribuer à l'open source parce qu'ils n'ont pas assez de compétences ou de temps pour aider avec le code. Cependant, contribuer à un projet open source implique plus que simplement du code.

Il existe de nombreuses façons non techniques de contribuer à un projet et à sa communauté, telles que :

* Ouvrir un problème lorsque vous voyez un bug ou une possibilité d'amélioration.
* Examiner les problèmes et les demandes de tirage.
* Améliorer la documentation du projet.
* Répondre aux questions.
* Proposer des idées autour du projet.
* Intégrer de nouveaux contributeurs.
* Mentorer d'autres contributeurs.
* Rédiger un article de blog ou créer une vidéo sur le projet.
* Promouvoir le projet sur les réseaux sociaux, et bien plus encore !

## Mots de la fin

Contribuer à des projets open source ne concerne pas seulement la compréhension de Git et GitHub. Certains aspects non techniques sont également importants à connaître. J'espère que cet article vous aidera.

Si vous avez aimé et apprécié cet article, veuillez le partager. Vous pouvez trouver d'autres travaux de moi sur mon [blog](https://adiati.com), et connectons-nous sur [X (anciennement Twitter)](https://twitter.com/@AdiatiAyu) ou [LinkedIn](https://www.linkedin.com/in/adiatiayu/)!