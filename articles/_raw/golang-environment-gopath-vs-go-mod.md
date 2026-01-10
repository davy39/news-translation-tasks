---
title: Golang Environment – GOPATH vs go.mod
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-26T00:23:11.000Z'
originalURL: https://freecodecamp.org/news/golang-environment-gopath-vs-go-mod
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-james-wheeler-1578750.jpg
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: null
seo_desc: "By Otavio Ehrenberger\nIn this article, we'll explore the differences between\
  \ the traditional GOPATH environment and the go.mod based environment for Go programming.\
  \ \nThis distinction has significant implications for how Go developers structure\
  \ and ma..."
---

By Otavio Ehrenberger

In this article, we'll explore the differences between the traditional `GOPATH` environment and the `go.mod` based environment for Go programming. 

This distinction has significant implications for how Go developers structure and manage their project workspaces and dependencies.

We'll start by understanding the `GOPATH` environment, its organization and its structure. Then we'll explore the `go.mod` approach, adopted to provide a modular and flexible way of organizing Go projects. 

Understanding these two environments and the transition from `GOPATH` to `go.mod` provides valuable insights into Go's evolving ecosystem.

# Single Workspace – the GOPATH Environment Variable

The Go programming language initially delimited a scope for the location of dependencies and custom projects inside a filesystem. This was defined by the `GOPATH` environment variable. This means that Go would look for binaries and source code only under the directory pointed to by this variable.

The `GOPATH` variable by default would point to a `/go` folder defined directly under the user home directory path (`~/` in unix-based or `%HOMEPATH%` on windows-based systems).

`GOPATH` could also be set to custom paths, and more than one `GOPATH` could be defined for a single user (but this was discouraged due to added difficulties in dependency management).

There are three notable directories under `GOPATH`: `src`, `pkg`, and `bin`. The `src` directory holds the source code of both your projects and installed dependencies. When you execute a command such as `go get github.com/user/repo`, the Go tool fetches the module from the specified location and places it into the `src` directory under the `GOPATH`, with a path named after the resource's URL.

For instance, if you were to download a library from a repository owned by "someuser" on GitHub, the library's source code would reside in `/home/user/go/src/github.com/someuser/library`.

The `pkg` directory contains compiled package objects (.a files) that your code depends on. When a package is built, the resulting file is placed in the `pkg` directory. The compiled package files help in reducing compilation time as they can be imported directly in other packages without the need for recompilation.

The `bin` directory holds the binary executables of your applications. When you build an executable program, the resulting binary file is placed in the `bin` directory.

## File Tree for a GOPATH Workspace

This assumes the default path for `GOPATH`:

```
/home/user/go/         <--- This is your GOPATH
├── bin/
├── pkg/
│   └── linux_amd64/
│       └── github.com/
│           └── someuser/
│               └── somelib.a    <--- Compiled dependency package
└── src/
    ├── github.com/
    │   └── someuser/
    │       └── somelib/         <--- Dependency's source code
    │           └── somelib.go
    └── myapp/                   <--- Your project
        └── main.go

```

In this structure:

* The src directory contains the source code of your projects and the installed dependencies.
* The pkg directory contains compiled versions of the packages that your code depends on.
* The bin directory contains the compiled binary executables.

The single workspace structure defined by `GOPATH` means that all your Go code and its dependencies share a single common space. 

It's worth noting, however, that this approach has evolved with the introduction of Go modules in Go 1.11. This mainly addresses the lack of a proper versioning system for dependencies and flexibility to store projects under a filesystem.

# Modular Approach – the `go.mod` File

Starting from Go 1.11 (August 2018), the modular option became available as an alternative to a workspace defined by `GOPATH`. This is delimited by the presence of a `go.mod` file and also usually a go.sum file, generated once any operation concerning externally hosted packages is executed (like `go get <package>`).

Before continuing, however, it is important to clarify what a package is and how a module differs from a package:

## Packages in Go

A package in Go is the smallest unit of code distribution. They are defined by a directory containing one or more `.go` source files with the package name declared on top of it. All files in the directory must declare the same package name.

Packages allow code to be organized and reused. They provide a way of encapsulating related code into a single unit, which can be imported and used by other packages. The Go standard library, for example, consists of many packages such as fmt, os, net, and so on.

There is a single special package name, `main`.  This package contains the `main()` function which is the entry point for a project. Every project meant to eventually become an executable must contain the `main()` function, and therefore the `main` package.

It is a good practice to declare the main package file(s) at the project's root folder and other packages in their own directories.

## Modules in Go

A module is a collection of related Go packages that are versioned together as a single unit. Modules record precise dependency requirements and create reproducible builds. 

A Go module is defined by a go.mod file that resides at the root of the module's directory hierarchy. This file defines the module path, which is the import path prefix for all packages within the module. It specifies the dependencies of the module, including the required versions of other modules.

Modules allow for versioning and releasing a set of packages together, and they also make dependency version information explicit and easier to manage. Note that, though versioned, **dependencies will still be downloaded under `src` defined in the `GOPATH` scope by default**.

To summarize, while a package is a way of structuring and reusing code within a Go program, a module is a versioned collection of packages that also handles dependency management. This allows each Go project to have its own isolated and reproducible build environment.

## Naming Conventions for Modules

In Go, **module names are used system-wide and therefore should be as specific as possible,** especially if you plan on distributing the module to other developers. The module name is specified in the `go.mod` file, which acts as the module's manifest and is located at the root of the module's directory hierarchy.

Here are some guidelines for module naming in Go:

**Module Path**: The module path should be a globally unique identifier for the module. It typically takes the form of an internet domain name in reverse order, followed by the module name. For example, `github.com/littlejohnny65/example-module`. The module path is used as an import path when importing packages from the module.

**Module Name**: The module name is the last component of the module path. It should be short, descriptive, and adhere to Go's naming conventions. It is recommended to use lowercase letters with no underscores or mixedCaps. For example, `examplemodule`.

**Versioning**: The module name itself does not include version information. The version of a module is specified separately in the `go.mod` file using a module version identifier, such as `v1.2.3`. The combination of the module path and the version identifier uniquely identifies a specific version of the module.

It's important to choose meaningful and descriptive names for modules, as they are publicly identifiable and may be used as dependencies in other projects. Clear and consistent naming conventions help in understanding the purpose and context of a module.

## The go.sum File

When you run a command like `go get github.com/user/repo`, the Go tooling will fetch the module from that location. This makes it possible to host Go code on any server that supports version control systems like Git, Mercurial, Bazaar, or Subversion.

Go has a very flexible and direct approach to download dependencies from external repositories. So the solution adopted in order to ensure the dependency's integrity is to create a local file to store a checksum for each dependency. This is what guarantees that the dependency installed is the exact same.

The checksum file is generated by the local Go tooling. It **should be pushed to external environments** such as servers and Dockerfiles if you want to make sure the dependencies will be exactly the same as in your local environment.

## File Tree for a Modular Go Project

```
/home/user/projects/
└── myapp/                         # Your project
    ├── custom/                   # Custom packages
       └── ...                          # .go files defining functionality
    ├── go.mod                     # go.mod file defining dependencies & versions
    ├── go.sum                     # go.sum file that verifies dependency integrity
    └── main.go                    # Entrypoint

```

File tree for the module cache, assuming the default GOPATH path:

```
/home/user/go/        # This is your GOPATH
└── pkg/
    └── mod/
        └── cache/
            └── download/
                └── github.com/
                    └── someuser/
                        └── somelib/     # Source code of the dependency
                            └── somelib.go

```

In this structure:

* Your project can live anywhere in your file system. It contains a go.mod file and a go.sum file.
* The go.mod file lists the specific versions of the dependencies that your project uses.
* The go.sum file provides checksums for the exact contents of each dependency at the time it is added to your module.
* The dependencies are stored in the Go module cache, which is shared across all projects on your system.

# Module CLI Commands

There are several convenient commands available for working with modular Go projects:

**`go mod init`**: Initializes a new module in the current directory. It creates a `go.mod` file that defines the module's path and sets it up for dependency management.

**`go mod tidy`**: Adds missing and removes unused modules and dependencies from the `go.mod` file. It ensures that the `go.mod` file accurately reflects the required dependencies of your project.

**`go mod download`**: Downloads the dependencies defined in the `go.mod` file and stores them in the module cache. It fetches the specific versions of the dependencies needed for your project.

**`go mod vendor`**: Copies the dependencies into a `vendor` directory within your project. This command is useful when you want to create a self-contained project that includes all its dependencies.

**`go mod verify`**: Verifies that the dependencies in the module cache match the expected cryptographic checksums specified in the `go.sum` file. It ensures the integrity and authenticity of the downloaded dependencies.

**`go mod graph`**: Prints the module dependency graph, showing the relationships between modules and their versions. It can be useful for understanding the overall structure of your project's dependencies.

**`go mod edit`**: Provides a range of subcommands for making manual edits to the `go.mod` file. It allows you to add, remove, or update module requirements, replace modules, and more.

These are just a few of the commonly used `go mod` commands. You can explore more commands and their options by running `go help mod` or referring to the official Go documentation on modules.

# Wrapping up

The modular approach is not radically different from nor incompatible with the single workspace. But it builds on it to bring more flexibility and manageability. 

Modules allow you to have a project wherever you want to in your filesystem and also to have namespaced dependencies for better stability. But it still uses GOPATH as the default location to store dependencies and executables.

In conclusion, the modular environment provided by go.mod is a powerful tool in the Go developer's toolbox, complementing and extending the functionality of the traditional GOPATH environment. It signals Go's adaptation to the increasing complexity and scale of modern software development, demonstrating the language's ongoing evolution to meet the changing needs of its users. 

As we move forward, it's exciting to imagine what future developments in Go's ecosystem will bring.

