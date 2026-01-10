---
title: How to Simplify Python Library RPM Packaging with Mock and Podman
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2025-01-15T19:29:16.918Z'
originalURL: https://freecodecamp.org/news/simplify-python-library-rpm-packaging-with-mock-and-podman
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1736952806487/e25f259a-71e0-4998-ad29-b5da286e3fba.png
tags:
- name: Python 3
  slug: python3
- name: rpm
  slug: rpm
- name: mock
  slug: mock
- name: packaging
  slug: packaging
- name: Devops
  slug: devops
seo_title: null
seo_desc: 'Packaging libraries and applications written in Python comes with its challenges.
  And while virtual environments are great for controlling and standardizing installations,
  there are some scenarios where using them may not be the best.

  For example, sa...'
---

Packaging libraries and applications written in Python comes with its challenges. And [while virtual environments are great](https://docs.python.org/3/tutorial/venv.html) for controlling and standardizing installations, there are some scenarios where using them may not be the best.

For example, say you need to install a Python library system wide. You could try to create a virtual environment on a shared well-known directory, or you could modify the environment variable [PYTHONPATH](https://docs.python.org/3/using/cmdline.html) to change where to look for packages.

But it may be simpler with an package manager like [RedHat RPM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/packaging_and_distributing_software/introduction-to-rpm_packaging-and-distributing-software) or [Debian DPKG](https://www.dpkg.org/), which can also help you keep track of dependencies and can even check if a package’s contents are tampered with after the installation with a checksum.

Also, system administration tools written in Python often require that you use an interpreter with all the required libraries ready to go. For example, imagine a system Python with the popular [numpy](https://numpy.org/) module installed by default, and such package is used by the tool – just calling the import without initializing any virtual environments.

For the sake of argument, say you need to go the route of an RPM packaging. You’ll quickly realize that your RPM package has runtime dependencies (libraries than your Python library needs to run once installed) and build dependencies (libraries you need to build your library but that are not required to use the library).

In particular, *build dependencies will force you to install those on the machines where you are packaging your application*. For example, look at the “BuildRequires” tag from the poetry RPM spec from RedHat (showing a fragment here):

```plaintext
 This patch moves the vendored requires definition
# from vendors/pyproject.toml to pyproject.toml
# Intentionally contains the removed hunk to prevent patch aging
Patch1:         poetry-core-1.6.1-devendor.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
# for tests (only specified via poetry poetry.dev-dependencies with pre-commit etc.)
BuildRequires:  python3-build
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-tomli-w
BuildRequires:  python3-virtualenv
BuildRequires:  gcc 
BuildRequires:  git-core
%endif
```

To complicate things further, you may:

* Need to build your library for a totally different OS that you have installed (say you have Fedora 42 but need and RPM for Alma Linux 9.5)
    
* Need to install an RPM that comes from a dubious source, and you want to make sure it doesn’t break your system while the packaging process is running (see the RPM [scriptlets](https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/)).
    

### Prerequisites

In this tutorial, I’ll show you how you can handle those concerns using an Open Source tool called [Mock](https://github.com/rpm-software-management/mock). But first you will need the following to be able to follow this tutorial:

* A Linux distribution that uses RPM as packaging tool (RedHat Enterprise Edition, Fedora, Alma Linux, Rocky, and so on)
    
* Ability to install RPM packages on your build server (like [mock](https://fedoraproject.org/wiki/Using_Mock_to_test_package_builds), [rpmdevtools](https://fedoraproject.org/wiki/Rpmdevtools)) using tools like [DNF](https://rpm-software-management.github.io/) or YUM.
    
* Understanding of how RPM packaging works (if you are unfamiliar, the [Fedora RPM guide](https://fedoranews.org/alex/tutorial/rpm/) is a great starting point)
    
* You should understand what a [container](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction#h.j2uq93kgxe0e) is and how [PODMAN](https://docs.podman.io/en/latest/index.html) or [Docker](https://docker.com/) works.
    
* Understanding how a [Python virtual environment](https://docs.python.org/3/library/venv.html) works. We will not cover this here, but is useful to know that [this alternative exists and how it works](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments).
    

### Here’s what we’ll cover:

* [Why Mock](#heading-why-mock)?
    
* [Packaging scenarios with Mock and Podman](#heading-packaging-scenarios-with-mock-and-podman)
    
* [Conclusion](#heading-conclusion)
    

## Why Mock?

As we discussed above, we already have [Python virtual environments](https://docs.python.org/3/library/venv.html) – so why bother to have an RPM of the same library?

Well, if you want to ensure consistent deployment across different systems, RPM packaging can be beneficial. It allows for easier management and distribution of software, especially in environments where system-wide installations are preferred over virtual environments.

Mock can help us with that. From the Mock Git README:

> *A 'simple'* [*chroot*](https://en.wikipedia.org/wiki/Chroot) *build environment manager for building RPMs.*
> 
> *Mock is used by the Fedora Build system to populate a chroot environment, which is then used in building a source-RPM (SRPM). It can be used for long-term management of a chroot environment, but generally a chroot is populated (using* [*DNF*](https://rpm-software-management.github.io/)*), an SRPM is built in the chroot to generate binary RPMs, and the chroot is then discarded.*

**This is very important:** it means mock will install dependencies on a [chroot](https://en.wikipedia.org/wiki/Chroot) environment, separated from the regular system, which will be discarded once the packaging is done.

Mock by itself doesn’t provide perfect isolation but [when used with a container](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction#h.j2uq93kgxe0e) execution framework like [PODMAN](https://docs.podman.io/en/latest/index.html), it helps to protect the integrity of your system when packaging an unknown RPM:

> Mock needs to execute some tasks under root privileges, therefore malicious RPMs can put your system at risk. Mock is not safe for unknown RPMs

By running mock inside Podman, you get the best of both worlds, as Podman will run with limited privileges by itself. Also Podman, being a container, can remove itself after execution, which helps out with the cleanup.

Let’s see a few scenarios that demonstrate where you can use mock.

## Packaging Scenarios with Mock and Podman

### Packaging a newer version of the module on an older Linux distribution

In this case, say we want to re-use the existing [textual 0.6.2](https://textual.textualize.io/) package from Fedora 41 into Fedora 40. This is possible with mock, but to make it more secure we should run it inside a Podman container. This will give us more isolation from the real operating system.

During testing, I found than my home directory was tool small when running Podman. To fix this, I created a configuration override to point Podman root storage to a bigger partition on my machine (/mnt/data/podman/):

```shell
mkdir --parent ---verbose $HOME/.config/containers/
/bin/cat<<EOF>$HOME/.config/containers/storage.conf
[storage]
driver = "overlay"
runroot = "/mnt/data/podman/"
graphroot = "/mnt/data/podman/"
EOF
```

Then I realized something else: I needed to preserve the results of our artifact generation. When you run a container with the `—rm` (remove) flag, all its contents are destroyed. In our case, we want to preserve the generated RPM package files. So what we do is to mount an external directory inside the Podman container using the `—mount` option: (`--mount type=bind,src=$HOME/tmp,target=/mnt/result`).

So far so good, right? Not quite. I found out that a Python dependency for Textual was missing too. It’s called Rich, and it needed an RPM as well. Luckily you can “chain” a list of dependencies as Source RPMS (SRPM) when building your main package, so Mock can make them available to you when preparing the main package (we must pass `—localrepo` instead of `—resultdir` and we use the `--chain` flag).

Now we are ready to build the package and its dependencies. This requires the following:

1. Create a local directory where the RPMS will be created
    
2. Run Podman on interactive mode so we can execute commands inside it
    
3. Install mock inside Podman using dnf.
    
4. Create a special user called mockbuilder to run mock and become that user
    
5. Execute mock passing the chain
    

```shell
mkdir --parent --verbose $HOME/tmp
podman run --mount type=bind,src=$HOME/tmp,target=/mnt/result --rm --privileged --interactive --tty fedora:40 bash
dnf install -y mock
useradd mockbuilder
usermod -a -G mock mockbuilder
chown mockbuilder /mnt/result/
su - mockbuilder
mock --localrepo /mnt/result/ --chain https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm
```

For example, on my Raspberry PI 4 with Fedora 40, the final output looks like this:

```shell
...
INFO: Success building python-textual-0.62.0-2.fc41.src.rpm
INFO: Results out to: /mnt/result/results/default
INFO: Packages built: 2
INFO: Packages successfully built in this order:
INFO: /tmp/tmpc6651dxo/python-rich-13.7.1-5.fc41.src.rpm
INFO: /tmp/tmpc6651dxo/python-textual-0.62.0-2.fc41.src.rpm
```

Outside the container, we can test the installation by installing both Rich and Textual (you need root for this):

```shell
josevnz@raspberypi1:~$ sudo dnf install -y /home/josevnz/tmp/results/default/python-rich-13.7.1-5.fc41/python3-rich-13.7.1-5.fc40.noarch.rpm /home/josevnz/tmp/results/default/python-textual-0.62.0-2.fc41/python3-textual-doc-0.62.0-2.fc40.noarch.rpm /home/josevnz/tmp/results/default/python-textual-0.62.0-2.fc41/python3-textual-0.62.0-2.fc40.noarch.rpm
...
nstalled:
  python3-linkify-it-py-2.0.3-1.fc40.noarch            python3-markdown-it-py-3.0.0-4.fc40.noarch    python3-markdown-it-py+linkify-3.0.0-4.fc40.noarch  
  python3-markdown-it-py+plugins-3.0.0-4.fc40.noarch   python3-mdit-py-plugins-0.4.0-4.fc40.noarch   python3-mdurl-0.1.2-6.fc40.noarch                   
  python3-pygments-2.17.2-3.fc40.noarch                python3-rich-13.7.1-5.fc40.noarch             python3-textual-0.62.0-2.fc40.noarch                
  python3-textual-doc-0.62.0-2.fc40.noarch             python3-uc-micro-py-1.0.3-1.fc40.noarch      

Complete!
```

Note than the contents of the container were removed from the original window once you exit, except the mounted volume. This is great, as we don’t have to worry about uninstalling building packages ourselves.

*But is it perfect?*

*Can you use Mock to package newer code on much older distributions?*

Mock works really well as long your dependencies aren't too far away from the version you are running. For example, say you want to build the RPMS for Fedora 37 instead of Fedora 40:

```shell
sudo rm -rf $HOME/tmp/results/*
podman run --mount type=bind,src=$HOME/tmp,target=/mnt/result --rm --privileged --interactive --tty fedora:37 bash
dnf install -y mock
useradd mockbuilder && usermod -a -G mock mockbuilder && chown mockbuilder /mnt/result/ && su - mockbuilder
mock --nocheck --localrepo /mnt/result/ --chain https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm
...
Package python3-poetry-core-1.0.8-3.fc37.noarch is already installed.
Package python3-pytest-7.1.3-2.fc37.noarch is already installed.
Package python3-setuptools-62.6.0-3.fc37.noarch is already installed.
Error: 
 Problem: nothing provides requested (python3dist(pygments) < 3~~ with python3dist(pygments) >= 2.13)
```

Uh oh, Fedora 37 doesn’t provide some of the dependencies. Can we build them in chain? I tried to add the SRPM for [pygments](https://pygments.org/) (a generic syntax highlight library for Python), before building [rich](https://rich.readthedocs.io/en/stable/introduction.html), as it is a dependency for it. So the dependency chain grew a little bit more:

```shell
mock --nocheck --localrepo /mnt/result/ --chain https://download.fedoraproject.org/pub/fedora/linux/releases/39/Everything/source/tree/Packages/p/python-pygments-2.15.1-4.fc39.src.rpm https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm
```

And then I found that two more python dependencies were broken, this time for textual on Fedora 37:

```shell
...
no matching package to install: 'python3-syrupy'
No matching package to install: 'python3-time-machine'
Not all dependencies satisfied
```

Looks like a game of trial an error. *How bad it can be?*

Several tries later, I found that [Syrupy (pytest plugin)](https://github.com/syrupy-project/syrupy) added a dependency on [Poetry (packaging tool)](https://python-poetry.org/), which complicated things a little bit, as Fedora 37 expects an older version of Poetry (poetry-1.1.14-1.fc37).

What could you do next? Well, you could try to get a version of Syrupy that works with this older version of Poetry. But that could potentially introduce vulnerabilities on your system or force you to use a version of Syrupy that doesn't work at all with Textual because of API changes.

It’s easier to work your dependencies upwards rather than downwards. In this case, I decided to stop my experiment as I don’t really need an RPM for Fedora 37 myself.

### Building a newer non-packaged version of the software

Can mock help us with packaging an entirely new version of a package? Textual made huge improvements and added new features on the first official release 1.0.0. Let's see if we can take a few shortcuts to build an RPM that we can use with the system Python.

We will recycle the RPM Spec file from Textual we used before, but with a few modifications. First, let's prepare our sources again:

```shell
josevnz@raspberypi1:~$ podman run --mount type=bind,src=$HOME/tmp,target=/mnt/result --rm --privileged --interactive --tty fedora:40 bash
[root@ccae845daa84 /]# dnf install -y rpmdevtool
[root@ccae845daa84 /]# dnf install -y mock && useradd mockbuilder && usermod -a -G mock mockbuilder && chown mockbuilder /mnt/result/ && su - mockbuilder
[root@ccae845daa84 /]# for dep in https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm; do rpm -ihv $dep; done
```

Then we update the [RPM spec file](https://rpm-software-management.github.io/rpm/manual/spec.html) for Textual, which describes how the RPM is created, bumping the version from 0.62.0 to 1.0.0.

What I like to do is to create a new SRPM for Textual. For that I do the following (I’m still inside the Podman container – yes you can reuse it as long it keeps running):

1. Install rpmdevtool, mock, as it contains a few tools I need to setup the environment to build the SRPM
    
2. Install the original SRPM for 0.6.2. Installing doesn’t need root and creates a new SRPM I can use to bootstrap my new installation. Steps 1 and 2 just below (this is optional if you are re-using the container from the previous example):
    
    ```bash
    [root@ccae845daa84 /]# dnf install -y rpmdevtool
    [root@ccae845daa84 /]# dnf install -y mock && useradd mockbuilder && usermod -a -G mock mockbuilder && chown mockbuilder /mnt/result/ && su - mockbuilder
    [root@ccae845daa84 /]# for dep in https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm; do rpm -ihv $dep; done
    ```
    
3. I bumped the version of the package from 0.6.2 on the SPEC file that gets extracted inside ~/rpmbuild/SPECS/python-textual.spec
    
4. Tell spectool to retrieve the proper compressed source tar file so we can used to prepare a new SRPM
    
5. Recreate the SRPM so it can be used by Mock.
    
    Steps 3, 4, and 5 below:
    

```shell
[root@ccae845daa84 /]# sed -i 's#0.62.0#1.0.0#' ~/rpmbuild/SPECS/python-textual.spec
[root@ccae845daa84 /]# sed -i 's#%{url}/archive/v%{version}/textual-%{version}.tar.gz#%{url}/archive/refs/tags/v%{version}.tar.gz#' ~/rpmbuild/SPECS/python-textual.spec
[root@ccae845daa84 /]# spectool --get-files ~/rpmbuild/SPECS/python-textual.spec --sourcedir
Downloading: https://github.com/Textualize/textual/archive/refs/tags/v1.0.0.tar.gz
|  28.3 MiB Elapsed Time: 0:00:02                                                                                                                       
Downloaded: v1.0.0.tar.gz
[root@ccae845daa84 /]# rpmbuild -bs ~/rpmbuild/SPECS/python-textual.spec
setting SOURCE_DATE_EPOCH=1717891200
Wrote: /root/rpmbuild/SRPMS/python-textual-1.0.0-2.fc40.src.rpm
```

Now we can rebuild the SRPM and make make sure mock can find it when running from the exposed volume:

```shell
[root@ccae845daa84 /]# cp -pv /root/rpmbuild/SRPMS/python-textual-1.0.0-2.fc40.src.rpm /tmp/
'/root/rpmbuild/SRPMS/python-textual-1.0.0-2.fc40.src.rpm' -> '/tmp/python-textual-1.0.0-2.fc40.src.rpm'
[root@ccae845daa84 /]# su - mockbuilder
[mockbuilder@ccae845daa84 ~]$ ls -l /tmp/python-textual-1.0.0-2.fc40.src.rpm
-rw-r--r--. 1 root root 29612335 Jan 11 00:12 /tmp/python-textual-1.0.0-2.fc40.src.rpm
```

Moment of truth, let’s build it:

```shell
[mockbuilder@ccae845daa84 ~]$ mock --nocheck --localrepo /mnt/result/ --chain https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm /tmp/python-textual-1.0.0-2.fc40.src.rpm
Wrote: /builddir/build/SRPMS/python-textual-1.0.0-2.fc40.src.rpm
Wrote: /builddir/build/RPMS/python3-textual-1.0.0-2.fc40.noarch.rpm
Wrote: /builddir/build/RPMS/python3-textual-doc-1.0.0-2.fc40.noarch.rpm
INFO: Done(/tmp/python-textual-1.0.0-2.fc40.src.rpm) Config(default) 2 minutes 38 seconds
```

Finally, test the installation by installing the RPMS outside the container:

```shell
josevnz@raspberypi1:~$ sudo dnf install /home/josevnz/tmp/results/default/python-rich-13.7.1-5.fc41/python3-rich-13.7.1-5.fc40.noarch.rpm /home/josevnz/tmp/results/default/python-textual-1.0.0-2.fc40/python3-textual-doc-1.0.0-2.fc40.noarch.rpm /home/josevnz/tmp/results/default/python-textual-1.0.0-2.fc40/python3-textual-1.0.0-2.fc40.noarch.rpm
Last metadata expiration check: 3:42:37 ago on Fri 10 Jan 2025 03:50:49 PM EST.
Package python3-rich-13.7.1-5.fc40.noarch is already installed.
Dependencies resolved.
=========================================================================================================================================================
 Package                                    Architecture                 Version                                Repository                          Size
=========================================================================================================================================================
Upgrading:
 python3-textual                            noarch                       1.0.0-2.fc40                           @commandline                       1.3 M
 python3-textual-doc                        noarch                       1.0.0-2.fc40                           @commandline                        24 M
Installing dependencies:
 python3-platformdirs                       noarch                       3.11.0-3.fc40                          fedora                              46 k

Transaction Summary
=========================================================================================================================================================
Install  1 Package
Upgrade  2 Packages

Total size: 25 M
Total download size: 46 k
Is this ok [y/N]: y
Downloading Packages:
python3-platformdirs-3.11.0-3.fc40.noarch.rpm                                                                             53 kB/s |  46 kB     00:00    
---------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                     41 kB/s |  46 kB     00:01     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                 1/1 
  Installing       : python3-platformdirs-3.11.0-3.fc40.noarch                                                                                       1/5 
  Upgrading        : python3-textual-1.0.0-2.fc40.noarch                                                                                             2/5 
  Upgrading        : python3-textual-doc-1.0.0-2.fc40.noarch                                                                                         3/5 
  Cleanup          : python3-textual-0.62.0-2.fc40.noarch                                                                                            4/5 
  Cleanup          : python3-textual-doc-0.62.0-2.fc40.noarch                                                                                        5/5 
  Running scriptlet: python3-textual-doc-0.62.0-2.fc40.noarch                                                                                        5/5 

Upgraded:
  python3-textual-1.0.0-2.fc40.noarch                                       python3-textual-doc-1.0.0-2.fc40.noarch                                      
Installed:
  python3-platformdirs-3.11.0-3.fc40.noarch                                                                                                              

Complete!
```

*Not bad*, we can now build sophisticated [TUIs](https://en.wikipedia.org/wiki/Text-based_user_interface) using Textual and the system Python, without the need to create a virtual environment nor force the installation of unwanted packages in our build server.

## Conclusion

As you can see, mock is a very valuable tool that can help you automate packaging Python libraries that are not yet available in your platform. It allows you to automate getting dependencies for the RPM and alerts you when some are missing in your platform.

As an added bonus, the fact than you can run it inside Podman gives you even more isolation from RPMs that could be dangerous when executed as root.

### Extra documentation (RTFM, Read The Fine Manual)

* [RPM-Macros](https://gitlab.com/redhat/centos-stream/rpms/pyproject-rpm-macros/)
    
* [Mock](https://rpm-software-management.github.io/mock/)
    
* [RPM dev tools](https://fedoraproject.org/wiki/Rpmdevtools)
    
* [RPM macro documentation](https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_201x/#_macros)
    
* [Packaging Python3 RPMS](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10-beta/html/packaging_and_distributing_software/packaging-python-3-rpms)
    
* [PyPA specifications](https://packaging.python.org/en/latest/specifications/)
    
* [Fedora Textual RPM](https://koji.fedoraproject.org/koji/buildinfo?buildID=2466451)
