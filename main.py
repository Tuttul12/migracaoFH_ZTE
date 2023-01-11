import getpass
import telnetlib
import pandas as pd
import time

df = pd.read_csv('teste.csv')
HOST = '10.7.0.66'
user = input("Digite o login: ")
password= getpass.getpass()

tn= telnetlib.Telnet(HOST)

tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")
time.sleep(1)
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")

for i,linhas in df .iterrows():
    sn= df.loc[i, 'SERIAL']
    num= df.loc[i, 'NUMERO']
    pon= df.loc [i, 'PON']
    desc= df.loc[i, 'DESCRIPTION']
    model= df.loc[i, 'MODELO']

    sn_ = bytes(sn, 'ascii')
    num1 = str(num)
    num_ = bytes(num1, 'ascii')
    pon1 = str(pon)
    pon_ = bytes(pon1, 'ascii')
    desc_ = bytes(desc, 'ascii')
    if 'AN5506' in model:
        time.sleep(1)
        tn.write(b"configure terminal\n")
        print("conf t")
        time.sleep(1)
        tn.write(b"interface gpon-olt_1/2/"+pon_)
        print("interface gpon-olt_1/2/",pon)
        time.sleep(1)
        tn.write(b"\n")
        time.sleep(1)
        tn.write(b"onu "+num_)
        time.sleep(1)
        tn.write(b" type F601 sn "+sn_)
        time.sleep(1)
        tn.write(b"\n")
        print("onu type F601 sn",sn)
        time.sleep(1)
        tn.write(b"exit\n")
        print("exit")
        time.sleep(1)
        tn.write(b"interface gpon-onu_1/2/"+pon_)
        time.sleep(1)
        tn.write(b":"+num_)
        time.sleep(1)
        tn.write(b"\n")
        print("interface gpon-onu_",pon)
        time.sleep(1)
        tn.write(b"description "+desc_)
        tn.write(b"\n")
        print("description",desc)
        time.sleep(1)
        tn.write(b"tcont 1 profile 1GB_UP\n")
        print("tcont 1 profile 1GB_UP")
        time.sleep(1)
        tn.write(b"gemport 1 tcont 1\n")
        print("gemport 1 tcont 1")
        time.sleep(1)
        tn.write(b"gemport 1 traffic-limit downstream 1GB_DW\n")
        print("gemport 1 traffic-limit downstream 1GB_DW")
        time.sleep(1)
        tn.write(b"service-port 1 vport 1 user-vlan 70 vlan 70\n")
        print("service-port 1 vport 1 user-vlan 70 vlan 70")
        time.sleep(1)
        tn.write(b"exit\n")
        print("exit")
        time.sleep(1)
        tn.write(b"pon-onu-mng gpon-onu_1/2/"+pon_)
        time.sleep(1)
        tn.write(b":"+num_)
        time.sleep(1)
        tn.write(b"\n")
        print("pon-onu-mng gpon-onu",pon)
        tn.write(b"service 1 gemport 1 vlan 70\n")
        print("service 1 gemport 1 vlan 70")
        time.sleep(1)
        tn.write(b"exit\n")
        print("exit")
        print("ONU Autorizada!")
