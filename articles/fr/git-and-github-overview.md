---
title: Git vs GitHub – Qu'est-ce que le contrôle de version et comment fonctionne-t-il
  ?
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2020-08-19T16:06:01.000Z'
originalURL: https://freecodecamp.org/news/git-and-github-overview
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9928740569d1a4ca1e25.jpg
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: version control
  slug: version-control
- name: Web Development
  slug: web-development
seo_title: Git vs GitHub – Qu'est-ce que le contrôle de version et comment fonctionne-t-il
  ?
seo_desc: 'Have you ever been confused by how Git and GitHub work? Don’t fret — you
  are not alone. Git and GitHub can be tricky sometimes, but by the end of this post
  you will have a good grasp of the two.

  At first, it may be tempting to believe Git and GitHub ...'
---

Avez-vous déjà été confus quant au fonctionnement de Git et GitHub ? Ne vous inquiétez pas – vous n'êtes pas seul. Git et GitHub peuvent parfois être délicats, mais à la fin de cet article, vous aurez une bonne compréhension des deux.

Au début, il peut être tentant de croire que Git et GitHub sont la même chose. Mais en réalité, ils ne le sont pas. En effet, il est possible d'utiliser Git sans GitHub ! Et finalement, les deux existent pour des objectifs différents.

Cet article commencera par examiner attentivement les objectifs de Git et GitHub. Ensuite, nous apprendrons les principales différences entre ces deux technologies vitales.

Sans plus tarder, commençons avec Git.

## Qu'est-ce que Git ?

Git est un système de contrôle de version distribué (DVCS) utilisé pour sauvegarder différentes versions d'un fichier (ou d'un ensemble de fichiers) afin que toute version puisse être récupérée à volonté.

Git facilite également l'enregistrement et la comparaison de différentes versions de fichiers. Cela signifie que les détails sur ce qui a changé, qui a changé quoi, ou qui a initié un problème sont consultables à tout moment.

Mais si Git est un système de contrôle de version distribué, que signifient exactement ces termes ?

### Que signifie « distribué » ?

Le terme « distribué » signifie que chaque fois que vous demandez à Git de partager le répertoire d'un projet, Git ne partage pas seulement la dernière version du fichier. Au lieu de cela, il distribue chaque version qu'il a enregistrée pour ce projet.

Ce système « distribué » contraste fortement avec d'autres systèmes de contrôle de version. Ils ne partagent que la version unique qu'un utilisateur a explicitement extraite de la base de données centrale/locale.

D'accord, donc « distribué » signifie distribuer _toutes_ — et non pas seulement quelques-unes sélectionnées — les versions des fichiers d'un projet que Git a enregistrées. Mais qu'est-ce qu'un système de contrôle de version ?

### Qu'est-ce qu'un système de contrôle de version ?

Un système de contrôle de version (VCS) fait référence à _la méthode_ utilisée pour sauvegarder les versions d'un fichier pour référence future.

Intuitivement, de nombreuses personnes contrôlent déjà les versions de leurs projets en renommant différentes versions du même fichier de diverses manières comme `blogScript.js`, `blogScript_v2.js`, `blogScript_v3.js`, `blogScript_final.js`, `blogScript_definite_final.js`, et ainsi de suite. Mais cette approche est sujette aux erreurs et inefficace pour les projets d'équipe.

De plus, suivre ce qui a changé, qui l'a changé, et pourquoi il a été changé est une tâche fastidieuse avec cette approche traditionnelle. Cela met en lumière l'importance d'un système de contrôle de version fiable et collaboratif comme Git.

Cependant, pour tirer le meilleur parti de Git, il est essentiel de comprendre comment Git gère vos fichiers.

## États des fichiers dans Git

Dans Git, il existe trois états principaux (conditions) dans lesquels un fichier peut se trouver : **état modifié**, **état indexé**, ou **état validé**.

### État modifié

Un fichier dans l'état modifié est un fichier révisé — mais non validé (non enregistré) — fichier.

En d'autres termes, les fichiers dans l'état modifié sont des fichiers que vous avez modifiés mais que vous n'avez pas explicitement demandé à Git de surveiller.

### État indexé

Les fichiers dans l'état indexé sont des fichiers modifiés qui ont été sélectionnés — dans leur état actuel (version) — et sont préparés pour être sauvegardés (validés) dans le dépôt `.git` lors de la prochaine validation.

Une fois qu'un fichier est indexé, cela implique que vous avez explicitement autorisé Git à surveiller la version de ce fichier.

### État validé

Les fichiers dans l'état validé sont des fichiers stockés avec succès dans le dépôt `.git`.

Ainsi, un fichier validé est un fichier dont vous avez enregistré la version indexée dans le répertoire Git (dossier).

**Note :** L'état d'un fichier détermine l'emplacement où Git le placera.

## Emplacements des fichiers

Il existe trois endroits clés où les versions d'un fichier peuvent résider lors du contrôle de version avec Git : le **répertoire de travail**, la **zone de préparation**, ou le **répertoire Git**.

### Répertoire de travail

Le répertoire de travail est un dossier local pour les fichiers d'un projet. Cela signifie que tout dossier créé n'importe où sur un système est un répertoire de travail.

**Note :**

* Les fichiers dans l'état modifié résident dans le répertoire de travail.
* Le répertoire de travail est différent du répertoire `.git`. C'est-à-dire que vous créez un répertoire de travail tandis que Git crée un répertoire `.git`.
* Consultez [cet article de comparaison](https://www.codesweetly.com/git-vs-working-directory/) pour plus de différences entre les deux dépôts.

### Zone de préparation

La zone de préparation — techniquement appelée « index » dans le jargon Git — est un fichier, généralement situé dans le répertoire `.git`, qui stocke des informations sur les fichiers prêts à être validés dans le répertoire `.git`.

**Note :**

* Les fichiers dans l'état indexé résident dans la zone de préparation.

### Répertoire Git

Le répertoire `.git` est le dossier (également appelé « dépôt ») que Git crée à l'intérieur du répertoire de travail que vous lui avez demandé de suivre.

De plus, le dossier `.git` est l'endroit où Git stocke les bases de données d'objets et les métadonnées des fichiers que vous lui avez demandé de surveiller.

**Note :**

* Le répertoire `.git` est le cœur de Git — c'est l'élément copié lorsque vous clonez un dépôt depuis un autre ordinateur (ou depuis une plateforme en ligne comme GitHub).
* Les fichiers dans l'état validé résident dans le répertoire Git.

## Le flux de travail de base de Git

Travailler avec le système de contrôle de version Git ressemble à ceci :

![Diagramme du flux de travail de base de Git](https://www.freecodecamp.org/news/content/images/2020/08/git-basic-workflow-codesweetly.png)

1. Modifiez les fichiers dans le répertoire de travail.  
Notez que tout fichier que vous modifiez devient un fichier dans l'_état modifié_.
2. Indexez sélectivement les fichiers que vous souhaitez valider dans le répertoire `.git`.  
Notez que tout fichier que vous indexez (ajoutez) dans la zone de préparation devient un fichier dans l'_état indexé_.  
Sachez également que les fichiers indexés ne sont pas encore dans la base de données `.git`.  
Indexer signifie que les informations sur le fichier indexé sont incluses dans un fichier (appelé "index") dans le dépôt `.git`.
3. Validez le(s) fichier(s) que vous avez indexé dans le répertoire .git. C'est-à-dire, stockez de manière permanente une capture instantanée du(s) fichier(s) indexé(s) dans la base de données .git.  
Notez que toute version de fichier que vous validez dans le répertoire .git devient un fichier dans l'état validé.

### L'essentiel jusqu'à présent

En résumé, Git est un système de contrôle de version brillant pour le versionnage, la gestion et la distribution compétents de fichiers. Consultez [ce guide simple](https://www.codesweetly.com/how-to-use-git/) pour apprendre à utiliser Git efficacement.

Mais, attendez une seconde, si Git aide à gérer et distribuer efficacement différentes versions des fichiers d'un projet, quel est le but de GitHub ?

## GitHub démystifié

GitHub est une plateforme basée sur le web où les utilisateurs peuvent héberger des dépôts Git. Il vous aide à faciliter le partage et la collaboration sur des projets avec n'importe qui, à tout moment.

GitHub encourage également une participation plus large aux projets open-source en fournissant un moyen sécurisé de modifier des fichiers dans le dépôt d'un autre utilisateur.

Pour héberger (ou partager) un dépôt Git sur GitHub, suivez les étapes ci-dessous :

### Étape 1 : Inscription à un compte GitHub

La première étape pour commencer à héberger sur GitHub est de créer un compte personnel. Visitez la [page d'inscription officielle](https://github.com/join) pour vous inscrire.

### Étape 2 : Créer un dépôt distant dans GitHub

Après vous être inscrit à un compte, [créez un dépôt (repository) dans GitHub](https://docs.github.com/en/github/getting-started-with-github/create-a-repo) pour le dépôt Git que vous souhaitez partager.

### Étape 3 : Connecter le répertoire Git du projet au dépôt distant

Une fois que vous avez créé un dépôt distant pour votre projet, liez le répertoire `.git` du projet — situé localement sur votre système — avec le dépôt distant sur GitHub.

Pour vous connecter au dépôt distant, **allez dans le répertoire racine** du projet que vous souhaitez partager via votre terminal local, et exécutez :

```
git remote add origin https://github.com/yourusername/yourreponame.git
```

**Note :**

* Remplacez `yourusername` dans le code ci-dessus par votre nom d'utilisateur GitHub.  
De même, remplacez `yourreponame` par le nom du dépôt distant auquel vous souhaitez vous connecter.
* La commande ci-dessus implique que _git_ doit _ajouter_ l'URL spécifiée au projet local en tant que référence distante avec laquelle le répertoire `.git` local peut interagir.
* L'option `origin` dans la commande ci-dessus est le nom par défaut (un nom court) que Git donne au serveur hébergeant votre dépôt distant.  
C'est-à-dire, au lieu de l'URL du serveur, Git utilise le nom court `origin`.
* Il n'est pas obligatoire de conserver le nom par défaut du serveur. Si vous préférez un autre nom plutôt que `origin`, remplacez simplement le nom `origin` dans la commande `git remote add` ci-dessus par le nom que vous préférez.
* N'oubliez pas qu'un nom court de serveur (par exemple, `origin`) n'a rien de spécial ! Il existe uniquement — localement — pour vous aider à référencer facilement l'URL du serveur. Alors n'hésitez pas à le changer en un nom court que vous pouvez facilement référencer.
* Pour renommer une URL distante existante, utilisez la commande `git remote rename` comme suit :

```
git remote rename theCurrentURLName yourNewURLName
```

* Chaque fois que vous clonez (téléchargez) un dépôt distant, Git nomme automatiquement l'URL de ce dépôt `origin`. Cependant, vous pouvez spécifier un nom différent avec la commande `git clone -o yourPreferredName`.
* Pour voir l'URL exacte stockée pour les surnoms comme `origin`, exécutez la commande `git remote -v`.

### Étape 4 : Confirmer la connexion

Une fois que vous avez connecté votre répertoire Git au dépôt distant, vérifiez si la connexion a réussi en exécutant `git remote -v` sur la ligne de commande.

Ensuite, vérifiez la sortie pour confirmer que l'_URL affichée_ est la même que l'_URL distante_ à laquelle vous souhaitez vous connecter.

**Note :**

* Consultez l'article « [Connexion avec SSH](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) » si vous souhaitez vous connecter en utilisant l'URL SSH au lieu de l'URL HTTPS.
* Cependant, si vous n'êtes pas sûr de l'URL distante à utiliser, consultez l'article « [Quelle URL distante dois-je utiliser ?](https://help.github.com/en/github/using-git/which-remote-url-should-i-use) ».
* Souhaitez-vous changer votre URL distante ? [Changer l'URL d'une référence distante](https://help.github.com/en/github/using-git/changing-a-remotes-url) est un excellent guide.

### Étape 5 : Pousser un dépôt Git local vers le dépôt distant

Après avoir connecté avec succès votre répertoire local au dépôt distant, vous pouvez alors commencer à pousser (télécharger) votre projet local en amont.

Chaque fois que vous êtes prêt à partager votre projet ailleurs, sur n'importe quel dépôt distant, demandez simplement à Git de pousser toutes vos validations, branches et fichiers dans votre répertoire `.git` local vers le dépôt distant.

La syntaxe de code utilisée pour télécharger (pousser) un répertoire Git local vers un dépôt distant est `git push -u remoteName branchName`.

C'est-à-dire, pour pousser votre répertoire `.git` local, et en supposant que le nom court de l'URL distante est « origin », exécutez :

```
git push -u origin master
```

**Note :**

* La commande ci-dessus implique que _git_ doit _pousser_ votre branche locale _master_ vers la branche distante _master_ située à l'URL nommée _origin_.
* Techniquement, vous pouvez substituer l'option `origin` par l'URL du dépôt distant. N'oubliez pas, l'option `origin` n'est qu'un surnom de l'URL que vous avez enregistrée dans votre répertoire `.git` local.
* Le drapeau `-u` (référence amont/suivi) lie automatiquement la branche locale du répertoire `.git` avec la branche distante. Cela vous permet d'utiliser `git pull` sans aucun argument.

### Étape 6 : Confirmer le téléchargement

Enfin, retournez à votre page de dépôt GitHub pour confirmer que Git a réussi à pousser votre répertoire Git local vers le dépôt distant.

**Note :**

* Vous devrez peut-être actualiser la page du dépôt distant pour que les changements soient visibles.
* GitHub dispose également d'une installation optionnelle gratuite pour convertir votre dépôt distant en un site web fonctionnel. Voyons « comment » ci-dessous.

## Publiez votre site web avec GitHub Pages

Après avoir poussé votre projet vers votre dépôt distant, vous pouvez facilement le publier sur le web en suivant ces étapes :

### Étape 1 : Nom du fichier HTML

Assurez-vous que le nom du fichier HTML principal de votre projet est `index.html`.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/step1-html-file-name-codesweetly.jpg)

### Étape 2 : Allez dans l'onglet Paramètres

Sur la plateforme web de GitHub, allez dans le dépôt du projet que vous souhaitez publier et cliquez sur l'onglet **paramètres** du dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/step2-settings-tab-codesweetly.jpg)

### Étape 3 : Allez dans l'onglet Pages

Faites défiler vers le bas jusqu'à la section **GitHub Pages**. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/step3-pages-tab-codesweetly.jpg)

### Étape 4 : Changer la Source

Là, changez la branche **Source** de **none** à **master**.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/step4-source-codesweetly.jpg)

### Étape 5 : Voir votre site en direct !

Ensuite, une notification disant : « Votre site est publié à _https://your-username.github.io/your-github-repo-name/_ » s'affichera.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/step5-see-your-site-live-codesweetly.jpg)

Maintenant, vous pouvez consulter — et publiciser — votre projet à l'URL spécifiée.

Cette section n'a fait qu'effleurer la surface de la publication de votre projet avec GitHub. Pour en savoir plus sur GitHub Pages, consultez cette documentation « [Travailler avec GitHub Pages](https://docs.github.com/en/github/working-with-github-pages) ».

### En bref

GitHub est une plateforme en ligne pour héberger (ou partager) des dépôts Git. Il vous aide à créer un moyen de collaborer facilement sur des projets avec n'importe qui, n'importe où, n'importe quand.

## Toujours dans le doute ?

Êtes-vous toujours perplexe quant à la fine ligne entre Git et GitHub ? Ne vous inquiétez pas — je vous couvre. Voici cinq différences clés entre Git et GitHub.

### Différence 1 : Git vs. GitHub — Fonction principale

**Git** est un système de contrôle de version distribué qui enregistre différentes versions d'un fichier (ou d'un ensemble de fichiers). Il permet aux utilisateurs d'accéder, de comparer, de mettre à jour et de distribuer toute version enregistrée à tout moment.

Cependant, **GitHub** est principalement une plateforme d'hébergement pour héberger des dépôts Git en ligne. Il permet aux utilisateurs de garder leur [dépôt distant](https://www.codesweetly.com/git-basic-introduction/#what-is-a-remote-repository) privé ou ouvert pour des entreprises collaboratives.

### Différence 2 : Git vs. GitHub — Plateforme d'exploitation

Les utilisateurs installent et exploitent Git sur leurs machines locales. Cela signifie que la plupart des opérations de Git sont réalisables sans Internet.

GitHub, cependant, est un service basé sur le web qui fonctionne uniquement en ligne. Cela signifie que vous avez besoin d'Internet pour faire quoi que ce soit sur GitHub.

### Différence 3 : Git vs. GitHub — Inventeurs

Linus Torvalds a commencé le développement de Git en avril 2005.

Chris Wanstrath, P. J. Hyett, Tom Preston-Werner et Scott Chacon ont fondé GitHub.com en février 2008.

### Différence 4 : Git vs. GitHub — Mainteneurs

En juillet 2005, Linus Torvalds a confié la maintenance de Git à Junio C. Hamano — qui est le mainteneur en chef depuis lors.

Et Microsoft a acquis GitHub en octobre 2018.

### Différence 5 : Git vs. GitHub — Concurrents

Les alternatives populaires à Git sont Mercurial, Team Foundation Version Control (TFVC), Perforce Helix Core, Apache Subversion et IBM Rational ClearCase.

Les concurrents les plus proches de GitHub sont GitLab, Bitbucket, SourceForge, Cloud Source Repositories et AWS CodeCommit.

## En résumé

Git et GitHub sont deux entités différentes qui vous aident à gérer et héberger des fichiers. En d'autres termes, Git sert à contrôler les versions de fichiers tandis que GitHub est une plateforme pour héberger des dépôts Git.

## Ressource utile

* [Comment utiliser Git – Un guide époustouflant avec des conseils géniaux](https://www.codesweetly.com/how-to-use-git/)