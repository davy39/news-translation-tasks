---
title: Comment configurer un environnement de développement Rasa dans Sagemaker Studiolab
  avec VS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-21T16:06:02.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-rasa-with-studiolab-and-vscode
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/fcc_coverimage.png
tags:
- name: AWS
  slug: aws
- name: Machine Learning
  slug: machine-learning
- name: Visual Studio Code
  slug: vscode
seo_title: Comment configurer un environnement de développement Rasa dans Sagemaker
  Studiolab avec VS Code
seo_desc: "By Sijil Salim\nLast week, I was excited to dive into chatbot development\
  \ with the open-source framework Rasa. With Rasa, you get a ton of flexibility,\
  \ from designing the conversation to developing the NLU logic to deployment. \n\
  But the \"Yay\" soon tran..."
---

Par Sijil Salim

La semaine dernière, j'étais ravi de me lancer dans le développement de chatbots avec le framework open-source [Rasa](https://rasa.com/). Avec Rasa, vous obtenez une grande flexibilité, de la conception de la conversation au développement de la logique NLU jusqu'au déploiement. 

Mais le "_Yay_" s'est rapidement transformé en me cogner la tête contre un mur. Le bot Rasa initial lui-même a commencé à planter sur mon ordinateur portable pas si mauvais avec 4 cœurs et 16 Go de RAM. 

Je devais trouver une autre plateforme où je pourrais faire mon développement, mais je ne voulais pas dépenser d'argent pour m'amuser avec des frameworks open-source. Pour être précis, ce dont j'avais vraiment besoin était une plateforme d'expérimentation en Machine Learning gratuite avec support VS Code.

Je vais vous expliquer comment j'ai résolu ces défis avec des plateformes cloud complètement gratuites.

J'ai trouvé que [AWS Sagemaker Studiolab](https://aws.amazon.com/sagemaker/studio-lab/) était un bon choix pour exécuter mes charges de travail Rasa en machine learning. Il est gratuit, offre 15 Go de stockage persistant, et propose des sessions CPU de 12 heures pour des algorithmes complexes ou des sessions GPU de 4 heures pour des algorithmes de deep learning.  

Sagemaker offre également un serveur Jupyterlab, et non une plateforme IDE de développement. J'avais désespérément besoin de mon interface VS Code préférée, ce qui m'a conduit à découvrir Github Codespaces. 

Codespaces fournit un environnement VS Code basé sur le cloud, mais il ne peut pas exécuter des tâches intensives en calcul comme l'entraînement ML. J'avais donc besoin d'une approche "le meilleur des deux mondes". J'avais besoin de VS Code dans Studiolab. 

Code-server à la rescousse ! Code-server est une bibliothèque Python qui vous aide à configurer un serveur VS Code sur une machine. 

## Outils que nous allons utiliser

* AWS Sagemaker Studiolab
* Conda
* Rasa
* Code-server pour VScode

## Configuration de l'environnement Conda

Voyons comment nous pouvons connecter tout cela ensemble. Nous allons commencer par créer un dossier vide dans Studiolab et exécuter les commandes suivantes à l'intérieur de ce dossier :

```
conda create --name rasa-env python==3.8  
conda activate rasa-env  

python -m pip uninstall pip  
python -m ensurepip  
python -m pip install -U pip  

python -m pip install --upgrade setuptools  
python -m pip install rasa  
```

Ces commandes créeront un nouvel environnement Conda dans Studiolab nommé rasa-env et installeront Rasa dedans. Vous pouvez également exécuter `conda install openssh` si vous souhaitez un accès SSH à Git. 

Pour installer le serveur VS Code dans cet environnement Conda, exécutez la commande `conda install -y -c conda-forge code-server`. Maintenant, vous avez votre propre environnement Conda avec Rasa, code-server et OpenSSH installés. 

Bien sûr, nous allons maintenir le code Rasa dans un dépôt Git. Si quelqu'un souhaite cloner le dépôt, nous ne voulons pas que cette personne doive passer par les mêmes tracas de création de l'environnement, n'est-ce pas ? 

Pour faciliter leur vie, nous allons générer un fichier environment.yml, qui est l'équivalent Conda de requirements.txt, en utilisant la commande `conda env export --file environment.yml`. En utilisant ce fichier, vous pouvez recréer l'environnement en exécutant `conda env create -n rasa-env -f environment.yml`.

## Configuration de VS Code

Maintenant que nous avons terminé la configuration de l'environnement, nous pouvons lancer le serveur VS Code dans un nouvel onglet et commencer notre développement Rasa. 

Pour lancer le serveur VS Code, ouvrez un nouveau terminal dans Studiolab et exécutez `code-server --auth none`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-91.png)

L'image ci-dessus montre les logs générés après l'exécution de la commande code-server. Vous pouvez également démarrer code-server avec authentification, ce qui permettra uniquement aux personnes ayant le mot de passe d'accéder au serveur VS Code.

Copiez l'URL de votre environnement Studiolab, qui ressemblera à quelque chose comme _https://xxxxxxxxxxxxxxxxxx.studio.us-east-2.sagemaker.aws/studiolab/default/jupyter/lab_ et remplacez le _/lab_ à la fin par _/proxy/8080/_ pour créer l'URL du serveur VS Code. 

Entrez cette nouvelle URL dans un onglet séparé pour accéder à VS Code s'exécutant dans Studiolab. Attendez 3 à 5 minutes pour que le serveur se lance. Une fois le serveur démarré, nous verrons que le texte dans le terminal de VS Code est flou. 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-88.png)

Pour corriger cela, désactivez l'accélération GPU pour le terminal VS Code en utilisant le paramètre VS Code `terminal.integrated.gpuAcceleration`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-89.png)

## Développement Rasa

Enfin, activez l'environnement Conda rasa-env en exécutant `conda activate rasa-env` pour activer notre environnement Rasa pour le développement.

Maintenant, mettons les mains dans le cambouis avec Rasa. Pour initialiser un projet Rasa exemple, exécutez `rasa init` dans le dossier. Une fois l'initialisation terminée, nous aurons le code pour un bot basique dans le dossier. 

Ensuite, nous devons générer le modèle NLU pour le bot. `rasa train` générera le modèle et le placera dans le sous-dossier models au format .tar.gz. 

Maintenant, le moment de vérité – exécutez `rasa shell`. Si tout se passe bien, nous devrions avoir notre bot opérationnel dans le serveur VS Code, qui à son tour s'exécute dans le runtime Studiolab.

N'oubliez pas de tout nettoyer après avoir terminé en arrêtant le serveur VS Code dans le runtime Studiolab et enfin en arrêtant le runtime lui-même.

## Conclusion

C'est tout ! Vous avez votre propre environnement de développement de chatbots basé sur le cloud, complètement gratuit, où vous pouvez exécuter des charges de travail intensives en calcul via l'interface VS Code. 

Si vous avez appris quelque chose de nouveau ou si vous avez apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine !

Vous pouvez également me trouver sur Twitter [@Live_ByThe_Code](https://twitter.com/Live_ByThe_Code).

Et vous pouvez lire plus d'articles comme celui-ci [ici](https://livebythecode.ml).