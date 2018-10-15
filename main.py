# 2017124921 JungJin Park Assignment 4
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Global variable
gCamAng = 0.


def myLookAt(eye, at, up):  # eye, at, up are 1D numpy array of length 3
    global gCamAng
    forward = eye - at
    forward = forward/np.sqrt(np.dot(forward, forward))

    side = np.cross(up, forward)
    side = side/np.sqrt(np.dot(side, side))

    up = np.cross(forward, side)

    pos = np.array([-np.dot(eye, side), -np.dot(eye, up), -np.dot(eye, forward)])

    viewMatrix = np.array([[side[0], up[0], forward[0], 0.0],
                          [side[1], up[1], forward[1], 0.0],
                          [side[2], up[2], forward[2], 0.0],
                          [pos[0], pos[1], pos[2], 1.0]])

    glMultMatrixf(viewMatrix)


def render(camAng):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -10, 10)

    # rotate "camera" position (right-multiply the current matrix by viewing matrix)
    # try to change parameters
    # gluLookAt(1 * np.sin(camAng), 1, 1 * np.cos(camAng), 0, 0, 0, 0, 1, 0)
    myLookAt(np.array([1 * np.sin(camAng), 1, 1 * np.cos(camAng)]), np.array([0, 0, 0]), np.array([0, 1, 0]))

    # draw coordinates
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


def key_callback(window, key, scancode, action, mods):
    global gCamAng
    # rotate the camera when 1 or 3 key is pressed or repeated
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key == glfw.KEY_3:
            gCamAng += np.radians(10)


def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, 'Lecture7', None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(gCamAng)
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
