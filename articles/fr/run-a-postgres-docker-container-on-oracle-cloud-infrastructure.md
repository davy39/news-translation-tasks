---
title: Comment exécuter un conteneur Docker Postgres sur Oracle Cloud Infrastructure
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2021-10-28T15:33:00.000Z'
originalURL: https://freecodecamp.org/news/run-a-postgres-docker-container-on-oracle-cloud-infrastructure
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/1QBgoEFNf.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Docker
  slug: docker
- name: Oracle
  slug: oracle
- name: postgres
  slug: postgres
seo_title: Comment exécuter un conteneur Docker Postgres sur Oracle Cloud Infrastructure
seo_desc: "In this article, I will show you how I quickly set up and ran a Docker\
  \ container for free on Oracle Cloud Infrastructure. \nIn short, I used a VM in\
  \ the Always Free Tier of OCI, and for a side project I set up a dockerised Postgres\
  \ database.\nLet's get..."
---

Dans cet article, je vais vous montrer comment j'ai rapidement configuré et exécuté un conteneur Docker gratuitement sur Oracle Cloud Infrastructure. 

En bref, j'ai utilisé une VM dans le niveau Always Free d'OCI, et pour un projet parallèle, j'ai configuré une base de données Postgres dockerisée.

Entrons un peu plus dans les détails maintenant.

## Pourquoi Oracle Cloud Infrastructure

Oracle offre une option de services cloud Always Free. Vous pouvez voir les détails ci-dessous :

![Offre gratuite d'Oracle Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1627392039154/de-tKbxcu.png)

Notez que la charge de travail d'un conteneur doit correspondre à la forme de cette VM toujours gratuite : VM.Standard.E2.1.Micro, 1/8 OCPU, 1 Go de RAM et jusqu'à 480 Mbps de bande passante réseau (voir la [documentation](https://docs.cloud.oracle.com/en-us/iaas/Content/FreeTier/resourceref.htm)). Le volume de démarrage offre un peu plus de 45 Go de stockage sur disque.

Pour que le conteneur soit accessible, les ports mappés sur la VM vers le conteneur doivent également être configurés dans les règles d'entrée dans la liste de sécurité. Nous devons installer Docker nous-mêmes dans la VM - elle est provisionnée avec juste une image Oracle Linux.

Commençons.

## Étape 1 - Obtenez un locataire et créez une machine virtuelle

La première chose que nous devons faire est de créer une VM. Si vous avez un locataire cloud, vous savez probablement déjà comment créer une instance. Si vous êtes nouveau sur Oracle Cloud, regardez la vidéo ci-dessous et créez une VM "always free" en vous inscrivant sur [https://cloud.oracle.com/free](https://cloud.oracle.com/free) :

%[https://www.youtube.com/watch?v=Fiu9BiNocJ4]

Remarque : La plupart des détails comme la zone de disponibilité, les détails de l'image et les options de réseau sont déjà pré-remplis par Oracle. Mais vous pouvez les ajuster si vous voulez quelque chose de spécifique. J'ai continué avec les paramètres standard.

La VM sera maintenant provisionnée comme indiqué ici :

![Exemple de VM provisionnée du blog des développeurs Oracle](https://miro.medium.com/max/1400/0*xGhUET08TkqbImko.png)

Après un petit moment, la VM sera opérationnelle et une adresse IP publique lui sera attribuée :

![Exemple de VM en cours d'exécution du blog des développeurs Oracle](https://miro.medium.com/max/1400/0*h0JYNsMZtsitKN2t.png)

La situation à ce stade peut être visualisée comme montré dans la figure ci-dessous :

![Visualisation de la configuration de la VM du blog des développeurs Oracle](https://miro.medium.com/max/1272/0*buppgWcJ5Wqgm3TK.png)

## Étape 2 - Configurer les règles d'entrée dans la liste de sécurité pour votre VM

Cela vous permet d'ouvrir les ports nécessaires pour le conteneur que vous souhaitez exécuter.

La VM est associée à un sous-réseau public dans un réseau cloud virtuel. La ou les listes de sécurité pour ce sous-réseau doivent être configurées avec des règles d'entrée qui permettent le trafic requis vers le ou les ports qui seront mappés à l'image du conteneur.

Ouvrez la page des détails pour le sous-réseau public. Cliquez sur la liste de sécurité (ou créez-en une nouvelle) :

![Écran du sous-réseau du blog des développeurs Oracle](https://miro.medium.com/max/1400/0*fgaHDl-hyONzSeh9.png)

Nous allons exécuter l'image du conteneur Postgres. Le port que nous mappons dans la VM vers le conteneur Postgres est un port que nous pouvons choisir nous-mêmes. Choisissons 5432 qui est le port par défaut pour Postgres. 

Nous devons configurer une règle d'entrée comme suit :

![Capture d'écran de la règle d'entrée](https://cdn.hashnode.com/res/hashnode/image/upload/v1627395159097/36GiB4i22.png)

Le CIDR source est défini sur 0.0.0.0/0, et la plage de ports source est laissée vide (c'est-à-dire, Tous), ce qui signifie que cette règle s'applique à n'importe quel client.

## Étape 3 - Se connecter en SSH à la VM et installer Docker

À ce stade, nous avons une instance de VM en cours d'exécution avec uniquement un système d'exploitation Linux mais sans Docker. Connectons-nous en SSH à la VM en utilisant cette commande :

```
ssh opc@public-id-address -i private-key-file

```

Remplacez public-id-address par l'adresse IP publique attribuée à la VM. Remplacez private-key-file par une référence au fichier qui contient la clé privée SSH.

Pour installer Docker, exécutez ces commandes :

```
sudo yum-config-manager --enable ol7_addons 
sudo yum install docker-engine -y 
sudo systemctl start docker 
sudo systemctl enable docker

```

![Capture d'écran de l'installation de Docker du blog des développeurs Oracle](https://miro.medium.com/max/1400/0*tAhI8bQyLIaDPQ3T.png)

Pour exécuter Docker en tant qu'utilisateur non-root, lisez [ces instructions](https://docs.docker.com/engine/security/rootless/).

## Comment exécuter l'image du conteneur Docker

Avec Docker installé, nous pouvons maintenant exécuter l'image du conteneur Postgres.

Exécutez l'image du conteneur avec cette commande. N'oubliez pas d'ajouter un mot de passe différent pour `POSTGRES_PASSWORD` :

```
sudo docker run -d -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=mysecretpassword postgres

```

Utilisez `sudo docker ps` pour vérifier si le conteneur est en cours d'exécution. La commande ci-dessus démarrera une base de données PostgreSQL et mappera les ports en utilisant le modèle suivant : `-p <host_port>:<container_port>`.

Le port 5432 de notre conteneur sera mappé sur le port 5432 de notre hôte ou serveur.

Accédez au conteneur sur votre hôte ou serveur. Nous allons créer une base de données à l'intérieur de notre conteneur Postgres.

```
sudo docker exec -it postgres bash

```

Vous êtes maintenant "à l'intérieur" de votre conteneur. Nous pouvons accéder à Postgres et créer la base de données.

```
root@12d48fde2627:/# psql -U postgres
psql (13.3 (Debian 13.3-1.pgdg100+1))
Tapez "help" pour obtenir de l'aide.

postgres=# CREATE DATABASE testdb;
CREATE DATABASE
postgres=# \q

```

Et avec cela, nous avons terminé ! Vous pouvez quitter votre conteneur (`\q`) et retourner à votre machine locale. 

Ici, vous avez besoin d'un outil client PostgreSQL installé comme [DBeaver](https://dbeaver.io/) ou [pgAdmin](https://www.pgadmin.org/). Connectez-vous au serveur de base de données en utilisant l'IP publique comme hôte, `5432` comme port, `postgres` comme nom d'utilisateur, le `POSTGRES_PASSWORD` comme mot de passe et connectez-vous à la `testdb`. Enregistrez la connexion et vous devriez maintenant pouvoir accéder à votre base de données.

## Félicitations, vous avez maintenant exécuté un conteneur Docker Postgres sur Oracle Cloud Infrastructure !

Merci d'avoir lu ! J'espère vraiment que vous trouverez cet article utile. Je suis toujours intéressé à connaître vos pensées et heureux de répondre à toutes les questions que vous pourriez avoir en tête. Si vous pensez que cet article était utile, veuillez le partager pour aider à promouvoir cet article auprès des autres.

Merci d'avoir lu ! :)

P.S. N'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/rohitjmathew) ou [Twitter](https://twitter.com/iamrohitjmathew).

## Ressources

Cet article s'appuie largement sur les matériaux suivants :

* [Exécuter un conteneur Docker Always Free sur Oracle Cloud Infrastructure](https://medium.com/oracledevs/run-always-free-docker-container-on-oracle-cloud-infrastructure-c88e36b65610) - Lucas Jellema
* [Se connecter depuis votre machine locale à une base de données PostgreSQL dans Docker](https://betterprogramming.pub/connect-from-local-machine-to-postgresql-docker-container-f785f00461a7) - Lorenz Vanthillo