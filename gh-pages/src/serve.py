from fasthtml.common import *
import subprocess

# Note: In the future this will be a PyPi module.

def serve_dev(
    app='app',
    host='0.0.0.0',
    port=None,
    reload=True,
    reload_includes=None,
    reload_excludes=None,
    sqlite_port=8035,
    db=False,
    db_path='data/app.db',
    jupyter=False,
    jupyter_port=8036,
    tw=False,
    tw_src='./app.css',
    tw_dist='./public/app.css'
):
    import inspect
    frame = inspect.currentframe().f_back
    module = inspect.getmodule(frame)
    
    # Check if this is the main module
    if module.__name__ != '__main__':
        return

    appname = module.__name__

    if db:
        print("Starting SQLite...")
        sqlite_process = subprocess.Popen(
            ['sqlite_web', db_path, '--port', str(sqlite_port), '--no-browser'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f'SQLite: http://localhost:{sqlite_port}')

    if jupyter:
        print("Starting Jupyter...")
        jupyter_process = subprocess.Popen(
            ['jupyter', 'lab', '--port', str(jupyter_port), '--no-browser', '--NotebookApp.token=', '--NotebookApp.password='],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
            text=True
        )

        # Extract and print the Jupyter Lab URL
        for line in jupyter_process.stderr:
            if 'http://' in line:
                match = re.search(r'(http://localhost:\d+/lab)', line)
                if match:
                    print(f'Jupyter Lab: {match.group(1)}')
                    break

    if tw:
        print("Starting Tailwind...")
        tailwind_process = subprocess.Popen(
            ['tailwindcss', '-i', tw_src, '-o', tw_dist, '--watch'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    try:
        print("Starting FastHTML...")
        serve(appname=appname, app=app, host=host, port=port, reload=reload, reload_includes=reload_includes, reload_excludes=reload_excludes)
    finally:
        if db:
            sqlite_process.terminate()
        if jupyter:
            jupyter_process.terminate()
        if tw:
            tailwind_process.terminate()
