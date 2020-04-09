import sys
from antlr4 import *
from lolcodeLexer import lolcodeLexer
from lolcodeParser import lolcodeParser
from lolcodeListener import lolcodeListener

class lolcodePrintListener(lolcodeListener):

	def enterProgram(self, ctx):
		print("entered program")

	def exitProgram(self, ctx):
		print("left program")

	def enterCode_block(self, ctx):
		print("entered code_block")

	def exitCode_block(selft, ctx):
		print("left code_block")

	def enterStatement(self, ctx):
		print ("entered statement")

	def exitStatement(self, ctx):
		print("left statement")

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = lolcodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = lolcodeParser(stream)
    tree = parser.program()
    printer = lolcodePrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer,tree)	
 
if __name__ == '__main__':
    main(sys.argv)