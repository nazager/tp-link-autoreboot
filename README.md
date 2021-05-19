## TP-Link Auto-Reboot

### Windows Service for auto rebooting router/AP when there are not internet connection.

#### TP-Link credentials were hardcoded, so before installing you have to modify your username and password inside Reboot.py, maybe also the IP address.

### Installing:

```
C:test> python Reboot.py install
```

#### Now you can find the service in Services.msc and configure it:

```
C:test> mmc Services.msc
```


### Start:

```
C:test> net start TP-LINK-Auto-reboot
```

### Stop:

```
C:test> net stop TP-LINK-Auto-reboot
```
____
____
____

#### Inspired by my faulty AP and made following this article by [@mastr035](https://github.com/mastro35):
#### http://thepythoncorner.com/dev/how-to-create-a-windows-service-in-python/