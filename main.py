# 2017124921 JungJin Park Assignment 3-2
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Global variable
gCamAng = 0.


def drawBox():
    glBegin(GL_QUADS)
    glVertex3fv(np.array([1, 1, 0.]))
    glVertex3fv(np.array([-1, 1, 0.]))
    glVertex3fv(np.array([-1, -1, 0.]))
    glVertex3fv(np.array([1, -1, 0.]))
    glEnd()


def drawTriangleTransformedBy(M):
    glBegin(GL_TRIANGLES)
    glVertex3fv((M @ np.array([.0, .5, 0., 1.]))[:-1])
    glVertex3fv((M @ np.array([.0, .0, 0., 1.]))[:-1])
    glVertex3fv((M @ np.array([.5, .0, 0., 1.]))[:-1])
    glEnd()


def drawTriangle():
    glBegin(GL_TRIANGLES)
    glVertex3fv(np.array([.0, .5, 0.]))
    glVertex3fv(np.array([.0, .0, 0.]))
    glVertex3fv(np.array([.5, .0, 0.]))
    glEnd()


def drawFrame():
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


def render(camAng, count):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    # set the current matrix to the identity matrix
    glLoadIdentity()

    # use orthogonal projection (multiply the current matrix by "projection" matrix - we'll see details later)
    glOrtho(-1, 1, -1, 1, -1, 1)

    # rotate "camera" position (multiply the current matrix by "projection" matrix - we'll see details later)
    gluLookAt(.1 * np.sin(camAng), .1, .1 * np.cos(camAng), 0, 0, 0, 0, 1, 0)

    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([1., 0., 0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([0., 1., 0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([0., 0., 1.]))
    glEnd()

    ###############################################
    # edit here

    # blue base transformation
    glPushMatrix()
    glTranslatef(-.5 + (count % 360) * .003, 0, 0)
    drawFrame()

    # blue base drawing
    glPushMatrix()
    glScalef(.2, .2, .2)
    glColor3ub(0, 0, 255)
    drawBox()
    glPopMatrix()

    # red arm transformation
    glPushMatrix()
    glRotatef(count % 360, 0, 0, 1)
    glTranslatef(.5, 0, .01)
    drawFrame()

    # red arm drawing
    glPushMatrix()
    glScalef(.5, .1, .1)
    glColor3ub(255, 0, 0)
    drawBox()
    glPopMatrix()

    # green arm transformation
    glPushMatrix()
    glTranslate(.5, 0, .01)
    glRotatef(count % 360, 0, 0, 1)
    drawFrame()

    # green arm drawing
    glPushMatrix()
    glScalef(.2, .2, .2)
    glColor3ub(0, 255, 0)
    drawBox()
    glPopMatrix()

    glPopMatrix()
    glPopMatrix()
    glPopMatrix()


def key_callback(window, key, scancode, action, mods):
    global gCamAng
    # rotate the camera when 1 or 3 key is pressed or repeated

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key == glfw.KEY_3:
            gCamAng += np.radians(10)

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

    # Make the window's context current
    glfw.make_context_current(window)

    # Key callback
    glfw.set_key_callback(window, key_callback)

    # let's just skip - we'll see this later
    glfw.swap_interval(1)

    count = 0
    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll events
        glfw.poll_events()

        render(gCamAng, count)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        count += 1

    glfw.terminate()


if __name__ == "__main__":
    main()
