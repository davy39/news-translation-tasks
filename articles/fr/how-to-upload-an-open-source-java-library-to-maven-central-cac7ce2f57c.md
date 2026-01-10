---
title: Comment télécharger une bibliothèque Java open-source sur Maven Central
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
seo_title: Comment télécharger une bibliothèque Java open-source sur Maven Central
seo_desc: 'By Seun Matt

  This article is a comprehensive guide, from start to finish, on how to deploy a
  Java library to Maven Central so everyone can use it by including the dependency
  in their project(s).

  It goes without saying that there has to be a Java libr...'
---

Par Seun Matt

Cet article est un guide complet, du début à la fin, sur la façon de déployer une bibliothèque Java sur Maven Central afin que tout le monde puisse l'utiliser en incluant la dépendance dans leurs projet(s).

Il va sans dire qu'il doit y avoir une bibliothèque Java pour qu'elle puisse être téléchargée. Par conséquent, la première chose à faire est de créer une bibliothèque Java unique, de qualité et qui sera bénéfique pour la communauté des développeurs. Bien sûr, vous l'avez déjà — c'est pourquoi vous lisez ceci après tout _(ou peut-être prévoyez-vous d'en créer une)_.

En résumé, pour télécharger une nouvelle bibliothèque Java sur Maven Central, nous devrons réserver notre Group ID, fournir les détails requis dans le fichier _pom.xml_ du projet, signer les artefacts générés avec GnuPG et, enfin, déployer sur le gestionnaire de dépôt Nexus de Sonatype.

### ÉTAPE UN :

La première étape consiste à s'assurer que notre bibliothèque open-source est disponible sur un dépôt de code publiquement accessible comme Github. Ensuite, nous pouvons procéder à la réservation de notre Group ID souhaité. Le Group ID doit idéalement être **unique pour un individu ou une organisation** — comme un domaine. Des exemples de Group ID incluent **_com.smattme_** et **_org.apache.commons_**_._

Nous allons donc créer un compte JIRA [ici](https://issues.sonatype.org/secure/Signup!default.jspa) puis [nous connecter](https://issues.sonatype.org/login.jsp) pour créer un nouveau ticket de projet. En cliquant sur le bouton **créer** en haut du site web, une fenêtre modale s'ouvrira où nous fournirons le Group ID (par exemple, com.smattme), l'URL SCM (par exemple, [_https://github.com/SeunMatt/mysql-backup4j.git_](https://github.com/SeunMatt/mysql-backup4j.git)_),_ l'URL du projet (par exemple, [_https://github.com/SeunMatt/mysql-backup4j_](https://github.com/SeunMatt/mysql-backup4j)_),_ le résumé (qui peut être le nom de la bibliothèque comme _mysql-backup4j_) et enfin la description du projet.

**NOTE :** Dans la fenêtre modale pour créer un nouveau ticket de projet, assurez-vous que le champ **Projet** est défini sur _Community Support — Open Source Project Repository Hosting (OSSRH)_ et que le **Type d'Issue** est _Nouveau Projet_.

La création du nouveau ticket de projet déclenchera la création de dépôts sur l'hébergement de dépôt OSS de Sonatype (OSSRH) qui seront synchronisés avec Maven Central après le déploiement de nos artefacts.

Il est important de ne pas déployer tant qu'il n'y a pas de confirmation par email que l'issue créée a été résolue. Si un problème survient, nous pouvons toujours commenter l'issue pour obtenir de l'aide et/ou des explications.

### ÉTAPE DEUX :

Maintenant que nous avons enregistré avec succès notre Group ID, la prochaine chose à faire est de mettre à jour le fichier **_pom.xml_** du projet avec les informations nécessaires. Commençons par fournir le nom du projet, la description et l'URL ainsi que les coordonnées et les informations de packaging :

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
<name>${project.groupId}:${project.artifactId}</name> 
```

```
<description> Ceci est une bibliothèque simple pour sauvegarder les bases de données mysql et les envoyer par email, stockage cloud, etc. Elle fournit également une méthode pour importer programmatiquement les requêtes SQL générées pendant le processus d'exportation</description> 
```

```
<url>https://github.com/SeunMatt/mysql-backup4j</url>
```

Ensuite, nous avons les informations sur la licence et les développeurs. Dans ce cas, nous utiliserons une licence MIT. Si une autre licence est utilisée, tout ce dont nous avons besoin est une URL correspondante pour cette licence. Si c'est une licence open-source, il y a de bonnes chances qu'elle soit disponible sur _opensource.org_ :

```
<licenses> <license>  <name>Licence MIT</name>              <url>http://www.opensource.org/licenses/mit-license.php</url>       </license> </licenses> <developers> 
```

```
 <developer>   <name>Seun Matt</name>   <email>smatt382@gmail.com</email>      <organization>SmattMe</organization> <organizationUrl>https://smattme.com</organizationUrl></developer> 
```

```
</developers>
```

Une autre information importante requise est la gestion du code source (SCM) :

```
<scm>   <connection>scm:git:git://github.com/SeunMatt/mysql-backup4j.git</connection>   <developerConnection>scm:git:ssh://github.com:SeunMatt/mysql-backup4j.git</developerConnection>   <url>https://github.com/SeunMatt/mysql-backup4j/tree/master</url> </scm>
```

Dans ce cas, le projet est hébergé sur Github, d'où les valeurs fournies. Des exemples de configurations pour d'autres SCM peuvent être trouvés [ici](https://central.sonatype.org/pages/requirements.html#scm-information).

### ÉTAPE TROIS :

Dans cette étape, nous allons configurer notre projet pour le déploiement sur OSSRH en utilisant le plugin Apache Maven. Le plugin nécessite que nous ajoutions une section **_distributionManagement_** à notre **_pom.xml_** :

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

Nous fournirons les identifiants utilisateur pour les dépôts configurés ci-dessus en ajoutant une entrée **_<servers>_** dans settings.xml qui se trouve dans le répertoire personnel de l'utilisateur, par exemple /Users/smatt/.m2. Notez que l'id est le même que celui du snapshotRepository et du repository configurés ci-dessus :

```
<settings>   <servers>    <server>     <id>ossrh</id>    <username>votre-id-jira</username>    <password>votre-mdp-jira</password>  </server>   </servers></settings>
```

La prochaine chose à faire est d'ajouter quelques plugins de build Maven : source-code, Javadoc, nexus staging et les plugins GPG. Chacun de ces plugins sera placé dans la balise **_<plugins>_** qui se trouve à l'intérieur de la balise **_<build>_**.

Le déploiement d'une bibliothèque sur OSSRH nécessite que le code source et la JavaDoc de la bibliothèque soient également déployés. Par conséquent, nous ajouterons les plugins Maven pour y parvenir de manière transparente :

```
<plugin>   <groupId>org.apache.maven.plugins</groupId>  <artifactId>maven-javadoc-plugin</artifactId>         <version>3.0.0</version> <executions>   <execution>    <id>attach-javadocs</id>   <goals>     <goal>jar</goal>   </goals>   </execution>  </executions> </plugin> 
```

```
<plugin>  <groupId>org.apache.maven.plugins</groupId>  <artifactId>maven-source-plugin</artifactId>    <version>3.0.1</version> <executions>   <execution>    <id>attach-sources</id>   <goals>      <goal>jar</goal>   </goals>   </execution> </executions> </plugin>
```

Les dernières versions des plugins Javadoc et Source code peuvent être trouvées [ici](https://search.maven.org/classic/#search%7Cga%7C1%7Cg%3Aorg.apache.maven.plugins%20a%3Amaven-javadoc-plugin) et [ici](https://search.maven.org/classic/#search%7Cga%7C1%7Cg%3Aorg.apache.maven.plugins%20a%3Amaven-source-plugin) respectivement.

Une autre exigence que nous devons satisfaire est la signature de nos artefacts avec un programme GPG/PGP. Pour cela, nous devons [installer](http://www.gnupg.org/download/) GnuPG sur notre système. Après le téléchargement et l'installation, nous pouvons toujours exécuter **_gpg — version_** pour vérifier l'installation. Notez que sur certains systèmes, **_gpg2 — version_** sera utilisé. De plus, nous devons nous assurer que le dossier bin de l'installation de GnuPG est dans le chemin du système.

Maintenant, nous pouvons générer une paire de clés pour notre système en exécutant la commande **_gpg — gen-key_** et en suivant les invites. Nous pouvons lister les clés disponibles en utilisant **_gpg — list-keys._** Il est important de suivre ce [guide](https://central.sonatype.org/pages/working-with-pgp-signatures.html#delete-a-sub-key) pour s'assurer que la clé primaire générée est utilisée pour signer nos fichiers.

Revenons à notre fichier **_pom.xml_** et ajoutons le plugin Maven pour le programme GnuPG afin que nos fichiers puissent être automatiquement signés avec la clé par défaut que nous générons pendant la construction du programme :

```
<plugin>  <groupId>org.apache.maven.plugins</groupId>  <artifactId>maven-gpg-plugin</artifactId>  <version>1.6</version>  <executions>  <execution>    <id>sign-artifacts</id>   <phase>verify</phase>   <goals>     <goal>sign</goal>   </goals> </execution> </executions> </plugin>
```

La dernière version du plugin Maven GPG peut être trouvée [ici](https://search.maven.org/classic/#search%7Cga%7C1%7Ca%3Amaven-gpg-plugin%20g%3Aorg.apache.maven.plugins). Lors de la génération de notre paire de clés, nous avons fourni une phrase de passe ; cette phrase de passe sera configurée dans notre fichier **_.m2/settings.xml_**. Nous pouvons également spécifier l'exécutable pour notre programme GnuPG — soit **_gpg_**, soit **_gpg2._** Dans le fichier _settings.xml_, nous ajouterons une section **_<profiles>_** juste après la balise de fermeture de **_</servers>_** :

```
<profiles>  <profile>   <id>ossrh</id>  <activation>   <activeByDefault>true</activeByDefault>  </activation>  <properties>    <gpg.executable>gpg</gpg.executable>   <gpg.passphrase>phrase-de-passe</gpg.passphrase> </properties> </profile> </profiles>
```

Pour tout rassembler, nous ajouterons le plugin Nexus Staging Maven afin que nous puissions déployer notre bibliothèque — y compris le code source, la Javadoc et les fichiers *.asc sur OSSRH, avec des commandes simples :

```
<plugin>  <groupId>org.sonatype.plugins</groupId> <artifactId>nexus-staging-maven-plugin</artifactId>          <version>1.6.8</version> <extensions>true</extensions>
```

```
 <configuration>    <serverId>ossrh</serverId>    <nexusUrl>https://oss.sonatype.org/</nexusUrl> <autoReleaseAfterClose>false</autoReleaseAfterClose> </configuration>
```

```
</plugin>
```

La dernière version du plugin peut être trouvée [ici](https://search.maven.org/classic/#search%7Cga%7C1%7Ca%3Anexus-staging-maven-plugin%20g%3Aorg.sonatype.plugins). Notez le **<serverId>ossrh</serverId>** ; vous remarquerez que la **même** valeur ossrh est **utilisée dans le** fichier settings.xml. Cela est important pour que le plugin puisse localiser les identifiants que nous avons configurés dans la section **_<servers>_** de settings.xml.

### ÉTAPE QUATRE :

Dans cette section, nous allons exécuter quelques commandes CLI Maven pour effectuer le déploiement réel. Avant cette étape, il est juste de vérifier et tester la bibliothèque pour s'assurer qu'il n'y a pas de bugs. Pourquoi ? Nous sommes sur le point de passer en production !

Pour commencer, exécutez : **_mvn clean deploy_**

Si tout se passe bien, nous verrons, parmi les sorties de la console, l'ID du dépôt de staging créé pour le projet comme ceci :

**_* Created staging repository with ID "comsmattme-1001"._**

NOTE : "**comsmattme**" est le Group ID que nous avons utilisé dans cet article comme exemple.

Connectons-nous à [_https://oss.sonatype.org_](https://oss.sonatype.org/) avec les mêmes identifiants que pour le compte JIRA créé précédemment pour inspecter les artefacts que nous avons déployés en staging. Après la connexion, nous cliquerons sur **Staging Repositories** dans le menu de gauche sous le sous-menu **Build Promotion** et en utilisant la barre de recherche en haut à droite de la page, nous rechercherons l'ID du dépôt de staging créé, par exemple **_comsmattme-1001_** dans ce cas.

Nous devrions pouvoir voir et inspecter les artefacts qui ont été téléchargés par le plugin Nexus Staging Maven. Si nous sommes satisfaits de tout, alors nous pouvons faire une release en exécutant cette commande maven :

**_mvn nexus-staging:release_**

Cela peut prendre jusqu'à 2 heures ou plus pour que la bibliothèque apparaisse sur [Maven Central Search](https://search.maven.org/). Pour rechercher notre artefact, nous fournirons la requête suivante dans la boîte de recherche : **_g:com.smattme a:mysql-backup4j_** où **g** est le group ID et **a** est le nom de l'artefact.

### Conclusion

Dans cet article complet, nous avons passé en revue le processus de déploiement de notre bibliothèque Java sur Maven Central. Le fichier **_pom.xml_** complet pour le projet exemple utilisé dans cet article peut être trouvé [ici](https://github.com/SeunMatt/mysql-backup4j/blob/master/pom.xml) et le fichier **_settings.xml_** peut être trouvé [ici](https://gist.github.com/SeunMatt/79abd3c3a7d110fefe01d8eaea730001#file-settings-xml) également. Bon codage !

_Publié à l'origine sur [smattme.com](https://smattme.com/blog/technology/comprehensive-step-by-step-guide-on-how-to-upload-open-source-java-library-to-maven-central)._