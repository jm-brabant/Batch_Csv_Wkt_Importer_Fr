def classFactory(iface):
    from .batch_csv_wkt_importer import BatchCSVWKTImporter
    return BatchCSVWKTImporter(iface)