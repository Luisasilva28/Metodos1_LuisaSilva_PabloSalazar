function factorial(){
        local fac=1
        for i in $(eval echo "{1..$1}")
        do
                fac=$(($fac*$i))
		echo $fac
        done
        let final=$fac
}
factorial $1
echo 'Factorial de '$1' es: '$final
echo 'Los primeros 20 factoriales son:'
factorial 20
