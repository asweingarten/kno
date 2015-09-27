echo Running Daemons...
sleep 1
python authsvr/authsvr.py &
sleep 1
python apisvr/server.py &
sleep 1
