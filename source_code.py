import random


''' Classe créant et lisant le fichier correspondant à une fiche d'interrogation'''
class fch_interro():
	def __init__(self):
		self.nb_words = 0
		self.name = ""
		self.langue1 = ""
		self.langue2 = ""
		self.nametxt = ""
		self.score = 0
		self.tableau = [] 
		self.to_guess = [] #tableau des question créés lors d'une interrogation
		self.answer = [] #tableau des réponses correspondantes

	''' Créer le fichier en préparation'''
	def create_file(self):
		self.nametxt = self.name + ".txt"
		self.fiche = open(self.nametxt, "a") 
		self.fiche.close()

	''' Ouvre le fichier en interrogation'''
	def open_file(self): 
		self.nametxt = self.name + ".txt"
		self.fiche = open(self.nametxt, "r") 
		self.fiche.close()

	'''Inscrit un couple de mot dans la fiche'''
	def collect_data(self, word_lg1, word_lg2):
		definition = word_lg1 + ":" + word_lg2 + '\n'
		self.fiche = open(self.nametxt, "a")
		self.fiche.write(definition)
		self.nb_words += 1
		self.fiche.close()

	'''Lis le fichier et reporte les lignes dans un tableau'''
	def read_file(self): 
		data = open(self.nametxt, "r")
		self.tableau = data.readlines()
		self.nb_words = len(self.tableau)
		data.close()

	'''Transforme le fichier en un tableau contenant tous les mots dans la langue 1 puis tous les mots dans la langue 2'''
	def file_to_tableau(self): 
		self.read_file()
		self.langue1 = self.tableau[0].split(':', 1)[0] #récupère l'information sur les langues de rédaction de la fiche
		langue_intermediaire = self.tableau[0].split(':', 1)[1] 
		self.langue2 = langue_intermediaire.split('\n', 1)[0]
		self.tableau = self.tableau[1:] #extrait du tableau de base ne contenant que les couples de mots et plus les langues
		self.nb_words -= 1
		for i in range(self.nb_words):
			word_lg1 = self.tableau[i].split(':', 1)[0] #mot dans la langue 1
			word_intermediaire = self.tableau[i].split(':', 1)[1] #mot correspondant dans la langue 2 + saut de ligne
			word_lg2 = word_intermediaire.split('\n', 1)[0] #mot correspondant dans la langue 2
			self.tableau[i] = word_lg1 
			self.tableau.append(word_lg2) #(prend la position nb_words+i)
		self.interrogate()

	'''Récupère de l'interface graphique l'information sur les langues d'interrogation'''
	def choose_lg(self): 
		if self.langue1 == self.langue_question:
			return 0
		if self.langue2 == self.langue_question:
			return 1
		else:
			print("Vous ne pouvez pas être intérrogé dans cette langue")

	'''créer un tableau de mots pour être intérogé dans un ordre au hasard ainsi que le tableau des réponses correspondantes'''
	def interrogate(self):
		couple_interro = [i for i in range(self.nb_words)]
		idx_language = self.choose_lg()
		for i in range(self.nb_words):
			idx_rdm = random.choice(couple_interro) #on choisit le couple de mot
			self.to_guess.append(self.tableau[idx_rdm + idx_language*self.nb_words])
			self.answer.append(self.tableau[idx_rdm + (1 - idx_language)*self.nb_words])
			couple_interro.remove(idx_rdm)

''' code pour la distance de levenshtein'''
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


'''Classe créer la fiche récapitulative contenant toutes les informations sur les fiches, les langues, les scores'''
class Recap():
	def __init__(self):
		self.name = "Recapitulatif"
		self.nametxt = "Recapitulatif.txt"
		self.nb_files = 0
		self.tableau_name = []
		self.tableau_langue = []
		self.tableau = []
	
	'''A la création d'une nouvelle fiche, rajoute le nom et les langues d'écriture'''
	def add_data(self, nom, langue1, langue2):
		self.fiche = open(self.nametxt, "a") 
		definition = nom + ":" + langue1 + ":" + langue2 + ":" + '\n'
		self.fiche.write(definition)
		self.fiche.close()
	
	'''Lis le fichier récapitulatif et inscrit les lignes dans un tableau'''
	def read_file(self):
		data = open(self.nametxt, "r")
		self.tableau = data.readlines()
		self.nb_files = len(self.tableau)
		data.close()

	'''Collecte les noms des fiches existantes'''
	def file_to_tableau(self):
		self.read_file()
		for i in range(self.nb_files):
			name = self.tableau[i].split(':', 1)[0] 
			self.tableau_name.append(name) 

	'''Pour la fiche choisie (index) récolte les langues possibles d'interrogation'''
	def which_langue(self, index):
		self.read_file()
		self.tableau_langue = []
		tableau_int = self.tableau[index].split(':')
		langue1 = tableau_int[1]
		langue2 = tableau_int[2]
		self.tableau_langue.append(langue1)
		self.tableau_langue.append(langue2)

	'''Pour la fiche choisie, indique les score déjà réalisés'''
	def recup_score(self, index):
		self.read_file()
		self.tableau_score = self.tableau[index].split(':')
		self.tableau_score = self.tableau_score[3:len(self.tableau_score)-1]

	'''Rajoute le nouveau score réalisé à la fiche correspondante'''
	def write_score(self, name, note):
		data = open(self.nametxt, "r")
		index_ligne = 0
		for line in data:
			if name in line:
				break
			else:
				index_ligne += 1
		data.close()
		old_text = self.tableau[index_ligne]
		new_text = old_text.split('\n',1)[0] + note + ":" + '\n'
		self.tableau[index_ligne] = new_text
		with open(self.nametxt, "w") as data:
			data.writelines(self.tableau)		 
		data.close()

