#!/bin/bash

Year=$( TZ=UTC date | cut -d' ' -f 7 | sort )
Time=$( TZ=UTC date | cut -d' ' -f 5 | sort ) 
Day=$( TZ=UTC date | cut -d' ' -f 4 | sort )
Month=$( TZ=UTC date +%m )
NetID=eawrght2.txt
Underscore=_
filename=$Year-$Month-$Day$Underscore$Time$Underscore$NetID

cp HW2script2.sh $filename
