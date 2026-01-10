---
title: How to Work with Images in HTML – A Beginner's Guide
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-09T15:33:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-images-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Beige-and-Blue-Minimal-Modern-Thesis-Defense-Presentation.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Images are an essential part of web development, adding visual appeal and\
  \ context to your web pages. \nIn HTML, you can easily incorporate images to enhance\
  \ the user experience. This article will guide you through the basics of working\
  \ with images in ..."
---

Images are an essential part of web development, adding visual appeal and context to your web pages. 

In HTML, you can easily incorporate images to enhance the user experience. This article will guide you through the basics of working with images in HTML and help you understand images in HTML better.

## How to Insert an Image into a Web Page

To display an image on your web page, you'll use the `<img>` element. It's a self-closing tag, which means you don't need a closing `</img>` tag. Instead, you place the image source and other attributes within the opening tag. 

Here's the basic syntax:

```html
<img src="image.jpg" alt="Description of the image">

```

* The `src` attribute specifies the image file's location.
* The `alt` attribute provides alternative text for screen readers and that's displayed if the image fails to load.

### Example:

```html
<img src="cat.jpg" alt="A cute cat">

```

Result:

<img src= "https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg">

## Image File Types

HTML supports various image file formats, including JPEG, PNG, GIF, and more. The choice of format depends on your needs. 

Here are explanations of some commonly used image formats in HTML:

### JPEG (Joint Photographic Experts Group):

* **Best For:** Photographs, images with gradients, and complex scenes.
* **Advantages:** High compression, small file sizes, and good image quality for photographs.
* **Considerations:** Lossy compression, not suitable for images with transparency.

### PNG (Portable Network Graphics):

* **Best For:** Images with transparency, icons, logos, and graphics with sharp edges.
* **Advantages:** Supports both lossless and lossy compression, excellent image quality, and transparency.
* **Considerations:** Larger file sizes for complex images compared to JPEG.

### GIF (Graphics Interchange Format):

* **Best For:** Simple animations, images with a limited color palette, and icons.
* **Advantages:** Supports animations, transparency, and small file sizes for simple graphics.
* **Considerations:** Limited color support (256 colors), not suitable for photographs or complex images.

### SVG (Scalable Vector Graphics):

* **Best For:** Vector graphics, logos, icons, and images that need to scale without loss of quality.
* **Advantages:** Resolution-independent, small file sizes, and sharp rendering at any size.
* **Considerations:** Not suitable for complex photographic images.

### WebP:

* **Best For:** Modern web browsers and efficient image delivery.
* **Advantages:** Provides both lossy and lossless compression, smaller file sizes, and good image quality.
* **Considerations:** Limited support in older browsers.

### BMP (Bitmap Image):

* **Best For:** Rarely used on the web due to large file sizes and lack of compression.
* **Advantages:** No loss of quality, suitable for certain specialized applications.
* **Considerations:** Large file sizes and not recommended for general web use.

When choosing an image format for your web page, consider factors such as the type of content, image complexity, required transparency, and your target audience's browser support. 

It's common to use a combination of formats within a website to optimize image delivery. Using appropriate image compression techniques and tools can also help reduce file sizes while maintaining image quality, which is crucial for web performance.

## Image Size and Scaling

You can control the size of your images using the `width` and `height` attributes. These attributes allow you to specify the dimensions of an image on your web page.

```html
<img src="cat.jpg" alt="A cute cat" width="300" height="200">

```

Result:

<img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Picture of a cat" width="300" height="200">


It's important to set appropriate dimensions to maintain aspect ratios and ensure responsive design.

## Image Alignment

Aligning an image within the text using the `align` attribute is an approach that was once used in older versions of HTML. But the `align` attribute is deprecated in modern HTML (HTML5). 

Instead, alignment is typically achieved through CSS. Here's an expanded explanation of both approaches:

### How to use the deprecated `align` attribute (not recommended):

In older versions of HTML, you could use the `align` attribute with the `<img>` element to control the alignment of an image within text. The `align` attribute had values like "left," "right," "top," "middle," and "bottom." Here's an example:

```html
<img src="cat.jpg" alt="A cute cat" align="left">
<p>This is some text that wraps around the image.</p>

```

Result:

<img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="An image" align="left">
<p>This is some text that wraps around the image.</p>


While this method worked in the past, it's considered outdated and is not recommended for modern web development. It's better to separate content from presentation by using CSS for alignment.

### How to use CSS for image alignment (recommended):

In modern web development, CSS (Cascading Style Sheets) is the preferred way to control the alignment of images within text. You can apply CSS rules directly in your HTML file using inline styles or, preferably, use an external CSS file for better maintainability.

Here's an example of how you can use CSS to align an image to the left within a paragraph:

```html
<style>
  .image-align-left {
    float: left;
    margin-right: 10px; /* Add some space between the image and text */
  }
</style>

<p><img src="cat.jpg" alt="A cute cat" class="image-align-left">This is some text that wraps around the image.</p>

```

<style>
  .image-align-left {
    float: left;
    margin-right: 10px; /* Add some space between the image and text */
  }
</style>

<p><img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="An image" class="image-align-left">This is some text that wraps around the image.</p>


In this example, we define a CSS class called `image-align-left` that uses the `float` property to make the image float to the left of the text. The `margin-right` property adds some space between the image and the text to improve readability.

Using CSS for alignment provides more flexibility and control over the positioning of images within text, and it is the recommended approach for modern web design. It also separates styling from content, making your HTML cleaner and more maintainable.

## Image Links

You can make images clickable by wrapping them in an `<a>` (anchor) element. You can further customize the behavior of the hyperlink by using additional HTML attributes, such as `target="_blank"` to open the linked page in a new browser tab or window. 

```html
<a href="link-to-page.html" target="_blank">
  <img src="cat.jpg" alt="Clickable Cat Image">
</a>

```

Result:

<a href="link-to-page.html" target="_blank">
  <img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Clickable Cat Image">
</a>


Now, when a user clicks the image, it will navigate to the specified link. 

## Responsive Images

Modern websites need to be responsive, adapting to various screen sizes. To make your images responsive, use the `max-width` style property:

```html
<img src="image.jpg" alt="Description" style="max-width: 100%;">

```

This property ensures that images will automatically scale down proportionally to fit the width of their parent containers when the screen size or viewport width decreases. 

This is particularly important for ensuring that images don't overflow or break the layout on smaller screens, such as those on mobile devices.

## How to Load Images from External Sources

You can also display images hosted on external websites by specifying the full URL in the `src` attribute:

```html
<img src="https://example.com/image.jpg" alt="External Image">

```

Just make sure you have permission to use external images and that they are publicly accessible.

## Image Accessibility

Web accessibility is crucial. Always include descriptive text in the `alt` attribute to assist users with disabilities. Meaningful alt text helps screen readers provide context for the image. 

Alt text, short for "alternative text," is a textual description of an image that can be read aloud by screen readers or displayed in place of the image if it cannot be loaded.

### Purpose of Alt Text:

* **Screen Readers:** People with visual impairments often use screen readers to navigate websites. When a screen reader encounters an image, it reads the alt text aloud to provide context and convey the image's meaning.
* **Image Loading Issues:** Alt text is also displayed when an image fails to load properly in a web browser, allowing users to understand the image's content even if they cannot see it.

### How to Create Meaningful Alt Text:

* Alt text should be concise but descriptive, conveying the essential information or purpose of the image.
* It should be free from unnecessary details or visual design descriptions (for example, "A blue button" is not as helpful as "Submit Form").
* Avoid using phrases like "image of" or "picture of" since screen readers already announce that it's an image.
* For decorative or purely aesthetic images that don't convey information, use an empty alt attribute (alt="") or indicate that it's decorative (alt="Decorative image").

### Examples of Alt Text:

**Example 1 (Informative Image):**

<img src="" alt="A guide dog assisting a person in a crosswalk.">

**Example 2 (Decorative Image):**

<img src="" alt="Decorative border">

**Example 3 (Complex Image with Description):**

<img src="" alt= "Diagram of the solar system showing the positions and orbits of the planets, with the sun in the center.">

Remember that the goal of alt text is to provide a meaningful and informative description of the image so that users with disabilities can understand its content and context. 

By following these guidelines and creating appropriate alt text, you contribute to a more accessible and inclusive web experience for all users.

## Additional Tips for Using Images

### 1. Image Optimization

[Optimizing images](https://www.freecodecamp.org/news/image-optimization/) is crucial for web performance. Compress images, use appropriate dimensions, and select the right file format to balance image quality and loading speed.

### 2. Lazy Loading

You can improve website performance by implementing lazy loading. The "loading" attribute set to "lazy" is a feature in HTML that tells the browser to load the image lazily. This means it will only load the image when it's in or near the viewport (visible area) of the web page. 

Lazy loading can help improve page loading performance by reducing the initial load time for images that are not immediately visible to the user. 

Here's the code to do that:

```html
<img src="cat.jpg" alt="A cute cat" loading="lazy">

```

<img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Description" loading="lazy">


### 3. Image Captioning

In addition to alt text for accessibility, consider using image captions for better context. You can include a `<figcaption>` element within a `<figure>` element:

```html
<figure>
  <img src="cat.jpg" alt="A cute cat">
  <figcaption>This is the picture of a cat with cute eyes</figcaption>
</figure>

```

Result:

<figure>
  <img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Description">
  <figcaption>This is a picture of a cat with cute eyes <figcaption>
</figure>


### 4. Retina and High-DPI Displays

For high-DPI displays like Retina screens, serve higher-resolution images using the `srcset` attribute:

```html
<img src="cat.jpg" alt="A cute cat" srcset="image.jpg 1x, image@2x.jpg 2x">

```

<img src="https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg" alt="Description" srcset="image.jpg 1x, image@2x.jpg 2x">


## Conclusion

Incorporating images into an HTML documents is a fundamental skill for web developers. With the `<img>` element and its attributes, you can easily control image display, size, and alignment. 

By following best practices for image optimization, accessibility, and responsive design, you'll create visually appealing and user-friendly web content.

As you continue your web development journey, practice integrating images into your projects and explore these additional tips to enhance the performance and accessibility of your websites.

