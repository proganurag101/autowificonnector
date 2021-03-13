import os
import sys
saved_profiles = os.popen("netsh wlan show profiles").read()
print(saved_profiles)
aval_profiles = os.popen("netsh wlan show networks").read()
print(aval_profiles)
inp_pref_network = input("Enter the preferred wifi for your connection: ")
disconn_network = os.popen("netsh wlan disconnect").read()
print(disconn_network)
if inp_pref_network not in saved_profiles:
    print("profile for"+inp_pref_network+"is not saved in system")
    print("sorry but the connection can not be made")
    sys.exit()
else:
    print("profile for "+inp_pref_network+" is saved in system")
while True:
    avail = os.popen("netsh wlan show networks").read()
    if inp_pref_network in avail:
        print("Network found!")
        break

print("------------connecting-------")
resp = os.popen('netsh wlan connect name ='+'"'+inp_pref_network+'"').read()
print(resp)

print("Sir/Ma'am,You're connected!")