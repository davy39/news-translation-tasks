---
title: Learn Basic Terraform Syntax in 20 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-26T18:00:52.000Z'
originalURL: https://freecodecamp.org/news/terraform-syntax-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/terraform-article-cover-image.jpg
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: Terraform
  slug: terraform
seo_title: null
seo_desc: "By Sumeet Ninawe\nIn this article, I'll give you a brief overview of the\
  \ configuration syntax of Terraform. \nTerraform's docs provide the most comprehensive\
  \ look at its syntax. But this article should serve as a condensed quick start introduction\
  \ that..."
---

By Sumeet Ninawe

In this article, I'll give you a brief overview of the configuration syntax of Terraform. 

[Terraform's docs](https://www.terraform.io/docs/index.html) provide the most comprehensive look at its syntax. But this article should serve as a condensed quick start introduction that'll give new users a simplified overview. We'll focus on the basic structures without getting too deep in the weeds.

To help you learn the syntax, we'll go through an example and I'll teach you the most important parts of the Terraform configuration language (which is called HCL - the HashiCorp Configuration Language). Then we'll build out some infrastructure as code (IaC) to see it in action.

Before we start, you should have Terraform installed on your local system. You should also have access to the AWS management console, and have set up and configured an IAM user for Terraform.

## Arguments and Blocks in Terraform

The first example below creates an EC2 instance:

```
provider “aws” {
    region = “us-west-1”
}
 
resource “aws_instance” “myec2” {
    ami = “ami-12345qwert”
    instance_type = “t2.micro”
}
```

The code consists of two blocks wrapped in curly braces ( {} ), and each of these blocks has certain **arguments** defined.

Just like in most programming languages, you use arguments to assign values to variables. In Terraform, these variables are attributes associated with a particular type of block.

The provider “aws” block has one argument – `region = “us-west-1”`, where the region is an attribute associated with the block, and it is assigned a value “us-west-1”. The value is a string type, so it is enclosed in a pair of double quotes ( “” ).

Similarly, the resource block has two arguments that set the values of associated attributes.

Terraform uses various types of **blocks**. Based on the type, blocks represent and enclose a set of attributes and functions. In the given example, we have a block of type provider and another of type resource, and each block has an identifier and a set of input labels.

The provider block takes one input label – the name of the provider. In this case “aws”. It also tells Terraform to install the AWS provider plugin, during the init phase.

The resource block takes 2 inputs labels – the type of resource and the name of the resource. In this case, the type is “aws_instance” and the name is “myec2”. What follows is the block body enclosed in curly braces.

## How to Create an EC2 Instance on AWS

So, how do we start expressing our infrastructure as code and make use of it? Let’s take an example of creating a simple EC2 instance on AWS.

Start by creating a directory of your choice where you would place all the configuration code required to create an EC2 instance.

By default, Terraform assumes that all the files with `.tf*` extensions in a directory are part of the configuration, irrespective of the file names. Create a file named `main.tf` in this directory.

The first thing we need to decide is which providers we are going to use. Since we are going to spin up an EC2 instance on AWS, we need to declare the required providers as you can see in the snippet below:

```
terraform {
 required_providers {
   aws = {
     source  = "hashicorp/aws"
     version = "~> 3.0"
   }
 }
}

provider "aws" {
 region = “us-west-1”
}
```

We have declared two blocks – `terraform` and `provider`. `terraform` is a top-most block, but it is optional as well. It is a good practice to specify this, especially when you're working with remote state management. 

The `terraform` block has a nested block that specifies `required_providers`. We require the `aws` provider. `aws` within required_providers is a map, which specifies the `source` and `version` of the provider. 

Next, we have a provider block for `aws`, which specifies the desired `region`.

Generally, this is how every Terraform code starts. Of course, there could be some variations, and the best way to be sure about it is to refer to the [Terraform registry](https://registry.terraform.io/) for specific versions of Terraform as well as the provider plugin itself. 

For the sake of the current example, we are referring to [AWS plugin documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs). 

The Terraform registry documents usage of all the resources of various cloud providers with examples. It is a great reference when you're working with Terraform.

### Terraform Providers

Installing Terraform on the system is not enough. Terraform works on a plugin-based architecture, where the Terraform binary forms the core and every cloud provider is a plugin.

To make configurations work, these plugins are installed in the initialization phase. 

Provider plugins come with their own set of configurations, resource types, and data sources. The Terraform registry documents all the details for a given provider.

### Terraform Resources

Every provider comes with a set of resources. `resource`, as the name suggests, represents the actual cloud resource to be created in the configuration language.

Providers enable resources. In the given example, `aws` is a provider and `aws_instance` is a resource provided by the AWS provider. 

The resource has its attributes. These attributes are documented in the Terraform registry. Out of all the attributes, some of them are required. Resources are the exact constructs that are executed by Terraform.

Continuing with the example, let's define an AWS EC2 instance resource by appending the below code into our [`main.tf`](http://main.tf/) file.

```
resource "aws_instance" "demo" {
 ami = “ami-00831fc7c1e3ddc60”
 instance_type = “t2.micro”

 tags = {
   name = "Demo System"
 }
}
```

We start with a resource block named `“aws_instance”` and we pass a label and name it `“demo”`. The label is the name of your choice. 

Next, open the block using curly braces and specify the required attributes used by the resource `aws_instance`. The first attribute is `ami` which specifies the Amazon machine image ID for the EC2 instance. 

The second attribute is the `instance_type` which specifies the size of the machine to be created. 

We are also passing tags which is an optional argument. As a tag, we pass `“name”` as the key and `“Demo System”` in the value. That's it – we have defined our resource.

We are now technically ready with the configuration. We can go ahead and initialize Terraform into this directory so that it installs the provider plugin for AWS. We can then `plan` and `apply` this configuration. 

Save the file, and then go ahead and run `terraform init` and see if it installs the AWS provider plugin. Once that's done successfully, run `terraform plan` and observe the output.

Let's put everything into perspective. `providers` let Terraform know which plugins need to be installed to execute the configuration. `resources` represent the actual cloud resources to be created. 

Generally, every resource has a name ( `“aws_instance”` ). The initial part of the name of the resource is the provider identifier ( `“aws”` ) which is separated by an underscore.

### Terraform Variables

Terraform is a declarative language. In the example, we have declared the final state of the virtual machine on the desired cloud. 

Now it is up to Terraform to take this configuration and execute it to create the virtual resource. Having said that, Terraform gives us the ability to specify **input variables** to its configuration.

Input variables are like parameters for a given function just like in any programming language.

They are particularly useful when you have to specify the same value at multiple places in your code. As the project grows in size, it becomes easier to change certain values that might be used in multiple places using variables.

Terraform supports primitive types of variables such as string, number, boolean, and several complex types such as list, set, map, object, and tuple.

Let's define some variables into our code as below:

```
variable "region" {
 default = "us-west-1"
 description = "AWS Region"
}

variable "ami" {
 default = "ami-00831fc7c1e3ddc60"
 description = "Amazon Machine Image ID for Ubuntu Server 20.04"
}

variable "type" {
 default = "t2.micro"
 description = "Size of VM"
}
```

As you can see, we have introduced three new variables for the `region`, the `ami`, and the `type`. We'll use this in our configuration so far. The values of the variables can be referred to using `var.<variable name>`.

Terraform configuration also gives us the ability to return values. These values are known as **output values**. 

When Terraform completes the execution of the configuration, it makes the output values available. They can then be used as input to other interfaces. 

We have defined one output variable `“instance_id”` in our code. The value of this output variable is set using the attribute reference of `“aws_instance.demo”`. Similarly, we can refer to other output variables available from any resource in the configuration.

Below is the updated code of our `main.tf`. We have used three variables here:

```
terraform {
 required_providers {
   aws = {
     source  = "hashicorp/aws"
     version = "~> 3.0"
   }
 }
}
 
provider "aws" {
 region = var.region
}
 
variable "region" {
 default = "us-west-1"
 description = "AWS Region"
}
 
variable "ami" {
 default = "ami-00831fc7c1e3ddc60"
 description = "Amazon Machine Image ID for Ubuntu Server 20.04"
}
 
variable "type" {
 default = "t2.micro"
 description = "Size of VM"
}
 
resource "aws_instance" "demo" {
 ami = var.ami
 instance_type = var.type
 
 tags = {
   name = "Demo System"
 }
}
 
output "instance_id" {
 instance = aws_instance.demo.id
}
```

Save the file and run `terraform plan`. Notice that Terraform takes note of the output variable this time. It states that the output is known `after apply`:

```
Plan: 1 to add, 0 to change, 0 to destroy.
 
Changes to Outputs:
  + instance_id = (known after apply)
```

Go ahead and do `terraform apply`, and check out the output. Don't forget to run `terraform destroy` after every successful `apply`.

Lastly, Terraform also supports **local variables**, which are temporary values used locally by functions and blocks.

### Terraform Provisioners

Provisioning means to install, update, and maintain the required software once the hardware or virtual machine is ready to go. 

Terraform can trigger software provisioning processes once a virtual machine is ready, but that doesn't mean it is a full-time provisioning tool. 

You can use this tool to make the infrastructure ready for management by installing initial and essential software components.

There are tools like Salt Stack, Ansible, Chef, and others, and most of them are agent-based. Terraform can run initial scripts to install some patch updates, agent software, or even set some user access policies to make sure machines are ready to go.

Terraform comes bundled with generic provisioners and also supports vendor-specific provisioners.

## How to Manage Code in Terraform

Before we proceed, let's first organize our code into multiple files. As a general practice, the Terraform codebase is divided into multiple files based on the providers, resources, and variables. Let's create three files as below:

1. `variables.tf` – This file contains all the declared input variables. In our example, we have input variables defined for `region`, `ami`, and `type` and an output variable `instance_id`.
2. `provider.tf` – This file contains declarations for the providers you're using. In our case, we have `terraform`, and the provider `aws` blocks.
3. `main.tf` – This file contains the declarations for actual resources to be created.

By default, Terraform assumes that all the code placed in a particular directory is part of the same configuration. 

So technically it doesn't make much of a difference if you put the code in a single file or divide it into multiple files and sub-directories. From a maintainability point of view, it makes a lot of sense to do so.

### Meta-Arguments in Terraform

Before we get into this, make sure that when you're working through the examples, always run `terraform destroy` after every `terraform apply` run.

Meta-arguments are special constructs provided for resources. We have seen that resource blocks are the actual cloud resources that Terraform creates.

Often, it's tricky to declare resources in a way that satisfies certain requirements. 

Meta-arguments come in handy in situations like creating resources in the same cloud provider but in different regions. They're also useful when we are creating multiple identical resources with different names, or when we have to declare implicit dependencies at places where Terraform is not able to identify the dependency itself.

The sections below describe some meta-arguments in action.

#### The Provider meta-argument

You'll use the `provider` meta-argument when you have multiple provider configurations in a given Terraform config. Terraform automatically maps the given resource to the default provider identified by the resource’s identifier. 

For example, the default provider for `aws_instance` is `aws`. This `aws` provider is currently configured to deploy a resource in a particular region. 

However, if we want to have another `aws` provider for another region, or with a different configuration setting, we can write another provider block.

Even though it's possible to write multiple provider configs, Terraform by default picks the same provider for `aws` for creating resources. 

This is where **aliases** come into the picture. Every provider configuration can be tagged with an alias, and the value of this alias is used in our **provider** meta-argument in the resource block to specify different provider configurations for identical resources.

In our example, let's duplicate the `aws` provider and give them appropriate aliases. Modified providers with an alias should look like the below in the `provider.tf` file:

```
provider "aws" {
  alias  = "aws_west"
  region = var.region_west
}

provider "aws" {
  alias  = "aws_east"
  region = var.region_east
}
```

Notice that we have also modified variables for the region to represent two different regions, west and east. Make the corresponding changes to the `variables.tf` file as below:

```
variable "region_west" {
  default     = "us-west-1"
  description = "AWS West Region"
}

variable "region_east" {
  default     = "us-east-1"
  description = "AWS East Region"
}
```

One final change that we need to make is in the `main.tf` file. There, we can now use provider meta-argument to specify a specific provider's alias. 

We can mention the provider config we want by specifying `<provider>.<alias>` in the meta-argument. Refer to the modified `main.tf` file below:

```
resource "aws_instance" "demo" {
  provider      = aws.aws_west
  ami           = var.ami
  instance_type = var.type

  tags = {
    name = "Demo System"
  }
}
```

Validate the final configuration by running `terraform validate`, and it should say “`Success!`”

#### The Lifecycle meta-argument

The `lifecycle` meta-argument specifies the settings related to the `lifecycle` of resources managed by Terraform. By default, whenever a configuration is changed and applied, Terraform operates in this sequence:

1. Create new resources.
2. Destroy those resources which do not exist in config anymore.
3. Update those resources which can be updated without destruction.
4. Destroy and re-create changed resources that cannot be changed on the fly.

You can use a `lifecycle` meta-argument if you want to alter this default behavior. These meta-arguments are used in resource blocks similar to provider meta-arguments. 

There are three lifecycle meta-argument settings:

1. `create_before_destroy`: Used when you want to avoid accidental loss of infrastructure when a changed config is applied. When this is set to true, Terraform will first create the new resource before destroying the older resource.
2. `prevent_destroy`: When set to true, any attempt to destroy this in the config will result in an error. This is often useful in the case of those resources where reproduction can prove to be expensive.
3. `ignore_changes`: This is a list type meta-argument which specifies the attributes of a certain resource in the form of a list. During update operations, often there is a situation where you want to prevent changes caused by external factors. In those cases, you need to declare the list of attributes that should not be changed without being reviewed.

`lifecycle` meta-arguments come in handy when we are in the process of setting up complex infrastructure. 

By altering the default behavior of Terraform, we can put some protection in the form of `lifecycle` meta-arguments for confirmed and finalized resource blocks. 

In our example, we would not use any lifecycle meta-arguments.

#### The depends_on meta-argument

Generally, Terraform is aware of dependencies while creating or modifying resources and takes care of the sequence by itself. 

However, in certain cases Terraform can't detect the implicit dependencies and just moves on with creating resources in parallel if it doesn’t see any dependency.

Take, for example, a Terraform configuration for two EC2 instances enclosed in a VPC. 

When you have this configuration, Terraform automatically knows that it shoudl create the VPC before spinning up the EC2 instances. 

This is general knowledge and Terraform knows it very well. In situations where dependencies are not so obvious, the `depends_on` meta-argument comes to the rescue. 

It is a list type of argument that takes in the list of resource identifiers declared in the configuration.

#### The count meta-argument

Imagine a situation where you would like to create multiple similar resources. By default, Terraform creates one real resource for a single resource block. 

But in the case of multiple resources, Terraform provides a meta-argument named `count`. As the name suggests, the `count` can be assigned with a whole number to represent multiple resources.

In our example, let's create three similar EC2 instances. In your `main.tf` file, add an attribute count to the resource `aws_instance.demo`, and assign it a value of `3`. It should look something like the below:

```
resource "aws_instance" "demo" {
  count         = 3
  provider      = aws.aws_west
  ami           = var.ami
  instance_type = var.type

  tags = {
    name = "Demo System"
  }
}
```

By doing this, we let Terraform know that we need to create three EC2 instances with the same configuration. 

Save the file and execute `terraform validate`. It throws an error saying “`Missing resource instance key`”. 

Remember in our `variables.tf` file we mentioned an output variable to output the `id` of the created resource. Since we have asked Terraform to create three instances, it is not very clear  which ID it should print. 

To get around this problem, we use a special expression called a `splat` expression. 

The ideal case here is to run a for loop over the instance and print out the ID property. The splat expression is a better way to do the same task with fewer lines of code. 

All you need to do is in the `variables.tf` file, replace the output value code with the below:

```
output "instance_id" {
  value = aws_instance.demo[*].id
}
```

Save this file and run `terraform validate` to see if everything is okay. 

Once successful, go ahead and run `terraform plan` and `apply` and check your AWS management console in us-west-1 region, that is `aws_west`. Let me know the IDs too.

Splat is one of a kind and we will take a better look at expressions in upcoming sections.

#### The for_each meta-argument

`for_each`, as the name suggests, is essentially a “for each” loop. `for_each` meta-argument is used to create/loop through multiple similar cloud resources. Yes, it does sound similar to the `count` meta-argument but there is a difference.

Firstly, `for_each` and `count` cannot be used together.

Secondly, you can say this is an enhanced version of the `count`. Count meta-argument is a number type. Terraform simply creates this many resources. 

However, if you would like to create these resources with some customizations in the output, or if you already have an object of type map or list based on which you want to create resources, then the `for_each` meta-argument is the way to go.

As mentioned earlier, you can assign `for_each` map and list type of values. A map is a collection of key-value pairs, whereas a list is a collection of values (in this case string values).

`for_each` comes with a special object `each`. This is the iterator in the loop which you can use to refer to the `key` or `value`, or only the key in case of list. 

Let's take a look at our example. We would like to create EC2 instances for the given map. The map is assigned to the `for_each` meta-argument and Terraform creates an EC2 instance for each key-value pair in the map. 

Lastly, we use the `key` and `value` information using `each` object to set the name attribute in the `tag`.

The resource block in `main.tf` now looks something like this:

```
resource "aws_instance" "demo" {
  for_each = {
    fruit = "apple"
    vehicle = "car"
    continent = "Europe"
  }
  provider      = aws.aws_west
  ami           = var.ami
  instance_type = var.type

  tags = {
    name = "${each.key}: ${each.value}"
  }
}
```

Execute `terraform validate` and observe the output. It throws an error for the output variable – “`This object does not have an attribute named id`”. 

A quick note here: `splat` expressions work for the list type of variables. Since we used map while setting our `for_each` meta-argument, we need to change the return value expression to for each, as below:

```
output "instance_id" {
  //value = aws_instance.demo[*].id
  value = [for b in aws_instance.demo : b.id]
}
```

Execute `terraform validate` again. If it's successful, go ahead and `apply` the configuration. Check the AWS management console for the machines created and the names assigned to them.

### Terraform Expressions

Expressions are ways to make your Terraform code dynamic. 

Expressions come in two forms – simple and complex. Up until now in our examples, we have mostly dealt with simple expressions. 

A simple expression is any argument used as part of some block. Writing down an argument with a primitive value assigned to it is a form of expression.

We have used a complex expression called splat ( `*` ) in our example while working with meta-arguments. 

However, there are even more complex expressions that you can use to make your Terraform code more dynamic, readable, and flexible. There are various types of expressions that you can take a look at in the [Terraform documentation](https://www.terraform.io/docs/configuration/expressions/index.html).

### Terraform Functions

Terraform has built-in functions that you can use with expressions. These are utility functions that are useful in number and string manipulations. 

There are functions to work with file systems, date and time, network, type conversion, and more.

Functions along with expressions make it super easy to write a really dynamic IaC. You can refer to the list of functions [here](https://www.terraform.io/docs/configuration/functions.html).

## Conclusion

In this post, we were able to play around with AWS EC2 instances using Terraform. I hope this helps you get more comfortable working with Terraform.

If you like this content, do consider subscribing, following, and sharing this blog post! [Let'sDoTech](https://letsdotech.dev/), [Instagram](https://www.instagram.com/letsdotech/), [Twitter](https://twitter.com/letsdotech_dev), [LinkedIn](https://www.linkedin.com/company/letsdotech).

