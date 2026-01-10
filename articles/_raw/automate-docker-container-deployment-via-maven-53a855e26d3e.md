---
title: How to automate Docker container deployment via Maven
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-13T09:40:37.000Z'
originalURL: https://freecodecamp.org/news/automate-docker-container-deployment-via-maven-53a855e26d3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4egCh1HO_8jjLK8Ahhw4CA.png
tags:
- name: automation
  slug: automation
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ravindu Fernando

  This article is intended for people who are using Maven as a build and dependency
  management tool for JAVA applications. It will show you how to integrate docker
  container build, tag and push workflows into their existing Maven bu...'
---

By Ravindu Fernando

This article is intended for people who are using Maven as a build and dependency management tool for JAVA applications. It will show you how to integrate docker container build, tag and push workflows into their existing Maven build management ecosystem.

Having the ability to build, tag and push your application as a container right off from the Maven lifecycle commands itself is a pretty cool thing to have. It just makes things easy and quick if you are trying to bring in the power of containers to deploy your applications and all-ready using Maven for dependency management.

If we take a look at existing solutions for integrating docker container deployment into Maven, there are several ones out there, like [spotify maven docker plugin](https://github.com/spotify/docker-client), [fabric8io docker maven plugin](https://github.com/fabric8io/docker-maven-plugin) etc. But all these solutions bring in unwanted complexity, additional learning curve and too much change into your existing application code. Yet there is a simpler and easy way to achieve this without the use of any third-party plugin.

If you note Maven’s Ant plugin, it allows us to run external commands. So by using the Ant plugin, we have the capability to run docker build, tag, push or just any command as you wish. The only thing that we have to do is to provide a proper Dockerfile for building the Docker image for your application and necessary set of commands and Maven configurations into the pom.xml file.

> For explaining the steps involved in this process, I will use a sample JAVA application. It contains all the code samples used in the following steps. You can clone it from [here](https://github.com/rav94/dockermavensample).

### **Step 1 | Create the Dockerfile**

> Dockerfile should be stored within the path **_src/main/docker/Dockerfile_** of your JAVA application.

```
# Pull base imageFROM tomcat:8.0.30-jre7# MaintainerMAINTAINER "ravindu@emojot.com"
```

```
# Set Environment propertiesENV JAVA_OPTS=-Denvironment=production# Copy war file to tomcat webapps folderCOPY /dockermavensample.war /usr/local/tomcat/webapps/
```

### **Step 2 | Update the pom.xml to copy all Docker-related resources into the target directory**

> We can use maven-resource-plugin to copy resources.

```
<plugin>    <artifactId>maven-resources-plugin</artifactId>    <executions>        <execution>            <id>copy-resources</id>            <phase>validate<;/phase>            <goals>                <goal>copy-resources</goal>            </goals>            <configuration>                <outputDirectory>${basedir}/target</outputDirectory>;                <resources>                    <resource>                        <directory>src/main/docker</directory>                        <filtering>true</filtering>                    </resource>                </resources>            </configuration>        </execution>    </executions></plugin>
```

### **Step 3 | Update the pom.xml to allow build and tag the Docker image via Maven’s Ant plugin**

```
&lt;plugin>    &lt;groupId>org.apache.maven.plugins</groupId&gt;    <artifactId&gt;maven-antrun-plugin&lt;/artifactId>    <version>1.6&lt;/version>    <executions>        <execution&gt;            <id>prepare-package<;/id>            <phase&gt;package</phase>            &lt;inherited>false<;/inherited>            <configuration>                &lt;target>                    <exec executable="docker">                        <arg value="build"/>                        <arg value="-t"/>                        <arg value="dockermavensample:${project.version}"/>                        <arg value="target"/>;                    <;/exec>                &lt;/target&gt;            </configuration>            <goals>                <goal>run</goal>            </goals>        </execution>    </executions></plugin>
```

Maven’s Ant plugin will execute the docker command in the package phase of Maven lifecycle in the following order, which will build the docker image from the Dockerfile which was copied into the target folder in step 2.

```
docker build -t dockermavensample:1.0.0 target
```

### **Step 4 | Update the pom.xml file to allow pushing Docker Image to remote Docker repository**

> Ideally for production, you would have to push your Docker images into your own private Docker registry or use a third party Docker image repository which allows storing private Docker images so that others cannot pull your Docker images directly.

```
<plugin>    <;groupId>org.apache.maven.plugins</groupId>;    <artifactId>maven-antrun-plugin<;/artifactId>    <version>1.6</version>    <executions>;        <execution>            <phase>install</phase>            <inherited>false</inherited>            &lt;configuration>                <target&gt;                    <exec executable="docker">                        <arg value="tag"/>                        <arg value="dockermavensample:${project.version}"/>                        <arg value="dockermavensample:latest"/&gt;                    </exec>                    <exec executable="docker">                        <arg value="push"/>                        <arg value="dockermavensample:latest"/>                    </exec>                </target>            </configuration>            <goals>                <goal>run</goal>            </goals>        </execution>    </executions></plugin>
```

In addition to the above steps, you may want to have control over how you are running these docker related commands in your Maven lifecycle. For that, you can use Maven profiles to logically divide above plugin definitions. Then execute those only when the profile related to that action is invoked.

**Take a look at following sample profiles:**

```
&lt;profile>    <id>dockerBuild</id>    <build>        <plugins>            <plugin>                <artifactId>maven-resources-plugin</artifactId>                <executions>                    &lt;execution>                        <id>copy-resources</id>                        <phase>validate</phase>;                        <goals&gt;                            <goal&gt;copy-resources</goal>                        </goals&gt;                        <configuration&gt;                            <outputDirectory&gt;${basedir}/target</outputDirectory>                            &lt;resources>                                <resource>                                    <directory>src/main/docker</directory&gt;                                    &lt;filtering>true</filtering>                                </resource&gt;                            </resources>;                        &lt;/configuration>                    </execution&gt;                </executions&gt;            </plugin>            <plugin>                <groupId>org.apache.maven.plugins</groupId>                <;artifactId>maven-antrun-plugin</artifactId>                <;version>1.6</version>                <executions>                    <execution>                        <id&gt;prepare-package</id>                        &lt;phase>package</phase>                        <inherited>false</inherited&gt;                        <configuration&gt;                            <target>                                <exec executable="docker">                                    <arg value="build"/>                                    &lt;arg value="-t"/>                                    <arg value="dockermavensample:${project.version}"/>                                    <arg value="target"/>                                </exec>                            </target>                        </configuration>                        <goals>                            <goal>run</goal>                        </goals>                    </execution>                </executions>            </plugin>        </plugins>    </build>
```

```
    &lt;activation>        <activeByDefault>true</activeByDefault>;    </activation></profile>
```

```
<!-- docker Image push and release profile -->&lt;profile>    <id&gt;dockerRelease</id&gt;    <build>        <plugins>            <plugin>                <groupId>org.apache.maven.plugins</groupId>                <artifactId&gt;maven-antrun-plugin</artifactId>                <version>1.6</version>                <executions>                    <execution>                        <phase&gt;install</phase>                        &lt;inherited>false</inherited&gt;                        <configuration>                            <target>                                <exec executable="docker">                                    <arg value="tag"/>                                    <arg value="dockermavensample:${project.version}"/>                                    <arg value="dockermavensample:latest"/>                                </exec&gt;                                <exec executable="docker">                                    <arg value="push"/>                                    <arg value="dockermavensample:latest"/>                                </exec>                            <;/target&gt;                        &lt;/configuration>                        <goals>                            <goal>run</goal>                        </goals>                    </execution>                </executions>            </plugin>        </plugins>    </build></profile>
```

After completing the above steps, just run

```
mvn clean install -P dockerBuild,dockerRelease
```

Now your JAVA application is packaged as a container and pushed into a remote docker repository as well. You can test whether the image you created is working by running following commands,

![Image](https://cdn-media-1.freecodecamp.org/images/H0mmu0zzMqdWt-UiERarfC6tPqgX5ZUUqUZS)
_After running dockerBuild profile, the Docker image should be available locally_

![Image](https://cdn-media-1.freecodecamp.org/images/Y854emSEIN8QMwYSIThdPU3VdLhgFjUXXK-M)
_Run dockermavensample:1.0.0 Docker Image_

![Image](https://cdn-media-1.freecodecamp.org/images/dPF05Esb-3p1AhDuoKncJzRQk0u76-9a5o4k)
_Apache Tomcat Home Page_

![Image](https://cdn-media-1.freecodecamp.org/images/KwXo738tVALAG3-fpvItOR4DqSKRcGuLDWVs)
_Kaboom! :)_

As you can see we can use already available Maven features and plugins to create a well-structured build pipeline for deploying our applications as containers.

**Sample Project:**

[**rav94/dockermavensample**](https://github.com/rav94/dockermavensample)  
[_Demo Project for showcasing Automating Container Deployment via Maven - rav94/dockermavensample_github.com](https://github.com/rav94/dockermavensample)

Thanks for reading!

