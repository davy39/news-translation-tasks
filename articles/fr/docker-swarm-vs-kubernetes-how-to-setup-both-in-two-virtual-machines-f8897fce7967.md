---
title: 'Docker Swarm vs Kubernetes : comment installer les deux sur deux machines
  virtuelles'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-25T18:32:32.000Z'
originalURL: https://freecodecamp.org/news/docker-swarm-vs-kubernetes-how-to-setup-both-in-two-virtual-machines-f8897fce7967
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JCzYiffzwccc3lXj_9V3YA.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Docker Swarm vs Kubernetes : comment installer les deux sur deux machines
  virtuelles'
seo_desc: 'By Zhuowei Zhang

  I installed Docker Swarm and Kubernetes on two virtual machines. I found that Docker
  Swarm is very easy to install and configure, while Kubernetes is slightly harder
  to setup but still simple to use.

  Introduction

  I’ve wanted to try c...'
---

Par Zhuowei Zhang

J'ai installé Docker Swarm et Kubernetes sur deux machines virtuelles. J'ai constaté que Docker Swarm est très facile à installer et à configurer, tandis que Kubernetes est légèrement plus difficile à installer mais reste simple à utiliser.

## Introduction

Je voulais essayer les conteneurs depuis des années : la configuration manuelle des serveurs prend du temps, n'est pas reproductible et est susceptible d'introduire des différences entre mon environnement de test local et la production. Les conteneurs offrent une solution à tous ces problèmes et rendent beaucoup plus facile l'exécution de plusieurs instances d'une application. Cela peut rendre un service plus scalable.

Pour exécuter un service scalable, vous avez besoin d'un moteur d'orchestration de conteneurs pour distribuer la charge en exécutant des conteneurs sur plusieurs ordinateurs et en envoyant des requêtes à chaque instance de l'application. Selon [New Relic](https://blog.newrelic.com/engineering/container-orchestration-explained/), deux moteurs d'orchestration populaires sont [Docker Swarm](https://docs.docker.com/engine/swarm/) et [Kubernetes](https://kubernetes.io/). J'ai décidé d'essayer les deux en déployant la même application avec chaque moteur.

## Création du conteneur

J'ai décidé d'utiliser [Samba](https://en.wikipedia.org/wiki/Samba_(software)) pour l'application de test. Samba est un serveur de fichiers populaire qui permet aux ordinateurs Linux de partager des fichiers avec les ordinateurs Windows. Il communique en utilisant TCP sur le port 445.

C'est la première fois que je travaille avec Docker, donc j'ai modifié un [conteneur Samba prêt à l'emploi](https://github.com/crops/samba) pour [inclure le fichier](https://github.com/zhuowei/ComparisonDockerSwarmKubernetes/blob/master/sambaonly/Dockerfile) que je voulais servir.

En suivant [le tutoriel de Docker](https://docs.docker.com/get-started/part2/), j'ai lancé manuellement le conteneur depuis la ligne de commande pour m'assurer qu'il fonctionne :

```
docker build -t sambaonly-v1 .
docker run --init -p 445:445 -i sambaonly-v1
```

et effectivement, j'ai pu me connecter au serveur Samba dans le conteneur avec `[smbclient](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html)` :

```
zhuowei@dora:~$ smbclient \\\\localhost\\workdir -U %
WARNING: The "syslog" option is deprecated
Try "help" to get a list of possible commands.
smb: \> ls
.                               D        0  Fri Oct  5 12:14:43 2018
..                              D        0  Sun Oct  7 22:09:49 2018
hello.txt                       N       13  Fri Oct  5 11:17:34 2018
102685624 blocks of size 1024. 72252576 blocks available
smb: \>
```

Maintenant que je sais que le conteneur fonctionne, je peux l'utiliser dans un moteur d'orchestration de conteneurs.

## Préparation des machines virtuelles

J'ai créé deux machines virtuelles exécutant Ubuntu 18.04 dans VirtualBox.

J'ai ajouté une carte réseau supplémentaire à chaque machine virtuelle, configurée pour le réseau interne afin qu'elles puissent communiquer entre elles :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_chCjRdcU_mV9ioAyQ7oB5A.png)

Ensuite, j'ai [ajouté un serveur DHCP](https://www.virtualbox.org/manual/ch08.html#vboxmanage-dhcpserver) pour attribuer des adresses IP à chaque machine virtuelle :

```
VBoxManage dhcpserver add --netname intnet --ip 10.133.7.99 --netmask 255.255.255.0 --lowerip 10.133.7.100 --upperip 10.133.7.200 --enable
```

Maintenant, les machines virtuelles peuvent communiquer entre elles. Cela donne à ma machine virtuelle principale l'adresse IP 10.133.7.100.

## Docker Swarm

Docker Swarm est un moteur d'orchestration de conteneurs intégré à Docker lui-même. Lorsque je l'ai découvert, j'étais sceptique : pourquoi l'utiliser au lieu du beaucoup plus célèbre Kubernetes ? La réponse : Docker Swarm est axé sur la simplicité plutôt que sur la configuration. Cela ressemblait à l'iOS des moteurs d'orchestration de conteneurs par rapport à l'Android de Kubernetes.

### Installation de Docker Swarm

Docker Swarm est agréablement facile à installer : tout ce que j'ai à installer est Docker et docker-compose. Ensuite, en suivant [le tutoriel officiel](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/), j'ai exécuté la seule commande nécessaire pour démarrer le nœud manager, en passant l'adresse IP de la machine virtuelle actuelle :

```
zhuowei@dora:~$ docker swarm init --advertise-addr 10.133.7.100 
Swarm initialized: current node (abcdefghijklmnopqrstuvwxy) is now a manager.
To add a worker to this swarm, run the following command:
docker swarm join --token SWMTKN-1-abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx-abcdefghijklmnopqrstuvwxy 10.133.7.100:2377
To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

C'est tout : le moteur Docker fonctionne maintenant en mode Swarm.

Ensuite, j'ai déployé un registre Docker privé afin que les autres nœuds puissent tirer des images, en suivant à nouveau [les instructions de configuration](https://docs.docker.com/engine/swarm/stack-deploy/#set-up-a-docker-registry) :

```
docker service create --name registry --publish published=5000,target=5000 registry:2
```

## Déploiement de l'application

Docker Swarm utilise le format [Docker Compose](https://docs.docker.com/compose/overview/) pour spécifier les conteneurs à exécuter et les ports qu'ils exportent.

En suivant le [tutoriel Docker Compose](https://docs.docker.com/compose/gettingstarted/#step-3-define-services-in-a-compose-file), j'ai créé ce manifeste Docker Compose :

```
version: '3.7'
services:
  samba:
    image: 127.0.0.1:5000/samba
    build: sambaonly
    init: true
    stdin_open: true
    ports:
      - "445:445"
```

Cela indique à Docker Compose de construire le Dockerfile à partir du répertoire "sambaonly", de télécharger/tirer les conteneurs construits vers mon registre privé nouvellement configuré, et d'exporter le port 445 depuis le conteneur.

Pour déployer ce manifeste, [j'ai suivi le tutoriel de Docker Swarm](https://docs.docker.com/engine/swarm/stack-deploy/#set-up-a-docker-registry). J'ai d'abord utilisé Docker Compose pour construire et télécharger le conteneur vers le registre privé :

```
docker-compose build

docker-compose push
```

Après la construction du conteneur, l'application peut être déployée avec la commande `docker stack deploy`, en spécifiant le nom du service :

```bash
$ docker stack deploy --compose-file docker-compose.yml samba-swarm
Ignoring unsupported options: build
Creating network samba-swarm_default
Creating service samba-swarm_samba
zhuowei@dora:~/Documents/docker$ docker stack services samba-swarm
ID           NAME                  MODE       REPLICAS IMAGE PORTS
yg8x8yfytq5d samba-swarm_samba     replicated 1/1
```

Et maintenant l'application fonctionne sous Samba Swarm. J'ai testé qu'elle fonctionnait toujours avec `smbclient` :

```
zhuowei@dora:~$ smbclient \\\\localhost\\workdir -U %
WARNING: The "syslog" option is deprecated
Try "help" to get a list of possible commands.
smb: \> ls
.                               D        0  Fri Oct  5 12:14:43 2018
..                              D        0  Sun Oct  7 22:09:49 2018
hello.txt                       N       13  Fri Oct  5 11:17:34 2018

102685624 blocks of size 1024. 72252576 blocks available
smb: \>
```

#### Ajout d'un autre nœud

Une fois de plus, la simplicité de Docker Swarm brille ici. Pour configurer un deuxième nœud, j'ai d'abord installé Docker, puis j'ai exécuté la commande que Docker m'a donnée lorsque j'ai configuré le swarm :

```
ralph:~# docker swarm join --token SWMTKN-1-abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx-abcdefghijklmnopqrstuvwxy 10.133.7.100:2377

This node joined a swarm as a worker.
```

Pour exécuter mon application sur les deux nœuds, j'ai exécuté la commande `scale` de Docker Swarm sur le nœud manager :

```
zhuowei@dora:~/Documents/docker$ docker service scale samba-swarm_samba=2
samba-swarm_samba scaled to 2 overall progress: 2 out of 2 tasks
1/2: running [==================================================>]
2/2: running [==================================================>] verify: Service converged
```

Sur le nouveau nœud worker, le nouveau conteneur est apparu :

```
ralph:~# docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
7539549283bd 127.0.0.1:5000/samba:latest "/usr/sbin/smbd -FS " 20 seconds ago Up 18 seconds 445/tcp samba-swarm_samba.1.abcdefghijklmnopqrstuvwxy
```

#### Test de l'équilibrage de charge

Docker Swarm inclut un équilibreur de charge intégré appelé le Mesh Router : les requêtes faites à l'adresse IP de n'importe quel nœud sont automatiquement distribuées dans le Swarm.

Pour tester cela, j'ai établi 1000 connexions à l'adresse IP du nœud manager avec `nc` :

```
print("#!/bin/bash")
for i in range(1000):
    print("nc -v 10.133.7.100 445 &")
print("wait")
```

Samba génère un nouveau processus pour chaque connexion, donc si l'équilibrage de charge fonctionne, je m'attendrais à environ 500 processus Samba sur chaque nœud dans le Swarm. C'est effectivement ce qui se passe.

Après avoir exécuté le script pour établir 1000 connexions, j'ai vérifié le nombre de processus Samba sur le manager (10.133.7.100) :

```
zhuowei@dora:~$ ps -ef|grep smbd|wc
506 5567 42504
```

et sur le nœud worker (10.133.7.50) :

```
ralph:~# ps -ef|grep smbd|wc
506 3545 28862
```

Ainsi, exactement la moitié des requêtes faites au nœud manager ont été magiquement redirigées vers le premier nœud worker, montrant que le cluster Swarm fonctionne correctement.

J'ai trouvé Docker Swarm très facile à configurer, et il a bien performé sous (une légère) charge.

## Kubernetes

Kubernetes devient la norme industrielle pour l'orchestration de conteneurs. Il est significativement plus flexible que Docker Swarm, mais cela le rend également plus difficile à configurer. J'ai trouvé que ce n'était pas _trop_ difficile, cependant.

Pour cette expérience, au lieu d'utiliser un environnement de développement Kubernetes pré-construit tel que `[minikube](https://kubernetes.io/docs/setup/minikube/)`, j'ai décidé de configurer mon propre cluster, en utilisant Kubeadm, WeaveNet et MetalLB.

### Installation de Kubernetes

Kubernetes a une [réputation](https://carlosrdrz.es/kubernetes-for-small-projects/) d'être difficile à configurer : vous avez peut-être entendu parler du processus compliqué en plusieurs étapes du [tutoriel Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way).

Cette réputation n'est plus exacte : les développeurs de Kubernetes ont automatisé presque toutes les étapes dans un script de configuration très facile à utiliser appelé `kubeadm`.

Malheureusement, parce que Kubernetes est si flexible, il reste encore quelques étapes que le [tutoriel sur l'utilisation](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/) de `[kubeadm](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/)` ne couvre pas, donc j'ai dû déterminer quel réseau et quel équilibreur de charge utiliser moi-même.

Voici ce que j'ai fini par exécuter.

D'abord, j'ai dû désactiver le Swap sur chaque nœud :

```
root@dora:~# swapoff -a
root@dora:~# systemctl restart kubelet.service
```

Ensuite, j'ai configuré le nœud master (10.133.7.100) avec la commande suivante :

```
sudo kubeadm init --pod-network-cidr=10.134.0.0/16 --apiserver-advertise-address=10.133.7.100 --apiserver-cert-extra-sans=10.0.2.15
```

L'option `--pod-network-cidr` attribue une adresse réseau interne à tous les nœuds du réseau, utilisée pour les communications internes dans Kubernetes.

Les options `--apiserver-advertise-address` et `--apiserver-cert-extra-sans` ont été ajoutées en raison d'une particularité de ma configuration VirtualBox : la carte réseau virtuelle principale sur les VM (qui a l'IP 10.0.2.15) ne peut accéder qu'à Internet. J'ai dû clarifier que les autres nœuds doivent accéder au master en utilisant l'adresse IP 10.133.7.100.

Après avoir exécuté cette commande, Kubeadm a imprimé quelques instructions :

```
Your Kubernetes master has initialized successfully!
To start using your cluster, you need to run the following as a regular user:

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
https://kubernetes.io/docs/concepts/cluster-administration/addons/
You can now join any number of machines by running the following on each node as root:

kubeadm join 10.133.7.100:6443 --token abcdefghijklmnopqrstuvw --discovery-token-ca-cert-hash sha256:abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl
```

J'ai manqué ces instructions la première fois, donc je n'ai pas vraiment terminé la configuration. J'ai ensuite passé une semaine entière à me demander pourquoi aucun de mes conteneurs ne fonctionnait !

Les développeurs de Kubernetes doivent être comme :

<div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="https://giphy.com/embed/3o6Ztq45dSCKelyyis" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>

Après avoir enfin lu les instructions, j'ai dû faire trois choses de plus :

* D'abord, j'ai dû exécuter les commandes données par `kubeadm` pour configurer un fichier de configuration.
* Par défaut, Kubernetes ne planifiera pas de conteneurs sur le nœud master, seulement sur les nœuds workers. Comme je n'ai qu'un seul nœud pour l'instant, [le tutoriel](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#master-isolation) m'a montré cette commande pour permettre l'exécution de conteneurs sur le seul nœud :

```
kubectl taint nodes --all node-role.kubernetes.io/master-
```

* Enfin, j'ai dû choisir un réseau pour mon cluster.

### Installation du réseau

Contrairement à Docker Swarm, qui doit utiliser sa propre couche de routage maillé pour le réseau et l'équilibrage de charge, Kubernetes offre plusieurs choix pour le réseau et l'équilibrage de charge.

Le composant réseau permet aux conteneurs de communiquer entre eux en interne. J'ai fait quelques recherches, et [cet article de comparaison](https://www.objectif-libre.com/en/blog/2018/07/05/k8s-network-solutions-comparison/) a suggéré Flannel ou WeaveNet car ils sont faciles à configurer. Ainsi, j'ai décidé d'essayer WeaveNet. J'ai suivi les instructions du [tutoriel kubeadm](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#pod-network) pour appliquer la configuration de WeaveNet :

```
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```

Ensuite, pour permettre aux conteneurs de communiquer avec le monde extérieur, j'ai besoin d'un équilibreur de charge. D'après mes recherches, j'ai eu l'impression que la plupart des implémentations d'équilibreur de charge Kubernetes sont axées sur les services HTTP uniquement, et non sur le TCP brut. Heureusement, j'ai trouvé MetalLB, un projet récent (d'un an) qui comble cette lacune.

Pour installer MetalLB, j'ai suivi son [tutoriel Getting Started](https://metallb.universe.tf/tutorial/layer2/), et j'ai d'abord déployé MetalLB :

```
kubectl apply -f https://raw.githubusercontent.com/google/metallb/v0.7.3/manifests/metallb.yaml
```

Ensuite, j'ai alloué la plage d'IP 10.133.7.200 10.133.7.230 à MetalLB, en créant et en appliquant [ce fichier de configuration](https://github.com/zhuowei/ComparisonDockerSwarmKubernetes/blob/master/metallb-config.yaml) :

```
kubectl apply -f metallb-config.yaml
```

### Déploiement de l'application

Les fichiers de configuration des services Kubernetes sont plus verbeux que ceux de Docker Swarm, en raison de la flexibilité de Kubernetes. En plus de spécifier le conteneur à exécuter, comme Docker Swarm, je dois spécifier comment chaque port doit être traité.

Après avoir [lu le tutoriel de Kubernetes](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/), j'ai élaboré cette configuration Kubernetes, composée d'un Service et d'un Deployment.

```yml
# https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/
kind: Service
apiVersion: v1
metadata:
  name: samba
  labels:
    app: samba
spec:
  ports:
    - port: 445
      protocol: TCP
      targetPort: 445
  selector:
    app: samba
  type: LoadBalancer

---
```

Ce [Service](https://kubernetes.io/docs/concepts/services-networking/#defining-a-service) indique à Kubernetes d'exporter le port TCP 445 de nos conteneurs Samba vers l'équilibreur de charge.

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: samba
  labels:
    app: samba
spec:
  selector:
    matchLabels:
      app: samba
  replicas: 1
  template:
    metadata:
      labels:
        app: samba
    spec:
      containers:
        - image: 127.0.0.1:5000/samba:latest
          name: samba
          ports:
            - containerPort: 445
          stdin: true
```

Cet objet Deployment indique à Kubernetes d'exécuter mon conteneur et d'exporter un port pour que le Service le gère.

Notez le `replicas: 1`   c'est le nombre d'instances du conteneur que je veux exécuter.

Je peux déployer ce service sur Kubernetes en utilisant `kubectl apply` :

```
zhuowei@dora:~/Documents/docker$ kubectl apply -f kubernetes-samba.yaml
service/samba configured
deployment.apps/samba configured
```

et, après avoir redémarré ma machine virtuelle plusieurs fois, le Deployment a finalement commencé à fonctionner :

```
zhuowei@dora:~/Documents/docker$ kubectl get pods
NAME                   READY STATUS  RESTARTS AGE
samba-57945b8895-dfzgl 1/1   Running 0        52m
zhuowei@dora:~/Documents/docker$ kubectl get service samba
NAME  TYPE         CLUSTER-IP     EXTERNAL-IP  PORT(S)       AGE
samba LoadBalancer 10.108.157.165 10.133.7.200 445:30246/TCP 91m
```

Mon service est maintenant disponible à l'External-IP assignée par MetalLB :

```
zhuowei@dora:~$ smbclient \\\\10.133.7.200\\workdir -U %
WARNING: The "syslog" option is deprecated
Try "help" to get a list of possible commands.
smb: \> ls
.                               D        0  Fri Oct  5 12:14:43 2018
..                              D        0  Sun Oct  7 22:09:49 2018
hello.txt                       N       13  Fri Oct  5 11:17:34 2018

102685624 blocks of size 1024. 72252576 blocks available
smb: \>
```

### Ajout d'un autre nœud

L'ajout d'un autre nœud dans un cluster Kubernetes est beaucoup plus facile : je n'ai eu qu'à exécuter la commande donnée par `kubeadm` sur la nouvelle machine :

```
zhuowei@davy:~$ sudo kubeadm join 10.133.7.100:6443 --token abcdefghijklmnopqrstuvw --discovery-token-ca-cert-hash sha256:abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl

(snip...)

This node has joined the cluster:* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the master to see this node join the cluster.
```

### Particularités de ma configuration

J'ai dû apporter deux modifications en raison de ma configuration VirtualBox :

Tout d'abord, puisque ma machine virtuelle a deux cartes réseau, je dois indiquer manuellement à Kubernetes l'adresse IP de ma machine. Selon [cet issue](https://github.com/kubernetes/kubeadm/issues/203), j'ai dû éditer

```
/etc/systemd/system/kubelet.service.d/10-kubeadm.conf
```

et changer une ligne en

```
Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml --node-ip=10.133.7.101"
```

avant de redémarrer Kubernetes :

```
root@davy:~# systemctl daemon-reload
root@davy:~# systemctl restart kubelet.service
```

L'autre ajustement concerne le registre Docker : puisque le nouveau nœud ne peut pas accéder à mon registre privé sur le nœud master, j'ai décidé de faire un terrible hack et de partager le registre de mon nœud master vers la nouvelle machine en utilisant `ssh` :

```
zhuowei@davy:~$ ssh dora.local -L 5000:localhost:5000
```

Cela redirige le port 5000 du nœud master, `dora` (qui exécute mon registre Docker) vers localhost, où Kubernetes peut le trouver sur cette machine.

En production réelle, on hébergerait probablement le registre Docker sur une machine séparée, afin que tous les nœuds puissent y accéder.

### Mise à l'échelle de l'application

Avec la deuxième machine configurée, j'ai modifié mon Deployment original pour ajouter une autre instance de l'application :

```
replicas: 2
```

Après avoir redémarré à la fois le master et le worker plusieurs fois, la nouvelle instance de mon application a finalement quitté le statut `CreatingContainer` et a commencé à s'exécuter :

```
zhuowei@dora:~/Documents/docker$ kubectl get pods
NAME                   READY STATUS  RESTARTS AGE
samba-57945b8895-dfzgl 1/1   Running 0        62m
samba-57945b8895-qhrtl 1/1   Running 0        12m
```

### Test de l'équilibrage de charge

J'ai utilisé la même procédure pour ouvrir 1000 connexions à Samba s'exécutant sur Kubernetes. Le résultat est intéressant.

Master :

```
zhuowei@dora$ ps -ef|grep smbd|wc
492 5411 41315
```

Worker :

```
zhuowei@davy:~$ ps -ef|grep smbd|wc
518 5697 43499
```

Kubernetes/MetalLB a également équilibré la charge entre les deux machines, mais la machine master a reçu légèrement moins de connexions que la machine worker. Je me demande pourquoi.

En tout cas, cela montre que j'ai finalement réussi à configurer Kubernetes après quelques détours. Lorsque j'ai vu les conteneurs fonctionner, je me suis senti comme [ce gars](http://www.girlgeniusonline.com/comic.php?date=20071126).

## Comparaison et conclusion

**Fonctionnalités communes aux deux** : Les deux peuvent gérer des conteneurs et équilibrer intelligemment la charge des requêtes sur la même application TCP sur deux machines virtuelles différentes. Les deux ont une bonne documentation pour la configuration initiale.

**Points forts de Docker Swarm** : configuration simple sans configuration nécessaire, intégration étroite avec Docker.

**Points forts de Kubernetes** : composants flexibles, nombreuses ressources et modules complémentaires disponibles.

Kubernetes vs Docker Swarm est un compromis entre simplicité et flexibilité.

J'ai trouvé plus facile de configurer Docker Swarm, mais je ne peux pas, par exemple, simplement remplacer l'équilibreur de charge par un autre composant   il n'y a aucun moyen de le configurer : je devrais [le désactiver complètement](https://docs.docker.com/engine/swarm/ingress/#using-the-routing-mesh).

Sur Kubernetes, trouver la bonne configuration m'a pris un certain temps grâce à la quantité impressionnante de choix, mais en échange, je peux remplacer des parties de mon cluster selon les besoins, et je peux facilement installer des modules complémentaires, tels qu'un [tableau de bord élégant](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/).

Si vous voulez simplement essayer Kubernetes sans toute cette configuration, je suggère d'utiliser `[minikube](https://kubernetes.io/docs/setup/minikube/)`, qui offre une machine virtuelle de cluster Kubernetes pré-construite, sans configuration nécessaire.

Enfin, je suis impressionné que les deux moteurs supportent les services TCP bruts : d'autres fournisseurs d'infrastructure en tant que service tels que [Heroku](https://www.heroku.com/) ou [Glitch](https://glitch.com/) ne supportent que l'hébergement de sites web HTTP(s). La disponibilité des services TCP signifie que l'on peut déployer ses serveurs de base de données, ses serveurs de cache, et même ses serveurs Minecraft en utilisant les mêmes outils pour déployer des applications web, ce qui rend la gestion de l'orchestration de conteneurs une compétence très utile.

En conclusion, si je devais construire un cluster, j'utiliserais Docker Swarm. Si je devais payer quelqu'un d'autre pour construire un cluster pour moi, je demanderais Kubernetes.

## Ce que j'ai appris

* Comment travailler avec les conteneurs Docker
* Comment configurer un cluster Docker Swarm à deux nœuds
* Comment configurer un cluster Kubernetes à deux nœuds, et quels choix fonctionneraient pour une application basée sur TCP
* Comment déployer une application sur Docker Swarm et Kubernetes
* Comment résoudre n'importe quel problème en redémarrant un ordinateur suffisamment de fois, comme si j'utilisais encore Windows 98
* Kubernetes et Docker Swarm ne sont pas aussi intimidants qu'ils en ont l'air

## Crédits d'images

* [Logo Docker : utilisé avec permission.](https://www.docker.com/legal/brand-guidelines)
* [Logo Kubernetes : utilisé avec permission.](https://github.com/kubernetes/kubernetes/blob/master/logo/usage_guidelines.md)
* [Icône de bureau depuis GitHub Octicons](https://github.com/webdog/octicons-png/blob/master/black/device-desktop.png).