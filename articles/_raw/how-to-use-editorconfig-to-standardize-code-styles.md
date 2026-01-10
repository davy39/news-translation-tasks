---
title: Why You Should Use EditorConfig to Standardize Code Styles
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2021-07-21T21:28:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-editorconfig-to-standardize-code-styles
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/untitled.png
tags:
- name: automation
  slug: automation
- name: configuration
  slug: configuration
- name: configuring settings
  slug: configuring-settings
- name: editor
  slug: editor
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'You use EditorConfig to define formatting conventions for textual files
  in a project. It''s great because it''s widely supported, and it''s not tied to
  any particular language, framework, or code editor.

  EditorConfig on its own is just a vendor-agnostic...'
---

You use [EditorConfig](https://editorconfig.org/) to define formatting conventions for textual files in a project. It's great because it's widely supported, and it's not tied to any particular language, framework, or code editor.

EditorConfig on its own is just a vendor-agnostic configuration file. It relies on third-party tools or integrations to implement support for the rules declared in the file.

They can be read by IDEs (Integrated Development Environments), code editors, or build tools to enforce or apply formatting conventions.

## What Does EditorConfig Solve?

Users usually configure the code style settings in an editor to *their* preferences. Unfortunately, their preferences probably don't correlate with yours.

What happens when they're contributing to a shared project? This might be a project at work, or an open-source project on GitLab or GitHub.

The user's style settings get applied to the files they modify. This can result in projects feeling inconsistent or messy, with some or all of the following issues:

* Mixed use of tabs and spaces.
    
* Mixed use of line endings. (Usually not a significant issue with [Git](https://git-scm.com/).)
    
* Files may not have the desired character encoding.
    
* Various indentation sizes across files.
    

Without consistency, the code can appear untidy and be a pain to read, depending on a user's development environment.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/3.png align="left")

[*eclipse.jdt.ls*](https://github.com/eclipse/eclipse.jdt.ls/blob/master/org.eclipse.jdt.ls.core/src/org/eclipse/jdt/ls/core/internal/EventNotification.java?ts=8) *mixes tabs and spaces, here's how it looks on GitHub with a tab size of 8.*

A common solution is to share editor settings as part of the project, but this assumes all committers are using the same editor as you, which probably isn't the case.

For Java development alone, the following are all popular choices:

* [Visual Studio Code](https://code.visualstudio.com/) (What I use!)
    
* [Eclipse](https://www.eclipse.org/)
    
* [IntelliJ](https://www.jetbrains.com/idea/)
    
* [NetBeans](https://netbeans.apache.org/)
    

You'll bloat your project with unrelated files if you add the configuration for every editor someone might use.

So, how about a vendor-agnostic solution where editors are responsible for utilizing a shared configuration instead?

## How EditorConfig Helps

Defining conventions helps everyone throughout a project's life-cycle. There are namely three ways it saves time.

### EditorConfig Makes Code More Readable

Making code more readable is by far the most important reason to use it. This improves the maintainability of the project, and the speed that people can work.

> “Indeed, the ratio of time spent reading versus writing is well over 10 to 1. We are constantly reading old code as part of the effort to write new code… Therefore, making it easy to read makes it easier to write.”  
> ― Robert C. Martin

There are many other reasons someone might be reading the code outside of development too:

* Researchers that need to better understand how the project works.
    
* Security analysts that are checking for vulnerabilities.
    
* Technical writers that are documenting application behavior.
    

People will be able to perform their role more effectively if your code is kept tidy, consistent, and human-readable.

### EditorConfig Makes Code Reviews Easier

As a project maintainer, you'll inevitably have to review code contributed by others. They might be a fellow team member, or open-source contributors that discover your project.

Enforcing formatting should be delegated to software. This will make reading and reviewing the code more efficient, and avoids the need to request changes based on formatting.

Reducing the feedback loop ultimately saves everyone time.

### EditorConfig Makes Development Easier

Developers can save a lot of headache by having conventions that are automatically applied by their editor.

Without it, they have to find a contribution guide, style guide, or check other code manually to learn project conventions.

Even when the conventions are known, they may conflict with a developer's settings. Then they'll have to code against the editor's automatic formatting, or frequently change settings between projects.

This is especially useful for developers that jump between projects a lot. For example, open-source contributors frequently write code for projects across organizations that follow different coding conventions.

## How EditorConfig Works

EditorConfig uses a simple [INI](https://en.wikipedia.org/wiki/INI_file)\-like file named `.editorconfig`. This file declares rules that will be translated to settings in your editor, or perform formatting over your workspace.

For example, in my editor I use 2-space indentations for XML files, but a project I contribute to might prefer 4-space indentations.

```plaintext
[*.xml]
indent_size = 4
```

When I open the project, my editor will see the `.editorconfig` file, and override the settings to suit the project's conventions.

![Instance of Visual Studio Code. There is an XML file on the left side which uses spaces as defined in the EditorConfig, but my default indentation size of 2.](https://www.freecodecamp.org/news/content/images/2021/07/1.png align="left")

*Writing an XML file with my default editor settings. I use spaces for indentation with a size of 2.*

![Instance of Visual Studio Code. The EditorConfig configuration includes an XML section that sets the indentation style to tab and size to 4. The XML file on the left is reformmated to reflect this change.](https://www.freecodecamp.org/news/content/images/2021/07/2-1.png align="left")

*Automatically reformatting the file after overriding the XML formatting settings.*

## How to Use EditorConfig

Depending on your editor of choice, it may have native support for EditorConfig already. There is a list of "[No Plugin Necessary](https://editorconfig.org/#pre-installed)" editors on the website, which includes JetBrains IDEs and Visual Studio.

If your editor doesn't have native support, you'll likely be able to add it with a plugin. Editors like Visual Studio Code and Eclipse support it this way, which can also be found on the EditorConfig website under "[Download a Plugin](https://editorconfig.org/#download)".

Once installed, your editor should automatically find the EditorConfig file in your project if it exists, and start applying the rules.

## How to Define Rules in EditorConfig

You can find a list of rules on the [EditorConfig Wiki](https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties). It contains all officially supported rules, as well as proposals for domain-specific rules that may be supported by certain implementations.

Not all implementations support every rule. This is especially true for domain-specific rules like `curly_bracket_next_line`. It can still be worth declaring these properties anyway for users that can utilize it, or to at least document the preference.

You must set `root` to `true` for the top level EditorConfig in the project, which is normally in the root of your project directory.

Additional EditorConfig files can be defined in nested directories, but shouldn't set `root` to `true`.

Then you can define a header that selects files, with rules for what to apply to matching files.

```plaintext
# Declares that this is the top-level configuration
root = true

# Applies to all files
[*]
indent_style = space
indent_size = 2

# Applies to all Markdown files
[*.md]
trim_trailing_whitespace = false

# Applies to all C# and Java files, overriding rules declared before
[*.{cs,java}]
indent_size = 4
```

There are no standard conventions for how to write an `.editorconfig` file, but there are two notable approaches you can take.

### Define Rules Per Project

Just add to it as you need to. This means just defining rules, or appending file formats as your project grows.

You can start by generating the file with your editor, or just create a file named `.editorconfig` manually. You can copy-and-paste the [example](https://editorconfig.org/#example-file) from the official website.

### Define Rules for All Projects

Alternatively, you can put together all of your preferences and plan the ideal configuration for all files you might interact with.

You can work from scratch, or start with mine and make the necessary adjustments.

```plaintext
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
curly_bracket_next_line = false
spaces_around_operators = true

[*.bat]
end_of_line = crlf

[*.cs]
curly_bracket_next_line = true

[*.{cpp,cs,gradle,java,kt,py,rs}]
indent_size = 4

[*.{js,ts}]
quote_type = single

[*.md]
trim_trailing_whitespace = false

[*.tsv]
indent_style = tab
```

## EditorConfig Rule Recommendations

These are rules I'd objectively recommend declaring, if your project contains the respective file format. It'll help you avoid tedious issues that can occur due to a user's development environment.

### Batch

Line endings need to have a textual representation when stored. This is usually something you wouldn't see or have to worry about.

However, different systems use different characters to represent the end of a line. ([More Info](https://en.wikipedia.org/wiki/Newline#Representation))

* Unix systems use a line feed. (`lf` or `\n`)
    
* Windows uses a carriage return and line feed. (`crlf` or `\r\n`)
    

[Batch](https://en.wikipedia.org/wiki/Batch_file) files can have unexpected behavior if they end with Unix line endings. You can avoid this by setting `end_of_line` to `crlf` to ensure they have Windows line endings instead. ([More Info](https://serverfault.com/questions/429594/is-it-safe-to-write-batch-files-with-unix-line-endings))

```plaintext
[*.bat]
end_of_line = crlf
```

### Markdown

In [Markdown](https://en.wikipedia.org/wiki/Markdown), you can write a line break in the current paragraph by adding 2 spaces at the end of a line. ([More Info](https://en.wikipedia.org/wiki/Markdown#Example))

You'll want to set `trim_trailing_whitespace` to `false` to avoid having your editor remove those spaces when you save.

```plaintext
[*.md]
trim_trailing_whitespace = false
```

### Tab Separated Values

[TSV](https://en.wikipedia.org/wiki/Tab-separated_values) (Tab Separated Values) files are very similar to [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) (Comma Separated Values), but use tabs instead of commas as the column delimiter.

It's very common for developers to have tabs automatically convert to spaces. You should set `indent_style` to `tab` to avoid the delimiter from being replaced, otherwise your entire table might become a single column.

```plaintext
[*.tsv]
indent_style = tab
```

## Conclusion

If you're a maintainer, either working in a collaborative environment or in open-source, I strongly recommend adding an `.editorconfig` file defining the project's conventions to the root of your repository.

Maintainers can then spend more time reviewing clean pull requests that adhere to the style guide, as the editor will automatically start enforcing or applying the conventions.

Committers get a better experience, as the project will override their workspace settings. This reduces the need to reformat code or work against preconfigured editor settings.

And projects will be cleaner, as the conventions will be in a single vendor-agnostic file, rather than editor-specific files that only certain contributors can use anyway.
