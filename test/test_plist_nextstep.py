from plist.parser import ParserGrammar, Parser, Rule, Terminal, NonTerminal, TokenStream
from plist.lexer import LexerGrammar, Pattern, Lexer
import sys
from StringIO import StringIO
if sys.version_info >= (2,7):
    import unittest
else:
    import unittest2 as unittest

import plist.nextstep
from plist.nextstep import NSPlistReader

testLexerGrammar = plist.nextstep.LEXER_GRAMMAR
testParserGrammar = plist.nextstep.PARSER_GRAMMAR

class ParserTest(unittest.TestCase):
    def test_simple_dict(self):
        input = """{a = valuea; b = valueb;}"""
        expected = {"a" : "valuea", "b" : "valueb"}

        self.assertPlistEquals(input, expected)

    def test_simple_array(self):
        input = """(a,b,c)"""
        expected = ["a", "b", "c"]

        self.assertPlistEquals(input, expected)

    def test_complex_string(self):
        input = """{a = "\\"abc\\"\\nlinebreak"; b = valueb;}"""
        expected = {"a" : "\"abc\"\nlinebreak", "b" : "valueb"}

        self.assertPlistEquals(input, expected)


    def assertPlistEquals(self, input, expected, msg=None):
        r = NSPlistReader(StringIO(input))
        actual = r.read()

        self.assertEquals(actual, expected, msg)