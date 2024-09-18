# Cloudflare Site Checker

## Descrição

Este é um script Python que verifica se sites populares estão utilizando a infraestrutura da Cloudflare. Ele faz uso de consultas DNS (`nslookup`) para obter o IP dos sites e, em seguida, utiliza o serviço WHOIS para determinar se o IP está associado à Cloudflare.

## Funcionalidades

- Realiza consultas DNS para vários sites populares.
- Usa a API WHOIS para identificar se os sites estão utilizando a Cloudflare.
- Gera uma lista de sites que utilizam a Cloudflare.

## Requisitos

- Python 3.6 ou superior
- Dependências Python:
  - `python-whois`
  
Para instalar as dependências, execute:

```bash
pip install python-whois
```

## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/cloudflare-site-checker-python.git
   cd cloudflare-site-checker-python
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # No Windows, use: myenv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install python-whois
   ```

4. Execute o script:
   ```bash
   python3 check_cloudflare.py
   ```

O script irá verificar os sites da lista e determinar se eles utilizam a Cloudflare.

## Exemplo de saída

```bash
Verificando www.google.com...
IP encontrado: 142.250.64.206
www.google.com NÃO está usando Cloudflare.

Verificando www.youtube.com...
IP encontrado: 172.217.29.142
www.youtube.com NÃO está usando Cloudflare.

Verificando www.cloudflare.com...
IP encontrado: 104.16.132.229
www.cloudflare.com está usando Cloudflare.

...

Sites que estão usando Cloudflare:
- www.cloudflare.com
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.
