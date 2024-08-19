import csv
import os
from datetime import datetime

def clear_screen():
    """Efface l'écran de la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def collect_user_info():
    """Collecte les informations de l'utilisateur et affiche chaque réponse à côté de la question."""
    questions = ["meditation", "yoga", "isha kriya", "chit shakti", "sport", "respiration", "tk","lecture","guitar", "video"]
    responses = [""] * len(questions)
    
    for i in range(len(questions)):
        clear_screen()
        for j in range(len(questions)):
            if responses[j]:
                print(f"{questions[j]} {responses[j]}")
            else:
                print(questions[j])
        
        responses[i] = input(f"\n> '{questions[i]}':  ")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    responses.append(current_date)
    return responses

def append_to_csv(file_path, data):
    """Ajoute une nouvelle ligne au fichier CSV."""
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(data)
    print("Les informations ont été ajoutées au fichier CSV.")

def main():
    """Fonction principale pour exécuter le formulaire et ajouter les données au CSV."""
    # Chemin du fichier CSV
    file_path = 'information.csv'
    
    # Collecte des informations de l'utilisateur
    user_info = collect_user_info()
    
    # Ajout des informations au fichier CSV
    append_to_csv(file_path, user_info)

if __name__ == "__main__":
    main()
