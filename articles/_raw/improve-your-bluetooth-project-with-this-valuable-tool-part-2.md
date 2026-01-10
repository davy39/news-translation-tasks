---
title: 'Improve Your Bluetooth Project With This Valuable Tool: Part 2!'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-01T07:57:49.000Z'
originalURL: https://freecodecamp.org/news/improve-your-bluetooth-project-with-this-valuable-tool-part-2
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Protocol-Buffers-Part-2.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: protocol-buffers
  slug: protocol-buffers
seo_title: null
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com.

  This is Part 2 of configuring your own Bluetooth Low Energy Service using a Nordic
  NRF52 series processor. If you haven’t seen Part 1 go back and check it out. I’ll
  be waiting right here...'
---

By Jared Wolff

**This post is originally from [www.jaredwolff.com.](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2/)**

This is Part 2 of configuring your own Bluetooth Low Energy Service using a Nordic NRF52 series processor. If you haven’t seen [Part 1][part1] go back and check it out. I’ll be waiting right here..

If you’re with me thus far,  high five. ?

Let’s jump in!

So far we’ve created an efficient cross platform data structure using Protocol Buffers. This Protocol Buffer in particular can be used to send these defined data structures a Bluetooth Low Energy Service. In this part, I’ll show you the inner workings of creating the service from scratch.

P.S. this post is lengthy. If you want something to download, [click here for a a beautifully formatted PDF.](https://www.jaredwolff.com/files/how-to-define-a-protocol-buffer-ble-service-pdf/) (Added bonus, the PDF has all three parts of this series!)


## Creating the Service
![Door Peoeple](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2/images/doorman.jpg)

Dealing with Bluetooth Low Energy in general can seem overwhelming. As I discussed [here][get-started],  there’s a few moving parts that you need to keep in mind.

The best way to create a new service is to copy an already existing one! I’ve done this by:

1. Go to the sdk -> components -> ble -> ble_services -> ble_bas
2. Copy `ble_bas.h` to `include/ble`
3. Copy `ble_bas.c` to `src/ble`

I’ve then renamed them from `ble_bas` to `ble_protobuf` to be consistent. I’ve also done the same inside the files. (BAS is the battery level service used to report battery voltage or relative charge using a percentage)

I’ve also gone ahead and removed all the battery measurement  functions as they will be replaced.  This part of the process is fairly tedious and prone to error. If you’re new to the Nordic SDK, [I highly recommend you download the example code for this post.][code]

### Adding a UUID

Normally, for a vendor defined service you’ll have to use your own UUID. There are certain ranges of UUIDs that are reserved for the Bluetooth SIG. Supposedly you can also reserve your own UUID if you’re a member. [Here’s a handy post on Stack Overflow on the subject.](https://stackoverflow.com/questions/10243769/what-range-of-bluetooth-uuids-can-be-used-for-vendor-defined-profiles)

In our case, I’ve defined a UUID that I’ve used for other projects. If you go to `ble_protobuf.h` you can see the UUIDs for both the service and the characteristic:

```c
// UUID for the Service & Char
#define PROTOBUF_UUID_BASE   {0x72, 0x09, 0x1a, 0xb3, 0x5f, 0xff, 0x4d, 0xf6, \
                               0x80, 0x62, 0x45, 0x8d, 0x00, 0x00, 0x00, 0x00}
#define PROTOBUF_UUID_SERVICE     0xf510
#define PROTOBUF_UUID_CONFIG_CHAR (PROTOBUF_UUID_SERVICE + 1)
```

Both `PROTOBUF_UUID_BASE` `PROTOBUF_UUID_SERVICE`  are used in `ble_protobuf_init` The last one is used in `command_char_add` (I’ll describe that a bit more below).

You can go without defining a BASE ID but I highly recommend you go the extra mile. That way your application will be impervious to future Bluetooth protocol updates.

## Creating the Characteristic
![Open Those PICKLES!](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2/images/man-641691_1280.jpg)

Nordic has a fairly straight forward way of initializing separate characteristics in each service. For each characteristic, there is a `char_add` function which then configures and add the characteristic to the service.

### Configure your Characteristic with`ble_add_char_params_t`

Nordic has put the configurations parameters for a BLE Characteristic into a logical (and helpful) struct. If you’re developing on a different platform you may find the same settings though all not in one place! (Or handled logically… ?)

Here’s the breakdown of the struct:

```c
typedef struct
{
    uint16_t                    uuid;
    uint8_t                     uuid_type;
    uint16_t                    max_len;
    uint16_t                    init_len;
    uint8_t *                   p_init_value;
    bool                        is_var_len;
    ble_gatt_char_props_t       char_props;
    ble_gatt_char_ext_props_t   char_ext_props;
    bool                        is_defered_read;
    bool                        is_defered_write;
    security_req_t              read_access;
    security_req_t              write_access;
    security_req_t              cccd_write_access;
    bool                        is_value_user;
    ble_add_char_user_desc_t    *p_user_descr;
    ble_gatts_char_pf_t         *p_presentation_format;
} ble_add_char_params_t;
```

It’s here that you tell the BLE Stack about what type of characteristic this is. In this example I use a handful of parameters to define the Protobuf Command Characteristic.

`uuid` defines the address of how the characteristic will be accessed. If you’re defining your own service.
`max_len` is the maximum length of data that you may send though the characteristic. That’s why it’s important to set `max_size` in your Protocol Buffer `.options` file for all variable length parameters. Once you compile your Protocol Buffers you’ll get a `*_size` variable much like the one defined in `command.pb.h` Here's a snippet of what it looks like below:

```c
/* Maximum encoded size of messages (where known) */
#define event_size                               67
```

Thus when defining `ble_add_char_params_t` I set `max_len` to `event_size`:

```c
add_char_params.uuid                      = PROTOBUF_UUID_CONFIG_CHAR;
add_char_params.max_len                   = event_size;
add_char_params.is_var_len                = true;
```

Along the same lines, because we’re using a *string* as one of the parameters in the Protocol Buffer, this data can be of variable size.  `is_var_len` is handy to make sure that the right amount of bytes is sent and received. The decode function of the Protocol Buffers will fail if more data is fed in than necessary. (I learned this the hard way!)

`char_props` define the permissions for the characteristic. If you’re familiar with file system permissions on a computer, this will be second nature to you. In this example, **read** and **write** is what we’re looking for.

Finally, parameters ending in `_access` determine the security type used. In most cases `SEC_OPEN` or `SEC_JUST_WORKS`is more than sufficient. If you’re handling critical data (passwords, etc) you may have to implement a second layer of encryption or enable a higher level security mode.

If you’re looking on more info about Bluetooth Low Energy security, [here’s a useful post on the subject.](https://duo.com/decipher/understanding-bluetooth-security)

### Add. dat. char.

Once you’ve defined your params, it’s as easy as calling the `characteristic_add` function. This will associate this new characteristic with the related service. The first argument is the service handle, the second the configuration parameters and the third is a pointer to the handles for the characteristic. (See below)

```c
uint32_t characteristic_add(uint16_t                   service_handle,
                            ble_add_char_params_t *    p_char_props,
                            ble_gatts_char_handles_t * p_char_handle)
```

## Getting it Running
Setting everything up inside `ble_protobuf.c` is 90% of the battle. The final mile requires some bits being added to  `services_init` in `main.c`

```c
    ble_protobuf_init_t       protobuf_init = {0};

    protobuf_init.evt_handler          = ble_protobuf_evt_hanlder;
    protobuf_init.bl_rd_sec            = SEC_JUST_WORKS;
    protobuf_init.bl_cccd_wr_sec       = SEC_JUST_WORKS;
    protobuf_init.bl_wr_sec            = SEC_JUST_WORKS;

    err_code = ble_protobuf_init(&m_protobuf,&protobuf_init);
    APP_ERROR_CHECK(err_code);
```

The above allows events to be funneled back to the main context. That way your app becomes much more interactive with the core logic of your firmware code. In Nordic’s examples they’ve also brought the security parameters out so they can be defined in the main context as well.

*Side note:* `m_protobuf` is defined using a macro from `ble_protobuf.h` It not only creates a static instance of the service but it also defines the callback that is used for handling events.

```c
/**@brief Macro for defining a ble_protobuf instance.
 *
 * @param   _name  Name of the instance.
 * @hideinitializer
 */
#define BLE_PROTOBUF_DEF(_name)                          \
    static ble_protobuf_t _name;                         \
    NRF_SDH_BLE_OBSERVER(_name ## _obs,             \
                         BLE_PROTOBUF_BLE_OBSERVER_PRIO, \
                         ble_protobuf_on_ble_evt,        \
                         &_name)
```

If you're making your own service, you'll have to update the function name for the event handler. If you need to tweak priorities you can define/update that as well.

## What happens when this characteristic is written to?
![Smoke Signal](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2/images/person-629676_1280.jpg)


`ble_protobuf_on_ble_evt` is the main way that events are handled within Bluetooth Low Energy services. We’re most concerned with the `BLE_GATTS_EVT_WRITE` event but you can trigger on any GATT event that tickles your fancy.

`on_write` is where the action happens. It takes the data that is written to the characteristic and decodes it according to `event_fields` It’s all put conveniently into a struct for additional processing, etc. If an error happens in decoding, `pb_decode` returns an error. Once modified, the data is encoded and made available for reading. Since reading [Part 1][part1], the calls to `pb_decode` and `pb_encode` should look very familiar!

Of course, you can have your firmware do whatever you want to. The Bluetooth Energy World is your oyster.

## Final Notes
When adding new services to a Bluetooth Low Energy example, you may have to make some changes to the underlying code.

For example, `sdk_config.h` may need some changes. Particularly `NRF_SDH_BLE_VS_UUID_COUNT` needs to be increased depending how many service UUIDs are made available. For this project, I am also using the  DFU service (as it should be a default for all connected projects!!)

Another important aspect is memory and flash management. The default `.ld` file that comes with the BLE DFU service may not be sufficient for another BLE Service. The only way you’ll know there’s not enough is when you compile and flash it to a NRF52 device. If the device boots up stating there’s not enough memory, you’ll have to make the suggested changes. The error will show up on the debug console where this message normally shows up:

```bash
<info> app: Setting vector table to bootloader: 0x00078000
<info> app: Setting vector table to main app: 0x00026000
```

Learn more about how to get the Debug Console set up [in the example code here.][code]

## Conclusion
In this part I’ve shown you the inner workings of a custom Bluetooth Low Energy service using Protocol Buffers. In the last part, I’ll show you how to load the firmware, run the example javascript app and test our freshly developed Protocol Buffer!


[code]: https://www.jaredwolff.com/files/protobuf/
[part1]: https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf
[get-started]: https://www.jaredwolff.com/get-started-with-bluetooth-low-energy/


