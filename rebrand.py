import re
import os

filepath = "index.html"
with open(filepath, "r") as f:
    html = f.read()

# 1. Fonts
html = html.replace(
    'family=Inter:wght@400;500;600;700;800&display=swap',
    'family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap'
)
html = html.replace("sans: ['Inter', 'sans-serif']", "sans: ['Plus Jakarta Sans', 'sans-serif'],\n                        mono: ['JetBrains Mono', 'monospace']")

# 2. Global Dark Mode Background & Text
html = html.replace('bg-[#fafafa]', 'bg-[#0a0a0a]')
html = html.replace('text-neutral-900', 'text-white')
html = html.replace('text-neutral-800', 'text-neutral-200')
html = html.replace('text-neutral-700', 'text-neutral-300')
html = html.replace('text-neutral-600', 'text-neutral-400')
html = html.replace('border-neutral-200', 'border-neutral-800')
html = html.replace('border-neutral-300', 'border-neutral-700')
html = html.replace('bg-white', 'bg-[#141414]')
html = html.replace('bg-neutral-50', 'bg-[#1a1a1a]')
html = html.replace('bg-neutral-100', 'bg-[#1f1f1f]')

# Special fixes for things that shouldn't be dark
# (Buttons that were white on dark might need fixing manually, but we'll see)
html = html.replace('bg-[#141414]/10', 'bg-white/10')
html = html.replace('border-[#141414]/20', 'border-white/20')

# 3. Orange Accents (Subtle Orange = Tailwind orange-500 / #f97316)
html = html.replace('red-500', 'orange-500')
html = html.replace('red-400', 'orange-400')
html = html.replace('red-600', 'orange-600')
html = html.replace('red-900', 'orange-900')
html = html.replace('#dc2626', '#f97316')
html = html.replace('#ef4444', '#f97316')
html = html.replace('#c92a2a', '#ea580c')
html = html.replace('#e53e3e', '#ea580c')

# 4. Particles Color
html = html.replace('Math.floor(Math.random() * 2000)}px #6b7280', 'Math.floor(Math.random() * 2000)}px #f97316')

# 5. Typewriter and Headings mono fonts
html = html.replace('class="text-[10px] font-bold', 'class="text-[10px] font-bold font-mono')
html = html.replace('class="text-[9px] text-neutral-500 uppercase', 'class="text-[9px] text-neutral-500 uppercase font-mono')
html = html.replace('text-xs text-orange-400 font-bold', 'text-xs text-orange-400 font-bold font-mono')

with open(filepath, "w") as f:
    f.write(html)

print("Rebrand script completed.")
