---
title: Apprendre le Développement Piloté par les Tests avec des Tests d'Intégration
  en .NET 5.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-14T17:37:46.000Z'
originalURL: https://freecodecamp.org/news/learn-tdd-with-integration-tests-in-net-5-0
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/tdd.jpg
tags:
- name: Software Testing
  slug: software-testing
- name: test driven development
  slug: test-driven-development
- name: Testing
  slug: testing
seo_title: Apprendre le Développement Piloté par les Tests avec des Tests d'Intégration
  en .NET 5.0
seo_desc: "By Arjav Dave\nTest-Driven Development is a much-debated concept in the\
  \ tech industry. Developers wonder whether they should practice TDD or not, how\
  \ advantageous it is, and so on. \nSo what is Test-Driven Development, or TDD? Simply\
  \ put, TDD dictates ..."
---

Par Arjav Dave

Le Développement Piloté par les Tests est un concept très débattu dans l'industrie technologique. Les développeurs se demandent s'ils doivent pratiquer le TDD ou non, à quel point c'est avantageux, et ainsi de suite. 

Alors, qu'est-ce que le Développement Piloté par les Tests, ou TDD ? En termes simples, le TDD dicte que vous testez votre code avant de le déployer en production.

Maintenant, il existe de nombreuses opinions sur les types de tests que vous devriez inclure dans le TDD. Par exemple, devriez-vous inclure des Tests Unitaires, des Tests d'Intégration, des Tests Système, ou même des Tests d'Acceptation Utilisateur ?

Dans cet article, nous allons passer par un exemple concret qui vous montrera comment écrire des tests d'intégration en .NET 5.0 avec une méthodologie TDD. 

Pour écrire des tests, nous utiliserons le framework XUnit, car il est plus complet que les frameworks de test NUnit ou MSTest. [Voici](https://www.lambdatest.com/blog/nunit-vs-xunit-vs-mstest/) un bon article si vous voulez en savoir plus sur la différence entre ces frameworks. 

Deuxièmement, VS Code a toujours été mon choix d'IDE, mais vous pouvez également utiliser Visual Studio. 

Commençons par définir les exigences de notre projet.

## Exigences du Projet

Le TDD nécessite une compréhension très claire de la portée du travail. Sans cette clarté, tous les cas de test pourraient ne pas être couverts.

Définissons ce que nous entendons par portée du travail. Nous allons développer un système d'admission de patients pour un hôpital.

### Exigences Métier

* Un hôpital dispose de X chambres de soins intensifs, Y chambres Premium et Z chambres Générales.
* Les chambres de soins intensifs et les chambres Premium peuvent accueillir un seul patient à la fois, tandis que les chambres Générales peuvent accueillir 2 patients. Chaque chambre a un numéro de chambre.
* À l'admission, le patient doit fournir son nom, son âge, son sexe et son numéro de téléphone.
* Il est possible de rechercher un patient par son nom ou son numéro de téléphone.
* Le même patient ne peut pas être admis dans plusieurs lits tant qu'il est encore enregistré.
* Un patient ne peut pas être admis si toutes les chambres sont occupées.

### Règles de Validation du Modèle

Sur la base des exigences ci-dessus, il y a deux modèles dont nous devons nous soucier, à savoir Patient et Room.

* L'âge d'un patient est compris entre 0 et 150 ans. La longueur de son nom doit être comprise entre 2 et 40 caractères. Le sexe peut être masculin, féminin ou autre. La longueur du numéro de téléphone doit être comprise entre 7 et 12 chiffres et doit être entièrement numérique.
* Le type de chambre peut être soit "ICU", "Premium" ou "General".

### Cas de Test à Implémenter

Maintenant que nous avons défini nos règles et exigences, commençons à créer des cas de test. Puisqu'il s'agit d'une application CRUD basique, nous aurons principalement des tests d'intégration.

#### Cas de test pour les patients

* Effectuer tous les tests de validation de modèle.
* Admettre le même patient deux fois.
* Enregistrer le départ du même patient deux fois.
* Admettre le même patient dans plusieurs chambres en même temps.
* Rechercher un patient par numéro de téléphone et par nom.

## Configuration du TDD

Dans la section précédente, nous avons recueilli les exigences de notre projet. Ensuite, nous avons défini les modèles. Enfin, nous avons créé la liste des cas de test que nous allons implémenter.

Ouvrez votre terminal et exécutez le script ci-dessous pour créer et configurer un nouveau projet.

```
mkdir TDD
cd TDD
dotnet new sln
dotnet new webapi --name TDD
dotnet new xunit --name TDD.Tests
cd TDD
dotnet add package Microsoft.EntityFrameworkCore --version 5.0.5
cd ../TDD.Tests
dotnet add reference ../TDD/TDD.csproj
dotnet add package Microsoft.EntityFrameworkCore --version 5.0.5
dotnet add package Microsoft.AspNetCore.Hosting --version 2.2.7
dotnet add package Microsoft.AspNetCore.Mvc.Testing --version 5.0.5
dotnet add package Microsoft.EntityFrameworkCore.InMemory --version 5.0.5
cd ..
dotnet sln add TDD/TDD.csproj
dotnet sln add TDD.Tests/TDD.Tests.csproj
code .

```

Le script ci-dessus crée un fichier de solution nommé _TDD.sln_. Deuxièmement, nous créons deux projets pour TDD et TDD.Tests. Ensuite, nous ajoutons les dépendances pour chaque projet. Enfin, nous ajoutons les projets à la solution et ouvrons le projet dans VS Code.

Avant de commencer les tests, nous avons un peu plus de configuration à faire. Essentiellement, les tests d'intégration testent un module spécifique sans mocking. Nous allons donc imiter notre application via TestServer.

### Custom WebApplicationFactory

Afin d'imiter le TestServer, il existe une classe appelée [WebApplicationFactory](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.testing.webapplicationfactory-1?view=aspnetcore-5.0) (WAF) qui initialise l'application en mémoire.

Dans votre projet **TDD.Tests**, créez un fichier nommé _PatientTestsDbWAF.cs_ avec le code suivant.

```
using System.Linq;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.AspNetCore;


namespace TDD.Tests
{
    public class PatientTestsDbWAF<TStartup> : WebApplicationFactory<TStartup> where TStartup : class
    {

        protected override IWebHostBuilder CreateWebHostBuilder()
        {
            return WebHost.CreateDefaultBuilder()
                .UseStartup<TStartup>();
        }
        protected override void ConfigureWebHost(IWebHostBuilder builder)
        {
            builder.ConfigureServices(async services =>
           {
               // Supprimer l'enregistrement du DbContext de l'application.
               var descriptor = services.SingleOrDefault(
                      d => d.ServiceType ==
                          typeof(DbContextOptions<DataContext>));

               if (descriptor != null)
               {
                   services.Remove(descriptor);
               }

               // Ajouter DbContext en utilisant une base de données en mémoire pour les tests.
               services.AddDbContext<DataContext>(options =>
                  {
                      // Utiliser une base de données en mémoire pour ne pas interférer avec la base de données originale.
                      options.UseInMemoryDatabase("PatientTestsTDD.db");
                  });
           });
        }
    }
}

```

Nous supprimons le DbContext de l'application et ajoutons un DbContext **en mémoire**. Cette étape est nécessaire car nous ne voulons pas interférer avec la base de données originale.

Deuxièmement, nous initialisons la base de données avec quelques données factices.

Puisque DataContext est une classe personnalisée, elle générera une erreur de compilation. Nous devons donc la créer.

### Data Context

Dans votre **projet TDD**, créez un fichier nommé _DataContext.cs_ avec le code suivant :

```
using Microsoft.EntityFrameworkCore;

namespace TDD
{
    public class DataContext : DbContext
    {
        public DataContext(DbContextOptions options) : base(options) { }

        // Pour stocker la liste des patients et leur état
        public DbSet<Patient> Patient { get; set; }

        // Pour stocker les chambres avec leurs types et capacités
        public DbSet<Room> Room { get; set; }

        // Pour enregistrer quels patients sont actuellement admis dans quelle chambre
        public DbSet<RoomPatient> RoomPatient { get; set; }

    }
}

```

Ici, Patient, Room et RoomPatient sont des classes d'entités avec les propriétés requises, que nous allons créer ensuite.

### Ajouter la propriété Patient

Encore une fois, dans votre **projet TDD**, créez un fichier nommé _Patient.cs_ et collez le code ci-dessous :

```
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TDD
{
    public class Patient
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
      
        public String Name { get; set; }

        public String PhoneNumber { get; set; }

        public int Age { get; set; }

        public String Gender { get; set; }
    }
}

```

### Ajouter la propriété Room

Créez un autre fichier nommé _Room.cs_ avec le code suivant :

```
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TDD
{
    public class Room
    {
      	[Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
      
        public String RoomType { get; set; }

        public int CurrentCapacity { get; set; }

        public int MaxCapacity { get; set; }
    }
}

```

### Ajouter la propriété RoomPatient

Créez le dernier fichier de modèle _RoomPatient.cs_ avec le code suivant :

```
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TDD
{
    public class RoomPatient
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        [Required]
        public int RoomId { get; set; }

        [ForeignKey("RoomId")]
        public Room Room { get; set; }

        [Required]
        public int PatientId { get; set; }

        [ForeignKey("PatientId")]
        public Patient Patient { get; set; }
    }
}

```

Maintenant, vous ne devriez plus avoir d'erreurs de compilation.

Enfin, supprimez les fichiers _WeatherForecast.cs_ et _WeatherForecastController.cs_.

Allez dans votre terminal dans VS Code et exécutez la commande suivante :

```
cd TDD.Tests
dotnet test

```

Vous verrez un beau résultat vert qui indique qu'un test a réussi.

![Image](https://arjavdave.com/wp-content/uploads/2021/04/Test_Success_1-1024x211.png)
_Succès du Test_

### Créer le Patient Controller

Malheureusement, .NET ne fournit pas de moyen de tester directement les modèles en eux-mêmes. Nous devons donc créer un contrôleur pour le tester.

Allez-y et créez un fichier _PatientController.cs_ dans le dossier Controllers dans le **projet TDD** avec le code ci-dessous :

```
using Microsoft.AspNetCore.Mvc;

namespace TDD.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PatientController : Controller
    {
        [HttpPost]
        public IActionResult AddPatient([FromBody] Patient Patient)
        {
            // TODO: Insérer le patient dans la base de données
            return Created("/patient/1", Patient);
        }
    }
}

```

Nous avons créé une API pour ajouter un patient. Afin de tester notre modèle, nous appellerons cette API.

C'est tout ce dont nous avons besoin pour commencer les tests.

## Tests de Validation de Modèle

Puisque nous avons configuré le code de base pour les tests, écrivons un test qui échoue. Nous commencerons nos tests avec les tests de validation de modèle.

### État d'Échec (Rouge)

Créons un nouveau fichier nommé _PatientTests.cs_ dans votre **projet TDD.Tests** et supprimez le fichier nommé _UnitTest1.cs_. Copiez le code ci-dessous dans votre fichier :

```
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using Xunit;
using System.Text;
using System.Text.Json;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.AspNetCore.Mvc.Testing;
using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace TDD.Tests
{
    public class PatientTests : IClassFixture<PatientTestsDbWAF<Startup>>
    {
        // HttpClient pour appeler nos API
        private readonly HttpClient httpClient;
        public WebApplicationFactory<Startup> _factory;

        public PatientTests(PatientTestsDbWAF<Startup> factory)
        {
            _factory = factory;

            // Initialiser le HttpClient
            httpClient = _factory.CreateClient();
        }

        [Theory]
        [InlineData("Test Name 2", "1234567891", 20, "Male", HttpStatusCode.Created)]
        [InlineData("T", "1234567891", 20, "Male", HttpStatusCode.BadRequest)]
        [InlineData("A very very very very very very loooooooooong name", "1234567891", 20, "Male", HttpStatusCode.BadRequest)]
        [InlineData(null, "1234567890", 20, "Invalid Gender", HttpStatusCode.BadRequest)]
        [InlineData("Test Name", "InvalidNumber", 20, "Male", HttpStatusCode.BadRequest)]
        [InlineData("Test Name", "1234567890", -10, "Male", HttpStatusCode.BadRequest)]
        [InlineData("Test Name", "1234567890", 20, "Invalid Gender", HttpStatusCode.BadRequest)]
        [InlineData("Test Name", "12345678901234444", 20, "Invalid Gender", HttpStatusCode.BadRequest)]
        public async Task PatientTestsAsync(String Name, String PhoneNumber, int Age, String Gender, HttpStatusCode ResponseCode)
        {
            var scopeFactory = _factory.Services;
            using (var scope = scopeFactory.CreateScope())
            {
                var context = scope.ServiceProvider.GetService<DataContext>();
                
                // Initialiser la base de données, afin que
                // les modifications apportées par d'autres tests soient réinitialisées.
                await DBUtilities.InitializeDbForTestsAsync(context);
                
                // Arranger
                var request = new HttpRequestMessage(HttpMethod.Post, "api/patient");

                request.Content = new StringContent(JsonSerializer.Serialize(new Patient
                {
                    Name = Name,
                    PhoneNumber = PhoneNumber,
                    Age = Age,
                    Gender = Gender
                }), Encoding.UTF8, "application/json");

                // Agir
                var response = await httpClient.SendAsync(request);

                // Assert
                var StatusCode = response.StatusCode;
                Assert.Equal(ResponseCode, StatusCode);
            }
        }
    }
}

```

L'attribut `[Theory]` nous permet de mentionner différents paramètres pour nos tests. Grâce à cela, nous n'avons pas à écrire différents tests pour toutes les combinaisons.

De plus, DBUtilities est une classe utilitaire pour réinitialiser la base de données à son état initial. Cela peut sembler trivial lorsque nous avons 1 ou 2 tests, mais cela devient critique à mesure que nous ajoutons plus de tests.

### Classe DBUtilities

La classe DBUtilities initialisera votre base de données avec 1 patient et 3 types de chambres différents.

Créez un fichier nommé _DBUtilities.cs_ dans votre **projet TDD.Tests** avec le code ci-dessous :

```
using System.Threading.Tasks;

namespace TDD.Tests
{
    // Aide à initialiser la base de données soit à partir du WAF pour la première fois
    // Ou avant d'exécuter chaque test.
    public class DBUtilities
    {

        // Efface la base de données puis,
        // Ajoute 1 Patient et 3 types de chambres différents à la base de données
        public static async Task InitializeDbForTestsAsync(DataContext context)
        {
            context.RoomPatient.RemoveRange(context.RoomPatient);
            context.Patient.RemoveRange(context.Patient);
            context.Room.RemoveRange(context.Room);
            
            // Arranger
            var Patient = new Patient
            {
                Name = "Test Patient",
                PhoneNumber = "1234567890",
                Age = 20,
                Gender = "Male"
            };
            context.Patient.Add(Patient);

            var ICURoom = new Room
            {
                RoomType = "ICU",
                MaxCapacity = 1,
                CurrentCapacity = 1
            };
            context.Room.Add(ICURoom);

            var GeneralRoom = new Room
            {
                RoomType = "General",
                MaxCapacity = 2,
                CurrentCapacity = 2
            };
            context.Room.Add(GeneralRoom);

            var PremiumRoom = new Room
            {
                RoomType = "Premium",
                MaxCapacity = 1,
                CurrentCapacity = 1
            };
            context.Room.Add(PremiumRoom);

            await context.SaveChangesAsync();
        }
    }
}

```

Allez-y et exécutez à nouveau la commande **dotnet test** et vous verrez 1 test réussi et 4 tests échoués. Cela est dû au fait que les 4 tests attendaient un BadRequest mais obtenaient un résultat Created.

![Image](https://arjavdave.com/wp-content/uploads/2021/04/failed_tests-1024x195.png)
_État d'Échec (Rouge)_

Corrigeons cela !

### État de Succès (Vert)

Pour corriger cela, nous devons ajouter des attributs à notre classe _Patient.cs_.

Mettez à jour le fichier _Patient.cs_ comme suit :

```
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace TDD
{
    public class Patient : IValidatableObject
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        [Required]
        [StringLength(40, MinimumLength = 2, ErrorMessage = "Le nom doit être compris entre 2 et 40 caractères.")]
        public String Name { get; set; }

        [Required]
        [DataType(DataType.PhoneNumber)]
        [RegularExpression(@"^(\d{7,12})$", ErrorMessage = "Numéro de téléphone non valide")]
        public String PhoneNumber { get; set; }

        [Required]
        [Range(1, 150)]
        public int Age { get; set; }

        [Required]
        public String Gender { get; set; }

        public Boolean IsAdmitted { get; set; }

        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        {
            // Seuls les genres Male, Female ou Other sont autorisés
            if (Gender.Equals("Male", System.StringComparison.CurrentCultureIgnoreCase) == false &&
                Gender.Equals("Female", System.StringComparison.CurrentCultureIgnoreCase) == false &&
                Gender.Equals("Other", System.StringComparison.CurrentCultureIgnoreCase) == false)
            {
                yield return new ValidationResult("Le genre peut être soit Male, Female ou Other");
            }

            yield return ValidationResult.Success;
        }
    }
}

```

Ici, nous avons ajouté les attributs requis. Nous avons également implémenté l'interface _IValidatableObject_ afin que nous puissions vérifier le _Gender_.

Il est temps d'exécuter la commande **dotnet test**. Vous verrez une belle ligne verte indiquant que 5 tests ont réussi.

![Image](https://arjavdave.com/wp-content/uploads/2021/04/Tests_passed_2-1024x244.png)

Vous pouvez ajouter plus de scénarios de cas limites dans le _InlineData_ pour tester les tests de validation de modèle Patient de manière approfondie.

## Test de Doublon de Patient

Nous allons maintenant créer un test qui échoue lorsque nous essayons d'ajouter un patient en double.

### Test d'Échec (Rouge)

Créez un autre test dans votre classe _PatientTests._ Ajoutez le code ci-dessous :

```
[Fact]
public async Task PatientDuplicationTestsAsync()
{
    var scopeFactory = _factory.Services;
    using (var scope = scopeFactory.CreateScope())
    {
        var context = scope.ServiceProvider.GetService<DataContext>();
        await DBUtilities.InitializeDbForTestsAsync(context);

        // Arranger
        var Patient = await context.Patient.FirstOrDefaultAsync();

        var Request = new HttpRequestMessage(HttpMethod.Post, "api/patient");
        Request.Content = new StringContent(JsonSerializer.Serialize(Patient), Encoding.UTF8, "application/json");

        // Agir
        var Response = await httpClient.SendAsync(Request);

        // Assert
        var StatusCode = Response.StatusCode;
        Assert.Equal(HttpStatusCode.BadRequest, StatusCode);
    }
}

```

Nous avons utilisé un attribut `[Fact]` au lieu de l'attribut `[Theory]` ici puisque nous ne voulons pas tester la même méthode avec différents paramètres. Au lieu de cela, nous voulons faire la même demande deux fois.

Exécutez **dotnet test** pour exécuter notre nouveau test. Le test échouera avec le message _Assert.Equal() Failure_. Il est temps de le corriger.

### Test de Succès (Vert)

Pour corriger le test échoué, nous devons ajouter l'implémentation de la méthode AddPatient dans _PatientController.cs_. Mettez à jour le code du fichier comme suit :

```
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace TDD.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PatientController : Controller
    {
        private readonly DataContext _context;

        public PatientController(DataContext context)
        {
            _context = context;
        }
        [HttpPost]
        public async Task<IActionResult> AddPatientAsync([FromBody] Patient Patient)
        {
            var FetchedPatient = await _context.Patient.FirstOrDefaultAsync(x => x.PhoneNumber == Patient.PhoneNumber);
            // Si le patient n'existe pas, en créer un nouveau
            if (FetchedPatient == null)
            {
                _context.Patient.Add(Patient);
                await _context.SaveChangesAsync();
                return Created($"/patient/{Patient.Id}", Patient);
            }
            // Sinon, renvoyer une mauvaise requête
            else
            {
                return BadRequest();
            }
        }
    }
}

```

Exécutez à nouveau **dotnet test** et vous verrez que les tests ont réussi.

## Notes Importantes

À mesure que vous ajoutez plus de modèles/domaines comme Doctors, Staff, Instruments et ainsi de suite, vous devrez créer plus de tests. Assurez-vous d'avoir un WAF différent, des wrappers utilitaires et des fichiers de test différents pour chacun d'eux.

Deuxièmement, les tests dans le même fichier ne s'exécutent pas en parallèle. Mais les tests de différents fichiers s'exécutent en parallèle. Par conséquent, chaque WAF doit avoir un nom de base de données différent afin que les données ne soient pas mal configurées.

Enfin, les connexions à la base de données originale doivent encore être configurées dans le projet principal.

## Comment écrire de bons tests

Le processus de réflexion pour créer des tests pour tous les scénarios est similaire.

C'est-à-dire que vous devez d'abord identifier les exigences. Ensuite, mettre en place un squelette de méthodes et de classes sans implémentation. Écrire des tests pour vérifier l'implémentation. Enfin, refactoriser si nécessaire et relancer les tests.

Ce tutoriel n'incluait pas l'authentification et l'autorisation pour les API. Vous pouvez [lire ici](https://arjavdave.com/2021/03/31/net-5-setup-authentication-and-authorisation/) comment configurer cela.

Puisque je n'ai pas couvert tous les cas de test ici, j'ai créé un [dépôt sur Github](https://github.com/shenanigan/tdd-demo). Il couvre l'implémentation de tous les cas de test si vous souhaitez y jeter un coup d'œil.

Vous pouvez trouver le [projet ici](https://github.com/shenanigan/tdd-demo).

## Conclusion

Pour que le TDD soit efficace, vous devez vraiment avoir une idée claire de ce que sont les exigences. Si les exigences continuent de changer, il deviendra très difficile de maintenir les tests ainsi que le projet.

Le TDD couvre principalement les tests unitaires, d'intégration et fonctionnels. Vous devrez encore effectuer des tests UAT, de Configuration et de Production avant de passer en production.

Cela dit, le TDD est vraiment utile pour rendre votre projet exempt de bugs. Deuxièmement, il renforce votre confiance pour l'implémentation. Vous pourrez modifier des parties de votre code tant que les tests passent. Enfin, il fournit une meilleure architecture pour votre projet.

[Consultez plus de tutoriels sur .NET ici.](https://arjavdave.com/)