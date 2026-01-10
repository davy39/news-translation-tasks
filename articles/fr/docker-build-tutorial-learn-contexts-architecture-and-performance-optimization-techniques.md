---
title: 'Tutoriel Docker Build : Apprenez les contextes, l''architecture et les techniques
  d''optimisation des performances'
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2025-10-07T18:20:08.327Z'
originalURL: https://freecodecamp.org/news/docker-build-tutorial-learn-contexts-architecture-and-performance-optimization-techniques
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759861193876/871b72e7-9673-4572-b788-48f082a6b380.png
tags:
- name: Docker
  slug: docker
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: software development
  slug: software-development
seo_title: 'Tutoriel Docker Build : Apprenez les contextes, l''architecture et les
  techniques d''optimisation des performances'
seo_desc: Docker build is a fundamental concept every developer needs to understand.
  Whether you're containerizing your first application or optimizing existing Docker
  workflows, understanding Docker build contexts and Docker build architecture is
  essential fo...
---

Docker build est un concept fondamental que chaque développeur doit comprendre. Que vous conteneurisiez votre première application ou que vous optimisiez des workflows Docker existants, la compréhension des contextes de build Docker et de l'architecture de build Docker est essentielle pour créer des applications conteneurisées efficaces et évolutives.

Ce guide complet couvre tout, des concepts de base aux techniques d'optimisation avancées, vous aidant à éviter les pièges courants et à construire de meilleures images Docker.

## Table des matières

1. [Qu'est-ce que Docker Build ?](#heading-qu-est-ce-que-docker-build)
    
2. [Architecture de Docker Build : comment ça marche](#heading-architecture-de-docker-build-comment-ca-marche)
    
3. [Fonctionnalités de Docker Build](#heading-fonctionnalites-de-docker-build)
    
4. [Contexte de build Docker](#heading-contexte-de-build-docker)
    
5. [Types de contextes de build Docker](#heading-types-de-contextes-de-build-docker)
    
6. [Erreurs courantes de Docker Build (et comment les corriger)](#heading-erreurs-courantes-de-docker-build-et-comment-les-corriger)
    
7. [Comment optimiser et surveiller les performances de build](#heading-comment-optimiser-et-surveiller-les-performances-de-build)
    
8. [Meilleures pratiques pour les performances de Docker Build](#heading-meilleures-pratiques-pour-les-performances-de-docker-build)
    
9. [Dépannage des problèmes de Docker Build](#heading-depannage-des-problemes-de-docker-build)
    
10. [Conclusion](#heading-conclusion)
    

## Qu'est-ce que Docker Build ?

Docker build est le processus de création d'une image Docker à partir d'un Dockerfile et d'un ensemble de fichiers appelé le **contexte de build**. Lorsque vous lancez `docker build`, vous demandez à Docker de :

1. Lire les instructions de votre Dockerfile
    
2. Rassembler les fichiers nécessaires (contexte de build)
    
3. Exécuter chaque instruction étape par étape
    
4. Créer une image Docker finale
    

Considérez cela comme le suivi d'une recette : le Dockerfile est votre recette, et le contexte de build contient tous les ingrédients dont vous pourriez avoir besoin.

## Architecture de Docker Build : comment ça marche

Docker Build utilise une architecture client-serveur où deux composants distincts (**Buildx et BuildKit**) travaillent ensemble pour construire vos images Docker. C'est différent de la façon dont beaucoup de gens imaginent le fonctionnement de Docker, car il ne s'agit pas d'un seul programme monolithique faisant tout.

### Qu'est-ce que Buildx (Le Client) ?

Buildx sert d'interface utilisateur avec laquelle vous interagissez directement chaque fois que vous travaillez avec des builds Docker. Lorsque vous tapez `docker build .` dans votre terminal, vous communiquez en réalité avec Buildx, qui agit comme intermédiaire entre vous et le moteur de build réel.

#### Les missions principales de Buildx :

* Interprète votre commande de build et ses options
    
* Envoie des requêtes de build structurées à BuildKit
    
* Gère plusieurs instances BuildKit (builders)
    
* Gère l'authentification et les secrets
    
* Vous affiche la progression du build
    

### Qu'est-ce que BuildKit (Le Serveur/Builder)

BuildKit fonctionne comme le moteur de build réel qui effectue tout le travail lourd pendant le processus de build Docker. Ce composant backend puissant reçoit les requêtes de build structurées de Buildx et commence immédiatement à lire et à interpréter vos Dockerfiles ligne par ligne.

#### Les missions principales de BuildKit :

* Reçoit les requêtes de build de Buildx
    
* Lit et interprète les Dockerfiles
    
* Exécute les instructions de build étape par étape
    
* Gère le cache de build et les couches (layers)
    
* Ne demande au client que les fichiers dont il a besoin
    
* Crée l'image Docker finale
    

### Comment ils communiquent

Voici ce qui se passe lorsque vous lancez `docker build .` :

![Diagramme montrant le processus de build Docker avec BuildKit, incluant l'envoi de la requête de build avec le Dockerfile et les arguments de build, la demande et la réception de package.json, l'exécution de npm install, la demande et la réception des fichiers du répertoire src, la copie des fichiers, la fin du build et l'option de push vers un registre.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758733757378/d3322dad-efac-4c4a-b8f8-69f17a4920e8.png align="center")

Lorsque vous lancez `docker build`, la commande initie un processus en plusieurs étapes avec BuildKit (comme illustré dans l'image ci-dessus).

Tout d'abord, elle envoie une requête de build contenant votre Dockerfile, les arguments de build, les options d'exportation et les options de cache. BuildKit demande ensuite intelligemment uniquement les fichiers dont il a besoin au moment où il en a besoin, en commençant par `package.json` pour exécuter `npm install` pour l'installation des dépendances.

Une fois cela terminé, il demande le répertoire `src/` contenant le code de votre application et copie ces fichiers dans l'image avec la commande `COPY`.

Une fois toutes les étapes de build terminées, BuildKit renvoie l'image finalisée. En option, vous pouvez ensuite pousser cette image vers un registre de conteneurs pour la distribution ou le déploiement.

Cette approche de transfert de fichiers à la demande est l'une des optimisations clés de BuildKit : au lieu d'envoyer l'intégralité de votre contexte de build à l'avance, il ne demande des fichiers spécifiques qu'au fur et à mesure que chaque étape de build en a besoin, ce qui rend le processus de build plus efficace.

### Détails clés de la communication

La requête de build contient :

```json
{
  "dockerfile": "FROM node:18\nWORKDIR /app\n...",
  "buildArgs": {"NODE_ENV": "production"},
  "exportOptions": {"type": "image", "name": "my-app:latest"},
  "cacheOptions": {"type": "registry", "ref": "my-app:cache"}
}
```

Requêtes de ressources :

* BuildKit demande : "J'ai besoin du fichier situé à `./package.json`"
    
* Buildx répond : Envoie le contenu réel du fichier
    
* BuildKit demande : "J'ai besoin du répertoire `./src/`"
    
* Buildx répond : Envoie tous les fichiers de ce répertoire
    

### Pourquoi cette architecture existe-t-elle ?

#### 1\. Efficacité

L'ancien builder Docker avait un défaut majeur : il copiait toujours l'intégralité de votre contexte de build à l'avance, quel que soit ce qui était réellement nécessaire. Même si votre Dockerfile n'utilisait que quelques fichiers, Docker transférait des centaines de mégaoctets avant de commencer le build.

BuildKit corrige cela grâce aux transferts de fichiers à la demande. Il ne demande que les fichiers spécifiques à chaque étape.

```bash
# Ancien Builder Docker (legacy)
# Copiait toujours l'INTÉGRALITÉ du contexte à l'avance
$ docker build .
Sending build context to Docker daemon  245.7MB  # Tout !

# Nouvelle architecture BuildKit  
# Ne demande les fichiers que si nécessaire
$ docker build .
#1 [internal] load build definition from Dockerfile    0.1s
#2 [internal] load .dockerignore                       0.1s
#3 [1/4] FROM node:18                                  0.5s
#4 [internal] load build context                       0.1s
#4 transferring context: 234B  # Uniquement package.json au début !
#5 [2/4] WORKDIR /app                                  0.2s  
#6 [3/4] COPY package*.json ./                         0.1s
#7 [4/4] RUN npm install                               5.2s
#8 [internal] load build context                       0.3s  
#8 transferring context: 2.1MB  # Demande maintenant les fichiers src/
#9 [5/4] COPY src/ ./src/                              0.2s
```

#### 2\. Évolutivité

L'architecture client-serveur permet des fonctionnalités d'évolutivité. Plusieurs clients Docker CLI peuvent se connecter à la même instance BuildKit, et BuildKit peut s'exécuter sur des serveurs distants plutôt que sur votre machine locale. Cela signifie que vous pourriez exécuter des builds sur un serveur cloud tout en les contrôlant depuis votre ordinateur portable. Les équipes peuvent également déployer plusieurs instances BuildKit pour différentes équipes ou usages, passant du développeur individuel aux grandes entreprises.

#### 3\. Sécurité

La sécurité est améliorée en ne demandant les fichiers sensibles que lorsqu'ils sont explicitement nécessaires. BuildKit ne voit jamais les fichiers que votre Dockerfile ne référence pas, réduisant ainsi la surface d'attaque. Il gère également les identifiants via des canaux sécurisés séparés plutôt que de les mélanger avec votre contexte de build, empêchant les secrets d'être intégrés dans les couches d'image ou exposés dans les logs de build.

### Exemple concret

Traçons une étape de build typique. Vous pouvez trouver le code complet disponible ici : [02-python-cache](https://github.com/Caesarsage/Learn-DevOps-by-building/tree/main/beginner/docker/docker-build-architecture-examples/02-python-cache).

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ ./src/
COPY main.py .
CMD ["python", "main.py"]
```

Voyons ce qui se passe réellement ici :

1. Vous lancez `docker build .`
    
2. Buildx dit à BuildKit :
    

```bash
   "Voici une requête de build avec ce Dockerfile"
```

3. **BuildKit traite** : `FROM python:3.9-slim`
    
    * Aucun fichier client nécessaire, récupère l'image de base
        
4. **BuildKit traite** : `COPY requirements.txt .`
    
    * BuildKit à Buildx : "J'ai besoin de `requirements.txt`"
        
    * Buildx à BuildKit : Envoie le contenu du fichier
        
5. **BuildKit traite** : `RUN pip install -r requirements.txt`
    
    * Aucun fichier client nécessaire, s'exécute à l'intérieur du conteneur
        
6. **BuildKit traite** : `COPY src/ ./src/`
    
    * BuildKit à Buildx : "J'ai besoin de tous les fichiers du répertoire `src/`"
        
    * Buildx à BuildKit : Envoie tous les fichiers de src/
        
7. **BuildKit traite** : `COPY main.py .`
    
    * BuildKit à Buildx : "J'ai besoin de `main.py`"
        
    * Buildx à BuildKit : Envoie le fichier
        
8. BuildKit à Buildx : "Build terminé, voici votre image"
    

D'après l'illustration, vous pouvez voir que BuildKit ne demande que ce dont il a besoin, quand il en a besoin. Pas tout ce contexte :

```bash

my-app/
├── src/                 # ← Chargé uniquement quand COPY src/ s'exécute
├── tests/              # ← Jamais demandé (pas dans le Dockerfile)
├── docs/               # ← Jamais demandé  
├── node_modules/       # ← Jamais demandé (dans .dockerignore)
├── requirements.txt    # ← Chargé tôt (premier COPY)
└── main.py            # ← Chargé plus tard (second COPY)
```

## Fonctionnalités de Docker Build

### Contextes nommés (Named Contexts)

👉 Projet de démo : [07-named-contexts](https://github.com/Caesarsage/Learn-DevOps-by-building/tree/main/beginner/docker/docker-build-architecture-examples/07-named-contexts)

Les contextes nommés vous permettent d'inclure des fichiers provenant de plusieurs sources lors d'un build tout en les gardant logiquement séparés. C'est utile lorsque vous avez besoin de documentation, de fichiers de configuration ou de bibliothèques partagées provenant de différents répertoires ou dépôts dans votre build.

```bash
# Build avec un contexte nommé supplémentaire
docker build --build-context docs=./documentation .
```

```dockerfile
# Utiliser le contexte nommé dans le Dockerfile
FROM alpine
COPY . /app
# Monter les fichiers depuis le contexte nommé
RUN --mount=from=docs,target=/docs \
    cp /docs/manual.pdf /app/
```

### Secrets de build

👉 Projet de démo : [06-build-secrets](https://github.com/Caesarsage/Learn-DevOps-by-building/tree/main/beginner/docker/docker-build-architecture-examples/06-build-secrets)

Les secrets de build vous permettent de transmettre des informations sensibles (comme des clés API ou des mots de passe) à votre build sans les inclure dans l'image finale ou l'historique de build. Les secrets sont montés temporairement lors de commandes `RUN` spécifiques et ne sont jamais stockés dans les couches d'image.

```bash
# Passer un secret au build
echo "api_key=secret123" | docker build --secret id=apikey,src=- .
```

```dockerfile
# Utiliser le secret dans le Dockerfile
FROM alpine
RUN --mount=type=secret,id=apikey \
    export API_KEY=$(cat /run/secrets/apikey) && \
    curl -H "Authorization: $API_KEY" https://api.example.com/data
```

## Contexte de build Docker

### Qu'est-ce qu'un contexte de build ?

Le contexte de build est la collection de fichiers et de répertoires auxquels Docker peut accéder pendant le processus de build. C'est comme rassembler tous vos ingrédients de cuisine sur le comptoir avant de commencer à cuisiner.

```bash
docker build [OPTIONS] CONTEXT
                       ^^^^^^^
                       Ceci est votre contexte de build
```

### Pourquoi les contextes de build sont importants

1. **Sécurité** : Seuls les fichiers du contexte sont accessibles pendant le build
    
2. **Performance** : Les contextes volumineux ralentissent les builds
    
3. **Fonctionnalité** : Votre Dockerfile ne peut utiliser COPY/ADD que pour les fichiers du contexte
    
4. **Efficacité** : Comprendre les contextes vous aide à construire des images plus rapides et plus légères
    

## Types de contextes de build Docker

### 1\. Contexte de répertoire local (Le plus courant)

👉 Voir le code ici : [01-node-local-context](https://github.com/Caesarsage/Learn-DevOps-by-building/tree/main/beginner/docker/docker-build-architecture-examples/01-node-local-context)

C'est ce que vous utiliserez dans 90 % des cas – pointer vers un dossier sur votre machine :

```bash
# Utiliser le répertoire courant
docker build .

# Utiliser un répertoire spécifique
docker build /chemin/vers/mon/projet

# Utiliser le répertoire parent
docker build ..
```

**Exemple de structure de projet :**

```bash
my-webapp/
├── src/
│   ├── index.js
│   └── utils.js
├── public/
│   ├── index.html
│   └── styles.css
├── package.json
├── package-lock.json
├── Dockerfile
├── .dockerignore
└── README.md
```

**Dockerfile correspondant :**

```dockerfile
FROM node:18-alpine
WORKDIR /app

# Copier les fichiers package en premier pour un meilleur cache de couche
COPY package*.json ./
RUN npm ci --only=production

# Copier les sources de l'application
COPY src/ ./src/
COPY public/ ./public/

EXPOSE 3000
CMD ["node", "src/index.js"]
```

### 2\. Contexte de dépôt Git distant

Vous pouvez construire directement à partir de dépôts Git sans clonage local :

```bash
# Build depuis la branche main de GitHub
docker build https://github.com/<username>/project.git

# Build depuis une branche spécifique
docker build https://github.com/<username>/project.git#develop

# Build depuis un répertoire spécifique dans le dépôt
docker build https://github.com/<username>/project.git#main:docker

# Build avec authentification
docker build --ssh default git@github.com:<username>/private-repo.git
```

Cela s'applique à divers cas comme les pipelines CI/CD, la construction de projets open-source, la garantie de builds propres à partir du contrôle de source, les déploiements automatisés, etc.

### 3\. Contexte d'archive Tarball distante

Vous pouvez également construire à partir d'archives compressées hébergées sur des serveurs Web. Une **tarball** distante est un fichier `.tar.gz` ou une archive compressée similaire accessible via HTTP/HTTPS. C'est utile lorsque votre code source est packagé et hébergé sur un serveur Web, un dépôt d'artefacts ou un CDN. Docker télécharge et extrait l'archive automatiquement, utilisant son contenu comme contexte de build.

Cette approche fonctionne bien pour les pipelines CI/CD où les artefacts de build sont stockés de manière centralisée, ou lorsque vous souhaitez construire des images à partir de versions publiées de votre code sans cloner des dépôts entiers.

```bash
# Build depuis une tarball distante
docker build http://server.com/context.tar.gz

# BuildKit télécharge et extrait automatiquement
docker build https://example.com/project-v1.2.3.tar.gz
```

### 4\. Contexte vide (Avancé)

Lorsque vous n'avez besoin d'aucun fichier, vous pouvez envoyer le Dockerfile directement via un pipe :

```bash
# Créer une image sans contexte de fichier
docker build -t hello-world - <<EOF
FROM alpine:latest
RUN echo "Hello, World!" > /hello.txt
CMD cat /hello.txt
EOF
```

## Erreurs courantes de Docker Build (et comment les corriger)

### Erreur 1 : Mauvais répertoire de contexte

👉 Reproduit ici : [04-wrong-context](https://github.com/Caesarsage/Learn-DevOps-by-building/tree/main/beginner/docker/docker-build-architecture-examples/04-wrong-context)

Cette erreur se produit lorsque vous lancez `docker build` depuis le mauvais répertoire, ce qui rend le contexte de build différent de ce que votre Dockerfile attend.

Dans l'exemple, lancer `docker build frontend/` depuis le répertoire `/projects/` signifie que le contexte est `/projects/frontend/`, mais le Dockerfile tente d'accéder à `../shared/utils.js`, qui est en dehors de ce contexte. Docker ne peut accéder qu'aux fichiers situés à l'intérieur du contexte de build, donc toute tentative de référencer des fichiers à l'extérieur échouera.

```bash
# Structure du projet
/projects/
├── frontend/
│   ├── Dockerfile
│   ├── src/
│   └── package.json
└── shared/
    └── utils.js

# MAUVAIS - Exécution depuis le répertoire projects
docker build frontend/
# Cela ne fonctionnera pas si le Dockerfile tente de faire COPY ../shared/utils.js
```

#### Comment corriger un mauvais répertoire de contexte :

La clé est d'aligner votre contexte de build avec les besoins de votre Dockerfile.

* **Option 1** : Changez votre répertoire de travail pour que le contexte corresponde aux attentes de votre Dockerfile. Vous lancez le build depuis l'intérieur de `frontend/`, faisant de ce répertoire la racine du contexte.
    
* **Option 2** : Restez dans le répertoire parent mais définissez-le explicitement comme contexte (l'argument `.`) tout en indiquant à Docker où trouver le Dockerfile avec le flag `-f`. Désormais, `frontend/` et `shared/` sont tous deux accessibles puisqu'ils sont tous deux dans le contexte `/projects/`.
    

```bash
# Option 1 : Lancer depuis le bon répertoire
cd frontend
docker build .

# Option 2 : Utiliser le répertoire parent comme contexte
docker build -f frontend/Dockerfile .
```

### Erreur 2 : Inclusion de fichiers massifs

👉 Version optimisée avec `.dockerignore` : [05-dockerignore-optimization](https://github.com/Caesarsage/Learn-DevOps-by-building/tree/main/beginner/docker/docker-build-architecture-examples/05-dockerignore-optimization)

Cette erreur survient lorsque votre contexte de build contient des fichiers volumineux et inutiles qui ralentissent le processus de build.

Docker doit transférer l'intégralité du contexte au démon de build avant de commencer. L'inclusion de fichiers comme `node_modules` (qui peuvent peser des centaines de Mo), l'historique git, les artefacts de build, les logs et les dumps de base de données rend les builds extrêmement lents. Ces fichiers sont rarement nécessaires dans l'image finale et devraient être exclus.

```bash
# Ce contexte inclut tout !
my-app/
├── node_modules/        # 200Mo+ 
├── .git/               # Historique de version
├── dist/               # Fichiers compilés
├── logs/               # Fichiers de log
├── temp/               # Fichiers temporaires
├── database.dump       # Sauvegarde de base de données de 1Go
└── Dockerfile
```

#### Comment corriger les fichiers massifs dans Docker build :

Utilisez un fichier `.dockerignore` pour exclure les fichiers inutiles, réduisant ainsi considérablement la taille du contexte et le temps de build. Nous en discuterons plus en détail ci-dessous.

### Erreur 3 : Mise en cache des couches inefficace

👉 Voir le code des bonnes pratiques ici : [02-python-cache](https://github.com/Caesarsage/Learn-DevOps-by-building/tree/main/beginner/docker/docker-build-architecture-examples/02-python-cache)

Cette erreur gaspille le système de mise en cache des couches de Docker en copiant des fichiers qui changent fréquemment (comme le code source) avant d'exécuter des opérations coûteuses (comme `npm install`). Lorsque vous modifiez votre code source, Docker invalide le cache pour cette couche et toutes les couches suivantes, forçant `npm install` à s'exécuter à nouveau même si les dépendances n'ont pas changé. Cela peut transformer un build de 5 secondes en un build de 5 minutes.

```dockerfile
# MAUVAIS - Les changements du code source reconstruisent npm install
FROM node:18
COPY . /app
WORKDIR /app
RUN npm install
CMD ["npm", "start"]
```

#### Comment corriger la mise en cache inefficace :

Copiez d'abord les fichiers de dépendances, installez les dépendances, puis copiez le code source. De cette façon, `npm install` ne s'exécute que lorsque `package.json` change réellement :

```dockerfile
# BON - npm install ne se reconstruit que si package.json change
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]
```

## Comment optimiser et surveiller les performances de build

Comprendre les métriques de performance de build vous aide à identifier les goulots d'étranglement et à mesurer les améliorations.

### Comment optimiser les builds Docker avec .dockerignore

Le fichier `.dockerignore` est votre arme secrète pour des builds plus rapides et plus sécurisés. Il indique à Docker quels fichiers exclure du contexte de build.

#### Création de motifs .dockerignore

Créez un fichier `.dockerignore` à la racine de votre projet. La syntaxe est similaire à celle du `.gitignore` : vous pouvez utiliser des jokers (`*`), cibler des extensions spécifiques (`*.log`), exclure des répertoires entiers (`node_modules/`), ou utiliser des motifs de négation (`!important.txt`) pour inclure des fichiers qui seraient autrement exclus. Chaque ligne représente un motif, et les commentaires commencent par `#`.

Exemple d'un fichier .dockerignore :

```bash
# Dépendances
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Sorties de build
dist/
build/
*.tgz

# Contrôle de version
.git/
.gitignore
.svn/

# Fichiers IDE et éditeur
.vscode/
.idea/
*.swp
*.swo
*~

# Fichiers générés par l'OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs et bases de données
*.log
*.sqlite
*.db

# Environnement et secrets
.env
.env.local
.env.*.local
secrets/
*.key
*.pem

# Documentation
README.md
docs/
*.md

# Fichiers de test
test/
tests/
*.test.js
coverage/

# Fichiers temporaires
tmp/
temp/
*.tmp
```

### Mesurer les performances de build

#### Analyser le temps de build

Comprendre où votre build passe du temps aide à identifier les goulots d'étranglement. La sortie détaillée de progression montre le timing pour chaque étape, les succès/échecs de cache (hits/misses) et l'utilisation des ressources.

```bash
# Activer la sortie de progression BuildKit
DOCKER_BUILDKIT=1 docker build --progress=plain .

# Utiliser buildx pour un timing détaillé
docker buildx build --progress=plain .
```

#### Profiler le transfert de contexte

Surveillez le temps de transfert du contexte pour comprendre comment sa taille affecte les performances globales. Identifiez quels répertoires contribuent le plus pour cibler les optimisations `.dockerignore`.

```bash
# Mesurer le temps de transfert du contexte
time docker build --no-cache .

# Profiler la taille du contexte par répertoire
du -sh */ | sort -hr
```

#### Mesurer l'impact du .dockerignore

Avant le `.dockerignore`, vous remarquerez que la taille du `transfering context` est de 245.7Mo en 15.2s :

```bash
$ docker build .
#1 [internal] load build context
#1 transferring context: 245.7MB in 15.2s
```

Après avoir ajouté le fichier .dockerignore, le contexte est réduit à 2.1Mo en 0.3s :

```bash
$ docker build .
#1 [internal] load build context  
#1 transferring context: 2.1MB in 0.3s
```

**Résultat** : Réduction de 99 % de la taille du contexte et transfert 50 fois plus rapide !

## Meilleures pratiques pour les performances de Docker Build

Nous avons couvert plusieurs techniques d'optimisation tout au long de ce guide. Voici un récapitulatif des pratiques clés, plus quelques stratégies supplémentaires :

1. **Mise en cache des couches** (couvert dans l'Erreur 3) : Copiez les fichiers de dépendances avant le code source pour maximiser la réutilisation du cache.
    
2. **Utilisation du .dockerignore** (couvert dans l'Erreur 2) : Excluez les fichiers inutiles pour réduire la taille du contexte et améliorer la vitesse.
    
3. **Choix du bon contexte** (couvert précédemment) : Sélectionnez les types de contexte appropriés (local, Git, tarball) selon votre cas d'usage.
    

Parlons maintenant d'autres moyens d'améliorer les performances :

### Utiliser les builds multi-étapes (Multi-Stage Builds)

👉 Projet de démo : [03-multistage-node](https://github.com/Caesarsage/Learn-DevOps-by-building/tree/main/beginner/docker/docker-build-architecture-examples/03-multistage-node)

Les builds multi-étapes vous permettent d'utiliser une image pour construire/compiler votre application et une image différente, plus petite, pour l'exécuter. Cela réduit considérablement la taille de votre image finale en excluant les outils de build, le code source et d'autres fichiers inutiles de l'image de production.

```dockerfile
# Étape de build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Étape de production
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Utiliser des images de base spécifiques

Les images de base génériques comme `ubuntu:latest` incluent de nombreux paquets dont vous n'avez pas besoin, ce qui rend vos images plus lourdes et plus lentes à télécharger. Des images spécifiques comme `node:18-alpine` ou des images "distroless" ne contiennent que le nécessaire pour l'exécution de votre application.

```dockerfile
# Image de base volumineuse
FROM ubuntu:latest

# Image de base plus petite et spécifique  
FROM node:18-alpine

# Image distroless encore plus petite
FROM gcr.io/distroless/nodejs18-debian11
```

### Combiner les commandes RUN

Chaque commande `RUN` crée une nouvelle couche dans votre image. Plusieurs commandes `RUN` créent plusieurs couches, augmentant la taille de l'image. Combiner les commandes en une seule instruction `RUN` ne crée qu'une seule couche, et vous pouvez nettoyer les fichiers temporaires dans la même étape.

```dockerfile
# Crée plusieurs couches
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get clean

# Couche unique
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

## Dépannage des problèmes de Docker Build

### Problème : "COPY failed: no such file or directory"

**Problème** : Fichier absent du contexte de build  
**Ce qui ne va pas** : Docker ne peut accéder qu'aux fichiers situés dans le contexte de build (le répertoire que vous spécifiez dans `docker build`). Si votre Dockerfile tente de faire un `COPY` sur un fichier qui n'existe pas dans le répertoire du contexte, le build échoue. Cela arrive souvent lors de l'exécution de la commande de build depuis le mauvais répertoire ou quand le chemin du fichier est incorrect par rapport à la racine du contexte.

**Solution** :

```bash
# Vérifiez ce qui se trouve dans votre contexte
ls -la

# Vérifiez le chemin du fichier par rapport au contexte
docker build -t debug . --progress=plain
```

### Problème : "Docker Build is extremely slow"

**Problème** : Contexte de build trop volumineux  
**Ce qui ne va pas** : Docker doit transférer l'intégralité de votre contexte de build au démon BuildKit avant le début du build. Si votre contexte contient des fichiers volumineux, des répertoires comme `node_modules` ou des fichiers inutiles, ce transfert peut prendre des minutes au lieu de secondes. Plus le contexte est grand, plus vos builds sont lents.

**Solution** :

```bash
# Vérifiez la taille du contexte
du -sh .

# Ajoutez plus de motifs au .dockerignore
echo "large-directory/" >> .dockerignore
echo "*.zip" >> .dockerignore
```

### Problème : "Cannot locate specified Dockerfile"

**Problème** : Dockerfile absent de la racine du contexte  
**Ce qui ne va pas** : Par défaut, Docker cherche un fichier nommé `Dockerfile` à la racine de votre contexte de build. Si votre Dockerfile est dans un sous-répertoire ou a un nom différent, Docker ne peut pas le trouver. C'est courant dans les configurations monorepo où les Dockerfiles sont organisés dans des dossiers séparés.

**Solution** :

```bash
# Spécifiez l'emplacement du Dockerfile
docker build -f path/to/Dockerfile .

# Ou déplacez le Dockerfile à la racine du contexte
mv path/to/Dockerfile .
```

### Problème : "Cache misses on unchanged files"

**Problème** : Les horodatages ou les permissions des fichiers ont changé  
**Ce qui ne va pas** : La mise en cache des couches de Docker repose sur les sommes de contrôle (checksums) et les métadonnées des fichiers. Même si le contenu du fichier est inchangé, des horodatages ou des permissions différents peuvent provoquer des échecs de cache, forçant des reconstructions inutiles. Cela arrive souvent après des opérations git, des manipulations du système de fichiers ou lorsque des fichiers sont copiés entre systèmes.

**Solution** :

```bash
# Vérifiez les modifications de fichiers
git status

# Réinitialisez les horodatages
git ls-files -z | xargs -0 touch -r .git/HEAD
```

## **Conclusion**

Comprendre les contextes et l'architecture de build Docker est essentiel pour obtenir des builds plus rapides. Nous avons couvert diverses techniques dans cet article, comme l'optimisation des contextes et les stratégies de cache, la création d'images plus petites avec un empilement efficace des couches et des builds multi-étapes, le maintien d'une meilleure sécurité avec une gestion appropriée des secrets et une surface d'attaque minimale, et l'amélioration de l'expérience développeur grâce à des cycles d'itération plus rapides.

👉 **Les exemples de code complets sont disponibles sur GitHub ici :** [Docker build architecture examples](https://github.com/Caesarsage/Learn-DevOps-by-building/tree/main/beginner/docker/docker-build-architecture-examples)

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).

Pour plus de projets pratiques, suivez et ajoutez une étoile à ce dépôt : [Learn-DevOps-by-building](https://github.com/Caesarsage/Learn-DevOps-by-building)