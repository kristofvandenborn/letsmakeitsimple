
# Basic Cisco Switch Configuration Guide

This guide outlines the essential steps for configuring a Cisco switch, including general setup, security hardening, remote management, logging, time synchronization, and network monitoring.

---

## 📘 Table of Contents

1. [Initial Configuration](#1-initial-configuration)
2. [Security Hardening](#2-security-hardening)
3. [Remote Management](#3-remote-management)
4. [MOTD Banner](#4-motd-banner)
5. [Syslog Configuration](#5-syslog-configuration)
6. [SNMP Setup](#6-snmp-setup)
7. [NTP Configuration](#7-ntp-configuration)
8. [Visual Diagrams](#8-visual-diagrams)

---

## 1. Initial Configuration

```bash
Switch> enable
Switch# configure terminal
Switch(config)# hostname Switch1
Switch1(config)# enable secret StrongPassword123

Switch1(config)# line console 0
Switch1(config-line)# password consolePass
Switch1(config-line)# login
Switch1(config-line)# exit

Switch1(config)# interface range Fa0/1 - 2
Switch1(config-if-range)# description PCs
Switch1(config-if-range)# switchport access vlan 10
Switch1(config-if-range)# no shutdown
Switch1(config-if-range)# exit

Switch1(config)# interface vlan 1
Switch1(config-if)# ip address 192.168.1.2 255.255.255.0
Switch1(config-if)# no shutdown
Switch1(config-if)# exit
```

---

## 2. Security Hardening

```bash
Switch1(config)# interface range Fa0/3 - 24
Switch1(config-if-range)# shutdown
Switch1(config-if-range)# switchport access vlan 999
Switch1(config-if-range)# exit

Switch1(config)# interface Fa0/1
Switch1(config-if)# switchport port-security
Switch1(config-if)# switchport port-security maximum 2
Switch1(config-if)# switchport port-security violation restrict
Switch1(config-if)# switchport port-security mac-address sticky
Switch1(config-if)# exit

Switch1(config)# service password-encryption
```

![Security Hardening](security_hardening.png)

---

## 3. Remote Management (SSH)

```bash
Switch1(config)# ip domain-name example.com
Switch1(config)# crypto key generate rsa
How many bits in the modulus [512]: 1024

Switch1(config)# username admin secret AdminPass123

Switch1(config)# line vty 0 4
Switch1(config-line)# transport input ssh
Switch1(config-line)# login local
Switch1(config-line)# exit
```

![Remote SSH Access](remote_ssh_access.png)

---

## 4. MOTD Banner

```bash
Switch1(config)# banner motd #Unauthorized access is prohibited!#
```

---

## 5. Syslog Configuration

```bash
Switch1(config)# logging 192.168.1.100
Switch1(config)# logging trap warnings
Switch1(config)# logging source-interface vlan 1   ! optional
```

![Encryption + Logging](encryption_logging.png)

---

## 6. SNMP Setup

```bash
! SNMPv2c
Switch1(config)# snmp-server community public RO

! SNMPv3 (example)
Switch1(config)# snmp-server group SNMPv3Group v3 priv
Switch1(config)# snmp-server user SNMPv3User SNMPv3Group v3 auth md5 AuthPass123 priv aes 128 PrivPass123
Switch1(config)# snmp-server enable traps
Switch1(config)# snmp-server contact admin@example.com
Switch1(config)# snmp-server location DataCenter1
```

---

## 7. NTP Configuration

```bash
Switch1(config)# ntp server 192.168.1.50
Switch1(config)# clock timezone PST -8
Switch1(config)# show clock
Switch1(config)# show ntp status
```

![NTP Time Sync](ntp_time_sync.png)

---

## 8. Visual Diagrams

- [x] Basic Switch Setup  
  ![Basic Switch Setup](basic_switch_setup.png)
- [x] Security Hardening  
  ![Security Hardening](security_hardening.png)
- [x] Remote SSH Access  
  ![Remote SSH Access](remote_ssh_access.png)
- [x] Syslog & SNMP Server Diagram  
  ![Encryption + Logging](encryption_logging.png)
- [x] NTP Time Sync Topology  
  ![NTP Time Sync](ntp_time_sync.png)

---

✅ **End of Configuration Guide**
