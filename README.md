# 📷 Image Resizer CLI (imgrszr)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.en.html) [![GitHub stars](https://img.shields.io/github/stars/kevinveenbirkenbach/image-resizer-cli.svg?style=social)](https://github.com/kevinveenbirkenbach/image-resizer-cli/stargazers)

Image Resizer CLI is a lightweight and powerful command-line tool for resizing images, designed to tackle huge photo files that are too big to upload to platforms like PixelFed. Simplify your workflow by resizing images quickly and easily! 🚀

## 🛠 Features

- 🌟 Resize images by percentage (e.g., 75%)
- 📐 Resize to maximum dimensions (width/height)
- 💾 Adjust images to meet a specific file size (e.g., 500KB, 2MB)
- 🖼️ Support for processing a single image or an entire folder
- 🗂️ Automatically saves resized files with a `_resized` suffix or creates a new output folder

---

## 📥 Installation

Install Image Resizer CLI easily via [Kevin's Package Manager](https://github.com/kevinveenbirkenbach/package-manager) under the alias `imgrszr`:

```bash
package-manager install imgrszr
```

This command makes the tool globally available as `imgrszr` in your terminal. 🔧

---

## 🚀 Usage

Run the tool using the alias:

### Resize a single image:
```bash
imgrszr path/to/image.jpg --percentage 75
```

### Resize all images in a folder:
```bash
imgrszr path/to/folder --max-width 800 --max-height 600
```

### Resize an image to fit within 500KB:
```bash
imgrszr path/to/image.jpg --max-size 500KB
```

### Options:
- `--percentage`: Resize by percentage (e.g., 75 for 75%)
- `--max-width`: Maximum width in pixels
- `--max-height`: Maximum height in pixels
- `--max-size`: Target file size (e.g., `500KB`, `2MB`)

### Output:
- Resized files are saved with a `_resized` suffix.
- When processing folders, a new folder named `<original_folder>_resized` is created.

---

## 🧑‍💻 Author

Created by **Kevin Veen-Birkenbach** with the assistance of **ChatGPT**  
🌐 [cybermaster.space](https://cybermaster.space/)

---

## 📜 License

This project is licensed under the **GNU Affero General Public License, Version 3, 19 November 2007**.  
For more details, see the [LICENSE](https://www.gnu.org/licenses/agpl-3.0.en.html).

---

## 🤝 Contributions

Contributions are welcome! Feel free to fork, submit pull requests, and help us improve image resizing for everyone. 😊
