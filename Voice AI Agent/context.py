from pathlib import Path
import json


def load_context():
    """Load all files from context directory"""
    context_dir = Path("agentFile")
    context_dir.mkdir(exist_ok=True)

    all_content = ""
    for file_path in context_dir.glob("*"):
        if file_path.is_file():
            try:
                content = file_path.read_text(encoding='utf-8')
                all_content += f"\n=== {file_path.name} ===\n{content}\n"
            except:
                pass

    return all_content.strip() or "No files found"


print(load_context())
print("Context is ready")
