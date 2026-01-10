---
title: Comment obtenir une adresse IP de conteneur Docker - Expliqué avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-22T21:54:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-a-docker-container-ip-address-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a19740569d1a4ca2384.jpg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Comment obtenir une adresse IP de conteneur Docker - Expliqué avec des
  exemples
seo_desc: 'By Marcelo Costa

  Docker provides the ability to package and run an application in a loosely isolated
  environment called a container.

  I know what you might be thinking – come on, not another post explaining what Docker
  is, it''s everywhere these days!

  ...'
---

Par Marcelo Costa

Docker offre la possibilité d'empaqueter et d'exécuter une application dans un environnement faiblement isolé appelé conteneur.

Je sais ce que vous pourriez penser – allez, pas un autre article expliquant ce qu'est Docker, c'est partout ces jours-ci !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/docker-i-see.jpg)

Mais ne vous inquiétez pas, nous allons sauter cette introduction basique. Le public cible de cet article devrait déjà avoir une compréhension de base de ce que sont Docker et les conteneurs.

Mais vous êtes-vous déjà demandé comment obtenir une adresse IP de conteneur Docker ?

## Réseau Docker expliqué

Tout d'abord, comprenons comment fonctionne le réseau Docker. Pour cela, nous allons nous concentrer sur le réseau `bridge` par défaut. Lorsque vous utilisez Docker, si vous ne spécifiez pas de pilote, c'est le type de réseau que vous utilisez.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/docker-network.png)
_Réseau Docker, image de [understanding-docker-networking-drivers-use-cases](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)_

Le réseau `bridge` fonctionne comme un réseau privé interne à l'hôte afin que les conteneurs puissent communiquer. L'accès externe est accordé en exposant des ports aux conteneurs.

Les réseaux bridge sont utilisés lorsque vos applications s'exécutent dans des conteneurs autonomes qui doivent communiquer.

Dans l'image ci-dessus, `db` et `web` peuvent communiquer entre eux sur un réseau bridge créé par l'utilisateur appelé `mybridge`.

Si vous n'avez jamais ajouté de réseau dans Docker, vous devriez voir quelque chose de similaire à ceci :

```bash
$ docker network ls

NETWORK ID          NAME                  DRIVER              SCOPE
c3cd46f397ce        bridge                bridge              local
ad4e4c24568e        host                  host                local
1c69593fc6ac        none                  null                local
```

Le réseau `bridge` par défaut est listé, ainsi que `host` et `none`. Nous allons ignorer les deux autres et utiliser le réseau `bridge` lorsque nous arriverons aux exemples.

## Adresse IP du conteneur Docker

Par défaut, le conteneur se voit attribuer une adresse IP pour chaque réseau Docker auquel il se connecte. Et chaque réseau est créé avec un masque de sous-réseau par défaut, l'utilisant plus tard comme un pool pour distribuer les adresses IP.

Habituellement, Docker utilise le sous-réseau par défaut **172.17.0.0/16** pour le réseau des conteneurs.

Pour mieux le comprendre, nous allons exécuter un cas d'utilisation réel.

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/flamenco-done.png" alt="drawing" width="300"/>
</div>

### Exemple Docker

Pour illustrer cela, nous allons utiliser un environnement Hive et Hadoop, contenant 5 conteneurs Docker.

Consultez le fichier `docker-compose.yml` que nous allons exécuter :

```
version: "3"

services:
  namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop2.7.4-java8
    volumes:
      - namenode:/hadoop/dfs/name
    environment:
      - CLUSTER_NAME=test
    env_file:
      - ./hadoop-hive.env
    ports:
      - "50070:50070"
  datanode:
    image: bde2020/hadoop-datanode:2.0.0-hadoop2.7.4-java8
    volumes:
      - datanode:/hadoop/dfs/data
    env_file:
      - ./hadoop-hive.env
    environment:
      SERVICE_PRECONDITION: "namenode:50070"
    ports:
      - "50075:50075"
  hive-server:
    image: bde2020/hive:2.3.2-postgresql-metastore
    env_file:
      - ./hadoop-hive.env
    environment:
      HIVE_CORE_CONF_javax_jdo_option_ConnectionURL: "jdbc:postgresql://hive-metastore/metastore"
      SERVICE_PRECONDITION: "hive-metastore:9083"
    ports:
      - "10000:10000"
  hive-metastore:
    image: bde2020/hive:2.3.2-postgresql-metastore
    env_file:
      - ./hadoop-hive.env
    command: /opt/hive/bin/hive --service metastore
    environment:
      SERVICE_PRECONDITION: "namenode:50070 datanode:50075 hive-metastore-postgresql:5432"
    ports:
      - "9083:9083"
  hive-metastore-postgresql:
    image: bde2020/hive-metastore-postgresql:2.3.0

volumes:
  namenode:
  datanode:
```

[De **docker-hive** GitHub](https://github.com/mesmacosta/docker-hive)

Personne ne veut lire un fichier de configuration **ÉNORME**, n'est-ce pas ? Alors voici une image :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-21-at-2.48.18-PM.png)

Bien mieux ! Maintenant, démarrons ces conteneurs :

```bash
docker-compose up -d
```

Nous pouvons voir 5 conteneurs :

```bash
$ docker ps --format \
"table {{.ID}}\t{{.Status}}\t{{.Names}}"

CONTAINER ID        STATUS                   NAMES
158741ba0339        Up 1 minutes             dockerhive_hive-metastore-postgresql
607b00c25f29        Up 1 minutes             dockerhive_namenode
2a2247e49046        Up 1 minutes             dockerhive_hive-metastore
7f653d83f5d0        Up 1 minutes (healthy)   dockerhive_hive-server
75000c343eb7        Up 1 minutes (healthy)   dockerhive_datanode
```

Vérifions maintenant nos réseaux Docker :

```bash
$ docker network ls

NETWORK ID          NAME                  DRIVER              SCOPE
c3cd46f397ce        bridge                bridge              local
9f6bc3c15568        docker-hive_default   bridge              local
ad4e4c24568e        host                  host                local
1c69593fc6ac        none                  null                local
```

Attendez une minute... il y a un nouveau réseau appelé `docker-hive_default` !

Par défaut, docker compose configure un seul réseau pour votre application. Et le réseau de votre application reçoit un nom basé sur le "nom de projet", provenant du nom du répertoire dans lequel il se trouve.

Donc, puisque notre répertoire est nommé `docker-hive`, cela explique le nouveau réseau.

Voici quelques exemples sur la façon d'obtenir l'adresse IP Docker.

## Comment obtenir une adresse IP de conteneur Docker - exemples

Et maintenant que j'ai votre attention, nous allons révéler le mystère.

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/bermuda-logged-out-1.png" alt="drawing" width="300"/>
</div>

### 1. Utilisation de Docker Inspect

Docker inspect est un excellent moyen de récupérer des informations de bas niveau sur les objets Docker. Vous pouvez extraire n'importe quel champ du JSON retourné de manière assez simple.

Alors, allons-nous l'utiliser pour obtenir l'adresse IP de `dockerhive_datanode` ?

```bash
$ docker inspect -f \
'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
75000c343eb7

172.18.0.5
```

N'avez-vous pas dit que Docker utilise le sous-réseau par défaut **172.17.0.0/16** pour le réseau des conteneurs ? Pourquoi l'adresse IP retournée est-elle **172.18.0.5** en dehors de celui-ci ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-22-at-3.25.07-PM.png)
_Image créée sur [ip-address-in-cidr-range](https://tehnoblog.org/ip-tools/ip-address-in-cidr-range/)_

Pour répondre à cela, nous devons examiner nos paramètres de réseau :

```bash
$ docker network inspect -f \
'{{range .IPAM.Config}}{{.Subnet}}{{end}}'  9f6bc3c15568

172.18.0.0/16
```

Nous avons exécuté cet exemple dans une VM Compute Engine, et dans ce test, le réseau docker s'est vu attribuer un sous-réseau différent : **172.18.0.0/16**. Cela explique cela !

De plus, nous pouvons également rechercher toutes les adresses IP à l'intérieur du réseau `docker-hive_default`.

Ainsi, nous n'avons pas besoin de rechercher l'IP de chaque conteneur individuellement :

```bash
$ docker network inspect -f \
'{{json .Containers}}' 9f6bc3c15568 | \
jq '.[] | .Name + ":" + .IPv4Address'

"dockerhive_hive-metastore-postgresql:172.18.0.6/16"
"dockerhive_hive-metastore:172.18.0.2/16"
"dockerhive_namenode:172.18.0.3/16"
"dockerhive_datanode:172.18.0.5/16"
"dockerhive_hive-server:172.18.0.4/16"
```

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/cherry-success.png" alt="drawing" width="300"/>
</div>

Si vous ne l'avez pas remarqué, nous avons utilisé [**jq**](https://github.com/stedolan/jq) pour analyser l'objet map `Containers`.

### 2. Utilisation de Docker exec

Dans l'exemple suivant, nous allons travailler avec `dockerhive_namenode`.

```bash
$ docker exec dockerhive_namenode cat /etc/hosts

127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.18.0.3      607b00c25f29
```

### 3. À l'intérieur du conteneur Docker

```bash
$ docker exec -it dockerhive_namenode /bin/bash

# en cours d'exécution à l'intérieur du conteneur dockerhive_namenode
ip -4 -o address

7: eth0    inet 172.18.0.3/16 brd 172.18.255.255 scope global eth0
```

Nous pouvons même trouver les adresses IP d'autres conteneurs qui sont à l'intérieur d'un conteneur dans le même réseau :

**Nœud de données**

```bash
# en cours d'exécution à l'intérieur du conteneur dockerhive_namenode
ping dockerhive_datanode

PING dockerhive_datanode (172.18.0.5): 56 data bytes
64 bytes from 172.18.0.5: icmp_seq=0 ttl=64 time=0.092 ms
```

**Métastore Hive**

```bash
# en cours d'exécution à l'intérieur du conteneur dockerhive_namenode
ping dockerhive_hive-metastore

PING dockerhive_hive-metastore_1 (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: icmp_seq=0 ttl=64 time=0.087 ms
```

**Serveur Hive**

```bash
# en cours d'exécution à l'intérieur du conteneur
ping dockerhive_hive-server

PING dockerhive_hive-server (172.18.0.4): 56 data bytes
64 bytes from 172.18.0.4: icmp_seq=0 ttl=64 time=0.172 ms
```

## **Conclusion**

Tous les exemples ont été exécutés dans une distribution Linux Compute Engine VM. Si vous les exécutez dans des environnements macOS ou Windows, les commandes exemples peuvent changer un peu.

Gardez également à l'esprit que ces adresses IP dans les exemples donnés sont internes au réseau exemple `docker-hive_default`. Donc, si vous avez un cas d'utilisation pour vous connecter à ces conteneurs de l'extérieur, vous devrez utiliser l'IP externe de la machine hôte (en supposant que vous exposez correctement les ports des conteneurs).

Ou si vous utilisez kubernetes, par exemple, pour gérer vos conteneurs Docker, laissez-le gérer les adresses IP pour vous [kubernetes-expose-external-ip-address](https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/) ?.

*** Illustrations de [icons8.com](https://icons8.com/) par [Murat Kalkavan](https://dribbble.com/muratkalkavan).**