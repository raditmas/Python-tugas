import glfw
from OpenGL.GL import *

def main():
    # Initialize GLFW
    if not glfw.init():
        print("Gagal untuk menginisialisasi GLFW")
        return

    window = glfw.create_window(800, 600, "Praktikum Grafika Komputer - Warna RGB", None, None)

    if not window:
        glfw.terminate()
        print("Gagal untuk membuat jendela GLFW")
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        # Set the clear color to a specific RGB value (e.g., red)
        glClearColor(1.0, 0.0, 0.0, 1.0)  # Red color
        glClear(GL_COLOR_BUFFER_BIT)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()