---
title: Comment créer un plugin IntelliJ — construisons un simple chercheur de dictionnaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T16:18:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-intellij-plugin-lets-build-a-simple-dictionary-finder-6c5192b449c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vZu_atWvhwDrpK4a2mhakg.jpeg
tags:
- name: intellij
  slug: intellij
- name: Java
  slug: java
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer un plugin IntelliJ — construisons un simple chercheur de
  dictionnaire
seo_desc: 'By Oliver Nybroe

  Most of us developers use IntelliJ platforms, either IDEA, PHPStorm, WebStorm, Android
  Studio, PyCharm and the list goes on and on. However sometimes when we use it, we
  find that a feature is missing, but we have no idea how to actua...'
---

Par Oliver Nybroe

La plupart d'entre nous, développeurs, utilisons les plateformes IntelliJ, que ce soit IDEA, PHPStorm, WebStorm, Android Studio, PyCharm et la liste est encore longue. Cependant, parfois lorsque nous l'utilisons, nous constatons qu'une fonctionnalité est manquante, mais nous n'avons aucune idée de la manière d'ajouter réellement cette fonctionnalité et finissons par nous en passer.

Dans cet article, je vais expliquer comment créer un plugin simple pour tous les IDE IntelliJ afin que, lorsque vous ajoutez un fichier `project.dic`, il l'ajoute automatiquement comme l'un de vos dictionnaires. Il recherchera également le fichier dans les packages, de sorte que les packages peuvent ajouter des mots personnalisés au dictionnaire. Un fichier `.dic` est un simple dictionnaire où chaque ligne est un mot du dictionnaire.

Le projet n'est qu'un exemple pour vous aider à démarrer le développement de vos propres plugins. Mais c'est en fait aussi une fonctionnalité qui me manquait, car lorsque je développe un package personnalisé avec mes propres mots, je déteste devoir les ajouter chaque fois dans le dictionnaire au niveau du projet.

### Création du projet

Lors de la création de plugins pour IntelliJ, nous avons le choix de le faire en Java ou en Kotlin. Je vais le faire en Java car la plupart des utilisateurs sont familiers avec ce langage. Comme il s'agit d'un projet Java, nous utiliserons IntelliJ IDEA comme notre IDE.

Selon le [guide de développement](https://www.jetbrains.org/intellij/sdk/docs/basics/getting_started.html), la méthode recommandée pour créer un projet est d'utiliser [Gradle](https://www.jetbrains.org/intellij/sdk/docs/tutorials/build_system.html). Nous commençons par ouvrir les `préférences` et vérifions si les plugins `Gradle` et `Plugin DevKit` sont installés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ASJDtMw774VpAgoWCZEmkw.png)

Après avoir installé les plugins et redémarré l'IDE, nous allons dans le flux de nouveaux projets et sous `Gradle`. Il y a maintenant une option appelée `IntelliJ Platform Plugin` qui est celle dont nous avons besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NTFEQjxMv7BBrHSzBj1THw.png)
_Etape 1 du flux de création de projet_

Ensuite, suivez le reste du flux de création de projet comme d'habitude — dans ce projet, je choisis la configuration suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qYo4hPtRV5aCWblW5HxzDA.png)
_Etape 2 du flux de création de projet_

![Image](https://cdn-media-1.freecodecamp.org/images/1*eqsj6ej8Qiqx4VzAEer2cQ.png)
_Etape 3 du flux de création de projet_

![Image](https://cdn-media-1.freecodecamp.org/images/1*ehSxccowC6-IR1tJ9h-5iQ.png)
_Etape 4 du flux de création de projet_

### Configuration de `plugin.xml`

Maintenant que nous avons un projet, nous devons configurer notre fichier `plugin.xml` et `build.gradle`. Le fichier `plugin.xml` est un fichier utilisé par IntelliJ qui définit toutes les informations sur le plugin. Cela inclut le nom, les dépendances, les actions qu'il doit ajouter ou s'il doit étendre quelque chose dans IntelliJ. Basiquement, ce fichier définit tout ce que votre plugin doit faire et est la racine de votre projet. Dans notre fichier `build.gradle`, nous pouvons définir certaines des valeurs de `plugin.xml`, et des informations comme quelle version d'IntelliJ nous voulons utiliser pour tester notre plugin lors de la construction avec gradle.

Commençons par définir notre fichier `plugin.xml`. Vous pouvez trouver le fichier dans `src/main/resources/META-INF/plugin.xml`. Nous voulons que notre plugin soit disponible sur tous les IDE IntelliJ, donc nous définissons nos `dependencies` sur `com.intellij.modules.lang`. Pour l'instant, notre fichier ressemble à ceci :

```
<idea-plugin>    <id>dk.lost_world.Dictionary</id>    <name>Dictionary</name>    <vendor email="olivernybroe@gmail.com" url="https://github.com/olivernybroe/intellij-Dictionary">GitHub</vendor>    <depends>com.intellij.modules.lang</depends></idea-plugin>
```

Cependant, pour l'instant, cela n'a aucune logique, et nous n'enregistrons rien sur la plateforme IntelliJ.

Comme ce projet trouvera les fichiers `project.dic` à l'intérieur d'un projet et les enregistrera comme dictionnaires dans ce projet, nous devrons enregistrer un composant de niveau projet. Ce composant sera appelé lorsqu'un projet est ouvert et fermé. Créons une classe et implémentons l'interface `ProjectComponent`. Lorsque nous survolons le nom de la classe, il nous indique que le composant n'est pas enregistré.

![Image](https://cdn-media-1.freecodecamp.org/images/1*imcg1FilSnSxkgJG6J9-0g.png)
_Indications sur la classe_

Nous pouvons ensuite appeler l'action appelée `Register Project Component` et elle l'enregistrera pour nous dans le fichier `plugin.xml`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b4OvFSeoPWJ6UDAtgKF_Vg.png)
_Actions sur la classe_

Si nous ouvrons `plugin.xml`, le code suivant devrait être ajouté. Si ce n'était pas le cas lors de l'appel de l'action, ajoutez-le manuellement.

```
<project-components>    <component>        <implementation-class>dk.lost_world.dictionary.DictionaryProjectComponent</implementation-class>    </component></project-components>
```

#### Système de fichiers IntelliJ

Lors de la manipulation de fichiers dans IntelliJ, nous utilisons un [**V**irtual **F**ile **S**ystem (VFS)](https://www.jetbrains.org/intellij/sdk/docs/basics/virtual_file_system.html). Le VFS nous donne une API universelle pour communiquer avec les fichiers, sans avoir à penser s'ils proviennent de FTP, d'un serveur HTTP ou simplement du disque local.

Comme notre plugin recherche des fichiers appelés `project.dic`, il devra bien sûr communiquer avec le **V**irtual **F**ile **S**ystem. Tous les fichiers dans le VFS sont des [Virtual Files](https://www.jetbrains.org/intellij/sdk/docs/basics/architectural_overview/virtual_file.html). Cela peut sembler un peu intimidant, mais en réalité, ce n'est qu'une API pour un système de fichiers et pour un fichier. La façon de le voir est simplement que le **V**irtual **F**ile **S**ystem est votre interface de système de fichiers et les Virtual Files sont vos fichiers.

#### Paramètres du correcteur orthographique

Comme IntelliJ prend déjà en charge les fichiers `.dic` et la vérification orthographique en général, la seule chose que nous devons faire est d'enregistrer nos fichiers `project.dic` dans les paramètres du correcteur orthographique.

Tous les paramètres du correcteur orthographique sont enregistrés dans une classe appelée `com.intellij.spellchecker.settings.SpellCheckerSettings`. Pour obtenir une instance de celle-ci, appelez simplement la méthode `getInstance` (la plupart des classes IntelliJ ont une méthode `getInstance` qui utilise le `ServiceManager` d'IntelliJ en dessous).
La classe de paramètres a une méthode appelée `getCustomDictionariesPaths` qui retourne tous les chemins vers les dictionnaires qui sont installés par l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pee95tAmC6aeTfpkOuBeew.png)
_API de getCustomDictionariesPaths_

En regardant la signature de la méthode, nous voyons également une annotation appelée `AvailableSince`. Nous utiliserons plus tard la valeur de cette annotation pour spécifier la version minimale requise pour que notre plugin fonctionne.

Comme la méthode retourne une liste, nous pouvons simplement appeler `add` sur la méthode pour ajouter un nouveau chemin vers un dictionnaire.

#### Exécution de notre plugin (build.gradle)

Maintenant que nous savons comment ajouter un dictionnaire au correcteur orthographique, ajoutons un petit exemple de code dans notre classe `DictionaryProjectComponent` pour faire cela.

```
public class DictionaryProjectComponent implements ProjectComponent {    private Project project;    public DictionaryProjectComponent(Project project) {        this.project = project;    }    @Override    public void projectOpened() {        SpellCheckerSettings            .getInstance(project)            .getCustomDictionariesPaths()            .add("./project.dic");    }}
```

Ce code enregistrera un fichier `project.dic` à partir de la racine de notre projet chaque fois que le projet est ouvert.

Pour tester notre petit exemple, nous devons mettre à jour notre fichier `build.gradle`. Dans la section `intellij` du fichier gradle, nous ajoutons la version d'IntelliJ que nous voulons utiliser. Ce numéro de version est celui de l'annotation `AvailableSince` sur la classe `SpellCheckerSettings`.

```
plugins {    id 'java'    id 'org.jetbrains.intellij' version '0.4.4'}group 'dk.lost_world'version '1.0-SNAPSHOT'sourceCompatibility = 1.8repositories {    mavenCentral()}dependencies {    testCompile group: 'junit', name: 'junit', version: '4.12'}// See https://github.com/JetBrains/gradle-intellij-plugin/intellij {    pluginName 'Dictionary'    version '181.2784.17'    type 'IC'    downloadSources true}
```

L'exécution de la commande `runIde` à partir de gradle démarrera une instance d'IntelliJ de la version spécifique. Après avoir démarré l'IDE de test, notre plugin devrait avoir été exécuté. Si nous ouvrons `préférences > Éditeur > Orthographe > Dictionnaires`, nous pouvons voir sous les dictionnaires personnalisés que le chemin que nous avons spécifié dans notre exemple est maintenant ajouté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*69zQmR1XsQ4txhWfgT3niw.png)
_Affichage des préférences des dictionnaires depuis l'IDE IntelliJ_

Nous sommes maintenant capables de tester notre plugin, il est donc temps de le construire correctement pour qu'il trouve les fichiers `project.dic` et les enregistre pour nous.

Dans la méthode `DictionaryProjectComponent::projectOpened`, nous devons d'abord trouver tous les fichiers appelés `project.dic` et les enregistrer, ainsi qu'ajouter un écouteur de fichiers pour que lorsque de nouveaux fichiers `project.dic` sont ajoutés, ils soient enregistrés automatiquement.

### Classe Dictionary

Nous aurons une classe appelée `Dictionary`, cette classe contiendra la logique pour nous permettre d'enregistrer et de supprimer des fichiers du dictionnaire. La classe aura les méthodes publiques suivantes :
`void registerAndNotify(Collection<VirtualFile> files)`
`void registerAndNotify(VirtualFile file)`
`void removeAndNotify(VirtualFile file)`
`void moveAndNotify(VirtualFile oldFile, VirtualFile newFile)

Ces méthodes créeront également une notification sur ce qui s'est passé, afin que l'utilisateur final sache ce qui a changé avec les dictionnaires personnalisés. Le fichier final pour cela ressemblera à ce qui suit :

#### Trouver tous les fichiers de dictionnaire

Pour trouver tous les fichiers de dictionnaire dans le projet appelés `project.dic`, nous utilisons la classe `[FilenameIndex](http://www.jetbrains.org/intellij/sdk/docs/basics/psi_cookbook.html#how-do-i-find-a-file-if-i-know-its-name-but-dont-know-the-path)`. Le fichier est dans l'espace de noms `com.intellij.psi.search.FilenameIndex`, il a une méthode `getVirtualFilesByName` que nous pouvons utiliser pour trouver nos fichiers `project.dic`.

```
FilenameIndex.getVirtualFilesByName(
    project,
    "project.dic",
    false,
    GlobalSearchScope.allScope(project))
```

Cet appel retournera tous les fichiers virtuels qui correspondent aux critères de recherche. Nous plaçons ensuite le résultat de retour dans la méthode de classe Dictionary `registerAndNotify`.

```
@Override
public void projectOpened() {
    Dictionary dictionary = new Dictionary(project);
    dictionary.registerAndNotify(
        FilenameIndex.getVirtualFilesByName(
            project,
            "project.dic",
            false,
            GlobalSearchScope.allScope(project)
        )
    );
}
```

Notre code est maintenant capable de trouver les fichiers `project.dic` au démarrage et de les enregistrer, s'ils ne sont pas déjà enregistrés. Il notifiera également les nouveaux fichiers enregistrés.

#### Ajout d'un écouteur de fichiers virtuels

La partie suivante consiste à écouter les changements dans les fichiers virtuels. Pour cela, nous avons besoin d'un écouteur. Pour cela, nous avons besoin de `com.intellij.openapi.vfs.VirtualFileListener`.

Dans le bloc de documentation de la classe d'écouteur, nous pouvons voir que pour l'enregistrer, nous pouvons utiliser `VirtualFilemanager#addVirtualFileListener`.
Créons une classe nommée `DictionaryFileListener` et implémentons les méthodes dont nous avons besoin pour notre projet.

Ensuite, nous mettons à jour notre classe `projectOpened` pour ajouter également le `VirtualFileListener`.

```
@Override
public void projectOpened() {
    Dictionary dictionary = new Dictionary(project);
    dictionary.registerAndNotify(
        FilenameIndex.getVirtualFilesByName(
            project,
            "project.dic",
            false,
            GlobalSearchScope.allScope(project)
        )
    );
    VirtualFileManager.getInstance().addVirtualFileListener(
        new DictionaryFileListener(dictionary)
    );
}
```

Notre plugin est maintenant capable de trouver nos fichiers de dictionnaire au démarrage, mais aussi d'écouter si un fichier de dictionnaire est ajouté plus tard. La prochaine chose dont nous avons besoin est d'ajouter des informations pour la liste de notre plugin.

#### Ajout d'informations sur le plugin

Pour ajouter des informations sur le plugin, nous ouvrons le fichier `build.gradle` et éditons l'objet `patchPluginXml`. Dans celui-ci, nous devons spécifier quelle version de build est requise pour le plugin, la version du plugin, la description et les notes de changement.

```
patchPluginXml {
    sinceBuild intellij.version
    untilBuild null
    version project.version
    pluginDescription """Plugin pour avoir un dictionnaire partagé pour tous les membres de votre projet. <br><br>Il trouvera automatiquement tous les fichiers <code>project.dic</code> et les ajoutera à la liste des dictionnaires. <br><br>Il recherchera également des fichiers de dictionnaire dans les packages et les ajoutera à notre liste de dictionnaires.    """
    changeNotes """<p>0.2</p><ul>    <li>Ajout de la prise en charge de l'écoute lors de l'ajout, du déplacement, de la suppression ou de la copie d'un fichier <code>project.dic</code>.</li></ul><p>0.1</p><ul>    <li>Première édition du plugin.</li></ul>    """
}
```

Nous mettons également à jour la propriété `version` à `'0.2'` du projet gradle lui-même. Le plugin peut maintenant s'exécuter sur toutes les versions depuis que la méthode d'enregistrement des dictionnaires personnalisés a été ajoutée.

Pour tester s'il génère la sortie souhaitée, nous pouvons exécuter la tâche gradle `patchPluginXml` et sous `build/patchedPluginXmlFiles`, notre fichier `plugin.xml` généré sera là.

Depuis la version IntelliJ `2019.1`, [tous les plugins supportent les icônes](http://www.jetbrains.org/intellij/sdk/docs/basics/plugin_structure/plugin_icon_file.html). Comme cela est relativement nouveau, de nombreux plugins n'ont pas d'icône, et votre plugin peut se démarquer en ayant une icône. La convention de nommage est `pluginIcon.svg` comme icône par défaut et `pluginIcon_dark.svg` pour le thème darcula.

Les icônes du plugin doivent être listées avec le fichier `plugin.xml` dans le chemin `resources/META-INF`.

#### Construction pour la distribution

Le plugin est maintenant prêt à être construit et distribué. Pour cela, nous exécutons la tâche gradle `buildPlugin`. Sous `build/distributions`, un fichier zip apparaîtra que vous pouvez distribuer et installer manuellement dans votre IDE. Ajoutez ce fichier zip comme une [version sous votre dépôt github](https://github.com/olivernybroe/intellij-Dictionary/releases), afin que les utilisateurs aient la possibilité de le télécharger manuellement depuis votre dépôt.

#### Publication d'un plugin

Pour publier notre plugin afin qu'il puisse être téléchargé directement depuis le dépôt de plugins d'IntelliJ, nous devons nous connecter à notre compte JetBrains sur le [site web du dépôt de plugins](https://plugins.jetbrains.com/). Une fois connecté, un menu déroulant depuis votre nom de profil montre une option pour télécharger un plugin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5BoQz8Wh4KMKZnXq6oPwlA.png)

Saisissez toutes les informations dans la boîte de dialogue (vous devez ajouter une licence, mais cela est assez [simple avec Github](https://help.github.com/en/articles/licensing-a-repository)). Ici, nous ajoutons le fichier zip de distribution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C3i5sxGFzG70I98oWHElfA.png)

Lorsque vous soumettez le formulaire, vous pouvez maintenant voir votre plugin dans le dépôt de plugins. Cependant, les autres utilisateurs n'ont pas accès à celui-ci avant qu'IntelliJ ne l'ait approuvé. L'approbation de votre plugin prend généralement 2 à 3 jours.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vvizHF3GWpNrG6XZ4u2qWA.png)

#### Mise à jour de votre plugin via Gradle

Après la création du plugin, nous pouvons le mettre à jour par programmation. Pour cela, la meilleure pratique est de créer un jeton. Ouvrez jetbrains hub et allez dans l'onglet [authentification](https://hub.jetbrains.com/users/me?tab=authentification). À partir de là, appuyez sur `New token...` et ajoutez la portée `Plugin Repository`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y-QOaZbX_IFv9DbbCAME8A.png)

Lorsque vous appuyez sur créer, vous obtenez un jeton. Créez un fichier appelé `gradle.properties` et ajoutez le jeton sous la clé `intellijPublishToken` (n'oubliez pas d'ignorer ce fichier avec git).

Dans notre fichier `build.gradle`, nous ajoutons simplement ce qui suit :

```
publishPlugin {
    token intellijPublishToken
}
```

Et nous pouvons maintenant exécuter la tâche gradle `publishPlugin` pour publier notre nouvelle version. Tous les numéros de version doivent être uniques, sinon la mise à jour échouera. Lorsqu'une mise à jour est créée, vous devez attendre 2 à 3 jours pour qu'ils approuvent la mise à jour.

Après avoir attendu quelques jours, notre plugin a maintenant été approuvé et peut être trouvé dans la place de marché des plugins en recherchant dictionary !

![Image](https://cdn-media-1.freecodecamp.org/images/1*vKzCf9d4QgpNVZ11j8luWA.png)

#### Conclusion

J'espère que cet article vous a donné plus de courage pour commencer à développer vos propres plugins. L'un des plus grands problèmes que j'ai eus lors de son développement était de trouver quelles classes utiliser. IntelliJ a un [guide complet](https://www.jetbrains.org/intellij/sdk/docs/welcome.html) que je vous recommande de lire du début à la fin, cependant, de nombreuses classes ne sont pas mentionnées. Dans les cas où vous êtes bloqué, ils ont un [chat Gitter](https://gitter.im/IntelliJ-Plugin-Developers/Lobby) qui est vraiment utile et il y a des personnes d'IntelliJ pour aider également.

Le code source de ce projet peut être trouvé sur [Github](https://github.com/olivernybroe/intellij-Dictionary) et le plugin que nous avons créé est dans la [place de marché JetBrains](https://plugins.jetbrains.com/plugin/12089-dictionary).