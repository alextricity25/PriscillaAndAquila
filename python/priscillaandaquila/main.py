# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
import re
from priscillaandaquila import args
from diyr.utils.bible import Bible

def main():
    """
    This is a command line utility and takes in a comma delimited list of
    verse references, performs a lookup on each reference, and returns a
    list of their corresponding verses
    """
    parsed_args = args.get_parser().parse_args()
    bible = Bible()
    if parsed_args.file:
        verse_refs = open(parsed_args.file, 'r')
    elif parsed_args.verses:
        verse_refs = parsed_args.verses.split(';')
    else:
        raise Exception("Choose an argument!")
    for verse_ref in verse_refs:
        extrapolated_verse_ref = bible.extrapolate_abbriv(verse_ref.strip())
        # Splitting verse to book, chapter, verse
        reg = re.compile('(([0-9]*) *[\D]+) *([0-9]*):([0-9]*)')
        m = reg.match(extrapolated_verse_ref)
        verse = bible.verse_lookup(m.group(1).strip(),
                                   m.group(3).strip(),
                                   m.group(4).strip())
        verse = re.sub('[0-9]*\.', '', verse).strip()
        print "{} - {} {}:{}".format(
            verse,
            m.group(1).strip(),
            m.group(3).strip(),
            m.group(4).strip())


if __name__ == '__main__':
    main()
