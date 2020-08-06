# COMP 120 (Programming and Abstractions)
# Author: Sophia Austin
# Date: February 13, 2020
# Description: GUI program to move a ball based on user commands.
import tkinter as tk # Import tkinter

class Move_ball():
	def __init__(self):
		""" Constructor """

		# Create window and give it a title
		window = tk.Tk() 
		window.title("Moving Ball")
		
		# Constants related to the program
		self.canvas_width = 300
		self.canvas_height = 200
		self.ball_init_x = self.canvas_width // 2
		self.ball_init_y = self.canvas_height // 2
		self.ball_radius = 10
		self.move_increment = 5
		self.highlightthickness = 10
		self.button_width = 5
		self.ball_tag = "ball"
		
		# Create canvas for the top of the window
		self.canvas = tk.Canvas(window, bg = "white", 
		        width = self.canvas_width, height = self.canvas_height, 
				highlightcolor = "black", highlightbackground = "black", 
				highlightthickness=self.highlightthickness)
		self.canvas.grid(row = 1, column = 1)
		self.ball = self.canvas.create_oval(self.ball_init_x - self.ball_radius, 
								self.ball_init_y - self.ball_radius,
								self.ball_init_x + self.ball_radius,
								self.ball_init_y + self.ball_radius,
								fill = "red", tags = self.ball_tag)
		
		# Create button frame.
		frame = tk.Frame(window)
		frame.grid(row = 2, column = 1)
		
		# Put the buttons in the frame.
		btLeft = tk.Button(frame, text = "Left", command = self.left, width = self.button_width)
		btLeft.grid(row = 1, column = 1)
		btRight = tk.Button(frame, text = "Right", command = self.right, width = self.button_width)
		btRight.grid(row = 1, column = 2)
		btUp = tk.Button(frame, text = "Up", command = self.up, width = self.button_width)
		btUp.grid(row = 1, column = 3)
		btDown = tk.Button(frame, text = "Down", command = self.down, width = self.button_width)
		btDown.grid(row = 1, column = 4)
		
		# Start the event loop
		window.mainloop() 


	def left(self):
		""" Move the ball left """
		pos = self.canvas.coords(self.ball)
		del_x = min(pos[0] - self.highlightthickness, self.move_increment)
		self.canvas.move("ball", -del_x, 0)
	
	def right(self):
		""" Move the ball right """
		pos = self.canvas.coords(self.ball)
		del_x = min(self.canvas_width + self.highlightthickness - pos[2], self.move_increment)
		self.canvas.move(self.ball, del_x, 0)
	
	def down(self):
		""" Move the ball down """
		pos = self.canvas.coords(self.ball)
		del_y = min(self.canvas_height + self.highlightthickness - pos[3], self.move_increment)
		self.canvas.move(self.ball, 0, del_y)
	
	def up(self):
		""" Move the ball up """
		pos = self.canvas.coords(self.ball)
		del_y = min(pos[1] - self.highlightthickness, self.move_increment)
		self.canvas.move("ball", 0, -del_y) # can also refer to the
						# ball by its tag.

if __name__ == "__main__":
	Move_ball()