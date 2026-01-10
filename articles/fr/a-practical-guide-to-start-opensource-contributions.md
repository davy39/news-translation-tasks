---
title: Open Source pour les Développeurs – Un Guide pour Débutants pour Vous Aider
  à Commencer à Contribuer
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2022-09-02T16:34:40.000Z'
originalURL: https://freecodecamp.org/news/a-practical-guide-to-start-opensource-contributions
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Open-Source-for-Developers-Book-Cover--1-.png
tags:
- name: community
  slug: community
- name: open source
  slug: open-source
seo_title: Open Source pour les Développeurs – Un Guide pour Débutants pour Vous Aider
  à Commencer à Contribuer
seo_desc: What comes to mind when you hear the term Open Source? In the programming
  world, open source is a generic term for Open Source Software (OSS). Open-source
  software is built on source code that's open to everyone to view, change, extend,
  and distribut...
---

Qu'est-ce qui vous vient à l'esprit lorsque vous entendez le terme `Open Source` ? Dans le monde de la programmation, l'open source est un terme générique pour désigner les logiciels open source (OSS). Les logiciels open source sont construits sur un code source ouvert à tous pour le consulter, le modifier, l'étendre et le distribuer.

Dans cet article, nous aborderons de nombreux aspects des logiciels open source et de leur écosystème. Nous discuterons de ce qu'il faut pour commencer à contribuer à l'open source, des compétences dont vous avez besoin, de la manière de maintenir des projets open source, des défis, des ressources et de quelques projets passionnants pour commencer.

Avant de commencer, voici quelques mots sur moi et mon intérêt pour le monde de l'open source. 

J'utilise quotidiennement des projets, des produits et des services open source et je contribue à certains d'entre eux pour améliorer ce que je peux. Je maintens également de nombreux projets open source pour éduquer les débutants sur la programmation web. 

Vous pouvez consulter les projets open source que je maintens sur mon [Profil GitHub](https://github.com/atapas). 

Cet article vise à partager mon expérience avec vous pour vous aider à commencer avec l'open source, si vous ne contribuez pas déjà.

## Comment Fonctionne l'Open Source ?

Les projets open source se composent des personnes et éléments suivants :

`Mainteneur(s) du Projet` : Les mainteneurs sont une ou plusieurs personnes qui lancent le projet open source, le gèrent, prennent des décisions, réfléchissent à des idées et travaillent en étroite collaboration avec les contributeurs, les utilisateurs et les plateformes de marketing. 

Les mainteneurs du projet auront des droits et privilèges d'accès supplémentaires pour contrôler divers aspects du projet.

`Contributeur(s) du Projet` : Lorsque le ou les mainteneurs lancent un projet open source, ils en sont les premiers contributeurs. À mesure que le projet grandit et que plus de personnes en apprennent davantage, la volonté de contribuer augmente.

À mesure qu'il grandit, le projet attire plus de contributeurs. Chacun peut examiner le code du projet, le modifier, demander une révision et intégrer les changements au projet.

`Dépôt de Code Source et de Documentation` : Le mainteneur conserve le code source du projet dans un dépôt centralisé de code source (par exemple, GitHub). Cela aide tous les contributeurs à avoir l'accès nécessaire au code pour contribuer.

`Licence du Projet` : Chaque projet open source doit spécifier une licence de distribution pour clarifier les choses pour ses utilisateurs/consommateurs. 

Différents types de licences existent, et le mainteneur peut en choisir une en fonction de ce qui convient au projet. Certaines licences de distribution courantes sont MIT, Apache License 2.0, GNU General Public License (GPL) 3.0, etc.

`Guide de Contribution` : Un mainteneur du projet OSS crée un guide de contribution pour aider les contributeurs à comprendre le processus de pull request, les normes, la portée, etc.

`Guide de Code de Conduite` : Le guide de code de conduite discute des différentes directives, de la collaboration, des attentes comportementales des contributeurs et de la manière d'escalader et de résoudre les problèmes.

`Culture du Projet` : La culture du projet évolue avec la communauté du projet. Bien que les mainteneurs aient un intérêt significatif, les contributeurs sont également responsables du maintien d'une culture saine d'apprentissage, de partage et de croissance.

`Communauté` : À mesure que le projet grandit, la communauté se construit autour de lui. Des outils comme GitHub Discussions et Discord sont célèbres pour organiser des interactions basées sur la communauté.

`Distribution` : Le projet open source doit avoir un moyen d'atteindre ses utilisateurs finaux et ses consommateurs. Il doit y avoir un modèle de distribution aidant le code à se traduire en produit final pour la livraison.

`Utilisateurs/Clients` : Les utilisateurs ou clients sont les consommateurs du produit que l'équipe open source construit à l'aide du code source.

Maintenant, jetons un coup d'œil à l'image ci-dessous. Ici, nous voyons une communauté de projet open source incluant des mainteneurs et des contributeurs. 

Le code source est dans le dépôt centralisé. Les contributeurs `forkent` (un terme que nous apprendrons bientôt) le `dépôt upstream` et contribuent. Une fois la contribution terminée, le mainteneur du projet `fusionne` les changements avec la branche principale.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/opensource-model.png)
_Une Vue d'Ensemble du Modèle de Fonctionnement de l'Open Source_

Ne vous inquiétez pas si vous n'êtes pas familier avec des termes comme fork, branche, fusion, etc. Nous les apprendrons bientôt dans cet article. Continuez simplement à lire.

Maintenant, comprenons comment les logiciels open source sont livrés aux utilisateurs/clients. 

L'image ci-dessous montre l'une des nombreuses possibilités à un niveau élevé. Le projet open source doit avoir un mécanisme de construction-paquetage-déploiement utilisant le processus d'Intégration Continue et de Déploiement Continu (CI/CD).

Chaque fois qu'il y a des changements de code dans la `branche principale`, le flux de travail CI/CD se lance automatiquement. Il construit le code source, le package et le déploie pour qu'il soit accessible aux utilisateurs finaux et aux clients cibles.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/deploy.png)
_Une Vue d'Ensemble de la Manière dont le CODE SOURCE Atteint les UTILISATEURS_

Veuillez noter : Le CI/CD ou tout autre mécanisme de déploiement ne fait pas fermement partie du développement de logiciels open source. Cependant, le connaître aide à comprendre le modèle de fonctionnement de l'OSS de bout en bout.

## Que Signifie la Contribution Open Source ?

La contribution `Open Source` signifie améliorer le projet open source par tous les moyens. L'une des idées fausses que vous pourriez avoir sur la contribution est que vous devez contribuer uniquement au code source. Eh bien, ce n'est pas tout.

Contribuer au code source d'un projet open source n'est qu'un type de contribution que vous pouvez faire. Cependant, vous pouvez contribuer à d'autres domaines comme,

* La documentation du projet. Améliorez-la afin que davantage de contributeurs et d'utilisateurs la trouvent facile à utiliser.
* Testez l'application, trouvez des problèmes et créez des tickets dans le système de gestion des problèmes.
* Participez aux revues de code pour aider le projet avec de meilleures normes de codage.
* Écrivez des tests unitaires, des tests de bout en bout et améliorez la qualité de l'application.
* Créez du contenu comme des articles et des vidéos pour sensibiliser au projet.
* Aidez à construire la communauté de personnes intéressées.

Toutes les contributions ci-dessus sont cruciales pour les projets open source.

## Avantages des Contributions Open Source

Les contributions à l'Open Source offrent de nombreux avantages aux développeurs. Voici quelques avantages clés :

* Avoir l'opportunité de développer vos compétences.
* Améliorer le logiciel/application avec du code et de la documentation.
* Rencontrer des personnes partageant les mêmes idées, construire des réseaux et des communautés.
* Comprendre les cycles de développement et de maintenance des applications.
* Apprendre des retours sur les Pull Requests.
* Apprendre à gérer votre code en open source.

## Mythes sur l'Open Source

Nous sommes maintenant conscients du modèle Open Source et de ses avantages. La prochaine chose que nous voulons apprendre est comment commencer à contribuer à l'Open Source, à la fois en tant que `mainteneur` du projet et en tant que `contributeur`.

Avant de faire cela, clarifions certains mythes sur l'Open Source.

❌ **Mythe** : Je ne sais pas coder. L'Open Source n'est pas fait pour moi.

✅ **Fait** : L'Open Source ne concerne pas uniquement le codage ! Vous avez de nombreuses opportunités de contribuer à l'amélioration de la documentation, aux tests, à la création de médias, à la création de contenu, et bien plus encore. Ne restez donc pas en arrière en pensant que le manque de codage peut vous empêcher de contribuer à l'OSS.

❌ **Mythe** : Je sais coder mais je ne suis pas familier avec la technologie utilisée dans ce projet Open Source. Je ne peux pas contribuer.

✅ **Fait** : Au contraire, c'est une excellente opportunité d'apprendre quelque chose que vous ne connaissez pas déjà ! L'écosystème Open Source est suffisamment patient pour vous donner le temps d'apprendre et de contribuer.

❌ **Mythe** : L'Open Source ne maintient pas un niveau de standard d'entreprise.

✅ **Fait** : Pas vrai du tout. En fait, de nombreux logiciels d'entreprise sont alimentés par des logiciels Open Source aujourd'hui. Il est incorrect de supposer que les projets Open Source ne se soucient pas de la qualité et des standards.

❌ **Mythe** : Les projets Open Source ne sont pas faciles à maintenir.

✅ **Fait** : Un projet Open Source est soutenu par des contributeurs. Un aspect essentiel pour un mainteneur est de poser les bases, de créer une feuille de route, de construire la communauté et de maintenir la motivation élevée. 

Pour de nombreux projets Open Source, les mainteneurs n'ont même pas besoin de coder. Les contributeurs peuvent faire avancer les choses à condition que le mainteneur apporte le soutien nécessaire.

❌ **Mythe** : Les logiciels Open Source sont toujours gratuits.

✅ **Fait** : La plupart le sont, mais tous les OSS ne sont pas gratuits. Cela dépend du type de licence utilisée par le projet. Certaines licences sont restrictives pour donner un accès gratuit à l'utilisation et à la distribution du code de quelque manière que ce soit. Vous devez porter une attention particulière aux informations de licence d'un projet pour comprendre "à quel point" l'OSS sera gratuit.

❌ **Mythe** : L'Open Source est pour les débutants.

✅ **Fait** : De nombreux développeurs pensent que l'OSS est pour les débutants et les étudiants. En fait, tout le monde est le bienvenu pour contribuer. Il est logique pour un expert en la matière d'améliorer un projet Open Source avec ses connaissances et son expérience.

## Ce qu'il faut Savoir pour Commencer avec l'Open Source

Les développeurs doivent connaître quelques bases pour commencer rapidement avec les projets Open Source. Ce sont des prérequis optionnels, mais si vous vous en informez, vous apprécierez encore plus de contribuer à l'Open Source.

### Connaître les Bases de Git

Vous avez un avantage si vous connaissez déjà le concept de Git et son utilisation principale. Git est omniprésent dans le monde de l'Open Source, et vous ne pouvez pas l'ignorer.

Vous devez connaître ces sujets au minimum,

* Qu'est-ce que Git et comment fonctionne-t-il ?
* Qu'est-ce qu'un dépôt ?
* Comment cloner un dépôt ?
* Comment mettre en scène/annuler la mise en scène des changements ?
* Comment valider vos changements ?
* Comment écrire de meilleurs messages de validation ?
* Comment résoudre les conflits de fusion ?
* Comment pousser vos changements vers un dépôt distant ?
* Comment tirer les changements du dépôt distant ?

Si vous êtes nouveau dans Git, je recommande cette vidéo pour vous aider à apprendre les concepts de Git et toutes les utilisations mentionnées ci-dessus : [Démystifier Git pour les Débutants](https://www.youtube.com/watch?v=vWtu4mzUgQo).

### Devenir Familier avec GitHub

Il y a 128M+ dépôts publics sur [GitHub](https://github.com/). Une partie significative de ces dépôts sont des projets Open Source. Le projet Open Source auquel vous souhaitez contribuer peut également être sur GitHub. Vous devez donc apprendre à gérer les choses sur GitHub.

En tant que contributeur à un projet Open Source, vous devez savoir :

* Comment fork un dépôt ?
* Comment trouver l'URL pour cloner le dépôt ?
* Comment créer une Pull Request ?
* Comment examiner une Pull Request ?

En tant que mainteneur de projet, vous devez savoir,

* Comment créer un dépôt ?
* Comment ajouter des informations de licence au projet ?
* Comment créer un guide de contribution et un guide de code de conduite ?
* Comment définir une norme pour la création de problèmes et de pull requests ?
* Comment fusionner les pull requests ?

Vous pouvez suivre le fil Twitter ci-dessous. Il explique tout de manière étape par étape pour vous,

%[https://twitter.com/tapasadhikary/status/1440296182396309513]

### Apprendre à Fork un Dépôt

Le forking est un autre concept crucial à comprendre. La plupart des projets `Open Source` ne permettront pas à un contributeur de créer des branches directement sur un dépôt. Au lieu de cela, le flux de travail de contribution peut se dérouler comme suit :

* Fork le dépôt.
* Clone le dépôt forké.
* Effectue des changements.
* Obtiens les changements de l'UPSTREAM.
* Crée une pull request du dépôt forké vers le dépôt de base.

Dans mon expérience de travail avec de nombreux contributeurs, la plupart d'entre eux trouvent le concept de forking un peu difficile. 

Vous pouvez consulter ce tutoriel vidéo pour apprendre [Comment Fork un Dépôt GitHub](https://www.youtube.com/watch?v=h8suY-Osn8Q). Vous pouvez également trouver ce [dépôt GitHub](https://github.com/atapas/fork-me) pour pratiquer le forking. Il est destiné aux débutants absolus pour gagner en confiance dans le forking d'un dépôt.

### Apprendre à Résoudre les Conflits de Fusion

Demandez à n'importe quel développeur ce qu'il pense de la résolution des conflits de fusion. Eh bien, ce n'est pas très simple à faire, mais plus vous y êtes confronté, mieux vous apprenez. Comprenez le processus de résolution des conflits de fusion, comment y réfléchir et comment résoudre un conflit de fusion.

Voici un [guide pratique avec des exemples pour apprendre à résoudre les conflits de fusion](https://www.freecodecamp.org/news/resolve-merge-conflicts-in-git-a-practical-guide/). Veuillez y jeter un coup d'œil.

### Apprendre la Syntaxe Markdown

La documentation est l'un des besoins principaux de tout projet Open Source. Un fichier `Readme.md` explique le projet, comment le configurer, l'exécuter, le déployer, etc. 

Le fichier `Contributing.md` discute de la manière de contribuer au projet. 

Le fichier `CODE_OF_CONDUCT.md` décrit ce que l'on peut attendre du comportement et de l'engagement d'un contributeur. Bien sûr, vous pouvez écrire de nombreux autres fichiers `.md` en fonction des besoins de votre projet.

Le `md` signifie markdown. Il s'agit d'une syntaxe utilisée pour la documentation sur GitHub. Il est préférable d'apprendre la syntaxe de base afin que vous puissiez participer à la documentation de manière transparente. 

Voici un projet Open Source qui fournit la syntaxe Markdown à copier et à utiliser. Vous pouvez y jeter un coup d'œil.

%[https://github.com/atapas/markdown-cheatsheet]

### Cultiver Vos Compétences Douces

L'`Open Source` est un terrain fertile pour de nombreux développeurs pour travailler, apprendre et construire ensemble. En tant que contributeur, vos compétences techniques peuvent ne pas suffire pour profiter pleinement de l'expérience open source. 

Discutons de quelques compétences douces indispensables pour les développeurs.

* **Patience** : La `patience` est une compétence indispensable pour les développeurs. Elle est nécessaire lorsque vous apprenez quelque chose de nouveau, déboguez un problème complexe, travaillez avec d'autres, négociez avec quelqu'un et recevez/donnez des retours. Parfois, les choses peuvent ne pas avancer au rythme que vous attendez, vous devez donc faire preuve de patience et évaluer la situation.
* **Curiosité** : Un esprit `curieux` va loin. Lorsque vous contribuez à l'open source, les possibilités sont immenses. Vous devez être curieux pour comprendre les choses. Cela ne s'applique pas seulement à la résolution des défis techniques, mais aussi lorsque vous travaillez avec des personnes. 
* **Être Réactif** : Dans l'écosystème Open Source, vous ne rencontrerez peut-être pas et ne parlerez pas aux gens quotidiennement, mais le travail doit continuer. Vous devez être `réactif` aux questions, tâches, demandes et tout ce dont vous êtes responsable. De nombreuses initiatives prometteuses s'éteignent simplement en raison d'un manque de réactivité des personnes.
* **Être Modeste** : Être `modeste` est la clé du succès. Une personne qui est compétente mais pas modeste échoue souvent à travailler en équipe.

## Comment Commencer à Contribuer aux Projets Open Source

Voyons maintenant comment commencer à contribuer à l'open source. La liste ci-dessous fournit des liens et des ressources pour vous permettre de commencer immédiatement à contribuer à l'open source.

### GitHub Explore

GitHub Explore vous montre les dépôts en fonction de vos intérêts. Vous pouvez configurer les notifications pour être informé d'un projet. 

De plus, vous pouvez rechercher des dépôts par sujets et tendances. Utilisez GitHub Explore pour trouver les projets les plus pertinents pour vos compétences, besoins et aspirations. Vous pouvez le trouver ici : [https://github.com/explore/](https://github.com/explore/)

### Comment Contribuer à l'Open Source par freeCodeCamp

Ce dépôt de freeCodeCamp est une véritable pépite. Il vous fournit de nombreuses ressources et conseils pour commencer avec l'open source. Vous pouvez le trouver ici : [https://github.com/freeCodeCamp/how-to-contribute-to-open-source](https://github.com/freeCodeCamp/how-to-contribute-to-open-source)

### Contributor Ninja

Ce site web vous aide avec une liste de langages de programmation parmi lesquels choisir – JavaScript, HTML, Rust, Go, et bien d'autres. Vous obtenez des cartes de dépôts parmi lesquelles sélectionner. C'est un endroit simple pour commencer. Vous pouvez le trouver ici : [https://contributor.ninja/](https://contributor.ninja/)

### First Contributions

Il s'agit d'une énorme liste de projets open source parmi lesquels rechercher et filtrer. Ils ont également une documentation bien guidée pour commencer. Vous pouvez le trouver ici : [https://firstcontributions.github.io/](https://firstcontributions.github.io/)

### CodeTriage

CodeTriage est une liste mammouth de projets avec des problèmes ouverts. Il montre une séparation des problèmes et des docs à trier. Le site web est très utile. Vous pouvez le trouver ici : [https://www.codetriage.com/](https://www.codetriage.com/)

### Up For Grabs

Il s'agit d'une liste complète de projets Open Source parmi lesquels choisir en fonction de vos intérêts. Vous pouvez le trouver ici : [https://up-for-grabs.net/#/](https://up-for-grabs.net/#/)

### First Timers Only

Si vous n'avez jamais contribué à un projet open source auparavant et que vous commencez tout juste, envisagez de lire cette page.

Vous y verrez de nombreuses sources que nous avons déjà discutées, mais la page est pleine de motivations. Vous pouvez la trouver ici : [https://www.firsttimersonly.com/](https://www.firsttimersonly.com/)

### Open Source Friday

Que faites-vous ce vendredi, ou le prochain ? Que diriez-vous d'investir quelques heures à contribuer au logiciel que vous utilisez et aimez. Veuillez consulter cela et vous inscrire. Vous pouvez le trouver ici : [https://opensourcefriday.com/](https://opensourcefriday.com/)

J'espère que vous avez trouvé les ressources utiles. De plus, n'hésitez pas à consulter ces fils Twitter et réponses, vous pourriez trouver plus d'informations à ce sujet. 

%[https://twitter.com/tapasadhikary/status/1435590663035310086]

## Mainteneurs de Projets Open Source

Jusqu'à présent, nous avons vu le côté des contributeurs open source. Cet article serait incomplet si nous n'abordions pas également le côté des mainteneurs de projets open source.

En tant que mainteneur du projet, vous devez suivre certaines normes pour que les autres puissent connaître et contribuer à votre dépôt de projet.

* Fournir un nom et une description clairs du projet. Vous devez également ajouter les sujets liés à votre projet.
* Ajouter un fichier `Readme.md` clair pour expliquer les objectifs du projet, comment l'utiliser, comment le configurer, etc. Si le code source est le cœur d'un dépôt, le fichier README en est le visage.
* Construire un profil de communauté. Cela aide les mainteneurs du dépôt open source à examiner le travail et à apprendre comment l'aider à grandir.
* Établir un Code de Conduite.
* Créer un Guide de Contribution.
* Décider des Modèles de Problèmes.
* Créer un Modèle de Pull Request (PR).
* Activer GitHub Sponsors.

[Vous pouvez consulter cet article pour en savoir plus](https://www.freecodecamp.org/news/increase-engagement-on-your-public-github-repositories/) sur ces normes en détail.

## Avant de Terminer...

C'est tout ! Nous voici arrivés à la fin de cet article. J'espère que vous l'avez trouvé instructif et qu'il vous a donné suffisamment de motivation pour commencer à contribuer à l'open source. 

Avant de terminer, je voudrais mentionner quelques projets et dépôts open source que vous pourriez consulter.

* [EddieHub](https://github.com/EddieHubCommunity)
* [ReactPlay](https://github.com/reactplay)
* [Hacktoberfest](https://github.com/topics/hacktoberfest)
* [First Contributions](https://github.com/firstcontributions/first-contributions)
* [The Hive](https://github.com/deleteman/the-hive)

Cette liste pourrait continuer à s'allonger, mais je vais m'arrêter ici. Si vous avez aimé lire cet article et/ou si vous avez des questions, souhaitez vous connecter, vous pouvez me trouver à ces endroits :

* [Suivre sur Twitter](https://twitter.com/tapasadhikary)
* [Se Connecter sur LinkedIn](https://www.linkedin.com/in/tapasadhikary/)
* [Connaître mon Travail sur GitHub](https://github.com/atapas)
* [S'abonner à ma Chaîne YouTube](https://youtube.com/tapasadhikary)