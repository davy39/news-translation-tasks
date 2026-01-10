---
title: How I Contributed to a Major Open Source Project Without Writing Any Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-12T18:48:35.000Z'
originalURL: https://freecodecamp.org/news/open-source-continuous-integration
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-12-at-9.56.22-AM.png
tags:
- name: community
  slug: community
- name: Continuous Integration
  slug: continuous-integration
- name: open source
  slug: open-source
- name: Phoenix framework
  slug: phoenix
seo_title: null
seo_desc: 'By Adam Gordon Bell

  I recently got a pull request merged into the popular Phoenix Framework, and I did
  it without writing any Elixir code. I didn''t write any documentation either. What
  I did was help improve the build process.

  In this post, I''d like ...'
---

By Adam Gordon Bell

I recently got a pull request merged into the popular Phoenix Framework, and I did it without writing any Elixir code. I didn't write any documentation either. What I did was help improve the build process.

In this post, I'd like to share the improvements I made to their build process. These improvements are not Phoenix Framework-specific and they might change the way you approach continuous integration.

But first, some background.

## What is the Phoenix Framework?

Phoenix is a web framework with some very interesting properties. With Phoenix, you can build rich interactive web applications without writing client-side code. 

You can do this using a feature called LiveView which sends real-time updates from the server to update the client browser's HTML.

We can create a page that shows the latest tweets on a topic, in real-time, quite easily.

Here is an example:

```elixir
defmodule TimelineLive do
  use Phoenix.LiveView

  def render(assigns) do
    render("timeline.html", assigns)
  end

  def mount(_, socket) do
    Twitter.subscribe("elixirphoenix")
    {:ok, assign(socket, :tweets, [])}
  end

  def handle_info({:new, tweet}, socket) do
    {:noreply,
     update(socket, :tweets, fn tweets ->
       Enum.take([tweet | tweets], 10)
     end)}
  end
end

```

![Image](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FCorecursive%2FDUy3Kzmdsn.png?alt=media&token=edf6aee0-7744-435e-9e3f-0557e000214e)
_Real-Time Twitter Results with No Javascript Written_

The framework is written in the programming language Elixir

It was created by José Valim. It looks a lot like Ruby but has very different semantics. Elixir runs on the Erlang VM, and it powers projects like Discord and is used at companies like Heroku.

## How to Reproduce the Builds

The Phoenix Framework uses GitHub Actions for their build pipeline. Like many great projects, they have a suite of unit tests that they need to run on every user contribution. 

This isn't where their testing efforts stop though. They also have a suite of integration tests. Phoenix uses an ORM to talk to various databases and the integration tests ensure that no changes break the integration with any of the 3 supported databases.

This is a common pattern. Having a large number of unit tests that are easy to run and well as a handful of slower but more comprehensive integration tests is a great way to prevent bugs from being introduced into the project.

The Phoenix Framework takes this even further, though, as they also need to support several versions of the Elixir language and a handful of versions of Open Telecom Platform (OTP).

This is starting to sound complex. We have to test each change with all combinations of the following:

* Databases (Postgres, MySQL MSSQL)
* Elixir (Current and Previous Version)
* OTP (Current and Previous Version)

It's relatively easy to set this up in GitHub Actions, but how would you run these tests locally? 

Installing all these would be a lot to ask, so contributors tend to rely on GitHubActions to test these combinations. However, if everyone has to rely on pushing things to GitHub it see if the tests pass then development gets slower.

How do we fix this?

## How to Unify the Test Runs

This is where I got involved. I work at Earthly Technologies as an open-source developer advocate. We have a pretty cool open-source build tool, and although I occasionally contribute directly to the project my job is to be the contact point between the community using the tool and the team working on it.

I had heard about this reproducibility problem the Phoenix team was having. I thought I could help write a build script that could be used both in GitHub Actions and for a local development workflow. So I set to work on a PR.

### Running The Tests Locally

What I ended up creating, slightly simplified, is this:

```dockerfile
setup:
   ARG ELIXIR=1.10.4
   ARG OTP=23.0.3
   # Pull a Docker Image to Run Build Inside Of
   FROM hexpm/elixir:$ELIXIR-erlang-$OTP-alpine-3.12.0
   ...
 
integration-test:
    FROM +setup
    COPY . .
    # Pull In Dependencies
    RUN mix deps.get 
    # Start Up Service Dependencies
    WITH DOCKER --compose docker-compose.yml 
        # Run Tests
        RUN mix test --include database 
    # Stop Service Dependencies
    END


```

This is an Earthfile. Its made up of several targets, like `setup` and `integration-test`. The targets can have dependencies between them.  You can use the command-line tool `earthly` to run any target and each is run in a Docker container.  Containerization is going allow us to run the build wherever we choose.

This example runs the `integration-test` inside of a the `hexpm/elixir` Docker container with the specified version of Elixir and OTP installed.

Before running the tests with  `mix test --include database`, we use Docker compose to start up all the needed dependencies:

```dockerfile
 WITH DOCKER --compose docker-compose.yml
        RUN mix test --include database
 END 

```

The Docker compose file looks like this:

```yaml
version: '3'
services:
  postgres:
    image: postgres
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: postgres
  mysql:
    image: mysql
    ports:
      - "3306:3306"
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: "yes"
  mssql:
    image: mcr.microsoft.com/mssql/server:2019-latest
    environment:
      ACCEPT_EULA: Y
      SA_PASSWORD: some!Password
    ports:
      - "1433:1433"	

```

These are the databases we need for testing Phoenix.

Now we can run the integration tests at the command line like so:

```
>  earthly -P +integration-test

```

And if we want to test a different version of Elixir, we can specify the version as build arguments:

```
 > earthly -P --build-arg ELIXIR=1.11.0 --build-arg OTP=23.1.1 +integration-test

```

There are other ways to accomplish this. A combination of a makefile and dockerfiles would have worked as well. The key is to get the build logic out of a GHA specific format and into something that be run can anywhere.

## How to Run it in GitHub Actions

To use this same process inside GitHub Actions, the only thing we need to do is adjust our GitHub Actions yaml to use Earthly for the build pipeline and we are all set.

```javascript
  integration-test-elixir:
    runs-on: ubuntu-latest
    env:
      FORCE_COLOR: 1
    
    strategy:
      fail-fast: false
      matrix:
        include:
          - elixir: 1.11.1
            otp: 21.3.8.18
          - elixir: 1.11.1
            otp: 23.1.1
    steps:
      - uses: actions/checkout@v2
      - name: Download released earth
        run: "sudo /bin/sh -c 'wget https://github.com/earthly/earthly/releases/download/v0.4.1/earthly-linux-amd64 -O /usr/local/bin/earthly && chmod +x /usr/local/bin/earthly'"
      - name: Execute tests
        run: earthly -P --build-arg ELIXIR=${{ matrix.elixir }}  --build-arg OTP=${{ matrix.otp }} +integration-test

```

There we go, we are now able to run our build pipeline locally, without any complex environment setup. We can also run the same build process on our developer machine without needing to install anything except Earthly. This makes it easier for new contributors to approach the project.

## The End Result

Eventually, with help from the Phoenix Team, I got this change approved and the Phoenix project now has an easy way to test and iterate on their build pipeline locally. And I didn't even write any Elixir code! You can find more details in the [PR](https://github.com/phoenixframework/phoenix/pull/4072).

Thank you for reading this article.  If you'd like to learn more about Earthly, [you can find out a lot here](http://earthly.dev/). And if you'd like my help on your open source project's build, let me know.

