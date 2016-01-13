import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL
import random

class Preparation(QtGui.QWidget):

	def __init__(self,parent=None):
		super(Preparation,self).__init__(parent)
		self.setWindowTitle("Preparation")
		'''Champs pour rentrer les mots'''
		self.champ1=QtGui.QLineEdit(self)
		self.champ2=QtGui.QLineEdit(self)
		'''Bouton pour passer à une définition suivante'''
		self.bouton=QtGui.QPushButton("Mot suivant",self)
		self.bouton.clicked.connect(self.ok_m)
		'''Bouton pour terminer la préparation'''
		self.terminer=QtGui.QPushButton("Préparation terminée",self)
		self.terminer.clicked.connect(self.fermer)
		'''On place le tout dans la fenêtre'''
		posit=QtGui.QGridLayout()
		posit.addWidget(self.champ1,0,0)
		posit.addWidget(self.champ2,1,0)
		posit.addWidget(self.bouton,2,0)
		posit.addWidget(self.terminer,3,0)
		self.setLayout(posit)
		'''Liste pour mise en mémoire'''
		self.french=[]
		self.english=[]

	def ok_m(self):
		'''Récupération des valeurs'''
		fr=self.champ1.text()
		eng=self.champ2.text()
		self.french.append(fr)
		self.english.append(eng)
		print(self.french)
		print(self.english)
		self.champ1.clear()
		self.champ2.clear()

	def fermer(self):
		self.close

class Evaluation(QtGui.QWidget):

	def __init__(self,parent=None):
		super(Evaluation,self).__init__(parent)
		self.setWindowTitle("Evaluation")
		'''Liste de départ qui contient les mots'''
		self.french=['tortue','écureuil','poisson']
		self.english=['turtle','squirrel','fish']
		'''Liste qui met en mémoire les réponses'''
		self.eval_french=[]
		self.eval_eng=[]
		'''Liste qui conserve les numéros des questions'''
		self.numero=[]
		'''Numéro question posée'''
		self.num=0
		'''Compteur de points'''
		self.note=0
		'''Champs d'interrogation'''
		self.question=QtGui.QLineEdit(self)
		self.reponse=QtGui.QLineEdit(self)
		'''Bouton pour passer à une définition suivante'''
		self.bouton=QtGui.QPushButton("Mot suivant",self)
		self.bouton.clicked.connect(self.mot_suivant)
		'''Bouton pour terminer la préparation'''
		self.terminer=QtGui.QPushButton("Évaluation finie",self)
		self.terminer.clicked.connect(self.fermer)
		'''On place le tout dans la fenêtre'''
		posit=QtGui.QGridLayout()
		posit.addWidget(self.question,0,0)
		posit.addWidget(self.reponse,1,0)
		posit.addWidget(self.bouton,2,0)
		posit.addWidget(self.terminer,3,0)
		self.setLayout(posit)
		self.reinit()

	def reinit(self):
		for i in range(len(self.numero)):
			while self.num==self.numero[i]:
				self.num=random.randint(0,len(self.french)-1)
		self.numero.append(self.num)
		self.question.setText(self.french[self.num])
		self.reponse.setText("")
		
		
	def mot_suivant(self):
		'''Récupération des valeurs'''
		if len(self.eval_french)<len(self.french):
			fr=self.question.text()
			eng=self.reponse.text()
			self.eval_french.append(fr)
			self.eval_eng.append(eng)
			print(self.eval_french)
			print(self.eval_eng)
			if eng==self.english[self.num]:
				self.note +=1
			else:
				self.note +=0
			self.reinit()
		else:
			self.question.clear()
			self.reponse.clear()
			print ("c'est fini")
			print(self.note)

	def fermer(self):
		self.close()

class InterfaceGraphique(QtGui.QMainWindow):
	
	def __init__(self,parent=None):
		super(InterfaceGraphique,self).__init__(parent)
		
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
		'''On fait appel à la classe préparation'''
		self.prepa=Preparation()
		self.prepa.show()

	def evaluer(self):
		self.eval=Evaluation()
		self.eval.show()

def main():
	app=QtGui.QApplication(sys.argv)
	interface=InterfaceGraphique()
	interface.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()

