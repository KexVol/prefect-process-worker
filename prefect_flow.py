# prefect_flow.py

from prefect import flow, task
import socket
import subprocess
import sys
import pygetwindow as gw

@flow(log_prints=True)
def run_external_python():
    print("111111")
    python_executable = sys.executable
    result = subprocess.run([python_executable, "playwright_script.py"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    hostname = socket.gethostname()
    print(f"Hostname: {hostname}")

    # 获取所有窗口
    windows = gw.getAllTitles()

    # 查找包含 "Google" 的窗口
    for window_title in windows:
        if "Google" in window_title:
            window = gw.getWindowsWithTitle(window_title)[0]
            window.activate()  # 将窗口置于最前面
            break

if __name__ == "__main__":
    # Create a deployment for the flow from a Git repository source
    # .from_source() specifies where Prefect should get the flow code from
    run_external_python.from_source(
        # The Git repository containing the flow code
        source="https://github.com/KexVol/prefect-process-worker.git",
        # The path to the flow function within the repository
        # Format is: file_path:function_name
        entrypoint="prefect_flow.py:run_external_python"
    ).deploy(
        # Configure the deployment settings
        # The name that will identify this deployment in the Prefect UI
        name="run_external_python",
        # The work pool that will execute this deployment
        # Must match an existing work pool name in your Prefect server
        work_pool_name="my-process-worker",
        # Tags help organize and filter deployments
        # 'local' tag indicates this is for local development
        tags=["local"]
    )
