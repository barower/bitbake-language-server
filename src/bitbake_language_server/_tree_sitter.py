r"""Tree sitter
===============
"""
import os
from glob import glob

from tree_sitter import Language, Parser

lib = glob(
    os.path.join(
        os.path.join(os.path.join(os.path.dirname(__file__), "data"), "lib"),
        "*",
    )
)[0]
BITBAKE_LANGUAGE = Language(lib, "bitbake")


def get_parser(language: Language | None = None) -> Parser:
    r"""Get parser.

    :param language:
    :type language: Language | None
    :rtype: Parser
    """
    if language is None:
        language = BITBAKE_LANGUAGE
    parser = Parser()
    parser.set_language(language)
    return parser
