---
title: Comment déployer une application React en production en utilisant Docker et
  NGINX avec des proxies API
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2021-03-17T16:43:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-react-apps-to-production
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/fringer-cat-hddmXlPaFGo-unsplash.jpg
tags:
- name: deployment
  slug: deployment
- name: Docker
  slug: docker
- name: nginx
  slug: nginx
- name: React
  slug: react
seo_title: Comment déployer une application React en production en utilisant Docker
  et NGINX avec des proxies API
seo_desc: 'This post will help you to learn how to deploy your React applications
  to production. We are going to use Docker and NGINX to secure API keys and proxy
  requests to prevent Cross-Origin Resource Sharing (CORS) violations.

  You can find the code and vid...'
---

Cet article vous aidera à apprendre comment déployer vos applications React en production. Nous allons utiliser Docker et NGINX pour sécuriser les clés API et proxyfier les requêtes afin de prévenir les violations de partage de ressources cross-origin (CORS).

Vous pouvez trouver le **code** et la **vidéo** dans le résumé à la fin.

### Ce que vous allez apprendre dans cet article

Dans chaque cycle de vie de projet, vient le moment de le publier, et ce n'est pas toujours évident de savoir comment faire. L'environnement de production est différent de celui de développement, et les utilisateurs ne prendront pas de mesures supplémentaires pour l'exécuter. La plupart des applications web consomment une sorte d'API, et souvent, elles sont hébergées sur un serveur différent.

Dans ce cas, en tant que développeur, nous devons résoudre les problèmes de partage de ressources cross-origin (CORS). Trop souvent, nous finissons par construire un backend même si ce n'est pas nécessaire. Je crois que les développeurs devraient garder leurs applications simples et supprimer toutes les pièces redondantes.

Dans cet article, j'aimerais vous montrer comment je prépare mes applications React pour les déployer en production.

Je pourrais construire une application React triviale, mais ce ne serait pas très utile. J'ai donc décidé de connecter mon application à une [API réelle fournie par la FED de St. Louis](https://fred.stlouisfed.org/docs/api/fred/). L'API nécessite une clé d'accès pour récupérer les données, et les endpoints sont protégés contre les requêtes cross-domain - aucune application web externe ne pourra consommer directement les données.

**À noter** : Si votre application repose sur le **rendering côté serveur**, ce n'est **pas la bonne** stratégie de déploiement. Vous pouvez vous en inspirer, mais vous aurez toujours besoin d'une sorte de backend.

## Prérequis

Il est crucial d'avoir quelques connaissances de base sur la construction d'applications React. Vous devriez également connaître quelques fondamentaux de Docker avant de suivre les instructions de cet article.

Si vous avez manqué quelque chose, ne vous inquiétez pas ! Consultez simplement cet article et ce tutoriel YouTube sur FreeCodeCamp :

* [Une introduction conviviale pour les débutants aux conteneurs, aux VM et à Docker](https://www.freecodecamp.org/news/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b/) par [@iam_preethi](https://twitter.com/iam_preethi)
* [Cours accéléré sur Create React App](https://www.freecodecamp.org/news/create-react-app-crash-course/)

## Comment construire une application React d'exemple

J'ai démarré une application web simple en utilisant _create-react-app_. Le seul travail de l'application est d'afficher un graphique linéaire avec une représentation du PIB des États-Unis.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/fredapp.png)

L'application récupère les données uniquement à partir de l'API suivante :

```
https://api.stlouisfed.org/fred/series/observations?series_id=GDPCA&frequency=a&observation_start=1999-04-15&observation_end=2021-01-01&file_type=json&api_key=abcdefghijklmnopqrstuvwxyz123456
```

Voici les paramètres :

* `series_id` - L'identifiant d'une série. Le `GDPCA` représente le "PIB réel".
* `frequency` - L'agrégation des données. Le `a` représente annuel.
* `observation_start` - Le début de la période d'observation.
* `observation_end` - La fin de la période d'observation.
* `file_type` - Le format des données. Par défaut, c'est `xml`.
* `api_key` - La clé d'accès requise pour récupérer des données de cette API. Vous pouvez en demander [une ici](https://fred.stlouisfed.org/docs/api/api_key.html).

Vous pouvez trouver plus de détails dans la [documentation](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

La vie n'est pas toujours parfaite, et la conception de l'API n'est pas idéale. Elle nécessite que le développeur passe la clé d'accès et le format de sortie attendu des données en tant que paramètres d'URL.

Passer le format de sortie en tant que paramètre n'est pas un problème pour nous car cela n'ajoute que du bruit - mais la fuite de la clé API l'est. Imaginez si quelqu'un les intercepte et abuse de l'API pour effectuer une action interdite. Nous ne voulons pas prendre ce risque.

Supposons un instant que les clés API ne posent pas de problème. Pourtant, il n'est pas possible de tirer parti de cette API. L'API FRED est protégée contre les requêtes cross-domain, de sorte que nous obtiendrons les erreurs suivantes si nous essayons de l'appeler depuis un domaine externe :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/frederror.png)

De nombreux développeurs suggéreraient de construire un middleware (un backend) pour proxyfier les requêtes vers l'API et filtrer les données sensibles. Ils diraient qu'ils pourraient avoir besoin d'ajouter de nouvelles fonctionnalités à l'avenir, et dans une certaine mesure, c'est une approche équitable.

Mais je préfère construire mes applications de manière plus [YAGNI (You Ain't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it). Ainsi, je vais éviter de construire le backend jusqu'à ce que ce soit nécessaire - dans notre cas, je ne le construirai pas du tout.

## Utilisons NGINX !

Je suis un grand fan de NGINX car il apporte de la simplicité. NGINX a tout ce dont vous avez besoin pour préparer un serveur web de qualité production, comme HTTP2, la compression, TLS, et bien d'autres fonctionnalités.

Le plus important est que nous pouvons réaliser tout cela en définissant quelques lignes de configuration. Jetez un coup d'œil au snippet ci-dessous :

```/container/etc/nginx/nginx.conf
...

http {
    ...

    server {
        ...

        location /api {
            set         $args   $args&&file_type=json&api_key=abcdefghijklmnopqrstuvwxyz123456;
            proxy_pass  https://api.stlouisfed.org/fred/series;
        }
    }
}
```

Ces 4 lignes sont tout ce dont j'avais besoin pour cacher notre clé API et supprimer les erreurs CORS. Littéralement ! À partir de maintenant, toutes les requêtes HTTP vers `/api` seront proxyfiées vers l'API FRED, et seules nos applications pourront consommer l'API. Toutes les requêtes externes seront confrontées à des erreurs CORS.

> Pour éviter l'encombrement, j'ai remplacé tout le contenu par défaut du fichier par `...` (trois points). Vous pouvez trouver la version complète sur mon **GitHub** ou dans la **vidéo** (liens ci-dessous).

Et voici à quoi ressemble notre endpoint :

```
/api/observations?series_id=GDPCA&frequency=a&observation_start=1999-04-15&observation_end=2021-01-01
```

Nous n'avons pas besoin de passer les paramètres `api_key` ni `file_type` pour récupérer les données. Et personne ne peut lire la clé d'accès depuis l'URL, donc c'est sécurisé.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-14-at-12.49.55.png)

## Docker aime NGINX

La manière la plus pratique de faire tourner NGINX dans le cloud est d'utiliser Docker. Pour cette partie, je suppose que vous savez ce qu'est Docker (mais si ce n'est pas le cas, veuillez lire l'article lié dans les prérequis).

Nous devons simplement créer un Dockerfile avec le contenu suivant :

```dockerfile
FROM nginx

COPY container /
COPY build /usr/share/nginx/html
```

Et maintenant, seulement trois étapes supplémentaires sont nécessaires pour exécuter l'application FRED :

1. _Construire l'application React_. Ce processus génère le répertoire `build/` contenant les fichiers statiques.
2. _Construire l'image Docker_. Cela créera une image Docker exécutable.
3. _Publier l'image Docker_ dans un dépôt ou _l'exécuter sur la machine locale_.

Pour l'instant, essayons de l'exécuter sur notre machine.

```
$ yarn install
$ yarn build
$ docker build -t msokola/fred-app:latest .
$ docker run -p 8081:80 -it msokola/fred-app:latest
```

Le `8081` est un port sur votre machine. Cela signifie que l'application sera disponible sous l'URL suivante : `http://localhost:8081`.

Après avoir ouvert cette URL dans le navigateur, vous devriez voir des logs comme ceci dans votre terminal :

```
0.0.0.1 - - [11/Mar/2021:18:57:50 +0000] "GET / HTTP/1.1" 200 1556 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36" "-"
...
0.0.0.1 - - [11/Mar/2021:18:57:51 +0000] "GET /api/observations?series_id=GDPCA&frequency=a&observation_start=1999-04-15&observation_end=2021-01-01 HTTP/1.1" 200 404 "http://localhost:8081/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36" "-"
```

Faites attention à ces `200` car ils représentent le statut HTTP OK. Si vous voyez un `400` à côté de la requête API, cela signifie qu'il y a un problème avec votre clé API. Le `304` est également correct (cela signifie que les données ont été mises en cache).

## Comment déployer le conteneur sur AWS

Le conteneur fonctionne, nous pouvons donc le déployer. Dans cette partie de l'article, je vais vous montrer comment exécuter votre application dans Amazon Web Services (AWS).

AWS est l'une des plateformes cloud les plus populaires. Si vous souhaitez utiliser Microsoft Azure ou une autre plateforme, les étapes seront similaires mais la syntaxe des commandes sera différente.

**À noter** : J'ai enregistré une vidéo YouTube afin que vous puissiez me regarder parcourir le processus de déploiement complet. Si vous êtes bloqué ou rencontrez des problèmes, vous pouvez vérifier si nous avons les mêmes résultats à chaque étape. Si vous souhaitez regarder la vidéo, [cliquez ici](https://youtu.be/bUSXeQ4H20g) ou vous pouvez la trouver intégrée dans le _Résumé_ ci-dessous.

### 1. Installer les outils AWS CLI

Avant de commencer, vous devrez installer les outils [AWS CLI](https://aws.amazon.com/cli/), afin de pouvoir invoquer des commandes sur votre cloud.

AWS propose des assistants d'installation pour tous les systèmes d'exploitation, je vais donc sauter cette section. Après une installation réussie, vous devez vous connecter en tapant la commande suivante :

```bash
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-2
Default output format [None]: json
```

Pour générer des clés d'accès, vous devez vous connecter à votre console AWS. Là, cliquez sur votre nom d'utilisateur, et sélectionnez "_My Security Credentials_".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-16-at-22.27.53-1.png)

### 2. Créer un nouveau Elastic Container Registry (ECR)

Une fois les outils CLI configurés, nous devrons créer un espace où nous pourrons stocker les exécutables de notre application. Nous utilisons Docker, donc nos exécutables seront des images Docker que nous exécuterons sur des machines virtuelles.

AWS offre un service dédié pour stocker les images appelé Elastic Container Registry. La commande suivante va en créer un pour nous :

```bash
aws ecr create-repository --repository-name react-to-aws --region us-east-2
```

Voici les paramètres :

* `ecr` - L'acronyme de "Elastic Container Registry".
* `repository-name` - Le nom de notre registre. Gardez à l'esprit que nous ferons référence à ce nom plus tard.
* `region` - Le code de la région. Vous pouvez trouver une région proche de votre emplacement pour réduire la latence. Voici une [liste de toutes les régions](https://docs.aws.amazon.com/general/latest/gr/rande.html).

Vous pouvez trouver plus de détails dans la [documentation](https://docs.aws.amazon.com/cli/latest/reference/ecr/create-repository.html).

Et voici la sortie attendue :

```file.json
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-2:1234567890:repository/react-to-aws2",
        "registryId": "1234567890",
        "repositoryName": "react-to-aws",
        "repositoryUri": "1234567890.dkr.ecr.us-east-2.amazonaws.com/react-to-aws2",
        "createdAt": "2021-03-16T22:50:23+04:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
```

### 3. Pousser les images Docker dans le cloud

Dans cette étape, nous allons pousser nos images Docker dans le cloud. Nous pouvons le faire en copiant les commandes de poussée depuis notre console AWS.

Ouvrons la _Console AWS_ dans le navigateur, et cliquons sur _Elastic Container Registry_ dans la liste "_All Services - Containers_". Si vous n'avez pas changé votre région, vous pouvez [simplement cliquer ici](https://us-east-2.console.aws.amazon.com/ecr/repositories?region=us-east-2). Vous allez voir la liste complète de vos dépôts :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-16-at-23.00.24-1.png)

Maintenant, vous devez sélectionner le dépôt `react-to-aws`, puis "_View push commands_" dans le menu (marqué avec des cercles rouges dans l'image ci-dessus). Vous allez voir la fenêtre suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-16-at-23.08.49.png)

Vous devez copier toutes les commandes de la modale dans votre terminal. **_Ne copiez pas_ les commandes du snippet ci-dessous** car cela ne fonctionnera pas.

```bash
$ aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-2.amazonaws.com
Login Succeeded

$ docker build -t react-to-aws .
[+] Building 0.6s (8/8) FINISHED
...

$ docker tag react-to-aws:latest 123465789.dkr.ecr.us-east-2.amazonaws.com/react-to-aws:latest

$ docker push 123456789.dkr.ecr.us-east-2.amazonaws.com/react-to-aws:latest
The push refers to repository [123456789.dkr.ecr.us-east-2.amazonaws.com/react-to-aws:latest]
...
latest: digest: sha256:3921262a91fd85d2fccab1d7dbe7adcff84f405a3dd9c0e510a20d744e6c3f74 size: 1988
```

Maintenant, vous pouvez fermer la modale et cliquer sur le nom du dépôt (`react-to-aws`) pour parcourir la liste des images disponibles. Vous devriez voir l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-16-at-23.17.56-1.png)

Votre application est dans le dépôt, prête pour le déploiement ! Maintenant, cliquez sur "_Copy URI_" **et gardez le contenu de votre presse-papiers** (collez-le dans un bloc-notes ou un fichier texte), car nous en aurons besoin pour l'exécuter !

### 4. Configurer l'application

Notre image est disponible dans le cloud, nous devons donc maintenant la configurer.

Les machines virtuelles ne savent pas comment exécuter votre image pour s'assurer qu'elle fonctionne bien. Nous devons définir certaines instructions telles que les ports ouverts, les variables d'environnement, etc. AWS appelle cela la définition de tâche.

Ouvrez la _Console AWS_, et cliquez sur _Elastic Container Service (ECS)_ dans la liste "_All Services - Containers_". Si vous n'avez pas changé votre région, vous pouvez [cliquer ici](https://us-east-2.console.aws.amazon.com/ecs/home?region=us-east-2#/clusters).

Maintenant, sélectionnez _Task Definitions_, et cliquez sur "_Create new Task Definition_" comme indiqué dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.07.54-1.png)

Nous avons deux options pour exécuter notre tâche : `FARGATE` et `EC2`. Choisissez `FARGATE`, et cliquez sur "_Next step_".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.09.53.png)

Dans l'étape suivante, vous devez remplir le formulaire avec les valeurs suivantes :

* **Task Definition Name** - `react-to-aws-task`.
* **Task Role** - `none`.
* **Task memory (GB)** - `0.5GB` (le plus petit).
* **Task CPU (vCPU)** - `0.25 vCPU` (le plus petit).

Une fois que vous avez atteint la section "_Container Definitions_", cliquez sur _"Add container"_ :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.18.19.png)

Remplissez le formulaire avec les valeurs suivantes :

* **Container Name** - `react-to-aws`.
* **Image** - L'URI de l'étape 4. Vous l'avez collé quelque part.
* **Memory Limits (MiB)**- `Soft limit` `128`.
* **Port mappings** - `80` - le port HTTP.

Les autres options ne sont pas pertinentes pour nous. Maintenant, cliquez sur le bouton "_Add_" pour ajouter un conteneur, et terminez la définition de la tâche en cliquant sur _Create_. Vous devriez voir l'écran suivant, et cliquez sur "_View task definition_".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.24.56.png)

### 5. Exécutons-le !

Enfin, nous pouvons créer un cluster, afin de pouvoir exécuter notre application dans le cloud. Vous devez sélectionner "_Clusters_" dans le menu de gauche, et "_Create Cluster_". Comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.29.46.png)

Maintenant, nous avons trois options : `Networking only`, `EC2 Linux + Networking`, et `EC2 Windows + Networking`. Choisissez la première - `Networking only`, et cliquez sur "_Next step_". Vous devriez voir l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.34.35.png)

Entrez le nom du cluster `react-to-aws`, et cliquez sur le bouton "_Create_". Vous devriez voir un statut de lancement réussi. Cela ressemble à l'écran que nous avons obtenu une fois notre définition de tâche créée. Maintenant, cliquez sur "_View Cluster_".

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.39.42-1.png)

Maintenant, vous devez cliquer sur l'onglet "_Tasks_", et cliquer sur "_Run new Task_". Félicitations ! Vous avez atteint le tout dernier formulaire à remplir :)

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.41.10.png)

Remplissez le formulaire avec les valeurs suivantes :

* **Launch type** - `FARGATE`.
* **Cluster VPC** - Le premier.
* **Subnet** - Le premier.

**Gardez les autres valeurs telles quelles**, et cliquez sur le bouton "_Run task_". Vous devriez voir l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.46.45-1.png)

Nous devrons attendre environ une minute jusqu'à ce que le "_Last status_" passe à RUNNING. Veuillez noter que vous devez cliquer sur le bouton "_Refresh_" pour actualiser la liste. Une fois que le statut de la tâche est en cours d'exécution, cliquez sur le nom de la tâche.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-00.50.52.png)

Dans la section "_Network_", vous trouverez l'_IP publique_ de votre conteneur. Vous pouvez l'ouvrir dans votre navigateur, et vous verrez votre application.

## Résumé

Si vous êtes au début de votre carrière, vous n'avez peut-être jamais déployé une application vous-même. Mais il est bon d'apprendre cette compétence, car un jour vous en aurez besoin.

Chaque projet doit faire face aux utilisateurs, sinon il n'aura aucune chance de réussir et ne se rentabilisera jamais.

> "Un navire dans le port est en sécurité — mais ce n'est pas pour cela que les navires sont construits."
> — John A. Shedd

Le processus de configuration est un peu fastidieux, mais la bonne nouvelle est que vous n'avez besoin de le faire qu'une seule fois.

Après avoir tout configuré, vos prochains déploiements seront plus simples. Vous n'avez besoin que de pousser la nouvelle image et de redémarrer la tâche pour déployer une nouvelle version de votre application.

Si vous êtes intéressé à approfondir AWS, FreeCodeCamp offre un [tutoriel gratuit](https://www.freecodecamp.org/news/learn-the-basics-of-amazon-web-services/) (~5 heures).

Vous pouvez trouver un **screencast de ce tutoriel (17 minutes)** sur ma chaîne **YouTube**. Je suis au tout début de mon parcours YouTube - au moins une fois par semaine, je télécharge une vidéo sur la programmation. Cela signifierait beaucoup pour moi si vous regardiez mon screencast, vous abonniez et cliquiez sur le bouton like :)

%[https://youtu.be/bUSXeQ4H20g]

**Vous pouvez trouver tout le code dans ce dépôt GitHub** : [https://github.com/mateuszsokola/react-to-aws](https://github.com/mateuszsokola/react-to-aws)

Vous pouvez m'envoyer un message direct sur Twitter : [@msokola](https://twitter.com/msokola)

C'est tout pour aujourd'hui ! J'espère que vous avez aimé et que vous passez une excellente journée :)

![Image](https://www.freecodecamp.org/news/content/images/2021/03/vidar-nordli-mathisen-xgP0GNl9Gzg-unsplash.jpg)
_Photo par [Unsplash](https://unsplash.com/@vidarnm?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Vidar Nordli-Mathisen</a> sur <a href="https://www.freecodecamp.org/news/s/photos/ship-storm?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_