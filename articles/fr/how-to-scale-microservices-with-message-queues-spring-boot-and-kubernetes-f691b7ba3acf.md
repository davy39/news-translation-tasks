---
title: Comment mettre à l'échelle des Microservices avec des Files d'Attente, Spring
  Boot et Kubernetes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-24T16:08:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-scale-microservices-with-message-queues-spring-boot-and-kubernetes-f691b7ba3acf
coverImage: https://cdn-media-1.freecodecamp.org/images/0*EYkQh1w1msyxqcl6.png
tags:
- name: Java
  slug: java
- name: Kubernetes
  slug: kubernetes
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment mettre à l'échelle des Microservices avec des Files d'Attente,
  Spring Boot et Kubernetes
seo_desc: 'By Daniele Polencic

  When you design and build applications at scale, you deal with two significant challenges:
  scalability and robustness.

  You should design your service so that even if it is subject to intermittent heavy
  loads, it continues to opera...'
---

Par Daniele Polencic

Lorsque vous concevez et construisez des applications à grande échelle, vous êtes confronté à deux défis majeurs : **l'évolutivité et la robustesse**.

Vous devez concevoir votre service de manière à ce que, même s'il est soumis à des charges intermittentes élevées, il continue à fonctionner de manière fiable.

Prenons l'exemple de l'Apple Store.

Chaque année, des millions de clients Apple s'inscrivent à l'avance pour acheter un nouvel iPhone.

Cela représente des millions de personnes achetant un article en même temps.

Si vous deviez représenter le trafic de l'Apple Store en requêtes par seconde au fil du temps, voici à quoi pourrait ressembler le graphique :

![Image](https://cdn-media-1.freecodecamp.org/images/3B9TiJGw7xmEUrQEkybIkg3Eax80yp0Hhmr6)

Imaginez maintenant que vous êtes chargé de relever le défi de construire une telle application.

**Vous construisez un magasin où les utilisateurs peuvent acheter leurs articles préférés.**

Vous construisez un microservice pour rendre les pages web et servir les actifs statiques. Vous construisez également une API REST backend pour traiter les requêtes entrantes.

Vous souhaitez que les deux composants soient séparés, car avec la même API REST, vous pourriez servir le site web et les applications mobiles.

![Image](https://cdn-media-1.freecodecamp.org/images/KwKWfcwyHdG6OpaKOHZy15omoa43sKlPZee8)

Aujourd'hui s'avère être le grand jour, et votre magasin est mis en ligne.

Vous décidez de mettre à l'échelle l'application à quatre instances pour le front-end et quatre instances pour le backend, car vous prévoyez que le site web sera plus fréquenté que d'habitude.

![Image](https://cdn-media-1.freecodecamp.org/images/Fi7dlKCFNMzb2mCho3XyXX9wEGREld79EPnd)

Vous commencez à recevoir de plus en plus de trafic.

Les services front-end gèrent bien le trafic. Mais vous remarquez que le backend connecté à la base de données a du mal à suivre le nombre de transactions.

Pas de problème, vous pouvez mettre à l'échelle le nombre de réplicas à 8 pour le backend.

![Image](https://cdn-media-1.freecodecamp.org/images/5Z4K917VtGh9GiAzxRMLhPuHAHEI6g7aXHHH)

Vous recevez encore plus de trafic, et le backend ne peut pas le gérer.

Certains des services commencent à perdre des connexions. Des clients mécontents contactent votre service client. Et maintenant, vous êtes submergé par le trafic.

Votre backend ne peut pas le gérer, et il perd de nombreuses connexions.

![Image](https://cdn-media-1.freecodecamp.org/images/iVvuX8mIs7oL-dpzPdQHrgfyLYjTNJKC3V9j)

Vous venez de perdre une tonne d'argent, et vos clients sont mécontents.

Votre application n'est pas conçue pour être robuste et hautement disponible :

* le front-end et le backend sont étroitement couplés — **en fait, il ne peut pas traiter les applications sans le backend**
* le front-end et le backend doivent être mis à l'échelle de concert — **s'il n'y a pas assez de backends, vous pourriez être submergé par le trafic**
* si le backend est indisponible, vous ne pouvez pas traiter les transactions entrantes.

Et les transactions perdues sont des revenus perdus.

Vous pourriez redessiner votre architecture pour découpler le front-end et le backend avec une file d'attente.

![Image](https://cdn-media-1.freecodecamp.org/images/DbJpi1nlwT6Ijdj9P09oHNoKnHqwwnMi0nom)

Le front-end publie des messages dans la file d'attente, tandis que le backend traite les messages en attente un à la fois.

La nouvelle architecture présente certains avantages évidents :

* si le backend est indisponible, la file d'attente agit comme un tampon
* si le front-end produit plus de messages que ce que le backend peut gérer, ces messages sont tamponnés dans la file d'attente
* vous pouvez mettre à l'échelle le backend indépendamment du front-end — c'est-à-dire que vous pourriez avoir des centaines de services front-end et une seule instance du backend

**Super, mais comment construire une telle application ?**

Comment concevoir un service capable de gérer des centaines de milliers de requêtes ? Et comment déployer une application qui s'adapte dynamiquement ?

Avant de plonger dans les détails du déploiement et de la mise à l'échelle, concentrons-nous sur l'application.

### Coder une application Spring

Le service comporte trois composants : le front-end, le backend et un courtier de messages.

Le front-end est une simple application web Spring Boot avec le moteur de templating Thymeleaf.

Le backend est un worker qui consomme des messages d'une file d'attente.

Et puisque [Spring Boot a une excellente intégration avec JSM](https://spring.io/guides/gs/messaging-jms/), vous pouvez l'utiliser pour envoyer et recevoir des messages asynchrones.

Vous pouvez trouver un projet exemple avec une application front-end et backend connectée à JSM sur [learnk8s/spring-boot-k8s-hpa](https://github.com/learnk8s/spring-boot-k8s-hpa).

> _Veuillez noter que l'application est écrite en Java 10 pour tirer parti de [l'intégration améliorée des conteneurs Docker](https://blog.docker.com/2018/04/improved-docker-container-integration-with-java-10/)._

Il y a une seule base de code, et vous pouvez configurer le projet pour qu'il s'exécute soit comme front-end, soit comme backend.

Vous devez savoir que l'application dispose de :

* une page d'accueil où vous pouvez acheter des articles
* un panneau d'administration où vous pouvez inspecter le nombre de messages dans la file d'attente
* un point de terminaison `/health` pour signaler lorsque l'application est prête à recevoir du trafic
* un point de terminaison `/submit` qui reçoit les soumissions du formulaire et crée des messages dans la file d'attente
* un point de terminaison `/metrics` pour exposer le nombre de messages en attente dans la file d'attente (plus d'informations à ce sujet plus tard)

L'application peut fonctionner en deux modes :

**En tant que frontend**, l'application rend la page web où les gens peuvent acheter des articles.

![Image](https://cdn-media-1.freecodecamp.org/images/UgRDK9Yty7Z6Q9KnGdg4AkxvfO4jouAIU2Au)

**En tant que worker**, l'application attend les messages dans la file d'attente et les traite.

![Image](https://cdn-media-1.freecodecamp.org/images/i5g1ZHHFo0GWcS0QwYykLEaHShB9AObaVrfD)

> _Veuillez noter que dans le projet exemple, le traitement est simulé en attendant cinq secondes avec un `Thread.sleep(5000)`._

Vous pouvez configurer l'application dans l'un ou l'autre mode en modifiant les valeurs dans votre `application.yaml`.

### Exécuter l'application en mode test

Par défaut, l'application démarre en tant que frontend et worker.

Vous pouvez exécuter l'application et, tant que vous avez une instance ActiveMQ en cours d'exécution localement, vous devriez pouvoir acheter des articles et les voir traités par le système.

![Image](https://cdn-media-1.freecodecamp.org/images/eAIyqOY-aH0R85A5zjqcL736s-RlYkBMWR0h)

Si vous inspectez les logs, vous devriez voir le worker traiter les articles.

Cela a fonctionné ! Écrire des applications Spring Boot est facile.

Un sujet plus intéressant est d'apprendre à connecter Spring Boot à un courtier de messages.

### Envoyer et recevoir des messages avec JMS

Spring JMS (Java Message Service) est un mécanisme puissant pour envoyer et recevoir des messages en utilisant des protocoles standard.

Si vous avez utilisé l'API JDBC dans le passé, vous devriez trouver l'API JMS familière, car elle fonctionne de manière similaire.

Le courtier de messages le plus populaire que vous pouvez consommer avec JMS est [ActiveMQ](http://activemq.apache.org/) — un serveur de messagerie open source.

Avec ces deux composants, vous pouvez publier des messages dans une file d'attente (ActiveMQ) en utilisant une interface familière (JMS) et utiliser la même interface pour recevoir des messages.

Et encore mieux, Spring Boot a une excellente intégration avec JMS, donc vous pouvez vous mettre à niveau en un rien de temps.

En fait, la classe courte suivante encapsule la logique utilisée pour interagir avec la file d'attente :

```
@Component
```

```
public class QueueService implements MessageListener {
```

```
private static final Logger LOGGER = LoggerFactory.getLogger(QueueService.class);
```

```
@Autowired  private JmsTemplate jmsTemplate;  public void send(String destination, String message) {    LOGGER.info("sending message='{}' to destination='{}'", message, destination);    jmsTemplate.convertAndSend(destination, message);  }
```

```
@Override  public void onMessage(Message message) {    if (message instanceof ActiveMQTextMessage) {      ActiveMQTextMessage textMessage = (ActiveMQTextMessage) message;      try {        LOGGER.info("Processing task " + textMessage.getText());        Thread.sleep(5000);        LOGGER.info("Completed task " + textMessage.getText());      } catch (InterruptedException e) {        e.printStackTrace();      } catch (JMSException e) {        e.printStackTrace();      }    } else {      LOGGER.error("Message is not a text message " + message.toString());    }  }}
```

Vous pouvez utiliser la méthode `send` pour publier des messages dans une file d'attente nommée.

De plus, Spring Boot exécutera la méthode `onMessage` pour chaque message entrant.

La dernière pièce du puzzle est d'instruire Spring Boot à utiliser la classe.

Vous pouvez traiter les messages en arrière-plan en [enregistrant l'écouteur dans l'application Spring Boot](https://docs.spring.io/spring/docs/current/spring-framework-reference/integration.html#jms-annotated-programmatic-registration) comme suit :

```
@SpringBootApplication@EnableJmspublic class SpringBootApplication implements JmsListenerConfigurer {  @Autowired  private QueueService queueService;
```

```
public static void main(String[] args) {    SpringApplication.run(SpringBootApplication.class, args);  }
```

```
@Override  public void configureJmsListeners(JmsListenerEndpointRegistrar registrar) {    SimpleJmsListenerEndpoint endpoint = new SimpleJmsListenerEndpoint();    endpoint.setId("myId");    endpoint.setDestination("queueName");    endpoint.setMessageListener(queueService);    registrar.registerEndpoint(endpoint);  }}
```

Où **id** est un identifiant unique pour le consommateur et **destination** est le nom de la file d'attente.

Vous pouvez [lire le code source complet pour le service de file d'attente Spring](https://github.com/learnk8s/spring-boot-k8s-hpa/blob/master/src/main/java/com/learnk8s/app/queue/QueueService.java) à partir du projet sur GitHub.

Remarquez comment vous avez pu coder une file d'attente fiable en moins de 40 lignes de code.

**Vous devez aimer Spring Boot.**

### Tout le temps que vous économisez sur le déploiement, vous pouvez le consacrer au codage

Vous avez vérifié que l'application fonctionne, et il est enfin temps de la déployer.

À ce stade, vous pourriez démarrer votre VPS, installer Tomcat, et passer du temps à créer des scripts personnalisés pour tester, construire, packager et déployer l'application.

Ou vous pourriez écrire une description de ce que vous souhaitez avoir : un courtier de messages et deux applications déployées avec un équilibreur de charge.

Des orchestrators tels que Kubernetes peuvent lire votre liste de souhaits et provisionner l'infrastructure appropriée.

Puisque moins de temps passé sur l'infrastructure signifie plus de temps pour le codage, vous allez déployer l'application sur Kubernetes cette fois-ci. Mais avant de commencer, vous avez besoin d'un cluster Kubernetes.

Vous pourriez vous inscrire à Google Cloud Platform ou Azure et utiliser l'offre Kubernetes du fournisseur cloud. Ou vous pourriez essayer Kubernetes localement avant de déplacer votre application dans le cloud.

`minikube` est un cluster Kubernetes local conditionné dans une machine virtuelle. C'est génial si vous êtes sur Windows, Linux et Mac, car il ne prend que cinq minutes pour créer un cluster.

Vous devriez également installer `kubectl`, le client pour vous connecter à votre cluster.

Vous pouvez trouver les instructions sur la façon d'installer `minikube` et `kubectl` à partir de la [documentation officielle](https://kubernetes.io/docs/tasks/tools/).

> _Si vous êtes sous Windows, vous devriez consulter notre [guide détaillé sur la façon d'installer Kubernetes et Docker](https://learnk8s.io/blog/installing-docker-and-kubernetes-on-windows)._

Vous devriez démarrer un cluster avec 8 Go de RAM et une configuration supplémentaire :

```
minikube start \  --memory 8096 \  --extra-config=controller-manager.horizontal-pod-autoscaler-upscale-delay=1m \  --extra-config=controller-manager.horizontal-pod-autoscaler-downscale-delay=2m \  --extra-config=controller-manager.horizontal-pod-autoscaler-sync-period=10s
```

> _Veuillez noter que si vous utilisez une instance `minikube` préexistante, vous pouvez redimensionner la VM en la détruisant et en la recréant. Ajouter simplement `--memory 8096` n'aura aucun effet._

Vérifiez que l'installation a réussi. Vous devriez voir quelques ressources listées sous forme de tableau. Le cluster est prêt, **peut-être devriez-vous commencer le déploiement maintenant ?**

Pas encore.

Vous devez d'abord emballer vos affaires.

### Qu'y a-t-il de mieux qu'un uber-jar ? Les conteneurs

Les applications déployées sur Kubernetes doivent être conditionnées sous forme de conteneurs. Après tout, Kubernetes est un orchestrateur de conteneurs, donc il n'est pas capable d'exécuter votre jar natif.

Les conteneurs sont similaires aux jars gras : ils contiennent toutes les dépendances nécessaires pour exécuter votre application. **Même la JVM fait partie du conteneur.** Ils sont donc techniquement un jar gras encore plus gros.

Une technologie populaire pour conditionner les applications sous forme de conteneurs est Docker.

> _Bien qu'étant la plus populaire, Docker n'est pas la seule technologie capable d'exécuter des conteneurs. D'autres options populaires incluent `rkt` et `lxd`._

Si vous n'avez pas Docker installé, vous pouvez suivre les [instructions sur le site officiel de Docker](https://docs.docker.com/install/).

Habituellement, vous construisez vos conteneurs et les poussez vers un registre. C'est similaire à la publication de jars vers Artifactory ou Nexus. Mais dans ce cas particulier, vous allez travailler localement et sauter la partie registre. En fait, vous allez créer l'image du conteneur directement dans `minikube`.

Tout d'abord, connectez votre client Docker à `minikube` en suivant les instructions imprimées par cette commande :

```
minikube docker-env
```

> _Veuillez noter que si vous changez de terminal, vous devez vous reconnecter au démon Docker à l'intérieur de `minikube`. Vous devez suivre les mêmes instructions chaque fois que vous utilisez un terminal différent._

et à partir de la racine du projet, construisez l'image du conteneur avec :

```
docker build -t spring-k8s-hpa .
```

Vous pouvez vérifier que l'image a été construite et est prête à être exécutée avec :

```
docker images | grep spring
```

Super !

Le cluster est prêt, vous avez conditionné votre application, **peut-être êtes-vous prêt à déployer maintenant ?**

Oui, vous pouvez enfin demander à Kubernetes de déployer les applications.

> **Ne manquez pas la prochaine histoire, expérience ou astuce.** Si vous appréciez cet article, restez à l'écoute pour plus de contenu. Recevez du nouveau contenu directement dans votre boîte de réception et améliorez votre expertise en Kubernetes. [Abonnez-vous maintenant](https://learnk8s.io/newsletter)

### Déployer votre application sur Kubernetes

Votre application comporte trois composants :

* l'application Spring Boot qui rend le frontend
* ActiveMQ en tant que courtier de messages
* le backend Spring Boot qui traite les transactions

Vous devez déployer les trois composants séparément.

Pour chacun d'eux, vous devez créer :

* Un objet **Deployment** qui décrit quel conteneur est déployé et sa configuration
* Un objet **Service** qui agit comme un équilibreur de charge pour toutes les instances de l'application créées par le **Deployment**

Chaque instance de votre application dans un déploiement est appelée un **Pod**.

![Image](https://cdn-media-1.freecodecamp.org/images/UT3oElo8lKNp9JQE6G3FMF5ZH8isRGhxgzC8)

### Déployer ActiveMQ

Commençons par ActiveMQ.

Vous devez créer un fichier `activemq-deployment.yaml` avec le contenu suivant :

```
apiVersion: extensions/v1beta1kind: Deploymentmetadata:  name: queuespec:  replicas: 1  template:    metadata:      labels:        app: queue    spec:      containers:      - name: web        image: webcenter/activemq:5.14.3        imagePullPolicy: IfNotPresent        ports:          - containerPort: 61616        resources:          limits:            memory: 512Mi
```

Le modèle est verbeux mais facile à lire :

* vous avez demandé un conteneur activemq du registre officiel nommé [webcenter/activemq](https://hub.docker.com/r/webcenter/activemq/)
* le conteneur expose le courtier de messages sur le port 61616
* il y a 512 Mo de mémoire alloués pour le conteneur
* vous avez demandé un seul réplica — une seule instance de votre application

Créez un fichier `activemq-service.yaml` avec le contenu suivant :

```
apiVersion: v1kind: Servicemetadata:  name: queuespec:  ports:  - port: 61616     targetPort: 61616  selector:    app: queue
```

Heureusement, ce modèle est encore plus court !

Le yaml se lit comme suit :

* vous avez créé un équilibreur de charge qui expose le port 61616
* le trafic entrant est distribué à tous les Pods (voir déploiement ci-dessus) qui ont une étiquette de type `app: queue`
* le `targetPort` est le port exposé par les Pods

Vous pouvez créer les ressources avec :

```
kubectl create -f activemq-deployment.yamlkubectl create -f activemq-service.yaml
```

Vous pouvez vérifier qu'une instance de la base de données est en cours d'exécution avec :

```
kubectl get pods -l=app=queue
```

### Déployer le front-end

Créez un fichier `fe-deployment.yaml` avec le contenu suivant :

```
apiVersion: extensions/v1beta1kind: Deploymentmetadata:  name: frontendspec:  replicas: 1  template:    metadata:      labels:        app: frontend    spec:      containers:      - name: frontend        image: spring-boot-hpa        imagePullPolicy: IfNotPresent        env:        - name: ACTIVEMQ_BROKER_URL          value: "tcp://queue:61616"        - name: STORE_ENABLED          value: "true"        - name: WORKER_ENABLED          value: "false"        ports:        - containerPort: 8080        livenessProbe:          initialDelaySeconds: 5          periodSeconds: 5          httpGet:            path: /health            port: 8080        resources:          limits:            memory: 512Mi
```

Le **Deployment** ressemble beaucoup au précédent.

Il y a cependant quelques nouveaux champs :

* il y a une section où vous pouvez injecter des variables d'environnement
* il y a la sonde de vivacité qui vous indique quand l'application est prête à accepter le trafic

Créez un fichier `fe-service.yaml` avec le contenu suivant :

```
apiVersion: v1kind: Servicemetadata:  name: frontendspec:  ports:  - nodePort: 32000    port: 80    targetPort: 8080  selector:    app: frontend  type: NodePort
```

Vous pouvez créer les ressources avec :

```
kubectl create -f fe-deployment.yamlkubectl create -f fe-service.yaml
```

Vous pouvez vérifier qu'une instance de l'application front-end est en cours d'exécution avec :

```
kubectl get pods -l=app=frontend
```

### Déployer le backend

Créez un fichier `backend-deployment.yaml` avec le contenu suivant :

```
apiVersion: extensions/v1beta1kind: Deploymentmetadata:  name: backendspec:  replicas: 1  template:    metadata:      labels:        app: backend      annotations:        prometheus.io/scrape: 'true'    spec:      containers:      - name: backend        image: spring-boot-hpa        imagePullPolicy: IfNotPresent        env:        - name: ACTIVEMQ_BROKER_URL          value: "tcp://queue:61616"        - name: STORE_ENABLED          value: "false"        - name: WORKER_ENABLED          value: "true"        ports:        - containerPort: 8080        livenessProbe:          initialDelaySeconds: 5          periodSeconds: 5          httpGet:            path: /health            port: 8080        resources:          limits:            memory: 512Mi
```

Créez un fichier `backend-service.yaml` avec le contenu suivant :

```
apiVersion: v1kind: Servicemetadata:  name: backend  spec:    ports:    - nodePort: 31000      port: 80      targetPort: 8080    selector:      app: backend    type: NodePort
```

Vous pouvez créer les ressources avec :

```
kubectl create -f backend-deployment.yamlkubectl create -f backend-service.yaml
```

Vous pouvez vérifier qu'une instance du backend est en cours d'exécution avec :

```
kubectl get pods -l=app=backend
```

Déploiement terminé.

**Est-ce que cela fonctionne vraiment, cependant ?**

Vous pouvez visiter l'application dans votre navigateur avec la commande suivante :

```
minikube service backend
```

et

```
minikube service frontend
```

Si cela fonctionne, vous devriez essayer d'acheter quelques articles !

Le worker traite-t-il les transactions ?

Oui, donné suffisamment de temps, le worker traitera tous les messages en attente.

Félicitations !

Vous venez de déployer l'application sur Kubernetes !

### Mise à l'échelle manuelle pour répondre à une demande croissante

Un seul worker peut ne pas être en mesure de gérer un grand nombre de messages. En fait, il ne peut traiter qu'un seul message à la fois.

Si vous décidez d'acheter des milliers d'articles, cela prendra des heures avant que la file d'attente ne soit vidée.

À ce stade, vous avez deux options :

* vous pouvez mettre à l'échelle manuellement
* vous pouvez créer des règles d'auto-scaling pour mettre à l'échelle automatiquement

Commençons par les bases d'abord.

Vous pouvez mettre à l'échelle le backend à trois instances avec :

```
kubectl scale --replicas=5 deployment/backend
```

Vous pouvez vérifier que Kubernetes a créé cinq instances supplémentaires avec :

```
kubectl get pods
```

Et l'application peut traiter cinq fois plus de messages.

Une fois que les workers ont vidé la file d'attente, vous pouvez réduire l'échelle avec :

```
kubectl scale --replicas=1 deployment/backend
```

La mise à l'échelle manuelle est géniale — si vous savez quand le trafic atteint le plus votre service.

Si vous ne le savez pas, la configuration d'un autoscaler permet à l'application de se mettre à l'échelle automatiquement sans intervention manuelle.

Vous n'avez besoin de définir que quelques règles.

### Exposition des métriques de l'application

Comment Kubernetes sait-il quand mettre à l'échelle votre application ?

C'est simple, vous devez le lui dire.

L'autoscaler fonctionne en surveillant les métriques. Ce n'est qu'alors qu'il peut augmenter ou diminuer les instances de votre application.

Vous pourriez donc exposer la longueur de la file d'attente comme une métrique et demander à l'autoscaler de surveiller cette valeur. Plus il y a de messages en attente dans la file d'attente, plus Kubernetes créera d'instances de votre application.

**Alors, comment exposez-vous ces métriques ?**

L'application dispose d'un point de terminaison `/metrics` pour exposer le nombre de messages dans la file d'attente. Si vous essayez de visiter cette page, vous remarquerez le contenu suivant :

```
# HELP messages Nombre de messages dans la file d'attente# TYPE messages gauge
messages 0
```

L'application n'expose pas les métriques au format JSON. Le format est en texte brut et est le standard pour exposer les [métriques Prometheus](https://prometheus.io/docs/concepts/metric_types/). Ne vous inquiétez pas de mémoriser le format. La plupart du temps, vous utiliserez l'une des [bibliothèques clientes Prometheus](https://prometheus.io/docs/instrumenting/clientlibs/).

### Consommation des métriques de l'application dans Kubernetes

Vous êtes presque prêt à auto-scaler — mais vous devez d'abord installer le serveur de métriques. En fait, Kubernetes n'ingérera pas les métriques de votre application par défaut. Vous devez activer l'[API Custom Metrics](https://github.com/kubernetes-incubator/custom-metrics-apiserver) si vous souhaitez le faire.

Pour installer l'API Custom Metrics, vous avez également besoin de [Prometheus](https://prometheus.io/) — une base de données de séries temporelles. Tous les fichiers nécessaires pour installer l'API Custom Metrics sont commodément conditionnés dans [learnk8s/spring-boot-k8s-hpa](https://github.com/learnk8s/spring-boot-k8s-hpa).

Vous devez télécharger le contenu de ce dépôt et changer le répertoire courant pour être dans le dossier `monitoring` de ce projet.

```
cd spring-boot-k8s-hpa/monitoring
```

À partir de là, vous pouvez créer l'API Custom Metrics avec :

```
kubectl create -f ./metrics-serverkubectl create -f ./namespaces.yamlkubectl create -f ./prometheuskubectl create -f ./custom-metrics-api
```

Vous devez attendre que la commande suivante retourne une liste de métriques personnalisées :

```
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1" | jq .
```

Mission accomplie !

**Vous êtes prêt à consommer des métriques.**

En fait, vous devriez déjà trouver une métrique personnalisée pour le nombre de messages dans la file d'attente :

```
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/default/pods/*/messages" | jq .
```

Félicitations, vous avez une application qui expose des métriques et un serveur de métriques qui les consomme.

Vous pouvez enfin activer l'autoscaler !

### Auto-scaling des déploiements dans Kubernetes

Kubernetes dispose d'un objet appelé [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) qui est utilisé pour surveiller les déploiements et mettre à l'échelle le nombre de Pods.

Vous aurez besoin de l'un de ceux-ci pour mettre à l'échelle vos instances automatiquement.

Vous devez créer un fichier `hpa.yaml` avec le contenu suivant :

```
apiVersion: autoscaling/v2beta1kind: HorizontalPodAutoscalermetadata:  name: spring-boot-hpaspec:  scaleTargetRef:    apiVersion: extensions/v1beta1    kind: Deployment    name: backend   minReplicas: 1  maxReplicas: 10  metrics:  - type: Pods    pods:      metricName: messages      targetAverageValue: 10
```

Le fichier est cryptique, alors laissez-moi le traduire pour vous :

* Kubernetes surveille le déploiement spécifié dans `scaleTargetRef`. Dans ce cas, c'est le worker.
* Vous utilisez la métrique `messages` pour mettre à l'échelle vos **Pods**. Kubernetes déclenchera l'auto-scaling lorsqu'il y aura plus de dix messages dans la file d'attente.
* En minimum, le déploiement doit avoir deux **Pods**. Dix **Pods** est la limite supérieure.

Vous pouvez créer la ressource avec :

```
kubectl create -f hpa.yaml
```

Après avoir soumis l'autoscaler, vous devriez remarquer que le nombre de réplicas pour le backend est de deux. Cela a du sens puisque vous avez demandé à l'autoscaler d'avoir toujours au moins deux réplicas en cours d'exécution.

Vous pouvez inspecter les conditions qui ont déclenché l'autoscaler et les événements générés en conséquence avec :

```
kubectl describe hpa
```

L'autoscaler suggère qu'il a pu mettre à l'échelle les Pods à 2 et qu'il est prêt à surveiller le déploiement.

**Des trucs passionnants, mais est-ce que cela fonctionne ?**

### Test de charge

Il n'y a qu'une seule façon de savoir si cela fonctionne : créer des charges de messages dans la file d'attente.

Rendez-vous sur l'application front-end et commencez à ajouter beaucoup de messages. Au fur et à mesure que vous ajoutez des messages, surveillez l'état de l'Horizontal Pod Autoscaler avec :

```
kubectl describe hpa
```

Le nombre de Pods passe de 2 à 4, puis à 8 et enfin à 10.

**L'application se met à l'échelle avec le nombre de messages ! Hourra !**

Vous venez de déployer une application entièrement scalable qui se met à l'échelle en fonction du nombre de messages en attente dans une file d'attente.

En passant, l'algorithme de mise à l'échelle est le suivant :

```
MAX(CURRENT_REPLICAS_LENGTH * 2, 4)
```

> _La documentation n'aide pas beaucoup lorsqu'il s'agit d'expliquer l'algorithme. Vous pouvez [trouver les détails dans le code](https://github.com/kubernetes/kubernetes/blob/bac31d698c1eed2b54374bdabfd120f7319dd5c8/pkg/controller/podautoscaler/horizontal.go#L588)._

De plus, chaque mise à l'échelle est réévaluée chaque minute, tandis que toute réduction d'échelle est réévaluée toutes les deux minutes.

Tous les paramètres ci-dessus peuvent être ajustés.

Vous n'avez pas encore terminé, cependant.

### Qu'y a-t-il de mieux que l'auto-scaling des instances ? L'auto-scaling des clusters.

La mise à l'échelle des Pods sur les nœuds fonctionne fabuleusement. **Mais que se passe-t-il si vous n'avez pas assez de capacité dans le cluster pour mettre à l'échelle vos Pods ?**

Si vous atteignez la capacité maximale, Kubernetes laissera les Pods dans un état en attente et attendra que plus de ressources soient disponibles.

Ce serait génial si vous pouviez utiliser un autoscaler similaire à l'Horizontal Pod Autoscaler, mais pour les nœuds.

Bonne nouvelle !

Vous pouvez avoir un autoscaler de cluster qui ajoute plus de nœuds à votre cluster Kubernetes au fur et à mesure que vous avez besoin de plus de ressources.

![Image](https://cdn-media-1.freecodecamp.org/images/Yp4TaOCbe6P5sKAvydPGN1dUu4un9EIAmdXm)

L'autoscaler de cluster se présente sous différentes formes et tailles. Et il est également spécifique au fournisseur cloud.

> _Veuillez noter que vous ne pourrez pas tester l'autoscaler avec `minikube`, car il est à nœud unique par définition._

Vous pouvez trouver [plus d'informations sur l'autoscaler de cluster](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler#cluster-autoscaler) et l'[implémentation du fournisseur cloud](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler#deployment) sur Github.

### Récapitulatif

La conception d'applications à grande échelle nécessite une planification et des tests minutieux.

L'architecture basée sur les files d'attente est un excellent modèle de conception pour découpler vos microservices et garantir qu'ils peuvent être mis à l'échelle et déployés indépendamment.

Et bien que vous puissiez déployer vos scripts de déploiement, il est plus facile de tirer parti d'un orchestrateur de conteneurs tel que Kubernetes pour déployer et mettre à l'échelle vos applications automatiquement.

### C'est tout pour aujourd'hui !

Merci à [Nathan Cashmore](https://www.linkedin.com/in/nathancashmore/), et [Andy Griffiths](https://andrewgriffithsonline.com/) pour leurs commentaires !

Si vous avez apprécié cet article, vous pourriez trouver intéressant de lire :

* [3 astuces simples pour des images Docker plus petites](https://learnk8s.io/blog/smaller-docker-images) et apprenez à construire et déployer des images Docker plus rapidement.
* [Ingénierie du Chaos Kubernetes : Leçons apprises — Partie 1](https://learnk8s.io/blog/kubernetes-chaos-engineering-lessons-learned) que se passe-t-il lorsque les choses tournent mal dans Kubernetes ? Kubernetes peut-il se rétablir d'une défaillance et s'auto-guérir ?

### Devenez un expert dans le déploiement et la mise à l'échelle d'applications dans Kubernetes

Apprendre à déployer et mettre à l'échelle des applications avec l'Horizontal Pod Autoscaler n'est que le début !

Prenez de l'avance avec nos cours pratiques et apprenez à maîtriser Kubernetes.

Apprenez comment :

* Gérer le trafic le plus chargé des sites web sans transpirer
* Mettre à l'échelle vos tâches sur des milliers de serveurs et réduire le temps d'attente de jours à minutes
* Avoir l'esprit tranquille en sachant que vos applications sont hautement disponibles avec une configuration multi-cloud
* Économiser beaucoup d'argent sur votre facture cloud en utilisant uniquement les ressources dont vous avez besoin
* Supercharger votre pipeline de livraison et déployer des applications 24h/24 et 7j/7

[Devenez un expert en Kubernetes](https://learnk8s.io/training) →

_Publié à l'origine sur [learnk8s.io](https://learnk8s.io/blog/scaling-spring-boot-microservices) le 11 juillet 2018._