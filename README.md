# XSS Vulnerability Scanner (Versão de Teste)

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

Um script em Python simples e direto projetado para realizar testes básicos de vulnerabilidades de **Cross-Site Scripting (XSS)**. A ferramenta valida a conexão com o alvo, mapeia formulários HTML estruturais e testa se um payload padrão é refletido na resposta do servidor.

> [!WARNING]
> **AVISO LEGAL:** Este script foi desenvolvido exclusivamente para fins educacionais, laboratoriais e testes de segurança autorizados. O uso deste software contra alvos sem autorização prévia é ilegal.

---

## 🚀 Funcionalidades

* **Validação de Conectividade:** Testa o estado do servidor web antes de iniciar a análise de vulnerabilidades.
* **Mapeamento de Formulários HTML:** Localiza formulários na página principal, identificando os seus atributos (`action`, `method`) e os respetivos campos de entrada (`input`).
* **Teste de Reflexão de Payload:** Envia um payload básico via parâmetro `GET` (`<script>alert('XSS')</script>`) e verifica se o mesmo é devolvido no corpo da resposta sem a devida higienização.

---

## 🛠️ Pré-requisitos & Instalação

Garante que tens o Python 3 instalado e as bibliotecas necessárias para o processamento HTTP e análise de HTML:

```bash
pip install requests beautifulsoup4

Como Usar 
python3 xss_scanner.py <URL_ALVO>
