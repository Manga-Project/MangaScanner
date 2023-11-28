import argparse

from pathlib import Path
from PIL import Image
from tqdm import tqdm

def get_args():
    parser = argparse.ArgumentParser(description='Manga Image Collector')
    parser.add_argument('--input_path', '-i', type=str, metavar='FILE', 
                        default='E:\\User\\Pictures\\ControlCenter4\\Scan', help='Path to image')
    parser.add_argument('--width',  '-w', type=int, help='Width of image')
    parser.add_argument('--height', '-he', type=int, help='Height of image')
    parser.add_argument('--crop_x', '-x', type=int, help='Height of image')
    parser.add_argument('--crop_y', '-y', type=int, help='Height of image')
    parser.add_argument('--chapter','-c', type=int, help='第幾話 Chapter')
    parser.add_argument('--volume', '-v', type=int, help='第幾集 Volume')
    parser.add_argument('--manga_name',   '-n', type=str, help='Manga\'s name')
    parser.add_argument('--reversed', action='store_true', help="If manga is scanned in reversed order (雙數頁面使用).")
    parser.add_argument('--output_path', '-o', type=str, metavar='FILE', default="E:\\Datasets\\Manga\\AppendManga", help='Path to output mangas')
    parser.add_argument('--target_ext', '-t', type=str, default='.tif', help='Path to output mangas')
    parser.add_argument('--delete_scanned', action='store_true', help="If delete collected manga image.")
    return parser.parse_args()

def main():
    args = get_args()

    # List image files with target extension
    image_files = list(Path(args.input_path).glob(f'*{args.target_ext}'))
    image_files.sort()
    image_count = len(image_files)
    
    output_dir = Path(args.output_path) / f"{args.manga_name}/{args.volume}/{args.chapter}/OriginSizeManga"
    output_dir.mkdir(parents=True, exist_ok=True)

    for idx, image_file in tqdm(enumerate(image_files), total=image_count):
        image = Image.open(image_file)
        image = image.crop((args.crop_x, args.crop_y, args.crop_x + args.width, args.crop_y + args.height))

        image_id = idx * 2 + 1
        if args.reversed:
            image_id = (image_count - idx) * 2
        image.save(output_dir / f"{args.manga_name}_{args.volume}_{args.chapter}_{image_id}.png")

        if args.delete_scanned:
            image_file.unlink()

if __name__ == '__main__':
    main()