# Installation:

## Clone repos
 - Install `64 bit Raspberry Pi OS` and update the system (`apt-get install update` && `apt-get install upgrade`)
 - Clone the `rpi-rgb-led-matrix` library and the `pandr-matrix` repo to the `Desktop`. You may want to sign into git using `gh auth login`

## Build Python bindings for the led matrix
 - Install Cython with `sudo apt install cython3 python3-dev`
 - `cd` into the `rpi-rgb-led-matrix` library
 - In this directory, run `make build-python PYTHON=python3` and `sudo make install-python PYTHON=python3`

## Disable sound
According to the `rpi-rgb-led-matrix` docs, "If sound is enabled on your Pi, this will not work together with the LED matrix, as both need the same internal hardware sub-system". We must disable it.

Run:
```
cat <<EOF | sudo tee /etc/modprobe.d/blacklist-rgb-matrix.conf
blacklist snd_bcm2835
EOF

sudo update-initramfs -u
```

Then reboot.