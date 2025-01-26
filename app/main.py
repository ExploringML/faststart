from fasthtml.common import *
from serve import serve_dev
from time import time
from datetime import datetime

DEV_MODE=True

cb = f"?v={int(time())}" if DEV_MODE else "" # CSS cache buster

app,rt = fast_app(
	pico=False,
    live=True,
    hdrs=(
        Link(rel="stylesheet", href=f"/public/app.css{cb}", type="text/css"),
    )
)

#@rt('/')
#def get(): return Div(P('Hello World!'), cls="text-red-400 p-2 bg-pink-300")

def Feature(icon, title, description):
    return Div(
        Div(
            Div(icon, cls="text-indigo-500 text-2xl mb-4"),
            H3(title, cls="text-lg font-semibold text-gray-900 mb-2"),
            P(description, cls="text-gray-600"),
            cls="p-6"
        ),
        cls="bg-white rounded-lg shadow-sm hover:shadow-md transition duration-200"
    )

def Features():
    features = [
        ("🚀", "Instant Setup", 
         "Get started in minutes with a pre-configured FastHTML and Tailwind CSS environment"),
        ("🔄", "Live Reload", 
         "See your Python and CSS changes instantly with automatic page updates"),
        ("🎨", "TailwindCSS Integration", 
         "Write modern, responsive CSS with zero configuration needed"),
        ("⚡", "HTMX Ready", 
         "Build dynamic interfaces without writing JavaScript"),
        ("🛠️", "Development Optimized", 
         "CSS and Python hot-reloading, with automatic cache busting"),
        ("📱", "Responsive by Default", 
         "Mobile-first design patterns built into the template"),
    ]
    
    return Div(
        Div(
            H2("Why Use This Template?", 
               cls="text-3xl font-bold text-center mb-4 text-gray-900"),
            P("Everything you need to build modern web apps with Python", 
              cls="text-xl text-gray-600 text-center mb-12"),
            Div(
                *[Feature(icon, title, desc) for icon, title, desc in features],
                cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
            ),
            cls="max-w-6xl mx-auto px-4"
        ),
        cls="py-16 bg-gradient-to-b from-slate-50 to-white"
    )

def GithubIcon():
    return NotStr("""<svg viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4">
        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>""")

def HtmxIcon():
    return NotStr("""<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" id="Htmx--Streamline-Simple-Icons" height="24" width="24"><desc>Htmx Streamline Icon: https://streamlinehq.com</desc><title>htmx</title><path d="M0 13.01v-2l7.09 -2.98 0.58 1.94 -5.1 2.05 5.16 2.05 -0.63 1.9Zm16.37 1.03 5.18 -2 -5.16 -2.09 0.65 -1.88L24 10.95v2.12L17 16zm-2.85 -9.98H16l-5.47 15.88H8.05Z" fill="#000000" stroke-width="1"></path></svg>""")

def TailwindIcon():
    return NotStr("""<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32"><title>file_type_tailwind</title><path d="M9,13.7q1.4-5.6,7-5.6c5.6,0,6.3,4.2,9.1,4.9q2.8.7,4.9-2.1-1.4,5.6-7,5.6c-5.6,0-6.3-4.2-9.1-4.9Q11.1,10.9,9,13.7ZM2,22.1q1.4-5.6,7-5.6c5.6,0,6.3,4.2,9.1,4.9q2.8.7,4.9-2.1-1.4,5.6-7,5.6c-5.6,0-6.3-4.2-9.1-4.9Q4.1,19.3,2,22.1Z" style="fill:#44a8b3"/></svg>""")

def Badge(text, color="indigo", icon=None, svg=None):
    return Span(
        *([Span(svg, cls="inline-flex items-center relative -mt-[1px]")] if svg else [icon, " "] if icon else []) + [text],
        cls=f"inline-flex items-center gap-1 px-4 py-2 h-[32px] text-sm font-medium text-{color}-600 bg-{color}-50 rounded-full"
    )

def HeroBadges():
    return Div(
        Badge("🚀 Production Ready"),
        A(Badge("GitHub", svg=GithubIcon()), 
          href="https://github.com/yourusername/fasthtml-tailwind-starter",
          cls="ml-2 hover:opacity-90 transition-opacity"),
        Badge("TailwindCSS v4", svg=TailwindIcon()),
        Badge("🐍 Python"),
        Badge("HTMX Ready", svg=HtmxIcon()),
        cls="flex flex-wrap justify-center gap-2 my-12"
    )

def Hero():
    return Div(
        Div(
            Div(
                HeroBadges(),
                # Main heading with gradient text
                H1(
                    Span("FastHTML + TailwindCSS", 
                         cls="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600"),
                    Span(" Boilerplate", 
                         cls="text-gray-900"),
                    cls="text-5xl font-extrabold tracking-tight text-center mt-20 mb-16"
                ),
                
                # Subheading with better description
                P("Use the power and flexibility of FastHTML and TailwindCSS to build modern Python web apps with automatic CSS and Python hot-reloading. Zero configuration required.", 
                  cls="max-w-xl mx-auto text-xl text-gray-600 mb-10 text-center leading-relaxed"),
                
                # CTA buttons with better styling
                Div(
                    A(Div(
                        Span("Get Started"),
                        Span("→", cls="ml-2 text-lg"),
                        cls="inline-flex items-center"
                      ), 
                      href="https://github.com/yourusername/fasthtml-tailwind-starter",
                      cls="inline-flex items-center px-8 py-3 text-base font-medium text-white bg-gradient-to-r from-indigo-600 to-purple-600 rounded-lg hover:opacity-90 transition duration-300"),
                    cls="flex justify-center space-x-4"
                ),        
                QuickStart()
            )
        )
    )

def QuickStart():
    return Div(
        Div(
            H2("Quick Start", cls="text-2xl font-bold mb-6 text-gray-900"),
            Pre("""git clone https://github.com/yourusername/fasthtml-tailwind-starter
pip install -r requirements.txt
python main.py""",
                cls="bg-gray-800 text-gray-200 p-4 rounded-lg font-mono text-sm"
            ),
            cls="max-w-2xl mx-auto"
        ),
        cls="pt-16 pb-22 container mx-auto px-4"
    )

@rt('/')
def get():
    return Div(
        Hero(),
        Features(),
        Footer(
            Div(
                P(f"© {datetime.now().year} Created with ❤️ by David Gwyer using FastHTML, Python, HTMX, and TailwindCSS!",
                cls="text-gray-600 text-center"),
                cls="container mx-auto px-4 py-8"
            ),
            cls="mt-16"
        )
    )

if DEV_MODE: serve_dev(tw=True)
else: serve()