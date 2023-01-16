#!/bin/bash


nmcli con down id HTW\ Dresden
nmcli con up id HTW\ Dresden

#Start Client
gnome-terminal --tab --title="Client" --command="bash -c 'cd ..; npm run dev; exec bash'" 

#Start Server
cd backend
rm pbo
python3 main.py


