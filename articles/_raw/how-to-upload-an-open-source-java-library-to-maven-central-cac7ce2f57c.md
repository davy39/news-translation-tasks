---
title: How to Upload an Open-Source Java Library to Maven Central
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T01:38:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-upload-an-open-source-java-library-to-maven-central-cac7ce2f57c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E-Rmyde820J8T6tWETnpTA.png
tags:
- name: Java
  slug: java
- name: Libraries
  slug: libraries
- name: open source
  slug: open-source
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Seun Matt

  This article is a comprehensive guide, from start to finish, on how to deploy a
  Java library to Maven Central so everyone can use it by including the dependency
  in their project(s).

  It goes without saying that there has to be a Java libr...'
---

By Seun Matt

This article is a comprehensive guide, from start to finish, on how to deploy a Java library to Maven Central so everyone can use it by including the dependency in their project(s).

It goes without saying that there has to be a Java library for it to be uploaded. Hence, the first thing is creating a Java library that’s unique, of quality code standard, and that will be beneficial to the developer community. Of course, you’ve got that already — that’s why you’re reading this after all _(or maybe you’re planning on creating one)_.

In summary, to upload a shiny new Java library to Maven Central, we’ll have to reserve our Group ID, provide the required details in the project’s _pom.xml_, sign the generated artifacts with GnuPG and, finally, deploy to Sonatype’s Nexus Repository Manager.

### STEP ONE:

The first step is for us to make sure our open-source library is available on a publicly accessible code repository like Github. Then we can proceed to reserve our desired Group ID. The Group ID should ideally be **unique to an individual or organization** — as in a domain. Examples of Group ID includes **_com.smattme_** and **_org.apache.commons_**_._

So, we are going to create a JIRA account [here](https://issues.sonatype.org/secure/Signup!default.jspa) and then [log in](https://issues.sonatype.org/login.jsp) to create a new project ticket. Clicking on the **create** button at the top of the website will load a modal where we’ll supply the Group ID (e.g. com.smattme), SCM URL (e.g. [_https://github.com/SeunMatt/mysql-backup4j.git_](https://github.com/SeunMatt/mysql-backup4j.git)_),_ project URL (e.g. [_https://github.com/SeunMatt/mysql-backup4j_](https://github.com/SeunMatt/mysql-backup4j)_),_ Summary (which can be the name of the library like _mysql-backup4j_) and finally project description.

**NOTE:** In the modal for creating a new project ticket, ensure the **Project** field is set to _Community Support — Open Source Project Repository Hosting (OSSRH)_ and the **Issue Type** is _New Project_**.**

The creation of the new ticket project will trigger the creation of repositories on Sonatype’s OSS Repository Hosting (OSSRH) that’ll be synced to Maven Central after deploying our artifacts.

It’s important not to deploy until there’s an email confirmation that the issue created has been resolved. If there’s any problem along the line, we can always comment on the issue to get help and/or explanation.

### STEP TWO:

Now that we’ve successfully registered our Group ID, the next thing to do is update the project’s **_pom.xml_** with the necessary information. Let’s start by providing the project’s name, description and URL as well as the coordinates and packaging information:

```
<groupId>com.smattme</groupId>
```

```
<artifactId>mysql-backup4j</artifactId>
```

```
<version>1.0.1</version>
```

```
<packaging>jar</packaging> 
```

```
<name>${project.groupId}:${project.artifactId}&lt;/name> 
```

```
<description> This is a simple library for backing up mysql databases and sending to emails, cloud storage and so on. It also provide a method for programmatically, importing SQL queries generated during the export process</description> 
```

```
<url>https://github.com/SeunMatt/mysql-backup4j</url>
```

Up next is the license and developers information. In this case, we’ll be using an MIT license. If any other license is used, all that’s needed is a corresponding URL to such license. If it’s an open-source license, there’s a good chance it’s going to be available on _opensource.org_:

```
<licenses> <license>  <name>MIT License</name>              <url>http://www.opensource.org/licenses/mit-license.php</url>       <;/license> </licenses> <developers> 
```

```
 <developer>   <name>Seun Matt</name>   <email>smatt382@gmail.com</email>      <organization>SmattMe</organization> <organizationUrl>https://smattme.com</organizationUrl></developer> 
```

```
</developers>
```

Another important piece of information required is the source code management (SCM) details:

```
<scm>   <connection>scm:git:git://github.com/SeunMatt/mysql-backup4j.git</connection>   <developerConnection>scm:git:ssh://github.com:SeunMatt/mysql-backup4j.git</developerConnection>   <url>https://github.com/SeunMatt/mysql-backup4j/tree/master</url> </scm>
```

In this case, the project is hosted on Github, thus the reason for the supplied values. Example configurations for other SCM can be found [here](https://central.sonatype.org/pages/requirements.html#scm-information).

### STEP THREE:

In this step, we’ll be configuring our project for deployment to the OSSRH using the Apache Maven Plugin. The plugin requires that we add a **_distributionManagement_** section to our **_pom.xml_**:

```
<distributionManagement> 
```

```
  <snapshotRepository>   <id>ossrh</id>        <url>https://oss.sonatype.org/content/repositories/snapshots</url> </snapshotRepository> 
```

```
<repository> <id>ossrh</id> <url>https://oss.sonatype.org/service/local/staging/deploy/maven2/</url> </repository> 
```

```
</distributionManagement>
```

We’ll supply the user credentials for the configured repositories above by adding a **_<serve_**rs> ent**_ry to settin_**gs.xml which can be found in the user’s home directory _e.g. /Users/sma_tt/.m2. Note tha**t** the id is the same as that o**f the snapshotRepo**sitor**y and repo**sitory configured above:

```
<settings>   <servers>    <server>     <id>ossrh</id>    <username>your-jira-id</username>    <password>your-jira-pwd&lt;/password>  </server>   </servers></settings>
```

The next thing is for us to add some Maven build plugins: source-code, Javadoc, nexus staging and the GPG plugins. Each of these plugins will be placed within the **_<plugi_**_n_s> tag that’s insid**_e the &_**lt;build> tag.

Deploying a library to OSSRH requires that the source code and JavaDoc of the library be deployed as well. Hence, we’ll add the Maven plugins to achieve that seamlessly:

```
<plugin>   <groupId>org.apache.maven.plugins</groupId>  <artifactId>maven-javadoc-plugin</artifactId>         <version>3.0.0</version> <executions>   <execution>    <id>attach-javadocs</id>   <goals>     <goal>jar</goal>   </goals>   </execution>  </executions> </plugin> 
```

```
<plugin>  <groupId>org.apache.maven.plugins</groupId>  <artifactId>maven-source-plugin</artifactId>    <version>3.0.1</version> <executions>   <execution>    <id>attach-sources</id>   <goals>      <goal>jar</goal>   </goals>   </execution> </executions> </plugin>
```

The latest version of the Javadoc and Source code plugins can be found [here](https://search.maven.org/classic/#search%7Cga%7C1%7Cg%3Aorg.apache.maven.plugins%20a%3Amaven-javadoc-plugin) and [here](https://search.maven.org/classic/#search%7Cga%7C1%7Cg%3Aorg.apache.maven.plugins%20a%3Amaven-source-plugin) respectively.

Another requirement we need to satisfy is the signing of our artifacts with a GPG/PGP program. For that, we have to [install](http://www.gnupg.org/download/) GnuPG on our system. After downloading and installation, we can always run **_gpg — version_** to verify the installation. Note that on some systems **_gpg2 — version_** will be used. Also, we should ensure that the bin folder of the GnuPG installation is in the system path.

Now we can generate a key pair for our system by running the command **_gpg — gen-key_** and following the prompts. We can list the keys that are available using **_gpg — list-keys._** It’s important to follow this [guide](https://central.sonatype.org/pages/working-with-pgp-signatures.html#delete-a-sub-key) to ensure the primary key generated is used to sign our files.

Let’s get back to our **_pom.xml_** file and add the Maven plugin for the GnuPG program so our files can be automatically signed with the default key we generate during program build:

```
<plugin>  <groupId>org.apache.maven.plugins</groupId>  <artifactId>maven-gpg-plugin</artifactId>  <version>1.6</version>  <executions>  <execution>    <id>sign-artifacts</id>   <phase>verify</phase>   <goals>     <goal>sign</goal>   </goals> </execution> </executions> </plugin>
```

The latest version for the Maven GPG plugin can be found [here](https://search.maven.org/classic/#search%7Cga%7C1%7Ca%3Amaven-gpg-plugin%20g%3Aorg.apache.maven.plugins). While generating our key pair, we provided a passphrase for it; that passphrase is going to be configured in our **_.m2/settings.xml_** file. We can also specify the executable for our GnuPG program — either **_gpg_** or **_gpg2._** So in the _settings.xml_ file, we’ll add a _&**lt;profil**_es> section just after the closing ta**_g for <_**/servers>:

```
<profiles>  <profile>   <id>ossrh</id>  <activation>   <activeByDefault>true</activeByDefault>  </activation>  <properties>    <gpg.executable>gpg</gpg.executable>   <gpg.passphrase>pass-phrase</gpg.passphrase> </properties> </profile> </profiles>
```

To wrap it all up, we’ll add the Nexus Staging Maven plugin so that we can deploy our library — including the source code, Javadoc and *.asc files to OSSRH, with simple commands:

```
<plugin>  <groupId>org.sonatype.plugins</groupId> <artifactId>nexus-staging-maven-plugin</artifactId>          <version>1.6.8</version> <extensions>true</extensions>
```

```
 <configuration>    <serverId>ossrh</serverId>    <nexusUrl>https://oss.sonatype.org/</nexusUrl> <autoReleaseAfterClose>false</autoReleaseAfterClose> </configuration>
```

```
</plugin>
```

The latest version of the plugin can be found [here](https://search.maven.org/classic/#search%7Cga%7C1%7Ca%3Anexus-staging-maven-plugin%20g%3Aorg.sonatype.plugins). Take note of the **<serverId>ossrh</se**rverId>; You’ll notice the **same** value ossrh is **used in the s**ettings.xml file. This is important for the plugin to be able to locate the credentials we config**ured in t_h_**e <serve**_rs> secti_**on of settings.xml.

### STEP FOUR:

In this section we’ll run some Maven CLI commands to do the actual deployment. Before this stage, it’s just so right that we double check and test the library to make sure there’re no bugs. Why? We’re about to go live!

To start with run: **_mvn clean deploy_**

If everything goes well, we’ll see, among the console outputs, the staging repository id created for the project like this:

**_* Created staging repository with ID “comsmattme-1001”._**

NOTE: “**comsmattme**” is the Group ID we’ve been using in this article as an example.

Let’s log in to [_https://oss.sonatype.org_](https://oss.sonatype.org/) with the same credentials for the JIRA account created earlier to inspect the artifacts we’ve deployed to staging. After login, we’ll click on **Staging Repositories** on the left side menu under the **Build Promotion** sub-menu and using the search bar at the top right of the page, we’ll search for the staging repository ID created e.g. **_comsmattme-1001_** in this case.

We should be able to see and inspect the artifacts that were uploaded by the nexus staging Maven plugin. If satisfied with everything, then we can do a release by running this maven command:

**_mvn nexus-staging:release_**

It may take up to 2 hours or more for the library to show up on [Maven Central Search](https://search.maven.org/). To search for our artifact, we’ll supply the following query to the search box: **_g:com.smattme a:mysql-backup4j_** where **g** is the group ID and **a** is the artifact name.

### Conclusion

In this comprehensive article, we’ve walked through the process of deploying our Java library to Maven Central. The complete **_pom.xml_** for the example project used in this article can be found [here](https://github.com/SeunMatt/mysql-backup4j/blob/master/pom.xml) and the **_settings.xml_** can be found [here](https://gist.github.com/SeunMatt/79abd3c3a7d110fefe01d8eaea730001#file-settings-xml) as well. Happy coding!

_Originally published at [smattme.com](https://smattme.com/blog/technology/comprehensive-step-by-step-guide-on-how-to-upload-open-source-java-library-to-maven-central)._

