#!/usr/bin/python3

class Animal:
	def talk(self):
		print("I have to talk something!")

	def walk(self):
		print(" I am walking")

	def clothes(self):
		print("I have my clothes here")

class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
    	super().walk()
    	print("Walking like a duck")

class Dog(Animal):
	def clothes(self):
		print("Dog clothes")

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

    fido = Dog()
    fido.walk()
    fido.clothes()

if __name__ == "__main__": main()
