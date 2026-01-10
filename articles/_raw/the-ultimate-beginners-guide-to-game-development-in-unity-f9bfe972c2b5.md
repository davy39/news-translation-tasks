---
title: The Ultimate Beginners Guide To Game Development In Unity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-21T20:27:47.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-beginners-guide-to-game-development-in-unity-f9bfe972c2b5
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca41d740569d1a4ca6043.jpg
tags:
- name: Game Development
  slug: game-development
- name: gaming
  slug: gaming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: unity
  slug: unity
seo_title: null
seo_desc: 'By Hugo Dolan

  Unity is a great tool for prototyping everything from games, to interactive visualisations.
  In this article, we run through all you need to know to get started using Unity.

  First, a little bit about me: I’m a hobbyist unity developer, 3...'
---

By Hugo Dolan

Unity is a great tool for prototyping everything from games, to interactive visualisations. In this article, we run through all you need to know to get started using Unity.

First, a little bit about me: I’m a hobbyist unity developer, 3d modeler and graphic designer who’s worked with Unity and Blender for over 5 years. I’m now a Financial Maths student at University College Dublin, and occasionally I do freelance graphic design, web prototyping, and game prototyping.

![Image](https://cdn-media-1.freecodecamp.org/images/Q-bD3OdyDZX2X2cmqgyyRIFwRpy9mngdYAtC)
_Concept art is one of the earliest phases in the game dev process, over the last 5 years i’ve got a lot of exposure to all areas of game design. Check out my [Portfolio ](http://hugodolan.com/portfolio" rel="noopener" target="_blank" title=")of Graphic, UX, Concept Art, Game Dev etc…_

### Introduction

This article is aimed at anyone who has never used Unity before, but has some previous experience programming or in web design / development. By the end of this article, you should have a good general overview of the engine as well as all the necessary functions and code to start making a basic game.

### Why Unity?

#### If you want to make games

There’s really very few options when it comes to Indie Game development. The three main choices if you want to build games are Unreal, Unity or GameMaker.

Unity is probably the least opinionated of the 3 platforms. It gives you a very raw product out of the box, but is highly flexible, well-documented, and highly extensible to build pretty much any genre of game you can think of.

There are plenty of highly successful games such as Escape from Tarkov (FPS), Monument Valley (Puzzler), and This War of Mine (Strategy / Survival) all built in Unity.

In reality the engine you build your first game on is probably not critical, so my advice is just to pick one and go with it.

#### If you want to prototype user experiences

Since unity is just an engine with a bunch of physics, animation, and real time 3d rendering, it’s also a great space to make fully fledged interactive prototypes for UX studies.

Unity has full support for VR and AR and hence could be a great tool for exploring architecture, automations and simulations with clients.

### **Sections to this article**

* **Why Unity?**
* **Unity Editor Window**
* **Unity Game Objects**
* **Unity Builtin Components**
* **Creating Custom Components**
* **Structure of a MonoBehaviour**
* **Manipulating GameObjects**
* **Raycasting**
* **Collision detection**
* **Advanced Features**
* **Advice For Newcomers**
* **Nice Resources and Communities**
* **Conclusion**

### **Unity editor window**

The editor window is split up into a couple of sections. We will cover this very briefly as we will refer to it constantly throughout the article. If your familiar with this already just skip past!

![Image](https://cdn-media-1.freecodecamp.org/images/hOKvEBDHVZj2N1udUtho7ksnzXmcdbMTWAWh)

> **Scene View:** Allows placement and movement of GameObjects in the Scene

> **Game View:** Previews how the player will see the scene from the camera

> **Inspector:** Provide details on the selected GameObject in the scene.

> **Assets / Project:** All prefabs, textures, models, scripts etc are stored here

> **Hierarchy:** Enables nesting and structuring of GameObjects within the scene

Now we’re good to start!

### Unity Game Objects

#### What are GameObjects

GameObjects are the core building block of everything in the Unity games engine. The name almost gives it away:

> Anything you place within a scene in Unity must be wrapped in a ‘game object.’

If you’ve got a web design background, you can think of GameObjects as being a lot like <div> elements! Extremely boring containers, but are highly extensible to create complex functionality or visuals.

![Image](https://cdn-media-1.freecodecamp.org/images/vlXNfFyr4lsQgC-DL05daoOtSWT35ZFUcA1l)
_I’ve lifted this straight out of the Unity editor window just to make this point._

Literally everything from particle effects, cameras, players, UI elements, … (the list goes on) is a GameObject.

#### Creating Hierarchy

Like a <div> in web development, a GameObject is also a container. Just as you nest <div>s to create varied and desirable layouts or abstractions you may wish to do the same with games objects.

> The logic behind nesting game objects is much the same as web development, I’ll give a few examples…

**Clutter & Efficiency**

> **_Web Analogy:_** _You’ve got many similar elements which may be dynamically generated on the fly in response to user interaction and want to keep them tidy._

> **_Unity Translation:_** _Your building a Minecraft clone and you’ve loads of blocks in the scene, you need to add and remove ‘chunks’ of blocks from the scene for performance reasons. Thus having them parented to an empty GameObject for each chunk makes sense, as deleting the chunk parent removes all the children blocks._

**Positioning**

> **_Web Analogy:_** _You want to keep the position of the content contained ‘relative’ to the container and not to the web page._

> **_Unity Translation:_** _You’ve created a bunch of helper drones which hover around the player. You would really not rather write code to tell them to chase after the player, so instead you instantiate them as children of the player game object._

### Unity Builtin Components

#### The Actor Component Model

GameObjects on their own are pretty useless — as we’ve seen they’re pretty much just containers. In order to add functionality to them we have to add components, which are essentially scripts written in either C# or Javascript.

Unity works off an Actor Component model, put simply the GameObjects are the actors and the Components are your scripts.

If you’ve written any web apps before you’ll be familiar with the idea of creating small reusable components such as buttons, form elements, flexible layouts that have various different directives and customisable properties. Then assembling these small components into larger web pages.

The big advantage of this approach is the level of reusability and clearly defined communication channels between elements. Likewise in game development, we want to minimise the risk of unintended side effects. Small bugs tend to spiral out of control if you’re not careful, and are extremely difficult to debug. Thus creating small, robust and reusable components is critical.

#### Key Built-in Components

I think it’s time for a few examples of the built in components provided by the Unity Games engine.

* **MeshFilter:** Allows you to assign materials to a 3D mesh to a GameObject
* **MeshRender:** Allows you to assign materials to a 3D Mesh
* **[Box | Mesh]Collider:** Enables detection of GameObject during collisions
* **Rigidbody:** Enables realistic physic simulation to act on GameObjects with 3d Meshes and will be trigger detection events on box colliders
* **Light:** Illuminates portions of your scene
* **Camera:** Defines the player viewport to be attached to a GameObject
* Various UI Canvas Components for displaying GUIs

There are loads more, but these are the main ones you’ll need to get familiar with. One tip is that you can access all the docs for these through the unity manual and scripting reference offline wherever you are:

![Image](https://cdn-media-1.freecodecamp.org/images/CNB5Rb4DWImRiHh04xThXYtZnojyCj5OJJ1f)
_Just click on the help section, the docs in general are pretty good_

### Creating Custom Components

The builtin components control physics and visuals primarily, but to really make a game, you’re going to need to accept user input and manipulate those standard components as well as the GameObjects themselves.

> To start creating components, go into the desired GameObject > Add Component > type the name of your new component in the search bar > new script (c#).

As a general recommendation I’d advise against using Javascript in Unity. It hasn’t been kept updated with all the great stuff that came with ES6, and most of the more advanced stuff relies on C# stuff ported over to Javascript… It just becomes a one giant work-around in my experience.

### Structure of a MonoBehaviour

#### Key Functions

All components inherit from the MonoBehaviour Class. It includes several standard methods, most importantly:

* **void Start()** which is called whenever an object containing the script is instantiated in the scene. This is useful anytime we want to perform some initialisation code, eg. set a player’s equipment after they spawn into a match.
* **void Update()** which is called every frame. This is where the bulk of code involving user input will go, updating various properties such as the motion of the player in the scene.

#### Inspector Variables

Often we want to make components as flexible as possible. For example all weapons might have a different damage, rate of fire, has_sight etc. Whilst all the weapons are essentially the same thing we may want to be able to create different variations quickly through the unity editor.

Another example where we might want to do this is when creating a UI component that tracks user mouse movements and places a cursor in the viewport. Here we might want to control the sensitivity of the cursor to movements (if the user was using a joystick or gamepad vs a computer mouse). Thus it would make sense to have these variable easy to change both in edit mode and also experiment with them during runtime.

![Image](https://cdn-media-1.freecodecamp.org/images/ARiWcy5AEsVyRicp7demoZnzQR0MjPQnFzXJ)
_Variables in the inspector window can be changed at any time during runtime or edit mode. Note: Changes made during runtime will not be permanent._

We can do this easily by simply declaring them as public variables in the body of the component.

![Image](https://cdn-media-1.freecodecamp.org/images/dMqFuop796E9p2Y4urYkJtsuM3Rh6oM07cIJ)
_Notice how we can make variables have different levels of access, private, public, or public but not displayed in the inspector window._

#### Accepting user input

Of course, we want our game to respond to user input. The most common ways to do that are using the following methods in the Update() function of a component (or anywhere else you like):

* Input.GetKey(KeyCode.W) Returns True W key is being held down
* Input.GetKeyDown(KeyCode.W) Returns True when W key is first pressed
* Input.GetAxis(“Vertical”), Input.GetAxis(“Horizontal”) Returns between -1,1 mouse input movement

### Manipulating GameObjects

Once we have user input we want GameObjects within our scene to respond. There are several types of responses we may consider:

* Translation, Rotation, Scale
* Create new GameObjects
* Sending messages to existing GameObjects / components

#### Transformations

GameObjects all have a transform property which enable various useful manipulations on the current game object to be performed.

![Image](https://cdn-media-1.freecodecamp.org/images/cqutjhXkSZxKNCywMSjGbxewqeDo5GCp0R-d)

The methods above are fairly self explanatory, just note that we use lowercase _gameObject_ to refer to the GameObject which owns this specific instance of the component.

In general it’s a good practice to use _local[Position,Rotation]_ rather than the global position / rotation of an object. This usually makes it easier to move objects in a manner that makes sense, as the local space axis will be oriented and centered on the parent object rather than the world origin and x,y,z directions.

![Image](https://cdn-media-1.freecodecamp.org/images/sgr4nHfYLQYqjEEPSxlxPA0BhCrNjgzzvOmW)
_The benefits of local space become a little more obvious with a diagram!_

If you need to convert between local and world space (which often is the case) you can use the following:

![Image](https://cdn-media-1.freecodecamp.org/images/vNEw9xUc-B2vZOaeAqXcQn5W-lxfmJbLiEZw)

As you can imagine, there is some fairly simple linear algebra behind this hinted at by the ‘Inverse’ in the method name.

#### Creating new GameObjects

Since GameObjects are basically everything in your scene, you might want to be able to generate them on the fly. For example if your player has some sort of projectile launcher you might want to be able to create projectiles on the fly which have their own encapsulated logic for flight, dealing damage, etc…

First we need to introduce the notion of a _Prefab_. We can create these simply by dragging any GameObject in the scene hierarchy into the assets folder.

![Image](https://cdn-media-1.freecodecamp.org/images/BEBGqpePGsVgtEY5y89WrnLAbdZjPHZiagjZ)
_What prefab looks like in the Asset tab_

This essentially stores a template of the object we just had in our scene with all the same configurations.

![Image](https://cdn-media-1.freecodecamp.org/images/wFLWTKOYgxfMEAEzUjgMsTCETSmTA3JIPLGp)
_An example of a custom brick object which is used to dynamically generate Lego bricks in a scene, it has a bunch of components attached to it with various default values._

Once we have these prefab components we can assign them to inspector variables (as we talked about earlier) on any component in the scene, so that we can create new GameObjects as specified by the prefab at any time.

We can then perform ‘instantiation’ of the prefab and manipulate it to the desired location in the scene and establish the necessary parent relationships.

![Image](https://cdn-media-1.freecodecamp.org/images/xAzUlbgEAIkyS8bsX8W0xlVI0YiSTiVyMljj)

### Accessing other GameObjects and Components

Often we need to communicate with other GameObjects as well as their associated components. Once you have a reference to a game object this is pretty simple.

> ComponentName comp = some_game_object.GetComponent<ComponentName>();

After that you can access any of the public methods / variables of the component in order to manipulate the GameObject. This is the straightforward bit, however actually obtaining the reference to the GameObject can be done in several ways…

#### Access via inspector variable

This is the most straightforward. Simply create a public variable for the GameObject, as we’ve demonstrated earlier with the prefabs, and manually drag and drop it onto the component via the inspector. Then access the variable as above.

#### Access via tagging

We can tag GameObjects or prefabs via the inspector and then use the find game object functions to locate references to them.

![Image](https://cdn-media-1.freecodecamp.org/images/9Ur13zYuVV3r17CGo9hDMnyCoG44jTXCwv4g)

This is simply done as below.

> GameObject some_game_object = GameObject.FindGameObjectWithTag(“Brick”);

#### Access via transform

If we wish to access components in some parent object we can easily do this via the transform attribute.

> ComponentName comp = gameObject.transform.parent.GetComponent<ComponentName>();

#### Access via SendMessage

Alternatively if we want to send a message to many other components or wish to message an object which is far up a nested hierarchy, we can use the send message functions, which accept the name of the function followed by the arguments.

> gameObject.SendMessage(“MethodName”,params); // Broadcast message

> gameObject.SendMessageUpwards(“MethodName”, params); // Only received by components which are nested above.

### Raycasting

You may have heard of this before when people compare FPS games that are ‘physics based’ or ‘ray based’. Raycasting is essentially like having a laser pointer which, when it comes into contact with a ‘collider’ or ‘rigidbody’, it returns a ‘hit’ and passes back the details of the object.

There are two scenarios where this comes in handy (There’s probably loads more):

1. If you were designing a weapon system for a game, you could use raycasting for hit detection, and even customise the length of the ray so that melee items ‘hit’ only at short ranges
2. Create a ray from the mouse pointer to a point in 3d space, ie if you wish the user to be able to select units with their mouse in a strategy game.

![Image](https://cdn-media-1.freecodecamp.org/images/GcxZnE2hbosbWwoDp94ecEd1g8aVlwrFKOhB)
_Example 2 detailed above_

As you can see, the code for this is a little bit more involved. The key thing to understand is that to cast a ray to where the mouse is pointing in 3d space requires the ScreenPointToRay transformation. The reason for this is the camera is rendering a 3d space as a 2d viewport on your laptop screen, so naturally there is a projection involved to transfer back to 3d.

### Collision detection

Earlier we mentioned the Collider and Rigidbody components which can be added to an object. The rule for collisions is that one object in the collision must have a rigidbody and the other a collider (or both have both components). Note that when using raycasting, rays will only interact with objects with collider components attached.

Once setup within any custom component attached to the object, we can use the OnCollisionEnter, OnCollisionStay and OnCollisionExit methods to respond to collisions. Once we have the collision information we can get the GameObject responsible and use what we learned earlier to interact with components attached to it as well.

![Image](https://cdn-media-1.freecodecamp.org/images/ppKZgvdAjKDqbW80Nin2wG9izk08UjyuaqAt)

One thing to note is that rigid-bodies provide physics such as gravity for objects, so if you want this turned off you will need to check the _is_kinematic_ on.

![Image](https://cdn-media-1.freecodecamp.org/images/I9UU3oy-UoVWOwjhXUy9PRiGDT5eFO4O9-IB)
_Check on is kinematic to disable unwanted physics but retain nice collision detection._

### Advanced Features

We won’t go into any of this now but perhaps in a future article — just to make you aware that they exist.

#### Creating GUI’s

Unity has a fully fledged UI engine for laying out the GUI for your game. In general these components work pretty similarly to the rest of the engine.

#### Extending the Unity Editor

Unity enables you to add custom buttons to your inspectors so that you can affect the world during edit mode. For example, to help with world building you might develop a custom tool window for building modular houses.

#### Animation

Unity has a graph-based animation system which enables you to blend and control animations on various objects such as players implementing a bone based animation system.

#### Materials and PBR

Unity runs off a physically-based rendering engine which enables real time lighting and realistic materials. The reality is you will either need to learn 3d modeling first or use models made and optimised by someone else before you get to this, in order to make stuff that actually looks good.

### Advice For Newcomers

If you’re planning on writing your first game, don’t underestimate the complexity and time it takes to write even the most trivial of games. Remember most of the games that come out on Steam have teams working on them for years full-time!

Pick a simple concept and break it down into small achievable milestones. It’s highly recommended to separate your game into as small independent components as possible, as you’re much less likely to run into bugs if you keep the components simple rather than monolithic code blocks.

Before you go and write any code for any part of your game, go and research what someone else has done before to solve the same problem — chances are they’ll have a much slicker solution.

### Nice Resources and Communities

Game design has one of the best communities of any out there, and there are loads of highly skilled pros in the industry who put content up for free or for next to nothing. It’s a field that requires 3d Modelers, Concept Artists, Game Designers, Programmers and so on. I’ve linked some great general resources that I’ve come across for each of these fields below:

**Concept Art**

* [Feng Zhu Design School](https://www.youtube.com/channel/UCbdyjrrJAjDIACjCsjAGFAA) (Over 90 hour long concept art tutorials)
* [Tyler Edlin Art](https://www.youtube.com/channel/UCm9pCim4dDN4KJZUILGizgA) (Great BST art community with feedback from pros on monthly challenges)
* [Art Cafe](https://www.youtube.com/channel/UCyGGrJ-wQlvcWujLKHzB42w) (Interviews and Workshops with Famous Concept Artists)
* [Trent Kaniuga](https://www.youtube.com/channel/UCmRm1xtLIpBhuWjTyD411pA) (Illustrator and 2D artist who’s also making his own game)

**3D Modelling**

* [CG Cookie](https://cgcookie.com/course/mesh-modeling-bootcamp/?utm_source=youtube&utm_medium=social&utm_campaign=course&utm_term=description&utm_content=modeling-bootcamp-lessons) (Best Mesh Modeling Basics in Blender Ever, they’ve loads of other excellent content for blender)
* [Tor Frick](https://www.youtube.com/channel/UCDmOobbSOonY66M6fsJO7GQ) (Hard Surface Modelers & Sculptors in Blender)
* [Gleb Alexandrov](https://www.youtube.com/channel/UCVA3cYOgsTN4hs3v7pjne7w) (Short powerful rendering tutorials in Blender)

**Game Design**

* [DoubleFine Amnesia Fortnight](https://www.youtube.com/watch?v=juJikoClDxw&list=PLIhLvue17Sd7riA8vb8h1kP3jCFS_qtTM) (GameDevs who do a 2 week hackathon and record their entire design process)
* [GameMakers Toolkit](https://www.youtube.com/channel/UCqJ-Xo29CKyLTjn6z2XwYAw) (Examines Game Design Principles)

**Programming**

* [Handmade Hero](https://www.youtube.com/channel/UCaTznQhurW5AaiYPbhEA-KA) (Writing a game and engine from scratch in C)
* [Jonathan Blow](https://www.youtube.com/channel/UCCuoqzrsHlwv1YyPKLuMDUQ) (Indie dev who livestreams his game development)
* [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) (Nice Unity Tutorials)

### Conclusion

Hope you guys liked this tutorial! I do a bit of graphic design work as well as game and UI prototypes so check out [**my portfolio**](http://hugodolan.com/portfolio)! I’m also on **linked in**.

[**Portfolio**](https://hugodolandesigns.portfoliobox.net) | [**LinkedIn**](https://www.linkedin.com/in/hugo-dolan-62971a174/)

![Image](https://cdn-media-1.freecodecamp.org/images/NwkVR7XrAVlrJUTy9x0Cc30JmbmpAayM69HK)
_[http://eepurl.com/gkV7ov](http://eepurl.com/gkV7ov)_

