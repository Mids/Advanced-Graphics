# 2017124921 JungJin Park Assignment 3-1
import glfw
from OpenGL.GL import *
import numpy as np

# Global variable
gComposedM = np.identity(3)


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
    glVertex2fv((T @ np.array([0.0, 0.5, 1.]))[:-1])
    glVertex2fv((T @ np.array([0.0, 0.0, 1.]))[:-1])
    glVertex2fv((T @ np.array([0.5, 0.0, 1.]))[:-1])
    glEnd()


def key_callback(window, key, scancode, action, mods):
    if action != glfw.PRESS: return

    global gComposedM
    newM = np.identity(3)

    if key == glfw.KEY_Q:  # Translate by -0.1 in x direction w.r.t. global coordinate
        newM = np.array([[1, 0, -0.1], [0, 1, 0], [0, 0, 1]])
        gComposedM = newM @ gComposedM

    elif key == glfw.KEY_E:  # Translate by 0.1 in x direction w.r.t. global coordinate
        newM = np.array([[1, 0, 0.1], [0, 1, 0], [0, 0, 1]])
        gComposedM = newM @ gComposedM

    elif key == glfw.KEY_A:  # Rotate by 10 degrees counterclockwise w.r.t global coordinate
        th = np.radians(10)
        newM = np.array([[np.cos(th), -np.sin(th), 0], [np.sin(th), np.cos(th), 0], [0, 0, 1]])
        gComposedM = gComposedM @ newM

    elif key == glfw.KEY_D:  # Rotate by 10 degrees clockwise w.r.t global coordinate
        th = np.radians(-10)
        newM = np.array([[np.cos(th), -np.sin(th), 0], [np.sin(th), np.cos(th), 0], [0, 0, 1]])
        gComposedM = gComposedM @ newM

    elif key == glfw.KEY_1:  # Reset the triangle with identity matrix
        gComposedM = np.identity(3)

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
