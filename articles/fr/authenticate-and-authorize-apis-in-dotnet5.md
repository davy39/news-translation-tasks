---
title: Sécurité des API – Comment authentifier et autoriser les API dans .NET 5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-31T21:22:23.000Z'
originalURL: https://freecodecamp.org/news/authenticate-and-authorize-apis-in-dotnet5
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/mask.jpg
tags:
- name: api
  slug: api
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Sécurité des API – Comment authentifier et autoriser les API dans .NET
  5
seo_desc: "By Arjav Dave\nIn my 11 years as a developer, I have seen so many API's\
  \ that have major security flaws. They either lack proper authentication or authorisation\
  \ or both. \nDevelopers might feel like everything's ok, since those endpoints are\
  \ usually not..."
---

Par Arjav Dave

En 11 ans en tant que développeur, j'ai vu tant d'API qui présentent de graves failles de sécurité. Elles manquent soit d'une authentification appropriée, soit d'une autorisation, soit des deux.

Les développeurs peuvent penser que tout va bien, puisque ces endpoints ne sont généralement pas publics. Mais c'est une énorme faille de sécurité que n'importe qui peut facilement exploiter.

Pour mieux comprendre la sécurité des API, créons un projet de démonstration pour le FBI. Il y aura un Admin qui peut enregistrer des Agents du FBI et modifier leurs niveaux d'habilitation.

Les Agents du FBI avec un _Niveau d'Habilitation 1_ pourront accéder aux fichiers publics, et les agents avec un _Niveau d'Habilitation 2_ pourront accéder aux fichiers publics et classifiés.

Mais avant de commencer, voici un peu de théorie.

## Comment fonctionne l'Authentification

Notre Agent a réussi tous ses examens ; il est temps de l'enregistrer. Pour ce faire, il fournira ses documents et recevra en retour son badge.

Dans le scénario ci-dessus, _fournir des documents_ est comme se connecter – une fois vérifié, l'agent recevra un token (badge). Ce processus est appelé _Authentification_. Il détermine si les agents sont bien ceux qu'ils prétendent être.

Nous allons utiliser des tokens JWT (JSON Web Tokens) Bearer pour l'authentification. Les _Bearer tokens_ sont un type de token généré par les serveurs, et qui contiennent des détails sur les revendications/rôles d'un utilisateur tentant de se connecter. Les Bearer tokens sont principalement des tokens structurés comme JWT. Vous pouvez [en savoir plus sur JWT ici](https://jwt.io/introduction) si vous souhaitez en apprendre davantage.

## Comment fonctionne l'Autorisation

Maintenant que l'Agent du FBI a obtenu son badge, il peut entrer dans le bâtiment du FBI. Il peut également accéder aux fichiers publics, mais lorsqu'il tente d'accéder aux fichiers classifiés, il obtient une [erreur 401](https://www.freecodecamp.org/news/http-401-error-vs-http-403-error-status-code-responses-explained/).

C'est parce que l'Agent du FBI n'est pas _autorisé_ à accéder aux fichiers classifiés. L'_Autorisation_ détermine ce que les agents peuvent et ne peuvent pas accéder.

Comme mentionné ci-dessus, le token JWT Bearer contient des revendications/rôles. Sur cette base, notre serveur décide d'accorder ou non l'accès à une ressource privée.

## Flux d'Accès

![Flux d'Accès](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y1pcf6w2cjhtj9hgzm8v.jpg)

Comme vous pouvez le voir dans le diagramme ci-dessus, lors d'une connexion réussie, le serveur retourne un Bearer token. Le client utilise le Bearer token dans les appels suivants pour accéder à une ressource privée.

Ce sont les deux concepts principaux que nous allons implémenter dans notre article.

Assez de théorie, montrez-moi du code !

## Comment Configurer notre Projet

Créez un nouveau projet en exécutant la commande **`dotnet new webapi --name FBI`** depuis votre CLI. Cela créera un projet avec une API WeatherForecast d'exemple.

Pourquoi travailler sur WeatherForecast alors que nous pouvons travailler sur le FBI ? Allez-y et supprimez le fichier `WeatherForecast.cs`.

Ajoutez les dépendances nécessaires en exécutant ces commandes :

```
dotnet add package Microsoft.IdentityModel.Tokens --version 6.9.0
dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer --version 5.0.4

```

Dans la fonction `ConfigureServices` de votre fichier `Startup.cs`, ajoutez le code suivant :

```
var TokenValidationParameters = new TokenValidationParameters
{
    ValidIssuer = "https://fbi-demo.com",
    ValidAudience = "https://fbi-demo.com",
    IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes("SXkSqsKyNUyvGbnHs7ke2NCq8zQzNLW7mPmHbnZZ")),
    ClockSkew = TimeSpan.Zero // supprime le délai du token à l'expiration
};

```

Nous définissons les paramètres pour valider un token. Assurez-vous que la longueur de la chaîne pour générer `SymmetricSecurityKey` est de 32.

Ensuite, configurez les services pour ajouter l'authentification pour les API comme ceci :

```
services
    .AddAuthentication(options =>
    {
        options.DefaultScheme = JwtBearerDefaults.AuthenticationScheme;
    })
    .AddJwtBearer(cfg =>
    {
        cfg.TokenValidationParameters = TokenValidationParameters;
    });

```

La méthode `AddAuthentication` enregistre les services requis par les services d'authentification. Elle configure également l'authentification JWT Bearer comme schéma par défaut.

`AddJwtBearer` active l'authentification JWT-bearer et définit les `TokenValidationParameters` définis ci-dessus.

Maintenant, ajoutons quelques revendications d'autorisation pour notre `Agent` et `Admin`.

```
services.AddAuthorization(cfg =>
    {
        cfg.AddPolicy("Admin", policy => policy.RequireClaim("type", "Admin"));
        cfg.AddPolicy("Agent", policy => policy.RequireClaim("type", "Agent"));
        cfg.AddPolicy("ClearanceLevel1", policy => policy.RequireClaim("ClearanceLevel", "1", "2"));
        cfg.AddPolicy("ClearanceLevel2", policy => policy.RequireClaim("ClearanceLevel", "2"));
    });

```

La méthode `AddAuthorization` enregistre les services requis pour l'autorisation. Nous ajoutons également des revendications pour `Admin`, `Agent`, `ClearanceLevel1` et `ClearanceLevel2` en appelant `AddPolicy`.

Une revendication est une paire nom-valeur qui représente ce que le sujet est. Puisque le niveau d'habilitation 2 peut également accéder au niveau d'habilitation 1, nous avons mis _"1", "2"_ dans ClearanceLevel1. Vous pouvez en savoir plus sur les revendications _[ici](https://docs.microsoft.com/en-us/aspnet/core/security/authorization/claims?view=aspnetcore-5.0)_.

Enfin, dans la méthode `Configure`, ajoutez la ligne suivante juste au-dessus de `app.UseAuthorization();` :

```
app.UseAuthentication();

```

## Le Fichier Admin Controller

Renommez votre fichier `WeatherForecastController.cs` en `AdminController.cs`. Changez également les noms de classe et de constructeur. Enfin, supprimez tout sauf le constructeur.

```
using Microsoft.AspNetCore.Mvc;

namespace FBI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class AdminController : ControllerBase
    {
        public AdminController() { }
    }
}


```

### Comment Configurer l'API de Connexion

Créons une API de connexion pour `Admin` afin qu'ils puissent obtenir un token pour effectuer d'autres tâches.

```
[HttpPost]
[Route("[action]")]
public IActionResult Login([FromBody] User User)
{
    // TODO: Authentifier Admin avec la Base de Données
    // Si non authentifié, retourner 401 Non Autorisé
    // Sinon, continuer avec le flux ci-dessous

    var Claims = new List<Claim>
            {
                new Claim("type", "Admin"),
            };

    var Key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes("SXkSqsKyNUyvGbnHs7ke2NCq8zQzNLW7mPmHbnZZ"));

    var Token = new JwtSecurityToken(
        "https://fbi-demo.com",
        "https://fbi-demo.com",
        Claims,
        expires: DateTime.Now.AddDays(30.0),
        signingCredentials: new SigningCredentials(Key, SecurityAlgorithms.HmacSha256)
    );

    return new OkObjectResult(new JwtSecurityTokenHandler().WriteToken(Token));
}

```

Dans le code ci-dessus, `User` est un modèle avec les propriétés `Username` et `Password`. Nous créons également un objet `JwtSecurityToken` en utilisant les configurations que nous avons utilisées dans notre fichier `Startup.cs`. Le token est ensuite converti en une chaîne et retourné dans un `OkObjectResult`.

Vous pouvez maintenant ouvrir Swagger et exécuter l'API pour voir un Bearer token. Un Bearer token sera retourné comme vous pouvez le voir ci-dessous.

![Réponse du Bearer Token](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/aedozuzics30gunpp3b5.png)

Gardez le token à portée de main puisque nous allons l'utiliser dans la section suivante. Vous pouvez également visiter [https://jwt.io](https://jwt.io) pour analyser votre token.

### Comment Générer l'API de Badge

Générer le badge pour un `Agent` est une tâche sensible et ne doit être autorisée que par un `Admin`. Nous allons ajouter un attribut `Authorize` pour l'API `GenerateBadge`.

```
[HttpPost]
[Route("[action]")]
[Authorize(Policy = "Admin")]
public IActionResult GenerateBadge([FromBody] Agent Agent)
{
    var Claims = new List<Claim>
    {
        new Claim("type", "Agent"),
        new Claim("ClearanceLevel", Agent.ClearanceLevel.ToString()),
    };

    var Key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes("SXkSqsKyNUyvGbnHs7ke2NCq8zQzNLW7mPmHbnZZ"));

    var Token = new JwtSecurityToken(
        "https://fbi-demo.com",
        "https://fbi-demo.com",
        Claims,
        expires: DateTime.Now.AddDays(30.0),
        signingCredentials: new SigningCredentials(Key, SecurityAlgorithms.HmacSha256)
    );

    return new OkObjectResult(new JwtSecurityTokenHandler().WriteToken(Token));
}
```

Ici, `Agent` est un modèle avec les propriétés `Name` en tant que chaîne et `ClearanceLevel` en tant qu'entier.

Maintenant, si vous retournez à Swagger et essayez d'exécuter l'API `GenerateBadge`, vous obtiendrez une réponse 401 Non Autorisé. Nous obtenons cette erreur parce que nous n'avons pas passé le Bearer token.

Pour pouvoir ajouter l'en-tête Authorize dans Swagger, modifiez `services.AddSwaggerGen` comme suit :

```
services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo { Title = "FBI", Version = "v1" });
    c.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
    {
        In = ParameterLocation.Header,
        Description = "Veuillez entrer le JWT avec Bearer dans le champ",
        Name = "Authorization",
        Type = SecuritySchemeType.ApiKey
    });
    c.AddSecurityRequirement(new OpenApiSecurityRequirement {
    { new OpenApiSecurityScheme
            {
                Reference = new OpenApiReference { Type = ReferenceType.SecurityScheme, Id = "Bearer"}
            },
        new string[] {}
    }
    });
});

```

Lorsque vous actualisez Swagger dans votre navigateur, vous remarquerez un bouton _Authorize_ sur le côté droit au-dessus de la liste des API.

Cliquez sur le bouton Authorize nouvellement ajouté dans Swagger, ce qui ouvrira une boîte de dialogue. Nous devons mentionner de quel type de token il s'agit. Entrez d'abord _Bearer_ dans le champ, puis un espace, puis le token généré à partir de l'API _/Admin/Login_ de la section précédente.

![En-tête d'Autorisation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5ks0jtoy39ogcpa61s71.png)

Cliquez sur l'en-tête pour verrouiller le token. Vous êtes maintenant prêt. Lorsque vous exécutez à nouveau l'API `GenerateBadge`, vous obtiendrez un token (analogue à un badge). Gardez ce token à portée de main, car nous en avons besoin dans la section suivante. Assurez-vous également de **passer ClearanceLevel à 1** pour l'instant.

## Comment Configurer le Contrôleur Agent

Créez un nouveau fichier appelé `AgentController.cs` avec le contenu suivant :

```
using Microsoft.AspNetCore.Mvc;

namespace FBI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    [Authorize(Policy = "Agent")]
    public class AgentController : ControllerBase
    {
        public AgentController() { }
    }
}

```

Comme vous pouvez le voir ci-dessus, nous autorisons l'accès à l'ensemble du contrôleur pour les Agents uniquement. Ainsi, même l'Admin ne pourra pas accéder aux API que nous allons créer.

### Comment Accéder aux API des Enregistrements

Ajoutons les API pour accéder aux fichiers publics et classifiés.

```
[HttpGet]
[Route("[action]")]
[Authorize(Policy = "ClearanceLevel1")]
public ActionResult<String> AccessPublicFiles()
{
    return new OkObjectResult("Accès aux Fichiers Publics");
}

[HttpGet]
[Route("[action]")]
[Authorize(Policy = "ClearanceLevel2")]
public ActionResult<String> AccessClassifiedFiles()
{
    return new OkObjectResult("Accès aux Fichiers Classifiés");
}

```

Nous avons ajouté les attributs `Authorize` pour les deux API de sorte que les fichiers publics peuvent être accessibles par `ClearanceLevel1` et les fichiers classifiés peuvent être accessibles par `ClearanceLevel2`.

Si vous essayez d'accéder à ces API avec le token Admin, vous obtiendrez une erreur 403 Interdit. Alors, allez-y et cliquez à nouveau sur le bouton _Authorize_, puis cliquez sur _logout_. Ensuite, obtenez le token de l'étape précédente et collez-le dans le champ avec _Bearer_ comme préfixe.

Maintenant, lorsque vous accédez à l'API _/Agent/AccessPublicFiles_, vous verrez une réponse 200 avec le message _Accès aux Fichiers Publics_. Mais lorsque vous essayez l'API classifiée, vous obtenez l'erreur 403 Interdit.

## Comment Changer le Niveau d'Habilitation

Trois ans plus tard, les performances de notre _Agent_ ont été exceptionnellement bonnes. La direction a maintenant décidé de le promouvoir au Niveau d'Habilitation 2.

L'_Agent_ se rend chez l'_Admin_ et lui demande de fournir un token/badge avec le Niveau d'Habilitation 2.

L'_Admin_ appelle l'API _/Admin/Login_ pour générer son propre token en premier. Il l'entre ensuite dans la boîte de dialogue _Authorize_.

L'admin appelle ensuite l'API _/Admin/GenerageBadge_ avec la valeur 2 dans le ClearanceLevel. Cela génère un nouveau token/badge qu'il remet ensuite à l'_Agent_.

L'_Agent_ entre ce token/badge dans la boîte de dialogue _Authorize_ et lorsqu'il appelle maintenant _/Agent/AccessClassifiedFiles_, il est ravi de voir le résultat _Accès aux Fichiers Classifiés_.

## Conclusion

Vous pouvez trouver le projet complet [ici](https://github.com/shenanigan/fbi-demo) sur GitHub.

La sécurité des API est extrêmement importante et ne doit pas être prise à la légère, même si elle est destinée à un usage interne uniquement. Configurez l'Authentification et l'Autorisation et vous êtes à moitié là.

Il existe d'autres mesures de sécurité que vous pouvez prendre contre les attaques DDoS, accepter les API d'une IP ou d'un domaine particulier uniquement, et ainsi de suite.

Comment avez-vous aimé l'article ? Quelles autres mesures de sécurité prenez-vous habituellement ? Des commentaires ou des retours ?

Vous pouvez consulter plus de tutoriels sur [mon site](https://daveops.co.in).