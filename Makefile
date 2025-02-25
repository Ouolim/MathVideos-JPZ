# Default values for the file and folder
FILE := basic.py
FOLDER := basic

# Define the target directory based on the folder variable
TARGET_DIR := build/$(FOLDER)

# Set resolution
LOW_RES = 1920x1080
HIGH_RES = 3840x2160

# Set the quality flags
LOW_QUALITY = -pql
HIGH_QUALITY = -pqh

low: $(TARGET_DIR)
	@mkdir -p $(TARGET_DIR)
	source .venv/bin/activate && python3 -m manim $(LOW_QUALITY) $(FOLDER)/$(FILE) --media_dir $(TARGET_DIR)

# Target for high quality render of $(FILE)
finished: $(TARGET_DIR)
	@mkdir -p $(TARGET_DIR)
	source .venv/bin/activate && python3 -m manim $(HIGH_QUALITY) $(FOLDER)/$(FILE)

# Default rule
basic: low

$(TARGET_DIR):
	@mkdir -p $(TARGET_DIR)