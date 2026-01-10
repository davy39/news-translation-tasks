---
title: Comment construire une SPA avec Vue.js et C# en utilisant .NET Core
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2020-09-15T19:14:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-spa-with-vuejs-and-c-using-net-core
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/dashboard-1.png
tags:
- name: C
  slug: c
- name: C#
  slug: csharp
- name: ' Single Page Applications '
  slug: single-page-applications
- name: Vue.js
  slug: vuejs
seo_title: Comment construire une SPA avec Vue.js et C# en utilisant .NET Core
seo_desc: 'Let''s say you are a front-end developer. Or you have just had to work
  more with the front end recently.

  Now and then you have used some back-end technologies, but you''ve always stayed
  in your comfort zone, perhaps in the JavaScript world. Or maybe yo...'
---

Disons que vous êtes un développeur front-end. Ou que vous avez récemment dû travailler davantage avec le front-end.

De temps en temps, vous avez utilisé certaines technologies back-end, mais vous êtes toujours resté dans votre zone de confort, peut-être dans le monde JavaScript. Ou peut-être avez-vous construit une petite API avec Python.

Mais vous n'avez jamais touché à la pile technologique moderne de la famille .NET.

Ce tutoriel vous guidera, étape par étape, dans la construction d'une application monopage moderne (SPA) qui tirera parti de [Vue.js](https://vuejs.org/) pour le front-end et de [.NET Core (C#)](https://docs.microsoft.com/en-us/dotnet/core/get-started?tabs=windows) pour le back-end.

Nous verrons également comment écrire quelques tests, à la fois unitaires et d'intégration, pour couvrir les fonctionnalités front-end et back-end (au moins partiellement).

Si vous souhaitez sauter la lecture, voici le dépôt GitHub avec un [README](https://github.com/mihailgaberov/pizza-app/blob/master/README.md) détaillé.

## Que allons-nous construire

🤝 Nous allons construire une application web où les utilisateurs peuvent s'inscrire/se connecter et nous dire à quel point ils aiment les pizzas, en appuyant sur un bouton "J'adore".

Il n'y a pas de restrictions sur le nombre de fois où chaque utilisateur peut montrer son appréciation. La seule exigence est que seuls les utilisateurs connectés peuvent voter.

Sur la page d'accueil, avec les boutons d'inscription/connexion, nous mettrons un petit graphique à barres, affichant les X meilleurs utilisateurs avec la plus grande appréciation (sur l'axe X) et le nombre de votes sur l'axe Y.

## Installation

Commençons par le front-end. Il est plus logique de construire d'abord les parties visibles de notre application. Nous construirons notre front-end avec l'une des bibliothèques front-end les plus célèbres sur le marché : Vue.js.

### Comment configurer le front-end

Pour installer et configurer notre configuration initiale de front-end avec Vue.js, nous utiliserons le [Vue CLI](https://cli.vuejs.org/). Il s'agit d'un outil standard en ligne de commande pour développer des applications Vue.js.

Pour l'installer, utilisez la commande suivante. Notez que toutes les commandes de ce tutoriel utilisent [NPM](https://www.npmjs.com/), que vous devez avoir installé sur votre machine pour suivre.

```bash
npm install -g @vue/cli
```

Après avoir installé avec succès le Vue CLI, nous devrions pouvoir commencer à l'utiliser pour installer et configurer Vue.js lui-même. Faisons-le avec le processus suivant.

Étape 1 : Créez un nouveau répertoire de projet vide et ouvrez-le avec les commandes suivantes :

```python
mkdir pizza-app
cd pizza-app
```

Étape 2 : Dans la racine du projet, exécutez ce qui suit :

```bash
vue create frontend
```

Puis, parmi les options fournies, sélectionnez les suivantes :

* Sélection manuelle des fonctionnalités

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-52.png align="left")

*Installation de Vue.js - Sélection manuelle des fonctionnalités*

* Babel

* Routeur

* Préprocesseurs CSS (SASS)

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-53.png align="left")

*Installation de Vue.js - sélection des fonctionnalités*

Puis sélectionnez la version 2.x à partir de l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-54.png align="left")

*Sélectionner la version 2.x*

Ensuite, sélectionnez 'Utiliser le mode historique pour le routeur ?' et 'Sass/SCSS (avec node-sass)', comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-57.png align="left")

* Linter / Formateur

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-58.png align="left")

* Tests unitaires avec Jest

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-59.png align="left")

* Tests E2E avec Cypress

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-60.png align="left")

Après cette dernière étape, terminez le processus d'installation avec les options par défaut.

Nous sommes maintenant prêts à exécuter l'application en utilisant les commandes suivantes à partir du dossier racine du projet :

```bash
cd frontend
npm run serve
```

Une fois l'application en cours d'exécution, vous pouvez la voir dans votre navigateur sur http://localhost:8080 :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/welcome-to-your-vuejs-app.png align="left")

*Écran d'installation par défaut de Vue.js*

Avant de continuer avec la construction des composants réels que notre application front-end aura, installons notre application back-end via le CLI .NET Core.

### Comment configurer le back-end

Comme mentionné ci-dessus, nous utiliserons un autre outil en ligne de commande, le CLI .NET Core, qui nous donne la possibilité de créer et de configurer des applications .NET.

Si vous ne l'avez pas déjà, vous pouvez utiliser [ce lien](https://dotnet.microsoft.com/download/dotnet-core/thank-you/sdk-3.1.401-windows-x64-installer) pour le télécharger et l'installer.

Une fois que vous avez installé l'outil CLI .NET Core, allez dans le répertoire racine de votre projet et exécutez la commande suivante pour créer notre application back-end. Ainsi, nous créerons un dossier appelé `backend` et installerons une application web .NET à l'intérieur :

```python
dotnet new web -o backend
```

### gitignore.io

Avant de continuer avec l'installation des prochains packages dont nous aurons besoin, occupons-nous de notre fichier *.gitignore*.

Il s'agit d'un fichier de configuration qui indique à [Git](https://git-scm.com/) quoi ignorer lors de la validation des modifications dans les dépôts basés sur Git (ceux dans [GitHub](https://github.com/)).

Puisque nous voulons avoir un seul fichier .*gitignore*, il inclura des règles pour deux types d'applications :

* une application basée sur Node.js, qui est notre front-end Vue.js, et

* une application .NET (C#) qui est notre back-end.

Pour cela, nous utiliserons un outil appelé [*gitignore.io*](https://www.toptal.com/developers/gitignore)*.* Cet outil générera de tels fichiers pour nous. L'avantage d'utiliser cet outil est qu'il nous permet de taper nos langages/platformes de programmation, et il génère le fichier .gitignore pour nous.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-61.png align="left")

*Utiliser gitignore.io pour générer un fichier .gitignore*

De plus, en haut du fichier généré, il enregistre des liens pour la création ou l'édition ultérieure, comme montré ci-dessous.

```python

# Créé par https://www.toptal.com/developers/gitignore/api/webstorm,vue,vuejs,visualstudio
# Éditer à https://www.toptal.com/developers/gitignore?templates=webstorm,vue,vuejs,visualstudio
```

Nous sommes maintenant prêts à continuer avec le reste des packages que nous devons installer.

Tout d'abord, nous installerons un package appelé SpaServices, qui nous permettra d'avoir notre application fonctionnant via une seule URL, et pointant vers l'application .NET. De son côté, elle redirigera les requêtes vers notre application front-end.

Pour l'installer, ouvrez votre terminal, allez dans le dossier `backend` de votre projet, et exécutez ce qui suit :

```bash
dotnet add package Microsoft.AspNetCore.SpaServices.Extensions --version 3.1.8
```

Après cela, nous devons configurer notre application back-end avec le package SpaServices afin d'obtenir le résultat souhaité.

Chaque requête ira à notre application back-end .NET, et si la requête est destinée au front-end, elle la redirigera.

Pour ce faire, ouvrez le fichier [Startup.cs](https://github.com/mihailgaberov/pizza-app/blob/master/backend/Startup.cs) et mettez à jour son contenu pour qu'il soit comme ceci :

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;

namespace backend
{
    public class Startup
    {
        public IConfiguration Configuration { get; }

        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        // Cette méthode est appelée par le runtime. Utilisez cette méthode pour ajouter des services au conteneur.
        // Pour plus d'informations sur la façon de configurer votre application, visitez https://go.microsoft.com/fwlink/?LinkID=398940
        public void ConfigureServices(IServiceCollection services)
        {
            string connectionString = Configuration.GetConnectionString("DefaultConnection");
            services.AddDbContext<ApplicationDbContext>(options => options.UseSqlite(connectionString));
            services.AddSpaStaticFiles(configuration: options => { options.RootPath = "wwwroot"; });
            services.AddControllers();
            services.AddCors(options =>
            {
                options.AddPolicy("VueCorsPolicy", builder =>
                {
                    builder
                    .AllowAnyHeader()
                    .AllowAnyMethod()
                    .AllowCredentials()
                    .WithOrigins("https://localhost:5001");
                });
            });
            services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
  .AddJwtBearer(options =>
                {
                    options.Authority = Configuration["Okta:Authority"];
                    options.Audience = "api://default";
                });
            services.AddMvc(option => option.EnableEndpointRouting = false);
        }

        // Cette méthode est appelée par le runtime. Utilisez cette méthode pour configurer le pipeline de requêtes HTTP.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env, ApplicationDbContext dbContext)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseCors("VueCorsPolicy");

            dbContext.Database.EnsureCreated();
            app.UseAuthentication();
            app.UseMvc();
            app.UseRouting();
            app.UseEndpoints(endpoints => { endpoints.MapControllers(); });
            app.UseSpaStaticFiles();
            app.UseSpa(configuration: builder =>
            {
                if (env.IsDevelopment())
                {
                    builder.UseProxyToSpaDevelopmentServer("http://localhost:8080");
                }
            });
        }
    }
}
```

✨ C'est la version finale du fichier Startup.cs et c'est pourquoi vous avez probablement remarqué plus de choses dedans. Nous y reviendrons un peu plus tard dans ce tutoriel.

À ce stade, vous devriez être en mesure d'exécuter votre application back-end. Si vous souhaitez le faire, exécutez les commandes suivantes à partir du dossier racine de votre projet :

```python
cd backend
dotnet run
```

## Comment configurer l'authentification

Comme vous vous en souvenez peut-être de la description au début, notre application devrait avoir une option d'inscription/connexion.

Pour répondre à cette exigence, nous utiliserons un service tiers appelé [Okta](https://www.okta.com/). Nous installerons les packages nécessaires pour utiliser le SDK Okta à la fois sur le front-end et le back-end de notre application.

Mais avant cela, vous devez créer un compte sur leur [site web](https://developer.okta.com/) et obtenir l'accès à leur panneau d'administration. À partir de là, vous pouvez créer une nouvelle application. Voici à quoi cela ressemble sur le mien :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-62.png align="left")

Commençons maintenant par le package dont nous avons besoin pour notre front-end. À partir du dossier racine, exécutez les commandes suivantes :

```bash
cd frontend
npm i @okta/okta-vue
```

Après cette étape, nous sommes prêts à modifier notre application Vue.js afin de tirer parti du SDK Okta.

Nous installerons également un autre package, appelé [BootstrapVue](https://bootstrap-vue.org/), qui fournit un ensemble de composants Vue.js prêts à l'emploi et esthétiques. Cela nous aidera à gagner du temps de développement et nous obtiendrons également un front-end attrayant.

Pour l'installer, exécutez ce qui suit à partir de votre dossier `frontend` :

```bash
npm i vue bootstrap-vue bootstrap
```

### Comment configurer le routeur

Il est temps de faire un peu de codage. Nous devons modifier notre [routeur](https://router.vuejs.org/) afin d'appliquer ce qui provient des services d'authentification Okta.

Vous pouvez voir le [fichier complet](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/src/router/index.js) dans mon dépôt GitHub, mais voici la partie essentielle que vous devez configurer avec vos propres détails (que vous avez obtenus lorsque vous vous êtes inscrit sur le site web du développeur Okta) :

```javascript
Vue.use(Auth, {
  issuer: 'https://dev-914982.okta.com/oauth2/default',
  client_id: '0oatq53f87ByM08MQ4x6',
  redirect_uri: 'https://localhost:5001/implicit/callback',
  scope: 'openid profile email'
})

....

router.beforeEach(Vue.prototype.$auth.authRedirectGuard())
```

### Écran d'accueil

Après avoir configuré notre routeur, nous pouvons enfin apporter quelques modifications à l'écran d'accueil de notre application, qui sera effectivement visible pour nos utilisateurs.

Ouvrez le fichier [App.vue](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/src/App.vue) dans votre IDE et modifiez son contenu comme suit :

```javascript
<template>
  <div id="app">
    <header>
      <b-navbar toggleable="md" type="light" variant="light">
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-navbar-brand to="/">Love Pizza</b-navbar-brand>
        <b-collapse is-nav id="nav-collapse">
          <b-navbar-nav>
            <b-nav-item href="#" @click.prevent="login" v-if="!user">Login</b-nav-item>
            <b-nav-item href="#" @click.prevent="logout" v-else>Logout</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </header>
    <main>
      <div>
        Love pizza button and clicks counter here
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      user: null
    }
  },
  async created() {
    await this.refreshUser()
  },
  watch: {
    '$route': 'onRouteChange'
  },
  methods: {
    login() {
      this.$auth.loginRedirect()
    },
    async onRouteChange() {
      await this.refreshUser()
    },
    async refreshUser() {
      this.user = await this.$auth.getUser()
    },
    async logout() {
      await this.$auth.logout()
      await this.refreshUser()
      this.$router.push('/')
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
```

À ce stade, votre application pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-173.png align="left")

*Application front-end Vue.js - travail en cours*

**Note** : Ne soyez pas confus par le texte 'Pizza button and clicks counter here'. Lors de la construction d'interfaces utilisateur, il est bon de laisser de tels espaces réservés pour les composants qui doivent être développés à l'avenir.

Dans notre cas, c'est là que nous ajouterons les composants responsables du bouton 'J'adore' et du compteur plus tard. Ils montreront le nombre de votes par utilisateur.

```javascript
<main>
  <div>
  	Love pizza button and clicks counter here
  </div>
</main>
```

### Authentification sur le back-end

À ce stade, nous avons configuré notre front-end pour tirer parti du service d'authentification fourni par Okta. Mais pour avoir une image complète prête à l'emploi, nous devons faire de même dans notre application back-end.

C'est de là que nous effectuerons des appels HTTP pour communiquer avec la base de données. Et, comme vous le verrez plus tard, certains de ces appels devront être authentifiés pour réussir.

Commençons à nouveau par installer quelques packages qui faciliteront notre travail. Dans votre terminal, allez dans votre répertoire `backend` et exécutez ce qui suit :

```bash
dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer --version 3.1.8
dotnet add package Microsoft.Extensions.Configuration --version 3.1.7
```

Ensuite, nous avons besoin d'un autre package qui nous aidera à configurer notre base de données. Nous utiliserons la base de données SQLite qui est super facile à utiliser dans la configuration .NET Core.

Toujours dans le dossier `backend`, exécutez :

```bash
dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version 2.1.1
```

Une fois les installations terminées, assurez-vous d'avoir le contenu complet du fichier [Startup.cs](https://github.com/mihailgaberov/pizza-app/blob/master/backend/Startup.cs) (et si ce n'est pas le cas, faites-le maintenant).

### PizzaVotesApiService

OK tout le monde, nous avons configuré à la fois nos front-end et back-end pour supporter l'authentification. Nous avons ajouté SQLite comme base de données à utiliser pour stocker les votes des utilisateurs. Et nous avons une version initiale de notre écran d'accueil.

Il est maintenant temps d'implémenter un service sur le front-end qui nous permettra de consommer l'API de notre back-end.

Bon travail jusqu'à présent ! ✨

Avant de pouvoir faire des appels HTTP depuis notre application front-end vers notre application back-end, nous devons installer un autre package dans notre application Vue.js. Il s'agit de [axios](https://www.npmjs.com/package/axios) et il nous donne la possibilité de faire des [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) depuis le navigateur, ce qui est exactement ce dont nous avons besoin.

Ouvrez votre terminal, allez dans le `frontend` de votre projet, et exécutez :

```python
npm i axious
```

Ensuite, dans votre IDE, allez dans le dossier `src` de votre application front-end, créez un nouveau fichier .js, et ajoutez ce qui suit à l'intérieur :

```python
import Vue from 'vue'
import axios from 'axios'

const client = axios.create({
    baseURL: 'http://localhost:5000/api/pizzavotes',
    json: true
})

export default {
    async execute(method, resource, data) {
        const accessToken = await Vue.prototype.$auth.getAccessToken()
        return client({
            method,
            url: resource,
            data,
            headers: {
                Authorization: `Bearer ${accessToken}`
            }
        }).then(req => {
            return req.data
        })
    },
    getAll() {
        return this.execute('get', '/')
    },
    getById(id) {
        return this.execute('get', `/${id}`)
    },
    create(data) {
        return this.execute('post', '/', data)
    },
    update(id, data) {
        return this.execute('put', `/${id}`, data)
    },
}
```

J'ai nommé le mien [PizzaVotesApiService.js](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/src/PizzaVotesApiService.js). Nous allons arrêter l'intégration de l'API pour un moment et créer un autre composant qui contiendra les contrôles que les utilisateurs utiliseront pour interagir avec cette API.

### Composant Dashboard

Dites bonjour à notre composant [Dashboard.vue](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/src/components/Dashboard.vue).

C'est ici que nous mettrons le bouton "J'adore" et un petit compteur de votes.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-63.png align="left")

*Bouton "J'adore" et compteur de votes*

Nous ajouterons également une belle image de pizza.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-64.png align="left")

*Image de pizza*

Ainsi qu'un beau graphique à barres, montrant les X meilleurs votants.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-65.png align="left")

*Graphique à barres des meilleurs votants*

Vous pouvez copier et coller le contenu complet du fichier depuis mon dépôt afin que nous puissions continuer avec l'intégration de l'ensemble.

### Intégration de l'API

Je vais utiliser un petit diagramme pour décrire le flux de données. Comme on dit, "une image vaut mille mots" :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/data-flow.png align="left")

*Diagramme de flux de données*

Comme vous pouvez le voir (je l'espère 😉) à partir du diagramme, lorsque l'utilisateur entre ses votes, les données passent du composant du tableau de bord à travers le service API que nous avons créé pour communiquer avec l'API back-end. Elles atteignent ensuite le contrôleur back-end qui effectue effectivement les appels HTTP.

Une fois les données récupérées, le service les renvoie à notre interface utilisateur où nous les affichons via nos composants Vue.js. Comme vous le verrez, il y a une logique supplémentaire qui vérifie si l'utilisateur est authentifié afin de savoir quels appels exécuter.

Voici l'implémentation du [contrôleur](https://github.com/mihailgaberov/pizza-app/blob/master/backend/PizzaVotesController.cs) lui-même :

```c#
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace backend.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PizzaVotesController : ControllerBase
    {
        private readonly ApplicationDbContext _dbContext;

        public PizzaVotesController(ApplicationDbContext dbContext)
        {
            _dbContext = dbContext;
        }

        // GET api/pizzavotes
        [HttpGet]
        public async Task<ActionResult<List<PizzaVotes>>> Get()
        {
            return await _dbContext.PizzaVotes.ToListAsync();
        }

        // GET api/pizzavotes/{email}
        [Authorize]
        [HttpGet("{id}")]
        public async Task<ActionResult<PizzaVotes>> Get(string id)
        {
            return await _dbContext.PizzaVotes.FindAsync(id);
        }

        // POST api/pizzavotes
        [Authorize]
        [HttpPost]
        public async Task Post(PizzaVotes model)
        {
            await _dbContext.AddAsync(model);
            await _dbContext.SaveChangesAsync();
        }

        // PUT api/pizzavotes/{email}
        [Authorize]
        [HttpPut("{id}")]
        public async Task<ActionResult> Put(string id, PizzaVotes model)
        {
            var exists = await _dbContext.PizzaVotes.AnyAsync(f => f.Id == id);
            if (!exists)
            {
                return NotFound();
            }

            _dbContext.PizzaVotes.Update(model);

            await _dbContext.SaveChangesAsync();

            return Ok();
        }
    }
}
```

Ici, nous avons quatre méthodes pour exécuter quatre opérations de base :

* obtenir tous les enregistrements de la base de données

* obtenir les enregistrements pour un utilisateur (par son adresse e-mail)

* créer un nouvel enregistrement utilisateur

* mettre à jour les enregistrements d'un utilisateur existant.

Vous avez probablement remarqué la clause `[Authorize]` ci-dessus dans trois des quatre méthodes. Ces méthodes nécessiteront que l'utilisateur soit authentifié pour s'exécuter.

Nous laisserons la méthode `GET api/pizzavotes` pour obtenir tous les enregistrements non autorisés intentionnellement. Puisque nous aimerions montrer le graphique à barres sur l'écran d'accueil à tous les utilisateurs, nous devrons être en mesure de faire cet appel, peu importe si l'utilisateur est authentifié ou non.

### Autoriser l'inscription

Une chose à noter : si vous souhaitez avoir un 'Inscription' sur votre écran de connexion, vous devez l'autoriser depuis le panneau d'administration Okta.

Une fois connecté, sélectionnez dans le menu **Utilisateurs->Inscription** :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-66.png align="left")

*Autoriser l'inscription pour les nouveaux utilisateurs*

### Terminer le back-end

Pour que votre application back-end devienne pleinement fonctionnelle, veuillez consulter [mon dépôt ici](https://github.com/mihailgaberov/pizza-app/tree/master/backend) et ajouter les fichiers manquants.

Si vous avez suivi jusqu'à ce point, vous devriez avoir les fichiers suivants (à l'exception du dossier `test`, car nous allons l'ajouter un peu plus tard) :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-67.png align="left")

*Structure de l'application back-end*

### Terminer le front-end

Pour finaliser le travail sur notre application front-end, nous créerons deux composants supplémentaires.

Le premier affichera le graphique à barres mentionné ci-dessus, et le second affichera l'adresse e-mail de l'utilisateur actuellement connecté.

Dans votre IDE, allez dans `frontend/src/components` et créez deux fichiers, nommés [Username.vue](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/src/components/Username.vue) et [VotesChart.vue](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/src/components/VotesChart.vue), respectivement.

Username.vue est un composant très court et simple qui prend l'adresse e-mail de l'utilisateur comme prop et la rend. Voici son implémentation :

```python
<template>
  <div class="username">{{ username }}</div>
</template>

<script>
export default {
  props: { username: String },
}
</script>

<style lang="scss">
.username {
  color: rebeccapurple;
  display: flex;
  align-items: center;
  justify-content: center;
}

.username::before {
  content: "";
}

.username::after {
  content: "";
}
</style>
```

La seule chose à noter ici est que nous utilisons SASS/SCSS pour les styles du composant. Cela est possible parce que nous avons choisi cette option au début (lorsque nous installions notre application Vue.js).

Pour dessiner le graphique, nous utiliserons un package appelé [vue-chartsjs](https://www.npmjs.com/package/vue-chartjs). Installez-le en exécutant la commande suivante à partir de votre dossier `frontend` :

```python
npm i vue-chartjs chart.js
```

Notre composant **VotesChart.vue** sera une sorte d'enveloppe pour le composant de graphique à barres qui provient du package vue-chartjs.

Nous l'utilisons pour obtenir les données du composant parent, **Dashboard.vue**, et les traiter.

Nous trions le tableau de données afin d'afficher nos meilleurs votants, triés du plus grand au plus petit nombre de votes. Ensuite, nous les passons au composant Bar chart pour les visualiser.

Voici l'implémentation complète :

```python
<script>
import { Bar } from 'vue-chartjs'

const TOP_N_VOTERS_TO_SHOW_ON_CHART = 10

// Utilisé pour trier par valeur de votes - du plus grand au plus petit (desc)
function sortByStartDate(nextUser, currentUser) {
  const nextVoteValue = nextUser.value
  const currentVoteValue = currentUser.value
  return currentVoteValue - nextVoteValue
}

export default {
  extends: Bar,
  props: { data: Array },

  watch: {
    data: async function (newVal) {
      const sortedVotes = Array.from(newVal).sort(sortByStartDate).slice(0, TOP_N_VOTERS_TO_SHOW_ON_CHART)
      this.labels = sortedVotes.map(user => user.id)
      this.values = sortedVotes.map(user => user.value)

      this.renderChart({
        labels: this.labels,
        datasets: [
          {
            label: 'Pizza Lovers',
            backgroundColor: '#f87979',
            data: this.values,
          }
        ]
      }, {
        scales: {
          yAxes: [{
            ticks: {
              stepSize: 1,
              min: 0,
              max: this.values[0]
            }
          }]
        }
      })
    }
  }
}
</script>
```

Notez qu'il y a une constante en haut du fichier qui définira combien de meilleurs votants nous aimerions montrer sur ce graphique. Actuellement, elle est définie à 10, mais vous pouvez la modifier comme vous le souhaitez.

Une fois que vous avez terminé avec toutes les choses front-end et que vous souhaitez exécuter l'application, vous pouvez le faire en :

Allant dans le dossier `frontend` et en exécutant :

```bash
npm run serve
```

Allant dans le dossier `backend` et en exécutant :

```bash
dotnet run
```

Ouvrant votre navigateur et allant sur https://localhost:5001.

## Comment tester nos applications

Jusqu'à présent, nous avons construit une application monopage moderne et entièrement fonctionnelle avec un back-end .NET Core et une base de données SQLite. C'est beaucoup de travail. Félicitations ! ✨

*Nous pourrions facilement nous arrêter ici et aller prendre une bière fraîche* 🍺.

Mais...

Nous sommes raisonnables pour savoir que si nous ne testons pas nos applications, nous ne pouvons pas garantir qu'elles fonctionneront comme prévu.

Nous savons également que si nous voulons rendre notre code testable, nous devons écrire de manière bien structurée, en gardant à l'esprit les [principes principaux de la conception logicielle](https://www.dotnettricks.com/learn/designpatterns/different-types-of-software-design-principles).

J'espère vous avoir convaincu de continuer à travailler sur ce tutoriel. Après tout, la seule chose qui nous reste à faire est d'écrire quelques tests pour nos deux applications. Alors faisons-le !

Nous couvrirons le fonctionnement de notre API back-end avec des **tests d'intégration**, et pour notre front-end, nous écrirons à la fois des tests **unitaires** et **d'intégration**.

### Tests unitaires et d'intégration

💡 Avant de passer au code, je voudrais dire quelques mots sur ces types de tests et répondre à certaines des questions les plus fréquemment posées.

Vous vous demandez peut-être, qu'est-ce que les tests unitaires ? Qu'est-ce que les tests d'intégration ? Pourquoi en avons-nous besoin ? Quand devons-nous utiliser chacun d'eux ?

En commençant par la première question, un **test unitaire** est un morceau de code qui teste la fonctionnalité d'un module encapsulé (signifiant un autre morceau). Il est écrit sous forme de fonction ou de bloc de code indépendant.

Ils sont bons à avoir, car ils vous donnent un retour rapide sur le temps de développement et protègent le code contre les régressions lorsque de nouvelles fonctionnalités sont ajoutées.

Les **tests d'intégration** sont utiles lorsque nous devons tester comment plusieurs modules/unités fonctionnent ensemble. Par exemple, une API REST et une interaction avec une base de données.

Selon la taille de l'application sur laquelle nous travaillons, nous pourrions avoir besoin uniquement de tests d'intégration. Mais parfois, nous avons besoin à la fois de tests d'intégration et unitaires pour protéger notre code.

Idéalement, nous devrions avoir les deux, car ils sont des parties essentielles de la pyramide de test et sont les moins chers à implémenter.

Mais dans certains cas, comme pour notre application back-end, seuls les tests d'intégration sont nécessaires pour couvrir la fonctionnalité qui mérite d'être testée. Nous n'avons que quelques méthodes API pour travailler avec la base de données.

### Comment créer nos tests back-end

Cette fois, nous commencerons par créer notre solution de test. Pour ce faire, vous devez faire quelques choses.

Tout d'abord, installez la bibliothèque xUnit en exécutant ce qui suit à partir du répertoire racine de votre projet :

```bash
dotnet add package xUnit
```

Ensuite, allez dans votre dossier `backend` et créez un dossier vide appelé `tests`. Ensuite, à l'intérieur de ce dossier, exécutez :

```bash
dotnet new xunit -o PizzaVotes.Tests
```

Une fois cela fait, ouvrez [backend.csproj](https://github.com/mihailgaberov/pizza-app/blob/master/backend/backend.csproj) et ajoutez les deux lignes suivantes au bloc `<PropertyGroup>` :

```python
<GenerateAssemblyInfo>false</GenerateAssemblyInfo>
<GenerateTargetFrameworkAttribute>false</GenerateTargetFrameworkAttribute>
```

Ensuite, allez dans votre dossier `tests` et installez les packages suivants :

```python
Microsoft.AspNetCore.Mvc
Microsoft.AspNetCore.Mvc.Core
Microsoft.AspNetCore.Diagnostics
Microsoft.AspNetCore.TestHost
Microsoft.Extensions.Configuration.Json
Microsoft.AspNetCore.Mvc.Testing
```

Vous faites cela en exécutant chacune des commandes suivantes dans votre application terminal :

```bash
dotnet add package Microsoft.AspNetCore.Mvc --version 2.2.0
dotnet add package Microsoft.AspNetCore.Mvc.Core --version 2.2.5
dotnet add package Microsoft.AspNetCore.Diagnostics --version 2.2.0
dotnet add package Microsoft.AspNetCore.TestHost --version 3.1.8
dotnet add package Microsoft.AspNetCore.Mvc.Testing --version 3.1.8
```

Après avoir tout installé, nous sommes prêts à procéder à l'écriture de quelques tests.

Comme vous pouvez le voir ici, en plus des tests eux-mêmes, j'ai ajouté deux fichiers supplémentaires dont nous avons besoin ou qu'il est bon d'avoir lors de l'exécution des tests.

L'un d'eux est simplement un [fichier d'aide](https://github.com/mihailgaberov/pizza-app/blob/master/backend/tests/PizzaVotes.Tests/ContentHelper.cs) avec une méthode pour gérer les objets sérialisés et obtenir le contenu de la chaîne. L'autre est le fichier [fixture](https://github.com/mihailgaberov/pizza-app/blob/master/backend/tests/PizzaVotes.Tests/TestFixture.cs), où nous avons des configurations et des paramètres pour notre serveur de test et notre client.

Et, bien sûr, il y a [un fichier](https://github.com/mihailgaberov/pizza-app/blob/master/backend/tests/PizzaVotes.Tests/PizzaVotesTests.cs) avec nos tests.

Je ne vais pas coller le contenu de ces fichiers ici, car ce tutoriel est déjà assez long.

**Vous pouvez simplement les copier depuis mon dépôt.**

Si vous regardez de plus près les tests, vous remarquerez peut-être que nous testons uniquement le premier appel non authentifié pour une réponse réussie. Le reste, nous vérifions uniquement la réponse HTTP 401, qui est `Non autorisé`.

C'est parce que seule la première méthode est publique, c'est-à-dire qu'elle n'a pas besoin d'authentification.

Si nous devions avoir les mêmes tests pour toutes les méthodes, nous aurions dû implémenter un middleware juste pour autoriser notre application de test devant les services d'authentification d'Okta.

Et puisque le but de ce tutoriel est d'apprendre une variété de choses, nous pourrions dire que cela ne vaut pas la peine de le faire.

Maintenant, la partie amusante : comment exécuter les tests. Il s'avère que c'est super simple. Allez simplement dans votre répertoire `tests` (où se trouve le fichier tests.sln) depuis votre terminal et exécutez :

```bash
dotnet test
```

Vous devriez voir quelque chose comme ceci dans votre terminal (ignorez les avertissements jaunes) :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-68.png align="left")

*Exécution des tests back-end*

### Comment créer nos tests front-end

Il est temps d'ajouter quelques tests à notre front-end. Ici, nous ferons à la fois des tests unitaires et d'intégration.

**Tests unitaires**

Comme je l'ai mentionné ci-dessus, les tests unitaires sont adaptés lorsque nous avons un module ou un composant qui n'a pas de dépendances du monde extérieur.

De tels composants s'avèrent être nos composants Username.vue et VotesChart.vue.

Ce sont des composants de représentation qui reçoivent les données dont ils ont besoin pour fonctionner correctement via des props. Cela signifie que nous pouvons écrire nos tests de la même manière : leur passer les données dont ils ont besoin et vérifier si les résultats de leur exécution sont ceux attendus.

Voici une chose importante à mentionner. Ce n'est pas que ce qui est fourni par le package **@vue/test-utils** (qui provient de l'installation de Vue.js) n'était pas suffisant pour tester les deux composants.

Plutôt, à des fins éducatives, j'ai décidé d'installer et d'utiliser également la [Vue Testing Library](https://testing-library.com/docs/vue-testing-library/intro). C'est pourquoi l'un des composants ci-dessous est testé avec @vue/test-utils, mais l'autre est testé avec @testing-library/vue.

N'oubliez pas de l'installer avant d'exécuter le test :

```python
npm i --save-dev @testing-library/vue
```

Encore une fois, pour économiser de l'espace, je ne vais pas coller le code des tests des composants ici, mais vous pouvez facilement le voir [ici](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/tests/unit/Username.spec.js) et [ici](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/tests/unit/VotesChart.spec.js).

Ensuite, pour exécuter les tests unitaires de votre application front-end, allez dans le dossier `frontend` et exécutez :

```python
npm run test:unit
```

**Test d'intégration**

Cela est probablement plus intéressant pour certains d'entre vous.

Si vous vous souvenez du début de ce tutoriel lorsque nous avons installé notre application Vue.js, pour notre solution de tests e2e (ou d'intégration), nous avons sélectionné [Cypress.js](https://www.cypress.io/).

Il s'agit d'un outil super facile à utiliser qui permet aux développeurs d'écrire de vrais tests e2e pour leurs applications en leur donnant un retour immédiat.

D'après mon expérience personnelle, je dirais que travailler avec Cypress est plus un plaisir qu'avec d'autres frameworks similaires. Si vous avez une expérience précédente avec des frameworks comme Nightwatch.js ou Selenium, ce que vous voyez ci-dessous pourrait vous être familier.

Avant d'exécuter nos tests avec Cypress, nous devons apporter quelques modifications mineures à sa configuration.

Trouvez le [fichier index](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/tests/e2e/plugins/index.js) sous le dossier `plugins` et ajoutez la ligne suivante à l'instruction return à la fin du fichier :

```python
  baseUrl: "https://localhost:5001"
```

Maintenant, mettez à jour le contenu du fichier test.js sous le dossier `specs` comme indiqué [ici](https://github.com/mihailgaberov/pizza-app/blob/master/frontend/tests/e2e/specs/test.js).

Une fois que vous avez tout fait, vous devriez être en mesure d'exécuter vos tests e2e via Cypress. Vous pouvez le faire en exécutant la commande suivante alors que vous êtes dans votre répertoire `frontend` :

```python
npm run test:e2e
```

⚡ N'oubliez pas de démarrer votre application back-end avant d'exécuter les tests e2e afin qu'ils fonctionnent correctement.

Si vous avez suivi, après avoir exécuté la commande ci-dessus, vous devriez voir quelque chose comme ceci dans votre terminal :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-69.png align="left")

*Exécution des tests e2e*

Et une nouvelle fenêtre de navigateur sera ouverte par Cyrpess.js lui-même, où vous pouvez utiliser l'interface utilisateur fournie pour voir et exécuter vos tests.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-70.png align="left")

*Interface utilisateur de Cypress.js*

Et lorsque tous les tests passent, vous êtes censé voir un écran comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-71.png align="left")

*Les tests e2e passent avec succès*

## Conclusion

Dans ce tutoriel, nous avons vu comment utiliser l'une des technologies les plus en vogue sur le marché, à la fois pour le front-end et le back-end.

Nous avons également appris comment les combiner correctement afin de construire une petite mais entièrement fonctionnelle application monopage avec support de base de données.

Enfin, nous avons également écrit des tests unitaires et d'intégration pour les deux extrémités.

Je crois que ce type d'exercice est bénéfique pour les lecteurs expérimentés et débutants, car il couvre beaucoup de choses différentes de manière étape par étape. Et vous terminez avec une application exemple fonctionnelle si vous avez terminé l'ensemble du processus.

Ce tutoriel s'est avéré beaucoup plus long que je ne le pensais initialement. Mais si vous l'avez fait entièrement, je vous admire 😊 ! Et j'espère que ce fut un plaisir pour vous de le lire, comme ce fut un plaisir pour moi de l'écrire.

🙏 Merci d'avoir lu ! 😊

## Ressources

Vous trouverez ci-dessous les liens qui m'ont été utiles d'une manière ou d'une autre lors de la rédaction de cet article.

https://consultwithgriff.com/spas-with-vuejs-aspnetcore/
[https://github.com/okta/okta-auth-dotnet](https://github.com/okta/okta-auth-dotnet)
[https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test](https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test)
[https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpresponsemessage?view=netcore-3.1](https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpresponsemessage?view=netcore-3.1)
[https://vue-test-utils.vuejs.org/guides/#testing-key-mouse-and-other-dom-events](https://vue-test-utils.vuejs.org/guides/#testing-key-mouse-and-other-dom-events)
[https://docs.cypress.io/guides/references/configuration.html#Options](https://docs.cypress.io/guides/references/configuration.html#Options)
[https://docs.cypress.io/guides/tooling/visual-testing.html#Functional-vs-visual-testing](https://docs.cypress.io/guides/tooling/visual-testing.html#Functional-vs-visual-testing)
[https://www.codingame.com/playgrounds/35462/creating-web-api-in-asp-net-core-2-0/part-3---integration-tests](https://www.codingame.com/playgrounds/35462/creating-web-api-in-asp-net-core-2-0/part-3---integration-tests)
[https://testing-library.com/docs/vue-testing-library/intro](https://testing-library.com/docs/vue-testing-library/intro)
https://www.valentinog.com/blog/canvas/