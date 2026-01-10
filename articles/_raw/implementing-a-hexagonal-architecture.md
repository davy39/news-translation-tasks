---
title: How to Implement a Hexagonal Architecture
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-19T21:54:15.000Z'
originalURL: https://freecodecamp.org/news/implementing-a-hexagonal-architecture
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/aluminum-architecture-art-1492232.jpg
tags:
- name: Clean Architecture
  slug: clean-architecture
- name: Hexagonal Architecture
  slug: hexagonal-architecture
- name: Java
  slug: java
- name: spring-boot
  slug: spring-boot
seo_title: null
seo_desc: 'By Bertil Muth

  A hexagonal  architecture simplifies deferring or changing technology decisions.
  You  want to change to a different framework? Write a new adapter. You want  to
  use a database, instead of storing data in files? Again, write an  adapter...'
---

By Bertil Muth

A hexagonal  architecture simplifies deferring or changing technology decisions. You  want to change to a different framework? Write a new adapter. You want  to use a database, instead of storing data in files? Again, write an  adapter for it.

Draw a boundary around the business logic. The hexagon. Anything inside the hexagon must be free from technology concerns.  
 The  outside of the hexagon talks with the inside only by using interfaces,  called ports. Same the other way around. By changing the implementation  of a port, you change the technology.

Isolating  business logic inside the hexagon has another benefit. It enables  writing fast, stable tests for the business logic. They do not depend on  web technology to drive them, for example.

Here’s  an example diagram. It shows Spring MVC technology as boxes with dotted  lines, ports and adapters as solid boxes, and the hexagon without its  internals:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/grafik.png)

An adapter translates between a specific technology and a technology free port. The `PoemController` adapter on the left receives requests and sends commands to the `IReactToCommands` port. The `PoemController` is a regular Spring MVC Controller. Because it actively uses the port, it's called a driver adapter.

`IReactToCommands` is called a driver port. Its implementation is inside the hexagon. It's not shown on the diagram.

On the right side, the `SpringMvcPublisher` adapter implements the `IWriteLines` port. This time, the _hexagon_ calls the adapter through the port. That's why `SpringMvcPublisher` is called a driven adapter. And `IWriteLines` is called a driven port.

I show you how to implement that application. We go all the way from a  user story to a domain model inside the hexagon. We start with a simple  version of the application that prints to the console. Then we switch  to Spring Boot and Spring MVC.

## From a user story to ports & adapters

The company FooBars.io decides to build a Poetry App. The product owner and the developers agree on the following user story:

As a reader  
I want to read at least one poem each day  
So that I thrive as a human being

As acceptance criteria, the team agrees on:

* When the user asks for a poem in a specific language, the system displays a random poem in that language in the console
* It's ok to "simulate" the user at first, i.e. no real user interaction. (This will change in future versions.)
* Supported languages: English, German

The developers meet and draw the following diagram:

![poem-hexagon](https://res.cloudinary.com/practicaldev/image/fetch/s--4a_F9pCz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/02hr6f652yran0dz38h1.PNG)

So the `SimulatedUser` sends commands to the `IReactToCommands` port. It asks for poems in English and German. Here's the code, it's available on [Github](https://github.com/bertilmuth/poem-hexagon).

_poem/simple/driver_adapter/[SimulatedUser.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/simple/driver_adapter/SimulatedUser.java)_

```java
public class SimulatedUser {
    private IReactToCommands driverPort;

    public SimulatedUser(IReactToCommands driverPort) {
        this.driverPort = driverPort;
    }

    public void run() {
        driverPort.reactTo(new AskForPoem("en"));
        driverPort.reactTo(new AskForPoem("de"));
    }
}

```

The `IReactToCommands` port has only one method to receive any kind of command.

_poem/boundary/driver_port/[IReactToCommands.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/driver_port/IReactToCommands.java)_

```java
public interface IReactToCommands{
    void reactTo(Object command);
}

```

`AskForPoem` is the command. Instances are simple, immutable POJOs. They carry the language of the requested poem.

_poem/command/[AskForPoem.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/command/AskForPoem.java)_

```java
public class AskForPoem {
    private String language;

    public AskForPoem(String language) {
        this.language = language;
    }

    public String getLanguage() {
        return language;
    }
}

```

And that's it for the left, driver side of the hexagon. On to the right, driven side.

![poem-hexagon: driven side up next](https://res.cloudinary.com/practicaldev/image/fetch/s--cMUjGG4H--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/8vsbpug5fjfjzs8sfs2y.PNG)

When the `SimulatedUser` asks the `IReactToCommands` port for a poem, the hexagon:

1. Contacts the `IObtainPoems` port for a collection of poems
2. Picks a random poem from the collection
3. Tells the `IWriteLines` port to write the poem to the output device

You can't see Step 2 yet. It happens inside the hexagon, in the  domain model. That's the business logic of the example. So we focus on  Step 1 and Step 3 first.

In Step 1, the collection of poems is a language dependent, hard coded array. It's provided by the `HardcodedPoemLibrary` adapter that implements the `IObtainPoems` port.

_poem/boundary/driven_port/[IObtainPoems.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/driven_port/IObtainPoems.java)_

```java
public interface IObtainPoems {
    String[] getMePoems(String language);
}

```

_poem/simple/driven_adapter/[HardcodedPoemLibrary.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/simple/driven_adapter/HardcodedPoemLibrary.java)_

```java
public class HardcodedPoemLibrary implements IObtainPoems {
    public String[] getMePoems(String language) {
        if ("de".equals(language)) {
            return new String[] { /* Omitted for brevity */ };
        } else { 
            return new String[] { /* Omitted for brevity */ };
        }
    }
}

```

In Step 3, the `ConsoleWriter` adapter writes the lines of the poems to the output device, i.e. the console.

_poem/boundary/driven_port/[IWriteLines.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/driven_port/IWriteLines.java)_

```java
public interface IWriteLines {
    void writeLines(String[] strings);
}

```

_poem/simple/driven_adapter/[ConsoleWriter.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/simple/driven_adapter/ConsoleWriter.java)_

```java
public class ConsoleWriter implements IWriteLines {
    public void writeLines(String[] lines) {
        Objects.requireNonNull(lines);
        for (String line : lines) {
            System.out.println(line);
        }
        System.out.println("");
    }
}

```

We have created all the ports, and a simple implementation of all the  adapters. So far, the inside of the hexagon remained a mystery. It's up  next.

![poem-hexagon: inside up next](https://res.cloudinary.com/practicaldev/image/fetch/s---tA0dZqp--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/efcfrsrwb9jei5uik63k.PNG)

# Command handlers (inside the hexagon)

When a user asks for a poem, the system displays a random poem.  
Similar in the code: when the `IReactToCommands` port receives an `AskForPoem`command, the hexagon calls a `DisplayRandomPoem` command handler.

The `DisplayRandomPoem` command handler obtains a list of  poems, picks a random one and writes it to the output device. This is  exactly the list of steps we talked about in the last clause.

_poem/boundary/internal/command_handler/[DisplayRandomPoem.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/internal/command_handler/DisplayRandomPoem.java)_

```java
public class DisplayRandomPoem implements Consumer<AskForPoem> {
        /* Omitted for brevity */

    @Override
    public void accept(AskForPoem askForPoem) {
        List<Poem> poems = obtainPoems(askForPoem);
        Optional<Poem> poem = pickRandomPoem(poems);
        writeLines(poem);   
    }

        /* Rest of class omitted for brevity */
}  
```

It's also the job of the command handler to translate between the domain model data and the data used in the port interfaces.

# Tying commands to command handlers

In my implementation of a hexagonal architecture, there is only a single driver port, `IReactToCommands`. It reacts to all types of commands.

```java
public interface IReactToCommands{
    void reactTo(Object command);
}

```

The `Boundary` class is the implementation of the `IReactToCommands` port. It creates a behavior model using a [library](https://github.com/bertilmuth/requirementsascode). The behavior model maps each command type to a command handler. Then, a behavior dispatches the commands based on the behavior model.

_poem/boundary/[Boundary.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/Boundary.java)_

```java
public class Boundary implements IReactToCommands, BehaviorModel {
  private final IObtainPoems poemObtainer;
  private final IWriteLines lineWriter;
  private final StatelessBehavior behavior;

  private static final Class<AskForPoem> asksForPoem = AskForPoem.class;

  public Boundary(IObtainPoems poemObtainer, IWriteLines lineWriter) {
    this.poemObtainer = poemObtainer;
    this.lineWriter = lineWriter;
    this.behavior = StatelessBehavior.of(this);
  }

  @Override
  public Model model() {
    return Model.builder()
        .user(asksForPoem).system(displaysRandomPoem())
        .build();
  }

  @Override
  public void reactTo(Object commandObject) {
    behavior.reactTo(commandObject);
  }

  private Consumer<AskForPoem> displaysRandomPoem() {
    return new DisplayRandomPoem(poemObtainer, lineWriter);
  }
}
```

# The domain model

The domain model of the example doesn’t have very interesting functionality. The [RandomPoemPicker](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/internal/domain/RandomPoemPicker.java) picks a random poem from a list.

A [Poem](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/internal/domain/Poem.java) has a constructor that takes a String containing line separators, and splits it into verses.

The really interesting bit about the example domain model: it doesn’t  refer to a database or any other technology, not even by interface!

That means that you can test the domain model with [plain unit tests](https://github.com/bertilmuth/poem-hexagon/blob/master/src/test/java/poem/boundary/internal/domain/RandomPoemPickerTest.java). You don’t need to mock anything.

Such a pure domain model is not a necessary property of an  application implementing a hexagonal architecture. But I like the  decoupling and testability it provides.

# Plug adapters into ports, and that's it

A final step remains to make the application work. The application  needs a main class that creates the driven adapters. It injects them  into the boundary.   
It then creates the driver adapter,  for the boundary, and runs it.

_poem/simple/[Main.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/simple/Main.java)_

```java
public class Main {
    public static void main(String[] args) {
        new Main().startApplication();
    }

    private void startApplication() {
        // Instantiate driven, right-side adapters
        HardcodedPoemLibrary poemLibrary = new HardcodedPoemLibrary();
        ConsoleWriter consoleWriter = new ConsoleWriter();

        // Inject driven adapters into boundary
        Boundary boundary = new Boundary(poemLibrary, consoleWriter);

        // Start the driver adapter for the application
        new SimulatedUser(boundary).run();
    }
}

```

And that's it! The team shows the result to the product owner. And  she's happy with the progress. Time for a little celebration.

![hexagon-poem the completed application](https://res.cloudinary.com/practicaldev/image/fetch/s--PDHorQ0r--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/6pe5yam3xe68m11bojff.PNG)

# Switching to Spring

The team decides to turn the poem app into a web application. And to  store poems in a real database. They agree to use the Spring framework  to implement it.  
Before they start coding, the team meets and draws the following diagram:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/grafik-1.png)

Instead of a `SimulatedUser`, there is a `PoemController` now, that sends commands to the hexagon.

_poem/springboot/driver_adapter/[PoemController.java](https://github.com/bertilmuth/poem-springboot/blob/master/src/main/java/poem/springboot/driver_adapter/PoemController.java)_

```java
@Controller
public class PoemController {
    private SpringMvcBoundary springMvcBoundary;

    @Autowired
    public PoemController(SpringMvcBoundary springMvcBoundary) {
        this.springMvcBoundary = springMvcBoundary;
    }

    @GetMapping("/askForPoem")
    public String askForPoem(@RequestParam(name = "lang", required = false, defaultValue = "en") String language,
            Model webModel) {
        springMvcBoundary.basedOn(webModel).reactTo(new AskForPoem(language));

        return "poemView";
    }
}
```

When receiving a command, the `PoemController` calls `springMvcBoundary.basedOn(webModel)`. This creates a new `Boundary` instance, based on the `webModel` of the request:

_poem/springboot/boundary/[SpringMvcBoundary.java](https://github.com/bertilmuth/poem-springboot/blob/master/src/main/java/poem/springboot/boundary/SpringMvcBoundary.java)_

```java
public class SpringMvcBoundary {
    private final IObtainPoems poemObtainer;

    public SpringMvcBoundary(IObtainPoems poemObtainer) {
        this.poemObtainer = poemObtainer;
    }

    public IReactToCommands basedOn(Model webModel) {
        SpringMvcPublisher webPublisher = new SpringMvcPublisher(webModel);
        IReactToCommands boundary = new Boundary(poemObtainer, webPublisher);
        return boundary;
    }
}
```

The call to `reactTo()` sends the command to the boundary, as before. On the right side of the hexagon, the `SpringMvcPublisher` adds an attribute `lines` to the Spring MVC model. That's the value Thymeleaf uses to insert the lines into the web page.

_poem/springboot/driven_adapter/[SpringMvcPublisher.java](https://github.com/bertilmuth/poem-springboot/blob/master/src/main/java/poem/springboot/driven_adapter/SpringMvcPublisher.java)_

```java
public class SpringMvcPublisher implements IWriteLines {
    static final String LINES_ATTRIBUTE = "lines";

    private Model webModel;

    public SpringMvcPublisher(Model webModel) {
        this.webModel = webModel;
    }

    public void writeLines(String[] lines) {
        Objects.requireNonNull(lines);
        webModel.addAttribute(LINES_ATTRIBUTE, lines);
    }
}

```

The team also implements a `PoemRepositoryAdapter` to access the `PoemRepository`. The adapter gets the `Poem` objects from the database. It returns the texts of all poems as a String array.

_poem/springboot/driven_adapter/[PoemRepositoryAdapter.java](https://github.com/bertilmuth/poem-springboot/blob/master/src/main/java/poem/springboot/driven_adapter/PoemRepositoryAdapter.java)_

```java
public class PoemRepositoryAdapter implements IObtainPoems {
    private PoemRepository poemRepository;

    public PoemRepositoryAdapter(PoemRepository poemRepository) {
        this.poemRepository = poemRepository;
    }

    @Override
    public String[] getMePoems(String language) {
        Collection<Poem> poems = poemRepository.findByLanguage(language);
        final String[] poemsArray = poems.stream()
            .map(p -> p.getText())
            .collect(Collectors.toList())
            .toArray(new String[0]);
        return poemsArray;
    }
}

```

Finally, the team implements the [Application](https://github.com/bertilmuth/poem-springboot/blob/master/src/main/java/poem/springboot/Application.java) class that sets up an example repository and plugs the adapters into the ports.

And that's it. The switch to Spring is complete.

# Conclusion

There are many ways to implement a hexagonal architecture. I showed  you a straightforward approach that provides an easy to use, command  driven API for the hexagon. It reduces the number of interfaces you need  to implement. And it leads to a pure domain model.

If you want to get more information on the topic, read [Alistair Cockburn’s original article on the subject](http://archive.is/5j2NI).

The example in this article is inspired by a three part series of [talks](https://www.youtube.com/playlist?list=PLGl1Jc8ErU1w27y8-7Gdcloy1tHO7NriL) by Alistair Cockburn on the subject.

_Last updated on 30 July 2021.__. If you want to keep up with what I’m doing or drop me a note, follow me on_ [_dev.to_](https://dev.to/bertilmuth)_,_ [_LinkedIn_](https://www.linkedin.com/in/bertilmuth/) _or_ [_Twitter_](https://twitter.com/BertilMuth)_. Or visit my_ [_GitHub project_](https://github.com/bertilmuth/requirementsascode)_. To learn about agile software development,_ [_visit my online course_](https://skl.sh/2Cq497P)_._

