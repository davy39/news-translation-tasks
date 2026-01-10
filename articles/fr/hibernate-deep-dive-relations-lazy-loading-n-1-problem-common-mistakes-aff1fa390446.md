---
title: Comment utiliser Hibernate pour interagir avec les bases de données relationnelles
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
seo_title: Comment utiliser Hibernate pour interagir avec les bases de données relationnelles
seo_desc: 'By Emre Savcı

  Dealing with Deep Dive Relations, Lazy Loading, and the N+1 Problem

  Hibernate is an Object Relational Mapping tool which allows us to use objects for
  interaction with relational databases. It has many features like code first modeling,
  ...'
---

Par Emre Savcı

#### Gestion des relations approfondies, du chargement paresseux et du problème N+1

Hibernate est un outil de [Mapping Objet-Relationnel](https://en.wikipedia.org/wiki/Object-relational_mapping) qui nous permet d'utiliser des objets pour interagir avec des bases de données relationnelles. Il possède de nombreuses fonctionnalités comme la modélisation code first, le chargement paresseux, le suivi des changements, la mise en cache, l'audit, etc.

Dans cet article, je vais présenter et discuter des relations **OneToMany** et **ManyToOne**. Nous verrons également quelles sont les conséquences de la construction de mauvaises relations ou de l'utilisation du mauvais **type de fetch**. J'examinerai également les relations bidirectionnelles et unidirectionnelles.

### OneToMany

Commençons par la relation OneToMany unidirectionnelle. Imaginons que nous avons une entité **Shipment** et qu'une expédition peut contenir plusieurs **Item**s.

_Note : le code ci-dessous est juste là pour vous montrer la manière directe d'implémenter une relation, mais il n'est pas recommandé de l'utiliser en production. Je l'expliquerai à la fin des exemples de code._

D'abord, notre persistence.xml :

```
<?xml version="1.0" encoding="UTF-8"?><persistence version="2.0" xmlns="http://java.sun.com/xml/ns/persistence"             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"             xsi:schemaLocation="http://java.sun.com/xml/ns/persistence             http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">    <persistence-unit name="testConfig" transaction-type="RESOURCE_LOCAL">        <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>        <class>deneme.Shipment</class>        <class>deneme.Item</class>        <properties>            <property name="javax.persistence.jdbc.url" value="jdbc:mysql://localhost:3306/jpadb"/>            <property name="javax.persistence.jdbc.user" value="root"/>            <property name="javax.persistence.jdbc.password" value="root"/>            <property name="javax.persistence.jdbc.driver" value="com.mysql.jdbc.Driver"/>            <property name="hibernate.logging.level" value="FINE"/>            <property name="hibernate.show_sql" value="true"/>            <property name="hibernate.format_sql" value="true"/>            <property name="hibernate.ddl-generation" value="auto"/>            <property name="hibernate.hbm2ddl.auto" value="update"/>        </properties>    </persistence-unit></persistence>
```

Et nos dépendances pom.xml :

```
<dependencies><dependency>    <groupId>org.projectlombok</groupId>    <artifactId>lombok</artifactId>    <version>1.18.2</version>    <scope>provided</scope></dependency>
```

```
<dependency>    <groupId>org.hibernate</groupId>    <artifactId>hibernate-entitymanager</artifactId>    <version>5.3.3.Final</version></dependency><!-- https://mvnrepository.com/artifact/org.hibernate/hibernate-core --><dependency>    <groupId>org.hibernate</groupId>    <artifactId>hibernate-core</artifactId>    <version>5.3.3.Final</version></dependency>
```

```
<!-- https://mvnrepository.com/artifact/mysql/mysql-connector-java --><dependency>    <groupId>mysql</groupId>    <artifactId>mysql-connector-java</artifactId>    <version>5.1.6</version></dependency><dependencies>
```

Voici nos entités :

```
@Entity@Table(name = "shipments")@Getter@Setterclass Shipment {    @Id    @GeneratedValue(strategy = GenerationType.IDENTITY)    private int id;    private String cargoName;    @OneToMany(fetch = FetchType.LAZY, cascade = CascadeType.ALL)    @JoinTable(name = "shipment_items")    private List<Item> childList;        public void addItem(Item item) {        if (childList == null) {            childList = new ArrayList();        }        childList.add(item);    }}@Entity@Table(name = "items")@Getter@Setterclass Item {    @Id    @GeneratedValue(strategy = GenerationType.IDENTITY)    private int id;    private String itemName;}
```

Élaborons sur les annotations qui sont définies dans nos entités.

L'annotation @Entity indique à Hibernate d'évaluer notre classe comme une entité, ce qui fait que Hibernate la suit dans le **PersistenceContext**.

L'annotation @**Table** indique à Hibernate quel est le nom de notre table de base de données.

Les annotations @**Getter** et @**Setter** proviennent de [Lombok](https://projectlombok.org/) pour éliminer le code boilerplate.

L'annotation @**OneToMany** (fetch = FetchType._LAZY_, cascade = CascadeType._ALL_) définit comment récupérer les objets enfants des bases de données en utilisant le paramètre FetchType.Lazy. CascadeType.All signifie qu'il cascade toutes les opérations du parent à l'enfant.

L'annotation @**JoinTable** (name = "shipment_items") définit le propriétaire de la relation qui est l'entité shipment dans notre cas. Elle crée une table intermédiaire pour maintenir les relations.

_Puisque nous utilisons l'annotation `OneToMany` uniquement du côté parent, elle est appelée une relation **Unidirectionnelle**. Par conséquent, nous ne pouvons pas acquérir l'objet parent du côté enfant._

Maintenant, nous devons acquérir **EntityManager** à partir de **EntityManagerFactory** pour effectuer des opérations de base de données.

Maintenant, nous allons voir comment sauvegarder nos entités.

```
public class Main {    public static void main(String[] args) {        EntityManagerFactory emfactory = Persistence.createEntityManagerFactory("testConfig");        EntityManager entitymanager = emfactory.createEntityManager();        Shipment shipment = new Shipment();        shipment.setCargoName("test cargo");        Item item = new Item();        item.setItemName("test item");        shipment.addItem(item);        entitymanager.close();        emfactory.close();    }}
```

Lorsque nous sauvegardons nos entités pour la première fois, Hibernate crée les tables et relations correspondantes. Voyons quelles requêtes sont générées par Hibernate :

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

Dans notre base de données, lorsque nous exécutons les requêtes :

```
SELECT * FROM shipments
```

```
SELECT * FROM items
```

```
SELECT * FROM shipment_items
```

Cela retourne des résultats vides :

![Image](https://cdn-media-1.freecodecamp.org/images/Sw5D7HzFKQXIqxbHRL8MVD2bU9JbVzAy7a9b)

Pourquoi ? Parce que nous n'avons pas persisté nos entités dans entityManager.

Persistons-les :

```
shipment.addItem(item);entitymanager.persist(shipment);
```

Lorsque nous exécutons le code à nouveau et vérifions la base de données, nous verrons qu'il n'y a toujours pas de données. C'est parce que nous n'avons pas démarré de transaction. Nous devons démarrer une transaction et ensuite la valider juste après la persistance.

```
entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

Lorsque nous l'exécutons à nouveau, nous verrons que Hibernate génère des requêtes qui sauvegardent nos entités dans la base de données :

```
Hibernate: insert into shipments (cargoName) values (?)
```

```
Hibernate: insert into items (itemName) values (?)
```

```
Hibernate: insert into shipment_items (Shipment_id, childList_id) values (?, ?)
```

Ici, nous voyons que nos données sont dans la base de données :

![Image](https://cdn-media-1.freecodecamp.org/images/k4MtyzOmhHIzVZ5Q-leYe6wrMiPQZK3rBoMZ)

Vous vous souvenez que nous utilisons `CascadeType.ALL` dans l'annotation `OneToMany` — alors pourquoi l'avons-nous utilisé ? Que se passe-t-il si nous ne le spécifions pas ?

Retirons-le de l'annotation :

```
@OneToMany(fetch = FetchType.LAZY)@JoinTable(name = "shipment_items")private List<Item> childList;
```

Et persistons notre entité à nouveau :

```
entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

![Image](https://cdn-media-1.freecodecamp.org/images/coAg7ynFNSUyDr6FyqNeQ93fWfo6FObDV5Ou)

Nous voyons deux choses ici : l'une est une exception lancée par Hibernate et l'autre est qu'il n'y a pas d'instruction SQL générée pour sauvegarder notre relation parent-enfant lorsque nous supprimons le paramètre de type de cascade. Et bien sûr, il n'y a pas de données écrites dans la base de données.

Que devons-nous faire ? Utiliser `CascadeType.ALL` est-il le seul moyen ? Bien sûr que non, mais c'est la manière recommandée selon ce cas d'utilisation.

> Pour plus d'informations sur les types de cascade, consultez [ici](https://vladmihalcea.com/a-beginners-guide-to-jpa-and-hibernate-cascade-types/).

Nous pouvons sauvegarder l'entité enfant explicitement et voir que notre relation est sauvegardée en douceur :

```
entitymanager.getTransaction().begin();entitymanager.persist(item);entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

Maintenant, Hibernate génère les instructions d'insertion correctes et nous voyons nos données dans la base de données :

```
Hibernate: insert into items (itemName) values (?)
```

```
Hibernate: insert into shipments (cargoName) values (?)
```

```
Hibernate: insert into shipment_items (Shipment_id, childList_id) values (?, ?)
```

### Gestion des données sauvegardées

D'accord, nous avons vu comment sauvegarder des entités sous forme de relations parent-enfant dans la base de données. Maintenant, il est temps de récupérer les données que nous avons sauvegardées.

```
Shipment shipment = entitymanager.find(Shipment.class, 1);System.out.println(shipment.getCargoName());
```

Lorsque nous regardons la sortie, nous verrons la requête générée et la valeur de retour de getCargoName() :

```
Hibernate: select shipment0_.id as id1_2_0_, shipment0_.cargoName as cargoNam2_2_0_ from shipments shipment0_ where shipment0_.id=?
```

```
test cargo
```

Rien d'intéressant ici. Mais essayons d'imprimer la taille de childList en utilisant `getChildList().size()` sur notre objet shipment.

```
Shipment shipment = entitymanager.find(Shipment.class, 1);System.out.println(shipment.getCargoName());System.out.println("Size of childList : " + shipment.getChildList().size());
```

Lorsque nous exécutons le code, nous verrons une requête supplémentaire qui récupère les objets enfants dans la sortie :

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

Ce qui s'est passé ici est connu sous le nom de [Lazy Loading](https://en.wikipedia.org/wiki/Lazy_loading). Parce que nous avons défini `fetch = FetchType.Lazy` dans l'annotation `@OneToMany`, lorsque nous avons chargé l'objet shipment la première fois, il ne charge pas les entités enfants ensemble.

**Dans les relations paresseuses, une entité enfant ne se charge que lorsque vous y accédez pour la première fois.**

Maintenant, voyons la version eager — nous allons changer le paramètre Lazy en Eager :

```
@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL)
```

Exécutez le code à nouveau et voyez la sortie :

```
Hibernate:
```

```
SELECTshipment0_.id AS id1_2_0_,shipment0_.cargoName AS cargoNam2_2_0_,childlist1_.Shipment_id AS Shipment1_1_1_,item2_.id AS childLis2_1_1_,item2_.id AS id1_0_2_,item2_.itemName AS itemName2_0_2_FROM shipments shipment0_LEFT OUTER JOIN shipment_items childlist1_ON shipment0_.id = childlist1_.Shipment_idLEFT OUTER JOIN items item2_ON childlist1_.childList_id = item2_.idWHERE shipment0_.id = ?
```

```
test cargoSize of childList : 1
```

Nous voyons qu'il n'y a pas de requête supplémentaire. Il a récupéré tout cela en une seule fois. (Maintenant vous pouvez ignorer ce changement — c'était juste pour vous montrer ce qui se passe sous le capot. Nous continuerons avec le chargement paresseux dans les exemples.)

Maintenant, essayons d'ajouter un Item à l'expédition existante.

```
Shipment shipment = entitymanager.find(Shipment.class, 1);Item item = new Item();item.setItemName("item to existing shipment");shipment.addItem(item);entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

Requêtes générées :

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

Il sélectionne une expédition, puis récupère l'entité enfant avec une requête de jointure, insère l'entité enfant dans une table et insère les identifiants dans la table intermédiaire qui maintient les relations.

D'accord, lorsque nous y réfléchissons, cela semble et fonctionne comme prévu. Maintenant, exécutez le code à nouveau pour ajouter un autre élément à l'expédition.

Maintenant, regardez de plus près les requêtes générées, surtout celles en gras :

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

Que s'est-il passé ici ? Nous voyons une suppression et deux insertions à la fin de nos requêtes.

* Il sélectionne une expédition
* Récupère l'enfant avec une requête de jointure
* Insère le nouvel élément
* **Supprime toutes les relations précédentes de la table intermédiaire**
* **Insère toutes les relations à partir de zéro**

C'est pourquoi il génère deux instructions d'insertion à la fin. Maintenant, je pense que vous pouvez imaginer ce qui se passe si nous avons des milliers d'éléments enfants. Bien sûr, nous n'utiliserons pas cette technique. C'est un **goulot d'étranglement** pour les **performances** .

Dans l'approche ci-dessus, nous utilisons une table intermédiaire pour maintenir les relations. Comme vous l'avez remarqué, elle génère des requêtes supplémentaires pour insérer des relations. Parce que nous avons défini une annotation `JoinTable` sur l'entité shipment...

### Faire cela différemment : ManyToOne

Comment éviter cette situation ? Eh bien, en utilisant l'annotation `JoinColumn` au lieu de `JoinTable`. Voyons comment l'implémenter avec l'annotation JoinColumn.

```
@Entity@Table(name = "shipments")@Getter@Setterclass Shipment {    @Id    @GeneratedValue(strategy = GenerationType.IDENTITY)    private int id;    private String cargoName;    @OneToMany(            fetch = FetchType.LAZY,            cascade = CascadeType.ALL,            mappedBy = "shipment")    private List<Item> childList;    public void addItem(Item item) {        if (childList == null) {            childList = new ArrayList();        }        childList.add(item);        item.setShipment(this);    }}@Entity@Table(name = "items")@Getter@Setterclass Item {    @Id    @GeneratedValue(strategy = GenerationType.IDENTITY)    private int id;    private String itemName;    @ManyToOne    @JoinColumn(name = "shipment_id")    private Shipment shipment;}
```

_Note : il y a deux choses à considérer dans le nouveau modèle de relation ci-dessus. Nous ajoutons les annotations ManyToOne et JoinColumn à Item. Nous ajoutons également le paramètre mappedBy à Shipment._

Maintenant, supprimons toutes les tables précédentes pour plus de clarté et un nouveau départ. Et lorsque nous exécutons le code pour la première fois, il crée des tables et des relations également (j'ai changé la base de données de mssql à mysql parce que j'ai écrit cet article sur quelques jours séparés. C'est pourquoi vous voyez InnoDB dans les requêtes générées ci-dessous) :

```
Hibernate:create table items (       id integer not null auto_increment,        itemName varchar(255),        shipment_id integer,        primary key (id)    ) engine=InnoDB
```

```
Hibernate:         create table shipments (       id integer not null auto_increment,        cargoName varchar(255),        primary key (id)    ) engine=InnoDB
```

```
Hibernate:         alter table items        add constraint FKcpv8kcpjc081l551hre32f2rg        foreign key (shipment_id)        references shipments (id)
```

Maintenant, lorsque nous insérons une expédition avec un élément :

```
Shipment shipment = new Shipment();shipment.setCargoName("test cargo");Item item = new Item();item.setItemName("test item");shipment.addItem(item);entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

Hibernate génère seulement deux requêtes SQL comme prévu :

```
Hibernate:     insert     into        shipments        (cargoName)     values        (?)
```

```
Hibernate:     insert     into        items        (itemName, shipment_id)     values        (?, ?)
```

Et nos enregistrements de base de données ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/AzyCvRemBg6yhzntc4XzIC7dinDHLgPY4uhB)

![Image](https://cdn-media-1.freecodecamp.org/images/Yv5jiOWXdwX7hY1gZHqJNL2R9gNYcp-c827E)

Et si nous sélectionnons une expédition depuis la base de données ? Comment cela changera-t-il nos requêtes ?

Exécutons le code ci-dessous et voyons nos requêtes générées :

```
Shipment shipment = entitymanager.find(Shipment.class, 1);System.out.println(shipment.getCargoName());System.out.println(shipment.getChildList().size());
```

Sortie :

```
Hibernate:     select        shipment0_.id as id1_1_0_,        shipment0_.cargoName as cargoNam2_1_0_     from        shipments shipment0_     where        shipment0_.id=?
```

```
test cargo
```

```
Hibernate:     select        childlist0_.shipment_id as shipment3_0_0_,        childlist0_.id as id1_0_0_,        childlist0_.id as id1_0_1_,        childlist0_.itemName as itemName2_0_1_,        childlist0_.shipment_id as shipment3_0_1_     from        items childlist0_     where        childlist0_.shipment_id=?
```

D'abord, Hibernate sélectionne une expédition depuis la base de données. Et ensuite, parce que nous appelons la méthode getChildList().size(), il charge paresseusement les entités enfants. Voyez-vous qu'il n'y a pas de requêtes de jointure lors du chargement des entités enfants parce qu'il n'y a pas de table intermédiaire comme dans le premier exemple ?

Maintenant, essayons d'ajouter un élément à l'expédition existante et comparons les requêtes générées avec le premier exemple. Comme vous vous en souvenez dans le premier exemple, lorsque nous essayons d'ajouter un nouvel élément à l'expédition existante, il charge toutes les entités enfants et supprime les relations de la table intermédiaire. Ensuite, il insère à nouveau les relations. C'est un énorme problème de performance lorsque vous travaillez avec des ensembles de données lourds.

Mais avec notre nouvelle approche, il est facile de résoudre ce problème :

```
Shipment shipment = entitymanager.find(Shipment.class, 1);Item item = new Item();item.setItemName("item to existing shipment");shipment.addItem(item);entitymanager.getTransaction().begin();entitymanager.persist(shipment);entitymanager.getTransaction().commit();
```

Il génère seulement deux requêtes comme il se doit, une sélection pour l'expédition et une insertion pour l'enfant :

```
Hibernate:     select        shipment0_.id as id1_1_0_,        shipment0_.cargoName as cargoNam2_1_0_     from        shipments shipment0_     where        shipment0_.id=?
```

```
Hibernate:     insert     into        items        (itemName, shipment_id)     values        (?, ?)
```

Maintenant, il est temps de vous montrer un problème courant lors de l'utilisation d'outils ORM. Supposons que nous avons 3 expéditions et que chaque expédition a 3 éléments enfants. Que se passe-t-il lorsque nous récupérons ces expéditions et essayons de parcourir leurs enfants ?

Nous insérons nos données initiales :

```
for (int i = 1; i <= 3; i++) {    Shipment shipment = new Shipment();    shipment.setCargoName("test shipment " + i);    for (int j = 1; j <= 3; j++) {        Item item = new Item();        item.setItemName("test item " + j);        shipment.addItem(item);    }    entitymanager.getTransaction().begin();    entitymanager.persist(shipment);    entitymanager.getTransaction().commit();}
```

Listons toutes les entités d'expédition dans notre base de données et imprimons les tailles de leurs éléments enfants :

```
EntityManagerFactory emfactory = Persistence.createEntityManagerFactory("Hibernate_Jpa");EntityManager entitymanager = emfactory.createEntityManager();List<Shipment> shipments = entitymanager.createQuery("select s from Shipment s").getResultList();for (Shipment shipment : shipments) {    System.out.println(shipment.getChildList().size());}entitymanager.close();emfactory.close();
```

Voici nos requêtes générées :

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

Ce qui s'est passé ici est appelé le problème [**N + 1**](https://stackoverflow.com/questions/97197/what-is-the-n1-select-query-issue). Parce qu'une requête est exécutée pour sélectionner toutes les expéditions et N (où N est la taille des expéditions, qui est 3 pour notre exemple) requêtes sont exécutées pour sélectionner les entités enfants.

Pour résoudre ce problème, nous avons plusieurs options.

L'une d'entre elles est d'utiliser l'annotation `BatchSize`.

Il est possible de régler la taille du lot pour chaque requête. Mettons l'annotation sur notre relation et voyons le SQL généré.

```
@OneToMany(        fetch = FetchType.LAZY,        cascade = CascadeType.ALL,        mappedBy = "shipment")@BatchSize(size = 10)private List<Item> childList;
```

J'ai donné une taille de lot de 10 à des fins de test. Et la requête suivante a été générée.

```
Hibernate:     select        shipment0_.id as id1_1_,        shipment0_.cargoName as cargoNam2_1_     from        shipments shipment0_Hibernate:     select        childlist0_.shipment_id as shipment3_0_1_,        childlist0_.id as id1_0_1_,        childlist0_.id as id1_0_0_,        childlist0_.itemName as itemName2_0_0_,        childlist0_.shipment_id as shipment3_0_0_     from        items childlist0_     where        childlist0_.shipment_id in (            ?, ?, ?        )
```

```
Child item size for shipment id:1 is 3Child item size for shipment id:2 is 3Child item size for shipment id:3 is 3
```

Parce que nous avons 3 expéditions et que la taille du lot est de 10, il ajoute les 3 identifiants d'expédition dans la requête where. Si la taille du lot était réglée sur 2, il y aurait 2 identifiants d'expédition dans la requête where.

Une autre solution est d'utiliser `fetch join` dans le jpql.

Nous changeons notre requête en :

```
List<Shipment> shipments = entitymanager.createQuery("select s from Shipment s join fetch s.childList").getResultList();
```

Et nous exécutons le code à nouveau. Il génère la sortie suivante :

```
Hibernate:     select        shipment0_.id as id1_1_0_,        childlist1_.id as id1_0_1_,        shipment0_.cargoName as cargoNam2_1_0_,        childlist1_.itemName as itemName2_0_1_,        childlist1_.shipment_id as shipment3_0_1_,        childlist1_.shipment_id as shipment3_0_0__,        childlist1_.id as id1_0_0__     from        shipments shipment0_     inner join        items childlist1_             on shipment0_.id=childlist1_.shipment_id
```

```
Child item size for shipment id:1 is 3Child item size for shipment id:1 is 3Child item size for shipment id:1 is 3Child item size for shipment id:2 is 3Child item size for shipment id:2 is 3Child item size for shipment id:2 is 3Child item size for shipment id:3 is 3Child item size for shipment id:3 is 3Child item size for shipment id:3 is 3
```

Wow, que s'est-il passé ? Pourquoi y a-t-il 9 sorties pour l'impression des tailles ? Parce que la requête jpql génère une requête SQL de jointure interne, elle provoque des enregistrements en double pour chaque enfant. Par conséquent, 3 expéditions x 3 enfants = 9 sorties en double. Pour éviter cette duplication, nous devons ajouter un mot-clé supplémentaire à notre jqpl qui est le mot-clé `distinct`.

```
List<Shipment> shipments = entitymanager.createQuery("select distinct s from Shipment s join fetch s.childList").getResultList();
```

Maintenant, la sortie a été générée comme prévu :

```
Hibernate:     select        distinct shipment0_.id as id1_1_0_,        childlist1_.id as id1_0_1_,        shipment0_.cargoName as cargoNam2_1_0_,        childlist1_.itemName as itemName2_0_1_,        childlist1_.shipment_id as shipment3_0_1_,        childlist1_.shipment_id as shipment3_0_0__,        childlist1_.id as id1_0_0__     from        shipments shipment0_     inner join        items childlist1_             on shipment0_.id=childlist1_.shipment_id
```

```
Child item size for shipment id:1 is 3Child item size for shipment id:2 is 3Child item size for shipment id:3 is 3
```

Et de cette manière, nous résolvons les problèmes de duplication.

Je pense que cela suffit pour un article, car il est déjà devenu assez long. Merci à tous d'avoir lu jusqu'ici. J'espère qu'il est maintenant clair pour vous comment Hibernate gère les relations, quelles requêtes sont générées sous le capot, et comment éviter certaines erreurs courantes.

### **Conclusion**

* Préférez le chargement paresseux lorsque vous pouvez l'utiliser
* Utilisez l'association bidirectionnelle avec l'annotation ManyToOne sur les entités enfants lorsque vous en avez besoin (plutôt que OneToMany)
* Donnez la responsabilité des relations au côté enfant chaque fois que possible
* Pour éviter le problème N + 1, utilisez l'annotation `BatchSize` ou écrivez jpql avec `fetch join`
* Utilisez `JoinColumn` au lieu de `JoinTable` sur les relations OneToMany pour éviter les requêtes de jointure supplémentaires

Vous pouvez trouver le code exemple dans mon dépôt github : [hibernate-examples](https://github.com/mstrYoda/hibernate-examples)

**Ressources**

[**HIBERNATE - Persistance relationnelle pour Java idiomatique**](http://docs.jboss.org/hibernate/orm/4.3/manual/en-US/html_single/#performance-fetching-batch)  
[_Hibernate ne prend pas seulement en charge la cartographie des classes Java vers les tables de base de données (et des types de données Java vers les types SQL..._docs.jboss.org](http://docs.jboss.org/hibernate/orm/4.3/manual/en-US/html_single/#performance-fetching-batch)[**Qu'est-ce que le problème de requête SELECT N+1 ?**](https://stackoverflow.com/questions/97197/what-is-the-n1-select-query-issue?noredirect=1&lq=1)  
[_SELECT N+1 est généralement énoncé comme un problème dans les discussions sur la cartographie objet-relationnelle (ORM), et je comprends que cela..._stackoverflow.com](https://stackoverflow.com/questions/97197/what-is-the-n1-select-query-issue?noredirect=1&lq=1)[**Un guide du débutant sur les types de cascade JPA et Hibernate - Vlad Mihalcea**](https://vladmihalcea.com/a-beginners-guide-to-jpa-and-hibernate-cascade-types/)  
[_(Dernière mise à jour le : 25 avril 2018) Introduction JPA traduit les transitions d'état des entités en instructions DML de base de données..._vladmihalcea.com](https://vladmihalcea.com/a-beginners-guide-to-jpa-and-hibernate-cascade-types/)