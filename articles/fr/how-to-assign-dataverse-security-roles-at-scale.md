---
title: Comment attribuer des rôles de sécurité Dataverse à grande échelle
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
seo_title: Comment attribuer des rôles de sécurité Dataverse à grande échelle
seo_desc: 'Assigning Dataverse security roles manually works pretty well – until it
  doesn''t.

  Whether you are onboarding 50 new hires or rolling out access to a new app, managing
  roles by hand can be tedious and error-prone.

  In this article, you will learn about...'
---

Attribuer manuellement des rôles de sécurité Dataverse fonctionne assez bien – jusqu'à ce que ce ne soit plus le cas.

Que vous intégriez 50 nouveaux employés ou que vous déployiez l'accès à une nouvelle application, la gestion des rôles à la main peut être fastidieuse et sujette aux erreurs.

Dans cet article, vous apprendrez trois méthodes évolutives pour attribuer des rôles de sécurité à plusieurs utilisateurs ou équipes, avec des options low-code et pro-code.

### Table des matières

1. [À part : Les équipes](#heading-aside-equipes)
    
2. [Fonctions Relate / Unrelate des applications Canvas](#heading-canvas-apps-relate-unrelate-functions)
    
3. [Power Automate avec l'action Relate Rows in Dataverse](#heading-power-automate-with-the-relate-rows-in-dataverse-action)
    
4. [Application console C# : Utilisation du SDK Dataverse](#heading-c-console-app-using-the-dataverse-sdk)
    
5. [Réflexions finales](#heading-final-thoughts)
    

## À part : Les équipes

Les équipes sont le moyen le plus simple d'attribuer des rôles à plusieurs utilisateurs.

Les administrateurs Dataverse et les propriétaires d'équipes peuvent ajouter des utilisateurs à une ou plusieurs équipes. Plutôt que d'attribuer des rôles à des utilisateurs individuels, le rôle de sécurité est attribué à l'équipe.

Mais il y a des mises en garde : la propriété des enregistrements et la gestion des équipes peuvent introduire leur propre complexité. Dans les environnements avec de nombreuses équipes, la mise à jour des rôles de sécurité peut devenir tout aussi fastidieuse que leur attribution individuelle.

Cet article se concentre sur les **attributions individuelles programmatiques**, mais gardez à l'esprit que les trois méthodes décrites ci-dessous peuvent être adaptées pour fonctionner avec des équipes également.

## Fonctions Relate / Unrelate des applications Canvas

Les développeurs d'applications Canvas peuvent utiliser Power FX pour attribuer des rôles de sécurité à des utilisateurs ou des équipes. Peu de code est requis, et le résultat peut servir de portail léger de gestion des rôles de sécurité.

Bien que ce ne soit pas idéal pour des lots massifs, cette approche est adaptée pour attribuer des rôles à quelques centaines d'utilisateurs.

```plaintext
ForAll(
    colSelectedUsers As User,
    Relate(
        User.'Security Roles (systemuserroles_association)',
        cbx_securityRoles.Selected
    )
)
```

Ici :

* `colSelectedUsers` est une collection d'utilisateurs.
    
* `cbx_securityRoles` est un contrôle Combobox contenant le rôle de sécurité à attribuer.
    

La fonction `Relate` connecte chaque utilisateur avec le rôle de sécurité sélectionné. Le premier paramètre est la relation plusieurs-à-plusieurs (`systemuserroles_association`) entre `systemuser` et `role`.

Pour trouver les noms de relations, ouvrez la table Utilisateur > **Relations**. Ensuite, recherchez les connexions plusieurs-à-plusieurs avec la table des rôles.

![Image des relations de la table utilisateur mettant en évidence la relation d'association des rôles système](https://scripted-bytes.ghost.io/content/images/2025/05/Snag_1e2ee592.png align="left")

La relation rôle/utilisateur est une relation plusieurs-à-plusieurs.

## Power Automate avec l'action Relate Rows in Dataverse

L'action **Relate Rows in Dataverse** vous permet d'attribuer des rôles dynamiquement dans les flux cloud.

![Image du flux cloud attribuant des rôles de sécurité](https://scripted-bytes.ghost.io/content/images/2025/05/power-automate.jpg align="left")

### Comment cela fonctionne :

* Déclenchez un flux (par exemple, manuellement ou via un déclencheur Dataverse).
    
* Récupérez une liste d'utilisateurs basée sur une condition.
    
* Parcourez chaque utilisateur avec **Apply to Each**.
    
* Attribuez un rôle de sécurité statique ou dynamique.
    

## Application console C# : Utilisation du SDK Dataverse

Cette méthode offre un contrôle maximal et prend en charge des attributions de rôles complexes et à grande échelle – mais elle nécessite des compétences en pro-code.

**Exemple :**

Cette application console :

1. Se connecte à l'environnement via des identifiants client.
    
2. Récupère tous les utilisateurs avec le titre "Commercial"
    
3. Construit un lot de demandes d'association.
    
4. Exécute le lot de manière transactionnelle – si l'un échoue, tous échouent.
    

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

Vous pouvez même utiliser cette logique dans une API personnalisée, permettant à Power Automate ou aux applications Canvas de l'appeler, mélangeant ainsi les capacités low-code et pro-code.

## Réflexions finales

Si vos équipes sont déjà bien structurées et gérables en nombre, **les équipes restent le moyen le plus simple** d'attribuer des rôles à grande échelle.

Mais lorsque les équipes ne sont pas réalisables – ou lorsque l'attribution directe aux utilisateurs est requise – chaque méthode que nous avons discutée ici offre une alternative viable :

* Utilisez **les applications Canvas** pour des portails de gestion légers et orientés utilisateur
    
* Utilisez **Power Automate** lorsque la complexité est faible et qu'il y a un besoin de le déclencher de diverses manières.
    
* Utilisez **C# et le SDK Dataverse** pour un contrôle total et une efficacité de lot.
    

Prêt à automatiser vos attributions de rôles ? Commencez petit – construisez une simple application Power App ou Flow – et développez votre approche à partir de là. Découvrez plus de conseils et astuces sur [ScriptedBytes.com](http://scriptedbytes.com/)