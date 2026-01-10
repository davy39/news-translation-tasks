---
title: How to Turn Ubuntu 24.04 into a KVM Hypervisor – Quick Setup with Web Management
subtitle: ''
author: Shamsuddoha Ranju
co_authors: []
series: null
date: '2025-04-28T15:45:09.631Z'
originalURL: https://freecodecamp.org/news/turn-ubuntu-2404-into-a-kvm-hypervisor
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745591647377/613d9a44-cc2b-45b7-b1d1-5fc3154b9623.png
tags:
- name: KVM
  slug: kvm
- name: hypervisor
  slug: hypervisor
- name: virtualization
  slug: virtualization
- name: virtual machine
  slug: virtual-machine
- name: vm
  slug: vm
seo_title: null
seo_desc: 'Virtualization lets you run multiple operating systems on one machine.
  It’s perfect for testing apps, hosting servers, or learning DevOps.

  A hypervisor is the software that lets you run multiple virtual machines on a single
  physical machine, and the ...'
---

Virtualization lets you run multiple operating systems on one machine. It’s perfect for testing apps, hosting servers, or learning DevOps.

A hypervisor is the software that lets you run multiple virtual machines on a single physical machine, and the Kernel-based Virtual Machine (KVM) is one of the best. Built into Linux, KVM is fast (near-native performance), open-source (free!), and flexible (supports Windows, Linux, and more). It’s trusted by both cloud providers and homelabbers for its stability and low overhead.

If you want to turn your Ubuntu 24.04 or Kubuntu 24.04 (Kubuntu is a Ubuntu variant with KDE Plasma desktop) system into a powerful hypervisor without **Proxmox**’s complexity, this guide is for you. With KVM, you’ll spin up virtual machines (VMs) in minutes, and with Cockpit’s web-based manager, you’ll control them from your browser.

In this tutorial, you’ll transform an Ubuntu 24.04 or Kubuntu 24.04 Desktop or Server – fresh or existing – into a KVM hypervisor. You’ll set up the backend (KVM, QEMU, libvirt), add Cockpit for web-based VM management, and create a guest VM to test it all. Whether you’re a coder, homelabber, or IT enthusiast, this guide is beginner-friendly.

## Table of Contents

* [Before You Start: What You Should Know](#heading-before-you-start-what-you-should-know)
    
* [What You’ll Need](#heading-what-youll-need)
    
* [Why KVM on Ubuntu/Kubuntu 24.04?](#heading-why-kvm-on-ubuntukubuntu-2404)
    
* [Step 1: Check Virtualization Support](#heading-step-1-check-virtualization-support)
    
* [Step 2: Install KVM and Backend Tools](#heading-step-2-install-kvm-and-backend-tools)
    
* [Step 3: Set Up a Network Bridge](#heading-step-3-set-up-a-network-bridge)
    
* [Step 4: Install Cockpit for Web Management](#heading-step-4-install-cockpit-for-web-management)
    
* [Step 5: Create a Guest VM](#heading-step-5-create-a-guest-vm)
    
* [Step 6: Run and Test Your Guest VM](#heading-step-6-run-and-test-your-guest-vm)
    
* [Keep Exploring Your Hypervisor](#heading-keep-exploring-your-hypervisor)
    
* [Wrapping Up](#heading-wrapping-up)
    

## Before You Start: What You Should Know

This guide is designed for virtualization newcomers, but you’ll need a few basic skills:

* Running terminal commands like `sudo apt install` or `nano` and so on.
    
* Basic Linux navigation (for example, editing files in `/etc`).
    
* Basic networking knowledge, such as understanding network interfaces (for example, `enp4s0` or `wlp3s0`), IP addresses, and concepts like bridging or NAT. You’ll use tools like `ip link` or `nmcli` to set up a network bridge in Step 3.
    
* Optional: Experience with VMs helps but isn’t required – I’ll explain everything.
    

No worries if terms like “libvirt” sound new. I’ll break them down as we go.

## What You’ll Need

* **A computer**: Running Ubuntu 24.04 or Kubuntu 24.04 Desktop or Server (fresh or existing). Minimum: 4GB RAM, 20GB storage, CPU with virtualization support (Intel VT-x or AMD-V). More RAM/storage for multiple VMs.
    
* **Internet access**: To download packages and VM ISOs.
    
* **A web browser**: Firefox (default on Ubuntu) or Chrome to access Cockpit.
    
* **An ISO image**: An ISO image for your guest VM (for example, Ubuntu 24.04 Desktop ISO from ubuntu.com or Windows ISO if you have it already).
    
* **30–45 minutes**: Depending on your setup speed.
    

## Why KVM on Ubuntu/Kubuntu 24.04?

KVM turns your Linux kernel into a hypervisor, letting you run VMs with near-native speed. Paired with QEMU (for hardware emulation) and libvirt (for management), it’s a lightweight alternative to **Proxmox** or **VMware**. Its strengths include:

* **Performance**: Runs VMs efficiently, ideal for homelabs or dev environments.
    
* **Free and Open-Source**: No licenses, just like Ubuntu/Kubuntu, and so on.
    
* **Flexibility**: Supports diverse guest OSs (Linux, Windows, BSD).
    
* **Integration**: Cockpit’s web UI makes VM management a breeze, no CLI required.
    

Here’s what each tool does:

* **KVM**: A Linux kernel module that turns your system into a hypervisor, enabling VMs to run with near-native performance by leveraging CPU virtualization features (for example, Intel VT-x).
    
* **QEMU**: A powerful emulator that provides the virtual hardware (for example, CPU, disk, network) for your VMs, working with KVM for fast execution.
    
* **libvirt**: A management layer that simplifies VM creation, networking, and storage, offering tools like `virsh` and APIs for automation.
    
* **Cockpit**: A web-based interface for managing VMs, system resources, and networks, perfect for beginners who want a visual dashboard.
    

Ubuntu 24.04 (“Noble Numbat”) brings the latest kernel and tools, ensuring top-notch KVM compatibility. Let’s build your hypervisor!

## Step 1: Check Virtualization Support

First, you’ll want to confirm that your CPU supports virtualization (most modern ones do). To do that, open a terminal (like Konsole on Kubuntu) and run:

```bash
lscpu | grep Virtualization
```

Look for "VT-x" (Intel) or "AMD-V" (AMD). If present, you’re good!

If nothing shows, check your BIOS/UEFI:

* Reboot, enter BIOS (usually `F2`, `Del`, or `Esc`).
    
* Enable "Intel VT-x" or "AMD-V" under CPU settings.
    
* Save and reboot.
    

![Konsole terminal on Kubuntu displaying ‘lscpu | grep Virtualization’ output confirming VT-x support for KVM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745226012162/337e2324-50b3-4bd9-b040-01c2ac919e7c.png align="center")

## Step 2: Install KVM and Backend Tools

Let’s install KVM, QEMU, and libvirt. These will form the backbone of your hypervisor:

Start by updating your system (you may need to restart your computer after the update):

```bash
sudo apt update && sudo apt upgrade -y
```

Then install the virtualization packages:

```bash
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y
```

* `qemu-kvm`: Emulates hardware for VMs.
    
* `libvirt-daemon-system`: Manages VMs.
    
* `libvirt-clients`: CLI tools like `virsh` for hypervisor management.
    
* `bridge-utils`: For network bridging.
    

Next, verify that KVM is loaded:

```bash
lsmod | grep kvm
```

You’ll see “kvm\_intel” or “kvm\_amd” if successful.

![Konsole terminal on Kubuntu displaying ‘lsmod | grep kvm’ output showing kvm_intel module loaded for KVM.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745226199517/a146d89d-2894-4bbc-b241-11a8ed385758.png align="center")

Finally, add your (current) user to the `libvirt` group for permission:

```bash
sudo usermod -aG libvirt $USER
```

Log out and back in to apply these changes.

## Step 3: Set Up a Network Bridge

VMs need network access, so you’ll create a bridge (`br0`) to connect them to your physical network. This allows VMs to act like devices on your network (bridged networking).

Ubuntu 24.04 and Kubuntu 24.04 Desktop typically use NetworkManager, while Ubuntu Server may use Netplan. We’ll prioritize the NetworkManager approach, with Netplan as an alternative.

**Note**: Installing libvirt (Step 2) creates a default bridge called `virbr0` for NAT-based networking, which isolates VMs from the physical network (IPs like `192.168.122.x`). For direct network access (IPs like `192.168.0.x`), use `br0` as described below, and select it in Step 5’s VM setup.

You can verify whether your system is using NetworkManager or Netplan. Open a console and run `systemctl status NetworkManager`. If you see the status active and running, go with NetworkManager.

![Konsole terminal on Kubuntu displaying ‘systemctl status NetworkManager’ output confirming NetworkManager status.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745305149513/0926f09c-1748-484f-af4c-37dcb82d06a5.png align="center")

### Option 1: NetworkManager (Recommended for Kubuntu/Ubuntu desktop)

Check your network interface:

```bash
ip link
```

Example: `enp4s0`. Replace `enp4s0` below if yours differs.

First, find your Ethernet connection name:

```bash
nmcli connection show
```

Look for the **NAME** column where **DEVICE** is `enp4s0` (for example, “Wired connection 1” or “Ethernet connection”). Note this name. Ignore `virbr0`, which is libvirt’s default NAT bridge.

Then create a bridge named `br0`:

```bash
sudo nmcli connection add type bridge ifname br0 con-name bridge-br0
```

Enslave your interface to the bridge:

```bash
sudo nmcli connection add type ethernet ifname enp4s0 master br0 con-name bridge-slave-enp4s0
```

Disable the old connection (replace with your connection name identified earlier):

```bash
sudo nmcli connection down "Wired connection 1"
sudo nmcli connection delete "Wired connection 1"
```

Enable DHCP on the bridge:

```bash
sudo nmcli connection modify bridge-br0 ipv4.method auto
```

Activate the bridge:

```bash
sudo nmcli connection up bridge-br0
```

Verify:

```bash
ip addr show br0
nmcli connection show
```

Now you’ll want to ensure `br0` is active, `enp4s0` is enslaved, and `virbr0` is separate. First, test the internet with `ping 8.8.8.8`.

Then you need to define `br0` in libvirt (to appear in Cockpit’s VM network dropdown). To do this, create `br0.xml` in your home directory:

```bash
nano ~/br0.xml
```

Then add the following:

```xml
<network>
  <name>br0</name>
  <forward mode='bridge'/>
  <bridge name='br0'/>
</network>
```

Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

Now define and start the following:

```bash
sudo virsh net-define ~/br0.xml
sudo virsh net-start br0
sudo virsh net-autostart br0
```

Verify like this:

```bash
virsh net-list --all
```

You can now delete `~/br0.xml` after defining, as libvirt stores it in `/etc/libvirt/qemu/networks/`.

```bash
rm ~/br0.xml
```

### Option 2: Netplan (For Ubuntu Server or If Preferred)

If you see `renderer: networkd` in `/etc/netplan/???.yaml` or prefer Netplan, follow these steps.

First, check your interface:

```bash
ip link
```

Example: `enp4s0`.

Next, edit the Netplan config like so:

```bash
sudo nano /etc/netplan/01-netcfg.yaml
```

Use the following:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp4s0:
      dhcp4: no
  bridges:
    br0:
      interfaces: [enp4s0]
      dhcp4: yes
```

Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

Now, set strict permissions to avoid errors:

```bash
sudo chmod 600 /etc/netplan/01-netcfg.yaml
```

And apply:

```bash
sudo netplan apply
```

Now verify:

```bash
ip addr show br0
```

Test the internet with `ping 8.8.8.8` (from console).

![Konsole terminal on Kubuntu displaying ‘nmcli connection show’ output with bridge-br0 active, enp4s0 enslaved, and virbr0 present for KVM networking.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745227201229/35988335-5ff1-49bc-9809-e9c08d6798c4.png align="center")

**Troubleshooting**:

* **Permissions error**: If Netplan complains about “too open” permissions, recheck `sudo chmod 600 /etc/netplan/01-netcfg.yaml`.
    
* **NetworkManager conflict**: If using Netplan, ensure `/etc/netplan/01-network-manager-all.yaml` is backed up or deleted (`sudo mv /etc/netplan/01-network-manager-all.yaml /etc/netplan/01-network-manager-all.yaml.bak`).
    
* **No onternet**: Restart NetworkManager (`sudo systemctl restart NetworkManager`) or reboot.
    
* **Wrong bridge**: If a VM uses `virbr0` (NAT, `192.168.122.x`), recheck Step 5’s network setting and select `br0`.
    
* **br0 missing in Cockpit**: Define `br0` in libvirt (step 9 above) or ensure `br0` is active (`ip addr show br0`).
    

## Step 4: Install Cockpit for Web Management

Cockpit provides a slick web UI to manage VMs. Let’s go ahead and set it up.

First, you’ll need to install Cockpit and its VM plugin:

```bash
sudo apt install cockpit cockpit-machines -y
```

Then you can start and enable Cockpit:

```bash
sudo systemctl enable --now cockpit.socket
systemctl status cockpit.socket
```

Now open your browser (for example, Firefox on Ubuntu) and visit:

```plaintext
https://localhost:9090
```

Or use your KVM server’s IP (for example, `https://192.168.0.100:9090`) if remote. Log in with your username and password. Ignore the self-signed certificate warning.

Allow Cockpit’s port if you’re using a firewall:

```bash
sudo ufw allow 9090
```

You’ll see Cockpit’s dashboard. Turn on administrative access by clicking on “**Turn on administrative access**”. Then, click “**Virtual Machines**” to manage VMs.

![Firefox on Kubuntu displaying Cockpit login page at https://localhost:9090 for web-based VM management.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745227293385/96291774-d4cf-4de2-9392-3947ade4bb8b.png align="center")

## Step 5: Create a Guest VM

Let’s create a guest VM using Cockpit. We’ll use an Ubuntu 24.04 Desktop ISO as an example:

To start, download the Ubuntu 24.04 Desktop ISO from ubuntu.com and save it (for example, `/home/ranju/Downloads/ubuntu-24.04.1-desktop-amd64.iso`).

In Cockpit, go to “Virtual Machines” and click “Create VM”. Here are the specs:

* **Name**: TestVM
    
* **Installation Type**: Local install media (or your desired installation type)
    
* **Installation Source**: Browse to your ISO (for example, `/home/ranju/Downloads/ubuntu-24.04.1-desktop-amd64.iso`).
    
* **OS**: Select “Ubuntu 24.04” (usually Cockpit auto-detects).
    
* **Storage**: Create new qcow2 volume (preferred). *Note: disk is created in* `/var/lib/libvirt/images/`*.*
    
* **Storage limit**: 20GB (adjust as needed).
    
* **Memory**: 4GB (adjust as needed).
    

Click “Create and Edit”. Cockpit opens an advanced dialog where there are options for customization (for example, CPU, Network Interfaces and Boot order, and so on). Make sure that `br0` has been selected as interface source. Finally, click “**Install**”.

![Cockpit web interface in Firefox on Kubuntu showing the Create VM dialog with TestVM settings.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745228999671/4d80faf7-d8f8-4395-985e-298b4add426c.png align="center")

In Cockpit’s VM console, follow the installer to set up the guest OS (username, password, and so on).

**Troubleshooting**:

* **Permissions error**: If you have permission error for the ISO, then copy the ISO to the default temp folder (`/tmp/`) and locate the ISO from there.
    
    ```bash
    cp /home/ranju/Downloads/ubuntu-24.04.1.iso /tmp/
    ```
    

## Step 6: Run and Test Your Guest VM

Your VM is running! Let’s test it:

1. In Cockpit, under “Virtual Machines,” click TestVM. You’ll see its console (a live view of the VM’s screen).
    
2. Log into the guest Ubuntu using the credentials you set.
    
3. Test networking:
    
    * Open a terminal in the VM (via Cockpit’s console).
        
    * Run `ip addr` in the console to confirm a physical network IP (for example, `192.168.0.x` with `br0`, not `192.168.122.x` with `virbr0`).
        
    * Run `ping 8.8.8.8` to confirm internet access.
        
4. Experiment: Open a browser in the VM, visit a website, or install apps to simulate real use.
    

If the VM boots and connects to your network, your KVM hypervisor is rocking! You can stop, restart, or delete it from Cockpit.

![Cockpit web interface in Firefox on Kubuntu displaying the TestVM console with Ubuntu 24.04 desktop.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745307664700/ed54d452-4979-4468-a7fe-1dd538844e25.png align="center")

## Keep Exploring Your Hypervisor

You’ve turned your Ubuntu 24.04 into a KVM hypervisor – congrats! Try these next steps:

* **Add more VMs**: Create Windows or other Linux VMs using different ISOs.
    
* **Use virt-manager**: Install virt-manager for a desktop-based alternative to Cockpit (`sudo apt install virt-manager`).
    
* **Back up VMs**: Export VM disks with `virsh` for safety.
    
* **Scale up**: Add storage or RAM for heavier workloads, like my Proxmox cluster guide.
    

Check your VMs anytime via CLI:

```bash
virsh list --all
```

## Wrapping Up

You’ve built a fast, free KVM hypervisor on Ubuntu 24.04, complete with Cockpit’s web UI and a running guest VM. It’s a perfect playground for coding, testing, or homelab fun.

Share your ideas or comments with me – I’d love to hear them!
