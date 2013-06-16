Date: 2012-12-07
Title: My Workstation / Dev Environment
Category: development
Tags: android, linux, debian, dwm

I've gone through a bunch of workstations over the past few years. From an underpowered [MSI Wind U100](http://en.wikipedia.org/wiki/MSI_Wind_Netbook) (That may or may not have fallen out of the back of a moving vehicle due to my failure to close the back when moving), to the [venerable](http://www.cnet.com/laptops/lenovo-thinkpad-t61p/4505-3121_7-32553560.html) [Thinkpad T61p](http://www.thinkwiki.org/wiki/Category:T61p) to the hand-me-down Dell Desktop or (ugh) Mac Book Pro Retina, I've tried a bunch. What has been missing? Not sure how to define it. 

### The Tablet
Currently, I have an [HP TouchPad](http://en.wikipedia.org/wiki/HP_TouchPad) (16GB Model) that is my tablet. Although WebOS is.. pretty, I prefer to use Android. Mostly because WebOS has been more or less left for dead (I have hopes for OpenWebOS, but that's off topic). The tablet has a 9.7" screen and a 1.2 GHz dual-core Snapdragon processor. It is, in comparison to modern tablets, underpowered, but most of the work I do is in The Cloud<sup>TM</sup>. I'm not too worried about my local dev machine.

### The Keyboard
My keyboard, originally purchased because it was the cheapest one I could find, wound up being a great investment. I have a [Rocksoul BK-101DROBB](http://www.frys.com/product/6828406?site=sr:SEARCH:MAIN_RSLT_PG) that I snagged from Fry's. For as cheap of a device as it was, the build quality is great. Keys are solid, and it (here's the big one) passes all the correct keycodes when you hit mod keys. This is important, since my window manager is a custom build of [DWM](https://bitbucket.org/kmwhite/dwm/src/f47d1318d7b3/?at=kristofer).

### Needed APKs
Assuming you have Android dual booting on your tablet (it isn't necessary, but I suggest the [CM9-Nighties > 2012-11-18](http://get.cm/?device=tenderloin) with the [Camera Patch](http://rootzwiki.com/topic/36499-hp-touchpad-camera-fix-for-cm9-official-nightly-builds-patch-by-dorregaray/#entry1026287)), there's a couple apps you need to install:

 * [Complete Linux Installer](https://play.google.com/store/apps/details?id=com.zpwebsites.linuxonandroid&hl=en) - This streamlines the installation of your linux of choice. I use Debian Lenny, but I'm sure that Arch Linux would have worked as well. Sadly, FreeBSD is a technical impossiblity given the current method of running these images.
 * [android-vnc-viewer](http://code.google.com/p/android-vnc-viewer/issues/detail?id=238#c28) - If you have the same keyboard I do, you'll likely have problems with the version that is in the Play Store. The linked version (on comment #28) is patched to correctly support the codes sent by Ctrl, Alt, et cetera. 

### Cutting to the Chase
*NOTE*: This is written off memory and will be updated once I get a chance to re-run it on my tablet to verify 
I'm going to assume that you installed the APKs, followed the instructions in Complete Linux Installer (for debian lenny, although the only difference is that you need to change the paths in the examples below), and have a functioning Linux chroot. This is all great, right? No. The space of the image, 700MB, is far to small to be productive in. We need to go bigger. To do this, start up the Android Terminal app that came installed with CM9 (It's also a requirement for Complete Linux Installer, so it will be installed) and cd to your install location:

> cd /sdcard/debian

Once inside, you'll need to create a new debian.img file:

> cp debian.img debian_new.img # wait for the slow copy...

To increase the size of the disk, you'll need to 'dd' zeros to the end of the image. We use double '>>' as we want to append, not overwrite:

> dd if=/dev/zero bs=1k count=4000000 >> debian_new.img

Once the write is completed, you can boot back to the debian.img. It would be great to say we're done, but we first need to resize the filesystem of debian_new.img before we can use it. The version of resize2fs in Lenny doesn't support live resizing. Once the chroot is back, run:

> sudo e2fsck -y -f /sdcard/debian/debian_new.img	# Ensure the filesystem is clean before resizing

> sudo resize2fs /sdcard/debian/debian_new.img		# Resize the filesystem

> sudo e2fsck -f /sdcard/debian/debian_new.img		# Ensure the filesystem is clean after resizing

Now you can exit. Once out of the chroot, run:

> mv /sdcard/debian/debian.img{,.old}

> mv /sdcard/debian/debian{_new,}.img

This will move the old, 700mb image out of the way (safely) and the new one into place. Now you can boot back up and enjoy all 4GB of space. Sadly, this isn't a lot either, but the FAT filesystem of the /sdcard mount is at fault for that. If you need more, you ahve to look into partitioning your sdcard and that's not covered here. Maybe another post... :)
