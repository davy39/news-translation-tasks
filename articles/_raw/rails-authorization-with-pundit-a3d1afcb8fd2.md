---
title: Rails Authorization with Pundit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-25T22:41:33.000Z'
originalURL: https://freecodecamp.org/news/rails-authorization-with-pundit-a3d1afcb8fd2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb6e0740569d1a4cae0a6.jpg
tags:
- name: General Programming
  slug: programming
- name: Rails
  slug: rails
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Joseph Gefroh

  Pundit is a Ruby gem that handles authorization via a very simple API.

  Remember that authorization is different from authentication — authentication is
  verifying that you are who you say you are, and authorization is verifying that
  y...'
---

By Joseph Gefroh

[Pundit](https://github.com/elabs/pundit) is a Ruby gem that handles authorization via a very simple API.

Remember that authorization is different from authentication — authentication is verifying that you are who you say you are, and authorization is verifying that you have permission to perform an action.

Pundit is squarely within the authorization camp — use another authentication system like [Devise](https://github.com/plataformatec/devise) to handle authentication.

### How you work with Pundit

**Step 1:** You create a `Policy` class that deals with authorizing access to a specific type of record — whether it be a `Blog` or `Potato` or `User`.

**Step 2:** You call the built-in `authorize` function, passing in what you’re trying to authorize access to.

**Step 3:** Pundit will find the appropriate `Policy` class and call the `Policy` method that matches the name of the method you are authorizing. If it returns true, you have permission to perform the action. If not, it’ll throw an exception.

It’s pretty straightforward. Logic for specific models is encapsulated into its own policy class, which is great for keeping things tidy. Competing authorization library [cancancan](https://github.com/CanCanCommunity/cancancan) had issues with complicated permissions getting out of hand.

### Minor tweaks required

Pundit’s simple conventions sometimes need to be tweaked to support more complex authorization use cases.

#### Access more information from within a Policy

By default, Pundit provides two objects to your authorization context: the `User` and the `Record` being authorized. This is sufficient if you have system-wide roles in your system like `Admin` or `Moderator`, but isn’t enough when you need authorize to a more specific context.

Let’s say you had a system that supported the concept of an `Organization`, and you had to support different roles within those organizations. System-wide authorization won’t cut it — you don’t want an admin of Organization Potato to be able to do things to Organization Orange unless they are an admin of both organizations. When authorizing this case, you would need access to 3 items: the `User`, the `Record`, and the user’s role information in the `Organization`. The ideal case would be to have access to the organization the record belongs to, but let’s make it harder and say we don’t have access to that via the record or the user.

Pundit provides an opportunity to provide additional context. By defining a function called `pundit_user`, this allows you to change what is considered a `user`. If you return a object with the authorization context from that function, that context will be available to your policies.

`application_controller.rb`

```
class ApplicationController < ActionController::Base  include Pundit
```

```
  def pundit_user    AuthorizationContext.new(current_user, current_organization)  endend
```

`authorization_context.rb`

```
class AuthorizationContext  attr_reader :user, :organization
```

```
  def initialize(user, organization)    @user = user    @organization = organization  endend
```

`application_policy.rb`

```
class ApplicationPolicy  attr_reader :request_organization, :user, :record
```

```
  def initialize(authorization_context, record)    @user = authorization_context.user    @organization = authorization_context.organization    @record = record  end
```

```
  def index?    # Your policy has access to @user, @organization, and @record.    endend
```

Your policies would now have access to all three kinds of information — you should be able to see how you would access more information if you needed it.

#### Override convention and specify which Policy to use

Pundit uses naming conventions to match up what you’re trying to authorize with the right policy. Most of the time this works well, but in certain cases you may need to override this convention, such as when you want to authorize a general dashboard action that doesn’t have an associated model. You can pass in symbols to specify which action or policy to use for authorization:

```
#Below will call DashboardPolicy#bake_potato?authorize(:dashboard, :bake_potato?)
```

If you have a model that is named differently, you can also override the `policy_class` function within the model itself:

```
class DashboardForAdmins  def self.policy_class   DashboardPolicy     # This forces Pundit to use Dashboard Policy instead of looking    # for DashboardForAdminsPolicy  endend
```

### Testing

Authorization is one of those things I strong recommend having an automated test suite around. Setting them up incorrectly can be catastrophic, and it’s in my opinion one of the most tedious things to test manually. Being able to run a single command and knowing that you haven’t inadvertently changed any authorization business rules is a great feeling.

Pundit makes testing authorization very simple.

```
def test_user_cant_destroy?  assert_raises Pundit::NotAuthorizedError do    authorize @record, :destroy?  endend
```

```
def test_user_can_show?  authorize @record, :show?end
```

Overall I like Pundit. I’ve only been using it for a short while, but I already prefer it over cancancan — it just feels more maintainable and testable.

Did you find this story helpful? Please **Clap** to show your support!  
If you didn’t find it helpful, please let me know why with a **Comment**!

