---
title: Comment construire une architecture propre moderne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-12T15:28:31.000Z'
originalURL: https://freecodecamp.org/news/modern-clean-architecture
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/300px-Guggenheim-New_York-interior-20060717.jpg
tags:
- name: Clean Architecture
  slug: clean-architecture
- name: clean code
  slug: clean-code
- name: software architecture
  slug: software-architecture
seo_title: Comment construire une architecture propre moderne
seo_desc: 'By Bertil Muth

  Clean Architecture is a term coined by Robert C. Martin. The main idea is that entities
  and use cases are independent of frameworks, UI, the database, and external services.

  A Clean Architecture style has a positive effect on maintaina...'
---

Par Bertil Muth

[Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) est un terme inventé par Robert C. Martin. L'idée principale est que les entités et les cas d'utilisation sont indépendants des frameworks, de l'interface utilisateur, de la base de données et des services externes.

Un style d'architecture propre a un effet positif sur la maintenabilité parce que :

* Nous pouvons tester les entités de domaine et les cas d'utilisation sans framework, interface utilisateur ou infrastructure.
* Les décisions technologiques peuvent changer sans affecter le code de domaine, et vice versa. Il est même possible de passer à un nouveau framework avec un effort limité.

Mon objectif est d'aplatir la courbe d'apprentissage et de réduire l'effort qu'il pourrait vous prendre pour implémenter une architecture propre. C'est pourquoi j'ai créé les bibliothèques [Modern Clean Architecture](https://github.com/bertilmuth/modern-clean-architecture).

Dans cet article, je vais vous montrer comment créer une application avec une architecture propre moderne, d'un front-end HTML/JavaScript à un back-end Spring Boot. L'accent sera mis sur le back-end.

Commençons par un aperçu de l'application exemple – un classique intemporel, l'application TODO.

## Application exemple de liste de tâches

Une _liste de tâches_ est une collection de _tâches_. Une tâche a un _nom_, et est soit _complétée_ soit non. En tant qu'utilisateur, vous pouvez :

* Créer une seule liste de tâches et la persister
* Ajouter une tâche
* Compléter une tâche, ou la "décompléter"
* Supprimer une tâche
* Lister toutes les tâches
* Filtrer les tâches complétées/non complétées

Voici à quoi ressemble une liste de tâches avec 1 tâche non complétée et 2 tâches complétées :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/grafik-1.png)

Nous commencerons par le cœur de l'application, les entités de domaine. Ensuite, nous travaillerons vers l'extérieur jusqu'au front-end.

## Les entités de domaine

Les entités de domaine centrales sont [TodoList](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/TodoList.java) et [Task](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/Task.java).

L'entité _TodoList_ contient :

* un identifiant unique,
* une liste de tâches,
* des méthodes de domaine pour ajouter, compléter et supprimer des tâches

L'entité `TodoList` ne contient pas de setters publics. Les setters briseraient l'encapsulation appropriée.

Voici une partie de l'entité [TodoList](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/TodoList.java). Les annotations [Lombok](https://projectlombok.org/) raccourcissent le code.

``` Java
public class TodoList implements AggregateRoot<TodoList, TodoListId> {
	private final TodoListId id;
	private final List<Task> tasks;
	
	@Value(staticConstructor = "of")
	public static class TodoListId implements Identifier {
		@NonNull
		UUID uuid;
	}

	@Override
	public TodoListId getId() {
		return id;
	}
	...
	public TaskId addTask(String taskName) {
		if (taskName == null || isWhitespaceName(taskName)) {
			throw new IllegalTaskName("Veuillez spécifier un nom de tâche non nul et non vide !");
		}
		TaskId taskId = add(TaskId.of(UUID.randomUUID()), taskName, false);
		return taskId;
	}
  	...
	public void deleteTask(TaskId task) {
		Optional<Task> foundTask = findTask(task);
		foundTask.ifPresent(tasks::remove);
	}
 	...
}
```

À quoi sert l'interface `AggregateRoot` ? Aggregate root est un terme de Domain Driven Design (DDD) par Eric Evans :

> Un agrégat est un ensemble d'objets associés que nous traitons comme une unité pour les modifications de données. Chaque agrégat a une racine et une frontière. La frontière définit ce qui est à l'intérieur de l'agrégat. La racine est une entité spécifique unique contenue dans l'agrégat.

Nous pouvons changer l'état de l'agrégat uniquement par la racine de l'agrégat. Dans notre exemple, cela signifie : nous devons toujours utiliser le `TodoList` pour ajouter, supprimer ou modifier une tâche.

Cela permet à `TodoList` de faire respecter les contraintes. Par exemple, nous ne pouvons pas ajouter une tâche avec un nom vide à la liste.

L'interface `AggregateRoot` fait partie de la bibliothèque [jMolecules](https://github.com/xmolecules/jmolecules). Cette bibliothèque rend les concepts DDD explicites dans le code de domaine. Pendant la construction, [un plugin ByteBuddy](https://github.com/xmolecules/jmolecules-integrations/tree/main/jmolecules-bytebuddy) mappe les annotations aux annotations Spring Data.

Ainsi, nous n'avons qu'un seul modèle, à la fois pour représenter les concepts de domaine et la persistance. Pourtant, nous n'avons aucune annotation spécifique à la persistance dans le code de domaine. Nous ne nous lions à aucun framework.

La classe [_Task_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/Task.java) est similaire, mais elle implémente l'interface _Entity_ de jMolecules à la place :

```java
public class Task implements Entity<TodoList, TaskId> {
	private final TaskId id;
	private final String name;
	private final boolean completed;
	
	@Value(staticConstructor = "of")
	public static class TaskId implements Identifier {
		@NonNull
		UUID uuid;
	}

	Task(@NonNull TaskId id, @NonNull String name, boolean completed) {
		this.id = id;
		this.name = name;
		this.completed = completed;
	}
}
```

Le constructeur de _Task_ est package private. Ainsi, nous ne pouvons pas créer une instance de _Task_ depuis l'extérieur du [package de domaine](https://github.com/bertilmuth/modern-clean-architecture/tree/main/samples/todolist/src/main/java/com/example/todolist/domain). Et la classe _Task_ est immutable. Aucun changement de son état n'est possible depuis l'extérieur de la frontière de l'agrégat.

Nous avons besoin d'un dépôt pour stocker le _TodoList_. Pour rester dans les termes de domaine dans le code de domaine, il est appelé [_TodoLists_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/TodoLists.java) :

``` java
public interface TodoLists extends Repository<TodoList, TodoListId> {
	TodoList save(TodoList entity);
	Optional<TodoList> findById(TodoListId id);
	Iterable<TodoList> findAll();
}
```

Encore une fois, le code utilise une annotation jMolecues : _Repository_. Pendant la construction, le plugin ByteBuddy le traduit en un dépôt Spring Data.

Nous allons sauter les exceptions de domaine, car il n'y a rien de spécial à leur sujet. C'est le [package de domaine](https://github.com/bertilmuth/modern-clean-architecture/tree/main/samples/todolist/src/main/java/com/example/todolist/domain) complet.

## Le comportement de l'application (et les cas d'utilisation)

Ensuite, nous définissons le comportement de l'application visible par l'utilisateur final. Toute interaction de l'utilisateur avec l'application se fait comme suit :

1. L'interface utilisateur envoie une _requête_.
2. Le backend réagit en exécutant un _gestionnaire de requêtes_. Le gestionnaire de requêtes fait tout ce qui est nécessaire pour satisfaire la requête : 
- Accéder à la base de données 
- Appeler des services externes 
- Appeler des méthodes d'entité de domaine
3. Le gestionnaire de requêtes **peut** retourner une _réponse_.

Nous implémentons un _gestionnaire de requêtes_ avec une interface fonctionnelle Java 8.

Un gestionnaire qui retourne une _réponse_ implémente l'interface `java.util.Function`. Voici le code du gestionnaire [_AddTask_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/AddTask.java). Ce gestionnaire

* extrait l'identifiant de la liste de tâches et le nom de la tâche d'une [_AddTaskRequest_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/request/AddTaskRequest.java)_,
* trouve la liste de tâches dans le dépôt (ou lance une exception),
* ajoute une tâche avec le nom de la requête à la liste,
* retourne une [_AddTaskResponse_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/response/AddTaskResponse.java) avec l'identifiant de la tâche ajoutée.

``` java
@AllArgsConstructor
class AddTask implements Function<AddTaskRequest, AddTaskResponse> {
	@NonNull
	private final TodoLists repository;

	@Override
	public AddTaskResponse apply(@NonNull AddTaskRequest request) {
		final UUID todoListUuid = request.getTodoListUuid();
		final String taskName = request.getTaskName();
		
		final TodoList todoList = repository.findById(TodoListId.of(todoListUuid))
			.orElseThrow(() -> new TodoListNotFound("Le dépôt ne contient pas de TodoList avec l'identifiant " + todoListUuid));

		TaskId taskId = todoList.addTask(taskName);
		repository.save(todoList);

		return new AddTaskResponse(taskId.getUuid());
	}
}
```

Lombok crée un constructeur avec l'interface de dépôt _TodoLists_ comme argument de constructeur. Nous passons toute dépendance externe sous forme d'interface au constructeur du gestionnaire.

Les requêtes et les réponses sont des objets immutables :

``` java
@Value
public class AddTaskRequest {
	@NonNull
	UUID todoListUuid;

	@NonNull
	String taskName;
}
```

Les bibliothèques Modern Clean Architecture les (dé)sérialisent depuis/vers JSON.

Ensuite, un exemple de gestionnaire qui ne retourne pas de réponse. Le gestionnaire [_DeleteTask_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/DeleteTask.java) reçoit une [_DeleteTaskRequest_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/request/DeleteTaskRequest.java). Comme le gestionnaire ne retourne pas de réponse, il implémente l'interface _Consumer_.

``` java
@AllArgsConstructor
class DeleteTask implements Consumer<DeleteTaskRequest> {
	@NonNull
	private final TodoLists repository;

	@Override
	public void accept(@NonNull DeleteTaskRequest request) {
		final UUID todoListUuid = request.getTodoListUuid();
		final UUID taskUuid = request.getTaskUuid();
		
		final TodoList todoList = repository.findById(TodoListId.of(todoListUuid))
			.orElseThrow(() -> new TodoListNotFound("Le dépôt ne contient pas de TodoList avec l'identifiant " + todoListUuid));

		todoList.deleteTask(TaskId.of(taskUuid));
		repository.save(todoList);
	}
}
```

Une question reste : qui crée ces gestionnaires ?

La réponse : une classe implémentant l'interface [_BehaviorModel_](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodecore/src/main/java/org/requirementsascode/BehaviorModel.java). Le modèle de comportement mappe chaque classe de _requête_ au _gestionnaire de requêtes_ pour ce type de requête.

Voici une partie du [_TodoListBehaviorModel_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/TodoListBehaviorModel.java) :

``` java
@AllArgsConstructor
public class TodoListBehaviorModel implements BehaviorModel {
	@NonNull
	private final TodoLists todoLists;
	...
	@Override
	public Model model() {
		return Model.builder()
			.user(FindOrCreateListRequest.class).systemPublish(findOrCreateList())
			.user(AddTaskRequest.class).systemPublish(addTask())
			.user(ToggleTaskCompletionRequest.class).system(toggleTaskCompletion())
			...
			.build();
	}

	private Function<FindOrCreateListRequest, FindOrCreateListResponse> findOrCreateList() {
		return new FindOrCreateList(todoLists);
	}

	private Function<AddTaskRequest, AddTaskResponse> addTask() {
		return new AddTask(todoLists);
	}

	private Consumer<ToggleTaskCompletionRequest> toggleTaskCompletion() {
		return new ToggleTaskCompletion(todoLists);
	}
	...
}
```

Les instructions `user(...)` définissent les classes de requête. Nous utilisons `systemPublish(...)` pour les gestionnaires qui retournent une _réponse_, et `system(...)` pour les gestionnaires qui ne le font pas.

Le _modèle de comportement_ a un constructeur avec des dépendances externes passées en tant qu'interfaces. Et il crée tous les gestionnaires et injecte les dépendances appropriées dans ceux-ci.

En configurant les dépendances du _modèle de comportement_, nous configurons tous les gestionnaires. C'est exactement ce que nous voulons : un endroit central où nous pouvons changer ou basculer les dépendances technologiques. C'est ainsi que les décisions technologiques peuvent changer sans affecter le code de domaine.

## La couche Web de l'application (les adaptateurs)

La couche Web dans une architecture propre moderne peut être très fine. Dans sa forme la plus simple, elle se compose de seulement 2 classes :

* Une classe pour la configuration des dépendances
* Une classe pour la gestion des exceptions

Voici la classe [_TodoListConfiguration_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/adapter/spring/TodoListConfiguration.java) :

``` java
@Configuration
class TodoListConfiguration {
	@Bean
	TodoListBehaviorModel behaviorModel(TodoLists repository) {
		return new TodoListBehaviorModel(repository);
	}
}
```

Spring injecte l'implémentation de l'interface de dépôt _TodoLists_ dans la méthode _behaviorModel(...)_. Cette méthode crée une implémentation de _modèle de comportement_ en tant que bean.

Si l'application utilise des services externes, la classe de configuration est l'endroit pour créer les instances concrètes en tant que beans. Et les injecter dans le _modèle de comportement_.

Alors, où sont tous les contrôleurs ?

Eh bien, il n'y en a pas que vous devez créer. Au moins si vous ne gérez que les requêtes POST. (Pour la gestion des requêtes GET, voir la section Q&A plus tard.)

La bibliothèque [_spring-behavior-web_](https://github.com/bertilmuth/modern-clean-architecture/tree/main/spring-behavior-web) fait partie des bibliothèques _Modern Clean Architecture_. Nous définissons un seul endpoint pour les requêtes. Nous spécifions l'URL de cet endpoint dans le fichier [_application.properties_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/application.properties) :

`behavior.endpoint = /todolist`

Si cette propriété existe, spring-behavior-web configure un contrôleur pour l'endpoint en arrière-plan. Ce contrôleur reçoit les requêtes POST.

Nous n'avons pas besoin d'écrire de code spécifique à Spring pour ajouter un nouveau comportement. Et nous n'avons pas besoin d'ajouter ou de modifier un contrôleur.

Voici ce qui se passe lorsque l'endpoint reçoit une requête POST :

1. spring-behavior-web désérialise la requête,
2. spring-behavior-web passe la requête à un comportement configuré par le modèle de comportement,
3. le comportement passe la requête au gestionnaire de requêtes approprié (s'il y en a un),
4. spring-behavior-web sérialise la réponse et la passe à l'endpoint (s'il y en a une).

Par défaut, spring-behavior-web enveloppe chaque appel à un gestionnaire de requêtes dans une transaction.

### Comment envoyer des requêtes POST

Une fois que nous démarrons l'application Spring Boot, nous pouvons envoyer des requêtes POST à l'endpoint.

Nous incluons une propriété `@type` dans le contenu JSON afin que spring-behavior-web puisse déterminer la bonne classe de requête lors de la désérialisation.

Par exemple, voici une commande `curl` valide de l'application To Do List. Elle envoie une [_FindOrCreateListRequest_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/request/FindOrCreateListRequest.java) à l'endpoint.

`curl -H "Content-Type: application/json" -X POST -d '{"@type": "FindOrCreateListRequest"}' [http://localhost:8080/todolist](http://localhost:8080/todolist)`

Et voici la syntaxe correspondante à utiliser dans Windows PowerShell :

`iwr http://localhost:8080/todolist -Method 'POST' -Headers @{'Content-Type' = 'application/json'} -Body '{"@type": "FindOrCreateListRequest"}'`

### Gestion des exceptions

La gestion des exceptions avec spring-behavior-web n'est pas différente de celle des applications Spring "normales". Nous créons une classe annotée avec `@ControllerAdvice`. Et nous plaçons des méthodes annotées avec `@ExceptionHandler` dans celle-ci.

Voir [_TodoListExceptionHandling_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/adapter/spring/TodoListExceptionHandling.java) par exemple :

``` java
@ControllerAdvice
class TodoListExceptionHandling {
	@ExceptionHandler({ Exception.class })
	public ResponseEntity<ExceptionResponse> handle(Exception e) {
		return responseOf(e, BAD_REQUEST);
	}
	...
}
```

Notez que dans une application réelle, les différents types d'exceptions nécessitent un traitement différent.

## Le front-end de l'application

Le front-end de l'application To Do List se compose de :

* une [page HTML](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/static/index.html),
* un [fichier CSS](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/static/styles.css) pour la mise en forme,
* et un [fichier JavaScript main.js](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/static/main.js)

Nous nous concentrons sur main.js ici. Il envoie des requêtes et met à jour la page web.

Voici une partie de son contenu :

``` javascript
// URL pour poster toutes les requêtes,
// Doit être la même que celle dans application.properties
// (Voir https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/application.properties)
const BEHAVIOR_ENDPOINT = "/todolist";

//variables
var todoListUuid;
...

// fonctions
function restoreList(){
	const request = {"@type":"FindOrCreateListRequest"};
	
	post(request, function(response){
		todoListUuid = response.todoListUuid;
		restoreTasksOf(todoListUuid);
	});
}

function restoreTasksOf(todoListUuid) {
	const request = {"@type":"ListTasksRequest", "todoListUuid":todoListUuid};

	post(request, function(response){	
		showTasks(response.tasks);
	});
}
...
function post(jsonObject, responseHandler) {	
	const xhr = new XMLHttpRequest();
	xhr.open("POST", BEHAVIOR_ENDPOINT);

	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json");
	
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4) {
			response = xhr.responseText.length > 0? JSON.parse(xhr.response) : "";
			if(response.error){
				alert('Statut ' + response.status + ' "' + response.message + '"');
			} else{
				responseHandler(response);
			}
		}	
	};
	
	const jsonString = JSON.stringify(jsonObject);
	xhr.send(jsonString);
}
```

Ainsi, par exemple, voici l'objet JSON pour une [_ListTasksRequest_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/request/ListTasksRequest.java) :

``` javascript
const request = {@type:ListTasksRequest, todoListUuid:todoListUuid};
```

La méthode `post(...)` envoie la requête au backend et passe la réponse au gestionnaire de réponse (la fonction de rappel que vous avez passée en tant que deuxième paramètre).

C'est tout ce qui concerne l'application To Do List.

# Questions & Réponses

Que faire si...

... je veux envoyer des requêtes GET au lieu de requêtes POST ?

... je veux que la couche web évolue séparément du comportement ?

... je veux utiliser un framework différent de Spring ?

... j'ai une application beaucoup plus grande que l'exemple To Do List. Comment la structurer ?

[Voici](https://github.com/bertilmuth/modern-clean-architecture/wiki/Questions-&-Answers) les réponses.

# Conclusion

Dans cet article, je vous ai présenté une manière particulière d'implémenter une Clean Architecture. Il existe de nombreuses autres façons.

Mon objectif est de réduire l'effort de construction d'une Clean Architecture et d'aplatir la courbe d'apprentissage.

Pour y parvenir, les bibliothèques Modern Clean Architecture fournissent les fonctionnalités suivantes :

* **Sérialisation des requêtes et réponses immutables** sans annotations spécifiques à la sérialisation.
* **Aucune nécessité de DTOs.** Vous pouvez utiliser les mêmes objets immutables pour les requêtes/réponses dans la couche web et les cas d'utilisation.
* **Endpoint générique** qui reçoit et transmet les requêtes POST. Un nouveau comportement et une nouvelle logique de domaine peuvent être ajoutés et utilisés sans avoir besoin d'écrire du code spécifique au framework.

Dans mon prochain article, je décrirai comment tester une Modern Clean Architecture.

Je vous invite à visiter la page [Modern Clean Architecture](https://github.com/bertilmuth/modern-clean-architecture/) sur GitHub.

Voir l'[application exemple To Do List](https://github.com/bertilmuth/modern-clean-architecture/tree/main/samples/todolist).

Et n'hésitez pas à partager vos commentaires avec moi. Qu'en pensez-vous ?

Si vous souhaitez suivre ce que je fais ou me laisser un message, suivez-moi sur [LinkedIn](https://www.linkedin.com/in/bertilmuth/) ou [Twitter](https://twitter.com/BertilMuth).

# Remerciements

Merci à Surya Shakti pour avoir publié le code original du front-end uniquement de la [liste de tâches](https://suryashakti1999.medium.com/to-do-list-app-using-javascript-for-absolute-beginners-13ea9e38a033).

Merci à Oliver Drotbohm pour m'avoir dirigé vers la bibliothèque [jMolecules](https://github.com/xmolecules/jmolecules).