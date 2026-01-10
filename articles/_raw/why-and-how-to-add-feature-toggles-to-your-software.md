---
title: Why and How to Add Feature Toggles to Your Software
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-11-24T15:49:00.000Z'
originalURL: https://freecodecamp.org/news/why-and-how-to-add-feature-toggles-to-your-software
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/featuretoggles.png
tags:
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Feature Toggles (aka Feature Flags) are a technique used in software development
  in order to hide, enable or disable a particular feature during runtime. They allow
  teams to modify system behavior without changing code.

  We just published a course on ...'
---

Feature Toggles (aka Feature Flags) are a technique used in software development in order to hide, enable or disable a particular feature during runtime. They allow teams to modify system behavior without changing code.

We just published a course on the freeCodeCamp YouTube channel that will teach you why and how to use feature toggles in your software.

<style>
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input { 
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>
<label class="switch">
  <input type="checkbox" onclick="toggle()">
  <span class="slider round"></span>
</label>
<br>
<img src="https://www.freecodecamp.org/news/content/images/2021/03/comments-meme.jpeg" id="secretimg" style="display:none;">
<script>
function toggle() {
  var x = document.getElementById("secretimg");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>

Fredrik Strand Oseberg created this course. Fredrik is a principle software engineer at Unleash, an open-source product that makes it simpler to add feature toggles to your software. Unleash provided freeCodeCamp a grant that helped make this course possible.

In this course you will learn the basics of what feature toggles are, how you can use them, and how they can help you to improve the workflow of your development team to accelerate time to delivery.

The course starts with an interview of Ivar Østhus, the founder of Unleash, and then continues to look into basic feature toggle use cases and how you can set up Unleash open source to tackle more advanced use cases and scenarios.

Here are the sections covered in this course:

* Introduction to feature toggling with Ivar Østhus
* Basic feature toggle implementation
* Basic feature toggle pitfalls
* Implementing an external feature toggle configuration
* Feature toggle vendors
* Unleash architecture
* Setup unleash open source with docker
* Create an API key
* Setup unleash proxy with docker
* Application overview and creating a feature toggle
* Using feature toggles in a real application
* Connecting to unleash with the react proxy sdk  
* Understanding stickiness and unleash context
* Using strategies for segmentation
* Introduction to Experimentation
* Understanding variants 
* Implementing variants in our codebase
* Using analytics providers to understand experiment data
* Usage metrics
* Technical debt and cleaning up feature toggles
* Outro

Watch the full course below or [on the freeCodeCamp.org YouTube channel](https://youtu.be/-yHZ9uLVSp4) (2-hour watch).

%[https://youtu.be/-yHZ9uLVSp4]

You may also find this article helpful: 11 principles for building a large-scale [feature flag](https://docs.getunleash.io/topics/feature-flags/feature-flag-best-practices) system.

