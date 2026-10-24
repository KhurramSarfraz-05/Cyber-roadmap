# Cyber Roadmap

My 2-month journey to become eligible for a cybersecurity fresher role (Penetration Testing / Red Teaming).

## About me
Cybersecurity student focused on offensive security. Building hands-on skills in penetration testing, network and web application security through free, legal labs (personal VMs, OverTheWire, picoCTF).

## Progress
- [x] Phase 1: Networking fundamentals
- [ ] Week 2: Linux + Pentest Methodology + Recon/Scanning (in progress)
- [ ] Weeks 3-4: Web Security + Burp Suite
- [ ] Weeks 5-6: Tools + CTFs / VulnHub machines
- [ ] Weeks 7-8: Portfolio and projects

## Week 2 progress (Linux + Recon)
- [x] Lab setup: Kali Linux (attacker) + Metasploitable 2 (target) on VirtualBox, isolated host-only network, clean snapshots
- [x] Workflow: tmux, structured notes
- [x] Linux: basics and kernel, terminal navigation, file system hierarchy, file management, text editors (nano/vim), users/groups/sudo
- [x] Pentest methodology: 5 phases, scope and authorization, Cyber Kill Chain, MITRE ATT&CK
- [x] OverTheWire Bandit: levels 0-11 (in progress)
- [x] Passive vs active recon, OSINT basics (whois, dig, theHarvester, crt.sh)
- [ ] Linux: permissions, processes, packages, services, networking commands, logs, SSH
- [ ] nmap: scan types, service/version detection, NSE scripts
- [ ] Web recon: nikto, gobuster/ffuf
- [ ] Writeup #1: complete recon of Metasploitable 2

## Lab setup
| Machine | Role | Network |
|---|---|---|
| Kali Linux | Attacker | NAT + Host-only |
| Metasploitable 2 | Intentionally vulnerable target | Host-only (isolated) |

The vulnerable VM is never exposed to a real network.

## Folders
- `01-networking/` : IP, ports, DNS, TCP/UDP notes
- `02-linux/` : commands, permissions, bash
- `03-web-security/` : OWASP Top 10, SQLi, Burp
- `04-tools/` : nmap, gobuster, Metasploit cheatsheets
- `05-writeups/` : lab and CTF writeups
- `06-projects/` : small scripts and labs

> All work is done in legal environments only: my own VMs, OverTheWire, CTF platforms, and targets I have written permission to test.
