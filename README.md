# Instructions for Building BSA STEM Camp VM

Start with the base Ubuntu 18.04 image in VMDK format. https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.vmdk

See the `iso/boostrap` directory for examples of these files

Create a generic instance metadata file `meta-data` with the below content

```
instance-id: iid-local01
local-hostname: stembase
```

Create network configuration file `network-config` according to the below template

See: https://cloudinit.readthedocs.io/en/latest/topics/network-config-format-v2.html#network-config-v2
```
version: 2
ethernets:
  enp0s3:
    dhcp4: true
```

Create the customization configuration file `user-data` according to the below template

See: https://cloudinit.readthedocs.io/en/latest/topics/examples.html

```
#cloud-config
users:
  - name: scout
    passwd: $6$rounds=4096$ovnDJSxEla4JKP$7OEystJi28MGGNtnBtuK33BsuO3s1gx4VjwyLP2WpuoT5l7qpDnQqTwNHnH02hFm9axde5yjU3kDKK/47D3e10
    lock_passwd: false

packages:
  - python3
  - apache2
  ...
``` 

Create the cloud-init ISO

```
genisoimage -V cidata -R -J -o cidata.iso network-config user-data meta-data
```

Create a VirtualBox VM. Use the Ubuntu VMDK as a hard drive image and the cloud-init ISO as a CD drive image. The VM should have one network card and at least 1 vCPU and 2GB of memory.
