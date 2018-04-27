#!/bin/sh

echo "Running with full provided YOLO weights."
echo "Please enter a file address for a video. If none is provided, source will default to webcam."
read -p "File address: " file_address

if [[ $# -eq 0 ]]
then
	./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights $file_address
else
	./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights 
fi