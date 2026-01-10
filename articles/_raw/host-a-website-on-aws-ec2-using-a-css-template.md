---
title: How to Host a Website on AWS EC2 Using a CSS Template
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-11-08T18:35:50.763Z'
originalURL: https://freecodecamp.org/news/host-a-website-on-aws-ec2-using-a-css-template
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731103973241/e1277a4c-3456-4f11-b809-24caf56ae13a.png
tags:
- name: AWS
  slug: aws
- name: ec2
  slug: ec2
- name: CSS
  slug: css
seo_title: null
seo_desc: 'Are you ready to take your web hosting skills to the next level by using
  a CSS template? Hosting a professional looking website doesn’t have to be complicated,
  and with AWS EC2, you can have your website live in no time!

  In this guide, I’ll show you ...'
---

Are you ready to take your web hosting skills to the next level by using a CSS template? Hosting a professional looking website doesn’t have to be complicated, and with AWS EC2, you can have your website live in no time!

In this guide, I’ll show you how to host a website using a pre-designed template from [**CSS templates**](https://www.free-css.com/free-css-templates) directly on your EC2 instance.

Before we dive into this guide, make sure you’ve gone through my [**previous blog**](https://www.freecodecamp.org/news/how-to-launch-an-ec2-instance-and-a-web-server-using-httpd/) on how to launch and connect to an EC2 instance. If you haven’t set up an EC2 instance yet, head over to that post first to get your instance up and running. Once that’s done, you’re all set to proceed!

### Step 1: Download the "Built Better" Template

For this tutorial, we’ll use the Built Better template, which is free and easy to set up.

Head over to [this link](https://www.free-css.com/free-css-templates/page284/built-better) and download the template.

Right-click on the download button and select "Copy clean link". We’ll use this link to download the template directly into your EC2 instance.

### Step 2: Download the Template Directly to Your EC2 Instance

Now that you have the link to the template, let’s download it straight to your EC2 instance using `wget`.

Log in to your EC2 instance via SSH or MobaXterm (as covered in my [**previous blog**](https://www.freecodecamp.org/news/connect-to-your-ec2-instance-using-mobaxterm/)) and navigate to the `/var/www/html` directory where your website files will be stored:

```bash
cd /var/www/html
```

Use the `wget` command followed by the copied link to download the "Built Better" template directly into your EC2 instance:

```bash
sudo wget https://www.free-css.com/assets/files/free-css-templates/download/page284/built-better.zip
```

**Note:** After downloading, it's a good idea to check the file name to ensure it matches the file used in the subsequent commands. You can do this by running the `ls` command:

```bash
ls
```

### Step 3: Unzip the Template Files

Now that the template has been downloaded, it’s time to extract it. Install the `unzip` utility if it’s not already installed:

```bash
sudo dnf install unzip -y
```

Then unzip the template:

```bash
sudo unzip built-better.zip -d /var/www/html/
```

After unzipping, make sure to check the folder name where the files were extracted from. You can do this by listing the contents of the `/var/www/html` directory:

```bash
ls /var/www/html/
```

In this case, the unzipped contents are located inside a folder named `html`. This folder contains all the template files. If the folder name is different in your case, adjust the following steps accordingly.

First, move the files from the `html` folder to the root `/var/www/html/` directory:

```bash
sudo mv /var/www/html/html/* /var/www/html/
```

Then remove the unnecessary folder:

```bash
sudo rm -r /var/www/html/html
```

Lastly, remove the ZIP file:

```bash
sudo rm built-better.zip
```

### Step 4: Set Up the Web Server to Host Your Template

If you haven’t already, make sure your Apache HTTPD web server is installed and running. You can follow these steps to ensure your server is ready:

Install Apache (if not installed):

```bash
sudo yum install httpd -y
```

Start the Apache service:

```bash
sudo systemctl start httpd
```

Enable Apache to start on boot:

```bash
sudo systemctl enable httpd
```

Now your web server should be up and running, ready to serve your template.

### Step 5: Test Your Website

Now for the exciting part seeing your site live! Open a browser and navigate to your EC2 instance’s public IP address. You should now see the Built Better template live and ready to go.

Here’s how to check:

* Find your EC2 instance’s public IP from the AWS EC2 dashboard.
    
* Enter the IP in your browser, like so: [`http://your-ec2-public-ip`](http://your-ec2-public-ip)
    
* Your website should now be live with the Built Better template! 🎉
    

### Wrapping Up

Congratulations! You’ve successfully hosted a professional-looking website using the Built Better CSS template on your EC2 instance.

With just a few steps, you’ve moved from launching an EC2 instance to hosting a fully styled website, all using the AWS powerful cloud infrastructure.

You can follow me on

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
