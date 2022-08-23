
function help(){
        echo "Debe ingresar 3 parametros"
}

if [ $# -eq 3 ]; then
	echo "corriendo programa"
else
	help
	exit 1
fi

