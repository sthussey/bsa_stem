# Instructions for Building BSA STEM Camp VM

1. Start with the base Ubuntu 18.04 image in VMDK format. https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.vmdk
1. Create network configuration file `network-config` according to the below template

```
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: true
```

1. Create the customization configuration file `user-data` according to the below template

```
#cloud-config
users:
  - name: scout
    passwd: $6$rounds=4096$ovnDJSxEla4JKP$7OEystJi28MGGNtnBtuK33BsuO3s1gx4VjwyLP2WpuoT5l7qpDnQqTwNHnH02hFm9axde5yjU3kDKK/47D3e10
    lock_passwd: false

packages:
  - python3
  - apache2
  - mariadb-server
  - mariadb-client 
``` 

1. Create the cloud-init ISO

```
genisoimage -V cidata -R -J -o cidata.iso network-config user-data
```
