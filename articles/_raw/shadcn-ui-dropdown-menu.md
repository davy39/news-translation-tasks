---
title: How to Make a Dropdown Menu with shadcn/ui
subtitle: ''
author: Ajay Kalal
co_authors: []
series: null
date: '2025-07-17T21:02:46.587Z'
originalURL: https://freecodecamp.org/news/shadcn-ui-dropdown-menu
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752786132476/fef60fd2-ad5e-4f9d-9dcf-de4b99adac99.png
tags:
- name: shadcn
  slug: shadcn
- name: Tailwind CSS
  slug: tailwind-css
- name: Next.js
  slug: nextjs
- name: UI
  slug: ui
seo_title: null
seo_desc: 'Dropdown menus are little pop-up menus that help you show more options
  without cluttering your screen. They’re super helpful in websites and apps.

  In this guide, you’ll learn how to build a dropdown menu using shadcn/ui. It’s a
  tool that works well w...'
---

Dropdown menus are little pop-up menus that help you show more options without cluttering your screen. They’re super helpful in websites and apps.

In this guide, you’ll learn how to build a dropdown menu using shadcn/ui. It’s a tool that works well with Tailwind CSS and Radix UI to help you make nice-looking, easy-to-use menus.

## Table of Contents

* [What is shadcn/ui?](#heading-what-is-shadcnui)
    
* [Why Use shadcn/ui for Dropdowns?](#heading-why-use-shadcnui-for-dropdowns)
    
* [Let’s Build a Dropdown Step-by-Step](#heading-lets-build-a-dropdown-step-by-step)
    
    * [Step 1: Start a New Project](#heading-step-1-start-a-new-project)
        
    * [Step 2: Add the Dropdown Menu Component](#heading-step-2-add-the-dropdown-menu-component)
        
    * [Step 3: Import What You Need](#heading-step-3-import-what-you-need)
        
    * [Step 4: Build a Simple Dropdown](#heading-step-4-build-a-simple-dropdown)
        
    * [Step 5: Make It Look Better](#heading-step-5-make-it-look-better)
        
    * [Step 6: Make It Work on All Screens](#heading-step-6-make-it-work-on-all-screens)
        
    * [Step 7: Add Cool Icons](#heading-step-7-add-cool-icons)
        
    * [Step 8: It’s Already Accessible!](#heading-step-8-its-already-accessible)
        
* [Real-World Use Case: Country Dropdown with Flags](#heading-real-world-use-case-country-dropdown-with-flags)
    
* [Final Thoughts](#heading-final-thoughts)
    

### 💡 Prerequisites

Before we start, make sure you have:

* Basic knowledge of React and JavaScript
    
* Node.js and a package manager like npm, pnpm, or yarn are installed
    
* Familiarity with Tailwind CSS is a bonus, but not required
    

We’ll walk through everything step by step, so don’t worry if you’re not an expert yet.

## What is shadcn/ui?

[shadcn/ui](https://ui.shadcn.com/docs/installation) is a group of tools (called components) that help you build parts of a website, like buttons, modals, and dropdowns. It’s built with Radix UI and styled using Tailwind CSS. It’s perfect if you’re using React or Next.js.

With shadcn/ui, you don’t get just styled components, you get full control over how everything works and looks. That makes it perfect for teams that want consistency in design without giving up flexibility.

### Why Use shadcn/ui for Dropdowns?

Dropdown menus are a great use case for shadcn/ui because:

* It’s easy to use with keyboard and screen readers
    
* You can create custom looks using Tailwind CSS
    
* You control how it works and looks
    
* It works great in real websites and apps
    
* It integrates well with modern React workflows
    

## Let’s Build a Dropdown Step-by-Step

### Step 1: Start a New Project with shadcn/ui

You don’t need to set up React, Next.js, or Tailwind manually. Just run this command:

```bash
pnpm dlx shadcn@latest init
```

This will automatically create a new Next.js app with Tailwind CSS and shadcn/ui preconfigured.

Tip: You can also use `npx` instead of `pnpm dlx` if you prefer:

```bash
npx shadcn@latest init
```

### Step 2: Add the Dropdown Menu Component

After your project is ready, add the dropdown component using:

```bash
npx shadcn@latest add dropdown-menu
```

This will pull in all the necessary components to create a dropdown menu.

### Step 3: Import What You Need

In your React file, import the full dropdown module so you can access all its features:

```tsx
import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuGroup,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuPortal,
} from "@/components/ui/dropdown-menu"
```

### Step 4: Build a Simple Dropdown

![Screenshot of basic dropdown we're building](https://cdn.hashnode.com/res/hashnode/image/upload/v1752690572839/4cb2bd61-b843-4fe3-8530-4b341d38a633.jpeg align="center")

Here’s a basic dropdown example:

```tsx
export function ProfileMenu() {
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <button className="px-4 py-2 bg-primary text-white rounded">
          Open Menu
        </button>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-56">
        <DropdownMenuLabel>My Account</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuItem>Profile</DropdownMenuItem>
        <DropdownMenuItem>Settings</DropdownMenuItem>
        <DropdownMenuItem>Log out</DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

This is just the start. You can add groups, submenus, and keyboard shortcuts for power users.

### Step 5: Make It Look Better

![Screenshot showing dropdown with styling applied](https://cdn.hashnode.com/res/hashnode/image/upload/v1752690441156/0c2b8e39-72ca-4823-8dd2-6af305f02275.jpeg align="center")

Use Tailwind CSS to style your dropdown, and hover effects like this:

```tsx
<DropdownMenu>
        <DropdownMenuTrigger asChild>
          <button className="px-3 py-1.5 bg-primary text-white text-sm font-medium rounded-md hover:bg-primary/90 transition-colors">
            Open Menu
          </button>
        </DropdownMenuTrigger>
        <DropdownMenuContent className="w-52 border-gray-200 shadow-lg rounded-md space-y-0.5">
          <DropdownMenuLabel className="text-xs text-gray-500">
            My Account
          </DropdownMenuLabel>
          <DropdownMenuSeparator className="border-t border-gray-100" />
          <DropdownMenuItem className="px-3 py-1.5 text-sm text-gray-700 hover:bg-gray-100 rounded-md cursor-pointer transition-colors">
            Profile
          </DropdownMenuItem>
          <DropdownMenuItem className="px-3 py-1.5 text-sm text-gray-700 hover:bg-gray-100 rounded-md cursor-pointer transition-colors">
            Settings
          </DropdownMenuItem>
          <DropdownMenuItem className="px-3 py-1.5 text-sm text-red-600 hover:bg-red-50 rounded-md cur
```

### Step 6: Make It Work on All Screens

Want your dropdown to be responsive? Use Tailwind’s responsive classes:

```tsx
<DropdownMenuContent className="w-full md:w-64">
```

You can also dynamically position the dropdown using Radix's built-in portal support.

### Step 7: Add Cool Icons

![Screenshot of dropdown with icons added](https://cdn.hashnode.com/res/hashnode/image/upload/v1752691587711/0a96c5ca-0fa2-4916-92d2-087f2071d40e.jpeg align="center")

Install Lucide icons:

```bash
npm install lucide-react
```

Then use them in your menu:

```tsx
import { User, Settings, LogOut } from "lucide-react"

<DropdownMenuItem>
  <User className="mr-2 h-4 w-4" /> Profile
</DropdownMenuItem>
```

Icons help users scan options quickly – a great touch for UX.

### Step 8: It’s Already Accessible!

shadcn/ui (thanks to Radix UI) makes your dropdown menu:

* Keyboard friendly
    
* Screen-reader ready
    
* Following best web practices
    

You don’t need to configure accessibility – it just works :)

## Real-World Use Case: Country Dropdown with Flags

Looking for a more advanced dropdown? Here’s an amazing example that includes search, flag icons, and grouping:

![Shadcn dropdown example](https://cdn.hashnode.com/res/hashnode/image/upload/v1752598285627/6cb8b27e-7cba-4d92-95c5-3bea44e0c01c.png align="center")

👉 [shadcn-country-dropdown.vercel.app](https://shadcn-country-dropdown.vercel.app/)

It’s open-source and a great place to see what’s possible with shadcn/ui.

## Final Thoughts

Using shadcn/ui to create a dropdown menu is fast, simple, and powerful. You get great styling, accessibility, and full control over how things look and work. Whether you’re just starting out or building for production, this is a solid tool to use.

Dropdowns are just the beginning. shadcn/ui offers a whole library of headless components for building modern UIs.

I hope you found this article helpful! If you're building a SaaS product or any web app that involves user interaction or conversion, consider enhancing user trust with real-time notifications like modal pop-ups, [sales pop up](http://toastie.saasindie.com), etc.
