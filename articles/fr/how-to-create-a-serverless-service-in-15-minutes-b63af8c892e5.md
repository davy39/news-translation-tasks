---
title: Comment créer un service serverless en 15 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T14:30:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-serverless-service-in-15-minutes-b63af8c892e5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ziV1Q7D3LwXK-7n8gLf9Pg.jpeg
tags:
- name: AWS
  slug: aws
- name: Python
  slug: python
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer un service serverless en 15 minutes
seo_desc: 'By Charlee Li

  The word “serverless” has been popular for quite a while. When Amazon released the
  AWS Lambda service in 2015, many tools emerged to help people build serverless services
  with just a few commands. Compared to traditional always-on servi...'
---

Par Charlee Li

Le mot « serverless » est populaire depuis un certain temps. Lorsque Amazon a lancé le service AWS Lambda en 2015, de nombreux outils sont apparus pour aider les gens à créer des services serverless avec seulement quelques commandes. Comparé aux services traditionnels toujours actifs, les services serverless sont très faciles à développer, déployer et maintenir. Ils sont également extrêmement rentables, surtout pour ces services simples qui n'ont pas trop de trafic.

### Qu'est-ce que le serverless ?

Comme son nom l'indique, « serverless » signifie que vous exécutez un service sans serveur. En réalité, il y a toujours un serveur qui exécute le service, mais en tant que propriétaire du service, vous n'avez pas besoin de vous soucier de ce serveur.

Par exemple, AWS Lambda vous permet de déployer une « fonction » pour traiter les requêtes. AWS dispose d'un serveur pour exécuter toutes les fonctions lorsqu'elles sont demandées. Mais vous n'avez pas besoin de vous soucier de la manière dont ce serveur fonctionne ou de la manière de faire fonctionner votre code avec ce serveur. Tout ce que vous devez savoir, c'est que vous écrivez une fonction puis la poussez vers le service Lambda.

Et le plus intéressant, c'est que c'est très bon marché. Amazon Lambda offre 1 million de requêtes gratuites et 400 000 GB-secondes de temps de calcul gratuit par mois (ce qui signifie que votre calcul peut utiliser 1 Go de mémoire pendant 400 000 secondes), ce qui est suffisant pour la plupart des petits services. Comparé à EC2, où une instance nano coûterait 0,0058 $ par heure (soit 0,14 $ par jour), Lambda est bien moins cher.

### Ce que nous allons faire ici

Dans cet article, je vais vous montrer comment créer un petit site web personnel serverless en utilisant AWS. Le site web a les caractéristiques suivantes :

* Comprend à la fois le front-end et le back-end
* Principalement statique, ou orienté front-end
* Requêtes API — celles-ci sont rares mais nécessaires
* Le back-end ne nécessite pas trop de mémoire ou de CPU (par exemple, un simple compteur web qui ne nécessite qu'un accès à la base de données)

Notre service sera déployé aux domaines suivants (j'ai utilisé des domaines fictifs dans cet article) :

* Service API : `[https://myservice-api.example.com](https://myservice-api.example.com)`
* Front End : `[https://myfrontend.example.com](https://myfrontend.example.com)`

Une solution serverless est parfaite à la fois sur le plan technique et du point de vue des coûts. Nous utiliserons les services AWS suivants :

* Lambda + API Gateway + S3, pour le serveur API
* DynamoDB, pour le stockage des données
* S3, pour l'hébergement web statique
* Cloudfront, pour le CDN distribué
* AWS Certificate Manager (ACM), pour générer des certificats pour notre site web https

![Image](https://cdn-media-1.freecodecamp.org/images/0uoj5U2PThzVHxYqiy1py0lyP0Qf6hx1Bpxd)

Pour le serveur API, nous utiliserons une combinaison Python + Flask, et Zappa comme boîte à outils serverless.

### Configuration de l'environnement AWS

Tout d'abord, nous devons configurer l'environnement AWS afin de pouvoir accéder à AWS depuis notre code et [zappa](https://github.com/Miserlou/Zappa). Cela se fait en deux étapes :

1. Nous devons créer un utilisateur AWS pour l'accès programmatique
2. Nous devons configurer un environnement AWS local pour utiliser cet utilisateur

#### Créer un utilisateur AWS

Connectez-vous à AWS, et choisissez le service « IAM » pour gérer les identifiants des utilisateurs.

Créez un utilisateur appelé « myservice-admin » (ou tout autre nom d'utilisateur que vous souhaitez utiliser), et n'oubliez pas de cocher l'option « **Accès programmatique** ».

![Image](https://cdn-media-1.freecodecamp.org/images/RJm34WWNBf21zqZXF7y2tcuxoHEJi-Km5Ked)

Dans l'écran suivant, cliquez sur le bouton « **Attacher directement les politiques existantes** », puis ajoutez « **AdministratorAccess** » à l'utilisateur.

> Remarque : D'un point de vue sécurité, ce n'est pas la meilleure pratique. Mais à des fins de démonstration, cet article ne couvrira pas les détails de la réduction des permissions.

![Image](https://cdn-media-1.freecodecamp.org/images/RL5qTOE2WERtOcGa5-Do8XBRpDeK8dGC3S-J)

Cliquez sur le bouton « suivant » puis sur le bouton « Créer un utilisateur », et l'utilisateur `myservice-admin` sera créé. Dans le dernier écran, l'**ID de la clé d'accès** et la **clé d'accès secrète** sont affichés. Assurez-vous de les copier et de les coller dans un fichier local. Ce sont les identifiants API que nous allons utiliser dans l'étape suivante.

> Remarque : **C'est le seul endroit où vous pouvez voir les clés d'accès secrètes** ! Si vous ne parvenez pas à en faire une copie, vous devez aller à l'écran de détail de l'utilisateur et générer une nouvelle paire de clés d'accès et de clés secrètes.

#### Configurer votre environnement AWS local

Nous devons créer un environnement local afin d'utiliser AWS localement.

Tout d'abord, installons l'outil `awscli`, qui nous aidera à configurer l'environnement :

```
$ sudo apt install awscli
```

Après l'installation, nous configurerons AWS en utilisant la commande `aws configure` :

```
$ aws configureAWS Access Key ID [None]: ******AWS Secret Access Key [None]: ******Default region name [None]: us-east-1Default output format [None]: json
```

Ici, nous devons taper l'**ID de la clé d'accès** et la **clé d'accès secrète** que nous avons reçus de l'étape précédente. En ce qui concerne la région par défaut, j'ai utilisé `us-east-1`. Vous pouvez choisir n'importe quelle région que vous souhaitez, mais d'autres régions peuvent causer quelques problèmes lors de la configuration de CloudFront.

### Créer une table dans DynamoDB

Afin de stocker la valeur du compteur de visiteurs du site web dans DynamoDB, nous avons besoin d'un stockage persistant. Nous devons donc créer une table et y insérer une valeur initiale.

Dans la console AWS, choisissez le service DynamoDB. Ensuite, cliquez sur le bouton « **Créer une table** ». Dans l'écran « Créer une table DynamoDB », remplissez le **Nom de la table** avec `myservice-dev` et le champ **Clé primaire** avec `id`, puis cliquez sur le bouton **Créer une table**.

![Image](https://cdn-media-1.freecodecamp.org/images/M3vIGIoT73EbIWi3FaUexw-6k-OXH1BQ5h6I)

Après quelques secondes, la table devrait être créée. Sélectionnez la table nouvellement créée, choisissez l'onglet **Éléments** dans le volet de droite, puis cliquez sur le bouton **Créer un élément**, et créez un élément avec `id='counter'` et `counter_value=0`.

> Remarque : Vous devez cliquer sur le signe plus sur le côté gauche pour ajouter l'attribut `_counter_value_`, et n'oubliez pas de définir le type de `_counter_value_` sur **Nombre**.

![Image](https://cdn-media-1.freecodecamp.org/images/S7qDIn8je7Zlbm9WONmR9LYTRsewyymMmNWr)

### Créer un service API

Ensuite, nous allons créer le service API. À des fins de démonstration, ce service API fournira une API de compteur qui augmentera une valeur de compteur lorsqu'elle sera cliquée. La valeur du compteur sera stockée dans DynamoDB. Les points de terminaison de l'API sont :

* `POST /counter/increase` augmente le compteur et retourne la valeur du compteur
* `GET /counter` retourne la valeur actuelle du compteur

#### Coder le service API avec Python et Flask

Nous allons commencer par créer un environnement virtuel Python et installer les packages nécessaires :

```
$ mkdir myservice && cd myservice$ python3 -m venv .env$ source .env/bin/activate(.env)$ pip install flask boto3 simplejson
```

`flask` est le framework web et le package `boto3` est requis pour accéder à DynamoDB. `simplejson` peut nous aider à gérer certains problèmes de conversion JSON. Créons le service en créant un fichier `myservice.py` avec le contenu suivant :

```
import boto3from flask import Flask, jsonify
```

```
app = Flask(__name__)
```

```
# Initialiser l'accès à dynamodbdynamodb = boto3.resource('dynamodb')db = dynamodb.Table('myservice-dev')
```

```
@app.route('/counter', methods=['GET'])def counter_get():  res = db.get_item(Key={'id': 'counter'})  return jsonify({'counter': res['Item']['counter_value']})
```

```
@app.route('/counter/increase', methods=['POST'])def counter_increase():  res = db.get_item(Key={'id': 'counter'})  value = res['Item']['counter_value'] + 1  res = db.update_item(    Key={'id': 'counter'},    UpdateExpression='set counter_value=:value',    ExpressionAttributeValues={':value': value},  )  return jsonify({'counter': value})
```

Créez un fichier `run.py` pour tester ce service API localement :

```
from myservice import appif __name__ == '__main__':  app.run(debug=True, host='127.0.0.1', port=8000)
```

Maintenant, exécutez le service :

```
(.env)$ python run.py
```

Et nous pouvons tester ce service avec les commandes suivantes (ouvrez un autre terminal pour taper ces commandes) :

```
$ curl localhost:8000/counter{  "counter": 0}$ curl -X POST localhost:8000/counter/increase{  "counter": 1}$ curl -X POST localhost:8000/counter/increase{  "counter": 2}$ curl localhost:8000/counter{  "counter": 2}
```

Nous pouvons voir que notre code fonctionne et qu'il augmente avec succès le compteur !

#### Déployer notre code sur Lambda avec Zappa

Déployer notre API sur Lambda est extrêmement facile avec zappa. Tout d'abord, nous devons installer zappa :

```
(.env)$ pip install zappa
```

Ensuite, initialisez l'environnement zappa avec `zappa init`. Il vous posera quelques questions, mais généralement vous pouvez utiliser les réponses par défaut pour toutes les questions :

```
(.env)$ zappa init...What do you want to call this environment (default 'dev'): ...What do you want to call your bucket? (default 'zappa-ab7dd70x5'):
```

```
It looks like this is a Flask application.What's the modular path to your app's function?This will likely be something like 'your_module.app'.We discovered: myservice.appWhere is your app's function? (default 'myservice.app'): ...
```

```
Would you like to deploy this application globally? (default 'n') [y/n/(p)rimary]:
```

```
Okay, here's your zappa_settings.json:
```

```
{    "dev": {        "app_function": "myservice.app",        "aws_region": "us-east-1",        "profile_name": "default",        "project_name": "myservice",        "runtime": "python3.6",        "s3_bucket": "zappa-ab7dd70x5"    }}
```

```
Does this look okay? (default 'y') [y/n]: ...
```

Après l'initialisation, nous pouvons voir le fichier `zappa_settings.json` généré. Ensuite, nous pouvons commencer à déployer notre service :

```
(.env)$ zappa deploy devCalling deploy for stage dev.....Deployment complete!: https://2ks1n5nrxh.execute-api.us-east-1.amazonaws.com/dev
```

Super ! Notre service est en ligne. Vous pouvez tester ce service avec curl également :

```
(.env)$ curl https://2ks1n5nrxh.execute-api.us-east-1.amazonaws.com/dev/counter{"counter":2}(.env)$ curl -X POST https://2ks1n5nrxh.execute-api.us-east-1.amazonaws.com/dev/counter/increase{"counter":3}(.env)$ curl https://2ks1n5nrxh.execute-api.us-east-1.amazonaws.com/dev/counter{"counter":3}
```

### Configurer un domaine personnalisé pour le service API

Cependant, il y a un problème avec le service API. Le point de terminaison API généré automatiquement `2ks1n5nrxh.execute-api.us-east-1.amazonaws.com` est très difficile à lire ou à utiliser pour une consommation humaine. Heureusement, nous pouvons lier un nom de domaine personnalisé à ce point de terminaison API.

Nous utiliserons le domaine personnalisé `https://myservice-api.example.com` pour ce service API. Puisque nous voulons le servir avec https, nous devons d'abord obtenir un certificat. AWS fournit un certificat gratuit avec le service « Certificate Manager », et il est très facile à utiliser.

Après la génération du certificat, nous pouvons l'utiliser pour configurer un domaine personnalisé pour notre service dans le service AWS API Gateway.

#### Demander un certificat

Passez au service ACM dans la console de gestion AWS (le service s'appelle en réalité Certificate Manager, mais vous pouvez taper « ACM » pour le rechercher). Cliquez sur le bouton **Demander un certificat**, puis choisissez l'option **Demander un certificat public** dans l'écran suivant. Le certificat est gratuit tant que vous choisissez un certificat public ici.

Dans l'écran suivant, entrez le nom de domaine pour lequel vous souhaitez demander le certificat, puis cliquez sur **Suivant**. Ici, j'ai demandé pour `*.example.com` ce qui signifie que le certificat peut être utilisé par tous les sous-domaines sous `example.com`. De cette manière, nous pouvons utiliser le même certificat pour notre front-end à `myfrontend.example.com` sans avoir à demander un nouveau.

![Image](https://cdn-media-1.freecodecamp.org/images/ZaiecxZNM6qLZ0qSrsyUqICIgeayzFQmJsec)

À l'étape suivante, nous devons prouver que nous possédons ce nom de domaine. Puisque j'ai demandé ce nom de domaine depuis Google Domains, je vais choisir **Validation DNS**. Cliquez sur le bouton **Examiner** puis sur **Confirmer et demander**.

La demande de certificat sera créée, et un écran de validation sera affiché. Les instructions montrent comment valider ce nom de domaine :

![Image](https://cdn-media-1.freecodecamp.org/images/K-R1B8uuia0qoYkG5ICokjgNksKt7kspld7Z)

Selon les instructions, nous devons ajouter un enregistrement `CNAME` et lui assigner la valeur donnée. Dans mon cas, je vais ouvrir Google Domains, trouver mon nom de domaine `example.com`, et ajouter l'enregistrement CNAME spécifié :

![Image](https://cdn-media-1.freecodecamp.org/images/7o2btPUTtH4wENbsBtPpemo9lTsAF6qjKiwm)

Remarque : J'ai seulement ajouté la chaîne aléatoire `_2adee19a0967c7dd5014b81110387d11` dans le champ Nom, sans taper la partie `.example.com`. Cela est pour éviter que le suffixe `.example.com` ne soit dupliqué.

Maintenant, nous devons attendre environ 10 minutes jusqu'à ce que AWS Certificate Manager valide ce nom de domaine. Une fois validé, la colonne « Statut » dans le certificat affichera « Émis » en vert.

![Image](https://cdn-media-1.freecodecamp.org/images/POueIJUYfB1Fvk9GzQDvgcFq0OBwesN9Mqjp)

Maintenant que nous avons le certificat prêt, nous pouvons commencer à lier notre nom de domaine personnalisé à notre API.

#### Configurer un domaine personnalisé pour notre service API

Allez dans le service « API Gateway ». Dans « APIs » dans le volet de gauche, nous pouvons voir que notre API `myservice-dev` a déjà été créée par zappa.

Cliquez sur « **Noms de domaine personnalisés** » dans le volet de gauche, puis cliquez sur le bouton **Créer un nom de domaine personnalisé** dans le volet de droite et remplissez les champs nécessaires.

![Image](https://cdn-media-1.freecodecamp.org/images/giptTgSYnBgKzDQk4wR2qQPKuY4chrJQoLzI)

Ici, je veux que mon service API soit exposé via CloudFront afin qu'il puisse être accessible avec une vitesse optimale dans le monde entier. J'ai donc choisi **Optimisé pour les bords** dans cette configuration. Vous pouvez choisir **Régional** si vous n'avez pas besoin de CloudFront.

Cliquez sur le lien « **Ajouter un mappage** » ci-dessous, puis sélectionnez notre API `myservice-dev` comme **Destination**, et choisissez **dev** pour la boîte la plus à droite. De cette manière, notre API n'exposera pas le nom de l'environnement `dev` dans l'URL. Laissez le champ **Chemin** vide.

![Image](https://cdn-media-1.freecodecamp.org/images/5unYz3372TkXLMvB1iRaCcVRmp33yXi1FVc-)

Après avoir cliqué sur le bouton **Enregistrer**, notre liaison de domaine personnalisé sera créée. La liaison de domaine réelle nécessite jusqu'à 40 minutes pour s'initialiser, mais nous pouvons configurer les paramètres DNS maintenant.

D'après la capture d'écran ci-dessus, nous pouvons voir que le nom de domaine réel est `dgt9opldriaup.cloudfront.net`. Nous devons configurer un `CNAME` dans notre DNS, pointant `myservice-api.example.com` vers le sous-domaine CloudFront `dgt9opldriaup.cloudfront.net`.

Allez dans Google Domains et ajoutez le CNAME aux paramètres DNS :

![Image](https://cdn-media-1.freecodecamp.org/images/oJ4YPm9XmMEhOMNaVowdRJbqFTrMb-7uPwq2)

Après cette étape, attendez environ 40 minutes jusqu'à ce que le « Initialisation... » dans le service API Gateway disparaisse.

Maintenant, essayez notre nouveau service API !

```
(.env)$ curl https://myservice-api.example.com/counter{"counter":3}(.env)$ curl -X POST https://myservice-api.example.com/counter/increase{"counter":4}(.env)$ curl https://myservice-api.example.com/counter{"counter":4}
```

### Site web statique pour le front-end

Pour la prochaine tâche, nous allons créer un front-end pour notre tout nouveau service API. À des fins de démonstration, nous allons créer une page simple avec un bouton qui déclenche l'appel API `/counter/increase`.

#### Coder le front-end

Créons un nouveau répertoire appelé `myfrontend` :

```
$ mkdir myfrontend && cd myfrontend
```

Ensuite, créez un simple fichier HTML `index.html` :

```
<html><body>  <h1>Bienvenue sur ma page d'accueil !</h1>  <p>Compteur : <span id="counter"></span></p>  <button id="increase">Augmenter le compteur</button>  <script>    const setCounter = (counter_value) => {      document.querySelector('#counter').innerHTML = counter_value;    };
```

```
    const api = 'https://myservice-api.example.com';    fetch(api + '/counter')      .then(res => res.json())      .then(result => setCounter(result.counter));
```

```
document.querySelector('#increase')      .addEventListener('click', () => {        fetch(api + '/counter/increase', { method: 'POST' })          .then(res => res.json())          .then(result => setCounter(result.counter));        }      );  </script></body></html>
```

#### Publier le front-end sur AWS S3

Pour créer un site web statique avec S3, nous devons créer un bucket avec le même nom que notre nom de domaine.

> Remarque : Si vous avez suivi ce tutoriel, le nom de bucket myfrontend.example.com peut ne pas être disponible, car les noms de bucket sont globalement uniques. De plus, vous devrez créer un nom de bucket basé sur votre domaine public. Par exemple, `_myfrontend.**[votredomaine]**.com_`

Passez au service S3 dans la console de gestion AWS. Puisque nous voulons héberger le site web statique sur `myfrontend.example.com`, nous allons créer un bucket avec ce nom. Cliquez sur le bouton **Créer un bucket**, et remplissez le nom du bucket, puis continuez à cliquer sur **Suivant** jusqu'à ce que le bucket soit créé.

![Image](https://cdn-media-1.freecodecamp.org/images/EjYD-VGI7VJmRnVIEmsr4Bzn5E-It5YQgFAx)

Ensuite, nous devons activer l'hébergement web statique à partir de ce bucket. Ouvrez ce bucket, puis choisissez l'onglet **Propriétés**, et choisissez **Hébergement web statique**. Dans la boîte de dialogue, sélectionnez **Utiliser ce bucket pour héberger un site web**, puis tapez `index.html` dans le champ « Document d'index ». Cliquez sur **Enregistrer** lorsque vous avez terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/POZJE4JrDzqtmXYYTmtW838Vw3Dku56h5iV-)

> Remarque : Le lien « Point de terminaison » affiché dans la boîte de dialogue ci-dessus. Nous testerons notre site web statique avec cette URL plus tard.

La dernière chose que nous devons faire est d'activer l'accès public sur le bucket. Cela peut être fait en ajoutant une politique de bucket. Ouvrez ce bucket et choisissez l'onglet **Autorisations**, puis cliquez sur le bouton **Politique de bucket**.

Tapez le contenu suivant comme politique, puis cliquez sur le bouton **Enregistrer** (n'oubliez pas de remplacer `myservice.example.com` par votre nom de domaine).

```
{    "Version": "2012-10-17",    "Statement": [        {            "Sid": "PublicReadGetObject",            "Effect": "Allow",            "Principal": "*",            "Action": "s3:GetObject",            "Resource": "arn:aws:s3:::myfrontend.example.com/*"        }    ]}
```

Après avoir enregistré, nous devrions pouvoir voir un signe orange « public » sur le bouton **Politique de bucket** et l'onglet **Autorisations**, ce qui indique que notre bucket est accessible au public.

Maintenant, le bucket est créé mais il est encore vide. Nous devons télécharger nos fichiers de code front-end dans ce bucket. Assurez-vous que nous sommes dans le répertoire nouvellement créé `myfrontend` et tapez la commande suivante :

```
# Assurez-vous d'être dans le répertoire `myfrontend`...
$ aws s3 sync . s3://myfrontend.example.com
```

La commande ci-dessus copie tous les fichiers du répertoire courant `.` vers S3.

Tout est fait ! Maintenant, nous pouvons tester ce site web statique avec l'URL affichée précédemment. Ouvrez cette URL avec n'importe quel navigateur (dans mon cas, [http://myfrontend.example.com.s3-website-us-east-1.amazonaws.com/)](http://myfrontend.example.com.s3-website-us-east-1.amazonaws.com/).) et voyez le résultat !

Oups ! Le compteur n'est pas affiché du tout. ?

![Image](https://cdn-media-1.freecodecamp.org/images/8HmkoqeY791wEFxKusCRKQRF6mS7ThvFBfLM)

Et il semble que nous ayons une erreur JavaScript. Nous pouvons voir l'erreur suivante dans la console :

```
Échec du chargement de https://myservice-api.example.com/counter : Aucun en-tête 'Access-Control-Allow-Origin' n'est présent sur la ressource demandée. L'origine 'http://myfrontend.example.com.s3-website-us-east-1.amazonaws.com' n'est donc pas autorisée à accéder. Si une réponse opaque répond à vos besoins, définissez le mode de la requête sur 'no-cors' pour récupérer la ressource avec CORS désactivé.
```

Apparemment, nous devons définir l'en-tête [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) afin de faire fonctionner ce script, puisque l'API backend est située sur un autre domaine. Mais puisque nous allons configurer un domaine personnalisé pour le frontend, l'URL va changer, donc nous nous occuperons de CORS plus tard.

#### Configurer CloudFront pour notre site web statique

La dernière étape consiste à configurer CloudFront pour notre front-end. Puisque nous avons déjà créé un certificat pour `*.example.com`, cette étape sera très facile.

Passez au service CloudFront dans la console de gestion AWS. Cliquez sur le bouton **Créer une distribution**, puis cliquez sur le bouton **Démarrer** dans la section « Web ».

Dans l'écran « Créer une distribution », nous devons apporter cinq modifications :

* Cliquez sur la zone de saisie **Nom de domaine d'origine** et sélectionnez notre bucket S3 `myfrontend.example.com.s3.amazonaws.com`.
* Ensuite, changez la **Stratégie de protocole du spectateur** en « Rediriger HTTP vers HTTPS » afin de forcer l'accès https.
* Dans la zone **Noms de domaine alternatifs**, tapez notre domaine personnalisé. Dans ce cas, nous tapons `myfrontend.example.com`.
* Faites défiler jusqu'à la section **Certificat SSL**, choisissez « Certificat SSL personnalisé », puis sélectionnez notre certificat `*.example.com`.
* Changez **Objet racine par défaut** en `index.html`.

Après la création de la distribution, nous pouvons voir le domaine CloudFront dans la liste des distributions.

![Image](https://cdn-media-1.freecodecamp.org/images/XVHiWsgZ5DzvulZNLv7qZ74dbaltssSU0Od2)

Bien que le statut soit encore « En cours », nous pouvons configurer notre enregistrement DNS maintenant. Allez dans Google Domains et ajoutez un CNAME pour ce domaine :

![Image](https://cdn-media-1.freecodecamp.org/images/IDE1BaGVdZi4v9-yjNyB9JaikGf1un-uylHq)

Ensuite, attendez que le statut de la distribution passe à « Déployé ». Maintenant, ouvrez votre navigateur et essayez d'accéder à `myfrontend.example.com`. Nous pouvons voir le même site web statique !

### Résoudre le problème CORS

Maintenant, le seul problème restant est CORS. Puisque nous utilisons un nom de domaine différent pour le backend et le frontend, nous devons ajouter la prise en charge de CORS.

> Le partage des ressources cross-origin (CORS) est un mécanisme qui permet de demander des ressources restreintes (par exemple, des polices) sur une page web à partir d'un autre domaine en dehors du domaine à partir duquel la première ressource a été servie. — [Wikipedia](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)

Retournez dans notre répertoire API (`myservice`) et activez l'environnement Python. Ensuite, installez le package `flask_cors`.

```
$ cd myservice$ source .env/bin/activate(.env)$ pip install flask_cors
```

Ensuite, éditez `myservice.py` et ajoutez les lignes suivantes (en gras) :

```
import boto3from flask import Flask, jsonifyfrom flask_cors import CORS
```

```
app = Flask(__name__)CORS(app, origins=['https://myfrontend.example.com'])
```

Poussez le service mis à jour vers AWS Lambda :

```
(.env)$ zappa update dev
```

Maintenant, essayez de rafraîchir notre navigateur. Nous pouvons voir que le compteur est affiché correctement. Cliquer sur le bouton « Augmenter le compteur » peut également augmenter le compteur.

![Image](https://cdn-media-1.freecodecamp.org/images/50exWZDflbAEedy9W3Rjzd7h8oGxKLKuGmb8)

### Conclusion

Dans cet article, nous avons exploré divers services AWS nécessaires pour créer un service serverless simple. Vous pouvez penser qu'il y a trop de services AWS si vous n'êtes pas familier avec AWS, mais la plupart des services AWS que nous avons utilisés ici sont pour une utilisation ponctuelle. Une fois qu'ils sont configurés, nous n'avons pas besoin de les toucher du tout dans le développement ultérieur. Tout ce que vous avez à faire est d'exécuter `zappa update` et `aws s3 sync`.

De plus, cela est bien plus facile que de configurer un VPS privé, d'installer des serveurs web et d'écrire un travail Jenkins pour le déploiement continu.

En résumé, voici les points clés à retenir de cet article :

* Lambda peut exécuter un service simple. Ce service peut être exposé par API Gateway.
* zappa est un excellent outil si vous souhaitez écrire des services serverless en Python.
* Un bucket S3 peut être utilisé pour l'hébergement statique.
* Demandez un certificat auprès d'AWS ACM si vous souhaitez utiliser https.
* API Gateway et CloudFront prennent tous deux en charge les noms de domaine personnalisés.

J'espère que vous avez aimé cet article et n'hésitez pas à applaudir ? pour moi si c'est le cas ! Suivez-moi si vous voulez lire plus d'articles sur le développement web.