---
title: <pre> Tag in HTML – Example Code
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-05T21:33:51.000Z'
originalURL: https://freecodecamp.org/news/pre-tag-in-html-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pre-tag.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "The HTML <pre> tag defines a preformatted block of text. It comes in handy\
  \ when you want to display text where the typographical formatting affects the meaning\
  \ of the content, such as code snippets and poems. \nBy default, browsers ignore\
  \ white space ..."
---

The HTML `<pre>` tag defines a preformatted block of text. It comes in handy when you want to display text where the typographical formatting affects the meaning of the content, such as code snippets and poems. 

By default, browsers ignore white space of any kind – extra text space, line breaks, tabs, or any other formatting characters – that are specified in the HTML. 

But with the `<pre>` tag, you can preserve all the white space you want. The default font-family assigned to any text inside the `<pre>` is `monospace`, but you can override it with CSS if you want. 

In this tutorial, we will look at the `<pre>` tag in detail. I'll show you how it works using some "with and without" code snippets so you can have more fun writing HTML, as HTML was never designed to be boring.

### Basic Syntax

Just like a lot of other HTML elements, the `<pre>` tag takes a closing tag (`</pre>`) as well.

```html
<pre>
            Hello World, 
            this text is inside a pre tag, all white       spaces     are 


        preserved
</pre>
```

Check out the screenshot below for the result:
![basic](https://www.freecodecamp.org/news/content/images/2021/08/basic.png)

## Examples of the `<pre>` Tag in HTML

Below are some code snippets and screenshots that show you how the `<pre>` tag works. 

### White Space in HTML without the `<pre>` Tag
```html
<div>
     <p>There are extra white spaces in the next two words, but they are ignored        by the browser: Hello  
     World</p>
</div>
```

```css
body {
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
      }

p, pre {
          font-size: 1.2rem;
      }
```

![ss1-1](https://www.freecodecamp.org/news/content/images/2021/08/ss1-1.png)

### White Space in HTML with the `pre` Tag

```html
<div>
     <p>There are extra white spaces in the next two words, made visible by the        <code>pre</code> 
     tag: <pre>Hello   World</pre> </p>
</div>
```
![ss2-1](https://www.freecodecamp.org/news/content/images/2021/08/ss2-1.png)

### Tab in HTML without the `pre` Tag

```html
<div>
     <p>There are tabs between the next words, but they're ignored by the browser:      I'm   a   camper</p>
</div>
```

![ss3-1](https://www.freecodecamp.org/news/content/images/2021/08/ss3-1.png)

### Tab in HTML with the `pre` Tag 

```html
<div>
     <p>There are tabs between the next words, made visible with the                    <code>pre</code> <pre>tag: I'm   
     a   camper</pre></p>
</div>
```

![ss4-1](https://www.freecodecamp.org/news/content/images/2021/08/ss4-1.png)

### Line Breaks in HTML without the `<pre>` Tag 

```html
<div>
<p>
        There are line breaks between the next words: 
        I'm

        a

        camper
    </p>
</div>
```

![ss5-1](https://www.freecodecamp.org/news/content/images/2021/08/ss5-1.png)

### Line Breaks in HTML with the `<pre>` Tag

```html
<div>
    <p>
    There are line breaks between the next words: 
   <pre>
   I'm

   a

   camper
   </pre>
    </p>
</div>
```

![ss6-1](https://www.freecodecamp.org/news/content/images/2021/08/ss6-1.png)

As you can probably imagine now, the `<pre>` tag is super useful in CSS art (HTML art too), illustrations, for inserting code snippets into HTML, and lots more.

## How to Insert Code Snippets without the `<pre>` Tag

Oftentimes, you might need to display code snippets on web pages for academic purposes or in the documentation of a programming language or framework. This helps you/the maintainers properly communicate with learners. 

And you'll want to preserve white space even after using the `<code>` tag to do it, and that's exactly what the `<pre>` tag does.

```html
<div> 
<h3>Some CSS Resets</h3>
      <p>
        Did you know you can remove the default padding and margin browsers
        insert onto web pages?
      </p>
      <code> * { padding: 0; margin: 0; box-sizing: border-box; }</code>
</div>
```

```css
 body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
```

![ss7-1](https://www.freecodecamp.org/news/content/images/2021/08/ss7-1.png)

## How to Insert Code Snippets with the `<pre>` Tag in HTML

```html
<div>
<h3>Some CSS Resets</h3>
      <p>
        Did you know you can remove the default padding and margin browsers
        insert to web pages?
      </p>
      <pre>
    <code>
        * {
         padding: 0;
         margin: 0;
         box-sizing: border-box;
       }
    </code>
    </pre>
      <p>Now you know that.</p>
</div>
```

![ss8](https://www.freecodecamp.org/news/content/images/2021/08/ss8.png)

### A Bit of Art without the `<pre>` Tag

```html
 <div><p>                     ^^^^^^^^^^^^^^^^^^^^^
                <><><>       ^ I'm Kolade,        ^
               <>    <>     ^  Web developer from ^
                <><><>  ^^^^   Nigeria.           ^          
                  <>        ^  I'm proud to be a  ^
                  <>         ^ Camper.            ^  
               <> <> <>       ^^^^^^^^^^^^^^^^^^^^^  
             <>   <>   <>
            <>    <>     <>
                  <>    
                <>  <>  
               <>    <>
              <>      <>
             <>        <>
            <>          <>
           <>            <></p> </div>
```

```css
body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
      }
```


![ss9](https://www.freecodecamp.org/news/content/images/2021/08/ss9.png)

### A Bit of Art with the `<pre>` Tag

```html
<div>
      <pre>
                              ^^^^^^^^^^^^^^^^^^^^^
                <><><>       ^ I'm Kolade,        ^
               <>    <>     ^  Web developer from ^
                <><><>  ^^^^   Nigeria.           ^          
                  <>        ^  I'm proud to be a  ^
                  <>         ^ Camper.            ^  
               <> <> <>       ^^^^^^^^^^^^^^^^^^^^^  
             <>   <>   <>
            <>    <>     <>
                  <>    
                <>  <>  
               <>    <>
              <>      <>
             <>        <>
            <>          <>
           <>            <>
      </pre>
    </div>
```

![ss10](https://www.freecodecamp.org/news/content/images/2021/08/ss10.png)

## How to Fix Unnecessary Scrollbars

Because the text inside a `<pre>` tag are displayed in the browser as they are in the code, having a block or line of text wider than the available screen width leads to a horizontal scrollbar. You can also sometimes get an unnecessary vertical scrollbar too. 

```html
    <div>
        <pre> These are some lorem texts: Lorem ipsum 
            
dolor sit                amet consectetur adipisicing elit. Amet rem nam ea nihil fuga doloribus voluptatem sed officiis iusto. Eveniet quaerat sit quisquam                consequatur necessitatibus 


totam placeat, ut unde                  nesciunt.
        </pre>
    </div>
```

![problem](https://www.freecodecamp.org/news/content/images/2021/08/problem.png)

To get rid of this, CSS provides a `white-space` property. Setting its value to `wrap` gets rid of the scrollbars.

```css
pre {
      white-space: pre-wrap;
    }
```

![problemFix](https://www.freecodecamp.org/news/content/images/2021/08/problemFix.png)

## Conclusion
 
During this tutorial, you have seen how the `<pre>` tag works in HTML. Now go have some fun with it in your next coding project. 

Thank you for reading, and keep coding.



