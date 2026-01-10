---
title: How to Secure Your Web Server with Continuous Integration Using NGINX and CircleCI
subtitle: ''
author: Abraham Dahunsi
co_authors: []
series: null
date: '2024-01-19T16:46:59.000Z'
originalURL: https://freecodecamp.org/news/secure-web-server-with-continuous-integration-using-nginx-and-circleci
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/feature-image.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: nginx
  slug: nginx
- name: Security
  slug: security
seo_title: null
seo_desc: 'Web servers are responsible for delivering web pages and various resources
  to clients through the internet. They can exist either as software or hardware components.

  But unfortunately, they often become targets for hackers and malicious individuals
  s...'
---

Web servers are responsible for delivering web pages and various resources to clients through the internet. They can exist either as software or hardware components.

But unfortunately, they often become targets for hackers and malicious individuals seeking to exploit any vulnerabilities to compromise data and disrupt functionality. As a result, you'll need to prioritize the security of your web server by updating it and implementing safeguards against threats.

To enhance the security of your web server, one effective approach is to use [Continous Integration](https://www.freecodecamp.org/news/what-is-ci-cd/) (CI). CI is a DevOps technique that allows the automated merging of code modifications from software engineers into a single repository. This practice enhances code quality, minimizes bugs and speeds up code delivery.

By using CI, you can automate the testing, building, and deployment processes for your web servers’ code and configuration. You can also ensure that your web server consistently maintains a stable state.

In this tutorial, I'll guide you through the process of strengthening the security of your web server by using two popular and powerful tools: [NGINX](https://www.freecodecamp.org/news/nginx/) and CircleCI.

NGINX, which is an open source web server, provides a range of features and modules that can greatly enhance the security of your web server. These include SSL/TLS encryption, security headers, and support for HTTP/2.

On the other hand, CircleCI offers both cloud-based and self-hosted options for Continous Integration (CI) and Continuous Delivery (CD), enabling seamless deployment processes.

By following this guide, you will learn how to:

* Configure NGINX to use SSL/TLS encryption and security headers
    
* Create a GitHub repository and push your NGINX configuration files to it
    
* Create a CircleCI project and link it to your GitHub repository
    
* Create a CircleCI configuration file and define your CI pipeline
    
* Test and deploy your web server with CircleCI
    

### Here is what we'll cover:

* [Prerequisites](#)
    

  

* [Step 1: Configure NGINX to Use SSL/TLS Encryption](#Configure-NGINX-to-Use-SSL/TLS-Encryption)
    

  

* [Step 2: Configure NGINX to Include Security Headers](#)
    

  

* [Step 3: Create a GitHub Repository and Push Your NGINX Configuration](#)
    

  

* [Step 4: Create a CircleCI Project and Link it to Your GitHub Repository](#)
    

  

* [Step 5: Create a CircleCI Configuration File and Define Your CI Pipeline](#)
    

  

* [Step 6: Test and Deploy Your Web Server with CircleCI](#)
    

  

Let's get started!

## Prerequisites

Before you start this guide, you need to ensure you have the following:

* A web server running NGINX. If you don't have one, you can follow this [guide](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04) to install NGINX on Ubuntu 20.04. You can also use any other operating system or cloud provider that supports NGINX.
    
* A GitHub account. If you don't have one, you can sign up for free [here](https://github.com/join).
    
* A CircleCI account. If you don't have one, you can sign up for free [here](https://circleci.com/signup/). You will also need to link your GitHub account to your CircleCI account.
    
* Some basic knowledge of [web development](https://www.freecodecamp.org/news/learn-web-development-with-this-free-20-hour-course/) and [Linux commands](https://www.freecodecamp.org/news/helpful-linux-commands-you-should-know/). You should be familiar with the concepts of web servers, SSL/TLS encryption, security headers, and CI. You should also be comfortable with using the command line and editing configuration files.
    

Once you have these, you are ready to proceed with the next steps.

## Step 1: Configure NGINX to Use SSL/TLS Encryption

SSL/TLS encryption ensures the transmission of data between your web server and clients. It safeguards against interception or manipulation of information. It also plays a role in verifying the identity and reliability of your web server.

You need an SSL/TLS certificate to use SSL/TLS for your web server. An SSL/TLS certificate contains information about your web server, such as its domain name, owner, and public key. The validity of the certificate is verified through the unique digital signature from a Certificate Authority (CA).

You can either purchase an SSL/TLS certificate from a commercial CA, such as DigiCert, Symantec, or GlobalSign, or you can just get one for free from a non-profit CA, such as Let's Encrypt. You can also create your own self-signed certificate, but this is not recommended for production use, as it will not be trusted by most browsers and clients.

In this guide, you will use Let's Encrypt to get a free SSL/TLS certificate for your web server. To use Let's Encrypt, you need to install a software client on your web server that can communicate with the CA and perform the necessary tasks.

One of the most common and recommended clients for Let's Encrypt is Certbot. Certbot is a command-line tool that can automatically request, install, and renew certificates for your web server. It can also configure your web server to use the certificates and enable HTTPS.

To install Certbot on your web server, run the following commands:

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx
```

After installing Certbot, use it to request and install a certificate for your web server. You need to provide your domain name and your email address for the certificate.

To request and install a certificate for your web server, run the following command:

```bash
sudo certbot --nginx -d yourdomain.com
```

Replace yourdomain.com with your actual domain name.

Follow the prompts and answer the questions. Certbot will automatically verify your domain ownership, obtain a certificate, and install it on your web server. It will also ask you whether you want to redirect all HTTP traffic to HTTPS. Choose option 2 to enable the redirection.

After the process is completed, you will see a message like this:

![certbot-success message](https://i.ibb.co/wBVfh1R/carbon-1.png align="left")

You have now successfully configured NGINX to use SSL/TLS encryption with a certificate from Let's Encrypt. You can now access your web server using HTTPS and see the lock icon in your browser.

![Lock Icon](https://i.ibb.co/b3pqJBB/secureverification2.png align="left")

You can also test your web server security using online tools, such as SSL Labs. You should see a grade of A or higher.

Note: Let's Encrypt certificates are valid for 90 days. Certbot can automatically renew them for you before they expire.

To enable the automatic renewal, you need to create a CRON job or a systemd timer that runs the following command at least once per day:

```bash
sudo certbot renew
```

You can also test the renewal process manually by running the following command:

```bash
sudo certbot renew --dry-run
```

This will perform a trial run without making any changes.

If you encounter any errors or issues, you can check the [Certbot documentation](https://eff-certbot.readthedocs.io/en/latest/) or the [Let's Encrypt community forum](https://community.letsencrypt.org/) for help.

## Step 2: Configure NGINX to Include Security Headers

Security headers help instruct the browser to apply certain security policies or restrictions when handling your web content. They can prevent or mitigate common web attacks, such as cross-site scripting (XSS), clickjacking, content injection, and more.

In this step, you will be adding security headers to your NGINX configuration. These headers include X Frame Options, X Content Type Options, X XSS Protection, and Content Security Policy.

### X-Frame-Options

The X-Frame-Options header tells the browser whether or not to allow your web page to be displayed in a frame, iframe, embed, or object element. This can help you prevent clickjacking attacks, where an attacker overlays a hidden frame on top of your web page and tricks the user into clicking on it.

There are three possible values for this header:

* DENY: This value prevents your web page from being displayed in any frame.
    
* SAMEORIGIN: This value allows your web page to be displayed in a frame only if the frame is from the same origin as your web page.
    
* ALLOW-FROM URI: This value allows your web page to be displayed in a frame only if the frame is from the specified URI.
    

To enable the X-Frame-Options header in NGINX, add the following line to your server block in your NGINX configuration file (/etc/nginx/sites-enabled/example.conf):

```nginx
add_header X-Frame-Options "SAMEORIGIN";
```

This will allow your web page to be displayed in a frame only if the frame is from the same origin as your web page. You can change the value to DENY or ALLOW-FROM uri according to your needs.

Save the file and restart NGINX to apply the changes.

### X-Content-Type-Options

The X Content Type Options header instructs the browser to perform MIME-type sniffing. This feature attempts to determine the content type of a resource by analyzing its content or file extension.

By using this header you can safeguard against content injection attacks. These attacks involve uploading a file with a content type to exploit the browser’s interpretation of it.

There is only one possible value for this header:

* nosniff: This value prevents the browser from performing MIME type sniffing.
    

To enable the X-Content-Type-Options header in NGINX, add the following line to your server block in your NGINX configuration file (/etc/nginx/sites-enabled/example.conf):

```nginx
add_header X-Content-Type-Options "nosniff";
```

This will prevent the browser from performing MIME type sniffing on your web resources.

Save the file and restart NGINX to apply the changes.

### X-XSS-Protection

The X-XSS-Protection header tells the browser to enable or disable its built-in XSS filter, which can detect and block some types of XSS attacks. This can help you prevent XSS attacks, where an attacker injects malicious code into your web page that executes in the browser.

There are three possible values for this header:

* 0: This value disables the XSS filter.
    
* 1: This value enables the XSS filter and sanitizes the page if an XSS attack is detected.
    
* 1; mode=block: This value enables the XSS filter and blocks the page if an XSS attack is detected.
    

To enable the X-XSS-Protection header in NGINX, add the following line to your server block in your NGINX configuration file (/etc/nginx/sites-enabled/example.conf):

```nginx
add_header X-XSS-Protection "1; mode=block";
```

This will enable the XSS filter and block the page if an XSS attack is detected. You can change the value to 0 or 1 according to your needs.

Save the file and restart NGINX to apply the changes.

### Content-Security-Policy

The Content-Security-Policy header tells the browser to enforce a set of rules that restrict what sources and types of content can be loaded and executed on your web page. This can help you prevent XSS, content injection, and other types of attacks that rely on loading malicious or untrusted content.

The value of this header is a complex policy that consists of multiple directives and values. Each directive specifies a type of content and a list of sources that are allowed or disallowed for that content.

For example, the following policy allows only scripts styles from the same origin, and images from the same origin or yourdomain.com:

```nginx
Content-Security-Policy: default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' yourdomain.com;
```

The Content-Security-Policy header is very powerful and flexible, but also very complicated and error-prone. You need to carefully design and test your policy to ensure that it does not break your web functionality or introduce new vulnerabilities. You can use tools like CSP Evaluator or CSP Scanner to check and improve your policy.

To enable the Content-Security-Policy header in NGINX, add the following line to your server block in your NGINX configuration file (/etc/nginx/sites-enabled/example.conf):

```nginx
add_header Content-Security-Policy "default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' yourdomain.com;";
```

This will enforce the policy that you described above. You can change the policy according to your needs.

Save the file and restart NGINX to apply the changes.

## Step 3: Create a GitHub Repository and Push Your NGINX Configuration

To create a GitHub repository and push your NGINX configuration files to it, follow these steps:

### Create a GitHub repository

First, log in to your GitHub account and go to the GitHub homepage.

Click on the plus icon in the top right corner of the page, and select "New repository" from the dropdown menu.

![Dropdown Menu](https://i.ibb.co/vkWX0BJ/dropdownmenu-edited.png align="left")

On the next page, enter a name for your repository in the "Repository name" field. This should be a short and descriptive name that accurately reflects the contents of the repository. For example, you can name it "nginx-config".

In the "Description" field, you can enter a longer description of the repository if you want. This is optional, but it can be helpful to provide more information about the purpose of the repository.

For example, you can write "A repository for storing and managing my NGINX configuration files".

You can set the visibility to whatever you prefer. If you want others to be able to see your work, set it to "Public". Otherwise, set it to "Private".

Leave the "Initialize this repository with a README" option unchecked, as you want to create an empty repository.

![Settting up New Repository](https://i.ibb.co/SQVJbqh/settingupnewrepo.png align="left")

Click on the "Create repository" button to create the repository.

Your new empty repository will be created and you will be taken to the repository page.

### Push your NGINX configuration files to the GitHub repository

On your web server, navigate to the directory where your NGINX configuration files are located. By default, this is /etc/nginx on most Linux distributions.

Initialize a new Git repository in this directory by running the following command:

```bash
git init
```

This will create a new .git directory in the current directory, which will be used to store all the version control information for your project.

Add all the configuration files that you want to include in the repository by running the following command:

```bash
git add .
```

This will add all the files in the current directory and its subdirectories to the repository. You can also specify individual files to be added by replacing the (.) with the file names, separated by spaces.

Then commit the files to the repository by running the following command:

```bash
git commit -m "Initial commit"
```

This will create the first commit in the repository, which will include all the files that were added in the previous step. The -m flag is used to specify a commit message, which should briefly describe the changes that were made in this commit.

Go back to your GitHub repository page and copy the URL of your repository. You can find it under the "Code" section. It should look something like this:

![github-url](https://i.ibb.co/GThsRSV/code-Button.png align="left")

On your web server, add the URL of your GitHub repository as a remote for your Git repository by running the following command:

```bash
git remote add origin https://github.com/username/nginx-config.git
```

Replace username with your GitHub username and nginx-config with your repository name. The origin is the name of the remote, which you can change to anything you want.

Push your local Git repository to the GitHub repository by running the following command:

```bash
git push -u origin master
```

This will push your master branch, which is the default branch in Git, to the origin remote, which is the GitHub repository that you created. The -u flag is used to set the upstream for your branch, which means that you can use git push or git pull without specifying the remote or the branch in the future.

Enter your GitHub username and password when prompted. If you have enabled two-factor authentication, you will need to use a personal access token instead of your password. You can generate one from your GitHub settings page.

You have successfully created a GitHub repository and pushed your NGINX configuration files to it. You can now view and manage your configuration files on GitHub.

## Step 4: Create a CircleCI Project and Link it to Your GitHub Repository

CircleCI is a platform that offers cloud-based and self-hosted options for continuous integration and delivery. It allows you to create and run pipelines that automate and streamline your web server deployment and update process.

To use CircleCI, you need to create a CircleCI project and link it to your GitHub repository. This will enable CircleCI to access your code and configuration files, and trigger builds whenever you push to GitHub.

To create a CircleCI project and link it to your GitHub repository, follow these steps:

### Sign up for CircleCI and connect your GitHub account

Start by logging in to your CircleCI account or sign up for free [here](https://circleci.com/login/).

On the CircleCI dashboard, click on the "Create Project" button in the top right corner of the page.

![Create project Button](https://i.ibb.co/wyPsNjk/project-button.png align="left")

On the next page, select "GitHub" as your version control provider and click on the "Connect with GitHub" button.

![Choosing Github](https://i.ibb.co/MhywfHF/choosing-github.png align="left")

On the next page, authorize CircleCI to access your GitHub account by clicking on the "Authorize circleci" button.

On the next page, Enter a “Project Name” and follow the remaining instructions to successfully create a CircleCI project.

![Enter Project Name](https://i.ibb.co/MkYZBTF/Project-Name.png align="left")

### Create a CircleCI project and link it to your GitHub repository

Next, create a new SSH key pair in your terminal:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/project_key -C email@example.com
```

Then copy the private key generated:

```bash
pbcopy < ~/.ssh/project_key
```

Next, enter it in the private key field:

![Enter private SSH Key](https://i.ibb.co/0Qs2TNJ/Private-SSH-Key.png align="left")

You will see a list of your GitHub repositories. Find the repository that you created in the previous step and click on the "Create Project" button next to it.

Now you will see a list of templates for different languages and frameworks. Since you are using Python and Flask, select the "Python" template and click on the "Use this config" button.

On the next page, you will see the generated CircleCI configuration file (config.yml) that defines your pipeline. You can review and edit the file if you want, or leave it as it is for now. Click on the "Start building" button to create the project and link it to your GitHub repository.

Your new CircleCI project will be created and linked to your GitHub repository.

You have now successfully created a CircleCI project and linked it to your GitHub repository. You can now configure and run your pipeline on CircleCI.

## Step 5: Create a CircleCI Configuration File and Define Your CI Pipeline

A CircleCI configuration file is a YAML file that defines your CI pipeline. A CI pipeline is a sequence of jobs that run whenever you push changes to your GitHub repository. Each job consists of steps that perform specific tasks, such as running commands, installing dependencies, or deploying your web server.

In this step, you will create a CircleCI configuration file and define your CI pipeline. You will use the Python template that you selected in the previous step as a starting point, and modify it to suit our needs. You will also explain what each step in the pipeline does and how it helps to automate and secure your web server deployment.

### Create a CircleCI configuration file

On your web server, navigate to the directory where your NGINX configuration files are located. By default, this is /etc/nginx on most Linux distributions.

Create a new directory called .circleci in this directory by running the following command:

```bash
mkdir .circleci
```

This is where you will store our CircleCI configuration file.

Then create a new file called config.yml in the .circleci directory by running the following command:

```bash
touch .circleci/config.yml
```

This is your CircleCI configuration file.

Open the config.yml file with your preferred text editor and paste the following code:

```yaml
version: 2.1

jobs:
  build:
    docker:
      - image: cimg/python:3.9
    steps:
      - checkout
      - run:
          name: Install dependencies
          command: |
            pip install -r requirements.txt
      - run:
          name: Run tests
          command: |
            pytest
  deploy:
    machine:
      image: ubuntu-2004:202101-01
    steps:
      - checkout
      - add_ssh_keys:
          fingerprints:
            - "YOUR_FINGERPRINT"
      - run:
          name: Deploy Nginx configuration
          command: |
            scp -r nginx root@YOUR_IP:/etc
            ssh root@YOUR_IP "systemctl restart nginx"

workflows:
  version: 2
  build-and-deploy:
    jobs:
      - build
      - deploy:
          requires:
            - build
          filters:
            branches:
              only: main
```

This is your CircleCI configuration file that defines your CI pipeline. You will explain each part of the file in the next section.

Finally, fave and close the file.

### Define your CI pipeline

Let's go through each part of the config.yml file and see what it does.

* Line 1: This indicates the version of the CircleCI platform you are using. 2.1 is the most recent version.
    
* Line 3: The jobs level contains a collection of children, representing your jobs. You specify the names for these jobs, for example, build, test, deploy.
    
* Line 6: This is the Docker image. The example shows cimg/python:3.9, which is a CircleCI-provided image that contains Python 3.9 and other common tools.
    
* Line 9: The run directive executes a shell command or script. You can specify a name and a command for each run directive.
    
* Line 11: The command attribute is a list of shell commands that you want to execute. In this case, you are installing the dependencies for your web application using pip.
    
* Line 12: This is another run directive that runs the tests for your web application using pytest.
    
* Line 13: deploy is the second child in the jobs collection. This job is responsible for deploying your NGINX configuration to your web server.
    
* Line 14: This specifies that you are using a machine executor for this job. A machine executor provides a full virtual machine with root access and various tools installed.
    
* Line 15: This is the machine image. The example shows ubuntu-2004:202101-01, which is a CircleCI-provided image that contains Ubuntu 20.04 and other common tools.
    
* Line 16: The steps collection is a list of run directives and other commands that you want to execute in this job.
    
* Line 18: The add\_ssh\_keys command adds your SSH keys to the machine. You need to provide the fingerprints of the keys that you want to use. You can generate and add SSH keys from your CircleCI settings page.
    
* Line 21: The command attribute is a list of shell commands that you want to execute. In this case, you are using SCP to copy your NGINX configuration files from the machine to your web server, and SSH to restart the NGINX service on your web server. You need to replace YOUR\_FINGERPRINT with the fingerprint of your SSH key, and YOUR\_IP with the IP address of your web server.
    
* Line 24: This indicates the version of the workflow syntax you are using. 2 is the most recent version.
    
* Line 29: The required attribute specifies the dependencies of this job. In this case, you are saying that the deploy job requires the build job to finish successfully before running.
    
* Line 30: The filters attribute specifies the conditions for running this job. In this case, you are saying that the deploy job should only run on the main branch of our GitHub repository.
    

### Push your CircleCI configuration file to your GitHub repository

On your web server, add, commit, and push your CircleCI configuration file to your GitHub repository by running the following commands:

```bash
git add .circleci/config.yml
git commit -m "Add CircleCI config file"
git push origin main
```

This will trigger a new build on CircleCI and run your CI pipeline.

Go to your CircleCI dashboard and click on the build-and-deploy workflow.

You can click on each job to see the details and logs of the steps.

Wait for the workflow to finish.

You have successfully created a CircleCI configuration file and defined your CI pipeline. You can now automate and secure your web server deployment with CircleCI. You can also modify and improve your configuration file according to your needs.

## Step 6: Test and Deploy Your Web Server with CircleCI

Now that you have created a CircleCI project and a configuration file for your CI pipeline, you can test and deploy your web server with CircleCI. You can trigger and monitor your CI pipeline from the CircleCI web app or the command line. You can also verify that your web server is deployed and secured correctly by using online tools or by accessing your web server using HTTPS.

### Trigger and monitor your CI pipeline from the CircleCI web app

To trigger and monitor your CI pipeline from the CircleCI web app, follow these steps:

* Go to the CircleCI dashboard.
    
* On the dashboard, you will see a list of your projects and pipelines. Find the project that you created in the previous step and click on it.
    
* On the project page, you will see a list of your branches and workflows. Find the branch that you pushed your CircleCI configuration file to in the previous step and click on the build-and-deploy workflow.
    
* On the workflow page, you will see a graphical representation of your pipeline, showing the status and duration of each job and step. You can click on each job or step to see the details and logs of the commands that were executed.
    
* Wait for the workflow to finish. If everything goes well, you will see a green check mark next to each job and step, indicating that they were successful.
    

You have successfully triggered and monitored your CI pipeline from the CircleCI web app. You can also trigger and monitor your CI pipeline from the command line.

### Trigger and monitor your CI pipeline from the command line

To trigger and monitor your CI pipeline from the command line, follow these steps:

* On your web server, navigate to the directory where your NGINX configuration files are located. By default, this is /etc/nginx on most Linux distributions.
    
* Make some changes to your configuration files, such as adding or removing security headers, and save them.
    
* Add, commit, and push your changes to your GitHub repository by running the following commands:
    

```bash
git add .
git commit -m "Update Nginx configuration"
git push origin main
```

This will trigger a new build on CircleCI and run your CI pipeline.

To monitor your CI pipeline from the command line, you can use the CircleCI CLI, which is a tool that allows you to interact with CircleCI from your terminal. You can install the CircleCI CLI by following the instructions on the official website.

After installing the CircleCI CLI, you can use the `circleci` command to perform various actions, such as listing your projects, pipelines, workflows, jobs, and artifacts. You can also use the --help flag to see the available options and arguments for each command.

To monitor your CI pipeline from the command line, you can use the circleci pipeline command to list and describe your pipelines.

For example, you can run the following command to list the pipelines for your project:

```bash
circleci pipeline list --org-slug <VCS>/<your-vcs-org-or-username> --project-slug <VCS>/<your-repo-name>
```

Replace `<VCS>` with either gh or bb depending on your version control system. Replace `<your-vcs-org-or-username>` with your GitHub or Bitbucket organization or username. Replace `<your-repo-name>` with your repository name. You will see something like this:

![Command Output](https://i.ibb.co/JKqc0cn/carbon-5.png align="left")

You can use the pipeline ID or number to describe a specific pipeline and see its details, such as the status, workflows, jobs, and steps. For example, you can run the following command to describe the latest pipeline for your project:

```bash
circleci pipeline describe --org-slug <VCS>/<your-vcs-org-or-username> --project-slug <VCS>/<your-repo-name> --pipeline-number <number>
```

Replace `<number>` with the pipeline number that you want to describe.

Wait for the pipeline to finish. If everything goes well, you will see a success message for each job and step, indicating that they were successful.

You have successfully triggered and monitored your CI pipeline from the command line. You can also verify that your web server is deployed and secured correctly.

### Verify that your web server is deployed and secured correctly

To verify that your web server is deployed and secured correctly, you can use online tools or access your web server using HTTPS. Here are some examples:

To verify that your web server is using the latest Nginx configuration that you pushed to GitHub, you can use a tool like [curl](https://curl.se/) or [wget](https://www.gnu.org/software/wget/) to make a request to your web server and inspect the response headers.

For example, you can run the following command to see the security headers that your web server is sending:

```bash
curl -I https://www.yourdomain.com
```

Replace yourdomain.com with your actual domain name.

You can compare the headers with the ones that you configured in your NGINX configuration file and see if they match.

To verify that your web server is using the SSL/TLS certificate that you installed with Certbot, you can use a tool like [SSL Labs](https://www.ssllabs.com/ssltest/) or [HTBridge](https://www.htbridge.com/ssl/) to scan your web server and check its SSL/TLS configuration and rating. You can check the details of your certificate, such as the issuer, validity, and chain. You can also check the grade of your SSL/TLS configuration, which should be A or higher.

To verify that your web server is accessible and functional using HTTPS, you can simply open your web browser and visit your web server using HTTPS. For example, you can go to https://www.yourdomain.com and see your web page.

You can check the lock icon in your browser, which indicates that your connection is secure. You can also click on the icon and see the details of your certificate and connection.

![Viewing Certificate](https://i.ibb.co/dGwr57V/certificate-viewer.png align="left")

## Conclusion

In this article, you have learned how to secure your web server using NGINX and CicleCI. NGINX and CircleCI, when used together, can provide a powerful solution for ensuring the continuous security of your web applications.

Stay ahead of the curve by integrating these technologies into your workflow, and empower your team to deliver secure and reliable web services.

Please don't forget to share this guide with your colleagues, friends, and online communities if you find it insightful.
