#!/usr/bin/env python3
"""
XSS Vulnerability Scanner - Versão Simples para Teste
"""

import requests
import urllib3
from urllib.parse import urljoin
import sys
import time

# Desabilitar warnings de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("="*60)
print("XSS SCANNER - VERSÃO DE TESTE")
print("="*60)

# Verificar se foi fornecido um URL
if len(sys.argv) < 2:
    print("Uso: python xss_scanner.py <url>")
    print("Exemplo: python xss_scanner.py http://bocadolobo.com")
    sys.exit(1)

url = sys.argv[1]
print(f"URL alvo: {url}")
print("A testar conexão...")

try:
    # Testar conexão
    response = requests.get(url, timeout=10, verify=False)
    print(f"Status: {response.status_code}")
    print(f"Tamanho da página: {len(response.text)} bytes")
    print("Conexão bem-sucedida!")
    
    # Procurar por formulários
    print("\nA procurar formulários...")
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    print(f"Encontrados {len(forms)} formulário(s)")
    
    if forms:
        for i, form in enumerate(forms):
            print(f"\nFormulário {i+1}:")
            action = form.get('action', '')
            method = form.get('method', 'get')
            print(f"  Action: {action}")
            print(f"  Method: {method}")
            
            # Listar inputs
            inputs = form.find_all('input')
            for input_field in inputs:
                name = input_field.get('name', 'sem nome')
                type_field = input_field.get('type', 'text')
                print(f"  Input: {name} (tipo: {type_field})")
    
    # Testar payload simples
    print("\nA testar payload básico...")
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?test={payload}"
    print(f"URL de teste: {test_url}")
    
    response2 = requests.get(test_url, timeout=10, verify=False)
    if payload in response2.text:
        print("!!! POSSÍVEL VULNERABILIDADE XSS DETECTADA !!!")
    else:
        print("Payload não foi refletido na resposta")
    
except Exception as e:
    print(f"ERRO: {e}")
    print("Verifica se o URL está correto e acessível")

print("\n" + "="*60)
input("Pressiona Enter para sair...")
