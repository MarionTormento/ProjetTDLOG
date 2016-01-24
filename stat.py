import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL
import random
#import numpy as np
import pyqtgraph as pg 

'''Ce qu'on a à la base : une liste avec les notes, 
une liste avec le nombre de questions posées'''

'''Les dates des sessions'''


class Statistiques(QtGui.QWidget):
	
	def __init__(self,date,note,nb_question):
		super(Statistiques,self).__init__()
		self.setGeometry(300,300,290,150)
		self.setWindowTitle("Tes statistiques")
		'''On définit les axes du plot'''
		self.x=date
		self.note=note
		self.nb_question=nb_question
		self.y=self.ramener_note()
		'''Ouvre le graphe dans une autre fenêtre'''
		self.courbe=pg.plot(self.x,self.y,pen='r')
		
		

	def ramener_note(self):
		note_ramen=[]
		for i in range(len(self.note)):
			note_ramen.append(20*self.note[i]/self.nb_question[i])
		return (note_ramen)

def main():
	app=QtGui.QApplication(sys.argv)
	note=[4,5,6,8,3,6]
	nb_question=[10,6,7,12,6,6]
	date=[1,2,3,4,5,6]
	Stat=Statistiques(date,note,nb_question)
	Stat.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()

