---
title: Comment installer Docker sur Ubuntu 18.04 [Guide pour les versions CE et EE]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-07T18:06:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-docker-on-ubuntu-18-04-guide-for-both-ce-and-ee
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Docker-CE--1-.png
tags:
- name: Docker
  slug: docker
- name: Ubuntu
  slug: ubuntu
seo_title: Comment installer Docker sur Ubuntu 18.04 [Guide pour les versions CE et
  EE]
seo_desc: 'By Marcelo Costa

  Back in 2017, Docker introduced two different versions of its platform: Docker-CE
  and Docker-EE. But do you know their differences?





  Docker CE (Community Edition) is the classical OSS (Open Source Software) Docker
  Engine. Includes...'
---

Par Marcelo Costa

[En 2017](https://www.docker.com/blog/docker-enterprise-edition/), Docker a introduit deux versions différentes de sa plateforme : Docker-CE et Docker-EE. Mais connaissez-vous leurs différences ?

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/DockerCE_1.png" alt="drawing" width="300">
</div>

Docker CE (Community Edition) est le classique moteur Docker OSS (Open Source Software). Il inclut la plateforme Docker complète et est idéal pour les développeurs et les équipes DIY qui commencent à construire des applications conteneurisées.

Si vous êtes un développeur passionné comme moi, vous utilisez probablement Docker depuis un certain temps. Et je dirais que c'est très probablement la version avec laquelle vous avez travaillé, simplement parce qu'elle est gratuite !

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/DockerEE.png" alt="drawing" width="300">
</div>

Docker EE, en revanche, est une version premium de CE. Il inclut toutes les capacités de CE plus de nombreuses [fonctionnalités de niveau entreprise](https://docs.mirantis.com/docker-enterprise/v3.0/dockeree-products/dee-intro.html).

Tout ce qui est premium n'est [pas gratuit, n'est-ce pas](https://hub.docker.com/editions/enterprise/docker-ee-server-ubuntu/purchase) ? Donc, cela va de 750 $/mois pour le plan de base à 2000 $/mois pour le plan avancé. En tout cas, les prix sont conformes à ce que l'on peut attendre des produits d'entreprise.

> Veuillez contacter leur équipe commerciale pour vérifier les prix les plus à jour.

## Docker CE vs EE - les détails

Faisons une comparaison rapide entre l'intérêt pour Docker EE et Docker CE au fil du temps :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-04-at-6.01.50-PM.png)

Maintenant, Docker EE vs Docker CE vs Docker :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-04-at-6.27.17-PM.png)

D'après mon expérience, les utilisateurs qui recherchent simplement Docker cherchent l'édition CE. Cela nous montre que Docker EE est beaucoup moins utilisé. Mais je suis certain qu'il existe des cas d'utilisation robustes où il est judicieux de l'utiliser.

Étant un passionné de l'open source, toute mon expérience vient de l'utilisation de l'édition Docker CE, donc écrire cet article a été une expérience merveilleuse pour jouer avec Docker EE.

Après cette brève introduction, mettons les mains dans le cambouis.

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/flamenco-285.png" alt="drawing" width="300">
</div>

## Préparer la machine Ubuntu 18.04

En premier lieu, nous allons préparer le terrain en exécutant quelques commandes courantes.

Toutes les commandes seront exécutées sur une machine Ubuntu 18.04 fraîchement installée, et cette fois, j'ai choisi Google Cloud Platform comme environnement de démonstration.

### Créer la machine virtuelle

Commençons par créer une nouvelle VM en utilisant l'image Ubuntu 18.04 :

```bash
gcloud compute instances create ubuntu-fcc-demo \
--zone=us-central1-c \
--machine-type=n1-standard-1 \
--image=ubuntu-minimal-1804-bionic-v20200703a \
--image-project=ubuntu-os-cloud \
--boot-disk-size=10GB \
--boot-disk-type=pd-standard
```

Maintenant, connectez-vous à celle-ci en utilisant ssh :

```bash
gcloud compute ssh ubuntu-fcc-demo --zone=us-central1-c
```

Configurez les dépendances courantes :

```bash
sudo apt-get update

sudo apt-get install \
   apt-transport-https \
   ca-certificates \
   curl \
   gnupg-agent \
   software-properties-common
```

## Installer Docker CE sur Ubuntu 18.04

### Installer depuis https://get.docker.com

Le script d'installation vous permet d'installer rapidement les dernières versions de Docker-CE sur les distributions Linux supportées. Je ne recommande pas de dépendre de ce script pour le déploiement sur des systèmes de production. D'après [docker-install](https://github.com/docker/docker-install) :

```bash
curl -sSL https://get.docker.com/ | sh
```

La beauté de cette commande est qu'elle vérifie votre distribution Linux et exécute les bonnes instructions pour faire fonctionner Docker CE pour vous.

Vous pouvez tester que tout est OK en exécutant :

```bash
sudo docker run hello-world

# output
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/flamenco-done.png" alt="drawing" width="300">
</div>

### Installer depuis le dépôt Docker

Celui-ci comporte plus d'étapes, mais c'est l'approche recommandée par la documentation officielle de Docker (nous vérifions même leur [empreinte de clé GPG](https://en.wikipedia.org/wiki/Public_key_fingerprint)).

Tout d'abord, ajoutez la clé GPG officielle de Docker :

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
| sudo apt-key add -
```

Ensuite, vérifiez l'empreinte de la clé :

```bash
sudo apt-key fingerprint 0EBFCD88
```

Recherchez l'empreinte `9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88`. Cela garantit que la clé n'a pas été altérée.

Ensuite, configurez un dépôt **stable** de Docker :

```bash
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

La commande `$(lsb_release -cs)` retourne la distribution Ubuntu. Dans notre cas, nous avons utilisé `bionic`.

Maintenant, installez le moteur Docker :

```bash
 sudo apt-get update
 sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Et testez que tout est OK en exécutant :

```bash
sudo docker run hello-world

# output
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/cherry-success.png" alt="drawing" width="300">
</div>

Instructions basées sur [docs.docker.com](https://docs.docker.com/engine/install/ubuntu/).

## Installer Docker EE sur Ubuntu 18.04

### Installer en utilisant Mirantis Launchpad CLI

Pour travailler avec Docker EE, vous avez besoin d'une version d'essai/achetée. Docker a désactivé l'option pour obtenir un abonnement d'essai sur leur site web, et maintenant vous devez contacter leur équipe commerciale [pour obtenir un compte d'essai](https://hub.docker.com/editions/enterprise/docker-ee-server-ubuntu).

En cherchant, j'ai découvert que, depuis que [Mirantis a acquis Docker Enterprise](https://techcrunch.com/2019/11/13/mirantis-acquires-docker-enterprise/), la manière d'obtenir un compte d'essai Docker EE a changé. Vous devez vous rendre sur le [site web de Mirantis](https://www.mirantis.com/software/docker/download/) et, après avoir postulé, vous pouvez le télécharger immédiatement.

Au moment de la rédaction de cet article, l'installeur est actuellement un logiciel bêta. Si vous connaissez une autre manière d'installer Docker EE, veuillez me contacter. J'adorerais améliorer cet article !

L'outil CLI Mirantis Launchpad ("**launchpad**") est la nouvelle et meilleure manière d'évaluer et d'expérimenter [Docker Enterprise](https://www.mirantis.com/software/docker/docker-enterprise/) (consultez [launchpad GitHub](https://github.com/Mirantis/launchpad)).

### Télécharger Launchpad CLI

Commencez par [télécharger Launchpad](https://github.com/Mirantis/launchpad/releases/latest). Pour Ubuntu 18.04, j'ai utilisé la version [launchpad-darwin-x64](https://github.com/Mirantis/launchpad/releases/download/0.12.0/launchpad-darwin-x64).

Si vous ne l'avez pas téléchargé depuis la machine virtuelle, voici une commande pour l'uploader :

```bash
gcloud compute scp launchpad-linux-x64 ubuntu-fcc-demo:~/launchpad \
  --zone=us-central1-c
```

Ensuite, vérifiez l'installation :

```bash
# Donnez-lui la permission d'écriture
chmod +x launchpad

# Vérifiez l'installation
./launchpad version

# output
version: 0.12.0
commit: 4492884
```

Ensuite, enregistrez votre utilisateur :

```bash
launchpad register
```

Les informations fournies via l'enregistrement sont utilisées pour attribuer des licences d'évaluation et pour fournir une assistance pour l'utilisation du produit.

Ensuite, configurez votre fichier `cluster.yaml`.

Cette étape a été celle qui m'a pris le plus de temps. Vous devez configurer 3 machines :

* Machine Admin : Celle où vous exécutez la commande launchpad.
* Machine Worker : Exécutera vos charges de travail.
* Machine Manager : Contient le tableau de bord admin, où vous avez accès à de nombreuses configurations et métriques.

Ils ont fait un excellent travail avec le binaire Go `launchpad`. Les parties délicates se trouvent dans la configuration de l'infrastructure. Heureusement, ils ont déjà quelques [scripts terraform](https://github.com/Mirantis/launchpad/tree/master/examples/terraform) pour aider avec cela.

Étant donné qu'au moment de la rédaction de cet article, il n'y avait pas d'option pour GCP, j'ai dû configurer l'infrastructure manuellement. La machine Admin se connecte aux nœuds Worker et Manager pour configurer de nombreuses étapes, assurez-vous donc d'avoir correctement configuré les clés ssh.

L'étape des clés ssh m'a pris un certain temps à comprendre, et j'ai même [ouvert un problème](https://github.com/Mirantis/launchpad/issues/30) dans leur dépôt, mais ensuite je l'ai rapidement résolu. Donc, si vous avez un problème similaire, assurez-vous de le vérifier.

Il existe une [documentation très détaillée](https://github.com/Mirantis/launchpad/blob/master/docs/configuration-file.md) sur chaque attribut que vous pouvez utiliser dans le fichier de configuration.

Maintenant, il est temps de démarrer votre cluster.

Une fois que vous avez configuré le fichier `cluster.yaml`, vous pouvez exécuter la commande apply :

```bash
launchpad --debug apply
```

Vous devriez voir quelque chose comme ceci :

**Exécution de la phase : Installer le moteur Docker EE sur les hôtes**

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-07-at-12.06.45-PM.png)

C'est ici que je peux dire qu'ils ont fait un excellent travail en abstraisant toutes les étapes de configuration.

Il y a 37 étapes que le binaire Go `launchpad` exécute.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-07-at-12.22.30-PM.png)

À la fin, vous devriez voir un message comme ceci :

```bash
INFO[0021] ==> Running phase: UCP cluster info
INFO[0021] Cluster is now configured. You can access your cluster admin UI at: https://34.71.157.231 \
INFO[0021] You can also download the admin client bundle with the following command: launchpad download-bundle --username <username> --password <password>

```

Maintenant, pour tester que tout est OK, allez dans l'interface d'administration du cluster :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-07-at-12.25.50-PM.png)
_Interface de connexion admin_

Après vous être connecté, vous êtes présenté à l'interface d'administration du cluster :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-07-at-12.27.30-PM.png)
_Tableau de bord admin_

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/cherry-success.png" alt="drawing" width="300">
</div>

J'ai un peu joué avec certaines de ses fonctionnalités, et globalement, elles sont excellentes. Elles fournissent des contrôles d'accès faciles à utiliser et des images Docker certifiées.

Ces instructions sont basées sur ce [guide de démarrage](https://github.com/Mirantis/launchpad/blob/master/docs/getting-started.md).

## **Conclusion**

Dans cet article, nous avons vu comment configurer Docker sur Ubuntu 18.04 pour les versions CE et EE.

Et puisque [Mirantis a acquis Docker Enterprise](https://techcrunch.com/2019/11/13/mirantis-acquires-docker-enterprise/), nous avons découvert que Launchpad est la dernière manière pour les clients souhaitant essayer les licences Docker Enterprise.

Globalement, l'expérience de développement/déploiement est vraiment bonne, puisque presque toutes les étapes pour préparer un environnement pour Docker EE sont automatisées. Et Docker semble chercher à automatiser de plus en plus ce processus, ce qui est vraiment bien !


* Illustrations de [Icons8](https://icons8.com/)

Si vous avez trouvé cela utile, ou si vous souhaitez contester ou étendre quelque chose mentionné ici, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/mesmacosta) ou [Linkedin](https://www.linkedin.com/in/mesmacosta). Restons en contact !