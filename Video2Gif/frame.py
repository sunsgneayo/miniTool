# !/user/bin/env python

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
                output_file = os.path.join(root, f"{base}.png")
                (
                    ffmpeg
                    .input(input_file, ss=0)  # ss=0表示从视频开始处提取，vframes=1表示只提取一帧
                    .output(output_file, vframes=1, vcodec='png')  # 指定输出格式为png
                    .run()
                )
                print(f"Processed {input_file} to {output_file}")


if '__main__' == __name__:
    input_path = input("输入视频文件路径:")
    print(input_path)

    process_mp4_files_in_dir(input_path)
    input("Tip: 按Enter键关闭窗口...")
