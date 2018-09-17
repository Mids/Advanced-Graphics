import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


def render(M, camAng):
	# enable depth test (we'll see details	later)
	glClear(GL_COLOR_BUFFER_BIT |
			GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glLoadIdentity()
	# use orthogonal projection (we'll see	details later)
	glOrtho(-1, 1, -1, 1, -1, 1)
	# rotate "camera" position to see this	3D space better (we'll see details later)
	gluLookAt(.1 * np.sin(camAng), .1, .1 * np.cos(camAng), 0, 0, 0, 0, 1, 0)
	# draw coordinate: x in red, y in	green, z in blue
	glBegin(GL_LINES)
	glColor3ub(255, 0, 0)
	glVertex3fv(np.array([0., 0., 0.]))
	glVertex3fv(np.array([1., 0., 0.]))
	glColor3ub(0, 255, 0)
	glVertex3fv(np.array([0., 0., 0.]))
	glVertex3fv(np.array([0., 1., 0.]))
	glColor3ub(0, 0, 255)
	glVertex3fv(np.array([0., 0., 0]))
	glVertex3fv(np.array([0., 0., 1.]))
	glEnd()
	# draw triangle
	glBegin(GL_TRIANGLES)
	glColor3ub(255, 255, 255)
	glVertex3fv((M @ np.array([.0, .5, 0., 1.]))[:-1])
	glVertex3fv((M @ np.array([.0, .0, 0., 1.]))[:-1])
	glVertex3fv((M @ np.array([.5, .0, 0., 1.]))[:-1])
	glEnd()


# # Affine
# def render(T):
# 	glClear(GL_COLOR_BUFFER_BIT)
# 	glLoadIdentity()
#
# 	# draw triangle
# 	glBegin(GL_TRIANGLES)
# 	glColor3ub(255, 255, 255)
# 	glVertex2fv((T @ np.array([0.0, 0.5, 1.]))[:-1])
# 	glVertex2fv((T @ np.array([0.0, 0.0, 1.]))[:-1])
# 	glVertex2fv((T @ np.array([0.5, 0.0, 1.]))[:-1])
# 	glEnd()

def main():
	# Initialize the library
	if not glfw.init():
		return
	# Create a Windowed mode window and its OpenGL context
	window = glfw.create_window(640, 480, "3D Trans", None, None)
	if not window:
		glfw.terminate()
		return

	# Make the window's context current
	glfw.make_context_current(window)

	# let's just skip - we'll see this later
	glfw.swap_interval(1)

	count = 0

	# Loop until the user closes the window
	while not glfw.window_should_close(window):
		# Poll events
		glfw.poll_events()

		# rotate 60 deg about x axis
		th = np.radians(-60)
		R = np.identity(4)
		R[:3, :3] = [[1., 0., 0.],
					 [0., np.cos(th), -np.sin(th)],
					 [0., np.sin(th), np.cos(th)]]
		# translate by (.4, 0., .2)
		T = np.identity(4)
		T[:3, 3] = [.4, 0., .2]

		camAng = np.radians(count % 360)
		render(R, camAng)
		# render(T, camAng)
		# render(T @ R, camAng)
		# render(R @ T, camAng)
		count += 1

		# Swap front and back buffers
		glfw.swap_buffers(window)

	glfw.terminate()


if __name__ == "__main__":
	main()
