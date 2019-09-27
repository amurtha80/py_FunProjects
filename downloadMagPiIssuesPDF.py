#import relevant libraries for program execution
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

#base url for MagPi magazine issues
url = "https://www.raspberrypi.org/magpi-issues/"

#if the target destination folder does not exist, then create one
folder_dest = r'/home/pi/MagPi'
if not os.path.exists(folder_dest):os.mkdir(folder_dest)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select('a[href$=".pdf"]'):
        #Name the pdf files using the last portion of each link which are
        #    unique in this case
        filename = os.path.join(folder_dest,link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)
else:
    #Get list of filenames from folder_dest
    existingFiles = os.listdir(path=folder_dest)
    existingFiles.sort()
    #Get list of filenames from website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    potentialFile = []
    for link in soup.select('a[href$=".pdf"]'):
        temp = link['href']
        potentialFile.append(temp)
        
    potentialFile.sort()
    
    #Compare existing files to potential files and return filenames not in
    #    existing files
    diff = list(set(potentialFile) - set(existingFiles))
    diff.sort()
    
    for i in diff:
        #Name the pdf files using the last portion of each link which are
        #    unique in this case
        filename = os.path.join(folder_dest,diff[-1])
        with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,diff)).content)
