# pyblynk - Blynk helpers for Python

This is just another Python implementation of the Blynk service ( http://blynk.cc ). I have forked (https://github.com/erazor83/pyblynk) and changed it quite radically

## How to use:
From the off this library is meant for overloading. The idea is that you import the Hardware library and use is as a base class. An example will follow.

In the mean time have a look at the original output:

## example
There is a simple example which connects to the blynk service and prints out detailed frame info:

```
erazor@s9 ~/d/p/t/examples> python2 hw.py 
Auth successfull
(20, 36, 14)
('OnPinMode', 0, 'out')
('OnPinMode', 2, 'out')
(20, 46, 4)
('OnVirtualRead', 1)
(20, 47, 4)
('OnVirtualRead', 1)
(20, 48, 4)
('OnVirtualRead', 1)
(20, 49, 4)
```

For a custom implementation you only need to overload **lib.hm.Hardware** .
