---
title: Comment automatiser le déploiement de conteneurs Docker via Maven
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
seo_title: Comment automatiser le déploiement de conteneurs Docker via Maven
seo_desc: 'By Ravindu Fernando

  This article is intended for people who are using Maven as a build and dependency
  management tool for JAVA applications. It will show you how to integrate docker
  container build, tag and push workflows into their existing Maven bu...'
---

Par Ravindu Fernando

Cet article s'adresse aux personnes qui utilisent Maven comme outil de construction et de gestion des dépendances pour les applications JAVA. Il vous montrera comment intégrer les workflows de construction, de balisage et de poussée de conteneurs Docker dans leur écosystème de gestion de construction Maven existant.

Avoir la capacité de construire, de baliser et de pousser votre application en tant que conteneur directement à partir des commandes du cycle de vie de Maven est une chose assez cool à avoir. Cela rend les choses faciles et rapides si vous essayez d'apporter la puissance des conteneurs pour déployer vos applications et que vous utilisez déjà Maven pour la gestion des dépendances.

Si nous examinons les solutions existantes pour intégrer le déploiement de conteneurs Docker dans Maven, il en existe plusieurs, comme [spotify maven docker plugin](https://github.com/spotify/docker-client), [fabric8io docker maven plugin](https://github.com/fabric8io/docker-maven-plugin), etc. Mais toutes ces solutions apportent une complexité indésirable, une courbe d'apprentissage supplémentaire et trop de changements dans votre code d'application existant. Pourtant, il existe une méthode plus simple et plus facile pour y parvenir sans utiliser de plugin tiers.

Si vous notez le plugin Ant de Maven, il nous permet d'exécuter des commandes externes. Ainsi, en utilisant le plugin Ant, nous avons la capacité d'exécuter des commandes docker build, tag, push ou toute autre commande selon vos souhaits. La seule chose que nous devons faire est de fournir un Dockerfile approprié pour construire l'image Docker de votre application et l'ensemble nécessaire de commandes et de configurations Maven dans le fichier pom.xml.

> Pour expliquer les étapes impliquées dans ce processus, j'utiliserai une application JAVA de démonstration. Elle contient tous les exemples de code utilisés dans les étapes suivantes. Vous pouvez la cloner depuis [ici](https://github.com/rav94/dockermavensample).

### **Étape 1 | Créer le Dockerfile**

> Le Dockerfile doit être stocké dans le chemin **_src/main/docker/Dockerfile_** de votre application JAVA.

```
# Pull base imageFROM tomcat:8.0.30-jre7# MaintainerMAINTAINER "ravindu@emojot.com"
```

```
# Set Environment propertiesENV JAVA_OPTS=-Denvironment=production# Copy war file to tomcat webapps folderCOPY /dockermavensample.war /usr/local/tomcat/webapps/
```

### **Étape 2 | Mettre à jour le pom.xml pour copier toutes les ressources liées à Docker dans le répertoire target**

> Nous pouvons utiliser maven-resource-plugin pour copier les ressources.

```
<plugin>    <artifactId>maven-resources-plugin</artifactId>    <executions>        <execution>            <id>copy-resources</id>            <phase>validate</phase>            <goals>                <goal>copy-resources</goal>            </goals>            <configuration>                <outputDirectory>${basedir}/target</outputDirectory>                <resources>                    <resource>                        <directory>src/main/docker</directory>                        <filtering>true</filtering>                    </resource>                </resources>            </configuration>        </execution>    </executions></plugin>
```

### **Étape 3 | Mettre à jour le pom.xml pour permettre la construction et le balisage de l'image Docker via le plugin Ant de Maven**

```
<plugin>    <groupId>org.apache.maven.plugins</groupId>    <artifactId>maven-antrun-plugin</artifactId>    <version>1.6</version>    <executions>        <execution>            <id>prepare-package</id>            <phase>package</phase>            <inherited>false</inherited>            <configuration>                <target>                    <exec executable="docker">                        <arg value="build"/>                        <arg value="-t"/>                        <arg value="dockermavensample:${project.version}"/>                        <arg value="target"/>                    </exec>                </target>            </configuration>            <goals>                <goal>run</goal>            </goals>        </execution>    </executions></plugin>
```

Le plugin Ant de Maven exécutera la commande docker dans la phase de package du cycle de vie de Maven dans l'ordre suivant, ce qui construira l'image docker à partir du Dockerfile qui a été copié dans le dossier target à l'étape 2.

```
docker build -t dockermavensample:1.0.0 target
```

### **Étape 4 | Mettre à jour le fichier pom.xml pour permettre la poussée de l'image Docker vers un dépôt Docker distant**

> Idéalement pour la production, vous devrez pousser vos images Docker dans votre propre registre Docker privé ou utiliser un dépôt d'images Docker tiers qui permet de stocker des images Docker privées afin que d'autres ne puissent pas tirer vos images Docker directement.

```
<plugin>    <groupId>org.apache.maven.plugins</groupId>    <artifactId>maven-antrun-plugin</artifactId>    <version>1.6</version>    <executions>        <execution>            <phase>install</phase>            <inherited>false</inherited>            <configuration>                <target>                    <exec executable="docker">                        <arg value="tag"/>                        <arg value="dockermavensample:${project.version}"/>                        <arg value="dockermavensample:latest"/>                    </exec>                    <exec executable="docker">                        <arg value="push"/>                        <arg value="dockermavensample:latest"/>                    </exec>                </target>            </configuration>            <goals>                <goal>run</goal>            </goals>        </execution>    </executions></plugin>
```

En plus des étapes ci-dessus, vous pouvez vouloir avoir un contrôle sur la manière dont vous exécutez ces commandes liées à Docker dans votre cycle de vie Maven. Pour cela, vous pouvez utiliser des profils Maven pour diviser logiquement les définitions de plugins ci-dessus. Ensuite, exécutez ceux-ci uniquement lorsque le profil lié à cette action est invoqué.

**Jetez un coup d'œil aux profils de démonstration suivants :**

```
<profile>    <id>dockerBuild</id>    <build>        <plugins>            <plugin>                <artifactId>maven-resources-plugin</artifactId>                <executions>                    <execution>                        <id>copy-resources</id>                        <phase>validate</phase>                        <goals>                            <goal>copy-resources</goal>                        </goals>                        <configuration>                            <outputDirectory>${basedir}/target</outputDirectory>                            <resources>                                <resource>                                    <directory>src/main/docker</directory>                                    <filtering>true</filtering>                                </resource>                            </resources>                        </configuration>                    </execution>                </executions>            </plugin>            <plugin>                <groupId>org.apache.maven.plugins</groupId>                <artifactId>maven-antrun-plugin</artifactId>                <version>1.6</version>                <executions>                    <execution>                        <id>prepare-package</id>                        <phase>package</phase>                        <inherited>false</inherited>                        <configuration>                            <target>                                <exec executable="docker">                                    <arg value="build"/>                                    <arg value="-t"/>                                    <arg value="dockermavensample:${project.version}"/>                                    <arg value="target"/>                                </exec>                            </target>                        </configuration>                        <goals>                            <goal>run</goal>                        </goals>                    </execution>                </executions>            </plugin>        </plugins>    </build>
```

```
    <activation>        <activeByDefault>true</activeByDefault>    </activation></profile>
```

```
<!-- docker Image push and release profile --><profile>    <id>dockerRelease</id>    <build>        <plugins>            <plugin>                <groupId>org.apache.maven.plugins</groupId>                <artifactId>maven-antrun-plugin</artifactId>                <version>1.6</version>                <executions>                    <execution>                        <phase>install</phase>                        <inherited>false</inherited>                        <configuration>                            <target>                                <exec executable="docker">                                    <arg value="tag"/>                                    <arg value="dockermavensample:${project.version}"/>                                    <arg value="dockermavensample:latest"/>                                </exec>                                <exec executable="docker">                                    <arg value="push"/>                                    <arg value="dockermavensample:latest"/>                                </exec>                            </target>                        </configuration>                        <goals>                            <goal>run</goal>                        </goals>                    </execution>                </executions>            </plugin>        </plugins>    </build></profile>
```

Après avoir terminé les étapes ci-dessus, exécutez simplement

```
mvn clean install -P dockerBuild,dockerRelease
```

Maintenant, votre application JAVA est conditionnée en tant que conteneur et poussée dans un dépôt Docker distant. Vous pouvez tester si l'image que vous avez créée fonctionne en exécutant les commandes suivantes,

![Image](https://cdn-media-1.freecodecamp.org/images/H0mmu0zzMqdWt-UiERarfC6tPqgX5ZUUqUZS)
_Après l'exécution du profil dockerBuild, l'image Docker doit être disponible localement_

![Image](https://cdn-media-1.freecodecamp.org/images/Y854emSEIN8QMwYSIThdPU3VdLhgFjUXXK-M)
_Exécuter l'image Docker dockermavensample:1.0.0_

![Image](https://cdn-media-1.freecodecamp.org/images/dPF05Esb-3p1AhDuoKncJzRQk0u76-9a5o4k)
_Page d'accueil d'Apache Tomcat_

![Image](https://cdn-media-1.freecodecamp.org/images/KwXo738tVALAG3-fpvItOR4DqSKRcGuLDWVs)
_Kaboom! :)_

Comme vous pouvez le voir, nous pouvons utiliser les fonctionnalités et plugins déjà disponibles de Maven pour créer un pipeline de construction bien structuré pour déployer nos applications en tant que conteneurs.

**Projet de démonstration :**

[**rav94/dockermavensample**](https://github.com/rav94/dockermavensample)  
[_Projet de démonstration pour montrer l'automatisation du déploiement de conteneurs via Maven - rav94/dockermavensample_github.com](https://github.com/rav94/dockermavensample)

Merci d'avoir lu !