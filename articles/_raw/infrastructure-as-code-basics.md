---
title: What is Infrastructure as Code? Explained for Beginners
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-06-15T14:32:46.000Z'
originalURL: https://freecodecamp.org/news/infrastructure-as-code-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/cover-5.png
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: Terraform
  slug: terraform
seo_title: null
seo_desc: Infrastructure as Code (IaC) is a way of managing your infrastructure like
  it was code. This gives you all the benefits of using code to create your infrastructure,
  like version control, faster and safer infrastructure deployments across different
  en...
---

Infrastructure as Code (IaC) is a way of managing your infrastructure like it was code. This gives you all the benefits of using code to create your infrastructure, like version control, faster and safer infrastructure deployments across different environments, and having up to date documentation of your infrastructure.

The article will cover how infrastructure as code works using an analogy. We'll cover the different infrastructure as code tools available as well as declarative vs imperative code

I'll also introduce you to Terraform, which is an open source infrastructure as code tool you can use to create infrastructure across multiple cloud providers like AWS, GCP, Azure and others.

## Infrastructure as Code in Practice

Imagine you are trying to create a three-tiered web application on AWS as you can see in the image below:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f739c67-e79c-4995-b58d-71d695cccd47_1018x1682.png align="left")

*Three tiered web application example*

The presentation tier is responsible for presenting the user interface to the user. It includes the user interface components such as HTML, CSS, and JavaScript running on EC2 instances.

The logic tier is responsible for processing user requests and generating responses, by communicating with the database layer to retrieve or store data. This is also deployed on EC2 instances

The database tier is responsible for storing and managing the application's data and allows access to its data through the logic tier. The database runs on AWS RDS.

Each of the instances are in an [autoscaling](https://lightcloud.substack.com/i/102200211/auto-scaling-explained) group with a [load balancer](https://lightcloud.substack.com/i/102200211/load-balancing-explained) in front of it (except for the database tier).

If you want to create this infrastructure through the AWS console, you would have to manually click through various screens to spin up the infrastructure. This is fine if it is a one time activity.

But if you need to repeat this across different environments like development and test, or need to add additional infrastructure like caches, queues, firewall rules, [IAM](https://lightcloud.substack.com/p/aws-iam-identity-and-access-management) or SSL certificates, then it becomes increasingly more complex to manage through the AWS console.

Managing complex infrastructure through the console also introduces the possibility of human error.

Infrastructure as code expresses your desired infrastructure in the language of code. This brings all the benefits of code to managing your infrastructure like:

1. Version Control – allows you to store the history of your infrastructure and revert to a previous version if needed.
    
2. Faster & safer deployments – can recreate infrastructure in new environments quickly and with less errors since every part of the infrastructure is clearly defined in the code.
    
3. Documentation – your current infrastructure state is documented and kept up to date automatically whenever you make a change. This keeps your infrastructure documentation detailed and accurate, compared to having the infrastructure written in a document or on a confluence page that may not be updated whenever there is a change.
    

## How Infrastructure as Code Works – Explained with an Analogy

Infrastructure as code allows you to create a detailed blueprint of your infrastructure. This blueprint gives instructions to your cloud provider about the infrastructure you want created.

This is similar to how an architecture blueprint works. It outlines the layout, dimensions, materials, and various components of the structure. The blueprint serves as a reference for architects and engineers to understand the desired construction.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d1aacbf-34c7-43ae-8384-2f912072cc00_2728x1514.png align="left")

*how an architectural blueprint is analogous to infrastructure as code*

The blueprint leaves little room for error. It will be interpreted in the same way by any architect or engineer. If you wanted to build exact copies of this house, all you need is the architecture blueprint.

Infrastructure as code, at a basic level, works in the same way as an architecture blueprint. It details the infrastructure you want to create as code in a number of different possible languages (JSON, YAML, HCL, Python, Ruby, JavaScript, and so on), instructing the cloud provider to create your infrastructure exactly as specified.

## Declarative & Imperative Infrastructure as Code Tools

There are many IaC options to choose from, and all the major cloud providers have their own dedicated tools:

* AWS has CloudFormation
    
* GCP has Deployment Manager
    
* Azure has Resource manager
    

One limitation of these cloud provider-specific tools is that they can only create infrastructure in their respective clouds. So CloudFormation only works in AWS and Deployment Manager only works in GCP. IaC using these providers is usually written in JSON or YAML format.

Terraform, on the other hand, is open source and you can use it to create infrastructure across all the major cloud providers. It uses HCL (HashiCorp Configuration Language).

Infrastructure as code can also be written using popular languages like Python and JavaScript.

These scripting/programming languages lie on a spectrum of declarative and imperative code as shown below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdaba03dc-13eb-4f45-873f-6f00dd648ffb_2508x870.png align="left")

*A spectrum of declarative & imperative languages and where Terraform HCL fits*

The main difference between an imperative and declarative language is that imperative languages explicitly define the *control flow*. This is simply the order in which instructions are executed in a program. Control flow determines the path the program takes and how it responds to different conditions or events.

In imperative languages, control flow is explicitly defined using control structures such as loops, conditionals, and function calls. Imperative languages give you more flexibility in configuring your infrastructure. This is not necessarily a positive, as more flexibility means more opportunity to introduce errors into your infrastructure.

A declarative language focuses on describing the desired result without giving specific instructions on how to achieve it.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fe4d2ce-6449-4597-beca-5a46f2aa6ee8_2620x1468.png align="left")

*An illustration demonstrating the difference between declarative and imperative languages*

An example JSON is shown below, used in AWS CloudFormation to create an EC2 instance:

```python
"Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "ami-0123456789",
        "InstanceType": "t2.micro",
        "KeyName": "my-key-pair",
        "SecurityGroupIds": ["sg-0123456789"],
        "SubnetId": "subnet-0123456789",
        "Tags": [
          {
            "Key": "Name",
            "Value": "MyEC2Instance"
          }
        ]
      }
```

A declarative language like JSON [abstracts](https://lightcloud.substack.com/p/cloud-computing-abstractions-explained) away the underlying complexity that details how the EC2 instance will be created. All it cares about is the end state.

Terraform HCL is closer to the declarative end of the spectrum. Terraform allows you to describe the desired infrastructure's final state without specifying the exact steps to get there. Terraform internally manages the execution order, resource dependencies, and handles the infrastructure changes based on the desired configuration.

But Terraform does have support for some imperative features like variables and expressions, allowing dynamic behaviour based on inputs. So, it is not a completely declarative language like JSON.

## How Terraform Works

There are two fundamental concepts that serve as a foundation for understanding Terraform:

1. The configuration file – this describes the desired infrastructure
    
2. The state file – this describes the current infrastructure as it exists in the real world
    

Terraform’s job is to create, modify or delete infrastructure as needed so that the desired infrastructure configuration is met. It does this by executing the necessary API calls to your cloud provider(s) to create, modify, or destroy the resources as specified.

Once the infrastructure has been created/modified/destroyed to match the configuration file, the state file is updated to reflect the current infrastructure.

The `terraform plan` command creates an [execution plan](https://developer.hashicorp.com/terraform/cli/commands/plan), which lets you preview the changes that Terraform plans to make to your infrastructure.

By default, when Terraform creates a plan, it compares the desired configuration as described in the configuration file, with the current configuration as described in the state file. Terraform then proposes a list of changes needed what will ensure that the current configuration matches the desired configuration.

If you then run the `terraform apply` command, terraform will modify the real world infrastructure so that it matches the desired configuration, and updates the state file to show the new infrastructure configuration.

At a high level, this is what terraform does:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba9f88a0-e8bb-4507-9fd9-a9576bb8fefe_2650x1380.png align="left")

*What happens when you run the* `terraform apply` command

Let’s bring back the architectural blueprint analogy.

The configuration file is like the architectural blueprint. It details the infrastructure that needs to be built, that is the desired construction. The real world infrastructure is the existing construction in the physical world and the state file is a representation of what currently exists – the current blueprint. The engineers work to ensure that the existing construction matches the architecture blueprint.

In this analogy, engineers do the work of Terraform in ensuring that the existing construction matches the architecture blueprint. You don’t need to specify the details of how to build the house, you just need to specify what you want built and the engineers handle the rest.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F973320df-191b-46b6-be0a-18cd43305288_2620x1468.png align="left")

*An architectural analogy to running* `terraform apply`

If you want to learn more about how Terraform works and how you can use it in your projects, you can [check out this free course](https://www.freecodecamp.org/news/learn-terraform-and-aws-by-building-a-dev-environment/) on freeCodeCamp's YouTube channel.

## Bringing it Together

Infrastructure as code (IaC) is a great way of managing complex infrastructure configuration in the form of code. This naturally brings all the advantages of code to your infrastructure like version control, faster and safer infrastructure deployments across different environments and up to date documentation of your infrastructure.

Terraform is an open source IaC tool that allows you to work with multiple cloud providers to spin up infrastructure as defined in your configuration files.

Terraform HCL is a declarative language that allows you to describe your desired infrastructure configuration. All you have to do is specify what you want created and terraform handles the creation on your behalf by making API calls to your chosen cloud provider(s).
