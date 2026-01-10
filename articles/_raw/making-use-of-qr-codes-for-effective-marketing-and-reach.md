---
title: How to Use QR Codes for Effective Marketing and Outreach
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-27T21:53:05.000Z'
originalURL: https://freecodecamp.org/news/making-use-of-qr-codes-for-effective-marketing-and-reach
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screenshot_1.jpg
tags:
- name: industry 4.0
  slug: industry-4-0
- name: business strategy
  slug: business-strategy
- name: '#content marketing'
  slug: content-marketing
- name: Digital Transformation
  slug: digital-transformation
- name: qr code
  slug: qr-code
seo_title: null
seo_desc: 'By Black Raven

  Efficient means doing things right. Effective is about doing the right things.

  I am an advocate for efficiency and effectiveness. There must be a more efficient
  way to share contact details other than manually typing details into my mo...'
---

By Black Raven

**Efficient** means doing things right. **Effective** is about doing the right things.

I am an advocate for efficiency and effectiveness. There must be a more efficient way to share contact details other than manually typing details into my mobile phone when I meet a new business contact.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-187.png align="left")

*Name cards with QR Code*

# Add a new contact on your mobile phone by scanning a QR Code

When Google launched the **Google Contacts** app in 2017, users could share contact information with QR codes. To add a new contact, simply scan a person's QR code to save their contact information on your phone.

I personally think that such an efficient way to save contact details should be implemented on business cards and marketing brochures.

The trend did not seem to take off, maybe because people did not know how to create the QR Codes in the first place.

## Create a list of customized contacts QR Codes

I made use of a **Google Sheets** template to generate the contact QR codes.

Open the template ([template link here](https://docs.google.com/spreadsheets/d/1jJdBgqQvYuQM-Bo0An2W7CUS5c4EQKjyRkHYZln3Wr0/edit?usp=sharing)) in another tab. Then click on “File -&gt; Make a copy” to save it to your own "My Drive" (Google Drive account).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_grwBMqbnT87naQki630AtA.png align="left")

*Google Sheets template to generate the contact QR codes*

*Note that this Google Sheets template seems to only work on desktops, not on mobile phones.*

You can use this template by updating **First Name**, **Last Name**, **Mobile Phone** number and **Email address**. The contact QR Code will be generated in the next column based on these 4 fields.

```excel
=image(“https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=BEGIN:VCARD%0AN:" & A3 & “%20” & B3 & “%0ATEL;CELL:” & C3 & “%0AEMAIL:” & D3 & “%0AEND:VCARD”)
```

Then another person can scan the generated QR code to add the contact details to their phone.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_fZzgOk0-Mc-zTzc3lCuGzA.jpeg align="left")

*New iOS and Android versions are equipped with QR Code scanner in camera mode*

After scanning, simply click on “Save” to add the information to Contacts.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_tkEkTu94w7CBhVhMat1aCA.jpeg align="left")

*Scan QR code and save contact*

This contact list QR Code template will be useful when you meet new people in a team or at a tradeshow and want to gather everyone’s contact details.

## To create a single customized contacts QR Code

Go to [QR Code Generator](https://www.qr-code-generator.com/), and select ‘vCard’ where you can customize various fields. Remember to test it out, as some fields do not allow special characters like "," or "@".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_q5Yxh3Yrq_XSweBRBOLKtg.png align="left")

[*https://www.qr-code-generator.com/*](https://www.qr-code-generator.com/)

You can also add this QR code to your business cards and marketing brochures. Customers and business people can then easily scan and save your contact details to their mobile phones.

# Go to a website by scanning a QR Code

Newer versions of iPhone and Android phones are equipped with QR code scanning in the camera app. Simply turn on the camera and hover over the QR Code to scan it. Then you can click the popup to go to the web address URL embedded.

For example, try to scan this QR code:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_8Rk_gKSDJVfafeWiullsWw.jpeg align="left")

*Web URL embedded* [*https://www.qrcode-monkey.com*](https://www.qrcode-monkey.com)

## To create your own customized QR Codes

I usually go to [QR Code Monkey](https://www.qrcode-monkey.com/) to create a customized QR codes. It is friendly and **free to use**, and there are more options if you want to:

* add a logo image in the middle (this can be your **company logo**!)
    
* set a color (to follow your **corporate identity**)
    
* use some other other customized design
    

So now you can easily create marketing materials with QR code of your company's website.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_-_nSVy6PxwJ9XKzU1PZ9iA.png align="left")

*Marketing materials with QR codes*

---

## QR Codes for name cards and marketing brochures

I hope the tips above are useful for getting things done more efficiently and effectively. All the best to your marketing and outreach efforts!

Thank you for reading!
