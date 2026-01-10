---
title: Comment implémenter une architecture hexagonale
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
seo_title: Comment implémenter une architecture hexagonale
seo_desc: 'By Bertil Muth

  A hexagonal  architecture simplifies deferring or changing technology decisions.
  You  want to change to a different framework? Write a new adapter. You want  to
  use a database, instead of storing data in files? Again, write an  adapter...'
---

Par Bertil Muth

Une architecture hexagonale simplifie le report ou la modification des décisions technologiques. Vous souhaitez changer de framework ? Écrivez un nouvel adaptateur. Vous souhaitez utiliser une base de données, au lieu de stocker des données dans des fichiers ? Encore une fois, écrivez un adaptateur pour cela.

Tracez une frontière autour de la logique métier. L'hexagone. Tout ce qui se trouve à l'intérieur de l'hexagone doit être exempt de préoccupations technologiques. 
 L'extérieur de l'hexagone communique avec l'intérieur uniquement en utilisant des interfaces, appelées ports. De même dans l'autre sens. En changeant l'implémentation d'un port, vous changez la technologie.

Isoler la logique métier à l'intérieur de l'hexagone présente un autre avantage. Cela permet d'écrire des tests rapides et stables pour la logique métier. Ils ne dépendent pas de la technologie web pour les exécuter, par exemple.

Voici un exemple de diagramme. Il montre la technologie Spring MVC sous forme de boîtes avec des lignes pointillées, les ports et les adaptateurs sous forme de boîtes pleines, et l'hexagone sans ses composants internes :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/grafik.png)

Un adaptateur traduit entre une technologie spécifique et un port indépendant de la technologie. L'adaptateur `PoemController` à gauche reçoit des requêtes et envoie des commandes au port `IReactToCommands`. Le `PoemController` est un contrôleur Spring MVC standard. Parce qu'il utilise activement le port, il est appelé un adaptateur pilote.

`IReactToCommands` est appelé un port pilote. Son implémentation se trouve à l'intérieur de l'hexagone. Elle n'est pas représentée sur le diagramme.

Du côté droit, l'adaptateur `SpringMvcPublisher` implémente le port `IWriteLines`. Cette fois, l'_hexagone_ appelle l'adaptateur via le port. C'est pourquoi `SpringMvcPublisher` est appelé un adaptateur piloté. Et `IWriteLines` est appelé un port piloté.

Je vous montre comment implémenter cette application. Nous allons du début à la fin, d'une histoire utilisateur à un modèle de domaine à l'intérieur de l'hexagone. Nous commençons par une version simple de l'application qui imprime sur la console. Ensuite, nous passons à Spring Boot et Spring MVC.

## D'une histoire utilisateur aux ports et adaptateurs

L'entreprise FooBars.io décide de créer une application de poésie. Le propriétaire du produit et les développeurs conviennent de l'histoire utilisateur suivante :

En tant que lecteur 
Je veux lire au moins un poème chaque jour 
Afin de m'épanouir en tant qu'être humain

En tant que critères d'acceptation, l'équipe convient de ce qui suit :

* Lorsque l'utilisateur demande un poème dans une langue spécifique, le système affiche un poème aléatoire dans cette langue dans la console
* Il est acceptable de "simuler" l'utilisateur au début, c'est-à-dire sans réelle interaction utilisateur. (Cela changera dans les versions futures.)
* Langues prises en charge : Anglais, Allemand

Les développeurs se réunissent et dessinent le diagramme suivant :

![poem-hexagon](https://res.cloudinary.com/practicaldev/image/fetch/s--4a_F9pCz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/02hr6f652yran0dz38h1.PNG)

Ainsi, le `SimulatedUser` envoie des commandes au port `IReactToCommands`. Il demande des poèmes en anglais et en allemand. Voici le code, il est disponible sur [Github](https://github.com/bertilmuth/poem-hexagon).

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

Le port `IReactToCommands` n'a qu'une seule méthode pour recevoir tout type de commande.

_poem/boundary/driver_port/[IReactToCommands.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/driver_port/IReactToCommands.java)_

```java
public interface IReactToCommands{
    void reactTo(Object command);
}

```

`AskForPoem` est la commande. Les instances sont des POJO simples et immuables. Ils transportent la langue du poème demandé.

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

Et c'est tout pour le côté gauche, pilote de l'hexagone. Passons au côté droit, piloté.

![poem-hexagon: côté piloté suivant](https://res.cloudinary.com/practicaldev/image/fetch/s--cMUjGG4H--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/8vsbpug5fjfjzs8sfs2y.PNG)

Lorsque le `SimulatedUser` demande au port `IReactToCommands` un poème, l'hexagone :

1. Contacte le port `IObtainPoems` pour obtenir une collection de poèmes
2. Choisit un poème aléatoire dans la collection
3. Demande au port `IWriteLines` d'écrire le poème sur le périphérique de sortie

Vous ne pouvez pas encore voir l'étape 2. Elle se produit à l'intérieur de l'hexagone, dans le modèle de domaine. C'est la logique métier de l'exemple. Nous nous concentrons donc d'abord sur les étapes 1 et 3.

À l'étape 1, la collection de poèmes est un tableau codé en dur, dépendant de la langue. Il est fourni par l'adaptateur `HardcodedPoemLibrary` qui implémente le port `IObtainPoems`.

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
            return new String[] { /* Omis pour plus de clarté */ };
        } else { 
            return new String[] { /* Omis pour plus de clarté */ };
        }
    }
}

```

À l'étape 3, l'adaptateur `ConsoleWriter` écrit les lignes des poèmes sur le périphérique de sortie, c'est-à-dire la console.

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

Nous avons créé tous les ports et une implémentation simple de tous les adaptateurs. Jusqu'à présent, l'intérieur de l'hexagone est resté un mystère. C'est au tour de l'intérieur.

![poem-hexagon: intérieur suivant](https://res.cloudinary.com/practicaldev/image/fetch/s---tA0dZqp--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/efcfrsrwb9jei5uik63k.PNG)

# Gestionnaires de commandes (à l'intérieur de l'hexagone)

Lorsque l'utilisateur demande un poème, le système affiche un poème aléatoire. 
De même dans le code : lorsque le port `IReactToCommands` reçoit une commande `AskForPoem`, l'hexagone appelle un gestionnaire de commandes `DisplayRandomPoem`.

Le gestionnaire de commandes `DisplayRandomPoem` obtient une liste de poèmes, en choisit un au hasard et l'écrit sur le périphérique de sortie. C'est exactement la liste des étapes dont nous avons parlé dans la dernière clause.

_poem/boundary/internal/command_handler/[DisplayRandomPoem.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/internal/command_handler/DisplayRandomPoem.java)_

```java
public class DisplayRandomPoem implements Consumer<AskForPoem> {
        /* Omis pour plus de clarté */

    @Override
    public void accept(AskForPoem askForPoem) {
        List<Poem> poems = obtainPoems(askForPoem);
        Optional<Poem> poem = pickRandomPoem(poems);
        writeLines(poem);   
    }

        /* Reste de la classe omis pour plus de clarté */
}  
```

C'est également le travail du gestionnaire de commandes de traduire entre les données du modèle de domaine et les données utilisées dans les interfaces de port.

# Lier les commandes aux gestionnaires de commandes

Dans mon implémentation d'une architecture hexagonale, il n'y a qu'un seul port pilote, `IReactToCommands`. Il réagit à tous les types de commandes.

```java
public interface IReactToCommands{
    void reactTo(Object command);
}

```

La classe `Boundary` est l'implémentation du port `IReactToCommands`. Elle crée un modèle de comportement en utilisant une [bibliothèque](https://github.com/bertilmuth/requirementsascode). Le modèle de comportement mappe chaque type de commande à un gestionnaire de commandes. Ensuite, un comportement distribue les commandes en fonction du modèle de comportement.

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

# Le modèle de domaine

Le modèle de domaine de l'exemple n'a pas de fonctionnalités très intéressantes. Le [RandomPoemPicker](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/internal/domain/RandomPoemPicker.java) choisit un poème au hasard dans une liste.

Un [Poem](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/boundary/internal/domain/Poem.java) a un constructeur qui prend une chaîne contenant des séparateurs de ligne et la divise en vers.

L'aspect vraiment intéressant du modèle de domaine de l'exemple : il ne fait référence à aucune base de données ou autre technologie, pas même par interface !

Cela signifie que vous pouvez tester le modèle de domaine avec des [tests unitaires simples](https://github.com/bertilmuth/poem-hexagon/blob/master/src/test/java/poem/boundary/internal/domain/RandomPoemPickerTest.java). Vous n'avez pas besoin de simuler quoi que ce soit.

Un tel modèle de domaine pur n'est pas une propriété nécessaire d'une application implémentant une architecture hexagonale. Mais j'apprécie le découplage et la testabilité qu'il offre.

# Brancher les adaptateurs aux ports, et c'est tout

Une dernière étape reste à faire pour que l'application fonctionne. L'application a besoin d'une classe principale qui crée les adaptateurs pilotés. Elle les injecte dans la frontière.   
Elle crée ensuite l'adaptateur pilote, pour la frontière, et l'exécute.

_poem/simple/[Main.java](https://github.com/bertilmuth/poem-hexagon/blob/master/src/main/java/poem/simple/Main.java)_

```java
public class Main {
    public static void main(String[] args) {
        new Main().startApplication();
    }

    private void startApplication() {
        // Instancier les adaptateurs pilotés, côté droit
        HardcodedPoemLibrary poemLibrary = new HardcodedPoemLibrary();
        ConsoleWriter consoleWriter = new ConsoleWriter();

        // Injecter les adaptateurs pilotés dans la frontière
        Boundary boundary = new Boundary(poemLibrary, consoleWriter);

        // Démarrer l'adaptateur pilote pour l'application
        new SimulatedUser(boundary).run();
    }
}

```

Et c'est tout ! L'équipe montre le résultat au propriétaire du produit. Et elle est heureuse des progrès. Il est temps de faire une petite célébration.

![hexagon-poem l'application complète](https://res.cloudinary.com/practicaldev/image/fetch/s--PDHorQ0r--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/6pe5yam3xe68m11bojff.PNG)

# Passage à Spring

L'équipe décide de transformer l'application de poèmes en une application web. Et de stocker les poèmes dans une vraie base de données. Ils conviennent d'utiliser le framework Spring pour l'implémenter.  
Avant de commencer à coder, l'équipe se réunit et dessine le diagramme suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/grafik-1.png)

Au lieu d'un `SimulatedUser`, il y a maintenant un `PoemController`, qui envoie des commandes à l'hexagone.

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

Lors de la réception d'une commande, le `PoemController` appelle `springMvcBoundary.basedOn(webModel)`. Cela crée une nouvelle instance de `Boundary`, basée sur le `webModel` de la requête :

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

L'appel à `reactTo()` envoie la commande à la frontière, comme avant. Du côté droit de l'hexagone, le `SpringMvcPublisher` ajoute un attribut `lines` au modèle Spring MVC. C'est la valeur que Thymeleaf utilise pour insérer les lignes dans la page web.

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

L'équipe implémente également un `PoemRepositoryAdapter` pour accéder au `PoemRepository`. L'adaptateur obtient les objets `Poem` de la base de données. Il retourne les textes de tous les poèmes sous forme de tableau de chaînes.

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

Enfin, l'équipe implémente la classe [Application](https://github.com/bertilmuth/poem-springboot/blob/master/src/main/java/poem/springboot/Application.java) qui configure un dépôt d'exemple et branche les adaptateurs aux ports.

Et c'est tout. Le passage à Spring est complet.

# Conclusion

Il existe de nombreuses façons d'implémenter une architecture hexagonale. Je vous ai montré une approche simple qui fournit une API facile à utiliser, pilotée par des commandes pour l'hexagone. Elle réduit le nombre d'interfaces que vous devez implémenter. Et elle conduit à un modèle de domaine pur.

Si vous souhaitez obtenir plus d'informations sur le sujet, lisez [l'article original d'Alistair Cockburn sur le sujet](http://archive.is/5j2NI).

L'exemple dans cet article est inspiré d'une série de trois [conférences](https://www.youtube.com/playlist?list=PLGl1Jc8ErU1w27y8-7Gdcloy1tHO7NriL) d'Alistair Cockburn sur le sujet.

_Dernière mise à jour le 30 juillet 2021.__. Si vous souhaitez suivre ce que je fais ou me laisser un mot, suivez-moi sur_ [_dev.to_](https://dev.to/bertilmuth)_,_ [_LinkedIn_](https://www.linkedin.com/in/bertilmuth/) _ou_ [_Twitter_](https://twitter.com/BertilMuth)_. Ou visitez mon_ [_projet GitHub_](https://github.com/bertilmuth/requirementsascode)_. Pour en savoir plus sur le développement logiciel agile,_ [_visitez mon cours en ligne_](https://skl.sh/2Cq497P)_._