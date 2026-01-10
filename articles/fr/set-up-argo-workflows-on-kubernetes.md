---
title: Comment installer Argo Workflows sur Kubernetes
subtitle: ''
author: Abraham Dahunsi
co_authors: []
series: null
date: '2024-02-15T23:23:44.000Z'
originalURL: https://freecodecamp.org/news/set-up-argo-workflows-on-kubernetes
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Feature-Image.png
tags:
- name: container
  slug: container
- name: Kubernetes
  slug: kubernetes
seo_title: Comment installer Argo Workflows sur Kubernetes
seo_desc: Argo Workflows is an open source project that enables the orchestration
  of multiple Kubernetes jobs. Argo Workflows is implemented as a Kubernetes custom
  resource definition (CRD), which means it is native to the Kubernetes ecosystem
  and can run on a...
---

Argo Workflows est un projet open source qui permet l'orchestration de plusieurs jobs Kubernetes. Argo Workflows est implémenté en tant que définition de ressource personnalisée Kubernetes (CRD), ce qui signifie qu'il est natif de l'écosystème Kubernetes et peut s'exécuter sur n'importe quel cluster Kubernetes.

Les workflows sont des étapes définies par lesquelles des jobs individuels sont exécutés. Vous pouvez utiliser Argo Workflows pour diverses finalités, telles que le traitement de données, le machine learning, le CI/CD et l'automatisation de l'infrastructure.

Dans cet article, vous allez installer Argo Workflows sur un cluster Kubernetes et utiliser des templates disponibles pour créer un Workflow à gérer dans un cluster Kubernetes.

## Concepts clés d'Argo Workflows

Comme mentionné ci-dessus, Argo Workflows est implémenté en tant que définition de ressource personnalisée Kubernetes (CRD) par son propre contrôleur. Argo Workflows est composé de deux concepts principaux : `workflow` et `Template`.

### Workflow

Un workflow est une ressource centrale dans Argo Workflows qui définit le workflow à exécuter et stocke l'état du workflow.

Un workflow se compose d'une spécification qui contient un point d'entrée et une liste de templates.

Un workflow peut modéliser une logique complexe en utilisant des graphes acycliques dirigés (DAG) ou des étapes pour capturer les dépendances ou les séquences entre les templates.

### Template

Un template est un concept central dans Argo Workflows qui définit les instructions à exécuter dans une étape de workflow. Un template peut être de l'un des types suivants :

* **Container** : Permet de définir le conteneur. Voici un exemple :

```YAML
  - name: hello-world
    container:
      image: alpine:latest
      command: [sh, -c]
      args: ["echo hello world"]
```

* **Script** : Un template qui exécute un script dans une image de conteneur. Cela est similaire au type conteneur, mais permet d'écrire le script en ligne au lieu d'utiliser un fichier séparé. Voici un exemple :

```YAML
  - name: factorial
    inputs:
      parameters:
      - name: num
    script:
      image: python:alpine 3.6
      command: [python]
      source: |
        def factorial(n):
          if n == 0:
            return 1
          else:
            return n * factorial(n-1)
        print(factorial(int({{inputs.parameters.num}})))
```

* **Resource** : Ce template permet la manipulation directe des ressources du cluster. Il peut être utilisé pour des opérations telles que la récupération, la création, la modification ou la suppression, y compris les requêtes GET, CREATE, APPLY, PATCH, REPLACE ou DELETE. Voici un exemple :

```YAML
  - name: create-configmap
    resource:
      action: create
      manifest: |
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: my-config
        data:
          foo: bar
          hello: world
```

* **DAG** : Ce template définit un graphe acyclique dirigé d'autres templates. Dans cet exemple, le DAG a trois tâches : A, B et C. La tâche A s'exécute en premier, puis les tâches B et C s'exécutent en parallèle. Voici un exemple :

```YAML
  - name: my-dag
    dag:
      tasks:
      - name: A
        template: echo
        arguments:
          parameters: [{name: message, value: A}]
      - name: B
        dependencies: [A]
        template: echo
        arguments:
          parameters: [{name: message, value: B}]
      - name: C
        dependencies: [A]
        template: echo
        arguments:
          parameters: [{name: message, value: C}]
```

Maintenant, commençons.

## Prérequis

Pour suivre ce guide, assurez-vous d'avoir les éléments suivants :

* Un cluster Kubernetes. Pour créer un nouveau cluster Kubernetes, suivez ce [guide](https://k21academy.com/docker-kubernetes/three-node-kubernetes-cluster/)

* Une connaissance de base de ce qu'est Kubernetes. [Vous pouvez en apprendre davantage sur Kubernetes à partir de leur documentation officielle](https://kubernetes.io/docs/concepts/overview/)

* [L'interface de ligne de commande Kubectl](https://kubernetes.io/docs/tasks/tools/)

## Étape 1 - Installer Argo Workflows

1. Utilisez `Kubectl` pour créer un namespace pour Argo Workflows afin de séparer les ressources de votre cluster Kubernetes.

```bash
$ kubectl create namespace argo
```

2. Installez le fichier de release le plus récent d'Argo Workflows à partir de la [page GitHub d'Argo Workflows](https://github.com/argoproj/argo-workflows/releases).

```bash
$ kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v<VERSION>/install.yaml
```

La version d'Argo Workflows utilisée dans ce guide est la v3.5.0.

3. Vérifiez si toutes les ressources ont été installées correctement.

```bash
$ kubectl get all -n argo
```

Sortie :

```bash
NAME                                      READY   STATUS    RESTARTS   AGE
pod/workflow-controller-7f8c9f8f5-9qj2l   1/1     Running   0          2m
pod/argo-server-6f8f9c9f8f-6kx4d          1/1     Running   0          2m

NAME                                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/argo-server                   ClusterIP   10.3.240.123    <none>        2746/TCP   2m
service/workflow-controller-metrics   ClusterIP   10.3.240.124    <none>        9090/TCP   2m

NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/workflow-controller   1/1     1            1           3m05s
deployment.apps/argo-server           1/1     1            1           3m07s

NAME                                            DESIRED   CURRENT   READY   AGE
replicaset.apps/workflow-controller-7f8c9f8f5   1         1         1       3m33s
replicaset.apps/argo-server-6f8f9c9f8f          1         1         1       2m33s
```

## Étape 2 - Démarrer l'interface utilisateur Argo pour la surveillance

Argo Server dispose d'une interface utilisateur graphique que vous pouvez utiliser pour gérer et surveiller les workflows de votre cluster Kubernetes.

Dans ce guide, vous allez contourner le processus d'authentification de demande de jeton pour accéder à l'interface web Argo car elle ne peut pas être accessible publiquement. Cela s'appelle le mode **Authentification du serveur**, bien que vous puissiez utiliser l'autre mode, **Authentification du client**, qui nécessite que vous demandiez un jeton pour pouvoir accéder à l'interface web.

1. Changez le mode d'authentification en Authentification du serveur.

```bash
$ kubectl patch deployment \
  argo-server \
  --namespace argo \
  --type='json' \
  -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/args", "value": [
  "server",
  "--auth-mode=server"
]}]'
```

Sortie :

```bash
deployment.apps/argo-server patched
```

Notez que ce mode n'est pas recommandé pour les environnements de production, car il crée des risques de sécurité significatifs. Une option plus sécurisée consiste à utiliser le **mode d'authentification client**, qui nécessite que les clients fournissent leur jeton porteur Kubernetes.

2. Configurez le contrôle d'accès basé sur les rôles Kubernetes (RBAC) pour accorder des permissions de niveau administrateur Argo pour la gestion des ressources au sein du namespace `argo`.

```bash
$ kubectl create rolebinding argo-default-admin --clusterrole=admin --serviceaccount=argo:default -n argo
```

3. Transférez le port de l'interface web du serveur Argo avec `kubectl port-forward`.

```bash
$ kubectl -n argo port-forward deployment/argo-server 2746:2746
```

En utilisant un navigateur comme Chrome, visitez l'adresse IP `http://localhost:2746`.

![Screenshot-20240213-003321](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-20240213-003321.png align="left")

## Créer un nouveau Workflow

Vous pouvez utiliser un manifeste YAML pour définir des workflows Argo et les appliquer à votre cluster Kubernetes.

1. Créez un nouveau fichier de Workflow.

```bash
Nano argo-workflow.yaml
```

2. Ajoutez ce qui suit au fichier :

```YAML
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
    name: demo-workflow
spec:
    entrypoint: main
    templates:
    - name: main
    container:
        image: busybox
        command: ["/bin/sh"]
        args: ["-c", "echo 'The first step of the Workflow'"]
```

Voici une brève description des composants du fichier :

* `entrypoint` spécifie le point d'entrée pour le workflow, qui est défini comme `main`.

* `templates` contient une liste de templates, qui définissent les étapes ou tâches au sein du workflow.

* `name` est le nom du template, qui est défini comme `main`.

* `container` spécifie une étape basée sur un conteneur au sein du workflow.

* `image` spécifie l'image Docker à utiliser pour le conteneur, définie ici comme `busybox`.

* `command` spécifie la commande à exécuter à l'intérieur du conteneur, définie comme `["/bin/sh"]`.

* `args` spécifie les arguments à passer à la commande à l'intérieur du conteneur, définis comme `["-c", "echo 'The first step of the Workflow'"]`. Cette commande exécutera `echo` pour imprimer "The first step of the Workflow".

3. Appliquez le Workflow à votre cluster :

```bash
$ kubectl -n argo create -f argo-workflow.yaml
```

Voici la sortie :

```bash
workflow.argoproj.io/hello-world-nb42c created
```

## Comment gérer Argo Workflows

1. Pour lister tous les workflows au sein du namespace `argo`, faites ce qui suit :

```bash
$ kubectl -n argo get wf
```

Voici la sortie :

```bash
NAME                      STATUS        AGE     MESSAGE
demo-workflow             Succeeded     4m23s
```

2. Pour voir les logs du pod pour votre Workflow, faites ce qui suit :

```bash
$ kubectl -n argo logs demo-workflow
```

Voici la sortie :

```bash
This template is the first step of the Workflow
time="2024-02-13T19:56:54.629Z" level=info msg="sub-process exited" argo=true error="<nil>"
```

3. Pour supprimer un workflow, faites ceci :

```bash
$ kubectl -n argo delete wf workflow-name
```

4. Pour suspendre ou reprendre un workflow, faites ceci :

```bash
$ kubectl -n argo suspend wf workflow-name
$ kubectl -n argo resume wf workflow-name
```

5. Pour soumettre un workflow en utilisant l'interface de ligne de commande Argo, faites ceci :

```bash
$ argo submit -n argo workflow.yaml
```

Vous pouvez en apprendre davantage sur Argo Workflows dans leur [documentation officielle](https://argo-workflows.readthedocs.io/en/latest/).

## Conclusion

Vous avez maintenant exploré Argo Workflows et l'avez installé avec succès. Cet outil puissant vous permet de créer une logique en utilisant des DAG ou des étapes individuelles, vous aidant à exécuter diverses tâches à travers différents templates. Vous pouvez également interagir avec vos workflows et suivre leur progression en utilisant des outils comme Argo CLI, Argo UI et Argo Events.

En utilisant Argo Workflows, vous pouvez tirer parti de la scalabilité et de la flexibilité de Kubernetes pour assurer une exécution fiable des tâches.