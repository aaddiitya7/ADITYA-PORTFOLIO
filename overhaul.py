import re

filepath = "index.html"
with open(filepath, "r") as f:
    html = f.read()

# 1. Animate ADITYA SINGH in the sidebar
name_old = """<h1 class="text-2xl font-bold tracking-wider mb-1 text-orange-400">ADITYA SINGH</h1>"""
name_new = """<h1 class="text-2xl font-black tracking-wider mb-1 name-glitch-anim bg-gradient-to-r from-orange-400 via-orange-500 to-orange-400 bg-clip-text text-transparent" style="font-family: 'Plus Jakarta Sans', sans-serif;">ADITYA SINGH</h1>"""
html = html.replace(name_old, name_new)

# Add CSS for name-glitch-anim 
css_anim = """
                    @keyframes nameShine {
                        0% { background-position: 200% center; }
                        100% { background-position: -200% center; }
                    }
                    .name-glitch-anim {
                        background-size: 200% auto;
                        animation: nameShine 5s linear infinite;
                    }
"""
if "@keyframes nameShine" not in html:
    html = html.replace("/* Sidebar Minimal Bold Fonts */", css_anim + "/* Sidebar Minimal Bold Fonts */")

# 2. Executive Summary - Overhaul stray styling (bg-red-50 -> orange styles)
html = html.replace('bg-red-50 ', 'bg-orange-600/10 ')
html = html.replace('group-hover:bg-red-100', 'group-hover:bg-orange-600/20')
html = html.replace('bg-[#1f1f1f]', 'bg-neutral-800/50')
html = html.replace('group-hover:bg-neutral-200', 'group-hover:bg-neutral-800')

# Executive summary skill pills: convert raw tailwind utility to `.skill-tag`
pill_old = 'class="px-3 py-1 bg-white/10 text-neutral-300 text-xs rounded-full border border-white/10"'
pill_new = 'class="skill-tag"'
html = html.replace(pill_old, pill_new)

# 3. Standardize Bento UI hover effects everywhere
# Convert border-neutral-100 to border-neutral-800
html = html.replace('border-neutral-100', 'border-neutral-800')

# Card hover upgrades to bento style:
# Find any div with bg-[#141414] or bg-[#1a1a1a] that has border-neutral-800 and add the orange hover
html = html.replace('border border-neutral-800 shadow-sm hover:shadow-md transition-shadow', 
                    'border border-neutral-800 transition-all duration-300 hover:border-orange-600/50 hover:shadow-[0_0_15px_rgba(234,88,12,0.15)]')

html = html.replace('border border-neutral-800 flex justify-center',
                    'border border-neutral-800 transition-all duration-300 hover:border-orange-600/50 hover:shadow-[0_0_15px_rgba(234,88,12,0.15)] flex justify-center')

# Overhaul the general cards
html = html.replace('hover:-translate-y-1 hover:shadow-xl transition-all duration-300 flex items-start',
                    'hover:-translate-y-1 border border-neutral-800 transition-all duration-300 hover:border-orange-600/50 hover:shadow-[0_0_15px_rgba(234,88,12,0.15)] flex items-start')

with open(filepath, "w") as f:
    f.write(html)

print("Overhaul complete.")
