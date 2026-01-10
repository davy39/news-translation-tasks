---
title: A step-by-step guide to getting started with HTML forms
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T23:55:42.000Z'
originalURL: https://freecodecamp.org/news/a-step-by-step-guide-to-getting-started-with-html-forms-7f77ae4522b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7dd2MZ78ekF3bA3N0Jlvmw.gif
tags:
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Abhishek Jakhar

  Overview

  HTML forms are required when you want to collect some data from the person who visits
  your website. For example, when you register/login for applications like Uber, Netflix,
  or Facebook, you enter information like Name, Em...'
---

By Abhishek Jakhar

#### Overview

HTML forms are required when you want to collect some data from the person who visits your website. For example, when you register/login for applications like Uber, Netflix, or Facebook, you enter information like **Name**, **Email**, and **Password** through HTML **forms**.

Now we will learn all the required elements for creating a form.

> **NOTE:** I have already added the Styling using CSS and so my elements will look different, but they will work in exactly the same way.  
> If you want to make your elements look like mine then, you can find my CSS file in the links given below:  
> Custom CSS: [https://gist.github.com/abhishekjakhar/493d920a219ed9d88f1846cd31de7751](https://gist.github.com/abhishekjakhar/493d920a219ed9d88f1846cd31de7751)  
> Normalize CSS:  
> [https://gist.github.com/abhishekjakhar/3a6c25fa61a293b6a56d28f98497808b](https://gist.github.com/abhishekjakhar/3a6c25fa61a293b6a56d28f98497808b)

#### Form Element

This is the first element which we will learn. This element wraps all the other elements that go inside of our form. This is the form element.

Our form won’t submit the data anywhere because it is not connected to a server. To connect our form to a server and process our data, we can use any server-side language like Node, Python, Ruby, or PHP. The part of processing the data involves two important attributes that are attached to the form element. Let’s take a look at those attributes.

**Attributes:**

1. **action:** The action attribute is the web address (URL) of a program that processes the information submitted by our form.
2. **method:** It is the [HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) that the browser uses to submit the form, the possible values are **POST** and **GET.**

* **POST** — Data from the body of the form is sent to the server.
* **GET** — Data is sent inside of the URL and parameters are separated with a question mark.

> **Note:** You cannot have **forms** nested **inside another form**. That means you cannot have a <form> element inside another<form> element.

#### Input Element

The input element is the most commonly used form element. It is used to make a **text field** where the user can type some **information** for example **email**, **password** etc.

Let’s make a text field where the user can type in their name.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pGZFUO5zQ1_QquSAcECo_Q.gif)

> **Note:** The input element is a self-closing tag, so there’s no need to type a closing tag to match the opening tag.

I have added three attributes in the above input tag. Let’s take a look at each one in detail.

**type**

The **type** attribute indicates what kind of input we want. If we give a value of **text** to the **type** attribute, than what we mean here is that the value which we are entering into the input field is of type text. There are many possible values for this particular attribute. Some possible values are email, tel for telephone and password etc.

Example: When you login into any of your accounts (Amazon/Netflix), you need to enter two things: **email** and **password**. So in this particular case the **input** element is used. The **type** attribute is given with the value of **email** and **password** respectively.

**id**

The ID attribute is not mandatory, but it’s a good idea to add one. In some cases, this is helpful for targeting elements with CSS/JavaScript. The ID attribute is added so that we can associate **labels** to **specific form controls**.

**name**

The name attribute is necessary. When a form is submitted to the server side code, the server can understand the form data and process the values appropriately.

**placeholder**

It is a short hint which is displayed in the input field before the user enters a value. As the user starts typing in the input field the placeholder disappears.

Let’s see what a few other basic input elements look like.

> **Note:** Using **different values** for the **type attribute** will produce different results. For example you can make input be of type email, text, or password etc. All of them show **slightly different behaviour,** which you will see below.

Multiple Input Elements (Text, Email, Password)

Multiple Input Element (Text, Email, Password)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UgNfHeAhkl-GQ0btgglbXA.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*I5AeYrtMwoAi-UtAxdPw9g.gif)
_**Input** elements without **placeholder**(Left) &amp; with **placeholder**(Right) attribute_

#### Textarea Element

Sometimes a single line of text is not enough and a simple input element won’t work. For example, some websites have a contact form for people to type their queries or messages. In these cases, it’s best to use the `textarea` element.

The **<textar**ea> is not a self-closing tag, so we need to type both the opening and the closing tag. (<textarea></textarea>)

**Attributes:**

* **id:** Same as mentioned above in <input/> element.
* **name:** Same as mentioned above in <input/> element.
* **cols:** Specifies the visible width of a text area.
* **rows:** Specifies the visible number of lines in a text area.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_k2gP5oTjbllKQtpDBfaAA.gif)
_Textarea Element_

You can see that the textarea allows us to type in multiple lines. A textarea is resizable by the user, you can see in the above illustration that I am resizing the textarea.

> **Note:** In most browsers the **textarea** element is resizable.

#### Button Element

The button element is one of the most important form elements. Without a button you cannot submit any form to the server for processing.

The button element accepts the attribute called **type.** This attribute accepts three values **submit**, **reset** and **button**.

**Attributes:**

* **type**=”reset”: It will **clear** **all the form data** when it’s clicked.
* **type**=”button”: It does not have any default behavior and it’s mostly used with JavaScript to program it for **custom behavior**.
* **type**=”submit”: The default behavior of the **submit type** is, as the name implies, submit the form and send all the data over to the server.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j8Pb34UJc8luxp_yUHBmRA.gif)
_Button of type submit_

#### Label Element

Right now it’s impossible for the user to tell which form control does what. There’s no way to know where you will be entering the email and where you will be entering the password. The form looks very incomplete and messy.

We can label each one of our forms controls using the label element.

The most used attribute with a **label** is **for.**

**Attributes:**

* **for:** The **for** attribute associates the label with a particular form element. The way it **matches is by ID**. As you can see in the above example the **value of the ID** attribute given to the input element is **email.** The value of the **for** attribute given to the label element is also **email,** so both of them are associated with each other.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ksf3FWyd6KOa4QIak8mSfA.gif)

> **Note:** When we click on the label, we automatically get the focus to the input field which is associated with the label. This is a default behaviour.

Now our form looks very good ?.

#### Select Menus

Sometimes, when you’re creating a form, you don’t want the user to be able to type in the text. Rather, you might want them to pick from **some preset options that you provide**.

Anytime you have a list of options that’s longer than, say, four or five things, it’s best to go with the select menu because it saves space.

Let’s say that our form is targeted for students who are going to seek admission at a university. We want to allow students to select from a predefined list of university programs.

The select menu element is made using opening and closing **<sele**ct> tag.

**<sele**ct> — The select element rend**ers a drop-dow**n menu that contains selectable options**. The** select element won’t do anything, by itself. This form element actually needs additional elements inside of it, exactly **lik**e <ul> ele**ment**s needs <li> elements. The elements **we put** inside of select e**lement** are called option elements.

**Attributes:**

* **name:** Same as mentioned above in <input/> element.

**<opti**on> — The option element represents one of the choices that a user can choose in a select menu**. The &l**t;option> elem**ent uses** an attri**bute c**alled value.

**Attributes:**

* **value:** When you submit a form to server-side code, each form element has an associated value for text inputs and text areas. That value is whatever the user types into the field. However, since we’re creating these predefined options, we need to specify what the value should look like when it’s submitted. So, we use the **value** attribute to specify the values to predefined options.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EkXaeFfKPsK1lbiDAeQvyg.gif)
_Select Menu_

Now we have Select Courses label with the select menu which we have just created. Now, we can also organize our list into logical groups with the **<optgro**up> element.

**Attributes:**

* **label:** The name of the group of options. In the example given below our list of options has been divided into two groups with the label of Engineering and Management.

In the example given below

![Image](https://cdn-media-1.freecodecamp.org/images/1*GHsseV7OitD9m9mTjHb8BA.gif)

#### Radio Buttons

Select menus are great if you have lots of options. If you have something like 5 or fewer options, it’s better to use radio buttons.

The difference between Select Menu and Radio Button is that radio buttons show you all the options at once. Like the select menu the user can only pick from one of them.

**Attributes:**

* **name:** Same as mentioned above in <input/> element.
* **value:** Since we’re creating these predefined options, we need to specify what the value should look like when it’s submitted. So, we use the **value** attribute to specify the values to predefined options.

> **_Note:_** _If you select one option and then you try to select another option, you’ll see that it deselects the previous option. The way that it knows to do that is because we have the **name** attribute exactly same. So it knows that these two radio buttons are part of the same group._

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jxp4WvykcA7siX0SG2P2CQ.gif)

> **Note:** Name should be the same if we want radio buttons to be a part of the same radio button group.

#### Checkboxes

Sometimes you might have a group of predefined options. You want the user to be able to select multiple options and not just one of them. That’s where checkboxes are useful.

**Attributes:**

* **name:** Same as mentioned above in <input/> element.
* **value:** Since we’re creating these predefined options, we need to specify what the value should look like when it’s submitted. So, we use the **value** attribute to specify the values to predefined options.
* **checked:** By default, a checkbox input is unchecked. You can set the default state to checked by using the attribute called **checked**. Remember this is a boolean attribute.

```
<input type="checkbox" checked id="name" value="abhishek" name="user_name" />
```

In the example given below, I have used the label for each individual option. I have connected the **checkbox** and a **label** using the **for** attribute of **label** and **id** attribute of the **checkbox**.

> **_Note:_** _It can be hard to click a small checkbox. It is recommended to wrap a <label> element around the checkbox. If we click the label then also our checkbox gets checked or unchecked. I have not done it below, but you can do it to make the UX b_etter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SFY1wuzU-95_FqsrkfuFMw.gif)

#### Difference between Checkbox and Radio button

1. Checkbox can exist **on its own**, while radio buttons can only appear as a **group** (minimum of 2 radio buttons should be there).
2. Selecting checkbox is **optional** but choosing one of the radio button is **mandatory**.

#### The Complete Form

![Image](https://cdn-media-1.freecodecamp.org/images/1*BWh2qjSRTuAa6ixPGsKcrg.png)

We’ve learned about lots of HTML form elements and have covered the essentials.

Don’t worry about memorizing everything. Almost no professional web developer can name every attribute or element. What’s more important than memorization is learning how to look up things in the documentation when you need them.

You can try adding your own CSS to make this form look the way you want it to look.

You can learn more about forms in the link given below

[**HTML forms**](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms)  
[_This module provides a series of articles that will help you master HTML forms. HTML forms are a very powerful tool for…_developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms)

I hope you’ve found this post informative and helpful. I would love to hear your feedback!

**Thank you for reading!**

