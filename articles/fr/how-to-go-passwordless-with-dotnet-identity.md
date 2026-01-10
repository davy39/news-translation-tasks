---
title: Connexion Sans Mot de Passe – Comment Passer à l'Authentification Sans Mot
  de Passe avec .NET Identity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-07T16:58:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-go-passwordless-with-dotnet-identity
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-02-at-6.59.47-PM.png
tags:
- name: api
  slug: api
- name: passwords
  slug: passwords
- name: Security
  slug: security
seo_title: Connexion Sans Mot de Passe – Comment Passer à l'Authentification Sans
  Mot de Passe avec .NET Identity
seo_desc: 'By Arjav Dave

  There are tons of new apps launching every day, so you''ll want to make yours stand
  out. It should have unique features, and it should be easy and convenient to use.

  One of the major pain points for many apps is that they require a usern...'
---

Par Arjav Dave

Il y a des tonnes de nouvelles applications qui lancent chaque jour, donc vous voudrez faire en sorte que la vôtre se démarque. Elle devrait avoir des fonctionnalités uniques, et elle devrait être facile et pratique à utiliser.

L'un des principaux points de friction pour de nombreuses applications est qu'elles nécessitent un nom d'utilisateur et un mot de passe pour se connecter. Personnellement, je dois me souvenir de 10 à 15 mots de passe pour des applications comme Gmail, Facebook, Instagram, et plus encore. Vous voyez l'idée.

Dans cet article, nous allons créer une solution pour vos API qui permettra à vos utilisateurs de se connecter sans mot de passe.

## Comment passer à l'authentification sans mot de passe

Pour omettre le besoin d'un mot de passe, votre application doit générer un type de jeton pour l'utilisateur.

Ce jeton est ensuite envoyé à l'utilisateur où seul lui peut y accéder – par exemple dans son email ou via son téléphone. Voici un aperçu du flux.

![Flux de Connexion Sans Mot de Passe](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/njjypscirkr5stsiqexu.png)

.NET Identity est un [package](https://www.nuget.org/packages/Microsoft.AspNetCore.Identity/) qui fournit des moyens de gérer les utilisateurs, les mots de passe, les données de profil, les rôles, les revendications, les jetons, et plus encore.

De plus, Identity fournit des moyens de générer des jetons pour la confirmation d'email ou pour changer l'email ou le téléphone de l'utilisateur. Nous allons utiliser les jetons générés par Identity pour vérifier nos utilisateurs.

Il y a deux principaux fournisseurs de jetons disponibles :

* `TotpSecurityStampBasedTokenProvider` (Mot de Passe à Usage Unique Basé sur le Temps).
* `DataProtectionTokenProvider`

### TotpSecurityStampBasedTokenProvider

Ce fournisseur de jetons génère des jetons basés sur le temps qui sont valides pendant environ 3 minutes (vous pouvez consulter le [code source ici](https://github.com/aspnet/AspNetIdentity/blob/b7826741279450c58b230ece98bd04b4815beabf/src/Microsoft.AspNet.Identity.Core/Rfc6238AuthenticationService.cs#L75)). Basé sur le fournisseur de jetons, les jetons sont générés à partir de l'email, du numéro de téléphone, ou de l'ID utilisateur ainsi que du cachet de sécurité de l'utilisateur.

Dotnet Identity fournit les classes utilitaires `EmailTokenProvider` et `PhoneNumberTokenProvider` qui sont des sous-classes de `TotpSecurityStampBasedTokenProvider`.

### DataProtectorTokenProvider

Si vous voulez générer un jeton qui n'expire pas pendant longtemps, `DataProtectorTokenProvider` est la solution.

`DataProtectorTokenProvider` génère des jetons en utilisant un `DataProtector` et des algorithmes cryptographiques. Vous pouvez consulter l'implémentation pour plus de détails [ici](https://github.com/aspnet/AspNetIdentity/blob/main/src/Microsoft.AspNet.Identity.Owin/DataProtectorTokenProvider.cs).

Dans cet article, nous allons sous-classer `DataProtectorTokenProvider` pour que notre jeton soit valide pendant 10 minutes.

## Comment Configurer Identity

Commençons par un nouveau projet. Créez un projet en exécutant la commande **`dotnet new webapi –name NoPasswordProject`**.

```
dotnet add package Microsoft.EntityFrameworkCore.InMemory --version 5.0.4
dotnet add package Microsoft.AspNetCore.Identity.EntityFrameworkCore --version 5.0.4

```

Nous allons créer une base de données en mémoire pour ce tutoriel. Mais vous pouvez utiliser une base de données de votre choix et changer le package en conséquence.

Note : La base de données en mémoire effacera les utilisateurs à chaque redémarrage du serveur.

## Comment Créer un Fournisseur de Jeton Personnalisé

Créons un fournisseur de jeton personnalisé qui génère des jetons valides pendant 10 minutes.

### NPTokenProvider

Créez un nouveau fichier appelé `NPTokenProvider.cs`. Le préfixe NP signifie No Password.

```
using Microsoft.AspNetCore.DataProtection;
using Microsoft.AspNetCore.Identity;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;

public class NPTokenProvider<TUser> : DataProtectorTokenProvider<TUser>
where TUser : IdentityUser
{
    public NPTokenProvider(
        IDataProtectionProvider dataProtectionProvider,
        IOptions<NPTokenProviderOptions> options, ILogger<NPTokenProvider<TUser>> logger)
        : base(dataProtectionProvider, options, logger)
    { }
}

```

Ici, nous sous-classons `DataProtectorTokenProvider`. Rien d'extraordinaire, sauf que dans le constructeur, nous passons `NPTokenProviderOptions`. Les options doivent être des sous-classes de `DataProtectionTokenProviderOptions`.

### NPTokenProviderOptions

Créez un nouveau fichier appelé `NPTokenProviderOptions.cs` et collez le code ci-dessous.

```
using System;
using Microsoft.AspNetCore.Identity;

public class NPTokenProviderOptions : DataProtectionTokenProviderOptions
{
    public NPTokenProviderOptions()
    {
        Name = "NPTokenProvider";
        TokenLifespan = TimeSpan.FromMinutes(10);
    }
}

```

Nous définissons des options pour la création des jetons. Vous pouvez changer le `Name` et `TokenLifeSpan` selon vos préférences.

### DbContext

Presque tous les projets ont besoin d'une base de données pour stocker leurs utilisateurs et autres données liées au projet. Le Framework EF Dotnet fournit un helper `DbContext` pour gérer les sessions avec la base de données et interroger et sauvegarder des entités.

Créez donc une sous-classe de `IdentityDbContext` qui est elle-même une sous-classe de `DbContext`. Nommez le fichier `NPDataContext.cs`.

```
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;

public class NPDataContext : IdentityDbContext
{
    public NPDataContext(DbContextOptions<NPDataContext> options)
        : base(options)
    { }
}

```

### Startup.cs

Nous avons créé les classes. Il est maintenant temps de les configurer dans notre fichier `Startup.cs`. Dans `ConfigureServices`, ajoutez le code ci-dessous au début.

```
var builder = services
.AddIdentityCore<IdentityUser>()
.AddEntityFrameworkStores<NPDataContext>();

var UserType = builder.UserType;
var provider = typeof(NPTokenProvider<>).MakeGenericType(UserType);
builder.AddTokenProvider("NPTokenProvider", provider);

services.AddDbContext<NPDataContext>(options =>
    options.UseInMemoryDatabase(Guid.NewGuid().ToString()));

services.AddAuthentication(options =>
{
    options.DefaultScheme = IdentityConstants.ExternalScheme;
});

```

Ajoutez également **`app.UseAuthentication();`** au-dessus de `app.UseAuthorization();` dans la méthode `Configure`.

### NoPasswordController.cs

Créons un contrôleur pour notre API de connexion et de vérification. Créez un fichier `NoPasswordController.cs` dans votre dossier `Controllers`. Ajoutez le contenu ci-dessous au fichier.

```
using System;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace NoPasswordProject.Controllers
{
    [ApiController]
    [Route("[controller]/[action]")]
    public class NoPasswordController : ControllerBase
    {
        private readonly UserManager<IdentityUser> _userManager;

        public NoPasswordController(UserManager<IdentityUser> userManager)
        {
            _userManager = userManager;
        }
    }
}

```

Nous injectons une instance de `UserManager` dans notre contrôleur. UserManager est utilisé pour les opérations CRUD pour un utilisateur ainsi que pour générer des jetons et les valider.

### API de Connexion

Ajoutons une API `Login` qui accepte un Email en entrée. L'Email est l'identifiant unique pour un utilisateur, c'est-à-dire qu'il doit y avoir une relation un-à-un entre l'utilisateur et l'email.

Créez une nouvelle fonction dans votre contrôleur comme ci-dessous.

```
[HttpGet]
public async Task<ActionResult<String>> Login([FromQuery] string Email)
{
    // Créez ou récupérez votre utilisateur depuis la base de données
    var User = await _userManager.FindByNameAsync(Email);
    if (User == null)
    {
        User = new IdentityUser();
        User.Email = Email;
        User.UserName = Email;
        var IdentityResult = await _userManager.CreateAsync(User);
        if (IdentityResult.Succeeded == false)
        {
            return BadRequest();
        }
    }

    var Token = await _userManager.GenerateUserTokenAsync(User, "NPTokenProvider", "nopassword-for-the-win");

    // NE RETOURNEZ PAS LE JETON.
    // ENVOYEZ-LE À L'UTILISATEUR VIA EMAIL.
    return NoContent();
}

```

Ici, nous récupérons un utilisateur depuis la base de données. Si l'utilisateur n'existe pas, nous créons un utilisateur. Assurez-vous de définir également le UserName, sinon cela donnera une erreur d'exécution.

Ensuite, en fonction de l'utilisateur, nous générons un `UserToken`. La méthode `GenerateUserTokenAsync` prend l'utilisateur, le fournisseur de jetons et le but de la génération d'un jeton.

La chaîne du fournisseur de jetons doit être celle que vous avez utilisée dans `NPTokenProviderOptions`. Le but peut être ce que vous voulez.

Envoyez le jeton à l'utilisateur via un lien dans un email bien conçu. Lorsque l'utilisateur clique sur le lien dans l'email, cela ouvrira votre page front-end. Par conséquent, cette page demandera l'API Verify.

### API de Vérification

Ajoutons une autre API appelée `Verify` qui prend l'`Email` et le `Token` comme paramètres de requête.

```
[HttpGet]
public async Task<ActionResult<String>> Verify([FromQuery] string Token, [FromQuery] string Email)
{
    // Récupérez votre utilisateur depuis la base de données
    var User = await _userManager.FindByNameAsync(Email);
    if (User == null)
    {
        return NotFound();
    }

    var IsValid = await _userManager.VerifyUserTokenAsync(User, "NPTokenProvider", "nopassword-for-the-win", Token);
    if (IsValid)
    {
        // TODO: Générer un jeton bearer
        var BearerToken = "";
        return BearerToken;
    }
    return Unauthorized();
}

```

Nous récupérons à nouveau l'utilisateur en fonction de l'email. Par conséquent, si nous ne pouvons pas trouver l'utilisateur, nous retournerons 404 Not Found.

Nous continuons ensuite à vérifier l'utilisateur. `VerifyUserTokenAsync` prend l'utilisateur, le fournisseur de jetons, le but et le jeton comme paramètres d'entrée. Le but doit être le même que celui utilisé lors de la génération du jeton.

Si le jeton n'est pas valide, retournez 401 Non Autorisé. Sinon, retournez le jeton bearer. [Voici un bon article](https://arjavdave.com/2021/03/31/net-5-setup-authentication-and-authorisation/) sur la façon de générer un jeton bearer pour l'utilisateur.

Vous pouvez trouver le projet complet [ici](https://github.com/shenanigan/dotnet-passwordless).

## Conclusion

Les bonnes fonctionnalités étaient autrefois la principale chose qui comptait lors de la création d'une application. Mais aujourd'hui, outre le fait d'avoir de grandes fonctionnalités, la commodité est une priorité pour les utilisateurs.

Dans cet article, nous avons examiné une façon de rendre vos applications plus conviviales. Faites-moi savoir si vous avez d'autres moyens d'améliorer vos applications.

[Consultez ici](https://arjavdave.com) pour plus de tutoriels comme celui-ci.