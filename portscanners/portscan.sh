#!/bin/bash

ajuda() {
	echo "uso:"
	echo -e "\033[01;31mex: $0 'ip de destino a ser escaneado'"
	echo
	reset_color
	echo "-p: portas para escanear (ex: -p 22,80,443)"
	echo "se a flag '-p' nao for especificada, portas TCP comuns serão escaneadas no lugar"
}

reset_color() {
	echo -e -n "\033[00;37m";
}
reset_color

if [ "$(whoami)" != "root" ]; then echo -e "\033[00;31mExecute como Root!";exit;fi

if [ "$1" == "" ] || [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
	ajuda
	reset_color
	exit 0
fi

if [ "$1" == "-p" ]; then
	host=$3
	ports=$(echo $2 | tr ',' ' ')
	get_ports=true

elif [ "$2" == "-p" ] || [ "$2" == "--port" ]; then
	ports=$(echo $3 | tr ',' ' ')
	host=$1
	get_ports=true
else
	host=$1
	ports=(20 21 22 23 25 53 67 68 80 81 110 123 143 179 443 1723 2000 3306 8080)
fi

cont=0;
for i in $*; do cont=$((cont+1)); done
if [ $cont -gt 3 ]; then ajuda; exit 0; fi

echo procurando dependencias...; sleep 2

if [ "$(sudo which hping3)" == "" ]; then
	echo -e "\033[00;31m[!] Hping3 nao encontrado"; sleep 2
	reset_color
	echo instalando...; sleep 1
	sudo apt-get install hping3 -y &> /dev/null
	echo [+] instalado; sleep 1
else
	echo -e "\033[00;36m[+] Encontrado: Hping3"; reset_color
fi
echo

for porta in ${ports[@]:0}; do
	hping3 --syn -i 1 -c 1 $host -p $porta 2> /dev/null > .scan_report.txt
	report=$(grep flags .scan_report.txt | tr ' ' '\n' | grep flags | cut -d'=' -f2)

	if [ "$(cat .scan_report.txt)" == "" ]; then
		echo -e "\033[00;31m[!] Host '$1' se encontra possivelmente inativo ou esta bloqueando nossas tentativas de comunicação."
		reset_color; sleep 1; exit 0

	echo $report
	elif [ "$report" == "SA" ]; then
		echo -e "\033[00;36mPort $porta: Open";
		opened=true
		reset_color
	elif [ "$report" == "RA" ] && [ "$get_ports" == true ]; then
		echo -e "\033[01;31mPort $porta: Closed or Filtered"
		reset_color
		opened=false
	fi
	sleep 0.5
done
if [ "$opened" != true ] && [ "$opened" != false ]; then
	echo -e "\033[01;31mall ports on '$host' are closed or filtered."
	reset_color
fi

echo -e "\nencerrando..."; sleep 1
