#!/usr/bin/env python3
"""
Skill Packager - Creates a distributable package of a skill
"""

import sys
import os
import shutil
import tarfile
import zipfile
from pathlib import Path

def package_skill(skill_path, output_format='zip'):
    """Package a skill directory into a compressed archive"""
    skill_path = Path(skill_path).resolve()
    if not skill_path.exists() or not skill_path.is_dir():
        print(f"❌ Error: Skill directory not found: {skill_path}")
        return None

    # Check for SKILL.md
    if not (skill_path / 'SKILL.md').exists():
        print(f"❌ Error: SKILL.md not found in {skill_path}")
        return None

    skill_name = skill_path.name
    output_filename = f"{skill_name}.{output_format}"
    
    print(f"📦 Packaging skill '{skill_name}'...")

    try:
        if output_format == 'zip':
            with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(skill_path):
                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(skill_path.parent)
                        zipf.write(file_path, arcname)
        elif output_format == 'tar.gz':
            with tarfile.open(f"{skill_name}.tar.gz", "w:gz") as tar:
                tar.add(skill_path, arcname=skill_name)
        else:
            print(f"❌ Error: Unsupported format '{output_format}'")
            return None
            
        print(f"✅ Created package: {output_filename}")
        return output_filename
    except Exception as e:
        print(f"❌ Error during packaging: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: package_skill.py <skill_directory> [--format zip|tar.gz]")
        sys.exit(1)
        
    skill_dir = sys.argv[1]
    fmt = 'zip'
    if len(sys.argv) > 3 and sys.argv[2] == '--format':
        fmt = sys.argv[3]
        
    package_skill(skill_dir, fmt)
