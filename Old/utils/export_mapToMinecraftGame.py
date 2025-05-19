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

def export_map_to_minecraft(map_name="JumpsAI", source_dir=None, debug=False, auto_correct=True):
    """
    Exporte une carte du projet vers le jeu Minecraft.
    
    Args:
        map_name (str): Nom de la carte à exporter
        source_dir (str, optional): Dossier source dans le projet. Par défaut, 'maps'
                                   relatif à la racine du projet.
        debug (bool): Affiche des informations de débogage si True
        auto_correct (bool): Tente de corriger automatiquement le nom de la carte si True
    
    Returns:
        bool: True si l'exportation a réussi, False sinon
    """
    try:
        # Définir le dossier source par défaut si non spécifié
        if source_dir is None:
            # Obtenir le chemin du dossier utils (où se trouve ce script)
            script_dir = Path(__file__).parent.absolute()
            # Remonter d'un niveau pour obtenir la racine du projet puis aller dans maps
            source_dir = script_dir.parent / "maps"
        else:
            source_dir = Path(source_dir)
        
        # Afficher les cartes disponibles en mode debug
        if debug:
            print(f"📂 Dossier source: {source_dir}")
            print("📋 Cartes disponibles:")
            if source_dir.exists():
                for item in source_dir.iterdir():
                    if item.is_dir():
                        print(f"  - {item.name}")
            else:
                print(f"  ❌ Le dossier source {source_dir} n'existe pas")
        
        # Chemin source (dans le projet)
        source_map_path = source_dir / map_name
        
        # Vérifier si la carte existe dans le projet
        if not source_map_path.exists() and auto_correct:
            # Rechercher des alternatives similaires
            alternatives = []
            if source_dir.exists():
                for item in source_dir.iterdir():
                    if item.is_dir():
                        # Correspondance exacte avec inversion AI/IA
                        if (map_name.lower().replace("ai", "ia") == item.name.lower() or 
                            map_name.lower().replace("ia", "ai") == item.name.lower()):
                            print(f"🔄 Correction automatique: '{map_name}' → '{item.name}'")
                            map_name = item.name
                            source_map_path = source_dir / map_name
                            break
                        # Autres correspondances similaires
                        elif (item.name.lower().startswith(map_name.lower()) or 
                             map_name.lower().startswith(item.name.lower())):
                            alternatives.append(item.name)
        
        # Nouvelle vérification après la correction automatique
        if not source_map_path.exists():
            print(f"❌ ERREUR: Carte '{map_name}' introuvable dans le projet ({source_map_path})")
            
            if alternatives:
                print(f"💡 Cartes similaires trouvées:")
                for alt in alternatives:
                    print(f"   - {alt}")
                print(f"   Essayez: python export_mapToMinecraftGame.py --map {alternatives[0]}")
            
            print(f"   Assurez-vous d'avoir d'abord importé ou créé la carte dans le projet.")
            print(f"   Vous pouvez utiliser l'option --debug pour voir les cartes disponibles.")
            return False
        
        # Chemin de destination (dans le jeu Minecraft)
        minecraft_saves = get_minecraft_saves_path()
        dest_map_path = minecraft_saves / map_name
        
        # Vérifier si le dossier Minecraft existe
        if not minecraft_saves.exists():
            print(f"⚠️ Dossier Minecraft introuvable ({minecraft_saves})")
            print(f"   Création du dossier saves...")
            minecraft_saves.mkdir(parents=True, exist_ok=True)
            print(f"✅ Dossier Minecraft saves créé avec succès.")
        
        # Si la destination existe déjà, la supprimer
        if dest_map_path.exists():
            print(f"⚠️ La carte '{map_name}' existe déjà dans Minecraft. Écrasement en cours...")
            shutil.rmtree(dest_map_path)
            
        # Copier la carte
        print(f"🔄 Copie de la carte '{map_name}' vers Minecraft...")
        shutil.copytree(source_map_path, dest_map_path)
        
        print(f"✅ Carte '{map_name}' exportée avec succès vers Minecraft: {dest_map_path}")
        return True
        
    except OSError as e:
        print(f"❌ Erreur lors de l'exportation de la carte: {e}")
        return False

def main():
    """
    Fonction principale pour l'utilisation en ligne de commande.
    """
    parser = argparse.ArgumentParser(
        description="Exporte une carte du projet vers le jeu Minecraft"
    )
    parser.add_argument(
        "--map", "-m",
        default="JumpsAI",
        help="Nom de la carte à exporter (par défaut: JumpsAI)"
    )
    parser.add_argument(
        "--input", "-i",
        help="Dossier source dans le projet (par défaut: ./maps)"
    )
    parser.add_argument(
        "--debug", "-d",
        action="store_true",
        help="Affiche des informations supplémentaires de débogage"
    )
    parser.add_argument(
        "--no-autocorrect", "-n",
        action="store_true",
        help="Désactive la correction automatique des noms de carte"
    )
    args = parser.parse_args()
    
    # Exporter la carte
    success = export_map_to_minecraft(args.map, args.input, args.debug, not args.no_autocorrect)
    
    # Sortir avec un code d'erreur approprié
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
