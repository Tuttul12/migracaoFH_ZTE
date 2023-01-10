import paramiko
import os
import pandas as pd
import time

df = pd.read_csv('teste.csv')
address = '10.7.0.66'
login = "noc"
passwd= "6O7noNaoiMClIn7e"
con = paramiko.SSHClient()
con.set_missing_host_key_policy(paramiko.AutoAddPolicy())

con.connect(address, port = 22, username = login, password = passwd , timeout= 3)
for i,linhas in df.iterrows():
    if 'AN5506' in df.loc[i,'MODELO']:
        try:
            stdin, stdout, stderr = con.exec_command("conf t")
            stdin, stdout,stderr = con.exec_command("interface gpon-olt_",df.loc[i, 'PON'])
            stdin, stdout,stderr = con.exec_command("onu "+ df.loc[i, 'NUMERO'] +" type F601 sn "+ df.loc[i, 'SERIAL'])
            stdin, stdout,stderr = con.exec_command("exit")
            stdin, stdout,stderr = con.exec_command("interface gpon-onu_2: " + df.loc[i, 'NUMERO'])
            stdin, stdout,stderr = con.exec_command("description "+ df.loc[i, 'DESCRIPTION'])
            stdin, stdout,stderr = con.exec_command("tcont 1 profile 1GB_UP")
            stdin, stdout,stderr = con.exec_command("gemport 1 tcont 1")
            stdin, stdout,stderr = con.exec_command("gemport 1 traffic-limit downstream 1GB_DW")
            stdin, stdout,stderr = con.exec_command("service-port 1 vport 1 user-vlan  70 vlan  70")
            stdin, stdout,stderr = con.exec_command("exit")
            stdin, stdout,stderr = con.exec_command("pon-onu-mng gpon-onu_"+ df.loc[i,'PON'] +":"+ df.loc[i, 'NUMERO'])
            stdin, stdout,stderr = con.exec_command("service 1 gemport 1 vlan 70;")
            stdin, stdout,stderr = con.exec_command("vlan port eth_0/1 mode tag vlan 70")
            print(stdout.read().decode('ascii'))
            con.close()
        except:
            print("Falha no:", df.loc[i,'DESCRIPTION'], df.loc[i, 'MODELO'])
    else:
        try:
            stdin, stdout, stderr = con.exec_command("conf t")
            stdin, stdout, stderr = con.exec_command("interface gpon-olt_",df.loc[i, 'PON'])
            stdin, stdout,stderr = con.exec_command("onu"+ df.loc[i, 'NUMERO'] +"type F601 sn "+ df.loc[i, 'SERIAL'])
            stdin, stdout,stderr = con.exec_command("exit")
            stdin, stdout,stderr = con.exec_command("interface gpon-onu_"+ df.loc[i, 'SERIAL'])
            stdin, stdout,stderr = con.exec_command("description " + df.loc[i, 'DESCRIPTION'])
            stdin, stdout,stderr = con.exec_command("tcont 1 profile 1GB_UP")
            stdin, stdout,stderr = con.exec_command("gemport 1 tcont 1")
            stdin, stdout,stderr = con.exec_command("gemport 1 traffic-limit downstream 1GB_DW")
            stdin, stdout,stderr = con.exec_command("service-port 1 vport 1 user-vlan 70 vlan 70")
            stdin, stdout,stderr = con.exec_command("exit")
            stdin, stdout,stderr = con.exec_command("pon-onu-mng gpon-onu_"+ df.loc[i,'PON']+":"+df.loc[i, 'NUMERO'])
            stdin, stdout,stderr = con.exec_command("service 1 gemport 1 vlan 70;")
            stdin, stdout,stderr = con.exec_command("vlan port eth_0/1 mode tag vlan 70")
            stdin, stdout,stderr = con.exec_command("security-mgmt 212 state enable mode forward protocol web")
        except:
            print("Falha no:", df.loc[i,'DESCRIPTION'], df.loc[i, 'MODELO'])
            con.close()
