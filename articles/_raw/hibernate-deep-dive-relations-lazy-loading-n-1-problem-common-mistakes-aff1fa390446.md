---
title: How to use Hibernate to interact with relational databases
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-16T19:51:58.000Z'
originalURL: https://freecodecamp.org/news/hibernate-deep-dive-relations-lazy-loading-n-1-problem-common-mistakes-aff1fa390446
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GI9m2zoDYsNNU59q20nMsg.jpeg
tags:
- name: database
  slug: database
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Emre Savcı

  Dealing with Deep Dive Relations, Lazy Loading, and the N+1 Problem

  Hibernate is an Object Relational Mapping tool which allows us to use objects for
  interaction with relational databases. It has many features like code first modeling,
  ...'
---

By Emre Savcı

#### Dealing with Deep Dive Relations, Lazy Loading, and the N+1 Problem

Hibernate is an [Object Relational Mapping](https://en.wikipedia.org/wiki/Object-relational_mapping) tool which allows us to use objects for interaction with relational databases. It has many features like code first modeling, lazy loading, change tracking, caching, auditing etc.

In this post I will present and discuss the relationships **OneToMany** and **ManyToOne.** Also we will see what are the consequences of building the wrong relationships or using the wrong **fetch type**. I will also examine Bidirectional and Unidirectional relations.

### OneToMany

Let’s start with the OneToMany UniDirectional relationship. Imagine that we have a **Shipment** entity and a shipment may contain many **Item**s.

_Note: the below code is just here to show you the straightforward way implementing a relationship, but it is not recommended to use in production. I will explain at the end of code examples._

First our persistence.xml:

```
<?xml version="1.0" encoding="UTF-8"?><persistence version="2.0" xmlns="http://java.sun.com/xml/ns/persistence"             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"             xsi:schemaLocation="http://java.sun.com/xml/ns/persistence             http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">    <persistence-unit name="testConfig" transaction-type="RESOURCE_LOCAL">        <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>        <class>deneme.Shipment</class>        <class>deneme.Item</class>        <properties>            <property name="javax.persistence.jdbc.url" value="jdbc:mysql://localhost:3306/jpadb"/>            <property name="javax.persistence.jdbc.user" value="root"/>            <property name="javax.persistence.jdbc.password" value="root"/>            <property name="javax.persistence.jdbc.driver" value="com.mysql.jdbc.Driver"/>            <property name="hibernate.logging.level" value="FINE"/>            <property name="hibernate.show_sql" value="true"/>            <property name="hibernate.format_sql" value="true"/>            <property name="hibernate.ddl-generation" value="auto"/>            <property name="hibernate.hbm2ddl.auto" value="update"/>        </properties>    </persistence-unit></persistence>
```

And our pom.xml dependencies:

```
<dependencies><dependency>    <groupId>org.projectlombok</groupId>    <artifactId>lombok</artifactId>    <version>1.18.2</version>    <scope>provided</scope></dependency>
```

```
<dependency>    <groupId>org.hibernate</groupId>    <artifactId>hibernate-entitymanager</artifactId>    <version>5.3.3.Final</version></dependency><!-- https://mvnrepository.com/artifact/org.hibernate/hibernate-core --><dependency>    <groupId>org.hibernate</groupId>    <artifactId>hibernate-core</artifactId>    <version>5.3.3.Final</version></dependency>
```

```
<!-- https://mvnrepository.com/artifact/mysql/mysql-connector-java --><dependency>    <groupId>mysql</groupId>    <artifactId>mysql-connector-java</artifactId>    <version>5.1.6</version></dependency><dependencies>
```

Here are our entities:

```
@Entity@Table(name = "shipments")@Getter@Setterclass Shipment {    @Id    @GeneratedValue(strategy = GenerationType.IDENTITY)    private int id;    private String cargoName;    @OneToMany(fetch = FetchType.LAZY, cascade = CascadeType.ALL)    @JoinTable(name = "shipment_items")    private List<Item> childList;        public void addItem(Item item) {        if (childList == null) {            childList = new ArrayList();        }        childList.add(item);    }}@Entity@Table(name = "items")@Getter@Setterclass Item {    @Id    @GeneratedValue(strategy = GenerationType.IDENTITY)    private int id;    private String itemName;}
```

Let’s elaborate upon the annotations which are defined in our entities.

@Entity annotation tells Hibernate to evaluation of our class as an entity which makes Hibernate keep track of it in **PersistenceContext.**

@**Table** annotation tells Hibernate what is our database table name.

@**Getter** and @**Setter** annotations come from [Lombok](https://projectlombok.org/) to eliminate boilerplate code.

@**OneToMany** (fetch = FetchType._LAZY_, cascade = CascadeType._ALL_) annotation defines how to fetch child objects from the databases using the parameter FetchType.Lazy. CascadeType.All means that it cascades all operations from parent to child.

@**JoinTable** (name = "shipment_items") annotation defines the owner of the relationship which is the shipment entity is our case. It creates an intermediate table to hold relations.

_Because we use `OneToMany` annotation only in the parent side, it is called a **Unidirectional** relationship. Hence we can not acquire the parent object from the child-side._

Now we need to acquire **EntityManager** from **EntityManagerFactory** to perform database operations.

Now we’ll see how to save our entities.

```
public class Main {    public static void main(String[] args) {        EntityManagerFactory emfactory = Persistence.createEntityManagerFactory("testConfig");        EntityManager entitymanager = emfactory.createEntityManager();        Shipment shipment = new Shipment();        shipment.setCargoName("test cargo");        Item item = new Item();        item.setItemName("test item");        shipment.addItem(item);        entitymanager.close();        emfactory.close();    }}
```

When we save our entities the first time, Hibernate creates corresponding tables and relations. Let’s see what queries are generated by Hibernate:

```
Hibernate: create table items (id int identity not null, itemName varchar(255), primary key (id))
```

```
Hibernate: create table shipment_items (Shipment_id int not null, childList_id int not null)
```

```
Hibernate: create table shipments (id int identity not null, cargoName varchar(255), primary key (id))
```

```
Hibernate: alter table shipment_items drop constraint UK_8ipo6hqqte0sdoftcqflf3hie
```

```
Hibernate: alter table shipment_items add constraint UK_8ipo6hqqte0sdoftcqflf3hie unique (childList_id)
```

```
Hibernate: alter table shipment_items add constraint FK20iu625dsmyisso2hrcc2qpk foreign key (childList_id) references items
```

```
Hibernate: alter table shipment_items add constraint FK6nronhhlbku40g81rfte2p02t foreign key (Shipment_id) references shipments
```

In our database, when we run the queries:

```
SELECT * FROM shipments
```

```
SELECT * FROM items
```

```
SELECT * FROM shipment_items
```

It returns empty results:

![Image](https://cdn-media-1.freecodecamp.org/images/Sw5D7HzFKQXIqxbHRL8MVD2bU9JbVzAy7a9b)

Why? Because we did not persist out entities into entityManager.

Let’s persist them:

```
shipment.addItem(item);entitymanager.persist(shipment);
```

When we run the code again and check the database, we’ll see that there is still no data. That’s because of we did not start any transaction. We need to start a transaction and then commit it just after persisting.

```
entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

When we run it again, we’ll see that Hibernate generates queries which save our entities into the database:

```
Hibernate: insert into shipments (cargoName) values (?)
```

```
Hibernate: insert into items (itemName) values (?)
```

```
Hibernate: insert into shipment_items (Shipment_id, childList_id) values (?, ?)
```

Here we see that our data is in the database:

![Image](https://cdn-media-1.freecodecamp.org/images/k4MtyzOmhHIzVZ5Q-leYe6wrMiPQZK3rBoMZ)

You remember that we use `CascadeType.ALL` in `OneToMany` annotation — so why did we use that? What happens if we don’t specify it?

Let’s remove it from the annotation:

```
@OneToMany(fetch = FetchType.LAZY)@JoinTable(name = "shipment_items")private List<Item> childList;
```

And persist our entity again:

```
entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

![Image](https://cdn-media-1.freecodecamp.org/images/coAg7ynFNSUyDr6FyqNeQ93fWfo6FObDV5Ou)

We see two thing here: one is an exception thrown by Hibernate and the other is that there is no SQL statement generated for saving our parent-child relationship when we remove the cascade type parameter. And of course, there is no data written into the database.

What we need to do? Is using the `CascadeType.ALL` is the only way to go? Of course not, but it’s the recommended way according to this use case.

> For more information about cascade types take a look [here](https://vladmihalcea.com/a-beginners-guide-to-jpa-and-hibernate-cascade-types/).

We can save the child entity explicitly and see that our relationship is saved smoothly:

```
entitymanager.getTransaction().begin();entitymanager.persist(item);entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

Now Hibernate generates the correct insert statements and we see our data in the database:

```
Hibernate: insert into items (itemName) values (?)
```

```
Hibernate: insert into shipments (cargoName) values (?)
```

```
Hibernate: insert into shipment_items (Shipment_id, childList_id) values (?, ?)
```

### Dealing with saved data

Okay, we have seen how to save entities in the form of parent-child relationships into the database. Now it’s time to retrieve the data which we saved.

```
Shipment shipment = entitymanager.find(Shipment.class, 1);System.out.println(shipment.getCargoName());
```

When we look at the output we’ll see the generated query and the getCargoName() return value:

```
Hibernate: select shipment0_.id as id1_2_0_, shipment0_.cargoName as cargoNam2_2_0_ from shipments shipment0_ where shipment0_.id=?
```

```
test cargo
```

No interesting things here. But let’s print the size of childList using `getChildList().size()` on our shipment object.

```
Shipment shipment = entitymanager.find(Shipment.class, 1);System.out.println(shipment.getCargoName());System.out.println("Size of childList : " + shipment.getChildList().size());
```

When we run the code we’ll see an additional query which fetches the child objects in the output:

```
Hibernate:
```

```
SELECTshipment0_.id AS id1_2_0_,shipment0_.cargoName AS cargoNam2_2_0_FROM shipments shipment0_WHERE shipment0_.id = ?
```

```
test cargo //the below query generated after calling getChildList() method
```

```
Hibernate:
```

```
SELECTchildlist0_.Shipment_id AS Shipment1_1_0_,childlist0_.childList_id AS childLis2_1_0_,item1_.id AS id1_0_1_,item1_.itemName AS itemName2_0_1_FROM shipment_items childlist0_INNER JOIN items item1_ON childlist0_.childList_id = item1_.idWHERE childlist0_.Shipment_id = ?
```

```
Size of childList : 1
```

What happened here is known as [Lazy Loading](https://en.wikipedia.org/wiki/Lazy_loading). Because we defined `fetch = FetchType.Lazy in @OneToMany` annotation when we loaded ther shipment object the first time, it does not load child entities together.

**In lazy relationships, a child entity loads only when you access it the first time.**

Now let’s see the eager version — we’ll change the Lazy parameter to Eager:

```
@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL)
```

Run the code again and see the output:

```
Hibernate:
```

```
SELECTshipment0_.id AS id1_2_0_,shipment0_.cargoName AS cargoNam2_2_0_,childlist1_.Shipment_id AS Shipment1_1_1_,item2_.id AS childLis2_1_1_,item2_.id AS id1_0_2_,item2_.itemName AS itemName2_0_2_FROM shipments shipment0_LEFT OUTER JOIN shipment_items childlist1_ON shipment0_.id = childlist1_.Shipment_idLEFT OUTER JOIN items item2_ON childlist1_.childList_id = item2_.idWHERE shipment0_.id = ?
```

```
test cargoSize of childList : 1
```

We see that there is not any additional query. It fetched all of it as a whole. (Now you can discard that change — it was just to show you what happens under the hood. We’ll keep going with lazy loading in the examples.)

Now let’s try to add an Item to the existing shipment.

```
Shipment shipment = entitymanager.find(Shipment.class, 1);Item item = new Item();item.setItemName("item to existing shipment");shipment.addItem(item);entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

Generated queries:

```
Hibernate:     select        shipment0_.id as id1_2_0_,        shipment0_.cargoName as cargoNam2_2_0_     from        shipments shipment0_     where        shipment0_.id=?
```

```
Hibernate:     select        childlist0_.Shipment_id as Shipment1_1_0_,        childlist0_.childList_id as childLis2_1_0_,        item1_.id as id1_0_1_,        item1_.itemName as itemName2_0_1_     from        shipment_items childlist0_     inner join        items item1_             on childlist0_.childList_id=item1_.id     where        childlist0_.Shipment_id=?
```

```
Hibernate:     insert     into        items        (itemName)     values        (?)
```

```
Hibernate:     insert     into        shipment_items        (Shipment_id, childList_id)     values        (?, ?)
```

It selects a shipment, then fetches the child entity with a join query, inserts the child entity to a table and inserts ids into intermediate table which hold relationships.

Okay, when we think about it, it looks and works as expected. Now run the code again to add another item to the shipment.

Now take a look closer at the generated queries, especially the bold ones:

```
Hibernate:     select        shipment0_.id as id1_2_0_,        shipment0_.cargoName as cargoNam2_2_0_     from        shipments shipment0_     where        shipment0_.id=?
```

```
Hibernate:     select        childlist0_.Shipment_id as Shipment1_1_0_,        childlist0_.childList_id as childLis2_1_0_,        item1_.id as id1_0_1_,        item1_.itemName as itemName2_0_1_     from        shipment_items childlist0_     inner join        items item1_             on childlist0_.childList_id=item1_.id     where        childlist0_.Shipment_id=?
```

```
Hibernate:     insert     into        items        (itemName)     values        (?)
```

```
Hibernate:     delete     from        shipment_items     where        Shipment_id=?
```

```
Hibernate:     insert     into        shipment_items        (Shipment_id, childList_id)     values        (?, ?)
```

```
Hibernate:     insert     into        shipment_items        (Shipment_id, childList_id)     values        (?, ?)
```

What happened here? We see one delete and two insert at the end of our queries.

* It selects a shipment
* Fetches the child with a join query
* Inserts the new item
* **Deletes all previous relationships from the intermediate table**
* **Inserts all relationships from zero**

Which is why it generates two insert statements at the end. Now I think you can imagine what happens if we have thousands of child items. Of course, we will not use this technique. It is a **bottleneck** for **performance** .

In the above approach, we use an intermediate table to hold relationships. As you have noticed, it generates additional queries for inserting relationships. Because we defined a `JoinTable` annotation on the shipment entity…

### Doing it another way: ManyToOne

How we avoid this situation? Well, by using the `JoinColumn` annotation instead of `JoinTable.`Let’s see how to implement it with the JoinColumn annotation.

```
@Entity@Table(name = "shipments")@Getter@Setterclass Shipment {    @Id    @GeneratedValue(strategy = GenerationType.IDENTITY)    private int id;    private String cargoName;    @OneToMany(            fetch = FetchType.LAZY,            cascade = CascadeType.ALL,            mappedBy = "shipment")    private List<Item> childList;    public void addItem(Item item) {        if (childList == null) {            childList = new ArrayList();        }        childList.add(item);        item.setShipment(this);    }}@Entity@Table(name = "items")@Getter@Setterclass Item {    @Id    @GeneratedValue(strategy = GenerationType.IDENTITY)    private int id;    private String itemName;    @ManyToOne    @JoinColumn(name = "shipment_id")    private Shipment shipment;}
```

_Note: there are two things to consider in the new relationship model above. We add the ManyToOne and JoinColumn annotations to Item. Also we add the mappedBy parameter to Shipment._

Now let’s delete all the previous tables for clarity and a fresh start. And when we run the code for the first time it creates tables and relationships as well (I changed the database from mssql to mysql because I wrote this post over a few separate days. This is why you see InnoDB in the generated queries below):

```
Hibernate:create table items (       id integer not null auto_increment,        itemName varchar(255),        shipment_id integer,        primary key (id)    ) engine=InnoDB
```

```
Hibernate:         create table shipments (       id integer not null auto_increment,        cargoName varchar(255),        primary key (id)    ) engine=InnoDB
```

```
Hibernate:         alter table items        add constraint FKcpv8kcpjc081l551hre32f2rg        foreign key (shipment_id)        references shipments (id)
```

Now again, when we insert a shipment with an item:

```
Shipment shipment = new Shipment();shipment.setCargoName("test cargo");Item item = new Item();item.setItemName("test item");shipment.addItem(item);entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

Hibernate generates only two sql queries as expected:

```
Hibernate:     insert     into        shipments        (cargoName)     values        (?)
```

```
Hibernate:     insert     into        items        (itemName, shipment_id)     values        (?, ?)
```

And our database records look like below:

![Image](https://cdn-media-1.freecodecamp.org/images/AzyCvRemBg6yhzntc4XzIC7dinDHLgPY4uhB)

![Image](https://cdn-media-1.freecodecamp.org/images/Yv5jiOWXdwX7hY1gZHqJNL2R9gNYcp-c827E)

What about selecting a shipment from db? How will it change our queries?

Let’s run the below code and see our generated queries:

```
Shipment shipment = entitymanager.find(Shipment.class, 1);System.out.println(shipment.getCargoName());System.out.println(shipment.getChildList().size());
```

Output:

```
Hibernate:     select        shipment0_.id as id1_1_0_,        shipment0_.cargoName as cargoNam2_1_0_     from        shipments shipment0_     where        shipment0_.id=?
```

```
test cargo
```

```
Hibernate:     select        childlist0_.shipment_id as shipment3_0_0_,        childlist0_.id as id1_0_0_,        childlist0_.id as id1_0_1_,        childlist0_.itemName as itemName2_0_1_,        childlist0_.shipment_id as shipment3_0_1_     from        items childlist0_     where        childlist0_.shipment_id=?
```

First hibernate selects a shipment from the db. And then because we call the getChildList().size() method, it lazy loads the child entities. Do you see that there are no Join queries when loading the child entities because there is no intermediate table like in the first example?

Now let’s add an item to the existing shipment and compare the generated queries with the first example. As you remember from the first example, when we try to add a new item to the existing shipment, it loads all child entities and deletes relationships from the intermediate table. Then it inserts the relationships again. It is a huge performance issue when you work with heavy data sets.

But with our new approach, it is easy to solve this problem:

```
Shipment shipment = entitymanager.find(Shipment.class, 1);Item item = new Item();item.setItemName("item to existing shipment");shipment.addItem(item);entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

It generates just two queries as it should, one select for the shipment and one insert for the child:

```
Hibernate:     select        shipment0_.id as id1_1_0_,        shipment0_.cargoName as cargoNam2_1_0_     from        shipments shipment0_     where        shipment0_.id=?
```

```
Hibernate:     insert     into        items        (itemName, shipment_id)     values        (?, ?)
```

Now it is time to show you one common problem while working with ORM tools. Suppose we have 3 shipments and every shipment has 3 child items. What happens when we retrieve those shipments and try to iterate their children?

We insert our initial data:

```
for (int i = 1; i <= 3; i++) {    Shipment shipment = new Shipment();    shipment.setCargoName("test shipment " + i);    for (int j = 1; j <= 3; j++) {        Item item = new Item();        item.setItemName("test item " + j);        shipment.addItem(item);    }    entitymanager.getTransaction().begin();    entitymanager.persist(shipment);    entitymanager.getTransaction().commit();}
```

Let’s list all shipment entities in our database and print their child item’s sizes:

```
EntityManagerFactory emfactory = Persistence.createEntityManagerFactory("Hibernate_Jpa");EntityManager entitymanager = emfactory.createEntityManager();List<Shipment> shipments = entitymanager.createQuery("select s from Shipment s").getResultList();for (Shipment shipment : shipments) {    System.out.println(shipment.getChildList().size());}entitymanager.close();emfactory.close();
```

Here are our generated queries:

```
Hibernate:     select        shipment0_.id as id1_1_,        shipment0_.cargoName as cargoNam2_1_     from        shipments shipment0_
```

```
Hibernate:     select        childlist0_.shipment_id as shipment3_0_0_,        childlist0_.id as id1_0_0_,        childlist0_.id as id1_0_1_,        childlist0_.itemName as itemName2_0_1_,        childlist0_.shipment_id as shipment3_0_1_     from        items childlist0_     where        childlist0_.shipment_id=?
```

```
Child item size for shipment id:1 is 3
```

```
Hibernate:     select        childlist0_.shipment_id as shipment3_0_0_,        childlist0_.id as id1_0_0_,        childlist0_.id as id1_0_1_,        childlist0_.itemName as itemName2_0_1_,        childlist0_.shipment_id as shipment3_0_1_     from        items childlist0_     where        childlist0_.shipment_id=?
```

```
Child item size for shipment id:2 is 3
```

```
Hibernate:     select        childlist0_.shipment_id as shipment3_0_0_,        childlist0_.id as id1_0_0_,        childlist0_.id as id1_0_1_,        childlist0_.itemName as itemName2_0_1_,        childlist0_.shipment_id as shipment3_0_1_     from        items childlist0_     where        childlist0_.shipment_id=?
```

```
Child item size for shipment id:3 is 3
```

What happened here is called the [**N + 1 problem.**](https://stackoverflow.com/questions/97197/what-is-the-n1-select-query-issue) Because 1 query executed for selecting all shipments and N (where N is the size of shipments, which is 3 for our example) queries executed for selecting child entities.

To solve this problem we have several options.

One of them is to use `BatchSize` annotation.

It is possible to tune the batch size for each query. Let’s put the annotation on our relationship and see the generated SQL.

```
@OneToMany(        fetch = FetchType.LAZY,        cascade = CascadeType.ALL,        mappedBy = "shipment")@BatchSize(size = 10)private List<Item> childList;
```

I gave batch size 10 for testing purposes. And the below query was generated.

```
Hibernate:     select        shipment0_.id as id1_1_,        shipment0_.cargoName as cargoNam2_1_     from        shipments shipment0_Hibernate:     select        childlist0_.shipment_id as shipment3_0_1_,        childlist0_.id as id1_0_1_,        childlist0_.id as id1_0_0_,        childlist0_.itemName as itemName2_0_0_,        childlist0_.shipment_id as shipment3_0_0_     from        items childlist0_     where        childlist0_.shipment_id in (            ?, ?, ?        )
```

```
Child item size for shipment id:1 is 3Child item size for shipment id:2 is 3Child item size for shipment id:3 is 3
```

Because we have 3 shipments and the batch size is 10, it adds the 3 shipment ids in the where query. If batch size was set to 2, there would be 2 shipment ids in the where query.

Another solution is using `fetch join` in the jpql.

We change our query to:

```
List<Shipment> shipments = entitymanager.createQuery("select s from Shipment s join fetch s.childList").getResultList();
```

And we run the code again. It generates the following output:

```
Hibernate:     select        shipment0_.id as id1_1_0_,        childlist1_.id as id1_0_1_,        shipment0_.cargoName as cargoNam2_1_0_,        childlist1_.itemName as itemName2_0_1_,        childlist1_.shipment_id as shipment3_0_1_,        childlist1_.shipment_id as shipment3_0_0__,        childlist1_.id as id1_0_0__     from        shipments shipment0_     inner join        items childlist1_             on shipment0_.id=childlist1_.shipment_id
```

```
Child item size for shipment id:1 is 3Child item size for shipment id:1 is 3Child item size for shipment id:1 is 3Child item size for shipment id:2 is 3Child item size for shipment id:2 is 3Child item size for shipment id:2 is 3Child item size for shipment id:3 is 3Child item size for shipment id:3 is 3Child item size for shipment id:3 is 3
```

Wow, what just happened? Why are there 9 outputs for printing sizes? Because the jpql query generates an inner join SQL query, it causes duplicate records for every child. Hence, 3 shipments x 3 children = 9 duplicated outputs. To avoid this duplication, we need to add one more keyword to our jqpl which is the `distinct` keyword.

```
List<Shipment> shipments = entitymanager.createQuery("select distinct s from Shipment s join fetch s.childList").getResultList();
```

Now the output had been generated just as expected:

```
Hibernate:     select        distinct shipment0_.id as id1_1_0_,        childlist1_.id as id1_0_1_,        shipment0_.cargoName as cargoNam2_1_0_,        childlist1_.itemName as itemName2_0_1_,        childlist1_.shipment_id as shipment3_0_1_,        childlist1_.shipment_id as shipment3_0_0__,        childlist1_.id as id1_0_0__     from        shipments shipment0_     inner join        items childlist1_             on shipment0_.id=childlist1_.shipment_id
```

```
Child item size for shipment id:1 is 3Child item size for shipment id:2 is 3Child item size for shipment id:3 is 3
```

And this way we solve the duplicate issues.

I think that is enough for one post as it has become quite long already. Thank you all for reading so far. I hope it is now clear to you how Hibernate manages relationships, what queries are generated under the hood, and how to avoid some common mistakes.

### **Conclusion**

* Prefer lazy loading when you can use it
* Use Bidirectional association with ManyToOne annotation on child entities when you need to (rather than OneToMany)
* Give the responsibility of relationships to the child side whenever possible
* To avoid the N + 1 problem, use `BatchSize` annotation or write jpql with `fetch join`
* Use `JoinColumn` instead of `JoinTable` on OneToMany relationships to avoid additional join queries

You can find the example code in my github repository: [hibernate-examples](https://github.com/mstrYoda/hibernate-examples)

**Resources**

[**HIBERNATE - Relational Persistence for Idiomatic Java**](http://docs.jboss.org/hibernate/orm/4.3/manual/en-US/html_single/#performance-fetching-batch)  
[_Hibernate not only takes care of the mapping from Java classes to database tables (and from Java data types to SQL data…_docs.jboss.org](http://docs.jboss.org/hibernate/orm/4.3/manual/en-US/html_single/#performance-fetching-batch)[**What is the N+1 SELECT query issue?**](https://stackoverflow.com/questions/97197/what-is-the-n1-select-query-issue?noredirect=1&lq=1)  
[_SELECT N+1 is generally stated as a problem in Object-Relational mapping (ORM) discussions, and I understand that it…_stackoverflow.com](https://stackoverflow.com/questions/97197/what-is-the-n1-select-query-issue?noredirect=1&lq=1)[**A beginner's guide to JPA and Hibernate Cascade Types - Vlad Mihalcea**](https://vladmihalcea.com/a-beginners-guide-to-jpa-and-hibernate-cascade-types/)  
[_(Last Updated On: April 25, 2018)Introduction JPA translates entity state transitions to database DML statements…_vladmihalcea.com](https://vladmihalcea.com/a-beginners-guide-to-jpa-and-hibernate-cascade-types/)

