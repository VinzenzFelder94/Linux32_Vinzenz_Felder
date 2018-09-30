#hw05 is a mixture of diffrent task.
#In the main directory of hw05 is a Makefile which compiles app.c the compiled file is app.arm. If you execute the file you will get "Hello World" message.

#a.out got cross-compiled from the host,(task2)

#the 3 directories are for LKM all of them are part from the Kernel tutorial from derek molloy

#in hello you will find a hello.c file after executing the Makefile, you can execute the Kernel model
#use sudo insmod hello.ko
#besides open the kernel log. it is quit nice option to watch what is going on with the kernel

#enter: bone$ sudo bash
#	bone$ cd /var/log/
#	bone$ tail -f kern.log

#in the terminal you should see the Kernel log, really helpfull for the following tasks.

#in gpio_test is gpio_test.c.it uses the kernal to operate and copy GPIO P9_15 for Led und P9_16

#ebbchar is a LKM to communicate with the Kernel . it is part of the second tutorial from Derek Molloy

#I enterd my name for Project idea
