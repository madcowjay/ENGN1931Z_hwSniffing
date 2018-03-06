# Detective Work and Port Sniffing
Sniffing Homework Assignment for ENGN1931Z

To this point, we have learned how to control instruments that were specifical designed for programmatic control, e.g. by SCPI. However, it is often the case that we may need to control devices that were not designed with this purpose. For example, there are many computer controlled instruments where the manufacturers intend for you to control their device using specific software. This includes cases where they did not imagine a need for automation or where they may wish for you to purchase additional software from them to enable automation.

Thankfully, many computer controlled devices use serial communication that can be easily monitored and decoded. (This includes many motor controllers and simple sensors that have USB connections, but use a USB-RS232 converter chip for operation.) The key to this procedure is finding a way to monitor (sniff) the serial port, and then carefully considering the commands that you send to the instrument. 

To monitor the port, I would recommend the `socat` method that we explored in class (and is [described here on SO](http://unix.stackexchange.com/a/225904/192231)). Remember that PTY is a pseudoterminal, so if you want to setup a virtual device at `/dev/ttyUSB0`, then you would use `PTY,link=/dev/ttyUSB0,raw,echo=0` as one of the socat ends. Finally, to read the resulting traffic (e.g. in your input/output text file logs), I would encourage you to use `xxd` to create hex dumps that will show you non-printable characters.

As demonstrated in class, the `hw_sniffing` file is an executable that can control a Thorlabs PRM1Z8 motorized rotation stage. Your goal for this assignment is to learn the serial commands that this program uses to control the stage, and demonstrate this knowledge by writing a python script that passes a set of precise motion commands as a long string to a virtual PRM1Z8 device online.  

Your goal is to produce a command sequence that will:
 - First home the stage;
 - Then move the stage to each position in a list of desiredAngles (as obtained from a web server);
 - Finally query the position of the stage at its final position.

`hw_sniffing` is the excecutable file that you will need to run on your RPi to decipher the command structure.  This executable was compiled for Raspbian and will not run on your personal laptop. (**Note that to run the executable, you can use the following terminal command: `sudo ./hw_sniffing` in the directory with the file.** The `./` prefix adds the current directory to the path when looking for executables, and sudo will probably be helpful when you are trying to sniff the port.) 

`hw_sniffing.py` is a template code for the assignment. **Please review the comments at the top of that file.**  `submit.py` is the script that will submit your code to the autograder.

Please note you are welcome to try this assignment as many times as you would like. (There is no penalty for failed attempts, because I wanted to encourage you to practice, test, and debug.) **However, please make sure to obey the class collaboration policy --- do not share your code with others; please write and debug on your own!**

If you happen to get a Bad Request (400) error, it may be that your `hw_sniffing.py` file is too large. To help address this, please feel free to delete the top part of the homework that includes my documentation so that your file gets smaller.
