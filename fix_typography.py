import re

filepath = "index.html"
with open(filepath, "r") as f:
    html = f.read()

# 1. Update .skill-tag CSS to Dark Mode
skill_old = """                    .skill-tag {
                        padding: 0.25rem 0.75rem;
                        background-color: #f1f5f9;
                        color: #475569;
                        border-radius: 9999px;
                        font-size: 0.75rem;
                        font-weight: 500;
                        border: 1px solid #e2e8f0;
                        transition: all 0.2s;
                        cursor: default;
                    }
                    .skill-tag:hover {
                        background-color: #e2e8f0;
                        transform: translateY(-1px);
                    }"""

skill_new = """                    .skill-tag {
                        padding: 0.25rem 0.75rem;
                        background-color: #141414;
                        color: #a3a3a3;
                        border-radius: 9999px;
                        font-size: 0.75rem;
                        font-family: 'JetBrains Mono', monospace;
                        font-weight: 600;
                        border: 1px solid #262626;
                        transition: all 0.2s;
                        cursor: default;
                    }
                    .skill-tag:hover {
                        background-color: rgba(234, 88, 12, 0.1);
                        color: #ea580c;
                        border-color: #ea580c;
                        transform: translateY(-1px);
                        box-shadow: 0 0 10px rgba(234, 88, 12, 0.2);
                    }
                    
                    /* Sidebar Minimal Bold Fonts */
                    .nav-btn {
                        font-family: 'JetBrains Mono', monospace;
                        font-size: 0.8rem;
                        font-weight: 700;
                        text-transform: uppercase;
                        letter-spacing: 0.05em;
                    }
                    .mob-nav-btn {
                        font-family: 'JetBrains Mono', monospace;
                        font-size: 0.8rem;
                        font-weight: 700;
                        text-transform: uppercase;
                        letter-spacing: 0.05em;
                    }"""

html = html.replace(skill_old, skill_new)

# 2. Let's make sure the Contact Email/LinkedIn on the sidebar are also minimal bold
# We have id="contact" sections on the sidebar.
# The user wants "more Bold and minimal fonts on the side bar".
sidebar_contact_title = '<span class="text-xs font-semibold text-neutral-500 uppercase tracking-wider mb-4 block">Contact</span>'
# Maybe we can add a global sidebar heading rule if needed, but it's already bold + uppercase. 
# We'll just write it back.

with open(filepath, "w") as f:
    f.write(html)

print("Typography and skill tags updated successfully.")
