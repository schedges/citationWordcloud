import pickle
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import article

dbName="Freedman.pkl"
wordcloudType="abstract" #"abstract" or "keywords"

stopwords = set(STOPWORDS)
#Words to skip
other_stopwords=["display","mn","mrow","mo","mi","math display",
                 "inline","mtext","stretchy","math","CE","altimg",
                 "msub","false","value","parameter","using","msup",
                 "multiscripts","mathvariant","normal","L","two","S",
                 "three","u","C","several","U","_","N","g","B","e","m",
                 "linebreak","badbreak","mprescripts","none","mmultiscripts",
                 "mml","id","p","textrm",">","d","Dz","Mc","msubsup"]
stopwords.update(other_stopwords)

title=dbName.split(".")[0]
with open(dbName, 'rb') as f:
  paperDB = pickle.load(f)

data=""
for paper in paperDB:
  if wordcloudType=="abstract":
    data+=" "+paper.abstract
  elif wordcloudType=="keywords":
    for keyword in paper.keywords:
      data+=" "+keyword
  else:
    data=""
  
wc = WordCloud(stopwords=stopwords,background_color = 'white', width = 1920, height = 1080)
wc.generate_from_text(data)
wc.to_file(title+"_"+wordcloudType+".png")
#plt.imshow(wc)
#plt.show()
