---
title: Les essentiels de Git expliqués en cinq minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-11T17:13:38.000Z'
originalURL: https://freecodecamp.org/news/the-essentials-of-git-explained-in-five-minutes-d554019eded9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lp9bCUSIc1Foh1fa2qaVWw.jpeg
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: remote work
  slug: remote-work
- name: 'tech '
  slug: tech
seo_title: Les essentiels de Git expliqués en cinq minutes
seo_desc: 'By James Okunlade

  As you learn to become a software developer, you’ll realize that most work is done
  in teams. And when you’re on a team, you’ll need a version control system to manage
  changes to your code base that come from different developers.

  Gi...'
---

Par James Okunlade

Alors que vous apprenez à devenir développeur logiciel, vous réaliserez que la plupart du travail se fait en équipe. Et lorsque vous êtes dans une équipe, vous aurez besoin d'un système de contrôle de version pour gérer les changements apportés à votre base de code par différents développeurs.

Git est l'un des systèmes de contrôle de version les plus populaires. Pourtant, les nouveaux développeurs peuvent facilement être submergés en l'utilisant - je sais que c'était mon cas. En fait, je l'ai évité pendant des années.

Si vous êtes un développeur expérimenté ou si vous ne tremblez pas à la mention de Git, n'hésitez pas à passer à l'article suivant. Cependant, si vous êtes nouveau dans Git ou peu sûr de son utilisation, prenez quelques minutes pour apprendre ces conseils de base - mais puissants - sur Git.

Voici ce que nous allons couvrir :

1. Git clone
2. Git checkout
3. Git pull
4. Git add et commit
5. Git stash et merge
6. Git push

![Image](https://cdn-media-1.freecodecamp.org/images/3w5y2tx33BATBrRgxW4zIBYU9syzS0riLfIg)
_Capture d'écran de mon dépôt old-apple sur Github_

### **Git clone**

Clônez toujours les nouveaux dépôts sur lesquels vous travaillez, ce qui signifie télécharger une copie des fichiers du dépôt sur votre ordinateur local. Bien qu'il existe de nombreuses façons de cloner un dépôt, je vais expliquer comment le faire avec la ligne de commande.

Par exemple, si vous souhaitez cloner le dépôt ci-dessus, copiez d'abord le lien de clonage ci-dessus. Ensuite, ouvrez votre terminal et accédez à l'emplacement sur votre ordinateur local où vous souhaitez placer ces fichiers. Tapez git clone puis collez le lien comme indiqué ci-dessous si vous souhaitez cloner la branche master.

`git clone [https://github.com/JamesOkunlade/old-apple.git](https://github.com/JamesOkunlade/old-apple.git)`

Si vous souhaitez cloner une branche particulière de ce dépôt, vous devrez faire quelque chose comme ceci :

`git clone [https://github.com/JamesOkunlade/old-apple.git](https://github.com/JamesOkunlade/old-apple.git) -b nom-de-la-branche`

### **Git checkout**

Il est considéré comme une bonne pratique de créer différentes branches pour différentes fonctionnalités au lieu de travailler directement sur la branche master. Lorsque toutes les fonctionnalités ont été jugées conformes à certains tests et exigences, vous pouvez alors les fusionner dans la branche master.

À différents moments, vous devrez basculer vers la branche particulière du dépôt sur laquelle vous souhaitez travailler, et vous pouvez le faire avec la commande suivante.

Si la branche avait déjà été créée :

`git checkout nom-de-la-branche`

Et si vous créez simplement la nouvelle branche de fonctionnalité :

`git checkout -b nom-de-la-branche`

### **Git pull**

Votre équipe ou votre partenaire de programmation en binôme modifiera différentes branches d'un dépôt, et vous devriez toujours tirer ces nouveaux changements avant de commencer à écrire du code. Dans votre terminal, basculez vers la branche sur laquelle vous allez travailler, et exécutez la commande `git pull`. Les changements récents seront tirés vers votre dépôt local.

### **Git add et commit**

Les commandes Git add et commit sont presque toujours utilisées ensemble. Considérez-les comme capture et sauvegarde. Vous ne pouvez pas sauvegarder quelque chose si vous ne le capturez pas d'abord. Ainsi, la commande add doit toujours précéder la commande commit. Alors que vous utilisez la commande add pour pointer vers le fichier particulier que vous souhaitez capturer dans son état actuel, vous utilisez commit pour sauvegarder une copie de ce que vous avez capturé.

Pour capturer tous les fichiers (sauf ceux exclus par Git ignore), vous utiliserez `git add .` et pour capturer l'état actuel d'un fichier particulier, par exemple index.html, vous devrez taper `git add index.html`

Après avoir pris les instantanés, vous devrez ensuite commiter et sauvegarder vos instantanés dans votre dépôt local en utilisant ce qui suit :

`git commit -m 'message de commit'`

Le message de commit doit expliquer la particularité de l'instantané que vous sauvegardez. Par exemple :

`git add index.html`

`git commit -m 'le bouton de la fonctionnalité de formulaire créé'`

Vous pouvez faire les deux ensemble avec l'opérateur && comme montré ci-dessous ;

`git add index.html && git commit -m 'structure html du pied de page créée'`

### **Git stash et merge**

Faire simplement `git stash` va stasher toute édition que vous avez faite sur la branche mais que vous ne souhaitez pas commiter. Cela signifie que lorsque vous attendez qu'un autre développeur commite et pousse sa copie du code, vous pouvez expérimenter certaines choses dans cette même branche. Git l'encourage. Chaque fois que vous êtes prêt à tirer de nouveaux changements vers votre dépôt local, mais que vous ne souhaitez pas fusionner vos propres éditions, vous devez alors stasher vos propres éditions. Git stash gardera la copie ailleurs pour vous et elle est accessible en faisant Git stash list.

La commande `git merge` fusionne deux instantanés différents ensemble. Cela peut être la fusion de différents instantanés de la même branche par différents développeurs ou la fusion de différents instantanés de différentes branches ensemble.

Lorsque vous avez basculé vers la branche master, git merge development va fusionner la branche development avec votre branche master et vice versa.

### **Git push**

Tout comme sauvegarder vos instantanés dans un album Google Photos pour quiconque avec qui vous partagez l'album, pensez à git push comme l'envoi de votre dépôt local vers le dépôt distant pour que les autres y accèdent.

`git push -u origin nom-de-la-branche`

Bien qu'il existe d'autres commandes Git disponibles pour une utilisation, il est intéressant de voir ce que vous pouvez accomplir en maîtrisant les quelques commandes que j'ai couvertes ci-dessus.

N'hésitez pas à me contacter et à me poser des questions sur Twitter

[**James Okunlade (@JamesOkunlade) | Twitter**](https://twitter.com/JamesOkunlade)  
[_The latest Tweets from James Okunlade (@JamesOkunlade). Full-stack SWE | JavaScript/React/Redux | Ruby/Ruby on Rails |
_twitter.com](https://twitter.com/JamesOkunlade)

```
def JamesOkunlade (beginnerDeveloper)
```

```
  unless you have a coding buddy OR you're making a lot of money
```

```
  doing it
```

```
     puts "Coding is not fun!"
```

```
  end
```

```
end
```

Je viens du Nigeria et je fais de la programmation en binôme tous les jours avec mon partenaire de codage du Bangladesh et d'autres développeurs de Serbie, du Kosovo et d'Ukraine. Ils m'ont tous aidé à utiliser Git.

En tant qu'étudiant, je fais de la programmation en binôme à distance pendant au moins 40 heures chaque semaine. Apprendre la programmation en tant que débutant peut être très fastidieux et réduit ainsi la productivité et rend la courbe d'apprentissage plus difficile. Avec un bon partenaire de codage, cependant, et sous une structure appropriée, vous seriez surpris de voir à quel point l'apprentissage pourrait être intéressant.

[**James Okunlade - Software Developer - Filmdrive | LinkedIn**](https://www.linkedin.com/in/james-okunlade-4a4502121/)  
[_View James Okunlade's profile on LinkedIn, the world's largest professional community. James has 2 jobs listed on their
_www.linkedin.com](https://www.linkedin.com/in/james-okunlade-4a4502121/)