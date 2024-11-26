# prefect_flow.py
from prefect import flow, task
import socket
import subprocess
import sys

@flow(log_prints=True)
def run_external_python():
    print("0run_external_python")
    python_executable = sys.executable
    result = subprocess.run([python_executable, "playwright_script.py"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    hostname = socket.gethostname()
    print(f"Hostname: {hostname}")

# def playwright_process(input_value: int = 10):
#     """Main flow that orchestrates data processing tasks"""
#     run_playwright_script()
#     print(f"start")
#     return {"result"}

if __name__ == "__main__":
    # Create a deployment for the flow from a Git repository source
    # .from_source() specifies where Prefect should get the flow code from
    run_external_python.from_source(
        # The Git repository containing the flow code
        source="https://github.com/KexVol/prefect-process-worker.git",
        # The path to the flow function within the repository
        # Format is: file_path:function_name
        entrypoint="prefect_flow.py:run_playwright_script"
    ).deploy(
        # Configure the deployment settings
        # The name that will identify this deployment in the Prefect UI
        name="get-hostname",
        # The work pool that will execute this deployment
        # Must match an existing work pool name in your Prefect server
        work_pool_name="my-process-worker",
        # Tags help organize and filter deployments
        # 'local' tag indicates this is for local development
        tags=["local"]
    )
