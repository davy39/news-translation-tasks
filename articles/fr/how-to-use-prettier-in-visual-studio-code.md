---
title: Comment utiliser Prettier dans Visual Studio Code
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-03-18T12:35:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-prettier-in-visual-studio-code
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Prettier.png
tags:
- name: Prettier
  slug: prettier
- name: Visual Studio Code
  slug: visual-studio-code
seo_title: Comment utiliser Prettier dans Visual Studio Code
seo_desc: "Nowadays, every tech company strives to build quality software fast. That's\
  \ why every developer must learn how to write clean and readable code. \nBut when\
  \ a project is managed by multiple developers, the focus shifts into consistency\
  \ especially in te..."
---

De nos jours, chaque entreprise technologique s'efforce de développer des logiciels de qualité rapidement. C'est pourquoi chaque développeur doit apprendre à écrire un code propre et lisible. 

Mais lorsqu'un projet est géré par plusieurs développeurs, l'accent est mis sur la cohérence, notamment en termes de code écrit. 

Maintenir un style de code et un formatage cohérents entre plusieurs membres de l'équipe et projets est une tâche difficile. Il est presque impossible de le faire manuellement, mais c'est là que Prettier entre en jeu.

Dans ce guide, vous apprendrez comment installer Prettier dans Visual Studio Code et comment l'utiliser pour formater du code.

## Prérequis 

Avant de suivre ce guide, vous devrez télécharger et installer [Visual Studio Code](https://code.visualstudio.com/).

## Qu'est-ce que Prettier ?

Prettier est un puissant formateur de code qui automatise ce processus de bout en bout. Il vous donne la confiance que votre code respecte les normes de codage définies sans aucune action manuelle (sauf si vous souhaitez le faire manuellement).   
  
Prettier prend non seulement en charge toutes les bibliothèques et frameworks JavaScript, tels qu'Angular, React, Vue et Svelte, mais fonctionne également avec TypeScript.

C'est pourquoi il est utilisé par de nombreuses personnes dans le domaine de la technologie à travers le monde.

## Comment installer Prettier dans Visual Studio Code

Pour installer Prettier dans Visual Studio Code, vous devez :

1. Ouvrir l'onglet Extensions.
2. Taper prettier dans la boîte de recherche.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---1--2-.png)
_Visual Studio Code / Extensions_

En haut de la liste, vous trouverez l'extension Prettier - Code formatter. Vous devez l'ouvrir et cliquer sur le bouton Installer :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---2.png)
_Visual Studio Code / Extensions / Prettier - Code Formatter_

Après l'installation réussie, vous verrez le texte indiquant "This extension is enabled globally" :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---2--1-.png)
_Visual Studio Code / Extensions / Prettier - Code Formatter (Installation terminée)_

## Comment activer Prettier dans Visual Studio Code

Lorsque votre extension Prettier est installée, vous devez configurer Visual Studio Code pour en tirer parti. Vous pouvez le faire dans l'onglet Paramètres. 

Note : pour ouvrir l'onglet Paramètres, vous pouvez utiliser `COMMAND + ,` sur macOS ou `CTRL + ,` sur Windows et Linux :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---4.png)
_Visual Studio Code / Vue principale_

En haut de l'onglet Paramètres, vous trouverez une boîte de recherche. Maintenant, vous devez taper formatter, puis Editor: Default Formatter apparaîtra dans la liste des paramètres :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---5.png)
_Visual Studio Code / Paramètres_

Maintenant, ouvrez le menu déroulant et sélectionnez Prettier - Code formatter dans la liste :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---6.png)
_Visual Studio Code / Paramètres / Formateur par défaut_

Maintenant, Prettier est votre formateur de code par défaut, mais vous pourriez vouloir activer Visual Studio Code pour formater automatiquement le code lorsque vous enregistrez des fichiers. 

Si vous le souhaitez, cochez simplement la case dans la section Format On Save :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---7.png)
_Visual Studio Code / Paramètres / Format On Save_

## Comment formater du code avec Prettier dans Visual Studio Code

Prenons un exemple d'un composant React que j'ai créé : 

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---8--2-.png)
_Visual Studio Code / Composant React 18 non formaté_

Comme vous pouvez le voir, ce code est complètement désaligné, il manque des points-virgules et il est très difficile à lire. Le code pourrait être mieux formaté, n'est-ce pas ? C'est là que Prettier entre en jeu.  

Pour formater le code, nous devons ouvrir la palette de commandes – vous pouvez utiliser `COMMAND + SHIFT + P` sur macOS ou `CTRL + SHIFT + P` sur Windows et Linux. 

Maintenant, vous devez trouver Format Document. N'hésitez pas à utiliser la boîte de recherche :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---9.png)
_Visual Studio Code / Commande Format Document_

Après avoir exécuté Format Document, votre code devient net et propre :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Prettier---10.png)
_Visual Studio Code / Composant React 18 formaté (avec Prettier)_

## Conclusion

Intégrer Prettier dans Visual Studio Code est un changement de jeu pour les développeurs qui s'efforcent de maintenir une base de code cohérente et de haute qualité. 

En automatisant le processus de formatage, vous ne respectez pas seulement les normes de codage, mais vous réduisez également les difficultés liées au formatage manuel du code. C'est pourquoi chaque développeur devrait utiliser Prettier pour garantir la cohérence de sa base de code. 

J'espère que cet article vous a beaucoup aidé. Cela signifierait beaucoup pour moi si vous le partagiez sur vos réseaux sociaux.

Si vous avez des questions, vous pouvez me joindre sur [Twitter](https://twitter.com/msokola).

## Apprendre React

Vous cherchez un cours pratique pour apprendre React ? 

🚀 **Rejoignez mon [Cours React 18 sur Udemy](https://assets.mateu.sh/r/fcc-prettier-guide)**.

Ce cours comprend :

* 🎥 5,5 heures de vidéo à la demande
* 📱 Accès sur mobile et TV
* 📝 Accès à vie complet
* 🎓 Certificat d'achèvement

Cliquez ci-dessous pour vous inscrire.

[![React 18 sur Udemy](https://assets.mateu.sh/assets/fcc-prettier-guide)](https://assets.mateu.sh/r/fcc-prettier-guide)  
_Cliquez pour commencer_