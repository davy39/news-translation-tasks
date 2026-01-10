---
title: Comment effectuer des opérations CRUD avec Blazor et Google Cloud Firestore
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T15:51:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-crud-operations-using-blazor-and-google-cloud-firestore-52890b06e2f8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*muHjpi3rrHCyXSoIqoK7Iw.gif
tags:
- name: Blazor
  slug: blazor
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment effectuer des opérations CRUD avec Blazor et Google Cloud Firestore
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will create a Blazor application using Google Firstore as database
  provider. We will create a Single Page Application (SPA) and perform CRUD operations
  on it. We will use Bootstrap 4 to display a modal...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons créer une application Blazor en utilisant Google Firestore comme fournisseur de base de données. Nous allons créer une application monopage (SPA) et effectuer des opérations CRUD dessus. Nous utiliserons Bootstrap 4 pour afficher une fenêtre modale permettant de gérer les entrées utilisateur. Le formulaire contient également une liste déroulante, qui sera liée à une collection dans notre base de données. Nous allons également implémenter une fonctionnalité de recherche côté client pour rechercher dans la liste des employés par nom d'employé.

Jetez un œil à l'application finale.

![Image](https://cdn-media-1.freecodecamp.org/images/W7b2ndw04cr4wdIHtI2olU2LYkePZaq5Fh33)

### Prérequis

* Installer le SDK .NET Core 2.1 ou supérieur depuis [ici](https://www.microsoft.com/net/learn/get-started-with-dotnet-tutorial#windowscmd)
* Installer la dernière version de Visual Studio 2017 depuis [ici](https://www.visualstudio.com/downloads/)
* Installer l'extension ASP.NET Core Blazor Language Services depuis [ici](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)

### Code Source

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-CRUD-With-CloudFirestore).

### Configuration de Cloud Firestore

La première étape consiste à créer un projet dans la console Google Firebase. Accédez à [https://console.firebase.google.com](https://console.firebase.google.com/) et connectez-vous avec votre compte Google. Cliquez sur le lien Ajouter un projet. Une fenêtre contextuelle s'ouvrira comme illustré dans l'image ci-dessous. Fournissez le nom de votre projet et cliquez sur le bouton Créer un projet en bas.

![Image](https://cdn-media-1.freecodecamp.org/images/IUhsu1yB0vg-JFpejfs-1V6lm22XajPQsF6G)

Notez l'identifiant du projet ici. Les identifiants de projet Firebase sont uniques au niveau mondial. Vous pouvez modifier l'identifiant de votre projet lors de la création d'un nouveau projet. Une fois le projet créé, vous ne pouvez plus modifier l'identifiant de votre projet. Nous utiliserons cet identifiant de projet dans la section suivante lors de l'initialisation de notre application.

Cliquez sur le projet que vous venez de créer. Une page de vue d'ensemble du projet s'ouvrira. Sélectionnez « Database » dans le menu de gauche. Cliquez ensuite sur le bouton « Create database ». Une fenêtre contextuelle s'ouvrira vous demandant de sélectionner les « Security rules for Cloud Firestore ». Sélectionnez « Start in locked mode » et cliquez sur enable.

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1f8jEpvnl1svzglTyJkp51RmOpcnzcGkeEFj)

Cela activera la base de données pour votre projet. Les projets Firebase ont deux options pour la base de données : Realtime Database et Cloud Firestore. Pour cette application, nous utiliserons la base de données « Cloud Firestore ». Cliquez sur le menu déroulant « Database » en haut de la page et sélectionnez « Cloud Firestore ».

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/bYGk2T-Rvk1AqCB9HgMkHz07T-iiCeTSpPPX)

Nous allons créer une collection de villes pour stocker le nom des villes des employés. Nous allons également lier cette collection à une liste déroulante dans notre application web à partir de laquelle l'utilisateur sélectionnera la ville souhaitée. Cliquez sur « Add collection ». Définissez l'identifiant de la collection sur « cities ». Cliquez sur « Next ». Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/PRjBhrBH7VofY1Mdn-ENX2gEzd9Uo6zf4hrY)

Mettez la valeur du champ sur « CityName », sélectionnez string dans le menu déroulant Type et remplissez la valeur avec le nom de la ville « Mumbai ». Cliquez sur Save. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/W8G7ATIkDBVliNQlTzBYHiAaGBAleX-W-NLF)

Cela créera la collection « cities » et insérera le premier document. De même, créez quatre autres documents dans cette collection et mettez la valeur « CityName » à Chennai, New Delhi, Bengaluru et Hyderabad.

Nous utiliserons la collection « employees » pour stocker les données des employés, mais nous ne la créerons pas manuellement. Nous créerons la collection « employees » lors de l'ajout des premières données d'employé depuis l'application.

### Configuration des identifiants de l'application Google

Pour accéder à la base de données depuis notre projet, nous devons définir la variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS` pour pointer vers un fichier de clé de compte de service JSON. Cela établira un pipeline d'authentification de notre application vers Cloud Firestore.

Pour générer le fichier de clé de compte de service, suivez les étapes mentionnées ci-dessous :

**Étape 1** : Accédez à [https://console.cloud.google.com/iam-admin/](https://console.cloud.google.com/iam-admin/). Connectez-vous avec le même compte Google que vous avez utilisé pour créer la base de données Firestore.

**Étape 2** : Sélectionnez le projet dans le menu déroulant de la barre de menu en haut.

**Étape 3** : Sélectionnez « Service accounts » dans le menu de gauche. Sélectionnez le compte de service pour lequel vous souhaitez créer la clé. Cliquez sur le bouton plus dans la colonne « Actions » de cette ligne, puis cliquez sur Create key.

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/9IHtUREAUoK49PnqL0Dwz5VbGQQgHFP4J0fU)

**Étape 4** : Une fenêtre modale contextuelle s'ouvrira vous demandant de sélectionner le type de clé. Sélectionnez « JSON » et cliquez sur le bouton create. Cela créera une clé privée pour accéder à votre compte Firestore et téléchargera un fichier de clé JSON sur votre machine. Nous utiliserons ce fichier pour définir la variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS` dans la suite de cet article.

### Créer une application web Blazor

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet. Après avoir sélectionné le projet, une boîte de dialogue « Nouveau Projet » s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Ensuite, sélectionnez « ASP.NET Core Web Application » parmi les types de projets disponibles. Donnez le nom du projet comme BlazorWithFirestore et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/yK4DI82EB76voCsnfmJaj5KmKwmjhaFwmeF9)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez observer deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez « .NET Core » et « ASP.NET Core 2.1 » dans ces menus déroulants. Ensuite, sélectionnez le modèle « Blazor (ASP .NET Core hosted) » et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/oq3ARrgxpuIWNZ-riZRsvEeB4QVe5QT2GTq7)

Maintenant, notre solution Blazor sera créée. Vous pouvez observer que nous avons trois fichiers de projet créés dans cette solution.

1. BlazorWithFirestore.Client — Il contient le code côté client et les pages qui seront rendues sur le navigateur.
2. BlazorWithFirestore.Server — Il contient les codes côté serveur tels que la couche d'accès aux données et l'API web.
3. BlazorWithFirestore.Shared — Il contient le code partagé qui peut être accessible à la fois par le client et le serveur. Il contient nos classes de modèle.

### Ajout de la référence de package pour Firestore

Nous devons ajouter la référence de package pour Google Cloud Firestore, ce qui nous permettra d'accéder à notre base de données depuis l'application Blazor. Faites un clic droit sur le projet `BlazorWithFirestore.Shared`.

Sélectionnez « Edit BlazorWithFirestore.Shared.csproj ». Cela ouvrira le fichier `BlazorWithFirestore.Shared.csproj`. Ajoutez les lignes suivantes à l'intérieur.

```
<ItemGroup>  <PackageReference Include="Google.Cloud.Firestore" Version="1.0.0-beta14" /></ItemGroup>
```

Ajoutez de même ces lignes au fichier `BlazorWithFirestore.Server.csproj`.

### Création du Modèle

Nous allons créer notre classe de modèle dans le projet `BlazorWithFirestore.Shared`. Faites un clic droit sur `BlazorWithFirestore.Shared` et sélectionnez Ajouter >> Nouveau Dossier. Nommez le dossier Models. Ensuite, faites un clic droit sur le dossier Models et sélectionnez Ajouter >> Classe pour ajouter un nouveau fichier de classe. Donnez le nom de votre classe comme Employee.cs et cliquez sur Ajouter.

Ouvrez la classe `Employee.cs` et mettez le code suivant à l'intérieur.

```
using System;using Google.Cloud.Firestore;namespace BlazorWithFirestore.Shared.Models{    [FirestoreData]    public class Employee    {        public string EmployeeId { get; set; }        public DateTime date { get; set; }        [FirestoreProperty]        public string EmployeeName { get; set; }        [FirestoreProperty]        public string CityName { get; set; }        [FirestoreProperty]        public string Designation { get; set; }        [FirestoreProperty]        public string Gender { get; set; }    }}
```

Nous avons décoré la classe avec l'attribut `[FirestoreData]`. Cela nous permettra de mapper cet objet de classe à la collection Firestore. Seules les propriétés de classe marquées avec l'attribut `[FirestoreProperty]` sont prises en compte lors de l'enregistrement du document dans notre collection. Nous n'avons pas besoin d'enregistrer EmployeeId dans notre base de données car il est généré automatiquement.

Lors de la récupération des données, nous lierons l'identifiant de document généré automatiquement à la propriété EmployeeId. De même, nous utiliserons la propriété date pour lier la date de création de la collection lors de la récupération de l'enregistrement. Nous utiliserons cette propriété date pour trier la liste des employés par date de création. Par conséquent, nous n'avons pas appliqué l'attribut `[FirestoreProperty]` à ces deux propriétés.

De même, créez un fichier de classe Cities.cs et mettez le code suivant à l'intérieur.

```
using System;using Google.Cloud.Firestore;namespace BlazorWithFirestore.Shared.Models{    [FirestoreData]    public class Cities    {        public string CityName { get; set; }    }}
```

### Création de la couche d'accès aux données pour l'application

Faites un clic droit sur le projet `BlazorWithFirestore.Server` puis sélectionnez Ajouter >> Nouveau Dossier et nommez le dossier DataAccess. Nous ajouterons notre classe pour gérer les opérations liées à la base de données uniquement à l'intérieur de ce dossier. Faites un clic droit sur le dossier DataAccess et sélectionnez Ajouter >> Classe. Nommez votre classe EmployeeDataAccessLayer.cs.

Mettez le code suivant à l'intérieur de cette classe.

```
using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;using BlazorWithFirestore.Shared.Models;using Google.Cloud.Firestore;using Newtonsoft.Json;namespace BlazorWithFirestore.Server.DataAccess{    public class EmployeeDataAccessLayer    {        string projectId;        FirestoreDb fireStoreDb;        public EmployeeDataAccessLayer()        {            string filepath = "C:\\FirestoreAPIKey\\blazorwithfirestore-6d0a096b0174.json";            Environment.SetEnvironmentVariable("GOOGLE_APPLICATION_CREDENTIALS", filepath);            projectId = "blazorwithfirestore";            fireStoreDb = FirestoreDb.Create(projectId);        }        public async Task<List<Employee>> GetAllEmployees()        {            try            {                Query employeeQuery = fireStoreDb.Collection("employees");                QuerySnapshot employeeQuerySnapshot = await employeeQuery.GetSnapshotAsync();                List<Employee> lstEmployee = new List<Employee>();                foreach (DocumentSnapshot documentSnapshot in employeeQuerySnapshot.Documents)                {                    if (documentSnapshot.Exists)                    {                        Dictionary<string, object> city = documentSnapshot.ToDictionary();                        string json = JsonConvert.SerializeObject(city);                        Employee newuser = JsonConvert.DeserializeObject<Employee>(json);                        newuser.EmployeeId = documentSnapshot.Id;                        newuser.date = documentSnapshot.CreateTime.Value.ToDateTime();                        lstEmployee.Add(newuser);                    }                }                List<Employee> sortedEmployeeList = lstEmployee.OrderBy(x => x.date).ToList();                return sortedEmployeeList;            }            catch            {                throw;            }        }        public async void AddEmployee(Employee employee)        {            try            {                CollectionReference colRef = fireStoreDb.Collection("employees");                await colRef.AddAsync(employee);            }            catch            {                throw;            }        }        public async void UpdateEmployee(Employee employee)        {            try            {                DocumentReference empRef = fireStoreDb.Collection("employees").Document(employee.EmployeeId);                await empRef.SetAsync(employee, SetOptions.Overwrite);            }            catch            {                throw;            }        }        public async Task<Employee> GetEmployeeData(string id)        {            try            {                DocumentReference docRef = fireStoreDb.Collection("employees").Document(id);                DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();                if (snapshot.Exists)                {                    Employee emp = snapshot.ConvertTo<Employee>();                    emp.EmployeeId = snapshot.Id;                    return emp;                }                else                {                    return new Employee();                }            }            catch            {                throw;            }        }        public async void DeleteEmployee(string id)        {            try            {                DocumentReference empRef = fireStoreDb.Collection("employees").Document(id);                await empRef.DeleteAsync();            }            catch            {                throw;            }        }        public async Task<List<Cities>> GetCityData()        {            try            {                Query citiesQuery = fireStoreDb.Collection("cities");                QuerySnapshot citiesQuerySnapshot = await citiesQuery.GetSnapshotAsync();                List<Cities> lstCity = new List<Cities>();                foreach (DocumentSnapshot documentSnapshot in citiesQuerySnapshot.Documents)                {                    if (documentSnapshot.Exists)                    {                        Dictionary<string, object> city = documentSnapshot.ToDictionary();                        string json = JsonConvert.SerializeObject(city);                        Cities newCity = JsonConvert.DeserializeObject<Cities>(json);                        lstCity.Add(newCity);                    }                }                return lstCity;            }            catch            {                throw;            }        }    }}
```

Dans le constructeur de cette classe, nous définissons la variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS`. Vous devez définir la valeur de la variable filepath sur le chemin où le fichier de clé de compte de service JSON est situé sur votre machine. Souvenez-vous que nous avons téléchargé ce fichier dans la section précédente. La variable projectId doit être définie sur l'identifiant de projet de votre projet Firebase.

Nous avons également défini les méthodes pour effectuer les opérations CRUD. La méthode GetAllEmployees récupérera la liste de tous les documents employés de notre collection « employees ». Elle retournera la liste des employés triée par date de création du document.

La méthode `AddEmployee` ajoutera un nouveau document employé à notre collection « employees ». Si la collection n'existe pas, elle créera d'abord la collection puis insérera un nouveau document.

La méthode `UpdateEmployee` mettra à jour les valeurs des champs d'un document employé déjà existant, en fonction de l'identifiant d'employé qui lui est passé. Nous lions l'identifiant du document à la propriété employeeId, donc nous pouvons facilement manipuler les documents.

La méthode `GetEmployeeData` récupérera un seul document employé de notre collection « employees » en fonction de l'identifiant d'employé.

La méthode `DeleteEmployee` supprimera le document pour un employé particulier de la collection « employees ».

La méthode `GetCityData` retournera la liste des villes de la collection « cities ».

### Ajout du contrôleur d'API web à l'application

Faites un clic droit sur le dossier `BlazorWithFirestore.Server/Controllers` et sélectionnez Ajouter >> Nouvel Élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez Web dans le panneau de gauche, puis sélectionnez « API Controller Class » dans le panneau des modèles et donnez le nom EmployeeController.cs. Cliquez sur Ajouter.

Cela créera notre classe API EmployeeController. Nous appellerons les méthodes de la classe EmployeeDataAccessLayer pour récupérer les données et les transmettre au côté client.

Ouvrez le fichier `EmployeeController.cs` et mettez le code suivant à l'intérieur.

```
using System;using System.Collections.Generic;using System.Threading.Tasks;using BlazorWithFirestore.Server.DataAccess;using BlazorWithFirestore.Shared.Models;using Microsoft.AspNetCore.Mvc;namespace BlazorWithFirestore.Server.Controllers{    [Route("api/[controller]")]    public class EmployeeController : Controller    {        EmployeeDataAccessLayer objemployee = new EmployeeDataAccessLayer();        [HttpGet]        public Task<List<Employee>> Get()        {            return objemployee.GetAllEmployees();        }        [HttpGet("{id}")]        public Task<Employee> Get(string id)        {            return objemployee.GetEmployeeData(id);        }        [HttpPost]        public void Post([FromBody] Employee employee)        {            objemployee.AddEmployee(employee);        }        [HttpPut]        public void Put([FromBody]Employee employee)        {            objemployee.UpdateEmployee(employee);        }        [HttpDelete("{id}")]        public void Delete(string id)        {            objemployee.DeleteEmployee(id);        }        [HttpGet("GetCities")]        public Task<List<Cities>> GetCities()        {            return objemployee.GetCityData();        }    }}
```

### Création du composant Blazor

Nous allons créer le composant dans le dossier `BlazorWithFirestore.Client/Pages`. Le modèle d'application fournit les fichiers Counter et Fetch Data par défaut dans ce dossier. Avant d'ajouter notre propre fichier de composant, nous allons supprimer ces deux fichiers par défaut pour rendre notre solution plus propre. Faites un clic droit sur le dossier `BlazorWithFirestore.Client/Pages` puis sélectionnez Ajouter >> Nouvel Élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira, sélectionnez « ASP.NET Core » dans le panneau de gauche, puis sélectionnez « Razor Page » dans le panneau des modèles et nommez-le EmployeeData.cshtml. Cliquez sur Ajouter. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Op5ktwMN2KAvOvrDx0M3ez3qA8uj3-5Y5ljt)

Cela ajoutera une page `EmployeeData.cshtml` à notre dossier BlazorSPA.Client/Pages. Cette page razor aura deux fichiers : EmployeeData.cshtml et EmployeeData.cshtml.cs.

### Ajout des références pour JS Interop

Nous allons utiliser une boîte de dialogue modale bootstrap dans notre application. Nous allons également inclure quelques icônes Font Awesome pour le style dans l'application. Pour pouvoir utiliser ces deux bibliothèques, nous devons ajouter les références CDN pour permettre l'interopérabilité JS.

```
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
```

Ici, nous avons inclus les références CDN, qui nous permettront d'utiliser la boîte de dialogue modale bootstrap et les icônes Font Awesome dans nos applications. Maintenant, nous allons ajouter des codes à nos fichiers de vue.

### EmployeeData.cshtml.cs

Ouvrez `EmployeeData.cshtml.cs` et mettez le code suivant à l'intérieur.

```
using System;using System.Collections.Generic;using System.Linq;using System.Net.Http;using System.Threading.Tasks;using BlazorWithFirestore.Shared.Models;using Microsoft.AspNetCore.Blazor;using Microsoft.AspNetCore.Blazor.Components;namespace BlazorWithFirestore.Client.Pages{    public class EmployeeDataModel : BlazorComponent    {        [Inject]        protected HttpClient Http { get; set; }        protected List<Employee> empList = new List<Employee>();        protected List<Cities> cityList = new List<Cities>();        protected Employee emp = new Employee();        protected string modalTitle { get; set; }        protected string searchString { get; set; }        protected override async Task OnInitAsync()        {            await GetCityList();            await GetEmployeeList();        }        protected async Task GetCityList()        {            cityList = await Http.GetJsonAsync<List<Cities>>("api/Employee/GetCities");        }        protected async Task GetEmployeeList()        {            empList = await Http.GetJsonAsync<List<Employee>>("api/Employee");        }        protected void AddEmployee()        {            emp = new Employee();            modalTitle = "Ajouter un employé";        }        protected async Task EditEmployee(string empID)        {            emp = await Http.GetJsonAsync<Employee>("/api/Employee/" + empID);            modalTitle = "Modifier un employé";        }        protected async Task SaveEmployee()        {            if (emp.EmployeeId != null)            {                await Http.SendJsonAsync(HttpMethod.Put, "api/Employee/", emp);            }            else            {                await Http.SendJsonAsync(HttpMethod.Post, "/api/Employee/", emp);            }            await GetEmployeeList();        }        protected async Task DeleteConfirm(string empID)        {            emp = await Http.GetJsonAsync<Employee>("/api/Employee/" + empID);        }        protected async Task DeleteEmployee(string empID)        {            Console.WriteLine(empID);            await Http.DeleteAsync("api/Employee/" + empID);            await GetEmployeeList();        }        protected async Task SearchEmployee()        {            await GetEmployeeList();            if (searchString != "")            {                empList = empList.Where(                x => x.EmployeeName.IndexOf(searchString,                StringComparison.OrdinalIgnoreCase) != -1).ToList();            }        }    }}
```

Ici, nous avons défini la classe EmployeeDataModel, qui hérite de BlazorComponent. Cela permet à la classe EmployeeDataModel d'agir comme un composant Blazor.

Nous injectons également le service HttpClient pour activer les appels d'API web à notre API EmployeeController.

Nous utiliserons les deux variables empList et cityList pour contenir les données de nos collections Employee et Cities respectivement. La propriété modalTitle, qui est de type string, est utilisée pour contenir le titre qui sera affiché dans la boîte de dialogue modale. La valeur fournie dans la boîte de recherche est stockée dans la propriété searchString qui est également de type string.

La méthode `GetCityList` effectuera un appel à notre méthode d'API web GetCities pour récupérer la liste des données de ville de la collection cities. La méthode `GetEmployeeList` enverra une requête GET à notre API web pour récupérer la liste des données des employés de la table Employee.

Nous invoquons ces deux méthodes à l'intérieur de la méthode `OnInitAsync`, pour nous assurer que les données des employés et les données des villes seront disponibles lors du chargement de la page.

La méthode `AddEmployee` initialisera une instance vide de l'objet Employee et définira la propriété modalTitle, qui affichera le message de titre sur la fenêtre contextuelle modale d'ajout.

La méthode `EditEmployee` acceptera l'identifiant de l'employé comme paramètre. Elle enverra une requête GET à notre API web pour récupérer l'enregistrement de l'employé correspondant à l'identifiant de l'employé fourni.

Nous utiliserons la méthode `SaveEmployee` pour enregistrer l'enregistrement de l'employé pour les requêtes d'ajout et de modification. Pour différencier les requêtes d'ajout et de modification, nous utiliserons la propriété EmployeeId de l'objet Employee. Si une requête de modification est effectuée, alors la propriété EmployeeId contient une valeur de chaîne, et nous enverrons une requête PUT à notre API web, qui mettra à jour l'enregistrement de l'employé. Sinon, si nous effectuons une requête d'ajout, alors la propriété EmployeeId n'est pas initialisée, et donc elle sera nulle. Dans ce cas, nous devons envoyer une requête POST à notre API web, qui créera un nouvel enregistrement d'employé.

La méthode `DeleteConfirm` acceptera l'identifiant de l'employé comme paramètre. Elle récupérera les données de l'employé correspondant à l'identifiant de l'employé fourni.

La méthode `DeleteEmployee` enverra une requête de suppression à notre API et passera l'identifiant de l'employé comme paramètre. Elle appellera ensuite la méthode GetEmployeeList pour rafraîchir la vue avec la liste mise à jour des données des employés.

La méthode `SearchEmployee` est utilisée pour implémenter la recherche par nom d'employé. Nous retournerons tous les enregistrements de l'employé qui correspondent aux critères de recherche, soit entièrement, soit partiellement. Pour rendre la recherche plus efficace, nous ignorerons la casse du texte de recherche. Cela signifie que le résultat de la recherche sera le même que le texte de recherche soit en majuscules ou en minuscules.

### EmployeeData.cshtml

Ouvrez la page `EmployeeData.cshtml` et mettez le code suivant à l'intérieur.

```
@page "/employeerecords"@inherits EmployeeDataModel<h1>Données des employés</h1><div class="container">    <div class="row">        <div class="col-xs-3">            <button class="btn btn-primary" data-toggle="modal" data-target="#AddEditEmpModal" onclick="@AddEmployee">                <i class="fa fa-user-plus"></i>                Ajouter un employé            </button>        </div>        <div class="input-group col-md-4 offset-md-5">            <input type="text" class="form-control" placeholder="Rechercher un employé" bind="@searchString" />            <div class="input-group-append">                <button class="btn btn-info" onclick="@SearchEmployee">                    <i class="fa fa-search"></i>                </button>            </div>        </div>    </div></div><br />@if (empList == null){    <p><em>Chargement...</em></p>}else{    <table class='table'>        <thead>            <tr>                <th>Nom</th>                <th>Genre</th>                <th>Poste</th>                <th>Ville</th>            </tr>        </thead>        <tbody>            @foreach (var emp in empList)            {                <tr>                    <td>@emp.EmployeeName</td>                    <td>@emp.Gender</td>                    <td>@emp.Designation</td>                    <td>@emp.CityName</td>                    <td>                        <button class="btn btn-outline-dark" data-toggle="modal" data-target="#AddEditEmpModal"                                onclick="@(async () => await EditEmployee(@emp.EmployeeId))">                            <i class="fa fa-pencil-square-o"></i>                            Modifier                        </button>                        <button class="btn btn-outline-danger" data-toggle="modal" data-target="#deleteEmpModal"                                onclick="@(async () => await DeleteConfirm(@emp.EmployeeId))">                            <i class="fa fa-trash-o"></i>                            Supprimer                        </button>                    </td>                </tr>            }        </tbody>    </table>}<div class="modal fade" id="AddEditEmpModal">    <div class="modal-dialog">        <div class="modal-content">            <div class="modal-header">                <h3 class="modal-title">@modalTitle</h3>                <button type="button" class="close" data-dismiss="modal">                    <span aria-hidden="true">X</span>                </button>            </div>            <div class="modal-body">                <form>                    <div class="form-group">                        <label class="control-label">Nom</label>                        <input class="form-control" bind="@emp.EmployeeName" />                    </div>                    <div class="form-group">                        <label class="control-label">Genre</label>                        <select class="form-control" bind="@emp.Gender">                            <option value="">-- Sélectionner le genre --</option>                            <option value="Male">Homme</option>                            <option value="Female">Femme</option>                        </select>                    </div>                    <div class="form-group">                        <label class="control-label">Poste</label>                        <input class="form-control" bind="@emp.Designation" />                    </div>                    <div class="form-group">                        <label class="control-label">Ville</label>                        <select class="form-control" bind="@emp.CityName">                            <option value="-- Sélectionner la ville --">-- Sélectionner la ville --</option>                            @foreach (var city in cityList)                            {                                <option value="@city.CityName">@city.CityName</option>                            }                        </select>                    </div>                </form>            </div>            <div class="modal-footer">                <button class="btn btn-block btn-success"                        onclick="@(async () => await SaveEmployee())" data-dismiss="modal">                    Enregistrer                </button>            </div>        </div>    </div></div><div class="modal fade" id="deleteEmpModal">    <div class="modal-dialog">        <div class="modal-content">            <div class="modal-header">                <h3 class="modal-title">Confirmer la suppression !!!</h3>                <button type="button" class="close" data-dismiss="modal">                    <span aria-hidden="true">X</span>                </button>            </div>            <div class="modal-body">                <table class="table">                    <tr>                        <td>Nom</td>                        <td>@emp.EmployeeName</td>                    </tr>                    <tr>                        <td>Genre</td>                        <td>@emp.Gender</td>                    </tr>                    <tr>                        <td>Poste</td>                        <td>@emp.Designation</td>                    </tr>                    <tr>                        <td>Ville</td>                        <td>@emp.CityName</td>                    </tr>                </table>            </div>            <div class="modal-footer">                <button class="btn btn-danger" data-dismiss="modal"                        onclick="@(async () => await DeleteEmployee(@emp.EmployeeId))">                    Supprimer                </button>                <button data-dismiss="modal" class="btn">Annuler</button>            </div>        </div>    </div></div>
```

Le chemin de notre composant est défini en haut comme « /employeerecords ». Pour utiliser les méthodes définies dans la classe EmployeeDataModel, nous l'héritons en utilisant la directive `@inherits`.

Nous avons défini un bouton Ajouter un employé. En cliquant dessus, ce bouton invoquera la méthode `AddEmployee` et ouvrira une boîte de dialogue modale, qui permet à l'utilisateur de remplir les nouvelles données de l'employé dans un formulaire.

Nous avons également défini notre boîte de recherche et un bouton de recherche correspondant. La boîte de recherche liera la valeur à la propriété searchString. En cliquant sur le bouton de recherche, la méthode `SearchEmployee` sera invoquée, qui retournera la liste filtrée des données selon le texte de recherche. Si la propriété empList n'est pas nulle, nous lierons les données des employés à un tableau pour les afficher sur la page web. Chaque enregistrement d'employé a les deux boutons d'action suivants correspondants :

* Modifier : Ce bouton effectuera deux tâches. Il invoquera la méthode EditEmployee et ouvrira la boîte de dialogue modale de modification de l'employé pour modifier l'enregistrement de l'employé.
* Supprimer : Ce bouton effectuera également deux tâches. Il invoquera la méthode DeleteConfirm et ouvrira une boîte de dialogue modale de confirmation de suppression, demandant à l'utilisateur de confirmer la suppression de l'enregistrement de l'employé.

Nous avons défini un formulaire à l'intérieur de la modale bootstrap pour accepter les entrées utilisateur pour les enregistrements des employés. Les champs d'entrée de ce formulaire se lieront aux propriétés de la classe employé. Le champ Ville est une liste déroulante, qui se liera à la collection des villes de la base de données à l'aide de la variable cityList. Lorsque nous cliquons sur le bouton Enregistrer, la méthode `SaveEmployee` sera invoquée et la boîte de dialogue modale sera fermée.

Lorsque l'utilisateur clique sur le bouton Supprimer correspondant à un enregistrement d'employé, une autre boîte de dialogue modale bootstrap sera affichée. Cette modale affichera les données de l'employé dans un tableau et demandera à l'utilisateur de confirmer la suppression. Cliquer sur le bouton Supprimer à l'intérieur de cette boîte de dialogue modale invoquera la méthode DeleteEmployee et fermera la modale. Cliquer sur le bouton Annuler fermera la modale sans effectuer aucune action sur les données.

### Ajout du lien de navigation vers notre composant

Avant d'exécuter l'application, nous allons ajouter le lien de navigation vers notre composant dans le menu de navigation.

Ouvrez la page `BlazorWithFirestore.Client/Shared/NavMenu.cshtml` et ajoutez le lien de navigation suivant :

```
<li class="nav-item px-3">  <NavLink class="nav-link" href="employeerecords">    <span class="oi oi-list-rich" aria-hidden="true"></span> Données des employés  </NavLink></li>
```

Ainsi, nous avons créé avec succès une application monopage (SPA) en utilisant Blazor avec l'aide de Cloud Firestore comme fournisseur de base de données.

### Démo d'exécution

Appuyez sur F5 pour lancer l'application.

Une page web s'ouvrira comme illustré dans l'image ci-dessous. Le menu de navigation à gauche montre le lien de navigation vers la page des données des employés.

![Image](https://cdn-media-1.freecodecamp.org/images/HxKudv9nbDAz4bUBjCJee7r1o5Dfqn2lXuyf)

Vous pouvez effectuer les opérations CRUD sur cette application comme montré dans l'image GIF au début de cet article.

### Conclusion

Nous avons créé une application monopage (SPA) en utilisant Blazor avec l'aide de Google Cloud Firestore comme fournisseur de base de données. Nous avons créé un système de gestion d'enregistrements d'employés exemple et effectué des opérations CRUD dessus. Firestore est une base de données NoSQL, qui nous permet de stocker des données sous forme de collections et de documents. Nous avons également utilisé une fenêtre modale bootstrap pour gérer les entrées utilisateur. Nous avons également implémenté une boîte de recherche pour rechercher dans la liste des employés par nom d'employé.

Veuillez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-CRUD-With-CloudFirestore) et jouez avec pour obtenir une meilleure compréhension.

Obtenez mon livre [Blazor Quick Start Guide](https://amzn.to/2OToEji) pour en savoir plus sur Blazor.

Préparation aux entretiens ? Lisez mon article sur [C# Coding Questions For Technical Interviews](https://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/)

### Voir aussi

* [BlazorGrid — Un composant de grille réutilisable pour Blazor](https://ankitsharmablogs.com/blazorgrid-reusable-grid-component-for-blazor/)
* [Publier un composant Blazor sur la galerie Nuget](https://ankitsharmablogs.com/publishing-blazor-component-to-nuget-gallery/)
* [Déployer une application Blazor sur IIS](https://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)
* [Déployer une application Blazor sur Azure](https://ankitsharmablogs.com/deploying-a-blazor-application-on-azure/)
* [Héberger une application Blazor sur Firebase](https://ankitsharmablogs.com/hosting-a-blazor-application-on-firebase/)
* [CRUD avec Blazor et MongoDB](https://ankitsharmablogs.com/crud-using-blazor-with-mongodb/)
* [Application monopage utilisant Blazor côté serveur](https://ankitsharmablogs.com/single-page-application-using-server-side-blazor/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)