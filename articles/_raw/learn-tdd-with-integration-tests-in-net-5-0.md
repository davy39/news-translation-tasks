---
title: Learn Test-Driven Development with Integration Tests in .NET 5.0
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
seo_title: null
seo_desc: "By Arjav Dave\nTest-Driven Development is a much-debated concept in the\
  \ tech industry. Developers wonder whether they should practice TDD or not, how\
  \ advantageous it is, and so on. \nSo what is Test-Driven Development, or TDD? Simply\
  \ put, TDD dictates ..."
---

By Arjav Dave

Test-Driven Development is a much-debated concept in the tech industry. Developers wonder whether they should practice TDD or not, how advantageous it is, and so on. 

So what is Test-Driven Development, or TDD? Simply put, TDD dictates that you test your code before you push it to production.

Now, there are a number of opinions for what type of tests you should include in TDD. For example, should you include Unit Tests, Integration Tests, System Tests, or even UAT?

In this article, we will go through a real-world example that'll show you how to write integration tests in .NET 5.0 with a TDD methodology. 

For writing tests, we will use the XUnit framework, since it is more extensive than the NUnit or MSTest testing frameworks. [Here](https://www.lambdatest.com/blog/nunit-vs-xunit-vs-mstest/) is a good article if you want to learn more about the difference between these frameworks. 

Secondly, VS Code has always been my choice of IDE, but you can use Visual Studio as well. 

Let's start by laying out our project requirements.

## Project Requirements

TDD requires a very clear understanding of the scope of work. Without that clarity, all the test cases might not be covered.

Let's define what we mean by scope of work. We will be developing a patient admission system for a hospital.

### Business Requirements

* A hospital has X ICU rooms, Y Premium rooms, and Z General rooms.
* ICU and Premium rooms can have a single patient at a time, while General rooms can have 2 patients. Each room has a room number.
* On admitting, the patient has to provide name, age, gender, and phone number.
* It is possible to search a patient via name or phone number.
* The same patient cannot be admitted to multiple beds while they are still checked in.
* A patient cannot be admitted if all the rooms are occupied.

### Model Validation Rules

Based on the above requirements, there are two models we need to worry about, namely Patient and Room.

* A patient's age is between 0 and 150. The length of their name should be between 2 and 40 characters. Gender can be male, female, and other. Phone Number's length should be between 7 and 12 and it should all be digits.
* Room type can be either "ICU", "Premium" or "General".

### Test Cases to implement

Now, that we have defined our rules and requirements, let's start creating test cases. Since it's a basic CRUD application, we will mostly have integration tests.

#### Patient test cases

* Do all the model validation tests.
* Admit the same patient twice
* Check out the same patient twice.
* Admit the same patient to multiple rooms at the same time.
* Search a patient with phone number and name.

## TDD Setup

In the above section we gathered our project requirements. Next we defined the models. Finally, we created the list of test cases which we will implement.

Open your terminal and run the below script to create and setup a new project.

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

The above script creates a solution file named _TDD.sln_. Secondly, we create two projects for TDD and TDD.Tests. Then we add the dependencies for each project. Lastly, we add the projects to the solution and open the project in VS Code.

Before we start testing, we have a bit more setup to do. Basically, integration tests test the a specific module without mocking. So we will be mimicking our application via TestServer.

### Custom WebApplicationFactory

In order to mimic the TestServer, there is a class called [WebApplicationFactory](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.testing.webapplicationfactory-1?view=aspnetcore-5.0) (WAF) which bootstraps the application in memory.

In your **TDD.Tests** project create a file named _PatientTestsDbWAF.cs_ with the following code.

```
using System.Linq;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.AspNetCore;


namespace TDD.Tests
{
    public class PatientTestsDbWAF&lt;TStartup&gt; : WebApplicationFactory&lt;TStartup&gt; where TStartup : class
    {

        protected override IWebHostBuilder CreateWebHostBuilder()
        {
            return WebHost.CreateDefaultBuilder()
                .UseStartup&lt;TStartup&gt;();
        }
        protected override void ConfigureWebHost(IWebHostBuilder builder)
        {
            builder.ConfigureServices(async services =&gt;
           {
               // Remove the app's DbContext registration.
               var descriptor = services.SingleOrDefault(
                      d =&gt; d.ServiceType ==
                          typeof(DbContextOptions&lt;DataContext&gt;));

               if (descriptor != null)
               {
                   services.Remove(descriptor);
               }

               // Add DbContext using an in-memory database for testing.
               services.AddDbContext&lt;DataContext&gt;(options =&gt;
                  {
                      // Use in memory db to not interfere with the original db.
                      options.UseInMemoryDatabase("PatientTestsTDD.db");
                  });
           });
        }
    }
}

```

We are removing the application's DbContext and adding an **in memory** DbContext. This is a necessary step since we don't want to interfere with the original database.

Secondly, we are initialising the database with some dummy data.

Since DataContext is a custom class, it will give compiler error. So we need to create it.

### Data Context

In your **TDD project**, create a file named _DataContext.cs_ with the following code:

```
using Microsoft.EntityFrameworkCore;

namespace TDD
{
    public class DataContext : DbContext
    {
        public DataContext(DbContextOptions options) : base(options) { }

        // For storing the list of patients and their state
        public DbSet&lt;Patient&gt; Patient { get; set; }

        // For the storying the rooms along with their types and capacity
        public DbSet&lt;Room&gt; Room { get; set; }

        // For logging which patients are currently admitted to which room
        public DbSet&lt;RoomPatient&gt; RoomPatient { get; set; }

    }
}

```

Here Patient, Room, and RoomPatient are Entity classes with the required properties, which we will create next.

### Add the Patient property

Again, in your **TDD project**, create a file named _Patient.cs_ and paste in the code below:

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

### Add the Room property

Create another file named _Room.cs_ with the following code:

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

### Add the RoomPatient property

Create the last model file _RoomPatient.cs_ with the following code:

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

Now you shouldn't be getting any more compiler errors.

Lastly, remove the _WeatherForecast.cs_ and _WeatherForecastController.cs_ files.

Go to your terminal in VS Code and run the below command:

```
cd TDD.Tests
dotnet test

```

You will see a nice green result which says that one test has passed.

![Image](https://arjavdave.com/wp-content/uploads/2021/04/Test_Success_1-1024x211.png)
_Test Success_

### Create the Patient Controller

Unfortunately .NET doesn't provide a way to directly test the models in itself. So we will have to create a controller to test it.

Go ahead and create a _PatientController.cs_ file in the Controllers folder in **TDD project** with the below code:

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
            // TODO: Insert the patient into db
            return Created("/patient/1", Patient);
        }
    }
}

```

We created an API to add a patient. In order to test our model we will call this API.

That's all we need to start testing.

## Model Validation Tests

Since we've setup the basic code for testing, let's write a test that fails. We will start our testing with the model validation tests.

### Failing (Red) State

Let's create a new file named _PatientTests.cs_ in your **TDD.Tests project** and delete the file named _UnitTest1.cs_. Copy the below code into your file:

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
    public class PatientTests : IClassFixture&lt;PatientTestsDbWAF&lt;Startup&gt;&gt;
    {
        // HttpClient to call our api's
        private readonly HttpClient httpClient;
        public WebApplicationFactory&lt;Startup&gt; _factory;

        public PatientTests(PatientTestsDbWAF&lt;Startup&gt; factory)
        {
            _factory = factory;

            // Initiate the HttpClient
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
                var context = scope.ServiceProvider.GetService&lt;DataContext&gt;();
                
                // Initialize the database, so that 
                // changes made by other tests are reset. 
                await DBUtilities.InitializeDbForTestsAsync(context);
                
                // Arrange
                var request = new HttpRequestMessage(HttpMethod.Post, "api/patient");

                request.Content = new StringContent(JsonSerializer.Serialize(new Patient
                {
                    Name = Name,
                    PhoneNumber = PhoneNumber,
                    Age = Age,
                    Gender = Gender
                }), Encoding.UTF8, "application/json");

                // Act
                var response = await httpClient.SendAsync(request);

                // Assert
                var StatusCode = response.StatusCode;
                Assert.Equal(ResponseCode, StatusCode);
            }
        }
    }
}

```

The `[Theory]` attribute allows us to mention different parameters for our tests. Because of this, we don't have to write different tests for all the combinations.

Also, DBUtilities is a utility class to reinitialise the database to its initial state. This might seem trivial when we have 1 or 2 tests, but it becomes critical as we add more tests.

### DBUtilities class

The DBUtilities class will initialise your database with 1 patient and 3 different type of rooms.

Create a file named _DBUtilities.cs_ in your **TDD.Tests** project with the below code:

```
using System.Threading.Tasks;

namespace TDD.Tests
{
    // Helps to initialise the database either from the WAF for the first time
    // Or before running each test.
    public class DBUtilities
    {

        // Clears the database and then,
        //Adds 1 Patient and 3 different types of rooms to the database
        public static async Task InitializeDbForTestsAsync(DataContext context)
        {
            context.RoomPatient.RemoveRange(context.RoomPatient);
            context.Patient.RemoveRange(context.Patient);
            context.Room.RemoveRange(context.Room);
            
            // Arrange
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

Go ahead and run the **dotnet test** command again and you will see 1 passed and 4 failed tests. This is because the 4 tests were expecting BadRequest but were getting a Created result.

![Image](https://arjavdave.com/wp-content/uploads/2021/04/failed_tests-1024x195.png)
_Failing (Red) State_

Let's fix it!

### Success (Green) State

In order to fix these we need to add attributes to our _Patient.cs_ class.

Update the _Patient.cs_ file as below:

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
        [StringLength(40, MinimumLength = 2, ErrorMessage = "The name should be between 2 &amp; 40 characters.")]
        public String Name { get; set; }

        [Required]
        [DataType(DataType.PhoneNumber)]
        [RegularExpression(@"^(\d{7,12})$", ErrorMessage = "Not a valid phone number")]
        public String PhoneNumber { get; set; }

        [Required]
        [Range(1, 150)]
        public int Age { get; set; }

        [Required]
        public String Gender { get; set; }

        public Boolean IsAdmitted { get; set; }

        public IEnumerable&lt;ValidationResult&gt; Validate(ValidationContext validationContext)
        {
            // Only Male, Female or Other gender are allowed
            if (Gender.Equals("Male", System.StringComparison.CurrentCultureIgnoreCase) == false &amp;&amp;
                Gender.Equals("Female", System.StringComparison.CurrentCultureIgnoreCase) == false &amp;&amp;
                Gender.Equals("Other", System.StringComparison.CurrentCultureIgnoreCase) == false)
            {
                yield return new ValidationResult("The gender can either be Male, Female or Other");
            }

            yield return ValidationResult.Success;
        }
    }
}

```

Here, we have added the required attributes. We have also implemented the _IValidatableObject_ interface so that we can verify the _Gender_.

Time to run the **dotnet test** command. You will see a nice green line saying 5 tests passed.

![Image](https://arjavdave.com/wp-content/uploads/2021/04/Tests_passed_2-1024x244.png)

You can add more edge case scenarios in the _InlineData_ to test the Patient model validation tests thoroughly.

## Duplicate Patient Test

We shall now create a test which fails when we try to add a duplicate patient.

### Failing (Red) Test

Create another test in your class _PatientTests._ Add the below code:

```
[Fact]
public async Task PatientDuplicationTestsAsync()
{
    var scopeFactory = _factory.Services;
    using (var scope = scopeFactory.CreateScope())
    {
        var context = scope.ServiceProvider.GetService&lt;DataContext&gt;();
        await DBUtilities.InitializeDbForTestsAsync(context);

        // Arrange
        var Patient = await context.Patient.FirstOrDefaultAsync();

        var Request = new HttpRequestMessage(HttpMethod.Post, "api/patient");
        Request.Content = new StringContent(JsonSerializer.Serialize(Patient), Encoding.UTF8, "application/json");

        // Act
        var Response = await httpClient.SendAsync(Request);

        // Assert
        var StatusCode = Response.StatusCode;
        Assert.Equal(HttpStatusCode.BadRequest, StatusCode);
    }
}

```

We have used a `[Fact]` attribute instead of the `[Theory]` attribute here since we don't want to test the same method with different parameters. Instead, we want to make the same request twice.

Run **dotnet test** to run our newly created test. The test will fail with the message _Assert.Equal() Failure_. Time to fix it.

### Success (Green) Test

To fix the failing test we need to add the implementation for the AddPatient method in _PatientController.cs_. Update the file's code as below:

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
        public async Task&lt;IActionResult&gt; AddPatientAsync([FromBody] Patient Patient)
        {
            var FetchedPatient = await _context.Patient.FirstOrDefaultAsync(x =&gt; x.PhoneNumber == Patient.PhoneNumber);
            // If the patient doesn't exist create a new one
            if (FetchedPatient == null)
            {
                _context.Patient.Add(Patient);
                await _context.SaveChangesAsync();
                return Created($"/patient/{Patient.Id}", Patient);
            }
            // Else throw a bad request
            else
            {
                return BadRequest();
            }
        }
    }
}

```

Run the **dotnet test** again and you will see that the tests have passed.

## Important Notes

As you add more models/domains like Doctors, Staff, Instruments and so on, you will have to create more tests. Make sure to have a different WAF, utility wrappers, and different test files for each of them.

Secondly, the tests in the same file do not run in parallel. But the tests from different files do run in parallel. Therefore, each WAF should have a different database name so that data is not misconfigured.

Lastly, the connections to the original database still need to be setup in the main project.

## How to write good tests

The thought process for creating tests for all scenarios is similar.

That is, you should first identify the requirements. Then, set up a skeleton of methods and classes without implementation. Write tests to verify the implementation. Finally, refactor as needed and rerun the tests.

This tutorial didn't include authentication and authorisation for APIs. You can [read here](https://arjavdave.com/2021/03/31/net-5-setup-authentication-and-authorisation/) on how to set that up.

Since I didn't cover all the test cases here, I have created a [repository on Github](https://github.com/shenanigan/tdd-demo). It covers the implementation for all the test cases if you want to have a look.

You can find the [project here](https://github.com/shenanigan/tdd-demo).

## Conclusion

In order for TDD to be effective you really need to have a clear idea of what the requirements are. If the requirements keep on changing, it'll become very difficult to maintain the tests as well as the project.

TDD mainly covers unit, integration, and functional tests. You will still have to do UAT, Configuration, and Production testing before you go live.

Having said that, TDD is really helpful in making your project bug free. Secondly, it boosts your confidence for the implementation. You will be able to change bits and pieces of your code as long as the tests pass. Lastly, it provides a better architecture for your project.

[Check out more tutorials on .NET here.](https://arjavdave.com/)

