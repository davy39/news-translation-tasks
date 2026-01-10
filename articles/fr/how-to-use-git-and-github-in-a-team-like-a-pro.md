---
title: Comment utiliser Git et GitHub en équipe comme un pro – avec Harry et Hermione
  🧙
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-07T18:13:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-and-github-in-a-team-like-a-pro
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Frame-17
seo_title: Comment utiliser Git et GitHub en équipe comme un pro – avec Harry et Hermione
  🧙
---

freeCodeCamp.png
étiquettes:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: travail d'équipe
  slug: travail-dequipe
- name: contrôle de version
  slug: controle-de-version
seo_title: null
seo_desc: 'Par Damian Demasi

Dans ce tutoriel, vous apprendrez à travailler en équipe avec un dépôt central
sur GitHub. Vous travaillerez sur des problèmes, des commits, des pull requests, des revues de code, et plus encore.

Je ne me considère pas comme un expert en Git, mais j'ai beaucoup appris à ce sujet lors de mon premier mois en tant que développeur logiciel.

J'ai écrit ce tutoriel pour partager comment Git est utilisé dans les environnements professionnels. Gardez à l'esprit qu'il n'y a pas qu'une seule façon d'utiliser Git – donc ceci n'est qu'une approche, et elle peut différer de ce que vous verrez dans votre carrière professionnelle.

Une bonne lecture pour commencer à travailler avec les workflows Git est ce tutoriel sur la [Comparaison des Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows).

## **Le Projet**

Harry et Hermione ont eu la brillante idée de créer une application SaaS permettant aux gens de créer leurs propres potions en ligne et de les partager avec le reste du monde. Ils l'ont nommée **Potionfy**, et ce sera leur première start-up.

![Image](https://media.giphy.com/media/BttC0fsMuGXVS/giphy.gif)

Ils ont décidé d'utiliser GitHub comme dépôt central dans lequel tout leur travail sera stocké. Ils ont choisi React et Ruby on Rails comme pile technologique de l'application.

## **L'Équipe**

Potionfy sera lancé par Harry et Hermione eux-mêmes en utilisant leurs économies. Ils travailleront dans leur garage à la maison et s'attendent à avoir un MVP prêt en 4 semaines.

Voyons comment ils vont travailler ensemble pour construire le produit SaaS et les obstacles qu'ils devront surmonter pour y parvenir.

## **Configuration initiale du projet**

Ce projet utilisera deux membres d'équipe fictifs – Harry et Hermione – avec deux comptes GitHub séparés. Vous voudrez peut-être commencer par créer deux comptes sur GitHub pour cela.

Bonus : afin de simplifier les choses, si vous avez un compte Gmail, vous pouvez utiliser votre adresse Gmail avec un plus et une chaîne après la première partie de celle-ci, et toutes les communications par e-mail seront centralisées dans un seul compte, comme suit :

```
my_email_address+harry@gmail.com
my_email_address+hermione@gmail.com

```

Plus d'informations à ce sujet [ici](https://support.google.com/a/users/answer/9308648?hl=en).

### Étape 1 : Comment créer deux comptes GitHub différents

Pour suivre ce tutoriel, vous aurez besoin de deux comptes GitHub différents. J'ai choisi d'en créer deux, mais vous pouvez simplement utiliser le vôtre et en créer un autre. Voici à quoi ressemble ma configuration :

![Comptes GitHub de Harry et Hermione](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o8n5im9orxfgn5cf19ch.png)

### Étape 2 : Comment configurer votre environnement de développement local

Nous allons utiliser un environnement de développement local et configurer Git dessus. J'ai décidé d'utiliser une machine virtuelle exécutant Linux, mais vous pouvez utiliser votre propre environnement (je veux simplement éviter tout problème de configuration avec Git).

Nous devons nous assurer que Git est installé dans notre système :

```
git --version

```

Cette commande doit retourner la version de Git installée dans votre système. Dans mon cas, mon Ubuntu virtuel ne l'avait pas installé, alors j'ai exécuté :

```
sudo apt install git

```

### Étape 3 : considérations sur le travail d'équipe

Harry sera celui qui travaillera localement dans notre environnement de développement, et Hermione choisira de travailler directement sur GitHub en utilisant un VSCode en ligne (plus d'informations à ce sujet plus tard).

## **Comment commencer à travailler sur le projet**

### Étape 1 : Comment créer le dépôt et construire l'équipe (gratuitement)

Hermione est la chef de l'équipe, car elle est plus expérimentée en codage, alors elle a décidé de créer un nouveau dépôt pour héberger le code du produit SaaS.

Pour créer le dépôt, elle a simplement utilisé l'interface web de GitHub et cliqué sur l'onglet `Dépôts`, puis sur le bouton `Nouveau`. Elle a nommé le dépôt `potionfy` et a ajouté une courte description et un fichier `Readme.md`.

![Dépôt Potionfy](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/92a2v6z1asks9og4pows.png)

Après la création du dépôt, elle a invité Harry à travailler dessus. Pour ce faire, elle a cliqué sur l'onglet `Paramètres` dans le dépôt `potionfy`, puis sur l'option `Gérer l'accès`, et enfin sur le bouton `Ajouter des personnes`.

![Ajouter des personnes au dépôt](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3veijbtrpirpxpx5qivl.png)

En entrant le nom d'utilisateur GitHub de Harry (ou son adresse e-mail) dans la fenêtre pop-up et en cliquant sur le bouton `Ajouter Harry(...) à ce dépôt`, elle a réussi à envoyer l'invitation à Harry.

![Invitation de Harry](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6o5mdaunh0wnbwil28c4.png)

Quelques secondes plus tard, Harry a reçu l'invitation par e-mail :

![E-mail d'invitation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/82utres034fp4hmpvkta.png)

Il l'a acceptée, et en faisant cela, les deux membres de l'équipe étaient prêts à commencer à travailler sur leur projet.

**NOTE :** Dans le cas où le lien d'invitation ne fonctionne pas (comme dans mon cas), Harry doit aller sur le profil GitHub d'Hermione, cliquer sur le dépôt `potionfy`, et accepter l'invitation là-bas :

![Acceptation de l'invitation (partie 1)](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/71u7wj0v3cicwnpinbhw.png)

![Acceptation de l'invitation (partie 2)](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d4d69vm27g19jo6kcvbv.png)

### Étape 2 : Comment créer un fichier

Hermione a commencé le projet en créant le fichier initial que le produit SaaS Potionfy utilisera : `index.html`.

Pour ce faire, elle a créé le fichier en utilisant l'interface web de GitHub en se positionnant dans le dépôt et en cliquant sur les boutons `Ajouter un fichier` > `Créer un nouveau fichier`.

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2gdlz27zm8k8cpziv7be.png)

Ensuite, elle a ajouté le nom du fichier, son contenu et un message de commit significatif. Après avoir cliqué sur le bouton `Valider le nouveau fichier`, le fichier a été créé dans le dépôt.

![Création d'un fichier](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/si7jxizohz7adle8rtr0.png)

### Étape 3 : Comment créer un problème et travailler dessus

Hermione doit passer à la tâche suivante concernant le marketing lié au lancement de Potionfy, alors elle a demandé à Harry d'ajouter un simple message de page d'accueil au fichier `index.html`. Elle a donc procédé à la création d'un **problème** dans le dépôt en cliquant sur l'onglet `Problèmes` et en cliquant sur le bouton `Nouveau problème`.

![Nouveau problème](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rasnvg01wtaxt35p4oa8.png)

![Description du nouveau problème](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mgf8tpr35i1dbzpnno2l.png)

Après la création du problème, Harry a jeté un coup d'œil (également en allant dans l'onglet `problèmes` dans le dépôt Potionfy) et a fait savoir à Hermione qu'il allait travailler dessus en laissant un commentaire et en s'assignant le problème.

![Assignation du problème](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6n6z1xfed0iy71y3nkpa.png)

En travaillant avec cette dynamique, l'équipe saura qui travaille sur quoi.

### Étape 4 : Comment configurer l'environnement de développement local

Pour travailler sur le fichier `index.html` du projet, Harry a choisi de travailler localement, donc il devait cloner le dépôt `potionfy` dans son environnement de développement (la machine virtuelle Linux).

La première chose qu'il devait faire était de configurer les clés SSH pour travailler avec GitHub. Il a suivi le tutoriel de GitHub [Générer une nouvelle clé SSH et l'ajouter à l'agent ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) pour ce faire. Il a ensuite ajouté la clé à son compte GitHub, en suivant le tutoriel [Ajouter une nouvelle clé SSH à votre compte GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

Ensuite, Harry a ouvert le dépôt d'Hermione sur GitHub et a copié le lien pour le cloner :

![Clonage du dépôt](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vj9me394xsugdav4wouh.png)

Maintenant, dans son environnement de développement local, il a créé un nouveau répertoire dans lequel tout son travail serait centralisé :

```
$ mkdir ~/development
$ cd ~/development

```

Enfin, il a cloné le dépôt en tapant `git clone` et en collant le code qu'il venait de copier depuis GitHub (qui est l'_adresse_ du dépôt) :

```
$ git clone git@github.com:Hermione-Colo-Codes/potionfy.git

```

De cette manière, il a maintenant une copie locale du dépôt et il est prêt à commencer à travailler dessus.

```
$ ll
total 12
drwxrwxr-x  3 parallels parallels 4096 Nov 17 07:34 ./
drwxr-xr-x 23 parallels parallels 4096 Nov 17 07:33 ../
drwxrwxr-x  3 parallels parallels 4096 Nov 17 07:34 potionfy/

```

### Workflow GitHub

Pour travailler sur un dépôt, voici le workflow que GitHub recommande :

1. Créer une branche
2. Apporter des modifications
3. Créer une pull request
4. Répondre aux commentaires de révision
5. Fusionner votre pull request
6. Supprimer votre branche

Pour plus d'informations à ce sujet, vous pouvez lire [ce document](https://docs.github.com/en/get-started/quickstart/github-flow).

#### Étape 1 : Créer une branche

Comme il est bon de ne pas travailler directement sur la branche principale, Harry a créé une nouvelle branche liée au problème sur lequel il va travailler.

Il a choisi de le faire sur le dépôt GitHub, mais il aurait pu faire la même chose dans son environnement local en utilisant des commandes Git.

Il a choisi un nom significatif et a préfixé le nom avec le numéro du problème associé (qui est `1`, dans ce cas).

![Création d'une branche](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f6yne1wb24kctulcw654.png)

Plus d'informations sur la création d'une branche sur GitHub peuvent être [trouvées ici](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository).

#### Étape 2 : Travailler sur la branche localement

Après la création de la branche, Harry a commencé à travailler dessus.

##### `git pull`

La première chose qu'il a faite a été un `pull` de l'ensemble du dépôt afin qu'il puisse voir la branche dans son environnement de développement local.

```bash
~/development/potionfy$ git pull
Warning: Permanently added the ECDSA host key for IP address '13.237.44.5' to the list of known hosts.
From github.com:Hermione-Colo-Codes/potionfy
 * [new branch]      1-add-landing-message -> origin/1-add-landing-message
Already up to date.

```

##### `git checkout`

Avec la nouvelle branche dans son environnement, il est passé à celle-ci en utilisant la commande `git checkout <name_of_branch>`. Après l'avoir fait, il s'est assuré de travailler dans la bonne branche avec la commande `git branch`.

```bash
~/development/potionfy$ git checkout 1-add-landing-message 
Branch '1-add-landing-message' set up to track remote branch '1-add-landing-message' from 'origin'.
Switched to a new branch '1-add-landing-message'

~/development/potionfy$ git branch
* 1-add-landing-message
  main

```

##### Résoudre le problème

Harry a commencé à travailler sur la résolution du problème. Pour ce faire, il a ouvert le fichier `index.html` et y a ajouté un en-tête `h1`.

![Apporter des modifications au fichier](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1rhinjvy8z4ouozekolm.png)

Après avoir apporté les modifications, il a vu comment Git a réagi à ce changement.

```bash
~/development/potionfy$ git status
On branch 1-add-landing-message
Your branch is up to date with 'origin/1-add-landing-message'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
parallels@parallels-Parallels-Virtual-Platform:~/development/potionfy$

```

Il a ensuite ajouté le fichier à la zone de staging avec la commande `git add` et a validé le changement avec la commande `git commit`.

```bash
~/development/potionfy$ git add -A

~/development/potionfy$ git commit -m "Add landing message. #1"

~/development/potionfy$ git status

```

Notez comment le message de validation inclut également l'identifiant du problème, qui dans ce cas est `#1`.

##### Pousser vers le dépôt

L'étape suivante que Harry doit faire est de pousser les changements vers le dépôt.

```bash
~/development/potionfy$ git push

```

![Pousser les changements](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/spgnh14xpr1wnqlis2k3.png)

##### Créer une pull request

Harry a ensuite cliqué sur le bouton `Compare & pull request` dans le dépôt GitHub (en s'assurant que sa branche était sélectionnée dans le menu déroulant de gauche des branches).

![Pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9nsmrf4fbqloojq41tk0.png)

Cette pull request sera analysée par Hermione et elle décidera si elle peut être fusionnée avec la branche principale ou non.

### Récapitulatif rapide jusqu'à présent

Jusqu'à ce point dans le tutoriel, nous avons appris comment Harry et Hermione ont décidé de créer une application SaaS pour permettre aux gens de créer leurs propres potions en ligne et de les partager avec le reste du monde. Ils l'ont nommée **Potionfy**. 

Hermione a créé un dépôt distant, puis un `problème` pour traiter la tâche de création d'une page d'accueil, et comment Harry a travaillé sur ce `problème` localement et a créé une `pull request` une fois qu'il a terminé de travailler dessus.

Maintenant, nous allons voir :

* comment Hermione révise le code de Harry,
* comment le code est fusionné dans la branche principale,
* la décision d'utiliser une branche `develop`,
* comment l'équipe travaille dans la branche develop et fusionne les changements dans main,
* et comment l'équipe résout les conflits de fusion.

![Image](https://media.giphy.com/media/VwUquCGtIatGg/giphy.gif)

## **Comment faire des revues de code**

### Étape 1 : Comment créer une revue de code

Hermione a terminé ses tâches de marketing et de promotion, et elle a maintenant le temps de réviser le code de Harry.

Pour ce faire, elle ouvre le dépôt GitHub et clique sur l'onglet `Pull requests` pour trouver la pull request de Harry.

![Première pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qytmh2qm30u2tfxfdc1p.png)

Après avoir cliqué dessus, elle clique ensuite sur l'onglet `Commits`, et enfin sur le dernier commit de Harry (ce n'est qu'une façon d'accéder aux fichiers modifiés dans la pull request).

![Réviser le code](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zr6b36csbr9btula3rh9.png)

Elle n'est pas entièrement convaincue par le code `<h1>`, alors elle clique sur l'icône plus qui apparaît lorsqu'elle survole cette ligne de code, et écrit un commentaire à Harry. Enfin, elle clique sur le bouton `Start a review`.

![Commentaire sur le code](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2ws8b6hfmuo9kqmun15q.png)

Comme elle n'a pas d'autres commentaires sur le code, elle clique maintenant sur le bouton `Review changes` pour rendre la revue visible pour le reste de l'équipe.

![Faire une revue](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hybyz2iwa71gsqbztvum.png)

Vous pouvez trouver plus d'informations sur la réalisation de revues dans cet article [Revoir les changements proposés dans une pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request).

### Étape 2 : Comment répondre à la revue et créer un changement de code

Harry vérifie sa pull request et trouve une nouvelle conversation : la revue d'Hermione.

![Travailler sur la revue](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pklnu1xdc1wmvf2mkl0f.png)

Harry répond au commentaire d'Hermione et clique sur le bouton `Resolve conversation`.

![Résoudre la conversation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ofalfmz3ukitvnng7yha.png)

Maintenant que la conversation est résolue, Hermione peut soumettre la revue en indiquant qu'**il y a des changements demandés** afin que Harry puisse réellement travailler dessus.

![Soumettre la revue](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/reok6k1teor9ho43vltv.png)

**Note :** ceci n'est qu'une version du processus de revue dans GitHub, et il peut différer de la manière dont votre équipe choisit de les gérer.

Harry vérifie à nouveau la pull request et constate qu'elle a `Changes requested`.

![Changements demandés](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6rz496wfrvxdesf0ij75.png)

### Étape 3 : Comment implémenter les changements

Comme Harry aime travailler localement, il continue à travailler sur la branche qu'il avait créée afin d'implémenter les changements de code.

```bash
$ git checkout 1-add-landing-message

```

Une fois qu'il est sûr de travailler sur la bonne branche, il apporte les modifications dans le fichier `index.html`.

![Implémenter les changements](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/no7pmw3pck2cpgi3nl5n.png)

**Note :** pour simplifier, nous ne créons pas de fichier CSS séparé ici.

Une fois que Harry a terminé de modifier le code, il met les changements en staging, les valide (en s'assurant d'inclure l'`id` du problème car il travaille toujours dessus), et les pousse vers GitHub.

```bash
$ git add -A

$ git commit -m "Add colour and remove text. #1"

$ git push

```

### Étape 4 : Comment fusionner la pull request

Maintenant, c'est au tour d'Hermione. Elle va à la pull request et trouve un nouveau commit : celui que Harry a fait et poussé vers GitHub.

![Nouveau commit](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4n6yso4pn6rfkdj0xioj.png)

Elle clique ensuite sur l'onglet `Files changed` et trouve ceux qu'elle a suggérés implémentés dans le fichier `index.html`.

![Changements dans le fichier](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tmudklpfre4op0afjem3.png)

Comme elle est satisfaite des changements, elle procède à leur approbation en cliquant sur le bouton `Review changes` et en sélectionnant l'option `Approve`.

![Approuver les changements](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/c7soa00zfq791oa50b9j.png)

Harry voit que sa pull request a été approuvée par Hermione, et il procède à sa fusion dans la branche principale du projet.

![Fusionner la pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6hdjyzbh1vxpyhf9joy0.png)

Il a décidé de ne pas supprimer la branche, car il souhaite la laisser là pour référence future (bien qu'il serait bon de la supprimer).

Comme Hermione est satisfaite de la manière dont le problème a été résolu, elle procède à sa fermeture en allant dans l'onglet `Problèmes` et en cliquant sur le bouton `Fermer le problème`.

![Fermer le problème](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/reqhbp9nrmvzxj46d9ms.png)

Si vous souhaitez voir une représentation graphique de l'ensemble du processus jusqu'à ce point, vous pouvez cliquer sur l'onglet `Insights` puis sur l'option `Network`. Vous pourrez réellement voir comment le branchement et la fusion ont été effectués.

![Représentation graphique](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u87v2ie8y93dq8ielyuq.png)

## **Comment utiliser une branche `develop` dans Git**

Lorsqu'on travaille sur des projets réels, fusionner des changements dans la branche principale comme vous l'avez vu jusqu'à présent n'est pas recommandé.

Au lieu de travailler directement avec la branche `main` (souvent appelée `production`), vous travaillerez avec une branche `develop`. Vous créerez des branches de problèmes à partir de cette branche `develop` et les fusionnerez à nouveau dans la branche `develop`.

Une fois qu'un groupe de problèmes a été résolu, cette branche `develop` sera fusionnée dans la branche `main` (ou `production`), indiquant généralement un changement de version dans l'application.

![Branche Develop](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/94wbcj99uvf39ax8f3ab.png)

Hermione est consciente de cela, et maintenant que la page d'accueil est en ligne et accessible aux clients, elle a décidé de préserver cet _environnement de production_ et de travailler sur une branche de développement.

Pour ce faire, elle crée une branche `develop` à partir de la branche `main`, afin qu'elle et Harry puissent travailler sur cette branche sans impacter l'environnement de production.

![Création d'une branche develop](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d7okjo7adstn9af3rymu.png)

## **Comment gérer les conflits de fusion dans Git**

Hermione souhaite ajouter une nouvelle fonctionnalité à la page d'accueil : un formulaire pour capturer les e-mails des clients. Pour ce faire, elle crée un nouveau problème.

![Nouveau problème](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4v5lyxbk8a18fjvet99o.png)

Une fois le problème créé, Harry décide de commencer à travailler dessus. Pour ce faire, **il crée une branche à partir de la branche `develop`** (en sélectionnant cette branche sur l'interface GitHub) une nouvelle branche appelée `3-email-form` (en incluant le numéro du problème au début pour clarifier comment cette branche se rapporte aux problèmes).

![Nouvelle branche de problème à partir de develop](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/km1xvg06alcri2d3q2uk.png)

Il tire ensuite cette branche localement et commence à travailler dessus.

```bash
$ git pull

$ git checkout 3-form

```

Harry décide d'inclure un formulaire simple dans le fichier `index.html` :

```html
<form action="mailto:hermione@potionfy.com" method="post" enctype="text/plain">
Name:<br>
    <input type="text" name="name"><br>
    E-mail:<br>
    <input type="text" name="mail"><br>
    <input type="submit" value="Send">
    <input type="reset" value="Reset">
</form>

```

**Note :** Ce code est juste pour exemplifier comment Harry travaille sur un fichier et ce n'est pas comment ce type de formulaire pourrait être réellement construit.

Harry met en staging et valide ses changements localement en utilisant le message `Contact form. #3`.

```bash
$ git add -A

$ git commit -m "Contact form. #3"

$ git push

```

![Image](https://media.giphy.com/media/7Yif3ae99ksCc/giphy.gif)

Avant que Harry ne puisse créer une nouvelle pull request, Hermione décide de construire un espace réservé pour le formulaire dans le fichier `index.html` par elle-même. Pour ce faire, **elle crée une nouvelle branche** à partir de `develop` appelée `3-email-form-placeholder`.

![Branche d'Hermione](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vtqld9mij5mxoj56qx4r.png)

Pour travailler sur le fichier `index.html`, elle utilise l'éditeur de code en ligne GitHub (basiquement, un VSCode pour le web). Pour l'ouvrir, elle appuie simplement sur la touche `.` de son clavier et la page GitHub est transformée en une interface VSCode (comme par magie 😉).

![VSCode en ligne](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/agznz5qsohwq8w7xh4xx.png)

Elle procède ensuite à l'ajout du code suivant au fichier :

```html
<form action="mailto:harry@potionfy.com" method="post" enctype="text/plain">

</form>

```

Après avoir sauvegardé le fichier, elle valide les changements directement là dans sa fenêtre de navigateur en utilisant l'interface graphique de VSCode :

![Valider les changements](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/26bow6vevor0j2bz3g1e.png)

Une fois le commit terminé, elle rouvre GitHub et décide de créer sa propre pull request et de fusionner ses changements dans la branche `develop`.

![Créer une pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4ucvh19hp86eh6vwth49.png)

![Fusionner les changements dans develop](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/s5p2ldzkvch67ziutdw5.png)

![Image](https://media.giphy.com/media/OUwzqE4ZOk5Bm/source.gif)

D'autre part, Harry décide également de créer une `pull request` pour fusionner ses changements dans la branche `develop`.

![Pull request de Harry](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/slmwjb3s1z263tnbhvye.png)

À ce stade, GitHub lui fait savoir que sa pull request ne pourra pas être fusionnée automatiquement dans la branche `develop`.

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xvyambidieetr4u3puhi.png)

Harry suppose que sa branche ne reflète plus l'état de la branche `develop` et que la branche `develop` a changé parce que quelqu'un d'autre a fusionné des changements affectant le fichier `index.html` sur lequel il travaillait. Néanmoins, il procède à la création d'une pull request.

Ce qu'il voit ensuite est la manière dont GitHub lui fait savoir qu'il y a un conflit affectant le fichier qu'il a modifié. Il procède à cliquer sur le bouton `Resolve conflicts`.

![Un conflit](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gtxo3qpizp3gfcfpeo14.png)

Il peut maintenant voir que le fichier `index.html` a effectivement été modifié, et que les changements apportés à ce fichier affectent les lignes qu'il a lui-même modifiées.

![Changements en conflit](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bdg7jgxt3zcrwbn6p66h.png)

Pour plus d'informations sur la résolution des conflits, vous pouvez lire l'article [Résoudre un conflit de fusion sur GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github).

Harry procède à la modification du fichier directement sur le site GitHub pour supprimer les changements en conflit, puis clique sur le bouton `Mark as resolved`.

![Résoudre le conflit](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9ijk9wdc6aenfwbzrt8z.png)

Une fois le conflit marqué comme résolu, il clique sur le bouton `Commit merge`.

![Valider la fusion](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cp87juwh255hou1kipgv.png)

Enfin, sa branche était exempt de conflits et il peut fusionner sa pull request (en supposant qu'Hermione a révisé son code et l'a approuvé, comme elle l'a fait précédemment).

![Fusionner la pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7m3lr63hu68nv0xdk15i.png)

Les conflits surviennent souvent lorsque les membres de l'équipe travaillent sur différentes branches qui affectent un fichier commun. Une excellente façon de prévenir les conflits de fusion est de faire une demande de `pull` sur la branche `develop`, de fusionner cette branche `develop` mise à jour dans la branche sur laquelle vous travaillez, puis de faire un `push` suivi d'une `pull request`.

```bash
$ git branch
x-my-branch # C'est un exemple de nom

$ git checkout develop

$ git pull

$ git checkout x-my-branch

$ git merge develop

# Vous apportez des modifications aux fichiers de la branche x-my-branch

$ git add -A

$ git commit -m "<un message>"

$ git push

```

## **Réflexions finales**

Après avoir travaillé sur leur page d'accueil, Harry et Hermione ont réussi à obtenir de nombreuses adresses e-mail de clients potentiels et ont continué à développer leur MVP. Ils ont réussi à obtenir un financement d'une société de capital-risque locale, et ils sont maintenant en train de recruter d'autres développeurs pour lancer Potionfy au public.

Je suis sûr qu'ils aimeront jeter un coup d'œil à votre CV pour vous considérer pour un poste dans leur entreprise, alors bonne chance !

![Image](https://media.giphy.com/media/gbErpwcLlizvi/giphy.gif)

📝 Si vous avez aimé cet article, vous aimerez peut-être d'autres articles que je publie. La meilleure façon de les connaître serait de [**s'abonner à ma newsletter**](https://mailchi.mp/22b236f812b1/subscribe-to-newsletter).

🐙 Vous pouvez me suivre et me contacter sur mon compte [**Twitter**](https://twitter.com/DamianDemasi).

Santé !

Damian.-