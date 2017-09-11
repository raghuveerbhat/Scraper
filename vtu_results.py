from urllib.request import urlopen as uo
from bs4 import BeautifulSoup as bs

link = 'http://results.vtu.ac.in/results17/result_page.php?usn=1rn14cs'
t = link
#.csv file writer
f = open("Res.csv","w")
f.write("NAME" + "," + "USN" + "," + "MARKS" + "\n")

#link = link + '078'
for i in range(0,400):
    link = link + str(i).zfill(3)
    print(link)
    results_client = uo(link)
    results_html = results_client.read()
    results_client.close()
    r_soup = bs(results_html, "html.parser")
    try:
        usn = r_soup.findAll("div", {"class":"col-md-12"})[3].findAll("td", {"style":"padding-left:15px;text-transform:uppercase"})[0].text.replace(":","").strip()
        name = r_soup.findAll("div", {"class":"col-md-12"})[3].findAll("td", {"style":"padding-left:15px"})[0].text.replace(":","").strip()
        marks = r_soup.findAll("table", {"style":"margin-left:30px;margin-bottom:5px;font-family:Times New Roman;font-size:12pt;"})[0].findAll("td", {"style":"padding-left:10px"})[0].b.text.replace(":","").strip()
        print(usn+"--->"+marks)
        f.write(name + "," + usn + "," + marks + "\n")
    except:
        usn = link[-10:]
        print("error! "+usn+" not found")
    link = t
