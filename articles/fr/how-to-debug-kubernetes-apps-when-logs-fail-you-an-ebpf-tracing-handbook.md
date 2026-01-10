---
title: Comment déboguer les applications Kubernetes quand les logs ne suffisent plus
  – Un manuel de traçage eBPF
author: Opaluwa Emidowojo
date: '2025-12-16T17:03:01.161Z'
originalURL: https://freecodecamp.org/news/how-to-debug-kubernetes-apps-when-logs-fail-you-an-ebpf-tracing-handbook
description: 'Imaginons que votre pod Kubernetes plante à 3h du matin et que les logs
  n''affichent rien d''utile. Le temps d''accéder au nœud en SSH, le conteneur a disparu,
  et vous en êtes réduit à deviner ce qui s''est passé dans ces derniers instants.

  C''est la réalité du débogage des applications modern...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765899860869/3eadf316-8539-4624-afba-1d4190b6c62a.png
tags:
- name: Devops
  slug: devops
- name: eBPF
  slug: ebpf
- name: Kubernetes
  slug: kubernetes
- name: observability
  slug: observability
- name: Open Source
  slug: opensource
- name: OpenTelemetry
  slug: opentelemetry
- name: inspektor gadget
  slug: inspektor-gadget
- name: handbook
  slug: handbook
seo_desc: 'Let’s say your Kubernetes pod crashes at 3am and the logs show nothing
  useful. By the time you SSH into the node, the container is gone, and you''re left
  guessing what happened in those final moments.

  This is the reality of debugging modern applicatio...'
---


Imaginons que votre pod Kubernetes plante à 3h du matin et que les logs n'affichent rien d'utile. Le temps d'accéder au nœud en SSH, le conteneur a disparu, et vous en êtes réduit à deviner ce qui s'est passé dans ces derniers instants.

C'est la réalité du débogage des applications modernes. Le monitoring traditionnel n'a pas été conçu pour des conteneurs qui vivent quelques secondes, des services qui se déplacent d'un nœud à l'autre, ou des chemins réseau qui changent constamment.

L'eBPF change la donne. Il vous permet de voir *à l'intérieur* du noyau (kernel) lui-même, en observant chaque appel système, chaque paquet réseau et chaque exécution de processus – sans modifier une seule ligne de code.

Dans ce tutoriel, vous allez tracer une application Kubernetes réelle à l'aide d'outils basés sur eBPF. Vous apprendrez les fondamentaux qui s'appliquent à l'ensemble de l'écosystème de l'observabilité moderne, avec les gadgets de l'écosystème Inspektor Gadget.

À la fin, vous serez capable de :

* Tracer les requêtes au fur et à mesure qu'elles circulent dans vos pods Kubernetes
    
* Observer le comportement au niveau du noyau et des syscalls
    
* Déboguer des pannes que les logs et les métriques ne parviennent tout simplement pas à expliquer
    

### Prérequis

**Connaissances requises :**

* Concepts de base de Kubernetes : pods, deployments, services, namespaces
    
* Familiarité avec kubectl : `get`, `describe`, `logs`, `exec`
    
* Bases des conteneurs
    
* Concepts de base de Linux : processus, appels système (syscalls)
    

**Configuration technique requise :**

* Un cluster Kubernetes (local ou dans le cloud)
    
* `kubectl` installé et configuré
    
* Permissions d'administrateur de cluster
    
* Noyau Linux 5.10+ (la plupart des services gérés le proposent)
    

### Table des matières

* [Comprendre l'observabilité eBPF](#heading-comprendre-l-observabilite-ebpf)
    
* [Comment fonctionne le traçage eBPF (sans se perdre dans le noyau)](#heading-comment-fonctionne-le-tracage-ebpf-sans-se-perdre-dans-le-noyau)
    
* [Comment configurer votre environnement](#heading-comment-configurer-votre-environnement)
    
* [Comment tracer votre première requête : tutoriel pratique](#heading-comment-tracer-votre-premiere-requete-tutoriel-pratique)
    
* [Comment interpréter les traces](#heading-comment-interpreter-les-traces)
    
* [Scénarios de débogage en conditions réelles](#heading-scenarios-de-debogage-en-conditions-reelles)
    
* [Aperçus avancés sur le traçage](#heading-apercus-avances-sur-le-tracage)
    
* [Bonnes pratiques et considérations pour la production](#heading-bonnes-pratiques-et-considerations-pour-la-production)
    
* [Prochaines étapes et ressources](#heading-prochaines-etapes-et-ressources)
    

## Comprendre l'observabilité eBPF

L'eBPF (extended Berkeley Packet Filter) est une technologie qui vous permet d'exécuter des programmes personnalisés à l'intérieur du noyau Linux sans modifier le code du noyau ni charger de modules noyau.

Le noyau Linux est le centre de contrôle de votre système d'exploitation. Historiquement, si vous vouliez observer une activité de bas niveau (comme les paquets réseau, les appels système ou les opérations sur les fichiers), vous deviez compter sur des modifications du noyau ou des modules noyau. Ces deux approches étaient fragiles, difficiles à maintenir et présentaient de réels risques pour la stabilité et la sécurité.

L'eBPF change notre approche de l'observabilité. Il fournit un environnement sécurisé et isolé (sandbox) où vous pouvez exécuter des programmes d'observabilité directement dans le noyau avec des vérifications de sécurité intégrées qui empêchent les plantages ou les vulnérabilités de sécurité.

### Pourquoi est-ce important pour l'observabilité ?

Dans l'observabilité traditionnelle, vous instrumentez le code de votre application. Vous ajoutez des instructions de log, des bibliothèques de métriques et des SDK de traçage. Cela fonctionne, mais présente des limites importantes :

* **Modifications de code requises** : Vous devez modifier et redéployer les applications.
    
* **Spécifique au langage** : Différents langages nécessitent différentes bibliothèques.
    
* **Zones d'ombre probables** : Vous ne pouvez voir que ce que vous instrumentez explicitement.
    
* **Surcharge (overhead)** : Une instrumentation lourde ralentit les applications.
    
* **Défis des conteneurs** : Le temps d'ajouter l'instrumentation et de redéployer, le problème peut avoir disparu.
    

L'eBPF adopte une approche différente. Au lieu d'instrumenter les applications, vous instrumentez le noyau. Comme chaque application effectue finalement des appels système au noyau pour les E/S réseau, les opérations sur les fichiers et la gestion des processus, vous pouvez tout observer depuis un point de vue unique.

### L'avantage eBPF pour Kubernetes

Kubernetes ajoute une couche de complexité supplémentaire. Votre application peut être répartie sur plusieurs conteneurs, pods et nœuds. Les outils APM (Application Performance Monitoring) traditionnels ont du mal ici car les conteneurs vont et viennent rapidement, la topologie du réseau change constamment, les services meshes ajoutent de la complexité au routage, et vous ne contrôlez souvent pas le code de l'application (pensez aux services tiers ou aux applications legacy que vous ne pouvez pas modifier).

L'eBPF ne se soucie de rien de tout cela. Il voit toute l'activité au niveau du noyau, quel que soit le langage dans lequel votre application est écrite, qu'elle soit conteneurisée ou non, le nombre de fois où le pod a été replanifié, ou si vous avez accès au code source. Cette visibilité universelle est la raison pour laquelle la Cloud Native Computing Foundation (CNCF) et les grands fournisseurs de cloud misent massivement sur l'eBPF pour l'avenir de l'observabilité.

## Comment fonctionne le traçage eBPF (sans se perdre dans le noyau)

Lorsque votre application s'exécute sur Kubernetes, il existe une séparation claire entre l'espace utilisateur (user space) et l'espace noyau (kernel space). Votre code s'exécute dans l'espace utilisateur, où il est isolé, sécurisé et dispose d'un accès limité aux ressources système. Pour faire quoi que ce soit d'utile – passer des appels réseau, lire des fichiers, allouer de la mémoire – votre application doit demander l'aide du noyau. Le noyau traite ces demandes via des appels système, communément appelés syscalls.

L'eBPF nous permet de nous "brancher" (hook) sur ces syscalls sans ralentir le système. C'est comme avoir une caméra de surveillance à chaque porte entre l'espace utilisateur et l'espace noyau, observant qui passe, quand, et ce qu'ils transportent.

### Un exemple simple : le traçage de requêtes HTTP

Votre application initie une requête HTTP GET, qui doit passer par la pile réseau. Pour établir une connexion, votre application effectue d'abord un appel système `socket()` pour créer une socket réseau. Ensuite, elle appelle `connect()` pour établir une connexion avec le serveur distant. Une fois connectée, elle utilise `send()` pour transmettre la requête HTTP. Les paquets réseau sont envoyés sur le fil, et finalement votre application appelle `recv()` pour recevoir la réponse.

Avec des outils eBPF comme Traceloop d'Inspektor Gadget, vous pouvez automatiquement vous brancher sur ces syscalls. Le programme eBPF capture les métadonnées de la requête, y compris les IP source et destination, les ports, les informations de timing et la taille de la charge utile (payload). Vous obtenez une trace complète de la requête sans toucher au code de votre application.

### Le flux d'exécution eBPF

Voici ce qui se passe sous le capot lorsque vous lancez un traçage. Lorsque vous déployez Inspektor Gadget et lancez un gadget, plusieurs choses se produisent en coulisses. Une fois déployé, le programme eBPF entre en action dès qu'un événement tracé survient.

Lorsque votre application effectue un syscall, le hook eBPF se déclenche et collecte rapidement les données pertinentes : horodatages, IDs de processus, IDs de conteneurs, noms de pods, détails de la requête et informations de latence. Ces données sont envoyées à l'espace utilisateur via des maps eBPF, qui sont des structures de données efficaces pour la communication entre le noyau et l'espace utilisateur.

Inspektor Gadget ajoute le contexte Kubernetes aux données brutes du noyau. Au lieu de voir uniquement des IDs de processus, vous pouvez voir les noms des pods, les namespaces, les labels et d'autres métadonnées. Par exemple, vous pouvez dire qu'une requête provient du pod frontend dans le namespace de production et cible le service backend.

Le gadget présente ensuite ces informations dans un format immédiatement utile, que vous utilisiez la CLI ou que vous l'intégriez à d'autres outils d'observabilité.

L'eBPF est rapide car :

* **Compilation JIT** : Les programmes sont transformés en code machine natif pour une performance maximale.
    
* **Piloté par les événements** : S'exécute uniquement lorsque des événements pertinents surviennent, pas de scrutation (polling) continue.
    
* **Résident dans le noyau** : Pas de changement de contexte coûteux entre le noyau et l'espace utilisateur.
    
* **Hautement optimisé** : Ajoute généralement moins de 5 % de surcharge, même sous forte charge.
    

### L'outil : Inspektor Gadget & Traceloop

Pour ce tutoriel, nous utilisons Traceloop, un outil basé sur eBPF qui trace les flux de requêtes à travers les applications en observant les syscalls, les appels réseau et les opérations d'E/S au niveau du noyau.

Pourquoi utilisons-nous Traceloop pour ce tutoriel ?

* Il est rapide à installer et à exécuter (une seule commande).
    
* La sortie correspond directement au comportement de l'application.
    
* Il ajoute automatiquement le contexte Kubernetes (noms de pods, namespaces).
    
* Vous n'avez pas besoin de modifier le code de l'application.
    

Ce que vous apprendrez s'applique au-delà de Traceloop. Tous les outils de traçage eBPF (Pixie, Cilium Hubble, Tetragon) fonctionnent de la même manière sous le capot. Ils s'attachent aux hooks du noyau et collectent des données d'événements. Une fois que vous aurez compris ces concepts, vous pourrez utiliser n'importe quel outil d'observabilité eBPF efficacement.

## Comment configurer votre environnement

Pour préparer votre environnement au traçage pratique, nous allons vérifier que votre cluster répond aux exigences, installer Inspektor Gadget et déployer une application d'exemple à tracer.

### Vérifier que votre cluster répond aux exigences

Avant d'installer quoi que ce soit, confirmez que votre cluster Kubernetes est prêt pour l'eBPF.

#### Vérifiez votre version de Kubernetes :

```bash
kubectl version --short
```

Vous avez besoin de Kubernetes 1.19 ou ultérieur. La plupart des clusters modernes dépassent cette exigence, mais cela vaut la peine de vérifier.

#### Vérifiez la version du noyau sur vos nœuds :

```bash
kubectl get nodes -o wide
```

Ensuite, vérifiez la version du noyau sur l'un de vos nœuds :

```bash
# Si vous utilisez un cluster local comme minikube ou kind
uname -r

# Pour les clusters cloud, vous devrez peut-être vérifier les détails du nœud
kubectl debug node/<node-name> -it --image=ubuntu -- bash -c "uname -r"
```

Vous avez besoin d'un noyau Linux 5.10 ou ultérieur pour le meilleur support eBPF. Le noyau 4.18+ fonctionne mais avec certaines limitations. Si vous utilisez un service Kubernetes géré (GKE, EKS, AKS), vous avez presque certainement un noyau compatible.

#### Confirmez que vous avez les permissions d'administrateur de cluster :

```bash
kubectl auth can-i create deployments --all-namespaces
```

Cela devrait renvoyer "yes". Inspektor Gadget a besoin de permissions élevées pour charger des programmes eBPF dans le noyau.

### Installer Inspektor Gadget

Vous pouvez installer Inspektor Gadget de plusieurs manières. Nous utiliserons la méthode du plugin kubectl car c'est la plus simple pour l'apprentissage.

#### Installez le plugin kubectl gadget :

```bash
# Télécharger et installer kubectl-gadget
kubectl krew install gadget

# Vérifier l'installation
kubectl gadget version
```

Si vous n'avez pas krew (le gestionnaire de plugins kubectl), vous pouvez l'installer d'abord :

```bash
# Installer krew
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)

# Ajouter krew à votre PATH
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
```

#### Déployez Inspektor Gadget sur votre cluster :

```bash
kubectl gadget deploy
```

Cela crée un namespace `gadget` et déploie le démon Inspektor Gadget sous forme de DaemonSet, garantissant que chaque nœud de votre cluster peut exécuter des programmes eBPF.

#### Vérifiez le déploiement :

```bash
kubectl get pods -n gadget
```

Vous devriez voir un pod `gadget-*` par nœud, tous à l'état `Running`. Si un pod est bloqué en `Pending` ou `CrashLoopBackOff`, vérifiez que votre noyau répond aux exigences de version.

#### Déploiement d'une application d'exemple

Pour apprendre le traçage efficacement, nous avons besoin d'une application qui fait quelque chose d'intéressant. Nous allons déployer une application simple en microservices avec plusieurs composants afin que vous puissiez voir les traces circuler entre les frontières des services.

Commencez par créer un namespace pour notre application de démonstration :

```bash
kubectl create namespace demo-app
```

Ensuite, déployez une application web simple avec un backend :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: demo-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: gcr.io/google-samples/microservices-demo/frontend:v0.8.0
        ports:
        - containerPort: 8080
        env:
        - name: PORT
          value: "8080"
        - name: PRODUCT_CATALOG_SERVICE_ADDR
          value: "productcatalog:3550"
---
apiVersion: v1
kind: Service
metadata:
  name: frontend
  namespace: demo-app
spec:
  type: LoadBalancer
  selector:
    app: frontend
  ports:
  - port: 80
    targetPort: 8080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: productcatalog
  namespace: demo-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: productcatalog
  template:
    metadata:
      labels:
        app: productcatalog
    spec:
      containers:
      - name: server
        image: gcr.io/google-samples/microservices-demo/productcatalogservice:v0.8.0
        ports:
        - containerPort: 3550
        env:
        - name: PORT
          value: "3550"
---
apiVersion: v1
kind: Service
metadata:
  name: productcatalog
  namespace: demo-app
spec:
  selector:
    app: productcatalog
  ports:
  - port: 3550
    targetPort: 3550
```

Appliquez la configuration :

```bash
kubectl apply -f demo-app.yaml
```

Et attendez que les pods soient prêts :

```bash
kubectl wait --for=condition=ready pod -l app=frontend -n demo-app --timeout=300s
kubectl wait --for=condition=ready pod -l app=productcatalog -n demo-app --timeout=300s
```

Vérifiez ensuite que tout fonctionne :

```bash
kubectl get pods -n demo-app
```

Vous devriez voir les pods `frontend` et `productcatalog` à l'état `Running`.

Maintenant, vous devrez obtenir l'URL du frontend :

```bash
# Pour les clusters locaux (minikube, kind, Docker Desktop)
kubectl port-forward -n demo-app service/frontend 8080:80

# Accédez ensuite à http://localhost:8080 dans votre navigateur

# Pour les clusters cloud
kubectl get service frontend -n demo-app
# Cherchez l'EXTERNAL-IP
```

Visitez l'application dans votre navigateur pour confirmer qu'elle fonctionne. Vous devriez voir une vitrine e-commerce simple. Cette application effectue des requêtes HTTP du frontend vers le service de catalogue de produits, ce qui est parfait pour le traçage.

## Comment tracer votre première requête : tutoriel pratique

Maintenant que tout est configuré, capturons notre première trace et voyons l'observabilité eBPF en action.

### Générer le trafic à tracer

Tout d'abord, nous avons besoin d'une activité applicative à observer. Nous allons générer quelques requêtes pour notre application de démonstration.

Dans un terminal, lancez le gadget Traceloop :

```bash
kubectl gadget traceloop -n demo-app
```

Cette commande commence à tracer le traitement des requêtes HTTP dans le namespace `demo-app`. Inspektor Gadget surveille le noyau pour capturer les appels de fonction et les événements système qui se produisent lors du traitement de chaque requête.  
  
Dans un autre terminal, générez du trafic :

```bash
# Si vous utilisez le port-forward
curl http://localhost:8080

# Si vous avez une IP externe
curl http://<EXTERNAL-IP>

# Générer plusieurs requêtes
for i in {1..10}; do curl http://localhost:8080; sleep 1; done
```

### Visualiser votre première trace

Revenez au terminal exécutant le gadget traceloop. Vous devriez voir des sorties apparaître au fur et à mesure que les requêtes circulent dans votre application. La sortie ressemblera à ceci :
```
NODE         NAMESPACE   POD              CONTAINER    PID    TYPE       COUNT  
minikube     demo-app    frontend-abc123  frontend     1234   loop       1      
minikube     demo-app    frontend-abc123  frontend     1234   loop       2
```

Chaque ligne montre un flux d'exécution tracé, le compteur augmentant à mesure que le même schéma est observé à nouveau.

Nous pouvons rendre la sortie plus intéressante en filtrant :

```bash
# Arrêtez la trace précédente avec Ctrl+C, puis lancez :
kubectl gadget traceloop -n demo-app --podname frontend
```

Cela restreint notre observation au seul pod frontend, réduisant le bruit et rendant les schémas plus clairs.

#### Comprendre ce que vous voyez :

Chaque colonne affiche des informations différentes sur votre application :

* **NODE** : Le nœud Kubernetes sur lequel l'événement tracé s'est produit. Dans les clusters multi-nœuds, cela vous aide à comprendre la répartition de la charge et à identifier les problèmes spécifiques à un nœud.
    
* **NAMESPACE** : Le namespace Kubernetes. Nous avons filtré sur `demo-app`, vous ne verrez donc que ce namespace. En production, le filtrage par namespace est crucial pour se concentrer sur des applications spécifiques.
    
* **POD** : Le pod spécifique où l'événement s'est produit. Chaque pod reçoit un nom unique (comme `frontend-abc123`), ce qui vous permet de distinguer les réplicas d'une même application.
    
* **CONTAINER** : Quel conteneur au sein du pod. Les pods peuvent avoir plusieurs conteneurs (application principale, sidecars, conteneurs d'initialisation), cela vous aide donc à localiser précisément où l'activité se déroule.
    
* **PID** : L'ID du processus à l'intérieur du conteneur. C'est le processus Linux réel qui a effectué les syscalls observés par eBPF. Plusieurs PIDs peuvent apparaître si votre application utilise plusieurs processus ou threads.
    
* **TYPE** : Le type d'événement tracé. Pour Traceloop, cela identifie les schémas au niveau du noyau détectés pendant le traitement de la requête.
    
* **COUNT** : Combien de fois ce schéma a été observé. Un compteur qui augmente rapidement indique un volume de requêtes élevé.
    

#### Ce que cela vous apprend sur votre application :

Même à partir de cette sortie simple, vous pouvez tirer des enseignements. Si vous voyez des événements apparaître pour le pod `frontend` mais pas pour le pod `productcatalog`, cela pourrait indiquer que les requêtes n'atteignent pas le backend. C'est un problème de configuration potentiel. Si le `COUNT` augmente rapidement pour un pod mais pas pour les autres, vous savez quel réplica reçoit le trafic, ce qui est utile pour déboguer les problèmes d'équilibrage de charge.

La véritable puissance devient évidente lorsque vous corrélez ces observations au niveau du noyau avec ce que vous savez de votre application. Lorsque vous avez effectué 10 requêtes curl, vous devriez voir une activité correspondante dans la sortie de la trace. Cette relation directe entre le comportement de l'application et les observations du noyau est le fondement de l'observabilité eBPF.

## Comment interpréter les traces

Comprendre la sortie brute d'une trace est précieux, mais interpréter ce qu'elle signifie pour la santé et la performance de votre application est là où réside la véritable compétence.

### Anatomie d'une trace : Spans, Timing et Flux de requêtes

Une trace représente le voyage d'une seule requête à travers votre système. Lorsque vous faites un curl sur le frontend, cela génère une trace. Un span représente une opération unique au sein de cette trace, comme "le frontend traite la requête", "le frontend appelle le catalogue de produits", "le catalogue de produits interroge les données" et "le frontend renvoie la réponse". Chaque span possède des informations de timing : quand il a commencé, quand il s'est terminé, et donc combien de temps il a duré.

Dans le traçage distribué traditionnel avec OpenTelemetry ou Jaeger, vous créeriez explicitement ces spans dans le code de votre application. Avec eBPF, l'outil déduit les spans à partir des schémas de syscalls. Lorsqu'eBPF voit votre processus frontend appeler `connect()` vers l'IP du catalogue de produits, suivi de `send()` et `recv()`, il comprend qu'il s'agit d'un span représentant une requête HTTP vers le service backend.

Le flux de requêtes est la séquence de spans montrant comment votre requête s'est déplacée à travers les services. Dans notre application de démonstration :

1. La requête de l'utilisateur arrive au frontend,
    
2. le frontend se connecte au catalogue de produits,
    
3. le catalogue de produits traite la requête,
    
4. le catalogue de produits renvoie les données, le frontend génère la page,
    
5. et enfin, la réponse est envoyée à l'utilisateur.
    

### Comment suivre les requêtes à travers les services

Traçons une requête à travers les frontières des services pour voir ce flux en action.

Tout d'abord, nous allons lancer une trace plus détaillée :

```bash
kubectl gadget trace_tcp -n demo-app
```

Le gadget trace\_tcp montre les connexions réseau, nous donnant une visibilité sur la communication de service à service.

Ensuite, générez une requête :

```bash
curl http://localhost:8080
```

Dans la sortie de la trace, cherchez les schémas de connexion :

Vous devriez voir le pod frontend établir une connexion TCP vers le service de catalogue de produits. La trace affichera les IP et ports source (frontend) et destination (catalogue de produits), ainsi que les informations de timing.

C'est ainsi qu'eBPF vous permet de suivre les requêtes : en observant les syscalls réseau qui implémentent la communication entre services. Vous n'avez pas besoin de service mesh ou de bibliothèques d'instrumentation, le noyau voit toute l'activité réseau et eBPF la capture.

#### Comprendre le flux :

1. Votre commande curl déclenche une connexion TCP vers l'IP du pod frontend sur le port 8080.
    
2. Le frontend traite la requête et ouvre une connexion TCP vers l'IP du catalogue de produits sur le port 3550.
    
3. Les données circulent dans les deux sens (vous verrez des événements send/receive).
    
4. Les connexions se ferment lorsque les requêtes sont terminées.
    

Chaque étape est visible pour eBPF car chaque étape nécessite des syscalls que le noyau gère.

### Comment identifier les goulots d'étranglement et les erreurs

Nous pouvons également utiliser le traçage pour identifier les problèmes de performance.

Commençons par simuler un backend lent :

```bash
# Créer un point de terminaison délibérément lent en modifiant notre déploiement
kubectl scale deployment productcatalog -n demo-app --replicas=0

# Attendre un moment, puis remonter à 1
kubectl scale deployment productcatalog -n demo-app --replicas=1
```

Pendant que le catalogue de produits est indisponible, générez quelques requêtes :

```bash
for i in {1..5}; do curl http://localhost:8080; done
```

Vous devriez voir des tentatives de connexion du frontend vers le catalogue de produits, mais si le service est indisponible, vous verrez des schémas différents, peut-être des timeouts de connexion ou des erreurs "connection refused", selon le timing exact.

À quoi ressemblent les goulots d'étranglement dans les traces :

* **Spans longs** : Un span qui prend nettement plus de temps que les autres indique un goulot d'étranglement. Dans la sortie de traceloop, vous pourriez voir des écarts entre les événements ou remarquer que certaines opérations prennent plus de temps.
    
* **Retries (tentatives de reconnexion)** : Des tentatives de connexion répétées vers la même destination suggèrent un service défaillant ou lent.
    
* **Schémas d'erreur** : Des échecs de connexion, des timeouts ou des séquences de syscalls inhabituelles indiquent des problèmes.
    

La meilleure compétence à acquérir est la reconnaissance de schémas. Un flux de requêtes typique et sain a un rythme, et les événements se produisent dans des séquences prévisibles avec un timing cohérent. Quand quelque chose casse, le rythme change. Les requêtes prennent plus de temps, des erreurs apparaissent, ou des événements attendus ne se produisent pas du tout.

## Scénarios de débogage en conditions réelles

Passons maintenant en revue trois scénarios réalistes où l'eBPF est utile :

### Scénario 1 : Trouver un point de terminaison lent

**Le problème :** Les utilisateurs signalent que la page du catalogue de produits se charge parfois très lentement, mais les métriques montrent une latence moyenne normale.

Utilisons Traceloop pour enquêter :

```bash
# Lancer le traçage avec les informations de timing
kubectl gadget traceloop -n demo-app --podname frontend
```

Nous allons générer un trafic mixte :

```bash
# Quelques requêtes vers la page d'accueil (rapides)
curl http://localhost:8080

# Quelques requêtes vers le catalogue de produits (potentiellement lentes)
curl http://localhost:8080/products
```

Dans la sortie de la trace, comparez les incréments de `COUNT` pour différents schémas de requêtes. Si certains schémas montrent significativement plus d'itérations de boucle ou des écarts plus longs entre les événements, cela indique que ces requêtes effectuent plus de travail, touchant peut-être un point de terminaison lent.

#### Le diagnostic :

Vous pourriez remarquer que les requêtes vers `/products` obligent le frontend à effectuer plusieurs appels au service de catalogue de produits (visible avec `kubectl gadget trace_tcp`), alors que les requêtes vers la page d'accueil ne le font pas. Cela explique pourquoi la page produit est lente : elle effectue des appels synchrones vers un service backend, et si ce service est lent ou si le réseau est encombré, les utilisateurs ressentent le délai.

#### La solution :

Vous pourriez implémenter du cache, rendre les appels backend asynchrones ou optimiser le service de catalogue de produits lui-même. L'essentiel est que l'eBPF vous a aidé à identifier quel chemin de code spécifique était lent sans ajouter d'instrumentation à votre application.

### Scénario 2 : Traquer les requêtes échouées

**Le problème :** Votre monitoring affiche un taux d'erreur de 5 %, mais les logs de l'application ne montrent aucune erreur. Où se produisent les échecs ?

Utilisons maintenant l'eBPF pour enquêter :

```bash
# Tracer les connexions réseau pour voir les échecs de connexion
kubectl gadget trace_tcp -n demo-app
```

Nous allons simuler des échecs intermittents :

```bash
# Créer un scénario d'échec en rompant temporairement la connectivité du service
kubectl delete service productcatalog -n demo-app

# Générer des requêtes
for i in {1..10}; do curl http://localhost:8080; sleep 1; done

# Restaurer le service
kubectl apply -f demo-app.yaml
```

Dans la trace TCP, vous verrez des tentatives de connexion du frontend vers le catalogue de produits qui échouent ou expirent. La trace affichera la source, la destination et ce qui s'est passé (connexion refusée, timeout, etc.).

#### Le diagnostic :

Les échecs se produisent au niveau du réseau, le frontend ne peut pas atteindre le catalogue de produits. Cela peut être dû à des problèmes de network policy, une mauvaise configuration du service mesh ou des problèmes DNS. Les logs d'application traditionnels pourraient ne pas capturer cela car l'application ne reçoit jamais de réponse à logger, et la connexion échoue avant même que la couche applicative ne soit impliquée.

#### Pourquoi l'eBPF trouve cela quand les logs ne le font pas :

Votre application logue ce qu'elle expérimente. Si une connexion échoue au niveau TCP, votre application peut simplement voir "connexion refusée" et réessayer sans log détaillé.

L'eBPF voit les syscalls réels et les événements réseau, vous donnant une visibilité sur ce qui se passe sous votre couche applicative.

### Scénario 3 : Comprendre les dépendances de service

**Le problème :** Vous n'êtes pas sûr de quels services dépendent les uns des autres, et vous voulez comprendre les dépendances réelles au runtime avant d'effectuer des changements.

Nous allons utiliser l'eBPF pour cartographier les dépendances :

```bash
# Tracer toutes les connexions TCP pour voir qui parle à qui
kubectl gadget trace_tcp -n demo-app
```

Ensuite, générez un trafic normal :

```bash
# Faire diverses requêtes pour exercer différents chemins de code
curl http://localhost:8080
curl http://localhost:8080/products
curl http://localhost:8080/cart
```

La sortie de la trace montre la source et la destination de chaque connexion. Construisez une carte mentale (ou réelle) des pods qui se connectent à quels services.

#### La découverte :

Vous verrez que le pod frontend se connecte au service de catalogue de produits, mais vous pourriez aussi découvrir des dépendances inattendues. Peut-être que le frontend effectue également des appels vers un cache Redis, un service d'authentification ou des API externes. Ces dépendances au runtime pourraient ne pas être documentées ou différer de ce que montrent les diagrammes d'architecture.

#### Pourquoi c'est important :

Avant de déployer une modification sur le service de catalogue de produits, vous savez maintenant exactement quels services seront affectés. Avant d'implémenter une network policy, vous savez quelles connexions autoriser. Avant de décomposer un monolithe, vous comprenez les schémas de communication réels.

C'est la compréhension de l'architecture pilotée par l'observabilité : laisser le système vous montrer comment il fonctionne réellement, et non comment vous pensez qu'il fonctionne.

## Aperçus avancés sur le traçage

Une fois que vous êtes à l'aise avec le traçage de requêtes de base, Inspektor Gadget offre des capacités d'observabilité plus profondes qui révèlent encore plus sur le comportement de votre système.

### Observation au niveau des syscalls

Les gadgets traceloop et trace\_tcp vous donnent des aperçus au niveau applicatif, mais parfois vous devez aller plus loin. Le gadget trace\_exec vous montre chaque exécution de processus dans vos conteneurs.

Tout d'abord, surveillons l'exécution des processus :

```bash
kubectl gadget trace_exec -n demo-app
```

Et générez de l'activité :

```bash
# Entrer dans un pod et exécuter des commandes
kubectl exec -it -n demo-app deployment/frontend -- /bin/sh
ls -la
ps aux
exit
```

Chaque commande que vous exécutez à l'intérieur du conteneur apparaît dans la trace : `/bin/sh`, `ls`, `ps`, et tout le reste. Cela vous aide à comprendre ce qui s'exécute dans vos conteneurs, à détecter une activité suspecte ou à déboguer des problèmes d'initialisation.

Dans des scénarios de production, cela vous aide à répondre à des questions telles que : Mon application lance-t-elle des sous-processus inattendus ? Y a-t-il des problèmes de sécurité comme quelqu'un exécutant `curl` pour télécharger des scripts malveillants ? Mon script `init` exécute-t-il réellement les commandes que je pense ?

### Aperçus sur le traçage réseau

Au-delà des connexions TCP, vous pouvez tracer les requêtes DNS, qui révèlent souvent des choses surprenantes sur le comportement de votre application.

Lancez `trace_dns` :

```bash
kubectl gadget trace_dns -n demo-app
```

Générez des requêtes :

```bash
curl http://localhost:8080
```

Vous verrez chaque requête DNS effectuée par votre application : résolution de noms de services, vérification d'API externes, peut-être même des requêtes inattendues indiquant une mauvaise configuration ou des dépendances que vous ignoriez.

Les enseignements courants du traçage DNS incluent la découverte que votre application utilise des dépendances externes non documentées, la détection d'échecs de résolution DNS causant des erreurs intermittentes, ou l'identification de requêtes DNS excessives qui pourraient être mises en cache.

### Combiner les données eBPF avec les logs et les métriques

L'observabilité eBPF donne les meilleurs résultats lorsqu'elle est combinée aux signaux d'observabilité traditionnels. Pour les combiner efficacement :

* Utilisez les métriques pour le monitoring de santé de haut niveau, l'alerte sur les anomalies, le suivi des tendances dans le temps et la visualisation sur tableaux de bord.
    
* Utilisez les logs pour le contexte spécifique à l'application, les détails de la logique métier, les messages d'erreur avec stack traces et le débogage du code applicatif.
    
* Utilisez les traces eBPF pour comprendre les flux de requêtes, identifier où le temps est passé, découvrir les dépendances au runtime et déboguer les problèmes qui n'apparaissent pas dans les logs.
    

#### Un flux de travail pratique :

Vos métriques vous alertent sur une augmentation de la latence. Vous vérifiez les logs mais ne voyez pas d'erreurs, les requêtes réussissent, mais lentement. Vous utilisez le traçage eBPF pour identifier que les requêtes passent du temps supplémentaire en E/S réseau vers un service backend particulier. Maintenant, vous vérifiez les métriques et les logs de ce service, et découvrez qu'il est sous forte charge. La trace eBPF vous a donné l'indice que les logs et les métriques seuls ne pouvaient pas fournir.

Cette approche de l'observabilité, consistant à utiliser le bon outil pour chaque question, est la manière dont les ingénieurs expérimentés déboguent efficacement les systèmes complexes.

### **Ce que l'eBPF peut et ne peut pas voir**

L'eBPF excelle pour :

* Le trafic réseau (requêtes, réponses, latence)
    
* Les appels système (E/S de fichiers, création de processus, allocation de mémoire)
    
* Les fonctions du noyau (ordonnancement, verrouillage, utilisation des ressources)
    
* Les appels de fonction dans les binaires (avec les uprobes)
    

Mais gardez à l'esprit que l'eBPF a des limites :

* Il ne peut pas déchiffrer les charges utiles chiffrées (à moins de se brancher sur les bibliothèques SSL avant le chiffrement).
    
* Il ne comprend pas automatiquement la logique métier de l'application.
    
* Il capture des événements de bas niveau mais peut avoir besoin de contexte pour la sémantique de haut niveau.
    

C'est pourquoi l'eBPF complète l'observabilité traditionnelle plutôt que de la remplacer entièrement. Il vous donne une visibilité au niveau de l'infrastructure sans modification de code et avec une couverture universelle. L'APM traditionnel fournit le contexte applicatif, les métriques métier et l'instrumentation personnalisée. Ensemble, ils vous offrent une observabilité complète sur toute votre pile.

## Bonnes pratiques et considérations pour la production

Avant d'utiliser le traçage eBPF en production, il y a des considérations importantes concernant la performance, la sécurité et les pratiques opérationnelles.

### Impact sur la performance

La réputation de l'eBPF pour sa faible surcharge est bien méritée, mais "faible" ne signifie pas "nulle".

La plupart des outils de traçage eBPF ajoutent une surcharge CPU de 2 à 5 % et une surcharge mémoire négligeable. Le chiffre exact dépend de la fréquence des événements : tracer un service qui traite 10 000 requêtes par seconde aura plus de surcharge qu'un service en traitant 10 par seconde.

Mesurer l'impact :

```bash
# Avant d'activer le traçage, vérifiez l'utilisation des ressources de base
kubectl top pods -n demo-app

# Activer le traçage
kubectl gadget traceloop -n demo-app

# Vérifier à nouveau l'utilisation des ressources
kubectl top pods -n demo-app
```

Vous devriez voir une légère augmentation de l'utilisation du CPU dans les pods où le traçage est actif. C'est le coût des programmes eBPF s'exécutant dans le noyau et traitant les événements.

#### Bonnes pratiques en production :

Utilisez un traçage ciblé plutôt que de tout tracer partout. Tracez des namespaces, des pods ou des conteneurs individuels spécifiques lors de l'investigation de problèmes. Pour les services à haut volume, réduisez la surcharge en appliquant des filtres, de l'agrégation ou de l'échantillonnage lorsque l'outil de traçage le permet.

Arrêtez le traçage une fois l'investigation terminée. Contrairement à la collecte de métriques, qui s'exécute généralement en continu, le traçage basé sur eBPF est mieux utilisé comme un outil de diagnostic à la demande pour capturer des aperçus détaillés pendant un débogage actif.

#### Quand la surcharge compte :

Si vous exécutez des applications sensibles à la latence (comme des systèmes de trading haute fréquence ou des communications en temps réel), même une surcharge de 2 à 5 % peut être inacceptable. Dans ces cas, utilisez le traçage eBPF dans des environnements de pré-production pour identifier les problèmes, ou activez-le temporairement en production uniquement lors d'un débogage actif.

### Considérations de sécurité

L'eBPF est puissant, ce qui signifie qu'il nécessite des privilèges élevés. Comprendre les implications de sécurité est crucial.

#### Ce à quoi l'eBPF peut accéder :

Les programmes eBPF peuvent observer tous les syscalls, le trafic réseau et l'exécution des processus dans le noyau. Cela inclut des données potentiellement sensibles comme les détails de connexion, les chemins de fichiers et les arguments de processus. Bien que les programmes eBPF s'exécutent dans une sandbox et ne puissent pas modifier les données ni faire planter le noyau, ils peuvent lire des informations qui pourraient être sensibles.

#### Exigences de privilèges :

Le chargement de programmes eBPF nécessite les capacités `CAP_SYS_ADMIN` ou `CAP_BPF` (sur les noyaux récents). C'est une opération privilégiée, seuls les utilisateurs de confiance devraient avoir cet accès. Le DaemonSet Inspektor Gadget s'exécute avec ces privilèges, protégez donc l'accès en conséquence.

#### Bonnes pratiques :

Implémentez le RBAC (Role-Based Access Control) pour restreindre qui peut exécuter des gadgets. Tous les développeurs n'ont pas besoin de la capacité de tracer les systèmes de production.

Soyez également attentif aux données que vous collectez : si vos traces peuvent contenir des informations sensibles (comme des jetons d'authentification dans les en-têtes HTTP), restreignez l'accès aux données de trace.

Enfin, envisagez d'utiliser des contrôleurs d'admission pour empêcher le chargement de programmes eBPF non autorisés. Auditez l'utilisation de l'eBPF dans les environnements de production pour savoir qui a exécuté quels gadgets et quand.

#### Network policies :

Le DaemonSet d'Inspektor Gadget doit communiquer avec le serveur d'API et entre ses composants. Assurez-vous que vos network policies autorisent cette communication tout en maintenant une segmentation appropriée.

### Quand utiliser le traçage eBPF vs l'APM traditionnel

Le traçage eBPF et les outils APM traditionnels comme New Relic, Datadog ou Dynatrace servent des objectifs différents. Comprendre quand utiliser chacun vous aide à construire une stratégie d'observabilité efficace.

Utilisez le traçage eBPF quand :

* Vous ne pouvez pas modifier le code de l'application (applications tierces, systèmes legacy, binaires compilés).
    
* Vous avez besoin d'une visibilité au niveau de l'infrastructure (réseau, syscalls, comportement du noyau).
    
* Vous déboguez des problèmes qui traversent les frontières des services mais n'apparaissent pas dans les logs applicatifs.
    
* Vous voulez une surcharge d'instrumentation nulle en fonctionnement normal (lancez le traçage uniquement en cas de besoin).
    
* Vous avez besoin de comprendre ce qui se passe réellement par rapport à ce que l'application rapporte.
    

Utilisez l'APM traditionnel quand :

* Vous avez besoin de métriques avec un contexte métier (IDs utilisateurs, types de transactions, données spécifiques au métier).
    
* Vous voulez une instrumentation automatique avec une configuration minimale pour les frameworks supportés.
    
* Vous avez besoin d'un stockage et d'une analyse à long terme de toutes les traces (le traçage eBPF est souvent utilisé pour l'investigation en temps réel).
    
* Vous voulez des tableaux de bord et des alertes pré-construits pour les schémas applicatifs courants.
    
* Vous avez besoin d'une visibilité au niveau du code applicatif (stack traces, valeurs de variables, appels de fonctions).
    

### L'approche idéale : utiliser les deux

De nombreuses équipes utilisent l'APM traditionnel pour le monitoring continu et le traçage eBPF pour l'investigation ciblée lorsque les données de l'APM ne suffisent pas. Par exemple, votre APM montre qu'un service est lent mais n'explique pas pourquoi. Vous activez le traçage eBPF sur ce service pour comprendre ce qui se passe au niveau du noyau : délais réseau, syscalls excessifs, dépendances inattendues, et trouver la cause racine.

Cette approche complémentaire vous donne à la fois la visibilité continue de l'APM et la puissance de diagnostic profonde de l'eBPF sans la surcharge liée à l'exécution des deux au maximum de leur capacité en permanence.

## Prochaines étapes et ressources

Si vous êtes arrivé jusqu'ici, merci de m'avoir lu ! Maintenant que vous avez appris les fondamentaux de l'observabilité eBPF et pratiqué le traçage avec Inspektor Gadget, vous pouvez poursuivre votre voyage en :

### Explorant d'autres outils eBPF

Maintenant que vous comprenez les concepts eBPF via traceloop, explorer d'autres outils sera beaucoup plus facile.

#### Essayez d'autres gadgets Inspektor Gadget :

```bash
# Voir tous les gadgets disponibles
kubectl gadget --help

# Quelques-uns utiles à explorer :
kubectl gadget trace_open -n demo-app     # Traçage des E/S de fichiers
kubectl gadget trace_bind -n demo-app     # Événements de liaison de ports
kubectl gadget profile cpu -n demo-app    # Profilage CPU
kubectl gadget snapshot process -n demo-app  # Liste des processus
```

Chaque gadget vous apprend quelque chose de différent sur le comportement du système et vous donne un autre outil de diagnostic dans votre boîte à outils.

### Expérimentez avec d'autres plateformes eBPF :

Si vous êtes intéressé par des plateformes d'observabilité plus larges, essayez Pixie pour son auto-instrumentation et son interface riche. Installez Cilium avec Hubble si vous vous concentrez sur l'observabilité réseau et voulez comprendre le comportement du service mesh. Explorez Tetragon si l'observabilité de la sécurité vous intéresse, pour voir quels processus s'exécutent et à quels fichiers ils accèdent.

Les concepts sont directement transposables : tous ces outils attachent des programmes eBPF aux hooks du noyau, collectent des données d'événements et les présentent de différentes manières. Votre compréhension des syscalls, des traces et de l'observation au niveau du noyau s'applique universellement.

### Connectez-vous à l'écosystème d'observabilité de la CNCF

Les outils d'observabilité eBPF n'existent pas de manière isolée. Ils font partie de l'écosystème plus large de la Cloud Native Computing Foundation.

#### Intégration OpenTelemetry :

De nombreux outils eBPF peuvent exporter des données au format OpenTelemetry, vous permettant de combiner les traces au niveau du noyau avec les traces au niveau applicatif dans un backend d'observabilité unifié. Cela vous donne une image complète : l'eBPF montre le comportement de l'infrastructure tandis qu'OpenTelemetry montre le contexte applicatif.

#### Prometheus et Grafana :

Les métriques dérivées de l'eBPF peuvent être exposées comme des métriques Prometheus et visualisées dans Grafana aux côtés de vos métriques applicatives. Cette approche par tableau de bord unifié vous aide à corréler le comportement de l'infrastructure et de l'application.

#### Intégration Service Mesh :

Si vous utilisez Istio, Linkerd ou d'autres services meshes, les outils eBPF comme Cilium Hubble peuvent fournir une visibilité plus profonde sur la communication de service à service que ce que le mesh seul propose. Le mesh gère la gestion du trafic tandis que l'eBPF vous donne la visibilité au niveau du noyau.

#### Jaeger et Zipkin :

Pour les organisations utilisant des backends de traçage distribué, les traces eBPF peuvent être exportées vers ces systèmes, enrichissant vos données de trace avec des spans au niveau de l'infrastructure que l'instrumentation applicative manque.

### Ressources communautaires et parcours d'apprentissage

La communauté eBPF est vibrante et accueillante. Vous pouvez continuer à apprendre grâce aux ressources ci-dessous.

**Documentation officielle et blog :**

* [eBPF.io](http://eBPF.io) : Le hub central pour la documentation eBPF, les tutoriels et la liste des projets.
    
* [Docs Inspektor Gadget](https://inspektor-gadget.io/docs/latest/) : Guides complets pour tous les gadgets et cas d'utilisation.
    
* [Documentation Cilium](https://docs.cilium.io/en/stable/index.html) : Plongées profondes dans le réseau eBPF.
    
* [Blog CNCF — “What is Observability 2.0?](https://www.cncf.io/blog/2025/01/27/what-is-observability-2-0/) : Un aperçu rapide de la façon dont l'observabilité moderne dépasse les outils traditionnels en unifiant métriques, logs et traces pour des aperçus en temps réel dans les systèmes cloud-native.
    

**Ressources d'apprentissage :**

* [Learning eBPF par Liz Rice](https://cilium.isovalent.com/hubfs/Learning-eBPF%20-%20Full%20book.pdf) : Livre complet couvrant les fondamentaux de l'eBPF.
    
* [eBPF Summit](https://ebpf.io/summit-2025/) : Conférence annuelle avec des interventions des créateurs et utilisateurs d'eBPF.
    
* [Webinaires CNCF](https://www.cncf.io/online-programs/cncf-on-demand-webinar-how-to-start-building-a-self-service-infrastructure-platform-on-kubernetes/) : Sessions régulières sur les sujets d'observabilité.
    
* [SIGs d'observabilité Kubernetes](https://www.kubernetes.dev/community/community-groups/) : Discussions et projets communautaires.
    

Pour rendre ce tutoriel facile à suivre et à expérimenter, j'ai inclus tous les manifestes Kubernetes, les applications de démonstration et les commandes de traçage eBPF dans ce [dépôt](https://github.com/Emidowojo/ebpf-k8s-tracing-tutorial). Vous pouvez également me contacter sur [LinkedIn](https://www.linkedin.com/in/emidowojo/) si vous souhaitez rester en contact.