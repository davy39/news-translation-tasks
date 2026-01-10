---
title: Comment héberger soi-même un registre de conteneurs
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2024-10-15T17:28:30.531Z'
originalURL: https://freecodecamp.org/news/how-to-self-host-a-container-registry
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728918386211/cf6fd053-453e-4257-abcd-16942c345845.png
tags:
- name: Docker
  slug: docker
- name: containers
  slug: containers
- name: Linux
  slug: linux
- name: nginx
  slug: nginx
- name: SSL
  slug: ssl
seo_title: Comment héberger soi-même un registre de conteneurs
seo_desc: 'A container registry is a storage catalog from where you can push and pull
  container images.

  There are many public and private registries available to developers such as Docker
  Hub, Amazon ECR, and Google Cloud Artifact Registry. But sometimes, inste...'
---

Un registre de conteneurs est un catalogue de stockage à partir duquel vous pouvez pousser et tirer des images de conteneurs.

Il existe de nombreux registres publics et privés disponibles pour les développeurs tels que [Docker Hub](https://hub.docker.com/), [Amazon ECR](https://aws.amazon.com/ecr/) et [Google Cloud Artifact Registry](https://cloud.google.com/artifact-registry/docs). Mais parfois, au lieu de dépendre d'un fournisseur externe, vous pourriez vouloir héberger vos images vous-même. Cela vous donne plus de contrôle sur la façon dont le registre est configuré et où les images de conteneurs sont hébergées.

Cet article est un tutoriel pratique qui vous apprendra à héberger vous-même un registre de conteneurs.

## Table des matières

* [Qu'est-ce qu'une image de conteneur ?](#heading-quest-ce-quune-image-de-conteneur)
    
* [Qu'est-ce qu'un registre de conteneurs ?](#heading-quest-ce-quun-registre-de-conteneurs)
    
* [Pourquoi vous pourriez vouloir héberger vous-même un registre de conteneurs](#heading-pourquoi-vous-pourriez-voir-heberger-vous-meme-un-registre-de-conteneurs)
    
* [Comment héberger soi-même un registre de conteneurs](#heading-comment-heberger-soi-meme-un-registre-de-conteneurs)
    
* [Étape 1 : Installer Docker et Docker Compose sur le serveur](#heading-etape-1-installer-docker-et-docker-compose-sur-le-serveur)
    
* [Étape 2 : Configurer et exécuter le conteneur de registre](#heading-etape-2-configurer-et-executer-le-conteneur-de-registre)
    
* [Étape 3 : Exécuter NGINX pour gérer le TLS](#heading-etape-3-executer-nginx-pour-gerer-le-tls)
    
* [Prêt à partir !](#heading-pret-a-partir)
    
* [Autres options](#heading-autres-options)
    
* [Conclusion](#heading-conclusion)
    

Vous tirerez le meilleur parti de cet article si vous êtes déjà familiarisé avec les outils comme Docker et NGINX, et si vous avez une compréhension générale de ce qu'est un conteneur.

## Qu'est-ce qu'une image de conteneur ?

Avant de parler des registres de conteneurs, comprenons d'abord ce qu'est une image de conteneur. En résumé, une image de conteneur est un package qui inclut tous les fichiers, bibliothèques et configurations pour exécuter un conteneur. Elles sont composées de [couches](https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/) où chaque couche représente un ensemble de changements du système de fichiers qui ajoutent, suppriment ou modifient des fichiers.

La manière la plus courante de créer une image de conteneur est d'utiliser un **Dockerfile**.

```bash
# construire une image
docker build -t pliutau/hello-world:v0 .

# vérifier les images localement
docker images
# REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
# hello-world   latest    9facd12bbcdd   22 seconds ago   11MB
```

Cela crée une image de conteneur qui est stockée sur votre machine locale. Mais que faire si vous voulez partager cette image avec d'autres ou l'utiliser sur une machine différente ? C'est là que les registres de conteneurs interviennent.

## Qu'est-ce qu'un registre de conteneurs ?

Un registre de conteneurs est un catalogue de stockage où vous pouvez pousser et tirer des images de conteneurs. Les images sont regroupées en dépôts, qui sont des collections d'images liées avec le même nom. Par exemple, sur le registre Docker Hub, [nginx](https://hub.docker.com/_/nginx) est le nom du dépôt qui contient différentes versions des images NGINX.

Certains registres sont publics, ce qui signifie que les images hébergées sur eux sont accessibles à quiconque sur Internet. Les registres publics tels que [Docker Hub](https://hub.docker.com/) sont une bonne option pour héberger des projets open-source.

D'autre part, les registres privés offrent un moyen d'incorporer la sécurité et la confidentialité dans le stockage des images de conteneurs d'entreprise, hébergées dans le cloud ou sur site. Ces registres privés viennent souvent avec des fonctionnalités de sécurité avancées et un support technique.

Il existe une liste croissante de registres privés disponibles tels que [Amazon ECR](https://aws.amazon.com/ecr/), [GCP Artifact Registry](https://cloud.google.com/artifact-registry/docs), [GitHub Container Registry](https://github.com/features/packages), et Docker Hub offre également une fonctionnalité de dépôt privé.

En tant que développeur, vous interagissez avec un registre de conteneurs lorsque vous utilisez les commandes `docker push` et `docker pull`.

```bash
docker push docker.io/pliutau/hello-world:v0

# Dans le cas de Docker Hub, nous pourrions également omettre la partie registre
docker push pliutau/hello-world:v0
```

Examinons l'anatomie d'une URL d'image de conteneur :

```bash
docker pull docker.io/pliutau/hello-world:v0@sha256:dc11b2...
                |            |            |          |
                                                  
             registre    dépôt      tag       digest
```

## Pourquoi vous pourriez vouloir héberger vous-même un registre de conteneurs

Parfois, au lieu de dépendre d'un fournisseur comme AWS ou GCP, vous pourriez vouloir héberger vos images vous-même. Cela garde votre infrastructure interne et vous rend moins dépendant des fournisseurs externes. Dans certaines industries fortement réglementées, cela est même une exigence.

Un registre auto-hébergé fonctionne sur vos propres serveurs, vous donnant plus de contrôle sur la façon dont le registre est configuré et où les images de conteneurs sont hébergées. En même temps, cela implique un coût de maintenance et de sécurisation du registre.

## Comment héberger soi-même un registre de conteneurs

Il existe plusieurs solutions de registre de conteneurs open-source disponibles. La plus populaire est officiellement soutenue par Docker, appelée [registry](https://hub.docker.com/_/registry), avec son implémentation pour le stockage et la distribution d'images et d'artifacts de conteneurs. Cela signifie que vous pouvez exécuter votre propre registre à l'intérieur d'un conteneur.

Voici les principales étapes pour exécuter un registre sur un serveur :

* Installer Docker et Docker Compose sur le serveur.
    
* Configurer et exécuter le conteneur **registry**.
    
* Exécuter **NGINX** pour gérer le TLS et transférer les requêtes au conteneur de registre.
    
* Configurer les certificats SSL et un domaine.
    

### Étape 1 : Installer Docker et Docker Compose sur le serveur

Vous pouvez utiliser n'importe quel serveur qui supporte Docker. Par exemple, vous pouvez utiliser un Droplet DigitalOcean avec Ubuntu. Pour cette démonstration, j'ai utilisé Google Cloud Compute pour créer une VM avec Ubuntu.

```bash
neofetch

# OS: Ubuntu 20.04.6 LTS x86_64
# CPU: Intel Xeon (2) @ 2.200GHz
# Memory: 3908MiB
```

Une fois que nous sommes dans notre VM, nous devons installer Docker et Docker Compose. Docker Compose est optionnel, mais il facilite la gestion des applications multi-conteneurs.

```bash
# installer le moteur docker et docker-compose
sudo snap install docker

# vérifier l'installation
docker --version
docker-compose --version
```

### Étape 2 : Configurer et exécuter le conteneur de registre

Ensuite, nous devons configurer notre conteneur de registre. Le fichier **compose.yaml** suivant créera un conteneur de registre avec un volume pour stocker les images et un volume pour stocker le fichier de mot de passe.

```yaml
services:
  registry:
    image: registry:latest
    environment:
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: Registry Realm
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/registry.password
      REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY: /data
    volumes:
      # Monter le fichier de mot de passe
      - ./registry/registry.password:/auth/registry.password
      # Monter le répertoire de données
      - ./registry/data:/data
    ports:
      - 5000
```

Le fichier de mot de passe défini dans **REGISTRY\_AUTH\_HTPASSWD\_PATH** est utilisé pour authentifier les utilisateurs lorsqu'ils poussent ou tirent des images du registre. Nous devons créer un fichier de mot de passe en utilisant la commande **htpasswd**. Nous devons également créer un dossier pour stocker les images.

```yaml
mkdir -p ./registry/data

# installer htpasswd
sudo apt install apache2-utils

# créer un fichier de mot de passe. nom d'utilisateur : busy, mot de passe : bee
htpasswd -Bbn busy bee > ./registry/registry.password
```

Maintenant, nous pouvons démarrer le conteneur de registre. Si vous voyez ce message, tout fonctionne comme il se doit :

```yaml
docker-compose up

# une exécution réussie devrait afficher quelque chose comme ceci :
# registry | level=info msg="listening on [::]:5000"
```

### Étape 3 : Exécuter NGINX pour gérer le TLS

Comme mentionné précédemment, nous pouvons utiliser NGINX pour gérer le TLS et transférer les requêtes au conteneur de registre.

Le registre Docker nécessite un certificat SSL valide et de confiance pour fonctionner. Vous pouvez utiliser quelque chose comme [Let's Encrypt](https://letsencrypt.org/) ou l'obtenir manuellement. Assurez-vous d'avoir un nom de domaine pointant vers votre serveur (**registry.pliutau.com** dans mon cas). Pour cette démonstration, j'ai déjà obtenu les certificats en utilisant [certbot](https://certbot.eff.org/) et je les ai placés dans le répertoire **./nginx/certs**.

Puisque nous exécutons notre registre Docker dans un conteneur, nous pouvons également exécuter NGINX dans un conteneur en ajoutant le service suivant au fichier **compose.yaml** :

```yaml
services:
  registry:
    # ...
  nginx:
    image: nginx:latest
    depends_on:
      - registry
    volumes:
      # monter la configuration nginx
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      # monter les certificats obtenus de Let's Encrypt
      - ./nginx/certs:/etc/nginx/certs
    ports:
      - "443:443"
```

Notre fichier **nginx.conf** pourrait ressembler à ceci :

```yaml
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    upstream registry {
        server registry:5000;
    }

    server {
        server_name registry.pliutau.com;
        listen 443 ssl;

        ssl_certificate /etc/nginx/certs/fullchain.pem;
        ssl_certificate_key /etc/nginx/certs/privkey.pem;

        location / {
            # paramètre important pour les grandes images
            client_max_body_size                1000m;

            proxy_pass                          http://registry;
            proxy_set_header  Host              $http_host;
            proxy_set_header  X-Real-IP         $remote_addr;
            proxy_set_header  X-Forwarded-For   $proxy_add_x_forwarded_for;
            proxy_set_header  X-Forwarded-Proto $scheme;
            proxy_read_timeout                  900;
        }
    }
}
```

### Prêt à partir !

Après ces étapes, nous pouvons exécuter nos conteneurs de registre et Nginx.

```bash
docker-compose up
```

Maintenant, côté client, vous pouvez pousser et tirer les images de votre registre. Mais d'abord, nous devons nous connecter au registre.

```bash
docker login registry.pliutau.com

# Nom d'utilisateur : busy
# Mot de passe : bee
# Connexion réussie
```

Il est temps de construire et de pousser notre image vers notre registre auto-hébergé :

```bash
docker build -t registry.pliutau.com/pliutau/hello-world:v0 .

docker push registry.pliutau.com/pliutau/hello-world:v0
# v0: digest: sha256:a56ea4... size: 738
```

Sur votre serveur, vous pouvez vérifier les images téléchargées dans le dossier de données :

```bash
ls -la ./registry/data/docker/registry/v2/repositories/
```

### Autres options

En suivant l'exemple ci-dessus, vous pouvez également exécuter le registre sur Kubernetes. Ou vous pourriez utiliser un service de registre géré comme [Harbor](https://goharbor.io/), qui est un registre open-source qui fournit des fonctionnalités de sécurité avancées et est compatible avec Docker et Kubernetes.

De plus, si vous voulez avoir une interface utilisateur pour votre registre auto-hébergé, vous pourriez utiliser un projet comme [joxit/docker-registry-ui](https://github.com/Joxit/docker-registry-ui) et l'exécuter dans un conteneur séparé.

## Conclusion

Les registres de conteneurs auto-hébergés vous permettent d'avoir un contrôle complet sur votre registre et la manière dont il est déployé. En même temps, cela implique un coût de maintenance et de sécurisation du registre.

Quelles que soient vos raisons de faire fonctionner un registre auto-hébergé, vous savez maintenant comment le faire. À partir de là, vous pouvez comparer les différentes options et choisir celle qui correspond le mieux à vos besoins.

Vous pouvez trouver le code source complet de cette démonstration sur [GitHub](https://github.com/plutov/packagemain/tree/master/26-self-hosted-container-registry). De plus, vous pouvez le regarder sous forme de vidéo sur [notre chaîne YouTube](https://www.youtube.com/watch?v=TGLfQZ9qRaI).