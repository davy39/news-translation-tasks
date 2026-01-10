---
title: Comment configurer Windows pour le développement Node.js avec NVM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-18T20:56:58.000Z'
originalURL: https://freecodecamp.org/news/set-up-windows-for-nodejs-development-with-nvm
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-tal-haim-4481881.jpg
tags:
- name: node
  slug: node
- name: node js
  slug: node-js
- name: Windows
  slug: windows
seo_title: Comment configurer Windows pour le développement Node.js avec NVM
seo_desc: "By Otavio Ehrenberger\nSo you want to develop using the JavaScript run-everywhere\
  \ platform on the same computer where you game, edit videos, code C# desktop apps,\
  \ or whatever. \nYou are also aware that there are multiple Node.js versions in\
  \ active deve..."
---

Par Otavio Ehrenberger

Vous souhaitez donc développer en utilisant la plateforme JavaScript qui fonctionne partout, sur le même ordinateur où vous jouez, éditez des vidéos, codez des applications de bureau en C# ou autre chose. 

Vous êtes également conscient qu'il existe plusieurs versions de Node.js en développement actif et qu'il est assez courant de trouver des projets qui ne fonctionnent que dans quelques-unes d'entre elles. 

Alors ce guide est fait pour vous. Configurons donc une machine Windows pour Node.js avec une gestion de plusieurs versions, tout en abordant les pièges courants.

## Comment installer Windows Terminal

Si vous utilisez Windows 11, bonne nouvelle : vous avez déjà Windows Terminal installé. Sinon, ouvrez le Microsoft Store et téléchargez-le gratuitement.

![Microsoft Store](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fnsj5h97qeq8grhtriqk.png)

Il s'agit d'un terminal à onglets accéléré par le matériel à partir duquel vous pouvez exécuter Powershell, CMD ou des interfaces WSL. Et c'est une étape importante (et, certains diraient, assez tardive) vers la simplification de l'expérience de développement sous Windows, similaire à celle des autres grands systèmes d'exploitation. 

L'installation de ce terminal est fortement recommandée si vous prévoyez de développer sous Windows, en utilisant Node.js ou autre chose.

## Comment installer NVM pour Windows

Maintenant, au lieu d'installer Node.js depuis le site officiel, nous devons installer le Node Version Manager et télécharger les versions de Node à partir de là. 

Si vous avez déjà Node installé, cela ne devrait pas poser de problème majeur car NVM écrasera toutes les variables d'environnement et les liens symboliques liés à Node. Cependant, je vous recommande de le désinstaller quand même, car ce processus rendra l'installation actuelle complètement inutile.

Rendez-vous sur la page du projet [NVM pour Windows](https://github.com/coreybutler/nvm-windows) et téléchargez la dernière version disponible de `nvm-setup.zip` depuis la page des [releases](https://github.com/coreybutler/nvm-windows/releases).

Notez que ce n'est pas le même projet que le [NVM](https://github.com/nvm-sh/nvm) basé sur UNIX, bien qu'il soit fonctionnellement équivalent. "Similaire, mais pas identique" comme le projet lui-même le précise.

Décompressez le contenu du dossier et exécutez `nvm-setup.exe`. Vous serez invité à accepter les conditions d'utilisation du projet (actuellement la licence MIT), puis l'installateur vous demandera où installer NVM. Ce sera également le même emplacement que les versions de Node téléchargées et leurs packages activés globalement. Le dossier de données d'application roaming sous votre utilisateur actuel devrait être parfaitement adapté.

Cependant, vous serez ensuite invité à indiquer où conserver le lien symbolique de Node.js, et (au moins dans les versions jusqu'à 1.1.8) il y a un piège : _vous ne pouvez pas conserver le lien symbolique sous un chemin contenant des espaces_, et malheureusement, le chemin d'installation par défaut (actuellement `C:\Program Files\nodejs`) tombe exactement dans ce piège.

![Chemin du lien symbolique NVM](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ng7dyyu59rm0zwoupf7z.png)

C'est là que j'ai installé mon NVM local. Ce n'est qu'une suggestion et vous pouvez installer où vous le souhaitez (tant que le chemin ne contient pas d'espaces). Je recommande simplement de donner au dossier cible un nom comme `\nodejs` pour ne pas perdre l'installation, qui peut être supprimée directement depuis le désinstallateur standard de toute façon.

## Comment installer Node et configurer NVM

Tout d'abord, vous devez exécuter Windows Terminal avec des privilèges administratifs. Une façon de le faire est de rechercher le terminal dans la recherche interne du système, de cliquer avec le bouton droit sur son icône, puis de sélectionner 'Exécuter en tant qu'administrateur'.

![Exécution de Windows Terminal en tant qu'administrateur](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m2gsgaduqa8fyn9uujep.png)

À tout moment où vous vous sentez perdu en manipulant NVM, tapez simplement `nvm` dans le terminal et un manuel très concis apparaîtra, expliquant chaque commande disponible et leurs paramètres.

![Manuel NVM](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ecc68wrbgdal06f7eqvz.png)

Assurons-nous que NVM est activé. Exécutez simplement :

```powershell
nvm on

```

Et après cela, installons la version actuelle de support à long terme, pré-aliasée comme `lts` (actuellement 14.18.1) :

```powershell
nvm install lts

```

Après la fin de l'installation, nous devons indiquer à NVM quelle version nous souhaitons utiliser :

```powershell
nvm use 14.18.1

```

Super ! Maintenant, les commandes spécifiques à Node.js telles que `node` et `npm` seront mappées à cette version de Node. Célébrons en installant le gestionnaire de packages yarn :

```powershell
npm install -g yarn

```

Après la fin de l'installation, vérifions si tout s'est bien passé :

```powershell
yarn -v

```

Si vous obtenez la version de yarn comme sortie, félicitations ! La configuration a été correctement effectuée.

## Comment gérer plusieurs versions de NodeJS

Maintenant que nous avons la version LTS, à quoi bon avoir un gestionnaire de versions si ce n'est pour utiliser différentes versions ? Installons également la version la plus récente de Node, pré-aliasée comme `latest` (actuellement 16.11.1) :

```powershell
nvm install latest

```

À tout moment, si vous souhaitez vérifier vos versions installées localement, exécutez

```powershell
nvm list

```

pour obtenir une liste de celles disponibles dans votre système. Pour changer votre version actuelle, exécutez simplement `nvm use` à nouveau, cette fois en pointant vers la nouvelle version installée :

```powershell
nvm use 16.11.1

```

Notez que si vous exécutez `yarn -v` à nouveau, vous ne recevrez pas de numéro de version car yarn n'est pas actuellement installé pour votre version locale 16.11.1. _Chaque version installée est complètement autonome, ce qui inclut l'accès aux packages globaux._

Félicitations, vous êtes maintenant un développeur Node.js organisé sous Windows qui suit les meilleures pratiques de gestion de versions localisées.

## Comment résoudre les problèmes courants

### Mes téléchargements via npm/yarn sont VRAIMENT lents.

Tout d'abord, assurez-vous que le réseau auquel vous êtes connecté est classé comme 'privé' par Windows, car le pare-feu Windows peut être très sélectif sur les réseaux publics. 

Si le problème persiste, ajoutez le répertoire nvm à la liste blanche (il devrait être `C:\Users\<votre_nom_d_utilisateur>\AppData\Roaming\nvm` si vous avez gardé les paramètres par défaut) dans votre logiciel antivirus.

### L'exécution de tâches dans Node (par exemple, la transpilation d'un projet TypeScript) est VRAIMENT lente.

Windows utilise le système de fichiers NTFS qui est particulièrement mauvais pour gérer les tâches impliquant un très grand nombre de petits fichiers. Et les projets Node sont notoires pour les nombreux modules différents qui dépendent de nombreux autres modules différents, donc ce problème est plus difficile à atténuer. 

À moins d'obtenir un SSD, votre meilleur choix serait de configurer Node sur le [Sous-système Windows pour Linux](https://docs.microsoft.com/en-us/windows/wsl/about) si la vitesse d'exécution est trop lente pour être utilisable.

### Je reçois un code de sortie 145 dans certaines commandes NVM.

Jetez un œil à la partie _Installer NVM pour Windows_ de ce tutoriel, en particulier celle concernant l'emplacement du lien symbolique. 

Vous devez avoir installé NVM dans un chemin de répertoire contenant des espaces. Désinstallez donc NVM et relancez `nvm-setup.exe`, en veillant cette fois à ce qu'aucun des chemins sélectionnés ne contienne d'espaces.

## Conclusion

Si vous pouvez installer des versions à partir de la ligne de commande et basculer entre elles (n'oubliez pas que vous aurez besoin de privilèges administratifs pour basculer entre les versions), alors tout le reste dépend de vous en tant que développeur JavaScript (ou TypeScript). 

Si vous devez installer un éditeur de code, je recommande Visual Studio Code pour sa commodité, Sublime Text 3 comme alternative légère à VSCode, ou [vim](https://www.freecodecamp.org/news/vim-windows-install-powershell/) si vous avez le temps et l'envie d'apprendre une nouvelle compétence.