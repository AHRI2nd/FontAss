cd "$(dirname "$0")"


python3 << END
import glob
import os

target_font = "SUITE-SemiBold"
ass_files = glob.glob('**/*.ass', recursive=True)

for file_path in ass_files:
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
        
        new_lines = []
        is_styles = False
        for line in lines:
            if line.strip() == '[V4+ Styles]': is_styles = True
            elif line.startswith('['): is_styles = False
            
            if is_styles and line.startswith('Style:'):
                parts = line.split(',')
                if len(parts) > 1:
                    parts[1] = target_font
                    line = ','.join(parts)
            new_lines.append(line)
            
        with open(file_path, 'w', encoding='utf-8-sig') as f:
            f.writelines(new_lines)
        print(f"Success: {file_path}")
    except Exception as e:
        print(f"Error {file_path}: {e}")
END

echo "Done."