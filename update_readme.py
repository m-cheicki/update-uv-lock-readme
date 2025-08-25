import re

import tomllib

# Load uv.lock (TOML format)
with open("uv.lock", "rb") as f:
    lock_data = tomllib.load(f)

# Extract packages from [[package]] sections
packages = lock_data.get("package", [])
dependencies = [(pkg["name"], pkg["version"]) for pkg in packages]

# Sort alphabetically
dependencies.sort(key=lambda x: x[0].lower())

# Generate Markdown table
md = "| Package | Version |\n|---------|---------|\n"
for name, ver in dependencies:
    md += f"| {name} | {ver} |\n"

# Read README
with open("README.md", "r") as f:
    readme = f.read()

# Replace section between markers
new_readme = re.sub(
    r"<!-- deps-start -->.*<!-- deps-end -->",
    f"<!-- deps-start -->\n{md}<!-- deps-end -->",
    readme,
    flags=re.DOTALL
)

# Save README
with open("README.md", "w") as f:
    f.write(new_readme)
