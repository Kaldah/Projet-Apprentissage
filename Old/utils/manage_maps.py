import argparse
import sys
from pathlib import Path
from import_mapToProject import import_map_to_project
from export_mapToMinecraftGame import export_map_to_minecraft

def print_banner():
    """Affiche une bannière décorative pour le script."""
    print("""
╔════════════════════════════════════════════════════╗
║                                                    ║
║            GESTIONNAIRE DE CARTES MINECRAFT        ║
║                  POUR PROJET JUMP IA               ║
║                                                    ║
╚════════════════════════════════════════════════════╝
    """)

def list_project_maps():
    """
    Liste toutes les cartes disponibles dans le dossier 'maps' du projet.
    
    Returns:
        list: Liste des noms de cartes trouvées
    """
    script_dir = Path(__file__).parent.absolute()
    maps_dir = script_dir.parent / "maps"
    
    if not maps_dir.exists():
        print(f"ℹ️ Le dossier 'maps' n'existe pas encore dans le projet.")
        return []
    
    # Récupérer tous les sous-dossiers (potentiellement des cartes)
    maps = [f.name for f in maps_dir.iterdir() if f.is_dir()]
    
    if not maps:
        print("ℹ️ Aucune carte n'a été trouvée dans le projet.")
    else:
        print(f"📋 Cartes disponibles dans le projet ({len(maps)}):")
        for i, map_name in enumerate(maps, 1):
            print(f"  {i}. {map_name}")
    
    return maps

def list_minecraft_maps():
    """
    Liste toutes les cartes disponibles dans Minecraft.
    
    Returns:
        list: Liste des noms de cartes trouvées
    """
    try:
        # Import depuis le module qui définit cette fonction
        from import_mapToProject import get_minecraft_saves_path
        
        minecraft_saves = get_minecraft_saves_path()
        
        if not minecraft_saves.exists():
            print(f"ℹ️ Le dossier Minecraft 'saves' n'a pas été trouvé.")
            return []
        
        # Récupérer tous les sous-dossiers (les cartes)
        maps = [f.name for f in minecraft_saves.iterdir() if f.is_dir()]
        
        if not maps:
            print("ℹ️ Aucune carte n'a été trouvée dans Minecraft.")
        else:
            print(f"📋 Cartes disponibles dans Minecraft ({len(maps)}):")
            for i, map_name in enumerate(maps, 1):
                print(f"  {i}. {map_name}")
        
        return maps
        
    except Exception as e:
        print(f"❌ Erreur lors de la recherche des cartes Minecraft: {e}")
        return []

def interactive_menu():
    """
    Affiche un menu interactif pour gérer les cartes.
    """
    while True:
        print("\n" + "=" * 50)
        print("🎮 MENU: GESTION DES CARTES MINECRAFT")
        print("=" * 50)
        print("1. Importer une carte de Minecraft vers le projet")
        print("2. Exporter une carte du projet vers Minecraft")
        print("3. Lister les cartes disponibles")
        print("4. Quitter")
        
        choice = input("\nChoisissez une option (1-4): ")
        
        if choice == '1':
            # Importer une carte
            maps = list_minecraft_maps()
            if not maps:
                continue
                
            map_num = input("\nEntrez le numéro de la carte à importer (ou 'q' pour annuler): ")
            if map_num.lower() == 'q':
                continue
                
            try:
                map_index = int(map_num) - 1
                if 0 <= map_index < len(maps):
                    map_name = maps[map_index]
                    print(f"\nImportation de la carte '{map_name}'...")
                    import_map_to_project(map_name)
                else:
                    print("❌ Numéro de carte invalide!")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide.")
                
        elif choice == '2':
            # Exporter une carte
            maps = list_project_maps()
            if not maps:
                continue
                
            map_num = input("\nEntrez le numéro de la carte à exporter (ou 'q' pour annuler): ")
            if map_num.lower() == 'q':
                continue
                
            try:
                map_index = int(map_num) - 1
                if 0 <= map_index < len(maps):
                    map_name = maps[map_index]
                    print(f"\nExportation de la carte '{map_name}'...")
                    export_map_to_minecraft(map_name)
                else:
                    print("❌ Numéro de carte invalide!")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide.")
                
        elif choice == '3':
            # Lister les cartes
            print("\n📂 CARTES DISPONIBLES")
            print("-" * 30)
            list_project_maps()
            print()
            list_minecraft_maps()
            
        elif choice == '4':
            # Quitter
            print("\n👋 Au revoir!")
            break
            
        else:
            print("❌ Option invalide! Veuillez choisir entre 1 et 4.")

def main():
    """
    Fonction principale pour l'utilisation en ligne de commande ou interactive.
    """
    parser = argparse.ArgumentParser(
        description="Gestionnaire de cartes Minecraft pour le projet Jump IA"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="Lister les cartes disponibles"
    )
    parser.add_argument(
        "--import", "-i",
        metavar="MAP_NAME",
        dest="import_map",
        help="Importer une carte de Minecraft vers le projet"
    )
    parser.add_argument(
        "--export", "-e",
        metavar="MAP_NAME",
        dest="export_map", 
        help="Exporter une carte du projet vers Minecraft"
    )
    parser.add_argument(
        "--interactive", "-m",
        action="store_true",
        help="Lancer le mode interactif (menu)"
    )
    
    args = parser.parse_args()
    
    # Afficher la bannière
    print_banner()
    
    # Si aucun argument n'est donné, lancer le mode interactif
    if len(sys.argv) == 1 or args.interactive:
        interactive_menu()
        return
    
    # Traiter les arguments
    if args.list:
        print("\n📂 CARTES DISPONIBLES")
        print("-" * 30)
        list_project_maps()
        print()
        list_minecraft_maps()
    
    if args.import_map:
        import_map_to_project(args.import_map)
    
    if args.export_map:
        export_map_to_minecraft(args.export_map)

if __name__ == "__main__":
    main()
