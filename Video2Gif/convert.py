# !/user/bin/env python

import os
import subprocess

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
                output_file = os.path.join(root, f"{base}_convert.mp4")
                command = [
                    'ffmpeg',
                    '-i', input_file,
                    '-movflags', 'faststart',
                    output_file
                ]

                # 运行FFmpeg命令
                try:
                    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print(f"成功将moov原子移动到{output_file}的前面。")
                except subprocess.CalledProcessError as e:
                    # 如果FFmpeg命令失败，打印错误信息
                    print(f"处理文件时发生错误: {e}")
                    print("FFmpeg的stderr输出:", e.stderr.decode())

if '__main__' == __name__:
    input_path = input("处理压缩视频格式--请输入视频文件路径:")
    print(input_path)

    process_mp4_files_in_dir(input_path)
    input("Tip: 按Enter键关闭窗口...")
