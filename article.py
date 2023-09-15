#Custom article type
class article():
  def __init__(self,id,title,creation_date,journal,year,abstract,citation_count,doi,keywords):
    self.id=id
    self.title=title
    self.creation_date=creation_date
    self.journal=journal
    self.year=year
    self.abstract=abstract
    self.citation_count=citation_count
    self.doi=doi
    self.keywords=keywords
