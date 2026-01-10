---
title: 'Tutoriel Helm Charts : Le gestionnaire de packages Kubernetes expliqué'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-31T19:28:44.000Z'
originalURL: https://freecodecamp.org/news/helm-charts-tutorial-the-kubernetes-package-manager-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/helm-blog-logo.jpg
tags:
- name: Docker
  slug: docker
- name: Helm
  slug: helm
- name: Kubernetes
  slug: kubernetes
seo_title: 'Tutoriel Helm Charts : Le gestionnaire de packages Kubernetes expliqué'
seo_desc: "By Sebastian Sigl\nThere are different ways of running production services\
  \ at a high scale. One popular solution for running containers in production is\
  \ Kubernetes. But interacting with Kubernetes directly comes with some caveats.\
  \ \nHelm tries to solve..."
---

Par Sebastian Sigl

Il existe différentes façons d'exécuter des services de production à grande échelle. Une solution populaire pour exécuter des conteneurs en production est Kubernetes. Mais interagir directement avec Kubernetes présente certains inconvénients. 

Helm tente de résoudre certains de ces défis avec des fonctionnalités utiles qui augmentent la productivité et réduisent les efforts de maintenance des déploiements complexes. 

Dans cet article, vous apprendrez :

* Ce qu'est Helm
* Les cas d'utilisation les plus courants de Helm
* Comment configurer et déployer un package Helm disponible publiquement
* Comment déployer une application personnalisée en utilisant Helm

Chaque exemple de code dans cet article nécessite un cluster Kubernetes. La manière la plus simple d'obtenir un cluster pour tester est d'installer Docker et d'activer sa fonctionnalité de cluster Kubernetes. De plus, vous devez installer [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) et [Helm](https://helm.sh/docs/intro/install/) pour interagir avec votre cluster.

_Veuillez noter : Lorsque vous essayez les exemples, soyez patient. Si vous allez trop vite, les conteneurs ne seront pas prêts. Cela peut prendre quelques minutes jusqu'à ce que les conteneurs puissent recevoir des requêtes._

## Qu'est-ce que Helm ?

Helm se décrit comme « Le gestionnaire de packages Kubernetes ». C'est un outil en ligne de commande qui vous permet de créer et d'utiliser des Helm Charts.

Un Helm Chart est une collection de modèles et de paramètres qui décrivent un ensemble de ressources Kubernetes. Sa puissance s'étend de la gestion d'une seule définition de nœud à un cluster multi-nœuds hautement scalable.

L'architecture de Helm a changé au fil des années. La version actuelle de Helm communique directement avec votre cluster Kubernetes via REST. Si vous lisez quelque chose sur Tiller dans le contexte de Helm, alors vous lisez un ancien article. Tiller a été supprimé dans Helm 3. 

Helm lui-même est stateful. Lorsqu'un Helm Chart est installé, les ressources définies sont déployées et des méta-informations sont stockées dans les secrets Kubernetes.

## Comment déployer une application Helm simple

Mettons les mains dans le cambouis et assurons-nous que Helm est prêt à être utilisé. 

Tout d'abord, nous devons être connectés à un cluster Kubernetes. Dans cet exemple, je vais me concentrer sur un cluster Kubernetes qui vient avec votre configuration Docker. Donc, si vous utilisez un autre cluster Kubernetes, les configurations et les sorties peuvent différer.

```shell
$ kubectl config use-context docker-desktop

  Basculé vers le contexte "docker-desktop".

$ kubectl get node
   
   NOM             STATUT   RÔLES    ÂGE   VERSION
   docker-desktop   Prêt    master   20j   v1.19.3
```

Déployons un serveur web Apache en utilisant Helm. En premier lieu, nous devons indiquer à Helm où chercher en ajoutant un dépôt Helm :

```shell
$ helm repo add bitnami https://charts.bitnami.com/bitnami
```

Installons le conteneur réel :

```shell
$ helm install my-apache bitnami/apache --version 8.0.2
```

Après quelques minutes, votre déploiement est prêt. Nous pouvons vérifier l'état des conteneurs en utilisant kubectl :

```shell
$ kubectl get pods

  NOM                               PRÊT   STATUT    REDÉMARRAGES   ÂGE
  my-apahe-apache-589b8df6bd-q6m2n   1/1     En cours   0          2m27s
```

Maintenant, ouvrez [http://localhost](http://localhost) pour voir le site web par défaut d'Apache exposé localement. De plus, Helm peut nous montrer des informations sur les déploiements actuels :

```shell
$ helm list

 NOM     	RÉVISION	STATUT  	CHART       	VERSION
 my-apache	1		déployé  	apache-8.0.2	2.4.46
```

### Comment mettre à jour une application Helm

Nous pouvons mettre à jour notre application déployée vers une nouvelle version comme ceci :

```shell
$ helm upgrade my-apache bitnami/apache --version 8.0.3

$ helm list

NOM     	RÉVISION	STATUT  	CHART      	VERSION
my-apache	2       	déployé	apache-8.0.3	2.4.46
```

La colonne Révision indique que c'est la 2ème version que nous avons déployée. 

### Comment revenir en arrière sur une application Helm

Essayons donc de revenir à la première version déployée :

```shell
$ helm rollback my-apache 1                    

Le retour en arrière a réussi ! Bon Helming !

$ helm list
               
NOM     	RÉVISION	STATUT  	CHART		VERSION
my-apache	3       	déployé	apache-8.0.2	2.4.46 
```

C'est une fonctionnalité très puissante qui vous permet de revenir rapidement en arrière sur les changements en production.

J'ai mentionné que Helm stocke les informations de déploiement dans des secrets – les voici :

```shell
$ kubectl get secret

NOM		  		  TYPE        	   	  	DONNÉES   ÂGE
default-token-nc4hn               kubernetes.io/sat		3      20j
sh.helm.release.v1.my-apache.v1   helm.sh/release.v1		1      1m
sh.helm.release.v1.my-apache.v2   helm.sh/release.v1		1      1m
sh.helm.release.v1.my-apache.v3   helm.sh/release.v1		1      1m
```

### Comment supprimer une application Helm déployée

Nettoyons notre Kubernetes en supprimant la version my-apache :

```shell
$ helm delete my-apache
   
  version "my-apache" désinstallée
```

Helm vous donne un moyen très pratique de gérer un ensemble d'applications qui vous permet de déployer, mettre à jour, revenir en arrière et supprimer.

Maintenant, nous sommes prêts à utiliser des fonctionnalités Helm plus avancées qui augmenteront votre productivité !

## Comment accéder aux Helm Charts prêts pour la production

Vous pouvez rechercher des hubs publics pour des Charts qui vous permettent de déployer rapidement votre application souhaitée avec une configuration personnalisable. 

Un Helm Chart ne contient pas seulement un ensemble statique de définitions. Helm offre des capacités pour s'accrocher à n'importe quel état du cycle de vie d'un déploiement Kubernetes. Cela signifie que pendant l'installation ou la mise à jour d'une application, diverses actions peuvent être exécutées comme la création d'une mise à jour de base de données avant de mettre à jour la base de données réelle.

Cette définition puissante des Helm Charts vous permet de partager et d'améliorer une description exécutable d'une configuration de déploiement qui couvre l'installation initiale, les mises à jour de version et les capacités de retour en arrière. 

Helm peut être lourd pour un simple conteneur comme un serveur web à nœud unique, mais il est très utile pour des applications plus complexes. Par exemple, il fonctionne très bien pour un système distribué comme Kafka ou Cassandra qui s'exécute généralement sur plusieurs nœuds distribués dans différents centres de données. 

Nous avons déjà utilisé Helm pour déployer un seul conteneur Apache. Maintenant, nous allons déployer une application WordPress prête pour la production qui contient :

* Des conteneurs qui servent WordPress,
* Des instances de MariaDB pour la persistance et
* Des conteneurs sidecar Prometheus pour chaque conteneur WordPress pour exposer les métriques de santé.

Avant de déployer, il est recommandé d'augmenter vos limites Docker à au moins 4 Go de mémoire.

Configurer tout cela semble être un travail qui prendrait des semaines. Pour le rendre résilient et scalable, probablement un travail qui prendrait des mois. Dans ces domaines, les Helm Charts peuvent vraiment briller. Grâce à la communauté grandissante, il existe peut-être déjà un Helm Chart que nous pouvons utiliser.

### Comment déployer WordPress et MariaDB

Il existe différents hubs publics pour les Helm Charts. L'un d'eux est [artifacthub.io](https://artifacthub.io). Nous pouvons rechercher « WordPress » et trouver un [Chart WordPress](https://artifacthub.io/packages/helm/bitnami/wordpress) intéressant. 

Sur le côté droit, il y a un bouton d'installation. Si vous cliquez dessus, vous obtenez des instructions claires sur ce qu'il faut faire :

```shell
$ helm repo add bitnami https://charts.bitnami.com/bitnami

$ helm install my-wordpress bitnami/wordpress --version 10.1.4
```

Vous verrez également des instructions qui vous indiquent comment accéder à l'interface d'administration et au mot de passe administrateur après l'installation.

Voici comment vous pouvez obtenir et décoder le mot de passe pour l'utilisateur **admin** sur Mac OS :

```shell
$ echo Nom d'utilisateur : user
$ echo Mot de passe : $(kubectl get secret --namespace default my-wordpress-3 -o jsonpath="{.data.wordpress-password}" | base64 --decode)

Nom d'utilisateur : user
Mot de passe : sZCa14VNXe
```

Sur Windows, vous pouvez obtenir le mot de passe pour l'utilisateur **user** dans PowerShell :

```powershell
$pw=kubectl get secret --namespace default my-wordpress -o jsonpath="{.data.wordpress-password}"
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($pw))
```

Notre développement local sera disponible à l'adresse : [http://localhost](http://localhost).  
Notre interface d'administration sera disponible à l'adresse : [https://localhost/admin](https://localhost/admin ).

Nous avons donc tout pour l'exécuter localement. Mais en production, nous voulons mettre à l'échelle certaines parties pour servir de plus en plus de visiteurs. Nous pouvons mettre à l'échelle le nombre de services WordPress. Nous voulons également exposer certaines métriques de santé comme l'utilisation de notre CPU et de notre mémoire.

Nous pouvons [télécharger la configuration d'exemple pour la production](https://raw.githubusercontent.com/bitnami/charts/master/bitnami/wordpress/values-production.yaml) à partir du mainteneur du Chart WordPress. Les changements les plus importants sont :

```yaml
### Démarrer 3 instances WordPress qui recevront toutes 
### les requêtes de nos visiteurs. Un équilibreur de charge distribuera les appels 
### à tous les conteneurs de manière égale.
replicaCount: 3

### démarrer un conteneur sidecar qui exposera les métriques pour votre conteneur wordpress
metrics:
  enabled: true
  image:
    registry: docker.io
    repository: bitnami/apache-exporter
    tag: 0.8.0-debian-10-r243
```

Arrêtons l'application par défaut :

```shell
$ helm delete my-wordpress
  
  version "my-wordpress" désinstallée
```

### Comment démarrer un déploiement multi-instances de WordPress et MariaDB

Déployons une nouvelle version en utilisant les valeurs de production :

```shell
$ helm install my-wordpress-prod bitnami/wordpress --version 10.1.4 -f values-production.yaml
```

Cette fois, nous avons plus de conteneurs en cours d'exécution :

```shell
$ kubectl get pods
NOM                                 PRÊT   STATUT    REDÉMARRAGES   ÂGE
my-wordpress-prod-5c9776c976-4bs6f   2/2     En cours   0          103s
my-wordpress-prod-5c9776c976-9ssmr   2/2     En cours   0          103s
my-wordpress-prod-5c9776c976-sfq84   2/2     En cours   0          103s
my-wordpress-prod-mariadb-0          1/1     En cours   0          103s

```

Nous voyons 4 lignes : 1 ligne pour MariaDB, et 3 lignes pour nos pods WordPress réels. 

Un pod dans Kubernetes est un groupe de conteneurs. Chaque groupe contient 2 conteneurs, un pour WordPress et un pour un exporteur pour Prometheus qui expose des métriques précieuses dans un format spécial.

Comme dans la configuration par défaut, nous pouvons [ouvrir localhost](http://localhost) et jouer avec notre application WordPress. 

### Comment accéder aux métriques de santé exposées

Nous pouvons vérifier les métriques de santé exposées en faisant un proxy vers l'un des pods en cours d'exécution :

```shell
kubectl port-forward my-wordpress-prod-5c9776c976-sfq84 9117:9117
```

_Assurez-vous de remplacer l'ID du pod par votre propre ID de pod lorsque vous exécutez la commande port-forward._ 

Maintenant, nous sommes connectés au port 9117 de l'exporteur Prometheus WordPress et mappons le port à notre port local 9117. Ouvrez [http://localhost:9117](http://localhost:9117/metrics) pour vérifier la sortie. 

Si vous n'êtes pas habitué au format Prometheus, cela peut être un peu déroutant au début. Mais c'est en fait assez facile à lire. Chaque ligne sans _'#'_ contient une clé de métrique et une valeur derrière elle :

```prometheus
apache_cpuload 1.2766
process_resident_memory_bytes 1.6441344e+07
```

Si vous n'êtes pas habitué à de telles métriques, ne vous inquiétez pas – vous vous y habituerez rapidement. Vous pouvez rechercher chaque clé sur Google et découvrir ce qu'elle signifie. Après un certain temps, vous identifierez quelles métriques sont les plus précieuses pour vous et comment elles se comportent dès que vos conteneurs reçoivent de plus en plus de trafic de production.

Nettoyons notre configuration en exécutant :

```shell
$ helm delete my-wordpress-prod

  version "my-wordpress-prod" désinstallée
```

Nous avons abordé de nombreux domaines de déploiement et fonctionnalités. Nous avons déployé plusieurs instances WordPress et l'avons mis à l'échelle avec plus de conteneurs pour la production. Vous pourriez même aller plus loin et activer la mise à l'échelle automatique. Consultez la documentation du Helm Chart et jouez avec !

### Chart Helm pour MariaDB

La persistance du Chart Helm pour WordPress dépend de MariaDB. Il s'appuie sur un autre [Chart Helm pour MariaDB](https://artifacthub.io/packages/helm/bitnami/mariadb) que vous pouvez configurer et mettre à l'échelle selon vos besoins, par exemple en démarrant plusieurs réplicas.

Les possibilités que vous avez lors de l'exécution de conteneurs en production en utilisant Kubernetes sont énormes. La définition du Chart WordPress est disponible publiquement. 

Dans la section suivante, nous allons créer notre propre Chart Helm avec une application de base pour comprendre les principes fondamentaux de la création d'un Chart Helm et pour rendre un déploiement de conteneur statique plus dynamique.

## Comment créer un modèle pour des applications personnalisées

Helm ajoute beaucoup plus de flexibilité à vos fichiers de déploiement Kubernetes. Les fichiers de déploiement Kubernetes sont statiques par nature. Cela signifie que les ajustements comme

* le nombre de conteneurs souhaité,
* les variables d'environnement ou
* la limite de CPU et de mémoire

ne sont pas ajustables en utilisant des fichiers de déploiement Kubernetes simples. Soit vous résolvez cela en dupliquant des fichiers de configuration, soit vous placez des espaces réservés dans vos fichiers de déploiement Kubernetes qui sont remplacés au moment du déploiement. 

Ces deux solutions nécessitent un travail supplémentaire et ne seront pas bien adaptées si vous déployez beaucoup d'applications avec différentes variations.

Mais bien sûr, il existe une solution plus intelligente basée sur Helm qui contient de nombreuses fonctionnalités pratiques de la communauté Helm. Créons un Chart personnalisé pour un moteur de blogging, cette fois pour un blog basé sur NodeJS appelé [ghost blog](https://ghost.org/). 

### Comment démarrer un blog Ghost en utilisant Docker

Une instance simple peut être démarrée en utilisant Docker pur :

```shell
docker run --rm -p 2368:2368 --name my-ghost ghost
```

Notre blog est disponible à l'adresse : [http://localhost:2368](http://localhost:2368/).

Arrêtons l'instance pour pouvoir en lancer une autre en utilisant Kubernetes :

```shell
$ docker rm -f my-ghost

  my-ghost
```

Maintenant, nous voulons déployer le blog ghost avec 2 instances dans notre cluster Kubernetes. Commençons par configurer un déploiement simple :

```yaml
# fichier 'application/deployment.yaml'

apiVersion: apps/v1
kind: Deployment
metadata:
  name: ghost-app
spec:
  selector:
    matchLabels:
      app: ghost-app
  replicas: 2
  template:
    metadata:
      labels:
        app: ghost-app
    spec:
      containers:
        - name: ghost-app
          image: ghost

          ports:
            - containerPort: 2368
```

et plaçons un équilibreur de charge devant pour pouvoir accéder à notre conteneur et distribuer le trafic aux deux conteneurs :

```yaml
# fichier 'application/service.yaml'

apiVersion: v1
kind: Service
metadata:
  name: my-service-for-ghost-app
spec:
  type: LoadBalancer
  selector:
    app: ghost-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 2368
```

Nous pouvons maintenant déployer les deux ressources en utilisant kubectl :

```
$ kubectl apply -f ./appplication/deployment.yaml -f ./appplication/service.yaml

  deployment.apps/ghost-app created
  service/my-service-for-ghost-app created
```

L'application ghost est maintenant disponible via [http://localhost](http://localhost). Arrêtons à nouveau l'application :

```
$ kubectl delete -f ./appplication/deployment.yaml -f ./appplication/service.yaml

  deployment.apps/ghost-app delete
  service/my-service-for-ghost-app delete
```

Jusqu'à présent, tout va bien, cela fonctionne avec Kubernetes simple. Mais que se passe-t-il si nous avons besoin de différents paramètres pour différents environnements ?

Imaginez que nous voulons le déployer dans plusieurs centres de données à différentes étapes (non-prod, prod). Vous finirez par dupliquer vos fichiers Kubernetes encore et encore. Ce sera un enfer pour la maintenance. Au lieu de scripter beaucoup, nous pouvons utiliser Helm. 

Créons un nouveau Chart Helm à partir de zéro :

```shell
$ helm create my-ghost-app

  Creating my-ghost-app
```

Helm a créé un ensemble de fichiers pour vous qui sont généralement importants pour un service prêt pour la production dans Kubernetes. Pour nous concentrer sur les parties les plus importantes, nous pouvons supprimer beaucoup des fichiers créés. Passons en revue les fichiers requis pour cet exemple.

Nous avons besoin d'un fichier de projet appelé Chart.yaml :

```yaml
# Chart.yaml

apiVersion: v2
name: my-ghost-app
description: Un chart Helm pour Kubernetes
type: application
version: 0.1.0
appVersion: 1.16.0
```

Le fichier de modèle de déploiement :

```yaml
# templates/deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: ghost-app
spec:
  selector:
    matchLabels:
      app: ghost-app
  replicas: {{ .Values.replicaCount }}
  template:
    metadata:
      labels:
        app: ghost-app
    spec:
      containers:
        - name: ghost-app
          image: ghost
          ports:
            - containerPort: 2368
          env:
            - name: url
              {{- if .Values.prodUrlSchema }}
              value: http://{{ .Values.baseUrl }}
              {{- else }}
              value: http://{{ .Values.datacenter }}.non-prod.{{ .Values.baseUrl }}
              {{- end }}
```

Cela ressemble beaucoup à notre fichier Kubernetes simple. Ici, vous pouvez voir différents espaces réservés pour le nombre de réplicas, et une condition if-else pour la variable d'environnement appelée url. Dans les fichiers suivants, nous verrons toutes les valeurs définies.

Le fichier de modèle de service :

```yaml
# templates/service.yaml

apiVersion: v1
kind: Service
metadata:
  name: my-service-for-my-webapp
spec:
  type: LoadBalancer
  selector:
    app: ghost-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 2368
```

Notre configuration de service est complètement statique.

Les valeurs pour les modèles sont les dernières parties manquantes de notre Chart Helm. Plus important encore, il est nécessaire d'avoir un fichier de valeurs par défaut appelé values.yaml :

```yaml
# values.yaml

replicaCount: 1
prodUrlSchema: false
datacenter: us-east
baseUrl: myapp.org
```

Un Chart Helm doit pouvoir s'exécuter simplement en utilisant les valeurs par défaut. Avant de continuer, assurez-vous d'avoir supprimé :

* my-ghost-app/templates/tests/test-connection.yaml
* my-ghost-app/templates/serviceaccount.yaml
* my-ghost-app/templates/ingress.yaml
* my-ghost-app/templates/hpa.yaml
* my-ghost-app/templates/NOTES.txt.

Nous pouvons obtenir la sortie finale qui serait envoyée à Kubernetes en exécutant un « dry-run » :

```shell
$ helm template --debug my-ghost-app

install.go:159: [debug] Original chart version: ""
install.go:176: [debug] CHART PATH: /helm/my-ghost-app

---
# Source: my-ghost-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service-for-my-webapp
spec:
  type: LoadBalancer
  selector:
    app: my-example-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 2368
---
# Source: my-ghost-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ghost-app
spec:
  selector:
    matchLabels:
      app: ghost-app
  replicas: 1
  template:
    metadata:
      labels:
        app: ghost-app
    spec:
      containers:
        - name: ghost-app
          image: ghost
          ports:
            - containerPort: 2368
          env:
            - name: url
              value: us-east.non-prod.myapp.org

```

Helm a inséré toutes les valeurs et a également défini l'url sur _`us-east.non-prod.myapp.org`_ car dans le _`values.yaml`_, `prodUrlSchema` est défini sur false et le datacenter est défini sur us-east.

Pour obtenir plus de flexibilité, nous pouvons définir certains fichiers de valeurs de substitution. Définissons-en un pour chaque datacenter :

```yaml
# values.us-east.yaml
datacenter: us-east
```

```yaml
# values.us-west.yaml
datacenter: us-west
```

et un pour chaque étape :

```yaml
# values.nonprod.yaml
replicaCount: 1
prodUrlSchema: false
```

```yaml
# values.prod.yaml
replicaCount: 3
prodUrlSchema: true
```

Nous pouvons maintenant utiliser Helm pour les combiner comme nous le souhaitons et vérifier à nouveau le résultat :

```shell
$ helm template --debug my-ghost-app -f my-ghost-app/values.nonprod.yaml  -f my-ghost-app/values.us-east.yaml 

install.go:159: [debug] Original chart version: ""
install.go:176: [debug] CHART PATH: /helm/my-ghost-app

---
# Source: my-ghost-app/templates/service.yaml
# templates/service.yaml

apiVersion: v1
kind: Service
metadata:
  name: my-service-for-my-webapp
spec:
  type: LoadBalancer
  selector:
    app: my-example-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 2368
---
# Source: my-ghost-app/templates/deployment.yaml
# templates/deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: ghost-app
spec:
  selector:
    matchLabels:
      app: ghost-app
  replicas: 1
  template:
    metadata:
      labels:
        app: ghost-app
    spec:
      containers:
        - name: ghost-app
          image: ghost
          ports:
            - containerPort: 2368
          env:
            - name: url
              value: http://us-east.non-prod.myapp.org

```

Et bien sûr, nous pouvons faire un déploiement final :

```shell
$ helm install -f my-ghost-app/values.prod.yaml my-ghost-prod ./my-ghost-app/

NOM: my-ghost-prod
DERNIÈRE DÉPLOYÉE: Mon Dec 21 00:09:17 2020
ESPACE DE NOMS: default
STATUT: déployé
RÉVISION: 1
SUITE DE TESTS: None
```

Comme avant, notre blog ghost est disponible via [http://localhost](http://localhost).

Nous pouvons supprimer ce déploiement et déployer l'application avec les paramètres us-east et non prod comme ceci :

```shell
$ helm delete my-ghost-prod                                                 
  version "my-ghost-prod" désinstallée

$ helm install -f my-ghost-app/values.nonprod.yaml -f my-ghost-app/values.us-east.yaml my-ghost-nonprod ./my-ghost-app
```

Nous nettoyons enfin notre déploiement Kubernetes via Helm :

```shell
$ helm delete my-ghost-nonprod
```

Nous pouvons donc combiner plusieurs fichiers de valeurs de substitution comme nous le souhaitons. Nous pouvons automatiser les déploiements de manière flexible dont nous avons besoin pour de nombreux cas d'utilisation de pipelines de déploiement. 

Surtout pour les entreprises, cela signifie définir des squelettes de Chart une fois pour s'assurer que les critères requis sont remplis. Plus tard, vous pouvez les copier et les ajuster aux besoins de votre application.

## Conclusion

La puissance d'un excellent moteur de modélisation et la possibilité d'exécuter des versions, des mises à jour et des retours en arrière rendent Helm formidable. En plus de cela, il y a le Hub de Charts Helm disponible publiquement qui contient des milliers de modèles prêts pour la production. Cela fait de Helm un outil indispensable dans votre boîte à outils si vous travaillez avec Kubernetes à plus grande échelle !

J'espère que vous avez apprécié ce tutoriel pratique. Motivez-vous à chercher sur Google, à consulter d'autres exemples, à déployer des conteneurs, à les connecter et à les utiliser.

Vous apprendrez de nombreuses fonctionnalités intéressantes à l'avenir qui vous permettront de livrer votre application en production de manière sans effort, réutilisable et scalable.

Comme toujours, j'apprécie tout commentaire et feedback. J'espère que vous avez apprécié l'article. Si vous l'aimez et ressentez le besoin d'une salve d'applaudissements, [suivez-moi sur Twitter](https://twitter.com/sesigl). Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. Au fait, [nous recrutons](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen) !

Références :

* [https://helm.sh/docs/chart_template_guide/getting_started/](https://helm.sh/docs/chart_template_guide/getting_started/)