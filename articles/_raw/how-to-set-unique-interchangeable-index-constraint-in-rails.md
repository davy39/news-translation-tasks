---
title: 'Rails: How to set unique interchangeable index constraint'
subtitle: ''
author: Saheed Oladele
co_authors: []
series: null
date: '2019-07-15T10:50:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-unique-interchangeable-index-constraint-in-rails
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca178740569d1a4ca4ec3.jpg
tags:
- name: database
  slug: database
- name: postgres
  slug: postgres
- name: Ruby on Rails
  slug: ruby-on-rails
seo_title: null
seo_desc: Setting uniqueness validation in rails is something you’ll end up doing
  quite often. Perhaps, you even already added them to most of your apps. However,
  this validation only gives a good user interface and experience. It informs the
  user of the error...
---

Setting uniqueness validation in rails is something you’ll end up doing quite often. Perhaps, you even already added them to most of your apps. However, this validation only gives a good user interface and experience. It informs the user of the errors preventing the data from being persisted in the database.

### Why uniqueness validation is not enough

Even with the uniqueness validation, unwanted data sometimes gets saved in the database. For clarity, let’s take a look at a user model shown below:

```ruby
class User
    validates :username, presence: true, uniqueness: true
end
```

To validate the username column, rails queries the database using SELECT to see if the username already exists. If it does, it prints “Username already exists”. If it doesn’t, it runs an INSERT query to persist the new username in the database.  


![Image](https://lh5.googleusercontent.com/BXp1jq7tCUcP9meYKOz4G8fL_2hcEKK5roipT6sH7wugLhIizTFov8q37QTDTF0mNJtgI0QQm8vbrXaKq9JIQVq1hzcnBYYDr_Fy2KO6mEAR4fBfJy9uWoJ3VUu_JNxUYa0_ELfm)

  
When two users are running the same process at the same time, the database can sometimes save the data regardless of the validation constraint and that is where the database constraints (unique index) comes in.

If user A and user B are both trying to persist the same username into the database at the same time, rails runs the SELECT query, if the username already exists, it informs both users. However, if the username doesn’t exist in the database, it runs the INSERT query for both users simultaneously as shown in the image below.

![Image](https://lh3.googleusercontent.com/8-B6arsNFfdkLSkZbYt3F2KPPaFEbjAolPeDU9j3jMw3twF7r44uCum8dGNPGCduaLcX1E4n5QUTF4YUzPrPMI_QHyajoma8ULLyWo1aSYM5CJgu-1NEc3PDIuSpUFQvISE4Pu4y)

  
Now that you know why the database unique index (database constraint) is important, let’s get into how to set it. It’s quite easy to set database unique index(es) for any column or set of columns in rails. However, some database constraint in rails can be tricky.

### A quick look at setting a unique index for one or more column

This is quite as simple as running a migration. Let’s assume we have a users table with column username and we want to ensure that each user has a unique username. You simply create a migration and input the following code:

```ruby
add_index :users, :username, unique: true
```

Then you run the migration and that’s it. The database now ensures that no similar usernames are saved in the table.

For multiple associated columns, let’s assume we have a requests table with columns sender_id and receiver_id. Similarly, you simply create a migration and input the following code:

```ruby
add_index :requests, [:sender_id, :receiver_id], unique: true
```

And that’s it? _Uh oh, not so fast._

### The problem with the multiple column migration above

The problem is that the ids, in this case, are interchangeable. This means that if you have a sender_id of 1 and receiver_id of 2, the request table can still save a sender_id of 2 and receiver_id of 1, even though they already have a pending request.

This problem often happens in a self-referential association. This means both the sender and receiver are users and sender_id or receiver_id is referenced from the user_id. A user with user_id(sender_id) of 1 sends a request to a user with user_id(receiver_id) of 2.

If the receiver sends another request again, and we allow it to save in the database, then we have two similar requests from the same two users(sender and receiver || receiver and sender) in the request table.

This is illustrated in the image below:

![Image](https://lh3.googleusercontent.com/9VNqmd8nuvhxKqJ3nVoZKS5ke1y5K-m6wQ7N5r8NPLSFYUnv3yeoMH2afGj89sGtsEhk3zsJbI30pB2WsgOOF1Xiijtqmv3mqbi1PxDzkIoQM0sfXGLZjcSTRrrIUTamG9RqGzEM)

### The common fix

This problem is often fixed with the pseudo-code below:

```ruby
def force_record_conflict
    # 1. Return if there is an already existing request from the sender to receiver 
    # 2. If not then swap the sender and receiver
end
```

The problem with this solution is that the receiver_id and sender_id get swapped each time before saving to the database. Hence, the receiver_id column will have to save the sender_id and vice versa.

For example, if a user with sender_id of 1 sends a request to a user with receiver_id of 2, the request table will be as shown below:

![Image](https://lh3.googleusercontent.com/FhGRXh1uZOdxMsL1CvfKsM82kazpp_smHl7LkxNHpoxCxX6sChTbve5lQAotyW0WsqEITf7Ddc3C2XYG2-wwppSW4glymJqgPu4JmbiU1uxXR52c7EvWft73UHGf5-1gfmNW4ziC)

  
This may not sound like an issue but it’s better if your columns are saving the exact data you want them to save. This has numerous advantages. For example, if you need to send a notification to the receiver through the receiver_id, then you’ll query the database for the exact id from the receiver_id column. This already became more confusing the moment you start switching the data saved in your request table.

### The proper fix

This problem can be entirely resolved by talking to the database directly. In this case, I’ll explain using PostgreSQL. When running the migration, you must ensure that the unique constraint checks for both (1,2) and (2,1) in the request table before saving.

You can do that by running a migration with the code below:

```ruby
class AddInterchangableUniqueIndexToRequests < ActiveRecord::Migration[5.2]
    def change
        reversible do |dir|
            dir.up do
                connection.execute(%q(
                    create unique index index_requests_on_interchangable_sender_id_and_receiver_id on requests(greatest(sender_id,receiver_id), least(sender_id,receiver_id));
                    create unique index index_requests_on_interchangable_receiver_id_and_sender_id on requests(least(sender_id,receiver_id), greatest(sender_id,receiver_id));
                ))
            end

            dir.down do
                connection.execute(%q(
                    drop index index_requests_on_interchangable_sender_id_and_receiver_id;
                    drop index index_requests_on_interchangable_receiver_id_and_sender_id;
                ))
            end    
        end
    end
end
```

### Code explanation

After creating the migration file, the reversible is to ensure that we can revert our database whenever we must. The `dir.up` is the code to run when we migrate our database and `dir.down` will run when we migrate down or revert our database.

`connection.execute(%q(...))` is to tell rails that our code is PostgreSQL. This helps rails to run our code as PostgreSQL.

Since our “ids” are integers, before saving into the database, we check if the greatest and least (2 and 1) are already in the database using the code below:

```ruby
requests(greatest(sender_id,receiver_id), least(sender_id,receiver_id))
```

Then we also check if the least and greatest (1 and 2) are in the database using:

```ruby
requests(least(sender_id,receiver_id), greatest(sender_id,receiver_id)) 
```

The request table will then be exactly how we intend as shown in the image below:

![Image](https://lh5.googleusercontent.com/LHiuQRNBeyui8vuXx1hMWZfzVOBBkccmnFUml2A4kehPHg1xcpC35LsRan_8oggdmYH0zvBardwpIXHWDA-hiFTH4Grd7D6tejAATSJZLpS0l1aLig00KD8NUx7yrtTmICD1C0tI)

And that’s it. Happy coding!

### References:

[Edgeguides](https://edgeguides.rubyonrails.org/active_record_validations.html#uniqueness) | [Thoughtbot](https://thoughtbot.com/blog/the-perils-of-uniqueness-validations)

