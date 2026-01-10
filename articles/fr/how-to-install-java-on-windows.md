---
title: Comment installer Java sur Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-03-03T18:07:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-java-on-windows
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/fCC-Cover-Image.jpg
tags:
- name: Java
  slug: java
- name: Windows
  slug: windows
seo_title: Comment installer Java sur Windows
seo_desc: "If you want to run any Java program on your Windows PC, you won't be able\
  \ to do it without installing the Java Development Kit (JDK for short). \nThe JDK\
  \ also contains the Java Runtime Environment (or JRE) which is the core of a Java\
  \ program. \nIf you ..."
---

Si vous souhaitez exécuter un programme Java sur votre PC Windows, vous ne pourrez pas le faire sans installer le Java Development Kit (JDK en abrégé). 

Le JDK contient également le Java Runtime Environment (ou JRE) qui est le cœur d'un programme Java. 

Si vous êtes un débutant essayant d'apprendre à exécuter des programmes Java dans votre système d'exploitation Windows, vous pourriez rencontrer des difficultés à installer Java correctement sur votre ordinateur. Mais ne craignez rien ! Je vais couvrir tout ce que vous devez savoir pour préparer votre ordinateur Windows à exécuter des programmes Java.

J'utiliserai Windows 11 dans cet article, mais la même méthode est applicable aux autres versions du système d'exploitation Windows.

## Télécharger Java depuis Oracle

Si vous vous demandez pourquoi nous téléchargeons Java depuis Oracle, alors l'extrait suivant de [Wikipedia](https://en.wikipedia.org/wiki/Oracle_Corporation) vous aidera :

> Java est un ensemble de logiciels et de spécifications informatiques développés par James Gosling chez Sun Microsystems, qui a ensuite été acquis par Oracle Corporation, fournissant un système pour développer des logiciels d'application et les déployer dans un environnement informatique multiplateforme.

Nous téléchargeons le JDK officiel directement depuis le site officiel d'Oracle. Alors, rendez-vous sur leur site : [https://www.oracle.com/](https://www.oracle.com/).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--13--1.png)

Vous pourriez obtenir ce type d'invite pour vous rappeler d'aller dans le pays le plus proche de vous afin d'obtenir une meilleure vitesse de téléchargement. Comme je suis du Bangladesh, il me suggère de visiter Oracle Bangladesh. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--14-.png)

Vous pouvez sélectionner le pays le plus proche de vous pour obtenir une meilleure vitesse de téléchargement, mais si vous ne voulez pas et souhaitez simplement télécharger depuis le site global, c'est bien aussi. Vous obtiendrez le même fichier d'installation.

Ensuite, le site pourrait se recharger.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--17-.png)

Cliquez sur **Produits**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--18-.png)

Puis cliquez sur **Java**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--19-.png)

Cela nous amènera à la page produit de Java.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--21-.png)

Cliquez sur **Télécharger Java**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--21--1.png)

Vous obtiendrez alors la page de téléchargement.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--22-.png)

Faites simplement défiler vers le bas jusqu'à obtenir l'onglet de sélection du système d'exploitation (OS).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--23-.png)

Puisque vous souhaitez installer Java sur votre ordinateur Windows, cliquez simplement sur **Windows**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--24-.png)

Puis cliquez sur **x64 Installer**. Vous obtiendrez une invite pour télécharger le fichier d'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--25-.png)

Téléchargez le fichier exécutable. Vous devrez attendre un peu pour que le processus de téléchargement se termine.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--26-.png)

## Comment installer Java

Après avoir téléchargé le fichier, vous obtiendrez un fichier exécutable comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--27-.png)

Double-cliquez simplement sur ce fichier. Un assistant d'installation apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--28-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--29-.png)

Cliquez sur `**Suivant>**`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--30-.png)

Nous utiliserons le répertoire par défaut. Cliquez donc sur `**Suivant>**`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--31-.png)

Terminez le processus d'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--32-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--33-.png)

Après avoir terminé l'installation, cliquez sur **Fermer** pour fermer l'assistant d'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--35-.png)

## Comment ajouter le répertoire au chemin de la variable d'environnement

Ouvrez l'explorateur de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--36-.png)

Allez dans le répertoire où vous avez installé l'installateur précédemment. Dans ce cas, le répertoire par défaut est toujours le **lecteur C.** 

Après être entré dans le lecteur C, allez dans le dossier **Program Files**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--38-.png)

Allez dans le dossier Java.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--39-.png)

Allez dans le dossier `**jdk-17.0.2**`. Ici, `**17.0.2**` représente la version du JDK. Dans votre cas, la version pourrait être différente car le JDK sera mis à jour à l'avenir, mais le processus est exactement le même.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--40-.png)

Allez dans le dossier **bin**. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--41-.png)

Les fichiers binaires sont conservés ici.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--42-.png)

Nous devons copier le chemin du répertoire (adresse du répertoire) de ce dossier.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--43-.png)

Copiez simplement l'adresse en utilisant votre souris, ou vous pouvez utiliser le raccourci `Ctrl` + `A` pour tout sélectionner, puis `Ctrl` + `C` pour copier le répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--44-.png)

Allez dans le **Panneau de configuration**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--45-.png)

Allez dans **Système et sécurité**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--47-.png)

Cliquez sur **Système**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--49-.png)

Cliquez sur **Paramètres système avancés**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--51-.png)

**Alternativement**, vous pouvez accéder aux Paramètres système avancés en les recherchant simplement depuis votre barre des tâches.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-03-103840.png)

Cliquez sur Variables d'environnement.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--53-.png)

Sélectionnez le Chemin et cliquez sur Modifier.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--55-.png)

Cliquez sur Nouveau.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--58-.png)

Une boîte vide apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--59--1.png)

Collez le chemin du répertoire. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--60-.png)

Vous pouvez également utiliser les touches de raccourci `Ctrl` + `V` pour cela.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--61-.png)

Cliquez sur OK.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--62-.png)

Cliquez sur OK.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--64-.png)

Cliquez sur OK.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--65-.png)

## Comment vérifier si Java a été installé avec succès

Ouvrez le terminal (CMD ou PowerShell).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--66-.png)

Vérifiez la version de Java en utilisant `java --version`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--68-.png)

Si la version que vous venez d'installer est affichée, alors vous êtes prêt à partir !

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--69-.png)

Alternativement, vous pouvez simplement exécuter du code Java pour vérifier s'il fonctionne ou non. Pour l'instant, je vais exécuter un simple code Hello World en Java. J'ai utilisé le bloc-notes pour l'instant, mais vous pouvez utiliser n'importe quel éditeur de texte que vous voulez.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--70-.png)

Compilez votre code Java en utilisant `javac nom_du_fichier_avec_extension`. Ensuite, exécutez le fichier de classe en utilisant `java nom_du_fichier_sans_extension`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--71-.png)

Wow ! Tout fonctionne parfaitement. Votre machine Windows est prête à exécuter n'importe quel programme Java maintenant.

J'ai également [publié une vidéo](https://youtu.be/jGuh6IV-5Vw) sur ma [chaîne YouTube en anglais](https://www.youtube.com/channel/UCG97GCUifMS2Vm28tgXQi0Q) où je vous guide à travers tous les processus mentionnés ci-dessus. Vous pouvez également la consulter ici :

%[https://www.youtube.com/watch?v=jGuh6IV-5Vw]

## Conclusion

J'espère que cet article vous aide à installer Java sur votre machine Windows. 

Si vous souhaitez savoir comment installer les compilateurs C et C++ pour votre système d'exploitation Windows, [vous pouvez consulter cet article](https://www.freecodecamp.org/news/how-to-install-c-and-cpp-compiler-on-windows/).

Si vous souhaitez savoir comment installer Python sur votre Windows, [vous pouvez consulter cet article](https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/).

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !