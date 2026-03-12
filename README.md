#  XSS Vulnerability Scanner - Simple Test Version

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)](CONTRIBUTING.md)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/seu-usuario/xss-scanner/graphs/commit-activity)

Uma ferramenta simples e educacional para deteção de vulnerabilidades de Cross-Site Scripting (XSS). Desenvolvida para fins de aprendizagem e testes autorizados.

##  Sobre o Projeto

O XSS Scanner é uma ferramenta leve e didática desenvolvida para ajudar estudantes de segurança e profissionais a compreenderem como funciona a deteção de vulnerabilidades XSS. Esta versão simples demonstra os conceitos fundamentais de:

-  **Deteção de formulários** em páginas web
-  **Análise de inputs** e parâmetros
-  **Teste de payloads XSS** básicos
-  **Verificação de reflexão** de payloads na resposta

###  Funcionalidades Atuais

| Funcionalidade | Descrição | Status |
|----------------|-----------|--------|
|  **Teste de Conexão** | Verifica se o alvo está acessível | ✅ Implementado |
|  **Deteção de Formulários** | Encontra e lista formulários HTML | ✅ Implementado |
|  **Análise de Inputs** | Identifica campos de entrada | ✅ Implementado |
|  **Payload Básico** | Testa `<script>alert('XSS')</script>` | ✅ Implementado |
|  **Verificação de Reflexão** | Confirma se payload foi refletido | ✅ Implementado |

##  Instalação

### Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/xss-scanner.git
cd xss-scanner
