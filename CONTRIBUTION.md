# Guide de contribution à Synopé

EN TRAVAUX

Quelques règles qui font la cohérence d'ensemble des ressources
de Synopé :
* Python 3
* Présentations en francais.
* 50% cours, 50% pratique.
* Un thème par demi-journée.
* Un TP fil-rouge tout au long de la formation.
* On utilise au maximum les notebooks Jupyter, et on essaie de les faire
  tourner sur un serveur central, pour l'instant via [Binder](http://mybinder.org/faq/).
* En projet, les utiliser aussi pour les travaux pratiques.  
  En attendant l'environnement à privilégier pour l'installation locale est Anaconda.

Quelques règles facilitant la restructuration continue des cours :
* Ne pas surnuméroter vos sections, en particulier ne pas utiliser
  une numérotation globale qui serait à refaire au moindre changement
  de plan.
* Les informations spécifiques à une session, comme le choix de la version de Python,
  le nom des orateurs, les outils et les éditeurs choisis... doivent être regroupées
  dans un notebook unique et isolé, et ne pas polluer les notebooks
  qui doivent resservir.
* Bien séparé les notebooks sur les travaux pratiques, notamment si on
  a un TP fil-rouge, de façon à pouvoir changer de fil-rouge selon le
  public de telle ou telle session.

