#subtitles downloader

import os,requests,bs4
import sys
from zipfile import ZipFile #pip install zipfile
import zipfile
n=input("Enter the name of Movie / Series: ")
r=requests.get("https://isubtitles.in/search?kwd="+n)

bs=bs4.BeautifulSoup(r.text,"html.parser")

link=bs.select(".col-lg-18 h3 a")


a=1
for i in link:
    print(str(a)+" "+i.get("title"))

    
    a=a+1
print("=====================================================================")
n1=int(input("Enter the number of movie : "))
file_name=link[n1-1].get("title")+".zip"
####################################################################################

r1=requests.get("https://isubtitles.in"+(link[n1-1].get("href")))

bs0=bs4.BeautifulSoup(r1.text,"html.parser")

link1=bs0.select(".dropdown-menu-large .col-sm-8 ul li a")
b=1
for i in link1:
    print(str(b)+" "+i.get("href"))
    b=b+1

print("=======================================================================")
n2=int(input("Enter the number of subtitle : "))

###################################################################################

r2=requests.get("https://isubtitles.in"+(link1[n2-1].get("href")))
# print(r2)
bs1=bs4.BeautifulSoup(r2.text,"html.parser")
link2=bs1.select(".movie-release a")
# b=1
print("The url for your subtitle file is : "+"https://isubtitles.in"+link2[0].get("href"))
print("Your subtitle is downloaded .")
###################################################################################


# print(file_name)
r3=requests.get("https://isubtitles.in/"+"download"+link2[0].get("href"))
with open(f"{file_name}", 'wb') as file:
    file.write(r3.content)
    print("\n" + file_name + " succesfully downloaded ")
    

with zipfile.ZipFile(f"{file_name}", "r") as zip_ref:
    zip_ref.extractall("E:\\Subtitles")
    
os.remove(file_name)
# o4=open(file_name,"wb")
# print(o4)
# o4.write(r3.content)
# print(o4)
# o4.close()

