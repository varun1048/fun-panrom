import os
import requests 
import bs4
from playsound import playsound 
os.system("cls")
url = "https://www.olx.in/"
res = requests.get(url)   
print(res.status_code)
# def masstamilan(album_name)->None:
#     album_name = album_name.replace(" ","-")
#     url = f"https://masstamilan.in/{album_name}/"
#     try:
#         response = requests.get(url)    
#     except:
#         print("Ennama neenga ippadi panreengale ma. Olunga name ah type pannunga ma.")
#         return None

#     # print(response)
    
#     soup  = bs4.BeautifulSoup(response.text,features="html.parser")
#     if soup.title.string == "Masstamilan | Latest World News Update And High Quality Tamil Mp3 Songs":
#         print("Ennama neenga ippadi panreengale ma. Olunga name ah type pannunga ma.")
#         return None

    
#     try:
#         out=soup.find(class_="info").p.get_text()
#         print(out)
#         print("\n\n")
#     except Exception as err:
#         print(err)
    
    
    
    
    
#     filterName = lambda name : "".join((x  for x in name if x != "\t" and x != "\n" ))
    
#     songs_name = map( lambda x : filterName(x.string)   ,soup.find_all(class_="nostyle"))
#     songs_name = list(songs_name)
    
#     artist = map( lambda x : x.string   ,soup.find_all(itemprop="byArtist"))
#     artist = list(artist)
     
    
#     songs_Link = filter(lambda x: filterName(x.string) == "320kbps", soup.find_all(class_="dlink anim") ) 
#     songs_Link = list(songs_Link)
    
#     songs_info = []
#     if len( songs_Link  ) == len( songs_name  ):
#         for i in range(len(  songs_Link )):
#             songs_info.append({
                
#                 "name" :  songs_name[i],
#                 "artist" : artist[i],
#                 "link" :songs_Link[i]["href"]
                
#             })
  
#     else:
#         print("songs_Link and songs_name not same")
#         return None
        
    
#     for i in range(len( songs_info) ): 
#         print(f"{i}\t{songs_info[i]['name']}")
#         print(f"\t\t{songs_info[i]['artist']}")
    
#     try:
#         inner = int(input("song number to play :"))
#         # inner = 1
    
#     except  Exception as err:
#         print("Oops!\t", err.__class__, " occurred. at Download")
#         return None
#     if inner < len(songs_info):
        
#         temp="temp.mp3"
#         os.remove("temp.mp3")
#         res = requests.get(songs_info[inner]["link"])
#         # print(res)
#         with open(temp,'wb') as file:
#             file.write(res.content)
        
#         print("playing .....")
#         playsound(temp)        
#     else:
#         print("invalid")
#         return None
        


    


# masstamilan(input("Album name :"))
# # masstamilan("beast")
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # filterName = lambda name : "".join((x  for x in name if x != "\t" and x != "\n" ))
    # songs= []
    # for x in soup.tbody.find_all("tr")[1:]:
        
    #     songs.append({
    #         "name": filterName(x.find(itemprop="name").string),
    #         "artist": x.find(itemprop="byArtist").string,
    #         "link":x.find_all(class_="dlink anim")[1]['href']
    #     })
    
    # for x in songs:
    #     print(x)      