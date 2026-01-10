---
title: Utilisation de Kubernetes pour déployer une passerelle de chat (ou quand la
  technologie fonctionne comme elle est censée le faire)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T10:40:51.000Z'
originalURL: https://freecodecamp.org/news/using-kubernetes-to-deploy-a-chat-gateway-or-when-technology-works-like-its-supposed-to-a169a8cd69a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZsohwEQHHw_sh0KX37pdeg.jpeg
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Utilisation de Kubernetes pour déployer une passerelle de chat (ou quand
  la technologie fonctionne comme elle est censée le faire)
seo_desc: 'By Richard Li

  TL;DR

  This is a story about what happens when cloud technologies work like they’re supposed
  to. In this case, the technologies are Docker and Kubernetes.

  Introduction

  At Datawire, we use Gitter so that users of our open source tools can...'
---

Par Richard Li

### TL;DR

Ceci est une histoire sur ce qui se passe lorsque les technologies cloud fonctionnent comme elles sont censées le faire. Dans ce cas, les technologies sont Docker et Kubernetes.

### Introduction

Chez [Datawire](https://www.datawire.io), nous utilisons [Gitter](http://gitter.im) afin que les utilisateurs de nos outils open source puissent discuter avec nous (et entre eux). Nous aimons Gitter car il est facile de s'inscrire, surtout si vous avez un compte GitHub ou Twitter. Cependant, le client mobile de Gitter n'est pas génial, et les notifications en général ne fonctionnent pas bien.

Étant donné que la migration d'une communauté d'utilisateurs représente un travail considérable, j'ai décidé de voir si je pouvais déployer un pont entre Slack (ce que nous utilisons en interne) et notre chat Gitter. Une petite recherche sur Google m'a conduit à [Matterbridge](https://github.com/42wim/matterbridge).

Dans le reste de l'article, je vais expliquer comment Docker et Kubernetes ont réellement simplifié ma vie, et pourquoi. J'ai trouvé que la quantité de [yak shaving](https://en.wiktionary.org/wiki/yak_shaving) requise était remarquablement faible... ce qui m'a fait vraiment apprécier les progrès que nous avons accomplis dans le monde du cloud.

### Docker est génial

Je voulais exécuter Matterbridge localement pour déboguer la configuration. J'ai suivi les instructions générales sur la création de comptes pour Slack et Gitter, puis j'ai placé les jetons d'authentification nécessaires dans un fichier `matterbridge.toml`.

J'étais heureux de voir que Matterbridge est disponible sous forme d'image Docker, donc j'ai pu simplement copier mon fichier de configuration dans l'image Docker pour tester la configuration. Tout ce que j'avais à faire était de spécifier mon fichier de configuration lors de l'utilisation de `docker run`:

```
docker run -ti -v /tmp/matterbridge.toml:/matterbridge.toml 42wim/matterbridge
```

J'ai dû faire quelques tours de cela pour déboguer ma configuration, mais c'était rapide et facile. L'image Docker a fait exactement ce qu'elle était censée faire : fournir un environnement d'exécution testé pour Matterbridge afin que je n'aie pas à le déboguer sur mon ordinateur portable.

### Exécution dans le cloud

L'étape suivante était de déployer ma configuration dans le cloud. Nous exécutons déjà un cluster Kubernetes de production fronté par une [API Gateway](https://www.getambassador.io) alimentée par [Envoy](https://www.datawire.io/envoyproxy/), donc je voulais déployer le service dans son propre namespace.

Pour déployer sur Kubernetes, j'ai écrit un simple Dockerfile :

```
FROM 42wim/matterbridge:1.9.0ADD matterbridge.toml .CMD ["/bin/matterbridge"]
```

Ensuite, tout ce dont j'avais besoin était un manifest Kubernetes.

### Kubernetes

Dans mon manifest Kubernetes, je peux spécifier un ensemble d'informations clés sur le service :

* Ma stratégie de mise à jour, `RollingUpdate`
* La quantité minimale et maximale de CPU et de mémoire à allouer
* Le nombre de réplicas du service

Voici mon manifest de base :

```
---apiVersion: apps/v1beta1kind: Deploymentmetadata:  name: {{build.name}}  namespace: {{service.namespace}}spec:  replicas: 1  strategy:    type: RollingUpdate  template:    metadata:      labels:        app: {{build.name}}    spec:      containers:      - name: {{build.name}}        image: {{build.images["Dockerfile"]}}        imagePullPolicy: IfNotPresent        resources:          requests:            memory: 0.1G            cpu: 0.1          limits:            memory: {{service.max_memory}}            cpu: {{service.max_cpu}}
```

(Notez que j'utilise [Forge](https://forge.sh) pour templater et gérer le service, donc ceci est un manifest Kubernetes templaté).

Avec ce manifest, j'ai pu mettre mon service en route et le faire fonctionner dans Kubernetes.

### Mon service Matterbridge dans Git

En résumé, mon service se compose de :

* Un Dockerfile
* Un manifest Kubernetes (templaté)
* Un fichier de configuration `matterbridge.toml`

Tout cela que j'ai pu commiter dans un dépôt Git.

### Le monde pré-Kubernetes

La facilité avec laquelle j'ai pu obtenir un service de manière fiable m'a fait réfléchir à la façon dont j'aurais fait cela à l'époque des VM. J'aurais dû :

* Approvisionner une VM (et/ou créer un groupe d'auto-scaling)
* Installer les dépendances d'exécution nécessaires sur la VM via un script bash (ou utiliser Ansible, ou construire une AMI personnalisée)
* Copier ma configuration sur la VM

De plus, si je voulais rendre ce qui précède reproductible, j'aurais dû utiliser Terraform, Ansible, CloudFormation, ou l'un de ces types d'outils. Voici l'exemple de la documentation Terraform sur [comment créer une instance EC2](https://www.terraform.io/docs/providers/aws/r/instance.html) :

```
# Créer une nouvelle instance de la dernière Ubuntu 14.04 sur un# nœud t2.micro avec une balise AWS la nommant "HelloWorld"provider "aws" {  region = "us-west-2"}data "aws_ami" "ubuntu" {  most_recent = true  filter {    name   = "name"    values = ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"]  }  filter {    name   = "virtualization-type"    values = ["hvm"]  }  owners = ["099720109477"] # Canonical}resource "aws_instance" "web" {  ami           = "${data.aws_ami.ubuntu.id}"  instance_type = "t2.micro"  tags {    Name = "HelloWorld"  }}
```

En tant que développeur, beaucoup des options ci-dessus (région, type d'instance) sont des choses dont je ne me soucie pas vraiment. Pourtant, c'est l'abstraction actuelle si je veux commiter de l'infrastructure-as-code.

### Résumé

Kubernetes est plus qu'un simple planificateur de conteneurs. Il vous donne vraiment les primitives dont vous avez besoin pour contrôler comment votre service est exécuté, sans vous encombrer des détails de déploiement. Nous adoptons définitivement la mentalité d'avoir une petite équipe de personnes ops gérer le cluster Kubernetes, tandis que le reste de l'équipe de développement gère simplement leurs services via les primitives Kubernetes.

Bien que ce ne soit pas toujours un long fleuve tranquille dans le monde de Kubernetes, dans mon cas de déploiement de Matterbridge, c'était le cas. Vous devrez attendre un autre article pour lire sur les défis !