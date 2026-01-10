---
title: Relative Vs Dynamic Routing in React – Different Routing Methods with Examples
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-08-12T13:57:55.370Z'
originalURL: https://freecodecamp.org/news/relative-vs-dynamic-routing-in-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723295443613/2cf6a928-b2b1-4f71-a6ba-a307b6c13dc9.png
tags:
- name: Web Development
  slug: web-development
- name: React
  slug: reactjs
seo_title: null
seo_desc: 'Single-Page Applications (SPAs) have been growing in popularity as people
  become accustomed to better user experiences and improved application responsiveness.
  This is in part thanks to the introduction of Client-Side Routing (CSR).

  CSR enables navig...'
---

Single-Page Applications (SPAs) have been growing in popularity as people become accustomed to better user experiences and improved application responsiveness. This is in part thanks to the introduction of Client-Side Routing (CSR).

CSR enables navigation between pages without having to send navigation requests to the server. Instead, it provides instant content updates on navigation. It does this by manipulating the history stack of the browser without making any request for a document to the server.

The benefits of using CSR in building single page applications are:

* It improves user experience as it allows for smoother transitions between pages, resulting in faster interactions.
    
* It increases an application's performance, because loading resources such as JavaScript, CSS, and images is done only once and is then re-used.
    
* It reduces multiple page requests handled by the server, resulting in lower bandwidth usage and quicker response time.
    

React, the most popular library for building dynamic and complex user interfaces, enables CSR through `React Router`. React Router is a third-party library that manages navigation and routing in React applications. Big companies such as Shopify, Spotify, Mozilla, and Gumroad (to name just a few) use React Router on their websites.

In this article, we will be taking a deep dive into the types of routing employed in React web applications: `Relative` and `Dynamic` routing.

By the end of this article, you will have good knowledge of these routing methods, and you'll be able to differentiate between them. You'll also be able to identify their best use cases and even combine them to achieve desired routing results in your React application.

### **Pre-Requisite**

To fully grasp what we'll discuss in this article, you should have a basic knowledge of React Routing.

If you need to review, you can read my article on [React Router](https://www.freecodecamp.org/news/use-react-router-to-build-single-page-applications/). If you're ready, then let's jump straight into it!

### Relative Routing

Relative routing is a way of defining routes in reference to their parent routes. It enables navigation to different paths or routes within an application based on the current location rather than a specified point which is usually the root of the application.

Relative routing works with relative paths which specify the location of a component in relation to the parent route. We can also say that relative paths are context-sensitive.

Here is a simple example of relative routing using relative paths:

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="about" element={<About />} />
</Routes>;
```

* The root route path `/` renders the `Home` component.
    
* The `<Route path="about" element={<About />} />` is a relative route that defines the relative path of `about`. It is relative because it considers the root path `/` as its parent.
    

In a nested relative route structure, it works in the same way and still appends to its parent route.

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="about" element={<About />} />
  <Route path="dashboard" element={<Dashboard />}>
    <Route path="profile" element={<Profile />} />
  </Route>
</Routes>;
```

* The `Dashboard` route defining the path `dashboard` still remains a relative route.
    
* The `Profile` route defining the path `profile` is nested within the `dashboard` route which makes it relative to the `dashboard` path. The full path for `Profile` will now read `/dashboard/profile`.
    

### **Absolute Routing**

Absolute routing is similar to relative routing but with a slight difference. Absolute paths in an application can be distinctly differentiated by the leading slash `(/)`. The leading slash prefixes the path name and indicates that the path is considered from the root level of the application.

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
</Routes>;
```

* The `about` is an absolute route, defining an absolute `about` path and directly referencing the root of the application.
    

In an absolute nested route structure, it appears like this:

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
  <Route path="/dashboard" element={<Dashboard />}>
    <Route path="/dashboard/profile" element={<Profile />} />
  </Route>
</Routes>;
```

* The nested `profile` route defines the path `/dashboard/profile` as an absolute path and renders the `Profile` component when the URL matches `/dashboard/profile`.
    

#### **Differences between Relative and Absolute Routing**

1. **Flexibility:** Relative routing is more flexible for nested route structures as relative paths adapt to changes to parent routes automatically. For absolute routing, changes made to parent routes will require an update to all child routes.
    
2. **Structure:** Relative routes are simpler to manage even in a nested route structure, as child routes append to their parent's route by default. Absolute routing, on the other hand, can become difficult to manage in a complex nested route structure because each path must be explicitly specified.
    
3. **Clarity:** In a nested route structure, it can be tricky to understand the hierarchical structure in relative routing. It is much easier in absolute routing, as the paths are clear, concise, and direct for non-nested routes.
    

### Dynamic Routing

Applications typically use data, which could be data for users or products and user input. The data can be unique, and it can also change at any point in time, making it dynamic.

Dynamic routing defines routes that can change based on certain parameters using route parameters or URL segments. The parameters added to the route path allow the application to handle routes dynamically and render different elements based on the URL, as you can see in the example below:

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
  <Route path="/dashboard" element={<Dashboard />}>
    <Route path="profile/:id" element={<Profile />} />
  </Route>
</Routes>;
```

* The `Profile` route with a dynamic segment `:id` matching `profile/:id`. Possible matches for this dynamic path can be `profile/123` or `profile/abc123`.
    

The example above shows relative routing with dynamic routing. We can also use absolute routing with dynamic routing:

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
  <Route path="/dashboard" element={<Dashboard />}>
    <Route path="/dashboard/profile/:id" element={<Profile />} />
  </Route>
</Routes>;
```

**Differences between Static and Dynamic Routing**

1. **Flexibility:** The ability to define a route path according to a parameter makes dynamic routes flexible and responsive to user interaction. Static routes are fixed and do not change.
    
2. **Complexity:** Dynamic routes often involve dynamic segments like parameters and conditional logic which can be difficult to understand. Static routes are straightforward and non-complex.
    
3. **Use Case:** Dynamic routes are used for pages that depend on user input or data. Static routes are used for pages that do not change.
    

### How to Combine Relative and Dynamic Routing

If you want to create a more complex or robust navigation system that includes hierarchical and nested route structures, it's best to combine both relative and dynamic routing.

The combination of both routing methods looks like this:

```markdown
<Routes>
  <Route>
    <Route path="/categories" element={<Categories />}>
      <Route path=":categoryId" element={<CategoryDetails />}>
        <Route path="product/:productId" element={<ProductDetails />} />
      </Route>
    </Route>
  </Route>
</Routes>;
```

* This example shows a deeply nested route structure with both relative and dynamic routes.
    
* The full matching path will be `/categories/:categoryId/product/:productId`.
    

**Benefits of Combining Relative and Dynamic Routing**

1. **Flexibility:** A combination of relative and dynamic routing is best in building a robust navigation structure. This is because it has the flexibility and versatility to define certain routes relatively and other dynamically created routes based on data or user inputs.
    
2. **Enhanced User Experience:** The combined routing methods will provide users with the best of both methods during interaction leaving them satisfied.
    

### Conclusion

In this article, we discussed routing in React web applications and learned about the routing methods used in React Router: relative and dynamic routing. They both play crucial roles in client side routing within React applications, and offer different advantages depending on use cases.

Understanding and implementing these routing methods can elevate the user experience and make your React application both maintainable and scalable.

If you enjoyed reading this article, you could [Buy Me a Coffee](https://buymeacoffee.com/timothyolanrewaju).

You can also connect with me on [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750/) for more insightful posts and articles.

See you on the next one!
