import glob, os
from blur_out_faces import blur_out_faces


if __name__ == "__main__":
    # blur_out_faces('IMG_1424.JPG','out.jpg', 4)
    input_root = r"H:\workspace\blur-out-face\data\test_inputs"
    output_root = r"H:\workspace\blur-out-face\data\test_outputs"
    
    for subdir, dirs, files in os.walk(input_root):
        for file in files:
            input_dir = subdir
            output_dir = input_dir.replace(input_root, output_root)
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            blur_out_faces(input_path, output_path, 99)
            # print(output_dir, file)
    