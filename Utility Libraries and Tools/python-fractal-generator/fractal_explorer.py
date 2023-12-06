from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import sys
import matplotlib.pyplot as plt


class Fractal:
    def __init__(self, threshold, density):
        self.threshold = threshold
        self.density = density
        self.generate_axis()
        self.fractal = np.zeros((self.density, self.density))

    def generate_axis(self):
        self.real_min, self.real_max = -2, 1
        self.imag_min, self.imag_max = -1.5, 1.5
        self.real_axis = np.linspace(self.real_min, self.real_max, self.density)
        self.imaginary_axis = np.linspace(self.imag_min, self.imag_max, self.density)

    def count_iterations_until_divergent(self, c):
        z = c
        for i in range(self.threshold):
            z = z**2 + c
            if abs(z) > 2:
                return i
        return self.threshold

    def generate(self):
        for i in range(self.density):
            for j in range(self.density):
                c = complex(self.real_axis[j], self.imaginary_axis[i])
                self.fractal[i, j] = self.count_iterations_until_divergent(c)

    def plot(self, colormap="jet"):
        plt.imshow(self.fractal, cmap=colormap)
        plt.axis("off")
        plt.show()


class Mandelbrot(Fractal):
    def __init__(self, threshold, density):
        super().__init__(threshold, density)

    def count_iterations_until_divergent(self, c):
        z = c
        for i in range(self.threshold):
            z = z**2 + c
            if abs(z) > 2:
                return i
        return self.threshold


class Julia(Fractal):
    def __init__(self, threshold, density):
        super().__init__(threshold, density)
        self.c_real, self.c_imag = -0.74543, 0.11301
        self.real_min, self.real_max = -1.5, 1.5
        self.imag_min, self.imag_max = -1.5, 1.5

    def count_iterations_until_divergent(self, z):
        for i in range(self.threshold):
            z = z**2 + complex(self.c_real, self.c_imag)
            if abs(z) > 2:
                return i
        return self.threshold


class BurningShip(Fractal):
    def __init__(self, threshold, density):
        super().__init__(threshold, density)
        self.real_min, self.real_max = -2, 1
        self.imag_min, self.imag_max = -2, 2

    def count_iterations_until_divergent(self, c):
        z = 0 + 0j
        for i in range(self.threshold):
            z = (abs(z.real) + abs(z.imag) * 1j) ** 2 + c
            if abs(z) > 2:
                return i
        return self.threshold


class Tricorn(Fractal):
    def __init__(self, threshold, density):
        super().__init__(threshold, density)
        self.real_min, self.real_max = -2.5, 1.5
        self.imag_min, self.imag_max = -2, 2

    def count_iterations_until_divergent(self, c):
        z = c
        for i in range(self.threshold):
            z = np.conj(z) ** 2 + c
            if abs(z) > 2:
                return i
        return self.threshold


class Mandelbar(Fractal):
    def __init__(self, threshold, density):
        super().__init__(threshold, density)
        self.real_min, self.real_max = -2, 1
        self.imag_min, self.imag_max = -1.5, 1.5

    def count_iterations_until_divergent(self, c):
        z = c
        for i in range(self.threshold):
            z = np.conj(z) ** 2 + c
            if abs(z) > 2:
                return i
        return self.threshold


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fractal Explorer")

        # create the central widget and layout
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        layout = QtWidgets.QGridLayout()
        central.setLayout(layout)

        # create the input fields
        self.model_label = QtWidgets.QLabel("Fractal Model:")
        self.model_combo = QtWidgets.QComboBox()
        self.model_combo.addItem("Mandelbrot")
        self.model_combo.addItem("Julia")
        self.model_combo.addItem("Burning Ship")
        self.model_combo.addItem("Tricorn")
        self.model_combo.addItem("Mandelbar")

        self.threshold_label = QtWidgets.QLabel("Threshold:")
        self.threshold_input = QtWidgets.QLineEdit("100")

        self.density_label = QtWidgets.QLabel("Density:")
        self.density_input = QtWidgets.QLineEdit("1000")

        # add the input fields to the layout
        layout.addWidget(self.model_label, 0, 0)
        layout.addWidget(self.model_combo, 0, 1)

        layout.addWidget(self.threshold_label, 1, 0)
        layout.addWidget(self.threshold_input, 1, 1)

        layout.addWidget(self.density_label, 2, 0)
        layout.addWidget(self.density_input, 2, 1)

        # create the canvas for the fractal plot
        self.canvas = FigureCanvas(Figure(figsize=(8, 8)))
        layout.addWidget(self.canvas, 3, 0, 1, 2)

        # create the buttons to interact with the fractal plot
        self.plot_button = QtWidgets.QPushButton("Plot")
        self.reset_button = QtWidgets.QPushButton("Reset View")
        self.save_button = QtWidgets.QPushButton("Save Image")
        self.color_label = QtWidgets.QLabel("Colormap:")
        self.color_combo = QtWidgets.QComboBox()
        self.color_combo.addItem("hsv")
        self.color_combo.addItem("hot")
        self.color_combo.addItem("gray")
        self.color_combo.addItem("cool")
        self.color_combo.addItem("pink")

        layout.addWidget(self.plot_button, 4, 0)
        layout.addWidget(self.reset_button, 4, 1)
        layout.addWidget(self.save_button, 5, 0)
        layout.addWidget(self.color_label, 6, 0)
        layout.addWidget(self.color_combo, 6, 1)

        # connect the buttons to their actions
        self.plot_button.clicked.connect(self.plot_fractal)
        self.reset_button.clicked.connect(self.reset_view)
        self.save_button.clicked.connect(self.save_image)
        self.color_combo.currentIndexChanged.connect(self.update_colormap)

        # initialize the fractal model
        self.fractal = Mandelbrot(
            int(self.threshold_input.text()), int(self.density_input.text())
        )

    def plot_fractal(self):
        # update the fractal model with the current input values
        self.fractal.threshold = int(self.threshold_input.text())
        self.fractal.density = int(self.density_input.text())

        if self.model_combo.currentText() == "Mandelbrot":
            self.fractal = Mandelbrot(self.fractal.threshold, self.fractal.density)
        elif self.model_combo.currentText() == "Julia":
            self.fractal = Julia(self.fractal.threshold, self.fractal.density)
        elif self.model_combo.currentText() == "Burning Ship":
            self.fractal = BurningShip(self.fractal.threshold, self.fractal.density)
        elif self.model_combo.currentText() == "Tricorn":
            self.fractal = Tricorn(self.fractal.threshold, self.fractal.density)
        elif self.model_combo.currentText() == "Mandelbar":
            self.fractal = Mandelbar(self.fractal.threshold, self.fractal.density)

        # generate and plot the fractal
        self.fractal.generate()
        self.canvas.figure.clear()
        self.fractal.plot(colormap=self.color_combo.currentText())
        self.canvas.draw()

    def reset_view(self):
        # reset the fractal model and plot the fractal
        self.threshold_input.setText("100")
        self.density_input.setText("1000")

        self.fractal.reset()
        self.canvas.figure.clear()
        self.fractal.plot(colormap=self.color_combo.currentText())
        self.canvas.draw()

    def save_image(self):
        # open a file dialog to choose a filename and directory to save the image
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)", options=options
        )

        if filename:
            # update the fractal model with the current input values
            self.fractal.threshold = int(self.threshold_input.text())
            self.fractal.density = int(self.density_input.text())

            # generate and save the image
            self.fractal.generate()
            self.fractal.save_image(filename, colormap=self.color_combo.currentText())

    def change_color(self):
        # update the colormap of the fractal plot
        self.fractal.change_color(colormap=self.color_combo.currentText())
        self.canvas.draw()

    def update_colormap(self):
        self.fractal.plot(colormap=self.color_combo.currentText())
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
