import telnetlib
import pandas as pd
import time

df = pd.read_csv('PON arcos-14 - Página1.csv')

HOST = '10.7.0.66'
user = 'noc'
password = '6O7noNaoiMClIn7e'

tn= telnetlib.Telnet(HOST, 23)
tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")
time.sleep(1)
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")

def separa():
    print("-----------------------------------------")

def bridge():
    time.sleep(0.1)
    tn.write(b"configure terminal\n")
    retorno = tn.read_until(b"#", timeout=0.5).decode("ascii")
    print(retorno)
    time.sleep(0.1)
    tn.write(b"interface gpon-olt_1/4/" + pon_ + b"\n")
    time.sleep(0.1)
    tn.write(b"onu " + num_ + b" type F601 sn " + sn_ + b"\n")
    tn.write(b"exit \n")
    time.sleep(0.1)
    tn.write(b"interface gpon-onu_1/4/" + pon_ + b":" + num_ + b"\n")
    time.sleep(0.1)
    tn.write(b"description " + desc_ + b"\n")
    time.sleep(0.1)
    tn.write(b"tcont 1 profile 1GB_UP \n")
    time.sleep(0.1)
    tn.write(b"gemport 1 tcont 1 \n")
    tn.write(b"gemport 1 traffic-limit downstream 1GB_DW \n")
    tn.write(b"service-port 1 vport 1 user-vlan 70 vlan 70 \n")
    tn.write(b"exit \n")
    time.sleep(0.1)
    tn.write(b"pon-onu-mng gpon-onu_1/4/" + pon_ + b":" + num_ + b"\n")
    time.sleep(0.1)
    tn.write(b"service 1 gemport 1 vlan 70 \n")
    time.sleep(0.1)
    tn.write(b"vlan port eth_0/1 mode tag vlan 70 \n")
    time.sleep(0.1)
    tn.write(b"end \n")
    print(f"ONU {sn} Provisionada!\n\n")
    separa()


def pppoe():
    time.sleep(0.1)
    tn.write(b"configure terminal\n")
    retorno = tn.read_until(b"#", timeout=0.5).decode("ascii")
    print(retorno)
    time.sleep(0.1)
    tn.write(b"interface gpon-olt_1/4/" + pon_ + b"\n")
    time.sleep(0.1)
    tn.write(b"onu " + num_ + b" type F601 sn " + sn_ + b"\n")
    tn.write(b"exit \n")
    time.sleep(0.1)
    tn.write(b"interface gpon-onu_1/4/" + pon_ + b":" + num_ + b"\n")
    time.sleep(0.1)
    tn.write(b"description " + desc_ + b"\n")
    time.sleep(0.1)
    tn.write(b"tcont 1 profile 1GB_UP \n")
    time.sleep(0.1)
    tn.write(b"gemport 1 tcont 1 \n")
    tn.write(b"gemport 1 traffic-limit downstream 1GB_DW \n")
    tn.write(b"service-port 1 vport 1 user-vlan 70 vlan 70 \n")
    tn.write(b"exit \n")
    time.sleep(0.1)
    tn.write(b"pon-onu-mng gpon-onu_1/4/" + pon_ + b":" + num_ + b"\n")
    time.sleep(0.1)
    tn.write(b"service 1 gemport 1 vlan 70 \n")
    time.sleep(0.1)
    tn.write(b"vlan port eth_0/1 mode tag vlan 70 \n")
    time.sleep(0.1)
    tn.write(b"security-mgmt 212 state enable mode forward protocol web \n")
    time.sleep(0.1)
    tn.write(b"end \n")
    print(f"ONU {sn} provisionada!\n\n")
    separa()

def bridge2portas():
    time.sleep(0.1)
    tn.write(b"configure terminal\n")
    retorno = tn.read_until(b"#", timeout=0.5).decode("ascii")
    print(retorno)
    time.sleep(0.1)
    tn.write(b"interface gpon-olt_1/4/" + pon_ + b"\n")
    time.sleep(0.1)
    tn.write(b"onu " + num_ + b" type F612 sn " + sn_ + b"\n")
    tn.write(b"exit \n")
    time.sleep(0.1)
    tn.write(b"interface gpon-onu_1/4/" + pon_ + b":" + num_ + b"\n")
    time.sleep(0.1)
    tn.write(b"description " + desc_ + b"\n")
    time.sleep(0.1)
    tn.write(b"tcont 1 profile 1GB_UP \n")
    time.sleep(0.1)
    tn.write(b"gemport 1 tcont 1 \n")
    tn.write(b"gemport 1 traffic-limit downstream 1GB_DW \n")
    tn.write(b"service-port 1 vport 1 user-vlan 70 vlan 70 \n")
    tn.write(b"exit \n")
    time.sleep(0.1)
    tn.write(b"pon-onu-mng gpon-onu_1/4/" + pon_ + b":" + num_ + b"\n")
    time.sleep(0.1)
    tn.write(b"service 1 gemport 1 vlan 70 \n")
    time.sleep(0.1)
    tn.write(b"vlan port eth_0/1 mode tag vlan 70 \n")
    time.sleep(0.1)
    tn.write(b"vlan port eth_0/2 mode tag vlan 70 \n")
    time.sleep(0.1)
    tn.write(b"end \n")
    print(f"ONU {sn} Provisionada!\n\n")
    separa()

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

    if "AN5506" in df.loc[i, 'MODELO']:
        print("executando script para Fiberhome")
        bridge2portas()

    elif "F612" in df.loc[i, 'MODELO']:
        print("executando script para ZTE F612")
        bridge2portas()

    elif "F601" in df.loc[i, 'MODELO']:
        print("executando script para ZTE F601")
        bridge()

    elif "F680" in df.loc[i, 'MODELO']:
        print("executando script para ZTE F680")
        pppoe()

    elif "HS" in df.loc[i, 'MODELO']:
        print("executando script para HUAWEI HS")
        pppoe()

    elif "HG" in df.loc[i, 'MODELO']:
        print("executando script para HUAWEI HG")
        pppoe()
    elif "F670" in df.loc[i, 'MODELO']:
        print("executando script para ZTE F680")
        pppoe()
    elif "F660" in df.loc[i, 'MODELO']:
        print("executando script para ZTE F680")
        pppoe()
    else:
        print(f"{sn} É de outro modelo")
        tn.close()

tn.close()