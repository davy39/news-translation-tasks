---
title: How Does Kerberos Work? The Authentication Protocol Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-19T14:34:59.000Z'
originalURL: https://freecodecamp.org/news/how-does-kerberos-work-authentication-protocol
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/cerberus.jpg
tags:
- name: Application Security
  slug: application-security
- name: authentication
  slug: authentication
- name: cybersecurity
  slug: cybersecurity
seo_title: null
seo_desc: "By Aaron Katz\nIn this article, we will learn what Kerberos is, how it\
  \ works, and the various pros and cons of using this authentication protocol.  \n\
  What is Kerberos?\nHave you ever wondered what happens when you type in your username\
  \ and password at w..."
---

By Aaron Katz

In this article, we will learn what Kerberos is, how it works, and the various pros and cons of using this authentication protocol.  

## What is Kerberos?

Have you ever wondered what happens when you type in your username and password at work, and magically have access to file servers, email servers, and other resources? Odds are, you are using Kerberos! 

Kerberos was designed to protect your credentials from hackers by keeping passwords off of insecure networks, even when verifying user identities.

Kerberos, at its simplest, is an authentication protocol for client/server applications. It's designed to provide secure authentication over an insecure network. 

The protocol was initially developed by MIT in the 1980s and was named after the mythical three-headed dog who guarded the underworld, Cerberus. It was later refined by Microsoft for inclusion in Windows 2000 to replace [NTLM](https://docs.microsoft.com/en-us/windows/win32/secauthn/microsoft-ntlm) – and the protocol remains [Open Source](https://www.kerberos.org/about/FAQ.html).

If you need to quickly sum up Kerberos vs NTLM in an interview, the most concise description is as follows:

> "While NTLM uses a three way handshake between the client and server, where credentials are sent between the systems, Kerberos avoids sending credentials across the network."

## Authentication with Kerberos

Authentication via Kerberos requires the use of a **Key Distribution Center (KDC)**. This is typically a service running on all Domain Controllers (DCs) as part of Active Directory Domain Services (AD DS). It contains the following components:

1. **Authentication service (AS)**: Authenticates users when they initially attempt to access a service
2. **Ticket granting service (TGS)**: Connects a user with the service server (for example, a file server) based on information stored in the database
3. **Kerberos database**: Where the IDs and passwords are stored, often an LDAP server or the Security Account Manager (SAM) database in an Active Directory environment.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-193.png)
_Kerberos authentication workflow_

### Kerberos authentication process explained

When a user requests access to a service through the authentication service, they enter their username and password locally, and send the following information:

1. Security Identifier (SID)
2. Name of the requested service (for example, example.cool.hat)
3. User's IP address
4. Desired lifetime of the Ticket granting ticket (TGT). The default is 10 hours and can be changed via Group Policy

Authentication service issues a ticket granting ticket (TGT) if the user exists in the database. The first message sent back to the user contains:

1. Security identifier (SID)
2. TGS ID
3. Timestamp
4. User's IP address
5. TGT lifetime
6. TGT
7. Session key

After this message, another message will be sent containing:

1. TGS ID
2. Timestamp
3. Session key

The user sends the TGT to the TGS along with the Kerberos ID of the requested services. Another message is sent containing the "Authenticator", which is composed of the User ID and timestamp, encrypted with the user's session key.

The TGS will respond to the user with two messages if it finds the user's information within the Kerberos database. The first message will contain the following information, encrypted with the server's secret service key:

1. Service ticket
2. User's ID
3. User's IP address
4. Validity period
5. Service session key

A second message, encrypted with the user's session key (for example a locked box within a locked box, where the user can only unlock the first box), will contain the service session key.

The user sends the service ticket to the requested service along with the service request in two messages. The first message will be the first message from the previous step (encrypted with the server's secret service key). The second message will contain a new Authenticator with an updated timestamp, encrypted with the user's session key.

The service server decrypts the ticket using its own secret key to retrieve the user's session key, which is used to decrypt the authenticator. If the user's ID from previous messages matches, it will send a message encrypted with the user's session key to the user with the timestamp found in the new authenticator to confirm the service's identity.

### Kerberos encryption

When creating a new account on an Active Directory Domain Controller, you get a username and password. 

The Kerberos client then adds a string known as a salt - a unique string used to improve the randomness of a credential - along with the Kerberos version number. In most configurations, the salt is the user's username. It then runs these two values through a string2Key function which will return the shared secret.

On a workstation, the user will request access to a service (such as logging in to the machine) by providing their username and password. The local Kerberos client will perform the same steps as the DC to arrive at a shared secret. If this secret matches the secret stored on the DC, the user can log in.

## Benefits of Kerberos

Kerberos provides several benefits over previous authentication technologies, such as:

* Plaintext passwords are never sent to the KDC
* Simple transparency and auditing of all events
* Verification against the KDC happens only once for the lifetime of the ticket
* Single sign-on is one of the biggest direct benefits of Kerberos, allowing a user to enter their credentials once, and continue to renew their ticket without intervention
* Support for Multifactor Authentication (MFA)
* Both ends of the communication chain must be authenticated

## Kerberos Security Vulnerabilities 

Now that we know how Kerberos works, it's important to understand the potential vulnerabilities inherent in its implementation, especially in Microsoft's proprietary extension to Kerberos. 

You can detect the majority of these attacks using native tools to monitor logs, but it is important to know what to look for. This section will provide a high level overview of the various attacks you'll find against Kerberos systems.

### Golden Ticket Attack

A golden ticket is a forged Kerberos key distribution center. You can create usable Kerberos tickets for accounts that do not exist in the Active Directory. 

To obtain a Golden ticket, an attacker needs domain/local administrator access on Active Directory forest or domain – and once the ticket is created, it is good for 10 years by default!

If you believe that someone created an unauthorized golden ticket, you would need to reset the Kerberos service account, krbtgt. While this isn't difficult, there are several critical steps to the process. 

Because Active Directory stores the old and current passwords for all accounts, you must reset the krbtgt account twice. But the second reset should occur **only after waiting the maximum user ticket lifetime** after the first password reset. Microsoft provides a handy script to assist with this [here](https://gallery.technet.microsoft.com/Reset-the-krbtgt-account-581a9e51).

### Silver Ticket Attack

A silver ticket is similar to a Golden Ticket, but does not have the broad administrative privileges of the golden ticket. 

An attacker would typically only gain access to a single service on an application, and an attacker must have compromised legitimate user credentials from a computer's SAM or local service account. 

What makes these attacks very difficult to detect is that forging a silver ticket (for example using the service account password hash) does not require any communication with a DC.

### Backdoor skeleton key malware attack

In a backdoor skeleton key malware attack, the attacker typically has compromised the Domain Controller and executed a successful Golden Ticket attack. 

The malware injects into LSASS a master password that would work against any account in the domain. When the account authenticates, the malware will check the injected master password hash, and if it's a match will authenticate the user, regardless of the user's true password. Legitimate users will still be able to log in with their normal credentials.

### Pass the hash attack

This is a technique where an attacker obtains a user's NTLM password hash, and subsequently passes the hash through for NTLM authentication purposes. 

This works because systems do not actually validate a user's password, but rather the hash of the password. This attack only works against interactive logons using NTLM authentication.

### Pass the ticket

In this attack, the threat actor creates a fake session key by forging a fake TGT. The attacker will present this to the service as a valid credential. 

In order to execute this attack, the attacker must obtain access to the session key. To perform this attack, an attacker would obtain Kerberos tickets from the memory of the LSASS process, and then inject the stolen TGT into their own session, which will let them adopt the identity and privileges of the stolen TGT.

### Overpass the hash

A combination of Pass the hash and Pass the ticket, an attacker uses a compromised hash to obtain a Kerberos ticket that they can use to access a resource. 

Often useful if you need Kerberos authentication if NTLM is disabled to reach your target but only have a compromised hash.

### Kerberoasting

When a domain account is configured to run a service (for example, Internet Information Systems, MSSQL, and so on.), a Service Principal Name is used to associate the service with a login account. 

If a user wants to access the resource, they receive a Kerberos ticket signed with the NTLM password hash of the account running the service. Hackers can then crack this hash offline and use it to gain access. 

_Any user on the domain with a valid TGT can request a TGS for any service with an SPN_ - no fancy credentials or access needed! Note that _there is no fix or patch_ beyond ensuring that the password for the service accounts are sufficiently complex.

To detect this attack, your _only_ native option is to monitor for event ID 4769, and look for a Ticket Encryption Type of 0x17 - user to user krb_tgt_reply. You can find more information on detecting Kerberoast attacks [here](https://www.trustedsec.com/blog/art_of_kerberoast/).

### Replay attack

A replay attack occurs if an attacker steals the packet sent from the user to the service, which they can then use to gain access to the service without knowing the user's credentials. 

This is generally low risk and is mitigated by the system checking the timestamp of the packet - any timestamp earlier or the same as a previous packet is rejected, as well as any timestamp out of sync with the server time by over 5 minutes.

## How to Defend Against Attacks on Kerberos

Now that we are well and scared by the attacks we just discussed, let's dive into some techniques to defend against attacks on our Kerberos infrastructure.

### Logging and monitoring

Attackers will often use a fake or blank account/domain name when issuing a Golden ticket, as these don't need to be real when issuing a valid ticket. 

You can search through the DC logs for event id **4769** - service ticket request, for users or domains that don't exist. For Silver ticket attacks, you would want to search the event id **4769** for any service ticket requests using RC4 encryption, type set to 0x17.

### Patch!

Make sure your systems are up to date. Not only will this help prevent many exploitation tools from working, but specifically patching [CVE-2014-6324](https://www.varonis.com/blog/microsoft-fixes-kerberos-silver-ticket-vulnerability/) will resolve a vulnerability allowing a Silver ticket to become a Domain administrator.

### Set admin and service accounts to "Sensitive and cannot be delegated"

This setting will prevent attackers from delegating their hacked accounts to other services or computers, restricting their ability to move laterally in your environment.

### Do not add computer accounts to administrator groups

A computer account that is a member of admin groups, such as "AD Backups", can be exploited to obtain Silver tickets and allow attackers to maintain persistence in Active Directory by adding new rights to the account.

### Run Local Security Authority Subsystem Service (LSASS) in protected mode

LSASS is responsible for providing the single sign-on service for users, and hosts numerous plugins such as NTLM authentication and Kerberos. 

Credentials are presented to each of these plugins, producing a one-way hash and tickets in the memory space of LSASS, which remains for the duration of the user's session.

When run as a [protected process](https://itm4n.github.io/lsass-runasppl/), LSASS can only be accessed by digitally signed binaries (of which most attack tools are not, though there are a few bypass methods available).

This can be set by opening the Registry Editor as an administrator, and adding a DWORD with the name **RunAsPPL** with a value of **1** at _HKLM\SYSTEM\CurrentControlSet\Control\LSA_ and restarting the system.

**IMPORTANT:** If you're using a _third party authentication module_, it must meet requirements listed here: [Configuring Additional LSA Protection | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection#protected-process-requirements-for-plug-ins-or-drivers). 

If you're using _Secure Boot/UEFI_, you can't disable the setting by changing the registry key, and you must follow the specific instructions outlined by Microsoft here: [Configuring Additional LSA Protection | Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection#to-disable-lsa-protection).

### Enforce Privileged Attribute Certificate (PAC) authentication for TGS

The Privileged Attribute Certificate contains information about a user's privileges. A forged PAC can instruct the TGS to grant additional privileges to a user that they are not entitled to - and because in Microsoft's implementation the krbtgt account is disabled and not used, the key doesn't change. 

When enabled, PAC Validation ensures that the PAC of a user authentication to a system is checked against Active Directory for validity. You can enable this by opening the Registry Editor (**regedit.exe**) as an Administrator, and setting the _HKLM\System\CurrentControlSet\Control\LSAKerberosParameters_ key to **1**.

### Principle of least privilege

Ensure that user accounts throughout the environment only have access to the services, groups, and resources they need to perform their function. This reduces the attack surface and can help prevent further compromise in the event an account is compromised.

### Use strong, unique passwords for administrative, local, and service accounts

Administrative accounts should ideally have passwords longer than 14 characters. However, SPN accounts should ideally have longer passwords to improve security - ideally 25 characters or greater.  

Host-based SPNs have secure, 128 character passwords changed every 30 days, but by default, user account SPNs often never expire, and have reused, weak passwords, as this makes it simpler for administration.

### Enable Windows Defender Credential Guard (except on domain controllers)

Windows Defender Credential Guard prevents attacks such as Pass the hash or Pass the ticket by protecting NTLM hashes, TGTs, and other credentials. It does this by leveraging virtualization-based security and the "isolated LSA" process to store and protect secrets. 

Only trusted, privileged applications and process will be able to access this information. You can find more information here: [Windows 10 Device Guard and Credential Guard Demystified - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/iis-support-blog/windows-10-device-guard-and-credential-guard-demystified/ba-p/376419).

### Disable RC4 encryption

RC4-HMAC is a known insecure encryption suite and you should disable it if possible.

* Enable AES support in domain trusts where trusts exist
* Enforce AES256 for Azure AD SSO account if applicable
* Roll over Kerberos Decryption Key
* Disable RC4-HMAC via Group Policy

**IMPORTANT:** There are numerous "gotchas" when disabling RC4 due to how Windows authenticates and the numerous locations where this setting will need to be modified.  Make sure to research and plan _thoroughly_ before applying. 

Here are some useful documents to help you out:

* [Tough Questions Answered: Can I disable RC4 Etype for Kerberos on Windows 10 ?](https://techcommunity.microsoft.com/t5/itops-talk-blog/tough-questions-answered-can-i-disable-rc4-etype-for-kerberos-on/ba-p/382718)
* [Lessons in Disabling RC4 in Active Directory](https://syfuhs.net/lessons-in-disabling-rc4-in-active-directory)

## Conclusion

See, that wasn't so bad - Kerberos can be fun! Kerberos is often one of the least thought about, but most critical components of any enterprise network. And it is imperative that defenders understand how this protocol works, and the various attacks and defenses available. Now go forth and conquer!

## Further reading

* [Kerberos, Active Directory’s Secret Decoder Ring – Active Directory Security](https://adsecurity.org/?p=227)
* [The Kerberos Protocol Explained | Identity & Access Management](https://iam.uconn.edu/the-kerberos-protocol-explained/)
* [Kerberos Authentication 101: Understanding the Essentials of the Kerberos Security Protocol -- Redmondmag.com](https://redmondmag.com/articles/2012/02/01/understanding-the-essentials-of-the-kerberos-protocol.aspx#:~:text=The%20SALT%20string%20is%20the,secret%20key%20on%20the%20client.&text=The%20user%20and%20the%20Authentication,communicate%20using%20the%20shared%20secret.)


