---
title: The (super) powers of MFractor and how they can make your life easier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T14:31:00.000Z'
originalURL: https://freecodecamp.org/news/the-super-power-of-mfractor-558deeb8ed66
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m8FRApkjXvrgg3OowObeEw.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: visual studio
  slug: visual-studio
- name: Xamarin
  slug: xamarin
seo_title: null
seo_desc: 'By Łukasz Ławicki

  If you ask a Xamarin developer what could be changed in Xamarin development, they
  would for sure mention one of the following:


  build time

  performance

  app start time

  previewers

  removing bin/obj from IDE

  lack of Image wizard in Visua...'
---

By Łukasz Ławicki

If you ask a Xamarin developer what could be changed in Xamarin development, they would for sure mention one of the following:

* build time
* performance
* app start time
* previewers
* removing bin/obj from IDE
* lack of Image wizard in Visual Studio for Mac
* no XAML Intellisense,

and so on...and if I’m being honest, the answers above are right. But hey, we are the developers! If Microsoft won’t give us these features, let’s try to find workarounds or invent something on our own.

There are several libraries and IDE extensions that make our lives easier. For sure one of them is MFractor —a super powerful extension for Visual Studio for Mac.

### So what is MFractor?

MFractor is an extension for Visual Studio for Mac. It was founded in 2015 in Australia. Being on the market for 3.5 years, it has gained people’s trust and love. “How did it do that?” — you might ask. It is because it extends Visual Studio for Mac with features that are missing on a daily basis.

* Do you want XAML Intellisense? Done. Just install MFractor.
* Do you want to remove bin/obj folders within your IDE? MFractor can do it. (By the way — in my opinion, it seems silly that we either need extensions for this or that we need to delete them from time to time. Something is definitely not working…)
* **And here comes the bomb:** Do you want to have an image wizard in Visual Studio for Mac, so you can manage the resources?

I knew you would want that! Have I already told you about MFractor? Och, I did!

Let’s make this clear: **MFractor is a super powerful tool when you are developing apps with Visual Studio on your Mac.**

You might not believe my words, so let’s check how it works in real life.

### Installation

It’s very easy. In VS4Mac, simply open **Extensions_…_** under the Visual Studio menu, click **Gallery** and search for **MFractor**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3KaeayISJSUFKXa3YA4wrg.png)

Voilà. One thing to notice: you will have install instead of **Disable/ Uninstall…** Simply install it and follow the steps required and a pop-up will open. After you’ve installed it, let’s move on to the interesting part.

### Image manager

Let’s start with this totally awesome feature. It came out quite recently, so it is still pretty fresh.

Let’s assume that you want to manage image assets within your project, but you really hate doing it manually.

Check out what MFractor is capable of:

![Image](https://cdn-media-1.freecodecamp.org/images/1*q_4qD5gd8jDy-9B5gnSjQg.png)

As you can see, you have a list of all icons included in the project with thumbnails. When you click on the item, you can see the image in a bigger size. Also, you may notice that there is a dropdown where you can select your project and check which icons are included in the project (SPYROtalks is the name of my project).

#### What can you do within the image manager?

**Import New Image Asset**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cwqa92AX-6dubJH-BPFkig.png)

Adding the asset is really easy.

1. You simply select the image from your computer. MFractor should detect automatically what is the Image Density. If you don’t agree you can change it.
2. After you do it, you need to provide the **Resource name**. Fair enough, right?
3. Now, you need to decide to which projects you want to add the asset.

Basically, that’s all you must provide. If you want, you can resize an image or optimise it. While writing this article I decided to check how good is the image optimisation. In order to check it, I took 10 photos and optimised all of them. Here are the results:

![Image](https://cdn-media-1.freecodecamp.org/images/1*7pOZo3uGONbRbwqAvxf5Og.png)
_Results of optimisation_

As you can see in the table above, in general, the results were pretty good. An average of 54% makes it a good result. What is interesting, though, is the fact that one image was bigger after optimisation than the others. Why? I don’t know.

#### Delete image

In Image manager, you can also delete assets. What is great and time-saving is the fact that it will remove all asset densities at once. No need to delete it 6 (or even more) times. Truly a time saver.

#### Optimise all images

In case you forgot to optimise your asset when adding it, you can later optimise all images. Good to know.

If you want to learn more about image assets, go ahead and read Matthew’s article which is available on MFractor [blog here](https://www.mfractor.com/blogs/news/simplified-image-asset-management-for-xamarin-apps).

### XAML IntelliSense

If you are not that experienced in developing with Xamarin.Forms, you might find developing XAML UIs a nightmare. On the other hand, even if you are an experienced Xamarin.Forms developer, you might get pretty frustrated when using XAML.

First of all, because of the lack of a previewer (there is one, but let’s be honest: it does not work for complex views), you are creating UI’s almost blind. You have to use your imagination. Wouldn’t it be better if we had a built-in LiveXAML or something like that? Unfortunately, it doesn’t look like Microsoft is gonna provide us with something at the moment. A pity.

Secondly, because of the lack of XAML IntelliSense. It would be nice to have it, so when you created bindings to your ViewModel you could select the property from the dropdown instead of typing it on your own. Who has never made a typo in the name of the property, compiled the code and then wondered why the heck it was not working?

#### MFractor to the rescue!

Another great feature of MFractor is XAML IntelliSense. It can suggest to you the names of the properties in ViewModel, so you can bind to them. Also, it can suggest the names of the images you have in resources and many more. Don’t believe me? Go ahead and check these gifs:

![Image](https://cdn-media-1.freecodecamp.org/images/1*SMz2x4MgrEzklBpRU9gfEw.gif)

Just to explain: in my project, I have three icons: _Icon.png, Launcher_Foreground.png,_ and _logo_spyrotalks.png._ As you can see, MFractor is giving me an option to choose one. Nice!

Let’s move on to bindings. As you may suspect, MFractor is suggesting the properties in a similar way that it is suggesting the images.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ny7GBRA2lTcVx_eBSZ7z4g.gif)

As you can see in my ViewModel, I have 5 bindable properties. What I really like is the fact that with MFractor, is almost not possible to make a typo in the name of the property.

#### **Generate ViewModel property**

Are you are a person that prefers to write Views first? If yes, I have good news for you: with MFractor you can generate ViewModel properties from your View.

When creating the View you may find that you’ve forgotten to create one property or another. With MFractor you can create them without changing the file. Nice, huh?

![Image](https://cdn-media-1.freecodecamp.org/images/1*tiv0sQZIqsED0P3sSsdRkA.gif)

#### **Go to a usage of ViewModel property**

From time to time you might want to check where the property is being used. Unfortunately, when you look for references in Visual Studio, it won’t find the ones you have in XAML. Of course, as you may assume, MFractor can find those references for you.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DKF1i0jXygiG5PfqTU1Cwg.gif)

### MVVM Wizard

This is something that wasn’t stated at the beginning of this blog as it was not released yet. According to the marketing announcement in version 3.7.3 the **MVVM Wizard** will be available.

According to the tweet by Matthew Robbins (the founder of MFractor) you will be able to create both View & ViewModels with (almost) one click.

What is nice about this feature is the fact that it gives you control over where you place the files and what are the base classes. It sounds promising, but I had some questions: will it support Xamarin.Native also? If we add XAML with BaseContentPage, will it work out of the box?

So I just installed version 3.7.3, and there is **MVVM Manager**. It looks like the one in the picture above. There are three ways to access it: from the MFractor menu, from Solution options, and with a **Cmd + Shift +M** shortcut. Right now, the manager works for Xamarin.Forms projects only.

If you want ViewModel to derive from BaseClass, you might need to write the class with a namespace before. Otherwise, you will need to import the class when the VM is created.

#### UPDATE 31.01

What you will read below is no longer valid (XAML issue). I have raised the issue above, and after 33h it was solved. Version 3.7.5 should have it fixed. As I have written in my tweet — this is how solving bugs should be done! End of update ;-)

The problem is with the XAML file. As I assumed, deriving from eg. BaseContentPage wouldn’t be that easy. When you want the View to derive from your BaseContentPage you need to feed the MVVM Manager with the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1yGsBw8qPVqFUxilS1WTEQ.png)

Is the code visible that we need? Not fully. It’s similar to the one that we want but not exactly the same. We need code like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*edLNzudQii71JenMrW0eSg.png)

It is not a big change, but we need to handle it on our own. I can fully understand that this is not an easy task to achieve. I believe it’s still better to slightly adjust the created files than to create them from scratch.

If you are interested, on the MFractor [blog](https://www.mfractor.com/blogs/news/generating-viewmodels-in-xamarin-forms-with-the-mvvm-wizard) you can read more about MVVM Manager.

### bin/obj

As I have stated at the beginning of this article, I am not sure what to think of bin/obj folders. Firstly, you have to delete them pretty often when developing a Xamarin app. I think it’s an issue.

Why do we have to do it? If it is a known issue (and based on my conversations with my colleagues, I believe it is), shouldn’t we be provided with an option to delete those folders within our IDE? Doing it manually takes so long. Sure, you can have a script to do it, but is it something we need to implement on our own?

Fortunately, MFractor has a feature that can delete those folders for you. How? Pretty simple. Check it out:

![Image](https://cdn-media-1.freecodecamp.org/images/1*egwuFt435DqROt58nB6sJg.gif)

In here you have options: either delete Output folders (deletes bin/obj & NuGet packages) or you can only Clear Nuget Packages.

### Conclusion

So what are the cons of using MFractor? Some might say that **MFractor Professional** price ($200 AUD per year) can be the issue. But hey! Is it that much for a lifetime license? I don’t think so. Especially when you take into consideration the number of hours being wasted because of, for example, a typo in your XAML or adding image assets.

Originally posted on my [blog](http://lukaszlawicki.pl/mfractor/) ?

