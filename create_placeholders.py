from PIL import Image, ImageDraw

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

def create_simple_sprite(width, height, color, shape, filename):
    """Creates a simple sprite with a specific shape and color."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(img)

    if shape == "rectangle":
        draw.rectangle([(2, 2), (width - 2, height - 2)], fill=color)
    elif shape == "triangle":
        points = [(width / 2, 2), (width - 2, height - 2), (2, height - 2)]
        draw.polygon(points, fill=color)
    elif shape == "circle": # Though not requested, good to have for A1 if triangle is too simple
        draw.ellipse([(2, 2), (width - 2, height - 2)], fill=color)


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
    create_simple_sprite(
        width=32,
        height=32,
        color=(0, 0, 255),  # Blue
        shape="rectangle",
        filename=art_dir + "pixel_paradox_placeholder.png"
    )

    # 3. A1 Holographic Sprite (Placeholder)
    create_simple_sprite(
        width=16,
        height=16,
        color=(0, 255, 255),  # Cyan
        shape="triangle",
        filename=art_dir + "a1_hologram_placeholder.png"
    )
