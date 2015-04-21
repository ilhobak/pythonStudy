# -*- coding: utf-8 -*-

from xml.etree.ElementTree import parse

# tree = parse("cha_asr_mdl_HistoryTest.xml")
tree = parse("note.xml")
note = tree.getroot()

print note

# print note.get("date")
# print note.get("foo","default")
# print note.keys()
# print note.items()


from_text = note.findtext("author")

print from_text

