---
title: Comment exécuter GitHub Actions localement en utilisant l'outil CLI act
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2024-03-11T20:21:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-github-actions-locally
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/How-to-run-GitHub-actions-locally.png
tags:
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
seo_title: Comment exécuter GitHub Actions localement en utilisant l'outil CLI act
seo_desc: "GitHub Actions help automate tasks like building, testing, and deploying\
  \ in your GitHub repository. \nWith one click, you can publish your production-ready\
  \ code or package on npm, GitHub pages, docker images, deploy your production code\
  \ on a cloud pro..."
---

GitHub Actions aide à automatiser des tâches comme la construction, les tests et le déploiement dans votre dépôt GitHub.

Avec un seul clic, vous pouvez publier votre code ou package prêt pour la production sur npm, GitHub pages, des images docker, déployer votre code de production sur un fournisseur cloud, et ainsi de suite.

Le problème commence lorsque vous testez GitHub Actions. Cela peut être chronophage et douloureux. D'abord, vous devez modifier le fichier GitHub Actions localement, pousser votre code local dans votre dépôt GitHub, et attendre le résultat.

Pour résoudre ce problème, vous pouvez utiliser l'outil CLI [the `act`](https://github.com/nektos/act) pour tester et écrire l'action GitHub localement. Avec `act` CLI, vous n'avez pas besoin de commiter/pousser votre code local vers le dépôt GitHub. Vous testez l'action GitHub localement sur votre ordinateur portable ou machine.

**Voici les étapes impliquées :**

* [Comment installer `act`.](#heading-installation-de-act-pour-github-actions)
* [Comment configurer et initialiser le CLI `act`.](#heading-comment-configurer-et-initialiser-le-cli-act)
* [Comment utiliser l'outil CLI `act`.](#comment-utiliser-loutil-cli-act)

## Comment installer `act` pour GitHub Actions

L'outil CLI [`act`](https://github.com/nektos/act) fonctionne avec Docker. Avant de commencer avec `act` CLI, installez d'abord [Docker](https://www.docker.com/) sur votre système ou ordinateur portable.

Pour installer le CLI `act`, vous devez exécuter la commande suivante :

```bash
# Windows
choco install act-cli

# MacOS
brew install act

# Linux
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

## Comment configurer et initialiser le CLI `act`

Après l'installation réussie du CLI `act` sur votre ordinateur portable ou machine, l'étape suivante consiste à l'exécuter dans votre projet.

Le CLI `act` demande quelle taille d'image Docker — grande, moyenne ou micro — doit être installée pendant l'installation.

Il existe différentes tailles d'images Docker :

1. La taille de l'image Docker Micro est de 200 Mo, et les petits projets l'utilisent.
2. La taille de l'image Docker Medium est de 500 Mo, et les grands projets l'utilisent.
3. La taille de l'image Docker Large est de 17 Go, et les entreprises l'utilisent.

Le CLI `act` utilise l'image Docker pour exécuter l'action GitHub localement.

```bash
$ act
```

La sortie de la commande dans le terminal ressemble à ceci :

```bash
$ test-github-actions git:(main) ✗ act
? Veuillez choisir l'image par défaut que vous souhaitez utiliser avec act :
  - Image de grande taille : env. 17 Go de téléchargement + 53,1 Go de stockage, vous aurez besoin de 75 Go d'espace disque libre, instantanés des GitHub Hosted Runners sans instantanés et images docker tirées
  - Image de taille moyenne : ~500 Mo, inclut uniquement les outils nécessaires pour démarrer les actions et vise à être compatible avec la plupart des actions
  - Image de taille micro : <200 Mo, contient uniquement NodeJS requis pour démarrer les actions, ne fonctionne pas avec toutes les actions

L'image par défaut et d'autres options peuvent être modifiées manuellement dans ~/.actrc (veuillez vous référer à https://github.com/nektos/act#configuration pour des informations supplémentaires sur la structure du fichier) Micro
[Build Ghost and test theme/install] 🚀  Start image=node:16-buster-slim
INFO[0023] Parallel tasks (0) below minimum, setting to 1 
[Build Ghost and test theme/install]   🐳  docker pull image=node:16-buster-slim platform= username= forcePull=true
INFO[0031] Parallel tasks (0) below minimum, setting to 1 
[Build Ghost and test theme/install]   🐳  docker create image=node:16-buster-slim platform= entrypoint=["tail" "-f" "/dev/null"] cmd=[] network="host"
[Build Ghost and test theme/install]   🐳  docker run image=node:16-buster-slim platform= entrypoint=["tail" "-f" "/dev/null"] cmd=[] network="host"
[Build Ghost and test theme/install]   ☁  git clone 'https://github.com/vimtor/action-zip' # ref=v1.2
[Build Ghost and test theme/install]   ☁  git clone 'https://github.com/softprops/action-gh-release' # ref=v0.1.15
[Build Ghost and test theme/install] ⭐ Run Main actions/checkout@v4
[Build Ghost and test theme/install]   🐳  docker cp src=/home/officialrajdeepsingh/medium/test-github-actions/. dst=/home/officialrajdeepsingh/medium/test-github-actions
[Build Ghost and test theme/install]   ✅  Success - Main actions/checkout@v4
[Build Ghost and test theme/install] ⭐ Run Main Easy Zip Files
[Build Ghost and test theme/install]   🐳  docker cp src=/home/officialrajdeepsingh/.cache/act/vimtor-action-zip@v1.2/ dst=/var/run/act/actions/vimtor-action-zip@v1.2/
[Build Ghost and test theme/install]   🐳  docker exec cmd=[node /var/run/act/actions/vimtor-action-zip@v1.2/dist/index.js] user= workdir=
| Ready to zip "build/ home.txt" into example.zip
|   - build/
|   - home.txt
| 
| Zipped file example.zip successfully
[Build Ghost and test theme/install]   ✅  Success - Main Easy Zip Files
[Build Ghost and test theme/install] Cleaning up container for job install
[Build Ghost and test theme/install] 🏁  Job succeeded
```

Après avoir téléchargé l'image depuis le dépôt Docker, le CLI `act` exécute l'action GitHub.

Le CLI `act` génère le fichier `~/.actrc` dans l'ordinateur portable pour la configuration. Le fichier `~/.actrc` contient le nom de l'image Docker.

```bash
# .actrc
-P ubuntu-latest=node:16-buster-slim
-P ubuntu-22.04=node:16-bullseye-slim
-P ubuntu-20.04=node:16-buster-slim
-P ubuntu-18.04=node:16-buster-slim
```

Pour installer d'autres images Docker, supprimez le fichier `~/.actrc` et relancez le CLI `act` pour installer les différentes images Docker.

### Erreur

En raison de la dépendance à Docker, nous pouvons rencontrer certaines erreurs lors de l'initialisation d'un CLI `act` pour la première fois.

```bash
$ act
```

L'erreur devrait ressembler à ceci :

```bash
$ test-github-actions git:(main) ✗ act       
ERRO[0000] daemon Docker Engine socket not found and containerDaemonSocket option was not set 
? Veuillez choisir l'image par défaut que vous souhaitez utiliser avec act :
  - Image de grande taille : env. 17 Go de téléchargement + 53,1 Go de stockage, vous aurez besoin de 75 Go d'espace disque libre, instantanés des GitHub Hosted Runners sans instantanés et images docker tirées
  - Image de taille moyenne : ~500 Mo, inclut uniquement les outils nécessaires pour démarrer les actions et vise à être compatible avec la plupart des actions
  - Image de taille micro : <200 Mo, contient uniquement NodeJS requis pour démarrer les actions, ne fonctionne pas avec toutes les actions

L'image par défaut et d'autres options peuvent être modifiées manuellement dans ~/.actrc (veuillez vous référer à https://github.com/nektos/act#configuration pour des informations supplémentaires sur la structure du fichier) Micro
[Build Ghost and test theme/install] 🚀  Start image=node:16-buster-slim
INFO[0305] Parallel tasks (0) below minimum, setting to 1 
[Build Ghost and test theme/install]   🐳  docker pull image=node:16-buster-slim platform= username= forcePull=true
Error: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

Vous voyez l'erreur `Cannot connect to the Docker daemon` dans le code ci-dessus. Ce problème se produit en raison du démon Docker. En termes simples, le démon Docker ne fonctionne pas. Vous pouvez résoudre ce problème en démarrant votre Docker et en relançant votre commande `act`.

Il existe deux façons de lancer les services Docker.

1. Ouvrez Docker desktop dans votre fenêtre, et votre service Docker est démarré.
2. Lancez Docker avec la commande `systemctl start docker` sur Linux.

Vous pouvez vérifier si votre Docker est en cours d'exécution ou non avec la commande suivante :

```bash
$ systemctl status docker

● docker.service - Docker Application Container Engine
     Loaded: loaded (/etc/systemd/system/docker.service; enabled; preset: enabled)
    Drop-In: /nix/store/fibzdkfv6in4xw39rm0c7bq4nadzisas-system-units/docker.service.d
             └─overrides.conf
     Active: active (running) since Mon 2024-02-26 12:38:37 IST; 3h 39min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 1186 (dockerd)
         IP: 0B in, 0B out
         IO: 109.0M read, 152.0K written
      Tasks: 40
     Memory: 148.5M
        CPU: 1min 40.817s
     CGroup: /system.slice/docker.service
             ├─1186 /nix/store/7pzis8dkhs461kl1bg2fp0202dw6r5i5-moby-24.0.5/libexec/docker/dockerd --config-file=/nix/store/3rlv5f0zldcc120b01szywidl0qz9x4p-daemon.json
             └─1256 containerd --config /var/run/docker/containerd/containerd.toml

Feb 26 12:38:37 nixos dockerd[1256]: time="2024-02-26T12:38:37.532987858+05:30" level=info msg="containerd successfully booted in 0.016901s"
Feb 26 12:38:37 nixos dockerd[1186]: time="2024-02-26T12:38:37.562515048+05:30" level=info msg="[graphdriver] using prior storage driver: overlay2"
Feb 26 12:38:37 nixos dockerd[1186]: time="2024-02-26T12:38:37.564062690+05:30" level=info msg="Loading containers: start."
Feb 26 12:38:37 nixos dockerd[1186]: time="2024-02-26T12:38:37.778478313+05:30" level=info msg="Default bridge (docker0) is assigned with an IP address 172.17.0.0/16. Daemon option --bip can be used to set a preferred IP address"
Feb 26 12:38:37 nixos dockerd[1186]: time="2024-02-26T12:38:37.805931545+05:30" level=info msg="Loading containers: done."
Feb 26 12:38:37 nixos dockerd[1186]: time="2024-02-26T12:38:37.828589904+05:30" level=info msg="Docker daemon" commit=v24.0.5 graphdriver=overlay2 version=24.0.5
Feb 26 12:38:37 nixos dockerd[1186]: time="2024-02-26T12:38:37.828929197+05:30" level=info msg="Daemon has completed initialization"
Feb 26 12:38:37 nixos systemd[1]: Started Docker Application Container Engine.
Feb 26 12:38:37 nixos dockerd[1186]: time="2024-02-26T12:38:37.841992729+05:30" level=info msg="API listen on /run/docker.sock"
Feb 26 12:38:37 nixos dockerd[1186]: time="2024-02-26T12:38:37.841993669+05:30" level=info msg="API listen on /run/docker.sock"
```

## Comment utiliser l'outil CLI `act`

Le CLI `act` a de nombreuses options, mais nous allons en examiner quelques-unes importantes. Vous pouvez vérifier toutes les options en exécutant la commande `act --help`.

### Options du CLI `act`

Voici quelques options du CLI `act` :

* [Événements](#heading-evenements)
* [Listes](#heading-listes)
* [Exécution de travaux spécifiques](#heading-execution-de-travaux-specifiques)
* [Graphique](#heading-graphique)
* [Variables d'environnement](#heading-variables-denvironnement)
* [Secrets](#heading-secrets)

### Événements

L'action par défaut du CLI `act` est l'action de push, qui ne déclenche que les événements de push par défaut.

```bash
$ act
```

Vous pouvez changer l'événement après avoir passé le deuxième argument, qui est le nom de votre action. Dans notre cas, nous allons passer pull_request.

```bash
$ act pull_request
```

Il existe une longue liste disponible pour déclencher les workflows. Vous pouvez [la lire sur la documentation de GitHub action](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows).

### Listes

L'option de liste imprime tous les travaux disponibles que vous écrivez dans `.github/workflows`.

```bash
$ act -l
```

La sortie de la commande dans le terminal ressemble à ceci.

```bash
$ act -l    
Stage  Job ID             Job name           Workflow name                  Workflow file      Events      
0      zip                zip                Convert files into Zip         build-project.yml  release     
0      request_test       request_test       Pull Request                   fork.yml           fork        
0      pull_request_test  pull_request_test  Pull Request                   issues.yml         issues      
0      show               show               Convert files into Zip folder  test.yml           pull_request
```

### Exécution de travaux spécifiques

Vous utilisez la commande d'option `--job` pour exécuter des travaux spécifiques à partir de vos workflows.

Assurez-vous que le nom de votre travail est unique — sinon, il exécute tous les travaux contenant le même dans votre workflow. Chaque fois que vous ne pouvez pas passer un événement par défaut, déclenchez l'événement de push.

### Syntaxe

```bash
act --job <nom-de-votre-travail>
```

Par exemple, nous exécutons un travail spécifique show.

```bash
$ act --job 'show'
```

### Graphique

L'option graphique dessine la structure des travaux de workflow disponibles dans votre terminal sous forme de graphique.

```bash
$ act --graph
```

La sortie de la commande dans le terminal ressemble à ceci :

```bash
$ act --graph
┌────────┬─────────────────────┬─────────────────────┬──────────────────────────────┐
│ zip    │ request_test        │ pull_request_test   │ show                        │
└────────┴─────────────────────┴─────────────────────┴──────────────────────────────┘
```

### Variables d'environnement

L'utilisation de variables d'environnement avec le CLI `act` est facile. Vous devez simplement créer un nouveau fichier `.env`. Le CLI `act` charge automatiquement l'environnement qui est disponible dans le fichier `.env`. Par exemple, nous ajoutons des variables `ENV_ID`.

```yaml
# .env

ENV_ID='Mon Env'
```

Pour utiliser les variables d'environnement `ENV_ID`, utilisez la syntaxe suivante `${{ env.ENV_ID }}` dans votre action GitHub :

```bash
# .github/workflows/test.yml

name: Convert files into Zip folder

on: pull_request

jobs:
  show:
    runs-on: ubuntu-latest
    steps:
      - name: Show Env
        run: echo "Env ${{ env.ENV_ID }}"
```

Avec l'option `--env-file`, vous pouvez changer le nom de fichier `.env` par défaut en fichier `my-custom.env`.

```bash
$ act --env-file=my-custom.env
```

### Secrets

Vous devez créer un nouveau fichier `.secrets` pour charger les secrets d'environnement avec le CLI `act`. Cela charge automatiquement les secrets d'environnement qui sont disponibles dans le fichier `secrets`. Par exemple, nous ajoutons des variables `APP_SECRET` et `APP_ID`.

```yaml
APP_SECRET='7824jurd789gyu45esxgfgf48822166974gtredsyujn'
APP_ID='7878974561587'
```

Pour utiliser les variables d'environnement `APP_SECRET`, utilisez la syntaxe suivante `${{ secrets.APP_SECRE}}` dans votre action GitHub :

```yaml
# .github/workflows/test.yml

name: Learn environment secrets 

on: pull_request

jobs:
  show:
    runs-on: ubuntu-latest
    steps:
      - name: Show env
        run: echo "App SECRET ${{ secrets.APP_SECRET }}"
      - name: Show varibale
        run: echo "App ID ${{ secrets.APP_ID }}"
```

Vous pouvez charger votre fichier personnalisé `my-custom.secrets` contenant tous vos secrets avec l'option `--secret-file`.

```bash
$ act --secret-file=my-custom.secrets
```

## Conclusion

Le CLI `act` aide à économiser du temps et de l'énergie lors du travail et des tests GitHub localement. Actuellement, il n'existe pas d'alternative au CLI `act`, qui nous permet d'exécuter des actions GitHub localement.

Le CLI `act` n'est pas entièrement compatible avec les actions GitHub. Certaines fonctionnalités ne sont pas implémentées, par exemple, la concurrency, aucun contexte `vars`, contexte `github` incomplet, et ainsi de suite.

Vous pouvez m'embaucher en tant que développeur freelance avec [Upwork](https://www.upwork.com/freelancers/~01a4e8ba7a41795229) et autres mises à jour. Suivez-moi sur [Twitter (X)](https://twitter.com/Official_R_deep) et [Medium](https://officialrajdeepsingh.medium.com/).