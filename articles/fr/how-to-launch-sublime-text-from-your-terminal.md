---
title: Comment lancer Sublime Text sur Windows depuis Git Bash
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2020-09-08T21:29:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-launch-sublime-text-from-your-terminal
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98cd740569d1a4ca1c23.jpg
tags:
- name: Bash
  slug: bash
- name: Git
  slug: git
- name: terminal
  slug: terminal
seo_title: Comment lancer Sublime Text sur Windows depuis Git Bash
seo_desc: "If you have been trying to figure out how to open the Sublime Text editor\
  \ from your Git bash, then you're in luck. This article will guide you through the\
  \ process with little or no stress. \nIt took me a while to figure out how it's\
  \ done, but now I ca..."
---

Si vous avez essayé de comprendre comment ouvrir l'éditeur Sublime Text depuis votre Git bash, alors vous avez de la chance. Cet article vous guidera à travers le processus avec peu ou pas de stress. 

Il m'a fallu un certain temps pour comprendre comment cela se fait, mais maintenant je peux partager cette connaissance avec vous tous dans cet article. À la fin, vous serez en mesure de lancer Sublime Text depuis bash.

### Prérequis :

* Assurez-vous d'avoir installé l'[éditeur Sublime text](https://www.sublimetext.com/3)
* Assurez-vous d'avoir installé [Git](https://git-scm.com/downloads)

## Getting started

[Sublime text](https://en.wikipedia.org/wiki/Sublime_Text#:~:text=Sublime%20Text%20is%20a%20shareware,maintained%20under%20free%2Dsoftware%20licenses.) est un éditeur de code source qui aide les développeurs de logiciels à coder et à éditer du texte ou du balisage. 

Il possède des fonctionnalités incroyables telles que la coloration syntaxique, l'indentation, les plugins et les packages. Toutes ces fonctionnalités aident à rendre plus facile et plus confortable le travail avec et la contribution à une grande variété de bases de code de langages de programmation.

Une fois que vous avez téléchargé et installé Sublime, il sera situé dans les fichiers de programme comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/sublime-text.PNG)

Ce que nous voulons faire, c'est créer un alias pour le fichier sublime_text.exe trouvé dans le dossier Sublime Text 3. Ensuite, lorsque nous tapons l'alias dans Git bash, il lance automatiquement l'éditeur de texte.

## Comment configurer Git Bash avec un alias Sublime

Pour commencer à configurer Git bash, nous devons d'abord ouvrir le terminal bash. Ensuite, nous pouvons procéder à l'exploration de diverses commandes Linux afin de compléter le processus de configuration.

Tout d'abord, nous devons créer un fichier .bashrc en utilisant la **[commande touch](https://www.geeksforgeeks.org/touch-command-in-linux-with-examples/)**. Il est important que le fichier soit créé dans le répertoire **C:\Users\username\**  sinon vous obtiendrez une erreur de permission refusée. 

J'ai créé le fichier bash dans le répertoire spécifié, donc le mien ressemble à **C:\Users\larry\.bashrc**.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/touch-1.PNG)

Ensuite, nous devons éditer le **.bashrc file** pour inclure l'alias dont nous aurons besoin pour lancer Sublime text :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vim.PNG)

Lorsque nous cliquons sur entrer, nous verrons une interface qui ressemble quelque peu à ce que nous avons ci-dessous. Ensuite, vous devez appuyer sur `i` pour entrer en mode insertion.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/insert.PNG)

Maintenant, vous avez accès et pouvez taper dans l'invite. Nous pouvons donc ajouter notre alias maintenant, comme ceci :

```
alias subl='C:/Program\ Files/Sublime\ Text\ 3/sublime_text.exe'
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/alias.PNG)

Une fois que nous avons inclus cela, nous pouvons appuyer sur `esc` pour quitter le mode insertion et ensuite `:wq` pour sauvegarder et quitter. 

Une fois que nous avons terminé cela, nous pouvons retourner à notre bash pour vérifier si notre configuration a fonctionné en faisant `subl` comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/sublz.PNG)

Oui, cela fonctionne ! Et vous pouvez voir Sublime Text se lancer lui-même. 

J'ai également découvert que si vous avez un répertoire de travail, vous pouvez forcer Sublime à ouvrir ce répertoire. Je vais naviguer dans une base de code maintenant et montrer la différence dans la prochaine capture d'écran :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vue--app.PNG)

D'après la capture d'écran ci-dessus, Sublime ne lance pas seulement un espace de travail vide  il se lance avec tous les dossiers de projet associés à ce projet. C'est parce que nous avons ajouté un caractère générique à la commande. 

J'espère qu'avec ce hack vous serez en mesure de configurer un alias pour Sublime Text. J'apprécie vraiment les réponses sur ce fil de stack overflow **[thread](https://stackoverflow.com/a/43431197/9352741)**. Cela m'a aidé à former les connaissances que j'ai pu partager dans cet article.