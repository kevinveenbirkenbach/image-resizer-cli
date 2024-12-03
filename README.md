# 📷 Image Resizer CLI

A lightweight and powerful command-line tool for resizing images, designed to tackle the challenge of super huge photo files that are too big to upload to platforms like PixelFed. Simplify your workflow by resizing images quickly and easily! 🚀

## 🛠 Features

- 🌟 Resize images by percentage (e.g., 75%)
- 📐 Resize to maximum dimensions (width/height)
- 💾 Adjust images to fit a specific file size (e.g., 500KB, 2MB)
- 🖼️ Support for single images or entire folders
- 🗂️ Automatically saves resized files with a `_resized` suffix

---

## 🏗️ Why This Script?

This tool was created after frequently receiving super huge photo files that were too large to upload to **PixelFed**. Instead of manually resizing them, this script automates the process and ensures the files are optimized for upload.

---

## 📋 Prerequisites

Make sure you have the following installed:

1. **Python 3.6+**
2. **Pillow** (Python Imaging Library)

Install Pillow using pip:
```bash
pip install pillow
```

---

## 📥 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/image-resizer-cli.git
   ```
2. Navigate to the folder:
   ```bash
   cd image-resizer-cli
   ```

---

## 🚀 Usage

The script is saved as `main.py`. Run it using Python:

### Resize a single image:
```bash
python main.py path/to/image.jpg --percentage 75
```

### Resize all images in a folder:
```bash
python main.py path/to/folder --max-width 800 --max-height 600
```

### Resize to fit within 500KB:
```bash
python main.py path/to/image.jpg --max-size 500KB
```

### Options:
- `--percentage`: Resize by percentage (e.g., 75 for 75%)
- `--max-width`: Maximum width in pixels
- `--max-height`: Maximum height in pixels
- `--max-size`: Target file size (e.g., `500KB`, `2MB`)

### Output:
- Resized files will automatically include the `_resized` suffix.
- For folders, a new folder named `<original_folder>_resized` is created.

---

## 🧑‍💻 Author

Created by **Kevin Veen-Birkenbach** with the help of **ChatGPT**  
🌐 [cybermaster.space](https://cybermaster.space/)  

This script was developed in collaboration with OpenAI's ChatGPT. You can view the conversation that led to its creation [here](https://chatgpt.com/share/674f246d-661c-800f-a2e5-9ae920bcd03b).

---

## 📜 License

This script is licensed under the **GNU Affero General Public License, Version 3, 19 November 2007**.  
For more details, see the [LICENSE file](https://www.gnu.org/licenses/agpl-3.0.en.html).

---

## 🛠️ Contributions

Feel free to fork, contribute, and submit pull requests. Let’s make image resizing even better! 😊
