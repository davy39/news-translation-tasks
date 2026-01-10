---
title: 'An intro to dep: How to manage your Golang project dependencies'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-02T20:23:34.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-dep-how-to-manage-your-golang-project-dependencies-7b07d84e7ba5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nPaOoEou7T-cM9WZGtU-gg.png
tags:
- name: Dep
  slug: dep
- name: glide
  slug: glide
- name: golang
  slug: golang
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ying Kit Yuen

  Update @ 2018–11–26: Technology is not just moving at a breakneck speed but also
  changing rapidly. Within a year, this article is OUTDATED!

  And according to the dep project page:


  dep was the “official experiment.” The Go toolchain, ...'
---

By Ying Kit Yuen

**Update @ 2018–11–26: Technology is not just moving at a breakneck speed but also changing rapidly. Within a year, this article is OUTDATED!**

And according to the [dep project page](https://github.com/golang/dep):

> _dep was the “official experiment.” The Go toolchain, as of 1.11, has (experimentally) adopted an approach that sharply diverges from dep. As a result, we are continuing development of dep, but gearing work primarily towards the development of an alternative prototype for versioning behavior in the toolchain._

For more information about the new Go build-in management, please refer to the official GitHub Wiki — [Go 1.11 Modules](https://github.com/golang/go/wiki/Modules).

Thanks [John Arundel @bitfield](https://twitter.com/bitfield) and [Erhan Yakut @yakuter](https://twitter.com/yakuter) for revealing the problem. ?

—

**Update @ 2018–02–03: [Sam Boyer](https://medium.com/@sdboyer) from the godep team has clarified some incorrect information in this article. I apologize to [Sam Boyer](https://medium.com/@sdboyer) and the readers for any inconvenience.** ?

—

Previously, I posted an [article](https://blog.boatswain.io/post/manage-go-dependencies-using-glide/) about dependency management in [Go](https://golang.org/) using [Glide.](https://glide.sh/) I got a feedback that [Glide](https://glide.sh/) will become obsolete. The [Glide](https://glide.sh/) team is suggesting users move to another dependency management tool called [dep](https://github.com/golang/dep) written by the [Golang](https://github.com/golang) team.

> The Go community now has the dep project to manage dependencies. Please consider trying to migrate from Glide to dep. Glide will continue to be supported for some time but is considered to be in a state of support rather than active feature development.

There is a plan about integrating [dep](https://github.com/golang/dep) into the toolchain in [Go 1.10 release](https://tip.golang.org/doc/go1.10), but seems [it still has a way to go](https://www.reddit.com/r/golang/comments/7dd2ty/go_110_release_notes_draft/#thing_t1_dpwyj4i).

**Update @ 2018–02–03:**

* [**dep**](https://github.com/golang/dep) **is officially released.**
* [**dep**](https://github.com/golang/dep) **is not moving into the toolchain with 1.10. please refer to the [roadmap](https://github.com/golang/dep/wiki/Roadmap) for the latest information.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*-jTtAekDfSoJn1uDzeyFVg.jpeg)
_And I am just not fast enough. ?_

### Create the project inside $GOPATH

The project folder has to be inside _$GOPATH_ in order to resolve the [Go](https://golang.org/)package paths. Let’s create a new project at _$GOPATH/src/gitlab.com/ykyuen/dep-example_ and add the following file.

**main.go**

### The dep way

#### Gopkg.toml and Gopkg.lock

[dep](https://github.com/golang/dep) reads two files called _Gopkg.toml_ and the _Gopkg.lock_. Let’s initialize these 2 files using the _dep init_ command.

```
[ykyuen@camus dep-example]$ dep init  Using master as constraint for direct dep github.com/dustin/go-humanize  Locking in master (bb3d318) for direct dep github.com/dustin/go-humanize
```

As you can see, the _dep init_ command scans the source codes and downloads all the packages needed for the project into the _vendor_ folder.

The _Gopkg.lock_ serves exactly the same function as the _glide.lock_ file. It locks the version of the packages **EXCEPT** the version should be maintained in the _Gopkg.toml_. In short, the _Gopkg.lock_ file is auto-generated and it depends on the _import_ statements in the source version controlled by _Gopkg.toml_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4rou4TKFvTSHxo_OSLp4jg.png)

#### Update dependency’s version

Let’s edit the _Gopkg.toml_ and use a slightly older version of the [go-humanize](https://github.com/dustin/go-humanize) package instead of the latest master branch.

Then run _dep ensure_ to update the package to the desired version. The following is the diff of the updated _Gopkg.lock_.

#### Add a new dependency

New package could be added using the _dep ensure -add_ command.

```
[ykyuen@camus dep-example]$ dep ensure -add github.com/leekchan/accountingFetching sources...
```

```
"github.com/leekchan/accounting" is not imported by your project, and has been temporarily added to Gopkg.lock and vendor/.If you run "dep ensure" again before actually importing it, it will disappear from Gopkg.lock and vendor/.
```

Now we have the new _accounting_ package ready in the _vendor_ folder with new constraints written to _Gopkg.toml_ and locked in _Gopkg.lock_. Let’s update the _main.go_ as follow.

**main.go**

And run it.

```
[ykyuen@camus dep-example]$ go run main.gohello worldThat file is 83 MB.You're my 193rd best friend.You owe $6,582,491.$123,456,789.21$12,345,678.00$25,925,925.67-$25,925,925.67$123,456,789.21
```

### The issue with git submodule

One major difference of [dep](https://github.com/golang/dep) compared to [Glide](https://glide.sh/) is the package’s submodule is ignored. For example, after adding the [go-goracle/goracle](https://github.com/go-goracle/goracle) package by [dep](https://github.com/golang/dep), the [odpi](https://oracle.github.io/odpi/) submodule inside is empty and leads to error. The reason for dropping the submodule could be found at the following link.

* [Are there any plans to add Git submodules support?](https://github.com/golang/dep/issues/1240)

**Update @ 2018–02–03:**

**The paragraph about Git submodules is incorrect.**

[**Sam Boyer**](https://github.com/sdboyer) **wrote:**

> _dep should be perfectly fine at pulling in git submodules in the case you describe. I just replicated what you describe here locally, and the problem isn’t submodules — it’s that there’s no Go code in github.com/go-goracle/goracle/odpi, so it can’t be imported directly._

> _You likely need to turn off unused-packages pruning in Gopkg.toml for that project specifically, as otherwise dep ensure will automatically remove what appears to be an unused directly (but it seems it’s actually used by cgo)._

**Update @ 2018–03–04:**

It is found that the [go-goracle/goracle](https://github.com/go-goracle/goracle) package doesn’t work with [dep](https://github.com/golang/dep). You could follow the issue below and check the latest update from the [dep](https://github.com/golang/dep) team.

* [Fail to get git submodule of a package after the dep ensure command](https://github.com/golang/dep/issues/1633)

### Summary

* d̶̵̶e̶̵̶p̶̵̶ ̶̵̶i̶̵̶s̶̵̶ ̶̵̶q̶̵̶u̶̵̶i̶̵̶t̶̵̶e̶̵̶ ̶̵̶l̶̵̶i̶̵̶k̶̵̶e̶̵̶l̶̵̶y̶̵̶ ̶̵̶t̶̵̶o̶̵̶ ̶̵̶b̶̵̶e̶̵̶ ̶̵̶t̶̵̶h̶̵̶e̶̵̶ ̶̵̶o̶̵̶f̶̵̶f̶̵̶i̶̵̶c̶̵̶i̶̵̶a̶̵̶l̶̵̶ ̶̵̶d̶̵̶e̶̵̶p̶̵̶e̶̵̶n̶̵̶d̶̵̶e̶̵̶n̶̵̶c̶̵̶y̶̵̶ ̶̵̶m̶̵̶a̶̵̶n̶̵̶a̶̵̶g̶̵̶e̶̵̶m̶̵̶e̶̵̶n̶̵̶t̶̵̶ ̶̵̶t̶̵̶o̶̵̶o̶̵̶l̶̵̶ ̶̵̶i̶̵̶n̶̵̶ ̶̵̶t̶̵̶h̶̵̶e̶̵̶ ̶̵̶G̶̵̶o̶̵̶l̶̵̶a̶̵̶n̶̵̶g̶̵̶ ̶̵̶c̶̵̶o̶̵̶m̶̵̶m̶̵̶u̶̵̶n̶̵̶i̶̵̶t̶̵̶y̶̵̶.̶̵̶
* I̶̵̶f̶̵̶ ̶̵̶y̶̵̶o̶̵̶u̶̵̶ ̶̵̶a̶̵̶r̶̵̶e̶̵̶ ̶̵̶s̶̵̶t̶̵̶a̶̵̶r̶̵̶t̶̵̶i̶̵̶n̶̵̶g̶̵̶ ̶̵̶a̶̵̶ ̶̵̶n̶̵̶e̶̵̶w̶̵̶ ̶̵̶G̶̵̶o̶̵̶l̶̵̶a̶̵̶n̶̵̶g̶̵̶ ̶̵̶p̶̵̶r̶̵̶o̶̵̶j̶̵̶e̶̵̶c̶̵̶t̶̵̶,̶̵̶ ̶̵̶d̶̵̶e̶̵̶p̶̵̶ ̶̵̶i̶̵̶s̶̵̶ ̶̵̶g̶̵̶o̶̵̶o̶̵̶d̶̵̶ ̶̵̶t̶̵̶o̶̵̶ ̶̵̶g̶̵̶o̶̵̶.̶̵̶
* I̶f̶ ̶y̶o̶u̶ ̶a̶r̶e̶ ̶u̶s̶i̶n̶g̶ ̶G̶l̶i̶d̶e̶ ̶i̶n̶ ̶a̶ ̶l̶e̶g̶a̶c̶y̶ ̶p̶r̶o̶j̶e̶c̶t̶.̶ ̶Y̶o̶u̶ ̶c̶o̶u̶l̶d̶ ̶c̶o̶n̶s̶i̶d̶e̶r̶ ̶m̶i̶g̶r̶a̶t̶i̶n̶g̶ ̶t̶o̶ ̶d̶e̶p̶ ̶b̶u̶t̶ ̶i̶ ̶t̶h̶i̶n̶k̶ ̶t̶h̶e̶r̶e̶ ̶i̶s̶ ̶n̶o̶ ̶h̶a̶r̶m̶ ̶t̶o̶ ̶k̶e̶e̶p̶ ̶u̶s̶i̶n̶g̶ ̶G̶l̶i̶d̶e̶ ̶f̶o̶r̶ ̶a̶ ̶w̶h̶i̶l̶e̶ ̶u̶n̶t̶i̶l̶ ̶d̶e̶p̶ ̶i̶s̶ ̶o̶f̶f̶i̶c̶i̶a̶l̶l̶y̶ ̶r̶e̶l̶e̶a̶s̶e̶d̶.̶
* I̶n̶ ̶a̶d̶d̶i̶t̶i̶o̶n̶,̶ ̶m̶i̶s̶s̶i̶n̶g̶ ̶p̶a̶c̶k̶a̶g̶e̶’̶s̶ ̶s̶u̶b̶m̶o̶d̶u̶l̶e̶ ̶m̶a̶y̶ ̶r̶e̶s̶u̶l̶t̶ ̶i̶n̶ ̶m̶a̶l̶f̶u̶n̶c̶t̶i̶o̶n̶ ̶o̶f̶ ̶y̶o̶u̶r̶ ̶c̶o̶d̶e̶.̶
* [**dep**](https://github.com/golang/dep) **is officially released.**
* [**dep**](https://github.com/golang/dep) **works well on pulling git submodule.**
* Use standard library wherever possible. (Suggested by [philoserf](https://www.freecodecamp.org/news/an-intro-to-dep-how-to-manage-your-golang-project-dependencies-7b07d84e7ba5/undefined))
* You can checkout this example on [gitlab.com](https://gitlab.com/ykyuen/dep-example).

— Originally posted on [Boatswain Blog](https://blog.boatswain.io/post/manage-go-dependencies-using-dep/).

