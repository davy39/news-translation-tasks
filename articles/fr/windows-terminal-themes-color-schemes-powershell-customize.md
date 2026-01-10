---
title: Thèmes PowerShell et schémas de couleurs du Terminal Windows – Comment personnaliser
  votre ligne de commande
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2021-03-06T01:39:57.000Z'
originalURL: https://freecodecamp.org/news/windows-terminal-themes-color-schemes-powershell-customize
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/header-1.png
tags:
- name: Powershell
  slug: powershell
- name: Windows
  slug: windows
seo_title: Thèmes PowerShell et schémas de couleurs du Terminal Windows – Comment
  personnaliser votre ligne de commande
seo_desc: "I recently set up and configured Windows Terminal for my local development\
  \ environment. In this article, I will walk you through the steps to configure your\
  \ own Terminal.  \nIf you have not done so already, you can download Windows Terminal\
  \ from the M..."
---

J'ai récemment configuré et installé Windows Terminal pour mon environnement de développement local. Dans cet article, je vais vous guider à travers les étapes pour configurer votre propre Terminal.  
  
Si vous ne l'avez pas encore fait, vous pouvez télécharger Windows Terminal [depuis le Microsoft Store](https://aka.ms/terminal) si vous êtes sous Windows 10. Windows Terminal n'est pas disponible sur les versions antérieures de Windows.

## Comment configurer vos sélections PowerShell

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-32.png)
_Image démontrant la fonctionnalité multi-onglets offerte par Windows Terminal_

L'un des plus grands avantages de Windows Terminal est la possibilité d'utiliser plusieurs shells dans le même écran, en basculant entre les onglets pour accéder à différents shells.

Une fois que vous avez installé l'application, ouvrez le terminal et sélectionnez le symbole `v` en haut (à côté de l'onglet ouvert). Vous devriez voir une liste des terminaux disponibles, mais nous allons les ignorer pour l'instant.

Dans le menu déroulant, sélectionnez l'option "Paramètres" et le fichier `settings.json` devrait s'ouvrir dans votre éditeur de texte par défaut.

Il y a plusieurs propriétés ici. La première que vous devrez examiner est la propriété `profiles`. La propriété `profiles` contient toutes vos options de sélection de terminal - la propriété imbriquée `defaults` contient les paramètres par défaut pour **tous** les profils, et la propriété `list` contient vos profils de terminal.

Nous allons nous concentrer sur la propriété `list`, qui devrait actuellement contenir des valeurs similaires à ceci :

```json
    [
        {
            "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
            "name": "Windows PowerShell",
            "commandline": "powershell.exe",
            "hidden": false
        },
        {
            "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
            "name": "cmd",
            "commandline": "cmd.exe",
            "hidden": false
        }
    ],
```

La propriété `list` est un tableau d'objets et détermine quels exécutables de terminal peuvent être chargés via Windows Terminal. Dans cet exemple, les options disponibles sont Windows PowerShell et l'invite de commande CMD.

Voici une explication des propriétés de ces objets :

* `guid` : Il s'agit d'un **I**dentifiant **U**nique **G**lobal et est utilisé exclusivement pour le paramètre `defaultProfile` (que nous aborderons plus tard).
* `name` : Il s'agit du nom qui s'affiche dans le menu déroulant lorsque vous ouvrez un nouvel onglet dans le Terminal Windows.
* `commandline` : Il s'agit de l'exécutable qui se charge lorsque vous ouvrez un onglet avec ce profil.
* `hidden` : Cette option est un booléen et détermine si le profil apparaît dans le menu déroulant du nouvel onglet. Si vous n'utilisez pas souvent un terminal, définissez cette option sur `true` pour l'empêcher de s'afficher dans le menu déroulant. Cela vous permet de conserver les paramètres du profil tout en gardant votre liste déroulante limitée aux terminaux dont vous avez besoin.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-29.png)
_Image représentant le menu déroulant, montrant deux terminaux activés : Ubuntu-20.04 et Git Bash_

## Exemple de configuration personnalisée du terminal Windows PowerShell

Ces options par défaut peuvent être tout ce dont vous avez besoin, selon votre environnement de développement. Je fais la plupart de mon travail dans Windows Subsystems for Linux (WSL 2) et j'utilise occasionnellement Git Bash, donc j'ai quelques options supplémentaires.

```json
      {
        "guid": "{07b52e3e-de2c-5db4-bd2d-ba144ed6c273}",
        "hidden": false,
        "name": "Ubuntu-20.04",
        "source": "Windows.Terminal.Wsl",
        "startingDirectory": "//wsl$/Ubuntu-20.04/home/nhcarrigan",
      },
      {
        "guid": "{00000000-0000-0000-ba54-000000000002}",
        "commandline": "%PROGRAMFILES%/git/usr/bin/bash.exe -i -l",
        "icon": "%PROGRAMFILES%/Git/mingw64/share/git/git-for-windows.ico",
        "name": "Git Bash",
        "startingDirectory": "%USERPROFILE%",
      },
```

Vous pourriez voir quelques nouvelles propriétés ici.

* `source` : Cette propriété est générée automatiquement lorsque Windows Terminal détecte et génère un profil pour un nouvel exécutable de terminal. Vous ne devez pas l'ajouter lorsque vous construisez manuellement un profil.
* `icon` : Cette propriété est utilisée pour sélectionner quel fichier d'icône `.ico` est utilisé à côté du nom dans le menu déroulant du nouvel onglet.
* `startingDirectory` : Il s'agit du chemin de fichier vers lequel Windows Terminal pointera lorsque vous chargerez un nouvel onglet avec ce profil.

## Comment construire un profil personnalisé dans PowerShell

Les paramètres de profil pour Git Bash n'ont pas été générés automatiquement par Windows Terminal, et j'ai dû les construire manuellement. Si vous devez faire de même, voici comment procéder.

Tout d'abord, vous devrez générer une valeur `guid`. Celles-ci prennent le format `{00000000-0000-0000-0000-000000000000}`. Vous pouvez en générer une dans Windows PowerShell en exécutant `[guid]::NewGuid()`, ou dans WSL en exécutant `uuidgen`.

Ensuite, définissez le chemin vers l'exécutable dans la propriété `commandline`. La valeur `%PROGRAMFILES%` pointe vers votre répertoire "Program Files" et tiendra compte de la différence entre le chemin pour les applications 32 bits et 64 bits.

Si votre installation se trouve dans votre répertoire utilisateur, vous pouvez utiliser la valeur `%USERPROFILE%`. Les drapeaux `-i -l` sont utilisés pour garantir que Windows Terminal chargera correctement votre fichier `.bashrc`.

La propriété `icon` peut être omise, mais si vous souhaitez que l'icône apparaisse à côté du nom du terminal, vous devrez ajouter le chemin de fichier vers ce fichier d'icône ici.

La propriété `name` est requise et détermine le nom d'affichage dans le sélecteur déroulant. Ici, j'utilise "Git Bash", afin de savoir quel terminal cette option ouvre.

Enfin, `startingDirectory` doit être défini sur l'emplacement du chemin de fichier par défaut que vous souhaitez que le terminal cible lorsqu'il s'ouvre. J'ai défini le mien sur `%USERPROFILE%`, qui pointe le terminal vers mon répertoire utilisateur Windows au chargement. De cette façon, je peux accéder rapidement à mon dossier "documents" ou à d'autres dossiers.

## Comment définir votre profil par défaut dans PowerShell Windows Terminal

Maintenant, si vous faites défiler jusqu'en haut de votre fichier `settings.json`, vous devriez voir une propriété `defaultProfile`. Cette option accepte une valeur `guid`, qui doit correspondre à l'une des valeurs `guid` dans votre tableau `list`. Windows Terminal chargera un onglet avec ce profil lorsque vous le démarrerez.

Dans mon cas, la majorité de mon travail est effectuée dans WSL, donc j'ai défini mon `defaultProfile` sur ce `guid` :

```json
  "defaultProfile": "{07b52e3e-de2c-5db4-bd2d-ba144ed6c273}",
```

Maintenant, lorsque j'ouvre mon application Windows Terminal, une instance WSL est lancée.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-18.png)
_Capture d'écran montrant une instance de Windows Terminal, avec un seul onglet intitulé "Ubuntu-20.04". "nhcarrigan @ DESKTOP-049HSUK ~" est affiché dans l'écran du terminal._

## Comment concevoir votre schéma de couleurs dans PowerShell Windows Terminal

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-30.png)

Maintenant que vous avez configuré vos applications de terminal, nous pouvons nous concentrer sur le style du texte pour le rendre joli.

Sous votre propriété `profiles` dans le `settings.json`, vous devriez voir une propriété `schemes`. `schemes` contient un tableau d'objets de schéma de couleurs, qui ressemblent à ceci :

```json
{
    "name" : "Campbell",

    "cursorColor": "#FFFFFF",
    "selectionBackground": "#FFFFFF",

    "background" : "#0C0C0C",
    "foreground" : "#CCCCCC",

    "black" : "#0C0C0C",
    "blue" : "#0037DA",
    "cyan" : "#3A96DD",
    "green" : "#13A10E",
    "purple" : "#881798",
    "red" : "#C50F1F",
    "white" : "#CCCCCC",
    "yellow" : "#C19C00",
    "brightBlack" : "#767676",
    "brightBlue" : "#3B78FF",
    "brightCyan" : "#61D6D6",
    "brightGreen" : "#16C60C",
    "brightPurple" : "#B4009E",
    "brightRed" : "#E74856",
    "brightWhite" : "#F2F2F2",
    "brightYellow" : "#F9F1A5"
},
```

Si vous avez utilisé des outils comme le package `chalk` sur `npm`, vous pouvez reconnaître certaines de ces valeurs de couleur (`purple` ici est `magenta` dans chalk). Les autres clés font ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-34.png)
_Image montrant les couleurs résultantes du thème par défaut ci-dessus._

* `name` : Cela est utilisé pour lier le schéma de couleurs à l'un des profils que nous avons créés précédemment.
* `cursorColor` : Cela détermine la couleur de votre curseur de texte.
* `selectionBackground` : Cela détermine la couleur de fond du texte mis en surbrillance.
* `background` : Cela détermine la couleur de fond de votre terminal.
* `foreground` : Cela détermine la couleur de premier plan de votre terminal. Avec ma configuration actuelle, je n'ai pas vu de différence notable en modifiant cette valeur.

Les propriétés de couleur déterminent comment chaque valeur de couleur envoyée par une commande de terminal (comme `console.log`) est affichée.

Les paramètres que j'utilise pour mon profil de couleur sont :

```json
    {
      "name": "Duotone Dark",
      "black": "#1f1d27",
      "red": "#d9393e",
      "green": "#2dcd73",
      "yellow": "#d9b76e",
      "blue": "#2488ff",
      "purple": "#de8d40",
      "cyan": "#6ad7d9",
      "white": "#b7a1ff",
      "brightBlack": "#353147",
      "brightRed": "#d9393e",
      "brightGreen": "#2dcd73",
      "brightYellow": "#d9b76e",
      "brightBlue": "#2488ff",
      "brightPurple": "#de8d40",
      "brightCyan": "#6ad7d9",
      "brightWhite": "#dfd1ed",
      "background": "#1f1d27",
      "foreground": "#b7a1ff"
    },
```

Je vous encourage à jouer avec ces valeurs jusqu'à ce que vous trouviez un ensemble de couleurs qui correspond à vos préférences.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-20.png)
_Image montrant les couleurs résultantes de mes paramètres de thème._

### Comment lier votre schéma de couleurs à un profil

Maintenant que vous avez défini vos paramètres de couleur, vous devez lier ces paramètres à un profil de terminal. Vous pourriez appliquer les paramètres à l'objet `defaults` dans la propriété `profiles`, ce qui les appliquera à tous vos terminaux. Je préfère configurer différents paramètres de couleur pour différents terminaux, afin de pouvoir identifier rapidement quand je suis dans la bonne fenêtre.

Appliquons cela à notre profil WSL. Ajoutez une clé `colorScheme` à votre objet de profil, et donnez-lui une valeur qui correspond au `name` de votre schéma. Vous devriez maintenant avoir quelque chose comme ceci :

```json
      {
        "guid": "{07b52e3e-de2c-5db4-bd2d-ba144ed6c273}",
        "hidden": false,
        "name": "Ubuntu-20.04",
        "source": "Windows.Terminal.Wsl",
        "startingDirectory": "//wsl$/Ubuntu-20.04/home/nhcarrigan",
        "colorScheme": "Duotone Dark",
      }
```

Si vous rechargez votre Windows Terminal, vous devriez voir vos nouvelles couleurs prendre effet.

### Comment configurer des paramètres d'apparence supplémentaires

Mon objet de profil WSL complet a quelques paramètres supplémentaires :

```json
      {
        "guid": "{07b52e3e-de2c-5db4-bd2d-ba144ed6c273}",
        "hidden": false,
        "name": "Ubuntu-20.04",
        "source": "Windows.Terminal.Wsl",
        "startingDirectory": "//wsl$/Ubuntu-20.04/home/nhcarrigan",
        "colorScheme": "Duotone Dark",
        "useAcrylic": true,
        "acrylicOpacity": 0.5,
        "fontFace": "PxPlus IBM VGA8",
        "fontSize": 16,
        "experimental.retroTerminalEffect": true
      },
```

Vous pouvez ajuster ces paramètres selon vos préférences.

* `useAcrylic` activera l'effet de transparence de Windows 10 sur le fond du terminal.
* Si l'effet de transparence est activé, `acrylicOpacity` déterminera la force de l'effet de transparence. Plus le nombre est bas, plus la transparence est élevée.
* `fontFace` sélectionnera la police utilisée pour le terminal. Notez que vous devez avoir la police installée sur votre ordinateur. J'utilise la police [PxPlus IBM VGA8](https://github.com/pocketfood/Fontpkg-PxPlus_IBM_VGA8), et j'ai téléchargé le fichier `.ttf` que Windows peut installer.
* `fontSize` déterminera la taille de la police (en `pt`).
* L'`experimental.retroTerminalEffect` est mon paramètre préféré. Cela simule des "lignes de balayage" sur votre terminal, comme les anciens moniteurs CRT.

Voici à quoi ressemble ma configuration finale :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-21.png)
_Image montrant le résultat final des paramètres de thème._

Tous ces paramètres d'apparence peuvent être passés dans l'option `defaultSettings` pour les appliquer à tous vos profils globalement.

```json
    "defaultSettings":
    {
        "useAcrylic": true,
        "acrylicOpacity": 0.1,
        "fontFace": "Cascadia Code",
        "fontSize": 10
    },
```

## Comment configurer des paramètres supplémentaires dans PowerShell Windows Terminal

Il y a quelques paramètres supplémentaires qui valent la peine d'être considérés.

Après la propriété `schemes`, vous devriez voir une propriété `actions`. Celle-ci contient un tableau de paramètres de raccourcis clavier.

Par défaut, Windows Terminal attribue les commandes de copie et de collage à `Ctrl+Shift+C` et `Ctrl+Shift+V` respectivement. Vous pouvez les lier aux `Ctrl+C` et `Ctrl+V` par défaut avec ces paramètres :

```json
    { "command": { "action": "copy", "singleLine": false }, "keys": "ctrl+c" },
    { "command": "paste", "keys": "ctrl+v" },
```

L'option `singleLine` définie sur `false` préserve les sauts de ligne dans le texte copié.

Probablement près du haut de votre fichier `settings.json`, il y a deux propriétés qui affectent également le comportement de la copie de texte depuis votre terminal :

* `copyOnSelect` est par défaut `false`. Lorsque défini sur true, la mise en surbrillance de texte dans le terminal avec votre souris le copiera dans votre presse-papiers.
* `copyFormatting` est par défaut `false`. Lorsque défini sur true, la mise en forme du texte sera également copiée (sinon, le contenu est copié en texte brut).

Copier du texte depuis votre terminal est généralement sûr, mais _coller_ du texte dans votre terminal [peut être dangereux](https://www.nhcarrigan.com/dont-paste-to-terminal/). Windows Terminal est livré avec quelques protections pour aider à éviter les risques :

* `largePasteWarning` est par défaut `true` et peut ne pas être présent dans votre fichier `settings.json`. Ce paramètre déclenche une boîte de dialogue lorsque vous tentez de coller plus de 5 Ko de contenu.
* `multiLinePasteWarning` est par défaut true et peut ne pas être présent dans votre fichier `settings.json`. Ce paramètre déclenche une boîte de dialogue lorsque vous tentez de coller du contenu textuel qui contient des sauts de ligne (une tactique courante pour les attaques de détournement de presse-papiers est de forcer l'exécution de commandes au collage avec des caractères de nouvelle ligne).

Je vous recommande fortement de laisser ces protections en place.

## Ressources supplémentaires

Félicitations ! Vous avez maintenant configuré et installé votre propre configuration de Windows Terminal. 

Pour des options de personnalisation supplémentaires que vous n'avez pas lues dans cet article, visitez la [Documentation de personnalisation de Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/startup).

Pour une large sélection de schémas de couleurs, disponibles sous forme de fichiers JSON téléchargeables, consultez [Windows Terminal Themes](https://windowsterminalthemes.dev/). C'est là que j'ai obtenu mes paramètres, que j'ai un peu ajustés à mon goût personnel.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-28.png)
_L'image qui a tout déclenché - une capture d'écran de démonstration de mon [outil d'envoi d'e-mails](https://www.freecodecamp.org/news/send-email-newsletter-with-the-sendgrid-api/)._

Bon codage.