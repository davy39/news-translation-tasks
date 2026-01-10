---
title: Une introduction au gestionnaire de paquets Helm pour Kubernetes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-10T11:10:49.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-helm-package-manager-for-kubernetes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99c6740569d1a4ca21a6.jpg
tags:
- name: Helm
  slug: helm
- name: Kubernetes
  slug: kubernetes
seo_title: Une introduction au gestionnaire de paquets Helm pour Kubernetes
seo_desc: 'By Jillian Rowe

  Before we dive into the Helm package manager, I''m going to explain some key concepts
  to deploying any application anywhere. I''ll also give you a brief introduction
  to Kubernetes terminology.

  What is Kubernetes?


  Kubernetes (K8s) is an...'
---

Par Jillian Rowe

Avant de plonger dans le [gestionnaire de paquets Helm](https://helm.sh/), je vais expliquer quelques concepts clés pour déployer une application n'importe où. Je vais également vous donner une brève introduction à la [terminologie Kubernetes](https://kubernetes.io/).

## Qu'est-ce que Kubernetes ?

> [Kubernetes (K8s)](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) est un système open-source pour automatiser le déploiement, la mise à l'échelle et la gestion des applications conteneurisées
> [kubernetes.io](https://kubernetes.io/#kubernetes-k8s-docs-concepts-overview-what-is-kubernetes-is-an-open-source-system-for-automating-deployment-scaling-and-management-of-containerized-applications)

Maintenant, vous vous demandez peut-être : "Qu'est-ce que cela signifie ?"

Kubernetes est essentiellement un ensemble très complet d'API pour déployer, gérer et mettre à l'échelle des applications.

Les applications sont empaquetées avec Docker, puis la logique entourant le déploiement de l'application est exprimée à l'aide de modèles Helm. Les modèles eux-mêmes sont des instructions qui sont ensuite exécutées à l'aide de l'API Kubernetes.

Il existe [une tonne de paquets Helm](https://bitnami.com/stacks/helm) déjà créés pour répondre à vos besoins de déploiement d'applications !

J'aime penser à Kubernetes + Helm comme une solution tout-en-un pour mes besoins DevOps d'applications.

## C'est l'heure des faits amusants !

Tout l'écosystème des conteneurs, y compris Docker, a un thème nautique très amusant. Docker a des baleines, Kubernetes a des pods (de baleines), et son logo ressemble à la partie de gouvernail d'un navire, et Helm est le gouvernail d'un navire.

Ne sont-ils pas mignons ?

![Image](https://www.freecodecamp.org/news/content/images/2020/07/docker-swarm-logo.png)
_[https://hub.docker.com/_/swarm](https://hub.docker.com/_/swarm)_

## Déployer une application sur Kubernetes

Tout d'abord, peu importe où vous déployez une application, il y aura certaines choses qui resteront les mêmes partout, et je veux dire partout ! ;-) Que vous déployiez sur votre ordinateur portable, un serveur distant, une instance AWS EC2, des systèmes de calcul haute performance ou Kubernetes, les concepts sous-jacents ne changent pas.

Je considère presque tout, en particulier les concepts technologiques, comme une série de couches. Une fois que vous comprenez quelles sont ces couches fondamentales, vous pouvez commencer à travailler.

### Couches de l'application

Ce sont :

| Général  | Kubernetes  |
|---|---|
| Couche de données  | PVC ou Persistent Volume Claims |
| Couche d'application  | Pods  |
| Services  | SVC|

Prenons ces éléments un par un.

**Couche de données / Persistent Volume Claims (PVCs)**

C'est simple et direct. Lorsque vous devez persister des données, vous les persistez dans un système de fichiers. Cela peut être un stockage local ou un type de système de fichiers en réseau (NFS). Si vous utilisez une base de données, celle-ci finit également par persister dans un système de fichiers.

**Couche d'application / Pods**

La couche d'application est ce à quoi nous pensons généralement dans un déploiement. C'est la partie que nous `apt-get install`, `npm run` ou `docker run`. Une application pourrait être un serveur web NGINX, une application Python ou Node.js, ou une application Spark, pour n'en nommer que quelques-unes.

Les applications sont soit des **Deployments** Kubernetes, soit des **Stateful Sets**, selon qu'elles persistant des données (ou ont un état) ou non.

Une base de données MySQL serait un exemple d'application _Stateful_. Elle doit garder une trace des informations sur elle-même.

Un serveur NGINX serait un déploiement Kubernetes, car il n'a pas besoin de garder une trace d'informations sur lui-même — il est _stateless_.

**Couche de services / SVC**

La couche de services est l'endroit où nous exposons notre _Application_ au monde extérieur. Cela est généralement accompli en disant "Hey, j'ai une application qui s'exécute sur ce port". Vous avez peut-être exécuté celles-ci directement, ou fait quelque chose comme un proxy pass dans NGINX ou Apache.

### **Couches de fiabilité du site**

La fiabilité du site est notre capacité à dire en toute confiance que notre application est en cours d'exécution, fonctionne et restera probablement en cours d'exécution et fonctionnera !

Pour être réaliste, nous voulons qu'une API fasse essentiellement cela. 💡

_[XKCD](https://xkcd.com/1495/) - Hard Reboot_

<img src="https://imgs.xkcd.com/comics/hard_reboot.png" alt="XKCD Hard Reboot">

| Général  | Kubernetes  |
|---|---|
| Surveillance  | metrics-server  |
| Mise à l'échelle (ou équilibrage de charge)  | Horizontal Pod Autoscaler (HPA) |
| Règles de service | Spécifications du conteneur |

**Couche de surveillance / Metrics Server**

La couche de surveillance répond à la question "Comment se porte notre application ?" Idéalement, elle répondrait à des questions comme "Combien de CPU reste-t-il sur cette machine ?" et "Sommes-nous à court de mémoire ?".

**Couche de mise à l'échelle / HPA**

Avez-vous déjà eu une application qui fonctionnait très bien jusqu'à ce que trop de personnes commencent à l'utiliser en même temps ? Vous vous en occupez en mettant à l'échelle les instances de votre application vers le haut ou vers le bas.

Avec les applications web, vous verrez souvent le terme d'équilibrage de charge également. Cette fonctionnalité est intégrée dans de nombreux gestionnaires de processus et serveurs https tels que [PM2](https://pm2.keymetrics.io/) et [Gunicorn](https://gunicorn.org/).

Dans Kubernetes, vous accomplissez cela avec un Horizontal Pod Autoscaler, ou HPA, auquel vous donnez des règles spécifiques pour la mise à l'échelle vers le haut ou vers le bas.

**Couche de règles de service**

Avez-vous déjà voulu automatiser quand / comment votre application devrait redémarrer ? Peut-être voulez-vous qu'elle redémarre 3 fois puis abandonne. Ou peut-être voulez-vous qu'elle redémarre, mais pas tout de suite.

Donnez-lui un peu de temps ! Vous pouvez également vouloir une mesure objective pour tester si votre application est en cours d'exécution ou non.

## Déployer des applications sur Kubernetes

Les applications Kubernetes peuvent être déployées soit via la CLI, soit en écrivant des modèles YAML qui décrivent les différentes PVC, Pods (qu'ils soient des Deployments ou des Stateful sets), et les couches de Service (SVC).

## Le gestionnaire de paquets Helm

> Helm est le meilleur moyen de trouver, partager et utiliser des logiciels conçus pour [Kubernetes](https://kubernetes.io/).
> [https://helm.sh/](https://helm.sh/)

Le gestionnaire de paquets Helm nous permet de configurer des déploiements Kubernetes complexes dans un seul paquet, qui peut être installé avec une seule commande.

Helm utilise un langage de modélisation sur le dessus des définitions YAML Kubernetes pour permettre plus de versatilité à nos déploiements.

Probablement le point le plus important à noter avec Helm est qu'il a été largement accepté par la communauté. Cela signifie qu'il existe de nombreuses ressources pour utiliser Helm, commencer, et aussi des tonnes de Helm Charts préconfigurés !

Il est très rare que je doive créer un paquet Helm complètement à partir de zéro. Je peux presque toujours trouver un bon point de départ à partir d'un ou plusieurs des [Helm charts déjà disponibles](https://bitnami.com/stacks/helm).

## Déployer NGINX sur Kubernetes

Tout d'abord, parlons d'un déploiement de base NGINX sans Helm.

Comme vous pouvez le voir, il y a beaucoup de choses à suivre et nous ne taperions probablement pas cela à la main. C'est là que le gestionnaire de paquets Helm intervient, mais il est bon de jeter un coup d'œil pour savoir ce qui se passe d'abord ! ;-)

```yaml
# Source: nginx/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    app.kubernetes.io/name: nginx
    helm.sh/chart: nginx-6.0.1
    app.kubernetes.io/instance: nginx
    app.kubernetes.io/managed-by: Helm
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: nginx
      app.kubernetes.io/instance: nginx
  replicas: 1
  template:
    metadata:
      labels:
        app.kubernetes.io/name: nginx
        helm.sh/chart: nginx-6.0.1
        app.kubernetes.io/instance: nginx
        app.kubernetes.io/managed-by: Helm
    spec:      
      containers:
        - name: nginx
          image: docker.io/bitnami/nginx:1.19.0-debian-10-r2
          imagePullPolicy: "IfNotPresent"
          ports:
            - name: http
              containerPort: 8080
            
          livenessProbe:
            failureThreshold: 6
            initialDelaySeconds: 30
            tcpSocket:
              port: http
            timeoutSeconds: 5
          readinessProbe:
            initialDelaySeconds: 5
            periodSeconds: 5
            tcpSocket:
              port: http
            timeoutSeconds: 3
```

Maintenant, décomposons les différentes parties de la définition de déploiement Kubernetes.

**Métadonnées**

Je veux très brièvement aborder les `labels`. Brièvement, car il y a de fortes chances que vous soyez satisfait des valeurs par défaut et que vous n'ayez pas besoin de les modifier.

L'un des objectifs de Kubernetes est qu'il devrait abstraire le serveur physique réel. Vous ne devriez _généralement_ pas avoir à vous soucier de savoir si votre application s'exécute sur `node1` ou `node2`. Bien sûr, à un moment donné, vous vous en souciez, et alors vous commencerez à vous intéresser aux labels.

Jusqu'à ce moment, ne vous en souciez pas et restez avec les valeurs par défaut.

**Conteneurs**

C'est la partie de l'application qui sera la plus pertinente pour vous lorsque vous déployez des applications. Vous devez définir vos conteneurs.

Un seul Pod de déploiement peut avoir de nombreux conteneurs. Ce conteneur a, au minimum, un `name`, un `repo` et un `tag` :

```yaml
      containers:
        - name: nginx
          #image:  "repo:tag"
          image: docker.io/bitnami/nginx:1.19.0-debian-10-r2
```

Une fois que vous avez la base, vous devez définir les ports qui seront pris en charge par le service. Voyez cette séparation des préoccupations ?

```yaml
          ports:
            - name: http
              containerPort: 8080
```

**Règles de l'application**

Ensuite, à un moment donné, nous voulons savoir si notre application est en cours d'exécution. Nous pouvons même déterminer exactement où elle se trouve dans son cycle de vie avec les différents hooks :

```yaml
         livenessProbe:
            failureThreshold: 6
            initialDelaySeconds: 30
            tcpSocket:
              # Cela correspond au ports[0].name
              port: http
            timeoutSeconds: 5
          readinessProbe:
            initialDelaySeconds: 5
            periodSeconds: 5
            # Cela correspond au ports[0].name
            tcpSocket:
              port: http
            timeoutSeconds: 3
```

**Noms**

C'est plus un concept général, mais je veux souligner que donner des noms aux choses est très important dans l'écosystème Kubernetes. Remarquez que nous avons donné à notre `container` et `port` un `name`. Plus tard, lorsque nous devons nous référer à eux, nous utilisons ce `name`.

## Déployer NGINX sur Kubernetes avec un Helm Chart

Le gestionnaire de paquets Helm crée une série de modèles qui peuvent être modifiés via la CLI Helm. Chacun de ces modèles correspond à l'un de nos types Kubernetes dont nous avons parlé précédemment.

Voici un exemple du [bitnami/nginx](https://github.com/bitnami/charts/blob/master/bitnami/nginx/templates/deployment.yaml) helm chart :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/helm-chart-view.jpg)
_Bitnami/NGINX Helm Chart Templates_

Voici ce même bloc avec le langage de modélisation Helm. Pour des raisons de brièveté, j'ai omis certaines parties du modèle. Si vous souhaitez voir le tout, vous pouvez le consulter dans [le dépôt GitHub](https://github.com/bitnami/charts/blob/master/bitnami/nginx/templates/deployment.yaml).

(Ceci est à des fins de démonstration et n'est pas un Helm chart entièrement fonctionnel. Veuillez ne pas l'utiliser. Prenez plutôt le vrai Helm chart.)

```yaml
# Source: nginx/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ template "nginx.fullname" . }}
  labels: {{- include "nginx.labels" . | nindent 4 }}
spec:
  selector:
    matchLabels: {{- include "nginx.matchLabels" . | nindent 6 }}
  replicas: {{ .Values.replicaCount }}
  template:
    metadata:
      labels: {{- include "nginx.labels" . | nindent 8 }}
      # Omitted the annotation labels!
    spec:
      containers:
        - name: nginx
          image: {{ template "nginx.image" . }}
          imagePullPolicy: {{ .Values.image.pullPolicy | quote }}
          ports:
            - name: http
              containerPort: {{ .Values.containerPort }}
            {{ if .Values.containerTlsPort }}
            - name: https
              containerPort: {{ .Values.containerTlsPort }}
            {{ end }}
          {{- if .Values.livenessProbe }}
          livenessProbe: {{- toYaml .Values.livenessProbe | nindent 12 }}
          {{- end }}
          {{- if .Values.readinessProbe }}
          readinessProbe: {{- toYaml .Values.readinessProbe | nindent 12 }}
          {{- end }}
          {{- if .Values.resources }}
          resources: {{- toYaml .Values.resources | nindent 12 }}
          {{- end }}

```

### D'où viennent les valeurs des modèles Helm ?

Maintenant, voici ce que j'aime vraiment chez Helm. Les valeurs qui sont exposées dans le modèle proviennent de l'un des deux endroits.

**Fonctions de modélisation**

Elles proviennent du modèle lui-même, comme montré ici.

```yaml
{{ template "nginx.fullname" . }}
```

Nous pouvons trouver que cela est défini dans notre `templates/_helpers.tpl`, qui est un moyen d'obtenir des fonctions plus complexes que celles que nous pourrions obtenir avec un simple fichier `yaml`.

```yaml
# templates/_helpers.tpl
{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
# Here is the nginx.fullname
{{- define "nginx.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}

```

**Valeurs exposées dans le Values.yaml**

C'est en fait une fonctionnalité très intéressante et ce qui rend Helm si puissant et configurable.

Chaque Helm chart est accompagné d'un `values.yaml`. Vous pouvez mettre ce que vous voulez dans le `values.yaml`, puis l'utiliser dans tout votre Helm chart, et il est exposé via la CLI !

```yaml
## Bitnami NGINX image version
## ref: https://hub.docker.com/r/bitnami/nginx/tags/
##
image:
  registry: docker.io
  repository: bitnami/nginx
  tag: 1.19.1-debian-10-r0
  ## Specify a imagePullPolicy
  ## Defaults to 'Always' if image tag is 'latest', else set to 'IfNotPresent'
  ## ref: http://kubernetes.io/docs/user-guide/images/#pre-pulling-images
  ##
  pullPolicy: IfNotPresent
```

Ensuite, nous voyons cela référencé dans nos modèles comme :

```yaml
# templates/deployment.yaml 

# ...
      containers:
        - name: nginx
          image: {{ template "nginx.image" . }}
          imagePullPolicy: {{ .Values.image.pullPolicy | quote }}
```

Tout dans le `values.yaml` peut également être modifié via la CLI Helm :

```
helm upgrade --install nginx bitnami/nginx \
	--set image.tag="my-new-tag"
```

Il rendrait alors le `containers[0].image` comme `image: docker.io/bitnami/nginx:my-new-tag`

## Conclusion

C'est tout ! J'espère que vous avez appris un peu sur Kubernetes et son gestionnaire de paquets Helm. Espérons qu'il n'est plus aussi effrayant qu'il l'était autrefois.