---
title: Comment générer des classes de données en Java
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
seo_title: Comment générer des classes de données en Java
seo_desc: 'By Bertil Muth

  Kotlin has a concise syntax to declare data classes:

  data class User(val name: String, val age: Int)


  The equivalent Java syntax is verbose. You have to create a Java class with private
  fields. And getter and setter methods for the fie...'
---

Par Bertil Muth

Kotlin a une syntaxe concise pour déclarer des classes de données :

```kotlin
data class User(val name: String, val age: Int)
```

La syntaxe Java équivalente est verbeuse. Vous devez créer une classe Java avec des champs privés. Et des méthodes `getter` et `setter` pour les champs. Et des méthodes supplémentaires comme `equals()`, `hashCode()` et `toString()`.

Mais qui dit que vous devez créer le code Java à la main ?

Dans cet article, je vais vous montrer comment générer des fichiers sources Java à partir d'un fichier [YAML](https://en.wikipedia.org/wiki/YAML).

Voici le fichier YAML d'exemple :

```yaml
User:
    name: Name
    age: Integer

Name:
    firstName: String
    lastName: String
```

L'exemple de sortie du générateur de code est deux fichiers sources Java, `User.java` et `Name.java`.

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

`Name.java` est similaire.

Le but de cet article est : vous allez apprendre à programmer un générateur de code à partir de zéro. Et il est facile de l'adapter à vos besoins.

### La méthode principale

La méthode `[main()](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/Main.java)` fait deux choses :

* Étape 1 : Lire le fichier YAML, dans des spécifications de classes
* Étape 2 : Générer des fichiers sources Java à partir des spécifications de classes

Elle découple la lecture et la génération. Vous pouvez changer le format d'entrée à l'avenir, ou supporter plus de formats d'entrée.

Voici la méthode `main()` :

```java
public static void main(String[] args) throws Exception {
    // Assurez-vous qu'il y a exactement un argument de ligne de commande,
    // le chemin vers le fichier YAML
    if (args.length != 1) {
        System.out.println("Veuillez fournir exactement un argument, le chemin vers le fichier YAML.");
        return;
    }
  
    // Obtenez le handle du fichier YAML et le répertoire qui le contient
    // (les fichiers générés seront placés là)
    final String yamlFilePath = args[0];
    final File yamlFile = new File(yamlFilePath);
    final File outputDirectory = yamlFile.getParentFile();
  
    // Étape 1 : Lire le fichier YAML, dans des spécifications de classes
    YamlClassSpecificationReader yamlReader = new YamlClassSpecificationReader();
    List<ClassSpecification> classSpecifications = yamlReader.read(yamlFile);
    
    // Étape 2 : Générer des fichiers sources Java à partir des spécifications de classes
    JavaDataClassGenerator javaDataClassGenerator = new JavaDataClassGenerator();
    javaDataClassGenerator.generateJavaSourceFiles(classSpecifications, outputDirectory);
    
    System.out.println("Fichiers générés avec succès dans : " + outputDirectory.getAbsolutePath());
}
```

### Étape 1 : Lire le fichier YAML dans des spécifications de classes

Permettez-moi d'expliquer ce qui se passe dans cette ligne :

```java
List<ClassSpecification> classSpecifications =  yamlReader.read(yamlFile);
```

Une spécification de classe est une définition d'une classe à générer et de ses champs.  
Souvenez-vous de `User` dans le fichier YAML d'exemple ?

```yaml
User:
    name: Name
    age: Integer
```

Lorsque le [lecteur YAML](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java) lit cela, il créera un objet `ClassSpecification`, avec le nom `User`. Et cette spécification de classe référencera deux objets `FieldSpecification`, appelés `name` et `age`.

Le code pour la classe `ClassSpecification` et la classe `FieldSpecification` est simple.

Le contenu de `[ClassSpecification.java](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/model/ClassSpecification.java)` est montré ci-dessous :

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

Le contenu de `[FieldSpecification.java](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/model/FieldSpecification.java)` est :

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

La seule question restante pour l'Étape 1 est : comment passe-t-on d'un fichier YAML à des objets de ces classes ?

Le [lecteur YAML](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java) utilise la bibliothèque [SnakeYAML](https://bitbucket.org/asomov/snakeyaml) pour analyser les fichiers YAML.   
SnakeYAML rend le contenu d'un fichier YAML disponible dans des structures de données comme des maps et des listes.

Pour cet article, vous n'avez besoin de comprendre que les maps — car c'est ce que nous utilisons dans les fichiers YAML.

Regardez à nouveau l'exemple :

```yaml
User:
    name: Name
    age: Integer

Name:
    firstName: String
    lastName: String
```

Ce que vous voyez ici est deux maps imbriquées.

La clé de la map externe est le nom de la classe (comme `User`).

Lorsque vous obtenez la valeur pour la clé `User`, vous obtenez une map des champs de la classe :

```yaml
name: Name
age: Integer
```

La clé de cette map interne est le nom du champ, et la valeur est le type du champ.

C'est une map de chaînes à une map de chaînes à chaînes. C'est important pour comprendre le code du [lecteur YAML](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java).

Voici la méthode qui lit le contenu complet du fichier YAML :

```java
private Map<String, Map<String, String>> readYamlClassSpecifications(Reader reader) {
	Yaml yaml = new Yaml();

	// Lire le fichier YAML complet dans une map de chaînes à une map de chaînes à chaînes
	Map<String, Map<String, String>> yamlClassSpecifications = 
		(Map<String, Map<String, String>>) yaml.load(reader);

	return yamlClassSpecifications;
}
```

Avec les `yamlClassSpecifications` en entrée, le [lecteur YAML](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java) crée les objets `ClassSpecification` :

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

La méthode `createClassNameToFieldSpecificationsMap()` crée

* les spécifications de champs pour chaque classe, et sur cette base
* une map de chaque nom de classe à ses spécifications de champs.

Ensuite, le [lecteur YAML](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/read/YamlClassSpecificationReader.java) crée un objet `ClassSpecification` pour chaque entrée dans cette map.

Le contenu du fichier YAML est maintenant disponible pour l'Étape 2 de manière indépendante de YAML. Nous avons terminé avec l'Étape 1.

### Étape 2 : Générer des fichiers sources Java à partir des spécifications de classes

[Apache FreeMarker](https://freemarker.apache.org/) est un moteur de template Java qui produit une sortie textuelle. Les templates sont écrits dans le langage de template FreeMarker (FTL). Il permet au texte statique de se mélanger avec le contenu des objets Java.

Voici le template pour générer les fichiers sources Java, `[javadataclass.ftl](https://github.com/bertilmuth/javadataclass/blob/2c550c8ea0ab551d06eed342ea0013043f96f080/src/main/resources/javadataclass.ftl)` :

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

Regardons la première ligne :

```
public class ${classSpecification.name}{
```

Vous pouvez voir qu'elle commence par le texte statique d'une déclaration de classe : `public class`. La partie intéressante est au milieu : `${classSpecification.name}`.

Lorsque Freemarker traite le template, il accède à l'objet `classSpecification` dans son modèle. Il appelle la méthode `getName()` sur celui-ci.

Et cette partie du template ?

```ftl
<#list classSpecification.fieldSpecifications as field>
    private ${field.type} ${field.name};
</#list>
```

Tout d'abord, Freemarker appelle `classSpecification.getFieldSpecifications()`. Il itère ensuite sur les spécifications de champs.

Une dernière chose. Cette ligne est un peu étrange :

```ftl
public ${field.type} get${field.name?cap_first}(){
```

Disons que le champ d'exemple est `age: Integer` (en YAML). Freemarker traduit cela par :

```java
public Integer getAge(){
```

Ainsi, `?cap_first` signifie : mettre en majuscule la première lettre, car le fichier YAML contient `age` en lettres minuscules.

Assez parlé des templates. Comment générez-vous les fichiers sources Java ?

Tout d'abord, vous devez configurer FreeMarker en créant une instance de `Configuration`. Cela se fait dans le constructeur du `[JavaDataClassGenerator](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/generate/JavaDataClassGenerator.java)` :

Pour générer des fichiers sources, le `[JavaDataClassGenerator](https://github.com/bertilmuth/javadataclass/blob/ee95965bc798ae5425083baf88c4750fb27ecf11/src/main/java/de/bertilmuth/javadataclass/generate/JavaDataClassGenerator.java)` itère sur les spécifications de classes, et génère un fichier source pour chacune :

Et c'est tout.

### Conclusion

Je vous ai montré comment construire un générateur de code source Java basé sur des fichiers YAML. J'ai choisi YAML parce qu'il est facile à traiter, et donc facile à enseigner. Vous pouvez le remplacer par un autre format si vous le souhaitez.

Vous pouvez trouver le code complet sur [Github](https://github.com/bertilmuth/javadataclass).

Pour rendre le code aussi compréhensible que possible, j'ai pris quelques raccourcis :

* pas de méthodes comme `equals()`, `hashCode()` et `toString()`
* pas d'héritage des classes de données
* les classes Java générées sont dans le package par défaut
* le répertoire de sortie est le même que le répertoire d'entrée
* la gestion des erreurs n'a pas été mon objectif

Une solution prête pour la production devrait traiter ces problèmes. De plus, pour les classes de données, [Project Lombok](https://projectlombok.org/) est une alternative sans génération de code.

Considérez donc cet article comme un début, et non une fin. Imaginez ce qui est possible. Quelques exemples :

* échafauder des classes d'entités JPA ou des dépôts Spring
* générer plusieurs classes à partir d'une spécification, basée sur des motifs dans votre application
* générer du code dans différents langages de programmation
* produire de la documentation

J'utilise actuellement cette approche pour traduire des exigences en langage naturel directement en code, à des fins de recherche. Que ferez-vous ?

*Si vous voulez savoir sur quoi je travaille, visitez [mon projet GitHub](https://github.com/bertilmuth/requirementsascode).*

*Vous pouvez me contacter sur [Twitter](https://twitter.com/BertilMuth) ou [LinkedIn](https://www.linkedin.com/in/bertilmuth).*

*La version originale de cet article a été publiée sur [dev.to](https://dev.to/bertilmuth/generating-data-classes-in-java-4cef)*