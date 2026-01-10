---
title: How to Assign Dataverse Security Roles at Scale
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2025-06-20T15:16:29.417Z'
originalURL: https://freecodecamp.org/news/how-to-assign-dataverse-security-roles-at-scale
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750432574148/b3cfaebe-7566-4795-b00e-5da9d65dd8f4.png
tags:
- name: Power Apps
  slug: power-apps
- name: Dataverse
  slug: dataverse
- name: power-automate
  slug: power-automate
- name: C#
  slug: csharp
seo_title: null
seo_desc: 'Assigning Dataverse security roles manually works pretty well – until it
  doesn''t.

  Whether you are onboarding 50 new hires or rolling out access to a new app, managing
  roles by hand can be tedious and error-prone.

  In this article, you will learn about...'
---

Assigning Dataverse security roles manually works pretty well – until it doesn't.

Whether you are onboarding 50 new hires or rolling out access to a new app, managing roles by hand can be tedious and error-prone.

In this article, you will learn about three scalable ways to assign security roles across multiple users or teams, with low-code and pro-code options.

### Table of Contents

1. [Aside: Teams](#heading-aside-teams)
    
2. [Canvas Apps Relate / Unrelate Functions](#heading-canvas-apps-relate-unrelate-functions)
    
3. [Power Automate with the Relate Rows in Dataverse Action](#heading-power-automate-with-the-relate-rows-in-dataverse-action)
    
4. [C# Console App: Using the Dataverse SDK](#heading-c-console-app-using-the-dataverse-sdk)
    
5. [Final Thoughts](#heading-final-thoughts)
    

## Aside: Teams

Teams are the simplest way to assign roles to multiple users.

Dataverse admins and team owners can add users to one or more teams. Rather than assigning roles to individual users, the security role is assigned to the team.

But there are caveats: record ownership and team management can introduce their own complexity. In environments with many teams, updating security roles can become just as tedious as assigning them individually.

This article focuses on **programmatic individual assignments**, but keep in mind that all three methods described below can be adapted to work with teams as well.

## Canvas Apps Relate / Unrelate Functions

Canvas app developers can use Power FX to assign security roles across users or teams. Minimal code is required, and the result can serve as a lightweight security role management portal.

While not ideal for massive batches, this approach is suitable for assigning roles to a few hundred users.

```plaintext
ForAll(
    colSelectedUsers As User,
    Relate(
        User.'Security Roles (systemuserroles_association)',
        cbx_securityRoles.Selected
    )
)
```

Here:

* `colSelectedUsers` is a collection of users.
    
* `cbx_securityRoles` is a Combobox control holding the security role to assign.
    

The `Relate` function connects each user with the selected security role. The first parameter is the many-to-many relationship (`systemuserroles_association`) between `systemuser` and `role`.

To find relationship names, open the User table &gt; **Relationships**. Then, look for many-to-many connections to the role table.

![Image of user table relationships highlighting the system user roles association relationship](https://scripted-bytes.ghost.io/content/images/2025/05/Snag_1e2ee592.png align="left")

The security role/user relationship is a many-to-many relationship.

## Power Automate with the Relate Rows in Dataverse Action

The **Relate Rows in Dataverse** action allows you to assign roles dynamically in cloud flows.

![Image of cloud flow assigning security roles](https://scripted-bytes.ghost.io/content/images/2025/05/power-automate.jpg align="left")

### How it works:

* Trigger a flow (for example, manually or via Dataverse trigger).
    
* Fetch a list of users based on a condition.
    
* Loop through each user with **Apply to Each**.
    
* Assign a static or dynamic security role.
    

## C# Console App: Using the Dataverse SDK

This method offers maximum control and supports complex, high-scale role assignments – but it requires pro-code skills.

**Example:**

This console app:

1. Connects to the environment via client credentials.
    
2. Retrieves all users with the title "Salesperson"
    
3. Builds a batch of associate requests.
    
4. Executes the batch transactionally – if one fails, all fail.
    

```csharp
using Microsoft.PowerPlatform.Dataverse.Client;
using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Messages;
using Microsoft.Xrm.Sdk.Query;

class Program
{
    static void Main(string[] args)
    {
        string dataverseUrl = "https://your-org.crm.dynamics.com";
        string clientId     = "client-id-here";
        string clientSecret = "client-secret-here";
        string tenantId     = "tenant-id-here";

        string connectionString = $@"
            AuthType=ClientSecret;
            Url={dataverseUrl};
            ClientId={clientId};
            ClientSecret={clientSecret};
            TenantId={tenantId};
        ";
        // Connect to our environment
        using var serviceClient = new ServiceClient(connectionString);

        if (!serviceClient.IsReady)
        {
            Console.WriteLine("Failed to connect.");
            return;
        }

        // Fetch a list of users that we intend to associate a role with
        var query = new QueryExpression("systemuser")
        {
            ColumnSet = new ColumnSet("systemuserid"),
            Criteria = new FilterExpression
            {
                Conditions =
                {
                     new ConditionExpression(
                        "title",
                        ConditionOperator.Equal,
                        "Salesperson"
                     ),
                }
            }
        };

        var users = serviceClient.RetrieveMultiple(query);

        // Role to assign (pretend guid for demo purposes)
        var securityRoleId = new Guid(
            "00000000-0000-0000-0000-000000000ABC"
        );

        // Prepare our transaction
        var transaction = new ExecuteTransactionRequest
        {
            ReturnResponses = true,
            Requests = new OrganizationRequestCollection()
        };

        // For each user we fetched above, we add an associate request 
        // to the transaction
        foreach (var user in users.Entities)
        {
            var userId = (Guid)user["systemuserid"];

            var relationship = new Relationship(
                "systemuserroles_association"
            );

            var relatedReferences = new EntityReferenceCollection
            {
                new EntityReference(
                    "role",
                    securityRoleId
                )
            };
            // build the associate request
            var request = new AssociateRequest
            {
                Target = new EntityReference(
                    "systemuser",
                    userId
                ),
                RelatedEntities = relatedReferences,
                Relationship = relationship
            };
            // add the request to the transaction
            transaction.Requests.Add(request);
        }

        // Finally, execute the batch as a transaction
        serviceClient.Execute(transaction);
    }
}
```

You can even utilize this logic within a Custom API, allowing Power Automate or Canvas Apps to call it, blending low-code and pro-code capabilities.

## Final Thoughts

If your teams are already well-structured and manageable in number, **teams remain the easiest way** to assign roles at scale.

But when teams aren't feasible – or when assigning directly to users is required – each method we discussed here offers a viable alternative:

* Use **Canvas Apps** for lightweight, user-facing management portals
    
* Use **Power Automate** when complexity is low and there is a need to trigger it in a variety of ways.
    
* Use **C# and the Dataverse SDK** for full control and batch efficiency.
    

Ready to automate your role assignments? Start small – build a simple Power App or Flow – and scale your approach from there. Check out more tips and tricks at [ScriptedBytes.com](http://scriptedbytes.com/)
