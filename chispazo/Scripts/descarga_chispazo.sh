#!/bin/bash
wget https://www.pronosticos.gob.mx/Documentos/Historicos/Chispazo.csv --no-check-certificate
mv Chispazo.csv ../data/real
echo 'Success'


