---
title: 'Apprendre Kubernetes en moins de 3 heures : Un guide détaillé pour orchestrer
  des conteneurs'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-14T19:10:07.000Z'
originalURL: https://freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0ju9JOPACF90yXSi-s2gwQ.jpeg
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Java
  slug: java
- name: Kubernetes
  slug: kubernetes
- name: Web Development
  slug: web-development
seo_title: 'Apprendre Kubernetes en moins de 3 heures : Un guide détaillé pour orchestrer
  des conteneurs'
seo_desc: 'By Rinor Maloku

  Why are banks paying me big bucks for something as simple as Kubernetes? When anybody
  — anybody can learn in under three hours?

  If you doubt me, I challenge you to give it a try! By the end of this article, you
  will be able to run a M...'
---

Par Rinor Maloku

Pourquoi les banques me paient-elles des sommes importantes pour quelque chose d'aussi simple que Kubernetes ? Alors que n'importe qui — n'importe qui peut l'apprendre en moins de trois heures ?

Si vous me doutez, je vous mets au défi d'essayer ! À la fin de cet article, vous serez capable de faire tourner une application basée sur des microservices sur un cluster Kubernetes. Et je vous le garantis parce que c'est ainsi que je présente Kubernetes à nos clients.

_Qu'est-ce que ce guide fait de différent par rapport aux autres ressources, Rinor ?_

Beaucoup de choses ! La plupart des guides commencent par les bases : les concepts de Kubernetes et les commandes kubectl. Ces guides supposent que le lecteur connaît le développement d'applications, les microservices et les conteneurs Docker.

Dans cet article, nous allons passer par :

1. Faire tourner une application basée sur des microservices sur votre ordinateur.
2. Construire des images de conteneurs pour chaque service de l'application de microservices.
3. Introduction à Kubernetes. Déployer une application basée sur des microservices dans un cluster Kubernetes géré.

La construction progressive fournit la profondeur nécessaire pour qu'un simple mortel puisse saisir la _simplicité_ de Kubernetes. Oui, Kubernetes est simple lorsque vous connaissez le contexte dans lequel il est utilisé. Sans plus attendre, voyons ce que nous allons construire.

### Démonstration de l'application

L'application a une seule fonctionnalité. Elle prend une phrase en entrée. En utilisant l'analyse de texte, elle calcule l'émotion de la phrase.

![Image](https://cdn-media-1.freecodecamp.org/images/Rl5B3SRE5U5IiIM-8-1HnZdnwMx1TzegzV3D)
_Fig. 1. Application Web d'analyse de sentiment_

D'un point de vue technique, l'application se compose de trois microservices. Chacun a une fonctionnalité spécifique :

* **SA-Frontend** : un serveur web Nginx qui **sert nos fichiers statiques ReactJS**.
* **SA-WebApp** : une application web Java qui **gère les requêtes** du frontend.
* **SA-Logic** : une application Python qui **effectue l'analyse de sentiment**.

Il est important de savoir que les microservices ne vivent pas en isolation, ils permettent une "séparation des préoccupations" mais ils doivent **toujours** interagir les uns avec les autres.

![Image](https://cdn-media-1.freecodecamp.org/images/JwIBwPsTfBmelKgSrCCkEZuTzC5Ty1pZi3K7)
_Fig. 2. Flux de données dans l'application Web d'analyse de sentiment_

Cette interaction est mieux illustrée en montrant comment les données circulent entre eux :

1. Une application cliente demande le fichier index.html (qui à son tour demande les scripts regroupés de l'application ReactJS)
2. L'utilisateur interagissant avec l'application déclenche des requêtes vers l'application Spring WebApp.
3. Spring WebApp transmet les requêtes pour l'analyse de sentiment à l'application Python.
4. L'application Python calcule le sentiment et retourne le résultat en tant que réponse.
5. Spring WebApp retourne la réponse à l'application React. (Qui représente ensuite l'information à l'utilisateur.)

Le code pour toutes ces applications peut être trouvé dans [ce dépôt](https://github.com/rinormaloku/k8s-mastery). Je recommande de le cloner immédiatement car nous allons construire des choses incroyables ensemble.

### 1. Faire tourner une application basée sur des microservices sur votre ordinateur

Nous devons démarrer les trois services. Commençons par le plus attrayant, l'application frontend.

#### Configuration de React pour le développement local

Pour démarrer l'application React, vous devez avoir NodeJS et NPM installés sur votre ordinateur. Après avoir installé ceux-ci, naviguez avec votre terminal vers le répertoire **sa-frontend**. Tapez la commande suivante :

```bash
npm install
```

Cela télécharge toutes les dépendances JavaScript de l'application React et les place dans le dossier **node_modules**. (Les dépendances sont définies dans le fichier package.json). Après que toutes les dépendances soient résolues, exécutez la commande suivante :

```bash
npm start
```

C'est tout ! Nous avons démarré notre application React et par défaut vous pouvez y accéder sur **localhost:3000**. N'hésitez pas à modifier le code et à voir les effets immédiatement sur le navigateur. Cela est rendu possible grâce au **Hot Module Replacement**. Cela rend le développement frontend très facile !

#### Préparer notre application React pour la production

Pour la production, nous devons construire notre application en fichiers statiques et les servir à l'aide d'un serveur web.

Pour construire l'application React, naviguez dans votre terminal vers le répertoire **sa-frontend**. Ensuite, exécutez la commande suivante :

```bash
npm run build
```

Cela génère un dossier nommé **build** dans votre arborescence de projet. Ce dossier contient tous les fichiers statiques nécessaires pour notre application ReactJS.

#### Servir des fichiers statiques avec Nginx

Installez et démarrez le serveur web Nginx ([comment faire](https://www.nginx.com/resources/wiki/start/topics/tutorials/install/)). Ensuite, déplacez le contenu du dossier sa-frontend/build vers [_votre_répertoire_d'installation_nginx_]/**html**.

De cette façon, le fichier index.html généré sera accessible dans [_votre_répertoire_d'installation_nginx_]/html/index.html. **C'est le fichier par défaut que Nginx sert**.

Par défaut, le serveur web Nginx écoute sur le port 80. Vous pouvez spécifier un port différent en mettant à jour la propriété server.listen dans le fichier [_votre_répertoire_d'installation_nginx_]/conf/nginx.conf.

Ouvrez votre navigateur et accédez à l'endpoint localhost:80, voyez l'application ReactJS apparaître.

![Image](https://cdn-media-1.freecodecamp.org/images/EOcacd0QABnXiFAXVHPpWcD9scHzvr7jq0Fp)
_Fig. 3. Application React servie depuis Nginx_

En tapant dans le champ : « Tapez votre phrase. » et en appuyant sur le bouton Envoyer, cela échouera avec une erreur 404 (Vous pouvez la vérifier dans la console de votre navigateur). Mais pourquoi cela ? Inspectons le code.

#### Inspection du code

Dans le fichier **App.js**, nous pouvons voir que l'appui sur le bouton Envoyer déclenche la méthode analyzeSentence. Le code de cette méthode est montré ci-dessous. (Chaque ligne commentée avec #Numéro sera expliquée sous le script) :

```js
analyzeSentence() {
    fetch('http://localhost:8080/sentiment', {  // #1
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
                       sentence: this.textField.getValue()})// #2
    })
        .then(response => response.json())
        .then(data => this.setState(data));  // #3
}
```

#1 : URL à laquelle un appel POST est effectué. (Une application doit écouter les appels à cette URL).

#2 : Le corps de la requête envoyé à cette application tel qu'affiché ci-dessous :

```
{
    sentence: "J'aime yogobella !"
}
```

#3 : La réponse met à jour l'état du composant. Cela déclenche un nouveau rendu du composant. Si nous avons reçu les données, (c'est-à-dire l'objet JSON contenant la phrase tapée et la polarité) nous afficherons le composant polarityComponent car la condition sera remplie et nous définirons le composant :

```js
const polarityComponent = this.state.polarity !== undefined ?
    <Polarity sentence={this.state.sentence} 
              polarity={this.state.polarity}/> :
    null;
```

Tout semble correct. Mais qu'est-ce qui nous manque ? Si vous avez deviné que nous n'avons rien configuré pour écouter sur localhost:8080, alors vous avez raison ! Nous devons démarrer notre application Spring Web pour qu'elle écoute sur ce port !

![Image](https://cdn-media-1.freecodecamp.org/images/KNFf142A66wPteChS7IQmcZA8ohQTZRA8U7E)
_Fig. 4. Microservice Spring WebApp manquant_

#### Configuration de l'application web Spring

Pour démarrer l'application Spring, vous devez avoir JDK8 et Maven installés. (leurs variables d'environnement doivent également être configurées). Après avoir installé ceux-ci, vous pouvez continuer à la partie suivante.

#### Emballage de l'application dans un Jar

Naviguez dans votre terminal vers le répertoire **sa-webapp** et tapez la commande suivante :

```
mvn install
```

Cela générera un dossier nommé **target**, dans le répertoire **sa-webapp**. Dans le dossier **target**, nous avons notre application Java emballée dans un jar : '**sentiment-analysis-web-0.0.1-SNAPSHOT.jar**'

#### Démarrage de notre application Java

Naviguez vers le répertoire target et démarrez l'application avec la commande :

```bash
java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar
```

Zut... Nous avons une erreur. Notre application échoue au démarrage et notre seule piste est l'exception dans la trace de la pile :

```bash
Error creating bean with name 'sentimentController': Injection of autowired dependencies failed; nested exception is java.lang.IllegalArgumentException: Could not resolve placeholder 'sa.logic.api.url' in value "${sa.logic.api.url}"
```

L'information importante ici est le placeholder sa.logic.api.url dans le **SentimentController**. Vérifions cela !

### Inspection du code

```java
@CrossOrigin(origins = "*")
@RestController
public class SentimentController {

    @Value("${sa.logic.api.url}")    // #1
    private String saLogicApiUrl;
    
    @PostMapping("/sentiment")
    public SentimentDto sentimentAnalysis(
        @RequestBody SentenceDto sentenceDto) 
    {
        RestTemplate restTemplate = new RestTemplate();
        
        return restTemplate.postForEntity(
                saLogicApiUrl + "/analyse/sentiment",    // #2
                sentenceDto, SentimentDto.class)
                .getBody();
    }
}
```

1. Le **SentimentController** a un champ nommé saLogicApiUrl. Le champ est défini par la propriété `sa.logic.api.url`.
2. La chaîne saLogicApiUrl est concaténée avec la valeur "/analyse/sentiment". Ensemble, elles forment l'URL pour faire la requête d'analyse de sentiment.

**Définition de la propriété**

Dans Spring, la source de propriété par défaut est **application.properties**. (Situé dans _sa-webapp/src/main/resources_). Mais ce n'est pas le seul moyen de définir une propriété, cela peut également être fait avec la commande précédente :

```bash
java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar 
     --sa.logic.api.url=WHAT.IS.THE.SA.LOGIC.API.URL
```

La propriété doit être initialisée avec la valeur qui définit où notre application Python est en cours d'exécution, de cette façon nous permettrons à notre application Spring Web de savoir où transférer les messages à l'exécution.

Pour simplifier les choses, décidons que nous allons exécuter l'application Python sur `localhost:5000`. N'oublions pas cela !

Exécutez la commande ci-dessous et nous sommes prêts à passer au dernier service, l'application Python.

```
java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar 
     --sa.logic.api.url=http://localhost:5000
```

![Image](https://cdn-media-1.freecodecamp.org/images/gRyXOa3fibWNB7s1DJiu31nB0ziy38FjCWe5)

#### Configuration de l'application Python

Pour démarrer l'application Python, nous devons avoir Python3 et Pip installés. (Leurs variables d'environnement doivent également être configurées).

#### Installation des dépendances

Naviguez dans le terminal vers le répertoire **sa-logic/sa** ([dépôt](https://github.com/rinormaloku/k8s-mastery)) et tapez la commande suivante :

```bash
python -m pip install -r requirements.txt
python -m textblob.download_corpora
```

#### Démarrage de l'application

Après avoir utilisé Pip pour installer les dépendances, nous sommes prêts à démarrer l'application en exécutant la commande suivante :

```bash
python sentiment_analysis.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Cela signifie que notre application est en cours d'exécution et écoute les requêtes HTTP sur le port 5000 sur localhost.

#### Inspection du code

Investiguons le code pour comprendre ce qui se passe dans l'application Python **SA Logic**.

```py
from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)                                   #1

@app.route("/analyse/sentiment", methods=['POST'])      #2
def analyse_sentiment():
    sentence = request.get_json()['sentence']           #3
    polarity = TextBlob(sentence).sentences[0].polarity #4
    return jsonify(                                     #5
        sentence=sentence,
        polarity=polarity
    )
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)                #6
```

1. Instancie un objet Flask.
2. Définit le chemin auquel une requête POST peut être faite.
3. Extrait la propriété "sentence" du corps de la requête.
4. Instancie un objet TextBlob anonyme et obtient la polarité de la première phrase. (Nous n'en avons qu'une seule).
5. Retourne la réponse avec le corps contenant la phrase et la polarité à l'appelant.
6. Exécute l'objet flask **app** pour écouter les requêtes sur 0.0.0.0:5000 (les appels à localhost:5000 atteindront également cette application).

**Les services sont configurés pour communiquer entre eux. Réouvrez le frontend sur localhost:80 et essayez-les avant de continuer !**

![Image](https://cdn-media-1.freecodecamp.org/images/Wfr68VDVe8eOlB0Z9sM8sunj60L7UZD1Hu9v)
_Fig. 6. Architecture de microservices complétée_

Dans la section suivante, nous verrons comment démarrer les services dans des conteneurs Docker, car c'est un préalable pour pouvoir les exécuter dans un cluster Kubernetes.

### 2. Construction d'images de conteneurs pour chaque service

Kubernetes est un orchestrateur de conteneurs. Compréhensiblement, nous avons besoin de conteneurs pour pouvoir les orchestrer. Mais qu'est-ce que les conteneurs ? Cela est mieux répondu par la documentation de Docker.

> _Une image de conteneur est un package léger, autonome et exécutable d'un logiciel qui inclut tout ce dont il a besoin pour fonctionner : code, runtime, outils système, bibliothèques système, paramètres. Disponible pour les applications basées sur Linux et Windows, un logiciel conteneurisé fonctionnera toujours de la même manière, indépendamment de l'environnement._

Cela signifie que les conteneurs peuvent fonctionner sur n'importe quel ordinateur — même sur le serveur de production — **sans aucune différence**.

À des fins d'illustration, comparons comment notre application React serait servie en utilisant une machine virtuelle par rapport à un conteneur.

#### Servir des fichiers statiques React depuis une VM

Les inconvénients de l'utilisation d'une machine virtuelle :

1. Inefficace en ressources, chaque VM a le surcoût d'un système d'exploitation complet.
2. Elle est dépendante de la plateforme. Ce qui fonctionnait sur votre ordinateur pourrait ne pas fonctionner sur le serveur de production.
3. Lourd et lent à mettre à l'échelle par rapport aux conteneurs.

![Image](https://cdn-media-1.freecodecamp.org/images/vP3JZyOygXDzTh7I650wZHtHWkv56ioduUJS)
_Fig. 7. Serveur web Nginx avec des fichiers statiques sur une VM_

#### Servir des fichiers statiques React depuis un conteneur

Les avantages de l'utilisation d'un conteneur.

1. Efficace en ressources, utilise le système d'exploitation hôte avec l'aide de Docker.
2. Indépendant de la plateforme. Le conteneur que vous exécutez sur votre ordinateur fonctionnera partout.
3. Léger en utilisant des couches d'images.

![Image](https://cdn-media-1.freecodecamp.org/images/6I9ZEnnQNMqeTCK8kRWoOjDucfLCJqjAUGWd)
_Fig. 8. Serveur web Nginx servant des fichiers statiques dans un conteneur_

Ce sont les caractéristiques et avantages les plus importants de l'utilisation de conteneurs. Pour plus d'informations, continuez à lire la [documentation Docker](https://www.docker.com/what-container).

#### Construction de l'image de conteneur pour l'application React (Introduction à Docker)

Le bloc de construction de base pour un conteneur Docker est le .dockerfile. Le **Dockerfile** commence avec une image de conteneur de base et suit avec une séquence d'instructions sur la façon de construire une nouvelle image de conteneur qui répond aux besoins de votre application.

Avant de commencer à définir le Dockerfile, rappelons les étapes que nous avons suivies pour servir les fichiers statiques React en utilisant Nginx :

1. Construire les fichiers statiques (npm run build)
2. Démarrer le serveur Nginx
3. Copier le contenu du dossier **build** de votre projet sa-frontend vers nginx**/**html.

Dans la section suivante, vous remarquerez des parallèles sur la façon dont la création d'un conteneur est similaire à ce que nous avons fait pendant la configuration locale de React.

#### Définition du Dockerfile pour SA-Frontend

Les instructions dans le Dockerfile pour le SA-Frontend ne sont qu'une tâche en deux étapes. C'est parce que l'équipe Nginx nous a fourni [une image de base](https://hub.docker.com/_/nginx/) pour Nginx, que nous allons utiliser pour construire par-dessus. Les deux étapes sont :

1. Commencer par l'image de base **Nginx**
2. Copier le répertoire **sa-frontend/build** vers le répertoire nginx**/**html du conteneur.

Converti en un Dockerfile, cela ressemble à :

```docker
FROM nginx
COPY build /usr/share/nginx/html
```

N'est-ce pas incroyable, c'est même lisible par un humain, faisons un récapitulatif :

Commencez par l'image nginx. (Quoi que les gars aient fait là-bas). Copiez le répertoire **build** vers le répertoire **nginx/html** dans l'image. C'est tout !

Vous vous demandez peut-être comment j'ai su où copier les fichiers de construction ? c'est-à-dire `/usr/share/nginx/html`. Très simple : C'était documenté dans l'image [nginx](https://hub.docker.com/_/nginx/) dans Docker Hub.

#### Construction et envoi du conteneur

Avant de pouvoir envoyer notre image, nous avons besoin d'un registre de conteneurs pour héberger nos images. Docker Hub est un service cloud de conteneurs gratuit que nous utiliserons pour cette démonstration. Vous avez trois tâches à accomplir avant de continuer :

1. [Installer Docker CE](https://www.docker.com/community-edition)
2. Vous inscrire sur Docker Hub.
3. Vous connecter en exécutant la commande suivante dans votre terminal :

```bash
docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
```

Après avoir terminé les tâches ci-dessus, naviguez vers le répertoire **sa-frontend**. Ensuite, exécutez la commande suivante (remplacez $DOCKER_USER_ID par votre nom d'utilisateur Docker Hub. Par exemple, rinormaloku/sentiment-analysis-frontend)

```
docker build -f Dockerfile -t $DOCKER_USER_ID/sentiment-analysis-frontend .
```

Nous pouvons supprimer `-f Dockerfile` car nous sommes déjà dans le répertoire contenant le Dockerfile.

Pour envoyer l'image, utilisez la commande docker push :

```
docker push $DOCKER_USER_ID/sentiment-analysis-frontend
```

Vérifiez dans votre dépôt Docker Hub que l'image a été envoyée avec succès.

#### Exécution du conteneur

Maintenant, l'image dans `$DOCKER_USER_ID/sentiment-analysis-frontend` peut être téléchargée et exécutée par n'importe qui :

```bash
docker pull $DOCKER_USER_ID/sentiment-analysis-frontend
docker run -d -p 80:80 $DOCKER_USER_ID/sentiment-analysis-frontend
```

Notre conteneur Docker est en cours d'exécution !

Avant de continuer, expliquons le 80:80 que je trouve déroutant :

* Le premier 80 est le port de l'hôte (c'est-à-dire mon ordinateur)
* Le second 80 représente le port du conteneur vers lequel les appels doivent être transférés.

![Image](https://cdn-media-1.freecodecamp.org/images/uUv5pZc6QErqJVcacC0vU-QEvjDjVF1VlQ9l)
_Fig. 9. Mappage de port de l'hôte vers le conteneur_

Il mappe de <hostPort> vers <containerPort>. Cela signifie que les appels au port 80 de l'hôte doivent être mappés au port 80 du conteneur, comme le montre la figure 9.

Parce que le port a été exécuté sur l'hôte (votre ordinateur) sur le port 80, il doit être accessible sur localhost:80. Si vous n'avez pas de support natif pour Docker, vous pouvez ouvrir l'application sur <ip de la machine docker>:80. Pour trouver l'ip de votre machine docker, exécutez docker-machine ip

Essayez-le ! Vous devriez pouvoir accéder à l'application React à cette adresse.

#### Le Dockerignore

Nous avons vu précédemment que la construction de l'image pour SA-Frontend était lente, pardonnez-moi, **extrêmement lente**. C'était le cas à cause du **contexte de construction** qui devait être envoyé au démon Docker. Plus en détail, le répertoire **contexte de construction** est défini par le dernier argument dans la commande docker build (le point final), qui spécifie le contexte de construction. Et dans notre cas, il incluait les dossiers suivants :

```bash
sa-frontend:
|   .dockerignore
|   Dockerfile
|   package.json
|   README.md
+---build
+---node_modules
+---public
\---src
```

Mais les seules données dont nous avons besoin se trouvent dans le dossier **build**. Télécharger autre chose serait une perte de temps. Nous pouvons améliorer notre temps de construction en supprimant les autres répertoires. C'est là que `.dockerignore` entre en jeu. Pour vous, cela sera familier car c'est comme `.gitignore`, c'est-à-dire ajouter tous les répertoires que vous souhaitez ignorer dans le fichier `.dockerignore`, comme montré ci-dessous :

```bash
node_modules
src
public
```

Le fichier `.dockerignore` doit être dans le même dossier que le Dockerfile. Maintenant, la construction de l'image ne prend que quelques secondes.

Continuons avec l'application Java.

#### Construction de l'image de conteneur pour l'application Java

Devinez quoi ! Vous avez appris presque tout sur la création d'images de conteneurs ! C'est pourquoi cette partie est extrêmement courte.

Ouvrez le Dockerfile dans **sa-webapp**, et vous trouverez seulement deux nouveaux mots-clés :

```docker
ENV SA_LOGIC_API_URL http://localhost:5000

EXPOSE 8080
```

Le mot-clé **ENV** déclare une variable d'environnement à l'intérieur du conteneur Docker. Cela nous permettra de fournir l'URL pour l'API d'analyse de sentiment lors du démarrage du conteneur.

De plus, le mot-clé **EXPOSE** expose un port que nous voulons accéder plus tard. **Mais attendez !!!** Nous ne l'avons pas fait dans le Dockerfile de SA-Frontend, bonne prise ! Cela sert uniquement à des fins de documentation, en d'autres termes, cela servira d'information à la personne lisant le Dockerfile.

Vous devriez être familier avec la construction et l'envoi de l'image du conteneur. Si des difficultés surviennent, lisez le fichier README.md dans le répertoire **sa-webapp**.

#### Construction de l'image de conteneur pour l'application Python

Dans le Dockerfile dans **sa-logic**, il n'y a pas de nouveaux mots-clés. Maintenant, vous pouvez vous appeler un Docker-Master ?.

Pour construire et envoyer l'image de conteneur, lisez le README.md dans le répertoire **sa-logic**.

#### Test de l'application conteneurisée

Pouvez-vous faire confiance à quelque chose que vous n'avez pas testé ? Moi non plus. Testons ces conteneurs.

1. Exécutez le conteneur **sa-logic** et configurez-le pour écouter sur le port 5050 :

```
docker run -d -p 5050:5000 $DOCKER_USER_ID/sentiment-analysis-logic
```

2. Exécutez le conteneur **sa-webapp** et configurez-le pour écouter sur le port 8080, et en plus, nous devons changer le port sur lequel l'application Python écoute en remplaçant la variable d'environnement SA_LOGIC_API_URL.

```
$ docker run -d -p 8080:8080 -e SA_LOGIC_API_URL='http://<container_ip or docker machine ip>:5000' $DOCKER_USER_ID/sentiment-analysis-web-app
```

Consultez le [README](https://github.com/rinormaloku/k8s-mastery/blob/master/sa-webapp/README.md) pour savoir comment obtenir l'ip du conteneur ou l'ip de la machine docker.

3. Exécutez le conteneur **sa-frontend** :

```bash
docker run -d -p 80:80 $DOCKER_USER_ID/sentiment-analysis-frontend
```

Nous avons terminé. Ouvrez votre navigateur sur **localhost:80**.

**Attention** : Si vous avez changé le port pour le sa-webapp, ou si vous utilisez l'ip de la machine docker, vous devez mettre à jour le fichier App.js dans **sa-frontend** dans la méthode analyzeSentence pour récupérer depuis la nouvelle IP ou le nouveau port. Ensuite, vous devez construire et utiliser l'image mise à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/gdDm95hkRv-AnNmuHUFDIONucxEWcvXN1p34)
_Fig. 10. Microservices s'exécutant dans des conteneurs_

#### Casse-tête 🧠 — Pourquoi Kubernetes ?

Dans cette section, nous avons appris à connaître le Dockerfile, comment l'utiliser pour construire une image, et les commandes pour la pousser vers le registre Docker. De plus, nous avons étudié comment réduire le nombre de fichiers envoyés au contexte de construction en ignorant les fichiers inutiles. Et à la fin, nous avons fait fonctionner l'application à partir de conteneurs. Alors pourquoi Kubernetes ? Nous approfondirons cela dans le prochain article, mais je veux vous laisser un casse-tête.

* Notre application web d'analyse de sentiment est devenue un succès mondial et nous avons soudainement un million de requêtes par minute pour analyser les sentiments et nous subissons une énorme charge sur **sa-webapp** et **sa-logic**. Comment pouvons-nous mettre à l'échelle les conteneurs ?

### Introduction à Kubernetes

Je promets et je n'exagère pas qu'à la fin de l'article vous vous demanderez « Pourquoi ne l'appelons-nous pas Supernetes ? ».

![Image](https://cdn-media-1.freecodecamp.org/images/6z5-sOpVzRF1YeB2kQzrXakp2kBiGDBlMx4t)
_Fig. 11. Supernetes_

Si vous avez suivi cet article depuis le début, nous avons couvert beaucoup de terrain et beaucoup de connaissances. Vous pourriez vous inquiéter que ce sera la partie la plus difficile, mais c'est la plus simple. La seule raison pour laquelle l'apprentissage de Kubernetes est intimidant est à cause du « tout le reste » et nous avons couvert cela si bien.

### Qu'est-ce que Kubernetes

Après avoir démarré nos microservices à partir de conteneurs, nous avions une question, élaborons-la davantage dans un format Q&R :  
**Q :** Comment mettons-nous à l'échelle les conteneurs ?  
**A :** Nous en démarrons un autre.  
**Q :** Comment partageons-nous la charge entre eux ? Que faire si le serveur est déjà utilisé au maximum et que nous avons besoin d'un autre serveur pour notre conteneur ? Comment calculons-nous la meilleure utilisation du matériel ?  
**A :** Ahm… Ermm… (Laissez-moi chercher sur Google).  
**Q :** Déployer des mises à jour sans rien casser ? Et si nous le faisons, comment pouvons-nous revenir à la version fonctionnelle.

Kubernetes résout toutes ces questions (et plus encore !). Ma tentative de réduire Kubernetes en une phrase serait : « Kubernetes est un orchestrateur de conteneurs, qui abstrait l'infrastructure sous-jacente. (Où les conteneurs sont exécutés) ».

Nous avons une vague idée de l'orchestration de conteneurs. Nous allons la voir en pratique dans la suite de cet article, mais c'est la première fois que nous lisons sur « l'abstraction de l'infrastructure sous-jacente ». Alors prenons un gros plan, sur celui-ci.

#### Abstraction de l'infrastructure sous-jacente

Kubernetes abstrait l'infrastructure sous-jacente en nous fournissant une API simple à laquelle nous pouvons envoyer des requêtes. Ces requêtes incitent Kubernetes à les satisfaire au mieux de ses capacités. Par exemple, c'est aussi simple que de demander « Kubernetes, démarrez 4 conteneurs de l'image x ». Ensuite, Kubernetes trouvera des nœuds sous-utilisés dans lesquels il démarrera les nouveaux conteneurs (voir Fig. 12.).

![Image](https://cdn-media-1.freecodecamp.org/images/oRhjNBu9XyT74V6dxJVs1YJhgoC2eMU8TsCX)
_Fig. 12. Requête au serveur API_

Qu'est-ce que cela signifie pour le développeur ? Qu'il n'a pas à se soucier du nombre de nœuds, de l'endroit où les conteneurs sont démarrés et de la manière dont ils communiquent. Il ne traite pas de l'optimisation du matériel ou ne s'inquiète pas de la panne des nœuds (et ils tomberont en panne, _loi de Murphy_), car de nouveaux nœuds peuvent être ajoutés au cluster Kubernetes. Pendant ce temps, Kubernetes démarrera les conteneurs dans les autres nœuds qui sont encore en cours d'exécution. Il le fait au mieux de ses capacités.

Dans la figure 12, nous pouvons voir quelques nouvelles choses :

* **Serveur API** : Notre seule façon d'interagir avec le cluster. Que ce soit pour démarrer ou arrêter un autre conteneur (err *pods) ou vérifier l'état actuel, les logs, etc.
* **Kubelet** : surveille les conteneurs (err *pods) à l'intérieur d'un nœud et communique avec le nœud maître.
* ***Pods** : Au début, pensez simplement aux pods comme des conteneurs.

Et nous nous arrêterons ici, car plonger plus profondément ne ferait que relâcher notre concentration et nous pouvons toujours le faire plus tard, il y a des ressources utiles pour apprendre, comme la documentation officielle (la manière difficile) ou lire le livre incroyable [Kubernetes in Action](https://www.amazon.com/Kubernetes-Action-Marko-Luksa/dp/1617293725), de [Marko Lukša](https://twitter.com/markoluksa).

#### Standardisation des fournisseurs de services cloud

Un autre point fort que Kubernetes met en avant, c'est qu'il standardise les fournisseurs de services cloud (CSP). C'est une déclaration audacieuse, mais élaborons avec un exemple :

— Un expert en Azure, Google Cloud Platform ou un autre CSP se retrouve à travailler sur un projet dans un tout nouveau CSP, et il n'a aucune expérience de travail avec celui-ci. Cela peut avoir de nombreuses conséquences, pour en nommer quelques-unes : il peut manquer la date limite ; l'entreprise pourrait avoir besoin d'embaucher plus de ressources, et ainsi de suite.

En revanche, avec Kubernetes, ce n'est pas un problème du tout. Parce que vous exécuterez les mêmes commandes vers le serveur API, quel que soit le CSP. Vous demandez de manière déclarative au serveur API **ce que vous voulez**. Kubernetes abstrait et implémente le **comment** pour le CSP en question.

Prenez un instant pour réfléchir — c'est une fonctionnalité extrêmement puissante. Pour l'entreprise, cela signifie qu'elles ne sont pas liées à un CSP. Elles calculent leurs dépenses sur un autre CSP, et elles passent à autre chose. Elles auront toujours l'expertise, elles auront toujours les ressources, et elles peuvent le faire pour _moins cher !_

Tout cela dit, dans la section suivante, nous mettrons Kubernetes en pratique.

### Kubernetes en pratique — Pods

Nous avons configuré les microservices pour qu'ils s'exécutent dans des conteneurs et c'était un processus fastidieux, mais cela a fonctionné. Nous avons également mentionné que cette solution n'est pas évolutive ou résiliente et que Kubernetes résout ces problèmes. Dans la suite de cet article, nous migrerons nos services vers le résultat final comme le montre la figure 13, où les conteneurs sont orchestrés par Kubernetes.

![Image](https://cdn-media-1.freecodecamp.org/images/mrA3VBYh2pbG7qH9wnsMj-QxRxZ2MAqA5oTt)
_Fig. 13. Microservices s'exécutant dans un cluster géré par Kubernetes_

Dans cet article, nous utiliserons Minikube pour le débogage local, bien que tout ce qui sera présenté fonctionne également dans Azure et dans Google Cloud Platform.

### Installation et démarrage de Minikube

Suivez la documentation officielle pour installer [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/). Lors de l'installation de Minikube, vous installerez également **Kubectl**. Il s'agit d'un client pour faire des requêtes au serveur API Kubernetes.

Pour démarrer Minikube, exécutez la commande `minikube start` et après son exécution, exécutez kubectl get nodes et vous devriez obtenir la sortie suivante

```
kubectl get nodes
NAME       STATUS    ROLES     AGE       VERSION
minikube   Ready     <none>    11m       v1.9.0
```

Minikube nous fournit un cluster Kubernetes qui n'a qu'un seul nœud, mais souvenez-vous que nous ne nous soucions pas du nombre de nœuds, Kubernetes abstrait cela, et pour nous apprendre Kubernetes, cela n'a pas d'importance. Dans la section suivante, nous commencerons avec notre première ressource Kubernetes [ROULEMENTS DE TAMBOUR] **le Pod**.

#### Pods

J'adore les conteneurs, et maintenant vous aussi. Alors pourquoi Kubernetes a-t-il décidé de nous donner des Pods comme la plus petite unité de calcul déployable ? Que fait un pod ? Les pods peuvent être composés d'un ou même d'un groupe de conteneurs qui partagent le même environnement d'exécution.

Mais devons-nous vraiment exécuter deux conteneurs dans un seul pod ? Erm.. Habituellement, vous n'exécutez qu'un seul conteneur et c'est ce que nous ferons dans nos exemples. Mais pour les cas où, par exemple, deux conteneurs doivent partager des volumes, ou communiquent entre eux en utilisant la communication inter-processus ou sont autrement étroitement couplés, alors cela est rendu possible en utilisant des **Pods**. Une autre fonctionnalité que les Pods rendent possible est que nous ne sommes pas liés aux conteneurs Docker, si nous le souhaitons, nous pouvons utiliser d'autres technologies comme [Rkt](https://coreos.com/rkt/).

![Image](https://cdn-media-1.freecodecamp.org/images/DiiFgshSEsYe9Rj2AHAUtJUI90CVH53VdioW)
_**Fig. 14. Propriétés des Pods**_

Pour résumer, les principales propriétés des Pods sont (également montrées dans la figure 14) :

1. Chaque pod a une adresse IP unique dans le cluster Kubernetes
2. Un pod peut avoir plusieurs conteneurs. Les conteneurs partagent le même espace de port, ils peuvent donc communiquer via localhost (compréhensiblement, ils ne peuvent pas utiliser le même port), et la communication avec les conteneurs des autres pods doit être faite en conjonction avec l'ip du pod.
3. Les conteneurs dans un pod partagent le même volume*, la même ip, l'espace de port, l'espace de noms IPC.

*Les conteneurs ont leurs propres systèmes de fichiers isolés, bien qu'ils soient capables de partager des données en utilisant la ressource Kubernetes **Volumes.**

Cela est plus que suffisant pour que nous continuions, mais pour satisfaire votre curiosité, consultez la [documentation officielle](https://kubernetes.io/docs/concepts/workloads/pods/pod/).

### Définition du Pod

Ci-dessous, nous avons le fichier manifeste pour notre premier pod **sa-frontend**, puis nous expliquons tous les points.

```bash
apiVersion: v1
kind: Pod                                            # 1
metadata:
  name: sa-frontend                                  # 2
spec:                                                # 3
  containers:
    - image: rinormaloku/sentiment-analysis-frontend # 4
      name: sa-frontend                              # 5
      ports:
        - containerPort: 80                          # 6
```

1. **Kind** : spécifie le type de ressource Kubernetes que nous voulons créer. Dans notre cas, un **Pod**.
2. **Name** : définit le nom de la ressource. Nous l'avons nommée **sa-frontend**.
3. **Spec** est l'objet qui définit l'état souhaité pour la ressource. La propriété la plus importante d'un Spec de Pod est le tableau de conteneurs.
4. **Image** est l'image du conteneur que nous voulons démarrer dans ce pod.
5. **Name** est le nom unique d'un conteneur dans un pod.
6. **Container Port** : est le port auquel le conteneur écoute. Ce n'est qu'un indicateur pour le lecteur (supprimer le port n'empêche pas l'accès).

### Création du pod SA Frontend

Vous pouvez trouver le fichier pour la définition du pod ci-dessus dans `resource-manifests/**sa-frontend-pod.yaml.** Vous pouvez soit naviguer dans votre terminal vers ce dossier, soit vous devrez fournir l'emplacement complet dans la ligne de commande. Ensuite, exécutez la commande :

```yaml
kubectl create -f sa-frontend-pod.yaml
pod "sa-frontend" created
```

Pour vérifier si le Pod est en cours d'exécution, exécutez la commande suivante :

```bash
kubectl get pods
NAME                          READY     STATUS    RESTARTS   AGE
sa-frontend                   1/1       Running   0          7s
```

S'il est encore en **ContainerCreating**, vous pouvez exécuter la commande ci-dessus avec l'argument `--watch` pour mettre à jour les informations lorsque le Pod est en état de fonctionnement.

#### Accès à l'application depuis l'extérieur

Pour accéder à l'application depuis l'extérieur, nous créons une ressource Kubernetes de type **Service**, qui sera notre prochain article, qui est l'implémentation appropriée, mais pour un débogage rapide, nous avons une autre option, et c'est le transfert de port :

```bash
kubectl port-forward sa-frontend 88:80
Forwarding from 127.0.0.1:88 -> 80
```

Ouvrez votre navigateur sur **127.0.0.1:88** et vous accéderez à l'application React.

#### La mauvaise façon de mettre à l'échelle

Nous avons dit que l'une des principales caractéristiques de Kubernetes était l'évolutivité, pour le prouver, faisons fonctionner un autre pod. Pour ce faire, créez une autre ressource de pod, avec la définition suivante :

```yaml
apiVersion: v1
kind: Pod                                            
metadata:
  name: sa-frontend2      # Le seul changement
spec:                                                
  containers:
    - image: rinormaloku/sentiment-analysis-frontend 
      name: sa-frontend                              
      ports:
        - containerPort: 80
```

Créez le nouveau pod en exécutant la commande suivante :

```bash
kubectl create -f sa-frontend-pod2.yaml
pod "sa-frontend2" created
```

Vérifiez que le deuxième pod est en cours d'exécution en exécutant :

```bash
kubectl get pods
NAME                          READY     STATUS    RESTARTS   AGE
sa-frontend                   1/1       Running   0          7s
sa-frontend2                  1/1       Running   0          7s
```

Maintenant, nous avons deux pods en cours d'exécution !

**Attention** : ce n'est pas la solution finale, et elle présente de nombreux défauts. Nous améliorerons cela dans la section pour une autre ressource Kubernetes **Deployments**.

#### Résumé des Pods

Le serveur web Nginx avec les fichiers statiques s'exécute dans deux pods différents. Maintenant, nous avons deux questions :

* Comment l'exposons-nous à l'extérieur pour le rendre accessible via une URL, et
* Comment équilibrons-nous la charge entre eux ?

![Image](https://cdn-media-1.freecodecamp.org/images/I4Xjozhym548e8iBKMcPJ5DnUXZojwrnmQpT)
_Fig. 15. Équilibrage de charge entre les pods_

Kubernetes nous fournit la ressource **Services**. Passons directement à cela, dans la section suivante.

### Kubernetes en pratique — Services

La ressource **Service** de Kubernetes agit comme point d'entrée pour un ensemble de pods qui fournissent le même service fonctionnel. Cette ressource effectue le travail lourd, de découverte des services et d'équilibrage de charge entre eux comme le montre la figure 16.

![Image](https://cdn-media-1.freecodecamp.org/images/vUV2hIHJnOtiiMKgw9GiExUShzlYB3hwUeWu)
_Fig. 16. Service Kubernetes maintenant les adresses IP_

Dans notre cluster Kubernetes, nous aurons des pods avec différents services fonctionnels. (Le frontend, l'application Spring WebApp et l'application Python Flask). La question se pose donc de savoir comment un service sait quels pods cibler ? C'est-à-dire comment génère-t-il la liste des endpoints pour les pods ?

Cela se fait en utilisant des **Labels**, et c'est un processus en deux étapes :

1. Appliquer un label à tous les pods que nous voulons que notre Service cible et
2. Appliquer un « sélecteur » à notre service afin de définir quels pods étiquetés cibler.

Cela est beaucoup plus simple visuellement :

![Image](https://cdn-media-1.freecodecamp.org/images/q-Eg301b9pZA7xpZ1hc2Tqj59cDQ2H18iRKp)
_Fig. 17. Pods avec labels et leurs manifestes_

Nous pouvons voir que les pods sont étiquetés avec « app: sa-frontend » et que le service cible les pods avec ce label.

#### Labels

Les labels fournissent une méthode simple pour organiser vos ressources Kubernetes. Ils représentent une paire clé-valeur et peuvent être appliqués à chaque ressource. Modifiez les manifestes pour les pods afin qu'ils correspondent à l'exemple montré précédemment dans la figure 17.

Enregistrez les fichiers après avoir terminé les modifications, et appliquez-les avec la commande suivante :

```bash
kubectl apply -f sa-frontend-pod.yaml
Warning: kubectl apply should be used on resource created by either kubectl create --save-config or kubectl apply
pod "sa-frontend" configured
kubectl apply -f sa-frontend-pod2.yaml 
Warning: kubectl apply should be used on resource created by either kubectl create --save-config or kubectl apply
pod "sa-frontend2" configured
```

Nous avons obtenu un avertissement (apply au lieu de create, bien reçu). Dans la deuxième ligne, nous voyons que les pods « sa-frontend » et « sa-frontend2 » sont configurés. Nous pouvons vérifier que les pods ont été étiquetés en filtrant les pods que nous voulons afficher :

```bash
kubectl get pod -l app=sa-frontend
NAME           READY     STATUS    RESTARTS   AGE
sa-frontend    1/1       Running   0          2h
sa-frontend2   1/1       Running   0          2h
```

Une autre façon de vérifier que nos pods sont étiquetés est d'ajouter le drapeau `--show-labels` à la commande ci-dessus. Cela affichera tous les labels pour chaque pod.  
Super ! Nos pods sont étiquetés et nous sommes prêts à les cibler avec notre Service. Commençons par définir le Service de type LoadBalancer montré dans la Fig. 18.

![Image](https://cdn-media-1.freecodecamp.org/images/xXXbN86FdMJitJZ0ueRT1DwBecqO4u681uVY)
_Fig. 18. Équilibrage de charge avec le Service LoadBalancer_

### Définition du Service

La définition YAML du Service Loadbalancer est montrée ci-dessous :

```yaml
apiVersion: v1
kind: Service              # 1
metadata:
  name: sa-frontend-lb
spec:
  type: LoadBalancer       # 2
  ports:
  - port: 80               # 3
    protocol: TCP          # 4
    targetPort: 80         # 5
  selector:                # 6
    app: sa-frontend       # 7
```

1. **Kind** : Un service.
2. **Type** : Type de spécification, nous choisissons LoadBalancer parce que nous voulons équilibrer la charge entre les pods.
3. **Port** : Spécifie le port auquel le service reçoit les requêtes.
4. **Protocol** : Définit la communication.
5. **TargetPort** : Le port auquel les requêtes entrantes sont transférées.
6. **Selector** : Objet qui contient des propriétés pour sélectionner les pods.
7. **app** : sa-frontend Définit quels pods cibler, uniquement les pods qui sont étiquetés avec « app: sa-frontend »

Pour créer le service, exécutez la commande suivante :

```
kubectl create -f service-sa-frontend-lb.yaml
service "sa-frontend-lb" created
```

Vous pouvez vérifier l'état du service en exécutant la commande suivante :

```
kubectl get svc
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
sa-frontend-lb   LoadBalancer   10.101.244.40   <pending>     80:30708/TCP   7m
```

L'**External-IP** est en état d'attente (et n'attendez pas, car cela ne va pas changer). Cela est uniquement dû au fait que nous utilisons **Minikube**. Si nous avions exécuté cela dans un fournisseur de cloud comme Azure ou GCP, nous aurions obtenu une IP publique, ce qui rend nos services accessibles dans le monde entier.

Malgré cela, Minikube ne nous laisse pas tomber, il fournit une commande utile pour le débogage local, exécutez la commande suivante :

```bash
minikube service sa-frontend-lb
Opening kubernetes service default/sa-frontend-lb in default browser...
```

Cela ouvre votre navigateur en pointant vers l'IP du service. Après que le Service reçoit la requête, il transférera l'appel à l'un des pods (peu importe lequel). Cette abstraction nous permet de voir et d'agir avec les nombreux pods comme une seule unité, en utilisant le Service comme point d'entrée.

#### Résumé du Service

Dans cette section, nous avons couvert l'étiquetage des ressources, l'utilisation de celles-ci comme sélecteurs dans les Services, et nous avons défini et créé un service LoadBalancer. Cela remplit nos exigences pour mettre à l'échelle l'application (il suffit d'ajouter de nouveaux pods étiquetés) et pour équilibrer la charge entre les pods, en utilisant le service comme point d'entrée.

### Kubernetes en pratique — Déploiements

Les déploiements Kubernetes nous aident avec une constante dans la vie de chaque application, et c'est le **changement**. De plus, les seules applications qui ne changent pas sont celles qui sont déjà mortes, et tant qu'elles ne le sont pas, de nouvelles exigences arriveront, plus de code sera livré, il sera emballé et déployé. Et à chaque étape de ce processus, des erreurs peuvent être commises.

La ressource Déploiement automatise le processus de passage d'une version de l'application à la suivante, avec un temps d'arrêt nul et en cas d'échecs, elle nous permet de revenir rapidement à la version précédente.

#### Déploiements en pratique

Actuellement, nous avons **deux pods** et **un service** qui les expose et équilibre la charge entre eux (voir Fig. 19.). Nous avons mentionné que le déploiement des pods séparément est loin d'être parfait. Cela nécessite de gérer séparément chacun (créer, mettre à jour, supprimer et surveiller leur santé). Les mises à jour rapides et les retours en arrière rapides sont hors de question ! Cela n'est pas acceptable et la ressource Kubernetes **Déploiements** résout chacun de ces problèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/81V1N8qcLyWZi4t69mWSgYbQWjQrqRD2Ye3W)
_Fig. 19. État actuel_

Avant de continuer, énonçons ce que nous voulons accomplir, car cela nous fournira l'aperçu qui nous permet de comprendre la définition du manifeste pour la ressource de déploiement. Ce que nous voulons est :

1. Deux pods de l'image rinormaloku/sentiment-analysis-frontend
2. Déploiements sans temps d'arrêt,
3. Pods étiquetés avec `**app:** sa-frontend` afin que les services soient découverts par le Service **sa-frontend-lb.**

Dans la section suivante, nous traduirons les exigences en une définition de déploiement.

### Définition du déploiement

La définition de la ressource YAML qui réalise tous les points mentionnés ci-dessus :

```yaml
apiVersion: apps/v1
kind: Deployment                                          # 1
metadata:
  name: sa-frontend
spec:
  selector:                                               # 2
    matchLabels:
      app: sa-frontend                                    
  replicas: 2                                             # 3
  minReadySeconds: 15
  strategy:
    type: RollingUpdate                                   # 4
    rollingUpdate: 
      maxUnavailable: 1                                   # 5
      maxSurge: 1                                         # 6
  template:                                               # 7
    metadata:
      labels:
        app: sa-frontend                                  # 8
    spec:
      containers:
        - image: rinormaloku/sentiment-analysis-frontend
          imagePullPolicy: Always                         # 9
          name: sa-frontend
          ports:
            - containerPort: 80
```

1. **Kind** : Un déploiement.
2. **Selector** : Les pods correspondant au sélecteur seront pris sous la gestion de ce déploiement.
3. **Replicas** est une propriété de l'objet Spec des déploiements qui définit combien de pods nous voulons exécuter. Donc seulement 2.
4. **Type** spécifie la stratégie utilisée dans ce déploiement lors du passage de la version actuelle à la suivante. La stratégie **RollingUpdate** garantit des déploiements sans temps d'arrêt.
5. **MaxUnavailable** est une propriété de l'objet RollingUpdate qui spécifie le nombre maximum de pods indisponibles autorisés (par rapport à l'état souhaité) lors d'une mise à jour progressive. Pour notre déploiement qui a 2 répliques, cela signifie qu'après avoir terminé un pod, nous aurions encore un pod en cours d'exécution, maintenant ainsi notre application accessible.
6. **MaxSurge** est une autre propriété de l'objet RollingUpdate qui définit la quantité maximale de pods ajoutés à un déploiement (par rapport à l'état souhaité). Pour notre déploiement, cela signifie que lors du passage à une nouvelle version, nous pouvons ajouter un pod, ce qui fait un total de 3 pods en même temps.
7. **Template** : spécifie le modèle de pod que le déploiement utilisera pour créer de nouveaux pods. Très probablement, la ressemblance avec les pods vous a immédiatement frappé.
8. `**app:** sa-frontend` l'étiquette à utiliser pour les pods créés par ce modèle.
9. **ImagePullPolicy** lorsqu'elle est définie sur **Always**, elle tirera les images de conteneur à chaque redéploiement.

Honnêtement, ce mur de texte m'a même confus, commençons simplement avec l'exemple :

```bash
kubectl apply -f sa-frontend-deployment.yaml
deployment "sa-frontend" created
```

Comme toujours, vérifions que tout s'est passé comme prévu :

```bash
kubectl get pods
NAME                           READY     STATUS    RESTARTS   AGE
sa-frontend                    1/1       Running   0          2d
sa-frontend-5d5987746c-ml6m4   1/1       Running   0          1m
sa-frontend-5d5987746c-mzsgg   1/1       Running   0          1m
sa-frontend2                   1/1       Running   0          2d
```

Nous avons obtenu 4 pods en cours d'exécution, deux pods créés par le déploiement et les deux autres sont ceux que nous avons créés manuellement. Supprimez ceux que nous avons créés manuellement en utilisant la commande `kubectl delete pod <pod-name>`.

**Exercice** : Supprimez également l'un des pods du déploiement et voyez ce qui se passe. Réfléchissez à la raison avant de lire l'explication ci-dessous.

**Explication** : La suppression d'un pod a fait remarquer au déploiement que l'état actuel (1 pod en cours d'exécution) est différent de l'état souhaité (2 pods en cours d'exécution), donc il a démarré un autre pod.

Alors, qu'est-ce qui était si bien avec les déploiements, en plus de maintenir l'état souhaité ? Commençons avec les avantages.

#### Avantages #1 : Déploiement sans temps d'arrêt

Notre chef de produit est venu vers nous avec une nouvelle exigence, nos clients veulent avoir un bouton vert dans le frontend. Les développeurs ont livré leur code et nous ont fourni la seule chose dont nous avons besoin, l'image du conteneur `rinormaloku/sentiment-analysis-frontend:green`. Maintenant, c'est à notre tour, nous, les DevOps, devons déployer sans temps d'arrêt, le travail acharné portera-t-il ses fruits ? Voyons cela !

Modifiez le fichier `sa-frontend-deployment.yaml` en changeant l'image du conteneur pour qu'elle pointe vers la nouvelle image : `rinormaloku/sentiment-analysis-frontend:green`. Enregistrez les modifications sous `sa-frontend-deployment-green.yaml` et exécutez la commande suivante :

```bash
kubectl apply -f sa-frontend-deployment-green.yaml --record
deployment "sa-frontend" configured
```

Nous pouvons vérifier l'état du déploiement en utilisant la commande suivante :

```bash
kubectl rollout status deployment sa-frontend
Waiting for rollout to finish: 1 old replicas are pending termination...
Waiting for rollout to finish: 1 old replicas are pending termination...
Waiting for rollout to finish: 1 old replicas are pending termination...
Waiting for rollout to finish: 1 old replicas are pending termination...
Waiting for rollout to finish: 1 old replicas are pending termination...
Waiting for rollout to finish: 1 of 2 updated replicas are available...
deployment "sa-frontend" successfully rolled out
```

Selon la sortie, le déploiement a été effectué. Cela a été fait de telle manière que les répliques ont été remplacées une par une. Ce qui signifie que notre application était toujours en ligne. Avant de continuer, vérifions que la mise à jour est en direct.

#### Vérification du déploiement

Voyons la mise à jour en direct sur nos navigateurs. Exécutez la même commande que nous avons utilisée auparavant `minikube service sa-frontend-lb`, qui ouvre le navigateur. Nous pouvons voir que le bouton a été mis à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/aRxOGkn2bSeCWdsuMPFAPRgbR7ZTQ59RX3uw)
_Fig. 20. Le bouton vert_

#### Derrière les scènes de « The RollingUpdate »

Après avoir appliqué le nouveau déploiement, Kubernetes compare le nouvel état avec l'ancien. Dans notre cas, le nouvel état demande deux pods avec l'image `rinormaloku/sentiment-analysis-frontend:green`. Cela est différent de l'état actuel en cours d'exécution, donc il déclenche le **RollingUpdate**.

![Image](https://cdn-media-1.freecodecamp.org/images/I86XgWQFhpFLolvA8v0eHmZSKGilmlTaevTa)
_Fig. 21. RollingUpdate remplaçant les pods_

Le RollingUpdate agit selon les règles que nous avons spécifiées, à savoir « **maxUnavailable:** 1 » et « **maxSurge:** 1 ». Cela signifie que le déploiement ne peut terminer qu'un seul pod et ne peut démarrer qu'un seul nouveau pod. Ce processus est répété jusqu'à ce que tous les pods soient remplacés (voir Fig. 21).

Continuons avec l'avantage numéro 2.

**Avertissement** : _À des fins de divertissement, la partie suivante est écrite sous forme de nouvelle._

#### Avantages #2 : Retour à un état précédent

Le chef de produit entre en courant dans votre bureau et il est en **crise !**

« L'application a un bug critique, en PRODUCTION !! Revenir immédiatement à la version précédente » — crie le chef de produit.

Il voit le calme en vous, sans un cillement. Vous vous tournez vers votre terminal bien-aimé et tapez :

```bash
kubectl rollout history deployment sa-frontend
deployments "sa-frontend"
REVISION  CHANGE-CAUSE
1         <none>         
2         kubectl.exe apply --filename=sa-frontend-deployment-green.yaml --record=true
```

Vous jetez un coup d'œil rapide aux déploiements précédents. « La dernière version est boguée, tandis que la version précédente fonctionnait parfaitement ? » — demandez-vous au chef de produit.

« Oui, m'écoutez-vous même ! » — crie le chef de produit.

Vous l'ignorez, vous savez ce que vous avez à faire, vous commencez à taper :

```bash
kubectl rollout undo deployment sa-frontend --to-revision=1
deployment "sa-frontend" rolled back
```

Vous actualisez la page et le changement est annulé !

La mâchoire du chef de produit s'ouvre.

Vous avez sauvé la journée !

_Fin !_

Oui… c'était une nouvelle ennuyeuse. Avant que Kubernetes n'existe, c'était bien mieux, nous avions plus de drame, une intensité plus élevée, et cela pendant une période plus longue. Ohh, le bon vieux temps !

La plupart des commandes sont explicites, à l'exception d'un détail que vous avez dû comprendre vous-même. Pourquoi la première révision a-t-elle une **CHANGE-CAUSE** de <none> tandis que la deuxième révision **a une CHANGE-CAUSE** de « kubectl.exe apply –filename=sa-frontend-deployment-green.yaml –record=true ».

Si vous avez conclu que c'est à cause du drapeau `--record` que nous avons utilisé lorsque nous avons appliqué la nouvelle image, alors vous avez tout à fait raison !

Dans la section suivante, nous utiliserons les concepts appris jusqu'à présent pour compléter toute l'architecture.

### Kubernetes et tout le reste en pratique

Nous avons appris toutes les ressources dont nous avons besoin pour compléter l'architecture, c'est pourquoi cette partie va être rapide. Dans la figure 22, nous avons grisé tout ce que nous devons encore faire. Commençons par le bas : **Déployer le déploiement sa-logic**.

![Image](https://cdn-media-1.freecodecamp.org/images/CwBGmdNtPUeZwsTSL9inGx8xikkNEejnEeVQ)
_Fig. 22. État actuel de l'application_

#### Déploiement SA-Logic

Naviguez dans votre terminal vers le dossier resource-manifests et exécutez la commande suivante :

```bash
kubectl apply -f sa-logic-deployment.yaml --record
deployment "sa-logic" created
```

Le déploiement SA-Logic a créé trois pods. (Exécutant le conteneur de notre application Python). Il les a étiquetés avec `**app:** sa-logic`. Cet étiquetage nous permet de les cibler en utilisant un sélecteur depuis le service SA-Logic. Prenez le temps d'ouvrir le fichier `sa-logic-deployment.yaml` et de vérifier le contenu.

Ce sont les mêmes concepts utilisés encore et encore, passons directement à la ressource suivante : **le service SA-Logic**.

#### Service SA Logic

Expliquons pourquoi nous avons besoin de ce Service. Notre application Java (s'exécutant dans les pods du déploiement SA — WebApp) dépend de l'analyse de sentiment effectuée par l'application Python. Mais maintenant, contrairement à lorsque nous exécutions tout localement, nous n'avons pas une seule application Python écoutant sur un port, nous avons 2 pods et si nécessaire nous pourrions en avoir plus.

C'est pourquoi nous avons besoin d'un **Service** qui « agit comme point d'entrée pour un ensemble de pods qui fournissent le même service fonctionnel ». Cela signifie que nous pouvons utiliser le Service SA-Logic comme point d'entrée pour tous les pods SA-Logic.

Faisons cela :

```
kubectl apply -f service-sa-logic.yaml
service "sa-logic" created
```

**État de l'application mis à jour** : Nous avons 2 pods (contenant l'application Python) en cours d'exécution et nous avons le service SA-Logic agissant comme un point d'entrée que nous utiliserons dans les pods SA-WebApp.

![Image](https://cdn-media-1.freecodecamp.org/images/fYibPnq4frpa7jf4aq9Htc3sT0OxtgOTZ52x)
_Fig. 23. État de l'application mis à jour_

Maintenant, nous devons déployer les pods SA-WebApp, en utilisant une ressource de déploiement.

#### Déploiement SA-WebApp

Nous commençons à comprendre les déploiements, bien que celui-ci ait une fonctionnalité supplémentaire. Si vous ouvrez le fichier `sa-web-app-deployment.yaml`, vous trouverez cette partie nouvelle :

```yaml
- image: rinormaloku/sentiment-analysis-web-app
  imagePullPolicy: Always
  name: sa-web-app
  env:
    - name: SA_LOGIC_API_URL
      value: "http://sa-logic"
  ports:
    - containerPort: 8080
```

La première chose qui nous intéresse est de savoir ce que fait la propriété **env** ? Et nous supposons qu'elle déclare la variable d'environnement SA_LOGIC_API_URL avec la valeur « [http://sa-logic](http://sa-logic/) » à l'intérieur de nos pods. Mais pourquoi l'initialisons-nous à [**http://sa-logic**](http://sa-logic/), qu'est-ce que **sa-logic** ?

Présentons-nous à **kube-dns**.

#### KUBE-DNS

Kubernetes a un pod spécial, le **kube-dns**. Et par défaut, tous les pods l'utilisent comme serveur DNS. Une propriété importante de **kube-dns** est qu'il crée un enregistrement DNS pour chaque service créé.

Cela signifie que lorsque nous avons créé le service **sa-logic**, il a obtenu une adresse IP. Son nom a été ajouté comme un enregistrement (en conjonction avec l'IP) dans kube-dns. Cela permet à tous les pods de traduire **sa-logic** en l'adresse IP du service SA-Logic.

Bien, maintenant nous pouvons continuer avec :

#### Déploiement SA WebApp (suite)

Exécutez la commande :

```bash
kubectl apply -f sa-web-app-deployment.yaml --record
deployment "sa-web-app" created
```

Terminé. Il nous reste à exposer les pods SA-WebApp à l'extérieur en utilisant un Service LoadBalancer. Cela permet à notre application React de faire des requêtes http au service qui agit comme un point d'entrée vers les pods SA-WebApp.

#### Service SA-WebApp

Ouvrez le fichier `service-sa-web-app-lb.yaml`, comme vous pouvez le voir, tout vous est familier.  
Alors sans plus attendre, exécutez la commande :

```bash
kubectl apply -f service-sa-web-app-lb.yaml
service "sa-web-app-lb" created
```

L'architecture est complète. Mais nous avons une seule dissonance. Lorsque nous avons déployé les pods SA-Frontend, notre image de conteneur pointait vers notre SA-WebApp sur [http://localhost:8080/sentiment](http://localhost:8080/sentiment). Mais maintenant, nous devons la mettre à jour pour qu'elle pointe vers l'adresse IP du Loadbalancer SA-WebApp. (Qui agit comme un point d'entrée vers les pods SA-WebApp).

Corriger cette dissonance nous offre l'opportunité de résumer une fois de plus tout ce qui va du code au déploiement. (C'est encore plus efficace si vous le faites seul au lieu de suivre le guide ci-dessous). Commençons :

1. Obtenez l'IP du Loadbalancer SA-WebApp en exécutant la commande suivante :

```bash
minikube service list
|-------------|----------------------|-----------------------------|
|  NAMESPACE  |         NAME         |             URL             |
|-------------|----------------------|-----------------------------|
| default     | kubernetes           | No node port                |
| default     | sa-frontend-lb       | http://192.168.99.100:30708 |
| default     | sa-logic             | No node port                |
| default     | sa-web-app-lb        | http://192.168.99.100:31691 |
| kube-system | kube-dns             | No node port                |
| kube-system | kubernetes-dashboard | http://192.168.99.100:30000 |
|-------------|----------------------|-----------------------------|
```

2. Utilisez l'IP du LoadBalancer SA-WebApp dans le fichier `sa-frontend/src/App.js`, comme montré ci-dessous :

```js
analyzeSentence() {
        fetch('http://192.168.99.100:31691/sentiment', { /* raccourci pour plus de concision */})
            .then(response => response.json())
            .then(data => this.setState(data));
    }
```

3. Construisez les fichiers statiques `npm run build` (vous devez naviguer vers le dossier **sa-frontend**)

4. Construisez l'image du conteneur :

```bash
docker build -f Dockerfile -t $DOCKER_USER_ID/sentiment-analysis-frontend:minikube .
```

5. Envoyez l'image vers Docker hub.

```bash
docker push $DOCKER_USER_ID/sentiment-analysis-frontend:minikube
```

6. Modifiez le fichier sa-frontend-deployment.yaml pour utiliser la nouvelle image et

7. Exécutez la commande kubectl apply -f sa-frontend-deployment.yaml

Actualisez le navigateur ou si vous avez fermé la fenêtre, exécutez `minikube service sa-frontend-lb`. Essayez en tapant une phrase !

![Image](https://cdn-media-1.freecodecamp.org/images/GkLNiTbXMvnaTdwnH0DjS-Lhq7mizlAnl9Mm)

### Résumé de l'article

Kubernetes est bénéfique pour l'équipe, pour le projet, simplifie les déploiements, l'évolutivité, la résilience, il nous permet de consommer n'importe quelle infrastructure sous-jacente et vous savez quoi ? À partir de maintenant, appelons-le Supernetes !

Ce que nous avons couvert dans cette série :

* Construction / Emballage / Exécution d'applications ReactJS, Java et Python
* Conteneurs Docker ; comment les définir et les construire en utilisant des Dockerfiles,
* Registres de conteneurs ; nous avons utilisé Docker Hub comme dépôt pour nos conteneurs.
* Nous avons couvert les parties les plus importantes de Kubernetes.
* Pods
* Services
* Déploiements
* Nouveaux concepts comme les déploiements sans temps d'arrêt
* Création d'applications évolutives
* Et en cours de route, nous avons migré toute l'application de microservices vers un cluster Kubernetes.

Je suis Rinor Maloku et je veux vous remercier de m'avoir accompagné dans ce voyage. Puisque vous avez lu jusqu'ici, je sais que vous avez aimé cet article et seriez intéressé par d'autres. J'écris des articles qui approfondissent les détails des nouvelles technologies tous les 3 mois. Vous pouvez toujours vous attendre à une application d'exemple, une pratique pratique et un guide qui vous fournit les bons outils et connaissances pour aborder n'importe quel projet réel.

Pour rester en contact et ne manquer aucun de mes articles, abonnez-vous à ma [newsletter](https://tinyletter.com/rinormaloku), suivez-moi sur [Twitter](https://twitter.com/rinormaloku), et consultez ma page [rinormaloku.com](https://rinormaloku.com/).