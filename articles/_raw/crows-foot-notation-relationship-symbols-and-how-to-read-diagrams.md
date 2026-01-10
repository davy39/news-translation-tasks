---
title: Crow's Foot Notation – Relationship Symbols And How to Read Diagrams
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-06T15:11:31.000Z'
originalURL: https://freecodecamp.org/news/crows-foot-notation-relationship-symbols-and-how-to-read-diagrams
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/hanna-morris-_XXNjSziZuA-unsplash.jpg
tags:
- name: database
  slug: database
seo_title: null
seo_desc: "Entity relationship diagrams (ERD) help us understand the connection between\
  \ various \"entities\" that make up a system. \nIn software development, ERDs are\
  \ mostly used in database design. This lets us create graphical representations\
  \ of the entities th..."
---

Entity relationship diagrams (ERD) help us understand the connection between various "entities" that make up a system. 

In software development, ERDs are mostly used in database design. This lets us create graphical representations of the entities that make up systems such as a database (you will understand this better with the examples in this tutorial). 

In order to understand the relationship between entities in an ERD, we use specific symbols and notations. 

Although there are various notations for understanding ERDs, we'll focus on Crow's Foot Notation which is one of the most commonly used when creating/designing ERDs.

This tutorial will help you understand what entities and their attributes are in entity relationship diagrams, the various symbols in crow's foot notation that you can use to define the relationship between entities, and how to read and understand diagrams. 

At the end of the tutorial, you should be able to understand and read diagrams, and create your own entity relationship diagrams making use of crow's foot notation to define your entity relationships.

You'll see the words: notation, indicators, and symbols used interchangeably.

## What Is an Entity in ERDs?

Before we look at some examples, let's talk about some of the key terms/components that'll make up the entity relationship diagrams we'll be working with. 

The first is the **entity**. An entity simply represents an object in our database. This could be an object for users, courses, products, and so on. 

Note that the name of every entity should be singular (user) and not plural (users).

Here is what an entity looks like:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/entity.png)

The diagram above shows an entity called user. This entity will have information about the various users registered on a platform. 

In the next section, we'll talk about attributes. 

## What Are Attributes in ERDs?

We've talked about entities and we know they store some sort of information about the object they're representing.

The information about an object is the attributes. So we can say the properties of an entity are the attributes. 

Let's represent this using a diagram.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/attributes-2.png)

The entity in the diagram above has three attributes – username, age, and email. 

Now you have a clearer picture of what an entity is and its attributes. 

If you still find this confusing, the entity above is called "User". The entity has three properties (username, age, and email) which are referred to as the entity's attributes.

## Relationship Between Entities in ERDs

In the previous sections, we talked about entities and their attributes. In most cases, databases are made up of more than one entity. 

To understand the relationship between one entity and another, we use lines to connect them. But these lines have notations (indicators) on them to specify the type of relationship that exists between two entities. 

We'll use crow's foot notation to specify our entity relationships. 

### Symbols in Crow’s Foot Notation and Their Meaning

Before we see diagrams of the symbols associated with crow's foot notation, we need to discuss a key term in crow's foot notation. 

One of the most important terms to know when using crow's foot notation is **cardinality**.

**Cardinality** acts as a parameter for the relationship between entities. For one entity, there is a minimum and maximum number that helps define its relationship with another entity. 

Don't worry if these explanations seem confusing. As we go further, you'll understand them perfectly. 

Here are the symbols associated with the crow's foot notation:

#### Zero

![Image](https://www.freecodecamp.org/news/content/images/2022/06/zero-crow.png)

The symbol/diagram above denotes zero in crow's foot notation. We know this because the of the zero/circle indicator at the right side of the horizontal line. 

#### One

![Image](https://www.freecodecamp.org/news/content/images/2022/06/one-crow.png)

The diagram above shows a horizontal line with a short vertical lines crossing it. The vertical line acts as the indicator – it denotes one.

#### Many

![Image](https://www.freecodecamp.org/news/content/images/2022/06/crows-crows-foot.png)

The diagram above denotes many. You can easily remember this symbol because it looks like a crow's foot. 

The three diagrams above are the basic representation of indicators in crow's foot notation. But in most cases, these indicators are combined to fully understand the relationship between entities. 

By the time we start looking at some practical examples, you'd understand the meaning of these symbols better. 

Before that, let's take a look at more diagrams and what they mean. We won't be introducing anything new – just a combination of the diagrams above. 

#### Zero or Many

![Image](https://www.freecodecamp.org/news/content/images/2022/06/zero-and-many-crow.png)

As can be seen above, the **zero or many** symbol/indicator in crow's foot notation is a combination of the zero and many indicators.

#### One or Many

![Image](https://www.freecodecamp.org/news/content/images/2022/06/one-and-many-crow.png)

 As expected, the **one or many** indicator is a combination of two indicators – one and many. 

#### One and only one

![Image](https://www.freecodecamp.org/news/content/images/2022/06/one-and-one-crow.png)

The **one and only one** indicator has two "one" indicators. In our examples in the next section, you'll understand its use better. 

## How to Use Crow’s Foot Notation in Entity Relationship Diagrams

In the last section, we focused on crow's foot notation diagrams and what they mean. They serve as indicators that explain the relationship between one entity and another. 

In this section, we'll dive in and look at some practical examples – this will help you fully understand how to use the crow's foot notation. 

If you have been following along from the previous sections, then some aspects of the diagrams we'll use in this section should be clear to you. 

### Crow's Foot Notation Example #1

In this example, we'll start with an assumption, create entities and denote their relationship using crow's foot notation. 

We'll break this example into steps with diagrams leading to the final sketch. 

##### Step #1 - Our Assumption and Entities

Let's assume we have two entities in our database. A teacher and course entity. Here's a representation of that:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/teacher-course-crow.png)

##### Step #2 - Relationship of the Teacher Entity and the Course Entity

Since we're the ones creating this model of the database, we get to set the rules! So for every teacher, they can only teach one course. 

We'll assume this is a platform where users are taught programming languages. Each teacher can only teach one programming language.

The notation here will be **one and only one**. The notation will be placed on the right side of the horizontal line. 

Here's an entity relationship diagram for that:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/teacher-course-crow2.png)

Remember when we talked about **cardinality**? Well, this is the perfect place to see it in practice. The minimum number of courses a teacher can take up is one, and the maximum is also one. 

##### Step #3 - Relationship of the Course Entity and the Teacher Entity

For each course, we want to have one or many teachers to choose from – meaning that one course can be taught by one or many teachers. The minimum here will be one while the maximum will be many. 

So the user can have one or many JavaScript teachers to learn from, one or many Python teachers to learn from, and so on. 

The notation to be used is **one or many**. The notation will be placed on the left side of the horizontal line.

Here is the ERD:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/teacher-course-crow3.png)

### Crow's Foot Notation Example #2

The notations don't always have to be different. What matters is the logic behind the relationship between entities. This is entirely up to the those creating or designing the database.

Have a look at the diagram below.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/crows-foot-example.png)

We have two entities – Customer and Pizza. These entities are linked together by a horizontal line with symbols/indicators/notations.

Let's begin with the notation on the left. It has the **zero or many** notation. This implies that a pizza can be ordered by none (optional) or many customers. 

Similarly, the notation on the right side implies that a customer can order **zero or many** pizzas. 

The **cardinality** here is the same for both entities. Zero is the minimum while many is the maximum. 

The use cases for other crow's foot notation diagrams are the same as the ones in our examples. It all depends on the logic and what you're designing.

## Conclusion

This tutorial serves as an introduction to understanding entity relationship diagrams and crow's foot notation for database design. 

We can use entity relationship diagrams to create a database model, or create a graphical representation of a database with the various entities that make up the database. This makes it easier to understand how each entity associates with another.

Notation makes it easier to understand the relationships between entities. In our case, we used crow's foot notation.

We began by explaining some key terminologies associated with entity relationship diagrams and crow's foot notation like entities, attributes, cardinality, and the meaning of the various crow's foot notation diagrams.

We then saw some examples to help understand the application of the crow's foot notation diagrams in defining the relationship between entities in an entity relationship diagram.

The examples used are very basic, but this isn't always the case when working on an actual database. Having a good understanding of the basic diagrams and their meaning will help you understand much more complex designs.

Thank you for reading!

