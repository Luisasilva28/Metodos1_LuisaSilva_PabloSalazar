file='punto_8.txt'

i=1

while read line; do
    if [ $i -eq 3 ];then
        echo $line
	break	
    fi
    i=$((i+1))
	
done < $file

