---
title: How to optimize your queries to solve common scalability bottlenecks in Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-04T19:18:58.000Z'
originalURL: https://freecodecamp.org/news/n-1-queries-batch-loading-active-model-serializers-in-rails-72662d7736f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ph_m9KGrsfJPHGwpfXA8nQ.png
tags:
- name: Batch Loading
  slug: batch-loading
- name: General Programming
  slug: programming
- name: Rails
  slug: rails
- name: REST API
  slug: rest-api
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Usama Ashraf

  The (perfect) solution for the N+1 problem


  The n+1 query problem is one of the most common scalability bottlenecks. It involves
  fetching a list of resources from a database that includes other associated resources
  within them. This m...'
---

By Usama Ashraf

#### The (perfect) solution for the N+1 problem

![Image](https://cdn-media-1.freecodecamp.org/images/Csu1xKKjVyRarXO3zKOQi-PwvPuR750NjwYt)

The n+1 query problem is one of the most common scalability bottlenecks. It involves fetching a list of resources from a database that includes other associated resources within them. This means that we might have to query for the associated resources separately. So if you have a list of n parent objects, _another n queries will have to be executed for fetching the associated resources_. Let’s try to get rid of this O(n) conundrum.

If you’re comfortable with Rails, [Active Model Serializers](https://github.com/rails-api/active_model_serializers), and already have a good idea about what our problem is going to be, then maybe you can jump straight into the code [here](https://gist.github.com/UsamaAshraf/95b0c8d0d64ee193148342a931c0a423).

#### A Concrete Example

Say you’re fetching an array of **Post** objects at a GET endpoint. You also want to load the respective authors of the posts, embedding an **author** object within each of the post objects. Here’s a naive way of doing it:

```
class PostsController < ApplicationController    def index        posts = Post.all              render json: posts    endend
```

```
class Post  belongs_to :author, class_name: 'User'end
```

```
class PostSerializer < ActiveModel::Serializer    attributes :id, :title, :details
```

```
  belongs_to :author end
```

For each of the n **Post** objects being rendered, a query will run to fetch the corresponding **User** object. Hence we’ll run a total of n+1 queries. This is disastrous. And here’s how you fix it by eager loading the **User** object:

```
class PostsController < ApplicationController    def index        # Runs a SQL join with the users table.    posts = Post.includes(:author).all              render json: posts    endend
```

#### When A Simple Join Is Not Possible

Until now there’s been absolutely nothing new for veterans.

But let’s complicate this. _Let’s assume that the site’s users are not being stored in the same RDMS as the posts are. Rather, the users are documents stored in MongoDB (for whatever reason)._ How do we modify our **Post** serializer to fetch the user now, optimally? This would be going back to square one:

```
class PostSerializer < ActiveModel::Serializer    attributes :id, :title, :details, :author
```

```
  # Will run n Mongo queries for n posts being rendered.  def author    User.find(object.author_id)  endend
```

```
# This is now a Mongoid document, not an ActiveRecord model.class User    include Mongoid::Document    include Mongoid::Timestamps    # ...end
```

The predicament that our users now reside in a Mongo database can be substituted with, say, calling a 3rd party HTTP service for fetching the users or storing them in a completely different RDMS. _Our essential problem remains that there’s no way to ‘join’ the users datastore with the posts table and get the response we want in a single query._

Of course, we can do better. We can fetch the entire response in two queries:

* Fetch all the posts without the **author** attribute (1 SQL query).
* Fetch all the corresponding authors by running a where-in query with the user IDs plucked from the array of posts (1 Mongo query with an IN clause).

```
posts      = Post.allauthor_ids = posts.pluck(:author_id)authors    = User.where(:_id.in => author_ids)
```

```
# Somehow pass the author objects to the post serializer and# map them to the correct post objects. Can't imagine what # exactly that would look like, but probably not pretty.render json: posts, pass_some_parameter_maybe: authors
```

#### Enter Batch Loader

So our original optimization problem has been reduced to “how do we make this code readable and maintainable”. The folks at [Universe](https://www.universe.com/about) have come up with an absolute gem (too obvious?). [Batch Loader](https://github.com/exAspArk/batch-loader) has been incredibly helpful to me recently.

`gem 'batch-loader'`

`bundle install`

```
class PostSerializer < ActiveModel::Serializer    attributes :id, :title, :details, :author
```

```
  def author    object.get_author_lazily  endend
```

```
class Post  def get_author_lazily    # The current post object is added to the batch here,    # which is eventually processed when the block executes.       BatchLoader.for(self).batch do |posts, batch_loader|          
```

```
      author_ids = posts.pluck(:author_id)        User.where(:_id.in => author_ids).each do |user|        post = posts.detect { |p| p.author_id == user._id.to_s }        #'Assign' the user object to the right post.        batch_loader.call(post, user)            end        end    endend
```

If you’re familiar with JavaScript Promises, think of the `get_author_lazily` method as returning a Promise which is evaluated later. That’s a decent analogy, I think since `BatchLoader` uses [lazy Ruby objects](https://ruby-doc.org/core-2.4.1/Enumerable.html#method-i-lazy). By default, `BatchLoader` caches the loaded values, and so to keep the responses up-to-date you should add this to your `config/application.rb`:

```
config.middleware.use BatchLoader::Middleware
```

That’s it! We’ve solved an advanced version of the n+1 queries problem while keeping our code clean and using Active Model Serializers the right way.

#### Using AMS for Nested Resources

One problem though. If you have a **User** serializer (Active Model Serializers work with Mongoid as well), that _won’t_ be called for the lazily loaded **author** objects, unlike before. To fix this, we can use a Ruby block and serialize the **author** objects before they’re ‘assigned’ to the posts.

```
class PostSerializer < ActiveModel::Serializer    attributes :id, :title, :details, :author
```

```
  def author    object.get_author_lazily do |author|      # Serialize the author after it has been loaded.           ActiveModelSerializers::SerializableResource                             .new(author)                             .as_json[:user]    end  endend
```

```
class Post  def get_author_lazily    # The current post object is added to the batch here,    # which is eventually processed when the block executes.       BatchLoader.for(self).batch do |posts, batch_loader|
```

```
      author_ids = posts.pluck(:author_id)      User.where(:_id.in => author_ids).each do |user|        modified_user = block_given? ? yield(user) : user        post = posts.detect { |p| p.author_id == user._id.to_s }          # 'Assign' the user object to the right post.        batch_loader.call(post, modified_user)            end        end    endend
```

[Here’s](https://gist.github.com/UsamaAshraf/95b0c8d0d64ee193148342a931c0a423) the entire code. Enjoy!

