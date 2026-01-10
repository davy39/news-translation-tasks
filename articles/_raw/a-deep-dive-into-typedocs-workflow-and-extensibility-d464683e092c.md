---
title: A deep dive into TypeDoc’s workflow and extensibility
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T19:46:01.000Z'
originalURL: https://freecodecamp.org/news/a-deep-dive-into-typedocs-workflow-and-extensibility-d464683e092c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZFveofx2WsPuiHo__izU1w.gif
tags:
- name: api
  slug: api
- name: documentation
  slug: documentation
- name: plugins
  slug: plugins
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Alexander Kamenov

  This topic aims to cover the basics on how you could extend the TypeDoc library
  functionality and what are the opportunities that it provides.

  For those of you who are not familiar with TypeDoc, this is a library which allows
  you...'
---

By Alexander Kamenov

This topic aims to cover the basics on how you could extend the **TypeDoc** library functionality and what are the opportunities that it provides.

For those of you who are not familiar with **TypeDoc**, this is a library which allows you to generate an API documentation based on your comments from your **TypeScript** source code.

By default there are two possible outputs:

* _Static website_
* _JSON file._

If you want to find more about configuration and terms of use please refer to the [**README**](https://github.com/TypeStrong/typedoc#typedoc).

### The problem I have encountered

The lack of documentation is a really common scenario, and this was the problem we faced. As most of you probably know, debugging and digging into any kind of software with exploratory purposes takes time. That’s why I decided to contribute and share the knowledge I’ve gained during the development of a [plugin](https://github.com/IgniteUI/typedoc-plugin-localization) which provides users with the ability to localize their documentation into multiple languages.

Good example here is the [Japanese API documentation](https://jp.infragistics.com/products/ignite-ui-angular/docs/typescript/latest/) that [Ignite UI for Angular library](https://github.com/IgniteUI/igniteui-angular) provides.

So I’m going to give a rough explanation of how **TypeDoc** works and what was the approach that was taken during the development of that plugin.

I won’t go much into detail about how the library works. Instead I will try to expose only the most important aspects of the execution flow which, in my opinion, are the base of the “tree” from where you can start exploring and diverting into different “branches”.

So without wasting more time, let’s move on to the essential part.

### How typedoc works.

#### Several components/classes you need to know about:

* [Application](https://typedoc.org/api/classes/application.html)**:**  
The default main application **class**.
* [Options](https://typedoc.org/api/classes/options.html):  
Aggregates and contributes configuration declarations, declared by components or plugins. Parses **option** values from various sources (config file, command-line, args, etc.)
* [Converter](https://typedoc.org/api/classes/converter.html):  
Compiles source files using **TypeScript** and converts compiler symbols to reflections.
* [ProjectReflection](https://typedoc.org/api/classes/projectreflection.html):  
A reflection that represents the **root** of the **project**.  
The project **reflection** acts as a global index. You may receive all reflections and source files of the processed project through this **reflection**.
* [Renderer](https://typedoc.org/api/classes/renderer.html):  
The **renderer** processes is a representation of [ProjectReflection](https://typedoc.org/api/classes/projectreflection.html), using a **BaseTheme** instance and writes the emitted html documents to an output directory.  
Simply, the **renderer** is used for generating the documentation output.
* [EventDispatcher](https://typedoc.org/api/classes/eventdispatcher.html):  
A class that provides a custom event channel.  
You may bind a callback to an event with ‘on’ or remove with ‘off’.
* [Logger](https://typedoc.org/api/classes/logger.html):  
The logger provides you with the ability to log without interruption any kind of errors or messages like success, warn, log, verbose, etc.
* [PluginHost](https://typedoc.org/api/classes/pluginhost.html):  
Responsible for discovering and loading plugins.

### Typedoc Execution Flow:

![Image](https://cdn-media-1.freecodecamp.org/images/0*xdTMvvjTlHlIwg44)

* Application tries to load all **TypeDoc** plugins by searching for **‘typedocplugin’** keyword declared into your **package.json** file.

* [Converter](https://typedoc.org/api/classes/converter.html)**:** Using **TypeScript API** in order to compile the referred project. If any compile errors are detected in the project, the convert process ends with the error that has been encountered.  
From the above diagram you can see that during the **Resolve Reflections** process, which comes right after the compilation process, the [EventDispatcher](https://typedoc.org/api/classes/eventdispatcher.html) emits several events which are a good prerequisite for manipulating or retrieving data.  
Once the conversion process ends we receive a [ProjectReflection](https://typedoc.org/api/classes/projectreflection.html) object which represents the project itself with all files and their comments.
* [Options](https://typedoc.org/api/classes/options.html)**:** Determines what would be the output of your documentation based on the [options](https://github.com/TypeStrong/typedoc#arguments) you have passed**.** There are two variants:  
 1. **JSON file**: Represents a **stringified** version of [ProjectReflection](https://typedoc.org/api/classes/projectreflection.html) object. This is what the [Serialization](https://typedoc.org/api/classes/serializer.html) does  
 2. **Static HTML** website.
* [Renderer](https://typedoc.org/api/classes/renderer.html)**:** At first the **renderer** needs to ensure that the **Theme** that corresponds to the **output static website** and the **output directory**, are set up correctly. If everything is fine, the **renderer** starts mapping the **Reflections** with the **Templates** from the **Theme**.  
Here the [RendererEvent](https://typedoc.org/api/classes/rendererevent.html) emits two events [BeginRenderer](https://typedoc.org/api/classes/rendererevent.html#begin)/[EndRenderer](https://typedoc.org/api/classes/rendererevent.html#end) suitable for manipulating the output data.
* **Finish Rendering**: This is where the process ends and the output of generated documentation is provided.

After that rough explanation and visualization of the execution flow we are ready to move on and see how to actually proceed with the **extensibility**.

### Extending typedoc

#### Set up the project:

The very first step we need to take is setting up a [node project with npm](https://www.wolfe.id.au/2014/02/01/getting-a-new-node-project-started-with-npm/).

Declare that **keyword `typedocplugin`** into your **package.json:**

Then we need to [export a module](https://nodejs.org/api/modules.html#modules_exports) which would serve as an entry point of the project. How does **TypeDoc** load the plugins? It simply searches through all **node_modules** packages and their **package.json** file, and when that **keyword** is encountered it [requires](https://nodejs.org/api/modules.html#modules_require_id) that package and executes it as a function by passing a reference to the main **Application** class.

Once all those steps are performed we have the freedom to manipulate the execution process and the output data as we want **?.**

### Approaches and examples

As I mentioned earlier, all the knowledge I share in this article was gained during the development of a [localization plugin](https://github.com/IgniteUI/typedoc-plugin-localization), which I firmly believe takes full advantage of what **TypeDoc** offers as an opportunity to extend. So all the examples and approaches below are inspired by the idea and the source of that “**creature**”.

In order to understand how it works, you can go through the [README](https://github.com/IgniteUI/typedoc-plugin-localization#typedoc-plugin-localization) file. It is enough to understand the first 3 steps.

Let’s start with the **main module (**[index.ts](https://github.com/IgniteUI/typedoc-plugin-localization/blob/master/index.ts)**)** file which **typedoc** executes once it requires the **plugin.** As we already know, a reference to the default **Application** class is passed through the **require** callback, where you have access to all those main components we have talked about in the **How TypeDoc works** section.

Through all those component references you are able to register your own custom components, and depending on what they extend, a different set of events are provided.

Sometimes just a theory is insufficient, so let’s move on and see how things happen in practice.

Here are the four most important things that we are going to review:

* _Register our own options._
* _Manipulating or retrieving the data during the conversion process._
* _Manipulating or retrieving the data during the **renderer** process._

#### Register our own option.

As we already know, all of the component registrations happen in the **main module**. The important part here is that, in order to register a component within the [options](https://typedoc.org/api/classes/options.html) context, you need to **extend** the [OptionsComponent](https://typedoc.org/api/classes/optionscomponent.html) class.

The custom definition of the [OptionComponent](https://github.com/IgniteUI/typedoc-plugin-localization/blob/master/components/options-component.ts) looks like this:

At the end you need to add that declaration into the options that the application provides.

You can refer to the [README](https://github.com/IgniteUI/typedoc-plugin-localization#arguments) of the extension/plugin we are talking about and see what kind of options are exposed and how they contribute to the process.

#### Manipulating or retrieving the data during the conversion process

The registration process here is the same, but instead of extending [OptionsComponent](https://typedoc.org/api/classes/optionscomponent.html) you need to extend [ConverterComponent](https://typedoc.org/api/classes/convertercomponent.html).

As you probably understood, the way we interact with the data is through the **events** that the [EventDispatcher](https://typedoc.org/api/classes/eventdispatcher.html) **emits**. So all the **events** that you can subscribe for within that context can be found and accessed through the [**Converter**](https://typedoc.org/api/classes/converter.html).

We will take a look within the context of the [EVENT_RESOLVE](https://typedoc.org/api/classes/converter.html#event_resolve) **event** callback. The event gets triggered every time when **TypeDoc** resolves a **Class**, **Interface** or **Enum** or (**method**, **property**, **etc.**) part of a particular **Class**, **Interface** or **Enum**. Wait what?

Okay It’s a bit of confusing, but the concept is as simple as iterating an array.

Let’s take an example of a simple class.

The event will emit four times referencing each unit per this declaration, transformed in [DeclarationReflection](https://typedoc.org/api/classes/declarationreflection.html):

1. **_Emits_** _the class with reference to all his [children](https://typedoc.org/api/classes/declarationreflection.html#children) (**b**, **c, d**)._
2. **_Emits_** _the property **b** with reference to his [parent](https://typedoc.org/api/classes/declarationreflection.html#parent) (class **A**)._
3. **_Emits_** _the property **c** with reference to his [parent](https://typedoc.org/api/classes/declarationreflection.html#parent)_ (class **A**).
4. **_Emits_** _the method **d** with reference to his [parent](https://typedoc.org/api/classes/declarationreflection.html#parent)_ (class **A**).

Hope everything is clearer now!

Let’s see how we can subscribe for the emitted events:

Then in the **resolve callback** you can see how the comments per every **Class**, **Enum** and **Interface** are taken and stored into a **JSON** file which represents each unit (**Class**, **Enum**, **Interface**) separately. For instance if we have two classes **A** and **B,** the output folder would contain two **JSON** files **A.json** and **B.json**.

The next example represents the moment where the comments per every **getter** and **setter** are retrieved which is the next unit of the **Class** declaration we talked about a little earlier.

These are just examples, of course — you can do whatever you want here.

#### Manipulating or retrieving the data during the Renderer process

Here we have the same concept as the **Convert**, but of course we need to extend another class. Guess what — the name of the class is [RendererComponent](https://typedoc.org/api/classes/renderercomponent.html), and the object that holds the event references is [RendererEvent](https://typedoc.org/api/classes/rendererevent.html).

The variety of the events is less than the [Converter](https://typedoc.org/api/classes/converter.html) but the information that the events provide is more than enough.

Subscription is the same:

Here, the behavior of the [RendererEvent.BEGIN](https://typedoc.org/api/classes/rendererevent.html#begin) event is a bit different. It gets triggered just once when the **Renderer** process has just started. Then all of the **reflections** that the **Converter** has created are taken, and with the “**power**” of the **forEach** we are going through each [DeclarationReflection](https://typedoc.org/api/classes/declarationreflection.html) and processing it:

What does the process do? It just takes the location of the **JSON** files that the **Converter** has built and replaces the content from those **JSONs** with the content in the reflection.

The example here again refers the manipulation of the **getters** and **setters** per current **Class**:

Of course again here you can improvise and do whatever you need.

### Conclusion

This is probably only one third of what the plugin does. There is much more that I can show and expose as functionality. For example how we came up with a solution for manipulating the **hardcoded strings** within our custom [theme](https://github.com/IgniteUI/igniteui-angular/tree/master/extras/docs/themes/typedoc). But the purpose of this blog is focused on the **extensibility** and **manipulation** of the **data**. So if you have further questions or interests you can let me know in the comments below.

