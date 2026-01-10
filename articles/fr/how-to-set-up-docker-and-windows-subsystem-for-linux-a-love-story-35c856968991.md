---
title: 'Comment configurer Docker et le sous-système Windows pour Linux : une histoire
  d''amour. ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T17:13:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-docker-and-windows-subsystem-for-linux-a-love-story-35c856968991
coverImage: https://cdn-media-1.freecodecamp.org/images/0*nKPs7NaTWQnJpNSU
tags:
- name: Docker
  slug: docker
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Comment configurer Docker et le sous-système Windows pour Linux : une
  histoire d''amour. ?'
seo_desc: 'By Piotr Gaczkowski

  Do you sometimes feel you’re a beautiful princess turned by an evil wizard into
  a frog? Like you don’t belong? I do. I’m a UNIX guy scared to leave the cozy command
  line. My terminal is my castle. But there are times when I’m forc...'
---

Par Piotr Gaczkowski

Vous arrive-t-il parfois de vous sentir comme une belle princesse transformée par un méchant sorcier en grenouille ? Comme si vous n'étiez pas à votre place ? Moi, oui. Je suis un passionné de UNIX qui a peur de quitter la ligne de commande confortable. Mon terminal est mon château. Mais il arrive que je sois obligé d'utiliser Microsoft Windows et j'ai appris quelques astuces pour m'en sortir.

Pour mes besoins quotidiens en terminal, j'ai installé le sous-système Windows pour Linux avec la distribution Ubuntu. En plus de cela, j'ai une installation de Linuxbrew qui m'aide à gérer toutes les applications tierces dont je pourrais avoir besoin. Cette combinaison fonctionne surprenamment bien ! J'ai un lien symbolique pratique pour accéder à toutes mes données "externes" (c'est-à-dire hébergées par Windows) : `ln -s ~/external /mnt/c/Users/DoomHammer` et la plupart des besoins sont satisfaits de cette manière. C'est-à-dire, sauf si j'ai besoin d'utiliser Docker.

### Qu'est-ce qui rend Docker si spécial ?

Contrairement à la plupart des applications que j'utilise habituellement tous les jours, Docker est une application système. Cela signifie qu'elle est profondément enracinée dans le système et nécessite un démon réel pour fonctionner sur la machine hôte. Et par machine hôte, je veux dire Microsoft Windows natif dans ce cas.

Cela signifie-t-il que vous ne pouvez pas utiliser Docker depuis WSL ? Pas nécessairement. Mais vous devez faire un peu plus d'efforts pour y parvenir. Tout d'abord, vous devez installer Docker pour Windows. Il existe des éditions Docker Enterprise pour Windows Server 2016 (et versions ultérieures) et une édition Community pour Windows 10 Professional ou Enterprise. Et j'étais bloqué avec Windows 10 Home Edition.

### Obtenir Docker sur Windows 10 Home

Il semble que faire fonctionner Docker sur Windows 10 Home Edition soit un peu plus compliqué. Docker Community Edition nécessite la prise en charge de Hyper-V, qui n'est pas disponible sur Home Edition. Cela signifie que j'ai dû déterrer [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/), une ancienne distribution qui reposait sur Docker Machine et Virtualbox. Mais après l'installation, Virtualbox m'a accueilli avec une invite disant qu'il était impossible d'exécuter la virtualisation.

Il s'est avéré que j'avais le paramètre de virtualisation désactivé dans le BIOS. Apparemment pour des raisons de sécurité. Je l'ai activé, j'ai rouvert Virtualbox et... même chose. Cela m'a un peu inquiété. Après un peu de recherche sur le Web, j'ai trouvé le conseil de vérifier `systeminfo`. Eh bien, il montrait clairement qu'un hyperviseur était en cours d'exécution. Mais pas Virtualbox et certainement pas Hyper-V, n'est-ce pas ?

À ma grande surprise, c'était Hyper-V tout le temps. Il semble que Home Edition manque des outils utilisateur pour utiliser Hyper-V, mais cela ne signifie pas que l'hyperviseur lui-même n'était pas en cours d'exécution. Heureusement, le désactiver était aussi simple que `bcdedit /set hypervisorlaunchtype off`. Après avoir redémarré la machine, Virtualbox était prêt à fonctionner. Cool, un point pour moi !

### Docker et WSL, meilleurs amis pour toujours ?

Avec Virtualbox fonctionnel, j'ai ouvert Docker Quickstart Terminal. Au premier lancement, il crée une Docker Machine (c'est pourquoi il a besoin de Virtualbox) pour agir en tant qu'hôte pour tous les conteneurs. J'ai tapé `docker run --rm hello-world` et j'ai regardé la barre de progression pendant que Docker téléchargeait l'image appropriée pour moi. Un autre point !

Maintenant, au lieu de `cmd.exe`, j'aimerais utiliser Docker depuis le confort de mon WSL. Comment faire ? Heureusement, WSL a accès aux binaires natifs de Windows. Cela signifie que je peux exécuter `docker-machine.exe ls` pour voir la machine créée par Docker Toolbox. Elle devrait être là, simplement nommée `default`. Si l'état est autre que "Running", vous pouvez la démarrer avec `docker-machine.exe start`. Chaque fois que vous voulez exécuter Docker Machine, rappelez-vous que contrairement à `cmd.exe`, l'extension (`.exe`) est obligatoire.

Normalement, nous appellerions `docker-machine.exe env` pour définir les variables d'environnement.

Malheureusement, il sort les variables dans un format compris par `cmd.exe`, et non par un shell compatible Bourne comme bash ou zsh. Mais nous pouvons changer ce comportement avec `docker-machine.exe env --shell sh`.

Hmm, presque là. Mais il reste une chose en suspens. Le chemin du certificat est écrit comme un chemin Windows. Comment le traduire en quelque chose que WSL comprend ? [Depuis un certain temps maintenant](https://github.com/MicrosoftDocs/WSL/releases/tag/17046), WSL dispose d'un utilitaire pratique appelé `wslpath`. Grâce à cet outil, nous pouvons appeler `export DOCKER_CERT_PATH=$(wslpath $DOCKER_CERT_PATH)` et nous sommes **presque** prêts.

Nous avons encore besoin des outils utilisateur. Donc, en utilisant votre gestionnaire de paquets préféré, installez à la fois le moteur Docker et Docker Compose. Pour moi, cela signifie `brew install docker docker-compose`. Après cela, un `docker run --rm hello-world` devrait donner exactement les mêmes résultats que dans un terminal Docker Toolbox. Félicitations !

### Est-ce tout ?

Non, bien sûr que non. Vous pouvez rapidement remarquer que le bind-mount ne fonctionne pas correctement. Cela est dû au fait que le démon Docker attend des chemins Windows corrects, et les chemins WSL ne peuvent malheureusement pas être traduits automatiquement. Mais il existe quelques astuces que nous pouvons utiliser pour améliorer la situation.

Maintenant, l'astuce dont vous avez besoin dépend de la version que vous exécutez. En appuyant sur Win+R et en tapant `winver`, vous devriez voir une boîte de dialogue qui dit quelque chose comme :

> Microsoft Windows  
> Version 18.03 (OS Build 17133.73)

Si c'est effectivement 18.03 ou plus récent, vous pouvez éditer `/etc/wsl.conf` pour qu'il ressemble à ceci :

```
[automount]
root = /
options = "metadata"
```

Cela signifie que WSL monterait le lecteur C: sous `/c/` au lieu de `/mnt/c`. Pourquoi est-ce important ? Eh bien, c'est important car c'est ce que le démon Docker attend des chemins Windows. Au fait : après avoir sauvegardé le fichier, vous devez vous reconnecter pour que les modifications prennent effet.

**Attention** ! Si vous utilisez [wsl-terminal](https://github.com/goreliu/wsl-terminal), ce changement le cassera. Utilisez la méthode suivante dans ce cas.

Une autre approche si vous ne voulez pas vous reconnecter ou si vous êtes bloqué avec une version plus ancienne est de monter un point de montage sur l'autre comme ceci :

```
sudo mkdir /c
sudo mount --bind /mnt/c /c
```

Plus rapide, mais seulement disponible tant que vous êtes connecté. Vous devrez répéter cela la prochaine fois que vous redémarrerez votre machine ou l'ajouter à votre configuration d'exécution de shell (comme `~/.bashrc` ou `~/.zshrc`). Cela est dû au fait que `/etc/fstab` ne fonctionne pas comme prévu sur WSL.

Comme vous l'avez peut-être remarqué, cela signifie que vous pouvez maintenant exécuter Docker avec des montages, mais seulement si vos volumes sont dans le système de fichiers Windows. Puisque la ligne de commande `docker` attend des chemins absolus, cela ne devrait pas poser de problème, mais avec Docker Compose, vous devez être particulièrement prudent. Il permet d'utiliser des chemins relatifs et de cette façon, tout ce qui commence par `./` ne fonctionnera pas.

Si vous insistez absolument pour monter le système de fichiers de WSL avec Docker, vous pouvez essayer de remplacer tous ces `./` par `/c/Users/$USERNAME/AppData/Local/lxss` avec le `$PWD` du projet. Dans ce cas, `$USERNAME` ne signifie pas votre nom d'utilisateur WSL, mais votre nom d'utilisateur Windows.

J'ai pensé qu'il serait intelligent d'écrire un wrapper autour de Docker Compose pour qu'il change le répertoire de travail dans ce `lxss`, mais malheureusement WSL n'a pas les droits d'y accéder. Et à juste titre, je pense !

### Un dernier obstacle

Nous pouvons exécuter Docker et nous pouvons lier les répertoires de données. Que pouvons-nous vouloir de plus ? Peut-être le port-forwarding ? Contrairement aux solutions natives, l'utilisation de Docker via Docker Machine nécessite d'appeler chaque service sur `$(docker-machine ip):$PORT` au lieu du habituel `localhost:$PORT`. Il existe un moyen de contourner cela, bien que ce ne soit pas très élégant :

```sh
#!/bin/sh

# Ce script utilise le port forwarding de Virtualbox pour rendre tous les services Docker
# disponibles sur l'hôte Windows sous `localhost`

VBXMGMT=/c/Program\ Files/Oracle/VirtualBox/VBoxManage.exe

# Liste tous les identifiants de conteneurs en cours d'exécution
docker ps -q | while read -r i; do
  # Liste tous les ports liés par ce conteneur
  for port in $(docker port "$i" | cut -d'-' -f1); do
    port_num=$(echo "${port}" | cut -d'/' -f1)
    port_type=$(echo "${port}" | cut -d'/' -f2)
    echo "Créer la règle natpf1 pour le port ${port_type} ${port_num}"
    "$VBXMGMT" controlvm "default" natpf1 "${port_type}-port${port_num},${port_type},,${port_num},,${port_num}"
  done
done
```

Je crois que vous pouvez écrire un wrapper autour de Docker pour effectuer cette danse chaque fois que vous exécutez un nouveau conteneur. J'avoue que je ne l'ai pas testé de cette manière, car la plupart du temps, je suis satisfait de rediriger un seul port.

J'espère que cela rendra votre travail avec Docker sur WSL beaucoup plus agréable. Cela a certainement été le cas pour moi !

### Bibliographie

Je n'aurais pas écrit cet article sans les personnes qui ont partagé leurs connaissances. Chaque fois que je suis tombé sur un obstacle, j'ai pu chercher des solutions existantes. Ci-dessous, une liste d'articles et de posts qui m'ont aidé à écrire ce guide :

[**Configurer Docker pour Windows et WSL pour qu'ils fonctionnent sans faille**](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)  
[_Avec quelques ajustements, le WSL (Windows Subsystem for Linux, également connu sous le nom de Bash pour Windows) peut être utilisé avec Docker..._nickjanetakis.com](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)[**Comment accéder aux fichiers Linux/Ubuntu depuis Windows 10 WSL ?**](https://superuser.com/a/1110976)  
[_Super User est un site de questions et réponses pour les passionnés d'informatique et les utilisateurs avancés. Rejoignez-les ; cela ne prend qu'une minute..._superuser.com](https://superuser.com/a/1110976)[**Redirection de port dans docker-machine ?**](https://stackoverflow.com/questions/32174560/port-forwarding-in-docker-machine)  
[_Vous pouvez toujours accéder à la commande VBoxmanage.exe depuis VirtualBox utilisée par docker machine : VBoxManage controlvm..._stackoverflow.com](https://stackoverflow.com/questions/32174560/port-forwarding-in-docker-machine)