import os
import re

def comment_plt_show(directory):
    """
    Recursively search for Python files in the given directory and comment out plt.show() statements
    """
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    # Read the file content
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Use regex to find and replace plt.show() with # plt.show()
                    # This pattern looks for plt.show() that isn't already commented
                    new_content = re.sub(r'(?<!\#\s?)plt\.show\(\)', r'# plt.show()', content)
                    
                    # If changes were made, write the file back
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
                        print(f"Updated: {filepath}")
                except Exception as e:
                    print(f"Error processing {filepath}: {str(e)}")
    
    return count

if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))
    updated_count = comment_plt_show(project_dir)
    print(f"\nTotal files updated: {updated_count}")
