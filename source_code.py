
# créer un fichier directement dès que les gens dépose leurs informations 
# choix de la langue d'interrogation
# distance de Levenshtein
# ATTENTION PROBLEME DANS READ FILE il ne voit pas la denière ligne

import random


# Fiche de vocabulaire sur un thème unique, choix du titre du fichier, collect data à partir de l'interface graphique
class fch_interro():
	def __init__(self):
		self.nb_words = 0
		self.name = ""
		self.nametxt = ""
		self.tableau_ensemble_mots = []
		self.to_guess = [] #mot à deviner
		self.answer = [] #réponse correspondante (self.to_guess[i] traduit = self.answer[i])

	def open_file(self): #crée un fichier .txt qui restera en mémoire à terme
		self.nametxt = self.name + ".txt"
		self.fiche = open(self.nametxt, "w")  # ou "a"? ou créer un conflit si le nom est déjà utilisé 
		self.fiche.close()

	def collect_data(self, word_lg1, word_lg2): #remplit le fichier la première fois
		definition = word_lg1 + ":" + word_lg2 + '\n'
		self.fiche = open(self.nametxt, "a")
		self.fiche.write(definition)
		self.nb_words += 1
		self.fiche.close()

	def read_file(self): #collecte ligne par ligne une première fois
		data = open(self.nametxt, "r")
		self.tableau_ensemble_mots = data.readlines()
		data.close()

	def file_to_tableau(self): #convertit le fichier texte en un tableau ou on trouve en indice par les mots langue 1 et en pair les mots langue 2
		self.read_file()
		for i in range(self.nb_words):
			word_lg1 = self.tableau_ensemble_mots[i].split(':', 1)[0] #mot dans la langue 1
			word_intermediaire = self.tableau_ensemble_mots[i].split(':', 1)[1] #mot correspondant dans la langue 2 + saut de ligne
			word_lg2 = word_intermediaire.split('\n', 1)[0] #mot correspondant dans la langue 2
			self.tableau_ensemble_mots[i] = word_lg1 
			self.tableau_ensemble_mots.append(word_lg2) #(prend la position nb_words+i)

	#def choose_lg(self): #renvoi 0 si premier langage, 1 sinon

	def interrogate(self):
		'''On suppose qu'on peut être intérrogé dans n'importe quel sens'''
		couple_interro = [i for i in range(self.nb_words)]
		choix_langue = [0, 1]
		for i in range(self.nb_words):
			idx_rdm = random.choice(couple_interro) #on choisit le couple de mot
			idx_language = random.choice(choix_langue) #on choisit le sens de l'intero
			self.to_guess.append(self.tableau[idx_rdm + idx_language*self.nb_words])
			self.answer.append(self.tableau[idx_rdm + (1 - idx_language)*self.nb_words])
			# print(to_guess, ":", answer)
			# processus d'interogation levenstein
			# self.score
			couple_interro.remove(idx_rdm)


#f = fch_interro()
#f.collect_data("bonjour", "hello")
#f.collect_data("bonjour2", "hello2")
#f.collect_data("bonjour3", "hello3")
#f.collect_data("bonjour4", "hello4")
#f.collect_data("jobi", "joba")
#f.collect_data("dd","dd")
#f.file_to_tableau()
#for i in range(2*f.nb_words):
#	print(f.tableau[i])
#f.interrogate()








