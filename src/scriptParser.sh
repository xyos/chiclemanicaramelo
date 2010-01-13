
for i in $(ls facturas/*.xml); do
	
	pat1='bbox="40.125,660.992'
	pat2='bbox="13.687,539.871'
	pat3='bbox="13.687,523.786'
	patCedula='[0-9]+.ESTRATO'

	echo $i

	if [ `grep -c $pat1 $i` -gt 0 ]; then
		lin=true
		echo Nombre: `grep  $pat1 $i|grep -oe '[A-Z]*' |awk '{print}' ` ;
		echo Cedula: `grep -oEe $patCedula $i |awk '{print $1}'`;
		echo Estrato:  `grep -e 'ESTRATO' $i |awk '{print $4}' `;
	else
		if [ `grep -c $pat2 $i` -gt 0 ]; then
			echo Nombre: `grep  $pat2 $i|grep -oe '[A-Z]*' |awk '{print}' ` ;
			echo Cedula: `grep -oEe $patCedula $i |awk '{print $1}'`;
			echo Estrato: `grep -e 'ESTRATO' $i |awk '{print $4}' `;
		else
			echo $i : No se encontraron coincidencias con los patrones;
		fi
	fi
	
	echo ''
done

