---
title: Why you might need Ansible and not even know it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T10:39:43.000Z'
originalURL: https://freecodecamp.org/news/why-you-might-need-ansible-and-not-even-know-it-d33b6e4b2ebe
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TP4UG0OLyN06mS39
tags:
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Piotr Gaczkowski

  Configuring machines with shell scripts is terribly messy

  Do you want to start using Ansible? Are you already using it, but coming up against
  challenges? Even if you don’t fall into either category, don’t stop reading. I’m
  going t...'
---

By Piotr Gaczkowski

#### Configuring machines with shell scripts is terribly messy

Do you want to start using Ansible? Are you already using it, but coming up against challenges? Even if you don’t fall into _either category_, don’t stop reading. I’m going to show you why you might actually **need** Ansible and how to best take advantage of it.

Ansible’s catchphrase is “simple IT automation.” This is a pretty accurate description of what it does. In its most popular mode of operation (there are several), you describe the desired state of your machines, and Ansible manipulates them to achieve this state. At this point, you may be thinking “yeah, but we’ve already got shell scripts for that.” Ansible, though, offers several advantages over good old shell scripts.

First of all, the playbook, which describes the desired state, is declarative and written in [YAML](http://yaml.org/). Using a playbook means you don’t need to handle the error control and condition checking yourself. It also means no actions will be taken if the state is already satisfied (e.g. `apt-get` won’t run if an `nginx` package is already installed).

But this is only part of the story.

The other thing that makes Ansible so powerful is the use of modules. Instead of relying on many third-party applications (`sed`, `grep`, `jq`, `useradd`, `parted`, etc.) and parsing their output, you can focus solely on the state itself. This means that regardless of the underlying userspace programs (`useradd`, `adduser`, Busybox, BSD, or GNU variants), you can just specify a universal task as follows:

```yaml
– name: Create the operator user
  user:
    name: operator
    createhome: yes
    groups: wheel
    shell: /bin/sh
```

In the same way, you would encapsulate parts of your script into separate libraries, Ansible embraces the concept of roles. Roles describe particular states of a machine, together with possible variables, configuration files, or templates. They’re aptly named, and the machine can use roles like `docker`, `nginx`, and `python`, for example. Each of these may then be tested in isolation and reused among all of your projects. They also can encapsulate more abstract concepts like the [ansible-hardening](https://github.com/openstack/ansible-hardening) role from OpenStack, which makes a target a little bit harder to break.

**And the other cool thing?** To run Ansible, you only need Python 2.6+ on your target machines and an open SSH connection. There’s no need to install anything else! This means you’re probably ready to start using Ansible right away! Prepare your control machine by running brew install ansible or pip install -user ansible and follow me.

### Deployment as Code

**Forget about the README located in the project’s root directory.** It usually contains all the tedious details on how to deploy to staging or production. With Ansible, the documentation is in the code. It’s testable, it’s reusable, and it can be run by anybody, as long as the person has access to the target machines. It also forms the perfect basis for a Continuous Deployment (CD) pipeline.

Making sure your app is always deployable can also help avert disaster. Instead of figuring out what to do when your servers go down, you simply edit the inventory file and make a fresh deployment to a new set of machines.

### Make Sure Your Team Is Ready for DevOps

When the deployment is a part of the codebase, it has to evolve with the codebase. Make sure all of your team is DevOps-enabled and understands how to use Ansible. The best way to do this is to provide a Vagrant environment so each dev can test the deployment process locally.

It’s essential that you test your deployment code in the same way you test your application. Each change to an application that may be relevant to deployment needs to be reflected in changes to Ansible files. For example, if you add new files that must be copied to the server, make sure there’s a corresponding task. If an application starts logging in a particular directory, make sure Ansible creates that directory and sets appropriate permissions.

### It’s Easy to Make It Work, Harder to Make It Maintainable

Ansible has its downsides, as well. These aren’t necessarily related to the tool itself, but they do crop up occasionally. Even though Ansible has well-documented [best practices](http://docs.ansible.com/ansible/latest/playbooks_best_practices.html), those don’t always help you achieve a single goal. This can lead to the creation of complicated solutions when simple ones would suffice.

### Prefer One-Time Deployments

Even though one of the features Ansible advertises is [idempotence](https://stackoverflow.com/questions/1077412/what-is-an-idempotent-operation), it’s still quite easy to write a playbook that won’t work correctly. For example, how do you update service in an idempotent way? You can’t, it’s self-contradictory, which means you have to sacrifice one thing to save another (an update, that is).

There are two concepts that can help with this problem: [disposable infrastructure](http://www.conigliaro.org/disposable-not-immutable-infrastructure/) and [immutable infrastructure](https://www.oreilly.com/ideas/an-introduction-to-immutable-infrastructure). The two are pretty similar from a deployment point of view. The former assumes that a machine can be easily disposed of at any point in time after a successful deployment. It may be reconfigured in the future, but there’s nothing stopping you from taking it down at any time. The latter also requires that a machine never changes its configuration after it is provisioned.

Both assume your application is located beyond a load balancer (or a reverse proxy). Such a load balancer could be hosted either externally or internally, independent of the rest of the infrastructure. Services that make up your application are registered in the load balancer. The backend configuration is updated dynamically as services come and go. If you want to host the load balancer yourself, [confd](https://github.com/kelseyhightower/confd) or [consul-template](https://github.com/hashicorp/consul-template) can help with dynamic reconfiguration.

### Use and Reuse Roles

Questions like when and how to use roles or what aspects should be configurable don’t have single, straightforward answers. In my experience, it’s best to think of the various use cases for a particular machine and then to encapsulate those use cases in separate roles that can not only be tested in isolation but can also be reused for other projects. Such reuse also leads to better code quality thanks to a larger testing base.

### A Galaxy of Possibilities

[Ansible Galaxy](https://galaxy.ansible.com/) provides lots of modules we can use. This is similar to Docker Hub or NPM, where you can search for the relevant parts and use them in your project. They are all written adhering to one standard, meaning they should be easily reusable. Unfortunately, this isn’t always the case.

More than once in my career, I’ve happened upon a module that declared compatibility with Debian but was only ever tested on Ubuntu. This may not be a problem if you can choose your base OS. It may mean some additional work in porting it if you want to make use of existing infrastructure.

Version pinning is another problem. We all know that software evolves and that backward compatibility is rarely observed. When modules use several dependencies, it’s crucial that every such dependency is described with an exact version tag. This way, we can avoid the problem of installing a package in the latest version that’s no longer compatible with another part of the system.

When talking about pinned versions, there’s no avoiding the subject of bit rot. Unused software decays. Referenced hyperlinks can become obsolete, releases can be taken down, hosting services may cease operation. Even if a module uses a pinned version, it may become unusable if it’s not regularly tested and updated as needed, which leads us to our next topic.

### Testing Is Hard — and Time-Consuming

Ansible usually operates on system services. While it’s possible to test some of its features in containers (e.g., with Docker), this approach will generally fail. Docker can’t test all the kernel operations or systemd calls, because they don’t exist in its scope. To properly test Ansible playbooks, you need VMs. **Did you notice the plural?** **Good, because it’s not enough to test on just one VM.**

The most basic test setup should use a clean VM, run the playbook, check the results, and then run the playbook again to check for idempotency issues. But this only gives you limited information. You still don’t know if the playbook will actually deploy in production. The target machine won’t necessarily be a clean VM (unless you’re already using disposable infrastructure).

To mitigate this risk, it may be a good idea to have a separate VM that could serve as “long-term memory.” This VM, in contrast, would not be cleaned after every test deployment but would allow changes to accumulate over time.

### Summary

The best way to document code is in the code itself. Considering this simple statement leads us to a logical conclusion — the best deployment documentation is the deployment code. There are many tools to help achieve this, with Ansible being one of them. Personally, I prefer it to [Chef](https://www.chef.io/chef/) or [Puppet](https://puppet.com/), but I’ve yet to try [Salt](https://saltstack.com/) or [StackStorm](https://stackstorm.com/).

As with every tool I’ve encountered in my professional life, it also has its downsides. Knowing them up front should help you avoid some of the problems I’ve stumbled upon. Hopefully, learning from my experience will save you time and frustration in your own work.

> _If you like [what I create](https://medium.com/@doomhammerng) consider [subscribing to Bit Better.](http://eepurl.com/gcdRVb) It’s a community newsletter with recommendations for books, articles, tools, and sometimes music._

_Originally published at [https://www.iamondemand.com](http://www.iamondemand.com/blog/might-need-ansible-not-even-know/) on August 10, 2017._

