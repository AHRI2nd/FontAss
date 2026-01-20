import glob
import os

def batch_change_font(target_font="SUITE-SemiBold"):
    ass_files = glob.glob('**/*.ass', recursive=True)
    
    if not ass_files:
        print("처리할 .ass 파일이 없습니다.")
        return

    print(f"총 {len(ass_files)}개의 파일을 찾았습니다.")

    for file_path in ass_files:
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()

            new_lines = []
            is_styles_section = False

            for line in lines:
                if line.strip() == '[V4+ Styles]':
                    is_styles_section = True
                elif line.startswith('[') and is_styles_section:
                    is_styles_section = False

                if is_styles_section and line.startswith('Style:'):
                    parts = line.split(',')
                    if len(parts) > 1:
                        parts[1] = target_font
                        line = ','.join(parts)
                
                new_lines.append(line)

            with open(file_path, 'w', encoding='utf-8-sig') as f:
                f.writelines(new_lines)
            
            print(f"성공: {file_path}")

        except Exception as e:
            print(f"실패: {file_path} (에러: {e})")

if __name__ == "__main__":
    batch_change_font("SUITE-SemiBold")