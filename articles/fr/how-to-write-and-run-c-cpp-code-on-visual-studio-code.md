---
title: Comment écrire et exécuter du code C et C++ dans Visual Studio Code
date: '2023-01-20T21:45:48.000Z'
author: Md. Fahim Bin Amin
authorURL: https://www.freecodecamp.org/news/author/FahimFBA/
originalURL: https://freecodecamp.org/news/how-to-write-and-run-c-cpp-code-on-visual-studio-code
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/asd.png
tags:
- name: C++
  slug: c-2
- name: c programming
  slug: c-programming
- name: compilers
  slug: compilers
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_desc: 'Visual Studio Code (or VS Code for short) is a very common and widely used
  text editor and IDE (Integrated Development Environment). You can make VS Code very
  powerful like an IDE using a lot of extensions.

  Before approaching the process of running y...'
---


Visual Studio Code (ou VS Code en abrégé) est un éditeur de texte et un IDE (Environnement de Développement Intégré) très commun et largement utilisé. Vous pouvez rendre VS Code très puissant, à l'instar d'un IDE, en utilisant de nombreuses extensions.

<!-- more -->

Avant d'aborder le processus d'exécution de votre premier code C ou C++ sur Visual Studio Code, laissez-moi vous guider à travers les étapes de configuration en fonction du système d'exploitation que vous utilisez sur votre ordinateur.

## Compilateurs C et C++

Pour exécuter du code C ou C++, vous devez simplement avoir un compilateur C/C++ valide installé sur votre ordinateur. Si vous utilisez un système d'exploitation Linux, il y a de fortes chances qu'il soit déjà installé. Mais nous devons nous assurer qu'il est correctement configuré.

Pour vérifier si vous avez le compilateur (GCC/G++/MinGW) installé sur votre système, vous devez d'abord vérifier la version du compilateur.

Ouvrez simplement votre terminal et utilisez `gcc --version` et `g++ --version`. Si vous obtenez le numéro de version, le compilateur est déjà installé sur votre système.

Vous pouvez vérifier la version en utilisant les mêmes commandes sur n'importe quel système d'exploitation, qu'il s'agisse de Windows, Linux ou macOS.

Si votre terminal vous indique qu'il ne connaît pas GCC ou G++, vous devez alors installer le compilateur correctement.

Si vous utilisez le système d'exploitation Windows, j'ai déjà écrit un article approfondi montrant toutes les étapes du processus sur freeCodeCamp. Assurez-vous de lire l'article complet au préalable, car il contient également une vidéo complète pour vous accompagner.

[Contenu intégré][1]

Si vous utilisez un autre système d'exploitation et que vous n'avez pas les compilateurs installés, veillez à les installer avant de continuer.

## Comment installer VS Code ou VS Code Insiders

Vous devez télécharger Visual Studio Code directement depuis le site officiel : [https://code.visualstudio.com/][2].

Si vous le souhaitez, vous pouvez également installer VS Code Insiders ; le processus est identique.

Visual Studio Code Insiders est en fait la version "Insiders" de Visual Studio Code, qui contient toutes les dernières fonctionnalités publiées quotidiennement. Vous pouvez considérer VS Code comme la version stable et VS Code Insiders comme la version de test (Insiders).

Si vous voulez découvrir les dernières mises à jour instantanément, vous pouvez essayer Visual Studio Code Insiders (je l'utilise moi-même). Pour télécharger VS Code Insiders, vous pouvez visiter le site officiel ici : [https://code.visualstudio.com/insiders/][3]

Assurez-vous de télécharger le fichier correspondant exactement à votre système d'exploitation.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-163.png) _**Page de téléchargement : VS Code**_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-164.png) _**Page de téléchargement : VS Code Insiders**_

Le processus d'installation est assez basique. Mais je vais vous montrer toutes les étapes séquentiellement. Pour l'instant, je vais illustrer le processus d'installation avec VS Code Insiders, mais tout ce que vous verrez ici sera exactement identique pour VS Code.

Veillez à cocher la case "Je comprends et j'accepte les termes du contrat de licence" et cliquez sur **Suivant**.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-165.png) _**Acceptez le contrat et cliquez sur Suivant**_

Laissez tout tel quel. Ne modifiez rien ici.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-168.png) _**Cliquez sur Suivant**_

Cliquez sur **Suivant**. Encore une fois, cliquez simplement sur **Suivant**.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-170.png) _**Cliquez sur Suivant**_

Assurez-vous de cocher (✔) toutes les cases. Cliquez ensuite sur **Suivant**.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-171.png) _**Cochez toutes les cases et cliquez sur Suivant**_

Cliquez sur **Installer**.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-172.png) _**Cliquez sur Installer**_

L'installation peut prendre un peu de temps.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-173.png) _**Laissez l'installation se terminer...**_

Cliquez sur **Terminer**.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-175.png) _**Cliquez sur Terminer**_

Félicitations ! Vous avez installé avec succès VS Code/VS Code Insiders sur votre système. Santé ! 🥂

## Comment préparer VS Code/VS Code Insiders pour le code C et C++

Tout d'abord, ouvrez VS Code ou VS Code Insiders.

Allez dans l'onglet Extensions. Recherchez "C" ou "C++" et installez la première extension, qui est déjà vérifiée par Microsoft.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-178.png) _**Installer l'extension C/C++**_

Installez également le **C/C++ Extension Pack**. Il doit également être vérifié par Microsoft.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-179.png) _**Installer le C/C++ Extension Pack**_

Ensuite, recherchez **Code Runner** et installez également cette extension.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-180.png) _**Installer l'extension Code Runner**_

Maintenant, nous devons modifier certains paramètres.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-177.png) _**Modifier certains paramètres**_

Cliquez sur l'icône d'**engrenage** (section Gérer), puis cliquez sur **Paramètres**. Alternativement, vous pouvez utiliser le raccourci clavier `Ctrl` + `,`. Remplacez la touche `Ctrl` par la touche Command sur Mac.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-182.png) _**Tapez "Run code in terminal" et appuyez sur Entrée**_

Dans la barre de recherche, tapez "Run code in terminal" et appuyez sur la touche Entrée.

Faites défiler un peu vers le bas jusqu'à trouver `Code-runner: Run In Terminal`. Assurez-vous que la case est cochée (✔).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-184.png) _**Assurez-vous de cocher la case**_

Vous devez maintenant redémarrer VS Code/VS Code Insiders. Fermez simplement et rouvrez le programme.

## Comment tester votre code

Ouvrez simplement VS Code/VS Code Insiders, ouvrez n'importe quel dossier et créez un fichier avec l'extension `.c` pour un fichier C ou `.cpp` pour un fichier C++.

Après avoir écrit votre code, vous pouvez l'exécuter directement en utilisant le bouton "Play" situé dans le coin supérieur droit.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-185.png) _**Voici comment exécuter n'importe quel programme C/C++ depuis VS Code/Insiders**_

Le programme sera compilé puis exécuté directement. Après une première exécution, le bouton Code Runner sera configuré par défaut pour une exécution directe. Votre ordinateur est désormais 100 % prêt pour compiler et exécuter du code de programmation C/C++. 😀

## Conclusion

Merci d'avoir lu cet article. S'il vous a été utile, vous pouvez également consulter mes autres articles sur [freeCodeCamp][4].

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter][5], [LinkedIn][6] et [GitHub][7].

Vous pouvez également vous [ABONNER à ma chaîne YouTube][8] (Code With FahimFBA) si vous souhaitez apprendre divers langages de programmation avec de nombreux exemples pratiques réguliers.

Si vous voulez voir mes moments forts, vous pouvez consulter ma [chronologie Polywork][9].

Vous pouvez également [visiter mon site web][10] pour en savoir plus sur moi et mes projets actuels.

Merci beaucoup !

[1]: https://www.freecodecamp.org/news/how-to-install-c-and-cpp-compiler-on-windows/
[2]: https://code.visualstudio.com/
[3]: https://code.visualstudio.com/insiders/
[4]: https://www.freecodecamp.org/news/author/fahimbinamin/
[5]: https://twitter.com/Fahim_FBA
[6]: https://www.linkedin.com/in/fahimfba/
[7]: https://github.com/FahimFBA
[8]: https://www.youtube.com/@FahimAmin?sub_confirmation=1
[9]: https://www.polywork.com/fahimbinamin
[10]: https://fahimbinamin.com/