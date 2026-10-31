# Metasploitable 2 — Reconnaissance & Scanning Writeup

**Author:** Khurram Sarfraz
**Date:** October 2026
**Lab environment:** VirtualBox — Kali Linux (attacker) + Metasploitable 2 (target), isolated host-only network
**Scope:** This engagement was conducted entirely in a personal, isolated lab environment. Metasploitable 2 is an intentionally vulnerable VM designed for security training and is never exposed to any real network.

---

## 1. Objective

Perform a structured reconnaissance and scanning engagement against Metasploitable 2 to identify live hosts, open ports, running services, service versions, and associated known vulnerabilities — following the standard penetration testing methodology (Reconnaissance → Scanning → Findings).

---

## 2. Lab Setup

| Machine | Role | IP Address | Network |
|---|---|---|---|
| Kali Linux | Attacker | 192.168.56.10 (static) | NAT + Host-only |
| Metasploitable 2 | Target (intentionally vulnerable) | 192.168.56.101 | Host-only (isolated) |

Both VMs were snapshotted in a clean state prior to testing.

---

## 3. Host Discovery
