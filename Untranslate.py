from random import randint
from googletrans import Translator;
import time;
import googletrans;


def Mangle(Original_text, TimesMangled):

    sText = Original_text;
    translator = Translator();
    KeyCollection = googletrans.constants.LANGCODES;
    KeyList = list(KeyCollection.values());
    listLength = len(KeyList);
    print("Starting Sentance: ", sText);

    for x in range(0, TimesMangled):
        varff = randint(0, listLength);
        text = translator.translate(sText, KeyList[varff]).text;
        sText = text;
        print("Tranlation:", x, "#", sText);
        time.sleep(2);
    sText = translator.translate(sText, 'en');
    return sText;



MangledText = Mangle('I ordered the strawberry tart with whipped cream and a lemon tea with a dash of brown sugar and honey', 5);
print(MangledText.text);
    



