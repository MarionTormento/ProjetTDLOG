# si on clique directemet sur préparation terminée ça n'enregistre pas le mot, simple à remplacer mais du coup ça vaudrait le coup de vérifier si on a pas mis deux fois le meme mot dans uen liste et de supprimer les doublons du coup 
#combo box pyqt qui présente la liste des fiches
# vous avez répondu ça qui été faux, l'attendu c'était ça juste

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL
from source_code import *
from leven import *
import os

''' Crée la fiche, la nomme et la prépare'''
class creer_fiche(QtGui.QWidget):

	def __init__(self):
		super(creer_fiche, self).__init__()
		self.f = fch_interro()
		self.setWindowTitle("Nommer votre fiche de révsion")
		'''Champs pour rentrer le nom'''
		self.titre_name=QtGui.QLabel("Nom de la fiche")
		self.line_name=QtGui.QLineEdit(self)
		'''Champs pour définir les langues de la fiche'''
		self.titre_langue1=QtGui.QLabel("Langue 1 :")
		self.line_langue1=QtGui.QLineEdit(self)
		self.titre_langue2=QtGui.QLabel("Langue 2 :")
		self.line_langue2=QtGui.QLineEdit(self)
		'''Enregistrer le nom'''
		self.bouton_name=QtGui.QPushButton("Ok",self)
		self.bouton_name.clicked.connect(self.ok_name)
		'''On place le tout dans la fenêtre'''
		posit = QtGui.QGridLayout()
		posit.addWidget(self.titre_name,0,0)
		posit.addWidget(self.line_name,0,1)
		posit.addWidget(self.titre_langue1,1,0)
		posit.addWidget(self.line_langue1,1,1)
		posit.addWidget(self.titre_langue2,2,0)
		posit.addWidget(self.line_langue2,2,1)
		posit.addWidget(self.bouton_name,3,0)
		self.setLayout(posit)
		
	def ok_name(self):
		'''Récupération du nom'''
		self.f.name = self.line_name.text()
		'''Récupération des langues'''
		self.f.langue1 = self.line_langue1.text()
		self.f.langue2 = self.line_langue2.text()
		'''Appel du create_file'''
		self.f.create_file() #Appelle le create_file du code source
		self.close()
		'''Lancement de la préparation'''		
		self.prepa_fiche = Preparation(self.f)
		self.prepa_fiche.show()		


class Preparation(QtGui.QWidget):

	def __init__(self, fch_interro):
		super(Preparation,self).__init__()
		'''Lie la préparation à une fiche déjà créée et nommée'''
		self.f = fch_interro
		self.setWindowTitle("Preparation de la fiche " + fch_interro.name)
		'''Champs pour rentrer les mots'''
		self.line1=QtGui.QLineEdit(self)
		self.line2=QtGui.QLineEdit(self)
		'''On définit des titres aux champs'''
		self.titre1=QtGui.QLabel(self.f.langue1)
		self.titre2=QtGui.QLabel(self.f.langue2)
		'''Bouton pour passer à une définition suivante'''
		self.bouton=QtGui.QPushButton("Définition suivante",self)
		self.bouton.clicked.connect(self.ok_m)
		'''Bouton pour terminer la préparation'''
		self.terminer=QtGui.QPushButton("Préparation terminée",self)
		self.terminer.clicked.connect(self.fermer)
		'''On place le tout dans la fenêtre'''
		posit = QtGui.QGridLayout()
		posit.addWidget(self.titre1,0,0)
		posit.addWidget(self.titre2,1,0)
		posit.addWidget(self.line1,0,1)
		posit.addWidget(self.line2,1,1)
		posit.addWidget(self.bouton,2,0)
		posit.addWidget(self.terminer,3,0)
		self.setLayout(posit)

	def ok_m(self):
		'''Récupération des valeurs'''
		word_lg1 = self.line1.text()
		word_lg2 = self.line2.text()
		self.f.collect_data(word_lg1, word_lg2)
		self.line1.clear()
		self.line2.clear()

	def fermer(self):
		self.ok_m()
		self.close()

	
class choose_fiche(QtGui.QWidget):

	def __init__(self):
		super(choose_fiche, self).__init__()
		self.f = fch_interro() #ouvre une nouvelle fiche
		self.setWindowTitle("Sur quel thème souhaitez vous être interrogé ?")
		'''Champs pour rentrer le nom'''
		self.titre_name=QtGui.QLabel("Nom de la fiche :")
		self.line_name=QtGui.QLineEdit(self)
		'''Champs pour demander de quelle langue vers quelle langue'''
		self.titre_langue_question=QtGui.QLabel("Traduction de :")
		self.line_langue_question=QtGui.QLineEdit(self)
		self.titre_langue_reponse=QtGui.QLabel("Vers :")
		self.line_langue_reponse=QtGui.QLineEdit(self)
		'''Enregistrer le nom + sens évaluation'''
		self.bouton_name=QtGui.QPushButton("Ok",self)
		self.bouton_name.clicked.connect(self.choose_name)
		'''On place le tout dans la fenêtre'''
		posit = QtGui.QGridLayout()
		posit.addWidget(self.titre_name,0,0)
		posit.addWidget(self.line_name,0,1)
		posit.addWidget(self.titre_langue_question,1,0)
		posit.addWidget(self.line_langue_question,1,1)
		posit.addWidget(self.titre_langue_reponse,2,0)
		posit.addWidget(self.line_langue_reponse,2,1)
		posit.addWidget(self.bouton_name,4,0)
		self.setLayout(posit)
		
	def choose_name(self):
		'''Récupération du nom'''
		self.f.name = self.line_name.text()
		'''Récupération du sens de traduction'''
		langue_question=self.line_langue_question.text()
		langue_reponse=self.line_langue_question.text()
		'''Ouvre fiche avec nom existant'''
		self.f.open_file() #ouvre la fiche avec le nom déjà existant
		# amélioration: vérification que la fiche existe, sinon on dit fuck => leven?, proposition des fiches qui existe déjà
		self.close()
		'''Lancement de l'Evaluation'''		
		self.evaluation_fiche = Evaluation(self.f)
		self.evaluation_fiche.show()	


# l'idée : reprendre un code en format comme interogation ou la première fenêtre permet de choisir le fichier sur lequel on veut être interroger
class Evaluation(QtGui.QWidget):

	def __init__(self, fiche):
		super(Evaluation,self).__init__()
		'''Lie l'évaluation à la fiche choisie'''
		self.f = fiche
		self.f.file_to_tableau() #récupère les mots en un tableau [mot langue 1.... mot langue 2...]
		self.index_question = 0
		self.setWindowTitle("Evaluation")
		'''Champs d'interrogation'''
		self.question=QtGui.QLineEdit(self)
		self.reponse=QtGui.QLineEdit(self)
		'''On définit des titres aux champs'''
		self.titre_question=QtGui.QLabel("Traduis :")
		self.titre_reponse=QtGui.QLabel("Réponse :")
		'''Bouton pour passer à une définition suivante'''
		self.bouton=QtGui.QPushButton("Mot suivant",self)
		self.bouton.clicked.connect(self.mot_suivant)
		'''Bouton pour terminer la préparation'''
		self.terminer=QtGui.QPushButton("Évaluation finie",self)
		self.terminer.clicked.connect(self.fermer)
		'''On place le tout dans la fenêtre'''
		posit=QtGui.QGridLayout()
		posit.addWidget(self.titre_question,0,0)
		posit.addWidget(self.titre_reponse,1,0)
		posit.addWidget(self.question,0,1)
		posit.addWidget(self.reponse,1,1)
		posit.addWidget(self.bouton,2,0)
		posit.addWidget(self.terminer,3,0)
		self.setLayout(posit)
		self.reinit()

	def reinit(self):
		self.question.setText(self.f.to_guess[self.index_question])
		self.reponse.setText("")
				
	def mot_suivant(self):
		user_answer = self.reponse.text()
		distance = distance_levenshtein(self.f.answer[self.index_question], user_answer)
		if distance == 0:
			self.f.score += 1
		if distance == 1:
			self.f.score += 0.5
		self.index_question += 1
		if self.index_question >= self.f.nb_words:
			self.question.setText("Partie Terminée")
			note = str(self.f.score) + "/" + str(self.f.nb_words)
			self.reponse.setText("Ton score est de " + note)
		else:
			self.reinit()

	def fermer(self):
		self.close()


class InterfaceGraphique(QtGui.QMainWindow):
	
	def __init__(self):
		super(InterfaceGraphique,self).__init__()
		self.d = Directory()
		self.setGeometry(300,300,290,150)
		self.setWindowTitle("Aide à la révision")
		'''Bouton préparation'''
		self.boutonPreparation=QtGui.QPushButton("Préparation",self)#création de l'onglet de préparation
		self.boutonPreparation.move(20,20)
		self.boutonPreparation.clicked.connect(self.preparer)#appel de la fonction si on clique sur l'onglet
		'''Bouton évaluation'''
		self.boutonEvaluation=QtGui.QPushButton("Evaluation",self)#création de l'onglet d'évaluation
		self.boutonEvaluation.move(150,20)
		self.boutonEvaluation.clicked.connect(self.evaluer)#appel de la fonction si on clique sur cet onglet

	
	def preparer(self):
		os.chdir(self.d.fiche_path)
		'''On fait appel à la classe creer_fiche pour créer la fiche, cette classe appelera la préparation'''
		self.fiche = creer_fiche()
		self.fiche.show()

	def evaluer(self):
		self.eval = choose_fiche()
		self.eval.show()

class Directory():
	def __init__(self):
		self.current_path = os.getcwd()
		self.fiche_path = self.current_path + "\Fiches"
		self.stats_path = self.current_path + "\Stastistiques"
		if not os.path.exists(self.fiche_path):
			os.makedirs(self.fiche_path)
		if not os.path.exists(self.stats_path):
			os.makedirs(self.stats_path)


def main():
	app=QtGui.QApplication(sys.argv)
	directory = Directory()
	interface=InterfaceGraphique()
	interface.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()