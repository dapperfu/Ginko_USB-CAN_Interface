.DEFAULT: all
.PHONY: all
all:
	sudo python3 Python_USB_CAN_Test/CANRead.py


.PHONY: test
test:
	pytest
