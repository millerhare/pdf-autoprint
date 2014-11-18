from PyPDF2 import PdfFileWriter, PdfFileReader

import optparse


def AddPrint(infile, outfile):
  output = PdfFileWriter()
  input  = PdfFileReader(open(infile, "rb"))

  # print how many pages input has:
  print "Processing '%s' with %d pages." % (infile, input.getNumPages())

  for x in range(0, input.getNumPages()):
    output.addPage(input.getPage(x))

  # add some Javascript to launch the print window on opening this PDF.
  output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

  # write output to disk
  outputStream = file(outfile, "wb")
  output.write(outputStream)


def Main():
    parser = optparse.OptionParser(usage='usage: %prog [options] in-pdf-file out-pdf-file', version='%prog 0.1')
    (options, args) = parser.parse_args()
 
    if len(args) != 2:
        print "pdf-autoprint, embed auto print JavaScript to a PDF document that will execute automatically when the document is opened"
        print ""
        parser.print_help()
        return

    infile  = args[0]
    outfile = args[1]
    AddPrint(infile, outfile)

if __name__ == '__main__':
    Main()

