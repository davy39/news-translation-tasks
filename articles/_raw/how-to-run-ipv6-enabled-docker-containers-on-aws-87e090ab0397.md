---
title: How to run IPv6-enabled Docker containers on AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T16:39:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-ipv6-enabled-docker-containers-on-aws-87e090ab0397
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E3u4QZGhjH8VH_X3fzMWfQ.png
tags:
- name: AWS
  slug: aws
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nicolas Leiva

  Do you want to forget about NAT and run containers without having to translate IP
  addresses? Then you need public IP addresses, lots of them. Unfortunately, the price
  of each IPv4 address is exceeding $20, so you won’t get one for ea...'
---

By Nicolas Leiva

Do you want to forget about NAT and run containers without having to translate IP addresses? Then you need public IP addresses, lots of them. Unfortunately, the price of each IPv4 address [is exceeding $20](http://www.circleid.com/posts/20181024_the_2018_ipv4_market_third_quarter_report/), so you won’t get one for each and every one of your containers. On the other hand, there is no shortage of IPv6 addresses, so you could in theory assign a unique one to as many containers as you’d like.

When the Internet protocol (**IP**) that helps deliver this blog post to your device was defined [back in 1981](https://tools.ietf.org/html/rfc791), the internet addresses that identify sources and destinations were specified as fixed length of four octets (**32 bits**). This is actually the fourth version of the protocol, so we refer to these addresses as IP version 4 (**IPv4**) addresses.

Approximately a decade later, [in 1992](https://tools.ietf.org/html/rfc1338), it became evident that we would eventually run out of 32-bit IPv4 addresses, so in [march 1994](https://tools.ietf.org/html/rfc1597), re-usable **private IP** addresses were defined in an attempt to preserve IP address space. You use these to identify hosts private to an enterprise. If any of these hosts need to connect to an outside host, its address needs to be translated into **a — public** — **IP** address that is globally unique. This process is know as Network Address Translation (**NAT**) and was defined a [couple of months later](https://tools.ietf.org/html/rfc1631).

About [a year later (1995)](https://www.rfc-editor.org/rfc/rfc1883.txt), a new version of the Internet Protocol came out to provide — [among other things](https://tools.ietf.org/html/rfc2460#page-2) — expanded addressing capabilities. We know this as **IPv6**, which increases the IP address size from 32 bits to **128 bits**.

> The problem? IPv6 is not backwards compatible with IPv4, therefore the transition has been really, really slow… Over 20 years now with a current [adoption of ~22%](https://www.google.com/intl/en/ipv6/statistics.html).

Anyways, the purpose of this post is to demonstrate how to run Containers on a Cloud Provider (AWS) using IPv6. This is something that was pending from my previous post: [Kubernetes multi-cluster networking made simple](https://medium.com/@nleiva/kubernetes-multi-cluster-networking-made-simple-c8f26827813). The target topology is the following.

![Image](https://cdn-media-1.freecodecamp.org/images/MxC6Wfw0JBNLbelksIgWkgtnukt8PrBUN7qY)

While we cannot currently breakup an IPv6 Block allocated to a `VPC` (`/56`), to assign smaller subnets (`/64`) to instances in AWS, we can use Elastic Network Interfaces ([ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)) to associate a contiguous block of IPv6 addresses to an instance. This will generate an IPv6 prefix length greater than `/64`—in this example `/126` — which is not a best practice in a LAN, so take this with a grain of salt.

In a nutshell, this is what we will do:

1. Create [EC2](https://aws.amazon.com/ec2/) instances with an [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) attached to it.
2. Re-configure IPv6 addressing on the instance and install Docker.
3. Run a couple of Containers using only IPv6.

### Create EC2 instances with an ENI attached to it

We will use the AWS [CLI](https://aws.amazon.com/cli/) [create-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-interface.html) to create an [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) with a primary IPv6 address and also a contiguous block of IPv6 addresses for each one of our instances. These addresses will come from a known `Subnet`. We will also apply a `Security Group` to our [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html).

#### Subnet, Security Group and ENI

If you don’t have a `VPC` with IPv6 support already, please take a look at [Getting Started with IPv6 for Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/get-started-ipv6.html), so you can store the ID of the`Subnet` and `Security Group` in the variables `subnetId` and `sgId`.

```
subnetId=subnet-09a931730fa9exxxxsgId=sg-0eaf439572982yyyy
```

For `instance-1` we will reserve addresses `::1:1`, `::8`, `::9`, `::a` and `::b`. I have removed the subnet prefix for the ease of reading. The first address will be for the instance, and the other four will make the `/126` we need for the linux bridge the containers will be connected to.

```
2600:1f18:47b:ca03::1:12600:1f18:47b:ca03::82600:1f18:47b:ca03::92600:1f18:47b:ca03::a2600:1f18:47b:ca03::b
```

For our `instance-2` we will reserve addresses `::2:2`, `::c`, `::d`, `::e` and `::f`.

```
2600:1f18:47b:ca03::2:22600:1f18:47b:ca03::c2600:1f18:47b:ca03::d2600:1f18:47b:ca03::e2600:1f18:47b:ca03::f
```

With all this info we execute the [create-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-network-interface.html) command. However, we also need to store the ID of [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) for the following operations, so we `query` `NetworkInterface.NetworkInterfaceId` and store the returned value in `eni1` for `instance-1`.

```
eni1=`aws ec2 create-network-interface \  --subnet-id $subnetId \  --description "My IPv6 ENI 1" \  --groups $sgId \  --ipv6-addresses \  Ipv6Address=2600:1f18:47b:ca03::1:1 \  Ipv6Address=2600:1f18:47b:ca03::8 \  Ipv6Address=2600:1f18:47b:ca03::9 \  Ipv6Address=2600:1f18:47b:ca03::a \  Ipv6Address=2600:1f18:47b:ca03::b \  --query 'NetworkInterface.NetworkInterfaceId' \  --output text`
```

You can check the value returned as follows.

```
$ echo $eni1eni-08ba7c2f50a22a160
```

Repeat for the second [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html).

```
eni2=`aws ec2 create-network-interface \  --subnet-id $subnetId \  --description "My IPv6 ENI 2" \  --groups $sgId \  --ipv6-addresses \  Ipv6Address=2600:1f18:47b:ca03::2:2 \  Ipv6Address=2600:1f18:47b:ca03::c \  Ipv6Address=2600:1f18:47b:ca03::d \  Ipv6Address=2600:1f18:47b:ca03::e \  Ipv6Address=2600:1f18:47b:ca03::f \  --query 'NetworkInterface.NetworkInterfaceId' \  --output text`
```

#### Launching instances with ENI attached

Amazon EC2 uses public–key cryptography to encrypt and decrypt login information [[Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)], so you need a public and private key to connect to the instances.

You can use an existing one or alternatively create one as follows, where `~/.ssh/id_rsa.pub` is the location of your public key file.

```
aws ec2 import-key-pair \  --key-name <name> \  --public-key-material file://~/.ssh/id_rsa.pub
```

We will store the name of the key pair in a variable named `AWS_SSH_KEY`. You either assign the name manually, as you just picked it, or retrieve it from AWS with `describe-key-pairs`.

```
AWS_SSH_KEY=$(aws ec2 describe-key-pairs --query KeyPairs[0].KeyName --output text)
```

Now is time to create the instances. We will use [AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) ID `ami-0ac019f4fcb7cb7e6`, which is `Ubuntu Server 18.04 LTS`, and instance type `r5d.large`.

The number of IP addresses you can assign to an instance is restricted by its type, so for `r5d.large` for example we can go up to 10 IPv6 addresses, which is enough for this small proof of concept. See the details for instance type in [IP Addresses Per Network Interface Per Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI).

We also want to attach the [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) we previously created, whose ID was stored in `eni1`. We keep the instance ID we receive back from AWS in `vm1` (we are querying`Instances[0].InstanceId`).

```
vm1=`aws ec2 run-instances \  --key-name $AWS_SSH_KEY \  --image-id ami-0ac019f4fcb7cb7e6 \  --instance-type r5d.large \  --network-interfaces DeviceIndex=0,NetworkInterfaceId=$eni1 \  --query 'Instances[0].InstanceId' \  --output text`
```

Similarly for `instance-2`.

```
vm2=`aws ec2 run-instances \  --key-name $AWS_SSH_KEY \  --image-id ami-0ac019f4fcb7cb7e6 \  --instance-type r5d.large \  --network-interfaces DeviceIndex=0,NetworkInterfaceId=$eni2 \  --query 'Instances[0].InstanceId' \  --output text`
```

Next, let’s get the first public IPv6 address of `instance-1` and store it in `ip1`.

```
ip1=`aws ec2 describe-instances \  --filter Name=instance-id,Values=$vm1 \  --output text \  --query 'Reservations[].Instances[].NetworkInterfaces[].\Ipv6Addresses[0].Ipv6Address'`
```

You can now access `instance-1` with `ssh -i <private key file> ubuntu@`${ip1}. Similarly`, for inst`ance-2 you can retrieve the first public IPv6 address with:

```
ip2=`aws ec2 describe-instances \  --filter Name=instance-id,Values=$vm2 \  --output text \  --query 'Reservations[].Instances[].NetworkInterfaces[].\Ipv6Addresses[0].Ipv6Address'`
```

So you can access it with `ssh -i <private key file> ubuntu@`${ip2}.

#### Making the instances IPv6-friendly

We will need to install software in our instances. Unfortunately, this won’t be possible right off the bat as our `sources.list` file comes with links to `[us-east-1.ec2.archive.ubuntu.com](http://us-east-1.ec2.archive.ubuntu.com/ubuntu/)`, that don’t resolve to an IPv6 address. ? We need to replace these to use a`[rchive.ubuntu.com](http://us-east-1.ec2.archive.ubuntu.com/ubuntu/)` instead, which properly supports IPv6. You can do this with s`ed.`

```
sudo sed -i 's/us-east-1\.ec2\.//g' /etc/apt/sources.list
```

Now you can use `apt-get` with the option `Acquire::ForceIPv6=true`.

```
$ sudo apt-get -o Acquire::ForceIPv6=true updateGet:1 http://archive.ubuntu.com/ubuntu bionic InRelease [242 kB]Get:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [83.2 kB]Get:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]...Get:38 http://archive.ubuntu.com/ubuntu bionic-backports/universe Sources [2068 B]Get:39 http://archive.ubuntu.com/ubuntu bionic-backports/universe amd64 Packages [3468 B]Get:40 http://archive.ubuntu.com/ubuntu bionic-backports/universe Translation-en [1604 B]Fetched 28.4 MB in 5s (5363 kB/s)Reading package lists... Done
```

### Re-configure IPv6 addressing on the instance and install Docker

Right now, our instances have a single interface with multiple IPv6 addresses. `instance-1` shows five `/128` IPv6 addresses.

```
$ ip add...2: ens5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000...    inet6 2600:1f18:47b:ca03::1:1/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec    inet6 2600:1f18:47b:ca03::8/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec    inet6 2600:1f18:47b:ca03::9/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec    inet6 2600:1f18:47b:ca03::a/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec    inet6 2600:1f18:47b:ca03::b/128 scope global dynamic noprefixroute       valid_lft 385sec preferred_lft 85sec
```

#### New IPv6 address distribution

We want only one (`/64`) in the main interface and a `/126` in a linux bridge (docker0) to allocate addresses to our containers from this range. For this purpose, we will edit [netplan](https://netplan.io/)’s config file at `/etc/netplan/50-cloud-init.yaml`. It originally looks like this:

```
network:  version: 2  ethernets:    ens5:      dhcp4: true      dhcp6: true      match:        macaddress: 12:fb:b4:8b:15:f8      set-name: ens5
```

We only remove the `dhcp6` statement from it.

```
network:  version: 2  ethernets:    ens5:      dhcp4: true      match:        macaddress: 12:fb:b4:8b:15:f8      set-name: ens5
```

As a side note, and completely **optional**, the `MAC` address of the instance and IPv6 addresses associated to it can be retrieved from the [Instance Metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-retrieval) anytime.

```
$ curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/12:fb:b4:8b:15:f8
```

And:

```
$ curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/12:fb:b4:8b:15:f8/ipv6s/2600:1f18:47b:ca03:0:0:0:82600:1f18:47b:ca03:0:0:0:92600:1f18:47b:ca03:0:0:0:a2600:1f18:47b:ca03:0:0:0:b2600:1f18:47b:ca03:0:0:1:1
```

> ⚠️ Yeah, [Instance Metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-retrieval) is an IPv4-only service ?. The good news is you don’t need a public IPv4 address to access to it.

Continuing with the instance’s interface configuration, we need to also create a separate file for the IPv6 config at`/etc/netplan/60-ipv6-static.yaml`.

```
network:  version: 2  ethernets:    ens5:      dhcp6: no      accept-ra: no      addresses:      - 2600:1f18:47b:ca03::1:1/64      gateway6: fe80::1066:30ff:feb8:c008
```

We disabled DHCPv6 (`dhcp6: no`) and discarded IPv6 Router Advertisements (`accept-ra: no`). The gateway information (`fe80::1066:30ff:feb8:c008`) comes from an `iproute2` command (seems like it’s always the same in EC2).

```
$ ip -6 route | grep defaultdefault via fe80::1066:30ff:feb8:c008 dev ens5 proto ra metric 100 pref medium
```

Finally, apply our config changes with `netplan apply`.

```
sudo netplan --debug apply
```

We repeat for `instance-2` with the corresponding addresses.

#### Install Docker

You can follow the [official installation guide](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce) or just run the following commands. Notice the option `Acquire::ForceIPv6=true` for `apt-get`.

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"sudo apt-get -o Acquire::ForceIPv6=true updatesudo apt-get -o Acquire::ForceIPv6=true install -y docker-cesudo usermod -aG docker ${USER}
```

You need to log out and log back in for the user changes to take effect.

We will edit/create a Docker config file at `/etc/docker/daemon.json` to start allocating IPv6 addresses to our containers. Should look like this for `instance-1`.

```
{  "ipv6": true,  "fixed-cidr-v6": "2600:1f18:47b:ca03::8/126"}
```

Then re-start the daemon to apply the changes; `sudo systemctl restart docker`. We have now successfully split the [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) IPv6 address allocation between the main interface and the Docker bridge.

```
$ ip add...2: ens5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000...    inet6 2600:1f18:47b:ca03::1:1/64 scope global       valid_lft forever preferred_lft forever...3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default...    inet6 2600:1f18:47b:ca03::9/126 scope global tentative       valid_lft forever preferred_lft forever...
```

Do the same for `instance-2`, with `fixed-cidr-v6` = `::c/126`.

### Run a couple of Containers using only IPv6

We are ready to run containers. Or at least that’s what I thought. Turns out `registry-1.docker.io` and `hub.docker.com` don’t support IPv6, so we can’t get Docker images from it. ?

#### Running an Image

Have we come to a dead end? No, Google Container Registry comes to our rescue! → `gcr.io/gcp-runtimes/ubuntu_18_0_4:latest`. Let’s run this on each instance.

```
docker run -it --rm gcr.io/gcp-runtimes/ubuntu_18_0_4:latest bash
```

Install `ping` and `iproute2` in each container to do some connectivity tests and check the routing table.

```
apt-get -o Acquire::ForceIPv6=true updateapt-get -o Acquire::ForceIPv6=true install iputils-ping iproute2 -y
```

At this point, we have already validated the instances can access the Internet over IPv6 (via `apt-get`). Let’s look at the IP addresses allocated; we got `::a` in the container on `instance-1` (`container-1`). Similarly, we got `::e` in the container running on `instance-2` (`container-2`).

```
root@d7c9480161f9:/# ip add...4: eth0@if5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default...    inet6 2600:1f18:47b:ca03::a/126 scope global nodad       valid_lft forever preferred_lft forever...
```

To make more explicit that this is working, we can ping a host in the Internet over IPv6.

```
root@d7c9480161f9:/# ping6 ipv6-test.com -c 1PING ipv6-test.com(agaric.t0x.net (2001:41d0:8:e8ad::1)) 56 data bytes64 bytes from agaric.t0x.net (2001:41d0:8:e8ad::1): icmp_seq=1 ttl=46 time=78.7 ms
```

```
--- ipv6-test.com ping statistics ---1 packets transmitted, 1 received, 0% packet loss, time 0msrtt min/avg/max/mdev = 78.788/78.788/78.788/0.000 ms
```

Ok, let’s now ping `container-2` (`d7c9480161f9`) from `container-1` (`5312fff41595`).

```
root@d7c9480161f9:/# ping6 2600:1f18:47b:ca03::e -c 1PING 2600:1f18:47b:ca03::e(2600:1f18:47b:ca03::e) 56 data bytes64 bytes from 2600:1f18:47b:ca03::e: icmp_seq=1 ttl=62 time=0.250 ms
```

```
--- 2600:1f18:47b:ca03::e ping statistics ---1 packets transmitted, 1 received, 0% packet loss, time 0msrtt min/avg/max/mdev = 0.250/0.250/0.250/0.000 ms
```

The other way around (`container-2` to `container-1)`, just in case. It all works. ?

```
root@5312fff41595:/#  ping6 2600:1f18:47b:ca03::a -c 1PING 2600:1f18:47b:ca03::a(2600:1f18:47b:ca03::a) 56 data bytes64 bytes from 2600:1f18:47b:ca03::a: icmp_seq=1 ttl=62 time=0.263 ms
```

```
--- 2600:1f18:47b:ca03::a ping statistics ---1 packets transmitted, 1 received, 0% packet loss, time 0msrtt min/avg/max/mdev = 0.263/0.263/0.263/0.000 ms
```

If this isn’t working for you, make sure the `Security Group` applied to the [ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) allows IPv6 ICMP from your instances. I specifically created an inbound `Custom ICMP Rule — IPv6` with the same `Security Group` ID as the source to make this example work.

#### Routing tables

Let’s explore the routing table in `container-1`.

```
root@d7c9480161f9:/# ip -6 route2600:1f18:47b:ca03::8/126 dev eth0 proto kernel metric 256 pref mediumfe80::/64 dev eth0 proto kernel metric 256 pref mediumdefault via 2600:1f18:47b:ca03::9 dev eth0 metric 1024 pref medium
```

`::9` is the IP in `docker0` as seen in a previous terminal output. What about `instance-1` routing’s table?

```
$ ip -6 route2600:1f18:47b:ca03::8/126 dev docker0 proto kernel metric 256 pref medium2600:1f18:47b:ca03::8/126 dev docker0 metric 1024 pref medium2600:1f18:47b:ca03::/64 dev ens5 proto kernel metric 256 pref medium...default via fe80::1066:30ff:feb8:c008 dev ens5 proto static metric 1024 pref medium
```

#### Word of advice

[Docker](https://docs.docker.com/v17.09/engine/userguide/networking/default_network/ipv6/#how-ipv6-works-on-docker) suggests we enable IPv6 routing on Linux to make this work by executing the following two lines.

```
sudo sysctl net.ipv6.conf.default.forwarding=1sudo sysctl net.ipv6.conf.all.forwarding=1
```

I didn’t have to do it for this example, as the EC2 instances came with this setup already. They also do not recommend IPv6 subnets smaller than `/80`.

> ⚠️ “The subnet for Docker containers should **at least have a size of /80**, so that an IPv6 address can end with the container’s MAC address and you prevent NDP neighbor cache invalidation issues in the Docker layer” [[Docker](https://docs.docker.com/v17.09/engine/userguide/networking/default_network/ipv6/#how-ipv6-works-on-docker)]

Last, but not least, I run into a [discussion](https://github.com/containernetworking/cni/issues/531) where they state IPv6 is disabled on containers in some Docker versions. I’m running `18.09.0`.

```
$ docker info  -f '{{.ServerVersion}}'18.09.0
```

The following are the network kernel settings for `disable_ipv6` within the container.

```
root@d7c9480161f9:/# sysctl -a | grep disable_ipv6net.ipv6.conf.all.disable_ipv6 = 1net.ipv6.conf.default.disable_ipv6 = 1net.ipv6.conf.eth0.disable_ipv6 = 0net.ipv6.conf.lo.disable_ipv6 = 0
```

### Conclusion

While this is not exactly the end goal, it is interesting to know we can run IPv6-only containers in the cloud **today**. ✅

Next up, I’ll try to extend this and run Kubernetes with only IPv6 on a cloud provider… Or maybe check out IPv6 support among different Cloud Providers first.

