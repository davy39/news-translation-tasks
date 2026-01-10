---
title: 'AWS CloudFormation: Where to Find Help When You Need It'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-05-18T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/aws-cloudformation-where-to-find-help
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/automation.jpg
tags:
- name: AWS
  slug: aws
- name: aws cli
  slug: aws-cli
- name: cloudformation
  slug: cloudformation
seo_title: null
seo_desc: "Staring at a plain, dumb command line prompt with no clue what to do with\
  \ the AWS CLI next can be a humbling experience. And, in my experience at least,\
  \ staring at the Management Console for AWS CloudFormation can be worse. \nSo let\
  \ me offer you some ..."
---

Staring at a plain, dumb command line prompt with no clue what to do with the AWS CLI next can be a humbling experience. And, in my experience at least, staring at the Management Console for AWS CloudFormation can be worse. 

So let me offer you some quick "getting started" help based on part of the content in [my latest Pluralsight course](https://pluralsight.pxf.io/EMPE2). 

First of all, if you're planning to manage your CloudFormation stacks through the AWS CLI rather than the Management Console, I discuss the basics in [this article](https://www.freecodecamp.org/news/aws-cli-tutorial-install-configure-understand-resource-environment/). Once that's all taken care of, you'll be ready for anything. 

Start simple: 

```
$ aws s3 ls
2019-11-03 13:16:59 athena5905
2019-02-03 18:01:42 book-3939
2014-07-01 18:52:32 elasticbeanstalk-ap-northeast-1-426397493112
2014-08-28 16:57:49 elasticbeanstalk-us-east-1-426497493912
2019-05-04 22:17:50 ltest236
2018-07-15 15:52:30 mybucket99688223
2017-07-25 17:06:43 nextcloud3239027
```

"aws" in that example tells your shell that you want what comes next to be handled by the AWS CLI. The "s3" I type next tells the CLI that I'll be using the S3 service - that's Amazon's Simple Storage Service. Finally, "ls" or "list" is the command I'd like to run against that service. 

The CLI, using the account authentication variables that the configure tool added to my environment, will now hurry off and access my account, in this case retrieving the names of all of my buckets.

Predictably, you tell AWS that you're looking to work with CloudFormation using "cloudformation." If I just run that without specifying a command, I'll get an error message:

```
aws cloudformation
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
aws: error: the following arguments are required: operation

```

But it's an important message, as it tells us how to access the inline documentation. Context-sensitive help is available at each layer. 

See what happens if you add "help" after "cloudformation". You'll get a brief description and then a list of all the available subcommands. 

```
$ aws cloudformation help

CLOUDFORMATION()                                              CLOUDFORMATION()
NAME
       cloudformation -
DESCRIPTION
AWS  CloudFormation  allows you to create and manage AWS infrastructure deployments predictably and repeatedly. You can use AWS  CloudFormation to  leverage AWS products, such as Amazon Elastic Compute Cloud, Amazon Elastic Block Store, Amazon Simple Notification Service,  Elastic  Load Balancing,  and Auto Scaling to build highly-reliable, highly scalable, cost-effective applications without creating or configuring the  underlying AWS infrastructure.
With  AWS  CloudFormation, you declare all of your resources and dependencies in a template  file.  The  template  defines  a  collection  of resources  as  a single unit called a stack. AWS CloudFormation creates and deletes all member resources of the stack together and manages  all dependencies between the resources for you.
For  more information about AWS CloudFormation, see the AWS CloudFormation Product Page.
Amazon CloudFormation makes use of other  AWS  products.  If  you  need additional  technical information about a specific AWS product, you can find the product's technical documentation at docs.aws.amazon.com.

AVAILABLE COMMANDS
       o cancel-update-stack
       o continue-update-rollback
       o create-change-set
       o create-stack
       o create-stack-set
       o delete-change-set
       o delete-stack
       o delete-stack-instances
       o delete-stack-set
       o deploy
       o describe-account-limits
       o describe-change-set
       o describe-stack-events
       o describe-stack-instance
       o describe-stack-resource
       o describe-stack-resources
       o describe-stack-set
       o describe-stack-set-operation
       o describe-stacks
       o estimate-template-cost
       o execute-change-set
       o get-stack-policy
[...]
```

Now run the "describe-stacks" command. There are probably no live stacks in your account right now so you won't see any output. 

But do that again, this time adding "help". This one will show you some options that'll let you filter or manipulate the data you get back. You could, for instance, point the CLI to one specific stack by using "--stack-name" followed by the name of an existing stack.

```
$ aws cloudformation describe-stacks
$ aws cloudformation describe-stacks help
NAME
       describe-stacks -
DESCRIPTION
       Returns  the  description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.
       NOTE:
          If the stack does not  exist,  an  AmazonCloudFormationException  is returned.
       See also: AWS API Documentation
       See 'aws help' for descriptions of global parameters.
       describe-stacks  is  a  paginated  operation. Multiple API calls may be issued in order to retrieve the entire data set  of  results.  You  can disable pagination by providing the --no-paginate argument.  When using --output text and the --query argument on  a  paginated  response,  the --query  argument  must  extract data from the results of the following query expressions: Stacks

SYNOPSIS
            describe-stacks
          [--stack-name <value>]
          [--cli-input-json <value>]
          [--starting-token <value>]
          [--max-items <value>]
          [--generate-cli-skeleton <value>]

OPTIONS
       --stack-name (string)
          The name or the unique stack ID that is associated with  the  stack,
          which are not always interchangeable:
[...]

$ aws cloudformation describe-stacks --stack-name myname

```

Those are tools that'll help you no matter what AWS service you're using. But looking specifically at CloudFormation, there are some valuable official collections of sample templates you should know about. JSON or YAML syntax being what they are, you probably won't want to start from an empty document. 

Amazon itself has done a great job creating templates for us to work with. Your first stop should be the [AWS CloudFormation Templates page](https://aws.amazon.com/cloudformation/resources/templates/). Here you'll find links to snippets and specific application frameworks and some more cutting edge content. 

But right now I'd like to draw your attention to one of the "sample templates" organized by AWS service (this code comes from one of the [Amazon EC2 examples](https://s3.us-west-2.amazonaws.com/cloudformation-templates-us-west-2/EC2InstanceWithSecurityGroupSample.template)). 

The template begins with a free form description that helpfully tells us what kind of stack this will generate. We're also told that we could customize the template by using an existing Elastic IP address instead of one that's automatically generated. 

```
{
  "AWSTemplateFormatVersion" : "2010-09-09",

  "Description" : "AWS CloudFormation Sample Template EC2InstanceWithSecurityGroupSample: Create an Amazon EC2 instance running the Amazon Linux AMI. The AMI is chosen based on the region in which the stack is run. This example creates an EC2 security group for the instance to give you SSH access. **WARNING** This template creates an Amazon EC2 instance. You will be billed for the AWS resources used if you create a stack from this template.",

```

You'll need to pass in the name of an existing KeyPair from the current region in your AWS account so you'll be able to open remote SSH into the Linux instance that will be launched. You can alternatively pass along that value from the command line.

The Parameters section is also where you define the EC2 instance type. The default is t2.small, but we'd be allowed to either swap that value out for any of the other AllowedValues in this document, or override it from the command line. 

```
  "Parameters" : {
    "KeyName": {
      "Description" : "Name of an existing EC2 KeyPair to enable SSH access to the instance",
      "Type": "AWS::EC2::KeyPair::KeyName",
      "ConstraintDescription" : "must be the name of an existing EC2 KeyPair."
    },

    "InstanceType" : {
      "Description" : "WebServer EC2 instance type",
      "Type" : "String",
      "Default" : "t2.small",

```

If you scroll down through the Mappings section, we can see long lists of available hardware architectures and Amazon Machine Image identifiers for each region. 

This is an optional section where you can insert your own non-standard values so, say, an image type would be launched based on a particular set of parameters - perhaps even a private AMI image. Such data is organized into key/value pairs. 

```
  "Mappings" : {
    "AWSInstanceType2Arch" : {
      "t1.micro"    : { "Arch" : "HVM64"  },
      "t2.nano"     : { "Arch" : "HVM64"  },
      "t2.micro"    : { "Arch" : "HVM64"  },

```

The Resources section in this case defines your instance environment. The SecurityGroup, for instance, is configured to open the SSH port 22 but nothing else. The instance's public IP address is also associated with the new Elastic IP address that will be allocated. 

```
    "InstanceSecurityGroup" : {
      "Type" : "AWS::EC2::SecurityGroup",
      "Properties" : {
        "GroupDescription" : "Enable SSH access via port 22",
        "SecurityGroupIngress" : [ {
          "IpProtocol" : "tcp",
          "FromPort" : "22",
          "ToPort" : "22",
          "CidrIp" : { "Ref" : "SSHLocation"}
        } ]
      }
    }
  },

```

One more important Amazon resource: [Quick Starts](https://aws.amazon.com/quickstart/?quickstart-all.sort-by=item.additionalFields.updateDate&quickstart-all.sort-order=desc). Strictly speaking the pre-built infrastructure stacks that are provided here to help you create more complex cloud deployments aren't directly related to CloudFormation. They were provided by third-party companies to simplify the process of building their infrastructure in within the AWS platform. 

But the fact is that each one starts with its own unique CloudFormation template. Clicking through to look at actual examples will often lead you to the stack source code templates within a GitHub repo. [This example](https://github.com/aws-quickstart/quickstart-hashicorp-consul) shows us the tools you'd need to fire up a HashiCorp Console:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-from-2020-05-17-13-06-37.png)

Either way, feel free to use these templates as learning tools - or browse through the selection to see if there's a stack there that happens to fit your needs.

_There's much more administration goodness in the form of books, courses, and articles available at my [bootstrap-it.com](https://bootstrap-it.com/)._

