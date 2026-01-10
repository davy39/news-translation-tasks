---
title: How to generate data classes in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T17:59:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-data-classes-in-java-fead8fa354a2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*upVmlEendf-ZejB-vCeh_g.jpeg
tags:
- name: code
  slug: code
- name: coding
  slug: coding
- name: generator
  slug: generator
- name: Java
  slug: java
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Bertil Muth

  Kotlin has a concise syntax to declare data classes:

  data class User(val name: String, val age: Int)


  The equivalent Java syntax is verbose. You have to create a Java class with private
  fields. And getter and setter methods for the fie...'
---

By Bertil Muth

Kotlin has a concise syntax to declare data classes:

```kotlin
data class User(val name: String, val age: Int)
```

The equivalent Java syntax is verbose. You have to create a Java class with private fields. And `getter` and `setter` methods for the fields. And additional methods like `equals()`, `hashCode()` and `toString()`.

But who says you have to create the Java code by hand?

In this article, I’ll show you how to generate Java source files from a [YAML](https://en.wikipedia.org/wiki/YAML) file.

Here’s the example YAML file:

```yaml
User:
    name: Name
    age: Integer

Name:
    firstName: String
    lastName: String
```

The example output of the code generator is two Java source files, `User.java` and `Name.java`.

```java
public class User{
    private Name name;
    private Integer age;
    
    public User(){
    }
    public Name getName(){
        return name;
    }
    public void setName(Name name){
        this.name = name;
    }
    public Integer getAge(){
        return age;
    }
    public void setAge(Integer age){
        this.age = age;
    }
}
```

`Name.java` is similar.

The point of this article is: You’ll learn how to program a code generator from scratch. And it’s easy to adapt it to your needs.

### The main method

The `[main()](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/Main.java)` method does two things:

* Step 1: Read in the YAML file, into class specifications
* Step 2: Generate Java source files from the class specifications

It decouples reading and generating. You can change the input format in the future, or support more input formats.

Here’s the `main()` method:

```java
public static void main(String[] args) throws Exception {
    // Make sure there is exactly one command line argument, 
    // the path to the YAML file
    if (args.length != 1) {
        System.out.println("Please supply exactly one argument, the path to the YAML file.");
        return;
    }
  
    // Get the YAML file's handle & the directory it's contained in
    // (generated files will be placed there)
    final String yamlFilePath = args[0];
    final File yamlFile = new File(yamlFilePath);
    final File outputDirectory = yamlFile.getParentFile();
  
    // Step 1: Read in the YAML file, into class specifications
    YamlClassSpecificationReader yamlReader = new YamlClassSpecificationReader();
    List<ClassSpecification> classSpecifications = yamlReader.read(yamlFile);
    
    // Step 2: Generate Java source files from class specifications
    JavaDataClassGenerator javaDataClassGenerator = new JavaDataClassGenerator();
    javaDataClassGenerator.generateJavaSourceFiles(classSpecifications, outputDirectory);
    
    System.out.println("Successfully generated files to: " + outputDirectory.getAbsolutePath());
}
```

### Step 1: Read the YAML file into class specifications

Let me explain what happens in this line:

```java
List<ClassSpecification> classSpecifications =  yamlReader.read(yamlFile);
```

A class specification is a definition of a class to be generated and its fields.  
Remember the `User` in the example YAML file?

```yaml
User:
    name: Name
    age: Integer
```

When the [YAML reader](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java) reads that, it will create one `ClassSpecification` object, with the name `User`. And that class specification will reference two `FieldSpecification` objects, called `name` and `age`.

The code for the `ClassSpecification` class and the `FieldSpecification` class is simple.

The content of `[ClassSpecification.java](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/model/ClassSpecification.java)` is shown below:

```java
public class ClassSpecification {
    private String name;
    private List<FieldSpecification> fieldSpecifications;
  
    public ClassSpecification(String className, List<FieldSpecification> fieldSpecifications) {
        this.name = className;
        this.fieldSpecifications = fieldSpecifications;
    }
  
    public String getName() {
        return name;
    }
  
    public List<FieldSpecification> getFieldSpecifications() {
        return Collections.unmodifiableList(fieldSpecifications);
    }
}
```

The content of `[FieldSpecification.java](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/model/FieldSpecification.java)` is:

```java
public class FieldSpecification {
    private String name;
    private String type;
  
    public FieldSpecification(String fieldName, String fieldType) {
        this.name = fieldName;
        this.type = fieldType;
    }
  
    public String getName() {
        return name;
    }
  
    public String getType() {
        return type;
    }
}
```

The only remaining question for Step 1 is: how do you get from a YAML file to objects of these classes?

The [YAML reader](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java) uses the [SnakeYAML](https://bitbucket.org/asomov/snakeyaml) library to parse YAML files.   
SnakeYAML makes a YAML file’s content available in data structures like maps and lists.

For this article, you only need to understand maps — because that’s what we use in the YAML files.

Look at the example again:

```yaml
User:
    name: Name
    age: Integer

Name:
    firstName: String
    lastName: String
```

What you see here is two nested maps.

The key of the outer map is the class name (like `User`).

When you get the value for the `User` key, you get a map of the class fields:

```yaml
name: Name
age: Integer
```

The key of this inner map is the field name, and the value is the field type.

It’s a map of strings to a map of strings to strings. That’s important to understand the code of the [YAML reader](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java).

Here’s the method that reads in the complete YAML file contents:

```java
private Map<String, Map<String, String>> readYamlClassSpecifications(Reader reader) {
	Yaml yaml = new Yaml();

	// Read in the complete YAML file to a map of strings to a map of strings to strings
	Map<String, Map<String, String>> yamlClassSpecifications = 
		(Map<String, Map<String, String>>) yaml.load(reader);

	return yamlClassSpecifications;
}
```

With the `yamlClassSpecifications` as input, the [YAML reader](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java) creates the `ClassSpecification` objects:

```java
private List<ClassSpecification> createClassSpecificationsFrom(Map<String, Map<String, String>> yamlClassSpecifications) {
	final Map<String, List<FieldSpecification>> classNameToFieldSpecificationsMap 
		= createClassNameToFieldSpecificationsMap(yamlClassSpecifications);

	List<ClassSpecification> classSpecifications = 
		classNameToFieldSpecificationsMap.entrySet().stream()
			.map(e -> new ClassSpecification(e.getKey(), e.getValue()))
			.collect(toList());

	return classSpecifications;
}
```

The `createClassNameToFieldSpecificationsMap()` method creates

* the field specifications for each class, and based on these
* a map of each class name to its field specifications.

Then the [YAML reader](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java) creates a `ClassSpecification` object for each entry in that map.

The contents of the YAML file are now available to Step 2 in a YAML independent way. We’re done with Step 1.

### Step 2: Generate Java source files from the class specifications

[Apache FreeMarker](https://freemarker.apache.org/) is a Java template engine that produces textual output. Templates are written in the FreeMarker Template Language (FTL). It allows static text to mix with the content of Java objects.

Here’s the template to generate the Java source files, `[javadataclass.ftl](https://github.com/bertilmuth/javadataclass/blob/2c550c8ea0ab551d06eed342ea0013043f96f080/src/main/resources/javadataclass.ftl)`:

```ftl
public class ${classSpecification.name}{
<#list classSpecification.fieldSpecifications as field>
    private ${field.type} ${field.name};
</#list>
    public ${classSpecification.name}(){
    }
<#list classSpecification.fieldSpecifications as field>
    public ${field.type} get${field.name?cap_first}(){
        return ${field.name};
    }
    public void set${field.name?cap_first}(${field.type} ${field.name}){
        this.${field.name} = ${field.name};
    }
</#list>    
}
```

Let’s look at the first line:

```
public class ${classSpecification.name}{
```

You can see it begins with the static text of a class declaration: `public class`. The interesting bit is in the middle: `${classSpecification.name}`.

When Freemarker processes the template, it accesses the `classSpecification` object in its model. It calls the `getName()` method on it.

What about this part of the template?

```ftl
<#list classSpecification.fieldSpecifications as field>
    private ${field.type} ${field.name};
</#list>
```

At first, Freemarker calls `classSpecification.getFieldSpecifications()`. It then iterates over the field specifications.

One last thing. That line is a bit odd:

```ftl
public ${field.type} get${field.name?cap_first}(){
```

Let’s say the example field is `age: Integer` (in YAML). Freemarker translates this to:

```java
public Integer getAge(){
```

So `?cap_first` means: capitalize the first letter, as the YAML file contains `age` in lower case letters.

Enough about templates. How do you generate the Java source files?

First, you need to configure FreeMarker by creating a `Configuration` instance. This happens in the constructor of the `[JavaDataClassGenerator](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/generate/JavaDataClassGenerator.java)`:

To generate source files, the `[JavaDataClassGenerator](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/generate/JavaDataClassGenerator.java)` iterates over the class specifications, and generates a source file for each:

And that’s it.

### Conclusion

I showed you how to build a Java source code generator based on YAML files. I picked YAML because it is easy to process, and thus easy to teach. You can replace it with another format if you like.

You can find the complete code on [Github](https://github.com/bertilmuth/javadataclass).

To make the code as understandable as possible, I took a few shortcuts:

* no methods like `equals()`, `hashCode()` and `toString()`
* no inheritance of data classes
* generated Java classes are in the default package
* the output directory is the same as the input directory
* error handling hasn’t been my focus

A production-ready solution would need to deal with those issues. Also, for data classes, [Project Lombok](https://projectlombok.org/) is an alternative without code generation.

So think of this article as a beginning, not an end. Imagine what is possible. A few examples:

* scaffold JPA entity classes or Spring repositories
* generate several classes from one specification, based on patterns in your application
* generate code in different programming languages
* produce documentation

I currently use this approach to translate natural language requirements   
 directly to code, for research purposes. What will you do?

_If you want to know what I’m hacking on, visit [my GitHub project](https://github.com/bertilmuth/requirementsascode)._

_You can contact me on [Twitter](https://twitter.com/BertilMuth) or [LinkedIn](https://www.linkedin.com/in/bertilmuth)._

_The original version of this article was posted on [dev.to](https://dev.to/bertilmuth/generating-data-classes-in-java-4cef)_

