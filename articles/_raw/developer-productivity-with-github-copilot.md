---
title: How to Use GitHub Copilot to Become a Happier and More Productive Developer
subtitle: ''
author: Tim Kleier
co_authors: []
series: null
date: '2023-06-16T17:02:17.000Z'
originalURL: https://freecodecamp.org/news/developer-productivity-with-github-copilot
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-14-at-12.42.04-PM.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: GitHub
  slug: github
- name: Happiness
  slug: happiness
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'There are a number of AI tools for developers emerging on the market. But
  in my mind GitHub Copilot stands above the rest because of its usability, seamless
  IDE integration, and remarkable enhancements to developer productivity.

  Copilot offers a vari...'
---

There are a number of AI tools for developers emerging on the market. But in my mind GitHub Copilot stands above the rest because of its usability, seamless IDE integration, and remarkable enhancements to developer productivity.

Copilot offers a variety of AI tools that have radically streamlined my experience as a software developer. I've used it to generate code, tests, and even simple applications. It's also great for debugging, refactoring, and documenting existing code. 

Weirdly, using Copilot has caused me to develop features faster than business stakeholders can review them.

It's important to note that AI tools, including Copilot, can be blatantly wrong, apologize (or not) when corrected, and then confidently produce the same error. But as long as you're aware of the downsides of AI tools, and have enough coding knowledge to recognize when they're incorrect, you can mitigate them on the path to [substantially improved productivity](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/).

## How to Setup GitHub Copilot

For setup and basic usage of Copilot, check out the [docs](https://docs.github.com/en/copilot). You can add on Copilot to an individual or business account, and there's a free trial and reasonable [pricing](https://github.com/features/copilot#pricing) after the trial. 

After adding Copilot to your GitHub account, you'll want to install the [plugins for your IDE](https://docs.github.com/en/copilot/getting-started-with-github-copilot) and log into GitHub to access Copilot.

In this article, we'll use these [Visual Studio Code extensions](https://marketplace.visualstudio.com/search?term=copilot&target=VSCode&category=All%20categories&sortBy=Relevance):

| GitHub Extension      | Description | Preview |
| ----------- | ----------- | ----------- |
| [Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)      | AI pair programmer with in-IDE code suggestions       | No |
| [Copilot Nightly](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-nightly)   | Nightly build of Copilot, includes latest changes        | No |
| [Copilot Labs](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-labs) | Experimental features in sidebar | [Yes](https://githubnext.com/projects/copilot-labs/) |
| [Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) | Interactive chat in sidebar, part of Copilot X | [Yes](https://github.com/features/preview/copilot-x) |
| [Copilot Voice](https://marketplace.visualstudio.com/items?itemName=GitHub.heygithub) | Voice assistant | [Yes](https://githubnext.com/projects/copilot-voice/) |

Notes:

1. This info is up-to-date as the writing of this article, but will likely change as GitHub evolves these products.
2. I haven't yet received access to Copilot Voice or Copilot (X) for Pull Requests, so my perspective on these are limited and based on GitHub's preview docs.

### Privacy

Before jumping into some key use cases for Copilot, a quick note on privacy: Basically, if you trust GitHub to host your source code, you can likely trust what they do with your Copilot prompts and code snippets. [See their [FAQ docs](https://github.com/features/copilot#faq) and [Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement).]

## Use Cases for GitHub Copilot

The uses cases for GitHub Copilot are numerous, especially when you add in [t](https://github.com/features/preview/copilot-x)he preview features of Labs, Chat, and Voice. Using Copilot's features can really streamline the development process. 

Here are some great ways to leverage Copilot extensions:

| Category      | Extension(s) |
| ----------- | ----------- |
| Code Generation      | Copilot, Copilot Nightly, Copilot Voice  |
| Explaining Code   | Copilot Labs, Copilot Chat, Copilot Voice        | 
| Language Translation | Copilot Labs, Copilot Chat |
| Debugging | Copilot Labs, Copilot Chat |
| Refactoring | Copilot Labs, Copilot Chat |
| Test Generation | Copilot, Copilot Nightly, Copilot Labs, Copilot Chat |
| Code Reviews | Copilot Chat |
| Voice-Driven Development | Copilot Voice |

### Code Generation

Copilot is known for its code completion features. If it's given a comment in the code or you type the beginnings of a line of code, Copilot will suggest a solution that you can accept, ignore, or explore alternatives. It's referred to as "ghost text".

Once you have the Copilot extension installed and you're logged in, code completion is as simple as typing instructions and hitting the Tab key once the suggestion comes up.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screen-Recording-2023-06-09-at-8--1-.gif)
_A comment prompt in Ruby that Copilot uses to create a method and invocation_

Taking code completion one step further, Copilot Chat can take a single prompt and generate instructions for building an entire application. 

I asked it to create a REST API in Node with CRUD functions for "products", and it generated functional code. Impressive overall. Given the same prompt, ChatGPT also gave me instructions for how to run the code, which was nice.

Copilot Voice can also write or edit code based on voice commands. Most of the time, using the keyboard with Copilot code completion is faster than dictating lines of code with Voice. But it's compelling to think about using Copilot Voice to create and run code without having to type or stare at a screen.

### Explaining Code

I often have to stare at a screen to figure out what a block of code is doing. Sometimes it's legacy code where I don't understand the business context. Sometimes it's using a particular library I'm not used to. Sometimes I curse the person who wrote it, even if it's me.

Below is some code generated by Copilot Chat from my "REST API in Node..." prompt from above:

```javascript
app.get('/products/:id', (req, res) => {
  const id = req.params.id;
  const product = products.find((p) => p.id === id);
  if (product) {
    res.json(product);
  } else {
    res.status(404).json({ error: 'Product not found' });
  }
});
```

I took this code and fed it into the "Explain" feature in Copilot Labs. Here's the response...

_Here is the explanation for the code above:_  

1. _We define a route with the route path /products/:id. The colon : in the path indicates that it is a route parameter. The value of the route parameter will be available in req.params. For example, if the route path is /products/:id and we make a request to /products/5, then the value of req.params will be { id: 5 }._
2. _We get the id from req.params and find the product with the given id from the products array. If a product with the given id exists, we return it. Otherwise, we send a 404 error response with the error message Product not found._

This is a pretty straightforward segment of code, and the response is clear and straightforward as well. It would be easy to add this as documentation in a code comment above the function.

Another good example is regular expressions. I understand how regular expressions work but I don't often have the patience to figure out what a particular regex is doing. I fed Copilot Chat this giant regex statement for email validation:

```
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
```

It explained the regex at a high level, indicating it was broken into the local and domain parts, representing before and after the "@" sign in an email address. Then it described allowable characters in each part. Quite helpful.  

### Language Translation

Developers are often required to quickly learn new languages and frameworks. Copilot Labs and Chat make this pretty easy. Here's an array of products in JavaScript and Ruby that was converted by Copilot:

```javascript
let products = [
  { id: '1', name: 'Product 1', price: 10.99 },
  { id: '2', name: 'Product 2', price: 19.99 },
  { id: '3', name: 'Product 3', price: 7.99 }
];
```

```ruby
products = [
  { id: '1', name: 'Product 1', price: 10.99 },
  { id: '2', name: 'Product 2', price: 19.99 },
  { id: '3', name: 'Product 3', price: 7.99 }
]
```

This is a very simple example, so let's try making this into a class and going the other way (from Ruby to JavaScript):

```ruby
class Product
  attr_reader :name, :price

  def initialize(name, price)
    @name = name
    @price = price
  end
end
```

```javascript
class Product {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
}
```

This checks out. For good measure, I tested TypeScript as well, and it worked perfectly, too.

### Debugging

This is a very handy feature. You can give Copilot Chat or Labs problematic code or error messages and it will indicate what it thinks the issue is. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screen-Recording-2023-06-14-at-1.gif)
_Copilot Labs "Fix Bug" Brush Feature_

I can't tell you how many hairs I've pulled out because I couldn't find what amounted to a syntax error. Copilot's ability to fix bugs just makes me happier and hairier. 

You can also give Copilot Chat an error message with no other prompt and it can tell you the issue. I arbitrarily removed a dot from the Node REST API code:

```javascript
products[productIndex] = { id, ..req.body };
```

I copied/pasted the error message in Chat, and it responded with...

> Looking at the code excerpt you provided, it seems that the issue is on line 49 where there is a syntax error in the object literal. The ".." before `req.body` is causing the error. It should be just one dot instead of two.

This is both correct (the line and source of the error) and incorrect (that it should be only one dot). It then gave me a code snippet with three dots, which is also correct. 

As I mentioned at the outset, you've gotta double-check AI's work. Still, I'm impressed by Copilot's ability to parse an error message, describe what it thinks is wrong, and suggest a fix.

### Refactoring

Another great use case is refactoring. Consider the code below:

```ruby
def price_with_discount
  price - (price * discount_rate)
end
```

This simple price calculation doesn't factor in `nil` values, strings that should be numbers, or reasonable values for `price` or `discount_rate`. We need the code to do this:

1. Ensure `price` is an integer or float (not nil)
2. Ensure `price` is not negative
3. Ensure `discount_rate` is a float (not nil)
4. Ensure `discount_rate` is not negative and less than or equal to 1

Copilot Chat handles this with ease...

```ruby
def price_with_discount(price, discount_rate)
  raise ArgumentError, "Price must be a positive number" unless price.is_a?(Numeric) && price >= 0
  raise ArgumentError, "Discount rate must be a float between 0 and 1" unless discount_rate.is_a?(Float) && discount_rate >= 0 && discount_rate <= 1

  price - (price * discount_rate)
end
```

### Test Generation

Using Copilot to generate tests is technically a subset of "Code Generation" above, but I felt it was so useful it warranted its own mention.

Generating unit tests for code can be tedious if you're trying to cover happy and sad paths, primary use cases and edge cases. Our `price_with_discount` code above needs test cases to ensure an error is raised if `price` or `discount_rate` don't meet the requirements. In addition, we might want to test the following:

1. A `price` without a `discount_rate`
2. A `price` with a reasonable `discount_rate` (for example, a 10% discount)
3. A `price` with a 100% `discount_rate` (for example, if we want to give the product away)

With these and our previous error cases, here's what Copilot Chat generated, after a little fine-tuning (re-prompting) and switching from Minitest to Rspec.

```ruby
RSpec.describe Product do
  describe "#price_with_discount" do
    context "when given a valid price and discount rate" do
      it "returns the price with the discount applied" do
        product = Product.new("Test Product", 100, 0.2)
        expect(product.price_with_discount(product.price, product.discount_rate)).to eq(80)
      end
    end

    context "when given a nil price" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", nil, 0.2)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Price must be a positive number")
      end
    end

    context "when given a price less than 0" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", -100, 0.2)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Price must be a positive number")
      end
    end

    context "when given a nil discount rate" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", 100, nil)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Discount rate must be a float between 0 and 1")
      end
    end

    context "when given a discount rate less than 0" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", 100, -0.2)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Discount rate must be a float between 0 and 1")
      end
    end

    context "when given a discount rate greater than 1" do
      it "raises an ArgumentError with an appropriate message" do
        product = Product.new("Test Product", 100, 1.5)
        expect { product.price_with_discount(product.price, product.discount_rate) }.to raise_error(ArgumentError, "Discount rate must be a float between 0 and 1")
      end
    end
  end
end
```

One test for valid input, five for invalid input. All six work, and I didn't have to write them!

### Code Reviews

One feature of Copilot X is [Copilot for Pull Requests](https://githubnext.com/projects/copilot-for-pull-requests#technical-preview-available-now). Here are some of the key features:

* **Template Expansion** – Leverage Copilot to fill in your PR template and explain code
* **Gentest** – Generate tests for your code based on Copilot's analysis
* **Ghost Text** – Receive suggestions while you're typing in the PR

### Voice-Driven Development

Formerly known as "Hey, Github!", Copilot Voice allows you to use natural language prompts to interact with your code. It looks impressive, boasting these capabilities:

* **Write/Edit Code** – Use voice controls to trigger Copilot code suggestions
* **Code Navigation** – Navigate a file without a keyboard or mouse
* **Control the IDE** – Trigger any VS Code command
* **Code Summarization** – Get summaries of blocks of code

## Summary

GitHub is rapidly producing revolutionary developer productivity tools with its suite of Copilot extensions. It's increasing my joy in programming and decreasing my time spent on mind-numbing tasks. I would encourage you to keep track of enhancements to Copilot as they're happening quickly.

Ignore click-bait promises of a "10x productivity gain", but don't ignore the research of [Copilot's impact on developer productivity and happiness](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/). 

Spend some time with Copilot tools trying out the use cases above, and I think you'll be surprised by its effect on your productivity and happiness.

