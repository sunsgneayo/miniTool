#!/user/bin/env python

import os
import ffmpeg


# 遍历目录下的mp4文件，生成封面gif
def process_mp4_files_in_dir(directory):
    print(f'process_mp4_files_in_dir:{directory}')
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                input_file = os.path.join(root, file)
                # 输出文件名（可以添加前缀、后缀或改变扩展名）  
                base, ext = os.path.splitext(file)
                output_file = os.path.join(root, f"{base}_converted.gif")

                # 注意：ffmpeg-python 提供了更高级别的API，但你也可以直接使用命令行参数  
                (
                    ffmpeg
                    .input(input_file, ss=0, t=3)
                    .output(output_file, vf='fps=15,scale=320:-1:flags=lanczos', vcodec='gif')
                    .run()
                )
                print(f"Processed {input_file} to {output_file}")



if '__main__'==__name__:
    input_path = input("please set video dir:")
    print(input_path)

    process_mp4_files_in_dir(input_path)
    input("Tip: press Enter , close window!")
