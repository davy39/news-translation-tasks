---
title: 'How to Use the JavaScript Selection API: Build a Rich Text Editor and Real-Time
  Element Detection'
subtitle: ''
author: Asfak Ahmed
co_authors: []
series: null
date: '2024-09-16T16:19:02.904Z'
originalURL: https://freecodecamp.org/news/use-the-javascript-selection-api-to-build-a-rich-text-editor
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726225376443/ae5d57c8-e79e-4dc4-b218-c3a5e34f8293.png
tags:
- name: selection api
  slug: selection-api
- name: element detection
  slug: element-detection
- name: JavaScript
  slug: javascript
- name: '#richtext'
  slug: richtext
- name: ' DOM In JavaScript'
  slug: dom-in-javascript
- name: JavaScript event handling
  slug: javascript-event-handling
seo_title: null
seo_desc: When you interact with web pages, a common task you’ll perform often is
  selecting text. Whether it's highlighting a section of a paragraph to copy, marking
  important parts of a document, or working with interactive features like note-taking
  or text e...
---

When you interact with web pages, a common task you’ll perform often is selecting text. Whether it's highlighting a section of a paragraph to copy, marking important parts of a document, or working with interactive features like note-taking or text editing, text selections are part of our everyday browsing experience.

The JavaScript **Selection API** is what makes it possible to interact programmatically with these text selections.

In this tutorial, we'll dive deep into the Selection API, explore what it can do, and demonstrate how you can use it to create interactive, selection-based web applications.

### In this article, we will cover:

* [Explore the JavaScript Selection API, a powerful tool for interacting with and manipulating user-selected text on a web page.](#heading-what-is-the-selection-api)
    
* [Introduce document.execCommand(), an easy-to-use method for adding formatting to selected text, including bold, italic, and underline.](#heading-the-documentexeccommand-function)
    
* [Demonstrate how to build a simple rich text editor with basic formatting features using both the Selection API and execCommand().](#heading-example-use-case-how-to-build-a-rich-text-editor-with-the-javascript-selection-api)
    
* [Detect clicked elements and their positions in real time.](#heading-how-to-get-the-clicked-element-and-its-real-time-position)
    

## What is the Selection API?

The **Selection API** is a web API provided by modern browsers that enables developers to work with user text selections on a web page. It allows you to:

1. Get details about the currently selected text.
    
2. Modify or manipulate selections programmatically.
    
3. Detect when users make a selection.
    
4. Store, replace, or delete selections of text.
    

This API is commonly used for rich text editors, copy/paste functionality, custom tooltips, highlighting, annotations, and more.

## What Can You Do Using the Selection API?

The Selection API gives you the power to interact with user-selected text in a variety of ways. Some key capabilities include:

1. **Get the currently selected text**: Extract the highlighted text that the user selects in the document.
    
2. **Modify the selection**: Programmatically set or modify a selection, either by setting new start and end points for the selection or collapsing it entirely.
    
3. **Remove the selection**: Clear a selection once you're done using it.
    
4. **Extract position information**: Know where the selection begins and ends, both within the document and on the screen (useful for custom tooltips or annotations).
    
5. **Apply custom styling**: You can style the selected text, add highlights, or trigger events when a user makes a selection.
    

## Key Components of the Selection API

To effectively use the Selection API, it's important to understand some of its core concepts. Here are the key objects and methods:

### **1\.** `Selection` **Object**

The `Selection` object represents the current selection of text on a web page. It’s accessible through the `window.getSelection()` method and is the core object you’ll interact with.

```typescript
const selection = window.getSelection();
console.log(selection);
```

The `Selection` object provides multiple properties and methods to retrieve, modify, and manipulate user-selected text.

### **2\.** `Range` **Object**

The `Range` object represents a fragment of a document. It holds information about the start and end points of a selection and allows you to manipulate portions of the document.

For example, you can create a range to highlight or manipulate specific text nodes or retrieve the text content within a certain range.

```typescript
const selection = window.getSelection();
const range = selection.getRangeAt(0); // Get the first range of the selection
console.log(range);
```

## Key Methods and Properties of the Selection API

Here’s a breakdown of the most commonly used methods and properties of the **Selection API** and the **Range API**:

### **Selection API Methods:**

#### 1\. `window.getSelection()`:

The `window.getSelection()` method is used to retrieve the current text selection on the webpage. It returns an `Selection` object, which represents the range of text selected by the user, or the caret's current position (if no text is selected).

**Details about** `window.getSelection()`**:**

The `Selection` object contains details about the currently selected text (if any), including the start and end nodes, offsets, and methods for manipulating the selection.

If no text is selected, the `Selection` the object will reflect the caret's current position without any selected range.

**Example Code:**

```typescript
const selection = window.getSelection();
console.log(selection);  // Logs the Selection object to the console
```

**Example Usage:**

Check if any text is selected:

```typescript
const selection = window.getSelection();
if (selection.rangeCount > 0) {
    console.log('Text is selected');
} else {
    console.log('No text selected');
}
```

This checks if any text is selected by verifying if `rangeCount` (the number of text ranges) is greater than zero.

#### 2\. `Selection.anchorNode` **and** `Selection.focusNode`**:**

`anchorNode` represents the node where the user started the selection. It's the starting point of the selection, although visually it could be at the end depending on the user's drag direction.

`focusNode` represents the node where the user ended the selection. It's the ending point of the selection, but again, this could visually appear as the start of the selection if the user selected backward.

**Important details:**

* **Selection direction**: If the selection is made left-to-right (dragging forward), this `anchorNode` will be the earlier part of the selection. If the selection is made right-to-left (dragging backward), the `anchorNode` will be at the later part of the selection, but the focus will appear first.
    
* **Node types**: Both `anchorNode` and `focusNode` return DOM nodes. This means they can be text nodes, element nodes, or any other type of node within the document.
    
* **Offsets**: Along with these properties, `Selection.anchorOffset` and `Selection.focusOffset` give you the exact character offset within the nodes where the selection starts and ends.
    

#### 3\. `Selection.toString()`:

To use the `Selection.toString()` method, you can simply call it on the current selection. This method returns the string value of the currently selected text in the document.

```typescript
const selectedText = selection.toString();
console.log(selectedText);  // Output: The selected text
```

**How it works:**

1. `window.getSelection()`: This retrieves the current `Selection` object representing the user-selected text.
    
2. `.toString()`: This converts the selected range to a plain string of text.
    
3. The result is then printed to the console.
    

#### 4\. `Selection.removeAllRanges()`:

The `Selection.removeAllRanges()` method is used to clear or remove any current text selection on a webpage. When called, it deselects any text that the user may have selected, leaving the selection empty.

```typescript
selection.removeAllRanges();
```

**How it works:**

* `window.getSelection()`: Retrieves the current `Selection` object.
    
* `.removeAllRanges()`: Clears the selection, effectively deselecting any highlighted text on the page.
    

#### 5\. `Selection.addRange(range)`:

The `Selection.addRange(range)` method is used to add a specific `Range` object to the current selection in the document. This allows you to programmatically select a range of text or elements.

```typescript
// Create a range object
const range = document.createRange();

// Select a specific element or part of the document
const element = document.getElementById('myElement');

// Set the range to start at the beginning of the element and end at the end
range.selectNodeContents(element);

// Clear any existing selection and add the new range
const selection = window.getSelection();
selection.removeAllRanges();  // Remove existing selections
selection.addRange(range);  // Add the new range
```

**How it works:**

1. `document.createRange()`: Creates a new `Range` object.
    
2. `range.selectNodeContents()`: Sets the range to cover the contents of a specific DOM element (in this case, the element with ID `myElement`).
    
3. `selection.removeAllRanges()`: Clears any previously selected text or elements.
    
4. `selection.addRange(range)`: Adds the definition `Range` to the selection, making it the currently selected text or content.
    

**Use Cases:**

* **Programmatically Select Text**: If you want to highlight specific parts of the document programmatically, you can use this method to select them.
    
* **Custom Selection Logic**: In web applications that require specific text or element selections, such as editors or custom UI tools, this can be used to manage user selections.
    

### **Range API Methods:**

#### 1\. `range.setStart(node, offset)`:

The `Range.setStart(node, offset)` method is used to set the starting point of an `Range` object. You specify `node` where the range should start and the `offset` (position within the node) for the starting point.

**Parameters:**

* `node`: The DOM node where the range should start. It can be an element node or a text node.
    
* `offset`: The position within the node where the range starts. For element nodes, this is the index of child nodes. For text nodes, it's the character position within the text.
    

```typescript
// Create a range object
const range = document.createRange();

// Select the text node where the range should start
const textNode = document.getElementById('myElement').firstChild;

// Set the start of the range at the 5th character in the text node
range.setStart(textNode, 5);
```

**Code explanation:**

1. `document.createRange()`: Creates a new `Range` object.
    
2. `textNode`: This refers to the first child of the element with ID `myElement`, which is expected to be a text node.
    
3. `range.setStart(textNode, 5)`: Sets the start of the range at the 5th character in the text node.
    

**Important notes:**

* In **text nodes**, the `offset` refers to the position of a character within the text. For example, `offset = 5` means the range starts after the 5th character.
    
* In **element nodes**, the `offset` refers to the index of child nodes. For instance, `offset = 0` would start before the first child element, while `offset = 1` would start after the first child.
    

**Example use case:**

You could use `setStart` in a scenario where you want to highlight or extract part of some text, starting at a specific point:

```typescript
const range = document.createRange();
const textNode = document.getElementById('myText').firstChild;
range.setStart(textNode, 3); // Start at the 4th character
range.setEnd(textNode, 8);   // End at the 9th character

const selection = window.getSelection();
selection.removeAllRanges(); // Clear previous selections
selection.addRange(range);   // Highlight the selected text
```

In this example, it selects the text starting from the 4th character and ending at the 9th character, effectively highlighting that part of the text.

#### 2\. `range.cloneContents()`:

The `Range.cloneContents()` method is used to create a copy of the content within the specified range. It returns a `DocumentFragment` containing the nodes and content from the range but does not modify the original document.

**Key details:**

* **Returns**: A `DocumentFragment` that contains the cloned nodes and elements within the range.
    
* **Non-destructive**: This method does not alter or remove the content from the original document – it simply creates a copy.
    

**Example code:**

```typescript
// Create a range object
const range = document.createRange();

// Select the content of a specific element
const element = document.getElementById('myElement');
range.selectNodeContents(element);

// Clone the contents of the range
const clonedContent = range.cloneContents();

// Append the cloned content somewhere in the document
document.body.appendChild(clonedContent);
```

**How it works:**

1. `document.createRange()`: Creates a new `Range` object.
    
2. `range.selectNodeContents(element)`: Selects all the content within the specified element.
    
3. `range.cloneContents()`: Creates a `DocumentFragment` that contains a copy of the selected contents.
    
4. `document.body.appendChild(clonedContent)`: Appends the cloned content somewhere in the document (in this case, at the end of the body).
    

**Use cases:**

1. **Duplicating Content**: Use this method when you need to create a copy of selected content without altering the original.
    
2. **Manipulating Copied Data**: After cloning the contents, you can modify or process the cloned fragment (for example, for drag-and-drop features, custom tooltips, or saving a portion of content).
    

**Example scenario:**

If you want to copy part of a webpage’s content and display it elsewhere:

```typescript
const range = document.createRange();
const element = document.querySelector('#textElement');
range.setStart(element.firstChild, 0);  // Set start of range
range.setEnd(element.firstChild, 10);   // Set end of range (first 10 characters)

// Clone the content and append it to another element
const clonedContent = range.cloneContents();
document.querySelector('#targetElement').appendChild(clonedContent);
```

In this example, the first 10 characters `#textElement` are cloned and inserted into `#targetElement`. This does not affect the original content in `#textElement`.

### Use Cases of the Selection API

#### 1\. Highlighting text

Using the Selection API, you can highlight text dynamically based on user input. For example, you can wrap the selected text in a `<mark>` tag to highlight it.

```xml
<p id="text">This is some selectable text.</p>
<button onclick="highlightSelection()">Highlight</button>

<script>
function highlightSelection() {
    const selection = window.getSelection();
    if (selection.rangeCount > 0) {
        const range = selection.getRangeAt(0);
        const highlight = document.createElement('mark');
        range.surroundContents(highlight);
    }
}
</script>
```

This script allows users to highlight the selected text with a simple click.

#### 2\. Copying selected text

You can easily extract and manipulate the selected text with the `Selection.toString()` method. Here’s an example of copying the selected text to the clipboard:

```xml
<p id="text">Select any portion of this text and copy it to the clipboard.</p>
<button onclick="copySelection()">Copy</button>

<script>
function copySelection() {
    const selection = window.getSelection();
    const text = selection.toString();
    
    navigator.clipboard.writeText(text).then(() => {
        alert("Copied to clipboard: " + text);
    });
}
</script>
```

This snippet allows users to copy any selected text and paste it elsewhere.

#### 3\. Annotating text

You can combine the Selection API with custom annotations. You can display a floating tooltip or annotation box by detecting the selection’s position on the page.

```xml
<p>Select text to see the annotation box.</p>

<script>
document.addEventListener("mouseup", () => {
    const selection = window.getSelection();
    const selectedText = selection.toString();
    
    if (selectedText.length > 0) {
        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        
        const annotationBox = document.createElement("div");
        annotationBox.style.position = "absolute";
        annotationBox.style.left = `${rect.left}px`;
        annotationBox.style.top = `${rect.top - 30}px`;
        annotationBox.textContent = "Annotate this!";
        document.body.appendChild(annotationBox);
    }
});
</script>
```

This script creates an annotation box just above the selected text.

### Advanced Features of the Selection API

1. **Multiple Ranges**: Some browsers support multiple text selections on a single page, where you can select multiple text ranges and manipulate them simultaneously.
    
2. **Detecting Selection Changes**: You can listen for `selectionchange` events on the document, allowing you to detect when the user changes their selection.
    
    ```typescript
    document.addEventListener("selectionchange", () => {
        const selection = window.getSelection();
        console.log("Selection changed:", selection.toString());
    });
    ```
    
3. **Working with Forms**: Selections can be useful in forms, allowing you to auto-complete, copy, or validate the user’s input based on selected text.
    

The **JavaScript Selection API** is a powerful tool for creating dynamic and interactive web applications. Whether you want to implement custom copy/paste functionality, enable annotations, or build advanced text editors, the Selection API provides the control and flexibility you need to handle user selections.

With its easy-to-use methods and properties, you can enhance user experiences and create intuitive, selection-based features.

## Example Use Case: How to Build a Rich Text Editor with the JavaScript Selection API

The Selection API not only allows you to interact with text selections but also opens the door to more advanced text manipulation, like creating a **rich text editor**. A rich text editor (RTE) allows users to format selected text with features such as bold, italic, and underline.

In this section, we'll walk through how to build a basic rich text editor using the Selection API and provide an example with key formatting features.

### How Does the Selection API Help Build a Rich Text Editor?

The Selection API lets you:

* Detect the text selected by the user.
    
* Programmatically modify the selected content, for example, applying bold, italic, or underlined styling.
    
* Allow users to make in-place edits with simple UI controls (like buttons or keyboard shortcuts).
    

By using the `window.getSelection()` and Range API, you can manipulate text based on user actions (such as clicking a "Bold" button). You can then wrap the selected text in appropriate HTML tags (`<b>`, `<i>`, `<u>`) or apply inline styles.

### Basic Rich Text Editor Features

For our example, we'll implement three core formatting features:

1. **Bold**: Make the selected text bold.
    
2. **Italic**: Italicize the selected text.
    
3. **Underline**: Underline the selected text.
    

#### HTML Structure

Here’s a simple layout for the editor with buttons for Bold, Italic, and Underline:

```xml
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple Rich Text Editor</title>
  <style>
    #editor {
      border: 1px solid #ccc;
      min-height: 150px;
      padding: 10px;
      margin-top: 10px;
    }
    .toolbar {
      margin-bottom: 5px;
    }
    .toolbar button {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <div class="toolbar">
    <button onclick="formatText('bold')"><b>Bold</b></button>
    <button onclick="formatText('italic')"><i>Italic</i></button>
    <button onclick="formatText('underline')"><u>Underline</u></button>
  </div>

  <!-- Contenteditable div for the editor -->
  <div id="editor" contenteditable="true">
    Type your text here...
  </div>

  <script src="editor.js"></script>
</body>
</html>
```

#### JavaScript: Handling Formatting with the Selection API

Now that we have the basic structure, let's add JavaScript to handle text formatting. We’ll use the **Selection API** and `document.execCommand()`, a legacy method still supported by most browsers, to apply formatting.

Here’s the JavaScript to make the buttons functional:

```typescript
// Function to format text based on the command
function formatText(command) {
  document.execCommand(command, false, null);
}
```

The `execCommand` method allows you to perform commands on the content inside an element that has the `contenteditable` attribute. In our case, the commands will be `'bold'`, `'italic'`, and `'underline'`.

### The `document.execCommand()` Function

The `document.execCommand()` function is a legacy method provided by browsers that allows developers to perform various document editing operations directly on content within an `contenteditable` element. This method has been widely used to build rich text editors for web applications due to its simplicity and browser support.

Though it's still functional in most modern browsers, it's worth noting that `execCommand` has been deprecated and may not be supported in future versions of browsers. But it still provides a good starting point for basic rich text editors.

If you're looking for a long-term solution, newer APIs like the Selection API combined with Range API or third-party libraries (like Quill.js and Draft.js) are recommended for complex editing needs.

### What is `document.execCommand()`?

The `document.execCommand()` the method executes a specified command for manipulating or formatting text in a **contenteditable** element (such as a div, textarea, or input field). It can perform commands such as applying styles, modifying text alignment, creating links, and much more.

#### Syntax of the `execCommand()`:

```typescript
document.execCommand(command, showUI, value);
```

* `command`: A string that represents the command to execute (for example, `'bold'`, `'italic'`, `'underline'`, `'createLink'`).
    
* `showUI`: A boolean value indicating whether the default user interface for the command should be shown (almost always `false`, as browser UIs are often inconsistent).
    
* `value`: Optional. A string representing the value to pass for certain commands (for example, the URL for creating a link).
    

#### Return Value

`execCommand()` returns `true` if the command is successfully executed or `false` otherwise.

### How to Enhance the Rich Text Editor

While the example above gives you a basic rich text editor, you can expand its features by adding more controls and handling other commands:

* **Text Color**: Change the color of the selected text using `execCommand('foreColor', false, 'red')`.
    
* **Text Alignment**: Align text left, center, or right using commands like `execCommand('justifyCenter')`.
    
* **Undo/Redo**: Implement undo and redo functionality using `execCommand('undo')` and `execCommand('redo')`.
    
* **Adding Links**: Allow users to add links with `execCommand('createLink', false, '`[`http://example.com`](http://example.com)`')`.
    

Using the Selection API combined with `document.execCommand()`, we’ve built a simple, yet functional rich text editor with bold, italic, and underline features. This basic editor can be further enhanced with additional features like font size, color, and alignment to create a full-fledged rich text editor for your web applications.

### **How to Get the Clicked Element and its Real-Time Position**

The simplest way to detect the clicked element in a webpage is by using the `click` event listener in JavaScript.

Here's how you can do it:

```typescript
document.addEventListener('click', (event) => {
    const clickedElement = event.target;
    console.log('You clicked on:', clickedElement.tagName);
});
```

#### Code explanation:

* `document.addEventListener('click', ...)`: This attaches an event listener to the whole document.
    
* [`event.target`](http://event.target): This property returns the specific element that was clicked.
    
* `clickedElement.tagName`: This provides the tag name of the clicked element (like `DIV`, `SPAN`, `BUTTON`, etc.).
    

This will log the element’s tag name to the console when you click anywhere on the document.

### **How to Get the Element's Realtime Position**

Once you have the clicked element, you can find its position on the screen using JavaScript’s DOM API. Specifically, `getBoundingClientRect()` gives us the element's position relative to the viewport.

```typescript
document.addEventListener('click', (event) => {
    const clickedElement = event.target;
    const position = clickedElement.getBoundingClientRect();

    console.log(`Element: ${clickedElement.tagName}`);
    console.log(`Position: Top - ${position.top}px, Left - ${position.left}px`);
});
```

#### Code explanation:

* `getBoundingClientRect()`: This method returns the size of an element and its position relative to the viewport. It gives you several useful properties:
    
    * `top`: Distance from the top of the viewport.
        
    * `left`: Distance from the left of the viewport.
        
    * `right`: Distance from the left edge to the right edge of the element.
        
    * `bottom`: Distance from the top edge to the bottom edge of the element.
        

The `top` and `left` values are usually the most useful, as they tell you where the element is positioned.

### **Full Example with Code**

Let’s put everything together. We’ll create an interactive example where clicking on any element displays its tag name and position in a tooltip-like fashion.

Here’s the complete code:

```xml
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detect Clicked Element and Position</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .tooltip {
            position: absolute;
            background-color: #333;
            color: #fff;
            padding: 5px;
            border-radius: 5px;
            font-size: 12px;
            display: none;
        }
    </style>
</head>
<body>

<div class="tooltip" id="tooltip"></div>

<h1>Click on elements to see their tag and position</h1>
<p>This is a paragraph. Click on it!</p>
<button>Click me</button>
<div style="width: 100px; height: 100px; background-color: lightblue;">Click this box</div>

<script>
    const tooltip = document.getElementById('tooltip');

    document.addEventListener('click', (event) => {
        const clickedElement = event.target;
        const position = clickedElement.getBoundingClientRect();
        
        // Get the tag name of the clicked element
        const elementTag = clickedElement.tagName;

        // Get the element's current position
        const top = position.top + window.scrollY; // Account for page scroll
        const left = position.left + window.scrollX;

        // Display the tooltip near the clicked element
        tooltip.innerHTML = `Tag: ${elementTag}<br>Position: Top - ${Math.round(top)}px, Left - ${Math.round(left)}px`;
        tooltip.style.display = 'block';
        tooltip.style.top = `${top + 20}px`; // Offset to position below the element
        tooltip.style.left = `${left + 20}px`; // Offset to position to the right of the element
    });

    document.addEventListener('scroll', () => {
        tooltip.style.display = 'none'; // Hide the tooltip when the user scrolls
    });
</script>

</body>
</html>
```

#### Code explanation:

1. **HTML structure**:
    
    * The `tooltip` div is initially hidden but will be shown dynamically when a user clicks on an element.
        
    * We’ve included some clickable elements (`h1`, `p`, `button`, `div`) for demonstration purposes.
        
2. **JavaScript**:
    
    * When any element is clicked, we calculate its tag name and position using [`event.target`](http://event.target) and `getBoundingClientRect()`.
        
    * We update the `tooltip` content and move it dynamically based on the element’s position.
        
    * `window.scrollY` and `window.scrollX` are added to account for any scrolling that has occurred on the page.
        
3. **CSS**:
    
    * The tooltip is styled as a small box with a dark background and white text. It is initially hidden (`display: none`).
        
    * When an element is clicked, the tooltip is positioned near the clicked element by adjusting its `top` and `left` styles.
        

### Live Example:

Click anywhere on the webpage, and you’ll see the tag name and position of the clicked element displayed in a tooltip. This method is beneficial for creating custom interactions, debugging, or handling complex layouts in modern web applications.

## Wrapping Up

In this tutorial, we explored how to use the **JavaScript Selection API** to interact with text the user selects and manipulate it programmatically. We also learned about the `document.execCommand()` function, which, despite being deprecated, allows us to apply basic text formatting like bold, italic, and underline to the selected content.

We demonstrated how to build a simple rich text editor with basic features using these tools. We also covered how to detect which HTML element was clicked by using the `click` event and accessing the [`event.target`](http://event.target) property.

These techniques form the foundation for creating dynamic, interactive web text editors.
