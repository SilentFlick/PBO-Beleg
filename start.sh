#!/usr/bin/env bash

function detach {
    ("$@" &>/dev/null &)
}
function xo {
    for var in "$@"; do
        detach xdg-open "$var"
    done
}

if ! ping -c 1 -n -i 0.2 rlux40.rz.htw-dresden.de &>/dev/null; then
    echo "Cannot contact HTW LDAP Server. Please connect to HTW VPN if you want to login."
fi
nohup npm run dev >/dev/null 2>&1 &
frontendPID=$(echo $!)
#Start Server
cd ./src/backend/
if [ -f pbo ]; then
    rm pbo
fi
nohup python3 main.py >/dev/null 2>&1 &
backendPID=$(echo $!)
printf 'To stop fronend run: kill -9 %d\n' "$frontendPID"
printf 'To stop backend run: kill -9 %d\n' "$backendPID"

xo "http://localhost:8080"