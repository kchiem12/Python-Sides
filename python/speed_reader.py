from drawingpanel import *
import sys


def animate_text(panel, filename, width, height, font_size, wpm):
	panel = DrawingPanel(width, height)
	canvas = panel.canvas
	word_list = parse_words(filename)
	render_word(panel, canvas, word_list, width, height, font_size, wpm)


def parse_words(filename):
	f = open(filename, "r")
	lines = f.readlines()
	word_list = []
	for line in lines:
		if len(line) > 0:	
			for words in line.split():
				word_list.append(words)
	f.close()
	return word_list

def render_word(panel, canvas, lst_words, width, height, font_size, wpm):
	for words in lst_words:
		canvas.create_text(width / 2, height / 2, text = words, font = ("Courier", font_size))
		panel.sleep(60000 / wpm)
		panel.clear()

def main():
	filename = sys.argv[1]
	width = int(sys.argv[2])
	height = int(sys.argv[3])
	font_size = int(sys.argv[4])
	wpm = int(sys.argv[5])
	panel = ""
	animate_text(panel, filename, width, height, font_size, wpm)

main()




