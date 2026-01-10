---
title: Want to know the easiest way to save time? Use `make`!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T22:05:17.000Z'
originalURL: https://freecodecamp.org/news/want-to-know-the-easiest-way-to-save-time-use-make-eec453adf7fe
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tag_5co_wBrmCdD3
tags:
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Piotr Gaczkowski

  People have always looked for ways to make their work easier. It is a matter of
  debate whether using tools and automation are distinct human features. Or do we
  share them with other species? The fact is that we try to outsource ou...'
---

By Piotr Gaczkowski

People have always looked for ways to make their work easier. It is a matter of debate whether using tools and automation are distinct human features. Or do we share them with other species? The fact is that we try to outsource our most mundane tasks to the machines. And that’s great!

### Why automate?

Repetition often leads to boredom and fatigue. Boredom is the first step toward burnout, while fatigue is one of the major sources of mistakes. Since we don’t want our colleagues (or ourselves) to burn out as much as we don’t want to make costly mistakes, we try to automate our everyday tasks.

There seems to be a proliferation of software dedicated to the automation of common tasks. In the Node.JS ecosystem alone, there are (or used to be) solutions like Bower, Yeoman, Grunt, Gulp, and NPM scripts.

But there is a good standard UNIX tool. By standard I mean it actually has robust documentation, that many forgot. Or never learned? I’m talking about `make`. More accurately, this article focuses on GNU make. It’s available on macOS, Windows, Linux and most other operating systems.

`make` is so standard you already have it installed. Type make in a command line and check yourself. This piece of software came out in 1977, which means it’s pretty much battle-tested. Is it quirky? Yup, even for the ’70s standard. But it does its job well and this is all we want from it.

### Isn’t Make for C/C++ code?

When you read about `make` you probably recall that there used to be such a tool to build C/C++ projects back then. It went like this `./configure && make && make install`. Yes, we are talking about exactly the same tool. And frankly, it’s not limited to compiling C/C++ code. To be honest, it can’t even compile the code.

Pretty much all `make` understands is files. It knows whether a file exists or not and which file is more recent. The other half of its power lies in maintaining a dependency graph. Not much, but those two features are what constitute its power.

In order for `make` to actually do anything, you write a set of recipes. Each recipe consists of a target, zero or more dependencies and zero or more rules. Targets are files that you want to obtain. Dependencies are files needed to create or update the targets. The set of rules describes the process of transforming dependencies into targets. For example imagine you want to automate installation on Node.js packages:

```
node_modules: package.json
	npm install
```

This means the **file** `node_modules` (yes, directories are files too) can be derived from the **file** `package.json` by running the `npm install` rule. Still with me?

Now, those dependencies can be other targets as well. This means we can chain different set of rules and create pipelines. For example making test results directory dependent on build directory, build directory dependent on `node_modules` directory and `node_modules` dependent on `package.json`. Heck, we can even create `package.json` dynamically making it a target of another rule.Remember when I mentioned `make` keeps track of which file is more recent? This is what actually saves us time. You see, without this feature, each time we run `make test` (following the example above) we would have to run the whole chain from the beginning (`npm install`, build, then test). But if nothing changed why install packages once again? Why build? Why run tests?

This is where `make` really shines. While figuring out the order of the jobs it checks the timestamps of targets and dependencies. It follows the rule **only** if

* one or more of dependencies is more recent than the target, and
* the target does not exist.

One thing! As `make test` won’t be actually creating a file named `test` we need to add this target as a dependency of a `.PHONY` target. That’s another convention. Like this:

```
.PHONY: test

test: build
	npm test
	
build: node_modules
	npm build
	
node_modules: package.json

```

In our example above, a single change in `package.json` would result in building everything from scratch. But if we only change the code of one of the tests, `make` would skip all the steps prior to tests. That is, provided the dependencies are written correctly.

#### But the Language I Use Already Has Its Own Build System…

Many modern programming languages and environments come with their own build tools. Java has Ant, Maven, and Gradle, Ruby has its Rake, Python uses setuptools. And if you are worried I’m about to take those toys away from you and replace them with `make`, you are mistaken.

Look at it this way: how much time is needed to introduce a person to your team and make that person productive? This means setting up the development environment, installing all the dependencies, configuring every moving part, building the project, running the project, maybe even deploying the project to a development environment.

Will a new hire start the actual work in a matter of hours? Days? Hopefully not weeks. Remember it’s not just the new hire’s time that’s wasted in the setup process. Somebody will also be bothered with lots of questions when things go wrong. And they usually do.

There is a convention I like to use in my projects. Since it’s a convention common to multiple projects, people are free to migrate between them. Each new project or each new person that’s introduced needs to learn this convention to reach the desired outcome. This convention assumes that projects have their own Makefiles with a set of predefined targets:

* `make prepare` installs all the external applications that might be needed. Normally this is done with a `Brewfile` and Homebrew/Linuxbrew. Since this step is optional coders can choose their own installation method at their own risk
* `make dev` sets up a local development environment. Usually, it builds and brings up Docker containers. But since `make` acts as a wrapper, it can be easily substituted by whatever is required (like `npm serve`)
* `make deploy` deploys the code to the select environment (by default its `development`). Under the hood, it usually runs Ansible.
* `make infrastructure` this is a prerequisite for `make deploy` as it uses Terraform to create said environments in the first place.
* `make all` produces all the artifacts required for deployment.

You know what it means? It means the mandatory `README.md` can focus on the business needs of the project and outline some collaboration processes. At the end, we attach the above list so everyone knows what those targets are. This means that when you enter a new project all you have to do is to `make prepare` and `make dev`. After a few CPU cycles you have a working project in front of you and you can start hacking.

### I Have a Continuous Integration Pipeline for That

At this point, some people may notice what am I getting at. Artifacts, steps, deployment, infrastructure. That’s what our Continuous Integration/Continuous Deployment pipeline does. I’m sure it does! But remember that CI/CD is not only there to run tests each time a new commit pops up.

Properly implemented CI/CD can help reduce debugging by making it easier to reproduce the issue and perform the root cause analysis. How? Versioned artifacts are one such means. They may help with finding the root cause, but not necessarily in fixing it.

To fix the bug you need to alter the code and produce your own build. See what I’m getting at? If you CI/CD pipeline can be mirrored locally developers can test and deploy tiny changes without the need to actually use the CI/CD pipeline thus shortening the cycle. And the easiest way to make your CI/CD pipeline available locally is by making it a thin wrapper around `make`.

Say you have a backend and a frontend and you have some tests for them as well (if not, you’re crazy running CD without tests!). This would make four distinct CI jobs. And they could be pretty much summed up as calling `make backend`, `make test-backend`, `make frontend`, `make test-frontend`. Or whatever convention you want to follow.

This way, no matter whether on a local machine or on CI, the code is built exactly the same way. Exactly the same steps are involved. The less commands go into your `Jenkinsfile` or `.travis.yml` (or some such) the less you rely on a Holy Build Machine.

### Ok, But Does Anyone Actually Use Make?

It turns out, yes. If you look around you’ll find articles like “Time for Makefiles to Make a Comeback” (by Jason Olson). “The Power Of Makefile” (by Ahmad Farag). “Rewriting our deploy tooling: from Makefile to Bash and back again” (by Paul David). Or “Makefile for Node.js developers” (by Patrick Heneise). And these are articles from the last year, not some reminiscences from the past century.

Yes, I admit that `make` is clunky. I know about its many shortcomings and weird language features. But show me a better tool for actual development workflow automation and I’ll be glad to switch. Until then I’ll ROTFL looking at this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qb7VuJIDBwyg9MOLyh9rUg.gif)
_[https://asciinema.org/a/dQb0jENCYWsBOCC9UiKxxKG4x](https://asciinema.org/a/dQb0jENCYWsBOCC9UiKxxKG4x" rel="noopener" target="_blank" title=")_

It’s [available on GitHub](https://github.com/DoomHammer/uss_enterprise), if you want to fly it.

### Cool, Now Show Me the Code

Here are some excerpts to show you what’s possible with `make`.

```
.PHONY: dev

.stamps:
	@mkdir -p $@

.stamps/git-hooks.installed: | .stamps
	# This checks whether git-hooks is an executable and installs it with
	# Homebrew/Linuxbrew is possible.
	@if ! command -v git-hooks >/dev/null 2>&1; then \
	  if command -v brew >/dev/null 2>&1; then \
	    brew install git-hooks; \
	  else \
	    echo "You have to install https://github.com/icefox/git-hooks"; \
	    exit 1; \
	  fi; \
	fi
	@touch $@

.git/hooks.old: | .stamps/git-hooks.installed
	git hooks --install

dev: | .git/hooks.old
	pip install -e .[dev]
```

This snippet sets up a simple development environment. Since we want to make sure all developers use the same set of pre-commit hooks while working with Git we install those hooks for them.

To do this we need to install git-hooks (that’s the name of the hooks manager). We take advantage of the knowledge that git-hooks moves the original hooks to `.git/hooks.old` so we check for a presence of such a file to determine whether we want to run `git hooks install` or not.

One trick we use here is `|` to denote order-only dependencies. If you just want to make sure something exists, not that it change more recently than a target, order-only dependencies are the way to go. So far, so good, I suppose?

Now imagine we want to build a Docker container that contains a file we cannot distribute in our source code.

```
WEBAPP_SOURCES = $(sort $(notdir $(wildcard webapp/**/*)))

all: webapp

.stamps: Makefile
	@mkdir -p $@

third-party/top_secret.xml:
	# WEB_USER and WEB_AUTH_TOKEN are variables that should contain credentials
	# required to obtain the file.
	@curl -u "$(WEB_USER):$(WEB_AUTH_TOKEN)" https://example.com/downloads/this_is_a_secret.xml -L -o $@

webapp: .stamps/webapp.stamp
.stamps/webapp.stamp: .stamps webapp/Dockerfile third-party/top_secret.xml $(WEBAPP_SOURCES)
	docker build -t example/webapp -f webapp/Dockerfile webapp
	@touch $@

.PHONY: all webapp
```

Since we cannot use the actual file created by Docker (because images have tight permissions), we do the second best thing. We create an empty file that indicates we have successfully run `docker build` at one point in time.

A common convention for such files calls them “stamps”. Our Docker image stamp depends obviously on `Dockerfile`, on source files and on another target, which runs `curl` to fetch the file obtaining credentials from environment variables.

Since we don’t want to print our credentials to the output we prefix the command with `@`. This means the rule itself is not printed to the screen. The output of the rule, however, isn’t silenced. Keep that in mind if any of the programs you want to run have a tendency of logging sensitive information to stdout or stderr.

Ok, we can set up git hooks and we can build some Docker images. Why not let developers create their own environments in the cloud and deploy to them?

```
# We include the previous Makefile so we can build the image
include previous.mk

.stamps/webapp_pushed.stamp: .stamps/webapp.stamp
        docker push example/webapp
        @touch $@

infrastructure: $(INFRASTRUCTURE_SOURCES)
        cd deployment/terraform && terraform apply

deploy: all infrastructure
        cd deployment && ansible-playbook -i inventories/hosts deploy.yml

.PHONY: infrastructure deploy
```

The actual Infrastructure as Code and Configuration Management is out of the scope of this article. Let me tell you that `terraform apply` manages cloud resources and `ansible-playbook` performs configuration on remote machines. You probably know what `docker push` does. In short, it pushes the local image to Docker Hub (or any other registry) so you could access it from anywhere. At this point, I’m sure you can figure out what the above snippet does.

### So, Who’s This Tool For?

Even though DevOps is rising in hype recently, there is still a lot of separation between the Dev and the Ops. Some tools are used solely by Dev, some solely by Ops. There is a bit of common ground, but how far it reaches depends on any given team.

Development package management, source code layout, coding guidelines are all the realms of Dev. Infrastructure as Code, Configuration Management, and orchestration are toys for the Ops. The build system and Continuous Integration pipeline might be split between the two or it might belong to either party. Can you see how the common ground is stretched thin?

`make` changes things, allowing for broader collaboration. Since it serves the purposes of both Dev and Ops, it is a common ground. Everyone speaks its language and everyone can contribute. But because it is so easy to use even when you want to do complex things (as in our example above) the true power of DevOps is given to the hands of every person on the team. Everyone can run `make test` and everyone can modify its rules and dependencies. Everyone could run `make infrastructure` and provision a nice cluster for development or for production. After all, they are documented in the same code!

Of course, when there’s a common ground it’s good to make sure whose responsible for which part. The last thing you want is people from Dev and Ops overwriting each other’s work! But great teamwork always relies on great communication, so this could happen with or without `make`.

So it doesn’t matter if you use any of the trendy technologies associated with DevOps. You may not need and not want any Docker, Cloud, Terraform or Travis. You can write desktop applications, for what its worth, and a carefully written `Makefile` would still be a DevOps enabler.

