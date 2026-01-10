---
title: Comment définir la version sémantique pour les applications et bibliothèques
  .NET Core
subtitle: ''
author: Naveed Ausaf
co_authors: []
series: null
date: '2024-11-08T11:26:27.859Z'
originalURL: https://freecodecamp.org/news/set-semantic-versioning-for-net
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731065367635/f8ce5091-d526-4d09-8282-2ffe63cead40.jpeg
tags:
- name: .NET
  slug: net
- name: Aspnetcore
  slug: aspnetcore
seo_title: Comment définir la version sémantique pour les applications et bibliothèques
  .NET Core
seo_desc: 'Semantic Versioning (or SemVer for short) is a software versioning scheme
  that stipulates three-part version numbers of the form <major>.<minor>.<patch>,
  such as 1.0.2, with an optional prerelease suffix of the form -<prerelease>, as
  in 1.0.2-beta.

  S...'
---

[Version sémantique](https://semver.org/) (ou SemVer en abrégé) est un schéma de versionnage de logiciels qui stipule des numéros de version en trois parties de la forme `<major>.<minor>.<patch>`, comme `1.0.2`, avec un suffixe de préversion optionnel de la forme `-<prerelease>`, comme dans `1.0.2-beta`.

SemVer est probablement le schéma de versionnage le plus largement utilisé aujourd'hui. Par exemple, à la fois [Nuget](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning?tabs=semver20sort#pre-release-versions) et [npm](https://docs.npmjs.com/about-semantic-versioning) le recommandent et le supportent, et VS Code [l'utilise](https://github.com/microsoft/vscode/releases) également.

Dans la plupart des dépôts GitHub qui utilisent la fonctionnalité GitHub Releases pour publier des versions, vous verriez un numéro de version SemVer dans le badge de la dernière version sur la page d'accueil, comme on peut le voir dans la capture d'écran ci-dessous :

![Badge de la dernière version dans le dépôt GitHub de Next.js montrant le numéro de version Semantic Versioning en trois parties 15.0.3](https://cdn.hashnode.com/res/hashnode/image/upload/v1730988665455/34706cc9-7cf3-401c-9407-2f15933fef49.png align="center")

J'ai fréquemment besoin de définir un numéro de version SemVer lors de la construction de projets d'API ASP.NET Core, puis de le lire ou de le rapporter à l'exécution.

Par exemple, si je construis une API minimale avec sa version définie sur `1.0.2-beta`, cela serait rapporté par un point de terminaison `/version` exposé par l'API, comme le montre la capture d'écran ci-dessous de [Hoppscotch](https://hoppscotch.io/) (c'est un outil similaire à [Postman](https://www.postman.com/) avec l'avantage qu'il s'exécute dans le navigateur) :

![Capture d'écran de Hoppscotch montre qu'un appel a été fait au point de terminaison /version d'une API s'exécutant localement (sur localhost). Le résultat était un document JSON contenant une propriété "version" dont la valeur est le numéro de version SemVer de l'API "1.0.2-beta".](https://cdn.hashnode.com/res/hashnode/image/upload/v1730746046707/eb8968ef-41c7-4919-a0ed-7aeb25e0a03d.png align="center")

Vérifier que la version rapportée par les services déployés, tels que les applications web et les API, est correcte est une partie cruciale de mon pipeline de CD et fait partie des tests de fumée que j'utilise pour déterminer si un déploiement a réussi.

Une légère complication lors de la définition d'un numéro de version SemVer sur les assemblages .NET est que .NET utilisait à l'origine des numéros de version en quatre parties comme `1.0.3.212` et les assemblages ont toujours ceux-ci (assembly est le terme .NET pour [unités de code compilées en bytecode .NET](https://learn.microsoft.com/en-us/dotnet/standard/assembly/), les plus typiques étant les dll et les exe).

L'autre est que .NET n'a pas un mais plusieurs numéros de version légèrement différents, présents dans le même assemblage.

Dans cet article, je vais vous montrer comment contourner ces particularités et estamper un numéro de version SemVer sur un assemblage .NET lors de la construction, puis le relire à l'exécution.

## Table des matières

* [Structure d'un numéro de version SemVer](#heading-structure-dun-numero-de-version-semver)

* [Les nombreux numéros de version d'un assemblage .NET](#heading-les-nombreux-numeros-de-version-dun-assemblage-net)

* [Comment définir un numéro de version SemVer](#heading-comment-definir-un-numero-de-version-semver)

* [Comment lire la version SemVer d'un assemblage à l'exécution](#heading-comment-lire-la-version-semver-dun-assemblage-a-lexecution)

* [Conclusion](#heading-conclusion)

## Structure d'un numéro de version SemVer

Considérez un numéro de version SemVer comme `1.0.2` ou `1.0.2-beta`. Il a la forme `<major>`.`<minor>`.`<patch>`\-`<prerelease>`

Voici ce que signifient les différents composants :

Le composant `<major>` du numéro de version serait incrémenté uniquement si la nouvelle version rompt une version existante (la plus récente).

Dans le cas d'une application UI, les clients peuvent être considérés comme des *clients humains*. Donc, si la nouvelle version rompt les actifs existants des utilisateurs tels que les définitions de flux de travail, cela nécessiterait d'incrémenter le numéro de version majeure. Dans ce cas, si la version précédente était `1.0.2`, la nouvelle version devrait être `2.0.0` (tous les composants inférieurs du numéro de version seraient réinitialisés).

Dans le cas d'une bibliothèque, comme un package de bibliothèque sur Nuget ou NPM, les clients seraient d'autres codes. Donc, si la nouvelle version rompt le code client existant, c'est-à-dire qu'elle ne serait pas compatible avec sa propre version précédente, alors encore une fois, c'est le composant `<major>` qui serait incrémenté.

`<minor>` est incrémenté si de nouvelles fonctionnalités ont été ajoutées mais que la nouvelle version est toujours compatible avec les versions précédentes. Donc, de `1.0.2`, vous passeriez à `1.1.0`.

`<patch>` est incrémenté lorsqu'une nouvelle version doit être publiée même s'il n'y a pas de changement de rupture et qu'aucune nouvelle fonctionnalité n'a été ajoutée. Cela pourrait se produire, par exemple, s'il y avait une correction de bug qui devait être publiée.

Le suffixe `-<prerelease>` est optionnel. Il est généralement suffixé à un numéro de version en trois parties lorsque le logiciel doit être mis à disposition pendant les phases de test de préversion telles que alpha et bêta. Par exemple, avant de publier généralement la version `1.0.2` de votre logiciel, vous pouvez la mettre à disposition de vos testeurs bêta sous le nom `1.0.2-beta`.

Le composant `<prerelease>` peut être à peu près n'importe quelle chaîne de votre choix et la seule exigence est qu'il s'agisse soit d'un *identifiant alphanumérique* tel que `beta` ou `12` ou `alpha2` (aucun caractère autre que des nombres ou des lettres de l'alphabet) ou de plusieurs identifiants alphanumériques séparés par un point (`.`) par exemple `development.version`.

## Les nombreux numéros de version d'un assemblage .NET

Comme l'explique l'article d'Andrew Lock sur la [version .NET](https://andrewlock.net/version-vs-versionsuffix-vs-packageversion-what-do-they-all-mean/#how-to-set-the-version-number-when-you-build-your-app-library), un assemblage .NET a non pas un mais plusieurs numéros de version différents :

* **AssemblyVersion** : Il s'agit d'un numéro de version en quatre parties, par exemple, `1.0.2.0`. Il est utilisé par le runtime lors du chargement des assemblages liés.

* **FileVersion** : Il s'agit du numéro de version rapporté pour un fichier **.dll** dans l'Explorateur de fichiers Windows lorsque vous cliquez avec le bouton droit sur l'assemblage et sélectionnez Propriétés.

* **InformationalVersion** : Encore un autre numéro de version et, comme FileVersion, peut être vu dans la boîte de dialogue Propriétés si vous cliquez avec le bouton droit sur l'assemblage dans Windows et sélectionnez Propriétés. Cela peut contenir des chaînes et pas seulement des entiers et des points auxquels AssemblyVersion et FileVersion sont contraints.

* **PackageVersion** : Si le projet est un package Nuget, il s'agirait du numéro de version du package dont l'assemblage fait partie.

Tous ces numéros de version sont émis dans l'assemblage lors de la compilation sous forme de métadonnées. Vous pouvez les voir si vous inspectez l'assemblage avec [JetBrains dotPeek](https://www.jetbrains.com/decompiler/) (gratuit) ou [Red gate Reflector](https://www.red-gate.com/products/reflector/) (non gratuit) ou similaire.

FileVersion et InformationalVersion peuvent également être vus dans l'onglet Détails de la boîte de dialogue Propriétés qui apparaît lorsque vous cliquez avec le bouton droit sur le fichier d'assemblage dans l'Explorateur de fichiers Windows et sélectionnez Propriétés :

![Boîte de dialogue Propriétés pour une DLL .NET compilée dans l'Explorateur de fichiers Windows. Elle montre l'attribut "File Version" de la DLL avec la valeur "1.0.2.0" et son attribut "Product version" avec la valeur "1.0.2-beta"](https://cdn.hashnode.com/res/hashnode/image/upload/v1730755185100/d444a84b-5148-47e6-ab75-951d9f0f73ac.png align="center")

Dans la capture d'écran ci-dessus, "Product version" est la légende pour InformationalVersion tandis que "File version" est la légende pour FileVersion.

Parmi les quatre types de numéros de version décrits ci-dessus, seuls les trois premiers s'appliquent à tout assemblage (c'est-à-dire que l'assemblage fait partie ou non d'un package Nuget).

Parmi ces trois, AssemblyVersion ajoute toujours un `0` à la quatrième place si vous essayez de définir une version SemVer qui n'a que trois nombres (plus un suffixe *prerelease* optionnel). Par exemple, si vous essayez de définir une version SemVer de `1.0.2-beta` lors de la construction, puis lisez la valeur AssemblyVersion à l'exécution dans l'assemblage, elle serait `1.0.2.0`.

FileVersion fait de même, comme le montre la capture d'écran ci-dessus.

InformationalVersion est le seul numéro de version qui serait défini exactement sur la version du serveur que vous avez définie lors de la construction, comme le montre la capture d'écran ci-dessus.

Par conséquent, InformationalVersion est ce que nous devons définir avec une version SemVer lors de la construction, et relire à l'exécution.

## Comment définir un numéro de version SemVer

Il y a deux choses que vous devez faire pour définir un numéro de version SemVer sur un assemblage lors de la construction.

**Premièrement**, dans un élément `<PropertyGroup>` dans le fichier `csproj` du projet, ajoutez l'élément `<IncludeSourceRevisionInInformationalVersion>false</IncludeSourceRevisionInInformationalVersion>` :

```xml
<PropertyGroup>
 ...
 <IncludeSourceRevisionInInformationalVersion>false</IncludeSourceRevisionInInformationalVersion> 
</PropertyGroup>
```

Comme décrit dans [cet issue](https://developercommunity.visualstudio.com/t/Build-adds-string-to-assembly-Informatio/10515014?sort=newest), cela garantit que InformationalVersion est défini exactement sur le numéro de version SemVer que nous avons spécifié et ne se voit pas ajouter un `+<hash code>` à la fin.

**Deuxièmement**, passez le numéro de version comme valeur de la propriété `Version` passée à la commande `dotnet build` par exemple :

```yaml
dotnet build --configuration Release -p Version=1.0.2-beta
```

Cela définirait InformationalVersion dans l'assemblage compilé (fichier .exe ou .dll) sur `1.0.2-beta`.

Accessoirement, cela définirait également AssemblyVersion et FileVersion (un `0` supplémentaire serait ajouté à la fin de `1.0.2`) mais nous ne nous intéressons pas à ceux-ci.

Notez que, au lieu de passer l'argument `Version` sur la ligne de commande, vous pouvez définir la propriété MS Build `<Version>1.0.2-beta</Version>` dans un élément `<PropertyGroup>` dans le fichier csproj. Cependant, passer une valeur du paramètre `Version` à `dotnet build` est plus simple car le fichier csproj n'a pas besoin d'être modifié chaque fois que le numéro de version est incrémenté. Cela est utile dans les pipelines de CD. Si vous définissez `<Version>` dans le fichier csproj, cela sera remplacé par ce que vous fournissez sur la ligne de commande `dotnet build` comme valeur de la propriété `Version`.

## Comment lire la version SemVer d'un assemblage à l'exécution

Le code qui lit InformationalVersion à l'exécution est le suivant :

```csharp
string? version = Assembly.GetEntryAssembly()?.
  GetCustomAttribute<AssemblyInformationalVersionAttribute>()?.
  InformationalVersion;
```

Dans mes API minimales, pour ajouter un point de terminaison `/version` comme je l'ai montré dans la section Introduction ci-dessus, je place l'extrait de code ci-dessus dans `Program.cs`, puis j'ajoute l'extrait de code suivant immédiatement après. Notez que l'ensemble doit apparaître **avant** que `builder.Build()` **soit appelé** :

```csharp
//cet objet d'un type anonyme sera
//sérialisé en JSON dans le corps de la réponse
//lorsqu'il est retourné par un gestionnaire
var objVersion = new { Version = version ?? "" };

//AUTRE CODE
//var app = builder.Build()
```

Après que `builder.Build()` soit appelé, je crée le gestionnaire pour le point de terminaison `/version` :

```csharp
app.MapGet("/version", () => objVersion);
```

Maintenant, lorsque j'exécute le projet d'API et que j'appelle le point de terminaison `/version`, je récupère le numéro de version dans un objet JSON dans le corps de la réponse HTTP :

```json
{
  "version": "1.0.2-beta"
}
```

C'est ce que la capture d'écran Hoppscotch dans l'Introduction a montré.

## Conclusion

Cet article vous a montré comment définir un numéro de version SemVer dans vos assemblages .NET.

Il vous a également montré comment lire le numéro de version à l'exécution.