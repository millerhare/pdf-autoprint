# pdf-autoprint
PDF file utiltiies.

  - Add auto printing javascript to PDFs
  - Remove auto printing javascript from PDFs
  - Remove all text from PDFs


## Install
You'll need [python](https://www.python.org/) installed

    pip install git+ssh://git@github.com/millerhare/pdf-autoprint.git
	
	python -m pip install PyPDF2

## Usage

    $ pdf-autoprint.py --help
    pdf-autoprint, embed auto print JavaScript to a PDF document that will execute automatically when the document is opened

    Usage: 
      pdf-autoprint [options] in-pdf-file out-pdf-file
      pdf-noprint [options] in-pdf-file out-pdf-file

      pdf-notext [options] in-pdf-file out-pdf-file


    Options:
      --version   show program's version number and exit
      -h, --help  show this help message and exit

So for example

    pdf-autoprint.py in.pdf out.pdf

It also supports glob matching which is used in the following way. Note the outpath **must** be a directory if the glob matches multiple files.
An appropriately named output file/folder will be automatically created if it not supplied. In windows there should be no trailing slash on the path.

    pdf-autoprint.py "doc*.pdf" out/


## License
MIT
