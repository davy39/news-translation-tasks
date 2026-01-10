---
title: The Difference Between <b> and <Strong> in HTML – Explained with Examples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-04-26T23:24:38.000Z'
originalURL: https://freecodecamp.org/news/difference-between-b-and-strong-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--6-.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Bold text is a common formatting technique used to grab attention and highlight\
  \ important information on webpages. \nIn HTML, we have two seemingly interchangeable\
  \ tags for bold formatting: <b> and <strong>. While they may achieve a similar visual\
  \ out..."
---

Bold text is a common formatting technique used to grab attention and highlight important information on webpages. 

In HTML, we have two seemingly interchangeable tags for bold formatting: `<b>` and `<strong>`. While they may achieve a similar visual outcome, there's a crucial difference between them. 

This article dives deep into the distinction between `<b>` and `<strong>` in HTML, exploring their semantic meaning, rendering, accessibility, and best practices for their use.

## What is the `b` Tag in HTML?

The `<b>` tag is an HTML element used to apply bold formatting to text content. It stands for "bold" and is a part of the set of inline elements in HTML. When you wrap text within `<b>` tags, the enclosed text is rendered in a bold font style by web browsers.

But it's essential to note that the `<b>` tag doesn't convey any specific semantic meaning to the text it wraps. Unlike other elements like `<strong>`, which indicates strong importance or emphasis, the `<b>` tag is primarily used for stylistic purposes. It simply instructs the browser to display the enclosed text in bold, without implying any inherent significance or importance.

For example:

```html
<p>This is <b>bold</b> text.</p>

```

<p>This is <b>bold</b> text.</p>


In this case, the word "bold" will be visually emphasized, but the `<b>` tag doesn't provide any additional information about why the text is bolded. Because of this, it's crucial to use the `<b>` tag judiciously, especially when conveying meaningful emphasis or importance in your HTML document.

## What is the `strong` Tag in HTML?

The `<strong>` tag is an HTML element used to denote text with strong importance, emphasis, or relevance. It is one of the semantic markup elements in HTML designed to convey meaning beyond mere presentation. 

When you enclose text within `<strong>` tags, it tells web browsers and assistive technologies that the enclosed text should be treated as having strong importance or emphasis.

Unlike the `<b>` tag, which is primarily used for stylistic purposes to apply bold formatting, the `<strong>` tag carries semantic meaning. While browsers typically render text within `<strong>` tags in a bold font, the primary purpose of the tag is to provide additional context about the significance of the enclosed text.

For example:

```html
<p>This is <strong>important</strong> text.</p>

```

<p>This is <strong>important</strong> text.</p>


In this case, the word "important" is not only visually emphasized with a bold font but also marked as having strong importance or emphasis within the document structure. 

This semantic meaning can be beneficial for accessibility purposes, as screen readers and other assistive technologies can interpret the significance of the text and convey it to users who may not be able to see the visual styling.

## Purpose of Bold Text Formatting

The purpose of bold text formatting in HTML is primarily to visually emphasize certain words or phrases within a block of text. When text is formatted in bold, it stands out more prominently compared to the surrounding text, drawing the reader's attention to it. 

This emphasis can serve various purposes, such as indicating importance, highlighting key points, or distinguishing headings and subheadings from body text.

Bold text formatting can be particularly useful for:

* **Highlighting Important Information:** Bold text is often used to emphasize critical information or key concepts within a paragraph or document, making it easier for readers to identify and comprehend essential points.
* **Improving Readability:** By visually separating important elements from the rest of the text, bold formatting can enhance the overall readability of the content, especially in lengthy passages.
* **Creating Visual Hierarchy:** Bold text can help establish a hierarchy of information within a document, with headings and subheadings appearing bolder than regular text, thus guiding readers through the structure of the content.
* **Emphasizing Call-to-Action:** In web design, bold text is frequently used to draw attention to call-to-action (CTA) buttons or links, prompting users to take specific actions such as making a purchase, signing up for a newsletter, or navigating to another page.

## Can Browser Styles Override?

Yes, browser styles can override the default rendering of HTML elements, including the `<b>` and `<strong>` tags.

Web browsers have their own default stylesheets (user agent stylesheets) that define how HTML elements should be displayed if no specific styles are provided by the webpage itself. These default stylesheets may specify the font size, font family, color, and other visual properties for various HTML elements.

When you use the `<b>` or `<strong>` tags without providing custom styles, browsers will typically apply their default styles for bold text. But these default styles can be overridden by CSS styles defined within the webpage's stylesheet or inline styles applied directly to the elements.

For example, if you have the following HTML:

```html
<p>This is <strong>important</strong> text.</p>

```

And you apply custom CSS styles to override the default bold formatting:

```css
strong {
    font-weight: normal; /* Override bold font weight */
    color: red; /* Change text color */
}



```

<style>
strong {
  font-weight: normal; /* Override bold font weight */
  color: red; /* Change text color */
}
</style>
</head>
<body>
<p>This is <strong style="font-weight: normal; color: red;">important</strong> text.</p>


The text within the `<strong>` tag will no longer appear bold and will be displayed in red, as specified by the CSS rules.

Similarly, you can override the default styles for the `<b>` tag using CSS, although it's less common to do so since the `<b>` tag is typically used for purely presentational purposes without conveying semantic meaning.

Screen readers interpret the `<strong>` tag as indicating text with strong importance or emphasis. When encountering content enclosed within `<strong>` tags, screen reader software will typically announce the text with additional emphasis, indicating to users that the enclosed content is particularly important or relevant within the context of the document.

This semantic markup is crucial for accessibility purposes, as it enables users who rely on screen readers to understand the significance of the text without relying solely on visual cues. By conveying the importance or emphasis of the text through semantic markup like `<strong>`, screen readers can provide a more accurate and informative representation of the content to users who may be visually impaired or otherwise unable to view the visual styling of the webpage.

For example, if a screen reader encounters the following HTML:

```html
<p>This is <strong>important</strong> text.</p>

```

It would announce the text "important" with additional emphasis, such as by adjusting the speech rate or volume, to indicate to the user that this particular text is of heightened significance within the document.

## Potential Issues with `<b>`

Using the `<b>` tag can lead to several potential issues, particularly in terms of accessibility and semantic markup:

**Lack of Semantic Meaning:** The `<b>` tag is purely presentational and does not convey any specific semantic meaning about the enclosed text. This can be problematic for users who rely on assistive technologies like screen readers to access web content, as the bold formatting provided by the `<b>` tag does not provide any indication of the importance or emphasis of the text.

**Accessibility Concerns:** Screen readers may not interpret text enclosed within `<b>` tags as being more important or relevant than surrounding text, potentially leading to a loss of context or understanding for users with disabilities. Without semantic markup to convey the significance of the text, users may struggle to understand the intended meaning of the content.

**SEO Impact:** Search engines may not give as much weight to content styled with the `<b>` tag compared to content marked up with semantic elements like `<strong>`. This could potentially affect search engine rankings, as search engines rely on semantic markup to understand the relevance and importance of content on webpages.

**Maintenance Challenges:** Overuse of the `<b>` tag for purely presentational purposes can lead to maintenance challenges, as it may be difficult to distinguish between text that is bolded for stylistic reasons and text that is genuinely important or emphasized within the document. This lack of clarity can make it harder for developers to maintain and update the content in the future.

Overall, while the `<b>` tag can be useful for adding bold formatting to text, it's important to use it judiciously and consider the potential implications for accessibility, SEO, and document structure

## Does `<strong>` Impact SEO?

Yes, the `<strong>` tag can indirectly impact SEO (Search Engine Optimization) in several ways, while using `<strong>` may indirectly impact SEO by improving content readability and accessibility, it's not a direct ranking factor.

**Semantic Markup:** Search engines like Google aim to understand the content of web pages to deliver relevant search results to users. Semantic markup, such as the `<strong>` tag, provides additional context and clarity about the importance or emphasis of text within a document. When you use `<strong>`, you're signaling to search engines that the enclosed text is of strong importance or relevance, potentially influencing how they interpret and index your content.

**Content Readability:** Clear and well-structured content improves readability, which is a key factor in SEO. By using `<strong>` to emphasize important keywords or phrases, you can enhance the readability and comprehension of your content for both users and search engines.

**User Engagement:** Content that effectively communicates key points using semantic markup like `<strong>` may result in increased user engagement, such as longer time spent on the page or higher click-through rates. Search engines may consider user engagement metrics as indicators of content quality, which can positively impact SEO rankings.

**Accessibility:** Semantic markup improves accessibility for users with disabilities, including those using screen readers. By properly marking up important content with `<strong>`, you're ensuring that all users, regardless of their abilities, can understand the significance of the text. Improved accessibility can lead to better user experiences, potentially resulting in higher rankings in search engine results pages (SERPs).

### When to Use `<strong>`

You should use the `<strong>` tag when you want to emphasize text that carries strong importance or relevance within the context of your document. Here are some scenarios when using `<strong>` would be appropriate:

* **Important Keywords:** Use `<strong>` to highlight important keywords or phrases that are central to the topic or main point of your content. This helps both readers and search engines understand the significance of those terms.
* **Key Points:** Use `<strong>` to emphasize key points, arguments, or conclusions within your content. This draws attention to critical information and makes it more memorable for readers.
* **Warnings or Notices:** Use `<strong>` to highlight warnings, notices, or alerts that require immediate attention from your audience. This ensures that important messages stand out and are not overlooked.
* **Calls to Action:** Use `<strong>` to emphasize calls to action (CTAs) such as "Buy Now," "Sign Up," or "Learn More." This encourages user engagement and increases the likelihood of conversion.
* **Headings and Subheadings:** Use `<strong>` within headings and subheadings to give them additional emphasis and hierarchy within your document structure. This helps users quickly scan and understand the organization of your content.
* **Quotations or Citations:** Use `<strong>` to emphasize quotations or citations from authoritative sources, indicating their importance or relevance to your content.

### When Might `<b>` Be Acceptable?

`<b>` might be acceptable for purely stylistic bold formatting when no specific semantic meaning is intended.

## Conclusion

In conclusion, understanding the subtle yet crucial differences between `<b>` and `<strong>` is essential for crafting well-structured and semantic HTML. 

By prioritizing the `<strong>` tag for conveying importance and reserving `<b>` for situations where emphasis is purely visual, you contribute to a clearer and more accessible web experience for all users. 

Remember, semantic HTML not only benefits users with disabilities but can also play a role in search engine optimization. So, make a conscious choice: use `<strong>` to highlight what truly matters, and leverage CSS for fine-tuning the visual presentation of your bold text. 

By embracing semantic coding practices, you'll create webpages that are not only informative but also speak a clear language to both users and search engines.

Connect with me on [LinkedIn](https://ng.linkedin.com/in/joan-ayebola).

