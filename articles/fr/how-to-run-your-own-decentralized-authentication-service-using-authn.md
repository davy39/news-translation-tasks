---
title: Comment exécuter votre propre service d'authentification décentralisé en utilisant
  AuthN
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-16T18:32:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-your-own-decentralized-authentication-service-using-authn
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-39624--2-.jpg
tags:
- name: authentication
  slug: authentication
seo_title: Comment exécuter votre propre service d'authentification décentralisé en
  utilisant AuthN
seo_desc: 'By Andrew Brown

  The old authentication systems from monolithic applications don''t work well in
  modern applications.

  When you build a web-application, you need a way to handle user authentication (the
  ability for a user to log in to your web-applicati...'
---

Par Andrew Brown

Les anciens systèmes d'authentification des applications monolithiques ne fonctionnent pas bien dans les applications modernes.

Lorsque vous construisez une application web, vous avez besoin d'un moyen de gérer l'authentification des utilisateurs (la capacité pour un utilisateur de se connecter à votre application web).

Traditionnellement, les applications web étaient construites comme des monolithes et les systèmes d'authentification étaient installés via une bibliothèque de programmation. Par exemple, Ruby on Rails utilisait Devise.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screen-Shot-2023-01-08-at-1.02.23-PM.png)
_Un exemple d'architecture monolithique fonctionnant sur une seule machine virtuelle._

L'industrie, en général, s'éloigne de l'architecture monolithique (tout fonctionnant sur un seul serveur) et adopte le développement d'applications modernes. Les développeurs divisent souvent leur base de code en services plus petits et isolés (applications web) hébergés dans des conteneurs, connus sous le nom d'architecture microservices.

Les bibliothèques d'authentification d'hier étaient conçues pour être étroitement couplées à un framework web qui encourage l'architecture monolithique. Cela signifie que nous nous retrouvons avec un système d'authentification centralisé sujet à un point de défaillance unique, mettant à rude épreuve un domaine de notre application partagé avec la logique métier. Cela entraîne également une mauvaise isolation pour la sécurité des identités.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screen-Shot-2023-01-08-at-1.13.55-PM.png)
_Un exemple d'architecture microservices avec authentification centralisée_

Ce que nous voulons, c'est que notre système d'authentification soit décentralisé, tout comme nous le ferions avec nos bases de données.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screen-Shot-2023-01-08-at-1.20.36-PM.png)
_Un exemple d'architecture microservices avec authentification décentralisée_

Pour les architectures microservices, il est considéré comme une meilleure pratique d'avoir des services avec état tels que vos services de base de données ou de stockage de données utilisant des services cloud gérés comme Amazon RDS, GCP Spanner, Azure Cosmos DB, Redis Cloud ou Aiven Postgres. Cela est dû au fait que la gestion des conteneurs avec état est difficile, et une grande perte de données ou une violation de données peut entraîner la mort de l'entreprise.

Mais la question est, est-ce également vrai pour les systèmes d'authentification ?

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screen-Shot-2023-01-08-at-1.32.00-PM.png)
_Un exemple d'architecture microservices utilisant des services gérés décentralisés_

## La solution est-elle d'utiliser un service d'authentification décentralisé géré ?

Une solution possible est d'utiliser un service d'authentification décentralisé géré tel que Okta, AuthO, Amazon Cognito, Azure AD B2C ou Ory.sh. Il existe une croyance croissante dans l'industrie que l'authentification est trop complexe ou difficile à implémenter et devrait utiliser un service cloud géré.

Sur le papier, cela semble simple : utiliser un service cloud géré pour l'authentification. Mais en pratique, vous découvrirez que ces services semblent incomplets. Ils peuvent également être extrêmement coûteux et donner un faux sentiment de sécurité et de disponibilité :

* **Amazon Cognito** ne peut pas être répliqué entre les régions, nous sommes donc vulnérables (et Cognito a effectivement connu des temps d'arrêt). Amazon Cognito ne prend pas en charge de nombreux fournisseurs d'identité (IpD) populaires. Il est rentable mais difficile à configurer, à déboguer et à utiliser.
* **Azure AD B2C** prend en charge de nombreux IpD, est très peu coûteux et offre plus de personnalisation autour des flux d'authentification. Mais vous ne pouvez pas facilement suivre les utilisateurs actifs mensuels (MAU), et souvent les utilisateurs se plaindront de l'authentification qui ne fonctionne pas en raison de problèmes intermédiaires inexpliqués. Pour obtenir l'apparence souhaitée, vous devez manipuler le HTML, le CSS et écrire du JavaScript, et vous êtes toujours limité.
* **Okta et Auth0** sont coûteux par MAU, et la tarification est confuse avec une matrice de tarification complexe. Okta a subi une violation de données en 2022. De nombreuses fonctionnalités utiles sont verrouillées par le paiement de sommes considérablement plus élevées, ce qui rend difficile l'exécution d'un modèle freemium aux côtés d'un modèle payant pour vos services.
* **Ory.SH** tente de reconstruire l'authentification à partir de zéro et pourrait finir par être le MUX.com des services d'authentification gérés. Mais son implémentation est incomplète et l'entreprise est immature (au moment de la rédaction de cet article). Donc, bien que ce soit prometteur, l'adoption d'Ory.SH pourrait vous amener à remplacer votre système d'authentification dans quelques années si quelque chose tourne mal ou si des changements drastiques sont apportés à la tarification ou à l'ensemble des fonctionnalités.

Nous remettons en question notre croyance dogmatique selon laquelle l'authentification devrait être gérée par un service cloud géré. Et ici, vous apprendrez comment implémenter votre propre système d'authentification en utilisant le projet open-source AuthN pour résoudre la partie la plus difficile de la création de votre propre service d'authentification.

## Qu'est-ce qu'AuthN ?

Le projet [Keratin AuthN](https://keratin.tech/) vous offre une solution open-source clé en main pour les mécanismes d'authentification de base dans votre application web.

Il prend en charge toutes les fonctionnalités intéressantes que vous pourriez vouloir dès la sortie de la boîte, comme :

* connexion sans mot de passe
* gestion simple des sessions
* prise en charge d'OAuth2

Cela vous permet de mettre en œuvre les meilleures pratiques de sécurité standard de l'industrie pour le stockage et la gestion des informations d'identification des utilisateurs sans être un expert.

Mais en raison de sa simplicité, il existe plusieurs choses qu'il n'inclut pas et que nous devrons apporter, comme :

* notre propre solution frontend/backend pour les pages d'inscription et de connexion,
* la liaison des utilisateurs authentifiés avec les utilisateurs dans notre application,
* les vérifications de confirmation/validation par e-mail

Avec cela à l'esprit, cet article expliquera comment mettre en place et rendre fonctionnel le service AuthN lui-même.

## Comment configurer le service AuthN

Notre service AuthN sera composé de 3 conteneurs Docker définis dans notre fichier Docker Compose :

* _authn_ (Microservice AuthN)
* _db_ (Base de données Postgres AuthN)
* _redis_ (Instance Redis AuthN)

### Comment configurer la structure des dossiers

Exécutez les commandes `mkdir` et `touch` ci-dessous pour configurer les répertoires et fichiers requis.

```bash
mkdir -p authn_service/db
touch authn_service/docker-compose.yml authn_service/dev_keys.sh authn_service/db/Dockerfile
```

Cela devrait configurer une structure de dossiers comme suit :

```
authn_service
├── db
│   └── Dockerfile
├── dev_keys.sh
└── docker-compose.yml
```

### Comment configurer les certificats SSL pour une utilisation avec Postgres pendant le développement.

Dans le cadre des meilleures pratiques de sécurité, AuthN nécessite par défaut que sa connexion à la base de données utilise SSL. À ce titre, nous devrons prendre quelques étapes supplémentaires pour générer des clés pour notre image Docker Postgres afin de faciliter cela.

`dev_keys.sh`

```bash
SECRET_KEY="TESTING123"
set -euo pipefail
openssl req -new -text -passout pass:$SECRET_KEY -subj /CN=localhost -out db/server.req -keyout db/privkey.pem
openssl rsa -in db/privkey.pem -passin pass:$SECRET_KEY -out db/server.key
openssl req -x509 -in db/server.req -text -key db/server.key -out db/server.crt
```

À partir de la racine de votre dossier, exécutez les commandes ci-dessus qui devraient générer les fichiers suivants dans le dossier db :

* **privkey.pem** (Chaîne de certificats)
* **server.crt** (Certificat signé)
* **server.key** (Clé privée)
* **server.req** (Demande de signature de certificat)

### Comment configurer le Dockerfile de Postgres

Créez un Dockerfile simple dans le dossier db qui copiera ces clés générées dans l'image et définira les permissions appropriées pour l'utilisateur Docker.

`db/Dockerfile`

```
FROM postgres:14.1-alpine

WORKDIR /var/lib/postgresql

COPY . .

RUN chown 70:70 server.key
RUN chmod 600 server.key
```

### Comment configurer Docker Compose

Configurez votre fichier Docker Compose avec le contenu ci-dessous. Une liste complète des options de configuration disponibles est disponible [ici](https://keratin.github.io/authn-server/#/config).

#### Conteneur AuthN

Une liste complète des options de configuration disponibles pour AuthN est disponible [ici](https://keratin.github.io/authn-server/#/config). Les options de configuration que nous utiliserons pour cet exemple sont :

* **APP_DOMAINS** – le domaine sur lequel notre application sera exécutée, nécessaire pour le partage de ressources cross-origin (CORS) avec le service AuthN
* **AUTHN_URL** – l'URL à laquelle nous publions le service AuthN
* **DATABASE_URL** – chaîne de connexion Postgres
* **HTTP_AUTH_USERNAME** – sera utilisé pour la communication avec les endpoints privés
* **HTTP_AUTH_PASSWORD** – sera utilisé pour la communication avec les endpoints privés
* **PORT** – le port accessible publiquement à utiliser pour notre service
* **REDIS_URL** – chaîne de connexion Redis
* **SECRET_KEY_BASE** – utilisé pour générer des clés HMAC pour le service
* **TIMEZONE** – pour le suivi et le rapport des statistiques

Un autre point important à noter ici est la commande exécutée. Cela forcerait AuthN à exécuter des migrations contre la base de données lors du démarrage du conteneur. Sans cela, notre base de données ne se remplira pas avec les définitions de tables.

```bash
sh -c "./authn migrate && ./authn server"
```

Enfin, nous avons une dépendance au service Redis qui doit être démarré et au service Postgres qui doit être sain.

La raison pour laquelle nous utilisons une _vérification de santé_ pour Postgres spécifiquement au lieu d'attendre uniquement le démarrage est que Postgres ait suffisamment de temps pour créer notre nouvelle base de données (si elle n'existe pas), avant qu'AuthN tente de démarrer.

#### Conteneur Postgres

Nous devons configurer notre base de données de conteneur Postgres et les informations d'identification pour correspondre à la chaîne de connexion que nous avons fournie à AuthN via l'option de lancement `DATABASE_URL`.

* **POSTGRES_DB** – le nom à utiliser pour notre base de données AuthN
* **POSTGRES_USER** – nom d'utilisateur Postgres souhaité
* **POSTGRES_PASSWORD** – mot de passe Postgres souhaité

Pour satisfaire nos exigences de sécurité, nous devons également que notre image Postgres démarre avec le mode SSL activé en utilisant nos clés générées précédemment. Nous faisons cela en fournissant quelques indicateurs de lancement avec référence aux chemins dans notre Dockerfile Postgres.

``` bash
-c ssl=on -c ssl_cert_file=/var/lib/postgresql/server.crt -c ssl_key_file=/var/lib/postgresql/server.key
```

#### Conteneur Redis

Pour notre conteneur Redis, nous fournirons simplement un numéro de port afin que le service démarre de manière fiable sur le même port à chaque fois. Nous ajusterons également notre commande de démarrage pour activer le mode _append only_ sur Redis, ce qui garantira que toutes les opérations d'écriture effectuées sur la base de données Redis sont journalisées dans un fichier.

`docker-compose.yml`

```yaml
version: "3.8"

services:
  authn:
    image: keratin/authn-server:1.15.0
    ports:
      - "8765:8765"
    environment:
      - TIMEZONE=EST
      - DATABASE_URL=postgres://postgres:postgres@db:5432/authn
      - REDIS_URL=redis://redis:6379/0
      - AUTHN_URL=http://authn:8765
      - PORT=8765
      - APP_DOMAINS=localhost
      - SECRET_KEY_BASE=MYSUPERSECRETKEYBASE
      - HTTP_AUTH_USERNAME=mysecretuser
      - HTTP_AUTH_PASSWORD=mysecretpass
    command: sh -c "./authn migrate && ./authn server"
    depends_on:
      redis:
        condition: service_started
      db:
        condition: service_healthy

  db:
    build: ./db
    restart: always
    command: -c ssl=on -c ssl_cert_file=/var/lib/postgresql/server.crt -c ssl_key_file=/var/lib/postgresql/server.key
    environment:
      - POSTGRES_DB=authn
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - '5432:5432'
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "postgres", "-d", "authn"]
      interval: 5s
      timeout: 5s
      retries: 2

  redis:
    image: redis
    ports: 
      - '6379:6379'
    command: ['redis-server', '--appendonly', 'yes']
```

### Démarrer le service

Démarrez le service en utilisant Docker Compose. Notez que lors du premier démarrage, il devra créer la base de données Postgres, ce qui peut prendre un moment selon votre environnement.

```
docker compose up
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/running-docker-compose.png)
_Un terminal Bash montrant docker compose up exécutant AuthN_

En naviguant vers [http://localhost:8765](http://localhost:8765/) dans votre navigateur, vous devriez maintenant être accueilli par la page de bienvenue de Keratin.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/authn-browser-running.png)
_Un navigateur web montrant AuthN en cours d'exécution sur localhost:8765_

### Créer un compte de test

Utilisez `curl` dans votre terminal pour faire une requête POST à l'endpoint des comptes pour créer de nouveaux comptes (/accounts). Vous devrez inclure l'en-tête d'origine CORS avec votre requête afin qu'AuthN sache qu'elle provient d'une source de confiance.

```bash
curl -X POST \
  -H "Origin: http://localhost" \
  -H "Content-Type: application/json" \
  -d '{"username":"garak","password":"TerokNor2023!!"}' \
  http://localhost:8765/accounts
```

Si tout se passe bien, vous devriez recevoir une réponse 200 contenant un **id_token** (JWT) indiquant que votre nouvel utilisateur a été créé et connecté avec succès.

Dans votre application frontend, vous stockeriez maintenant cela dans un cookie ou un stockage local, respectivement, pour une utilisation dans les requêtes ultérieures de l'utilisateur.

```
{"result":{"id_token":"eyJhbGciOiJSUzI............"}}
```

### Intégrer avec votre application

Vous avez maintenant un service d'authentification entièrement fonctionnel en cours d'exécution dans votre environnement de développement. Il ne reste plus qu'à configurer votre client frontend et les intégrations backend.

#### Configurer le client frontend

* [authn-js](https://github.com/keratin/authn-js)

AuthN n'inclut pas réellement de pages web physiques pour que vos utilisateurs s'inscrivent/se connectent (uniquement les endpoints). Nous devrons donc apporter notre propre solution pour collecter/valider les informations que nous voulons transmettre à AuthN.

Nous sommes également responsables de la validation/confirmation de toutes les informations utilisateur AVANT de les fournir à AuthN.

Une bibliothèque JS pratique est fournie pour faciliter l'intégration, liée ci-dessus. Ou vous pouvez interagir directement avec les [endpoints publics et privés](https://keratin.github.io/authn-server/#/api).

#### Configurer les intégrations backend

* [authn-rb](https://github.com/keratin/authn-rb)
* [authn-go](https://github.com/keratin/authn-rb)
* [authn-node](https://github.com/keratin/authn-node)

AuthN ne fournit aucun type d'intégration backend directe avec votre application.

Les utilisateurs seront simplement authentifiés après l'inscription. Ils se voient attribuer un user_id par le système que vous devrez associer manuellement avec les enregistrements correspondants dans votre propre table d'utilisateurs pour votre application.

AuthN fournit quelques outils d'intégration de base pour [Ruby](https://github.com/keratin/authn-rb), [Go](https://github.com/keratin/authn-go) et [NodeJS](https://github.com/keratin/authn-node) pour servir de point de départ à votre intégration.

## Conclusion

Nous pouvons utiliser AuthN pour résoudre les problèmes les plus difficiles concernant l'authentification décentralisée. Mais nous devrons développer notre propre interface utilisateur et nos propres e-mails transactionnels autour d'AuthN pour compléter la solution.