# Trier deux fichiers pour n'en faire plus qu'un
# Interoger au hasard 
# créer un fichier directement dès que les gens dépose leurs informations 
# anna faut pusher systmatiquement et t'assurer que c'est bien passé !
# choix de la langue d'interrogation

import random


# Fiche de vocabulaire sur un thème unique, choix du titre du fichier, collect data à partir de l'interface graphique
class fch_interro():
	def __init__(self):
		self.fiche = create_file(self)
		self.nb_words = 0
		self.name = ""
		self.tableau = []

	def create_file(self): #crée un fichier .txt qui restera en mémoire à terme
		# self.name = ask for name + .txt
		self.fiche = open(self.name, "w")  # ou "a"? ou créer un conflit si le nom est déjà utilisé 

	def collect_data(word_lg1,word_lg2): #remplit le fichier la première fois
		definition = word_lg1 + ":" + word_lg2
		self.fiche = open(self.name, "w")
		self.fiche.append(definition)

    def read_file(self): # collecte ligne par ligne une premère fosi 
        with open(self.name, "r") as data:
            for line in data:
                self.tableau.append(line)
                self.nb_words += 1

    def file_to_tableau(self):
    	self.read_file()
        for i in range(self.nb_words):
            indice_imp = int(float(self.tableau_idx[i].split(':', 1)[0]))
            info = self.tableau_idx[i].split(' ', 1)[1]
            self.tableau_idx[i] = indice_imp

	def choose_lg(self): #renvoi 1 si premier langage, 2 si deuxième

    def collect_info(self):
        for i in range(self.nb_total_elements):
            indice_imp = int(float(self.tableau_idx[i].split(':', 1)[0]))
            info = self.tableau_idx[i].split(' ', 1)[1]
            self.tableau_idx[i] = indice_imp
            self.tableau_info.append(info)


	def interrogate(self):
		idx_language = self.choose_lg()
		vocab = [i for i in range(self.nb_words)]
		for i in range(self.nb_words):
			idx_rdm = random.choice(vocab)








