#!/bin/bash
echo "Application started in `date`" >> /var/log/mtop.log
while true ; do
	trap 'echo "got SIGUSR1"' SIGUSR1
	al=$(free |grep 'Память'|awk '{print $2}') 
	us=$(free |grep 'Память'|awk '{print $3}') 
	pc=$(echo "scale=4; $us / $al" | bc)
	#echo $pc
	if [[ $pc > 0.9 ]]; then
		pid=$(ps -eo size,pid,user=$USER,command --sort -size | grep $USER  |head -n 2 |tail -n 1 |awk '{print $2}') ; echo $pid
		echo "killed process ID `date -I` - $pid" >> /var/log/mtop.log
		kill -9 $pid
	fi
	sleep 5
done
echo "Application stoped in `date`" >> /var/log/mtop.log