---
title: 'Le Google Doc du Codage : Git & GitHub'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-23T01:16:38.000Z'
originalURL: https://freecodecamp.org/news/the-google-doc-of-coding-git-github-ec103e87926d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e5O_94Tw9eUfUAbQVnVr_Q.png
tags:
- name: Collaboration
  slug: collaboration
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Le Google Doc du Codage : Git & GitHub'
seo_desc: 'By Yung L. Leung

  Introduction

  Google Doc is a server-side (online) word processor. A user’s files are created
  via a web browser & stored in a server. This software makes it possible for users
  to share documents with others for collaboration. Normally...'
---

Par Yung L. Leung

### **Introduction**

Google Doc est un traitement de texte côté serveur (en ligne). Les fichiers d'un utilisateur sont créés via un navigateur web et stockés sur un serveur. Ce logiciel permet aux utilisateurs de partager des documents avec d'autres pour collaborer. Normalement, le flux de travail est le suivant :

* Créer un document et le remplir avec du contenu.
* Enregistrer le contenu et partager le fichier avec d'autres pour collaboration.
* Les membres contribuent sur le même document, en ligne.

Outre le partage de fichiers, une autre fonctionnalité importante est la possibilité d'annuler ou de refaire les modifications apportées au fichier 'master'. Les modifications apportées au document sont séquentielles et tout utilisateur peut annuler (ou refaire) ces modifications.

![Image](https://cdn-media-1.freecodecamp.org/images/Wk3M8qv3BVmUo8xK8WTiFKo8qtJzdOlOuc59)

Mais cela peut rapidement devenir un grand désordre, surtout lorsque plusieurs utilisateurs ajoutent ou modifient simultanément du contenu. Qui a créé ou modifié quel contenu et pour quelle raison est inconnu.

### Atom, Git & GitHub

En développement logiciel, les outils pour la programmation collaborative consistent en un éditeur de texte, un système de contrôle de version et un dépôt en ligne.

**Atom** (ou tout autre éditeur de texte) est comme votre traitement de texte côté client (bureau), sauf que le document est du code écrit dans un certain langage (par exemple : JavaScript).

**Git** est un outil pour enregistrer sélectivement l'historique des modifications enregistrées de votre projet. C'est un moyen de 'contrôler' toutes les différentes versions de votre projet de programmation.

**GitHub** est comme votre Google Docs, sauf que vous pouvez créer et enregistrer votre version du code hors ligne, avant de la 'pousser' pour qu'elle soit enregistrée en ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/jLU1vB1GLr3vSedxMo-viUIvU4HtNfzCfrnY)
_Atom, Git & GitHub_

Ainsi, vous avez votre **éditeur de texte** (Atom), votre **système de contrôle de version** (Git) et votre **système de stockage de fichiers à distance** (GitHub). Ce sont les éléments de base qui résolvent le problème de la collaboration, surtout pour les développeurs de logiciels. Le flux de travail est similaire à l'utilisation de Google Docs, avec quelques différences.

### Flux de travail pour le développement collaboratif de logiciels

1. **Créer un dépôt GitHub en ligne (à distance) ([https://github.com/new](https://github.com/new))**

![Image](https://cdn-media-1.freecodecamp.org/images/XEkgb2eqPgGSa7dz5imdRFXhyjcDzFfa8zJ1)

**2. Créer un dépôt hors ligne (local).** La commande terminal **git init** **_nom_du_projet_** lance votre projet en créant un dossier pour stocker son contenu et des fichiers de contrôle de version pour stocker un historique de ses modifications.

* L'idée est d'avoir finalement une copie locale et à distance de votre projet.

![Image](https://cdn-media-1.freecodecamp.org/images/YVsP0MYeOVIygYs4cz9x3NmjdsdRyue53aw7)

**3. Utiliser un éditeur de texte pour créer du contenu.** C'est ici que vous commencez à écrire votre programme avec Atom et à créer vos fichiers JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/BIlW7r0KUNAyOXzkjQbNrXmSykewezNpGQRv)
_Codage avec un éditeur de texte Atom_

**4. Enregistrer le contenu et noter les progrès historiques significatifs dans votre projet.** La commande terminal **git add .** ajoute tout le contenu du dossier, toutes les modifications, **_à être validées_** dans l'historique. La commande **git commit -m 'message'** valide les modifications dans l'historique, avec un message expliquant les modifications apportées. La commande **git push** pousse vos fichiers et données historiques vers votre dépôt à distance.

* Au fur et à mesure que vous faites des progrès continus dans votre projet, vous enregistrez la logique derrière chaque étape de développement (git add, git commit, git push).

![Image](https://cdn-media-1.freecodecamp.org/images/sphMS4DSgfC8zZI4yky53GMI-6gWU5qCVdRQ)
_Votre copie locale et à distance grandit à chaque push._

**5. Partager le fichier avec d'autres pour collaboration.** Une fois que votre dépôt à distance contient du contenu, vous pouvez partager votre projet avec des collaborateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/Viri6BCHeiLtcq9cxUGYFMGUmqNQ1pkUAHIa)

* Après que les membres ont accepté l'invitation, ils peuvent créer une branche à partir du dépôt à distance et cloner le projet localement (**git clone** **_<url_du_depot_ou_ssh>_).

![Image](https://cdn-media-1.freecodecamp.org/images/wUhCAZn3Q6ieiNbNo9KK3Y3o4bRkytIGIPh-)
_Créateur avec deux collaborateurs construisant du contenu sur des clones du projet._

* Chaque collaborateur peut créer du contenu, enregistrer le contenu et le pousser vers leur branche à distance.
* Au fur et à mesure que les collaborateurs continuent à créer et à enregistrer leur contenu, ils finissent par créer des branches dans le 'ciel' GitHub (**git add**, **git commit**, **git push**).

![Image](https://cdn-media-1.freecodecamp.org/images/AiMhl6s958Kgw6Q1Ev1xoHTiHEjftaId7yWC)
_Créateur et collaborateurs développant le projet et le poussant vers GitHub._

* Chaque branche est un collaborateur qui se détache du projet original afin que les membres puissent travailler en parallèle avec le créateur, sans perturber les progrès des uns et des autres. Chaque fois qu'un collaborateur effectue un **git push**, la branche s'allonge.

**6. Fusionner les fichiers branchés.** À la demande des collaborateurs, le **créateur** peut tirer leur branche pour la fusionner avec la branche principale.

![Image](https://cdn-media-1.freecodecamp.org/images/NKXd9qyn0FphVnA-rAwtUXDesF7arDnJCRut)
_Les collaborateurs poussent et soumettent des demandes de tirage. Le créateur tire les clones et fusionne les branches._

* Lorsqu'un collaborateur soumet une demande de tirage, le créateur peut effectuer un **git pull** pour fusionner les branches en une seule version mise à jour du projet. Cette nouvelle version peut ensuite être poussée dans le dépôt à distance pour que tout le monde puisse la voir et l'utiliser.

### Contrôle de version et partage de fichiers

Dans le développement collaboratif de logiciels, des modifications sont apportées à plusieurs clones d'une copie principale, avant qu'elles ne soient fusionnées dans le fichier principal. Ainsi, les modifications apportées sont séquentielles, mais avec des chevauchements dans le temps.

![Image](https://cdn-media-1.freecodecamp.org/images/uh4g7TmUn95gPVPP3SV1Z-HXTtDzZnCZkXeh)
_Les collaborateurs créent des branches, poussent et fusionnent leurs branches avec le créateur, à différents moments._

Chaque nouveau morceau de contenu créé sur un clone est finalement poussé vers le dépôt principal d'un collaborateur. Chaque message de validation d'un collaborateur fournit des commentaires au créateur afin qu'il puisse apporter des modifications et des ajouts intelligibles au projet original.

Cela serait une tâche difficile sans le **contrôle de version de Git** et le **partage de fichiers de GitHub**. Une simple commande terminal (**git branch <nom_de_la_branche>**) peut prendre un clone sur une machine locale et créer une branche afin qu'une version différente du projet puisse être développée. Un utilisateur peut ensuite noter ses progrès (git add & git commit) à tout moment. S'il y avait des problèmes avec une version active, l'utilisateur peut simplement basculer vers une branche précédente (git checkout <nom_de_la_branche>) et continuer à partir de là.

C'est la signification du **contrôle de version**. À tout moment, un utilisateur peut basculer vers des versions alternatives d'un projet, tout en validant des notes intelligibles qui expliquent la progression de chaque version. L'utilisateur a un contrôle total sur les versions qui sont développées. Une simple poussée terminal vers les 'nuages' GitHub rend toute version disponible à leurs collaborateurs. C'est la puissance d'utiliser Git & GitHub dans le développement collaboratif de logiciels.

**Références :**

[**Git - Vidéos**](https://git-scm.com/videos)
[_Edit description_git-scm.com](https://git-scm.com/videos)[**_Apprendre Git avec Bitbucket Cloud_ | Tutoriel Git Atlassian**](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)
[Apprendre Git avec Bitbucket Cloudwww.atlassian.com](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)[**Comment fonctionne Google Docs**](https://computer.howstuffworks.com/internet/basics/google-docs5.htm)
[_Back End de Google Docs - Le back end de Google Docs repose sur du matériel et des logiciels simples et peu coûteux. En savoir plus..._computer.howstuffworks.com](https://computer.howstuffworks.com/internet/basics/google-docs5.htm)[**Atom (éditeur de texte) - Wikipédia**](https://en.wikipedia.org/wiki/Atom_(text_editor))
[_Atom est un éditeur de texte et de code source gratuit et open-source pour macOS, Linux et Microsoft Windows avec support pour..._en.wikipedia.org](https://en.wikipedia.org/wiki/Atom_(text_editor))[**Git - Wikipédia**](https://en.wikipedia.org/wiki/Git)
[_Git () est un système de contrôle de version distribué pour suivre les modifications du code source pendant le développement logiciel. C'est..._en.wikipedia.org](https://en.wikipedia.org/wiki/Git)[**GitHub - Wikipédia**](https://en.wikipedia.org/wiki/GitHub)
[_GitHub propose des plans pour les comptes entreprise, équipe, pro et gratuits qui sont couramment utilisés pour héberger des logiciels open-source..._en.wikipedia.org](https://en.wikipedia.org/wiki/GitHub)