---
title: Comment GitHub Codespaces peut augmenter la productivité et réduire les obstacles
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-08-18T15:36:06.000Z'
originalURL: https://freecodecamp.org/news/how-github-codespaces-increase-productivity-and-lower-barriers
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cover-2.png
tags:
- name: codespaces
  slug: codespaces
- name: GitHub
  slug: github
seo_title: Comment GitHub Codespaces peut augmenter la productivité et réduire les
  obstacles
seo_desc: 'In this article, we''ll take a look at how GitHub Codespaces can help remove
  barriers for new teammates and contributors.

  The most recent integration between Visual Studio Code and GitHub really helps make
  development accessible and welcoming.

  Now in ...'
---

Dans cet article, nous allons voir comment GitHub Codespaces peut aider à supprimer les obstacles pour les nouveaux membres de l'équipe et les contributeurs.

La plus récente intégration entre Visual Studio Code et GitHub rend vraiment le développement accessible et accueillant.

Maintenant en bêta, [GitHub Codespaces](https://docs.github.com/en/github/developing-online-with-codespaces/about-codespaces) fournit un IDE en ligne, dans le navigateur, alimenté par Visual Studio Code.  

Cela vous permet d'utiliser cet IDE complet, avec des extensions, un terminal, des commandes Git et tous les paramètres auxquels vous êtes habitué, sur n'importe quelle machine. Vous pouvez maintenant emporter votre flux de travail de développement n'importe où en utilisant une tablette ou un autre appareil basé sur un navigateur.

Codespaces est également une excellente nouvelle pour les contributeurs open source. [Ajouter une configuration de codespace](https://docs.github.com/en/github/developing-online-with-codespaces/configuring-codespaces-for-your-project) à votre projet est un excellent moyen d'inviter de nouvelles personnes à commencer facilement à contribuer. 

Un nouveau contributeur open source ou un nouveau employé dans votre organisation peut rapidement lancer un codespace et commencer à travailler sur un `bon premier problème` sans avoir besoin de configurer ou d'installer un environnement local.

![Démarrer un nouveau codespace](https://victoria.dev/blog/add-productivity-remove-barriers-with-github-codespaces/open-with-codespaces-button.png)

Nous avons ajouté des paramètres de configuration de codespace sur le [Guide de test de sécurité Web OWASP (WSTG)](https://github.com/OWASP/wstg). Vous voulez l'essayer ? Consultez nos [problèmes ouverts](https://github.com/OWASP/wstg/issues).

## Configuration des Codespaces

Vous pouvez utiliser le dossier `.devcontainer` de Visual Studio Code pour configurer un conteneur de développement pour votre dépôt également. 

De nombreux [conteneurs pré-construits sont disponibles](https://github.com/microsoft/vscode-dev-containers/tree/master/containers) – il suffit de copier le `.devcontainer` dont vous avez besoin à la racine de votre dépôt. Si votre dépôt n'en a pas, une [image Linux de base par défaut](https://github.com/microsoft/vscode-dev-containers/tree/master/containers/codespaces-linux) sera utilisée.

Voici une raison de supprimer `.vscode` de votre fichier `.gitignore`. Tout nouveau codespace créé dans votre dépôt respectera désormais les paramètres trouvés dans `.vscode/settings.json`. Cela signifie que votre IDE en ligne peut avoir la même configuration d'espace de travail que celle que vous avez sur votre machine locale. N'est-ce pas utile !

## Personnalisation des Codespaces

Pour une personnalisation de niveau supérieur des [dotfiles](https://docs.github.com/en/github/developing-online-with-codespaces/personalizing-codespaces-for-your-account), envisagez de commiter les fichiers pertinents de votre dossier local `dotfiles` en tant que dépôt GitHub public à l'adresse `votreutilisateur/dotfiles`. 

Lorsque vous créez un nouveau codespace, cela intègre vos configurations, telles que les alias de shell et les préférences, en créant des liens symboliques vers les dotfiles dans votre codespace `$HOME`. Cela personnalise tous les codespaces que vous créez dans votre compte. 

Besoin d'inspiration ? Parcourez [mon dépôt de dotfiles sur GitHub](https://github.com/victoriadrake/dotfiles).

## Développement dans les Codespaces

[Développer dans un codespace](https://docs.github.com/en/github/developing-online-with-codespaces/developing-in-a-codespace) est une expérience familière pour les utilisateurs de Visual Studio Code, jusqu'à l'exécution d'une application localement. 

Grâce au [transfert de port](https://docs.github.com/en/github/developing-online-with-codespaces/developing-in-a-codespace), lorsque j'exécute une application dans un terminal de codespace, en cliquant sur l'URL `localhost` résultante, je suis redirigé vers le port approprié tel que sorti de mon codespace. 

Lorsque je travaille sur [mon blog](https://victoria.dev/) dans mon codespace, par exemple, j'exécute `hugo serve` puis je clique sur le lien `localhost:1313` fourni pour voir un aperçu de mes modifications dans un autre onglet du navigateur.

Vous voulez rester synchronisé entre les appareils ? Il y a une extension pour cela. Vous pouvez [vous connecter à votre codespace depuis Visual Studio Code](https://docs.github.com/en/github/developing-online-with-codespaces/connecting-to-your-codespace-from-visual-studio-code) sur votre machine locale pour toujours reprendre là où vous vous êtes arrêté.

## Développez n'importe où

Codespaces est un ajout super excitant à mon flux de travail GitHub. Il me permet d'accéder à mon processus de développement complet pratiquement n'importe où, en utilisant des appareils comme mon iPad. 

Cela facilitera également la tâche des nouveaux contributeurs open source ou des nouveaux employés dans votre organisation pour se lancer avec un IDE déjà configuré. 

Si vous avez accès à la bêta limitée, je vous invite à lancer un codespace et à essayer de [contribuer au WSTG](https://github.com/OWASP/wstg/issues), ou à [un problème sur l'un de mes projets open source](https://github.com/users/victoriadrake/projects/1).

J'ai hâte de voir la disponibilité générale et de découvrir ce que la communauté open source imaginera pour GitHub Codespaces ensuite !

Et oui – les codespaces supportent [votre thème préféré de Visual Studio Code](https://github.com/victoriadrake/kabukicho-vscode). ?

![Image](https://www.freecodecamp.org/news/content/images/2020/08/codespace.png)
_Capture d'écran d'un codespace avec le thème [Kabukichō](https://marketplace.visualstudio.com/items?itemName=VictoriaDrake.kabukicho" rel="noopener) pour Visual Studio Code_