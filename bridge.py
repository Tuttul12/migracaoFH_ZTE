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

    if model == "AN5506" or "F612" or "F601":
        time.sleep(0.1)
        tn.write(b"configure terminal\n")
        retorno = tn.read_until(b"#", timeout=0.5).decode("ascii")
        print(retorno)
        time.sleep(0.1)
        tn.write(b"interface gpon-olt_1/2/"+pon_+b"\n")
        time.sleep(0.1)
        tn.write(b"onu "+num_+b" type F601 sn "+sn_+ b"\n")
        tn.write(b"exit \n")
        time.sleep(0.1)
        tn.write(b"interface gpon-onu_1/2/"+pon_+b":"+num_+b"\n")
        time.sleep(0.1)
        tn.write(b"description "+desc_+b"\n")
        time.sleep(0.1)
        tn.write(b"tcont 1 profile 1GB_UP \n")
        time.sleep(0.1)
        tn.write(b"gemport 1 tcont 1 \n")
        tn.write(b"gemport 1 traffic-limit downstream 1GB_DW \n")
        tn.write(b"service-port 1 vport 1 user-vlan 73 vlan 73 \n")
        tn.write(b"exit \n")
        time.sleep(0.1)
        tn.write(b"pon-onu-mng gpon-onu_1/2/"+pon_+b":"+num_+b"\n")
        time.sleep(0.1)
        tn.write(b"service 1 gemport 1 vlan 73 \n")
        time.sleep(0.1)
        tn.write(b"vlan port eth_0/1 mode tag vlan 73 \n")
        time.sleep(0.1)
        tn.write(b"end")
        print(f"ONU {sn} Provisionada!")

    else:
        time.sleep(0.1)
        tn.write(b"configure terminal\n")
        retorno = tn.read_until(b"#", timeout=0.5).decode("ascii")
        print(retorno)
        time.sleep(0.1)
        tn.write(b"interface gpon-olt_1/2/" + pon_ + b"\n")
        time.sleep(0.1)
        tn.write(b"onu " + num_ + b" type F601 sn " + sn_ + b"\n")
        tn.write(b"exit \n")
        time.sleep(0.1)
        tn.write(b"interface gpon-onu_1/2/" + pon_ + b":" + num_ + b"\n")
        time.sleep(0.1)
        tn.write(b"description " + desc_ + b"\n")
        time.sleep(0.1)
        tn.write(b"tcont 1 profile 1GB_UP \n")
        time.sleep(0.1)
        tn.write(b"gemport 1 tcont 1 \n")
        tn.write(b"gemport 1 traffic-limit downstream 1GB_DW \n")
        tn.write(b"service-port 1 vport 1 user-vlan 73 vlan 73 \n")
        tn.write(b"exit \n")
        time.sleep(0.1)
        tn.write(b"pon-onu-mng gpon-onu_1/2/" + pon_ + b":" + num_ + b"\n")
        time.sleep(0.1)
        tn.write(b"service 1 gemport 1 vlan 73 \n")
        time.sleep(0.1)
        tn.write(b"vlan port eth_0/1 mode tag vlan 73 \n")
        time.sleep(0.1)
        tn.write(b"security-mgmt 212 state enable mode forward protocol web \n")
        print(f"ONU {sn} provisionada!")