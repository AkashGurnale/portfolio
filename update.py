import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1, 2, 3: Meta tags, Open Graph, Twitter, JSON-LD
old_meta = """    <title>Akash Gurnale | Lead Software Engineer</title>
    <meta name="description" content="Portfolio of Akash Gurnale, Lead Software Engineer with 7+ years of experience in native iOS and cross-platform development, building scalable BFSI products used by millions.">
    <meta name="keywords" content="Akash Gurnale, iOS Developer, Lead Software Engineer, Swift, SwiftUI, Flutter, Portfolio">
    <meta name="author" content="Akash Gurnale">
    <meta property="og:title" content="Akash Gurnale | Lead Software Engineer">
    <meta property="og:description" content="7+ years of experience building scalable consumer and BFSI products used by millions.">
    <meta property="og:type" content="website">"""

new_meta = """    <title>Akash Gurnale | Lead Software Engineer | Fintech Systems</title>
    <meta name="description" content="Lead Software Engineer with 7+ years experience building scalable fintech platforms used by 16M+ users. Focus on system design, performance, mobile + cloud.">
    <meta name="keywords" content="lead software engineer, fintech, system design, scalable systems, iOS, Swift, Flutter, backend">
    <meta name="author" content="Akash Gurnale">
    
    <!-- Open Graph -->
    <meta property="og:title" content="Akash Gurnale | Lead Software Engineer | Fintech Systems">
    <meta property="og:description" content="Lead Software Engineer with 7+ years experience building scalable fintech platforms used by 16M+ users. Focus on system design, performance, mobile + cloud.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://akashgurnale.com/">
    <meta property="og:image" content="https://akashgurnale.com/akash-gurnale-lead-software-engineer.jpg">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Akash Gurnale | Lead Software Engineer | Fintech Systems">
    <meta name="twitter:description" content="Lead Software Engineer with 7+ years experience building scalable fintech platforms used by 16M+ users. Focus on system design, performance, mobile + cloud.">
    <meta name="twitter:image" content="https://akashgurnale.com/akash-gurnale-lead-software-engineer.jpg">

    <!-- Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "Person",
      "name": "Akash Gurnale",
      "jobTitle": "Lead Software Engineer",
      "description": "Lead Software Engineer with 7+ years experience building scalable fintech platforms used by 16M+ users. Focus on system design, performance, mobile + cloud.",
      "worksFor": {
        "@type": "Organization",
        "name": "Bajaj Finserv Direct"
      },
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Pune",
        "addressCountry": "India"
      },
      "sameAs": [
        "https://linkedin.com/in/akash-gurnale",
        "https://github.com/AkashGurnale"
      ]
    }
    </script>"""

content = content.replace(old_meta, new_meta)

# 4. H1 & h2 adjustments
# Hero H1
old_hero_h1 = """                    <h1 class="hero-title fade-in">
                        <span class="hero-greeting">Hello, I'm</span>
                        <span class="hero-name">Akash Gurnale</span>
                    </h1>
                    <p class="hero-subtitle fade-in">Lead Software Engineer</p>"""
new_hero_h1 = """                    <div class="hero-title fade-in" style="font-size: var(--sz-h1); font-weight: 700; line-height: 1.1; margin-bottom: var(--space-4);">
                        <span class="hero-greeting" style="display: block; font-size: var(--sz-xl); color: var(--text-secondary); font-weight: 500; margin-bottom: var(--space-2);">Hello, I'm</span>
                        <span class="hero-name" style="background: var(--gradient-primary); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Akash Gurnale</span>
                    </div>
                    <h1 class="hero-subtitle fade-in" style="font-size: var(--sz-2xl); font-weight: 600; color: var(--text-primary);">Lead Software Engineer</h1>"""
content = content.replace(old_hero_h1, new_hero_h1)

# h2: About
content = content.replace('<h2 class="section-title">Crafting Digital Experiences</h2>', '<h2 class="section-title">About</h2>')
# h2: Experience
content = content.replace('<h2 class="section-title">Work Experience</h2>', '<h2 class="section-title">Experience</h2>')
# h2: Selected Work (Projects)
content = content.replace('<h2 class="section-title">Key Projects</h2>', '<h2 class="section-title">Selected Work</h2>')
# h2: Contact
content = content.replace('<h2 class="section-title">Let\'s Work Together</h2>', '<h2 class="section-title">Contact</h2>')
# h2: Impact (We will use Stats/Skills section or create a new one. Let's rename Skills & Technologies to Impact)
content = content.replace('<h2 class="section-title">Skills & Technologies</h2>', '<h2 class="section-title">Impact</h2>')


# 5 & 10. Content & GEO updates
old_hero_desc = """                    <p class="hero-description fade-in">
                        Native iOS &amp; Cross-Platform Developer with <strong>7+ years</strong> of experience building scalable products used by <strong>millions</strong>. Currently leading engineering at Bajaj Markets.
                    </p>"""
new_hero_desc = """                    <p class="hero-description fade-in">
                        I am a Lead Software Engineer with <strong>7+ years</strong> of experience building scalable systems and fintech platforms. I currently lead engineering at Bajaj Markets, optimizing system design and performance for <strong>16M+ users</strong> across iOS, Flutter, and backend services.
                    </p>"""
content = content.replace(old_hero_desc, new_hero_desc)

old_about_text = """                <div class="about-text fade-in">
                    <p>
                        I'm a Lead Software Engineer with a passion for building products that make a difference. With over 7 years in the industry, I've had the privilege of working on large-scale applications that serve millions of users across the BFSI sector.
                    </p>
                    <p>
                        Currently, I lead engineering initiatives at <strong>Bajaj Markets</strong>, an award-winning fintech platform with <strong>16M+ users</strong>. My work spans architecture design, performance optimization, team mentorship, and driving innovation through AI-powered features.
                    </p>
                    <p>
                        I believe great software is a blend of solid engineering, thoughtful design, and relentless attention to detail. Whether it's modernizing legacy codebases or prototyping cutting-edge AI modules, I bring the same commitment to quality.
                    </p>
                </div>"""
new_about_text = """                <div class="about-text fade-in">
                    <p>
                        I am a Lead Software Engineer with 7+ years of experience designing scalable systems and building high-performance fintech platforms. My core tech focus is on mobile architectures, system design, and performance optimization.
                    </p>
                    <p>
                        Currently, I lead engineering initiatives at <strong>Bajaj Markets</strong>, an enterprise fintech platform that processes large volumes of transactions for <strong>16M+ users</strong>. I specialize in cross-platform integrations, ensuring robust cloud architectures, and mentoring high-performing engineering teams.
                    </p>
                    <p>
                        My work revolves around solving complex engineering challenges, delivering scalable infrastructure, and optimizing frontend-to-backend data flows to provide seamless user experiences.
                    </p>
                </div>"""
content = content.replace(old_about_text, new_about_text)

# 6 Images
content = content.replace('src="profile.jpg" alt="Akash Gurnale"', 'src="akash-gurnale-lead-software-engineer.jpg" alt="Akash Gurnale - Lead Software Engineer Profile" loading="lazy"')

# 7. Performance (defer script)
content = content.replace('<script src="script.js"></script>', '<script src="script.js" defer></script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done index.html updates")
