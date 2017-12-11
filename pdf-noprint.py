#!/usr/bin/env python
from PyPDF2 import PdfFileWriter, PdfFileReader

import optparse
import glob
import os


def AddPrint(infile, outpath):
  files = glob.glob(infile)
  outisdir = os.path.isdir(outpath)

  # We have multiple files check if the output is a directory.
  if len(files) > 1 and not(outisdir):
    print 'Out path must be a directory if infile is multiple files'
    return

  for f in files:
    if outisdir:
      outfile = os.path.join(outpath, os.path.basename(f))
    else:
      outfile = outpath

    output = PdfFileWriter()
    input  = PdfFileReader(open(f, "rb"))

    # print how many pages input has:
    print "Processing: '%s', %d pages" % (f, input.getNumPages())

    for x in range(0, input.getNumPages()):
      output.addPage(input.getPage(x))

    # add some Javascript to launch the print window on opening this PDF.
    output.addJS("")

    # write output to disk
    outputStream = file(outfile, "wb")
    output.write(outputStream)
    print "Written: %s" % outfile



def Main():
    parser = optparse.OptionParser(usage='usage: %prog [options] in-pdf-file out-pdf-file', version='%prog 0.1')
    (options, args) = parser.parse_args()
 
    if len(args) != 2:
        print "pdf-noprint, remove auto print JavaScript from a PDF document that executes automatically when the document is opened"
        print ""
        parser.print_help()
        return

    infile  = args[0]
    outfile = args[1]
    AddPrint(infile, outfile)

if __name__ == '__main__':
    Main()

