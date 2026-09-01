# 📝 Reflection - Level 3, Task 3: Neural Networks with TensorFlow/Keras

## 🎯 What I Did
For this final task, I built a neural network to classify handwritten digits using the MNIST dataset (70,000 images, 60,000 training / 10,000 testing). Before any modelling, I hit two real environment blockers: TensorFlow doesn't yet officially support Python 3.14 (the version used throughout this internship), and installing a second Python 3.12 environment then hit a Windows "long path" limit due to deeply nested internal TensorFlow files. Both were resolved by creating a virtual environment with Python 3.12 in a short, root-level path (C:\tfenv) rather than inside the deeply nested project folder.

I completed all 4 objectives:

- 🖼️ **Load and preprocess:** loaded MNIST directly via Keras, normalized pixel values from 0-255 down to 0-1, and flattened each 28x28 image into a single row of 784 numbers.
- 🧠 **Architecture design:** built a 3-layer Sequential neural network (128 neurons → 64 neurons → 10 output neurons with softmax), totalling 109,386 trainable parameters.
- 🏋️ **Training and evaluation:** trained for 10 epochs using the Adam optimizer, reaching 97.77% test accuracy. Plotted training vs validation accuracy/loss curves, which clearly showed overfitting starting around epoch 2-3 (training metrics kept improving while validation metrics plateaued or slightly worsened).
- 🎛️ **Hyperparameter tuning:** retrained a fresh model with only 3 epochs instead of 10, expecting this to reduce overfitting and match or improve test accuracy. It actually performed slightly worse (96.98% vs 97.77%), revealing that validation performance was still slowly improving even during the epochs where overfitting was visible, not purely plateaued.

## 💡 What I Learned
- ✅ Library compatibility issues (like TensorFlow not yet supporting a very new Python version) are a normal part of real data science work, and creating an isolated virtual environment with a different, compatible Python version is a standard, practical fix.
- ✅ Windows has a legacy 260-character file path limit that can break package installations with deeply nested files (like TensorFlow's), and the simplest fix is often shortening the install path rather than editing system registry settings.
- ✅ A neural network is built from stacked layers of connected neurons, with activation functions (ReLU for hidden layers, softmax for multi-category output) introducing the non-linearity needed to learn complex patterns.
- ✅ Backpropagation is the process of tracing prediction errors backward through the network to adjust each connection's weight, and Keras handles this automatically once the model is compiled with an optimizer and loss function.
- ✅ Comparing training vs validation accuracy/loss curves is the clearest way to visually detect overfitting, a growing gap between the two lines is the signal to watch for.
- ✅ A reasonable hypothesis for improving a model (stopping training earlier) does not always work as expected, and testing it honestly, including reporting when it makes things slightly worse, is more valuable than assuming a fix worked without checking.

## 🧗 Challenges I Faced
- TensorFlow failed to install entirely at first, traced back to Python 3.14 not yet being officially supported. Resolved by installing Python 3.12 alongside the existing installation and creating a dedicated virtual environment with it.
- The first attempt to create that virtual environment inside the project folder failed with a Windows long-path OSError, due to TensorFlow's deeply nested internal files combined with an already-long project folder path. Resolved by creating the environment at a short root-level path (C:\tfenv) instead.
- Manually tuning epochs down to 3 (based on reading the overfitting curves) did not improve test accuracy as expected, a genuine, honest finding rather than a clean success, which prompted a deeper look at why the validation curve wasn't a simple plateau.

## 🛠️ Tools Used
`Python 3.12 (isolated virtual environment)` · `TensorFlow` · `Keras` · `numpy` · `matplotlib` · `Jupyter Notebook`

---
*Level 3, Task 3 of the Codveda Data Science Internship - Advanced (Final Task)*