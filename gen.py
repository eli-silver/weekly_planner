#!/usr/bin/env python3

CELL_SIZE = 10;
HEIGHT = 5;
WIDTH = 5;
GRID_THICKNESS = 0.3
RADIUS = 6

import svgwrite


def cross_box(x,y):
	group = svg_document.add(
		svg_document.g(
			id='cross_box_{}_{}'.format(x, y)
		)
	)
	x = x*CELL_SIZE
	y = y*CELL_SIZE
	group.add(
		svg_document.rect(
			insert = (x, y),
			size = (CELL_SIZE, CELL_SIZE),
			fill = "#000000",
			fill_opacity = 0,
		)
		.stroke("black", width=GRID_THICKNESS*2)
	)
	group.add(
		svg_document.line(
			start=(x,y), end=(x+CELL_SIZE,y+CELL_SIZE)
		)
		.stroke("black", width=GRID_THICKNESS)
		.dasharray([1,1], offset="75%")
	)
	group.add(
		svg_document.line(
			start=(x+CELL_SIZE,y), end=(x,y+CELL_SIZE)
		)
		.stroke("black", width=GRID_THICKNESS)
		.dasharray([1,1], offset="75%")
	)


def num_circle(x,y,val, filled=False, fill="white"):
	group = svg_document.add(
		svg_document.g(
			id='num_circle_{}_{}'.format(x, y)
		)
	)
	x = x*CELL_SIZE
	y = y*CELL_SIZE
	group.add(
		svg_document.circle(
			center = (x, y),
			r = RADIUS,
			fill = fill,
		)
		.stroke("black", width=GRID_THICKNESS*2)
	)
	group.add(
		svg_document.text(
			str(val),
			x = [x],
			y = [y],
			text_anchor = "middle",
			text_anchor_y = "middle",
			dominant_baseline = "central",
		)
	)






svg_document = svgwrite.Drawing(
	filename = "out.svg",
	size = ("{}px".format(WIDTH*CELL_SIZE), "{}px".format(HEIGHT*CELL_SIZE))
)

lines = svg_document.add(
	svg_document.g(id='lines')
		.stroke("black", width=GRID_THICKNESS)
		.dasharray([1,1])
)
for idx_x in range(WIDTH + 1):
	lines.add(
		svg_document.line(start=(idx_x*CELL_SIZE,-0.5), end=(idx_x*CELL_SIZE,HEIGHT*CELL_SIZE))
	)
for idx_y in range(HEIGHT + 1):
	lines.add(
		svg_document.line(start=(-0.5,idx_y*CELL_SIZE), end=(WIDTH*CELL_SIZE,idx_y*CELL_SIZE))
	)

cross_box(1,1)
#num_circle(3,1, 3)

#path = svg_document.path()
#
#x_start = 0
#y_start = conf.height/2 + conf.thickness/2
#
#r_out = conf.width/2 + conf.thickness/2
#x_out_end = r_out
#y_out_end = -r_out
#
#vy1 = 0
#h_x = conf.width/2 - conf.thickness/2
#vy2 = conf.height/2 - r_out + conf.thickness/2
#
#r_in = conf.width/2 - conf.thickness/2
#x_in_end = -r_in
#y_in_end = r_in
#
#if self.horizontal:
#	x_start = conf.width - x_start
#	x_out_end = -x_out_end
#	x_in_end = -x_in_end
#	h_x = conf.width - h_x
#if self.vertical:
#	y_start = conf.height - y_start
#	y_out_end = -y_out_end
#	y_in_end = -y_in_end
#	vy1 = conf.height - vy1
#	vy2 = conf.height - vy2
#
#angle_dir = '-' if self.vertical == self.horizontal else '+'
#inv_angle_dir = '+' if self.vertical == self.horizontal else '-'
#
#path.push("M", x_start, y_start)
#path.push_arc((x_out_end, y_out_end), 90, r_out, large_arc = False, angle_dir = angle_dir)
#path.push("V", vy1)
#path.push("H", h_x)
#path.push("V", vy2)
#path.push_arc((x_in_end, y_in_end), 90, r_in, large_arc = False, angle_dir = inv_angle_dir)
#svg_document.add(path)

svg_document.save()
