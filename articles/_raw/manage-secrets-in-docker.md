---
title: How to Manage Secrets in Docker
subtitle: ''
author: Abraham Dahunsi
co_authors: []
series: null
date: '2024-01-03T16:26:00.000Z'
originalURL: https://freecodecamp.org/news/manage-secrets-in-docker
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/feature-image.jpg
tags:
- name: Docker
  slug: docker
- name: Security
  slug: security
seo_title: null
seo_desc: 'Protecting sensitive data like API keys, passwords, and certificates in
  your Docker projects can be quite daunting and error-prone. And many devs neglect
  it when dealing with applications deployed in containers.

  There is no global way of storing and ...'
---

Protecting sensitive data like API keys, passwords, and certificates in your Docker projects can be quite daunting and error-prone. And many devs neglect it when dealing with applications deployed in containers.

There is no global way of storing and sharing secrets in containers. Traditional methods of storing them, such as hardcoding them in source code and tucking them away in text files, leave them vulnerable to exposure and exploitation.

Docker Secrets was introduced to address this issue. Docker secrets offer a secure way to store your sensitive data, safeguarding your applications from the pitfalls of careless storage.

In this article, you will learn what Docker secrets are and their default structures. I will also walk you through the steps on how to manage secrets in Docker to safeguard your sensitive data and unlock the full potential of your Docker applications.

## What are Docker Secrets?

To effectively manage secrets, you must first understand what they are. Docker secrets include a wide array of sensitive data, including:

* Credentials such as usernames and passwords for databases, servers, third-party services, and more.
    
* API keys, which are unique keys that grant access to external APIs and services.
    
* Digital certificates, which are used for secure communication and authentication, such as SSL/TLS certificates.
    
* Encryption keys, which are keys used to encrypt sensitive data or files.
    
* Tokens, such as Access tokens for authentication and authorization purposes.
    
* Software licenses that may contain sensitive information.
    
* Other sensitive data that could pose a security risk if exposed.
    

### How Secrets Are Stored

Docker offers several pathways to create and reference secrets within your containerized environment:

* Files: You can store secrets in plain text files, but this method is less secure and not recommended for production environments.
    
* Environment Variables: You can set secrets as environment variables within containers, but this may still expose them in logs and process listings.
    
* Docker Secrets: You can utilize Docker's built-in secrets management feature for basic encryption and access control.
    
* Docker Compose: You can define secrets within your Docker Compose files for convenient management during development and testing.
    
* Docker Swarm Secrets: You can leverage advanced secret management capabilities for clustered Docker environments, providing secure storage and granular access control.
    

## Solutions for Managing Key Secrets

Docker offers two main ways to manage your sensitive data: built-in solutions within the platform itself and external solutions for more advanced needs.

### Built-in solutions

For those starting out or seeking basic secret management, Docker's built-in solutions offer a convenient entry point (this guide is based on the built-in solutions):

* Docker Secrets: This lightweight method allows creating and injecting basic secrets into containers via CLI or Compose files. While easy to use, it lacks advanced features like centralized storage and granular access control. It is best suited for simple deployments with minimal secrets.
    
* Docker Swarm Secrets: For clustered environments, Swarm secrets offer a step up in security. Secrets reside securely on Swarm managers and are distributed to nodes on demand. You gain granular access control and audit trails, making it ideal for production deployments with multiple secrets.
    

### External solutions

For robust security and advanced features, external secrets management platforms stand out. Here are some popular options:

* Vault: A feature-rich, open-source platform offering encryption, access control, logging, and audit trails. It integrates seamlessly with various tools and platforms, making it a versatile choice for complex deployments.
    
* Keywhiz: Another open-source option, Keywhiz, focuses on ease of use and cloud-native deployments. Its lightweight design makes it ideal for managing secrets in Kubernetes environments.
    
* AWS Secrets Manager: If you're an AWS user, this native service provides secure storage, rotation, and retrieval of secrets, integrating seamlessly with your existing infrastructure.
    
* Cloud Native Options: Most major cloud providers offer dedicated secrets management services like Azure Key Vault and GCP Secret Manager. These leverage the security and scalability of their respective platforms for secure and streamlined management.
    

### How to choose the right solution

The optimal approach depends on your personal or team’s specific needs and environment. Consider these factors:

* Application complexity: Complex applications with numerous secrets likely require the advanced features of an external solution.
    
* Deployment environment: Production environments demand robust security and access control, favoring external options.
    
* Team expertise: Evaluate your team's familiarity with managing and integrating external tools.
    
* Scalability needs: If you envision scaling your containerized infrastructure, choose solutions that cater to multi-node deployments.
    

Remember, there's no one-size-fits-all approach. Prioritize secure practices for creating, storing, rotating, and deleting secrets, regardless of your chosen method.

## How to Get Started with Managing Secrets

Now, let's get practical, as I will show you how to create and manage Docker Secrets.

### How to create a Docker secret

Start by creating a file with a secret, like a file containing your password:

```bash
$ echo yourpassword > password.txt
```

Next, create the Docker secret object using the `docker secret` command:

```bash
$ docker secret create your_secret ./path/to/password.txt
```

In the process of creating and managing Docker Secrets, you start by generating a file containing a secret, such as a password, using the `echo` command and saving it to a file (such as `password.txt`).

After that, you use the `docker secret create` command to establish a Docker secret object named `your_secret` from the contents of the specified file (`./path/to/password.txt`). This sequence of commands enables the creation and storage of confidential information, like passwords, into your Docker environment securely.

### How to initiate a service using the secret

Now to create a service that uses the secret, use this template:

```bash
$ docker service create --name <service_name>  --secret <secret_name>   <image_name>:<tag>
```

The `docker service create` command starts the creation of a new service within a Docker Swarm cluster. To customize and configure the service, several options are available:

1. `--name <service_name>`: Assigns a specific name to the service, aiding in easy identification. For example, `--name my-nginx-service` designates the service as `my-nginx-service`.
    
2. `--secret <secret_name>`: Uses an existing Docker Swarm secret into the service. This allows the secret to be accessed within the containers associated with the service. For instance, `--secret your_secret` associates the `your_secret` secret with the service.
    
3. `<image_name>:<tag>`: Specifies the Docker image to be utilized for the service, including its tag. For example, `<image_name>:<tag>` can be replaced with `nginx:latest` to use the latest version of the Nginx image for the service.
    

## How to Manage Docker Secrets

### How to list Docker secrets

You can check out the list of Docker Secrets available by using the `Docker ls` command:

```bash
$ docker secret ls
```

This is what the output should look like:

![Screenshot-2023-12-23-171215-1](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-23-171215-1.png align="left")

This command does not provide comprehensive information about your Docker secrets, as only the metadata is displayed. To inspect a specific secret's metadata, use the `Docker Inspect` command:

```bash
$ docker secret inspect <secret_name> #use 'your_secret' for this example
```

When executed, it provides a comprehensive output that includes metadata about the specified secret, such as its ID, version, and labels. Additionally, it displays the secret's creation and update timestamps. This inspection command is valuable for administrators and developers seeking to understand the properties and attributes of a Docker secret, aiding in effective management and utilization within the Docker Swarm cluster.

However, Docker secrets prioritize security, and unveiling their contents through CLI commands would compromise their integrity. To access the secret's content, it must be attached to a service within your Docker Swarm. Subsequently, the secret becomes accessible as a file within the containers associated with that service.

#### How to remove Docker secrets

To remove and delete unused Docker Secrets use the `docker secret rm` command:

```bash
$ docker secret rm your_secret
```

Remember, this action is irreversible, so make sure to double-check your choice!

## How to Use Docker Secrets with Docker Compose

If you are not a big fan of using the command-line interface, then don’t worry, as you can still use Docker compose files to manage Docker secrets.

```yaml
version: '3.1'

services:
  web:
    image: nginxdemos/hello
    secrets:
      - your_secret
      - your_external_secret
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./conf/nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web

secrets:
  your_file_secret:
    file:  ./path/to/password.txt
  your_external_secret:
    external: true
```

This YAML configuration is a Docker Compose file, specifying the setup for two services –`web` and `nginx`– along with some associated configurations and secrets.

Let's me breakdown what I did.

### Services configuration

The `web service` uses the image `nginxdemos/hello` and includes two secrets: `your_secret` and `your_external_secret`.

The `nginx service` uses the `nginx:latest` image and maps port 80 on the host to port 80 on the container.

Also, it mounts the local file `./conf/nginx.conf` into the container at `/etc/nginx/nginx.conf` and depends on the `web' service`, which means that `web` needs to be running before `nginx` starts.

### Secrets configuration

There are two secrets defined.

The first one is `your_file_secret`, which reads the content of `./path/to/password.txt` and creates a secret from it.

The second one is `your_external_secret`, which specifies that this secret is external. This implies that the actual secret content is managed externally, and the configuration here is a reference to that external secret.

In summary, this Docker Compose file example sets up two services, `web` and `nginx`, with the `nginx` service depending on `web`. Secrets, both from files (`your_file_secret`) and external sources (`your_external_secret`), are utilized for the secure handling of sensitive information within the services. The `nginx` service also has additional configurations related to port mapping and volume mounting.

## Best Practices

Below are some tips and best practices to follow when working with Docker Secrets.

### How to Choose a Method

Selecting the right method depends on several factors:

* Application Needs: Consider the complexity of your application and its security requirements. Simple applications might thrive with built-in Docker secrets, while complex deployments might necessitate an external solution.
    
* Infrastructure: Analyze your existing infrastructure and tools. If you already utilize specific cloud platforms or orchestration engines, their native secrets management solutions might offer seamless integration and familiarity.
    
* Desired Control: Assess your need for advanced features like granular access control, automated rotation, and centralized management. External solutions typically offer greater control compared to built-in options.
    

### How to Secure Secret Creation and Storage

The foundation of secure secrets management lies in protecting the data itself:

* Encryption: Implement encryption for secrets both at rest (stored on disk) and in transit (transmitted between systems). Utilize strong encryption algorithms and key management best practices.
    
* Access Control: Enforce the principle of least privilege. Grant access to secrets only on a need-to-know basis. Consider employing role-based access control (RBAC) mechanisms for granular control.
    

### Secret Rotation and Lifecycle Management

Preventing the compromise of even a single secret can significantly mitigate risk. Employ these measures:

* Rotation: Regularly rotate your secrets, even if they haven't been exposed. Define automated rotation schedules based on best practices and your specific security needs.
    
* Lifecycle Management: Implement secure deletion processes for outdated or unused secrets. Avoid simply deleting files, as data recovery tools might still access them. Secure deletion methods offer a safer approach.
    

### How to Integrate Secrets with CI/CD Pipelines

Incorporate secrets management seamlessly into your development workflow:

* Injection Techniques: Utilize environment variables, dynamic secret injection tools, or file mounts to provide secrets to containers only when needed. This avoids their storage within container images.
    
* Automated Credential Management: Integrate your chosen secrets management solution with your CI/CD pipeline to automate credential retrieval, rotation, and injection as part of your deployment process.
    
* Minimize Exposure: Avoid logging secrets in plain text during the build or deployment stages. Implement masking techniques or utilize tools that handle secrets securely within your CI/CD pipeline.
    

Using these best practices and customizing them to your specific needs, you can build a robust and secure foundation for managing your Docker secrets.

Remember, the solution you choose is just one piece of the puzzle. Constant vigilance, adherence to best practices, and regular security audits are crucial for maintaining a resilient defense against potential threats.

## Additional Resources

Below are some additional resources to use if you want to learn more about Docker Secrets and other security practices:

* [Docker documentation](https://docs.docker.com/) Official guides for Docker secrets and secure practices.
    
* Secret management platforms guides: Each solution provides extensive documentation and tutorials.
    
    * [Official Docker Docs guide on managing Docker secrets (read for more in-depth knowledge)](https://docs.docker.com/engine/swarm/secrets/)
        
    * [A guide to using an external solution: Vault](https://developer.hashicorp.com/vault/doc)
        
    * [A guide to AWS Secrets manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
        
* Community Forums and Blogs: Actively engage with the security and Docker communities for further learning and support.
    
    * [Stackoverflow](https://stackoverflow.com/)
        
    * [The official blog page of the Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/blog/)
        

## Conclusion

Now, in this guide, you've learned what Docker secrets are, how they are stored, the different methods of storing them, and how to manage Docker secrets in your personal projects.

Remember, secure secrets are the cornerstones of secure applications. Build your fortress wisely, and your data will remain safe and sound.

Please feel free to ask if you have any specific questions on any of these aspects!

Also, if you liked this guide and found it insightful, please make sure to share it with your colleagues and online communities.
