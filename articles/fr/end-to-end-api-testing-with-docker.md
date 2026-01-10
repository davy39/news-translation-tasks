---
title: Un guide complet pour les tests API de bout en bout avec Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-13T20:29:11.000Z'
originalURL: https://freecodecamp.org/news/end-to-end-api-testing-with-docker
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/api-end-to-end-testing-with-docker-1.png
tags:
- name: continuous delivery
  slug: continuous-delivery
- name: Continuous Integration
  slug: continuous-integration
- name: Developer Tools
  slug: developer-tools
- name: Devops
  slug: devops
- name: Docker
  slug: docker
seo_title: Un guide complet pour les tests API de bout en bout avec Docker
seo_desc: 'By Jean-Paul Delimat

  Testing is a pain in general. Some don''t see the point. Some see it but think of
  it as an extra step slowing them down. Sometimes tests are there but very long to
  run or unstable. In this article you''ll see how you can engineer t...'
---

Par Jean-Paul Delimat

Les tests sont généralement une source de frustration. Certains n'en voient pas l'utilité. D'autres en voient l'intérêt mais les considèrent comme une étape supplémentaire qui les ralentit. Parfois, les tests existent mais sont très longs à exécuter ou instables. Dans cet article, vous découvrirez comment concevoir des tests pour vous-même avec Docker.

Nous voulons des tests rapides, significatifs et fiables, écrits et maintenus avec un effort minimal. Cela signifie des tests qui vous sont utiles en tant que développeur au quotidien. Ils doivent améliorer votre productivité et la qualité de votre logiciel. Avoir des tests simplement parce que "tout le monde dit qu'il faut des tests" n'est pas utile si cela vous ralentit.

Voyons comment y parvenir sans trop d'effort.

## L'exemple que nous allons tester

Dans cet article, nous allons tester une API construite avec Node/express et utiliser chai/mocha pour les tests. J'ai choisi une stack JS car le code est super court et facile à lire. Les principes appliqués sont valables pour n'importe quelle stack technique. Continuez à lire même si JavaScript vous donne la nausée.

L'exemple couvrira un ensemble simple d'endpoints CRUD pour les utilisateurs. C'est plus que suffisant pour comprendre le concept et l'appliquer à la logique métier plus complexe de votre API.

Nous allons utiliser un environnement assez standard pour l'API :

* Une base de données Postgres
* Un cluster Redis
* Notre API utilisera d'autres API externes pour faire son travail

Votre API pourrait avoir besoin d'un environnement différent. Les principes appliqués dans cet article resteront les mêmes. Vous utiliserez différentes images de base Docker pour exécuter les composants dont vous avez besoin.

## Pourquoi Docker ? Et en fait Docker Compose

Cette section contient de nombreux arguments en faveur de l'utilisation de Docker pour les tests. Vous pouvez la sauter si vous souhaitez passer directement à la partie technique.

## Les alternatives douloureuses

Pour tester votre API dans un environnement proche de la production, vous avez deux choix. Vous pouvez simuler l'environnement au niveau du code ou exécuter les tests sur un serveur réel avec la base de données, etc., installée.

Simuler tout au niveau du code encombre le code et la configuration de notre API. Ce n'est également souvent pas très représentatif de la façon dont l'API se comportera en production. Exécuter le tout sur un serveur réel est lourd en infrastructure. Cela nécessite beaucoup de configuration et de maintenance, et cela ne s'adapte pas bien. Avec une base de données partagée, vous ne pouvez exécuter qu'un seul test à la fois pour vous assurer que les exécutions des tests n'interfèrent pas les unes avec les autres.

Docker Compose nous permet d'obtenir le meilleur des deux mondes. Il crée des versions "conteneurisées" de toutes les parties externes que nous utilisons. C'est de la simulation, mais à l'extérieur de notre code. Notre API pense qu'elle est dans un environnement physique réel. Docker Compose créera également un réseau isolé pour tous les conteneurs pour une exécution de test donnée. Cela vous permet d'en exécuter plusieurs en parallèle sur votre ordinateur local ou un hôte CI.

## Trop compliqué ?

Vous pourriez vous demander si ce n'est pas trop compliqué de réaliser des tests de bout en bout avec Docker Compose. Pourquoi ne pas simplement exécuter des tests unitaires à la place ?

Au cours des 10 dernières années, les grandes applications monolithiques ont été divisées en services plus petits (tendant vers les "microservices" à la mode). Un composant API donné dépend de plus de parties externes (infrastructure ou autres API). À mesure que les services deviennent plus petits, l'intégration avec l'infrastructure devient une partie plus importante du travail.

Vous devriez maintenir un petit écart entre votre production et vos environnements de développement. Sinon, des problèmes surgiront lors du déploiement en production. Par définition, ces problèmes apparaissent au pire moment possible. Ils entraîneront des corrections précipitées, une baisse de qualité et de la frustration pour l'équipe. Personne ne veut cela.

Vous pourriez vous demander si les tests de bout en bout avec Docker Compose prennent plus de temps que les tests unitaires traditionnels. Pas vraiment. Vous verrez dans l'exemple ci-dessous que nous pouvons facilement garder les tests sous 1 minute, et avec un grand avantage : les tests reflètent le comportement de l'application dans le monde réel. Cela est plus précieux que de savoir si votre classe quelque part au milieu de l'application fonctionne correctement ou non.

De plus, si vous n'avez aucun test pour le moment, commencer par des tests de bout en bout vous apporte de grands avantages pour peu d'efforts. Vous saurez que toutes les couches de l'application fonctionnent ensemble pour les scénarios les plus courants. C'est déjà quelque chose ! À partir de là, vous pouvez toujours affiner une stratégie pour tester les parties critiques de votre application.

## Notre premier test

Commençons par la partie la plus facile : notre API et la base de données Postgres. Et exécutons un simple test CRUD. Une fois que nous avons ce framework en place, nous pouvons ajouter plus de fonctionnalités à la fois à notre composant et au test.

Voici notre API minimale avec un GET/POST pour créer et lister les utilisateurs :

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const config = require('./config');

const db = require('knex')({
  client: 'pg',
  connection: {
    host : config.db.host,
    user : config.db.user,
    password : config.db.password,
  },
});

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

app.route('/api/users').post(async (req, res, next) => {
  try {
    const { email, firstname } = req.body;
    // ... valider les entrées ici ...
    const userData = { email, firstname };

    const result = await db('users').returning('id').insert(userData);
    const id = result[0];
    res.status(201).send({ id, ...userData });
  } catch (err) {
    console.log(`Erreur : Impossible de créer l'utilisateur : ${err.message}. ${err.stack}`);
    return next(err);
  }
});

app.route('/api/users').get((req, res, next) => {
  db('users')
  .select('id', 'email', 'firstname')
  .then(users => res.status(200).send(users))
  .catch(err => {
      console.log(`Impossible de récupérer les utilisateurs : ${err.message}. ${err.stack}`);
      return next(err);
  });
});

try {
  console.log("Démarrage du serveur web...");

  const port = process.env.PORT || 8000;
  app.listen(port, () => console.log(`Serveur démarré sur : ${port}`));
} catch(error) {
  console.error(error.stack);
}
```

Voici nos tests écrits avec chai. Les tests créent un nouvel utilisateur et le récupèrent. Vous pouvez voir que les tests ne sont pas couplés de quelque manière que ce soit avec le code de notre API. La variable `SERVER_URL` spécifie le point de terminaison à tester. Il peut s'agir d'un environnement local ou distant.

```javascript
const chai = require("chai");
const chaiHttp = require("chai-http");
const should = chai.should();

const SERVER_URL = process.env.APP_URL || "http://localhost:8000";

chai.use(chaiHttp);

const TEST_USER = {
  email: "john@doe.com",
  firstname: "John"
};

let createdUserId;

describe("Users", () => {
  it("should create a new user", done => {
    chai
      .request(SERVER_URL)
      .post("/api/users")
      .send(TEST_USER)
      .end((err, res) => {
        if (err) done(err)
        res.should.have.status(201);
        res.should.be.json;
        res.body.should.be.a("object");
        res.body.should.have.property("id");
        done();
      });
  });

  it("should get the created user", done => {
    chai
      .request(SERVER_URL)
      .get("/api/users")
      .end((err, res) => {
        if (err) done(err)
        res.should.have.status(200);
        res.body.should.be.a("array");

        const user = res.body.pop();
        user.id.should.equal(createdUserId);
        user.email.should.equal(TEST_USER.email);
        user.firstname.should.equal(TEST_USER.firstname);
        done();
      });
  });
});
```

Bien. Maintenant, pour tester notre API, définissons un environnement Docker Compose. Un fichier appelé `docker-compose.yml` décrira les conteneurs que Docker doit exécuter.

```yaml
version: '3.1'

services:
  db:
    image: postgres
    environment:
      POSTGRES_USER: john
      POSTGRES_PASSWORD: mysecretpassword
    expose:
      - 5432

  myapp:
    build: .
    image: myapp
    command: yarn start
    environment:
      APP_DB_HOST: db
      APP_DB_USER: john
      APP_DB_PASSWORD: mysecretpassword
    expose:
      - 8000
    depends_on:
      - db

  myapp-tests:
    image: myapp
    command: dockerize
        -wait tcp://db:5432 -wait tcp://myapp:8000 -timeout 10s
        bash -c "node db/init.js && yarn test"
    environment:
      APP_URL: http://myapp:8000
      APP_DB_HOST: db
      APP_DB_USER: john
      APP_DB_PASSWORD: mysecretpassword
    depends_on:
      - db
      - myapp
```

Alors, que avons-nous ici ? Il y a 3 conteneurs :

* **db** lance une nouvelle instance de PostgreSQL. Nous utilisons l'image publique Postgres de Docker Hub. Nous définissons le nom d'utilisateur et le mot de passe de la base de données. Nous disons à Docker d'exposer le port 5432 sur lequel la base de données écoutera afin que d'autres conteneurs puissent se connecter.
* **myapp** est le conteneur qui exécutera notre API. La commande `build` indique à Docker de construire l'image du conteneur à partir de notre source. Le reste est comme le conteneur db : variables d'environnement et ports.
* **myapp-tests** est le conteneur qui exécutera nos tests. Il utilisera la même image que myapp car le code y sera déjà, donc il n'est pas nécessaire de le reconstruire. La commande `node db/init.js && yarn test` exécutée sur le conteneur initialisera la base de données (création de tables, etc.) et exécutera les tests. Nous utilisons dockerize pour attendre que tous les serveurs requis soient opérationnels. Les options `depends_on` garantiront que les conteneurs démarrent dans un certain ordre. Cela ne garantit pas que la base de données à l'intérieur du conteneur db soit réellement prête à accepter les connexions. Ni que notre serveur API soit déjà opérationnel.

La définition de l'environnement est d'environ 20 lignes de code très faciles à comprendre. La seule partie complexe est la définition de l'environnement. Les noms d'utilisateur, les mots de passe et les URL doivent être cohérents afin que les conteneurs puissent réellement fonctionner ensemble.

Une chose à noter est que Docker Compose définira l'hôte des conteneurs qu'il crée sur le nom du conteneur. Ainsi, la base de données ne sera pas disponible sous `localhost:5432` mais sous `db:5432`. De la même manière, notre API sera servie sous `myapp:8000`. Il n'y a pas de localhost de quelque sorte que ce soit ici.

Cela signifie que votre API doit supporter les variables d'environnement en ce qui concerne la définition de l'environnement. Pas de choses codées en dur. Mais cela n'a rien à voir avec Docker ou cet article. Une application configurable est le point 3 du [manifeste des applications 12 facteurs](https://12factor.net/), donc vous devriez déjà le faire.

La toute dernière chose que nous devons dire à Docker est comment construire réellement le conteneur **myapp**. Nous utilisons un Dockerfile comme ci-dessous. Le contenu est spécifique à votre stack technique, mais l'idée est de regrouper votre API dans un serveur exécutable.

L'exemple ci-dessous pour notre API Node installe Dockerize, installe les dépendances de l'API et copie le code de l'API à l'intérieur du conteneur (le serveur est écrit en JS brut, donc pas besoin de le compiler).

```
FROM node AS base

# Dockerize est nécessaire pour synchroniser le démarrage des conteneurs
ENV DOCKERIZE_VERSION v0.6.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir -p ~/app

WORKDIR ~/app

COPY package.json .
COPY yarn.lock .

FROM base AS dependencies

RUN yarn

FROM dependencies AS runtime

COPY . .
```

Typiquement, à partir de la ligne `WORKDIR ~/app` et en dessous, vous exécuteriez des commandes qui construiraient votre application.

Et voici la commande que nous utilisons pour exécuter les tests :

```
docker-compose up --build --abort-on-container-exit
```

Cette commande indiquera à Docker Compose de lancer les composants définis dans notre fichier `docker-compose.yml`. Le drapeau `--build` déclenchera la construction du conteneur myapp en exécutant le contenu du `Dockerfile` ci-dessus. Le `--abort-on-container-exit` indiquera à Docker Compose d'arrêter l'environnement dès qu'un conteneur se termine.

Cela fonctionne bien puisque le seul composant censé se terminer est le conteneur de test **myapp-tests** après l'exécution des tests. Cerise sur le gâteau, la commande `docker-compose` se terminera avec le même code de sortie que le conteneur qui a déclenché la sortie. Cela signifie que nous pouvons vérifier si les tests ont réussi ou non depuis la ligne de commande. Cela est très utile pour les builds automatisés dans un environnement CI.

N'est-ce pas la configuration de test parfaite ?

L'exemple complet est [ici sur GitHub](https://github.com/fire-ci/tuto-api-e2e-testing). Vous pouvez cloner le dépôt et exécuter la commande docker compose :

```
docker-compose up --build --abort-on-container-exit
```

Bien sûr, vous avez besoin de Docker installé. Docker a la tendance ennuyeuse de vous forcer à créer un compte juste pour télécharger la chose. Mais vous n'avez pas vraiment à le faire. Allez aux notes de version ([lien pour Windows](https://docs.docker.com/docker-for-windows/release-notes/) et [lien pour Mac](https://docs.docker.com/docker-for-mac/release-notes/)) et téléchargez non pas la dernière version mais celle juste avant. Il s'agit d'un lien de téléchargement direct.

La toute première exécution des tests sera plus longue que d'habitude. Cela est dû au fait que Docker devra télécharger les images de base pour vos conteneurs et mettre en cache quelques choses. Les exécutions suivantes seront beaucoup plus rapides.

Les logs de l'exécution ressembleront à ceci. Vous pouvez voir que Docker est assez cool pour mettre les logs de tous les composants sur la même timeline. Cela est très pratique lors de la recherche d'erreurs.

```
Creating tuto-api-e2e-testing_db_1    ... done
Creating tuto-api-e2e-testing_redis_1 ... done
Creating tuto-api-e2e-testing_myapp_1 ... done
Creating tuto-api-e2e-testing_myapp-tests_1 ... done
Attaching to tuto-api-e2e-testing_redis_1, tuto-api-e2e-testing_db_1, tuto-api-e2e-testing_myapp_1, tuto-api-e2e-testing_myapp-tests_1
db_1           | The files belonging to this database system will be owned by user "postgres".
redis_1        | 1:M 09 Nov 2019 21:57:22.161 * Running mode=standalone, port=6379.
myapp_1        | yarn run v1.19.0
redis_1        | 1:M 09 Nov 2019 21:57:22.162 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis_1        | 1:M 09 Nov 2019 21:57:22.162 # Server initialized
db_1           | This user must also own the server process.
db_1           | 
db_1           | The database cluster will be initialized with locale "en_US.utf8".
db_1           | The default database encoding has accordingly been set to "UTF8".
db_1           | The default text search configuration will be set to "english".
db_1           | 
db_1           | Data page checksums are disabled.
db_1           | 
db_1           | fixing permissions on existing directory /var/lib/postgresql/data ... ok
db_1           | creating subdirectories ... ok
db_1           | selecting dynamic shared memory implementation ... posix
myapp-tests_1  | 2019/11/09 21:57:25 Waiting for: tcp://db:5432
myapp-tests_1  | 2019/11/09 21:57:25 Waiting for: tcp://redis:6379
myapp-tests_1  | 2019/11/09 21:57:25 Waiting for: tcp://myapp:8000
myapp_1        | $ node server.js
redis_1        | 1:M 09 Nov 2019 21:57:22.163 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
db_1           | selecting default max_connections ... 100
myapp_1        | Starting web server...
myapp-tests_1  | 2019/11/09 21:57:25 Connected to tcp://myapp:8000
myapp-tests_1  | 2019/11/09 21:57:25 Connected to tcp://db:5432
redis_1        | 1:M 09 Nov 2019 21:57:22.164 * Ready to accept connections
myapp-tests_1  | 2019/11/09 21:57:25 Connected to tcp://redis:6379
myapp_1        | Server started on: 8000
db_1           | selecting default shared_buffers ... 128MB
db_1           | selecting default time zone ... Etc/UTC
db_1           | creating configuration files ... ok
db_1           | running bootstrap script ... ok
db_1           | performing post-bootstrap initialization ... ok
db_1           | syncing data to disk ... ok
db_1           | 
db_1           | 
db_1           | Success. You can now start the database server using:
db_1           | 
db_1           |     pg_ctl -D /var/lib/postgresql/data -l logfile start
db_1           | 
db_1           | initdb: warning: enabling "trust" authentication for local connections
db_1           | You can change this by editing pg_hba.conf or using the option -A, or
db_1           | --auth-local and --auth-host, the next time you run initdb.
db_1           | waiting for server to start....2019-11-09 21:57:24.328 UTC [41] LOG:  starting PostgreSQL 12.0 (Debian 12.0-2.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit
db_1           | 2019-11-09 21:57:24.346 UTC [41] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1           | 2019-11-09 21:57:24.373 UTC [42] LOG:  database system was shut down at 2019-11-09 21:57:23 UTC
db_1           | 2019-11-09 21:57:24.383 UTC [41] LOG:  database system is ready to accept connections
db_1           |  done
db_1           | server started
db_1           | CREATE DATABASE
db_1           | 
db_1           | 
db_1           | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
db_1           | 
db_1           | waiting for server to shut down....2019-11-09 21:57:24.907 UTC [41] LOG:  received fast shutdown request
db_1           | 2019-11-09 21:57:24.909 UTC [41] LOG:  aborting any active transactions
db_1           | 2019-11-09 21:57:24.914 UTC [41] LOG:  background worker "logical replication launcher" (PID 48) exited with exit code 1
db_1           | 2019-11-09 21:57:24.914 UTC [43] LOG:  shutting down
db_1           | 2019-11-09 21:57:24.930 UTC [41] LOG:  database system is shut down
db_1           |  done
db_1           | server stopped
db_1           | 
db_1           | PostgreSQL init process complete; ready for start up.
db_1           | 
db_1           | 2019-11-09 21:57:25.038 UTC [1] LOG:  starting PostgreSQL 12.0 (Debian 12.0-2.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit
db_1           | 2019-11-09 21:57:25.039 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db_1           | 2019-11-09 21:57:25.039 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db_1           | 2019-11-09 21:57:25.052 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1           | 2019-11-09 21:57:25.071 UTC [59] LOG:  database system was shut down at 2019-11-09 21:57:24 UTC
db_1           | 2019-11-09 21:57:25.077 UTC [1] LOG:  database system is ready to accept connections
myapp-tests_1  | Creating tables ...
myapp-tests_1  | Creating table 'users'
myapp-tests_1  | Tables created succesfully
myapp-tests_1  | yarn run v1.19.0
myapp-tests_1  | $ mocha --timeout 10000 --bail
myapp-tests_1  | 
myapp-tests_1  | 
myapp-tests_1  |   Users
myapp-tests_1  | Mock server started on port: 8002
myapp-tests_1  |     ✓ should create a new user (151ms)
myapp-tests_1  |     ✓ should get the created user
myapp-tests_1  |     ✓ should not create user if mail is spammy
myapp-tests_1  |     ✓ should not create user if spammy mail API is down
myapp-tests_1  | 
myapp-tests_1  | 
myapp-tests_1  |   4 passing (234ms)
myapp-tests_1  | 
myapp-tests_1  | Done in 0.88s.
myapp-tests_1  | 2019/11/09 21:57:26 Command finished successfully.
tuto-api-e2e-testing_myapp-tests_1 exited with code 0
```

Nous pouvons voir que **db** est le conteneur qui prend le plus de temps à s'initialiser. Cela a du sens. Une fois que c'est fait, les tests commencent. Le temps d'exécution total sur mon ordinateur portable est de 16 secondes. Comparé aux 880 ms utilisés pour exécuter réellement les tests, c'est beaucoup. En pratique, des tests qui s'exécutent en moins d'une minute sont excellents car c'est presque un retour immédiat. Les 15 secondes de surcharge sont un temps d'achat qui sera constant à mesure que vous ajoutez plus de tests. Vous pourriez ajouter des centaines de tests et toujours garder le temps d'exécution sous une minute.

Voilà ! Nous avons notre framework de test opérationnel. Dans un projet réel, les prochaines étapes consisteraient à améliorer la couverture fonctionnelle de votre API avec plus de tests. Considérons les opérations CRUD couvertes. Il est temps d'ajouter plus d'éléments à notre environnement de test.

## Ajout d'un cluster Redis

Ajoutons un autre élément à notre environnement API pour comprendre ce que cela implique. Spoiler alert : ce n'est pas grand-chose.

Imaginons que notre API conserve les sessions utilisateur dans un cluster Redis. Si vous vous demandez pourquoi nous ferions cela, imaginez 100 instances de votre API en production. Les utilisateurs atteignent un serveur ou un autre en fonction de l'équilibrage de charge round robin. Chaque requête doit être authentifiée.

Cela nécessite des données de profil utilisateur pour vérifier les privilèges et d'autres logiques métiers spécifiques à l'application. Une façon de procéder est de faire un aller-retour vers la base de données pour récupérer les données chaque fois que vous en avez besoin, mais ce n'est pas très efficace. L'utilisation d'un cluster de base de données en mémoire rend les données disponibles sur tous les serveurs pour le coût d'une lecture de variable locale.

Voici comment vous améliorez votre environnement de test Docker Compose avec un service supplémentaire. Ajoutons un cluster Redis à partir de l'image Docker officielle (je n'ai gardé que les nouvelles parties du fichier) :

```yaml
services:
  db:
    ...

  redis:
    image: "redis:alpine"
    expose:
      - 6379

  myapp:
    environment:
      APP_REDIS_HOST: redis
      APP_REDIS_PORT: 6379
    ...
  myapp-tests:
    command: dockerize ... -wait tcp://redis:6379 ...
    environment:
      APP_REDIS_HOST: redis
      APP_REDIS_PORT: 6379
      ...
    ...
```

Vous pouvez voir que ce n'est pas grand-chose. Nous avons ajouté un nouveau conteneur appelé **redis**. Il utilise l'image minimale officielle redis appelée `redis:alpine`. Nous avons ajouté la configuration de l'hôte et du port Redis à notre conteneur API. Et nous avons fait en sorte que les tests attendent également ce conteneur ainsi que les autres avant d'exécuter les tests.

Modifions maintenant notre application pour qu'elle utilise réellement le cluster Redis :

```
const redis = require('redis').createClient({
  host: config.redis.host,
  port: config.redis.port,
})

...

app.route('/api/users').post(async (req, res, next) => {
  try {
    const { email, firstname } = req.body;
    // ... valider les entrées ici ...
    const userData = { email, firstname };
    const result = await db('users').returning('id').insert(userData);
    const id = result[0];
    
    // Une fois l'utilisateur créé, stocker les données dans le cluster Redis
    await redis.set(id, JSON.stringify(userData));
    
    res.status(201).send({ id, ...userData });
  } catch (err) {
    console.log(`Erreur : Impossible de créer l'utilisateur : ${err.message}. ${err.stack}`);
    return next(err);
  }
});
```

Changeons maintenant nos tests pour vérifier que le cluster Redis est peuplé avec les bonnes données. C'est pourquoi le conteneur **myapp-tests** reçoit également la configuration de l'hôte et du port Redis dans `docker-compose.yml`.

```
it("should create a new user", done => {
  chai
    .request(SERVER_URL)
    .post("/api/users")
    .send(TEST_USER)
    .end((err, res) => {
      if (err) throw err;
      res.should.have.status(201);
      res.should.be.json;
      res.body.should.be.a("object");
      res.body.should.have.property("id");
      res.body.should.have.property("email");
      res.body.should.have.property("firstname");
      res.body.id.should.not.be.null;
      res.body.email.should.equal(TEST_USER.email);
      res.body.firstname.should.equal(TEST_USER.firstname);
      createdUserId = res.body.id;

      redis.get(createdUserId, (err, cacheData) => {
        if (err) throw err;
        cacheData = JSON.parse(cacheData);
        cacheData.should.have.property("email");
        cacheData.should.have.property("firstname");
        cacheData.email.should.equal(TEST_USER.email);
        cacheData.firstname.should.equal(TEST_USER.firstname);
        done();
      });
    });
});
```

Voyez comme c'était facile. Vous pouvez construire un environnement complexe pour vos tests comme vous assemblez des briques Lego.

Nous pouvons voir un autre avantage de ce type de test d'environnement complet conteneurisé. Les tests peuvent en fait examiner les composants de l'environnement. Nos tests peuvent non seulement vérifier que notre API retourne les codes de réponse et les données appropriés. Nous pouvons également vérifier que les données dans le cluster Redis ont les valeurs appropriées. Nous pourrions également vérifier le contenu de la base de données.

## Ajout de mocks d'API

Un élément courant pour les composants d'API est d'appeler d'autres composants d'API.

Supposons que notre API doit vérifier les e-mails d'utilisateurs indésirables lors de la création d'un utilisateur. La vérification est effectuée à l'aide d'un service tiers :

```
const validateUserEmail = async (email) => {
  const res = await fetch(`${config.app.externalUrl}/validate?email=${email}`);
  if(res.status !== 200) return false;
  const json = await res.json();
  return json.result === 'valid';
}

app.route('/api/users').post(async (req, res, next) => {
  try {
    const { email, firstname } = req.body;
    // ... valider les entrées ici ...
    const userData = { email, firstname };

    // Nous ne créons pas n'importe quel utilisateur. Les e-mails indésirables doivent être rejetés
    const isValidUser = await validateUserEmail(email);
    if(!isValidUser) {
      return res.sendStatus(403);
    }

    const result = await db('users').returning('id').insert(userData);
    const id = result[0];
    await redis.set(id, JSON.stringify(userData));
    res.status(201).send({ id, ...userData });
  } catch (err) {
    console.log(`Erreur : Impossible de créer l'utilisateur : ${err.message}. ${err.stack}`);
    return next(err);
  }
});
```

Maintenant, nous avons un problème pour tester quoi que ce soit. Nous ne pouvons pas créer d'utilisateurs si l'API pour détecter les e-mails indésirables n'est pas disponible. Modifier notre API pour contourner cette étape en mode test est une source dangereuse d'encombrement du code.

Même si nous pouvions utiliser le vrai service tiers, nous ne voulons pas le faire. En règle générale, nos tests ne doivent pas dépendre d'une infrastructure externe. Tout d'abord, parce que vous exécuterez probablement vos tests de nombreuses fois dans le cadre de votre processus CI. Ce n'est pas très cool de consommer une autre API de production à cette fin. Ensuite, l'API pourrait être temporairement indisponible, faisant échouer vos tests pour de mauvaises raisons.

La bonne solution est de simuler les API externes dans nos tests.

Pas besoin de framework sophistiqué. Nous allons construire un mock générique en JS vanilla en ~20 lignes de code. Cela nous donnera l'opportunité de contrôler ce que l'API retournera à notre composant. Cela permet de tester des scénarios d'erreur.

Améliorons maintenant nos tests.

```javascript
const express = require("express");

...

const MOCK_SERVER_PORT = process.env.MOCK_SERVER_PORT || 8002;

// Un objet pour encapsuler les attributs de notre serveur mock
// Le mock stocke toutes les requêtes qu'il reçoit dans la propriété `requests`.
const mock = {
  app: express(),
  server: null,
  requests: [],
  status: 404,
  responseBody: {}
};

// Définir quel code de réponse et quel contenu le mock enverra
const setupMock = (status, body) => {
  mock.status = status;
  mock.responseBody = body;
};

// Démarrer le serveur mock
const initMock = async () => {
  mock.app.use(bodyParser.urlencoded({ extended: false }));
  mock.app.use(bodyParser.json());
  mock.app.use(cors());
  mock.app.get("*", (req, res) => {
    mock.requests.push(req);
    res.status(mock.status).send(mock.responseBody);
  });

  mock.server = await mock.app.listen(MOCK_SERVER_PORT);
  console.log(`Mock server started on port: ${MOCK_SERVER_PORT}`);
};

// Détruire le serveur mock
const teardownMock = () => {
  if (mock.server) {
    mock.server.close();
    delete mock.server;
  }
};

describe("Users", () => {
  // Notre mock est démarré avant que tout test ne commence ...
  before(async () => await initMock());

  // ... tué après que tous les tests soient exécutés ...
  after(() => {
    redis.quit();
    teardownMock();
  });

  // ... et nous réinitialisons les requêtes enregistrées entre chaque test
  beforeEach(() => (mock.requests = []));

  it("should create a new user", done => {
    // Le mock nous dira que l'email est valide dans ce test
    setupMock(200, { result: "valid" });

    chai
      .request(SERVER_URL)
      .post("/api/users")
      .send(TEST_USER)
      .end((err, res) => {
        // ... vérifier la réponse et redis comme avant
        createdUserId = res.body.id;

        // Vérifier que l'API a appelé le service mocké avec les bons paramètres
        mock.requests.length.should.equal(1);
        mock.requests[0].path.should.equal("/api/validate");
        mock.requests[0].query.should.have.property("email");
        mock.requests[0].query.email.should.equal(TEST_USER.email);
        done();
      });
  });
});
```

Les tests vérifient maintenant que l'API externe a été appelée avec les bonnes données lors de l'appel à notre API.

Nous pouvons également ajouter d'autres tests vérifiant comment notre API se comporte en fonction des codes de réponse de l'API externe :

```javascript
describe("Users", () => {
  it("should not create user if mail is spammy", done => {
    // Le mock nous dira que l'email n'est PAS valide dans ce test ...
    setupMock(200, { result: "invalid" });

    chai
      .request(SERVER_URL)
      .post("/api/users")
      .send(TEST_USER)
      .end((err, res) => {
        // ... donc l'API devrait échouer à créer l'utilisateur
        // Nous pourrions tester que la DB et Redis sont vides ici
        res.should.have.status(403);
        done();
      });
  });

  it("should not create user if spammy mail API is down", done => {
    // Le mock nous dira que le service de vérification d'email
    //  est indisponible pour ce test ...
    setupMock(500, {});

    chai
      .request(SERVER_URL)
      .post("/api/users")
      .send(TEST_USER)
      .end((err, res) => {
        // ... dans ce cas également, un utilisateur ne devrait pas être créé
        res.should.have.status(403);
        done();
      });
  });
});
```

La manière dont vous gérez les erreurs des API tierces dans votre application vous appartient, bien sûr. Mais vous comprenez l'idée.

Pour exécuter ces tests, nous devons indiquer au conteneur **myapp** quelle est l'URL de base du service tiers :

```yaml
  myapp:
    environment:
      APP_EXTERNAL_URL: http://myapp-tests:8002/api
    ...

  myapp-tests:
    environment:
      MOCK_SERVER_PORT: 8002
    ...
```

## Conclusion et quelques autres réflexions

Espérons que cet article vous a donné un aperçu de ce que Docker Compose peut faire pour vous en matière de tests d'API. L'exemple complet est [ici sur GitHub](https://github.com/fire-ci/tuto-api-e2e-testing).

L'utilisation de Docker Compose permet aux tests de s'exécuter rapidement dans un environnement proche de la production. Cela ne nécessite aucune adaptation de votre code de composant. La seule exigence est de supporter une configuration pilotée par des variables d'environnement.

La logique du composant dans cet exemple est très simple, mais les principes s'appliquent à n'importe quelle API. Vos tests seront simplement plus longs ou plus complexes. Ils s'appliquent également à n'importe quelle stack technique qui peut être mise dans un conteneur (c'est-à-dire toutes). Et une fois que vous y êtes, vous êtes à un pas de déployer vos conteneurs en production si nécessaire.

Si vous n'avez aucun test pour le moment, voici comment je vous recommande de commencer : les tests de bout en bout avec Docker Compose. C'est si simple que vous pourriez avoir votre premier test en cours d'exécution en quelques heures. N'hésitez pas à [me contacter](https://twitter.com/jpdelimat) si vous avez des questions ou besoin de conseils. Je serais ravi de vous aider.

J'espère que vous avez apprécié cet article et que vous commencerez à tester vos API avec Docker Compose. Une fois que vous avez les tests prêts, vous pouvez les exécuter directement sur notre plateforme d'intégration continue [Fire CI](https://fire.ci).

## Une dernière idée pour réussir avec les tests automatisés.

En ce qui concerne la maintenance de grandes suites de tests, la fonctionnalité la plus importante est que les tests soient faciles à lire et à comprendre. Cela est essentiel pour motiver votre équipe à maintenir les tests à jour. Les frameworks de tests complexes sont peu susceptibles d'être correctement utilisés à long terme.

Quelle que soit la stack de votre API, vous pourriez envisager d'utiliser chai/mocha pour écrire des tests pour celle-ci. Cela peut sembler inhabituel d'avoir des stacks différentes pour le code d'exécution et le code de test, mais si cela fait le travail... Comme vous pouvez le voir à partir des exemples de cet article, tester une API REST avec chai/mocha est aussi simple que possible. La courbe d'apprentissage est proche de zéro.

Donc, si vous n'avez aucun test et que vous avez une API REST à tester écrite en Java, Python, RoR, .NET ou toute autre stack, vous pourriez envisager d'essayer chai/mocha.

Si vous vous demandez comment commencer avec l'intégration continue, j'ai écrit un guide plus large à ce sujet. Le voici : [Comment commencer avec l'intégration continue](https://fire.ci/blog/how-to-get-started-with-continuous-integration/)

Publié à l'origine sur le [Blog Fire CI](https://fire.ci/blog/).