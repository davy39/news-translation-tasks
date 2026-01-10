---
title: How to uniquely name your elements and  automate tests for your desktop app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T20:43:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-uniquely-name-your-elements-and-automate-tests-for-your-desktop-app-8fec67eaca4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N9MfB3_mghGuOlRHX5YAzw.jpeg
tags:
- name: 'automation testing '
  slug: automation-testing
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Vinicius de Melo Rocha

  Motivation

  Writing automated tests for Desktop applications is not an easy task. Especially
  when it uses Windows Presentation Foundation (WPF). This allows so many possibilities
  of nested control and complex grids and menus....'
---

By Vinicius de Melo Rocha

### Motivation

Writing automated tests for Desktop applications is not an easy task. Especially when it uses Windows Presentation Foundation (WPF). This allows so many possibilities of nested control and complex grids and menus.

Here at [Clemex](https://www.clemex.com/), we use a tool to automate desktop tests that rely on the WPF `[FrameworkElement.Name](https://msdn.microsoft.com/en-us/library/system.windows.frameworkelement(v=vs.110).aspx)` property to interact with the application. Because we need to create dynamic controls based on collection data, they can end up with the same name for multiple UI elements.

For example, the following code generates a menu based on a collection of panels.

Inspecting the element tree, we would see that we now have multiple elements with the same name: “MenuBtn”.

To avoid this situation and have unique names for each button, we came up with four different approaches.

* Using the Code-Behind
* Using data binding
* Using attached properties
* Using collection indexes

### Using the Code-Behind

Assuming that we have access to some unique ID on the elements data context. The easiest approach is to use the `Loaded` event of `FrameworkElement` to set a unique name using the code-behind model.

Now, when we check the element tree, we will see that we have unique names for each button.

### Using data binding

Using data binding makes our code much cleaner, as well as easier to read and understand. If we try a similar approach using data binding we might end up with source code like the following:

Unfortunately, if we try to build this code, we will get a compilation error with the message:

> MarkupExtensions are not allowed for Uid or Name property values, so ‘{Binding Panel.PanelType, StringFormat=’MenuBtn{0}’}’ is not valid.

This restriction prevents us from binding directly to the `Name` property.

### Using attached properties

To overcome the limitation of the previous attempt we can define a new property that would set the name for us. To add new properties to existing controls we can use [Attached Properties](https://docs.microsoft.com/en-us/dotnet/framework/wpf/advanced/attached-properties-overview).

The `OnValueChanged` event triggers every time the value of our property changes. When that happens, we get the new value and set it to be the `FrameworkElement` name. We are giving our attached property the name `Name`. It could be anything we want, like `CustomName` or `TestName`.

To use the new property, we need to add a namespace to the XAML and attach the property to our button.

Our code will now compile without any problems, and we will have unique names for each element.

### Using collection indexes

In the previous example, we created unique names by appending the property `Id`. There are other scenarios where we don’t have an ID on the item to create a unique element name. For that, we can instead use the collection index.

Let’s try to bind our button collection to a list of strings.

To achieve that, we can use the same `AttachedProperty` with a converter. It will look for the index of the element inside the collection.

In the XAML, we will now use [MultiBinding](https://msdn.microsoft.com/en-us/library/system.windows.data.multibinding(v=vs.110).aspx) because we need both the element and the collection.

Looking at the element tree we can see that our buttons are named `MenuBtn00`, `MenuBtn01` and so on.

### Summary

Generating unique names for dynamically created WPF controls can be done in an elegant way by using Attached Properties and using the multi-binding with a custom converter.

