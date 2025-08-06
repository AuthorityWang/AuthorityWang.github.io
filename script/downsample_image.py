from PIL import Image
import os
import argparse

def downscale_image(input_path, target_width):
    with Image.open(input_path) as img:
        width_percent = target_width / float(img.width)
        target_height = int(float(img.height) * float(width_percent))
        
        img_resized = img.resize((target_width, target_height), Image.LANCZOS)
        
        filename, ext = os.path.splitext(input_path)
        output_path = f"{filename}_downsampled{ext}"
        
        img_resized.save(output_path)
        print(f"Image saved to {output_path}")
        print(f"Old resolution: {img.width}x{img.height}")
        print(f"New resolution: {target_width}x{target_height}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='downsample')
    parser.add_argument('image', help='input path')
    parser.add_argument('width', type=int, help='target width')
    
    args = parser.parse_args()
    
    if args.width <= 0:
        raise ValueError("width should > 0")
    
    downscale_image(args.image, args.width)