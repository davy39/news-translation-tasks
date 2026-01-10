---
title: How to Reduce Technical Debt in the Power Platform
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2025-06-06T10:37:39.795Z'
originalURL: https://freecodecamp.org/news/how-to-reduce-technical-debt-in-the-power-platform
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748957101508/ffb9fc9d-3d35-477b-841f-280d8c6a6793.png
tags:
- name: Power Platform
  slug: power-platform
- name: powerapps
  slug: powerapps
- name: engineering
  slug: engineering
seo_title: null
seo_desc: 'Technical debt refers to the future cost – measured in terms of time, money,
  effort, or opportunity – of choosing expedient solutions today instead of more deliberate
  and scalable ones. And it''s not just a pro-code concept.

  It might be easier to unde...'
---

**Technical debt** refers to the future cost – measured in terms of time, money, effort, or opportunity – of choosing expedient solutions today instead of more deliberate and scalable ones. And it's not just a pro-code concept.

It might be easier to understand if we compare it to financial debt.

Howard G. Cunningham – the creator of the first wiki – described technical debt this way:

> *Shipping first-time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite. Objects make the cost of this transaction tolerable.*  
>   
> *The danger occurs when the debt is not repaid. Every minute spent on not-quite-right code counts as interest on that debt. Entire engineering organizations can be brought to a stand-still under the debt load of an unconsolidated implementation, object-oriented or otherwise.*

In this article, you'll learn why technical debt is just as much a concern in low-code projects as in traditional development – and why, in some ways, it can be even more prominent. We'll walk through eight common contributors to technical debt in Power Platform projects that, if left unchecked, can lead to future headaches.

### Table of Contents

1. [Why Technical Debt Is Also a Low-Code Problem](#heading-why-technical-debt-is-also-a-low-code-problem)
    
2. [Eight Examples of Technical Debt in a Low-Code Project](#heading-eight-examples-of-technical-debt-in-a-low-code-project)
    
    * [Hard-Coded or Static Values in Your Code](#heading-hard-coded-or-static-values-in-your-code)
        
    * [Duplicated Code](#heading-duplicated-code)
        
    * [Poor Naming of Controls and Variables](#heading-poor-naming-of-controls-and-variables)
        
    * [Overloaded Screens and Applications](#heading-overloaded-screens-and-applications)
        
    * [No Version Notes](#heading-no-version-notes)
        
    * [Invisible Logic](#heading-invisible-logic)
        
    * [Denormalized Data Models](#heading-denormalized-data-models)
        
    * [Leading with Layout Before Logic](#heading-leading-with-layout-before-logic)
        
3. [Wrapping Up](#heading-wrapping-up)
    

## Why Technical Debt Is Also a Low-Code Problem

Technical debt builds when short-term decisions ignore long-term consequences. While it exists in any development, low-code platforms increase the risk for a simple reason: they remove much of the traditional friction that forces teams to slow down.

With fewer barriers to entry, it's easier for citizen developers – and even professional developers new to the platform – to start building without considering maintainability, scalability, and security.

Low-code platforms enable speed – but if you aren't intentional, the speed can create an environment that fosters the growth of technical debt.

## Eight Examples of Technical Debt in a Low-Code Project

### Hard-Coded or Static Values in Your Code

We've all seen code like this:

```plaintext
Office365Outlook.SendEmailV2(
  gblAuthenticatedUser.Email, 
  "Sign-Up Request Received!", 
  "A team member will reach out shortly with more information."
)
```

At first glance, this appears to be fine. But what happens if the subject or body of the email needs to change?

Hard-coded values are fragile. A better approach is to store your email templates in a data source, even if it only contains one record.

```plaintext
With({
  wthEmailTemplate: LookUp(EmailTemplates, TemplateType="new_signup")},
  Office365Outlook.SendEmailV2(
    gblAuthenticatedUser, 
    wthEmailTemplate.Subject, 
    wthEmailTemplate.Message
  )
)
```

Now, if the email needs to be changed, you update the data source, not the application logic.

### Duplicated Code

While it can be trickier to avoid than in traditional code, duplicate logic is a future maintenance headache.

Imagine two different ways to create comments in an application:

```plaintext
//Main dialog in a stream of comments
With(
    {
        wthNewlyCreatedComment: Patch(
            Comments,
            Defaults(Comments),
            {Comment: txt_hs_comment.Value}
        )
    },
    Collect(
        colComments,
        wthNewlyCreatedComment
    );
    Set(
        gblCommentCount,
        CountRows(colComments)
    )
)

//A different dialog when replying to another's comment
With(
    {
        wthNewlyCreatedComment: Patch(
            Comments,
            Defaults(Comments),
            {Comment: txt_hs_dialogComment.Value}
        )
    },
    Collect(
        colComments,
        wthNewlyCreatedComment
    );
    Set(
        gblCommentCount,
        CountRows(colComments)
    )
)
```

These two blocks do the same thing. If the logic ever changes, you must remember to update it in both places.

A cleaner approach is to use a **user-defined function (UDF)** to encapsulate logic that gets reused across your app.

```plaintext
// App.Formulas
UpdateComments(comment: Text):Void = 
{
	With(
        {
            wthNewlyCreatedComment: Patch(
                Comments,
                Defaults(Comments),
                {Comment: comment}
            )
        },
        Collect(
            colComments,
            wthNewlyCreatedComment
        );
        Set(
            gblCommentCount,
            CountRows(colComments)
        )
    )
};
```

And then in each of the locations that need this formula:

```plaintext
//Main dialog in a stream of comments
UpdateComments(txt_hs_comment.Value)

//A different dialog when replying to another's comment
UpdateComments(txt_hs_dialogComment.Value)
```

As of this writing, **user-defined functions in Canvas apps support side effects** (such as modifying collections or setting variables), but the overall feature is still **in preview**.

If UDFs aren't an option for your current use case, a common workaround is to use a hidden button that encapsulates the logic and call it with `Select(ButtonName)`. Just keep in mind: the control must be on the same screen where it's being invoked.

### Poor Naming of Controls and Variables

```plaintext
Home Screen
  ButtonCanvas4
  TextCanvas2
  ButtonCanvas1
```

What's wrong with the scenario above? It is impossible to know what each control is responsible for.

Good naming isn't just a nice-to-have – it's one of the best ways to reduce confusion and improve maintainability, especially in collaborative environments.

Here is an improved version that allows any developer to understand what these controls do:

```plaintext
Home Screen
  txt_hs_userName
  btn_hs_submitForm
  btn_hs_cancelSubmission
```

In this example, we follow the pattern of:

`[control_type]_[screen]_[control responsibility]`

This helps make it easy to search for items quickly as well as identify what they do.

Another aspect that naturally lends itself to naming conventions is the use of variables. Canvas apps have various methods for storing data locally. They include:

1. Collections (ClearCollect/Collect)
    
2. Global Variables (Set)
    
3. Local Variables (UpdateContext)
    
4. Contextual Variables (With functions)
    

Each type of variable has a different scoping associated with it. Collections are tables and available throughout your entire application. Global variables are also available throughout the entire application. Variables set using `UpdateContext` are scoped to the screen on which they are declared. And variables contained within a `With` function are available only within that function.

It is a good idea to ensure that the variable name accurately reflects the type of variable it represents. For example:

```plaintext
// prefixed with "wth" for a with-function scoped variable
With({wthNewlyCreatedUser: Patch(AppUsers,...)},...)

// prefixed with "ctx" for a screen-scoped contextual variable
UpdateContext({ctxCurrentPostVotes: LookUp(colPostVotes, ....)})

// prefixed with "gbl" for global
Set(gblAuthenticatedUser, LookUp(AppUsers,....))

// prefixed with "col" for a collection
ClearCollect(colUserRoles, LookUp(AppRoles, ...))
```

Each data storage type is designated by a prefix that indicates its kind, which makes debugging an application easier.

### Overloaded Screens and Applications

It can be tempting to keep everything on one screen for simple applications. But canvas apps can quickly become non-performant if too many controls or too much logic is on a single screen. The recommended limit is no more than 500 controls per app and 300 controls per screen. Using and editing the application can slow down significantly if these limits are exceeded.

One way to prevent this issue is to think more modularly. For example, you may have both administrative and non-administrative tasks within a single application. Instead, you can make two applications, one for admin users and the other for general users.

Another way to avoid these issues in the same application is to build using components. The controls that make up a component don't count individually towards the screen limits and are also a natural way to reduce duplication within and across your applications. Components can be created within an application or as a component library (if your component needs to be used in multiple applications – for example, loaders/spinners and confirmation dialogs).

For more information on components, refer to [this article I wrote about building reusable components.](https://www.scriptedbytes.com/posts/power-apps-reusable-components)

### No Version Notes

As the Power Platform ecosystem grows, advanced versioning techniques are being introduced, including the integration of solutions with Git. But even if you don't have that git integration, there is something simple you can do.

When you save an application after any non-trivial change, use the built-in version notes.

![Image of how to save with version notes in a canvas app](https://scripted-bytes.ghost.io/content/images/2025/05/Snag_29bdb959.png align="left")

This simple habit will make two things much easier:

1. If you ever need to roll back changes, it becomes much easier to identify the correct version to roll back to.
    
2. When using multiple environments (for example, Dev, Test, and Prod), this can help you identify which version is currently in each environment, as the built-in version numbers may not necessarily match.
    

To view version notes for a canvas app, select 'View Details' for the app and then select the versions tab.

![Image of canvas app versions and version notes](https://scripted-bytes.ghost.io/content/images/2025/05/Snag_29bde376.png align="left")

### Invisible Logic

Invisible logic is logic that supports a product, but it is not immediately recognizable. For example, custom APIs and cloud flows can quickly become forgotten if there is no documentation reminding developers that these critical components exist – and what they actually do.

One of the best ways to document a project is by using solutions. Solutions will typically include the majority of a project's assets – often more than 90% – but there are notable exceptions, such as SharePoint lists, Power BI reports, and certain external integrations.

Some things a solution often won't or can't include are assets that belong to core or base solutions – for example, generic cloud flows that serve multiple projects or products. Depending on your solution strategy, you may not want to add these to each solution, and they will only exist in a core or base solution.

Other things that fall under the umbrella of invisible logic include Power BI assets and Dataflows, along with their respective automation architectures (for example, how and when a Dataflow gets triggered).

As a best practice, utilize the self-documenting nature of solutions to provide references to all assets, logic, and dependencies that a project uses. Also, consider adopting a feature-based documentation practice, where each feature or user story implemented includes basic documentation, including high-level implementation details and any underlying logic. This could be a wiki-like document that allows developers, who may be troubleshooting or extending a feature, a simple way to get oriented before diving into an unfamiliar project.

### Denormalized Data Models

Data normalization is a topic of its own, but you don't need to be an expert to get started building robust and *scalable* data models. In simple terms, data normalization involves grouping similar data elements and eliminating duplication.

Take a look at the following example of the employee table.

```plaintext
Employees Table (Denormalized)

| Employee ID | Name   | Department Name | Department Location |
|-------------|--------|------------------|----------------------|
| 1           | Alice  | HR               | Building A           |
| 2           | Bob    | IT               | Building B           |
| 3           | Carol  | HR               | Building A           |
| 4           | Dan    | IT               | Building B           |
| 5           | Eve    | Finance          | Building C           |
```

In the above table, we can see the EMPLOYEE table records contain information about the department. Conceptually, this is fine, but the main issue is that the attributes of each record not only describe the employee but also provide details about the department.

This type of data is referred to as denormalized data. Denormalized data makes the data model harder to scale and maintain. For example, if the `Department Name` changes, we must locate every record with that department name and update it accordingly.

Instead, let's examine a more normalized data model that consists of two tables now.

```plaintext
Employees Table (Normalized)

| Employee ID | Name   | Department ID |
|-------------|--------|----------------|
| 1           | Alice  | 1              |
| 2           | Bob    | 2              |
| 3           | Carol  | 1              |
| 4           | Dan    | 2              |
| 5           | Eve    | 3              |


Departments Table

| Department ID | Department Name | Department Location |
|---------------|------------------|----------------------|
| 1             | HR               | Building A           |
| 2             | IT               | Building B           |
| 3             | Finance          | Building C           |
```

This data model eliminates duplication and simplifies attribute updates for the department, requiring only a single record update to be made. And because each attribute of the EMPLOYEES and DEPARTMENTS tables only describes the primary key of the respective table, this is a normalized data model.

One common misconception among new developers is that more tables are a bad thing. Many believe that fewer data sources are easier to maintain, but that’s not always true.

In development, what makes things easier to maintain isn't less of something, but rather how atomic, modular, and dependent-free it is. For example, a few small, pure functions that do just one thing will be easier to maintain than a single side-effect-producing function that does many things.

Don't shy away from normalized data just because it creates more tables. Shy away from data models that won't scale.

**One final note:** Denormalized data has its place, too, and it's not a bad thing. For example, reporting data is often denormalized and is much more preferred as it makes reporting logic much easier.

### Leading with Layout Before Logic

Low code makes it easy to jump in and start building, which is a significant benefit. But this model can also make it very easy to skip important aspects of development, such as requirement gathering, user interface design, and data modeling.

It's perfectly fine to prototype ideas. This is great for quickly determining if something may or may not be feasible. But you must have the discipline to stop before getting too far along, and take time to plan properly.

For example, consider employing a business logic-first approach. This means that the requirements and core business logic are decided on (and often implemented) before you even start building the user interface.

The core principle of this type of development is that, regardless of the interface a user chooses to interact with our data – and remember, a web application is nothing more than an interface to your data – the core business logic should function properly. In this light, a Canvas app becomes just an aesthetic wrapper that complements what is hopefully well-designed business logic.

## Wrapping Up

Technical debt exists in both traditional and low-code development. Recognizing this debt early, before it begins to accumulate, is critical. Some tips that can reduce and keep technical debt at manageable levels are:

1. Avoid hard-coded or static data in your app logic
    
2. Eliminate duplicated logic with user-defined functions (UDFs)
    
3. Use consistent naming conventions for controls and variables
    
4. Break overloaded apps into multiple screens or multiple apps
    
5. Add version notes to track meaningful changes
    
6. Document invisible logic such as flows and APIs
    
7. Normalize your data to reduce duplication
    
8. Start with business logic—not layout or visuals
    

> **Found this helpful?** I work at the intersection of low-code and pro-code development, focusing on building performant apps and helping you reclaim your time through thoughtful automation. Explore more at [scriptedbytes.com.](https://scriptedbytes.com)
