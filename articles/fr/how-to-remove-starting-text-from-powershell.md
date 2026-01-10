---
title: Comment supprimer le texte de démarrage de PowerShell
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-03-22T17:18:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-starting-text-from-powershell
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Artboard-1-1.jpg
tags:
- name: Powershell
  slug: powershell
- name: Windows
  slug: windows
seo_title: Comment supprimer le texte de démarrage de PowerShell
seo_desc: "If you are using a Windows operating system, you have likely used the latest\
  \ Windows PowerShell at least once. \nWhenever you open PowerShell using Windows\
  \ Terminal, you get a text message inside the terminal which shows the PowerShell\
  \ version, the li..."
---

Si vous utilisez un système d'exploitation Windows, vous avez probablement utilisé la version la plus récente de Windows PowerShell au moins une fois. 

Chaque fois que vous ouvrez PowerShell en utilisant Windows Terminal, vous obtenez un message texte à l'intérieur du terminal qui affiche la version de PowerShell, le lien pour télécharger la dernière version de PowerShell, et ainsi de suite. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--3--1.png)

Parfois, cela peut être agaçant, et vous pourriez vouloir supprimer ce texte pour que ce message n'apparaisse plus jamais. Il existe un moyen de le faire, et dans cet article, je vais vous montrer comment vous pouvez supprimer le texte de démarrage du terminal une fois pour toutes ! ✌️

Tout d'abord, ouvrez PowerShell dans Windows Terminal. Vous obtiendrez le texte de démarrage comme d'habitude.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--3--2.png)

Cliquez sur le bouton du menu déroulant pour afficher le menu situé en dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--4-.png)

Allez dans **Paramètres**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--5-.png)

Vous obtiendrez une interface comme celle ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--6-.png)

Cliquez sur **Ouvrir le fichier JSON**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--7-.png)

Le fichier JSON s'ouvrira dans un éditeur de texte. Pour moi, il s'agit du Bloc-notes – mais pour vous, il peut s'agir de VS Code ou de tout autre éditeur de texte de votre choix.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--9-.png)

Faites défiler vers le bas jusqu'à ce que vous trouviez le bloc PowerShell comme ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--12-.png)

Ajoutez `"commandline": "pwsh.exe -nologo",` comme ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--14--1.png)

La commande devrait ressembler à ceci pour le bloc PowerShell :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--15-.png)

Puis enregistrez le fichier. Vous pouvez également utiliser les touches de raccourci `Ctrl` + `S` pour cela.

Cliquez sur **Enregistrer**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--16-.png)

Fermez tous les onglets.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--17--1.png)

Rouvrez le terminal et admirez la magie ! 🪄

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--19--1.png)

## Conclusion

Merci d'avoir lu cet article en entier. S'il vous a aidé, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [vous ABONNER à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers langages de programmation avec de nombreux exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce sur quoi je travaille.

Merci beaucoup !

L'image de la bannière provient de [storyset](https://storyset.com/worker) (Worker illustrations par Storyset) et a été modifiée à l'aide d'Adobe Photoshop.