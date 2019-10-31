#!/usr/bin/env python
from PyPDF2 import PdfFileWriter, PdfFileReader

import optparse
import glob
import os


def AddPrint(infile, outpath):
  files = glob.glob(infile)
  if not outpath:
    if len(files) > 1:
      outpath = os.path.join(os.path.dirname(infile), "autoprint")
    else:
      outpath = os.path.splitext(infile)[0] + '_autoprint.pdf'
    print("Defaulting output to " + outpath)

  outisdir = os.path.isdir(outpath)
  outexists = os.path.exists(outpath)

  if len(files) > 1 and not(outisdir):
    outpath = os.path.dirname(outpath)
    outisdir = os.path.isdir(outpath)
    outexists = os.path.exists(outpath)

  if outisdir and os.path.samefile(os.path.dirname(infile), outpath):
    outpath = os.path.join(outpath, "autoprint")
    outisdir = os.path.isdir(outpath)
    outexists = os.path.exists(outpath)

  if not outexists and len(files) > 1:
    os.makedirs(outpath)
    outisdir = os.path.isdir(outpath)
    outexists = os.path.exists(outpath)

  # We have multiple files check if the output is a directory.
  if len(files) > 1 and not(outisdir):
    print('Out path must be a directory if infile is multiple files')
    return

  for f in files:
    if outisdir:
      outfile = os.path.join(outpath, os.path.basename(f))
    else:
      outfile = outpath

    output = PdfFileWriter()
    input  = PdfFileReader(open(f, "rb"))

    # print how many pages input has:
    print("Processing: '%s', %d pages" % (f, input.getNumPages()))

    for x in range(0, input.getNumPages()):
      output.addPage(input.getPage(x))

    # add some Javascript to launch the print window on opening this PDF.
    output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

    # write output to disk
    outputStream = open(outfile, "wb")
    output.write(outputStream)
    print("Written: %s" % outfile)



def Main():
    parser = optparse.OptionParser(usage='usage: %prog [options] in-pdf-file [out-pdf-file]', version='%prog 0.2')
    (options, args) = parser.parse_args()
 
    if len(args) < 1:
        print("pdf-autoprint, embed auto print JavaScript to a PDF document that will execute automatically when the document is opened")
        print("")
        parser.print_help()
        return

    infile  = args[0]
    outfile = ""
    if len(args) > 1:
      outfile = args[1]
    AddPrint(infile, outfile)

if __name__ == '__main__':
    Main()

