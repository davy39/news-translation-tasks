---
title: Comment configurer une base de données si vous êtes un développeur front-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-07T15:12:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-database-if-youre-a-front-end-developer-3ed945221219
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d_hx4BxGZ9qYODhnTn-Bjg.jpeg
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment configurer une base de données si vous êtes un développeur front-end
seo_desc: 'By Andrea Zanin

  Someone recently asked me what’s the easiest way for a front-end developer to save
  users’ data. So I am going to explain how to do just that.

  Setting up the database

  The first thing we will need is an actual database. You can head to ...'
---

Par Andrea Zanin

Quelqu'un m'a récemment demandé quelle était la manière la plus simple pour un développeur front-end de sauvegarder les données des utilisateurs. Je vais donc expliquer comment faire exactement cela.

### Installation de la base de données

La première chose dont nous aurons besoin est une base de données réelle. Vous pouvez vous rendre sur [mlab](https://mlab.com) pour en obtenir une gratuite. Une fois inscrit, cliquez sur **créer nouveau** dans l'onglet MongoDB Deployments. La base de données sandbox est gratuite, c'est donc celle que nous allons utiliser.

Une fois que nous avons créé la base de données, nous devons créer un compte afin de pouvoir nous authentifier. Cliquez sur le nom de la base de données, puis sur **users**, et **add database user**. Notez le nom d'utilisateur et le mot de passe que vous avez choisis, car nous en aurons besoin plus tard.

En haut de la page de la base de données, vous devriez voir un URI MongoDB. Il s'agit de l'adresse web de notre base de données. L'URI de votre base de données est comme l'URL d'une page web. Par convention, l'URI MongoDB est comme suit :

```
mongodb://<dbuser>:<dbpassword>@<host&gt;:<port>/<dbname>
```

Le mien, par exemple, est :

```
mongodb://admin:superSecretPassword@ds111885.mlab.com:11885/medium
```

### Configuration du serveur

Nous allons utiliser Node dans notre back-end. Pour éviter de devoir le configurer, vous pouvez cloner mon projet sur Glitch en cliquant [ici](https://glitch.com/edit/#!/remix/amusing-timbale)

Jetez un coup d'œil au fichier `server.js` de départ que j'ai fourni :

Nous commençons par importer `express` — c'est la bibliothèque que nous utiliserons pour gérer les requêtes vers notre serveur.

Nous avons besoin de `use(require(cors))` pour permettre les requêtes cross-domain. Ce sont des requêtes d'un site web hébergé sur un domaine vers un serveur sur un autre domaine.  
`app.use(require('body-parser').json())` analyse automatiquement la requête en JSON pour nous.

Ensuite, nous passons à la méthode `get` la route que nous voulons gérer et le callback qui la gérera. Cela signifie que chaque fois que quelqu'un ouvre la page `/` de notre site web, la requête sera gérée par ce callback. Le domaine de base est implicite, donc si votre domaine est http://shiny-koala.glitch.com, la route `/about` sera http://shiny-koala.glitch.com/about_._

Pour être précis, lorsque je dis « ouvrir la page », je veux dire qu'il fait une requête en utilisant la méthode `GET` vers notre serveur. Les méthodes Http sont simplement des types de requêtes que vous pouvez faire à un serveur. Nous n'utiliserons que les suivantes :

* `GET` Cette méthode est utilisée pour récupérer des ressources d'un serveur. Par exemple, lorsque vous ouvrez Facebook, il charge le HTML, le CSS et le JavaScript nécessaires.
* `POST` Cette méthode est utilisée pour créer des ressources sur un serveur. Par exemple, lorsque vous publiez quelque chose sur Facebook, les informations que vous avez écrites dans ce post sont envoyées aux serveurs de Facebook dans une requête `POST`.
* `PUT` Cette méthode est utilisée pour mettre à jour des ressources sur un serveur. Par exemple, lorsque vous modifiez un post, vos modifications sont envoyées au serveur de Facebook dans une requête `PUT`.

Les méthodes `app.post` et `app.put` fonctionnent exactement comme `app.get`, mais gèrent les méthodes POST et PUT au lieu de GET, ce qui est assez raisonnable.

### Routage

Pendant que vous développez le serveur, vous devrez effectuer quelques tests. Pour exécuter des requêtes HTTP, vous pouvez utiliser le site pratique [REST test test](https://resttesttest.com/) ou l'application [Insomnia](https://insomnia.rest/).

Pour vérifier l'URL de votre application Glitch, cliquez sur le bouton **show**.

Jusqu'à présent, nous n'avons utilisé que la route `/`. Mais nous voulons stocker différentes informations sur différents utilisateurs, nous avons donc besoin d'une route différente pour chaque utilisateur. Par exemple : `/ZaninAndrea` et `/JohnGreen`

Nous avons maintenant un problème : nous ne pouvons pas coder chaque route individuellement, car ce n'est pas une approche très scalable. Ce dont nous avons besoin, ce sont des **paramètres de route**. Nous ne coderons qu'une seule route : `/:user`

Le deux-points indique à Express de capturer toute route commençant par `/` et suivie uniquement de caractères alphanumériques.

Quelques exemples :

* `/ZaninAndrea` sera capturé
* `/Johnny45` sera capturé
* `/alex/score` ne **sera pas** capturé

Nous pouvons ensuite récupérer la valeur de `user` dans la variable `request.params.user`

Notre serveur répond maintenant à chaque requête en renvoyant le nom d'utilisateur.

### Ajout de données à la base de données

Nous savons qui est l'utilisateur, et maintenant nous voulons pouvoir stocker quelques informations à son sujet.

Pour interroger la base de données, nous utiliserons la bibliothèque `mongodb`. Vous pouvez l'installer de deux manières :

```
npm install mongodb --save
```

ou si vous utilisez Glitch, allez dans le fichier `package.json` et cliquez sur le bouton **Add package**.

Chargeons la bibliothèque et stockons l'URI MongoDB dans une variable :

L'URI est une information très sensible — c'est tout ce dont vous avez besoin pour accéder à votre base de données. Il est préférable de le mettre dans un fichier `.env` qui ne sera pas visible par les autres.

Glitch chargera automatiquement les variables du fichier `.env` dans la variable `process.env`.

La connexion à la base de données est une opération asynchrone, nous devons donc envelopper toute la configuration du serveur dans un callback comme ceci :

Les bases de données sont organisées en collections, et les collections contiennent des documents (basiquement des fichiers JSON). Connectons-nous donc à la collection `user` (elle sera créée la première fois que nous y accéderons).

Tout d'abord, nous allons gérer la route `POST`. C'est celle que nous utiliserons lorsque nous ajouterons des données sur un utilisateur pour la première fois. Ensuite, nous utiliserons la route `PUT` pour la mettre à jour.

La méthode `collection.insertOne` ajoute un nouveau document à la collection. Dans notre cas, chaque utilisateur aura son propre document.

`{ ...request.body, user : request.params.user }` utilise l'opérateur de propagation ([spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator)) pour fusionner les données fournies via le corps de la requête et l'utilisateur fourni via l'URL.

Le résultat est le document qui sera stocké dans la collection.

Le deuxième argument est un callback, et il notifie simplement l'utilisateur du résultat de l'opération.

### Récupération de données de la base de données

Maintenant que nous avons des données sur le serveur, nous voulons pouvoir les lire. Nous utilisons la méthode `GET` pour cela.

Cette fois, le premier argument est un filtre indiquant à la base de données de ne nous envoyer que les documents avec la bonne propriété utilisateur.

Les documents sont retournés à l'utilisateur dans un tableau, car il pourrait théoriquement y avoir plus d'un document avec cette propriété utilisateur. C'est à nous de nous assurer que cela n'arrive pas.

### Mise à jour des données dans la base de données

Enfin, mais non des moindres, la méthode `PUT` que nous utilisons pour mettre à jour un utilisateur déjà existant.

Le premier argument est un filtre, comme celui que nous avons utilisé dans la méthode `GET`.

Le deuxième argument est un document de mise à jour — vous pouvez en lire plus à ce sujet [ici](https://docs.mongodb.com/manual/reference/method/db.collection.update/#update-parameter). Dans notre cas, nous disons à la base de données de fusionner les données passées par l'utilisateur avec les données déjà existantes.

Faites attention cependant, car les paramètres imbriqués seront remplacés et non fusionnés.

### Au revoir

Ceci est loin d'être un guide complet sur les bases de données et la programmation back-end, mais c'est suffisant pour vous lancer et pour alimenter des projets personnels.

Je parlerai probablement de l'authentification dans un futur article. En attendant, n'utilisez pas cela pour stocker des données sensibles.

Vous pouvez bricoler avec le projet complet [ici](https://glitch.com/edit/#!/remix/bush-vegetable), vous aurez besoin de votre propre base de données, si vous n'en avez pas encore créé une, retournez à la section **Installation de la base de données**.

Si vous avez aimé cet article, veuillez lui donner quelques applaudissements pour que plus de gens le voient. Merci !