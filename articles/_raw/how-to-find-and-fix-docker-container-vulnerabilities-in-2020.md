---
title: How to find and fix Docker container vulnerabilities
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-20T16:20:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-and-fix-docker-container-vulnerabilities-in-2020
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/New-Project--1-.jpg
tags:
- name: Docker
  slug: docker
- name: Security
  slug: security
seo_title: null
seo_desc: 'By Dipto Karmakar

  Containerization allows engineering teams to create a sandbox environment in which
  to run and test applications. Containers are mostly made up of open-source images
  pulled in from docker hub or other public image repositories.

  But t...'
---

By Dipto Karmakar

Containerization allows engineering teams to create a sandbox environment in which to run and test applications. Containers are mostly made up of open-source images pulled in from docker hub or other public image repositories.

But these open-source images may sometimes contain vulnerabilities which can jeopardise the safety of containers and in turn its host computer/server.

Since these containers run on a host machine, it is possible to hijack containers in production if they’re left unprotected.

A good example of such a hack is [Tesla’s cryptojacking attack](https://cointelegraph.com/news/tesla-cryptojacked-hackers-use-passwordless-system-to-mine-crypto) on an unprotected Kubernetes cluster. In this attack, the attackers were able to download and run a malicious script for mining crypto using GPUs provided by Tesla’s K8s (Kubernetes) cluster. They were able to keep this attack under the radar by keeping CPU usage to a minimum and also running the script at specific time intervals.

In the course of this article, we will take a look at common container vulnerabilities and possible ways to fix them.

## Common container vulnerabilities and how to fix them

Containers are used by ops engineers to package and deploy a software/application in a closed and controlled environment.

In a bid to avoid re-inventing the wheel and speed up time to market, already existing open-source images are pulled in to satisfy the dependencies needed to run the software. These images often contain certain vulnerabilities which make the entire container and its host vulnerable to malicious attacks.

Listed below are some common container vulnerabilities and exposures as well as how to mitigate them.

### Cryptojacking

Cryptojacking is a type of attack where a malicious script is used to steal a device’s computational resources for mining cryptocurrencies.

Recently, a vulnerability was discovered on Docker with dictionary entry [CVE-2018-15664](https://nvd.nist.gov/vuln/detail/CVE-2018-15664). This vulnerability makes it possible for attackers to gain root access to a host’s machine.

Aside from being able to use the host’s machine’s CPU and GPU resources to mine crypto, attackers can also steal sensitive credentials, carry out DoS attacks, launch phishing campaigns, and more.

Containers can be susceptible to cryptojacking if they contain malicious images which give attackers root access to the entire container. They're also vulnerable if the docker container API endpoints are publicly accessible on the internet without passwords or security firewalls, like in the case of Tesla.

%[https://twitter.com/bad_packets/status/1199087675833085959?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fpaperusercontent.com%2Fintegrations%2Fembed%2Fiframe%2Ftweet%3Fid%3D1199087675833085959] 

### Malicious open-source images

A vulnerability which makes it possible to overwrite the host’s runc binary gives attackers the leeway to execute commands with root access. Docker engines which predate v18.09.2 make containers with attacker-controlled images susceptible to the [CVE-2019-5736](https://nvd.nist.gov/vuln/detail/CVE-2019-5736) vulnerability.

Engineers are advised as much as possible to make use of official Docker images provided by docker. After all, there’s even a Docker sponsored team which works closely with software maintainers/publishers and security experts to ensure the security of official Docker images.

### Static Dockerfiles

One of the principles of containers is that an image is immutable. This means when an image is built, its content is unchangeable. That in itself gives rise to vulnerabilities which result from outdated packages/libraries/images contained in an image.

Therefore, it's a good idea to incorporate vulnerability scanners in CI/CD processes in order to identify vulnerable container images. Since images are immutable, rolling out a newly built container with updated dependencies will help curb the security vulnerabilities as [container patching](https://cloud.google.com/blog/products/containers-kubernetes/exploring-container-security-how-containers-enable-passive-patching-and-a-better-model-for-supply-chain-security) is discouraged.

## How to find container vulnerabilities

In the previous section, we took a look at the possible ways vulnerabilities can creep into docker containers.

Finding vulnerabilities in our containers before it gets to production will help avoid possible security breaches and keep malicious [attackers away](https://en.wikipedia.org/wiki/An_apple_a_day_keeps_the_doctor_away).

> As they say - an ounce of prevention is worth a pound of cure.

In this section, we will take a look at the possible ways you can stay ahead of container vulnerabilities.

### Using Docker Bench for Security

[Docker bench](https://github.com/docker/docker-bench-security) for security is a script that tests all docker containers on the host computer/server for best practices for deploying containers in production. These tests are based on the [CIS docker benchmark](https://www.cisecurity.org/benchmark/docker/).

For a test run, you can pull the `docker/docker-bench-security` image and test existing containers on your local machine like so:

```bash
docker run -it --net host --pid host --userns host --cap-add audit_control \
    -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
    -v /etc:/etc:ro \
    -v /usr/bin/docker-containerd:/usr/bin/docker-containerd:ro \
    -v /usr/bin/docker-runc:/usr/bin/docker-runc:ro \
    -v /usr/lib/systemd:/usr/lib/systemd:ro \
    -v /var/lib:/var/lib:ro \
    -v /var/run/docker.sock:/var/run/docker.sock:ro \
    --label docker_bench_security \
    docker/docker-bench-security
```

**Note**: this command doesn’t work well in OSX. See this [GitHub issue](https://github.com/docker/docker-bench-security/issues/158) for details.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image_preview.png align="left")

### Scanning for vulnerabilities in GCR

Docker image repositories (for example, [GCR](https://cloud.google.com/container-registry)) make it possible for engineers to run vulnerability scans for images in the container registry.

To enable vulnerability scanning in GCR (Google container registry), head over to the [container registry settings](https://console.cloud.google.com/gcr/settings) on the Google cloud console and click on "enable vulnerability scanning" like so:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image_preview--1-.png align="left")

When a vulnerability scan is complete, you’ll see a result like in the image below if vulnerabilities exist:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image_preview--2-.png align="left")

### Using Enterprise-Grade Solutions

There are enterprise-grade containerisation security suites which manages vulnerabilities and enforces deployment policies throughout a container's lifecycle.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image_preview--3-.png align="left")

In addition, this product suite also integrates seamlessly with popular CI/CD tools and container registries. This allows it to provide risk-free deployments as well as end-to-end container management from deployment to production.

## Conclusion

Containers make it possible for engineering teams to roll out software seamlessly. However, this ease comes at the cost of security.

There are a couple of CVEs (common vulnerability exposures) in docker containers recorded in recent years. Some of them have been resolved in recent docker-engine updates with the remainder promised in future [patch releases](https://docs.docker.com/engine/release-notes/).

Engineering teams should have security in mind when building and deploying containers. They should also enforce container security policies in their DevOps lifecycles.
