---
title: How Do Open Source Licenses Work? Permissive and Protective Software Licenses
  Explained
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2024-02-28T17:07:49.000Z'
originalURL: https://freecodecamp.org/news/permissive-and-protective-software-licenses
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/katerina-pavlyuchkova-FQYCJSqER_0-unsplash.jpg
tags:
- name: open source
  slug: open-source
seo_title: null
seo_desc: "If you're going to use or work with open source resources, you'll need\
  \ to understand the fine print on various classes of an open source license. Otherwise,\
  \ how can you be sure you're not infringing on someone else's rights? \nThis article\
  \ will introd..."
---

If you're going to use or work with open source resources, you'll need to understand the fine print on various classes of an open source license. Otherwise, how can you be sure you're not infringing on someone else's rights? 

This article will introduce you to the big players and concepts in the open source license universe.

This article comes from my Complete LPI Open Source Essentials Exam Study Guide [Udemy course](https://www.udemy.com/course/complete-lpi-open-source-essentials-exam-study-guide/?referralCode=05B999CE18EF4D6E243C) and [book](https://www.amazon.com/dp/B0CK3Q8DCF). You can also view the video version here:

%[https://www.youtube.com/watch?v=G7S5wY0PKkw]

In broad terms, we'll divide those classes into two categories. We'll discuss both permissive and restrictive licenses here.

## Working with Permissive Software Licenses

Permissive open source software licenses are a type of software license that allows for a wide range of uses of the licensed software. Some examples of permissive open source software licenses — that we'll explore in greater depth a bit later — include Apache, BSD, and MIT.

In general, permissive open source software licenses give you the right to use the software for any purpose – including commercial purposes – and the right to modify the software to suit your needs. 

You'll get the right to distribute the software to others, either in its original form or as a modified version and the right to sublicense the software to others, allowing them to exercise the same rights as the original licensee. You'll also have the right to use any patents or trademarks associated with the software, as long as they comply with any applicable laws.

At the same time, permissive open source software licenses also impose certain obligations on users. You might be required to include a copyright notice when making further copies or distributions of the software. 

You could also need to include a copy of the license in subsequent distributions. You might need to disclaim any warranties or liability for damages that may arise from the use of the software. And you'll often have to give attribution to the original software authors or contributors. Although there might also be times when using the names of those authors without explicit permission is _forbidden_.

The bottom line: make sure you read the fine print.

Now let's take a more detailed look at some actual permissive licenses.

### The 2-Clause BSD License

The 2-Clause BSD License, also known as the Simplified BSD License, is a permissive open source software license that allows for a wide range of uses of the licensed software. 

The license permits users to use, copy, modify, and distribute the software, as long as they include a copyright notice and disclaimer of any warranties or liability. The 2-Clause BSD License is commonly used for software that is released as open source but also used in proprietary software products.

### The 3-Clause BSD License

The 3-Clause BSD License, also known as the New BSD License, is similar to the 2-Clause BSD License but includes an additional clause that requires users to include a copy of the license and copyright notice in any distributions of the software. This license is commonly used for open source software projects that want to ensure proper attribution and give credit to the original authors or contributors.

"BSD", by the way, stands for "Berkeley Software Distribution". The license is associated with the version of the Unix operating system that was developed at the University of California, Berkeley in the late 1970s and early 1980s.

### The MIT License

The MIT License is a permissive open source software license that allows users to use, copy, modify, and distribute the software, as long as they include a copyright notice and disclaimer of any warranties or liability. 

The license is similar to the 2-Clause BSD License but is often preferred for its brevity and simplicity. The MIT License is commonly used for open source software projects, especially those related to web development and programming languages.

"MIT", of course, stands for Massachusetts Institute of Technology, a private research university located in Cambridge, Massachusetts, USA. The MIT License is named after the university because it was developed by the university's computer science department and used for its open source software releases.

### The Apache License

The Apache License version 2.0 is widely used for open source software projects, especially those related to web and server software. The license permits users to use, copy, modify, and distribute the software, as long as they include a copyright notice, disclaimer of any warranties or liability, and a notice of any changes made to the original software. 

The license also includes patent grant provisions that protect users against patent infringement lawsuits. The Apache License version 2.0 is often considered to be one of the most permissive open source software licenses available.

### The Eclipse Public License (EPL)

The EPL is a permissive open source software license that was developed by the Eclipse Foundation for use with the Eclipse software development environment. On the other hand, EPL is _not_ a permissive open source software license. In fact, EPL kind of straddles the border between permissive and restrictive. I'll describe it here, but bear in mind that it actually shares some features with the restrictive copyleft licenses we'll talk about later.

At any rate, the license is designed to be compatible with other open source software licenses and allows for the creation of derivative works.

The EPL version 1.0 is a copyleft license that requires any modifications or derivative works to be released under the same license. The license also includes a patent license grant that allows users to use any patents associated with the software, as long as they comply with the terms of the license.

The EPL version 2.0, released in 2017, is also a copyleft license but includes several updates and improvements over the previous version. The license has been updated to address some of the legal issues that arose with the previous version and to make it more compatible with other open source software licenses. One notable change in version 2.0 is the addition of a patent non-assertion covenant, which assures users that the software's licensors will not assert their patents against the user for using or distributing the licensed software.

## Working with Protective Software Licenses

Copyleft software licenses aim to ensure that the licensed software remains free and open for future users and developers. These licenses use copyright law to achieve this goal by requiring any derivative works of the software to be licensed under the same license terms.

This means that anyone who modifies or distributes the software must also make their changes and additions available to others under the same license.

The most well-known copyleft software license is the GNU General Public License (GPL), but there are many other copyleft licenses such as the Lesser General Public License (LGPL), the Mozilla Public License (MPL), and the Affero General Public License (AGPL).

The rights and obligations defined by copyleft software licenses can vary depending on the specific license, but some common aspects include rights, typically granting users the right to use, modify, and distribute the software. The licenses often require that any derivative works be licensed under the same terms, which ensures that the software remains free and open for future use and development.

Copyleft software licenses also impose certain obligations on users and developers of the software. These obligations can include requirements to include a copy of the license with any distributions of the software, to make the source code available, and to maintain copyright notices and attribution to the original authors.

Copyleft licenses can have implications for compatibility with other licenses. For example, using individual software components licensed as copyleft as _part_ of a larger project may require the entire project to be released under a copyleft license. This is because the copyleft license requires any derivative works to be licensed under the same terms.

Let's work through some of the more popular copyleft templates, one at a time.

### The GNU General Public License

The GPL is developed by the Free Software Foundation (FSF). It requires any derivative works of the licensed software to be licensed under the same terms. 

The GPL has several versions, including version 2.0 (GPLv2) and version 3.0 (GPLv3). The GPL is widely used for software development projects and is often seen as a key component of the free software movement. 

GPLv2 (that is, "version 2") of the GPL includes provisions for distributing the source code and making modifications to the software. GPLv3 added provisions for preventing "tivoization" (meaning, the practice of using digital restrictions to prevent users from modifying the software) and for addressing patent issues.

### The GNU Lesser General Public License

The LGPL is another license developed by the FSF that allows for more flexibility in the use of the licensed software. The LGPL has two versions, version 2 (LGPLv2) and version 3 (LGPLv3). 

The LGPL is commonly used for software libraries and other software components that are designed to be linked with other software. LGPLv2 and LGPLv3 added more flexibility in the use of the licensed software, particularly for software libraries. Later versions also worked to add greater compatibility with the GPLv3.

### The GNU Affero General Public License

The AGPL also comes from the FSF. It's similar to the GPL but includes additional requirements for software that is distributed over a network. 

The AGPL is often used for software that's designed to be run on servers and accessed over a network, such as web applications. 

Version 3 (AGPLv3) includes additional requirements for software that is distributed over a network. It requires anyone who uses the software over a network to make the source code available and to provide a copy of the license to users.

### The Mozilla Public License

The MPL was developed by the Mozilla Foundation – the people behind the Firefox browser. It is a copyleft license that allows for the distribution of the licensed software under both proprietary and open source terms. The MPL is compatible with the GNU General Public License (GPL), allowing code to be shared between MPL-licensed software and GPL-licensed software. The MPL is also compatible with other open source licenses such as Apache and MIT.

The MPL requires that the source code for any modified versions of the licensed software be made available. This allows others to see and modify the code, promoting the growth and development of the software. The MPL also requires that any distribution of the licensed software, whether in its original or modified form, be made under the MPL. 

This means that anyone who distributes the software must provide a copy of the license with the software and make the source code available. The MPL includes provisions to protect users from patent claims related to the licensed software. These provisions ensure that users of the software are able to use and distribute the software without fear of legal action.

## Wrapping Up

With this information you're now ready to carefully evaluate the benefits and limitations of each specific collection of open source code you might use. And you can similarly understand how you might want to license your own code when it's ready to be shared with the world.

_This article comes from my_ [_Complete LPI_](https://www.udemy.com/course/complete-lpi-open-source-essentials-exam-study-guide/?referralCode=05B999CE18EF4D6E243C) Open Source _Essentials Study Guide course__._ _And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/)_

