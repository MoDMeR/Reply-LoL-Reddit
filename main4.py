# coding=utf-8
import init
from converter import championconverter, itemconverter, spellconverter
from riotapi import matchlist, match
from displayreddit import drmatch, drouttro

init.init()

#20267827 David
#2634415570 match 2770739260

matchString = match.requestMatch(2634415570, 'euw')
print(drmatch.drMatch(matchString) + drouttro.getOuttro())


