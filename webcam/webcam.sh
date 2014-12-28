#!/bin/bash
# A simple bash script to fetch a picture from a USB webcam

DATE=$(date +"%d-%m-%Y_%H%M")
fswebcam -r 1280x720 --no-banner /srv/webcam/$DATE.jpg
