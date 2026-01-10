---
title: Comment automatiser la configuration de votre projet et de votre dépôt Github
  depuis la ligne de commande
subtitle: ''
author: Zubin Pratap
co_authors: []
series: null
date: '2019-08-20T08:59:00.000Z'
originalURL: https://freecodecamp.org/news/automate-project-github-setup-mac
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/octo.png
tags:
- name: automation
  slug: automation
- name: GitHub
  slug: github
- name: Scripting
  slug: scripting
- name: workflow
  slug: workflow
seo_title: Comment automatiser la configuration de votre projet et de votre dépôt
  Github depuis la ligne de commande
seo_desc: 'This post comes out of an irritation I faced personally, when I was first
  learning to code - setting up my local repo and syncing with Github.

  I learned by doing projects (often freeCodeCamp ones!). But I needed to make sure
  I didn''t lose my hard wor...'
---

Cet article est né d'une frustration que j'ai personnellement rencontrée lorsque j'ai commencé à apprendre à coder - la configuration de mon dépôt local et la synchronisation avec Github.

J'ai appris en réalisant des projets (souvent ceux de freeCodeCamp !). Mais je devais m'assurer de ne pas perdre mon travail acharné et que les autres puissent voir les efforts que je déployais, donc chaque projet *devait* être mis sur Github. [Plus j'avais de projets complets sur Github, plus ce serait facile pour les recruteurs](https://www.freecodecamp.org/news/learned-to-code-job-ready-and-heres-why/). Mais les étapes nécessaires pour configurer un projet, initialiser un dépôt et se synchroniser avec Github étaient vraiment ennuyeuses et répétitives, alors j'ai décidé de résoudre le problème.

Mauvaise nouvelle : cet article ne sera pas un grand, élégant, détaillé et techniquement sophistiqué. Il sera très peu sophistiqué.

Bonne nouvelle : vous n'avez pas besoin d'être un dieu (ou une déesse) du scripting shell pour le faire.

Donc, mon flux de travail typique pour la configuration d'un projet ressemble généralement à ceci :

1. Aller dans mon dossier `../projects` et exécuter `mkdir project-of-some-name` pour créer un dossier avec le nom `project-of-some-name`.
    
2. `cd` dans ce dossier de projet et faire `git init` pour initialiser un dépôt git local.
    
3. exécuter `touch README.MD` pour créer le fichier `README`, l'ouvrir et ajouter quelques descriptions de base, y compris des liens vers les ressources / tutoriels que j'implémentais dans ce projet. Enregistrer le fichier.
    
4. exécuter `git add .` puis `git commit -m ' ...un message de commit initial...`
    
5. ouvrir un navigateur, aller sur Github, se connecter, créer un nouveau dépôt (distant), copier l'URL, revenir à mon terminal, m'assurer que je suis dans le bon dossier de projet `project-of-some-name`... puis exécuter les scripts git nécessaires pour configurer le dépôt distant comme le dépôt 'upstream' et connecter mon dépôt local à celui-ci. Ensuite, enfin, je peux exécuter un `git push` et mon commit local sera poussé
    
6. s'allonger et faire une sieste, épuisé par ce processus répétitif.
    

Je l'admets, c'était mon processus, mais j'aimais rester organisé et toujours pouvoir accéder à mes projets pour m'y référer.

Puisque l'automatisation est un excellent moyen de pratiquer vos compétences en codage, j'ai décidé d'écrire un petit script shell qui automatise ces étapes horribles et répétitives. Le script se trouve en bas de cet article, et soyez averti - il n'est pas sophistiqué ou élégant. Mais il fait certainement le travail, et je n'ai pas besoin de me connecter à Github et de m'embêter avec toutes ces étapes !

Avant de copier le script, vous devez savoir comment l'exécuter sur votre Mac. Voici donc les étapes que vous devez suivre pour pouvoir utiliser le script afin d'automatiser votre flux de travail de configuration.

1. Je garde mes scripts dans mon dossier racine/d'accueil, dans un sous-dossier appelé `scripts`. Je vous suggère de faire de même ou similaire. Pour accéder au dossier racine/d'accueil, dans votre terminal, tapez `cd ~` car le tilde (`~`) est le symbole du dossier d'accueil. Dans votre application Finder Mac, il apparaît comme celui avec une icône de maison. Donc tous mes scripts sont stockés dans `~/scripts`
    
2. Cela compte car pour exécuter un script shell depuis n'importe quel répertoire dans le terminal, vous devez taper le chemin complet. Dans mon cas, je dois taper `~/scripts/git-script.sh` pour exécuter le script. Mais nous nous emballons.
    
3. copiez le morceau de code en bas de cet article, puis ouvrez un éditeur de texte, collez-le et enregistrez-le sous `[nomdefichier].sh`. L'extension `.sh` est celle des scripts shell. Enregistrez le fichier dans le répertoire où vous souhaitez le sauvegarder - je recommande à nouveau `~/scripts` comme dossier pour sauvegarder vos scripts.
    
4. Naviguez jusqu'à ce dossier dans votre terminal. Pour être sûr, exécutez `ls` dans le terminal pour vérifier que vous pouvez voir le script. S'il n'y est pas, vous êtes dans le mauvais dossier ou l'étape 3 ne s'est pas terminée avec succès.
    
5. Rendez le script shell exécutable. Pour cela, tapez ce qui suit dans le terminal : `chmod +x <<le-bon-nom-de-fichier.sh>>`. C'est la manière Unix de rendre un script shell "exécutable". Je ne suis pas sûr de bien comprendre ce que cela signifie, autre que le fait que c'est nécessaire pour rendre exécutables les scripts shell que vous écrivez, alors ne me demandez pas et je ne vous mentirai pas.
    
6. naviguez jusqu'à votre dossier de projets et créez un nouveau dossier destiné à contenir votre projet. En effet, vous devez faire ceci : `mkdir` - créer un `project-of-some-name` à l'intérieur du dossier où vous gardez tous vos projets. Votre projet sera finalement placé dans `my-computer/my-projects/project-of-some-name`. `cd` dans ce dossier puis tapez `pwd` pour obtenir le chemin complet. Copiez-le - vous devrez le coller bientôt. Il devrait ressembler à `my-computer/my-projects/project-of-some-name`
    
7. ouvrez à nouveau votre terminal, puis tapez `~/scripts/`&lt;&lt;le-bon-nom-de-fichier.sh&gt;&gt;\`\`. Le script s'exécute ! Vous serez guidé à travers quelques entrées... Les étapes principales sont :
    
    > comment voulez-vous appeler votre dépôt Github (**ne pas utiliser d'espaces-** 'my-awesome-project' est bien. Ne pas utiliser 'my awesome project' comme nom de dépôt.
    
    > Entrez une description qui apparaît dans la description du dépôt Github. Pour cela, il est sûr d'utiliser des espaces.
    

> Entrez le chemin du projet que vous avez obtenu à l'étape 6, celui que vous obtenez après avoir tapé `pwd` dans le terminal et obtenu quelque chose comme `my-computer/my-projects/project-of-some-name`

> entrez votre nom d'utilisateur Github (pas l'adresse email) puis votre mot de passe Github. Soyez prudent lorsque vous tapez car ces valeurs n'apparaissent pas à l'écran.

> ....c'est tout. Le script configurera votre dépôt git localement dans `my-computer/my-projects/project-of-some-name` puis créera un `README.MD` (vide) et le committera localement, puis configurera un dépôt distant dans Github (vous connectera via l'API) etc et poussera tout !

> enfin, vous verrez que le terminal avec lequel vous interagissiez a changé le répertoire actuellement actif pour votre dossier de projet. Il sera maintenant dans `my-computer/my-projects/project-of-some-name` et vous pourrez taper `ls` et voir le fichier `README.MD`. Si vous tapez ensuite `git status`, vous verrez l'état de votre dépôt local (l'état de votre projet local) et si vous tapez `git remote`, il vous montrera l'URL Github de votre projet !

Terminé ! Bon codage !

Et.....enfin......voici le script ! J'ai commenté chaque étape pour que vous puissiez comprendre.

```plaintext
# Rendre exécutable avec chmod +x <<nomdefichier.sh>>

CURRENTDIR=${pwd}

# étape 1 : nom du dépôt distant. Entrez un seul mot ..ou...séparez avec des traits d'union
echo "Quel nom voulez-vous donner à votre dépôt distant ?"
read REPO_NAME

echo "Entrez une description du dépôt : "
read DESCRIPTION


# étape 2 : le chemin du dossier de projet local
echo "quel est le chemin absolu de votre répertoire de projet local ?"
read PROJECT_PATH

echo "Quel est votre nom d'utilisateur github ?"
read USERNAME

# étape 3 : aller au chemin 
cd "$PROJECT_PATH"


# étape 4 : initialiser le dépôt localement, créer un README vide, ajouter et committer
git init
touch README.MD
git add README.MD
git commit -m 'commit initial - configuration avec le script .sh'


# étape 5 utiliser l'API github pour connecter l'utilisateur
curl -u ${USERNAME} https://api.github.com/user/repos -d "{\"name\": \"${REPO_NAME}\", \"description\": \"${DESCRIPTION}\"}"

# étape 6 ajouter le dépôt github distant au dépôt local et pousser
git remote add origin https://github.com/${USERNAME}/${REPO_NAME}.git
git push --set-upstream origin master

# étape 7 changer pour le répertoire racine de votre projet.
cd "$PROJECT_PATH"

echo "Terminé. Allez sur https://github.com/$USERNAME/$REPO_NAME pour voir." 
echo " *** Vous êtes maintenant dans la racine de votre projet. ***"
```

#### Merci d'avoir lu !

Si vous souhaitez en savoir plus sur mon parcours dans le code, consultez [l'épisode 53](http://podcast.freecodecamp.org/53-zubin-pratap-from-lawyer-to-developer) du [podcast freeCodeCamp](http://podcast.freecodecamp.org/), où Quincy (fondateur de freeCodeCamp) et moi partageons nos expériences en tant que reconvertis professionnels, ce qui pourrait vous aider dans votre parcours. Vous pouvez également accéder au podcast sur [iTunes](https://itunes.apple.com/au/podcast/ep-53-zubin-pratap-from-lawyer-to-developer/id1313660749?i=1000431046274&mt=2), [Stitcher](https://www.stitcher.com/podcast/freecodecamp-podcast/e/59201373?autoplay=true), et [Spotify](https://open.spotify.com/episode/4lG0RGpzriG5vXRMgza05C).

Je participerai également à quelques AMAs et webinaires dans les mois à venir. Si cela vous intéresse, faites-le moi savoir en allant [ici](http://www.matchfitmastery.com/). Et bien sûr, vous pouvez également me tweeter à [@ZubinPratap](https://twitter.com/zubinpratap).