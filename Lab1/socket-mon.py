import csv
from collections import Counter
import psutil

def main():
     
 b = open('testsock.csv', 'w')
 a = csv.writer(b, quoting =csv.QUOTE_ALL) 
 a.writerow(['pid', 'laddr', 'raddr','status'])
 templ = "%s,%s,%s,%s  " 
 temp2 = "%s%s%s,%s%s%s,%s%s%s,%s%s%s "
 for conn in psutil.net_connections(kind='tcp'):
  if(conn.raddr != () and conn.laddr != ()):
   laddr = "%s@%s"%(conn.laddr)
   raddr = "%s@%s"%(conn.raddr)
   s_tuples = [(conn.pid,laddr,raddr,conn.status)]
   a.writerows(s_tuples)
 b.close()
 
  
 g = open ('testsock.csv','r')
 next(g)
 items =[data[0] for data in csv.reader(g,delimiter=',')]
 count= Counter(items)
 most_common = [item for item in count.most_common()]
 h = open ('writesock.csv','w')
 j = csv.writer(h,quoting =csv.QUOTE_ALL)
 for i in most_common: 
  q1 = i[0]
  q2 = i[1]
  count_tuples =[(q1, q2)]
  j.writerows(count_tuples)
 h.close() 
 g.close()
 
 file = open('testsock.csv','r')
 countfile = open('writesock.csv','r')
 
 next (file)

 print(templ % ('"pid"','"laddr"', '"raddr"','"status"'))
 for gr1 in csv.reader(countfile, delimiter =','):
  file = open('testsock.csv','r')
  for fr1 in csv.reader(file,delimiter = ','):
   if(gr1[0] == fr1[0]):
     print( temp2 % ('"',fr1[0],'"','"',fr1[1],'"','"',fr1[2],'"','"',fr1[3],'"'))
    
 file.close()
 countfile.close() 
      
if __name__ == '__main__':
    main()
	
	
