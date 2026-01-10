---
title: How to Handle Breaking Changes for API and Event Schemas
subtitle: ''
author: Tim Kleier
co_authors: []
series: null
date: '2023-10-19T14:18:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-breaking-changes
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/7115374283_30d07f11c3_c-2.jpg
tags:
- name: api
  slug: api
- name: Microservices
  slug: microservices
- name: schema
  slug: schema
- name: versioning
  slug: versioning
seo_title: null
seo_desc: "Several years ago while designing APIs for an ecommerce company, I discovered\
  \ the importance of API versioning. So I wrote about it in a freeCodeCamp article\
  \ entitled How to Version a REST API. \nNow I find myself designing event schemas\
  \ for sending m..."
---

Several years ago while designing APIs for an ecommerce company, I discovered the importance of API versioning. So I wrote about it in a [freeCodeCamp](https://www.freecodecamp.org/news) article entitled [How to Version a REST API](https://www.freecodecamp.org/news/how-to-version-a-rest-api/). 

Now I find myself designing event schemas for sending messages across a distributed system. It's a very similar problem with similar pain points and solutions. Adhering to data contracts is critical to ensure we don't frustrate event subscribers or bring down systems.

Versioning APIs is translatable to versioning event schemas, but if you can effectively evolve schemas, you don't actually need versioning. Effective evolution of schemas comes down to avoiding breaking changes. 

Though I covered that briefly in the article above, here I want to thoroughly address breaking changes and propose more solutions to avoiding them.

## What are Breaking Changes?

Essentially, a breaking change to a schema (in an API or event context) is anything that requires a consumer to make an update on their end. It's a change that forces change. Schemas will evolve, but once a schema is in use in production, you have to be very careful not to break the data contract. 

Removing an event format or changing an event's basic structure constitutes a breaking change. But the nuts and bolts are at the attribute (the field or property) level. 

### Structural breaking changes

Here's a list of structural breaking changes for schema attributes:

* **Renaming Attributes** – Changes to an attribute's name, even if it's just changing the case (for example, from camelCase to TitleCase), is a breaking change.
* **Removing Attributes** – Taking an attribute out of a schema.
* **Data Types Changes** – Changing data types, even if the change seems compatible.
* **Making Attributes Required** – Anytime you mark an attribute (even a new one) as required when it wasn't before, it's a breaking change.

|Type|Example|
|------|-------|
|Renaming Attributes|`name` to `firstName`|
|Removing Attributes|Introducing `firstName` but removing `name`|
|Data Type Changes|Changing `productSKU` from `integer` to `string`|
|Making Attributes Required|Now requiring a `customerID`|

### Semantic breaking changes

The other primary category of attribute-level breaking changes has to do with changes in what the data means, or semantic changes. They force consumers to re-interpret the data they're getting. 

They are as follows:

* **Format Changes** – Any change to the format of an attribute. 
* **Meaning Changes** – When the declared or implied meaning of data changes.
* **Stricter Constraints** – When attribute requirements are added or made more restrictive.

|Type|Example|
|------|------|
|Format Changes|Date from `mm/dd/yyyy` to `yyyy-mm-dd`|
|Meaning Changes|Changing an enum, changing `providerCost` from dollars to cents
|Stricter Constraints|Adding `percentage` maximum of 100 

It's important to note that what counts as a "breaking change" might be more nuanced. Changing an `amount` from dollars to cents still forces a change by event subscribers, in interpreting the _meaning_ of the data being sent. Be careful of those, as they are not always obvious.

## What are Non-Breaking Changes?

We can generally describe non-breaking changes as additive or permissive ones. These are changes that don't require change for consumers. 

Here is a list of non-breaking attribute changes: 

* **Adding New Attribute** – In all schema contexts, the addition of a new attribute is a non-breaking change, so long as it's not required (for example, for a POST request). 
* **Making Attribute Not Required** – When an attribute was required but newer schema versions do not require it.
* **Looser Constraints** – Things like more permissive integer ranges (min and max) or allowing for greater decimal precision. Be cautious and communicate with consumers, though, as they may rely on stricter constraints.

|Type|Example|
|------|------|
|Adding New Attribute|Adding `firstName` alongside `name`|
|Making Attribute Not Required|`customerID` is no longer required|
|Looser Constraints|Percentage max increased from 100 to 200|

Non-breaking changes can often be avoided. But evolving schemas effectively can be challenging and require a lot of thought so as not to break schemas and consumers' trust.

## How to Evolve Schemas

Sadly, the list of breaking changes is longer than the non-breaking ones. But there are some strategies for evolving schemas in a non-breaking way.

1. **Domain Knowledge** – Understanding the domain will help ensure you don't end up with poorly named attributes, attributes on the wrong object, or incorrect data types.
2. **Specific Attribute Names** – Rather than changing an attribute's name, data type, or format, introduce a new attribute with a more specific name and correct the data type or format.
3. **Attribute Names With Intent** – Leverage attribute names that reflect their format or intent. For example, consumers might not know whether `providerCost` would be in dollars or cents, so specify with `providerCostInDollars` or `providerCostInCents`. This will also prevent a breaking change if you're having calculation precision issues with dollars and decide to deliver the cost in cents. 
4. **Drafted Schemas & Attributes** – Utilize "draft mode" extensively at the schema level, getting feedback on attributes in simulated environments before they are live in production. For schemas that are in use in production, you could introduce a `draftedAttributes` object and dump experimental (non-production ready) attributes into it. Communicate with consumers that they attributes are being refined – so they should expect breaking changes – and will be moved to the main schema when ready.
5. **Support Existing Attributes** – Leave old attributes in the schema. Don't remove old attributes unless you've been able to coordinate a deprecation/sunsetting strategy with consumers.
6. **Versioning** – If necessary, version your schemas. Although it can become quite difficult to maintain, versioning your schemas is a way to allow for backwards compatibility but move forward with a new schema. You can do high-level versioning (for example, v1 and v2) or more granular semantic versioning (for example, v1.0.1). It's best to version each schema independently, so you don't have to, for example, copy all API v1 endpoints to v2. 

## Conclusion

Breaking changes are a quick way to break trust for any API consumers or event subscribers. I hope that the guidelines above will provide more insight what constitutes a breaking versus non-breaking change, and how to evolve schemas effectively.

If you can't avoid breaking changes, **make sure to coordinate with any and all consumers.** You can actually earn more trust with your consumers if you effectively evolve schemas and communicate breaking changes when they are necessary. 

