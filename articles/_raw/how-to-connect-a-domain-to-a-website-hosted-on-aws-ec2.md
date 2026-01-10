---
title: How to Connect a Domain Name to a Website Hosted on AWS EC2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-02-19T23:51:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-connect-a-domain-to-a-website-hosted-on-aws-ec2
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/my-hashnode-technical-blog-images.jpg
tags:
- name: AWS
  slug: aws
- name: ec2
  slug: ec2
seo_title: null
seo_desc: 'By Obed Ehoneah

  You may want to host your website on a virtual private server or a virtual machine
  like AWS EC2. But it can be a challenge to connect a domain name that you purchased
  from providers like Namecheap or Godaddy.

  But if you know the steps...'
---

By Obed Ehoneah

You may want to host your website on a virtual private server or a virtual machine like AWS EC2. But it can be a challenge to connect a domain name that you purchased from providers like Namecheap or Godaddy.

But if you know the steps to follow, this doesn't have to be difficult.

In this post, I'll break the whole process of connecting a domain name to a website hosted on EC2 down. I'll show you how to do it practically with screenshots guiding you through every step. I'll be using a Namecheap domain in this example.

There are 4 major steps that you'll need to follow, and it shouldn't be too tricky if you follow the discussion in this tutorial. Here they are:

* Step1: [Set up your website on EC2](#step-1-how-to-set-up-your-website-on-ec2#step-1-how-to-set-up-your-website-on-ec2)
* Step 2: [Set up Route 53 for DNS management](#heading-step-2-how-to-set-up-route-53-for-dns-management)
* Step 3: [Update nameservers with your domain provider](#heading-step-3-update-nameservers-with-your-domain-provider)
* Step 4: [Wait for propagation](#wait-for-propagation)

Let's get started.

## Step 1: How to Set Up Your Website on EC2

First, visit [https://aws.amazon.com/console/](https://aws.amazon.com/console/). Click on the sign in button at the top right corner or the Log back in button in the middle.

![Image](https://lh7-us.googleusercontent.com/1P8t02v71WBoFie3Noxs-9-32Ckege-I36ZM4vpfsXqBiSrJTeOgvOA2F9FCTPBTFo4fkWUhwxCDIXAiB2ZTyPgRXqJpyYOGIv7EhV2AS01LnsMilBBCgvgYwKxVauR70bKfIQ3FVFD7JrrPwW_9A94)
_AWS Management Console_

  
Create an account if you don’t already have one. Otherwise sign in with your credentials.

![Image](https://lh7-us.googleusercontent.com/_4dJQGRVfyRepII17I6GGUmpHiEJ_YShtzztq9SBMPS8GIqk79HdS_678Cue6g7Ws06LlV28ity_Nqjwk8QJkF3SZOUgSdImmdTbOhfvpUWXZ4foziwGLkwtL1NJdTfiHnje9k9GwugtjxGRP2b14fU)
_User Login Page_

After logging in, you will be redirected to the main dashboard.

![Image](https://lh7-us.googleusercontent.com/1ten0edaOEW9fyi94wZJDYLAO4iwjMOxpR9iVX9Q-52fnDO8_W2zq85Jm9y70K0Nm32twNDmEFmFjQ1FYUvkW7iqcfHpaeBCRSZqYWSIYouvkmgvScm4p15zeH6r6El_6S23mW_GBTCd-OQ3DC-FUs4)
_User Dashboard_

  
In the search bar at the very top, you can search for EC2 and click on the first option under Services.

![Image](https://lh7-us.googleusercontent.com/wVnUvVADZoMmKBmWMTGjA79mBeSni4Ie7U6IuvatJNeglH1ss4-JPapyqWUNHuCTEmxHm4_Wl12jhL4Y7DbSmhO_HqFhLCRxxqfT9N_2K3o_0Sp5t_5xoAagztYd5ZXIoTX_qCZTTh07VA99E1pQRsE)
_Searching for EC2_

This will then open the EC2 dashboard that gives you a summary of all the EC2 resources that you are using. If you are not using any of them, then you are likely to find that the value for each will be zero.

![Image](https://lh7-us.googleusercontent.com/G7PsvT8tE97xb4pp75H1Kmta3Jdv_A8xIWtAROQXz7vNNYQ2O6g8VliULPxLQmcGwOxf_BXcwE_QBrKtLVqdlM-8j5BSkJUzfGiI6NDBtCaAsyMRwxC7Oj_HEDkNt0_CcgEL-yOqgfPws1ZMs4PAutQ)
_EC2 Dashboard_

### Launching an EC2 instance

Click on the Launch Instance button.

On the "Launch an instance" page, you will select the specifications for the virtual machine intended to host your website or web application. Initially, assign a name to your machine for easy identification..

For the sake of this example, I used the name "FC Web Server".

![Image](https://lh7-us.googleusercontent.com/PGh6o3yysjEl5xkqof7IvhE7Dg0eU6SWO9fmRaRY0sEUJoWLPiXcunxQQ4MI1Z_k1oaGbymInJLxTJv9l02pcmrfxi_YPjRZdPnW72PojjOTwqtihrtFVUwK5FZw-y_d1UyrdcjOafbr_KlIlKQkN_4)
_Naming your EC2 Instance_

Choose the Amazon Machine Image (AMI) which represents the specific operating system and applications you want to have by default on your virtual machine when you boot it.

For the sake of this example, I selected Ubuntu, and I'm using the Free tier eligible Ubuntu Server 22.04 LTS as the AMI. I left the architecture at 64-bit (x86).

![Image](https://lh7-us.googleusercontent.com/T2FD0Pwnrkni6FWDuK1P_NFgPVmoV63I9QRFFLPt6HijKo4MuBGZr8Kua4ELs8p9ThtDYOF4juugnrZOYi3G9Pq4u1GkF-V8ZJjUq3rj9zg1pCyAwJj-0L3-vi-CFs8G718iZlVFPgSzGsjOPY7G61Y)
_Choosing an Amazon Machine Image_

For the instance type, you can also stick with the Free tier eligible t2.micro – but if your app or website requires more resources, then you'll have to choose the most appropriate instance based on the number of vCPU and memory required.

![Image](https://lh7-us.googleusercontent.com/L-syY4yUQNlpzBn_3EchnBFOPzCcVs_6yOgtdjljp05Gn6cTr0XLONAiDY_nNuILJq4tV2y5yug6IJdEagCu599FanEYkrV9QrKwbwpxqAD0EOGpZJcDQob1A99y3E977vV7BaY1m9oBxLyfA79YJ5A)
_Choosing the instance type_

To securely connect to your virtual machine, you will need an SSH key pair. Go ahead and click on the Create new key pair link under the Key pair section if you don’t already have an existing key pair that you can use.

![Image](https://lh7-us.googleusercontent.com/35slbh7seL4zxMwSnR4ZrZPddFJ0yAOxvJIPatukKXAb0wIbuJ9wfOWRdbGHSFJRaMUsSiCV0-d-NiZqMe0gQVppGCU4WbMyN33XcrOvnwmXtf1ZEeMYJhyAAugpcawQ7jz2zuwiX6Yiyy7_xwOLOH0)
_Creating a key pair_

Give your key pair a name that you can easily identify. Set the key pair type to RSA and the private key file format to .pem. You can also use .ppk if you are in a windows environment and know how to use PuTTY. 

Click the Create key pair button. After clicking it, the file will automatically be downloaded. Make sure you keep this file in a secured place.

Move on to the Network settings. You need to set up a firewall that controls the various protocols through which your website or web app can be accessed. For the sake of this example, you can choose Create security group and allow SSH, HTTPS, and HTTP. 

You can leave the IP address at Anywhere 0.0.0.0/0.

![Image](https://lh7-us.googleusercontent.com/pmqY3ZoEQF7G0EcQPi49Ik6LjrwM3AkK3k2pgXbC4YpEn61ISeXjZID3l2cIK2cyNMrRKSTksLtRNeOZQ4zRyTAyKHZcxattdNOgY5bLunSvKzMJI8gaDovxxYKz6yKc-LXPPwVrG3xtc_SxjhLXMoY)
_Network settings for your instance_

Finally, you need to configure the storage options. You can also go with the default 8GiB gp2. You can ignore the additional details and click on the Launch instance button.

![Image](https://lh7-us.googleusercontent.com/og9GB9frMs-IFbrDxUhwS5FXefMLDISspiJCMhskzN0nX9JVabNKbo-VWw-HQ1q9Tq7_ONdQRGAzbttG_nbEuWihA2mjVX-BZNFOL32pEyzz0JNUR6ESr3-M8TWwckI7IfslpirqkXKULWg06Ag7ssI)
_Storage configuration for your instance_

After the instance has successfully be launched, you will get a success message.

![Image](https://lh7-us.googleusercontent.com/qNgmnZI1S2YUOoSc6Pv92rlo40HDxFquPmXOP_1Qdqx103KxBfsSZyzw1Q6xDpy2J7q_3cIdXHpsGsa8B3NEeTYAaImUk31nf4M5DmgXeQouwYQKwDzo9YYWD9akS0tfv7xPHhbFeANXAfR4AXe041I)
_Success message after launching instance_

### Connecting to an EC2 instance

You've now created your virtual machine – so you need to connect to it and turn it on. You can do this by clicking on the Connect to instance. You can also click on  View all instances to see the instance that you created.

If you click on view all instances, it will take you to this page where you see your instance (see below). If you have only one, then you will see something like what is shown below. But if you have other instances, then you will see all of the instances created in that same AWS region. 

![Image](https://lh7-us.googleusercontent.com/kKXsADE-G5yS_Z0EKK6KQx7QviZnJrrhAyorzGJC6DPPH53aXcVWmxW_AjvpfwrAtYNzIS6JF3uKySS2R3ehgQGxKmCFL-lGAqtCSsA9sB95HIr15XP3gVCb9hNcU9ca8nZX_ocgmNGpWhCSt_a5LfE)
_List of EC2 instances launched_

Select the specific instance that you just created and click the Actions dropdown at the top right side. You can then click on Connect from the dropdown menu.

![Image](https://lh7-us.googleusercontent.com/HlYh7FNpoUi-BvMCg_J9hANAg9w0HWoISqCquGaJ5agnv5a6fpkG29qqpPsh8D47ntjd35TZY5e6FyQF2SxzQ4VmsBoY2uFigDIXsl-zy7xWAP6d-g92s-uDyqk1NITQ3c6hnax5hWx87dOS-IZ6FUQ)
_Connecting to the selected instance_

The third way that you could have used to reach the connect to instance page is to click on the Instance ID from the list of instances. It takes you to the instance page with details about your selected instance. You will then find a Connect button at the top right side.

![Image](https://lh7-us.googleusercontent.com/TjXw51BB3V9HLxnXsKszZUyIRNzAwa_GvobWLHxPzYf0QnrzCLofCa8TGVspGR5NpfDniXSiiYkEtxpmsAkHHlz8XXVdqZhd_Xn5H3gaVkECfHCFAWmbA23Ni8-GUTrYzwk0tGKfgW28xJt9SFckaOM)
_Details about the selected instance_

On the **Connect to instance** page, you are presented with several options to connect to your instance. For the sake of this example, you can use EC2 Instance Connect. This option will allow you to connect to your virtual machine through the browser. You can stick with the default values and click the Connect button.

![Image](https://lh7-us.googleusercontent.com/SjIELpNqBcMXahNHK_dJx3Jhky8CdXxr0kbdhOpWqQZ-nM3BLEQ9A8uGv4Uh-alBNA5aYWDuXOGEw_MS48VM3InAQQJquHHvq2yl7FYlk98GDy0QDd0a9LFaGENVUMM9Sucz7Rc1ti6LjeZuKPTsLGw)
_Options to connect to the instance_

This opens up a terminal in the browser. This is your virtual machine. Remember that you installed Ubuntu so now you have access to an Ubuntu machine with all the specifications you selected.

![Image](https://lh7-us.googleusercontent.com/KdV49cJVMg2EEVOdVkhZNWbG9qtA2u0H3OahaZDCnkoTcgjnZBuI4ZWY_GQKG1o_fbUkocBljYl8RB2LbVG969eq6az-R8csZEXAIxo74mv-1frHdrE_pAwwwHsa4CCHz1eM2rHynGX6NeFAtgineEg)
_Ubuntu terminal opened in the browser_

It is now time for you to install NGINX. Follow the steps below to install NGINX on your instance.

### Update your package list

Use this command to update your package lists:

`sudo apt update`

![Image](https://lh7-us.googleusercontent.com/cnk6SxfwNaz-dsEUd1C3AcaM1Ueh-GGTRCRTEoRNDYKIs_Gp2bU1JwsBwLzd05mwGLrDjVscZuWq2mu-6CU0Ch5Tx7TQ0rraMc3_BVUIGtBH8jjsQcH7FlkYR5vRBQ33jvUVc6bIIQ5RHAkY24bHyQg)
_Updating the package list_

### Install NGINX

Use this command to install NGINX:

`sudo apt install nginx -y`

![Image](https://lh7-us.googleusercontent.com/5xyqlguhGA2pCjltDJXeLFKNsm-HaKTlDab6QjmlucpBWRLGdEbjoFg5_5FJ3xV73s047_ycOX59A7Yphq4xyKBZmcv1NfWySx3G6nqi6a8e2XgQutrJBWazwR4UlYi9CA49c-8TL2-7E7PVRml6h38)
_Installing NGINX_

Once the installation is done, you can access the default page for NGINX by entering the public IP address of your instance in the address bar of your browser. 

To find the public IP, you can check the bottom of your terminal or go to the instance page and look for Public IPv4 address.

![Image](https://lh7-us.googleusercontent.com/hYkF9Fvl2yc-W6kR5XWQWGTnEINJbEdj3k9_SQZUGcdb_MQ3MgQ6fKOh791HgxEdDXC28g2Mazk04n-JsM1xwT2TttF5u_vZQqp5aUD963ZzKelbImsPqW_1ePkI0FNFH-mPT0QC3CWhzgYxQZxLmos)
_Public IP address of the instance from below the terminal_

![Image](https://lh7-us.googleusercontent.com/86hZhXn99AFBdk-gZ6fqa-yLLzJqqAASd43rL0zM-kD0ZflQJ_65yP4s4bSKcxYFvaPiLThaX948B8Q12iQrmeQw8rwkbCwrhP-RdWdU2ZOhUz1OVTTHr7BbEYFxDtX_Obpfj7rqHhzAjgqntzW0s4g)
_Public IP address of the instance from the details page_

You should get the default page open in your browser like shown below:

![Image](https://lh7-us.googleusercontent.com/JZPEFIWMHIUAWSURn80p-AEYsWukl-W5Um2YZ9ce5d4Ox9H8UQozMnYCltaLTBfbzl_tvmZ3Fn6tJEO_VOv-_1ne7F8ElYIUexdg9I7JgySqSmI2yo0b2fmT0zJYxHArDYxY39LTsmDrRbmG6M5ZKsQ)
_Default page for NGINX web server_

NB: You may have to refresh the page for it to work.

For the next set of steps to set up your website or web app, it will depend on the programming language or framework that you used. But since this tutorial is focused on connecting a domain name to your EC2, you can proceed with the next steps for connecting the domain.

![Image](https://lh7-us.googleusercontent.com/m9xoyqffR1ExdcIcXO7Ir5owVxyZgVP3z1iPaG_ISKUyIn6nwlCP_sJH-Yn6y64ZytEQkS0hLMXTirDdwHzAHnUrr0j8H4vj8v-2i1KATd7cDf7r8d47siBIEET12RKg68Q183mrw3XmXFnQG0l4gxE)
_Default page of NGINX_

Working from this image, let’s now connect our domain name to this website. As you can see in the image above, I am accessing it with the public IP address of the EC2 instance.

To connect the website with a domain name simply means to replace its IP address with a more memorable name. In our case, I will be replacing it with the domain name `krachy.com`.

## Step 2: How to Set Up Route 53 for DNS Management

AWS provides a service called Route 53 that you can use for DNS (Domain Name Service) management. So now, we need to set up this service to manage the domain that you purchased. 

I have my domain with Namecheap, but the process will be similar for almost every other domain retailing company.

First, you'll need to create a [hosted zone](https://aws.amazon.com/route53/faqs/#:~:text=A%20hosted%20zone%20is%20an,domain%20name%20as%20a%20suffix.) in Route 53.

![Image](https://lh7-us.googleusercontent.com/XVis1IAhzZ3CdJiDBOu9NXc66ER63DSDgfuWLL-zqiJStnsjEa0COfK-EtuKYnpjBr6gOouLcAYDQlhcrRX1YNIFbNk4qyzYIuLHqJ2Y3f1zo4Rz7OI0lv-MI2Z6g_AMvgoCcjY-5zNYernNhhCoUv0)
_Amazon Route 53_

### Creating a hosted zone in Route53

To do that, click on the orange `Get started` button. It takes you to the next page, as shown below.

![Image](https://lh7-us.googleusercontent.com/2ZJ658N8zV3L9UjxrRDqmAUSF-6se1J6yc0qBRO_tsATMijkY3k7cWc5D2TFIiC_PHLOEvukyQnVo5vJi7mQQq19y1bNJCeeYsvBQ_Of5RrfL7tjRfWYOfaPzRtjKiEKnENyU48ZxQeXr63R4IY9mU4)
_Getting started options for Route 53_

Choose `Create hosted zones` and click the `Get started` button. Go ahead and fill out the details on the next page.

![Image](https://lh7-us.googleusercontent.com/ibfwFdt41BH4rgMKJ44-4qmcF-xUTePMD6WL7Q341AzcBM6KWUtrwvGAavwuZmEWNeImMVuPLQfRsfkaMKjiDSpfA1r5IRQEXo1crcbZL33vpNCH8hrbYetMUCuFYsTOXZrU18fe-H3NR_BCNdpdE3g)
_Hosted zone configuration_

![Image](https://lh7-us.googleusercontent.com/-UmPq2sd9RuiNkRxwC545W0iXzSnofRok4d3XVJ4yMoxP4j7jM_WQp2FzUeptBEmlFknPgeB4DY3EjDUtlu-dGgwfLK-bCyCtHv4DyUxYHXWOYKv9V1M3Z-oyPrcJDKXULWPxFi7WTmkjWUsXi8oTwY)
_Providing details for hosted zone_

Provide the domain name that you want to connect to the EC2 instance and then give it a description that will make it easier for you to distinguish this hosted zone from any others you may have. Choose `Public hosted zone` since you want your website to be accessible to the public.

Click the orange `Create hosted zone` button.

![Image](https://lh7-us.googleusercontent.com/A4_iFzOVyOTal9QBXCCVAaI56OaNs-Z9yQfZKqDWzSbMj1sE953_z3kUi9v_L8hq25FBjgt-MolYw0pANYVsawS4oek9KkJpJikW6XWmDsaxEr2-XaPi_Um2Zl58MdNrsuw5CFKvFolNSxieIlduwnE)
_Success message for the hosted zone_

You'll get a green success message showing that you have successfully created the hosted zone. 

### Adding records to the created Hosted Zone

From the screenshot above, you can see that Route 53 automatically created two records for us: the NS (Name Server) and the SOA (Start of Authority) records. The NS record is what you will need for pointing your domain to this service. But before you grab those, you have a couple of things to do here.

Because our website is being hosted on an EC2 instance which can be accessed through its public IP address, you need to create an **A record** for it. Also just so you ensure that people who try accessing your website with the `www` subdomain are still able to access it, you will also need to add another record with an **alias** for it. 

To do that, start by clicking the orange `Create record` button, as you can see in the screenshot below:

![Image](https://lh7-us.googleusercontent.com/0Sb2ip2tg_IvOAaumH1KB4V8d6XPFtBk9s1lBJ1lyTXHnia3kCe5VicjCqd-D1VX14fpGSoJp0GlskDDxtgOb8ztgFrGXJP_cHQgomH114x85tXrxQEC177Yn8pUsz3XghjBPc_OTRoUiBcuDA-500I)
_Adding an A record_

For the **A record**, don't put anything in the `subdomain` input box. Under Record type, make sure `A – Routes traffic to an IPv4 address and some AWS resources` is selected. Then paste or type the public IP of your EC2 instance in the textarea for Value. 

You can leave everything as default (NB: Check to ensure that the Routing policy is Simple routing).

To get the IP address, visit the instance that you are using and look for the Public IPv4 address and copy that.

![Image](https://lh7-us.googleusercontent.com/m1uIxp03So9xxaiE-YvmS9Px93lq48sMG0V6ZA84MmNsjHHn6eQZW6SyWN1nvacKelmqboYRG-RSJzViGtmJ1M9YOI8iX8dnmEKPiioPZhfE5sf65WhGHCfukTVY8OjfUvlNYpEgm-EF53AWwBigGXw)
_IP address from instance details page_

It should now look like what is shown below (where 18.232.109.18 is the public IP for my instance). Afterwards, click the orange `Create records` button in the bottom right corner.

![Image](https://lh7-us.googleusercontent.com/5oj2JsQt_YRKWqDSbINcSWbnK5ON3T1u49MI9TyYqhuSMkcaJ3SU__aYJjh7cc7730OVsIDVRC9WMiWzEshiDkYl1NIJ8cb6sdYmHQuvW9Y7kcYarxdBk-BcZ91zPHKyZkFIpWBJCZ4aI_ouyPWx374)
_Completing the A Record creation_

You should see a success message. Also, that the record will now be added to the records table that you saw earlier, as shown below:

![Image](https://lh7-us.googleusercontent.com/DlR8djeTU_JtBEWHJIbwxfhxHzI_ubQl5Bfx2X6f3qlpnDwr3R_xs1YuZN_2donh4sH8KTG1PRWicd7wjzLLcjjoRcdTOHENhKGpvcNDEecudxvYC3JAhCvvEh6rmgBOVKDAkF_rZWZrbyP61dV0SkI)
_Success message after creating the record_

You still have to add the record to cater to the possible use of `www` when reaching your website. Click the `Create record` button to add that record. This time around, you will put `www` into the subdomain input box.

![Image](https://lh7-us.googleusercontent.com/4JBcC8FFtVm9GLd3hl0wm3PptwXgpaySUlxdw2g1vWnu0g3jote---0v5MxLVTz6Ypj3yjAEngPx4XfUDgJ2-uShQiY5z8sKTI0yLiCJLH4saASR5xdwxLXSKyxzySYGBrgWa_E3LsdVBruMJ9dSIr8)
_Adding A record to handle the use of www_

Also, you will need to turn on `Alias` which is beneath the Record name. After turning it on, a new set of options (Route traffic to) will be made available. 

![Image](https://lh7-us.googleusercontent.com/xd5aFDvaDaCl6i4ZV-8ZHhmRTBcE8UDLjTe9N1p6ffOhRYFZuAt2ElEAGyXV4piLPk8pJD3e_uS-3MXBZDU5nN1n4XWHd9k49HYkrGeiZMtQl4935dhvhjzgC2wgS2tIpNSs4HARQ5Dl5hVZvZ6h1SY)
_Turning on the Alias for the record_

For the `Choose endpoint` dropdown, select `Alias to another record in this hosted zone` and the Region will automatically be populated for you. But it also brings up another field labeled `Choose record`.

![Image](https://lh7-us.googleusercontent.com/tzVQSFj6MyEhnT-7p_310X_DgbuucKT3BqKmbgIUqihIAfdiFvJw83HTlpG8mGVdhOFjyCOn0lFSkFFlgdk2sQH9aE6fINs29BoyPZs35uZwbP-p76mGU9cFGBnqFmHNVVaRWJd-G2MxTGRBldM4TMA)
_Select an option for "Route traffic to"_

Go ahead and click within the `Choose record` field and it will suggest your domain name for you. Go ahead and select it.

![Image](https://lh7-us.googleusercontent.com/cCGijn9B6_j8BtxIs-zncIDZyRoRsb66JdeLPJv4-RgSNlbT8aZr6CELWboC7zYfuspwoRE3bhlOKvCeZ4RFESKzmA47SoYTX5N9119kdA9QxC6gw2e2895IK3Vlo5tWwyOs62zYESw22keeTWs3nU4)
_Associate domain with record_

Now you are ready to add this record too so proceed to click the `Create records` button. You will get a success message and see that the new record has been added to the records table.

![Image](https://lh7-us.googleusercontent.com/2SmlaORdC9UHuNL_FDJxTKNUBTqfRloS3jK1TtB4N_mzfVIWwXI-N33kd2qizIGlUGvuGm1lvBUdMj3T99BnG6t-AcOiZd2mQk-dnBY-i2rLr7OWVwwO8VaEauOLsIpk2r7pqQFujv5OWw_dIzjC0DY)
_Success message after adding new record_

Once you are done setting up the records, you can now proceed to update your name servers with our Domain retailing company (NameCheap in my case).

## Step 3: Update Nameservers with Your Domain Provider

If you already have an account with a domain provider, then log in to your account. But if not, then you'll need to sign up with one to purchase a new domain. 

Personally, I use Namecheap for most of my domains. So, I will be showing how to get this done with Namecheap (but again, it will be similar for various Domain providers). 

Note that I already have a domain name, and for any domain that you purchase you will have some default nameservers. Your goal here is to change the default nameservers or whatever your nameservers currently are to the ones which Route 53 provides you. 

### Changing nameservers in Namecheap

![Image](https://lh7-us.googleusercontent.com/Lkdxzcd7dt-85SamUv4R2c1OI0UY9W3zAqqlXljpI6x4ywSlFUxbPJ-y1F3CGHlxW6Laz55IaS542jSeZuo3uc_gQqsMEL4ysQEK4pR3i6Ig81GXXNjCB0uuqlWyrufEEGjYbMYvqIbT-4lbkeu72Qs)
_Namecheap user Dashboard_

Click on the `Domain list` to see a list of all the domains that you have in that account. Look for the specific domain that you have.

![Image](https://lh7-us.googleusercontent.com/4eSm_L1erf8ma66aZNKJCQtFCjIgJgQ0i7mx013PJ6ZRZU-zp2gHOltqYrZFaworF9-sUGE5iW07joLUw4rlUnPx7aUiCdyxDCljZtFv7l5C5HViYdZh-my2aOXji55OaIwG2m7_anaUs1XPS-aR3fg)
_Domain list_

Next to each domain name, you will find the `Manage` button. Click the respective one for the domain that you are using (krachy.com in my case).

![Image](https://lh7-us.googleusercontent.com/sTT4r41ZnwwtG9FURnWSo4SDEvhhuiXXfhDrJDgSxg26Jk2VmWhLMkL-SWhQJ9b84l88LsPf-ywDaxnWpbI7VD44tl3Kprau26EoTzRRfo2cdcRPSxvqAnFCyGqnmQrMgrJ-zgXl-o6r_QBMxPRHgVc)
_Detail page for selected domain_

Under Nameservers, make sure you have selected `Custom DNS`. Then go back to Route 53 and copy the nameservers that you were provided with. Then delete what you currently have and add what you get from Route 53.

In my case, Route 53 gave me four different Nameservers. So I have to copy them one after the other and add them to Namecheap (remember to delete any old ones that were in the domain provider account).

![Image](https://lh7-us.googleusercontent.com/vq9KwsyF13Tmt00vHzDIkIMU47h_5EzB4CaXFUhrvjpIJqpWCI8qOcmXEkdqJS92d6up3nvVYq78gSE-4SHMATFxJWSNQJvdhZZW-SUh4tAOi4llNRIJwy4_Kj5qRhhuHHth1mDpQS08gTu_R-OcjGg)
_Nameservers for the domain name_

In Namecheap, they provide two spaces for the nameservers – but there is a button just below that lets you add more than 2. In my case, I added all four of them as you can see below:

![Image](https://lh7-us.googleusercontent.com/Bunq4l59Hm7HzrnOzqDwU1YesduGAhxdlpuOYVp8290Mc30rY3z3iwSg0D6LCra4t2JJ2ysGEWqdIdDA18YfGIEvdpWNMFuGkKF7k9RAJ-v-A1Z678QfdVJqv4GZUsDP9cjZnt6eNmlOoGFk4XpaPKg)
_Updating nameservers_

Also, after adding them, you need to accept the changes and save them. In the screenshot above, you can see that at the far right of `Custom DNS` is a check mark and an x mark. Click on the check mark to save the changes.

After saving, you will notice that those buttons are no longer available.

![Image](https://lh7-us.googleusercontent.com/7xuh7yPSzecl12m5BCblDIWBcXo27f5dqPK6huZpGLvZ-R2gH3wTYHaWCl02X3xTZLBAKWbNvGyyIPn4pkaMMQv6xO9nORX-BDZw21k_0hwVx4L8rSXYq0UuzTPTnhuSIFNLhbgWpl63BxXubJf5yDk)
_Nameservers updated on Namecheap_

## Step 4: DNS Propagation

Congratulations, you are now done with the set up. Now you just need to wait for the DNS propagation to be completed.

This step doesn’t involve you taking any action, but just waiting for a couple of minutes. The propagation can take anywhere from a couple of minutes to more than 24 hours. 

But after a short while, just enter your domain name in your browser’s address bar and see if it shows the website that you have hosted on the EC2 instance.

Once the DNS propagation goes through, your website will be live on the domain name that you used. Congratulations once again!

![Image](https://lh7-us.googleusercontent.com/UOIjgyUqN4-DGBvTfLscjsnulDkapBsOvEfga7m-NkEkp8CriJfXEL-w1a6ZdlqIOc_ebkK1NLQm7H-tZDIOEMhcj3_cWfEUPLXjyob7aq4bU19qyN3lWHlL60G1pCH_AdrydjUE1KiZPC4gHCwwvQw)
_Website linked to domain after DNS propagation_

As you can see, this is the same interface that I started with – but the good news is that now, I accessed it with the domain name I purchased and not the IP address of the instance.

## Wrapping Up

Even though you are done, you are currently using a non-secured transfer protocol (http) for your website. This is because you haven't yet installed an SSL certificate on your website. 

Watch out for my next tutorial where I walk you through how to install SSL on your domain to make it secure (https).  

