---
title: Comment exécuter des applications Linux sur Windows 10 et 11 en utilisant WSL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-16T17:33:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-linux-apps-on-windows-10-11-using-wsl
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/photo_2021-12-16_19-57-32.jpg
tags:
- name: Linux
  slug: linux
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
- name: WSL
  slug: wsl
seo_title: Comment exécuter des applications Linux sur Windows 10 et 11 en utilisant
  WSL
seo_desc: 'By Yosra Emad

  I''ve been using Windows Subsystem for Linux (WSL) for my OS class for quite a while
  now. And I love how I can use Linux commands in Windows in a straightforward way
  without the added complexity of installing a virtual machine or dual bo...'
---

Par Yosra Emad

J'utilise le sous-système Windows pour Linux (WSL) pour mon cours de systèmes d'exploitation depuis un certain temps maintenant. Et j'adore la façon dont je peux utiliser les commandes Linux dans Windows de manière simple, sans la complexité supplémentaire de l'installation d'une machine virtuelle ou du dual boot. 

À la fin de cet article, vous devriez être en mesure d'exécuter des commandes Linux directement depuis Windows comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled.png)
_exemple de commandes linux sur windows_

# Prérequis

Pour que WSL fonctionne efficacement, je vous suggère de passer à Windows 11. WSL est également disponible sur Windows 10, mais il est bien plus efficace sur Windows 11 selon mon expérience. 

Pour Windows 10, vous aurez besoin de la build 21364 ou supérieure.

Cet article couvrira ce que vous pouvez faire sur Windows 10 et 11.

# Comment installer WSL

La commande pour exécuter WSL est simple :

```powershell
wsl --install

```

Cela téléchargera le noyau Linux, définira WSL 2 comme version par défaut et installera Ubuntu comme distribution par défaut.

Vous ne voulez pas Ubuntu ? Voici la commande pour vous :

```powershell
wsl --install -d <nom de la distribution>

```

Voici les distributions disponibles à ce jour :

* Ubuntu
* OpenSUSE Leap 42
* SUSE Linux Enterprise Server 12 (SLES)
* Kali Linux
* Debian GNU/Linux

Après cela, vous trouverez une application appelée Ubuntu (ou toute autre distribution) dans votre menu démarrer :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled-1.png)

# Ouvrir le terminal Linux

Ouvrez l'application Ubuntu que vous venez d'installer, et vous serez accueilli par un terminal Linux ! Essayez d'exécuter quelques commandes :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled-2.png)

# Que faire si je veux accéder à mes fichiers Windows ?

Si vous allez dans votre explorateur de fichiers (touche Windows + E), vous trouverez une nouvelle option Linux à gauche où se trouvent tous vos fichiers Linux. C'est là que seront situés les fichiers que vous créez dans le terminal :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled-3.png)

Mais que faire si vous voulez accéder à vos fichiers habituels ?

Heureusement, vous pouvez le faire facilement. Exécutez simplement la commande suivante dans votre terminal Linux :

```bash
cd /mnt/

```

Si vous exécutez `ls` ici, vous trouverez les lecteurs de votre ordinateur. De cette façon, vous pourrez vous déplacer dans vos fichiers avec `cd`.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled-4-1.png)

# Comment créer des alias dans WSL2

Avez-vous déjà une longue commande à taper et souhaitez qu'il existe un raccourci pour celle-ci ? Alors, les alias sont vos amis.

Il existe deux façons de créer des alias :

* par session
* de manière permanente

## Comment créer des alias par session dans WSL2

Pour créer un alias dans votre session actuelle de Linux (l'alias sera oublié une fois que vous fermerez le terminal), vous devez exécuter la commande suivante :

```bash
alias <nom de l'alias>='<commande>'

```

par exemple :

```bash
alias runc='gcc main.c -o main'

```

## Comment créer des alias permanents dans WSL2

Nous allons éditer un fichier appelé `.bash_aliases` pour sauvegarder nos alias.

Exécutez les commandes suivantes :

```bash
cd ~
ls -a

```

Parcourez la liste des fichiers qui sont imprimés et cherchez `.bash_aliases`.

Si vous ne le trouvez pas, exécutez la commande suivante :

```bash
touch .bash_aliases

```

Maintenant, pour éditer le fichier, exécutez cette commande :

```bash
vi .bash_aliases

```

Vous serez accueilli par un écran comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled-5.png)

* Appuyez sur "i" pour commencer à taper, et ajoutez autant d'alias que vous le souhaitez.

Par exemple :

```bash
alias runc='gcc main.c -o main'
alias hello='echo hello'

```

* Pour quitter le mode de frappe, appuyez sur "ctrl + c".
* Pour quitter Vim et sauvegarder les fichiers, tapez ":wq!" (Je suis fier de ne pas avoir eu à googler cela.)

Maintenant, vous êtes prêt ! Redémarrez Ubuntu et commencez à taper l'un des alias ci-dessus et cela devrait fonctionner parfaitement :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled-6.png)

# Comment exécuter des applications GUI

D'accord, maintenant nous savons comment exécuter des applications en ligne de commande depuis WSL2. Mais que faire si nous voulons exécuter des applications GUI Linux ? La réponse est simple – vous devez simplement installer l'application GUI avant de l'exécuter. Je vais utiliser Firefox comme exemple.

Pour installer Firefox :

```bash
sudo apt install firefox

```

Pour exécuter Firefox :

```bash
firefox

```

![Untitled](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot--531-.png)

Si vous avez déjà Firefox sur votre machine Windows, vous remarquerez qu'il n'est pas ouvert. C'est parce que vous exécutez maintenant Firefox pour Linux et non pour Windows.

Vous pouvez même exécuter Firefox pour Linux directement depuis le menu démarrer si vous utilisez Windows 11. Vous le trouverez sous le dossier de votre distribution.

![Untitled](https://www.freecodecamp.org/news/content/images/2021/12/Untitled-7.png)

# Conclusion

Cet article a couvert comment exécuter WSL 2 efficacement. Si vous avez des questions, n'hésitez pas à me contacter sur l'une de mes [plateformes de médias sociaux](https://yosracodes.bio.link/)