import os
import sys
from PIL import Image

def convert_to_webp(input_path, output_path):
    try:
        # 尝试以图片形式打开文件
        with Image.open(input_path) as img:
            # 如果是RGBA模式，转换为RGB模式（WebP不支持RGBA）
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            # 保存为WebP格式，质量设为80（可调整）
            img.save(output_path, 'WEBP', quality=80)
            return True
    except Exception as e:
        print(f"无法转换文件 {input_path}: {str(e)}")
        return False

def main():
    # 获取当前脚本文件名
    script_name = os.path.basename(__file__)
    
    # 获取当前目录下所有文件
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    converted_count = 0
    skipped_count = 0
    
    for filename in files:
        # 跳过脚本文件本身
        if filename == script_name:
            continue
            
        # 构造输出文件名（保持原名，仅修改扩展名）
        base_name, ext = os.path.splitext(filename)
        output_filename = base_name + '.webp'
        
        # 如果输出文件已存在，跳过
        if os.path.exists(output_filename):
            print(f"文件 {output_filename} 已存在，跳过转换")
            skipped_count += 1
            continue
            
        # 尝试转换文件
        print(f"正在转换: {filename} -> {output_filename}")
        if convert_to_webp(filename, output_filename):
            converted_count += 1
        else:
            skipped_count += 1
    
    print(f"\n转换完成！")
    print(f"成功转换: {converted_count} 个文件")
    print(f"跳过: {skipped_count} 个文件")

if __name__ == "__main__":
    main()