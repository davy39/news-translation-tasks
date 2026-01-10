---
title: What Does JavaScript:Void(0) Mean?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T18:06:00.000Z'
originalURL: https://freecodecamp.org/news/what-does-javascript-void-operator-do
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/jeremy-thomas-rMmibFe4czY-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'JavaScript’s void operator evaluates an expression and returns undefined.

  You can use the console to verify the same:


  Note: void, irrespective of any value passed along, always returns undefined as
  shown above. But, void with the operand 0 is prefer...'
---

JavaScript’s void operator evaluates an expression and returns undefined.

You can use the console to verify the same:

![ConsoleOutput](https://github.com/srawat19/-Guide_Images/blob/master/VoidConsole.PNG?raw=true)

**Note**: **void**, irrespective of any value passed along, *always returns **undefined** as shown above*. But, **void with** the **operand 0 is preferred**.

There are two ways of using operand 0: void(0) or void 0. Either of them is fine.

## When to use Javascript void(0)

Use javascript:void(0) if, when a link is clicked, you don’t want the browser to load a new page or refresh the same page (depending on the URL specified).

Instead it will just perform the JavaScript attached to that link.

### Example 1 with Javascript void(0):

```html
<html>
<body>
<a href="javascript:void(0);alert('Hello ! I am here')">Click Me</a>
</body>
</html>
```

#### **Output:**

When someone clicks on the ClickMe link, an alert pops up as below:

![Output1](https://github.com/srawat19/-Guide_Images/blob/master/voidOutput1.PNG?raw=true)

### Example 2 with Javascript void(0):

```html
<html>
<body>
<a href="javascript:void(0)" ondblclick="alert('Hi,i didnt refresh the page')" )>Click Me</a>
</body>
</html>
```

#### **Output:**

When you double click the link, an alert will popup without any page refresh.

### Example 3 with Javascript void(0):

```html
<html>
<body>
<a href="javascript:void(0);https://www.google.co.in/" 
ondblclick="alert('Hello !! You will see me and not get redirected to google.com ')">Click Me</a>
</body>
</html>
```

#### **Output:**

When you double click the link, an alert will popup. Closing it will also not redirect to google.com.

### Example without Javascript void(0):

```html
<html>
<body>
<a href="https://www.google.co.in/" ondblclick="alert('Hello !! You will see me and then get redirected to google.com even if not needed')">Click Me</a>
</body>
</html>
```

#### **Output:**

When you double click the link, an alert will popup, but closing it will redirect to google.com.

## Conclusion

The **void** operator is useful when you need to prevent any unwanted page refresh or redirection. Rather, it performs some JavaScript operation.

#### **More Information:**

1. [Mozilla Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)

