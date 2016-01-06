import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL

from source_code import *

class Preparation(QtGui.QWidget):

	def __init__(self,parent=None):
		super(Preparation,self).__init__(parent)
		self.setWindowTitle("Preparation")
		'''Champs pour rentrer les mots'''
		self.line1=QtGui.QLineEdit(self)
		self.line2=QtGui.QLineEdit(self)
		'''Bouton pour passer à une définition suivante'''
		self.bouton=QtGui.QPushButton("Définition suivante",self)
		self.bouton.clicked.connect(self.ok_m)
		'''Bouton pour terminer la préparation'''
		self.terminer=QtGui.QPushButton("Préparation terminée",self)
		self.terminer.clicked.connect(self.fermer)
		'''On place le tout dans la fenêtre'''
		posit=QtGui.QGridLayout()
		posit.addWidget(self.line1,0,0)
		posit.addWidget(self.line2,1,0)
		posit.addWidget(self.bouton,2,0)
		posit.addWidget(self.terminer,3,0)
		self.setLayout(posit)
		'''Liste pour mise en mémoire'''
		self.french=[]
		self.english=[]

	def ok_m(self):
		'''Récupération des valeurs'''
		fr=self.line1.text()
		eng=self.line2.text()
		self.french.append(fr)
		self.english.append(eng)
		print(self.french)
		print(self.english)
		self.line1.clear()
		self.line2.clear()

	def fermer(self):
		self.close

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
		self.prepa=Preparation()
		self.prepa.show()

def main():
	app=QtGui.QApplication(sys.argv)
	interface=InterfaceGraphique()
	interface.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()