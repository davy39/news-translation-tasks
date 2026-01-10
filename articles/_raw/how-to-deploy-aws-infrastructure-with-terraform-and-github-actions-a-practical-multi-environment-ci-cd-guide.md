---
title: How to Deploy AWS Infrastructure with Terraform and Github Actions – A Multi-Environment
  CI/CD Guide
subtitle: ''
author: Nitheesh Poojary
co_authors: []
series: null
date: '2022-02-11T19:09:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-aws-infrastructure-with-terraform-and-github-actions-a-practical-multi-environment-ci-cd-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/pexels-pixabay-163235.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud
  slug: cloud
- name: GitHub
  slug: github
- name: Terraform
  slug: terraform
seo_title: null
seo_desc: "Recently, I've been considering developing a complete end-to-end greenfield\
  \ DevOps personal lab project. \nThe term \"greenfield software project\" refers\
  \ to the development of a system for a new product that requires development from\
  \ scratch with no le..."
---

Recently, I've been considering developing a complete end-to-end greenfield DevOps personal lab project. 

The term "greenfield software project" refers to the development of a system for a new product that requires development from scratch with no legacy code. 

This is a method you use when you are beginning from scratch and have no constraints or dependencies. You have a fantastic opportunity to build a solution from the ground up. The project is open to new tools and architectures.

I've been looking around the internet for ideas on how to put up a CI/CD pipeline for terraforming deployment. But I couldn't find a comprehensive end-to-end terraform deployment instruction. 

The majority of the guides and blog posts I discovered discuss the deployment pipeline for single (Prod) environments. So I've chosen to build my personal lab project and turn it into a blog post. 

In this article, I will discuss the entire Terraform deployment workflow from Development to Production environments. I will also present topics and techniques that I will be using in my lab assignment.

There are two reasons why I choose Terraform as my infrastructure as code tool. The first is that I've been using cloud formation for a long time and have a lot of experience with it, so I wanted to get some experience with Terraform. 

The second reason I chose Terraform is that this is a greenfield DevOps project, so I can pick a modern technology and play with it. 

I will go over some of the features of Terraform in this article. Let's get started.

## Deployment Tools

Before we get into deployment patterns, I'd like to go over the tools I'll be using.

### Terraform

Terraform is an open-source provisioning framework. It's a cross-platform application that can operate on Windows, Linux, and macOS. 

You can use Terraform in three ways.

* Terraform OSS (Free)
* Terraform Cloud (Paid - Saas Model)
* Terraform Enterprise (Paid - Self Hosted)

![bj3ZlORR_](https://www.freecodecamp.org/news/content/images/2022/02/bj3ZlORR_.jpeg)

### What is Terraform Cloud?

For my lab project, I'm utilizing Terraform Cloud. Terraform OSS is fantastic for small teams, but as your team expands, so does the difficulty of administering Terraform. HashiCorp's Terraform Cloud is a commercial SaaS offering.

![LvbPPn6sH](https://www.freecodecamp.org/news/content/images/2022/02/LvbPPn6sH.jpeg)

**Terraform Cloud Offerings**

* Remote Terraform workflow for teams.
* VCS Connection (GitHub, GitLab, Bitbucket) State Management (Storage, History, and Locking)
* Okta-integrated single sign-on (SSO) with a full user interface
* Terraform Cloud serves as your Terraform state's remote backend.
* Terraform Cloud incorporates the Sentinel policy-as-code framework, which lets you establish and enforce specific policies for how your business provisions infrastructure. You can limit the number of compute VMs, restrict important upgrades to predefined maintenance times, and perform a variety of other tasks.
* Terraform Cloud can show an estimate of its entire cost as well as any cost change caused by the proposed modifications.

### GitHub Actions (CI/CD)

You can use Terraform CLI or Terraform console to deploy infrastructure from your laptop. 

If you are a single team member, this may work for a while. But this strategy will not be scalable as your team grows in size. You must deploy from a centralized location where everyone has visibility, control, and rollback capabilities.

There are numerous technologies available for deployment from a centralized location (CI/CD). I intended to try Terraform pipeline deployment using the "GitOps" technique. 

A Git repository serves as the single source of truth for infrastructure definitions in GitOps. For all infrastructure modifications, GitOps use merge requests as the change method. When new code is integrated, the CI/CD pipeline updates the environment. GitOps automatically overwrites any configuration drift, such as manual modifications or errors.

For my deployment, I'll be using GitHub Actions.

GitHub Actions lets you automate tasks throughout the software development lifecycle. GitHub Actions are event-driven, which means you can run a series of commands in response to a specific event. 

For example, you can run a command that executes a testing script, plan script, and apply script every time someone writes a pull request for a repository. This allows you to incorporate continued integration (CI) and continuous deployment (CD) capabilities, as well as a variety of other features, directly in your repository.

![PC6GGaSwk](https://www.freecodecamp.org/news/content/images/2022/02/PC6GGaSwk.jpeg)

**Github Actions Features**

* Github Actions are fully integrated into Github and can be controlled alongside your other repository-related features like pull requests and problems.
* They have Docker container support
* Github Actions are available for free for all repositories and feature 2000 free build minutes per month for all private repositories.

Check out this [link](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) to get more information about the actions available on GitHub.

So far, I've introduced the tools and services that I'll use in my deployment pipeline. Now I'll look into the Terraform directory structure. 

To summarize, I will be using Terraform Cloud and GitHub Actions. Another thing to note is that I will not go into great length about writing Terraform code in this article. I'll be using code from the Terraform Registry. Thank you very much, Anton Babenko.

## Setting Up the Project

Assume you've just started a new job and your first assignment is to create VPCs. They want you to set up three VPCs for them (Dev—>Stage—>Prod VPC). You've decided to use Terraform to deploy VPCs.

### Terraform Directory Structure

Your first step should be to create Terraform's directory structure. You don't need to establish a directory structure if you've previously used cloud-formation because you don't need to handle state files or modules. But while using Terraform, it is critical to define the directory structure. 

First, I'll provide several samples of commonly used directory structures, followed by information about the directory I'll be using in my project.

**Basic Directory Structure**

![I-Yg30jok](https://www.freecodecamp.org/news/content/images/2022/02/I-Yg30jok.jpeg)

In this arrangement, you will have three files. Your major file is main.tf. This is the file in which all of the resources are defined.

```
{
  resource "aws_vpc" "this" {

  cidr_block = var.cidr
 }
}
```

variables.tf is where you define your input variables:

```
variable "cidr" {
 description = "The CIDR block for the VPC"
 type        = string
 default     = "10.0.0.0/16"
}
```

outputs.tf output values are defined in this file:

```
output "vpc_id" {
  description = "The ID of the VPC"
  value       = concat(aws_vpc.this.*.id, [""])[0]
}

```

If you're working on a modest project with a small team, this structure will work well. But as you use modules and work on larger projects, this structure will not be able to scale as well.

### Complex and Scalable Directory Structure

You will not be able to scale your project or team with the basic directory structure. 

Multiple habitats and areas will be required for the broader project. You'll need a decent directory structure to transfer infrastructure from development to production environments using a CI/CD solution. You can use Terraform Modules in this structure.

> Modules are reusable Terraform configurations that can be called and configured by other configurations.
> 

```

├── enviournments
│   ├── dev
│   │   ├── compute.tf
│   │   ├── dev.tfvars
│   │   ├── outputs.tf
│   │   ├── rds.tf
│   │   ├── s3.tf
│   │   ├── variables.tf
│   │   └── vpc.tf
│   ├── prod
│   │   ├── compute.tf
│   │   ├── outputs.tf
│   │   ├── prod.tfvars
│   │   ├── rds.tf
│   │   ├── s3.tf
│   │   ├── variables.tf
│   │   └── vpc.tf
│   └── stage
│       ├── compute.tf
│       ├── outputs.tf
│       ├── rds.tf
│       ├── s3.tf
│       ├── stage.tfvars
│       ├── variables.tf
│       └── vpc.tf
└── modules
    ├── compute
    │   ├── main.tf
    │   ├── outputs.tf
    │   └── variables.tf
    ├── rds
    │   ├── main.tf
    │   ├── outputs.tf
    │   └── variables.tf
    ├── s3
    │   ├── main.tf
    │   ├── outputs.tf
    │   └── variables.tf
    ├── security-group
    │   ├── main.tf
    │   ├── outputs.tf
    │   └── variables.tf
    └── vpc
        ├── main.tf
        ├── outputs.tf
        └── variables.tf
```

I've noticed a lot of projects use this structure. In this case, the contents of each environment will be nearly identical. 

But in my opinion, content should be the same across all environments. For all environments, we should use the same main.tf file. Variables can be used to adjust the number of servers or number of subnets.

```
variable "instance_count" {
  description = "Numbers of servers count"
}

variable "instance_type" {
  description = "Instance Size (t2.micro,t2.large"
}

```

**Proposed Directory Structure**

Having a separate folder and separate configuration file, as I described in the prior section, makes little sense. You can get in touch if you believe there is an advantage to having a different folder for each setting. 

As a result, below is my proposed directory layout for VPC deployment.

VPC: github.com/nitheesh86/network-vpc

Security Group: github.com/nitheesh86/network-sg

Compute-ASG: github.com/nitheesh86/compute-asg

You may be wondering how you will reference resources from multiple repositories. This is where Terraform cloud workspace will come in handy. I'll go through this in more detail later in the article.

If you look at the above directory, you might assume it looks like a "Basic Directory Structure." You may also be asking where module directories are. Yes, directories seem the same, but the magic happens within the configuration files.

```
terraform {
  required_version = "~> 0.12"
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "xxxxxxxx"
    workspaces { prefix = "vpc-" }
  }
}

provider "aws" {
  region = "ap-south-1"
}


module "vpc" {
  source = "github.com/nitheesh86/terraform-modules/modules/vpc"

  name = var.name
  cidr = "10.0.0.0/16"

  azs             = ["ap-south-1a", "ap-south-1b", "ap-south-1c"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform   = "true"
    Environment = var.env
  }
}

```

I maintained modules separate from setups. My modules are all placed in a separate repository. I'll refer to that module by its Git repo URL.
> The source argument in a module block tells Terraform where to find the source code for the desired child module.
> 

Terraform supports sources in the following modules:

* Local paths
* Terraform Registry
* GitHub
* Bitbucket
* Generic Git, Mercurial repositories
* HTTP URLs
* S3 buckets
* GCS buckets

We can use the Terraform registry as a module source because we are using Terraform Cloud. However, each module needs its own git repository. If you're publishing vpc modules (terraform-aws-vpc), for example, you can only provide code for those vpc resources that are relevant to the module. Another repo is needed for the security group module (terraform-aws-sg).

> One module per repository. The registry cannot use combined repositories with multiple modules.
> 

However, it is worth considering this structure if your organization has a separate network, security, and compute team. Each team can handle their modules independently.

## Terraform Cloud Components

### Organizations

Organizations are a shared place in Terraform Cloud for teams to collaborate on workspaces. Remote state setups can be shared between organizations. 

You can, for example, build companies based on a project or a product. Like if you are attempting to create an Apple product, you can name it "apple." "nitheeshp" is the name I gave to my project.

![KR3DCPRWz](https://www.freecodecamp.org/news/content/images/2022/02/KR3DCPRWz.jpeg)

### WorkSpaces

Instead of directories, Terraform Cloud maintains infrastructure collections using workspaces. A workspace is related to contexts such as dev, staging, and prod. 

Terraform configurations, variable values, and state files connected with an environment are all stored in the workspace. Each workspace keeps backups of earlier state files.

In my project, I set up a workspace for each Amazon Web Services service. Each workspace can be linked to a Git branch or Git repo.

![ncNrBPUb7](https://www.freecodecamp.org/news/content/images/2022/02/ncNrBPUb7.jpeg)

When you create a workspace, you have three options for designing your Terraform workflow:

* Version Control Workflow
* CLI-Driven Workflow
* API-Driven Workflow

![wsGudB1Pa](https://www.freecodecamp.org/news/content/images/2022/02/wsGudB1Pa.jpeg)

If you look at my Terraform directory structure below, you'll notice that I haven't set any default values for my variables. Variables have been related in Terraform workspace settings.

![GbQMtKo2F](https://www.freecodecamp.org/news/content/images/2022/02/GbQMtKo2F.jpeg)

If you look at main.tf, you'll notice that all environments use the same Terraform cloud-config. You may be curious as to how I go about making modifications to a certain workspace. The workspace prefix is what I'm using.

```
terraform {
  required_version = "~> 0.12"
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "nitheeshp"
    workspaces { prefix = "vpc-" }
  }
}
```

When you add a workspace to your configuration, it will prompt you to choose a workspace. As an example:

```
$ terraform init

Initializing the backend...

Successfully configured the backend "remote"! Terraform will automatically
use this backend unless the backend configuration changes.

The currently selected workspace (default) does not exist.
  This is expected behaviour when the selected workspace did not have an
  existing non-empty state. Please enter a number to select a workspace:

  1. dev
  2. stage
  3. prod

  Enter a value:

```

Set the TF WORKSPACE environment variable to the workspace name you want to be selected when using Terraform in CI/CD.

```
export TF_WORKSPACE="dev"`
```

### How to Deploy Security Groups

As previously stated, I deploy security groups using a separate repo and workspace. A VPC id is required for the deployment of security groups. This is where Terraform data sources come in.

> Data sources allow data to be fetched or computed for use elsewhere in Terraform configuration. The use of data sources allows a Terraform configuration to make use of information defined outside of Terraform, or defined by another separate Terraform configuration.
> 

```
data "terraform_remote_state" "vpc" {
  backend = "remote"

  config = {
    organization = "nitheeshp"
    workspaces = {
     name = "vpc-${var.env}"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}


module "elb_sg" {
  source = "terraform-aws-modules/security-group/aws"

  name        = "${var.env}-elb-sg"
  description = "elb security group."
  vpc_id      = data.terraform_remote_state.vpc.outputs.vpc_id

  egress_with_cidr_blocks = [
    {
      from_port   = 0
      to_port     = 65535
      protocol    = "all"
      description = "Open internet"
      cidr_blocks = "0.0.0.0/0"
    }
  ]

```

As you can see, I'm getting the VPC id from the vpc-dev workspace.

```
vpc_id      = data.terraform_remote_state.vpc.outputs.vpc_id
```

### GitHub Actions

As we discussed above, we'll also use GitHub Actions in our deployment pipeline.

![3Xxi80ooR](https://www.freecodecamp.org/news/content/images/2022/02/3Xxi80ooR.png)

GitHub Actions makes it simple to automate all of your CI/CD workflows. You can build, test, and deploy code directly from your GitHub repository. You can also make code reviews, branch management, and issue triaging the way you want them to function. Github Actions offers free plans.

![eD4NRbeS-g](https://www.freecodecamp.org/news/content/images/2022/02/eD4NRbeS-g.jpeg)

## GitOps and Terraform WorkFlow

![3Wg3lPnMu](https://www.freecodecamp.org/news/content/images/2022/02/3Wg3lPnMu.jpeg)

* Each service has its own repository (Network-VPC, Network-Security Groups, Compute-ASG, Compute-EC2)
* I've made three branches (Develop, Stage and Prod). Each branch reflects one of our actual infrastructure environments or workplace terraforms.
* Workflow begins when the DevOps engineer begins to make modifications to the infrastructure.
* A DevOps engineer develops a feature branch from the master (production) branch
* Make your changes and submit a pull request to the branch's development team.

I made a separate workflow for each branch (terraform-develop.yml,terraform-stage.yml,terraform-prod.yml). The workflow is a procedure that you add to your repository. 

Workflows consist of one or more jobs that can be scheduled or triggered by an event. You can use the workflow to create, test, package, release, or deploy a GitHub project.

GitWorkFlow will:
* Check out feature branch code.
* Check for syntax.
* Initialise Terraform.
* Generate a plan for every pull requests.
* When a pull request is merged with the develop branch, it deploys the resources to the development environment.
* Deploy the changes Development Branch.
* Again create pull requests to stage branch and same to prod branch.

Here are the GitHub repos for this project if you want to take a look:

* github.com/nitheesh86/network-vpc
* github.com/nitheesh86/network-sg
* github.com/nitheesh86/terraform-modules

I would love to learn more about your Terraform deployment methods. Please get in touch with me if you'd like to share them and discuss further.



