# The jetson-dronekit-camera project
This project was written to equip a Pixhawk4 drone with a jetson nano as 
companion computer. In the present case the jetson nano takes on command 
two images in parallel (up to 30 ms delay) using its two CSI cameras. The 
command is triggered by MAVLink messages from ground control. Since the 
images are used for aerial mapping, gps coordinates are tracked.

## Quick Start
Connect your jetson nano with two CSI cameras as companion computer to your 
PX4 by UART, e.g. using a CP2102. Remember to forward the mavlink messages and
start-up the application with

```console
foo@jetson-nano:~$ docker-compose up app
```

The images and logs are saved to ./data in a time stamped directory.

##License
The jetson-dronekit-camera project is primarily distributed under the terms 
of  both the MIT license and the Apache License (Version 2.0).

See LICENSE-APACHE, LICENSE-MIT, and COPYRIGHT for details.