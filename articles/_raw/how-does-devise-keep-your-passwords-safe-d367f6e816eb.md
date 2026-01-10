---
title: How Devise keeps your Rails app passwords safe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-15T10:45:18.000Z'
originalURL: https://freecodecamp.org/news/how-does-devise-keep-your-passwords-safe-d367f6e816eb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iOXaisZyDdgXEPpwHaFrRQ.jpeg
tags:
- name: Cryptography
  slug: cryptography
- name: Ruby on Rails
  slug: ruby-on-rails
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Tiago Alves

  Devise is an incredible authentication solution for Rails with more than 40 million
  downloads. However, since it abstracts most of the cryptographic operations, it’s
  not always easy to understand what’s happening behind the scenes.

  One...'
---

By Tiago Alves

[Devise](https://github.com/plataformatec/devise) is an incredible authentication solution for Rails with [more than 40 million downloads](https://rubygems.org/gems/devise). However, since it abstracts most of the cryptographic operations, it’s not always easy to understand what’s happening behind the scenes.

One of those abstractions culminates in the persistence of an `encrypted_password` directly on the database. So I’ve always been curious about what it actually represents. Here’s an example:

`$2a$11$yMMbLgN9uY6J3LhorfU9iuLAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO`

But what does that gibberish mean?

Devise uses [Bcrypt](https://github.com/codahale/bcrypt-ruby) to securely store information. On its website it mentions that it uses “_OpenBSD bcrypt() password hashing algorithm, allowing you to easily store a secure hash of your users’ passwords_”. But what exactly is this hash? How does it work and how does it keep stored passwords safe?

That’s what I want to show you today.

Let’s work backwards — from the stored hash on your database to the encryption and decryption process.

That hash `$2a$11$yMMbLgN9uY6J3LhorfU9iuLAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO` is actually comprised of several components:

* **Bcrypt version** (`2a`) - the version of the bcrypt() algorithm used to produce this hash (stored after the first `$` sign)
* **Cost** (`11`) - the cost factor used to create the hash (stored after the second `$` sign)
* **Salt** (`$2a$11$yMMbLgN9uY6J3LhorfU9iu`) - a random string that when combined with your password makes it unique (first 29 characters)
* **Checksum** (`LAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO`) - the actual hash portion of the stored `encrypted_password` (remaining string after the 29 chars)

![Image](https://cdn-media-1.freecodecamp.org/images/C1o8LTw8UCfepc7Tq3m5Yd1VGcMcT4XpRkBD)

Let’s explore the last 3 parameters:

* When using Devise, the `**Cost**` value is set by a class variable called [stretches](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/lib/devise.rb#L74) and the default value is `11`. It specifies the number of times the password is hashed. (_On your [devise.rb initializer](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/test/rails_app/config/initializers/devise.rb#L70), you can configure this to a lower value for the test environment to make your test suite run faster._) *
* The **salt** is the random string used to combine with the original password. This is what makes the same password have different values when stored encrypted. (_See more below about why that matters and what are Rainbow Table Attack_s.) **
* The **checksum** is the actual generated hash of the password after being combined with the random salt.

When a user registers on your app, they must set a password. Before this password is stored in the database, a random salt is generated via [BCrypt::Engine.generate_salt(cost)](https://www.rubydoc.info/github/codahale/bcrypt-ruby/BCrypt%2FEngine.generate_salt) by taking into account the cost factor previously mentioned. _(Note: if the `[pepper](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/lib/devise.rb#L155)` [class variable value](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/lib/devise.rb#L155) is set it will [append its value to the password](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/lib/devise/encryptor.rb#L9) before salting it.)_

With that salt (ex. `$2a$11$yMMbLgN9uY6J3LhorfU9iu`, which includes the cost factor) it will call [BCrypt::Engine.hash_secret(password, salt)](https://www.rubydoc.info/github/codahale/bcrypt-ruby/BCrypt%2FEngine.hash_secret) that computes the final hash to be stored using the generated salt and the password selected by the user. This final hash (for example, `$2a$11$yMMbLgN9uY6J3LhorfU9iuLAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO`) will in turn be stored in the `encrypted_password` column of the database.

![Image](https://cdn-media-1.freecodecamp.org/images/mKgk9fAildsnwkuXhmOU0SDIiflG-nI8FPUa)

But if this hash is nonreversible and the salt is randomly generated on the `BCrypt::Password.create` call by `BCrypt::Engine.generate_salt(cost)`, **how can it be used to sign in the user?**

That’s where those different hash components are useful. After finding the record that matches the email supplied by the user to sign in, the encrypted password is retrieved and broken down into the different components mentioned above (**Bcrypt version**, **Cost**, **Salt** and **Checksum**).

After this initial preparation, here’s what happens next:

1. Fetch the **input password** (`1234`)
2. Fetch the **salt** of the stored password (`$2a$11$yMMbLgN9uY6J3LhorfU9iu`)
3. Generate the **hash** from the password and salt using the same bcrypt version and cost factor (`BCrypt::Engine.hash_secret(“1234”, “$2a$11$yMMbLgN9uY6J3LhorfU9iu”)`)
4. Check if the **stored hash** is the same one as the computed on step 3 (`$2a$11$yMMbLgN9uY6J3LhorfU9iuLAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO`)

![Image](https://cdn-media-1.freecodecamp.org/images/kJxy3TSK0VJ3fVqfFcVjmCCPCdgm1HyBb9C8)

And that’s how Devise stores passwords securely and protects you from a range of attacks even if your database is compromised.

Get in touch on Twitter [@alvesjtiago](https://twitter.com/alvesjtiago) and let me know if you found this article interesting! Thank you for reading.

![Image](https://cdn-media-1.freecodecamp.org/images/Lo-yU9BkzXFiqwgk5JS4RAKntUaE4KffvT5-)

> PS: I’m by no means a security or cryptography expert so please do reach out if you find something wrong. I’m hoping that by simplifying some of the concepts it will be easier to understand what’s happening.

_Thank you [@filipepina](https://twitter.com/filipepina), [@ivobenedito](https://twitter.com/ivobenedito), [@jackveiga](https://twitter.com/jackveiga), [@joao_mags](https://twitter.com/joao_mags) and [@pedrosmmoreira](https://twitter.com/pedrosmmoreira) for the reviews and suggestions. This article is also available at [http://blog.tiagoalves.me/how-does-devise-keep-your-passwords-safe](http://blog.tiagoalves.me/how-does-devise-keep-your-passwords-safe/)._

More information about some of the topics.

**Cost factor ***

* [Perils of the default bcrypt cost factor](https://labs.clio.com/bcrypt-cost-factor-4ca0a9b03966)
* [Recommended number of rounds for bcrypt](https://security.stackexchange.com/questions/17207/recommended-of-rounds-for-bcrypt)

**Rainbow Table Attacks ****

* [Rainbow table — Wikipedia](https://en.wikipedia.org/wiki/Rainbow_table)
* [What are rainbow tables and how are they used?](https://security.stackexchange.com/a/440)

