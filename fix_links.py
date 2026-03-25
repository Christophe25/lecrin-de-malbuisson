import re

with open("index.html", "r") as f:
    content = f.read()

urls = [
    '<a href="https://www.le-bon-accueil.fr/" target="_blank" rel="noopener noreferrer" class="adresse-card fade-in">',
    '<a href="https://www.hotel-le-lac.fr/" target="_blank" rel="noopener noreferrer" class="adresse-card fade-in">',
    '<a href="https://www.l-edelweiss-restaurant-les-hopitaux-neufs.fr/" target="_blank" rel="noopener noreferrer" class="adresse-card fade-in">',
    '<a href="https://www.google.com/maps/search/?api=1&query=Boulangerie+Au+Petit+Desmouss+Malbuisson" target="_blank" rel="noopener noreferrer" class="adresse-card fade-in">',
    '<a href="https://www.base-nautique-malbuisson.fr/" target="_blank" rel="noopener noreferrer" class="adresse-card fade-in">',
    '<a href="https://www.metabiefaventures.fr/" target="_blank" rel="noopener noreferrer" class="adresse-card fade-in">',
    '<a href="https://www.station-metabief.com/" target="_blank" rel="noopener noreferrer" class="adresse-card fade-in">',
    '<a href="https://www.aqua2lacs.fr/" target="_blank" rel="noopener noreferrer" class="adresse-card fade-in">'
]

# The block starts with <div class="adresse-card fade-in">
# and ends with                </div> (16 spaces before </div>)

pattern = r'( {16})<div class="adresse-card fade-in">(.*?) {16}</div>'
matches = list(re.finditer(pattern, content, flags=re.DOTALL))

if len(matches) == 8:
    for i in reversed(range(8)):
        start, end = matches[i].span()
        inner = matches[i].group(2)
        new_block = f"{matches[i].group(1)}{urls[i]}{inner}{matches[i].group(1)}</a>"
        content = content[:start] + new_block + content[end:]
        
    with open("index.html", "w") as f:
        f.write(content)
    print("Successfully replaced 8 cards with links.")
else:
    print(f"Error: Found {len(matches)} matches instead of 8.")
