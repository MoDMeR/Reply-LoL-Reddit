# coding=utf-8
from subredditstylesheet import getchampionimages, getitemimages, getsummonerspells
from subredditstylesheet import resizeimages
from subredditstylesheet import cssgenerator
from riotapi import summoner, matchlist, match, champion, item
from converter import initializeconverters, championconverter, itemconverter, spellconverter, matchconverter

from converter import championconverter

#getchampionimages.getChampionImages()
#resizeimages.resizeImages()
#cssgenerator.createSingleChampionImage()
#cssgenerator.generateCode()
#cssgenerator.generateTestCode()

#getsummonerspells.getSummonerSpellsImages()
#getitemimages.getItemImages()
#resizeimages.resizeImages()
#cssgenerator.createSingleImage()
#cssgenerator.generateCode()
#cssgenerator.generateTestCode()



#response = summoner.requestSummoner({'t1nn3r'}, region='euw', byID=False)

#20267827 DAVID
#response = matchlist.requestMatchList(20267827, 'euw', championIds={1})

#response = match.requestMatch(2593714165, 'euw')

#print(response)

#test = 'CHALLENGER, MASTER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE, UNRANKED'

#splitString = test.split(' ')
#print(splitString)
#result = ''
#for string in splitString:
#    template = "'{add}': '{add}', "
#    subResult = template.format(add=string)
#    result += subResult
#print(result[:-2])

#champion.updateChampionDictionary()
#print(champion.championDictionaryById)
#print(champion.championDictionaryByName)

item.updateItemDictionary()
initializeconverters.initializeConverters()
print(itemconverter.itemDictionary)
print(itemconverter.itemConverter)