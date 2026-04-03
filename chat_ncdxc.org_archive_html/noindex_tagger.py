import os

# The tag that stops Google, Bing, and AI crawlers
TAG = '\n    <meta name="robots" content="noindex, nofollow">\n'

def add_noindex(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()

                # Don't add it if it's already there
                if any('content="noindex' in line for line in lines):
                    continue

                # Find the <head> tag and insert after it
                new_content = []
                added = False
                for line in lines:
                    new_content.append(line)
                    if not added and '<head>' in line.lower():
                        new_content.append(TAG)
                        added = True
                
                # If no <head> was found, prepend it to the top
                if not added:
                    new_content.insert(0, TAG)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(new_content)
                count += 1
    print(f"Done! Successfully tagged {count} files.")

if __name__ == "__main__":
    add_noindex('.')