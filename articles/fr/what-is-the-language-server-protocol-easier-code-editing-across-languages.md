---
title: Comprendre le Language Server Protocol – Faciliter l'édition de code à travers
  les langages et les outils
date: '2025-01-08T21:54:00.922Z'
author: Alex Pliutau
authorURL: https://www.freecodecamp.org/news/author/pltvs/
originalURL: https://freecodecamp.org/news/what-is-the-language-server-protocol-easier-code-editing-across-languages
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1736371728078/f1da2e66-4095-44e6-bcdf-de44c92e81ad.jpeg
tags:
- name: Language Server Protocol
  slug: language-server-protocol
- name: programming languages
  slug: programming-languages
- name: lsp
  slug: lsp
- name: Go Language
  slug: go
seo_desc: 'In the past, many code editors were built just for one specific language.
  To provide rich and smart code editing, tight integration between the editor and
  the language tooling was a must.

  On the other hand, there were (and still are) more general-pur...'
---


Par le passé, de nombreux éditeurs de code étaient conçus pour un seul langage spécifique. Pour offrir une édition de code riche et intelligente, une intégration étroite entre l'éditeur et l'outillage du langage était indispensable.

<!-- more -->

D'un autre côté, il existait (et il existe toujours) des éditeurs plus généralistes, mais ils manquaient de fonctionnalités lorsqu'il s'agissait de fonctions avancées spécifiques au langage comme la complétion de code, le « aller à la définition », et ainsi de suite. Par exemple, la coloration syntaxique était réalisée à l'aide d'expressions régulières.

Avec le nombre croissant d'éditeurs de code et de langages de programmation disponibles, cela est devenu le problème classique de complexité **M\*N**.

Mais Microsoft a ensuite introduit le [Language Server Protocol][1] (LSP) comme solution au problème ci-dessus, ce qui transforme élégamment cette complexité **M\*N** en une situation **M+N** plus gérable.

## Table des matières

-   [Pourquoi Microsoft a créé le LSP][2]
    
-   [Qu'est-ce que le Language Server Protocol (LSP) ?][3]
    
-   [Fonctionnalités du Language Server][4]
    
-   [Comment fonctionne le LSP ?][5]
    
-   [Language Server pour Go][6]
    
-   [Adoption du LSP][7]
    
-   [Conclusion][8]
    
-   [Ressources][9]
    

## Pourquoi Microsoft a créé le LSP

Le LSP a été initialement motivé par les besoins de VS Code. VS Code devait fonctionner avec des centaines de Language Servers différents dans le cadre de ses extensions. Mais plusieurs problèmes se posaient :

-   **Incompatibilité de langage** : Les Language Servers sont souvent écrits dans des langages différents de celui de l'éditeur (comme le Node.js de VS Code).
    
-   **Impact sur les performances** : Les fonctionnalités de langage peuvent être gourmandes en ressources, ralentissant potentiellement l'éditeur.
    
-   **Complexité d'intégration** : La multiplicité des éditeurs et des langages introduit la complexité **M\*N** mentionnée plus haut.
    

C'est précisément pour cela que Microsoft a introduit le LSP afin de standardiser la communication entre les outils de langage et les éditeurs, permettant aux serveurs de langage d'être écrits dans n'importe quel langage, de s'exécuter séparément pour de meilleures performances, et de s'intégrer facilement à n'importe quel éditeur compatible LSP. Cela simplifie le support linguistique tant pour les fournisseurs d'outils que pour les éditeurs.

Vous trouverez plus d'informations dans ce [Guide d'extension Language Server][10].

## Qu'est-ce que le Language Server Protocol (LSP) ?

Le LSP sépare les serveurs de langage des éditeurs de code (clients de langage). En faisant des serveurs de langage des processus indépendants dédiés à la compréhension du langage, le LSP permet à n'importe quel éditeur d'utiliser un serveur de langage standard. Cela signifie qu'un seul serveur de langage standard peut être utilisé par tous les éditeurs.

Cette interopérabilité est réalisée grâce à un ensemble défini de messages et de procédures standard qui régissent la communication entre les serveurs de langage et les éditeurs. Le LSP définit le format des messages envoyés via JSON-RPC entre l'outil de développement et le serveur de langage.

![Communication entre l'éditeur et le Language Server](https://miro.medium.com/v2/resize:fit:700/0*Vdycq7316e_hKTCe.png)

## **Fonctionnalités du Language Server**

La liste des fonctionnalités peut varier pour chaque serveur de langage individuel, mais ils fournissent généralement les fonctionnalités suivantes :

-   Auto-complétion
    
-   Aller à la définition/déclaration
    
-   Trouver les références
    
-   Formatage de code
    
-   Diagnostics
    
-   Documentation
    

Et plus encore.

Par exemple, [ici][11] vous pouvez voir la liste des fonctionnalités d'éditeur que **gopls** (le Language Server de Go) propose.

Et [ici][12] vous pouvez consulter la spécification LSP complète pour les fonctionnalités disponibles.

Il existe des centaines de Language Servers. Typiquement, chaque langage de programmation mature (ou langage de balisage) possède au moins un Language Server. Vous pouvez voir la liste complète des serveurs de langage qui implémentent le LSP [ici][13].

## **Comment fonctionne le LSP ?**

Le Language Server Protocol est construit sur [JSON-RPC][14]. Il utilise spécifiquement JSON RPC 2.0. Vous pouvez considérer le JSON-RPC comme un protocole d'appel de procédure à distance qui utilise JSON pour l'encodage des données.

En résumé, cela fonctionne comme ceci. Tout d'abord, l'éditeur établit une connexion avec le serveur de langage. Ensuite, au fur et à mesure que le développeur tape du code, l'éditeur envoie les modifications incrémentielles au serveur de langage. Celui-ci renvoie ensuite des informations telles que des suggestions d'auto-complétion et des diagnostics.

Voyons un exemple concret pour l'auto-complétion. La requête du client de langage (l'éditeur) pour ce cas sera :

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/completion",
  "params": {
    "textDocument": {
      "uri": "file:///home/alex/code/test/main.go"
    },
    "position": {
      "line": 35,
      "character": 21
    }
  }
}
```

Comme vous pouvez le voir, il envoie les informations sur la position actuelle du curseur et le fichier tampon. Analysons cela :

-   **ID** : Le client définit ce champ pour identifier la requête de manière unique. Une fois la requête traitée, il renverra une réponse avec le même ID de requête afin que le client puisse faire correspondre la réponse à la bonne requête.
    
-   **Method** : Une chaîne de caractères contenant le nom de la méthode à invoquer.
    
-   **Params** : Les paramètres à passer à la méthode. Cela peut être structuré comme un tableau ou un objet.
    

Le serveur de langage peut accéder à ce fichier, l'analyser et répondre avec des suggestions :

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "isIncomplete": false,
    "items": [
      {
        "label": "Println",
        "kind": 3,
        "insertText": "Println(${1:format}, ${2:a ...interface{}})$0",
        "insertTextFormat": 2,
        "detail": "func Println(a ...interface{}) (n int, err error)",
        "documentation": "Println formats ..."
      },
      // ... other items
    ]
  }
}
```

## **Language Server pour Go**

Le serveur de langage le plus populaire et le plus couramment utilisé pour Go est [gopls][15]. Il est utilisé par de nombreux éditeurs, par exemple par l'[extension Go pour Visual Studio Code][16]. Auparavant, il existait un autre Language Server populaire pour Go créé par l'équipe Sourcegraph appelé [go-langserver][17], mais celui-ci n'est plus activement maintenu.

De nombreux éditeurs installent automatiquement le serveur de langage gopls s'il n'est pas présent sur la machine hôte. Mais vous pouvez également l'installer manuellement :

```
# check if its' installed and which version
gopls version
# golang.org/x/tools/gopls v0.16.2

# install or upgrade
go install golang.org/x/tools/gopls@latest
```

gopls propose également une interface CLI expérimentale :

```
gopls references ./main.go:35:8
```

## **Adoption du LSP**

La tendance est clairement à l'adoption du LSP. De nombreux éditeurs qui ne le supportaient pas initialement ajoutent des capacités LSP en raison de ses avantages.

Cependant, il est important de noter que tous les éditeurs n'utilisent pas le LSP. Les éditeurs classiques comme **Vi**, **Vim** (dans sa configuration de base) et **emacs** (sans plugins spécifiques) s'appuient traditionnellement sur des méthodes plus simples pour le support des langages, comme la coloration syntaxique basée sur des expressions régulières.

De plus, lorsque votre éditeur utilise un Language Server, cela peut avoir un impact notable sur le processeur et la mémoire, en particulier pour les grands projets ou les langages complexes. La bonne nouvelle est que vous pouvez choisir un serveur de langage plus efficace ou les désactiver dans votre éditeur.

Voici comment je peux inspecter quels serveurs de langage mon éditeur [Zed][18] exécute actuellement :

```
ps aux | grep language-server

node yaml-language-server --stdio
node tailwindcss-language-server --stdio
...
```

## **Conclusion**

Grâce au Language Server Protocol, les capacités de codage avancées deviennent universellement accessibles à travers divers langages de programmation et environnements de développement.

Il est utile de savoir comment fonctionnent vos éditeurs de code, il est donc bénéfique d'avoir une compréhension de cette technologie largement utilisée qu'est le LSP. En résumé, la connaissance du LSP vous aide à comprendre et à mieux utiliser les outils de développement modernes.

Le LSP est une victoire tant pour les fournisseurs de langages que pour les éditeurs d'outils.

### **Ressources**

-   [Language Server Protocol][19]
    
-   [gopls][20]
    
-   Découvrez plus d'articles sur [packagemain.tech][21]
    

[1]: https://microsoft.github.io/language-server-protocol/
[2]: #heading-pourquoi-microsoft-a-cree-le-lsp
[3]: #heading-qu-est-ce-que-le-language-server-protocol-lsp
[4]: #heading-fonctionnalites-du-language-server
[5]: #heading-comment-fonctionne-le-lsp
[6]: #heading-language-server-pour-go
[7]: #heading-adoption-du-lsp
[8]: #heading-conclusion
[9]: #heading-ressources
[10]: https://code.visualstudio.com/api/language-extensions/language-server-extension-guide
[11]: https://github.com/golang/tools/blob/master/gopls/doc/features/README.md
[12]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#languageFeatures
[13]: https://microsoft.github.io/language-server-protocol/implementors/servers/
[14]: https://www.jsonrpc.org/
[15]: https://github.com/golang/tools/tree/master/gopls
[16]: https://github.com/golang/vscode-go
[17]: https://github.com/sourcegraph/go-langserver
[18]: https://zed.dev/
[19]: https://microsoft.github.io/language-server-protocol/
[20]: https://github.com/golang/tools/tree/master/gopls
[21]: https://packagemain.tech/