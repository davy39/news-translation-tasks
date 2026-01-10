---
title: AWS CLI Tutorial – How to Install, Configure, and Use AWS CLI to Understand
  Your Resource Environment
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-05-11T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/aws-cli-tutorial-install-configure-understand-resource-environment
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/keyboard.png
tags:
- name: AWS
  slug: aws
- name: aws cli
  slug: aws-cli
- name: Cloud Computing
  slug: cloud-computing
- name: cloudformation
  slug: cloudformation
seo_title: null
seo_desc: 'How to get exactly the account and environment information you need to
  manage your AWS account using just the AWS CLI

  Installing the AWS CLI is actually quite simple. The best way to get it done is
  to head over to the AWS installation guide and follo...'
---

_How to get exactly the account and environment information you need to manage your AWS account using just the AWS CLI_

Installing the AWS CLI is actually quite simple. The best way to get it done is to head over to the [AWS installation guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and follow instructions for your OS. 

Right now they're pushing us towards version 2 of the CLI and I haven't seen any reason not to go along. I'm working with Linux so that's where I'd head next.

To get it done, I'll paste the curl command from the Amazon page into my Linux shell that'll download the package and write it to a local zip file, which I'll then unzip. That'll create a new directory called aws that'll contain a install script, which I can run using sudo to get admin privileges. I'll run aws --version to confirm everything worked as it was supposed to.

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
ls aws
sudo ./aws/install
aws --version

```

The next step will require one quick trip to the management console. You see, to authenticate the CLI to your account you'll need a valid access key. Now, the CLI has a "create-access-key" command that'll generate a new key, but that's only possible once I've authenticated. I'm sure you understand the problem with that.

You access the security credentials page from the drop-down account menu at the top of any page on the console. With your credentials in hand, you can run "aws configure." You'll be prompted to enter your access key ID and the secret key itself. If you like you can then choose a default AWS region and output format. The format won't be an issue so I'll leave it as default.

```
aws configure

```

That's it. Just to confirm it all worked, I'll list all the S3 buckets in my account. With that, we'll all set to get down to work in the next clip.

```
aws s3 ls

```

You may already know that Amazon's CloudFormation service exists to let you manage your application infrastructure by organising it into stacks of your AWS account resources.

The CloudFormation templates that define those stacks can be shared, edited, and launched anywhere, giving you predictable and reliable cloud application environments wherever and whenever you need them. 

You may also know that you can mange your CloudFormation stacks both through the AWS Management Console and, as I discuss in my [new Pluralsight course, Create and Manage Stacks with AWS CloudFormation Using the Command Line Interface](https://pluralsight.pxf.io/EMPE2), using the AWS CLI.

If you do choose to go with the AWS CLI – something I highly recommend – you'll need a way to gather key information about other account resources. But how you're expected to get that information through the CLI might, at first, not appear so obvious.

To show you what I mean, let's experiment with a more complex stack using a template that comes from the AWS documentation samples.

The [Application Frameworks template set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-appframeworks-us-east-1.html) includes a template for auto scaled Linux servers that will come pre-provisioned with the Apache web server and the PHP scripting language, and a connection to a Multi-AZ RDS database instance running the MySQL database engine.

You can click View from that AWS documentation page and take a look at the template itself. There you'll see Parameters sections defining the VPC and subnets into which your instance will launch and the MySQL database name, user, and password. 

It's critical that all the right services know those details because, otherwise, they won't be able to talk to each other. We'll have to figure out a way to add those values. To get things going, you can simply click to view the template ([which you can see here](https://s3.amazonaws.com/cloudformation-templates-us-east-1/LAMP_Multi_AZ.template)), and copy the contents, pasting it into a new JSON file on your local machine.

You use the CLI to fire up a Cloudformation stack using the create-stack command. The command, however, takes a few arguments to pass important information. This minimal example shows you how to point CloudFormation to your JSON template file, a name to assign to your stack, and a valid SSH key so I'll be able to log into the instance it creates.

```
aws cloudformation create-stack \
  --template-body file://lamp-as.json \
  --stack-name lamp \
  --parameters \
  ParameterKey=KeyName,ParameterValue=mykey

```

The problem is that, if you were to run that command against the template in your JSON document, it would fail. That's because, as you'll no doubt remember from looking through the template, there are some extra parameters that need satisfying. Specifically, we'll need references to a VPC and to two subnets - and because this is a multi-availability-zone deployment, they'll need to be in different zones.

How will that work? It's the AWS CLI to the rescue. Need a VPC ID? Keeping in mind that VPCs are EC2 objects, you can run aws ec2 describe-vpcs and all the data you'll need - including the VPC ID - will magically appear. And subnets? Well more of the same, obviously. Just copy subnet IDs for any two of the subnets that will appear and you're in business.

```
aws ec2 describe-vpcs
aws ec2 describe-subnets

```

Now let's put all that information together into our new version of the create-stack command. You'll need to be careful with this as there are some nasty gotchas in the syntax.

```
aws cloudformation create-stack \
  --template-body file://lamp-as.json \
  --stack-name lamp-as \
  --parameters \
  ParameterKey=KeyName,ParameterValue=mykey \
  ParameterKey=VpcId,ParameterValue=vpc-1ffbc964 \
  ParameterKey=Subnets,ParameterValue=\'subnet-0e170b31,subnet-52d6117c\' \
  ParameterKey=DBUser,ParameterValue=myadmin \
  ParameterKey=DBPassword,ParameterValue=mypass23

```

The first new parameter is VPC-ID. But make sure you get the case right: using an uppercase D in Id will cause the whole thing to fail. I don't know why they make things so difficult to live with, but that's what we've got.

The next one is even more delicate. Since we need two subnets, we'll need to enter them on a single line separated by a comma - but no space. However, we'll also need to enclose the string within single apostrophes. But the CLI can't read apostrophes just like that, so we'll need to escape them using backslashes. Got that? 

I'll also add those two database parameters: DBUser and my ultra secret, super cryptic DBPassword. Will it work? You betcha. But don't tell anyone how many times I had to try this without you watching before I got it right. Remember: failure is your friend.

When our stack is good and launched (which could take as long as half an hour), running describe-stacks will give us our website URL.

```
aws cloudformation describe-stacks

```

But that's not the whole story.  I'm going to use another aws ec2 command - describe-instances this time - to get some information about the EC2 instances that were launched as part of this stack. This one will filter results, restricting output to only those instances that are currently running. 

```
aws ec2 describe-instances \
  --filters Name=instance-state-name,Values=running \
  --query 'Reservations[*].Instances[*].{Instance:InstanceId,PublicIPAddress:PublicIpAddress}'

```

I happen to have no other instances running in this region, so only the CloudFormation instances will show up. Now I use --query to further filter the output to give me only the Instance IDs and public IP addresses of those instances. There are, as you would expect, exactly two running.

Just a taste - and most of it related specifically to CloudFormation - but I think you get the idea of how information gathering works using the AWS CLI.

_There's much more administration goodness in the form of books, courses, and articles available at my [bootstrap-it.com](https://bootstrap-it.com)._ 

