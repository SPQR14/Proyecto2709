@ECHO OFF
curl https://www.pronosticos.gob.mx/Documentos/Historicos/Chispazo.csv -O Chispazo.csv
move /Y Chispazo.csv ..\Data_set\real\
ECHO ON