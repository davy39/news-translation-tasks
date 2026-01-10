---
title: Automatiser la configuration de votre sous-système Windows pour Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T18:07:26.000Z'
originalURL: https://freecodecamp.org/news/automating-your-windows-subsystem-linux-setup-df4c9a7b0e7b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*03UuTGdsAF5PEgaI4BwYZg.jpeg
tags:
- name: Node.js
  slug: nodejs
- name: terminal
  slug: terminal
- name: Web Development
  slug: web-development
- name: Windows 10
  slug: windows-10
- name: WSL
  slug: wsl
seo_title: Automatiser la configuration de votre sous-système Windows pour Linux
seo_desc: 'By Scott Spence

  I’m a Windows user and have been so for as long as I can remember. I have fiddled
  around with Linux as well but have stuck to Windows as I’ve found it to be a bit
  less neckbeardy for me. Both have their pros and cons. But one of the b...'
---

Par Scott Spence

Je suis un utilisateur de Windows et je le suis depuis aussi longtemps que je m'en souvienne. J'ai également bidouillé avec Linux mais je suis resté sur Windows car j'ai trouvé que c'était un peu moins « neckbeardy » pour moi. Les deux ont leurs avantages et leurs inconvénients. Mais l'un des plus grands inconvénients de Windows pour moi lorsque j'ai commencé à apprendre le développement web était le manque de tous mes outils de ligne de commande Linux.

C'était jusqu'à ce que le sous-système Windows pour Linux (WSL) arrive ?

J'adore ça ! Vous pouvez avoir un shell Bash dans Windows et exécuter toutes vos applications Node.js à travers lui aussi et avec la mise à jour Windows 10 Fall Creators Update, WSL est vraiment facile à configurer.

Petite histoire rapide sur pourquoi je publie ceci. J'ai détruit mon ordinateur portable l'autre jour car j'avais des problèmes avec Bash sur Windows liés en partie à l'utilisation de [nvm](https://github.com/Microsoft/WSL/issues/776) avec WSL. Je commençais à m'énerver avec la façon dont mon ordinateur fonctionnait. Mais je réalise maintenant que j'ai surréagi.

Après avoir remis mon ordinateur en marche, j'ai dû reconfigurer mon environnement de développement à partir de zéro. Heureusement pour moi, je garde tous mes paramètres et informations de configuration dans un [dépôt GitHub](https://github.com/spences10/settings) en cas d'obtention d'un nouvel ordinateur ou pour récupérer après un événement catastrophique (comme un ordinateur détruit).

Dans cet article, je voudrais vous montrer comment je configure mon sous-système Windows pour Linux pour mon environnement de développement.

Ceci est mon point de vue subjectif sur ma configuration spécifique et mon utilisation de WSL et voici mon guide étape par étape pour la prochaine fois que je devrai créer un environnement de développement à partir de zéro sur Windows.

Donc, après avoir installé [WSL](https://www.microsoft.com/store/productId/9NBLGGH4MSV6) depuis le Microsoft Store et ajouté votre utilisateur par défaut, la première chose à faire est de tout mettre à jour et améliorer.

```
sudo apt updatesudo apt -y upgrade
```

Si vous n'avez jamais utilisé de distributions Linux auparavant, le `-y` dans l'instruction de mise à niveau est pour définir la réponse par défaut à « Oui » pour toute invite affichée dans le terminal. Vous ne voudrez peut-être pas faire cela, car il peut y avoir certains programmes que vous ne souhaitez pas mettre à jour, mais je le fais.

![Image](https://cdn-media-1.freecodecamp.org/images/OXOMF6dNg6mFcLndoTphMYRDL76E880tt09a)
_Oui à toutes les choses !_

En ajoutant le drapeau `-y`, vous n'aurez plus ces messages ?

**Outils de construction**

Pour compiler et installer des modules complémentaires natifs depuis npm, vous devrez peut-être également installer des outils de construction. J'en ai besoin pour les images Gatsby qui utilisent `sharp` qui utilise à son tour `node-gyp` :

```
sudo apt install -y build-essential
```

**Installer node**

L'installation de Node.js via les instructions données sur le site nodejs.org ne configure pas les permissions correctes pour moi. Donc, lorsque j'essaie d'installer quelque chose avec `npm install`, j'obtiens des erreurs. J'ai [découvert](https://github.com/Microsoft/WSL/issues/776#issuecomment-266112578) que l'utilisation de `n` aide :

**Installer node avec `n`**

Comme c'est une nouvelle installation, nous pouvons utiliser [n-install](https://github.com/mklement0/n-install) avec :

```
curl -L https://git.io/n-install | bash
```

Cela installera la dernière version stable de node ?

Une fois le script terminé, redémarrez bash avec :

```
. /home/my_user_name/.bashrc # affiche cela pour que vous puissiez copier-coller
```

Vérifiez vos versions de node et npm :

```
node -v && npm -v
```

**Installer fish ?**

Fish est maintenant mon shell de prédilection purement pour la complétion automatique/intellisense ? il y a aussi quelques jolis thèmes que vous pouvez obtenir pour lui aussi.

![Image](https://cdn-media-1.freecodecamp.org/images/sT61-l2VWUosXNsabUdkBCH2ZJQm6COn6LEy)
_La génialité de fish ?_

```
sudo apt -y install fishsudo apt -y upgrade && sudo apt -y autoremove
```

**Installer Oh My Fish | OMF**

Oh My Fish est comme un gestionnaire de paquets pour Fish permettant l'installation de paquets et de thèmes.

```
curl -L https://get.oh-my.fish | fish
```

**Installer le thème OMF**

```
omf install clearance
```

**Le début du commencement**

Ok, donc c'est une configuration de base pour WSL. Vous voudrez probablement configurer Git maintenant. J'utilise SSH plutôt que HTTPS depuis un certain temps maintenant sur WSL.

**Note :** Au moment de la rédaction de cet article, l'intégration de WSL Git avec VSCode ne fonctionne pas, donc j'ai ajouté une installation de Git à ma machine Windows. Vous pouvez omettre cela et utiliser Git uniquement via le terminal, mais j'aime vraiment l'intégration de VSCode Git.

Pour configurer SSH sur votre machine, consultez ce [guide pratique de configuration SSH](https://github.com/spences10/cheat-sheets/blob/master/git.md#how-to-authenticate-with-github-using-ssh). Je dis SSH au lieu de HTTPS parce que j'ai eu toutes sortes de problèmes avec le gestionnaire d'informations d'identification Git et le gestionnaire de trousseau. À la fin, il était en fait plus rapide de créer une clé SSH et de s'authentifier avec GitHub. Le guide que j'ai lié vous guide à travers cela.

**Déplacer vos dotfiles**

Si vous avez tous vos [dotfiles](https://github.com/spences10/dotfiles) sauvegardés dans un dépôt GitHub, c'est maintenant le bon moment pour les ajouter à votre dossier WSL. Les dernières fois que j'ai fait cela, j'ai défini manuellement les permissions après avoir déplacé chacun des fichiers, mais j'ai depuis découvert `[rsync](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)` pour déplacer tous les fichiers.

```
rsync -avzh /mnt/c/Users/dotfiles/ ~/
```

Cela copiera le contenu de mon dossier `dotfiles` dans le répertoire `~/` (home) dans WSL, vous pouvez les vérifier avec :

```
ls -la ~/
```

![Image](https://cdn-media-1.freecodecamp.org/images/Uq3kAxUEXpizEGd-h7ajRZMLBBZVvlrg5t8B)

J'ai copié mon `.gitconfig`, `.gitignore` et `.npmrc` dotfiles représentés ici et vous pouvez voir que les permissions ne sont pas cohérentes avec le fichier `.bashrc`.

Changez les permissions des fichiers avec `chmod` et pour obtenir les attributs d'un fichier similaire, utilisez `stat` :

```
stat -c "%a %n" ~/.*
```

Cela listera tout ce qui commence par un `.` voici le mien :

```
777 /home/scott/.755 /home/scott/..600 /home/scott/.bash_history644 /home/scott/.bash_logout644 /home/scott/.bashrc777 /home/scott/.cache777 /home/scott/.config777 /home/scott/.gitconfig777 /home/scott/.gitignore777 /home/scott/.local777 /home/scott/.npm777 /home/scott/.npmrc644 /home/scott/.profile644 /home/scott/.sudo_as_admin_successful
```

Je ne veux changer que `.gitconfig`, `.gitignore` et `.npmrc` ici, donc je vais faire ceci :

```
chmod 644 .gitconfig .gitignore .npmrc
```

Et maintenant mes fichiers ressemblent à ceci. ?

![Image](https://cdn-media-1.freecodecamp.org/images/JbMu-0tz5J581tQ3FwIjYADBvuWyqXC-xMof)

Ok, maintenant nous sommes opérationnels avec une installation Ubuntu mise à jour, node et le terminal fish. Bien sûr, il reste encore à installer tous vos paquets npm globaux que vous voulez pour le développement maintenant.

Bonne chance !

### Merci d'avoir lu

Si vous avez trouvé cela intéressant, laissez un ou deux applaudissements, abonnez-vous pour les futures mises à jour ou tweetez-moi vos pensées.

Si j'ai manqué quelque chose, ou si vous avez une meilleure façon de faire quelque chose, faites-le moi savoir.

Retrouvez-moi sur [Twitter](https://twitter.com/ScottDevTweets) ou [Ask Me Anything](https://github.com/spences10/ama) sur GitHub.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).**