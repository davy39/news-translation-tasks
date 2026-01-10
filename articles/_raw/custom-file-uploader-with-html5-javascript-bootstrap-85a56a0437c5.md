---
title: How to build a custom file uploader with HTML5, JavaScript, & Bootstrap
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-07T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/custom-file-uploader-with-html5-javascript-bootstrap-85a56a0437c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B6zah6pnLHvaYJ1Gppp-hQ.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Prashant Yadav

  In this short article, we’ll learn how to create custom file uploader with JQuery,
  ES6, and Bootstrap4.

  We will create a file uploader with a custom design and an option to preview selected
  files and remove them.

  Support me by readi...'
---

By Prashant Yadav

In this short article, we’ll learn how to create custom file uploader with JQuery, [ES6](https://learnersbucket.com/tutorials/es6/es6-intro), and Bootstrap4.

We will create a file uploader with a custom design and an option to preview selected files and remove them.

_Support me by reading this article [here](https://learnersbucket.com/examples/bootstrap4/custom-fileuploader-in-javascript/)._

### Demo

Check out the live demo [here](https://codepen.io/Learnersbucket/pen/drWENz).

### Implementation

* We will use the html5 file uploader to upload the files.
* Then, with the help of Bootstrap popover, we will preview the selected files.
* While previewing the files, we will provide an option to remove the selected file.
* As JQuery is one of the dependencies for Bootstrap popover, we will use it to ease our work.

### Dependencies

### HTML layout for file uploader

Explanation

* We have created a container named `custom-file-picker`.
* In this, we have our custom file upload `picture-container` and our popover previewer `popover-container`.
* Every file picker has a unique id `a8755cf0-f4d1-6376-ee21-a6defd1e7c08` and its corresponding popover refers to that id `data-target="a8755cf0-f4d1-6376-ee21-a6defd1e7c08"` to preview the files.

### Styling our components

### Handling the functionality

Now that we have styled our components, it is time to handle the functionality. We will use Jquery with [ES6](https://learnersbucket.com/tutorials/es6/es6-intro) to make things easy.

### Storing the files

We will create a global variable to store the files.

We will use this variable to store all the files of the corresponding file picker with the help of its id.

Now we will create a function which will manage the storing of the file and displaying the count of the files. This function will take `id` and `array of files` as input.

`$(`[data-id="${id}"] > .file-total-viewer`).text(files.lengt`h); will update the file count in popover previewer.

### Handling the file picking

We have our function ready to update the count and store the files. We will just pass data to this function once the files are selected or changed.

Once the files are selected we will show the complete animation with SVG to notify users that files are changed.

Right now we have our file stored and the count visible. Let's create the file previewer with a bootstrap popover.

Bootstrap provides us a method to dynamically generate the content of the popover. So we attach the popover to `[data-toggle="popover"]`. Learn more about it [here](https://getbootstrap.com/docs/4.1/components/popovers/).

#### How it works

* Every time a popup is about to render it will use its `[data-target]` id and pull all the files from the `fileStorage`.
* If there are files, then render those files along with the delete button.
* If there is no file, then show some message.

Now in case you have multiple file uploaders and you want only one popover to be open at a time, add the following code.

If you select some file and click on `view` you should be able to view it. Now the last thing we will do is handle the deletion of files.

### Deleting the file

We have provided the id of the file picker to the delete button through `data-target` and the name of the file through `data-name`. Every time the delete icon is clicked we will use these values to remove the files.

As we are dynamically generating the content of the popover and it does not already exist in the DOM, we cannot assign an event to it. So we have to use a workaround of assigning an event on the DOM and checking if the delete icon is clicked with `$(document).on('click', '.popover-content-remove', function (e) {});`.

#### How it works

* Once the delete icon is clicked we will ask for confirmation from the user.
* If the user wants to proceed, then we fetch the id and the name assigned to delete button through `data-target` and `data-name`.
* We remove that particular file using filter() method.
* Once the file is removed from the array, then we update its count by passing the value to our helper function `storeFile(id, newArr);`.
* Also, we remove the element from the popover. If the array is empty then show some message.

Note: You should provide a unique id to each file picker and its popover previewer.

### Complete code

If you liked this article, please give it 50+ ?and share it! If you have any questions related to this feel free to ask me.

_For more like this and algorithmic solutions in Javascript, follow me on_ [**Twitter**](https://twitter.com/LearnersBucket)_._ I write about [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), React, Nodejs, [Data structures](https://learnersbucket.com/tutorials/topics/data-structures/), and [Algorithms](https://learnersbucket.com/examples/topics/algorithms/) on [_learnersbucket.com_](https://learnersbucket.com/)_._

