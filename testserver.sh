#!/bin/bash 

server=$1
c=$2
a=$3

if [ -z "$a" ]
then
	if [ -z "$c" ]
	then
		if [ -z "$server" ]
		then
			echo "Usage: testserver.sh <server> [ {hello|find|call|ring|accept|drop|goodby} ] [ {<user>|kclu} ]"
			exit 1
		fi
		for i in hello find call ring accept drop goodbye
		do
			./testserver.sh $server $i
			for j in alice bob kclu
			do
				./testserver.sh $server $i $j
			done
		done
	fi
fi

# At this point, we know server, c and a are specified

echo "connect to http://$server/$c/$a"
curl "http://$server/$c/$a"
