---
title: Linux Boot Process – What Happens when Booting RHEL
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-02-02T17:49:18.000Z'
originalURL: https://freecodecamp.org/news/linux-boot-process-in-rhel
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Frame-1000004568.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'The boot process is made up of a series of necessary actions that a computer
  goes through upon startup. These range from powering on to the complete loading
  of the operating system (OS) for optimal functionality.

  It is vital to familiarize yourself w...'
---

The boot process is made up of a series of necessary actions that a computer goes through upon startup. These range from powering on to the complete loading of the operating system (OS) for optimal functionality.

It is vital to familiarize yourself with the boot process for various reasons. First of all, having a solid understanding of booting process is crucial for effectively addressing boot issues, enhancing system performance, and efficiently controlling various components of system startup.

For example, it'll help you identify and resolve problems that may arise during the boot process, such as hardware malfunctions or incorrect configurations.

Also, gaining a thorough understanding of the boot process can help you personalize your startup configurations. This includes the ability to select the specific programs or services that are launched upon startup, ultimately affecting both the overall system performance and user satisfaction.

## **Table Of Contents**

Here's what we'll cover in this comprehensive guide:

* [High level overview of the booting process](#heading-high-level-overview-of-the-booting-process)
    
* [Understanding the boot process in depth](#heading-understanding-the-boot-process-in-depth)
    
* [POST (Power-On Self-Test)](#heading-post-power-on-self-test)
    
* [Understanding BIOS/UEFI](#heading-understanding-biosuefi)
    
* [MBR (Master Boot Record)](#heading-mbr-master-boot-record)
    
* [GPT (GUID Partition Table)](#heading-gpt-guid-partition-table)
    
* [GRUB (Grand Unified Boot Loader)](#heading-grub-grand-unified-boot-loader)
    
* [Initrd (Initial RAM Disk) Image](#heading-initrd-initial-ram-disk-image)
    
* [Kernel](#heading-kernel)
    
* [RootFS](#heading-rootfs)
    
* [Init Process](#heading-init-process)
    
* [System Daemons](#heading-system-daemons)
    
* [Wrapping Up](#heading-wrapping-up)
    

## High Level Overview of the Booting Process

### Initializing Hardware

During the boot process, the computer's firmware (such as BIOS or UEFI) takes charge and sets up all the necessary hardware components, including the processor, memory, storage devices, and peripherals. This crucial initialization stage guarantees that these components are fully prepared for the operating system's use.

### Loading the Operating System

Once the hardware has been initialized, the boot process commences with loading the operating system. This step usually consists of loading the kernel and initializing crucial OS services into memory.

### Launching System Services

As the operating system starts up, it activates a range of system services and drivers. These essential components ensure the smooth operation of the computer, enabling tasks such as managing network connections, processing input/output operations, and maintaining security measures.

### User Interaction

At long last, the boot process reaches its peak by greeting you (the user) with a login screen or desktop environment, granting full access to the computer and its various applications.

## Understanding the Boot Process in Depth

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-150.png align="left")

*Booting Process*

## POST (Power-On Self-Test)

When a computer is first turned on, there is a vital process that takes place known as the Power-On Self-Test, or POST for short. This diagnostic testing sequence is conducted by the system's firmware, whether it be BIOS or UEFI, as a crucial step in the booting sequence.

Its main purpose is to verify that all essential hardware components are functioning properly before handing control over to the operating system. In short, POST is a crucial step in ensuring that a computer is ready to operate at its full potential upon startup.

### Stages and Functions of POST

#### Initialization

When the computer is turned on, the system's firmware (BIOS or UEFI) takes control.

The firmware begins by initializing critical hardware components like the CPU, RAM, chipset, and other essential devices.

#### Power-On Self-Test (POST)

The POST sequence begins immediately after initialization. It checks various hardware components by sending test signals and commands to them.

It checks the CPU, RAM (memory), storage devices (hard drives, SSDs), graphics cards, peripherals (keyboard, mouse), and other connected hardware.

Each component is tested to ensure it responds correctly and operates within acceptable parameters.

1. The CPU is checked by verifying its operating frequency and executing a simple test.
    
2. The RAM is tested by writing and reading data to verify its integrity.
    
3. Storage devices are checked for presence and basic functionality.
    
4. Peripherals might be tested by checking if they respond to commands.
    

Any failure during the POST process results in error messages or audible beeps that indicate which component failed the test.

#### Error Handling

If an error is detected during POST, the system typically halts and displays an error message, or it might emit a series of audible beeps (known as beep codes) indicating the nature of the issue.

Error codes or messages generated during POST are crucial for diagnosing hardware problems. They help in identifying the failing component or area causing the issue.

#### Completion and Handover

Once the POST sequence completes without detecting any critical errors, the firmware determines that the hardware is functioning correctly.

The firmware proceeds to initialize other system components and search for a boot device to load the operating system.

## Understanding BIOS/UEFI

BIOS and UEFI are two essential firmware interfaces responsible for initializing hardware components, running system diagnostics, and supporting the startup of the operating system on a computer. These interfaces are vital players in the boot process of a system.

### BIOS

For decades, BIOS has been a dominant firmware interface, stored on the motherboard's chip. Its crucial role is to activate and oversee hardware during the boot-up phase.

As soon as the computer is switched on, the BIOS assumes command and executes the Power-On Self-Test (POST) to ensure the essential hardware components – including the RAM, CPU, and storage devices – are all functioning properly.

After the POST is successfully completed, the BIOS will then proceed to search for the boot device, using a predetermined boot order that was previously set in the BIOS settings. This boot order typically includes popular devices such as hard drives, solid-state drives, optical drives (CD/DVD), USB drives, and network interfaces.

Once the boot device has been identified, the BIOS proceeds to search for either the Master Boot Record (MBR) or the GUID Partition Table (GPT) on the storage device. These contain the crucial initial boot loader code. The BIOS then dutifully passes the reins to the designated boot loader, such as GRUB for Linux operating systems.

### UEFI (Unified Extensible Firmware Interface)

UEFI is a more modern and versatile replacement for BIOS. It provides more advanced features and capabilities than BIOS.

UEFI is firmware that resides on the motherboard and is responsible for initializing hardware and booting the operating system.

Similar to BIOS, UEFI starts with the hardware initialization and system checks. But UEFI supports more modern hardware standards and allows for faster boot times compared to traditional BIOS.

UEFI includes a boot manager, which is more sophisticated than the boot loaders used in BIOS systems. It understands different file systems, allowing the system to boot from drives formatted with newer file systems like GPT. It uses EFI boot partitions to store bootloaders and related information.

UEFI introduced Secure Boot, a security feature that verifies the digital signatures of boot loaders and operating system kernels during the boot process. This helps prevent the loading of unauthorized or malicious code during boot time.

### Differences between BIOS and UEFI

* BIOS uses the Master Boot Record (MBR) method, while UEFI uses the GUID Partition Table (GPT) method.
    
* UEFI is more flexible and supports larger storage capacities, modern hardware, and faster boot times compared to BIOS.
    
* UEFI introduces Secure Boot, enhancing system security by verifying the authenticity of bootloader and OS components.
    

## MBR (Master Boot Record)

The Master Boot Record (MBR) plays a vital role in the storage structure of a disk. It is closely linked to BIOS-based systems and serves as the catalyst for the initial booting process.

### Structure of MBR

The MBR is located in the first sector of a storage device (usually the first 512 bytes of a hard drive or SSD). It's in a fixed location, the LBA (Logical Block Address) 0.

The Master Boot Record (MBR) if of 512 bytes in size. It consists of three components:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image--1--1.png align="left")

*MBR Structure: Boot signature, partitions, and bootstrap code*

1. The primary boot loader information occupies the initial 446 bytes.
    
2. Following that, the partition table information fills the subsequent 64 bytes.
    
3. Lastly, the MBR validation check, also known as the magic number, resides in the final 2 bytes.
    

A partition table is a small database that holds information about the disk's partitions. This table can store information for up to four primary partitions or three primary partitions and one extended partition.

Each entry in the partition table consists of

1. Starting and ending addresses of each partition.
    
2. Partition type (such as FAT, NTFS, Linux filesystem, and so on).
    
3. Bootable flag indicating which partition is the active/bootable partition.
    

### Function of MBR

The MBR boot code's primary function is to locate and load the active/bootable partition's boot loader. It reads the partition table to identify which partition holds the bootable flag and executes the boot loader code from that partition.

The boot loader (for example, GRUB) subsequently takes over and presents a boot menu if configured, allowing the user to choose an operating system to load. It then loads the selected OS's kernel and initiates its booting process.

### Limitations of MBR

MBR has limitations in supporting only four primary partitions or three primary partitions and one extended partition, which can further contain multiple logical partitions. This restricts the number of partitions usable on a disk.

MBR uses 32-bit addressing, limiting disk sizes to 2 terabytes (TB). Larger disks cannot be fully utilized under MBR due to this limitation.

It also lacks built-in security features, making it susceptible to boot sector viruses or malicious code overwriting the boot loader.

## GPT (GUID Partition Table)

The GUID Partition Table (GPT) is a partitioning scheme used on modern storage devices and is closely associated with UEFI-based systems. It replaced the older Master Boot Record (MBR) partitioning scheme due to its numerous advantages and capabilities, especially in conjunction with UEFI firmware.

### Structure of GPT

GPT is a partitioning scheme that defines the layout of partitions on a storage device. Unlike MBR, which has limitations regarding disk size and partition count, GPT offers more flexibility and scalability.

Each partition in a GPT disk is identified by a unique GUID (Globally Unique Identifier). This allows for up to 128 partitions per disk (though practical limitations might apply based on the operating system and system firmware).

GPT disks contain a Protective MBR to maintain compatibility with legacy systems that may not recognize GPT partitions. This Protective MBR tells older systems that the disk is in use and prevents them from overwriting or modifying the GPT partitions.

GPT stores partition entries in a table located at the beginning and end of the disk. This redundancy enhances data integrity and provides backup information about the partition layout.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-33.png align="left")

*GUID partition table scheme diagram*

### Function of GPT

UEFI requires a specific partition known as the UEFI System Partition (ESP), which is a primary component of the GPT scheme. The ESP contains bootloaders, firmware executables, and other necessary files for the boot process.

UEFI firmware uses information stored in the GPT to locate the UEFI boot loader. The boot loader is stored in the ESP and is specified in the firmware's boot configuration data.

UEFI firmware understands GPT and can read the partition information directly from the GPT header. It uses this information to identify the bootable partition and load the UEFI boot loader from the ESP.

GPT and UEFI work together to support Secure Boot functionality. Secure Boot uses information from GPT to verify the digital signatures of bootloaders and OS components, ensuring a secure boot process.

GPT supports disk sizes larger than 2TB, addressing the limitations of the MBR partitioning scheme. It efficiently manages partitions on larger disks and provides scalability for future storage needs.

## GRUB (Grand Unified Boot Loader)

GRUB stands for Grand Unified Boot Loader. It's a widely used boot loader in the Linux world, responsible for managing the boot process of a computer.

A boot loader is a program that loads the operating system into the computer's memory during the startup process. GRUB is specifically designed for Unix-like operating systems, especially Linux.

GRUB's primary function includes locating the kernel of the chosen operating system and loading it into memory. It also manages the initial RAM disk (initrd/initramfs) that assists the kernel during the boot process.

GRUB uses a configuration file (`grub.cfg` or `menu.lst`) where users can define boot options, specify kernel parameters, and customize the appearance of the boot menu. This allows users to modify boot settings or add specific parameters for the operating system to use during startup.

During the installation of Linux distributions, GRUB is usually installed in the Master Boot Record (MBR) of the hard drive or the EFI system partition (for systems using UEFI). This allows GRUB to take control during boot-up and present its menu interface.

## Initrd (Initial RAM Disk) Image

An Initial RAM Disk (initrd), also known as an Initial RAM filesystem (initramfs), is a temporary file system loaded into memory during the boot process of a computer before the main operating system takes over. It's an essential component in modern Linux booting.

The primary purpose of the initrd is to provide a minimal set of tools, drivers, and utilities necessary to mount the root file system. It contains essential drivers for storage controllers, file systems, and other hardware components that the kernel might need to access the actual root file system.

During boot-up, the boot loader (such as GRUB) loads the Linux kernel into memory. The kernel then decompresses itself and, if configured to use an initrd, loads the initrd image as a temporary root file system into a predetermined memory location.

Once the initrd is in place, the kernel executes the code within the initrd. This code performs various tasks like loading essential drivers (for example, for disk controllers, file systems, and so on), initializing hardware, and performing necessary checks to prepare the system to transition to the actual root file system.

After the kernel initializes and detects hardware, the initrd's job is largely complete. It hands control over to the main kernel, which then unmounts the initrd and mounts the actual root file system (specified by the bootloader or kernel parameters).

Traditionally, initrd was used, but modern systems often use initramfs (a more flexible successor). Initramfs is a cpio archive that is uncompressed into a RAM disk at boot time. It's more versatile, allowing for a more modular approach to including essential files and drivers.

## Kernel

The kernel is the core of the operating system, managing hardware resources, providing abstractions, and controlling interactions between hardware and software.

After the initrd image completes its tasks, the kernel takes control. It initializes the system hardware, mounts the root file system, and begins the user-space initialization process.

The kernel uses information provided by the initrd to mount the actual root file system (for example, ext4, XFS) specified in the boot parameters.

## RootFS

The Root File System (rootfs) is a critical component in the booting process of an operating system. It is the top-level directory hierarchy of the file system and contains essential system files and directories.

In the context of the booting process, the root file system is the initial file system that the operating system kernel mounts during the boot sequence.

The root file system is the starting point for the entire file system hierarchy. It is mounted by the kernel during the boot process, and all other file systems are mounted as subdirectories of the root file system.

The bootloader, such as GRUB in many Linux systems, is configured to specify the location of the root file system. This information is crucial for the kernel to know where to find the core files and directories needed to start the operating system.

The root file system can be of different types, such as ext4, XFS, or other supported file systems. The choice of the file system type depends on the system administrator's preferences and requirements.

In some cases, especially in complex storage scenarios (for example, RAID or LVM configurations), an initial RAM disk (initramfs) is used. The initramfs provides necessary modules and tools for the kernel to initialize and mount the root file system. Afterward, the kernel switches to the actual root file system.

The root file system contains critical directories such as `/bin`, `/etc`, `/sbin`, and `/lib`. These directories house essential binaries, configuration files, system libraries, and scripts required for system operation.

The root file system is typically a persistent file system stored on a storage device like a hard drive or an SSD. It retains data and configurations across reboots, ensuring a consistent environment for the operating system.

The stability and functionality of the operating system depend on the successful initialization and mounting of the root file system. It provides the foundation for the entire operating system environment.

## Init Process

The init process, short for initialization, is a fundamental part of the booting process in Unix-like operating systems, including many Linux distributions. Its primary responsibility is to initialize the system and bring it to a functional state by starting various system services and user-space processes.

After the kernel has loaded and initialized, it hands over control to the init process. The kernel command-line parameters or configuration files specify the process to which control should be transferred.

Traditional Unix systems used the init process with different runlevels, where each runlevel represented a different system state. But modern Linux systems, including those based on Red Hat Enterprise Linux (RHEL), have transitioned to using systemd, which serves as a replacement for init and introduces a more flexible and efficient approach to managing system initialization.

On modern Linux systems like RHEL, systemd has become the default init system. It initializes the system in parallel, improving boot times and system responsiveness. systemd reads its configuration from unit files located in directories such as `/etc/systemd/system` and `/usr/lib/systemd/system`.

The init process, whether traditional init or systemd, is responsible for starting system services and daemons. These services provide essential functionality to the operating system, such as networking, logging, and hardware-related services.

## System Daemons

System daemons, also known as background processes or services, play a vital role in the booting process and ongoing operation of Unix-like operating systems, including those based on Red Hat Enterprise Linux (RHEL). These daemons are specialized programs that run in the background, providing essential services to the system and users.

A daemon is a background process that runs independently of user interaction. Daemons perform specific tasks, such as managing hardware, handling system events, or providing network services.

During the boot process, the init or systemd process is responsible for starting system daemons. These daemons are configured to launch automatically at specific runlevels (in the case of traditional init) or as defined in systemd unit files.

Daemons are typically initialized by the init or systemd process as part of the system startup. The initialization process may involve reading configuration files, setting up communication channels, and allocating resources.

Examples of system daemons include:

* **Network services:** Daemons like `sshd` for secure shell access, `httpd` for web services, and `dhcpd` for dynamic host configuration protocol.
    
* **Logging services:** `rsyslogd` or `syslog-ng` for handling system logs.
    
* **Time synchronization:** `ntpd` for Network Time Protocol (NTP) synchronization.
    
* **Printing services:** `cupsd` for Common Unix Printing System.
    
* **Hardware management:** `udev` for device management and `acpid` for Advanced Configuration and Power Interface events.
    

The init or systemd process manages dependencies between daemons. It ensures that daemons relying on specific resources or services are started in the correct order to satisfy these dependencies.

systemd, in particular, introduces parallel initialization, meaning that multiple daemons and services can be started simultaneously, improving boot times by taking advantage of modern multi-core systems.

Once system daemons are initialized, the system is ready to handle user interactions. For example, network services are available, and users can log in or access various system resources.

## **Wrapping Up**

Thank you for exploring booting process in RHEL with me today. You can dive deeper into the realm of Linux expertise and stay tuned for more insightful content in my future tutorials.

You can follow me on:

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
