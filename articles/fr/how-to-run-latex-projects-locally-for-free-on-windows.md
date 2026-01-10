---
title: Comment exécuter des projets LaTeX localement (gratuitement) sur Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2025-02-25T15:44:04.309Z'
originalURL: https://freecodecamp.org/news/how-to-run-latex-projects-locally-for-free-on-windows
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740494599916/ce7cfadb-985c-4245-9cc8-1ccba483ba69.png
tags:
- name: latex
  slug: latex
- name: Mathematics
  slug: mathematics
- name: Windows
  slug: windows
- name: research
  slug: research
seo_title: Comment exécuter des projets LaTeX localement (gratuitement) sur Windows
seo_desc: 'LaTeX is a high-quality typesetting system that is widely used in technical,
  academic, and scientific writing. It’s very popular in academia, especially in fields
  like mathematics, physics, computer science, and engineering.

  LaTeX is not a word proce...'
---

LaTeX est un système de composition de haute qualité largement utilisé dans les domaines techniques, académiques et scientifiques. Il est très populaire dans le milieu universitaire, notamment dans des domaines comme les mathématiques, la physique, l'informatique et l'ingénierie.

LaTeX n'est pas un traitement de texte comme Microsoft Word, mais plutôt un système de préparation de documents qui vous permet de vous concentrer sur le contenu de votre écriture tout en gérant la mise en forme. Si vous utilisez LaTeX pour rédiger vos documents formels (comme un CV, un curriculum vitæ ou un article de recherche), vous n'avez pas à vous soucier de la mise en forme et de la structure, car tout peut être fait à l'aide de scripts LaTeX.

Si vous utilisez LaTeX pour rédiger vos articles académiques ou de recherche, vous êtes peut-être familier avec des applications basées sur le web comme [Overleaf](https://www.overleaf.com/). Overleaf est un site web qui permet à quiconque de lire, écrire et compiler des scripts LaTeX en ligne.

Ces sites sont acceptables pour des petites tâches ou des compilations, ou si vous avez besoin d'un peu de collaboration gratuite. Mais si vous devez travailler sur des projets plus importants ou effectuer de nombreuses tâches collaboratives, l'offre gratuite peut être insuffisante. Et à mon avis, l'abonnement payant coûte trop cher.

Mais ne vous inquiétez pas : exécuter LaTeX localement pourrait être la solution parfaite pour vous. Je le sais car j'ai également été confronté à une situation similaire, et cela a simplement changé ma vie ! Je garde également toutes les traces dans Git (GitHub, GitLab, etc.) avec des opportunités de collaboration illimitées et de compilation. Et le plus beau, c'est que tout cela est complètement gratuit car tout se passe sur ma machine locale.

Alors dans cet article, je vais discuter des méthodes en détail. J'ai également créé une vidéo approfondie pour vous aider à comprendre comment cela fonctionne.

### Tutoriel Vidéo

%[https://www.youtube.com/watch?v=A45lWrndVHA]

## Ressources dont vous aurez besoin :

### 1. Dépôt GitHub

L'ensemble de ce guide est disponible dans l'un de mes projets GitHub nommé [Install-LaTeX](https://github.com/FahimFBA/Install-LaTeX). Le site web en direct est également disponible [ici](https://fahimfba.github.io/install-latex/) ([fahimfba.github.io/Install-LaTeX](https://fahimfba.github.io/Install-LaTeX/)). Je serais très reconnaissant si vous mettez une étoile (★) au dépôt. Vous pouvez également créer des issues [ici](https://github.com/FahimFBA/Install-LaTeX/issues) si vous rencontrez des problèmes. Toute contribution est également la bienvenue.

### 2. Système d'exploitation

Vous pouvez installer LaTeX sur n'importe quel système d'exploitation majeur (Windows, MacOS et systèmes d'exploitation basés sur Linux). Mais dans cet article, je vais uniquement parler du système d'exploitation Windows.

Ici, j'utilise le dernier système d'exploitation Windows 11, mais la même procédure devrait être applicable à tous les systèmes d'exploitation basés sur Windows qui sortiront à l'avenir. Windows 10 devrait également convenir.

### 3. Éditeur

Je vais utiliser le populaire [Visual Studio Code](https://code.visualstudio.com/) comme éditeur. C'est un éditeur 100 % gratuit et robuste, très populaire parmi les développeurs du monde entier. Si vous ne l'avez pas déjà, allez-y et installez-le avant de continuer.

![VS Code](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972339481/729ecab1-b87e-43d6-baf5-dbda170bcefc.png align="center")

### 4. Compilateur/IDE LaTeX

Pour travailler sur des fichiers LaTeX, vous aurez besoin d'un compilateur spécifique. Je vais utiliser [MikTeX](https://miktex.org/). Il existe d'autres outils, mais c'est le meilleur outil pour l'instant (selon moi !). Il est complètement gratuit et prend en charge tous les principaux systèmes d'exploitation. Il dispose également d'un IDE intégré, mais nous allons utiliser VS Code comme éditeur principal.

![MiKTeX](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972305065/8119b362-3c95-42a0-9458-be211d2ead35.png align="center")

Téléchargez le fichier exécutable Windows depuis la section Téléchargement.

![Télécharger MiKTeX](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972408494/71b39032-3adc-426e-8bd9-3a18dc454cf5.png align="center")

Après la fin du téléchargement, installez l'exécutable. À la fin de l'installation, gardez la coche dans "Vérifier les mises à jour maintenant".

![Vérifier les mises à jour](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972492255/a59f7000-8137-46c5-89f1-4f7151a751b6.png align="center")

Vous trouverez la console MikTeX dans votre barre des tâches. Ouvrez-la.

![Console MiKTeX](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972541856/e7bad89a-4920-4175-a361-ba8fb51f6b20.png align="center")

Allez dans l'onglet "Mises à jour" et cliquez sur "Mettre à jour maintenant". Cela installera tous ces packages.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972581283/6d585388-0218-4792-b78e-798c75dee6a6.png align="center")

À la fin, il vous demandera de fermer la console. Cliquez sur "OK". Ouvrez à nouveau MiKTeX.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972610846/926b5aba-0a3a-4c80-a103-fef5a5aafc38.png align="center")

C'est tout pour cet outil.

### 5. Perl

Les commandes que nous allons exécuter pour construire les fichiers LaTeX dépendent de Perl. Comme le système d'exploitation Windows ne dispose pas d'un compilateur Perl intégré, nous allons installer [Strawberry Perl](https://strawberryperl.com/).

![Perl](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972724660/7a6ad623-c2cc-45bd-bac6-08afdd5512c1.png align="center")

Téléchargez le dernier package MSI.

![Télécharger Strawberry Perl](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972749178/33c95897-37af-4be7-a24f-3520c3c1486e.png align="center")

Installez l'exécutable une fois le téléchargement de l'application terminé.

Nous devons ajouter le chemin de Perl à la variable d'environnement du système. Pour ce faire, allez dans l'emplacement où il a été installé. Par défaut, il est installé dans le répertoire `C:\Strawberry\perl\bin`. Copiez le chemin.

Recherchez maintenant "env" dans la barre de recherche Windows jusqu'à ce que vous trouviez quelque chose appelé "Modifier les variables d'environnement du système".

![env](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972898818/7cfdab3a-9ad0-47a7-b0ed-7721b589de97.png align="center")

Cliquez maintenant sur "Variables d'environnement...".

![Propriétés système](https://cdn.hashnode.com/res/hashnode/image/upload/v1739972945973/832e011b-0841-4318-a9b8-8b7a8ae42819.png align="center")

Sélectionnez maintenant "Path" dans "Variables système" et cliquez sur "Modifier".

![Variables système](https://cdn.hashnode.com/res/hashnode/image/upload/v1739973034756/df3d91f0-907e-42bf-9f1d-883172abd268.png align="center")

Cliquez sur "Nouveau". Collez le chemin. Fermez maintenant toutes les fenêtres en cliquant sur "OK" dans chaque fenêtre.

![ajouter var dans le chemin système](https://cdn.hashnode.com/res/hashnode/image/upload/v1739973087965/b73dd5e2-5c35-4399-a645-cb92ba43fe7b.png align="center")

## Extensions Visual Studio Code

Nous avons besoin de certaines extensions dans VS Code pour rationaliser notre flux de travail.

Tout d'abord, obtenons [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop). C'est l'extension principale pour travailler avec des fichiers LaTeX dans VS Code Studio.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1739973174197/2311c19b-d56e-4363-a3c0-75a9b0a323ee.png align="center")

Ensuite, vous aurez besoin de [Rewrap](https://marketplace.visualstudio.com/items?itemName=stkb.rewrap). C'est un outil incroyable qui vous permet de wrap les lignes plus longues. Il vous aide à travailler sur une longue ligne en lignes séparées sans casser aucune structure ou phrase.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1739973216887/86bacaa6-77ff-441c-acca-08ee6a74d354.png align="center")

## Construire le fichier LaTeX

Chaque fois que vous souhaitez construire un fichier LaTeX dans VS Code Studio, ouvrez simplement ce fichier. Ensuite, ouvrez la palette de commandes en utilisant `Ctrl` + `Shift` + `P`.

Recherchez "LaTeX Workshop: Build with recipe" et allez-y. Cela commencera à construire le fichier. Chaque fois qu'il vous demande d'installer un package manquant, décochez la case qui dit "Toujours afficher cette boîte de dialogue" et appuyez sur "Installer". Je fais cela car cliquer sur "Installer" sur des centaines de fenêtres de demande pour construire un fichier LaTeX est très difficile pour moi.

![installation du package](https://cdn.hashnode.com/res/hashnode/image/upload/v1739973393900/0ec3a626-38bb-4fbd-8f98-658cb6bc4853.png align="center")

Après avoir terminé la construction du fichier LaTeX, vous obtiendrez le fichier PDF de sortie dans VS Code. Vous pouvez ouvrir le fichier PDF directement dans VS Code.

Si vous souhaitez aller à une ligne spécifique dans le code à partir du fichier PDF de sortie comme Overleaf, cliquez simplement sur cette partie spécifique dans le PDF en appuyant sur la touche `Ctrl`. Cela vous amènera immédiatement à la partie du code où elle se trouve.

C'est tout ! Il fonctionne maintenant sur votre machine locale et il n'y a aucune restriction ni limitation, littéralement ! De plus, pour la collaboration et le suivi de l'historique, l'utilisation de Git est la meilleure option, comme je le fais.

## Conclusion

Merci d'avoir lu ce court tutoriel. J'espère qu'il vous a aidé à interagir plus facilement avec LaTeX.

Vous pouvez me suivre sur [GitHub](https://github.com/FahimFBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [YouTube](https://youtube.com/@FahimAmin) pour obtenir plus de contenu comme celui-ci. De plus, mon [site web](https://www.fahimbinamin.com/) est toujours disponible pour vous !