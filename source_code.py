
# créer un fichier directement dès que les gens dépose leurs informations 
# choix de la langue d'interrogation
# distance de Levenshtein
# ATTENTION PROBLEME DANS READ FILE il ne voit pas la denière ligne

import random
import os


# Fiche de vocabulaire sur un thème unique, choix du titre du fichier, collect data à partir de l'interface graphique
class fch_interro():
	def __init__(self):
		self.nb_words = 0
		self.name = ""
		self.langue1 = ""
		self.langue2 = ""
		#self.datafiche = ""
		self.nametxt = ""
		#self.namedata = ""
		self.score = 0
		self.tableau = []
		self.to_guess = [] #mot à deviner
		self.answer = [] #réponse correspondante (self.to_guess[i] traduit = self.answer[i])

	def create_file(self): #crée un fichier .txt qui restera en mémoire à terme
		self.nametxt = self.name + ".txt"
		#self.namedata = "data_" + self.name + ".txt"
		self.fiche = open(self.nametxt, "a")  # ou "a"? ou créer un conflit si le nom est déjà utilisé 
		self.fiche.close()
		#self.datafiche = open(self.namedata,"w")
		#self.datafiche.write(self.langue1 + ":" + self.langue2 + '\n')
		#self.datafiche.close()

	def open_file(self): #crée un fichier .txt qui restera en mémoire à terme
		self.nametxt = self.name + ".txt"
		self.fiche = open(self.nametxt, "r")  # ou "a"? ou créer un conflit si le nom est déjà utilisé 
		self.fiche.close()

	def collect_data(self, word_lg1, word_lg2): #remplit le fichier la première fois
		definition = word_lg1 + ":" + word_lg2 + '\n'
		self.fiche = open(self.nametxt, "a")
		self.fiche.write(definition)
		self.nb_words += 1
		self.fiche.close()

	def read_file(self): #collecte ligne par ligne une première fois
		data = open(self.nametxt, "r")
		self.tableau = data.readlines()
		self.nb_words = len(self.tableau)
		data.close()

	def file_to_tableau(self): #convertit le fichier texte en un tableau ou on trouve en indice par les mots langue 1 et en pair les mots langue 2
		self.read_file()
		self.langue1 = self.tableau[0].split(':', 1)[0] 
		langue_intermediaire = self.tableau[0].split(':', 1)[1] 
		self.langue2 = langue_intermediaire.split('\n', 1)[0]
		self.tableau = self.tableau[1:]
		self.nb_words -= 1
		for i in range(self.nb_words):
			word_lg1 = self.tableau[i].split(':', 1)[0] #mot dans la langue 1
			word_intermediaire = self.tableau[i].split(':', 1)[1] #mot correspondant dans la langue 2 + saut de ligne
			word_lg2 = word_intermediaire.split('\n', 1)[0] #mot correspondant dans la langue 2
			self.tableau[i] = word_lg1 
			self.tableau.append(word_lg2) #(prend la position nb_words+i)
		self.interrogate()

	def choose_lg(self): #langue 1 renvoie l'indice 0 et langue 2 l'indice 1 du choix langue d'apres
		if self.langue1 == self.langue_question:
			return 0
		if self.langue2 == self.langue_question:
			return 1
		else:
			print("Vous ne pouvez pas être intérrogé dans cette langue")

	def interrogate(self):
		couple_interro = [i for i in range(self.nb_words)]
		idx_language = self.choose_lg()
		for i in range(self.nb_words):
			idx_rdm = random.choice(couple_interro) #on choisit le couple de mot
			self.to_guess.append(self.tableau[idx_rdm + idx_language*self.nb_words])
			self.answer.append(self.tableau[idx_rdm + (1 - idx_language)*self.nb_words])
			couple_interro.remove(idx_rdm)

class stats():
	def __init__(self):
		self.nb_words = 0
		self.name = ""
		self.langue1 = ""
		self.langue2 = ""
		#self.datafiche = ""
		self.nametxt = ""
		#self.namedata = ""
		self.score = 0
		self.tableau = []
		self.to_guess = [] #mot à deviner
		self.answer = [] #réponse correspondante (self.to_guess[i] traduit = self.answer[i])

def distance_levenshtein(mot1,mot2):
	len1=len(mot1)
	len2=len(mot2)
	d=[0]*((len1+1)*(len2+1))
	for i in range(len1+1):
		d[(len2+1)*i]=i
	for j in range(len2+1):
		d[j]=j
	for i in range(1,len1+1):
		for j in range(1,len2+1):
			if mot1[i-1]==mot2[j-1]:
				cout=0
			else:
				cout=1
			d[(len2+1)*i+j]=min((d[(len2+1)*(i-1)+j]+1), (d[(len2+1)*i+j-1]+1), (d[(len2+1)*(i-1)+j-1]+cout))
	return d[(len2+1)*len1+len2]

class Recap():
	def __init__(self):
		self.name = "Recapitulatif"
		self.nametxt = "Recapitulatif.txt"
		self.nb_files = 0
		self.tableau_name = []
		self.tableau_langue = []
		self.tableau = []
	
	def add_data(self, nom, langue1, langue2):
		self.fiche = open(self.nametxt, "a")  # ou "a"? ou créer un conflit si le nom est déjà utilisé 
		definition = nom + ":" + langue1 + ":" + langue2 + '\n'
		self.fiche.write(definition)
		self.fiche.close()
	
	def read_file(self): #collecte ligne par ligne une première fois
		data = open(self.nametxt, "r")
		self.tableau = data.readlines()
		self.nb_files = len(self.tableau)
		data.close()

	def file_to_tableau(self): #convertit le fichier texte en un tableau ou on trouve en indice par les mots langue 1 et en pair les mots langue 2
		self.read_file()
		for i in range(self.nb_files):
			name = self.tableau[i].split(':', 1)[0] #mot dans la langue 1
			self.tableau_name.append(name) #(prend la position nb_words+i)
			word_intermediaire = self.tableau[i].split(':', 1)[1] #mot correspondant dans la langue 2 + saut de ligne
			langue = word_intermediaire.split('\n', 1)[0] #mot correspondant dans la langue 2

	def which_langue(self, index):
		self.read_file()
		lignesansnom = self.tableau[index].split(':', 1)[1]
		langue1 = lignesansnom.split(':',1)[0]
		intermed = lignesansnom.split(':',1)[1]
		langue2 = intermed.split('\n',1)[0]
		self.tableau_langue.append(langue1)
		self.tableau_langue.append(langue2)

