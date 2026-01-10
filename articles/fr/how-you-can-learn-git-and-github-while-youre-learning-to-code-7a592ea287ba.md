---
title: Comment apprendre Git et GitHub tout en apprenant à coder
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-31T18:53:36.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zGKyRHC3yvnYyCDzHgtL9A.jpeg
tags:
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment apprendre Git et GitHub tout en apprenant à coder
seo_desc: 'By Iago Rodrigues

  In this article, I’ll give you some hints about how to become a Git/GitHub ninja.
  Also, as a bonus, I’ll show you how to use the Terminal (shell) while coding. So
  if you are a beginner, this post should help you understand this tech...'
---

Par Iago Rodrigues

Dans cet article, je vais vous donner quelques conseils sur la façon de devenir un ninja de Git/GitHub. De plus, en bonus, je vais vous montrer comment utiliser le **Terminal** (shell) tout en codant. Donc, si vous êtes débutant, cet article devrait vous aider à comprendre cette technologie. Et si vous êtes déjà un ninja, parcourez-le pour vous rappeler des choses que vous auriez pu oublier.

### Une brève introduction

Git et GitHub sont des outils extrêmement importants dans notre routine en tant que développeurs logiciels. Mais comment pouvons-nous les apprendre alors que nous avons tant à faire lorsque nous apprenons à coder ?

Je suis Iago Rodrigues, un Brésilien. Je suis étudiant en systèmes d'information, stagiaire en développement logiciel et freelance. Je suis au début de ma carrière et je voulais partager avec vous quelques connaissances que j'ai acquises. Alors, prenez votre café et commençons à coder !

Si vous êtes un lecteur portugais, veuillez vous rendre [ici](https://medium.com/trainingcenter/plano-para-estudar-git-e-github-enquanto-aprende-programa%C3%A7%C3%A3o-f5d5f986f459).

Vous pouvez utiliser ce plan pour étudier n'importe quel langage de programmation comme JavaScript, Python, Node, ainsi que HTML et CSS. Peu importe la technologie que vous apprenez, versionner votre travail avec Git est la méthode par défaut pour programmer.

### Préparation de l'environnement

Avant de commencer, nous devons configurer l'environnement pour sauvegarder notre code et les exemples de ce que nous apprenons.

Pour cela, nous devons remplir certaines conditions :

* installer Git sur notre machine
* créer un compte GitHub
* créer un espace de travail sur notre machine

Si vous avez déjà fait cela, vous pouvez passer directement à la section **Workflow de GitHub et le Terminal**. 

#### Installation de Git sur votre machine

L'installation de Git est différente selon chaque système d'exploitation. Consultez le [site officiel de Git](https://git-scm.com/downloads) pour voir quelle méthode vous convient.

Mais si vous utilisez Windows (et parlez portugais), je recommande [cet article](https://woliveiras.com.br/posts/instalando-o-git-windows/).

Une fois Git installé, nous devons créer un compte GitHub et le configurer sur notre machine.

#### Création d'un compte sur GitHub

Pour créer un compte, rendez-vous sur le [site web de GitHub](https://github.com/) et remplissez le formulaire principal.

![Image](https://cdn-media-1.freecodecamp.org/images/5cNW40jBqX4VdNrWJoCP8HAXPagXVfLvPus8)
_Ce formulaire est la première chose qui apparaît si vous entrez sur le site sans être connecté_

Je vous recommande de choisir un nom d'utilisateur réel et agréable ici afin de pouvoir utiliser le compte sur vos CV ou votre compte [LinkedIn](https://www.linkedin.com/in/iago-rodrigues/).

Vous devez informer GitHub du plan que vous souhaitez utiliser. Choisissez l'option **gratuite**. La seule différence est que vous pouvez configurer des dépôts privés avec le plan payant.

![Image](https://cdn-media-1.freecodecamp.org/images/dayAModQsbAZ5Evh5-DuMKdNx9sQwJpoHBmA)
_Choisir le plan de votre compte GitHub._

GitHub vous demandera quelques informations avant de terminer la configuration de votre compte. Vous pouvez répondre maintenant ou simplement passer à l'écran suivant.

Avec tout complété, nous pouvons commencer notre projet.

![Image](https://cdn-media-1.freecodecamp.org/images/p5NkEAEk33Tp8PgRbJRc8e63VNKA8D0IovjJ)
_Écran de confirmation._

Avant de créer notre dépôt, configurons notre email GitHub et notre nom d'utilisateur sur notre machine.

#### Configuration de notre système avec nos données GitHub

Ouvrez votre Terminal. Sous Windows, vous devez ouvrir le **menu démarrer** et taper **cmd**. Ensuite, cliquez sur Entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/nCvpCO1j10nA46u-DvtqvP6tSLKqTSPRMKP4)
_Accéder au CMD via le menu démarrer sur Windows_

Ou vous pouvez installer [cmder](http://cmder.net/) (qui est une bonne option) pour l'utiliser à la place de **cmd**, qui est le Terminal Windows par défaut.

Avec cela, nous devons exécuter la commande shell suivante dans cmder :

```
git config --global user.name "notre_nom_dutilisateur_GitHub"
```

Maintenant, entrez votre adresse email GitHub :

```
git config --global user.email "notre_email_GitHub"
```

#### Configuration de votre clé d'accès GitHub

Chaque fois que vous accédez à un dépôt via le shell, vous devez avoir une permission d'accès. Cela est accordé lorsque vous vous connectez à votre compte GitHub. Mais chaque fois que vous envoyez quelque chose à votre dépôt (repo), vous devez passer vos identifiants.

Pour éviter cela, utilisez une clé SSH. Il s'agit d'une clé d'accès que GitHub échange avec celle configurée sur notre machine.

Pour créer cette clé, suivez le processus décrit dans la [documentation de GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

Avec tout configuré, vous êtes prêt à partir !

![Image](https://cdn-media-1.freecodecamp.org/images/D9WuDGk4mfRzuxpwkWdP1OdKxphqAZwRa2-2)

### Workflow de GitHub et le Terminal

Établissons une **règle** ici :

Chaque fois que vous créez un projet pour étudier quelque chose, comme créer une page HTML ou un jeu en ligne de commande avec Node.js ou autre chose, vous créerez un dépôt, le clonerez sur votre machine, travaillerez dessus en utilisant des branches, et ferez de petits commits pour les envoyer sur GitHub.

D'accord ?!

Cela garantira que vous acquerrez une expérience dont vous aurez besoin pour maîtriser ces outils.

Alors, commençons.

#### **Créer un nouveau projet**

Retournez à votre page GitHub et cliquez sur l'icône plus (+) en haut de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/aRgF6kizz2QH8XyBmXpMpJxf73SgS5Ryn6kH)
_Création d'un nouveau dépôt._

Cliquez sur **New repository**.

Disons que vous créez un projet pour étudier HTML, alors nommez votre dépôt **learning-html**. Cela pourrait être le nom d'une page qui est en cours de création ou tout autre projet, comme : **curriculum-in-html**, **little-snake**, **tic-tac-toe**, ou autre chose, d'accord ?

La description du projet est facultative. Mais je pense qu'il est important d'entrer un texte utile là, car il identifiera la portée de votre projet. Si d'autres personnes veulent vous aider, elles peuvent comprendre votre projet brièvement grâce à la description. Dans votre cas, vous pouvez entrer quelque chose comme **Dépôt d'étude du langage HTML**.

![Image](https://cdn-media-1.freecodecamp.org/images/ZHd1WW2mltowVKBEVXCAxfbLgjXVlzmeaCi3)
_Création d'un dépôt._

Vous devriez également créer un fichier README et définir le type de licence que vous utiliserez dans le projet. Jetez un œil à ces bons [exemples](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) de README, ainsi qu'à la [licence](https://choosealicense.com/) à utiliser sur le projet.

Le fichier README est une description plus complète de votre projet, il est donc bon d'y mettre quelques informations utiles. Suivez les exemples dans le lien.

Bien que la licence soit facultative, il est bon de la définir. La licence indiquera ce que d'autres personnes peuvent faire avec votre code. La licence MIT est l'une des plus populaires et permet à vous (et aux autres) de faire beaucoup de choses avec le projet. Prenez le temps de rechercher d'autres types de licences si vous le souhaitez.

#### **Créer votre espace de travail**

Une fois que vous avez créé le dépôt, vous pouvez le cloner sur votre machine. Mais avant cela, vous devez créer un dossier où vous clonerez tous les futurs dépôts sur lesquels vous travaillerez.

Utilisez le terminal pour créer un dossier qui sera votre **workspace**. Vous faites cela pour maintenir un système organisé, sinon vous finirez par disperser vos projets (et vous pourriez les perdre comme vous avez perdu ces GIFs de chatons que vous avez sauvegardés sur votre ordinateur...).

En supposant que vous avez déjà installé cmder, nous pouvons maintenant l'ouvrir (si vous ne l'avez pas fait, [c'est le moment](http://cmder.net/)) et nous serons à `C:/Users/nom_de_votre_ordinateur`.

Si vous n'êtes pas sur ce chemin, utilisez la commande :

```
cd %home%
```

Exécutez la commande `mkdir nom_du_dossier` pour créer l'espace de travail. Par exemple :

```
mkdir workspace
```

C'est tout ! Maintenant, vous avez le dossier par défaut pour vos projets, et vous pouvez cloner vos dépôts dedans.

#### **Cloner vos dépôts**

Cloner un dépôt signifie que vous allez copier tous les fichiers et répertoires du serveur GitHub sur votre machine afin de pouvoir travailler avec eux.

Maintenant, vous devez cloner le projet que vous avez créé sur GitHub dans votre **workspace**. Pour cela, allez dans le dossier que vous venez de créer. Dans cmder, tapez :

```
cd workspace\
```

**Astuce** : si vous avez créé le dossier ou souhaitez accéder à un dossier existant, vous pouvez commencer à taper son nom et appuyer sur TAB, et cmder complétera automatiquement le nom pour vous.

Avec cela, allez sur la page de votre projet sur GitHub et obtenez le lien dont vous avez besoin pour cloner le dépôt.

Le lien se trouve dans ce bouton vert nommé **Clone or Download** :

![Image](https://cdn-media-1.freecodecamp.org/images/fvqwCR6gUSaY2P6mo1FAATPOjnt68Ug-aple)
_Obtenir le lien pour cloner notre dépôt._

Changez de HTTPS à SSH, car vous avez déjà configuré votre clé d'accès dans votre compte.

![Image](https://cdn-media-1.freecodecamp.org/images/rizYyKsRhGxI7Jo5V85wbufiqLJpqDFa5pjP)
_Changer le lien https en ssh._

Maintenant, vous pouvez exécuter la commande `git clone` et passer le lien que vous avez obtenu. Comme ceci :

```
git clone git@github.com:notre-utilisateur/learning-html.git
```

Et votre dépôt sera cloné, comme dans l'image suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/y3Ek5z6w63gFwCq-gUjcxhexVyZYtp5HKKnu)
_Message de confirmation de clonage._

Vous pouvez accéder au dossier du dépôt qui a été créé dans votre espace de travail lorsque vous l'avez cloné.

Tapez la commande : `cd learning-html/`

**Attention** : Je suppose que vous êtes dans le répertoire `workspace` maintenant. Si ce n'est pas le cas, la commande ci-dessus ne fonctionnera pas. Utilisez `cd %home%\workspace\` puis la commande ci-dessus.

#### **Créer une branche**

Chaque fois que vous modifiez quelque chose dans un projet versionné avec Git, vous devez créer une **branche** avec le nom de la tâche sur laquelle vous travaillez. Cela vous évite de mélanger le code "principal" situé sur la branche **master**. Pour cela, vous pouvez utiliser la commande suivante :

```
git checkout -b nom_de_la_tache
```

Une **branche** est comme une branche d'arbre. Elle fait partie du tronc de l'arbre. Vous pouvez donc apporter des modifications en parallèle avec la partie principale du projet sans l'affecter.

Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/h4qa8Fx5PUOOjlvN5AAyy2xqMHcHkSWSG9Hi)
_Changement de branche._

Une fois que vous avez fait cela, vous pouvez basculer automatiquement vers la nouvelle branche créée et coder comme un fou maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/owmN8324SP6p7hQt1wayIX1oYkVWy22hF-Ch)
_Un chat qui code._

#### **Valider les modifications**

Une fois que vous avez terminé une modification de votre projet, vous devez **valider** la modification dans votre dépôt distant (celui sur les serveurs de GitHub).

**Valider** quelque chose, c'est dire à Git que vous mettez vos modifications dans la file d'attente pour être poussées (envoyées) vers votre dépôt distant.

Imaginez que vous venez de créer une page HTML et que vous y avez ajouté des titres et du texte. Vous avez la première version de ce document maintenant, alors vous devriez la valider.

Pour cela, exécutez quelques commandes afin que Git comprenne que nous voulons envoyer nos modifications au dépôt distant. Exécutez `git add nom_du_fichier` pour dire à Git de préparer le fichier.

Alternativement, vous pouvez exécuter `git add --all` pour envoyer tous les fichiers que vous avez modifiés. Avec la commande `git status`, vous pouvez voir quels fichiers modifiés vous allez valider sur le serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/PFTyey85HGhG36f1xJsc-VvOI-Xt17GvDS53)
_Exemple de la première version d'un fichier._

Dans l'exemple ci-dessus, le fichier **index.html** a été créé et la commande **git status** a été exécutée pour voir ce qui a été modifié. Ensuite, le fichier a été ajouté avec **git add** et **git status** a été exécuté à nouveau pour voir quel fichier a été ajouté à l'espace de travail Git.

Avec cela, vous pouvez maintenant **valider** les modifications. Il suffit d'exécuter la commande **git commit**, comme `git commit -m "message_de_validation"`. N'oubliez pas d'inclure un message descriptif de ce qui a été ajouté à la validation.

#### **Fusionner les modifications**

Après avoir validé les modifications, vous avez maintenant une branche avec des modifications en avance sur celles de la branche **master**. Cela signifie que vous avez une version différente du projet, et vous devez fusionner ces modifications avec la version principale du projet. Avant de faire cela, vérifiez quelles sont les différences entre les branches. Sur votre branche, exécutez la commande :

```
git diff master
```

La sortie sera quelque chose comme :

![Image](https://cdn-media-1.freecodecamp.org/images/9dKretvO8Ne5fHSUs2lofy0SqXXvZyynxCvV)
_Sortie de git diff._

Git vous montre le dernier commit effectué, quels fichiers ont été ajoutés ou modifiés, et ce qui a été modifié également.

Puisque vous savez que vous avez des différences entre votre branche et la master, vous devez les **fusionner** pour **joindre** les nouveaux commits, que vous avez faits dans votre branche, avec le code dans la master. Pour cela, vous devez aller dans la branche master, dans cmder, et exécuter la commande `git merge`.

Pour revenir à la master, exécutez `git checkout master`. Pour fusionner les commits, exécutez `git merge nom_de_notre_branche`.

![Image](https://cdn-media-1.freecodecamp.org/images/TOoDL2f60zFngTvP-TUexS3p2pknLqNWR3xV)
_Exemple de fusion._

Git vous montrera une sortie confirmant ce qui a été ajouté.

#### **Envoyer sur GitHub**

Après avoir fait et fusionné toutes les modifications, vous pouvez maintenant les envoyer à votre dépôt distant sur GitHub.

Vous utiliserez `git push origin master` pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/2XbKSpQhgJi8d0teKw11WeBt2J7Q0814etT4)
_Envoyer nos modifications au dépôt distant._

Vous pouvez également utiliser simplement `git push`. Cela aura le même résultat. Mais lorsque vous envoyez des modifications pour la première fois dans votre espace de travail, vous devez faire `git push origin master` afin que Git sache que votre espace de travail est l'origine de l'envoi.

Maintenant, votre commit apparaîtra sur la page de votre dépôt GitHub :

![Image](https://cdn-media-1.freecodecamp.org/images/B3ytaUMnmfBhj4fGouLbEiixHnVgDZqbxN0E)
_Le dernier commit que nous venons de faire est affiché sur la page du projet sur GitHub._

### Conclusion

Dans ce tutoriel, vous avez appris à créer un projet sur GitHub afin de suivre vos progrès chaque fois que vous étudiez quelque chose de nouveau. Cela vous aidera à connaître la ligne de commande (Terminal), les commandes Git et GitHub. En outre, cela vous aidera à créer un beau portfolio que vous pourrez montrer lors d'entretiens d'embauche.

Pratiquer de cette manière vous aidera également à mieux comprendre comment utiliser **Git avec des dépôts distants** (les dépôts hébergés sur une plateforme comme **GitHub**). Vous améliorerez également vos connaissances et compétences sur le Terminal.

N'oubliez pas les règles de base que vous avez établies :

* toujours créer un nouveau projet d'étude
* travailler sur des branches
* valider les modifications jusqu'à ce qu'il soit temps de les envoyer sur GitHub

D'accord ? :)

Revenez ici et suivez ce guide étape par étape chaque fois que vous oubliez quelque chose !

Je m'appelle Iago Rodrigues. Je suis stagiaire au Brésil, dans la ville de Belém.

Vous pouvez me suivre sur les réseaux sociaux. Toujours un plaisir d'aider avec ce que je peux.

[**Iago Rodrigues (@iagokv) | Twitter**](https://twitter.com/iagokv)  
[_The latest Tweets from Iago Rodrigues (@iagokv). Front-End Developer | Vue.js padawan | Noob on life. Belém, Brasil_twitter.com](https://twitter.com/iagokv)

Oui ! Je sais. Ma photo Twitter est quelque chose...