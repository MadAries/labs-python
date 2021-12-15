#3.1
print('lab3.1')
string = 'FastEthernet0/1'
print(string.replace('Fast', 'Gigabit'))
#3.2
print('lab3.2')
MAC = 'AAAA:BBBB:CCCC'
print(MAC.replace(':', '.'))
#3.3
print('lab3.3')
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
array = CONFIG.split()
print(array[-1].split(','))
#3.4
print('lab3.4')
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
setVlans = set(((command1.split())[-1]).split(',') + ((command2.split())[-1]).split(','))
print(list(setVlans))
#3.5
print('lab3.5')
vlans = '10,20,30,1,2,100,10,30,3,4,10'
vlansList = list(set((vlans).split(',')))
vlansList.sort()
print(vlansList)
#3.6
print('lab3.6')
ospf_route = 'O     10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_routeArray = ospf_route.split();
prefix = ospf_routeArray[1];
adMetric = ospf_routeArray[2].strip();
nextHop = ospf_routeArray[4].strip();
lastUpdate = ospf_routeArray[-2].strip();
outboundInterface = ospf_routeArray[-1];
print(
    'Protocol:\t\t\tOSPF\n'
    'Prefix:\t\t\t\t'+prefix+'\n'+
    'AD/Metric:\t\t\t'+adMetric+'\n'+
    'Next-Hop:\t\t\t'+nextHop+'\n'+
    'Last update:\t\t'+lastUpdate+'\n'+
    'Outbound Interface:\t'+outboundInterface
)
#3.7
print('lab3.7')
MAC = 'AAAA:BBBB:CCCC'
print(bin(int(MAC.replace(':', ''), 16)))
#3.8
print('lab3.8')
IP = '192.168.1.5'.split('.')
print(''.join(format(int(i), '10d') for i in IP))
print(''.join(format(int(i), '10b') for i in IP))
#3.9
print('lab3.9')
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['sad', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl' ]
element_word_list = 'python'
element_num_list = 10
print(len(word_list) - (word_list[::-1]).index(element_word_list) - 1)
print(len(num_list) - (num_list[::-1]).index(element_num_list) - 1)