---
title: How to create an IntelliJ plugin — let’s build a simple dictionary finder
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
seo_title: null
seo_desc: 'By Oliver Nybroe

  Most of us developers use IntelliJ platforms, either IDEA, PHPStorm, WebStorm, Android
  Studio, PyCharm and the list goes on and on. However sometimes when we use it, we
  find that a feature is missing, but we have no idea how to actua...'
---

By Oliver Nybroe

Most of us developers use IntelliJ platforms, either IDEA, PHPStorm, WebStorm, Android Studio, PyCharm and the list goes on and on. However sometimes when we use it, we find that a feature is missing, but we have no idea how to actually add that feature and eventually just live without it.

In this article I will cover how we can create a simple plugin for all of the IntelliJ IDEs so when you add a `project.dic` file, it will automatically add it as one of your dictionaries. It will also search for the file in packages, so packages can add custom words to the dictionary. A `.dic` file is a simple dictionary where each line is a word in the dictionary.

The project is just a sample to get you started on developing your own plugins. But it’s actually also a feature I have been missing, as when I develop a custom package with my own words in it, I hate that I have to add them each time in the project level dictionary.

### Creating the project

When creating plugins for IntelliJ, we have to option to do it in either Java or Kotlin. I will do it in Java as most users are familiar with that. As this is a Java project, we will use IntelliJ IDEA as our IDE.

According to the [development guide](https://www.jetbrains.org/intellij/sdk/docs/basics/getting_started.html), the recommended way to create a project is by using [Gradle](https://www.jetbrains.org/intellij/sdk/docs/tutorials/build_system.html). We start by opening up `preferences` and check if `Gradle` and `Plugin DevKit` plugins are installed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ASJDtMw774VpAgoWCZEmkw.png)

After installing the plugins and restarting the IDE, we go to the new projects flow and under `Gradle`. In here there is now an option called `IntelliJ Platform Plugin` which is the one we need.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NTFEQjxMv7BBrHSzBj1THw.png)
_Project creation flow step 1_

Then go through the rest of the project creation flow as normal — in this project I choose the following configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qYo4hPtRV5aCWblW5HxzDA.png)
_Project creation flow step 2_

![Image](https://cdn-media-1.freecodecamp.org/images/1*eqsj6ej8Qiqx4VzAEer2cQ.png)
_Project creation flow step 3_

![Image](https://cdn-media-1.freecodecamp.org/images/1*ehSxccowC6-IR1tJ9h-5iQ.png)
_Project creation flow step 4_

### Setting up `plugin.xml`

Now that we have a project, we have to setup our `plugin.xml` file and `build.gradle`. The `plugin.xml` file is a file used by IntelliJ which defines all the information about the plugin. This includes the name, dependencies, what actions it should add or if it should extend something in IntelliJ. Basically this file defines everything your plugin should do and is the root of your project. In our `build.gradle` file we can define some of the values from `plugin.xml`, and information like which version of IntelliJ we want to test our plugin on when building with gradle.

Let’s start by defining our `plugin.xml` file. You can find the file in `src/main/resources/META-INF/plugin.xml`. We want our plugin to be available on all IntelliJ IDE’s so we set our `dependencies` to `com.intellij.modules.lang`. Right now our file looks like this:

```
<idea-plugin>    <id>dk.lost_world.Dictionary</id>    <name>Dictionary</name>    <vendor email="olivernybroe@gmail.com" url="https://github.com/olivernybroe/intellij-Dictionary">GitHub</vendor>    <depends>com.intellij.modules.lang</depends></idea-plugin>
```

However right now this does not have any logic, and we do not register anything to the IntelliJ platform.

As this project will find `project.dic` files inside a project and register them as dictionaries in that project, we will have to register a Project level component. This component will be called when a project is opened and closed. Let’s create a class and implement the `ProjectComponent` interface. When we hover over the class name it tells us that the component is not registered.

![Image](https://cdn-media-1.freecodecamp.org/images/1*imcg1FilSnSxkgJG6J9-0g.png)
_Hints on class_

We can then call the action called `Register Project Component` and it will register it for us in the `plugin.xml` file.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b4OvFSeoPWJ6UDAtgKF_Vg.png)
_Actions on class_

If we open `plugin.xml` the following code should be added. If it wasn’t added when calling the action, then just add it manually.

```
<project-components>    <component>        <implementation-class>dk.lost_world.dictionary.DictionaryProjectComponent</implementation-class>    </component></project-components>
```

#### IntelliJ Filesystem

When working with files in IntelliJ, we use a [**V**irtual **F**ile **S**ystem (VFS)](https://www.jetbrains.org/intellij/sdk/docs/basics/virtual_file_system.html). The VFS gives us a universal API to talk with files, without us having to think about if they are from FTP, an HTTP server or just on the local disk.

As our plugin looks for files called `project.dic` it will of course need to talk with the **V**irtual **F**ile **S**ystem. All files in the VFS are [Virtual Files](https://www.jetbrains.org/intellij/sdk/docs/basics/architectural_overview/virtual_file.html). This can sound a little intimidating, but in reality it is just an API for a filesystem and for a file. The way to think about it is just that the **V**irtual **F**ile **S**ystem is your file system interface and the Virtual Files are your files.

#### Spell Checker Settings

As IntelliJ already has support for `.dic` files and spell checking in general, the only thing we need to do is register our `project.dic` files in the spell checkers settings.

All the settings for the spell checker are saved in a class called `com.intellij.spellchecker.settings.SpellCheckerSettings`. To get an instance of it, simply call the `getInstance` method (most of the IntelliJ classes got a `getInstance` method which uses IntelliJ’s `ServiceManager` underneath).  
The settings class got a method called `getCustomDictionariesPaths` which returns all of the paths to dictionaries which are installed by the user.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pee95tAmC6aeTfpkOuBeew.png)
_API of getCustomDictionariesPaths_

When looking at the method signature, we also see an annotation called `AvailableSince`. We will later use the value in this annotation to specify the minimum required version for our plugin to work.

As the method returns a list, we can simply call `add` on the method to add in a new path to a dictionary.

#### Running Our Plugin (build.gradle)

As we now know how to add a dictionary to the spell checker, let’s add a small code example in our `DictionaryProjectComponent` class for doing this.

```
public class DictionaryProjectComponent implements ProjectComponent {    private Project project;    public DictionaryProjectComponent(Project project) {        this.project = project;    }    @Override    public void projectOpened() {        SpellCheckerSettings            .getInstance(project)            .getCustomDictionariesPaths()            .add("./project.dic");    }}
```

This code will register a `project.dic` file from the root of our project whenever the project is opened.

To test out our little example, we need to update our `build.gradle` file. In the `intellij` section of the gradle file we add in what version of IntelliJ we want to use. This version number is the one from the `AvailableSince` annotation on the `SpellCheckerSettings` class.

```
plugins {    id 'java'    id 'org.jetbrains.intellij' version '0.4.4'}group 'dk.lost_world'version '1.0-SNAPSHOT'sourceCompatibility = 1.8repositories {    mavenCentral()}dependencies {    testCompile group: 'junit', name: 'junit', version: '4.12'}// See https://github.com/JetBrains/gradle-intellij-plugin/intellij {    pluginName 'Dictionary'    version '181.2784.17'    type 'IC'    downloadSources true}
```

Running the `runIde` command from gradle will start up an instance of IntelliJ of the specific version. After starting up the testing IDE our plugin should have been run. If we open up `preferences > Editor > Spelling > Dic`tionaries we can see under custom dictionaries that the path we specified in our example is now added.

![Image](https://cdn-media-1.freecodecamp.org/images/1*69zQmR1XsQ4txhWfgT3niw.png)
_Showing dictionaries preferences from IntelliJ IDE_

We are now able to test our plugin, so now it is time to build it out correctly so it finds the `project.dic` files and registers them for us.

In the `DictionaryProjectComponent::projectOpened` method, we need to first find all files called `project.dic` and register them and also add a file listener so when new `project.dic` files are added, they are registered automatically.

### Dictionary Class

We will have a class called `Dictionary`, this class will contain the logic for us to register and remove files from the dictionary. The class will have the following public methods:   
`void registerAndNotify(Collection<VirtualFile> files)`  
`void registerAndNotify(VirtualFile file)`  
`void removeAndNotify(VirtualFile file)`  
`void moveAndNotify(VirtualFile oldFile, VirtualFile ne`wFile)

These methods will also create a notification about what happened, so the end user knows what changed with the custom dictionaries. The end file for this will look the following way:

#### Finding all dictionary files

For finding all the dictionary files in the project called `project.dic` we use the class `[FilenameIndex](http://www.jetbrains.org/intellij/sdk/docs/basics/psi_cookbook.html#how-do-i-find-a-file-if-i-know-its-name-but-dont-know-the-path)`. The file is in the namespace `com.intellij.psi.search.FilenameIndex`, it has a method `getVirtualFilesByName` which we can use to find our `project.dic` files.

```
FilenameIndex.getVirtualFilesByName(    project,    "project.dic",    false,    GlobalSearchScope.allScope(project))
```

This call will return all Virtual Files which matches the search criteria. We then put the return result into the Dictionary class method `registerAndNotify`.

```
@Overridepublic void projectOpened() {    Dictionary dictionary = new Dictionary(project);    dictionary.registerAndNotify(        FilenameIndex.getVirtualFilesByName(            project,            "project.dic",            false,            GlobalSearchScope.allScope(project)        )    );}
```

Our code is now able to find `project.dic` files at start up and register them, if they are not already registered. It will also notify about the newly registered files.

#### Adding a Virtual File Listener

The next part is for us to listen for changes in virtual files. To do this we need a listener. For this we need the `com.intellij.openapi.vfs.VirtualFileListener`.

In the docblock for the listener class we can see that to register it we can use `VirtualFilemanager#addVirtualFileListener`.  
Let’s create a class named `DictionaryFileListener` and implement the methods which we need for our project.

Then we update our `projectOpened` class to also add the `VirtualFileListener`.

```
@Overridepublic void projectOpened() {    Dictionary dictionary = new Dictionary(project);    dictionary.registerAndNotify(        FilenameIndex.getVirtualFilesByName(            project,            "project.dic",            false,            GlobalSearchScope.allScope(project)        )    );    VirtualFileManager.getInstance().addVirtualFileListener(        new DictionaryFileListener(dictionary)    );}
```

Our plugin is now able to find our dictionary files at startup, but also listen for if a dictionary file is added later on. The next thing we need is to add information for our plugin listing.

#### Adding plugin information

To add information about the plugin, we open the `build.gradle` file and edit the object `patchPluginXml`. In here we need to specify which build version is required for the plugin, version of the plugin, description and change notes.

```
patchPluginXml {    sinceBuild intellij.version    untilBuild null    version project.version    pluginDescription """Plugin for having a shared dictionary for all members of your project. <br><br>It will automatically find any <code>project.dic</code> files and add themto the list of dictionaries. <br><br>It will also search packages for dictionary files and add them to our list of dictionaries.    """    changeNotes """<p>0.2</p><ul>    <li>Added support for listening for when a <code>project.dic</code> file is added, moved, deleted, copied.</li></ul><p>0.1</p><ul>    <li>First edition of the plugin.</li></ul>    """}
```

We also update the `version` property to `'0.2'`of the gradle project itself. The plugin can now run on all versions since the method for registering custom dictionaries was added.

To test if it generates the desired output, we can run the gradle task `patchPluginXml` and under `build/patchedPluginXmlFiles` our generated `plugin.xml` file will be there.

Since IntelliJ version `2019.1`, [all plugins supports icons](http://www.jetbrains.org/intellij/sdk/docs/basics/plugin_structure/plugin_icon_file.html). As this is fairly new a lot of plugins do not have an icon, and your plugin can stand out a lot by having one. The naming convention is `pluginIcon.svg` as the default icon and `pluginIcon_dark.svg` for the darcula theme.

The plugin icons should be listed together with the `plugin.xml` file in the path `resources/META-INF`.

#### Building for distribution

The plugin is now ready to be built and shipped. To do this we run the gradle task `buildPlugin`. Under `build/distributions` a zip file will appear which you can distribute and install manually in your IDE. Add this zip file as a [release under your github repo](https://github.com/olivernybroe/intellij-Dictionary/releases), so users have the option to download it manually from you repo.

#### Publishing a plugin

To publish our plugin so it can be downloaded directly from IntelliJ’s plugin repository, we need to login on our JetBrains account on the [Plugin Repository website](https://plugins.jetbrains.com/). When in here, a dropdown from your profile name shows an option to upload a plugin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5BoQz8Wh4KMKZnXq6oPwlA.png)

Input all the information in the dialog (you have to add a license, but that is pretty [straightforward with Github](https://help.github.com/en/articles/licensing-a-repository)). Here we add the distribution zip file.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C3i5sxGFzG70I98oWHElfA.png)

When you submit the form, you can now see your plugin in the plugin repository. However other users do not have access to it before IntelliJ has approved it. Approving your plugin normally takes 2–3 days.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vvizHF3GWpNrG6XZ4u2qWA.png)

#### Updating your plugin via Gradle

After the plugin has been created, we can update it programmatically. To do this the best practice is to create a token. Open up jetbrains hub and go to the [authentification tab](https://hub.jetbrains.com/users/me?tab=authentification). From here press `New token...` and add the scope `Plugin Repository`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y-QOaZbX_IFv9DbbCAME8A.png)

When pressing create you get a token. Create a file called `gradle.properties` and add the token under the key `intellijPublishToken` (remember to git ignore this file).

In our `build.gradle` file, we simply add the following:

```
publishPlugin {    token intellijPublishToken}
```

And we can now run the gradle task `publishPlugin` for publishing our new version. All versions numbers have to be unique or else it will fail updating. When an update is created, you have to wait 2–3 days again for them to approve the update.

After waiting some days our plugin has now been approved and can now be found in the plugin marketplace by searching for dictionary!

![Image](https://cdn-media-1.freecodecamp.org/images/1*vKzCf9d4QgpNVZ11j8luWA.png)

#### Conclusion

I hope this article has given you more courage to start developing your own plugins. One of the biggest problems I had while developing it was to find out which classes to use. IntelliJ has an [extensive guide](https://www.jetbrains.org/intellij/sdk/docs/welcome.html) which I would recommend that you read from start to end, however a lot of classes are not mentioned in there. In cases where you get stuck, they have a [Gitter chat](https://gitter.im/IntelliJ-Plugin-Developers/Lobby) which is really helpful and there are people from IntelliJ on there to help also.

The source code for this project can be found on [Github](https://github.com/olivernybroe/intellij-Dictionary) and the plugin we created is in the [JetBrains marketplace](https://plugins.jetbrains.com/plugin/12089-dictionary).

