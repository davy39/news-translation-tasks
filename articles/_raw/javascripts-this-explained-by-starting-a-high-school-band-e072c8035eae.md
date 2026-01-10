---
title: JavaScript’s “this” Explained By Starting A High School Band
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-12T02:59:10.000Z'
originalURL: https://freecodecamp.org/news/javascripts-this-explained-by-starting-a-high-school-band-e072c8035eae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sQcxkf5QH-TA29tcMGDHGA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever been in a band, had a friend that started a band, or seen a corny
  80s movie about starting a band, then you can understand the concept of “this” in
  JavaScript.

  When you are reading over some JavaScript, and you com...'
---

By Kevin Kononenko

If you have ever been in a band, had a friend that started a band, or seen a corny 80s movie about starting a band, then you can understand the concept of “this” in JavaScript.

When you are reading over some JavaScript, and you come across the _this_ keyword, the steps you need to take in order to figure out its value might seem obvious.

You might be thinking, “I just need to find the function that contains _this_, and then I will know what it is referring to!”

```
let band= {  name: "myBand",  playGig:function() {    console.log("Please welcome to the stage" + this.name);  }}
```

In the example above, for example, _this.name_ refers to the name “myBand”. This seems easy!

But, as you learn more JavaScript concepts, like closures and callbacks, you will quickly find that _this_ does not behave like you would expect.

So, I wanted to create a visual explanation of how _this_ works in JavaScript. Here’s the scenario: You are back in high school, and starting a band with your friends (or maybe you are currently in high school?)

* Your band has four members
* You play three types of gigs: you play at bars, school competitions, and public events in town.
* Your team can play all types of music, so you try to choose the right songs to match the audience. You don’t want curse words or sexual references at the family-friendly events, for example.

As you will soon see, the biggest concept you need to understand with _this_ is **execution context.** That is what determines the value of _this_.

Before you use this tutorial, you need to understand [objects](https://blog.codeanalogies.com/2017/04/29/javascript-arrays-and-objects-are-just-like-books-and-newspapers/) and [variables](https://blog.codeanalogies.com/2017/12/20/a-visual-guide-to-understanding-the-sign-in-javascript/). Check out my tutorials on each of these subjects if you need to review.

If you are interested in a more technical version of this tutorial, check out the [guide from JavaScriptIsSexy](http://javascriptissexy.com/understand-javascripts-this-with-clarity-and-master-it/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*vkmneQ0bjkfUKE4A.)

### The Global Execution Context

Let’s say that your band needs to do a family-friendly gig at the local park as part of a local fair. You need to choose the right type of music that will keep parents happy and also not offend anyone else.

Let’s say that you choose to play some songs by [Billy Joel](https://en.wikipedia.org/wiki/Billy_Joel) (a famous American artist), and even though this is not your favorite, you know that it’s what you need to do to get paid.

Here is what that looks like in code.

```
//The songs you will play var artist= "Billy Joel"; 
```

```
function playGig(){   //instruments that your band will use   let instruments= ["piano", "microphone", "acousticGuitar", "harmonica"]; 
```

```
  console.log("We are going to be playing music from " + this.artist + "tonight!"); } 
```

```
playGig();
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*nDmTsWSyhway3yRK.)

In the example above, we have an artist **variable** that indicates what type of music we will be playing. And we have an array full of _instruments_ that will be used to play that music within the playGig **function**.

In the last line, we call the playGig function. So what is _this.artist_, in this case?

Well, first we must determine the **execution context** for this function. The execution context is determined by the **object that the function is called upon**.

In this case, there is no object listed, so that means that the function is called on the _window_ object. It could also be called like this:

```
window.playGig(); "We are going to be playing music from Billy Joel tonight!"
```

This is the global **execution context**. The function is called at the level of the global object, _window_. And, the variable _artist_ is available as a property of the _window_ object ([see this note on the JavaScript specification](https://stackoverflow.com/questions/19855823/are-global-variables-just-properties-on-the-window-object)).

So, in line 1 of the snippet above, we are also saying:

```
//old version- let artist = "Billy Joel"; this.artist="Billy Joel";
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*pR8LAtC76p1kvE5s.)

Your band is executing the gig on the global context by playing music that appeals to everyone (unless there are any Billy Joel haters out there).

![Image](https://cdn-media-1.freecodecamp.org/images/0*19QcrhPgf38OU00_.)

### Object-Level Execution Context

Let’s say that your band got a gig at a local bar. This is great! Now, you don’t need to play music that satisfies everyone in town. You only need to play music that people can dance to.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_djQrnI4NQ5nDzD2.)

Let’s say that you choose [Coldplay](https://en.wikipedia.org/wiki/Coldplay), since most of their recent songs are pop music. You need a piano, microphone, drum set, and guitar for this gig.

Let’s create a bar object with the same pattern as we created for the public park gig.

```
//The songs you will play in the public park/fair var artist= "Billy Joel"; 
```

```
function playGig(){   //instruments that your band will use   let instruments= ["piano", "microphone", "acousticGuitar", "harmonica"];   console.log("We are going to be playing music from " + this.artist + "tonight!"); } 
```

```
//NEW PART let bar = {  artist:"coldplay",  playGig: function(){     //instruments that your band will use     let instruments= ["piano", "microphone", "guitar", "drumset"];         console.log("We are going to be playing music from " + this.artist + "tonight!");    } }
```

Here is the diagram for the code above:

![Image](https://cdn-media-1.freecodecamp.org/images/0*hfc66VpcvHZZueNz.)

So, let’s say that we want to write the code to get the gig at the bar started. We need to watch our **execution context**, which is the _bar_ object in this case. Here is what that would look like:

```
bar.playGig(); //"We are going to be playing music from coldplay tonight!"
```

And, we can still execute the playGig function on a global level — but we will get a different output. This is great news, since we do not want to be playing Billy Joel or Coldplay at the wrong venue…

```
playGig(); //"We are going to be playing music from Billy Joel tonight!"
```

So far, this has been the easy stuff. Whenever we have been calling a function, the object that provides the **execution context** has been pretty straightforward. But that is about to change as we get more complex.

![Image](https://cdn-media-1.freecodecamp.org/images/0*F1hheXRD2SSTmszz.)

### Changing Execution Context using jQuery

It’s the big event that has been covered in every single movie from the 1980s: The Battle of The Bands! Yes, every band in your high school is going to get into a competition to see who is the best.

You are going to play some songs from [AC/DC](https://en.wikipedia.org/wiki/AC/DC), pretty much the coolest band on the planet. But in order to do that, you need a different instrument mix than before:

* A microphone
* An electric guitar
* A bass guitar
* A drumset

Let’s call this the battle **object**. Here is what it looks like in code.

```
let battle = {  artist:"acdc",  playGig: function(){     //instruments that your band will use     let instruments= ["microphone", "electricguitar", "bass", "drumset"]; 
```

```
    console.log("We are going to be playing music from " + this.artist + "tonight!");   } }
```

Since this is an annual event, we are going to use a click **event** from jQuery to start your show. Here is what that looks like:

```
$('#annualBattle').click(battle.playGig);
```

But if you actually ran this code… it would not work. Your band would forget the words and the notes, then slowly walk off the stage.

To figure out why, let’s return to execution context. We are referencing a DOM element called _#annualBattle_, so let’s see where that fits within the _window_ object.

Since _#annualBattle_ is an element in the DOM, it is part of the _document_ object within the _window_ object. It doesn’t have any property called _artist_. So if you ran the code, you would get:

```
$('#annualBattle').click(battle.playGig); //"We are going to be playing music from undefined tonight!"
```

In this case, the **execution context** is an element from the DOM. That is what kicked off the click() method, which used the playGig function as a **callback**. So, _this_ will end up with an undefined value.

In our analogy, this means that your band showed up to the competition with all their instruments, got in position to play, and then stared at the crowd like it was going to tell them what to do. It means you have forgotten the context of why you were there in the first place.

To solve this, we need to use the [bind() method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) to make sure that the playGig method still references the _battle_ object, even when we call it from the context of a different object! It looks like this:

```
$('#annualBattle').click(battle.playGig.bind(battle)); //"We are going to be playing music from acdc tonight!"
```

Now, we get the correct output, even though the context was a DOM element.

### Pulling A Function Out of Context

Let’s say that we wanted to write the code that will allow us to practice for the Battle of the Bands event. We will create a separate variable called _practice_, and assign the playGig **method** from the _battle_ object.

```
var artist= "Billy Joel"; 
```

```
function playGig(){  //instruments that your band will use   let instruments= ["piano", "microphone", "acousticGuitar", "harmonica"]; 
```

```
  console.log("We are going to be playing music from " + this.artist + "tonight!"); } 
```

```
let battle = {  artist:"acdc",   playGig: function(){     //instruments that your band will use     let instruments= ["microphone", "electricguitar", "bass", "drumset"]; 
```

```
    console.log("We are going to be playing music from " + this.artist + "tonight!");   } } 
```

```
let practice = battle.playGig; //run a practice practice();
```

So you are probably wondering: what is the execution context of the last line?

Well, this will run into a similar problem as the previous example. When we create the _practice_ variable, we are now storing an instance of the playGig method in the **global context**! It is no longer in the context of the battle object.

![Image](https://cdn-media-1.freecodecamp.org/images/0*nsh11uuf9M7miGMI.)

If we ran the code above, we would get:

```
practice(); 
```

```
//"We are going to be playing music from Billy Joel tonight!"
```

Not what we want. We are trying to practice AC/DC, and instead practicing Billy Joel. Yikes.

Instead, we need to use the bind() method just like above. This will allow us to bind the context of the _battle_ object.

```
let practice = battle.playGig.bind(battle); 
```

```
practice(); //"We are going to be playing music from AC/DC tonight!"
```

### How Anonymous Functions Affect Context

Let’s say that your gig is coming to a close, and you want to give a shoutout to everyone in your band so that the crowd can give each person a round of applause.

In order to do this, we are going to use the forEach() method to iterate through each element in the value of the _instruments_ property. (You will see why we changed it from a variable to a property in a moment). It will look like this:

```
let battle = {  artist:"acdc",
```

```
  //instruments that your band will use  instruments: ["microphone", "electricguitar", "bass", "drumset"],
```

```
  shoutout: function(){ 
```

```
    this.instruments.forEach(function(instrument){      console.log("Give a shoutout to my friend for covering the " + instrument + " from " + this.artist + "!");     }   } } 
```

```
battle.shoutout();
```

But yet again, if we ran this code, it would not work.

It all centers around the line where we declare an anonymous function to use on each element in _instruments_. When this function is executed, the first _this_ will retain the correct context: the _battle_ object.

But, when we arrive at _this.artist_ in the console.log statement, we will get… “Billy Joel”. This is because of the anonymous function that is used as a callback in the forEach() method. It resets the scope to the global scope.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BACZfoonzMUUwpfNzi9jIw.png)

In this case, that means we would claim at the end to be playing Billy Joel… d’oh!

But here’s what we can do. We can create a new variable called _that_ to store _this_ in the correct context. Then, when we reference the artist that we played in this specific gig, we can reference the stored context, rather than being forced to return to global context.

```
let battle = {  artist:"acdc",  //instruments that your band will use   instruments: ["microphone", "electricguitar", "bass", "drumset"],   shoutout: function(){
```

```
    //store context of this     let that = this;
```

```
    this.instruments.forEach(function(instrument){      console.log("Give a shoutout to my friend for covering the " + instrument + " from " + that.artist + "!");    }   } }
```

```
battle.shoutout();
```

### Get The Latest Tutorials

Did you enjoy this tutorial? If you did, give it a clap or sign up for the latest visual tutorials from CodeAnalogies here:

