# Cyber Roadmap

My 2-month journey to become eligible for a cybersecurity fresher role (Penetration Testing / Red Teaming).

## About me
Cybersecurity student focused on offensive security. Building hands-on skills in penetration testing, network and web application security through free, legal labs (personal VMs, OverTheWire, picoCTF).

## Progress
- [x] Phase 1: Networking fundamentals
- [x] Week 2: Linux + Pentest Methodology + Recon/Scanning (Days 1-6 complete)
- [ ] Weeks 3-4: Web Security + Burp Suite (deep dive)
- [ ] Weeks 5-6: Tools + CTFs / VulnHub machines
- [ ] Weeks 7-8: Portfolio and projects

## Week 2 progress (Linux + Recon)

### Linux (all 14 topics covered)
- [x] Basics and kernel, terminal navigation, file system hierarchy
- [x] File and directory management, text editors (nano/vim)
- [x] Users, groups, sudo
- [x] Permissions (chmod, SUID/SGID, sticky bit)
- [x] Processes (ps, kill, background jobs)
- [x] Package management (apt, dpkg)
- [x] Services and daemons (systemd), cron jobs
- [x] Networking commands (ip, ss), logs (auth.log, journalctl)
- [x] SSH deep-dive: key-based authentication, scp, sshd_config
- [x] Disk/system info: df, du, lsblk, uname, free

### Pentest methodology
- [x] 5 phases, scope and authorization, Cyber Kill Chain, MITRE ATT&CK
- [x] Passive vs active recon, OSINT basics (whois, dig, theHarvester, crt.sh)

### Reconnaissance and scanning (Metasploitable 2)
- [x] nmap: host discovery, scan types (-sS/-sT/-sU), port ranges, full port scan
- [x] Service/version detection (-sV), OS detection (-O), NSE scripts (--script vuln)
- [x] nikto web server scan (27 findings)
- [x] gobuster and ffuf directory enumeration
- [x] Burp Suite: proxy setup and request interception (intro)
- [x] searchsploit + CVE lookup for identified service versions

### Practice labs
- [x] OverTheWire Bandit: levels 0-12
- [ ] OverTheWire Bandit: levels 13-20

### Projects
- [x] Custom Python TCP port scanner (`06-projects/portscanner.py`)

### Pending
- [ ] Writeup #1: complete recon report for Metasploitable 2 (findings table ready, write-up pending)

## Key findings (Metasploitable 2 recon) — summary
11+ findings identified through nmap, NSE scripts, and nikto, including an outdated FTP service with a known backdoor, outdated kernel and web stack, exposed configuration/debug files, and weak SSL/TLS configuration. Full details in `05-writeups/`.

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
