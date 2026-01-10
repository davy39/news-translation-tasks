---
title: Les meilleurs outils Go à utiliser pour vos projets frontend
date: '2023-12-13T18:45:10.000Z'
author: Ekemini Samuel
authorURL: https://www.freecodecamp.org/news/author/envitab/
originalURL: https://freecodecamp.org/news/go-tools-for-your-frontend-projects
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/go-tools-1.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_desc: 'The Go programming language is renowned for its efficiency in backend development.
  But it''s pretty easy to extend its capabilities to frontend projects as well.

  This article explores essential Go tools that empower frontend developers to enhance
  thei...'
---


Le [langage de programmation Go][1] est réputé pour son efficacité dans le [développement backend][2]. Mais il est assez facile d'étendre ses capacités aux projets frontend également.

<!-- more -->

Cet article explore les outils Go essentiels qui permettent aux développeurs frontend d'améliorer leurs workflows, en mettant l'accent sur la simplicité et la productivité.

### Prérequis

Avant de plonger dans l'exploration des outils Go pour les projets frontend, assurez-vous d'avoir les éléments suivants en place :

-   Go installé sur votre machine. Vous pouvez le télécharger sur le [site officiel de Go][3].
-   Un éditeur de code de votre choix installé, tel que [Visual Studio Code][4], [GoLand][5] ou [Zed][6].
-   Une compréhension de base de Go, consultez la [documentation de Go][7] ou ce [manuel Go][8].

## Outils Go pour vos projets frontend

Voici cinq outils Go que vous pouvez essayer pour vos projets frontend :

### 1\. Fiber : un framework web performant

[Fiber][9] est un framework web pour Go inspiré d'[Express.js][10], connu pour ses hautes performances et son design minimaliste. Il facilite le routage efficace et le support des middlewares, ce qui le rend idéal pour la communication frontend-backend et le développement d'API.

Fiber est particulièrement utile pour créer des API robustes et performantes avec lesquelles les applications frontend peuvent interagir de manière fluide.

**Exemple de code :**

Cet exemple sera une application web simple où les utilisateurs peuvent saisir leur nom, soumettre un formulaire et recevoir un message de salutation personnalisé en retour.

Dans votre éditeur de code, utilisez cette structure pour le projet :

![arborescence-du-projet](https://www.freecodecamp.org/news/content/images/2023/12/project-tree.png)

Saisissez ce code pour le fichier `main.go` :

```
package main

import (
    "fmt"
    "github.com/gofiber/fiber/v2"
    "github.com/gofiber/template/html/v2"
)

// RenderForm renders the HTML form.
func RenderForm(c *fiber.Ctx) error {
    return c.Render("form", fiber.Map{})
}

// ProcessForm processes the form submission.
func ProcessForm(c *fiber.Ctx) error {
    name := c.FormValue("name")
    greeting := fmt.Sprintf("Hello, %s!", name)
    return c.Render("greeting", fiber.Map{"Greeting": greeting})
}

func main() {
    app := fiber.New(fiber.Config{
        Views: html.New("./views", ".html"),
    })

    // Serve static files (HTML templates and stylesheets).
    app.Static("/", "./static")

    // Define routes.
    app.Get("/", RenderForm)
    app.Post("/submit", ProcessForm)

    // Start the Fiber app on port 8080.
    app.Listen(":8080")
}
```

Le dossier **views** contient deux fichiers HTML qui affichent le formulaire et la réponse dans le navigateur. Saisissez le code pour ceux-ci :

`form.html`

```
<!-- views/form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fiber Example</title>
    <link rel="stylesheet" href="/styles/main.css">
</head>
<body>
    <form action="/submit" method="post">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

`greeting.html`

```
<!-- views/greeting.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fiber Example</title>
    <link rel="stylesheet" href="/styles/main.css">
</head>
<body>
    <p>{{.Greeting}}</p>
</body>
</html>
```

Ensuite, dans le dossier **styles** à l'intérieur du répertoire **static**, saisissez ce code pour le fichier `main.css` :

```
/* main.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 20px;
  }

  form {
    max-width: 400px;
    margin: 0 auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  label {
    display: block;
    margin-bottom: 10px;
  }

  input {
    width: 100%;
    padding: 8px;
    margin-bottom: 20px;
    box-sizing: border-box;
  }

  button {
    background-color: #007bff;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }
```

Le code de ce projet est accessible sur ce [dépôt GitHub][11].

#### [Moteur de rendu de Fiber][12]

Fiber s'intègre à des moteurs de rendu (view engines), et nous utiliserons le moteur de template HTML dans cet exemple. La configuration du moteur de rendu est simple, permettant une séparation claire des préoccupations entre le backend et le frontend.

```
app := fiber.New(fiber.Config{
    Views: html.New("./views", ".html"),
})
```

[Servir des actifs statiques][13]

Fiber simplifie le service des actifs statiques, assurant une livraison efficace des feuilles de style, des images et des fichiers JavaScript côté client. Dans notre exemple, les styles sont stockés dans le dossier static et liés dans les templates HTML.

```
// Serve static files (HTML templates and stylesheets)
app.Static("/", "/.static")
```

Exécutez le programme en utilisant `main.go` pour démarrer le serveur sur le port 8080. Il affiche une sortie console générée par le framework Fiber.

```
go run main.go
```

![fib](https://www.freecodecamp.org/news/content/images/2023/12/fib.png)

Visitez http://127.0.0.1:8080/ dans votre navigateur pour voir la réponse. Voici comment cela fonctionne :

![fibd](https://www.freecodecamp.org/news/content/images/2023/12/fibd.gif)

### 2\. Buffalo : un écosystème de développement web holistique

[Buffalo][14] est un écosystème de développement web holistique pour Go, fournissant un ensemble complet d'outils, de bibliothèques et de conventions pour construire des applications web modernes. Il simplifie le développement frontend et backend en proposant du [scaffolding][15] et des [fonctionnalités de hot-reload][16].

Buffalo est avantageux pour mettre en place rapidement des applications web full-stack, permettant aux développeurs de se concentrer sur la création de fonctionnalités plutôt que sur le code boilerplate.

Un projet Buffalo typique a la structure suivante :

```
myapp/
|-- actions/
|-- grifts/
|-- migrations/
|-- models/
|-- public/
|-- templates/
|-- go.mod
|-- go.sum
|-- main.go
```

-   actions : Contient les gestionnaires (handlers) pour les routes web.
-   grifts : Héberge les tâches Grift pour l'automatisation.
-   migrations : Stocke les fichiers de migration de la base de données.
-   models : Définit les modèles de données.
-   public : Contient les actifs statiques comme les feuilles de style et les images.
-   templates : Stocke les templates HTML.
-   `go.mod et go.sum` : Suivent les dépendances du projet et leurs versions.
-   `main.go` : Point d'entrée de l'application Buffalo, initialise et démarre le serveur.

Exécutez cette commande pour créer une nouvelle application Buffalo :

```
buffalo new myapp
```

### 3\. Grift : automatiser les tâches en Go

[Grift][17] est un exécuteur de tâches (task runner) idéal pour automatiser diverses tâches liées au projet. Il gère les processus de build frontend, la manipulation des actifs et l'automatisation du déploiement.

Grift s'avère précieux pour automatiser les tâches répétitives dans le workflow de développement frontend, améliorant ainsi l'efficacité et réduisant l'intervention manuelle.

**Exemple de code :**

Cet exemple démontre comment Grift peut être utilisé pour packager (bundle) et minifier des fichiers JavaScript dans un projet frontend.

Structure du projet :

![gf](https://www.freecodecamp.org/news/content/images/2023/12/gf.png)

Voici les fichiers JavaScript :

`file1.js` et `file2.js`, se trouvent dans le répertoire src.

`file1.js`

```
// file1.js
function greet(name) {
  console.log(`Hello, ${name}!`);
}
greet("John");
```

`file2.js`

```
// file2.js
function multiply(a, b) {
  return a * b;
}
console.log(multiply(3, 4));
```

#### [Tâche Grift][18]

La tâche Grift [package et minifie ces fichiers JavaScript][19] en un seul fichier nommé bundle.js. La tâche est définie dans le fichier main.go du projet.

`main.go`

```
// main.go
package main

import (
    "fmt"
    "github.com/markbates/grift/grift"
    "github.com/tdewolff/minify/v2"
    "github.com/tdewolff/minify/v2/js"
    "io/ioutil"
    "os"
    "path/filepath"
)

// BundleAndMinifyJS is a Grift task that bundles and minifies JavaScript files.
func BundleAndMinifyJS(c *grift.Context) error {
    // ... (code omitted for brevity)

    fmt.Printf("JavaScript files bundled and minified successfully. Output: %s\n", outputPath)
    return nil
}

// main function registers the Grift task and runs it.
func main() {
    grift.Desc("bundle-js", "Bundle and minify JavaScript files")
    grift.Add("bundle-js", BundleAndMinifyJS)

    taskName := "bundle-js"
    context := &grift.Context{}
    if err := grift.Run(taskName, context); err != nil {
        if err.Error() == "task not found" {
            fmt.Println("Task not found.")
            os.Exit(1)
        }
        panic(err)
    }
}
```

#### Exécution de la tâche Grift

Pour exécuter la tâche Grift, lancez la commande suivante dans votre terminal :

```
go run main.go bundle-js
```

Cette tâche Grift packagera et minifiera `file1.js` et `file2.js` en un seul fichier nommé `bundle.js` dans le répertoire dist.

Voici la sortie, montrant le nouveau répertoire et le fichier `bundle.js` créé, ainsi que le message affiché dans le terminal :

![gjs](https://www.freecodecamp.org/news/content/images/2023/12/gjs.png)

### 4\. Gomponents : créer des composants UI web en Go

[Gomponents][20] est une bibliothèque pour générer des composants HTML en Go. Elle simplifie la création de [composants UI pour les applications frontend][21].

[Gomponents][22] est particulièrement utile lorsque vous souhaitez générer des composants HTML dynamiquement dans votre code Go, offrant ainsi plus de flexibilité et d'abstraction dans la construction des interfaces utilisateur.

**Exemple de code :** Cette application web montre comment utiliser Gomponents et est inspirée de l'exemple [Gomponents tailwindcss][23] de [Markus Wüstenberg][24].

Créez un fichier `main.go` et saisissez le code ci-dessous :

```
package main

import (
    "fmt"
    "net/http"

    g "github.com/maragudk/gomponents"
    c "github.com/maragudk/gomponents/components"
    . "github.com/maragudk/gomponents/html"
)

func main() {
    http.Handle("/", createHandler("Welcome!", simpleComponent("Hello, this is the main page!")))
    http.Handle("/contact", createHandler("Contact", simpleComponent("Contact us!")))
    http.Handle("/about", createHandler("About", simpleComponent("About this site!")))

    // Print a message indicating that the server is running
    fmt.Println("Server is running on http://localhost:8080")

    _ = http.ListenAndServe("localhost:8080", nil)
}

func createHandler(title string, body g.Node) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        _ = Page(title, r.URL.Path, body).Render(w)
    }
}

func simpleComponent(content string) g.Node {
    return Div(
        H1(g.Text(content)),
        P(g.Text("This is a simple component.")),
    )
}

func Page(title, path string, body g.Node) g.Node {
    return c.HTML5(c.HTML5Props{
        Title:    title,
        Language: "en",
        Body: []g.Node{
            Navbar(path),
            Container(body),
        },
    })
}

func Navbar(currentPath string) g.Node {
    return Nav(Class("navbar"),
        Container(
            NavbarLink("/", "Home", currentPath == "/"),
            NavbarLink("/contact", "Contact", currentPath == "/contact"),
            NavbarLink("/about", "About", currentPath == "/about"),
        ),
    )
}

func NavbarLink(path, text string, active bool) g.Node {
    return A(Href(path), g.Text(text),
        c.Classes{
            "active": active,
        },
    )
}

func Container(children ...g.Node) g.Node {
    return Div(Class("container"), g.Group(children))
}
```

Exécutez le code avec cette commande pour démarrer le serveur :

```
go run main.go
```

Ensuite, saisissez cette URL dans votre navigateur pour voir les composants Go : http://localhost:8080 comme illustré ici :

![gomp](https://www.freecodecamp.org/news/content/images/2023/12/gomp.png)

Et nous avons les composants Home, About et Contact construits avec [Gomponents][25].

### 5\. Present : un outil de présentation basé sur Go

[Present][26] est un outil de l'écosystème Go utilisé pour créer des supports de présentation (slide decks). Il permet aux développeurs de générer des présentations techniques ou de la documentation directement en Go.

Present est bénéfique lorsque vous devez créer et partager des présentations techniques sur des sujets de développement frontend, des mises à jour de projet ou toute autre information pertinente.

Voici comment vous pouvez utiliser Present dans vos projets :

Tout d'abord, créez un fichier nommé `presentation.slide` dans votre éditeur de code et saisissez cet exemple de code :

```
# My Frontend Tech Talk

---

## Agenda

1. Introduction
2. Project Scope
3. Live Demo
4. Q&A
```

Ensuite, écrivez le contenu de votre présentation en utilisant [CommonMark][27], un langage de balisage simple. Utilisez des titres (#) pour les diapositives et --- pour les séparer.

Installez l'outil [Present][28] comme ceci :

```
go get -u golang.org/x/tools/cmd/present
```

Ensuite, lancez l'outil Present dans le répertoire contenant votre fichier de présentation. Votre navigateur affichera alors la présentation.

```
present
```

## Pourquoi utiliser les outils Go dans les projets frontend ?

-   **Efficacité :** Les outils Go sont conçus pour améliorer l'efficacité, automatiser les tâches répétitives et réduire l'intervention manuelle dans les workflows de développement frontend.
    
-   **Performance :** Des outils comme [Fiber][29] sont optimisés pour la performance, garantissant que votre communication frontend-backend est rapide et réactive.
    
-   **Cohérence :** Les conventions et la structure de projet de [Buffalo][30] favorisent la cohérence, permettant aux développeurs de se concentrer sur la création de fonctionnalités plutôt que sur le code boilerplate.
    
-   **Flexibilité :** La capacité de [Gomponents][31] à générer des composants HTML dynamiquement en Go offre une grande flexibilité dans la construction d'interfaces utilisateur au sein même du langage.
    
-   **Documentation et Présentation :** [Present][32] simplifie la création de présentations techniques et de documentation, gardant les informations et les mises à jour de votre projet organisées.
    

L'intégration fluide des outils Go non seulement rationalise le développement, mais s'aligne également sur la philosophie de simplicité et d'efficacité de Go.

Expérimentez avec ces outils, et vous verrez l'impact positif qu'ils peuvent avoir sur votre workflow.

Bon code ! 💜

[1]: https://go.dev/
[2]: https://blog.boot.dev/golang/become-golang-backend-dev/
[3]: https://go.dev/doc/install
[4]: https://code.visualstudio.com/
[5]: https://www.jetbrains.com/go/
[6]: https://zed.dev/
[7]: https://go.dev/doc/
[8]: https://www.freecodecamp.org/news/go-beginners-handbook/
[9]: https://gofiber.io/
[10]: https://expressjs.com/
[11]: https://github.com/Tabintel/go-tools/tree/master/fiber
[12]: https://docs.gofiber.io/guide/templates/
[13]: https://docs.gofiber.io/api/app/#:~:text=Use%20the%20Static%20method%20to,a%20request%20on%20a%20directory.&text=If%20you%20want%20to%20have,settings%20for%20serving%20static%20files.
[14]: https://gobuffalo.io/
[15]: https://pkg.go.dev/github.com/facily-tech/go-scaffold
[16]: https://medium.com/@adamszpilewicz/effortless-hot-reloading-in-golang-harnessing-the-power-of-viper-4b54703f7424
[17]: https://github.com/markbates/grift
[18]: https://github.com/markbates/grift
[19]: https://medium.com/everything-for-developers/minification-and-bundle-c8e8908ae5c8
[20]: https://www.gomponents.com/
[21]: https://www.sencha.com/blog/7-reasons-to-use-ui-component-libraries-to-style-web-apps/#:~:text=A%20UI%20component%20library%20is,front%2Dend%20applications%20and%20websites.
[22]: https://www.gomponents.com/
[23]: https://github.com/maragudk/gomponents/blob/main/examples/tailwindcss/tailwindcss.go
[24]: https://www.linkedin.com/in/markus-w%C3%BCstenberg/
[25]: https://www.gomponents.com/
[26]: https://pkg.go.dev/golang.org/x/tools/present?utm_source=godoc
[27]: https://commonmark.org/help/tutorial/
[28]: https://pkg.go.dev/golang.org/x/tools/present?utm_source=godoc
[29]: https://gofiber.io/
[30]: https://gobuffalo.io/
[31]: https://www.gomponents.com/
[32]: https://pkg.go.dev/golang.org/x/tools/present?utm_source=godoc