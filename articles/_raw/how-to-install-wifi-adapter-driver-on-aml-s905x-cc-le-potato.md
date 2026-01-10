---
title: How to Install a Wifi Adapter Driver on AML-S905X-CC (Le Potato)
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2022-11-30T17:27:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-wifi-adapter-driver-on-aml-s905x-cc-le-potato
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/How-to-install-driver-for-external-wifi-adapter-in-Le-Potato-3.png
tags:
- name: Raspberry Pi
  slug: raspberry-pi
- name: wifi
  slug: wifi
seo_title: null
seo_desc: "If you're a developer, you might be familiar with Raspberry Pi. But you\
  \ might not know about the Libre Computer AML-S905X-CC – also called Le Potato.\
  \ \nThere was a chip shortage during the pandemic that has resulted in increased\
  \ Raspberry Pi prices. O..."
---

If you're a developer, you might be familiar with Raspberry Pi. But you might not know about the Libre Computer AML-S905X-CC – also called Le Potato. 

There was a chip shortage during the pandemic that has resulted in increased Raspberry Pi prices. Other world events have also skyrocketed the price of Raspberry Pis, and the manufacturing of a few models has even been stopped. You can read more about it [here](https://www.raspberrypi.com/news/supply-chain-shortages-and-our-first-ever-price-increase/). 

Because of this, I felt that switching to a Raspberry Pi alternative would be a good option for a project I wanted to work on.

Le Potato is similar to Raspberry Pi in terms of appearance, configuration, and so on. It also has the ability to run numerous operating systems such as Ubuntu, Debian, Raspbian, Android, and others. 

But unfortunately, it does not come with a pre-installed wifi module, whereas Raspberry Pi has the wifi module pre-installed. 

In this article, I'll give you clear step-by-step instructions to install an external wifi adapter driver in Le Potato running **Ubuntu OS**. For those who are running other operating systems, you can try the following steps, but I cannot assure you that it'll definitely work. 

Let's have a quick look at my accessories. 

##### Here's my Le Potato device:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Le-Potato.jpeg)
_Le Potato Device_

##### And here's my Zebronics External Wifi Adapter:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Wifi-Device-1.jpeg)
_Zebronics External Wifi Adapter_

## Trial and Error – What Didn't Work

Before I found my final solution and ended up installing the wifi driver and being able to access the internet with my wifi adapter, I tried many approaches. But none of them worked out. 

Here's what I tried along the way:

1. I tried to install the driver given on the CD that was delivered along with the wifi adapter. But, I couldn't understand the steps they asked me to follow and finally ended up with a lot of errors.
2. I downloaded the exact driver for this device from the Zebronics official site. Again that did not pay off well.
3. I tried to install some open source drivers from GitHub forked by many people from the Realtek source. This also did not work out as expected.

Finally, I found an answer from the [Ubuntu Q&A forum](https://askubuntu.com/questions/1415466/wireless-usb-apapter-not-show-any-available-networks) and I was able to install it on the first try. Though the steps were not so clear initially, I managed to figure them out. So I'll explain how to do it here. 

## How to Install the Wifi Adapter Driver for Le Potato in Ubuntu

Follow the below steps to install the driver on your device:

### Install the dependencies

The first step is to install the required software. 

You need to install `git`, `dkms`, `build-essential`, and `linux-headers` for your system architecture. 

You can install them all together in a single command:

```bash
sudo apt-get install -y build-essential git dkms linux-headers-$(uname -r)
```

If you have been prompted (yes/no) while running the above command, just hit `y` (which is basically agreeing to install the software in your system). 

### Download the driver source

Drivers for some devices will not be available in any installable/executable formats. In such cases, you should download, compile, and install the source code on the machine directly. Unfortunately, this driver also falls under this category. 

We can download the source of this driver from GitHub. Run the following command in your terminal to download the source code:

```bash
git clone https://github.com/kelebek333/rtl8188fu
```

### Build and install the driver

Before building and installing the driver, you need to know about the `dkms` command in Linux. If you know about `dkms`, you can skip this paragraph and move on to the next paragraph. 

DKMS stands for Dynamic Kernel Module Support. It's a program/framework that lets you install the supplementary versions of kernel modules. A package can be compiled and installed into the kernel tree. DKMS is called automatically upon installation of new Ubuntu kernel-image packages, and so modules added to DKMS will be automatically carried across updates. 

This is the source package that we downloaded in the previous step. We need to add, compile, and install the source package into our kernel tree. 

Run the following commands sequentially to add, compile and install the driver package:

#### Add Source to Kernel

```bash
sudo dkms add ./rtl8188fu
```

#### Compile source package

```bash
sudo dkms build rtl8188fu/1.0
```

#### Install the package into the kernel tree

```bash
sudo dkms install rtl8188fu/1.0
```

#### Copy the firmware

The compiled binary firmware file should then be copied to the default firmware location in Linux, that is `/lib/firmware` . 

**Firmware** is software that enables the communication between hardware and software. It gives the machine instructions that make the hardware function. 

Run the following command to copy the compiled firmware:

```bash
sudo cp ./rtl8188fu/firmware/rtl8188fufw.bin /lib/firmware/rtlwifi/
```

### Disable power saving and auto suspend modes on kernel

It is always a good idea to disable power saving and auto suspend modes for wifi drivers. So, you'll need to add this option by default on updating the kernel, too. You can add this configuration in the `.conf` file in `/etc/modprobe.d/` directory. 

We are creating this conf file in `/etc/modprobe.d` directory, because we need to load this customized module with the persistent changes. 

You use the `rtw_power_mgnt` flag to control power saving mode:

* 0 - Disables power saving
* 1 - Power saving on with minPS
* 2 - Power saving on with maxPS

You use the `rtw_enusbss` flag to control auto-suspend mode:

* 0 - Disables auto suspend
* 1 - Enables auto suspend

Run the following commands to create a `.conf` file and store the options:

```bash
sudo mkdir -p /etc/modprobe.d/
sudo touch /etc/modprobe.d/rtl8188fu.conf
echo "options rtl8188fu rtw_power_mgnt=0 rtw_enusbss=0" | sudo tee /etc/modprobe.d/rtl8188fu.conf
```

### Blacklist the existing module

You have to blacklist the module which you tried to install before. 

**Note:** Blacklisting a module will not allow it to be loaded automatically, but the module may be loaded if another non-blacklisted module depends on it or if it is loaded manually. 

Let's assume you have added a module named `rtl8188au`. Then, you need to blacklist it by adding the following line at the end of the `/etc/modprobe.d/blacklist.conf` file. 

```bash
blacklist rtl8188au
```

If you haven't added any such module, you can ignore the blacklisting part. 

### Reload the module

You need to reload the module to make it start working. 

Here's the command to reload the module we added now:

```bash
sudo modprobe -rv rtl8188fu && sudo modprobe -v rtl8188fu
```

And you're done! You should be able to see the wifi enabled on your Le Potato running Ubuntu OS. If you cannot see it, reboot your system and everything should be alright.  

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-98.png)
_Trying to connect to a network after installing the driver_

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-97.png)
_Connected to my wifi network_

## Conclusion

In this article, we have gone through the steps to install the driver for our external wifi adapter. 

These are the exact (basic) steps you need to follow to add any external module into your kernel. 

Subscribe to my [newsletter](https://5minslearn.gogosoon.com/) to receive more such insightful articles that get delivered straight to your inbox. 


