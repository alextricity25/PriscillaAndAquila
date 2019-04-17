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
import pdb

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
        # Expand the verse reference, so that users can also
        # provide book abbrivations.
        extrapolated_verse_ref = bible.extrapolate_abbriv(verse_ref.strip(),
                                                          raise_exp = False)
        # Splitting verse to book, chapter, verse(s)
        reg = re.compile('(([0-9]*) *[\D]+) *([0-9]*):([0-9]*-*[0-9]*)')
        _verse_refs = _expand_verse_range(reg, extrapolated_verse_ref)
        for _verse_ref in _verse_refs:
            m = reg.match(_verse_ref)
            verse = bible.verse_lookup(m.group(1).strip(),
                                       m.group(3).strip(),
                                       m.group(4).strip())
            # Strip off identifier returned by "verse_lookup"
            verse = re.sub('[0-9]*\.', '', verse).strip()

            if parsed_args.references_first:
                print "{} {}:{} - {}".format(
                    m.group(1).strip(),
                    m.group(3).strip(),
                    m.group(4).strip(),
                    verse)
            else:
                print "{} - {} {}:{}".format(
                    verse,
                    m.group(1).strip(),
                    m.group(3).strip(),
                    m.group(4).strip())

def _expand_verse_range(reg, verse_ref):
    """
    Takes in a Reg  object with very specific groupings. The
    groupings must follow these specifications:
    group(0) - The matched string
    group(1) - The book name
    group(2) - The book number
    group(3) - The book chapter
    group(4) - The verse, or a verse range to be expanded.
    If group(4) is just a single verse, then this method will
    not attempt any logic. If group(4) is a verse range, i.e.
    1 Corin. 2:11-14, the method will return a list of all the
    verses in that range, inclusively.

    The second argument is the verse reference to be expanded.
    """
    verses = []
    m = reg.match(verse_ref)
    if "-" in m.group(4):
        verse_ends = m.group(4).split('-')
        for i in xrange(int(verse_ends[0]), int(verse_ends[1]) + 1):
            verses.append("{} {}:{}".format(
                m.group(1).strip(),
                m.group(3).strip(),
                str(i)))
        return verses
    else:
        return ["{} {}:{}".format(
            m.group(1).strip(),
            m.group(3).strip(),
            m.group(4).strip())]


if __name__ == '__main__':
    main()
