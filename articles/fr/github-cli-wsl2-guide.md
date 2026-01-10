---
title: Comment configurer GitHub CLI sur WSL2
subtitle: ''
author: Ayu Adiati
co_authors: []
series: null
date: '2025-08-14T20:17:16.374Z'
originalURL: https://freecodecamp.org/news/github-cli-wsl2-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755202477019/fbc68131-107a-40ae-9dae-c14224d0866a.png
tags:
- name: GitHub
  slug: github
- name: WSL
  slug: wsl
- name: Linux
  slug: linux
seo_title: Comment configurer GitHub CLI sur WSL2
seo_desc: 'Recently, I set up WSL2 and Ubuntu on my Windows 11 to work on some open-source
  projects. Since I also maintain these projects, I installed GitHub CLI to ease my
  workflow. I successfully installed the GitHub CLI, but failed to authenticate it.

  The er...'
---

Récemment, j'ai configuré WSL2 et Ubuntu sur mon Windows 11 pour travailler sur des projets open-source. Comme je maintiens également ces projets, j'ai installé [GitHub CLI](https://cli.github.com/) pour faciliter mon flux de travail. J'ai réussi à installer GitHub CLI, mais j'ai échoué lors de l'authentification.

Le message d'erreur `failed to authenticate via web browser: Too many requests have been made in the same timeframe. (slow_down)` est apparu dans mon terminal, alors que sur le navigateur web, il indiquait que l'authentification était réussie.

![Un message indique "Félicitations, vous êtes prêt", marquant que l'authentification GitHub CLI est réussie](https://cdn.hashnode.com/res/hashnode/image/upload/v1754718774837/0d1de969-a1e3-4f0a-a3ce-e3c4661ce0d0.png align="center")

J'ai cherché sur Google et trouvé quelques solutions de contournement que j'ai essayées, mais une seule a fonctionné à merveille !

Après avoir enfin résolu ce problème d'authentification délicat pour GitHub CLI sur WSL2, j'ai conçu ce guide. C'est un tutoriel complet pour une solution qui fonctionne, couvrant tout, de l'installation fluide à la gestion continue.

## Table des matières

* [Prérequis](#heading-prequis)
    
* [Comment installer GitHub CLI sur WSL2](#heading-comment-installer-github-cli-sur-wsl2)
    
* [Comment authentifier GitHub CLI sur WSL2 avec votre compte GitHub](#heading-comment-authentifier-github-cli-sur-wsl2-avec-votre-compte-github)
    
* [Comment mettre à jour GitHub CLI sur WSL2](#heading-comment-mettre-a-jour-github-cli-sur-wsl2)
    
* [Comment désinstaller GitHub CLI sur WSL2](#heading-comment-desinstaller-github-cli-sur-wsl2)
    
* [Comment révoquer l'accès de GitHub CLI sur GitHub](#heading-comment-revoquer-lacces-de-github-cli-sur-github)
    
* [Le mot de la fin](#heading-le-mot-de-la-fin)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir installé ces éléments sur votre machine Windows :

* WSL2
    
* Une distribution Linux
    
* Windows PowerShell
    
* [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/install) (optionnel)
    

Pour suivre les instructions de cet article, vous pouvez utiliser le terminal Windows PowerShell en tant qu'administrateur.

Alternativement, si Windows Terminal est installé, vous pouvez utiliser le terminal Linux en cliquant sur l'icône « flèche vers le bas » en haut et en sélectionnant la distribution.

![Menu déroulant dans Windows Terminal](https://cdn.hashnode.com/res/hashnode/image/upload/v1754677301223/7e846117-3fd1-42a2-ab3e-029e94672aca.png align="center")

## Comment installer GitHub CLI sur WSL2

Vous pouvez utiliser le processus d'installation décrit ici si vous utilisez les distributions Ubuntu, Debian ou Raspberry Pi OS (apt). Pour les autres distributions que celles mentionnées ici, vous pouvez consulter le processus d'installation disponible sur la [documentation officielle de GitHub CLI](https://github.com/cli/cli/blob/trunk/docs/install_linux.md).

Pour installer GitHub CLI dans WSL2 :

1. Exécutez cette commande :
    
    ```bash
    (type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
    	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
    	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
    	&& cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
    	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
    	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    	&& sudo apt update \
    	&& sudo apt install gh -y
    ```
    
2. Saisissez votre mot de passe Linux lorsque vous y êtes invité.
    
3. Assurez-vous que GitHub CLI est installé en exécutant la commande `gh --version`. Si l'installation a réussi, vous devriez voir quelque chose comme ceci dans votre terminal :
    
    ```bash
    gh version 2.76.2 (2025-07-30)
    https://github.com/cli/cli/releases/tag/v2.76.2
    ```
    

## Comment authentifier GitHub CLI sur WSL2 avec votre compte GitHub

Avant de pouvoir utiliser GitHub CLI, vous devez d'abord l'authentifier. Vous recevrez un message d'erreur `HTTP 401: Bad credentials (https://api.github.com/graphql)` si vous exécutez une commande GitHub CLI sans authentification.

Pour authentifier GitHub CLI avec votre compte GitHub :

1. Exécutez la commande `gh auth login` dans votre terminal.
    
2. Vous recevrez plusieurs invites et vous devrez choisir les méthodes que vous préférez. Voici ce que j'ai sélectionné pour chaque invite :
    
    ```plaintext
    ? Where do you use GitHub? GitHub.com
    ? What is your preferred protocol for Git operations on this host? HTTPS
    ? How would you like to authenticate GitHub CLI? Login with a web browser
    ```
    
    Après avoir répondu à toutes les invites, vous devriez recevoir le message pour copier un code à usage unique comme indiqué ci-dessous. Vous **n'avez pas besoin de copier le code** à ce stade.
    
    ```bash
    ! First copy your one-time code: XXXX—XXXX
    ```
    
3. Appuyez sur « Entrée ». Cela ouvre automatiquement la page « Device Activation » sur votre navigateur.
    
4. Cliquez sur le bouton vert « Continue ».
    
    ![Page d'activation d'appareil GitHub sur un navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1754848322666/2a4af9ab-c197-4ec9-802f-ad9b4f24375c.png align="center")
    
    GitHub devrait vous demander de saisir le code affiché sur votre terminal, comme indiqué dans la capture d'écran ci-dessous. Mais voici l'astuce ! **Ne collez aucun code et ne fermez pas le navigateur**. Revenons d'abord à votre terminal.
    
    ![Page d'activation d'appareil GitHub sur un navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1754722491767/d84534da-522f-4e82-84c2-a1bfc75940ef.png align="center")
    
    Maintenant, vous pourriez obtenir ce message d'erreur sur votre terminal :
    
    ```bash
    grep: /proc/sys/fs/binfmt_misc/WSLInterop: No such file or directory
    WSL Interopability is disabled. Please enable it before using WSL.
    grep: /proc/sys/fs/binfmt_misc/WSLInterop: No such file or directory
    [error] WSL Interoperability is disabled. Please enable it before using WSL.
    ```
    
5. Appuyez sur `Ctrl + C` pour arrêter le processus s'il est toujours en cours, ou laissez-le s'arrêter de lui-même. Une fois arrêté, vous devriez voir ce message :
    
    ```bash
    failed to authenticate via web browser: Too many requests have been made in the same timeframe. (slow_down)
    ```
    
6. Exécutez à nouveau la commande `gh auth login` et répétez le processus pour sélectionner les méthodes de votre choix. Cette fois, lorsqu'on vous demande d'appuyer sur « Entrée », **ne le faites pas**.
    
7. Copiez le dernier code et retournez à la page « Device Activation » que vous avez laissée ouverte dans votre navigateur.
    
8. Collez le code que vous avez copié et cliquez sur le bouton vert « Continue ».
    
9. Cliquez sur le bouton vert « Authorize github » après que GitHub vous a redirigé vers la page « Authorize GitHub CLI ». Vous devriez maintenant voir le message « Félicitations, vous êtes prêt ! »
    
10. Retournez à votre terminal et appuyez sur « Entrée ». Cela déclenche ces actions :
    
    * Cela ouvre automatiquement une nouvelle page « Device Activation » dans votre navigateur. Vous pouvez l'ignorer sans risque.
        
    * Dans le terminal, vous voyez d'abord le message d'erreur comme à l'étape 4. Ne faites rien et attendez un peu. Ensuite, vous obtenez :
        
        ```bash
        ✓ Authentication complete.
        - gh config set -h github.com git_protocol https
        ✓ Configured git protocol
        ! Authentication credentials saved in plain text
        ✓ Logged in as YOUR-GITHUB-USERNAME
        ! You were already logged in to this account
        ```
        

Et voilà, GitHub CLI est maintenant authentifié avec succès !

> Merci à l'utilisateur [« ikeyan » sur GitHub pour sa solution d'authentification GitHub CLI](https://github.com/cli/cli/discussions/6884#discussioncomment-10176332) !

## Comment mettre à jour GitHub CLI sur WSL2

C'est toujours une bonne pratique de vérifier régulièrement les mises à jour des paquets et des dépendances, et de passer à la version la plus récente lorsqu'elle est disponible — cela inclut GitHub CLI. Pour vérifier les mises à jour et mettre à jour la version de GitHub CLI :

1. Exécutez la commande `sudo apt update` dans votre terminal. Cette commande récupère la liste des mises à jour disponibles.
    
2. Saisissez votre mot de passe Linux lorsque vous y êtes invité.
    
3. Si vous devez mettre à jour votre GitHub CLI, exécutez `sudo apt install gh`. Cette commande installe la version la plus récente de GitHub CLI.
    
4. Saisissez votre mot de passe Linux lorsque vous y êtes invité.
    

Maintenant, votre GitHub CLI dispose de la version la plus récente.

## Comment désinstaller GitHub CLI sur WSL2

Si un jour vous sentez que vous n'avez plus besoin d'utiliser GitHub CLI, vous pouvez le désinstaller en suivant ces étapes :

1. Exécutez la commande `sudo apt remove gh` dans votre terminal.
    
2. Saisissez votre mot de passe Linux lorsque vous y êtes invité.
    
3. Appuyez sur « Y » pour continuer le processus de désinstallation.
    

GitHub CLI est maintenant désinstallé de votre environnement WSL.

## Comment révoquer l'accès de GitHub CLI sur GitHub

Après avoir désinstallé GitHub CLI, vous pourriez penser que l'accès à votre compte a disparu, mais ce n'est pas le cas. L'authentification que vous avez accordée est toujours active. Si vous ne prévoyez pas d'utiliser à nouveau la CLI, il est de bonne pratique de révoquer cet accès.

Voici comment faire directement depuis votre compte GitHub :

1. Sur votre compte GitHub, cliquez sur votre photo de profil en haut à droite et cliquez sur « Settings ».
    
    ![Option Settings sur le menu déroulant de GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1754725091482/8fb8a0fd-8dbd-4342-9fe8-309a13d72c39.png align="center")
    
    2. Dans la barre latérale gauche, trouvez « Integrations » et cliquez sur « Applications ».
        
        ![Onglet Applications dans les paramètres d'intégrations sur GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1754815240842/ca49d207-6ee2-476f-a53d-bde53b2d57dd.png align="center")
        
    3. Cliquez sur l'onglet « Authorized OAuth Apps » en haut.
        
        ![Onglet Authorized OAuth Apps sur GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1754815346304/a360f7dc-7024-44c3-8e19-15d94b35ce8e.png align="center")
        
    4. Trouvez GitHub CLI et cliquez sur l'icône « trois points » à côté.
        
    5. Cliquez sur « Revoke ».
        
        ![Option Revoke sur GitHub pour révoquer une application OAuth autorisée](https://cdn.hashnode.com/res/hashnode/image/upload/v1754725454783/dd544380-482a-4385-97c1-4ebc35026658.png align="center")
        
    6. Confirmez en cliquant sur le bouton « I understand, revoke access ».
        

Maintenant, GitHub CLI n'a plus accès à votre compte GitHub.

---

## Le mot de la fin

🖼️ Crédit image de couverture : [undraw.co](http://undraw.co)

Merci de m'avoir lu ! Enfin, vous pouvez me retrouver sur [X](https://twitter.com/@AdiatiAyu) et [LinkedIn](https://www.linkedin.com/in/adiatiayu/). Connectons-nous ! 😊