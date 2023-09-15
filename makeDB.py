import sys
import urllib.request
import json
import pickle
import article

#Makes a database of all citations based on a paper or list of papers
paperIDs=["85292"]
dbName="Freedman.pkl"

paperDB=[]
idsInDict=[]
for paperID in paperIDs:
  #Get total number of published articles citing this one
  apiCall = "https://inspirehep.net/api/literature/?q=refersto%3Arecid%3A"+paperID+"&doc_type=published&doc_type=article"
  data = json.loads(urllib.request.urlopen(apiCall).read())
  nCitations=data["hits"]["total"]
  print(nCitations)
  
  #Limited to 1000 results in inspire-hep API
  if nCitations>1000:
    nCitations=1000

  if nCitations==0:
    continue
    
  #Make ths call -- we sort by most cited to get top 1000 articles if more are present
  apiCall="https://inspirehep.net/api/literature/?q=refersto%3Arecid%3A"+paperID+"&doc_type=published&doc_type=article&size="+str(nCitations)+"&sort=mostcited"
  data = json.loads(urllib.request.urlopen(apiCall).read())
  
  #Step through, loading relevant data into a custom "article" objects. We skip this an article if any category is missing except for keywords
  for icitation,citation in enumerate(data["hits"]["hits"]):
    
    if "id" in citation:
      id=citation["id"]
      if id in idsInDict:
        continue
      else:
        idsInDict.append(id)
        
    if "titles" in citation["metadata"]:
      titles=citation["metadata"]["titles"]
      if len(titles)>0:
        title=titles[0]["title"]
      else:
        continue
    else:
      continue
      
    if "created" in citation:
      creation_date=citation["created"]
    else:
      continue
      
    if "publication_info" in citation["metadata"]:
      publicationInfos=citation["metadata"]["publication_info"]
      if len(publicationInfos)>0:
        if "journal_title" in publicationInfos[0]:
          journal_title=publicationInfos[0]["journal_title"]
        else:
          continue
        if "year" in publicationInfos[0]:
          year=publicationInfos[0]["year"]
        else:
          continue
      else:
        continue
    
    if "abstracts" in citation["metadata"]:
      abstracts=citation["metadata"]["abstracts"]
      if len(abstracts)>0:
        abstract=abstracts[0]["value"]
      else:
        continue
    else:
      continue
          
    if "citation_count" in citation["metadata"]:
      citation_count=citation["metadata"]["citation_count"]
    else:
      continue
      
    if "dois" in citation["metadata"]:
      dois=citation["metadata"]["dois"]
      if len(dois)>0:
        doi=dois[0]
      else:
        continue
    else:
      continue
      
    keywords=[]
    if "keywords" in citation["metadata"]:
      queriedKeywords=citation["metadata"]["keywords"]
      for queriedKeyword in queriedKeywords:
        keywords.append(queriedKeyword["value"])
    
    paperDB.append(article.article(id,title,creation_date,journal_title,year,abstract,citation_count,doi,keywords))
    
    #pretty print query, for debugging
    #print(json.dumps(citation,sort_keys=True,indent=1))

with open(dbName, 'wb') as f:
  pickle.dump(paperDB, f)
