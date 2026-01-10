---
title: Comment j'ai construit mon propre outil de prévision en utilisant une API météo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-11T17:50:21.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-my-own-forecasting-tool-using-a-weather-api
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b25740569d1a4ca29f2.jpg
tags:
- name: api
  slug: api
- name: forecasting
  slug: forecasting
- name: weather
  slug: weather
seo_title: Comment j'ai construit mon propre outil de prévision en utilisant une API
  météo
seo_desc: "By Anton Lawrence\nAbrupt weather and climate change are things that everybody\
  \ is dealing with. In fact, the vast majority of the global population relies on\
  \ accurate, real-time weather data and forecasts to make informed decisions.   \n\
  This has increa..."
---

Par Anton Lawrence

Les changements climatiques et les conditions météorologiques imprévisibles sont des défis auxquels tout le monde est confronté. En fait, la grande majorité de la population mondiale dépend de données météorologiques précises et en temps réel pour prendre des décisions éclairées.

Cela a accru l'importance des applications météo fiables pour Android et iOS. Dans cet article, nous allons vous montrer comment créer un outil de prévision simple en utilisant NodeJS et une API météo.

Mais avant cela, passons en revue l'importance des applications météo.

# Pourquoi avons-nous besoin d'applications météo ?

Une application de prévision météo riche en fonctionnalités peut offrir une grande valeur à divers secteurs. Voici quelques avantages notables des applications météo :

* Fournir un accès immédiat aux conditions météorologiques locales et aux prévisions à venir, ce qui vous fait gagner du temps.
* Fournir des notifications en temps réel sur les conditions météorologiques actuelles et prévues.
* Aider les gouvernements et les administrations locales à se préparer aux catastrophes naturelles et à sauver des vies.
* Aider les agriculteurs à prendre des mesures préventives.
* Faciliter l'industrie mondiale du voyage et du tourisme.
* Fournir des prévisions météorologiques claires, cruciales dans les industries de l'aviation et de la logistique.

# Ce dont vous avez besoin pour construire une application météo

Voici quelques-unes des choses dont vous aurez besoin pour construire une application météo avec succès :

* Une bonne connaissance de JavaScript (Node.js)
* Un éditeur de texte tel que Notepad ou un IDE. Mon préféré est Visual Studio.
* Un accès à une API météo fiable comme ClimaCell
* Un accès à un service de cartes
* Des connaissances en HTML, CSS et Bootstrap

Une fois que vous avez tout cela prêt, vous êtes prêt à commencer.

# Présentation de l'API météo ClimaCell

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589167731846_climacell+api+weather.jpg)

ClimaCell est un fournisseur de données météorologiques populaire qui offre des données météorologiques historiques hyper-précises ainsi que des prévisions via une API facile à utiliser.

# Le processus de construction

Dans cette section, je vais vous montrer comment j'ai créé une application de prévision où un utilisateur entre sa ville ou tout autre lieu par nom et récupère les données météorologiques de l'API ClimaCell. L'API répond à la demande en retournant des données, qui sont ensuite affichées à l'utilisateur.

## Installer NodeJS et créer un nouveau projet

Pour ce projet, nous allons utiliser Node.js — l'un des environnements d'exécution les plus populaires pour JavaScript. Node.js aide les développeurs à créer rapidement des applications web. Il dispose d'une large gamme de bibliothèques et de modules pour créer des applications web avancées.

Si vous n'avez pas Node.js sur votre appareil, vous pouvez l'installer depuis le [site officiel](https://nodejs.org/en/).
Une fois installé, nous utilisons cette commande pour initialiser npm - le gestionnaire de paquets par défaut utilisé par Node.js.

`$ npm init`

Cela crée notre projet, vous serez donc invité à entrer quelques détails tels que le nom du paquet, la description, le dépôt Git, etc.

Ensuite, nous installons les modules nécessaires pour exécuter notre projet. Pour générer un squelette d'application Node.js, nous utilisons express - un framework pour construire des applications web Node.js.

`$ npm install express`

L'installation du framework express vous aide à exécuter le serveur, gérer les requêtes des clients et connecter le bon modèle HTML avec une réponse.

Ensuite, nous allons également installer unirest - une solution simple mais puissante qui vous permet de demander une bibliothèque.

Cela nous aidera à faire des requêtes à l'API ClimaCell et à gérer les réponses.

Utilisez cette commande :

`npm install unirest`

À ce stade, nous avons installé les modules nécessaires et le projet est prêt.
Ensuite, nous générons une application météo en utilisant l'outil de générateur express. Sur la ligne de commande, tapez ceci :

`express --view=pug weather-app-nodejs`

Vous devriez maintenant avoir une vue comme celle-ci sur la ligne de commande :

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589167675672_create+weather+app.png)

## Obtenir l'API météo ClimaCell

Pour accéder à l'API ClimaCell, vous devrez vous inscrire pour un compte sur leur page.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589187768233_CLIMACELL+DASHBOARD.png)

Une fois que vous avez créé un compte, connectez-vous à leur tableau de bord de l'API Microweather qui ressemble à ceci :

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589188690033_dashboard.png)

Sur le tableau de bord, cliquez sur les références pour vérifier les points de terminaison de l'API. Comme vous pouvez le voir, l'API ClimaCell dispose de plusieurs points de terminaison, y compris les prévisions à court terme, les prévisions horaires, les données en temps réel, et plus encore.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589191651855_API+endpoints.png)

Il est à noter que chaque point de terminaison a son propre extrait de code. Par exemple, voici l'extrait de code Node.js pour obtenir des données météorologiques en temps réel.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589192780403_carbon.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=router.post(%27%252Fweather%27%252C%2520function(req%252C%2520res%252C%2520next)%257B%250A%250A%2520%2520let%2520city%2520%253D%2520req.body.city%253B%250A%250A%2520%2520url%2520%253D%2520url%252Bcity%252B%2522%2526%2522%252BappId%253B%250A%250A%2520request(url%252C%2520function%2520(error%252C%2520response%252C%2520body)%2520%257B%250A%250A%2520%2520%2520%2520%2520%2520body%2520%253D%2520JSON.parse(body)%253B%250A%250A%2520%2520%2520%2520%2520%2520if(error%2520%2526%2526%2520response.statusCode%2520!%253D%2520200)%257B%250A%250A%2520%2520%2520%2520%2520%2520%2520%2520throw%2520error%253B%250A%250A%2520%2520%2520%2520%2520%2520%257D%250A%250A%2520%2520%2520%2520let%2520country%2520%253D%2520(body.sys.country)%2520%253F%2520body.sys.country%2520%253A%2520%27%27%2520%253B%250A%250A%2520%2520%2520%2520let%2520var%2520request%2520%253D%2520require(%2522request%2522)%253B%250A%250Avar%2520options%2520%253D%2520%257B%250A%2520%2520method%253A%2520%27GET%27%252C%250A%2520%2520url%253A%2520%27https%253A%252F%252Fapi.climacell.co%252Fv3%252Fweather%252Frealtime%27%252C%250A%2520%2520qs%253A%2520%257Bapikey%253A%2520%279efRx8KrGKa6ME0ORWIJz7TaNjuRQAvb%27%257D%250A%257D%253B%250A%250Arequest(options%252C%2520function%2520(error%252C%2520response%252C%2520body)%2520%257B%250A%2520%2520if%2520(error)%2520throw%2520new%2520Error(error)%253B%250A%250A%2520%2520console.log(body)%253B%250A%257D)%253B%2520%253D%2520%2522For%2520city%2520%2522%252Bcity%252B%27%252C%2520country%2520%27%252Bcountry%253B%250A%250A%2520%2520%2520%2520res.render(%27index%27%252C%2520%257Bbody%2520%253A%2520body%252C%2520forecast%253A%2520forecast%257D)%253B%250A%250A%2520%2520%2520%257D)%253B%250A%250A%257D)%253B" rel="noreferrer nofollow noopener)_

## Modifier l'application

Pour appeler l'API ClimaCell, nous devons d'abord éditer certains fichiers. Ici, vous pouvez utiliser Notepad ou ouvrir le répertoire du projet dans votre IDE pour une édition plus facile. Il devrait apparaître comme suit :

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589180215929_repo.png)

Nous commençons à modifier nos fichiers en ajoutant bootstrap à layout.pug. Ouvrez le répertoire des vues et insérez cet extrait dans le fichier.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589170180082_carbon+1.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=doctype%2520html%250Ahtml(lang%253D%2522en%2522)%250A%2520%2520head%250A%2520%2520%2520%2520title%2520Weather%2520Forecast%2520Tool%2520using%2520Climacell%2520API%250A%2520%2520%2520%2520meta(charset%253D%2522utf-8%2522)%250A%2520%2520%2520%2520meta(name%253D%2522viewport%2522%2520content%253D%2522width%253Ddevice-width%252C%2520initial-scale%253D1%2522)%250A%2520%2520%2520%2520link(rel%253D%2522stylesheet%2522%2520href%253D%2522https%253A%252F%252Fmaxcdn.bootstrapcdn.com%252Fbootstrap%252F3.3.7%252Fcss%252Fbootstrap.min.css%2522)%250A%2520%2520%2520%2520script(src%253D%2522https%253A%252F%252Fajax.googleapis.com%252Fajax%252Flibs%252Fjquery%252F3.3.1%252Fjquery.min.js%2522)%250A%2520%2520%2520%2520script(src%253D%2522https%253A%252F%252Fmaxcdn.bootstrapcdn.com%252Fbootstrap%252F3.3.7%252Fjs%252Fbootstrap.min.js%2522)%250A%2520%2520body%250A%2520%2520%2520%2520block%2520content" rel="noreferrer nofollow noopener)_

Ensuite, nous créons un formulaire en ajoutant l'extrait suivant au fichier index.pug.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589170264156_carbon.png)

Remarquez comment nous utilisons la [méthode HTTP post](https://en.wikipedia.org/wiki/POST_(HTTP)) pour envoyer des données au serveur. Le code ci-dessus définit également le paramètre d'action sur la route météo et ajoute l'entrée de texte en tant que « ville ».

Un bouton d'entrée pour récupérer la météo est également ajouté.

Nous créons maintenant un tableau HTML juste en dessous du formulaire pour afficher les enregistrements météo récupérés.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589171285500_carbon+2.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=htmlmixed&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=.row%250A%2520%2520%2520%2520%2520%2520%2520.col-md-12%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520p%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520br%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520br%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520strong%2520Weather%2520Forecast%2520%2523%257Bforecast%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520table.table%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520thead%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520tr%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520th%2520Longitude%2520%252F%2520Latitude%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520th%2520Pressure%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520th%2520Temprature%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520th%2520Humidty%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520tbody%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520if%2520body%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520tr%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2523%257Bbody.coord.lon%257D%2520%252F%2520%2523%257Bbody.coord.lon%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2523%257Bbody.main.pressure%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2523%257Bbody.main.temp%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2523%257Bbody.main.humidity%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520else%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520tr%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520td(colspan%253D%25226%2522)%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%257C%2520Enter%2520city%2520name%2520and%2520click%2520Fetch%2520Weather%2520button" rel="noreferrer nofollow noopener)_

L'insertion de l'extrait de code ci-dessus crée un tableau qui ressemble à ceci :

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589196907929_Weather+1.png)

## Appeler l'API ClimaCell

Pour envoyer des requêtes à l'API ClimaCell, nous devons installer le [module de requête](https://nodejs.dev/making-http-requests-with-nodejs).

`npm i request --save`

Ensuite, nous ajoutons les informations d'identification de l'API ClimaCell dans le fichier index.js. Ouvrez le fichier dans votre répertoire de routes et ajoutez la clé API que vous avez obtenue sur le tableau de bord ClimaCell :

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589171891228_example+key.png)

Voici le code pour ajouter les informations d'identification de l'API :

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589172288863_carbon+4.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=let%2520url%2520%2520%2520%2520%253D%2520%27https%253A%252F%252Fclimacell-microweather-v1.p.rapidapi.com%252Fweather%252Frealtime%27%250Alet%2520appId%2520%2520%253D%2520%27appid%253DYOUR%2520API%2520KEY%27%253B%250Alet%2520units%2520%2520%253D%2520%27%2526units%253Dmetric%27%253B%2520%250Avar%2520request%2520%253D%2520require(%27request%27)%253B" rel="noreferrer nofollow noopener)_

Après avoir ajouté les informations d'identification de l'API, nous mettons à jour la route de l'index. Cela se fait en remplaçant la section de code dans la route **'/'** dans le fichier index.js.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589172437273_carbon+5.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=%252F*%2520GET%2520home%2520page.%2520*%252F%250Arouter.get(%27%252F%27%252C%2520function(req%252C%2520res%252C%2520next)%2520%257B%250A%2520res.render(%27index%27%252C%2520%257B%27body%27%253A%27%27%252C%2520forecast%253A%2520%27%27%257D)%253B%250A%257D)%253B" rel="noreferrer nofollow noopener)_

Nous terminons en créant la route météo dans index.js.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589172832852_carbon+6.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=router.post(%27%252Fweather%27%252C%2520function(req%252C%2520res%252C%2520next)%257B%250A%250A%2520%2520let%2520city%2520%253D%2520req.body.city%253B%250A%250A%2520%2520url%2520%253D%2520url%252Bcity%252B%2522%2526%2522%252BappId%253B%250A%250A%2520request(url%252C%2520function%2520(error%252C%2520response%252C%2520body)%2520%257B%250A%250A%2520%2520%2520%2520%2520%2520body%2520%253D%2520JSON.parse(body)%253B%250A%250A%2520%2520%2520%2520%2520%2520if(error%2520%2526%2526%2520response.statusCode%2520!%253D%2520200)%257B%250A%250A%2520%2520%2520%2520%2520%2520%2520%2520throw%2520error%253B%250A%250A%2520%2520%2520%2520%2520%2520%257D%250A%250A%2520%2520%2520%2520let%2520country%2520%253D%2520(body.sys.country)%2520%253F%2520body.sys.country%2520%253A%2520%27%27%2520%253B%250A%250A%2520%2520%2520%2520let%2520forecast%2520%253D%2520%2522For%2520city%2520%2522%252Bcity%252B%27%252C%2520country%2520%27%252Bcountry%253B%250A%250A%2520%2520%2520%2520res.render(%27index%27%252C%2520%257Bbody%2520%253A%2520body%252C%2520forecast%253A%2520forecast%257D)%253B%250A%250A%2520%2520%2520%257D)%253B%250A%250A%257D)%253B" rel="noreferrer nofollow noopener)_

Cet extrait de code permet aux données du formulaire d'entrée d'être postées à la route de l'index. Une fois que l'utilisateur entre un nom de ville, il est assigné à la variable ville en utilisant l'objet de requête.

L'URL est ensuite complétée avec le nom de la ville et l'ID et la requête est envoyée à l'API ClimaCell.

La réponse du serveur de l'API ClimaCell est retournée sous forme de fichier JSON, qui est ensuite analysé et alimenté au modèle de sortie.

Par exemple, si l'utilisateur recherchait des prévisions météo pour Boston, l'application retournerait ceci :

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589196959089_WEATHER+2.png)

Note - La température dans cet exemple est indiquée en Kelvin et est égale à 50°F ou 10°C.

## Ajouter des cartes pour visualiser vos données

Vous pouvez intégrer des cartes interactives dans votre application de prévision pour améliorer l'expérience utilisateur. Cela peut être réalisé en utilisant un fournisseur de service de cartes tiers pour les applications web.

Mapbox est un tel outil qui aide les développeurs à créer des cartes météo géniales pour leurs applications. Il s'intègre parfaitement avec n'importe quelle application météo.

Pour utiliser Mapbox, inscrivez-vous sur leur site web et [consultez leur API](https://www.mapbox.com/install/). Il existe des intégrations pour Android, iOS, Web et Unity. Dans ce cas, nous choisissons l'intégration Web pour notre outil.

Nous pouvons soit installer le CDN Mapbox, soit utiliser le module bundler. Utilisons le module bundler.

La première étape serait d'installer le package

`npm install Mapbox-gl –save`

Ensuite, nous ajoutons le fichier CSS GL JS dans le fichier HTML en incluant cet extrait dans le <head>

`<link href='https://api.mapbox.com/mapbox-gl-js/v1.8.1/mapbox-gl.css' rel='stylesheet' />`

Nous pouvons maintenant ajouter la carte à notre application. Pour ce faire, utilisez l'extrait de code ci-dessous.

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589201956495_carbon+1.png)
_[Raw](https://carbon.now.sh/embed?bg=rgba(0%2C0%2C0%2C1)&amp;t=blackboard&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=1x&amp;wm=false&amp;code=var%2520mapboxgl%2520%253D%2520require(%27mapbox-gl%252Fdist%252Fmapbox-gl.js%27)%253B%250A%2520%250Amapboxgl.accessToken%2520%253D%2520%27pk.eyJ1IjoiZGlja3Nvbi1tIiwiYSI6ImNrOXphd3MzZDBlMXYzbHFwM2kwbmlvbmkifQ.VE3RRbb8l78w9kxfmh_9ew%27%253B%250Avar%2520map%2520%253D%2520new%2520mapboxgl.Map(%257B%250Acontainer%253A%2520%27CONTAINER_ELEMENT_ID%27%252C%250Astyle%253A%2520%27mapbox%253A%252F%252Fstyles%252Fmapbox%252Fstreets-v11%27%250A%257D)%253B%250A" rel="noreferrer nofollow noopener)_

Vous pouvez choisir où placer la carte en remplaçant le

« CONTAINER_ELEMENT_ID ».

Voici un exemple de carte générée en utilisant Mapbox :

![Image](https://paper-attachments.dropbox.com/s_09D7754335BDD40A8ECD55F1187847147F5C3FBE3BBD081087C52D1E8CDCDF32_1589202164225_map.png)

# Qu'est-ce qui suit ?

À ce stade, la majeure partie du travail est terminée, et votre application peut obtenir des prévisions météorologiques pour n'importe quelle ville en utilisant l'API ClimaCell.

Cependant, vous pouvez envisager d'ajouter plus de fonctionnalités interactives à votre application ou d'étendre ses fonctionnalités.

Voici quelques choses que vous pourriez vouloir faire :

* Ajouter une fonction de recherche.
* Améliorer l'apparence de votre interface utilisateur.
* Interroger l'application par ID ou par nom.
* Afficher une liste de villes cibles et leurs ID respectifs.
* Ajouter des paramètres pour afficher des données météorologiques supplémentaires.
* Intégrer des notifications en temps réel et des signaux d'avertissement.

Comme vous pouvez le voir, le processus de construction de l'application de base est assez simple et direct. En suivant le processus ci-dessus pour exploiter la puissance d'une API météo, même les développeurs de niveau débutant peuvent mettre leur application météo en marche en quelques minutes.