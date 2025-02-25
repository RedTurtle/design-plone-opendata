# https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/file-type

# import xml.etree.ElementTree as ET
# file_path = "/mnt/data/filetypes.xml"
# tree = ET.parse(file_path)
# root = tree.getroot()
# records = []
# for record in root.findall("record"):
#     internet_media_type = record.find("internet-media-type")
#     authority_code = record.find("authority-code")
#     labels = record.find("label")    
#     if internet_media_type is not None and authority_code is not None:
#         label_text = None
#         if labels is not None:
#             ita_label = labels.find("lg.version[@lg='ita']")
#             eng_label = labels.find("lg.version[@lg='eng']")
#             label_text = ita_label.text if ita_label is not None else (eng_label.text if eng_label is not None else None)
#         records.append({
#             "internet-media-type": internet_media_type.text,
#             "authority-code": authority_code.text,
#             "label": label_text
#         })


# http://publications.europa.eu/resource/authority/file-type/CSV"
[
    {
        "internet-media-type": "application/x-tar",
        "authority-code": "TAR",
        "label": "TAR"
    },
    {
        "internet-media-type": "application/x-gzip",
        "authority-code": "GZIP",
        "label": "GNU zip"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "ZIP",
        "label": "ZIP"
    },
    {
        "internet-media-type": "application/vnd.amazon.ebook",
        "authority-code": "AZW",
        "label": "Amazon Kindle eBook"
    },
    {
        "internet-media-type": "application/epub+zip",
        "authority-code": "EPUB",
        "label": "EPUB"
    },
    {
        "internet-media-type": "application/x-mobipocket-ebook",
        "authority-code": "MOBI",
        "label": "Mobipocket eBook"
    },
    {
        "internet-media-type": "image/gif",
        "authority-code": "GIF",
        "label": "GIF"
    },
    {
        "internet-media-type": "image/jpeg",
        "authority-code": "JPEG",
        "label": "JPEG"
    },
    {
        "internet-media-type": "image/tiff",
        "authority-code": "TIFF",
        "label": "TIFF"
    },
    {
        "internet-media-type": "image/png",
        "authority-code": "PNG",
        "label": "PNG"
    },
    {
        "internet-media-type": "application/postscript",
        "authority-code": "EPS",
        "label": "Encapsulated Postscript"
    },
    {
        "internet-media-type": "text/css",
        "authority-code": "CSS",
        "label": "CSS"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDF",
        "label": "PDF"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFA1A",
        "label": "PDF/A-1a"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFA1B",
        "label": "PDF/A-1b"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFX",
        "label": "PDF/X"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "METS",
        "label": "METS XML"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "METS_ZIP",
        "label": "METS package"
    },
    {
        "internet-media-type": "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
        "authority-code": "PPSX",
        "label": "PowerPoint PPSX"
    },
    {
        "internet-media-type": "application/vnd.ms-powerpoint",
        "authority-code": "PPS",
        "label": "PowerPoint Slide Show"
    },
    {
        "internet-media-type": "application/vnd.ms-powerpoint",
        "authority-code": "PPT",
        "label": "PowerPoint PPT"
    },
    {
        "internet-media-type": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "authority-code": "PPTX",
        "label": "PowerPoint PPTX"
    },
    {
        "internet-media-type": "application/vnd.ms-excel",
        "authority-code": "XLS",
        "label": "Excel XLS"
    },
    {
        "internet-media-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "authority-code": "XLSX",
        "label": "Excel XLSX"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "XSLFO",
        "label": "XSL-FO"
    },
    {
        "internet-media-type": "application/xslt+xml",
        "authority-code": "XSLT",
        "label": "XSLT"
    },
    {
        "internet-media-type": "application/sgml",
        "authority-code": "DTD_SGML",
        "label": "SGML DTD"
    },
    {
        "internet-media-type": "application/xml-dtd",
        "authority-code": "DTD_XML",
        "label": "XML DTD"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "SCHEMA_XML",
        "label": "XML schema"
    },
    {
        "internet-media-type": "text/sgml",
        "authority-code": "FMX2",
        "label": "Formex 2"
    },
    {
        "internet-media-type": "text/sgml",
        "authority-code": "FMX3",
        "label": "Formex 3"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "FMX4",
        "label": "Formex 4"
    },
    {
        "internet-media-type": "application/rdf+xml",
        "authority-code": "RDF_XML",
        "label": "RDF XML"
    },
    {
        "internet-media-type": "text/turtle",
        "authority-code": "RDF_TURTLE",
        "label": "RDF Turtle"
    },
    {
        "internet-media-type": "text/sgml",
        "authority-code": "SGML",
        "label": "SGML"
    },
    {
        "internet-media-type": "application/rdf+xml",
        "authority-code": "SKOS_XML",
        "label": "SKOS"
    },
    {
        "internet-media-type": "application/owl+xml",
        "authority-code": "OWL",
        "label": "OWL"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "XML",
        "label": "XML"
    },
    {
        "internet-media-type": "application/sparql-query",
        "authority-code": "SPARQLQ",
        "label": "SPARQL"
    },
    {
        "internet-media-type": "application/sparql-results+xml",
        "authority-code": "SPARQLQRES",
        "label": "SPARQL results"
    },
    {
        "internet-media-type": "application/msword",
        "authority-code": "DOC",
        "label": "Word DOC"
    },
    {
        "internet-media-type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "authority-code": "DOCX",
        "label": "Word DOCX"
    },
    {
        "internet-media-type": "application/vnd.oasis.opendocument.text",
        "authority-code": "ODT",
        "label": "ODT"
    },
    {
        "internet-media-type": "text/plain",
        "authority-code": "TXT",
        "label": "Plain text"
    },
    {
        "internet-media-type": "text/rtf",
        "authority-code": "RTF",
        "label": "RTF"
    },
    {
        "internet-media-type": "text/html",
        "authority-code": "HTML",
        "label": "HTML"
    },
    {
        "internet-media-type": "application/xhtml+xml",
        "authority-code": "XHTML",
        "label": "XHTML"
    },
    {
        "internet-media-type": "text/csv",
        "authority-code": "CSV",
        "label": "CSV"
    },
    {
        "internet-media-type": "application/x-msaccess",
        "authority-code": "MDB",
        "label": "MDB"
    },
    {
        "internet-media-type": "application/x-dbase",
        "authority-code": "DBF",
        "label": "DBF"
    },
    {
        "internet-media-type": "chemical/x-mopac-input",
        "authority-code": "MOP",
        "label": "MOP"
    },
    {
        "internet-media-type": "application/x-e00",
        "authority-code": "E00",
        "label": "E00"
    },
    {
        "internet-media-type": "application/x-mxd",
        "authority-code": "MXD",
        "label": "MXD"
    },
    {
        "internet-media-type": "application/vnd.google-earth.kml+xml",
        "authority-code": "KML",
        "label": "KML"
    },
    {
        "internet-media-type": "text/tab-separated-values",
        "authority-code": "TSV",
        "label": "TSV"
    },
    {
        "internet-media-type": "application/json",
        "authority-code": "JSON",
        "label": "JSON"
    },
    {
        "internet-media-type": "application/vnd.google-earth.kmz",
        "authority-code": "KMZ",
        "label": "KMZ"
    },
    {
        "internet-media-type": "application/gml+xml",
        "authority-code": "GML",
        "label": "GML"
    },
    {
        "internet-media-type": "application/rss+xml",
        "authority-code": "RSS",
        "label": "RSS feed"
    },
    {
        "internet-media-type": "application/vnd.oasis.opendocument.spreadsheet",
        "authority-code": "ODS",
        "label": "ODS"
    },
    {
        "internet-media-type": "application/x-indesign",
        "authority-code": "INDD",
        "label": "INDD"
    },
    {
        "internet-media-type": "application/x-photoshop",
        "authority-code": "PSD",
        "label": "PSD"
    },
    {
        "internet-media-type": "application/postscript",
        "authority-code": "PS",
        "label": "PS"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "ODF",
        "label": "ODF"
    },
    {
        "internet-media-type": "application/x-compressed",
        "authority-code": "TAR_XZ",
        "label": "TAR XZ"
    },
    {
        "internet-media-type": "application/gzip",
        "authority-code": "TAR_GZ",
        "label": "TAR GZ"
    },
    {
        "internet-media-type": "application/rdf+xml",
        "authority-code": "RDF",
        "label": "RDF"
    },
    {
        "internet-media-type": "application/xliff+xml",
        "authority-code": "XLIFF",
        "label": "XLIFF"
    },
    {
        "internet-media-type": "application/ovf",
        "authority-code": "OVF",
        "label": "OVF"
    },
    {
        "internet-media-type": "application/ld+json",
        "authority-code": "JSON_LD",
        "label": "JSON-LD"
    },
    {
        "internet-media-type": "application/n-triples",
        "authority-code": "RDF_N_TRIPLES",
        "label": "RDF N-Triples"
    },
    {
        "internet-media-type": "application/x-hdf",
        "authority-code": "HDF",
        "label": "HDF"
    },
    {
        "internet-media-type": "application/x-netcdf",
        "authority-code": "NETCDF",
        "label": "NetCDF"
    },
    {
        "internet-media-type": "application/EDIFACT",
        "authority-code": "SDMX",
        "label": "SDMX"
    },
    {
        "internet-media-type": "image/jp2",
        "authority-code": "JPEG2000",
        "label": "JPEG 2000"
    },
    {
        "internet-media-type": "application/x-shapefile",
        "authority-code": "SHP",
        "label": "Esri Shape"
    },
    {
        "internet-media-type": "application/x-filegdb",
        "authority-code": "GDB",
        "label": "Esri File Geodatabase"
    },
    {
        "internet-media-type": "application/x-gmz",
        "authority-code": "GMZ",
        "label": "Zipped GML"
    },
    {
        "internet-media-type": "application/x-ecw",
        "authority-code": "ECW",
        "label": "ECW"
    },
    {
        "internet-media-type": "application/x-ascii-grid",
        "authority-code": "GRID_ASCII",
        "label": "Esri ASCII grid"
    },
    {
        "internet-media-type": "application/x-oracledump",
        "authority-code": "DMP",
        "label": "Oracle Dump"
    },
    {
        "internet-media-type": "application/x-las",
        "authority-code": "LAS",
        "label": "LASer file"
    },
    {
        "internet-media-type": "application/x-laz",
        "authority-code": "LAZ",
        "label": "Compressed LAS file"
    },
    {
        "internet-media-type": "application/x-tab",
        "authority-code": "TAB",
        "label": "MapInfo TAB file"
    },
    {
        "internet-media-type": "application/x-tab-raster",
        "authority-code": "TAB_RSTR",
        "label": "MapInfo TAB raster file"
    },
    {
        "internet-media-type": "application/x-worldfile",
        "authority-code": "WORLD",
        "label": "World file"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "TMX",
        "label": "TMX"
    },
    {
        "internet-media-type": "application/atom+xml",
        "authority-code": "ATOM",
        "label": "Atom Feed"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "OCTET",
        "label": "Octet Stream"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "BIN",
        "label": "Binary Data"
    },
    {
        "internet-media-type": "application/vnd.oasis.opendocument.chart",
        "authority-code": "ODC",
        "label": "OpenDocument Chart"
    },
    {
        "internet-media-type": "application/vnd.oasis.opendocument.database",
        "authority-code": "ODB",
        "label": "OpenDocument Database"
    },
    {
        "internet-media-type": "application/vnd.oasis.opendocument.graphics",
        "authority-code": "ODG",
        "label": "OpenDocument Image"
    },
    {
        "internet-media-type": "image/x-ms-bmp",
        "authority-code": "BMP",
        "label": "Bitmap Image File"
    },
    {
        "internet-media-type": "application/x-director",
        "authority-code": "DCR",
        "label": "DCR File"
    },
    {
        "internet-media-type": "chemical/x-xyz",
        "authority-code": "XYZ",
        "label": "XYZ Chemical File"
    },
    {
        "internet-media-type": "arcgis_map_preview",
        "authority-code": "MAP_PRVW",
        "label": "ArcGIS Map Preview"
    },
    {
        "internet-media-type": "arcgis_map_service",
        "authority-code": "MAP_SRVC",
        "label": "ArcGIS Map Service"
    },
    {
        "internet-media-type": "arcgis_rest",
        "authority-code": "REST",
        "label": "Esri REST"
    },
    {
        "internet-media-type": "message/http",
        "authority-code": "MSG_HTTP",
        "label": "HTTP Message"
    },
    {
        "internet-media-type": "image/tiff-fx",
        "authority-code": "TIFF_FX",
        "label": "TIFF FX"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDF1X",
        "label": "PDF1X"
    },
    {
        "internet-media-type": "application/gzip",
        "authority-code": "WARC_GZ",
        "label": "WARC GZ"
    },
    {
        "internet-media-type": "application/n-quads",
        "authority-code": "RDF_N_QUADS",
        "label": "RDF N-Quads"
    },
    {
        "internet-media-type": "application/trig",
        "authority-code": "RDF_TRIG",
        "label": "RDF TriG"
    },
    {
        "internet-media-type": "application/rdfa",
        "authority-code": "RDFA",
        "label": "RDFa"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "ARC",
        "label": "ARC"
    },
    {
        "internet-media-type": "text/html",
        "authority-code": "HTML_SIMPL",
        "label": "HTML simplified"
    },
    {
        "internet-media-type": "application/xhtml+xml",
        "authority-code": "XHTML_SIMPL",
        "label": "XHTML simplified"
    },
    {
        "internet-media-type": "application/sql",
        "authority-code": "SQL",
        "label": "SQL"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFA2A",
        "label": "PDF/A-2a"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFA2B",
        "label": "PDF/A-2b"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFA3",
        "label": "PDFA-3"
    },
    {
        "internet-media-type": "application/mbox",
        "authority-code": "MBOX",
        "label": "MBOX"
    },
    {
        "internet-media-type": "audio/mpeg",
        "authority-code": "MPEG2",
        "label": "MPEG-2"
    },
    {
        "internet-media-type": "application/mp4",
        "authority-code": "MPEG4",
        "label": "MPEG-4"
    },
    {
        "internet-media-type": "application/mp4",
        "authority-code": "MPEG4_AVC",
        "label": "MPEG-4 AVC"
    },
    {
        "internet-media-type": "audio/vnd.wave",
        "authority-code": "BWF",
        "label": "BWF"
    },
    {
        "internet-media-type": "message/html",
        "authority-code": "MHTML",
        "label": "MHTML"
    },
    {
        "internet-media-type": "application/gzip",
        "authority-code": "ARC_GZ",
        "label": "ARC GZ"
    },
    {
        "internet-media-type": "application/warc",
        "authority-code": "WARC",
        "label": "WARC"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFX1A",
        "label": "PDF/X-1a"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFX2A",
        "label": "PDF/X-2a"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFX4",
        "label": "PDF/X-4"
    },
    {
        "internet-media-type": "application/geo+json",
        "authority-code": "GEOJSON",
        "label": "GeoJSON"
    },
    {
        "internet-media-type": "application/x-grid",
        "authority-code": "GRID",
        "label": "Esri binary grid"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "JATS",
        "label": "JATS XML"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "BITS",
        "label": "BITS XML"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "PWP",
        "label": "PWP"
    },
    {
        "internet-media-type": "application/x-iso9660-image",
        "authority-code": "ISO",
        "label": "ISO image"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "ISO_ZIP",
        "label": "Zipped ISO image"
    },
    {
        "internet-media-type": "application/vnd.rar",
        "authority-code": "RAR",
        "label": "RAR"
    },
    {
        "internet-media-type": "image/svg+xml",
        "authority-code": "SVG",
        "label": "SVG"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "QGS",
        "label": "QGS"
    },
    {
        "internet-media-type": "text/n3",
        "authority-code": "N3",
        "label": "N3"
    },
    {
        "internet-media-type": "image/x-mrsid",
        "authority-code": "MRSID",
        "label": "MrSID"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "EXE",
        "label": "EXE"
    },
    {
        "internet-media-type": "application/javascript",
        "authority-code": "JS",
        "label": "JavaScript"
    },
    {
        "internet-media-type": "text/calendar",
        "authority-code": "ICS",
        "label": "ICalendar"
    },
    {
        "internet-media-type": "text/x-perl",
        "authority-code": "PL",
        "label": "Perl script"
    },
    {
        "internet-media-type": "application/gml+xml",
        "authority-code": "WFS_SRVC",
        "label": "WFS"
    },
    {
        "internet-media-type": "application/vnd.ogc.wms_xml",
        "authority-code": "WMS_SRVC",
        "label": "WMS"
    },
    {
        "internet-media-type": "application/vnd.hdt",
        "authority-code": "HDT",
        "label": "HDT"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "LEG",
        "label": "LEG"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "IMMC_XML",
        "label": "IMMC XML message"
    },
    {
        "internet-media-type": "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
        "authority-code": "XLSB",
        "label": "XLSB"
    },
    {
        "internet-media-type": "application/vnd.ms-excel.sheet.macroEnabled.12",
        "authority-code": "XLSM",
        "label": "XLSM"
    },
    {
        "internet-media-type": "application/vnd.oasis.opendocument.presentation",
        "authority-code": "ODP",
        "label": "ODP"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "RDF_TRIX",
        "label": "RDF TriX"
    },
    {
        "internet-media-type": "application/x-7z-compressed",
        "authority-code": "7Z",
        "label": "7z"
    },
    {
        "internet-media-type": "audio/aac",
        "authority-code": "AAC",
        "label": "AAC"
    },
    {
        "internet-media-type": "application/vnd.android.package-archive",
        "authority-code": "APK",
        "label": "APK"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "APPX",
        "label": "AppX"
    },
    {
        "internet-media-type": "application/x-arj",
        "authority-code": "ARJ",
        "label": "ARJ"
    },
    {
        "internet-media-type": "application/x-bzip2",
        "authority-code": "BZIP2",
        "label": "bzip2"
    },
    {
        "internet-media-type": "application/vnd.debian.binary-package",
        "authority-code": "DEB",
        "label": "deb"
    },
    {
        "internet-media-type": "application/x-apple-diskimage",
        "authority-code": "DMG",
        "label": "DMG"
    },
    {
        "internet-media-type": "application/java-archive",
        "authority-code": "JAR",
        "label": "JAR"
    },
    {
        "internet-media-type": "application/x-lzh-compressed",
        "authority-code": "LHA",
        "label": "LHA"
    },
    {
        "internet-media-type": "application/x-lzip",
        "authority-code": "LZIP",
        "label": "lzip"
    },
    {
        "internet-media-type": "application/x-lzop",
        "authority-code": "LZO",
        "label": "lzo"
    },
    {
        "internet-media-type": "application/x-lzma",
        "authority-code": "LZMA",
        "label": "lzma"
    },
    {
        "internet-media-type": "application/x-rpm",
        "authority-code": "RPM",
        "label": "RPM"
    },
    {
        "internet-media-type": "application/x-sb3",
        "authority-code": "SB3",
        "label": "sb3"
    },
    {
        "internet-media-type": "application/x-ms-wim",
        "authority-code": "SWM",
        "label": "SWM"
    },
    {
        "internet-media-type": "application/x-ms-wim",
        "authority-code": "WIM",
        "label": "WIM"
    },
    {
        "internet-media-type": "application/x-xz",
        "authority-code": "XZ",
        "label": "xz"
    },
    {
        "internet-media-type": "application/x-compress",
        "authority-code": "Z",
        "label": "Z"
    },
    {
        "internet-media-type": "application/x-ole-storage",
        "authority-code": "MSI",
        "label": "MSI"
    },
    {
        "internet-media-type": "application/java+zip",
        "authority-code": "WAR",
        "label": "WAR"
    },
    {
        "internet-media-type": "application/java-archive",
        "authority-code": "EAR",
        "label": "EAR"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "FMX4_ZIP",
        "label": "FMX4 ZIP"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "AKN4EU",
        "label": "AKN4EU file"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "AKN4EU_ZIP",
        "label": "AKN4EU ZIP"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "ETSI_XML",
        "label": "ETSI signature validation report"
    },
    {
        "internet-media-type": "application/geopackage+sqlite3",
        "authority-code": "GPKG",
        "label": "GeoPackage"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "DGN",
        "label": "DGN"
    },
    {
        "internet-media-type": "image/vnd.dxf",
        "authority-code": "DXF",
        "label": "DXF"
    },
    {
        "internet-media-type": "image/vnd.dwg",
        "authority-code": "DWG",
        "label": "DWG"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "IPA",
        "label": "IPA"
    },
    {
        "internet-media-type": "multipart/related",
        "authority-code": "WCS_SRVC",
        "label": "WCS"
    },
    {
        "internet-media-type": "application/pdf",
        "authority-code": "PDFUA",
        "label": "PDF/UA"
    },
    {
        "internet-media-type": "text/html",
        "authority-code": "HTML5",
        "label": "HTML5"
    },
    {
        "internet-media-type": "model/stl",
        "authority-code": "STL",
        "label": "StL"
    },
    {
        "internet-media-type": "application/x-authorware-bin",
        "authority-code": "AAB",
        "label": "AAB"
    },
    {
        "internet-media-type": "multipart/mixed",
        "authority-code": "ARCINFO_COV",
        "label": "ArcInfo coverage"
    },
    {
        "internet-media-type": "image/tiff",
        "authority-code": "GEOTIFF",
        "label": "GeoTIFF"
    },
    {
        "internet-media-type": "multipart/mixed",
        "authority-code": "LPK",
        "label": "Layer package"
    },
    {
        "internet-media-type": "text/plain",
        "authority-code": "MIF_MID",
        "label": "MIF/MID"
    },
    {
        "internet-media-type": "text/plain",
        "authority-code": "UNGEN",
        "label": "Ungen"
    },
    {
        "internet-media-type": "application/vnd.android.package-archive",
        "authority-code": "OAPK",
        "label": "OAPK"
    },
    {
        "internet-media-type": "application/vnd.android.package-archive",
        "authority-code": "DAPK",
        "label": "DAPK"
    },
    {
        "internet-media-type": "audio/MPA",
        "authority-code": "MP3",
        "label": "MP3"
    },
    {
        "internet-media-type": "audio/vnd.wave",
        "authority-code": "WAV",
        "label": "WAV"
    },
    {
        "internet-media-type": "application/rdf+thrift",
        "authority-code": "RDF_THRIFT",
        "label": "RDF Thrift"
    },
    {
        "internet-media-type": "application/xhtml+xml",
        "authority-code": "XHTML5",
        "label": "XHTML5"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "GTFS",
        "label": "GTFS"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "YAML",
        "label": "YAML"
    },
    {
        "internet-media-type": "application/xml",
        "authority-code": "EFORMS_XML",
        "label": "eForms XML"
    },
    {
        "internet-media-type": "image/webp",
        "authority-code": "WEBP",
        "label": "WebP"
    },
    {
        "internet-media-type": "application/gml+xml",
        "authority-code": "WMTS_SRVC",
        "label": "WMTS"
    },
    {
        "internet-media-type": "video/quicktime",
        "authority-code": "MOV",
        "label": "MOV"
    },
    {
        "internet-media-type": "application/mathml+xml",
        "authority-code": "MATHML",
        "label": "MathML"
    },
    {
        "internet-media-type": "application/gzip",
        "authority-code": "DWCA",
        "label": "DwC-A"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "GPX",
        "label": "GPX"
    },
    {
        "internet-media-type": "application/vnd.etsi.tsl+xml",
        "authority-code": "ETSI_TSL",
        "label": "ETSI TSL"
    },
    {
        "internet-media-type": "application/xhtml+xml",
        "authority-code": "LEGALHTML",
        "label": "LegalHTML"
    },
    {
        "internet-media-type": "text/markdown",
        "authority-code": "MARKDOWN",
        "label": "Markdown"
    },
    {
        "internet-media-type": "application/vnd.apache.parquet",
        "authority-code": "PARQUET",
        "label": "Parquet"
    },
    {
        "internet-media-type": "application/vnd.apache.thrift.binary",
        "authority-code": "THRIFT_BINARY",
        "label": "Thrift binary"
    },
    {
        "internet-media-type": "application/vnd.apache.thrift.compact",
        "authority-code": "THRIFT_COMPACT",
        "label": "Thrift compact"
    },
    {
        "internet-media-type": "application/vnd.apache.thrift.json",
        "authority-code": "THRIFT_JSON",
        "label": "Thrift JSON"
    },
    {
        "internet-media-type": "application/vnd.apache.arrow.file",
        "authority-code": "ARROW_FILE",
        "label": "Arrow file"
    },
    {
        "internet-media-type": "application/vnd.apache.arrow.stream",
        "authority-code": "ARROW_STREAM",
        "label": "Arrow stream"
    },
    {
        "internet-media-type": "application/zip",
        "authority-code": "AKN4EU_LEG",
        "label": "AKN4EU LEG"
    },
    {
        "internet-media-type": "application/octet-stream",
        "authority-code": "MATLAB_MAT",
        "label": "MATLAB MAT"
    }
]