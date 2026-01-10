---
title: Comment assurer la persistance de l'état dans les modèles de séries temporelles
  avec Docker et Redis
subtitle: ''
author: Chirag Agrawal
co_authors: []
series: null
date: '2025-10-09T01:18:59.918Z'
originalURL: https://freecodecamp.org/news/how-to-persist-state-in-time-series-models-with-docker-and-redis
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759972706788/66d45afa-f86b-4365-8a55-8b6873df718b.png
tags:
- name: Docker
  slug: docker
- name: Time Series Forecasting
  slug: time-series-forecasting
- name: Redis
  slug: redis
- name: Machine Learning
  slug: machine-learning
- name: PersistentVolumes
  slug: persistentvolumes
seo_title: Comment assurer la persistance de l'état dans les modèles de séries temporelles
  avec Docker et Redis
seo_desc: Have you ever built a brilliant time-series model, one that could forecast
  sales or predict stock prices, only to watch it fail in the real world? Well, this
  is a common frustration. Your model works perfectly on your machine, but the moment
  you depl...
---

Avez-vous déjà conçu un modèle de séries temporelles brillant, capable de prévoir des ventes ou de prédire le cours des actions, pour le voir ensuite échouer en conditions réelles ? C'est une frustration courante. Votre modèle fonctionne parfaitement sur votre machine, mais dès que vous le déployez dans un conteneur Docker, il semble devenir amnésique. Il oublie tout ce qu'il a appris la veille, rendant ses prédictions pour le lendemain inutiles.

Ne vous inquiétez pas. Il ne s'agit probablement pas d'un défaut de votre modèle, mais d'un conflit entre la conception des modèles de séries temporelles et celle des conteneurs Docker.

Les modèles de séries temporelles reposent entièrement sur la mémoire. Ils ont besoin de se souvenir du passé pour prédire l'avenir. En revanche, les conteneurs Docker sont conçus pour être sans état (stateless) et oublieux, réinitialisant leur mémoire à chaque redémarrage. Ce conflit fondamental peut transformer un modèle puissant en un outil inutile en production.

Dans cet article, nous allons résoudre ce problème. Nous allons donner à votre modèle de séries temporelles une mémoire permanente. Vous apprendrez à construire un service de prédiction prêt pour la production qui utilise Redis comme cerveau externe et des volumes Docker pour garantir que cette mémoire survive à tout redémarrage. Nous suivrons un exemple pratique, étape par étape, afin que vous puissiez apprendre à construire un système à la fois intelligent et incroyablement fiable.

### Ce que nous allons aborder :

* [À qui s'adresse ce guide ?](#heading-a-qui-sadresse-ce-guide)
    
* [Comprendre le problème](#heading-comprendre-le-probleme)
    
    * [Alors, qu'est-ce qu'un modèle de séries temporelles ?](#heading-alors-quest-ce-quun-modele-de-series-temporelles)
        
    * [1\. Les conteneurs sont éphémères par conception](#heading-1-les-conteneurs-sont-ephemeres-par-conception)
        
    * [2\. Perte de contexte entre les prédictions](#heading-2-perte-de-contexte-entre-les-predictions)
        
    * [3\. Amnésie du modèle au redémarrage](#heading-3-amnesie-du-modele-au-redemarrage)
        
* [La solution : stockage d'état externe](#heading-la-solution-stockage-detat-externe)
    
* [Mise en pratique](#heading-mise-en-pratique)
    
    * [Commencer par l'approche qui ne fonctionne pas](#heading-commencer-par-lapproche-qui-ne-fonctionne-pas)
        
    * [Comment corriger cela avec des volumes](#heading-comment-corriger-cela-avec-des-volumes)
        
    * [Comment le code gère l'état](#heading-comment-le-code-gere-letat)
        
    * [Tester l'endpoint de santé](#heading-tester-lendpoint-de-sante)
        
* [Et le passage à l'échelle ?](#heading-et-le-passage-a-lechelle)
    
    * [Mise à l'échelle horizontale avec Redis Cluster](#heading-mise-a-lechelle-horizontale-avec-redis-cluster)
        
    * [Haute disponibilité avec Redis Sentinel](#heading-haute-disponibilite-avec-redis-sentinel)
        
    * [Utiliser des services Redis gérés](#heading-utiliser-des-services-redis-geres)
        
* [Pièges courants à éviter](#heading-pieges-courants-a-eviter)
    
    * [Ne supposez pas que les volumes fonctionnent](#heading-ne-supposez-pas-que-les-volumes-fonctionnent)
        
    * [N'ignorez pas les limites de mémoire Redis](#heading-nignorez-pas-les-limites-de-memoire-redis)
        
    * [Ne négligez pas la surveillance](#heading-ne-negligez-pas-la-surveillance)
        
* [Conclusion](#heading-conclusion)
    

## À qui s'adresse ce guide ?

Pour tirer le meilleur parti de ce tutoriel, il sera utile d'avoir quelques bases. Nous allons plonger dans du code et des lignes de commande, une petite préparation sera donc très utile.

* Les outils principaux pour ce projet sont [Docker](https://docs.docker.com/get-started/get-docker/) et [Docker Compose](https://docs.docker.com/compose/). Assurez-vous qu'ils sont installés et opérationnels sur votre ordinateur.
    
* Il sera également plus facile de suivre si vous êtes à l'aise avec les bases de Docker, Python et le Framework web [Flask](http://flask.palletsprojects.com/en/stable/quickstart/). Une petite expérience en ligne de commande sera aussi pratique pour exécuter les instructions du tutoriel.
    
* Mais ne vous inquiétez pas si vous n'avez jamais utilisé [Redis](https://redis.io/docs/latest/) auparavant. Tout ce que vous devez savoir, c'est qu'il s'agit d'une base de données en mémoire ultra-rapide. Nous nous occupons du reste en cours de route.
    

Considérez cela comme une visite guidée. Tant que vous êtes curieux et que vous avez les outils de base prêts, tout ira bien.

## Comprendre le problème

Avant de passer aux solutions, clarifions d'abord ce qu'est un modèle de séries temporelles, puis explorons pourquoi sa conteneurisation est si délicate.

### Alors, qu'est-ce qu'un modèle de séries temporelles ?

Simplement dit, un modèle de séries temporelles est un type de modèle qui analyse des points de données collectés au fil du temps pour prédire des valeurs futures. Pensez à la météo : un météorologue ne regarde pas seulement le ciel à l'instant T. Il analyse la température, la pression et les vents des dernières heures et des derniers jours pour prévoir le temps de demain.

Les modèles de séries temporelles font la même chose avec les données, qu'il s'agisse du trafic d'un site web, du cours des actions ou de la consommation d'énergie. Le point clé est que l'historique compte. La séquence des événements passés fournit le contexte nécessaire pour faire une prédiction intelligente sur l'avenir.

Voici maintenant ce qui casse lorsque vous placez ces modèles dans Docker.

### 1\. Les conteneurs sont éphémères par conception

Les conteneurs Docker sont censés être sans état (stateless). Cela fonctionne très bien pour la plupart des APIs. Un endpoint de profil utilisateur ? Stateless. Un modèle d'analyse de sentiment ? Stateless. Ils reçoivent une entrée, renvoient une sortie et oublient tout entre-temps.

Les modèles de séries temporelles ne fonctionnent pas ainsi. Ils ont besoin du contexte des prédictions précédentes. Sans cela, votre modèle est pratiquement aveugle.

### 2\. Perte de contexte entre les prédictions

Chaque prédiction se produit de manière isolée. Votre modèle reçoit un seul point de données et fait une supposition sans savoir ce qui l'a précédé. Cela va à l'encontre de l'objectif même de la modélisation de séries temporelles.

Vous pourriez penser : « Je n'ai qu'à charger toutes les données historiques à chaque requête ». Mais cette approche échoue pour deux raisons :

* C'est lent. Très lent si vous avez des milliers de points de données.
    
* Ce n'est pas scalable. Lorsque vous avez plusieurs séries ou un volume de requêtes élevé, vous atteindrez rapidement des limites de performance.
    

### 3\. Amnésie du modèle au redémarrage

Chaque fois que vous déployez une nouvelle version ou que le conteneur plante, tout l'état accumulé disparaît. Votre modèle repart de zéro. En production, c'est inacceptable.

## La solution : stockage d'état externe

Au lieu de conserver l'état à l'intérieur du conteneur, nous allons le déplacer à l'extérieur. Redis devient la mémoire du modèle.

Le schéma ressemble à ceci :

```plaintext
Requête Client → Flask API → Redis → Prédiction avec Contexte
```

Votre conteneur reste stateless et remplaçable. Mais le système dans son ensemble maintient son état via Redis.

## Mise en pratique

Construisons cela. Clonez le dépôt de démonstration :

```bash
git clone https://github.com/ag-chirag/docker-redis-time-series
cd docker-redis-time-series
```

### Commencer par l'approche qui ne fonctionne pas

Le fichier `docker-compose.initial.yml` montre ce qu'il ne faut PAS faire :

```yaml
services:
  api:
    build: ./flask-api
    ports:
      - "5000:5000"
  
  redis:
    image: redis:alpine
```

Remarquez ce qui manque ? Aucun volume. Redis stocke les données dans le système de fichiers du conteneur, ce qui signifie que ces données sont temporaires.

Lancez-le :

```bash
docker compose -f docker-compose.initial.yml up
```

Faites quelques prédictions :

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "series_id": "demo",
    "historical_data": [
      {"timestamp": "2024-01-01T12:00:00", "value": 10},
      {"timestamp": "2024-01-01T12:01:00", "value": 20},
      {"timestamp": "2024-01-01T12:02:00", "value": 30}
    ]
  }'
```

Vous recevrez une réponse montrant que Redis fonctionne :

```json
{
  "data_points_used": 3,
  "prediction": 40,
  "redis_connected": true
}
```

Maintenant, redémarrez les services :

```bash
docker compose down
docker compose -f docker-compose.initial.yml up
```

Faites une autre prédiction. Vérifiez le champ `data_points_used`. Il s'est réinitialisé. Toutes vos données historiques ont disparu. C'est exactement ce que nous essayons d'éviter.

### Comment corriger cela avec des volumes

Le fichier `docker-compose.yml` correct ajoute la persistance :

```yaml
services:
  api:
    build: ./flask-api
    ports:
      - "5000:5000"
    environment:
      - REDIS_HOST=redis
  
  redis:
    image: redis:alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

volumes:
  redis_data:
```

#### Alors, qu'est-ce qu'un volume et comment ça marche ?

Considérez un volume Docker comme un disque dur externe dédié à votre conteneur. Par défaut, lorsqu'un conteneur écrit des données, il le fait sur une couche temporaire qui est détruite lors de la suppression du conteneur. Un volume permet de sauvegarder ces données de manière permanente.

Voici comment cela fonctionne :

1. Docker crée et gère une zone de stockage spéciale sur la machine hôte, totalement séparée du système de fichiers de tout conteneur. Dans notre `docker-compose.yml`, la section `volumes: redis_data:` en bas indique à Docker de créer un volume nommé `redis_data`.
    
2. Lorsque le conteneur Redis démarre, la ligne `volumes: - redis_data:/data` dit à Docker de « brancher » ce disque dur externe. Il connecte le volume `redis_data` au répertoire `/data` à l'intérieur du conteneur.
    
3. Désormais, chaque fois que le processus Redis à l'intérieur du conteneur écrit des données dans son répertoire `/data` (ce que nous avons configuré), il écrit en réalité dans le volume `redis_data` sur la machine hôte.
    
4. Lorsque vous lancez `docker compose down`, le conteneur Redis est détruit, mais le volume `redis_data` reste intact. C'est comme débrancher le disque dur externe : les données sont toujours en sécurité. La prochaine fois que vous lancerez `docker compose up`, un tout nouveau conteneur Redis sera créé, le volume sera rattaché, et Redis retrouvera toutes ses anciennes données exactement là où il les avait laissées.
    

Ce mécanisme est la clé pour donner à notre service avec état une mémoire qui survit aux redémarrages.

Lancez la version corrigée :

```bash
docker compose up --build
```

Envoyez plusieurs prédictions pour accumuler de l'état :

```bash
for i in {1..5}; do
  curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d "{
      \"series_id\": \"demo\",
      \"historical_data\": [{\"timestamp\": \"2024-01-01T12:0$i:00\", \"value\": $((i*10))}]
    }"
done
```

Maintenant, le test. Redémarrez tout :

```bash
docker compose down
docker compose up
```

Faites une autre prédiction. Regardez `data_points_used`. Il inclut tous les points précédents. Le modèle reprend exactement là où il s'était arrêté.

Cela fonctionne car le volume existe indépendamment du cycle de vie du conteneur.

### Comment le code gère l'état

L'API Flask dans `flask-api/app.py` stocke chaque point de données dans Redis en utilisant des sorted sets :

```python
def store_data_point(series_id, timestamp, value):
    key = f"ts:{series_id}"
    redis_client.zadd(key, {json.dumps({"ts": timestamp, "val": value}): timestamp})
```

Lors des prédictions, il récupère l'historique récent :

```python
def get_recent_data(series_id, limit=100):
    key = f"ts:{series_id}"
    data = redis_client.zrange(key, -limit, -1)
    return [json.loads(d) for d in data]
```

Les sorted sets de Redis permettent un tri temporel automatique. Le volume garantit que ces données survivent aux redémarrages.

### Tester l'endpoint de santé

Vérifiez que tout est correctement connecté :

```bash
curl http://localhost:5000/health
```

Vous devriez voir :

```json
{
  "model_loaded": true,
  "redis_connected": true,
  "status": "healthy"
}
```

Si `redis_connected` est faux, vérifiez vos logs Docker. Les problèmes courants sont la configuration réseau ou Redis qui ne démarre pas correctement.

## Et le passage à l'échelle ?

Cette configuration fonctionne bien pour les déploiements à instance unique. Lorsque le trafic augmente, vous avez plusieurs options.

### Mise à l'échelle horizontale avec Redis Cluster

Pour un débit élevé, distribuez vos données sur plusieurs nœuds Redis. Redis Cluster gère automatiquement le sharding.

### Haute disponibilité avec Redis Sentinel

Ajoutez une capacité de basculement (failover) pour que votre stockage d'état ne devienne pas un point de défaillance unique. Sentinel surveille les instances Redis et promeut les réplicas lorsque le primaire échoue.

### Utiliser des services Redis gérés

AWS ElastiCache, Azure Cache for Redis ou Google Cloud Memorystore gèrent la charge opérationnelle. Vous vous concentrez sur votre modèle, ils s'occupent de la fiabilité de Redis.

L'idée clé : vos conteneurs API restent stateless. Vous faites évoluer le stockage d'état indépendamment.

## Pièges courants à éviter

Je ne saurais trop insister là-dessus : testez votre persistance avant de déployer en production.

### Ne supposez pas que les volumes fonctionnent

Redémarrez réellement vos conteneurs et vérifiez que l'état persiste. J'ai vu des déploiements échouer parce que quelqu'un avait oublié de monter le volume en production.

### N'ignorez pas les limites de mémoire Redis

Redis garde tout en mémoire. Surveillez votre utilisation de la mémoire. Définissez des politiques `maxmemory` appropriées pour votre charge de travail. Si vous manquez de mémoire, Redis commencera à supprimer des clés ou refusera les écritures.

### Ne négligez pas la surveillance

Ajoutez des health checks. Surveillez l'état de la connexion Redis. Suivez la latence des prédictions. Vous voulez être informé quand les choses cassent, pas l'apprendre par des utilisateurs en colère.

## Conclusion

Les modèles de séries temporelles ont besoin de mémoire. Les conteneurs Docker perdent la mémoire par défaut. La solution est simple : séparer l'état du calcul.

Utilisez Redis comme stockage d'état externe. Utilisez des volumes Docker pour persister cet état. Votre modèle reste intelligent, vos conteneurs restent remplaçables et vos déploiements deviennent fiables.

Le code complet fonctionnel est disponible sur [github.com/ag-chirag/docker-redis-time-series](https://github.com/ag-chirag/docker-redis-time-series). Clonez-le, lancez-le, cassez-le, apprenez-en.

Et rappelez-vous : la solution la plus simple qui fonctionne est généralement la bonne. Vous n'avez pas toujours besoin de Kubernetes et de StatefulSets. Parfois, Docker Compose et un volume suffisent.