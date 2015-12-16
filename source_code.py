# Trier deux fichiers pour n'en faire plus qu'un
# Interoger au hasard 
# créer un fichier directement dès que les gens dépose leurs informations 
# anna faut pusher systmatiquement et t'assurer que c'est bien passé !
# choix de la langue d'interrogation
# importation modulaire du code dans interface
# distance de Levenshtein
# créer une fonction choix du nom dans l'interface


import random


# Fiche de vocabulaire sur un thème unique, choix du titre du fichier, collect data à partir de l'interface graphique
class fch_interro():
	def __init__(self):
		self.nb_words = 0
		self.name = "test.txt"
		self.tableau = []
		self.fiche = self.create_file()

	def create_file(self): #crée un fichier .txt qui restera en mémoire à terme
		# self.name = ask for name + .txt
		self.fiche = open(self.name, "w")  # ou "a"? ou créer un conflit si le nom est déjà utilisé 

	def collect_data(self, word_lg1, word_lg2): #remplit le fichier la première fois
		definition = word_lg1 + ":" + word_lg2 + '\n'
		self.fiche = open(self.name, "a")
		self.fiche.write(definition)

	def read_file(self): #collecte ligne par ligne une premère fois
		with open(self.name, "r") as data:
			for line in data:
				self.tableau.append(line)
				self.nb_words += 1
		for i in range(f.nb_words):
			print(self.tableau[i])


	def file_to_tableau(self): #convertit le fichier texte en un tableau ou on trouve en indice par les mots langue 1 et en pair les mots langue 2
		self.read_file()
		for i in range(self.nb_words):
			word_lg1 = self.tableau[i].split(':', 1)[0] #mot dans la langue 1
			word_intermediaire = self.tableau[i].split(':', 1)[1] #mot correspondant dans la langue 2 + saut de ligne
			word_lg2 = word_intermediaire.split('\n', 1)[0] #mot correspondant dans la langue 2
			self.tableau[i] = word_lg1 
			self.tableau.append(word_lg2) #(prend la position nb_words+i)

	#def choose_lg(self): #renvoi 1 si premier langage, 2 si deuxième

#	def interrogate(self):
#		idx_language = self.choose_lg()
#		vocab = [i for i in range(self.nb_words)]
#		for i in range(self.nb_words):
#			idx_rdm = random.choice(vocab)

f = fch_interro()
f.collect_data("bonjour", "hello")
f.collect_data("bonjour2", "hello2")
f.collect_data("bonjour3", "hello3")
f.collect_data("bonjour4", "hello4")
f.file_to_tableau()
for i in range(2*f.nb_words):
	print(f.tableau[i])








