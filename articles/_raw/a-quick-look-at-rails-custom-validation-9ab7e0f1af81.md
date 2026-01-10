---
title: A quick look at Rails Custom Validation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-08T16:33:30.000Z'
originalURL: https://freecodecamp.org/news/a-quick-look-at-rails-custom-validation-9ab7e0f1af81
coverImage: https://cdn-media-1.freecodecamp.org/images/1*otuQiVYDCBjZee9xZ0UnvA.jpeg
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Raymond Blessed

  I recently started working with Ruby (almost 2 months now) and Ruby on Rails (a
  little over 3 weeks). Working with Rails’ Active Record framework is one of my favorite
  things about Ruby on Rails. In this post, we will be looking at...'
---

By Raymond Blessed

I recently started working with Ruby (almost 2 months now) and Ruby on Rails (a little over 3 weeks). Working with Rails’ Active Record framework is one of my favorite things about Ruby on Rails. In this post, we will be looking at validations in Active Record, custom ones particularly. Here is a quick intro to Active Record before we move to the good stuff.

Active Record is one of the core gems that make up Ruby on Rails. It is the part of the framework that deals with databases.

It is an ORM (Object Relational Mapping) framework that lets you build a schema for a database using pure ruby and it is based on the Active Record design pattern described by [Martin Fowler](https://martinfowler.com/). So, with Active Records, you are creating your DB, creating tables, storing, retrieving and deleting data using ruby which translates to SQL under the hood.

### Quick Intro

Suppose we have a student model with properties first name and last name. To use Active Record we just need to extend the **ApplicationRecord** and when we run `rails db:migrate` it gives us the SQL statement for it.

To interact with the database, we use methods inherited from the ApplicationRecord superclass.

It also supports associations and other database stuff.

For a detailed intro to Active Record, check out the official ruby on rails guide.

### Validation

Because we write web applications for users other than ourselves, we cannot be sure that the users will always input valid data into the database. To enforce this, Active Record provides us a mini-validation framework that ensures the presence of data, uniqueness of certain fields, and so on.

Let’s look at our students table above. We wouldn’t want to create a user without a first name or last name which presently is possible. To mitigate this, we just need to modify our Student class like so:

With this modification, when you create a Student instance without the first name or last name attributes, it is an invalid student and active records will not persist it to the database.

Active record also provides us with methods to check if our data is valid or invalid:

With this, we do not even have to attempt to save the data.

Apart from just preventing the data from being persisted, Active Record also provides an error list that holds the attributes that failed validations and user-friendly messages to present to the users. These errors can be accessed as shown in the snippet below.

There is a lot more on validation but it’s not the topic of this article. For a deep dive, you can get an in-depth explanation from the ruby on rails guide chapter on Validation.

### Custom Validation

Sometimes, we might want to use certain validations that are more than just ensuring the presence of an attribute, length, uniqueness, or any of the helpers provided by Active Record. Luckily, Active Record allows us to define our own custom validations, which is the point of this article.

So, let’s say for our Student model, we have a compulsory student registration number column. It has to be filled from the registration form (I know this can be auto-generated) which should always start with the registration year. Now, Active Record does not provide this kind of validation out of the box, but has made it possible for us to define it and use it.

There are mainly two ways to define your own validation logic:

* Custom Validator
* Custom Methods

#### **Custom Validator**

To validate using a custom validator, you just need to define your validation logic in a class that extends **ActiveModel::Validator** and implements the validate method, which takes the record to be validated as its argument.

If validation fails, it adds the attribute to the errors array along with its error message. So, in our case, we’ll have RegNumValidator as seen below:

To use this validator in the Student model, we use the `validates_with` method:

With this, when a user tries to create a student with the wrong registration number, the record creation fails and an error message can be shown.

#### **Custom Methods**

To use custom methods for validation, you just need to define a method to use for validation in your model class and call it like you would call any of the in-built validations — using `validate`. Using the same logic as what we had above, our model would look like this:

### Conclusion

I hope this article has given you the necessary knowledge to begin to explore Active Records validation and custom validation especially. Whenever you have a validation rule that is not part of the existing active record validation API, you can write one yourself.

[**Active Record Validations — Ruby on Rails Guides**](https://guides.rubyonrails.org/active_record_validations.html)  
[_Validations are used to ensure that only valid data is saved into your database. For example, it may be important to…_guides.rubyonrails.org](https://guides.rubyonrails.org/active_record_validations.html)

