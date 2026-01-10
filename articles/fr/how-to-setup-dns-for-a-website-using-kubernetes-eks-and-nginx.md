---
title: Comment configurer le DNS pour un site web avec Kubernetes, EKS et NGINX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-07T11:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-dns-for-a-website-using-kubernetes-eks-and-nginx
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/nyc.png
tags:
- name: Devops
  slug: devops
- name: dns
  slug: dns
- name: Kubernetes
  slug: kubernetes
- name: nginx
  slug: nginx
seo_title: Comment configurer le DNS pour un site web avec Kubernetes, EKS et NGINX
seo_desc: 'By Adam Henson

  As the creator of Foo, a platform for website quality monitoring, I recently endeavored
  in a migration to Kubernetes and EKS (an AWS service).

  Kubernetes provides a robust level of DNS support. Luckily for us, within a cluster,
  we can ...'
---

Par Adam Henson

En tant que créateur de [Foo, une plateforme de surveillance de la qualité des sites web](https://www.foo.software/), j'ai récemment entrepris une migration vers Kubernetes et EKS (un service AWS).

Kubernetes offre un support DNS robuste. Heureusement pour nous, au sein d'un cluster, nous pouvons référencer les pods par leur nom d'hôte tel que défini dans une spécification (spec).

Mais que se passe-t-il si nous voulons exposer une application au monde extérieur en tant que site web sous un domaine statique ? Je pensais que ce serait un cas courant et bien documenté, mais j'avais bien tort.

> Supposons un Service nommé `foo` dans l'espace de noms Kubernetes `bar`. Un Pod s'exécutant dans l'espace de noms `bar` peut rechercher ce service en effectuant simplement une requête DNS pour `foo`. Un Pod s'exécutant dans l'espace de noms `quux` peut rechercher ce service en effectuant une requête DNS pour `foo.bar` ~ [DNS pour les Services et les Pods - Kubernetes](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)

Oui, c'est génial ❤️ Mais cela laisse encore de nombreux mystères non résolus. Allons-y étape par étape, voulez-vous ?! Cet article traitera des points suivants.

1. **Comment définir des services**
2. **Comment exposer plusieurs services sous un seul serveur NGINX**. Pas besoin d'un « [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) » sophistiqué ?
3. **Comment créer un DNS externe et se connecter à un domaine** que vous avez acquis via n'importe quel registre qualifié comme GoDaddy ou Google Domains, par exemple. Nous utiliserons [Route 53](https://aws.amazon.com/route53/) et [ExternalDNS](https://github.com/kubernetes-sigs/external-dns) pour faire le gros du travail.

Cet article suppose une configuration avec EKS et `eksctl` comme documenté dans « [Getting started with `eksctl`](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) », mais de nombreux concepts et exemples de cet article pourraient être applicables dans diverses configurations.

## Étape 1 : Définir des services

[Connecter des applications avec des services](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/) explique comment exposer une application NGINX en définissant un `Deployment` et un `Service`. Créons 3 applications de la même manière : une application web orientée utilisateur, une API et un serveur NGINX reverse proxy pour exposer les deux applications sous un seul hôte.

> web-deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        # etc., etc.
```

> web-service.yaml

```
apiVersion: v1
kind: Service
metadata:
  name: web
  labels:
    app: web
spec:
  ports:
  - name: "3000"
    port: 3000
    targetPort: 3000
  selector:
    app: web
```

> api-deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
      - name: api
        # etc., etc.
```

> api-service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
  labels:
    app: api
spec:
  ports:
  - name: "3000"
    port: 3000
    targetPort: 3000
  selector:
    app: api
```

C'est assez clair, continuons !

## Étape 2 : Exposer plusieurs services sous un seul serveur NGINX

NGINX est un reverse proxy dans le sens où il relaie une requête en l'envoyant à une origine spécifiée, récupère la réponse et la renvoie au client.

En revenant sur le fait que les noms de services sont accessibles aux autres pods d'un cluster, nous pouvons mettre en place une configuration NGINX ressemblant à ceci.

> sites-enabled/www.example.com.conf

```
upstream api {
  server api:3000;
}

upstream web {
  server web:3000;
}

server {
  listen 80;

  server_name www.example.com;

  location / {
    proxy_pass http://web;
  }

  location /api {
    proxy_pass http://api;
  }
}
```

Notez comment nous pouvons référencer des hôtes d'origine comme `web:3000` et `api:3000`. Sympa !

> nginx-deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80

```

> nginx-service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
  annotations:
    # cette partie sera plus claire plus tard
    external-dns.alpha.kubernetes.io/hostname: www.example.com
  labels:
    app: nginx
spec:
  type: LoadBalancer
  ports:
  - name: "80"
    port: 80
    targetPort: 80
  selector:
    app: nginx
```

...et voilà, c'est fini ! N'est-ce pas ? D'après mon expérience, c'est ce que je pensais au début. Le `[LoadBalancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/)` fournit une adresse IP accessible de l'extérieur. Vous pouvez le confirmer en exécutant `kubectl get svc` et vous trouverez effectivement un nom d'hôte répertorié dans la colonne `EXTERNAL-IP`.

En supposant que vous ayez acquis un domaine auprès d'un fournisseur proposant une interface pour gérer les paramètres DNS, vous pourriez simplement ajouter cette URL en tant que `CNAME` et tout serait réglé, n'est-ce pas ? Eh bien, plus ou moins... mais pas tout à fait.

Les Pods Kubernetes sont considérés comme des entités relativement éphémères (plutôt que durables). Pour en savoir plus, consultez « [Cycle de vie des Pods - Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) ».

Cela dit, chaque fois qu'un changement significatif est apporté au cycle de vie d'un service, dans notre cas l'application NGINX, nous aurons une adresse IP différente, ce qui entraînera une interruption importante de notre application. Cela va à l'encontre de l'un des objectifs principaux de Kubernetes : aider à établir une application « hautement disponible ».

D'accord, ne paniquez pas - nous allons y arriver ?

## Étape 3 : Créer un service DNS externe pour pointer dynamiquement vers NGINX

À l'étape précédente, avec notre spécification `LoadBalancer` couplée à EKS, nous avons en fait créé un [Elastic Load Balancer](https://aws.amazon.com/elasticloadbalancing/) (pour le meilleur ou pour le pire).

Dans cette section, nous allons créer un service DNS qui pointe vers notre load balancer via un « enregistrement ALIAS ». Cet enregistrement ALIAS est essentiellement dynamique dans le sens où un nouveau est créé chaque fois que notre service change. La stabilité est établie dans les enregistrements de serveur de noms.

Le TL;DR pour la partie restante est de simplement suivre la [documentation pour utiliser ExternalDNS avec Route 53](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md). Route 53 est un « [service web de système de noms de domaine (DNS) dans le cloud](https://aws.amazon.com/route53/) ».

Voici les choses que j'ai dû faire et qui n'étaient pas évidentes dans la documentation. Accrochez-vous, ça va devenir un peu mouvementé.

* `eksctl utils associate-iam-oidc-provider --cluster=votre-nom-de-cluster` selon la [documentation des comptes de service `eksctl`](https://eksctl.io/usage/iamserviceaccounts/).
* Lors de la création du document de politique IAM selon la [documentation ExternalDNS](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#iam-policy), j'ai dû le faire via la CLI plutôt qu'en ligne sur mon compte. Je recevais sans cesse cette erreur : `WebIdentityErr: failed to retrieve credentials\ncaused by: AccessDenied: Not authorized to perform sts:AssumeRoleWithWebIdentity\n\tstatus code: 403`. Lorsque j'ai créé la politique via la CLI, le problème a disparu. Voici la commande complète que vous devriez pouvoir copier et exécuter littéralement si vous avez installé l'[AWS CLI](https://aws.amazon.com/cli/).

```
aws iam create-policy \
  --policy-name AllowExternalDNSUpdates \
  --policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":["route53:ChangeResourceRecordSets"],"Resource":["arn:aws:route53:::hostedzone/*"]},{"Effect":"Allow","Action":["route53:ListHostedZones","route53:ListResourceRecordSets"],"Resource":["*"]}]}'
```

* Utilisez l'ARN de la politique généré ci-dessus pour créer un rôle IAM lié au compte de service ExternalDNS avec une commande qui ressemblera à `eksctl create iamserviceaccount --cluster=votre-nom-de-cluster --name=external-dns --namespace=default --attach-policy-arn=arn:aws:iam::123456789:policy/AllowExternalDNSUpdates`.
* Nous devrions maintenant avoir un nouveau rôle issu de l'étape précédente que nous pouvons voir dans la [console IAM](https://console.aws.amazon.com/iam) et qui aura un nom comme `eksctl-foo-addon-iamserviceaccount-Role1-abcdefg`. Cliquez sur le rôle dans la liste et, en haut de l'écran suivant, notez l'« ARN du rôle » (Role ARN) comme `arn:aws:iam::123456789:role/eksctl-foo-addon-iamserviceaccount-Role1-abcdefg`.
* Suivez [ces étapes](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#set-up-a-hosted-zone) pour créer une « zone hébergée » (hosted zone) dans Route 53.
* Vous pouvez confirmer les informations dans la [console Route 53](https://console.aws.amazon.com/route53).
* Si votre fournisseur de domaine vous permet de gérer les paramètres DNS, ajoutez les 4 enregistrements de serveur de noms (NS) issus de la sortie de la commande que vous avez exécutée pour créer une « zone hébergée ».
* Déployez ExternalDNS en suivant [les instructions](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#deploy-externaldns). Ensuite, vous pouvez suivre les logs avec `kubectl logs -f nom-du-pod-external-dns`. Vous devriez voir une ligne comme celle-ci à la fin : `time="2020-05-05T02:57:31Z" level=info msg="All records are already up to date"` 

Facile, n'est-ce pas ?! D'accord, peut-être pas... mais au moins vous n'avez pas eu à trouver tout cela tout seul ? Il pourrait y avoir quelques lacunes ci-dessus, mais j'espère que cela vous aidera à vous guider dans votre processus.

## Conclusion

Bien que cet article puisse comporter des zones d'ombre, s'il vous aide à établir une résolution DNS dynamique dans le cadre d'une application hautement disponible, vous avez là quelque chose de vraiment spécial ✨

N'hésitez pas à ajouter des commentaires si je peux aider à éclaircir quoi que ce soit ou à corriger ma terminologie !