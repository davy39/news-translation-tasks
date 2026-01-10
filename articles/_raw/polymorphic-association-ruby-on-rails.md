---
title: How to Use Polymorphic Associations in Ruby on Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-26T18:40:39.000Z'
originalURL: https://freecodecamp.org/news/polymorphic-association-ruby-on-rails
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Add-a-subheading--2-.png
tags:
- name: Ruby on Rails
  slug: ruby-on-rails
seo_title: null
seo_desc: 'By Sampurna Chapagain

  Polymorphic association in Ruby on Rails refers to the type of active record association.
  From the Rails Guide, it allows a single model to belong to more than one other
  model on a single association.

  This tutorial assumes that ...'
---

By Sampurna Chapagain

Polymorphic association in Ruby on Rails refers to the type of active record association. From the [Rails Guide](https://guides.rubyonrails.org/association_basics.html#polymorphic-associations), it allows a single model to belong to more than one other model on a single association.

This tutorial assumes that you have some knowledge of a few associations in Rails like the `belongs_to`, `has_one`, and `has_many` associations. 

It is a slightly more advanced type of association but it's perfect when you want to connect a model to multiple other models.

## The Problem with Not Using Polymorphic Associations

Suppose you want to create an app with features like posts, a forum, and event functionality. 

In the initial stage of your app, you might plan to add a comment feature to just the posts model. But as your app grows, you might want to add a similar comment feature to the forum and event models as well (maybe for other models, too, along the line). 

Let's see how this would look in the picture below:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Comment--1-.jpg)
_Passing comments to posts, event, and forum models_

Every time you want to add something that has comments in the app, you have to add a foreign key to the comments table. You would end up writing lots of repetitive code in this process. 

This might not be a problem for small applications, but as your app grows this can be a huge issue. And this is where polymorphic associations come in super handy.

## How Polymorphic Associations Helps Solve This Problem

The solution to the above problem is to use polymorphic associations in Rails. This lets you define a single model which can belong to other different models without having to write repeated code.

Considering the above example, you do not have to add the foreign key to the comments table every time you have to add comments to other models.

With polymorphic associations, you can add just two columns in the comments table, which is very straightforward. Let's see how it works in the next section of this article. 

## How to Implement Polymorphic Associations

To create the new `PolyComment` model, we will be using the following command:

`rails g model PolyComment content:text commentable:references{polymorphic}`

Let's check the `PolyComment` model now:

``` ruby
class PolyComment < ApplicationRecord
  belongs_to :commentable, polymorphic: true
end


The migration file will look like this:

```ruby
class CreatePolyComments < ActiveRecord::Migration[6.1]
  def change
    create_table :poly_comments do |t|
      t.text :content
      t.references :commentable, polymorphic: true, null: false

      t.timestamps
    end
  end
end


Now, let's run the migration using the `rails db:migrate` command to update the `schema` which will have two additional interesting columns.

```ruby
create_table "poly_comments", force: :cascade do |t|
    t.text "content"
    t.string "commentable_type", null: false
    t.integer "commentable_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["commentable_type", "commentable_id"], name: "index_poly_comments_on_commentable"
  end

The columns `commentable_type` and `commentable_id` help setup the polymorphic associations.

`commentable_type` stores the name of models like `Event`, `Post`, or `Forum` in this case. And `commentable_id` stores the `id` that corresponds to that model.

Now, let's generate the three models with the following commands:

`rails g model Post title`

`rails g model Event title`

`rails g model Forum title`

Now, we need to add `has_many` relationships in these three models:

Post.rb
```ruby
class Post < ApplicationRecord
    has_many :poly_comments, as: :commentable
end

Event.rb
```ruby
class Event < ApplicationRecord
    has_many :poly_comments, as: :commentable
end


Forum.rb
```ruby
class Forum < ApplicationRecord
    has_many :poly_comments, as: :commentable
end


 You can add comments to as many models as you want based on the above logic.

### How to test it in the console

Now, let's play around with the console to test the results:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-from-2023-01-23-20-08-00.png)
_Creating new post_

Here, we have created a new Post.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-from-2023-01-23-20-08-25-3.png)
_Adding Comment to Post_

 Here, you can see that the value of `commentable_type` is `Post` (in the form of a string) since it is associated with the `Post` model. Also, the value of `commentable_id` is `1` since it matches the `id` of the respective object. 

This is how you can add comments for any models you want.

## Conclusion

Polymorphic associations make your code DRY (Don't repeat yourself) and bug-free. If you want to connect a model with multiple other models then the polymorphic associations will be a great choice. Using this approach, you do not have to define a separate association for each model.

If you liked this article, please consider [buying me a coffee](https://www.buymeacoffee.com/SamChapagain) ☕.

You can find me on [Twitter](https://twitter.com/saam_codes) for various content related to Web Development.

Happy Coding!






