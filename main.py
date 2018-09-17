import glfw
from OpenGL.GL import *
import numpy as np

# Global variable
gComposedM = np.identity(2)


def render(T):
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	# draw cooridnate
	glBegin(GL_LINES)
	glColor3ub(255, 0, 0)
	glVertex2fv(np.array([0., 0.]))
	glVertex2fv(np.array([1., 0.]))
	glColor3ub(0, 255, 0)
	glVertex2fv(np.array([0., 0.]))
	glVertex2fv(np.array([0., 1.]))
	glEnd()
	# draw triangle
	glBegin(GL_TRIANGLES)
	glColor3ub(255, 255, 255)
	glVertex2fv(T @ np.array([0.0, 0.5]))
	glVertex2fv(T @ np.array([0.0, 0.0]))
	glVertex2fv(T @ np.array([0.5, 0.0]))
	glEnd()


def key_callback(window, key, scancode, action, mods):
	if action != glfw.PRESS: return

	global gComposedM
	newM = np.identity(2)

	if key == glfw.KEY_W:  # Scale by 0.9 times in x direction
		newM = np.array([[0.9, 0], [0, 1]])

	elif key == glfw.KEY_E:  # Scale by 1.1 times in x direction
		newM = np.array([[1.1, 0], [0, 1]])

	elif key == glfw.KEY_S:  # Rotate by 10 degrees counterclockwise
		th = np.radians(10)
		newM = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])

	elif key == glfw.KEY_D:  # Rotate by 10 degress clockwise
		th = np.radians(-10)
		newM = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])

	elif key == glfw.KEY_X:  # Shear by a factor of -0.1 in x direction
		newM = np.array([[1, -0.1], [0, 1]])

	elif key == glfw.KEY_C:  # Shear by a factor of 0.1 in x direction
		newM = np.array([[1, 0.1], [0, 1]])

	elif key == glfw.KEY_R:  # Reflection across x axis
		newM = np.array([[1, 0], [0, -1]])

	elif key == glfw.KEY_1:  # Reset the triangle with identity matrix
		gComposedM = np.identity(2)

	else:
		return

	gComposedM = newM @ gComposedM

	return


def main():
	# Initialize the library
	if not glfw.init():
		return
	# Create a Windowed mode window and its OpenGL context
	window = glfw.create_window(640, 480, "2017124921 JungJin Park", None, None)
	if not window:
		glfw.terminate()
		return

	# Key callback
	glfw.set_key_callback(window, key_callback)

	# Make the window's context current
	glfw.make_context_current(window)

	# let's just skip - we'll see this later
	glfw.swap_interval(1)

	# Loop until the user closes the window
	while not glfw.window_should_close(window):
		# Poll events
		glfw.poll_events()

		# Swap front and back buffers
		glfw.swap_buffers(window)

		render(gComposedM)

	glfw.terminate()


if __name__ == "__main__":
	main()
