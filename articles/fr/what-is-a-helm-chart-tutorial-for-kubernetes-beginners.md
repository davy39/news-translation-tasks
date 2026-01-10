---
title: Qu'est-ce qu'un Helm Chart ? Un tutoriel pour les débutants Kubernetes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-09T18:44:46.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-helm-chart-tutorial-for-kubernetes-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/604640a8a7946308b768453d.jpg
tags:
- name: charts
  slug: charts
- name: containers
  slug: containers
- name: Helm
  slug: helm
- name: Kubernetes
  slug: kubernetes
seo_title: Qu'est-ce qu'un Helm Chart ? Un tutoriel pour les débutants Kubernetes
seo_desc: 'By Lucas Santos

  Kubernetes is a very helpful tool for cloud-native developers. But it doesn''t cover
  all the bases on its own – there are some things that Kubernetes cannot solve or
  that are outside its scope.

  This is one of the reasons why open sourc...'
---

Par Lucas Santos

[Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan) est un outil très utile pour les développeurs cloud-native. Mais il ne couvre pas tous les aspects par lui-même – il y a certaines choses que Kubernetes ne peut pas résoudre ou qui sont en dehors de son champ d'application.

C'est l'une des raisons pour lesquelles les projets open source sont si géniaux. Ils aident les outils incroyables à devenir encore plus incroyables lorsque nous les combinons avec d'autres outils open source tout aussi géniaux. Et souvent, ces outils ont été développés dans le seul but de combler les lacunes. L'un de ces outils est Helm.

## Qu'est-ce que Helm ?

[Helm](https://helm.sh) est largement connu comme "le gestionnaire de paquets pour [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan)". Bien qu'il se présente ainsi, son champ d'application va bien au-delà de celui d'un simple gestionnaire de paquets. Cependant, commençons par le début.

Helm est un projet open-source qui a été initialement créé par [DeisLabs](https://deislabs.io/) et donné à [CNCF](https://azure.microsoft.com/blog/announcing-cncf/?WT.mc_id=containers-19838-ludossan), qui le maintient maintenant. L'objectif initial de Helm était de fournir aux utilisateurs un meilleur moyen de gérer tous les fichiers YAML [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan) que nous créons dans les projets [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan).

La voie que [Helm](https://docs.microsoft.com/azure/aks/kubernetes-helm?WT.mc_id=containers-19838-ludossan) a prise pour résoudre ce problème a été de créer des **[Charts](https://docs.microsoft.com/azure/aks/kubernetes-helm?WT.mc_id=containers-19838-ludossan)** Helm. Chaque chart est un bundle avec un ou plusieurs manifests [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan) – un chart peut avoir des charts enfants et des charts dépendants également.

Cela signifie que Helm installe tout l'arbre de dépendances d'un projet si vous exécutez la commande d'installation pour le chart de niveau supérieur. Vous n'avez besoin que d'une seule commande pour installer toute votre application, au lieu de lister les fichiers à installer via `kubectl`.

Les [Charts](https://docs.microsoft.com/azure/aks/kubernetes-helm?WT.mc_id=containers-19838-ludossan) vous permettent également de versionner vos fichiers de manifest, tout comme nous le faisons avec Node.js ou tout autre package. Cela vous permet d'installer des versions spécifiques de chart, ce qui signifie conserver des configurations spécifiques pour votre infrastructure sous forme de code.

Helm conserve également un historique des versions de tous les charts déployés, afin que vous puissiez revenir à une version précédente si quelque chose ne va pas.

[Helm](https://docs.microsoft.com/azure/aks/kubernetes-helm?WT.mc_id=containers-19838-ludossan) prend en charge [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan) nativement, ce qui signifie que vous n'avez pas à écrire de fichiers de syntaxe complexe ou autre chose pour commencer à utiliser Helm. Il vous suffit de déposer vos fichiers de template dans un nouveau chart et vous êtes prêt à partir.

Mais pourquoi devrions-nous l'utiliser ? La gestion des manifests d'application peut être facilement effectuée avec quelques combinaisons de commandes.

## Pourquoi devriez-vous utiliser Helm ?

Helm brille vraiment là où Kubernetes ne va pas. Par exemple, le templating. Le champ d'application du projet Kubernetes est de gérer vos conteneurs pour vous, pas vos fichiers de template.

Cela rend excessivement difficile la création de fichiers véritablement génériques à utiliser dans une grande équipe ou une grande organisation avec de nombreux paramètres différents qui doivent être définis pour chaque fichier.

Et aussi, comment versionnez-vous les informations sensibles en utilisant Git lorsque les fichiers de template sont en texte brut ?

La réponse : les templates Go. Helm vous permet d'ajouter des variables et d'utiliser des fonctions à l'intérieur de vos fichiers de template. Cela le rend parfait pour les applications scalables qui devront éventuellement voir leurs paramètres changés. Regardons un exemple.

J'ai un projet open-source appelé [Zaqar](https://github.com/khaosdoctor/zaqar/), un microservice d'email simple pour Node.js qui communique avec SendGrid. Le projet est essentiellement composé d'un service, d'un déploiement et d'un autoscaler.

Prenons le fichier de déploiement comme exemple. J'aurais quelque chose comme ceci :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: zaqar
  namespace: default
  labels:
    app: zaqar
    version: v1.0.0
    env: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: zaqar
      env: production
  template:
    metadata:
      labels:
        app: zaqar
        version: v1.0.0
        env: production
    spec:
      containers:
        - name: zaqar
          image: "khaosdoctor/zaqar:v1.0.0"
          imagePullPolicy: IfNotPresent
          env:
            - name: SENDGRID_APIKEY
              value: "MY_SECRET_KEY"
            - name: DEFAULT_FROM_ADDRESS
              value: "my@email.com"
            - name: DEFAULT_FROM_NAME
              value: "Lucas Santos"
          ports:
            - name: http
              containerPort: 3000
              protocol: TCP
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 250m
              memory: 256Mi
```

Si je voulais utiliser ce template dans un [pipeline CI](https://docs.microsoft.com/learn/modules/aks-deployment-pipeline-github-actions/?WT.mc_id=containers-19838-ludossan), ou le publier sur mon [GitHub](https://github.com/khaosdoctor), je devrais remplacer les parties variables par des espaces réservés. Nous pouvons donc remplacer ces textes par les informations requises.

Dans ce cas, à la fois l'étiquette de version, l'étiquette `env` et les variables d'environnement seraient remplacées par des espaces réservés, comme ceci :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: zaqar
  namespace: default
  labels:
    app: zaqar
    version: #!VERSION!#
    env: #!ENV!#
spec:
  replicas: 1
  selector:
    matchLabels:
      app: zaqar
      env: #!ENV!#
  template:
    metadata:
      labels:
        app: zaqar
        version: #!VERSION!#
        env: #!ENV!#
    spec:
      containers:
        - name: zaqar
          image: "khaosdoctor/zaqar:#!VERSION!#"
          imagePullPolicy: IfNotPresent
          env:
            - name: SENDGRID_APIKEY
              value: "#!SENDGRID_KEY!#"
            - name: DEFAULT_FROM_ADDRESS
              value: "#!FROM_ADDR!#"
            - name: DEFAULT_FROM_NAME
              value: "#!FROM_NAME!#"
          ports:
            - name: http
              containerPort: 3000
              protocol: TCP
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 250m
              memory: 256Mi
```

Nous pouvons maintenant exécuter notre [pipeline CI](https://docs.microsoft.com/learn/modules/aks-deployment-pipeline-github-actions/?WT.mc_id=containers-19838-ludossan). Mais avant de le faire, nous devons remplacer nos espaces réservés par les valeurs réelles.

Pour cela, nous pouvons utiliser `sed` et sa syntaxe "super facile" `sed 's/#!PLACEHOLDER!#/replacement/g'`, et transmettre cela jusqu'à ce que nous finissions tous les espaces réservés. La commande finale serait quelque chose comme ceci :

```bash
cat deploy.yaml | \
    sed 's/#!ENV!#/production/g' | \
    sed 's/#!VERSION!#/v1.0.0/g' | \
    sed 's/#!SENDGRID_KEY!#/MyKey/g' | \
    sed 's/#!FROM_ADDR!#/my@email.com/g' | \
    sed 's/#!FROM_NAME!#/Lucas Santos/g'
```

Par défaut, sed envoie tout vers `stdout`, donc nous pouvons ajouter un autre pipe vers `kubectl -f`, comme `<all the command from before> | kubectl -f -`. Ensuite, nous aurons notre déploiement en place. Le seul problème est que nous devons faire la même chose pour **tous** les autres fichiers.

Maintenant, imaginez un projet plus grand, avec beaucoup d'autres variables et espaces réservés. Vous écriviez probablement un script pour le faire pour vous, n'est-ce pas ? Ce script est Helm.

Lorsque vous créez un Chart (nous en parlerons plus tard), nous avons une arborescence de répertoires spécifique que nous devons suivre pour que Helm comprenne ce que nous voulons faire. À l'intérieur du répertoire `templates`, nous pouvons ajouter nos fichiers de manifest, **avec un templating natif Go**, comme ceci :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Values.name }}
  namespace: {{ default .Release.Namespace .Values.namespace }}
  labels:
    app: {{ .Values.name }}
    version: {{ .Values.image.tag }}
    env: {{ .Values.env }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Values.name }}
      env: {{ .Values.env }}
  template:
    metadata:
      labels:
        app: {{ .Values.name }}
        version: {{ .Values.image.tag }}
        env: {{ .Values.env }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "khaosdoctor/zaqar:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          env:
            - name: SENDGRID_APIKEY
              value: {{ required "You must set a valid Sendgrid API key" .Values.environment.SENDGRID_APIKEY | quote }}
            - name: DEFAULT_FROM_ADDRESS
              value: {{ required "You must set a default from address" .Values.environment.DEFAULT_FROM_ADDRESS | quote }}
            - name: DEFAULT_FROM_NAME
              value: {{ required "You must set a default from name" .Values.environment.DEFAULT_FROM_NAME | quote }}
          ports:
            - name: http
              containerPort: 3000
              protocol: TCP
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
```

Toutes ces valeurs peuvent être obtenues à partir d'un fichier `Values.yaml` (pour les valeurs par défaut), ou vous pouvez les définir dans le CLI en utilisant le flag `--set <path> value`.

Si nous voulons installer notre chart, nous pouvons émettre la commande suivante :

```bash
helm upgrade --install --create-namespace myChart ./path/to/my/chart \
  --set image.tag=v1.0.0 \
  --set env=production \
  --set environment.SENDGRID_APIKEY=myKey \
  --set environment.DEFAULT_FROM_ADDRESS="my@email.com" \
  --set environment.DEFAULT_FROM_NAME="Lucas Santos"
```

Helm nous permet également d'utiliser des fonctions à l'intérieur de nos déploiements. Nous pouvons donc avoir des fonctions `default` pour revenir aux valeurs par défaut si elles ne sont pas remplies, comme le namespace. Ou nous pouvons avoir `required` qui affiche un message et échoue à installer le chart si la valeur n'est pas fournie, ce qui est le cas de nos variables d'environnement.

Il y a beaucoup d'autres fonctions utiles dans leur [docs](https://helm.sh/docs/chart_template_guide/) - allez les voir.

Maintenant, nous sommes capables non seulement de gérer plus efficacement les ressources de notre application, mais aussi de publier ces ressources dans un système de version open-source sans aucun tracas ou problème de sécurité.

## Comment créer un Helm Chart

Il est assez facile de créer un chart dans Helm. Tout d'abord, vous devez avoir [Helm installé](https://helm.sh/docs/intro/quickstart/). Ensuite, tapez simplement `helm create <chart name>` et il créera un répertoire rempli de fichiers et d'autres répertoires. Ces fichiers sont requis pour que Helm crée un chart.

Examinons de plus près à quoi ressemble cette arborescence de fichiers et quels sont les fichiers qu'elle contient :

* **chart.yaml:** C'est ici que vous mettrez les informations relatives à votre chart. Cela inclut la version du chart, le nom et la description afin que vous puissiez le trouver si vous le publiez dans un dépôt ouvert. Dans ce fichier, vous pourrez également définir des [dependencies](https://helm.sh/docs/topics/charts/#chart-dependencies) externes en utilisant la clé `dependencies`.
* **values.yaml**: Comme nous l'avons vu précédemment, ce fichier contient les valeurs par défaut pour les variables.
* **templates (dir):** C'est l'endroit où vous mettrez tous vos fichiers de manifest. Tout ce qui se trouve ici sera transmis et créé dans Kubernetes.
* **charts:** Si votre chart dépend d'un autre chart que vous possédez, ou si vous ne voulez pas dépendre de la bibliothèque par défaut de Helm (le registre par défaut d'où Helm tire les charts), vous pouvez apporter cette même structure à l'intérieur de ce répertoire. Les dépendances de chart sont installées de bas en haut, ce qui signifie que si le chart A dépend du chart B, et B dépend de C, l'ordre d'installation sera C ->B ->A.

Il y a d'autres champs, mais ce sont les plus courants, et ils sont requis. Vous pouvez jeter un coup d'œil rapide au [dépôt de Zaqar](https://github.com/khaosdoctor/zaqar/tree/master/helm) pour voir comment nous pouvons publier des charts open source.

Une note rapide : lors de l'installation de Helm, assurez-vous d'installer la version 3. La version 2 fonctionne toujours, mais elle nécessite un composant côté serveur appelé Tiller, qui lie votre installation de Helm à un seul cluster. Helm 3 a supprimé ce besoin avec l'ajout de plusieurs CRDs, mais il n'est pas supporté dans toutes les versions de Kubernetes.

## Comment héberger un Helm Chart

D'accord, vous avez créé votre chart, maintenant quoi ? Devons-nous télécharger tout le dépôt pour installer ces charts ? Non ! Helm dispose d'une [bibliothèque publique pour les charts les plus utilisés](https://artifacthub.io/), qui fonctionne un peu comme Docker Hub.

Vous pouvez également créer votre propre dépôt de charts et [l'héberger en ligne](https://helm.sh/docs/topics/chart_repository/). Helm s'inspire des mêmes sources que HomeBrew ou Linux. Vous pouvez utiliser ces dépôts pour télécharger les charts qu'ils contiennent.

Puisqu'un dépôt de charts est essentiellement un fichier `index.yaml` servi à partir d'un serveur web statique, vous pouvez pratiquement créer un dépôt de charts n'importe où.

Prenez [Zaqar](https://github.com/khaosdoctor/zaqar/tree/master/helm), par exemple – il est hébergé sur GitHub Pages et est accessible via [mon domaine](https://lsantos.me/zaqar/helm/index.yaml). Lorsque Helm recherche un fichier `index.yaml`, il recherche en fait la liste des versions disponibles de ce chart, leurs digest SHA256 et l'emplacement du fichier `.tgz` empaqueté pour télécharger le chart lui-même. C'est à peu près ce que NPM fait sous le capot (très simplifié).

Cela signifie que vous n'avez pas besoin d'avoir votre dépôt cloné pour toujours, et vos charts peuvent également être privés. Vous devez simplement créer un dépôt de charts.

Vous pouvez même utiliser des [services hébergés comme Azure CR](https://docs.microsoft.com/azure/container-registry/container-registry-helm-repos?WT.mc_id=containers-19838-ludossan) pour faire le travail, ou vous pouvez avoir une solution complète appelée [Chart Museum](https://github.com/helm/chartmuseum), qui vous permet de stocker vos charts et vous fournit une interface utilisateur soignée.

## Conclusion

Helm est là pour rester. Il a aidé et aidera beaucoup de développeurs Kubernetes pendant longtemps.

Si vous voulez savoir comment utiliser Helm, vous pouvez vous référer à leur [docs](https://helm.sh), ou vous pouvez suivre ce [module d'apprentissage gratuit](https://docs.microsoft.com/learn/modules/aks-app-package-management-using-helm/?WT.mc_id=containers-19838-ludossan) sur la façon de déployer vos applications sur Kubernetes facilement avec Helm.