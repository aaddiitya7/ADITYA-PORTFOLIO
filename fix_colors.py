import re

filepath = "index.html"
with open(filepath, "r") as f:
    html = f.read()

# 1. Global subtle orange replacement
# The user wants the orange (#f97316 / orange-500) to be more subtle. We'll use #ea580c (Tailwind orange-600)
html = html.replace('#f97316', '#ea580c')
html = html.replace('orange-500', 'orange-600')
# Adjust hover states to be relative
html = html.replace('orange-600/50', 'orange-600/40')

# 2. Radar Chart (Skills) fixes
radar_old = """skillsChartInstance = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['SEO', 'Consumer Psychology', 'AI Web Gen', 'Prompt Engineering', 'Data Analysis via AI', 'Ads Management'],
                    datasets: [{
                        label: 'Proficiency Level',
                        data: [90, 85, 75, 80, 70, 65],
                        fill: true,
                        backgroundColor: 'rgba(220, 38, 38, 0.1)', // Orange transparent
                        borderColor: 'rgb(220, 38, 38)',
                        pointBackgroundColor: 'rgb(220, 38, 38)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgb(220, 38, 38)'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            angleLines: { display: true },
                            suggestedMin: 0,
                            suggestedMax: 100,
                            grid: { color: 'rgba(0,0,0,0.05)' },
                            pointLabels: {
                                font: { size: 12, weight: 'bold' },
                                color: '#475569'
                            }
                        }
                    },"""

radar_new = """skillsChartInstance = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['SEO', 'Consumer Psychology', 'AI Web Gen', 'Prompt Engineering', 'Data Analysis via AI', 'Ads Management'],
                    datasets: [{
                        label: 'Proficiency Level',
                        data: [90, 85, 75, 80, 70, 65],
                        fill: true,
                        backgroundColor: 'rgba(234, 88, 12, 0.15)', // Subtle Orange transparent
                        borderColor: 'rgb(234, 88, 12)',
                        pointBackgroundColor: 'rgb(234, 88, 12)',
                        pointBorderColor: '#1a1a1a',
                        pointHoverBackgroundColor: '#1a1a1a',
                        pointHoverBorderColor: 'rgb(234, 88, 12)'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            angleLines: { display: true, color: 'rgba(255, 255, 255, 0.1)' },
                            suggestedMin: 0,
                            suggestedMax: 100,
                            grid: { color: 'rgba(255, 255, 255, 0.1)' },
                            pointLabels: {
                                font: { size: 11, weight: 'bold', family: 'JetBrains Mono' },
                                color: '#a3a3a3'
                            },
                            ticks: { display: false }
                        }
                    },"""
html = html.replace(radar_old, radar_new)

# 3. Bar Chart (Experience) fixes
bar_old = """expChartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Freelance', 'Amazon Seller', 'Aglo Bond Intern'],
                    datasets: [{
                        label: 'Business Impact Score',
                        data: [75, 85, 65],
                        backgroundColor: [
                            'rgba(115, 115, 115, 0.7)', // Emerald
                            'rgba(23, 23, 23, 0.9)', // Blue
                            'rgba(220, 38, 38, 0.8)'  // Orange
                        ],
                        borderColor: [
                            'rgb(115, 115, 115)',
                            'rgb(23, 23, 23)',
                            'rgb(220, 38, 38)'
                        ],"""

bar_new = """expChartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Freelance', 'Amazon Seller', 'Aglo Bond Intern'],
                    datasets: [{
                        label: 'Business Impact Score',
                        data: [75, 85, 65],
                        backgroundColor: [
                            'rgba(64, 64, 64, 0.8)', // Neutral 700
                            'rgba(38, 38, 38, 0.9)', // Neutral 800
                            'rgba(234, 88, 12, 0.8)'  // Subtle Orange
                        ],
                        borderColor: [
                            'rgb(82, 82, 82)',
                            'rgb(64, 64, 64)',
                            'rgb(234, 88, 12)'
                        ],"""
html = html.replace(bar_old, bar_new)

bar_opts_old = """options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            display: false,
                            grid: { display: false }
                        },
                        x: {
                            grid: { display: false }
                        }
                    },"""
bar_opts_new = """options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            display: false,
                            grid: { display: false }
                        },
                        x: {
                            grid: { display: false },
                            ticks: { color: '#a3a3a3', font: { family: 'JetBrains Mono', size: 10 } }
                        }
                    },"""
html = html.replace(bar_opts_old, bar_opts_new)

# 4. Doughnut Chart (Certs) fixes
doughnut_old = """certsChartInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Google', 'Universities', 'Other Inst.'],
                    datasets: [{
                        data: [4, 3, 2],
                        backgroundColor: [
                            '#171717', // Google Blue
                            '#ea580c', // Orange (already replaced above)
                            '#737373'  // Emerald
                        ],"""
doughnut_new = """certsChartInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Google', 'Universities', 'Other Inst.'],
                    datasets: [{
                        data: [4, 3, 2],
                        backgroundColor: [
                            '#262626', // Neutral 800
                            '#ea580c', // Subtle Orange
                            '#525252'  // Neutral 600
                        ],"""
html = html.replace(doughnut_old, doughnut_new)

doughnut_opts_old = """options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom' }
                    }
                }"""
doughnut_opts_new = """options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { 
                            position: 'bottom',
                            labels: { color: '#a3a3a3', font: { family: 'JetBrains Mono', size: 10 } }
                        }
                    }
                }"""
html = html.replace(doughnut_opts_old, doughnut_opts_new)

with open(filepath, "w") as f:
    f.write(html)
print("Charts and colors updated.")
