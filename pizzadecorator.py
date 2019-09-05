from tkinter import *

class pizza(object):	
	def get_price(self):
		pass
	
class BaseJamon(pizza):	
	def get_price(self):
		return 10
		
class AbstractDecorator(pizza):	
	def __init__(self,decorated_pizza):
		self.decorated_pizza = decorated_pizza	

	def get_price(self):
		self.decorated_pizza.get_price()

class chorizo(AbstractDecorator):
	def __init__(self,decorated_pizza):
		AbstractDecorator.__init__(self,decorated_pizza)

	def get_price(self):
		return self.decorated_pizza.get_price() + 2

class jalapeño(AbstractDecorator):
	def __init__(self,decorated_pizza):
		AbstractDecorator.__init__(self,decorated_pizza)

	def get_price(self):
		return self.decorated_pizza.get_price() + 3

class queso(AbstractDecorator):
	def __init__(self,decorated_pizza):
		AbstractDecorator.__init__(self,decorated_pizza)

	def get_price(self):
		return self.decorated_pizza.get_price() + 4
		
class pepperoni(AbstractDecorator):
	def __init__(self,decorated_pizza):
		AbstractDecorator.__init__(self,decorated_pizza)

	def get_price(self):
		return self.decorated_pizza.get_price() + 1
		
class piña(AbstractDecorator):
	def __init__(self,decorated_pizza):
		AbstractDecorator.__init__(self,decorated_pizza)

	def get_price(self):
		return self.decorated_pizza.get_price() + 0.5

class app:

	def __init__(self):
		#configuracion de ventana
		self.ventana = Tk()		
		self.ventana.title("Pizza: Decorator")
		self.ventana.geometry("250x150")		
		
		
		#self.la_pizza = BaseJamon()
		#variables para los botones
		self.chorizobuttonvar = IntVar()
		self.jalapenobuttonvar = IntVar()
		self.quesobuttonvar = IntVar()
		self.pepperonibuttonvar = IntVar()
		self.pinabuttonvar = IntVar()		

		#botones para el cambio de precio
		self.chorizobutton = Checkbutton(self.ventana,text="chorizo", variable=self.chorizobuttonvar,command=self.chorizoaction)
		self.chorizobutton.grid(row=0)
		
		self.jalapenobutton = Checkbutton(self.ventana,text="jalapeno", variable=self.jalapenobuttonvar,command=self.jalapenoaction)
		self.jalapenobutton.grid(row=1)
		
		self.quesobutton = Checkbutton(self.ventana,text="queso", variable=self.quesobuttonvar,command=self.quesoaction)
		self.quesobutton.grid(row=2)
		
		self.pepperonibutton = Checkbutton(self.ventana,text="pepperoni", variable=self.pepperonibuttonvar,command=self.pepperoniaction)
		self.pepperonibutton.grid(row=3)
		
		self.pinabutton = Checkbutton(self.ventana,text="pina", variable=self.pinabuttonvar,command=self.pinaaction)
		self.pinabutton.grid(row=4)
		
		#botones para Crear pizza, precio
		self.buttonz = Button(self.ventana, text="Crear Pizza", command=self.CREAR)
		self.buttonz.grid(row=1,column=2)
		self.buttony = Button(self.ventana, text="Precio", command=self.precio)
		self.buttony.grid(row=2,column=2)
		
		#texto precio total
		self.label = Label(text="Precio total"  )
		self.label.grid(row=3,column=2)
		
		self.ventana.mainloop()
	
	#acciones para los botones	
	
	def chorizoaction(self):		
		try:
			self.la_pizza = chorizo(self.la_pizza)
			self.label.configure(text="Precio total = " + str( self.la_pizza.get_price() ) )			
		except AttributeError:
			self.label.configure(text="Crea una pizza primero."  )

	def jalapenoaction(self):		
		try:
			self.la_pizza = jalapeño(self.la_pizza)	
			self.label.configure(text="Precio total = " + str( self.la_pizza.get_price() ) )			
		except AttributeError:
			self.label.configure(text="Crea una pizza primero."  )

	def quesoaction(self):
		try:
			self.la_pizza = queso(self.la_pizza)
			self.label.configure(text="Precio total = " + str( self.la_pizza.get_price() ) )			
		except AttributeError:
			self.label.configure(text="Crea una pizza primero."  )

	def pepperoniaction(self):		
		try:
			self.la_pizza = pepperoni(self.la_pizza)
			self.label.configure(text="Precio total = " + str( self.la_pizza.get_price() ) )			
		except AttributeError:
			self.label.configure(text="Crea una pizza primero."  )

	def pinaaction(self):		
		try:
			self.la_pizza = piña(self.la_pizza)
			self.label.configure(text="Precio total = " + str( self.la_pizza.get_price() ) )			
		except AttributeError:
			self.label.configure(text="Crea una pizza primero."  )
			
	def CREAR(self):
		self.la_pizza = BaseJamon()
					
	def precio(self):		
		try:
			self.label.configure(text="Precio total = " + str( self.la_pizza.get_price() ) )			
		except AttributeError:
			self.label.configure(text="Crea una pizza primero."  )


app()

