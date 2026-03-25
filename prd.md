# Product Requirement Document (PRD) – L'Écrin de Malbuisson

Ce document détaille la méthodologie, les choix techniques et les exigences fonctionnelles ayant guidé la construction de l'application promotionnelle **L'Écrin de Malbuisson**.

## 1. Vision du Produit
Créer une vitrine digitale "Premium" et "Haute-Fidélité" pour un studio de location courte durée, capable de rivaliser avec les standards d'Airbnb tout en conservant une identité locale forte et une indépendance technique.

## 2. Méthodologie de Développement : "The Vanilla Way"

L'architecture repose sur une approche **"Zero-Dependency"** (Pure HTML5/CSS3/Vanilla JS) pour garantir :
- **Performance Maximale** : Chargement instantané sur mobile (score Lighthouse proche de 100).
- **Maintenance Facilitée** : Pas de frameworks (React/Vue/Angular) qui pourraient devenir obsolètes ou nécessiter des mises à jour de sécurité complexes.
- **Portabilité** : Le site peut être hébergé sur n'importe quel serveur statique (GitHub Pages, Vercel, FTP classique).

## 3. Architecture Technique & Fonctionnalités Clés

### A. Intégration iCal Dynamique
Au lieu d'utiliser un widget tiers payant ou lourd, nous avons implémenté un **parseur iCal sur-mesure** en JavaScript :
- **Flux iCal** : Connexion directe à l'URL `.ics` fournie par Airbnb.
- **Proxy CORS** : Utilisation d'un proxy pour contourner les restrictions de sécurité du navigateur et récupérer les données en temps réel.
- **Logique de Calendrier** : Calcul dynamique des plages de dates, gestion des états (Arrivée/Départ), et remplissage automatique du formulaire de contact.

### B. Design System & UX
- **Micro-Animations** : Utilisation d'Intersection Observer API pour déclencher des effets de `fade-in` au décompte du défilement.
- **Responsive Grid** : Layout flexible basé sur `CSS Grid` et `Flexbox` pour une adaptation parfaite de l'iPhone 15 à l'écran 4K.
- **Palette de Couleurs** : Utilisation de variables CSS (`:root`) pour une cohérence chromatique (Vert Forêt, Bleu Lac, Or) facilitant de futurs ajustements de thème.

### C. Optimisation iOS (PWA)
Transformation du site en **Progressive Web App (PWA)** pour un rendu natif sur iPhone :
- **Apple Touch Icon** : Génération d'une icône skeuomorphique (relief 3D) pour donner une impression de profondeur sur l'écran d'accueil.
- **Meta-tags Apple** : Configuration de `apple-mobile-web-app-capable` pour supprimer les bordures du navigateur Safari et simuler une application mobile dédiée.

### D. Authenticité Visuelle & SEO
- **Référencement Naturel** : Structure sémantique HTML5 (`<article>`, `<section>`, `<h1>`-`<h4>`) pour un indexation optimale par Google.
- **Balisage Open Graph** : (Optionnel) Préparation des tags pour un partage visuel sur les réseaux sociaux.
- **Contenu Réel** : Remplacement systématique des placeholders par des photos réelles géo-localisées et des adresses postales exactes.

## 4. Guide de Maintenance
1. **Mise à jour des Prix/Dates** : Directement dans la section script de `index.html`.
2. **Photos** : Déposer les nouvelles images dans le dossier `/images/` et mettre à jour le lien dans le `src` correspondant.
3. **iCal** : Coller l'URL export Airbnb dans la variable `AIRBNB_ICAL_URL` au début du script.

---
*Document produit pour le projet L'Écrin de Malbuisson.*
