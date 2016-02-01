# si on clique directemet sur préparation terminée ça n'enregistre pas le mot, simple à remplacer mais du coup ça vaudrait le coup de vérifier si on a pas mis deux fois le meme mot dans uen liste et de supprimer les doublons du coup 
#combo box pyqt qui présente la liste des fiches
# vous avez répondu ça qui été faux, l'attendu c'était ça juste

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL
from source_code import *
import os
import random
import numpy as np
import pyqtgraph as pg 

''' Classe qui crée la fiche, la nomme et la prépare'''
class creer_fiche(QtGui.QWidget):

	def __init__(self):
		super(creer_fiche, self).__init__()
		self.f = fch_interro()
		self.recap = Recap()
		self.setWindowTitle("Nommez votre fiche de révision")
		'''Champs pour rentrer le nom'''
		self.titre_name=QtGui.QLabel("Nom de la fiche")
		self.line_name=QtGui.QLineEdit(self)
		'''Menu déroulant pour définir les langues de la fiche'''
		self.titre_langue1=QtGui.QLabel("Langue 1 :")
		self.line_langue1=QtGui.QComboBox(self)
		self.line_langue1.addItem("Français")
		self.line_langue1.addItem("Anglais")
		self.line_langue1.addItem("Espagnol")
		'''On appelle la fonction menu langue'''
		self.line_langue1.activated.connect(self.menu_langue)
		self.titre_langue2=QtGui.QLabel("Langue 2 :")
		self.line_langue2=QtGui.QComboBox(self)
		'''Enregistrer le nom et les langues'''
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

		'''Fonction menu langue : permet de enregistrer la langue 1 choisie et de éliminer cette langue des choix de langue2'''
	def menu_langue(self):
		'''On récupère l'indice de la langue 1 choisie'''
		index_langue = self.line_langue1.currentIndex()
		self.line_langue2.clear()
		'''On propose des langues pour la langue 2 en fonction de la langue 1 choisie'''
		if index_langue == 0:
			self.line_langue2.addItem("Anglais")
			self.line_langue2.addItem("Espagnol")
		if index_langue == 1:
			self.line_langue2.addItem("Français")
			self.line_langue2.addItem("Espagnol")
		if index_langue == 2:
			self.line_langue2.addItem("Français")
			self.line_langue2.addItem("Anglais")


	def ok_name(self):
		'''Récupération du nom de la fiche'''
		self.f.name = self.line_name.text()
		'''Récupération des langues de la fiche'''
		self.f.langue1 = self.line_langue1.currentText()
		self.f.langue2 = self.line_langue2.currentText()
		'''Appel du create_file : on crée une fiche txt'''
		self.f.create_file()
		self.recap.add_data(self.f.name, self.f.langue1, self.f.langue2)
		self.close()
		self.f.collect_data(self.f.langue1, self.f.langue2)
		'''Lancement de la préparation'''		
		self.prepa_fiche = Preparation(self.f)
		self.prepa_fiche.show()		

'''Classe qui lance la préparation'''
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
		'''Récupération des mots rentrés par l'utilisateur'''
		word_lg1 = self.line1.text()
		word_lg2 = self.line2.text()
		self.f.collect_data(word_lg1, word_lg2)
		'''On efface ces mots pour pouvoir rentrer une série suivante'''
		self.line1.clear()
		self.line2.clear()

	def fermer(self):
		self.ok_m()
		self.close()

'''Classe permettant de choisir la fiche et les langues de l'évaluation'''
class choose_fiche(QtGui.QWidget):

	def __init__(self):
		super(choose_fiche, self).__init__()
		self.f = fch_interro() #ouvre une nouvelle fiche
		self.r = Recap()
		self.r.file_to_tableau()
		self.setWindowTitle("Sur quel thème souhaitez vous être interrogé ?")
		'''Champs titre'''
		self.titre_name=QtGui.QLabel("Nom de la fiche :")
		'''On demande à l'utilisateur de choisir une fiche parmi celles existantes à l'aide d'un menu déroulant'''
		self.line_name=QtGui.QComboBox(self)
		for i in range(self.r.nb_files):
			self.line_name.addItem(self.r.tableau_name[i])
		'''On demande à l'utilisateur de choisir le sens de traduction à l'aide de menu déroulant'''
		self.titre_langue_question=QtGui.QLabel("Traduction de :")
		self.line_langue_question=QtGui.QComboBox(self)
		self.titre_langue_reponse=QtGui.QLabel("Vers :")
		self.line_langue_reponse=QtGui.QComboBox(self)
		self.line_name.activated.connect(self.menu_langue)
		'''Enregistrer le nom + sens évaluation'''
		self.bouton_name=QtGui.QPushButton("Ok",self)
		self.bouton_name.clicked.connect(self.choose_name)
		'''On place le tout dans la fenêtre'''
		posit = QtGui.QGridLayout()
		posit.addWidget(self.titre_name,0,0)
		posit.addWidget(self.line_name,0,1)
		posit.addWidget(self.bouton_name,4,0)
		posit.addWidget(self.titre_langue_question,1,0)
		posit.addWidget(self.line_langue_question,1,1)
		posit.addWidget(self.titre_langue_reponse,2,0)
		posit.addWidget(self.line_langue_reponse,2,1)
		self.setLayout(posit)
		
	def menu_langue(self):
		'''Champs pour demander de quelle langue vers quelle langue'''
		index_file = self.line_name.currentIndex()
		self.r.which_langue(index_file)
		self.line_langue_question.clear()
		self.line_langue_reponse.clear()
		'''On propose à l'utilisateur une langue de départ parmi les deux définies dans la fiche'''
		for i in range(2):
			self.line_langue_question.addItem(self.r.tableau_langue[i])
		'''On appelle la fonction choix_langue_question'''
		self.line_langue_question.activated.connect(self.choix_langue_question)
		for i in range(2):
			self.line_langue_reponse.addItem(self.r.tableau_langue[i])

	'''Fonction permettant de définir la langue d'arrivée en éliminant la langue de départ des choix possibles'''
	def choix_langue_question(self):
		index_langue = self.line_langue_question.currentIndex()
		self.line_langue_reponse.clear()	
		self.line_langue_reponse.addItem(self.r.tableau_langue[1-index_langue])

	def choose_name(self):
		'''Récupération du nom'''
		self.f.name = self.line_name.currentText()
		'''Récupération du sens de traduction'''
		self.f.langue_question=self.line_langue_question.currentText()
		self.f
		self.f.langue_reponse=self.line_langue_question.currentText()
		'''Ouvre fiche avec nom existant'''
		self.f.open_file() 
		self.close()
		'''Lancement de l'Evaluation'''		
		self.evaluation_fiche = Evaluation(self.f)
		self.evaluation_fiche.show()	

'''Classe qui lance l'évaluation'''
class Evaluation(QtGui.QWidget):

	def __init__(self, fiche):
		super(Evaluation,self).__init__()
		self.r = Recap()
		self.r.read_file()
		self.erreur_to_guess = []
		self.erreur_answer = []
		self.erreur_user_answer = []
		self.note = 0
		'''Lie l'évaluation à la fiche choisie'''
		self.f = fiche
		self.f.file_to_tableau() #récupère les mots en un tableau [mot langue 1.... mot langue 2...]
		self.index_question = 0
		self.setWindowTitle("Evaluation")
		'''Champs d'interrogation'''
		self.question=QtGui.QLabel(self)
		self.reponse=QtGui.QLineEdit(self)
		'''On définit des titres aux champs'''
		self.titre_question=QtGui.QLabel("Traduis :")
		self.titre_reponse=QtGui.QLabel("Réponse :")
		'''Bouton pour passer à une définition suivante'''
		if self.f.nb_words == 1:
			self.bouton = QtGui.QPushButton("Evaluation Terminée", self)
		else:
			self.bouton=QtGui.QPushButton("Mot suivant",self)
		self.bouton.clicked.connect(self.mot_suivant)
		'''On place le tout dans la fenêtre'''
		posit=QtGui.QGridLayout()
		posit.addWidget(self.titre_question,0,0)
		posit.addWidget(self.titre_reponse,1,0)
		posit.addWidget(self.question,0,1)
		posit.addWidget(self.reponse,1,1)
		posit.addWidget(self.bouton,2,0)
		self.setLayout(posit)
		self.reinit()

	def reinit(self):
		'''Permet de proposer une question aléatoire à l'utilisateur'''
		self.question.setText(self.f.to_guess[self.index_question])
		self.reponse.setText("")
				
	def mot_suivant(self):
		'''On enregistre la réponse de l'utilisateur'''
		user_answer = self.reponse.text()
		'''On calcule la distance de levenshtein entre la réponse utilisateur et la réponse attendue'''
		distance = distance_levenshtein(self.f.answer[self.index_question], user_answer)
		'''Choix des critères d'évaluation'''
		'''Distance de zéro, l'utilisateur a un point'''
		if distance == 0:
			self.f.score += 1
		'''Distance de un, l'utilisateur a un demi point'''
		if distance == 1:
			self.f.score += 0.5
			self.erreur_to_guess.append(self.f.to_guess[self.index_question]) 
			self.erreur_answer.append(self.f.answer[self.index_question])
			self.erreur_user_answer.append(user_answer)
		'''Distance supérieure à un, l'utilisateur a zéro'''
		if distance > 1:
			self.erreur_to_guess.append(self.f.to_guess[self.index_question]) 
			self.erreur_answer.append(self.f.answer[self.index_question])
			self.erreur_user_answer.append(user_answer)
		self.index_question += 1
		'''Evaluation terminée quand on arrive à la fin des questions'''
		if self.index_question == self.f.nb_words - 1:
			self.bouton.setText("Evaluation Terminée")
		'''On enregistre le score final et on lance la fenêtre préparation terminée'''
		if self.index_question >= self.f.nb_words:
			self.note = str(self.f.score) + "/" + str(self.f.nb_words)
			self.r.write_score(self.f.name, self.note)
			self.termin = PartieTermin(self.erreur_to_guess, self.erreur_answer, self.erreur_user_answer, self.note)
			self.termin.show()
			self.close()
		else:
			self.reinit()

'''Classe qui permet d'afficher le score et la correction à l'issue de l'évaluation'''
class PartieTermin(QtGui.QWidget):
	
	def __init__(self, a_traduire, reponse_juste, reponse_user ,note):
		super(PartieTermin,self).__init__()
		'''On prend le tableau récapitulatif des erreurs'''
		self.to_guess = a_traduire
		self.answer = reponse_juste
		self.user_answer = reponse_user
		self.score = note
		'''Titre de la fenêtre'''
		self.setWindowTitle("TADAAAA")
		'''Affichage score'''
		self.titre = QtGui.QLabel("Évaluation terminée!")
		self.affiche_score = QtGui.QLabel("Vous avez obtenu un score de : "+ str(note))
		index = len(self.to_guess)
		if index == 0:
			self.annonce_erreur = QtGui.QLabel("Vous n'avez fait aucune erreur, bravo!")
		else: 
			'''On précise à l'utilisateur ses erreurs et la réponse attendue'''
			self.annonce_erreur = QtGui.QLabel("Vos erreurs sont les suivantes")
			self.question = QtGui.QLabel("Question")
			self.reponse = QtGui.QLabel("Réponse Attendue")
			self.votre_reponse = QtGui.QLabel("Votre réponse")
			self.affiche_question = []
			self.affiche_reponse = []
			self.affiche_user_reponse = []
			for i in range(index):
				self.affiche_question.append(QtGui.QLabel(self.to_guess[i]))
				self.affiche_reponse.append(QtGui.QLabel(self.answer[i]))
				self.affiche_user_reponse.append(QtGui.QLabel(self.user_answer[i]))
		'''On positionne le tout'''
		posit=QtGui.QGridLayout()
		posit.addWidget(self.titre,0,0)
		posit.addWidget(self.affiche_score,1,0)
		posit.addWidget(self.annonce_erreur,2,0)
		if index != 0:
			posit.addWidget(self.question, 3, 0)
			posit.addWidget(self.reponse, 3, 1)
			posit.addWidget(self.votre_reponse, 3, 2)
			for i in range(index):
				posit.addWidget(self.affiche_question[i],4+i,0)
				posit.addWidget(self.affiche_reponse[i], 4+i, 1)
				posit.addWidget(self.affiche_user_reponse[i], 4+i, 2)
		self.setLayout(posit)

'''Fenêtre principale du logiciel'''
class InterfaceGraphique(QtGui.QMainWindow):
	
	def __init__(self):
		super(InterfaceGraphique,self).__init__()
		self.d = Directory()
		self.setGeometry(300,300,290,150)
		self.setWindowTitle("ANMA : Aide à la révision")
		'''Bouton préparation'''
		self.boutonPreparation=QtGui.QPushButton("Préparation",self)#création de l'onglet de préparation
		self.boutonPreparation.move(20,20)
		self.boutonPreparation.setStyleSheet("background-color:green")
		self.boutonPreparation.clicked.connect(self.preparer)#appel de la fonction si on clique sur l'onglet
		'''Bouton évaluation'''
		self.boutonEvaluation=QtGui.QPushButton("Evaluation",self)#création de l'onglet d'évaluation
		self.boutonEvaluation.move(150,20)
		self.boutonEvaluation.setStyleSheet("background-color:red")
		self.boutonEvaluation.clicked.connect(self.evaluer)#appel de la fonction si on clique sur cet onglet
		'''Bouton Statistiques'''
		self.boutonStat=QtGui.QPushButton("Tes statistiques",self)
		self.boutonStat.clicked.connect(self.statistiques)#appel de la fonction si on clique sur cet onglet
		self.boutonStat.move(85,50)
		self.boutonStat.setStyleSheet("background-color:yellow")
	
	def preparer(self):
		os.chdir(self.d.fiche_path)
		'''On fait appel à la classe creer_fiche pour créer la fiche, cette classe appelera la préparation'''
		self.fiche = creer_fiche()
		self.fiche.show()

	def evaluer(self):
		os.chdir(self.d.fiche_path)
		self.eval = choose_fiche()
		self.eval.show()

	def statistiques(self):
		os.chdir(self.d.fiche_path)
		self.stat = Statistiques()
		self.stat.show()

'''Classe qui permet d'accéder aux fiches créées'''
class Directory():
	def __init__(self):
		self.current_path = os.getcwd()
		self.fiche_path = self.current_path + "\Fiches"
		if not os.path.exists(self.fiche_path):
			os.makedirs(self.fiche_path)

'''Classe permettant à l'utilisateur d'avoir accès à ses statistiques'''
class Statistiques(QtGui.QWidget):
	
	def __init__(self):
		super(Statistiques,self).__init__()
		self.r = Recap()
		self.r.file_to_tableau()
		self.setGeometry(300,300,290,150)
		self.setWindowTitle("Tes statistiques")
		self.titre_name=QtGui.QLabel("Nom de la fiche :")
		'''L'utilisateur choisit la fiche sur laquelle il veut avoir accès à ses statistiques'''
		self.line_name=QtGui.QComboBox(self)
		for i in range(self.r.nb_files):
			self.line_name.addItem(self.r.tableau_name[i])
		self.line_name.activated.connect(self.menu_score)
		'''On place le tout dans la fenêtre'''
		posit = QtGui.QGridLayout()
		posit.addWidget(self.titre_name,0,0)
		posit.addWidget(self.line_name,0,1)
		self.setLayout(posit)
	

	def ramener_note(self):
		note_ramen=[]
		for i in range(len(self.r.tableau_score)):
			note = self.r.tableau_score[i].split('/',1)[0]
			intermed = self.r.tableau_score[i].split('/',1)[1]
			nb_question = intermed.split('/n',1)[0]
			note_ramen.append(20*float(note)/float(nb_question))
		return (note_ramen)

	def menu_score(self):
		'''On enregistre la fiche sélectionnée par l'utilisateur '''
		index_file = self.line_name.currentIndex()
		self.r.recup_score(index_file)
		'''On définit les axes du plot'''
		self.x= list(range(1,len(self.r.tableau_score)+1))
		'''On ramène les notes sur 20'''
		self.y=self.ramener_note()
		'''Ouvre le graphe dans une autre fenêtre'''
		self.courbe=pg.plot()
		self.courbe.addLegend()
		self.courbe.setLabel('left','Notes (/20)')
		self.courbe.setLabel('bottom',"Sessions d'évaluation")
		self.courbe.plot(self.x,self.y,pen='r', name=self.line_name.currentText())
		self.close()


'''Programme principal'''
def main():
	app=QtGui.QApplication(sys.argv)
	interface=InterfaceGraphique()
	interface.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()