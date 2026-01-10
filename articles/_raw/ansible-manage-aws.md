---
title: How to Use Ansible to Manage Your AWS Resources
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-10-28T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/ansible-manage-aws
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/jean_victor_balin_icon_monitoring-1.png
tags:
- name: ansible
  slug: ansible
- name: AWS
  slug: aws
- name: Orchestration
  slug: orchestration
seo_title: null
seo_desc: "Wouldn't you love to be able to simply wave a wand and layers of resources\
  \ in your AWS account would suddenly - and magically - spring to perfectly configured\
  \ life, ready to meet your complex infrastructure needs? \nIf you already have experience\
  \ with..."
---

Wouldn't you love to be able to simply wave a wand and layers of resources in your AWS account would suddenly - and magically - spring to perfectly configured life, ready to meet your complex infrastructure needs? 

If you already have experience with AWS, then you know how much of a pain it can be to work through web page after web page in the Amazon management console as you manually provision services. And even the AWS CLI - which is a huge step up - can add its own complexity and effort to the mix.

That's not to say that AWS itself doesn't address the problem with their own class of powerful orchestration tools, including CloudFormation and their Elastic Kubernetes Service (something I address at length in [my "Using Docker on AWS" course at Pluralsight](https://pluralsight.pxf.io/nZgKx)). But neither of those options lives quite so close to your existing infrastructure - or uses as familiar a way of operating - as Ansible. 

If you're already using Ansible for your on-premises operations, plugging it into your AWS account can sometimes be the quickest and most painless way to migrate operations to the cloud.

### Understanding the Ansible/AWS Advantage

My book "[Manage AWS Resources Using Ansible](https://www.amazon.com/gp/product/B07YK42ZH1/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07YK42ZH1&linkCode=as2&tag=projemun-20&linkId=d90b5a553223444f00992afa4c8f8d16)" - from which this article is excerpted - is designed to quickly introduce you to applying Ansible's _declarative_ approach to working with AWS resources. Being able to "declare" the precise configuration results you want and then produce them by getting Ansible to read a playbook is Ansible's magic wand. When properly planned, it's amazing how simple it can be to execute complex, layered AWS deployments.

Before we launch a simple "Hello World" Ansible playbook, let's first make sure you've got a properly-configured working environment through which Ansible can communicate with all its new friends in your AWS account.

### Preparing a Local Environment

As you probably already know, Ansible is an orchestration tool that lets you write plain-text _playbook_ files that _declare_ the software profile and ideal state you'd like applied to a target server. Those servers - known as hosts - can be provisioned for just about any digital workload you can imagine, using just about any combination of application software, and running on just about any platform.

In the good old days, when a playbook was run against a physical server, Ansible would employ an existing SSH connection to securely login to the remote host and go about building your application. But that won't work for AWS workloads. You see, because the EC2 instances and other infrastructure you want to launch don't yet exist, there can be no "existing" SSH connections. Instead, Ansible will use Boto 3 - the software development kit (or SDK) used by AWS that allows Python code to communicate with the AWS API.

### Using the AWS CLI to Connect Ansible

You don't have to know how all that works, but it has to be there so it _can_ work. For that reason you're going to install the AWS command line interface (CLI). We won't be using the CLI itself for anything important, but installing it will give us all the dependencies we'll need. You can find out how to make this work on the latest version of whatever OS you're using from the [AWS documentation page](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

Working with the Python package manager, PIP, is a popular way to get all this done. Here's how you would install PIP itself and then the AWS CLI on an Ubuntu machine:

```
sudo apt update
sudo apt install python3-pip
pip3 install awscli
```

I should note that, as I write this, Python 2 is still alive...but only just. So there might sometimes still be separate Python 2 and Python 3 versions installed on your system. Since Python 2 will soon be fully deprecated, you probably won't have to worry about specifying python3 or pip3 with your commands: that should be automatic.

Once the CLI is installed, run `aws configure` and enter your AWS access key ID and secret access key.

```
aws configure
cat .aws/credentials
```

You can get keys from the Your Security Credentials page in the AWS Management Console. Here's how those keys will look (don't get any naughty ideas, these aren't valid):

```
AccessKeyId: AKIALNZTQW6H3EFBRLHQ
SecretAccessKey: f26B8touguUBELGpdyCyc9o0ZDzP2MEUWNC0JNwA
```

Just remember that a pair of keys issued to the root user of your AWS account provides full access to your entire AWS account. Anyone in possession of those credentials would be quickly able to run up six and even seven figure services charges, so be _very_ careful how you use and store them. Ideally, you would be better off limiting your risk exposure by creating an admin user in the AWS Identify and Access Management (IAM) service with limited powers and using a key issued to that user.

At any rate, why am I doing this? The value of populating my AWS credentials file is that Ansible is smart enough to look for it and, if no other authentication keys are available in the system environment, it'll use these. You'll soon see how mighty convenient that will be. However, you should be aware of other ways to manage authentication for Ansible playbooks, like using _ansible-vault_ or by creating and then invoking an aws_keys.yml file. But one thing you should definitely NOT do is hardcode the keys in your playbook files - especially if you plan to push them to an online repository like GitHub. I'll quickly test the CLI to make sure we can properly connect to AWS. This simple command will list any S3 buckets I happen to have within this account.

```
aws s3 ls
```

We're now ready to install ansible. I'll go with pip3 for that. I could use the regular Ubuntu apt repository just as easily, but it will most likely install a slightly older version. Depending on your network connection, that'll take a minute or two, but I'll skip most of that.

```
$ pip3 install ansible

```

I'll confirm that it's properly installed by running ansible --version. This shows us the version that was built, that configured Ansible modules will, by default, be saved in either one of these two locations in the file system, that other modules would be available here and - most importantly - that the Ansible executable is located within the /local/bin/ directory beneath my user's home directory. My user here, by the way, is called ubuntu. You can also see that we're using a nice, up-to-date version of Python 3.

```
$ ansible --version
ansible 2.8.5
  config file = None
  configured module search path = 
    ['/home/ubuntu/.ansible/plugins/modules', 
    '/usr/share/ansible/plugins/modules']
  ansible python module location = 
    /home/ubuntu/.local/lib/python3.6/site-packages/ansible
  executable location = /home/ubuntu/.local/bin/ansible
  python version = 3.6.8 (default, Aug 20 2019, 17:12:48) [GCC 8.3.0]

```

One more step. As I mentioned earlier, Ansible will connect to AWS using the boto SDK. So we'll need to install the boto and boto 3 packages. I'll go with PIP for this one, too.

```
$ pip3 install boto boto3

```

Once that one has been brought on board, we'll be ready to get some real stuff done. That'll begin in the next section.

## Testing Ansible with a Simple Playbook

This is going to be very simple proof of concept demo. I'll create a couple of files, walk you through the syntax, and then fire it up. First off, I'll use any plain text editor to create a _hosts_ file. Normally, the hosts file tells Ansible where it can find the remote servers you want to provision. But since, in the case of AWS, the resources that will be our hosts don't yet exist, we'll simply point Ansible to localhost and boto will handle connections behind the scenes. Here's what the contents of that file will look like:

```
[local]
localhost

```

Next, I'll create a playbook file that I'll call test-ansible.yml. The yml extension, of course, indicates that this file must be formatted using YAML markup language syntax. As you can see from the file text I've pasted just below, that'll begin with three dashes marking the start of the file and then an indented dash introducing a set of definitions. The value of "hosts" could be one or more remote computers but, as I've said, we'll leave that up to the local system to figure out. The same goes for our connection.

The next section includes the _tasks_ we want Ansible to perform. This one will use the aws_s3 module to _create_ a new bucket on Amazon's S3 Simple Storage Service in the us-east-1 region. I have to give it this ugly name because S3 buckets require globally unique names - if a name you choose clashes with any one of the countless millions of names already out there, the operation will fail.

```yaml
---
  - name: Test s3
    hosts: local
    connection: local

    tasks:
      - name: Create new bucket
        aws_s3:
          bucket: testme817275b
          mode: create
          region: us-east-1

```

I run the playbook by calling the ansible-playbook command using -i to specify the hosts file, and then pointing to the test.yml file. Ansible should give us some feedback in just a moment or two. If we're successful, you'll see "0" as the value of "failed" and at least "1" as the value of "ok".

```
$ ansible-playbook -i hosts test-ansible.yml
PLAY [Test s3] ******************************************************

TASK [Create new bucket] ********************************************

changed: [localhost]

PLAY RECAP **********************************************************
localhost: ok=1    changed=1    unreachable=0    failed=0   skipped=0
    rescued=0    ignored=0 

```

If I check my list of buckets once more, I should - and do - see the new one:

```
$ aws s3 ls
2018-12-30 15:19:24 elasticbeanstalk-us-east-1-297972716276
2018-10-12 04:09:37 mysite548.com
2019-09-24 15:53:26 testme817275b

```

That's a very brief intro to setting up an Ansible environment. We saw how using Ansible with Amazon's automatically provisioned resources is going to work differently than it would with traditional Ansible hosts. You're going to require a different set of authentication and inventory control tools. We walked through the process of setting up an Ansible environment and connecting it to AWS, and then running a simple playbook. Short and sweet.

This article comes from my book "[Manage AWS Resources Using Ansible](https://www.amazon.com/gp/product/B07YK42ZH1/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07YK42ZH1&linkCode=as2&tag=projemun-20&linkId=d90b5a553223444f00992afa4c8f8d16)". There's more technology goodness - in the form of books, courses, and articles - available on my [website, bootstrap-it.com](https://bootstrap-it.com). 

