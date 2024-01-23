#!/usr/bin/env python3

CELL_SIZE = 10;
HEIGHT = 63;
WIDTH = 80;
GRID_THICKNESS = 0.3
RADIUS = 3
TEXT_VERTICAL_OFFSET = 1.6
BLACK = "#222"
GRID_COLOR = "#555"

import svgwrite

def cross_box(x,y):
	group = svg_document.g(id='cross_box_{}_{}'.format(x, y))
	x = x*CELL_SIZE
	y = y*CELL_SIZE
	group.add(
		svg_document.rect(
			insert = (x, y),
			size = (CELL_SIZE, CELL_SIZE),
			fill = "#000000",
			fill_opacity = 0,
		)
		.stroke(BLACK, width=GRID_THICKNESS*2)
	)
	group.add(
		svg_document.line(
			start=(x,y), end=(x+CELL_SIZE,y+CELL_SIZE)
		)
		.stroke(BLACK, width=GRID_THICKNESS)
		.dasharray([1,1], offset="75%")
	)
	group.add(
		svg_document.line(
			start=(x+CELL_SIZE,y), end=(x,y+CELL_SIZE)
		)
		.stroke(BLACK, width=GRID_THICKNESS)
		.dasharray([1,1], offset="75%")
	)
	return group


def num_circle(x,y,val, fill="white"):
	group = svg_document.g(
		id='num_circle_{}_{}'.format(x, y)
	)
	x = x*CELL_SIZE
	y = y*CELL_SIZE
	group.add(
		svg_document.circle(
			center = (x, y),
			r = RADIUS,
			fill = fill,
		)
		.stroke(BLACK, width=GRID_THICKNESS*2)
	)
	group.add(
		svg_document.text(
			str(val),
			x = [x],
			y = [y + TEXT_VERTICAL_OFFSET],
			text_anchor = "middle",
			font_family = "sans-serif",
			font_size = 4,
			font_weight = "bold",
		)
		.fill(BLACK if fill=="white" else "white")
	)
	return group

def line(x,y,w,h, color=BLACK, thickness=GRID_THICKNESS):
	return (
		svg_document.line(
			start=(x*CELL_SIZE,  y*CELL_SIZE),
			end=  ((x+w)*CELL_SIZE, (y+h)*CELL_SIZE),
		)
		.stroke(color, width=thickness)
	)

def circle(x,y,r, fill="white", thickness=1):
	return (
		svg_document.circle(
			center=(x*CELL_SIZE, y*CELL_SIZE),
			r=r,
			fill=fill,
		)
		.stroke(BLACK if fill=="white" else "white", width=thickness)
	)

def rect(x,y,w,h, fill="white", thickness=1):
	return (
		svg_document.rect(
			insert = (x*CELL_SIZE, y*CELL_SIZE),
			size   = (w*CELL_SIZE, h*CELL_SIZE),
			fill = fill,
		)
		.stroke(BLACK, width=thickness)
	)

# puts a character in the middle of a cell
def character(x,y,char, fill=BLACK):
	return (
		svg_document.text(
			char,
			x = [x*CELL_SIZE + CELL_SIZE/2],
			y = [y*CELL_SIZE + TEXT_VERTICAL_OFFSET*2 + CELL_SIZE/2],
			text_anchor = "middle",
			font_family = "sans-serif",
			font_size = 8,
			font_weight = "bold",
		)
		.fill(fill)
	)



svg_document = svgwrite.Drawing(
	filename = "out.svg",
	size = ("{}px".format(WIDTH*CELL_SIZE), "{}px".format(HEIGHT*CELL_SIZE))
)

lines = svg_document.add(
	svg_document.g(id='lines')
		.stroke(GRID_COLOR, width=GRID_THICKNESS)
		.dasharray([1,1])
)
for idx_x in range(WIDTH + 1):
	lines.add(
		svg_document.line(
			start=(idx_x*CELL_SIZE,0), end=(idx_x*CELL_SIZE,HEIGHT*CELL_SIZE)
		)
	)
for idx_y in range(HEIGHT + 1):
	lines.add(
		svg_document.line(
			start=(0,idx_y*CELL_SIZE), end=(WIDTH*CELL_SIZE,idx_y*CELL_SIZE)
		)
	)

for idx in range(int((HEIGHT - 3)/2)):
	svg_document.add(cross_box(2, 2 + idx*2))

DAY_OFFSET=11
DAY_WIDTH=9
Y_OFFSET=6
LINE_T=0.5

svg_document.add(line(DAY_OFFSET,             1, DAY_WIDTH*7, 0, thickness=LINE_T))
svg_document.add(line(DAY_OFFSET, Y_OFFSET     , DAY_WIDTH*7, 0, thickness=LINE_T))
svg_document.add(line(DAY_OFFSET, Y_OFFSET +  6, DAY_WIDTH*7, 0, thickness=LINE_T))
svg_document.add(line(DAY_OFFSET, Y_OFFSET + 28, DAY_WIDTH*7, 0, thickness=LINE_T))

svg_document.add(line(DAY_OFFSET, Y_OFFSET + 50, DAY_WIDTH*7, 0, thickness=LINE_T))
svg_document.add(line(DAY_OFFSET, Y_OFFSET + 52, DAY_WIDTH*7, 0, thickness=LINE_T))
svg_document.add(line(DAY_OFFSET, Y_OFFSET + 54, DAY_WIDTH*7, 0, thickness=LINE_T))
svg_document.add(line(DAY_OFFSET, Y_OFFSET + 56, DAY_WIDTH*7, 0, thickness=LINE_T))

for ea_day in range(7):
	x = ea_day*DAY_WIDTH + DAY_OFFSET

	# date header
	svg_document.add(rect(x,1, DAY_WIDTH,3, thickness=LINE_T))
	svg_document.add(
		svg_document.text(
			"jan 01",
			x = [(x+0.5)*CELL_SIZE],
			y = [(3+0.5)*CELL_SIZE],
			font_family = "sans-serif",
			font_size = 16,
			font_weight = "bold",
		)
		.fill(BLACK)
	)

	# extra bits and bobs
	svg_document.add(line(x, 1, 0, 61, thickness=LINE_T))
	for idx, ea_char in enumerate("☼☁☂☇☃"):
		svg_document.add(character(x+idx,4, ea_char))
	for idx, ea_char in enumerate("hms"):
		svg_document.add(character(x,53+idx, ea_char))
	svg_document.add(character(x,57, "☼"))
	svg_document.add(character(x,59, "☼"))
	svg_document.add(rect(x,61,1,1, fill=BLACK, thickness=GRID_THICKNESS))
	svg_document.add(character(x,61, "★", fill="white"))

	# number line
	y_off = Y_OFFSET
	svg_document.add(line(x, y_off, 0, 8, thickness=2))
	svg_document.add(line(x, 33.5, 0, 48-33.5, thickness=2))

	for ea_hr in range(7):
		svg_document.add(num_circle(x, ea_hr + y_off, ea_hr, fill=BLACK))
	y_off = Y_OFFSET - 6
	for ea_hr in range(7, 25):
		svg_document.add(line(x, ea_hr*2 + y_off, DAY_WIDTH, 0, thickness=LINE_T))
		fill = BLACK if ea_hr >= 17 else "white"
		svg_document.add(circle(x,ea_hr*2 + y_off-1,1, thickness=0.5))
		svg_document.add(num_circle(x, ea_hr*2 + y_off, ea_hr, fill=fill))

svg_document.add(line(DAY_WIDTH*7 + DAY_OFFSET, 1, 0, 61, thickness=LINE_T))

svg_document.save()
