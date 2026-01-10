---
title: What Are Terraform Modules and How Do They Work?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-09T00:18:25.000Z'
originalURL: https://freecodecamp.org/news/terraform-modules-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/tf-modules.jpeg
tags:
- name: Devops
  slug: devops
- name: Terraform
  slug: terraform
seo_title: null
seo_desc: 'By Serhii Vasylenko

  Surprisingly, a lot of beginners skip over Terraform modules for the sake of simplicity,
  or so they think.

  Later, they find themselves going through hundreds of lines of configuration code.

  I assume you already know some of the ba...'
---

By Serhii Vasylenko

Surprisingly, a lot of beginners skip over Terraform modules for the sake of simplicity, or so they think.

Later, they find themselves going through hundreds of lines of configuration code.

I assume you already know some of the basics about Terraform, and have even tried to use it before. If not, check out this [overview on Terraform](https://serhii.vasylenko.info/2020/05/02/Terraform-explained-for-managers.html) and this [video tutorial](https://www.freecodecamp.org/news/how-to-use-terraform-to-automate-your-aws-cloud-infrastructure-tutorial/) before you continue reading.

Please note: I do not use real code examples with some specific provider like AWS or Google intentionally, just for the sake of simplicity.

## Terraform modules

### You already write modules

Even when you don't create a module intentionally, if you use Terraform, you are already writing a module – a so-called "_root_" module.

Any Terraform configuration file (`.tf`) in a directory, even just one, forms a module.

### What does a module do?

A Terraform module allows you to create logical abstraction on the top of some resource set. In other words, a module allows you to group resources together and reuse this group later, possibly many times.

Let's assume we have a virtual server with some features hosted in the cloud. What set of resources might describe that server? For example:

* the virtual machine itself, created from some image
* an attached block device of a specified size for additional storage
* a static public IP mapped to the server's virtual network interface
* a set of firewall rules to be attached to the server
* other things like another block device, additional network interface, and so on

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Untitled-2020-08-24-0025-10.png)

Now let's assume that you need to create this server with a set of resources many times. This is where modules are really helpful – you don't want to repeat the same configuration code over and over again, do you?

Here is an example that illustrates how our "server" module might be called.  
"_To call a module_" means to use it in the configuration file.

Here we create 5 instances of the "server" using single set of configurations (in the module):

```hcl
module "server" {
    
    count         = 5
    
    source        = "./module_server"
    some_variable = some_value
}
```

### Module organisation: child and root

Of course, you would probably want to create more than one module. Here are some common examples:

* a network like a virtual private cloud (VPC)
* static content hosting (i.e. buckets)
* a load balancer and it's related resources
* a logging configuration
* or whatever else you consider a distinct logical component of the infrastructure 

Let's say we have two different modules: a "server" module and a "network" module. The module called "network" is where we define and configure our virtual network and place servers in it:

```
module "server" {
    source        = "./module_server"
    some_variable = some_value
}

module "network" {  
    source              = "./module_network"
    some_other_variable = some_other_value
}
```

Once we have some custom modules, we can refer to them as "child" modules. And the configuration file where we call child modules relates to the root module.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Untitled-2020-08-24-0025-11.png)

A child module can be sourced from a number of places:

* local paths
* the official Terraform Registry – if you're familiar with other registries like the Docker Registry then you already understand the idea
* a Git repository (a custom one or GitHub/BitBucket)
* an HTTP URL to a .zip archive with the module

But how can you pass resources details between modules? 

In our example, the servers should be created in a network. So how can we tell the "server" module to create VMs in a network which was created in a module called "network"?

This is where **encapsulation** comes in.

## Module encapsulation

Encapsulation in Terraform consists of two basic concepts: module scope and explicit resource exposure.

### Module Scope

All resource instances, names, and therefore, resource visibility, are isolated in a module's scope. For example, module "A" can't see and does not know about resources in module "B" by default.

Resource visibility, sometimes called resource isolation, ensures that resources will have unique names within a module's namespace. For example, with our 5 instances of the "server" module:

```
module.server[0].resource_type.resource_name
module.server[1].resource_type.resource_name
module.server[2].resource_type.resource_name
...
```

On the other hand, we could create two instances of the same module with different names:

```
module "server-alpha" {    
    source        = "./module_server"
    some_variable = some_value
}
module "server-beta" {
    source        = "./module_server"
    some_variable = some_value
}
```

In this case, the naming or address of resources would be as follows:

```
module.server-alpha.resource_type.resource_name

module.server-beta.resource_type.resource_name
```

### Explicit resource exposure

If you want to access some details for the resources in another module, you'll need to explicitly configure that.

By default, our module "server" doesn't know about the network that was created in the "network" module.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Untitled-2020-08-24-0025-13.png)

So we must declare an `output` value in the "network" module to export its resource, or an attribute of a resource, to other modules.

The module "server" must declare a `variable` to be used later as the input:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Untitled-2020-09-01-2021-4.png)
_The names `output` and `variable` can differ, but I suggest using the same names for clarity._

This explicit declaration of the output is the way to expose some resource (or information about it) outside — to the scope of the 'root' module, hence to make it available for other modules.

Next, when we call the child module "server" in the root module, we should assign the output from the "network" module to the variable of the "server" module:

```
network_id = module.network.network_id
```

Here's what the final code for calling our child modules will look like:

```
module "server" {
    count         = 5
    source        = "./module_server"
    some_variable = some_value
    network_id    = module.network.network_id
}

module "network" {  
    source              = "./module_network"
    some_other_variable = some_other_value
}
```

This example configuration would create 5 instances of the same server, with all the necessary resources, in the network we created with as a separate module.

## Wrapping up

Now you should understand what modules are and what do they do.

If you're at the beginning of your Terraform journey, here are some suggestions for the next steps.

I encourage you to take this short tutorial from HashiCorp, the creators of Terraform, about modules: "[Organize Configuration](https://learn.hashicorp.com/collections/terraform/modules)".

Also, there is a great comprehensive study guide which covers everything from beginner to advanced concepts about Terraform: "[Study Guide - Terraform Associate Certification](https://learn.hashicorp.com/tutorials/terraform/associate-study?in=terraform/certification)".

The modular code structure makes your configuration more flexible and yet easy to be understood by others. The latter is especially useful for a team.

If you liked the article, follow me on Twitter ([@vasylenko](https://twitter.com/vasylenko)) where I occasionally share my findings and tips about Terraform, AWS, Ansible, and other DevOps-related technologies.

