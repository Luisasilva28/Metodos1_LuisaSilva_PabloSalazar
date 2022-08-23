function factorial(){
	local fac=1
	for i in $(eval echo "{1..$1}")
	do
		fac=$(($fac*$i))
	done
	let final=$fac
}

function variaciones(){
	local n=20
	local r=3
	factorial $n
	numerador=$final
	factorial $(($n-$r))
	denominador=$final
	let final=$(($numerador/$denominador))
	
}
variaciones
echo $final


