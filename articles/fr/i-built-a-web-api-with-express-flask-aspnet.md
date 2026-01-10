---
title: J'ai reconstruit la même API web en utilisant Express, Flask et ASP.NET. Voici
  ce que j'ai trouvé.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-29T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/i-built-a-web-api-with-express-flask-aspnet
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c5c740569d1a4ca31ac.jpg
tags:
- name: Aspnetcore
  slug: aspnetcore
- name: 'Back end development '
  slug: back-end-development
- name: backend
  slug: backend
- name: Backend Development
  slug: backend-development
- name: C#
  slug: csharp
- name: Express
  slug: express
- name: Flask Framework
  slug: flask
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: Python
  slug: python
- name: REST API
  slug: rest-api
- name: Web Development
  slug: web-development
seo_title: J'ai reconstruit la même API web en utilisant Express, Flask et ASP.NET.
  Voici ce que j'ai trouvé.
seo_desc: "By M. S. Farzan\nI've been shopping around for a back end framework to\
  \ support a tabletop game app, and decided to do some research to determine the\
  \ best fit for my needs. \nThe objective was straightforward: to build a simple\
  \ RESTful API that would al..."
---

Par M. S. Farzan

Je cherchais un framework backend pour supporter une [application de jeu de table](https://www.nightpathpub.com/entromancy), et j'ai décidé de faire quelques recherches pour déterminer celui qui correspondrait le mieux à mes besoins. 

L'objectif était simple : construire une API [RESTful](https://restfulapi.net/) basique qui permettrait à une application frontend d'effectuer des opérations [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) de base, me donnant ainsi une introduction à ce à quoi ressemblerait le processus de développement.

Il existe de nombreuses options de frameworks backend, et je suis le plus à l'aise avec JavaScript, C# et Python (dans cet ordre), ce qui a quelque peu limité mes choix. Le point de départ naturel était de construire un frontend simple qui enverrait des requêtes à une API, qui à son tour lirait et écrirait dans une base de données locale.

J'ai commencé mon processus de développement avec Express, ce qui, pour des raisons que j'expliquerai bientôt, m'a également conduit à examiner Flask et ASP.NET. J'ai pensé que mes conclusions pourraient être utiles à d'autres qui recherchent des frameworks backend pour de petits projets. Dans cet article, je fournirai également des exemples de code et les ressources que j'ai utilisées pour tout construire.

Vous pouvez accéder au code complet sur [GitHub](https://github.com/sominator/web-api-project), également.

Je devrais préciser que je ne vais pas promouvoir un framework plutôt qu'un autre, et que je n'ai pas encore comparé des choses comme le déploiement, l'authentification ou la scalabilité. Vos résultats peuvent varier si ces particularités sont importantes pour vous !

Je vais, cependant, fournir un **TL;DR** à la fin si vous voulez simplement obtenir le résumé et les points clés.

C'est parti !

## Définition de l'API

Si vous êtes nouveau dans le développement web, vous pourriez vous demander, "qu'est-ce qu'une API ?"

J'ai dû poser la question une centaine de fois pour trouver une réponse qui avait du sens. Et ce n'est vraiment qu'après avoir construit la mienne que j'ai pu dire que je comprenais ce qu'une API _fait_.

Simplement, une API, ou "interface de programmation d'application", permet à deux systèmes informatiques différents de communiquer entre eux. Dans cet article, je vais montrer une application frontend simple qui affiche un suivi de "quête" que les joueurs peuvent consulter pour leur jeu de rôle sur table. Chaque quête a un "nom" et une "description", tous deux affichés dans le navigateur web.

Si j'avais déjà toutes les quêtes listées sur le site web et que je voulais simplement que les joueurs les consultent, je n'aurais pas besoin d'une API ou d'un backend. Pour ce projet, cependant, je veux permettre aux utilisateurs d'ajouter des quêtes, de les rechercher, de les supprimer, et ainsi de suite. Pour ces opérations, j'ai besoin de stocker les quêtes quelque part, mais mon application frontend n'est pas capable de transférer des informations directement à une base de données.

Pour cela, j'ai besoin d'une API qui peut recevoir des requêtes HTTP du site web, déterminer ce qu'il faut faire avec ces requêtes, interagir avec ma base de données, et renvoyer plus d'informations en amont de la chaîne afin que l'utilisateur puisse voir ce qui s'est passé.

L'ensemble du système - le client "frontend", l'API ou serveur "backend", et la base de données - est appelé une "stack", ou plus précisément, la "full stack". Pour ce projet, j'ai construit un site web frontend simple en haut de la stack, et j'ai changé tout ce qui se trouve en dessous en essayant différents frameworks et bases de données.

## Structure du projet

La structure de ce projet était assez simple, avec le client frontend séparé de trois serveurs différents que je pourrais lancer selon les besoins pour servir l'API.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Project-Structure.PNG)

J'ai utilisé [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/) comme éditeur de code et IDE, avec les packages de langage requis installés pour JavaScript, Python et C#.

Je vais fournir un aperçu de mon expérience avec chaque framework, avec des liens vers les tutoriels et les packages que j'ai utilisés pour les faire fonctionner avec le client. Mais d'abord, examinons le frontend !

## Le Client : Vue.js

L'objectif pour le client était d'avoir un site web simple qui recevrait des informations de la base de données via l'API et les afficherait à l'utilisateur. Pour simplifier le processus, mes exigences étaient que le client devrait uniquement "lire" tous les éléments de la base de données, et fournir à l'utilisateur la possibilité de "créer" une nouvelle quête.  

Ces opérations de "lecture" et de "création" - le "R" et le "C" dans "CRUD" - sont analogues aux méthodes HTTP de "GET" et "POST", que nous verrons dans le code ci-dessous.

En développement frontend, je suis le plus à l'aise avec [Vue](https://vuejs.org/), et j'ai utilisé le [Vue CLI](https://cli.vuejs.org/) pour échafauder un client de base, avec la structure de fichiers suivante :   

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Client-Structure.PNG)

J'ai remplacé le balisage de base fourni par le Vue CLI par le suivant :

```html
<template>
    <div id="app">
        <h1>Quêtes RPG</h1>
        <p v-for="(quest, index) in quests" v-bind:key="index">{{quest.name}}: {{quest.description}}</p>
        <input type="text" v-model="newQuestName" placeholder="Nom de la quête" /> <br />
        <input type="text" v-model="newQuestDescription" placeholder="Description de la quête" /><br /><br />
        <button v-on:click="postQuest">Ajouter une quête</button>
    </div>
</template>
```

Et le code Vue correspondant :

```javascript
import axios from 'axios';

    export default {
        name: 'App',
        data: function () {
            return {
                quests: null,
                newQuestName: null,
                newQuestDescription: null
            }
        },
        methods: {
            getQuests: function () {
                axios
                    .get('http://localhost:3000/quests')
                    .then(response => (this.quests = response.data));
            },
            addQuest: function () {
                axios
                    .post('http://localhost:3000/quests', {
                        name: this.newQuestName,
                        description: this.newQuestDescription
                    });
            },
            postQuest: function () {
                axios.all([this.addQuest(), this.getQuests()]);
                this.$forceUpdate();
            }
        },
        mounted: function () {
            this.getQuests();
        }
    }
```

Si vous n'êtes pas familier avec Vue, les spécificités du frontend ne sont pas si importantes ! Ce qui est significatif ici, c'est que j'utilise un package JavaScript appelé [Axios](https://github.com/axios/axios) pour faire mes requêtes GET et POST à un serveur potentiel. 

Lorsque le client se charge, il fera une requête GET à l'URL http://localhost:3000/quests pour charger toutes les quêtes de la base de données. Il fournit également quelques champs de saisie et un bouton qui POSTera une nouvelle quête.

En utilisant le Vue CLI pour servir le client sur http://localhost:8080, le frontend de l'application ressemble à ceci en action :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Client.PNG)

Une fois que les quêtes sont ajoutées à la base de données, elles commenceront à apparaître entre l'en-tête "Quêtes RPG" et les champs de saisie.

### Ressources du Client

Pour construire le client, j'ai utilisé :

* [NodeJS](https://nodejs.org/en/)/[NPM](https://www.npmjs.com/) pour la gestion des packages
* [Vue CLI](https://cli.vuejs.org/) pour l'échafaudage, le service et la construction de projets
* [Axios](https://github.com/axios/axios) pour faire des requêtes HTTP à l'API
* [Documentation Vue Axios](https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html) pour comprendre comment utiliser Axios en concert avec l'API
* [Postman](https://www.postman.com/) pour tester les requêtes API via le navigateur avant de les implémenter dans le client.

## API JavaScript : Express

[Express](https://expressjs.com/) est un framework web léger pour [NodeJS](https://nodejs.org/en/) qui vous permet d'écrire des applications côté serveur avec JavaScript.

Il est non-opinionné, ce qui signifie que vous pouvez construire vos applications comme vous le souhaitez sans qu'il définisse l'architecture pour vous. Vous pouvez ajouter des packages pour améliorer la fonctionnalité comme vous le souhaitez, ce que j'ai trouvé être une épée à double tranchant en tant que débutant avec le framework. Plus sur cela plus tard.

Étant le plus à l'aise en JavaScript, j'étais enthousiasmé par la perspective d'avoir toute la stack fonctionnant sur un seul langage au lieu de plusieurs. J'avais entendu parler de la "MEVN Stack", qui désigne une application full stack composée de [MongoDB](https://www.mongodb.com/), Express, Vue et NodeJS, et j'ai décidé d'essayer cela pour cette itération du projet.

J'ai suivi un [tutoriel sur les API web](https://dev.to/beznet/build-a-rest-api-with-node-express-mongodb-4ho4) pour d'abord construire une application template, puis j'ai utilisé un autre [tutoriel MEVN](https://medium.com/@anaida07/mevn-stack-application-part-1-3a27b61dcae0) pour remplir les détails sur la façon de faire communiquer l'API avec le client Vue que j'avais construit. L'API Express que j'ai créée pour ce projet suit une structure similaire à la première, utilisant MongoDB comme base de données :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Express-Structure.PNG)

Si vous venez d'un background JavaScript, Express est assez facile à lire, même si vous n'êtes pas familier avec certains termes de backend. Voici un extrait de /routes/quests.js, par exemple, qui gère les requêtes HTTP [endpoint](https://en.wikipedia.org/wiki/Web_API#Endpoints) :

```javascript
router.get('/', async (req, res) => {
    try {
        const quests = await Quest.find();
        res.json(quests);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

router.post('/', async (req, res) => {
    const quest = new Quest({
        name: req.body.name,
        description: req.body.description
    });
    try {
        const newQuest = await quest.save();
        res.status(201).json(newQuest);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});
```

Le thème général du code est de recevoir une requête, d'essayer de contacter la base de données pour effectuer un travail, puis d'envoyer une réponse à celui qui demande. Les spécificités peuvent être assez complexes, en particulier si vous écrivez votre propre [middleware](https://expressjs.com/en/guide/using-middleware.html) qui fait des choses entre la requête et la réponse, mais le code est au moins lisible.

J'ai trouvé MongoDB sans douleur à utiliser en tant que base de données [NoSQL](https://www.mongodb.com/nosql-explained). Si vous travaillez avec Express, vous utiliserez probablement [Mongoose](https://mongoosejs.com/) comme [ODM](https://en.wikipedia.org/wiki/Object-relational_mapping#Object-oriented_databases) - essentiellement comme un "intermédiaire" qui traduit un modèle de ce à quoi ressemblent vos données pour la base de données.

Le modèle dans cette application (appelé un "schéma" en termes Mongoose) est vraiment simple, situé dans /models/quests.js :

```language
const questSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    }
});
```

Ce qui précède indique que la base de données doit stocker nos deux champs : un nom de quête et une description de quête. Ces deux champs sont des chaînes de caractères et sont requis. Toutes les requêtes GET et POST devront se conformer à ce modèle pour interagir avec la base de données.

Après avoir tout configuré et POSTé quelques nouvelles quêtes, le site frontend a commencé à se remplir de données :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Vue-Front-End-1.PNG)

Le processus de configuration de l'API Express n'a pas été sans ses moments de frustration, cependant. Étant principalement un développeur frontend et de jeux 2D, je suis devenu intimement familier avec la dispersion de l'écosystème JavaScript. Cette frustration a été amplifiée en essayant de construire une application backend. Il y a un _grand nombre_ de packages nécessaires pour tout faire fonctionner, chacun ayant sa propre configuration et implémentation requises.

Si vous cherchez un framework qui fait tout dès la sortie de la boîte, Express n'est certainement pas le choix pour vous. Il est léger, flexible et facile à lire, de manière très "choisissez-votre-propre-aventure". J'aime beaucoup la propreté du code et la possibilité de structurer mes projets comme je le souhaite, mais le dépannage et la gestion des erreurs laissent beaucoup à désirer.

### Ressources JavaScript/Express

Pour construire l'API JavaScript, j'ai utilisé :

* [NodeJS](https://nodejs.org/en/)/[NPM](https://www.npmjs.com/) pour la gestion des packages
* [Express](https://expressjs.com/) comme framework web principal
* [Dotenv](https://www.npmjs.com/package/dotenv) pour créer des variables spécifiques à l'environnement
* [Nodemon](https://nodemon.io/) pour surveiller les fichiers pour les changements et redémarrer le serveur afin de ne pas avoir à le faire
* [CORS](https://expressjs.com/en/resources/middleware/cors.html) pour permettre les [requêtes cross-origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (basiquement une douleur si vous essayez de faire des requêtes d'un client à un serveur qui s'exécutent tous deux localement sur votre machine)
* [MongoDB](https://www.mongodb.com/) pour la base de données [NoSQL](https://www.mongodb.com/nosql-explained)
* [Mongoose](https://mongoosejs.com/) pour écrire des modèles qui mappent sur MongoDB 
* [Ce tutoriel API](https://dev.to/beznet/build-a-rest-api-with-node-express-mongodb-4ho4) pour fournir une compréhension de base de la création d'une stack Express-MongoDB
* [Ce tutoriel MEVN](https://medium.com/@anaida07/mevn-stack-application-part-1-3a27b61dcae0) pour combler les lacunes de l'exécution d'une stack complète MongoDB-Express-Vue-Node

## API Python : Flask

Dans le processus de construction de l'API Express, j'ai eu une conversation avec un ami data scientist qui travaille en Python. Cela m'a donné l'idée d'essayer des frameworks non-JavaScript pour voir s'ils étaient mieux adaptés à mon application.

J'ai jeté un coup d'œil rapide à [Django](https://www.djangoproject.com/), puisque j'en avais entendu parler comme un framework backend puissant qui fournit tout dès la sortie de la boîte. J'étais un peu intimidé par son côté opinionné, et j'ai opté pour essayer [Flask](https://palletsprojects.com/p/flask/) à la place, qui ressemble un peu à l'équivalent Python d'Express.

J'ai suivi les premiers morceaux de l'excellent [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) pour configurer la structure de mon application, en utilisant le tutoriel compagnon [RESTful API](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) pour remplir les pièces des requêtes HTTP. La structure des fichiers s'est avérée être seulement un peu plus complexe que celle de l'API Express :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Flask-Structure.PNG)

Le tutoriel que j'ai suivi utilise [SQLite](https://www.sqlite.org/index.html) pour sa base de données, avec [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) comme [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping). Le code de requête HTTP qui est le plus analogue à l'API Express est situé dans /app/routes.py :

```python
@app.route('/quests', methods=['GET'])
def get_quests():
    questQuery = Quest.query.all()
    quests = {}
    for quest in questQuery:
        quests[quest.name] = quest.description
    return jsonify(quests)

@app.route('/quests', methods=['POST'])
def post_quest():
    newQuest = Quest(name=request.json['name'], description=request.json['description'])
    db.session.add(newQuest)
    db.session.commit()
    return "Quête ajoutée !"
```

De même, le modèle de la base de données (similaire au "schéma" Mongoose) est dans /app/models.py :

```python
class Quest(db.Model):
    name = db.Column(db.String(256), primary_key=True, index=True, unique=True)
    description = db.Column(db.String(256), index=True, unique=True)
```

Comme je l'ai mentionné, je suis plus familier avec JavaScript et C# qu'avec Python, et travailler avec ce dernier pour construire l'API Flask semblait presque comme de la triche. Certaines choses comme le cheminement, la gestion des packages et l'écriture de code fonctionnel étaient simplement _faciles_, bien que j'aie eu du mal à faire en sorte que l'API analyse correctement le JSON pour le client. Je soupçonne que c'était plus un problème de ma méconnaissance du langage qu'autre chose, mais cela a pris du temps à résoudre.

Pour être tout à fait honnête, venant d'un background non-Flask, je m'attendais à compléter quelques tutoriels et à lancer une API sans avoir à faire trop de travail.

Je ne peux pas dire que cela s'est passé ainsi, car Python a ses propres particularités qui nécessitent un certain temps pour s'y habituer. Néanmoins, l'écosystème Python semble être extrêmement bien organisé, et j'ai apprécié mon temps à construire l'API Flask.

J'ai également entendu dire que Django est une meilleure option et plus scalable pour les grands projets. Mais il semble que cela impliquerait une courbe d'apprentissage séparée et plus raide pour devenir compétent. 

Flask était assez facile pour moi, en tant que développeur non-Python, à apprendre et à construire quelque chose en un week-end. Je soupçonne que l'apprentissage de Django prendrait beaucoup plus de temps, mais avec des dividendes potentiellement plus grands à long terme. 

### Ressources Python/Flask

Pour construire l'API Flask, j'ai utilisé :

* [Python 3](https://www.python.org/)/[pip](https://pip.pypa.io/en/stable/) pour la gestion des packages
* [Flask](https://palletsprojects.com/p/flask/) comme framework web principal
* [python-dotenv](https://pypi.org/project/python-dotenv/) pour configurer les variables d'environnement
* [SQLite](https://www.sqlite.org/index.html) comme base de données 
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) comme ORM pour travailler avec SQLite
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) comme outil supplémentaire pour migrer les données vers SQLite 
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) pour gérer le même problème CORS que avec l'API Express
* Le [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) pour apprendre les bases
* Le [tutoriel Flask REST API](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) pour comprendre comment recevoir les requêtes HTTP

## API C# : ASP.NET

Je ne peux pas vous dire combien de fois j'ai googlé ".[NET](https://dotnet.microsoft.com/)" pour comprendre ce que c'est, comment il est différent de [ASP.NET](https://dotnet.microsoft.com/apps/aspnet), et pourquoi je voudrais l'utiliser. Mes connaissances en C# proviennent principalement de mon travail avec [Unity](https://unity.com/), qui existe quelque peu en marge de .NET et ne fournit pas beaucoup d'exposition à l'écosystème plus large de Microsoft.

J'ai passé du temps à rechercher [Razor Pages](https://docs.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-3.1&tabs=visual-studio) et [MVC](https://docs.microsoft.com/en-us/aspnet/core/mvc/overview?view=aspnetcore-3.1), et j'ai finalement compris l'étendue des fonctionnalités d'ASP.NET en tant que framework web open source de Microsoft. J'ai décidé d'inclure ASP.NET dans les options potentielles pour le backend de mon application, et je me suis mis à travailler sur le [tutoriel officiel sur les API web](https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-mongo-app?view=aspnetcore-3.1&tabs=visual-studio) avec ASP.NET Core et MongoDB.

La structure des fichiers pour cette version de l'API était plus complexe que les autres, étant donné que les projets .NET ont tendance à avoir une empreinte beaucoup plus grande :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/ASPNet-Structure.PNG)

Je devrais également mentionner que j'avais déjà Visual Studio et toutes les charges de travail requises installées, ce qui a facilité le processus de configuration. De plus, ayant passé du temps avec MongoDB pour l'API Express, j'ai trouvé que la partie base de données du projet était similaire, bien que par défaut, ASP.NET semble préférer utiliser le [SQL Server](https://www.microsoft.com/en-us/sql-server/default.aspx) de Microsoft et l'[ORM Entity Framework](https://docs.microsoft.com/en-us/ef/).

Le code ASP.NET pour les requêtes HTTP est un peu plus complexe que ce que nous avons vu avec les deux autres API, mais ce n'est rien comparé à tout le code qui l'entoure.  

Tout d'abord, considérons cet extrait dans /Controllers/QuestController.cs qui gère les requêtes :

```c#
namespace QuestAPI.Controllers
{
    [Route("quests/")]
    [ApiController]
    public class QuestsController : ControllerBase
    {
        private readonly QuestService _questService;

        public QuestsController(QuestService questService)
        {
            _questService = questService;
        }

        [HttpGet]
        public ActionResult<List<Quest>> Get() =>
            _questService.Get();

        [HttpPost]
        public ActionResult<Quest> Create(Quest quest)
        {
            _questService.Create(quest);
            return CreatedAtRoute("GetQuest", new { id = quest.Id.ToString() }, quest);
        }
    }
}
```

Pas trop terrible, presque lisible, d'une certaine manière C#. Le modèle de données dans /Models/Quest.cs est encore plus facile :

```c#
namespace QuestAPI.Models{
    public class Quest
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }

        [BsonElement("Name")]
        public string Name { get; set; }

        public string Description { get; set; }
    }
}
```

Ces deux extraits font essentiellement les mêmes choses que les exemples précédents que nous avons vus : prendre des requêtes du frontend, les traiter pour obtenir ou modifier des données dans la base de données, et envoyer une réponse au client.  

Cependant, comme vous pouvez probablement le constater à partir de la structure de fichiers complexe, il y a tellement de code qui entoure ces extraits, ainsi que des [Interfaces](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/interfaces/), de l'[Injection de Dépendances](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-3.1), et d'autres abstractions, qu'il peut être difficile de comprendre comment tout cela fonctionne ensemble.

Considérez le code de configuration suivant dans /Startup.cs :

```c#
        public void ConfigureServices(IServiceCollection services)
        {
            services.Configure<QuestDatabaseSettings>(Configuration.GetSection(nameof(QuestDatabaseSettings)));

            services.AddSingleton<IQuestDatabaseSettings>(sp => sp.GetRequiredService<IOptions<QuestDatabaseSettings>>().Value);

            services.AddSingleton<QuestService>();

            services.AddCors(options =>
            {
                options.AddPolicy(MyAllowSpecificOrigins, builder =>
                {
                    builder.WithOrigins("http://localhost:3000/quests", "http://localhost:8080").AllowAnyHeader().AllowAnyMethod();
                });
            });

            services.AddControllers();
        }
```

Ou ce morceau particulièrement imbriqué d'un [tutoriel sur les API web SQL Server](https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-web-api?view=aspnetcore-3.1&tabs=visual-studio) :

```c#
    [HttpGet]
    public async Task<ActionResult<IEnumerable<TodoItemDTO>>> GetTodoItems()
    {
        return await _context.TodoItems
            .Select(x => ItemToDTO(x))
            .ToListAsync();
    }
```

Lol. Qu'est-ce que c'est ? En tant que nouvel utilisateur, même si je suis familier avec C#, je peux passer ligne par ligne pour comprendre chaque abstraction, ou je peux simplement faire confiance au framework pour tout gérer pour moi et l'oublier.

J'ai tendance à vouloir savoir exactement comment mon code fonctionne afin de pouvoir le corriger ou le modifier si nécessaire. Mais je sens certainement que mon temps passé à apprendre les tenants et aboutissants d'ASP.NET pourrait être mieux utilisé pour maîtriser un autre framework.

Pour être juste, ASP.NET semble être similaire à Django en étant plus opinionné et en vous fournissant une tonne de choses dès la sortie de la boîte, y compris une solution d'authentification, une gestion de base de données, et bien plus. Si ces choses sont importantes pour vous, cela vaut certainement la peine de le considérer.  

Il a également le soutien complet de Microsoft et d'une communauté open source. Donc, si vous cherchez à développer des applications de niveau entreprise qui doivent évoluer, vous pourriez vouloir jeter un regard plus approfondi sur ASP.NET comme solution potentielle.

### Ressources C#/ASP.Net

Pour construire l'API ASP.Net, j'ai utilisé les ressources suivantes :

* [Visual Studio Community](https://visualstudio.microsoft.com/downloads/) comme éditeur de code et IDE, avec la charge de travail ASP.NET et le développement web installés (j'avais déjà MongoDB en cours d'exécution à partir de l'API Express)
* Le [tutoriel officiel](https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-mongo-app?view=aspnetcore-3.1&tabs=visual-studio) de Microsoft pour construire des API web avec ASP.NET et MongoDB

## TL;DR

En résumé, avec quelques variations et accrocs entre eux, j'ai réussi à faire fonctionner chacune des API web avec le client Vue, avec la possibilité de consulter les quêtes et d'en ajouter à la base de données. J'espère que mon explication du processus vous a été utile dans votre propre recherche d'un framework backend, mais voici quelques recommandations supplémentaires au cas où :

* Si vous êtes un développeur JavaScript et/ou souhaitez gérer tout ce que fait votre application, y compris son architecture, envisagez d'utiliser Express.
* Si vous êtes un développeur Python et/ou souhaitez une expérience agréable dans le développement de petits projets, essayez Flask, mais envisagez d'utiliser Django si vous avez besoin de plus de support dès la sortie de la boîte et ne vous dérangez pas de vous conformer à un framework opinionné.
* Si vous êtes un développeur C# et prêt à passer du temps à apprendre les détails les plus obscurs des meilleures pratiques de codage en C#, envisagez d'utiliser ASP.NET. Alternativement, si vous avez besoin d'un support de niveau entreprise dès la sortie de la boîte, vous seriez bien en peine de trouver mieux.
* Si vous ne savez pas quoi utiliser et souhaitez simplement apprendre le développement backend, jetez un coup d'œil à Flask. C'est facile à utiliser et vous enseignera les bases dont vous aurez besoin pour construire des applications web dans n'importe quel langage de codage.
* Si vous ne savez pas quoi utiliser et souhaitez une aventure, choisissez Express. Il y a un terrier de gestion de packages et de questions Stack Overflow qui attendent et qui pourraient vous faire arracher les cheveux, mais vous apprendrez beaucoup sur l'écosystème JavaScript et le développement web en général.

De plus, deux choses méritent d'être mentionnées et qui m'ont posé problème dans ce processus : CORS et les variables d'environnement. J'ai déjà mentionné le premier dans cet article à plusieurs reprises, mais cela vaut la peine d'en discuter à nouveau pour comprendre l'ampleur de la construction d'une application full stack sur votre machine.

Sauf si vous avez un environnement de développement intégré qui gère toute la stack pour vous, vous aurez probablement un client, un serveur et une base de données qui s'exécutent indépendamment les uns des autres.  

Dans la section sur l'API Express ci-dessus, par exemple, j'exécutais 

1. le serveur Vue CLI, qui rendait mon application frontend sur le port 8080 ; 
2. un script NPM pour lancer le serveur de l'API Express sur le port 3000 ; et
3. une instance séparée de la base de données Mongo pour faire fonctionner tout cela ensemble. Cela fait trois invites de commande ouvertes et un vrai bazar !

Si vous creusez dans le code Vue ci-dessus (ou sur GitHub), vous verrez que les requêtes faites au nom du client, s'exécutant sur http://localhost:8080, sont adressées au serveur sur http://localhost:3000, où l'API Express écoute. Cela s'appelle le "partage des ressources cross-origin", ou [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS), et il est bloqué par le navigateur pour des raisons de sécurité. La plupart des frameworks nécessitent que vous installiez un package supplémentaire pour faire fonctionner tout cela dans votre environnement local.

Deuxièmement, vous voudrez vous familiariser avec les [variables d'environnement](https://en.wikipedia.org/wiki/Environment_variable), qui peuvent vraiment aider à lisser certains bords rugueux au moment de l'exécution. J'ai utilisé [dotenv](https://www.npmjs.com/package/dotenv) et [Flask-Env](https://pypi.org/project/Flask-Env/) pour les projets Express et Flask, respectivement. 

Les deux packages vous permettent de configurer des choses comme l'emplacement de votre base de données, ou le port par défaut que votre application devrait utiliser, dans un seul document. Votre application utilise ensuite ce document au moment de l'exécution pour déterminer où trouver tout, sans nécessiter de configuration supplémentaire de votre part.

Une dernière note qui pourrait être utile si vous travaillez simplement sur un projet backend et ne souhaitez pas vous donner la peine de construire un client frontend : envisagez d'utiliser une application tierce comme [Postman](https://www.postman.com/). Je l'ai utilisé pour faire des requêtes HTTP à chacune des API pour m'assurer qu'elles fonctionnaient correctement avant d'ajouter le client Vue et d'essayer de faire fonctionner toute la stack ensemble. 

J'espère que cet article vous a été utile dans votre propre processus de recherche d'un framework backend. Faites-moi savoir ce que vous trouvez ! 

Si vous avez apprécié cet article, envisagez de [découvrir mes jeux et livres](https://www.nightpathpub.com/), de [vous abonner à ma chaîne YouTube](https://www.youtube.com/msfarzan?sub_confirmation=1), ou de [rejoindre le Discord _Entromancy_](https://discord.gg/RF6k3nB).

M. S. Farzan, Ph.D. a écrit et travaillé pour des entreprises de jeux vidéo de haut profil et des sites éditoriaux tels qu'Electronic Arts, Perfect World Entertainment, Modus Games et MMORPG.com, et a servi en tant que Community Manager pour des jeux comme _Dungeons & Dragons Neverwinter_ et _Mass Effect: Andromeda_. Il est le Directeur Créatif et le Game Designer Principal de _[Entromancy: A Cyberpunk Fantasy RPG](https://www.nightpathpub.com/rpg)_ et l'auteur de _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Retrouvez M. S. Farzan sur Twitter [@sominator](https://twitter.com/sominator).