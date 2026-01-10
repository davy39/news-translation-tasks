---
title: Visual Studio Code Extensions to Boost Your Productivity in 2024
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2024-01-24T22:42:52.000Z'
originalURL: https://freecodecamp.org/news/best-vscode-extensions
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Group-1.png
tags:
- name: Productivity
  slug: productivity
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'According to the 2023 Stack Overflow Developer Survey, Visual Studio Code
  (also known as VSCode) ranked as the most preferred integrated developer environment
  (IDE) tool.

  Visual Studio Code has many great features out-of-the-box, and supports a large...'
---

According to the [2023 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2023/#section-most-popular-technologies-integrated-development-environment), Visual Studio Code (also known as VSCode) ranked as the most preferred integrated developer environment (IDE) tool.

Visual Studio Code has many great features out-of-the-box, and supports a large community of extensions to add enhanced functionality.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-12.01.59-PM.png align="left")

*Stack Overflow survey image showing VSCode's popularity (73.71% of respondents use it)*

Using extensions can expand VSCode's available features and tools. With a majority of tools in one place, it allows for less context switching which has been shown to [kill productivity](https://asana.com/resources/context-switching).

I have tested out over 40 different extensions in the last year and refined a curated list of my favorites. These extensions boosted my productivity as a software engineer. I want to share this list with you to boost your productivity, too.

This list is designed to be language-agnostic with an emphasis on productivity. If you're interested in exploring my recommended extensions to customize the style of your editor, you can find more details [in this article](https://www.freecodecamp.org/news/best-colorful-vscode-extensions-for-productivity/).

## VSCode Extensions We'll Cover:

* [Better Comments](#heading-better-comments)
    
* [Bookmarks](#heading-bookmarks)
    
* [Code Spell Checker](#heading-code-spell-checker)
    
* [CodeSnap](#heading-codesnap)
    
* [CodiumAI](#heading-codiumai)
    
* [Error Lens](#heading-error-lens)
    
* [Git History](#heading-git-history)
    
* [GitLens](#heading-gitlens)
    
* [GitHub Copilot](#heading-github-copilot)
    
* [Icons Themes](#heading-icon-themes)
    
* [Indent Rainbow](#heading-indent-rainbow)
    
* [Live Share](#heading-live-share)
    
* [Multiple Cursor Case Preserve](#heading-multiple-cursor-case-preserve)
    
* [Path Intellisense](#heading-path-intellisense)
    
* [Peacock](#heading-peacock)
    
* [Prettier](https://www.freecodecamp.org/news/p/db680fa0-6ecb-42b3-a803-ea6b47c90add/@prettier)
    
* [Project Manager](#heading-project-manager)
    
* [Tabnine](#heading-tabnine)
    
* [TODO Highlight](#heading-todo-highlight)
    
* [Todo Tree](#heading-todo-tree)
    

In this article, I will cover all of these extensions in greater detail and advise on how they can elevate your levels of efficiency as a developer.

## Better Comments

[Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) helps you strengthen the comments in code. Code comments are beneficial for readability, and providing explanations or context for future reference. Leaving good code comments can save others and yourself time in the future.

Supported features include the ability to categorize the annotations from alerts, writing queries, making a TODO list, and showing highlights. There is an extensive list of supported languages.

Lines of code that are commented out are styled to be dark gray with a text strikethrough, emphasizing their exclusion and signaling that they should be removed.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/better-comments.png align="left")

*Styled code comments with Better Comments.*

## Bookmarks

[Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks) allows you to bookmark positions in your code. These lines are noted with a blue bookmark icon. Bookmarks can be organized and named to allow for quick reference.

All of the bookmarks can be found in a dedicated sidebar section. This is a great tool to improve navigation, and to help you spend lest time searching for references.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/printscreen-toggle.png align="left")

*Bookmarks displayed in blue with a bookmark icon next to the line number.*

## Code Spell Checker

[Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) lives up to its name. It provides a basic spell checker to find and fix spelling errors throughout your codebase. Misspelled words are indicated with a squiggly underline. It is available in many languages.

This is one of my personal favorite extensions. I have caught and fixed so many typos thanks to this one.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/example.gif align="left")

*This image displays how Spell Checker detects and corrects spelling errors.*

## CodeSnap

[CodeSnap](https://marketplace.visualstudio.com/items?itemName=adpyke.codesnap) is used to snap a screenshots of code. It can come in handy for sharing code snippets with ease.

To snap a shot of your code, use (Ctrl+Shift+P on Windows and Linux, Cmd+Shift+P on OS X) and search for `CodeSnap`. Then select the area of your code to screenshot, adjust the width, and click the shutter button. You can also take a snapshot by selecting code, right clicking, and selecting CodeSnap.

There are websites that can do this, however, having these tools right in your editor allows for less context switching to boost productivity.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/material_operator-mono.png align="left")

*Sample React code snippet created with CodeSnap.*

## CodiumAI

[CodiumAI](https://marketplace.visualstudio.com/items?itemName=Codium.codium) is a free AI-powered code toolkit. It supports features like code autocompletion, chat, enhanced search, and suggestions.

AI has become a major player in improved developer productivity. Imagine spending half the time writing tests, allowing you to spend more time on other crucial, creative tasks.

When it comes to testing, CodiumAI excels. It can analyze code and generate meaningful tests and comprehensive test suites.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Tests-Gif.gif align="left")

*CodiumAI generating a test suite based on a section of Python code.*

This is a relatively new extension and that has been rapidly gaining popularity. Languages supported are Python, JavaScript, TypeScript, Java, Go, and others.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/g_python_random_gen_with_logo.gif align="left")

*CodiumAI's autocomplete functionality used to create functions based on natural language prompts.*

## Error Lens

[Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) improves highlighting of errors, warnings, and other language diagnostics. This is a great debugging and error-prevention tool to have.

Errors will not go unnoticed with this extension. Error and warnings are made prominent by highlighting the entire line, along with the related message printed inline.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/demo.png align="left")

*Error Lens identifying an error, notifying that there is a missing semicolon and a syntax error.*

Spend less time sourcing errors, as clicking on an an annotation routes you directly to the corresponding line of code.

There is support for multiple languages which makes it a valuable for developers working in projects in different languages. You can also configure the appearance and behavior of errors and warnings.

## Git History

[Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) is an extremely useful extension for version control with Git (the extension has 10 million installs, so it's clear that it's popular). This extension allows you to explore the detailed history of your Git repository directly from the VSCode interface. You can view file history, git log, and perform comparisons.

It provides an interactive and visual representation of commit logs, branches, and file changes over time. This extension provides a more accessible and uncomplicated experience working on version-controlled projects.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/gitLogv3--1-.gif align="left")

*Git History is being used here to create a tag on a specific commit.*

## GitLens

[GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) is the most robust Git tool, with so many features bundled into one extension. It has a strong open-source community, and it continues to have active support with frequent updates.

With GitLens, you can gain powerful insights into your repositories directly in VSCode. Annotations are integrated throughout the editor, displaying tons of Git information.

One of the most useful features of GitLens is the blame annotation. This allows you to see who wrote the code, and how long ago.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/current-line-blame.png align="left")

*GitLens traces the line of code to a commit created 4 years ago from the user (You).*

Another feature that I have found to be handy is the interactive rebase editor. This provides a nice user experience when performing rebases.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/rebase.gif align="left")

*GitLens' example of an interactive rebase. Commits can be picked, edited, dropped, squashed, and more.*

## GitHub Copilot

[GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) has gained a ton of traction over the last two years. This product has revolutionized the coding experience by leveraging advanced AI capabilities. It not only assists with completing code snippets but also acts as an AI pair programming copilot, offering intelligent suggestions for entire lines or blocks of code.

The strength of GitHub Copilot lies in its integration with OpenAI, tapping into a vast repository of open-source code to provide contextually relevant and practical suggestions. This not only accelerates coding speed but also serves as a valuable learning tool, exposing you to diverse coding patterns and best practices.

This is not a free tool. A subscription can run you $10 per month as an individual, or it can be purchased for teams at a discounted rate. If you'd like to try out GitHub Copilot, there is currently a 30-day trail offer.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/212964557-8d832278-61bb-4288-a8a7-47f35859e868.gif align="left")

*GitHub Copilot using intelligent autocomplete on a function.*

There are also some free alternatives which you can [read more about here](https://www.freecodecamp.org/news/ai-tools-to-use-in-vs-code/) (and I talk about Tabnine below as well).

## Icon Themes

While VSCode includes default icons, incorporating icon packs provides an excellent means to boost productivity and infuse a visually appealing aesthetic into the editor.

Icon packs provide a more extensive and visually recognizable set of icons compared to the defaults. This can make it easier for visual distinction between file types and folders. It can build intuitive recognition and reduce the cognitive load when navigating through files.

There are plenty of options when it comes to choosing an icon pack. Three popular choices are the [Material Theme Icons](https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme-icons), [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons), and [file-icons](https://marketplace.visualstudio.com/items?itemName=file-icons.file-icons).

I find that a good set of icons improves the overall readability of the file explorer. I enjoy the added benefits of the upgraded visual experience.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Group-2.png align="left")

*Side-by-side comparison of my editor with the vscode-icons (left) and Material Icon Theme (right) enabled. There are icons for file types and folders that indicate what they contain.*

## Indent Rainbow

[Indent Rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) is a colorful extension that you can use to make indentation comprehensible, aiding in maintaining well-organized and properly indented code.

Each indent is marked with a different color, alternating between 4 different colors. The colorful representation of the structure is not only useful but also visually appealing. This extension is particularly useful for languages that rely heavily on indentation such as YAML or Python.

If you aren't fond of the default set of colors, you can configure your own!

![Image](https://www.freecodecamp.org/news/content/images/2024/01/example--1-.png align="left")

*A side-by-side comparison of two styles from Indent Rainbow. The one on the left shows the lines of the indent in vibrant color and the other shows the entire indention in a muted tone.*

## Live Share

[Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) is a collaborative development extension, enabling real-time sharing.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-18-at-12.10.57-PM.png align="left")

*The Live Share header in the extension marketplace. There are 15 million installs.*

This extension helps you facilitate productive teamwork. Unlike traditional pair programming sessions, Live Share lets you work together while retaining your own editor preferences. Each person has their own cursor, and you can follow each others' cursors around the codebase.

With Live Share, there is no need to clone repositories or encounter conflicts when working off of a shared branch. Context is immediately gained from the environment when entering a session.

## Multiple Cursor Case Preserve

The [Multiple Cursor Case Preserve](https://marketplace.visualstudio.com/items?itemName=Cardinal90.multi-cursor-case-preserve) extension is a productivity-boosting tool that aids in rapid code editing.

I have personally experienced the frustration when targeting multiple variable names throughout a file for renaming, and inadvertently overriding casing when making a change.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Example--1-.gif align="left")

*Targeting multiple variables with the same word but different casing, and updating them all from 'element' to 'node' with the casing remaining in tact.*

### Tip: Multi-Line Editing in VSCode

Take advantage of these Mac keyboard shortcuts for multi-line editing:

* **Cmd + D:** Quickly select a word and press it again to extend the selection to sequential occurrences.
    
* **Alt + Shift + Up/Down:** Create multiple cursors above or below your cursor. Use `Cmd + Right/Left` to navigate each cursor to the line end or start, and `Cmd + Left/Right` to reach the start or end of a word.
    
* **Alt + Up/Down:** Move the current line up or down. Combine with `Shift + Up/Down` to select and move multiple lines simultaneously, streamlining your code editing process.
    

By preserving the case, it streamlines the editing process by reducing the manual effort required to fix casing.

## Path Intellisense

[Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) is a file path productivity tool. It has intelligent auto-completion that dynamically suggests file paths and directory names as you type. It can minimize errors due to incomplete or wrong file paths.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/iaHeUiDeTUZuo.gif align="left")

*Path Intellisense used to auto-complete a link element's 'href' attribute with a style.css file.*

It is compatible with a variety of programming languages. But if you are using npm, the [npm Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.npm-intellisense) plugin is recommended specifically.

## Peacock

[Peacock](https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock) is a personal favorite of mine, as I love to add more color to my editor. Not only does it outline your editor in color, but it also allows you to configure specific colors for each workspace which is very beneficial when context switching.

Peacock comes with a range of preselected colors, while also allowing for user-defined custom colors.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/peacock-windows.png align="left")

*A stack of editors from Peacock showing the various default color options. The color is applied to the sidebar and bottom section in the editor window.*

## Prettier

[Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) is a widely embraced code formatting tool with over 40 million installations. It provides you with a shared solution to improve code readability.

This opinionated code formatter enforces consistent style throughout a codebase. With support for various programming languages, Prettier automatically analyzes and formats code according to a set of standardized rules, this eliminates debates over coding style and enhancing collaboration.

Prettier's integration with "format on save" in VSCode vastly increases productivity by automatically applying formatting, preventing any time spent on manual formatting concerns.

You've probably already heard about Prettier, nonetheless it's important to mention as one of the top extensions to have.

## Project Manager

[Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager) is a simple tool to set projects (aka Favorites) and access them. It includes a dedicated side bar section to manage all of your projects in one place.

This is great tool when you have a lot of projects to manage and need to frequently switch between them. It comes with a set of handy features like the ability to further organize projects by tags.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/vscode-project-manager-side-bar-tags.gif align="left")

*Project Manager's example of how to create a tag by selecting 'Edit Tags', choosing from the previously created tags, and where to view them under Favorites.*

## Tabnine

[Tabnine](https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode) is an free AI coding assistant. It can help to increase your productivity by providing real-time code completions.

Beyond basic code completion, it takes in the context and offers further relevant suggestions. This can be particularly useful when working in intricate codebases demanding extensive code exploration.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/completions-main.gif align="left")

*Tabnine's example of autocompletion. The autocomplete is used to quickly create Python and TypeScript code.*

Tabnine supports many programming languages. Adaptive learning is used to adjust to the developer's coding style over time. There is an added focus on privacy, as code is never stored or shared.

As I mentioned above, Tabnine is often compared to as a GitHub Copilot alternative, and worth trying out at no cost. Keep an eye out on this one as they add new competitive features.

Support for this extension is strong with continual updates. Chat functionality is soon to come, allowing you to ask questions and generate anything from code to documentation.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/260391624-68c486fc-fa0d-4cfe-b8e1-432684b057d8.gif align="left")

*Example from Tabnine of how the new AI chat functionality will look. The user asks for a weather API and Tabnine responds with several examples.*

## TODO Highlight

Never forget another to-do with [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight). It emphasizes `TODO`s and other annotations with a colorful highlight.

It is common to encounter a `TODO` or `FIXME` relic of the past in a codebase that has been around for awhile. These can be hard to remember to remove. TODO Highlight is here to help remind you to not leave a trail.

Wether your theme is light or dark, TODO Highlight will put a spotlight on annotations.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/material-night-eighties.png align="left")

*Some JavaScript code with a TODO highlighted in yellow along with a FIXME highlighted in pink.*

## Todo Tree

[Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) offers a quick and organized solution to uncover annotations. It searches your workspace for `TODO` and other annotations and organizes them in a file tree.

It occupies a specific section in the side activity bar. Clicking on each `TODO` opens the related file, where the `TODO` is highlighted for immediate attention.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/screenshot.png align="left")

*The TODO Tree sidebar section with a selected to-do of 'TODO Fix this!'. In the code to the right, the 'TODO' is highlighted with a bright purple color.*

## Summary

VSCode stands out for its expansive extension ecosystem, making it a go-to choice for developers. Having thoroughly tested an array of popular extensions, I've carefully curated this list of my top recommendations.

This list is a great place to start from and build on. I highly encourage you to implement routine trial periods with new extensions. Delve into other extensions through the [Visual Studio Code extension search](https://marketplace.visualstudio.com/vscode).

Recognizing the importance of minimizing cognitive load for sustained focus, each extension on this list is chosen with the goal of reducing unnecessary mental burdens like context switching. Make VSCode become your main hub of development needs, and you an improved focus mode along with other benefits.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-23-at-10.33.01-AM-1.png align="left")

I hope these recommendations allow you to optimize your workflow, minimize distractions, and ultimately boost your productivity!
