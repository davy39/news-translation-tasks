---
title: 'From Zero to Game Designer: how to start building video games even if you
  don’t have any experience'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-10T20:06:23.000Z'
originalURL: https://freecodecamp.org/news/from-zero-to-game-designer-how-to-start-building-video-games-even-if-you-dont-have-any-experience-5e2f9f45f4bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ceUs59K42Htx2517TdSvQg.png
tags:
- name: Design
  slug: design
- name: gaming
  slug: gaming
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Angela He

  2 years ago I was just 17 year old high school student who knew nothing about coding.
  But I pushed forward anyway, and within a few months I published my first game on
  Steam.

  Now, I’ve made over 10 games for desktop, web, and mobile, wit...'
---

By Angela He

2 years ago I was just 17 year old high school student who knew nothing about coding. But I pushed forward anyway, and within a few months I published my first game on Steam.

Now, I’ve made over [10 games for desktop, web, and mobile](https://zephyo.itch.io/), with over 1.9 million plays combined.

No matter your skill level, you can make a game too. 2 years ago, I thought it was impossible, but tried anyways. It was the hardest thing I’d ever done. But it was worth it. Now, I realize game development is like any skill — you only get better by doing, failing, then improving.

I taught myself everything I know. And now I’m going to teach you.

### To make a game, you must go through the 6 stages of game development: Design. Art. Code. Audio. Polish. Market.

The rest of my post will structure each stage into the following:

* ?A**dvice I**’ve curated from my and others’ experiences.
* ?R**esources** I’ve found most helpful.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VZbUqT8oEH34kK0XXBcwzg.png)

### 1. Design ?

#### Advice?

You’ve got a great idea. *

But how do you capture it in writing?

Everyone’ll have their own way of doing that best. Some compose 60-page design documents. Others, like me, write a page of badly-written notes, unreadable to anyone else. I don’t know what’s best for you. **But I can give suggestions on _what to write about_:**

* **Hook.** _What makes your game idea great?_ For me, this is the most important to write down. Once you capture this, you can write down the next three points much easier. Is your game about something thought-provoking? Scandalous? Is it putting a new twist to an old classic? Or, is it doing something that’s never been done before?
* **Mechanics.** _What does your player do? And for what purpose?_ This is your gameplay. It can be as simple as pressing QWOP to move in the game QWOP, to tapping buttons to chat in Mystic Messenger, to the tons of key combos in Dwarf Fortress.
* **Story.** _What story should players remember your game by? What emotions should they leave your game with?_ Every game has a story. If the story isn’t obvious, it is created by the player. A story can be created from the increasing numbers in 2048, the rising empires in Civilization, and the silent interactions in Monument Valley. Think about what story’ll be found in your game.
* **Mood.** _What impression does your game make? What are the visuals? Sound?_ First impressions matter. First impressions will hook — then keep — the player playing. Perhaps, you’ll give your game a retro vibe with [pixel graphics and chiptune music](https://www.youtube.com/watch?v=1Hojv0m3TqA). Or, a modern, clean look with [flat geometries and instrumentals](https://www.youtube.com/watch?v=GatTHt8SUiA).

![Image](https://cdn-media-1.freecodecamp.org/images/0*Zm7Qnuq-zJcdKP6d.gif)

*** Having a hard time thinking of an idea?** Creative block hits us all.

* _Join a game hackathon/jam._ You and other participants’ll be tasked to make a game in a short amount of time. Throughout, and after, you’ll be met with support from other jammers. And the excitement and creativity during a jam? Infectious. Don’t know where to get started? [Try Ludum Dare](https://ldjam.com/), one of the largest game jams.
* _Keep a list of ideas._ I and other developers I know jot down our ideas. That way, we can refer back to our old ones when we run out of new.

When the muse hits, stop whatever you’re doing. Write that idea down. The next time creativity ghosts, you won’t be left grasping for straws.

#### Resources ?

All of the below are tried and true. (?) means I use it currently.

**Note-taking:**

* Notes for Mac (?)
* Google Docs (?)
* Trello

**Collaboration (for teams):**

* Google Drive
* GitHub (?). R_equires git and Unity .gitignore._
* Unity Collab. _Easiest out of the three. The free version has limitations._

Heads up — Unity is the game engine I use to make games, so I’ll be mentioning it throughout. Feel free to use a different engine.

**Game design:**

* [The Art of Game Design by Jesse Schell](https://www.google.com/search?q=jesse+schell+book+of+lenses&oq=jesse+schell+book&aqs=chrome.0.0j69i57j0l2.3902j0j1&sourceid=chrome&ie=UTF-8)
* [Gamasutra](https://www.gamasutra.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gThJElasWJawt867DTcr2w.png)

### 2. Art ?

#### Advice?

You’ve planned out your idea; congrats, that’s amazing! Now, you can work on the actual game.

_(**If you don’t know how to code**, I suggest doing stage 3, Code, before Art. You don’t want to create art that you’ll trash later because you can’t code it in.)_

> **_Don’t know how to draw?_** _Do not fret. Anyone can make something beautiful with the [3 basic visual principles](https://en.wikipedia.org/wiki/Visual_design_elements_and_principles): color, shape, space._

![Image](https://cdn-media-1.freecodecamp.org/images/0*E0eirD4x5D_CejDi.)
_Thomas Was Alone — a beautiful yet simple game_

#### **UI**

Think about how you can make it **_unique_** — have a distinct color scheme, font(s), shape(s), and icon(s) — while **_functional_**. Is the important information readable and obvious? Do the colors/fonts/icons distract from that at all?

![Image](https://cdn-media-1.freecodecamp.org/images/1*7oMigOwvb5hZw8oNYc4yEA.png)
_Who would win? ?_

#### **2D animations**

You have two options:

* **_Frame-by-frame._** Draw out each frame of the animation. For this, you should use sprite sheets with [TexturePacker](https://www.codeandweb.com/texturepacker) (or if you’re using Unity, [Sprite Packer](https://docs.unity3d.com/Manual/SpritePacker.html)).
* **_Bone-based._** Draw each animated limb, then animate the limb’s position, rotation, and whatnot in-game. Can be faster, easier, and save memory. If you’re doing 2D and using Unity, try editing the pivots of sprites or [Anima2D](https://assetstore.unity.com/packages/essentials/unity-anima2d-79840).

![Image](https://cdn-media-1.freecodecamp.org/images/0*hIZxk2xfmyTYCL38.)

#### **Misc**

Here are some general miscellaneous art tips that apply to not only art in games, but in other software as well.

* **_Tile_** patterned assets to create tiled images and save memory.

![Image](https://cdn-media-1.freecodecamp.org/images/0*kJidu4j0jdoKiSak.png)
_Untiled to tiled_

* **_9-patch/9-slice_** assets with unscalable borders but a scalable center to create scalable images and save memory.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2JhJt6iStsR1P8hy.png)
_?The blue ditto grows, but its corners stay the same!_

* Make the dimensions of each asset [a multiple of 4](https://www.gamasutra.com/blogs/RobertBasler/20180202/313739/DXT_Texture_Compression_in_2018.php) or [a power of 2](https://docs.unity3d.com/Manual/HOWTO-ArtAssetBestPracticeGuide.html) to save memory. Which one depends on how you’re compressing the assets.
* If you’re using Photoshop, use “File > Export > Layers to Files” to quickly export each layer as a file (e.g. PNG, JPEG).

#### Resources ?

**Creating UI:**

* Photoshop (?).
* Sketch.

**UI principles:**

* [Google Material Design](https://material.io/design/) (?).
* [Apple’s UI Do’s and Don’ts](https://developer.apple.com/design/tips/).

**Creating 2D assets:**

* Photoshop (?).
* Gimp.
* Paint Tool SAI. _Good for smooth/anime styles._

**Creating 3D assets:**

* Blender (?). P_owerful but steep learning curve._
* Maya. _Good for animation._
* Max. _Good for rendering._

**Free assets:**

* [Behance](https://www.behance.net/) (?). F_onts + icons + other designs._
* [KennyNL](https://kenney.nl/). _HQ, game-ready UI/2D/3D art._
* [Open Game Dev Art](https://opengameart.org/). _Large library of user-generated art._

**Inspiration:**

* [Dribbble.](https://dribbble.com/) _Designs from invite-only designers._
* [Behance](https://www.behance.net/) (?). D_esigns from anyone with an account._
* [itch.io](http://itch.io/) (?). B_eautiful indie games._

![Image](https://cdn-media-1.freecodecamp.org/images/1*TMF40Hb52oFS-GlvLRs4Gg.gif)

### 3. Code ?

#### Advice?

```
Debug.Log(“Oh boy! Time to code!! ^_^”);
```

**Your first step?** Decide on a **game engine** and an **IDE** (Integrated Development Environment — basically, an app that lets you code). My recommended game engines+IDEs are in Resources below.

**Your second step?** Code.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PMyxT_fjoTaVsDcs.gif)

**Don’t know how to code?** No worries. I got you. You can learn.

These CS fundamentals should be enough to start. (All code examples here are in C++, one of the main languages the Unity 3D game development framework uses.)

**1) Data types and variables.** At the root of all code is data. That data is stored in variables. You can declare a variable like this:

```cpp
int i = 0;
```

Let’s break that down.

`int` is the data type. `i` is the variable name. And that `= 0` assigns zero as the variable value.

So what’s this?

```cpp
string s = "pusheen is best cat";
```

`string` is the data type. `s` is the variable name. And yep — you guessed it — `“pusheen is best cat”` is the variable value.

Some common data types: `int` and `long` are `integers`. `float` and `double` are decimal numbers. And string is any sentence. (Even an empty one — `“”`!)

Want to know more? Go through [this](https://lifehacker.com/5736011/learn-how-to-code-part-i-variables-and-basic-data-types) and [this](https://lifehacker.com/5742493/learn-to-code-part-ii-working-with-variables).

**2) If statements.** If statements evaluate if a certain condition is true. If it is, run the code that’s inside the `if` statement:

```
if (true){ //true is always true!

    doThings(); //I'm inside the if statement's brackets; run me!
}
```

If the condition isn’t true, we can evaluate other conditions with `else if`:

```cpp
int i = 1;

if (i == 0){ 

   doThings(); 
}
else if (i == 1){

   doOtherThings(); //I'm gonna be run!
   
}
```

Or, just run some other code with `else`:

```cpp
int i = 60000;

if (i == 0){

  doThings(); 
  
} else {

  doOtherThings(); //I'm still gonna be run.
  
}
```

**3) For/while loops.** While loops continue while a certain condition is still true, executing the same lines of code over and over again. When the condition is false, the while loop exits.

```cpp
while (someBool == true){ //condition

   doThings(); //We'll keep doing things until someBool is false
   
}
```

Think: how long does this while loop last?

```cpp
while (true){

  doThings();
  
}
```

For loops are basically while loops where:

```cpp
int i = 0;
while (i < condition){ 

    doThings();
    
    i++; //increment after doing things
}
```

That’s equivalent to:

```cpp
for (int i = 0; i < condition; i++){

    doThings();
}
```

**4) Basic data structures.** So, we have data, and we ways to evaluate and manipulate that data. We can also store that data into some structure — a data structure. Data structures you should know are [arrays](https://www.geeksforgeeks.org/introduction-to-arrays/), [lists](https://www.geeksforgeeks.org/linked-list-set-1-introduction/), [queues](https://www.geeksforgeeks.org/queue-data-structure/), [stacks](https://www.geeksforgeeks.org/stack-data-structure/), and [sets](https://www.geeksforgeeks.org/hashing-set-1-introduction/).

Here’s a quick example of an array:

```cpp
/*
Say you have numbers 0 through 9 that you want to store somewhere. You can store it in an array!
*/
int[] arr = new int[10]; 
/*
The [] brackets declare an array. We assign a new array to arr of size 10 - that means it can hold 10 elements. Arr now looks like this:

arr = [ 0 0 0 0 0 0 0 0 0 0 ]
*/
for (int i=0; i<10; i++){

    arr[i]=i; //We assign whatever i is to the the ith index of arr.
    
//Did you know data structures' indices start at 0? ? 
}

/*
After the for loop, our array data structure should look like this!
arr = [ 0 1 2 3 4 5 6 7 8 9 ]
*/
```

To solidify your knowledge of 2–4, go through [this](https://lifehacker.com/5742494/learn-to-code-part-iii-arrays-and-logic-statements).

**5) Functions and exceptions.** Functions are basically a small line of code describing a big bunch of code. For example, if you call:

```cpp
EatBread();
```

And EatBread() looks like:

```cpp
void EatBread(){ //<---this is a function. 

   breadAte=true;
   
   printf("I CAN FEEL THE CARBS COURSING THROUGH MY BODY");
   
}
```

Then the call to `EatBread()` is actually a call to the two statements within the `EatBread()` function.

If you do something bad in your code, an exception might get thrown. They’re angry red errors there to tell you, hey, back up, what you did right there just ain’t ‘workin out logically. Go revise it.

To learn more about functions, [go here](https://lifehacker.com/5742495/learn-to-code-part-iv-understanding-functions-and-making-a-guessing-game); for exceptions, [go here.](http://www.tutorialspoint.com/java/java_exceptions.htm)

Then, there’re other things you should know:

**6) Language.** What language are you going to code in? C++? Javascript? C#? Every language is written somewhat differently and can let you do different things.

**7) API (Application Programming Interface).** Once you know the basics, you’ll have to learn the specific API of your game engine. APIs are essentially a bunch of powerful tools wrapped in simple classes and functions that you can call. APIs make life easier. Way easier.

Lastly:

**8) Look at an example project in your chosen game engine.** [Unreal](https://docs.unrealengine.com/en-us/Resources) and [Unity](https://unity3d.com/learn/resources/downloads) both have a ton of free example projects. This’ll let you discover how everything comes together. Plus, you can build your game idea off of the project. (I built my first game off of [Corgi Engine](http://corgi-engine.moremountains.com/).)

```cpp
if (you.getThisFar()==true){
  veryProud=true;
  you.didIt(); //CURRENT MOOD: THE SH⭐⭐KEST ???
  
}
```

**A word of encouragement:** I know. Coding is scary at first. Nothing makes sense, you’re hitting constant roadblocks, and you might want to quit in the face of failures and exceptions. It doesn’t mean you’re bad at coding. Coding is challenging. It’s understandable to feel incompetent at first.

But it just takes time, like any other skill. It’ll get easier. And it’ll get fun (at least, it did for me).

![Image](https://cdn-media-1.freecodecamp.org/images/0*276fFujnYO2MY-5j.gif)

**Important game programming concepts:**

* [_Object orientation._](https://en.wikipedia.org/wiki/Object-oriented_programming) Makes programming feel more natural.
* [_Naming conventions._](https://stackoverflow.com/questions/421965/anyone-else-find-naming-classes-and-methods-one-of-the-most-difficult-parts-in-p) Name your classes, methods, and variables as something that obviously conveys its purpose. For instance, a melee attack function should be named meleeAttack(), not mA() or protecbutalsoattac(). You (and others who read your code) should know what’s going on.
* [_Decomposition._](https://cs.stanford.edu/people/nick/compdocs/Decomposition_and_Style.pdf) Put code that repeats itself into a separate function. Call that function instead of duplicating the repeatable code.
* [_Singleton design pattern._](http://gameprogrammingpatterns.com/singleton.html) Allows data that a lot of things need to be stored in one place.
* _Static avoidance._ Beyond singletons, I’d avoid making static variables— their lifetime is the game’s lifetime, [they’re slower,](https://jacksondunstan.com/articles/1713) and they can have unexpected behaviors in the editor.
* [_Observer design pattern_](http://gameprogrammingpatterns.com/observer.html)_._ Allows things that must happen depending on another thing to not waste the computer’s time checking that other thing.

**Important Unity-specific things:**

* [_Coroutines._](https://docs.unity3d.com/ScriptReference/MonoBehaviour.StartCoroutine.html) IEnumerators and Coroutines allow you to start doing things, continue doing things until some time has passed, then stop. I use them _all the time:_ for bursts of visual effects; for lerping movement; for waiting for a scene to load before grabbing the scene’s objects.
* [_ScriptableObject._](https://unity3d.com/learn/tutorials/modules/beginner/live-training-archive/scriptable-objects) These contain data with less overhead than MonoBehaviors.

#### Resources ?

**Game engines:**

* Make your own. _Requires C/C++. Low level. Really, really low._
* [Unity](https://t.umblr.com/redirect?z=http%3A%2F%2Funity.com&t=YTA4MGJkNmI1N2Q5MTUxODI4ZWNkOGEwZGVhMjA3ZDNiZmQ1ODJlYyxxRDFMV0V3eA%3D%3D&b=t%3AlfGQjHHkXZBrPEtOysXejA&p=http%3A%2F%2Fzephyo.tumblr.com%2Fpost%2F166397059953%2Fhello-first-off-i-want-to-say-that-i-really-love&m=1) (?). 2_D/3D. Requires Javascript/C#. Mid-level. Cross-platform._
* [Unreal Engine](https://t.umblr.com/redirect?z=https%3A%2F%2Fwww.unrealengine.com&t=NjMyOGZkMjcyNDA3ZmUwN2JhNGI4NzA1MTFlOTNkMWRiZWM4MTMxMSxxRDFMV0V3eA%3D%3D&b=t%3AlfGQjHHkXZBrPEtOysXejA&p=http%3A%2F%2Fzephyo.tumblr.com%2Fpost%2F166397059953%2Fhello-first-off-i-want-to-say-that-i-really-love&m=1). _2D/3D. Requires C++. Mid-level. Cross-platform. Notes: 2D support is not great._
* [pixi.js](http://www.pixijs.com/) (?). _2D. Requires Javascript. Mid-level. Web._
* [GameMaker Studio](https://t.umblr.com/redirect?z=https%3A%2F%2Fwww.yoyogames.com%2Fgamemaker&t=ODE1NjZlZGViNGRlZjAyNjIwODhkNWNmYThmNmJhMDI2N2FlM2ZmYyxxRDFMV0V3eA%3D%3D&b=t%3AlfGQjHHkXZBrPEtOysXejA&p=http%3A%2F%2Fzephyo.tumblr.com%2Fpost%2F166397059953%2Fhello-first-off-i-want-to-say-that-i-really-love&m=1). _2D/3D. Requires GML. Beginner level. Cross-platform._
* [Corona](https://coronalabs.com/). _2D. Requires Lua. Beginner level. Cross-platform._

**IDEs:**

* Visual Studio Code (?). F_or MacOS. Gives me no lag and has awesome, VSCode-exclusive features (such as inline reference info, quick navigation (⌘T))._
* Visual Studio (?). F_or Windows._
* MonoDevelop. _Comes with Unity. Tends to lag._

**Free Unity assets:**

For Unity, tons of free assets exist on the Unity Asset Store, GitHub, bitbucket, and other sites. I use at least 2 in every project. Make your life easier with assets, but realize they’re not perfect. If you spot mistakes, don’t hesitate to fix them and/or ping the developers.

* [TextMeshPro](https://www.assetstore.unity3d.com/en/?stay#!/content/84126) (?).
* [LeanTween](https://www.assetstore.unity3d.com/en/?stay#!/content/3595) (?).
* [Fungus](https://assetstore.unity.com/packages/templates/systems/fungus-34184).
* [Corgi Engine.](http://corgi-engine.moremountains.com/)
* [Dialogue System](http://www.pixelcrushers.com/dialogue-system/).
* [Post Processing Stack.](https://assetstore.unity.com/packages/essentials/post-processing-stack-83912)
* [Keijiro Takahashi.](https://github.com/keijiro) _Works at Unity. Has_ amazing _open source Unity visual effects projects!_

> Last but not least, my #1 solution for coding problems: Google!

![Image](https://cdn-media-1.freecodecamp.org/images/0*NI1eGAQJ23f8EBOI.jpg)

### 4. Audio ?

#### Advice?

First: **Do you want audio?**

Audio can do [_wonders_ for immersion and mood](https://dl.acm.org/citation.cfm?id=2146327). But, it can cost memory.

If the answer’s yes, what audio?

Will you include **music**? **Sound effects**? **Voiceovers** or **narration**?

For any of the above, record and mix them in a way that matches your game’s **mood**. For example, Bastion uses organic mouth and instrument sounds, matching its game world. Crypt of the Necrodancer uses a blend of electronic beats and chiptune rock to match the colorful, rhythmic game.

> “Immersion is king.”  
>   
> [-Darren Korb, Supergiant Games](http://twvideo01.ubm-us.net/o1/vault/gdc2012/slides/Audio%20Track/KORB_DARREN_BUILD%20THAT%20WALL.pdf)

If your audio doesn’t match your game’s **mood,** it could detract from immersion. How will _your_ audio match your game?

#### Resources ?

**Audio tools:**

* Logic Pro. _$200. MacOS only._
* FL Studio (?). $_99–899. Has free demo._
* Reaper. _$60–225._
* Audacity (?). F_ree. Limited capabilities. Useful for cleaning audio._

**Retro sound effect generators:**

* [Chiptone](http://sfbgames.com/chiptone/).
* [Bfxr](https://www.bfxr.net/).
* [Leshy SFMaker](https://www.leshylabs.com/apps/sfMaker/).
* [as3sfxr](http://www.superflashbros.net/as3sfxr/).

**Free sounds:**

* [Soundcloud](http://soundcloud.com/) (?). S_oundcloud has a t_on o_f gorgeous gems under Creative Commons (CC). H[ere’s a playlist to get started.](https://soundcloud.com/tilohensel/sets/creative-commons-music) Make sure to provide attribution if needed._
* [Incompetech](https://incompetech.com/music/) (?). C_C music. Must attribute._
* [Bensound](https://www.bensound.com/royalty-free-music). _CC music. Must attribute._

![Image](https://cdn-media-1.freecodecamp.org/images/1*JKnp8SVLbSaIyBtj8wyehw.gif)

### 5. Polish ?

#### Advice?

Hey! You’re here! You made it; that’s **_absolutely incredible_** (I’m serious, if you get this far, I’d love to hear about your game; hit me up)!

You’re done.. right?

Well. There’s a 99.99999% chance there’re bugs.

It’s time to bug test.

![Image](https://cdn-media-1.freecodecamp.org/images/0*hAs_R5zvpdfkKKiV.gif)

#### **Bug testing your game**

1. _Get others — not you — to play it._ Preferably in front of you, because if they encounter a bug, they might not realize or have a hard time describing it.
2. _Play it on all targeted platforms._ It may work in the editor, but does it work where it matters? For Linux and the different versions of Android especially, I find that things get a little wonky.

Alright. **You’ve found a bug. What now?**

![Image](https://cdn-media-1.freecodecamp.org/images/0*GFIXUr8X6BwoXdgb.jpg)

1. _Check the console for exceptions._ Found one? Great! Find the file and line number where the exception was thrown. If the exception sounds like something from Mars, Google it and learn about it. Then figure out why that line number is throwing that exception.
2. _Still can’t figure it out? Write to console._ Start tossing in them log statements in the place(s) you think is causing you trouble. Print variable values, and see whether what’s printed is what’s expected. If not, fix that.
3. _When worse comes to worse, check logs._ The logs of your project will give you way more info than the console. Read the last lines where the exception occurred. Google anything you don’t know. Can you fix it now?
4. _Sleep._ It’ll get fixed in the morning. This is just a bad dream. Right? ?

#### **Common errors**

* _NullReferenceException._

```cpp
var.doThing(); //throws NullReferenceException: Object reference not set to an instance of an object
```

_Problem:_ You’re doing a thing on a **null** (nonexistent) variable.

_Quick fix:_ Check if the variable is null before doing the thing.

```cpp
if(var != null)
    {
        var.doThing(); // do the thing safely!
    }
```

* _SyntaxErrorException._

_Problem:_ Your code has invalid syntax.

_Quick fix:_ In the Exception message, it should tell you what character is throwing the error. Change that character.

_Note:_ If the character is a double quote, make sure you’re using dumb quotes instead of smart quotes:

```cpp
" //dumb quote
” //smart quote. I promise these'll give you trouble at some point in your life. ?
```

* Pink or black screen.

_Possible problem:_ Some shader can’t render.

_Possible causes:_ You’re using a 3D shader for a 2D game. Or, you’re using some shader feature unsupported by the target OS. Be sure to use mobile shaders for mobile games.

![Image](https://cdn-media-1.freecodecamp.org/images/0*YpNXKqqy_Nka3RYp.gif)

After you’re done debugging, **polish your game off by optimizing its memory usage and performance.** This’ll make it download faster and heat up people’s devices less.

#### **General optimization tips**

* [_Set the target frame rate._](http://resetoter.cn/UnityDoc/ScriptReference/Application-targetFrameRate.html) The frame rate could be 20 for a visual novel or 60 for a first-person shooter. A lower than default target frame rate allows the game to spend less time rendering frames.
* _Animation / [particles](https://blogs.unity3d.com/2016/12/20/unitytips-particlesystem-performance-culling/) / [occlusion culling](https://docs.unity3d.com/Manual/OcclusionCulling.html)._ Culling means that things invisible to the camera aren’t rendered. Characters’ll only animate, particles’ll only update, and 3D models will only be rendered when in view.

![Image](https://cdn-media-1.freecodecamp.org/images/0*--aqZp6ZFl7wMVWI.jpg)

![Image](https://cdn-media-1.freecodecamp.org/images/0*sOU-nKokr1HlJP3a.jpg)

* _Compress textures and audio._ [Crunch compress textures.](https://blogs.unity3d.com/2017/12/15/crunch-compression-of-etc-textures/) [Stream music and decompress sound effects on load.](https://medium.com/@hex3r_/making-your-unity-game-scream-and-shout-and-not-killing-it-in-the-process-673a7384693c) Decrease the audio quality. Note that compression may or may not decrease the quality of assets noticeably.
* [_Object pooling._](https://unity3d.com/learn/tutorials/topics/scripting/object-pooling) Avoid instantiating and destroying many objects at once to prevent huge spikes. Instead, object pool them in a List, Queue, or other data structure. Things like bullets should be object pooled.
* [_Don’t let raycasts hit things that don’t need input._](https://create.unity3d.com/Unity-UI-optimization-tips) Raycasts are like little rays that shoot from your fingers or mouse everytime you tap or click. Remove objects that don’t react to those inputs from raycast calculations.

#### **If you’re up for a challenge:**

* _Optimize shaders._ Give each renderer a material. This’ll save resources in the beginning since the game doesn’t have to create new materials for everything. Have the shader for the material only include what’s functionally needed (for example, a button that doesn’t need masking can use a Sprite shader instead).
* _In Unity, [Use AssetBundles instead of Resources.](https://blogs.unity3d.com/2017/04/12/asset-bundles-vs-resources-a-memory-showdown/)_ AssetBundles will save memory by pulling from online (e.g. dropbox) or local storage (e.g. hard disk). I haven’t tried too much due to the poor documentation, though.

#### Resources ?

All of these are from Unity but can be applicable to other engines.

**Scripts:**

* [Optimizing scripts in Unity games](https://unity3d.com/learn/tutorials/topics/performance-optimization/optimizing-scripts-unity-games) (?)

**Art:**

* [A guide to optimizing Unity UI](https://unity3d.com/learn/tutorials/topics/best-practices/guide-optimizing-unity-ui) (?)
* [Art Asset best practice guide](https://docs.unity3d.com/Manual/HOWTO-ArtAssetBestPracticeGuide.html) (?)

**Memory:**

* [Reducing the file size of your build](https://docs.unity3d.com/Manual/ReducingFilesize.html) (?)
* [Memory](https://docs.unity3d.com/Manual/BestPracticeUnderstandingPerformanceInUnity2.html)

**Platform-specific:**

* [Practical guide to optimization for mobiles](https://docs.unity3d.com/Manual/MobileOptimizationPracticalGuide.html) (?)
* [WebGL performance considerations](https://docs.unity3d.com/Manual/webgl-performance.html) (?)
* [Memory Considerations when targeting WebGL](https://docs.unity3d.com/Manual/webgl-memory.html) (?)
* [Olly’s seven stages of optimizations for mobile VR](https://unity3d.com/how-to/optimize-mobile-VR-games)

![Image](https://cdn-media-1.freecodecamp.org/images/0*0kiegwenNUvH_1CV.png)

### 6. Market ?

#### Advice?

**Congrats!** ?? You’ve made something. It’s time to show the world what you’ve made.

Personally, marketing is my most anxiety-inducing stage. If you, too, get doubtful, the **game developer community** is helpful. You’re not alone in this. And you’ve come so far — might as well get through to the end, right?

> You’ll never know if it’ll be a hit unless you try.

![Image](https://cdn-media-1.freecodecamp.org/images/0*qFXvryTQVsP8UCcn.gif)

1. **Draft.** Create drafts of your game page on all your targeted game distribution platforms. Find a list of platforms in **Resources** below.
2. **Network.** If you go the full networking mile, you’ll want to email **game press**, showcase in **festivals**, and attend **conferences**.

_With game press,_ email your unlisted game page a week before release. Give people some time to write about it. It’s likely they won’t write about it at all. I’ve found that press loves a compelling developer story, unique/controversial concept, and, most importantly, a [presskit](http://dopresskit.com/).

**How do you find emails?** You can..

1. Find writers you like and Google their name. Their email is bound to come up somewhere: Twitter, LinkedIn, etc. Or..
2. Find the magazine/new’s company-wide email on their _About_ page. It’s usually in the format of **tips@company.com.**

**Do not** email press about your game if they explicitly don’t cover your genre/targeted platform.

_Festivals_ can get you awards and/or professional recognition by other developers and press.

_Conferences_ are what you make of it: they can be all about networking with other developers, companies, and press (go get them business cards!); updating your latest game dev know-how; playing others’ games; or meeting up with internet friends.

Game conference tickets are _expensive._ If you’re a student, think about applying for scholarships for them. The [IGDA Scholars program](http://scholars.igdafoundation.org/) gives you some especially amazing networking and event opportunities.

3. **Youtubers/Streamers.** You can get video coverage of your game by:

1. _Ranking high_ on game distribution platforms.
2. _Emailing._ If you email, don’t talk about yourself; talk about the game. Keep it sweet, short, and compelling. Use eye-catching photos and gifs.

**How do you find emails?** Look at their About page. If you can’t find it there, Google them and see if their other social media have it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Y35x-rZIuBapR5WFNpFqQ.png)
_’tis an email_

![Image](https://cdn-media-1.freecodecamp.org/images/1*ISj787elwqyMUQOHo3o40g.png)
_*dances in the air*_

4. **Social media.**

Social media is an _amazing_ marketing tool. [Agar.io found its rise from 4chan](https://www.rockpapershotgun.com/2018/02/22/the-rise-and-rise-of-io-games/), [Butterfly Soup got mad boosts from Twitter](https://twitter.com/brii_u/status/909114732287627264?lang=en), and some form of social media always ends up in my top 4 referrers:

![Image](https://cdn-media-1.freecodecamp.org/images/1*9zJi8w4bKAqD4FlAmlc6DA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*XXB_AREPwK0K0ozaTaBKNg.png)
_Live Portrait Maker (left), YOU LEFT ME. (right)_

My favorite social media platforms for marketing are in **Resources** below.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Z0LdyJ-sK4zD3-iZ.gif)

**A last note** — **Publisher or self-publish?** Game marketing is a lot. Do you want a publisher to take care of all that? Want to go the Hotline Miami x Devolver Digital route, or rely on Farmville and Doki Doki Literature Club’s word-of-mouth?

With a publisher, you’ll have to do your research to find a good one. After, you’ll sign paperwork and go through legal hoops. Plus, it’s a huge financial investment.

By yourself, you’ll have to put a lot of time and effort into learning marketing. You may love it. You may hate it. And you might not do a great job of it, either. But it’s free, and you learn valuable skills.

![Image](https://cdn-media-1.freecodecamp.org/images/1*abfGrvwSMrEaha8ViVHzww.png)
_Yay organic, self-publishing growth~ (But is it non-GMO though?)_

For me, I’ll always self-publish. _I love learning new things. Also, I firmly believe that a truly great game will succeed no matter what, as long as_ some _marketing effort was put._

6. Hit that **Publish** button!

??Yooo, you D**ID i**t!! ?Now relax, sit back, grab a yummy drink, and take some time for yourself! You’ve worked so hard. You deserve it.

And remember that, even if your game doesn’t get the reception you expected, that’s ok. It’s not gonna be perfect your first time. My first game on Steam only has 255 downloads.

The facts are, you made a game. You learned so much. That’s enough.

And there’s always a next time!

![Image](https://cdn-media-1.freecodecamp.org/images/0*oSrrX_kk-L4Lwion.gif)

#### Resources ?

**Game distribution platforms:**

* [Steam](https://store.steampowered.com/) (?). P_C. Requires $100 USD fee per game._
* [Origin](https://www.origin.com/). _PC._
* [GOG](https://www.gog.com/). _PC. Free to publish. Game must get accepted._
* [Mac App Store](https://developer.apple.com/macos/distribution/). _MacOS. Requires Apple Developer account._
* [itch.io](http://itch.io/) (?). P_C/Web. Free to publish._
* [Game Jolt](http://gamejolt.com/) (?). P_C/Web. Free to publish._
* [Armor Games](http://developers.armorgames.com/) (?). F_ree to publish. Must apply to be a developer._
* [Kongregate](http://www.kongregate.com/) (?). W_eb. Free to publish._
* [Newgrounds](http://www.newgrounds.com/) (?). W_eb. Free to publish._
* [GitHub](https://github.com/) (?). W_eb. Free to publish on your own site with domain name formatted as “_**__.github.io”**._
* [Amazon.](https://developer.amazon.com/app-submission) _Web/Mobile. Free to publish._
* [Google Play](https://play.google.com/store) (?). M_obile. Requires one-time $25 USD fee._
* [iOS App Store](https://itunes.apple.com/us/genre/ios) (?). M_obile. Requires Apple Developer account._

**Game press:**

* [IndieGames.](http://indiegames.com/)
* [Siliconera.](http://www.siliconera.com/)
* [FreeGamesPlanet](https://www.freegameplanet.com/live-portrait-maker-browser-game/). _Super nice admin._
* [PCGamer.](https://www.pcgamer.com/)
* [Kotaku.](https://kotaku.com/)
* [Rock Paper Shotgun.](https://www.rockpapershotgun.com/)
* [Polygon.](https://www.polygon.com/gaming/2012/9/17/3348450/zynga-a-bit-lucky-acquisition-zynga-san-francisco-john-tobias)
* [Giant Bomb.](https://www.giantbomb.com/florence/3030-66441/similar-games/)
* [EuroGamer.](https://www.eurogamer.net/)

**Game festivals:**

* [Independent Games Festival (IGF).](http://www.igf.com/) _Deadline around October._
* [Indiecade.](https://www.indiecade.com/) _Deadline around May/June._
* [Swedish Game Awards.](https://www.gameawards.se/) _Deadline around July._
* [South by Southwest Festival (SXSW)](https://gaming.sxsw.com/awards/). _Deadline around December._
* [The Game Awards.](http://thegameawards.com/) _Deadline around November._

**Game conferences:**

* Game Developer’s Conference (GDC). _San Francisco._
* Penny Arcade Expo (PAX). _Seattle/Boston/Philadelphia/Melbourne._
* Electronic Entertainment Expo (E3). _Los Angeles._
* Tokyo Game Show. _Japan._
* Steam Dev Days. _Seattle. For Steam developers only._

**Emailing:**

* [presskit()](http://dopresskit.com/)

**Social media:**

* reddit (?). P_ick an appropriate subreddit. Some of my favorites are /r/WebGames,_ _/r/IndieGaming/, and /r/visualnovels._

![Image](https://cdn-media-1.freecodecamp.org/images/1*uXjTNgJQLRD6GxREPjLWZg.png)
_/r/WebGames._

* Facebook (?). P_ost on your Facebook Page (if you have one) and personal facebook (if you’re comfortable). There’s also tons of Facebook Groups where you can show off your game! Here’s some:_

[**GameDev Show and Test**](https://www.facebook.com/groups/GameDevShowAndTest)  
[_Welcome to GameDev Show and Test - a sister group to the Indie Game developer groups. The purpose of this group is to…_](https://www.facebook.com/groups/GameDevShowAndTest)

[**Indie Game Developers**](https://www.facebook.com/groups/IndieGameDevs/)  
[_Independent Game Developers group for small companies and individuals designing and publishing their own games. **READ…_](https://www.facebook.com/groups/IndieGameDevs/)

[**Indie Game Promo**](https://www.facebook.com/groups/IndieGamePromo/1066211690197686/)  
[_Indie Game Promo has 47,645 members. Sister group to Indie Game Dev and Indie Game Chat for the purpose of promoting…_](https://www.facebook.com/groups/IndieGamePromo/1066211690197686/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*I4pg-w5UL-nkA4IOSqndpw.png)
_Indie Game Promo._

* Tumblr (?).
* Twitter (?). T_ry using tags like #gamedev, #indiedev, and #screenshotsaturday to get discovered._

**Community:**

* [/r/gamedev](https://www.reddit.com/r/gamedev) (?).
* [Ludum Dare](https://ldjam.com/) (?).
* [Indie Game Devs](https://www.facebook.com/groups/IndieGameDevs/) (?).

### **Conclusion**

There’s no cheat code to making a game. It’s just a lot of determination and effort.

> “Behind every Half Life, Minecraft and Uncharted, there are OCEANS of blood, sweat and tears.”  
>   
> [— Ken Levine](https://medium.com/@IGLevine/so-lots-of-people-have-responded-to-my-encouragement-to-get-into-the-industry-asking-how-do-i-get-e2d0cd738733)

You’ll get confused. You’ll make mistakes. You might even cry (I did—and still do).

But that’s okay. It means you’re growing. If you‘re putting in that much effort, I believe in you and your game: **You can do it.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*IH1bpE4Hf0crXYVd.)
_supportive foxtato by Emily’s Diary_

![Image](https://cdn-media-1.freecodecamp.org/images/0*cc_Fm6yLJIZaCGRB.gif)

If you liked reading my first article, be sure to give a ?(or several — did you know you can give more than one?) It’d mean the world ?

You can also follow/DM me on [Twitter](https://twitter.com/zephybite), [Tumblr](http://zephyo.tumblr.com/), and [GitHub](https://github.com/zephyo), and [buy me a coffee](https://ko-fi.com/J3J6DIQC) if you wish.

