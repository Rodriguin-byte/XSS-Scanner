# ⚠️ XSS Vulnerability Scanner - Simple Test Version

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)](CONTRIBUTING.md)

A simple and educational tool for detecting Cross-Site Scripting (XSS) vulnerabilities. Developed for learning purposes and authorized testing.

## 🎯 About The Project

The XSS Scanner is a lightweight, didactic tool designed to help security students and professionals understand how XSS vulnerability detection works. This simple version demonstrates fundamental concepts of:

- 🔍 **Form detection** on web pages
- 📝 **Input field analysis** and parameters
- 💉 **Basic XSS payload testing**
- 📊 **Payload reflection verification** in responses

### ✨ Current Features

| Feature | Description | Status |
|---------|-----------|--------|
| 🌐 **Connection Test** | Checks if target is accessible | ✅ Implemented |
| 📋 **Form Detection** | Finds and lists HTML forms | ✅ Implemented |
| 🔍 **Input Analysis** | Identifies input fields | ✅ Implemented |
| 💉 **Basic Payload** | Tests `<script>alert('XSS')</script>` | ✅ Implemented |
| 📊 **Reflection Check** | Confirms if payload was reflected | ✅ Implemented |

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/your-username/xss-scanner.git
cd xss-scanner
