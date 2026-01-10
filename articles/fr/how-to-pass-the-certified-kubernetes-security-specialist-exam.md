---
title: Comment réussir l'examen Certified Kubernetes Security Specialist - Guide de
  révision et aide-mémoire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-08T17:40:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-pass-the-certified-kubernetes-security-specialist-exam
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/cks.jpeg
tags:
- name: cheatsheet
  slug: cheatsheet
- name: 'exam '
  slug: exam
- name: Kubernetes
  slug: kubernetes
seo_title: Comment réussir l'examen Certified Kubernetes Security Specialist - Guide
  de révision et aide-mémoire
seo_desc: 'By Faizan Bashir

  This article is based on my experience studying for and passing the Certified Kubernetes
  Security Specialist exam. I passed the exam on my first attempt in Sep 2021.

  I passed the Certified Kubernetes Application Developer exam back i...'
---

Par Faizan Bashir

Cet article est basé sur mon expérience d'étude et de réussite de l'examen Certified Kubernetes Security Specialist. J'ai réussi l'examen à ma première tentative en septembre 2021.

J'ai passé l'examen Certified Kubernetes Application Developer en février 2020, suivi de Certified Kubernetes Administrator en mars 2020. 

L'examen Certified Kubernetes Security Specialist ou CKS a été lancé autour de novembre 2020, mais je n'ai pas eu l'occasion de passer cet examen avant septembre 2021.

À titre d'information, je travaille avec Kubernetes depuis presque 3 ans sur une base quotidienne, et cette expérience a été un avantage supplémentaire pour m'aider à réussir le CKS.

Dans cet article, je vais partager quelques ressources qui devraient vous aider à étudier et à réussir l'examen, ainsi qu'un aide-mémoire utile que vous pouvez utiliser pendant votre préparation. Je vais également partager quelques conseils qui devraient vous aider tout au long du processus.

### Qu'est-ce que Kubernetes ?

Kubernetes est le système d'orchestration de conteneurs le plus évolué et le plus riche en fonctionnalités disponible, et il ne cesse de s'améliorer. 

Il bénéficie d'une énorme communauté pour le soutenir, et il développe constamment de nouvelles fonctionnalités et résout des problèmes. Kubernetes évolue certainement à un rythme effréné, et il devient un défi de suivre son rythme de développement. Cela en fait le meilleur choix pour une solution d'orchestration de conteneurs.

***
## Table des matières :

* [Ressources pour l'examen CKS](#heading-ressources-pour-lexamen)
* [Aliases](#heading-aliases)
    * [vi defaults pour ~/.vimrc](#heading-vi-defaults-pour-vimrc)
    * [kubectl defaults pour ~/.bashrc](#heading-kubectl-defaults-pour-bashrc)
* [Raccourcis](#heading-raccourcis)
* [Aide-mémoire Kubernetes](#heading-aide-memoire-kubernetes)
    * [Commande kubectl run](#heading-commande-kubectl-run)
    * [Comment générer une spécification yaml à partir d'un pod existant](#heading-comment-generer-une-specification-yaml-a-partir-dun-pod-existent)
    * [Commandes kubectl pod](#heading-commandes-kubectl-pod)
    * [Comment imprimer les logs et les exporter](#heading-comment-imprimer-les-logs-et-les-exporter)
    * [Comment créer des configmaps et des secrets](#heading-comment-creer-des-configmaps-et-des-secrets)
    * [Commandes utiles pour le débogage](#heading-commandes-utiles-pour-le-debogage)
    * [Mises à jour et déploiements progressifs](#heading-mises-a-jour-et-deploiements-progressifs)
    * [Commande de mise à l'échelle et d'auto-scaling](#heading-commande-de-mise-a-lechelle-et-dauto-scaling)
    * [Politique de réseau](#heading-politique-de-reseau)
    * [Analyse statique utilisant Kubesec](#heading-analyse-statique-utilisant-kubesec)
    * [Scan de vulnérabilités utilisant Trivvy](#heading-scan-de-vulnerabilites-utilisant-trivvy)
    * [Comment supprimer les services indésirables](#heading-comment-supprimer-les-services-indesirables)
    * [Classes d'exécution](#heading-classes-dexecution)
    * [Commandes RBAC](#heading-commandes-rbac)
    * [Maintenance du cluster](#heading-maintenance-du-cluster)
* [Conseils pour l'examen CKS](#heading-conseils-pour-lexamen-cks)
    * [JSON et JSONPath](#heading-json-et-jsonpath)
* [Sujets de l'examen CKS](#heading-sujets-de-lexamen-cks)
    * [Comment sécuriser et renforcer les images de conteneurs](#heading-comment-securiser-et-renforcer-les-images-de-conteneurs)
    * [Comment minimiser l'empreinte du système d'exploitation](#heading-comment-minimiser-lempreinte-du-systeme-dexploitation)
        * [Couches de conteneur](#heading-couches-de-conteneur)
        * [Builds multi-étapes](#heading-builds-multi-etapes)
    * [Comment limiter l'accès aux nœuds](#heading-comment-limiter-lacces-aux-noeuds)
    * [Renforcement SSH](#heading-renforcement-ssh)
        * [Comment désactiver SSH](#heading-comment-desactiver-ssh)
        * [Comment supprimer les paquets et services obsolètes](#heading-comment-supprimer-les-paquets-et-services-obsoletes)
        * [Comment restreindre les modules du noyau](#heading-comment-restreindre-les-modules-du-noyau)
        * [Comment identifier et désactiver les ports ouverts](#heading-comment-identifier-et-desactiver-les-ports-ouverts)
    * [Comment restreindre l'accès réseau](#heading-comment-restreindre-lacces-reseau)
        * [Comment identifier un service en cours d'exécution sur un port](#heading-comment-identifier-un-service-en-cours-dexecution-sur-un-port)
        * [Pare-feu UFW](#heading-pare-feu-ufw)
    * [Appels système Linux](#heading-appels-systeme-linux)
        * [Comment tracer les appels système en utilisant Strace](#heading-comment-tracer-les-appels-systeme-en-utilisant-strace)
    * [AquaSec tracee](#heading-aquasec-tracee)
    * [Comment restreindre les appels système avec Seccomp](#heading-comment-restreindre-les-appels-systeme-avec-seccomp)
        * [Seccomp dans Kubernetes](#heading-seccomp-dans-kubernetes)
    * [AppArmor](#heading-apparmor)
        * [Comment utiliser AppArmor dans Kubernetes](#heading-comment-utiliser-apparmor-dans-kubernetes)
    * [Capacités Linux](#heading-capacites-linux)
* [Comment se préparer à l'examen](#heading-comment-se-preparer-a-lexamen)
* [Pratique, pratique et pratique !](#heading-pratique-pratique-et-pratique)
***

## Ressources pour l'examen

Voici quelques ressources disponibles pour réussir l'examen CKS :
1. [Certified Kubernetes Security Specialist by Killer.sh](https://www.udemy.com/course/certified-kubernetes-security-specialist/) 
2. [Certified Kubernetes Security Specialist (CKS) by KodeKloud](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks/)
3. [Walid Shaari a rassemblé des matériaux indispensables pour l'examen CKS](https://github.com/walidshaari/Certified-Kubernetes-Security-Specialist)
4. [Références d'Abdennour pour les objectifs de l'examen CKS](https://github.com/abdennour/certified-kubernetes-security-specialist)
5. [Collection de ressources d'Ibrahim Jelliti pour se préparer à l'examen Certified Kubernetes Security Specialist (CKSS)](https://github.com/ibrahimjelliti/CKSS-Certified-Kubernetes-Security-Specialist)

Les cours de KodeKloud et Killer.sh fournissent des simulateurs d'examen qui sont très utiles pour se préparer à l'examen et donnent une assez bonne idée de ce à quoi ressemble l'examen. Je suggère fortement de s'inscrire à un ou aux deux cours. 

L'achat de l'examen auprès de la Linux Foundation vous donne 2 tentatives gratuites au simulateur d'examen de killer.sh. Ainsi, si vous maîtrisez bien le contenu du programme, vous pouvez sauter les cours et aller directement au simulateur d'examen fourni avec l'examen.

L'examen coûte 375 $, mais il existe des offres et des promotions disponibles, et si vous les cherchez, vous pourriez obtenir un meilleur prix. La durée de l'examen est de 2 heures et il est valable pour 2 ans, contrairement au CKA et au CKAD qui sont valables pour 3 ans.

## Aliases

Le CKS est un examen basé sur la performance où vous disposez d'un simulateur d'examen dans lequel vous devez résoudre les problèmes. Vous êtes autorisé à ouvrir seulement un onglet en plus de l'onglet de l'examen. 

Étant donné que cet examen nécessite d'écrire beaucoup de commandes, j'ai rapidement compris que je devrais m'appuyer sur des alias pour réduire le nombre de frappes et gagner du temps.

J'ai utilisé l'éditeur **vi** pendant l'examen, donc voici quelques conseils utiles pour cet éditeur.

### vi defaults pour ~/.vimrc :

```
vi ~/.vimrc
---
:set number
:set et
:set sw=2 ts=2 sts=2
---
^ : Début de mot dans la ligne
0 : Début de ligne
$ : Fin de ligne
w : Fin de mot
GG : Fin de fichier
```

### kubectl defaults pour ~/.bashrc :

```
vi ~/.bashrc
---
alias k='kubectl'
alias kg='k get'
alias kd='k describe'
alias kl='k logs'
alias ke='k explain'
alias kr='k replace'
alias kc='k create'
alias kgp='k get po'
alias kgn='k get no'
alias kge='k get ev'
alias kex='k exec -it'
alias kgc='k config get-contexts'
alias ksn='k config set-context --current --namespace'
alias kuc='k config use-context'
alias krun='k run'
export do='--dry-run=client -oyaml'
export force='--grace-period=0 --force'

source <(kubectl completion bash)
source <(kubectl completion bash | sed 's/kubectl/k/g' )
complete -F __start_kubectl k


alias krp='k run test --image=busybox --restart=Never'
alias kuc='k config use-context'
---
```

## Raccourcis

La commande `kubectl get` fournit des noms courts et accrocheurs pour accéder aux ressources, comme `pvc` pour `persistentstorageclaim`. Ceux-ci peuvent aider à économiser beaucoup de frappes et de temps précieux pendant l'examen.

* **po** pour `pods`
* **rs** pour `replicasets`
* **deploy** pour `deployments`
* **svc** pour `services`
* **ns** pour `namespace`
* **netpol** pour `networkpolicy`
* **pv** pour `persistentstorage`
* **pvc** pour `persistentstorageclaim`
* **sa** pour `serviceaccounts`

## Aide-mémoire Kubernetes

### Commande kubectl run

La commande `kubectl run` fournit un flag `--restart` qui permet de créer différents types d'objets Kubernetes, d'un Deployment à un CronJob. 

L'extrait ci-dessous montre les différentes options disponibles pour le flag `--restart`.

```
k run:
--restart=Always                             #Crée un deployment
--restart=Never                              #Crée un Pod
--restart=OnFailure                          #Crée un Job
--restart=OnFailure --schedule="*/1 * * * *" #Crée un CronJob
```

### Comment générer une spécification yaml à partir d'un pod existant

Parfois, il est plus facile de générer une spécification à partir d'un pod existant et d'y apporter des modifications plutôt que d'en créer une nouvelle à partir de zéro. La commande `kubectl get pod` fournit les flags nécessaires pour sortir la spécification du pod dans le format souhaité.

```
kgp <pod-name> -o wide

# Génération de la spécification YAML du Pod
kgp <pod-name> -o yaml
kgp <pod-name> -o yaml > <pod-name>.yaml

# Obtenir la spécification YAML d'un pod sans les informations spécifiques au cluster
kgp my-pod -o yaml --export > <pod-name>.yaml
```

### Commandes kubectl pod

La commande `kubectl run` offre de nombreuses options, comme la spécification des requêtes et des limites qu'un pod est censé utiliser ou les commandes qu'un conteneur doit exécuter une fois créé.

```
# Sortie YAML pour un pod nginx exécutant une commande echo
krun nginx --image=nginx --restart=Never --dry-run -o yaml -- /bin/sh -c 'echo Hello World!'
# Sortie YAML pour un pod busybox exécutant une commande sleep
krun busybox --image=busybox:1.28 --restart=Never --dry-run -o yaml -- /bin/sh -c 'while true; do echo sleep; sleep 10; done'
# Exécuter un pod avec des requêtes et des limites définies
krun nginx --image=nginx --restart=Never --requests='cpu=100m,memory=512Mi' --limits='cpu=300m,memory=1Gi'
# Supprimer le pod sans délai
k delete po busybox --grace-period=0 --force
```

### Comment imprimer les logs et les exporter

Les logs sont la source fondamentale d'informations lorsqu'il s'agit de déboguer une application. La commande `kubectl logs` fournit la fonctionnalité pour vérifier les logs d'un pod donné. Vous pouvez utiliser les commandes ci-dessous pour vérifier les logs d'un pod donné.
```
kubectl logs deploy/<podname>
kubectl logs deployment/<podname>
#Suivre les logs
kubectl logs deploy/<podname> --tail 1 --follow
```

En plus de simplement regarder les logs, nous pouvons également exporter les logs vers un fichier pour un débogage ultérieur ou pour les partager avec quelqu'un.
```
kubectl logs <podname> --namespace <ns> > /path/to/file.format
```

### Comment créer des config maps et des secrets

La commande `kubectl create` nous permet de créer des ConfigMaps et des Secrets à partir de la ligne de commande. Nous pouvons également utiliser le fichier YAML pour créer les mêmes ressources et en utilisant `kubectl apply -f <filename>` nous pouvons appliquer les commandes.
```
kc cm my-cm --from-literal=APP_ENV=dev
kc cm my-cm --from-file=test.txt
kc cm my-cm --from-env-file=config.env

kc secret generic my-secret --from-literal=APP_SECRET=sdcdcsdcsdcsdc
kc secret generic my-secret --from-file=secret.txt
kc secret generic my-secret --from-env-file=secret.env
```

### Commandes utiles pour le débogage

Le débogage est une compétence très importante lorsque vous êtes confronté à des problèmes et des erreurs, tant dans notre travail quotidien que lors de la résolution de problèmes dans l'examen CKS. 

En plus de la capacité à sortir les logs d'un conteneur, la commande `kubectl exec` vous permet de vous connecter à un conteneur en cours d'exécution et de déboguer les problèmes. À l'intérieur du conteneur, vous pouvez également utiliser des utilitaires comme `nc` et `nslookup` pour diagnostiquer les problèmes liés au réseau.
```
# Exécuter le conteneur busybox
k run busybox --image=busybox:1.28 --rm --restart=Never -it sh
# Se connecter à un conteneur spécifique dans un Pod
k exec -it busybox -c busybox2 -- /bin/sh
# ajouter des limites et des requêtes dans la commande
kubectl run nginx --image=nginx --restart=Never --requests='cpu=100m,memory=256Mi' --limits='cpu=200m,memory=512Mi'
# Créer un Pod avec un service
kubectl run nginx --image=nginx --restart=Never --port=80 --expose
# Vérifier le port
nc -z -v -w 2 <service-name> <port-name>
# NSLookup
nslookup <service-name>
nslookup 10-32-0-10.default.pod
```

### Mises à jour et déploiements progressifs

La commande `kubectl rollout` fournit la capacité de vérifier l'état des mises à jour et, si nécessaire, de revenir à une version précédente.
```
k set image deploy/nginx nginx=nginx:1.17.0 --record
k rollout status deploy/nginx
k rollout history deploy/nginx
# Retour à la version précédente
k rollout undo deploy/nginx
# Retour à un numéro de révision
k rollout undo deploy/nginx --to-revision=2
k rollout pause deploy/nginx
k rollout resume deploy/nginx
k rollout restart deploy/nginx
kubectl run nginx-deploy --image=nginx:1.16 --replias=1 --record
```

### Commande de mise à l'échelle et d'auto-scaling

La commande `kubectl scale` fournit la fonctionnalité de mettre à l'échelle ou de réduire les pods dans un déploiement donné. 

En utilisant la commande `kubectl autoscale`, nous pouvons définir le nombre minimum de pods qui doivent être en cours d'exécution pour un déploiement donné et le nombre maximum de pods que le déploiement peut mettre à l'échelle, ainsi que les critères de mise à l'échelle comme le pourcentage de CPU.
```
k scale deploy/nginx --replicas=6
k autoscale deploy/nginx --min=3 --max=9 --cpu-percent=80
```

### Politique de réseau

Dans un cluster Kubernetes, tous les pods peuvent communiquer avec tous les pods par défaut, ce qui peut poser un problème de sécurité dans certaines implémentations. 

Pour contourner ce problème, Kubernetes a introduit les Network Policies pour permettre ou refuser le trafic vers et depuis les pods en fonction des étiquettes de pod qui font partie de la spécification du pod.

L'exemple ci-dessous refuse à la fois le trafic Ingress et Egress pour les pods en cours d'exécution dans tous les namespaces. 
```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: example
  namespace: default
spec:
  podSelector: {}
  policyTypes:
  - Egress
  - Ingress
```

L'exemple ci-dessous refuse à la fois le trafic Ingress et Egress pour les pods en cours d'exécution dans tous les namespaces. Mais il permet l'accès aux services de résolution DNS en cours d'exécution sur le port 53.
```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny
  namespace: default
spec:
  podSelector: {}
  policyTypes:
  - Egress
  - Ingress
  egress:
  - to:
    ports:
      - port: 53
        protocol: TCP
      - port: 53
        protocol: UDP
```

L'exemple ci-dessous refuse l'accès Egress au serveur de métadonnées en cours d'exécution sur l'adresse IP `169.256.169.256` dans les instances AWS EC2.
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name:cloud-metadata-deny
  namespace: default
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
      - ipBlock: 
          cidr: 0.0.0.0/0
          except:
          - 169.256.169.256/32
```

L'exemple ci-dessous permet l'accès Egress au serveur de métadonnées en cours d'exécution sur l'adresse IP `169.256.169.256` dans les instances AWS EC2.
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: cloud-metadata-accessor
  namespace: default
spec:
  podSelector:
    matchLabels:
      role: metadata-accessor
  policyTypes:
  - Egress
  egress:
  - to:
    - ipBlock:
        cidr: 169.256.169.256/32
```

### Analyse statique utilisant Kubesec

Kubesec est un outil d'analyse statique pour analyser les fichiers YAML afin de trouver des problèmes avec les fichiers.
```
kubesec scan pod.yaml

# Utilisation de l'API kubesec en ligne
curl -sSX POST --data-binary @pod.yaml https://v2.kubesec.io/scan

# Exécution de l'API localement
kubesec http 8080 &

kubesec scan pod.yaml -o pod_report.json -o json
```

### Scan de vulnérabilités utilisant Trivvy

Trivvy est un outil de scan de vulnérabilités qui scanne les images de conteneurs pour détecter les problèmes de sécurité.
```
trivy image nginx:1.18.0
trivy image --severity CRITICAL nginx:1.18.0
trivy image --severity CRITICAL, HIGH nginx:1.18.0
trivy image --ignore-unfixed nginx:1.18.0

# Scan d'une archive d'image
docker save nginx:1.18.0 > nginx.tar
trivy image --input archive.tar

# Scan et sortie des résultats vers un fichier
trivy image --output python_alpine.txt python:3.10.0a4-alpine
trivy image --severity HIGH --output /root/python.txt python:3.10.0a4-alpine

# Scan d'une archive d'image
trivy image --input alpine.tar --format json --output /root/alpine.json
```

### Comment supprimer les services indésirables

La commande `systemctl` expose les capacités de démarrer, arrêter, activer, désactiver et lister les services en cours d'exécution sur une machine virtuelle Linux.

Lister les services :
```
systemctl list-units --type service
```
Arrêter un service :
```
systemctl stop apache2
```
Désactiver un service :
```
systemctl disable apache2
```
Supprimer un service :
```
apt remove apache2
```

### Classes d'exécution

Kubernetes a introduit la fonctionnalité RuntimeClass dans la version `v1.12` pour sélectionner la configuration du runtime de conteneur. La configuration du runtime de conteneur est utilisée pour exécuter les conteneurs sous-jacents d'un pod. 

La plupart des clusters Kubernetes utilisent le `dockershim` comme classe Runtime pour les conteneurs en cours d'exécution, mais vous pouvez utiliser différents runtimes de conteneurs. 

Le `dockershim` a été déprécié dans la version `v1.20` de Kubernetes, et sera supprimé dans la `v1.24`.

Comment créer une Runtime Class :
```
apiversion: node.k8s.io/v1beta1
kind: RuntimeClass
metadata:
  name: gvisor
handler: runsc
```
Comment utiliser une classe d'exécution pour un pod donné :
```
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: nginx
  name: nginx
spec:
  runtimeClassName: gvisor
  containers:
  - name: nginx
    image: nginx 
```

### Commandes RBAC

Dans Kubernetes, 

> Le contrôle d'accès basé sur les rôles (RBAC) fournit une méthode de régulation de l'accès aux ressources Kubernetes basée sur les rôles des utilisateurs individuels ou des comptes de service. ([Source](https://kubernetes.io/docs/reference/access-authn-authz/rbac/))

Voici comment créer un rôle :
```
kubectl create role developer --resource=pods --verb=create,list,get,update,delete --namespace=development
```

Comment créer une liaison de rôle :
```
kubectl create rolebinding developer-role-binding --role=developer --user=faizan --namespace=development
```

Comment valider :
```
kubectl auth can-i update pods --namespace=development --as=faizan
```

Comment créer un rôle de cluster :
```
kubectl create clusterrole pvviewer-role --resource=persistentvolumes --verb=list
```

Et comment créer une liaison de rôle de cluster avec un compte de service :
```
kubectl create clusterrolebinding pvviewer-role-binding --clusterrole=pvviewer-role --serviceaccount=default:pvviewer
```

### Maintenance du cluster

Vous utilisez la commande `kubectl drain` pour supprimer toutes les charges de travail en cours (pods) d'un nœud donné. 

Vous utilisez la commande `kubectl cordon` pour marquer un nœud comme non planifiable. 

Et vous utilisez la commande `kubectl uncordon` pour marquer le nœud comme planifiable, ce qui signifie que le Controller Manager peut planifier de nouveaux pods sur le nœud donné.

Comment vider un nœud de tous les pods :
```
kubectl drain node-1
```

Comment vider un nœud et ignorer les daemonsets :
```
kubectl drain node01 --ignore-daemonsets
```

Comment forcer le vidage :
```
kubectl drain node02 --ignore-daemonsets --force
```

Comment marquer un nœud comme non planifiable, afin qu'aucun nouveau pod ne puisse être planifié sur ce nœud :
```
kubectl cordon node-1
```
Marquer un nœud comme planifiable
```
kubectl uncordon node-1
```

## Conseils pour l'examen CKS

La commande Kubernetes `kubectl get` fournit à l'utilisateur un flag de sortie, `-o` ou `--output`, qui nous aide à formater la sortie sous forme de JSON, yaml, wide, ou custom-columns.

### JSON et JSONPath

Comment sortir le contenu de tous les pods sous forme d'objet JSON :
```
kubectl get pods -o json
```

Le JSONPath sort une clé spécifique de l'objet JSON :
```
kubectl get pods -o=jsonpath='{@}'
kubectl get pods -o=jsonpath='{.items[0]}'
```

Le `.items[*]` est utilisé lorsque nous avons plusieurs objets, par exemple plusieurs conteneurs avec une configuration de pod :
```
# Pour une liste d'objets, utilisez .items[*]
k get pods -o 'jsonpath={.items[*].metadata.labels.version}'
# Pour un seul objet
k get po busybox -o jsonpath='{.metadata}'
k get po busybox -o jsonpath="{['.metadata.name', '.metadata.namespace']}{'\n'}"
```

La commande retourne l'IP interne d'un nœud en utilisant JSONPath :
```
kubectl get nodes -o=jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}'
```

La commande vérifie l'égalité sur une clé spécifique :
```
kubectl get pod api-stag-765797cf-lrd8q -o=jsonpath='{.spec.volumes[?(@.name=="api-data")].persistentVolumeClaim.claimName}'
kubectl get pod -o=jsonpath='{.items[*].spec.tolerations[?(@.effect=="NoSchedule")].key}'
```

Les colonnes personnalisées sont utiles pour sortir des champs spécifiques :
```
kubectl get pods -o='custom-columns=PODS:.metadata.name,Images:.spec.containers[*].image'
```

## Sujets de l'examen CKS

L'examen CKS couvre des sujets liés à la sécurité dans l'écosystème Kubernetes. La sécurité Kubernetes est un vaste sujet à couvrir dans un seul article, donc cet article contient certains des sujets couverts dans l'examen.

### Comment sécuriser et renforcer les images de conteneurs

Lors de la conception d'images de conteneurs pour exécuter votre code, portez une attention particulière aux mesures de sécurisation et de renforcement afin de prévenir les piratages et les attaques par élévation de privilèges. Gardez les points suivants à l'esprit lors de la création des images de conteneurs :

1. Utilisez des versions spécifiques de paquets comme `alpine:3.13`.
2. Ne pas exécuter en tant que root - utilisez `USER <username>` pour bloquer l'accès root.
3. Rendre le système de fichiers en lecture seule dans le `securityContext` en utilisant `readOnlyRootFilesystem: true`
4. Supprimer l'accès shell en utilisant `RUN rm -rf /bin/*`

### Comment minimiser l'empreinte du système d'exploitation

#### Couches de conteneur

Les instructions `RUN`, `COPY` et `ADD` créent des couches de conteneur. Les autres instructions créent des images intermédiaires temporaires et n'augmentent pas la taille de la construction. Les instructions qui créent des couches ajoutent à la taille de l'image résultante.

Un Dockerfile typique ressemble à celui donné ci-dessous. Il ajoute une seule couche en utilisant l'instruction `RUN`.
```
FROM ubuntu

RUN apt-get update && apt-get install -y golang-go

CMD ["sh"]
```

#### Builds multi-étapes

Les builds multi-étapes exploitent plusieurs instructions `FROM` dans le Dockerfile. L'instruction `FROM` marque une nouvelle étape dans la construction. Elle combine plusieurs instructions `FROM` pour tirer parti de la construction précédente afin de copier sélectivement des binaires vers la nouvelle étape de construction en omettant les binaires inutiles. L'image Docker résultante est considérablement plus petite avec une surface d'attaque drastiquement réduite.

```
FROM ubuntu:20.04 AS build
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y golang-go
COPY app.go .
RUN CGO_ENABLED=0 go build app.go

FROM alpine:3.13
RUN chmod a-w /etc
RUN addgroup -S appgroup && adduser -S appuser -G appgroup -h /home/appuser
RUN rm -rf /bin/*
COPY --from=build /app /home/appuser/
USER appuser
CMD ["/home/appuser/app"]
```

### Comment limiter l'accès aux nœuds

Les fichiers de contrôle d'accès contiennent des informations sensibles sur les utilisateurs/groupes dans le système d'exploitation Linux.
```
#Stocke les informations sur l'UID/GID, le shell utilisateur et le répertoire personnel pour un utilisateur
/etc/passwd
#Stocke le mot de passe de l'utilisateur dans un format haché
/etc/shadow
#Stocke les informations sur le groupe auquel appartient un utilisateur
/etc/group
#Stocke les informations sur les Sudoers présents dans le système
/etc/sudoers
```

La désactivation d'un compte utilisateur aide à sécuriser l'accès à un nœud en désactivant la connexion à un compte utilisateur donné.
```
usermod -s /bin/nologin <username>
```

La désactivation du compte utilisateur `root` est d'une importance particulière, car le compte root a toutes les capacités.
```
usermod -s /bin/nologin root
```

Voici comment ajouter un utilisateur avec un répertoire personnel et un shell :
```
adduser --home /opt/faizanbashir --shell /bin/bash --uid 2328 --ingroup admin faizanbashir
useradd -d /opt/faizanbashir -s /bin/bash -G admin -u 2328 faizanbashir
```

Comment supprimer le compte utilisateur :
```
userdel <username>
```

Comment supprimer un groupe :
```
groupdel <groupname>
```

Comment ajouter un utilisateur à un groupe :
```
adduser <username> <groupname>
```

Comment supprimer un utilisateur d'un groupe :
```
#deluser faizanbashir admin
deluser <username> <groupname>
```

Comment définir un mot de passe pour un utilisateur :
```
passwd <username>
```

Comment élever un utilisateur au statut de sudoer :
```
vim /etc/sudoers
>>>
faizanbashir ALL=(ALL:ALL) ALL
```

Comment activer sudo sans mot de passe :
```
vim /etc/sudoers
>>>
faizanbashir ALL=(ALL) NOPASSWD:ALL

visudo
usermod -aG sudo faizanbashir
usermod faizanbashir -G admin
```

### Renforcement SSH

#### Comment désactiver SSH

La configuration donnée dans `/etc/ssh/sshd_config` peut être utilisée pour sécuriser l'accès SSH aux nœuds Linux. La définition de `PermitRootLogin` à `no` désactive la connexion root sur un nœud. 

Pour imposer l'utilisation d'une clé pour se connecter et désactiver la connexion par mot de passe aux nœuds, vous pouvez définir `PasswordAuthentication` à `no`.
```
vim /etc/ssh/sshd_config
>>
PermitRootLogin no
PasswordAuthentication no
<<
# Redémarrer le service SSHD
systemctl restart sshd
```

Comment définir aucune connexion pour l'utilisateur root :
```
usermod -s /bin/nologin root
```

Copie de la clé utilisateur SSH / SSH sans mot de passe :
```
ssh-copy-id -i ~/.ssh/id_rsa.pub faizanbashir@node01
ssh faizanbashir@node01
```

### Comment supprimer les paquets et services obsolètes

Voici comment vous pouvez lister tous les services en cours d'exécution sur une machine Ubuntu :
```
systemctl list-units --type service
systemctl list-units --type service --state running
```

Comment arrêter, désactiver et supprimer un service :
```
systemctl stop apache2
systemctl disable apache2
apt remove apache2
```

### Comment restreindre les modules du noyau

Dans Linux, les modules du noyau sont des morceaux de code qui peuvent être chargés et déchargés dans le noyau à la demande. Ils étendent la fonctionnalité du noyau sans avoir besoin de redémarrer le système. Un module peut être configuré comme intégré ou chargeable.

Comment lister tous les modules du noyau :
```
lsmod
```

Comment charger manuellement des modules dans un noyau :
```
modprobe pcspkr
```

Comment blacklister un module : (Référence : CIS Benchmarks -> 3.4 Protocoles réseau peu courants)
```
cat /etc/modprobe.d/blacklist.conf
>>>
blacklist sctp
blacklist dccp

# Arrêt pour que les modifications prennent effet
shutdown -r now

# Vérifier
lsmod | grep dccp
```

### Comment identifier et désactiver les ports ouverts

Comment vérifier les ports ouverts :
```
netstat -an | grep -w LISTEN
netstat -natp | grep 9090

nc -zv <hostname|IP> 22
nc -zv <hostname|IP> 10-22

ufw deny 8080
```

Comment vérifier l'utilisation des ports :
```
/etc/services | grep -w 53
```

Voici le document de référence pour une [liste des ports ouverts](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#control-plane-node-s).

### Comment restreindre l'accès réseau

#### Comment identifier un service en cours d'exécution sur un port :
```
systemctl status ssh
cat /etc/services | grep ssh
netstat -an | grep 22 | grep -w LISTEN
```

#### Pare-feu UFW

Uncomplicated Fire Wall (UFW) est un outil pour gérer les règles de pare-feu dans Arch Linux, Debian ou Ubuntu. UFW vous permet d'autoriser et de bloquer le trafic sur un port donné et à partir d'une source donnée.

Voici comment installer le pare-feu UFW :
```
apt-get update
apt-get install ufw
systemctl enable ufw
systemctl start ufw
ufw status
ufw status numbered
```

Comment autoriser toutes les connexions sortantes et entrantes :
```
ufw default allow outgoing
ufw default allow incoming
```

Comment autoriser les règles :
```
ufw allow 22
ufw allow 1000:2000/tcp
ufw allow from 172.16.238.5 to any port 22 proto tcp
ufw allow from 172.16.238.5 to any port 80 proto tcp
ufw allow from 172.16.100.0/28 to any port 80 proto tcp
```

Comment refuser les règles :
```
ufw deny 8080
```

Comment activer et activer le pare-feu :
```
ufw enable
```

Comment supprimer les règles :
```
ufw delete deny 8080
ufw delete <rule-line>
```

Comment réinitialiser les règles :
```
ufw reset
```

### Appels système Linux

Les appels système Linux sont utilisés pour faire des requêtes depuis l'espace utilisateur vers le noyau Linux. Par exemple, lors de la création d'un fichier, l'espace utilisateur fait une requête au noyau Linux pour créer le fichier. 

L'espace noyau contient les éléments suivants :
- Code du noyau
- Extensions du noyau
- Pilotes de périphériques

#### Comment tracer les appels système en utilisant Strace

Voici comment vous pouvez tracer les appels système en utilisant strace :
```
which strace
strace touch /tmp/error.log
```

Comment obtenir le PID d'un service :
```
pidof sshd
strace -p <pid>
```

Comment lister tous les appels système effectués pendant une opération :
```
strace -c touch /tmp/error.log
```

Comment consolider la liste des appels système : (Compter et résumer)
```
strace -cw ls /
```

Comment suivre un PID et consolider :
```
strace -p 3502 -f -cw
```

### AquaSec Tracee

AquaSec Tracee a été créé par Aqua Security qui utilise eBPF pour tracer les événements dans les conteneurs. Tracee utilise eBPF (Extended Berkeley Packet Filter) au runtime directement dans l'espace noyau sans interférer avec la source du noyau ou charger des modules noyau.

- Binaire stocké dans `/tmp/tracee`
- Nécessite l'accès aux éléments suivants, en mode lecture seule si exécuté en utilisant un conteneur avec la capacité `--privileged` :
	- `/tmp/tracee` -> Espace de travail par défaut
	- `/lib/modules` -> En-têtes du noyau
	- `/usr/src` -> En-têtes du noyau

Comment exécuter Tracee dans un conteneur Docker :
```
docker run --name tracee --rm --privileged --pid=host \
  -v /lib/modules/:/lib/modules/:ro -v /usr/src/:/usr/src/ro \
  -v /tmp/tracee:/tmp/tracee aquasec/tracee:0.4.0 --trace comm=ls

# Lister les appels système effectués par tous les nouveaux processus sur l'hôte
docker run --name tracee --rm --privileged --pid=host \
  -v /lib/modules/:/lib/modules/:ro -v /usr/src/:/usr/src/ro \
  -v /tmp/tracee:/tmp/tracee aquasec/tracee:0.4.0 --trace pid=new

# Lister les appels système effectués à partir de tout nouveau conteneur
docker run --name tracee --rm --privileged --pid=host \
  -v /lib/modules/:/lib/modules/:ro -v /usr/src/:/usr/src/ro \
  -v /tmp/tracee:/tmp/tracee aquasec/tracee:0.4.0 --trace container=new
```

### Comment restreindre les appels système avec Seccomp

**SECCOMP** - Secure Computing Mode - est une fonctionnalité au niveau du noyau Linux que vous pouvez utiliser pour sandboxer des applications afin qu'elles n'utilisent que les appels système dont elles ont besoin.

Comment vérifier la prise en charge de seccomp :
```
grep -i seccomp /boot/config-$(uname -r)
```

Comment tester le changement de l'heure système :
```
docker run -it --rm docker/whalesay /bin/sh
# date -s '19 APR 2013 22:00:00'

ps -ef
```

Comment vérifier le statut seccomp pour un PID donné :
```
grep -i seccomp /proc/1/status
```

Modes Seccomp :
- Mode 0 : Désactivé
- Mode 1 : Strict
- Mode 2 : Filtré

La configuration suivante est utilisée pour lister les appels système. Le profil de liste blanche est sécurisé, mais les appels système doivent être activés sélectivement car il bloque tous les appels système par défaut.
```
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "names": [
        "<syscall-1>",
        "<syscall-2>",
        "<syscall-3>"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

La configuration suivante est utilisée pour blacklister les appels système. Le profil de blacklist a une surface d'attaque plus grande que la liste blanche. 
```
{
  "defaultAction": "SCMP_ACT_ALLOW",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "names": [
        "<syscall-1>",
        "<syscall-2>",
        "<syscall-3>"
      ],
      "action": "SCMP_ACT_ERRNO"
    }
  ]
}
```

Le profil seccomp de Docker bloque 60 des 300+ appels système sur l'architecture x86.

Comment utiliser les profils seccomp avec Docker :
```
docker run -it --rm --security-opt seccomp=/root/custom.json docker/whalesay /bin/sh
```

Comment autoriser tous les appels système avec le conteneur :
```
docker run -it --rm --security-opt seccomp=unconfined docker/whalesay /bin/sh

# Vérifier
grep -i seccomp /proc/1/status

# La sortie devrait être :
Seccomp:         0
```

Comment utiliser le conteneur Docker pour obtenir des informations liées au runtime du conteneur :
```
docker run r.j3ss.co/amicontained amicontained
```

#### Seccomp dans Kubernetes

Le mode de calcul sécurisé (SECCOMP) est une fonctionnalité du noyau Linux. Vous pouvez l'utiliser pour restreindre les actions disponibles dans le conteneur. [Documentation Seccomp](https://kubernetes.io/docs/tutorials/clusters/seccomp)

Comment exécuter amicontained dans Kubernetes :
```
kubectl run amicontained --image r.j3ss.co/amicontained amicontained -- amicontained
```

À partir de la version `v1.20`, Kubernetes n'implémente pas seccomp par défaut.

Profil seccomp 'RuntimeDefault' de Docker dans Kubernetes :
```
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: amicontained
  name: amicontained
spec:
  securityContext:
    seccompProfile:
      type: RuntimeDefault
  containers:
  - args:
    - amicontained
    image: r.j3ss.co/amicontained
    name: amicontained
    securityContext:
      allowPrivilegeEscalation: false
```

Emplacement par défaut de seccomp dans les kubelets
```
/var/lib/kubelet/seccomp
```

Comment créer un profil seccomp dans un nœud :
```
mkdir -p /var/lib/kubelet/seccomp/profiles

# Ajouter un profil pour l'audit
vim /var/lib/kubelet/seccomp/profiles/audit.json
>>>
{
  defaultAction: "SCMP_ACT_LOG"
}

# Ajouter un profil pour les violations (Bloque tous les appels système par défaut, ne laissera rien s'exécuter)
vim /var/lib/kubelet/seccomp/profiles/violation.json
>>>
{
  defaultAction: "SCMP_ACT_ERRNO"
}
```

Profil seccomp local - ce fichier doit exister localement sur un nœud pour pouvoir fonctionner :

```
...
securityContext:
  seccompProfile:
    type: Localhost
    localhostProfile: profiles/audit.json
...
```

Le profil ci-dessus permettra d'enregistrer les appels système dans un fichier.
```
grep syscall /var/log/syslog
```

Comment mapper les numéros d'appels système aux noms d'appels système :
```
grep -w 35 /usr/include/asm/unistd_64.h

# OU
grep -w 35 /usr/include/asm-generic/unistd.h
```

### AppArmor

AppArmor est un module de sécurité Linux utilisé pour confiner un programme à un ensemble limité de ressources.

Comment installer les utilitaires AppArmor :
```
apt-get install apparmor-utils
```

Comment vérifier si AppArmor est en cours d'exécution et activé :
```
systemctl status apparmor

cat /sys/module/apparmor/parameters/enabled
Y
```

Les profils AppArmor sont stockés dans :
```
cat /etc/apparmor.d/root.add_data.sh
```

Comment lister les profils AppArmor :
```
cat /sys/kernel/security/apparmor/profiles
```

Comment refuser toutes les écritures de fichiers :
```
profile apparmor-deny-write flags=(attach_disconnected) {
  file,
  # Refuser toutes les écritures de fichiers.
  deny /** w,
}
```

Comment refuser l'écriture dans les fichiers `/proc` :
```
profile apparmor-deny-proc-write flags=(attach_disconnected) {
  file,
  # Refuser toutes les écritures de fichiers.
  deny /proc/* w,
}
```

Comment refuser le remontage du système de fichiers racine :
```
profile apparmor-deny-remount-root flags=(attach_disconnected) {

  # Refuser toutes les écritures de fichiers.
  deny mount options=(ro, remount) -> /,
}
```

Comment vérifier le statut du profil :
```
aa-status
```

Modes de chargement des profils
- `Enforce`, surveiller et appliquer les règles
- `Complain`, n'appliquera pas les règles mais les enregistrera comme événements
- `Unconfined`, n'appliquera pas ou ne journalisera pas les événements

Comment vérifier si un profil est valide :
```
apparmor_parser /etc/apparmor.d/root.add_data.sh
```

Comment désactiver un profil :
```
apparmor_parser -R /etc/apparmor.d/root.add_data.sh
ln -s /etc/apparmor.d/root.add_data.sh /etc/apparmor.d/disable/
```

Comment générer un profil et répondre à la série de questions qui suivent :
```
aa-genprof /root/add_data.sh
```

Comment générer un profil pour une commande :
```
aa-genprof curl
```

Comment désactiver le profil à partir des logs :
```
aa-logprof
```

#### Comment utiliser AppArmor dans Kubernetes

Pour utiliser AppArmor avec Kubernetes, les conditions préalables suivantes doivent être remplies :
- La version de Kubernetes doit être supérieure à `1.4`
- Le module noyau AppArmor doit être activé
- Le profil AppArmor doit être chargé dans le noyau
- Le runtime de conteneur doit être supporté

Exemple d'utilisation dans Kubernetes :
```
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
  annotations:
    container.apparmor.security.beta.kubernetes.io/<container-name>: localhost/<profile-name>
spec:
  containers:
  - name: ubuntu-sleeper
    image: ubuntu
    command: ["sh", "-c", "echo 'Sleeping for an hour!' && sleep 1h"]
```

**Note** : Le conteneur doit s'exécuter dans un nœud contenant le profil AppArmor.

### Capacités Linux

La fonctionnalité des capacités Linux divise les privilèges disponibles pour les processus exécutés en tant qu'utilisateur `root` en groupes plus petits de privilèges. Ainsi, un processus s'exécutant avec un privilège `root` peut être limité pour obtenir uniquement les permissions minimales dont il a besoin pour effectuer son opération. 

Docker supporte les capacités Linux dans le cadre de la commande Docker run : avec `--cap-add` et `--cap-drop`. Par défaut, un conteneur est démarré avec plusieurs capacités qui sont autorisées par défaut et peuvent être supprimées. D'autres permissions peuvent être ajoutées manuellement. 

Les options `--cap-add` et `--cap-drop` supportent la valeur ALL, pour autoriser ou supprimer toutes les capacités. Par défaut, les conteneurs Docker s'exécutent avec 14 capacités.

- Noyau < 2.2
	- Processus privilégié
	- Processus non privilégié
- Noyau >= 2.2
	- Processus privilégié
		- `CAP_CHOWN`
		- `CAP_SYS_TIME`
		- `CAP_SYS_BOOT`
		- `CAP_NET_ADMIN`

[Consultez ce document pour la liste complète des capacités Linux](https://man7.org/linux/man-pages/man7/capabilities.7.html).

Comment vérifier les capacités nécessaires pour une commande :
```
getcap /usr/bin/ping
```

Comment obtenir les capacités d'un processus :
```
getpcaps <pid>
```

Comment ajouter des capacités de sécurité :
```
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
spec:
  containers:
  - name: ubuntu-sleeper
    image: ubuntu
    command: ["sleep", "1000"]
    securityContext:
      capabilities:
        add: ["SYS_TIME"]
        drop: ["CHOWN"]
```


## Comment se préparer à l'examen

Le CKS est considéré comme un examen assez difficile. Mais selon mon expérience, je pense que, avec une pratique suffisante et si vous comprenez les concepts couverts par l'examen, il sera assez gérable en deux heures. 

Vous devez absolument comprendre les concepts sous-jacents de Kubernetes. Et puisque le prérequis pour le CKS est de réussir l'examen CKA, vous devriez avoir une solide compréhension de Kubernetes et de son fonctionnement avant de tenter le CKS. 

De plus, pour réussir le CKS, vous devez comprendre les menaces et les implications de sécurité introduites par l'orchestration de conteneurs.

L'introduction de l'examen CKS est une indication que la sécurité des conteneurs ne doit pas être prise à la légère. Des mécanismes de sécurité doivent toujours être en place pour contrer les attaques sur les clusters Kubernetes. 

Le [piratage de cryptomonnaie de Tesla](https://www.wired.com/story/cryptojacking-tesla-amazon-cloud/) qui était dû à un tableau de bord Kubernetes non protégé met en lumière les risques associés à Kubernetes ou à tout autre moteur d'orchestration de conteneurs. [Hackerone a une page de prime pour Kubernetes](https://hackerone.com/kubernetes?type=team) listant les dépôts de code source utilisés dans un cluster Kubernetes standard.

## Pratique, pratique et pratique !

La pratique est la clé pour réussir l'examen. Personnellement, j'ai trouvé que les simulateurs d'examen de KodeKloud et Killer.sh étaient extrêmement utiles pour moi.

Je n'ai pas eu autant de temps pour me préparer à l'examen CKS que pour l'examen CKA, mais je travaillais sur Kubernetes dans mon travail quotidien, donc j'étais devenu très à l'aise avec cela. 

La pratique est la clé du succès. Bonne chance pour l'examen !

*Vous pouvez lire cet article et d'autres sur [faizanbashir.me](https://faizanbashir.me/rough-guide-to-qualifying-the-cks-exam-in-a-hurry)*