import os.path
import csv

ParserData={
	"HeaderDivHtml":(soup.find_all('div',{"class":"graybar"})),
	"MainContentDivHtml":(soup.find_all('div',{"class":"sitemap-menu-box"})),
	"FooterDivHtml":(soup.find_all('div',{"class":"footer-band-align"})),
	"SocialDivHtml":(soup.find_all('div',{"class":"bottomfooter-align"})),
	}	
url= 'http://stackoverflow.uk.co/questions/339537/end-line-characters-from-lines-read-from-text-file-using-python'
new=url.split("//")[-1].split("/")[0]
print (new)





