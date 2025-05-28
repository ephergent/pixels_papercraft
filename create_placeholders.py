from PIL import Image, ImageDraw

# Function to create a graph paper background
def create_graph_paper(width, height, grid_size, line_color, bg_color, filename):
    """Creates a graph paper image."""
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Draw vertical lines
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=line_color)

    # Draw horizontal lines
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=line_color)

    img.save(filename)
    print(f"Created {filename}")

# Function to create a sprite with a shape, color, grid overlay, and sketched border
def create_papercraft_sprite(width, height, color, shape, filename, grid_size=4, grid_color=(150, 150, 150, 100), border_color=(0, 0, 0, 255), border_width=2):
    """
    Creates a simple sprite with a specific shape and color,
    adds a subtle grid overlay, and a sketched border effect.
    """
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(img)

    # Draw the main shape
    if shape == "rectangle":
        draw.rectangle([(2, 2), (width - 2, height - 2)], fill=color)
    elif shape == "triangle":
        points = [(width / 2, 2), (width - 2, height - 2), (2, height - 2)]
        draw.polygon(points, fill=color)
    elif shape == "circle":
        draw.ellipse([(2, 2), (width - 2, height - 2)], fill=color)

    # Add subtle grid overlay
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=grid_color)
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=grid_color)

    # Add sketched border effect
    # This is a simplified "sketched" effect by drawing multiple slightly offset lines
    for i in range(border_width):
        # Top
        draw.line([(i, i), (width - 1 - i, i)], fill=border_color)
        # Bottom
        draw.line([(i, height - 1 - i), (width - 1 - i, height - 1 - i)], fill=border_color)
        # Left
        draw.line([(i, i), (i, height - 1 - i)], fill=border_color)
        # Right
        draw.line([(width - 1 - i, i), (width - 1 - i, height - 1 - i)], fill=border_color)

        # Add some slight "jitter" for a more hand-drawn feel (optional, but enhances effect)
        if i % 2 == 0:
            draw.line([(i + 1, i), (width - 2 - i, i)], fill=border_color) # Slight offset

    img.save(filename)
    print(f"Created {filename}")

if __name__ == "__main__":
    art_dir = "pixels-papercraft/assets/art/"

    # 1. Graph Paper Background
    create_graph_paper(
        width=1024,
        height=600,
        grid_size=20,
        line_color=(200, 200, 200),  # Light grey
        bg_color=(255, 255, 255),    # White
        filename=art_dir + "graph_paper_background.png"
    )

    # 2. Pixel Paradox Sprite (Placeholder)
    create_papercraft_sprite(
        width=32,
        height=32,
        color=(0, 0, 255),  # Blue
        shape="rectangle",
        filename=art_dir + "pixel_paradox_placeholder.png"
    )
    # 3. A1 Holographic Sprite (Placeholder)
    create_papercraft_sprite(
        width=16,
        height=16,
        color=(0, 255, 255),  # Cyan
        shape="triangle",
        filename=art_dir + "a1_hologram_placeholder.png"
    )

