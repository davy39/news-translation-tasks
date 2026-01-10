---
title: Comment installer MySQL et MySQL Workbench sur Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-06-30T18:23:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-mysql-workbench-on-windows
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/boitumelo-phetla-0DJHJcpwN9Q-unsplash.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: Windows
  slug: windows
seo_title: Comment installer MySQL et MySQL Workbench sur Windows
seo_desc: 'If you want to learn MySQL, starting with a good client is super helpful
  – especially when you are just beginning your journey.

  There are a lot of clients out there for your MySQL-based needs, like XAMPP, DataGrip,
  and others. Among all of them, I pr...'
---

Si vous souhaitez apprendre MySQL, commencer avec un bon client est super utile, surtout lorsque vous débutez.

Il existe de nombreux clients pour vos besoins basés sur MySQL, comme XAMPP, DataGrip, et autres. Parmi tous ceux-ci, je préfère [MySQL Workbench](https://www.mysql.com/products/workbench/). Il est complètement gratuit, d'ailleurs.

Dans ce tutoriel, je vais vous montrer comment installer et configurer votre machine Windows pour MySQL et MySQL Workbench à partir de zéro.

Si vous aimez aussi apprendre à partir de vidéos, alors ne vous inquiétez pas car j'ai également créé une vidéo étape par étape spécialement pour vous :

%[https://www.youtube.com/watch?v=kZf_h-Phfds]

## Comment installer MySQL Workbench

#### 539539 Télécharger MySQL Workbench

Assurez-vous de visiter uniquement le [site officiel](https://www.mysql.com/products/workbench/) pour télécharger MySQL Workbench. Vous ne voulez pas vous retrouver sur des sites douteux et télécharger le mauvais fichier qui infecte votre machine préférée, n'est-ce pas ?

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-32.png)
_Trouvez le site officiel pour MySQL Workbench : https://www.mysql.com/products/workbench/_

Maintenant, cliquez sur l'onglet "DOWNLOADS".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-32_1.png)

Faites défiler vers le bas jusqu'à trouver `MySQL Community (GPL) Downloads 539539`.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-32_2.png)

Cliquez sur `MySQL Community (GPL) Downloads 539539`. Après cela, sur la nouvelle page, cliquez sur "MySQL installer for Windows".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-32_3.png)

Dans le menu déroulant, sélectionnez votre système d'exploitation comme "Microsoft Windows". Ensuite, téléchargez le fichier qui est le plus grand en taille.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-33.png)

Un fichier `.msi` sera téléchargé. C'est notre fichier d'installation pour installer MySQL et MySQL Workbench.

#### 539539 Installer MySQL et MySQL Workbench

Double-cliquez simplement sur le fichier d'installation. Il rechargera les composants nécessaires et ouvrira la fenêtre de sélection de l'interface graphique de l'installateur. Choisissez le type d'installation comme personnalisé et cliquez sur "Suivant".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-34_1.png)
_Sélectionnez Personnalisé_

Une nouvelle page apparaîtra. Assurez-vous de sélectionner le dernier "MySQL Server", "MySQL Workbench" et "MySQL Shell". La sélection et le clic sur la flèche de droite feront passer le nom du produit dans la section "Produits à installer". Ensuite, cliquez sur "Suivant".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-34-1.png)
_Installer les composants nécessaires_

Cliquez sur "Exécuter" pour installer les trois composants nécessaires. Le processus peut prendre un certain temps en fonction de votre vitesse Internet et de la configuration de votre ordinateur. Une fois terminé, cliquez simplement sur "Suivant".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-35.png)
_Exécuter_

Dans la fenêtre de configuration du produit, cliquez simplement sur "Suivant". Cela installera les trois composants sélectionnés pour nous.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-37.png)
_Suivant_

Gardez tout tel quel et cliquez simplement sur "Suivant". Cela configurera le serveur MySQL.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-37_1.png)
_Suivant_

Gardez tout tel quel et cliquez simplement sur "Suivant". Cela appliquera la connectivité TCP/IP pour notre serveur MySQL.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-37_2.png)
_Suivant_

Maintenant, donnez-lui un mot de passe Root. À des fins de test, j'utilise un "1111" très simple comme mot de passe, mais je vous recommande de ne pas faire de même. Assurez-vous également de vous souvenir du mot de passe, car vous en aurez besoin lorsque vous voudrez travailler dans MySQL Workbench. Cliquez sur "Suivant".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-37_3.png)
_Suivant_

Gardez tout tel quel et cliquez simplement sur "Suivant". Cela s'assurera de configurer notre mot de passe root pour MySQL Workbench.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38.png)
_Mot de passe root_

Nous voulons exécuter le service en tant que compte système standard pour notre système d'exploitation. Par conséquent, gardez tout tel quel et cliquez simplement sur "Suivant".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38_1.png)
_Suivant_

Sélectionnez l'option pour accorder un accès complet à l'utilisateur exécutant le service Windows, puis cliquez sur "Suivant".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38_2.png)
_Suivant_

Ensuite, cliquez sur "Exécuter". Cela accordera un accès complet à l'utilisateur exécutant le service Windows et au groupe d'administrateurs uniquement, mais les autres utilisateurs et groupes n'auront pas accès.

Donc, si vous avez plusieurs comptes utilisateur sur votre ordinateur, ils ne pourront pas accéder au serveur/Workbench MySQL. Si vous le souhaitez, vous pouvez modifier les paramètres ici en fonction de vos besoins.

Comme je n'ai qu'un seul compte utilisateur sur ma machine Windows, je peux garder la première option sélectionnée en toute sécurité.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38_3.png)
_Exécuter_

Cela peut prendre un certain temps. Ensuite, lorsque vous recevrez une case à cocher verte dans toutes les étapes de configuration, cliquez simplement sur "Terminer".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38_4.png)
_Terminer_

La configuration a été appliquée avec succès. Cliquez simplement sur "Suivant".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-39.png)
_Suivant_

Cliquez sur "Terminer" pour compléter l'installation.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-39_1.png)
_Terminer_

Cela ouvrira MySQL Workbench et MySQL Shell. Fermez simplement tous les deux maintenant.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-39_1-L.png)

## 539539 Configuration

Maintenant, nous devons configurer les variables de chemin pour notre système d'exploitation. Allez dans le lecteur où vous avez installé votre système d'exploitation Windows. Comme les autres, j'ai également installé mon système d'exploitation sur le lecteur "C".

Par conséquent, je vais dans le lecteur "C" et j'ouvre le répertoire "Program Files".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40.png)

Allez dans le dossier "MySQL".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_1.png)

Ensuite, allez dans le dossier MySQL Server.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_2.png)

Allez dans le dossier "bin".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_3.png)

Copiez le chemin/adresse.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_4.png)

Maintenant, ouvrez les paramètres des variables d'environnement. Cliquez simplement sur le bouton Windows et tapez "env".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_5.png)

Cliquez sur "Variables d'environnement".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41.png)

Sélectionnez "Path" et cliquez sur "Modifier".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41_1.png)

Cliquez sur "Nouveau". Une nouvelle case vide apparaîtra. Collez le chemin/adresse que vous avez copié précédemment. Ne fermez pas la fenêtre maintenant car nous devons faire la même chose pour le dossier MySQL Shell.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41_2.png)

Maintenant, nous devons faire la même chose pour MySQL Shell. Ouvrez le dossier MySQL Shell maintenant.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41_3.png)

Allez dans le dossier "bin".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41_4.png)

Copiez le chemin/répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42.png)

Maintenant, appliquez le même processus que précédemment. Cliquez sur "Nouveau" dans la fenêtre de modification des variables d'environnement. Collez le chemin/répertoire dans la nouvelle case vide.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42_1.png)

Maintenant, cliquez sur "OK".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42_2.png)

Cliquez à nouveau sur "OK".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42_3.png)

Et cliquez sur "OK" une fois de plus.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42_4.png)

## 539539 Finalisation

Notre tâche est maintenant terminée. Vous pouvez maintenant ouvrir MySQL Workbench.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43.png)

Cliquez simplement sur l'instance locale. Il demandera le mot de passe root. Entrez le mot de passe. Si vous ne voulez pas avoir la même corvée d'entrer un mot de passe à chaque fois, cochez la case pour enregistrer le mot de passe dans le coffre. Cliquez sur "OK".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_1.png)

C'est votre espace de travail MySQL Workbench par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_2.png)
_Espace de travail Workbench_

Si vous le souhaitez, vous pouvez également masquer l'onglet SQL Additions en cliquant sur la case colorée.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_3.png)

Pour obtenir les schémas, cliquez sur l'onglet "Schémas" dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_4.png)

Votre MySQL Workbench est également prêt pour tout type de processus de développement. Vous pouvez également utiliser MySQL à partir de votre terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_5.png)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_11-32.png)

## Conclusion

Merci d'avoir lu l'article entier.

Si vous avez des questions, n'hésitez pas à me contacter via [Twitter](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Assurez-vous également de me suivre sur [GitHub](https://github.com/FahimFBA) !

Vous pouvez également [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) pour plus de contenu vidéo utile.

Si vous êtes intéressé, vous pouvez également consulter mon site web : [https://fahimbinamin.com/](https://fahimbinamin.com/)

Bonne journée ! 60a

Couverture : Photo de [Boitumelo Phetla](https://unsplash.com/@writecodenow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/photos/0DJHJcpwN9Q?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)