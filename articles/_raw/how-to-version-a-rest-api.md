---
title: How to Version a REST API
subtitle: ''
author: Tim Kleier
co_authors: []
series: null
date: '2020-03-03T01:17:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-version-a-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Art-Exhibit-Blog-Banner.png
tags:
- name: api
  slug: api
- name: data contracts
  slug: data-contracts
- name: REST
  slug: rest
- name: REST API
  slug: rest-api
- name: versioning
  slug: versioning
seo_title: null
seo_desc: "If you're not very familiar with APIs, you might be wondering...why all\
  \ the fuss about API versioning? \nIf you've been burned by API changes, you're\
  \ probably the one fussing. If you are a maintainer of an API, you might also be\
  \ fussing about trying t..."
---

If you're not very familiar with APIs, you might be wondering...why all the fuss about API versioning? 

If you've been burned by API changes, you're probably the one fussing. If you are a maintainer of an API, you might also be fussing about trying to field challenging questions like these:

```
# Is this version 2 of just products or of the entire API?
/v2/products

# What catalyzed the change between v1 and v2? How are they different?
/v1/products
/v2/products
```

These questions around versioning are not easy to answer. It's not always clear as to what `v1` or `v2` is referring to. And we should not just make a second version of an endpoint when the first no longer _seems_ to suffice. 

There are clear reasons _why_ your API needs to have versioning, and there are clear strategies for _how_ to effectively navigate API changes. 

However, I have found that most developers--including myself, until I learned some lessons the hard way--are not aware of these reasons and strategies.

This article seeks to highlight those reasons for versioning and strategies for accomplishing it. We're going to assume a [REST](https://restfulapi.net/) API context, as it's a standard for many APIs, and focus on the _versioning_ aspect.

## What is Versioning?

We should start with level-setting on what is meant by the term "API versioning". Here's our working definition:

> API versioning is the practice of transparently managing changes to your API.

Versioning is effective communication around changes to your API, so consumers know what to expect from it. You are delivering data to the public in some fashion and you need to communicate when you change the way that data is delivered.

What this boils down to, in the nitty gritty, is managing data contracts and breaking changes. The former is the primary building block of your API and the latter reveals why versioning is needed.

### Data Contracts

An API is an Application Programming **Interface**, and an interface is a _shared_ boundary to exchange information. The data contract is the heart of this interface.

> A data contract is an agreement on the shape and general content of the request and/or response data. 

To illustrate a data contract, here's a basic JSON response body:

```json
{
  "data": [
    {
      "id": 1,
      "name": "Product 1"
    },
    {
      "id": 2,
      "name": "Product 2"
    }
  ]
}
```

It's an object with a `data` property that is an array (list) of products, each with an `id` and `name` property. But the `data` property could have just as easily been called `body`, and the `id` property on each product could have been a GUID instead of an integer. If a single product was being returned, `data` could be an object instead of an array. 

These seemingly subtle changes would have made for a different agreement, a different contract, regarding the "shape" of the data. The data shape could apply to property names, data types, or even the expected format (JSON vs. XML).

## Why is Versioning Needed?

With APIs, something as simple as changing a property name from `productId` to `productID` can break things for consumers. This very thing happened to our team last week. 

Thankfully, we had tests to catch changes to the API contract. However, we shouldn't have needed those tests, because the maintainers of the API should have known this would be a breaking change.

### Breaking Changes

This was a breaking change to the agreed upon data contract because their change forced us to change our application as well. 

> _What constitutes a "breaking change" in an API endpoint?_ Any change to your API contract that forces the consumer to also make a change. 

Breaking changes primarily fit into the following categories:

1. Changing the request/response format (e.g. from XML to JSON)
2. Changing a property name (e.g. from `name` to `productName`) or data type on a property (e.g. from an integer to a float)
3. Adding a required field on the request (e.g. a new required header or property in a request body)
4. Removing a property on the response (e.g. removing `description` from a product)

### API Change Management

It is never wise or kind to force consumers of an API to make a change. If you must make a breaking change, that's what versioning is for, and we'll cover the most effective ways to version your application and endpoints. 

But first let's briefly discuss how to avoid breaking changes in the first place. We could call this API change management.

Effective change management in the context of an API is summarized by the following principles:

* Continue support for existing properties/endpoints
* Add new properties/endpoints rather than changing existing ones
* Thoughtfully sunset obsolete properties/endpoints

Here's an example that demonstrates all three of these principles in the context of the response for requesting user data:

```json
{
  "data": {
    "id": 1,
    "name": "Carlos Ray Norris",     // original property
    "firstName": "Carlos",           // new property
    "lastName": "Norris",            // new property
    "alias": "Chuck",                // obsolete property
    "aliases": ["Chuck", "Walker"]   // new property
  },
  "meta": {
    "fieldNotes": [
      {
        "field": "alias",
        "note": "Sunsetting on [future date]. Please use aliases."
      }
    ]
  }
}
```

In this example, `name` was an original property. The `firstName` and `lastName` fields are being implemented to provide a more granular option, in the event that the consumer wants to display "Mr. Norris" with some string interpolation but without having to parse the `name` field. However, the `name` property will be supported in an ongoing fashion. 

`alias`, on the other hand, is going to be deprecated in favor of the `aliases` array--because Chuck has so many aliases--and there is a note in the response to indicate the sunsetting time frame.

## How Do You Version an API?

These principles will take a long way in navigating changes to your API without needing to roll a new version. However, sometimes it's avoidable, and if you need a brand new data contract, you'll need a new version of your endpoint. So you'll need to communicate that to the public in some way.

As an aside, do note that we're not talking about the version of the underlying code base. So if you're using [semantic versioning](https://semver.org/) for your application that also supports a public API, you will likely want to separate those versioning systems.

How do you create a new version of your API? What are the different methods for doing so? You'll need to determine what _type_ of versioning strategy you want to take in general, and then as you develop and maintain your API, you'll need to determine the _scope_ of each version change.

### Scope

Let's tackle scope first. As we explored above, sometimes data contracts will be compromised by a breaking change, and that means we'll need to provide a new version of the data contract. That could mean a new version of an endpoint, or it could mean a change at a more global application scope.

We can think of levels of scope change within a tree analogy:

* **Leaf** - A change to an isolated endpoint with no relationship to other endpoints
* **Branch** - A change to a group of endpoints or a resource accessed through several endpoints
* **Trunk** - An application-level change, warranting a version change on most or all endpoints
* **Root** - A change affecting access to all API resources of all versions

As you can see, moving from leaf to root, the changes become progressively more impactful and global in scope.

The _leaf_ scope can often be handled through effective API change management. If not, simply create a new endpoint with the new resource data contract.

A _branch_ is a little trickier, depending on just how many endpoints are affected by the data contract change on the resource in question. If the changes are relatively confined to a clear group of related endpoints, you could potentially navigate this by introducing a new name for the resource and updating your docs accordingly.

```
# variants, which has a breaking change, is accessed on multiple routes
/variants
/products/:id/variants

# we introduce product-variants instead
/product-variants
/products/:id/product-variants
```

A _trunk_ refers to application-level changes that are often a result of a change in one of the following categories:

* Format (e.g. from [XML](https://www.w3schools.com/xml/xml_whatis.asp) to [JSON](https://www.w3schools.com/js/js_json_intro.asp))
* Specification (e.g. from an in-house one to [JSON API](https://www.freecodecamp.org/news/p/ccead735-3d4a-4304-b4e2-57b78ce59156/jsonapi.org) or [Open API](https://www.openapis.org/))
* Required headers (e.g. for authentication/authorization)

These will necessitate a change in your overall API version, so you should plan carefully and execute the transition well. 

A _root_ change will force you to go one step further in ensuring that all consumers of all versions of your API are aware of the change.

## Types of API Versioning

As we turn to different types of API versioning, we'll want to use these insights into varying scopes of API changes to evaluate the types. Each approach has its own set of strengths and weaknesses in addressing changes based on their scope.

There are several methods for managing the version of your API. URI path versioning is the most common.

### URI Path

```
http://www.example.com/api/v1/products
http://api.example.com/v1/products
```

This strategy involves putting the version number in the path of the URI, and is often done with the prefix "v". More often than not, API designers use it to refer to their application version (i.e. "trunk") rather than the endpoint version (i.e. "leaf" or "branch"), but that's not always a safe assumption.

URI path versioning implies orchestrated releases of application versions that will require one of two approaches: maintaining one version while developing a new one or forcing consumers to wait for new resources until the new version is released. It also means you'd need to carry over any non-changed endpoints from version to version. However, for APIs with relatively low volatility, it's still a decent option.

You would likely not want to relate your version number to that of the endpoint or resource, because it would easily result in something like a `v4` of `products` but a `v1` of `variants`, which would be rather confusing.

### Query Params

```
http://www.example.com/api/products?version=1
```

This type of versioning adds a query param to the request that indicates the version. Very flexible in terms of requesting the version of the resource you'd like at the "leaf" level, but it holds no notion of the overall API's version and lends itself to the same out-of-sync issues mentioned in the above comment on endpoint-level versioning of the URI path.

### Header

```
Accept: version=1.0
```

The header approach is one that provides more granularity in serving up the requested version of any given resource. 

However, it's buried in the request object and isn't as transparent as the URI path option. It's also still hard to tell whether `1.0` refers to the version of the endpoint or the API itself.

### Integrating Types

Each of these approaches seem to have the weakness of either favoring a "leaf" or "trunk" scope, but not supporting both. 

If you need to maintain the overall API version and also provide support for multiple versions of resources, consider a blend of the URI Path and Query Params types, or a more advanced Header approach.

```
# URI path and query params combo
http://api.example.com/v1/products?version=1
http://api.example.com/v1/products?version=2

# Extended headers, for http://api.example.com/products
Accept: api-version=1; resource-version=1
Accept: api-version=1; resource-version=2
```

## Conclusion

We've covered a lot of ground here, so let's recap:

* API versioning is the practice of transparently managing changes to your API.
* Managing an API boils down to defining and evolving data contracts and dealing with breaking changes.
* The most effective way to evolve your API without breaking changes is to follow effective API change management principles.
* For most APIs, versioning in the URI path is the most straightforward solution.
* For more complex or volatile APIs, you can manage varying scopes of changes by employing an integration of URI path and query params approaches.

Although these principles should provide clear direction in how to effectively manage change to your APIs, evolving an API is potentially more of an art than a science. It requires thought and foresight to create and maintain a reliable API.

