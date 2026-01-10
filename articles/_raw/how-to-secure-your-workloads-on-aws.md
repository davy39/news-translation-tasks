---
title: How to Secure Your Workloads on AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-10T17:21:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-your-workloads-on-aws
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Secure-Your-Workloads-on-AWS.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Services
  slug: cloud-services
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: null
seo_desc: "By Riya Sander\nBusinesses are trying to save money these days, so many\
  \ are moving to the cloud. And a study suggests that the global public cloud services\
  \ market will have grown 6.3% in 2020. \nCloud services revenue will go up to US$257.9\
  \ billion fro..."
---

By Riya Sander

Businesses are trying to save money these days, so many are moving to the cloud. And a study suggests that the [global public cloud services market](https://www.gartner.com/en/newsroom/press-releases/2020-07-23-gartner-forecasts-worldwide-public-cloud-revenue-to-grow-6point3-percent-in-2020#:~:text=The%20worldwide%20public%20cloud%20services,increasing%2095.4%25%20to%20%241.2%20billion.) will have grown 6.3% in 2020. 

Cloud services revenue will go up to US$257.9 billion from US$242.7 billion in 2019. But as technologies grow more advanced, hackers are becoming better at using that tech to gain access to your mission-critical data. [Cloud-based attacks](https://www.fintechnews.org/the-2020-cybersecurity-stats-you-need-to-know/) rose 630% between January and April 2020.

With more data being stored in the cloud, businesses need to have robust security policies. They must also include best practices for dealing with data that's stored in cloud services like AWS. 

With around 83% of [enterprise workloads moving to the cloud](https://www.varonis.com/blog/cybersecurity-statistics/) by the end of 2020, there is a large amount of critical data that needs to be protected. 

In this article, we will discuss some best practices that businesses should implement to protect the data they have moved to the cloud.

## Go through the AWS documentation

The [AWS docs](https://docs.aws.amazon.com/) detail the responsibilities of the client as well as those of AWS. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model) states that AWS is responsible for protecting the infrastructure that runs the services offered on the AWS cloud. 

The customer's responsibilities include the security configuration and management of the services they choose to use.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/shared-responsibility-model.png)
_[Source](https://aws.amazon.com/compliance/shared-responsibility-model)_

## Use Identity and Access Management

The AWS docs categorically state that the client needs to use Identity and Access Management (IAM) tools to safeguard their data. The [AWS IAM tool](https://aws.amazon.com/iam/) allows you to manage users who will have access to the cloud. 

IAM allows users to control access to certain resources. The tool also enables clients to create and manage AWS users and groups.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/aws-vpc-module.png)
_[Source](https://aws.amazon.com/blogs/aws/category/iam)_

Specific permissions are provided that allow or deny access to various AWS resources. If you wish to assign permissions to any one resource, you can create policies like the following:

* **Actions**: which service actions are allowed.
* **Resources**: for what resources you will allow those actions.
* **Effect**: whether you're denying or allowing access.
* **Conditions**: the requirements for which the actions will take effect.

Your webmaster can create one or more IAM users in the AWS account. You can create the users in the AWS Management Console, and you can add up to ten users at a time.

## Use Multi-factor Authentication

While storing your data on AWS is fairly secure, you must still take precautions against unauthorized access to that data.

As suggested by AWS, you can use [multi-factor authentication (MFA)](https://aws.amazon.com/iam/features/mfa/) for an extra layer of security. Using only your user ID and password may not be safe enough because hackers have developed many methods for breaking through your password.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/sign-in-aws-with-mfa.png)
_[Source](https://aws.amazon.com/blogs/security/use-yubikey-security-key-sign-into-aws-management-console)_

You can also control access to AWS's APIs using MFA. You can enable and manage a virtual MFA device for an IAM user in the AWS account. 

Just login to the AWS Management Console and add MFA after choosing the user.

## Have a Robust Security Apparatus in Place

Amazon's relational databases must be encrypted unless they're already encrypted at the storage level. IAM keys must be changed every three months.

You must also tag your EC2 instances logically as this can provide more information about the location of the instance and its usage. It also helps you maintain consistency in your environment.

Tagging can also help you manage your Amazon resources more effectively. Your webmaster can locate, classify, and identify the resources for their various needs.

Filtering can help you find and validate the standards of tagging undertaken in your organization. You can use automated tools to assist in the tagging process. There is a Resource Groups Tagging API to help you filter, manage and search tags.

## **Train your employees**

While you are taking steps to enhance the security of your systems on AWS cloud, you must also organize periodic training sessions for your employees.

Studies show that hackers often target employees to gain access to protected networks. A small letdown in defenses can lead to a potential data breach that can damage your organization.

Your employees must be aware of the security protocols you're using to safeguard your data on AWS. If everyone in your organization is not aware of these protocols, you might have issues enforcing them.

When you introduce new processes, you should organize a short training session for your employees. You can also create self-learning videos and have a quiz at the end.

## Use End-to-end Encryption

End-to-end encryption helps protect your data against unauthorized access - you just have to install an SSL certificate on AWS.

The AWS Management Console can use the SSL certificate between the console service endpoints and the client's browser. The SSL certificate will allow encrypted interaction between a browser and the webserver. The client browser can authenticate the identity of the control service endpoint.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/LDAP-security-in-AWS-Directory-Service.png)
_[Source](https://aws.amazon.com/blogs/security/how-to-improve-ldap-security-in-aws-directory-service-with-client-side-ldaps)_

Using the HTTPS protocol can help protect your sensitive data. But you must also consider the additional resource requirements when your servers are handling hundreds of SSL/ TLS sessions.

To install the certificate, you need to convert the certificate and the intermediates to the PEM format. Then, you have to upload it to your AWS account and configure an HTTPS listener. Let's look at that process a bit more in-depth.

### How to Install SSL on your AWS server

Once the CSR is generated and submitted to the certificate authority, the certificate authority verifies the details and issues an SSL certificate. 

The private key file and certificate file both are in .CRT format. Once you have these two files, you need to upload them to the server.

* First Login to AWS and sign in onto AWS EC2.
* Then, browse the navigation menu >> click “**Network Security**” >> choose ‘**Load Balancers**’.
* Browse the main pane and select the Load Balancers icon while uploading the certificate.
* Now, click on the ‘**Listeners**’ tab and click on ‘**Edit**’ and ‘**Add**’.
* Choose HTTPS in the SSL certificate column and click on ‘**change**’ in the same column.
* Click the radio button “**Upload a new SSL certificate to AWS Identity and Access Management (IAM)**”. You can rename the certificate here too.
* In the private key field, paste the whole contents of the private key in the provided box **“—–BEGIN RSA PRIVATE KEY—–” and “—–END RSA PRIVATE KEY—–”**.
* In the public key certificate, paste the details of the certificate in the respective field **“—–BEGIN CERTIFICATE—–” and “—–END CERTIFICATE—–”**.
* Finally, paste the certificate chain or CA Bundle.crt in the respective column **“—–BEGIN CERTIFICATE—–” and “—–END CERTIFICATE—–”**.
* Click **Save** to complete the installation process. IAM will verify and confirm the installation after uploading the certificate.
* Restart your **AWS EC2** instance to see the changes.

## Have a Proper Recovery Policy in Place

You should have a robust backup and recovery policy in place. Even if your security is top-notch, backup and disaster recovery is critical.

AWS backup can help you find the right tools for a scalable backup and recovery solution. Their centralized backup process allows you to easily automate and centralize your backup.

Your webmaster can easily monitor this backup process for a number of AWS resources. Also, you can create backup policies in the AWS Backup console with only a few clicks.

To start your AWS backup, you have to sign into your AWS account and launch the AWS Backup console.

Next, create a backup plan and allocate the resources. The resources will get backed up based on your policy.

Once the resources are backed up, the user can monitor, restore, or modify them as necessary.

Below are few steps you should take to create a Disaster Recovery Plan (DRP):

* Create a set of instructions defining the rules and regulations relating to DRP. This is called Disaster Recovery Management Contingency Statement.
* Run a business impact analysis to get an idea of critical IT apps and components as well the impact of risks associated with the business.
* Take preventive, detective and corrective control measures that detect and minimize your risk ratio. Also, keeps security software updated, install fire alarms, run employee training sessions, and install network and server monitoring software.
* Find the application and business departments that will be impacted marginally during a failure (low failure assurance).
* Run tests to check whether changes occurred after each testing process. Management and employees should be trained for the disaster recovery process.

## **Use CloudTrail**

[CloudTrail](https://aws.amazon.com/cloudtrail) helps with operational and risk auditing as well as compliance and governance of your AWS account. 

Its services allow your webmaster to continuously monitor the activity on your AWS account. It also preserves a history of all activity across all your AWS services.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/AWS-CloudTrail.png)
_[Source](https://aws.amazon.com/cloudtrail)_

CloudTrail will help you to track resources changes, analyze your security protocols, and detect unusual activity on your account. You must identify the data that is critical for your activities.

You can analyze CloudTrail's logs as they collect critical data about the usage of your AWS accounts. CloudTrail must be enabled across all geographies to give you these insights.

### How to Set Up AWS CloudTrail

When you create a trail in your AWS account, it allows you to utilize other AWS services. With that, you can check the event data stored in CloudTrail's logs. CloudTrail comes by default when you create an AWS account.

#### Set Up Cloud Trail for All religions

Name your CloudTrail and choose ‘Yes’ for ‘Apply trail to all regions'. You should apply it to all regions even if you are just handling a single country. You can check other regions’ activity as a comparison to yours.

#### Select Event Log

You can log dissimilar events like management, data, and insight events. You should choose the event types based on your organization’s needs.

#### Enable Log File Validation

You should configure logs on your S3 bucket(s), which are by default encoded with SSE-S3 encryption. Under the storage location option, you can click on ‘Yes’ to ‘Enable log file validation’.

#### Configure CloudWatch Alarms

Once you create a trail in your AWS account, you can configure CloudWatch security by clicking the ‘configure’ button. 

After that, enable IAM by clicking 'Create CloudWatch Alarms for Security and Network related API activity using CloudFormation template'. 

When you do this, you will get a notification regarding any API security calls.

Now CloudTrail should be all set up.

## Use AWS Trusted Advisor

[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor) helps you keep an eye on all areas of your cloud services.

It watches over the cloud environment and the applications that run on it. It also allows you to scan your internal networks and compare them with AWS's standards.

You can access AWS Trusted Advisor from the AWS Management Console. All accounts have access to a few of the checks. 

Businesses must subscribe to the Business or Enterprise levels of AWS support to get access to all the checks.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/AWS-Trusted-Advisor.png)
_[Source](https://aws.amazon.com/premiumsupport/technology/trusted-advisor)_

You can get the following checks through AWS at no additional charge:

* **Check IAM use**: checks if the client is adhering to security best practices and whether users, groups, and roles have been created to control access to the AWS resources.
* **Service limits check**: Your position for the essential service limits for the different products is checked.
* **MFA on root account check**: checks if you use MFA.
* **Security Groups** (Specific Ports Unrestricted Check): This check is essential, and it informs the webmaster if access to your EC2 instances is too permissive. It helps prevent denial of service or hacking attacks.

## Conclusion

As more and more businesses move their data onto the cloud, they have to take more precautions to manage that data safely and effectively.

This move to the cloud has resulted in more data breaches, and SSL certificates have become essential for secure AWS services.

I hope you've learned some best practices to help manage your AWS services in this article.

