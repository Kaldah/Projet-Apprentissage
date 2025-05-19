import os
import shutil
import platform
import argparse
from pathlib import Path

def get_minecraft_saves_path():
    """
    Récupère le chemin vers le dossier 'saves' de Minecraft en fonction du système d'exploitation.
    
    Returns:
        Path: Chemin vers le dossier 'saves' de Minecraft
    """
    system = platform.system()
    user_home = Path.home()

    if system == "Windows":
        return user_home / "AppData" / "Roaming" / ".minecraft" / "saves"
    elif system == "Darwin":  # macOS
        return user_home / "Library" / "Application Support" / "minecraft" / "saves"
    elif system == "Linux":
        return user_home / ".minecraft" / "saves"
    else:
        raise OSError(f"Système d'exploitation non supporté: {system}")

def import_map_to_project(map_name="JumpsIA", target_dir=None):
    """
    Importe une carte Minecraft du jeu vers le projet.
    
    Args:
        map_name (str): Nom de la carte Minecraft à importer
        target_dir (str, optional): Dossier de destination dans le projet. Par défaut, 'maps'
                                   relatif à la racine du projet.
    
    Returns:
        bool: True si l'importation a réussi, False sinon
    """
    # Définir le dossier cible par défaut si non spécifié
    if target_dir is None:
        # Obtenir le chemin du dossier utils (où se trouve ce script)
        script_dir = Path(__file__).parent.absolute()
        # Remonter d'un niveau pour obtenir la racine du projet puis aller dans maps
        target_dir = script_dir.parent / "maps"
    else:
        target_dir = Path(target_dir)
    
    try:
        # Chemin source (dans le jeu Minecraft)
        minecraft_saves = get_minecraft_saves_path()
        source_map_path = minecraft_saves / map_name
        
        # Chemin de destination (dans le projet)
        dest_map_path = target_dir / map_name
        
        # Vérifier si la carte existe dans Minecraft
        if not source_map_path.exists():
            print(f"❌ ERREUR: Carte '{map_name}' introuvable dans Minecraft ({source_map_path})")
            print(f"   Vérifiez que vous avez bien créé cette carte dans Minecraft.")
            return False
        
        # Créer le dossier de destination s'il n'existe pas
        os.makedirs(target_dir, exist_ok=True)
        
        # Supprimer la destination si elle existe déjà
        if dest_map_path.exists():
            print(f"⚠️ La carte '{map_name}' existe déjà dans le projet. Écrasement en cours...")
            shutil.rmtree(dest_map_path)
        
        # Copier la carte
        print(f"🔄 Copie de la carte '{map_name}' depuis Minecraft...")
        shutil.copytree(source_map_path, dest_map_path)
        
        print(f"✅ Carte '{map_name}' importée avec succès dans: {dest_map_path}")
        return True
        
    except OSError as e:
        print(f"❌ Erreur lors de l'importation de la carte: {e}")
        return False

def main():
    """
    Fonction principale pour l'utilisation en ligne de commande.
    """
    parser = argparse.ArgumentParser(
        description="Importe une carte de Minecraft vers le projet"
    )
    parser.add_argument(
        "--map", "-m",
        default="JumpsIA",
        help="Nom de la carte Minecraft à importer (par défaut: JumpsIA)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Dossier de destination dans le projet (par défaut: ./maps)"
    )
    args = parser.parse_args()
    
    # Importer la carte
    success = import_map_to_project(args.map, args.output)
    
    # Sortir avec un code d'erreur approprié
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
