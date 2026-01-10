---
title: How to Build Modern Clean Architecture
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
seo_title: null
seo_desc: 'By Bertil Muth

  Clean Architecture is a term coined by Robert C. Martin. The main idea is that entities
  and use cases are independent of frameworks, UI, the database, and external services.

  A Clean Architecture style has a positive effect on maintaina...'
---

By Bertil Muth

[Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) is a term coined by Robert C. Martin. The main idea is that entities and use cases are independent of frameworks, UI, the database, and external services.

A Clean Architecture style has a positive effect on maintainability because:

* We can test domain entities and use cases without a framework, UI, or infrastructure.
* Technology decisions can change without affecting domain code, and vice versa. It is even possible to switch to a new framework with limited effort.

My goal is to flatten the learning curve, and reduce the effort it might take you to implement a Clean Architecture. That’s why I created the [Modern Clean Architecture](https://github.com/bertilmuth/modern-clean-architecture) libraries.

In this article, I will show you how to create an application with a modern clean architecture, from a HTML/JavaScript front end to a Spring Boot back end. The focus will be on the back end.

Let’s start with an overview of the sample application – a timeless classic, the TODO app.

## Sample TODO List Application

A _to do list_ is a collection of _tasks_. A task has a _name_, and is either _completed_ or not. As a user, you can:

* Create a single to do list, and persist it
* Add a task
* Complete a task, or “uncomplete” it
* Delete a task
* List all tasks
* Filter completed/uncompleted tasks

Here’s what a todo list with 1 uncompleted and 2 completed tasks looks like:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/grafik-1.png)

We'll start at the core of the application, the domain entities. Then we'll work our way outwards to the front end.

## The Domain Entities

The central domain entities are [TodoList](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/TodoList.java) and [Task](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/Task.java).

The _TodoList_ entity contains:

* a unique id,
* a list of tasks,
* domain methods for adding, completing, and deleting tasks

The `TodoList` entity doesn’t contain public setters. Setters would break proper encapsulation.

Here’s part of the [TodoList](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/TodoList.java) entity. [Lombok](https://projectlombok.org/) annotations shorten the code.

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
			throw new IllegalTaskName("Please specify a non-null, non-whitespace task name!");
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

What is the `AggregateRoot` interface good for? Aggregate root is a term from Domain Driven Design (DDD) by Eric Evans:

> An aggregate is a cluster of associated objects that we treat as a unit for the purpose of data changes. Each aggregate has a root and a boundary. The boundary defines what is inside the aggregate. The root is a single, specific entity contained in the aggregate.

We can change the aggregate’s state only through the aggregate root. In our example that means: we always have to use the `TodoList` to add, remove, or change a task.

That allows the `TodoList` to enforce constraints. For example, we can’t add a task with a blank name to the list.

The `AggregateRoot` interface is part of the [jMolecules](https://github.com/xmolecules/jmolecules) library. This library makes DDD concepts explicit in the domain code. During build, [a ByteBuddy plugin](https://github.com/xmolecules/jmolecules-integrations/tree/main/jmolecules-bytebuddy) maps the annotations to Spring Data annotations.

So we only have a single model, both for representing domain concepts, and persistence. Still, we don’t have any persistence-specific annotations in the domain code. We don’t tie ourselves to any framework.

The [_Task_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/Task.java) class is similar, but it implements the jMolecules _Entity_ interface instead:

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

The constructor of _Task_ is package private. So we can’t create an instance of _Task_ from outside of the [domain package](https://github.com/bertilmuth/modern-clean-architecture/tree/main/samples/todolist/src/main/java/com/example/todolist/domain). And the _Task_ class is immutable. No changes to its state are possible from outside of the aggregate’s boundary.

We need a repository for storing the _TodoList._ To stick to domain terms in the domain code, it is called [_TodoLists_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/domain/TodoLists.java):

``` java
public interface TodoLists extends Repository<TodoList, TodoListId> {
	TodoList save(TodoList entity);
	Optional<TodoList> findById(TodoListId id);
	Iterable<TodoList> findAll();
}
```

Again, the code uses a jMolecues annotation: _Repository_. During build, the ByteBuddy plugin translates it to a Spring Data repository.

We’ll skip the domain exceptions, since there’s nothing special about them. That’s the complete [domain package](https://github.com/bertilmuth/modern-clean-architecture/tree/main/samples/todolist/src/main/java/com/example/todolist/domain).

## The App's Behavior (and Use Cases)

Next, we define the behavior of the application that is visible to the end user. Any interaction of the user with the application happens as follows:

1. The user interface sends a _request_.
2. The backend reacts by executing a _request handler._ The request handler does everything necessary to fulfill the request:  
- Access the database  
- Call external services  
- Call domain entity methods
3. The request handler **may** return a _response_.

We implement a _request handler_ with a Java 8 functional interface.

A handler that returns a _response_ implements the `java.util.Function` interface. Here’s the code of the [_AddTask_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/AddTask.java) handler. This handler

* extracts the to do list id and task name from an [_AddTaskRequest_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/request/AddTaskRequest.java)_,_
* finds the to do list in the repository (or throws an exception),
* adds a task with the name from the request to the list,
* returns an [_AddTaskResponse_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/response/AddTaskResponse.java) with the added task’s id.

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
			.orElseThrow(() -> new TodoListNotFound("Repository doesn't contain a TodoList of id " + todoListUuid));

		TaskId taskId = todoList.addTask(taskName);
		repository.save(todoList);

		return new AddTaskResponse(taskId.getUuid());
	}
}
```

Lombok creates a constructor with the _TodoLists_ repository interface as constructor argument. We pass in any external dependency as interface to the handler’s constructor.

The requests and responses are immutable objects:

``` java
@Value
public class AddTaskRequest {
	@NonNull
	UUID todoListUuid;

	@NonNull
	String taskName;
}
```

The Modern Clean Architecture libraries (de)serialize them from/to JSON.

Next, an example of a handler that doesn’t return a response. The [_DeleteTask_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/DeleteTask.java) handler receives a [_DeleteTaskRequest_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/request/DeleteTaskRequest.java). Since the handler doesn’t return a response, it implements the _Consumer_ interface.

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
			.orElseThrow(() -> new TodoListNotFound("Repository doesn't contain a TodoList of id " + todoListUuid));

		todoList.deleteTask(TaskId.of(taskUuid));
		repository.save(todoList);
	}
}
```

One question remains: who creates these handlers?

The answer: a class implementing the [_BehaviorModel_](https://github.com/bertilmuth/requirementsascode/blob/master/requirementsascodecore/src/main/java/org/requirementsascode/BehaviorModel.java) interface. The behavior model maps each _request_ class to the _request handler_ for this kind of request.

Here’s a part of the [_TodoListBehaviorModel_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/TodoListBehaviorModel.java):

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

The `user(...)` statements define the request classes. We use `systemPublish(...)` for handlers that return a _response_, and `system(...)` for handlers that don’t.

The _behavior model_ has a constructor with external dependencies passed in as interfaces. And it creates all handlers and injects the appropriate dependencies into them.

By configuring the dependencies of the _behavior model_, we configure all handlers. That’s exactly what we want: a central place where we can change or switch the dependencies to technology. That’s how technology decisions can change without affecting the domain code.

## The Apps' Web Layer (the Adapters)

The web layer in a modern clean architecture can be very thin. In its simplest form, it consists of only 2 classes:

* One class for configuration of dependencies
* One class for exception handling

Here’s the [_TodoListConfiguration_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/adapter/spring/TodoListConfiguration.java) class:

``` java
@Configuration
class TodoListConfiguration {
	@Bean
	TodoListBehaviorModel behaviorModel(TodoLists repository) {
		return new TodoListBehaviorModel(repository);
	}
}
```

Spring injects the implementation of the _TodoLists_ repository interface into the _behaviorModel(…)_ method. That method creates a _behavior model_ implementation as a bean.

If the application uses external services, the configuration class is the place to create the concrete instances as beans. And inject them into the _behavior model_.

So, where are all the controllers?

Well, there aren’t any that you have to create. At least if you only handle POST requests. (For the handling of GET requests, see the Q&A later.)

The [_spring-behavior-web_](https://github.com/bertilmuth/modern-clean-architecture/tree/main/spring-behavior-web) library is part of the _Modern Clean Architecture_ libraries. We define a single endpoint for requests. We specify the URL of that endpoint in the [_application.properties_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/application.properties):

`behavior.endpoint = /todolist`

If that property exists, spring-behavior-web sets up a controller for the endpoint in the background. That controller receives POST requests.

We don’t need to write Spring specific code to add new behavior. And we don’t need to add or change a controller.

Here’s what happens when the endpoint receives a POST request:

1. spring-behavior-web deserializes the request,
2. spring-behavior-web passes the request to a behavior configured by the behavior model,
3. the behavior passes the request to the appropriate request handler (if there is one),
4. spring-behavior-web serializes the response and passes it back to the endpoint (if there is one).

By default, spring-behavior-web wraps every call to a request handler in a transaction.

### How to send POST requests

Once we start the Spring Boot application, we can send POST requests to the endpoint.

We include a `@type` property in the JSON content so that spring-behavior-web can determine the right request class during deserialization.

For example, this is a valid `curl` command of the To Do List application. It sends a [_FindOrCreateListRequest_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/request/FindOrCreateListRequest.java) to the endpoint.

`curl -H "Content-Type: application/json" -X POST -d '{"@type": "FindOrCreateListRequest"}' [http://localhost:8080/todolist](http://localhost:8080/todolist)`

And that’s the corresponding syntax to use in Windows PowerShell:

`iwr http://localhost:8080/todolist -Method 'POST' -Headers @{'Content-Type' = 'application/json'} -Body '{"@type": "FindOrCreateListRequest"}'`

### Exception handling

Exception handling with spring-behavior-web is no different than in “normal” Spring applications. We create a class annotated with `@ControllerAdvice`. And we place methods annotation with `@ExceptionHandler` in it.

See the [_TodoListExceptionHandling_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/adapter/spring/TodoListExceptionHandling.java) for example:

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

Note that in a real application, the different exception types need different treatment.

## The App's Front End

The front end of the To Do List application consists of:

* a [HTML page](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/static/index.html),
* a [CSS file](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/static/styles.css) for formatting,
* and a the [main.js JavaScript file](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/static/main.js)

We focus on main.js here. It sends requests and updates the web page.

Here’s part of its content:

``` javascript
// URL for posting all requests,
// Must be the same as the one in application.properties
// (See https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/resources/application.properties)
const BEHAVIOR_ENDPOINT = "/todolist";

//variables
var todoListUuid;
...

// functions
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
				alert('Status ' + response.status + ' "' + response.message + '"');
			} else{
				responseHandler(response);
			}
		}	
	};
	
	const jsonString = JSON.stringify(jsonObject);
	xhr.send(jsonString);
}
```

So for example, this is the JSON object for a [_ListTasksRequest_](https://github.com/bertilmuth/modern-clean-architecture/blob/main/samples/todolist/src/main/java/com/example/todolist/behavior/request/ListTasksRequest.java):

``` javascript
const request = {“@type”:”ListTasksRequest”, “todoListUuid”:todoListUuid};
```

The `post(…)` method sends the request to the backend, and passes the response to the response handler (the callback function you passed in as second parameter).

That’s all about the To Do List application.

# Questions & Answers

What if…

… I want to send GET requests instead of POST requests?

… I want the web layer to evolve separately from the behavior?

… I want to use a different framework than Spring?

… I have a much bigger application than the To Do List sample. How do I structure it?

[Here](https://github.com/bertilmuth/modern-clean-architecture/wiki/Questions-&-Answers) are the answers.

# Conclusion

In this article, I presented you a particular way to implement a Clean Architecture. There are many other ways.

My goal is to reduce the effort of building a Clean Architecture and flatten the learning curve.

To achieve this, the Modern Clean Architecture libraries provide the following features:

* **Serialization of immutable requests and responses** without serialization specific annotations.
* **No necessity for DTOs.** You can use the same immutable objects for requests/responses in web layer and use cases..
* **Generic endpoint** that receives and forwards POST requests. New behavior and domain logic can be added and used without the need to write framework specific code.

In my next article, I will describe how to test a Modern Clean Architecture.

I invite you to visit the [Modern Clean Architecture](https://github.com/bertilmuth/modern-clean-architecture/) GitHub page.

See the [To Do List sample application](https://github.com/bertilmuth/modern-clean-architecture/tree/main/samples/todolist).

And please share any feedback you have with me. What do you think about it?

If you want to keep up with what I’m doing or drop me a note, follow me on [LinkedIn](https://www.linkedin.com/in/bertilmuth/) or [Twitter](https://twitter.com/BertilMuth).

# Acknowledgements

Thank you to Surya Shakti for publishing the original front end only [to do list code](https://suryashakti1999.medium.com/to-do-list-app-using-javascript-for-absolute-beginners-13ea9e38a033).

Thank you to Oliver Drotbohm for pointing me to the awesome [jMolecules](https://github.com/xmolecules/jmolecules) library.

