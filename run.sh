echo Running Daemons...
sleep 1
python authsvr/authsvr.py &
sleep 1
python apisvr/apisvrr.py &
sleep 1
