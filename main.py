import qrcode
from urllib.parse import urlparse

#********************Affectation des variables********************

url = str(input("                       / __ \|  __ \  | |           | |  | (_)\n"
            "   ___  __ _ ___ _   _| |  | | |__) | | |__  _   _  | |__| |\n"
            "  / _ \/ _` / __| | | | |  | |  _  /  | '_ \| | | | |  __  | | '__/ _ \ \ /\ / /_  /_  /\n"
            " |  __/ (_| \__ \ |_| | |__| | | \ \  | |_) | |_| | | |  | | | | | (_) \ V  V / / / / /\n"
            "  \___|\__,_|___/\__, |\___\_\_|  \_\ |_.__/ \__, | |_|  |_|_|_|  \___/ \_/\_/ /___/___|\n"
            "                  __/ |                       __/ |\n"
            "                 |___/                       |___/\n"
            "Veuillez renseigner ci-dessous l'URL à transformé en QRCode :\n"))

# Analyse l'url donné
parsed_url = urlparse(url)
# Extrait le nom de domaine de celui-ci
nom_de_domaine = parsed_url.netloc

#***********************Programme principal***********************

# Vérifie que l'url choisi existe bel et bien
if not nom_de_domaine:
    print("Veuillez choisir un URL valide et existant")
else:
    # Création du QRcode à partir de l'url fourni
    img = qrcode.make(url)
    # Sauvegarde le QRcode dans un png avec un nom lisible (nom de domaine only)
    img.save(nom_de_domaine + '.png')
    print(f"Votre QR code pour {nom_de_domaine} a bien été créé")
