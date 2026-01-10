---
title: Check the temperature of your CPU using Python (and other cool tricks)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-03T17:12:17.000Z'
originalURL: https://freecodecamp.org/news/using-psutil-in-python-8623d9fac8dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gx9zzO6SmaEn8btnqGxhGw.png
tags:
- name: coding
  slug: coding
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ori Roza

  Python’s psutil module provides an interface with all the PC resources and processes.

  This module is very helpful whether we want to get some data on a specific resource
  or manage a resource according to its state.

  In this article, I will...'
---

By Ori Roza

Python’s [psutil module](https://psutil.readthedocs.io/en/latest/) provides an interface with all the PC resources and processes.

This module is very helpful whether we want to get some data on a specific resource or manage a resource according to its state.

In this article, I will show you the main features of this module and how to use them.

### **Getting PC resources information**

Let’s see how we can get some info about our PC’s current system state.

We can get some info about the CPU since boot time, including how many [system calls](https://www.geeksforgeeks.org/operating-system-introduction-system-call/) and [context switches](http://www.linfo.org/context_switch.html) it has made:

```
In [1]: psutil.cpu_stats()Out[1]: scpustats(ctx_switches=437905181,interrupts=2222556355L,soft_interrupts=0,syscalls=109468308)
```

We can get some info about the disk and the memory state:

```
In [1]: psutil.disk_usage("c:")Out[1]: sdiskusage(total=127950385152L,                   used=116934914048L,                   free=11015471104L,                   percent=91.4)
```

```
In [2]: psutil.virtual_memory()Out[2]: svmem(total=8488030208L,              available=3647520768L,              percent=57.0,              used=4840509440L,              free=3647520768L)
```

We can even get some physical information about how many seconds of battery life is left, or the current CPU temperature:

```
In [1]: psutil.sensors_battery()Out[1]: sbattery(percent=77, secsleft=18305, power_plugged=False)
```

```
In [2]: psutil.sensors_temperatures() # In CelsiusOut[2]: {'ACPI\\ThermalZone\\THM0_0':         [shwtemp(label='',          current=49.05000000000001,          high=127.05000000000001,          critical=127.05000000000001)]}
```

### **Getting Information about Processes**

One of the most powerful features this module provides us is the “Process” class. We can access each process’ resources and statistics and respond accordingly.

(There are processes that require some admin or system privileges, so after trying to access their instance it will fail with an “AccessDenied” error.)

Let’s check this feature out.

First, we create an instance by giving the wanted process ID:

```
In [1]: p = psutil.Process(9800)
```

Then, we can access all the information and statistics of the process:

```
In [1]: p.exe()Out[1]: 'C:\\Windows\\System32\\dllhost.exe'
```

```
In [2]: p.cpu_percent()Out[2]: 0.0
```

```
In [3]: p.cwd()Out[3]: 'C:\\WINDOWS\\system32'
```

Let’s create a function that links open connections ports to processes.

First, we need to iterate all the open connections. `ps.net_connections` is exactly what we need!

```
In [1]: ps.net_connections?Signature: ps.net_connections(kind='inet')Docstring:Return system-wide socket connections as a list of(fd, family, type, laddr, raddr, status, pid) namedtuples.In case of limited privileges 'fd' and 'pid' may be set to -1and None respectively.The *kind* parameter filters for connections that fit thefollowing criteria:
```

```
+------------+----------------------------------------------------+| Kind Value | Connections using                                  |+------------+----------------------------------------------------+| inet       | IPv4 and IPv6                                      || inet4      | IPv4                                               || inet6      | IPv6                                               || tcp        | TCP                                                || tcp4       | TCP over IPv4                                      || tcp6       | TCP over IPv6                                      || udp        | UDP                                                || udp4       | UDP over IPv4                                      || udp6       | UDP over IPv6                                      || unix       | UNIX socket (both UDP and TCP protocols)           || all        | the sum of all the possible families and protocols |+------------+----------------------------------------------------+
```

We can see that one of the attributes that net_connections returns is “pid”.

We can link this to a process name:

```
In [1]: def link_connection_to_process():    ...:     for connection in ps.net_connections():    ...:         try:    ...:             yield [ps.Process(pid=connection.pid).name(),    ...:                   connection]    ...:         except ps.AccessDenied:    ...:             continue # Keep going if we don't have access
```

We should remember that unless we’ve got some root privileges, we cannot access particular processes. Therefore we need to wrap it in a try-catch statement for handling an “AccessDenied” error.

Let’s check the output.

It will output a lot of data, so let’s print the first member:

```
In [1]: for proc_to_con in ps.net_connections():    ...:     print proc_to_con    ...:     raw_input("...")    ...:['ManagementServer.exe', sconn(fd=-1, family=2, type=1, laddr=addr(ip='127.0.0.1', port=5905), raddr=addr(ip='127.0.0.1', port=49728), status='ESTABLISHED', pid=5224)]...
```

As we can see, the first member is the process name and the second is the connection data: ip address, port, status and so on.

This function is very useful to explore which ports are used by each processes.

We’ve all gotten the error “This address is already in use” once, haven’t we?

### Conclusion

The psutil module is a great library for system management. It is useful for managing resources as a part of a code flow.

I hope this article taught you something new, and I am looking forward to your feedback. Please, do tell — was this useful for you?

