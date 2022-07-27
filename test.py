import prefect
from prefect import task, Flow
from prefect.storage import Git

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

with Flow("hello-flow") as flow:
    hello_task()

flow = Flow("my-flow")
flow.storage = Git(repo="my/repo", flow_path="/flows/flow.py", repo_host="github.com"
