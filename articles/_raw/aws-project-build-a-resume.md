---
title: How to Build an Online Résumé on AWS Using S3, Route 53, CloudFront, and ACM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-08T00:38:02.000Z'
originalURL: https://freecodecamp.org/news/aws-project-build-a-resume
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/thumbnail-final-1.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Job Hunting
  slug: job-hunting
- name: projects
  slug: projects
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Amber Israelsen\nIf you're new to AWS, you can probably appreciate the\
  \ sense of overwhelm that comes from trying to understand all the different services\
  \ (seriously, like, hundreds of them). What are they all for, and how do they work\
  \ together? \nAn..."
---

By Amber Israelsen

If you're new to AWS, you can probably appreciate the sense of overwhelm that comes from trying to understand all the different services (seriously, like, _hundreds_ of them). What are they all for, and how do they work together? 

And then once you've conquered some basic skills, the next challenge is how to demonstrate those skills to a potential employer. What kind of a project can you highlight on your résumé or CV, without breaking the bank?

In this hands-on tutorial, you'll get help with both of those things by building your _actual_ résumé/CV on AWS, by following these steps:

* Write code for your résumé using HTML, CSS and JavaScript
* Upload your files to a Simple Storage Service (S3) bucket that you configure for static website hosting, with public access
* Use Route 53 to set up a custom domain for your résumé
* Set up a TLS/SSL certificate with AWS Certificate Manager (ACM)
* Create a CloudFront distribution (that points to the files in S3) where you can apply the certificate.

Here's what we'll build:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Completed-resume-with-callouts-1-2.png)
_Sample resume on AWS, using S3, CloudFront, Certificate Manager and Route 53_

By the end of this tutorial, you'll have more than just an online résumé. You'll have a real-world project that you can use to dazzle your friends, family, network, and potential employers.

For a live walk-through of the project, check out this video:

%[https://youtu.be/NiCZSdWucZE]

## Table of Contents

* [What you need to follow along](#heading-what-you-need-to-follow-along)
* [But first, what will this cost?](#heading-but-first-what-will-this-cost)
* [Create the code (HTML, CSS, JavaScript) for your résumé](#create-the-code-html-css-javascript-for-your-resume)
* [Create an S3 bucket and configure it for static website hosting and public access](#heading-create-an-s3-bucket-and-configure-it-for-static-website-hosting-and-public-access)
* [Domain name option 1: Register a new domain name with Route 53](#heading-domain-name-option-1-register-a-new-domain-name-with-route-53)
* [Domain name option 2: Use a domain name from a third-party provider](#heading-domain-name-option-2-use-a-domain-name-from-a-third-party-provider)
* [Create an A Record with an alias to point to the S3 website](#heading-create-an-a-record-with-an-alias-to-point-to-the-s3-website)
* [Create a public TLS/SSL certificate using AWS Certificate Manager](#heading-create-a-public-tlsssl-certificate-using-aws-certificate-manager)
* [Create a CloudFront distribution](#heading-create-a-cloudfront-distribution)
* [Update Route 53 to point to the CloudFront distribution](#heading-update-route-53-to-point-to-the-cloudfront-distribution)
* [Behold the final result](#heading-behold-the-final-result)
* [IMPORTANT! Delete your resources](#heading-important-delete-your-resources)
* [Wrapping up](#heading-wrapping-up)

## What You Need to Follow Along

To successfully complete this tutorial, you'll need the following:

* **An AWS account**: You can [set one up for free](https://portal.aws.amazon.com/billing/signup) (though it does require a credit card for validation).
* **Basic experience**: Having some basic AWS experience will make the tutorial easier, but you should still be able to follow along if you're a total newbie.
* **Appropriate permissions**: I'd suggest logging in as an IAM user with administrator privileges, or using your root account (though I'm obliged to say that working in your root account day-to-day is not recommended/not a best practice).

## But First, What Will This Cost?

Before we get too far along, let's break down the different services and what they'll cost. 

If you want to delete everything after the tutorial, be sure to see that section towards the end of this article. I'd also recommend [setting up an AWS Budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) so you can put a limit on spending and be notified if you're going to exceed it (no surprise bills, please!).

* **S3**: Used to host website files. If you're still in the [AWS Free Tier](https://aws.amazon.com/free), there should be no cost. Outside of the Free Tier, the cost should be minimal, as in cents.
* **Route 53**: If you decide to purchase a domain name through Route 53 (optional – you can also "bring your own" domain name from another provider), it will cost $10+. You'll also need a hosted zone, which will run you 50 cents per month. And Route 53 queries (when someone visits your domain) will cost 40 cents per million queries.
* **AWS Certificate Manager**: A TLS/SSL certificate through ACM is free.
* **CloudFront**: Inside the Free Tier, there is no cost. Outside of the Free Tier, it will depend on traffic, but for our purposes, it will likely only cost cents. See the [full pricing page](https://aws.amazon.com/cloudfront/pricing/?nc=sn&loc=3) for more info.

## Create the Code (HTML, CSS, JavaScript) for Your Résumé

This section is where you can let your creativity (and your coding skills) fly. Nothing here is specific to AWS – it's just good ol' web development.

You'll eventually be using an S3 bucket to host your résumé files (HTML, CSS and JavaScript). S3 can only host a static website, meaning you can't include anything that requires server-side code. But front-end stuff all day long.

I won't be too prescriptive for the code you use here – this is _your_ résumé, after all. But you'll want to highlight the "usual" résumé things: employment history, education, skills/certifications, and maybe things like honors/awards or hobbies to make you seem more human.

If you want to list skills of HTML, CSS and JavaScript on your résumé, you'll ideally want to code this part by hand (wink, no ChatGPT help!), but you're also welcome to use my code below as a starting point.

### index.html file

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Resume - Your Name</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <img src="headshot.jpg" alt="Headshot" class="headshot">
            <h1 id="name">Name</h1>
            <p id="contactInfo">Location | Email</p>
        </header>
        <section id="employmentHistory">
            <h2>Employment History</h2>
            <div id="timeline"></div> <!-- Placeholder for the JavaScript array -->
        </section>
        <section id="education">
            <h2>Education</h2>
            <ul>
                <li>Degree | University (Year)</li>
                <li>Degree | University (Year)</li>
                <!-- Add more list items as needed -->
            </ul>
        </section>
        <section id="skills">
            <h2>Skills/Certifications</h2>
            <ul>
				<li>Skill 1</li>
				<li>Skill 2</li>
				<li>Skill 3</li>
				<li>Skill 4</li>
                <!-- Add more list items as needed -->
			</ul>
        </section>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

### styles.css file

```css
/* Base reset for padding and margin for all elements */
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Container for centering the content */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
    padding: 20px;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

/* Header image and name styling */
.headshot {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    display: block;
    margin: 20px auto;
}

header h1 {
    margin-bottom: 10px;
}

/* Contact information styling */
#contactInfo {
    font-size: 1.1em;
    margin-bottom: 20px;
    color: #fff; 
    padding: 15px;
}


/* Section styling for employment, education, and skills */
section {
    background: #fff;
    margin: 20px 0;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

section h2 {
    margin-bottom: 10px;
}

/* Timeline styling */
#timeline .entry {
    border-left: 3px solid #333;
    margin-bottom: 5px;
    cursor: pointer;
}

#timeline .entry-header {
    background: #e2e2e2;
    padding: 10px;
    margin-left: -3px; 
}

#timeline .entry-header:hover {
    background: #ccc; 
    color: #333; 
}

/* Style for the job description content */
#timeline .entry-content p {
    padding: 5px 10px;
    background: #f9f9f9;
    border-left: 3px solid #333;
    display: block; 
}

/* List styling for education and skills */
section ul {
    list-style: inside square;
    padding: 0 20px;
}

section ul li {
    padding: 2px 0;
}

/* Adjustments for active class */
.entry.active .entry-header {
    background-color: #e2e2e2; 
    color: #333; 
}

.entry.active .entry-content {
    display: block; 
}

/* Visual cue for clickable items */
.entry .entry-header:after {
    content: ' (click to expand)';
    font-size: 0.8em;
    color: #666;
}

.entry.active .entry-header:after {
    content: ' (click to collapse)';
    font-size: 0.8em;
    color: #666; 
}
```

### script.js file

```javascript
// Used on the résumé to make the employment history interactive (each job is clickable)
document.addEventListener('DOMContentLoaded', function () {
    // Placeholder array with employment history data
    const employmentHistory = [
        { id: 1, title: 'Job Title', company: 'Company Name', years: 'Year - Year', description: 'Description of what you did' },
        { id: 2, title: 'Job Title', company: 'Company Name', years: 'Year - Year', description: 'Description of what you did' },
        { id: 3, title: 'Job Title', company: 'Company Name', years: 'Year - Year', description: 'Description of what you did' }
        // Add more entries as needed
    ];

    const timeline = document.getElementById('timeline');

    // Create timeline entries
    employmentHistory.forEach(job => {
        // Entry container for job
        const entry = document.createElement('div');
        entry.className = 'entry';
        entry.id = 'entry-' + job.id;

        // Title header for job
        const header = document.createElement('div');
        header.className = 'entry-header';
        header.innerText = job.title;

        // Content container for job, initially hidden
        const content = document.createElement('div');
        content.className = 'entry-content';
        content.innerHTML = `<strong>Company:</strong> ${job.company}<br>
                             <strong>Years:</strong> ${job.years}<br>
                             <p>${job.description}</p>`;
        content.style.display = 'none';

        // Append header and content to the entry
        entry.appendChild(header);
        entry.appendChild(content);

        // Event listener to toggle content visibility
        header.addEventListener('click', function () {
            // Check if the clicked header's content is currently shown
            const isContentShown = content.style.display === 'block';
            // Hide all open contents
            document.querySelectorAll('.entry-content').forEach(el => {
                el.style.display = 'none'; // Hide content
            });
            // Deactivate all headers
            document.querySelectorAll('.entry').forEach(el => {
                el.classList.remove('active'); // Remove active class
            });

            if (!isContentShown) {
                // If it was not shown before, display it
                content.style.display = 'block';
                entry.classList.add('active');
            } // If it was shown, it will be hidden as part of the above loop
        });

        timeline.appendChild(entry);
    });
});
```

## Create an S3 Bucket and Configure it for Static Website Hosting and Public Access

Now that you have your three code files (plus don't forget a "headshot.jpg" to display your smiling face), you need somewhere to put them.  

In AWS, S3 is a great option for inexpensive object (read: files) storage. And if you're only using client-side code like you are, then you can configure S3 for static website hosting.

### Create an S3 bucket

In the [AWS Management Console](https://console.aws.amazon.com/), navigate to **S3**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Navigate-to-S3.png)
_Navigate to S3_

Click **Create bucket**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-an-S3-bucket.png)
_Create a new bucket_

Enter the details for your bucket.

* **Bucket name**: **IMPORTANT**! If you plan to use a custom domain for your résumé, then this bucket name should match the domain name exactly. For example, I'll be using "amberaws.com" so my bucket name needs to be "amberaws.com". If you use a different name, you'll run into trouble when you get to the Route 53 part of the tutorial.
* **AWS Region**: You can choose any region you'd like, but I'd recommend going with the one closest to you. 
* **Object Ownership**: Leave the default of **ACLs disabled (recommended)**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Bucket-details-1.png)
_Enter bucket name, region, and object ownership_

Scrolling down, **deselect** the setting for **Block _all_ public access**. **NOTE**: In most scenarios, this is not recommended, as you'll see from the warning you receive when you disable it. But because you're creating a public résumé that you DO want to be open to the world, then disabling this is appropriate.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Block-all-public-access-1.png)
_Deselect the option to block all public access, then acknowledge the setting_

Use the defaults for the rest of the bucket settings and then click **Create bucket**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Bucket-defaults-and-create.png)
_Select defaults for the rest of the bucket settings, then create bucket_

Now you have an empty bucket, but it's not quite ready for primetime in terms of website hosting. You'll need to make a couple more updates.

### Enable static website hosting

For S3 to be able to serve your files up as a website, you'll need to enable that on the bucket.

Click into the bucket you just created and go to the **Properties** tab.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Properties-tab.png)
_Navigate to the Properties tab for the bucket_

Scroll _all the way_ down to the bottom of the page, and in the **Static website hosting** section, click **Edit**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Static-website-hosting-edit.png)
_Edit the static website hosting setting_

Select **Enable**. This will open additional options.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Enable-static-website-hosting.png)
_Enable static website hosting_

For the **Index document**, enter **index.html**. This specifies the default home page for the site (your HTML code for your résumé). Then click **Save changes**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Static-website-hosting-index-page.png)
_Specify the default home page (index.html) and save changes_

### Add a bucket policy to allow the contents of the bucket to be publicly accessible

When you created the bucket, you said you _didn't_ want to block all public access. But even with that setting, the default behavior of S3 is to "deny" everything. So if you don't explicitly say that people _can_ access the files in your bucket, they won't be able to. You'll grant read permissions with a bucket policy.

At the top of the page, click the **Permissions** tab.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Permissions-tab.png)
_Click the Permissions tab of the bucket_

Scroll down to the **Bucket policy** section, and click **Edit**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Edit-bucket-policy.png)
_Edit the bucket policy_

Copy the following bucket policy (JSON code).

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::Bucket-Name/*"
            ]
        }
    ]
}
```

Paste the code into the Policy section in the AWS console. This policy says to "Allow" everyone (the Principal of "*") to take the action of "GetObject" (basically "read") on all files in your bucket ("Bucket-Name/*").

**IMPORTANT**: Update "Bucket-Name" with the name of your bucket. Then click **Save changes**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Bucket-policy-1.png)
_Paste the JSON code for the bucket policy, updating "Bucket-Name" to your own_

You've now got a bucket that's configured for static website hosting, and you've applied a policy that will let people access the site. Now it's time to add your impressive code files that you created earlier.

On the top of the page, click the **Objects** tab.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Objects-tab.png)
_Click the Objects tab on the bucket_

Click the **Upload** button.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Upload-files.png)
_Click the Upload button to upload your code files_

Drag and drop your four files to the browser.  This should include **index.html**, **styles.css**, **script.js** and **headshot.jpg**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Drag-and-drop-files.png)
_Drag and drop your four files (code and headshot.jpg)_

After the files have uploaded and all four display in the **Files and folders** section, click the **Upload** button.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Upload-files-2.png)
_Upload the files_

Now it's time to test that your résumé loads. To do this, you'll need to get the S3 bucket website endpoint.

Navigate to the **Properties** tab of the bucket.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Properties-tab-1.png)
_Navigate to the Properties tab_

Scroll _all the way_ down to the bottom of the page, to the **Static website hosting** section. Click on the **Bucket website endpoint** link (it will open in a new tab).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Website-endpoint-1.png)
_Click the bucket website endpoint to view your resume (in a new tab)_

If everything worked, you should see your handiwork displayed in the browser.  Yay!

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Website-test-1-1.png)
_It works! Your resume being served up by S3._

Congrats on getting your résumé hosted in S3 with public access! But as impressive as it is, it would be even _more_ impressive if it were using a custom domain. Currently, it's using the S3 website URL, formatted as [bucketname].s3-website-[regionname].amazonaws.com. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/S3-bucket-URL.png)
_The resume would be much cooler with its own custom domain name_

Let's work on the domain name next, using Route 53, which is Amazon's domain name and DNS service.

## Domain Name Option 1: Register a New Domain Name with Route 53

If you don't already have a domain name, then you can register one with AWS, using Route 53. (If you already have a domain name with another provider, I'll give you some general guidance on using that in the next section.)

Navigate to **Route 53**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Navigate-to-Route-53.png)
_Navigate to Route 53_

On the Route 53 Dashboard, simply **enter the domain name** you're interested in, then click **Check**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Check-domain-name-availability-1.png)
_Check availability of a domain name_

If the domain name is available, you'll be able to **Select** it (and if it's not available, you'll see some alternate names). Selecting it will add it to your cart, take you through a checkout process, and then the charge will show up on your AWS bill.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Select-available-domain.png)
_Select the available domain or choose alternatives_

After you purchase the domain, it will automatically create a **hosted zone** for you. You can think of a hosted domain as a container for records and rules that control how traffic is routed.  

A public hosted zone (which you'll be working with) controls traffic from the internet. A private hosted zone controls traffic internal to an AWS Virtual Private Cloud (VPC).

You can view your hosted zones by clicking on **Hosted zones** on the left navigation, then click into the zone that matches the domain name you purchased ("amberaws.com" in my case).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Hosted-zones.png)
_Select the hosted zone for your domain name_

## Domain Name Option 2: Use a Domain Name from a Third-Party Provider

So, you already have a domain name from somewhere else, like GoDaddy, Namecheap, Google Domains or the like. It's totally possible to use Route 53 as your DNS service (which has a lot of benefits, and is easy to integrate with other AWS services), while still keeping the domain name with your other provider.

The details of each registrar are slightly different, so I'll give some general guidance here. Also know that propagation of DNS changes will take longer with an external provider, and if things go wrong, you'll probably need to work with them directly. But I'll get you started!

### Create a hosted zone and get your name servers

Even if you aren't using a domain name from Route 53, you'll still need a hosted zone (again, this holds the records and rules that control how traffic is routed). 

Click on **Hosted zones** on the left navigation, then click **Create hosted zone**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-a-hosted-zone-1.png)
_Create a hosted zone for your external domain name_

Enter the **domain name** from the third-party provider, select **Public hosted zone**, then click **Create hosted zone**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Created-hosted-zone-details.png)
_Fill in the details for the public hosted zone_

Once your public hosted zone is created, you'll see four **name servers** listed. Make a note of these.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Name-servers.png)
_Make a note of your name servers so you can enter them with the third-party provider_

Next, go to the DNS settings for your current domain provider. Find your name server settings, and replace them with the name servers from Route 53.

For more specifics, here are guides from some of the more popular domain name providers:

* [GoDaddy](https://uk.godaddy.com/help/edit-my-domain-nameservers-664)
* [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/)
* [Google Domains](https://support.google.com/domains/answer/3290309?hl=en)
* [Hostgator](https://www.hostgator.com/help/article/how-do-i-change-my-dns-or-name-servers)

After you've made the updates on the third-party site, and changes have propagated, you should be good to follow along with the rest of this article.

## Create an A Record with an Alias to Point to the S3 Website

Now that you have a public hosted zone, you need to create a record that says how traffic should be routed when someone goes to your domain name.

Click into your hosted zone, and then click **Create record**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-record.png)
_Create a new record_

**NOTE**: If you get the "wizard" view below, click **Switch to quick create**.  (If you don't see this "tile" view, then you're already in quick create mode.)

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Switch-to-quick-create.png)
_Switch to quick create view_

Fill out the details for the record.

* **Record name**: Leave the subdomain blank, and just go with the root domain (like "amberaws.com").
* **Record type**: A
* **Alias**: Toggle this on. An alias lets you route to AWS resources like S3, CloudFront, Elastic Beanstalk and so on.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Record-details-1.png)
_Fill in the domain, record type and then toggle Alias to on_

Now fill in the details of where to route traffic. You can type into these dropdowns to filter the values.

* **Alias to S3 website endpoint**
* **Your region** (I'm using US West (Oregon))
* The final dropdown should automatically populate with **your S3 website**. **NOTE**: If nothing shows up here, it's likely because you didn't name your bucket the same as your domain name. D'oh! You'll need to recreate the bucket with the exact name of your domain.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Route-traffic-to.png)
_Fill in the details for traffic routing_

For **Routing policy**, select **Simple routing.** For **Evaluate target health**, leave the default of **Yes**, then click **Create records**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-record-details-2.png)
_Choose routing policy, target health, and then create record_

It can take up to 60 seconds for your changes to take effect. You can view the status of propagation by clicking on the handy **View status** on top of the page.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/View-DNS-status.png)
_View the propagation status of your changes_

After the **Status** changes from PENDING to **INSYNC**, then you should be good to test out your changes.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Status-of-INSYNC.png)
_Make sure the status says INSYNC before testing things out_

Now let's test!  If everything worked, then when you **type your domain name into a browser** (like amberaws.com), Route 53 should direct you to the S3 website, which means you should see your (awesome) résumé.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Test-domain-name-1-1.png)
_It works! Your domain name should now display your resume._

Congratulations! You've made a ton of progress. The last piece is to get a secure connection (HTTPS, with a TLS/SSL certificate) working so you can get rid of that pesky "Not secure" message from your browser.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Test-domain-name-cert.png)

Let's tackle that piece next, using AWS Certificate Manager.

## Create a Public TLS/SSL Certificate using AWS Certificate Manager

If you need a refresher on certificates, these help ensure a secure connection between users and the server they're making a request to.  

If I'm sending bank information across the internet, for example, I want to know that it's going to a server that's reputable, and that the connection is encrypted. And even for something as "simple" as a résumé, a secure connection will give viewers confidence that they haven't ended up on a sketchy website.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Certificates.png)
_Why we need certificates_

In AWS land, certificates are created and managed in AWS Certificate Manager (ACM). (You can also import existing certificates from another authority if you have them.)

Navigate to **Certificate Manager**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Navigate-to-ACM.png)
_Navigate to Certificate Manager_

**IMPORTANT!**  For this section, you need to switch your region to **us-east-1 (N. Virginia)**. If you create a certificate in another region, you won't be able to use it with CloudFront (where you'll eventually end up).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/us-east-1.png)
_Change region to us-east-1 (N. Virginia)_

From the Certificate Manager landing page, click **Request a certificate**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Request-a-certificate.png)
_Request a certificate_

Select **Request a public certificate** and then click **Next**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Request-public-certificate.png)
_Select a public certificate and then click next_

Enter your **domain name** (like "amberaws.com"), leave the rest of the options as defaults, then click **Request**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Details-of-certificate.png)
_Enter your domain name and then request_

The request was successful, but it will have a "pending validation" status until you validate DNS. Click **View certificate**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/View-certificate.png)
_View the certificate to take additional actions_

Before a certificate can be issued, Amazon needs to confirm that you own this domain and that you're able to modify DNS settings (in Route 53). To start this process, click **Create records in Route 53**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-records-in-Route-53.png)
_Create records in Route 53 to validate DNS_

There are various filters applied to this next screen, checking for validation status and whether your domain is found in Route 53. From here, you can click **Create records**, which will actually – wait for it – create a record in Route 53 for you.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-records-from-ACM.png)
_Create records, which will create a CNAME record in Route 53_

If the record creation was successful, you should see a message to that effect.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Success-DNS-record.png)
_Successfully created a record in Route 53 to validate DNS_

The record was created in Route 53. So navigate to **Route 53**, to **your hosted zone** you were working in earlier. You should see a new **CNAME record** that was created from Certificate Manager.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/CNAME-record-in-Route-53.png)
_View the new CNAME record in Route 53_

Great! You have a TLS/SSL certificate, but what do you do with it now?

Your website files are currently hosted in S3, but unfortunately, you can't use a certificate on an S3 bucket.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/No-cert-on-S3.png)
_Certificates don't work with S3_

What you need instead is a CloudFront distribution that points to the S3 bucket. And then the certificate is applied to the CloudFront distribution.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Cert-on-CloudFront.png)
_CloudFront is the solution!_

You know what that means, right? It means we need to head off to CloudFront next!

## Create a CloudFront Distribution

CloudFront is Amazon's content delivery network, or CDN. It's used to get content to users faster by caching it at "edge locations" around the world. This works great for things like videos and images, making them faster to load.  

For your simple résumé, because the files are so small, you won't notice much of a performance difference. But it _is_ the way you'll be able to apply the TLS/SSL certificate you created in the last section.

Navigate to **CloudFront**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Navigate-to-CloudFront.png)
_Navigate to CloudFront_

On the CloudFront home page, click **Create a CloudFront distribution**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-a-CloudFront-distribution.png)
_Create a CloudFront distribution_

The origin domain is where your website files live, which is in S3. If you type in **S3** to filter, it should pull up your bucket.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Origin-domain.png)
_Filter by S3 to find your bucket as the domain origin_

But wait! You get a message about using the website endpoint rather than the bucket endpoint. Yes, that's what you want! Click **Use website endpoint**, and AWS will update the endpoint for you.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Website-endpoint-not-bucket-endpoint.png)
_Use the website endpoint, not the bucket endpoint_

There are gobs of settings on the rest of this page, but you only need to update a few of them.

Scroll down to the **Default cache behavior section**, then under **Viewer**, select **Redirect HTTP to HTTPS**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Redirect-HTTP-to-HTTPS.png)
_Redirect HTTP to HTTPS_

Scroll down to **Web Application Firewall (WAF)** and select **Do not enable security protections**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/WAF.png)
_Do not enable WAF_

In the next section, **Settings**:

* For **Alternate domain name (CNAME)**, enter your domain name (like "amberaws.com").
* For **Custom SSL certificate**, select the certificate you set up earlier. **NOTE**: if you set it up in a region other than us-east-1 (N. Virginia), it won't show up here. D'oh! You'll need to recreate it in us-east-1.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Settings-for-CloudFront.png)
_Enter an alternate domain name and the custom SSL certificate_

Scroll to the bottom of the page.

For **Default root object**, enter **index.html** (your default home page) and then click **Create distribution**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Index-and-create-distribution.png)
_Set the default root object as index.html and then create distribution_

It will take several minutes for the CloudFront distribution to finish deploying (even if it says "Successfully created" at the top of the page). You'll know it's done when the **Last modified** value shows a date and time.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Last-modified.png)
_The deployment is done when a date/time appear in "Last modified"_

To test that everything is working with CloudFront and the TLS/SSL certificate, copy the **Distribution domain name**. Open a new tab in the browser and navigate to that address. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Distribution-domain-name.png)
_Copy the distribution domain name and open it in a new tab_

If everything worked, you should now see the all-important padlock icon in your browser, indicating that you're on a secure connection using the certificate set up through Certificate Manager.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/CloudFront-cert.png)
_The TLS/SSL certificate is working with CloudFront!_

Awesome! But before you get excited thinking we're done, remember that you ultimately want to go to your custom domain name to load the résumé, not to this lengthy CloudFront distribution domain name.

## Update Route 53 to Point to the CloudFront Distribution

At the moment, the A Record in Route 53 is pointing to the S3 bucket, like this...

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Current-setup.png)
_Route 53 currently points to the S3 bucket_

Instead, we want Route 53 to point to the CloudFront distribution, which then points to S3, like this...

![Image](https://www.freecodecamp.org/news/content/images/2023/11/What-we-want.png)
_Route 53 should point to CloudFront, which then points to S3_

Navigate back to **Route 53**, to the **hosted zone** you've been working with.  **Select the A Record**, then on the right of the screen, click **Edit record**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Edit-A-record.png)
_Edit the Route 53 A Record_

Instead of routing traffic to S3, update the three dropdowns to point to your CloudFront distribution.

* **Alias to CloudFront distribution** 
* **US East (N. Virginia)** (this option is selected for you and grayed out)
* **Choose your distribution** (it should automatically populate in the third dropdown)

Click **Save**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Edit-A-record-details.png)
_Update the A Record to route traffic to CloudFront_

## Behold the Final Result

And now the moment of truth: if everything worked, you should be able to navigate to your custom domain name and have it load your résumé on a secure connection.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Final-resume.png)
_Final résumé loading on a custom domain name over a secure connection_

And VOILÀ! It works.

The résumé files (coming from S3 via CloudFront) load on the custom domain name (from Route 53) over a secure connection using the TLS/SSL certificate (from Certificate Manager). Nice work.

Here's what you've built:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Final-diagram.png)
_A diagram of the final project_

## IMPORTANT! Delete Your Resources

At the beginning of the article, I covered the costs for the services. If you choose to leave them running, it shouldn't cost you a fortune (unless, of course, your résumé goes viral and you're suddenly paying for a ton of Route 53 and CloudFront traffic...maybe a good problem?).  

But definitely set up an [AWS Budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) to be notified when charges reach a certain threshold.

For those of you who want to delete everything you built, let's do that now.

### Disable and delete the CloudFront distribution

Navigate to **CloudFront** and select your distribution. Before you can delete it, you first have to **Disable** it. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Disable-CloudFront-distribution-1.png)
_Disable the CloudFront distribution_

This will take several minutes to complete, and it has to finish before you can delete some other things. So let it run. When it's done, you should see a date and time in the **Last modified** column.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/CloudFront-disabled.png)
_Ensure the CloudFront distribution is disabled_

Once the distribution is disabled, select it and then click **Delete**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-CloudFront-distribution.png)
_Delete the CloudFront distribution_

### Delete records from the Route 53 hosted zone

Navigate to **Route 53** and the hosted zone you've been working in. Records won't cost any money, but if you don't plan to use them, it's a good idea to delete them to avoid confusion in the future.

Select the **A Record** and the **CNAME Record** and then click **Delete records**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-Route-53-records.png)
_Delete the A Record and CNAME Record from Route 53_

### Delete the hosted zone (optional)

You can also choose to delete your hosted zone in Route 53, but if you do, your domain might become unavailable on the internet.  

If you plan to use your domain name at some point in the future, I'd recommend keeping the hosted zone (I've chosen to keep mine).  **Keeping the zone will cost you 50 cents per month.**

But if you'd like to go ahead with deletion, just **select the hosted zone** and click **Delete**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-hosted-zone.png)
_Delete the Route 53 hosted zone_

Confirm that you've completed the actions in this warning message, type "**delete**," and then click **Delete**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-hosted-zone-1.png)
_Confirm deletion of the Route 53 hosted zone_

### Delete the certificate from Certificate Manager

Navigate to **Certificate Manager**. Select **the certificate** you created, then click **Delete**. (If the CloudFront distribution hasn't been disabled yet, you'll get an error on this step saying the resource is still in use.)

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-certificate.png)
_Delete the certificate from Certificate Manager_

### Empty the S3 bucket and then delete it

Navigate to **S3**, to the list of all your buckets. Select the bucket and then click **Delete**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-bucket.png)
_Delete the S3 bucket_

Before you can delete a bucket, you must first delete the files in it. AWS provides a handy link to do that. Click the link to **empty bucket configuration**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Empty-bucket.png)
_Empty files from the S3 bucket_

Confirm that you want to permanently delete the files (you do) by typing "**permanently delete**" and then clicking **Empty**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Permanently-delete.png)
_Confirm deletion of files_

Now that the bucket is empty, you can delete it.  And in the success message at the top of the screen, there's a convenient link to do so. Click **delete bucket configuration**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-bucket-configuration.png)
_Delete the S3 bucket_

Confirm this action by typing in the **name of your bucket**, then clicking **Delete bucket**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-bucket-final.png)

And that's it! The resources have been deleted, and you shouldn't incur any additional charges.

## Wrapping up

Congratulations on making it all the way to the end! I hope you were able to successfully build out a résumé, and at the same time cement some of your AWS skills for the future. Feel free to share it with the world, and best of luck in your job search.

_For more tutorials on AWS and other tech, head to [Tiny Technical Tutorials](https://www.youtube.com/playlist?list=PLwyXYwu8kL0wg9R_VMeXy0JiK5_c70IrV) on YouTube._

