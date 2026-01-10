---
title: 'Docker Supprimer une Image : Comment Supprimer des Images Docker Expliqué
  avec des Exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-22T21:45:00.000Z'
originalURL: https://freecodecamp.org/news/docker-remove-image-how-to-delete-docker-images-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/DockerErase3.png
tags:
- name: Docker best practices
  slug: docker-best-practices
- name: Docker
  slug: docker
- name: docker image
  slug: docker-image
- name: Productivity
  slug: productivity
seo_title: 'Docker Supprimer une Image : Comment Supprimer des Images Docker Expliqué
  avec des Exemples'
seo_desc: 'By Marcelo Costa

  We live in an era where storage is becoming cheaper everyday. We can just send everything
  to the cloud and pay almost nothing.

  So why would we need to worry about deleting Docker images?

  First of all, there are still some mission cri...'
---

Par Marcelo Costa

Nous vivons à une époque où le stockage devient de moins en moins cher chaque jour. Nous pouvons tout envoyer dans le cloud et payer presque rien.

Alors pourquoi devrions-nous nous soucier de supprimer des images Docker ?

Tout d'abord, il existe encore certaines charges de travail critiques qui ne peuvent pas être déplacées vers le cloud, en particulier celles dans des industries fortement réglementées comme le droit ou la santé.  
  
Mais pour mieux répondre à cette question, je dirais que nous, en tant que développeurs, nous retrouvons souvent à court d'espace sur nos machines locales.

 Faisons une analyse rapide de ce [jeu de données public StackOverflow](https://cloud.google.com/blog/products/gcp/google-bigquery-public-datasets-now-include-stack-overflow-q-a) pour explorer cela plus en détail :

```sql
SELECT tag,
       title,
       answer_count,
       favorite_count,
       score,
       view_count VIEWS
FROM
  (SELECT title,
          answer_count,
          favorite_count,
          view_count,
          score,
          SPLIT(tags, '|') tags
   FROM `bigquery-public-data.stackoverflow.posts_questions` 
         posts_questions), UNNEST(tags) tag
WHERE tag = 'docker'
  AND title LIKE '%space left%'
ORDER BY VIEWS DESC
```

**Résultats de la requête :**

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-21-at-2.11.43-PM.png)

Donc, cela n'arrive pas qu'à moi, n'est-ce pas ? Regardez combien de vues nous avons sur ces publications StackOverflow. Si vous vous demandez, le nombre est de **465687** vues pour les publications correspondant à la requête de recherche.

Heureusement pour nous, aujourd'hui nous allons voir quelques exemples **faciles à utiliser** sur la façon de supprimer nos images Docker inutilisées et sans référence pour nous aider.

## Qu'est-ce que les images Docker sans référence et inutilisées ?

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/07/hanging3.png" alt="drawing" width="300">
</div>

Quelle est la différence entre les images sans référence et inutilisées, pourriez-vous demander ?

Une image sans référence signifie que vous avez créé une nouvelle version de l'image mais que vous ne lui avez pas donné un nouveau nom. Pensez à ces anciennes images oubliées que personne ne sait plus quoi en faire – ce sont des "images sans référence". 

Elles sont laissées sans étiquette et affichent `<none>` sur leur nom lorsque vous exécutez `docker images`.

D'autre part, une image inutilisée signifie qu'elle n'a pas été assignée ou n'est pas utilisée dans un conteneur. 

Par exemple, lorsque vous exécutez `docker ps -a` – il listera tous vos conteneurs actuellement en cours d'exécution ainsi que les conteneurs arrêtés. Toutes les images utilisées à l'intérieur de l'un des conteneurs sont affichées comme "images utilisées", et toutes les autres sont inutilisées.

## Supprimer les Images Docker

Maintenant, voyons quelques exemples de la façon de supprimer des images Docker.

### Notre étude de cas

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/07/busyCat.png" alt="drawing" width="300">
</div>

La Busy Cat Corp est une entreprise fictive qui capture les données de comportement des chats et fournit des recommandations aux propriétaires de chats sur la façon de rendre leurs animaux de compagnie plus occupés et plus heureux.  
  
Toutes leurs charges de travail sont conteneurisées, et elles utilisent les images de base de données suivantes :  
[cassandra](https://hub.docker.com/_/cassandra), [postgres](https://hub.docker.com/_/postgres), [mysql](https://hub.docker.com/_/mysql) et [mongo](https://hub.docker.com/_/mongo).

Leurs développeurs manquent constamment d'espace sur leurs machines, et ils sont des utilisateurs assidus de StackOverflow – ne le sommes-nous pas tous ?  
  
Ils nous ont donc demandé quelques exemples rapides de la façon de supprimer certaines images et de récupérer leur espace.

Commençons par jeter un coup d'œil à la machine de l'un de leurs développeurs.

```bash
docker images
```

**Sortie**

```bash
REPOSITORY  TAG          IMAGE ID            CREATED              SIZE
<none>       <none>      9c872a6119cc        About a minute ago   384MB
mysql        latest      5ac22cccc3ae        43 hours ago         544MB
cassandra    3           9fab0c92a93d        4 days ago           384MB
adoptopenjdk 8-jre...    2bf0172ac69b        4 days ago           210MB
mongo        latest      6d11486a97a7        2 weeks ago          388MB
postgres     latest      b97bae343e06        6 weeks ago          313MB
```

C'est bien, ils ont toutes les images de leurs charges de travail téléchargées. Mais regardez l'espace disque – c'est plus de **2 Go** ! Voyons ce que nous pouvons faire pour eux.

### Supprimer les images Docker sans référence

Nous allons commencer par chercher les images sans référence.

```
docker images -qf "dangling=true"
```

**Sortie**

```bash
REPOSITORY  TAG          IMAGE ID            CREATED              SIZE
<none>       <none>      9c872a6119cc        About a minute ago   384MB
```

Nous en avons une, alors nous allons la supprimer.

**Supprimer l'image sans référence**

```
docker rmi $(docker images -qf "dangling=true")

```

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/flamenco-done.png" alt="drawing" width="300">
</div>

### Supprimer les images Docker inutilisées

Ensuite, nous cherchons les images inutilisées.

```
docker ps -a
```

**Sortie**

```bash
CONTAINER ID  IMAGE   CREATED           NAMES
b6387b343b81  mysql   16 minutes ago    some-mysql
```

Nous n'avons qu'un seul conteneur exécutant l'image `mysql`, donc toutes les autres images sont inutilisées. 

Pour ne pas avoir à le faire manuellement, nous pouvons mettre en place un script qui montre toutes les images inutilisées pour les vérifier.

```bash
# Obtenir toutes les images actuellement utilisées
USED_IMAGES=($( \
    docker ps -a --format '{{.Image}}' | \
    sort -u | \
    uniq | \
    awk -F ':' '$2{print $1":"$2}!$2{print $1":latest"}' \
))

# Obtenir toutes les images actuellement disponibles
ALL_IMAGES=($( \
    docker images --format '{{.Repository}}:{{.Tag}}' | \
    sort -u \
))

# Afficher les images inutilisées
for i in "${ALL_IMAGES[@]}"; do
    UNUSED=true
    for j in "${USED_IMAGES[@]}"; do
        if [[ "$i" == "$j" ]]; then
            UNUSED=false
        fi
    done
    if [[ "$UNUSED" == true ]]; then
        echo "$i n'est pas utilisée."
    fi
done
```

**Sortie**

```bash
adoptopenjdk:8-jre-hotspot-bionic n'est pas utilisée.
cassandra:3 n'est pas utilisée.
mongo:latest n'est pas utilisée.
postgres:latest n'est pas utilisée.
```

Ensuite, il supprime les images inutilisées.

```
# Obtenir toutes les images actuellement utilisées
USED_IMAGES=($( \
    docker ps -a --format '{{.Image}}' | \
    sort -u | \
    uniq | \
    awk -F ':' '$2{print $1":"$2}!$2{print $1":latest"}' \
))

# Obtenir toutes les images actuellement disponibles
ALL_IMAGES=($( \
    docker images --format '{{.Repository}}:{{.Tag}}' | \
    sort -u \
))

# Supprimer les images inutilisées
for i in "${ALL_IMAGES[@]}"; do
    UNUSED=true
    for j in "${USED_IMAGES[@]}"; do
        if [[ "$i" == "$j" ]]; then
            UNUSED=false
        fi
    done
    if [[ "$UNUSED" == true ]]; then
        docker rmi "$i"
    fi
done
```

Après avoir supprimé les images sans référence et inutilisées, nous pouvons voir ce qu'il nous reste.

```bash
docker images
```

**Sortie**

```bash
REPOSITORY  TAG          IMAGE ID            CREATED              SIZE
mysql        latest      5ac22cccc3ae        43 hours ago         544MB
```

Donc, nous n'avons plus que l'image `mysql`, c'est génial !

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/flamenco-done.png" alt="drawing" width="300">
</div>

### Supprimer toutes les images Docker obsolètes avec prune

Ces commandes semblent géniales, mais un deuxième développeur a dit qu'il ne se souciait pas des différences entre les images sans référence et inutilisées. 

Tout ce qu'il voulait, c'était de supprimer les images obsolètes et de récupérer son espace disque.

> Personnellement, c'est ce que je fais habituellement.

Nous pouvons donc simplement utiliser les commandes prune de Docker.

```
# D'abord, supprimer tous les conteneurs arrêtés
docker container prune

# Ensuite, supprimer les images sans référence et inutilisées
docker image prune --all
```

Cela supprimera les images inutilisées et sans référence. En d'autres termes, les images sans au moins un conteneur associé.

Remarque : c'est pourquoi nous avions besoin de supprimer d'abord les conteneurs arrêtés dans le code ci-dessus.

## **Conclusion**

Dans cet article, nous avons vu comment supprimer des images Docker, et nous avons utilisé une entreprise fictive pour l'expliquer avec quelques exemples faciles à utiliser.

Il est important de souligner que vous ne devriez pas utiliser Docker pour conserver un historique de vos anciennes images. Pour un environnement de développement, c'est bien, et vous pouvez même automatiser la charge de travail de nettoyage des images si vous devez gérer beaucoup d'entre elles. 

Mais pour une charge de travail de production, vous devriez utiliser une solution de registre de conteneurs pour gérer vos images Docker. 

Il existe de nombreuses solutions de registre de conteneurs, comme Google Cloud Platform avec [Artifact Registry](https://cloud.google.com/artifact-registry) et Docker Enterprise avec [Docker Trusted Registry](https://docs.mirantis.com/docker-enterprise/v3.0/dockeree-products/dtr.html). Et si vous êtes dans le monde de l'open source, vous pouvez simplement utiliser [Docker Hub](https://hub.docker.com/) :).  
  
Merci d'avoir lu !

* Illustrations de [Icons8](https://icons8.com/)

Si vous avez trouvé cela utile, ou si vous souhaitez contester ou étendre quelque chose soulevé ici, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/mesmacosta) ou [Linkedin](https://www.linkedin.com/in/mesmacosta). Restons en contact !