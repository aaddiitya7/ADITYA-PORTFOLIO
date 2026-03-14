import re

filepath = "index.html"
with open(filepath, "r") as f:
    html = f.read()

# 1. Cards styling updates
# Change background of cards from bg-[#141414] (previously bg-white) to pure `#111` or `#141414` but with neon hover.
# Add neon hover to .anim-card elements:
# We find class="..." and if it contains anim-card, we ensure it has the hover classes.
# The user wants "subtle orange" (#ea580c is orange-600, #f97316 is orange-500)
# A subtle dark bento border: border-neutral-800 hover:border-orange-500/50 hover:shadow-[0_0_15px_rgba(249,115,22,0.15)]
# Let's just do a specific replace for the common card classes:
html = html.replace('bg-[#141414] border border-neutral-200 shadow-sm', 'bg-[#141414] border border-neutral-800 shadow-sm hover:border-orange-500/50 hover:shadow-[0_0_15px_rgba(249,115,22,0.15)] transition-all duration-300')

html = html.replace('bg-[#141414] rounded-2xl border border-neutral-150', 'bg-[#141414] rounded-2xl border border-neutral-800 hover:border-orange-500/50 hover:shadow-[0_0_15px_rgba(249,115,22,0.15)] transition-all duration-300')
html = html.replace('bg-[#141414] border border-neutral-800 shadow-sm', 'bg-[#141414] border border-neutral-800 shadow-none hover:border-orange-500/50 hover:shadow-[0_0_15px_rgba(249,115,22,0.15)] transition-all duration-300')

# Also for the case study header bar
html = html.replace('bg-[#0f172a] hover:bg-neutral-800', 'bg-[#141414] hover:bg-neutral-900')

# 2. Fix some specific colors that got wrongly converted
# border-neutral-150 -> border-neutral-800
html = html.replace('border-neutral-150', 'border-neutral-800')
# border-neutral-200 -> border-neutral-800
html = html.replace('border-neutral-200', 'border-neutral-800')

# 3. Echo shadows for H2 elements (Brutalist style)
# class="anim-heading text-3xl font-black mb-10 text-neutral-900" -> this was converted to text-white.
html = html.replace('class="anim-heading text-3xl font-black mb-10 text-white"', 'class="anim-heading text-4xl font-black mb-10 text-white uppercase tracking-tighter drop-shadow-[2px_2px_0_rgba(249,115,22,0.3)]"')
html = html.replace('class="anim-heading text-2xl md:text-3xl font-black mb-1 text-white"', 'class="anim-heading text-3xl md:text-4xl font-black mb-1 text-white uppercase tracking-tighter drop-shadow-[2px_2px_0_rgba(249,115,22,0.3)]"')

with open(filepath, "w") as f:
    f.write(html)
print("Bento fix completed.")
