---
title: Comment exécuter plusieurs conteneurs avec Docker Compose
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-27T19:31:29.000Z'
originalURL: https://freecodecamp.org/news/run-multiple-containers-with-docker-compose
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/docker-compose-scaled-1.jpeg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Comment exécuter plusieurs conteneurs avec Docker Compose
seo_desc: "By Arjav Dave\nDocker has become increasingly popular over the last several\
  \ years. One reason for this is that you can create portable containers which are\
  \ fast and easy to deploy. \nAs described on Docker's website, a container is something\
  \ that packa..."
---

Par Arjav Dave

Docker est devenu de plus en plus populaire au cours des dernières années. Une des raisons à cela est que vous pouvez créer des conteneurs portables qui sont rapides et faciles à déployer. 

Comme décrit sur le [site web](https://www.docker.com/resources/what-container/) de Docker, un **conteneur** est quelque chose qui emballe votre code ainsi que toutes les autres dépendances afin qu'il puisse être déployé sur plusieurs plateformes de manière fiable. 

Ces conteneurs peuvent être exécutés localement sur votre Windows, Mac et Linux. Et les principaux systèmes cloud comme AWS ou Azure les supportent directement. Vous pouvez également utiliser Docker sur tout espace d'hébergement où il peut être installé et exécuté. 

Si vous souhaitez en savoir plus sur les bases de Docker et avez besoin d'une feuille de triche pour la CLI de Docker, j'ai [écrit un article d'introduction à ce sujet ici](https://www.daveops.co.in/post/docker-a-beginner-s-cheat-sheet-2022).

Dans ce tutoriel, nous allons approfondir afin que vous puissiez comprendre certaines des fonctionnalités plus avancées comme comment exécuter plusieurs conteneurs.

## Pourquoi Docker Compose ?

Avec Docker Compose, vous pouvez configurer et démarrer plusieurs conteneurs avec un seul fichier YAML. Cela est vraiment utile si vous travaillez sur une pile technologique avec plusieurs technologies. 

Par exemple, supposons que vous travaillez sur un projet qui utilise une base de données MySQL, Python pour l'IA/ML, NodeJS pour le traitement en temps réel et .NET pour servir des API. Il serait fastidieux de configurer un tel environnement pour chaque membre de l'équipe. Heureusement, Docker facilite cela avec l'aide de Compose.

### Comment fonctionne Docker Compose ?

`docker compose` est un fichier YAML dans lequel nous pouvons configurer différents types de services. Ensuite, avec une seule commande, tous les conteneurs seront construits et démarrés. 

Il y a 3 étapes principales impliquées dans l'utilisation de Compose :

* Générer un Dockerfile pour chaque projet.
* Configurer les services dans le fichier docker-compose.yml.
* Démarrer les conteneurs.

Nous allons maintenant voir comment utiliser `docker compose` peut vous aider à configurer un environnement pour un projet qui utilise un ensemble d'outils différents, comme nous en avons discuté ci-dessus.

### Prérequis

Vous pourriez penser que vous devez avoir toutes les technologies installées pour exécuter cette pile technologique de MySQL, Python, NodeJS, .NET et PHP. 

Mais en réalité, tout ce dont vous avez besoin est un moteur Docker en cours d'exécution. Les dernières versions de Docker viennent avec Docker Compose installé. Pour l'instant, vous n'avez pas besoin d'installer autre chose.

## Ce que nous allons faire dans ce tutoriel

Avant de commencer, voici un bref aperçu de ce que nous allons faire. Nous allons aborder chaque technologie une par une. 

Pour chaque technologie, nous allons créer une application d'exemple (sauf pour MySQL) et créer un Dockerfile pour chacune.

Ensuite, nous allons pointer ces Dockerfiles dans notre fichier YAML `docker compose`. 

Enfin, nous allons configurer `docker compose` afin que chaque application fasse ce qu'elle est censée faire.

Avant de commencer, créez un dossier nommé `super-app`. Ensuite, créez un fichier `docker-compose.yml`. Dans ce fichier, nous allons configurer toutes nos applications. Alors commençons.

Pour ceux d'entre vous qui sont intéressés par le code, vous pouvez visiter le [dépôt ici](https://github.com/shenanigan/super-app-docker).

### Comment configurer MySQL

Ajoutez le contenu suivant dans votre fichier docker-compose.yml :

    version: '3.4'
    services:
      super-app-db:
        image: mysql:8.0.28
        environment:
          MYSQL_DATABASE: 'super-app'
          MYSQL_ROOT_PASSWORD: '$SuperApp1'
        ports:
          - '3306:3306'
        expose:
          - '3306'

Sous la section `services`, nous allons lister tous les types d'applications à configurer.

Pour commencer, nous configurons un service `super-app-db` qui récupère une image Docker de MySQL avec la version 8.0.28. 

Ensuite, nous instruisons le conteneur de créer une base de données nommée `super-app` avec `root` comme utilisateur par défaut et son mot de passe défini sur _$SuperApp1_. 

Enfin, puisque le port par défaut pour MySQL est 3306, nous le mappons au port 3306 du conteneur et exposons ce port pour l'accès.

Une fois le fichier ci-dessus créé, exécutez la commande suivante pour créer votre image Docker et l'exécuter en tant que conteneur.

    docker compose up

L'image MySQL sera téléchargée, puis Docker lancera un conteneur pour exécuter cette image. Le serveur MySQL peut être vérifié en s'y connectant via un client MySQL. 

Si ce n'est pas le cas, ne vous inquiétez pas, nous verrons ci-dessous comment s'y connecter via l'une de nos applications. Tant que le conteneur n'est pas supprimé, les tables seront persistées.

Configurons notre prochaine application NodeJS.

### Comment configurer NodeJS

Nous allons créer une application Node Express très simple. Pour ce faire, créez un dossier nommé node dans notre dossier super-app. 

Ajoutez les fichiers server.js, package.json et Dockerfile dans le dossier node.

server.js :

    const server = require("express")();
    server.listen(3000, async () => { });
    server.get("/super-app", async (_, response) => {
        response.json({ "super": "app" });
    });

package.json :

    {
        "name": "super-app-node",
        "dependencies": {
            "express": "^4.17.1"
        }
    }

Dockerfile :

    # Télécharger la version slim de node
    FROM node:17-slim

    # Définir le répertoire de travail sur le dossier app. 
    # Nous allons copier notre code ici
    WORKDIR /node

    # Copier le fichier package.json dans le dossier node à l'intérieur du conteneur
    COPY package.json .

    # Installer les dépendances dans le conteneur
    RUN npm install

    # Copier le reste du code dans le conteneur
    COPY . .

    # Exécuter le serveur node avec le fichier server.js
    CMD ["node", "server.js"]

    # Exposer le service sur le PORT 3000
    EXPOSE 3000

Ici, nous créons une application Node qui retourne du JSON lorsque nous accédons à localhost:3000/super-app dans le navigateur. Maintenant, nous n'allons pas exécuter directement le projet à partir de ce dossier.

Au lieu de cela, retournez à votre dossier super-app et ajoutez les lignes suivantes à votre fichier docker-compose.yml :

      super-app-node:
        build: ./node
        ports:
          - "3000:3000"

Nous mentionnons simplement de créer un service nommé super-app-node. Nous mappons également le port du conteneur au port hôte 3000. 

Enfin, exécutez la commande suivante pour exécuter vos deux conteneurs (MySQL et NodeJS) :

    docker compose up

Maintenant, si vous accédez à localhost:3000/super-app, vous verrez une réponse {"super":"app"}. Simultanément, votre service MySQL est également en cours d'exécution. Hourra ! Nous avons réussi à créer deux conteneurs en utilisant un fichier docker compose.

Passons à l'application suivante. Créons une application .NET qui interagit avec la base de données et retourne une liste de chaînes.

### Comment configurer .NET 6.0

Nous voulons que l'application .NET se connecte à la base de données. Elle récupérera des données de la base de données via une API GET et les affichera dans le navigateur. 

Pour ce faire, créez un dossier nommé dotnet dans notre projet super-app.

### Comment configurer le projet

Pour commencer, installez le [SDK .NET 6.0](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) si vous ne l'avez pas déjà installé. Exécutez la commande suivante pour créer une nouvelle application dotnet :

    dotnet new webapi --name dotnet

Il créera un nouveau projet .NET avec des contrôleurs et quelques autres fichiers. Afin de supporter la connexion à MySQL, nous devons ajouter un package nuget. Nous ajouterons également Microsoft.EntityFrameworkCore qui est essentiellement un ORM pour se connecter à la base de données. 

Pour ce faire, exécutez les commandes suivantes dans le projet .NET nouvellement créé :

    dotnet add package Pomelo.EntityFrameworkCore.MySql --version 6.0.1
    dotnet add package Microsoft.EntityFrameworkCore --version 6.0.4
    dotnet add package Microsoft.EntityFrameworkCore.Design --version 6.0.4

Puisque nous n'avons plus besoin du fichier WeatherForecast.cs, vous pouvez le supprimer. Au lieu de cela, créez deux autres entités dans Job.cs et User.cs comme suit :

    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;

    namespace dotnet;
    public class User
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        public string FirstName { get; set; }
    }


    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;

    namespace dotnet;
    public class Job
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        public string Name { get; set; }
        public int UserId { get; set; }
        [ForeignKey("UserId")]
        public virtual User User { get; set; }
    }

Nous aurons également besoin d'une sous-classe DbContext pour accéder à ces entités. Créez un fichier nommé MySQLDBContext.cs et ajoutez le contenu suivant :

    using Microsoft.EntityFrameworkCore;

    namespace dotnet;
    public class MySQLDBContext : DbContext
    {
        public DbSet<User> User { get; set; }
        public DbSet<Job> Job { get; set; }
        public MySQLDBContext(DbContextOptions<MySQLDBContext> options) : base(options) { }
    }

Nous voulons configurer .NET pour utiliser cette classe DbContext pour le mappage O/RM. Naviguez vers votre fichier Program.cs et remplacez ce qui s'y trouve par le contenu suivant :

    using dotnet;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.EntityFrameworkCore;
    using Microsoft.Extensions.Hosting;
    using Microsoft.Extensions.Configuration;

    var builder = WebApplication.CreateBuilder(args);

    // Ajouter des services au conteneur.
    builder.Services.AddDbContext<MySQLDBContext>(options =>
        {
        var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
        options.UseMySql(connectionString, ServerVersion.AutoDetect(connectionString));
        });

    builder.Services.AddControllers();
    // En savoir plus sur la configuration de Swagger/OpenAPI à l'adresse https://aka.ms/aspnetcore/swashbuckle
    builder.Services.AddEndpointsApiExplorer();
    builder.Services.AddSwaggerGen();

    var app = builder.Build();

    // Configurer le pipeline de requête HTTP.
    if (app.Environment.IsDevelopment())
    {
        app.UseSwagger();
        app.UseSwaggerUI();
    }

    // Supprimer cette ligne
    // app.UseHttpsRedirection();

    app.UseAuthorization();

    app.MapControllers();

    app.Run();

Les applications dans les conteneurs n'ont pas besoin de redirection HTTPS. Puisque le HTTPS doit être géré par le serveur, supprimez la ligne `app.UseHtttpsRedirecttion();` de Program.cs : 

Note : depuis .NET 6.0, le fichier Startup.cs est supprimé et à la place Program.cs est utilisé pour toutes les configurations.

Puisque nous utilisons une configuration qui récupère la DefaultConnection à partir des ConnectionStrings, nous devrons l'ajouter à notre fichier appsettings. 

Pour ce faire, définissez le contenu des fichiers appsettings.development.json et appsettings.json comme suit. Veuillez noter que nous utilisons super-app-db comme nom de serveur puisque c'est le nom de notre conteneur MySQL.

    {
      "Logging": {
        "LogLevel": {
          "Default": "Information",
          "Microsoft": "Warning",
          "Microsoft.Hosting.Lifetime": "Information"
        }
      },
      "AllowedHosts": "*",
      "ConnectionStrings": {  
        "DefaultConnection": "server=super-app-db; port=3306; database=super-app; user=root; password=$SuperApp1; Persist Security Info=False; Connect Timeout=300"  
      } 
    }super-app-db

Ensuite, nous allons créer une API GET qui retourne une liste d'objets Job dans la base de données. Pour ce faire, supprimez le fichier WeatherForecastController.cs et ajoutez un fichier UserController.cs avec le contenu suivant.

    using System.Collections.Generic;
    using System.Linq;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.EntityFrameworkCore;

    namespace dotnet.Controllers
    {
        [Route("api/[controller]")]
        [ApiController]
        public class JobController : Controller
        {
            private MySQLDBContext _dbContext;  

            public JobController(MySQLDBContext context)  
            {  
                _dbContext = context;  
            }  

            [HttpGet]  
            public IList<Job> Get()  
            {  
                return (this._dbContext.Job.Include(x => x.User).ToList());  
            } 
        }
    }

Nous sommes prêts côté code. Mais nous devons encore configurer notre base de données. Pour ce faire, nous allons créer une table User et Job dans notre base de données super-app.

### Outil EF .NET

L'Entity Framework Core de .NET fournit un moyen très pratique de le réaliser. Installez d'abord l'outil CLI dotnet-ef en exécutant la commande suivante :

    dotnet tool install --global dotnet-ef

Une fois installé, nous utiliserons une approche code first et créerons une migration de nos entités qui sera ensuite poussée vers notre base de données.

    dotnet ef migrations add InitialCreate
    dotnet ef database update

Les deux instructions ci-dessus, une fois exécutées, créeront la base de données, les tables à l'intérieur et configureront également la relation entre les deux tables.

### Comment ajouter des données à MySQL

Afin de récupérer des données de la base de données, nous devons d'abord ajouter des données dans les tables. Installez un client MySQL pour vous connecter à la base de données. Mon préféré est [DBeaver](https://dbeaver.io/). 

Maintenant, vous pouvez ajouter des données à partir de DBeaver en ajoutant d'abord une connexion avec des détails comme Host=super-app-db, Port=3306, User=root & password=$SuperApp1.

Une fois connecté, naviguez vers la base de données super-app, ouvrez la table User, ajoutez une ligne et enregistrez les données. De même, naviguez vers la table Job, ajoutez une ligne et enregistrez les données. Notre base de données est maintenant prête.

#### Comment configurer Docker

Une fois le projet configuré et en cours d'exécution, il est temps de le configurer pour qu'il s'exécute dans Docker en utilisant Dockerfile et docker compose. 

Dans le dossier dotnet, créez un Dockerfile avec le contenu suivant :

    # Obtenir l'image SDK pour construire et publier le projet
    FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env
    WORKDIR /app

    # Copier tout
    COPY . ./

    # Restaurer en couches distinctes
    RUN dotnet restore

    # Construire et publier une version
    RUN dotnet publish -c Release -o out

    # Construire l'image runtime
    FROM mcr.microsoft.com/dotnet/aspnet:6.0
    WORKDIR /app

    # Copier le fichier de construction dans le répertoire de l'application
    COPY --from=build-env /app/out .
    ENTRYPOINT ["dotnet", "dotnet.dll"]

    # Exposer le port pour la communication
    EXPOSE 80

Retournez maintenant au fichier docker-compose.yml et ajoutez le contenu suivant :

      super-app-dotnet:
        build: ./dotnet
        ports:
        - "8080:80"

Ici, nous relions le port 8080 de la machine hôte au port 80 du conteneur. C'est tout pour l'instant. Exécutez la commande suivante pour démarrer tous les conteneurs :

    docker compose up

Enfin, accédez à [localhost:8080/api/job](http://127.0.0.1:8080/api/job) dans un navigateur. L'API GET récupérera la liste des jobs de la base de données.

### Comment configurer Python avec Docker

À ce stade, vous avez probablement deviné que nous allons devoir créer un dossier python dans notre dossier super-app 😊. 

Deuxièmement, créez les trois fichiers nécessaires pour notre projet : ai-ml.py, requirements.txt et Dockerfile avec le contenu suivant :

ai-ml.py :

    import matplotlib.pyplot as plt
    import pandas as pd
    from scipy import signal

    if __name__ == "__main__":
        print("All working good")

requirements.txt :

    pandas
    scipy
    matplotlib

Dockerfile :

    # Obtenir l'image python
    FROM python:3.7.13-slim

    # Passer au répertoire de l'application
    WORKDIR /app

    # Copier les exigences dans l'application
    COPY requirements.txt ./

    # Installer les dépendances
    RUN pip install --no-cache-dir -r requirements.txt

    # Copier le reste
    COPY . .

    # Exécuter le script python
    CMD [ "python", "./ai-ml.py" ]

Enfin, retournez au fichier docker-compose.yml et ajoutez le contenu suivant :

      super-app-python:
        build: ./python

C'est aussi simple que cela. Puisqu'il s'agit simplement d'un script simple, il s'exécutera une fois puis le conteneur se fermera. Mais les logs du conteneur montreront _All working good_ imprimé. C'est tout pour Python.

### Comment configurer PHP avec Docker

Configurer PHP avec Docker est l'une des parties les plus faciles de toutes. Créez deux fichiers index.php et Dockerfile comme suit :

index.php :

    <?php echo "I am running in a container."; ?>

Dockerfile :

    # Obtenir l'image php apache
    FROM php:8.0-apache

    # Passer au répertoire de l'application
    WORKDIR /var/www/html

    # Copier tout
    COPY . .

    EXPOSE 80

Enfin, ajoutez le contenu suivant à docker-compose.yml.

      super-app-php:
        build: ./php
        ports:
        - "8000:80"

Enfin, démarrez tous les conteneurs à nouveau avec `docker compose up`. Lorsque vous accédez à [http://localhost:8000](http://localhost:8000), un joli message disant _"I am running in a container."_ apparaîtra.

Voici le dépôt [final](https://github.com/shenanigan/super-app-docker) avec tous les Dockerfiles et autres informations de configuration.

## Conclusion

Docker est un outil de conteneurisation merveilleux et il a été rendu plus puissant avec docker compose. Il vous permet d'exécuter plusieurs conteneurs côte à côte sans interférer les uns avec les autres. Vous devriez définitivement l'avoir dans votre arsenal d'outils.

Comment avez-vous aimé l'article ? Quels autres cas d'utilisation pouvez-vous imaginer pour Docker ? Des commentaires ou des suggestions ?

Si vous commencez avec Docker, vous pouvez en savoir plus à ce sujet [ici](https://arjavdave.com/2022/04/12/docker-introduction-and-cheat-sheet/).