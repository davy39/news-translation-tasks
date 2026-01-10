---
title: How to manage Lambda VPC cold starts and deal with that killer latency
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T22:27:53.000Z'
originalURL: https://freecodecamp.org/news/lambda-vpc-cold-starts-a-latency-killer-5408323278dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*16yC8qApBwQirGLItTPtjA.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nathan Malishev

  All serverless computing suffers from the dreaded “cold start”, and AWS Lambda is
  no different. I’ve explored cold starts before in a previous article. But what is
  not common knowledge is how using Lambda in conjunction with a Virt...'
---

By Nathan Malishev

All serverless computing suffers from the **dreaded** “**cold start”,** and [AWS Lambda](http://aws.amazon.com/lambda/) is no different. I’ve explored [cold starts](https://medium.com/@nathan.malishev/lambda-cold-starts-language-comparison-️-a4f4b5f16a62) before in a previous article. But what is not common knowledge is how using Lambda in conjunction with a Virtual Private Cloud affects latency. From [various](https://www.reddit.com/r/aws/comments/6lfubn/aws_lambda_vpc_redis_slow/) [reports](https://forums.aws.amazon.com/thread.jspa?threadID=231069) [around](https://www.reddit.com/r/aws/comments/7gpd53/lambda_rds_incredibly_slow/) [the web](https://www.robertvojta.com/aws-journey-api-gateway-lambda-vpc-performance/), cold starts within VPCs could add **up to 10 seconds of latency!** ?

### **Background**

**AWS Lambda and serverless computing** are shifting the paradigm of computing by having code executed on demand. And yes, that means you only pay for when your code is executing! ?

The serverless **cold start** is the first time your code is being executed by your cloud provider, and requires it to be downloaded, containerised, booted, and primed to be run. This can add significant overhead — **up to 1.5s of latency**!

But good news: these cold starts are expected to be outliers, only affecting 5% of executions. So, while they don’t happen all the time, they are important to think about when designing your application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HsUccdkDffywiUjM7AYdFw.png)
_[Regular cold start](https://youtu.be/oQFORsso2go?t=8m5s" rel="noopener" target="_blank" title=") (screenshot from the video)_

**Virtual Private Cloud (VPC)** is a private network in which you strictly control the inbound and outbound network traffic. They are widely used and, traditionally, you would run your databases and servers securely behind your VPC, only exposing a load balancer. If you have strict security requirements or services already behind a VPC to which you need access, you might have to deploy your Lambda functions in a VPC.

The added complexity of having a Lambda function live inside a VPC introduces new latencies. These latencies are due to creating an Elastic Network Interface and then waiting for Lambda to assign itself that IP. Also be careful, each Lambda function requires an IP address and you don’t want to run out!

![Image](https://cdn-media-1.freecodecamp.org/images/1*FCpFITtI7oxassyWOQdrKw.png)
_[Cold Start within a VPC](https://youtu.be/oQFORsso2go?t=41m49s" rel="noopener" target="_blank" title=") (screenshot from the video)_

This is extra networking overhead that you can’t do anything about, except to avoid the VPC in the first place. So, just how bad is it?

### Setup

To test the affect of the VPC and cold starts, I created two nearly identical [CloudFormation](https://aws.amazon.com/cloudformation/) stacks.

**CloudFormation is infrastructure as code**, that is natively supported by AWS. You may have heard of similar products like Terraform or Ansible, which are great alternatives. The great advantage of CloudFormation is the tight integration with AWS and its [intrinsic functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html).

[**AWS Sam**](https://github.com/awslabs/serverless-application-model) is an awesome extension of CloudFormation, which greatly reduces the complexity of deploying a Lambda function. It ties multiple cloud-formation resources together, so you don’t have to separately manage them to deploy a Lambda function. It also eases the deployment process, by zipping and deploying your code to S3 seamlessly. It also features [**built in canary deployments**](https://docs.aws.amazon.com/lambda/latest/dg/automating-updates-to-serverless-apps.html)! But there are great alternatives like [serverless](https://serverless.com/), if being cloud agnostic is your thing.

This article isn’t about CloudFormation and Sam. but if you would like to see one, leave a comment :)

![Image](https://cdn-media-1.freecodecamp.org/images/0*teE_0mjhNDaQCTRz.png)
_[AWS Sam](https://github.com/awslabs/serverless-application-model" rel="noopener" target="_blank" title=") is awesome!_

My two stacks are both CloudFormation stacks with the AWS Sam extension. They both feature a simple read and write function, written in [Golang](https://golang.org/). These functions read and write to a single [AWS Aurora RDS](https://aws.amazon.com/rds/aurora/) instance. The difference is that one stack is in a private subnet and requires the extra cold start overhead.

The VPC and RDS instances are managed by just CloudFormation, while the API Gateway and Lambda functions are managed by the Sam extension.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LwyfJUjmHsFbdMgGpLj57g.png)
_The diagram attempts to give a visual representation of the two stacks &amp; how their deployment is managed._

Below is a gist of Stack #1:

The other stack and the rest of the code can be found in my GitHub repo [here](https://github.com/nathanmalishev/go-lambda-vpc-experiment).

### Results

I ran these stacks, with an automated [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Scheduled-Rule.html) rule to trigger the Lambda functions every hour. I also deployed the stacks with varying degrees of RAM: 128mb, 1536mb, and 3008mb. In the graph below, all values above the 5 second mark are from Stack #2 (inside a VPC), and all values below are from Stack #1 (outside of a VPC).

![Image](https://cdn-media-1.freecodecamp.org/images/1*16yC8qApBwQirGLItTPtjA.png)
_Lambda Read &amp; Write functions from stacks #1 &amp; #2. [Play with the graph here](https://plot.ly/~nathanmalishev/1/" rel="noopener" target="_blank" title=")_

It’s interesting to note that, over all the data points, adding a **VPC increased cold start times by an average of 8.83s**. Increasing the RAM did seem to reduce the cold start times added by the VPC.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GwWZRFPuYZ8qx0cBRFiH2A.png)
_Average cold start time across the stacks and RAM configurations_

It looks like the internet was right, and deploying your Lambda functions to a VPC adds huge overheads. An 8 second delay alone is a horrible user experience. If your application is properly decoupled, running into multiple cold starts would negatively affect a user’s experience.

### When to VPC?

You should really only be putting your Lambda functions inside a VPC when you absolutely need access to resources that can’t be exposed to the outside world. Otherwise, you are going to be paying for it in start up times **and it matters**. As [Yan Cui](https://www.freecodecamp.org/news/lambda-vpc-cold-starts-a-latency-killer-5408323278dd/undefined) highlighted in his article [‘You’re thinking about cold starts wrong’](https://medium.com/p/im-afraid-you-re-thinking-about-aws-lambda-cold-starts-all-wrong-7d907f278a4f?source=user_popover), cold starts can happen at anytime, and especially during peak service usage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4RwbY1CiZC2jzsD7jBtIlQ.png)
_Decision tree for Lambda &amp; VPC from their [Serverless White Paper](https://d1.awsstatic.com/whitepapers/architecture/AWS-Serverless-Applications-Lens.pdf" rel="noopener" target="_blank" title=")_

### Gotcha’s ?

If you do need to use a VPC, keep in mind that each time a Lambda function is executed, it uses a proportion of your ENI capacity from the subnet. From the [AWS docs](https://docs.aws.amazon.com/lambda/latest/dg/vpc.html), they state you must have sufficient ENI capacity to support your Lambda scaling requirements. If you run out of ENI capacity this will cause your Lambda functions to fail!

To calculate your maximum concurrent Lambda executions in a given subnet we must use the following formula.

`ENI Capacity = Projected peak concurrent executions * (Memory in GB / 3GB)`

`ENI Capacity` = Number of IP addresses your subnet has

`Memory in GB` = RAM dedicated to your Lambda function

For example, the subnet 10.0.70.0/24, has 251 available subnets. If we have a Lambda function assigned with 1.5gb of RAM:

251 = Project peak concurrent executions * (1.5/3)

Projected peak concurrent (Lambda) executions = 502

As your concurrent Lambda executions is directly reliant on IP addresses available in the subnets, it’s best to use a subnet that gives you over 1000 IP addresses.

If you’re not sure, you can do the math and ensure your RAM allocation for all your Lambda functions in a given subnet is appropriate for your available IPs.

**Thanks for reading!** If you enjoyed it be sure to give it a clap.

### References

The first slides displaying the cold start variants comes from AWS Reinvent’s 2017 talk “Become a [Serverless](https://serverless.com) Black Belt”.

#### Useful links

[The AWS server-less application model](https://github.com/awslabs/serverless-application-model) on GitHub.

[My Lambda VPC experiment](https://github.com/nathanmalishev/go-lambda-vpc-experiment) on GitHub.

