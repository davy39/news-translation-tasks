---
title: Comment gérer les secrets dans Docker
subtitle: ''
author: Abraham Dahunsi
co_authors: []
series: null
date: '2024-01-03T16:26:00.000Z'
originalURL: https://freecodecamp.org/news/manage-secrets-in-docker
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/feature-image.jpg
tags:
- name: Docker
  slug: docker
- name: Security
  slug: security
seo_title: Comment gérer les secrets dans Docker
seo_desc: 'Protecting sensitive data like API keys, passwords, and certificates in
  your Docker projects can be quite daunting and error-prone. And many devs neglect
  it when dealing with applications deployed in containers.

  There is no global way of storing and ...'
---

Protéger les données sensibles comme les clés API, les mots de passe et les certificats dans vos projets Docker peut être assez intimidant et sujet aux erreurs. Et de nombreux développeurs le négligent lorsqu'ils traitent avec des applications déployées dans des conteneurs.

Il n'existe pas de méthode universelle pour stocker et partager des secrets dans des conteneurs. Les méthodes traditionnelles de stockage, telles que les coder en dur dans le code source et les cacher dans des fichiers texte, les rendent vulnérables à l'exposition et à l'exploitation.

Docker Secrets a été introduit pour répondre à ce problème. Docker Secrets offre un moyen sécurisé de stocker vos données sensibles, protégeant vos applications des pièges du stockage négligent.

Dans cet article, vous apprendrez ce que sont les secrets Docker et leurs structures par défaut. Je vous guiderai également à travers les étapes pour gérer les secrets dans Docker afin de protéger vos données sensibles et de libérer tout le potentiel de vos applications Docker.

## Qu'est-ce que les secrets Docker ?

Pour gérer efficacement les secrets, vous devez d'abord comprendre ce qu'ils sont. Les secrets Docker incluent une large gamme de données sensibles, notamment :

* Les identifiants tels que les noms d'utilisateur et les mots de passe pour les bases de données, les serveurs, les services tiers, et plus encore.

* Les clés API, qui sont des clés uniques permettant l'accès à des API et services externes.

* Les certificats numériques, utilisés pour la communication sécurisée et l'authentification, tels que les certificats SSL/TLS.

* Les clés de chiffrement, utilisées pour chiffrer des données ou des fichiers sensibles.

* Les jetons, tels que les jetons d'accès pour l'authentification et l'autorisation.

* Les licences logicielles qui peuvent contenir des informations sensibles.

* Autres données sensibles qui pourraient poser un risque de sécurité si elles étaient exposées.

### Comment les secrets sont stockés

Docker offre plusieurs méthodes pour créer et référencer des secrets dans votre environnement conteneurisé :

* Fichiers : Vous pouvez stocker des secrets dans des fichiers en texte brut, mais cette méthode est moins sécurisée et non recommandée pour les environnements de production.

* Variables d'environnement : Vous pouvez définir des secrets comme variables d'environnement dans les conteneurs, mais cela peut encore les exposer dans les logs et les listes de processus.

* Docker Secrets : Vous pouvez utiliser la fonctionnalité de gestion des secrets intégrée de Docker pour un chiffrement de base et un contrôle d'accès.

* Docker Compose : Vous pouvez définir des secrets dans vos fichiers Docker Compose pour une gestion pratique pendant le développement et les tests.

* Docker Swarm Secrets : Vous pouvez exploiter des capacités avancées de gestion des secrets pour les environnements Docker en cluster, offrant un stockage sécurisé et un contrôle d'accès granulaire.

## Solutions pour gérer les secrets clés

Docker offre deux principales méthodes pour gérer vos données sensibles : des solutions intégrées au sein de la plateforme elle-même et des solutions externes pour des besoins plus avancés.

### Solutions intégrées

Pour ceux qui débutent ou recherchent une gestion basique des secrets, les solutions intégrées de Docker offrent un point d'entrée pratique (ce guide est basé sur les solutions intégrées) :

* Docker Secrets : Cette méthode légère permet de créer et d'injecter des secrets de base dans des conteneurs via la CLI ou des fichiers Compose. Bien que facile à utiliser, elle manque de fonctionnalités avancées comme le stockage centralisé et le contrôle d'accès granulaire. Elle est mieux adaptée aux déploiements simples avec un minimum de secrets.

* Docker Swarm Secrets : Pour les environnements en cluster, les secrets Swarm offrent une sécurité accrue. Les secrets résident en toute sécurité sur les gestionnaires Swarm et sont distribués aux nœuds à la demande. Vous obtenez un contrôle d'accès granulaire et des traces d'audit, ce qui en fait une solution idéale pour les déploiements de production avec plusieurs secrets.

### Solutions externes

Pour une sécurité robuste et des fonctionnalités avancées, les plateformes externes de gestion des secrets se distinguent. Voici quelques options populaires :

* Vault : Une plateforme open-source riche en fonctionnalités offrant le chiffrement, le contrôle d'accès, la journalisation et les traces d'audit. Elle s'intègre parfaitement avec divers outils et plateformes, ce qui en fait un choix polyvalent pour les déploiements complexes.

* Keywhiz : Une autre option open-source, Keywhiz, se concentre sur la facilité d'utilisation et les déploiements natifs dans le cloud. Son design léger en fait une solution idéale pour gérer les secrets dans les environnements Kubernetes.

* AWS Secrets Manager : Si vous êtes utilisateur d'AWS, ce service natif offre un stockage sécurisé, une rotation et une récupération des secrets, s'intégrant parfaitement à votre infrastructure existante.

* Options Cloud Native : La plupart des principaux fournisseurs de cloud proposent des services dédiés de gestion des secrets comme Azure Key Vault et GCP Secret Manager. Ceux-ci tirent parti de la sécurité et de l'évolutivité de leurs plateformes respectives pour une gestion sécurisée et rationalisée.

### Comment choisir la bonne solution

L'approche optimale dépend de vos besoins spécifiques ou de ceux de votre équipe, ainsi que de votre environnement. Prenez en compte ces facteurs :

* Complexité de l'application : Les applications complexes avec de nombreux secrets nécessitent probablement les fonctionnalités avancées d'une solution externe.

* Environnement de déploiement : Les environnements de production exigent une sécurité robuste et un contrôle d'accès, favorisant les options externes.

* Expertise de l'équipe : Évaluez la familiarité de votre équipe avec la gestion et l'intégration d'outils externes.

* Besoins d'évolutivité : Si vous envisagez de faire évoluer votre infrastructure conteneurisée, choisissez des solutions qui répondent aux déploiements multi-nœuds.

Rappelez-vous, il n'existe pas d'approche universelle. Priorisez les pratiques sécurisées pour la création, le stockage, la rotation et la suppression des secrets, quelle que soit la méthode choisie.

## Comment commencer avec la gestion des secrets

Maintenant, passons à la pratique, car je vais vous montrer comment créer et gérer des secrets Docker.

### Comment créer un secret Docker

Commencez par créer un fichier avec un secret, comme un fichier contenant votre mot de passe :

```bash
$ echo yourpassword > password.txt
```

Ensuite, créez l'objet secret Docker en utilisant la commande `docker secret` :

```bash
$ docker secret create your_secret ./path/to/password.txt
```

Dans le processus de création et de gestion des secrets Docker, vous commencez par générer un fichier contenant un secret, tel qu'un mot de passe, en utilisant la commande `echo` et en l'enregistrant dans un fichier (comme `password.txt`).

Après cela, vous utilisez la commande `docker secret create` pour établir un objet secret Docker nommé `your_secret` à partir du contenu du fichier spécifié (`./path/to/password.txt`). Cette séquence de commandes permet la création et le stockage d'informations confidentielles, comme des mots de passe, dans votre environnement Docker de manière sécurisée.

### Comment initier un service utilisant le secret

Maintenant, pour créer un service qui utilise le secret, utilisez ce modèle :

```bash
$ docker service create --name <service_name>  --secret <secret_name>   <image_name>:<tag>
```

La commande `docker service create` commence la création d'un nouveau service au sein d'un cluster Docker Swarm. Pour personnaliser et configurer le service, plusieurs options sont disponibles :

1. `--name <service_name>` : Assigne un nom spécifique au service, aidant à son identification facile. Par exemple, `--name my-nginx-service` désigne le service comme `my-nginx-service`.

2. `--secret <secret_name>` : Utilise un secret Docker Swarm existant dans le service. Cela permet au secret d'être accessible dans les conteneurs associés au service. Par exemple, `--secret your_secret` associe le secret `your_secret` au service.

3. `<image_name>:<tag>` : Spécifie l'image Docker à utiliser pour le service, y compris son tag. Par exemple, `<image_name>:<tag>` peut être remplacé par `nginx:latest` pour utiliser la dernière version de l'image Nginx pour le service.

## Comment gérer les secrets Docker

### Comment lister les secrets Docker

Vous pouvez consulter la liste des secrets Docker disponibles en utilisant la commande `Docker ls` :

```bash
$ docker secret ls
```

Voici à quoi devrait ressembler la sortie :

![Screenshot-2023-12-23-171215-1](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-23-171215-1.png align="left")

Cette commande ne fournit pas d'informations complètes sur vos secrets Docker, car seules les métadonnées sont affichées. Pour inspecter les métadonnées d'un secret spécifique, utilisez la commande `Docker Inspect` :

```bash
$ docker secret inspect <secret_name> #utilisez 'your_secret' pour cet exemple
```

Lorsqu'elle est exécutée, elle fournit une sortie complète qui inclut les métadonnées du secret spécifié, telles que son ID, sa version et ses labels. De plus, elle affiche les horodatages de création et de mise à jour du secret. Cette commande d'inspection est précieuse pour les administrateurs et les développeurs cherchant à comprendre les propriétés et les attributs d'un secret Docker, aidant à une gestion et une utilisation efficaces au sein du cluster Docker Swarm.

Cependant, les secrets Docker privilégient la sécurité, et révéler leur contenu via des commandes CLI compromettrait leur intégrité. Pour accéder au contenu du secret, il doit être attaché à un service au sein de votre Docker Swarm. Par la suite, le secret devient accessible en tant que fichier au sein des conteneurs associés à ce service.

#### Comment supprimer les secrets Docker

Pour supprimer et effacer les secrets Docker inutilisés, utilisez la commande `docker secret rm` :

```bash
$ docker secret rm your_secret
```

Rappelez-vous, cette action est irréversible, alors assurez-vous de vérifier votre choix !

## Comment utiliser les secrets Docker avec Docker Compose

Si vous n'êtes pas un grand fan de l'utilisation de l'interface de ligne de commande, ne vous inquiétez pas, car vous pouvez toujours utiliser les fichiers Docker Compose pour gérer les secrets Docker.

```yaml
version: '3.1'

services:
  web:
    image: nginxdemos/hello
    secrets:
      - your_secret
      - your_external_secret
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./conf/nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web

secrets:
  your_file_secret:
    file:  ./path/to/password.txt
  your_external_secret:
    external: true
```

Cette configuration YAML est un fichier Docker Compose, spécifiant la configuration pour deux services - `web` et `nginx` - ainsi que certaines configurations et secrets associés.

Permettez-moi de décomposer ce que j'ai fait.

### Configuration des services

Le service `web` utilise l'image `nginxdemos/hello` et inclut deux secrets : `your_secret` et `your_external_secret`.

Le service `nginx` utilise l'image `nginx:latest` et mappe le port 80 de l'hôte au port 80 du conteneur.

De plus, il monte le fichier local `./conf/nginx.conf` dans le conteneur à `/etc/nginx/nginx.conf` et dépend du service `web`, ce qui signifie que `web` doit être en cours d'exécution avant que `nginx` ne démarre.

### Configuration des secrets

Il y a deux secrets définis.

Le premier est `your_file_secret`, qui lit le contenu de `./path/to/password.txt` et crée un secret à partir de celui-ci.

Le second est `your_external_secret`, qui spécifie que ce secret est externe. Cela implique que le contenu réel du secret est géré en externe, et la configuration ici est une référence à ce secret externe.

En résumé, cet exemple de fichier Docker Compose configure deux services, `web` et `nginx`, avec le service `nginx` dépendant de `web`. Les secrets, à la fois à partir de fichiers (`your_file_secret`) et de sources externes (`your_external_secret`), sont utilisés pour le traitement sécurisé des informations sensibles au sein des services. Le service `nginx` a également des configurations supplémentaires liées à la cartographie des ports et au montage des volumes.

## Bonnes pratiques

Voici quelques conseils et bonnes pratiques à suivre lors de l'utilisation de Docker Secrets.

### Comment choisir une méthode

Le choix de la bonne méthode dépend de plusieurs facteurs :

* Besoins de l'application : Considérez la complexité de votre application et ses exigences de sécurité. Les applications simples peuvent prospérer avec les secrets Docker intégrés, tandis que les déploiements complexes peuvent nécessiter une solution externe.

* Infrastructure : Analysez votre infrastructure et vos outils existants. Si vous utilisez déjà des plateformes cloud spécifiques ou des moteurs d'orchestration, leurs solutions natives de gestion des secrets peuvent offrir une intégration transparente et une familiarité.

* Contrôle souhaité : Évaluez votre besoin de fonctionnalités avancées comme le contrôle d'accès granulaire, la rotation automatisée et la gestion centralisée. Les solutions externes offrent généralement un meilleur contrôle par rapport aux options intégrées.

### Comment sécuriser la création et le stockage des secrets

La base de la gestion sécurisée des secrets réside dans la protection des données elles-mêmes :

* Chiffrement : Implémentez le chiffrement pour les secrets à la fois au repos (stockés sur disque) et en transit (transmis entre les systèmes). Utilisez des algorithmes de chiffrement robustes et les meilleures pratiques de gestion des clés.

* Contrôle d'accès : Appliquez le principe du moindre privilège. Accordez l'accès aux secrets uniquement sur une base de besoin de savoir. Envisagez d'employer des mécanismes de contrôle d'accès basé sur les rôles (RBAC) pour un contrôle granulaire.

### Rotation des secrets et gestion du cycle de vie

Prévenir la compromission d'un seul secret peut réduire considérablement le risque. Employez ces mesures :

* Rotation : Faites tourner régulièrement vos secrets, même s'ils n'ont pas été exposés. Définissez des calendriers de rotation automatisés basés sur les meilleures pratiques et vos besoins spécifiques en matière de sécurité.

* Gestion du cycle de vie : Implémentez des processus de suppression sécurisés pour les secrets obsolètes ou inutilisés. Évitez de simplement supprimer des fichiers, car des outils de récupération de données pourraient encore y accéder. Les méthodes de suppression sécurisées offrent une approche plus sûre.

### Comment intégrer les secrets avec les pipelines CI/CD

Incorporez la gestion des secrets de manière transparente dans votre flux de travail de développement :

* Techniques d'injection : Utilisez des variables d'environnement, des outils d'injection dynamique de secrets ou des montages de fichiers pour fournir des secrets aux conteneurs uniquement lorsque cela est nécessaire. Cela évite leur stockage dans les images de conteneurs.

* Gestion automatisée des identifiants : Intégrez votre solution de gestion des secrets choisie avec votre pipeline CI/CD pour automatiser la récupération, la rotation et l'injection des identifiants dans le cadre de votre processus de déploiement.

* Minimiser l'exposition : Évitez de logger les secrets en texte brut pendant les étapes de construction ou de déploiement. Implémentez des techniques de masquage ou utilisez des outils qui gèrent les secrets de manière sécurisée dans votre pipeline CI/CD.

En utilisant ces bonnes pratiques et en les adaptant à vos besoins spécifiques, vous pouvez construire une base robuste et sécurisée pour gérer vos secrets Docker.

Rappelez-vous, la solution que vous choisissez n'est qu'une pièce du puzzle. Une vigilance constante, le respect des bonnes pratiques et des audits de sécurité réguliers sont cruciaux pour maintenir une défense résiliente contre les menaces potentielles.

## Ressources supplémentaires

Voici quelques ressources supplémentaires à utiliser si vous souhaitez en savoir plus sur les secrets Docker et d'autres pratiques de sécurité :

* [Documentation Docker](https://docs.docker.com/) Guides officiels pour les secrets Docker et les pratiques sécurisées.

* Guides des plateformes de gestion des secrets : Chaque solution fournit une documentation et des tutoriels extensifs.

    * [Guide officiel de la documentation Docker sur la gestion des secrets Docker (à lire pour des connaissances plus approfondies)](https://docs.docker.com/engine/swarm/secrets/)

    * [Un guide pour utiliser une solution externe : Vault](https://developer.hashicorp.com/vault/doc)

    * [Un guide pour AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

* Forums communautaires et blogs : Engagez-vous activement avec les communautés de sécurité et Docker pour un apprentissage et un soutien supplémentaires.

    * [Stackoverflow](https://stackoverflow.com/)

    * [La page de blog officielle de la Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/blog/)

## Conclusion

Maintenant, dans ce guide, vous avez appris ce que sont les secrets Docker, comment ils sont stockés, les différentes méthodes de stockage et comment gérer les secrets Docker dans vos projets personnels.

Rappelez-vous, les secrets sécurisés sont les pierres angulaires des applications sécurisées. Construisez votre forteresse avec sagesse, et vos données resteront en sécurité.

N'hésitez pas à demander si vous avez des questions spécifiques sur l'un de ces aspects !

De plus, si vous avez aimé ce guide et l'avez trouvé instructif, assurez-vous de le partager avec vos collègues et vos communautés en ligne.