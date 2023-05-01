# for printing an html document to pdf
# useful for creating a pdf from modified posterdown html

doc <- PATH/TO/MY/DOCUMENT
pagedown::chrome_print(doc, format = "pdf")
