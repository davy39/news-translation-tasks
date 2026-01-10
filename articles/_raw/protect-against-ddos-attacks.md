---
title: How to Protect Against DDoS Attacks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-10T17:36:54.000Z'
originalURL: https://freecodecamp.org/news/protect-against-ddos-attacks
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-sora-shimazaki-5935794.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: null
seo_desc: "By Megan Kaczanowski\nDistributed Denial of Service (DDoS) attacks aim\
  \ to take an organization or service offline and originate from multiple, distributed\
  \ hosts. \nThe difficult part of defending against DDoS attacks is that the hosts\
  \ are distributed –..."
---

By Megan Kaczanowski

Distributed Denial of Service (DDoS) attacks aim to take an organization or service offline and originate from multiple, _distributed_ hosts. 

The difficult part of defending against DDoS attacks is that the hosts are distributed – if it were a single host or small group, you could easily block the traffic with a firewall rule. 

There are many different types of DDoS attacks, but we can broadly group them into three categories – volumetric, protocol, and application attacks. Let's look at each one in detail.

## What Are Volumetric DDoS Attacks?

Volumetric DDoS attacks aim to fill up a victim's bandwidth (such as UDP reflection attacks). 

A UDP reflection attack sends packets with the target's IP address spoofed as a the source. Then, the responses to the spoofed packet will be sent to the target, rather than the attacker. 

The advantage to going through an intermediate server rather than attacking the target directly is that response packets are typically much larger than the packet sent. For example, the response to a DNS query can be between 28 to 54 times larger than the original [request](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.pdf). 

In this way, an attacker can send many, smaller packets and the response packets will use up the resources of the target.

## What Are Protocol DDoS Attacks? 

Protocol DDoS attacks find a weakness in how a protocol operates (such as a SYN flood). A SYN flood exploits the way a three-way handshake works. 

When an attacker sends large numbers of SYN packets to a machine, the server will allocate resources to this request and send a SYN ACK packet back – assuming that it is the beginning of a connection request. 

Normally, the other server would respond with ACK, starting the connection. In the case of an attack, the attacker continues to send SYN requests without completing the connection, until the server is out of resources and unable to accept any additional traffic. 

## What Are Application DDoS Attacks? 

Application DDoS attacks target weaknesses in how an application works (such as a Slowloris attack). 

A Slowloris attack is very similar to a SYN flood, but targets webservers. It occurs when an attacker sends HTTP requests without completing them, continuing (slowly) to send additional headers to keep the connection open. 

As the connections are never completed, they absorb all of the server's available resources so it cannot process legitimate connections.

## Other Types of DDoS Attacks

Alternatively, DDoS attacks can be grouped based on the OSI model layer they impact. These are usually divided into infrastructure attacks (such as UDP reflection and SYN floods) or application attacks (such as HTTP floods and cache-busting). 

HTTP floods occur when an attacker sends a 'flood' of what appear to be legitimate HTTP requests to a server or application, exhausting its resources. 

Cache-busing attacks are a subset of HTTP floods which are designed to avoid CDN caching by varying the query string so the CDN must contact the origin server for every request, thus overloading it.

## Mitigation Measures for DDoS Attacks

The most important part of protecting against a DDoS attack is the preparation itself. It's much hard to deal with a DDoS attempt after it has begun.

### Scale Up Bandwidth

One way to deal with volumetric attacks is to scale up bandwidth in response. Unfortunately, this can be extremely difficult depending on the size of the attack, and an attacker's ability to scale up their attack size in response. 

Unless the organization being attacked is a service provider or an extremely large organization, it's unlikely that this is realistic. 

### Outsource Responses

Smaller organizations can outsource their responses to other, specialized firms, or to their ISP (or both). 

These types of relationships need to be in place prior to an attack occurring so that when one does occur, mitigation is as simple as reaching out to the ISP or service provider in order to activate protection (or having protection constantly on). 

Often what theDDoS protection provider will do is swing traffic to their environment (if it's not already passing through their environment). This can be via DNS, by updating the A record to point to an IP that the DDoS provider has allocated (though you need a low TTL in order to have this take effect quickly), or BGP, by advertising a route more specific than that which is currently being advertised.

### Have a DDoS-Specific Incident Response Plan

Even if the organization has outsourced their DDoS protection, having a DDoS-specific incident response plan is key. 

Once it's been written and agreed to by various stakeholders, it's important to review it at least annually (ideally via table top exercise) to ensure that everyone understands their role in the plan. 

A DDoS-specific response plan should include the following:

#### Pre-Event:

* **Circuit diagrams:** Create circuit diagrams which are as accurate as possible, including telecommunications contacts.   
  
Also create a map of your own network and any appropriate contacts (including those who are able and empowered to make local changes, as well as those who can contact the telco firm to make any updates).
* **Escalation:** Determine when (and how) to involve your ISP or a DDoS mitigation organization (with up to date contacts and a copy of the contract). 
* **Communication:** Develop a list of who should be notified and when (contact info for the security team, appropriate network team contacts, and so on).   
  
This should be divided into two groups - technical response folks (who can/will implement technical changes to address the attack) and everyone else (communications, legal, and so on). The second group should include anyone who may need to be involved, but who should be on a separate call from the technical folks making changes, in order to have as efficient a response as possible.   
  
Ideally this should be printed and distributed, so folks have access even if systems are unavailable.   
  
Ensure that your communications team has a plan for how and what to communicate in the event of an incident which takes down customer-facing assets.
* **Review:** These documents and contact lists should be reviewed regularly (at least quarterly).

#### During the Event:

* **Classify an event as a DDoS attack:** It needs to be confirmed that this is a DDoS attack, not just a short burst of high traffic or an error someone has made in the network. Ideally this also includes determining what type of attack is occurring and what the volume is.
* **Escalate:** Loop in the incident commander so they can begin notifying necessary folks.
* **Take initial steps:** If possible, [sinkhole](https://www.wired.com/story/what-is-sinkholing/) the traffic. If the traffic is higher than the link's bandwidth, reach out to your carrier (who will likely sinkhole the traffic on their end). Simultaneously, if you have a DDoS mitigation service, reach out to them as well.
* **Communicate:** Set up both a link for the technical folks to communicate and the non-technical folks to stay up to date on the incident.   
  
This is particularly important if public services go down for an extended period, as your comms team will need to be up to date in order to communicate with shareholders/media/customers.

#### Post-Event: 

* **Return to Normal:** When will you remove any mitigation measures? Who will sign off?
* **Attack Source:** What information can you gather about the attack to explain it and the attackers behind it? Was this a targeted attack? 
* **Lessons Learned:** What were they? How can they be used to improve the incident response plan?

### Build Resilient Architecture

Architecting systems to be resilient requires a comprehensive business continuity plan, with DDoS as a component of that plan. 

Essentially the same principles apply to data centers and networks when architecting for DDoS as when architecting for business continuity. You want to avoid any single points of failure or bottlenecks and have geographically diverse networks and diversity of providers. 

Content distribution networks (CDNs) are one way to improve your response to DDoS, as they provide a geographically distributed network of proxy servers which can significantly increase resilience.

Cloud architecture offers significant improvement over old models. It allows organizations of any size to create fully redundant systems which can be spun up and down and the click of a button. It also has geographically diverse infrastructure for a very low cost, and a cheap, easy way to scale load capacity up and down as needed. 

Architecting specifically for the cloud can enable organizations to take advantage of these new models and significantly improve your DDoS response.

### Upgrade Your Hardware

Some DDoS attack types are very old and can be mitigated by newer hardware. For example, you can defend against many protocol attacks (like SYN floods) and application attacks (like Slowloris) with appropriate network firewalls and load balancers. 

These firewalls can often monitor for signs of these types of attacks and close out connections once they reach unsustainable levels. Installing the correct hardware can mitigate the damage an attack could cause.

### Other Resources:

* [DDoS Quick Guide US CERT](https://us-cert.cisa.gov/sites/default/files/publications/DDoS%20Quick%20Guide.pdf)
* [AWS Best Practices for DDoS Resiliency](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.pdf)
* [NCC Cyber Incident Response DDoS](https://www.gov.scot/binaries/content/documents/govscot/publications/advice-and-guidance/2019/10/cyber-resilience-incident-management/documents/cyber-incident-response-denial-of-service-playbook/cyber-incident-response-denial-of-service-playbook/govscot%3Adocument/Cyber%2BCapability%2BToolkit%2B-%2BCyber%2BIncident%2BResponse%2B-%2BDenial%2Bof%2BService%2BPlaybook%2Bv2.3.pdf)
* [Imperva DDoS Response Playbook](https://www.cbronline.com/wp-content/uploads/dlm_uploads/2018/04/Playbook-DDoS-Response-Playbook-new-V2.pdf)


