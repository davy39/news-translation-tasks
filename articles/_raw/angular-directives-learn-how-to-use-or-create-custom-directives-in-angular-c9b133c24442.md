---
title: How to use and create custom directives in Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-30T12:28:26.000Z'
originalURL: https://freecodecamp.org/news/angular-directives-learn-how-to-use-or-create-custom-directives-in-angular-c9b133c24442
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A4-tgMN9OZ6gIoRVFDJj_g.jpeg
tags:
- name: Angular
  slug: angular
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Gulfam Ansari

  After playing with Angular for a long time, I finally came up with an understandable
  explanation of Angular directives. In this article, we will first understand what
  a directive exactly is and how to use it in Angular. We will creat...'
---

By Gulfam Ansari

After playing with Angular for a long time, I finally came up with an understandable explanation of Angular directives. In this article, we will first understand what a directive exactly is and how to use it in Angular. We will create our own custom directives as well. So what are we waiting for? Let's dive deep into it.

### What is an Angular Directive?

Directives are the functions which will execute whenever Angular compiler finds it**.** Angular Directives enhance the capability of HTML elements by attaching custom behaviors to the DOM.

From the core concept, Angular directives are categorized into three categories.

1. **Attribute Directives**
2. **Structural Directives**
3. **Components**

#### Attribute Directives

Attribute Directives are responsible for manipulating the appearance and behavior of DOM elements. We can use attribute directives to change the style of DOM elements. These directives are also used to hide or show particular DOM elements conditionally. Angular provides many built-in Attribute Directives like **NgStyle**, **NgClass**, etc. We can also create our own custom Attribute Directives for our desired functionality.

#### **Structural Directives**

Structural Directives are responsible for changing the structure of the DOM. They work by adding or removing the elements from the DOM, unlike Attribute Directives which just change the element’s appearance and behavior.

You can easily differentiate between the Structural and Attribute Directive by looking at the syntax. The Structural Directive’s name always starts with an asterisk(*) prefix, whereas Attribute Directive does not contain any prefix. The three most popular built-in Structural Directives Angular provides are **NgIf**, **NgFor**, and **NgSwitch**.

#### **Components**

Components are directives with templates. The only difference between Components and the other two types of directives is the Template. Attribute and Structural Directives don't have Templates. So, we can say that the Component is a cleaner version of the Directive with a template, which is easier to use.

### **Using Angular Built-In Directives**

There are a lot of built-in Directives available in Angular which you can easily use. In this section, we will use two very simple built-in directives.

**NgStyle Directive** is an Attribute directive used to change the styling of any DOM element on the basis of some condition.

```
<p [ngStyle]="{'background': isBlue ? 'blue' : 'red'}"> I am an Attribute Directive</p>
```

> In the above code snippet, we are adding a blue background if the value of `isBlue` variable is true. If the value of `isBlue` variable is false, then the background of the above element will be red.

**NgIf Directive** is a structural directive used to add elements into the DOM according to some condition.

```
<p *ngIf="show">I am a Structural Directive</p>
```

> In the above code snippet, the whole paragraph will remain in the DOM if the value of `show` variable is true, else it will kick off from the DOM.

### **Creating a Custom Attribute Directive**

Creating a custom directive is just like creating an Angular component. To create a custom directive we have to replace `@Component` decorator with `@Directive` decorator.

So, let's get started with creating our first Custom Attribute directive. In this directive, we are going to highlight the selected DOM element by setting an element’s background color.

Create an `app-highlight.directive.ts` file in `src/app` folder and add the code snippet below.

```
import { Directive, ElementRef } from '@angular/core';
```

```
@Directive({
```

```
    selector: '[appHighlight]'
```

```
})
```

```
export class HighlightDirective {
```

```
    constructor(private eleRef: ElementRef) {
```

```
        eleRef.nativeElement.style.background = 'red';
```

```
    }
```

```
}
```

Here, we are importing `Directive` and `ElementRef` from Angular core. The `Directive` provides the functionality of `@Directive` decorator in which we provide its property selector to `appHighLight` so that we can use this selector anywhere in the application. We are also importing the `ElementRef` which is responsible for accessing the DOM element.

Now to get `appHighlight` Directive to work, we need to add our Directive to the declarations array in the `app.module.ts` file.

```
import ...;
```

```
import { ChangeThemeDirective } from './app-highlight.directive';
```

```
@NgModule({
```

```
declarations: [
```

```
AppComponent,
```

```
ChangeThemeDirective
```

```
],
```

```
imports: [
```

```
...
```

```
],
```

```
providers: [],
```

```
bootstrap: [AppComponent]
```

```
})
```

```
export class AppModule { }
```

Now we are going to use our newly created custom directive. I am adding the `appHightlight` directive in the `app.component.html` but you can use it anywhere in the application.

```
<h1 appHightlight>Highlight Me !</h1>
```

The output of the above code snippet will look like this.

![Image](https://cdn-media-1.freecodecamp.org/images/2gCU64J6c149TzNBHuP-QROInU7IA09OyDwA)

### Creating a Custom Structural Directive

In the previous section, we created our first Attribute directive. The same approach is used to create the structural directive as well.

So, let’s get started with creating our structural directive. In this directive, we are going to implement the `*appNot` directive which will work just opposite of `*ngIf`.

Now create a `app-not.directive.ts` file in the `src/app` folder and add the code below.

```
import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';
```

```
@Directive({
```

```
    selector: '[appNot]'
```

```
})
```

```
export class AppNotDirective {
```

```
constructor(
```

```
    private templateRef: TemplateRef<any>,
```

```
    private viewContainer: ViewContainerRef) { }
```

```
    @Input() set appNot(condition: boolean) {
```

```
        if (!condition) {
```

```
            this.viewContainer.createEmbeddedView(this.templateRef);
```

```
        } else {
```

```
            this.viewContainer.clear();        }
```

```
    }
```

```
}
```

As you saw in the above code snippet, we are importing `Directive, Input, TemplateRef and ViewContainerRef` from `@angular/core.`

`Directive` provides the same functionality for the `@Directive` decorator. The `Input` decorator is used to communicate between the two components. It sends data from one component to the other using property binding.

`TemplateRef` represents the embedded template which is used to instantiate the embedded views. These embedded views are linked to the template which is to be rendered.

`ViewContainerRef` is a container where one or more views can be attached. We can use `createEmbeddedView()` function to attach the embedded templates in the container.

Now to get the `appNot` directive to work, we need to add our directive to the declarations array in the `app.module.ts` file.

```
import ...;
```

```
import { AppNotDirective } from './app-not.directive';
```

```
@NgModule({
```

```
declarations: [
```

```
AppComponent,
```

```
AppNotDirective
```

```
],
```

```
imports: [
```

```
...
```

```
],
```

```
providers: [],
```

```
bootstrap: [AppComponent]
```

```
})
```

```
export class AppModule { }
```

Now, it’s time to use our newly created structural directive.

I am adding the `appNot` directive in the `app.component.html` but you can use it anywhere in the application.

```
<h1 *appNot="true">True</h1><h1 *appNot="false">False</h1>
```

The `*appNot` directive is designed in a way that it appends the template element into the DOM if the `*appNot` value is `false` just opposite the `*ngIf` directive.

The output of the above code snippet will look like this.

![Image](https://cdn-media-1.freecodecamp.org/images/Gq-nb90cSoMpnte266GnWRQb3RuUqVESuRAe)

I hope this article answered most of your questions regarding Angular directives. If you have any queries or doubts, feel free to reach out to me in the comment box.

