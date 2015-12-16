import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class InterfaceGraphique(QtGui.QWidget):
	
	def __init__(self):
		super(InterfaceGraphique,self).__init__()
		self.initUI()
	
	def initUI(self):
		self.boutonPreparation=QtGui.QPushButton("Préparation",self)#création de l'onglet de préparation
		self.boutonPreparation.move(20,20)
		self.boutonPreparation.clicked.connect(self.preparer)#appel de la fonction si on clique sur l'onglet
		
		self.boutonEvaluation=QtGui.QPushButton("Evaluation",self)#création de l'onglet d'évaluation
		self.boutonEvaluation.move(150,20)
		self.boutonEvaluation.clicked.connect(self.evaluer)#appel de la fonction si on clique sur cet onglet

		self.liste_francais=[]
		self.liste_anglais=[]

		self.setGeometry(300,300,290,150)
		self.setWindowTitle("Aide à la révision")
		self.show()
	
	def preparer(self):
		francais, ok1=QtGui.QInputDialog.getText(self,"Préparation","Mot français:")#on rentre le mot français
		anglais, ok2=QtGui.QInputDialog.getText(self,"Préparation","Mot anglais:")#on rentre la traduction
		if ok1 and ok2:
			self.liste_francais.append(francais)#mise en mémoire
			self.liste_anglais.append(anglais)#mise en mémoire
			print(self.liste_francais)#affiche (mot)
			print(self.liste_anglais)#affiche (mot)

	def evaluer(self):
		dialogue=QtGui.QInputDialog.getText(self,"Evaluation","Mot français:")

def main():
	app=QtGui.QApplication(sys.argv)
	interface=InterfaceGraphique()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()