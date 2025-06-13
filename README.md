# Batch_Csv_Wkt_Importer_Fr
Import as many csv files with wkt line geometry, with a single click, provided the files are of the same known type.
In this first version, the CRS is by default the CRS of the project, the first field is WKT geometry (and named WKT), and all the other fields are of integer type by default.
If there are characters in the features, the corresponding field is of string type.
US version uses comma as field separator. Fr version uses semicolon.
Developped as part of Q-Traf, a macroscopic traffic program working with QGis.
Feel free to modify the file batch_csv_wkt_importer.py to your convenance.
