---
title: Comment installer les compilateurs C et C++ sur Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-02-22T18:04:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-c-and-cpp-compiler-on-windows
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/banner_freeCodeCamp.png
tags:
- name: C++
  slug: c-2
- name: c programming
  slug: c-programming
- name: compilers
  slug: compilers
seo_title: Comment installer les compilateurs C et C++ sur Windows
seo_desc: "If you want to run C or C++ programs in your Windows operating system,\
  \ then you need to have the right compilers. \nThe MinGW compiler is a well known\
  \ and widely used software for installing GCC and G++ compilers for the C and C++\
  \ programming language..."
---

Si vous souhaitez exécuter des programmes C ou C++ sur votre système d'exploitation Windows, vous devez avoir les bons compilateurs. 

Le compilateur MinGW est un logiciel bien connu et largement utilisé pour installer les compilateurs GCC et G++ pour les langages de programmation C et C++. 

Mais de nombreux développeurs rencontrent des difficultés lors de l'installation du compilateur, alors je vais vous montrer toutes les étapes à suivre dans cet article avec des captures d'écran pour vous aider à le faire. 

J'utiliserai Windows 11, mais le même processus est applicable pour tous les autres systèmes d'exploitation Windows, sauf si vous utilisez Windows XP (vous devez changer certaines étapes dans Windows XP).

Si vous souhaitez également regarder la vidéo que j'ai faite sur ce sujet, la voici :

%[https://www.youtube.com/watch?v=c7FjV8Gwk_M]

## Installer MSYS2

Tout d'abord, nous devons télécharger un fichier exécutable depuis MSYS2. Rendez-vous sur le site officiel de MSYS2 : [https://www.msys2.org/](https://www.msys2.org/). Le site ressemble à ceci aujourd'hui.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--8-.png)

Faites défiler un peu jusqu'à ce que vous trouviez le bouton de téléchargement pour le fichier exécutable.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--9-.png)

Cliquez simplement sur le bouton d'installation et enregistrez le fichier d'installation à l'endroit de votre choix.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--10--1.png)

Terminez le téléchargement du fichier exécutable. Cela ne devrait pas prendre beaucoup de temps en fonction de votre vitesse de connexion Internet.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--11-.png)

Après avoir téléchargé le fichier, nous obtiendrons ce fichier exécutable.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--12-.png)

Double-cliquez sur le fichier exécutable. Ensuite, cliquez sur `Suivant`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--13-.png)

Gardez le nom tel quel et cliquez sur `Suivant`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--14--1.png)

Gardez tout cela tel quel et cliquez sur `Suivant`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--15-.png)

Donnez-lui un peu de temps pour terminer le processus d'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--16-.png)

Si vous gardez la coche, le terminal MSYS2 s'ouvrira une fois que vous cliquerez sur `Terminer`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--17-.png)

Je préfère faire cela de cette manière, mais si vous souhaitez effectuer les tâches restantes plus tard, vous devez ouvrir le terminal vous-même depuis le menu Démarrer. 

Dans ce cas, vous devez cliquer sur le bouton Démarrer > Rechercher `MSYS2` et cliquer sur le terminal comme dans l'image suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--26-.png)

Supposons que nous avons ouvert le terminal **MSYS2 MSYS** avec succès.

Appliquez la commande `pacman -Syu` pour mettre à jour la base de données des paquets et les paquets de base.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--19-.png)

Tapez `Y` et appuyez sur la touche Entrée si vous obtenez ce type d'invite d'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--20-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--21-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--22-.png)

Tapez `Y` et appuyez sur la touche Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--23-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--24-.png)

Le terminal sera fermé. Nous devons ouvrir le terminal manuellement et mettre à jour le reste des paquets.

Cliquez sur le bouton Démarrer.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--25-.png)

Recherchez le dossier nommé **MSYS2 64bit**. Cliquez sur le dossier pour l'expanser et obtenir le terminal. Ouvrez le terminal en cliquant sur **MSYS2 MSYS**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--26--1.png)

Mettez à jour le reste des paquets en appliquant la commande `pacman -Su`. Vous devrez peut-être appliquer la commande `pacman -Sy` si le terminal vous le demande.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--27-.png)

Si vous obtenez une invite d'installation, vous devez taper `Y` ou `y` et appuyer sur la touche Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--28-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--29-.png)

Attendez un peu pour terminer l'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--30-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--31-.png)

Fermez la fenêtre après avoir terminé l'installation.

## Installer les compilateurs GCC et G++

Cliquez sur le bouton Démarrer. Trouvez le dossier **MSYS2 64bit**. Cliquez sur ce dossier pour l'expanser.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--32-.png)

Si vous utilisez un système d'exploitation **64 bits** comme moi, alors nous devons utiliser le terminal **MSYS2 MinGW x64**. Cliquez sur le terminal pour l'ouvrir.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--33-.png)

⚠️ Mais, si vous utilisez un système d'exploitation **32 bits**, alors vous devez utiliser le terminal **MSYS2 MinGW x86**. Ensuite, vous devez ouvrir ce terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--34-.png)

Comme j'utilise un système d'exploitation **64 bits**, j'ai ouvert le terminal pour 64 bits. Appliquez la commande `pacman -S mingw-w64-x86_64-gcc` pour installer les compilateurs.

⚠️ Si vous utilisez un système d'exploitation **32 bits**, alors vous devez appliquer la commande `pacman -S mingw-w64-i686-gcc` dans votre terminal 32 bits.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--35-.png)

Attendez un peu.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--36-.png)

Tapez `Y` ou `y` et appuyez sur la touche Entrée si vous obtenez les invites d'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--37-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--38-.png)

Donnez-lui un peu de temps pour terminer le processus d'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--39-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--39--1.png)

Vous avez maintenant terminé l'installation des compilateurs.

## Comment installer le débogueur

Si vous utilisez un système d'exploitation **64 bits** comme moi, alors vous devez appliquer la commande `pacman -S mingw-w64-x86_64-gdb`.

⚠️ Si vous utilisez un système d'exploitation **32 bits**, alors vous devez appliquer la commande `pacman -S mingw-w64-i686-gdb` dans votre terminal 32 bits.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--41-.png)

Si vous obtenez une invite d'installation, tapez simplement `Y` ou `y` et appuyez sur la touche Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--42-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--38--1.png)

Donnez-lui un peu de temps pour terminer l'installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--44-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--45-.png)

Vous pouvez fermer le terminal.

## Comment ajouter le répertoire au chemin des variables d'environnement

Ouvrez l'explorateur de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--46-.png)

Je suppose que vous avez installé MSYS dans le répertoire par défaut comme je l'ai fait. Si vous avez utilisé des répertoires personnalisés, alors vous devez vous rendre dans le répertoire où vous l'avez installé.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--47-.png)

Si vous utilisez un système d'exploitation 64 bits comme moi, alors allez dans le dossier **mingw64**.

⚠️ Si vous utilisez un système d'exploitation 32 bits, alors allez dans le dossier **mingw32**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--48-.png)

Nous devons maintenant aller dans le dossier binaire. Allez dans le dossier **bin**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--49-.png)

⚠️ Si vous utilisez un système d'exploitation 32 bits, alors vous devez aller dans votre dossier **mingw32** > dossier **bin**.

Copiez le répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--51-.png)

⚠️ Si vous utilisez un système d'exploitation 32 bits et que vous avez également installé MSYS2 dans le répertoire par défaut, alors votre répertoire devrait être comme suit :

```
C:\msys64\mingw32\bin
```

Ouvrez les **Paramètres système avancés**. Vous pouvez le faire de plusieurs manières. Une manière simple est de cliquer sur le bouton Démarrer et de le rechercher comme dans la capture d'écran ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--52-.png)

Cliquez sur **Variables d'environnement** dans l'onglet Avancé.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--54-.png)

Cliquez sur **Path** et sélectionnez-le. Ensuite, cliquez sur **Modifier**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--57-.png)

Une fenêtre apparaîtra comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--58-.png)

Cliquez sur **Nouveau**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--59-.png)

Une boîte vide apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--60-.png)

Collez le répertoire ici.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--61-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--62-.png)

Cliquez sur **OK**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--63-.png)

Cliquez sur **OK**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--65-.png)

Cliquez sur **OK**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--66-.png)

Si vous souhaitez obtenir toutes les étapes dans une vidéo, vous pouvez également regarder [cette vidéo](https://www.youtube.com/watch?v=0HD0pqVtsmw).

## Vérifier l'installation

Maintenant, il est temps de vérifier si nous avons réussi à installer tout ce qui précède ou non.

Ouvrez le terminal / PowerShell / CMD et appliquez les commandes en série :

Pour vérifier la version de **GCC** :

```powershell
gcc --version
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--68-.png)

Pour vérifier la version de **G++** :

```powershell
g++ --version
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--69-.png)

Pour vérifier la version de **GDB** :

```powershell
gdb --version
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--70-.png)

## Conclusion

J'espère que cet article vous aide à installer vos compilateurs sur le système d'exploitation Windows pour les programmes C et C++. 

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/) et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers types de langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !