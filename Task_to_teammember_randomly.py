
import random

team_members = ['Hakim', 'Farid', 'Asmae', 'Amina', 'Oumaima']
random_team_members = random.sample(team_members, len(team_members)) 
taches = ['centre_gestionnaire_formController', 'contactrespo', 'dashbord_controller', 'Historique_C_R_O', 'historique_formController'
, 'historique_respo_equi', 'historiques_salles_respo', 'reservation_controller']
taqsimhh = {member: [] for member in random_team_members}

while len(taches) > 0:
    for member in random_team_members:
        if len(taches) > 0:
            task_to_assign = random.choice(taches)
            taqsimhh[member].append(task_to_assign)
            taches.remove(task_to_assign)

print("Taqsim dyal les taches randomly:")
for member in team_members:
    print(member, ":", taqsimhh[member])
