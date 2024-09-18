import subprocess
import whois

sites = [
    "www.google.com",
    "www.youtube.com",
    "www.uol.com.br",
    "www.globo.com",
    "www.mercadolivre.com.br",
    "www.amazon.com.br",
    "www.netflix.com",
    "www.instagram.com",
    "www.whatsapp.com",
    "www.twitter.com",
    "www.reddit.com",
    "www.linkedin.com",
    "www.facebook.com",
    "www.olx.com.br",
    "www.magazineluiza.com.br",
    "www.ifood.com.br",
    "www.americanas.com.br",
    "www.nubank.com.br",
    "www.bb.com.br",
    "www.itau.com.br",
    "www.santander.com.br",
    "www.c6bank.com.br",
    "www.bradesco.com.br",
    "www.tiktok.com",
    "www.pontofrio.com.br",
    "www.submarino.com.br",
    "www.livrariacultura.com.br",
    "www.shoptime.com.br"
]

def get_ip(site):
    try:
        result = subprocess.run(['nslookup', site, '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.splitlines()
        for line in output:
            if "Address" in line and not "127.0.0.1" in line and not "8.8.8.8" in line:  # Ignora loopback e o próprio servidor DNS
                return line.split()[-1]
    except Exception as e:
        print(f"Erro ao executar nslookup para {site}: {e}")
        return None

def is_cloudflare(ip):
    try:
        domain_info = whois.whois(ip)
        if "cloudflare" in str(domain_info).lower():
            return True
        return False
    except Exception as e:
        print(f"Erro ao consultar WHOIS para {ip}: {e}")
        return False

cloudflare_sites = []

for site in sites:
    print(f"Verificando {site}...")
    ip = get_ip(site)
    if ip:
        print(f"IP encontrado: {ip}")
        if is_cloudflare(ip):
            print(f"{site} está usando Cloudflare.")
            cloudflare_sites.append(site)
        else:
            print(f"{site} NÃO está usando Cloudflare.")
    else:
        print(f"Não foi possível encontrar o IP de {site}.")

if cloudflare_sites:
    print("\nSites que estão usando Cloudflare:")
    for site in cloudflare_sites:
        print(site)
else:
    print("\nNenhum site da lista está usando Cloudflare.")
