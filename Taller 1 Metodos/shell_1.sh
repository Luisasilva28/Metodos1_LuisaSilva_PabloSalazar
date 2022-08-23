function factorial(){
local fac=1
for i in $(eval echo "{1..$1}")
	do
        	fac=$(($fac*$i))
        done
        let final=$fac
}
factorial $1
echo $final

