---
title: How to Write Math Equations in Google Docs
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2025-05-16T15:42:41.421Z'
originalURL: https://freecodecamp.org/news/write-math-equations-in-google-docs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747410133881/93c8cf6e-6cbb-4890-8023-fcc2fdaa0fa2.png
tags:
- name: Google Docs
  slug: google-docs
- name: Mathematics
  slug: mathematics
- name: chatgpt
  slug: chatgpt
- name: chatgptguide
  slug: chatgptguide
- name: MathJax
  slug: mathjax
seo_title: null
seo_desc: Math equations are a critical part of academic papers, research reports,
  and technical documentation. While LaTeX is widely used for professional typesetting,
  Google Docs offers a robust set of features for inserting and formatting math equations
  and...
---

Math equations are a critical part of academic papers, research reports, and technical documentation. While LaTeX is widely used for professional typesetting, Google Docs offers a robust set of features for inserting and formatting math equations and also supports LaTeX-style input.

Whether you're a student submitting a math assignment or a professional documenting formulas, Google Docs provides multiple ways to insert and format equations efficiently.

In this article, you'll learn how to [write math equations in Google Docs](https://support.google.com/docs/answer/160749) using different methods, including using Google Docs’ built-in equation editor and typing LaTeX-style commands directly, inserting complex equations with the help of the Auto-LaTeX add-on, and copying math equations from [ChatGPT to Google Docs](https://chromewebstore.google.com/detail/chatgpt-to-google-docs-or/oibghjgooccojibfacdonaoipegckdeg) without losing formatting by using the ChatGPT to Google Docs or PDF Chrome extension.

## Table of Contents

* [How to Write Equations Using the Built-in Equation Editor](#heading-how-to-write-equations-using-the-built-in-equation-editor)
    
* [How to Write Equations Using LaTeX Commands](#heading-how-to-write-equations-using-latex-commands)
    
* [How to Use Auto Latex Add-on for Writing Advanced Math Equations](#heading-how-to-use-auto-latex-add-on-for-writing-advanced-math-equations)
    
* [How to Copy Math Equations from ChatGPT to Google Docs](#heading-how-to-copy-math-equations-from-chatgpt-to-google-docs)
    
* [Watch: How to Write Equations in Google Docs](#heading-watch-how-to-write-equations-in-google-docs)
    
* [Tips for Formatting Math Equations in Google Docs](#heading-tips-for-formatting-math-equations-in-google-docs)
    
* [Conclusion](#heading-conclusion)
    

## **How to Write Equations Using the Built-in Equation Editor**

Google Docs has a built-in equation editor that makes it easy to insert mathematical symbols and expressions.

To insert an equation editor box:

1. Open your Google Docs document.
    
2. Go to the top menu and click *Insert* → *Equation*.
    
3. An equation editor will appear, and a new toolbar will show up with common math symbols like fractions, exponents, Greek letters, and more.
    

Alternatively, you can use the following keyboard shortcuts to insert an equation editor box. 

* **Windows/Linux:** `Alt` + `I`, then `E`
    
* **Mac:** `Control` + `Option` + `I`, then `E`
    

This shortcut quickly opens the equation editor without clicking through menus.

**Toolbar Symbols:**

Once the toolbar appears, you’ll find buttons for:

* Greek letters
    
* Miscellaneous operations
    
* Relations
    
* Math operations
    
* Arrows
    

The equation editor box and a toolbar look like the following:

![Google Docs Equation Editor and Toolbar](https://cdn.hashnode.com/res/hashnode/image/upload/v1747198733591/9defa152-16a5-42a1-b098-228a9d1f7f79.png align="center")

Now let’s learn how to write equations using the equation editor with a practical example.

### Example: Typing the Quadratic Formula

Follow these steps to insert the following quadratic formula in Google Docs:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

1. Go to *Insert* → *Equation* to insert an equation editor and enable the equation toolbar.
    
2. Type `x=`
    
3. Click the Math Operations dropdown (the one with templates like square roots, brackets), then select the fraction template. This inserts a placeholder with two parts: a numerator and a denominator.
    
    ![Screenshot of Google Docs displaying a feature to insert math equations. A dropdown menu shows various mathematical symbols like fractions, square roots, and integrals. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1747199319708/142157c9-f997-494a-be4a-efb619b7c12d.png align="center")
    
4. Click inside the numerator field. Begin by typing `-b`.
    
5. Now insert the ± (plus-minus) symbol. To do this:
    
    * Click the Miscellaneous Operations dropdown
        
    * Select the ± symbol from the list.  
        Your numerator should now show: `-b ±` as in the following image:
        
    * ![Screenshot of Google Docs showing a math equation being edited with the equation toolbar open. Various symbols are visible on the toolbar, and part of a quadratic formula is visible in the document area.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747199567908/be5daee7-2ed2-4c86-be16-d90e033a05be.png align="center")
        
6. After the ± symbol, insert a square root:
    
    * Go back to the Math Operations dropdown and select the square root template.
        
    * Inside the root, type `b^2 - 4ac`.
        
        * Use `^` to enter exponents. For example, `b^2` will be rendered as *b²*.
            
            ![Screenshot of Google Docs showing a math equation being inserted. A dropdown menu displays mathematical symbols like fractions, square roots, and integrals. A formula for the quadratic equation is in the document area on the right.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747199681755/cc2084c2-5856-4999-9905-d825b5c276d9.png align="center")
            
7. Move to the denominator field and type `2a`.
    

Now your full equation should appear as:

![Screenshot of Google Docs showing an open document. It has menu options at the top and a formula for the quadratic equation displayed on the page.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747199739733/2c1ef4f8-9730-491f-9120-5ba6daee41c3.png align="center")

The equation will be properly formatted using Google Docs’ equation rendering, making it easy to read and mathematically accurate. You can continue typing more text below or beside the equation as needed – it behaves like any other element in your document.

This approach is useful for inserting neatly formatted equations without relying on add-ons or external tools. It’s especially helpful for students, teachers, and professionals preparing technical documents directly in Google Docs.

## How to Write Equations Using LaTeX Commands

If you're familiar with [**LaTeX**](https://www.latex-project.org/), you can take advantage of Google Docs’ support for a subset of LaTeX-style commands inside the built-in equation editor. This can greatly speed up the process of entering complex mathematical expressions, especially if you're already comfortable with LaTeX syntax.

### How to Use LaTeX Commands in Google Docs

1. Open your Google Docs document.
    
2. Go to Insert → Equation to activate the equation toolbar and equation input field.
    
3. Click inside the equation box. Instead of using the toolbar buttons, type LaTeX-style commands directly.
    
4. As you type, Google Docs will automatically render the commands into formatted math once you press space or enter after each command or expression.
    

#### Commonly Supported LaTeX Commands in Google Docs:

| **Instruction** | **Result** |
| --- | --- |
| To insert a fraction | `\frac{a}{b}` → 𝑎⁄𝑏 |
| To insert a square root | `\sqrt{x}` → √𝑥 |
| To insert Greek letters like α, β | `\alpha, \beta` → α, β |
| To insert an integral with limits | `\int_a^b f(x)\,dx` → ∫ᵃᵇ 𝑓(𝑥) 𝑑𝑥 |
| To insert x superscript 2 | `x^2` → 𝑥² |
| To insert x subscript 1 | `x_1` → 𝑥₁ |

Type these commands in the equation box, and when you press space or enter, they will be converted to properly formatted mathematical notation.

#### Example: Typing the Quadratic Formula Using LaTeX Commands

Let’s walk through how to enter the following quadratic formula using LaTeX-style commands:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Steps:**

1. Insert the equation box: Go to Insert → Equation.
    
2. In the equation input area, type the following:
    

```javascript
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

* `\frac` creates a fraction.
    
* `-b` is the numerator’s first term.
    
* `\pm` inserts the plus-minus symbol.
    
* `\sqrt` creates a square root.
    
* `b^2` formats *b squared*.
    
* `- 4ac` is written normally inside the square root.
    
* `2a` is the denominator.
    

3. As you type, press space or enter after each LaTeX command. Google Docs will automatically convert the code into properly formatted math notation.
    

After rendering, the equation will appear as:

![A Google Docs interface showing the quadratic formula being entered as a math equation](https://cdn.hashnode.com/res/hashnode/image/upload/v1747199739733/2c1ef4f8-9730-491f-9120-5ba6daee41c3.png align="left")

This method is ideal for users who prefer keyboard-based input over clicking toolbar icons. It also allows you to enter complex expressions faster and more accurately, especially if you're familiar with standard LaTeX syntax.

#### Notes:

* Not all LaTeX features are supported in Google Docs. The supported commands are limited to basic math formatting, Greek letters, and common symbols.
    
* Make sure to press **space** after each LaTeX command so that Docs knows to render it.
    

## How to Use Auto Latex Add-on for Writing Advanced Math Equations

When generating mathematical content using tools like ChatGPT, you'll notice that equations are **rendered visually on the webpage**, but behind the scenes they’re created using [LaTeX](https://www.latex-project.org/) code. So when you copy content from ChatGPT into Google Docs, the equations come through as raw LaTeX code rather than rendered math expressions.

For example, a quadratic formula provided by ChatGPT might look like this when pasted into your document:

```javascript
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

While this format is ideal for precision, Google Docs doesn’t support LaTeX rendering by default.

This is where the **Auto-LaTeX Equations** add-on becomes essential, especially if you're moving content from [ChatGPT to Google Docs](https://www.docstomarkdown.pro/chatgpt-to-google-docs/). It’s also incredibly useful when importing LaTeX-based documents into Google Docs, such as content originally written in [Overleaf](https://overleaf.com/) or other LaTeX editors.

Instead of manually reformatting equations, the add-on automatically renders LaTeX code into properly formatted math equations, preserving the typesetting and structure you’d expect from a LaTeX environment.

### What is Auto-LaTeX Equations?

[**Auto-LaTeX Equations**](https://workspace.google.com/marketplace/app/autolatex_equations/850293439076) is a free and open-source Google Docs add-on that scans your document for LaTeX expressions and converts them into a properly formatted equations.

It recognizes LaTeX code wrapped in these delimiters:

* Inline: `$$ ... $$`
    
* Display: `\[ ... \]`
    

Once detected, it renders the equations seamlessly within your document, eliminating the need to retype or manually format them.

1. Paste your LaTeX expression into the Google Docs document. Make sure the expression is enclosed using one of the supported delimiters:
    
    `$$ ... $$ or \[ ... \]`
    
2. Open the add-on sidebar by clicking Extensions **→** Auto-LaTeX Equations **→** Start.
    
3. Once the sidebar opens, you’ll see a dropdown labeled “Delimiters” and a button called “Render Equations.”
    
4. Select the delimiter you used when enclosing your LaTeX equations – for example, `$$` or `\[ \]`.
    
5. Click the “Render Equations” button.
    

![Auto Latex Equations add-on sidebar](https://cdn.hashnode.com/res/hashnode/image/upload/v1747203253430/e96fe9ac-ccba-4ed5-ab10-1e759d737d7d.png align="center")

The add-on will automatically scan your document and convert all valid LaTeX expressions into properly formatted equation images.

This step-by-step process allows you to take any LaTeX-based math copied from ChatGPT and render it cleanly within Google Docs – ready for export to Word or PDF.

### Example: Converting a LaTeX coded Equation to Rendered Math Equations

Paste the following equation into Google Docs:

`$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$`

To convert it:

1. Go to Extensions → Auto-LaTeX Equations → Start.
    
2. Select the Delimitor as `$$` ..`$$` and click on the Render Equations button. The equation will be rendered and look as follows:
    

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

#### How to Install Auto-LaTeX Equations

1. In Google Docs, click Extensions → Add-ons → Get add-ons.
    
2. Search for Auto-LaTeX Equations.
    
3. Click Install and follow the prompts.
    
4. After installation, access it from Extensions → Auto-LaTeX Equations.
    

## How to Copy Math Equations from ChatGPT to Google Docs

To easily transfer math equations and the surrounding content from ChatGPT into Google Docs without losing formatting, use the free [**ChatGPT to Google Docs or PDF**](https://chromewebstore.google.com/detail/chatgpt-to-google-docs-or/oibghjgooccojibfacdonaoipegckdeg) Chrome extension.

This extension allows you to:

* Export a single response (with equations and tables) into Google Docs while preserving formatting
    
* Export an entire conversation, including math, code, and text, into a clean, one organized Google Docs, no need to export responses separately and [merge multiple Google Docs into one](https://www.freecodecamp.org/news/merge-multiple-google-docs-with-apps-script-or-google-docs-api/) later
    
* Save ChatGPT canvas content as a Google Docs or PDF
    
* Export ChatGPT deep research documents directly into Google Docs
    
* Export [ChatGPT content directly into PDF format](https://www.docstomarkdown.pro/chatgpt-to-pdf/) when no further edits are necessary, eliminating the need to first export to Google Docs and then convert [Google Docs to PDF](https://workspace.google.com/marketplace/app/docs_to_pdf_pro/302636103705)
    

It’s especially useful for students, researchers, and professionals who want to keep their AI-generated math, notes, and research well-organized in Google Docs or PDF format with minimal effort.

## Watch: How to Write Equations in Google Docs

If you prefer visual learning, here’s a helpful video walkthrough that demonstrates all the methods discussed above – using the built-in equation editor, LaTeX-like commands, and the Auto-LaTeX Equations add-on.

This step-by-step tutorial covers:

* Opening and using the built-in equation toolbar
    
* Typing LaTeX-style commands directly in the equation editor
    
* Converting AI-generated LaTeX (e.g., from ChatGPT) into clean equations
    

%[https://www.youtube.com/watch?v=Y_2q45Qscp0] 

## Tips for Formatting Math Equations in Google Docs

**Use inline equations when:**

* Inserting short expressions like `x²`, `a/b`, or single variables
    
* Including math within a sentence to maintain the flow of text
    

**Use block equations when:**

* Writing complex or multi-line formulas (e.g., the quadratic formula)
    
* You want the equation to be clearly separated from the surrounding text for readability
    

**Wrapping tips for rendered equations:**

* Rendered equations are treated as images in Google Docs, which may disrupt the document layout if not positioned correctly
    
* To fix this:
    
    * Click the equation image
        
    * Choose from:
        
        * **In line** – aligns the equation with surrounding text (best for inline use)
            
        * **Wrap text** – wraps paragraph text around the equation image
            
        * **Break text** – places the equation on its own line, isolating it
            
    * Use the margin handles or spacing options to fine-tune the layout and prevent overlap or crowding
        

## Conclusion

Google Docs offers several flexible ways to write and manage math equations:

* **Use the built-in equation editor** for basic symbols, fractions, exponents, and common operations. It’s easy to access and great for straightforward math tasks without needing special syntax.
    
* **Try LaTeX-like commands** inside the equation editor for faster input. You can type commands like `\frac`, `\sqrt`, or `\alpha` to quickly insert structured equations without navigating menus.
    
* **Install add-ons like Auto-LaTeX Equations** for advanced LaTeX rendering. This is especially useful if you're copying equations from Overleaf, ChatGPT, or LaTeX documents into Google Docs, as it preserves formatting and converts code into clean equation images.
    
* **Use external tools when copying from other formats**, like the *ChatGPT to Google Docs or PDF* Chrome extension, which helps retain equation formatting when moving content from ChatGPT or other platforms.
    

Whether you’re completing math homework, preparing teaching materials, or writing a research paper, Google Docs, combined with these tools, gives you everything you need to create clear, professional-looking documents with math content.
